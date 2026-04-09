---
title: Harness Decision Matrix
created: 2026-04-07
updated: 2026-04-07
type: comparison
tags: [comparison, benchmark, code-quality]
sources: [raw/articles/openai-unlocking-codex-harness.md, raw/articles/openai-harness-engineering.md, raw/articles/anthropic-effective-harnesses.md, raw/articles/anthropic-harness-design-long-running-apps.md, raw/articles/anthropic-claude-code-overview.md, raw/articles/hermes-agent-github.md, raw/articles/hermes-agent-api-server-docs.md, raw/articles/newstack-openclaw-vs-hermes.md, raw/articles/openclaw-agent-runtime-docs.md, raw/articles/yegge-future-of-coding-agents.md, raw/articles/yegge-gas-town-emergency-user-manual.md, raw/articles/yegge-welcome-to-the-wasteland.md]
---

# Harness Decision Matrix

## Purpose
This page converts the qualitative comparisons in [[harness-quality-comparison]] and [[harness-architecture-comparison]] into a decision table suitable for design choice rather than mere literary appreciation. The numbers are provisional and literature-grounded, not benchmark scripture.

## Scoring rubric
Use a 1-5 scale with 0.5 increments.
Weighted total = sum(weight × score / 5).

| Criterion | Weight | Meaning |
| :--- | :--- | :--- |
| Architecture cleanliness and legibility | 20 | Protocol clarity, session model clarity, and repo/system-of-record discipline |
| State continuity | 20 | Memory persistence, resumability, and recovery after context loss |
| Evaluation and review rigor | 20 | Explicit QA loops, evaluator separation, and reality-bearing verification |
| Work primitives and orchestration power | 15 | Richness of work representation and coordination model |
| Operational trustworthiness | 15 | Safety controls, permissions, and stability or migration risk |
| Surface breadth and reuse | 10 | Coherent operation across CLI, IDE, API, web, or messaging surfaces |

## Matrix
| Harness          | Arch | State | Eval | Orch | Trust | Surf | Total |
| :--------------- | :--: | :---: | :--: | :--: | :---: | :--: | ----: |
| [[claude-code]]  | 4.5  |  5.0  | 5.0  | 3.5  |  4.0  | 4.5  |  89.5 |
| [[codex-cli]]    | 5.0  |  3.5  | 4.0  | 3.5  |  4.5  | 5.0  |  84.0 |
| [[hermes-agent]] | 3.5  |  5.0  | 3.0  | 3.0  |  4.5  | 5.0  |  78.5 |
| [[gas-town]]     | 2.5  |  4.0  | 3.5  | 5.0  |  2.5  | 2.0  |  66.5 |
| [[gas-city]]     | 3.0  |  3.5  | 3.0  | 5.0  |  2.0  | 3.0  |  65.0 |
| [[openclaw]]     | 3.0  |  4.0  | 2.0  | 2.5  |  1.5  | 5.0  |  58.0 |

## Reading the matrix
[[claude-code]] wins the present-tense overall score because the corpus treats it as the strongest on resumable artifacts, evaluator separation, and long-running task recovery. [[codex-cli]] remains the best architectural specimen: if the question is what shape a new harness core should have, Codex is the cleanest answer.

[[hermes-agent]] ranks lower overall only because the current corpus puts less weight on explicit evaluator loops than on persistent memory and multi-surface continuity. If the goal were long-term personal usefulness rather than design purity, Hermes would rise. [[gas-town]] and [[gas-city]] dominate the orchestration column for the obvious industrial reasons, while [[openclaw]] demonstrates that breadth without strong trust boundaries is a poor bargain.

## Design verdict for another-harness
The matrix supports the design thesis already sketched in [[new-harness-design-notes]]:
- borrow core architecture from [[codex-cli]]
- borrow persistence and skill accumulation from [[hermes-agent]]
- borrow evaluator discipline from [[claude-code]]
- borrow explicit work objects and orchestration direction from [[gas-town]] and [[gas-city]]

## Cautions
These scores are not laboratory measurements. They are a disciplined reduction of the current wiki corpus. If the source base becomes more quantitative, the matrix should be recomputed rather than fondly defended.

## Related pages
Read this beside [[harness-quality-comparison]], [[harness-architecture-comparison]], [[evaluation-and-review-loops]], and [[new-harness-design-notes]].
