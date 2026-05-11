---
title: Basis Source Basis and Safety Gate
created: 2026-05-10
updated: 2026-05-11
type: query
tags: [safety, context-engineering, code-quality, formal-methods, work-management]
sources: [raw/articles/basis-project-deep-dive-2026-05-10.md, queries/basis-project-index.md, queries/spec-deep-dive-wiki-ingest-project.md, concepts/safety-and-permissions.md]
---

# Basis Source Basis and Safety Gate

## Purpose

This page defines what the Basis wiki corner may cite, what it must not publish, and how future updates should avoid turning private run state into public prose.

It is the boring page. Boring pages are where systems remain housebroken.

## Source basis

| Claim scope | Source | Public-safe use | Hard limit |
|---|---|---|---|
| Core Basis architecture | `/Users/ericfode/src/basis` safe files and [[queries/nightly-src-projects-desk-2026-05-10|nightly-src-projects-desk-2026-05-10]] | commit state, tests, compile/format gate, safe file/module responsibilities | no raw provider streams or local run payloads |
| Hermes plugin bridge | `/Users/ericfode/src/basis-hermes` safe files and repair note evidence | tool names, schema posture, tests, dashboard/API route names | no arbitrary local file contents or private dashboard outputs |
| Jcode reducer/control plane | `/Users/ericfode/src/basis-jcode/components/spec-basis-reducer` source/tests plus `.basis` counts | architecture, test status, run names/counts, dashboard loopback status | no `.basis` packet/log/prompt/NDJSON bodies |
| Spec corpus relation | [[spec-dataset-evolution-research-project]] and [[spec-deep-dive-index]] | aggregate counts, provenance policy, public-safe synthesis | no raw copied corpus specs |
| Publication policy | [[spec-deep-dive-wiki-ingest-project]] and [[safety-and-permissions]] | fail-closed public-safety rules | no secrets, PII, private prompts, evaluator payloads, or run bodies |
| Experiment discipline | [[evaluation-and-review-loops]] and [[work-management-primitives]] | gates, no-go criteria, status tables | no claim without verifier or caveat |

## Allowed public evidence

Allowed by default:

- repository names and local paths;
- branch/commit/status summaries;
- safe filenames and module responsibilities;
- test, compile, lint, and format outcomes;
- route/tool names;
- `.basis` directory names and aggregate counts;
- output filenames;
- synthetic examples written specifically for publication;
- short architectural synthesis.

Allowed only after separate review:

- excerpts from public upstream source files;
- synthetic packet bodies;
- redacted run summaries;
- dashboard screenshots or exports.

## Excluded evidence

Do not publish:

- `.basis` raw run trees;
- prompt text;
- NDJSON event bodies;
- stdout/stderr log bodies;
- worker packet bodies;
- validation bodies from real private runs;
- local dashboard `/api/state` payloads;
- local service configuration;
- private corpus raw files;
- evaluator-like payloads;
- hidden references/oracles;
- credentials, tokens, `.env` contents, or secret-adjacent values;
- raw model outputs that have not been explicitly accepted and reviewed.

## Public update checklist

Before adding a Basis wiki update:

1. Name which surface the claim concerns: `basis`, `basis-hermes`, `basis-jcode`, `steward`, or corpus pressure.
2. Cite a safe source: commit metadata, safe filename, test result, or existing wiki source page.
3. Mark whether the claim is:
   - observed evidence;
   - synthesis;
   - plan;
   - caveat;
   - no-go criterion.
4. If `.basis` is involved, use counts/status only unless a separate review approved the body.
5. Run wiki lint before commit.
6. Keep the public page narrower than the private tree.

## Basis-specific safety risks

| Risk | Why it matters | Mitigation |
|---|---|---|
| Dashboard local-file access | `basis-hermes` dashboard routes can read a local source path and write output directories. | Keep dashboard loopback-bound; document local-only posture. |
| Jcode dashboard run state | `/api/state` can expose run records, event summaries, and execution metadata. | Do not scrape/publish it without review. |
| Prompt and NDJSON artifacts | Real runs preserve prompts, model streams, stderr, and parsed packets for audit. | Count filenames only; summarize architecture. |
| Proposal/acceptance confusion | Proposed records can look authoritative. | Always say proposal until an explicit acceptance change exists. |
| Dirty/ahead repo state | `basis-jcode` has unpushed commits and tracked deletions. | Architecture-only summary until clean/reviewed. |
| Formatter red gate | Core `basis` has a small formatting failure. | Report it; fix before presenting as green. |

## Relationship to other wiki safety patterns

This page follows the same public/private split used by [[spec-deep-dive-wiki-ingest-project]] and [[spec-deep-dive-index]]: public pages may contain synthesis, metadata, counts, repo references, and caveats; raw private artifacts stay private.

That distinction is not bureaucracy. It is the difference between analysis and accidental exfiltration.
