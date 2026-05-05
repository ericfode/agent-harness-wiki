---
title: Spec dataset evolution Kanban design raw notes
author: Hermes Kanban design pass with three specialist subagent lenses
date: 2026-05-04
accessed: 2026-05-04
ingested: 2026-05-04
---

# Spec Dataset Evolution Kanban Design Raw Notes

Context: design pass for `queries/spec-dataset-evolution-research-project.md`
and Hermes Kanban board `spec-dataset-evolution`.

## Source lanes used

Three independent specialist lanes were asked to design Kanban-ready guidance:

1. Discovery and corpus construction.
2. Longitudinal change analysis.
3. Code-to-spec ratio and connectedness analysis.

The web tool available to those subagents reported missing Firecrawl
configuration, so these are methodology notes rather than externally-grounded web
citations. They are still useful as design priors, but any implementation task
that relies on forge API limits or syntax should verify against current platform
docs.

## Discovery and corpus construction notes

Recommended positive patterns:

- Exact filenames: `spec.md`, `SPEC.md`, `specs.md`, `specification.md`,
  `requirements.md`, `prd.md`, `design.md`, `architecture.md`.
- Variant names: `technical-spec*.md`, `functional-spec*.md`,
  `product-requirements*.md`, `software-requirements*.md`, `user-stories.md`.
- Directories: `docs/specs/**`, `specs/**`, `requirements/**`, `rfcs/**`,
  `adr/**`.
- Agent-era directories: `.kiro/specs/**`, `.agent-os/specs/**`, `.claude/**`,
  `.cursor/**` when the content is requirements/design/task specification.

Recommended exclusions:

- Test files: `*.spec.ts`, `*.spec.js`, `*.spec.jsx`, `*.spec.rb`, etc.
- Packaging specs: `.rpm.spec`, `.nuspec`, `.podspec`, unless explicitly studied.
- API schema files unless the project decides to include executable contract specs.

Discovery should combine:

- search-first queries for exact filename/path/content matches;
- repository enumeration plus tree inspection for recall;
- query slicing by date, stars, language, extension, and owner/repo range to
  avoid search caps;
- checkpointed pagination, backoff, ETags, and idempotent fetches.

Every artifact should preserve a stable reference:

- `repo_url`;
- `file_url` using an immutable commit SHA;
- `raw_url` when available;
- `commit_sha`;
- `path`;
- `content_sha256` and normalized hash;
- `matched_query` and match type.

## Longitudinal change analysis notes

Primary tables:

- `spec_lineages`: one row per logical spec document across renames/moves.
- `spec_revisions`: one row per commit changing a spec.
- `spec_snapshots`: one row per material version.
- `repo_time_buckets`: monthly/quarterly repo pressure features.
- `event_timeline`: star bursts, releases, code churn spikes, dependency,
  security, AI-feature, and collaboration events.

Recommended metrics:

- line/word churn;
- normalized edit distance;
- heading and section deltas;
- requirement-like sentence changes;
- rewrite flag;
- months between changes;
- burstiness;
- spec half-life;
- time to first major change;
- dormant/reactivated/deleted/replaced labels.

Recommended AI-era labels:

- primary cutoff: ChatGPT launch, 2022-11-30;
- sensitivity: GitHub Copilot technical preview, 2021-06-29;
- sensitivity: GPT-4 launch, 2023-03-14;
- separate repo birth era, spec birth era, pre/post exposure months, and
  AI-related content signals.

Pressure families:

- popularity/adoption: stars, forks, star bursts;
- development: code churn, changed files, refactors;
- collaboration/community: contributors, issues, PRs;
- release: tags/releases, major release windows;
- dependency/ecosystem: package/dependency file changes;
- security/compliance: advisories, CVEs, security sections;
- AI: AI feature/code/spec signals.

## Code-to-spec ratio and connectedness notes

Artifact classifiers should distinguish:

- `spec`;
- `code`;
- `test`;
- `docs`;
- `generated`;
- `vendor`;
- `other`.

Primary ratio features:

- spec/code file count;
- spec/code LOC;
- spec/code tokens;
- spec files per KLOC;
- executable contract ratio;
- test/spec and docs/code baselines.

Connectedness evidence:

- direct Markdown links from specs to code;
- code comments/docstrings linking to specs/RFCs/ADRs/issues/requirement IDs;
- path proximity and module-local specs;
- same-commit and rolling-window spec/code co-change;
- issue/PR linkage and labels;
- symbol/API/schema/config/CLI flag matching;
- test/spec linkage;
- typed documentation graph edges.

Graph node types:

- repo, file, symbol, spec section, test, issue, pull request, commit, release,
  label, maintainer.

Graph edge types:

- references, mentions_symbol, implements, tests, changes, co_changes,
  linked_issue, review_discusses, same_directory, semantic_match,
  generated_from.

Important validation checks:

- preserve edge evidence;
- count broken links separately;
- flag ambiguous symbol matches;
- handle merge and mechanical formatting commits consistently;
- sample high-confidence and low-confidence edges for manual audit.

## Design caveat

These notes intentionally avoid claiming causality from observed temporal
association. The project can ask whether pressures precede spec changes; it
cannot simply announce that stars “caused” a spec rewrite because a lag variable
looked handsome in a regression table.
