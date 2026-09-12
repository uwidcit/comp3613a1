# COMP 3613 Assignment 1 — 15%

**Individual** · this file lives in the FastMVC starter repo.

## Description

In this assignment you will interpret a **brief problem description**, decide what an MVP needs, identify **four main features / workflows**, model a solution, design a usable interface, and implement a working web application.

Build with **this** FastMVC template and develop with **Cursor**, **GitHub Copilot** (agent mode), or **OpenCode**, using the Buildmine Guide skill. Your process (not only the final code) will be assessed.

**GitHub Education (student license):** https://github.com/settings/education/benefits

Run and install steps: [README.md](README.md). Skill notes: [.agents/skills/README.md](.agents/skills/README.md).

## Learning outcomes

1. Produce a reasonably in-depth interpretation of a short problem brief (actors, goals, assumptions, edge cases, MVP scope).
2. Derive **exactly four** important MVP features / workflows from that brief (not a laundry list of extras).
3. Model entities and relationships that support those four features.
4. Design and implement a clean, usable UI on FastMVC.
5. Work with an LLM as a coach under Guide rules — you own decisions, verification, and explanations.

## Project selection

Refer to the assignment spreadsheet (myeLearning) for your **assigned** project. Each option is only a **problem brief**. You must interpret it and define the MVP yourself.

### 1. Alumni App

A CRM-style platform for the department / faculty to stay connected with graduates: alumni profiles, events, networking, and related engagement.

### 2. Internship Platform

A departmental system that takes student applications and distributes / matches them across internship positions offered by participating companies.

### 3. MyAdvisor

An app for students to track degree progress, plan semester course selections, and obtain approval from an administrator / advisor.

### 4. Research Platform

A submissions platform for research posters and presentations (submit, review/manage, and present status through the event lifecycle).

### 5. Student Awards (incentive system)

Students gain hours by volunteering, appear on a leaderboard, unlock milestones, and redeem progress for prizes / awards.

### 6. Student Accommodation

An Airbnb-like marketplace for finding nearby student accommodation: trusted listings, reviews, and tenant / booking management.

You may add minimal supporting behaviour (login, roles, seed data, navigation) required to make the four MVP features usable. Do **not** invent a second product. Depth on four solid features beats a shallow feature dump.

## Your job: interpret → four MVP features

The brief does **not** list features for you. In Phase 0 / your PDF you must:

1. Interpret the problem (actors, primary job, assumptions, edge cases, what is **out of scope** for MVP).
2. Name **exactly four** main MVP features / workflows.
3. For each of the four: who acts, step sequence, what “done” looks like.
4. Let those four drive your use cases, model, UI, and implementation.

Markers will exercise **your** four named workflows. If a named workflow cannot be completed in the UI, you lose marks for that area.

## Agents, Education license, and setup

Pick **one** agent. Skills are already in this repo (`.agents/skills/` and `.cursor/skills/`). Web chatbots do not load them.

**Student license:** sign in and apply at https://github.com/settings/education/benefits

Use a verified academic email if you have one (UWI: `@my.uwi.edu`). After approval, activate Copilot on that same page. Approval and Copilot activation are separate steps. If the student Copilot offer is not available, use **Copilot Free**. Do not buy a paid plan for this course.

- [Apply to GitHub Education](https://docs.github.com/en/education/about-github-education/github-education-for-students/apply-to-github-education-as-a-student)
- [Copilot for students](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-students)

### Cursor (Hobby, no card)

1. Install [Cursor](https://cursor.com) and stay on free **Hobby**.
2. **File → Open Folder** → this project root.
3. New **Agent** chat. Use `/buildmine-guide` or the prompt below.

### GitHub Copilot (agent mode)

Skills load only in **Agent** mode or the Copilot CLI — not inline autocomplete.

1. GitHub account, then the Education link above (or Copilot Free).
2. [VS Code](https://code.visualstudio.com/) + **GitHub Copilot** and **GitHub Copilot Chat**. Sign in.
3. Open this folder. Copilot Chat → mode **Agent** (not Ask, not Edit).
4. If the skill does not attach: `Use the buildmine-guide skill in .agents/skills/buildmine-guide/SKILL.md`.

Optional: [Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli) from this folder. It reads `AGENTS.md` and `.github/copilot-instructions.md`.

### OpenCode

Free client; you still need a model. Docs: https://opencode.ai/docs/

**Windows:** `npm install -g opencode-ai` (or `scoop install opencode` / `choco install opencode`). Desktop: https://opencode.ai/download

**macOS / Linux:**

```bash
curl -fsSL https://opencode.ai/install | bash
# or: brew install anomalyco/tap/opencode
# or: npm install -g opencode-ai
```

Then `cd` to this repo, run `opencode`, and `/connect` a model. **Do not run `/init`** — it overwrites `AGENTS.md`.

### App commands (after you clone)

```bash
python -m venv .venv
# activate the venv, then:
pip install -e .
# copy env.example to .env
python manage.py init
python manage.py seed
python manage.py run
```

Full detail: [README.md](README.md).

### Start Guide

```text
Use the buildmine-guide skill. I'm in Phase 0 for [assigned project].
Here is the problem brief: …
I will propose exactly 4 MVP features/workflows. Question me before coding.
```

One slice at a time. When finished: `Use the buildmine-judge skill on this session.`

### Allowed / not allowed

| Allowed | Not allowed as primary agent |
|---------|------------------------------|
| Cursor Hobby, Copilot **Agent** (or Copilot CLI), OpenCode | Ungarded ChatGPT / Claude / Gemini **web** |
| Copilot autocomplete alongside one of the agents above | Pasting a full external solution and saying “just apply this” |

## Deliverables

### A. Interpretation & four MVP features (PDF)

Actors, primary job, assumptions, out-of-scope items, edge cases, and **exactly four** named workflows with step sequences.

### B. Modelling & design (PDF)

Use case diagram, model diagram, UI wireframes for those four happy paths.

### C. Implementation (GitHub)

FastMVC web UI (not CLI-only), models matching the diagram, all four features usable end-to-end, seed data, README walkthroughs.

### D. Process evidence (PDF)

Public GitHub URL, deploy URL if required, which agent you used, optional transcript for Judge, account email on the cover page.

## Submission

One PDF via myeLearning:

1. Cover page — Name, ID, Assigned Project, GitHub, Deploy (if any), agent used, account email
2. Problem interpretation
3. The four MVP features / workflows
4. Use case diagram
5. Model diagram
6. UI wireframes / key screens
7. Implementation notes
8. Process note (agent + Guide / Judge)

## Marks

| Feature | Description | Marks |
| --- | --- | --- |
| Problem interpretation | In-depth reading of the brief; clear MVP boundary | 15 |
| Four MVP features / workflows | Exactly four; concrete, role-aware, drive model and UI | 15 |
| Use case diagram | Actors, coverage of your four, dependencies | 10 |
| Model diagram | Entities and relationships for the MVP | 15 |
| UI design & implementation | FastMVC; four features end-to-end; seed data | 35 |
| Process (Guide / Judge) | Cursor, Copilot Agent, or OpenCode; phased Guide work; integrity clean | 10 |
| **Total** |  | **100** |

## Notes

- Individual work. FastMVC boilerplate may be used and cited.
- LLMs only under Guide in Cursor, Copilot Agent, or OpenCode.
- Prefer four deep features over many shallow ones.
- Only `main` is graded unless stated otherwise.
