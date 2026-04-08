---
title: Agent Harness Anatomy
created: 2026-04-07
updated: 2026-04-07
type: concept
tags: [orchestration, memory, tool-execution, subagents, survey]
sources: [raw/articles/openai-unlocking-codex-harness.md, raw/articles/openai-harness-engineering.md, raw/articles/anthropic-harness-design-long-running-apps.md, raw/articles/yegge-welcome-to-gas-town.md]
---

# Agent Harness Anatomy

## Definition
An agent harness is the infrastructure around the model: state containers, tool execution, memory, review loops, work representation, and operator surfaces. The model writes sentences; the harness decides whether those sentences become durable work or expensive compost.

## Common components
Across the sources in this wiki, a mature harness usually contains at least these parts:
1. Session containers such as threads, turns, or resumable runs.
2. Prompt assembly and context-loading rules.
3. Tool execution, approval, and [[safety-and-permissions]] machinery.
4. Durable memory or state artifacts.
5. Work representations such as beads, feature lists, or plans.
6. Validation and evaluator loops.
7. Handoff or resume mechanisms.
8. Human control surfaces and client integrations.
9. Observability, logging, and debugging hooks.
10. Coordination roles or subagent topologies.

## Representative implementations
[[codex-cli]] emphasizes clean protocol boundaries and client separation.
[[claude-code]] emphasizes handoff artifacts, evaluators, and context resets.
[[hermes-agent]] emphasizes persistence, skill accumulation, and multi-surface continuity.
[[gas-town]] and [[gas-city]] emphasize explicit work graphs and multi-agent orchestration.

## Why anatomy matters
Without structural decomposition, discussions about agents collapse into model talk. The sources here suggest the opposite lesson: many practical wins come from changing the harness rather than changing the model. That is the central claim of [[harness-engineering]].

## Related pages
Use this page as the map before reading [[harness-architecture-comparison]], [[context-engineering]], [[safety-and-permissions]], or [[work-management-primitives]].
