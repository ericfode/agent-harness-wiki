---
title: "ArXiv Round Three: Under-Explored Coordination Strategies for AI Models"
created: 2026-04-09
updated: 2026-04-09
type: query
tags: [survey, comparison, orchestration, work-management]
sources: [raw/papers/arxiv-salemi-2025-llm-blackboard-data-discovery.md, raw/papers/arxiv-nakamura-2025-terrarium-blackboard-multi-agent-safety.md, raw/papers/arxiv-pugachev-2025-codecrdt-observation-driven-coordination.md, raw/papers/arxiv-duetting-2023-mechanism-design-large-language-models.md, raw/papers/arxiv-zhao-2025-llm-auction-generative-auction.md, raw/papers/arxiv-li-2025-lacp-agent-communication-protocol.md, raw/papers/arxiv-ehtesham-2025-survey-agent-interoperability-protocols.md, raw/papers/arxiv-ben-khaled-2026-g2cp-graph-grounded-communication-protocol.md, raw/papers/arxiv-zou-2025-blocka2a-secure-verifiable-interoperability.md, raw/papers/arxiv-miculicich-2025-veriguard-verified-code-generation.md, raw/papers/arxiv-ye-2025-x-mas-heterogeneous-llms.md, raw/papers/arxiv-yu-2025-dyntaskmas-dynamic-task-graph.md, raw/papers/arxiv-wang-2024-battleagentbench.md, raw/papers/arxiv-sun-2025-collab-overcooked.md]
---

# ArXiv Round Three: Under-Explored Coordination Strategies for AI Models

## Goal
Answer the narrower question directly: which coordination strategies still look under-explored on arXiv once "manager and workers" and generic debate loops are set aside?

## Short answer
The thinnest serious clusters in this pass are:
- blackboard and other shared-workspace coordination
- convergent shared-state coordination such as CRDT-backed observation
- typed or graph-grounded communication protocols
- secure and verifiable interoperability layers
- heterogeneous model ecologies instead of one-model role cloning
- asynchronous task-graph orchestration
- mechanism-design style allocation, though that thread is still more adjacent than native to harness research

## Strategy clusters
| Cluster | Representative papers | Why it still looks thin | Harness implication |
| --- | --- | --- | --- |
| Blackboard / shared workspace | Salemi et al., Terrarium | The pattern is live again, but still small compared with planner-worker systems | Use shared artifacts as the substrate and let agents volunteer based on local capability |
| Convergent shared state | CodeCRDT | Very little work treats deterministic merge semantics as the coordination primitive | Put conflict handling in the data structure, not only in chat repair loops |
| Typed communication protocols | LACP, interoperability survey, G2CP | Protocol standardization is still in an early, partly position-paper phase | Replace free-text chatter with typed, auditable message surfaces |
| Secure interoperability | BlockA2A, VeriGuard | Trust, revocation, and runtime guarantees are still not normal design defaults | Treat identity, audit, and action validation as core coordination boundaries |
| Heterogeneous model teams | X-MAS | Many MAS papers still assume every role runs the same model | Route by capability and cost, not only by role label |
| Asynchronous task graphs | DynTaskMAS | Dynamic dependency management is less explored than role prompting | Make the task graph explicit and schedule against it directly |
| Mechanism design | Mechanism Design for Large Language Models, LLM-Auction | The mathematics exists, but harness work rarely uses it for task claiming | Explore bidding, prices, and externalities for dynamic work allocation |

## What feels most important
The strongest shift in this corpus is away from "who talks next?" and toward "what shared object or protocol makes coordination legible?" Blackboard systems, CRDT systems, graph-grounded communication, and verified interop all move coordination out of informal chat and into structured state transitions. That is much closer to [[non-hierarchical-coordination-patterns]] and [[work-management-primitives]] than to ordinary roleplay prompting.

The second shift is that coordination is no longer only about role prompts. [[orchestration-topologies]] now has good reason to distinguish topology from substrate, because X-MAS and DynTaskMAS show that model assignment and dependency scheduling can matter as much as the visible team chart. A manager tree with heterogeneous models and an async task graph is a different machine from a manager tree with cloned workers, even if the surface diagram looks similar.

The third shift is defensive. BlockA2A, VeriGuard, and Terrarium all imply that coordination cannot be separated cleanly from trust boundaries. Once multiple agents share data, delegate work, or cross organizational boundaries, authentication, revocation, audit, and verified action surfaces stop being optional polish. They become part of the runtime's actual semantics, which connects this thread to [[formal-methods-for-agent-harnesses]] and [[safety-and-permissions]].

## Best bets for this repo
1. Treat shared workspaces as the default substrate for non-trivial collaboration.
2. Push toward typed or graph-grounded message formats before adding more roles.
3. Add a verifier or monitor at promotion boundaries rather than only at the end.
4. Make heterogeneous model selection and async task graphs first-class work objects.
5. Read the benchmark papers as evidence that collaboration remains the bottleneck, not as proof that today's simple orchestration patterns are already adequate.

## Related pages
Read this with [[non-hierarchical-coordination-patterns]], [[orchestration-topologies]], [[formal-methods-for-agent-harnesses]], [[work-management-primitives]], [[safety-and-permissions]], and [[new-harness-design-notes]].
