---
title: "Spec Deep-Dive: RFC, ADR, and Executable Contracts"
created: 2026-05-05
updated: 2026-05-05
type: query
tags: [survey, work-management, context-engineering, formal-methods, code-quality]
sources: [queries/spec-deep-dive-wiki-ingest-project.md, queries/spec-dataset-evolution-research-project.md]
---

# Spec Deep-Dive: RFC, ADR, and Executable Contracts

## Question

How should the corpus model proposal-heavy repositories and executable contract
repositories without flattening them into the same class as Markdown product
specifications?

Short answer: RFCs, ADRs, and proposals are governance records; OpenAPI, Proto,
Smithy, AsyncAPI, GraphQL, Thrift, TLA+, and Dafny are closer to executable or
machine-checkable contracts. Both can be “specs,” but they put authority in very
different places. A taxonomy that treats all of them as pleasant Markdown-shaped
fog will not survive contact with a compiler, a standards body, or Kubernetes.

This page is part of [[spec-deep-dive-wiki-ingest-project]] and extends the public
frame in [[spec-dataset-evolution-research-project]]. It publishes synthesis and
metadata only; no private raw corpus bodies are copied here.

## Source basis

| Claim scope | Private corpus source | Public upstream reference | Evidence fields used | Caveat |
|---|---|---|---|---|
| RFC/proposal repositories are intentionally spec-primary and encode lifecycle in paths, templates, CI, and history. | `reports/deep-dives/SPEC-REPO-05/index.md`; per-repo JSON/Markdown dossiers; `reports/deep-dives/SPEC-REPO-05/sources.md` | `https://github.com/rust-lang/rfcs`, `https://github.com/kubernetes/enhancements`, `https://github.com/open-telemetry/opentelemetry-specification`, `https://github.com/emberjs/rfcs`, `https://github.com/ethereum/EIPs` | repo URL, inspected commit, spec inventory count, spec/code/test LOC, spec-changing commits, same-commit co-change, compliance status | ADR discovery was not recall-complete: web search failed and unauthenticated GitHub search hit HTTP 403; `backstage/backstage` was rejected/deferred as too large for this scout. |
| Executable contracts need artifact-aware classification rather than documentation heuristics. | `reports/deep-dives/SPEC-REPO-06/index.md`; `reports/deep-dives/SPEC-REPO-06/*.json`; `data/connectedness_features.jsonl` | `https://github.com/open-telemetry/opentelemetry-proto`, `https://github.com/temporalio/api`, `https://github.com/smithy-lang/smithy`, `https://github.com/oapi-codegen/oapi-codegen`, `https://github.com/asyncapi/spec` | contract file counts, code/spec/test LOC, `same_commit_spec_code_count`, contract path samples, API/search failures, redistribution status | `asyncapi/spec` and `smithy-lang/smithy` are hard-quarantined for raw content by the SPEC-REPO-16 gate because lightweight scans flagged secret-like example material. |
| GraphQL, Thrift, TLA+, Dafny, and a large OpenAPI generator broaden executable/formal coverage beyond the first contract scout. | `reports/deep-dives/SPEC-REPO-18/index.md`; `reports/deep-dives/SPEC-REPO-18/validation_report.md`; per-repo JSON/Markdown dossiers | `https://github.com/graphql/graphql-spec`, `https://github.com/apache/thrift`, `https://github.com/tlaplus/tlaplus`, `https://github.com/dafny-lang/dafny`, `https://github.com/OpenAPITools/openapi-generator` | clone mode, history coverage, formal/contract file counts, pygount probe, large sparse fallback, license/compliance status | GitHub code search returned HTTP 401; OpenAPI Generator used a blobless sparse fallback with limited first-parent history coverage. Several records are review-required despite public readability. |
| Non-GitHub public forges host real standards corpora, but discovery and license surfaces differ by host. | `reports/deep-dives/SPEC-REPO-19/index.md`; `reports/deep-dives/SPEC-REPO-19/sources.md`; per-repo JSON/Markdown dossiers | `https://codeberg.org/ariadne/ariadne-identity-specification`, `https://git.sr.ht/~sircmpwn/hare-specification`, `https://bitbucket.org/openid/connect`, `https://gitlab.freedesktop.org/wayland/wayland-protocols` | host-specific discovery endpoints, clone URLs, inspected commits, spec inventories, compliance review notes, sensitive-scan counts/classes | Codeberg, SourceHut, Bitbucket, and self-hosted GitLab were not treated as if they had GitHub-like global code search. Raw export remains metadata-only or review-required except Wayland’s allowed-with-obligations status. |
| Raw publication must fail closed. | `reports/deep-dives/SPEC-REPO-16/COMPLIANCE_EXPORT_GATE.md`; `reports/deep-dives/SPEC-REPO-16/compliance_export_gate.jsonl` rows for SPEC-REPO-05/06 | Public metadata only; upstream URLs preserved above | derived export policy, license status, redistribution status, secret/PII/internal scan status, reason codes | This page deliberately avoids direct long excerpts. Metadata and synthesis are not raw-content permission. |

## Cohort map

### RFC, ADR, and proposal-heavy governance repositories

`SPEC-REPO-05` selected five repositories whose primary artifacts are proposals,
RFCs, enhancement proposals, or improvement standards:

| Repository | Artifact family | Inspected commit | Inventory / LOC signal | Compliance caveat |
|---|---|---:|---|---|
| `rust-lang/rfcs` | language RFCs | `318c2acc1b22` | 641 candidate specs; 198,549 spec LOC; 6,028 approximate spec-changing commits | Apache-2.0; raw export still review-required by the fail-closed gate because PII scan evidence is missing. |
| `kubernetes/enhancements` | KEPs / enhancement proposals | `e2ddea8769ce` | 1,722 candidate specs; 433,941 spec LOC; 33 same-commit spec/code co-change events | Apache-2.0; raw export review-required before release because PII scan evidence is missing. |
| `open-telemetry/opentelemetry-specification` | current specification plus OTEP history | `4034703db495` | 174 candidate specs; 44,601 spec LOC; current specs mixed with proposal history and generation tooling | Apache-2.0; raw export review-required before release because PII scan evidence is missing. |
| `emberjs/rfcs` | framework RFC process | `01909817d773` | 259 candidate specs; 71,191 spec LOC; stage/state movement is a lineage issue | Metadata-only: this pass had no normalized license metadata. |
| `ethereum/EIPs` | EIP/ERC/RIP improvement proposals | `257357a1447c` | 916 candidate specs; 95,465 spec LOC; 95 same-commit spec/code co-change events | CC0-1.0, but fail-closed raw export still needs PII-scan review. |

The useful distinction is not “Markdown versus code.” It is where authority lives.
In proposal-heavy repositories, authority sits in accepted status, numbered files,
stage directories, templates, OWNERS/reviewer process, validation scripts, and
merge history. Implementations often live outside the repository, so same-repo
co-change undercounts coupling by design.

The ADR side remains explicitly incomplete. `SPEC-REPO-05` recorded failed web
searches and a GitHub rate-limit failure, then used high-signal public seed
repositories. That means this page should not be read as an ADR census. It is a
first typological slice, not a triumphal parade.

### Executable contract repositories

`SPEC-REPO-06` and `SPEC-REPO-18` cover API schemas, IDLs, formal specs, and
large generator/test corpora:

| Repository | Contract family | Inspected commit | Evidence signal | Raw/export caveat |
|---|---|---:|---|---|
| `open-telemetry/opentelemetry-proto` | Protocol Buffers telemetry contracts | `62498ba4f8e2` | 13 contract files, 3,236 spec LOC, 29 same-commit spec/code events | Apache-2.0; metadata and synthesis here only. |
| `temporalio/api` | Protocol Buffers service API contracts | `8e0453c3a176` | 64 contract files, 57,382 spec LOC, 64 same-commit spec/code events | MIT; metadata and synthesis here only. |
| `smithy-lang/smithy` | Smithy IDL/model contracts and protocol docs | `a8766999c9af` | 1,728 contract files, 152,227 spec LOC, 738 same-commit spec/code events | Hard-quarantined for raw content by SPEC-REPO-16 due flagged secret-like example scan hits. |
| `oapi-codegen/oapi-codegen` | OpenAPI-driven code generation and regression fixtures | `c346d1273edb` | 13 selected contract files, 966 spec LOC, 80,747 test LOC | Apache-2.0; fixture/authoritative-contract separation is required. |
| `asyncapi/spec` | AsyncAPI JSON Schema and normative spec/examples | `e0078a119c0c` | 25 contract files, 4,255 spec LOC, 4 same-commit spec/code events | Hard-quarantined for raw content by SPEC-REPO-16 due flagged secret-like example scan hits. |
| `graphql/graphql-spec` | GraphQL normative language specification | `1fe9b61b3151` | 12 formal/contract files, 8,994 spec LOC | NOASSERTION; review-required. |
| `apache/thrift` | Thrift IDL compiler/runtime | `c1710f06e13d` | 210 contract/formal files, 17,771 spec LOC, 331 same-commit spec/code events | Apache-2.0; allowed in scout, but this page still publishes metadata only. |
| `tlaplus/tlaplus` | TLA+ formal specification language/toolchain | `209713870170` | 1,056 formal/spec files, 114,444 spec LOC, 308 same-commit spec/code events | MIT but review-required in scout; `.tla` files mix examples, tests, specs, and tool implementation context. |
| `dafny-lang/dafny` | Dafny verification language and proof/program corpus | `6a33d0af6fd7` | 2,201 formal/spec files, 217,081 spec LOC, 1,886 same-commit spec/code events | NOASSERTION; review-required. |
| `OpenAPITools/openapi-generator` | large OpenAPI generator monorepo | `600c13a148ce` | 1,530 contract/formal files and sparse-path analysis over a 65k-file tree | Review-required; blobless sparse fallback and limited history coverage must stay visible. |

Machine-readable contracts invert the ordinary “docs support code” assumption.
A `.proto`, `.smithy`, OpenAPI file, AsyncAPI schema, GraphQL spec chapter,
`.thrift`, `.tla`, or `.dfy` file may be source, test, example, specification,
model, and tool input at once. The scanner therefore needs artifact-family fields,
not just `doc_type = spec`.

## How these differ from Markdown product specs

Markdown product specs, including LLM-facing specs in [[llm-readable-spec-files]],
usually work as durable intent: requirements, non-goals, acceptance criteria,
examples, and verification plans. They can be excellent when structured, but their
force is mostly social and procedural unless a harness links them to tests,
review gates, or code generation.

RFC/proposal repositories are different:

- They record governance over time: draft, accepted, recommended, released,
  stagnant, superseded, or migrated states.
- The lifecycle is often structural: numbered proposal files, stage directories,
  KEP paths, templates, OWNERS/review process, and validation CI.
- Their implementation edge is often external. Rust RFCs, Kubernetes KEPs, Ember
  RFCs, Ethereum EIPs, and OpenTelemetry OTEPs may govern ecosystem code that
  does not live in the same repository.
- A filename alone is weak evidence. The same Markdown pattern may be current
  normative spec, historical proposal, template, rejected idea, or migration note.

Executable contracts are different again:

- OpenAPI and AsyncAPI describe interface surfaces that tools can validate,
  render, generate clients/servers from, or use as conformance fixtures.
- Protocol Buffers and Thrift are IDLs: schema changes carry compatibility and
  generated-code consequences.
- Smithy is a service-modeling IDL with traits, protocol definitions, validators,
  docs, and generated artifacts around a model graph.
- GraphQL’s repository is mostly normative prose and grammar, but the spec defines
  a language contract: validation, execution, response, introspection, and grammar
  semantics are more precise than ordinary product prose.
- TLA+ and Dafny are not “requirements docs.” They are formal or checkable models
  and programs. A `.tla` or `.dfy` file can be a proof/checking surface, a test
  fixture, a tutorial artifact, or implementation-adjacent source; classification
  must preserve that ambiguity instead of sanding it flat.

This is the central modeling rule: artifact class has to be part of the dataset
unit. A product spec, a KEP, an EIP, a `.proto`, a `.smithy` model, a GraphQL
normative chapter, a `.thrift` file, a `.tla` model, and a `.dfy` verified program
are all specification-like, but they imply different authority, validation,
versioning, and coupling mechanisms.

## Non-GitHub standards and protocol corpora

`SPEC-REPO-19` added four public-forge repositories that broaden the cohort beyond
GitHub:

| Repository | Forge | Inspected commit | Spec signal | Publication caveat |
|---|---|---:|---|---|
| `ariadne/ariadne-identity-specification` | Codeberg / Forgejo | `20faf8fe62f5` | 9 Markdown spec files across core, related specs, and ARCs | Review-required because a signature-profile document includes illustrative private-key-like material; no raw examples reproduced. |
| `~sircmpwn/hare-specification` | SourceHut | `91492e0a1b29` | 16 LaTeX language-spec files; build tooling around normative PDF source | Metadata-only because no conventional top-level license was detected. |
| `openid/connect` | Bitbucket | `a139823c56bc` | 57 XML/Markdown standards files; core, discovery, registration, session, identity assurance, and federation drafts | Review-required because no simple repo-level OSS license was found and public contact metadata is present. |
| `wayland/wayland-protocols` | freedesktop GitLab | `e193660a389f` | 69 XML protocol/spec files; stable, staging, experimental, unstable/deprecated phase semantics | Allowed with obligations under MIT/X.org-style license; notice obligations remain. |

The lesson is operationally prosaic and therefore important: discovery is
host-shaped. Codeberg repo search, SourceHut HTML/project pages, Bitbucket
workspace APIs, and instance-local GitLab search are not interchangeable with
GitHub code search. The corpus should preserve host, endpoint, raw retrieval
status, and rejected/fork-heavy candidate evidence before making coverage claims.

## Compliance and public-safety gate

The public-safe boundary for this page is synthesis plus metadata:

| Gate class | Records affected here | Public wiki treatment |
|---|---|---|
| `hard_quarantine_raw_content` | `SPEC-REPO-06:asyncapi__spec`, `SPEC-REPO-06:smithy-lang__smithy` | No raw text excerpts. Only repo URL, commit, counts, paths, and paraphrased interpretation. |
| `metadata_only` | `emberjs/rfcs`, `~sircmpwn/hare-specification`, plus any missing/NOASSERTION or metadata-only rows under the gate | Metadata and synthesis only; no raw corpus bodies. |
| `review_required` / `review_required_before_raw_export` | GraphQL, Dafny, TLA+, OpenAPI Generator, Ariadne, OpenID, and several permissively licensed proposal repos under missing scan evidence | Treat public readability as insufficient for raw publication. Human/legal/security review is a separate gate. |
| `allowed_with_obligations` | `wayland/wayland-protocols` | Preserve license/notice obligations; this page still chooses metadata-only publication. |

The hard-quarantine caveat is not decoration. In the source gate, hard quarantine
means raw content export is blocked even when the upstream repository is public
and permissively licensed, because scan evidence found secret-like example
material. Public examples can still be unsafe to launder into a derived corpus if
the scanner/adjudication contract has not closed.

## Negative evidence and uncertainty

- `SPEC-REPO-05` preserved failed Firecrawl/web-search attempts and GitHub HTTP
  403 rate-limit failures for ADR/RFC discovery. ADR coverage is therefore a
  documented gap, not a census.
- `SPEC-REPO-06` preserved GitHub code-search and API HTTP 403 failures; selected
  executable-contract repos were curated from known public seeds and local clone
  inspection.
- `SPEC-REPO-18` preserved GitHub code-search HTTP 401 and `pygount` availability
  context; OpenAPI Generator’s sparse clone means path-level evidence is not the
  same as full blob/history mining.
- `SPEC-REPO-19` preserved host-specific search limitations and rejected/deferred
  candidates; no non-GitHub host was forced into a GitHub-shaped schema.
- Current-star, issue, and co-change signals are association evidence, not causal
  pressure timelines. The more honest sentence is “associated with,” not “caused
  by.” Tiny wording choices are where datasets either grow bones or become jam.

## Dataset schema implications

For the next corpus schema pass, these cohorts argue for separate fields for:

1. `artifact_family`: `product_spec`, `rfc`, `adr`, `improvement_proposal`,
   `openapi`, `asyncapi`, `protobuf`, `smithy`, `graphql_spec`, `thrift_idl`,
   `tla_model`, `dafny_program_or_proof`, `standards_xml`, `latex_language_spec`.
2. `authority_origin`: standards body, language governance, project governance,
   source-of-truth IDL, generated fixture, conformance test, tutorial/example, or
   external implementation edge.
3. `validation_surface`: lint, schema validation, compiler/codegen, model checker,
   verifier, conformance tests, CI, or human review.
4. `implementation_coupling_scope`: same repo, sibling repo, ecosystem-wide,
   standards body, or unknown.
5. `raw_export_policy`: derived fail-closed status separate from metadata export.
6. `clone_and_history_coverage`: full, blobless, sparse, first-parent-limited,
   rate-limited, or host-specific retrieval.

Without those fields, an RFC and a `.proto` file both become “spec-like text,”
which is true in the same way that a theorem and a Post-it note both contain
symbols. The distinction rather matters.

## Related pages

- [[spec-dataset-evolution-research-project]]
- [[spec-deep-dive-wiki-ingest-project]]
- [[llm-readable-spec-files]]
- [[formal-methods-for-agent-harnesses]]
- [[context-engineering]]
- [[evaluation-and-review-loops]]

## Deep-dive navigation

- Aggregate index: [[spec-deep-dive-index]]
- Priority cases: [[spec-deep-dive-case-jcode]], [[spec-deep-dive-case-droidagent]], [[spec-deep-dive-case-j8-ambiguity]]
- Cohort pages: [[spec-deep-dive-cohort-exact-spec-md-and-standards]], [[spec-deep-dive-cohort-agent-native-spec-kit-kiro]], [[spec-deep-dive-cohort-rfc-adr-executable-contracts]]
