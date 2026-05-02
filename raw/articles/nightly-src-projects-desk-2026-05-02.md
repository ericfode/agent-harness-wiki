---
title: Nightly Src Projects Desk Raw Survey (2026-05-02)
author: local multi-agent survey synthesis
url: file:///Users/ericfode/src
ingested: 2026-05-02
---

# Nightly Src Projects Desk Raw Survey (2026-05-02)

This raw note preserves the public-facing basis for the 2026-05-02 nightly `src/` projects desk. It intentionally keeps the evidence layer compact and safe to publish; deeper local material that looked explicit-tagged, secret-bearing, internal-only, private, or too skeletal remains omitted.

## Survey scope and method

- Survey root: `/Users/ericfode/src`
- Survey date: 2026-05-02
- Coverage: 27 top-level directories under `src/`
- Execution shape: exactly 10 top-level Hermes survey lanes. The runtime rejected a single 10-task batch because `max_concurrent_children` was 6, so the lanes ran as two batches of five while preserving exactly ten top-level lanes.
- Recursive shape: every lane reported that deeper `delegate_task` was available and used. Lanes split into purpose/docs, live-work evidence, and safety/public-summary eligibility; their children reported further three-way per-directory recursion where available. The summaries were then synthesized here.
- Evidence allowed: local README/docs, package/project files, git status, branch names, recent commits, modified/untracked file names, mtimes, plans, and visible artifacts.
- Evidence excluded: secrets, private deployment details, hidden personal/runtime prompt details, raw explicit/provocative content, and insufficiently evidenced skeleton directories.

## Ten survey lanes

1. `another-harness`, `are-the-astrological-signs-rascist`, `cardgame1`
2. `deer-flow`, `FACEMUSIC`, `gas-city-but-its-just-codex`
3. `gemma4-tinygrad-opt`, `hoid`, `is-codex-better`
4. `is-it-formal`, `justfooln`, `kettlebellsim`
5. `kimi-tests`, `langfuse`, `local-hermes`
6. `meta-hermes`, `nnpl-external-latent-bus`, `nnpl-shared-bus`
7. `nnpl-typed-boundary-ir`, `overengineeredlife`, `silly-pi-stuff`
8. `src`, `testing-rl`, `testing-rl-hermes`
9. `tinygrad`, `tinygrad-gemma-gemini`
10. `tinygrad-gemma-kimi`

## Public-safe lead candidates

### `testing-rl`
- Evidence: `README.md`, `pyproject.toml`, `docs/environment-contract.md`, `docs/software-risk-model.md`, `docs/counterfactual-testing-history.md`, `docs/counterfactual-verifier.md`, `docs/non-cheating-test-writer.md`, `docs/lean-verification.md`, `docs/alternative-test-history.md`, `testing_rl/*.py`, `tests/`, `benchmarks/python/*.json`, `formal/lakefile.lean`, `formal/TestingRL.lean`, `formal/TestingRL/Plan.lean`.
- Git: not a git worktree, so branch/commit/status evidence was unavailable.
- Live signal: 2026-05-01 mtimes on Lean/formal docs, README, alternative-test-history docs, CLI/events code, and tests.
- Public summary basis: a Python/Lean RL environment for training agents to write tests that expose defects, with risk modeling, counterfactual history, and formal structural checks.

### `FACEMUSIC`
- Evidence: `docs/browser-instrument-architecture.md`, `ios/FACEMUSICNative/README.md`, `web/package.json`, `ml/README.md`, `ml/pyproject.toml`, `ml/configs/expression_forecast_v0_500ms.json`, `Cargo.toml`.
- Git: branch `main`, HEAD `f6cf6cf`; recent commits include native camera/platform hardening, iOS native camera control source, and browser face-control/stage UI stabilization.
- Live signal: dirty worktree with about 30 entries across browser docs, iOS native files, web face-control/music-engine files, styling, and a new ML training stack; latest status mtime around 2026-04-20.
- Public summary basis: face-controlled music instrument joining browser, iOS, audio, visual, and forecasting work. Session/capture identifiers omitted.

### `cardgame1` / Dungeon Steward
- Evidence: `project.godot`, `design/gdd/game-concept.md`, `prototypes/core-loop/README.md`, `docs/WORKFLOW-BALANCE-SIM.md`, `docs/engine-reference/godot/VERSION.md`, `LICENSE`.
- Git: branch `hermes/combat-stage-art-fallback-upstream`, status clean; recent commit `a9a8ef6` hardens combat-stage art presentation and asset fallbacks; adjacent commits cover map viewer, floor-one layout, and hover behavior.
- Live signal: recent balance artifact / cache mtimes after the latest commit.
- Public summary basis: Godot 4.6-era browser-first roguelite deckbuilder prototype emphasizing deterministic combat presentation, deck/run legibility, and balance tooling.

### `gas-city-but-its-just-codex`
- Evidence: `README.md`, `Cargo.toml`, crate manifests, `apps/operator-ui-macos/Package.swift`, `docs/project-formalization.md`, `docs/requirements/control-plane-requirements.md`, `docs/architecture/current-control-plane-architecture.md`, `docs/implementation/implementation-map.md`, `docs/evidence/correctness-evidence.md`, `formal/README.md`, `formal/lakefile.toml`.
- Git: branch `codex/native-codex-ui`, HEAD `198aefc`; recent commits include Harbor task-level transfer reporting, native sandbox relaunch/operator wiring, and UI showcase workflow templates.
- Live signal: very dirty worktree, concentrated in docs, state/config, scripts, schemas, templates, and limited Rust source areas; local/session/runtime details omitted.
- Public summary basis: Rust Codex-native orchestration/control-plane workspace with graph ledger, operator surfaces, templates, benchmarks, and formal evidence artifacts. Operational runbook/state details withheld.

### NNPL research cluster
- `nnpl-external-latent-bus`: evidence from `README.md`, `PROJECT_BRIEF.md`, `pyproject.toml`, architecture/space/hypothesis/benchmark docs, source, tests, and report artifacts; no git metadata. It tests an external latent bus versus matched baselines.
- `nnpl-shared-bus`: evidence from `README.md`, `PROJECT_BRIEF.md`, architecture/hypothesis/benchmark docs, run summaries, configs, source, and trace artifacts; no git metadata. It records a negative shared-bus result against preregistered gates.
- `nnpl-typed-boundary-ir`: evidence from `README.md`, `PROJECT_BRIEF.md`, `pyproject.toml`, architecture/IR/hypothesis docs, source/tests, `results/bakeoff.json`, and tinygrad comparison results; no git metadata. It focuses on typed boundary artifacts, validation, rendering, and auditability.

## Research bench / side-room candidates

- `another-harness`: Lean-backed agent-harness R&D prototype with no valid `HEAD` commit and an untracked initial tree. Public-safe at high level as work-object/evaluator/resume/formal-semantics exploration; local MCP/config/run details omitted.
- `deer-flow`: public LangGraph/Next.js/Python super-agent harness checkout with dirty local deployment/config artifacts. Public docs/source are usable, but local config is not.
- `gemma4-tinygrad-opt`: local tinygrad Gemma optimization workbench with benchmark/Metal/generation scripts, package exports, and current-night artifacts. No git/root README; local logs/prompts/deployment details omitted.
- `is-codex-better`: unborn Git workbench for Codex-native harness plugins: repo loops, specialist fanout, Honcho memory, transcript recall, checkpoints, jobs, and procedure promotion. Public-safe if framed as uncommitted/partially proven.
- `is-it-formal`: Lean 4 + Python scaffold for grading claim formality, with JSON examples and deterministic CLI. No commits yet; public-safe as a prototype.
- `justfooln`: research-and-benchmark workspace for long-horizon/tool-heavy agent harness work. Not a git repo; artifact-heavy and suitable only as a bench note.
- `local-hermes`: local llama.cpp / GGUF serving setup for Hermes 4.3 36B. Public-safe only generically; no model artifact details needed.
- `src`: game-development workflow/skill bundle under hidden agent-skill paths. Public-safe only as high-level process tooling.
- `silly-pi-stuff`: private-marked Pi-extension sandbox plus octonion-surface browser experiment. Public-safe only as a side-room mention; hidden local prompt/config material omitted.
- `tinygrad-gemma-kimi`: Git repo on `opt/attention` for Gemma/tinygrad optimization racing. Dirty tree with patches, reject/backups, caches, local deployment hints, and local result artifacts; summarize only as an unpolished side-room sandbox.

## Held back from the public page

The following directories were surveyed but not described in project-specific public detail:

- `are-the-astrological-signs-rascist` — sensitive identity/reputational research material; only generic omission is appropriate.
- `hoid` — mixed creative-worldbuilding material with explicit-tagged/local/internal risk; needs curated subset before public summary.
- `kettlebellsim` — clear simulation purpose, but local docs/artifacts include internal operational and credential-management references; hold back until scrubbed.
- `kimi-tests` — skeletal/non-project evidence.
- `langfuse` — credential/private deployment configuration signals.
- `meta-hermes` — top-level scratch/meta wrapper; nested public-ish material is not the assigned root.
- `overengineeredlife` — empty/no substantive evidence.
- `testing-rl-hermes` — internal/Hermes-specific supervisor/evaluator and generated/local material; hold back pending separation.
- `tinygrad` — empty/non-git directory.
- `tinygrad-gemma-gemini` — empty/non-git directory.

## Editorial synthesis

The safe publishable movement tonight clusters around three themes:

1. testing and verification environments for agents (`testing-rl`, `is-it-formal`, parts of `another-harness`);
2. embodied or game-facing interfaces (`FACEMUSIC`, `cardgame1`, selected side-room experiments);
3. honest research benches where failures and boundaries are explicit (`NNPL` cluster, Gemma/tinygrad workbenches, Codex-native orchestration work).

The public page should therefore avoid pretending the tree is a single product line. It is a night desk: a testing lab, an instrument shop, a card table, and several research benches, all sharing the same insistence that claims should survive contact with artifacts.
