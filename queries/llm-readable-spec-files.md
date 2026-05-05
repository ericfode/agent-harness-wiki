---
title: LLM-Readable Spec Files
created: 2026-05-04
updated: 2026-05-04
type: query
tags: [survey, context-engineering, formal-methods, work-management, code-quality]
sources: [raw/articles/llm-readable-spec-files-research-2026-05-04.md, concepts/context-engineering.md, concepts/evaluation-and-review-loops.md, concepts/formal-methods-for-agent-harnesses.md, queries/specification-elaboration-naming-frame.md, raw/papers/arxiv-endres-2023-natural-language-to-postconditions.md]
---

# LLM-Readable Spec Files

## Question

What kind of `spec.md` files work best for LLM agents, what do excellent specs
look like, and how should they be verified?

## Short answer

The best `spec.md` files are not essays. They are compact executable contracts:
structured enough for the model to parse, precise enough to constrain
implementation, and instrumented enough that humans, tests, evaluators, and
formal tools can contest the result.

For agent work, `spec.md` should be the canonical contract, not the whole wiki.
It should orient the agent, name constraints, define requirements and invariants
with stable IDs, attach every normative claim to a verification method, and
point to deeper documents only when necessary. This is the specification-facing
version of [[context-engineering]]: what matters must be visible, scoped, and
recoverable.

## What makes a spec work for LLMs

### Stable authority

The agent should know which file is canonical and what has lower authority. A
top-level `spec.md` works when it is treated as the contract and not as a
scratchpad. If the project is large, the top-level file should be an authority
map: normative contract, explanatory notes, historical rationale, and adapter
projections should not collapse into one undifferentiated prompt. This is the
same pressure behind [[instruction-layering]].

### Predictable structure

LLMs handle regular Markdown sections better than clever document prose. Use
boring headings, stable identifiers, short lists, and tables where traceability
matters. Useful ID families: `REQ`, `INV`, `AC`, `NFR`, `SCN`, and `TBR`.

### One claim per unit

Every normative statement should be singular. If one bullet contains three
behaviors, it is three requirements. This matters because agents, tests, and
reviewers need to point at one thing at a time.

### Verification next to the claim

The spec should not save verification for the end. Each requirement or invariant
should name at least one verification method:

| Method | Use when |
| --- | --- |
| Test | Behavior can be executed. |
| Demonstration | A workflow or UI path must be shown. |
| Inspection | A static artifact, schema, or UI state can be reviewed. |
| Analysis | A property requires reasoning, calculation, model checking, or proof. |

That ladder is directly compatible with [[evaluation-and-review-loops]] and the
formal turn described in [[formal-methods-for-agent-harnesses]].

### Examples and counterexamples

Positive examples teach the target shape. Negative examples define the boundary.
For LLMs, counterexamples are often the cheapest way to prevent plausible wrong
implementations. Include a valid case, invalid case, boundary case, forbidden
move, and minimal passing scenario.

### Named uncertainty

Do not hide uncertainty in polished prose. Use `TBR`, `TBD`, or `NEEDS
CLARIFICATION`, then give each item an owner, impact, and resolution condition.
Agents handle explicit unknowns better than implied gaps.

## Recommended `spec.md` skeleton

```text
# Spec: <system or feature>

## Status
- owner, status, created, updated, canonical source, target readers

## Objective
- problem, intended outcome, why now

## Context
- repo paths, source documents, constraints, first files to inspect

## Glossary
- <term>: <definition>

## Scope
- in scope, out of scope, forbidden moves

## System Model
- actors, entities, state machine, events, interfaces

## Requirements
- REQ-001: The system MUST ...

## Invariants
- INV-001: ...

## Scenarios
- SCN-001: priority, independent test, Given/When/Then

## Verification Matrix
| ID | Claim | Method | Evidence | Status |
| --- | --- | --- | --- | --- |

## Operational Gates
- unit, integration, build, lint, replay/browser/formal

## Examples and Counterexamples
- valid, invalid, edge

## Open Questions
- TBR-001:

## Change Log
- YYYY-MM-DD: ...
```

## What excellent specs look like

Excellent specs have these traits:

- They can be read in one pass by a fresh agent.
- They separate user intent from implementation strategy.
- They include non-goals and forbidden moves.
- They tie every normative claim to a verification method.
- They include both examples and counterexamples.
- They are concise enough to stay loaded, with deeper material linked by
  progressive disclosure.
- They preserve assumptions, rationale, and unresolved questions explicitly.

Weak specs usually fail in predictable ways:

| Weak pattern | Failure mode |
| --- | --- |
| Long narrative with no IDs | Agent cannot trace obligations. |
| "Make it robust/user-friendly/fast" | No testable success condition. |
| Requirements mixed with rationale | Reviewer cannot tell what is normative. |
| No non-goals | Agent overbuilds. |
| No examples | Agent guesses shape from priors. |
| No verification matrix | Completion becomes a vibe check. |
| No open-question ledger | Unknowns get laundered into fake certainty. |

## Verification ladder

1. Structural lint: required sections, unique IDs, no dangling references, no
   unresolved `TBR` without owner or condition.
2. Requirements-quality lint: ambiguous words, multi-behavior requirements,
   missing glossary terms, missing verification methods, and implementation
   leakage.
3. Traceability matrix: every `REQ`, `INV`, and `AC` maps to evidence.
4. Executable gates: the spec names real unit, integration, build, lint,
   replay, browser, or formal commands.
5. Negative tests: the spec says what bad implementation should fail.
6. Fresh-agent comprehension eval: a fresh agent produces plan, test plan,
   risks, and questions from only the spec and repo.
7. Independent reviewer pass: compare diff and evidence to spec IDs, not to the
   builder's summary.
8. Formal slice: promote the smallest central invariant into Lean, TLA+, Alloy,
   Dafny, or another checker when the stakes justify it.

This is where `spec.md` starts looking like a [[specification-elaboration-naming-frame|Spec Gym]]
surface: the useful action is not only implementing, but attacking and refining
the spec.

## Ideas worth building

- `spec doctor`: parse `spec.md`, extract claims, flag ambiguity, and emit a
  verification matrix.
- `spec score`: report verifiability, traceability, falsifiability, and
  unresolved-risk pressure.
- `spec ask`: run a fresh-agent comprehension probe and grade the response
  against the spec.
- `spec lattice`: convert prose into a claim lattice with refinements, evidence,
  contradictions, and obligations.
- `spec formalize`: export selected invariants to Lean, TLA+, Alloy, Dafny, or
  another checker.

## Bottom line

A good `spec.md` is a context object. An excellent `spec.md` is an adversarial
acceptance surface. It tells the model what to build, what not to build, how to
know when it is done, and which claims still require judgment.

Read this with [[harness-engineering]], [[context-engineering]],
[[evaluation-and-review-loops]], [[formal-methods-for-agent-harnesses]], and
[[specification-elaboration-naming-frame]].
