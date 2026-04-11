---
title: "another-harness evaluator-discipline environment"
created: 2026-04-10
updated: 2026-04-10
type: query
tags: [benchmark, tool-execution, work-management]
sources: [raw/articles/another-harness-evaluator-discipline-environment-2026-04-10.md, raw/articles/another-harness-work-item-closure-environment-2026-04-10.md, raw/articles/another-harness-atropos-environment-schema-2026-04-10.md]
---

# another-harness evaluator-discipline environment

## Question
What changed once `another-harness` stopped at a builder-side environment prototype and added the evaluator lane as a real executable family rather than a promise in a schema?

## Short answer
The repo gained a second kind of seriousness.

The first prototype, [[another-harness-work-item-closure-environment]], proved that `another-harness` could compile and grade bounded builder episodes. This new evaluator slice proves that the repo can also grade reviewer honesty over ambiguous completion states without collapsing the builder/checker separation back into one self-congratulatory actor.

## Why this matters
The evaluator lane is where a lot of agent systems quietly become unserious. It is easy to say “have a separate reviewer.” It is harder to build a benchmark that punishes false approval, respects repo-native completion rules, and refuses to let the reviewer rewrite the task it is supposedly judging.

That is precisely why this slice matters. It now gives the repo:
- evaluator episodes compiled from repo-native artifacts
- a benchmark family where `approved_for_completion` is evaluator-owned rather than builder-owned
- explicit truth tests for incomplete, complete, and ambiguous builder states
- a harder boundary between repo reality and whatever the evaluator wishes were true

## Most important design move
The most important move is not merely that the runner exists. It is that the runner derives evaluator truth from the frozen builder contract plus live check results, while treating builder-owned work items, handoffs, and deliverables as out of scope.

That preserves the repo’s constitutional order. The evaluator may bless completion, but it may not quietly edit the republic to make the blessing convenient.

## What the prototype actually proves
The repo now demonstrates all of the following in executable form:
1. **Evaluator-only edit scope** over the canonical evaluation artifact
2. **Truthful approval logic** tied to repo state instead of vibes
3. **Ambiguity handling** when checks pass but completion readiness still fails
4. **Deterministic regression** where oracle evaluator artifacts beat noop
5. **Review-driven hardening** against benchmark gaming in the evaluator lane

The fifth item is not decorative. The slice had to be hardened repeatedly against hidden-file smuggling, replace-ref tricks, control-bundle retargeting, and a variety of attempts to smuggle mutable control state back in through side doors. This is all rather encouraging in the same way a properly paranoid lock is encouraging.

## What it still does not prove
The evaluator prototype does not yet show:
- resume/recover episodes
- persistent `state/runs/` history as canonical repo state
- trainer hookup or scalable rollout orchestration
- stronger operator-side isolation against a fully compromised workstation
- real model trajectory capture beyond the current coarse run artifacts

So the right reading is still measured. The repo now has builder and evaluator lanes, but not yet a mature multi-family RL substrate.

## Architectural implication
This materially strengthens the local argument in [[another-harness-and-atropos]]. The answer remains “later” for Atropos proper, but the repo now has enough executable substrate of its own that an eventual Atropos-style rollout layer would have something real to wrap.

Put differently:
- before: schema-only environment ambition
- after work-item closure: executable builder lane
- after evaluator discipline: executable builder and evaluator lanes
- later, if earned: resume/recover and more serious rollout history

## Bottom line
`another-harness` now has a real evaluator-side environment prototype. That does not make it a finished training substrate, but it does make the repo’s claims about evaluator discipline much less rhetorical and much more mechanical.

## Related pages
Read this with [[another-harness-work-item-closure-environment]], [[another-harness-atropos-environment-schema]], [[another-harness-and-atropos]], [[evaluation-and-review-loops]], and [[rl-gyms-and-executable-environments-for-ai-harnesses]].
