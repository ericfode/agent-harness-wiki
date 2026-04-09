---
title: Harness Engineering
created: 2026-04-07
updated: 2026-04-09
type: concept
tags: [orchestration, context-engineering, tool-execution, survey]
sources: [raw/articles/openai-harness-engineering.md, raw/articles/anthropic-effective-harnesses.md, raw/articles/anthropic-harness-design-long-running-apps.md]
---

# Harness Engineering

## Definition
Harness engineering is the discipline of making agents effective by shaping the environment around them: repo knowledge, plans, tool affordances, evaluation loops, permissions, and remediation paths. It is not prompt tinkering with better manners; it is systems design.

## Core idea
OpenAI's framing is especially blunt: when the agent fails, ask what capability is missing and make it legible and enforceable. Anthropic's work makes the same point from another angle: if the agent forgets, externalize state; if it flatters itself, assign it an evaluator; if it overreaches, force incremental contracts.

## Practical ingredients
- Keep the repository as the system of record via `AGENTS.md`, plans, and references.
- Encode architecture rules as tests or linters the agent can actually trip.
- Prefer structured handoff artifacts over heroic memory.
- Make validation observable through browser automation, logs, metrics, or screenshots.
- Make branches, checkpoints, and runtime evidence navigable in the operator surface instead of burying them in transcript prose; see [[non-linear-interface-options-for-next-harness]].
- Design error messages as remediation hints for future agent turns.

## Formal turn
The next turn of the discipline is not simply more scaffolding but more checkable semantics. The current arXiv pass suggests two especially relevant directions: [[formal-methods-for-agent-harnesses]] for intent surfaces and specification ladders, and [[probabilistic-epistemic-updates]] for stating what the harness and the agent are actually justified in believing at each step.

## Implication for software teams
Engineering work shifts upward: fewer keystrokes in the hot path, more effort spent on invariant design, evaluation criteria, and legible documentation. This is why [[codex-cli]] and [[claude-code]] matter as much for their surrounding machinery as for their underlying models.

## Related pages
Harness engineering depends on [[context-engineering]], [[memory-persistence]], [[agent-harness-anatomy]], and [[evaluation-and-review-loops]]. It is compared concretely in [[harness-architecture-comparison]]. The current surface-design extension is [[non-linear-interface-options-for-next-harness]].
