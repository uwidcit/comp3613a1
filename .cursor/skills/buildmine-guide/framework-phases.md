# Buildmine phases (agent reference)

Use with **buildmine-guide** and **buildmine-judge**. Full narrative: course student guide if provided; otherwise this table + your assignment brief.

## Components (every serious app)

- Viewport **shell** (sticky chrome, pane scroll)
- **Auth + roles** (member vs admin/staff)
- **Schema + seed/import** (real-ish data)
- **Member** primary path
- **Admin** parity (same chrome, more power)
- Shared kit: labeled **FAB → modal**, tabs, fill-tables, **URL state**
- Ops: local≠prod, deploy, later perf/security

## Phases & exit gates

| Phase | Name | Exit gate (student must meet) |
|-------|------|-------------------------------|
| **0** | Intent & users | Paragraph: users, primary job, assets. No code. |
| **1** | UI surface | Click primary path on sample data; explain each screen. |
| **2** | Spec / schema / auth / seed | Explain entities + R/W by role; seed runs clean. |
| **3** | Feature slices | ≥1 vertical slice works E2E; student can demo unaided. |
| **4** | Role parity & workflows | Demo both roles; backend/rules enforce access. |
| **5** | Harden & ship | Deployed/submitted; top mitigated risk + one deferred risk named. |

## Feature-slice loop (Phase 3+)

Explore → structured report → **student Decision** → implement one slice → **student verifies** → polish.

## Standing defaults

- UI before API unless schema-heavy domain
- Create/edit on existing list → modal + FAB (not a new page)
- Admin chrome matches member
- Ephemeral UI state in URL search params
- Density via restructure, not cramped fonts
- Explore before large edits on big codebases

## Anti-patterns (penalize in Judge; block in Guide)

- Whole-app / answer-seeking prompts
- Implement without explore/decision on non-trivial codebases
- Admin UI before member path (when member is in scope)
- Local UI → prod API
- Schema/roles the student cannot explain
- “Done” claimed without verification evidence
