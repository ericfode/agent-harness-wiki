---
title: "CodeTracer: Towards Traceable Agent States"
author: "arXiv authors (extracted from arXiv:2604.11641)"
ingested: 2026-05-01
---

# CodeTracer: Towards Traceable Agent States

**Paper:** arXiv:2604.11641v1 (April 2026)

## Core claim
Agent execution produces heterogeneous run directories that are difficult to inspect after the fact. CodeTracer converts them into structured hierarchical traces, enables failure-onset localization, and supports diagnostic feedback injection (reflective replay) that can recover failed runs under the same token budget.

## Three-stage pipeline
1. **Evolving Extraction:** Scans run directories and synthesizes typed parsers per framework (OpenHands, SWE-Agent, etc.)
2. **Tree Indexing:** Flattens sequences into a Hierarchical Trace Tree with exploration nodes and state-changing nodes
3. **Failure Onset Localization:** Identifies the earliest error-critical step that triggered the downstream cascade

## Key findings
- Agents often gather correct diagnostic evidence but fail to act on it (Evidence-to-Action Gap)
- Complex frameworks consume ~2x tokens for +2–5% success over lightweight baselines
- Success rates plateau around 40 iterations; extra iterations usually produce unproductive loops
- Stage-dependent errors: early = environment/setup; later = mislocalized edits and incorrect hypotheses

## Reflective Replay
CodeTracer's diagnostic signals, when fed back as prefix hints, consistently recover originally failed runs under the same budget. This proves the signals are actionable rather than merely descriptive.

## Relevance to harness design
CodeTracer validates that raw run artifacts are insufficient for harness-native verification. Normalized traces, typed nodes, and failure-onset indices are prerequisites for agent-facing evidence surfaces. The trace-tree node is a candidate primitive for the evidence ledger and regression memory in harness architecture.

## Sources
- arXiv:2604.11641v1
