---
title: Formal-Core Agent Architecture
created: 2026-04-08
updated: 2026-04-08
type: query
tags: [survey, formal-methods, semantics]
sources: [raw/papers/arxiv-song-2024-lean-copilot.md, raw/papers/arxiv-endres-2023-natural-language-to-postconditions.md, raw/papers/arxiv-murphy-2024-llm-codegen-formal-spec-reactive-synthesis.md, raw/papers/arxiv-lin-2024-fvel.md, raw/papers/arxiv-burigana-2026-epddl.md, raw/papers/arxiv-allen-2025-sound-complete-neurosymbolic-reasoning.md, raw/papers/arxiv-lahiri-2026-intent-formalization.md]
---

# Formal-Core Agent Architecture

## Question
What would it mean to put formal methods at the core of an agent's cognition, so that it tries to transform problems into formal space, solve them there, and then transform the result back into the best implementation space?

## Short answer
The most credible architecture is not “one theorem prover for everything,” but a **formal-core loop** with multiple admissible formal spaces and a strict refinement discipline.

## Proposed architecture

### 1. Formalization gate
Every serious task first passes through a gate that asks:
- what is the object here: theorem, contract, constraint system, plan, protocol, type-level transformation?
- what facts are trusted inputs, and which are hypotheses to be checked?
- what would count as a witness or certificate of success?

### 2. Solver selection by semantic fit
- **Lean / Isabelle / Coq style proof kernel** for invariants, structural refinement, algebraic reasoning, and certified transformations.
- **SMT / constraint solving** for satisfiability, admissibility, policy checks, and bounded search.
- **Reactive or DSL synthesis** for code that can be generated directly from a formal specification.
- **Epistemic planning formalisms** when the cognition problem is about who knows what and how actions update that state.

### 3. Witness-first output
The agent should prefer producing:
- proof objects,
- checked postconditions,
- valid plans,
- model witnesses,
- or solver certificates,

before it produces implementation artifacts. Code or prose then becomes a projection from the witness, not the other way around.

### 4. Reification layer
Once a formal witness exists, the system translates it back into the target space:
- code patches,
- test updates,
- operational plans,
- user explanations,
- UI or workflow artifacts.

This step needs its own check, because correctness can be lost during projection even if the formal result was sound.

## What the papers suggest
- **Lahiri**: the core bottleneck is intent formalization.
- **Endres et al.**: natural-language intent can be translated into usable postconditions that catch real bugs.
- **Murphy et al.**: hard program pieces should be routed into formal synthesis rather than left entirely to the LLM.
- **Lean Copilot / FVEL**: theorem provers can be active reasoning workspaces, not just post-hoc verifiers.
- **EPDDL**: if cognition is epistemic or multi-agent, the formal space may be a planning language rather than a proof goal.
- **Allen et al.**: if LLMs help ground symbols, the surrounding logic still needs preserved soundness/completeness properties.

## My current verdict
If the goal is an agent whose cognition is genuinely formal at the core, the right design is:
- a typed formalization gate,
- a small family of formal spaces chosen by fit,
- a strict witness-first policy,
- and refinement checks on the way back into implementation space.

That is more realistic than demanding that every problem be expressed directly in one universal proof assistant, and more principled than using formal tools only as occasional audits.

## Open design problems
- How should the agent decide which formal space is the right one?
- Can one maintain a common meta-IR above proofs, plans, and constraints?
- How interactive must the user be during intent formalization?
- When should the system refuse implementation because the formalization is too weak?

## Related pages
Read this with [[formal-cognition-loop]], [[theorem-proving-as-cognitive-kernel]], [[formal-methods-for-agent-harnesses]], [[probabilistic-epistemic-updates]], [[partial-order-trace-semantics]], and [[new-harness-design-notes]].
