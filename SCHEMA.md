---
title: Wiki Schema
created: 2026-04-07
updated: 2026-04-07
type: schema
tags: [meta, schema]
---

# Wiki Schema

## Domain

Agent harnesses: the software infrastructure that wraps LLMs to enable reliable, long-running, autonomous coding and general-purpose task execution. Covers specific harness implementations (Codex CLI, Claude Code, Hermes Agent, Gas Town/Gas City), architectural patterns, orchestration strategies, and the engineering discipline of "harness engineering."

## Conventions

- File names: lowercase, hyphens, no spaces (e.g., `gas-town-meow-stack.md`)
- Every content page under `entities/`, `concepts/`, `comparisons/`, and `queries/` starts with YAML frontmatter (see below)
- Top-level meta files (`SCHEMA.md`, `index.md`, `log.md`) may omit `sources` and are exempt from the outbound-wikilink minimum
- Use `[[wikilinks]]` to link between content pages (minimum 2 outbound links per page)
- When updating a page, always bump the `updated` date
- Every new content page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`

## Frontmatter

```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query
tags: [from taxonomy below]
sources: [raw/articles/source-name.md]
---
```

## Tag Taxonomy

### Implementations
- `codex-cli` — OpenAI Codex CLI / harness
- `claude-code` — Anthropic Claude Code
- `hermes-agent` — Nous Research Hermes Agent
- `gas-town` — Steve Yegge's Gas Town orchestrator
- `gas-city` — Gas Town's modular successor
- `openclaw` — OpenClaw persistent agent
- `langchain` — LangChain / LangGraph
- `crewai` — CrewAI multi-agent framework
- `cursor` — Cursor IDE agent

### Architecture & Patterns
- `orchestration` — Multi-agent coordination
- `memory` — Persistent memory / context management
- `tool-execution` — Tool calling, sandboxing, permissions
- `subagents` — Sub-agent delegation patterns
- `work-management` — Task tracking, planning, DAGs
- `context-engineering` — Context window optimization
- `error-recovery` — Error handling, retry, state recovery
- `safety` — Guardrails, permissions, sandboxes

### Evaluation
- `comparison` — Side-by-side analyses
- `benchmark` — Performance measurement
- `code-quality` — Codebase quality analysis

### Meta
- `survey` — Survey / overview articles
- `opinion` — Opinion pieces and predictions
- `tutorial` — How-to guides
- `history` — Historical context and evolution
- `meta` — Wiki-internal metadata or maintenance notes
- `schema` — Schema or taxonomy definitions for the wiki itself

Rule: every tag on a page must appear in this taxonomy. If a new tag is needed, add it here first, then use it.

## Page Thresholds

- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source
- **Add to existing page** when a source mentions something already covered
- **DON'T create a page** for passing mentions, minor details, or things outside the domain
- **Split a page** when it exceeds ~200 lines — break into sub-topics with cross-links
- **Archive a page** when its content is fully superseded — move to `_archive/`, remove from index

## Entity Pages

One page per notable entity. Include:
- Overview / what it is
- Key facts and dates
- Architecture highlights
- Strengths and weaknesses
- Relationships to other entities ([[wikilinks]])
- Source references

## Concept Pages

One page per concept or topic. Include:
- Definition / explanation
- Current state of knowledge
- Open questions or debates
- Related concepts ([[wikilinks]])

## Comparison Pages

Side-by-side analyses. Include:
- What is being compared and why
- Dimensions of comparison (table format preferred)
- Verdict or synthesis
- Sources

## Update Policy

When new information conflicts with existing content:
1. Check the dates — newer sources generally supersede older ones
2. If genuinely contradictory, note both positions with dates and sources
3. Mark the contradiction in frontmatter: `contradictions: [page-name]`
4. Flag for user review in the lint report
