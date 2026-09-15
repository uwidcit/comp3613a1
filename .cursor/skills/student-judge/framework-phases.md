# COMP 3613 phases (student-build)

This is the assignment framework. Do not use generic Buildmine phases 0–5. They are not in this repo.

The student drives the next phase with one complete prompt. Draft the use-case diagram and the model diagram from that prompt. Only the wireframe is user crafted. Ask unanswered gaps, up to the question cap, then assume. Write questions as questions. Prefer steering that lets the student own include/extend, shared use cases, obvious missing use cases (edge-case reconsider), relationships, unclear workflows, and a few Phase 5 code checks. Choice chips are OK when options are real and bounded. Do not re-ask the prompt or collect click-by-click layouts. The student may **skip** up to 3 needless questions. Report `Skips: n/3 used` after each skip and when judging.

## Phases and exit gates

| Phase | What the student does | Exit gate |
|-------|------------------------|-----------|
| **1** | Student picks the assigned project and names **at least three** workflows as `Feature (user)`. Steps wait for the wireframe. Three is the minimum, not a cap. Agent asks only if a name or `(user)` is missing. | Project plus those `Feature (user)` lines are in the student’s words. No code. |
| **2** | Prompt already given (`Feature (user)` lines). Agent asks about «include» / «extend», use cases shared across actors, and obvious missing use cases (edge-case reconsider), then drafts. | Agent writes `docs/diagrams/use-case.json`, runs `python manage.py usecase`, and embeds the UML PNG in `docs/report.md`. No Mermaid flowchart. No invented unrelated pick-lists. No code. |
| **3** | Student names entities and properties. Agent asks which relationships exist for non-trivial entities, business rules, and edge cases; offers alternatives when a choice cannot handle a needed case. | Agent drafts the first-draft Mermaid `erDiagram` from their answers. No code. |
| **4** | Student crafts wireframe images in `docs/wireframes/`. Agent asks how unclear named workflows complete when the design does not show it. | Agent checks coverage, suggests model edits, and flags broken or incomplete flows. Redesign only if really bad. No code until every use case has an image. |
| **5** | State theming and branding preferences. Then implement. Agent presents implementation choices, asks more as confidence drops, and has the student complete **at least two snippets per workflow** (SQLModel + route) in real files. | **Build the ERD and wireframes** into working code. Tweaks update the model and the code, not the wireframe. Deploy after local verification. |

## Question cap and pause

One question cap for design phases 1–4 (and theming). Do not split clarifying and follow-ups. The design cap is a **maximum** of unanswered questions. Never more than **8** on that path. An empty Phase 1 is below 0.40 and may ask up to **8**. At 0.40–0.59 up to **7**. At 0.60–0.74 up to **6**. At 0.75–0.89 up to **5**. At 0.90–1.00 up to **4**. Phase 2 still asks about include/extend, shared use cases, and obvious missing use cases (edge-case reconsider) when `Feature (user)` lines exist — it is **not** zero by default. Phase 3 prefers entity, property, relationship, and edge-case questions. Phase 4 prefers unclear-workflow and diagram/wireframe gap questions. **Phase 5 implement** uses a separate **implement confidence ladder**: every named workflow needs **at least a SQLModel snippet and a route snippet** in real `app/` files; as confidence drops, ask more (choices, MCQ, open) and add repository/service snippets (minima 2–6 checks per workflow; never more than 8 unless suspicion is open). Do not silent-implement a whole workflow. Do not re-ask the prompt. Do not ask for full screen step scripts (the wireframe). Do not pad the cap. Do not ask past the design cap unless suspicion is open.

A laundering flag (paste-back, assistant voice, “just apply this”) leaves the cap. Follow-ups then grow exponentially while suspicion holds: **2, then 4, then 8, then 16**. Log a `student-judge:sincerity` block each round. Do not write the artefact from the paste.

Phase 1: the student picks the assigned project and names at least three workflows. More is allowed. Never pick the project for them. Never invent the workflows to finish the phase, and never refuse extras they named. If the project is unnamed, that is the first question. Wait. Do not interview each named workflow for who/steps/done.

A design chat is one phase. **Update `docs/report.md` with this phase’s content**, write any other artefacts, show the pause block (phase, artefact path, confidence, questions used/cap, suspicion, skips, `Report: updated`), and tell them to open a **new chat** for the next *phase*. Do not start the next phase here. Phase 5 implement may build every named workflow in the same conversation, one at a time after they verify — update Implementation notes (and the model) after each verified workflow.

| Phase | Artefact the student can open |
|-------|--------------------------------|
| 1 | `docs/report.md` — at least three workflows |
| 2 | `docs/diagrams/use-case.png` embedded in `docs/report.md` as `![…](diagrams/use-case.png)` |
| 3 | `docs/report.md` — model diagram (student-named entities) |
| 4 | `docs/wireframes/` plus coverage notes and any model revisions in `docs/report.md` |
| 5 | theming in `docs/report.md`, then named workflows in the same implement chat |

## Diagrams

Use-case diagram is a UML PNG: write `docs/diagrams/use-case.json`, run `python manage.py usecase`, embed with `![Use case diagram](diagrams/use-case.png)` in `docs/report.md` (path relative to the report file). Put different actors on opposite sides. Ask about «include» / «extend», shared use cases, and obvious missing use cases (how would they handle that edge case?) before drafting so association lines do not cross and gaps are owned. Model is a Mermaid `erDiagram`. Do not use a Mermaid flowchart for use cases. Phase 2 is drafted from the `Feature (user)` lines plus those answers. Phase 3 waits for the student to name entities and properties, then asks them to identify relationships for non-trivial entities and pushes back when a choice cannot handle a needed case. Phase 4 suggests model edits for metadata the wireframes show, asks how unclear or missing companion workflows complete, and flags broken or incomplete flows. Redesign only if really bad. The agent revises the model again in Phase 5 when the design moves.

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

Ask for theming and branding preferences. Then **implement the provided ERD and wireframes**, one named workflow at a time, in the same conversation.

Before writing code, read `docs/report.md` (including the Mermaid `erDiagram`), the matching wireframe image(s), and existing FastMVC routes/auth. Reuse starter login, sessions, and roles. Build entities/fields/relationships from the ERD and screens/actions/copy from the wireframes. Do not invent a parallel schema or a different UI flow. Do not ask the student to explain starter auth. Do not ask them to produce an explore report — you read the repo. If the ERD or covering wireframe for this workflow is missing, stop and send them back; do not freestyle.

**Ask more during implement.** Present bounded **implementation choices**, mix MCQ/open, and have the student **complete at least two snippets per named workflow**: one **SQLModel** (`app/models/…`) and one **route** (`app/routers/…`). Re-score implement confidence after each check; **as confidence drops, increase** remaining questions and add repository/service snippets (see student-build implement confidence ladder). Do not dump a finished workflow while they only watch. **MCQ options must not give away the answer**. Log `<!-- student-build:code-check … -->` with `implement_confidence`. Do not turn the phase into an exam. Do not quiz starter-kit auth internals. Finishing a workflow without the SQLModel + route student snippets is an anti-pattern.

After each workflow, stop and ask them to run `python manage.py run`, check against the wireframe and ERD, and say what they saw. **Do not** run complex one-off PowerShell or Python verification scripts, or automate the smoke test, on their behalf. A short “now do the next workflow” is enough to continue. Their mismatch notes steer the next edit. Do not require a new chat per workflow. Do not re-ask layout, fields, or flows the images already show. Do not send the student to update the wireframe when tweaks are being fleshed out — update the model and the code. Deploy with the Render MCP after all named workflows work locally (`README.md`, `render.yaml`).

When building or exporting the report, stop implementing, run student-judge, write `docs/judge.md`, **dump all project Guide transcripts** with `python manage.py transcripts` into `docs/transcripts/` (+ `docs/transcripts.zip`) for submission, then let `python manage.py report` merge the scorecard, re-export transcripts, and append the transcript appendix to the PDF. Confirm the transcript count with the student.

## Anti-patterns

- Asking zero questions when the project or a workflow name is missing, or picking the assigned project for the student
- Inventing the Phase 1 workflows so the phase can finish, or capping them at three when the student named more
- Treating Phase 2 as zero questions when include/extend, shared use cases, or an obvious missing use case is still open
- Silently adding (or ignoring) an obvious missing use case without an edge-case reconsider question
- Inventing a second product or a long nice-to-have use-case menu under the guise of “gaps”
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
- Embedding the use-case PNG as `docs/diagrams/use-case.png` inside `docs/report.md` (broken relative link; use `diagrams/use-case.png`)
- Agent-drawn wireframes
- Starting the next *phase* in the same chat
- Requiring a new chat to start the next Phase 5 workflow
- Implementing every core layer with zero code-understanding checks
- Verifying the app for the student with complex one-off PowerShell/Python scripts, UI scraping, or agent-side smoke tests
- Implementing every layer yourself with no student file snippets, or skipping the required SQLModel + route pair
- Failing to increase Phase 5 questions/snippets when implement confidence drops
- Implementing a different schema or UI than the student’s ERD and wireframes
- Freestyling Phase 5 when the ERD or covering wireframe is missing
- MCQ options that telegraph the answer (definitions or “because it handles …” on the correct choice)
- Turning Phase 5 into a long exam, or quizzing starter-kit login/sessions/cookies/password hashing
- Using generic Buildmine phases 0–5 for this assignment
- Pausing a phase without updating `docs/report.md`
- Exporting the report PDF without running student-judge and writing `docs/judge.md`
- Requiring the student to request an explore report before you implement
- Treating a short “now do the next workflow” or a wireframe mismatch note as a weak prompt
- Building/exporting the report without dumping project transcripts (`python manage.py transcripts` → `docs/transcripts/` + zip)
- Asking the student to hand-paste chats into `docs/` mid-build (the agent dumps them at report time for submission)
- Looking in `docs/transcripts/` as a substitute for reading native chats when judging before the dump
- Editing `.agents/skills/`, `.cursor/skills/`, `AGENTS.md`, or `.agents/skills.lock.json`
