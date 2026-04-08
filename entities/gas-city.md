---
title: Gas City
created: 2026-04-07
updated: 2026-04-07
type: entity
tags: [gas-city, orchestration, work-management]
sources: [raw/articles/yegge-gas-town-clown-show-to-v1.md, raw/articles/yegge-welcome-to-the-wasteland.md, raw/articles/yegge-vibe-maintainer.md, raw/articles/yegge-birthday-blog.md]
---

# Gas City

## Overview
Gas City is the modular successor to [[gas-town]]. Where Gas Town is an opinionated orchestrator, Gas City aims to expose the constituent parts: identity, roles, messaging, cost tracking, model dispatch, molecules, seances, and federated work exchange. It is the builder kit version of the same instinct.

## Modular primitives
Yegge's description repeatedly frames Gas City as LEGO-like: instead of one factory topology, provide parts from which many topologies can be assembled. This matters because it moves the harness discussion from "which worker is best" to "which coordination graph is native to the problem." See [[agent-harness-anatomy]] and [[new-harness-design-notes]].

## Wasteland federation
The Wasteland concept extends the local swarm into a federated trust network with wanted boards, validators, rigs, reputation stamps, and Dolt-backed data exchange. This is a more ambitious notion of memory and collaboration than ordinary repo-local handoff files. It is also one that raises correspondingly ambitious questions about trust, schema migration, and governance.

## Strengths
- Clear path from monolithic orchestrator to modular platform.
- Strong integration with Beads and Dolt-backed federation.
- Richer support for custom roles, reputational signals, and inter-town cooperation.

## Weaknesses and limits
The material is explicitly alpha-stage and expects migrations. Gas City is conceptually compelling, but a concept can still be half scaffolding and half prophecy. One should not confuse architectural promise with complete implementation.

## Relationships
Gas City is the most forward-looking orchestration system in this wiki's source set. It informs [[work-management-primitives]], stretches [[memory-persistence]] into federated territory, and heavily influences [[new-harness-design-notes]].
