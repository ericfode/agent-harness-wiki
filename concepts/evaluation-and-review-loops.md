---
title: Evaluation and Review Loops
created: 2026-04-07
updated: 2026-04-10
type: concept
tags: [subagents, code-quality, orchestration]
sources: [raw/articles/openai-harness-engineering.md, raw/articles/openai-introducing-codex-app.md, raw/articles/anthropic-effective-harnesses.md, raw/articles/anthropic-three-agent-harness-infoq.md, raw/articles/anthropic-claude-code-overview.md, raw/articles/yegge-gas-town-emergency-user-manual.md, raw/articles/yegge-vibe-maintainer.md, raw/papers/arxiv-trivedi-2024-appworld.md, raw/papers/arxiv-pan-2024-swe-gym.md, raw/papers/arxiv-chuang-2026-proxy-state-based-evaluation.md]
---

# Evaluation and Review Loops

## Definition
Evaluation and review loops are the mechanisms by which a harness checks whether the worker agent actually achieved the goal instead of merely composing a plausible success story. They can be automated tests, browser checks, separate evaluator agents, or human-in-the-loop PR triage. The important feature is adversarial distance from the original worker.

## Representative patterns
[[codex-cli]] appears in this corpus through OpenAI's self-review and agent-review loop: implement, request review, absorb criticism, repeat, then inspect diffs in a multi-agent supervisor surface. [[claude-code]] pushes the separation further by giving evaluation work to distinct roles with explicit pass/fail criteria and live-system tooling, then extending that into CI and automated review workflows. In the Yegge line, review becomes operational governance: PR sheriffs, maintainers, and merge strategies that keep swarm output from becoming a landfill.

## What strong loops require
- Explicit acceptance criteria, often externalized into durable files or checklists.
- Tool access to reality: browser automation, logs, screenshots, metrics, or local repro commands.
- Structural independence between builder and reviewer, even if both are agents.
- A workflow that routes failure back into the next iteration instead of letting it dissolve into vague "looks good" prose.

## Executable environments
The newer benchmark literature adds a more concrete substrate for review loops: executable environments with state-based grading. [[rl-gyms-and-executable-environments-for-ai-harnesses]] collects the main families, but the practical lesson is already clear. AppWorld, SWE-Gym, OSWorld, and related systems do not merely evaluate final prose; they evaluate world state, test outcomes, or rubric satisfaction after a multi-step interaction trace. That is much closer to the kind of evidence a learning or promotion loop can safely consume.

## Main trade-off
Good review loops cost more in tokens, time, and operator design. They also add coordination overhead. But without them, long-running systems drift toward premature victory, hidden regressions, and PR pileups. This is why evaluation belongs inside [[harness-engineering]] rather than as an afterthought bolted onto release time.

## Related pages
Read with [[harness-engineering]], [[claude-code]], [[codex-cli]], and [[work-management-primitives]]. This concept also explains much of the ranking logic in [[harness-quality-comparison]] and the evaluation column in [[harness-architecture-comparison]]. The gym-style extension of this idea is [[rl-gyms-and-executable-environments-for-ai-harnesses]].
