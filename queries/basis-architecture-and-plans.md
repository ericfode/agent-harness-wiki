---
title: Basis Architecture and Plans
created: 2026-05-10
updated: 2026-05-10
type: query
tags: [formal-methods, context-engineering, work-management, code-quality, safety]
sources: [raw/articles/basis-project-deep-dive-2026-05-10.md, queries/basis-project-index.md, queries/nightly-src-projects-desk-2026-05-10.md]
---

# Basis Architecture and Plans

## Architecture thesis

Basis should not be a clever Markdown transformer. It should be a custody system for specification state.

The core pattern is:

```text
source prose / surrounding artifacts
        │
        ▼
source topology: files, sections, ranges, hashes
        │
        ▼
proposed semantic records: claims, constraints, assumptions, interfaces
        │
        ▼
validation, critique, pressure, open questions, target verdicts
        │
        ▼
explicit human/model acceptance boundary
        │
        ▼
accepted Basis state
        │
        ▼
projections: Markdown, code plans, tests, proofs, dashboards, runbooks
```

This is why the project belongs near [[formal-methods-for-agent-harnesses]], [[evaluation-and-review-loops]], and [[context-engineering]]. It is not formal verification yet; it is a way to keep specification claims from evaporating into chat residue.

## Surfaces

| Surface | Implementation language | Current responsibility | Desired boundary |
|---|---|---|---|
| Core `basis` | Elixir/BEAM | live reducer/imaginer runtime, source topology, server, UI projection | authoritative event/run model and accepted-state transitions |
| `basis-hermes` | Python + dashboard JS | deterministic Hermes tool/plugin bridge | fast local reduction/validation and dashboard inspection |
| `basis-jcode` reducer | Node/Jcode | headless model-worker control plane, ledger, validation, dashboard decisions | experiment lane for recursive/model-assisted Basis generation |
| `steward` | Python design seed | benchmark/governance pressure | external evaluator and spec-code grounding dataset |

## Core Basis plan

The core Elixir repo should converge toward smaller named boundaries. Current evidence shows `lib/basis/run/server.ex` owns too many responsibilities at once. The desired split is not framework ceremony; it is semantic hygiene.

Near-term plan:

1. Fix the formatter gate in `lib/basis/run/server.ex`.
2. Split live-run responsibilities into explicit modules:
   - source topology;
   - context packet construction;
   - provider adapter events;
   - proposed-record lifecycle;
   - intervention events;
   - projection building;
   - accepted-state transition.
3. Preserve append-only event logs as run authority.
4. Keep browser UI as projection/command surface, not semantic authority.
5. Add tests around each boundary before expanding behavior.

No-go criterion: if a patch makes generated prose, UI cache, or raw provider output silently authoritative, it is not Basis work. It is decorative entropy.

## Hermes bridge plan

`basis-hermes` is currently the cleanest integration surface. It should stay deliberately modest:

- deterministic reducer first;
- packet validator first;
- provider-facing tool schemas kept Codex-compatible;
- richer semantic claims represented as proposals, not truth;
- dashboard loopback-bound unless explicitly secured.

Near-term plan:

1. Keep `basis_reduce_spec` and `basis_validate_packet` stable as Hermes tool contracts.
2. Add small golden examples over public/synthetic specs.
3. Export artifacts with stable IDs and source hashes.
4. Keep schema constraints simple at provider boundary; enforce cross-field logic at runtime.
5. Keep dashboard routes local-file-capable but documented as local-only.

This surface should be the agent-facing handhold for [[hermes-agent]]. It does not need to become the whole cathedral.

## Jcode control-plane plan

`basis-jcode` is the richest experiment, because it tests the full reducer/control-plane story: worker packets, production provenance, validation, convergence judgement, UI attention, questions, and acceptance decisions.

Near-term plan:

1. Resolve dirty tracked deletions in the repo.
2. Decide whether the ten ahead-of-origin commits should become the new canonical reducer branch.
3. Keep `.basis/self-convergence` private until packet bodies and dashboard payloads are reviewed.
4. Extract a public-safe run summary generator that emits only counts, statuses, validation results, and caveats.
5. Define a rule for promoting accepted records out of `.basis` into durable state.

The key architectural rule is already right: deterministic framework code routes, validates, and materializes declared decisions. It does not invent semantics. Semantic labels must come from source-backed model or human packets with falsifiable witnesses.

## Steward and benchmark pressure

`steward` should be used as external pressure on Basis, not as another name for it. Steward asks whether specs connect to code, tests, diffs, and stale-surface signals. Basis asks how to represent specification meaning once such evidence exists.

Useful integration path:

1. Steward creates spec-code grounding examples.
2. Basis reduces selected specs into proposed records.
3. Steward evaluates whether those records improve retrieval, stale-spec detection, or update prediction.
4. Failed examples become Basis pressure tests rather than anecdotes.

That is the clean order. Benchmark first, metaphysics later.

## Open design questions

| Question | Current stance |
|---|---|
| Is Markdown canonical? | No. Markdown is bootstrap input and review projection. |
| Is a reducer packet accepted state? | No. It is proposed state until an explicit acceptance record. |
| Should Lean own live orchestration? | No. Lean may project accepted claims and proof obligations; live context custody belongs in the runtime. |
| Should Jcode worker outputs be public? | Not by default. Counts and structure may be public; packet/log bodies require review. |
| Should Basis depend on LLM semantic correctness? | No. It should depend on provenance, witnesses, validation, review, and acceptance boundaries. |

## Immediate next slice

The best next engineering slice is small:

```text
core-basis-format-and-boundary-split
```

Acceptance gates:

- `mise exec -- mix format --check-formatted` passes;
- `mise exec -- mix test` passes;
- `mise exec -- mix compile --warnings-as-errors` passes;
- one responsibility moves out of `Basis.Run.Server` behind tests;
- no UI or provider output becomes authoritative.

A tiny proof of taste, as it were.
