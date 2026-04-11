# Prompt optimization evaluation/transfer/robustness open questions research batch

Date: 2026-04-11
Collector: Hermes Agent
Method: OpenAlex API lookups plus targeted arXiv metadata retrieval via `python3` in the local workspace.

## Scope
- Prompt optimization and prompting-system literature focused on evaluation validity, transfer, robustness, and benchmark design.
- Center of gravity: DSPy-style LM programs, teleprompter/optimizer comparisons, textual-gradient and evolutionary optimizers, and robustness/transfer papers that expose where prompt gains fail to travel.
- Explicitly excludes papers whose main contribution is a new base model architecture.

## Evaluation and benchmarking papers

1. Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs (2024)
   - URL: https://arxiv.org/abs/2406.11695
   - DOI: https://doi.org/10.18653/v1/2024.emnlp-main.525
   - Note: MIPRO explicitly studies prompt optimization for multi-stage LM programs without module-level labels, making credit assignment and evaluation design first-class problems.

2. A Comparative Study of DSPy Teleprompter Algorithms for Aligning Large Language Models Evaluation Metrics to Human Evaluation (2024)
   - URL: https://arxiv.org/abs/2412.15298
   - Note: direct optimizer comparison inside DSPy against human-labeled hallucination annotations rather than only an internal proxy metric.

3. Analyzing LLM Instruction Optimization for Tabular Fact Verification (2026)
   - URL: https://arxiv.org/abs/2602.17937
   - DOI: https://doi.org/10.18653/v1/2026.findings-eacl.161
   - Note: optimizer ranking depends on prompting regime, model family, and whether tools are in the loop; strong evidence that one benchmark/task is not enough.

4. To Write or to Automate Linguistic Prompts, That Is the Question (2026)
   - URL: https://arxiv.org/abs/2603.25169
   - Note: systematic comparison of expert-written prompts, base DSPy signatures, and GEPA-optimized signatures across tasks and model configurations; explicitly notes the fairness asymmetry between labeled-data-driven optimization and expert prompt writing.

5. GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning (2025)
   - URL: https://arxiv.org/abs/2507.19457
   - Note: claims higher quality with far fewer rollouts than GRPO and MIPROv2, which makes search-budget normalization central to fair evaluation.

## Transfer and portability papers

1. PromptBridge: Cross-Model Prompt Transfer for Large Language Models (2025)
   - URL: https://arxiv.org/abs/2512.01420
   - Note: frames cross-model prompt reuse as a model-drifting problem and proposes a calibration-light transfer method.

2. Is It Time To Treat Prompts As Code? A Multi-Use Case Study For Prompt Optimization Using DSPy (2025)
   - URL: https://arxiv.org/abs/2507.03620
   - Note: useful negative result as well as positive one; optimized prompts helped some tasks, but a cheaper model did not inherit gains simply by reusing the optimized prompt.

3. Fine-Tuning and Prompt Optimization: Two Great Steps that Work Better Together (2024)
   - URL: https://arxiv.org/abs/2407.10930
   - DOI: https://doi.org/10.18653/v1/2024.emnlp-main.597
   - Note: argues portability limits of prompt-only adaptation and motivates joint prompt-plus-weight evaluation setups.

## Robustness papers

1. Robust Prompt Optimization for Large Language Models Against Distribution Shifts (2023)
   - URL: https://arxiv.org/abs/2305.13954
   - DOI: https://doi.org/10.18653/v1/2023.emnlp-main.95
   - Note: prompt optimization is vulnerable to subpopulation shifts; introduces a setting where prompts must generalize from labeled source data to unlabeled target groups.

2. PromptRobust: Towards Evaluating the Robustness of Large Language Models on Adversarial Prompts (2023)
   - URL: https://arxiv.org/abs/2306.04528
   - DOI: https://doi.org/10.1145/3689217.3690621
   - Note: robustness benchmark with 4,788 adversarial prompts spanning character-, word-, sentence-, and semantic-level perturbations across 8 tasks and 13 datasets.

3. Benchmarking Prompt Sensitivity in Large Language Models (2025)
   - URL: https://arxiv.org/abs/2502.06065
   - Note: introduces Prompt Sensitivity Prediction and PromptSET, showing that even small prompt variations remain hard to predict and benchmark.

4. When Punctuation Matters: A Large-Scale Comparison of Prompt Robustness Methods for LLMs (2025)
   - URL: https://arxiv.org/abs/2508.11383
   - DOI: https://doi.org/10.18653/v1/2025.findings-emnlp.1109
   - Note: unified robustness-method comparison across 8 models and 52 tasks, including multiple non-semantic format perturbations and distribution shifts.

5. Evaluating the Instruction-Following Robustness of Large Language Models to Prompt Injection (2024)
   - URL: https://arxiv.org/abs/2308.10819
   - DOI: https://doi.org/10.18653/v1/2024.emnlp-main.33
   - Note: prompt robustness is not only about typos and paraphrases; embedded adversarial instructions expose a distinct instruction-priority failure mode.

6. InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents (2024)
   - URL: https://arxiv.org/abs/2403.02691
   - DOI: https://doi.org/10.18653/v1/2024.findings-acl.624
   - Note: extends prompt-injection robustness into agentic/tool-integrated systems where retrieved text and tool outputs can silently override developer intent.

## Structured prompt-program papers that matter for the benchmark design question

1. DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines (2023)
   - URL: https://arxiv.org/abs/2310.03714
   - Note: changes the unit of optimization from one prompt string to a multi-module LM program.

2. DSPy Assertions: Computational Constraints for Self-Refining Language Model Pipelines (2023)
   - URL: https://arxiv.org/abs/2312.13382
   - Note: adds assertions and self-refinement strategies, making reliability constraints part of the optimization/evaluation surface.

3. Symbolic Prompt Program Search: A Structure-Aware Approach to Efficient Compile-Time Prompt Optimization / SAMMO (2024)
   - URL: https://arxiv.org/abs/2404.02319
   - DOI: https://doi.org/10.18653/v1/2024.findings-emnlp.37
   - Note: prompts as symbolic prompt programs, with structure-aware compile-time search rather than flat string editing.

4. TextGrad: Automatic “Differentiation” via Text (2024)
   - URL: https://arxiv.org/abs/2406.07496
   - Note: extends optimization to compound AI systems and text-defined computation graphs.

5. Modular Prompt Optimization: Optimizing Structured Prompts with Section-Local Textual Gradients (2026)
   - URL: https://arxiv.org/abs/2601.04055
   - Note: explicitly evaluates section-local prompt editing as an alternative to monolithic prompt rewriting.

6. Adaptive Prompt Structure Factorization: A Framework for Self-Discovering and Optimizing Compositional Prompt Programs (2026)
   - URL: https://arxiv.org/abs/2604.06699
   - Note: factorized prompt programs plus interventional factor-level scoring; directly relevant to module-level credit assignment and cost-aware benchmarking.

## Working synthesis
- The main open issue is no longer whether prompts can be optimized at all; it is how to evaluate prompt-program optimizers without confusing proxy overfitting, search-budget advantages, and genuine end-task improvement.
- Transfer is now a first-class empirical problem: optimized prompts often do not survive model changes, prompt-format perturbations, or subpopulation shift without extra calibration.
- Robustness needs to be measured at multiple layers: prompt wording, prompt format, data distribution, instruction hierarchy, and tool-mediated prompt injection.
- Benchmark design is lagging behind optimizer design. The literature has many new optimizers, but still too few shared suites that equalize search budget, labels, model families, and adversarial/context-shift conditions.
