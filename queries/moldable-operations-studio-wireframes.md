---
title: Moldable Operations Studio Wireframes
created: 2026-04-09
updated: 2026-04-09
type: query
tags: [orchestration, work-management, context-engineering, comparison]
sources: [queries/moldable-operations-studio-architecture-spec.md, queries/moldable-operations-studio-schema-pass.md, queries/grounding-moldable-operations-studio-ideas-in-real-research.md, queries/sci-fi-audit-for-moldable-operations-studio.md]
---

# Moldable Operations Studio Wireframes

## Goal
Translate the moldable-operations-studio architecture into concrete surfaces that a human could actually operate. This page is the screen-model companion to [[moldable-operations-studio-architecture-spec]] and the surface-level companion to [[moldable-operations-studio-schema-pass]].

## Diagram asset
- Excalidraw board: `raw/assets/moldable-operations-studio-wireframes.excalidraw`

The board collects the first serious six surfaces in one place:
1. fleet wallboard
2. work graph / branch studio
3. evidence / whyline inspector
4. queue / approval cockpit
5. spatial evidence canvas
6. pocket inspector

## Global chrome rules
Every serious surface should carry the same top-band invariants:
- mode (`live`, `replay`, `simulation`, `inferred`)
- current view name and object path
- epoch / membership version
- causal frontier or lag indicator
- current principal / session / label state
- stale marker when the surface cannot satisfy the required frontier

This is the visual discipline that keeps the room from becoming theatrical nonsense.

## 1. Fleet wallboard
**Purpose:** room-scale common operating picture.

**Questions it should answer quickly:**
- what is on fire?
- what is waiting for a human?
- which branch, run, or coalition changed state recently?
- what mode and epoch is the room in right now?

**Layout:**
- left: critical queue
- center: fleet grid / common operating picture
- right: hot inspector for the currently selected object
- bottom: event ticker and room notices

```text
+------------------------------------------------------------------------------------------------+
| MODE | VIEW | PATH | epoch | frontier | stale? | principal | labels                            |
+------------------------------------------------------------------------------------------------+
| Critical queue      | Fleet grid / COP                        | Hot inspector                    |
| - approvals         | rows = agents / branches               | selected object                  |
| - stalled runs      | cols = state / risk / owner / mode     | why blocked? what changed?       |
| - escalations       | click cell -> focus elsewhere          | next allowed actions             |
+------------------------------------------------------------------------------------------------+
| Event ticker | epoch changes | mode alarms | replay/live boundary | room notices                    |
+------------------------------------------------------------------------------------------------+
```

## 2. Work graph / branch studio
**Purpose:** structure-first planning, promotion, and dependency reasoning.

**Questions it should answer quickly:**
- what depends on what?
- why is this branch not promotable?
- which approvals or evidence are missing?
- what changed since checkpoint X?

**Layout:**
- left: branch tree and checkpoint navigator
- center: DAG canvas
- right: detail inspector
- bottom: promotion bar

```text
+------------------------------------------------------------------------------------------------+
| MODE | VIEW | PATH | epoch | frontier | stale? | principal | labels                            |
+------------------------------------------------------------------------------------------------+
| Branch / checkpoint | DAG canvas                             | Selection inspector              |
| navigator           | work items / branches / approvals      | required approvals               |
| filters             | blocked edges / superseded nodes       | frontier delta                   |
|                     | coalition links                        | budgets / promotion blockers     |
+------------------------------------------------------------------------------------------------+
| Promotion bar: source checkpoint | target branch | stale? | ready? | approve / merge / defer       |
+------------------------------------------------------------------------------------------------+
```

## 3. Evidence / Whyline inspector
**Purpose:** inspect an object, explain it, replay it, and compare it.

**Questions it should answer quickly:**
- why did this output happen?
- why did this branch fail?
- what was concurrent but independent?
- what if I flip this assumption?

**Layout:**
- left: artifact stack
- center: primary evidence pane
- right: why / why-not causal chain
- bottom: lineage and replay footer

```text
+------------------------------------------------------------------------------------------------+
| MODE | VIEW | PATH | epoch | frontier | stale? | principal | labels                            |
+------------------------------------------------------------------------------------------------+
| Artifact stack      | Primary evidence pane                  | Why / why-not chain              |
| logs / traces       | trace scrubber / diff / screenshot     | causal parents                   |
| snapshots / reports | annotate / bookmark                    | first bad event                  |
|                     |                                        | concurrent siblings / counterfactual |
+------------------------------------------------------------------------------------------------+
| lineage | checkpoint | replay isolation | derived from | mode                                   |
+------------------------------------------------------------------------------------------------+
```

## 4. Queue / approval cockpit
**Purpose:** make human decisions typed, bounded, and legible.

**Questions it should answer quickly:**
- what is waiting for judgment?
- what evidence is required?
- what rights or budgets are affected?
- what caveats should constrain this grant?

**Layout:**
- left: approval inbox
- center: decision sheet
- right: required evidence
- bottom: action strip

```text
+------------------------------------------------------------------------------------------------+
| MODE | VIEW | PATH | epoch | frontier | stale? | principal | labels                            |
+------------------------------------------------------------------------------------------------+
| Approval inbox      | Decision sheet                         | Required evidence                |
| pending / expired   | requested action                       | test report / diff / whyline     |
| rescinded / blocked | label / secrecy check                  | compare candidate branches       |
| priority + owner    | budget impact / caveats                |                                  |
+------------------------------------------------------------------------------------------------+
| approve | reject | rescind | request more evidence | grant caveated budget                      |
+------------------------------------------------------------------------------------------------+
```

## 5. Spatial evidence canvas
**Purpose:** loose arrangement before formalization.

**Questions it should answer quickly:**
- how do these artifacts feel related before I know the exact graph?
- which clusters should become formal work items or evidence bundles?
- what should be promoted to the room?

**Layout:**
- large loose canvas
- right-side promotion inspector
- bottom action rail

```text
+------------------------------------------------------------------------------------------------+
| MODE | VIEW | PATH | epoch | frontier | stale? | principal | labels                            |
+------------------------------------------------------------------------------------------------+
|                                                                 | Promotion inspector              |
|            loose evidence canvas                                | turn cluster into:               |
|            cluster cards / notes / hypotheses                   | - work item                      |
|            compare branches / pin traces                        | - evidence bundle                |
|                                                                 | - checkpoint                     |
|                                                                 | - queue item / view definition   |
+------------------------------------------------------------------------------------------------+
| save arrangement | publish to room | promote cluster | attach annotations | compare checkpoint |
+------------------------------------------------------------------------------------------------+
```

## 6. Pocket inspector
**Purpose:** pocket-scale supervision and staging with low blast radius.

**Questions it should answer quickly:**
- what is this object?
- why should I care?
- what are the safe local actions?
- should I pull this into the room?

**Layout:**
- compact chrome
- object summary card
- key evidence card
- constrained action card

```text
+--------------------------------------+
| MODE | object | frontier             |
+--------------------------------------+
| Compact inspector                    |
| state / risk / owner / why blocked   |
+--------------------------------------+
| Key evidence                         |
| 1 trace / 1 diff / 1 note            |
+--------------------------------------+
| Actions                              |
| pull to wall | annotate | ack | ask  |
+--------------------------------------+
```

## Primary interaction loops

### Loop A: alert to explanation
1. wallboard cell turns critical
2. operator selects it
3. evidence inspector opens on the same object id
4. whyline chain answers why / why-not
5. operator bookmarks or annotates the relevant cause

### Loop B: explanation to decision
1. evidence inspector identifies missing action or branch
2. queue cockpit opens with the related approval request
3. decision sheet shows caveats, labels, and budget impact
4. approval or rejection lands as a durable control-plane fact

### Loop C: private to public
1. specialist stages a filter or note on pocket inspector
2. explicitly promotes it to the room
3. wallboard updates to a published shared view
4. room sees the same object and frontier, not a screenshot

### Loop D: loose to formal
1. investigator clusters evidence on the spatial canvas
2. selects a cluster
3. promotion inspector converts it into a work item, evidence bundle, checkpoint, or view definition
4. graph / queue views now treat that cluster as a typed object

## Wireframe rules
- The wallboard is the common operating picture, not the only place where meaning exists.
- The pocket inspector is the low-blast-radius staging surface.
- Any destructive or promotive action must show mode, frontier, epoch, and authority implications before it fires.
- The evidence inspector should always make lineage and replay state visible.
- The queue cockpit should never ask for judgment without attached evidence.
- The spatial canvas should admit ambiguity first and formalize second.

## What this clarifies for implementation
The wireframes suggest a first vertical slice built around four synchronized screens instead of all six at once:
1. fleet wallboard
2. evidence / whyline inspector
3. queue / approval cockpit
4. pocket inspector

That slice is enough to prove:
- one state, many surfaces
- mode clarity
- evidence-linked decisions
- public/private surface promotion

The graph studio and spatial canvas can follow once the basic control-plane and evidence loops work.

## Related pages
Read this with [[grounding-moldable-operations-studio-ideas-in-real-research]], [[moldable-operations-studio-architecture-spec]], [[moldable-operations-studio-schema-pass]], [[sci-fi-audit-for-moldable-operations-studio]], and [[web-patterns-for-non-linear-harness-interfaces]].
