"""Render a UML use-case diagram PNG from a small JSON spec.

Mermaid has no real UML use-case notation (stick-figure actors, system
boundary, ellipses). Phase 2 writes docs/diagrams/use-case.json and this
module draws the PNG the report embeds.
"""

from __future__ import annotations

import json
import textwrap
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

REPO_ROOT = Path(__file__).resolve().parents[1]

DEFAULT_SPEC = REPO_ROOT / "docs" / "diagrams" / "use-case.json"
DEFAULT_PNG = REPO_ROOT / "docs" / "diagrams" / "use-case.png"

NAVY = (27, 54, 93)
GOLD = (196, 163, 90)
INK = (30, 35, 45)
FILL = (255, 255, 255)
BOX = (248, 250, 252)
LINE = (27, 54, 93)

_FONT_CANDIDATES = (
    Path(r"C:\Windows\Fonts\arial.ttf"),
    Path(r"C:\Windows\Fonts\arialbd.ttf"),
    Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
    Path("/System/Library/Fonts/Supplemental/Arial.ttf"),
)


@dataclass(frozen=True)
class UseCase:
    name: str
    actors: tuple[str, ...]


@dataclass(frozen=True)
class DiagramSpec:
    system: str
    actors: tuple[str, ...]
    use_cases: tuple[UseCase, ...]


def render_usecase_png(
    spec_path: Path | None = None,
    output: Path | None = None,
) -> Path:
    spec = load_spec(spec_path or DEFAULT_SPEC)
    dest = output or DEFAULT_PNG
    dest.parent.mkdir(parents=True, exist_ok=True)
    image = _draw(spec)
    image.save(dest, "PNG")
    return dest


def load_spec(path: Path) -> DiagramSpec:
    if not path.is_file():
        raise SystemExit(
            f"Missing {path.as_posix()}. Write the use-case JSON, then re-run "
            "python manage.py usecase."
        )
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path.as_posix()}: {exc}") from exc
    if not isinstance(payload, dict):
        raise SystemExit("Use-case spec must be a JSON object.")

    system = str(payload.get("system") or "System").strip() or "System"
    raw_actors = payload.get("actors") or []
    if not isinstance(raw_actors, list) or not raw_actors:
        raise SystemExit("Use-case spec needs a non-empty actors array.")
    actors = tuple(str(item).strip() for item in raw_actors if str(item).strip())

    raw_cases = payload.get("use_cases") or []
    if not isinstance(raw_cases, list) or not raw_cases:
        raise SystemExit("Use-case spec needs a non-empty use_cases array.")
    cases: list[UseCase] = []
    for item in raw_cases:
        if isinstance(item, str):
            name = item.strip()
            linked = actors
        elif isinstance(item, dict):
            name = str(item.get("name") or "").strip()
            linked_raw = item.get("actors") or actors
            if isinstance(linked_raw, list):
                linked = tuple(str(a).strip() for a in linked_raw if str(a).strip()) or actors
            else:
                linked = actors
        else:
            continue
        if name:
            cases.append(UseCase(name=name, actors=linked))
    if not cases:
        raise SystemExit("Use-case spec has no named use cases.")
    return DiagramSpec(system=system, actors=actors, use_cases=tuple(cases))


def _fonts() -> tuple[ImageFont.FreeTypeFont, ImageFont.FreeTypeFont, ImageFont.FreeTypeFont]:
    regular_path = next((path for path in _FONT_CANDIDATES if path.is_file()), None)
    if regular_path is None:
        raise SystemExit("No TrueType font found for the use-case diagram (Arial or DejaVu).")
    bold_path = regular_path
    if "arial.ttf" in regular_path.name.lower():
        candidate = regular_path.with_name("arialbd.ttf")
        if candidate.is_file():
            bold_path = candidate
    elif "DejaVuSans.ttf" in regular_path.name:
        candidate = regular_path.with_name("DejaVuSans-Bold.ttf")
        if candidate.is_file():
            bold_path = candidate
    title = ImageFont.truetype(str(bold_path), 22)
    label = ImageFont.truetype(str(regular_path), 15)
    small = ImageFont.truetype(str(regular_path), 13)
    return title, label, small


def _draw(spec: DiagramSpec) -> Image.Image:
    title_font, label_font, small_font = _fonts()
    columns = 2 if len(spec.use_cases) > 4 else 1
    ellipse_w, ellipse_h = 300, 86
    h_gap, v_gap = 36, 28
    rows = (len(spec.use_cases) + columns - 1) // columns
    inner_w = columns * ellipse_w + (columns - 1) * h_gap
    inner_h = rows * ellipse_h + (rows - 1) * v_gap
    box_pad_x, box_pad_top, box_pad_bot = 48, 56, 40
    box_w = inner_w + 2 * box_pad_x
    box_h = inner_h + box_pad_top + box_pad_bot

    actor_col = 150
    left_margin, right_margin = 48, 48
    top_margin, bottom_margin = 40, 48
    width = left_margin + actor_col + 36 + box_w + right_margin
    height = top_margin + max(box_h, 110 * len(spec.actors)) + bottom_margin

    image = Image.new("RGB", (width, height), FILL)
    draw = ImageDraw.Draw(image)

    box_x = left_margin + actor_col + 36
    box_y = top_margin + max(0, (height - top_margin - bottom_margin - box_h) // 2)
    draw.rounded_rectangle(
        (box_x, box_y, box_x + box_w, box_y + box_h),
        radius=8,
        fill=BOX,
        outline=NAVY,
        width=3,
    )
    _centered_text(draw, spec.system, box_x + box_w / 2, box_y + 28, title_font, NAVY)
    draw.line((box_x + 24, box_y + 44, box_x + box_w - 24, box_y + 44), fill=GOLD, width=3)

    ellipses: list[tuple[float, float, float, float, UseCase]] = []
    for index, use_case in enumerate(spec.use_cases):
        col = index % columns
        row = index // columns
        cx = box_x + box_pad_x + col * (ellipse_w + h_gap) + ellipse_w / 2
        cy = box_y + box_pad_top + row * (ellipse_h + v_gap) + ellipse_h / 2
        ellipses.append((cx, cy, ellipse_w, ellipse_h, use_case))

    actor_span = max(box_h, 110 * len(spec.actors))
    actor_positions: dict[str, tuple[float, float]] = {}
    for index, actor in enumerate(spec.actors):
        if len(spec.actors) == 1:
            ay = box_y + box_h / 2
        else:
            ay = box_y + 40 + index * (actor_span - 80) / (len(spec.actors) - 1)
        ax = left_margin + actor_col / 2
        actor_positions[actor] = (ax, ay)

    for cx, cy, ew, eh, use_case in ellipses:
        left = cx - ew / 2
        for actor in use_case.actors:
            if actor not in actor_positions:
                continue
            ax, ay = actor_positions[actor]
            draw.line((ax + 22, ay, left, cy), fill=LINE, width=2)

    for cx, cy, ew, eh, use_case in ellipses:
        bbox = (cx - ew / 2, cy - eh / 2, cx + ew / 2, cy + eh / 2)
        draw.ellipse(bbox, fill=FILL, outline=NAVY, width=3)
        _wrapped_center(draw, use_case.name, cx, cy, ew - 28, label_font, INK)

    for actor, (ax, ay) in actor_positions.items():
        _stick_actor(draw, ax, ay, actor, small_font)

    return image


def _stick_actor(
    draw: ImageDraw.ImageDraw,
    x: float,
    y: float,
    name: str,
    font: ImageFont.FreeTypeFont,
) -> None:
    head_r = 11
    draw.ellipse((x - head_r, y - 38, x + head_r, y - 38 + 2 * head_r), outline=NAVY, width=3)
    draw.line((x, y - 16, x, y + 10), fill=NAVY, width=3)
    draw.line((x - 16, y - 6, x + 16, y - 6), fill=NAVY, width=3)
    draw.line((x, y + 10, x - 14, y + 32), fill=NAVY, width=3)
    draw.line((x, y + 10, x + 14, y + 32), fill=NAVY, width=3)
    _centered_text(draw, name, x, y + 48, font, INK)


def _centered_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    x: float,
    y: float,
    font: ImageFont.FreeTypeFont,
    color: tuple[int, int, int],
) -> None:
    bbox = draw.textbbox((0, 0), text, font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text((x - w / 2, y - h / 2), text, font=font, fill=color)


def _wrapped_center(
    draw: ImageDraw.ImageDraw,
    text: str,
    x: float,
    y: float,
    max_width: float,
    font: ImageFont.FreeTypeFont,
    color: tuple[int, int, int],
) -> None:
    avg = max(draw.textlength("M", font=font), 1)
    width_chars = max(int(max_width / avg), 8)
    lines = textwrap.wrap(text, width=width_chars) or [text]
    line_h = draw.textbbox((0, 0), "Ag", font=font)[3]
    total = line_h * len(lines)
    start = y - total / 2
    for index, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=font)
        w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        draw.text((x - w / 2, start + index * line_h + (line_h - h) / 2), line, font=font, fill=color)
