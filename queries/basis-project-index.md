---
title: Basis Project Index
created: 2026-05-10
updated: 2026-05-11
type: query
tags: [survey, formal-methods, context-engineering, work-management, code-quality, safety]
sources: [raw/articles/basis-project-deep-dive-2026-05-10.md, raw/articles/basis-reduce-imagine-codex-log-sift-2026-05-11.md, queries/nightly-src-projects-desk-2026-05-10.md, queries/nightly-src-projects-desk-2026-05-09.md, queries/spec-dataset-evolution-research-project.md, queries/spec-deep-dive-index.md]
---

# Basis Project Index

## Question

What is Basis, what experiments are running, what are the plans, and how is it going?

## Short answer

Basis is the local spec-state research line for turning messy prose specifications into structured, provenance-backed, reviewable state. It sits between [[llm-readable-spec-files]], [[context-engineering]], [[work-management-primitives]], and [[formal-methods-for-agent-harnesses]]: specifications should remain readable to humans, but their durable authority should live in explicit records, evidence, acceptance boundaries, and projections.

The project is not one repo. It is a cluster:

| Surface | Role | Status |
|---|---|---|
| `basis` | Elixir/BEAM core for live reducer and imaginer state | clean, tests/compile pass, format gate currently red |
| `basis-hermes` | Hermes plugin and dashboard bridge for deterministic reducer/validator tools | clean, Python and JS gates pass |
| `basis-jcode` | Jcode-native headless reducer/control-plane experiment | ahead and dirty, tests pass, raw runs private |
| `steward` | benchmark-first spec-code grounding project | design seed; empirical pressure path, not Basis runtime |

This corner is public-safe synthesis. It does not publish `.basis` run bodies, prompts, raw packets, event streams, logs, private corpus material, or dashboard payloads. The point is to keep the signal without laundering the private workshop floor into public prose.

## Navigation

- [[basis-reduce-workbench]] — recovered Basis.Reduce workbench, UI artifacts, control-gate status, and spec-pathology experiment lane.
- [[basis-imagine-workbench]] — recovered Basis.Imagine workbench, future-tradeoff UI, app-server-backed lenses, and proposal-only caveats.
- [[basis-architecture-and-plans]] — architecture, planned boundaries, and near-term work.
- [[basis-experiment-status]] — experiments currently running or implied by repo state.
- [[basis-source-basis-and-safety-gate]] — evidence table, safety boundary, and publication rules.
- [[spec-dataset-evolution-research-project]] and [[spec-deep-dive-index]] — corpus and spec-code research pressure feeding this line of work.

## Current rollup

| Question | Answer |
|---|---|
| Is the core idea coherent? | Yes. The core Basis spec is precise: Markdown can bootstrap and project state, but accepted structured records are the intended authority. |
| What works today? | Core source/run surfaces exist; `basis-hermes` exposes deterministic reduction/validation; `basis-jcode` can run a headless control-plane loop with tests and a local dashboard. |
| What is the cleanest surface? | `basis-hermes`, because it is clean, test-passing, and installed as the Hermes plugin surface. |
| What is the richest experiment? | `basis-jcode` self-convergence, because it exercises ledgers, worker packets, validation, UI projection, and acceptance decisions. |
| What is the main caution? | The richest evidence is inside private `.basis` run trees and dashboard state; public pages should summarize architecture/counts, not bodies. |
| What is currently red? | Core `basis` still needs consolidation; the recovered reducer pathology study is untracked, and the imaginer worktree is dirty with a large active diff. |
| What was missing from the wiki? | [[basis-reduce-workbench]] and [[basis-imagine-workbench]], now recovered from Codex logs/worktrees with generated UI artifacts and safety caveats. |

## Why this matters

Ordinary specs decay because prose becomes authority by accident. Basis tries to separate:

- source topology: files, sections, ranges, hashes;
- execution topology: workers, forks, packets, events;
- semantic topology: claims, constraints, assumptions, interfaces, conflicts, accepted decisions;
- projection topology: Markdown, dashboards, tests, proof obligations, code-facing views.

That separation is the system's taste. Collapse it and the project becomes a very elaborate note-taking app with opinions. Preserve it and Basis becomes a custody mechanism for specification meaning.

## Relationship to adjacent work

- [[spec-dataset-evolution-research-project]] provides empirical pressure: real repositories have many spec-like surfaces, varying authority levels, and uneven code connection.
- [[spec-deep-dive-index]] supplies public-safe cases for how specs connect to code, tests, standards, and agent-native scaffolds.
- [[evaluation-and-review-loops]] supplies the discipline: proposed records need gates, not merely confidence.
- [[safety-and-permissions]] supplies the publication boundary: private run artifacts stay private unless explicitly reviewed.
- [[hermes-agent]] is the integration context for the `basis-hermes` plugin.

## Status sentence

As of 2026-05-11, Basis is an active spec-code reducer/control-plane line with one clean Hermes bridge, a reducer workbench branch whose recent review/decision UI commits are tracked, an untracked but substantial spec-pathology experiment lane, and a dirty imaginer worktree that has separate future-tradeoff/architecture surfaces but must remain proposal-only until reviewed.
