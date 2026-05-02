---
title: Software Verification and Testing Environment Research Program
created: 2026-05-01
updated: 2026-05-01
type: query
tags: [formal-methods, code-quality, benchmark, work-management, tool-execution]
sources: [concepts/formal-methods-for-agent-harnesses.md, concepts/evaluation-and-review-loops.md, concepts/work-management-primitives.md, queries/rl-gyms-and-executable-environments-for-ai-harnesses.md, concepts/harness-engineering.md]
---

# Software Verification and Testing Environment Research Program

## Purpose
This page anchors the first research project for a software verification and testing environment: an agent-facing substrate where tests, proofs, model checks, traces, reviewer gates, and evidence ledgers become explicit work objects rather than scattered terminal output.

The initial Kanban graph deliberately separates evidence gathering from synthesis and wiki writing. The project should connect the formal-methods line in [[formal-methods-for-agent-harnesses]] and [[formal-cognition-loop]] with the executable-environment line in [[evaluation-and-review-loops]] and [[rl-gyms-and-executable-environments-for-ai-harnesses]]. The result should inform [[harness-engineering]], not merely decorate it with proof-assistant vocabulary.

## Kanban graph
The project is currently represented in Hermes Kanban as a dependency graph:

| Task | Role | Purpose |
|---|---|---|
| `t_7a29256d` | research | Formal verification foundations: proof assistants, contracts, model checking, symbolic execution, and runtime verification. |
| `t_77b7318b` | research | Testing/evidence primitives: property testing, fuzzing, mutation testing, differential testing, coverage, shrinking, and reproducible CI. |
| `t_2cf92f9b` | research | Agent-facing architecture: how verifiers, tests, proofs, traces, evidence stores, and reviewer gates should appear as harness objects. |
| `t_8b1eb08c` | synthesis | Fan-in synthesis over the three research lanes into a research map and minimum viable architecture. |
| `t_78213be9` | wiki writing | Durable wiki update from the synthesis, including raw source notes and cross-links. |
| `t_176aa99f` | verification | Final `scripts/lint-wiki.sh` pass and repair loop. |

## Initial architecture question
The core design question is what the environment treats as first-class state. A serious version should probably not begin with “run tests” as a shell habit; it should model:

- **specification surfaces** — natural-language requirements narrowed into contracts, assertions, invariants, temporal properties, or theorem statements;
- **test/evidence primitives** — unit tests, property tests, fuzz targets, mutation suites, differential checks, coverage reports, and minimized counterexamples;
- **formal lanes** — proof obligations, model-checking tasks, symbolic-execution queries, and runtime monitors;
- **evidence ledger** — durable records of command, environment, result, artifact hash, reviewer decision, and known limitation;
- **promotion gates** — explicit state transitions from proposed implementation to tested, reviewed, proved, waived, or rejected;
- **regression memory** — prior failures and counterexamples promoted into reusable checks, adjacent to [[memory-persistence]] and [[self-evolving-workflows]].

## Research lanes to resolve
The first pass should answer four practical questions:

1. Which verification tools are worth integrating as environment primitives rather than one-off commands?
2. Which testing techniques produce agent-usable evidence rather than merely developer-facing reports?
3. What is the minimum object model needed for traces, proofs, tests, counterexamples, and review decisions?
4. Where should the boundary sit between lightweight executable contracts and heavier proof/model-checking machinery?

## Expected wiki outcome
The later wiki-writing task should either expand this page or replace it with a more source-grounded successor. Likely adjacent updates include [[formal-methods-for-agent-harnesses]], [[evaluation-and-review-loops]], [[work-management-primitives]], [[harness-engineering]], and [[rl-gyms-and-executable-environments-for-ai-harnesses]]. If the research reveals reusable named systems, they may deserve entity pages; otherwise they should remain raw source notes and structured synthesis rather than ornamental nodes.

The architecture synthesis for this project is now captured in [[agent-facing-verifier-environment-architecture]].

## Open risks
- The environment can become a bag of tools instead of a coherent semantics for evidence.
- Heavy formal methods may be over-applied where property tests or differential checks give better leverage.
- Testing output may look objective while hiding weak or irrelevant assertions.
- The agent-facing interface may need stronger provenance than ordinary CI logs provide.

The useful test is simple: after a failure, can the next agent recover the exact claim, evidence, counterexample, and required next move without reading a theatrical transcript? If yes, we have an environment. If no, we have a vibes engine wearing a lab coat.
