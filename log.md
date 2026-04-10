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

## [2026-04-07] ingest | Current-source refresh from parallel research agents
- Spawned three parallel research agents to expand the corpus across OpenAI/Codex, Anthropic/Claude Code, and persistent-orchestrator runtimes.
- Added 9 raw source summaries for newly researched primary sources:
  - raw/articles/openai-introducing-codex-app.md
  - raw/articles/openai-codex-app-server-readme.md
  - raw/articles/anthropic-claude-code-overview.md
  - raw/articles/anthropic-claude-code-memory.md
  - raw/articles/anthropic-claude-code-settings.md
  - raw/articles/hermes-agent-memory-docs.md
  - raw/articles/hermes-agent-api-server-docs.md
  - raw/articles/openclaw-agent-runtime-docs.md
  - raw/articles/yegge-gas-town-emergency-user-manual.md
- Updated major pages to reflect current surface models, memory systems, permissions, and orchestration details:
  - entities/codex-cli.md
  - entities/claude-code.md
  - entities/hermes-agent.md
  - entities/openclaw.md
  - entities/gas-town.md
  - entities/gas-city.md
  - concepts/agent-harness-anatomy.md
  - concepts/context-engineering.md
  - concepts/memory-persistence.md
  - concepts/safety-and-permissions.md
  - concepts/evaluation-and-review-loops.md
  - comparisons/harness-architecture-comparison.md
  - comparisons/harness-quality-comparison.md

## [2026-04-07] create | codex-app-server
- Added entities/codex-app-server.md because the App Server is now central enough in OpenAI's public materials to warrant its own page.
- Updated index.md to include the new entity and bump total pages from 16 to 17.

## [2026-04-07] create | harness-decision-matrix
- Added comparisons/harness-decision-matrix.md to turn the current qualitative corpus into a weighted design-choice table.
- Cross-linked the new comparison from comparisons/harness-quality-comparison.md and queries/new-harness-design-notes.md so it participates in the existing synthesis graph.
- Updated index.md to include the new comparison and bump total pages from 17 to 18.

## [2026-04-07] create | automation-and-background-work
- Added concepts/automation-and-background-work.md to capture the recurring-work pattern now visible across Codex app automations, Claude Code recurring tasks, and Hermes cron jobs.
- Cross-linked the new concept from concepts/context-engineering.md, concepts/work-management-primitives.md, concepts/safety-and-permissions.md, entities/codex-cli.md, entities/claude-code.md, and entities/hermes-agent.md.
- Updated index.md to include the new concept and bump total pages from 18 to 19.

## [2026-04-07] create | instruction-layering
- Added concepts/instruction-layering.md to separate durable scoped guidance from transcript memory, using `AGENTS.md`, `CLAUDE.md`, Hermes memory files, and OpenClaw bootstrap files as the main examples.
- Cross-linked the new concept from concepts/context-engineering.md, concepts/memory-persistence.md, concepts/safety-and-permissions.md, entities/codex-cli.md, entities/claude-code.md, entities/hermes-agent.md, and entities/openclaw.md.
- Updated index.md to include the new concept and bump total pages from 19 to 20.

## [2026-04-07] ingest | orchestration and automation docs refresh
- Added 4 raw source summaries for current official docs:
  - raw/articles/anthropic-claude-code-subagents.md
  - raw/articles/anthropic-claude-code-agent-teams.md
  - raw/articles/anthropic-claude-code-scheduled-tasks.md
  - raw/articles/openai-codex-chatgpt-plan.md
- Updated synthesis pages to reflect the stronger distinction between subagents, session teams, and background work:
  - concepts/agent-harness-anatomy.md
  - concepts/automation-and-background-work.md
  - entities/claude-code.md
  - comparisons/harness-architecture-comparison.md
  - queries/new-harness-design-notes.md

## [2026-04-07] create | orchestration-topologies
- Added concepts/orchestration-topologies.md to capture the emerging split between inline subagents, separate-session teams, and full swarm/factory coordination.
- Cross-linked the new concept from concepts/agent-harness-anatomy.md, concepts/automation-and-background-work.md, entities/claude-code.md, comparisons/harness-architecture-comparison.md, and queries/new-harness-design-notes.md.
- Updated index.md to include the new concept and bump total pages from 21 to 22.

## [2026-04-08] ingest | arXiv round two on formal semantics for agent harnesses
- Added 6 raw paper summaries:
  - raw/papers/arxiv-zhang-2024-formal-methods-trustworthy-ai-agents.md
  - raw/papers/arxiv-lahiri-2026-intent-formalization.md
  - raw/papers/arxiv-conradie-2016-probabilistic-epistemic-updates.md
  - raw/papers/arxiv-kishida-2017-categories-for-dynamic-epistemic-logic.md
  - raw/papers/arxiv-wang-2026-structural-operational-semantics-true-concurrency.md
  - raw/papers/arxiv-edixhoven-2022-branching-pomsets-for-choreographies.md
- Extended SCHEMA.md with new tags for `formal-methods`, `semantics`, `epistemics`, and `concurrency`.
- Created 4 content pages:
  - concepts/formal-methods-for-agent-harnesses.md
  - concepts/probabilistic-epistemic-updates.md
  - concepts/partial-order-trace-semantics.md
  - queries/arxiv-round-two-formal-semantics-for-agent-harnesses.md
- Updated existing synthesis pages to cross-link the new research layer:
  - concepts/harness-engineering.md
  - concepts/agent-harness-anatomy.md
  - concepts/work-management-primitives.md
  - concepts/orchestration-topologies.md
  - concepts/memory-persistence.md
- Updated index.md to include the new pages and bump total pages from 22 to 26.

## [2026-04-08] ingest | formal-core cognition research pass
- Added 6 raw paper summaries:
  - raw/papers/arxiv-song-2024-lean-copilot.md
  - raw/papers/arxiv-endres-2023-natural-language-to-postconditions.md
  - raw/papers/arxiv-murphy-2024-llm-codegen-formal-spec-reactive-synthesis.md
  - raw/papers/arxiv-lin-2024-fvel.md
  - raw/papers/arxiv-burigana-2026-epddl.md
  - raw/papers/arxiv-allen-2025-sound-complete-neurosymbolic-reasoning.md
- Created 3 content pages:
  - concepts/theorem-proving-as-cognitive-kernel.md
  - concepts/formal-cognition-loop.md
  - queries/formal-core-agent-architecture.md
- Updated existing synthesis pages to absorb the new formal-core angle:
  - concepts/formal-methods-for-agent-harnesses.md
  - queries/new-harness-design-notes.md
- Updated index.md to include the new pages and bump total pages from 26 to 29.

## [2026-04-08] ingest | non-linear harness interface research pass
- Added 9 raw paper summaries:
  - raw/papers/arxiv-sarkar-2023-code-relevant-ui.md
  - raw/papers/arxiv-angert-2023-spellburst.md
  - raw/papers/arxiv-rein-2024-live-programmers.md
  - raw/papers/arxiv-krause-glau-2023-code-proximal-dynamic-software-visualization.md
  - raw/papers/arxiv-kuhn-2010-spatial-software-visualization-ide.md
  - raw/papers/arxiv-li-2024-kishu-time-traveling-notebooks.md
  - raw/papers/arxiv-fang-2025-code-data-space-versioning.md
  - raw/papers/arxiv-chen-2022-nl2interface.md
  - raw/papers/arxiv-krause-glau-2024-code-review-software-city.md
- Created 1 content page:
  - queries/non-linear-interface-options-for-next-harness.md
- Updated existing synthesis pages to absorb the new surface/interface angle:
  - concepts/agent-harness-anatomy.md
  - concepts/harness-engineering.md
  - queries/new-harness-design-notes.md
- Updated index.md to include the new query and bump total pages from 29 to 30.

## [2026-04-08] update | add diagrams to core concept pages
- Added Mermaid diagrams to clarify structure and flow on:
  - concepts/agent-harness-anatomy.md
  - concepts/work-management-primitives.md
  - concepts/formal-cognition-loop.md
  - concepts/orchestration-topologies.md
- Chose diagrams that mirror existing prose rather than introducing new claims: a harness component map, a work-object lifecycle, a formalization loop, and a topology comparison sketch.

## [2026-04-08] lint | wiki grooming pass
- Audited the corpus against the current schema: index coverage, source existence, tag taxonomy, outbound wikilinks, and modified-page `updated` dates.
- Fixed the taxonomy violation in `queries/gas-city-but-its-just-codex.md` by replacing ad hoc tags with existing schema tags.
- Bumped stale `updated` dates on the already edited comparison, concept, and query pages so frontmatter matches the current worktree.
- Added `scripts/lint-wiki.sh` and documented it in `SCHEMA.md` so future grooming does not depend on chat memory.

## [2026-04-09] ingest | non-hierarchical orchestration research pass
- Added 11 raw paper summaries for non-hierarchical coordination patterns and dolphin-sociality inputs:
  - raw/papers/smith-1980-contract-net-protocol.md
  - raw/papers/gelernter-1985-generative-communication-in-linda.md
  - raw/papers/mcmanus-1991-design-and-analysis-tools-for-concurrent-blackboard-systems.md
  - raw/papers/olfati-saber-fax-murray-2007-consensus-and-cooperation-in-networked-multi-agent-systems.md
  - raw/papers/shehory-kraus-1998-methods-for-task-allocation-via-agent-coalition-formation.md
  - raw/papers/dias-zlot-kalra-stentz-2006-market-based-multirobot-coordination.md
  - raw/papers/brambilla-ferrante-birattari-dorigo-2013-swarm-robotics-review.md
  - raw/papers/lusseau-conradt-2009-unshared-consensus-decisions-dolphins.md
  - raw/papers/bruck-2013-decades-long-social-memory-in-bottlenose-dolphins.md
  - raw/papers/evans-krzyszczyk-frere-mann-2021-lifetime-stability-of-social-traits-in-bottlenose-dolphins.md
  - raw/papers/king-connor-kruetzen-allen-2021-cooperation-based-concept-formation-in-male-bottlenose-dolphins.md
- Created 3 content pages:
  - concepts/non-hierarchical-coordination-patterns.md
  - concepts/fission-fusion-orchestration.md
  - queries/non-hierarchical-agent-orchestration.md
- Updated existing synthesis pages so the new material participates in the main design graph:
  - concepts/orchestration-topologies.md
  - queries/new-harness-design-notes.md
- Updated index.md to include the new pages and bump total pages from 30 to 33.

## [2026-04-09] ingest | Memento-Skills paper and companion code
- Added 2 raw source summaries:
  - raw/papers/arxiv-zhou-2026-memento-skills.md
  - raw/articles/memento-skills-github.md
- Created 1 content page:
  - entities/memento-skills.md
- Updated existing synthesis pages so the new system participates in the main graph:
  - concepts/memory-persistence.md
  - comparisons/harness-architecture-comparison.md
- Extended SCHEMA.md with a `memento-skills` implementation tag.
- Updated index.md to include the new entity and bump total pages from 33 to 34.

## [2026-04-09] ingest | broader web patterns for non-linear harness interfaces
- Added 14 raw source summaries:
  - raw/articles/sketch-n-sketch.md
  - raw/articles/glamorous-toolkit-moldable-development-environment.md
  - raw/papers/arxiv-omar-2018-live-functional-programming-with-typed-holes.md
  - raw/papers/arxiv-doderlein-2026-spacetime-programming.md
  - raw/articles/pernosco-omniscient-printf-debugging.md
  - raw/articles/plutojl-interactive-programming-environment.md
  - raw/articles/vistrails-aosa.md
  - raw/articles/spatial-hypertext.md
  - raw/articles/langgraph-studio-first-agent-ide.md
  - raw/articles/temporal-web-ui.md
  - raw/articles/windmill-suspend-approval-prompts.md
  - raw/articles/trigger-dev-product.md
  - raw/articles/airflow-ui-overview.md
  - raw/articles/dagster-scaling-dag-visualization.md
- Created 1 content page:
  - queries/web-patterns-for-non-linear-harness-interfaces.md
- Updated existing synthesis pages so the new material participates in the main interface graph:
  - queries/non-linear-interface-options-for-next-harness.md
- Updated index.md to include the new query and bump total pages from 34 to 35.

## [2026-04-09] ingest | under-explored coordination strategies arXiv pass
- Added 14 raw paper summaries:
  - raw/papers/arxiv-salemi-2025-llm-blackboard-data-discovery.md
  - raw/papers/arxiv-nakamura-2025-terrarium-blackboard-multi-agent-safety.md
  - raw/papers/arxiv-pugachev-2025-codecrdt-observation-driven-coordination.md
  - raw/papers/arxiv-duetting-2023-mechanism-design-large-language-models.md
  - raw/papers/arxiv-zhao-2025-llm-auction-generative-auction.md
  - raw/papers/arxiv-li-2025-lacp-agent-communication-protocol.md
  - raw/papers/arxiv-ehtesham-2025-survey-agent-interoperability-protocols.md
  - raw/papers/arxiv-ben-khaled-2026-g2cp-graph-grounded-communication-protocol.md
  - raw/papers/arxiv-zou-2025-blocka2a-secure-verifiable-interoperability.md
  - raw/papers/arxiv-miculicich-2025-veriguard-verified-code-generation.md
  - raw/papers/arxiv-ye-2025-x-mas-heterogeneous-llms.md
  - raw/papers/arxiv-yu-2025-dyntaskmas-dynamic-task-graph.md
  - raw/papers/arxiv-wang-2024-battleagentbench.md
  - raw/papers/arxiv-sun-2025-collab-overcooked.md
- Created 1 content page:
  - queries/arxiv-under-explored-coordination-strategies.md
- Updated existing synthesis pages so the new coordination material participates in the main graph:
  - concepts/non-hierarchical-coordination-patterns.md
  - concepts/orchestration-topologies.md
  - concepts/formal-methods-for-agent-harnesses.md
- Updated index.md to include the new query and bump total pages from 34 to 35.

## [2026-04-09] update | page-count recovery note
- The content-page total is 36, not 35.
- Two separate query-page ingests landed on 2026-04-09 (`queries/web-patterns-for-non-linear-harness-interfaces.md` and `queries/arxiv-under-explored-coordination-strategies.md`), so the later page-bump note undercounted by one.
- `index.md` now records the repaired total while preserving the earlier historical note as written.

## [2026-04-09] ingest | legacy distributed-systems ideas and studio architecture spec
- Added 11 raw source summaries:
  - raw/articles/virtual-synchrony.md
  - raw/articles/chandy-lamport-algorithm.md
  - raw/articles/vector-clock.md
  - raw/articles/failure-detector.md
  - raw/articles/jif.md
  - raw/articles/session-type.md
  - raw/articles/viewstamped-replication-revisited.md
  - raw/articles/optimistic-replication.md
  - raw/articles/self-certifying-file-system.md
  - raw/papers/session-guarantees-weakly-consistent-replicated-data.md
  - raw/papers/escrow-transactional-method.md
- Created 2 content pages:
  - queries/legacy-distributed-systems-ideas-for-moldable-operations-studio.md
  - queries/moldable-operations-studio-architecture-spec.md
- Updated existing synthesis pages so the new semantics layer participates in the main design graph:
  - queries/new-harness-design-notes.md
  - queries/web-patterns-for-non-linear-harness-interfaces.md
- Updated index.md to include the new queries and bump total pages from 36 to 38.

## [2026-04-09] lint | maintenance pass
- Ran `scripts/lint-wiki.sh` and a structural audit across the content corpus.
- Fixed invalid YAML frontmatter quoting in:
  - queries/arxiv-round-two-formal-semantics-for-agent-harnesses.md
  - queries/arxiv-under-explored-coordination-strategies.md
- Repaired inbound navigation for previously orphaned query pages by cross-linking them from:
  - concepts/formal-methods-for-agent-harnesses.md
  - concepts/formal-cognition-loop.md
  - concepts/non-hierarchical-coordination-patterns.md
- Hardened `scripts/lint-wiki.sh` to parse YAML frontmatter, so colon-bearing titles now fail fast instead of slipping past the shell-only checks.
- Re-ran lint: pass, 36 content pages checked, with no orphan content pages in the follow-up structural scan.

## [2026-04-09] update | staged lint polish
- Adjusted `scripts/lint-wiki.sh` so the `updated:` check inspects staged modified content pages when a commit is in flight, rather than only unstaged worktree edits.
- Limited that `updated:` rule to modified tracked pages (`--diff-filter=M`), so newly introduced historical pages can keep their original creation/update dates.
- Guarded the git-diff branch so staged-tree audits outside a git checkout do not emit misleading repo warnings.

## [2026-04-09] ingest | schema pass and sci-fi audit for moldable operations studio
- Added 11 raw source summaries:
  - raw/articles/star-trek-lcars.md
  - raw/articles/battlestar-galactica-dradis.md
  - raw/articles/minority-report-film.md
  - raw/articles/wargames.md
  - raw/articles/foundation-prime-radiant.md
  - raw/articles/machineries-of-empire.md
  - raw/articles/ancillary-justice.md
  - raw/articles/quantum-thief.md
  - raw/articles/embassytown.md
  - raw/articles/the-city-and-the-city.md
  - raw/articles/diaspora-novel.md
- Created 2 content pages:
  - queries/moldable-operations-studio-schema-pass.md
  - queries/sci-fi-audit-for-moldable-operations-studio.md
- Updated existing synthesis pages so the new concrete and speculative layers participate in the main design graph:
  - queries/moldable-operations-studio-architecture-spec.md
  - queries/web-patterns-for-non-linear-harness-interfaces.md
- Updated index.md to include the new queries and bump total pages from 38 to 40.
- Re-ran lint after the fix: pass.

## [2026-04-09] ingest | grounded research for moldable operations studio ideas
- Added 20 raw source summaries:
  - raw/papers/yang-wigdor-2014-panelrama.md
  - raw/papers/klokmose-et-al-2015-webstrates.md
  - raw/papers/bragdon-et-al-2011-code-space.md
  - raw/papers/danielsson-alvinius-larsson-2014-common-operating-picture.md
  - raw/papers/nandiganahalli-et-al-2014-mode-confusion-detection.md
  - raw/papers/honarmand-torrellas-2014-replay-debugging.md
  - raw/papers/ko-myers-2009-java-whyline.md
  - raw/papers/stasko-gorg-liu-2008-jigsaw.md
  - raw/papers/andrews-north-2012-analysts-workspace.md
  - raw/papers/groth-streefkerk-2006-provenance-annotation-visual-exploration.md
  - raw/papers/amershi-et-al-2015-modeltracker.md
  - raw/papers/wexler-et-al-2019-what-if-tool.md
  - raw/papers/malkhi-lamport-zhou-2008-stoppable-paxos.md
  - raw/articles/rfc-9420-mls-protocol.md
  - raw/articles/rivest-lampson-1996-sdsi.md
  - raw/papers/birgisson-et-al-2014-macaroons.md
  - raw/papers/efstathopoulos-et-al-2005-asbestos.md
  - raw/papers/finkelstein-et-al-1992-viewpoints.md
  - raw/papers/foster-et-al-2007-bidirectional-tree-transformations.md
  - raw/papers/green-karvounarakis-tannen-2007-provenance-semirings.md
- Created 1 content page:
  - queries/grounding-moldable-operations-studio-ideas-in-real-research.md
- Updated existing synthesis pages so the grounded-research layer participates in the main design graph:
  - queries/moldable-operations-studio-architecture-spec.md
  - queries/moldable-operations-studio-schema-pass.md
  - queries/sci-fi-audit-for-moldable-operations-studio.md
- Updated index.md to include the new query and bump total pages from 40 to 41.

## [2026-04-09] ingest | wireframe pass for moldable operations studio
- Added 1 asset:
  - raw/assets/moldable-operations-studio-wireframes.excalidraw
- Created 1 content page:
  - queries/moldable-operations-studio-wireframes.md
- Updated existing synthesis pages so the wireframe layer participates in the main design graph:
  - queries/moldable-operations-studio-architecture-spec.md
  - queries/moldable-operations-studio-schema-pass.md
  - queries/grounding-moldable-operations-studio-ideas-in-real-research.md
  - queries/sci-fi-audit-for-moldable-operations-studio.md
- Updated index.md to include the new query; total pages now 42.

## [2026-04-09] update | page-count recovery after concurrent studio additions
- The content-page total is 44, not 42.
- Concurrent additions landed in the corpus while the wireframe pass was in flight, including `concepts/self-evolving-workflows.md` and `queries/arxiv-self-evolving-workflows-for-codex-control-plane.md`.
- `index.md` now records the repaired total while preserving the earlier line-level history.

## [2026-04-09] ingest | self-evolving workflows for gas-city-but-its-just-codex
- Added 16 raw source summaries:
  - raw/articles/gas-city-but-its-just-codex-repo-2026-04-09.md
  - raw/papers/arxiv-zhang-2024-aflow.md
  - raw/papers/arxiv-li-2024-autoflow.md
  - raw/papers/arxiv-wang-2024-agent-workflow-memory.md
  - raw/papers/arxiv-hu-2024-automated-design-of-agentic-systems.md
  - raw/papers/arxiv-wang-2025-evoagentx.md
  - raw/papers/arxiv-wang-2026-learning-to-compose-agentic-workflow-generation.md
  - raw/papers/arxiv-xu-2026-hyevo.md
  - raw/papers/arxiv-zhao-2025-a2flow.md
  - raw/papers/arxiv-shen-2026-skillfoundry.md
  - raw/papers/arxiv-zhang-2026-evoskills.md
  - raw/papers/arxiv-wang-2026-skillx.md
  - raw/papers/arxiv-ma-2026-scaling-coding-agents-via-atomic-skills.md
  - raw/papers/arxiv-rhodes-2026-compiled-memory.md
  - raw/papers/arxiv-shinn-2023-reflexion.md
  - raw/papers/arxiv-zhao-2023-expel.md
- Created 2 content pages:
  - concepts/self-evolving-workflows.md
  - queries/arxiv-self-evolving-workflows-for-codex-control-plane.md
- Updated existing pages to connect the new workflow-evolution layer into the main graph:
  - queries/gas-city-but-its-just-codex.md
  - concepts/work-management-primitives.md
  - concepts/memory-persistence.md
- Updated index.md to include the new concept and query and bump total pages from 41 to 43.
- Re-ran lint after the ingest: pass, 43 content pages checked.

## [2026-04-09] ingest | broader arxiv sweep for self-evolving workflows
- Added 19 additional raw source summaries to widen the literature map beyond the first direct-hit pass:
  - raw/papers/arxiv-qiao-2024-benchmarking-agentic-workflow-generation.md
  - raw/papers/arxiv-zheng-2025-mermaidflow.md
  - raw/papers/arxiv-wang-2026-query-level-workflows.md
  - raw/papers/arxiv-ma-2026-judgeflow.md
  - raw/papers/arxiv-wang-2025-dyflow.md
  - raw/papers/arxiv-wang-2025-self-improving-agent-skill-library.md
  - raw/papers/arxiv-ye-2026-meta-context-engineering.md
  - raw/papers/arxiv-du-2025-bottom-up-skill-evolution.md
  - raw/papers/arxiv-zhai-2025-agentevolver.md
  - raw/papers/arxiv-qian-2025-metaagent.md
  - raw/papers/arxiv-banerjee-2026-severa.md
  - raw/papers/arxiv-ye-2025-sop-agent.md
  - raw/papers/arxiv-li-2025-sopbench.md
  - raw/papers/arxiv-huo-2026-atommem.md
  - raw/papers/arxiv-liu-2026-graph-of-skills.md
  - raw/papers/arxiv-ni-2026-trace2skill.md
  - raw/papers/arxiv-zhang-2026-memskill.md
  - raw/papers/arxiv-xia-2026-metaclaw.md
  - raw/papers/arxiv-xu-2025-robustflow.md
- Expanded the main synthesis pages so the literature map now includes evaluator loops, robustness, retrieval over large skill libraries, and learnable memory/context routines:
  - concepts/self-evolving-workflows.md
  - queries/arxiv-self-evolving-workflows-for-codex-control-plane.md
  - queries/gas-city-but-its-just-codex.md
  - index.md
- Re-ran lint after the broader sweep: pass, 43 content pages checked.

## [2026-04-09] ingest | rl gyms and executable environments for ai harnesses
- Added 20 raw source summaries for executable benchmark and training environments:
  - raw/papers/arxiv-zhou-2023-webarena.md
  - raw/papers/arxiv-chezelles-2024-browsergym-ecosystem.md
  - raw/papers/arxiv-koh-2024-visualwebarena.md
  - raw/papers/arxiv-drouin-2024-workarena.md
  - raw/papers/arxiv-boisvert-2024-workarena-plus-plus.md
  - raw/papers/arxiv-pan-2024-webcanvas.md
  - raw/papers/arxiv-xie-2024-osworld.md
  - raw/papers/arxiv-bonatti-2024-windows-agent-arena.md
  - raw/papers/arxiv-trivedi-2024-appworld.md
  - raw/papers/arxiv-ma-2024-agentboard.md
  - raw/papers/arxiv-xi-2024-agentgym.md
  - raw/papers/arxiv-nathani-2025-mlgym.md
  - raw/papers/arxiv-pan-2024-swe-gym.md
  - raw/papers/arxiv-yao-2024-tau-bench.md
  - raw/papers/arxiv-chuang-2026-proxy-state-based-evaluation.md
  - raw/papers/arxiv-chen-2025-rl-long-horizon-interactive-llm-agents.md
  - raw/papers/arxiv-lai-2025-computerrl.md
  - raw/papers/arxiv-mehta-2026-enterprisebench-corecraft.md
  - raw/papers/arxiv-mialon-2023-gaia.md
  - raw/papers/arxiv-yao-2022-webshop.md
- Created 1 content page:
  - queries/rl-gyms-and-executable-environments-for-ai-harnesses.md
- Updated existing concept pages so environment substrates connect back into the main harness graph:
  - concepts/evaluation-and-review-loops.md
  - concepts/harness-engineering.md
- Updated index.md to include the new query and corrected the total page count from 43 to 45 after a recount.
- Re-ran lint after the gym sweep: pass, 45 content pages checked.

## [2026-04-10] ingest | neural-native programming via internal-layer interfaces
- Added 35 raw source notes to resolve the user-provided NNPL draft into explicit bibliography entries:
  - raw/articles/neural-native-programming-direct-internal-layer-interfaces-draft-2026-04-10.md
  - raw/articles/transformer-circuits-mathematical-framework.md
  - raw/articles/logit-lens-lesswrong.md
  - raw/articles/anthropic-toy-models-of-superposition.md
  - raw/articles/anthropic-monosemantic-features.md
  - raw/articles/nnsight-docs.md
  - raw/articles/baukit-github.md
  - raw/articles/doug-github.md
  - raw/papers/arxiv-vaswani-2017-attention-is-all-you-need.md
  - raw/papers/geva-2021-transformer-feed-forward-layers-are-key-value-memories.md
  - raw/papers/arxiv-belrose-2023-tuned-lens.md
  - raw/papers/arxiv-hewitt-2019-structural-probe.md
  - raw/papers/arxiv-meng-2022-locating-and-editing-factual-associations-in-gpt.md
  - raw/papers/arxiv-turner-2023-steering-language-models-with-activation-engineering.md
  - raw/papers/arxiv-panickssery-2023-steering-llama-2-via-contrastive-activation-addition.md
  - raw/papers/arxiv-dathathri-2019-pplm.md
  - raw/papers/arxiv-wu-2024-pyvene.md
  - raw/papers/arxiv-li-2023-inference-time-intervention.md
  - raw/papers/arxiv-zou-2023-representation-engineering.md
  - raw/papers/arxiv-burns-2022-discovering-latent-knowledge.md
  - raw/papers/arxiv-hu-2021-lora.md
  - raw/papers/arxiv-reed-2015-neural-programmer-interpreters.md
  - raw/papers/arxiv-kusner-2017-grammar-variational-autoencoder.md
  - raw/papers/arxiv-van-den-oord-2017-neural-discrete-representation-learning.md
  - raw/papers/arxiv-hong-2020-latent-programmer.md
  - raw/papers/arxiv-macfarlane-2024-searching-latent-program-spaces.md
  - raw/papers/kanerva-2009-hyperdimensional-computing.md
  - raw/papers/plate-1995-holographic-reduced-representations.md
  - raw/papers/arxiv-gayler-2004-vector-symbolic-architectures.md
  - raw/papers/arxiv-weiss-2021-thinking-like-transformers.md
  - raw/papers/arxiv-lindner-2023-tracr.md
  - raw/papers/arxiv-tomkins-flanagan-2025-differentiable-vector-symbolic-types.md
  - raw/papers/arxiv-chen-2021-evaluating-llms-trained-on-code.md
  - raw/papers/arxiv-austin-2021-program-synthesis-with-large-language-models.md
  - raw/papers/arxiv-hendrycks-2021-measuring-coding-challenge-competence-with-apps.md
- Extended SCHEMA.md with `mechanistic-interpretability` and `program-synthesis` tags so the new material can be filed without abusing older categories.
- Created 2 content pages:
  - concepts/neural-native-programming.md
  - queries/neural-native-programming-via-direct-interfaces-to-transformer-internal-layers.md
- Updated existing synthesis pages so the new topic participates in the current harness graph:
  - concepts/formal-cognition-loop.md
  - queries/new-harness-design-notes.md
  - queries/non-linear-interface-options-for-next-harness.md
- Updated navigation/meta files:
  - SCHEMA.md
  - index.md

## [2026-04-10] lint | neural-native programming ingest maintenance pass
- Ran `scripts/lint-wiki.sh` after the ingest.
- Initial lint failed because several already-modified tracked pages still carried `updated: 2026-04-09` even though the worktree date had advanced.
- Bumped `updated` to 2026-04-10 on the following pages to restore schema consistency:
  - concepts/evaluation-and-review-loops.md
  - concepts/harness-engineering.md
  - concepts/memory-persistence.md
  - concepts/work-management-primitives.md
  - queries/gas-city-but-its-just-codex.md
  - queries/web-patterns-for-non-linear-harness-interfaces.md
- Re-ran lint: pass, 47 content pages checked.

## [2026-04-10] create | neural-native programming research program
- Added queries/neural-native-programming-research-program.md as a tighter staged plan with explicit promotion gates, kill criteria, benchmark order, and first-quarter deliverables.
- Cross-linked the new plan page from:
  - concepts/neural-native-programming.md
  - queries/neural-native-programming-via-direct-interfaces-to-transformer-internal-layers.md
- Updated index.md to include the new query and bump total pages from 47 to 48.

## [2026-04-10] lint | neural-native research-program follow-up
- Re-ran `scripts/lint-wiki.sh` after adding the research-program page.
- Result: pass, 48 content pages checked.

## [2026-04-10] ingest | rl gym entity pages and atropos fit analysis
- Added 2 repo-grounded raw source summaries for local harness integration state:
  - raw/articles/hermes-atropos-integration-2026-04-09.md
  - raw/articles/another-harness-repo-2026-04-09.md
- Created 21 entity pages for the executable-environment and gym layer:
  - entities/agentboard.md
  - entities/agentgym.md
  - entities/appworld.md
  - entities/atropos.md
  - entities/browsergym.md
  - entities/computer-rl.md
  - entities/enterprisebench-corecraft.md
  - entities/gaia.md
  - entities/mlgym.md
  - entities/osworld.md
  - entities/proxy-state-based-evaluation.md
  - entities/sopbench.md
  - entities/swe-gym.md
  - entities/tau-bench.md
  - entities/visualwebarena.md
  - entities/webarena.md
  - entities/webcanvas.md
  - entities/webshop.md
  - entities/windows-agent-arena.md
  - entities/workarena.md
  - entities/workarena-plus-plus.md
- Created 1 synthesis page:
  - queries/another-harness-and-atropos.md
- Updated the main gym synthesis and surrounding concept pages so the new environment layer participates in the harness graph:
  - queries/rl-gyms-and-executable-environments-for-ai-harnesses.md
  - concepts/evaluation-and-review-loops.md
  - concepts/harness-engineering.md
  - index.md
- Recounted content pages and updated index total from 48 to 70.
- Re-ran lint after the entity-page pass: pass, 70 content pages checked.

## [2026-04-10] update | public repo rename and github pages publishing layer
- Renamed the public GitHub repository from `wiki` to `agent-harness-wiki`.
- Added a lightweight MkDocs publishing layer with:
  - mkdocs.yml
  - docs-requirements.txt
  - scripts/prepare_site_docs.py
  - .github/workflows/pages.yml
  - README.md updates for local preview and published-site usage
  - .gitignore rules for generated site directories and local virtualenvs
- Verified the docs build locally after preparing the generated docs tree.
- Re-ran lint after the publishing-layer pass: pass, 70 content pages checked.
