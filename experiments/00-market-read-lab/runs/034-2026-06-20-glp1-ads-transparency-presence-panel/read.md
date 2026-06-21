# Market Read

## Question

For a bounded panel of up to 6 captured GLP-1 telehealth brands, what does the Google Ads
Transparency Center show about active paid-acquisition motion (running-now vs ran-only,
advertising tenure, creative format), and is ads-presence a cheap, real Signal the store's
current toolkit can't see — or too push-biased to trust as traction?

## Result

**A gap-probe with a clean dual finding: the ads source family is cheap and works, but it
is a *push/resourcing* Signal the store does not capture today, and it must not be read as
demand.**

Panel of 6 GLP-1 DTC brands (1 SerpAPI call each, 6 credits, US region, captured
2026-06-21), domain-keyed:

| Brand (domain) | Verdict | Tenure (first→last shown) | First-page creatives | Formats |
|---|---|---|---|---|
| hims.com | **Active** | 2022-06-29 → 2026-06-20 | 14 | image, text |
| ro.co | **Active** | 2023-02-16 → 2026-06-20 | 40 (page cap) | image, text, **video** |
| henrymeds.com | Ran, now quiet (~209d) | 2024-01-02 → 2025-11-24 | 2 | image, text |
| lifemd.com | Ran, now quiet (~309d) | 2022-07-14 → 2025-08-16 | 1 | text |
| remedymeds.com | **Zero on this surface** | — | 0 | — |
| eden.health | **Zero on this surface** | — | 0 | — |

Three readable states emerge cleanly: **actively visible** (2/6), **ran-but-quiet on
Google** (2/6), and **zero on this exact surface** (2/6). The signal is real and
discriminating — recency, advertising tenure, and format-richness all separate the panel —
and each call costs one SerpAPI credit.

**But the read stops at "push/resourcing motion," by design.** Running Google ads proves
budget and an active acquisition motion; it says nothing about conversion, demand, or
whether the brand is winning. The four traps the contract named were all live and avoided
(see Gap Map). The honest one-line answer: *ads-transparency is a cheap, real
acquisition-push Signal the store cannot see today (1/130 captured; 0 GLP-1) — worth adding
to the capture toolkit as a push-side traction ingredient, never as a demand/quality read.*

## Gap Map

**Where Truffle answered cleanly (via the new tool, not the store):**
- The tool itself is reliable and bounded: 6/6 domains returned a clean result (4 with
  creatives, 2 clean zeros), 1 credit each, domain-keyed so no name collisions.
- Three decision-useful axes are extractable per brand: **recency** (active vs quiet),
  **advertising tenure** (first_shown), and **format mix** (text/image/video).

**Where the store fell short (the structural gap):**
- **The store cannot see any of this today.** Only **1/130** profiles carry a
  `signals/ads_transparency` dir (`waldo-fyi`); **0** GLP-1 brands. The tool exists and the
  `ads_transparency` source_type resolves, but the surface is essentially **uncaptured** —
  the same "machinery ahead of coverage" shape run-029 found for traction broadly. This is
  a **coverage** gap, not an architecture gap.

**The four false-confidence traps (contracted `loop1_failure_mode`), all live, all avoided:**
1. **push ≠ demand.** A naive ranking ro > hims > henrymeds > lifemd > remedymeds=eden as
   "who's doing best" is *wrong*; it ranks visible Google spend, not market success.
2. **first-page ≠ volume.** ro.co's `n_creatives_first_page: 40` is the page cap, not "ro
   runs 40 ads." Only presence/recency/tenure/format are safe to report.
3. **legal-name ≠ brand.** ro→"Roman Health Ventures Inc.", henrymeds→"ADONIS HEALTH INC.",
   lifemd→"LifeMD, Inc." A name-keyed search would mis-attribute; domain-keying fixed it.
4. **zero ≠ not advertising.** remedymeds/eden clean-zero = *not visible on Google
   Transparency for that target_domain*, not "not advertising" — they may run Meta ads or
   land on a different domain (`eden.health` is itself an uncertain ad-landing key).

**What would change the answer:** a Meta/Apify social-ads route (deferred) would catch the
two zeros if they advertise off-Google; a second-region or repeat capture would add a
time-delta (today's read is single-point, single-region).

## Evidence Used

All claims rest on primary SerpAPI captures saved under `receipts/ads/*.json` and
summarized in `receipts/ads-transparency-panel-2026-06-20.md`. Capture date 2026-06-21,
region US, one call per domain. Claim IDs C1–C7 map in the receipt's Claim Map. This is a
`bounded-live` run; every outside source is logged in `run-notes.md` `live_evidence_used`.

- C1 — readable result for all 6 (incl. clean zeros): S1–S6.
- C3 — 2/6 active, 2/6 ran-quiet, 2/6 zero: S1,S2,S3,S6 + S4,S5.
- C5 — store sees 1/130 ads signals, 0 GLP-1: S7 (`ls -d store/*/signals/ads_transparency`).

## Companies Seen

Panel (6): hims.com, ro.co, henrymeds.com, remedymeds.com, eden.health, lifemd.com.
Drawn from the GLP-1-anchored cohort (25 by loose `anchor_category` grep; ~19 strict per
run-029). The other ~19 cohort brands were **not sampled** — this is a panel, not a census.

## Missing / Stale Coverage

- **Ads source family: 1/130 captured store-wide** (waldo-fyi), 0 GLP-1. The dominant gap.
- The panel's "zeros" (remedymeds, eden) may be coverage artifacts of domain-keying /
  channel choice, not true ad-absence — flagged, not resolved.
- No time-delta: ads captures are single-point; `signal_delta.py` has no ads branch (mirrors
  the run-029/MRL-012 sec_edgar-no-delta gap).

## Source Gaps

- **Meta/Instagram ads** (Apify route, deferred) — the obvious second source family; the
  only way to disambiguate the two Google-zeros from genuine non-advertisers.
- **Ad-landing-domain resolution** — a brand's ads may target a domain ≠ its store `domain:`
  key (campaign LPs, `try<brand>.com`), which the current domain-keyed search misses.

## Raw Learning to Preserve

See `run-notes.md` Discovery ledger IDs O1–O5, S1, G1, W1, F1 for Loop 2 to append to
`discovery-ledger.md`.

## External Completeness Check

Not run — completeness of the *cohort* is not load-bearing here (the run is a
source-family probe on a deliberately bounded 6-brand panel, reported as a sample). The
store cohort (25 loose / 19 strict) is the denominator the panel is drawn from; no outside
denominator was needed.

## Market Pattern

1. **A push-spend tier is visible and real in GLP-1.** The two most-recognized brands
   (hims, ro) are continuously, currently advertising on Google with multi-format creative
   (ro adds video) and 2–3-year tenure — a sustained, well-resourced acquisition motion.
   Mid-tier brands (henrymeds, lifemd) have *run* Google ads but are currently quiet on the
   surface; two (remedymeds, eden) are invisible on it.
2. **Tenure ≠ current activity.** lifemd has the 2nd-longest tenure (since 2022) yet has
   been quiet on Google ~10 months — long-tenured advertisers can go dormant; recency and
   tenure are independent axes and both matter.
3. **The signal's whole value is presence/recency/tenure/format — and its whole danger is
   being read as demand.** This is the cleanest single illustration yet of the traction
   frame's push-vs-demand split (run-029): a cheap external Signal that is genuinely
   informative about *resourcing* and genuinely silent about *outcomes*.

## What Would Change This Answer

- A **Meta/Apify** capture catching the two Google-zeros advertising elsewhere → reframes
  "zero" from "quiet" to "off-Google channel."
- **Ad-landing-domain resolution** finding eden/remedymeds ads on a campaign domain →
  flips a zero to active.
- **No new primitive is needed** to *consume* this — `ads_transparency.py` already emits a
  clean envelope and `scripts/signals.py` already resolves the `ads_transparency`
  source_type. What's missing is **capture coverage** (a campaign to run the tool across a
  cohort) and a **`signal_delta.py` ads branch** for time-deltas — both spend/approval-gated,
  not autonomous-safe, and consistent with run-029's "coverage + comparator, not a new
  primitive" verdict.
