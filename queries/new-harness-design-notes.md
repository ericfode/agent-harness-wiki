---
title: New Harness Design Notes
created: 2026-04-07
updated: 2026-04-07
type: query
tags: [opinion, orchestration, memory, code-quality]
sources: [raw/articles/openai-unlocking-codex-harness.md, raw/articles/openai-harness-engineering.md, raw/articles/hermes-agent-github.md, raw/articles/newstack-openclaw-vs-hermes.md, raw/articles/yegge-gas-town-clown-show-to-v1.md, raw/articles/yegge-welcome-to-the-wasteland.md, raw/articles/anthropic-harness-design-long-running-apps.md]
---

# New Harness Design Notes

## Goal
Design a harness that combines three virtues the current landscape tends to separate: Codex's architectural cleanliness, Hermes's durable learning loop, and Gas City's orchestration ambition. The missing fourth ingredient is Anthropic's insistence on evaluator-driven reality checks.

## What to borrow from Codex
- A thin, explicit protocol layer between harness core and user surfaces.
- Durable session containers with named primitives rather than a monolithic transcript blob.
- Repo-legibility as a first-class engineering problem, not a documentation afterthought.

## What to borrow from Hermes
- Searchable persistent memory and deliberate user modeling.
- Skill extraction from successful procedures.
- Profile isolation so multiple workflows can coexist without memory contamination.

## What to borrow from Anthropic
- Fresh-session handoffs instead of pretending the context window is infinite.
- Separate evaluator roles with live-system tooling.
- Explicit sprint contracts and artifact-driven recovery.

## What to borrow from Gas City
- Work as a graph of durable primitives, not only as prose TODOs.
- Modular orchestration parts rather than one fixed swarm topology.
- Federation as a long-term possibility once local rigor exists.

## Provisional architecture
1. Core runtime: App-Server-like protocol with durable threads and tool events.
2. Memory plane: searchable personal memory plus project-scoped handoff artifacts.
3. Work plane: bead-like task graph with explicit state transitions.
4. Evaluation plane: dedicated reviewer agents with browser/log/metric access.
5. Surface plane: CLI first, then IDE and messaging clients against the same core.

## Main caution
Every extra layer must earn its existence. The landscape is full of beautiful abstractions that mostly manufacture new failure modes. A harness should become more modular only when the previous monolith has already become legible. Otherwise one is merely arranging confusions into neighborhoods.

## Related pages
This synthesis depends on [[harness-architecture-comparison]], [[harness-quality-comparison]], [[memory-persistence]], and [[work-management-primitives]].
