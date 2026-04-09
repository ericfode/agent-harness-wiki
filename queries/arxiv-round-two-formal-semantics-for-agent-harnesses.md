---
title: "ArXiv Round Two: Formal Semantics for Agent Harnesses"
created: 2026-04-08
updated: 2026-04-09
type: query
tags: [survey, comparison, formal-methods, semantics]
sources: [raw/papers/arxiv-zhang-2024-formal-methods-trustworthy-ai-agents.md, raw/papers/arxiv-lahiri-2026-intent-formalization.md, raw/papers/arxiv-conradie-2016-probabilistic-epistemic-updates.md, raw/papers/arxiv-kishida-2017-categories-for-dynamic-epistemic-logic.md, raw/papers/arxiv-wang-2026-structural-operational-semantics-true-concurrency.md, raw/papers/arxiv-edixhoven-2022-branching-pomsets-for-choreographies.md]
---

# ArXiv Round Two: Formal Semantics for Agent Harnesses

## Goal
Re-run arXiv research with a sharper target: not generic “agent papers,” but mathematical ideas that can actually guide a formal theory of agent harnesses.

## What I was looking for
1. Formal methods that address the intent gap in AI coding systems.
2. Epistemic update machinery that can justify richer belief layers without discarding simpler quotients.
3. Partial-order or pomset semantics that treat concurrent and branching harness work honestly.

## Most relevant papers by thread

### 1. Formal methods for agentic coding
- **Zhang et al. (2024), _The Fusion of Large Language Models and Formal Methods for Trustworthy AI Agents_**
  - Best as a roadmap paper.
  - Main use: legitimizes the fusion of LLM flexibility with formal-method guarantees rather than treating them as opposing paradigms.
- **Lahiri (2026), _Intent Formalization_**
  - Best statement of the coding-agent problem.
  - Main use: reframes reliability as a specification problem, not merely a generation problem.

### 2. Epistemic and probabilistic updates
- **Conradie et al. (2016), _Probabilistic Epistemic Updates on Algebras_**
  - Most relevant to the current bounded-confidence direction.
  - Main use: updates as algebraic transformations, which is congenial to quotient maps and forgetful semantics.
- **Kishida (2017), _Categories for Dynamic Epistemic Logic_**
  - Best structural paper in this batch.
  - Main use: encourages thinking in families of related models and update maps, not isolated state mutations.

### 3. Partial-order traces and concurrency
- **Wang (2026), _Structural Operational Semantics for True Concurrency_**
  - Best direct bridge from ordinary SOS to true-concurrency semantics.
  - Main use: suggests a path from serial event traces to pomset-like harness transitions.
- **Edixhoven et al. (2022), _Branching Pomsets for Choreographies_**
  - Best paper here for multi-agent coordination with explicit branching.
  - Main use: shows that concurrency alone is insufficient; choices need compact semantic representation too.

## Provisional synthesis
The most promising shape for a harness theory now looks like this:
- use [[formal-methods-for-agent-harnesses]] to define what the system is trying to satisfy
- use [[probabilistic-epistemic-updates]] to model what the agent and the world can justify while preserving forgetful quotients
- use [[partial-order-trace-semantics]] to model how work can proceed concurrently or branch under orchestration

That is much cleaner than trying to squeeze every concern into one giant state machine. It suggests a tower of related semantics rather than a single overburdened object.

## What seems most actionable for the current repo
1. Treat intent surfaces and acceptance checks as first-class formal objects, not just review habits.
2. Keep pushing on commuting forgetful maps between richer epistemic layers and simpler quotients.
3. Treat the current scheduler layer as a coarse shadow of a future partial-order trace semantics.
4. Resist fake Bayesian grandeur: modest bounded-confidence layers are acceptable if their quotient behaviour is explicit and useful.

## What I would read next
- More on dynamic / probabilistic epistemic logic with explicit update operators.
- More on event structures and realizability conditions for choreographies.
- More on specification validation and user-in-the-loop intent formalization for coding agents.

## Related pages
This note distills into [[formal-methods-for-agent-harnesses]], [[probabilistic-epistemic-updates]], and [[partial-order-trace-semantics]], and it should be read beside [[new-harness-design-notes]] and [[harness-engineering]].
