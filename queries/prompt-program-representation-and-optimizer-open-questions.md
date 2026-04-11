---
title: "Prompt Program Representation and Optimizer Open Questions"
created: 2026-04-11
updated: 2026-04-11
type: query
tags: [survey, dspy, context-engineering, program-synthesis]
sources: [raw/articles/prompt-optimization-representation-optimizer-open-questions-2026-04-11.md, raw/articles/prompt-optimization-dspy-followups-2026-04-11.md]
---

# Prompt Program Representation and Optimizer Open Questions

## Executive read
The sharpest open problems in prompt optimization are now upstream of any one optimizer. The field still does not know the best answer to three linked questions:
1. what the optimized object should be
2. what abstraction should expose editable structure without overconstraining search
3. which optimizer family fits which regime

Below are the seven most important open questions I see in the representation / abstraction / optimizer-design cluster.

## 1. What is the right intermediate representation for a prompt program?
Flat prompt strings are easy to mutate but hard to reason about. Typed modules and symbolic program trees are easier to search and debug, but may rule out useful emergent prompt patterns.

Anchors:
- [[dspy]] / DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines (2023)
- [[sammo|Symbolic Prompt Program Search / SAMMO]] (2024)
- [[dspy-assertions|DSPy Assertions]] (2023)

What would resolve it:
- Build a cross-task benchmark where the same systems are expressed as:
  1. one monolithic prompt
  2. a DSPy-style module graph
  3. a SAMMO-style symbolic program
  4. the same program plus assertions/contracts
- Hold model, budget, and evaluator fixed.
- Compare not just accuracy, but search efficiency, optimizer transfer across models, failure localization, and human editability.
- A useful result would be an actual Pareto frontier between representation richness and optimization tractability.

## 2. What should be optimizable, and at what granularity?
Current systems edit different things: instruction wording, few-shot demos, module choice, signatures, tool-use scaffolds, or full workflow topology. The literature still lacks a principled answer to which layers should be optimized jointly versus separately.

Anchors:
- DSPy (module instructions plus demonstrations)
- [[tempera|TEMPERA]] (edits instructions, exemplars, verbalizers at test time)
- [[autodspy|AutoDSPy]] (selects modules, signatures, execution strategies)
- BetterTogether (joint prompt and weight optimization)

What would resolve it:
- Factor the search space into layers: instruction text, examples, decomposition, routing/tool policy, constraints.
- Run ablations where optimizers can touch only one layer, then pairs of layers, then all layers.
- Measure marginal gain per edited layer, optimizer instability, and overfitting under distribution shift.
- The result should be a decomposition map: which components are worth exposing as first-class optimization variables for which task families.

## 3. How should feedback be represented so that prompt updates are stable and reusable?
The field has scalar rewards, natural-language critiques, reflective memories, mutation prompts, and textual gradients, but there is no settled representation for optimizer state or update signals. This is one reason optimizer comparisons are noisy.

Anchors:
- [[rlprompt|RLPrompt]] (scalar reward over discrete prompts)
- APO / ProTeGi (textual gradients)
- [[reflexion|Reflexion]] (verbal feedback plus memory)
- [[textgrad|TextGrad]] (textual backprop over computation graphs)
- Promptbreeder and [[gepa|GEPA]] (reflection/evolution over prompts and optimizer prompts)
- Scaling Textual Gradients via Sampling-Based Momentum (2025)

What would resolve it:
- Standardize a benchmark where the editable program is fixed and only the feedback representation changes.
- Compare scalar reward, free-form critique, structured error taxonomy, trace-level critique, and hybrid reward-plus-critique updates.
- Track variance across runs, convergence speed, quality of final artifacts, and whether updates remain interpretable enough for human review.
- A particularly useful experiment: can structured critiques beat free-form text while remaining cheaper and more stable?

## 4. Which optimizer family wins in which regime?
The literature increasingly suggests there is no universal winner. RL helps in some settings, while evolution, planning, textual gradients, or symbolic search dominate elsewhere. But the field still lacks a regime map.

Anchors:
- [[rlprompt|RLPrompt]], [[tempera|TEMPERA]]
- [[opro|OPRO]]
- [[promptbreeder|Promptbreeder]]
- [[promptagent|PromptAgent]]
- [[textgrad|TextGrad]]
- [[gepa|GEPA]]
- A Comparative Study of DSPy Teleprompter Algorithms (2024)
- Analyzing LLM Instruction Optimization for Tabular Fact Verification (2026)

What would resolve it:
- Build a benchmark matrix varying:
  - reward type: scalar vs judge vs executable metric
  - timing: compile-time vs test-time
  - search object: prompt text vs demos vs modules vs workflow structure
  - environment: deterministic QA vs tool use vs interactive agent tasks
  - budget: evaluation count, latency, token cost
- Report optimizer regret, sample efficiency, robustness to evaluator noise, and transfer across models.
- The field needs optimizer scaling laws or at least a decision chart, not just isolated leaderboard wins.

## 5. How should multi-module systems handle credit assignment?
Once a prompt becomes a pipeline, global scores are too coarse. Failures may come from retrieval, decomposition, tool selection, answer formatting, or reflection policy. Current systems often optimize globally or with weak local heuristics.

Anchors:
- [[dspy]] (module graphs)
- [[textgrad|TextGrad]] (computation-graph optimization)
- [[autodspy|AutoDSPy]] (module/pipeline selection)
- Dspy-based Neural-Symbolic Pipeline to Enhance Spatial Reasoning in LLMs (2024/2025)

What would resolve it:
- Create instrumented benchmarks with per-module traces and executable intermediate checks.
- Compare:
  1. pure end-to-end optimization
  2. pure module-local optimization
  3. hierarchical optimization with learned credit assignment
- Measure whether local fixes compose or interfere, and whether credit assignment improves data efficiency.
- A strong result here would be a practical optimizer that knows when to patch a local module versus rewrite the whole pipeline.

## 6. How should compile-time optimization interact with run-time adaptation?
The literature currently mixes durable prompt-program improvements with ephemeral test-time adaptation. That is conceptually messy: a system may look strong because it improvises locally, not because it learned a reusable artifact.

Anchors:
- [[dspy]] and [[sammo|SAMMO]] (compile-time optimization)
- [[tempera|TEMPERA]] (test-time editing)
- [[reflexion|Reflexion]] (memory-based run-time improvement)
- [[dspy-assertions|DSPy Assertions]] (inference-time self-refinement)
- [[gepa|GEPA]] (few-rollout reflective improvement)

What would resolve it:
- Evaluate three conditions separately:
  1. compile-time only
  2. run-time only
  3. two-level systems that can promote successful run-time edits into long-lived artifacts
- Test on distribution shift and repeated-task settings.
- Measure durability: does an update help only this instance, this task family, or future model versions too?
- The key output should be a clean separation between reusable prompt-program compilation and local adaptive control.

## 7. Do constraints and assertions merely prune search, or do they change the best abstraction?
Assertions are often presented as reliability add-ons, but they may also be representationally important. A prompt program with typed outputs, schemas, and repair contracts may be a fundamentally different optimization object from a free-form prompt.

Anchors:
- [[dspy-assertions|DSPy Assertions]] (2023)
- [[dspy]] (2023)
- Is It Time To Treat Prompts As Code? (2025)
- Analyzing LLM Instruction Optimization for Tabular Fact Verification (2026)

What would resolve it:
- Compare unconstrained optimization against:
  - hard assertions
  - soft penalties
  - repair-loop-based self-refinement
  - typed intermediate representations
- Evaluate not just final task score, but search-space size, brittleness, reward hacking, and failure recoverability.
- The strongest experiment would test whether constraints enable stronger optimizers by making the search object more legible, not merely more restricted.

## Bottom line
The frontier question is not “what is the best prompt optimizer?” in isolation. It is “what representation of a prompting system makes optimization possible, reliable, and transferable?” My current read is:
- [[dspy]] and [[sammo|SAMMO]] are the clearest representation bets.
- Assertions are underrated because they may change both searchability and reliability.
- Optimizer pluralism is here to stay; RL is only one branch.
- The biggest missing artifact is a shared benchmark suite that crosses representation choice, optimizer family, and compile-time versus run-time adaptation.

## Most decisive next experiments
If I had to prioritize only three:
1. Representation benchmark: monolithic prompt vs modular graph vs symbolic program vs asserted program under equal budgets.
2. Optimizer regime map: RL vs evolution vs planning vs textual gradients vs symbolic search across controlled task regimes.
3. Two-level adaptation study: separate compile-time prompt-program optimization from run-time self-repair and test whether successful local adaptations can be promoted safely.

## Related pages
Read this with [[prompt-optimization-and-dspy-follow-ups]], [[prompt-optimization-eval-transfer-robustness-open-questions]], [[prompt-program-deployment-open-questions]], [[instruction-layering]], and [[self-evolving-workflows]].
