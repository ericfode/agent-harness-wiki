---
title: Harness Engineering
created: 2026-04-07
updated: 2026-04-07
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
- Design error messages as remediation hints for future agent turns.

## Implication for software teams
Engineering work shifts upward: fewer keystrokes in the hot path, more effort spent on invariant design, evaluation criteria, and legible documentation. This is why [[codex-cli]] and [[claude-code]] matter as much for their surrounding machinery as for their underlying models.

## Related pages
Harness engineering depends on [[context-engineering]], [[memory-persistence]], [[agent-harness-anatomy]], and [[evaluation-and-review-loops]]. It is compared concretely in [[harness-architecture-comparison]].
