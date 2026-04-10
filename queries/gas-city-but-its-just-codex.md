---
title: Gas City But It's Just Codex
created: 2026-04-07
updated: 2026-04-10
type: query
tags: [codex-cli, gas-city, orchestration, tool-execution, work-management]
sources: [raw/articles/gas-city-but-its-just-codex-repo-2026-04-09.md, entities/codex-app-server.md, entities/codex-cli.md, entities/gas-city.md, concepts/work-management-primitives.md, queries/new-harness-design-notes.md]
---

# Gas City But It's Just Codex

## Goal
Rebuild the useful control-plane ideas of [[gas-city]] using Codex-native seams rather than transplanting Gas City's runtime stack whole.

## Working thesis
Gas City's strongest idea is not its shell choreography. It is the decision to center durable work objects, controller reconciliation, and observable session state. Codex centers a different primitive: threads, turns, items, and tool execution. The right move is therefore to keep Codex as the execution kernel and rebuild the work/control plane above it.

## Main decisions
- Keep task state outside Codex conversation history.
- Use [[codex-app-server]] as the execution-facing protocol for worker threads and event streaming.
- Prefer MCP-backed typed tools before any `codex-rs` fork.
- Treat plugins and skills as behavior packaging, not as the durable orchestration substrate itself.

## First spike
The first credible prototype is small:

1. A JSON-backed task store.
2. An append-only event log.
3. A tiny MCP tool surface for task listing, claiming, reading, reporting, and worker peeking.

That is enough to test whether Codex can act coherently against external durable work state.

## Main caution
Do not force Gas City's work graph into Codex thread items. Threads should remain execution history. Once work state is confused with transcript state, recovery becomes folklore instead of infrastructure.

## 2026-04-09 update
The repository has now moved well past the original toy spike. It already has a durable `redb` ledger, formula lineage and evolution policy, top-level and in-turn formula mutation or assessment surfaces, and frontier benchmarks that isolate autonomy debt. The broader arXiv pass suggests the current problem actually decomposes into three layers: workflow generation, evaluator-and-promotion plumbing, and a likely future skill layer beside formulas. The immediate bottleneck is still the middle one: benchmark evidence is not yet the routine source of `formula_assess` plus `formula_select` decisions. Read this note now beside [[self-evolving-workflows]] and [[arxiv-self-evolving-workflows-for-codex-control-plane]].

## Related pages
This note extends [[new-harness-design-notes]] with a narrower conclusion about Codex-specific execution seams and depends on [[codex-cli]], [[codex-app-server]], and [[work-management-primitives]]. It should now also be read with [[self-evolving-workflows]] and [[arxiv-self-evolving-workflows-for-codex-control-plane]].
