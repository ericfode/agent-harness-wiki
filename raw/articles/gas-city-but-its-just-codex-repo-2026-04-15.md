---
title: Gas City But It's Just Codex Repository Snapshot (2026-04-15)
author: local repository synthesis
url: file:///Users/ericfode/src/gas-city-but-its-just-codex
ingested: 2026-04-15
---

# Gas City But It's Just Codex Repository Snapshot (2026-04-15)

This raw note preserves the current repo state as inspected from the live local worktree on 2026-04-15.

## Branch and worktree state

- Repo: `/Users/ericfode/src/gas-city-but-its-just-codex`
- Branch: `main`
- HEAD at inspection: `0bc527d` (`Align policy routing runtime with Lean semantics`)
- Important honesty note: the worktree is dirty and appears to be mid-increment beyond HEAD.
- `cargo run -- development-snapshot --db state/workflows.redb` reports:
  - `currentCheckpoint = recipe-policy-bridge-088`
  - `nextTarget = phase-summary-workspace-coverage-089`
  - two non-blocking due items: `formalize-after-runtime-change` and `observer-surface-sync`

In other words, the repo's operative self-description has already moved past the last committed Git history. That is not a contradiction; it is merely a live worktree refusing to pretend otherwise.

## Current top-level structure

The important directories right now are:

- `src/` — root runtime crate: app service, store, app-server adapter, MCP, gRPC, development/commentary/overlay services
- `crates/workflow-core/` — canonical workflow model types
- `crates/workflow-observer/` — dispatch-watch observation state machine
- `crates/operator-daemon/` — external operator over gRPC
- `crates/operator-ui/` — sidecar-style runtime plus gRPC surface and autorun loop
- `apps/operator-ui-macos/` — native SwiftUI macOS client
- `formulas/` — tracked recipes/fragments
- `configs/` — repo-loop state, operator-policy JSON specs, research configs, progression ladder
- `state/` — default `workflows.redb`, historical run artifacts, maintenance state, evolution log
- `benchmarks/` — file-backed real app-server benchmark projects and blind verifiers
- `sandbox/` — especially the active `research-triangulation-wiki` sandbox
- `formal/` — Lean model and related documentation
- `docs/architecture/`, `docs/specifications/`, `docs/implementation/`, `docs/evidence/`, `docs/usage/` — current explanatory and operational surfaces

## Canonical control-plane shape

The repo's current architecture documents describe a five-layer control plane:

1. formulas and schemas
2. `WorkflowStore` in `redb`
3. `App` service
4. interface surfaces (`gRPC`, `MCP`, app-server dynamic tools, operator daemon, UI sidecar)
5. evidence layer (schemas, tests, benchmarks, runbooks, formal model, live artifacts)

Primary files inspected for this:

- `README.md`
- `docs/architecture/current-control-plane-architecture.md`
- `docs/requirements/control-plane-requirements.md`
- `docs/specifications/workflow-ledger-specification.md`
- `docs/implementation/implementation-map.md`
- `docs/evidence/correctness-evidence.md`

## Runtime and model structure

### Durable model and ledger

- The real model types now live in `crates/workflow-core/src/lib.rs`, while `src/model.rs` is just a re-export shim.
- `WorkflowStore` in `src/store.rs` is authoritative for:
  - workflow metadata
  - nodes and edges
  - append-only events
  - worker bindings
  - shared-workspace entries
  - allocation rounds and bids
  - coalition records and transitions
  - observer cursors and dispatch watches
  - overlay-view definitions and saved projections

### Formula layer

Tracked formulas are intentionally small and current:

- `formulas/recipes/repo-loop.json`
- `formulas/recipes/research-triangulation.json`
- `formulas/recipes/open-question-triangulation.json`
- `formulas/fragments/breakdown.json`

The formula runtime in `src/formula.rs` now supports lineage, mutation, assessment, and active-family selection. Deterministic step settlement lives in `src/deterministic.rs`.

### App service and execution kernel

`src/app.rs` is the policy/orchestration boundary between the ledger and Codex runtime operations. It resolves recipes/fragments, claims nodes, dispatches worker turns, handles recover/handoff/expand, and enriches workflow snapshots with thread state.

Codex remains the execution kernel through `src/app_server.rs`. The important design choice is still: threads and turns are execution containers, not the durable system of record.

### Control surfaces

Three control surfaces matter most:

- top-level MCP tools in `src/mcp.rs`
- in-turn dynamic tools injected through the app-server adapter in `src/app_server.rs`
- the broad typed gRPC API in `crates/operator-ui/proto/operator_ui.proto` plus `src/control_plane_grpc.rs`

The gRPC surface now appears to be the richest contract in the system.

## Operator, sidecar, and native UI

The intended same-host split in docs is:

1. control-plane daemon owns `redb`, app-server, and gRPC authority
2. operator daemon consumes gRPC and steers work
3. UI sidecar serves projections over gRPC
4. macOS app acts as a pure client of the sidecar

Relevant docs:

- `docs/architecture/application-stack.md`
- `docs/architecture/same-host-three-service-architecture.md`
- `docs/usage/three-service-stack.md`

Important current implementation reality from inspected code:

- `crates/operator-ui/src/main.rs` still opens `WorkflowStore`, loads `FormulaRegistry`, spawns `CodexAppServer`, and starts an autorun loop.
- `scripts/run-operator-ui-sidecar.sh` launches that binary directly with DB/formulas/codex arguments.

So the repo currently documents a cleaner three-service authority split than the code fully enforces. The sidecar is not merely a passive projection shim yet.

## Operational center of gravity now

The files that best describe what is active right now are:

- `configs/repo-loop-state.json`
- `state/evolution-log.md`
- `configs/operator-policy/default-current.json`
- `configs/operator-policy/research-current.json`
- `configs/operator-policy/nomic-current.json`

This is where the live operating loop, checkpoint, and next target actually reside. `docs/plans/` is still useful archaeological history, but it is no longer the main planner of record.

## Formal and evaluation surfaces

- `formal/` is active, not decorative. The 2026-04-15 evolution-log entry adds `formal/CodexGasCityFormal/RecipeWorkflowSemantics.lean` and the new architecture note `docs/architecture/recipe-workflow-policy-semantics.md`.
- `benchmarks/` remains the file-backed real-app-server evaluation harness.
- `cargo run -- validate-formulas` passed at inspection time.

## Most important current tensions

1. The repo is preserving the original thesis — external durable control plane over Codex-native execution seams — while growing into a much larger runtime than the original tiny MCP spike.
2. The control-plane gRPC contract has become central enough that multiple other surfaces orbit it.
3. The sidecar/UI split is still partially duplicated in implementation.
4. The active worktree is mid-increment and truthfully says so through `repo-loop-state.json` and `state/evolution-log.md`.
5. The next pressure point is not "invent more orchestration" but making the phase/barrier and workspace coverage read-models match the widened runtime and formal bridge.

## Commands run during inspection

- `git status --short --branch`
- `git log -5 --oneline --decorate`
- `cargo run -- validate-formulas`
- `cargo run -- development-snapshot --db state/workflows.redb`

## Bottom line

The current repo is no longer a note about how one might rebuild Gas City over Codex. It is a live, layered control-plane implementation with a durable ledger, formula runtime, typed gRPC and MCP control surfaces, operator automation, a native UI path, benchmarks, and an active Lean bridge — but it still carries some honest structural tension between the clean split described in docs and the more entangled sidecar/runtime arrangement that exists in code today.
