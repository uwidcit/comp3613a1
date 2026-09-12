"""Export docs/report.md to a PDF with the student's name and ID on the cover."""

from __future__ import annotations

import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from fpdf import FPDF

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REPORT = REPO_ROOT / "docs" / "report.md"
DEFAULT_PDF = REPO_ROOT / "docs" / "report.pdf"

_FONT_CANDIDATES = (
    (
        Path(r"C:\Windows\Fonts\arial.ttf"),
        Path(r"C:\Windows\Fonts\arialbd.ttf"),
    ),
    (
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
    ),
    (
        Path("/System/Library/Fonts/Supplemental/Arial.ttf"),
        Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf"),
    ),
)


def export_report(
    *,
    name: str,
    student_id: str,
    source: Path | None = None,
    output: Path | None = None,
) -> Path:
    """Write a PDF from the markdown report. Returns the output path."""
    src = source or DEFAULT_REPORT
    dest = output or DEFAULT_PDF
    if not src.is_file():
        raise SystemExit(
            f"Missing {src}. Co-draft docs/report.md first (Mermaid diagrams, "
            "wireframe image links), then re-run this command."
        )
    clean_name = name.strip()
    clean_id = student_id.strip()
    if not clean_name or not clean_id:
        raise SystemExit("Report export needs both --name and --id.")

    markdown = src.read_text(encoding="utf-8")
    app_url, logins = _require_marker_access(markdown)
    dest.parent.mkdir(parents=True, exist_ok=True)

    pdf = _new_pdf()
    _cover(pdf, clean_name, clean_id, app_url, logins)
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
        _body(pdf, markdown, src.parent, Path(tmp))
    pdf.output(dest)
    print(f"Wrote {dest}")
    return dest


def _new_pdf() -> FPDF:
    pdf = FPDF(format="A4")
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.set_margins(18, 18, 18)
    regular, bold = _fonts()
    if regular is None:
        raise SystemExit(
            "No Unicode font found (looked for Arial or DejaVu). "
            "Cannot embed the student name safely."
        )
    pdf.add_font("Body", "", str(regular))
    pdf.add_font("Body", "B", str(bold or regular))
    return pdf


def _fonts() -> tuple[Path | None, Path | None]:
    for regular, bold in _FONT_CANDIDATES:
        if regular.is_file():
            return regular, bold if bold.is_file() else regular
    return None, None


def _write(pdf: FPDF, text: str, size: int, *, bold: bool = False, line: float = 7) -> None:
    pdf.set_font("Body", "B" if bold else "", size)
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(pdf.epw, line, text, new_x="LMARGIN", new_y="NEXT")


def _cover(
    pdf: FPDF,
    name: str,
    student_id: str,
    app_url: str,
    logins: str,
) -> None:
    pdf.add_page()
    _write(pdf, "COMP 3613 Assignment 1", 20, bold=True, line=12)
    pdf.ln(4)
    _write(pdf, "Individual report", 12)
    pdf.ln(6)
    _write(pdf, "Student name", 12, bold=True)
    _write(pdf, name, 12)
    pdf.ln(2)
    _write(pdf, "Student ID", 12, bold=True)
    _write(pdf, student_id, 12)
    pdf.ln(2)
    _write(pdf, "Deployed app", 12, bold=True)
    _write(pdf, app_url, 11, line=6)
    pdf.ln(2)
    _write(pdf, "Logins", 12, bold=True)
    for line in logins.splitlines():
        if line.strip():
            _write(pdf, line.strip(), 11, line=6)
    pdf.ln(4)
    _write(
        pdf,
        "The YouTube video must show this name and must not show or say this ID. "
        "Do not put the student ID in the video. App logins belong in this report, not database passwords.",
        10,
        line=6,
    )


def _section(markdown: str, *titles: str) -> str:
    wanted = {title.lower() for title in titles}
    capture = False
    lines: list[str] = []
    for line in markdown.splitlines():
        if line.startswith("#"):
            if capture:
                break
            heading = line.lstrip("#").strip().lower()
            capture = heading in wanted
            continue
        if capture:
            lines.append(line)
    return "\n".join(lines).strip()


def _require_marker_access(markdown: str) -> tuple[str, str]:
    deployed = _section(markdown, "deployed app", "deployed app link", "deploy url")
    urls = re.findall(r"https?://[^\s)]+", deployed)
    app_url = next((url for url in urls if "localhost" not in url and "127.0.0.1" not in url), "")
    if not app_url:
        raise SystemExit(
            "docs/report.md needs a Deployed app section with the public Render URL "
            "(not localhost)."
        )

    logins = _section(markdown, "logins", "user logins")
    login_lines = [
        line.strip()
        for line in logins.splitlines()
        if line.strip() and not line.strip().startswith("Markers ")
        and not line.strip().startswith("Every ")
        and not line.strip().startswith("Starter ")
    ]
    if len(login_lines) < 2:
        raise SystemExit(
            "docs/report.md needs a Logins section with at least two accounts "
            "(username / password — role), including every user a marker must use."
        )
    return app_url, "\n".join(login_lines)


def _body(pdf: FPDF, markdown: str, base: Path, tmp: Path) -> None:
    pdf.add_page()
    diagram_n = 0
    for block in _blocks(markdown):
        kind = block[0]
        if kind == "heading":
            level, text = block[1], block[2]
            size = {1: 16, 2: 14, 3: 12}.get(level, 12)
            pdf.ln(3)
            _write(pdf, text, size, bold=True)
            pdf.ln(1)
        elif kind == "paragraph":
            _write(pdf, _inline(block[1]), 11, line=6)
            pdf.ln(2)
        elif kind == "list":
            _write(pdf, "- " + _inline(block[1]), 11, line=6)
        elif kind == "image":
            _image(pdf, _resolve(block[1], base))
        elif kind == "mermaid":
            diagram_n += 1
            png = tmp / f"diagram-{diagram_n}.png"
            if _render_mermaid(block[1], png):
                _image(pdf, png)
            else:
                _write(
                    pdf,
                    "Mermaid source (install Node.js and re-run export to render the image):\n"
                    + block[1],
                    9,
                    line=5,
                )
                pdf.ln(2)
                print(
                    "warning: Mermaid diagram left as source. "
                    "Install Node.js, then re-run so npx @mermaid-js/mermaid-cli can render it."
                )
        elif kind == "code":
            _write(pdf, block[1], 9, line=5)
            pdf.ln(2)


def _blocks(markdown: str) -> list[tuple]:
    lines = markdown.splitlines()
    blocks: list[tuple] = []
    i = 0
    paragraph: list[str] = []

    def flush() -> None:
        text = " ".join(part.strip() for part in paragraph if part.strip())
        paragraph.clear()
        if text:
            blocks.append(("paragraph", text))

    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            flush()
            lang = line[3:].strip().lower()
            i += 1
            body: list[str] = []
            while i < len(lines) and not lines[i].startswith("```"):
                body.append(lines[i])
                i += 1
            text = "\n".join(body).strip()
            blocks.append(("mermaid" if lang == "mermaid" else "code", text))
            i += 1
            continue
        image = re.fullmatch(r"!\[[^\]]*\]\(([^)]+)\)", line.strip())
        if image:
            flush()
            blocks.append(("image", image.group(1).strip()))
            i += 1
            continue
        heading = re.match(r"^(#{1,3})\s+(.+)$", line)
        if heading:
            flush()
            blocks.append(("heading", len(heading.group(1)), heading.group(2).strip()))
            i += 1
            continue
        if re.match(r"^\s*[-*]\s+", line):
            flush()
            blocks.append(("list", re.sub(r"^\s*[-*]\s+", "", line)))
            i += 1
            continue
        if not line.strip():
            flush()
            i += 1
            continue
        paragraph.append(line)
        i += 1
    flush()
    return blocks


def _inline(text: str) -> str:
    return re.sub(r"[*_`]", "", text).strip()


def _resolve(raw: str, base: Path) -> Path:
    path = Path(raw)
    if path.is_file():
        return path
    from_report = (base / path).resolve()
    if from_report.is_file():
        return from_report
    from_root = (REPO_ROOT / path).resolve()
    if from_root.is_file():
        return from_root
    raise SystemExit(f"Image not found: {raw} (looked next to the report and at the repo root)")


def _image(pdf: FPDF, path: Path) -> None:
    if path.suffix.lower() not in {".png", ".jpg", ".jpeg"}:
        raise SystemExit(f"Wireframe images must be PNG or JPG: {path}")
    pdf.ln(2)
    pdf.image(str(path), w=pdf.epw)
    pdf.ln(3)


def _render_mermaid(source: str, png: Path) -> bool:
    mmd = png.with_suffix(".mmd")
    mmd.write_text(source, encoding="utf-8")
    commands: list[list[str]] = []
    mmdc = shutil.which("mmdc")
    if mmdc:
        commands.append([mmdc, "-i", str(mmd), "-o", str(png), "-b", "white"])
    npx = shutil.which("npx")
    if npx:
        commands.append(
            [npx, "--yes", "@mermaid-js/mermaid-cli", "-i", str(mmd), "-o", str(png), "-b", "white"]
        )
    for cmd in commands:
        try:
            subprocess.run(cmd, check=True, timeout=180, capture_output=True)
        except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
            continue
        if png.is_file():
            return True
    return False
