---
title: Merkle-CRDTs: Merkle-DAGs meet CRDTs
author: Hector Sanjuan, Samuli Poyhtari, Pedro Teixeira, Ioannis Psaras
url: https://arxiv.org/abs/2004.00107
date: 2020-03-31
ingested: 2026-04-10
---

# Merkle-CRDTs: Merkle-DAGs meet CRDTs

**Source:** [arXiv](https://arxiv.org/abs/2004.00107)
**Authors:** Hector Sanjuan, Samuli Poyhtari, Pedro Teixeira, Ioannis Psaras
**Date:** 2020-03-31

## Abstract / key passage
Merkle-CRDTs combine CRDT convergence with Merkle-DAG structure so replicas can exchange authenticated state efficiently in open networks. The design makes anti-entropy incremental, content-addressed, and hash-verifiable rather than requiring naive whole-state synchronization.

## Harness takeaway
A peer-to-peer harness network should not sync giant opaque session blobs. It should sync signed operations and content-addressed artifact graphs so peers can reconcile only the missing pieces and verify what they received.
