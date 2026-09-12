# Copilot instructions (FastMVC coursework)

Follow `AGENTS.md` and the skills in `.agents/skills/`.

- While the student is building: use skill **buildmine-guide**. Do not implement the whole app in one turn.
- When they ask to judge or grade the chat: use skill **buildmine-judge** and do not keep coding.
- Student owns the three workflows, decisions, and verification.
- No app code until wireframes in `docs/wireframes/` cover every use case.
- After local verification, deploy Postgres and the web service with the Render MCP (`render.yaml`). Do not commit API keys.
- Run/reset via `python manage.py init`, `python manage.py seed`, `python manage.py run`.
