# Findings — offerings-module tournament: does `offerings.md` beat extending `profile.md`?

> **Verdict: BUILD `offerings.md` — but roster-first, and lighter than the 2026-06-01 draft.** A
> probe-grounded tournament (3 designs × 4 telehealth companies, produced → adversarially verified →
> answered cold) put the module decisively past the baseline on the live per-SKU/molecule consumer
> query: **B1 (roster-first) scored 8.3 vs baseline 5.5**, filling **35 molecule×form rows vs 14**, and
> was the *only* design that prices all four brands' GLP-1s (baseline leaves Ro's whole GLP-1 lineup
> gated). Three sharp seconds: (1) the win is the **roster**, not the deep blocks — cold agents answered
> from the table; deep blocks earned ~3 correctness-guard cells and otherwise "merely restated roster
> prices"; (2) the **molecule-pivot (B2) backfires** — same captures, but only 14 rows (no gain over
> baseline) *and* it induced the exact anti-Doro failure the exercise tests for (tagged Mounjaro
> "tirzepatide" with no page support; wrong slugs on its own declared key); (3) the recipe is **free over
> baseline** — all three designs read the same 15-credit capture, so the module is a structuring choice
> over already-captured state, not new spend.

*2026-06-03. The activation probe the [offerings design](../../_design/2026-06-01-offerings.md) left
open ("§Activation — open"), and the per-SKU re-trigger [Probe 0](../2026-06-01-profile-enrichment/FINDINGS.md)
parked it behind. The live per-SKU consumer (the Teleprescribe Venture's Products/SKUs) has appeared, so
the trigger is met — this tests what to build, not whether a consumer exists.*

## Method

A probe-grounded tournament, judged on **what each design produces from real pages**, not how it reads.

- **Contestants (each a coupled recipe+schema+destination):** **A — baseline** (extend `profile.md`'s
  *What they offer* family lines + price-visibility token); **B1 — roster-first `offerings.md`** (the
  2026-06-01 incumbent: overview → deep blocks → roster table, molecule in "What", slug-keyed); **B2 —
  molecule-pivoted `offerings.md`** (same skeleton, but the roster leads with a **Molecule** column).
- **Probe set (span the gating spectrum):** **Ro** (per-SKU prices published, incl. a `/weight-loss/pricing/`
  page) · **Hims** (big GLP-1 lineup, med-only floors + a mandatory separate membership → `[partial]`) ·
  **Maximus** (TRT flagship with a published 1/3/12-mo plan ladder; GLP-1 floors only) · **Remedy Meds**
  (`Single`, GLP-1 only, 2 of 4 SKUs priced).
- **Harness (25 agents):** per company, a recipe-driven **capture** (reuse warm, Firecrawl the gaps) →
  **produce** B1 & B2 → **adversarially verify** each against the source pages (author ≠ judge: every
  SKU caught? prices verbatim + greppable? any hallucinated cross-company canon?) → a **cold agent**
  answered the decisive query from each design's artifacts *alone* → an **independent judge** scored the
  three. Captures + all 12 artifacts persisted under [`captures/`](captures/) + [`artifacts/`](artifacts/).
- **The decisive query (molecule-grouped price table):** *"Across these brands, build one cited table of
  every GLP-1/TRT offering — molecule, form/dose, branded-or-compounded, SKU name, verbatim starting
  price, price-visibility — then group by molecule×form and name the cheapest brand per molecule. Use
  only the artifacts; no prior knowledge."*

## Findings

**1. The module beats the baseline decisively — and the reason is structural, not cosmetic.**
Cold-answer resolution: **baseline 14 / B1 35 / B2 14** molecule×form rows; judge overall **5.5 / 8.3 /
6.4**. Baseline's two holes are felt immediately: (a) **Ro's entire GLP-1 lineup is unpriced** — the
family line collapses six GLP-1 SKUs into one *"Ro Body membership … medication cost billed separately
`[partial]`"* line, so a four-brand price table is missing one brand's GLP-1 prices outright; (b) it
**collapses sema oral/injection/compounded and tirz pen/vial/compounded into single buckets**, making
several cheapest-per-molecule calls "genuinely unknowable from this source" (its own words). B1 prices
all six Ro SKUs ($149 first / $199–$299 thereafter, etc.) **from the same `/weight-loss/pricing/` page** —
the family line simply has no room for six SKU prices, and cramming them into `profile.md` would bloat
the cross-corpus point-read for a per-SKU consumer that is cohort-specific. The win is a **separation of
concerns**, not data the baseline couldn't physically hold.

**2. The win is the ROSTER; the deep blocks are a thin correctness guard.** Instrumented `artifact_parts_used`:
the cold agents drove every cheapest-per-molecule call from **roster rows** (SKU + verbatim price +
visibility + molecule/form in "What"). B1's deep blocks earned exactly ~3 cells worth keeping — the
`$99/mo` enclomiphene FAQ figure (which *flips* the enclomiphene cheapest call to "Maximus is the
on-page/published one"), the compounded-vs-branded / "is this even TRT?" framing (which prevents
mis-grouping Ro's supplement and Hims's enclomiphene as TRT), and one dose ladder (a dose cell — moot,
since dose is "not in source" for ~20 rows). B2's own agent said it plainly: deep blocks "earned their
place in exactly 2 spots… elsewhere merely restated roster prices." → **Lead with the roster; make deep
blocks earned, not default.**

**3. The molecule-PIVOT (B2) backfires — twice.** Same captures, same 100% fillability, but **only 14
rows — identical resolution to the prose baseline**: pivoting the table to a Molecule lead-column bought
*zero* answerable granularity for this query. Worse, it induced the precise failure the exercise tests
against: the verifier caught **hallucinated canon** — B2 tagged Mounjaro (and a modal Zepbound pen)
`tirzepatide` though *no Hims page states the molecule* (the page says only "a weekly GLP-1 injection") —
plus **two wrong slugs** on Hims (`/enclomiphene-supplements` vs the real `/enclomiphene`), and Slug *is*
the declared within-company key. Making molecule the authoritative lead column pressures the producer to
fill it from outside knowledge. B1, with molecule as a *descriptive* token inside "What", stayed
page-faithful (zero hallucinated canon on all four companies) **and** the cold agent still grouped by
molecule fine. → **Keep molecule in the descriptive cell, page-attested only; do not pivot, and do not
add a canonical molecule column yet.**

**4. Fillability is proven and the recipe is free over baseline.** Verification: **100% completeness on
all four companies** for the roster design (`source_sku_count ≈ artifact_sku_count` throughout). Capture
cost: **Ro 3 + Hims 6 + Maximus 6 + Remedy 0 (warm) = 15 Firecrawl credits** for the cohort — and **all
three designs read the same pages**, so B1's marginal Firecrawl cost over baseline is **zero**. The
recipe is "capture the per-condition product/pricing pages" — largely what `/research-company` already
targets, plus a dedicated `/pricing` page where one exists (Ro). No cross-company canonical key needed.

**5. Gating is real, and the per-SKU row + token carry it where the family line can't.** Even where the
all-in price is quiz/membership-gated, the roster captures a per-SKU **floor + `[partial]`/`[on-request]`
token** — and that surfaces the venture-relevant story the family line blurs: **compounded undercuts
branded all-in** (Maximus compounded semaglutide `$149.99` all-in vs Ro/Hims branded `$149` *med-only +
a separate $74–$149/mo membership*), and **"testosterone" ≠ TRT** at three of four brands (Ro = OTC
supplement; Hims = compounded enclomiphene, explicitly "no synthetic testosterone," + cypionate "coming
2026"; Remedy = none; real buyable TRT only at Maximus).

**6. The two warts are recipe-discipline lessons, not schema flaws.** B1's only blemish: Remedy
`price_verbatim_ok=false` — but every *number* is verbatim-correct; it fabricated *where* the price is
published (claimed the homepage shows prices; misplaced the sema "$299/mo" string). B2's Mounjaro tag is
the molecule-from-brand-name leak. Both convert directly into recipe rules: **cite the exact page a price
sits on; record molecule only from page text, else "not stated."**

## Caveats — what this sample can't see

- **Vertical + grain:** telehealth GLP-1/TRT, four enumerable companies. The module's win is demonstrated
  for an enumerable, price-publishing-ish vertical — exactly the cohort with a live consumer. `Catalog`
  shapes (Nike/AWS) are unchanged (shape-only, per the draft) and were not re-probed.
- **Dose is unreachable, so a dose-comparison consumer stays unserved.** Dose/strength is absent for ~20
  of the SKUs (provider-titrated, quiz-gated); only Ro's Zepbound ladder and Hims's Wegovy-pen range are
  published. Don't promise a dose field as load-bearing.
- **Prices are a point-in-time snapshot.** Ro/Hims run A/B + promo pricing ("for a limited time" on every
  Wegovy/Foundayo start) — `offerings.md`'s own `captured_at` + a short freshness TTL matter most here.
- **Cold-test caveat (inherited from Probe 0):** the cold agents were independent of production, but the
  baseline artifact is `profile.md`'s existing family section — a fair test of the grain, not of a
  maximally-enriched profile (Probe 0 already showed family-grain enrichment barely helps).

## Follow-on — recipe + prominence probes (2026-06-03)

Two lightweight probes after the tournament nailed the *recipe* (gathering) half + the prominence signal.

**Firecrawl `/search` vs `/map` for roster enumeration (live, ~24 credits).** Domain-filtered search on
warm companies vs. the known SKU roster: a **generic keyword query** (`weight loss GLP-1` + `includeDomains`)
returned SEO/blog noise — **1 of 7** Hims SKUs; brand-name OR queries collapsed to 2 results. A
**path-prefix query** (`site:hims.com/weight-loss`) returned **7 of 7** SKUs with usable labels, clean, 4
credits — *but only because Hims separates products (`/weight-loss/<sku>`) from content (`/blog`,
`/guides`)*. The same query on Ro (which nests its content farm under `/weight-loss/`) gave ~20% products
and missed SKUs. → **Enumeration ladder:** index-page scrape (authoritative, structure-independent) as the
backbone; `site:domain/path` search as a cheap accelerant on clean-taxonomy sites only; `/map` as a flat
census. Never keyword/brand search to enumerate, never search `position` for prominence (Google rank ≠
emphasis); `/crawl` + `/extract` stay off the path. ~10–20 credits for a 20-SKU company.

**Prominence read (2 independent readers each on Hims + Ro, warm captures).** Both readers per company
**converged** on the portfolio-level emphasis (weight-loss leads `[HIGH]`; the #2 companion; the demoted
franchises) and both independently down-calibrated the soft parts (rotating hero, carousel order) to LOW —
so a **calibrated emphasis narrative** is reliable, with confidence tied to signal stability. It lives in
the **Portfolio overview**, not a per-row field. Capture-sufficiency: the warm captures' **full-page
screenshots + rawHtml** were load-bearing and present (un-pruned here), so the read must run **at capture
time** before payloads prune. Gotchas: popularity-badge ≠ stock-tag; scope badge grep to rendered text
(the `FeaturedTile` CSS trap); exclude alphabetical index pages from order inference.

Both fold into [`../../_design/2026-06-03-offerings-module.md`](../../_design/2026-06-03-offerings-module.md)
(§The recipe, §Prominence).

## Decision

Activate `offerings.md`, **roster-first and store-only**, per the proposal in
[`_design/2026-06-03-offerings-module.md`](../../_design/2026-06-03-offerings-module.md). The baseline
(`extend profile.md`) **loses decisively** for the per-SKU/molecule consumer — but `profile.md`'s family
lines + visibility token **stay** as the cross-corpus point-read; `offerings.md` is the opt-in per-SKU
layer (telehealth cohort first). Reject the molecule-pivot; demote deep blocks to earned. Promotion to
the venture's Notion Products/SKUs is sketched, not designed (propose-only, later).

---

<sub>**Artifacts:** [`captures/`](captures/) (15-credit shared source, 4 companies) · [`artifacts/`](artifacts/)
(12 produced docs: `baseline-*`, `B1-*`, `B2-*`). Tournament: 25 agents, ~3.2M tokens, 2026-06-03. The
[full run record](.) (scorecards, cold answers, judge verdict) is the workflow output.</sub>
