---
title: Non-Hierarchical Coordination Patterns
created: 2026-04-09
updated: 2026-04-09
type: concept
tags: [orchestration, work-management, subagents, concurrency]
sources: [raw/papers/smith-1980-contract-net-protocol.md, raw/papers/gelernter-1985-generative-communication-in-linda.md, raw/papers/mcmanus-1991-design-and-analysis-tools-for-concurrent-blackboard-systems.md, raw/papers/olfati-saber-fax-murray-2007-consensus-and-cooperation-in-networked-multi-agent-systems.md, raw/papers/shehory-kraus-1998-methods-for-task-allocation-via-agent-coalition-formation.md, raw/papers/dias-zlot-kalra-stentz-2006-market-based-multirobot-coordination.md, raw/papers/brambilla-ferrante-birattari-dorigo-2013-swarm-robotics-review.md, raw/papers/arxiv-edixhoven-2022-branching-pomsets-for-choreographies.md, raw/papers/arxiv-salemi-2025-llm-blackboard-data-discovery.md, raw/papers/arxiv-nakamura-2025-terrarium-blackboard-multi-agent-safety.md, raw/papers/arxiv-pugachev-2025-codecrdt-observation-driven-coordination.md, raw/papers/arxiv-li-2025-lacp-agent-communication-protocol.md, raw/papers/arxiv-ehtesham-2025-survey-agent-interoperability-protocols.md, raw/papers/arxiv-ben-khaled-2026-g2cp-graph-grounded-communication-protocol.md, raw/papers/arxiv-zou-2025-blocka2a-secure-verifiable-interoperability.md, raw/papers/arxiv-duetting-2023-mechanism-design-large-language-models.md, raw/papers/arxiv-zhao-2025-llm-auction-generative-auction.md, raw/papers/arxiv-wang-2024-battleagentbench.md, raw/papers/arxiv-sun-2025-collab-overcooked.md]
---

# Non-Hierarchical Coordination Patterns

## Definition
Non-hierarchical coordination patterns are ways to allocate work, share state, and reach decisions without forcing every dependency through a fixed manager tree. The point is not to abolish leadership. The point is to stop pretending that routing, authority, memory, and scheduling are always the same problem.

## Pattern map
| Pattern | Main coordination object | Where it beats a hierarchy | Main failure mode |
| --- | --- | --- | --- |
| Blackboard | Shared hypothesis space | When solution order is uncertain and specialists should contribute opportunistically | Contention and controller bottlenecks |
| Tuple space | Persistent associative tuples | When producers and consumers should be decoupled in time and identity | Semantic drift and garbage accumulation |
| Contract net / market | Task announcements, bids, awards | When cost and capability are local and dynamic | Bad utility functions create bad allocations |
| Consensus / gossip | Neighbor-to-neighbor state updates | When agreement matters more than command | Slow or fragile under high contention |
| Coalition formation | Temporary team objects | When tasks need bundles of capabilities, not lone workers | Group churn without memory |
| Swarm / stigmergy | Local rules plus environmental traces | When agents are numerous, simple, and redundant | Weak at rich tightly coupled tasks |
| Choreography | Peer protocol with partial-order constraints | When the allowed interactions matter more than central routing | Hard debugging and observability |

## Shared-workspace patterns
Blackboard and tuple-space systems both start from the same heresy: coordination need not be a conversation between named roles. In the blackboard model, specialized knowledge sources read a shared partial solution and add results opportunistically. In Linda, agents publish tuples into a shared space and other agents consume them later without direct addressing. Both patterns beat a manager tree when the main problem is not deciding who is in charge, but making partial findings visible fast enough that the right next step becomes obvious.

The difference matters. Blackboard systems usually assume richer shared semantics and more explicit interpretation of a common problem state. Tuple spaces are more anonymous and more decoupled. Blackboard is closer to collaborative reasoning; tuple space is closer to asynchronous work exchange. Both connect directly to [[work-management-primitives]] and [[memory-persistence]] because their real substrate is durable shared state, not interpersonal authority.

The recent LLM papers make this pattern feel current again. Salemi et al. show that a blackboard design can beat stronger centralized baselines when the coordinator cannot know every subordinate agent's competence in advance. Terrarium shows the same substrate is useful for safety and attack analysis because collaboration, compromise, and leakage all become more inspectable when they pass through a shared environment. CodeCRDT pushes the idea further: the shared object can be a convergent replicated data type rather than a plain bulletin board, which moves part of coordination into deterministic merge semantics.

## Negotiated allocation
Contract-net and market approaches move coordination into negotiation. A node with work announces it, candidate workers bid, and assignment emerges from mutual selection or clearing rules. This is better than hierarchy when no central planner can keep up with changing capability, cost, locality, or load.

The core requirement is brutally simple: the bids must mean something. If the cost model is fake, the market is fake. That is why these patterns pair naturally with [[evaluation-and-review-loops]] and with the stronger semantics in [[formal-methods-for-agent-harnesses]]: a negotiation layer only helps if capability, effort, and acceptance are legible enough to price.

The LLM-era arXiv corpus is still relatively thin here. Mechanism-design papers now show that LLM-mediated generation can be governed by explicit auction rules with analyzable incentive properties, and LLM-Auction shows the allocation and generation loop can even be learned jointly. But harness work still rarely uses these ideas for task claiming, repricing, or coalition formation. The mathematical path exists before the engineering habit does.

## Protocolized coordination
Recent agent papers also sharpen a distinction that older coordination work often left implicit: messages are not yet protocols. LACP and the interoperability survey both argue that tool access, peer delegation, and network discovery need separate standardized surfaces rather than one vague notion of "agent communication." G2CP goes further by replacing free-text inter-agent messaging with graph operations over a shared knowledge graph, while BlockA2A adds identity, audit, and revocation as native interoperability concerns.

This matters because semantic drift is itself a coordination failure. If every handoff is untyped prose, the system is always one paraphrase away from corruption. Protocolized coordination is therefore not only about interop with outside systems. It is a way to make multi-agent collaboration more auditable and less dependent on lucky wording. Read this beside [[partial-order-trace-semantics]] and [[safety-and-permissions]].

## Peer agreement
Consensus algorithms and gossip protocols are useful when the system needs agreement on a value, estimate, or commit barrier but should not trust one permanent decider. They are not a full orchestration replacement. They are a specific answer to a specific problem: how peers converge on shared state through local interaction.

This makes consensus a good fit for narrow control decisions, merge readiness, replicated memory, or distributed evaluator verdicts. It is a poor fit for rich task decomposition. In harness terms, consensus belongs beside [[partial-order-trace-semantics]], not above it: first decide what really requires agreement, then pay the price only there.

## Coalitions and swarms
Coalition formation handles tasks that require temporary group structure. Swarm and stigmergic systems handle large populations where redundancy and local rules are the point. These are often confused, but they solve different problems. Coalitions are about composing the right temporary team. Swarms are about letting many simple actors produce global behavior without much individual specialization.

The more interesting frontier for agent harnesses is to combine them selectively. A runtime might use market-style bidding to form a coalition, a tuple space to exchange artifacts, and a quorum rule for irreversible commits. That mixed architecture is usually more defensible than declaring one universal topology. See [[fission-fusion-orchestration]] and [[orchestration-topologies]].

The benchmark picture reinforces this. BattleAgentBench and Collab-Overcooked both show that models can look locally competent while still failing at sustained collaboration, adaptation, and competition. That is exactly the failure profile you would expect if coordination structure is still too weak, too implicit, or too centralized.

## Selection rule
Choose the lightest pattern that matches the actual uncertainty:
- If the next useful action depends on accumulating partial evidence, use a shared workspace.
- If allocation depends on local cost and changing availability, use negotiation.
- If the system only needs agreement on a narrow state transition, use consensus there and nowhere else.
- If the required unit of work is a temporary team, make coalitions explicit.
- If the task tolerates many simple local actors, use stigmergic or swarm rules.
- If semantic drift between agents is the bottleneck, use typed or graph-grounded protocols before adding more roles.

## Related pages
Read this with [[non-hierarchical-agent-orchestration]], [[arxiv-under-explored-coordination-strategies]], [[orchestration-topologies]], [[work-management-primitives]], [[memory-persistence]], [[evaluation-and-review-loops]], [[partial-order-trace-semantics]], and [[fission-fusion-orchestration]].
