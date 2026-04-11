---
title: another-harness Work-Item Closure Environment Prototype
author: local repository synthesis
url: file:///Users/ericfode/src/another-harness/docs/specs/work-item-closure-environment.md
ingested: 2026-04-10
---

# another-harness Work-Item Closure Environment Prototype

The `another-harness` repo now contains the first live executable slice underneath its earlier Atropos sidecar design: a thin local `work_item_closure` benchmark family with synthetic repo-native fixtures, isolated git worktrees, and deterministic noop-versus-oracle self-tests.

## Main architectural facts

- The implementation is deliberately **not** full Atropos integration; it is a local runner that proves the benchmark mechanics first.
- Each prepared run now splits operator-side control artifacts from the sandbox tree, so the grading surface is not a sibling file living inside the agent’s own worktree.
- The immutable grading contract is frozen into the baseline commit as `.work-item-closure-contract.json`.
- Grading uses the frozen contract for acceptance checks, deliverable paths, and artifact bindings instead of trusting a sandbox-mutated work-item file.
- Diffs are computed against the baseline commit rather than only the current `HEAD`, so committed tampering is still visible.
- Replace refs are disabled while reading the frozen contract and computing diffs, which blocks a particularly silly form of git-history laundering.
- File-scoped allowlist entries match exactly; only paths explicitly recorded as directories recurse to descendants.
- The repo now has synchronized work-item, evaluation, handoff, and council-acceptance artifacts for this slice, plus deterministic tests covering out-of-scope edits, evaluator-artifact tampering, contract rewriting, external metadata tampering, replace-ref forgery, file-prefix abuse, and baseline-metadata mismatch.

## Practical conclusion

This is the point where `another-harness` stops talking about an RL-environment substrate purely as future constitutional theory and starts owning a small executable benchmark harness. The result is still partial: it only covers the builder-side `work_item_closure` family, with no trainer hookup and no evaluator-discipline or resume/recover families yet.
