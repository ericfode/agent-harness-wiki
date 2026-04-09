---
title: UI Overview — Airflow
author: Apache Airflow
url: https://airflow.apache.org/docs/apache-airflow/stable/ui.html
date: unknown
accessed: 2026-04-09
ingested: 2026-04-09
---

# UI Overview — Airflow

**Source:** [Airflow docs](https://airflow.apache.org/docs/apache-airflow/stable/ui.html)
**Topic:** Multiple supervisory views over workflow fleets.

## Core idea
Airflow's UI includes list, details, grid, graph, run, task-instance, event, and code views. The key lesson is not merely that workflows exist, but that different supervisory questions need different visual projections.

## Key claims
- Grid and graph views answer different operational questions.
- Run-specific views are useful alongside workflow-wide views.
- Code, events, logs, and structure belong in one navigable supervisory surface.

## Harness takeaway
A harness for many agents or branches should not rely on a single graph alone. Matrix/grid views are often better for spotting retries, flakes, stuck work, or systemic failure patterns across many runs.
