# COMP 3613 phases (this assignment)

This file **replaces** the generic Buildmine phases (intent, UI-first, slices, role parity, harden) for COMP 3613 Assignment 1. Follow this table. The assignment brief is `ASSIGNMENT.md`.

## Phases and exit gates

| Phase | Name | Exit gate (student must meet before moving on) |
|-------|------|--------------------------------------------------|
| **1** | Project and workflows | Assigned project selected. **Exactly three** workflows named: who acts, step sequence, what “done” looks like. Interpretation of the brief in the student’s words. No diagrams required yet. **No app code.** |
| **2** | Use cases | Use cases derived from those three workflows. Mermaid use-case diagram in `docs/report.md`. Student can explain every actor and use case. **No app code.** |
| **3** | Model (first draft) | Mermaid model diagram that can support the use cases. Explicitly a **first draft** — expect it to change. Student can explain entities and relationships. **No app code.** |
| **4** | Wireframes | Student drafts wireframes **outside** the agent, for the three workflows only. Exports images (PNG or JPG) into `docs/wireframes/`. Agent checks coverage. **Do not start Phase 5 unless every use case is covered by a wireframe image.** |
| **5** | Implement and deploy | Build from the **current** model and the imported wireframes. One workflow at a time. Update the Mermaid model when the design changes. Verify locally, then deploy Postgres and the web service with the **Render MCP** (see below). Public URL in the report. Student verifies the three workflows on that URL. |

## Diagrams (Mermaid)

Use-case and model diagrams are **Mermaid in `docs/report.md`**, not screenshots of another drawing tool.

- Use-case diagram: a Mermaid `flowchart` (actors as stadium/circle nodes, use cases as rectangles, associations as edges). Mermaid has no reliable UML use-case type.
- Model diagram: Mermaid `erDiagram` (or `classDiagram` if they can justify it).

The agent may **format** Mermaid from decisions the student already made. The agent may not invent the use cases or the model and hand them over as finished work. The student must be able to explain every node.

The Phase 3 model is a first version. During Phase 5, revise the Mermaid when entities, fields, or relationships change, and note what changed and why in the report.

## Wireframes (student, external)

The agent does **not** draw the wireframes and does not generate substitute images.

The student designs them elsewhere (paper, Figma, Excalidraw, draw.io, and so on), exports **images**, and puts them in `docs/wireframes/`. Only the three main workflows — not signup, login, or a CRUD field tour.

Before Phase 5, the agent writes a coverage check and **stops** if anything is missing:

```text
<!-- buildmine:wireframe-coverage
use_case: <name from the Phase 2 diagram>
image: docs/wireframes/<file>
covered: yes|no
note: <one line>
-->
```

One block per use case. Phase 5 is closed until every block is `covered: yes` and the image file is actually in the workspace.

## Report (Markdown, then PDF)

Co-draft `docs/report.md` **with** the student, from decisions already in the session. Do not write the report alone from a one-line “write my report” prompt.

When the student has reviewed the markdown and supplied their name and student ID:

```bash
python manage.py report --name "Student Name" --id "816000000"
```

That writes `docs/report.pdf`. The cover includes the name, student ID, **deployed app link**, and **user logins** (every account a marker needs). Export fails if those are missing. The YouTube video must **not** show or say the student ID. Do not put the database password in the report.

## Phase 5 loop

Explore the FastMVC patterns to copy → student `Decision:` → implement **one** workflow → student runs the app and reports what they clicked and saw → update the model diagram if the design moved → next workflow.

When all three workflows work locally, deploy with the **Render MCP**. Do not deploy before local verification. Do not paste database passwords into the report.

1. Repo is pushed to GitHub. Student is signed in to Render MCP (`.cursor/mcp.json` or the Render plugin). Confirm the workspace with them.
2. `create_postgres`: name `fastmvc-db`, plan `free`, region `oregon`, disk 1 GB. Match `render.yaml`.
3. `create_web_service`: runtime `python`, plan `free`, **same region**, their repo and branch. Build `pip install .`. Start: `python manage.py init --no-drop && python manage.py seed && python manage.py run --host 0.0.0.0 --port $PORT`.
4. Set `DATABASE_URI` to the database **internal** URL, `SECRET_KEY` to a long random string, `ENV=production`, `PYTHON_VERSION=3.12.7`.
5. Wait until the deploy is live. `GET /health` must succeed. Student opens the public URL and walks the three workflows.

Do not also apply the Blueprint in the Dashboard if MCP already created these resources.

Refuse “build the whole app.” A missing public URL is not “done.”

## Anti-patterns (block in Guide; penalize in Judge)

- App code before the Phase 4 coverage gate
- Agent-authored wireframes standing in for the student’s
- A frozen Phase 3 model that is never revised after implementation
- Inventing the three workflows, use cases, or model and filing that as the student’s work
- Whole-app dumps
- “Done” with no verification in the running app
- Deploying before the three workflows work locally
- SQLite on Render, or the external database URL on the web service
- Diagrams that are not Mermaid
