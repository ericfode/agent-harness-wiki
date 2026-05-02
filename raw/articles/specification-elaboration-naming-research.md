---
title: Specification Elaboration Naming Research
author: local synthesis with external references
date: 2026-05-02
accessed: 2026-05-02
ingested: 2026-05-02
---

# Specification Elaboration Naming Research

**Context:** naming pass for `/Users/ericfode/Documents/New project 4`.

The term "spec image" is misleading. It makes the product sound like a visual
snapshot or graph viewer. The actual product is closer to a knowledge
representation and elaboration kernel: it turns prose into typed claims,
obligations, evidence links, critique findings, formal predicates, and optional
tool adapters.

## Sources checked

- Davis, Shrobe, and Szolovits, "What Is a Knowledge Representation?"
  - URL: https://groups.csail.mit.edu/medg/ftp/psz/k-rep.html
  - Naming implication: the core artifact should be framed as a representation:
    a surrogate, a set of ontological commitments, a fragmentary theory of
    reasoning, a computational medium, and a medium of human expression.
- Formal Concept Analysis introduction
  - URL: https://arxiv.org/abs/1703.02819
  - Naming implication: "lattice" is justified if the system organizes objects
    and attributes into a concept hierarchy rather than merely drawing a graph.
- Problem Frames approach
  - URL: https://www.researchgate.net/publication/4308621_The_Problem_Frames_Approach_to_Software_Engineering
  - Naming implication: the name should preserve the problem-space versus
    solution-space boundary; avoid names that sound like implementation planning.
- Moldable Development
  - URL: https://book.gtoolkit.com/moldable-development-ejn67l5cdqh83kegi9umt1mdd
  - Naming implication: the system is a question-driven tool-building surface,
    not one fixed visualization.
- Open Knowledge Maps
  - URL: https://openknowledgemaps.org/
  - Naming implication: "map" is understandable, but likely over-indexes on
    visual overview. It is better as an adapter/capability word than as the core
    product name.

## Research takeaways

1. "Image" is the wrong noun.
   - It implies static visual output.
   - It makes the graph projection sound canonical.
   - It underplays proof obligations, critique, and execution packets.

2. "Map" is better but still risky.
   - It captures topology and exploration.
   - It still points users toward visual surface expectations.
   - It should remain a capability/adaptor term.

3. "Workbench" is accurate but bland.
   - It suggests active elaboration.
   - It does not communicate the formal or typed structure.

4. "Lattice" fits the formal direction.
   - It suggests order, refinement, concepts, and constraints.
   - It aligns with formal concept analysis.
   - It may be too abstract for broad users, but this project is formal-methods
     oriented enough for the term to carry useful signal.

5. "Intent" is stronger than "specification" for the product noun.
   - It covers problem, goals, constraints, obligations, tests, risks, and
     bad-idea rejection.
   - It avoids making the tool sound like a document formatter.
   - It still needs typed artifacts to prevent vague product-speak.

## Naming recommendation

Initial recommendation: use **Intent Lattice** as the working project/product
name.

Use these internal terms:

- `intent model`: canonical core artifact.
- `intent graph`: graph-shaped serialization/projection of the model.
- `viability critique`: bad-idea findings.
- `refinement packet`: generic work packet for the next correction.
- `adapter`: optional projection into a concrete tool or workflow.

Second-choice literal option: **Claim Lattice**.

Avoid:

- Spec Image
- Spec Map
- Spec Graph
- Specification Canvas
- Visual Spec

These names keep dragging attention back to display technology rather than
problem elaboration and formalizable intent.

## 2026-05-02 clarification: verifiability, not imagery

User clarification shifted the frame: the project is really about making
specifications **more verifiable**. The specification may remain partly
unbounded, exploratory, and domain-specific, but the toolkit should expose the
aspects that can be checked, measured, criticized, or used as training signal.

Additional sources checked:

- NASA, "Appendix C: How to Write a Good Requirement"
  - URL: https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/
  - Naming implication: verifiability/testability is a first-class property of
    a good requirement. A requirement should have a means of verification:
    test, demonstration, inspection, or analysis.
- Huang et al., "Reinforcement Learning with Negative Tests as Completeness
  Signal for Formal Specification Synthesis"
  - URL: https://arxiv.org/abs/2604.05820
  - Naming implication: an RL environment for specifications needs a reward
    signal that distinguishes weak specifications from stronger ones. Negative
    tests are one concrete completeness signal.
- Neider and Roy, "What is Formal Verification without Specifications? A
  Survey on mining LTL Specifications"
  - URL: https://arxiv.org/abs/2501.16274
  - Naming implication: formal verification depends on precise specifications,
    but producing those specifications is itself a difficult, error-prone task.
    This supports a toolkit focused on specification improvement before
    implementation.

Updated conclusion: **Claim Lattice** is a better product/kernel name than
Intent Lattice if the durable center is verifiability.

Use "collaborative spec verifiability environment" as the category description.
Use **Claim Lattice** as the working name for the core model.

Why:

- A claim is the smallest unit that can be sharpened, traced, contradicted,
  tested, proved, or rejected.
- A lattice can organize claims by refinement, dependency, evidence, obligation,
  and verification strength.
- The name does not imply a graph viewer, canvas, issue tracker, or prover.
- It gives a future RL environment a natural state/action/reward boundary.

RL-environment interpretation:

- `state`: the current claim lattice plus source anchors, dependencies,
  obligations, critiques, tests, proof artifacts, and adapter outputs.
- `action`: split a claim, strengthen a claim, add evidence, add a negative
  test, attach a proof obligation, resolve contradiction, mark a non-goal,
  reject an idea, or request a narrower experiment.
- `reward`: increased verifiability, increased traceability, increased
  falsifiability, discharged obligations, negative tests rejected, ambiguity
  reduced, complexity justified, or invalid idea rejected early.
- `terminal`: the spec reaches an implementation-ready threshold, is rejected
  as a bad idea, or is marked unresolved with named missing evidence.

Human-in-the-loop interpretation:

- The environment is not only for automated RL policies.
- A human can take the same actions as an agent: split claims, reject claims,
  add examples, mark uncertainty, request proof obligations, accept weaker
  guarantees, or choose that an idea is not worth implementing.
- Human moves should be first-class transitions in the same history as agent and
  prover moves.
- The system should preserve authorship/provenance of moves because the quality
  of a refinement depends on who or what made it and what evidence was visible.
- Reward should not erase judgment. It should make the verifiable part of the
  judgment explicit.

This is a better frame than "spec image": the graph remains useful, but it is a
projection of a verifiability environment rather than the product identity.

## 2026-05-02 clarification: CLI name must evoke the process

User rejected **Claim Lattice** as a CLI/product name because it names the model,
not the process the tool encodes.

That critique is correct.

Layered naming should be:

- CLI/product: short process/environment name.
- Process verb: what the user is doing to a spec.
- Internal model: claim lattice / verifiability model.
- Output artifacts: claim lattice, obligation graph, viability critique,
  refinement packet.

Accepted CLI recommendation: **Spec Gym**, command `specgym`.

Why `specgym` fits the process better:

- It evokes an environment rather than a static artifact.
- It admits both human and agent play.
- It naturally supports RL language without making RL mandatory.
- It gives obvious CLI verbs: `play`, `step`, `score`, `reset`, `rollout`,
  `export`, `train`.
- It keeps the internal formal object available as `claim-lattice` without
  forcing that phrase to be the user-facing executable.

Recommended command shape:

```text
specgym play spec.md
specgym score spec.md
specgym step spec.md --action split_claim --claim claim-12
specgym rollout spec.md --policy human
specgym export spec.md --projection symphony
```

Secondary candidate: **Proveout**, command `proveout`.

Why it is useful:

- It is a verb-like command.
- It captures the pre-prototype goal: prove out whether the idea deserves
  implementation.
- It is less ML-coded than `specgym`.

Why it is weaker:

- It underplays multiplayer/human-play mechanics.
- It sounds more like final proof than iterative environment play.

Practical npm registry check on 2026-05-02:

- `specgym`: registry returned 404.
- `spec-gym`: registry returned 404.
- `speclab`: registry returned 404.
- `spec-lab`: registry returned 404.
- `proveout`: registry returned 404.
- `spec-assay`: registry returned 404.
- `spec-trial`: registry returned 404.
- `specforge`: already exists.
- `assay`: already exists.
- `sharpen`: already exists.
- `spec-check`: already exists.

Conclusion: use `specgym` as the CLI name. Keep **Claim Lattice** as the
internal model, not as the executable.

User accepted the name on 2026-05-02.
