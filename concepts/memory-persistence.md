---
title: Memory Persistence
created: 2026-04-07
updated: 2026-04-07
type: concept
tags: [memory, context-engineering, error-recovery]
sources: [raw/articles/yegge-welcome-to-gas-town.md, raw/articles/yegge-gas-town-clown-show-to-v1.md, raw/articles/anthropic-effective-harnesses.md, raw/articles/hermes-agent-github.md, raw/articles/newstack-openclaw-vs-hermes.md]
---

# Memory Persistence

## Definition
Memory persistence is the set of mechanisms that let an agent continue coherent work across sessions. The sources here offer at least three distinct models: work-graph memory, handoff-artifact memory, and personal recall memory.

## Work-graph memory
In [[gas-town]] and [[gas-city]], Beads act as durable work objects storing not just tasks but design intent. This is memory as ledger: queryable, structured, and tied to the evolving work graph.

## Handoff-artifact memory
Anthropic's approach is narrower but practical: `feature_list.json`, progress logs, and init scripts give each new session enough structured state to recover. This is less romantic than a grand memory system, but often exactly what keeps the app from being quietly ruined.

## Personal recall memory
[[hermes-agent]] represents a third model: persistent searchable memory plus skill creation from successful procedures. The emphasis is not only on project continuity but on the agent becoming a better long-term collaborator.

## Design tension
Persistent memory is not one thing. A harness must decide whether it primarily needs resumable project state, reusable personal knowledge, or a federated work ledger. Confusing these layers tends to produce baroque systems that remember everything except the one thing required.

## Related pages
This page grounds [[context-engineering]], extends into [[work-management-primitives]], and is a primary comparison dimension in [[harness-architecture-comparison]].
