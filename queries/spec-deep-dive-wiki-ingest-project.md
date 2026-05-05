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

The private corpus currently contains:

- 1,741 artifact occurrence rows in `data/artifact_occurrences.jsonl`.
- 1,676 private raw-file copies under `corpus/by_repo/`.
- 65 hard-quarantined raw rows preserved as metadata-only.
- 51 unique selected repositories and 55 selected dossier occurrences.
- Authored deep-dive dossiers under `reports/deep-dives/`.
- Validation scripts, provenance manifests, dedup clusters, connectedness frames,
  and aggregate reports.

The private repository is intentionally not a public release. Its raw files retain
upstream licenses and copyright context; the public wiki should not copy them
wholesale.

## Ingest policy

Wiki pages may include:

- synthesis of the deep-dive dossiers;
- repository URLs, commit SHAs, paths, and stable source references;
- short excerpts only when they are necessary and safe;
- caveats about missing metadata, API limits, license review, and manual-audit
  status;
- links back to [[llm-readable-spec-files]], [[context-engineering]],
  [[work-management-primitives]], and [[evaluation-and-review-loops]].

Wiki pages should not include:

- bulk raw spec contents;
- unreviewed long copied excerpts;
- claims that a post-ChatGPT timestamp proves AI generation;
- current-star snapshots presented as historical pressure timelines;
- flattened “spec” labels that erase templates, executable contracts, RFCs,
  negative controls, and package/test lookalikes.

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
