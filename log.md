# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

## [2026-04-07] create | Wiki initialized
- Domain: Agent harnesses — software infrastructure for reliable autonomous coding agents
- Focus: Codex CLI, Claude Code, Hermes Agent, Gas Town/Gas City, and architectural patterns
- Structure created with SCHEMA.md, index.md, log.md, raw/, entities/, concepts/, comparisons/, queries/

## [2026-04-07] ingest | Bulk ingestion: 15 sources
- Sources:
  - raw/articles/yegge-welcome-to-gas-town.md
  - raw/articles/yegge-future-of-coding-agents.md
  - raw/articles/yegge-gas-town-clown-show-to-v1.md
  - raw/articles/yegge-birthday-blog.md
  - raw/articles/yegge-welcome-to-the-wasteland.md
  - raw/articles/yegge-vibe-maintainer.md
  - raw/articles/openai-unlocking-codex-harness.md
  - raw/articles/openai-harness-engineering.md
  - raw/articles/anthropic-effective-harnesses.md
  - raw/articles/anthropic-three-agent-harness-infoq.md
  - raw/articles/daily-dose-anatomy-agent-harness.md
  - raw/articles/philschmid-agent-harness-2026.md
  - raw/articles/gupta-2026-is-agent-harnesses.md
  - raw/articles/orami-top-ai-agents-2026.md
  - raw/articles/newstack-openclaw-vs-hermes.md
  - raw/articles/calv-coding-agents-feb-2026.md
  - raw/articles/hn-gas-town-decoded.md
  - raw/articles/prius-of-gastown.md
  - raw/articles/codex-cli-github.md
  - raw/articles/hermes-agent-github.md
- Pages created: 12 (6 entities, 5 concepts, 2 comparisons, 1 query)

## [2026-04-07] update | Wiki recovery after Codex-assisted audit
- Spawned parallel Codex collaborators to audit on-disk state, recover a minimal canonical source set, and propose the missing page set.
- Verified the wiki had become partially ingested: index/log referenced pages and sources that did not yet exist on disk.
- Restored 8 missing raw source summaries:
  - raw/articles/openai-unlocking-codex-harness.md
  - raw/articles/openai-harness-engineering.md
  - raw/articles/anthropic-effective-harnesses.md
  - raw/articles/anthropic-harness-design-long-running-apps.md
  - raw/articles/anthropic-three-agent-harness-infoq.md
  - raw/articles/codex-cli-github.md
  - raw/articles/hermes-agent-github.md
  - raw/articles/newstack-openclaw-vs-hermes.md
- Created 14 content pages:
  - entities/codex-cli.md
  - entities/claude-code.md
  - entities/hermes-agent.md
  - entities/gas-town.md
  - entities/gas-city.md
  - entities/openclaw.md
  - concepts/agent-harness-anatomy.md
  - concepts/harness-engineering.md
  - concepts/context-engineering.md
  - concepts/memory-persistence.md
  - concepts/work-management-primitives.md
  - comparisons/harness-quality-comparison.md
  - comparisons/harness-architecture-comparison.md
  - queries/new-harness-design-notes.md
- Repaired SCHEMA.md so content-page rules and meta-file exceptions are explicit, and added `meta` / `schema` tags to the taxonomy.
- Rebuilt index.md to match the actual on-disk page set: 14 pages.
- Note: the earlier bulk-ingestion entry reflects intended scope at the time and does not exactly match the previously materialized on-disk state; this recovery entry records the repaired truth.

## [2026-04-07] create | safety-and-permissions
- Added concepts/safety-and-permissions.md to normalize a central theme already present across Codex, Hermes, and OpenClaw sources.
- Cross-linked the new concept from entities/codex-cli.md, entities/hermes-agent.md, entities/openclaw.md, and concepts/agent-harness-anatomy.md.
- Updated index.md to include the new concept and bump total pages from 14 to 15.

## [2026-04-07] create | evaluation-and-review-loops
- Added concepts/evaluation-and-review-loops.md to capture evaluator agents, self-review loops, and PR-governance patterns across OpenAI, Anthropic, and Yegge sources.
- Cross-linked the new concept from entities/claude-code.md, concepts/harness-engineering.md, and comparisons/harness-quality-comparison.md.
- Updated index.md to include the new concept and bump total pages from 15 to 16.
