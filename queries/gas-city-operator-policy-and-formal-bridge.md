---
title: Gas City Operator Policy and Formal Bridge
created: 2026-04-15
updated: 2026-04-15
type: query
tags: [gas-city, formal-methods, semantics, work-management]
sources: [raw/articles/gas-city-but-its-just-codex-doc-architecture-and-ops-2026-04-15.md, raw/articles/gas-city-but-its-just-codex-repo-2026-04-15.md]
---

# Gas City Operator Policy and Formal Bridge

## Question
What is actually interesting now about the repo's operator-policy and Lean bridge work, beyond the vague claim that it has "formal methods"?

## Short answer
The repo has crossed from prose about policy into a typed, file-backed policy surface that now affects runtime behavior, and it is currently extending that story upward into an explicit recipe/workflow/policy bridge in Lean.

That is the important shift.

## What the policy layer now is
Operator policy is no longer just a Rust constructor full of opinions. The repo now treats it as:
- typed observational logic over workflow state
- file-backed JSON policy bindings under `configs/operator-policy/`
- a runtime-evaluated admissibility surface carried in workflow snapshots
- something the operator daemon actually obeys when deciding whether `claim` is admissible

This matters because it keeps policy on the observational side of the authority boundary. Policy reads workflow state and denotes admissible action families; it does not itself become the authoritative mutation kernel. That is exactly the boundary formalized in the workflow/operator semantics note and fits the broader caution of [[formal-methods-for-agent-harnesses]].

## Why this is more than decorative formalization
The repo's recent increments make two distinct moves.

### 1. Runtime policy alignment
The earlier policy-routing increment made the runtime carry typed routing details and policy evaluation in a way the daemon and client can actually consume. In plainer language: policy ceased to be a UI ornament and became a runtime gate.

### 2. Recipe/workflow/policy bridge
The newer bridge work does not collapse recipes, workflow state, and policy into one grand algebra. Instead it keeps them split:
- recipes remain generative
- workflow remains authoritative
- policy remains observational
- the bridge is explicit and narrow

That restraint is the tasteful part. A sloppier system would call everything "the program" and quietly blur compile-time generation with run-time admissibility. This repo is trying not to commit that category mistake.

## Why the bridge is interesting
The bridge buys three things that matter operationally, not only formally:
- one more explicit story for how recipe structure projects into workflow-facing policy facts
- a more honest way to talk about composed workflow programs without fusing all layers together
- a foundation for the next read-model work around phase, barrier, and workspace coverage

This is also why the repo should be read alongside [[gas-city-but-its-just-codex]] and [[prompt-program-architecture-plans-for-another-harness-and-gas-city]]. The question is no longer merely "what workflow should run?" It is increasingly "what kind of explicit program artifact is this repo actually operating?"

## What the current checkpoint says
At inspection time, the repo's own operational state said:
- current checkpoint: `recipe-policy-bridge-088`
- next target: `phase-summary-workspace-coverage-089`

That is revealing. It means the formal bridge is not being treated as a ceremonial side quest. It is immediately feeding the next generic program read-model backlog.

## The real design choice
The most important real choice here is restraint.

The repo is explicitly refusing to:
- turn operator policy into the authoritative transition kernel
- collapse recipe semantics into policy denotation
- pretend compile-time formula evolution and run-time policy live on the same cadence

Instead it is choosing composition over fusion. That is a much saner way to grow a serious control plane.

## Open edge
The obvious open edge is not whether the repo has any formal content. It plainly does. The open edge is whether the resulting runtime surfaces and read models become more legible to operators, or whether the repo accumulates a beautifully arranged semantic attic that the UI and daemons only partly inhabit.

The next target being phase and workspace coverage suggests the repo itself knows this.

## Bottom line
The interesting thing about this repo's formal layer is not that Lean exists. It is that typed operator policy already reaches runtime behavior, while the newer recipe/workflow/policy bridge tries to extend that semantic discipline without collapsing the repo's core authority boundary. That is a much more serious move than merely proving a tasteful theorem off to the side.

## Related pages
Read this with [[gas-city-but-its-just-codex]], [[formal-methods-for-agent-harnesses]], [[theorem-proving-as-cognitive-kernel]], [[prompt-program-architecture-plans-for-another-harness-and-gas-city]], and [[self-evolving-workflows]].