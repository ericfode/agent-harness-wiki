# Prompt optimization and DSPy follow-ups research batch

Date: 2026-04-11
Collector: Meridian (Hermes)
Method: direct arXiv API (`export.arxiv.org`) plus OpenAlex API lookups for title, year, citation count, landing URL, and abstract snippets. This batch was assembled because `web_search` was credit-limited in-session.

## Scope
- Research on RL training prompts and prompting systems, focusing on the prompt/program/workflow surface rather than underlying model architectures.
- Research that directly extends, evaluates, or meaningfully follows up on DSPy.

## RL training prompts and prompting systems

1. Prefix-Tuning: Optimizing Continuous Prompts for Generation (2021)
   - URL: https://doi.org/10.18653/v1/2021.acl-long.353
   - arXiv: https://arxiv.org/abs/2101.00190
   - OpenAlex cited_by_count: 2117
   - Notes: canonical soft-prompt paper; optimizes a continuous prefix while keeping the base LM fixed.

2. Black-Box Tuning for Language-Model-as-a-Service (2022)
   - URL: https://arxiv.org/abs/2201.03514
   - OpenAlex cited_by_count: 56
   - Notes: prompt optimization under API-only access; useful for black-box prompt search settings.

3. RLPrompt: Optimizing Discrete Text Prompts with Reinforcement Learning (2022)
   - URL: https://doi.org/10.18653/v1/2022.emnlp-main.222
   - arXiv: https://arxiv.org/abs/2205.12548
   - OpenAlex cited_by_count: 135
   - Notes: cleanest direct paper on RL over discrete prompts for frozen language models.

4. TEMPERA: Test-Time Prompting via Reinforcement Learning (2022)
   - URL: https://arxiv.org/abs/2211.11890
   - OpenAlex cited_by_count: 8
   - Notes: RL-driven prompt editing at test time rather than only offline prompt search.

5. Large Language Models Are Human-Level Prompt Engineers (2022)
   - URL: https://arxiv.org/abs/2211.01910
   - OpenAlex cited_by_count: 297
   - Notes: Automatic Prompt Engineer (APE); not RL, but a major step toward automated prompt search.

6. Active Prompting with Chain-of-Thought for Large Language Models (2023)
   - URL: https://arxiv.org/abs/2302.12246
   - OpenAlex cited_by_count: 44
   - Notes: prompt selection policy over which examples receive CoT annotation and enter the prompt.

7. Reflexion: Language Agents with Verbal Reinforcement Learning (2023)
   - URL: https://arxiv.org/abs/2303.11366
   - OpenAlex cited_by_count: 259
   - Notes: replaces weight updates with textual self-critique and memory; operationally a prompting-system paper.

8. Automatic Prompt Optimization with “Gradient Descent” and Beam Search (2023)
   - URL: https://doi.org/10.18653/v1/2023.emnlp-main.494
   - arXiv: https://arxiv.org/abs/2305.03495
   - OpenAlex cited_by_count: 131
   - Notes: ProTeGi / APO; textual-gradient prompt editing rather than RL.

9. Large Language Models as Optimizers (2023)
   - URL: https://arxiv.org/abs/2309.03409
   - OpenAlex cited_by_count: 91
   - Notes: OPRO frames prompt optimization as iterative black-box optimization with the LM itself as the optimizer.

10. Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution (2023)
    - URL: https://arxiv.org/abs/2309.16797
    - OpenAlex cited_by_count: 27
    - Notes: evolutionary search over prompts and mutation prompts; important alternative to RL.

11. PromptAgent: Strategic Planning with Language Models Enables Expert-level Prompt Optimization (2023)
    - URL: https://arxiv.org/abs/2310.16427
    - OpenAlex cited_by_count: 5
    - Notes: treats prompt optimization as a strategic planning/search problem.

12. DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines (2023)
    - URL: https://arxiv.org/abs/2310.03714
    - OpenAlex cited_by_count: 50
    - Notes: prompt-program framework; moves optimization target from a single prompt to an LM program/pipeline.

13. TextGrad: Automatic “Differentiation” via Text (2024)
    - URL: https://arxiv.org/abs/2406.07496
    - OpenAlex cited_by_count: 12
    - Notes: optimization framework for compound AI systems via textual feedback; adjacent to DSPy.

14. Fine-Tuning and Prompt Optimization: Two Great Steps that Work Better Together (2024)
    - URL: https://doi.org/10.18653/v1/2024.emnlp-main.597
    - arXiv: https://arxiv.org/abs/2407.10930
    - OpenAlex cited_by_count: 7
    - Notes: argues prompt optimization and model tuning should be treated jointly in modular LM pipelines.

15. GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning (2025)
    - URL: https://arxiv.org/abs/2507.19457
    - OpenAlex cited_by_count: 0
    - Notes: explicit recent claim that reflective/evolutionary prompt optimization can beat RL in some settings.

16. Symbolic Prompt Program Search: A Structure-Aware Approach to Efficient Compile-Time Prompt Optimization (2024)
    - URL: https://doi.org/10.18653/v1/2024.findings-emnlp.37
    - OpenAlex cited_by_count: 2
    - Notes: SAMMO; represents prompt programs symbolically and searches compile-time transformations.

## DSPy follow-ups and closely related work

### Direct extensions and evaluations

1. DSPy Assertions: Computational Constraints for Self-Refining Language Model Pipelines (2023)
   - URL: https://arxiv.org/abs/2312.13382
   - OpenAlex cited_by_count: 2
   - Notes: extends DSPy with assertions / computational constraints and compilation strategies for more reliable pipelines.

2. A Comparative Study of DSPy Teleprompter Algorithms for Aligning Large Language Models Evaluation Metrics to Human Evaluation (2024)
   - URL: https://arxiv.org/abs/2412.15298
   - OpenAlex cited_by_count: 0
   - Notes: empirical comparison of COPRO, MIPRO, BootstrapFewShot, BootstrapFewShot with Optuna, and KNN few-shot within the DSPy framework.

3. Dspy-based Neural-Symbolic Pipeline to Enhance Spatial Reasoning in LLMs (2024)
   - URL: https://arxiv.org/abs/2411.18564
   - OpenAlex cited_by_count: 1
   - Notes: application paper using DSPy inside an LLM + ASP spatial reasoning pipeline.

4. Is It Time To Treat Prompts As Code? A Multi-Use Case Study For Prompt Optimization Using DSPy (2025)
   - URL: https://arxiv.org/abs/2507.03620
   - OpenAlex cited_by_count: 0
   - Notes: multi-use-case study applying DSPy to guardrails, hallucination detection, code generation, routing, and prompt evaluation.

5. Analyzing LLM Instruction Optimization for Tabular Fact Verification (2026)
   - URL: https://doi.org/10.18653/v1/2026.findings-eacl.161
   - arXiv: https://arxiv.org/abs/2602.17937
   - OpenAlex cited_by_count: 0
   - Notes: systematic comparison of DSPy optimizers including COPRO, MiPROv2, and SIMBA.

6. Optimizing LLM Prompt Engineering with DSPy Based Declarative Learning (2026)
   - URL: https://arxiv.org/abs/2604.04869
   - OpenAlex cited_by_count: 0
   - Notes: recent DSPy-centered prompt engineering paper; appears more application-facing than foundational.

7. AutoDSPy: Automating Modular Prompt Design with Reinforcement Learning for Small and Large Language Models (2025)
   - URL: not resolved by OpenAlex landing-page field in-session
   - OpenAlex cited_by_count: 0
   - Notes: explicitly positions itself as the first framework to automate DSPy pipeline construction with reinforcement learning.

### Adjacent systems reacting to the same problem

1. TextGrad: Automatic “Differentiation” via Text (2024)
   - URL: https://arxiv.org/abs/2406.07496
   - Notes: optimization substrate for compound AI systems via textual gradients.

2. Symbolic Prompt Program Search: A Structure-Aware Approach to Efficient Compile-Time Prompt Optimization (2024)
   - URL: https://doi.org/10.18653/v1/2024.findings-emnlp.37
   - Notes: prompt programs as symbolic search objects; very close to the same design thesis as DSPy.

3. Fine-Tuning and Prompt Optimization: Two Great Steps that Work Better Together (2024)
   - URL: https://doi.org/10.18653/v1/2024.emnlp-main.597
   - Notes: from the DSPy orbit; important because it broadens the optimization target from prompts alone to prompt-plus-weight adaptation.

4. GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning (2025)
   - URL: https://arxiv.org/abs/2507.19457
   - Notes: not a DSPy paper per se, but squarely in the same optimizer-for-language-programs conversation.

## Provisional synthesis
- The field has moved from static prompt templates to optimizing prompts, then to optimizing prompt programs and multi-stage LM pipelines.
- Strictly RL-based prompt optimization exists, but a large share of the strongest recent work uses textual gradients, evolutionary search, strategic planning, or compiler-like rewrites instead.
- DSPy matters because it reframes the optimization object: not “find one good string”, but “compile and tune an LM program”.
- The direct research literature following DSPy is still thinner than the library and tooling line around DSPy itself. The most visible paper trail so far is assertions, teleprompter/optimizer evaluation, application studies, and RL-driven automation attempts like AutoDSPy.
