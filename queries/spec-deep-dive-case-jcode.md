---
title: "Spec Deep-Dive: jcode"
created: 2026-05-05
updated: 2026-05-05
type: query
tags: [survey, context-engineering, work-management, code-quality]
sources: [queries/spec-deep-dive-wiki-ingest-project.md, queries/spec-dataset-evolution-research-project.md, queries/llm-readable-spec-files.md]
---

# Spec Deep-Dive: jcode

## Question

Why should `1jehuang/jcode` be treated as a priority case study for the
[[spec-dataset-evolution-research-project]] rather than as just another Markdown-heavy
repository?

## Short answer

`jcode` is a post-LLM coding-agent harness whose specification surface is
not one canonical `spec.md`, but a distributed system of architecture notes,
performance plans, audits, protocols, agent instructions, behavior prompts,
safety policies, and product-surface designs. It is therefore a calibration case
for the difference between [[llm-readable-spec-files]] as a clean ideal and real
AI-era repos whose contracts are scattered through the workspace like well-meaning
sparrows.

The public-safe conclusion is: include `1jehuang/jcode` as a priority calibration
seed for **distributed spec surfaces** and **high code/spec connectedness**, but
keep raw-content export blocked pending policy review.

## Source basis

| Claim scope | Private corpus source | Public upstream reference | Evidence fields used | Caveat |
|---|---|---|---|---|
| Identity and classification | `reports/deep-dives/jcode.md`; `reports/jcode_first_calibration_seed.md` | `https://github.com/1jehuang/jcode` | repo URL, repository description, topics, primary language, created/pushed dates, observed default branch | The private dossier was used as evidence; no raw corpus file body is reproduced here. |
| Current inspected revision | `reports/deep-dives/jcode.md`; `reports/deep-dives/jcode-analysis.json` | commit `36b46fcd32d724bc3eaaabaf88e79e23e21980c2` | local clone metadata, HEAD subject, commit count, history span | This is a snapshot at corpus HEAD `4659608`; current GitHub state may have moved. |
| Distributed spec surface | `reports/deep-dives/jcode.md`; `reports/jcode_first_calibration_seed.md` | paths such as `AGENTS.md`, `src/prompt/system_prompt.md`, `docs/COMPILE_PERFORMANCE_PLAN.md`, `docs/MODULAR_ARCHITECTURE_RFC.md` | selected spec-like paths, path classes, LOC, touch counts, artifact labels | README is mixed product/marketing/spec material; it must be section-classified rather than counted wholesale. |
| Code/spec connectedness | `reports/deep-dives/jcode.md`; `reports/deep-dives/jcode-analysis.json` | same inspected repo and commit | spec-like commit count, doc/code co-change examples, path/command references, prompt/instruction files | Co-change is evidence of connection, not proof of causal governance. |
| AI-era timing and pressure | `reports/deep-dives/jcode.md`; `reports/jcode_first_calibration_seed.md` | repo created `2026-01-05`; release `v0.11.10` observed `2026-05-04` | first commit date, release density, pressure-category counts, topics | Post-LLM timing is a repo-era/product-domain label, not evidence that any specific file was AI-generated. |

## Why this case matters

The dataset needs examples that falsify simplistic miners. `jcode` does this in
both directions:

- an exact-`spec.md` miner would miss almost everything important;
- an all-Markdown miner would inflate the corpus with product prose, screenshots,
  demos, operations notes, and marketing material;
- a better miner has to classify artifact families: architecture, RFC, plan,
  audit, protocol, prompt, safety policy, agent operating instructions, and mixed
  README sections.

That makes `jcode` an anchor for the project’s real question: which spec-like
artifacts actually constrain code and agent behavior, and which are just decorative
context with nicer typography?

## Distributed spec surface

The jcode calibration seed gives these high-priority classes:

| Artifact class | Example paths | Dataset treatment |
|---|---|---|
| Agent operating instructions | `AGENTS.md`; `src/prompt/system_prompt.md` | Include as normative behavior contracts, because they address future agents/developers and the harness itself. |
| Performance/resource plan | `docs/COMPILE_PERFORMANCE_PLAN.md`; `docs/MEMORY_BUDGET.md`; `docs/TERMINAL_BENCH.md` | Include when commands, budgets, thresholds, or benchmark gates are explicit. |
| Runtime architecture | `docs/SERVER_ARCHITECTURE.md`; `docs/MEMORY_ARCHITECTURE.md`; desktop/iOS architecture notes | Include when module boundaries, state ownership, lifecycle invariants, or process topology are named. |
| RFC / migration plan | `docs/MODULAR_ARCHITECTURE_RFC.md`; split/server-service plans | Include as proposed/refactor contracts with status and validation fields when available. |
| Contract audit | `docs/PROVIDER_SESSION_SHARED_CONTRACT_AUDIT.md`; code/mobile audits | Include as measurement/review artifacts, distinct from prospective design. |
| Protocol and safety policy | `docs/BROWSER_PROVIDER_PROTOCOL.md`; `TELEMETRY.md`; `docs/SAFETY_SYSTEM.md`; `docs/AMBIENT_MODE.md` | Include when the text constrains external integration, event shape, permissions, reversibility, or autonomy. |
| Mixed README/product surface | `README.md`; desktop/mobile/figma docs | Include only with section-level or manual classification. |

This is the same authority-layer problem that appears in [[context-engineering]]:
models and humans both need to know which text is contract, rationale, policy,
example, or ambient color.

## Connectedness evidence

The corpus dossier records `39` selected spec-like files, `14,209` spec-like LOC,
`348,326` Rust LOC, and `2,953` commits over `120` observed days. It also records:

| Metric | Value |
|---|---:|
| Selected spec-like commits | `298` |
| Fraction of all commits touching selected spec-like paths | `0.101` |
| Spec-like commits also touching code | `130` |
| Spec-like commits also touching tests | `26` |
| Spec/code co-change fraction among spec-like commits | `0.436` |

Representative anchors from the dossier include architecture or telemetry docs
co-changing with CLI/server/TUI code, a desktop prototype document co-changing
with `crates/jcode-desktop/src/main.rs`, and multi-session architecture notes
co-changing with TUI workspace-map code.

The interpretation should stay modest: this is strong connectedness evidence,
not a theorem of design causality. The point is to make a measurable surface for
[[evaluation-and-review-loops]], not to make the spreadsheet feel heroic.

## AI-era timing and pressure

`jcode` begins in January 2026, after the public LLM coding-agent wave, and its
observed topics and architecture include AI, Claude/OpenAI provider surfaces,
MCP, browser automation, swarm/agent coordination, memory, ambient mode, and
self-development. The dataset label should therefore be `post_llm_agent_wave` or
`ai_native_agent_harness`.

Pressure labels from the dossier include TUI/UX, fix/bug, multi-session/server,
provider/auth, performance/resource, agent coordination, testing/safety,
platform/product-surface, documentation/spec, and refactor/architecture pressure.
These are descriptive commit-message classes. They should not be laundered into a
historical popularity or causality timeline.

## Limitations and publication boundary

- Raw content export remains `review_required`; this page uses synthesis and
  metadata only.
- The local dossier observed release/tag data and Cargo package version mismatch;
  release derivation should use tags/releases rather than `Cargo.toml` alone.
- Current stars/forks are current-snapshot evidence, not historical pressure.
- Generated assets, demo JSON, package manifests, CI files, screenshots, videos,
  and fixtures are negative/control families unless a separate policy promotes
  them as executable contracts.
- `README.md` is useful but dangerous: classify it by section, not by aura.

## Dataset implication

Use `jcode` to calibrate the high-connectedness end of the corpus. The crawler
should preserve exact path classes, same-commit co-change, path and command
references, prompt/instruction files, status fields, and adjacent negative
controls. This page is one public-safe slice of [[spec-deep-dive-wiki-ingest-project]];
the raw dossier stays in the private corpus.
