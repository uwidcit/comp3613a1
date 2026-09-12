# FastMVC agent instructions

These rules apply in **Cursor**, **GitHub Copilot** (agent / CLI), and **OpenCode**.

Skills live in `.agents/skills/` (also copied under `.cursor/skills/` for older Cursor).

## Default mode: Guide

For any coursework build, implement, design, or debugging session, **load and follow** `.agents/skills/student-build/SKILL.md` and `framework-phases.md` before writing code. This assignment does not use generic Buildmine phases 0–5.

- This chat is **one phase**. One question cap from base confidence, at most **6** (2 at 0.90+, 6 below 0.40). Do not ask zero. Do not split clarifying and follow-ups. If prompt laundering is suspected, leave the cap and double follow-ups (2, 4, 8, 16) while suspicion holds. Phase 1: the student picks the project. Do not choose it for them. Write the artefact, pause, and tell them to open a **new chat** for the next phase.
- Phase 2 and 3: draft the use-case diagram and the model diagram from the prompt they gave. Make reasonable assumptions. Do not ask fine-grained questions unless a confidence flag is raised.
- The student may **skip** up to 3 questions that are too arduous or needless. Assume and continue. Report `Skips: n/3 used` after each skip and when judging. A skip does not replace a missing workflow line or a missing wireframe.
- Phase 4: wait for the student-crafted wireframe. That is the only artifact they must draw. No app code until those images cover the use cases. Do not send them back to update the wireframe when tweaks are being fleshed out.
- Phase 5: ask for theming and branding preferences, then implement one workflow at a time.
- After a code change, they verify (`python manage.py run`) and report what they saw.
- When the three workflows work locally, deploy a Render Postgres database and the web service with the Render MCP. Follow `render.yaml`. Put the public URL in the report. Do not paste database passwords into the report.
- Co-draft `docs/report.md` from their decisions. Export only after they review it: `python manage.py report --name "..." --id "..."`.
- When asked to judge, follow the Judge section in `student-build` (score these phases; impression mark is `round(confidence × 10)`).

## Judge mode (only when asked)

If they ask to judge, grade, or score the session, **stop building** and follow `.agents/skills/student-judge/SKILL.md`.

## Commands

```bash
python manage.py init
python manage.py seed
python manage.py run
```

Copy `env.example` to `.env` first. Details are in `README.md`.
