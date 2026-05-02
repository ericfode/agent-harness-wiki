# Synthesis Handoff: Software Verification and Testing Environment Research Map

> Task: t_8b1eb08c | Date: 2026-05-01
> Parents: t_7a29256d (formal verification foundations) | t_77b7318b (testing/evidence primitives) | t_2cf92f9b (agent-facing architecture)
> Target: t_78213be9 (wiki writing lane)

---

## 1. Coherent Research Map

### The story so far

Three research lanes have converged on a single conclusion: an agent-facing software verification environment is not a test runner with a fancy API. It is a structured substrate where specifications, evidence, promotion gates, and regression memory become addressable, versioned, machine-readable objects that an agent can query, reason about, and learn from.

**Lane A (Formal Foundations)** found that deterministic prover feedback neutralizes LLM hallucination. Across proof assistants (VeriSoftBench, LeetProof), contracts (NL2VC-60), model checking (COBALT-TLA), symbolic execution (AutoBug), and runtime verification (Watchdogs & Oracles), the common pattern is a convergent search loop: generate → verify → feed back trace/counterexample → retry. The verifier is not a post-hoc linter; it is a first-class oracle.

**Lane B (Testing Primitives)** mapped five composable evidence primitives: property-based testing, mutation testing, metamorphic testing, coverage-guided fuzzing, and concolic/symbolic testing. The critical insight is that each produces a different *kind* of evidence (counterexample, mutant survival rate, relative invariance violation, branch coverage gap, path constraint). A unified environment must preserve the evidence type, not flatten everything into a pass/fail bit.

**Lane C (Agent-Facing Architecture)** already produced the object model, state machine, and primitive set. The five environment objects are: specification_surface, evidence_ledger, promotion_gate, regression_memory, and trace_tree_node. The promotion pipeline enforces role separation: builders propose, testers verify, reviewers approve, formal verifiers prove.

### Cross-lane architectural themes

| Theme | Lane A | Lane B | Lane C |
|---|---|---|---|
| Verifier as oracle | COBALT-TLA, LeetProof | PBT property violations | evidence_ledger |
| Staged pipeline with early rejection | LeetProof spec validation | Mutation sweep gates | promotion_gate state machine |
| Evidence type preservation | Proof obligation, trace | Counterexample, coverage, mutant | evidence_record with typed result |
| Trace decomposition | CodeTracer failure-onset | Fuzz campaign paths | trace_tree_node |
| Role separation | Dafny assertion inference reviewer | FLARE agentic fuzzing | builder/tester/reviewer/verifier |

### Minimum vocabulary for the research map

- **Specification surface**: the checkable narrowing of intent (assertion, contract, property, theorem, checklist)
- **Evidence record**: durable, hash-addressed, append-only record of a verification run
- **Promotion gate**: mutable state machine tracking where work sits in the acceptance pipeline
- **Regression memory**: prior failures promoted into reusable, evictable specification objects
- **Trace tree**: hierarchical, normalized, write-once index of agent runs with failure-onset localization

---

## 2. Proposed Wiki Change-Set

### New entity pages to create (2)

| Page | Why | Key links |
|---|---|---|
| `entities/cobalt-tla.md` | Strong architectural precedent: LLM + TLC model checker loop with trace feedback. Discovered real exploits. | [[formal-methods-for-agent-harnesses]], [[agent-facing-verifier-environment-architecture]], [[formal-cognition-loop]], [[evaluation-and-review-loops]] |
| `entities/leetproof.md` | Multi-modal verifier pipeline: PBT validation + auto-active reasoning + interactive proof. Spec-first validation pattern. | [[formal-cognition-loop]], [[agent-facing-verifier-environment-architecture]], [[theorem-proving-as-cognitive-kernel]], [[evaluation-and-review-loops]] |

### New raw source notes to create (17-19)

From Lane A (formal foundations):
1. `raw/papers/arxiv-2602.18307-verisoftbench.md` — Repository-scale FM benchmark for Lean 4
2. `raw/papers/arxiv-2604.16584-leetproof.md` — Certified program synthesis with multi-modal verifier
3. `raw/papers/arxiv-2604.22601-nl2vc-60.md` — Dafny-based formal verification from natural language
4. `raw/papers/arxiv-2511.00125-infer-dafny-assertions.md` — LLM inference of missing helper assertions
5. `raw/papers/arxiv-2604.12172-cobalt-tla.md` — Neuro-symbolic verification with TLA+ model checker
6. `raw/papers/arxiv-2604.08633-icepick-glacier.md` — Systematic API testing through model checking + executable contracts
7. `raw/papers/arxiv-2505.13452-autobug.md` — LLM-powered symbolic execution
8. `raw/papers/arxiv-2511.14435-watchdogs-oracles.md` — Runtime verification × LLMs vision paper
9. `raw/papers/arxiv-2506.18315-property-generated-solver.md` — PBT for LLM code generation

From Lane B (testing primitives):
10. `raw/papers/arxiv-2307.04346-llm-pbt.md` — Can LLMs write good property-based tests?
11. `raw/papers/arxiv-2406.09843-llm-mutation-testing.md` — Comprehensive study on LLMs for mutation testing
12. `raw/papers/arxiv-2308.16557-llm-test-generation-mutation.md` — Effective test generation using pre-trained LLMs and mutation testing
13. `raw/papers/arxiv-2504.05289-flare.md` — Agentic coverage-guided fuzzing for LLM-based multi-agent systems
14. `raw/papers/arxiv-2310.15991-whitefox.md` — White-box compiler fuzzing empowered by LLMs
15. `raw/papers/arxiv-2601.12274-hybrid-concolic-llm.md` — Hybrid concolic testing with LLMs for guided path exploration
16. `raw/papers/arxiv-2504.17542-cottontail.md` — LLM-driven concolic execution for structured test input generation
17. `raw/papers/arxiv-2405.00648-drowzee.md` — Metamorphic testing for fact-conflicting hallucination detection
18. `raw/papers/arxiv-2511.02108-metamorphic-testing-llm-nlp.md` — Metamorphic testing of LLMs for NLP

### Updated wiki pages (5)

| Page | What to add |
|---|---|
| `concepts/formal-methods-for-agent-harnesses.md` | Add "verifier as hallucination-free oracle" argument from COBALT-TLA. Add "structural anchor + self-healing" pattern from NL2VC-60. Add "spec-first validation" pattern from LeetProof. Add "dependency burden" insight from VeriSoftBench. |
| `concepts/evaluation-and-review-loops.md` | Add metamorphic relations as primary review technique for non-deterministic LLM pipelines. Add agentic coverage-guided fuzzing (FLARE/WhiteFox) as formal evaluation stage. Add PBT as continuous contract primitive. |
| `concepts/work-management-primitives.md` | Add fuzz campaign and mutation sweep as long-running task primitives. Add constraint/path solver offloads from hybrid concolic testing. |
| `concepts/harness-engineering.md` | Add property-based invariants into the formalization plane. Note architectural need for exposing coverage feedback and mutant survival rates natively to agent runtime. |
| `queries/software-verification-testing-environment-research-program.md` | Close the open questions with answers from all three lanes. Mark the project as having a complete first-pass research foundation. Link to the architecture page. |

### Cross-links to verify

- [[agent-facing-verifier-environment-architecture]] needs links to new [[cobalt-tla]] and [[leetproof]] entities
- [[formal-cognition-loop]] needs links to LeetProof spec-first validation pattern
- [[theorem-proving-as-cognitive-kernel]] needs VeriSoftBench dependency burden insight
- [[rl-gyms-and-executable-environments-for-ai-harnesses]] needs IcePick/Glacier cross-link
- [[self-evolving-workflows]] needs regression_memory connection

### Index update
- Bump total pages from 138 to 140 (2 new entities)
- Add new entities to Entities section
- Add any new raw notes do not appear in index (raw notes are not content pages)
- Update "Last updated" date

### Log update
- Append entry: `## [2026-05-01] ingest | software verification/testing environment research synthesis`
- List all files created/updated

---

## 3. Minimum Viable Environment Architecture

### Components

```
┌─────────────────────────────────────────────────────────────────┐
│                    VERIFICATION ENVIRONMENT                      │
├─────────────────────────────────────────────────────────────────┤
│  SOURCE INGEST LAYER                                             │
│  └── Parse repos, extract contracts, infer properties            │
│      from types, docs, and trajectories                          │
├─────────────────────────────────────────────────────────────────┤
│  SPEC EXTRACTION LAYER                                           │
│  └── Specification library: assertions, contracts, properties,   │
│      theorems, reviewer checklists. Versioned, addressable.      │
├─────────────────────────────────────────────────────────────────┤
│  TEST GENERATION / EXECUTION LANE                                │
│  ├── Unit test runners (pytest, jest, etc.)                      │
│  ├── Property-based testing (Hypothesis, QuickCheck)             │
│  ├── Mutation testing (LLMorpheus-style semantic mutants)        │
│  ├── Coverage-guided fuzzing (FLARE-style agentic fuzz)          │
│  └── Differential / metamorphic testing                          │
├─────────────────────────────────────────────────────────────────┤
│  FORMAL / MODEL-CHECKING LANE                                    │
│  ├── Theorem prover integration (Lean, Dafny, Coq)               │
│  ├── Model checker integration (TLA+/TLC via COBALT-TLA loop)    │
│  ├── Symbolic execution (AutoBug path decomposition)             │
│  └── Runtime verification (Watchdog monitors)                    │
├─────────────────────────────────────────────────────────────────┤
│  EVIDENCE LEDGER                                                 │
│  └── Append-only, hash-addressed records of every verification   │
│      run. Binds spec_ref + run_context + result + artifact_hash  │
│      + reviewer_decision.                                        │
├─────────────────────────────────────────────────────────────────┤
│  PROMOTION GATES                                                 │
│  └── State machine: Proposed → Tested → Reviewed → Proved|Waived │
│      → Accepted. Role-separated transitions.                     │
├─────────────────────────────────────────────────────────────────┤
│  REGRESSION MEMORY                                               │
│  └── Prior failures and counterexamples as reusable spec         │
│      objects. Evictable with decay policy. Linked to evidence.   │
├─────────────────────────────────────────────────────────────────┤
│  REVIEW GATES                                                    │
│  ├── Automated: promotion gate computed fields                   │
│  ├── Agent reviewer: separate evaluator agent with tool access   │
│  └── Human reviewer: explicit approval/waiver with attribution   │
├─────────────────────────────────────────────────────────────────┤
│  REGRESSION MEMORY                                               │
│  └── Prior failures promoted into future checks. Learns from     │
│      evidence ledger. Supports test selection and prioritization.│
└─────────────────────────────────────────────────────────────────┘
```

### Key design decisions

1. **Two-lane architecture**: The test lane and formal lane run in parallel where possible, but the formal lane is not a gate for the test lane. A component can be "tested" without being "proved." The promotion gate tracks both independently.

2. **Evidence is typed, not boolean**: An evidence_record preserves what kind of verification produced it (test, property, proof, model-check, fuzz, mutation) so downstream reasoning can weight appropriately.

3. **Role separation is enforced by the state machine, not by convention**: The promotion gate explicitly rejects builder-initiated transitions beyond "Proposed." This is borrowed from [[another-harness-work-item-closure-environment]] and [[another-harness-evaluator-discipline-environment]].

4. **Regression memory is bounded**: Not all failures deserve permanent storage. A decay policy (age, fix confidence, environment drift suspicion) evicts stale items.

5. **Trace trees support replay**: The trace_forest preserves failure-onset localization from CodeTracer so agent recovery can resume from the exact failing prefix.

---

## 4. Explicit Uncertainties and Kill Criteria

### Uncertainties

| # | Question | Current best guess | Confidence |
|---|---|---|---|
| 1 | **Specification authority** — who may add spec objects? | Agent may propose, operator must approve; inferred specs from trajectories require human validation. | Medium |
| 2 | **Trace tree granularity vs. compression** | Keep full tree for recent runs, compress older trees to failure-onset summaries only. | Medium |
| 3 | **Formal lane integration depth** | Treat theorem prover as privileged transition in promotion gate, but also as regular tool in evidence ledger. Dual status. | Medium |
| 4 | **Anti-gaming at evidence level** | Bind evidence to environment hash + agent turn ID; implement adversarial re-run sampling on promotion. | Low-Medium |
| 5 | **Waiver semantics and governance** | Log all waivers as evidence records with limitation statements; flag waiver petition patterns for operator review. | Medium |
| 6 | **Regression item decay** | Age-based decay with fix-confidence boost; items older than N days without reproduction enter "stale" state. | Low |
| 7 | **Cost of formal lanes** | Lean/Dafny integration may be too slow for interactive agent loops. May need async formal lane with deferred promotion. | Medium |
| 8 | **PBT generator quality from LLMs** | Literature shows LLMs can write properties but struggle with good generators/shrinkers. May need human generator library. | Medium |

### Kill criteria

Criterion | What would trigger it | Consequence
|---|---|---
| **Formal lane latency** | Average proof/model-check time exceeds 5 minutes per agent turn | Demote formal lane to async background task; promotion gate no longer blocks on proof completion
| **Evidence ledger bloat** | Storage growth exceeds 10 GB per 1000 agent turns without compression | Implement mandatory trace tree compression and evidence eviction after 30 days
| **Waiver rate threshold** | >10% of promotions involve waivers rather than evidence | Signal environment failure: either specs are too hard or agent is gaming the system
| **Mutation false positive rate** | >30% of mutants are semantically equivalent or trivially killed | Degrade mutation testing from gate to advisory; investigate LLM mutation operator quality
| **Specification orphan rate** | >20% of spec objects have zero linked evidence after 7 days | Spec library is being written faster than it is being checked; freeze spec authoring until backlog clears
| **Regression memory accuracy** | <50% of regression items reproduce on re-run | Regression memory has become noise; flush and restart with stricter reproducibility requirements
| **Agent trace replay failure** | >15% of failure-onset traces fail to deterministically replay | Trace tree serialization is insufficient; add environment snapshotting or containerization

---

## 5. Verification Checklist

- [x] All three parent research lanes read and synthesized
- [x] Sources mapped to wiki targets (entities, concepts, raw notes)
- [x] New entity pages identified with justification and cross-links
- [x] Raw source notes catalogued with arXiv IDs and one-line relevance
- [x] Updated pages identified with specific content to add
- [x] Index and log update strategy specified
- [x] Minimum viable architecture drawn with components and decisions
- [x] Uncertainties listed with confidence levels
- [x] Kill criteria defined with thresholds and consequences
- [x] Handoff prepared for wiki-writing lane (t_78213be9)

---

*End of synthesis handoff. Forward to wiki-writing lane for durable wiki edits.*
