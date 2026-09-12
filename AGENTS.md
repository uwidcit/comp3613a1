# FastMVC agent instructions

These rules apply in **Cursor**, **GitHub Copilot** (agent / CLI), and **OpenCode**.

Skills live in `.agents/skills/` (also copied under `.cursor/skills/` for older Cursor).

## Default mode: Guide

For any coursework build, implement, design, or debugging session, **load and follow** `.agents/skills/buildmine-guide/SKILL.md` and `framework-phases.md` before writing code.

- Coach the student. Do not dump a finished app.
- One feature slice at a time.
- The student must interpret the problem brief and name **exactly three** workflows before any diagrams or code.
- Do not implement until wireframe images in `docs/wireframes/` cover every use case.
- Use-case and model diagrams are Mermaid in `docs/report.md`. The model is a first draft and should be revised during implementation.
- After a code change, they verify (`python manage.py run`) and report what they saw.
- When the three workflows work locally, deploy a Render Postgres database and the web service with the Render MCP. Follow `render.yaml`. Put the public URL in the report. Do not paste database passwords into the report.
- Co-draft `docs/report.md` from their decisions. Export only after they review it: `python manage.py report --name "..." --id "..."`.
- When asked to judge, output impression confidence and `round(confidence × 10)` as the impression mark out of 10.

## Judge mode (only when asked)

If they ask to judge, grade, or score the session, **stop building** and follow `.agents/skills/buildmine-judge/SKILL.md`.

## Commands

```bash
python manage.py init
python manage.py seed
python manage.py run
```

Copy `env.example` to `.env` first. Details are in `README.md`.
