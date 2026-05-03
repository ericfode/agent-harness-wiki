---
title: Nightly Src Projects Desk (2026-05-03)
created: 2026-05-03
updated: 2026-05-03
type: query
tags: [survey, work-management, orchestration, code-quality, formal-methods, benchmark]
sources: [raw/articles/nightly-src-projects-desk-2026-05-03.md, concepts/formal-methods-for-agent-harnesses.md, concepts/evaluation-and-review-loops.md, concepts/harness-engineering.md, concepts/neural-native-programming.md, concepts/work-management-primitives.md]
---

# Nightly Src Projects Desk (2026-05-03)

![Editorial illustration of the current source-project desk: test-writing labs, deckbuilder cards, face-music waves, Codex control-plane ledgers, NNPL boundary diagrams, transformer benches, and a kettlebell biomechanics silhouette.](news-assets/2026-05-03-project-desk-hero.svg)

_Editorial illustration generated as a local SVG after the configured image backend reported no `FAL_KEY`. It is an illustration, not a screenshot; no imaginary dashboard was harmed in the making of this page._

## Verdict

Tonight's `src/` tree is no longer just a spread of clever experiments. Its strongest public-safe signal is evidence work: `testing-rl` and `testing-rl-hermes` are shaping agent test-writing into explicit environments, replay/verifier surfaces, artifact schemas, and hidden-evaluator discipline. That sits close to [[evaluation-and-review-loops]], [[formal-methods-for-agent-harnesses]], and [[work-management-primitives]] rather than merely borrowing their vocabulary.

The second line is practical feel. Dungeon Steward (`cardgame1`) is polishing combat-stage art fallback, deck/run legibility, and smoke coverage. `FACEMUSIC` continues binding face-expression semantics to browser, iOS, audio, and forecasting machinery. Beside them, `gas-city-but-its-just-codex` and `openai-symphony` keep the orchestration bench serious: ledgers, workspaces, operator surfaces, path safety, and app-server sessions rather than a confetti cannon labelled "autonomy."

Ten top-level survey lanes covered all 30 top-level directories under `/Users/ericfode/src`. The runtime would not accept all ten lanes concurrently, so the desk ran them as 6 + 4. That is not glamorous, but neither is a correct semaphore.

## Front page

### Test-writing environments

`testing-rl` is the lead because its evidence is both current and specific. The repo is a dirty `master` worktree with one visible commit from 2026-05-02 and local work across replay verification, artifact/training-product schemas, adapters, risk/event mining, tests, and Lean formalization. The public claim is not "an RL breakthrough". It is narrower and better: a software-testing environment is being made observable enough that test-writer behavior can be rewarded, replayed, and criticized without pretending the transcript is the ground truth.

`testing-rl-hermes` is the cleaner sibling: a `main` branch with recent commits adding a deterministic test-generation RL environment, history-derived fixtures, and inverse-fix history mutants. Its docs are explicit about the game being played: reward tests that reveal behavior, kill mutants, preserve correct code, and do not tamper with the referee. That belongs in the same district as [[automation-and-background-work]] and [[harness-engineering]]: less oracle, more apparatus.

Supervisor-only benchmark details were deliberately left out. A hidden evaluator stops being useful at the exact moment one publishes its answer key. Formal systems have few jokes, but that is one of them.

### Dungeon Steward (`cardgame1`)

Dungeon Steward remains the most straightforward game-facing lead. The repo is clean on `hermes/combat-stage-art-fallback-upstream`, ahead of upstream by one commit, with evidence in `project.godot`, GDD docs, combat-stage controllers, deck-inspection UI, texture loading, smoke probes, and prototype tests.

The recent work is not decorative; it is legibility work. Combat-stage art fallback, deck/run presentation, and smoke coverage are the sorts of changes that make a prototype stop lying to the player. Game code earns dignity one trustworthy frame at a time. Annoying, but true.

### FACEMUSIC

`FACEMUSIC` is still the embodied interface outlier: browser MediaPipe/Tone-style control, native iOS Vision/AVAudioEngine work, Rust/audio-core scaffolding, and an offline ML stack for expression forecasting. The worktree is dirty in the useful way: browser control schema and music-engine paths, iOS conductor/camera/session files, and untracked ML configs/scripts all point at the same problem.

The safe summary is simple. Facial gesture is being treated as musical control semantics, not just a telemetry stream with better lighting. Capture/session specifics were omitted.

### gas-city-but-its-just-codex and openai-symphony

`gas-city-but-its-just-codex` is the denser orchestration bench: Rust workspace, workflow-ledger semantics, repo-loop automation, image-first context boards, templates, validators, smoke scripts, and operator-policy surfaces. Its branch is dirty, so the page says what can be safely said: this is control-plane work, with state being pulled into explicit artifacts rather than left to dissolve in a heroic chat log.

`openai-symphony` is cleaner and more package-shaped: Apache-2.0, clean `main`, Elixir/OTP reference implementation, docs for orchestrating autonomous coding-agent work over Linear, isolated workspaces, Codex app-server sessions, path safety, observability, logging, and token accounting. The public caveat is equally important: the docs frame it as prototype/evaluation software, not production infrastructure.

Together, these two projects make the orchestration story less mystical. Work objects, ledgers, workspaces, and safety rails are not ornamental. They are the part that lets the machine be audited after it has been clever.

### NNPL research cluster

The NNPL cluster remains public-safe because it is unusually honest about its own uncertainty:

- `nnpl-external-latent-bus` tests a two-space external/internal latent bus against matched one-space comparators.
- `nnpl-shared-bus` records a negative v0 result for a shared recurrent workspace rather than smoothing it into success prose.
- `nnpl-typed-boundary-ir` shifts the interface to typed boundary artifacts, validation, rendering, and auditability.

None of these had git metadata available, so the claims are doc/source/artifact-grounded rather than commit-grounded. The useful theme is exactly the one [[neural-native-programming]] needs if it is to become engineering: boundaries, baselines, and failed hypotheses have to remain visible.

## Research bench

### another-harness and is-it-formal

`another-harness` is a large uncommitted Lean-backed harness prototype: work items, evaluator loops, handoffs, resumable artifacts, MCP/control-plane tooling, plugins, benchmarks, and formal harness modeling. It is public-safe only at architecture altitude because the tree has no commits and substantial untracked state.

`is-it-formal` is smaller and sharper: a Lean 4 + Python scaffold for grading how formal a claim is, with JSON examples and deterministic CLI checks. It is also uncommitted, which keeps it on the bench rather than the front page. Still, its instinct is correct: before a claim can be verified, one should notice whether it has acquired a shape capable of being verified.

### Gemma/tinygrad benches

The Gemma/tinygrad area is active but not suitable for public performance theatre. `.tinygrad_research` is a clean public tinygrad checkout. `gemma4-tinygrad-opt` is a local optimization/Metal benchmarking workspace with nested tinygrad, logs, prompts, and evolution traces. `tinygrad-gemma-kimi` is a dirty `opt/attention` repo with Gemma attention/JIT/memory-layout/correctness patch experiments and result JSON artifacts.

The safe public claim is WIP experimentation. The unsafe claim would be benchmark victory. The desk declines the latter with the grave restraint appropriate to a folder full of patches.

### Kettlebell simulation and local model rooms

`kettlebellsim` is a simulation-first biomechanics project around scripted kettlebell swing templates, cyclic observations, behavior-cloning warm-start, reward/retention diagnostics, and Modal probe/training workflows. It stays side-room because local temp/tool fragments and external secret-handling references make raw publication irresponsible.

`local-hermes` is a small non-git llama.cpp / GGUF runner. `langfuse` is a local compose stack with `.env` present. Both can be named only generically. Local infrastructure is useful; publishing its drawer labels is not.

### Process and creative side rooms

`justfooln` contains a research harness and benchmark ladder for long-horizon/tool-heavy agent evaluation. `silly-pi-stuff` mixes a private-marked Pi companion UI with an octonion-surface browser cellular automata demo. A hidden `cardgame1` skill bundle under `src` appears to be game-development workflow/process tooling. These are visible enough for side-room notes, not sturdy enough for front-page claims.

A mixed creative-worldbuilding suite and a sensitive reputational/social-claim notebook were inspected and left out. They may contain work; they are not appropriate public desk material tonight.

## What the desk left out

The safety filter fully held back, or reduced to category-only mention, material from ten top-level directories. Reasons included sensitive identity/reputational framing, local agent settings, `.env` or deployment-config signals, empty/skeletal directories, zero-commit all-untracked trees, mixed creative material needing curation, hidden supervisor/evaluator surfaces, and prompt-bearing workflow residues.

That is not coyness. It is the minimum competence required when turning a local source tree into a public page. A newspaper should report the city; it should not publish the locksmith's notebook.

## Bottom line

The publishable story tonight is pleasantly austere:

- test-writing environments are becoming explicit enough to audit;
- game/interface work is spending effort on trustworthy feel;
- orchestration benches are externalizing state into ledgers and work objects;
- NNPL and Gemma/tinygrad benches are keeping baselines and failures visible.

It is not a unified product line. It is a set of workshops learning the same discipline: claims should be attached to artifacts, and artifacts should survive being looked at.
