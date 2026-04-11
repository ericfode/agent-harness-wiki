---
title: Access control on the Web using proof-carrying authorization
author: L. Bauer, M.A. Schneider, E.W. Felten, A.W. Appel
url: https://doi.org/10.1109/discex.2003.1194942
date: 2004
ingested: 2026-04-10
---

# Access control on the Web using proof-carrying authorization

**Source:** [DOI](https://doi.org/10.1109/discex.2003.1194942)
**Authors:** L. Bauer, M.A. Schneider, E.W. Felten, A.W. Appel
**Date:** 2004

## Core idea
A requester can carry machine-checkable proof that an action satisfies the receiver's local policy, allowing authorization decisions to rest on evidence rather than on opaque trust.

## Key claims
- Authorization can be transmitted as a proof object attached to a request.
- The verifier remains sovereign because it checks the proof against its own policy.
- Credentials become useful when they compose into explicit evidence of permission.

## Harness takeaway
Sensitive cross-node actions in a harness should prefer evidence-carrying requests: "here is why I may do this" is better than "trust me, my reputation says I'm fine."
