---
title: "another-harness model/docs drift checker"
created: 2026-04-11
updated: 2026-04-11
type: query
tags: [formal-methods, semantics, work-management]
sources: [raw/articles/another-harness-model-docs-drift-check-2026-04-11.md, raw/articles/another-harness-repo-2026-04-09.md]
---

# another-harness model/docs drift checker

## Question
What is the first honest way for `another-harness` to check that its explanatory markdown still matches the Lean model, without embarking on a doomed campaign to compare every doc to every theorem?

## Short answer
Pick one high-value contract and fence that, not the whole republic.

The repo's first chosen contract is the attempt-vs-stream grounding distinction:
- retries preserve stream identity while changing attempt identity
- stream history can retain historical support and evidence of a grounded attempt
- a restarted attempt on that same stream can still remain ungrounded

That is exactly the sort of subtle asymmetry that docs enjoy flattening when nobody is watching.

## Why this contract first
It is a good first target because the repo already leans on it repeatedly when explaining:
- why retries are not the same as one long task
- why stream continuity does not license attempt-local completion claims
- why builder/evaluator/handoff artifacts stay separate instead of collapsing into one triumphant status bit

In other words, this is not a random formal nicety. It is one of the repo's active explanatory load-bearing walls.

## What the checker actually does
The new checker in the repo verifies that:
1. the Lean model still contains the core attempt/stream vocabulary and restart behavior
2. the refinement surface still exposes stream-historical and stream-grounded-attempt predicates distinctly from attempt-local grounded completion
3. the restart-aware theory still contains witnesses for the intended asymmetry
4. the main explanatory docs still say the same thing in prose

The implementation is intentionally narrow. It strips Lean comments and string literals before matching so dead quoted text cannot counterfeit agreement, but it still does not attempt semantic equivalence between markdown and proofs.

## Why this is a good harness move
This is a satisfying example of formal methods doing practical harness work.

The repo does not merely have Lean for prestige or post-hoc demonstrations. It uses Lean as the canonical surface for a real explanatory invariant, then adds a cheap executable checker that fails when the prose drifts away from the model.

That is exactly the right size of machinery for a repo that wants rigor without building a second bureaucracy to celebrate it.

## Limits
The checker does not prove that the docs are complete, elegant, or pedagogically ideal.
It only proves that they still say the same essential thing as the model on one chosen contract.

That limitation is a virtue. A narrow honest fence is better than a grand fake map.

## Bottom line
`another-harness` now has a first genuine docs/model drift checker, and the contract it chose is not arbitrary. It protects one of the formal distinctions the repo uses to explain runtime, evaluation, and retry behavior without lying to itself about what completion means.

## Related pages
Read this with [[another-harness-and-atropos]], [[formal-methods-for-agent-harnesses]], [[theorem-proving-as-cognitive-kernel]], [[formal-cognition-loop]], and [[evaluation-and-review-loops]].
