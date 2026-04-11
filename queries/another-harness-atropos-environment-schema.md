---
title: "another-harness Atropos environment schema"
created: 2026-04-10
updated: 2026-04-10
type: query
tags: [comparison, benchmark, tool-execution, work-management]
sources: [raw/articles/another-harness-atropos-environment-schema-2026-04-10.md, raw/articles/another-harness-work-item-closure-environment-2026-04-10.md, raw/articles/another-harness-evaluator-discipline-environment-2026-04-10.md, raw/articles/another-harness-repo-2026-04-09.md, raw/articles/hermes-atropos-integration-2026-04-09.md, raw/papers/arxiv-trivedi-2024-appworld.md, raw/papers/arxiv-pan-2024-swe-gym.md, raw/papers/arxiv-mehta-2026-enterprisebench-corecraft.md]
---

# another-harness Atropos environment schema

## Goal
Turn the earlier “later, not now” Atropos fit judgment into a concrete design: if `another-harness` eventually adopts an Atropos-style environment layer, what exactly should the contract look like?

## Main design move
The repo spec makes one excellent decision immediately: Atropos is a sidecar around canonical repo artifacts, not a new source of truth. Episodes are derived from work items, evaluations, and handoffs. They are not allowed to invent a cleaner parallel ontology and quietly declare the old files legacy baggage.

That is the right answer for this repo because `another-harness` is not a blank-slate trainer project. It is a repo with durable work artifacts, a Lean scaffold, and a deliberate insistence that completion claims flow through separate evaluator artifacts.

## Environment families
The schema defines four families, in the correct order of seriousness:
1. **work-item closure** — builder episodes for bounded artifact completion
2. **evaluator discipline** — separate reviewer episodes that grade honestly
3. **resume/recover** — continuation episodes for interrupted work
4. **lean maintenance** — deferred until the first three are stable

This ordering matters. It resists the usual urge to sprint directly into “train the theorem-prover agent” before the repo has even proved it can close ordinary bounded work slices coherently.

## Why the evaluator lane matters
The most important refinement in the concrete schema is explicit role-specific permissions. Builder-style episodes may not set `approved_for_completion`. Evaluator episodes may write the evaluation artifact but may not casually edit implementation deliverables. That keeps the repo's existing work/evaluation split alive inside the environment layer instead of letting training flatten it back into one actor praising itself.

## Reward shape
The reward contract is grounded in reality-bearing checks and penalties for:
- false completion claims
- out-of-scope edits
- missing handoff updates
- missing evaluation artifacts
- failed real checks

This is exactly what the repo needs. A thinner harness should learn to respect its own paperwork because, in this architecture, the paperwork is not bureaucracy; it is the mechanism that prevents transcript folklore from becoming state.

## Storage and runtime stance
The schema is careful about the run layer. It permits either:
- a future `state/runs/` file-first attempt log, or
- a projection through `plugins/codex-control-plane/`

But it refuses to let either become a competing truth model. That is the correct restraint. Once a second source of truth appears, the harness stops being thin and starts becoming a small constitutional crisis.

## What it implies for implementation
The first real prototype should almost certainly be the **work-item closure** environment, executed in isolated worktrees, with reward computed by the repo's existing checkers. Only after that is stable should the repo attempt evaluator-discipline training or more ambitious resume/recover tasks.

For reference classes, the best neighboring systems remain [[appworld]], [[swe-gym]], [[enterprisebench-corecraft]], and [[atropos]]. They all combine explicit task contracts, real checks, and trajectory capture, which is closer to what `another-harness` wants than the pure browser-gym line alone.

## What happened next
That recommended first prototype now exists as [[another-harness-work-item-closure-environment]], and the evaluator complement now exists as [[another-harness-evaluator-discipline-environment]]. This matters because it confirms the schema was not merely tasteful prose: the repo can actually compile bounded builder episodes, separate reviewer episodes, freeze grading contracts, and harden the benchmark surface against several concrete gaming attacks before introducing heavier rollout machinery.

## Bottom line
The concrete schema is good because it does not confuse “we could use RL infrastructure” with “the repo should now revolve around RL infrastructure.” It describes a disciplined path where Atropos could later amplify the repo's existing artifact-first loop, rather than replacing it with trainer-centric mythology. The new builder and evaluator prototypes strengthen that judgment by showing the repo can instantiate the first two families locally before asking Atropos to carry more weight.

## Related pages
Read this with [[another-harness-work-item-closure-environment]], [[another-harness-evaluator-discipline-environment]], [[another-harness-and-atropos]], [[atropos]], and [[rl-gyms-and-executable-environments-for-ai-harnesses]].
