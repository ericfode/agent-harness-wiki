---
title: Basis Experiment Status
created: 2026-05-10
updated: 2026-05-11
type: query
tags: [survey, benchmark, work-management, code-quality, safety]
sources: [raw/articles/basis-project-deep-dive-2026-05-10.md, raw/articles/basis-reduce-imagine-codex-log-sift-2026-05-11.md, queries/basis-project-index.md, queries/basis-reduce-workbench.md, queries/basis-imagine-workbench.md, queries/spec-dataset-evolution-research-project.md, queries/spec-deep-dive-index.md]
---

# Basis Experiment Status

## Status table

| Experiment | Hypothesis | Evidence inspected | Current status | Next public milestone |
|---|---|---|---|---|
| Core Basis reducer runtime | Overcomplete prose specs can be reduced toward structured state with provenance and explicit projection targets. | `/Users/ericfode/src/basis`, HEAD `a5544e0`; `spec.md`; reducer/imaginer specs; Elixir source/tests. | Active baseline. Root is not where the recovered Reduce/Imagine spikes live. | Keep core gates green; consolidate recovered work through reviewable branches. |
| [[basis-reduce-workbench|Basis.Reduce workbench]] | Source-backed review UI can expose sentence evidence, projection impact, and decision actions without accepting model output as truth. | `/Users/ericfode/.codex/worktrees/4e6b/basis`, branch `codex/inspect-reducer-eval`, HEAD `ceb8df8`; generated UI assets; reducer control contract. | Branch is tracked and recent UI commits are coherent; pathology study is untracked. | Decide whether to commit/split/prune `spec-pathology-study/`; preserve control-contract gate. |
| [[basis-imagine-workbench|Basis.Imagine workbench]] | Plan-space futures can be compared as proposal-only implementation choices before human acceptance. | `/Users/ericfode/.codex/worktrees/95ae/basis`, branch `codex/start-imaginer`; `imaginer.html`; `future-tradeoffs.js`; runtime/provider/test diffs. | Active dirty spike. Mix tests and JS checks pass, but patch is large and unreviewed. | Stabilize into a reviewable patch; keep Packet Schema First as default unless evidence beats it. |
| Basis Hermes plugin | Basis reduction can be exposed as Hermes tools without provider-schema breakage. | `/Users/ericfode/src/basis-hermes`, HEAD `0061d32`; plugin manifest; Python reducer; dashboard API; tests. | Strongest clean integration surface. Python and JS gates pass. | Add public/synthetic golden examples and stable packet contract docs. |
| Jcode self-convergence | Model/human worker packets can drive a resumable reducer loop with validation, convergence judgement, dashboard attention, and explicit acceptance. | `/Users/ericfode/src/basis-jcode/components/spec-basis-reducer`; HEAD `4b1e621`; `.basis/self-convergence` inspected by counts only. | Richest prior experiment, but dirty/ahead and public-sensitive. 26 tests pass. | Resolve dirty state; generate public-safe run summary without packet bodies. |
| Spec-pathology study | Reducer/imaginer usefulness should be tested by behavior, process cost, intervention controls, and competence floors. | Untracked `components/spec-basis-reducer/experiments/spec-pathology-study/`; reward state and JSON score reports. | Important but not canonical. Large wave is complete but inconclusive because clean control failed below competence floor. | Add competence-floor gate; repeat only after baseline builders can pass the locked evaluator. |
| Smoke fixture reducer | The control plane can validate packet contracts without live model calls. | `.basis/smoke` names/counts and test suite. | Useful deterministic fixture lane. | Keep as regression gate; do not delete existing smoke run casually. |
| Spec-code grounding pressure | Basis records should help connect specs to code/tests/diffs, not merely look structured. | [[spec-dataset-evolution-research-project]], [[spec-deep-dive-index]], local `steward` design repo. | Design-stage external pressure. | Run a small public/synthetic connectedness benchmark with Basis records as features. |

## How it is going

The honest answer is: **promising, but still pre-consolidation**.

Good signs:

- the core Basis contract is crisp about proposal versus acceptance;
- `basis-hermes` is clean and test-passing;
- Codex tool-schema compatibility was repaired and recorded;
- [[basis-reduce-workbench]] has a tracked review/decision UI branch with a passing control-binding gate;
- the spec-pathology study measures final behavior, process cost, reducer prediction, placebo/noisy/wrong controls, and competence-floor failure separately;
- [[basis-imagine-workbench]] has a dedicated imaginer URL, future-tradeoff model, and app-server-backed lens/runtime hooks;
- `basis-jcode` has meaningful test coverage for production packet provenance, convergence, repair, dashboard decisions, and acceptance boundaries;
- the self-convergence run has enough artifact structure to be worth studying internally.

Friction signs:

- core `basis` has a red formatter gate;
- `Basis.Run.Server` is large and cross-cutting;
- `basis-jcode` is ahead by ten commits and has dirty tracked deletions;
- `.basis/self-convergence` is too sensitive to publish raw;
- dashboard state is useful but local-file and run-state capable, so it needs a loopback/auth posture.

## Current gates

| Gate | Surface | Result |
|---|---|---:|
| `mise exec -- mix test` | core `basis` | pass: `4 tests, 0 failures` |
| `mise exec -- mix compile --warnings-as-errors` | core `basis` | pass |
| `mise exec -- mix format --check-formatted` | core `basis` | fail: one formatting issue |
| `uv run --extra dev pytest -q` | `basis-hermes` | pass: `15 passed` |
| `npm test` | `basis-hermes/components/spec-basis-reducer` | pass: `4 pass` |
| `npm test` | `basis-jcode/components/spec-basis-reducer` | pass: `26 pass` |

## Experiment posture

The experiments should be judged by whether they reduce discretion, not whether they produce impressive prose.

A Basis experiment is useful when it leaves:

- source identity and line/range provenance;
- proposed records with witnesses;
- validation status;
- acceptance/rejection/defer decisions;
- explicit unresolved questions;
- target projections with loss/caveat notes;
- enough event history to audit why a record exists.

A Basis experiment is not useful merely because it has a pretty dashboard or a large packet. Large packets are not wisdom. They are, at best, disciplined compost.

## Recommended next experiments

### 1. Format-and-boundary slice

Goal: make core `basis` locally green and extract one responsibility from `Basis.Run.Server`.

Acceptance:

- format/test/compile all pass;
- no semantic behavior expansion;
- new tests around the extracted boundary.

### 2. Public-safe self-convergence summary

Goal: create a script in `basis-jcode` that emits safe summary JSON from `.basis/self-convergence`.

Allowed output:

- run ID/hash;
- counts by packet type;
- counts by round;
- validation/convergence status;
- accepted/rejected/deferred counts;
- caveats.

Disallowed output:

- prompt text;
- packet bodies;
- NDJSON/log bodies;
- dashboard state body;
- source text from working copies.

### 3. Golden public/synthetic spec reduction

Goal: reduce one tiny synthetic spec and one explicitly public permissive spec through `basis-hermes`, then publish only the packet schema and summarized records.

Acceptance:

- deterministic output hashes;
- validation pass;
- no local paths in publishable examples;
- reviewer can trace each record to a source range.

### 4. Steward connectedness pressure

Goal: evaluate whether Basis records help a simple spec-code retrieval task in [[spec-dataset-evolution-research-project]] / Steward.

Acceptance:

- BM25/path baseline exists;
- Basis features are compared against the baseline;
- no model training until baseline and hard negatives exist.

## No-go criteria

Stop or redesign if:

- accepted Basis state is indistinguishable from model output;
- UI state becomes canonical;
- `.basis` run artifacts are published raw;
- a benchmark claim lacks a baseline;
- semantic labels are generated by deterministic framework code instead of explicit model/human packets;
- hidden prompts/logs/evaluator material leak into public docs.

That is the useful discipline. The project is promising because it already knows what not to make authoritative.
