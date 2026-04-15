---
title: Wiki Schema
created: 2026-04-07
updated: 2026-04-14
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
- `log.md` should also use native Obsidian `[[wikilinks]]` for any internal page or source reference; when the precise repo path matters, use an alias such as `[[codex-cli|entities/codex-cli.md]]`
- When updating a page, always bump the `updated` date
- Every new content page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`
- Run `scripts/lint-wiki.sh` after structural edits or before committing wiki changes

## Frontmatter

```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query
tags: [from taxonomy below]
sources: [raw/articles/source-name.md]
formal:   # optional except for harness entity pages used by the Lean extractor
  harness_id: codex_cli
  session_model: thread_turn_item
  memory_model: repo_artifacts
  work_model: plans
  evaluation_model: repo_checks
  surface_model: cli_ide_web_protocol
  topology: single_session
  work_primitives: [plan]
  surfaces: [cli]
  durable_stores: [repo_artifacts]
  evaluation_primitives: [repo_check]
  coordination_roles: [generator, reviewer]
  explicit_protocol_boundary: true
  fresh_session_resets: false
  skill_learning: false
  observability_hooks: true
---
```

## Formal extraction block

The `formal:` block exists so the harness wiki can act as an actual typed source for the Lean formalization instead of forcing semantics back into prose notes.

Rules:
- It is currently required for the harness entity pages that feed the repo extractor:
  - `entities/codex-cli.md`
  - `entities/claude-code.md`
  - `entities/hermes-agent.md`
  - `entities/gas-town.md`
  - `entities/gas-city.md`
  - `entities/openclaw.md`
- It should use stable snake_case enum values.
- Every list value must use inline YAML list syntax, e.g. `[cli, ide, web]`.
- Prose may elaborate on the formal facts, but the extractor does not infer semantics from prose.
- If a new enum value is needed, update this schema and the repo extractor before using it.

Current enum domains used by the extractor:
- `harness_id`: `claude_code`, `codex_cli`, `gas_town`, `gas_city`, `hermes_agent`, `openclaw`
- `session_model`: `thread_turn_item`, `fresh_session_handoff`, `persistent_conversation`, `swarm_sessions`, `service_runtime`
- `memory_model`: `transcript_only`, `repo_artifacts`, `searchable_personal_memory`, `git_beads`, `service_state`
- `work_model`: `none`, `plans`, `sprint_contracts`, `tasks_skills_cron`, `bead_graph`, `ecosystem_skills`
- `evaluation_model`: `self_review_only`, `repo_checks`, `tool_verification`, `separate_evaluator`, `federated_oversight`
- `surface_model`: `cli_only`, `coding_surface`, `cli_ide_web_protocol`, `cli_gateway_mcp`, `orchestrator_factory`, `multi_channel_service`
- `topology`: `single_session`, `session_team`, `factory_swarm`, `federated_exchange`, `service_hub`
- `work_primitives`: `plan`, `feature_list`, `progress_log`, `sprint_contract`, `task`, `skill`, `cron_job`, `automation`, `bead`, `epic`, `molecule`, `protomolecule`, `formula`, `wisp`, `wanted_board`, `ecosystem_skill`
- `surfaces`: `cli`, `terminal`, `ide`, `browser`, `desktop`, `web`, `app`, `cloud`, `sdk`, `slack`, `messaging`, `mcp`, `http_api`, `tmux`
- `durable_stores`: `transcript`, `repo_artifacts`, `shared_client_state`, `searchable_memory`, `git`, `dolt`, `service_workspace`, `workspace_files`, `session_database`
- `evaluation_primitives`: `self_review`, `repo_check`, `tool_observation`, `separate_evaluator`, `ci_review`, `browser_evaluation`, `validator_role`, `federated_trust`
- `coordination_roles`: `planner`, `generator`, `evaluator`, `reviewer`, `orchestrator`, `mayor`, `polecat`, `sheriff`, `witness`, `deacon`, `validator`, `scheduler`, `memory_manager`

`sources` should name the immediate inputs for the page. Usually these are files under `raw/`; synthesis or design pages may instead cite existing wiki pages when those pages are the direct source material.

## Tag Taxonomy

### Implementations
- `codex-cli` — OpenAI Codex CLI / harness
- `mathcode` — MathCode mathematical coding agent with Lean formalization and proof search
- `claude-code` — Anthropic Claude Code
- `hermes-agent` — Nous Research Hermes Agent
- `memento-skills` — Memento-Teams self-evolving skill-memory agent system
- `gas-town` — Steve Yegge's Gas Town orchestrator
- `gas-city` — Gas Town's modular successor
- `openclaw` — OpenClaw persistent agent
- `langchain` — LangChain / LangGraph
- `crewai` — CrewAI multi-agent framework
- `cursor` — Cursor IDE agent
- `dspy` — Declarative Self-improving Python / LM-program compilation and optimization framework

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

### Model internals & synthesis
- `mechanistic-interpretability` — Residual streams, feature discovery, activation interventions, model editing
- `program-synthesis` — Program induction, latent program representations, executable IR design

### Semantics & Formalization
- `formal-methods` — Specifications, verification, proof systems, certified reasoning
- `semantics` — Formal semantics, abstraction layers, interpretation maps
- `epistemics` — Knowledge, belief, uncertainty, update logics
- `concurrency` — Partial orders, event structures, pomsets, scheduling semantics

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
