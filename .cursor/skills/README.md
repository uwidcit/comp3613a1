# Buildmine skills (Cursor, Copilot, OpenCode)

Two project skills for coursework. Canonical copies: `.agents/skills/` (also under `.cursor/skills/`).

| Skill | When to use |
|-------|-------------|
| **buildmine-guide** | While building |
| **buildmine-judge** | After a session, when asked to score |

## Which agents load them

| Agent | Works? | How |
|-------|--------|-----|
| Cursor Hobby | Yes | Open folder; new Agent chat; `/buildmine-guide` |
| GitHub Copilot agent / CLI | Yes | Open repo; agent mode (not autocomplete-only); `/buildmine-guide` |
| OpenCode | Yes | Run from repo root; it reads `AGENTS.md` and `.agents/skills/` |
| ChatGPT / Claude / Gemini **web** | No | They never see these files |

`AGENTS.md` and `.github/copilot-instructions.md` tell Copilot and OpenCode to follow Guide by default.

## Cursor Hobby checklist

1. Install [Cursor](https://cursor.com) and stay on free **Hobby**.
2. **File → Open Folder** on this project root.
3. Confirm `.agents/skills/buildmine-guide/SKILL.md`.
4. New Agent chat → `Use buildmine-guide`.
5. End with `Use buildmine-judge on this session.`

## GitHub Education (student license)

Apply (signed in): **https://github.com/settings/education/benefits**

[Apply as a student](https://docs.github.com/en/education/about-github-education/github-education-for-students/apply-to-github-education-as-a-student). Use a verified academic email if you have one. After approval, activate Copilot from that page ([Copilot for students](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-students)). If the student offer is not available, use Copilot Free. Do not buy a paid plan for this course.

## Copilot setup

1. GitHub account, then the Education link above.
2. Install [VS Code](https://code.visualstudio.com/) and the **GitHub Copilot** and **GitHub Copilot Chat** extensions. Sign in.
3. Open this project root. In Copilot Chat, set the mode to **Agent** (not Ask, not Edit, not autocomplete-only).
4. `Use the buildmine-guide skill.` It reads `.agents/skills/` and `.github/copilot-instructions.md`.

Optional: [Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli) from this folder. One slice at a time — free quotas are limited.

## OpenCode setup

Free client; you still need a model (local or a free API tier). Docs: https://opencode.ai/docs/

**Windows:** `npm install -g opencode-ai` (or `scoop install opencode` / `choco install opencode`).

**macOS / Linux:** `curl -fsSL https://opencode.ai/install | bash` or `brew install anomalyco/tap/opencode`.

Then `cd` to this repo, run `opencode`, and `/connect` a model. **Do not run `/init`** — it overwrites the course `AGENTS.md`. Start with `Use the buildmine-guide skill.`

## Do / don’t

- **Do** stay in one agent session so Guide can see your decisions.
- **Don’t** build in a web chatbot and paste the result back.
- **Don’t** say “just apply this.”

## Installation (students)

Skills under `.cursor/skills/` are **already included** when you clone or fork this repo. You normally do **not** need to copy anything.

1. Open this project folder in **Cursor** (File → Open Folder).
2. Confirm the skills exist (paths above).
3. Start an Agent chat in the project. Cursor discovers project skills automatically from `.cursor/skills/`.
4. For the build: say you want **Guide** mode, or `@buildmine-guide` / ask the agent to follow the Buildmine guide skill.
5. When finished (or for marking): ask for **Judge** / `@buildmine-judge` on the same chat or a saved agent transcript.

### If skills are missing (older fork / incomplete copy)

Copy from a fresh FastMVC clone into your project root and commit:

```text
.cursor/skills/buildmine-guide/
.cursor/skills/buildmine-judge/
.cursor/skills/README.md
```

Do **not** put course skills only in `~/.cursor/skills/` if your assignment requires them in the submitted repo — markers need them in the project.

### Personal vs project skills

| Location | Scope |
|----------|--------|
| `.cursor/skills/` (this repo) | Shared with anyone who clones; use for coursework |
| `~/.cursor/skills/` | Your machine only; optional for personal prefs |

## Quick start prompts

**Guide (start of assignment):**

```text
Use buildmine-guide. I'm in Phase 0 for [project name].
Here is the problem brief: …
I need to interpret it and propose exactly 4 MVP features/workflows.
Question me before we design screens or write code.
```

**Judge (end of session):**

```text
Use buildmine-judge on this chat.
Target phases: 0–3 (or as specified by the assignment).
```

## Notes

- Course briefs are short on purpose — **you** choose the four MVP features; Guide should challenge vague or oversized scope.
- Guide refuses shallow “just build it” prompts and quarantines paste-backs from other chatbots.
- Judge scores process and integrity; working code alone is not a high score.
- Keep `framework-phases.md` next to each `SKILL.md` (both skills link to it).
- Free Hobby quotas last longer if you stay in-phase and verify each slice yourself.
