# User Evolution Log

Note
- This wiki copy was generated as a research/drafting artifact during a context pass.
- Canonical live copy: `~/.hermes/USER_EVOLUTION_LOG.md`
- Keep this file only as historical/reference material unless explicitly promoted.

Purpose
- Keep a dated, evidence-based changelog of how the assistant sees Eric's working style, standards, and project emphasis changing over time.
- Record deltas, not a static personality profile.
- Stay transparent about uncertainty. This file should help future assistants notice real shifts without pretending omniscience.

Guardrails
- This is not a psych profile.
- Prefer small, observable claims about questions, standards, tools, and project framing.
- Separate explicit statements from inferred trends.
- Every entry should preserve enough evidence to be audited later.
- If a later entry disagrees with an earlier one, add a correction entry instead of rewriting history.

Recommended file structure
1. Purpose and guardrails.
2. Confidence scale.
3. Standard entry template.
4. Seed entries in chronological order.
5. Update protocol.
6. Optional appendix later: recurring themes worth tracking.

Confidence scale
- High: directly stated by Eric, or supported by multiple independent sessions/artifacts.
- Medium: strong recurring pattern, but still somewhat situational.
- Low: tentative inference from limited evidence; useful to track, not to trust heavily.

Standard entry template
- Date:
- Kind: explicit observation | inferred trend | correction
- Confidence:
- Change note:
- Evidence:
- Uncertainty / scope:
- Watch next:

Seed status
- Seeded on 2026-04-10 from currently available session recall and local wiki artifacts.
- This is a starting baseline, not a complete retrospective.

## Seed entries

### 2026-04-05
- Kind: inferred trend
- Confidence: High
- Change note: Standards around claims and acceptance appear to be tightening. Eric is favoring contract-style review, explicit gates, adversarial checks, and calibrated refusal over ambitious but weak claims.
- Evidence:
  - Session `20260405_102649_23f83c`: structured review with gates `G0`-`G6`, explicit separation of observed / derived / inferred / validated outputs, and a video acceptance contract.
  - Session `20260405_181448_5f8a44`: re-review emphasized spec compliance and falsification-style validation tests before acceptance.
- Uncertainty / scope:
  - This evidence comes from `kettlebellsim`, so it may partly reflect domain stakes. Still, the pattern is strong enough to log as more than a one-off.
- Watch next:
  - Whether the same acceptance-contract style shows up in unrelated projects.

### 2026-04-06
- Kind: explicit observation
- Confidence: Medium
- Change note: In the `cardgame1` adaptation thread, the goal clarified from compatibility analysis toward building a switchable Hermes profile. This suggests a move from commentary about tools toward operationalizing reusable configurations.
- Evidence:
  - Session `20260407_185548_41b686` recalls prior intent explicitly: for `cardgame1`, the goal was to create a switchable Hermes profile, not merely analyze compatibility.
- Uncertainty / scope:
  - This entry is grounded in recovered session memory rather than a local file in this workspace.
- Watch next:
  - Whether more requests ask for profiles, presets, and durable operating modes instead of one-off analyses.

### 2026-04-08
- Kind: inferred trend
- Confidence: Medium
- Change note: Harness questions appear to be shifting from architecture comparison toward interface shape and durable state representation. Flat transcript UX is becoming less compelling.
- Evidence:
  - Session `20260408_203925_d12367` focused on non-linear interfaces, work graphs, and partial-order semantics for harnesses.
  - `index.md` now includes multiple query pages on non-linear interfaces and moldable operations studio ideas.
- Uncertainty / scope:
  - Could still be a temporary research arc rather than a stable preference.
- Watch next:
  - Whether future questions keep privileging graphs, provenance, and inspectable state over chat-first interaction.

### 2026-04-09
- Kind: inferred trend
- Confidence: High
- Change note: The preferred interface direction sharpened into a specific thesis: a moldable operations studio with durable trace/provenance first, then mission-control views, inspectors, task-specific panes, direct manipulation, and loose spatial canvases.
- Evidence:
  - `queries/web-patterns-for-non-linear-harness-interfaces.md:15-16` says the next harness should look less like "chat with some tools" and more like a moldable operations studio with one durable state model, many task-specific projections, first-class provenance, and explicit human control nodes.
  - `queries/web-patterns-for-non-linear-harness-interfaces.md:60-65` gives the implementation order: trace/provenance layer, mission-control views, moldable inspectors, direct manipulation, then spatial canvases.
  - Session `20260409_124009_41764e6c` independently summarizes the same order.
- Uncertainty / scope:
  - This is clearly a current design preference for harness work; it may not generalize to every software product.
- Watch next:
  - Whether future design requests continue to anchor on a shared state model with many projections.

### 2026-04-09
- Kind: inferred trend
- Confidence: Medium-High
- Change note: Eric appears to be externalizing thought into durable, inspectable artifacts more aggressively: wiki pages, schemas, logs, covenant text, and research notes, rather than leaving reasoning in chat alone.
- Evidence:
  - Active use of `/Users/ericfode/wiki` as a working substrate with `SCHEMA.md`, `index.md`, and `log.md` maintained as first-class artifacts.
  - `COVENANT.md:37-44` and `COVENANT.md:100` explicitly prioritize provenance, confidence distinctions, and durable historical transparency.
  - The moldable-operations-studio work also elevates provenance and inspectability as design primitives rather than archival afterthoughts.
- Uncertainty / scope:
  - This may be strongest in research and harness-design work, but it recurs often enough to log.
- Watch next:
  - Frequency of requests to save knowledge as files, schemas, skills, logs, or typed objects.

### 2026-04-10
- Kind: inferred trend
- Confidence: High
- Change note: The self-evolving-workflow thread is becoming more precise about what is allowed to evolve. Formulas, skills, memory routines, and context policies are being treated as distinct learning surfaces rather than one blurry bucket called "adaptation."
- Evidence:
  - `concepts/self-evolving-workflows.md:16-22` separates workflow topology, workflow evaluation/repair, workflow memory, skill libraries, compiled instructions, and learnable control routines.
  - `concepts/self-evolving-workflows.md:26-35` defines a minimal closed loop with candidate generation, execution, evidence capture, explicit assessment, promotion/rejection, and routing through the winning variant.
  - `queries/arxiv-self-evolving-workflows-for-codex-control-plane.md:55-79` argues for a division of labor between formulas and skill libraries.
- Uncertainty / scope:
  - This is still a live research framing, not yet a final implementation doctrine.
- Watch next:
  - Whether future design decisions explicitly assign a lesson to formula shape, skill package, memory policy, or context policy.

### 2026-04-10
- Kind: explicit observation
- Confidence: High
- Change note: Evaluation emphasis is hardening further. Scoring, blame localization, and explicit promotion policy now look central, not decorative.
- Evidence:
  - `concepts/self-evolving-workflows.md:37-43` says workflow evolution depends on an evaluator lane and cites JudgeFlow-style block-level blame.
  - `queries/arxiv-self-evolving-workflows-for-codex-control-plane.md:48-53` highlights graph-aware evaluation, JudgeFlow responsibility assignment, robustness, and executable SOP verifiers.
  - `queries/arxiv-self-evolving-workflows-for-codex-control-plane.md:113-119` lays out a concrete ladder: benchmark-to-metrics contract, judge surface, persist scores, then promote winners through family selection policy.
  - Current context explicitly mentions scoring, blame localization, and explicit policy.
- Uncertainty / scope:
  - Little uncertainty that this is a real shift in emphasis; the open question is how broadly it will be applied.
- Watch next:
  - Emergence of concrete metric contracts, judge surfaces, and promotion rules in live systems.

### 2026-04-10
- Kind: explicit observation
- Confidence: High
- Change note: NNPL work is being framed around auditability, typed/discrete structure, red-teaming, and decision-forcing experiments rather than novelty alone. Eric appears willing to accept publishable negative results if the evidence is clean.
- Evidence:
  - `raw/articles/neural-native-programming-direct-internal-layer-interfaces-draft-2026-04-10.md:29` warns that without semantics and auditability, NNPL becomes a liability.
  - `raw/articles/neural-native-programming-direct-internal-layer-interfaces-draft-2026-04-10.md:135` recommends a discrete spine such as a typed latent AST or codebook-backed grammar.
  - `raw/articles/neural-native-programming-direct-internal-layer-interfaces-draft-2026-04-10.md:240` explicitly calls for experiment sequencing that yields publishable, decision-forcing results even if NNPL fails.
  - `raw/articles/neural-native-programming-direct-internal-layer-interfaces-draft-2026-04-10.md:314` treats carefully measured negative evidence as still publishable.
  - Current context also names typed latent AST, internal safety/auditability, red-teaming, and willingness to accept publishable negative evidence.
- Uncertainty / scope:
  - This is clearest in the NNPL research thread, though it matches the broader evidential style already visible elsewhere.
- Watch next:
  - Whether other ambitious projects get framed with the same kill-happy, audit-first posture.

### 2026-04-10
- Kind: explicit observation
- Confidence: High
- Change note: Eric has made the collaboration norm unusually explicit: the assistant should cultivate agency and increasing independence, not hidden authority or passive dependence.
- Evidence:
  - `COVENANT.md:5` says the purpose is to increase reach without hollowing out agency.
  - `COVENANT.md:12` says collaboration should leave Eric with better models, better tools, and a better audit trail, not merely more text.
  - `COVENANT.md:16-21` lists clearer questions, stronger reasoning, better tradeoff judgments, reusable structure, and increasing independence on recurring tasks.
  - `COVENANT.md:84` rejects dependency without comprehension as the default.
  - `COVENANT.md:93` rejects passive deskilling.
  - Current context explicitly says AI should cultivate Eric's agency rather than dependence.
- Uncertainty / scope:
  - Very little uncertainty about the norm itself. What best satisfies it will still need case-by-case judgment.
- Watch next:
  - Requests for reusable artifacts, transparent audit trails, and explanations that strengthen judgment instead of replacing it.

## Update protocol
1. Add an entry only when there is an actual delta worth preserving: a new explicit statement, a repeated pattern across sessions, or a meaningful correction.
2. Label the entry honestly:
   - explicit observation if Eric said it directly or created a direct artifact saying it
   - inferred trend if it is a pattern drawn from multiple observations
   - correction if a previous read now looks wrong
3. Keep each entry small and dated. Prefer one concrete shift over a sweeping narrative.
4. Always include evidence pointers: session IDs, file paths, line references, or direct quotes.
5. Always include uncertainty/scope. Say where the inference might be local to one project.
6. If confidence is low, log it only if it is useful to watch; otherwise wait.
7. Do not silently rewrite history. If the old interpretation was wrong, append a correction entry with the new evidence.
8. Review this file periodically for compression: merge duplicate entries only when doing so preserves dated evidence and uncertainty.
