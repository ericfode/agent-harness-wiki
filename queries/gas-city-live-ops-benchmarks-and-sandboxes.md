---
title: Gas City Live Ops, Benchmarks, and Sandboxes
created: 2026-04-15
updated: 2026-04-15
type: query
tags: [gas-city, benchmark, work-management, context-engineering]
sources: [raw/articles/gas-city-but-its-just-codex-doc-architecture-and-ops-2026-04-15.md, raw/articles/gas-city-but-its-just-codex-repo-2026-04-15.md]
---

# Gas City Live Ops, Benchmarks, and Sandboxes

## Question
Where does the repo's current operational truth actually live, and which workloads or evaluation surfaces matter most right now?

## Short answer
Not in `docs/plans/`.

The current operational center of gravity is:
- `configs/repo-loop-state.json`
- `state/evolution-log.md`
- `configs/operator-policy/*.json`
- the benchmark harness
- the research-triangulation sandbox and the grounded use-case notes around `research` and `nomic`

That is where the repo stops being an architecture essay and becomes a live machine.

## The live planner of record
The most useful current files are the ones that tell you what the repo thinks it is doing now:
- current checkpoint
- next target
- due non-blocking maintenance work
- dirty-file driven observer state
- policy bindings that change runtime admissibility

This is why the repo should be read with [[gas-city-but-its-just-codex]] and [[evaluation-and-review-loops]] instead of through plan documents alone. The repo has moved to a tighter loop of state file plus evolution log plus runtime snapshot.

## Benchmarks are not an appendix anymore
The benchmark ladder is now one of the most interesting parts of the repo.

It distinguishes:
- green baseline tracks
- deliberately red frontier tracks

That is good taste. It means the repo is trying to separate "works at all" from "works with low enough intervention to count as real progress." The frontier failures are therefore useful because they isolate autonomy debt rather than merely exposing graph-shape bugs.

This is exactly the kind of discipline discussed more generally in [[evaluation-and-review-loops]].

## Research is the cleanest live workload
The `research-triangulation` path looks like the clearest current operational workload.

Why it matters:
- it is bounded
- it uses copied execution repos rather than contaminating the source checkout
- it exercises the multi-role workflow substrate with readers, critic, synthesizer, and verifier
- it has a real sandbox and acceptance-test story

So the repo has at least one grounded workload that already fits its abstractions rather than merely being promised by them.

## Nomic is the sterner abstraction test
The `nomic` workload matters for a different reason.

It pressures:
- cross-workflow lineage
- phase and barrier visibility
- promotion or ratification semantics
- richer artifact-state views

The repo can already run enough of this workload to make the pressure real. What it does not yet have is perfect legibility for that program-shaped workload. That is why the next generic read-model work matters.

## The development observer is one of the quietly interesting bits
A good deal of the repo's seriousness lives in the development observer layer.

It encodes the idea that some work should be durable and visible without pretending it is a graph blocker. Formalization drift and observer-surface sync can become due work without rewriting the main workflow graph into a small religion of fake blockers.

That is a subtle but important architectural choice, and one worth keeping in view beside [[context-engineering]] and [[work-management-primitives]].

## What the repo currently says about itself
At inspection time the repo's own development snapshot said:
- current checkpoint: `recipe-policy-bridge-088`
- next target: `phase-summary-workspace-coverage-089`
- due items: `formalize-after-runtime-change` and `observer-surface-sync`

This tells you two useful things:
1. the repo's live self-description is explicit and queryable
2. the next bottleneck is legibility and projection quality, not lack of architectural ambition

## Why this matters for the wiki
If the wiki only rendered the architecture notes, it would miss the most interesting operational truth.

What makes this repo worth tracking is not only its clean diagrams, but also:
- that it has live benchmark pressure
- that it has sandboxed workloads
- that it encodes its own maintenance drift as observable overlay work
- that its current target is improving generic program read models

Those are the parts that show whether the control plane is becoming a usable system rather than an increasingly ornate shelf of components.

## Bottom line
The repo's live interesting bits are now operational as much as architectural. The real story sits where benchmarks, sandboxes, policy files, development snapshots, and the evolution log meet. That is where you can tell what the system actually is becoming, rather than what its docs once hoped it might be.

## Related pages
Read this with [[gas-city-but-its-just-codex]], [[evaluation-and-review-loops]], [[work-management-primitives]], [[context-engineering]], and [[self-evolving-workflows]].