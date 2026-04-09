---
title: Branching Pomsets for Choreographies
author: Luc Edixhoven, Sung-Shik Jongmans, José Proença, Guillermina Cledou
url: https://arxiv.org/abs/2208.04632v1
date: 2022-08-09
ingested: 2026-04-08
---

# Branching Pomsets for Choreographies

**Source:** [arXiv](https://arxiv.org/abs/2208.04632v1)
**Authors:** Luc Edixhoven, Sung-Shik Jongmans, José Proença, Guillermina Cledou
**Date:** 2022-08-09
**Primary category:** cs.PL
**All categories:** cs.PL, cs.LO

## Abstract
Choreographic languages describe possible sequences of interactions among a set of agents. Typical models are based on languages or automata over sending and receiving actions. Pomsets provide a more compact alternative by using a partial order over these actions and by not making explicit the possible interleaving of concurrent actions. However, pomsets offer no compact representation of choices. For example, if an agent Alice can send one of two possible messages to Bob three times, one would need a set of 2 * 2 * 2 distinct pomsets to represent all possible branches of Alice's behaviour. This paper proposes an extension of pomsets, named branching pomsets, with a branching structure that can represent Alice's behaviour using 2 + 2 + 2 ordered actions. We encode choreographies as branching pomsets and show that the pomset semantics of the encoded choreographies are bisimilar to their operational semantics.
