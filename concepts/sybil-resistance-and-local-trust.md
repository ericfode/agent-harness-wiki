---
title: Sybil Resistance and Local Trust
created: 2026-04-11
updated: 2026-04-11
type: concept
tags: [semantics, safety, orchestration]
sources: [raw/papers/cheng-friedman-2005-sybilproof-reputation-mechanisms.md, queries/sovereignty-and-observed-goals-ledgers-for-multiplayer-harnesses.md, queries/commitment-governance-semantics-for-multiplayer-harness.md, queries/multiplayer-agent-harnesses-and-p2p-networks.md]
---

# Sybil Resistance and Local Trust

## Definition
Sybil resistance is the requirement that a trust or coordination mechanism not become trivially gameable when participants can mint cheap new identities. In a harness context, the practical lesson is that trust should stay local, directional, and evidence-backed rather than collapsing into a symmetric global reputation score.

## Core result
Cheng and Friedman show in _Sybilproof reputation mechanisms_ that there is no symmetric sybilproof reputation function in the static-graph setting. Once identity creation is cheap, a uniform actor-wide score can be inflated by spawning cooperating identities and manufacturing supportive edges.

That result matters directly for multiplayer harness design. If the system wants sovereign participants, portable identity, and low-friction federation, it should not pretend that one scalar score will remain honest under strategic identity splitting.

## Harness implications
### 1. Trust must be directional or observer-relative
If trust propagates at all, it should be computed from bounded paths, endorsements, or local policy contexts rather than from one globally shared number. This is the governance-side complement to the identity work in [[sovereignty-and-observed-goals-ledgers-for-multiplayer-harnesses]].

### 2. Identity should be sovereign, not centrally flattened
Self-certifying or locally named identities make it easier to keep trust anchored in explicit relationships and evidence. That is why the concrete object model in [[sovereign-identity-and-observed-goals-schema-pass]] centers identity cards, local name bindings, credentials, presentations, and authorization proofs instead of a universal score field.

### 3. Authority should come from evidence and policy
A participant should be able to ask not "what is this node's reputation?" but "what evidence does this action carry, and under whose policy is it acceptable?" This aligns with the commitment- and case-oriented design in [[commitment-governance-semantics-for-multiplayer-harness]].

### 4. Federation gets safer when trust stays local
A network of harnesses can exchange capabilities, credentials, and provenance without requiring universal agreement about who is globally trustworthy. That design direction already appears in [[multiplayer-agent-harnesses-and-p2p-networks]] and becomes much more defensible once the anti-sybil constraint is stated explicitly.

## Design rules
- Do not store a universal `reputation_score` and then politely rename it later.
- Prefer attestations, provenance receipts, commitments, and policy checks over actor-wide moral summaries.
- Treat endorsements as scoped edges with lineage, not as permanent essence.
- Make risk judgments contestable and revisionable.
- Keep historical violations as governed facts and cases, not as mystical score residue.

## What this does not mean
Sybil resistance does not require distrust of everyone forever. It means the system should represent trust in a form that survives strategic identity creation:
- local naming rather than universal naming
- policy evaluation rather than ambient authority
- evidence bundles rather than vibes
- commitments and remedies rather than silent score decay

## Related pages
Read this with [[sovereignty-and-observed-goals-ledgers-for-multiplayer-harnesses]], [[sovereign-identity-and-observed-goals-schema-pass]], [[commitment-governance-semantics-for-multiplayer-harness]], and [[multiplayer-agent-harnesses-and-p2p-networks]].
