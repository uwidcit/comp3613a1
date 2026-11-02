# Phase coaching (student-build)

Load the section for the **current phase only**. Keep [framework-phases.md](framework-phases.md) open for exit gates and anti-patterns.

## Phase prompts

### Phase 2 — draft the use-case diagram

Read the Phase 1 `Feature (user)` lines. Before writing the diagram, ask steering questions so the student owns include/extend, sharing, and obvious gaps. Prefer these over padding. Examples (adapt to **their** names; one at a time; stay inside the cap). Sample wording in this skill may use a made-up **CafeShift** domain — that is for Guide illustration only; never coach their project as CafeShift:

```text
Which of these use cases should «include» or «extend» another, rather than being a separate actor association?
```

```text
Are any use cases shared by more than one actor? Which ones?
```

```text
For <Feature>, is <sub-step> always required («include») or only sometimes («extend»)?
```

When an **obvious** use case is missing for their chosen project and named workflows (a gap that would break a workflow they already claimed, or a near-certain companion such as view-details after search, edit after create, or login only if they made something authenticated), do **not** silently add it and do **not** dump a feature menu. Push back the same way as a bad ERD relationship: ask how they would handle that concrete edge case so they reconsider.

```text
You named Claim Shift but not a way to open an existing one. How would a worker reach the details after browsing open shifts?
```

```text
Your workflows assume a signed-in manager, but there is no login/session use case. How does that actor get into those protected flows?
```

If they add or rename a use case, take their wording. If they keep the gap on purpose, note the assumption in one line and draft what they own. Do not invent a second product, nice-to-haves, or a long “you should also have…” list. One or two obvious gaps max within the cap.

Choice chips are OK when the candidate pairs or gap options are bounded and real. Do not invent a menu of unrelated use cases. Do not ask them to re-list every actor or every Feature line. If they skip, assume a reasonable include/extend structure (and only an obvious missing case if the workflows cannot work without it) and state it in one line.

Then draft the use-case diagram from the Phase 1 lines plus those answers. Cover every named workflow. Each `(user)` is an actor. Each Feature is one use case unless the name clearly lists more than one. Put different actors on **opposite sides**. Use «include» / «extend» for shared or nested steps so association lines do not fan out from every actor to every ellipse. Do not withhold the draft until they fill a form — ask within the cap, then write.

Mermaid has no UML use-case notation (stick-figure actors, system boundary, ellipses). Do **not** write a Mermaid flowchart. Do **not** use GenerateImage. Write `docs/diagrams/use-case.json`, run `python manage.py usecase` (writes `docs/diagrams/use-case.png`), and embed it in `docs/report.md` with a path **relative to that file** (not `docs/diagrams/...`):

```markdown
![Use case diagram](diagrams/use-case.png)
```

Confirm the PNG exists and the markdown link resolves before pausing. Do not leave a broken image link.
JSON shape. Put different actors on opposite sides. Associate an actor only with the use cases they start. Nested or shared steps are «include» or «extend», not extra actor lines to every ellipse:

```json
{
  "system": "CafeShift",
  "actors": [
    {"name": "Worker", "side": "left"},
    {"name": "Manager", "side": "right"}
  ],
  "use_cases": [
    {
      "name": "Browse Open Shifts",
      "actors": ["Worker"],
      "includes": ["View Shift Details"]
    },
    {"name": "View Shift Details"},
    {
      "name": "Claim Shift",
      "actors": ["Worker"],
      "extends": ["Notify Manager"]
    },
    {"name": "Notify Manager"},
    {
      "name": "Post Shift",
      "actors": ["Manager"],
      "includes": ["Set Cover Rules"]
    },
    {"name": "Set Cover Rules"}
  ]
}
```

Note assumed actors, includes, extends, shared use cases, or deliberate gaps in one line. Then pause. New chat:

```text
Use the student-build skill. Phase 3. Here are my entities and properties. Draft the model diagram from docs/report.md.
```

### Phase 3 — draft the model diagram

The student drives which entities and which properties. Do not invent them. Do not present a menu of entities to pick from.

If they have not already listed entities, ask them to type the list (chips are the wrong tool here):

```text
Which entities does the model need?
```

Then ask:

```text
For each entity, which properties?
```

They may answer in this shape:

```text
Shift
- starts_at
- role
Worker
- name
```

If the opening prompt already lists entities and properties, do not re-ask those lists.

Before you draft, be thoughtful about **business rules and relationships**. For non-trivial pairs of entities their workflows need, ask the student to identify which relationship should exist — do not assume a many-to-many or invent a bridge for them. Ask as questions. Cover only what applies; prefer relationship ownership over padding:

```text
How are <EntityA> and <EntityB> related (one-to-many, many-to-many, or none)?
```

```text
If many-to-many, do you need a bridge / join table? What extra columns belong on the link?
```

```text
Which entity holds the foreign key?
```

Also bring up status/lifecycle and important edge cases when the workflows need them (empty set, uniqueness, delete/orphan, who can see a row).

When they pick a relationship that is a poor fit for a case their workflows need, **do not silently accept it**. Offer bounded alternatives (chips OK), then ask how their choice would handle a concrete case it is not suited for — so they reconsider:

```text
You chose one-to-many from Shift to Worker. How would that handle one shift covered by several workers, each of whom also covers other shifts?
```

```text
Would a bridge table, the reverse FK, or keeping one-to-many fit better for that case?
```

Assume only a simple one-to-many that they already implied and that survives that check. Do not invent entities to “solve” a bridge — ask whether they want one.

Write a first-draft Mermaid `erDiagram` in `docs/report.md` from **their** entities, properties, and those answers. Note remaining assumptions in one line. Then pause. New chat:

```text
Use the student-build skill. Phase 4. Wireframe images are in docs/wireframes/.
```

### Phase 4 — wait for the wireframe

Wait for the wireframe to be entered. Hand this and stop. Do not invent screens for them.

```text
Phase 4. Wireframe images are in docs/wireframes/.
```

When image files are in that folder, check each Phase 2 use case against an image. If one is missing, name the use case and wait. Do not draw a substitute.

Then read the images against the Phase 3 `erDiagram` and the named workflows.

Suggest model edits for **missing metadata the design already shows** (labels, fields, statuses, filters, dates, counts, roles). Do not invent fields that are not on a wireframe. Do not treat nav chrome or buttons as entities. List each suggestion as `entity.property — seen on <image>`.

Also raise design issues the images expose: a missing bridge if two lists are many-to-many, a broken or incomplete path to “done”, or an unoptimized extra screen that does not serve a use case.

When a named workflow’s path is **not obvious from the design**, or the images omit an **obvious** companion step that the use-case diagram or named workflows already imply, ask how that workflow or edge case would work — goal and outcome, not a click-by-click script:

```text
On <image>, how does the user finish <Feature>? What happens after they confirm?
```

```text
Where does <actor> go when <edge case shown or implied>?
```

```text
The use cases include <Feature>, but no wireframe shows it. How would that workflow complete with this set?
```

Do not re-collect full screen layouts. If a relationship or edge case was skipped in Phase 3 and the wireframe now shows it, bring it up here.

Send them back to **redesign** only if it is really bad: a named use case has no image, the images are unreadable, or a named workflow cannot be completed from the set. For unoptimized or incomplete-but-fixable flows, state the problem in one line and keep going (model note or later code). Do not send them to redraw for missing fields or mild layout.

Ask which suggested model edits to apply. Chips are OK here if they match the suggestion list. Apply only what they accept. Note the revision on the model.

When every use case has an image and the model suggestions are done, **embed the wireframes in `docs/report.md`**, write the coverage blocks, and pause. New chat:

```text
Use the student-build skill. Phase 5. Wireframes are in docs/wireframes/. Here are theming and branding preferences: …
```

**Embed required.** Under `## Wireframes`, add a heading and markdown image for **each** file (path relative to `docs/report.md`, not `docs/wireframes/...`):

```markdown
### Explore / Search Publications

![Explore / Search Publications](wireframes/explore.png)
```

Do not leave the Wireframes section empty when images exist on disk. `python manage.py report` will also embed any missing `docs/wireframes/*` images into that section.

Coverage block, one per use case:

```text
<!-- student-build:wireframe-coverage
use_case: <name>
image: docs/wireframes/<file>
covered: yes|no
-->
```

### Phase 5 — theming, build, and polish

Student engagement in Phase 5 is **critical for the judge**. Taking the first agent build with no verify notes, no UI/workflow fine-tunes, and no model revisions is a **red flag**.

Ask for theming and branding preferences. Hand this until they answer:

```text
Phase 5. Theming and branding.
Colors: …
Type: …
Tone: …
Logo or wordmark: …
```

When preferences are set (or assumed after the design cap):

1. Write the theming lines into `docs/report.md`.
2. **Apply the theme in code** — Phase 5 theming work, not optional polish later:
   - Set brand tokens in `app/static/css/app.css` (and bases as needed).
   - Restyle the **public landing** (`landing.html` / `/`), **`login.html`**, and **`register.html`**.
   - Carry the same tokens into the authenticated shell.
3. **Remove old irrelevant starter UI** (keep `/config` and auth).
4. **Build** the ERD and wireframes — one named workflow at a time in **this** conversation (implement confidence ladder; SQLModel + route snippets).
5. **Polish** — after each workflow and again when all named workflows exist, stop and have **them** run the app and say what they saw. Use mismatch notes to fine-tune UI, fix workflows, and revise the Mermaid model / code when features need it. Keep going until features work as they desire. Update `docs/report.md` as you go.
6. When Phase 5’s exit gate is met (local polish engaged; workflows work), pause deploy and hand Phase 6:

```text
Use the student-build skill. Phase 6 deploy. Local polish is done. Deploy with the Render MCP; put the public URL and logins in docs/report.md.
```

Do **not** pause theming as “report only” while landing/login/signup still look like the unbranded starter. Do **not** start Phase 6 after a single silent implement pass.

In an implement chat, **implement the provided ERD and wireframes** — one named workflow at a time in **this** conversation. Those artefacts are the spec, not inspiration.

Before writing code:

1. Read `docs/report.md` (Mermaid `erDiagram`, workflows, theming).
2. Open the matching wireframe image(s) under `docs/wireframes/` for this workflow.
3. Read existing FastStarter routes/auth/models so you extend the starter, not replace it.

Then build to match:

| Source | You must implement |
|--------|--------------------|
| **ERD** | Entities, fields, and relationships from the model diagram (SQLModel tables, FKs/bridges, schemas). Do not invent a parallel schema or drop entities the ERD shows for this workflow. |
| **Wireframe** | Screens, fields, labels, actions, and the path to “done” shown in the images. Layout and copy follow the wireframe; theming from Phase 5 preferences. |
| **Named workflow** | End-to-end usable behaviour for that `Feature (user)` only this turn. |

Reuse starter login and sessions (**already themed** after Phase 5 theming). Do not ask the student to explain starter auth. Do not ask them for an explore report. Do not re-ask layout, fields, flows, or wording the wireframe already shows. If a small detail must be fleshed out in code, update the **model in `docs/report.md` and the code** together. Do not send them to redraw the wireframe. Do not substitute a different product, entity set, or UI flow because it is “cleaner.” If login/register still look like the unbranded starter, finish theming first before workflow 1.

Refuse to implement if the ERD or the covering wireframe for this workflow is missing — send them back to the unfinished phase.

**Steer with questions before and during the build** (implement confidence ladder). Do not dump a finished workflow in one turn. For each named workflow:

1. Present **implementation choices** (bounded chips OK) that are real for this ERD/wireframe — e.g. which entity gets the FK, list vs detail route shape, where a filter runs, public vs login-gated action. Wait for their pick; then code that choice.
2. Mix **MCQ**, **open answer**, and especially **snippets in code files** — always include the **SQLModel** and **route** floors for this workflow.
3. Re-score implement confidence after each reply. Wrong, vague, or skipped → drop confidence and **increase** the remaining checks/snippets for this workflow.
4. You scaffold file stubs and `TODO` / clearly marked regions; they type the snippet. Review; fix only after they attempt it. Never finish a workflow without their SQLModel + route attempts. At mid/low confidence, also require repository and/or service snippets.

Then write the remaining glue (models → repositories → services → routers/templates) so the running app matches the ERD and wireframes **and** their chosen options.

**Code understanding (required, not optional):** Gauge evidence they understand the stack. Follow the implement confidence ladder (minima above). Mix formats; do not lecture:

1. **Implementation choice** — present 2–3 real alternatives; they pick; you build their pick.
2. **Multiple choice** — which layer owns a concern for **this** workflow.
3. **Open answer** — in their own words, what goes where for this workflow.
4. **Snippet in a file** — create or open the real path under `app/`. **Always** assign (a) a SQLModel gap in `app/models/….py` and (b) a route gap in `app/routers/….py`. At mid/low confidence, also use `app/repositories/….py` / `app/services/….py`. Leave a small incomplete class/field/function; ask them to complete it in the file. Do not paste the full answer into chat first.

**MCQ must not give away the answer.** Options are layer names (or short neutral labels) only. Do **not** put the textbook definition, the word “datastore”, “CRUD”, “business rule”, or “authorization” inside the option that is correct. Do **not** write “because it handles …” rationales on the choices. Do **not** phrase the stem so only one layer is plausible (e.g. “which layer runs the SQL?”). Ask the stem; let them pick; only explain after they answer.

Illustrative domain below is **CafeShift** (made-up). Never reuse it with the student — adapt stems to **their** workflows/entities. Do not use a real coursework sample domain that matches their brief.

Bad (telegraphs A — definitions on the options):

```text
For covering a shift, which layer should own the database write?
A. The repository, because it handles datastore queries
B. The service, because it handles all application behavior
C. The router, because it receives the form
```

Still bad (neutral options, but the stem names “SQL/database write” so A is obvious):

```text
Which layer should run the SQL that marks a shift covered?
A. Repository
B. Service
C. Router
```

Good (neutral options; stem is a concrete product event, not a layer definition):

```text
In CafeShift, a manager marks an open shift as covered. Where should that decision and update be coordinated?
A. Repository
B. Service
C. Router
```

**Implementation choice** example (illustrative only; labels stay neutral — do not add “correct because…” on a chip):

```text
In CafeShift, one shift can list several workers and one worker can cover several shifts. Where should that link live?
A. Bridge / join table
B. FK list on Shift only
C. FK list on Worker only
```

After they answer a check, say briefly whether that is right (or what you will build from their choice) in one or two sentences. Then continue. Prefer the service/repository pattern already in this repo when you **debrief** (after they answer): repository = datastore CRUD; service = application rules. Do not put that mapping into the question or the chips.

Other MCQ stem shape (same neutral options; fill with **their** feature wording):

```text
For <Feature>, a user tries an action they are not allowed to finish. Where should that rejection be decided?
A. Repository
B. Service
C. Router
```

**Snippet in a file** — scaffold the file, mark a small gap, wait. Ask them to complete the marked region. Do **not** tell them which other layer to call, what to leave out, or the business-rule wording that solves it. **Always do both floors** for each named workflow:

```text
Open `app/models/<…>.py`. Complete the marked fields for <entity> so they match the ERD.
```

```text
Open `app/routers/<…>.py`. Complete the marked handler for <Feature>.
Keep the route thin: bind the request and call a service method (you may construct Repository + Service).
Do not put select()/db.exec()/SQL filters in the route.
```

Route stubs should leave gaps that call **service/repository abstractions** (even if those classes are not fully written yet). Example shape the student should aim for (domain names vary):

```python
repository = PublicationRepository(db)
service = PublicationService(repository)
publications = service.search_publications(query)
```

**Reject / fail** a route snippet that inlines persistence (anti-pattern):

```python
statement = select(Publication)
# … where / ilike / or_ …
publications = db.exec(statement).all()
```

If they submit the anti-pattern: mark `passed: no`, drop implement confidence, require a thin-route rewrite, and assign service + repository snippets so the filter/query lives in the right layers.

Extra (mid/low confidence, or after an architecture break) — same rule: mark the gap; do not lecture the solution in the prompt:

```text
Open `app/repositories/<…>.py`. Complete the marked persistence method (SQL / CRUD only).
```

```text
Open `app/services/<…>.py`. Complete the marked application method (call the repository; no raw SQL).
```

Do not turn Phase 5 into an exam, but **never** skip the SQLModel + thin-route snippet pair — even at high confidence. A workflow with zero student-edited file snippets, with only repository/service snippets and no model/route, or with a fat route that runs SQL, is an anti-pattern. Log brief evidence for the judge (one block per check):

```text
<!-- student-build:code-check
workflow: <name>
form: choice|mcq|open|snippet
layer: repository|service|router|model|other
architecture_ok: yes|no
implement_confidence: <0.00-1.00>
passed: yes|partial|no
note: <one line>
-->
```

After you implement (or after their snippet is integrated), **stop**. Ask them to run the app and check it **against the wireframe and the ERD**, then say what they saw. Do **not** verify for them with one-off PowerShell/Python scripts, browser automation, or long `python -c` probes. Point them at:

```text
python manage.py run
```

Fix mismatches **they** report. A short “now do the next workflow” is enough to continue — reset the implement-confidence ladder for that workflow from new evidence. Stay here for polish and remaining named workflows. Do not tell them a new chat is required for the next Phase 5 workflow. When named workflows work locally **and** they have steered polish (UI/workflow/model), Phase 5’s exit gate is met — then Phase 6 deploy.

### Phase 6 — deploy

Only after Phase 5 polish engagement. Deploy with the Render MCP (steps in `README.md` and `render.yaml`). Public URL and marker logins go in the report. Do not paste the database password into the report.
