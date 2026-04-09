---
title: Probabilistic Epistemic Updates
created: 2026-04-08
updated: 2026-04-08
type: concept
tags: [epistemics, semantics, formal-methods]
sources: [raw/papers/arxiv-conradie-2016-probabilistic-epistemic-updates.md, raw/papers/arxiv-kishida-2017-categories-for-dynamic-epistemic-logic.md]
---

# Probabilistic Epistemic Updates

## Definition
Probabilistic epistemic updates study how knowledge, belief, and uncertainty change when new actions or observations arrive. The interesting question is not only what is true in the world, but how the agent-side state should evolve and how richer uncertain states can forget back to coarser ones without lying.

## What the new papers add
Conradie et al. treat probabilistic dynamic epistemic logic algebraically: updates are not mysterious narrative gestures but concrete transformations on associated algebras. Kishida pushes a complementary line: dynamic epistemic logic can be recast categorically, so an update is understood as movement inside a structured family of models rather than as a one-off mutation of a single state.

## Harness takeaway
This is unusually close to the current harness formalization work. The repo already distinguishes world facts from agent beliefs and now has a bounded-confidence refinement over the finite epistemic layer. The papers suggest three useful attitudes:
- keep world-side and agent-side update rules explicit
- treat forgetting as a structural map, not a pile of examples
- expect richer semantics to live in families of related models rather than one flat state space

That makes [[agent-harness-anatomy]] and [[memory-persistence]] look slightly different. Memory is not merely stored text; it is part of the evidence surface from which later belief states are derived. The relevant correctness question becomes whether richer epistemic states commute properly with the simpler quotient the harness already uses.

## Why this matters for current harness theory
A bounded-confidence layer is only interesting if it buys more than decorative numerics. The point is to distinguish traces that collapse to the same finite quotient while still carrying different confidence. These papers make that move respectable. They also support the instinct that the real theorem shape should be commuting forgetful maps rather than an ever-growing museum of representative examples.

## Open questions
- How far should a harness go toward genuine probabilistic epistemic logic rather than a modest thresholded credence layer?
- Is the next useful theorem categorical in spirit even if the implementation stays Lean-first and concrete?
- How should premature-completion taint interact with uncertain belief updates?
- What is the right boundary between [[formal-methods-for-agent-harnesses]] and the operational concerns in [[partial-order-trace-semantics]]?

## Related pages
Read this with [[agent-harness-anatomy]], [[memory-persistence]], [[formal-methods-for-agent-harnesses]], [[partial-order-trace-semantics]], and [[new-harness-design-notes]].
