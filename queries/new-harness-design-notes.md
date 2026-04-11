---
title: New Harness Design Notes
created: 2026-04-07
updated: 2026-04-11
type: query
tags: [opinion, orchestration, memory, code-quality]
sources: [raw/articles/openai-unlocking-codex-harness.md, raw/articles/openai-harness-engineering.md, raw/articles/openai-codex-chatgpt-plan.md, raw/articles/hermes-agent-github.md, raw/articles/newstack-openclaw-vs-hermes.md, raw/articles/yegge-gas-town-clown-show-to-v1.md, raw/articles/yegge-welcome-to-the-wasteland.md, raw/articles/anthropic-harness-design-long-running-apps.md, raw/articles/anthropic-claude-code-agent-teams.md, raw/articles/anthropic-claude-code-subagents.md, concepts/non-hierarchical-coordination-patterns.md, concepts/fission-fusion-orchestration.md, concepts/neural-native-programming.md]
---

# New Harness Design Notes

## Goal
Design a harness that combines three virtues the current landscape tends to separate: Codex's architectural cleanliness, Hermes's durable learning loop, and Gas City's orchestration ambition. The missing fourth ingredient is Anthropic's insistence on evaluator-driven reality checks. The scored argument for that blend now lives in [[harness-decision-matrix]].

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

## What not to borrow from anyone
- The reflex to turn every coordination problem into one manager session with a stack of subordinates.
- One universal control shape for routing, memory, task allocation, and review.
- Implicit coalition logic hidden in chat transcripts instead of explicit work objects.

## Provisional architecture
1. Core runtime: App-Server-like protocol with durable threads and tool events.
2. Formalization plane: a typed gate that routes problems into the right formal space, as argued in [[formal-cognition-loop]].
3. Memory plane: searchable personal memory plus project-scoped handoff artifacts.
4. Work plane: bead-like task graph with explicit state transitions, plus a mix of shared-workspace, bidding, and coalition patterns from [[non-hierarchical-coordination-patterns]] rather than one default hierarchy.
5. Evaluation plane: dedicated reviewer agents with browser/log/metric access.
6. Surface plane: CLI as the exact textual kernel, then IDE and other clients against the same core, with non-linear control surfaces layered on top where they earn their keep; see [[non-linear-interface-options-for-next-harness]].
7. Control-plane semantics: causal events, consistent cuts, view epochs, session guarantees, and bounded delegated rights; see [[legacy-distributed-systems-ideas-for-moldable-operations-studio]] and [[moldable-operations-studio-architecture-spec]].
8. Federated collaboration plane: local-first harness nodes, replicated shared spaces, typed peer delegation, and multiplayer operational surfaces rather than one giant manager session; see [[multiplayer-agent-harnesses-and-p2p-networks]].
9. Experimental model-facing IR plane: keep an explicit place for typed latent-program interfaces that might eventually sit below token text without collapsing into opaque activation sludge; see [[neural-native-programming]] and [[neural-native-programming-via-direct-interfaces-to-transformer-internal-layers]].

For work that repeatedly alternates between scouting, tight collaboration, and reaggregation, the right local pattern may be [[fission-fusion-orchestration]] rather than a permanent manager-worker tree.

## Main caution
Every extra layer must earn its existence. The landscape is full of beautiful abstractions that mostly manufacture new failure modes. A harness should become more modular only when the previous monolith has already become legible. Otherwise one is merely arranging confusions into neighborhoods.

## Related pages
This synthesis depends on [[formal-cognition-loop]], [[theorem-proving-as-cognitive-kernel]], [[harness-architecture-comparison]], [[harness-quality-comparison]], [[orchestration-topologies]], [[memory-persistence]], [[work-management-primitives]], [[non-linear-interface-options-for-next-harness]], [[legacy-distributed-systems-ideas-for-moldable-operations-studio]], [[moldable-operations-studio-architecture-spec]], and [[multiplayer-agent-harnesses-and-p2p-networks]].
