---
title: Basis Project Deep Dive Evidence (2026-05-10)
author: Hermes local repo inspection
url: file:///Users/ericfode/src/basis
ingested: 2026-05-10
---

# Basis Project Deep Dive Evidence (2026-05-10)

This raw note preserves the public-safe inspection basis for the local Basis project cluster. It summarizes repo metadata, safe filenames, architectural surfaces, tests, and publication boundaries. It deliberately does not publish `.basis` run bodies, prompts, raw packets, event streams, stderr logs, private corpus material, local dashboard payloads, or secrets.

## Scope

The inspection treated Basis as a cluster of three active surfaces:

| Surface | Local path | Role | Public posture |
|---|---|---|---|
| Core Basis | `/Users/ericfode/src/basis` | Elixir/BEAM reducer runtime and specification-state experiment | Public-safe architecture and gate summary |
| Basis Hermes | `/Users/ericfode/src/basis-hermes` | Hermes plugin and dashboard bridge exposing deterministic reducer/validator tools | Public-safe integration summary |
| Basis Jcode | `/Users/ericfode/src/basis-jcode/components/spec-basis-reducer` | Jcode-native headless reducer/control-plane experiment with `.basis` run ledgers | Architecture and counts only; raw run state withheld |

Existing wiki context came from [[queries/nightly-src-projects-desk-2026-05-10|nightly-src-projects-desk-2026-05-10]], [[queries/nightly-src-projects-desk-2026-05-09|nightly-src-projects-desk-2026-05-09]], [[queries/nightly-src-projects-desk-2026-05-08|nightly-src-projects-desk-2026-05-08]], [[spec-dataset-evolution-research-project]], and [[spec-deep-dive-index]].

## Core Basis evidence

Observed repository state:

```text
path: /Users/ericfode/src/basis
branch: main...origin/main
HEAD: a5544e0 Split reducer UI into separate app entrypoints
working tree: clean
```

Recent commits inspected:

```text
a5544e0 Split reducer UI into separate app entrypoints
031340a Integrate implementation imaginer merge
5f2dd8b Add implementation imaginer runtime
8e81759 Reset reducer implementation to spec
92f7eaf Revise spec for basis core boundary and purpose
```

Key safe files:

```text
spec.md
mix.exs
mise.toml
docs/codex-environment.md
components/spec-basis-reducer/spec.md
components/implementation-imaginer/spec.md
components/implementation-imaginer/experiments/2026-05-05-plan-space-search.md
lib/basis/application.ex
lib/basis/source.ex
lib/basis/run/server.ex
lib/basis/web/server.ex
lib/mix/tasks/basis.server.ex
test/basis/source_test.exs
test/basis/run/server_test.exs
test/basis/llm/app_server_provider_test.exs
```

Observed gates:

| Gate | Result | Notes |
|---|---:|---|
| `mise exec -- mix test` | pass | `4 tests, 0 failures` |
| `mise exec -- mix compile --warnings-as-errors` | pass | compile exit 0 |
| `mise exec -- mix format --check-formatted` | fail | one formatting issue in `lib/basis/run/server.ex` around `interventions/1` |

Architecture summary: core Basis is an Elixir/BEAM project for reducing prose/spec artifacts into structured, provenance-backed specification state. Its normative spec says raw model output, projection output, and chat transcripts must not become authoritative state without explicit acceptance. The current implementation centers on source sectioning, run ownership, model-provider boundaries, HTTP/SSE projection, reducer and imaginer modes, and browser projections.

Main pressure: the runtime is moving in the right direction but still has large cross-cutting files. `lib/basis/run/server.ex` owns too much of the live run model, jobs, context packets, provider streams, proposed records, interventions, and projections. The project's own contract prefers explicit boundaries: accepted state before projections, event logs before mutable UI state, provenance before confidence, proposal before acceptance.

## Basis Hermes evidence

Observed repository state:

```text
path: /Users/ericfode/src/basis-hermes
branch: main
HEAD: 0061d32 fix: make basis tool schemas codex-compatible
working tree: clean
installed clone: /Users/ericfode/.hermes/plugins/basis
```

Observed gates:

| Gate | Result | Notes |
|---|---:|---|
| `uv run --extra dev pytest -q` | pass | `15 passed in 0.08s` |
| `cd components/spec-basis-reducer && npm test` | pass | `4 tests`, `4 pass` |

Key safe files:

```text
README.md
plugin.yaml
pyproject.toml
__init__.py
basis_core/reducer.py
basis_core/models.py
basis_core/io.py
basis_core/tool_handlers.py
basis_core/cli.py
dashboard/manifest.json
dashboard/plugin_api.py
dashboard/dist/index.js
dashboard/dist/style.css
components/spec-basis-reducer/spec.md
```

Plugin surface:

| Surface | Purpose |
|---|---|
| `basis_reduce_spec` | Reduce Markdown into proposed Basis records, section provenance, pressure findings, target verdicts, and validation artifacts |
| `basis_validate_packet` | Validate an inline or file-backed Basis packet |
| `hermes basis reduce` | CLI wrapper for local operation |
| `/basis` | Slash-command help surface |
| Hermes dashboard tab `Basis` | Local UI for reduction, validation, records, verdicts, and packet JSON |

The notable operational scar is useful: an earlier schema used top-level combinators that Codex/OpenAI tool validation rejected. Commit `0061d32` made the tool schemas Codex-compatible by keeping the provider-facing schema object-shaped and enforcing cross-field requirements at runtime. This belongs in the public history because it directly affects Hermes reliability.

## Basis Jcode evidence

Observed repository state:

```text
path: /Users/ericfode/src/basis-jcode
branch: main...origin/main [ahead 10]
HEAD: 4b1e621
origin/main: 345b40d
worktree: dirty tracked deletions in reducer example/UI files
```

Dirty tracked paths observed:

```text
D components/spec-basis-reducer/examples/gas-city-prior-art.md
D components/spec-basis-reducer/examples/symphony-reference-comparison.md
D components/spec-basis-reducer/ui/index.html
```

Observed gate:

```text
cd components/spec-basis-reducer && npm test
26 tests, 26 pass
```

Important public-safe source files:

```text
components/spec-basis-reducer/README.md
components/spec-basis-reducer/spec.md
components/spec-basis-reducer/package.json
components/spec-basis-reducer/src/cli.mjs
components/spec-basis-reducer/src/reducer.mjs
components/spec-basis-reducer/src/dashboard-server.mjs
components/spec-basis-reducer/src/ledger/run-ledger.mjs
components/spec-basis-reducer/src/jcode/plan.mjs
components/spec-basis-reducer/src/jcode/executor.mjs
components/spec-basis-reducer/src/orchestration/convergence-loop.mjs
components/spec-basis-reducer/src/packets/contracts.mjs
components/spec-basis-reducer/src/validation/validate-run.mjs
components/spec-basis-reducer/src/ui/ui-model.mjs
components/spec-basis-reducer/src/acceptance/acceptance.mjs
components/spec-basis-reducer/tests/*.mjs
```

Jcode-native reducer architecture:

- deterministic code reads source material and computes hashes;
- builds section manifests and worker prompts;
- maintains an append-only run ledger;
- validates worker, synthesis, convergence, and human packets;
- synthesizes proposal-only Basis packets from explicit model or human packets;
- computes UI projections and structural attention over explicit packet references;
- writes accepted-state changes only through a separate acceptance boundary.

Current `.basis` run inventory was inspected by names and counts only:

| Run | Status | Safe observed shape |
|---|---|---|
| `.basis/self-convergence` | live/active experiment surface | 383 files, including 69 worker packets by filename, 75 logs, 74 NDJSON streams, 74 prompt text files, output names `basis-packet.json`, `validation.json`, `ui-model.json`, `convergence-judgement.json` |
| `.basis/smoke` | fixture smoke run | 13 files, fixture packets and validation/UI outputs |

Dashboard surface:

```text
127.0.0.1:5177 listening via node PID 97180
command includes: src/cli.mjs dashboard --run .../.basis/self-convergence --host 127.0.0.1 --port 5177 --open
```

The dashboard is useful but public-sensitive: `GET /api/state` loads run state, and `POST /api/decision` writes acceptance decisions. It is loopback-bound in the observed process, but there is no inspected auth layer. Do not publish dashboard payloads.

## Public-safety boundary

Allowed public evidence:

- repo names and local paths;
- commit hashes, branch/ahead/dirty summaries;
- safe filenames and module responsibilities;
- test and lint outcomes;
- `.basis` run names/counts and output filenames;
- architecture synthesis and caveats.

Excluded evidence:

- `.basis` raw run trees;
- prompt text;
- NDJSON event bodies;
- stderr/stdout log bodies;
- worker packet bodies;
- validation bodies;
- local dashboard `/api/state` payloads;
- private corpus bodies;
- secrets, credentials, or local service configuration.

## Current status summary

| Area | Current state | Honest verdict |
|---|---|---|
| Core Basis | clean repo, tests and compile pass, format gate red | promising core with one small gate failure and large-module pressure |
| Basis Hermes | clean repo, Python and JS tests pass, installed clone synced | best current integration surface |
| Basis Jcode | ahead 10, dirty deletions, tests pass, dashboard alive | richest experiment surface; needs cleanup and publication fence |
| Self-convergence experiment | `.basis/self-convergence` exists with many run artifacts | active but private; summarize counts only until reviewed |
| Steward relation | separate docs-first benchmark project exists | useful next empirical pressure, not yet Basis runtime evidence |
