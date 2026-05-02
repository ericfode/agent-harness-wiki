---
title: Specification Elaboration Naming Frame
created: 2026-05-02
updated: 2026-05-02
type: query
tags: [formal-methods, semantics, work-management, context-engineering]
sources: [raw/articles/specification-elaboration-naming-research.md, concepts/formal-methods-for-agent-harnesses.md, concepts/theorem-proving-as-cognitive-kernel.md, concepts/work-management-primitives.md, queries/non-linear-interface-options-for-next-harness.md, queries/node-card-and-minimum-adapter-contract.md]
---

# Specification Elaboration Naming Frame

## Question

What should replace "spec image" for the toolkit in
`/Users/ericfode/Documents/New project 4`?

## Short answer

Accepted name: **Spec Gym** as the CLI/product name, with **collaborative spec
verifiability environment** as the category description. Use **Claim Lattice**
for the internal model, not for the command users type.

"Spec image" points at the wrong thing. It sounds like a visual snapshot or
graph-rendering feature. The project is better understood as a tool-neutral
kernel for turning written specifications into typed claims, evidence,
obligations, verification surfaces, viability critiques, formal predicates, and
optional adapters.

Earlier recommendation was **Intent Lattice**, then **Claim Lattice**. Those were
better than "spec image", but still too artifact-shaped for the CLI. The command
name should evoke the process: a human/agent/prover environment where a spec is
played, attacked, refined, scored, and either readied or rejected.

## Why "Spec Image" is wrong

The product is not primarily an image.

It does create a graph-shaped artifact, but that graph is only one projection of
the underlying model. The important thing is that the system converts prose into
a representation that can be questioned, refined, rejected, formalized, and sent
to humans or agents for narrow follow-up work.

In the terms of knowledge representation, the core artifact acts as a surrogate
for the idea: it lets the user reason about consequences before acting. It also
commits to an ontology of goals, requirements, risks, tests, claims, findings,
and adapters. That is not an image; it is a reasoning substrate.

## Research basis

The naming pass drew on adjacent bodies of language:

1. **Knowledge representation**
   - A representation is a surrogate, a set of ontological commitments, a
     fragmentary theory of reasoning, a computational medium, and a human
     expression medium.
   - This favors "model", "lattice", "representation", or "kernel" over
     "image".

2. **Formal concept analysis**
   - FCA builds concept lattices from object-attribute relations.
   - The toolkit is not doing full FCA yet, but its direction is compatible:
     claims and artifacts become objects; properties, obligations, risks, and
     evidence become attributes and relations.
   - This makes "lattice" an honest aspirational term.

3. **Problem Frames**
   - Requirements work should distinguish problem world, requirement, and
     machine/solution behavior.
   - The name should not sound like implementation planning. It should preserve
     the problem-space and intent-elaboration posture.

4. **Moldable Development**
   - The method starts with questions, builds contextual tools, and interprets
     results to guide action.
   - This favors a name that can contain many adapters without becoming any one
     adapter.

5. **Requirements verifiability**
   - Requirements quality guidance treats verifiability/testability as a
     concrete property: can compliance be shown through test, demonstration,
     inspection, or analysis?
   - This favors "claim", "obligation", "evidence", "verification surface", and
     "criterion" over "image".

6. **Specification synthesis and RL**
   - Recent formal-specification synthesis work uses negative tests as a
     completeness signal for reinforcement learning.
   - This makes the project easier to frame as an environment: states are
     specification models, actions are refinements, and rewards are increases in
     verifiability rather than vague improvement.

## Candidate names

| Name | Verdict | Why |
| --- | --- | --- |
| Spec Gym / `specgym` | Best CLI candidate | Evokes a playable environment for humans, agents, provers, tests, and future RL policies. |
| Proveout / `proveout` | Strong non-ML fallback | Verb-like and focused on pre-prototype validation, but less obviously multiplayer/playable. |
| Claim Lattice | Best internal model name | Claims are the units that can be traced, tested, contradicted, strengthened, proved, or rejected. |
| Collaborative Spec Verifiability Environment | Best category phrase | Plainly names the job: improve verifiable aspects of a specification while preserving human, agent, prover, and test participation. |
| Intent Lattice | Good but demoted | Captures goals and constraints, but underplays verification pressure and RL signal design. |
| Intent Workbench | Good broader alternative | Conveys active elaboration and tool use, but loses the formal-methods edge. |
| Problem Lattice | Good for rejection pressure | Centers problem-space discipline, but underplays implementation consistency across languages. |
| Obligation Graph | Useful subterm | Good for formal requirements, but too compliance-heavy for ideation and bad-idea rejection. |
| Concept Cartography | Tempting but too visual | Better than "image", but still pulls toward map/UI expectations. |
| Specification Workbench | Safe but generic | Accurate, but sounds like an IDE feature rather than a new reasoning kernel. |

## Recommended vocabulary

Project/product:

- **Spec Gym**

CLI command:

- `specgym`

Category:

- **collaborative spec verifiability environment**

Core terms:

- `verifiability model`: canonical typed representation.
- `claim lattice`: model-level network of claims, refinements, obligations,
  evidence, contradictions, and verification surfaces.
- `obligation graph`: proof/test/analysis obligations derived from the model.
- `verification surface`: any way a claim can be checked: test, proof,
  inspection, analysis, negative example, benchmark, or manual review.
- `viability critique`: findings that pressure the idea before prototype.
- `refinement action`: a candidate change to the model.
- `refinement packet`: tool-neutral next-work artifact, suitable for a human,
  agent, Symphony workflow, or future RL policy.
- `reward signal`: measured change in verifiability, traceability,
  falsifiability, consistency, obligation discharge, or early rejection value.
- `adapter`: optional projection into a tool, workflow, prover, or execution
  queue.

Command vocabulary:

- `specgym play spec.md`: open an interactive human/agent refinement loop.
- `specgym score spec.md`: report current verifiability and rejection pressure.
- `specgym step spec.md --action split_claim --claim claim-12`: apply one durable
  refinement action.
- `specgym rollout spec.md --policy human`: record a sequence of player moves.
- `specgym export spec.md --projection symphony`: project the current state into an
  adapter.
- `specgym play spec.md`: emit default prover-facing artifacts, including
  `ClaimLattice.lean`.

Avoid:

- `spec image`
- `spec map`
- `visual spec`
- `spec canvas`
- `graph viewer`

## Design implication

The top-level `spec.md` in the project should eventually be renamed internally
from "Spec Imaging Toolkit" to a Spec Gym / verifiability-environment
framing:

- title: `Spec Gym Specification`
- subtitle/category: `A collaborative spec verifiability environment`
- default artifact: `verifiability-model.json` or `claim-lattice.json`
- formal artifact: `ClaimLattice.lean`
- critique: `viability-critique.md`
- execution packet: `refinement-packet.md`

Do not do that rename mechanically until the user accepts the direction. The
important immediate correction is conceptual: the project is not imaging
specifications; it is constructing a verifiability model where claims can be
made sharper, checked, rewarded, or rejected.

## RL Environment Boundary

A future spec RL environment needs these pieces, but it must remain playable by
humans. The same environment should accept moves from a human, an LLM agent, a
prover, a test runner, a search procedure, or a learned policy.

- `observation`: source spec plus current claim lattice, source anchors,
  extracted claims, obligations, critiques, tests, proof artifacts, and adapter
  outputs.
- `action`: split, merge, strengthen, weaken, restate, classify, add evidence,
  add negative test, add proof obligation, mark non-goal, reject idea, or ask for
  a narrower experiment.
- `actor`: human, agent, prover, test runner, adapter, or policy.
- `reward`: verifiability score delta, traceability score delta,
  falsifiability score delta, contradiction reduction, ambiguity reduction,
  obligations discharged, negative tests rejected, or invalid idea killed early.
- `done`: implementation-ready threshold reached, idea rejected, or unresolved
  state preserved with named missing evidence.
- `safety invariant`: the policy cannot hide unverifiable claims by deleting
  source evidence or weakening the problem statement without recording that
  tradeoff.

The current toolkit should therefore emit not just "a graph", but the minimum
state needed to score specification refinements.

## Human Play Boundary

The human is not outside the environment as a supervisor of last resort. The
human is a player.

Human moves include:

- choosing that a claim matters
- declaring a claim irrelevant
- weakening an overambitious claim
- adding a counterexample or negative test
- accepting an explicit uncertainty
- rejecting the project as not worth implementing
- overriding a reward metric with recorded rationale

The system should make those moves durable and comparable with automated moves.
That is what lets the project become an RL environment later without losing the
actual judgment that made the specification better.

## Related pages

Read with [[formal-methods-for-agent-harnesses]], [[theorem-proving-as-cognitive-kernel]],
[[work-management-primitives]], [[non-linear-interface-options-for-next-harness]], and
[[node-card-and-minimum-adapter-contract]].
