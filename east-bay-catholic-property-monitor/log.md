# East Bay Catholic Property Monitor Log

<!-- oakland-visuals:start -->
## Visuals

<iframe title="Interactive Oakland Catholic price-bubble map" src="east-bay-catholic-property-monitor/assets/maps/oakland-catholic-price-bubble-map.htm" loading="lazy" width="100%" height="680" style="border:1px solid #cbd5e1;border-radius:18px;max-width:100%;background:#e2e8f0;"></iframe>

![Oakland Catholic church price-bubble map](east-bay-catholic-property-monitor/assets/visuals/oakland-catholic-price-bubble-map.png)

![Oakland Catholic project visual index](east-bay-catholic-property-monitor/assets/visuals/oakland-catholic-project-visual-index.svg)

![Oakland Catholic core-site price rank](east-bay-catholic-property-monitor/assets/visuals/oakland-catholic-site-price-rank.svg)

<!-- oakland-visuals:end -->














> Chronological record of actions in this focused sub-vault. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`.

## [2026-05-13] create | monitor initialized
- Created focused LLM Wiki sub-vault for East Bay Catholic church/site property-sale monitoring.
- Created [[diocese-of-oakland]], [[property-sale-signals]], and [[east-bay-catholic-property-sales-monitor]].
- Captured baseline raw source note [[raw/articles/baseline-oakland-diocese-closures-2026-05-13|baseline-oakland-diocese-closures-2026-05-13]].
- Baseline status: 13 sites announced for closure; sale/disposition explicitly contemplated, with St. Paschal Baylon reported by Oaklandside/BishopAccountability as facing sale; no public asking prices identified yet.


## [2026-05-13] update | all Oakland Catholic church dossiers and price screens
- Expanded the watch to all identified Catholic Diocese of Oakland parish/church/pastoral-center sites in Oakland, using the official parish directory, MAP closure list, and Oakland Parcels API.
- Created 19 Oakland site dossiers under [[entities|entities/]], plus [[valuation-methodology]] and [[oakland-catholic-church-price-screen-2026-05-13]].
- Captured raw methodology and parcel records in [[raw/articles/oakland-catholic-church-dossier-expansion-2026-05-13|oakland-catholic-church-dossier-expansion-2026-05-13]].
- Updated [[east-bay-catholic-property-sales-monitor]], [[SCHEMA|SCHEMA.md]], and [[index|index.md]]; content-page count moved 3 → 24.
- Price posture: all dollar ranges are `agent estimate` screens, not asking prices. No public listing, confirmed buyer, or sale price found in this expansion pass; [[saint-paschal-baylon-oakland]] remains the strongest sale-probability watch item.

## [2026-05-13] ingest | nightly red court-docket sale/collateralization signal
- Alert level: Red — Verita docket #2867 Plan Supplement, Exhibit G names Oakland closure sites as potential whole-parish-site disposition/collateralization candidates; no public asking price, sale price, broker listing, buyer, or sale approval found.
- Verdict: the story moved from closure/speculation into primary court-docket site identification; sale versus collateralization remains unresolved.
- Created [[raw/articles/nightly-east-bay-catholic-property-monitor-2026-05-13|raw/articles/nightly-east-bay-catholic-property-monitor-2026-05-13.md]].
- Updated [[east-bay-catholic-property-sales-monitor|queries/east-bay-catholic-property-sales-monitor.md]], [[diocese-of-oakland|entities/diocese-of-oakland.md]], [[property-sale-signals|concepts/property-sale-signals.md]], [[oakland-catholic-church-price-screen-2026-05-13|comparisons/oakland-catholic-church-price-screen-2026-05-13.md]], and [[SCHEMA|SCHEMA.md]].
- Updated Oakland dossiers: [[cathedral-parish-of-christ-the-light]], [[mary-help-of-christians-oakland]], [[our-lady-of-lourdes-oakland]], [[sacred-heart-oakland]], [[saint-andrew-kim-korean-pastoral-center-oakland]], [[saint-augustine-oakland]], [[saint-leo-the-great-oakland]], [[saint-paschal-baylon-oakland]], and [[saint-patrick-oakland]].


## [2026-05-13] alert | nightly red docket signal
- Captured raw nightly source note [[raw/articles/nightly-east-bay-catholic-property-monitor-2026-05-13|nightly-east-bay-catholic-property-monitor-2026-05-13]].
- Alert level: Red. Verita docket #2867 / Exhibit G is recorded as a primary court-docket signal for potential disposition/collateralization of named Oakland closure sites.
- Updated [[east-bay-catholic-property-sales-monitor]], [[diocese-of-oakland]], [[oakland-catholic-church-price-screen-2026-05-13]], and the affected Oakland dossiers.
- Price posture remains disciplined: no public asking price, confirmed buyer, broker listing, or sale price; affected ranges remain `agent estimate` screens.

## [2026-05-14] update | visual coverage and price-bubble map
- Added generated visual blocks to every Markdown page in the Oakland church sub-vault: dossier cards for site pages, shared price-bubble map, rank chart, method diagrams, schema diagram, and raw-note visual wrappers.
- Added [[oakland-catholic-church-price-screen-2026-05-13]] map/rank visuals with bubbles scaled by midpoint of the current core `agent estimate`; no visual is an asking price, appraisal, or sale confirmation.
- Generated durable local SVG assets under the sub-vault asset tree and cached OpenStreetMap/Nominatim coordinates for the 19 Oakland site dossiers.
## [2026-05-14] update | section landing pages with visuals
- Added visual section landing pages for [[entities/index|entities]], [[concepts/index|concepts]], [[comparisons/index|comparisons]], [[queries/index|queries]], [[raw/index|raw evidence]], and [[raw/articles/index|raw articles]] so folder routes are no longer blank auto-indexes.
- Updated [[index|index.md]] to distinguish 24 curated content pages from 36 authored Markdown pages.

## [2026-05-14] update | real basemap price-bubble map
- Replaced the schematic Oakland price map with a real OpenStreetMap/CARTO tile-backed PNG and an embedded Leaflet interactive map on every Oakland project page.
- The map still uses the current dossier `agent estimate` midpoint for bubble area; it remains a navigational screen, not an appraisal or asking-price claim.
