---
title: "Prompt-Program Architecture Plans for another-harness and Gas City"
created: 2026-04-11
updated: 2026-04-11
type: query
tags: [comparison, context-engineering, program-synthesis, work-management]
sources: [queries/research-on-open-questions-in-prompt-optimization-and-language-programs.md, queries/open-questions-in-prompt-optimization-and-language-programs.md, queries/another-harness-and-atropos.md, queries/gas-city-but-its-just-codex.md]
---

# Prompt-Program Architecture Plans for another-harness and Gas City

## Goal
Turn the ten prompt-program research questions into two repo-grounded architecture plans:
- one for `another-harness`
- one for `gas-city-but-its-just-codex`

## Produced artifacts

### another-harness
Repo plan:
- `/Users/ericfode/src/another-harness/docs/plans/2026-04-11-another-harness-prompt-program-architecture-plan.md`

Core stance:
- optimize compiled, contract-bearing role bundles derived from canonical repo artifacts
- trust executable checks plus separate evaluator artifacts over judge-only scoring
- keep compile-time, run-time, and promotion-time explicitly separate
- keep memory plural and owned: repo truth, preserved evidence, Honcho memory, and procedure candidates each have distinct roles
- treat release engineering as staged promotion through the existing work/evaluation/handoff/checker architecture

Why this fits:
- `another-harness` already has the right asymmetry: Lean is canonical but revisable, while repo artifacts are canonical operational truth.
- The benchmark families (`work_item_closure`, `evaluator_discipline`) are already the right place to introduce prompt-program bundles without inventing a second ontology.

Recommended first slice:
- define a prompt-program bundle contract for the two live environment families
- add split-aware benchmark metadata and structured score vectors
- do not add a new canonical prompt-program registry yet

### gas-city-but-its-just-codex
Repo plan:
- `/Users/ericfode/src/gas-city-but-its-just-codex/docs/plans/2026-04-11-gascity-prompt-program-architecture-plan.md`

Core stance:
- treat formulas as the base prompt-program substrate
- compare and promote typed variant bundles rather than isolated prompt strings
- trust blind/state-based verifiers plus real app-server benchmarks over commentary
- keep compile-time artifacts distinct from run-time overlays and workspace state
- treat release engineering as promoted formula-family selection plus evidence bundles

Why this fits:
- the repo already has durable workflow state, formula lineage/assessment, typed control surfaces, and real evaluator lanes
- the missing layer is not a generic optimizer but an explicit variant-bundle plane that makes comparison, transfer, and release honest

Recommended first slice:
- create explicit variant-bundle configs and schema
- enrich `FormulaEvaluation.metrics` into structured scorecards
- keep optimizer work manual or lightly searched until the measurement environment is stable

## Main contrast between the two repos

### another-harness
The design center is semantic discipline:
- Lean-backed meaning
- repo-native canonical truth
- strict attempt-vs-stream distinctions
- evaluator separation as a first-class invariant

So the prompt-program layer should remain thin and contract-heavy.

### gas-city-but-its-just-codex
The design center is orchestration and releaseability:
- formula families
- durable workflow state
- typed operator/control-plane surfaces
- benchmark and blind-verifier evidence

So the prompt-program layer should become a formula-and-variant release system.

## Shared lesson
Both repos should refuse the old temptation to treat prompts as ambient prose. In both cases the right move is to make prompt programs into explicit, versionable, evidence-bearing artifacts. The difference is where each repo wants to anchor that explicitness:
- `another-harness` anchors it in Lean plus repo work/evaluation artifacts
- `gas-city-but-its-just-codex` anchors it in formulas, ledger state, and benchmarked release bundles

## Related pages
Read this with [[research-on-open-questions-in-prompt-optimization-and-language-programs]], [[open-questions-in-prompt-optimization-and-language-programs]], [[another-harness-and-atropos]], and [[gas-city-but-its-just-codex]].
