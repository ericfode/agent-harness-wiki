---
title: Sovereign Identity and Observed-Goals Schema Pass
created: 2026-04-10
updated: 2026-04-10
type: query
tags: [semantics, work-management, memory, safety]
sources: [queries/moldable-operations-studio-schema-pass.md, queries/sovereignty-and-observed-goals-ledgers-for-multiplayer-harnesses.md, queries/commitment-governance-semantics-for-multiplayer-harness.md, raw/articles/w3c-verifiable-credentials-data-model-v2.md, raw/papers/li-mitchell-winsborough-role-based-trust-management-framework.md, raw/papers/bauer-schneider-felten-appel-proof-carrying-authorization.md, raw/papers/claimchain.md, raw/papers/torres-arias-2019-in-toto.md, raw/articles/w3c-prov-dm.md, raw/papers/medina-mora-winograd-flores-flores-action-workflow-approach.md, raw/papers/fornara-colombetti-commitment-based-agent-communication-language.md, raw/papers/singh-chopra-computational-governance-violable-contracts.md, raw/papers/keren-gal-karpas-goal-recognition-design.md, raw/papers/ramirez-geffner-probabilistic-plan-recognition.md, raw/papers/erickson-et-al-socially-translucent-systems.md, raw/articles/self-certifying-file-system.md, raw/articles/rivest-lampson-1996-sdsi.md, raw/papers/birgisson-et-al-2014-macaroons.md, raw/articles/rfc-9420-mls-protocol.md, raw/papers/efstathopoulos-et-al-2005-asbestos.md]
---

# Sovereign Identity and Observed-Goals Schema Pass

## Goal
Extend [[moldable-operations-studio-schema-pass]] with a sovereignty layer that replaces scalar reputation with sovereign identity, portable attestations, evidence receipts, explicit commitments, inferred-goal hypotheses, and governance objects.

This page is the concrete schema companion to [[sovereignty-and-observed-goals-ledgers-for-multiplayer-harnesses]] and the commitment/governance extraction in [[commitment-governance-semantics-for-multiplayer-harness]].

## Non-goals
- Adding a kinder global reputation score.
- Treating inferred goals as facts.
- Forcing all nodes into one universal naming hierarchy.
- Letting cryptographic objects impersonate judgment they do not actually encode.

## Design rules
1. Identity is sovereign and locally named.
2. Credentials are portable, but trust evaluation stays local.
3. Raw evidence is stored separately from interpretations.
4. Commitments are first-class, violable, and governable.
5. Inferred goals are revisionable hypotheses with evidence and expiry.
6. Governance actions are durable control-plane events, not moderator folklore.
7. Subjects must be able to inspect and contest what the ledger says about them.
8. No scalar `trust_score`, `reputation_score`, or equivalent flattening field exists anywhere in the schema.

## Patch to the base schema
This page adds new object kinds, relations, and event families. The base event log, object envelope, frontier semantics, checkpoints, and linearizable control subset from [[moldable-operations-studio-schema-pass]] remain in force.

## Extended object kinds
Add these kinds wherever the base schema currently enumerates object kinds:

```yaml
object_kind +=
  identity_card |
  local_name_binding |
  capability_card |
  organization_context |
  credential |
  presentation |
  authorization_proof |
  evidence_receipt |
  observation_window |
  commitment |
  hypothesis_set |
  goal_hypothesis |
  dispute_case |
  remedy |
  policy_version
```

## Extended relation kinds
Add these relations wherever views or provenance queries enumerate relations:

```yaml
relation_kind +=
  named_by |
  publishes |
  attests_to |
  presented_as |
  authorized_by |
  governed_by |
  grounded_by |
  witnessed_by |
  contradicts |
  alternative_to |
  disambiguates |
  appeals |
  compensates |
  waives |
  releases |
  scoped_by |
  evaluated_under
```

## Sovereignty-aware common types

```yaml
principal_ref:
  principal_id: string
  principal_kind: human | agent | service | organization | coalition
  identity_card_id: string?

revocation_state:
  active | suspended | revoked | expired | superseded

grounding_state:
  presented | received | acknowledged | accepted | contested | withdrawn

hypothesis_state:
  candidate | active | superseded | rejected | expired

confidence_descriptor:
  semantics: posterior | ordinal_rank | bounded_confidence | qualitative
  value: number | string
  calibration_state: uncalibrated | estimated | validated
  model_ref: string
  observation_window_id: string

transparency_anchor:
  anchor_kind: key_log | issuer_log | status_list | merkle_root
  anchor_ref: string
  frontier: [event_id]?

policy_eval_result:
  allowed | denied | indeterminate
```

Notes:
- Where the base schema uses `actor_ref`, sovereignty-aware objects should use `principal_ref`.
- Existing `actor_ref` fields may be interpreted as an abbreviated `principal_ref` when no stronger identity data is available.

## Existing object patches

### `approval` extension
```yaml
approval +=
  policy_version_id: string?
  authorization_proof_id: string?
  evidence_receipt_ids: [string]
  related_case_id: string?
  evaluated_under_frontier: [event_id]?
```

### `artifact` extension
```yaml
artifact +=
  provenance_bundle_id: string?
  evidence_receipt_ids: [string]
  authorization_proof_id: string?
  verification_state: unverified | verified | disputed
  related_case_ids: [string]
```

### `authority_budget` extension
```yaml
authority_budget +=
  issued_via_presentation_id: string?
  policy_version_id: string?
  related_case_id: string?
```

## New object schemas

### `identity_card`
`identity_card` is the sovereign identity object for a principal.

```yaml
identity_card:
  object_id: string
  subject:
    stable_subject_id: string
    subject_kind: human | agent | service | organization
  self_certifying_handle: string
  verification_method_ids: [string]
  active_verification_method_id: string
  state: active | rotated | suspended | revoked
  rotation_epoch: integer
  rotated_from_identity_card_id: string?
  controller_ids: [string]
  service_endpoints:
    - endpoint_id: string
      transport: https | websocket | json_rpc | mcp | custom
      uri: string
  transparency_anchors: [transparency_anchor]
  valid_from: RFC3339 timestamp
  valid_until: RFC3339 timestamp?
```

Rules:
- `identity_card.revoked` is linearizable within a workspace or federation scope that relies on the card.
- Rotation creates a new `identity_card` linked by `rotated_from_identity_card_id`; it does not rewrite history.

### `local_name_binding`
`local_name_binding` stores a sovereign local name for a foreign identity.

```yaml
local_name_binding:
  object_id: string
  binder_identity_card_id: string
  local_name: string
  target_identity_card_id: string
  target_handle: string
  basis_refs: [object_ref]
  state: active | superseded | revoked
  valid_from: RFC3339 timestamp
  valid_until: RFC3339 timestamp?
  revoked_by: principal_ref?
```

### `capability_card`
`capability_card` advertises what a node can actually consume, emit, verify, and honor.

```yaml
capability_card:
  object_id: string
  subject_identity_card_id: string
  publication_state: draft | published | deprecated
  schema_versions: [integer]
  supported_object_kinds: [string]
  supported_event_kinds: [string]
  accepted_presentation_formats: [sd_jwt_vc, vc_jwt, ldp_vc, custom]
  accepted_proof_formats: [proof_carrying_auth, detached_signature, dsse, in_toto, custom]
  tool_classes: [string]
  approval_actions: [promote_branch, deploy, publish_view, grant_budget, change_policy]
  transport_endpoints: [string]
  can_issue_credentials: boolean
  can_verify_presentations: boolean
  can_participate_in_cases: boolean
  can_hold_authority_budget: boolean
  issued_at: RFC3339 timestamp
  expires_at: RFC3339 timestamp?
```

### `organization_context`
`organization_context` is the normative scope for commitments, policies, sanctions, and appeals. Use it for durable governance. Use `coalition` for temporary operational grouping.

```yaml
organization_context:
  object_id: string
  name: string
  state: active | suspended | dissolved
  member_identity_card_ids: [string]
  role_policy_version_ids: [string]
  sanction_authority_ids: [string]
  appeal_authority_ids: [string]
  local_namespace_root: string?
  membership_epoch: integer
```

### `credential`
`credential` is a portable attestation object.

```yaml
credential:
  object_id: string
  issuer_identity_card_id: string
  holder_identity_card_id: string?
  subject_ref: object_ref
  credential_type: role | membership | capability | budget_class | approval_authority | environment_class | custom
  claim_schema_uri: string
  claim_commitment_hash: string?
  disclosed_claim_paths: [string]
  caveats:
    audience_ids: [string]
    scope_refs: [object_ref]
    expiry: RFC3339 timestamp?
    attenuation_only: boolean
  proof_suite: string
  status_ref: string?
  valid_from: RFC3339 timestamp
  valid_until: RFC3339 timestamp?
  state: active | suspended | revoked | expired
```

Notes:
- `claim_commitment_hash` exists so the full claim set need not be exposed in every context.
- `disclosed_claim_paths` may be empty when the credential stores only a commitment and requires a later presentation to reveal claims.

### `presentation`
`presentation` is a selective disclosure of credential material for one interaction.

```yaml
presentation:
  object_id: string
  holder_identity_card_id: string
  audience_identity_card_id: string?
  derived_from_credential_ids: [string]
  disclosed_claim_paths: [string]
  predicate_claims: [string]
  challenge_nonce: string
  request_id: string?
  created_at: RFC3339 timestamp
  expires_at: RFC3339 timestamp?
  proof_suite: string
  status_snapshot_refs: [transparency_anchor]
  state: active | superseded | expired | revoked
```

Rule:
- A durable record of a `presentation` must not silently persist undisclosed claims. Otherwise selective disclosure becomes theater.

### `authorization_proof`
`authorization_proof` carries machine-checkable evidence that a requested action satisfies a local policy.

```yaml
authorization_proof:
  object_id: string
  requester_identity_card_id: string
  audience_identity_card_id: string
  requested_action: string
  subject_ref: object_ref
  policy_version_id: string
  presentation_ids: [string]
  credential_ids: [string]
  replay_nonce: string
  evaluated_frontier: [event_id]
  result: allowed | denied | indeterminate
  obligations: [string]
  generated_at: RFC3339 timestamp
  expires_at: RFC3339 timestamp?
  verifier_identity_card_id: string?
```

Rule:
- The proof must bind action, audience, policy version, nonce, and evaluated frontier. Otherwise one proof becomes a reusable charm against unrelated doors.

### `evidence_receipt`
`evidence_receipt` is the durable receipt object for observed facts and grounded acknowledgments.

```yaml
evidence_receipt:
  object_id: string
  receipt_kind: message | tool_output | artifact_observed | approval_seen | policy_notice | membership_notice | delivery | acknowledgment | contradiction | witness_statement
  subject_ref: object_ref
  source_event_id: string?
  observed_by: principal_ref
  counterparty_ref: principal_ref?
  content_hash: string
  storage_uri: string?
  witness_refs: [principal_ref]
  observation_frontier: [event_id]
  grounding_state: presented | received | acknowledged | accepted | contested | withdrawn
  invalidates_receipt_ids: [string]
  valid_from: RFC3339 timestamp
  valid_until: RFC3339 timestamp?
```

### `observation_window`
`observation_window` pins the evidence set used for an inference or a judgment.

```yaml
observation_window:
  object_id: string
  subject_ref: object_ref
  evidence_receipt_ids: [string]
  start_frontier: [event_id]
  end_frontier: [event_id]
  include_basis: string
  excluded_reason: string?
  redaction_markers: [string]
  created_by: principal_ref
  created_at: RFC3339 timestamp
```

### `commitment`
`commitment` is the first-class social obligation object.

```yaml
commitment:
  object_id: string
  debtor_ref: principal_ref
  creditor_ref: principal_ref
  context_ref: object_ref
  subject_ref: object_ref?
  antecedent: predicate_ast?
  consequent: predicate_ast?
  satisfaction_artifact_kinds: [string]
  deadline: RFC3339 timestamp?
  creation_basis_event_id: string
  grounding_receipt_ids: [string]
  lifecycle_state: proposed | created | detached | active | discharged | expired | violated | cancelled | released | delegated | assigned | compensated
  successor_commitment_id: string?
  supersedes_commitment_id: string?
  policy_version_id: string?
```

Notes:
- `detached` means the antecedent has fired and the commitment is now active against the consequent.
- `released` and `cancelled` must preserve history rather than deleting the commitment.

### `hypothesis_set`
`hypothesis_set` groups competing inferred goals over one observation window.

```yaml
hypothesis_set:
  object_id: string
  subject_ref: object_ref
  observation_window_id: string
  model_name: string
  model_version: string
  state: open | revised | expired | resolved
  generated_at: RFC3339 timestamp
  review_after: RFC3339 timestamp?
  expires_at: RFC3339 timestamp?
  competing_goal_hypothesis_ids: [string]
```

### `goal_hypothesis`
`goal_hypothesis` is one candidate inferred goal. It is never an observed fact.

```yaml
goal_hypothesis:
  object_id: string
  hypothesis_set_id: string
  candidate_goal_label: string
  candidate_goal_kind: task | policy_intent | coordination_intent | avoidance | unknown
  evidence_for_refs: [object_ref]
  evidence_against_refs: [object_ref]
  alternative_hypothesis_ids: [string]
  confidence:
    semantics: posterior | ordinal_rank | bounded_confidence | qualitative
    value: number | string
    calibration_state: uncalibrated | estimated | validated
    model_ref: string
    observation_window_id: string
  state: candidate | active | superseded | rejected | expired
  explanation_summary: string?
  disambiguation_needs:
    - need_id: string
      description: string
      satisfying_receipt_kinds: [string]
      expected_information_gain: number?
  asserted_by: principal_ref?
  valid_from: RFC3339 timestamp
  valid_until: RFC3339 timestamp?
  supersedes_goal_hypothesis_id: string?
```

### `dispute_case`
`dispute_case` holds contestation, waiver requests, and appeals.

```yaml
dispute_case:
  object_id: string
  case_kind: fact_dispute | interpretation_dispute | authority_dispute | policy_conflict | waiver_request | appeal
  opened_by: principal_ref
  target_refs: [object_ref]
  evidence_refs: [object_ref]
  counter_evidence_refs: [object_ref]
  related_commitment_ids: [string]
  requested_stay: boolean
  adjudicator_refs: [principal_ref]
  recusal_refs: [principal_ref]
  grounds: [factual_error, missing_notice, policy_conflict, emergency_override, disproportional_sanction, other]
  policy_version_id: string?
  state: open | under_review | stayed | waived | ruled | appealed | resolved | dismissed
  ruling_summary: string?
  ruling_event_id: string?
  remedy_ids: [string]
  filed_at: RFC3339 timestamp
  resolution_deadline: RFC3339 timestamp?
```

### `remedy`
`remedy` is the successor obligation or sanction created in response to a case or violation.

```yaml
remedy:
  object_id: string
  remedy_kind: compensate | redo | refund | investigate | apologize | narrow_scope | temporary_suspension | exoneration_note
  triggered_by_case_id: string
  target_commitment_id: string?
  debtor_ref: principal_ref?
  creditor_ref: principal_ref?
  due_at: RFC3339 timestamp?
  fulfills_or_compensates_commitment_id: string?
  state: proposed | active | fulfilled | failed | waived
```

### `policy_version`
`policy_version` is the durable governance rule object.

```yaml
policy_version:
  object_id: string
  policy_id: string
  version: integer
  jurisdiction_refs: [object_ref]
  rule_ast_hash: string?
  rule_storage_uri: string?
  proposer_ref: principal_ref
  enacted_by_event_id: string?
  supersedes_policy_version_id: string?
  effective_from: RFC3339 timestamp
  effective_until: RFC3339 timestamp?
  retroactivity: none | forward_only | bounded_migration
  review_after: RFC3339 timestamp?
  sunset_at: RFC3339 timestamp?
  accepted_issuer_identity_card_ids: [string]
  accepted_proof_formats: [string]
  appeal_rule_summary: string?
  sanction_rule_summary: string?
  migration_rule_summary: string?
  state: proposed | enacted | repealed | sunset | superseded
```

## Event families
Add the following minimum event types.

### Identity and attestations
- `identity_card.published`
- `identity_card.rotated`
- `identity_card.suspended`
- `identity_card.revoked`
- `local_name.bound`
- `local_name.superseded`
- `local_name.revoked`
- `capability_card.published`
- `capability_card.deprecated`
- `credential.issued`
- `credential.revoked`
- `presentation.submitted`
- `authorization_proof.recorded`

### Evidence and inference
- `evidence_receipt.recorded`
- `evidence_receipt.invalidated`
- `observation_window.created`
- `hypothesis_set.created`
- `goal_hypothesis.generated`
- `goal_hypothesis.revised`
- `goal_hypothesis.rejected`
- `goal_hypothesis.expired`
- `disambiguation.requested`

### Commitments and governance
- `commitment.proposed`
- `commitment.created`
- `commitment.detached`
- `commitment.discharged`
- `commitment.expired`
- `commitment.violated`
- `commitment.released`
- `commitment.delegated`
- `commitment.assigned`
- `commitment.compensated`
- `case.opened`
- `case.stayed`
- `case.ruled`
- `appeal.filed`
- `case.resolved`
- `remedy.created`
- `remedy.fulfilled`
- `policy.proposed`
- `policy.enacted`
- `policy.repealed`
- `policy.sunset`

## Linearizable subset additions
The minimum sovereignty-aware linearizable event set is:
- `identity_card.revoked`
- `credential.revoked`
- `approval.granted`
- `approval.rejected`
- `authority_budget.granted`
- `authority_budget.revoked`
- `case.ruled`
- `policy.enacted`
- `policy.repealed`
- `checkpoint.finalized`
- `branch.promoted`

Everything else may remain causal, provided the frontier and staleness are explicit.

## Explanation and inspection queries
A sovereignty-preserving ledger must support explanation queries directly from stored data.

Minimum query family:
- `why_goal_hypothesis(hypothesis_id)`
- `why_not_goal(subject_ref, candidate_goal_label, observation_window_id)`
- `evidence_for(ref)`
- `active_commitments(subject_ref)`
- `commitment_history(commitment_id)`
- `rights_at_time(subject_ref, requested_action, frontier)`
- `who_authorized(ref)`
- `what_policy_was_used(ref)`
- `open_cases(subject_ref | object_ref)`
- `what_changed(old_ref, new_ref)`

## Forbidden fields and shortcuts
The schema explicitly forbids the following fields as first-class control-plane concepts:
- `trust_score`
- `reputation_score`
- `moral_rank`
- `behavior_score`
- any hidden scalar that tries to summarize a subject globally across contexts

This does not forbid derived local risk heuristics inside one policy evaluator. It does forbid pretending such heuristics are the substrate of social truth.

## Minimal consistency rules for this layer
1. A revocation or ruling must dominate any later authorization or sanction that depends on it.
2. A `goal_hypothesis` must always cite an `observation_window_id` and at least one evidence reference.
3. A `presentation` without a matching audience/challenge/nonce binding is invalid for replay-sensitive actions.
4. A `commitment` may be violated, but violation alone does not imply expulsion or moral essence.
5. A waiver, release, or appeal must preserve the original history rather than rewriting it.
6. Subjects must be able to inspect the evidence, policy, and case history behind consequential claims affecting them.

## Acceptance criteria
A first serious sovereignty layer makes these statements true:
- A node can identify itself without depending on one central naming service.
- A verifier can accept or reject a request using local policy plus portable evidence.
- An artifact can carry its authorization and provenance context across boundaries.
- A work obligation can be represented as a commitment rather than a reputation score.
- A contested interpretation can open a case, cite evidence, and resolve through explicit governance.
- An inferred goal can be inspected as a hypothesis with alternatives, confidence semantics, and expiry.
- No surface needs to invent a scalar moral summary to answer operational questions.

## Suggested implementation order
1. Add `identity_card`, `capability_card`, and `local_name_binding`.
2. Add `credential`, `presentation`, and `authorization_proof`.
3. Add `evidence_receipt` and `observation_window`.
4. Add `commitment` and commitment lifecycle events.
5. Add `policy_version`, `dispute_case`, and `remedy`.
6. Add `hypothesis_set` and `goal_hypothesis`.
7. Add explanation queries and socially translucent UI surfaces.

This order is deliberate: own identity and evidence before inferring anything about intentions.

## Related pages
Read this with [[node-card-and-minimum-adapter-contract]], [[moldable-operations-studio-schema-pass]], [[sovereignty-and-observed-goals-ledgers-for-multiplayer-harnesses]], [[commitment-governance-semantics-for-multiplayer-harness]], [[multiplayer-agent-harnesses-and-p2p-networks]], [[how-to-build-a-multiplayer-harness-network]], and [[legacy-distributed-systems-ideas-for-moldable-operations-studio]].
