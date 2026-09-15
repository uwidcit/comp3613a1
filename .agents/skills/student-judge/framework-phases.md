# COMP 3613 phases (student-build)

This is the assignment framework. Do not use generic Buildmine phases 0–5. They are not in this repo.

The student drives the next phase with one complete prompt. Draft the use-case diagram and the model diagram from that prompt. Only the wireframe is user crafted. Ask unanswered gaps, up to the question cap, then assume. Write questions as questions. Prefer steering that lets the student own include/extend, relationships, unclear workflows, and a few Phase 5 code checks. Choice chips are OK when options are real and bounded. Do not re-ask the prompt or collect click-by-click layouts. The student may **skip** up to 3 needless questions. Report `Skips: n/3 used` after each skip and when judging.

## Phases and exit gates

| Phase | What the student does | Exit gate |
|-------|------------------------|-----------|
| **1** | Student picks the assigned project and names **at least three** workflows as `Feature (user)`. Steps wait for the wireframe. Three is the minimum, not a cap. Agent asks only if a name or `(user)` is missing. | Project plus those `Feature (user)` lines are in the student’s words. No code. |
| **2** | Prompt already given (`Feature (user)` lines). Agent asks about «include» / «extend» and use cases shared across actors, then drafts. | Agent writes `docs/diagrams/use-case.json`, runs `python manage.py usecase`, and embeds the UML PNG in `docs/report.md`. No Mermaid flowchart. No invented unrelated pick-lists. No code. |
| **3** | Student names entities and properties. Agent asks which relationships exist for non-trivial entities, business rules, and edge cases; offers alternatives when a choice cannot handle a needed case. | Agent drafts the first-draft Mermaid `erDiagram` from their answers. No code. |
| **4** | Student crafts wireframe images in `docs/wireframes/`. Agent asks how unclear named workflows complete when the design does not show it. | Agent checks coverage, suggests model edits, and flags broken or incomplete flows. Redesign only if really bad. No code until every use case has an image. |
| **5** | State theming and branding preferences. Then implement. Agent runs a few light code-understanding checks (MCQ, open answer, or a layer snippet). | Build from the model and wireframes. Tweaks update the model and the code, not the wireframe. Deploy after local verification. |

## Question cap and pause

One question cap. Do not split clarifying and follow-ups. The cap is a **maximum** of unanswered questions. Never more than **8** on this path. An empty Phase 1 is below 0.40 and may ask up to **8**. At 0.40–0.59 up to **7**. At 0.60–0.74 up to **6**. At 0.75–0.89 up to **5**. At 0.90–1.00 up to **4**. Phase 2 still asks about include/extend and shared use cases when `Feature (user)` lines exist — it is **not** zero by default. Phase 3 prefers entity, property, relationship, and edge-case questions. Phase 4 prefers unclear-workflow questions. Phase 5 prefers a few service/repository understanding checks, not starter auth. Do not re-ask the prompt. Do not ask for full screen step scripts (the wireframe). Do not pad the cap. Do not ask past the cap unless suspicion is open.

A laundering flag (paste-back, assistant voice, “just apply this”) leaves the cap. Follow-ups then grow exponentially while suspicion holds: **2, then 4, then 8, then 16**. Log a `student-judge:sincerity` block each round. Do not write the artefact from the paste.

Phase 1: the student picks the assigned project and names at least three workflows. More is allowed. Never pick the project for them. Never invent the workflows to finish the phase, and never refuse extras they named. If the project is unnamed, that is the first question. Wait. Do not interview each named workflow for who/steps/done.

A design chat is one phase. Write the artefact, show the pause block (phase, artefact path, confidence, questions used/cap, suspicion, skips), and tell them to open a **new chat** for the next *phase*. Do not start the next phase here. Phase 5 implement may build every named workflow in the same conversation, one at a time after they verify.

| Phase | Artefact the student can open |
|-------|--------------------------------|
| 1 | `docs/report.md` — at least three workflows |
| 2 | `docs/diagrams/use-case.png` embedded in `docs/report.md` |
| 3 | `docs/report.md` — model diagram (student-named entities) |
| 4 | `docs/wireframes/` plus coverage notes and any model revisions in `docs/report.md` |
| 5 | theming in `docs/report.md`, then named workflows in the same implement chat |

## Diagrams

Use-case diagram is a UML PNG: write `docs/diagrams/use-case.json`, run `python manage.py usecase`, embed `docs/diagrams/use-case.png` in `docs/report.md`. Put different actors on opposite sides. Ask about «include» / «extend» and shared use cases before drafting so association lines do not cross. Model is a Mermaid `erDiagram`. Do not use a Mermaid flowchart for use cases. Phase 2 is drafted from the `Feature (user)` lines plus those answers. Phase 3 waits for the student to name entities and properties, then asks them to identify relationships for non-trivial entities and pushes back when a choice cannot handle a needed case. Phase 4 suggests model edits for metadata the wireframes show, asks how unclear workflows complete, and flags broken or incomplete flows. Redesign only if really bad. The agent revises the model again in Phase 5 when the design moves.

## Wireframes

The agent does not draw them. Wait until image files are in `docs/wireframes/`. Coverage is a file check first. After coverage, compare each image to the model, suggest missing metadata, raise unoptimized, incomplete, or broken workflows, and ask how a named workflow finishes when that path is not obvious from the design. Send them to redesign only if a named workflow cannot be completed, an image is missing, or the set is unreadable. One coverage block per use case:

```text
<!-- student-build:wireframe-coverage
use_case: <name>
image: docs/wireframes/<file>
covered: yes|no
-->
```

## Phase 5

Ask for theming and branding preferences. Then implement one workflow at a time from the model and the wireframes, in the same conversation.

Before writing code, read `docs/report.md`, the matching wireframe, and existing FastMVC routes/auth. Reuse starter login, sessions, and roles. Do not ask the student to explain starter auth. Do not ask them to produce an explore report — you read the repo.

For a few core implementations, gauge code understanding with a short MCQ, open answer, or a student-written snippet in the correct layer file (repository vs service vs thin router). Prefer the service/repository pattern in this repo. Log `<!-- student-build:code-check … -->`. Do not turn the phase into an exam. Do not quiz starter-kit auth internals.

After each workflow, stop and ask them to check the running app against the wireframe and say what they saw. A short “now do the next workflow” is enough to continue. Their mismatch notes steer the next edit. Do not require a new chat per workflow. Do not re-ask layout, fields, or flows the images already show. Do not send the student to update the wireframe when tweaks are being fleshed out. Deploy with the Render MCP after all named workflows work locally (`README.md`, `render.yaml`).

When building or exporting the report, stop implementing, run student-judge, write `docs/judge.md`, and let `python manage.py report` append that scorecard under Competency.

## Anti-patterns

- Asking zero questions when the project or a workflow name is missing, or picking the assigned project for the student
- Inventing the Phase 1 workflows so the phase can finish, or capping them at three when the student named more
- Treating Phase 2 as zero questions when include/extend or shared use cases are still open
- Fine-grained questions past the confidence cap
- Re-asking the opening prompt, or asking for full click-by-click layouts the wireframe will show
- Invented choice chips, or chips used to withhold a draft
- Withholding a Phase 2 or 3 draft forever until they pick an option (ask within the cap, then write)
- Treating “that’s in the prompt” or “steps are in the wireframe” as a skip
- Treating a skip as cheating, or allowing a 4th skip
- Asking the student to re-list every actor or use case the prompt already named
- Inventing Phase 3 entities or properties, or offering an entity pick-list
- Drafting the ERD without asking which relationships non-trivial entities need
- Silently accepting a relationship that cannot handle a concrete case the workflows need
- Applying wireframe-derived model fields without asking, or inventing fields the images do not show
- Skipping questions about a named workflow whose path is not obvious from the wireframe
- Sending the student to redesign a wireframe that is only unoptimized or missing a field
- Sending the student to update the wireframe for an implementation tweak
- App code before Phase 4 images cover the use cases
- Mermaid flowchart (stadium/circle + rectangles) as the use-case diagram
- Using GenerateImage or a hand-drawn UML instead of `python manage.py usecase`
- Agent-drawn wireframes
- Starting the next *phase* in the same chat
- Requiring a new chat to start the next Phase 5 workflow
- Implementing every core layer with zero code-understanding checks
- Turning Phase 5 into a long exam, or quizzing starter-kit login/sessions/cookies/password hashing
- Using generic Buildmine phases 0–5 for this assignment
- Exporting the report PDF without running student-judge and writing `docs/judge.md`
- Requiring the student to request an explore report before you implement
- Treating a short “now do the next workflow” or a wireframe mismatch note as a weak prompt
- Looking in `docs/` for chat transcripts, or asking the student to dump chats there
- Editing `.agents/skills/`, `.cursor/skills/`, `AGENTS.md`, or `.agents/skills.lock.json`
