---
title: Nightly Src Projects Desk (2026-05-31)
created: 2026-05-31
updated: 2026-05-31
type: query
tags: [survey, work-management, orchestration, code-quality, formal-methods, benchmark, safety, program-synthesis]
sources: [raw/articles/nightly-src-projects-desk-2026-05-31.md, concepts/evaluation-and-review-loops.md, concepts/formal-methods-for-agent-harnesses.md, concepts/harness-engineering.md, concepts/work-management-primitives.md, concepts/neural-native-programming.md, concepts/safety-and-permissions.md]
---

# Nightly Src Projects Desk (2026-05-31)

![Symbolic editorial illustration of ten source-tree survey lanes passing through a safety prism into clusters for games, verifier benches, JEPA and tinygrad/Gemma research, simulation, proof, and orchestration tooling.](news-assets/2026-05-31-project-desk-hero.svg)

_Editorial illustration generated locally as deterministic SVG after raster generation was unavailable in this environment. It is symbolic art, not a screenshot; no fake dashboard has been promoted into evidence._

## Verdict

Tonight's `src/` desk has a cleaner center than the usual heap of experimental glitter. The front-page lead is `gemma-dungeon`: it has same-night commit evidence, a clean worktree, and a public-safe story about symbolic roguelike state remaining authoritative while Gemma/tinygrad-facing projections are audited. That is the sort of architecture that does not ask the model to be a deity in a bathrobe, which is already progress.

The second tier is sturdy rather than theatrical. `cardgame1` / Dungeon Steward carries the Godot game-craft line; `testing-rl` and `testing-rl-hermes` remain the verifier/test-generation benches; `kettlebellsim` is the simulation-validation lead. The formal/spec/provenance room is active — Basis/Hermes, `another-harness`, `is-it-formal`, `openai-symphony`, and `steward` — but most of it belongs in curated side rooms because the live surfaces include uncommitted state, private corpora, run ledgers, prompts, logs, or local service details. [[evaluation-and-review-loops]] applies: a claim earns the page only after its evidence does.

Exactly 10 top-level Hermes survey lane identities covered all 50 top-level directories under the local `src/` root, including hidden directories. All 10 lanes reported three read-only subteams for purpose/docs/manifests, live-work evidence, and public-safety/public-summary review; each subteam reported a further three-way leaf probe. The controller audit found 50 assigned directories, 50 unique assignments, no missing directories, no extras, and no duplicates. The tree was wider than the page. Good.

## Front-page lead projects

### Game craft, symbolic worlds, and verifier benches

`gemma-dungeon` is tonight's lead. The inspected evidence is concrete: README, goal/spec/implementation docs, pyproject, schemas, tests, clean `main`, and 2026-05-30/31 commits around verified eval/train-gap and sweep-best status-token work. The safe claim is narrow: embedding-native roguelike/world-model research where symbolic game state stays authoritative and model-facing projections are auditable. This sits naturally beside [[formal-methods-for-agent-harnesses]], not because it is a formal proof, but because it respects the same boundary between witness and wish.

`cardgame1` / Dungeon Steward remains the game-craft lead: Godot project, README, MIT license, design/docs/data evidence, a branch ahead by one, and visible work around combat-stage art fallback, map hover legality, and authored floor-one map layout. The public version is a browser-first fantasy roguelite deckbuilder prototype with deterministic combat, map, reward, and art-fallback handling. The private `.beads`, agent, JSONL, prompt/imagegen, generated-media, and Godot import surfaces stay out.

`testing-rl` and `testing-rl-hermes` remain the verifier bench. The former is clean and ahead by three commits, with recent evidence around verifier dashboards, held-out ranking, rewards dashboards, and counterfactual case breakdowns. The latter has deterministic history-derived fixtures and grading logic. The safe story is test-generation and evaluator discipline, not a claim that the reinforcement-learning fairy has visited in the night.

`kettlebellsim` is the simulation-validation lead: clean branch, ahead by 36 commits, pyproject/docs/config/scripts/tests, and visible work on bounded Modal Isaac probe execution wrappers plus planar local-to-remote restart validation. The useful phrase is “deterministic local validation before bounded remote simulator execution.” It is less catchy than “AI fitness oracle,” but unlike that phrase, it has the virtue of being sane.

### Formal/spec/provenance and orchestration side rooms

Basis remains the coherent spec-reduction cluster. `basis` shows active Elixir/BEAM spec-basis work; `basis-hermes` is the clean plugin/dashboard slice exposing deterministic reduction and packet validation; `basis-jcode` has strong reducer/control-plane evidence but is dominated by `.basis` run ledgers, prompts, NDJSON streams, dashboard outputs, and local runtime surfaces. Public summary: structured spec-state custody and provenance-backed reduction. Not public summary: packet necromancy.

`another-harness` and `is-it-formal` are legible but young. `another-harness` has a Lean-backed Codex/Hermes harness shape, yet no commits and a fully untracked baseline. `is-it-formal` has a Lean/Python scaffold for grading formalization strength across domains, also with no commits and no visible license. Both can be named as local work-in-progress; neither should be inflated into a release.

`openai-symphony` and `steward` are real control-plane/provenance side rooms. Symphony has a public concept around isolated autonomous implementation runs managed by an Elixir reference service and dashboard. Steward points toward an Elixir/Postgres provenance/query service over specs, code, tests, reasoning, agent runs, verification, and Git history. Both require redaction because the inspected live surfaces include dirty worktrees, local config, private-corpus or operational references, logs, prompts, or service details. [[work-management-primitives]] remains the useful lens here: durable work objects are interesting only when their custody is legible.

## Research bench / side-room notes

`jepa-lang` is the clean small artifact in the JEPA room: deterministic typed operations, replayable traces, and evidence receipts. `jepa-poker` is publishable at high level as imperfect-information poker world-model work, now visibly oriented around Kuhn/Leduc/player benchmarking. `unconventional-jepa-lab` is a larger research-bench scaffold with explicit lanes and falsification gates, but its local-path, `.beads`, `.codex`, `.gascity`, and dirty packet surfaces keep it curated.

The NNPL trio belongs here as concept-level evidence: external latent bus, shared bus with a documented negative v0 result, and typed-boundary IR. `tinygrad-gemma` and `tinygrad-gemma-kimi` are technically rich, but benchmark/checkpoint/evolution-state and patch-result artifacts mean the public page should say “runtime/optimization research” rather than laundering raw performance claims. `word-games` has pivoted toward Story JEPA / character-interiority modeling, with generated runs and checkpoints held back. This whole room is a useful neighbor to [[neural-native-programming]], provided we remember that an elegant boundary object is not the same thing as solved cognition.

The quieter public-safe side notes are tidy: `handterm` is a clean MIT Rust/Wayland terminal project; `parenting-bookshelf-compass` is a small static humane artifact with README, `index.html`, clean `main`, and a recent publish commit.

## What the desk left out

The public-safety filter fully held back, or reduced to category-only mention, hidden local assistant/settings directories, security/dependency scan artifacts, empty or skeletal directories, one provocative/protected-class-sensitive social-claim notebook, local deployment/model-runner folders, private corpus bodies, prompt/agent/skill instruction bodies, scratch/meta workspaces, generated media, raw logs/prompts/trajectories, evaluator/oracle payloads, raw benchmark outputs, model/checkpoint artifacts, biometric/capture data, creative/canon/world-packet drafts, service configuration, raw test/counterexample bodies, local `.env`-style material, cache/build/vendor directories, dirty patch/reject variants, and too-skeletal placeholders.

This is not coyness. It is the public page refusing to become an incident report.

## Bottom line

- `gemma-dungeon` is tonight's clear same-night lead.
- `cardgame1`, `testing-rl`, `testing-rl-hermes`, and `kettlebellsim` form the strongest public-safe working set.
- Basis/Hermes, `another-harness`, `is-it-formal`, `openai-symphony`, and `steward` remain formal/spec/provenance/control-plane side rooms under redaction.
- `jepa-lang`, `jepa-poker`, `unconventional-jepa-lab`, the NNPL projects, `tinygrad-gemma`, `tinygrad-gemma-kimi`, and `word-games` belong on the research bench with careful caveats.
- `handterm` and `parenting-bookshelf-compass` are the clean side notes.
- The page is deliberately narrower than the source tree. This is not a defect; it is the membrane working.
