---
title: Harness Engineering: Leveraging Codex in an Agent-First World
author: OpenAI
url: https://openai.com/index/harness-engineering/
date: 2026-02-11
ingested: 2026-04-07
---

# Harness Engineering: Leveraging Codex in an Agent-First World

**Source:** [OpenAI](https://openai.com/index/harness-engineering/)
**Date:** February 11, 2026
**Key Premise:** A small team of OpenAI engineers built and shipped a production software product with **0 lines of manually-written code**, reducing development time by an estimated **90% (1/10th the time)**.

---

## 1. The Experiment: "Humans Steer, Agents Execute"
The project started in August 2025 with an empty repository. Over five months, a team (initially 3 engineers, now 7) used Codex (GPT-5) to generate **one million lines of code** across application logic, CI/CD, infrastructure, and documentation.

### Key Metrics
- **Codebase Size:** ~1,000,000 lines.
- **Throughput:** ~3.5 Pull Requests (PRs) per engineer, per day.
- **Human Role:** Designing environments, specifying intent, and building feedback loops.
- **Constraint:** No manually-written code allowed.

---

## 2. Redefining Engineering Work
The primary job shifted from writing code to **enabling agents**. When tasks failed, the solution was not to "prompt better," but to ask: *"What capability is missing, and how do we make it legible and enforceable for the agent?"*

### The "Ralph Wiggum Loop"
Engineers drive PRs by instructing Codex to:
1. Review its own changes locally.
2. Request specific agent reviews (local and cloud).
3. Respond to feedback.
4. Iterate until all agent reviewers are satisfied.

---

## 3. Increasing Application Legibility
To reduce the bottleneck of human QA, the team made the application state directly "readable" by Codex:
- **UI Legibility:** Wired Chrome DevTools Protocol into the agent runtime. Codex uses DOM snapshots and screenshots to reproduce bugs and validate UI fixes.
- **Observability Legibility:** Exposed logs (LogQL), metrics (PromQL), and traces (TraceQL) to Codex via ephemeral local stacks.
- **Autonomous Validation:** Codex can run tasks for 6+ hours, querying metrics to ensure performance targets (e.g., "service startup < 800ms") are met.

---

## 4. Repository Knowledge as the System of Record
The team abandoned monolithic instruction manuals in favor of **Progressive Disclosure**.

### The `AGENTS.md` Strategy
Instead of a giant manual, `AGENTS.md` acts as a **Table of Contents** (approx. 100 lines) pointing to a structured `docs/` directory.

**In-repository knowledge store layout:**
```text
AGENTS.md
ARCHITECTURE.md
docs/
├── design-docs/
│   ├── index.md
│   └── core-beliefs.md
├── exec-plans/
│   ├── active/
│   ├── completed/
│   └── tech-debt-tracker.md
├── generated/
│   └── db-schema.md
├── product-specs/
│   ├── index.md
│   └── new-user-onboarding.md
├── references/
│   ├── design-system-reference-llms.txt
│   └── nixpacks-llms.txt
└── [DESIGN/FRONTEND/PLANS/QUALITY_SCORE].md
```

> **Insight:** "What Codex can’t see doesn’t exist." All context (Slack decisions, design docs) must be encoded into the repo as Markdown to be accessible to the agent.

---

## 5. Enforcing Architecture and "Taste"
Agents require **strict boundaries** to prevent architectural drift. The team implemented a rigid, layered domain architecture:
- **Directional Dependencies:** `Types → Config → Repo → Service → Runtime → UI`.
- **Mechanical Enforcement:** Custom Codex-generated linters and structural tests block illegal dependency edges.
- **Taste Invariants:** Static enforcement of naming conventions, file size limits, and structured logging.
- **Remediation:** Linter error messages are written specifically to provide "remediation instructions" for the agent's context.

---

## 6. Managing Entropy: "Garbage Collection"
To prevent "AI slop" (suboptimal patterns replicated by the model), the team uses **Golden Principles**:
1. **Centralized Invariants:** Prefer shared utility packages over hand-rolled helpers.
2. **Boundary Validation:** No "YOLO-style" data probing; use typed SDKs or validated boundaries.
3. **Automated Cleanup:** Background Codex tasks scan for deviations and open refactoring PRs on a regular cadence.

---

## 7. Current State of Autonomy
The system has reached a threshold where a single prompt allows an agent to:
- Reproduce a bug and **record a video** of the failure.
- Implement and validate a fix.
- **Record a second video** of the resolution.
- Open, iterate on, and merge the PR, escalating to humans only for judgment calls.

> **Conclusion:** "Building software still demands discipline, but the discipline shows up more in the scaffolding rather than the code."
