---
title: St. Louis Bertrand Parish, Oakland
created: 2026-05-13
updated: 2026-05-13
type: entity
tags: [diocese-oakland, real-estate, valuation]
sources: [raw/articles/baseline-oakland-diocese-closures-2026-05-13.md, raw/articles/oakland-catholic-church-dossier-expansion-2026-05-13.md]
---

# St. Louis Bertrand Parish, Oakland

## Status

- Address/source address: 1410 100th Avenue, Oakland
- Current status: active / not on 2026 closure list
- Closure list: No — not on the 2026-04-28 MAP closure list identified in the baseline pass.
- Sale probability screen: `low`
- Watch priority: baseline dossier
- Sale signal: No direct sale/listing signal yet.
- Notes: Official directory gives 1410 100th Avenue, but parcel API appears to store the Catholic parcel envelope on International Blvd / 101st Ave. Needs assessor-map verification before transactional use.

## Price and parcel screen

These are not asking prices. They are dossier-maintenance estimates until a listing, appraisal, court value, or sale price appears. See [[valuation-methodology]].

- Cost label: `agent estimate` (low-confidence land-centric screen).
- Core parcel lot area: 108,829 sq ft
- Core parcel API component total (`SHP_LANDVALUE + SHP_IMPRVMTS_VALUE`): $3.8M
- Core parcel API assessed-value total: $0
- Same-ZIP sampled median land value: $17.33/sq ft (weighted across core parcels; sample n≈16778).
- Core acquisition/redevelopment screen: $1M–$2.4M (mid $1.6M).
- Expanded adjacent-campus envelope screen: $1.1M–$2.5M (mid $1.7M).
- Adjacent-envelope warning: adjacent parcels may be school, parking, rectory, or unrelated Catholic institutional property; do not assume they are part of a sale package until a docket/listing says so.

## Core parcels

- APN `47-5515-8-2` — 10002 INTERNATIONAL BLVD OAKLAND 94603; owner: ROMAN CATHOLIC BISHOP OF OAKLAND; lot: 31,729 sq ft; building area: unknown; use: `6600`; component total: $2M; assessed: $0.
- APN `47-5515-6-5` — 10020 INTERNATIONAL BLVD OAKLAND 94603; owner: ROMAN CATHOLIC WELFARE CORPORATION OF OAKLAND; lot: 77,100 sq ft; building area: unknown; use: `6400`; component total: $1.8M; assessed: $0.

## Adjacent / campus parcels to verify

- APN `47-5516-18-1` — 1432 101ST AVE OAKLAND 94603; owner: ROMAN CATHOLIC WELFARE CORPORATION OF OAKLAND; lot: 8,466 sq ft; use: `6400`; component total: $241,500.

## Monitoring checklist

- Search exact church name + `for sale`, `listing`, `sold`, `buyer`, `broker`, `bid procedures`, `permit`, and `redevelopment`.
- Check Diocese MAP / Chapter 11 pages and KCC/Verita docket for named site sale motions.
- If price appears, replace the `agent estimate` lead with observed `asking price`, `court value`, `broker estimate`, or `sale price`.

## Links

- [[east-bay-catholic-property-sales-monitor]]
- [[diocese-of-oakland]]
- [[property-sale-signals]]
- [[valuation-methodology]]
