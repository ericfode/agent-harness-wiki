---
title: "Commitment and Governance Semantics for a Sovereignty-Preserving Multiplayer Harness"
created: 2026-04-10
updated: 2026-04-10
type: query
tags: [survey, orchestration, semantics, work-management]
sources: [queries/multiplayer-agent-harnesses-and-p2p-networks.md]
---

# Commitment and Governance Semantics for a Sovereignty-Preserving Multiplayer Harness

## Short answer
If you want a serious alternative to scalar reputation, the best substrate is a commitment ledger plus explicit governance. The harness should log public facts, infer commitment state from those facts, allow commitments to be violated, and route violations into organizational procedures rather than into hidden trust scores.

## Ranked sources

### 1. Yolum and Singh (2002), _Commitment Machines_
Why it matters:
- Best core semantic model for treating coordination as social commitments instead of message order.
- Gives the minimum commitment object and the canonical operations over it.

Directly useful primitives:
- `commitment(debtor, creditor, context_group, condition)`
- `base_commitment` versus `metacommitment`
- operations: `create`, `discharge`, `cancel`, `release`, `assign`, `delegate`
- `context_group` as the organizational scope for compliance and dispute resolution

Harness implication:
- Model protocol progress as changes to commitments, not just message transcripts.
- Keep the organizational context explicit because that is where waiver, release, and adjudication live.

### 2. Mallya and Singh (2005), _Modeling Exceptions via Commitment Protocols_
Why it matters:
- Strongest source here on how commitments interact with exceptions.
- Makes violations and exception-handling first-class instead of treating them as protocol crashes.

Directly useful primitives:
- a protocol run is a sequence of states with evolving commitments
- `expected_exception` and `unexpected_exception`
- preferences over runs, so some deviations are less preferred but still governable
- dynamically attachable exception handlers / compensation handlers
- explicit notion that violation detection is separate from commitment operations

Harness implication:
- Do not treat all deviations as failure.
- Represent recovery, compensation, and negotiated replacement as normal semantic moves.

### 3. King, Gunay, Chopra, and Singh (2017), _Tosca: Operationalizing Commitments Over Information Protocols_
Why it matters:
- Best operational bridge from declarative commitments to decentralized enactment.
- Sharpest source on what to log versus what to infer.

Directly useful primitives:
- log message / event facts only
- infer lifecycle events from the event history
- lifecycle events: `create`, `detach`, `discharge`, `expire`, `violate`
- commitment alignment: different parties must be able to make compatible inferences from decentralized histories
- forwarding / notification messages synthesized specifically to repair misalignment

Harness implication:
- The ledger should record observable facts, not mutable obligation state as the primary truth.
- Commitment state should be derived from the fact history.
- If a participant may not observe the same facts, the harness needs explicit alignment events or receipts.

### 4. Singh and Chopra (2020), _Computational Governance and Violable Contracts for Blockchain Applications_
Why it matters:
- Best argument for why commitments must remain violable and how governance fits around them.
- Introduces the compact / organization split that maps well to a multiplayer harness.

Directly useful primitives:
- `compact` as declarative agreement among principals
- `organization` as the context that governs the compact
- norms such as commitments and prohibitions
- `public record of events` for verifiability
- sanctions as follow-on commitments by the organization when a norm is violated

Harness implication:
- A harness should never try to regiment every action.
- It should record exogenous facts, compute whether norms were satisfied or violated, and then activate governance commitments such as investigate / remediate / compensate.

### 5. Zhang, Hugh, and Bernstein (2020), _PolicyKit: Building Governance in Online Communities_
Why it matters:
- Most actionable source for executable governance workflows.
- Shows how everyday actions and constitutional changes can use the same policy engine.

Directly useful primitives:
- `platform_action` versus `constitution_action`
- `policy` with action scope and decision procedure
- `proposal` object with statuses including `PROPOSED`, `PASSED`, `FAILED`
- voters / jurors / stages / datetime triggers
- auditability and reversibility of bad policies

Harness implication:
- Governance should itself be programmable and amendable.
- Meta-governance is essential: the harness needs rules for changing the rules.

### 6. Context sources: Action Workflow, Common Information Spaces, and Ostrom
Why they matter:
- Action Workflow gives a very usable conversational loop: proposal, agreement, performance, satisfaction.
- Common Information Spaces gives the CSCW warning that “shared state” is never free: making information common and interpreting it both require work.
- Ostrom is the strongest governance sanity check even though it is less semantically precise than the commitment papers: keep boundaries clear, monitoring explicit, sanctions graduated, conflict-resolution cheap, and rule changes participatory.

Harness implication:
- Good human/agent UX should expose commitment loops in conversational form.
- Do not assume a globally shared ledger automatically yields common understanding.
- Use Ostrom-style design principles to evaluate whether a policy layer will stay governable without collapsing into either central admin fiat or scalar reputation.

## Concrete primitives the harness should implement

### Core ledger objects
- `event`: immutable observed fact, with actor, timestamp, causal parents, witnesses / attesters, and artifact references
- `commitment`: debtor, creditor, context, subject, antecedent, consequent, deadline, creation basis
- `norm`: commitment, prohibition, permission, sanction commitment
- `policy`: scope, proposer, decision procedure, electorate / jury rule, quorum / threshold, trigger, sunset / review rule
- `case`: dispute / appeal / waiver / exception-handling object linked to events and commitments
- `organization`: membership, roles, authority to release / waive / sanction / adjudicate

### Derived semantic fields
- `lifecycle_state`: proposed, created, detached, active, discharged, expired, violated, cancelled, released, delegated, assigned, compensated
- `alignment_state`: aligned, locally inferred, disputed_due_to_observation_gap
- `governance_state`: open, under_review, stayed, waived, remedied, sanctioned, appealed, resolved

### Essential transitions
- proposal -> agreement -> performance claim -> satisfaction acknowledgment
- created -> detached when antecedent is met
- detached -> discharged when consequent is met
- created -> expired when antecedent deadline passes unmet
- detached -> violated when consequent deadline passes unmet
- active -> cancelled or released by authorized act
- active -> delegated or assigned with traceable successor commitment
- violated -> case opened -> investigate -> remedy / compensate / sanction / exonerate -> close
- policy proposed -> deliberated -> passed / failed -> enacted
- policy enacted -> amended / repealed / sunset via constitution action

## What to log versus what to infer

### Log directly
- observable messages and world events
- artifact submissions, deliveries, payments, approvals, refusals, withdrawals
- who observed or attested what
- deadlines, declared conditions of satisfaction, and explicit waivers/releases
- policy proposals, votes, jury selections, rulings, amendments
- case filings, evidence attachments, recusal, decisions, remedies

### Infer from logs
- whether a commitment was created, detached, discharged, expired, or violated
- whether different parties should be aligned or are misaligned
- whether a prohibition was violated
- whether a sanction commitment became active
- whether a case should auto-open because a violation condition fired
- whether a deadline extension or waiver supersedes a default violation

## Violation, dispute, appeal, waiver

### Violation
- Violation is not the same as expulsion or bad reputation.
- It is a computed state saying: given the public record and current rules, an obligation was not satisfied in time or a prohibition was breached.

### Dispute
- A dispute can challenge facts, correlation, interpretation, authority, or applicability of a rule.
- The case object should support evidence, counter-evidence, witness attestations, and status transitions.

### Appeal
- Appeals should target a specific ruling or sanction, with deadlines and allowed grounds.
- Appeals are governance actions, not informal chat.
- Important grounds: factual error, misalignment / missing notice, policy conflict, emergency override, disproportional sanction.

### Waiver / release
- Waiver should be an explicit authorized act that changes future inference.
- The creditor or context organization may release a debtor.
- Waiver should preserve the original obligation in history while marking it as superseded or forgiven rather than silently deleting it.

### Compensation / remedy
- If violation occurs, the default next move should often be a compensating commitment, not a trust score reduction.
- Examples: redo work, refund, provide substitute artifact, investigate, or accept a narrower completion condition.

## Governance design without scalar reputation
- Prefer role- and event-based authority over global scores.
- Decide access by explicit delegation, policy, and case history, not by a hidden reputation number.
- Use bounded local memory: past violations matter insofar as they trigger explicit policy predicates or escalation rules, not because they accumulate into an opaque score.
- Keep constitutional governance separate from operational commitments, but connect them through the same event ledger.
- Let the organization itself be a party that can hold sanction or remediation commitments.

## Cautions
1. Do not collapse inferred commitment state into the primary stored truth; store facts first.
2. Do not assume everyone observed the same events; alignment is a separate problem.
3. Do not make violation impossible; real autonomy requires violability plus governance.
4. Do not replace reputation with an equally opaque “risk score.”
5. Do not let policy changes retroactively rewrite prior facts without explicit migration semantics.
6. Do not ignore the cost of making information common; interpretation work and evidence curation need dedicated objects.
7. Do not let exception-handling stay off-ledger; waivers, extensions, and compensations must be first-class.

## Recommended harness minimum
1. Immutable event ledger with attestations and causal links.
2. Commitment engine deriving lifecycle state from events.
3. Case system for disputes, appeals, waivers, and remedies.
4. Policy engine for operational and constitutional governance.
5. Alignment mechanisms: receipts, forwards, or witness events when parties may have asymmetric visibility.
6. Organization object that can hold sanction and adjudication commitments.

## Related pages
Read this with [[sovereignty-and-observed-goals-ledgers-for-multiplayer-harnesses]], [[multiplayer-agent-harnesses-and-p2p-networks]], [[how-to-build-a-multiplayer-harness-network]], [[moldable-operations-studio-schema-pass]], and [[non-hierarchical-agent-orchestration]].
