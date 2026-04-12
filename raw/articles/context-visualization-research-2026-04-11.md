# Context visualization research batch

Date: 2026-04-11
Collector: Meridian (Hermes)
Method: local wiki grounding plus direct terminal fetches against arXiv, ACL Anthology, DOI/Crossref, product docs, and project documentation when `web_search` / `web_extract` were unreliable.

## Scope
- Better ways to show users what context is being assembled, from where, and under which trust conditions.
- Honest UI for source provenance, trust state, and influence.
- What can and cannot be shown about “what the model is attending to now”.

## Provenance and trust visualization anchors

1. PROV-DM (W3C)
   - URL: https://www.w3.org/TR/prov-dm/
   - Notes: provenance should model entities, activities, agents, derivation, attribution, revision, and invalidation as first-class relations.

2. in-toto (2019)
   - URL: https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias
   - Notes: signed provenance metadata attached to workflow steps; good anchor for trust as inspectable evidence rather than ambient status.

3. Provenance and Annotation for Visual Exploration Systems (2006)
   - URL: https://doi.org/10.1109/TVCG.2006.101
   - Notes: replayable history plus annotations; supports revisit/explain/share rather than only final results.

4. Provenance Semirings (2007)
   - URL: https://doi.org/10.1145/1265530.1265535
   - Notes: formal lineage should survive derivation and composition instead of being flattened.

5. ModelTracker (2015)
   - URL: https://doi.org/10.1145/2702123.2702509
   - Notes: strongest compact pattern for binding aggregate summaries to concrete example-level failures.

6. The What-If Tool (2019)
   - URL: https://doi.org/10.1109/TVCG.2019.2934619
   - Notes: interactive counterfactual editing and subset comparison without bespoke coding.

7. From Common Operating Picture to Situational Awareness (2014)
   - URL: https://doi.org/10.1504/IJEM.2014.061659
   - Notes: one shared picture, but role-specific interpretation and situational views.

8. Design of a role-based trust-management framework (2002/2005 record)
   - URL: https://doi.org/10.1109/secpri.2002.1004366
   - Notes: trust stays local and policy-based; avoid global scalar trust scores.

9. ClaimChain (2017)
   - URL: https://arxiv.org/abs/1707.06279
   - Notes: append-only claims and beliefs with selective sharing; useful for observer-relative trust evidence.

10. W3C Verifiable Credentials Data Model v2.0
    - URL: https://www.w3.org/TR/vc-data-model-2.0/
    - Notes: portable attestations and selective disclosure.

11. Evaluation of Filesystem Provenance Visualization Tools (2013)
    - URL: https://doi.org/10.1109/TVCG.2013.155
    - Notes: raw node-link provenance views do poorly at high-level summary; grouped and time-oriented views help.

12. AVOCADO: Visualization of Workflow-Derived Data Provenance for Reproducible Biomedical Research (2016)
    - URL: https://doi.org/10.1111/cgf.12924
    - Notes: large provenance graphs need hierarchical aggregation and degree-of-interest expansion.

13. Characterizing Provenance in Visualization and Data Analysis (2016)
    - URL: https://doi.org/10.1109/TVCG.2015.2467551
    - Notes: provenance has multiple types and uses; UI should not collapse them into one undifferentiated story.

14. Uncertainty as a Form of Transparency (2021)
    - URL: https://doi.org/10.1145/3461702.3462571
    - Notes: uncertainty display is core transparency, not garnish.

15. Augmenting Web Pages and Search Results to Support Credibility Assessment (2011)
    - URL: https://doi.org/10.1145/1978942.1979127
    - Notes: credibility cues work best inline at point of use rather than hidden in a separate panel.

## Attention and attribution anchors

1. Attention is not Explanation (2019)
   - URL: https://arxiv.org/abs/1902.10186
   - Notes: strong warning against treating raw attention weights as faithful explanations.

2. Attention is not not Explanation (2019)
   - URL: https://aclanthology.org/D19-1002/
   - Notes: qualified rebuttal; attention can be useful under disciplined evaluation, but not by default.

3. What Does BERT Look at? An Analysis of BERT’s Attention (2019)
   - URL: https://aclanthology.org/W19-4828/
   - Notes: attention heads reveal real structure and specialization, but that is different from full answer explanation.

4. Quantifying Attention Flow in Transformers (2020)
   - URL: https://arxiv.org/abs/2005.00928
   - Notes: attention rollout / flow are better input-level summaries than raw attention alone, but still derived heuristics.

5. A Multiscale Visualization of Attention in the Transformer Model / BertViz (2019)
   - URL: https://aclanthology.org/P19-3007/
   - Tool: https://github.com/jessevig/bertviz
   - Notes: practical open-weight attention inspection tool; good for diagnostics, not a final user-facing explanation on its own.

6. Ecco
   - URL: https://github.com/jalammar/ecco
   - Docs: https://ecco.readthedocs.io/en/main/
   - Notes: saliency, attribution, and neuron views beyond raw attention.

7. LIT (Learning Interpretability Tool)
   - URL: https://github.com/PAIR-code/lit
   - Docs: https://pair-code.github.io/lit
   - Notes: strong browser UI for salience maps, counterfactuals, and side-by-side interpretability views.

8. MIRAGE: Model Internals-based Answer Attribution for Trustworthy RAG (2024)
   - URL: https://arxiv.org/abs/2406.13663
   - Notes: answer-to-document attribution using model internals; useful for “which retrieved source supported this answer span?”

9. VISA: Retrieval Augmented Generation with Visual Source Attribution (2025)
   - URL: https://aclanthology.org/2025.acl-long.1456/
   - Notes: source attribution via exact evidence regions in the original document images/pages.

10. Source Attribution in Retrieval-Augmented Generation (2025)
    - URL: https://arxiv.org/abs/2507.04480
    - Notes: document-level attribution with redundancy, complementarity, and synergy between retrieved documents.

11. TokenShapley (2025)
    - URL: https://aclanthology.org/2025.findings-acl.200/
    - Notes: token-level contribution estimates for context attribution.

12. Lost in the Middle (2023)
    - URL: https://arxiv.org/abs/2307.03172
    - Notes: prompt position materially changes actual use of context; retrieval score is not the same thing as influence.

## Context-assembly UX anchors

1. Sourcegraph Cody Context
   - URL: https://sourcegraph.com/docs/cody/core-concepts/context
   - Notes: explicit context picker, visible retrieval modes, and clear inclusion pathways.

2. NotebookLM Sources panel
   - URL: https://support.google.com/notebooklm/answer/16215270?hl=en&co=GENIE.Platform%3DDesktop
   - Notes: user-facing source-set control and citation-oriented source views.

3. LangGraph Studio
   - URL: https://blog.langchain.com/langgraph-studio-the-first-agent-ide/
   - Notes: graph-first agent interface rather than transcript-first inspection.

4. LangSmith observability
   - URL: https://docs.langchain.com/langsmith/observability-quickstart
   - Notes: nested traces for retrieval/tool/LLM calls; useful prompt-assembly provenance pattern.

5. Arize Phoenix
   - URL: https://github.com/Arize-ai/phoenix
   - Notes: tracing plus retrieval/groundedness evaluation over RAG and agent flows.

6. TruLens
   - URL: https://www.trulens.org/
   - Notes: context relevance and groundedness evaluations attached to execution traces.

7. Whyline
   - URL: https://doi.org/10.1145/1518701.1518942
   - Notes: click output -> traverse causes / why-not chain.

8. Jigsaw
   - URL: https://doi.org/10.1057/palgrave.ivs.9500180
   - Notes: coordinated multi-view evidence workspace.

9. Analyst’s Workspace
   - URL: https://doi.org/10.1109/VAST.2012.6400559
   - Notes: spatial evidence and hypothesis arrangement as active analysis state.

## Provisional synthesis
- The UI should separate three layers that products often blur:
  1. exact assembly provenance
  2. trust / verification / uncertainty state
  3. influence or salience estimates
- Source selection score is not the same thing as actual answer influence.
- “What the model is attending to now” should usually be framed as a selected-token diagnostic for open-weight models, or as a proxy estimate for API-only models.
- One canonical context/provenance substrate should back a shared common operating picture and role-specific situational panes.
- Trust should be displayed as evidence state vectors and receipts, not as a scalar reputation score.
- The smallest serious UI should show Included / Candidate / Dropped sources, why chips, answer-to-source traversal, and a with/without-source compare affordance.
