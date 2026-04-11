---
title: Serious Alternatives to Hierarchical Agent Orchestration
created: 2026-04-09
updated: 2026-04-11
type: query
tags: [opinion, orchestration, work-management, subagents]
sources: [concepts/non-hierarchical-coordination-patterns.md, concepts/fission-fusion-orchestration.md, concepts/orchestration-topologies.md, queries/new-harness-design-notes.md]
---

# Serious Alternatives to Hierarchical Agent Orchestration

## Question
If "make a manager and some workers" is too crude, what should replace it in an agent harness?

## Short answer
Not one replacement. Most serious alternatives split the problem into separate coordination functions:
- shared visibility of partial work
- dynamic task allocation
- temporary team formation
- narrow agreement on commits or state transitions

Hierarchy bundles all four into one role. That is often exactly the mistake.

## Better defaults
### Shared workspace as the substrate
Use a blackboard or tuple-space style substrate so agents can publish findings, artifacts, and requests without routing everything through a parent session. This reduces serialization pressure and makes late-joining specialists viable. See [[non-hierarchical-coordination-patterns]] and [[memory-persistence]].

### Negotiation for claiming work
Use contract-net or market-style allocation when cost, locality, or capability are changing too quickly for a static planner. Let agents bid for tasks or propose coalitions rather than waiting for a fixed manager to micromanage routing. This fits the concerns in [[work-management-primitives]] better than plain spawn trees do.

### Fission-fusion coalitions for coupled phases
When tasks move between solo work, tight collaboration, and reintegration, make coalitions first-class. Let teams split, merge, and overlap while retaining durable relation memory. The important part is not the dolphin analogy; it is the operating rule extracted in [[fission-fusion-orchestration]].

### Consensus only for narrow commits
Reserve peer consensus or quorum rules for the few places that truly require agreement: merge readiness, shared estimate updates, state promotion, or replicated memory changes. Do not use consensus as the universal scheduler. It is a commit mechanism, not a full production model. This aligns with [[partial-order-trace-semantics]].

## A plausible composite design
The most defensible near-term architecture in this wiki now looks like:
1. Tuple-space or blackboard substrate for artifacts and pending work.
2. Contract-net claiming for initial task assignment and rebalancing.
3. Fission-fusion coalition objects for tasks that require temporary tight coordination.
4. Dedicated evaluator loops outside the production coalitions, as in [[evaluation-and-review-loops]].
5. Quorum or consensus barriers only where state promotion must be shared.

This is closer to a market-plus-blackboard runtime with coalition memory than to a classical org chart. It also fits the broader architecture direction in [[new-harness-design-notes]] better than a larger and larger manager tree does.

## Open design questions
- Which artifacts belong in the shared workspace, and which should remain private to a coalition?
- How should coalition memory decay so past success informs future grouping without creating permanent cliques?
- What should be priced in bidding: elapsed time, token cost, evaluator confidence, or all three?
- Which state transitions deserve quorum semantics, and which only need review?

## Related pages
Read this with [[non-hierarchical-coordination-patterns]], [[fission-fusion-orchestration]], [[orchestration-topologies]], [[work-management-primitives]], [[evaluation-and-review-loops]], [[new-harness-design-notes]], and [[multiplayer-agent-harnesses-and-p2p-networks]].
