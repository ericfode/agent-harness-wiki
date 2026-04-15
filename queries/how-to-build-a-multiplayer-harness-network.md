---
title: How to Build a Multiplayer Harness Network
created: 2026-04-10
updated: 2026-04-15
type: query
tags: [survey, orchestration, semantics, work-management, memory]
sources: [queries/multiplayer-agent-harnesses-and-p2p-networks.md, queries/moldable-operations-studio-architecture-spec.md, queries/moldable-operations-studio-schema-pass.md, queries/legacy-distributed-systems-ideas-for-moldable-operations-studio.md, queries/grounding-moldable-operations-studio-ideas-in-real-research.md, concepts/non-hierarchical-coordination-patterns.md, concepts/partial-order-trace-semantics.md, raw/articles/google-agent2agent-protocol.md, raw/papers/arxiv-ehtesham-2025-survey-agent-interoperability-protocols.md, raw/papers/arxiv-zou-2025-blocka2a-secure-verifiable-interoperability.md, raw/papers/merkle-crdts.md, raw/articles/local-first-software.md, raw/papers/session-guarantees-weakly-consistent-replicated-data.md, raw/papers/escrow-transactional-method.md]
---

# How to Build a Multiplayer Harness Network

## Question
If the long-term goal is a world where many different harnesses can jack into the same collaboration fabric, do you build protocol first?

## Short answer
Not exactly. Build seam-first, ontology-first, and reference-node-first.

More bluntly:
- do not start by standardizing a giant universal wire protocol
- do define the durable object model and event semantics very early
- do build one real reference node plus one real foreign-harness adapter
- only then freeze the interop protocol that survives contact with both

The mistake on one side is code-first tribalism: every harness invents its own private state model and later discovers that interop is translation hell. The mistake on the other side is standards-first theatre: a grand protocol gets specified before anyone has proved what the stable objects even are. Both are common. Neither is charming.

## The right ordering

### 1. Semantic core first
Before protocol work, decide what is actually being shared across harnesses.

That core should be the minimum typed collaboration substrate already implied by [[moldable-operations-studio-schema-pass]]:
- `work_item`
- `branch`
- `artifact`
- `approval`
- `trace`
- `coalition`
- `authority_budget`
- `view_definition`
- `session_token`

And the minimum event semantics:
- causal parents / frontier
- tentative vs committed lifecycle
- suspicion states
- session guarantees across surfaces
- a small linearizable subset for approvals, promotion, and revocation

If those objects are unstable, the protocol is premature.

### 2. Reference node second
Build one local harness node that natively owns the model.

This node should provide:
- append-only event log
- durable object store for the collaboration objects
- local artifact storage with content hashes
- query APIs for graph, queue, and evidence views
- local policy engine for approvals and budgets
- session tokens and frontiers for consistent replay/read state

This is the system that teaches you what the protocol needs to say. Without it, protocol design is speculative fiction wearing JSON.

### 3. Adapter boundary third
Before broad federation, prove that a different harness can connect through an adapter.

This is the key move if you want every harness to jack in. Define a narrow adapter contract:
- ingest task / artifact / approval objects from the shared space
- emit local events as normalized control-plane events
- expose a capability card describing what the harness can actually do
- respect authority budgets and revocations
- report frontier / staleness / replay boundaries honestly

That gives you three integration modes:

1. Native node
- harness adopts the shared object model directly

2. Sidecar bridge
- harness keeps its internal model, but a sidecar translates local state to the shared substrate

3. Gateway wrapper
- harness is too opaque or too weak for real integration, so a wrapper only exposes limited tasks/artifacts around it

The sidecar bridge is the most important near-term mode because it lets existing harnesses join without rewriting themselves into sainthood.

### 4. Protocol fourth
Only after the reference node and one bridge exist should you freeze the peer protocol.

At that point the protocol should be small and layered:

#### Layer A: node capability and identity
- node id / self-certifying handle
- supported schema versions
- supported object kinds
- supported event kinds
- policy / approval capabilities
- transport endpoints

#### Layer B: peer task and artifact exchange
- announce capability
- propose work
- claim / decline / delegate work
- transfer artifact refs or content-addressed blobs
- request / grant / reject approvals
- consume / revoke budgets
- publish trace and checkpoint refs

#### Layer C: sync and replication
- frontier exchange
- object/event fetch by id or range
- content-addressed blob retrieval
- anti-entropy / reconciliation
- optional subscription streams

#### Layer D: discovery
- directory, federation registry, or DHT-style lookup later

This matches the separation already visible in [[arxiv-ehtesham-2025-survey-agent-interoperability-protocols]]: tool access, peer delegation, and open-network discovery should not be collapsed into one shapeless "agent protocol."

## So: protocol first or not?
Use this formulation instead:

- protocol boundary early
- protocol standard late

You want an explicit boundary from day one so local hacks do not metastasize into private metaphysics.
But you want the wire contract to harden only after a real node and a real adapter have forced the semantics to become honest.

## What to implement in what order

## Phase 0: choose the reference host
Pick one harness or repo as the reference node host.

Criteria:
- you control it
- it already has durable state or can tolerate a sidecar
- it already has at least one CLI / automation surface
- it can emit real events from nontrivial work

Do not begin with the hardest possible foreign harness. Start where you can make the ontology real.

## Phase 1: local control-plane sidecar
Build a local sidecar that sits beside one harness and materializes the shared substrate.

Minimum outputs:
- event log
- object store
- artifact store
- query surfaces for queue / graph / evidence

Acceptance test:
- one human and one agent can complete a task while all important state is recoverable from the sidecar without rereading the transcript

## Phase 2: replicated shared space between two nodes
Now make two sidecars replicate one workspace.

Do not start with public discovery. Start with explicit peering.

Minimum replicated objects:
- work items
- artifacts
- approvals
- traces

Acceptance test:
- two humans on two machines can see the same task move through claim, work, review, and completion without using one central database as the only truth store

## Phase 3: first foreign-harness bridge
Add one adapter for a different harness family.

This is where you learn what "jack in" really means.

You will probably discover that many harnesses can expose only a subset, which is fine. Treat partial participation as normal:
- some can consume tasks but not expose rich traces
- some can emit artifacts but not honor budgets
- some can expose tool events but not coalition structure

That is why the capability card matters.

Acceptance test:
- the foreign harness can receive a task, produce artifacts, and return trace/progress state through the shared substrate without pretending it has native support for everything

## Phase 4: approvals, budgets, and revocation
Before broad federation, get trust semantics right.

Implement:
- approval objects with explicit state
- authority budgets with bounded rights
- revocation events
- membership / session epochs

Acceptance test:
- an agent can act autonomously inside a limited budget, then lose that budget immediately and observably when revoked

## Phase 5: multiplayer human surfaces
Only now build the serious UI layer.

Required first surfaces:
- queue / inbox
- work graph
- evidence / trace timeline
- shared artifact pane
- presence / focus / follow mechanics

This is where [[visual-studio-live-share]], [[jupyterlab-real-time-collaboration]], [[klokmose-et-al-2015-webstrates|webstrates]], and [[yang-wigdor-2014-panelrama|panelrama]] stop being inspiration and start becoming requirements.

Acceptance test:
- two humans and multiple agents can coordinate around the same work objects without relying on one scrolling transcript as the only operational surface

## Phase 6: broader federation and discovery
Only after the above should you add:
- federation registries
- DHT-like peer discovery
- public or cross-org routing
- more general peer search / matchmaking

Discovery is late because it multiplies ambiguity, abuse, and debugging pain. There is no prize for discovering peers you cannot meaningfully coordinate with.

## What "every harness can jack in" should mean in practice
It should not mean every harness must fully adopt your internal runtime.
It should mean every harness can implement some stable participation contract.

A reasonable minimum contract is:
- identity: who are you?
- capabilities: what can you consume / emit / honor?
- tasks: what work objects can you accept?
- artifacts: what outputs can you publish?
- traces: what runtime evidence can you expose?
- approvals: what decisions can you request or satisfy?
- budgets: what bounded autonomy can you operate under?
- sync: how do you exchange frontier and object state?

That is enough for a meaningful federation. It is also small enough that an adapter can plausibly be written.

## Suggested technical stance

### Local-first internally
Follow [[local-first-software]] as the product principle.
Each node should stay useful offline and own its local state.

### CRDT/Merkle where concurrency is normal
Use convergent replicated state for shared notes, artifact metadata, task state, and other collaborative objects where concurrent edits are expected. See [[merkle-crdts]].

### Stronger semantics only for narrow control facts
Approvals, budget grants, revocations, promotions, and checkpoint finalization should use stronger coordination semantics, as in [[moldable-operations-studio-architecture-spec]].

### Capability security from the beginning
Do not bolt safety on later. [[escrow-transactional-method]] and [[arxiv-zou-2025-blocka2a-secure-verifiable-interoperability]] are the right warning here: bounded rights, audit, and revocation are core protocol semantics, not optional enterprise garnish.

## Prototype shape I would actually build
If forced to choose a practical first implementation, I would build this:

1. A reference sidecar beside one harness
- local SQLite/Postgres or embedded log/object store
- content-addressed artifact storage
- HTTP/WebSocket or JSON-RPC API for local clients

2. A minimal replicated workspace
- two trusted peers
- explicit peering configuration
- frontier exchange plus event/object sync

3. One foreign harness bridge
- capability card
- task/artifact/traces adapter
- budget + approval hooks where possible

4. One multiplayer app surface
- queue
- graph
- evidence pane
- shared artifact inspector

Notably absent:
- giant public mesh
- universal discovery
- speculative blockchain pageantry
- one protocol to rule everything

## Bottom line
Do not build protocol first in the sense of freezing a universal standard before you have a real node.
Do build protocol first in the sense of declaring an explicit adapter boundary before implementation sprawls.

The practical order is:
1. ontology
2. reference node
3. one bridge
4. harden protocol
5. trust/budget semantics
6. multiplayer surfaces
7. wider federation

That is the path most likely to produce something other harnesses can actually jack into, rather than a noble standard no one can truthfully implement.

The concrete node-facing version of that boundary now lives in [[node-card-and-minimum-adapter-contract]].
If the immediate question is what to inspect before deciding, the prioritized reading list now lives in [[high-impact-artifacts-for-multiplayer-harness-design]].

## Related pages
Read this with [[node-card-and-minimum-adapter-contract]], [[high-impact-artifacts-for-multiplayer-harness-design]], [[multiplayer-agent-harnesses-and-p2p-networks]], [[moldable-operations-studio-architecture-spec]], [[moldable-operations-studio-schema-pass]], [[legacy-distributed-systems-ideas-for-moldable-operations-studio]], [[grounding-moldable-operations-studio-ideas-in-real-research]], [[new-harness-design-notes]], and [[non-hierarchical-agent-orchestration]].
