---
title: The Escrow Transactional Method
author: Patrick E. O’Neil
url: https://www.cs.umb.edu/~poneil/EscrowTM.pdf
date: 1986
ingested: 2026-04-09
---

# The Escrow Transactional Method

**Source:** [PDF](https://www.cs.umb.edu/~poneil/EscrowTM.pdf)
**Author:** Patrick E. O’Neil
**Date:** 1986

## Abstract / key passage
The paper presents a method for permitting record updates by long-lived transactions without forbidding simultaneous access by other users. It is designed for long-lived work where intermediate recoverability matters and where aggregate quantities or bounded rights can be allocated without turning hot spots into bottlenecks. The paper explicitly notes advantages for distributed transactions, delayed messages, occasional disconnection, and even human interaction in the middle of a transaction.

## Harness takeaway
Escrow is a beautiful fit for delegated autonomy. Budgeted rights — token spend, deployment slots, edit scope, API quota, or approval capacity — can be pre-allocated to agents so they operate safely without serializing every action through one coordinator.
