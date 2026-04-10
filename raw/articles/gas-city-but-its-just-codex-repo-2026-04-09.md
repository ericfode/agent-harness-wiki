---
title: Gas City But It's Just Codex Repository Snapshot
author: local repository synthesis
url: file:///Users/ericfode/src/gas-city-but-its-just-codex
ingested: 2026-04-09
---

# Gas City But It's Just Codex Repository Snapshot

This repository studies how to recreate the durable orchestration value of Gas City using Codex-native primitives and thin adapters rather than a deep Codex fork. The current runtime is a Rust `redb` workflow ledger with graph-native MCP tools, Codex app-server thread binding, and a growing formalization stack under `formal/`.

## Current control-plane shape

- `README.md` describes the active substrate as a durable workflow ledger rather than transcript-only coordination.
- `docs/architecture/current-control-plane-architecture.md` splits the system into a formula layer, ledger layer, application service layer, and execution surfaces.
- `state/evolution-log.md` records the April 9 shift that made formulas first-class mutable objects with lineage, evolution policy, active-variant state, and durable evolved variants under `formulas/evolution/`.
- `docs/evidence/correctness-evidence.md` distinguishes structural correctness from autonomy debt: the frontier benchmark failures are no longer mostly graph-shape failures, but failures of worker behavior under low-intervention budgets.

## Self-evolving workflow surfaces already present

- Recipes and fragments carry family, generation, parentage, and mutation metadata.
- Both top-level MCP tools and worker-turn dynamic tools can list, mutate, assess, and select formulas.
- Workflow metadata records which recipe family and generation actually ran.
- The repo tracks coordination overlays such as shared workspace, negotiated allocation, and coalitions without collapsing them into transcript folklore.

## Most relevant current limitation

The repository now has mutation and selection surfaces for formulas, but the benchmark and evidence documents still emphasize frontier autonomy gaps rather than a fully closed-loop workflow-evolution pipeline. The obvious next pressure point is therefore not merely “can a formula mutate?” but “what evidence promotes a mutation into the active workflow family?”
