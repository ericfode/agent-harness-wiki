---
title: another-harness Model/Docs Drift Checker
author: local repository synthesis
url: file:///Users/ericfode/src/another-harness/docs/specs/model-docs-drift-checks.md
ingested: 2026-04-11
---

# another-harness Model/Docs Drift Checker

`another-harness` now contains its first narrow Lean-backed docs/model drift fence.

## Main architectural facts

- The checker does **not** attempt whole-repo docs-vs-Lean equivalence.
- It governs one high-value contract: the distinction between attempt-local grounded completion and stream-level historical continuity across retries.
- The model side is anchored in:
  - `Work.lean`
  - `Operational.lean`
  - `Refinement.lean`
  - `Theory.lean`
- The explanatory side is currently anchored in:
  - `docs/harness-formalization-bootstrap.md`
  - `docs/specs/architecture-spec.md`
  - `docs/recent-work-grounded-tour.md`
- The checker validates exact symbols such as `ObservationScope`, `ObservationTarget`, `WorkId.restart`, `Trace.hasHistoricalSupportAt`, and `Trace.hasGroundedAttemptAt`, plus restart-aware theorem witnesses showing that a stream may retain support while a restarted attempt remains ungrounded.
- It also strips Lean comments and string literals before matching, so dead quoted text cannot masquerade as live formal support.

## Practical conclusion

The repo now has a way to stop one of its favorite explanatory moves from drifting into decorative prose. That is modest, but legitimate. If a second Lean-backed contract becomes central later, the same pattern can be extended without pretending to solve documentation in general.
