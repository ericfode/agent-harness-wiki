---
title: "Prompt Optimizer Regimes for Harnesses"
created: 2026-04-11
updated: 2026-04-11
type: query
tags: [survey, comparison, context-engineering, program-synthesis]
sources: [raw/papers/arxiv-zhang-2022-tempera.md, raw/papers/azim-2025-autodspy.md, raw/papers/arxiv-yang-2023-opro.md, raw/papers/arxiv-fernando-2023-promptbreeder.md, raw/papers/arxiv-wang-2023-promptagent.md, queries/prompt-optimization-and-dspy-follow-ups.md, queries/prompt-program-representation-and-optimizer-open-questions.md]
---

# Prompt Optimizer Regimes for Harnesses

## Goal
Turn the newly covered systems into a practical regime map for agent harnesses: when is the right abstraction runtime prompt editing, RL over a modular prompt program, in-context black-box search, evolutionary prompt search, or planning over prompt states?

## Short answer
The systems split cleanly by what they treat as the writable artifact and by how much structure they assume in the feedback signal.

- [[tempera]] — runtime editing of the live prompt instance
- [[autodspy]] — RL over modular DSPy program structure
- [[opro]] — black-box optimization over scored candidate histories
- [[promptbreeder]] — evolutionary search over prompts and mutators
- [[promptagent]] — planning over prompt states with reflective error feedback

That is not merely a taxonomy. It is a design choice about what the harness can observe, score, retain, and safely promote.

## Regime map

### 1. Runtime adaptation: [[tempera]]
Use this regime when the problem is query-local and the harness wants to patch the active prompt without pretending it learned a durable artifact. TEMPERA is the clean example because it edits interpretable prompt components at test time: instruction phrases, exemplars, and verbalizers.

Best fit:
- narrow tasks
- fast local adaptation
- human-seeded prompt skeletons
- low appetite for persistent self-modification

Main limit:
- it improves the live prompt instance, not necessarily the harness's long-term artifact library

### 2. RL over modular prompt programs: [[autodspy]]
Use this regime when the writable object is already a structured LM workflow rather than one prompt string. AutoDSPy matters because it treats module choice, signatures, and execution strategy as the RL target.

Best fit:
- modular LM programs
- reusable workflow artifacts
- evaluator loops that can score whole-pipeline behavior
- systems that want promotion and rollback at the program level

Main limit:
- still an early line with thinner empirical depth than the simpler prompt-search papers

### 3. Black-box candidate search: [[opro]]
Use this regime when the harness can score candidates reliably but does not have much structured critique. OPRO is the clean baseline: candidate/value history in, next candidate out.

Best fit:
- scoreable artifacts
- cheap evaluation loops
- minimal structured trace information
- simple optimizer baselines

Main limit:
- weak local credit assignment; it knows what scored well, not necessarily why

### 4. Evolutionary search over prompts and mutators: [[promptbreeder]]
Use this regime when diversity matters and when the optimizer itself should become a writable artifact. Promptbreeder's key move is that the mutation prompts are optimized too.

Best fit:
- exploration-heavy search
- robustness through diversity
- systems willing to retain mutators, not only task prompts
- long-lived libraries of optimization heuristics

Main limit:
- search can become expensive and messy without a disciplined promotion policy

### 5. Planning over prompt states: [[promptagent]]
Use this regime when the harness already produces richer failure evidence and can afford guided search rather than flat proposal/scoring. PromptAgent is the clearest example because it treats prompt improvement as strategic planning over prompt states.

Best fit:
- rich error traces
- expensive but high-value prompt edits
- domains where reflection materially improves the next move
- systems that already preserve intermediate failure evidence

Main limit:
- more machinery, more search budget, and more dependence on the quality of reflective feedback

## My synthesis

### The real divider is not RL versus non-RL
The sharper divider is what kind of learning signal the harness has.

- Only scalar scores? [[opro]] or [[rlprompt]] are natural.
- Live query-specific repair? [[tempera]] is the right mental model.
- Modular prompt programs? [[autodspy]], [[dspy]], and [[sammo]] become more relevant.
- Rich traces and reflection? [[promptagent]], [[promptbreeder]], and [[gepa]] become much more attractive.

### Durable harnesses should store more than a “best prompt”
These systems collectively imply that a serious harness may want to retain:
- candidate prompt histories
- reflective error analyses
- mutation prompts and search heuristics
- module-selection policies
- promotion / rollback provenance

That begins to look less like prompt engineering and more like release engineering for language programs.

### The compile-time versus run-time boundary still matters
[[tempera]] is the clearest runtime-adaptation case here. [[autodspy]], [[opro]], [[promptbreeder]], and [[promptagent]] all lean more toward artifact search that could, in principle, feed a durable release pipeline. A harness that blurs these lanes risks mistaking attractive improvisation for real learning.

## Bottom line
The new coverage fills three missing slots in the regime map:
1. runtime prompt adaptation via [[tempera]]
2. RL over modular prompt programs via [[autodspy]]
3. three non-identical search baselines via [[opro]], [[promptbreeder]], and [[promptagent]]

Together with [[rlprompt]], [[dspy]], [[dspy-assertions]], [[sammo]], [[textgrad]], and [[gepa]], the wiki now has a much cleaner optimizer-family map for prompt programs and language workflows.

## Related pages
Read this with [[prompt-optimization-and-dspy-follow-ups]], [[prompt-program-representation-and-optimizer-open-questions]], [[prompt-program-deployment-open-questions]], and [[prompt-optimization-timeline-and-harness-lessons]].