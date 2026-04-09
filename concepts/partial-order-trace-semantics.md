---
title: Partial-Order Trace Semantics
created: 2026-04-08
updated: 2026-04-08
type: concept
tags: [concurrency, semantics, work-management]
sources: [raw/papers/arxiv-wang-2026-structural-operational-semantics-true-concurrency.md, raw/papers/arxiv-edixhoven-2022-branching-pomsets-for-choreographies.md]
---

# Partial-Order Trace Semantics

## Definition
Partial-order trace semantics treats a run not as one total sequence of events, but as a structure in which some events are causally ordered, some are concurrent, and some represent branching choice. For agent harnesses, this matters whenever parallel subwork, review gates, or multi-agent coordination are collapsed into a mere list of turns.

## What the new papers add
Wang argues that structural operational semantics can be extended from ordinary labelled transition systems to pomset-style transitions, so the semantic unit becomes a partially ordered multiset of actions rather than one token at a time. Edixhoven et al. add the other half of the problem: concurrency alone is not enough, because choices also need compact representation. Their branching pomsets encode both partial order and branching behaviour for multi-agent choreographies.

## Harness takeaway
The harness analogue is straightforward:
- subagents and teams create concurrent work, not just longer transcripts
- review and approval introduce causal barriers
- delegation choices create branches, not only longer serial histories
- critical-path reasoning is therefore better expressed over dependency structure than over raw event count

This sits directly beside [[orchestration-topologies]], [[work-management-primitives]], and [[automation-and-background-work]]. A work graph is already an admission that the transcript is not the right semantic object.

## Why this matters for current harness theory
A scheduler lower bound is a good first move, but it is still only a scalar shadow of a richer object. The next serious step would be to treat harness traces as partial orders or pomset-like structures, from which critical path, branching, and realizability properties can be derived. That would make the current scheduler layer look like a coarse quotient rather than an isolated trick.

## Open questions
- Which harness events should remain atomic, and which should be grouped into a concurrent action set?
- Is pomset structure enough, or do harness traces eventually want full event structures?
- How should branching for retries, evaluator disagreement, or tool failure be represented?
- How should this layer interact with [[formal-methods-for-agent-harnesses]] and [[probabilistic-epistemic-updates]]?

## Related pages
Read this with [[orchestration-topologies]], [[work-management-primitives]], [[automation-and-background-work]], [[formal-methods-for-agent-harnesses]], [[probabilistic-epistemic-updates]], and [[new-harness-design-notes]].
