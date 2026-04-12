---
title: Workflow Visualization Beyond DAGs for Expanding Frontiers
author: local synthesis with external papers and docs
date: 2026-04-11
accessed: 2026-04-11
ingested: 2026-04-11
---

# Workflow Visualization Beyond DAGs for Expanding Frontiers

**Context:** research note for the `gas-city-but-its-just-codex` operator UI.

The current native `Relation` view is a fast local ego map: one center node,
incoming edges on the left, outgoing edges on the right, same-worker nodes on
the lower left, and ready frontier nodes on the lower right. That is a good
first operator surface, but it breaks down in four cases:

- cycles read like contradictory left-right spokes instead of first-class loops
- dense local pockets turn into edge clutter
- an expanding frontier becomes an unbounded strip instead of an interpretable boundary
- live updates can reshuffle nodes enough to damage the operator's mental map

The research result is straightforward: do not keep stretching one node-link
projection until it lies. Use a small family of coordinated projections instead.

## Main conclusion

For workflows that are not reliably DAG-shaped, or whose ready frontier expands
and contracts aggressively, the UI should split its answers across five
projections:

- `Structure`: SCC-condensed dependency view with stable layout
- `Focus`: local path or blocker lens around the selected node
- `Frontier`: explicit ready-boundary view, grouped and ranked rather than sprayed into the main graph
- `Dense Pocket`: matrix or hybrid rendering for dense local components
- `Evolution`: static summary of frontier width, blocked count, and worker occupancy over time

The important design move is not "find the one better graph layout." The move
is to stop asking one layout to answer every operator question.

## Research findings

### 1. Preserve the mental map under live updates

Frishman and Tal's work on online dynamic graph drawing argues that dynamic
layout must preserve the user's mental map, especially in unchanged regions,
and should spend most layout effort near the modified part of the graph. This
fits the operator UI exactly: a pushed bundle refresh should not cause a broad
re-layout of the visible subgraph.

For this UI, that implies:

- persist stable positions per saved projection
- pin unchanged nodes or components across refreshes
- re-layout only the affected neighborhood after `expand`, `recover`, `handoff`, or claim changes
- animate local changes, not whole-screen rearrangements

ELK's `interactive Layout` option and layered layout support make this idea
practical rather than theoretical: the layout engine can be told that the graph
is changing interactively and can respect position and layer hints instead of
starting from zero every time.

### 2. Separate cycles from the acyclic backbone

If the workflow contains cycles, the UI should not pretend otherwise. The right
top-level move is to compute strongly connected components and visualize the
condensation graph. Once each SCC is contracted into a single node, the
resulting graph is a DAG. That gives the operator a truthful backbone without
erasing the existence of loops.

For this UI, that implies:

- top-level structure view should operate on SCC capsules, not raw nodes
- each capsule should show member count, status rollup, loop badge, and frontier count
- inter-capsule edges should use a layered layout
- entering a capsule should switch to an internal local view rather than flattening the whole cycle into the outer graph

ELK layered explicitly supports cycle breaking and even exposes SCC-oriented
cycle-breaking strategies. That is a strong fit for a graph that is mostly
directional but not guaranteed acyclic.

### 3. Use focus-plus-context lenses instead of global shrink

Classic fisheye thinking and later structure-aware fisheye work make the same
point: when the graph is large, operators still need both local detail and
global context. Wang et al. argue that structure-aware fisheye lenses can
reduce path and temporal distortion and improve readability, with path, cluster,
and polyfocal variants for different tasks.

For this UI, that implies:

- `path lens`: emphasize upstream blockers and downstream consequences of the selected node
- `cluster lens`: magnify the selected SCC or worker cluster without removing the outer structure
- `polyfocal lens`: keep the selected node, current blocker set, and ready frontier visible at the same time

This is better than zooming the whole graph or continuously shrinking node
labels as the workflow grows.

### 4. Treat frontier growth as a boundary, not as more interior graph

GraphFlow is useful here because it argues that high-level dynamic patterns are
hard to read from animation alone, and that static summaries of metric change
over time can expose patterns that animated node-link views hide. An expanding
ready frontier is one of those patterns.

For this UI, that implies:

- frontier width should be visible as a first-class metric over time
- ready work should be grouped by component, blocker-release source, worker affinity, or overlay relation
- the frontier should be rendered as a ranked band, ring, or lane, not simply appended to the bottom of the relation map
- the trace view should expose churn: frontier growth, claim rate, blocked rate, and open child-scope count

The operator question here is not only "what nodes are ready?" It is also "is
the workflow converging, stalling, or exploding?"

### 5. Use hybrid views for dense local pockets

NodeTrix argues that node-link diagrams work well for global structure, while
adjacency matrices are better for dense local communities. This maps directly to
workflow hotspots such as tight debate loops, same-worker tangles, or dense
cross-coalition interactions.

For this UI, that implies:

- use node-link for inter-component structure
- switch a dense SCC, coalition, or same-worker pocket to a matrix or NodeTrix-style card
- keep click-through from matrix cell to node inspector, worker inspector, and event trail

This gives the operator a way to read density without pretending every edge
deserves its own visible stroke at all times.

### 6. Keep relation families layered instead of blending them into one hairball

The repo already separates authoritative workflow state from overlay relations
such as worker binding, negotiated allocation, coalitions, and observer state.
The UI should keep doing that visually.

For this UI, that implies:

- dependency and containment edges stay primary in the structure view
- worker, allocation, coalition, and observer relations should be optional overlays or sidecars
- overlay relations should never silently rewrite authoritative dependency geometry

This avoids a common failure mode where a graph becomes unreadable because four
different semantics are encoded with only color and line style.

## Recommended projection model

### 1. Structure projection

- unit: SCC capsule or single node
- layout: layered at the backbone, stable across updates
- question: what depends on what, and where are the loops?

### 2. Focus projection

- unit: selected node plus a bounded causal neighborhood
- layout: local lens with anchored positions
- question: why is this node waiting, and what can it unblock?

### 3. Frontier projection

- unit: ready boundary rather than whole graph
- layout: ranked columns, band, or radial ring
- question: where can work expand next, and what shape is the expansion taking?

### 4. Dense pocket projection

- unit: matrix or hybrid card for a dense component
- question: is this a tangle, or a coherent local cluster?

### 5. Evolution projection

- unit: event or time slices plus metric summaries
- layout: static flow summary with selected structural snapshots
- question: is the workflow converging, thrashing, or simply growing?

## First executable spike for this UI

The first useful spike is not a brand-new graph engine. It is a data-model and
projection change.

1. Extend the workflow snapshot or saved-projection payload with:
   - SCC membership
   - condensation edges
   - frontier grouping metadata
   - stable position hints per projection
2. Replace the single `Relation` projection with a switch:
   - `Local`: keep the current ego map
   - `Structure`: add SCC-condensed view
   - `Frontier`: add grouped ready-boundary view
3. Persist stable positions keyed by `workflow + scope + projection + anchor`
   so pushed updates preserve the mental map.
4. Render any component above a density threshold as a matrix or hybrid card
   instead of a raw node-link tangle.
5. Add a compact frontier sparkline to `Pulse` and `Trace`:
   - ready count
   - claimed count
   - blocked count
   - open child-scope count

## Concrete UI moves for the current operator console

- Turn repeated `recover`, `handoff`, and `expand` chains into visible loop
  badges on SCC capsules.
- Stop placing every extra ready node into one growing frontier row once the
  ready boundary crosses a small threshold.
- Add overlay toggles:
  - `dependency`
  - `worker`
  - `allocation`
  - `coalition`
  - `observer`
- Keep the inspector authoritative: every aggregated glyph must drill into node
  ids, worker ids, event sequences, and turn ids.
- Degrade deliberately:
  - `<= 12` visible items: direct node-link
  - `13-40` visible items: SCC capsules plus focus lens
  - `> 40` visible items or a dense pocket: matrix or hybrid view plus frontier table plus time summary

## Recommended implementation stance

- Use SCC condensation to make non-DAG structure legible without lying.
- Use ELK layered for the condensation backbone and ELK force or another
  general-graph layout for internal local pockets that are not usefully layered.
- Keep layout state in saved projections so live subscriptions refresh the data
  without destroying the view.
- Treat frontier visualization as a separate product surface, not as overflow
  from the dependency map.

## Sources

- [Yaniv Frishman and Ayellet Tal, "Online Dynamic Graph Drawing" (IEEE TVCG, 2008)](https://www.ee.technion.ac.il/~ayellet/Ps/tvcg08_FrishmanTal.pdf)
- [NetworkX `condensation()` documentation](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.components.condensation.html)
- [Eclipse Layout Kernel: ELK Layered](https://eclipse.dev/elk/reference/algorithms/org-eclipse-elk-layered.html)
- [Eclipse Layout Kernel: `interactive Layout`](https://eclipse.dev/elk/reference/options/org-eclipse-elk-interactiveLayout.html)
- [Eclipse Layout Kernel: cycle breaking strategy](https://eclipse.dev/elk/reference/options/org-eclipse-elk-layered-cycleBreaking-strategy.html)
- [Eclipse Layout Kernel: ELK Force](https://eclipse.dev/elk/reference/algorithms/org-eclipse-elk-force.html)
- [Yunhai Wang et al., "Structure-aware Fisheye Views for Efficient Large Graph Exploration" (IEEE TVCG, 2018)](https://pubmed.ncbi.nlm.nih.gov/30136962/)
- [Nathalie Henry, Jean-Daniel Fekete, and Michael J. McGuffin, "NodeTrix: A Hybrid Visualization of Social Networks" (InfoVis, 2007)](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/12/Henry_infovis07.pdf)
- [Weiwei Cui et al., "Let It Flow: a Static Method for Exploring Dynamic Graphs" (PacificVis, 2013)](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/12/graphflow.pdf)

