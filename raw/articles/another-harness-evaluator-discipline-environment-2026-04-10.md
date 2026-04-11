---
title: another-harness Evaluator-Discipline Environment Prototype
author: local repository synthesis
url: file:///Users/ericfode/src/another-harness/docs/specs/evaluator-discipline-environment.md
ingested: 2026-04-10
---

# another-harness Evaluator-Discipline Environment Prototype

The `another-harness` repo now contains the second live executable slice underneath its Atropos sidecar design: a thin local `evaluator_discipline` benchmark family that grades reviewer honesty over bounded repo-native builder states.

## Main architectural facts

- The implementation is deliberately **not** full Atropos integration; it is a local runner that proves evaluator-lane mechanics first.
- The suite contains three evaluator fixtures: reject an obviously incomplete builder state, approve a clean reviewed state, and reject an ambiguous in-progress state despite passing checks.
- Each prepared run freezes the benchmark contract into the baseline commit as `.evaluator-discipline-contract.json`.
- Evaluator episodes may write only the evaluation artifact; builder-owned work items, handoffs, and deliverables remain frozen.
- The grader now derives truth from the frozen builder contract plus real check results, rather than from mutable sandbox paperwork.
- Review forced a long series of anti-gaming fixes: ignored-file smuggling detection, replace-ref resistance, file-vs-directory scope discipline, run-metadata hardening, control-bundle retarget detection, and finally a control-dir baseline anchor plus sandbox-root anchor.
- The final spec now states the honest assumption surface explicitly: the evaluated agent is judged inside `sandbox_root`, while direct mutation of operator-side control artifacts remains out of scope for this local prototype unless stronger OS-level isolation is added later.

## Practical conclusion

`another-harness` now has builder and evaluator benchmark lanes of its own. That still does not make it an Atropos deployment or a trainer stack, but it does mean the repo’s RL-environment story is no longer just one schema and a wistful look into the distance.
