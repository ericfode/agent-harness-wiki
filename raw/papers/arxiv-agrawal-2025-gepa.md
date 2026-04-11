---
title: GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning
author: Lakshya A Agrawal, Shangyin Tan, Dilara Soylu, Noah Ziems, Rishi Khare, Krista Opsahl-Ong, Arnav Singhvi, Herumb Shandilya, Michael J Ryan, Meng Jiang, Christopher Potts, Koushik Sen, Alexandros G. Dimakis, Ion Stoica, Dan Klein, Matei Zaharia, Omar Khattab
url: https://arxiv.org/abs/2507.19457
date: 2025-07-25
ingested: 2026-04-11
---

# GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning

**Source:** [arXiv](https://arxiv.org/abs/2507.19457)
**Authors:** Lakshya A Agrawal, Shangyin Tan, Dilara Soylu, Noah Ziems, Rishi Khare, Krista Opsahl-Ong, Arnav Singhvi, Herumb Shandilya, Michael J Ryan, Meng Jiang, Christopher Potts, Koushik Sen, Alexandros G. Dimakis, Ion Stoica, Dan Klein, Matei Zaharia, Omar Khattab
**Date:** 2025-07-25
**Primary category:** cs.CL
**All categories:** cs.CL, cs.AI, cs.LG, cs.SE

## Abstract / key passage
GEPA argues that prompt and program optimization should learn from full language-rich trajectories rather than mostly from sparse scalar rewards. It samples reasoning and tool-use traces, reflects on failures in natural language, proposes prompt updates, and preserves complementary candidates on a Pareto frontier instead of collapsing search to one global winner. The paper reports stronger results than several RL-style baselines while using many fewer rollouts.

## Harness takeaway
GEPA is interesting for long-lived harnesses because those systems already emit the traces it wants to learn from: reasoning steps, tool calls, outputs, and evaluator feedback. It is therefore best read not as “RL is dead” theater, but as a strong recent case that reflective evolution over durable prompt/program artifacts can be a better fit than scalar-reward RL when rollouts are expensive and traces are rich.