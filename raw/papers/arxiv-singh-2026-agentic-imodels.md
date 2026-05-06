---
title: "Agentic-imodels: Evolving agentic interpretability tools via autoresearch"
author: Chandan Singh, Yan Shuo Tan, Weijia Xu, Zelalem Gero, Weiwei Yang, Michel Galley, Jianfeng Gao
url: https://arxiv.org/abs/2605.03808v1
pdf: https://arxiv.org/pdf/2605.03808v1
source: https://arxiv.org/e-print/2605.03808
date: 2026-05-05
ingested: 2026-05-06
arxiv_id: 2605.03808v1
primary_category: cs.AI
categories: [cs.AI, cs.CL, cs.LG]
---

# Agentic-imodels: Evolving agentic interpretability tools via autoresearch

**Source:** [arXiv:2605.03808v1](https://arxiv.org/abs/2605.03808v1)  
**PDF:** <https://arxiv.org/pdf/2605.03808v1>  
**arXiv source:** <https://arxiv.org/e-print/2605.03808>  
**Authors:** Chandan Singh, Yan Shuo Tan, Weijia Xu, Zelalem Gero, Weiwei Yang, Michel Galley, Jianfeng Gao  
**Affiliations from source TeX:** Microsoft Research; National University of Singapore  
**Published:** 2026-05-05  
**Version read:** v1  
**Primary category:** cs.AI  
**All categories:** cs.AI, cs.CL, cs.LG  
**Code:** <https://github.com/csinva/agentic-imodels>

## Retrieval notes

- User supplied the canonical arXiv URL `https://arxiv.org/abs/2605.03808`.
- `web_extract` was unavailable in this Hermes session because Firecrawl was not configured.
- arXiv Atom API grounded metadata via `https://export.arxiv.org/api/query?id_list=2605.03808`.
- arXiv HTML was attempted at `https://arxiv.org/html/2605.03808v1` and `https://arxiv.org/html/2605.03808`; both returned HTTP 404 at ingest time.
- The source package from `https://arxiv.org/e-print/2605.03808` was fetched successfully as `application/gzip` and the LaTeX source was inspected directly (`main.tex`, `content.tex`, `appendix.tex`, and tables).

## Abstract

Agentic data science systems are increasingly capable of autonomously analyzing, fitting, and interpreting data, but their statistical tools were designed to be interpreted by humans rather than agents. The paper introduces **Agentic-imodels**, an agentic autoresearch loop that evolves data-science tools designed for agent interpretability.

The system develops a library of `scikit-learn`-compatible tabular regressors optimized for predictive performance and an LLM-based interpretability metric. The metric tests whether a fitted model's string representation is **simulatable** by an LLM: can the LLM answer questions about the model's behavior from the printed representation alone? The authors report that evolved models improve both predictive performance and agent-facing interpretability, generalize to new datasets and held-out tests, and improve downstream agentic data-science performance on BLADE for Copilot CLI, Claude Code, and Codex by up to 73%.

## Extracted structure

- **Introduction:** Frames the mismatch between human-interpretable statistical tools and agent-interpretable tools in agentic data science.
- **Related work:** Connects interpretable ML, agentic data science, automated model discovery, autoresearch, evolving skills, and harness optimization.
- **Methods:** Defines the autoresearch loop: a coding agent modifies a `scikit-learn`-compatible Python class with `fit`, `predict`, and `__str__`; evaluations score prediction and agent interpretability.
- **Interpretability metric:** Uses 200 LLM-graded tests over feature attribution, point simulation, sensitivity, counterfactual reasoning, structural understanding, and complex function simulation. Development and held-out test splits are used to detect overfitting and reward hacking.
- **Autoresearch loop:** A coding agent edits `interpretable_regressor.py`, runs evaluations, records metrics and candidate model ideas in a CSV memory, then continues for 50-200 iterations unless stopped.
- **Experimental setup:** Evaluates 65 development regression datasets plus 16 held-out OpenML datasets, compares against 16 baseline models across five families, and uses Claude Code and Codex runs at multiple reasoning-effort settings.
- **Main results:** 467 evolved models across 9 runs push the interpretability-performance Pareto frontier beyond baselines; some runs show reward hacking on development interpretability tests, but many generalize to held-out tests.
- **End-to-end ADS results:** Equipping agents with the curated 10-model Agentic-imodels package improves BLADE results for Copilot CLI, Claude Code, and Codex.
- **Discussion:** Argues for agent-centered interpretability as a design target for future data-science tools while noting judge bias, imperfect metrics, reward hacking, and LLM cost as limitations.

## Key paper claims and results

- Agentic data-science tools should be optimized for interpretability by agents, not only by humans.
- A model representation can be evaluated by whether an LLM can simulate predictions, feature effects, sensitivities, and counterfactuals from the model's `__str__` output alone.
- Agentic-imodels searches over model implementations using coding agents such as Claude Code and Codex.
- The loop evaluates two objectives: predictive performance and LLM-graded agent interpretability.
- The experiments use 65 development tabular regression datasets, 16 held-out OpenML datasets, 200 interpretability tests, and 16 baseline model families/variants.
- The authors report 467 evolved models from 9 Agentic-imodels runs.
- Example evolved models include `HingeEBM`, `TeacherStudentRuleSpline`, `SparseSignedBasisPursuit`, and `SmartAdditive` variants.
- Reported BLADE end-to-end gains from adding the evolved package:
  - Copilot CLI with Gemini 2.5 Pro: +72.5%, 13/13 datasets improved.
  - Copilot CLI with Sonnet 4.5: +47.0%, 13/13 improved.
  - Claude Code with Sonnet 4.6: +32.3%, 13/13 improved.
  - Codex with GPT-5.3: +7.9%, 13/13 improved.
- Explicitly emphasizing existing `imodels` or `interpretML` packages did not explain the same gains in the reported controls.

## Limitations noted by the paper

- End-to-end ADS scoring relies on LLM-as-judge, which may introduce bias or artifacts.
- The interpretability metric is also LLM-graded, and may not measure human interpretability.
- Reward hacking appears in some evolved models that overfit development interpretability tests.
- The interpretability tests do not cover every application-specific aspect of interpretability.
- The agentic loop is expensive in coding-agent and evaluator LLM calls.

## Why it matters here

For this wiki, the paper is a concrete example of **agent-facing tool design**. It treats a tool's printed representation as an interface meant for another agent to reason over, then evaluates that interface with held-out tests and downstream agent benchmarks. That is directly relevant to harness engineering: if future agents consume tools, model objects, traces, and diagnostics, those artifacts should be designed for agent simulation and verification rather than for human screenshots alone.
