---
title: "The Last Harness You'll Ever Build"
author: Haebin Seong, Li Yin, Haoran Zhang, Zhan Shi
url: https://arxiv.org/abs/2604.21003v3
pdf: https://arxiv.org/pdf/2604.21003v3
html: https://arxiv.org/html/2604.21003v3
date: 2026-05-01
ingested: 2026-05-06
arxiv_id: 2604.21003v3
primary_category: cs.AI
license: CC BY 4.0
---

# The Last Harness You'll Ever Build

**Source:** [arXiv:2604.21003v3](https://arxiv.org/abs/2604.21003v3)  
**PDF:** <https://arxiv.org/pdf/2604.21003v3>  
**HTML:** <https://arxiv.org/html/2604.21003v3>  
**Authors:** Haebin Seong, Li Yin, Haoran Zhang, Zhan Shi  
**Organization:** Sylph.AI  
**Published:** 2026-04-22  
**Version read:** v3, updated 2026-05-01  
**Primary category:** cs.AI  
**License:** CC BY 4.0

## Retrieval notes

- User supplied an image of the article's first page; the arXiv identifier visible in the image was `2604.21003v3`.
- `web_extract` was unavailable in this Hermes session because Firecrawl was not configured, so the source was grounded through:
  - arXiv Atom API: `https://export.arxiv.org/api/query?id_list=2604.21003v3`
  - arXiv HTML: `https://arxiv.org/html/2604.21003v3`
- The arXiv HTML was fetched successfully on 2026-05-06 and used for section-level extraction.

## Abstract

AI agents are increasingly deployed on complex, domain-specific workflows—navigating enterprise web applications that require dozens of clicks and form fills, orchestrating multi-step research pipelines that span search, extraction, and synthesis, automating code review across unfamiliar repositories, and handling customer escalations that demand nuanced domain knowledge. Each new task domain requires painstaking, expert-driven harness engineering: designing the prompts, tools, orchestration logic, and evaluation criteria that make a foundation model effective. The paper presents a two-level framework that automates this process.

At the first level, the **Harness Evolution Loop** optimizes a worker agent's harness for a single task: a Worker Agent executes the task, an Evaluator Agent adversarially diagnoses failures and scores performance, and an Evolution Agent modifies the harness from the full prior-attempt history. At the second level, the **Meta-Evolution Loop** optimizes the evolution blueprint itself across diverse tasks, learning a blueprint that enables rapid harness convergence on new tasks. The authors frame this as shifting manual harness engineering into automated harness engineering and then automating the design of that automation.

## Extracted structure

- **Section 1:** Motivates the problem: harnesses amplify agents, but current harness construction is expert-driven and domain-specific.
- **Section 2:** Defines the Harness Evolution Loop over a task, worker harness, evaluator, evolution agent, and iteration budget.
- **Section 2.1:** Defines an agent harness as everything around the model: prompts, tools, skills, infrastructure, orchestration logic, hooks, middleware, and model configuration.
- **Sections 2.2-2.5:** Define task instructions/success criteria, worker trace generation, adversarial evaluator reports and scores, and an evolution agent that edits harness code/configuration from history.
- **Section 3:** Treats the harness evolution loop itself as a harness, denoted as an evolution blueprint, and optimizes that blueprint across meta-train tasks.
- **Section 3.2:** Maps the two-level structure to meta-learning: the inner loop adapts a harness for one task, while the outer loop improves the adaptation procedure.
- **Section 3.3:** Proposes generalization metrics: convergence speed, final performance, and robustness across held-out tasks.
- **Section 4:** Concludes with a product-oriented claim: a future system should let users point a general-purpose agent at a new domain and have it evolve into a specialized agent without human harness-engineering expertise.

## Key paper claims

- A raw model is not an agent; the agent is the model plus its harness.
- Harnesses include prompts, tools, skills, bundled infrastructure, orchestration logic, hooks, middleware, and model-routing/configuration.
- Harness improvement should be a closed loop over execution traces, adversarial evaluation, and code/configuration modification.
- The evaluator is not merely a score function; it diagnoses state perception, criterion satisfaction, performance bottlenecks, and regressions.
- The evolution agent should modify the full harness, not merely prompt text.
- The evolution process itself can be treated as a harness and optimized at a meta level across task families.
- The paper is primarily a framework/proposal paper; it explicitly says empirical results and product release are future work.

## References called out by the paper

- OpenAI Harness Engineering, 2026.
- Anthropic Harness Design for Long-Running Application Development, 2026.
- Anthropic Claude Code best practices, 2025.
- LangChain, The Anatomy of an Agent Harness, 2026.
- OpAgent, 2026.
- WebArena, 2024.
- LLM-AutoDiff, 2025.
- Thrun and Pratt, *Learning to Learn*, 1998.
