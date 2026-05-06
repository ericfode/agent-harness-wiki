---
title: Context Engineering
created: 2026-04-07
updated: 2026-05-06
type: concept
tags: [context-engineering, memory, error-recovery]
sources: [raw/articles/openai-harness-engineering.md, raw/articles/anthropic-effective-harnesses.md, raw/articles/anthropic-harness-design-long-running-apps.md, raw/articles/anthropic-claude-code-memory.md, raw/articles/openai-introducing-codex-app.md, raw/articles/0xsero-self-distillation-video-2026-05-02.md, raw/papers/arxiv-singh-2026-agentic-imodels.md]
---

# Context Engineering

## Definition
Context engineering is the management of what the agent sees now, what it can recover later, and what must be written down so the future self does not improvise fiction. It includes prompt assembly, compaction, resets, progressive disclosure, and explicit handoff artifacts.

## Failure modes
The Anthropic papers are useful because they name the pathologies plainly: one-shot overreach, premature completion, and context anxiety. OpenAI's account adds another constraint: if important knowledge lives outside the repo, the agent effectively cannot see it.

## Working techniques
- Progressive disclosure through `AGENTS.md` and linked documents.
- Scoped instruction files such as `CLAUDE.md`, plus auto memory that carries recoverable learnings forward without pretending the full transcript should stay loaded forever.
- Durable instruction hierarchies so repo guidance, user preferences, and managed policy do not collapse into one mutable blob; see [[instruction-layering]].
- Fresh-session resets when long transcripts become liabilities.
- Structured state files such as feature lists and progress logs.
- Tool-assisted re-orientation at session start: run the environment, inspect logs, confirm the app still works.
- Surface handoff and resume flows so work can move between terminal, app, IDE, or web without losing the durable artifacts.
- Bounded turns and explicit sprint contracts.

## Why it matters
Many harness failures are context failures wearing other hats. A bad plan may be a memory problem; a false success may be an evaluation problem caused by insufficient state; a messy codebase may be a documentation visibility problem. An unattended job with weak bootstrap context is the same problem in slower motion, which is why context engineering also sits underneath [[automation-and-background-work]].

## Compressing context into behavior
[[on-policy-self-distillation]] can be read as a bridge out of pure context engineering. In-context learning lets a model use examples, feedback, and instructions transiently; self-distillation asks whether that temporary adaptation can be compressed into durable weights or adapters. The price is governance: once context becomes parameter change, the harness needs evaluation gates, scope boundaries, and rollback rather than simply better prompt assembly.

## Agent-facing representations
[[agentic-imodels]] adds a more immediate version of the same pressure: some artifacts should be shaped for agent simulation, not only human reading. Its `__str__`-based interpretability tests ask whether an LLM can answer operational questions from a model's printed representation alone. That is a useful standard for tool outputs, failure reports, state snapshots, and model summaries in a long-running harness.

## Related pages
Read with [[instruction-layering]], [[memory-persistence]], [[harness-engineering]], [[on-policy-self-distillation]], and [[claude-code]]. For operator-facing visibility into assembled context, provenance, and influence, also read [[context-assembly-visualization-for-harnesses]] and [[attention-and-attribution-views-for-llm-harnesses]]. It also supplies much of the explanatory vocabulary for [[harness-quality-comparison]].

