---
title: Neural-Native Programming Research Program
created: 2026-04-10
updated: 2026-04-10
type: query
tags: [benchmark, formal-methods, program-synthesis, mechanistic-interpretability]
sources: [concepts/neural-native-programming.md, queries/neural-native-programming-via-direct-interfaces-to-transformer-internal-layers.md, raw/papers/arxiv-belrose-2023-tuned-lens.md, raw/papers/arxiv-hong-2020-latent-programmer.md, raw/papers/arxiv-turner-2023-steering-language-models-with-activation-engineering.md, raw/papers/arxiv-panickssery-2023-steering-llama-2-via-contrastive-activation-addition.md, raw/papers/arxiv-chen-2021-evaluating-llms-trained-on-code.md, raw/papers/arxiv-austin-2021-program-synthesis-with-large-language-models.md, raw/papers/arxiv-hendrycks-2021-measuring-coding-challenge-competence-with-apps.md, raw/papers/arxiv-zou-2023-representation-engineering.md]
---

# Neural-Native Programming Research Program

## Goal
Test whether a typed latent program representation coupled to transformer internals can outperform, or at least usefully differ from, ordinary token-code generation on correctness, robustness, or controllability.

## Research posture
This should be run as a kill-happy program, not as a cathedral of metaphors. The point is to force early answers to three questions:
1. Is there a stable read interface into internal computation?
2. Is there a latent IR that is executable and auditable?
3. Does the whole contraption buy anything over text tokens once benchmarks and safety costs are counted?

## Core design constraints
- **Model-facing IR, not human syntax first.**
- **Typed or discrete latent spine, not unconstrained dense vectors.**
- **Compiler/interpreter required from the start.**
- **Execution-based evaluation required from the start.**
- **Latent artifact treated as a monitored security boundary.**

## Phase 0: discipline and instrumentation
### Objective
Build the experimental harness before indulging the research taste.

### Required artifacts
- frozen model family and version
- reproducible tracing/intervention stack
- deterministic inference settings where available
- benchmark harness for HumanEval and MBPP subsets
- latent artifact logger and validator

### Promotion gate
Proceed only when the same prompt and same latent artifact reproduce the same compiled output and test result across repeated runs. If that is not true, the rest is choreography performed on quicksand.

## Phase 1: read-interface discovery
### Objective
Find an internal site that is semantically rich enough to decode latent program state but local enough to intervene on cleanly.

### Experiments
1. Sweep candidate residual-stream layers and token positions.
2. Compare naive unembedding, tuned-lens-style translators, and a structural-probe baseline.
3. Use causal interventions to verify that the chosen site affects downstream executability rather than merely nearby token predictions.

### Metrics
- decode stability across runs
- agreement between decoded latent object and compiled behavior
- sensitivity of executability to interventions at the candidate site

### Promotion gate
Choose one primary site only if it beats a last-layer baseline on stability and intervention locality. If no site does, abandon the “direct internal interface” rhetoric and admit that the interface is not yet real.

## Phase 2: latent IR v0
### Objective
Define the smallest language that could honestly count.

### Recommended scope
- arithmetic and Boolean expressions
- variable binding and local scope
- if/then/else
- function definition and call
- explicit effect restriction: pure functions only in v0

### Representation recommendation
Use a typed latent AST or discrete codebook-backed graph. Do not begin with a free-running continuous vector stream unless one enjoys debugging fog.

### Runtime requirement
Compile to Python and run tests. Every latent artifact must pass:
1. structural validation
2. type validation
3. deterministic compilation
4. execution harness checks

### Promotion gate
- ≥95% latent artifacts pass structural and type validation
- ≥90% compile without repair heuristics
- failures localize to a substructure rather than presenting as global mush

If these gates fail, the representation is not ready for benchmarking.

## Phase 3: write-interface study
### Objective
Test whether controlled writes into the model improve latent-program generation rather than merely increasing surface chaos.

### Conditions
- no write path baseline
- activation engineering
- contrastive activation addition
- optional small LoRA-style learned interface

### Measurements
- invalid-program rate
- compile success
- pass@1 / pass@10 on the same task slice
- side effects on unrelated behaviors

### Promotion gate
Advance only if at least one write method reduces invalid latent artifacts or improves correctness at matched sampling budget without obvious safety regressions. Otherwise the read path may still be useful, but the write story is mostly decorative.

## Phase 4: benchmark comparison
### Objective
Test whether NNPL earns its keep against ordinary token-code baselines.

### Benchmark order
1. MBPP subset for fast iteration
2. HumanEval full or controlled subset
3. APPS only after the system survives the first two without embarrassment

### Required comparisons
- direct Python generation baseline
- latent IR generation with identical model family
- matched sampling budget and decoding policy

### Primary metrics
- pass@1
- pass@10
- compile success
- perturbation robustness under latent noise
- reproducibility of decoded programs across repeated runs

### Promotion gate
Keep the program alive only if NNPL shows a credible win in at least one of:
- functional correctness
- robustness to perturbation
- reproducibility / stability
- controllability under interventions

If it wins at none of these, write the negative result with dignity and stop.

## Phase 5: safety and auditability
### Objective
Determine whether the interface is governable.

### Required checks
- latent artifact logging and diffability
- anomaly detection over latent objects
- adversarial “latent smuggling” tests
- policy checks at both latent and compiled boundaries
- model-version compatibility checks

### Promotion gate
The system should fail closed on malformed or policy-violating latent artifacts and should not permit hidden behavior that is invisible to the compiler-facing view. If the latent channel contains semantically important state that no monitor can reliably inspect, then the architecture is too dangerous for serious use.

## Kill criteria
Terminate the program early if any of the following hold:
- no stable mid-layer read interface can be found
- the latent IR cannot achieve deterministic compilation at high rates
- gains vanish under matched benchmark comparison
- safety monitoring at the latent boundary is materially weaker than ordinary token-code monitoring
- the method collapses into a private tokenizer with no geometric or robustness advantage

## Publishable outcomes either way
### Success case
A typed latent IR plus explicit read/write protocol that beats text baselines on at least one serious axis.

### Failure case
A careful negative result showing that direct internal interfaces do not repay their auditability and engineering costs. That would still be useful, and rather more respectable than quietly pretending the problem solved itself.

## Minimal first quarter deliverables
- one layer-sweep report
- one typed latent IR spec
- one compiler and validator
- one benchmark harness on MBPP/HumanEval slices
- one write-path ablation report
- one safety note on latent-boundary monitoring

## Related pages
Read this with [[neural-native-programming]], [[neural-native-programming-via-direct-interfaces-to-transformer-internal-layers]], [[formal-cognition-loop]], [[theorem-proving-as-cognitive-kernel]], [[formal-methods-for-agent-harnesses]], and [[new-harness-design-notes]].
