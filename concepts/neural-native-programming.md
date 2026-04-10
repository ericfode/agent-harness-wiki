---
title: Neural-Native Programming
created: 2026-04-10
updated: 2026-04-10
type: concept
tags: [semantics, formal-methods, program-synthesis, mechanistic-interpretability]
sources: [raw/articles/neural-native-programming-direct-internal-layer-interfaces-draft-2026-04-10.md, raw/articles/transformer-circuits-mathematical-framework.md, raw/papers/geva-2021-transformer-feed-forward-layers-are-key-value-memories.md, raw/papers/arxiv-belrose-2023-tuned-lens.md, raw/papers/arxiv-turner-2023-steering-language-models-with-activation-engineering.md, raw/papers/arxiv-hong-2020-latent-programmer.md, raw/papers/arxiv-gayler-2004-vector-symbolic-architectures.md, raw/papers/kanerva-2009-hyperdimensional-computing.md, raw/papers/plate-1995-holographic-reduced-representations.md, raw/papers/arxiv-tomkins-flanagan-2025-differentiable-vector-symbolic-types.md, raw/papers/arxiv-chen-2021-evaluating-llms-trained-on-code.md]
---

# Neural-Native Programming

## Definition
Neural-native programming means treating the primary program object as something carried in a model’s internal state or a tightly coupled latent representation, rather than as a string of output tokens. The interesting version is not “continuous prompting” with extra romance. It is a model-facing intermediate representation with explicit semantics, a compiler or interpreter, and a deliberate read/write interface into model internals.

## Why this matters
The motivating complaint is straightforward: token text is a rather clumsy bottleneck for model-to-model computation when the model itself already performs its work in a high-dimensional residual workspace. If the internal substrate is where structure is actually being refined, then a future harness may want access to that substrate as a first-class programming surface, much as [[formal-cognition-loop]] routes some problems into proofs or typed constraints instead of leaving them in prose.

## Necessary split: language versus interface
A serious NNPL project has two distinct obligations.

1. **Define the language.**
   The latent object must have composition rules, type or validity constraints, and deterministic execution semantics. Otherwise it is not a language; it is merely an activation puddle with good marketing.
2. **Define the interface.**
   The system must specify where in the model the latent object is read or written, how decoding is stabilized across layers, and what guarantees exist about reproducibility and auditability.

This is why the concept sits between program-synthesis concerns and mechanistic-interpretability concerns. One side asks what a latent program should be; the other asks how that thing can inhabit an actual transformer without dissolving into basis-dependent mush.

## Best current design instinct
The current literature suggests starting from a **discrete or typed latent spine** rather than a purely continuous vector stream. VQ-style codebooks, typed latent ASTs, or vector-symbolic bindings with explicit cleanup mechanisms all look more promising than unconstrained dense vectors if the goal is something debuggable and executable. The strong reason is not austerity for its own sake. It is that NNPL needs crisp failure modes, deterministic compilation, and structural validity checks in order to avoid becoming a high-bandwidth steganographic channel.

## Candidate substrate families
- **Residual-stream interfaces:** read/write the shared hidden workspace described in the transformer-circuits and key-value-memory sources.
- **Layer translators and probes:** tuned-lens-style read heads that make intermediate states legible enough to decode consistently.
- **Latent program objects:** codebooks, typed graphs, or vector-symbolic structures rather than only token strings.
- **Execution anchors:** compilers, interpreters, or test harnesses so meaning is grounded by behavior rather than reconstruction loss.
- **Boundary monitors:** safety checks that inspect the latent object itself, not only the final compiled artifact.

## Main caution
The internal-state interface is attractive precisely because it is high-bandwidth. That is also the danger. Without explicit semantics and logging, NNPL risks becoming opaque control traffic that is difficult to review, constrain, or even describe. In that form it would conflict with the entire spirit of [[harness-engineering]], which increasingly treats legibility and checkability as the real substance of reliability.

## Open questions
- Which latent representation earns the best tradeoff between expressivity and auditability?
- Are mid-layer interfaces genuinely better than output-adjacent ones, or do they mostly feel more mysterious?
- Can a latent program be made robust to perturbation in a way that token programs are not?
- What should the security boundary be: the compiled artifact, the latent artifact, or both?

## Related pages
Read this with [[neural-native-programming-via-direct-interfaces-to-transformer-internal-layers]], [[neural-native-programming-research-program]], [[formal-cognition-loop]], [[theorem-proving-as-cognitive-kernel]], [[non-linear-interface-options-for-next-harness]], [[new-harness-design-notes]], [[harness-engineering]], and [[formal-methods-for-agent-harnesses]].
