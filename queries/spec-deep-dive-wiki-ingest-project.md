---
title: Spec Deep-Dive Wiki Ingest Project
created: 2026-05-05
updated: 2026-05-05
type: query
tags: [survey, work-management, context-engineering, code-quality, formal-methods]
sources: [queries/spec-dataset-evolution-research-project.md, raw/articles/spec-dataset-evolution-kanban-error-repair-2026-05-05.md]
kanban_board: spec-deep-dive-wiki-ingest
private_corpus_repo: https://github.com/ericfode/spec-dataset-evolution-corpus
---

# Spec Deep-Dive Wiki Ingest Project

## Question

How should the private `spec-dataset-evolution-corpus` repository be turned into
public-safe wiki knowledge without dumping raw copied specs into the public wiki?

This is a continuation of [[spec-dataset-evolution-research-project]]. The private
corpus is a working archive; the wiki should receive synthesis, source-grounded
deep dives, cohort maps, and explicit caveats. Raw specs stay in the private
repository unless an export gate says otherwise. Neat archive, clean window.

## Current private corpus

Private GitHub repository:

- `https://github.com/ericfode/spec-dataset-evolution-corpus`

Local checkout:

- `/Users/ericfode/src/spec-dataset-evolution-corpus`

Inspected state for `SPEC-WIKI-00`:

- Local corpus checkout `git status --short`: clean.
- Local corpus checkout `git rev-parse --short HEAD`: `4659608`.
- `reports/deep-dives/`: 207 files, including 103 Markdown files, 87 JSON files,
  and 17 JSONL files.
- `reports/AGGREGATE.md` and `reports/deep-dives/AGGREGATE.md`: aggregate digest
  `sha256[:12] = 76c912ddb1e3`.
- `data/corpus_file_manifest.jsonl`: 1,741 artifact occurrence rows, 1,676 private
  raw-file copies, and 65 metadata-only or hard-quarantined raw rows.
- `data/aggregate_repo_records.jsonl`: 55 selected dossier occurrences across 51
  unique public repositories.
- `data/connectedness_features.jsonl`: 55 connectedness feature rows.

The private repository is intentionally not a public release. Its raw files retain
upstream licenses and copyright context; the public wiki should not copy them
wholesale. The publication boundary is therefore: **synthesis and provenance out;
raw corpus files stay in**.

## Source map

The source map below is the contract for downstream `SPEC-WIKI-*` tasks. Paths are
corpus-relative unless an absolute project scratch path is explicitly named.

| Source surface | What it proves | Public-safe use | Hard limits |
|---|---|---|---|
| `PROJECT_BRIEF.md` in the project scratch directory | Board purpose, intended outputs, source surfaces, and publication boundary. | Cite as the local project brief in Kanban handoffs; use it to keep the ingest scope stable. | Do not treat it as evidence about upstream repos. |
| `reports/deep-dives/jcode.md` and `reports/deep-dives/jcode-analysis.json` | Priority case study for `1jehuang/jcode`, including source basis, spec inventory, churn, pressure, and code/spec connectedness. | Synthesize a case page; preserve `https://github.com/1jehuang/jcode` and cited commit/path evidence. | Do not paste the dossier wholesale; do not copy private raw corpus files. |
| `reports/deep-dives/droidagent.md` | Priority case study for `coinse/droidagent`, including retrieval notes, repo chronology, requirements, architecture, and memory model. | Synthesize a case page with repo URL, inspected paths, and caveats. | Keep runtime/setup details descriptive; do not launder raw repo text into the wiki. |
| `reports/deep-dives/j8-agent.md` | J8/J8Spec ambiguity trail, including the distinction between `j8agent` and `j8spec/j8spec`. | Create a public-safe ambiguity/correction section that names the namespace uncertainty and final inspected repo. | Do not overstate identity resolution beyond the dossier evidence. |
| `reports/deep-dives/SPEC-REPO-01..12/` | Whole-repo scout cohorts: exact `spec.md`, requirements/design, agent-native specs, Spec Kit, RFC/ADR, executable contracts, mature baselines, AI-era repos, low-star samples, non-GitHub forges, templates/forks, and negative controls. | Use `index.md`, `sources.md`, `candidates.jsonl`, and per-repo dossier Markdown/JSON pairs to build cohort pages. Preserve repo URLs, commit SHAs, file paths, selected/rejected status, and negative evidence. | Do not flatten cohorts into one generic “spec” label; do not omit rejected candidates and search failures when they shape interpretation. |
| `reports/deep-dives/AGGREGATE.md` and `reports/AGGREGATE.md` | Aggregate counts, cohort yield, artifact classes, duplicate/template clusters, ratio regimes, connectedness patterns, pressure patterns, schema changes, and case-study carry-forward list. | Use for the public deep-dive index and cohort summaries. Prefer aggregate numbers and short paraphrases. | Do not treat aggregate snippets as a substitute for per-dossier source checks on individual claims. |
| `data/corpus_file_manifest.jsonl` | Artifact occurrence metadata: cohort, doc type, repo URL, inspected commit, private raw path, normalized cluster, authority origin, and raw-inclusion status. | Use for counts, source path preservation, doc-type summaries, and fail-closed raw-export checks. | Never publish raw bytes from `corpus/by_repo/`; private raw paths are provenance, not public content. |
| `data/aggregate_repo_records.jsonl` | Repo-level records with artifact inventories, compliance fields, clone/history coverage, connectedness, pressure, ratios, and source-path provenance. | Use as the main structured source for per-repo evidence tables. Include `repo_url`, `repo_full_name`, source dossier path, compliance status, and caveats. | Do not collapse nested compliance fields into a single permissive label. Missing or ambiguous fields fail closed. |
| `data/connectedness_features.jsonl` | Typed connectedness flags and missingness for direct links, reverse backrefs, path/symbol mentions, test linkage, and co-change. | Use for connectedness summaries and evidence-type tables. | Do not claim causality from connectedness flags; they are evidence categories, not proofs of governance. |
| `reports/deep-dives/SPEC-REPO-16/COMPLIANCE_EXPORT_GATE.md` and `compliance_export_gate.*` | Public raw-content export gate design and per-record compliance policy. | Use to decide whether a downstream page may include a quoted excerpt at all. | Any missing license, flagged scan, internal/private-LAN signal, or unclear raw-content right means metadata-only or review-required. |
| `reports/deep-dives/SPEC-REPO-17/PRESSURE_EVIDENCE_REVIEW.md` | Pressure metric caveats and causality lint. | Use to phrase pressure claims as associations with evidence limits. | No historical pressure timeline claim without a proper time-series source. |
| `reports/deep-dives/SPEC-REPO-20/TEMPLATE_LINEAGE_MODEL.md` and `template_lineage_*` | Template, fork, tutorial, and generated-scaffold lineage model. | Use to separate canonical authority from copied or generated descendants. | Do not count template descendants as independent evidence without a lineage caveat. |
| `queries/spec-dataset-evolution-research-project.md` | Public research frame, dataset units, discovery patterns, schema sketch, and Kanban design. | Link from all public pages as the project root. | Do not rewrite the public research question in each page; link back and state the local slice. |

## Downstream task source routing

| Downstream task | Primary sources | Expected public output |
|---|---|---|
| `SPEC-WIKI-01` priority cases | `jcode.md`, `jcode-analysis.json`, `droidagent.md`, `j8-agent.md` | Case-study page or sections for `jcode`, DroidAgent, and the J8/J8Spec ambiguity trail. |
| `SPEC-WIKI-02` exact `spec.md` and mature standards | `SPEC-REPO-01`, `SPEC-REPO-07`, `SPEC-REPO-18`, `SPEC-REPO-19`, aggregate records | Cohort page distinguishing exact `spec.md`, standards/protocol repos, and mature baselines. |
| `SPEC-WIKI-03` agent-native / Spec Kit / Kiro | `SPEC-REPO-03`, `SPEC-REPO-04`, `SPEC-REPO-08`, `SPEC-REPO-11`, `SPEC-REPO-20` | Cohort page for `.kiro`, `.agent-os`, `.specify`, Spec Kit, templates, and generated scaffolds. |
| `SPEC-WIKI-04` RFC / ADR / executable contracts | `SPEC-REPO-05`, `SPEC-REPO-06`, `SPEC-REPO-18`, `SPEC-REPO-19`, connectedness features | Cohort page separating prose governance corpora from machine-readable contracts. |
| `SPEC-WIKI-05` aggregate index | `AGGREGATE.md`, `aggregate_repo_records.jsonl`, `corpus_file_manifest.jsonl`, all cohort pages | Public-safe index page with source map, cohort links, top findings, caveats, and remaining gates. |
| `SPEC-WIKI-06` public-safety review | All wiki pages produced by the ingest wave plus `SPEC-REPO-16` compliance gate | Review page or handoff confirming lint, public-safety policy adherence, and push verification. |

## Naming conventions

Use stable, boring names. Boring names are a gift to future grep.

- Project anchor: `queries/spec-deep-dive-wiki-ingest-project.md`.
- Aggregate public index: `queries/spec-deep-dive-index.md`.
- Priority case pages, if split out:
  - `queries/spec-deep-dive-case-jcode.md`
  - `queries/spec-deep-dive-case-droidagent.md`
  - `queries/spec-deep-dive-case-j8-ambiguity.md`
- Cohort pages, if split out:
  - `queries/spec-deep-dive-cohort-exact-spec-md-and-standards.md`
  - `queries/spec-deep-dive-cohort-agent-native-spec-kit-kiro.md`
  - `queries/spec-deep-dive-cohort-rfc-adr-executable-contracts.md`
- Raw wiki notes are optional and should only summarize a source; never store raw
  private corpus files under `raw/`. If a raw note is needed, name it
  `raw/articles/spec-deep-dive-<topic>-source-note-2026-05-05.md` and keep it
  paraphrased.
- Every new content page must be added to [[index]] and must use `type: query`
  while it lives under `queries/`.
- Use the visible page title form `Spec Deep-Dive: <topic>` for pages in this
  ingest wave.

## Citation style

Each page produced from the private corpus should contain a `Source basis` section
near the top with this shape:

| Claim scope | Private corpus source | Public upstream reference | Evidence fields used | Caveat |
|---|---|---|---|---|
| One sentence naming the claim | Corpus-relative path such as `reports/deep-dives/SPEC-REPO-08/openai__codex.json` | Repo URL plus commit/file path when available | `repo_url`, `inspected_commit`, `file_path`, `doc_type`, `connectedness.flags`, `compliance.*` | Missingness, rate limit, license, or ambiguity note |

Rules:

1. Prefer corpus-relative paths over absolute local paths in public prose.
2. Preserve public repo URLs exactly when they are available.
3. Preserve commit SHAs and file paths when the source record provides them.
4. Cite source rows by dossier path plus row identity when a JSONL row is the
   evidence. Example: `data/aggregate_repo_records.jsonl` row for
   `openai/codex`, sourced from `reports/deep-dives/SPEC-REPO-08/openai__codex.json`.
5. Treat negative evidence as citable evidence: failed GitHub code search, API
   rate limits, missing license fields, partial clone coverage, and rejected
   candidates should appear when they constrain the claim.
6. Keep [[llm-readable-spec-files]], [[context-engineering]],
   [[work-management-primitives]], and [[evaluation-and-review-loops]] as conceptual
   links, not substitutes for corpus evidence.

## Excerpt policy

Default publication mode is synthesis plus metadata. Direct quotation is an
exception, not a decorating habit.

Allowed:

- Short excerpts from public upstream files when needed to explain a classification
  or ambiguity.
- Quoted field names, file paths, repo names, command names, and stable IDs.
- Aggregate numbers, paraphrased findings, and evidence tables derived from private
  JSON/JSONL records.

Limits:

- No wholesale raw corpus files in the wiki.
- No copied private `corpus/by_repo/` file bodies.
- No excerpt from a record with `metadata_only`, `review_required`, flagged secret
  or PII scan, unclear license, internal/private-LAN signal, or missing scan evidence
  unless a human reviewer explicitly approves it in a later task.
- Keep ordinary excerpts to at most 25 words each and at most three excerpts per
  upstream repository on a single page. If the claim needs more than that, the page
  should summarize and link to the public upstream repository instead.
- Every excerpt must have a nearby citation row naming corpus-relative path, public
  repo URL, file path, and commit or retrieval basis when available.
- Do not publish secrets, tokens, private emails, private local-only URLs, raw PII,
  or screenshots of private corpus content. Placeholder-looking secrets must still
  be classified as placeholder before quotation.

## Public-safety ingest policy

Wiki pages may include:

- synthesis of the deep-dive dossiers;
- repository URLs, commit SHAs, paths, and stable source references;
- short excerpts only under the excerpt policy above;
- caveats about missing metadata, API limits, license review, clone coverage, and
  manual-audit status;
- links back to [[spec-dataset-evolution-research-project]],
  [[llm-readable-spec-files]], [[context-engineering]],
  [[work-management-primitives]], and [[evaluation-and-review-loops]].

Wiki pages must not include:

- bulk raw spec contents;
- unreviewed long copied excerpts;
- private raw corpus file bodies;
- claims that a post-ChatGPT timestamp proves AI generation;
- current-star snapshots presented as historical pressure timelines;
- flattened “spec” labels that erase templates, executable contracts, RFCs,
  negative controls, and package/test lookalikes;
- compliance shortcuts that treat `allowed_pending_policy_review` as unrestricted
  raw-export permission.

Fail-closed publication gates:

1. If license or redistribution status is missing or unclear, publish metadata and
   synthesis only.
2. If secret/PII/internal scan status is flagged, missing, or only spot-checked,
   publish metadata and synthesis only unless the page explicitly records why a
   short excerpt is safe.
3. If clone/history coverage is partial, preserve the limitation next to any churn,
   pressure, or connectedness claim.
4. If a repo is a fork, template, tutorial, translation, generated scaffold, or
   downstream Spec Kit consumer, label its authority origin before using it as
   independent evidence.
5. If a finding depends on failed or rate-limited search, cite the failure as
   negative evidence and avoid recall-completeness claims.

## Acceptance criteria for downstream pages

A downstream ingest page is acceptable only when all of the following are true:

1. It has valid YAML frontmatter for the wiki directory it lives in.
2. It contains at least two outbound wikilinks and is listed in [[index]] if it is a
   content page under `queries/`, `concepts/`, `entities/`, or `comparisons/`.
3. It has a `Source basis` section with corpus-relative paths, public repo URLs,
   and commit/file-path evidence where available.
4. It records compliance status or explicitly says that raw export is blocked or
   unreviewed.
5. It marks negative evidence and uncertainty rather than smoothing them into
   confident prose.
6. It does not include wholesale raw corpus files or long copied source passages.
7. It distinguishes at least the relevant artifact class: exact `spec.md`,
   requirements/design, agent-native spec, template/control plane, RFC/ADR,
   executable contract, or negative control.
8. It separates timing labels from AI-generation claims.
9. It runs `scripts/lint-wiki.sh` after edits and records the result in the Kanban
   handoff.
10. If it creates or edits a public ingest wave page, it updates [[log]] with the
    page names and validation result.

## Kanban task graph

Board: `spec-deep-dive-wiki-ingest`

| Task | ID | Purpose |
|---|---|---|
| `SPEC-WIKI-00` | `t_06d43bca` | Source map and public-safety ingest policy |
| `SPEC-WIKI-01` | `t_34564330` | Priority case studies: `jcode`, DroidAgent, J8/J8Spec |
| `SPEC-WIKI-02` | `t_8f345b83` | Exact `spec.md` and mature standards cohort |
| `SPEC-WIKI-03` | `t_23bdfe0a` | Agent-native / Spec Kit / Kiro cohort |
| `SPEC-WIKI-04` | `t_a42f722e` | RFC / ADR / executable-contract cohort |
| `SPEC-WIKI-05` | `t_81257281` | Aggregate deep-dive index and cross-links |
| `SPEC-WIKI-06` | `t_c84d9ec2` | Public-safety review, lint, commit, push |

Dependency shape:

```text
SPEC-WIKI-00
  ├─ SPEC-WIKI-01
  ├─ SPEC-WIKI-02
  ├─ SPEC-WIKI-03
  └─ SPEC-WIKI-04
        ↓
SPEC-WIKI-05
        ↓
SPEC-WIKI-06
```

## Acceptance criteria

The ingest project is complete when:

1. The wiki has a public-safe deep-dive index page.
2. Priority case studies and cohorts have either dedicated pages or clearly named
   sections with source paths and caveats.
3. The original [[spec-dataset-evolution-research-project]] links to the private
   corpus and the ingest index.
4. The wiki log records each ingest wave.
5. `scripts/lint-wiki.sh` passes.
6. The final wiki commit is pushed and `HEAD == origin/main` is verified.

## Open gates

- Raw public export remains blocked by the manual/adjudicated label gate from
  `SPEC-DATA-22`.
- The private corpus may be used as evidence, but publication still needs the
  fail-closed export checks: license, redistribution, secret/PII/internal scans,
  excerpt policy, and human audit labels.
- Historical pressure timelines remain future work; current stars and sampled
  co-change are not longitudinal pressure series.
