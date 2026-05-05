---
title: Spec dataset evolution Kanban error repair
author: Meridian / Hermes Agent
date: 2026-05-05
accessed: 2026-05-05
ingested: 2026-05-05
source_path: /Users/ericfode/.hermes/gateway-scratch/spec-dataset-evolution/KANBAN_ERROR_REPAIR_2026-05-05.md
kanban_board: spec-dataset-evolution
---

# Kanban error repair — 2026-05-05

Timestamp: 2026-05-05T06:51:02Z
Board: `spec-dataset-evolution`

## Root cause

The board was not failing because of the research tasks themselves. Default-profile Kanban workers were crash-looping during Hermes startup because the globally enabled `basis` plugin registered tool parameter schemas with top-level `anyOf` clauses:

- `basis_reduce_spec`
- `basis_validate_packet`

OpenAI Codex rejected the function schema before the worker could make its first useful model call:

```text
HTTP 400: Invalid schema for function 'basis_reduce_spec': schema must have type 'object' and not have 'oneOf'/'anyOf'/'allOf'/'enum'/'not' at the top level.
```

This affected the running/default workers for:

- `SPEC-DATA-21 / t_383dad01`
- `SPEC-DATA-JCODE / t_63d0e80e`

## Repair applied

Patched local Basis plugin repo:

- Path: `/Users/ericfode/.hermes/plugins/basis`
- Commit: `0061d32 fix: make basis tool schemas codex-compatible`

Change shape:

- removed top-level `anyOf` from the two tool parameter schemas
- moved cross-field requirement guidance into descriptions and kept runtime validation in handlers
- added regression coverage asserting registered parameter schemas do not use provider-rejected top-level composition/negation/enum keywords

Verification:

```text
uv run --extra dev pytest -q
13 passed

hermes -p default chat -q 'Reply exactly OK' -Q --toolsets basis
OK
```

## Board recovery

After the plugin fix:

- `SPEC-DATA-JCODE / t_63d0e80e` completed successfully.
  - Outputs:
    - `outputs/spec_data_jcode_seed_v0_1/jcode_first_calibration_seed.md`
    - `outputs/spec_data_jcode_seed_v0_1/jcode_seed_manifest.json`
    - `work/spec_data_jcode_seed_v0_1/kanban_metadata.json`
- `SPEC-DATA-21 / t_383dad01` generated the required manual-audit gate artifacts, but the spawned worker process lingered after artifact generation. The task was completed manually after deterministic verification.
  - Key output directory: `outputs/spec_data21_manual_audit_gate_v0_1/`
  - Metadata: `work/spec_data21_manual_audit_gate/kanban_metadata.json`
  - Verification: `python3 -m pytest tests/test_spec_data21_manual_audit_gate.py -q` → `3 passed`
  - Gate recommendation: `hold_bounded_staged_expansion`
  - Reason: human primary/dual/adjudicated labels are unresolved; semantic edges remain non-gated; raw content export remains fail-closed.
- `SPEC-DATA-22 / t_977f775e` was dispatched after both parents completed and correctly blocked before crawl work.
  - Block metadata: `work/spec_data22_gate_checked_staged_expansion/kanban_metadata.json`
  - sha256 observed in worker handoff: `ed87aae7dc2ca6cab685696af757fd3b90d30606ba69533e5589342e1e79ba30`
  - Block reason: `SPEC-DATA-21 gate is HOLD, not pass: human primary/dual/adjudicated labels are unresolved, so SPEC-DATA-22 must not run the staged crawl until labels are completed and gate estimates are recomputed.`

## Final board state after repair

```text
triage    0
todo      0
ready     0
running   0
blocked   1
done      45
```

Blocked:

- `SPEC-DATA-22 / t_977f775e`

No active Kanban worker process remained for `t_383dad01`, `t_63d0e80e`, or `t_977f775e` after final verification.

## Interpretation

The original error condition is repaired. The remaining blocked task is intentional and evidence-based, not a runtime failure. The project is now waiting on real human/adjudicated audit labels before staged expansion, which is exactly what the gate was designed to enforce.
