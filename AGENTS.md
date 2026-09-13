# FastMVC agent instructions

These rules apply in **Cursor**, **GitHub Copilot** (agent / CLI), and **OpenCode**.

Skills live in `.agents/skills/` (also copied under `.cursor/skills/` for older Cursor).

## Default mode: Guide

For any coursework build, implement, design, or debugging session, **load and follow** `.agents/skills/student-build/SKILL.md` and `framework-phases.md` before writing code. This assignment does not use generic Buildmine phases 0–5.

- A design chat is **one phase**. One question cap from base confidence, at most **8** (up to 4 at 0.90+, up to 8 below 0.40). Phase 2 is 0 when `Feature (user)` lines exist. Ask only unanswered gaps. Do not re-ask the prompt or collect wireframe steps. Do not split clarifying and follow-ups. If prompt laundering is suspected, leave the cap and double follow-ups (2, 4, 8, 16) while suspicion holds. Phase 1: the student picks the project and names the workflows as `Feature (user)`. Do not choose them. Do not interview each workflow for who/steps/done. Write the artefact, pause, and tell them to open a **new chat** for the next *phase*. Phase 5 implement may keep every workflow in the same conversation.
- Phase 2: draft the UML use-case PNG from the `Feature (user)` lines (`docs/diagrams/use-case.json`, `python manage.py usecase`, embed the image in `docs/report.md`). Assume actors and grouping. Do not use Mermaid for this diagram. Do not withhold the draft. Choice chips are OK when options are real and bounded; do not invent a pick-list.
- Phase 3: the student names entities and properties. Do not invent that list. Ask about relationships, bridge tables, and important edge cases before drafting. Do not assume a many-to-many.
- The student may **skip** up to 3 questions that are too arduous or needless. Assume and continue. Report `Skips: n/3 used` after each skip and when judging. A skip does not replace a missing workflow line or a missing wireframe.
- Phase 4: wait for the student-crafted wireframe. That is the only artifact they must draw. No app code until those images cover the use cases. Compare the images to the model and suggest edits for missing metadata. Flag unoptimized, incomplete, or broken workflows. Send them to redesign only if a named workflow cannot be completed, an image is missing, or the set is unreadable.
- Phase 5: ask for theming and branding preferences, then implement one workflow at a time in the same chat. Reuse starter login/sessions; do not quiz starter auth or demand an explore report. After they verify against the wireframe, continue here. Do not require a new chat per workflow.
- After a code change, they verify (`python manage.py run`) and report what they saw.
- When the named workflows work locally (at least three; more is allowed), deploy a Render Postgres database and the web service with the Render MCP. Follow `render.yaml`. Put the public URL in the report. Do not paste database passwords into the report.
- Co-draft `docs/report.md` from their decisions. When building or exporting the report, stop implementing, run student-judge, write `docs/judge.md`, then export if they asked (`python manage.py report --name "..." --id "..."`). The PDF merges the judge scorecard into the report. Do not refuse a draft export. Export hashes the course skills and fails if they were edited. Do not edit `.agents/skills/`, `.cursor/skills/`, `AGENTS.md`, or `.agents/skills.lock.json`.
- When asked to judge, or when building the report, follow the Judge section in `student-build` (score these phases 1–5, not generic Buildmine 0–5; impression mark is `round(confidence × 10)`). Read **all** native agent chats for this project (phases start in new chats). Students never put transcripts in the repo. Do not penalize missing explore reports or starter-kit auth lectures. Terse mismatch notes are high-quality. Report awarded total / scoreable max, then overall / 4. Write the scorecard to `docs/judge.md`.

## Judge mode

If they ask to judge, grade, or score the session, **or** they ask to build/export the report, **stop building** and follow `.agents/skills/student-judge/SKILL.md`. Write `docs/judge.md`, then return to the report export if that was the request.

## Commands

```bash
python manage.py init
python manage.py seed
python manage.py run
```

Copy `env.example` to `.env` first. Details are in `README.md`.
