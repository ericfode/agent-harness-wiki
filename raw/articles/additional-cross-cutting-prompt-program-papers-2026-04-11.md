# Additional cross-cutting prompt-program papers

Date: 2026-04-11
Collector: Meridian (Hermes)
Method: exact-title verification via OpenAlex API after delegated research passes on prompt-program open questions.

## Scope
A small supporting batch for cross-cutting papers that were useful in the question-by-question synthesis but were not already captured cleanly elsewhere in the wiki's raw prompt-optimization notes.

1. G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment (2023)
- URL: https://doi.org/10.18653/v1/2023.emnlp-main.153
- OpenAlex cited_by_count: 509
- Note: influential early evidence that rubric-guided LLM judges can align better with humans than older automatic metrics; useful for the evaluator-trust question.

2. Prometheus 2: An Open Source Language Model Specialized in Evaluating Other Language Models (2024)
- URL: https://doi.org/10.18653/v1/2024.emnlp-main.248
- OpenAlex cited_by_count: 34
- Note: representative of the specialized-open-judge direction, where evaluation models are explicitly trained and benchmarked for judging rather than improvised ad hoc.

3. Prompting Is Programming: A Query Language for Large Language Models (2023)
- URL: https://doi.org/10.1145/3591300
- OpenAlex cited_by_count: 91
- Note: LMQL-style view of prompting as an executable language with constraints and control flow; useful for the structure-exposure and hard-constraint questions.

4. Kishu: Time-Traveling for Computational Notebooks (2024)
- URL: https://doi.org/10.14778/3717755.3717759
- Note: not prompt-specific, but useful for rollback, checkout, branching, and durable state history when thinking about release engineering for language programs.
