---
title: "another-harness work-item closure environment"
created: 2026-04-10
updated: 2026-04-10
type: query
tags: [benchmark, tool-execution, work-management]
sources: [raw/articles/another-harness-work-item-closure-environment-2026-04-10.md, raw/articles/another-harness-evaluator-discipline-environment-2026-04-10.md, raw/articles/another-harness-atropos-environment-schema-2026-04-10.md]
---

# another-harness work-item closure environment

## Question
What does it mean for `another-harness` to instantiate the first real executable environment slice under its Atropos sidecar design without prematurely turning itself into a trainer laboratory?

## Short answer
It means the repo now owns a small but real benchmark harness: a builder-side `work_item_closure` family with synthetic repo-native fixtures, isolated git worktrees, frozen baseline contracts, and deterministic noop-versus-oracle regression.

That is much more serious than the earlier schema alone, but still much less than full Atropos adoption.

## Why this matters
The key transition is from design to executable evidence. The earlier schema in [[another-harness-atropos-environment-schema]] said the first viable family should be work-item closure in isolated worktrees. This prototype now makes that sentence true.

That matters because it gives the repo:
- bounded episode preparation from canonical work/evaluation/handoff artifacts
- a real reward and penalty surface grounded in repo checks
- a place to test anti-gaming discipline before adding trainer machinery
- an executable stepping stone between a file-backed benchmark ladder and a true RL substrate like [[atropos]] or [[agentgym]]

## Most important design move
The best move in the implementation is not merely “there is a runner now.” It is that the runner freezes the grading contract in the baseline commit and refuses to let the mutable sandbox work item redefine acceptance checks, deliverables, or artifact bindings.

That is exactly the sort of thing one wants in a serious harness benchmark. Otherwise the benchmark becomes a small theology of task self-redefinition rather than a measurement surface.

## What the prototype actually proves
The repo now demonstrates all of the following in executable form:
1. **Episode compilation** from repo-native artifacts
2. **Isolated worktree execution** around a temporary baseline repo
3. **Reward grounded in real checks** rather than summaries alone
4. **Penalty for scope and contract violations**
5. **Deterministic regression** where oracle runs beat noop
6. **Review-driven hardening** against several concrete gaming attacks

The last point is important. The slice was not accepted on first draft. It had to be tightened against committed-tamper invisibility, mutable contract rewriting, sibling metadata tampering, git replace-ref forgery, file-prefix scope abuse, and baseline-metadata mismatch. That is reassuring. Benchmarks worth caring about generally have to earn their paranoia.

## What it still does not prove
The prototype does not yet show:
- resume/recover episodes
- persistent `state/runs/` history as canonical repo state
- trainer hookup or large-scale rollout orchestration
- real model trajectory capture beyond the current coarse run artifacts

It is also no longer the repo's only executable environment lane. The reviewer-side complement now exists in [[another-harness-evaluator-discipline-environment]], which means the main remaining conceptual gap is no longer "can the repo benchmark anything at all?" but rather "how should the next family extend the two-lane substrate without turning it into a small state religion?"

So the right reading is not “Atropos now, immediately.” The right reading is “the repo finally has a small executable substrate on which later Atropos-style machinery could rest without becoming decorative nonsense.”

## Architectural implication
This changes the fit judgment in [[another-harness-and-atropos]] only slightly but importantly. The answer is still “later, not now” for Atropos proper, yet the repo is no longer purely pre-environment. It now has the beginning of a benchmark layer of its own.

In other words:
- before: design-only substrate
- now: local executable prototype
- later, if earned: broader environment families and possibly Atropos-style rollout/training integration

## Bottom line
`another-harness` now has a real builder-side environment prototype, not merely a plan to have one. That makes the repo’s RL-environment story more credible, while also vindicating the earlier insistence that the first environment family should be narrow, artifact-first, and suspicious of benchmark gaming.

## Related pages
Read this with [[another-harness-evaluator-discipline-environment]], [[another-harness-atropos-environment-schema]], [[another-harness-and-atropos]], [[rl-gyms-and-executable-environments-for-ai-harnesses]], [[evaluation-and-review-loops]], and [[atropos]].
