---
title: Gas City But It's Just Codex
created: 2026-04-07
updated: 2026-04-21
type: query
tags: [codex-cli, gas-city, orchestration, tool-execution, work-management]
sources: [raw/articles/gas-city-but-its-just-codex-repo-2026-04-15.md, raw/articles/gas-city-but-its-just-codex-repo-2026-04-09.md, entities/codex-app-server.md, entities/codex-cli.md, entities/gas-city.md, concepts/work-management-primitives.md, queries/prompt-program-architecture-plans-for-another-harness-and-gas-city.md]
---

# Gas City But It's Just Codex

## Verdict
This repo is no longer a tiny MCP experiment wrapped around a romantic thesis. It is now a substantial Codex-native control plane with five real layers:

1. a formula layer
2. a durable `redb` workflow ledger
3. an `App` orchestration service
4. multiple typed control surfaces (`gRPC`, `MCP`, app-server dynamic tools, operator daemon, native UI path)
5. an explicit evidence layer of schemas, benchmarks, runbooks, live artifacts, and Lean-backed semantics

The core thesis still holds, however: keep durable workflow state outside transcript history, and treat Codex threads and turns as execution containers rather than the durable system of record.

## One honesty note before the tour
The current snapshot is from the live worktree on 2026-04-15, not only from the last clean commit.

That matters because the repo currently reports:
- `currentCheckpoint = recipe-policy-bridge-088`
- `nextTarget = phase-summary-workspace-coverage-089`

while Git HEAD is still at the preceding policy-routing commit. So the most current truth is the repo's own control artifacts plus the dirty worktree, not merely the last tidy commit message. This is, regrettably for tidy metaphysics, the correct answer.

## Layer 0 map

```text
[formulas + schemas]
          -> [WorkflowStore / redb ledger]
          -> [App service]
          -> [gRPC API | MCP tools | dynamic worker tools]
          -> [operator daemon | sidecar/native UI]
          -> [benchmarks | runbooks | formal model | live artifacts]
```

## 1. Authoritative state lives in the ledger
The most important architectural fact is still the externalization of durable work state.

The authoritative substrate is `WorkflowStore` over `redb`, not Codex history. It owns:
- workflow metadata
- node and edge records
- append-only event history
- durable worker bindings
- shared-workspace entries
- negotiated allocation rounds and bids
- coalition records plus split/merge transitions
- observer cursors and dispatch watches
- overlay-view definitions and saved projections

This is the real implementation of the broader point in [[work-management-primitives]]: the work graph is durable and inspectable, not merely implied by scrollback.

## 2. The model moved into `workflow-core`
An important current structural detail is that the root crate no longer really owns the model layer. `src/model.rs` is now a re-export shim, while the actual domain structs live in `crates/workflow-core/`.

That crate now holds the canonical workflow graph objects, worker binding objects, workspace and allocation objects, coalition objects, and the main snapshot/view types used throughout the runtime. So the repo has effectively become a small workspace, not a single Rust crate with some auxiliary folders stapled on.

## 3. The formula layer is small but real
The tracked formulas are still strikingly compact:
- `repo-loop`
- `research-triangulation`
- `open-question-triangulation`
- `breakdown` fragment

That is the right kind of small. It means formulas are being treated as live operating assets rather than as a bloated graveyard of half-loved workflow folklore.

What changed since the original spike is that formulas are no longer static templates. The runtime now carries:
- lineage and family metadata
- mutation and assessment surfaces
- active-family selection state
- deterministic step execution

This is the repo's concrete bridge toward [[self-evolving-workflows]]: not yet a grand self-editing civilization, but clearly more than inert JSON templates.

## 4. `App` is the policy boundary, not a thin convenience wrapper
`src/app.rs` is where the repo's real operational taste shows up.

It is the boundary between:
- authoritative ledger state
- formula resolution
- worker-thread continuity
- dispatch/recover/handoff/expand logic
- live thread inspection
- typed control-surface responses

So the repo is not just "ledger plus tools." It is ledger plus a real orchestration kernel that decides how durable state and execution-state meet.

That is why this repo should be read with [[codex-cli]] and [[codex-app-server]] rather than as a Gas City imitation in costume. The execution seam is specifically Codex-native.

## 5. Codex remains the execution kernel
The app-server adapter keeps the original thesis honest.

Threads and turns are execution containers. They are not the authoritative work graph.

That is the right separation. If the repo collapsed durable workflow state back into Codex conversation history, it would lose the main thing it claims to be building. The controller would become transcript archaeology with better manners.

## 6. The gRPC surface is now the richest contract in the system
There are three distinct control surfaces:

### Operator-side top-level control
The MCP surface exposes graph-native tools such as:
- `workflow_start`
- `workflow_view`
- `node_claim`
- `node_dispatch`
- `node_report`
- `node_recover`
- `node_handoff`
- `node_expand`
- workspace, allocation, and coalition tools
- `worker_peek`

### In-turn worker control
Dispatched worker turns get dynamic tools such as:
- `ledger_current_view`
- `ledger_workspace_publish`
- `ledger_workspace_list`
- `ledger_current_report`
- `ledger_current_expand`
- `ledger_claim`
- formula list/mutate/assess/select tools

### Typed control-plane gRPC
The broadest surface now appears to be the control-plane gRPC API, which carries:
- health and workflow listing/snapshots
- event cursors and observer-session state
- subscriptions
- overlay and commentary projections
- thread/turn inspection
- typed tool calls
- policy/routing payloads in workflow snapshots

So the repo's current architecture is not best described as "an MCP server." It is better described as a ledger-centric control plane with MCP as one of several operator-facing skins.

## 7. The intended three-process split is cleaner than the current implementation
The docs now clearly want a same-host split of:
1. one store-owning control-plane daemon
2. one external operator daemon over gRPC
3. one UI sidecar serving projections over gRPC
4. one macOS app as a pure client

That is a sensible shape.

But the current code still shows a more entangled reality:
- `crates/operator-ui/src/main.rs` opens `WorkflowStore`
- it loads `FormulaRegistry`
- it spawns `CodexAppServer`
- it starts an autorun loop
- `scripts/run-operator-ui-sidecar.sh` launches that binary directly with DB/formulas/codex arguments

So the repo currently documents a purer authority split than it has yet enforced.

This is the most important structural caution in the current codebase. The system wants one store-owning authority process, but the sidecar path still behaves like a partial second runtime.

## 8. The operator daemon is now a real runtime participant
The operator daemon is no longer a decorative future note. It is an external controller over the gRPC surface that:
- polls workflow state
- consumes event deltas
- evaluates admissibility through the operator-policy view
- claims and dispatches work
- watches active turns
- steers or closes work after watch windows
- auto-closes completed research nodes in some paths

That makes the repo feel much closer to a true control plane than to a static workflow description engine.

## 9. The live operating loop has shifted away from `docs/plans/`
A very important current-structure detail is where the live planner actually lives.

If you want the current operational truth, read:
- `configs/repo-loop-state.json`
- `state/evolution-log.md`
- `configs/operator-policy/*.json`
- the active sandbox/runtime artifacts

`docs/plans/` is still valuable history, but it no longer appears to be the primary live control artifact. The repo has moved toward a tighter loop of state file plus evolution log plus runtime snapshot.

## 10. The research sandbox is not ornamental
The `sandbox/research-triangulation-wiki/` path now looks like the clearest live workload.

That matters because it means the repo is not only reasoning about control-plane architecture in prose. It is also exercising the architecture in a bounded copied-repo workload with a real control plane, operator daemon, and native UI path.

By contrast, some older state DBs and dated plan files now read more like useful archaeological layers than the active frontier.

## 11. Formalization is active, not ceremonial
The `formal/` subtree is not a post-hoc plaque explaining why the architecture is tasteful.

The current worktree is actively extending the Lean side again:
- the evolution log records `recipe-policy-bridge-088`
- the new bridge note lives in `docs/architecture/recipe-workflow-policy-semantics.md`
- the new Lean file is `formal/CodexGasCityFormal/RecipeWorkflowSemantics.lean`

So the repo's current structure is not just runtime plus docs. It is runtime plus formal bridge, with the bridge still being extended.

That makes this repo one of the sterner inhabitants of the control-plane zoo. Not the biggest, perhaps, but certainly one of the ones least interested in flattering itself cheaply.

## 12. Evidence layer and present checks
At inspection time:
- `cargo run -- validate-formulas` passed
- `cargo run -- development-snapshot --db state/workflows.redb` passed

The development snapshot also reported two due non-blocking maintenance obligations:
- `formalize-after-runtime-change`
- `observer-surface-sync`

That is useful because it shows the repo is trying to encode its own drift hygiene instead of leaving synchronization duties to pious memory.

## Main real choices, in plain language
The implementation choices that seem genuinely in force are:
- keep durable workflow state outside transcript history
- keep Codex as the execution kernel
- prefer thin adapters and typed surfaces over a deep Codex fork
- keep formulas small and explicit rather than magical and ambient
- support multiple coordination modes over one authoritative ledger rather than hard-coding one manager tree forever
- move operator policy into typed, file-backed JSON specs rather than freezing it inside Rust constructors
- treat the formal layer as an active constraint surface, not merely as retrospective decoration

## The current open edges that matter most
1. The same-host three-process story is cleaner in docs than in code.
2. `AGENTS.md` still speaks as if the repo is choosing its first executable spike, which is now historically charming but operationally stale.
3. The next explicit target is not a new orchestration fantasy; it is the phase/barrier and workspace-coverage read-model backlog.
4. The worktree is currently mid-increment, so the honest current structure is slightly ahead of the last committed one.

## Rendered subpages
The repo is now broad enough that one giant note is not the best rendering surface. The current focused follow-on pages are:
- [[gas-city-control-plane-and-authority-split]] — the intended three-service authority split, plus the still-important sidecar/runtime duplication seam
- [[gas-city-operator-policy-and-formal-bridge]] — the typed operator-policy runtime and the newer recipe/workflow/policy bridge work
- [[gas-city-live-ops-benchmarks-and-sandboxes]] — where the repo's live operational truth sits across checkpoints, sandboxes, and benchmark pressure

## Bottom line
The repo has matured from "Gas City but with Codex seams" into a real control-plane workspace:
- ledger-centric
- formula-driven
- Codex-executed
- gRPC-heavy
- policy-aware
- benchmarked
- Lean-bridged

If I compress the whole thing into one sentence, it is this:

Gas City But It's Just Codex is now a live attempt to externalize orchestration, policy, and observation into a durable control plane around Codex-native execution, with the main remaining structural tension being that the architecture wants a cleaner authority split than the current sidecar implementation has fully achieved.

## Related pages
Read this with [[gas-city]], [[codex-app-server]], [[codex-cli]], [[work-management-primitives]], [[self-evolving-workflows]], [[gas-city-control-plane-and-authority-split]], [[gas-city-operator-policy-and-formal-bridge]], [[gas-city-live-ops-benchmarks-and-sandboxes]], and [[prompt-program-architecture-plans-for-another-harness-and-gas-city]].
