---
title: another-harness Resume-Recover Environment Prototype
author: local repository synthesis
url: file:///Users/ericfode/src/another-harness/docs/specs/resume-recover-environment.md
ingested: 2026-04-11
---

# another-harness Resume-Recover Environment Prototype

`another-harness` now contains its first executable `resume_recover` benchmark family.

## Main architectural facts

- The new family is still synthetic, not yet a live recovery path.
- It is built explicitly around the Lean restart architecture:
  - `WorkId.restart`
  - `ObservationScope`
  - stream continuity vs attempt-local grounded completion
- The current two benchmark cases intentionally separate two truths:
  - a same-stream fresh-attempt recovery can succeed while remaining `in_progress`
  - an interrupted implementation can also be honestly finished to `reviewed`
- The recovering agent may update scoped implementation files, the work item, and the handoff, but it may not approve completion or mutate the evaluator artifact.
- Review tightened the family so missing handoffs score a failure instead of crashing, and empty required-substring contracts are rejected as vacuous.

## Practical conclusion

The repo's recovery story is no longer merely promised by the Atropos schema. It now exists as executable harness machinery, even if the live `prepare-live` and checkpoint/MCP integration cuts still remain to be earned.

