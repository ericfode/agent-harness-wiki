---
title: "Spec Deep-Dive: Aggregate Index"
created: 2026-05-05
updated: 2026-05-05
type: query
tags: [survey, work-management, context-engineering, code-quality, formal-methods]
sources: [queries/spec-deep-dive-wiki-ingest-project.md, queries/spec-dataset-evolution-research-project.md, queries/llm-readable-spec-files.md]
private_corpus_repo: https://github.com/ericfode/spec-dataset-evolution-corpus
private_corpus_head: 4659608
raw_publication_mode: synthesis_plus_metadata
kanban_task: t_81257281
---

# Spec Deep-Dive: Aggregate Index

## Question

What did the private `spec-dataset-evolution-corpus` deep-dive wave show once
whole repositories, cohort scouts, and public-safety gates were considered
together?

This page is the public-safe aggregate index for
[[spec-deep-dive-wiki-ingest-project]] and the deep-dive companion to
[[spec-dataset-evolution-research-project]]. It uses the private corpus
repository as a private-source pointer and evidence store, but it does not
release raw copied corpus files: raw corpus bodies stay private. The public unit
here is synthesis plus provenance: URLs, commits, corpus-relative paths, counts,
caveats, and links to focused wiki pages.

## Short answer

The deep-repo wave confirms that “software specification” is not one document
shape. Exact `spec.md` files, requirements documents, `.kiro/specs`, Spec Kit
scaffolds, RFC/ADR corpora, OpenAPI/Proto/Smithy/AsyncAPI contracts, formal
specification languages, and negative-control documentation all have to be kept
as separate artifact families. Collapse them into one bucket and the analysis
becomes elegantly wrong, which is still wrong.

Across the aggregate private-corpus evidence, the scout wave produced 55 selected
dossier occurrences across 51 unique public repositories, from 400 candidate
rows. It also preserved 335 rejected/deferred rows and 10 failed-search or
metadata-limit rows, so discovery failures remain evidence instead of vanishing
into the carpet.

## Source basis

The source paths below are corpus-relative inside the private repository
`https://github.com/ericfode/spec-dataset-evolution-corpus` at observed HEAD
`4659608` unless otherwise stated.

| Claim scope | Private corpus source | Public upstream reference | Evidence fields used | Caveat |
|---|---|---|---|---|
| Ingest boundary and public-safety policy | `PROJECT_BRIEF.md`; `reports/deep-dives/SPEC-REPO-16/COMPLIANCE_EXPORT_GATE.md`; [[spec-deep-dive-wiki-ingest-project]] | private corpus repo URL only | publication mode, source routing, raw-export gate, excerpt policy | The private corpus is evidence, not a public raw-content release. |
| Aggregate dossier counts and cohort yield | `reports/AGGREGATE.md`; `reports/deep-dives/AGGREGATE.md`; `data/aggregate_repo_records.jsonl` | 51 public repositories represented by selected dossier records | selected occurrences, candidate classes, scout directories, Markdown/JSON artifacts read, parse errors | Aggregate counts summarize selected scouts; they are not prevalence estimates for all public repositories. |
| Artifact-class distribution | `reports/AGGREGATE.md`; `data/corpus_file_manifest.jsonl`; `data/aggregate_repo_records.jsonl` | public repo URLs in aggregate rows | normalized doc types, inventory samples, authority origin, raw-inclusion status | File-class counts include occurrence evidence and must be separated from independent authority. |
| Code/spec connectedness | `data/connectedness_features.jsonl`; `data/aggregate_repo_records.jsonl`; per-cohort dossiers | repo URLs and inspected commits preserved in child pages | direct links, reverse backrefs, path/symbol mentions, test linkage, same-commit co-change | Connectedness is evidence of coupling, not proof of causality or governance success. |
| Template and duplicate lineage | `reports/deep-dives/SPEC-REPO-20/TEMPLATE_LINEAGE_MODEL.md`; `reports/deep-dives/SPEC-REPO-20/template_lineage_mapping.jsonl` | Spec Kit, Kiro, Agent OS, prompt-template, and tutorial/fork repos named in child pages | template family, authority origin, generated scaffold, edited project contract, independent authority weight | Template descendants are adoption evidence unless reviewed as independent project authority. |
| Search and platform limits | `reports/deep-dives/SPEC-REPO-01..12/index.md`; `sources.md`; `candidates.jsonl` | GitHub, GitLab, Codeberg, SourceHut, Bitbucket, and public clone URLs where available | failed searches, HTTP 401/403, rate-limit notes, host-specific fallback method, rejected candidates | These failures constrain recall; they must not be silently converted into complete-search claims. |

## Navigation map

| Page | Role in the ingest wave | Main artifact family |
|---|---|---|
| [[spec-deep-dive-wiki-ingest-project]] | Source map, citation style, public-safety gate, and Kanban task graph | ingest contract |
| [[spec-deep-dive-case-jcode]] | Priority calibration case for a post-LLM coding-agent harness | distributed spec surfaces and high connectedness |
| [[spec-deep-dive-case-droidagent]] | Priority case for agent-generated mobile-GUI behavioral scenarios | requirements/tasks/reports/scripts as replayable behavior specs |
| [[spec-deep-dive-case-j8-ambiguity]] | Negative-evidence trail separating `j8agent` ambiguity from J8Spec control value | namespace ambiguity and pre-AI executable-spec control |
| [[spec-deep-dive-cohort-exact-spec-md-and-standards]] | Exact `spec.md`, mature standards, and protocol repositories | normative standards and implementation-backed spec files |
| [[spec-deep-dive-cohort-agent-native-spec-kit-kiro]] | Agent-native workflow specs, Spec Kit, Kiro, templates, and lineage | generated scaffolds versus edited project contracts |
| [[spec-deep-dive-cohort-rfc-adr-executable-contracts]] | RFC/proposal governance and executable/formal contracts | governance prose, API schemas, IDLs, TLA+/Dafny-like formal artifacts |

## Aggregate findings

### 1. Cohort yield is heterogeneous by design

The aggregate wave read 12 scout directories, 79 top-level Markdown artifacts,
and 70 JSON artifacts, with zero parse errors reported. It emitted 55 aggregate
records. The main cohort yield table is:

| Cohort family | Selected records | Candidate rows | What the cohort teaches |
|---|---:|---:|---|
| Exact lower-case `spec.md` | 5 | 130 | `spec.md` is a precise seed, not the definition of a specification. |
| Requirements / PRD / design / architecture | 4 | 10 | Code-rich repos need section/path classification and license review. |
| AI-native `.kiro` / Agent OS specs | 4 | 49 | Requirements/design/tasks packets expose project-local agent contracts. |
| Spec Kit / spec-driven development | 5 | 63 | Templates, commands, hooks, skills, and consumers form a control plane. |
| RFC / ADR / proposals | 5 | 17 | Governance corpora are spec-primary but often implementation-external. |
| Executable contracts | 5 | 9 | OpenAPI, Proto, Smithy, AsyncAPI, and similar files are machine-readable specs. |
| Mature pre-AI baselines | 4 | 8 | Standards and protocol projects provide long-lived comparison cases. |
| Recent AI-era fast-growing repos | 5 | 11 | Agentic product repos show small but highly connected spec islands. |
| Low-star / small-repo counter-sample | 5 | 69 | Co-born specs, missing licenses, and SRS recall holes appear early. |
| Non-GitHub forges | 4 | 11 | Host-specific adapters are required; GitHub assumptions do not port. |
| Forks/templates/tutorials | 5 | 13 | Duplicate inflation is a lineage problem, not just a hash problem. |
| Negative controls | 4 | 10 | Docs/tests/manuals can be code-connected without being product specs. |

### 2. Artifact classes are not interchangeable

The aggregate artifact-class inventory is dominated by requirements, RFCs, and
technical specs, but it also includes architecture docs, exact `spec.md`, Proto,
OpenAPI/API contracts, AsyncAPI, schema/config contracts, agent-native Kiro
packets, PRDs, ADRs, and formal/executable surfaces. The high-count classes
reported in the aggregate include:

| Normalized artifact class | Aggregate count | Interpretation |
|---|---:|---|
| `requirements` | 627 | Largest prose-spec family; needs false-positive controls for dependency manifests and loose docs. |
| `rfc` | 385 | Governance records; often spec-primary but not app-local implementation specs. |
| `technical_spec` | 350 | Broad technical-design/spec family; needs path and authority labels. |
| `architecture` | 61 | Can be normative, explanatory, or historical depending on connectedness evidence. |
| `proto_contract` | 48 | Machine-readable contract surface; codegen/test linkage matters. |
| `api_contract` | 41 | API definitions belong in the spec corpus even when not Markdown. |
| `exact_spec_md` | 34 | Useful discovery handle, not an artifact ontology. |
| `schema_or_config_contract` | 28 | Config/schema files can carry contractual meaning. |
| `asyncapi_contract` | 24 | Executable contract family with raw-export caveats in this pass. |
| `agent_native_kiro` | 20 | Agent-native requirements/design/tasks packets; important AI-era stratum. |

### 3. Connectedness is widespread, but it is evidence, not metaphysics

Across aggregate records, connectedness flags were common: `test_linkage` appears
in 50 records, `path_or_symbol_mentions` in 43, `cochange` in 42, `direct_links`
in 29, and `reverse_backrefs` in 21. Those flags support graph features for
[[llm-readable-spec-files]] and [[evaluation-and-review-loops]], but they should
remain typed evidence. Same-commit co-change says “these moved together,” not
“this spec governed that implementation by divine right.”

### 4. Spec/code ratios need role labels

The aggregate ratio distribution was available for 51 records: min `0.0000`, p25
`0.0319`, median `0.1337`, p75 `3.4141`, and max `3008.3182`, with four
zero-high-confidence-spec records. That range is meaningful only when each repo’s
role is preserved:

- spec-as-product repositories such as RFC, KEP, EIP, or OpenTelemetry-style
  standards can have enormous ratios;
- code-rich implementation repos often have small but meaningful spec islands;
- executable-contract repos need separate treatment because schemas are both
  specifications and build inputs;
- negative controls prove that manuals, tests, and dependency files can be
  strongly code-connected while still not being high-confidence specs.

### 5. Raw export still fails closed

The normalized redistribution summary in the aggregate was 34 `allowed`, 11
`review_required`, 6 `metadata_only`, 3 `allowed_pending_policy_review`, and 1
`allowed_with_obligations`. That is not a license to publish raw content from the
private corpus. Wiki pages in this wave use synthesis, metadata, public URLs,
commits, representative paths, and caveats. Any raw-content export still depends
on the fail-closed gate: license status, redistribution status, secret/PII/internal
scan status, excerpt policy, and human audit labels.

### 6. Discovery failures are part of the result

Several scouts recorded unavailable or rate-limited discovery surfaces:
unauthenticated GitHub code search returned HTTP 401 or 403 in multiple lanes;
Hermes web search was unavailable where Firecrawl was not configured; GitLab,
Codeberg, SourceHut, Bitbucket, and self-hosted GitLab required host-specific
methods. The correct dataset behavior is to store these as `discovery_event` and
`negative_evidence` rows, not to pretend the search frontier was complete.

## Dataset-design carry-forward

The next corpus build should preserve these schema separations:

1. `repo_dossier` / `repo_context` alongside artifact rows.
2. `artifact_form` separate from `authority_origin`.
3. `template_lineage` separate from independent project authority.
4. `discovery_event` and `negative_evidence` rows for failed searches and fallback methods.
5. `clone_and_history_coverage` for full, blobless, sparse, current-tree-only, and rate-limited retrieval.
6. Typed `spec_code_edge` evidence: direct link, reverse backref, path proximity, symbol/endpoint mention, test linkage, codegen linkage, co-change, and issue/PR/release linkage.
7. Per-record compliance gates and raw-content export policy.
8. AI-era timing labels separate from AI-generation claims.
9. Negative-control strata in every crawl batch.

## Remaining gates

- [[spec-deep-dive-wiki-ingest-project]] still routes a final public-safety review
  through `SPEC-WIKI-06` before commit/push publication.
- The manual/adjudicated label gate from the broader
  [[spec-dataset-evolution-research-project]] remains unresolved for raw public
  export.
- Historical pressure timelines are future work. Current stars, forks, and recent
  churn are pressure markers, not longitudinal causal evidence.
- Non-GitHub forge coverage needs proper adapters before anyone says “complete”
  with a straight face.

## See also

- [[spec-dataset-evolution-research-project]]
- [[spec-deep-dive-wiki-ingest-project]]
- [[llm-readable-spec-files]]
- [[context-engineering]]
- [[work-management-primitives]]
- [[evaluation-and-review-loops]]
- [[formal-methods-for-agent-harnesses]]
