---
title: Gas City But It's Just Codex Documentation and Operations Bundle (2026-04-15)
author: local repository synthesis
url: file:///Users/ericfode/src/gas-city-but-its-just-codex/docs
ingested: 2026-04-15
---

# Gas City But It's Just Codex Documentation and Operations Bundle (2026-04-15)

This raw note preserves the main repo documentation clusters and the operational facts they currently emphasize.

## Architecture cluster

Primary docs inspected:
- `docs/architecture/current-control-plane-architecture.md`
- `docs/architecture/application-stack.md`
- `docs/architecture/same-host-three-service-architecture.md`
- `docs/architecture/workflow-operator-semantics.md`
- `docs/architecture/recipe-workflow-policy-semantics.md`
- `docs/architecture/use-case-evaluation.md`
- `docs/architecture/development-observer-architecture.md`

Main points these docs collectively assert:
- the runtime is a five-layer control plane around Codex-native execution
- the desired same-host split is one control-plane daemon, one operator daemon, one UI sidecar, and one pure native client
- operator policy is a typed observational layer over workflow state, not a second authority kernel
- the recipe/workflow/policy bridge should unify only at a narrow boundary rather than collapsing compile-time and run-time semantics into one language
- research and nomic are the two grounded workload families used to pressure the abstractions
- non-blocking maintenance and development observation should live as overlay state, not fake blockers on the main graph

## Usage and runbook cluster

Primary docs inspected:
- `docs/usage/control-plane-grpc-cli.md`
- `docs/usage/three-service-stack.md`
- `docs/usage/research-triangulation.md`
- `docs/usage/progression-test-ladder.md`

Main points these docs collectively assert:
- direct gRPC CLI is now the preferred manual operator path for reads, mutations, and subscriptions
- the same-host three-process runbook is the intended local deployment shape
- research triangulation is a bounded many-agent workflow against an isolated copied checkout
- the progression ladder measures whether the system is actually becoming more capable rather than merely more baroque
- the benchmark suite distinguishes green baseline tracks from deliberately red frontier tracks

## Implementation and evidence cluster

Primary docs inspected:
- `docs/implementation/implementation-map.md`
- `docs/evidence/correctness-evidence.md`
- `README.md`
- `configs/repo-loop-state.json`
- `state/evolution-log.md`

Main points these docs collectively assert:
- the real model has moved into `crates/workflow-core`, even if some docs still speak of `src/model.rs`
- the control-plane gRPC surface has become a first-class runtime contract rather than a convenience wrapper
- the benchmark suite, runbooks, and maintenance rules are part of the repo's visible correctness case
- the live worktree is ahead of the last clean commit and currently identifies itself as `recipe-policy-bridge-088` with next target `phase-summary-workspace-coverage-089`
- the interesting current pressure is not inventing more orchestration shapes, but making the widened runtime legible through better read models and projections

## Honest tension carried by the docs

The architecture docs want a cleaner authority split than the current code fully enforces.

In particular:
- the docs say only the control-plane daemon should own `redb` and the app-server client
- the current sidecar implementation still opens the store, loads formulas, spawns Codex app-server, and runs an autorun loop

So the documentation is useful and revealing, but it still describes a slightly cleaner future-facing topology than the fully disentangled implementation now provides.

## Why this bundle matters

The repo is no longer mainly interesting as a design thesis. It now has enough real documentation strata that the documentation itself becomes part of the object under study:
- architecture notes show the intended clean decomposition
- usage docs show the surviving operational seams
- implementation/evidence docs show where the repo thinks truth and proof currently live
- state/config artifacts show what the repo believes it is doing right now

That is the level at which the repo becomes worth rendering into the external harness wiki rather than merely being remembered as "that Gas City over Codex idea."