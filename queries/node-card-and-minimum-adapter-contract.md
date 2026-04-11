---
title: Node Card and Minimum Adapter Contract
created: 2026-04-10
updated: 2026-04-10
type: query
tags: [semantics, work-management, memory, safety]
sources: [queries/how-to-build-a-multiplayer-harness-network.md, queries/sovereign-identity-and-observed-goals-schema-pass.md, queries/moldable-operations-studio-schema-pass.md, queries/multiplayer-agent-harnesses-and-p2p-networks.md, raw/articles/google-agent2agent-protocol.md, raw/papers/arxiv-ehtesham-2025-survey-agent-interoperability-protocols.md, raw/articles/w3c-verifiable-credentials-data-model-v2.md, raw/papers/li-mitchell-winsborough-role-based-trust-management-framework.md, raw/papers/bauer-schneider-felten-appel-proof-carrying-authorization.md, raw/papers/torres-arias-2019-in-toto.md, raw/articles/w3c-prov-dm.md]
---

# Node Card and Minimum Adapter Contract

## Goal
Define the smallest honest participation contract by which a harness can jack into the multiplayer collaboration fabric without first adopting the full native runtime.

This page makes the vague phrase “every harness can jack in” concrete.

## Short answer
The node card is the signed public description of a node’s identity, transports, supported schema versions, and participation capabilities.

The minimum adapter contract is the smallest interface a foreign harness must implement to:
- ingest shared work objects
- emit normalized control-plane events
- expose artifacts and traces honestly
- respect approvals, budgets, and revocations
- report frontiers and staleness without lying

The node card tells other nodes what this harness claims it can do.
The adapter contract is how it proves that claim at runtime.

## Design rules
1. The node card is a projection over durable local objects, not an extra truth store.
2. Capability claims must be narrow and falsifiable.
3. Partial participation is normal.
4. Local policy remains local.
5. Frontiers, revocations, and uncertainty must be surfaced explicitly.
6. The adapter may be thinner than the native runtime, but it may not fabricate semantics it does not actually support.

## Participation modes
The contract supports three integration modes from [[how-to-build-a-multiplayer-harness-network]]:

### 1. Native node
- the harness natively stores the shared objects and events
- the node card is mostly a direct export of internal state

### 2. Sidecar bridge
- the harness keeps its internal model
- a sidecar translates between local state and shared control-plane objects
- this is the main intended mode

### 3. Gateway wrapper
- the harness can only expose a narrow subset
- good enough for task/artifact exchange, not full semantic fidelity

The contract must make these differences visible instead of pretending everyone is equally legible.

## The node card
The node card is the transport-facing advertisement document.
It should be derivable from at least:
- `identity_card`
- `capability_card`
- current transport endpoints
- current accepted schema versions
- current transparency / status anchors

It should not duplicate hidden local state that cannot be checked later.

## `node_card`
```yaml
node_card:
  node_id: string
  node_card_version: integer
  issued_at: RFC3339 timestamp
  expires_at: RFC3339 timestamp?

  identity:
    identity_card_id: string
    self_certifying_handle: string
    display_name: string?
    local_namespace_root: string?
    transparency_anchors: [transparency_anchor]

  transports:
    - endpoint_id: string
      transport: https | websocket | json_rpc | mcp | custom
      uri: string
      auth_modes: [none, bearer, signature, presentation]
      priority: integer

  schema_support:
    core_schema_versions: [integer]
    sovereignty_schema_versions: [integer]
    supported_object_kinds: [string]
    supported_event_kinds: [string]
    supported_relation_kinds: [string]

  adapter_mode:
    native | sidecar_bridge | gateway_wrapper

  participation:
    can_consume_work_items: boolean
    can_emit_artifacts: boolean
    can_emit_traces: boolean
    can_request_approvals: boolean
    can_honor_approvals: boolean
    can_honor_authority_budgets: boolean
    can_participate_in_cases: boolean
    can_publish_views: boolean
    can_issue_credentials: boolean
    can_verify_presentations: boolean

  fidelity:
    frontier_reporting: exact | bounded_staleness | none
    trace_fidelity: full | summary_only | none
    artifact_fidelity: content_addressed | opaque_blob | metadata_only
    commitment_fidelity: native | derived | none
    hypothesis_fidelity: native | derived | none
    case_fidelity: native | derived | none

  formats:
    accepted_presentation_formats: [sd_jwt_vc, vc_jwt, ldp_vc, custom]
    accepted_proof_formats: [proof_carrying_auth, detached_signature, dsse, in_toto, custom]
    artifact_bundle_formats: [dsse, in_toto, custom]

  policy_surface:
    policy_version_ids: [string]
    approval_actions: [promote_branch, deploy, publish_view, grant_budget, change_policy]
    budget_kinds: [token_count, tool_calls, network_calls, branch_creations, deploy_attempts, approval_routes, concurrent_runs]

  limits:
    max_subscription_count: integer?
    max_blob_bytes: integer?
    max_object_batch: integer?
    max_event_batch: integer?

  status:
    status_ref: string?
    current_membership_epoch: integer?
    last_known_frontier: [event_id]?
```

## Node-card rules
1. `node_id` must be stable across endpoint changes and should correspond to the sovereign identity handle.
2. The card must be signed or otherwise authenticated by the node identity.
3. The card is cacheable, but revocation/status checks may supersede cached claims.
4. `adapter_mode` is mandatory; this avoids the ritual dishonesty in which a gateway wrapper cosplays as a native node.
5. Fidelity flags are normative, not decorative. If `trace_fidelity = summary_only`, peers must not assume reconstructible trace spans exist.
6. Unsupported capability must be represented as `false` or `none`, never inferred optimistically.

## Minimum adapter contract
The adapter contract is the local implementation surface a harness or sidecar must expose.

It is intentionally smaller than the full internal runtime API.

## Required adapter functions
The minimum adapter contract has six required families.

### 1. Identity and card publication
```yaml
publish_node_card() -> node_card
refresh_node_card() -> node_card
get_status_snapshot() ->
  status_ref: string?
  transparency_anchors: [transparency_anchor]
  current_membership_epoch: integer?
```

Meaning:
- emit the current node card
- refresh it after key rotation, endpoint change, capability change, or policy change

### 2. Frontier and staleness reporting
```yaml
get_frontier(scope_refs?: [object_ref]) ->
  read_frontier: [event_id]
  fidelity: exact | bounded_staleness | none
  stale_after_ms: integer?
  stale_reason: string?
```

Meaning:
- a peer must be able to ask what this adapter has really observed
- “I don’t know” is acceptable
- fabricated certainty is not

### 3. Inbound object ingestion
```yaml
ingest_objects(objects: [object_envelope]) ->
  accepted: [object_id]
  rejected:
    - object_id: string
      reason: unsupported_kind | invalid_schema | unauthorized | stale_policy | malformed | too_large | other
  ack_frontier: [event_id]
```

Minimum supported inbound kinds for a meaningful bridge:
- `work_item`
- `artifact`
- `approval`
- `authority_budget`
- `identity_card`
- `capability_card`

Optional but recommended:
- `commitment`
- `policy_version`
- `dispute_case`

Meaning:
- this is how shared work enters the foreign harness
- rejection reasons are explicit and typed

### 4. Outbound event export
```yaml
export_events(since_frontier?: [event_id], limit?: integer) ->
  events: [event]
  read_frontier: [event_id]
  has_more: boolean
```

Minimum event families a meaningful bridge should export if it claims the corresponding capability:
- `artifact.recorded`
- `trace.opened`
- `trace.closed`
- `approval.requested`
- `approval.granted` / `approval.rejected`
- `authority_budget.consumed`
- `identity_card.revoked` if local trust changes invalidate the node

Optional but recommended:
- `commitment.*`
- `case.*`
- `goal_hypothesis.*`

Meaning:
- local actions must become normalized control-plane facts
- a bridge may derive these from local runtime state, but it must mark fidelity honestly in the node card

### 5. Artifact and trace retrieval
```yaml
fetch_object(object_id: string) -> object_envelope?
fetch_artifact_blob(artifact_id: string) ->
  content_hash: string
  media_type: string
  bytes: base64 | uri
  proof_refs: [string]
fetch_trace(trace_id: string) ->
  trace: object
  fidelity: full | summary_only | none
```

Meaning:
- if you claim to emit artifacts or traces, peers need a way to fetch them
- “metadata-only” is acceptable if declared

### 6. Control actions under policy
```yaml
apply_control_action(action) ->
  result: accepted | denied | indeterminate
  event_id: string?
  policy_version_id: string?
  authorization_proof_id: string?
  reason: string?
```

Minimum control actions:
- `request_approval`
- `record_approval_outcome`
- `grant_budget`
- `revoke_budget`
- `acknowledge_receipt`

Optional:
- `open_case`
- `record_commitment_transition`
- `record_goal_hypothesis`

Meaning:
- this is the narrowest runtime path for approvals, budgets, and governance-sensitive actions
- all such actions must be evaluated under explicit policy or returned as indeterminate

## Minimum honesty contract
A harness may be thin, but it may not lie.

Minimum honesty rules:
1. If the adapter cannot report exact frontier, it must say so.
2. If the adapter cannot honor authority budgets, it must say so.
3. If approvals in the foreign harness are only advisory, `can_honor_approvals` must be false.
4. If traces are summaries reconstructed after the fact, `trace_fidelity` must not be `full`.
5. If local semantics cannot support commitments, cases, or goal hypotheses, those fidelity flags must be `none`.

The adapter is allowed to be partial.
It is not allowed to be romantic.

## Required mappings
A sidecar bridge must define three explicit translation tables.

### A. Local-to-shared object mapping
```yaml
local_to_shared_object_map:
  local_kind: string
  shared_kind: string
  mapping_version: integer
  field_mappings: object
  dropped_fields: [string]
  synthetic_fields: [string]
```

### B. Local-to-shared event mapping
```yaml
local_to_shared_event_map:
  local_event_kind: string
  shared_event_type: string
  trigger_condition: string
  confidence: exact | derived | heuristic
```

### C. Unsupported semantics declaration
```yaml
unsupported_semantics:
  - shared_kind: string
    reason: no_local_analog | cannot_verify | too_opaque | policy_forbidden | performance_cost | other
```

These tables are where translation honesty becomes checkable instead of aspirational.

## Minimum acceptance profile
A foreign harness counts as meaningfully integrated if it can do all of the following:
1. Publish a valid node card.
2. Ingest `work_item`, `artifact`, `approval`, and `authority_budget` objects.
3. Export normalized events for artifacts and trace progress.
4. Fetch emitted artifacts by id.
5. Report frontiers or bounded staleness honestly.
6. Reject unsupported actions with typed reasons instead of silent no-op behavior.

Everything beyond that is desirable, not required.

## Sovereignty-aware additions
Because this contract sits on the sovereignty layer, these fields are especially important.

### Required when supported
- `identity.identity_card_id`
- `identity.self_certifying_handle`
- `accepted_presentation_formats`
- `accepted_proof_formats`
- `status_ref`
- `transparency_anchors`
- `policy_version_ids`

### Required if claiming stronger participation
If a node claims any of these, it must support the corresponding minimum object or action:
- `can_issue_credentials` -> `credential.issued`
- `can_verify_presentations` -> `presentation.submitted` + `authorization_proof.recorded`
- `can_participate_in_cases` -> `dispute_case`
- `commitment_fidelity != none` -> `commitment` object and at least `commitment.created` / `commitment.discharged` / `commitment.violated`
- `hypothesis_fidelity != none` -> `hypothesis_set` + `goal_hypothesis`

## Error model
The adapter contract should return typed failures rather than ad hoc prose whenever possible.

Minimum error kinds:
- unsupported_kind
- unsupported_action
- invalid_schema
- unauthorized
- stale_policy
- revoked_identity
- expired_presentation
- invalid_proof
- frontier_too_old
- frontier_unknown
- not_found
- too_large
- internal_error

## Security and replay rules
1. `authorization_proof` must bind action + audience + nonce + policy version + evaluated frontier.
2. `presentation` must not outlive its declared expiry.
3. Revoked identities, credentials, or budgets must block later dependent control actions.
4. Artifact retrieval must preserve content hash semantics.
5. If the adapter emits a proof ref for an artifact, it must be fetchable or locally verifiable.

## Suggested implementation order
1. Implement node-card publication.
2. Implement frontier reporting.
3. Implement inbound `work_item` / `artifact` / `approval` / `authority_budget` ingestion.
4. Implement outbound artifact + trace event export.
5. Implement artifact fetch by id.
6. Implement approval/budget control actions.
7. Add optional commitment, case, and hypothesis support.

That is the minimum path from “private harness” to “federated participant.”

## Acceptance tests
A useful first adapter should satisfy these tests:
- A peer can fetch the node card and understand what this harness really supports.
- A work item can be ingested and either accepted or rejected with a typed reason.
- A locally produced artifact appears as a normalized exported event and can be fetched by id.
- A granted budget can be honored or explicitly rejected as unsupported.
- A revoked identity or budget blocks subsequent sensitive actions.
- Two peers can compare frontiers and detect staleness without guessing.

## Bottom line
The node card is the node’s signed self-description.
The adapter contract is the smallest honest bridge between a foreign harness and the shared control plane.

If we get those two things right, “jack in” stops being a metaphor and becomes an engineering boundary.

## Related pages
Read this with [[how-to-build-a-multiplayer-harness-network]], [[sovereign-identity-and-observed-goals-schema-pass]], [[moldable-operations-studio-schema-pass]], [[multiplayer-agent-harnesses-and-p2p-networks]], [[sovereignty-and-observed-goals-ledgers-for-multiplayer-harnesses]], and [[commitment-governance-semantics-for-multiplayer-harness]].
