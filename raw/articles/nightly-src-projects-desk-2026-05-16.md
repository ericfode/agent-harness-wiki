---
title: Nightly Src Projects Desk Raw Survey (2026-05-16)
author: local multi-agent survey synthesis
url: file:///Users/ericfode/src
ingested: 2026-05-16
---

# Nightly Src Projects Desk Raw Survey (2026-05-16)

This raw note preserves the public-safe basis for the 2026-05-16 nightly `src/` projects desk. It summarizes inspectable local evidence only: README/docs/plans, manifests, branch/status/log metadata, safe filenames, mtimes, tests, checked-in reports, and visible artifacts. It does not publish secret-bearing files, `.env` contents, hidden local settings, raw prompts/logs/trajectories, private corpus bodies, evaluator payloads, raw benchmark outputs, checkpoint/model artifacts, biometric/capture data, generated media bodies, or sensitive/provocative material.

Where a directory is local-only, sensitive, artifact-heavy, private-corpus-backed, or too skeletal, this note uses category-level wording. The point is provenance, not rummaging. Rummaging is for raccoons and, on bad days, software archaeology.

## Survey scope and method

- Survey root: `/Users/ericfode/src`.
- Survey timestamp: 2026-05-16 01:36 PDT.
- Full top-level directory count: 43, including hidden directories.
- Execution shape: exactly 10 top-level Hermes survey lane identities, dispatched as one batch of 10 orchestrator lanes.
- Lane coverage audit: controller enumeration found 43 assigned directories, 43 unique assignments, no missing directories, no extras, and no duplicates.
- Lane recursion: all 10 top-level lanes reported spawning three read-only subteams for purpose/docs/manifests, live-work evidence, and public-safety/public-summary eligibility. Those subteams reported one further three-way leaf recursion. The recorded depth is lane → subteams → leaves; no deeper recursion is claimed.
- Evidence allowed: README/docs/plans, manifests, branch/status/log metadata, safe modified/untracked filenames, mtimes, tests, checked-in reports, and visible artifacts.
- Evidence excluded: secret contents, `.env` contents, hidden local settings, raw prompts/logs/trajectories, hidden evaluator/supervisor payloads, private corpus bodies, explicit/provocative/unsafe material, raw benchmark outputs, checkpoints/model artifacts, biometric/capture data, generated media bodies, and directories too skeletal for a responsible public claim.
- Illustration: a generated raster draft was rejected because it contained pseudo-readable text. The committed illustration is deterministic symbolic SVG art at `queries/news-assets/2026-05-16-project-desk-hero.svg`; it is not a screenshot.

## Ten survey lanes

1. `.claude`; `.socket-dev-scan`; `.tinygrad_research`; `another-harness`.
2. `are-the-astrological-signs-rascist`; `basis`; `basis-hermes`; `basis-jcode`.
3. `cardgame1`; `creative`; `deer-flow`; `FACEMUSIC`.
4. `gas-city-but-its-just-codex`; `gemma-dungeon`; `gemma4-tinygrad-opt`; `handterm`; `hoid`.
5. `is-codex-better`; `is-it-formal`; `jepa-expriments`; `jepa-poker`.
6. `justfooln`; `kettlebellsim`; `kimi-tests`; `langfuse`.
7. `local-hermes`; `meta-hermes`; `nnpl-external-latent-bus`; `nnpl-shared-bus`; `nnpl-typed-boundary-ir`.
8. `openai-symphony`; `overengineeredlife`; `silly-pi-stuff`; `spec-dataset-evolution-corpus`.
9. `src`; `steward`; `testing-rl`; `testing-rl-hermes`.
10. `textual-world-model`; `tinygrad`; `tinygrad-gemma`; `tinygrad-gemma-gemini`; `tinygrad-gemma-kimi`.

## Public-safe lead candidates

### Same-night JEPA and world-model bench

- `jepa-poker` is tonight's clearest new public-safe research signal. Evidence: non-git root with README/pyproject/docs describing a tinygrad JEPA-style Kuhn poker project: first learn world representation, then train a player model from frozen world embeddings. Recent visible artifacts include metrics/policy/world-model JSON outputs and `src/jepa_poker/pipeline.py`. Safe summary: a compact poker world/player-model experiment; raw model outputs remain withheld unless separately reviewed.
- `jepa-expriments` is active but category-only. Evidence: non-git root, pyproject package naming local JEPA experiments for poker and kubectl-action simulation, docs for acceptance/spec/world-model substrate research, and recent research/report/artifact activity. Public handling: mention only as an internal local JEPA research bench; hold back evaluator/falsification corpora, leakage audits, model-visible snapshots, gold-patch/test-run artifacts, logs, and caches.
- `gemma-dungeon` remains a strong public-safe model/state project. Evidence: clean git repo on `main`, HEAD `f682fdf` for train-baseline slot status text ledger, Python package metadata, README/specs/CLI, and recent docs/spec/package mtimes around 2026-05-15. Safe summary: an embedding-native, symbolically audited roguelike workspace where explicit game state remains authoritative and Gemma-facing projections are auditable.
- `textual-world-model` is public-safe only from the top-level concept page. Evidence: `index.html` frames an action-conditioned latent predictor over Git repository histories; `research-loop/` has recent heartbeat/ledger/dashboard-style artifacts by filename. Safe summary: concept-page evidence for repository-history world-model research; raw research-loop artifacts stay held back.

### Stable verifier and model-runtime benches

- `testing-rl` remains the clearest verifier/test-generation repo. Evidence: clean git tree on `master`, tracking origin and ahead by 3 commits; recent May 10–11 commits around ranking lift, local verifier dashboard evidence, held-out verifier rankers, live rewards dashboard, and counterfactual cases; README/SPEC/WORKFLOW/docs/formal/pyproject. Safe summary: an RL environment for agents or models that write high-value software tests while evaluator-held references remain private.
- `tinygrad-gemma` remains the strongest model-runtime package. Evidence: repo on `main`, ahead of origin by 93 commits, README and pyproject for a native tinygrad Gemma 4 implementation, CLI/chat entry points, tinygrad dependency, and many untracked benchmark/reference-fetch artifacts. Safe summary: Gemma 4 inference/generation work in tinygrad; raw benchmark numbers, profile payloads, checkpoints, and unreviewed performance claims remain withheld.
- `tinygrad-gemma-kimi`, `gemma4-tinygrad-opt`, and empty `tinygrad*` placeholders were surveyed but stay category-only or held back because they are sparse, scratch-heavy, undocumented, dirty, or artifact-heavy.

### Formal/spec/provenance and orchestration bench

- `is-it-formal` is public-summary eligible. Evidence: unborn git repo on `main`, Lean/Lake manifests (`leanprover/lean4:v4.29.0`), README describing a Lean-backed scaffold for grading “how formal” claims across domains, examples, a grading script, and Lean CI workflow. Safe summary: a small Lean-backed formality-grading scaffold.
- `basis-hermes` is the clean public-safe Basis face. Evidence: clean git repo, pyproject package `basis-hermes`, plugin metadata exposing `basis_reduce_spec` and `basis_validate_packet`, recent commits around schema compatibility, dashboard autorun, docs reload, and smoke contracts. Safe summary: a Hermes plugin and dashboard wrapper around deterministic spec reduction and packet validation.
- `basis` is public-safe at high level as an Elixir/BEAM Basis reducer project; `basis-jcode` is category-only because `.basis` run ledgers, worker packets, streams, and generated artifacts dominate the public boundary tonight.
- `steward` shows internal service-kernel movement. Evidence: dirty git repo, seeded design commit, Elixir/Mix/Ecto service scaffold, docs and query-contract material. Safe handling: category-only as durable provenance/service-kernel tooling connecting specs, code, tests, reasoning, agent runs, verification, and Git history.
- `openai-symphony`, `gas-city-but-its-just-codex`, `another-harness`, `is-codex-better`, and `deer-flow` were surveyed as orchestration/control-plane side rooms. Public handling should stay architectural: issue/workspace orchestration, app-server bridges, workflow ledgers, formal scaffolds, and agent-harness extension ideas; not local logs, prompt bodies, tracker identifiers, or runtime state.

### Craft, interface, simulation, and neural-native side rooms

- `handterm` remains the cleanest craft lead. Evidence: clean Rust 2024 workspace on `master...origin/master`, MIT license, README, Cargo workspace, CPU/GPU renderers, server/client crates, tests, and recent kitty upload-state extraction. Safe summary: resource-efficient Wayland-native terminal work.
- `cardgame1` / Dungeon Steward remains a high-level public candidate. Evidence: clean Godot branch ahead by one, `project.godot` naming Dungeon Steward, deterministic combat-loop prototype docs, scenes/assets/data/scripts/tests. Hold back agent workflow scaffolding, prompt/process artifacts, generated/cache/build material, and raw balance artifacts.
- `kettlebellsim` is public-safe high-level. Evidence: clean git branch, pyproject package `kettlebellsim`, README-planning-system material, docs/scripts/tests, and recent Modal/Isaac guard/restart commits. Safe summary: simulation-first kettlebell swing path-signature research; remote-service details, logs, trajectories, rollouts, and generated media remain private.
- The NNPL cluster (`nnpl-external-latent-bus`, `nnpl-shared-bus`, `nnpl-typed-boundary-ir`) has public-docs evidence for latent-bus, shared-bus, and typed-boundary IR experiments, but raw artifacts, runs, metrics, data exports, traces, model states, and oracle/eval outputs stay held back.
- `FACEMUSIC` is high-level only because the project crosses camera/facial capture and ML. Evidence supports web/iOS/Rust/ML face-controlled music instrumentation, but raw capture/session/model-run details remain private.

## Held back from project-specific public detail

The survey fully held back, or reduced to category-only mention, hidden local settings, security-scan artifacts, empty or hidden-only directories, one provocative/protected-class-sensitive social-claim notebook, local deployment/model-runner folders, private corpus bodies, prompt/agent/skill instruction bodies, scratch/meta workspaces, generated media, raw logs/prompts/trajectories, evaluator-like payloads, hidden references/oracles, benchmark raw outputs, model/checkpoint artifacts, biometric/capture data, creative story/canon drafts, service configuration, raw test/counterexample bodies, cache/build/vendor directories, and too-skeletal placeholders.

## Editorial synthesis

The publishable movement tonight clusters around five claims:

1. `jepa-poker` is the new public-safe live lead: small, legible, and world-model shaped.
2. `gemma-dungeon`, `testing-rl`, and `tinygrad-gemma` remain the sturdier benches: symbolic game state, verifier/test generation, and model runtime.
3. `is-it-formal`, `basis-hermes`, and `basis` give the formal/spec-provenance corner enough structure to mention without raiding private run ledgers.
4. `handterm`, Dungeon Steward, and `kettlebellsim` remain the clean craft/game/simulation rooms.
5. Many orchestration and local-research directories are real work but not public copy: the safety filter did useful violence to curiosity.
