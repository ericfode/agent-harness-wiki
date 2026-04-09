---
title: Non-Linear Interface Options for the Next Harness
created: 2026-04-08
updated: 2026-04-09
type: query
tags: [comparison, orchestration, context-engineering, work-management]
sources: [raw/articles/openai-unlocking-codex-harness.md, raw/articles/openai-introducing-codex-app.md, raw/papers/arxiv-sarkar-2023-code-relevant-ui.md, raw/papers/arxiv-angert-2023-spellburst.md, raw/papers/arxiv-rein-2024-live-programmers.md, raw/papers/arxiv-krause-glau-2023-code-proximal-dynamic-software-visualization.md, raw/papers/arxiv-kuhn-2010-spatial-software-visualization-ide.md, raw/papers/arxiv-li-2024-kishu-time-traveling-notebooks.md, raw/papers/arxiv-fang-2025-code-data-space-versioning.md, raw/papers/arxiv-chen-2022-nl2interface.md, raw/papers/arxiv-krause-glau-2024-code-review-software-city.md]
---

# Non-Linear Interface Options for the Next Harness

## Question
What non-linear operator surfaces look promising for the next evolution of a programming harness, given the current Codex-style protocol split, the Gas City instinct toward durable work graphs, and the broader arXiv literature on programming interfaces?

## Short answer
The strongest direction is not “replace the CLI with a fancy canvas,” but to keep a textual kernel such as [[codex-app-server]] or equivalent durable thread/work primitives, then project that same state into branchable, spatial, and replayable views.

The papers point toward five especially credible interface families:
1. a branchable work-graph canvas
2. a time-travel and checkpoint surface
3. code-proximal runtime overlays
4. spatial system and review maps
5. query-driven generated control panels

For a broader web-systems follow-on that adds moldable tools, provenance/query interfaces, and durable mission-control surfaces, see [[web-patterns-for-non-linear-harness-interfaces]].

## Why this matters now
The current harness corpus already suggests that transcripts are the wrong place to store all meaning. [[gas-town]] and [[gas-city]] move work into durable graph objects; [[codex-cli]] and [[codex-app-server]] move execution into typed protocol items; [[hermes-agent]] moves durable learning into memory and skills. The surface layer is therefore the obvious next place to stop pretending that one scrolling transcript should bear the entire cognitive load.

## What the papers suggest

### 1. Branchable work-graph canvas
**Spellburst** is the clearest direct interface precedent. Its node-based surface lets users branch and merge exploratory work while moving fluidly between semantic prompts and editable code. For harness design, the key lesson is that branching should be a first-class interaction, not an accidental by-product of duplicated chats or ad-hoc worktrees.

The harness analogue would be a surface where work items, reviewer branches, alternate plans, and subagent runs appear as explicit nodes and edges. That fits naturally with [[work-management-primitives]] and with the current instinct that serious work wants a graph, not a monologue.

### 2. Time-travel and checkpoint surface
**Kishu** and **Code+Data Space Versioning** argue that exploratory work is inherently non-linear. Users want rollback, checkout, branching, and re-entry into prior states without paying the cost of full restart or losing provenance. Notebook authors may be doing data work, but the structural lesson is broader than that.

For a harness, this suggests a “session history board” with checkpoints, branch labels, and reversible state transitions over both code state and agent work state. The caution is equally valuable: notebooks become treacherous when the visible document diverges from the real runtime state. A harness time-travel surface therefore needs explicit checkpoints and replay semantics, not decorative history.

### 3. Code-proximal runtime overlays
**Broadening the View of Live Programmers** and **Collaborative, Code-Proximal Dynamic Software Visualization within Code Editors** converge on the same interface principle: local detail and cross-cutting runtime structure should be visible together. One shows a call-tree browser integrated into a live environment; the other embeds distributed runtime visualization directly beside code and synchronizes it for collaborators.

The harness version would not merely show text output from tools. It would let the operator click from a work item or test failure into the relevant files, traces, spans, logs, and call structure. In other words, validation evidence becomes navigable rather than merely narrated. This is adjacent to [[evaluation-and-review-loops]] and [[automation-and-background-work]].

### 4. Spatial system and review maps
**Embedding Spatial Software Visualization in the IDE** shows that developers do build spatial memory around software maps, though layout must be carefully chosen or the map becomes confusing. **Software City Visualization for Code Reviews** extends the spatial idea into review, where structural and dynamic information can be explored together rather than left as separate rituals.

For harnesses, this suggests a review/architecture surface that is neither a generic whiteboard nor a pile of diffs. A spatial map could show ownership, hot paths, changed zones, failing components, and reviewer attention. The useful version is not ornamental 3D whimsy; it is a navigable compression layer over repo and runtime structure.

### 5. Query-driven generated control panels
**NL2INTERFACE** offers a different but important idea: do not force users to learn one fixed meta-interface when the system can materialize the right multi-view interface for the task. Combined with Sarkar's broader claim that code itself may stop being the dominant user interface, this suggests a harness that can generate temporary, task-specific control surfaces from operator intent.

The harness analogue would be something like: “show me all parallel refactors touching auth, grouped by risk, with reviewer disagreement highlighted,” and the system materializes a filtered graph, queue, and evidence panes for exactly that question.

## Recommended build order
1. **First:** branchable work graph plus explicit checkpoints.
   - This has the best fit with [[new-harness-design-notes]], [[work-management-primitives]], and [[partial-order-trace-semantics]].
   - It also gives the cleanest answer to "where does alternate work live?"
2. **Second:** code-proximal evidence overlays.
   - This turns evaluator output into something inspectable instead of ceremonial.
3. **Third:** spatial review map.
   - Best for architecture changes, multi-agent review, and large-repo supervision.
4. **Fourth:** query-generated custom interfaces.
   - Probably the highest ceiling, but it should be built atop a stable typed state model rather than guessed from transcript text.

## Design invariant
Non-linear surfaces should be projections over one durable state model, not separate truth stores. The CLI, IDE, web view, and generated canvases should all be clients of the same core thread/work/checkpoint/trace primitives. Otherwise the system will merely invent a new species of desynchronization, which would be a rather baroque way to rediscover ordinary confusion.

## Open design problems
- What is the smallest typed state model that can support chat, graph, replay, and spatial views without drift?
- Which events should become first-class nodes: work items, branches, tool calls, checkpoints, traces, reviewer objections?
- How much of the non-linear surface should be user-authored versus generated from intent?
- How should time-travel interact with permissions, automations, and background agents that may have side effects outside the repo?

## Related pages
Read this with [[web-patterns-for-non-linear-harness-interfaces]], [[new-harness-design-notes]], [[agent-harness-anatomy]], [[harness-engineering]], [[work-management-primitives]], [[partial-order-trace-semantics]], [[evaluation-and-review-loops]], and [[gas-city-but-its-just-codex]].
