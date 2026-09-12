# Copilot instructions (FastMVC coursework)

Follow `AGENTS.md` and the skills in `.agents/skills/`.

- While the student is building: use skill **student-build**. Do not use generic Buildmine phases 0–5. Do not implement the whole app in one turn. Do not ask a series of questions.
- When they ask to judge or grade the chat: use skill **student-judge** and do not keep coding.
- Student owns the workflows (at least three; more is allowed), decisions, and verification.
- No app code until wireframes in `docs/wireframes/` cover every use case.
- After local verification, deploy Postgres and the web service with the Render MCP (`render.yaml`). Do not commit API keys.
- Run/reset via `python manage.py init`, `python manage.py seed`, `python manage.py run`.
