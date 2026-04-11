---
title: another-harness Atropos Environment Schema
author: local repository synthesis
url: file:///Users/ericfode/src/another-harness/docs/specs/atropos-environment-schema.md
ingested: 2026-04-10
---

# another-harness Atropos Environment Schema

The `another-harness` repo now contains a concrete design note for how an Atropos-style RL environment could be adopted later without replacing repo-native work items, evaluation artifacts, handoffs, or the Lean scaffold.

## Main architectural facts

- The design explicitly treats Atropos as a **repo-artifact-first sidecar** rather than a new source of truth.
- Compiled episodes must be mechanical derivations of canonical repo artifacts, preserving canonical field names where possible.
- The first environment families are deliberately narrow: work-item closure, evaluator discipline, resume/recover, and later narrow Lean maintenance.
- Role-specific permissions are part of the schema, so builder-like episodes cannot silently grade themselves.
- Reward is tied to reality-bearing checks, with explicit penalties for false completion claims, out-of-scope edits, and missing handoff/evaluation artifacts.
- The design leaves the attempt-log layer open between a future `state/runs/` directory and projections from `plugins/codex-control-plane/`, but insists that either option must remain subordinate to the canonical repo artifact model.

## Practical conclusion

The design does not recommend immediate Atropos adoption. It says Atropos becomes appropriate only after `another-harness` has a stable repeated benchmark suite, deterministic enough checks, isolated worktree execution, and a genuine need for repeated rollout data. Until then, the repo should keep strengthening its current work/evaluation/handoff discipline.
