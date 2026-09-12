# Shared skills (Cursor, Copilot, OpenCode)

Canonical skills for all three agents:

| Skill | Path |
|-------|------|
| Guide | `.agents/skills/buildmine-guide/SKILL.md` |
| Judge | `.agents/skills/buildmine-judge/SKILL.md` |

A copy also lives under `.cursor/skills/` for older Cursor builds.

| Agent | How it loads these |
|-------|--------------------|
| **Cursor** | Discovers `.agents/skills/` and `.cursor/skills/`. Start a new Agent chat, then `/buildmine-guide`. |
| **GitHub Copilot** | Agent mode and Copilot CLI load `.agents/skills/*/SKILL.md` plus `AGENTS.md` and `.github/copilot-instructions.md`. Use **Agent** mode (not Ask/Edit, not autocomplete-only). |
| **OpenCode** | Loads `.agents/skills/` and always reads `AGENTS.md`. Run from the project root. Do not run `/init` (it overwrites `AGENTS.md`). |

## GitHub Education

Student license / benefits (apply, then activate Copilot):

https://github.com/settings/education/benefits

[How to apply](https://docs.github.com/en/education/about-github-education/github-education-for-students/apply-to-github-education-as-a-student) · [Copilot for students](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-students)

## Copilot setup

1. GitHub account → apply at the benefits link above → activate Copilot (or use Copilot Free).
2. VS Code + GitHub Copilot and Copilot Chat extensions, signed in.
3. Open this repo. Copilot Chat → **Agent**.
4. `Use the buildmine-guide skill.`

## OpenCode setup

1. Install: `npm install -g opencode-ai` (Windows also: `scoop install opencode` or `choco install opencode`). macOS/Linux: `curl -fsSL https://opencode.ai/install | bash`. Docs: https://opencode.ai/docs/
2. From this repo root: `opencode`, then `/connect` a model.
3. Do not run `/init`.
4. `Use the buildmine-guide skill.`

Web chat (chatgpt.com, claude.ai, gemini.google.com) does **not** load these files. That path is not allowed for the assignment.

When you change a skill, update **both** `.agents/skills/` and `.cursor/skills/` so they stay the same.

## This assignment's phases

1. Select the project and name **three** workflows.
2. Use cases and a Mermaid diagram in `docs/report.md`.
3. First Mermaid model diagram (revise it later).
4. Student wireframes exported into `docs/wireframes/`. The agent checks coverage. No code until every use case is covered.
5. Implement from the model and wireframes until the three workflows work locally, then deploy Postgres and the web service with the Render MCP.

Judge turns conversation confidence into the impression mark: `round(confidence × 10)` out of 10.

Export the report with `python manage.py report --name "..." --id "..."`.
