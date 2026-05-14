---
title: East Bay Catholic Property Monitor Schema
created: 2026-05-13
updated: 2026-05-14
type: schema
tags: [meta, schema]
---

# East Bay Catholic Property Monitor Schema

<!-- oakland-visuals:start -->
## Visuals

<iframe title="Interactive Oakland Catholic price-bubble map" src="east-bay-catholic-property-monitor/assets/maps/oakland-catholic-price-bubble-map.htm" loading="lazy" width="100%" height="680" style="border:1px solid #cbd5e1;border-radius:18px;max-width:100%;background:#e2e8f0;"></iframe>

![Sub-vault structure diagram](east-bay-catholic-property-monitor/assets/visuals/schema-content-map.svg)

![Oakland Catholic project visual index](east-bay-catholic-property-monitor/assets/visuals/oakland-catholic-project-visual-index.svg)

![Oakland Catholic church price-bubble map](east-bay-catholic-property-monitor/assets/visuals/oakland-catholic-price-bubble-map.png)

<!-- oakland-visuals:end -->














## Domain

Nightly monitoring of the Diocese of Oakland's announced East Bay Catholic church/site closures, likely property disposition, bankruptcy dynamics, candidate sites, sale/listing signals, and estimated or reported acquisition cost.

The watch maintains dossiers for all identified Catholic Diocese of Oakland parish/church/pastoral-center sites in Oakland, not only currently announced closure sites. Outside-Oakland closure sites remain monitor-level items unless they develop concrete sale/listing/price signals or Eric asks for full dossiers.

This is a focused LLM Wiki sub-vault under `~/wiki` so the local real-estate watch does not pollute the main agent-harness wiki schema. Tidy boundaries: the small mercy by which notes do not become soup.

## Conventions

- File names: lowercase, hyphenated, no spaces.
- Raw sources live under `raw/articles/` or `raw/dockets/` and are immutable after capture.
- Curated pages live under `entities/`, `concepts/`, `comparisons/`, and `queries/`.
- Every content page must have YAML frontmatter with `title`, `created`, `updated`, `type`, `tags`, and `sources`.
- Every rendered project page should include at least one non-evidentiary visual block (`<!-- oakland-visuals:start -->`) so the public surface is navigable by eye; raw evidence bodies remain authoritative over visual aids.
- Use Obsidian-style wikilinks for cross-references; every curated page should have at least two outbound links unless there are fewer than two relevant curated pages.
- Update `index.md` and append `log.md` after every run.
- Separate observed facts from estimates, rumors, and inference.
- For cost: label each figure as one of `asking price`, `sale price`, `court value`, `assessed value`, `broker estimate`, `agent estimate`, or `unknown`.
- Never present a property as for sale unless a primary source, court docket, broker listing, or named credible news outlet says so.

## Frontmatter

```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | index | schema | raw-source-note
tags: [from taxonomy below]
sources: [raw/articles/source-name.md]
---
```

## Tag Taxonomy

- `diocese-oakland` — Roman Catholic Bishop / Diocese of Oakland.
- `bankruptcy` — Chapter 11, reorganization plans, court filings, survivor trust funding.
- `parish-closure` — announced closure, merger, receiving parish, final Mass, staff transition.
- `real-estate` — property disposition, sale, listing, broker, parcel, zoning, permits.
- `candidate-site` — specific church/site likely to be watched as a possible sale candidate.
- `valuation` — asking price, sale price, assessed value, comparable sale, estimate.
- `court-docket` — Verita/KCC/PACER bankruptcy documents and orders.
- `city-planning` — planning permits, SB4/YIGBY, zoning, historic review, redevelopment signals.
- `news` — local/regional reporting.
- `alert` — material watch condition requiring user notification.
- `meta` — wiki maintenance.
- `schema` — schema/taxonomy.

## Page Thresholds

- Maintain one dossier page for every identified Catholic Diocese of Oakland parish/church/pastoral-center site in Oakland.
- Create or promote an outside-Oakland candidate-site page when a site has either a confirmed sale/listing signal, a unique valuation trail, or repeated source mentions requiring more than one paragraph.
- Keep single-mention or low-detail outside-Oakland site notes in the monitor query page.
- Split cost/valuation work into a comparison page if multiple sites acquire concrete price data, or when a dated all-Oakland price screen is refreshed.

## Alert Policy

Notify Eric prominently when any of these occurs:

1. A candidate site is publicly listed, marketed, or brokered with an asking price.
2. A bankruptcy docket filing seeks approval to sell a named church/site, hire a broker for it, approve bid procedures, or approve a sale.
3. A credible news source reports a sale, purchase agreement, buyer, developer, or expected price.
4. City or county records show a permit, pre-application, parcel transfer, deed record, or redevelopment filing tied to a candidate site.
5. The monitor can provide a grounded cost range from observed listings, sale comps, or parcel/assessed-value data and the sale probability is at least `likely`.

If none of the above is present, append the nightly update to the wiki and send only a compact "no material movement" note if the cron job is configured to deliver nightly.
