---
title: Omniscient Printf Debugging In Pernosco
author: Robert O'Callahan
url: https://robert.ocallahan.org/2019/11/omniscient-printf-debugging-in-pernosco.html
date: 2019-11
accessed: 2026-04-09
ingested: 2026-04-09
---

# Omniscient Printf Debugging In Pernosco

**Source:** [Eyes Above The Waves](https://robert.ocallahan.org/2019/11/omniscient-printf-debugging-in-pernosco.html)
**Topic:** Querying a recorded execution instead of repeatedly rerunning it.

## Core idea
Pernosco treats execution history as something that can be searched and queried after the fact rather than merely stepped through linearly.

## Key claims
- A recorded execution can answer questions that normally require adding print statements and rerunning.
- The interesting interaction is query-based and retrospective, not just forward stepping.
- The debugger becomes closer to an analysis database over execution history.

## Harness takeaway
Validation traces in a harness should be queryable artifacts. Operators should be able to ask when something first failed, where a value changed, or which branch introduced a regression without rebuilding the whole world every time.
