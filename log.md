# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

## [2026-04-07] create | Wiki initialized
- Domain: Agent harnesses — software infrastructure for reliable autonomous coding agents
- Focus: Codex CLI, Claude Code, Hermes Agent, Gas Town/Gas City, and architectural patterns
- Structure created with [[SCHEMA|SCHEMA.md]], [[index|index.md]], [[log|log.md]], raw/, entities/, concepts/, comparisons/, queries/

## [2026-04-07] ingest | Bulk ingestion: 15 sources
- Sources:
  - [[yegge-welcome-to-gas-town|raw/articles/yegge-welcome-to-gas-town.md]]
  - [[yegge-future-of-coding-agents|raw/articles/yegge-future-of-coding-agents.md]]
  - [[yegge-gas-town-clown-show-to-v1|raw/articles/yegge-gas-town-clown-show-to-v1.md]]
  - [[yegge-birthday-blog|raw/articles/yegge-birthday-blog.md]]
  - [[yegge-welcome-to-the-wasteland|raw/articles/yegge-welcome-to-the-wasteland.md]]
  - [[yegge-vibe-maintainer|raw/articles/yegge-vibe-maintainer.md]]
  - [[openai-unlocking-codex-harness|raw/articles/openai-unlocking-codex-harness.md]]
  - [[openai-harness-engineering|raw/articles/openai-harness-engineering.md]]
  - [[anthropic-effective-harnesses|raw/articles/anthropic-effective-harnesses.md]]
  - [[anthropic-three-agent-harness-infoq|raw/articles/anthropic-three-agent-harness-infoq.md]]
  - raw/articles/daily-dose-anatomy-agent-harness.md
  - raw/articles/philschmid-agent-harness-2026.md
  - raw/articles/gupta-2026-is-agent-harnesses.md
  - raw/articles/orami-top-ai-agents-2026.md
  - [[newstack-openclaw-vs-hermes|raw/articles/newstack-openclaw-vs-hermes.md]]
  - raw/articles/calv-coding-agents-feb-2026.md
  - raw/articles/hn-gas-town-decoded.md
  - raw/articles/prius-of-gastown.md
  - [[codex-cli-github|raw/articles/codex-cli-github.md]]
  - [[hermes-agent-github|raw/articles/hermes-agent-github.md]]
- Pages created: 12 (6 entities, 5 concepts, 2 comparisons, 1 query)

## [2026-04-07] update | Wiki recovery after Codex-assisted audit
- Spawned parallel Codex collaborators to audit on-disk state, recover a minimal canonical source set, and propose the missing page set.
- Verified the wiki had become partially ingested: index/log referenced pages and sources that did not yet exist on disk.
- Restored 8 missing raw source summaries:
  - [[openai-unlocking-codex-harness|raw/articles/openai-unlocking-codex-harness.md]]
  - [[openai-harness-engineering|raw/articles/openai-harness-engineering.md]]
  - [[anthropic-effective-harnesses|raw/articles/anthropic-effective-harnesses.md]]
  - [[anthropic-harness-design-long-running-apps|raw/articles/anthropic-harness-design-long-running-apps.md]]
  - [[anthropic-three-agent-harness-infoq|raw/articles/anthropic-three-agent-harness-infoq.md]]
  - [[codex-cli-github|raw/articles/codex-cli-github.md]]
  - [[hermes-agent-github|raw/articles/hermes-agent-github.md]]
  - [[newstack-openclaw-vs-hermes|raw/articles/newstack-openclaw-vs-hermes.md]]
- Created 14 content pages:
  - [[codex-cli|entities/codex-cli.md]]
  - [[claude-code|entities/claude-code.md]]
  - [[hermes-agent|entities/hermes-agent.md]]
  - [[gas-town|entities/gas-town.md]]
  - [[gas-city|entities/gas-city.md]]
  - [[openclaw|entities/openclaw.md]]
  - [[agent-harness-anatomy|concepts/agent-harness-anatomy.md]]
  - [[harness-engineering|concepts/harness-engineering.md]]
  - [[context-engineering|concepts/context-engineering.md]]
  - [[memory-persistence|concepts/memory-persistence.md]]
  - [[work-management-primitives|concepts/work-management-primitives.md]]
  - [[harness-quality-comparison|comparisons/harness-quality-comparison.md]]
  - [[harness-architecture-comparison|comparisons/harness-architecture-comparison.md]]
  - [[new-harness-design-notes|queries/new-harness-design-notes.md]]
- Repaired [[SCHEMA|SCHEMA.md]] so content-page rules and meta-file exceptions are explicit, and added `meta` / `schema` tags to the taxonomy.
- Rebuilt [[index|index.md]] to match the actual on-disk page set: 14 pages.
- Note: the earlier bulk-ingestion entry reflects intended scope at the time and does not exactly match the previously materialized on-disk state; this recovery entry records the repaired truth.

## [2026-04-07] create | safety-and-permissions
- Added [[safety-and-permissions|concepts/safety-and-permissions.md]] to normalize a central theme already present across Codex, Hermes, and OpenClaw sources.
- Cross-linked the new concept from [[codex-cli|entities/codex-cli.md]], [[hermes-agent|entities/hermes-agent.md]], [[openclaw|entities/openclaw.md]], and [[agent-harness-anatomy|concepts/agent-harness-anatomy.md]].
- Updated [[index|index.md]] to include the new concept and bump total pages from 14 to 15.

## [2026-04-07] create | evaluation-and-review-loops
- Added [[evaluation-and-review-loops|concepts/evaluation-and-review-loops.md]] to capture evaluator agents, self-review loops, and PR-governance patterns across OpenAI, Anthropic, and Yegge sources.
- Cross-linked the new concept from [[claude-code|entities/claude-code.md]], [[harness-engineering|concepts/harness-engineering.md]], and [[harness-quality-comparison|comparisons/harness-quality-comparison.md]].
- Updated [[index|index.md]] to include the new concept and bump total pages from 15 to 16.

## [2026-04-07] ingest | Current-source refresh from parallel research agents
- Spawned three parallel research agents to expand the corpus across OpenAI/Codex, Anthropic/Claude Code, and persistent-orchestrator runtimes.
- Added 9 raw source summaries for newly researched primary sources:
  - [[openai-introducing-codex-app|raw/articles/openai-introducing-codex-app.md]]
  - [[openai-codex-app-server-readme|raw/articles/openai-codex-app-server-readme.md]]
  - [[anthropic-claude-code-overview|raw/articles/anthropic-claude-code-overview.md]]
  - [[anthropic-claude-code-memory|raw/articles/anthropic-claude-code-memory.md]]
  - [[anthropic-claude-code-settings|raw/articles/anthropic-claude-code-settings.md]]
  - [[hermes-agent-memory-docs|raw/articles/hermes-agent-memory-docs.md]]
  - [[hermes-agent-api-server-docs|raw/articles/hermes-agent-api-server-docs.md]]
  - [[openclaw-agent-runtime-docs|raw/articles/openclaw-agent-runtime-docs.md]]
  - [[yegge-gas-town-emergency-user-manual|raw/articles/yegge-gas-town-emergency-user-manual.md]]
- Updated major pages to reflect current surface models, memory systems, permissions, and orchestration details:
  - [[codex-cli|entities/codex-cli.md]]
  - [[claude-code|entities/claude-code.md]]
  - [[hermes-agent|entities/hermes-agent.md]]
  - [[openclaw|entities/openclaw.md]]
  - [[gas-town|entities/gas-town.md]]
  - [[gas-city|entities/gas-city.md]]
  - [[agent-harness-anatomy|concepts/agent-harness-anatomy.md]]
  - [[context-engineering|concepts/context-engineering.md]]
  - [[memory-persistence|concepts/memory-persistence.md]]
  - [[safety-and-permissions|concepts/safety-and-permissions.md]]
  - [[evaluation-and-review-loops|concepts/evaluation-and-review-loops.md]]
  - [[harness-architecture-comparison|comparisons/harness-architecture-comparison.md]]
  - [[harness-quality-comparison|comparisons/harness-quality-comparison.md]]

## [2026-04-07] create | codex-app-server
- Added [[codex-app-server|entities/codex-app-server.md]] because the App Server is now central enough in OpenAI's public materials to warrant its own page.
- Updated [[index|index.md]] to include the new entity and bump total pages from 16 to 17.

## [2026-04-07] create | harness-decision-matrix
- Added [[harness-decision-matrix|comparisons/harness-decision-matrix.md]] to turn the current qualitative corpus into a weighted design-choice table.
- Cross-linked the new comparison from [[harness-quality-comparison|comparisons/harness-quality-comparison.md]] and [[new-harness-design-notes|queries/new-harness-design-notes.md]] so it participates in the existing synthesis graph.
- Updated [[index|index.md]] to include the new comparison and bump total pages from 17 to 18.

## [2026-04-07] create | automation-and-background-work
- Added [[automation-and-background-work|concepts/automation-and-background-work.md]] to capture the recurring-work pattern now visible across Codex app automations, Claude Code recurring tasks, and Hermes cron jobs.
- Cross-linked the new concept from [[context-engineering|concepts/context-engineering.md]], [[work-management-primitives|concepts/work-management-primitives.md]], [[safety-and-permissions|concepts/safety-and-permissions.md]], [[codex-cli|entities/codex-cli.md]], [[claude-code|entities/claude-code.md]], and [[hermes-agent|entities/hermes-agent.md]].
- Updated [[index|index.md]] to include the new concept and bump total pages from 18 to 19.

## [2026-04-07] create | instruction-layering
- Added [[instruction-layering|concepts/instruction-layering.md]] to separate durable scoped guidance from transcript memory, using `AGENTS.md`, `CLAUDE.md`, Hermes memory files, and OpenClaw bootstrap files as the main examples.
- Cross-linked the new concept from [[context-engineering|concepts/context-engineering.md]], [[memory-persistence|concepts/memory-persistence.md]], [[safety-and-permissions|concepts/safety-and-permissions.md]], [[codex-cli|entities/codex-cli.md]], [[claude-code|entities/claude-code.md]], [[hermes-agent|entities/hermes-agent.md]], and [[openclaw|entities/openclaw.md]].
- Updated [[index|index.md]] to include the new concept and bump total pages from 19 to 20.

## [2026-04-07] ingest | orchestration and automation docs refresh
- Added 4 raw source summaries for current official docs:
  - [[anthropic-claude-code-subagents|raw/articles/anthropic-claude-code-subagents.md]]
  - [[anthropic-claude-code-agent-teams|raw/articles/anthropic-claude-code-agent-teams.md]]
  - [[anthropic-claude-code-scheduled-tasks|raw/articles/anthropic-claude-code-scheduled-tasks.md]]
  - [[openai-codex-chatgpt-plan|raw/articles/openai-codex-chatgpt-plan.md]]
- Updated synthesis pages to reflect the stronger distinction between subagents, session teams, and background work:
  - [[agent-harness-anatomy|concepts/agent-harness-anatomy.md]]
  - [[automation-and-background-work|concepts/automation-and-background-work.md]]
  - [[claude-code|entities/claude-code.md]]
  - [[harness-architecture-comparison|comparisons/harness-architecture-comparison.md]]
  - [[new-harness-design-notes|queries/new-harness-design-notes.md]]

## [2026-04-07] create | orchestration-topologies
- Added [[orchestration-topologies|concepts/orchestration-topologies.md]] to capture the emerging split between inline subagents, separate-session teams, and full swarm/factory coordination.
- Cross-linked the new concept from [[agent-harness-anatomy|concepts/agent-harness-anatomy.md]], [[automation-and-background-work|concepts/automation-and-background-work.md]], [[claude-code|entities/claude-code.md]], [[harness-architecture-comparison|comparisons/harness-architecture-comparison.md]], and [[new-harness-design-notes|queries/new-harness-design-notes.md]].
- Updated [[index|index.md]] to include the new concept and bump total pages from 21 to 22.

## [2026-04-08] ingest | arXiv round two on formal semantics for agent harnesses
- Added 6 raw paper summaries:
  - [[arxiv-zhang-2024-formal-methods-trustworthy-ai-agents|raw/papers/arxiv-zhang-2024-formal-methods-trustworthy-ai-agents.md]]
  - [[arxiv-lahiri-2026-intent-formalization|raw/papers/arxiv-lahiri-2026-intent-formalization.md]]
  - [[arxiv-conradie-2016-probabilistic-epistemic-updates|raw/papers/arxiv-conradie-2016-probabilistic-epistemic-updates.md]]
  - [[arxiv-kishida-2017-categories-for-dynamic-epistemic-logic|raw/papers/arxiv-kishida-2017-categories-for-dynamic-epistemic-logic.md]]
  - [[arxiv-wang-2026-structural-operational-semantics-true-concurrency|raw/papers/arxiv-wang-2026-structural-operational-semantics-true-concurrency.md]]
  - [[arxiv-edixhoven-2022-branching-pomsets-for-choreographies|raw/papers/arxiv-edixhoven-2022-branching-pomsets-for-choreographies.md]]
- Extended [[SCHEMA|SCHEMA.md]] with new tags for `formal-methods`, `semantics`, `epistemics`, and `concurrency`.
- Created 4 content pages:
  - [[formal-methods-for-agent-harnesses|concepts/formal-methods-for-agent-harnesses.md]]
  - [[probabilistic-epistemic-updates|concepts/probabilistic-epistemic-updates.md]]
  - [[partial-order-trace-semantics|concepts/partial-order-trace-semantics.md]]
  - [[arxiv-round-two-formal-semantics-for-agent-harnesses|queries/arxiv-round-two-formal-semantics-for-agent-harnesses.md]]
- Updated existing synthesis pages to cross-link the new research layer:
  - [[harness-engineering|concepts/harness-engineering.md]]
  - [[agent-harness-anatomy|concepts/agent-harness-anatomy.md]]
  - [[work-management-primitives|concepts/work-management-primitives.md]]
  - [[orchestration-topologies|concepts/orchestration-topologies.md]]
  - [[memory-persistence|concepts/memory-persistence.md]]
- Updated [[index|index.md]] to include the new pages and bump total pages from 22 to 26.

## [2026-04-08] ingest | formal-core cognition research pass
- Added 6 raw paper summaries:
  - [[arxiv-song-2024-lean-copilot|raw/papers/arxiv-song-2024-lean-copilot.md]]
  - [[arxiv-endres-2023-natural-language-to-postconditions|raw/papers/arxiv-endres-2023-natural-language-to-postconditions.md]]
  - [[arxiv-murphy-2024-llm-codegen-formal-spec-reactive-synthesis|raw/papers/arxiv-murphy-2024-llm-codegen-formal-spec-reactive-synthesis.md]]
  - [[arxiv-lin-2024-fvel|raw/papers/arxiv-lin-2024-fvel.md]]
  - [[arxiv-burigana-2026-epddl|raw/papers/arxiv-burigana-2026-epddl.md]]
  - [[arxiv-allen-2025-sound-complete-neurosymbolic-reasoning|raw/papers/arxiv-allen-2025-sound-complete-neurosymbolic-reasoning.md]]
- Created 3 content pages:
  - [[theorem-proving-as-cognitive-kernel|concepts/theorem-proving-as-cognitive-kernel.md]]
  - [[formal-cognition-loop|concepts/formal-cognition-loop.md]]
  - [[formal-core-agent-architecture|queries/formal-core-agent-architecture.md]]
- Updated existing synthesis pages to absorb the new formal-core angle:
  - [[formal-methods-for-agent-harnesses|concepts/formal-methods-for-agent-harnesses.md]]
  - [[new-harness-design-notes|queries/new-harness-design-notes.md]]
- Updated [[index|index.md]] to include the new pages and bump total pages from 26 to 29.

## [2026-04-08] ingest | non-linear harness interface research pass
- Added 9 raw paper summaries:
  - [[arxiv-sarkar-2023-code-relevant-ui|raw/papers/arxiv-sarkar-2023-code-relevant-ui.md]]
  - [[arxiv-angert-2023-spellburst|raw/papers/arxiv-angert-2023-spellburst.md]]
  - [[arxiv-rein-2024-live-programmers|raw/papers/arxiv-rein-2024-live-programmers.md]]
  - [[arxiv-krause-glau-2023-code-proximal-dynamic-software-visualization|raw/papers/arxiv-krause-glau-2023-code-proximal-dynamic-software-visualization.md]]
  - [[arxiv-kuhn-2010-spatial-software-visualization-ide|raw/papers/arxiv-kuhn-2010-spatial-software-visualization-ide.md]]
  - [[arxiv-li-2024-kishu-time-traveling-notebooks|raw/papers/arxiv-li-2024-kishu-time-traveling-notebooks.md]]
  - [[arxiv-fang-2025-code-data-space-versioning|raw/papers/arxiv-fang-2025-code-data-space-versioning.md]]
  - [[arxiv-chen-2022-nl2interface|raw/papers/arxiv-chen-2022-nl2interface.md]]
  - [[arxiv-krause-glau-2024-code-review-software-city|raw/papers/arxiv-krause-glau-2024-code-review-software-city.md]]
- Created 1 content page:
  - [[non-linear-interface-options-for-next-harness|queries/non-linear-interface-options-for-next-harness.md]]
- Updated existing synthesis pages to absorb the new surface/interface angle:
  - [[agent-harness-anatomy|concepts/agent-harness-anatomy.md]]
  - [[harness-engineering|concepts/harness-engineering.md]]
  - [[new-harness-design-notes|queries/new-harness-design-notes.md]]
- Updated [[index|index.md]] to include the new query and bump total pages from 29 to 30.

## [2026-04-08] update | add diagrams to core concept pages
- Added Mermaid diagrams to clarify structure and flow on:
  - [[agent-harness-anatomy|concepts/agent-harness-anatomy.md]]
  - [[work-management-primitives|concepts/work-management-primitives.md]]
  - [[formal-cognition-loop|concepts/formal-cognition-loop.md]]
  - [[orchestration-topologies|concepts/orchestration-topologies.md]]
- Chose diagrams that mirror existing prose rather than introducing new claims: a harness component map, a work-object lifecycle, a formalization loop, and a topology comparison sketch.

## [2026-04-08] lint | wiki grooming pass
- Audited the corpus against the current schema: index coverage, source existence, tag taxonomy, outbound wikilinks, and modified-page `updated` dates.
- Fixed the taxonomy violation in [[gas-city-but-its-just-codex|queries/gas-city-but-its-just-codex.md]] by replacing ad hoc tags with existing schema tags.
- Bumped stale `updated` dates on the already edited comparison, concept, and query pages so frontmatter matches the current worktree.
- Added `scripts/lint-wiki.sh` and documented it in [[SCHEMA|SCHEMA.md]] so future grooming does not depend on chat memory.

## [2026-04-09] ingest | non-hierarchical orchestration research pass
- Added 11 raw paper summaries for non-hierarchical coordination patterns and dolphin-sociality inputs:
  - [[smith-1980-contract-net-protocol|raw/papers/smith-1980-contract-net-protocol.md]]
  - [[gelernter-1985-generative-communication-in-linda|raw/papers/gelernter-1985-generative-communication-in-linda.md]]
  - [[mcmanus-1991-design-and-analysis-tools-for-concurrent-blackboard-systems|raw/papers/mcmanus-1991-design-and-analysis-tools-for-concurrent-blackboard-systems.md]]
  - [[olfati-saber-fax-murray-2007-consensus-and-cooperation-in-networked-multi-agent-systems|raw/papers/olfati-saber-fax-murray-2007-consensus-and-cooperation-in-networked-multi-agent-systems.md]]
  - [[shehory-kraus-1998-methods-for-task-allocation-via-agent-coalition-formation|raw/papers/shehory-kraus-1998-methods-for-task-allocation-via-agent-coalition-formation.md]]
  - [[dias-zlot-kalra-stentz-2006-market-based-multirobot-coordination|raw/papers/dias-zlot-kalra-stentz-2006-market-based-multirobot-coordination.md]]
  - [[brambilla-ferrante-birattari-dorigo-2013-swarm-robotics-review|raw/papers/brambilla-ferrante-birattari-dorigo-2013-swarm-robotics-review.md]]
  - [[lusseau-conradt-2009-unshared-consensus-decisions-dolphins|raw/papers/lusseau-conradt-2009-unshared-consensus-decisions-dolphins.md]]
  - [[bruck-2013-decades-long-social-memory-in-bottlenose-dolphins|raw/papers/bruck-2013-decades-long-social-memory-in-bottlenose-dolphins.md]]
  - [[evans-krzyszczyk-frere-mann-2021-lifetime-stability-of-social-traits-in-bottlenose-dolphins|raw/papers/evans-krzyszczyk-frere-mann-2021-lifetime-stability-of-social-traits-in-bottlenose-dolphins.md]]
  - [[king-connor-kruetzen-allen-2021-cooperation-based-concept-formation-in-male-bottlenose-dolphins|raw/papers/king-connor-kruetzen-allen-2021-cooperation-based-concept-formation-in-male-bottlenose-dolphins.md]]
- Created 3 content pages:
  - [[non-hierarchical-coordination-patterns|concepts/non-hierarchical-coordination-patterns.md]]
  - [[fission-fusion-orchestration|concepts/fission-fusion-orchestration.md]]
  - [[non-hierarchical-agent-orchestration|queries/non-hierarchical-agent-orchestration.md]]
- Updated existing synthesis pages so the new material participates in the main design graph:
  - [[orchestration-topologies|concepts/orchestration-topologies.md]]
  - [[new-harness-design-notes|queries/new-harness-design-notes.md]]
- Updated [[index|index.md]] to include the new pages and bump total pages from 30 to 33.

## [2026-04-09] ingest | Memento-Skills paper and companion code
- Added 2 raw source summaries:
  - [[arxiv-zhou-2026-memento-skills|raw/papers/arxiv-zhou-2026-memento-skills.md]]
  - [[memento-skills-github|raw/articles/memento-skills-github.md]]
- Created 1 content page:
  - [[memento-skills|entities/memento-skills.md]]
- Updated existing synthesis pages so the new system participates in the main graph:
  - [[memory-persistence|concepts/memory-persistence.md]]
  - [[harness-architecture-comparison|comparisons/harness-architecture-comparison.md]]
- Extended [[SCHEMA|SCHEMA.md]] with a `memento-skills` implementation tag.
- Updated [[index|index.md]] to include the new entity and bump total pages from 33 to 34.

## [2026-04-09] ingest | broader web patterns for non-linear harness interfaces
- Added 14 raw source summaries:
  - [[sketch-n-sketch|raw/articles/sketch-n-sketch.md]]
  - [[glamorous-toolkit-moldable-development-environment|raw/articles/glamorous-toolkit-moldable-development-environment.md]]
  - [[arxiv-omar-2018-live-functional-programming-with-typed-holes|raw/papers/arxiv-omar-2018-live-functional-programming-with-typed-holes.md]]
  - [[arxiv-doderlein-2026-spacetime-programming|raw/papers/arxiv-doderlein-2026-spacetime-programming.md]]
  - [[pernosco-omniscient-printf-debugging|raw/articles/pernosco-omniscient-printf-debugging.md]]
  - [[plutojl-interactive-programming-environment|raw/articles/plutojl-interactive-programming-environment.md]]
  - [[vistrails-aosa|raw/articles/vistrails-aosa.md]]
  - [[spatial-hypertext|raw/articles/spatial-hypertext.md]]
  - [[langgraph-studio-first-agent-ide|raw/articles/langgraph-studio-first-agent-ide.md]]
  - [[temporal-web-ui|raw/articles/temporal-web-ui.md]]
  - [[windmill-suspend-approval-prompts|raw/articles/windmill-suspend-approval-prompts.md]]
  - [[trigger-dev-product|raw/articles/trigger-dev-product.md]]
  - [[airflow-ui-overview|raw/articles/airflow-ui-overview.md]]
  - [[dagster-scaling-dag-visualization|raw/articles/dagster-scaling-dag-visualization.md]]
- Created 1 content page:
  - [[web-patterns-for-non-linear-harness-interfaces|queries/web-patterns-for-non-linear-harness-interfaces.md]]
- Updated existing synthesis pages so the new material participates in the main interface graph:
  - [[non-linear-interface-options-for-next-harness|queries/non-linear-interface-options-for-next-harness.md]]
- Updated [[index|index.md]] to include the new query and bump total pages from 34 to 35.

## [2026-04-09] ingest | under-explored coordination strategies arXiv pass
- Added 14 raw paper summaries:
  - [[arxiv-salemi-2025-llm-blackboard-data-discovery|raw/papers/arxiv-salemi-2025-llm-blackboard-data-discovery.md]]
  - [[arxiv-nakamura-2025-terrarium-blackboard-multi-agent-safety|raw/papers/arxiv-nakamura-2025-terrarium-blackboard-multi-agent-safety.md]]
  - [[arxiv-pugachev-2025-codecrdt-observation-driven-coordination|raw/papers/arxiv-pugachev-2025-codecrdt-observation-driven-coordination.md]]
  - [[arxiv-duetting-2023-mechanism-design-large-language-models|raw/papers/arxiv-duetting-2023-mechanism-design-large-language-models.md]]
  - [[arxiv-zhao-2025-llm-auction-generative-auction|raw/papers/arxiv-zhao-2025-llm-auction-generative-auction.md]]
  - [[arxiv-li-2025-lacp-agent-communication-protocol|raw/papers/arxiv-li-2025-lacp-agent-communication-protocol.md]]
  - [[arxiv-ehtesham-2025-survey-agent-interoperability-protocols|raw/papers/arxiv-ehtesham-2025-survey-agent-interoperability-protocols.md]]
  - [[arxiv-ben-khaled-2026-g2cp-graph-grounded-communication-protocol|raw/papers/arxiv-ben-khaled-2026-g2cp-graph-grounded-communication-protocol.md]]
  - [[arxiv-zou-2025-blocka2a-secure-verifiable-interoperability|raw/papers/arxiv-zou-2025-blocka2a-secure-verifiable-interoperability.md]]
  - [[arxiv-miculicich-2025-veriguard-verified-code-generation|raw/papers/arxiv-miculicich-2025-veriguard-verified-code-generation.md]]
  - [[arxiv-ye-2025-x-mas-heterogeneous-llms|raw/papers/arxiv-ye-2025-x-mas-heterogeneous-llms.md]]
  - [[arxiv-yu-2025-dyntaskmas-dynamic-task-graph|raw/papers/arxiv-yu-2025-dyntaskmas-dynamic-task-graph.md]]
  - [[arxiv-wang-2024-battleagentbench|raw/papers/arxiv-wang-2024-battleagentbench.md]]
  - [[arxiv-sun-2025-collab-overcooked|raw/papers/arxiv-sun-2025-collab-overcooked.md]]
- Created 1 content page:
  - [[arxiv-under-explored-coordination-strategies|queries/arxiv-under-explored-coordination-strategies.md]]
- Updated existing synthesis pages so the new coordination material participates in the main graph:
  - [[non-hierarchical-coordination-patterns|concepts/non-hierarchical-coordination-patterns.md]]
  - [[orchestration-topologies|concepts/orchestration-topologies.md]]
  - [[formal-methods-for-agent-harnesses|concepts/formal-methods-for-agent-harnesses.md]]
- Updated [[index|index.md]] to include the new query and bump total pages from 34 to 35.

## [2026-04-09] update | page-count recovery note
- The content-page total is 36, not 35.
- Two separate query-page ingests landed on 2026-04-09 ([[web-patterns-for-non-linear-harness-interfaces|queries/web-patterns-for-non-linear-harness-interfaces.md]] and [[arxiv-under-explored-coordination-strategies|queries/arxiv-under-explored-coordination-strategies.md]]), so the later page-bump note undercounted by one.
- [[index|index.md]] now records the repaired total while preserving the earlier historical note as written.

## [2026-04-09] ingest | legacy distributed-systems ideas and studio architecture spec
- Added 11 raw source summaries:
  - [[virtual-synchrony|raw/articles/virtual-synchrony.md]]
  - [[chandy-lamport-algorithm|raw/articles/chandy-lamport-algorithm.md]]
  - [[vector-clock|raw/articles/vector-clock.md]]
  - [[failure-detector|raw/articles/failure-detector.md]]
  - [[jif|raw/articles/jif.md]]
  - [[session-type|raw/articles/session-type.md]]
  - [[viewstamped-replication-revisited|raw/articles/viewstamped-replication-revisited.md]]
  - [[optimistic-replication|raw/articles/optimistic-replication.md]]
  - [[self-certifying-file-system|raw/articles/self-certifying-file-system.md]]
  - [[session-guarantees-weakly-consistent-replicated-data|raw/papers/session-guarantees-weakly-consistent-replicated-data.md]]
  - [[escrow-transactional-method|raw/papers/escrow-transactional-method.md]]
- Created 2 content pages:
  - [[legacy-distributed-systems-ideas-for-moldable-operations-studio|queries/legacy-distributed-systems-ideas-for-moldable-operations-studio.md]]
  - [[moldable-operations-studio-architecture-spec|queries/moldable-operations-studio-architecture-spec.md]]
- Updated existing synthesis pages so the new semantics layer participates in the main design graph:
  - [[new-harness-design-notes|queries/new-harness-design-notes.md]]
  - [[web-patterns-for-non-linear-harness-interfaces|queries/web-patterns-for-non-linear-harness-interfaces.md]]
- Updated [[index|index.md]] to include the new queries and bump total pages from 36 to 38.

## [2026-04-09] lint | maintenance pass
- Ran `scripts/lint-wiki.sh` and a structural audit across the content corpus.
- Fixed invalid YAML frontmatter quoting in:
  - [[arxiv-round-two-formal-semantics-for-agent-harnesses|queries/arxiv-round-two-formal-semantics-for-agent-harnesses.md]]
  - [[arxiv-under-explored-coordination-strategies|queries/arxiv-under-explored-coordination-strategies.md]]
- Repaired inbound navigation for previously orphaned query pages by cross-linking them from:
  - [[formal-methods-for-agent-harnesses|concepts/formal-methods-for-agent-harnesses.md]]
  - [[formal-cognition-loop|concepts/formal-cognition-loop.md]]
  - [[non-hierarchical-coordination-patterns|concepts/non-hierarchical-coordination-patterns.md]]
- Hardened `scripts/lint-wiki.sh` to parse YAML frontmatter, so colon-bearing titles now fail fast instead of slipping past the shell-only checks.
- Re-ran lint: pass, 36 content pages checked, with no orphan content pages in the follow-up structural scan.

## [2026-04-09] update | staged lint polish
- Adjusted `scripts/lint-wiki.sh` so the `updated:` check inspects staged modified content pages when a commit is in flight, rather than only unstaged worktree edits.
- Limited that `updated:` rule to modified tracked pages (`--diff-filter=M`), so newly introduced historical pages can keep their original creation/update dates.
- Guarded the git-diff branch so staged-tree audits outside a git checkout do not emit misleading repo warnings.

## [2026-04-09] ingest | schema pass and sci-fi audit for moldable operations studio
- Added 11 raw source summaries:
  - [[star-trek-lcars|raw/articles/star-trek-lcars.md]]
  - [[battlestar-galactica-dradis|raw/articles/battlestar-galactica-dradis.md]]
  - [[minority-report-film|raw/articles/minority-report-film.md]]
  - [[wargames|raw/articles/wargames.md]]
  - [[foundation-prime-radiant|raw/articles/foundation-prime-radiant.md]]
  - [[machineries-of-empire|raw/articles/machineries-of-empire.md]]
  - [[ancillary-justice|raw/articles/ancillary-justice.md]]
  - [[quantum-thief|raw/articles/quantum-thief.md]]
  - [[embassytown|raw/articles/embassytown.md]]
  - [[the-city-and-the-city|raw/articles/the-city-and-the-city.md]]
  - [[diaspora-novel|raw/articles/diaspora-novel.md]]
- Created 2 content pages:
  - [[moldable-operations-studio-schema-pass|queries/moldable-operations-studio-schema-pass.md]]
  - [[sci-fi-audit-for-moldable-operations-studio|queries/sci-fi-audit-for-moldable-operations-studio.md]]
- Updated existing synthesis pages so the new concrete and speculative layers participate in the main design graph:
  - [[moldable-operations-studio-architecture-spec|queries/moldable-operations-studio-architecture-spec.md]]
  - [[web-patterns-for-non-linear-harness-interfaces|queries/web-patterns-for-non-linear-harness-interfaces.md]]
- Updated [[index|index.md]] to include the new queries and bump total pages from 38 to 40.
- Re-ran lint after the fix: pass.

## [2026-04-09] ingest | grounded research for moldable operations studio ideas
- Added 20 raw source summaries:
  - [[yang-wigdor-2014-panelrama|raw/papers/yang-wigdor-2014-panelrama.md]]
  - [[klokmose-et-al-2015-webstrates|raw/papers/klokmose-et-al-2015-webstrates.md]]
  - [[bragdon-et-al-2011-code-space|raw/papers/bragdon-et-al-2011-code-space.md]]
  - [[danielsson-alvinius-larsson-2014-common-operating-picture|raw/papers/danielsson-alvinius-larsson-2014-common-operating-picture.md]]
  - [[nandiganahalli-et-al-2014-mode-confusion-detection|raw/papers/nandiganahalli-et-al-2014-mode-confusion-detection.md]]
  - [[honarmand-torrellas-2014-replay-debugging|raw/papers/honarmand-torrellas-2014-replay-debugging.md]]
  - [[ko-myers-2009-java-whyline|raw/papers/ko-myers-2009-java-whyline.md]]
  - [[stasko-gorg-liu-2008-jigsaw|raw/papers/stasko-gorg-liu-2008-jigsaw.md]]
  - [[andrews-north-2012-analysts-workspace|raw/papers/andrews-north-2012-analysts-workspace.md]]
  - [[groth-streefkerk-2006-provenance-annotation-visual-exploration|raw/papers/groth-streefkerk-2006-provenance-annotation-visual-exploration.md]]
  - [[amershi-et-al-2015-modeltracker|raw/papers/amershi-et-al-2015-modeltracker.md]]
  - [[wexler-et-al-2019-what-if-tool|raw/papers/wexler-et-al-2019-what-if-tool.md]]
  - [[malkhi-lamport-zhou-2008-stoppable-paxos|raw/papers/malkhi-lamport-zhou-2008-stoppable-paxos.md]]
  - [[rfc-9420-mls-protocol|raw/articles/rfc-9420-mls-protocol.md]]
  - [[rivest-lampson-1996-sdsi|raw/articles/rivest-lampson-1996-sdsi.md]]
  - [[birgisson-et-al-2014-macaroons|raw/papers/birgisson-et-al-2014-macaroons.md]]
  - [[efstathopoulos-et-al-2005-asbestos|raw/papers/efstathopoulos-et-al-2005-asbestos.md]]
  - [[finkelstein-et-al-1992-viewpoints|raw/papers/finkelstein-et-al-1992-viewpoints.md]]
  - [[foster-et-al-2007-bidirectional-tree-transformations|raw/papers/foster-et-al-2007-bidirectional-tree-transformations.md]]
  - [[green-karvounarakis-tannen-2007-provenance-semirings|raw/papers/green-karvounarakis-tannen-2007-provenance-semirings.md]]
- Created 1 content page:
  - [[grounding-moldable-operations-studio-ideas-in-real-research|queries/grounding-moldable-operations-studio-ideas-in-real-research.md]]
- Updated existing synthesis pages so the grounded-research layer participates in the main design graph:
  - [[moldable-operations-studio-architecture-spec|queries/moldable-operations-studio-architecture-spec.md]]
  - [[moldable-operations-studio-schema-pass|queries/moldable-operations-studio-schema-pass.md]]
  - [[sci-fi-audit-for-moldable-operations-studio|queries/sci-fi-audit-for-moldable-operations-studio.md]]
- Updated [[index|index.md]] to include the new query and bump total pages from 40 to 41.

## [2026-04-09] ingest | wireframe pass for moldable operations studio
- Added 1 asset:
  - raw/assets/moldable-operations-studio-wireframes.excalidraw
- Created 1 content page:
  - [[moldable-operations-studio-wireframes|queries/moldable-operations-studio-wireframes.md]]
- Updated existing synthesis pages so the wireframe layer participates in the main design graph:
  - [[moldable-operations-studio-architecture-spec|queries/moldable-operations-studio-architecture-spec.md]]
  - [[moldable-operations-studio-schema-pass|queries/moldable-operations-studio-schema-pass.md]]
  - [[grounding-moldable-operations-studio-ideas-in-real-research|queries/grounding-moldable-operations-studio-ideas-in-real-research.md]]
  - [[sci-fi-audit-for-moldable-operations-studio|queries/sci-fi-audit-for-moldable-operations-studio.md]]
- Updated [[index|index.md]] to include the new query; total pages now 42.

## [2026-04-09] update | page-count recovery after concurrent studio additions
- The content-page total is 44, not 42.
- Concurrent additions landed in the corpus while the wireframe pass was in flight, including [[self-evolving-workflows|concepts/self-evolving-workflows.md]] and [[arxiv-self-evolving-workflows-for-codex-control-plane|queries/arxiv-self-evolving-workflows-for-codex-control-plane.md]].
- [[index|index.md]] now records the repaired total while preserving the earlier line-level history.

## [2026-04-09] ingest | self-evolving workflows for gas-city-but-its-just-codex
- Added 16 raw source summaries:
  - [[gas-city-but-its-just-codex-repo-2026-04-09|raw/articles/gas-city-but-its-just-codex-repo-2026-04-09.md]]
  - [[arxiv-zhang-2024-aflow|raw/papers/arxiv-zhang-2024-aflow.md]]
  - [[arxiv-li-2024-autoflow|raw/papers/arxiv-li-2024-autoflow.md]]
  - [[arxiv-wang-2024-agent-workflow-memory|raw/papers/arxiv-wang-2024-agent-workflow-memory.md]]
  - [[arxiv-hu-2024-automated-design-of-agentic-systems|raw/papers/arxiv-hu-2024-automated-design-of-agentic-systems.md]]
  - [[arxiv-wang-2025-evoagentx|raw/papers/arxiv-wang-2025-evoagentx.md]]
  - [[arxiv-wang-2026-learning-to-compose-agentic-workflow-generation|raw/papers/arxiv-wang-2026-learning-to-compose-agentic-workflow-generation.md]]
  - [[arxiv-xu-2026-hyevo|raw/papers/arxiv-xu-2026-hyevo.md]]
  - [[arxiv-zhao-2025-a2flow|raw/papers/arxiv-zhao-2025-a2flow.md]]
  - [[arxiv-shen-2026-skillfoundry|raw/papers/arxiv-shen-2026-skillfoundry.md]]
  - [[arxiv-zhang-2026-evoskills|raw/papers/arxiv-zhang-2026-evoskills.md]]
  - [[arxiv-wang-2026-skillx|raw/papers/arxiv-wang-2026-skillx.md]]
  - [[arxiv-ma-2026-scaling-coding-agents-via-atomic-skills|raw/papers/arxiv-ma-2026-scaling-coding-agents-via-atomic-skills.md]]
  - [[arxiv-rhodes-2026-compiled-memory|raw/papers/arxiv-rhodes-2026-compiled-memory.md]]
  - [[arxiv-shinn-2023-reflexion|raw/papers/arxiv-shinn-2023-reflexion.md]]
  - [[arxiv-zhao-2023-expel|raw/papers/arxiv-zhao-2023-expel.md]]
- Created 2 content pages:
  - [[self-evolving-workflows|concepts/self-evolving-workflows.md]]
  - [[arxiv-self-evolving-workflows-for-codex-control-plane|queries/arxiv-self-evolving-workflows-for-codex-control-plane.md]]
- Updated existing pages to connect the new workflow-evolution layer into the main graph:
  - [[gas-city-but-its-just-codex|queries/gas-city-but-its-just-codex.md]]
  - [[work-management-primitives|concepts/work-management-primitives.md]]
  - [[memory-persistence|concepts/memory-persistence.md]]
- Updated [[index|index.md]] to include the new concept and query and bump total pages from 41 to 43.
- Re-ran lint after the ingest: pass, 43 content pages checked.

## [2026-04-09] ingest | broader arxiv sweep for self-evolving workflows
- Added 19 additional raw source summaries to widen the literature map beyond the first direct-hit pass:
  - [[arxiv-qiao-2024-benchmarking-agentic-workflow-generation|raw/papers/arxiv-qiao-2024-benchmarking-agentic-workflow-generation.md]]
  - [[arxiv-zheng-2025-mermaidflow|raw/papers/arxiv-zheng-2025-mermaidflow.md]]
  - [[arxiv-wang-2026-query-level-workflows|raw/papers/arxiv-wang-2026-query-level-workflows.md]]
  - [[arxiv-ma-2026-judgeflow|raw/papers/arxiv-ma-2026-judgeflow.md]]
  - [[arxiv-wang-2025-dyflow|raw/papers/arxiv-wang-2025-dyflow.md]]
  - [[arxiv-wang-2025-self-improving-agent-skill-library|raw/papers/arxiv-wang-2025-self-improving-agent-skill-library.md]]
  - [[arxiv-ye-2026-meta-context-engineering|raw/papers/arxiv-ye-2026-meta-context-engineering.md]]
  - [[arxiv-du-2025-bottom-up-skill-evolution|raw/papers/arxiv-du-2025-bottom-up-skill-evolution.md]]
  - [[arxiv-zhai-2025-agentevolver|raw/papers/arxiv-zhai-2025-agentevolver.md]]
  - [[arxiv-qian-2025-metaagent|raw/papers/arxiv-qian-2025-metaagent.md]]
  - [[arxiv-banerjee-2026-severa|raw/papers/arxiv-banerjee-2026-severa.md]]
  - [[arxiv-ye-2025-sop-agent|raw/papers/arxiv-ye-2025-sop-agent.md]]
  - [[arxiv-li-2025-sopbench|raw/papers/arxiv-li-2025-sopbench.md]]
  - [[arxiv-huo-2026-atommem|raw/papers/arxiv-huo-2026-atommem.md]]
  - [[arxiv-liu-2026-graph-of-skills|raw/papers/arxiv-liu-2026-graph-of-skills.md]]
  - [[arxiv-ni-2026-trace2skill|raw/papers/arxiv-ni-2026-trace2skill.md]]
  - [[arxiv-zhang-2026-memskill|raw/papers/arxiv-zhang-2026-memskill.md]]
  - [[arxiv-xia-2026-metaclaw|raw/papers/arxiv-xia-2026-metaclaw.md]]
  - [[arxiv-xu-2025-robustflow|raw/papers/arxiv-xu-2025-robustflow.md]]
- Expanded the main synthesis pages so the literature map now includes evaluator loops, robustness, retrieval over large skill libraries, and learnable memory/context routines:
  - [[self-evolving-workflows|concepts/self-evolving-workflows.md]]
  - [[arxiv-self-evolving-workflows-for-codex-control-plane|queries/arxiv-self-evolving-workflows-for-codex-control-plane.md]]
  - [[gas-city-but-its-just-codex|queries/gas-city-but-its-just-codex.md]]
  - [[index|index.md]]
- Re-ran lint after the broader sweep: pass, 43 content pages checked.

## [2026-04-09] ingest | rl gyms and executable environments for ai harnesses
- Added 20 raw source summaries for executable benchmark and training environments:
  - [[arxiv-zhou-2023-webarena|raw/papers/arxiv-zhou-2023-webarena.md]]
  - [[arxiv-chezelles-2024-browsergym-ecosystem|raw/papers/arxiv-chezelles-2024-browsergym-ecosystem.md]]
  - [[arxiv-koh-2024-visualwebarena|raw/papers/arxiv-koh-2024-visualwebarena.md]]
  - [[arxiv-drouin-2024-workarena|raw/papers/arxiv-drouin-2024-workarena.md]]
  - [[arxiv-boisvert-2024-workarena-plus-plus|raw/papers/arxiv-boisvert-2024-workarena-plus-plus.md]]
  - [[arxiv-pan-2024-webcanvas|raw/papers/arxiv-pan-2024-webcanvas.md]]
  - [[arxiv-xie-2024-osworld|raw/papers/arxiv-xie-2024-osworld.md]]
  - [[arxiv-bonatti-2024-windows-agent-arena|raw/papers/arxiv-bonatti-2024-windows-agent-arena.md]]
  - [[arxiv-trivedi-2024-appworld|raw/papers/arxiv-trivedi-2024-appworld.md]]
  - [[arxiv-ma-2024-agentboard|raw/papers/arxiv-ma-2024-agentboard.md]]
  - [[arxiv-xi-2024-agentgym|raw/papers/arxiv-xi-2024-agentgym.md]]
  - [[arxiv-nathani-2025-mlgym|raw/papers/arxiv-nathani-2025-mlgym.md]]
  - [[arxiv-pan-2024-swe-gym|raw/papers/arxiv-pan-2024-swe-gym.md]]
  - [[arxiv-yao-2024-tau-bench|raw/papers/arxiv-yao-2024-tau-bench.md]]
  - [[arxiv-chuang-2026-proxy-state-based-evaluation|raw/papers/arxiv-chuang-2026-proxy-state-based-evaluation.md]]
  - [[arxiv-chen-2025-rl-long-horizon-interactive-llm-agents|raw/papers/arxiv-chen-2025-rl-long-horizon-interactive-llm-agents.md]]
  - [[arxiv-lai-2025-computerrl|raw/papers/arxiv-lai-2025-computerrl.md]]
  - [[arxiv-mehta-2026-enterprisebench-corecraft|raw/papers/arxiv-mehta-2026-enterprisebench-corecraft.md]]
  - [[arxiv-mialon-2023-gaia|raw/papers/arxiv-mialon-2023-gaia.md]]
  - [[arxiv-yao-2022-webshop|raw/papers/arxiv-yao-2022-webshop.md]]
- Created 1 content page:
  - [[rl-gyms-and-executable-environments-for-ai-harnesses|queries/rl-gyms-and-executable-environments-for-ai-harnesses.md]]
- Updated existing concept pages so environment substrates connect back into the main harness graph:
  - [[evaluation-and-review-loops|concepts/evaluation-and-review-loops.md]]
  - [[harness-engineering|concepts/harness-engineering.md]]
- Updated [[index|index.md]] to include the new query and corrected the total page count from 43 to 45 after a recount.
- Re-ran lint after the gym sweep: pass, 45 content pages checked.

## [2026-04-10] ingest | neural-native programming via internal-layer interfaces
- Added 35 raw source notes to resolve the user-provided NNPL draft into explicit bibliography entries:
  - [[neural-native-programming-direct-internal-layer-interfaces-draft-2026-04-10|raw/articles/neural-native-programming-direct-internal-layer-interfaces-draft-2026-04-10.md]]
  - [[transformer-circuits-mathematical-framework|raw/articles/transformer-circuits-mathematical-framework.md]]
  - [[logit-lens-lesswrong|raw/articles/logit-lens-lesswrong.md]]
  - [[anthropic-toy-models-of-superposition|raw/articles/anthropic-toy-models-of-superposition.md]]
  - [[anthropic-monosemantic-features|raw/articles/anthropic-monosemantic-features.md]]
  - [[nnsight-docs|raw/articles/nnsight-docs.md]]
  - [[baukit-github|raw/articles/baukit-github.md]]
  - [[doug-github|raw/articles/doug-github.md]]
  - [[arxiv-vaswani-2017-attention-is-all-you-need|raw/papers/arxiv-vaswani-2017-attention-is-all-you-need.md]]
  - [[geva-2021-transformer-feed-forward-layers-are-key-value-memories|raw/papers/geva-2021-transformer-feed-forward-layers-are-key-value-memories.md]]
  - [[arxiv-belrose-2023-tuned-lens|raw/papers/arxiv-belrose-2023-tuned-lens.md]]
  - [[arxiv-hewitt-2019-structural-probe|raw/papers/arxiv-hewitt-2019-structural-probe.md]]
  - [[arxiv-meng-2022-locating-and-editing-factual-associations-in-gpt|raw/papers/arxiv-meng-2022-locating-and-editing-factual-associations-in-gpt.md]]
  - [[arxiv-turner-2023-steering-language-models-with-activation-engineering|raw/papers/arxiv-turner-2023-steering-language-models-with-activation-engineering.md]]
  - [[arxiv-panickssery-2023-steering-llama-2-via-contrastive-activation-addition|raw/papers/arxiv-panickssery-2023-steering-llama-2-via-contrastive-activation-addition.md]]
  - [[arxiv-dathathri-2019-pplm|raw/papers/arxiv-dathathri-2019-pplm.md]]
  - [[arxiv-wu-2024-pyvene|raw/papers/arxiv-wu-2024-pyvene.md]]
  - [[arxiv-li-2023-inference-time-intervention|raw/papers/arxiv-li-2023-inference-time-intervention.md]]
  - [[arxiv-zou-2023-representation-engineering|raw/papers/arxiv-zou-2023-representation-engineering.md]]
  - [[arxiv-burns-2022-discovering-latent-knowledge|raw/papers/arxiv-burns-2022-discovering-latent-knowledge.md]]
  - [[arxiv-hu-2021-lora|raw/papers/arxiv-hu-2021-lora.md]]
  - [[arxiv-reed-2015-neural-programmer-interpreters|raw/papers/arxiv-reed-2015-neural-programmer-interpreters.md]]
  - [[arxiv-kusner-2017-grammar-variational-autoencoder|raw/papers/arxiv-kusner-2017-grammar-variational-autoencoder.md]]
  - [[arxiv-van-den-oord-2017-neural-discrete-representation-learning|raw/papers/arxiv-van-den-oord-2017-neural-discrete-representation-learning.md]]
  - [[arxiv-hong-2020-latent-programmer|raw/papers/arxiv-hong-2020-latent-programmer.md]]
  - [[arxiv-macfarlane-2024-searching-latent-program-spaces|raw/papers/arxiv-macfarlane-2024-searching-latent-program-spaces.md]]
  - [[kanerva-2009-hyperdimensional-computing|raw/papers/kanerva-2009-hyperdimensional-computing.md]]
  - [[plate-1995-holographic-reduced-representations|raw/papers/plate-1995-holographic-reduced-representations.md]]
  - [[arxiv-gayler-2004-vector-symbolic-architectures|raw/papers/arxiv-gayler-2004-vector-symbolic-architectures.md]]
  - [[arxiv-weiss-2021-thinking-like-transformers|raw/papers/arxiv-weiss-2021-thinking-like-transformers.md]]
  - [[arxiv-lindner-2023-tracr|raw/papers/arxiv-lindner-2023-tracr.md]]
  - [[arxiv-tomkins-flanagan-2025-differentiable-vector-symbolic-types|raw/papers/arxiv-tomkins-flanagan-2025-differentiable-vector-symbolic-types.md]]
  - [[arxiv-chen-2021-evaluating-llms-trained-on-code|raw/papers/arxiv-chen-2021-evaluating-llms-trained-on-code.md]]
  - [[arxiv-austin-2021-program-synthesis-with-large-language-models|raw/papers/arxiv-austin-2021-program-synthesis-with-large-language-models.md]]
  - [[arxiv-hendrycks-2021-measuring-coding-challenge-competence-with-apps|raw/papers/arxiv-hendrycks-2021-measuring-coding-challenge-competence-with-apps.md]]
- Extended [[SCHEMA|SCHEMA.md]] with `mechanistic-interpretability` and `program-synthesis` tags so the new material can be filed without abusing older categories.
- Created 2 content pages:
  - [[neural-native-programming|concepts/neural-native-programming.md]]
  - [[neural-native-programming-via-direct-interfaces-to-transformer-internal-layers|queries/neural-native-programming-via-direct-interfaces-to-transformer-internal-layers.md]]
- Updated existing synthesis pages so the new topic participates in the current harness graph:
  - [[formal-cognition-loop|concepts/formal-cognition-loop.md]]
  - [[new-harness-design-notes|queries/new-harness-design-notes.md]]
  - [[non-linear-interface-options-for-next-harness|queries/non-linear-interface-options-for-next-harness.md]]
- Updated navigation/meta files:
  - [[SCHEMA|SCHEMA.md]]
  - [[index|index.md]]

## [2026-04-10] lint | neural-native programming ingest maintenance pass
- Ran `scripts/lint-wiki.sh` after the ingest.
- Initial lint failed because several already-modified tracked pages still carried `updated: 2026-04-09` even though the worktree date had advanced.
- Bumped `updated` to 2026-04-10 on the following pages to restore schema consistency:
  - [[evaluation-and-review-loops|concepts/evaluation-and-review-loops.md]]
  - [[harness-engineering|concepts/harness-engineering.md]]
  - [[memory-persistence|concepts/memory-persistence.md]]
  - [[work-management-primitives|concepts/work-management-primitives.md]]
  - [[gas-city-but-its-just-codex|queries/gas-city-but-its-just-codex.md]]
  - [[web-patterns-for-non-linear-harness-interfaces|queries/web-patterns-for-non-linear-harness-interfaces.md]]
- Re-ran lint: pass, 47 content pages checked.

## [2026-04-10] create | neural-native programming research program
- Added [[neural-native-programming-research-program|queries/neural-native-programming-research-program.md]] as a tighter staged plan with explicit promotion gates, kill criteria, benchmark order, and first-quarter deliverables.
- Cross-linked the new plan page from:
  - [[neural-native-programming|concepts/neural-native-programming.md]]
  - [[neural-native-programming-via-direct-interfaces-to-transformer-internal-layers|queries/neural-native-programming-via-direct-interfaces-to-transformer-internal-layers.md]]
- Updated [[index|index.md]] to include the new query and bump total pages from 47 to 48.

## [2026-04-10] lint | neural-native research-program follow-up
- Re-ran `scripts/lint-wiki.sh` after adding the research-program page.
- Result: pass, 48 content pages checked.

## [2026-04-10] ingest | rl gym entity pages and atropos fit analysis
- Added 2 repo-grounded raw source summaries for local harness integration state:
  - [[hermes-atropos-integration-2026-04-09|raw/articles/hermes-atropos-integration-2026-04-09.md]]
  - [[another-harness-repo-2026-04-09|raw/articles/another-harness-repo-2026-04-09.md]]
- Created 21 entity pages for the executable-environment and gym layer:
  - [[agentboard|entities/agentboard.md]]
  - [[agentgym|entities/agentgym.md]]
  - [[appworld|entities/appworld.md]]
  - [[atropos|entities/atropos.md]]
  - [[browsergym|entities/browsergym.md]]
  - [[computer-rl|entities/computer-rl.md]]
  - [[enterprisebench-corecraft|entities/enterprisebench-corecraft.md]]
  - [[gaia|entities/gaia.md]]
  - [[mlgym|entities/mlgym.md]]
  - [[osworld|entities/osworld.md]]
  - [[proxy-state-based-evaluation|entities/proxy-state-based-evaluation.md]]
  - [[sopbench|entities/sopbench.md]]
  - [[swe-gym|entities/swe-gym.md]]
  - [[tau-bench|entities/tau-bench.md]]
  - [[visualwebarena|entities/visualwebarena.md]]
  - [[webarena|entities/webarena.md]]
  - [[webcanvas|entities/webcanvas.md]]
  - [[webshop|entities/webshop.md]]
  - [[windows-agent-arena|entities/windows-agent-arena.md]]
  - [[workarena|entities/workarena.md]]
  - [[workarena-plus-plus|entities/workarena-plus-plus.md]]
- Created 1 synthesis page:
  - [[another-harness-and-atropos|queries/another-harness-and-atropos.md]]
- Updated the main gym synthesis and surrounding concept pages so the new environment layer participates in the harness graph:
  - [[rl-gyms-and-executable-environments-for-ai-harnesses|queries/rl-gyms-and-executable-environments-for-ai-harnesses.md]]
  - [[evaluation-and-review-loops|concepts/evaluation-and-review-loops.md]]
  - [[harness-engineering|concepts/harness-engineering.md]]
  - [[index|index.md]]
- Recounted content pages and updated index total from 48 to 70.
- Re-ran lint after the entity-page pass: pass, 70 content pages checked.

## [2026-04-10] ingest | concrete another-harness atropos schema
- Added 1 raw source summary for the new repo-native Atropos sidecar design:
  - [[another-harness-atropos-environment-schema-2026-04-10|raw/articles/another-harness-atropos-environment-schema-2026-04-10.md]]
- Created 1 synthesis page:
  - [[another-harness-atropos-environment-schema|queries/another-harness-atropos-environment-schema.md]]
- Updated existing pages so the concrete schema is linked back into the gym and fit-analysis graph:
  - [[another-harness-and-atropos|queries/another-harness-and-atropos.md]]
  - [[rl-gyms-and-executable-environments-for-ai-harnesses|queries/rl-gyms-and-executable-environments-for-ai-harnesses.md]]
  - [[index|index.md]]
- Updated [[index|index.md]] to include the new query and bump total pages from 70 to 71.
- Re-ran lint after the schema sync: pass, 71 content pages checked.

## [2026-04-10] update | public repo rename and github pages publishing layer
- Renamed the public GitHub repository from `wiki` to `agent-harness-wiki`.
- Added a lightweight MkDocs publishing layer with:
  - mkdocs.yml
  - docs-requirements.txt
  - scripts/prepare_site_docs.py
  - .github/workflows/pages.yml
  - [[README|README.md]] updates for local preview and published-site usage
  - .gitignore rules for generated site directories and local virtualenvs
- Enabled GitHub Pages in workflow-deployment mode and updated the Pages workflow to current action major versions to avoid stale Node 20 warnings.
- Verified the docs build locally after preparing the generated docs tree.
- Re-ran lint after the publishing-layer pass: pass, 70 content pages checked.

## [2026-04-10] update | another-harness work-item closure environment prototype
- Added 1 raw source summary for the first live executable environment slice in another-harness:
  - [[another-harness-work-item-closure-environment-2026-04-10|raw/articles/another-harness-work-item-closure-environment-2026-04-10.md]]
- Created 1 synthesis page:
  - [[another-harness-work-item-closure-environment|queries/another-harness-work-item-closure-environment.md]]
- Updated existing pages so the executable prototype is linked back into the Atropos fit/schema/gym graph:
  - [[another-harness-atropos-environment-schema|queries/another-harness-atropos-environment-schema.md]]
  - [[another-harness-and-atropos|queries/another-harness-and-atropos.md]]
  - [[rl-gyms-and-executable-environments-for-ai-harnesses|queries/rl-gyms-and-executable-environments-for-ai-harnesses.md]]
  - [[atropos|entities/atropos.md]]
  - [[index|index.md]]
- Updated [[index|index.md]] to include the new query and bump total pages from 71 to 72.
- Re-ran lint after the prototype sync: pass.

## [2026-04-10] update | seeded user evolution log
- Added top-level meta file:
  - USER_EVOLUTION_LOG.md
- Designed a durable entry format that separates explicit observations from inferred trends, records confidence, and preserves evidence, uncertainty, and what-to-watch-next.
- Seeded initial entries for 2026-04-05 through 2026-04-10 covering:
  - tightening acceptance and review standards
  - shift from compatibility analysis toward switchable Hermes profiles
  - movement toward non-linear / moldable operations studio interfaces
  - clearer separation of formulas, skills, memory, and evaluation in self-evolving workflow research
  - explicit agency-preserving collaboration norms

## [2026-04-10] ingest | multiplayer harness and p2p network research pass
- Added 7 raw source summaries for the local-first, peer-to-peer, interoperability, and multiplayer-surface layer:
  - [[local-first-software|raw/articles/local-first-software.md]]
  - [[pushpin-peer-to-peer-collaboration|raw/articles/pushpin-peer-to-peer-collaboration.md]]
  - [[jupyterlab-real-time-collaboration|raw/articles/jupyterlab-real-time-collaboration.md]]
  - [[visual-studio-live-share|raw/articles/visual-studio-live-share.md]]
  - [[google-agent2agent-protocol|raw/articles/google-agent2agent-protocol.md]]
  - [[merkle-crdts|raw/papers/merkle-crdts.md]]
  - [[maymounkov-mazieres-2002-kademlia|raw/papers/maymounkov-mazieres-2002-kademlia.md]]
- Created 1 synthesis page:
  - [[multiplayer-agent-harnesses-and-p2p-networks|queries/multiplayer-agent-harnesses-and-p2p-networks.md]]
- Updated existing synthesis pages so the new multiplayer/federated direction is linked into the harness graph:
  - [[new-harness-design-notes|queries/new-harness-design-notes.md]]
  - [[non-hierarchical-agent-orchestration|queries/non-hierarchical-agent-orchestration.md]]
  - [[index|index.md]]
- Updated [[index|index.md]] to include the new query and bump total pages from 72 to 73.
- Re-ran lint after the research pass: pass, 73 content pages checked.

## [2026-04-10] create | multiplayer harness build strategy
- Created 1 synthesis page answering the implementation-order question directly:
  - [[how-to-build-a-multiplayer-harness-network|queries/how-to-build-a-multiplayer-harness-network.md]]
- Updated the multiplayer research synthesis to point at the new implementation-focused page:
  - [[multiplayer-agent-harnesses-and-p2p-networks|queries/multiplayer-agent-harnesses-and-p2p-networks.md]]
- Updated [[index|index.md]] to include the new query and bump total pages from 73 to 74.
- Re-ran lint after the build-strategy pass: pass.

## [2026-04-10] create | multiplayer harness inspection guide
- Created 1 synthesis page for deciding what to inspect first when shaping the design:
  - [[high-impact-artifacts-for-multiplayer-harness-design|queries/high-impact-artifacts-for-multiplayer-harness-design.md]]
- Updated the build-strategy page to point at the new inspection guide:
  - [[how-to-build-a-multiplayer-harness-network|queries/how-to-build-a-multiplayer-harness-network.md]]
- Updated [[index|index.md]] to include the new query and bump total pages from 74 to 75.
- Re-ran lint after the inspection-guide pass: pass.

## [2026-04-10] update | another-harness evaluator-discipline environment prototype
- Added 1 raw source summary for the second live executable environment slice in another-harness:
  - [[another-harness-evaluator-discipline-environment-2026-04-10|raw/articles/another-harness-evaluator-discipline-environment-2026-04-10.md]]
- Created 1 synthesis page:
  - [[another-harness-evaluator-discipline-environment|queries/another-harness-evaluator-discipline-environment.md]]
- Updated existing pages so the evaluator prototype is linked back into the Atropos fit/schema/gym graph:
  - [[another-harness-work-item-closure-environment|queries/another-harness-work-item-closure-environment.md]]
  - [[another-harness-atropos-environment-schema|queries/another-harness-atropos-environment-schema.md]]
  - [[another-harness-and-atropos|queries/another-harness-and-atropos.md]]
  - [[rl-gyms-and-executable-environments-for-ai-harnesses|queries/rl-gyms-and-executable-environments-for-ai-harnesses.md]]
  - [[atropos|entities/atropos.md]]
  - [[index|index.md]]
- Updated [[index|index.md]] to include the new query and bump total pages from 75 to 76.
- Re-ran lint after the evaluator-prototype sync: pass.

## [2026-04-10] ingest | sovereignty and observed-goals deep-dive for multiplayer harnesses
- Added 12 raw source summaries spanning portable attestations, trust management, proof-carrying authorization, provenance, commitments, governance, goal recognition, and socially translucent collaboration:
  - [[w3c-verifiable-credentials-data-model-v2|raw/articles/w3c-verifiable-credentials-data-model-v2.md]]
  - [[li-mitchell-winsborough-role-based-trust-management-framework|raw/papers/li-mitchell-winsborough-role-based-trust-management-framework.md]]
  - [[bauer-schneider-felten-appel-proof-carrying-authorization|raw/papers/bauer-schneider-felten-appel-proof-carrying-authorization.md]]
  - [[claimchain|raw/papers/claimchain.md]]
  - [[torres-arias-2019-in-toto|raw/papers/torres-arias-2019-in-toto.md]]
  - [[w3c-prov-dm|raw/articles/w3c-prov-dm.md]]
  - [[medina-mora-winograd-flores-flores-action-workflow-approach|raw/papers/medina-mora-winograd-flores-flores-action-workflow-approach.md]]
  - [[fornara-colombetti-commitment-based-agent-communication-language|raw/papers/fornara-colombetti-commitment-based-agent-communication-language.md]]
  - [[singh-chopra-computational-governance-violable-contracts|raw/papers/singh-chopra-computational-governance-violable-contracts.md]]
  - [[keren-gal-karpas-goal-recognition-design|raw/papers/keren-gal-karpas-goal-recognition-design.md]]
  - [[ramirez-geffner-probabilistic-plan-recognition|raw/papers/ramirez-geffner-probabilistic-plan-recognition.md]]
  - [[erickson-et-al-socially-translucent-systems|raw/papers/erickson-et-al-socially-translucent-systems.md]]
- Added 2 synthesis pages from the multi-round deep-dive:
  - [[commitment-governance-semantics-for-multiplayer-harness|queries/commitment-governance-semantics-for-multiplayer-harness.md]]
  - [[sovereignty-and-observed-goals-ledgers-for-multiplayer-harnesses|queries/sovereignty-and-observed-goals-ledgers-for-multiplayer-harnesses.md]]
- Updated existing synthesis/navigation pages to link the new sovereignty track into the harness graph:
  - [[high-impact-artifacts-for-multiplayer-harness-design|queries/high-impact-artifacts-for-multiplayer-harness-design.md]]
  - [[multiplayer-agent-harnesses-and-p2p-networks|queries/multiplayer-agent-harnesses-and-p2p-networks.md]]
  - [[index|index.md]]
- Recounted content pages and updated index total from 76 to 78.
- Note: the commitment/governance synthesis page was materialized during the deeper research pass itself; this entry records it explicitly so the log matches the on-disk truth.

## [2026-04-10] create | sovereign identity and observed-goals schema pass
- Created 1 concrete schema page layering sovereignty and non-scalar trust into the control plane:
  - [[sovereign-identity-and-observed-goals-schema-pass|queries/sovereign-identity-and-observed-goals-schema-pass.md]]
- Updated existing synthesis pages so the new schema pass is linked into the research graph:
  - [[sovereignty-and-observed-goals-ledgers-for-multiplayer-harnesses|queries/sovereignty-and-observed-goals-ledgers-for-multiplayer-harnesses.md]]
  - [[moldable-operations-studio-schema-pass|queries/moldable-operations-studio-schema-pass.md]]
  - [[high-impact-artifacts-for-multiplayer-harness-design|queries/high-impact-artifacts-for-multiplayer-harness-design.md]]
  - [[index|index.md]]
- Updated [[index|index.md]] to include the new query and bump total pages from 78 to 79.
- Re-ran lint after the schema pass: pass, 79 content pages checked.

## [2026-04-10] create | node card and minimum adapter contract
- Created 1 concrete federation-boundary page:
  - [[node-card-and-minimum-adapter-contract|queries/node-card-and-minimum-adapter-contract.md]]
- Updated existing synthesis/schema pages so the adapter contract is linked into the multiplayer and sovereignty graph:
  - [[how-to-build-a-multiplayer-harness-network|queries/how-to-build-a-multiplayer-harness-network.md]]
  - [[sovereign-identity-and-observed-goals-schema-pass|queries/sovereign-identity-and-observed-goals-schema-pass.md]]
  - [[high-impact-artifacts-for-multiplayer-harness-design|queries/high-impact-artifacts-for-multiplayer-harness-design.md]]
  - [[index|index.md]]
- Updated [[index|index.md]] to include the new query and bump total pages from 79 to 80.
- Re-ran lint after the contract pass: pass, 80 content pages checked.

## [2026-04-11] create | prompt optimization research and dspy follow-ups
- Created 1 raw research batch note capturing arXiv/OpenAlex-grounded bibliography and notes:
  - [[prompt-optimization-dspy-followups-2026-04-11|raw/articles/prompt-optimization-dspy-followups-2026-04-11.md]]
- Created 1 new entity page for the central framework and 1 synthesis/query page:
  - [[dspy|entities/dspy.md]]
  - [[prompt-optimization-and-dspy-follow-ups|queries/prompt-optimization-and-dspy-follow-ups.md]]
- Updated schema and navigation to include DSPy in the implementation taxonomy and add both new pages to the index:
  - [[SCHEMA|SCHEMA.md]]
  - [[index|index.md]]
- Intended focus: RL prompt optimization, prompt-program systems, and the early research line following DSPy.

## [2026-04-11] create | prompt optimization timeline and harness lessons
- Created 1 follow-on synthesis page that turns the prompt-optimization survey into a chronological map and an agent-harness design memo:
  - [[prompt-optimization-timeline-and-harness-lessons|queries/prompt-optimization-timeline-and-harness-lessons.md]]
- Updated related prompt-program pages and navigation so the new synthesis is linked into the graph:
  - [[prompt-optimization-and-dspy-follow-ups|queries/prompt-optimization-and-dspy-follow-ups.md]]
  - [[dspy|entities/dspy.md]]
  - [[index|index.md]]
- Updated index total from 83 to 84.

## [2026-04-11] create | prompt-program deployment open questions
- Created 1 new synthesis page focused on deployment-time research gaps for prompt programs and writable instruction artifacts:
  - [[prompt-program-deployment-open-questions|queries/prompt-program-deployment-open-questions.md]]
- Updated navigation to include the new page in the query index:
  - [[index|index.md]]
- Focus: compile-time vs runtime adaptation, promotion and rollback, safety constraints, drift, human oversight, memory substrates, and long-lived harness packaging.
- Updated index total from 84 to 85.

## [2026-04-11] create | prompt optimization open questions fan-out
- Created 2 raw research batch notes for the fan-out clusters:
  - [[prompt-optimization-eval-transfer-robustness-open-questions-2026-04-11|raw/articles/prompt-optimization-eval-transfer-robustness-open-questions-2026-04-11.md]]
  - [[prompt-optimization-representation-optimizer-open-questions-2026-04-11|raw/articles/prompt-optimization-representation-optimizer-open-questions-2026-04-11.md]]
- Created 4 query/synthesis pages covering the umbrella map and the three main open-question clusters:
  - [[open-questions-in-prompt-optimization-and-language-programs|queries/open-questions-in-prompt-optimization-and-language-programs.md]]
  - [[prompt-optimization-eval-transfer-robustness-open-questions|queries/prompt-optimization-eval-transfer-robustness-open-questions.md]]
  - [[prompt-program-representation-and-optimizer-open-questions|queries/prompt-program-representation-and-optimizer-open-questions.md]]
  - [[prompt-program-deployment-open-questions|queries/prompt-program-deployment-open-questions.md]]
- Updated navigation and page metadata to index the new pages and normalize frontmatter/tags for lint correctness:
  - [[index|index.md]]
  - [[prompt-optimization-eval-transfer-robustness-open-questions|queries/prompt-optimization-eval-transfer-robustness-open-questions.md]]
  - [[prompt-program-representation-and-optimizer-open-questions|queries/prompt-program-representation-and-optimizer-open-questions.md]]
  - [[prompt-program-deployment-open-questions|queries/prompt-program-deployment-open-questions.md]]
- Updated index total from 85 to 88.

## [2026-04-11] update | another-harness run-history decision
- Added 1 raw repository-synthesis note:
  - [[another-harness-run-history-decision-2026-04-11|raw/articles/another-harness-run-history-decision-2026-04-11.md]]
- Updated the main Atropos fit synthesis page so it now records the repo's explicit storage answer:
  - [[another-harness-and-atropos|queries/another-harness-and-atropos.md]]
- Updated [[index|index.md]] so the query summary reflects the new run-history stance while keeping total content pages at 88.
- Captured the repo's current decision that `state/runs/` remains non-canonical and that historically important attempts should live as derived evidence bundles under `docs/plans/artifacts/` until real multi-attempt pressure says otherwise.

## [2026-04-11] lint | wiki pass after another-harness run-history sync
- Ran `scripts/lint-wiki.sh` after the run-history decision sync.
- Confirmed the updated query/index metadata and the new raw note pass the current wiki structural checks.

## [2026-04-11] create | self-evolving workflow tool coverage
- Created 25 entity pages so the systems and benchmarks named in [[arxiv-self-evolving-workflows-for-codex-control-plane|queries/arxiv-self-evolving-workflows-for-codex-control-plane.md]] are first-class wiki nodes:
  - [[aflow|entities/aflow.md]]
  - [[agent-workflow-memory|entities/agent-workflow-memory.md]]
  - [[agentevolver|entities/agentevolver.md]]
  - [[atommem|entities/atommem.md]]
  - [[autoflow|entities/autoflow.md]]
  - [[compiled-memory|entities/compiled-memory.md]]
  - [[dyflow|entities/dyflow.md]]
  - [[evoskills|entities/evoskills.md]]
  - [[expel|entities/expel.md]]
  - [[graph-of-skills|entities/graph-of-skills.md]]
  - [[judgeflow|entities/judgeflow.md]]
  - [[memskill|entities/memskill.md]]
  - [[mermaidflow|entities/mermaidflow.md]]
  - [[metaagent|entities/metaagent.md]]
  - [[metaclaw|entities/metaclaw.md]]
  - [[reflexion|entities/reflexion.md]]
  - [[robustflow|entities/robustflow.md]]
  - [[sage|entities/sage.md]]
  - [[severa|entities/severa.md]]
  - [[skillfoundry|entities/skillfoundry.md]]
  - [[skillx|entities/skillx.md]]
  - [[sop-agent|entities/sop-agent.md]]
  - [[trace2skill|entities/trace2skill.md]]
  - [[worfbench|entities/worfbench.md]]
  - [[worfeval|entities/worfeval.md]]
- Updated the query page to add the missing raw sources for Learning to Compose and AgentEvolver, and replaced plain-text system names with wikilinks where appropriate:
  - [[arxiv-self-evolving-workflows-for-codex-control-plane|queries/arxiv-self-evolving-workflows-for-codex-control-plane.md]]
- Updated the core concept page so its main workflow, evaluation, memory, and skill-system examples now resolve to concrete entity pages:
  - [[self-evolving-workflows|concepts/self-evolving-workflows.md]]
- Updated [[index|index.md]] to include the new entities and bump total pages from 88 to 113.

## [2026-04-11] lint | self-evolving workflow tool coverage pass
- Ran `scripts/lint-wiki.sh` after adding the workflow, memory, skill-library, and self-evolving-agent entity pages.
- Confirmed index coverage and wikilink resolution for the new entity set: pass, 113 content pages checked.

## [2026-04-11] create | prompt optimization tool coverage
- Created 5 raw paper notes so the main prompt-program optimizer systems now have first-class source stubs:
  - [[arxiv-deng-2022-rlprompt|raw/papers/arxiv-deng-2022-rlprompt.md]]
  - [[arxiv-yuksekgonul-2024-textgrad|raw/papers/arxiv-yuksekgonul-2024-textgrad.md]]
  - [[arxiv-agrawal-2025-gepa|raw/papers/arxiv-agrawal-2025-gepa.md]]
  - [[arxiv-singhvi-2023-dspy-assertions|raw/papers/arxiv-singhvi-2023-dspy-assertions.md]]
  - [[schnabel-2024-sammo|raw/papers/schnabel-2024-sammo.md]]
- Created 5 entity pages so the prompt-optimization literature has concrete reusable nodes rather than only query-page mentions:
  - [[rlprompt|entities/rlprompt.md]]
  - [[textgrad|entities/textgrad.md]]
  - [[gepa|entities/gepa.md]]
  - [[dspy-assertions|entities/dspy-assertions.md]]
  - [[sammo|entities/sammo.md]]
- Updated the central prompt-program synthesis pages so the new systems resolve as concrete entities and the DSPy follow-up line is less foggy:
  - [[dspy|entities/dspy.md]]
  - [[prompt-optimization-and-dspy-follow-ups|queries/prompt-optimization-and-dspy-follow-ups.md]]
  - [[prompt-optimization-timeline-and-harness-lessons|queries/prompt-optimization-timeline-and-harness-lessons.md]]
  - [[prompt-program-representation-and-optimizer-open-questions|queries/prompt-program-representation-and-optimizer-open-questions.md]]
  - [[prompt-optimization-eval-transfer-robustness-open-questions|queries/prompt-optimization-eval-transfer-robustness-open-questions.md]]
  - [[prompt-program-deployment-open-questions|queries/prompt-program-deployment-open-questions.md]]
  - [[index|index.md]]
- Normalized the index total to 119 after adding the new prompt-optimizer entity set and reconciling prompt-query coverage.

## [2026-04-11] create | research on the ten prompt-optimization questions
- Added 1 supporting raw research note for extra cross-cutting evaluator / programming-language / release-engineering references:
  - [[additional-cross-cutting-prompt-program-papers-2026-04-11|raw/articles/additional-cross-cutting-prompt-program-papers-2026-04-11.md]]
- Created 1 question-by-question synthesis page covering the ten cross-cutting open questions with anchor papers and concise research reads:
  - [[research-on-open-questions-in-prompt-optimization-and-language-programs|queries/research-on-open-questions-in-prompt-optimization-and-language-programs.md]]
- Updated related prompt-program navigation so the new research map is reachable from the umbrella open-questions page and indexed in the query catalog:
  - [[open-questions-in-prompt-optimization-and-language-programs|queries/open-questions-in-prompt-optimization-and-language-programs.md]]
  - [[index|index.md]]
- Updated index total from 118 to 119.

## [2026-04-11] create | another-harness model-docs drift checker
- Added 1 raw repository-synthesis note:
  - [[another-harness-model-docs-drift-check-2026-04-11|raw/articles/another-harness-model-docs-drift-check-2026-04-11.md]]
- Created 1 query page capturing why the repo's first Lean-backed drift fence targets the attempt-vs-stream grounding distinction:
  - [[another-harness-model-docs-drift-checker|queries/another-harness-model-docs-drift-checker.md]]
- Updated navigation so the new page is indexed alongside the other another-harness slices:
  - [[index|index.md]]
- Updated index total from 119 to 120.

## [2026-04-11] lint | wiki pass after model-docs drift sync
- Ran `scripts/lint-wiki.sh` after the 0032 sync.
- Confirmed the new raw note, query page, and index update pass the current wiki structural checks.

## [2026-04-11] create | three more prompt-optimizer branches
- Added 5 raw paper notes for the runtime-adaptation, RL-over-program, and planning/evolution optimizer branches:
  - raw/papers/arxiv-zhang-2022-tempera.md
  - raw/papers/azim-2025-autodspy.md
  - raw/papers/arxiv-yang-2023-opro.md
  - raw/papers/arxiv-fernando-2023-promptbreeder.md
  - raw/papers/arxiv-wang-2023-promptagent.md
- Created 5 entity pages so these optimizer families now have first-class wiki nodes:
  - entities/tempera.md
  - entities/autodspy.md
  - entities/opro.md
  - entities/promptbreeder.md
  - entities/promptagent.md
- Created 1 synthesis page that turns the newly covered systems into a regime map for harness design:
  - queries/prompt-optimizer-regimes-for-harnesses.md
- Updated the central DSPy and prompt-optimization pages so the new systems resolve as concrete entities and the optimizer-family map is more explicit:
  - entities/dspy.md
  - entities/rlprompt.md
  - queries/prompt-optimization-and-dspy-follow-ups.md
  - queries/prompt-optimization-timeline-and-harness-lessons.md
  - queries/prompt-program-representation-and-optimizer-open-questions.md
  - queries/prompt-program-deployment-open-questions.md
  - queries/research-on-open-questions-in-prompt-optimization-and-language-programs.md
  - index.md
- Updated index total from 120 to 126.
