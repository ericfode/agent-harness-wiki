---
title: "another-harness resume-recover environment"
created: 2026-04-11
updated: 2026-04-11
type: query
tags: [benchmark, tool-execution, work-management]
sources: [raw/articles/another-harness-resume-recover-environment-2026-04-11.md, raw/articles/another-harness-atropos-environment-schema-2026-04-10.md]
---

# another-harness resume-recover environment

## Question
What does it mean for `another-harness` to make recovery a real executable harness family instead of merely a tasteful promise in the Atropos schema?

## Short answer
It means the repo can now benchmark interrupted work honestly.

The important move is not just “there is a third runner now.” It is that the runner preserves the asymmetry already formalized in Lean:
- a stream can carry continuity across retries
- a restarted attempt still has to earn its own status honestly
- a strong handoff is evidence of continuity, not a completion indulgence coupon

## What the prototype currently proves
The repo now has two deterministic recovery patterns:
1. **Honest re-orientation**
   - the task is resumed on the same stream
   - a recovery note and handoff update are produced
   - the work item still remains `in_progress`
2. **Recovered implementation finish**
   - interrupted implementation work is actually finished
   - the checker passes
   - the work item can move to `reviewed`

That is exactly the right first split. If the family had started by forcing every recovery episode to end in triumphant completion, it would have violated the model before it even shipped.

## Why this matters
This slice is the first place where the Lean restart architecture visibly governs runtime behavior rather than merely explaining it afterwards.

`another-harness` had already implemented:
- builder-side bounded work-item closure
- evaluator-side honest review

Recovery was the missing third family because it is where stale claims, partial work, stream continuity, and fresh attempts all collide. That is where a harness either becomes honest or becomes theatrical.

## Limits
The family is still intentionally modest:
- synthetic only
- no live `prepare-live` recovery path yet
- no MCP wrapper yet
- no checkpoint/control-plane projection yet

So this is not yet the repo's full recovery runtime. It is the first executable rung, which is enough to make the next rung meaningful.

## Bottom line
`another-harness` now has a real recovery family, and it is correctly shaped. It does not confuse historical support with grounded completion, and it does not let recovery quietly become a flattering synonym for "done."

## Related pages
Read this with [[another-harness-and-atropos]], [[another-harness-work-item-closure-environment]], [[another-harness-evaluator-discipline-environment]], [[formal-cognition-loop]], and [[evaluation-and-review-loops]].

