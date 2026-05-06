---
title: "Spec Deep-Dive: Agent-Native, Spec Kit, and Kiro Cohort"
created: 2026-05-05
updated: 2026-05-05
type: query
tags: [survey, context-engineering, work-management, code-quality, benchmark]
sources: [queries/spec-deep-dive-wiki-ingest-project.md, queries/spec-dataset-evolution-research-project.md, queries/llm-readable-spec-files.md]
private_corpus_repo: https://github.com/ericfode/spec-dataset-evolution-corpus
kanban_task: SPEC-WIKI-03
raw_publication_mode: synthesis_plus_metadata
---

# Spec Deep-Dive: Agent-Native, Spec Kit, and Kiro Cohort

## Question

What does the private spec corpus show about agent-native specification systems:
`.kiro/specs`, Spec Kit / `.specify`, `cc-sdd`, prompt-template families,
and fast-moving AI-era repositories whose specs are schemas, protocols, commands,
or workflow contracts rather than a single `spec.md` file?

This page is one cohort slice of [[spec-deep-dive-wiki-ingest-project]] and
extends [[spec-dataset-evolution-research-project]]. It does not publish raw
corpus files. It uses the private corpus for synthesis, source paths, repository
URLs, commits, representative file paths, and caveats. The raw files can remain
where raw files belong: in the evidence store, not smeared across the public
window.

## Short answer

The agent-native cohort should be counted in two ledgers at once:

1. **Occurrence and adoption ledger.** Count every selected dossier occurrence,
   including forks, translations, tutorials, template copies, command prompts,
   `.kiro/specs` packets, `.specify` scaffolds, schemas, and generated examples.
2. **Independent authority ledger.** Count only rows that are canonical upstream
   authorities or edited project-local contracts. Template descendants and lab
   exercises remain evidence of propagation, but they should not inflate the
   number of independent specs.

Across the SPEC-WIKI-03 source slice, the template-lineage mapping covers 19
selected dossier occurrences from `SPEC-REPO-03`, `SPEC-REPO-04`, `SPEC-REPO-08`,
and `SPEC-REPO-11`. Fail-closed lineage mapping assigns them 14 independent
authority weights. That split is the main finding: agent-native specs are real
contracts often enough to matter, but their copied scaffolds are common enough
that file-count statistics alone are decorative arithmetic.

## Source basis

| Claim scope | Private corpus source | Public upstream reference | Evidence fields used | Caveat |
|---|---|---|---|---|
| `.kiro/specs` packets are edited project contracts in sampled product, infra, and agent-runtime repos. | `reports/deep-dives/SPEC-REPO-03/index.md`; per-repo JSON/Markdown dossiers; `reports/deep-dives/SPEC-REPO-20/template_lineage_mapping.jsonl` rows `SPEC-REPO-03::*` | `https://github.com/Unson-LLC/brainbase`, `https://github.com/eibrahim/freeresend`, `https://github.com/fivexl/terraform-aws-sso-elevator`, `https://github.com/zavora-ai/adk-rust` | `repo_url`, `inspected_commit`, `.kiro/specs/**` paths, `ratios.*`, `connectedness.*`, `compliance.*`, `authority_origin` | AI-era timing is a discovery/timestamp label, not proof that a model generated the specs. |
| Spec Kit is both an upstream control plane and a downstream project-spec style. | `reports/deep-dives/SPEC-REPO-04/index.md`; `reports/deep-dives/SPEC-REPO-11/index.md`; `reports/deep-dives/SPEC-REPO-20/TEMPLATE_LINEAGE_MODEL.md` | `https://github.com/github/spec-kit`, `https://github.com/chenziyang110/spec-kit-plus`, `https://github.com/eitatech/gatomia-vscode`, `https://github.com/fancy-bread/bureau`, `https://github.com/ganesh-nagarkoti/specDrivenQAPlaywrightHeliumFramework` | `artifact_references`, `ratios`, `history`, `connectedness`, `authority_origin`, `upstream_template_repo`, `duplicate_of_record_id` | `github/spec-kit` appears in multiple cohorts but contributes one canonical upstream template authority. |
| Forks, translations, tutorials, and prompt templates create duplicate inflation. | `reports/deep-dives/SPEC-REPO-11/index.md`; `reports/deep-dives/SPEC-REPO-20/TEMPLATE_LINEAGE_MODEL.md` | `https://github.com/888888888881/spec-kit-chinese`, `https://github.com/Azure-Samples/TechConnect-2026-LAB-1073-Building-intelligent-multi-agent-Apps-with-GH-Speckit-and-Agent-Framework`, `https://github.com/KhazP/vibe-coding-prompt-template`, `https://github.com/gotalab/cc-sdd` | duplicate/canonicalization table, `template_family`, `fork_or_translation`, `tutorial_or_lab`, `generated_scaffold`, `edited_project_contract` | These are useful adoption and lineage evidence; only some are independent project authority. |
| Fast-growing AI-era repos use spec-like contracts without necessarily using a spec-directory workflow. | `reports/deep-dives/SPEC-REPO-08/index.md`; per-repo JSON/Markdown dossiers; lineage rows `SPEC-REPO-08::*` | `https://github.com/openai/codex`, `https://github.com/google-gemini/gemini-cli`, `https://github.com/anomalyco/opencode`, `https://github.com/modelcontextprotocol/modelcontextprotocol`, `https://github.com/github/spec-kit` | `spec_inventory`, schema/proto/OpenAPI paths, `clone_mode`, `stars`, `forks`, `ratios.spec_loc_per_kloc`, `history` | Current popularity counters are pressure markers only; they are not historical causal timelines. |

## Cohort ledger

| Source cohort | What was selected | Main artifact class | Lineage interpretation |
|---|---:|---|---|
| `SPEC-REPO-03` | 4 repositories | `.kiro/specs` requirements/design/tasks packets | All four are `edited_project_contract` rows in `kiro-agent-native`; scaffolded form, project-local authority. |
| `SPEC-REPO-04` | 5 repositories | Spec Kit / `.specify` upstream, forks, and consumers | One canonical upstream template; three edited consumer contracts; one derivative fork/extension. |
| `SPEC-REPO-08` | 5 repositories | AI-era fast-growing repos, schemas, protocols, specs-as-product | Three project contract rows, one normative standard row, and a duplicate Spec Kit occurrence. |
| `SPEC-REPO-11` | 5 repositories | forks, translations, tutorials, `cc-sdd`, prompt-template families | Deliberately biased duplicate-inflation sample: translation, lab, prompt template, workflow template, and duplicate upstream occurrence. |
| `SPEC-REPO-20` | 55-row lineage mapping; 19 relevant here | template/fork/generated-scaffold normalization | Relevant slice: 19 occurrences, 15 generated-scaffold rows, 11 edited-project-contract rows, 14 fail-closed independent-authority weights. |

## Evidence table

| Family | Repository | Authority class | Commit / representative paths | Public-safe interpretation |
|---|---|---|---|---|
| Kiro agent-native | `Unson-LLC/brainbase` | edited project contract | `678d4211bbb2`; `.kiro/specs/kiro-task-activation/requirements.md`, `.kiro/specs/schedule-kiro-migration/design.md` | Mature app: Kiro specs bind UI CRUD and scheduling work to services, tests, and event paths. |
| Kiro agent-native | `eibrahim/freeresend` | edited project contract | `3439985c3d9f`; `.kiro/specs/hosted-version-waitlist/{requirements,design,tasks}.md` | Small product app: waitlist and pricing spec connects product behavior, database/API shape, and UX. |
| Kiro agent-native | `fivexl/terraform-aws-sso-elevator` | edited project contract | `a224610c1449`; `.kiro/specs/attribute-based-group-sync/*`, `.kiro/specs/config-s3-migration/*` | Infrastructure module: specs capture Lambda/S3/IAM migration and group-sync pressure. |
| Kiro agent-native | `zavora-ai/adk-rust` | edited project contract; metadata-only raw redistribution | `2cc498cf36f0`; `.kiro/specs/adk-payments/*`, `docs/roadmap/adk-spatial-os-requirements.md` | Large Rust workspace: useful cross-crate commerce-contract evidence; raw excerpts stay blocked by NOASSERTION / metadata-only posture. |
| Spec Kit upstream | `github/spec-kit` | canonical upstream template | `0d8685aa80e2`; `templates/spec-template.md`, `templates/commands/{plan,specify,tasks}.md` | Source of the `.specify` grammar: command prompts, templates, hooks, tests, and process docs are the contract surface. |
| Spec Kit derivative | `chenziyang110/spec-kit-plus` | derived template fork/extension | `2127e1d36cc5`; `templates/spec-template.md`, `templates/commands/specify.md`, passive-skill templates | Extension lab; occurrence evidence for lineage, not independent project authority by default. |
| Spec Kit consumer | `eitatech/gatomia-vscode` | edited project contract | `acad55191c58`; `specs/001-devin-integration/spec.md`, `specs/002-hooks-module/spec.md` | VS Code extension using feature-spec bundles; project authority while preserving Spec Kit lineage. |
| Spec Kit consumer | `fancy-bread/bureau` | edited project contract | `2e07e5b1c66f`; `specs/001-autonomous-runtime-core/spec.md`, `specs/006-tasks-md-driven/spec.md` | Autonomous development runtime gated by Spec Kit-like specs; young but directly project-bound. |
| Spec Kit adoption burst | `ganesh-nagarkoti/specDrivenQAPlaywrightHeliumFramework` | edited project contract; review required | `940300dc6802`; `.specify/templates/spec-template.md`, `specs/login/spec.md` | Adoption snapshot with weak longitudinal evidence; useful, but license/redistribution status fails closed for raw content. |
| AI-era protocol/spec | `modelcontextprotocol/modelcontextprotocol` | normative standard | `6523895fcdc4`; `docs/specification/*/*.mdx` | Protocol repository where the spec is the product; NOASSERTION/mixed-license status means raw redistribution needs review. |
| AI-era product contract | `openai/codex` | edited project contract | `4950e7d8a67a`; `codex-rs/core/config.schema.json`, `codex.thread_store.v1.proto` | Fast-moving terminal-agent repo: schema/proto files stabilize behavior even without a Kiro/Spec Kit workflow. |
| AI-era product contract | `google-gemini/gemini-cli` | edited project contract | `8f0edcd64fc7`; `schemas/settings.schema.json` | High-pressure agent CLI with a settings schema as the principal accepted spec-like contract. |
| AI-era product contract | `anomalyco/opencode` | edited project contract | `84afd2bef8d1`; `packages/opencode/specs/effect/*.md`, OpenAPI/SDK schemas | Specs-as-islands in a large product repo; strong project authority but not a generated scaffold family. |
| Spec Kit translation | `888888888881/spec-kit-chinese` | derived template fork/translation | `e12f36a182df`; `.cursor/commands/speckit.{clarify,specify}.md` | Near-duplicate/translation specimen; count occurrence and localization, not a new independent authority. |
| Spec Kit tutorial/lab | `Azure-Samples/TechConnect-2026-LAB-1073-Building-intelligent-multi-agent-Apps-with-GH-Speckit-and-Agent-Framework` | tutorial or lab | `d3bc15c279c7`; `.specify/templates/*`, `.github/agents/speckit.*.agent.md`, lab specs | Pedagogical propagation evidence; excellent for template-lineage analysis, poor as independent project authority. |
| Prompt template | `KhazP/vibe-coding-prompt-template` | prompt-template authority | `e063721c7917`; `.claude/skills/vibe-*/SKILL.md`, PRD/design prompt files | Count once as reusable prompt/process template authority, not as an app-local project contract. |
| Workflow template | `gotalab/cc-sdd` | workflow-template authority | `29aee950f4ad`; `.kiro/specs/*`, `tools/cc-sdd/templates/shared/settings/templates/specs/*` | Non-Spec-Kit Kiro/cc-sdd workflow authority with live examples; scaffolded and edited, but counted as one workflow authority. |

## What the distinction buys us

### Template lineage is not noise

Spec Kit, Kiro, `cc-sdd`, Agent OS-style workflows, and prompt templates all make
agent-facing specification more regular. That regularity is useful to builders
and to crawlers. It is also dangerous to naive statistics: a copied
`tasks-template.md` and an edited product requirement can look equally
"spec-like" to a scorer.

The lineage model therefore records fields such as `authority_origin`,
`template_family`, `upstream_template_repo`, `fork_or_translation`,
`tutorial_or_lab`, `generated_scaffold`, and `edited_project_contract`. This is
not bookkeeping fussiness. It is the difference between measuring design
practice and measuring how many times a template went for a walk.

### Generated scaffolds can still be real contracts

Generated form is not disqualifying. The Kiro rows in `SPEC-REPO-03` and several
Spec Kit consumer rows in `SPEC-REPO-04` are both `generated_scaffold = true` and
`edited_project_contract = true` in the lineage mapping. They are scaffolded
because the shape comes from a workflow family; they are still project contracts
because the content is edited around implementation, product, API, test, or
infrastructure surfaces.

This connects directly to [[llm-readable-spec-files]]: regular structure helps
agents, but only when there is project-local authority and verification pressure
behind it.

### AI-era fast growth changes the surface, not the proof standard

`openai/codex`, `google-gemini/gemini-cli`, and `anomalyco/opencode` do not need
`.kiro/specs` to be relevant. Their spec-like artifacts include JSON schemas,
Proto definitions, OpenAPI documents, configuration contracts, and effect-system
notes. Those are legitimate specification surfaces, especially when same-commit
or path-level evidence connects them to implementation.

The pressure claims remain deliberately modest. Current stars, forks, issues,
and repository activity are pressure indicators in the preserved dossiers; they
are not a longitudinal causal story. The project can study pressure later with a
proper time series. Today we keep the ontology clean. It is cheaper than
apologizing to it later.

## Negative evidence and uncertainty

- `SPEC-REPO-03` records that `web_search` failed because Firecrawl was not
  configured, GitHub unauthenticated code search failed with HTTP 401, and the
  workflow proceeded through Sourcegraph/public clone inspection.
- `SPEC-REPO-04` records 63 candidate rows: 5 selected and 58 rejected/probed.
  Broad `spec-kit` search was noisy, with star-list/readme aggregators and other
  false positives preserved in `candidates.jsonl`.
- `SPEC-REPO-08` used blobless partial clones for large repositories such as
  `openai/codex`, `google-gemini/gemini-cli`, and `anomalyco/opencode`; full
  historical blob materialization remains a narrower follow-up task.
- `SPEC-REPO-11` is intentionally biased toward duplicate inflation. Its purpose
  is not prevalence estimation but classifier calibration and canonicalization
  failure discovery.
- The template-lineage model cites Agent OS as an adjacent scaffold family from
  the broader 55-row mapping, including `SPEC-REPO-10::tylerdotai/agent-os`; this
  page treats it as lineage context, not as a main `SPEC-WIKI-03` selected row.
- Raw export remains blocked or review-required for rows with missing,
  NOASSERTION, mixed-license, partial-scan, or metadata-only evidence. This page
  uses no long direct excerpts.

## Public-safety and compliance posture

Publication mode for this page is `synthesis_plus_metadata`. It names public
repository URLs, commits, file paths, corpus-relative dossier paths, aggregate
counts, and lineage classifications. It does not copy private raw corpus bodies
or long upstream passages.

Rows with explicit or effective raw-content restrictions include:

- `zavora-ai/adk-rust`: NOASSERTION / `metadata_only` posture in
  `SPEC-REPO-03`.
- `ganesh-nagarkoti/specDrivenQAPlaywrightHeliumFramework`: missing license / raw
  content `review_required` in `SPEC-REPO-04`.
- `modelcontextprotocol/modelcontextprotocol`: mixed transition / NOASSERTION,
  `review_required` in `SPEC-REPO-08`.
- `SPEC-REPO-11` selected rows: dossier policy says metadata-only or
  review-required for content, with short excerpts in the private dossier only.

For downstream synthesis, use this page as a public-safe map of evidence and
caveats, not as a replacement for the underlying private dossier records.

## Implications for the dataset

1. Store both occurrence counts and independent-authority counts. They answer
   different questions.
2. Keep `template_family` first-class for Spec Kit, Kiro/cc-sdd, Agent OS,
   prompt-template, and future agent-skill scaffold families.
3. Treat `generated_scaffold && edited_project_contract` as valuable project
   evidence, not a false positive.
4. Treat `generated_scaffold && !edited_project_contract`, fork/translation, and
   tutorial/lab rows as propagation evidence unless a later review proves
   independent normative edits.
5. For fast-growing AI-era repos, include schema/protocol/config surfaces in the
   spec taxonomy and connect them to [[evaluation-and-review-loops]] and
   [[work-management-primitives]] by evidence type rather than filename romance.

## See also

- [[spec-deep-dive-wiki-ingest-project]]
- [[spec-dataset-evolution-research-project]]
- [[llm-readable-spec-files]]
- [[context-engineering]]
- [[evaluation-and-review-loops]]
- [[work-management-primitives]]

## Deep-dive navigation

- Aggregate index: [[spec-deep-dive-index]]
- Priority cases: [[spec-deep-dive-case-jcode]], [[spec-deep-dive-case-droidagent]], [[spec-deep-dive-case-j8-ambiguity]]
- Cohort pages: [[spec-deep-dive-cohort-exact-spec-md-and-standards]], [[spec-deep-dive-cohort-agent-native-spec-kit-kiro]], [[spec-deep-dive-cohort-rfc-adr-executable-contracts]]
