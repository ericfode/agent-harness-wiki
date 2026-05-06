---
title: Nightly Src Projects Desk Raw Survey (2026-05-06)
author: local multi-agent survey synthesis
url: file:///Users/ericfode/src
ingested: 2026-05-06
---

# Nightly Src Projects Desk Raw Survey (2026-05-06)

This raw note preserves the public-safe basis for the 2026-05-06 nightly `src/` projects desk. It is evidence-first and deliberately leaky only in the engineering sense: it says what could be inspected, what was held back, and where the public page should not pretend to know more than the files do.

## Survey scope and method

- Survey root: `/Users/ericfode/src`
- Survey timestamp: 2026-05-06 01:36 PDT
- Coverage: 38 top-level directories, including hidden/scratch directories.
- Execution shape: exactly 10 top-level Hermes survey lanes, dispatched as 6 + 4. This preserved the required ten lanes without betting the night on a concurrency semaphore.
- Recursive shape: all 10 lane summaries reported recursive delegation available, attempted, and succeeded: each lane split into purpose/docs, live-work evidence, and safety/public-summary eligibility, with further 3-way leaf splits where useful. The parent synthesis treats those as lane self-reports and relies only on inspectable repo evidence in the final page.
- Evidence allowed: README/docs/plans, project manifests, branch/status/log metadata, safe modified/untracked filenames, mtimes, tests, checked-in reports, and visible artifacts.
- Evidence excluded: secret contents, `.env` contents, local settings contents, raw prompt/log/trajectory material, hidden evaluator/supervisor payloads, private corpus bodies, explicit/provocative material, and directories too skeletal for a responsible public claim.
- Illustration: the configured image backend failed with missing `FAL_KEY`; the page therefore uses a generated local SVG editorial illustration under `queries/news-assets/`. It is symbolic art, not a screenshot.

## Ten survey lanes, safety-filtered

1. Hidden local agent settings; clean public tinygrad checkout; early Lean-backed harness scaffold; one sensitive social-claim notebook withheld.
2. `basis`; `basis-hermes`; `basis-jcode`; `cardgame1` / Dungeon Steward.
3. Empty `creative`; `deer-flow`; `FACEMUSIC`; `gas-city-but-its-just-codex`.
4. `gemma4-tinygrad-opt`; `handterm`; `hoid`; `is-codex-better`.
5. `is-it-formal`; `justfooln`; `kettlebellsim`; skeletal `kimi-tests`.
6. Local `langfuse` deployment folder; local Hermes GGUF runner; `meta-hermes`; `nnpl-external-latent-bus`.
7. `nnpl-shared-bus`; `nnpl-typed-boundary-ir`; `openai-symphony`; empty `overengineeredlife`.
8. `silly-pi-stuff`; private `spec-dataset-evolution-corpus`; skeletal nested `src`; `steward`.
9. `testing-rl`; `testing-rl-hermes`; empty `tinygrad`.
10. `tinygrad-gemma`; empty `tinygrad-gemma-gemini`; `tinygrad-gemma-kimi`.

## Public-safe lead candidates

### Basis and spec-code grounding cluster

- `basis` evidence: `spec.md`, `AGENTS.md`, `mix.exs`, `components/spec-basis-reducer/spec.md`, and tests under `test/basis/`. Git branch `main`; recent commits include `8e81759` resetting the reducer implementation to spec and `92f7eaf` revising the core boundary/purpose. Worktree is dirty with modified reducer spec and untracked Elixir app/test/UI files.
- `basis-hermes` evidence: `README.md`, `plugin.yaml`, `pyproject.toml`, `dashboard/manifest.json`, dashboard API files, reducer component docs, and tests. Git branch `main`; clean at `0061d3261329`, whose commit message records Codex-compatible Basis tool schemas. Safe summary: Hermes plugin/dashboard exposing deterministic reducer and validator tools for Basis packets.
- `basis-jcode` evidence: `spec.md`, `components/spec-basis-reducer/README.md`, reducer `spec.md`, package manifest, and orchestration/dashboard tests. Git branch `main`; dirty with tracked deletions in examples/UI. Safe summary: Jcode-native reducer control-plane work; raw packets, prompts, ledgers, event streams, and local run surfaces withheld.
- `steward` evidence: `README.md`, `pyproject.toml`, and design docs including project charter, benchmark spec, architecture, implementation plan, data governance, modeling roadmap, and product workflows. Git branch `main`; clean at `ba88837` with README stating design/ideation only and no production code yet. Safe summary: early local-first spec-code grounding project.
- `spec-dataset-evolution-corpus` is intentionally private by README and clean at `4659608`; public use is metadata/source-boundary only, not raw corpus publication.

### Test-writing environments

- `testing-rl` evidence: `README.md`, `SPEC.md`, `pyproject.toml`, docs for dashboard/artifact schemas/environment/counterfactual verifier/Hermes adapter, Lean formalization files, Python environment/replay/sidecar code, and tests. Git branch `master` tracking `origin/master`; dirty. Recent commit `139cea4` publishes the project surface; safe modified/untracked filenames point at workflow/docs/scripts plus a recent-data page/render/test surface.
- `testing-rl-hermes` evidence: `MASTER_PLAN.md`, `pyproject.toml`, `ADVERSARIAL_RISK_REVIEW.md`, docs for test-generation environment/history fixtures/verifiable properties, testgen source, and tests. Git branch `main`; clean. Recent commits on 2026-05-01/02 add test-generation RL environment, history materialization, and inverse-fix history mutants.
- Public summary basis: software-testing environments remain a front-page theme, but evaluator/reference/oracle/hidden-answer details are category-only.

### Tinygrad, Gemma, and NNPL benches

- `.tinygrad_research` is a clean public tinygrad checkout on `master`, with README, MIT license, `pyproject.toml`, docs, tests, and recent upstream commits around FP8 llama quantization, shapes/range/special handling, and one-hot helpers.
- `tinygrad-gemma` evidence: README and `pyproject.toml` for a native tinygrad Gemma 4 implementation, CLI/chat scripts, tests, benchmark files, and 2026-05-05 assistant/MTP plans. Git branch `main`, ahead of origin by 73 commits, with no tracked changes and many untracked benchmark/progress/log-style artifacts. Safe claim: assistant/MTP scaffolding and evaluation design are active; throughput/speculative-decode claims are explicitly not made.
- `tinygrad-gemma-kimi` is an undocumented dirty `opt/attention` local optimization repo with attention/JIT/correctness/validation filenames and patch artifacts. High-level only.
- `gemma4-tinygrad-opt` is a non-root-git Gemma/tinygrad optimization workspace with nested clean tinygrad checkout, scripts, and generated/log/prompt artifacts. High-level only.
- NNPL evidence: `nnpl-external-latent-bus`, `nnpl-shared-bus`, and `nnpl-typed-boundary-ir` have docs, Python manifests/source/tests, and public-safe methodological claims around external/internal latent buses, a reported negative shared-bus v0 result, and typed boundary IR. Raw results, traces, rollouts, metrics, and checkpoints are withheld.

### Craft, interface, and game benches

- `handterm` is the cleanest ordinary public-facing project tonight: Rust Wayland-native terminal emulator, MIT license, README, Cargo metadata, clean `master` at `977e709`, and recent commits refactoring kitty graphics/upload helper state.
- `cardgame1` / Dungeon Steward remains a clean Godot 4.6 browser-first roguelite deckbuilder project on `hermes/combat-stage-art-fallback-upstream`, with deterministic-runtime ADR, GDD docs, sprint/planning docs, smoke/simulation/determinism tests, and recent combat-stage/deck-presentation work.
- `FACEMUSIC` is dirty but coherent: browser face-control/music-engine files, iOS camera/control files, Rust package metadata, browser/iOS docs, and new offline expression-forecasting ML package files. Public summary is face-expression musical control semantics; capture/session/model specifics are withheld.
- `kettlebellsim` is high-level only: Python simulation-first kettlebell swing biomechanics/RL toolkit with docs, tests, planning artifacts, probe/training scripts, and rollout media; remote-compute, experiment-tracking, and secret-reference details withheld.
- `hoid` is high-level only: worldbuilding/narrative tooling corpus with docs, Go/TypeScript/Lean surfaces, tests, and many unpublished creative/generated artifacts. Story/canon/music/comic details are not public desk copy.

### Orchestration and harness side rooms

- `openai-symphony`: README/spec/Elixir docs describe a trusted-environment engineering preview for coding-agent orchestration over isolated workspaces, status dashboards, Codex app-server sessions, logging, and token accounting. Branch `main` tracks origin; dirty tracked work touches app-server/orchestrator/status/dashboard/presenter code and tests.
- `gas-city-but-its-just-codex`: Rust/Codex orchestration-control-plane research prototype with workflow-ledger specs, templates/schemas, MCP/gRPC/app-server surfaces, operator tooling, context boards, and Lean formalization. Dirty branch; raw state/log/transcript/verifier/vendor/sandbox material withheld.
- `deer-flow`: public docs/manifests support a high-level LangGraph/LangChain agent-harness summary, but local Flox/config/deployment state keeps it side-room.
- `another-harness`, `is-it-formal`, `is-codex-better`, `justfooln`, `meta-hermes`, local `langfuse`, local Hermes GGUF runner, and `silly-pi-stuff` were inspected and kept to high-level or category-only treatment according to maturity and privacy risk.

## Held back from project-specific public detail

The survey fully held back, or reduced to category-only mention, material from 13 top-level directories. Reasons included local hidden agent settings, a sensitive social/reputational notebook, empty directories, skeletal hidden workflow folders, private corpus contents, local deployment or model-runner configuration, missing README/docs/manifests, uncommitted zero-commit scaffolds, raw logs/trajectories/prompts, benchmark answer-key/evaluator-like materials, generated artifacts, and creative material needing human publication review.

This is a public-safety filter, not a claim that nothing is there. The desk can report that a room was surveyed without publishing the contents of the drawers.

## Editorial synthesis

The public-safe movement tonight clusters around five themes:

1. specification state and spec-code grounding are becoming first-class artifacts (`basis`, `basis-hermes`, `basis-jcode`, `steward`);
2. software-testing environments are preserving replay/evidence boundaries rather than presenting benchmarks as magic (`testing-rl`, `testing-rl-hermes`);
3. model-internals benches are using boundaries, baselines, and withheld performance claims (`tinygrad-gemma`, NNPL, Gemma/tinygrad sandboxes);
4. craft projects continue to make feel and interface surfaces inspectable (`handterm`, Dungeon Steward, `FACEMUSIC`, `kettlebellsim`);
5. orchestration projects are externalizing state into ledgers, workspaces, dashboards, and formal/control-plane surfaces (`openai-symphony`, `gas-city-but-its-just-codex`, DeerFlow).

The theme is not a product launch. It is better than that, in the limited but respectable sense: more of the work is acquiring checkable shape.
