---
title: Session Guarantees for Weakly Consistent Replicated Data
author: Douglas B. Terry, Alan J. Demers, Karin Petersen, Mike Spreitzer, Marvin Theimer, Brent Welch
url: https://www.cs.utexas.edu/~lorenzo/corsi/cs380d/papers/SessionGuaranteesBayou.pdf
date: 1994
ingested: 2026-04-09
---

# Session Guarantees for Weakly Consistent Replicated Data

**Source:** [PDF](https://www.cs.utexas.edu/~lorenzo/corsi/cs380d/papers/SessionGuaranteesBayou.pdf)
**Authors:** Douglas B. Terry, Alan J. Demers, Karin Petersen, Mike Spreitzer, Marvin Theimer, Brent Welch
**Date:** 1994

## Abstract / key passage
The paper proposes four per-session guarantees for weakly consistent replicated data: Read Your Writes, Monotonic Reads, Writes Follow Reads, and Monotonic Writes. The goal is to give each application a view of the database that is consistent with its own actions even when it reads and writes from potentially inconsistent replicas. The guarantees were developed in the Bayou project and are explicitly motivated by mobile and intermittently connected use.

## Harness takeaway
This is an excellent template for multi-surface harness consistency. After a human or agent acts, later views across CLI, dashboard, and background workers should at least preserve session-level monotonicity even if the whole system is not globally strong.
