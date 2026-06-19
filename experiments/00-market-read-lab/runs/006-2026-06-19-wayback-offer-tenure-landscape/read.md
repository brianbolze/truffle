# Market Read

## Question

In the captured telehealth cohort, which offer pages are long-lived vs newly stood up per the
Wayback tenure signal, and what does that captured tenure signal actually measure — and where
does it mislead (offer-page tenure vs company age)?

## Direct Answer

**The headline is a warning, not a ranking: the captured Wayback `tenure_days` field is the most
confidently-wrong number in this signal.** Read naively, it says brands like noom (27y), rexmd
(25y), bluechew (24y), telolife, ivyrx, remedymeds (22y each) are decades-old incumbents. They are
not — those are *domain* ages, and several of the domains were dormant or owned by someone else
for most of that span before the current brand stood up on them. **What the signal honestly
measures is "how long a URL has existed in the Wayback archive," which is brand age only when the
domain was continuously the same business.**

Within that caveat, the captured slice splits three ways `[Judgment, built on S1/S2]`:

1. **Credibly established** — old `first_seen` *and* dense continuous archival: **noom, nurx,
   onemedical, ro.co, defymedical, bluechew, lifemd**. Domain age here is plausible brand age
   (the *current GLP-1/ED offer* may still be a recent pivot — domain-old ≠ offer-old).
2. **Revival/reuse candidates** — old `first_seen` but sparse pre-2020 archival, dense only from
   2024+: **telolife, remedymeds, ivyrx, goodlifemeds, effecty, directmeds, getopt, rugiet,
   tryshed, mylifeforce, vitalityrx, trtnation, functionhealth, mydrhank, invigormedical**. The
   22–20-year `tenure_days` here is essentially noise for "how established is this brand."
3. **Genuinely new builds** — recent `first_seen` on freshly-stood-up pages: **home-medvi (0.3y),
   brellohealth (1.8y), niagenplus (2.2y), joiandblokes (2.2y)** at the domain level, and the
   offer-page captures (honehealth mens-sermorelin 38d, struthealth blog 199d, joinamble 314d)
   which are the *truest* brand-era markers because the URL only exists once the brand built it.

So: **the sparse offer-page captures (the minority) are more honest about brand/offer recency than
the clean-looking root `tenure_days` (the majority).** That inverts the naive read.

## Evidence Used

All from captured store signals + frontmatter — no external fetch, no snippets. Audit trail and
the full per-domain reuse diagnostic live in
[`receipts/wayback-tenure-panel.md`](receipts/wayback-tenure-panel.md).

- **C1** — 47 domains / 55 distinct captures carry a Wayback signal; 49 scorable. First read to
  consume the Wayback layer.
- **C2** — 39 captures are homepages (`root`), 16 are specific offer/blog pages.
- **C3** — root tenure spans 0.3y (home-medvi-org) → 27.4y (noom-com); the oldest-dated roots are
  GLP-1 / ED / hormone DTC brands.
- **C4** — root `first_seen` overstates brand age for revival-candidate domains (sparse pre-2020 /
  dense 2024+ snapshots) — *derived heuristic, not proof of an ownership change*.
- **C5** — GLP-1-anchored roots dated 2004–2013 and online-ED roots dated 2001 pre-date their own
  product category (GLP-1 weight-loss telehealth ~2021+, online ED ~2017+), so the `first_seen`
  cannot be the current brand's operating age — *internal-consistency argument, no external claim*.
- **C6** — offer/blog-page tenure (the truer brand-era marker) is captured for only ~10 brands.

## Companies Seen

**Signal (captured `first_seen` / `tenure_days`, root unless noted):** State below is the captured
archive fact; the "age-credible?" column is Judgment from the C4/C5 diagnostic.

| Brand | first_seen | tenure | anchor_category | Age-credible? |
|---|---|---|---|---|
| noom-com | 1999-01 | 27.4y | GLP-1 | yes (dense archival; GLP-1 is a recent pivot) |
| lifemd-com | 2000-05 | 26.1y | multi | yes |
| mylifeforce-com | 2000-10 | 25.7y | longevity/NAD | **no — revival candidate** |
| rexmd-com | 2001-07 | 24.9y | sexual-health | **no — ED category post-dates 2001** |
| bluechew-com | 2001-12 | 24.5y | sexual-health | **no — ED category post-dates 2001** |
| nurx-com | 2002-05 | 24.1y | multi | partial (dense, but pre-2020 ≠ current brand) |
| telolife / ivyrx / remedymeds | 2004 | 22y | GLP-1 | **no — revival + category anachronism** |
| getopt / vitalityrx / malemd | 2003–04 | 22–23y | TRT/multi | **no — revival candidates** |
| goodlifemeds / effecty | 2006 | 19.8y | GLP-1 | **no — revival + anachronism** |
| directmeds | 2008 | 18.1y | GLP-1 | **no — revival + anachronism** |
| onemedical-com | 2009-07 | 16.9y | primary-care | yes (dense, continuous) |
| defymedical-com | 2012-01 | 14.4y | TRT | yes (dense, continuous) |
| ro-co | 2013-06 | 13.0y | GLP-1 | yes domain; GLP-1 offer is recent |
| trtnation-com | 2017-05 | 9.1y | TRT | domain old-ish, archival starts ~2024 |
| henrymeds / ivimhealth / joinfridays | 2022–23 | 3–4y | GLP-1 | yes — plausible brand age |
| brellohealth / niagenplus / joiandblokes | 2024 | 1.8–2.2y | GLP-1/NAD/multi | yes — new builds |
| home-medvi-org | 2026-03 | 0.3y | GLP-1 | yes — newest captured |

**Offer/blog-page captures (truer offer-era markers):** hims hard-mint ED (992d), hydramed
semorelin (918d), honehealth longevity-nad (631d), maximustribe enclomiphene-only (560d), joinamble
sermorelin (314d), agelessrx sermorelin (299d), struthealth sermorelin blog (199d), honehealth
mens-enclomiphene (191d), maximustribe enclomiphene-tadalafil-cream (148d), honehealth mens-sermorelin
(38d, `provisional`). Six offer-page captures are `insufficient` (no `first_seen`) — hims
enclomiphene pages, honehealth peptides-waitlist, eden + sermorelin.com articles.

## Missing / Stale Coverage

- 46 of 54 captured telehealth brands have a Wayback signal; 8 telehealth packs have none. The
  broader store (135 profiles) is far less covered.
- Mostly one capture-URL per domain. Where it's an offer page (honehealth, maximustribe, hims),
  there is **no root/homepage** tenure for that brand — so brand-vs-offer tenure can't be compared
  within the same brand for most of the cohort.
- `snapshots_truncated: true` on ivyrx, noom, onemedical → their snapshot counts are floors.

## Source Gaps

- The captured signal exposes `tenure_days` as a top-level field but **not** the discriminator
  that makes it trustworthy (snapshot density over time / `status_trail` gaps). Both live in the
  same JSON, but a consumer reading only `tenure_days` gets the trap with no warning attached.
- No registration/WHOIS or "brand launch" evidence is captured, so true brand age can't be
  confirmed store-only — only the *unreliability* of `first_seen` can be flagged.

## External Completeness Check

Not run — store-only contract, and completeness is **not** load-bearing here: the read's value is
the methodological caveat on the captured signal, not a census of who's oldest. An external
denominator (full Wayback CDX over all 54 telehealth domains) would extend coverage but not change
the confound, which is the finding.

## Market Pattern

- **Domain age is a poor proxy for brand age in this market specifically**, because GLP-1 and
  online-ED telehealth are recent categories layered onto older or recycled domains. The brands
  that *look* oldest (20+ years) are disproportionately the ones where the domain was reused —
  an aged domain is plausibly an acquisition/SEO asset, not evidence of incumbency.
- **The genuinely old, continuously-archived players** (noom, onemedical, nurx, ro.co, defymedical,
  lifemd, bluechew) are a small set — and even they are mostly old *platforms* that pivoted into
  GLP-1/hormones recently, so their domain age overstates their tenure *in the current category*.
- **The honest recency signal is the offer page.** A `/sermorelin/` or `/testosterone/enclomiphene-only`
  URL dates the brand's *entry into that offer*, and those cluster in the last 1–3 years —
  consistent with the GLP-1/peptide/enclomiphene land-grab being a recent wave.

## What Would Change This Answer

- Capturing root + key offer pages for the *same* brands would let brand-vs-offer tenure be
  compared head-to-head instead of inferred across brands.
- A captured registration/launch signal (or surfacing snapshot-density / status-trail gaps as a
  derived field) would convert the "revival candidate" heuristic into a confirmable flag.
- Broader Wayback coverage across all 54 telehealth domains would firm up the cohort distribution,
  though not the central confound.
