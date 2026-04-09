---
title: Memory Persistence
created: 2026-04-07
updated: 2026-04-09
type: concept
tags: [memory, context-engineering, error-recovery]
sources: [raw/articles/yegge-welcome-to-gas-town.md, raw/articles/yegge-gas-town-clown-show-to-v1.md, raw/articles/anthropic-effective-harnesses.md, raw/articles/anthropic-claude-code-memory.md, raw/articles/hermes-agent-github.md, raw/articles/hermes-agent-memory-docs.md, raw/articles/openclaw-agent-runtime-docs.md, raw/articles/newstack-openclaw-vs-hermes.md, raw/papers/arxiv-zhou-2026-memento-skills.md, raw/articles/memento-skills-github.md]
---

# Memory Persistence

## Definition
Memory persistence is the set of mechanisms that let an agent continue coherent work across sessions. The sources here offer at least four distinct models: work-graph memory, handoff-artifact memory, personal recall memory, and workspace-injected memory.

## Work-graph memory
In [[gas-town]] and [[gas-city]], Beads act as durable work objects storing not just tasks but design intent. This is memory as ledger: queryable, structured, and tied to the evolving work graph.

## Handoff-artifact memory
Anthropic's approach is narrower but practical: `feature_list.json`, progress logs, init scripts, and now scoped `CLAUDE.md` files plus auto memory give each new session enough structured state to recover. This is less romantic than a grand memory system, but often exactly what keeps the app from being quietly ruined.

## Personal recall memory
[[hermes-agent]] represents a third model: `MEMORY.md`, `USER.md`, persistent searchable session recall, and skill creation from successful procedures. The emphasis is not only on project continuity but on the agent becoming a better long-term collaborator.

## Skill-library memory
[[memento-skills]] makes a sharper claim than ordinary recall: the evolving skill library is itself the memory substrate. Skills live as structured markdown packages with scripts and metadata, retrieval decides which prior experience becomes active, and reflection writes improvements back into the library instead of into model weights. That turns memory into a deployment-time learning surface and blurs the boundary between persistence and [[work-management-primitives]].

## Workspace-injected memory
[[openclaw]] adds another variant: bootstrap files such as `AGENTS.md`, `SOUL.md`, `TOOLS.md`, and `USER.md` are injected into the runtime context from the workspace itself. This is memory as working environment rather than only as logs or learned summaries.

## Design tension
Persistent memory is not one thing. A harness must decide whether it primarily needs resumable project state, reusable personal knowledge, workspace bootstrap context, or a federated work ledger. Confusing these layers tends to produce baroque systems that remember everything except the one thing required. The neighboring problem is [[instruction-layering]]: some durable files are memory, some are policy, and some are both depending on how the harness reads them. The more formal nearby question is epistemic: what does each memory surface actually justify? That is where [[probabilistic-epistemic-updates]] becomes relevant.

## Related pages
This page grounds [[context-engineering]], [[instruction-layering]], extends into [[work-management-primitives]], and is a primary comparison dimension in [[harness-architecture-comparison]].
