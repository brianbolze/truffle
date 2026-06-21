# Market Read

## Question

Across a multi-anchor set (18 captured telehealth brands + 5 SaaS brands, **Hone Health** the
calibration anchor), who do buyers actually cross-shop per **external demand-side evidence** — Exa
`/findSimilar` neighbors + owned/third-party comparison ("alternatives to X") pages? Which neighbors
recur as cross-shop **hubs**, which are **store-absent**, and does the external set **confirm or
overturn run 017's store-only** Hone substitute/adjacent tiering? Does the recipe generalize to SaaS?

This is a `gap-probe`. The deliverable is the **source-quality map** — does external demand-side
evidence give Truffle a trustworthy cross-shop signal it lacks store-only — not a verdict on any one
company's competitors.

## Result

**Neither external source, as exercised, delivers a clean demand-side cross-shop map — but the two
fail *differently*, and that contrast is the finding.** Run 017's store-only positioning judgment is
**partially corroborated and not overturned**; this *vindicates* MRL-011's "don't build a
`competitors:` field," because the outside sources that would feed such a field are unreliable.

- **Exa `/findSimilar` is a name/semantic-similarity signal, NOT a cross-shop signal.** Calibrated
  against run 017's 16 store-only Hone neighbors, Exa's top-25 for Hone recovered **1 of 16**
  (`hormonemd` only) — it missed **all four Tier-1 substitutes** (mylifeforce, gogeviti, gethealthspan,
  defymedical) a Hone shopper would genuinely cross-shop (C2). What it returned instead was
  name-collisions and mirrors: `hims` → `bit.ly`, `mailchi.mp`, "HMS Holdings Corp" (an unrelated
  healthcare-IT company sharing the letters); `ro.co` → Roon (`roon.com`), `ro.am`, Rvo Health
  (`rvohealth.com`); `notion` → `notion.so` (mirror), Notion Wave (`notionwave.ai`), OneNote (C3).
  Quality is governed by **anchor-name distinctiveness**,
  not market structure — only `posthog` (a distinctive dev-tool name) returned real rivals
  (Plausible, Matomo, Statsig, Clickhouse, Supabase) (C4).
- **Comparison/"alternatives to" pages are better but self-serving-SEO-biased.** For Hone they
  recovered **4 of 16** run-017 neighbors — including **2 of the 4 Tier-1 substitutes** (Lifeforce,
  Defy Medical) plus Maximus and Peter MD (C6) — 4× Exa's recall. But **only 1 of the 5 result pages
  was a neutral third-party listicle**: 3 were owned `/vs` (hims-vs-hone, hone-vs-hims, viking-vs-hone),
  1 a competitor-intel page (cbinsights), 1 an affiliate listicle (policylab) (C7) — the named set is
  biased toward *whoever bothered to write the page*, not neutral demand. Cross-source recurrence is
  the only usable filter.
- **The store-only read (017) holds up as the more trustworthy substrate.** That the comparison
  pages *independently* re-named 4 of 017's supply-side-inferred neighbors (incl. its two closest
  substitutes) means 017's judgment wasn't fabricated — but neither external source is clean enough
  to *overturn* it, and both are too noisy to *populate* a durable competitive primitive. The
  honest answer to "does demand-side evidence confirm or overturn 017?" is **weak partial
  corroboration; no overturn; sources not graduation-grade.**

**Cross-vertical (SaaS):** the recipe *runs* off-telehealth, and the same Exa-vs-comparison contrast
holds — sharpened. For `notion` (common name) Exa returned mirror-junk, but "Notion alternatives"
pages recovered real rivals (**Coda, Obsidian, Craft, Capacities, ClickUp, Asana, Confluence**) (C10).
So comparison pages **rescue the common-name case Exa fails** — in both verticals.

## Gap Map

The gap-probe's main result: a **source-quality map** for demand-side cross-shop evidence.

| Source family | Did it give a trustworthy cross-shop set? | Failure mode | Verdict |
|---|---|---|---|
| **Exa `/findSimilar`** (neighbor-graph) | **No.** 1/16 recall on the calibration anchor (C2). | Name/embedding similarity + mirrors + link-shorteners; anchor-name-dependent (C3, C4). | Not a cross-shop signal. Use only for distinctive-name anchors, and even then corroborate. |
| **Comparison / "alternatives to" pages** | **Partially.** 4/16 recall, incl. 2/4 Tier-1 (C6). | Self-selection: 3/5 owned `/vs` + 1 competitor-intel, only 1/5 a neutral listicle (C7); affiliate junk in the tail; a drugs-not-platforms category confound on GoodRx (C9). | Better than Exa; usable only with cross-source recurrence; not graduation-grade. |
| **Store-only positioning read (017)** | Baseline. | Supply-side inference; buyer-relative; anchored-only floor. | Remains the most trustworthy substrate; the external panel corroborates but doesn't beat it. |

**Where Truffle answered cleanly:** the *calibration* itself — having 017's store-only set let this
run *measure* each external source's recall, which is the load-bearing output. **Where it fell
short:** there is no external source in this panel that converts the substitute/adjacent judgment
into a joinable fact; MRL-011's "relation-as-judgment, don't build the field" is reinforced, now with
demand-side evidence that the field's inputs are unreliable.

## Evidence Used

`bounded-live`; lines up with `run-notes.md` `live_evidence_used`. Exa = captured envelopes
(`receipts/exa/*.json`, summarized in `receipts/analysis-output.txt`); comparison pages =
`receipts/comparison-pages-2026-06-20.md`. External named sets are **secondary/direction-finding**
(demand-side leads, affiliate/SEO/owned-page confounded), never adjudicated truth.

| ID | Claim | Source | Grade |
|---|---|---|---|
| C1 | Exa `/findSimilar` ran on 23 anchors (24 calls incl. 1 Hone smoke test), 25 neighbors each, total ≈ $0.53 | `receipts/exa/*.json`; `analysis-output.txt` | Signal (captured) |
| C2 | Hone Exa top-25 recovered 1 of 16 run-017 neighbors (`hormonemd`); all 4 Tier-1 substitutes absent | `analysis-output.txt` (Hone calibration); `read 017` | Signal + Judgment (calibration) |
| C3 | Exa returns name-collisions / mirrors / link-shorteners (hims→bit.ly, mailchi.mp, HMS Holdings; ro→Roon/ro.am; notion→notion.so/OneNote) | `receipts/exa/hims-com.json`, `ro-co.json`, `notion-com.json` | Signal (captured) |
| C4 | Exa quality tracks anchor-name distinctiveness: `posthog`→real rivals (Plausible/Matomo/Statsig/Clickhouse); common names→junk | `receipts/exa/posthog-com.json` vs `notion-com.json` | Judgment (tied to C3) |
| C5 | 36 telehealth cross-anchor "hubs" (≥2 anchors), nearly all store-absent and dominated by low-authority aggregators/SEO/link tools (linkedin, linktr.ee, tap.bio, comparemedsrx, directmedsusa) | `analysis-output.txt` (TELEHEALTH hubs) | Signal + Judgment |
| C6 | "Hone alternatives" pages recovered 4 of 16 run-017 neighbors (Defy Medical, Peter MD, Maximus, Lifeforce), incl. 2 of 4 Tier-1 | `receipts/comparison-pages-2026-06-20.md` Q1 | Signal (captured) |
| C7 | Of 5 "Hone alternatives" result pages: 3 owned `/vs` (hims, hone, viking) + 1 competitor-intel (cbinsights) + 1 affiliate (policylab) — only 1 neutral third-party | `receipts/comparison-pages-2026-06-20.md` Q1 | Signal (captured) |
| C8 | Store-absent cross-shop nominees surfaced: Numan, Male Excel, Fountain TRT, Viking Alternative Medicine (Hone); Sesame (Ro) | `receipts/comparison-pages-2026-06-20.md` Q1, Q2 | Signal (captured) — capture leads, not verified |
| C9 | "Alternatives to Ro" SERP barely surfaced real GLP-1 peers; GoodRx page named drugs (Qsymia/Contrave/Orlistat/Phentermine), not platforms | `receipts/comparison-pages-2026-06-20.md` Q2 | Signal (captured) |
| C10 | "Notion alternatives" pages recovered real rivals (Coda, Obsidian, Craft, Capacities, ClickUp, Asana, Confluence) where Exa returned mirror-junk | `receipts/comparison-pages-2026-06-20.md` Q3; `receipts/exa/notion-com.json` | Signal (captured) |

## Companies Seen

23 anchors: **telehealth (18)** — honehealth (anchor), mylifeforce, gethealthspan, gogeviti, agelessrx
(longevity/NAD); defymedical, marekhealth, maximustribe, hormonemd (TRT); functionhealth (labs); ro,
hims, henrymeds, remedymeds (GLP-1); rexmd, bluechew (sexual-health); lifemd, nurx (multi/none).
**SaaS (5)** — posthog, notion, linear, airtable, snowflake. Plus ~575 Exa neighbor rows + ~25 named
brands across the comparison pages (see receipts).

## Missing / Stale Coverage

- **Store-absent cross-shop nominees (capture leads, NOT verified — MRL-009):** *Numan*, *Male Excel*,
  *Fountain TRT*, *Viking Alternative Medicine* (Hone/TRT side, C8); *Sesame* (Ro/GLP-1 side, C8).
  These are the only genuinely-actionable corpus-growth output of the run; each is a demand-side
  *lead* requiring a `/research-company` capture to confirm it fronts as a real cross-shop peer.
- **The per-anchor "store-absent neighbor" rate is NOT a clean selection-bias measurement.** 0–3 of
  each anchor's 25 Exa neighbors are captured — but because Exa's neighbors are mostly name-alikes the
  store correctly would not capture, this rate measures Exa noise, not a real coverage gap. (Contrast
  the *clean* selection-bias measurement runs 022/024 got from authoritative listicles.) Flagged, not
  closed.
- Telehealth cross-anchor hubs (C5) include a few real-but-store-absent names worth noting —
  `skinnyrx` (also surfaced in run 012's GLP-1 leaderboard tail), `medmo`, `harleymeds`,
  `collectivehealth` — but the hub list is too aggregator/SEO-contaminated to use as a worklist
  without per-name inspection.

## Source Gaps

- **No review-platform "people also viewed" / search co-occurrence panel.** The two demand-side
  sources tested are the weakest two; a Trustpilot "people also looked at" or true keyword
  co-occurrence panel might be the cleaner cross-shop signal, untested here (out of family).
- **Owned `/vs` pages as a *directed* signal were observed but not systematically mined.** "Brand X
  publishes a vs-Y page" is itself a self-declared, directed cross-shop edge (X treats Y as a threat)
  — a cheap capturable signal, distinct from the noisy listicle named-set. See `W1`.
- SaaS comparison-page corroboration was run only for `notion` (the common-name test); a full SaaS
  arm (per-anchor "alternatives" + owned `/vs`) was deliberately out of budget scope.

## Raw Learning to Preserve

Append to `discovery-ledger.md` in Loop 2: `run-notes.md` Discovery ledger IDs **O1–O4, S1–S2, G1,
W1–W2, F1, V1**. The load-bearing singletons: Exa-similarity≠cross-shop (S1), owned-`/vs`
SEO-self-selection confound (S2/O3), drugs-not-platforms extraction confound (O4), the directed
`/vs`-edge source idea (W1), and the small store-absent capture worklist (O2).

## External Completeness Check

Completeness was **not** the load-bearing axis (this read classifies *source quality*, not a market
census), so no single external denominator is claimed. The calibration *is* the completeness check:
external recall measured against the run-017 store baseline (1/16 Exa, 4/16 comparison-pages). Absence
language throughout says "not found in this panel," never "not a competitor."

## Market Pattern

Across both verticals the demand-side cross-shop surface stratifies the same way: a **noisy
similarity layer** (Exa, dominated by name/embedding collisions) sits below a **self-serving
declaration layer** (owned `/vs` pages + affiliate listicles, where the named set is whoever wrote
the page), and the only trustworthy distillation is **cross-source recurrence** — exactly the filter
runs 012/022/024 already established for the *listicle* family. The new wrinkle: for *cross-shop
neighbor* discovery specifically, the cleanest single source observed is neither — it's the **owned
`/vs` page read as a directed edge** ("who did this brand choose to attack"), which is biased but
self-declared and cheap. Truffle's store-only positioning read remains the most trustworthy substrate;
the external panel corroborates at the margins and supplies a short capture worklist, nothing more.

## What Would Change This Answer

- A **review-platform co-shopping panel** (Trustpilot "people also viewed" / keyword co-occurrence)
  that cleanly recovered ≥2 of 017's Tier-1 set would promote a demand-side source from
  "corroboration-only" to "graduation-candidate."
- **Capturing the 5 store-absent nominees** (C8) and finding they front-door as real Hone/Ro peers
  would convert this run's leads into MRL-001/009 corpus growth and let a future read re-test recall
  against a larger baseline.
- A **distinctive-name SaaS cohort** where Exa `/findSimilar` recovered real rivals at high recall
  would narrow the "Exa is useless" claim to "Exa is name-distinctiveness-bound" (already the C4
  reading) — i.e. confirm the boundary rather than overturn the verdict.
