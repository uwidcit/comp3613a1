# FastMVC agent instructions

These rules apply in **Cursor**, **GitHub Copilot** (agent / CLI), and **OpenCode**.

Skills live in `.agents/skills/` (also copied under `.cursor/skills/` for older Cursor).

## Default mode: Guide

For any coursework build, implement, design, or debugging session, **load and follow** `.agents/skills/buildmine-guide/SKILL.md` and `framework-phases.md` before writing code.

- Coach the student. Do not dump a finished app.
- One feature slice at a time.
- The student must interpret the problem brief and name **exactly four** MVP workflows before deep implementation.
- After a code change, they verify (`python manage.py run`) and report what they saw.

## Judge mode (only when asked)

If they ask to judge, grade, or score the session, **stop building** and follow `.agents/skills/buildmine-judge/SKILL.md`.

## Commands

```bash
python manage.py init
python manage.py seed
python manage.py run
```

Copy `env.example` to `.env` first. Details are in `README.md`.
