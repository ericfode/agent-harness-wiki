---
title: Prompt-Program Deployment Open Questions
created: 2026-04-11
updated: 2026-04-11
type: query
tags: [survey, context-engineering, work-management, safety]
sources: [queries/prompt-optimization-timeline-and-harness-lessons.md, queries/arxiv-self-evolving-workflows-for-codex-control-plane.md, raw/articles/prompt-optimization-dspy-followups-2026-04-11.md, raw/papers/arxiv-shinn-2023-reflexion.md, raw/papers/arxiv-zhao-2023-expel.md, raw/papers/arxiv-wang-2024-agent-workflow-memory.md, raw/papers/arxiv-rhodes-2026-compiled-memory.md, raw/papers/arxiv-zhou-2026-memento-skills.md, raw/papers/arxiv-li-2025-sopbench.md, raw/papers/arxiv-pan-2024-webcanvas.md, raw/papers/arxiv-xu-2025-robustflow.md, raw/papers/arxiv-zheng-2025-mermaidflow.md, raw/papers/arxiv-ma-2026-judgeflow.md, raw/papers/arxiv-banerjee-2026-severa.md, raw/papers/arxiv-huo-2026-atommem.md, raw/papers/arxiv-ye-2026-meta-context-engineering.md, raw/articles/anthropic-harness-design-long-running-apps.md, raw/articles/openai-harness-engineering.md]
---

# Prompt-Program Deployment Open Questions

## Goal
Identify the unresolved questions that appear once prompt optimization stops being an offline benchmark trick and becomes a deployment-time control-plane problem inside long-lived agent harnesses.

## Short answer
The literature is now reasonably rich on how to optimize prompts, prompt programs, workflows, and writable skills. It is still much thinner on how to operate those artifacts over time. The main gaps cluster around compile-time versus runtime adaptation, promotion and rollback, hard safety constraints, drift, human oversight, memory boundaries, and the packaging of learned artifacts inside durable harnesses.

## Open questions

### 1. What should be compiled once, and what should adapt online?
Compile-time systems such as [[dspy]] and [[sammo|SAMMO]] optimize reusable prompt programs before deployment. Runtime systems such as [[tempera|TEMPERA]], [[reflexion|Reflexion]], and [[agent-workflow-memory|Agent Workflow Memory]] adapt to the current query, trajectory, or local failure. What is still missing is a principled boundary between:
- ephemeral per-instance adaptation
- promotable artifact changes
- reusable workflow or skill rewrites

The unresolved systems question is not merely "which optimizer is best?" It is whether a harness can tell the difference between a one-off improvisation and a durable improvement.

Anchors:
- DSPy
- [[sammo|SAMMO / Symbolic Prompt Program Search]]
- [[tempera|TEMPERA]]
- Reflexion
- Agent Workflow Memory

Work that would answer it:
- Run the same harness with three explicit lanes: offline compilation, runtime adaptation, and candidate promotion.
- Log whether runtime edits transfer across later tasks or only help the current episode.
- Measure task success, cross-task transfer, operator review burden, and regression rate after promotion.

### 2. What promotion, shadowing, and rollback policy should govern optimized prompt artifacts?
A better benchmark score is not yet a deployment policy. Long-lived harnesses need canaries, blame assignment, lineage, and fast rollback when a newly promoted artifact quietly degrades other tasks. Compiled Memory gets closest by using a promotion gate for instruction rewrites, and JudgeFlow gets closer still by localizing responsibility to individual workflow blocks. But the literature still lacks a standard promotion contract for prompt artifacts analogous to software release engineering.

Anchors:
- Compiled Memory
- JudgeFlow
- Harness Design for Long-Running Application Development
- Harness Engineering: Leveraging Codex in an Agent-First World

Work that would answer it:
- Version every prompt module, exemplar bundle, and workflow edit as a first-class artifact with lineage.
- Compare promotion policies: offline-only score, shadow traffic, canary rollout, evaluator-triggered promotion, and human approval.
- Measure rollback frequency, mean time to detection, blast radius of regressions, and operator trust.

### 3. How can hard safety constraints survive self-modifying prompt programs?
Prompt optimization is attractive partly because its artifacts are inspectable, but that same editability creates a fresh safety problem: the system can optimize itself into policy violations, schema breakage, or unsafe action plans. The open question is how to let prompt programs evolve while keeping some constraints genuinely hard rather than advisory.

Anchors:
- [[dspy-assertions|DSPy Assertions]]
- [[sopbench]]
- MermaidFlow
- SEVerA

Work that would answer it:
- Layer static assertions, executable SOP verifiers, and runtime action monitors into one harness.
- Adversarially mutate prompt artifacts and workflow graphs to test whether constraints fail open or fail closed.
- Report the Pareto frontier between capability gain and safety-violation rate.

### 4. How brittle are optimized prompt artifacts under model, environment, and judge drift?
A prompt artifact that wins on one model version, benchmark slice, or UI layout may collapse after an API update or a paraphrased task description. RobustFlow and [[webcanvas]] show parts of this problem, but prompt deployment still lacks a mature notion of artifact half-life under real-world drift.

Anchors:
- RobustFlow
- [[webcanvas]]
- [[sopbench]]
- Harness Engineering: Leveraging Codex in an Agent-First World

Work that would answer it:
- Re-run promoted artifacts on frozen tasks, paraphrase variants, model-version variants, and live environment canaries.
- Track score decay, behavior variance, and failure modes after each model or environment change.
- Add automatic demotion or review triggers when artifact robustness falls below threshold.

### 5. Which writable memory surface should accumulate deployed learning?
The field now offers several plausible accumulation surfaces:
- reflection memories in the style of Reflexion and ExpeL
- compiled instruction rewrites in Compiled Memory
- reusable workflow artifacts in Agent Workflow Memory
- skill libraries in [[memento-skills]]
- context or memory-control policies in Meta Context Engineering and AtomMem

The open question is which of these should be the long-term learning substrate for a deployed harness. Different surfaces may optimize for different things: transfer, inspectability, safety review, retrieval cost, and resistance to entropy.

Anchors:
- Reflexion
- ExpeL
- Compiled Memory
- Agent Workflow Memory
- [[memento-skills]]
- Meta Context Engineering via Agentic Skill Evolution
- AtomMem

Work that would answer it:
- Hold the base model fixed and compare several writable memory substrates on the same repeated task families.
- Measure transfer, stale-error persistence, reviewability, storage growth, and ease of rollback.
- Study whether different lessons naturally belong in different substrates instead of forcing one universal memory object.

### 6. Where should human oversight enter the loop once prompt optimization becomes continuous?
The evaluator literature strongly suggests that a separate judge is useful, but it does not settle where human judgment must remain in the loop. Humans may still be needed for rubric design, evaluator calibration, promotion approval, and postmortems on silent regressions. The unresolved operational question is how to place humans so that they catch reward hacking without becoming the whole control plane.

Anchors:
- Harness Design for Long-Running Application Development
- Anthropic's Three-Agent Harness for Long-Running AI Development
- JudgeFlow
- [[sopbench]]

Work that would answer it:
- Route only high-risk, high-novelty, or evaluator-disagreement cases to humans.
- Compare full human approval, selective approval, and post-hoc audit regimes.
- Measure review hours, missed failures, evaluator overconfidence, and operator willingness to trust promoted artifacts.

### 7. What is the right runtime home for optimized prompt artifacts inside long-lived harnesses?
Once prompt programs become durable system components, they need a home: repo files, skill packages, registries, scoped instruction layers, session handoff bundles, or some hybrid. Anthropic and OpenAI both push toward repository artifacts and structured handoffs; [[memento-skills]] pushes toward markdown skill objects; [[dspy]] pushes toward module-level program artifacts. What is still missing is a stable packaging and loading contract for long-lived harnesses.

Anchors:
- [[dspy]]
- [[memento-skills]]
- Harness Design for Long-Running Application Development
- Harness Engineering: Leveraging Codex in an Agent-First World

Work that would answer it:
- Implement an artifact registry with explicit scope, inheritance, signatures, provenance, and loading rules.
- Test session reset, cross-surface continuation, subagent specialization, and crash recovery with the same artifact store.
- Measure resumability, debugging speed, multi-agent coordination quality, and how often operators can explain why a given artifact was active.

## Bottom line
The live research frontier is no longer just "find better prompts." It is how to run prompt artifacts as durable, reviewable, self-improving system components. The strongest next experiments will look less like prompt competitions and more like release engineering for language programs: clear separation between runtime adaptation and durable updates, explicit promotion and rollback gates, executable safety constraints, drift canaries, calibrated human oversight, and a real artifact packaging model for long-lived harnesses.

## Related pages
Read this with [[prompt-optimization-timeline-and-harness-lessons]], [[prompt-optimization-and-dspy-follow-ups]], [[dspy]], [[self-evolving-workflows]], [[memory-persistence]], [[evaluation-and-review-loops]], [[harness-engineering]], and [[instruction-layering]].
