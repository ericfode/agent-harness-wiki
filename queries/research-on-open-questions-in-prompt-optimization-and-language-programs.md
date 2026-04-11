---
title: "Research on Open Questions in Prompt Optimization and Language Programs"
created: 2026-04-11
updated: 2026-04-11
type: query
tags: [survey, comparison, context-engineering, program-synthesis]
sources: [queries/open-questions-in-prompt-optimization-and-language-programs.md, queries/prompt-optimization-eval-transfer-robustness-open-questions.md, queries/prompt-program-representation-and-optimizer-open-questions.md, queries/prompt-program-deployment-open-questions.md, raw/articles/prompt-optimization-eval-transfer-robustness-open-questions-2026-04-11.md, raw/articles/prompt-optimization-representation-optimizer-open-questions-2026-04-11.md, raw/articles/additional-cross-cutting-prompt-program-papers-2026-04-11.md]
---

# Research on Open Questions in Prompt Optimization and Language Programs

## Goal
Gather actual research around each of the ten cross-cutting open questions in the prompt-optimization / prompting-systems / [[dspy]] lane, so the questions stop floating as tasteful abstractions and start carrying a real bibliography.

## Executive read
The research picture is now fairly clear. These ten questions are not ten unrelated curiosities; they collapse into three deeper disputes:
- what kind of artifact a language program is
- what kind of evaluator or evidence can be trusted to improve it
- what kind of operational regime can safely run it over time

## 1. What is the right optimization unit?
Anchor research:
- **RLPrompt** (2022) — treats the optimized object as a discrete prompt string.
- **DSPy** (2023) — shifts the unit to a multi-module LM program.
- **DSPy Assertions** (2023) — suggests the unit may be a contract-bearing program, not free prose.
- **Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs** (2024) — treats instructions plus demos as a joint artifact.
- **SAMMO / Symbolic Prompt Program Search** (2024) — makes the unit a symbolic prompt program.
- **TextGrad** (2024) — pushes the unit up to a text-defined computation graph.
- **Adaptive Prompt Structure Factorization** (2026) — treats compositional prompt factors as the searchable object.

Research read:
- The literature has moved steadily away from “one clever string” toward instructions, demos, modules, factors, assertions, and sometimes workflows.
- The unresolved part is not whether structure helps, but which layer should be optimized directly and which should remain fixed scaffolding.
- This question sits at the core of [[instruction-layering]] and [[context-engineering]].

## 2. What evaluator deserves to be trusted?
Anchor research:
- **G-Eval** (2023) — early influential case for rubric-guided LLM judging.
- **A Comparative Study of DSPy Teleprompter Algorithms...** (2024) — tests optimizer outputs against human labels.
- **Prometheus 2** (2024) — specialized open judge for evaluating other LMs.
- **SOPBench** (2025) — executable procedure graphs and rule-based verification.
- **Proxy State-Based Evaluation** (2026) — structured state tracking plus judging in multi-turn tool settings.
- **JudgeFlow** (2026) — adds block-level responsibility rather than only end-task scores.

Research read:
- The trustworthy end of the spectrum is still executable metrics and human calibration, not a lone free-form judge prompt.
- LLM judges become more credible when separated from the optimized artifact, tightly rubric-conditioned, and checked against humans or state-based verification.
- The major unresolved question is evaluator drift: what happens when the judge, rubric, or provider shifts underneath a previously optimized artifact.
- This is the central dispute inside [[evaluation-and-review-loops]].

## 3. Which optimizer belongs in which regime?
Anchor research:
- **RLPrompt** (2022) and **TEMPERA** (2022) — RL-style prompt optimization.
- **[[rlprompt|RLPrompt]]** (2022) and **[[tempera|TEMPERA]]** (2022) — RL-style prompt optimization.
- **[[opro|OPRO]]** (2023) — in-context black-box optimization.
- **[[promptbreeder|Promptbreeder]]** (2023) — evolutionary optimization over prompts and mutation prompts.
- **[[promptagent|PromptAgent]]** (2023) — planning/search over prompt states.
- **TextGrad** (2024) — gradient-like optimization for compound text systems.
- **GEPA** (2025) — reflective evolution challenging RL-heavy baselines.

Research read:
- The literature no longer supports a single sovereign optimizer. Reward form, artifact structure, evaluation cost, and compile-time versus run-time timing all matter.
- RL seems strongest when action spaces and online reward loops are stable; symbolic search needs explicit structure; critique and textual gradients help when language feedback is rich; evolution helps when diversity and non-local jumps matter.
- The missing artifact is a genuine regime map rather than another benchmark victory lap.

## 4. What makes a prompt artifact transferable?
Anchor research:
- **Robust Prompt Optimization for Large Language Models Against Distribution Shifts** (2023).
- **PromptBridge: Cross-Model Prompt Transfer for Large Language Models** (2025).
- **Benchmarking Prompt Sensitivity in Large Language Models** (2025).
- **When Punctuation Matters** (2025).
- **Is It Time To Treat Prompts As Code?** (2025).
- **To Write or to Automate Linguistic Prompts, That Is the Question** (2026).

Research read:
- Transfer is weak by default. Many optimized prompts capture model quirks, benchmark peculiarities, or formatting sensitivities rather than durable task structure.
- The best current guess is that transfer improves when artifacts are more structured, more invariant to paraphrase/formatting, and easier to lightly recalibrate.
- The unresolved question is whether structured prompt programs actually travel better than monolithic prompts or merely fail more elegantly.

## 5. How should structure be exposed?
Anchor research:
- **DSPy** (2023).
- **DSPy Assertions** (2023).
- **Prompting Is Programming: A Query Language for Large Language Models** (2023).
- **SAMMO** (2024).
- **Modular Prompt Optimization: Optimizing Structured Prompts with Section-Local Textual Gradients** (2026).
- **Adaptive Prompt Structure Factorization** (2026).

Research read:
- The field is converging on the claim that prompt systems want explicit structure, but disagrees on whether that structure should be hand-authored, typed, symbolic, section-based, or partially discovered by the optimizer.
- Lightweight languages such as LMQL and heavier programmatic substrates such as [[dspy]] point in the same direction: prompts are becoming executable control objects.
- The unresolved tradeoff is between legibility and search freedom. More structure helps debugging and local repair, but may narrow the search space too early.

## 6. Where should credit assignment happen?
Anchor research:
- **Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs** (2024).
- **TextGrad** (2024).
- **[[autodspy|AutoDSPy]]** (2025).
- **Dspy-based Neural-Symbolic Pipeline to Enhance Spatial Reasoning in LLMs** (2024/2025).
- **JudgeFlow** (2026).
- **Modular Prompt Optimization** (2026).
- **Adaptive Prompt Structure Factorization** (2026).

Research read:
- Once prompt systems become pipelines, end-to-end metrics are too coarse; the literature is moving toward block-level, factor-level, and node-level blame.
- Some systems place credit assignment in the optimizer, others in the evaluator, and others in explicit program structure plus local edits.
- The unresolved question is when local fixes compose cleanly and when the whole pipeline needs recompilation.

## 7. What belongs to compile time versus run time?
Anchor research:
- **DSPy** (2023) and **SAMMO** (2024) — compile-time optimization.
- **[[tempera|TEMPERA]]** (2022) — run-time prompt editing.
- **Reflexion** (2023) — run-time improvement via memory and self-critique.
- **DSPy Assertions** (2023) — hybrid compile-time plus inference-time refinement.
- **Agent Workflow Memory** (2024).
- **Compiled Memory** (2026).

Research read:
- The cleanest emerging framing is not a binary but a three-part split: compile-time optimization, run-time adaptation, and promotion-in-between.
- Current evaluations often blur temporary improvisation and durable learning, which makes systems look wiser than they really are.
- The unresolved question is promotion policy: when should a local fix remain ephemeral, and when should it become a versioned artifact.

## 8. How do we preserve hard constraints under self-modification?
Anchor research:
- **DSPy Assertions** (2023).
- **Can Large Language Models Transform Natural Language Intent into Formal Method Postconditions?** (2024).
- **SOPBench** (2025).
- **MermaidFlow** (2025).
- **VeriGuard: Enhancing LLM Agent Safety via Verified Code Generation** (2025).
- **SEVerA: Verified Synthesis of Self-Evolving Agents** (2026).

Research read:
- The literature increasingly suggests that hard constraints only start to look hard once they are externalized into executable objects: assertions, schemas, procedure graphs, verified policies, or formal specifications.
- Natural-language guardrails alone do not survive optimization pressure very well.
- The unresolved bottleneck is still intent-to-spec translation: turning what humans mean into machine-checkable constraints without absurd overhead.
- This question sits close to [[formal-methods-for-agent-harnesses]] and [[safety-and-permissions]].

## 9. What is the correct writable memory substrate?
Anchor research:
- **Reflexion** (2023).
- **ExpeL** (2023).
- **Agent Workflow Memory** (2024).
- **Compiled Memory** (2026).
- **Memento-Skills** (2026).
- **AtomMem** (2026).
- **Meta Context Engineering via Agentic Skill Evolution** (2026).

Research read:
- The field has clearly forked into multiple writable substrates: reflections, distilled lessons, workflow artifacts, compiled instructions, skill packages, and context policies.
- The likely answer is plural rather than singular: different kinds of learning want different homes.
- The unresolved comparison is still missing: which substrate gives the best tradeoff among transfer, entropy resistance, reviewability, retrieval cost, and rollback ease.
- This question connects directly to [[memory-persistence]], [[memento-skills]], and [[self-evolving-workflows]].

## 10. What is the release engineering model for language programs?
Anchor research:
- **Is It Time To Treat Prompts As Code?** (2025).
- **Compiled Memory** (2026).
- **JudgeFlow** (2026).
- **Harness Design for Long-Running Application Development** (2026).
- **Harness Engineering: Leveraging Codex in an Agent-First World** (2026).
- **in-toto: Providing farm-to-table guarantees for bits and bytes** (2019).
- **Kishu: Time-Traveling for Computational Notebooks** (2024).

Research read:
- The operational frontier now looks much more like release engineering than prompt craft: artifact versioning, provenance, promotion, canaries, rollback, drift monitoring, and postmortem discipline.
- Recent harness work gives partial pieces of this stack, but not yet a clean common contract for language-program artifacts.
- The unresolved question is also ontological: what exactly is being released — a prompt string, an exemplar bundle, a module, a workflow block, a skill package, or a memory/control policy?

## Bottom line
The literature around these ten questions says the same thing from several angles: prompt optimization is maturing into a study of explicit language-program artifacts and the systems needed to evaluate, constrain, promote, and maintain them. The better question is no longer “how do we write a great prompt?” It is “how do we engineer a language program that can improve without becoming illegible or untrustworthy?”

## Related pages
Read this with [[open-questions-in-prompt-optimization-and-language-programs]], [[prompt-optimization-and-dspy-follow-ups]], [[prompt-optimization-timeline-and-harness-lessons]], [[prompt-optimization-eval-transfer-robustness-open-questions]], [[prompt-program-representation-and-optimizer-open-questions]], and [[prompt-program-deployment-open-questions]].
