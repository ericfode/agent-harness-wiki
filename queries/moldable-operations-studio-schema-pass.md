---
title: Moldable Operations Studio Schema Pass
created: 2026-04-09
updated: 2026-04-09
type: query
tags: [orchestration, work-management, semantics, concurrency]
sources: [queries/moldable-operations-studio-architecture-spec.md, queries/legacy-distributed-systems-ideas-for-moldable-operations-studio.md, queries/non-linear-interface-options-for-next-harness.md, queries/web-patterns-for-non-linear-harness-interfaces.md, concepts/work-management-primitives.md, concepts/partial-order-trace-semantics.md]
---

# Moldable Operations Studio Schema Pass

## Goal
Turn [[moldable-operations-studio-architecture-spec]] into a minimum typed control-plane schema that can back CLI, graph, queue, grid, evidence, and moldable inspector views without semantic drift. The main import from [[legacy-distributed-systems-ideas-for-moldable-operations-studio]] is that surfaces may differ, but causality, commitment, and authority must not.

The concrete implementation refinements suggested by HCI, CSCW, provenance, and security literature now live in [[grounding-moldable-operations-studio-ideas-in-real-research]]. The operator-facing screen model now lives in [[moldable-operations-studio-wireframes]].

## Design rules
- The transcript is a projection, not the source of truth.
- One append-only event log backs every surface.
- Objects have stable ids across CLI, IDE, web, and generated views.
- Wall-clock order is advisory; causal order is semantic.
- Approval, promotion, budget grants, view publication, policy change, and checkpoint finalization are control-plane facts, not UI state.
- Tentative work is first-class and must not be confused with committed state.

## Common types

```yaml
id:
  description: stable opaque string; sortable ids are fine, but semantics come from causal parents, not lexical order

actor_ref:
  actor_id: string
  actor_kind: human | agent | service

object_ref:
  object_id: string
  kind: work_item | branch | checkpoint | approval | artifact | trace | view_definition | coalition | authority_budget | session_token

label_set:
  secrecy: public | workspace | restricted | secret
  integrity: untrusted | agent | reviewed | approved
  compartments: [string]

lifecycle:
  tentative | committed | compensated | superseded | abandoned

suspicion_state:
  healthy | delayed | suspected_failed | unreachable | confirmed_failed | recovered

view_epoch:
  description: explicit membership version for live coalitions, subscriptions, or watcher sets
  value: integer

frontier:
  description: antichain of maximal event ids known to be included in a read, object head, or checkpoint
  value: [event_id]
```

## Object envelope

```yaml
object_envelope:
  object_id: string
  schema_version: integer
  kind: work_item | branch | checkpoint | approval | artifact | trace | view_definition | coalition | authority_budget | session_token
  lifecycle: tentative | committed | compensated | superseded | abandoned
  frontier: [event_id]
  created_at: RFC3339 timestamp
  updated_at: RFC3339 timestamp
  created_by: actor_ref
  labels: label_set
  metadata: object
```

Each object has both `lifecycle` and a domain-specific `state`. `lifecycle` answers tentative versus committed versus superseded. `state` answers the workflow state of the specific object.

## Event schema

```yaml
event:
  event_id: string
  schema_version: integer
  event_type: string
  clock:
    lamport: integer
    parents: [event_id]
  wall_time: RFC3339 timestamp
  actor: actor_ref
  surface: cli | ide | web | app | automation | system
  session_token_id: string?
  view_epoch: integer?
  affected_objects: [object_ref]
  lifecycle: tentative | committed | compensated | superseded | abandoned
  suspicion: suspicion_state
  labels: label_set
  consistency_class: causal | linearizable
  payload: object
```

## Minimum core event types

### Work and branch
- `work_item.created`
- `work_item.claimed`
- `work_item.updated`
- `work_item.blocked`
- `work_item.ready_for_review`
- `work_item.completed`
- `work_item.canceled`
- `branch.created`
- `branch.updated`
- `branch.rebased`
- `branch.promotable`
- `branch.promoted`
- `branch.merged`
- `branch.abandoned`

### Checkpoints and approvals
- `checkpoint.proposed`
- `checkpoint.finalized`
- `checkpoint.reopened`
- `checkpoint.invalidated`
- `approval.requested`
- `approval.granted`
- `approval.rejected`
- `approval.expired`
- `approval.rescinded`

### Evidence and runtime
- `artifact.recorded`
- `artifact.superseded`
- `trace.opened`
- `trace.closed`
- `tool_call.started`
- `tool_call.finished`
- `tool_call.failed`
- `suspicion.raised`
- `suspicion.cleared`

### Coordination and surfaces
- `coalition.formed`
- `coalition.reconfigured`
- `coalition.dissolved`
- `authority_budget.granted`
- `authority_budget.consumed`
- `authority_budget.revoked`
- `session_token.issued`
- `session_token.revoked`
- `view_definition.drafted`
- `view_definition.published`
- `policy.changed`

### Linearizable subset
The minimum linearizable event set is:
- `approval.granted`
- `approval.rejected`
- `approval.rescinded`
- `authority_budget.granted`
- `authority_budget.revoked`
- `branch.promoted`
- `view_definition.published`
- `policy.changed`
- `checkpoint.finalized`

Everything else may remain causal or eventually materialized, provided the surface declares its frontier and staleness.

## Object schemas

Work-item state follows [[work-management-primitives]] while keeping commitment separate.

### `work_item`
```yaml
work_item:
  object_id: string
  title: string
  summary: string
  state: pending | claimed | active | review | blocked | completed | canceled
  requested_by: actor_ref
  owner: actor_ref?
  coalition_id: string?
  depends_on_work_item_ids: [string]
  blocked_on_refs: [object_ref]
  branch_id: string?
  input_refs: [object_ref]
  output_refs: [object_ref]
  required_approval_ids: [string]
  acceptance_artifact_ids: [string]
```

### `branch`
```yaml
branch:
  object_id: string
  name: string
  state: open | frozen | promotable | promoted | merged | abandoned
  parent_branch_id: string?
  fork_checkpoint_id: string?
  target_branch_id: string?
  head_frontier: [event_id]
  head_artifact_id: string?
  related_work_item_ids: [string]
  promotion_ready: boolean
```

### `checkpoint`
```yaml
checkpoint:
  object_id: string
  name: string
  state: proposed | finalized | invalidated
  scope: branch | workspace | review_bundle
  scope_refs: [object_ref]
  cut_mode: quiescent | suspended
  cut_frontier: [event_id]
  manifest:
    branch_ids: [string]
    artifact_ids: [string]
    open_trace_ids: [string]
    pending_approval_ids: [string]
  reopened_branch_ids: [string]
```

### `approval`
```yaml
approval:
  object_id: string
  subject: object_ref
  requested_action: promote_branch | deploy | publish_view | spend_budget | override_policy
  state: pending | granted | rejected | expired | rescinded
  requester: actor_ref
  required_approver_ids: [string]
  decision_by: actor_ref?
  decision_reason: string?
  related_checkpoint_id: string?
  expires_at: RFC3339 timestamp?
```

### `artifact`
```yaml
artifact:
  object_id: string
  artifact_kind: repo_diff | file_snapshot | build_log | test_report | prompt | note | deployment_receipt | evidence_bundle
  storage_uri: string
  content_hash: string
  produced_by_event_id: string
  derived_from_artifact_ids: [string]
  branch_id: string?
  checkpoint_id: string?
```

### `trace`
```yaml
trace:
  object_id: string
  trace_kind: run | tool_call | evaluation | deployment | conversation
  state: open | closed | failed | truncated
  root_span_id: string
  start_event_id: string
  end_event_id: string?
  related_work_item_id: string?
  artifact_ids: [string]
  suspicion: suspicion_state
```

### `coalition`
```yaml
coalition:
  object_id: string
  purpose: string
  state: forming | active | reconfiguring | dissolved
  membership_epoch: integer
  member_ids: [string]
  coordinator_id: string?
  protocol_ref: string?
  authority_budget_ids: [string]
  work_item_ids: [string]
```

### `session_token`
```yaml
session_token:
  object_id: string
  principal: actor_ref
  surfaces: [cli, ide, web, app, automation]
  issued_at: RFC3339 timestamp
  expires_at: RFC3339 timestamp
  guarantees: [read_your_writes, monotonic_reads, writes_follow_reads, monotonic_writes]
  last_seen_frontier: [event_id]
  state: active | expired | revoked
```

## `view_definition` schema
`view_definition` is the durable description of a projection. The rendered view is a cache over the log, not an independent truth store.

```yaml
view_definition:
  object_id: string
  name: string
  kind: cli_transcript | work_graph | queue | grid | evidence | spatial_canvas | inspector | custom
  version: integer
  publication_state: draft | published | deprecated
  scope:
    root_refs: [object_ref]
    branch_ids: [string]
    checkpoint_ids: [string]
  query:
    kinds: [work_item, branch, checkpoint, approval, artifact, trace, coalition, authority_budget]
    filter: predicate_ast
    relations: [depends_on, blocked_on, derived_from, caused_by, member_of]
    group_by: [field_name]
    sort: [field_name]
    limit: integer?
  layout:
    panes:
      - pane_id: string
        pane_kind: transcript | graph | queue | grid | evidence | inspector | markdown
        source: string
    default_focus_ref: object_ref?
  actions:
    allowed_commands: [claim_work, request_approval, reopen_checkpoint, promote_branch, publish_view]
  consistency:
    read_level: session | causal | linearizable
    stale_after_ms: integer
    show_frontier: boolean
  origin: manual | generated | hybrid
  authored_by: actor_ref
  source_prompt: string?
```

Notes:
- The CLI transcript is just a published `kind: cli_transcript`, not a privileged storage model.
- `view_definition.drafted` may be causal.
- `view_definition.published` is linearizable because multiple surfaces must agree on the published definition.
- Materialized projections are disposable caches keyed by `(view_definition_id, frontier, labels, membership_epoch)`. They may be rebuilt at any time from the log.

## `authority_budget` schema
`authority_budget` is the escrow object for bounded delegated rights. It exists so autonomy can be real without becoming universal ambient permission.

```yaml
authority_budget:
  object_id: string
  subject:
    subject_kind: actor | coalition
    subject_id: string
  sponsor: actor_ref
  state: active | exhausted | revoked | expired
  scope:
    branch_ids: [string]
    work_item_ids: [string]
    file_globs: [string]
    tool_allowlist: [string]
    surface_allowlist: [cli, ide, web, app, automation]
  limits:
    token_count: integer?
    tool_calls: integer?
    network_calls: integer?
    branch_creations: integer?
    deploy_attempts: integer?
    approval_routes: integer?
    concurrent_runs: integer?
  prohibitions:
    protected_file_globs: [string]
    forbidden_actions: [promote_branch, change_policy]
  required_followups:
    require_artifact_kinds: [test_report, repo_diff, deployment_receipt]
    require_approval_for: [deploy, promote_branch]
  consumed:
    token_count: integer
    tool_calls: integer
    network_calls: integer
    branch_creations: integer
    deploy_attempts: integer
    approval_routes: integer
    concurrent_runs: integer
  valid_from: RFC3339 timestamp
  valid_until: RFC3339 timestamp
  revoked_by: actor_ref?
  revocation_reason: string?
```

Rules:
- `authority_budget.granted` and `authority_budget.revoked` are linearizable.
- `authority_budget.consumed` may be causal, but it must monotonically reduce remaining capacity.
- A budget may widen autonomy only within its declared scope. It may never mint new authority outside that scope.
- Promotion, policy change, and view publication are not implied by generic write access; they require explicit budget or approval.

## Checkpoint and cut semantics
This is the replay-facing companion to [[partial-order-trace-semantics]]: the cut is defined over a partial order, not a flat timestamp.

- A checkpoint is the tuple `(scope_refs, cut_mode, cut_frontier, manifest)`.
- `cut_frontier` must be causally closed within the declared scope: if an event is included, every in-scope causal ancestor is included.
- `cut_mode: quiescent` requires no open traces or pending approvals in scope.
- `cut_mode: suspended` allows open traces or pending approvals only if they are listed in `manifest.open_trace_ids` or `manifest.pending_approval_ids`. Reopen must recreate them as still open, not silently resolve them.
- External side effects are in the cut only when a receipt artifact or failure event is in the cut. Otherwise the side effect remains open in the manifest.
- `checkpoint.proposed` may be causal. `checkpoint.finalized` is linearizable and freezes the cut.
- Reopening a finalized checkpoint creates a new branch from exactly that cut. Two surfaces opening the same checkpoint must reconstruct the same frontier, same manifest, and same redaction boundaries.

## Branch promotion rules
Promotion is a commit action over a pinned checkpoint, not a floating branch head.

```yaml
branch_promoted_payload:
  source_branch_id: string
  source_checkpoint_id: string
  target_branch_id: string
  strategy: fast_forward | merge_commit | replace_projection
  validated_target_frontier: [event_id]
  new_target_frontier: [event_id]
```

Rules:
1. Promotion operates on a finalized checkpoint.
2. The source branch must contain `source_checkpoint_id` and be `open` or `frozen`.
3. The target branch must not be `abandoned`.
4. All approvals required by the source checkpoint, related work items, and target policy must be granted and unexpired.
5. Any rejected approval, required check in failed state, or trace in `confirmed_failed` blocks promotion. `suspected_failed` or `unreachable` require either clearance or explicit waiver.
6. If the target branch has advanced beyond `validated_target_frontier`, the promotion is stale and must be revalidated or merged again.
7. `branch.promoted` is linearizable and records both the old target frontier and the new target frontier.
8. Promotion changes commitment state on the target branch; it does not erase the source branch or its evidence.
9. Objects displaced on the target become `superseded`; they are not silently rewritten out of history.

## Minimal consistency contract across surfaces
The studio does not need universal strong consistency everywhere, but it does need a small cross-surface contract.

1. Shared identity
   - The same `object_id` and `event_id` mean the same thing on CLI, IDE, web, app, and generated views.
   - Surfaces may render differently, but they may not clone or renumber the underlying control objects.

2. Frontier-carrying reads and writes
   - Every write returns `ack_event_id` and `ack_frontier`.
   - Every read returns `read_frontier`.

3. Session guarantees
   - A client presenting a `session_token` with `last_seen_frontier = F` must receive a `read_frontier` that causally dominates `F`, or an explicit stale response.
   - If a surface cannot satisfy the session frontier, it must refresh, block, or visibly mark itself stale and disable destructive controls.

4. Linearizable control operations
   - `approval.*` outcome changes, `authority_budget.granted`, `authority_budget.revoked`, `branch.promoted`, `view_definition.published`, `policy.changed`, and `checkpoint.finalized` appear in one total order across surfaces.

5. Causal completeness
   - A surface may filter or redact, but it may not present a committed child event without either its in-scope causal parents or an explicit redaction/truncation marker.

6. Epoch fidelity
   - Live collaboration views must track `view_epoch` and `coalition.membership_epoch`.
   - Reconfiguration must render as a boundary, not as a silent blend of old and new memberships.

7. Projection convergence
   - For a fixed `(view_definition, labels, membership_epoch)`, materialized projections on different surfaces must converge to the same object set and object states at the same frontier.
   - A stale projection must show its frontier lag.

8. Checkpoint equivalence
   - Opening checkpoint `X` from CLI, graph, queue, or evidence view must resolve the same `cut_frontier` and the same manifest.

## Related pages
Read this with [[moldable-operations-studio-wireframes]], [[grounding-moldable-operations-studio-ideas-in-real-research]], [[moldable-operations-studio-architecture-spec]], [[legacy-distributed-systems-ideas-for-moldable-operations-studio]], [[non-linear-interface-options-for-next-harness]], [[web-patterns-for-non-linear-harness-interfaces]], [[work-management-primitives]], and [[partial-order-trace-semantics]].
