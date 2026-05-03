---
title: Nightly Src Projects Desk Raw Survey (2026-05-03)
author: local multi-agent survey synthesis
url: file:///Users/ericfode/src
ingested: 2026-05-03
---

# Nightly Src Projects Desk Raw Survey (2026-05-03)

This raw note preserves the public-safe basis for the 2026-05-03 nightly `src/` projects desk. It is deliberately compact: the source tree was inspected as local evidence, not mined for publishable secrets. Names or details that would create a public-safety leak are withheld or reduced to category-level descriptions.

## Survey scope and method

- Survey root: `/Users/ericfode/src`
- Survey timestamp: 2026-05-03 01:36 PDT
- Coverage: 30 top-level directories, including hidden/scratch directories.
- Execution shape: exactly 10 top-level Hermes survey lanes. A first all-at-once 10-task dispatch was rejected by the runtime because `max_concurrent_children` was 6; the real survey therefore ran as two batches, 6 lanes plus 4 lanes, preserving exactly 10 top-level survey lanes.
- Recursive shape: the completed lanes reported orchestrator-style project splits and focused passes over purpose/docs, live-work evidence, and public-summary safety. Most lanes reported deeper `delegate_task` use; one child was handled directly by its project worker, and parent lanes spot-verified with local tools. No lane output is treated as magic; all synthesis below is based on filenames, docs, git metadata, and visible artifacts.
- Evidence allowed: README/docs/plans, project manifests, git branch/status/log/diff metadata, modified/untracked filenames, mtimes, tests, run summaries, and visible artifacts.
- Evidence excluded: secret contents, `.env` contents, local settings contents, raw prompt/log/trajectory material, hidden evaluator/supervisor payloads, explicit/provocative material, and directories too skeletal to support a public claim.

## Ten survey lanes, safety-filtered

1. Hidden local agent configuration; public tinygrad checkout; Lean-backed harness prototype.
2. Sensitive reputational/social-claim notebook withheld; Dungeon Steward / `cardgame1`; empty creative scratch directory.
3. `deer-flow`; `FACEMUSIC`; `gas-city-but-its-just-codex`.
4. `gemma4-tinygrad-opt`; mixed creative-worldbuilding suite withheld pending curation; zero-commit Codex plugin workbench withheld.
5. `is-it-formal`; `justfooln`; `kettlebellsim`.
6. Skeletal local test directory withheld; local `langfuse` compose stack; `local-hermes` GGUF runner.
7. `meta-hermes` wrapper with nested Gas City checkout; `nnpl-external-latent-bus`; `nnpl-shared-bus`.
8. `nnpl-typed-boundary-ir`; `openai-symphony`; empty `overengineeredlife` scratch directory.
9. `silly-pi-stuff`; hidden `cardgame1` skill bundle under `src`; `testing-rl`.
10. `testing-rl-hermes`; empty tinygrad scratch directories; `tinygrad-gemma-kimi`.

## Public-safe lead candidates

### Test-writing environments: `testing-rl` and `testing-rl-hermes`

- `testing-rl` evidence: `README.md`, `SPEC.md`, `WORKFLOW.md`, `pyproject.toml`, `docs/project-dashboard.md`, `docs/artifact-schemas.md`, `docs/counterfactual-verifier.md`, `docs/environment-contract.md`, `docs/software-risk-model.md`, `docs/lean-verification.md`, `testing_rl/*.py`, `formal/TestingRL/Plan.lean`, and `tests/test_*.py`.
- `testing-rl` git signal: branch `master`, one visible commit `eac91d0 2026-05-02 init`, dirty worktree with 23 tracked modified files and 46 untracked files; current local edits expand replay verification, artifact/training-product schemas, adapters, risk/event mining, and Lean formalization.
- `testing-rl-hermes` evidence: `MASTER_PLAN.md`, `ADVERSARIAL_RISK_REVIEW.md`, `docs/test-generation-rl-environment.md`, `docs/history-to-testgen-fixtures.md`, `docs/good-test-verifiable-properties.md`, `benchmarks/test-generation/README.md`, `src/testing_rl_hermes/testgen/*.py`, and tests.
- `testing-rl-hermes` git signal: branch `main`, clean worktree; recent commits add the test-generation RL environment, history-derived fixtures, and inverse-fix history mutants.
- Public summary basis: the strongest publishable theme is an agent-testing bench moving from broad idea to explicit environment contracts, replay/evidence artifacts, and hidden-evaluator discipline. Supervisor-only benchmark details are not public copy.

### Dungeon Steward / `cardgame1`

- Evidence: `project.godot`, `design/gdd/game-concept.md`, `design/gdd/systems-index.md`, `docs/plans/2026-04-05-combat-fun-roadmap.md`, `docs/plans/2026-04-11-deck-inspection-mvp-plan.md`, `docs/WORKFLOW-BALANCE-SIM.md`, combat-stage and deck-inspection controllers, texture loader, smoke probes, and prototype tests.
- Git signal: branch `hermes/combat-stage-art-fallback-upstream`, clean tree, ahead of `upstream/main` by one commit. Latest commit hardens combat-stage art presentation and asset fallbacks; recent areas include combat stage UI, deck inspection UI, texture loading, smoke probes, and image-generation prompt docs.
- Public summary basis: browser-first Godot roguelite deckbuilder work is currently about legibility and trust: combat-stage art, deck/run presentation, asset fallback behavior, and smoke coverage.

### `FACEMUSIC`

- Evidence: `docs/browser-instrument-architecture.md`, `ios/FACEMUSICNative/README.md`, `web/package.json`, `ml/README.md`, `ml/pyproject.toml`, `ml/configs/expression_forecast_v0_500ms.json`, `Cargo.toml`, browser control/music-engine files, iOS native control files, and offline ML scaffold files.
- Git signal: dirty `main` branch with tracked edits across browser and iOS face-control/conductor/music-engine paths; new untracked ML work adds expression-forecasting data contracts, configs, tinygrad training, TensorBoard visualization, scripts, and plan docs.
- Public summary basis: face-expression-driven music remains a real interface project, now spanning browser, iOS, audio mapping, and forecasting semantics. Raw capture/session details are omitted.

### `gas-city-but-its-just-codex`

- Evidence: `README.md`, `AGENTS.md`, `Cargo.toml`, `docs/usage/research-triangulation.md`, `docs/usage/image-first-codex-loop.md`, `docs/context-boards/README.md`, `docs/specifications/workflow-ledger-specification.md`, templates, schemas, `src/metaharness.rs`, repo-loop gate artifacts, and smoke/validator scripts.
- Git signal: active dirty branch `codex/native-codex-ui`; recent commits cover Harbor transfer reporting, native sandbox relaunch/operator UI wiring, UI showcase templates, and policy-routing semantics.
- Public summary basis: Codex-native orchestration work is centered on workflow-ledger semantics, operator tooling, repo-loop automation, image-first context boards, and research-triangulation workflows. Local state IDs, logs, raw databases, and generated run payloads are omitted.

### `openai-symphony`

- Evidence: `README.md`, `SPEC.md`, `LICENSE`, `NOTICE`, `elixir/README.md`, `elixir/WORKFLOW.md`, logging/token-accounting docs, and Elixir modules for orchestrator, agent runner, workspace, Codex app-server, Linear client, and path safety.
- Git signal: clean `main` tracking `origin/main`; visible shallow HEAD `58cf97d fix(elixir): configure Codex app-server model via config`.
- Public summary basis: an Apache-2.0 engineering-preview agent-orchestration service with an Elixir/OTP reference implementation. The safe wording should not imply production readiness or reveal operational tokens/issue details.

### NNPL research cluster

- `nnpl-external-latent-bus`: docs/source/tests/report artifacts support a public-safe summary of a two-space external/internal latent bus experiment, including output-side bridge probes and matched one-space comparators. No git metadata.
- `nnpl-shared-bus`: docs/configs/tests/run summaries support a public-safe negative-result summary: v0 shared-bus recurrence did not show an honest recurrent advantage over preregistered controls. No git metadata.
- `nnpl-typed-boundary-ir`: docs/source/tests/results support a public-safe summary of typed boundary artifacts, validation, rendering, auditability, and comparison to direct shared-bus baselines. No git metadata.
- Public summary basis: the useful public claim is methodological, not promotional: baselines, boundaries, and negative evidence are being preserved as inspectable objects.

## Research bench and side-room candidates

- `.tinygrad_research`: clean upstream-style public tinygrad checkout on `master`, tracking `origin/master`; recent upstream commits around FP8 llama quantization, shape/range/special handling, `one_hot`, and mock interfaces.
- `another-harness`: initialized git repo on `main` with no commits and hundreds of untracked paths; docs and layout point to Codex/Hermes harness architecture, work-item/evaluator/handoff loops, MCP/control-plane tooling, plugins, and Lean-backed modeling. High-level only.
- `is-it-formal`: new Lean 4 + Python scaffold for grading claim formality across domains, with JSON examples and deterministic CLI; all visible files are untracked and no license was found.
- `justfooln`: non-git research harness plus benchmark ladder for long-horizon/tool-heavy agent evaluation, with a long-autonomous-loops research brief; hidden agent workflows and recursive artifacts make it side-room material only.
- `kettlebellsim`: active branch `codex/reward-audit-and-swing-training`; evidence points to scripted swing templates, cyclic observations, behavior-cloning warm-start, reward/retention diagnostics, and Modal probe/training workflows. Local temp/tool fragments and external secret-handling references keep it high-level only.
- `gemma4-tinygrad-opt`: non-root-git Gemma/tinygrad optimization workspace with nested clean tinygrad checkout, Metal benchmarking/generation scripts, logs/prompts/evolution artifacts. Publish only as a local sandbox.
- `tinygrad-gemma-kimi`: dirty `opt/attention` worktree for Gemma attention/JIT/memory-layout/correctness benchmarking, patch experiments, and result JSON artifacts. No benchmark numbers should be laundered into public claims.
- `local-hermes`: non-git llama.cpp / GGUF runner with helper scripts and a local model artifact; publish only as a generic local serving setup.
- `langfuse`: non-git local self-hosted compose stack with `.env` present; credential-bearing details withheld.
- `meta-hermes`: top-level wrapper around a nested clean Gas City checkout; env-looking material and internal prompt/workflow surfaces mean only a narrow high-level summary is appropriate.
- `silly-pi-stuff`: private-marked Pi companion UI plus an octonion-surface browser cellular automata demo; hidden prompt/config material withheld.
- `src`: hidden game-development workflow/skills bundle for `cardgame1`; filename-derived broad characterization only.

## Held back from project-specific public detail

The survey fully held back, or reduced to category-only omission, material in ten top-level directories. Reasons included sensitive identity/reputational framing, local agent settings, empty/skeletal directories, zero-commit all-untracked work that is not yet responsibly summarizable, local deployment configuration with `.env` signals, mixed creative material requiring curation, and hidden supervisor/evaluator or prompt-bearing workflow surfaces.

This is a public-safety filter, not a lack of inspection. The desk can say a room was surveyed without printing the contents of the drawers.

## Editorial synthesis

The public-safe movement tonight clusters around four themes:

1. test-writing and verification environments becoming explicit workspaces (`testing-rl`, `testing-rl-hermes`, `is-it-formal`, selected `another-harness` surfaces);
2. interface projects spending effort on legibility and embodied control (`cardgame1`, `FACEMUSIC`, `kettlebellsim` at high level);
3. orchestration systems moving state out of transcript fog and into ledgers, workspaces, and policy surfaces (`gas-city-but-its-just-codex`, `openai-symphony`, nested Gas City material);
4. research benches preserving baselines, boundaries, and negative results instead of rounding them into triumphal prose (NNPL, Gemma/tinygrad benches).

That is enough for a public desk. It is also the only style of progress note that does not require clairvoyance, which remains, regrettably, absent from the toolchain.
