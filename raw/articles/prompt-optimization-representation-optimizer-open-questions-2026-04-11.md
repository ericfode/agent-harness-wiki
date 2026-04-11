# Prompt optimization representation/optimizer open questions research batch

Date: 2026-04-11
Collector: Hermes Agent
Method: arXiv API (`export.arxiv.org`) and OpenAlex API lookups via `python3` in the local workspace.

## Scope
- Prompt optimization and prompting-system literature centered on representation, abstraction, and optimizer design.
- Focus on prompt programs, DSPy, symbolic prompt-program search, textual gradients, RL prompt optimization, assertions, and module decomposition.
- Explicitly excludes papers whose main contribution is a new base model architecture.

## Core representation / abstraction papers

1. DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines (2023)
   - URL: https://arxiv.org/abs/2310.03714
   - OpenAlex cited_by_count: 50
   - Abstract note: abstracts LM pipelines as text-transformation graphs with declarative modules and a compiler that optimizes the pipeline against a metric.

2. DSPy Assertions: Computational Constraints for Self-Refining Language Model Pipelines (2023)
   - URL: https://arxiv.org/abs/2312.13382
   - OpenAlex cited_by_count: 2
   - Abstract note: adds assertion-like computational constraints plus compilation and inference-time self-refinement strategies for more reliable LM pipelines.

3. Symbolic Prompt Program Search: A Structure-Aware Approach to Efficient Compile-Time Prompt Optimization / SAMMO (2024)
   - URL: https://arxiv.org/abs/2404.02319
   - DOI: https://doi.org/10.18653/v1/2024.findings-emnlp.37
   - OpenAlex cited_by_count: 2
   - Abstract note: treats prompts as symbolic prompt programs and searches over compile-time transformations rather than assuming fixed prompt structure.

4. AutoDSPy: Automating Modular Prompt Design with Reinforcement Learning for Small and Large Language Models (2025)
   - DOI: https://doi.org/10.18653/v1/2025.emnlp-industry.192
   - OpenAlex cited_by_count: 0
   - Abstract note: uses RL to automate DSPy pipeline construction by selecting reasoning modules, signatures, and execution strategies.

5. Fine-Tuning and Prompt Optimization: Two Great Steps that Work Better Together (2024)
   - URL: https://arxiv.org/abs/2407.10930
   - DOI: https://doi.org/10.18653/v1/2024.emnlp-main.597
   - OpenAlex cited_by_count: 7
   - Abstract note: argues modular LM pipelines should sometimes alternate prompt optimization and weight adaptation rather than choosing only one.

6. Dspy-based Neural-Symbolic Pipeline to Enhance Spatial Reasoning in LLMs (2024/2025)
   - URL: https://arxiv.org/abs/2411.18564
   - DOI: https://doi.org/10.1016/j.neunet.2025.108022
   - OpenAlex cited_by_count: 4
   - Abstract note: uses DSPy as a modular substrate in a neural-symbolic pipeline, showing that decomposition itself can be performance-critical.

7. Is It Time To Treat Prompts As Code? A Multi-Use Case Study For Prompt Optimization Using DSPy (2025)
   - URL: https://arxiv.org/abs/2507.03620
   - OpenAlex cited_by_count: 0
   - Abstract note: mixed but real evidence that DSPy-style optimization helps across guardrails, routing, hallucination detection, and prompt-evaluation tasks.

## Core optimizer-design papers

1. RLPrompt: Optimizing Discrete Text Prompts with Reinforcement Learning (2022)
   - URL: https://arxiv.org/abs/2205.12548
   - DOI: https://doi.org/10.18653/v1/2022.emnlp-main.222
   - OpenAlex cited_by_count: 135
   - Abstract note: optimizes discrete prompts with RL, but the resulting prompts are often ungrammatical gibberish, raising representation questions.

2. TEMPERA: Test-Time Prompting via Reinforcement Learning (2022)
   - URL: https://arxiv.org/abs/2211.11890
   - OpenAlex cited_by_count: 8
   - Abstract note: edits prompts at test time using an action space over instructions, exemplars, and verbalizers.

3. Large Language Models Are Human-Level Prompt Engineers / APE (2022)
   - URL: https://arxiv.org/abs/2211.01910
   - OpenAlex cited_by_count: 297
   - Abstract note: treats instructions as programs and uses proposal-and-selection search over natural-language candidates.

4. Reflexion: Language Agents with Verbal Reinforcement Learning (2023)
   - URL: https://arxiv.org/abs/2303.11366
   - OpenAlex cited_by_count: 259
   - Abstract note: replaces weight updates with linguistic feedback plus episodic memory, showing that optimizer state can itself be textual.

5. Automatic Prompt Optimization with “Gradient Descent” and Beam Search / APO or ProTeGi (2023)
   - URL: https://arxiv.org/abs/2305.03495
   - DOI: https://doi.org/10.18653/v1/2023.emnlp-main.494
   - OpenAlex cited_by_count: 131
   - Abstract note: turns critique into textual gradients and prompt edits guided by beam search and bandit selection.

6. Large Language Models as Optimizers / OPRO (2023)
   - URL: https://arxiv.org/abs/2309.03409
   - OpenAlex cited_by_count: 91
   - Abstract note: uses the LM itself as a black-box optimizer that proposes candidate instructions from prior solution-value histories.

7. Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution (2023)
   - URL: https://arxiv.org/abs/2309.16797
   - OpenAlex cited_by_count: 27
   - Abstract note: evolves both task prompts and mutation prompts, making the optimizer prompt itself part of the search object.

8. PromptAgent: Strategic Planning with Language Models Enables Expert-level Prompt Optimization (2023)
   - URL: https://arxiv.org/abs/2310.16427
   - OpenAlex cited_by_count: 5
   - Abstract note: casts prompt optimization as Monte-Carlo-tree-search-style strategic planning over prompt states.

9. TextGrad: Automatic “Differentiation” via Text (2024)
   - URL: https://arxiv.org/abs/2406.07496
   - OpenAlex cited_by_count: 12
   - Abstract note: extends textual-gradient ideas to computation graphs and compound AI systems, not just single prompts.

10. GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning (2025)
    - URL: https://arxiv.org/abs/2507.19457
    - OpenAlex cited_by_count: 0
    - Abstract note: argues natural-language reflection and Pareto-style evolution can outperform GRPO and MIPROv2 with far fewer rollouts.

11. Scaling Textual Gradients via Sampling-Based Momentum (2025)
    - URL: https://arxiv.org/abs/2506.00400
    - OpenAlex cited_by_count: 0
    - Abstract note: explicitly studies instability and context-wall effects in textual-gradient optimization, proposing momentum-style sampling over prompt histories.

## Empirical comparison / evaluation papers

1. A Comparative Study of DSPy Teleprompter Algorithms for Aligning Large Language Models Evaluation Metrics to Human Evaluation (2024)
   - URL: https://arxiv.org/abs/2412.15298
   - OpenAlex cited_by_count: 0
   - Note: compares COPRO, MIPRO, BootstrapFewShot, BootstrapFewShot with Optuna, and KNN few-shot on hallucination detection judged against human labels.

2. Analyzing LLM Instruction Optimization for Tabular Fact Verification (2026)
   - URL: https://arxiv.org/abs/2602.17937
   - DOI: https://doi.org/10.18653/v1/2026.findings-eacl.161
   - OpenAlex cited_by_count: 0
   - Note: compares COPRO, MiPROv2, and SIMBA across direct prediction, CoT, ReAct+SQL, and CodeAct+Python, finding optimizer performance depends on the prompting regime.

## Working synthesis
- The open technical question is no longer just “how do we find a better prompt string?” but “what is the right representation of an LM program, and which optimizer should operate over which parts of that representation?”
- DSPy and SAMMO push the representation side: typed/module-level prompt programs, symbolic transformations, and explicit constraints.
- RLPrompt, TEMPERA, OPRO, Promptbreeder, PromptAgent, TextGrad, and GEPA push different optimizer families over roughly the same object class.
- The evaluation papers suggest optimizer ranking is highly regime-dependent, which means the field still lacks a good abstraction for optimizer selection itself.
