---
title: Oakland Church Valuation Methodology
created: 2026-05-13
updated: 2026-05-13
type: concept
tags: [valuation, real-estate, candidate-site]
sources: [raw/articles/oakland-catholic-church-dossier-expansion-2026-05-13.md]
---

# Oakland Church Valuation Methodology

## Purpose

This page defines the screening estimate used across the Oakland Catholic church dossiers in [[east-bay-catholic-property-sales-monitor]]. It is not an appraisal. It is a repeatable triage method for watching whether a site might be cheap, expensive, or strategically material if the [[diocese-of-oakland]] starts selling property.

## Observed values retained

For every dossier, preserve the Oakland Parcels API fields when available:

- `SHP_LANDVALUE`
- `SHP_IMPRVMTS_VALUE`
- `ASSESSED_VALUE`
- `PC_LOT_SIZE`
- `PC_BLDG_AREA`
- APN, owner, use code, and situs address

Because many religious properties are exempt or carry legacy assessment treatment, `ASSESSED_VALUE` may be zero or misleading. The dossiers therefore also retain `SHP_LANDVALUE + SHP_IMPRVMTS_VALUE` as a parcel-API component total, but do not treat it as an asking price.

## Agent estimate

The current `agent estimate` is land-centric:

1. For each ZIP code represented in the Oakland Catholic parcel set, sample non-Catholic/non-government Oakland parcels from the same Oakland Parcels API.
2. Compute median `SHP_LANDVALUE / PC_LOT_SIZE` for parcels with usable lot sizes and nonzero land value.
3. Multiply the church/site parcel lot area by the weighted ZIP median land value per square foot.
4. Report a broad screening range: low 55%, mid 85%, high 125% of the land screen.

This deliberately estimates redevelopment/acquisition land pressure, not sacred-use value, insurance replacement cost, or final negotiated sale price. It is useful because buyers of closed church sites often price the dirt, entitlements, constraints, and optionality; the stained glass rarely fits in a spreadsheet, though it does try.

## Confidence and caveats

- Confidence is low until a broker listing, court motion, appraisal, or comparable sale appears.
- Dedicated worship buildings, schools, cemeteries, steep parcels, historic resources, SB4/YIGBY eligibility, parking, and neighborhood politics can move value sharply.
- Candidate pages separate core parcels from adjacent campus parcels because a sale package may not include the whole Catholic-owned envelope.
- Any red-signal alert must still privilege observed price labels: `asking price`, `sale price`, `court value`, `assessed value`, or `broker estimate` over this `agent estimate`.

See [[property-sale-signals]] for alert thresholds.
