---
title: "Attention and Attribution Views for LLM Harnesses"
created: 2026-04-11
updated: 2026-04-11
type: query
tags: [survey, context-engineering, mechanistic-interpretability, epistemics]
sources: [raw/articles/context-visualization-research-2026-04-11.md]
---

# Attention and Attribution Views for LLM Harnesses

## Question
If we want to show the user what the model is “attending to now”, what can we honestly show, and what should we refuse to pretend we know?

## Short answer
Raw attention is not a faithful explanation of a model’s answer. It is one internal routing signal among several, and even when you can observe it directly, it should usually be presented as a diagnostic view over a selected token rather than as the model’s revealed inner truth.

The honest UI stack is:
1. observable provenance
2. derived attribution estimates
3. optional internal attention diagnostics for open-weight models

In that order.

## 1. What the literature says

### Attention is not explanation
The strongest corrective is Jain and Wallace's “Attention is not Explanation”: raw attention weights can diverge sharply from gradient importance, and very different attention distributions can yield the same prediction.

This means a user-facing attention heatmap should not be sold as “why the model answered this.”

### Attention can still be useful
The important qualifier from Wiegreffe and Pinter's “Attention is not not Explanation” is that attention can still be informative under disciplined evaluation. Meanwhile Clark et al.'s “What Does BERT Look at?” shows that attention heads can reveal real structure and specialization.

So the right posture is neither mystical trust nor total dismissal. It is diagnostic restraint.

### Derived summaries help
Abnar and Zuidema's “Quantifying Attention Flow in Transformers” introduces rollout and flow summaries that correlate better with some causal or gradient-based importance measures than raw layer-local attention alone.

That still does not make them ground truth. It merely makes them better-behaved proxies.

## 2. What each tool/view really gives you

### Raw attention view
Examples: BertViz and TransformerLens-style internal inspectors

What it gives:
- head-by-head and layer-by-layer attention patterns
- token-to-token routing for a selected token step
- good diagnostics for head specialization or failure analysis

What it does not give:
- a faithful explanation of the final answer
- a single global “what the model is thinking about now” picture

### Rollout / flow view
Examples: attention flow, attention rollout

What it gives:
- more aggregated input-level summaries across layers
- a better first-pass picture than raw attention alone

What it does not give:
- direct internal truth rather than a derived heuristic

### Saliency / attribution view
Examples: Ecco, LIT, MIRAGE, TokenShapley, and answer-to-source attribution systems

What it gives:
- estimated contribution of inputs, tokens, spans, or retrieved documents
- often much more user-relevant than head-local attention

What it does not give:
- exact causal semantics unless backed by explicit counterfactual tests or careful attribution methods

### Counterfactual view
Examples: with/without-source compare, span masking, source replacement

What it gives:
- the clearest user-facing signal of whether a source or span materially affected the output

What it does not give:
- a cheap answer; counterfactuals cost additional runs and careful evaluation criteria

## 3. Open-weight versus API-only honesty

### Open-weight models
You can honestly show:
- raw attention tensors for a selected token, layer, and head
- rollout / flow summaries
- activation or saliency probes
- answer-to-source attribution overlays

Recommended label:
- “Observed attention patterns for selected token”
- “Derived influence estimate”

Not recommended:
- “The model is attending to X” without specifying token/time/layer/head

### API-only models
You usually cannot honestly show true internal attention at all.

You can honestly show:
- included sources and exact provenance
- prompt slot position
- retrieval and rerank scores
- citations and answer-to-source links
- heuristic relevance or proxy salience from a separate model or method, if clearly labeled

Recommended label:
- “Internal attention unavailable from this API”
- “Proxy relevance estimate”
- “Observable provenance and selection signals”

Not recommended:
- fake internal heatmaps that visually imply access to hidden provider state

## 4. Recommended user-facing framing

### Default user surface
Show three nested levels:

1. **Used sources**
   - exact evidence and provenance
2. **Why this source mattered**
   - answer-to-source links, citation spans, counterfactual delta if available
3. **Internal diagnostics**
   - only for expert mode, and only when genuine internals exist

### Best wording
Use language like:
- “supported by”
- “selected because”
- “proxy-used”
- “observed attention pattern”
- “counterfactual effect”

Avoid language like:
- “the model focused on this because...”
- “the model’s true reason was...”
- “attention proves...”

## 5. Concrete design recommendation

### A. Answer-centric inspector
Click an answer sentence or token span.
Show:
- supporting source excerpts
- source provenance and trust state
- answer-to-source links
- optional proxy attribution
- optional counterfactual with/without-source delta

### B. Advanced diagnostics drawer
Only for open-weight models or expert users:
- token picker
- layer/head selector
- raw attention matrix
- rollout summary
- saliency overlay
- explicit disclaimer that this is diagnostic, not a final explanation

### C. API-only fallback
If internals are unavailable:
- hide the diagnostics drawer by default
- show provenance, selection rationale, prompt slot position, and influence proxies instead
- say plainly that internal attention is unavailable

## 6. Main pitfalls
- treating raw attention as faithful explanation
- showing one global “current attention” map without a selected token/time
- failing to distinguish observed internals from derived proxies
- implying access to provider-model internals that the API does not expose
- not separating selection score from answer influence
- giving users a pretty heatmap and no source/provenance trail

## Bottom line
If the question is “what is the model attending to now?”, the honest answer is usually:
- for open weights: a selected-token diagnostic over attention patterns, plus better attribution views nearby
- for API-only systems: not directly knowable, so show provenance and influence proxies instead

The mature product stance is to make provenance primary, attribution secondary, and raw attention diagnostic rather than doctrinal.

## Related pages
Read this with [[context-assembly-visualization-for-harnesses]], [[context-engineering]], [[grounding-moldable-operations-studio-ideas-in-real-research]], [[web-patterns-for-non-linear-harness-interfaces]], and [[neural-native-programming-via-direct-interfaces-to-transformer-internal-layers]].
