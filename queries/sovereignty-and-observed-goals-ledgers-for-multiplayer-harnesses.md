---
title: Sovereignty and Observed-Goals Ledgers for Multiplayer Harnesses
created: 2026-04-10
updated: 2026-04-10
type: query
tags: [survey, orchestration, semantics, work-management, memory]
sources: [queries/multiplayer-agent-harnesses-and-p2p-networks.md, queries/how-to-build-a-multiplayer-harness-network.md, queries/moldable-operations-studio-schema-pass.md, queries/legacy-distributed-systems-ideas-for-moldable-operations-studio.md, raw/articles/w3c-verifiable-credentials-data-model-v2.md, raw/papers/li-mitchell-winsborough-role-based-trust-management-framework.md, raw/papers/bauer-schneider-felten-appel-proof-carrying-authorization.md, raw/papers/claimchain.md, raw/papers/torres-arias-2019-in-toto.md, raw/articles/w3c-prov-dm.md, raw/papers/medina-mora-winograd-flores-flores-action-workflow-approach.md, raw/papers/fornara-colombetti-commitment-based-agent-communication-language.md, raw/papers/singh-chopra-computational-governance-violable-contracts.md, raw/papers/keren-gal-karpas-goal-recognition-design.md, raw/papers/ramirez-geffner-probabilistic-plan-recognition.md, raw/papers/erickson-et-al-socially-translucent-systems.md, raw/articles/self-certifying-file-system.md, raw/articles/rivest-lampson-1996-sdsi.md, raw/papers/birgisson-et-al-2014-macaroons.md, raw/articles/rfc-9420-mls-protocol.md, raw/papers/efstathopoulos-et-al-2005-asbestos.md, raw/articles/local-first-software.md]
---

# Sovereignty and Observed-Goals Ledgers for Multiplayer Harnesses

## Question
If sovereignty is a first-class requirement, what should replace a simplistic reputation system in a multiplayer harness? In particular, what would it mean to keep a durable log of observed goals rather than a good/bad score?

## Short answer
Replace scalar reputation with a sovereignty-preserving ledger composed of:
1. sovereign identity and local naming
2. portable attestations and local policy evaluation
3. signed provenance receipts
4. explicit commitments and governance state
5. inferred goal hypotheses with evidence and expiration
6. socially translucent multiplayer surfaces

The crucial move is this: the system should not ask "is this participant good?" It should ask:
- what did they declare?
- what commitments did they accept?
- what evidence exists?
- what did observers infer, with what confidence?
- what happened afterward?
- under whose policy is this action acceptable?

That is a much healthier question, and also a more truthful one.

## Why scalar reputation is the wrong abstraction
A scalar reputation score collapses too many different things:
- competence
- honesty
- alignment
- reliability
- authority
- conflict history
- context-specific skill
- governance disputes
- temporary failure
- principled refusal

The literature found in this deep-dive points in a different direction. Trustworthy multiplayer systems work better when they preserve structured social facts rather than compressing people into one number. [[erickson-et-al-socially-translucent-systems]] is the HCI version of this point. [[li-mitchell-winsborough-role-based-trust-management-framework]] and [[bauer-schneider-felten-appel-proof-carrying-authorization]] are the authorization version. [[fornara-colombetti-commitment-based-agent-communication-language]] and [[singh-chopra-computational-governance-violable-contracts]] are the protocol and governance version.

## Round 1 result: the strongest research clusters
The broad pass converged on three source families.

### A. Sovereign identity and portable attestation
The strongest line here is:
- [[rivest-lampson-1996-sdsi]]
- [[self-certifying-file-system]]
- [[w3c-verifiable-credentials-data-model-v2]]
- [[li-mitchell-winsborough-role-based-trust-management-framework]]
- [[bauer-schneider-felten-appel-proof-carrying-authorization]]
- [[claimchain]]
- [[torres-arias-2019-in-toto]]
- [[birgisson-et-al-2014-macaroons]]

The common lesson is that identity should be sovereign, authorization should be policy-evaluated, and important actions should carry evidence rather than asking for ambient trust.

### B. Provenance, commitments, and goal hypotheses
The strongest line here is:
- [[w3c-prov-dm]]
- [[medina-mora-winograd-flores-flores-action-workflow-approach]]
- [[fornara-colombetti-commitment-based-agent-communication-language]]
- [[singh-chopra-computational-governance-violable-contracts]]
- [[ramirez-geffner-probabilistic-plan-recognition]]
- [[keren-gal-karpas-goal-recognition-design]]

The common lesson is that the system should separately represent:
- observed facts
- declared commitments
- inferred goals
- outcomes and remedies

If those are collapsed, the ledger becomes manipulative very quickly.

### C. Human-facing accountability without moral scoring
The strongest line here is:
- [[erickson-et-al-socially-translucent-systems]]
- [[local-first-software]]
- [[rfc-9420-mls-protocol]]
- [[efstathopoulos-et-al-2005-asbestos]]

The common lesson is that collaboration works better when people can see relevant activity, retain local agency, and rely on scoped compartments and explicit epochs, rather than being silently judged by hidden systems.

## Round 2 result: what the ledger should actually contain
The targeted pass sharpens the design considerably.

## 1. Identity layer: sovereign and locally named
The identity substrate should follow the spirit of [[rivest-lampson-1996-sdsi]] and [[self-certifying-file-system]].

### Required primitives
- `node_id`
  - self-certifying key-derived identifier
- `local_name_binding`
  - "my name for this foreign node"
- `membership_epoch`
  - current coalition/workspace/security epoch
- `capability_card`
  - what this node can actually do

### Design rule
Do not force one flattening global actor identity. A multiplayer harness should support linked local names and scoped memberships.

## 2. Attestation layer: portable claims, local policy
The attestation substrate should follow [[w3c-verifiable-credentials-data-model-v2]], [[li-mitchell-winsborough-role-based-trust-management-framework]], [[bauer-schneider-felten-appel-proof-carrying-authorization]], and [[birgisson-et-al-2014-macaroons]].

### Required primitives
- `credential`
  - role, membership, budget class, environment class, review authority
- `presentation`
  - selectively disclosed claims for a specific interaction
- `policy_rule`
  - local acceptance logic
- `authorization_proof`
  - machine-checkable evidence that a request satisfies policy
- `revocation_status`
  - current validity and suspension state

### Design rule
The verifier remains sovereign. A credential does not force trust; it only carries evidence that local policy may accept.

## 3. Provenance layer: receipts before interpretations
The substrate here is [[w3c-prov-dm]] plus the artifact lineage logic of [[torres-arias-2019-in-toto]].

### Required primitives
- `evidence_receipt`
  - user message, tool result, file change, approval, review, artifact emission
- `artifact_provenance_bundle`
  - signed lineage attached to important outputs
- `observation_window`
  - the evidence set used for a particular inference or review
- `revision_edge`
  - what superseded or invalidated what

### Design rule
The system must keep raw evidence and provenance separate from later interpretation. Otherwise the newest story overwrites the past, which is efficient and barbaric.

## 4. Commitment layer: the real non-score social substrate
This is where [[medina-mora-winograd-flores-flores-action-workflow-approach]], [[fornara-colombetti-commitment-based-agent-communication-language]], and [[singh-chopra-computational-governance-violable-contracts]] become central. The more concrete semantic extraction from this lane now lives in [[commitment-governance-semantics-for-multiplayer-harness]].

### Required primitives
- `commitment`
  - debtor, creditor, scope, antecedent, consequent, deadline
- `commitment_event`
  - create, acknowledge, accept, delegate, assign, discharge, cancel, release, expire, violate, compensate
- `waiver`
  - authorized release or exception
- `remedy`
  - compensating commitment after violation
- `dispute_case`
  - challenge to facts, interpretation, or rule application

### Design rule
Represent obligation, release, breach, and remedy explicitly. Do not turn a missed obligation into a hidden score decrement.

## 5. Goal-hypothesis layer: observed goals, not mind-reading
The observed-goals part of the system should follow [[ramirez-geffner-probabilistic-plan-recognition]] and [[keren-gal-karpas-goal-recognition-design]].

### Required primitives
- `hypothesis_set`
  - competing candidate goals for one observation window
- `goal_hypothesis`
  - candidate goal, evidence, model, confidence semantics, alternatives
- `disambiguation_need`
  - what evidence would reduce ambiguity
- `expiration_policy`
  - when a hypothesis becomes stale or must be revised

### Design rule
Inferred goals are hypotheses, not facts. They should always be:
- evidence-linked
- revisionable
- contestable
- expiring
- accompanied by alternatives when ambiguity remains live

## 6. Governance layer: procedural justice, not reputation theater
This is the main lesson from [[singh-chopra-computational-governance-violable-contracts]] together with the broader governance tradition already reflected in the wiki.

### Required primitives
- `policy_proposal`
- `policy_version`
- `appeal`
- `ruling`
- `sanction`
- `recusal`
- `monitoring_rule`
- `organization_context`

### Design rule
Governance must itself be on-ledger. If the system can sanction, revoke, or downgrade participants, the grounds, authority, and remedy path must be explicit and inspectable.

## 7. Human surface layer: socially translucent, not surveillance-heavy
The UI principle comes from [[erickson-et-al-socially-translucent-systems]].

The right surface shows:
- what commitments are active
- which evidence grounds them
- which goals are inferred rather than declared
- who has acknowledged what
- what remains ambiguous
- which rule or credential authorized an action
- how to contest, appeal, or annotate a record

The wrong surface shows:
- a leader board
- a hidden trust score
- one definitive claim about what someone "really wants"
- a persuasive but uncheckable summary

## What the ledger should log directly
These should be durable first-class events and objects, not derived impressions.

### Directly logged
- identity and key bindings
- credentials and presentations
- requests, offers, promises, acknowledgments, acceptances
- approvals, rejections, waivers, revocations
- artifact creation and review
- evidence receipts and provenance links
- policy proposals and rulings
- disputes, remedies, and appeals

### Derived but queryable
- whether a commitment is active, satisfied, expired, violated, or compensated
- whether a requested action satisfies local policy
- current candidate goals for an actor or object
- ambiguity status and disambiguating evidence needed
- risk flags grounded in explicit rule conditions

## What the ledger must never do
- Never store inferred goals as if they were observed facts.
- Never collapse role, trust, competence, and conflict history into one scalar reputation.
- Never let a hidden model decide authority without exposing evidence and policy.
- Never overwrite old interpretations instead of revising them with lineage.
- Never make participation legible only to central administrators; the subject should be able to inspect and contest the record.
- Never treat violation as moral essence. It is a governed event with context, not a metaphysical verdict.

## The key replacement formula
The strongest replacement for reputation is:

`trace + commitments + capabilities + policy + hypotheses + remedies`

Or in plainer language:
- what happened
- what was promised
- what was allowed
- how it was judged
- what was inferred
- what happened when things went wrong

That is richer, fairer, and much harder to game with aesthetics alone.

## Suggested control-plane objects
The concrete schema patch for this layer now lives in [[sovereign-identity-and-observed-goals-schema-pass]].

If this were added to [[moldable-operations-studio-schema-pass]], the most natural new or refined objects would be:
- `identity_card`
- `credential`
- `presentation`
- `authorization_proof`
- `evidence_receipt`
- `commitment`
- `hypothesis_set`
- `goal_hypothesis`
- `dispute_case`
- `remedy`
- `policy_version`

The current objects such as `approval`, `artifact`, `trace`, and `authority_budget` still belong. They simply gain a more explicit sovereignty and governance layer around them.

## Recommended build order
1. Add sovereign identity and capability cards to the node model.
2. Add provenance receipts and artifact provenance bundles.
3. Add commitment objects and commitment lifecycle transitions.
4. Add policy-evaluated credentials and proof-carrying authorization for sensitive actions.
5. Add goal-hypothesis sets as explicit, expiring, evidence-backed inferences.
6. Add dispute, waiver, remedy, and appeal objects.
7. Add socially translucent surfaces that let participants inspect and contest all of the above.

This is the correct order because people should first own identity and evidence before the system starts inferring anything about their goals.

## Bottom line
If sovereignty matters, the answer is not a kinder reputation score. The answer is a structured, queryable, contestable ledger that distinguishes identity, evidence, commitments, inferences, and governance.

That gives you a system that can say:
- here is what we observed
- here is what was promised
- here is what we infer, tentatively
- here is who authorized it
- here is how to challenge it

That is a much more civilized basis for human-plus-agent collaboration.

## Related pages
Read this with [[sovereign-identity-and-observed-goals-schema-pass]], [[commitment-governance-semantics-for-multiplayer-harness]], [[multiplayer-agent-harnesses-and-p2p-networks]], [[how-to-build-a-multiplayer-harness-network]], [[moldable-operations-studio-schema-pass]], [[legacy-distributed-systems-ideas-for-moldable-operations-studio]], [[grounding-moldable-operations-studio-ideas-in-real-research]], and [[high-impact-artifacts-for-multiplayer-harness-design]].
