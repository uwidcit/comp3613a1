<!-- student-build:skill-integrity
status: pass
root: 0505e5debc73d36e2be07ebce310571324cce5deb0bde5d1c6d8227d6b13e950
expected_root: 0505e5debc73d36e2be07ebce310571324cce5deb0bde5d1c6d8227d6b13e950
mismatches: none
-->

# COMP 3613 Assignment 1

Draft this file with the Guide. **Update it after every phase milestone** before you pause. The use-case diagram is a UML PNG at `docs/diagrams/use-case.png`, linked from this file as `diagrams/use-case.png` (path relative to `docs/report.md`). The model diagram is Mermaid. Link wireframe images as `wireframes/<file>` (files live in `docs/wireframes/`).

Do not put your student ID in this file if you will commit it. The PDF cover adds your name and ID at export time.

## Assigned project

## Problem interpretation

## Three workflows

### 1.

### 2.

### 3.

## Use case diagram

![Use case diagram](diagrams/use-case.png)

## Model diagram

First draft. Update this section in Phase 5 when polish revises the model, and note what changed.

```mermaid
erDiagram
  ENTITY ||--o{ OTHER : relates
```

## Wireframes

## Theming

Branding preferences and how they were applied (landing / login / register).

## Implementation notes

One named workflow at a time. Include verify notes and polish / model revisions (Phase 5). Do not treat the first build as final.

## Deployed app

Phase 6. Public Render URL (not localhost). Markers open this to mark the three workflows.

https://

## Logins

Every account a marker needs, including extra users you added. Starter accounts:

- bob / bobpass — regular user
- admin / adminpass — admin

## YouTube URL

## Session transcripts

Filled by `python manage.py report` from native agent chats. Students do not paste chats here during the build.

Exported **10** Guide chat(s) to `docs/transcripts/` (and `docs/transcripts.zip`).

Index: [docs/transcripts/INDEX.md](transcripts/INDEX.md)

- [`851240f2-e415-4b3f-8294-9774a9f44af7`](transcripts/851240f2-e415-4b3f-8294-9774a9f44af7.md)
- [`a940a2a4-6aa9-4c12-94d7-9e3481ff51c8`](transcripts/a940a2a4-6aa9-4c12-94d7-9e3481ff51c8.md)
- [`aa2c30f6-175e-4412-bfaa-bc4645ec977f`](transcripts/aa2c30f6-175e-4412-bfaa-bc4645ec977f.md)
- [`bdef6a85-8618-407b-a200-1214637046eb`](transcripts/bdef6a85-8618-407b-a200-1214637046eb.md)
- [`dc4f53b4-5ea1-46db-9351-2caa02f71a8f`](transcripts/dc4f53b4-5ea1-46db-9351-2caa02f71a8f.md)
- [`851240f2-e415-4b3f-8294-9774a9f44af7`](transcripts/851240f2-e415-4b3f-8294-9774a9f44af7.md)
- [`a940a2a4-6aa9-4c12-94d7-9e3481ff51c8`](transcripts/a940a2a4-6aa9-4c12-94d7-9e3481ff51c8.md)
- [`aa2c30f6-175e-4412-bfaa-bc4645ec977f`](transcripts/aa2c30f6-175e-4412-bfaa-bc4645ec977f.md)
- [`bdef6a85-8618-407b-a200-1214637046eb`](transcripts/bdef6a85-8618-407b-a200-1214637046eb.md)
- [`dc4f53b4-5ea1-46db-9351-2caa02f71a8f`](transcripts/dc4f53b4-5ea1-46db-9351-2caa02f71a8f.md)

## Competency (student-judge)

Filled when the report is built. Guide runs student-judge, writes `docs/judge.md`, and export appends the scorecard here.

## Skill integrity

Course skills are hashed at export and compared to `.agents/skills.lock.json`. Do not edit `.agents/skills/`, `.cursor/skills/`, or `AGENTS.md`.

- Status: **pass**
- Root: `0505e5debc73d36e2be07ebce310571324cce5deb0bde5d1c6d8227d6b13e950`
- none
