---
title: Vibe Maintainer
author: Steve Yegge
url: https://steve-yegge.medium.com/vibe-maintainer-a2273a841040
date: 2026-03-31
ingested: 2026-04-07
---

# Vibe Maintainer: Managing the AI PR Storm

## Scale
- ~50 contributor PRs per day across Beads (20k stars) and Gas Town (13k stars)
- 1,000+ unique contributors; 4,000+ total PRs
- Median time to resolution: 15 hours
- ~88% merge rate
- 15-20 hours/week human oversight

## PR Sheriff Decision Tree
- Easy Wins: Bug fixes, docs, dependency updates — automatic every 2 hours
- Merge-fix: Merge as-is, push follow-up fix to main
- Fix-merge: Pull locally, fix, push with contributor attribution
- Cherry-pick: Take only useful parts of multi-part PR
- Split-merge: Separate large PR into distinct concerns
- Redesign: Reject code but implement idea better
- Reject/Retire: Niche features, high tech debt, obsolete PRs

"Requesting changes is the last resort because it quickly leads to contributor starvation."

## PR Hygiene Rules
- Cross-project pollution: Keep project boundaries strict
- Zero Framework Cognition (ZFC): Build resilient apps without heavy framework dependencies
- Use Plugins: Keep core minimal
- One concern per PR
- Always rebase before submission

## Future
- Dark Factories: Coding agents as SREs and production workers
- SaaS-Eater: AI-driven de-SaaS-ing
- Gas City: Dark Factory Factory replacing binary with declarative "packs"
