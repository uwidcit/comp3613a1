# COMP 3613 phases (student-build)

This is the assignment framework. Do not use generic Buildmine phases 0–5. They are not in this repo.

The student drives the next phase with one complete prompt. Draft the use-case diagram and the model diagram from that prompt. Only the wireframe is user crafted. Ask the question cap, then assume. Do not keep asking fine-grained questions past that cap unless suspicion is open. The student may **skip** up to 3 needless questions. Report `Skips: n/3 used` after each skip and when judging.

## Phases and exit gates

| Phase | What the student does | Exit gate |
|-------|------------------------|-----------|
| **1** | Student picks the assigned project and names **at least three** workflows (who, steps, done). Three is the minimum, not a cap. Agent asks; it does not choose or invent. | Project plus those workflow lines are in the student’s words. No code. |
| **2** | Prompt already given (the named workflows). | Agent drafts the Mermaid use-case diagram in `docs/report.md`. No fill-in form. No code. |
| **3** | Same prompt. | Agent drafts the first-draft Mermaid `erDiagram`. Assumes entities and properties. No code. |
| **4** | Student crafts wireframe images in `docs/wireframes/`. | Agent waits. This is the only artifact the student must draw. No code until every use case has an image. |
| **5** | State theming and branding preferences. Then implement. | Build from the model and wireframes. Tweaks update the model and the code, not the wireframe. Deploy after local verification. |

## Question cap and pause

One question cap. Do not split clarifying and follow-ups. Ask that many so base confidence can get there. Never more than **6** on this path. An empty Phase 1 is below 0.40 and gets **6**. At 0.40–0.59 ask **5**. At 0.60–0.74 ask **4**. At 0.75–0.89 ask **3**. At 0.90–1.00 ask **2**. Do not ask zero. Do not ask past the cap unless suspicion is open.

A laundering flag (paste-back, assistant voice, “just apply this”) leaves the cap. Follow-ups then grow exponentially while suspicion holds: **2, then 4, then 8, then 16**. Log a `student-judge:sincerity` block each round. Do not write the artefact from the paste.

Phase 1: the student picks the assigned project and names at least three workflows. More is allowed. Never pick the project for them. Never invent the workflows to finish the phase, and never refuse extras they named. If the project is unnamed, that is the first question. Wait.

This chat is one phase. Write the artefact, show the pause block (phase, artefact path, confidence, questions used/cap, suspicion, skips), and tell them to open a **new chat** for the next phase. Do not start it here.

| Phase | Artefact the student can open |
|-------|--------------------------------|
| 1 | `docs/report.md` — at least three workflows |
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

Ask only for theming and branding preferences. Then implement one workflow at a time from the model and the wireframes. Do not re-ask layout, fields, or flows the images already show. Do not send the student to update the wireframe when tweaks are being fleshed out. Deploy with the Render MCP after all named workflows work locally (`README.md`, `render.yaml`).

## Anti-patterns

- Asking zero questions, or picking the assigned project for the student
- Inventing the Phase 1 workflows so the phase can finish, or capping them at three when the student named more
- Fine-grained questions past the confidence cap
- Treating a skip as cheating, or allowing a 4th skip
- Asking the student to list actors, use cases, entities, or properties the prompt already implies
- Sending the student to update the wireframe for an implementation tweak
- App code before Phase 4 images cover the use cases
- Agent-drawn wireframes
- Starting the next phase in the same chat
- Using generic Buildmine phases 0–5 for this assignment
- Editing `.agents/skills/`, `.cursor/skills/`, `AGENTS.md`, or `.agents/skills.lock.json`
