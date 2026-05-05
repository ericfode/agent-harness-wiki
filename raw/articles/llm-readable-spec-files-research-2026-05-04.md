---
title: LLM-readable spec.md files research
author: local synthesis with external references
date: 2026-05-04
accessed: 2026-05-04
ingested: 2026-05-04
---

# LLM-readable spec.md Files Research

Context: research pass for `/Users/ericfode/wiki`.

Question: what kind of `spec.md` files work best for LLM agents, what excellent
specs look like, and how those specs should be verified.

## Sources checked

- OpenAI, "Prompt engineering"
  - URL: https://developers.openai.com/api/docs/guides/prompt-engineering
  - Takeaway: Markdown headers, lists, XML-style boundaries, examples, and
    explicit context sections help models understand hierarchy and task shape.
    OpenAI also recommends pinning model snapshots and building evals around
    prompt behavior as prompts evolve.
- OpenAI, "Evaluation best practices"
  - URL: https://developers.openai.com/api/docs/guides/evaluation-best-practices
  - Takeaway: evals should be task-specific, run continuously, use logs as
    case-mining material, automate where possible, and maintain human agreement
    for calibration. Vibe-based evals are explicitly an anti-pattern.
- Anthropic Claude Code, "How Claude remembers your project"
  - URL: https://code.claude.com/docs/en/memory
  - Takeaway: repo instruction files are loaded context, not enforced
    configuration. Specific, concise instructions work better; recurring
    correction should become durable guidance; larger projects should split
    rules into scoped files.
- GitHub Docs, "About customizing GitHub Copilot responses"
  - URL: https://docs.github.com/en/copilot/concepts/prompting/response-customization
  - Takeaway: repository instructions should be short, self-contained, broadly
    applicable, and include project overview, folder structure, coding
    standards, and tool/library details. Some Copilot contexts impose explicit
    size limits.
- GitHub Spec Kit
  - URL: https://github.com/github/spec-kit
  - URL: https://github.com/github/spec-kit/blob/main/spec-driven.md
  - URL: https://raw.githubusercontent.com/github/spec-kit/main/templates/spec-template.md
  - Takeaway: spec-driven development treats specifications as the primary
    artifact. The template shape is strong: user stories, independent tests,
    acceptance scenarios, edge cases, functional requirements, entities,
    measurable success criteria, assumptions, and later plan/checklist gates.
    The method also emphasizes CLI observability, test-first development,
    simplicity gates, and integration-first tests.
- NASA, "Appendix C: How to Write a Good Requirement"
  - URL: https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/
  - Takeaway: requirements should be clear, concise, singular, complete,
    traceable, implementation-free, and verifiable. Verification should be
    possible by test, demonstration, inspection, or analysis; vague words like
    easy, flexible, robust, quickly, and user-friendly are suspect.
- NASA, "Appendix D: Requirements Verification Matrix"
  - URL: https://www.nasa.gov/reference/appendix-d-requirements-verification-matrix/
  - Takeaway: every normative requirement should have an identifier, source, and
    verification approach. Only true requirements should enter the matrix.
- INCOSE Requirements Working Group, "Guide to Writing Requirements" overview
  - URL: https://www.incose.org/docs/default-source/working-groups/requirements-wg/guidetowritingrequirements/gtwr-v4-overview-081723.pdf
  - Takeaway: good requirements are necessary, unambiguous, complete, singular,
    verifiable/validatable, feasible, appropriate, correct, consistent, and
    comprehensible; good sets are also complete, consistent, feasible, and able
    to be validated.
- Microsoft Foundry, "Evaluating AI Agents: Can LLM-as-a-Judge Evaluators Be
  Trusted?"
  - URL: https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/evaluating-ai-agents-can-llm%E2%80%91as%E2%80%91a%E2%80%91judge-evaluators-be-trusted/4480110
  - Takeaway: LLM judges can scale objective rubric checks, but they need
    calibration, repeated measurement, human alignment checks, and caution
    around ambiguous interpretation.
- Endres et al., "Can Large Language Models Transform Natural Language Intent
  into Formal Method Postconditions?"
  - URL: https://arxiv.org/abs/2310.01831v2
  - Takeaway: natural-language intent can be translated into checkable
    postconditions, but quality must be measured by correctness and
    discriminative power. The key move is turning prose into assertions that
    catch real defects.

## Synthesis

An excellent `spec.md` for LLM work is not a product essay. It is a compact
operating contract for agents, humans, tests, and sometimes provers.

It needs to do four jobs at once:

1. Orient the model quickly.
2. Constrain implementation choices.
3. Define what counts as success.
4. Provide enough structure for verification.

The best specs are therefore closer to a hybrid of prompt, requirements set,
test plan, and traceability matrix than to a traditional narrative design doc.

## What works best for LLMs

- Stable top-level location: the agent should know where the canonical contract
  lives. If subdocuments exist, `spec.md` should be the table of contents and
  authority map.
- Predictable headings: models benefit from repeated section shapes. Avoid
  clever prose hierarchy.
- Explicit terms: include a glossary for domain nouns, state-machine names,
  role names, event names, and artifact names.
- Requirement identifiers: use stable IDs such as `REQ-001`, `INV-003`,
  `AC-002`, `NFR-004`, `TBR-001`.
- One thought per requirement: compound paragraphs are bad input for both
  models and tests.
- Concrete examples and counterexamples: these are often more steerable than
  prose instructions.
- Non-goals and forbidden moves: LLMs overbuild when negative space is not
  stated.
- Verification next to the claim: every normative claim should name at least
  one verification mode.
- Real gates: commands, tests, linters, browser checks, formal builds, replay
  commands, or explicit human review steps.
- Named uncertainty: use `TBR` or `NEEDS CLARIFICATION` rather than burying
  unresolved choices in smooth prose.
- Progressive disclosure: keep the canonical file concise; push deep protocol
  details, UI flows, or proofs into linked files.

## Proposed top-level shape

```text
# Spec: <system or feature>

## Status
- owner
- status
- created / updated
- canonical source
- target readers

## Objective
- problem
- success outcome
- why now

## Context
- relevant repo paths
- upstream documents
- existing constraints
- what the agent should inspect first

## Glossary
- domain terms
- state names
- actor names
- artifact names

## Scope
- in scope
- out of scope
- forbidden implementation moves

## System Model
- actors
- entities
- state machine
- events
- data contracts
- external interfaces

## Behavioral Requirements
- REQ-001: ...
- REQ-002: ...

## Invariants
- INV-001: ...
- INV-002: ...

## User / Operator Scenarios
- scenario
- priority
- independent test
- acceptance cases

## Verification Matrix
| ID | Claim | Method | Evidence | Owner | Status |

## Operational Gates
- test command
- build command
- lint command
- replay / browser / formal command

## Examples and Counterexamples
- positive examples
- negative examples
- edge cases

## Open Questions
- TBR-001: ...
- TBR-002: ...

## Change Log
- date, decision, reason
```

## Verification ladder

1. Structural lint: file exists, headings present, IDs unique, no duplicate
   requirement IDs, no unresolved `TBR` without owner/date.
2. Requirements-quality lint: flag vague terms, compound requirements, missing
   subject/predicate, missing verification method, implementation leakage, and
   undefined glossary terms.
3. Traceability check: every normative ID appears in the verification matrix;
   every acceptance test points back to at least one requirement or invariant.
4. Executable tests: unit, integration, browser, replay, or CLI tests prove
   concrete behavior.
5. Negative and metamorphic tests: the spec should say what must fail or remain
   invariant under transformation.
6. Cross-agent comprehension eval: give the spec to an agent in a fresh context
   and ask it to produce an implementation plan, test plan, and risk list; score
   whether it preserves the intended constraints.
7. Implementation replay: compare the final diff, artifacts, and evidence
   against the spec and verification matrix.
8. Formal slice: for small but central invariants, translate into Lean, TLA+,
   Alloy, Dafny, or another checker. Do not pretend the whole spec is formal
   unless it actually is.

## Ideas worth building

- `spec doctor`: parses `spec.md`, extracts normative claims, finds ambiguity,
  and emits a verification matrix.
- `spec score`: reports verifiability, traceability, and falsifiability scores.
- `spec mutate`: creates bad implementations or bad tests to see whether the
  spec catches them.
- `spec replay`: checks whether an implementation branch actually discharged the
  acceptance surface.
- `spec ask`: runs a fresh-agent comprehension probe and compares the plan to a
  rubric.
- `spec lattice`: converts prose into a claim lattice with refinements,
  evidence, contradictions, and open obligations.
- `spec formalize`: promotes selected invariants into a prover-facing artifact.

## Bottom line

The best `spec.md` files for LLMs are short enough to load, structured enough to
parse, specific enough to constrain, and verifiable enough to argue with. A spec
that cannot produce tests, checks, counterexamples, or proof obligations is only
context. Useful context is not the same as a specification.
