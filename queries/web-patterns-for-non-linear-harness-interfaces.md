---
title: Web Patterns for Non-Linear Harness Interfaces
created: 2026-04-09
updated: 2026-04-10
type: query
tags: [comparison, orchestration, context-engineering, work-management]
sources: [raw/articles/sketch-n-sketch.md, raw/articles/glamorous-toolkit-moldable-development-environment.md, raw/papers/arxiv-omar-2018-live-functional-programming-with-typed-holes.md, raw/papers/arxiv-doderlein-2026-spacetime-programming.md, raw/articles/pernosco-omniscient-printf-debugging.md, raw/articles/plutojl-interactive-programming-environment.md, raw/articles/vistrails-aosa.md, raw/articles/spatial-hypertext.md, raw/articles/langgraph-studio-first-agent-ide.md, raw/articles/temporal-web-ui.md, raw/articles/windmill-suspend-approval-prompts.md, raw/articles/trigger-dev-product.md, raw/articles/airflow-ui-overview.md, raw/articles/dagster-scaling-dag-visualization.md, queries/non-linear-interface-options-for-next-harness.md]
---

# Web Patterns for Non-Linear Harness Interfaces

## Question
After the first arXiv-heavy pass, what additional interface patterns emerge from the broader web of live-programming systems, workflow control planes, moldable tools, and alternative knowledge-work environments?

## Short answer
The next harness should look less like "chat with some tools" and more like a moldable operations studio: one durable state model, many task-specific projections, first-class provenance, and explicit human control nodes. The follow-on distributed-systems pass sharpens the semantic layer beneath this in [[legacy-distributed-systems-ideas-for-moldable-operations-studio]] and [[moldable-operations-studio-architecture-spec]], while the speculative-design pass checks the control metaphors against [[sci-fi-audit-for-moldable-operations-studio]].

## Additional patterns worth stealing

### 1. Moldable interfaces instead of one canonical IDE
[[glamorous-toolkit-moldable-development-environment]] argues that the environment should make custom tools cheap to build. [[langgraph-studio-first-agent-ide]] reaches the same destination from the agent side: graph visualization, interaction, and debugging are first-class. Together they suggest that the right surface is often generated or specialized for the current problem, not chosen from a fixed tab bar.

### 2. Direct manipulation should sometimes outrank text editing
[[sketch-n-sketch]] is valuable because it treats direct manipulation and programming as peers. The harness analogue is obvious: sometimes the user should drag a failing dependency edge, adjust a rendered UI state, or reshape a work graph directly and let the system synthesize the corresponding structured change.

### 3. Incomplete work should remain live
[[arxiv-omar-2018-live-functional-programming-with-typed-holes]] is a sharp corrective to the common habit of turning partially built states into dead zones. A harness should continue to expose useful structure even when code, plans, or proofs are unfinished. Draft branches and provisional evidence should still be explorable.

### 4. Provenance should be queryable, not archival
[[vistrails-aosa]], [[arxiv-doderlein-2026-spacetime-programming]], and [[pernosco-omniscient-printf-debugging]] all point in the same direction: execution and derivation history should be searchable as data. This goes beyond "show me the transcript." The stronger model is: show me the lineage of this result, the alternative branches that almost happened, and the first point at which the invariant failed.

### 5. Dependency-driven interactivity beats hidden-state notebooks
[[plutojl-interactive-programming-environment]] makes the appealing spreadsheet move: recompute by dependency, not by opaque historical accident. That is highly relevant to harness workbooks, review panes, and debugging boards, which otherwise tend to accumulate hidden state and ceremonial reruns.

### 6. Loose spatial arrangement before formal structure
[[spatial-hypertext]] is a lovely reminder that early understanding is often ambiguous. A harness should sometimes let the user loosely arrange traces, notes, files, incidents, and prompts before demanding explicit graph edges or rigid schemas. Once the pattern stabilizes, the system can promote it into typed work objects.

### 7. Durable mission control for autonomous work
[[temporal-web-ui]], [[trigger-dev-product]], and [[windmill-suspend-approval-prompts]] together suggest that long-running agent work deserves a proper control plane: live state, event history, approvals, suspensions, and resumptions as durable primitives. [[airflow-ui-overview]] adds the useful lesson that graph view is not enough; grid and run-centric views often reveal fleet-level problems faster.

### 8. Scalability is part of interface design, not a late optimization
[[dagster-scaling-dag-visualization]] matters because it names the inevitable problem directly. If a harness succeeds, it will eventually visualize thousands of files, tasks, branches, traces, and agents. Filtering, collapsing, virtualization, and selective fetch are therefore core UI architecture, not polish.

## What this changes in the harness design
The first non-linear surface pass already argued for branchable graphs, checkpoints, runtime overlays, spatial maps, and generated control panels. The broader web pass sharpens that into a more opinionated set of interface primitives:

1. **View definitions as first-class objects**
   - If surfaces are moldable, the harness needs durable definitions for panes, inspectors, dashboards, and graph projections.
2. **Trace database, not transcript pile**
   - Provenance and omniscient inspection require a searchable execution/event store.
3. **Human approval as typed work node**
   - Approval, suspend, claim, and resume steps should be explicit graph objects.
4. **Dependency-aware live surfaces**
   - Review boards and notebooks should update by declared dependency rather than remembered order.
5. **Loose-to-formal promotion**
   - Some workflows should begin with ambiguous spatial grouping and only later harden into typed relations.
6. **Multiple supervisory projections**
   - The same run set may need graph, grid, queue, and evidence views depending on the question.

## Revised implementation order
1. Add a durable trace/provenance layer beneath the existing work graph.
2. Build mission-control views over runs: queue, grid, event history, approval inbox.
3. Add moldable inspectors and task-specific panes over the shared state model.
4. Add direct-manipulation affordances for selected artifacts and graphs.
5. Add loose spatial canvases for exploratory arrangement before formalization.

## Main caution
A harness should not become a carnival of disconnected surfaces. All of these patterns only help if they are projections over one coherent underlying model of work, execution, provenance, and approval. Otherwise one merely invents a more colorful way to become desynchronized.

## Related pages
Read this with [[non-linear-interface-options-for-next-harness]], [[legacy-distributed-systems-ideas-for-moldable-operations-studio]], [[moldable-operations-studio-architecture-spec]], [[moldable-operations-studio-schema-pass]], [[sci-fi-audit-for-moldable-operations-studio]], [[new-harness-design-notes]], [[work-management-primitives]], [[partial-order-trace-semantics]], [[evaluation-and-review-loops]], and [[harness-engineering]].
