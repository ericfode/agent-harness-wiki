---
title: Moldable Operations Studio Architecture Spec
created: 2026-04-09
updated: 2026-04-09
type: query
tags: [orchestration, work-management, semantics, formal-methods]
sources: [queries/non-linear-interface-options-for-next-harness.md, queries/web-patterns-for-non-linear-harness-interfaces.md, queries/legacy-distributed-systems-ideas-for-moldable-operations-studio.md, queries/new-harness-design-notes.md, raw/articles/openai-unlocking-codex-harness.md, raw/articles/openai-introducing-codex-app.md]
---

# Moldable Operations Studio Architecture Spec

## Goal
Specify a harness architecture in which the CLI remains an exact textual kernel, but the larger system becomes a moldable operations studio: one durable control plane, many projections, explicit provenance, and first-class support for autonomous and human-supervised work.

The concrete typed companion to this page is [[moldable-operations-studio-schema-pass]]. The speculative design companion is [[sci-fi-audit-for-moldable-operations-studio]]. The real-research grounding pass is [[grounding-moldable-operations-studio-ideas-in-real-research]]. The screen-model companion is [[moldable-operations-studio-wireframes]].

## Non-goals
- Replacing code with a toy canvas.
- Forcing every task through one graphical control shape.
- Turning the control plane into a giant eventually-consistent fever dream.

## Design axioms
1. The transcript is a projection, not the source of truth.
2. All surfaces are clients of one shared state model.
3. Causality matters more than wall-clock order.
4. Partial failure must remain legible.
5. Human approval is a typed work primitive.
6. Speculative work is normal and should be represented explicitly.
7. A surface earns its existence by making a real operational question cheaper to answer.

## Core state model

### 1. Durable event log
The studio stores append-only events for user actions, agent actions, tool calls, approvals, rejections, view changes, failures, suspicions, merges, and checkpoint creation.

Every event should include:
- event id
- logical timestamp
- causal parents or frontier
- actor identity
- view epoch
- affected objects
- secrecy/integrity labels where relevant

This imports the lessons of [[vector-clock]], [[virtual-synchrony]], and [[jif]].

### 2. Control objects
The minimum durable object family should be:
- `work_item`
- `branch`
- `checkpoint`
- `approval`
- `artifact`
- `trace`
- `view_definition`
- `coalition`
- `authority_budget`
- `session_token`

The current transcript thread is then only one possible rendering over these objects.

### 3. Consistent cuts
A `checkpoint` is not merely a label on recent history. It should identify a consistent cut over the relevant state so replay, audit, and review do not begin from an incoherent mixture. This is the Chandy–Lamport import.

### 4. Tentative versus committed state
Objects and events should distinguish:
- tentative
- committed
- compensated
- superseded
- abandoned

This is the optimistic-replication / Bayou lesson. Branches are normal, and the studio should never confuse speculative work with promoted state.

## Consistency model

### 1. Selective linearizability
Only a small set of control-plane operations need linearizable semantics:
- approve / reject
- grant / revoke authority budget
- promote branch
- publish view definition
- change policy
- finalize checkpoint

Everything else may use weaker but explicit semantics.

### 2. Session guarantees across surfaces
Humans and agents should receive at least:
- read-your-writes
- monotonic reads
- writes-follow-reads
- monotonic writes

A person who approves in the app should not open the CLI and be told, with a straight face, that the past is still pending.

### 3. View epochs
Live collaborations, subscriptions, and coalitions should be versioned by explicit membership epochs. This makes failover, reassignment, and watcher changes renderable rather than mystical.

### 4. Suspicion model
Runtime status should distinguish:
- healthy
- delayed
- suspected failed
- unreachable
- confirmed failed
- recovered

Decisions taken under suspicion should record that fact in provenance.

## Authority model

### 1. Escrowed rights
Delegated autonomy should use bounded budgets rather than universal central gates. Budgets may cover:
- token spend
- API calls
- deployment attempts
- file-edit scope
- branch creation rights
- approval routing rights

### 2. Labeled artifacts
Artifacts, traces, and prompts should carry information-flow labels describing who may read, derive from, or act on them. This is finer-grained than generic workspace roles.

### 3. Self-certifying references
Remote artifacts and capabilities should prefer cryptographically meaningful handles when crossing trust boundaries.

## Interaction model

### Required projections
The first serious studio should support at least these synchronized views:

1. **CLI transcript view**
   - exact text stream and tool I/O
2. **Work graph view**
   - items, dependencies, branches, approvals, coalitions
3. **Queue / inbox view**
   - pending approvals, stalled work, escalations, human asks
4. **Grid / fleet view**
   - runs by state across many branches or agents
5. **Evidence / trace view**
   - logs, tool outputs, runtime spans, diff lineage, queryable replay
6. **Spatial exploration canvas**
   - loose arrangement of evidence before formalization
7. **Moldable inspector view**
   - generated pane specialized for the current object or question

Each view is a `view_definition` plus a materialized projection over the same state.

## Protocol model

### 1. Typed handoffs
Approvals, tool calls, reviewer requests, and escalation flows should be expressed as typed protocol steps, not free-text suggestion clouds.

### 2. Session-typed boundaries
Where a protocol is stable enough, the studio should check conformance: who may send next, what object shape is expected, and what counts as completion.

### 3. Human override
Humans may intervene by issuing commands that become ordinary durable control-plane events. Override should not mean bypassing history.

## Replay and debugging

### 1. Queryable provenance
The replay system should answer:
- what caused this state?
- what was concurrent but independent?
- when was this object first suspected bad?
- what tentative work later became committed?
- what changed between checkpoint A and B?

### 2. Counterfactual support
Where feasible, replay should support branch-local counterfactuals: inspect what the system would have looked like had a branch been promoted or an approval been denied.

## Suggested implementation order
1. Build the durable event log with causal metadata.
2. Add consistent-cut checkpoints and replay queries.
3. Separate linearizable control operations from weaker projection updates.
4. Add session guarantees across CLI/app/web surfaces.
5. Add work graph, queue, and grid projections.
6. Add approval nodes and escrowed authority budgets.
7. Add moldable inspectors.
8. Add spatial exploration canvas and direct-manipulation affordances.

## Acceptance criteria
A first usable moldable operations studio should make the following statements true:
- The same work can be inspected coherently from CLI, graph, and queue views.
- A checkpoint can be reopened as a consistent cut.
- Parallel edits can be recognized as concurrent rather than merely conflicting.
- Approval and promotion events are durable, auditable control-plane facts.
- Humans and agents see monotonic state across surfaces.
- Partial failure is represented explicitly rather than buried in retry folklore.
- Delegated autonomy can operate inside bounded budgets.

## Main warning
Do not build the projections first and invent the semantics later. The old distributed-systems literature is mostly a reminder that nice surfaces become nonsense quickly when the underlying control plane cannot distinguish causality, membership, suspicion, tentative state, and committed state.

## Related pages
Read this with [[moldable-operations-studio-wireframes]], [[grounding-moldable-operations-studio-ideas-in-real-research]], [[moldable-operations-studio-schema-pass]], [[sci-fi-audit-for-moldable-operations-studio]], [[legacy-distributed-systems-ideas-for-moldable-operations-studio]], [[web-patterns-for-non-linear-harness-interfaces]], [[non-linear-interface-options-for-next-harness]], [[new-harness-design-notes]], [[work-management-primitives]], [[partial-order-trace-semantics]], and [[harness-engineering]].
