---
title: "ArXiv: Self-Evolving Workflows for Codex Control Planes"
created: 2026-04-09
updated: 2026-04-09
type: query
tags: [survey, comparison, work-management, memory]
sources: [raw/articles/gas-city-but-its-just-codex-repo-2026-04-09.md, raw/papers/arxiv-zhang-2024-aflow.md, raw/papers/arxiv-li-2024-autoflow.md, raw/papers/arxiv-qiao-2024-benchmarking-agentic-workflow-generation.md, raw/papers/arxiv-zheng-2025-mermaidflow.md, raw/papers/arxiv-wang-2026-query-level-workflows.md, raw/papers/arxiv-ma-2026-judgeflow.md, raw/papers/arxiv-wang-2025-dyflow.md, raw/papers/arxiv-xu-2025-robustflow.md, raw/papers/arxiv-wang-2024-agent-workflow-memory.md, raw/papers/arxiv-rhodes-2026-compiled-memory.md, raw/papers/arxiv-shinn-2023-reflexion.md, raw/papers/arxiv-zhao-2023-expel.md, raw/papers/arxiv-zhou-2026-memento-skills.md, raw/papers/arxiv-shen-2026-skillfoundry.md, raw/papers/arxiv-zhang-2026-evoskills.md, raw/papers/arxiv-wang-2026-skillx.md, raw/papers/arxiv-wang-2025-self-improving-agent-skill-library.md, raw/papers/arxiv-liu-2026-graph-of-skills.md, raw/papers/arxiv-ni-2026-trace2skill.md, raw/papers/arxiv-zhang-2026-memskill.md, raw/papers/arxiv-huo-2026-atommem.md, raw/papers/arxiv-ye-2026-meta-context-engineering.md, raw/papers/arxiv-du-2025-bottom-up-skill-evolution.md, raw/papers/arxiv-qian-2025-metaagent.md, raw/papers/arxiv-xia-2026-metaclaw.md, raw/papers/arxiv-ma-2026-scaling-coding-agents-via-atomic-skills.md, raw/papers/arxiv-ye-2025-sop-agent.md, raw/papers/arxiv-li-2025-sopbench.md, raw/papers/arxiv-banerjee-2026-severa.md]
---

# ArXiv: Self-Evolving Workflows for Codex Control Planes

## Goal
Look at what `~/src/gas-city-but-its-just-codex` is already doing, then ask what arXiv work is actually relevant to implementing self-evolving workflows rather than merely talking about agents in the abstract.

## What the repo already has
The repository is no longer at the toy “JSON task list plus a few tools” stage. It already has a durable `redb` workflow ledger, a formula layer with lineage and evolution policy, top-level MCP surfaces for formula mutation and selection, matching in-turn worker tools, benchmark fixtures, and frontier evidence that isolates autonomy debt from graph-shape correctness. In other words, [[gas-city-but-its-just-codex]] already has editable workflow artifacts.

The missing piece is the closed evaluator-and-promotion loop. The repo can mutate formulas and record assessments, but the current benchmark stack does not yet appear to feed benchmark outcomes back into a durable `formula_assess` plus `formula_select` cycle that safely promotes winners. This is exactly the distinction between editable workflows and [[self-evolving-workflows]].

## What I missed on the first pass
The first pass found the direct headline papers, but the broader sweep shows the field is already splitting into several subliteratures:
- workflow search and generation
- workflow evaluation, diagnosis, and robustness
- workflow memory and instruction compilation
- skill-library evolution and retrieval
- learnable memory/context pipelines
- broader continual self-evolving agent systems

That split matters because the repo's bottleneck now sits at the boundary between workflow search and workflow evaluation, with skill evolution as the likely adjacent layer.

## Literature map

### 1. Workflow generation and topology search
These papers treat workflows themselves as explicit search objects.

- **AutoFlow** — automatic generation of natural-language workflows for LLM agents.
- **AFlow** — search over code-represented workflows with execution feedback and MCTS.
- **MermaidFlow** — safety-constrained evolutionary search over statically structured workflow graphs.
- **DyFlow** — dynamic workflow generation and revision from intermediate feedback.
- **Learning to Compose for Cross-domain Agentic Workflow Generation** — learns reusable workflow capabilities for cheaper cross-domain composition.
- **Do We Always Need Query-Level Workflows?** — useful caution that online per-query generation is not always worth its cost.

For the current repo, AFlow, MermaidFlow, DyFlow, and the query-level caution paper are the most operationally useful. They jointly suggest that workflow search needs explicit structure, bounded search cost, and a decision about when not to regenerate the world.

### 2. Workflow evaluation, diagnosis, and robustness
These papers are unusually relevant because they answer the question the repo is now actually facing: how does evidence drive promotion?

- **Benchmarking Agentic Workflow Generation** — gives graph-aware workflow evaluation rather than only end-task scores.
- **JudgeFlow** — assigns block-level responsibility and directs targeted workflow repair.
- **RobustFlow** — measures and trains for workflow invariance under paraphrase and noisy instruction variants.
- **SOPBench** — builds executable SOP graphs and rule-based verifiers for procedure-following agents.

This is the cluster I would borrow most aggressively for `gas-city-but-its-just-codex`. The mutation substrate already exists. The missing move is benchmark-to-score-to-promotion plumbing, and these papers are the closest thing to a syllabus for that problem.

### 3. Workflow memory and instruction compilation
These papers study how experience becomes a reusable procedure rather than just more retrieved text.

- **Agent Workflow Memory** — induces workflows from prior trajectories and recalls them later.
- **Compiled Memory** — rewrites instructions from accumulated experience instead of merely retrieving more facts.
- **Reflexion** — foundational verbal-reflection memory loop.
- **ExpeL** — extracts reusable experiential lessons from prior tasks.
- **AtomMem** — makes memory management itself a learnable workflow over atomic operations.

This cluster helps with a design decision the repo has not yet fully made: which lessons should become formula topology, which should become reusable skills, and which should become instruction rewrites or memory-control policies.

### 4. Skill libraries as the writable learning substrate
This cluster is now large enough to be treated as a distinct architectural family.

- **[[memento-skills]]** — strongest direct statement of external skill memory as the learning substrate.
- **SkillFoundry** — mines and validates skills from heterogeneous domain resources.
- **EvoSkills** — adds the crucial co-evolving verifier for skill generation.
- **SkillX** — builds hierarchical skill knowledge bases from trajectories.
- **Reinforcement Learning for Self-Improving Agent with Skill Library** — RL-based skill accumulation and use.
- **Trace2Skill** — consolidates trajectory-local lessons into unified transferable skills.
- **Graph of Skills** — retrieves bounded dependency-aware skill bundles from very large libraries.
- **MemSkill** — turns memory procedures into evolvable skills.

If the repo keeps formulas as the orchestration-shape layer, this skill-library literature is the most plausible place to put reusable execution techniques. That division of labor feels considerably cleaner than cramming every learned behavior into the formula graph.

### 5. Context evolution and broader self-evolving agents
These papers widen the picture beyond graph mutation.

- **Meta Context Engineering via Agentic Skill Evolution** — co-evolves context-engineering skills and context artifacts.
- **MetaAgent** — tool meta-learning with persistent knowledge accumulation.
- **MetaClaw** — continual platform-scale evolution through skill synthesis plus opportunistic policy optimization.
- **AgentEvolver** — broader self-evolving agent system with self-questioning and self-attribution.
- **SEVerA** — verified synthesis of self-evolving agents under hard formal constraints.

This cluster matters because it shows that “self-evolving workflows” is not the whole game. The system may want formulas, skills, memory policies, and context-engineering routines all to be evolvable — but under different evidence and promotion rules.

### 6. Architectural counter-pressure: skills versus workflows
A few papers explicitly resist the assumption that top-down workflow design is the final substrate.

- **Rethinking Agent Design: From Top-Down Workflows to Bottom-Up Skill Evolution** — argues that bottom-up skill formation may be the more natural long-term architecture.
- **Scaling Coding Agents via Atomic Skills** — suggests coding-agent progress may come from reusable skill atoms beneath composite workflows.
- **SOP-Agent** — externalizes operating procedures as graph-like SOPs, useful as a bridge object between human-authored procedure and learned workflow.

This is a healthy warning. The repo should probably evolve formulas, but it should not assume formulas are the only place intelligence can accumulate.

## Best papers for the repo right now
If I had to choose a short reading queue for `gas-city-but-its-just-codex`, it would be:
1. **JudgeFlow** — because block-level diagnosis is exactly the missing evaluator lane.
2. **Benchmarking Agentic Workflow Generation** — because benchmark structure will likely determine what promotion means.
3. **AFlow** — because it is the cleanest direct workflow-search reference.
4. **RobustFlow** — because workflow churn under paraphrase is a real production problem, not a decorative one.
5. **Agent Workflow Memory** — because some repeated frontier lessons may belong in reusable routines, not graph edits.
6. **EvoSkills** — because verifier-driven skill evolution is the nearest analog to what the repo should do for formulas.
7. **SkillFoundry** — because the repo will likely want a skill layer next to formulas.
8. **Meta Context Engineering** — because some improvements should land in context policy instead of graph structure.
9. **Graph of Skills** — because retrieval becomes structural once the learned library grows large.
10. **SEVerA** — because safety and correctness cannot remain an afterthought forever, even if the repo is not yet ready for full formal guarding.

## Concrete implementation ladder for `gas-city-but-its-just-codex`
1. Define a benchmark-to-metrics contract that maps verifier outcomes, intervention counts, cost, latency, and robustness into structured formula-evaluation metrics.
2. Run candidate formula variants against the existing benchmark ladder, especially the frontier fixtures that already expose autonomy debt.
3. Add a judge surface that summarizes why a candidate failed: wrong artifact schema, bad routing choice, unnecessary operator intervention, weak decomposition, or paraphrase brittleness.
4. Persist those scores and failure annotations through the existing `formula_assess` path.
5. Promote winners only through family selection policy, keeping rollback and lineage intact.
6. Split evolution into two layers: formula families for orchestration shape, and skill packages or atomic skills for reusable execution technique.
7. Decide explicitly which lessons should instead land in instruction or context artifacts, using the workflow-memory and compiled-memory literature as the reference class.

## Bottom line
The literature says the repo is asking the right question, but the answer is wider than “workflow generation.” The next serious move is to connect benchmark evidence, judge diagnostics, and promotion policy into one closed loop. After that, the likely follow-on move is to add a skill layer beside formulas, because the field increasingly treats reusable skills, memory routines, and context policies as the real accumulation surfaces for long-lived agents.

## Related pages
This note sharpens [[gas-city-but-its-just-codex]] through the lens of [[self-evolving-workflows]], [[memento-skills]], [[memory-persistence]], and [[work-management-primitives]]. It also complements [[new-harness-design-notes]] and the system table in [[harness-architecture-comparison]].