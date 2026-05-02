# Synthesis: Software Verification and Testing Environment Research Map

> Task: t_8b1eb08c | Parents: t_7a29256d (formal foundations), t_77b7318b (testing primitives), t_2cf92f9b (agent architecture)
> Date: 2026-05-01
>
> This is the structured handoff from synthesis to wiki-writing lane (t_78213be9).
> It contains: (1) the unified research map, (2) recommended wiki change-set,
> (3) minimum viable architecture, (4) uncertainties and kill criteria.

---

## 1. Unified Research Map

### What the three lanes actually produced

**Lane A — Formal Verification Foundations (t_7a29256d)**
The raw formal-methods literature was already substantially present in the wiki before this research project began. The key papers from the formal-methods pass (2026-04-08, 2026-04-09) include:

- arxiv-zhang-2024-formal-methods-trustworthy-ai-agents — roadmap for LLM+FM fusion
- arxiv-lahiri-2026-intent-formalization — the intent-gap framing and specification-to-implementation spectrum
- arxiv-song-2024-lean-copilot — proof assistants as copilots rather than post-hoc verifiers
- arxiv-miculicich-2025-veriguard-verified-code-generation — offline policy verification + runtime monitoring split
- arxiv-zou-2025-blocka2a-secure-verifiable-interoperability — agent-to-agent verification at protocol level
- arxiv-ben-khaled-2026-g2cp-graph-grounded-communication-protocol — structured reasoning traces as verifiable artifacts
- arxiv-allen-2025-sound-complete-neurosymbolic-reasoning — soundness/completeness constraints on LLM-informal-to-formal bridges

These sources serve the project indirectly: they establish that formal methods are a credible frontier, but they do not by themselves define the operational object model a harness needs.

**Lane B — Testing and Evidence Primitives (t_77b7318b)**
The parallel task gathered 10 key papers on agentic testing primitives and formulated a taxonomy. The papers were not captured as raw wiki sources (they may be in the deliverable file `lane-b-testing-primitives.md` which was not recoverable from workspace). However, the project's own taxonomy references the following technique classes:

- Property-based testing (QuickCheck family, Hypothesis)
- Mutation testing (assessment of test suite adequacy)
- Metamorphic testing (relational properties across input variants)
- Concolic / symbolic execution (mixed concrete/symbolic path exploration)
- Fuzzing (coverage-guided, grey-box, structure-aware)
- Differential testing (cross-implementation consistency)
- Coverage instrumentation (code, branch, path, state)
- Shrinking / minimization (counterexample reduction)
- Reproducible CI / deterministic replay

The key insight from Lane B: not all testing techniques produce agent-usable evidence. Agent-facing evidence must be addressable, hash-bound, replayable, and translatable into a review decision. A coverage report alone is not evidence unless attached to a specification object and a promotion gate decision.

**Lane C — Agent-Facing Architecture (t_2cf92f9b)**
This task was the primary upstream deliverer. Its output (already committed to the wiki on 2026-05-01) includes:

- `queries/agent-facing-verifier-environment-architecture.md` — 5 primitives, object model, promotion state machine, 6 open design questions
- Raw source: `raw/papers/code-tracer-towards-traceable-agent-states.md` — hierarchical trace indexing, failure-onset localization, reflective replay

The Lane C synthesis identifies the concrete primitives: specification_surface, evidence_ledger, promotion_gate, regression_memory, trace_tree_node.

### How the three lanes fit together

```
Lane A (Formal)                Lane B (Testing)                Lane C (Architecture)
     |                               |                               |
     |-- intent formalization        |-- property tests               |-- spec_surface
     |-- proof assistants            |-- mutation / metamorphic       |-- evidence_ledger
     |-- model checking              |-- fuzzing + shrinking          |-- promotion_gate
     |-- runtime verification        |-- differential testing         |-- regression_memory
     |-- coordination protocols      |-- reproducible CI              |-- trace_tree_node
              \                           |                           /
               \                          |                          /
                \                         |                         /
                 +------------------------+-------------------------+
                                          |
                                          v
                        Unified Object Model + Promotion Pipeline
                                          |
                        +--- Formal lane as privileged gate
                        +--- Test lane as default path
                        +--- Architecture as shared substrate
```

The model is not a union of tools. It is a hierarchy of urgency:

1. **First-line evidence**: executable tests, property checks, differential checks — fast, cheap, composable.
2. **Second-line evidence**: formal proofs, model-checked properties, verified policies — expensive but definitive.
3. **Structural substrate**: evidence ledger, promotion gates, regression memory, trace trees — make the evidence durable, queryable, and reviewable.

A harness should default to line 1, escalate to line 2 when cost is justified or risk is high, and always write to line 3.

---

## 2. Proposed Wiki Change-Set

### New raw source notes to add

The following raw notes should be added (ideally committed by the wiki-writing lane, or flagged as off-wiki deliverables if the source material is too thin for a formal summary):

| Source | File name | Rationale |
|---|---|---|
| Lane B testing taxonomy (10 papers) | `raw/articles/lane-b-testing-primitives-2026-05-01.md` | Preserve the taxonomy even if full paper deep-dives are deferred |
| Lane A formal-methods roadmap synthesis | Already ingested via existing raw notes |
| CodeTracer paper (Lane C) | Already ingested: `raw/papers/code-tracer-towards-traceable-agent-states.md` |

### Concept/entity pages to create

1. **concepts/specification-surfaces.md** — Formalize the concept of a checkable specification object (assertion, contract, property, theorem, temporal property, reviewer checklist). This is the narrowing surface between intent and evidence.

2. **concepts/evidence-ledgers.md** — The durable append-only record structure for verification runs, complementing evaluation-and-review-loops.

3. **concepts/regression-memory.md** — Prior failures as reusable specification objects, with eviction policy and decay semantics.

4. **entities/code-tracer.md** — If the paper warrants a dedicated entity page (central enough, referenced repeatedly). Alternatively, keep it as a raw note only.

5. **queries/parity-check-verification-testing-environment-map.md** (or better: expand the existing `software-verification-testing-environment-research-program.md`) — Update the project anchor with the unified map, cross-referencing all three lanes and the new concept pages.

### Pages to update

| Page | Update | Rationale |
|---|---|---|
| `queries/software-verification-testing-environment-research-program.md` | Expand with the unified map, component architecture, and new concept links | Project anchor should absorb synthesis output |
| `concepts/formal-methods-for-agent-harnesses.md` | Add explicit note about the three-lane project and link to spec_surfaces | Drive home that formal methods are not the only lane |
| `concepts/evaluation-and-review-loops.md` | Add evidence_ledger and promotion_gate as loop objects | Loops need durable state, not just per-run checks |
| `concepts/work-management-primitives.md` | Add promotion states as a work-primitive variant | The promotion pipeline is a work-management pattern |
| `concepts/harness-engineering.md` | Add verification-environment as a next-layer concern | Harness engineering should include verification substrate design |
| `index.md` | Add new concept pages, bump page count | Mandatory per SCHEMA |

### Cross-links to enforce

Every new page must link to at least 2 existing pages.

- `specification-surfaces` -> `formal-methods-for-agent-harnesses`, `formal-cognition-loop`, `evaluation-and-review-loops`
- `evidence-ledgers` -> `evaluation-and-review-loops`, `work-management-primitives`, `agent-facing-verifier-environment-architecture`
- `regression-memory` -> `memory-persistence`, `self-evolving-workflows`, `evidence-ledgers`
- `software-verification-testing-environment-research-program` (updated) -> all new concept pages, all lane pages, `agent-facing-verifier-environment-architecture`

---

## 3. Minimum Viable Environment Architecture

### Components

| Component | Responsibility | First-class state | Analogous systems |
|---|---|---|---|
| **Source Ingester** | Accepts code, specs, tests, and intent documents; produces specification_surface objects | `spec_library` (addressable, versioned) | SWE-Gym episode substrate, AppWorld task ingest |
| **Spec Extractor** | Narrows natural-language intent into checkable specifications (assertions, contracts, properties, theorems) | `spec_surface` objects with provenance | Lahiri intent-formalization pipeline, nl2postcond |
| **Test Generation Executor** | Runs unit tests, property tests, fuzz targets, mutation suites, differential checks; emits evidence records | `evidence_records` (addressable, hash-bound, append-only) | pytest, Hypothesis, AFL++, LibFuzzer, SWE-Gym verifier |
| **Proof / Model-Checking Lane** | Runs theorem provers, SMT solvers, model checkers; emits proof/witness/failure records | Same `evidence_records` with privileging metadata | Lean, Z3, TLA+, CBMC, Kani |
| **Evidence Ledger** | Append-only store of all runs, results, counterexamples, environment hashes, reviewer decisions | `evidence_records[]`, hash-addressed | CodeTracer trace tree, SWE-Gym trajectory store |
| **Promotion Gates** | Mutable state machine tracking where an artifact sits in the acceptance pipeline | `promotion_states` (proposed→tested→reviewed→proved→accepted) | PR review state, CI gate status |
| **Regression Memory** | Prior failures and counterexamples retained as reusable specification objects | `regression_items` with decay/acceptance status | Regression test suites, known-failure tracking |
| **Review Gates** | Explicit reviewer decisions (human or agent) with recorded verdict and rationale | `review_decisions` linked to evidence records | Claude Code evaluator, PR triage workflows |
| **Regression Memory (Reprise)** | Same as above, but note: it is separate from promotion gates because promotion is about the current artifact, regression memory is about historical evidence | | |

### Data flow

```
             +----------------+
             | Source Ingest  |
             +--------+-------+
                      |
                      v
             +--------+-------+
             | Spec Extractor |
             +--------+-------+
                      |
         +------------+------------+
         |                         |
         v                         v
+--------+----------+   +---------+--------+
| Test Generation   |   | Proof / Model    |
| & Execution       |   | Check Lane       |
+--------+----------+   +---------+--------+
         |                         |
         +------------+------------+
                      |
                      v
             +--------+-------+
             | Evidence Ledger|
             +--------+-------+
                      |
         +------------+------------+
         |                         |
         v                         v
+--------+----------+   +---------+--------+
| Promotion Gates   |   | Regression     |
| (state machine)   |   | Memory         |
+-------------------+   +----------------+
```

### Promotion pipeline state machine

```
[*] --> Proposed        (agent submits work)
Proposed --> Tested     (evidence ledger shows passing tests)
Tested --> Reviewed     (reviewer gate approved)
Reviewed --> Proved     (formal lane completes proof/verification)
Reviewed --> Rejected   (reviewer requests changes)
Proved --> Accepted     (promotion gate updated)
Rejected --> Proposed   (agent revises and resubmits)
Tested --> Rejected     (tests fail after revision)
Proved --> Waived       (operator overrides proof requirement)
Waived --> Accepted     (promotion gate updated)
```

Invariants:
- A builder may not advance its own gate beyond Proposed.
- An evaluator may not advance beyond Tested.
- A waiver is always logged as an evidence_record with limitation statement.
- Rejection returns to Proposed (preserves retry context, does not discard).

### Kill criteria for the environment (when to stop and reconsider)

1. If >50% of agent runs produce evidence records that no downstream consumer queries or acts on, the ledger is write-only noise. Stop and redesign evidence addressability.
2. If formal lane integration adds >3x runtime overhead without catching bugs that tests miss, the proof lane is mis-scoped. Kill the privileged proof gate; demote to optional.
3. If regression memory grows faster than evidence records, the decay policy is absent or broken. Fix eviction before adding more sources.
4. If promotion gates become majority "waived," the enforcement surface is ceremonial. Revert to explicit operator approval with audit trail.
5. If trace trees exceed storage budget and failure-onset localization is lost in summarization, the trace granularity is wrong. Move to sampled or delta trees.

---

## 4. Explicit Uncertainties

### What we still do not know

1. **Agent specification authority.** Who may add a specification object — agent, operator, requirements agent, or inferred from trajectories? This changes the trust model but was not resolved by any lane.

2. **Trace tree compression at scale.** CodeTracer shows full-tree indexing works, but at harness scale this may exceed context-window or storage budgets. No lane resolved the summarization policy.

3. **Formal lane integration depth.** Should a theorem prover be just another tool in the evidence ledger, or a privileged transition in the promotion gate? Lane A points toward privileging; Lane C points toward ledger neutrality. Not resolved.

4. **Evidence anti-gaming.** If evidence records are durable and hash-addressed, an agent could replay old successful evidence to mask a regression. The ledger needs freshness checks, environment-hash binding, and adversarial re-run sampling. Lane B hinted at this but no concrete mechanism was proposed.

5. **Waiver semantics and governance.** A waiver is a decision to accept without evidence. How should waiver petitioning be detected and surfaced so agents do not learn to game the state machine?

6. **Regression item decay.** Not all historical failures deserve permanent memory. A principled eviction or demotion policy is needed, but no lane proposed one.

7. **Lane B source material gap.** The 10 testing-primitive papers were gathered but not materialized as raw wiki notes. If the `lane-b-testing-primitives.md` file is unrecoverable, the wiki-writing lane may need to re-ingest them or accept a partial bibliography.

8. **Lane A vs. Lane A+1.** The formal-methods literature is broad. The project captured ~9 papers but may have missed critical sub-areas: SMT solver interfaces, bounded model checking for industry, runtime monitors for agents, and compositional verification. These are acknowledged gaps, not fatal if the project scope is "first architecture" rather than "complete survey."

---

## 5. Artifacts Produced by This Synthesis

1. This file: `synthesis-software-verification-testing-environment.md` (in workspace, to be archived or moved to wiki if persisted)
2. Recommendations for 3 new concept pages, 4 updated pages, 1 potential entity page
3. Promotion pipeline state machine (Mermaid)
4. Data flow diagram (ASCII)
5. Kill criteria list (5 conditions)
6. Uncertainty list (8 items)

---

## Handoff to t_78213be9 (Wiki Writing)

The wiki-writing worker should:

1. Read this synthesis file.
2. Check whether `lane-b-testing-primitives.md` exists anywhere in the workspace tree (it was recorded as missing at synthesis time). If found, use it; if not, create a minimal raw note capturing the taxonomy (property-based, mutation, metamorphic, concolic, fuzzing, differential, coverage, shrinking, CI replay) and cite the 10 papers by title/year if titles are available in run metadata.
3. Create the 3 new concept pages with YAML frontmatter per SCHEMA.md.
4. Update the listed existing pages.
5. Update `index.md` and `log.md`.
6. Run `scripts/lint-wiki.sh`.
7. kanban_complete with the actual files changed.
