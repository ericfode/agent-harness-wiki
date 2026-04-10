---
title: "RL Gyms and Executable Environments for AI Harnesses"
created: 2026-04-09
updated: 2026-04-09
type: query
tags: [survey, benchmark, tool-execution, work-management]
sources: [raw/articles/hermes-agent-github.md, raw/articles/newstack-openclaw-vs-hermes.md, raw/papers/arxiv-zhou-2023-webarena.md, raw/papers/arxiv-chezelles-2024-browsergym-ecosystem.md, raw/papers/arxiv-koh-2024-visualwebarena.md, raw/papers/arxiv-drouin-2024-workarena.md, raw/papers/arxiv-boisvert-2024-workarena-plus-plus.md, raw/papers/arxiv-pan-2024-webcanvas.md, raw/papers/arxiv-xie-2024-osworld.md, raw/papers/arxiv-bonatti-2024-windows-agent-arena.md, raw/papers/arxiv-trivedi-2024-appworld.md, raw/papers/arxiv-ma-2024-agentboard.md, raw/papers/arxiv-xi-2024-agentgym.md, raw/papers/arxiv-nathani-2025-mlgym.md, raw/papers/arxiv-pan-2024-swe-gym.md, raw/papers/arxiv-yao-2024-tau-bench.md, raw/papers/arxiv-chuang-2026-proxy-state-based-evaluation.md, raw/papers/arxiv-chen-2025-rl-long-horizon-interactive-llm-agents.md, raw/papers/arxiv-lai-2025-computerrl.md, raw/papers/arxiv-mehta-2026-enterprisebench-corecraft.md, raw/papers/arxiv-mialon-2023-gaia.md, raw/papers/arxiv-yao-2022-webshop.md]
---

# RL Gyms and Executable Environments for AI Harnesses

## Question
If self-evolving workflows need evidence, where do the evidence-producing environments come from? In other words: what are the RL gyms, executable benchmarks, and trainable substrates for agent harnesses rather than just static prompt evaluations?

## Short answer
Yes, there is now a serious and growing layer of gym-like environments for agent harnesses. But the phrase “RL gym” hides several distinct species:
1. **Unified environment APIs** such as BrowserGym, AgentGym, and MLGym.
2. **Executable benchmark worlds** such as WebArena, OSWorld, AppWorld, WorkArena, Windows Agent Arena, and τ-bench.
3. **Training-grade RL substrates** such as AppWorld+LOOP, ComputerRL, EnterpriseBench Corecraft, and SWE-Gym.
4. **Analytical or broad assistant evaluation boards** such as AgentBoard and GAIA, which matter but are not quite gyms in the strict sense.

The key design lesson is that harness engineering is acquiring its own empirical substrate. One no longer needs to argue only from anecdotes, demos, or screenshots of an agent behaving itself once by accident.

## The main families

### 1. Browser and web gyms
These are the clearest descendants of classic RL environments, except the actions are clicks, typed text, DOM interactions, or higher-level browser operations.

- **WebArena** provides realistic multi-domain websites and long-horizon web tasks.
- **VisualWebArena** adds the visual layer required for multimodal web agents.
- **WorkArena** and **WorkArena++** focus on enterprise knowledge-work tasks and planning-heavy workflows.
- **WebCanvas** makes web evaluation online and maintainable under site drift.
- **BrowserGym** unifies several of these benchmarks under a common gym-like interface.
- **WebShop** remains an important precursor: simpler than a full browser stack, but already structured enough to support RL and imitation-learning baselines.

If the question is “what is the browser equivalent of a real agent gym?”, BrowserGym is probably the cleanest current answer.

### 2. Computer-use and operating-system environments
These environments move beyond the browser into desktop workflows, filesystems, and multi-application tasks.

- **OSWorld** is the central benchmark here: real computer environments, cross-OS support, execution-based evaluation, and open-ended tasks.
- **Windows Agent Arena** narrows the same idea to Windows and emphasizes scalable parallel evaluation.
- **ComputerRL** pushes from benchmark into large-scale RL training infrastructure, including distributed virtual desktops and mixed API/GUI interaction.

This family is especially important for harnesses that aspire to be actual digital workers rather than glorified autocomplete with a browser tab.

### 3. Tool/API and workflow worlds
These environments are closer to harness evaluation in the narrow sense, because they test stateful tool use, policies, and workflows rather than only perception and navigation.

- **AppWorld** is the standout example: many apps, many APIs, rich code generation, and state-based unit-test evaluation.
- **τ-bench** evaluates tool-agent-user interaction under domain-specific rules and dynamic conversation.
- **Proxy State-Based Evaluation** extends this line by replacing fully deterministic backends with scalable structured proxy-state judging.
- **SOPBench** from the previous pass belongs here too: it turns procedure-following into executable evaluation rather than vague prose grading.

For agent harnesses specifically, this family is often more relevant than pure web navigation because it tests policy adherence, tool correctness, and collateral damage.

### 4. Software-engineering and research-agent gyms
These are the most directly relevant if the harness is meant to do coding or research rather than general assistant tasks.

- **SWE-Gym** provides executable codebases, tests, and natural-language bug-fix tasks for training both agents and verifiers.
- **MLGym** is the first explicit gym for AI-research agents, with open-ended ML tasks that support RL experimentation.
- **EnterpriseBench Corecraft** is a high-fidelity enterprise RL environment with rubric-based rewards and transfer claims.
- **Reinforcement Learning for Long-Horizon Interactive LLM Agents** shows direct RL in AppWorld, which is one of the best current demonstrations that these environments are not only for evaluation.

This is the family I would watch most closely for harnesses intended to improve coding and research performance over time.

### 5. Cross-environment suites and analytical boards
These are not always gyms in the strict OpenAI-Gym sense, but they matter because they compare or analyze agent behavior across many tasks.

- **AgentBoard** is an analytical evaluation board for multi-turn agents with progress metrics.
- **GAIA** is a broad assistant benchmark requiring reasoning, browsing, multimodality, and tool use.
- **AgentGym** also belongs partly here, since it spans multiple environments and packages trajectories plus evolution methods.

These are useful when the question is “how good is the harness overall?” rather than “what policy should we train in one world?”

## What a good harness gym actually needs
A serious gym substrate for AI harnesses should provide most of the following:
- resettable tasks and initial states
- stable action and observation semantics
- state-based or otherwise verifiable reward
- trajectory capture for later analysis or training
- enough realism that the learned behavior transfers beyond the benchmark
- enough control that one can reproduce failures instead of worshipping them
- scalable parallel execution, because otherwise training becomes an expensive form of nostalgia

This is why AppWorld, OSWorld, BrowserGym, SWE-Gym, and Corecraft feel more substantial than many early “agent benchmarks.” They supply not just tasks, but a world model plus an adjudication model.

## Why this matters for self-evolving workflows
Self-evolving workflows need evaluator loops, and evaluator loops need environments. The gym layer is therefore not separate from [[self-evolving-workflows]]; it is the empirical substrate underneath them.

A system like [[gas-city-but-its-just-codex]] already has a file-backed benchmark harness, but it is still closer to an operator test ladder than to a full RL gym. The literature suggests a plausible progression:
1. benchmark fixtures with structured scorecards
2. richer resettable environments and more varied domains
3. explicit state-based or proxy-state reward
4. trajectory export and judge diagnostics
5. scalable parallel rollouts
6. policy or workflow-family optimization against those environments

That is the road from “repo benchmark” to “actual training substrate.”

## Where Hermes fits
The current wiki only has a thin signal here, but it is suggestive: the Hermes repository notes mention batch trajectory generation and RL environments via **Atropos**, and the comparison article notes a self-training loop that fine-tunes cheaper models from successful trajectories. That is not yet enough to make a dedicated Atropos page without more source material, but it does confirm that Hermes also points toward this gym-and-trajectory direction.

## Best immediate references by use case
- **Need a browser gym:** the BrowserGym ecosystem paper is the current anchor, with WebArena and WorkArena as surrounding benchmarks.
- **Need general computer-use evaluation:** OSWorld.
- **Need a tool/API workflow world:** AppWorld and τ-bench.
- **Need a coding gym:** SWE-Gym.
- **Need an AI-research gym:** MLGym.
- **Need scalable enterprise RL:** EnterpriseBench Corecraft.
- **Need a scalable judge instead of a deterministic backend:** Proxy State-Based Evaluation.

## Bottom line
Yes — the RL-gym story for AI harnesses is now real enough to matter architecturally. The field is converging on executable worlds, state-based grading, trajectory capture, and increasingly trainable substrates. For harness design, the important question is no longer whether such environments exist, but which family of environments best matches the kind of competence the harness is supposed to accumulate.

## Related pages
Read this with [[self-evolving-workflows]], [[evaluation-and-review-loops]], [[harness-engineering]], [[work-management-primitives]], and [[gas-city-but-its-just-codex]]. It is also a natural companion to [[arxiv-self-evolving-workflows-for-codex-control-plane]].