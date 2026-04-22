---
title: Gas City Control Plane and Authority Split
created: 2026-04-15
updated: 2026-04-15
type: query
tags: [codex-cli, gas-city, orchestration, tool-execution, work-management]
sources: [raw/articles/gas-city-but-its-just-codex-doc-architecture-and-ops-2026-04-15.md, raw/articles/gas-city-but-its-just-codex-repo-2026-04-15.md]
---

# Gas City Control Plane and Authority Split

## Question
What is the current runnable stack, and where does authority actually live in `gas-city-but-its-just-codex`?

## Short answer
The repo clearly wants a three-service same-host split:
1. one control-plane daemon that owns `redb`, the app-server client, and the authoritative event log
2. one operator daemon that consumes projections and issues typed commands back
3. one UI sidecar that serves projections to the native app

That is the intended clean boundary. The interesting current fact is that the code has not fully finished obeying its own sermon: the UI sidecar still opens the store, loads formulas, spawns Codex app-server, and runs autorun logic. So the architecture is best read as a strong intended split with one still-material duplication seam.

## The intended boxes
The current docs describe the stack as:
- formulas and schemas
- `WorkflowStore` over `redb`
- `App` service
- `gRPC`, `MCP`, and dynamic worker-tool surfaces
- operator and UI processes over those surfaces
- Codex app-server and turns as execution kernel

That keeps the main thesis from [[gas-city-but-its-just-codex]] intact: durable workflow truth lives outside transcript history, while [[codex-app-server]] remains the execution-facing seam.

## Why the split matters
This is not a pedantic process chart. It is an authority question.

If one process owns the store and app-server boundary, then:
- workflow truth stays singular
- projections become plainly derived
- operator behavior is legible as policy rather than magic
- UI behavior stays presentational rather than quietly mutating the republic from backstage

That is the same durable-state discipline discussed more generally in [[work-management-primitives]] and [[harness-engineering]].

## What the docs currently claim
The architecture and runbook cluster says:
- the control plane is the only store-owning authority process
- the operator daemon talks to it over gRPC
- the UI sidecar serves projections over gRPC
- the native macOS app is a pure client
- direct gRPC CLI is now the preferred manual operator path

This is a strong design choice. It turns the gRPC contract into the central same-host boundary rather than letting MCP, app-server, and UI all become rival truths.

## What the code currently still does
The main structural tension is that the sidecar is not merely passive yet.

The current implementation still has the sidecar path:
- open `WorkflowStore`
- load `FormulaRegistry`
- spawn `CodexAppServer`
- start an autorun loop
- then serve gRPC

So the repo has not yet fully reduced the sidecar to pure projection or presentation. It still behaves like a partial local runtime.

## How to read that tension correctly
This should not be read as failure. It should be read as the current interesting seam.

The docs show the architecture the repo wants to stabilize around. The code shows the remaining place where the authority split is not yet fully enforced. That makes this repo especially worth watching: the control-plane question is no longer abstract, because the pressure point is now concrete and inspectable.

## Practical consequence
If you want to understand or extend this repo honestly:
- trust the control-plane-as-authority story more than the sidecar's present convenience behavior
- treat the sidecar/runtime duplication as an open edge, not as evidence that the clean split was a fiction
- read the current stack through the gRPC contract first, not through one incidental launcher or sidecar behavior

## Bottom line
The interesting architectural fact is not merely that the repo has a control plane. It is that the repo now has a clear theory of where authority should live, plus a visible remaining mismatch where the sidecar still does more than a presentation service ought to do. That mismatch is one of the most useful truths in the current codebase.

## Related pages
Read this with [[gas-city-but-its-just-codex]], [[codex-app-server]], [[work-management-primitives]], [[context-engineering]], and [[harness-engineering]].