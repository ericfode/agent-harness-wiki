---
title: Nightly Src Projects Desk Raw Survey (2026-04-21)
author: local multi-agent survey synthesis
url: file:///Users/ericfode/src
ingested: 2026-04-21
---

# Nightly Src Projects Desk Raw Survey (2026-04-21)

This raw note preserves the public-facing survey basis for the first nightly src projects desk.

## Survey scope and method

- Survey root: `/Users/ericfode/src`
- Survey time: 2026-04-21 22:22 PDT
- Coverage: 23 top-level directories under `src/`
- Execution shape: 10 survey lanes over repo clusters, using repo docs, git/worktree state, recent file activity, and content-safety checks
- Publication rule: omit directories whose visible material is explicit-tagged, secret-bearing, internal-only, or too skeletal to summarize responsibly

The survey request asked for recursive teams of three. Some lanes managed deeper worker fanout; others reported that deeper subagent delegation was not exposed in their runtime and fell back to parallel three-pass inspection instead. The public brief therefore reflects the best available evidence rather than pretending the orchestration layer was tidier than it was.

## Lead projects judged safe to publish

### another-harness
- Lean-backed, artifact-first harness repo competing with Hermes while keeping a formalization plane live.
- Freshest visible work centers on native agent execution for builder-side benchmark runs and a browser review/doc viewer.
- The live repo state points next toward extending native execution and/or resume/recover integration rather than opening a brand-new front.

### Dungeon Steward (`cardgame1`)
- Godot 4.6.2 browser-first fantasy roguelite deckbuilder.
- Current tracked branch work hardens combat-stage art presentation and generated-asset fallbacks, with smoke probes around layout and hit areas.
- Recent adjacent work added the map deck viewer, authored floor-one map layout, and stricter map hover legality.

### gas-city-but-its-just-codex
- Rust Codex-native orchestration/control-plane workspace with ledger, operator surfaces, and formal/runtime bridge work.
- Latest committed work adds Harbor task-level transfer reporting.
- Dirty-tree work extends that into task-level Harbor gates, per-thread bootstrap recommendations, a self-hosting repo-loop-toolsmith workflow, image-memory/image-first experiments, and a queued Workgraph rename pass.

### kettlebellsim
- Isaac Lab + Modal robotics/biomechanics repo training a Unitree H1 humanoid to swing a kettlebell.
- Active branch work is not claiming victory; it is trying to turn scripted bootstrap into retained swing behavior.
- Current visible increment adds scripted swing template extraction, richer cyclic observations, behavior-cloning warm-start, and more honest swing-quality metrics.

### FACEMUSIC
- Face-controlled music instrument spanning browser, native iOS, and an emerging offline ML stack.
- Local work aligns browser and iOS control models around richer expression signals such as asymmetry, tension, volatility, recovery lag, and expressive leak.
- A new forecasting foundation is present locally for predicting facial state 500 ms ahead from 1.5 s of history.

## Secondary safe bench worth noting

### is-codex-better
- Pre-commit Codex-native harness/plugin source repo.
- Visible work sits in installer/runtime proof docs, gap audit material, and file-backed procedure state.

### is-it-formal
- Pre-commit Lean 4 + Python scaffold for grading claim formality.
- Visible work centers on the JSON-to-Lean loader, deterministic CLI grader, and cross-artifact drift examples.

### nnpl-external-latent-bus
- Current motion is on output-side bridge and modularity probes after weaker input-side bridge results.

### nnpl-shared-bus
- The visible state reads as a completed negative-result sweep rather than a fresh win claim.

### nnpl-typed-boundary-ir
- Recent work adds evaluation and bakeoff tooling; typed boundaries visibly improve auditability even where competence gains remain modest.

## Lower-signal safe directories

- `deer-flow` shows local runtime/debugging activity and an nginx logging tweak rather than a new product slice.
- `.tinygrad_research` is a clean official tinygrad checkout with no local changes.
- `silly-pi-stuff` contains a whimsical subconscious-pet extension plus an octonion-surface browser experiment.
- `justfooln` contains a finished long-autonomy brief and benchmark artifacts, but the visible work is older than the current front-burner projects.
- `local-hermes` is a local GGUF-serving setup folder, not an actively developed source repo.

## Held back from the public brief

Some surveyed directories were intentionally omitted from the public page because the visible material was one or more of:
- explicit-tagged mixed-content creative work
- secret-bearing local deployment configuration
- internal debate/staging material
- skeletal or empty non-project directories
- provocative framing better left out of a public nightly roundup

## Evidence style

This note intentionally keeps only the public-summary layer. The deeper survey evidence included branch names, recent commits, worktree dirtiness, modified file clusters, and selective doc inspection for each lane. The news page cites this raw note and compresses those findings into a readable desk brief.
