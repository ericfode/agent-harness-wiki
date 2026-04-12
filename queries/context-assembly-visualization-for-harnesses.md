---
title: "Context Assembly Visualization for Harnesses"
created: 2026-04-11
updated: 2026-04-11
type: query
tags: [survey, comparison, context-engineering, epistemics]
sources: [raw/articles/context-visualization-research-2026-04-11.md, concepts/context-engineering.md, queries/web-patterns-for-non-linear-harness-interfaces.md, queries/grounding-moldable-operations-studio-ideas-in-real-research.md]
---

# Context Assembly Visualization for Harnesses

## Goal
Figure out a better way to show the user:
1. what context is being assembled
2. where that context came from
3. how much trust those places deserve
4. what the model appears to be using now

## Short answer
The right surface is not one more transcript sidebar. It is a three-layer inspector over one canonical context/provenance substrate:

1. **Assembly layer** — exact, auditable, and mostly deterministic
2. **Trust layer** — policy, provenance, verification, freshness, and uncertainty
3. **Influence layer** — observable or estimated evidence of what mattered for the current answer

The crucial discipline is to keep those three layers distinct. If you collapse them into one heatmap or one “importance score,” you will lie in at least two different ways at once.

## 1. The assembly layer should be exact
This layer answers: what got included, from where, by which transformation path, and where did it land in the final prompt or tool context?

This is the part that should be mechanically true.

### What to show
For each context item or span:
- source kind: user message, repo file, tool output, retrieval result, memory item, policy text, generated summary
- stable id / source path / URL
- exact selected span or excerpt
- token count / byte size
- inclusion mode: pinned, retrieved, carried over, policy-required, summarized, derived
- retrieval or selection path: query rewrite, retriever, reranker, filter, truncation, summarization
- final prompt position or slot
- supersession / eviction history if it was later replaced or trimmed

### Best representation
Use three coordinated views over the same underlying objects:

1. **Included / Candidate / Dropped lists**
   - the fastest way to answer “what did you use?”
2. **Assembly DAG**
   - request -> query rewrite -> retrieval -> rerank/filter -> summarization -> final prompt slots
3. **Prompt slot / timeline view**
   - where each context item actually landed and when it was added, revised, or evicted

This is the civilized alternative to making users infer prompt assembly from vibes.

## 2. The trust layer should show evidence states, not a reputation score
This layer answers: how much should I trust this source, and on what grounds?

The strong result from the provenance and trust literature is that trust should be shown as a bundle of evidence-bearing properties, not as one scalar virtue number.

### What to show per source
- **origin** — who or what produced it
- **integrity / verification** — signed, policy-verified, reviewed, unverified, disputed
- **freshness** — current, stale relative to frontier, superseded
- **scope / labels** — public, private, privileged, selectively disclosed
- **authorization context** — credential, approval chain, policy version, quorum state
- **uncertainty** — inferred, partial provenance, conflicting attestations, low-signal heuristic
- **revocation / invalidation** — revoked, challenged, invalidated, replaced

### UI rule
Trust cues should appear inline at the point of use.

A source row should already show the key badges. The inspector can then expand to the full proof bundle, credential chain, provenance receipts, or dispute history.

### Strong recommendation
Do not show a single global trust score for a source or actor.

That would collapse competence, recency, authorization, policy compliance, and uncertainty into one decorative lie. Better to show a compact trust state vector than one falsely magical number.

## 3. The influence layer should be explicit about what kind of signal it shows
This layer answers: what seems to have mattered for the current answer or action?

This is where many systems become theatrical. The correct move is to distinguish several very different notions of influence.

### A. Lineage / contribution existence
Question: was this source actually included and linked into the derivation path?

This is exact provenance.

### B. Selection rationale
Question: why was this source chosen?
- similarity score
- graph-neighbor relation
- recency
- manual pin
- policy requirement
- prior successful use

This is still not the same as answer influence.

### C. Usage proxy
Question: does the model appear to have used it?
- answer-to-source attribution
- highlighted supporting spans
- saliency / attribution estimates
- citation or quote linkage

This is approximate.

### D. Counterfactual effect
Question: what changes if this source is removed or swapped?
- answer changes materially
- groundedness drops
- judge score shifts
- source was redundant with another source

This is the strongest user-facing causal signal, though still dependent on the evaluation setup.

### UI rule
Name the kind of signal directly.
For example:
- included
- selected because
- proxy-used
- measured effect

If you label all of those as “importance,” you deserve the confusion you get.

## 4. Shared view versus role-specific view
The common-operating-picture literature makes one point especially clean: one shared picture is not enough.

You want:
- one canonical operational substrate
- a shared common operating picture
- role-specific situational panes derived from the same substrate

### Suggested split
**Shared COP**
- current mode: live / replay / simulation / inferred
- current frontier / checkpoint
- source counts and token budget
- blocked / stale / policy-missing warnings
- major context branches and summaries

**Reviewer pane**
- missing evidence
- proof / approval chain
- source trust states
- whyline from answer or diff back to sources

**Planner pane**
- what was selected
- what was excluded
- context budget pressure
- missing but desired sources

**Investigator pane**
- assembly DAG
- replayable provenance trail
- with/without-source compare
- conflicting or superseded sources

The wallboard is the common operating picture. It is not the only place where meaning lives.

## 5. What to do about “what the model is attending to now”
This is the dangerous part.

### What can be shown honestly
For open-weight models:
- attention patterns for a selected output token / layer / head
- derived rollout or attention-flow summaries
- attribution or saliency estimates
- answer-to-source highlighting
- counterfactual source removal or span masking results

For API-only models:
- exact source provenance
- prompt slot placement
- retrieval/rerank scores
- citations and answer-to-source links
- heuristic or shadow-model salience estimates, if clearly labeled as proxies

### What should not be claimed lightly
- one global “current attention” state
- raw attention as a faithful explanation of the answer
- provider-model internals when the API does not expose them

The safe formulation is:
- “observed attention patterns” for open-weight internals
- “derived influence estimate” for rollout/saliency/counterfactuals
- “observable provenance and selection signals” for API-only systems

## 6. Concrete UI sketch

### Top bar
- mode: live / replay / simulation
- run id / branch / frontier
- token budget used / available
- stale / policy / approval warnings

### Left pane: Context set
Tabs:
- Included
- Candidates
- Dropped

Each row:
- title/path/URL
- selected span preview
- tokens used
- inclusion mode
- why chips
- trust badges
- prompt-position mini-bar
- influence chip type

### Center pane: Assembly view
Toggle:
- DAG
- timeline
- final prompt view

Hovering a source should highlight its full path into the assembled context and where it landed.

### Right pane: Why / trust / influence inspector
On selecting an answer span or source row, show:
- exact supporting excerpt
- answer-to-source links
- whyline chain
- trust state vector
- verification receipts / credentials / supersession
- proxy attribution or measured with/without-source delta
- redundancy / complementarity notes where available

### Bottom action bar
- pin
- exclude
- rerank
- expand excerpt
- compare with / without source
- annotate
- open provenance trail

## 7. Main design rules
1. Keep provenance exact.
2. Keep trust multidimensional.
3. Keep influence labels honest.
4. Show trust cues inline, not only in a side dashboard.
5. Preserve replay and supersession history.
6. Let users traverse from answer -> source -> derivation path.
7. Use one canonical substrate with many projections, not many half-synchronized panes.

## 8. Main pitfalls
- one scalar trust score
- one undifferentiated “importance” score
- raw attention heatmaps presented as answer explanations
- hiding superseded or revoked sources
- separate truth stores for different roles
- node-link provenance hairballs with no aggregation
- summary metrics with no drill-down to concrete examples
- mode confusion between live, replay, and simulation views

## Bottom line
If you want users to understand assembled context, trust, and current model use, the right primitive is not “show more of the prompt.” It is a provenance-rich, role-aware context inspector that cleanly separates:
- what was assembled
- why it was trusted
- how it appears to matter now

That is the difference between legibility and dashboard cosplay.

## Related pages
Read this with [[context-engineering]], [[web-patterns-for-non-linear-harness-interfaces]], [[grounding-moldable-operations-studio-ideas-in-real-research]], [[moldable-operations-studio-architecture-spec]], [[attention-and-attribution-views-for-llm-harnesses]], and [[sovereignty-and-observed-goals-ledgers-for-multiplayer-harnesses]].
