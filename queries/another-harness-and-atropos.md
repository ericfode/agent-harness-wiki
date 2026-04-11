---
title: "another-harness and Atropos"
created: 2026-04-10
updated: 2026-04-11
type: query
tags: [comparison, benchmark, tool-execution, work-management]
sources: [raw/articles/another-harness-repo-2026-04-09.md, raw/articles/another-harness-atropos-environment-schema-2026-04-10.md, raw/articles/another-harness-work-item-closure-environment-2026-04-10.md, raw/articles/another-harness-evaluator-discipline-environment-2026-04-10.md, raw/articles/another-harness-run-history-decision-2026-04-11.md, raw/articles/hermes-atropos-integration-2026-04-09.md, raw/papers/arxiv-xi-2024-agentgym.md, raw/papers/arxiv-trivedi-2024-appworld.md, raw/papers/arxiv-pan-2024-swe-gym.md, raw/papers/arxiv-mehta-2026-enterprisebench-corecraft.md]
---

# another-harness and Atropos

## Question
Should `another-harness` adopt Atropos now, and if so, how would it use it without turning a thin repo-native harness into a small bureaucratic empire?

## Verdict
Later for Atropos proper; now for a thin local benchmark substrate.

That answer is not a contradiction. It is a refinement. `another-harness` still should not import full Atropos/trainer machinery yet, but it has now earned two smaller steps in that direction via [[another-harness-work-item-closure-environment]] and [[another-harness-evaluator-discipline-environment]]. The repo now has builder and evaluator executable environment lanes of its own, which means the old “later, not now” judgment still holds for Atropos proper while no longer implying “do nothing until then.”

## Why not now
The repo's own architecture and backlog place the current design center elsewhere:
- active project truth lives in repo artifacts such as work items and evaluation artifacts
- automation is still explicitly pending
- heavier orchestration is supposed to wait until the single-agent path is legible
- the Lean scaffold remains a first-class occupant and should not be swallowed by a training runtime

In short, the repo does not yet have a mature benchmark-and-rollout layer. Adding Atropos immediately would risk importing a training apparatus before the task objects and graders it would optimize have settled down.

## What Atropos would be, if adopted
In the Hermes stack, [[atropos]] is not merely a trainer. It is an environment/runtime contract with rollout, evaluation, and training hookup. If `another-harness` adopted it, the clean use would be as an optional sidecar for repeated execution against explicit repo artifacts, not as the new source of truth.

A concrete follow-on now exists in [[another-harness-atropos-environment-schema]], which turns this high-level fit judgment into a repo-native episode contract and reward design.

## Best use of Atropos for another-harness later
The right shape would be:
1. keep repo artifacts authoritative for intent, evaluation, and handoff
2. let an Atropos environment consume those artifacts as episode definitions
3. score episodes with reality-bearing checks already present in the repo
4. export trajectories and judgments for later policy or workflow improvement

The new local prototypes in [[another-harness-work-item-closure-environment]] and [[another-harness-evaluator-discipline-environment]] now fill in the missing early rungs between design and adoption. They prove the repo can own both a builder contract and an evaluator contract locally before asking Atropos to scale them.

That keeps the current artifact discipline intact while adding a repeated environment around it.

## Current run-history decision

The repo has now answered the first storage question the live loops created: do **not** make `state/runs/` canonical yet.

The reason is simple and annoyingly persuasive:
- the preserved 0028 builder and 0030 evaluator attempts are already replayable through `tools/check_real_loop_smoke.py`
- canonical truth still lives cleanly in work items, evaluation artifacts, and handoffs
- the preserved `run.json` files still contain temporary sandbox-path context, which is useful evidence but shabby canon

So the current Atropos-facing storage story is deliberately thin:
- keep canonical truth in the existing repo artifacts
- preserve historically important attempts as derived evidence bundles under `docs/plans/artifacts/`
- reopen a real run plane only if future many-attempt pressure or resume/recover work genuinely demands it

That matters for Atropos because it says the sidecar does not need permission to create a second operational truth model just because trajectories exist. Repeated execution may be real before a canonical run plane is warranted.

## Plausible environment designs

### 1. Work-item closure environment
- input: one work item plus scope files
- actions: bounded repo edits, command execution, evaluation artifact updates, handoff generation
- reward: passing work-item checker plus passing reality-bearing checks

### 2. Evaluator-discipline environment
- input: partial implementation plus existing work item
- actions: run checks, inspect artifacts, write evaluator verdict
- reward: whether the evaluator artifact matches actual repo state honestly

### 3. Resume-and-recover environment
- input: interrupted work item with handoff
- actions: re-orient, rerun checks, continue work, update evaluation state
- reward: coherent recovery without false completion claims

### 4. Narrow Lean-harness environment
- input: tightly scoped Lean or ontology maintenance task
- actions: build, inspect diagnostics, patch local targets, update evaluation artifact
- reward: `lake build` plus targeted theorem/checker success

## Prerequisites before Atropos is a good idea
- reconcile the docs/backlog with the repo's emerging control-plane surfaces
- stabilize one run/attempt model for repeated execution
- define a small benchmark suite rather than relying on one-off tasks
- make reward hard to game by anchoring it in existing reality-bearing checks
- sandbox repeated execution so the Lean scaffold is not casually vandalized

## Most relevant reference class
For another-harness, the most useful neighboring systems are not the pure web gyms first. They are [[appworld]], [[swe-gym]], [[enterprisebench-corecraft]], and [[agentgym]], because those systems combine explicit tasks, state-based grading, trajectory capture, and eventually training. They look much closer to what a repo-native Codex harness would actually need.

## Bottom line
Atropos looks like the right tool only after `another-harness` has a stable executable task suite. Before that, the repo should keep strengthening its current work/evaluation/handoff discipline. After that, Atropos becomes attractive as a training and rollout sidecar precisely because it can sit beneath those repo-native artifacts instead of replacing them.

## Related pages
Read this with [[another-harness-work-item-closure-environment]], [[another-harness-evaluator-discipline-environment]], [[atropos]], [[rl-gyms-and-executable-environments-for-ai-harnesses]], [[evaluation-and-review-loops]], [[harness-engineering]], and [[swe-gym]].
