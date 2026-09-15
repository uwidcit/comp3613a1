# Copilot instructions (FastStarter coursework)

Follow `AGENTS.md` and the skills in `.agents/skills/`.

- While the student is building: use skill **student-build**. Do not use generic Buildmine phases 0–5. Do not implement the whole app in one turn. Ask phase steering questions within the cap (include/extend, relationships, unclear wireframe flows, light Phase 5 code checks); do not pad or spiral unless suspicion is open.
- When they ask to judge or grade the chat, **or** to build/export the report: use skill **student-judge** and do not keep coding. Write the scorecard to `docs/judge.md`. Score COMP 3613 phases 1–5. Read all native agent chats for this project. **Dump all project transcripts** with `python manage.py transcripts` into `docs/transcripts/` (+ zip) for submission. Update `docs/report.md` after every phase. Do not penalize missing explore reports or starter-kit auth lectures. Credit include/extend, relationship, and code-check evidence. Show awarded total / scoreable max, then overall / 4. Then export if they asked (`python manage.py report`).
- Student owns the workflows (at least three; more is allowed), design decisions, Phase 5 code-check answers when asked, and verification. Guide keeps `docs/report.md` current after each milestone.
- No app code until wireframes in `docs/wireframes/` cover every use case.
- After local verification, deploy Postgres and the web service with the Render MCP (`render.yaml`, `.vscode/mcp.json`). Student starts the `render` server in `.vscode/mcp.json` (API key via input prompt — never commit the key). Docs: https://render.com/docs/mcp-server and https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/extend-copilot-chat-with-mcp
- Run/reset via `python manage.py init` (creates tables and seeds demo users), then `python manage.py run`.
