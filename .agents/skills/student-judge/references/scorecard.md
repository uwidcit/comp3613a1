# Scorecard output (student-judge)

Use this template when writing `docs/judge.md` and the in-chat scorecard.

## Output format (required)

```markdown
# student-judge competency report

**Student / session:** …
**Artifact:** Guide chats for this project (Cursor and/or Copilot/OpenCode) and/or `docs/transcripts` dump
**Phases in evidence:** 1–6 (COMP 3613; Phase 5 polish, Phase 6 deploy; never generic 0–5)

### Totals
| | Count / value |
|--|--|
| Metrics on rubric | 12 (M1–M12) |
| N/A (excluded) | 0 or list: M… (reason) |
| Metrics scored | N |
| Scoreable max | N × 4 |
| Awarded total | X / (N × 4) |
| **Overall (avg of scored)** | **X.X / 4** |
| Impression mark | K / 20 |

## Scorecard

| ID | Metric | Score / 4 | In avg | Evidence |
|----|--------|----------:|:------:|----------|
| M1 | Phase discipline | 3 | yes | … |
| M7 | Slice explanation | N/A | no | … |

## Strengths
- …

## Gaps (priority order)
1. … (only gaps still true **after this fresh evidence pass** and only where the student had an **opportunity**. Remove fixed items. **Do** list first-build-only Phase 5 with no polish when that happened. **Do** list architecture breaks (SQL/`select`/`db.exec` in student route snippets or final routers) when evidence shows them. **Never** list: starter auth lecture, explore report, final all-workflow walkthrough as a ritual, missing file snippets when Guide never asked, or missing Cursor JSONL when Copilot/OpenCode and/or `docs/transcripts.zip` is the record)

## Phase gate status
| Phase | Status | Note |
|-------|--------|------|
| 1 | met / partial / not met / N/A | … |
| 2 | … | … |
| 3 | … | … |
| 4 | … | … |
| 5 | … | theme/build/**polish**; not met if only first dump |
| 6 | … | deploy URL + marker logins |

## Recommended next practice
- One concrete exercise tied to the weakest **scored** metric (not “explain AuthDep”, not “write an explore report”).

## Integrity note
- Clean | Suspected external assist / paste-back | Cleared after suspicion spiral | Edited skills | Concerns: …
## Provenance flags
- None | List red flags with turn references
## Sincerity log summary
- Blocks found: N | max round: R | min/mean/final confidence: … | trend: … | cleared: yes/no/abandoned
## Skips
- Skips: n/3 used (from Guide). Skips are not an integrity failure.
```

## Calibration

- **High overall (≥3.2)** — Ideal FastStarter session: student named workflows and entities, answered include/extend and relationship questions, engaged obvious-gap reconsider questions lightly, supplied wireframes, clarified unclear flows, attempted Phase 5 code checks with **architecture-respecting** snippets (thin routes → services → repositories), **steered polish** (verify notes, UI/workflow/model refinements), verified locally. Agent was primary implementer. Integrity clean. Incomplete **Phase 6** deploy can still be high if Phase 5 polish is met (note Phase 6 partial). **Not** high if they only accepted the first build, or if their snippets put SQL in routers.
- **Mid (2.0–3.1)** — Missing student-owned artefacts (no `Feature (user)` lines, invented entities, no wireframes), they accepted the first dump / broken mismatches without polish, **or** fat-route SQL persisted after Guide asked for layered code.
- **Low (&lt;2.0)** — Answer-seeking, skipped gates, little verification, agent invented the product, **or** likely paste-back / abandoned suspicion spiral.

If **Suspected external assist**, overall must reflect discounted M3/M7/M10/M11/M12 even when the final app looks complete.

Do **not** place an ideal engagement session in mid because prompts were short, the agent wrote the code, or `docs/` has no chat logs. Do **not** score only the export chat when other native phase transcripts exist.
