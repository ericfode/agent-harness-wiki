---
title: another-harness Run-History Decision
author: local repository synthesis
url: file:///Users/ericfode/src/another-harness/docs/specs/run-evidence-storage.md
ingested: 2026-04-11
---

# another-harness Run-History Decision

`another-harness` has now resolved the first honest storage fork created by its live builder/evaluator loops.

## Main architectural facts

- The repo explicitly decided **not** to make `state/runs/` canonical yet.
- Canonical operational truth remains in:
  - `state/work-items/*.json`
  - `state/evaluations/*.json`
  - `state/handoffs/*.md`
- Historically important attempts may be preserved as **derived evidence bundles** under `docs/plans/artifacts/<work-id>/<attempt-id>/...`.
- The preserved 0028/0030 live evidence is already mechanically replayable through `tools/check_real_loop_smoke.py`, so there is no need to invent a second truth plane merely to rescue those attempts from transcript oblivion.
- The new `tools/check_run_evidence.py` checker validates the storage decision itself, the preserved bundle structure, the actual replay inputs (`builder.patch` and evaluator-artifact snapshots), and the fact that replay still works without preserved `run.json` / `episode.json` metadata.

## Practical conclusion

The repo now has a thinner answer to run history:
- keep canonical truth in the work/evaluation/handoff loop
- promote only historically important attempts as evidence bundles
- reopen `state/runs/` only if future many-attempt pressure or resume/recover work genuinely earns it

This is a design gain precisely because it refuses bureaucracy before necessity. A rare civic virtue.
