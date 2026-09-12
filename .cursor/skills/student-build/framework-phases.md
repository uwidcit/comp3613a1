# COMP 3613 phases (student-build)

This is the assignment framework. Do not use generic Buildmine phases 0–5. They are not in this repo.

The student drives the next phase with one complete prompt. Draft the use-case diagram and the model diagram from that prompt. Only the wireframe is user crafted. Do not ask fine-grained questions when no confidence flags are raised. Make reasonable assumptions. The student may **skip** up to 3 needless questions. Report `Skips: n/3 used` after each skip and when judging.

## Phases and exit gates

| Phase | What the student does | Exit gate |
|-------|------------------------|-----------|
| **1** | One prompt: assigned project and exactly three workflows (who, steps, done). | Those four lines are filled. No code. |
| **2** | Prompt already given (the three workflows). | Agent drafts the Mermaid use-case diagram in `docs/report.md`. No fill-in form. No code. |
| **3** | Same prompt. | Agent drafts the first-draft Mermaid `erDiagram`. Assumes entities and properties. No code. |
| **4** | Student crafts wireframe images in `docs/wireframes/`. | Agent waits. This is the only artifact the student must draw. No code until every use case has an image. |
| **5** | State theming and branding preferences. Then implement. | Build from the model and wireframes. Tweaks update the model and the code, not the wireframe. Deploy after local verification. |

## Follow-up cap and pause

A **clarifying question** fills one gap the artefact cannot be written without. A **follow-up** is extra probing after that. Do not conflate them. Zero is too low: even at 0.75+ allow **1** clarifying question and **1** follow-up. At 0.40–0.74 allow **2** clarifying and **1** follow-up. Below 0.40 allow **2** and **2**. A confidence flag caps confidence at 0.40. Do not ask past either cap.

This chat is one phase. Write the artefact, show the pause block (phase, artefact path, confidence, clarifying used/cap, follow-ups used/cap, skips), and tell them to open a **new chat** for the next phase. Do not start it here.

| Phase | Artefact the student can open |
|-------|--------------------------------|
| 1 | `docs/report.md` — three workflows |
| 2 | `docs/report.md` — use-case diagram |
| 3 | `docs/report.md` — model diagram |
| 4 | `docs/wireframes/` plus coverage notes in `docs/report.md` |
| 5 | theming in `docs/report.md`, then one verified workflow per chat |

## Diagrams

Mermaid in `docs/report.md`. Use-case diagram is a flowchart. Model is an `erDiagram`. Draft both from the prompt they gave. Assume what the prompt implies and note it in one line. Phase 3 is a first draft; the agent revises it in Phase 5 when the design moves. Do not ask the student to redraw it.

## Wireframes

The agent does not draw them. Wait until image files are in `docs/wireframes/`. Coverage is a file check, not a question. One block per use case:

```text
<!-- student-build:wireframe-coverage
use_case: <name>
image: docs/wireframes/<file>
covered: yes|no
-->
```

## Phase 5

Ask only for theming and branding preferences. Then implement one workflow at a time from the model and the wireframes. Do not re-ask layout, fields, or flows the images already show. Do not send the student to update the wireframe when tweaks are being fleshed out. Deploy with the Render MCP after the three workflows work locally (`README.md`, `render.yaml`).

## Anti-patterns

- Fine-grained questions when no confidence flag is raised
- Treating a skip as cheating, or allowing a 4th skip
- Asking the student to list actors, use cases, entities, or properties the prompt already implies
- Sending the student to update the wireframe for an implementation tweak
- App code before Phase 4 images cover the use cases
- Agent-drawn wireframes
- Starting the next phase in the same chat
- Using generic Buildmine phases 0–5 for this assignment
