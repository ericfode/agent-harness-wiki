---
title: "Spec Deep-Dive: Exact spec.md and Standards Cohort"
created: 2026-05-05
updated: 2026-05-05
type: query
tags: [survey, context-engineering, code-quality, formal-methods]
sources: [queries/spec-deep-dive-wiki-ingest-project.md, queries/spec-dataset-evolution-research-project.md, queries/llm-readable-spec-files.md]
private_corpus_repo: https://github.com/ericfode/spec-dataset-evolution-corpus
private_corpus_head: 4659608
kanban_task: t_8f345b83
---

# Spec Deep-Dive: Exact `spec.md` and Standards Cohort

## Question

What does the exact lower-case `spec.md` cohort teach once the private corpus looks
at whole repositories rather than isolated Markdown files, and how should mature
standards/protocol repositories shape the public [[spec-dataset-evolution-research-project]]?

This page is the `SPEC-WIKI-02` public-safe synthesis for
[[spec-deep-dive-wiki-ingest-project]]. It uses the private corpus repository as
evidence, but it does not publish raw copied corpus files. The right public unit
here is repository-level synthesis plus provenance, not a ceremonial dumping of
other people's standards text. We are civilized; barely.

## Short answer

Exact `spec.md` is a high-signal discovery handle, not a document type. In this
cohort it points to at least four distinct authority shapes:

1. **Standards repository with a root contract** — OCI runtime, OCI distribution,
   Compose, and Cloud Foundry Service Broker use `spec.md` as a normative public
   surface, but schemas, conformance tests, release tags, CI, and profiles decide
   whether the file is operationally alive.
2. **Language/library implementation contract** — HCL's `spec.md` files live next
   to parser, formatter, decoder, writer, and test packages; the filename looks
   like documentation, but the repository behaves like a language-specification
   workbench.
3. **Mature specification machine** — OpenTelemetry, Protocol Buffers, and gRPC
   show that long-lived standards often distribute authority across chapters,
   design docs, `.proto` contracts, interop tests, compliance matrices, and
   release governance rather than a single top-level file.
4. **Executable/formal or non-GitHub standards corpus** — GraphQL, Thrift, TLA+,
   Dafny, OpenAPI Generator, Wayland protocols, OpenID Connect, Hare, and Ariadne
   add cases where specs are grammars, XML protocols, IDLs, proof/program files,
   or workgroup source trees. A crawler that only knows GitHub Markdown will miss
   much of the actual contract surface.

For [[llm-readable-spec-files]], the lesson is pleasantly severe: a good `spec.md`
is not valuable because it is named `spec.md`; it is valuable because the
repository treats it as an acceptance surface with adjacent enforcement. Names
are handles. Evidence is structure.

## Source basis

The private corpus source paths below are corpus-relative. Public prose cites
repository URLs, commits, paths, metadata fields, and caveats; it deliberately
avoids wholesale raw spec content.

| Claim scope | Private corpus source | Public upstream reference | Evidence fields used | Caveat |
|---|---|---|---|---|
| Exact `spec.md` cohort composition and per-repo summary | `reports/deep-dives/SPEC-REPO-01/index.md`, `reports/deep-dives/SPEC-REPO-01/candidates.jsonl` | Sourcegraph-derived public GitHub candidates; selected repos listed below | selected/rejected rows, repo URL, stars from Sourcegraph, inspected commit, exact `spec.md` path, license, search failures | Sourcegraph excludes forks/archives by default; GitHub code search required auth; this is a high-signal cohort, not prevalence. |
| Cloud Foundry Service Broker is API/profile contract, not just Markdown | `reports/deep-dives/SPEC-REPO-01/cloudfoundry__servicebroker.{md,json}` | https://github.com/cloudfoundry/servicebroker at `60e1e77662d3`; paths `spec.md`, `openapi.yaml`, `swagger.yaml` | spec inventory, exact spec history, connectedness, release tags, compliance | Issue/PR pressure unresolved because unauthenticated GitHub API budget was exhausted. |
| Compose Spec is a spec-first repository | `reports/deep-dives/SPEC-REPO-01/compose-spec__compose-spec.{md,json}` | https://github.com/compose-spec/compose-spec at `14a4f1c4c8bf`; path `spec.md` | exact spec LOC/history, schema/build paths, direct links, code/spec ratio | Local repo has little conventional code; implementation influence lives downstream in Compose tools. |
| HCL is an implementation-backed language specification | `reports/deep-dives/SPEC-REPO-01/hashicorp__hcl.{md,json}` | https://github.com/hashicorp/hcl at `2efc2662361a`; paths `spec.md`, `hclsyntax/spec.md`, `json/spec.md` | spec inventory, parser/test proximity, same-commit co-change, code/test/spec LOC | Some normative behavior may live in tests and package docs rather than exact `spec.md` history alone. |
| OCI runtime/distribution show two standards-repo contract shapes | `reports/deep-dives/SPEC-REPO-01/opencontainers__runtime-spec.{md,json}`, `reports/deep-dives/SPEC-REPO-01/opencontainers__distribution-spec.{md,json}` | https://github.com/opencontainers/runtime-spec at `6999a89a76a0`; https://github.com/opencontainers/distribution-spec at `ed885fa76559` | exact `spec.md`, schema paths, conformance/test paths, tag/release proxy, co-change | Git/tag pressure is a local proxy; full issue/PR/release pressure was not collected. |
| Mature baselines distribute spec authority across many artifacts | `reports/deep-dives/SPEC-REPO-07/index.md`, per-repo records under `SPEC-REPO-07/` | OCI runtime, OpenTelemetry, Protocol Buffers, gRPC public repos at inspected commits | code/spec/test counts, spec+contract inventories, first/last artifact dates, clone mode, compliance | Protocol Buffers and gRPC were partial blob clones with full commit graph/current checkout, not full historical blob export. |
| Related standards and executable/formal cohorts widen the taxonomy | `reports/deep-dives/SPEC-REPO-18/index.md`, `reports/deep-dives/SPEC-REPO-19/index.md` | GraphQL, Thrift, TLA+, Dafny, OpenAPI Generator, Wayland, OpenID, Hare, Ariadne public repos | contract file counts, clone modes, compliance, host-specific discovery notes, negative evidence | Several records are `review_required` or `metadata_only`; this page uses metadata/synthesis only. |

## Exact `spec.md` cohort: one filename, several governance shapes

`SPEC-REPO-01` selected five high-signal public repositories with exact lower-case
`spec.md` files. All selected exact specs were public, had no private-token
access, and received a clean lightweight regex spotcheck on exact spec files.
The raw corpus stores private file copies and dossier records; this page reports
metadata and interpretation only.

| Repository | Public reference | Exact/spec-like artifacts | History and connectedness | Dataset lesson |
|---|---|---:|---|---|
| `opencontainers/runtime-spec` | https://github.com/opencontainers/runtime-spec at `6999a89a76a0`; root `spec.md` | 54 LOC in exact `spec.md`; adjacent schema docs and Go `specs-go` material | 16 exact-spec changing commits; 4 same-commit exact spec/code changes; 21 release tags in the dossier | Root `spec.md` is the normative center, but schemas, Go structs, validation checks, CI, and platform-specific docs make the contract executable enough to matter. |
| `opencontainers/distribution-spec` | https://github.com/opencontainers/distribution-spec at `ed885fa76559`; root `spec.md` | 921 LOC exact `spec.md`; conformance and `specs-go` surfaces | 118 exact-spec changing commits; 8 same-commit spec/code changes; 8 same-commit spec/test changes | The contract boundary is prose plus conformance tests, schema/OpenAPI material, and registry interoperability pressure. |
| `compose-spec/compose-spec` | https://github.com/compose-spec/compose-spec at `14a4f1c4c8bf`; root `spec.md` | 3,588 LOC exact `spec.md`; schema/build scaffolding | 232 exact-spec changing commits; 0 local code co-change by the scanner | This is the purest spec-first case: the spec is the product, while downstream implementations carry much of the execution pressure. |
| `hashicorp/hcl` | https://github.com/hashicorp/hcl at `2efc2662361a`; `spec.md`, `hclsyntax/spec.md`, `json/spec.md` | 2,039 LOC across exact `spec.md` files; 30,127 code LOC and 33,644 test LOC | 15 exact-spec changing commits; 1 same-commit spec/code and 1 same-commit spec/test event; 50 tags | `spec.md` behaves like a language contract embedded in an implementation repo; path proximity to parser/test packages is central evidence. |
| `cloudfoundry/servicebroker` | https://github.com/cloudfoundry/servicebroker at `60e1e77662d3`; `spec.md`, `openapi.yaml`, `swagger.yaml` | 1,969 LOC exact `spec.md`; 3,910 spec-like LOC | 304 exact-spec changing commits; 14 same-commit spec/code changes; profile links and validation scripts | A service/API profile spec combines prose, OpenAPI/Swagger contracts, profile docs, scripts, and versioned release practice. |

The empirical warning is simple: exact filename search is useful for candidate
discovery, but it cannot classify authority. `compose-spec/compose-spec` and
`hashicorp/hcl` both satisfy the same exact-path predicate; one is a mostly
spec-first standards repository and the other is an implementation-backed language
library. Treating both as a single “Markdown spec” class would be, technically,
a taxonomy misdemeanor.

## Mature standards baselines

`SPEC-REPO-07` intentionally selected mature pre-AI public repositories whose
spec-like artifacts have long-lived lineage. These records are important because
they give the dataset a baseline for what living specifications look like before
agent-native `spec.md` culture enters the scene.

| Repository | Public reference | Spec/code shape | Mature-baseline lesson |
|---|---|---|---|
| `opencontainers/runtime-spec` | https://github.com/opencontainers/runtime-spec at `6999a89a76a0` | 1,944 spec+contract LOC / 1,569 code LOC / 1,012 test LOC in the mature-baseline scanner | OCI runtime appears in both exact and mature cohorts: the root `spec.md` is small, but the repository-level contract is larger because `config.md`, `runtime.md`, JSON schemas, and Go structures carry normative load. |
| `open-telemetry/opentelemetry-specification` | https://github.com/open-telemetry/opentelemetry-specification at `4034703db495` | 54,245 spec+contract LOC / 494 code LOC | The repository itself is a governance/specification machine: specification chapters, OTEPs, compliance matrices, semantic conventions, and stability/versioning documents form a lifecycle. |
| `protocolbuffers/protobuf` | https://github.com/protocolbuffers/protobuf at `c4e2cdfb07dc` | 24,899 spec+contract LOC / 893,012 code LOC / 471,638 test LOC | Design docs for Editions live beside executable `.proto` contracts and multi-language runtimes, so spec authority is deeply coupled to implementation and compatibility pressure. |
| `grpc/grpc` | https://github.com/grpc/grpc at `d4cb49f91817` | 55,099 spec+contract LOC / 814,902 code LOC / 519,063 test LOC | Protocol docs, service config, status codes, health-checking, load balancing, `.proto` files, and interop tests form a distributed contract surface. |

This baseline matters for [[context-engineering]] because a usable agent-facing
spec should expose the local authority map. Mature projects rarely put every
important obligation in one file. They use layered contracts: prose for intent,
schemas/IDLs for shape, tests for behavioral pressure, release tags for version
boundaries, and governance docs for change control.

## Related standards and executable-contract dossiers

The broader standards cohorts (`SPEC-REPO-18` and `SPEC-REPO-19`) prevent the
exact-`spec.md` page from becoming parochial. Their role here is not to expand
this page into every executable-contract case; `SPEC-WIKI-04` owns more of that
territory. Their role is to show the boundary of the exact filename strategy.

| Cohort | Repositories | What they add to the taxonomy | Publication gate |
|---|---|---|---|
| `SPEC-REPO-18` formal/executable and large contract repos | `graphql/graphql-spec`, `apache/thrift`, `tlaplus/tlaplus`, `dafny-lang/dafny`, `OpenAPITools/openapi-generator` | Specs may be Markdown standards chapters, IDL files, `.tla` models, `.dfy` programs/proofs, generated contract fixtures, and workflow/config contracts. Formal-methods files blur code/spec/test categories. | Apache Thrift is `allowed`; GraphQL, TLA+, Dafny, and OpenAPI Generator records are `review_required` or have clone/license caveats, so this page uses metadata only. |
| `SPEC-REPO-19` non-GitHub public forges | Wayland protocols, OpenID Connect, Hare specification, Ariadne identity specification | Standards sources exist on GitLab, Bitbucket, SourceHut, and Codeberg; discovery is host-specific and often lacks GitHub-like global code search. XML protocols, LaTeX specs, and workgroup XML drafts are first-class spec artifacts. | Wayland is `allowed_with_obligations`; OpenID and Ariadne are `review_required`; Hare is `metadata_only`. No raw excerpts are used here. |

The non-GitHub cohort is especially useful negative evidence. It proves that
“GitHub code search for Markdown specs” is not the dataset; it is one lantern in
a fairly large cave. Host-specific search limits, forks/mirrors, sparse clone
fallbacks, and license ambiguity must be preserved as data, not apologized away
in prose.

## Implications for the dataset design

### 1. Discovery and classification must be separate

Exact-path discovery should enqueue candidates, not decide their class. A row
matching `(^|/)spec.md$` still needs repository-level classification:

- Is `spec.md` the product, a chapter index, a language contract, a profile/API
  contract, or a placeholder beside stronger machine-readable contracts?
- Are schemas, OpenAPI, IDL, `.proto`, `.tla`, `.dfy`, XML protocol files,
  conformance tests, or CI workflows the real enforcement surface?
- Is the repository an upstream authority, a fork/template/tutorial, or a
  downstream generated scaffold?

This is the same discipline used by [[evaluation-and-review-loops]]: evidence
must be typed before it is judged.

### 2. Code/spec ratios need artifact-aware denominators

The cohort is deliberately bimodal. Compose has no local conventional code by the
scanner; HCL has roughly fifteen times more test LOC than exact-spec LOC; mature
gRPC and Protobuf are enormous implementation/test corpora with relatively small
but important spec surfaces. A naive `spec LOC / code LOC` scalar will punish
spec-first standards repos and understate implementation-backed language specs.
The dataset should keep separate ratios for:

- exact `spec.md`;
- broader prose specification artifacts;
- machine-readable contracts such as schemas, IDLs, `.proto`, XML protocols, and
  formal/spec-program files;
- tests, conformance suites, examples, and CI/build surfaces.

### 3. Connectedness is not only hyperlinks

The strongest contract evidence often appears as path proximity, co-change,
schema/test adjacency, release tags, or typed protocol artifacts. For example,
OCI distribution's same-commit spec/test evidence and Cloud Foundry's profile and
OpenAPI surfaces say more than a plain Markdown link count. HCL's parser/test
proximity is a different kind of connectedness again.

This supports the existing [[spec-dataset-evolution-research-project]] plan for
`spec_code_edge` records: direct links are only one edge type. The corpus needs
edges for paths, symbols, tests, schemas, commits, release tags, and governance
objects.

### 4. Era labels are timing labels, not authorship labels

Every exact `spec.md` record in `SPEC-REPO-01` is labeled `pre_chatgpt` by first
exact-spec commit date. Several mature standards have substantial post-2022
activity. That supports change-over-time analysis, not AI-generation claims. A
date is not a provenance oracle; it is only a date wearing a little hat.

### 5. Public raw export should remain fail-closed

This page uses synthesis, paths, repo URLs, commit SHAs, counts, and caveats. It
does not quote or republish raw private corpus files. Even when a source is public
and permissively licensed, the private corpus policy still requires license,
redistribution, secret/PII/internal scan, clone coverage, and excerpt-policy
checks before raw export. `SPEC-REPO-18` and `SPEC-REPO-19` make that necessity
visible: some records are public and useful but still `review_required` or
`metadata_only` for raw-content publication.

## Practical carry-forward

For later cohort pages and the aggregate index:

- Keep `SPEC-REPO-01` as the exact-filename control group, not as the definition
  of software specification.
- Treat `SPEC-REPO-07` as the mature baseline for non-agent-native standards and
  compatibility pressure.
- Use `SPEC-REPO-18` and `SPEC-REPO-19` to widen artifact classes and forge
  coverage, while preserving their compliance gates.
- Report rejected/deferred candidates and failed searches alongside selected
  repos; otherwise discovery bias quietly turns into a result.
- Link this page from the eventual `[[spec-deep-dive-index]]` so exact `spec.md`
  examples sit beside agent-native, RFC/ADR, executable-contract, and negative
  control cohorts.

## Validation note

No raw upstream spec bodies were copied into this page. Source evidence is limited
to corpus-relative dossier paths, public repository URLs, inspected commits,
artifact paths, aggregate counts, and paraphrased synthesis. The private corpus
checkout inspected for this wave was `4659608`, matching the `SPEC-WIKI-00`
source-map handoff.
