# comp3613a1

COMP 3613 Assignment 1 starter ([uwidcit/comp3613a1](https://github.com/uwidcit/comp3613a1)). Built on FastMVC (FastAPI MVC).

**Assignment brief, agents, and GitHub Education link:** [ASSIGNMENT.md](ASSIGNMENT.md)

Based on the [fullstack FastAPI template](https://github.com/fastapi/full-stack-fastapi-template) with a layered architecture that reduces repeated code [(DRY)](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) across CLI, headless API, and fullstack UI.

This codebase follows an API-first, modern AJAX flow:

1. If the backend should render the UI, implement **views** that return the interface.
2. A small JavaScript helper (`app.js` / related static scripts) can intercept form submissions and call **API** endpoints instead.

Advantages of this structure:

1. Implement API endpoints first; views can stay thin
2. Reuse the same API for mobile / desktop clients
3. Pair with a separate frontend (Vue, React, Next, Nuxt, etc.)
4. Export endpoints for other services (including AI agents)
5. Drive features from the CLI when needed

---

## Initial setup

You need **Python 3.10+**. Coursework agents (Cursor, Copilot, or OpenCode) are in [ASSIGNMENT.md](ASSIGNMENT.md).

All project commands are a **Python CLI** (`manage.py`). There are no shell setup scripts.

### 1. Clone

```bash
git clone https://github.com/uwidcit/comp3613a1.git
cd comp3613a1
```

### 2. Virtual environment and install dependencies

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e .
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e .
```

`pip install -e .` installs this project and everything listed in `pyproject.toml`.

### 3. Create `.env`

**Windows:**

```powershell
Copy-Item env.example .env
```

**macOS / Linux:**

```bash
cp env.example .env
```

Defaults use a local SQLite file (`database.db`). Change `SECRET_KEY` before any real deployment.

### 4. Initialise the database (Python CLI)

Creates tables (drops existing tables by default):

```bash
python manage.py init
```

Flags:

```bash
python manage.py init --no-drop   # create tables without dropping
python manage.py init --seed      # init, then load demo users
```

### 5. Seed demo data (Python CLI)

```bash
python manage.py seed
```

| Username | Password    | Role         |
|----------|-------------|--------------|
| `bob`    | `bobpass`   | regular_user |
| `admin`  | `adminpass` | admin        |

Seeding skips usernames that already exist. Add more rows in `cmd_seed` in `app/cli.py`.

```bash
python manage.py users
```

### 6. Run the project (Python CLI)

```bash
python manage.py run
```

Then open http://127.0.0.1:8000 (host/port from `.env` / settings).

```bash
python manage.py run --host 127.0.0.1 --port 8000
python manage.py run --no-reload
```

---

## CLI reference

Commands are implemented in `app/cli.py` (stdlib `argparse`) and invoked via `manage.py`.

| Command | Purpose |
|---------|---------|
| `python manage.py init` | Drop (default) and create DB tables |
| `python manage.py seed` | Insert demo users |
| `python manage.py run` | Start Uvicorn (reload unless `ENV=production`) |
| `python manage.py users` | Print users in the DB |
| `python manage.py report --name "..." --id "..."` | Merge `docs/judge.md` into the report if present, export `docs/report.pdf`. Incomplete drafts allowed. Cover has name, ID, and skill-integrity hash. Fails only if course skills were edited |
| `python manage.py usecase` | Render `docs/diagrams/use-case.json` to a UML use-case PNG (`docs/diagrams/use-case.png`) |
| `python manage.py skills-verify` | Check course skills against `.agents/skills.lock.json` |
| `python manage.py --help` | Show all commands |

Typical reset-and-start:

```bash
# venv activated, cwd = project root
python manage.py init --seed
python manage.py run
```

The app binds `0.0.0.0` and reads `PORT` when Render sets it. Locally it uses port 8000.

---

## Deploy (Render MCP)

Deploy a **Postgres database** and the **web app** on Render’s free plan. Use the Render MCP from your agent (Cursor, Copilot, or OpenCode). Config lives in `render.yaml` and `.cursor/mcp.json`. Do not commit an API key. Do not put the **database** password in the report or the video. **App** usernames and passwords belong in `docs/report.md`.

1. Push your repo to GitHub (Render clones the remote; it cannot deploy an unpushed folder).
2. Create a free [Render](https://render.com) account. Open this project so `.cursor/mcp.json` loads the Render MCP (`https://mcp.render.com/mcp`). Sign in when prompted, or install the [Render plugin](https://render.com/docs/mcp-server) and complete OAuth.
3. Ask the agent to deploy using the Render MCP, matching `render.yaml`:
   - `create_postgres` — name `fastmvc-db`, plan `free`, region `oregon`, disk 1 GB
   - `create_web_service` — runtime `python`, plan `free`, **same region**, repo and branch, build `pip install .`
4. Set env vars on the web service (use the database **internal** connection string, not the external one):
   - `DATABASE_URI` — internal Postgres URL
   - `SECRET_KEY` — long random string
   - `ENV` — `production`
   - `PYTHON_VERSION` — `3.12.7`
5. Start command (do not drop tables on each boot):

```bash
python manage.py init --no-drop && python manage.py seed && python manage.py run --host 0.0.0.0 --port $PORT
```

6. Confirm the deploy is live and `GET /health` succeeds. Put the public URL and the marker logins (username, password, role) in `docs/report.md`.

Free web services sleep after inactivity. Free Postgres expires after 30 days. Do not also apply `render.yaml` in the Dashboard if the MCP already created these resources — that makes a second copy.

---

## Agents: Cursor, Copilot, or OpenCode

Pick **one** of these. All three load Guide and Judge from this repo. Web chatbots (chatgpt.com, claude.ai, gemini.google.com) do not.

Start every build session with:

```text
Use the student-build skill.

Phase 1. Assigned project: …
Workflows (at least three; format Feature (user); steps go in the wireframe):
- Explore/Search Publications (Public)
- …
- …
```

When finished: ask the Guide to **build the report**. That run includes student-judge (`docs/judge.md` is appended to the PDF).

### GitHub Education (student license)

Apply here (sign in, then **Start an application**):

**https://github.com/settings/education/benefits**

Docs: [Apply to GitHub Education as a student](https://docs.github.com/en/education/about-github-education/github-education-for-students/apply-to-github-education-as-a-student).

Use a verified **academic email** if your school issues one (UWI: `@my.uwi.edu`), plus proof of enrolment if asked. After approval, activate Copilot from that same benefits page — approval and Copilot activation are separate steps. Details: [Copilot for students](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-students).

If the student Copilot offer is not available yet, use **Copilot Free** in agent mode. Do not buy a paid plan for this course.

### Cursor (Hobby, no card)

1. Install [Cursor](https://cursor.com) and sign in. Stay on free **Hobby**.
2. **File → Open Folder** → this project root (not a parent folder).
3. New **Agent** chat. Confirm it can see `student-build` (or type `/student-build`).
4. Paste the Guide prompt above.

### GitHub Copilot (agent mode)

Skills load only in **agent** mode or the Copilot CLI — not inline autocomplete.

1. Create a GitHub account if you do not have one.
2. Apply for [GitHub Education](https://github.com/settings/education/benefits) and activate Copilot (or use Copilot Free).
3. Install [VS Code](https://code.visualstudio.com/) and the **GitHub Copilot** and **GitHub Copilot Chat** extensions. Sign in with the same GitHub account.
4. **File → Open Folder** → this project root.
5. Open Copilot Chat and switch the mode to **Agent** (not Ask, not Edit).
6. Start with the prompt above. If the skill does not attach, say: `Use the student-build skill in .agents/skills/student-build/SKILL.md`.

Optional CLI (same account): [Install GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli), then run it from this folder. It also reads `AGENTS.md` and `.github/copilot-instructions.md`.

One feature slice at a time — free quotas are limited.

### OpenCode

OpenCode is a free client. You still need a model (local, or a free API tier). Docs: [opencode.ai/docs](https://opencode.ai/docs/).

**Windows (PowerShell):**

```powershell
npm install -g opencode-ai
```

Or: `scoop install opencode` / `choco install opencode`. Desktop app: [opencode.ai/download](https://opencode.ai/download).

**macOS / Linux:**

```bash
curl -fsSL https://opencode.ai/install | bash
# or: brew install anomalyco/tap/opencode
# or: npm install -g opencode-ai
```

Then:

1. `cd` to this project root (the folder that contains `AGENTS.md`).
2. Run `opencode`.
3. Connect a model with `/connect` (or `opencode auth login`). Do **not** run `/init` — this repo already has `AGENTS.md`, and `/init` would overwrite it.
4. Start with the prompt above. OpenCode should follow `AGENTS.md` and can load `.agents/skills/student-build`.

More setup detail: [`.agents/skills/README.md`](.agents/skills/README.md).

---

## What is the Model View Controller (MVC) pattern?

- **Models** — SQLModel/SQLAlchemy classes (database tables)
- **Controllers** — utility functions that mutate models and/or perform business logic
- **Views** — bind controllers to HTTP routes, passing request parameters through

In this template, business rules often sit in a **service** layer, with repositories handling data access.

## What is the Service repository pattern?

- **Repository layer** — mediator to the datastore (CRUD); no business rules
- **Service layer** — application **rules** (authz, workflows, invariants)

## App structure

```text
comp3613a1
|-- .agents/skills/           # Guide + Judge (Cursor, Copilot, OpenCode)
|-- .cursor/skills/          # same skills (older Cursor)
|-- .github/copilot-instructions.md
|-- AGENTS.md                # always-on: use Guide unless asked to Judge
|-- ASSIGNMENT.md            # course brief, agents, GitHub Education link
|-- README.md
|-- manage.py                # python manage.py init|seed|run|users
|-- env.example
|-- pyproject.toml
|-- app/
|    |- cli.py               # Python CLI: init / seed / run / users
|    |- main.py
|    |- database.py
|    |- models/
|    |- repositories/
|    |- routers/
|    |- schemas/
|    |- services/
|    |- static/
|    |- templates/
|    |- utilities/
```

> **Note:** You **must** have a `.env` (copy from `env.example`) before init/seed/run. See `app/config.py` for settings.

## Using this in production

1. Change default configuration (production database, secret, environment)
2. Review `config.py` for scalability settings
3. Add a migration tool such as Alembic
4. Consider Docker for deployment
5. Prefer secure cookie practices over casual localStorage token storage where appropriate
