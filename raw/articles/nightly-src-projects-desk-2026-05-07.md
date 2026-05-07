---
title: Nightly Src Projects Desk Raw Survey (2026-05-07)
author: local multi-agent survey synthesis
url: file:///Users/ericfode/src
ingested: 2026-05-07
---

# Nightly Src Projects Desk Raw Survey (2026-05-07)

This raw note preserves the public-safe basis for the 2026-05-07 nightly `src/` projects desk. It records what was inspected, where the safety filter intervened, and where the desk should not pretend that a filename is the same thing as a theorem. Tempting, but no.

## Survey scope and method

- Survey root: `/Users/ericfode/src`
- Survey timestamp: 2026-05-07 PDT
- Full top-level directory count: 38.
- Execution shape: exactly 10 top-level Hermes survey lanes, dispatched as 3 + 3 + 3 + 1.
- Lane recursion: all 10 lane summaries reported that `delegate_task` was available and used. Each lane reported a 3-way split for purpose/docs, live-work evidence, and safety/public-summary eligibility, plus a further one-level 3-way recursion by its sub-inspectors. The parent synthesis treats those as lane self-reports and grounds public claims in inspectable evidence.
- Coverage correction: the first lane inventory used the 36 visible top-level directories. A post-dispatch full root audit found two hidden top-level directories. To preserve the exact-ten-lane constraint rather than invent an eleventh lane, the controller performed a read-only hidden-directory supplement: one local hidden settings directory was held back, and one clean upstream tinygrad checkout was summarized from README/git metadata.
- Evidence allowed: README/docs/plans, project manifests, branch/status/log metadata, safe modified/untracked filenames, mtimes, tests, checked-in reports, and visible artifacts.
- Evidence excluded: secret contents, `.env` contents, local settings contents, raw prompt/log/trajectory material, hidden evaluator/supervisor payloads, private corpus bodies, explicit/provocative material, and directories too skeletal for a responsible public claim.
- Illustration: the configured image backend failed with missing `FAL_KEY`; the page therefore uses a generated local SVG editorial illustration under `queries/news-assets/`. It is symbolic art, not a screenshot.

## Ten survey lanes plus hidden-dir supplement

1. `another-harness`; one sensitive social-claim notebook withheld; `basis`; `basis-hermes`.
2. `basis-jcode`; `cardgame1` / Dungeon Steward; empty `creative`; `deer-flow`.
3. `FACEMUSIC`; `gas-city-but-its-just-codex`; `gemma4-tinygrad-opt`.
4. `handterm`; `hoid`; `is-codex-better`; `is-it-formal`.
5. `justfooln`; `kettlebellsim`; skeletal `kimi-tests`; local `langfuse` folder.
6. `local-hermes`; `meta-hermes`; `nnpl-external-latent-bus`; `nnpl-shared-bus`.
7. `nnpl-typed-boundary-ir`; `openai-symphony`; empty `overengineeredlife`.
8. `silly-pi-stuff`; private `spec-dataset-evolution-corpus`; skeletal nested `src`.
9. `steward`; `testing-rl`; `testing-rl-hermes`.
10. empty `tinygrad`; `tinygrad-gemma`; empty `tinygrad-gemma-gemini`; `tinygrad-gemma-kimi`.
11. Hidden-dir supplement, not an extra lane: hidden local settings withheld; hidden clean upstream tinygrad research checkout summarized only as tinygrad context.

## Public-safe lead candidates

### Spec-code and Basis cluster

- `basis` evidence: `spec.md`, `mix.exs`, `components/spec-basis-reducer/spec.md`, Elixir runtime/source/server files, tests, and recent commits. Parent git check: branch `main`, head `031340a` on 2026-05-06, dirty with 6 tracked changes and 1 untracked file. Safe summary: an Elixir/BEAM prototype for turning overcomplete specifications into structured, provenance-bearing Basis state and proposals.
- `basis-hermes` evidence: `README.md`, `plugin.yaml`, `pyproject.toml`, `dashboard/manifest.json`, reducer component docs, and tests. Parent git check: clean `main` at `0061d32` on 2026-05-05, whose message records Codex-compatible Basis tool schemas. Safe summary: Hermes plugin/dashboard exposing deterministic Basis reducer and packet validator surfaces.
- `basis-jcode` evidence: reducer README/spec, package manifest, CLI/dashboard server files, tests, and recent commits. Parent git check: `main` at `4b1e621` on 2026-05-05, ahead/dirty by lane report with tracked deletions. Safe summary: Jcode-native reducer control-plane work; raw packets, ledgers, events, and run materials withheld.
- `steward` evidence: `README.md`, `pyproject.toml`, project charter, benchmark spec, architecture, implementation plan, data governance, modeling roadmap, workflows, and decision log. Parent git check: clean `main` at `ba88837` on 2026-05-05. Safe summary: design-stage local-first spec-code grounding tool.
- `is-it-formal` is a small no-commit Lean/Python scaffold for classifying formalization strength; public-safe as a concept, but not yet release-like.

### Test-writing and evaluator environments

- `testing-rl` evidence: `README.md`, `SPEC.md`, `pyproject.toml`, workflow docs, dashboard/artifact schemas, environment/counterfactual verifier/Hermes adapter docs, Lean files, Python environment/replay/sidecar code, and tests. Parent git check: `master` at `139cea4` on 2026-05-04, dirty with 5 tracked changes and 3 untracked files. Safe summary: a software-testing RL environment where replay, evidence, and evaluator boundaries are first-class.
- `testing-rl-hermes` evidence: `MASTER_PLAN.md`, `pyproject.toml`, docs for deterministic test-generation environments and history-derived fixtures, benchmark fixture suite, source, and tests. Parent git check: clean `main` at `6cbca51` on 2026-05-02. Safe summary: executable/prototype companion for deterministic test-generation and hidden-reference style grading.
- Hidden evaluator/reference/oracle details remain category-only. A hidden answer key is not improved by being laminated.

### Tinygrad, Gemma, and NNPL benches

- `tinygrad-gemma` evidence: `README.md`, `pyproject.toml`, source package, tests, scripts, docs, and CI. Parent git check: `main` at `8128f4b` on 2026-05-07, no tracked dirt and 57 untracked local/generated artifacts. Safe summary: native tinygrad Gemma 4 implementation with generation, tokenizer/KV-cache, multimodal, CLI/chat, training, and int8-related surfaces; raw benchmark logs/checkpoints/prompts and performance claims withheld.
- `.tinygrad_research` evidence: clean hidden upstream tinygrad checkout on `master` at `87378331e` on 2026-04-21, with README, `pyproject.toml`, and license. Safe summary: tinygrad context only, not a new local project story.
- `tinygrad-gemma-kimi` evidence: dirty `opt/attention` repo at `8d23d35` on 2026-04-26 with attention/JIT/correctness/validation filenames. High-level optimization-workspace mention only.
- `gemma4-tinygrad-opt` evidence: non-root-git Gemma/tinygrad optimization workspace with scripts and nested tinygrad checkout. High-level only; raw logs/prompts/results withheld.
- NNPL evidence: `nnpl-external-latent-bus`, `nnpl-shared-bus`, and `nnpl-typed-boundary-ir` have docs, source/tests, and public-safe methodological framing around external/internal latent buses, shared-bus negative-result posture, and typed boundary IR. Raw results, traces, rollouts, metrics, and generated artifacts withheld.

### Craft, interface, game, and simulation work

- `handterm` evidence: `README.md`, MIT license, Cargo metadata, clean `master` at `977e709` on 2026-04-19. Safe summary: Rust/Wayland terminal emulator focused on low latency, rendering architecture, and shared-process scaling.
- `cardgame1` / Dungeon Steward evidence: `README.md`, `project.godot`, GDD docs, deterministic-runtime ADRs, balance workflow docs, smoke/simulation/determinism tests. Parent git check: clean branch `hermes/combat-stage-art-fallback-upstream` at `a9a8ef6` on 2026-04-15. Safe summary: browser-first Godot roguelite deckbuilder with deterministic combat and combat-stage art fallback polish.
- `FACEMUSIC` evidence: browser architecture docs, iOS native README, ML README/manifest, Vite/React/Tone/MediaPipe package surface. Parent git check: `main` at `f6cf6cf` on 2026-04-19, dirty with 15 tracked changes and 2 untracked entries. Safe summary: face-expression musical control semantics across browser, iOS, audio, and forecasting surfaces; capture/session/model specifics withheld.
- `kettlebellsim` evidence: Python manifest, planning-system README, cyclic-control docs, tests/scripts, and branch `codex/reward-audit-and-swing-training` at `b075200` on 2026-04-09 with only untracked temp/probe files. Safe summary: simulation-first kettlebell biomechanics and training-incentive research toolkit.
- `hoid` was inspected but reduced to high-level creative/worldbuilding/tooling mention. Unpublished creative drafts, generated review data, story/canon/music/comic details, and local state stay out of public copy.

### Orchestration and harness side rooms

- `openai-symphony` evidence: README/spec/Elixir docs for coding-agent orchestration over isolated workspaces, status dashboards, Codex app-server sessions, logging, and token accounting. Parent git check: `main` at `58cf97d` on 2026-04-27, dirty with 9 tracked changes. Safe summary: engineering-preview orchestration bench; uncommitted details/logs omitted.
- `gas-city-but-its-just-codex` evidence: Rust workspace, workflow-ledger specs, templates/schemas, MCP/gRPC/app-server surfaces, operator tooling, Swift/macOS UI, and Lean formalization. Parent git check: `codex/native-codex-ui` at `198aefc` on 2026-04-21, dirty with 7 tracked changes and many untracked files. Safe summary: Codex-native durable workflow/control-plane research prototype; runtime state, logs, transcripts, and generated artifacts withheld.
- `another-harness`, `is-codex-better`, `justfooln`, `deer-flow`, `meta-hermes`, `local-hermes`, local `langfuse`, `silly-pi-stuff`, and the private spec corpus were inspected and kept to high-level/category-only treatment according to maturity and privacy risk.

## Held back from project-specific public detail

The survey fully held back, or reduced to category-only mention, material from the hidden local settings directory, one sensitive social-claim notebook, empty/skeletal directories, local deployment/model-runner folders, private corpus contents, internal workflow/assistant configuration, scratch/meta workspaces, generated artifacts, prompt/log/trajectory materials, evaluator-like payloads, benchmark raw outputs, model/checkpoint artifacts, and creative material needing human curation.

That is not coyness. It is the basic hygiene of turning a local source tree into a public note: describe the workshop, not the locksmith's notebook.

## Editorial synthesis

The public-safe movement tonight clusters around five themes:

1. specification state and spec-code grounding are becoming first-class artifacts (`basis`, `basis-hermes`, `basis-jcode`, `steward`);
2. software-testing environments are preserving replay/evidence boundaries rather than presenting benchmarks as magic (`testing-rl`, `testing-rl-hermes`);
3. model-internals benches are using boundaries, baselines, and withheld performance claims (`tinygrad-gemma`, NNPL, Gemma/tinygrad sandboxes);
4. craft projects continue to make feel and interface surfaces inspectable (`handterm`, Dungeon Steward, `FACEMUSIC`, `kettlebellsim`);
5. orchestration projects are externalizing state into ledgers, workspaces, dashboards, and formal/control-plane surfaces (`openai-symphony`, `gas-city-but-its-just-codex`, DeerFlow).

The theme is not a product launch. It is better than that, in the limited but respectable sense: more of the work is acquiring checkable shape.
