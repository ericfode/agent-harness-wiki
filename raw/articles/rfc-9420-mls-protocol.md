---
title: The Messaging Layer Security (MLS) Protocol
author: Richard Barnes, Benjamin Beurdouche, Raphael Robert, Jon Millican, Emad Omara, Katriel Cohn-Gordon
url: https://www.rfc-editor.org/rfc/rfc9420.html
date: 2023-07
ingested: 2026-04-09
---

# The Messaging Layer Security (MLS) Protocol

**Source:** [RFC 9420](https://www.rfc-editor.org/rfc/rfc9420.html)
**Authors:** Richard Barnes, Benjamin Beurdouche, Raphael Robert, Jon Millican, Emad Omara, Katriel Cohn-Gordon
**Date:** 2023-07

## Core idea
MLS provides efficient asynchronous group key establishment with explicit group epochs, forward secrecy, and post-compromise security for large groups.

## Harness takeaway
A distributed actor or coalition in the studio should treat embodiment changes, membership updates, and role reassignment as explicit epoch transitions that roll security and context material forward safely.
