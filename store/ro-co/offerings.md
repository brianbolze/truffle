---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: ro.co               # company key; each offering's slug (its relative url) is its key *within* the company
captured_at: 2026-06-04     # own freshness; captures/2026-06-04/ holds the source pages
site_notes: "Catalog backbone = the public /pricing/ page — it enumerates per-SKU prices + active ingredient + 'Most popular' badges for EVERY non-GLP-1 line (ED, hair, PE, cold sores/herpes, multivitamin, testosterone, LATISSE, Custom Rx, women's hair). GLP-1 prices live ONLY on /weight-loss/pricing/ (not /pricing/, which shows just the Ro Body membership). Fertility (Modern Fertility kits + Sperm Kit) is the one line with NO published price — intake/quiz-gated, enumerated off the /fertility/ hub + nav. Hair-care add-ons (Revive Shampoo, Restore Conditioner) and Upneeq have no PDP/price — funnel/FAQ only. Prices A/B + promo volatile (own ro-experiments engine; 'Prepay & Save', TrumpRx-matched cash pricing, dated $20-off ED) — re-capture before trusting current. Per-dose GLP-1 ladders (Wegovy pill/pen, Foundayo) sit behind an unrendered 'See pricing details' expander; only Zepbound KwikPen's full ladder is in the FAQ."
---

## Portfolio overview

Ro (Ro/Roman, private) is **Multi-product** — eight consumer-health lines on one telehealth platform: weight
loss (GLP-1s), sexual health (ED + premature ejaculation), hair (men + women), skin/derm, cold sores / genital
herpes, fertility, and daily supplements. This doc enumerates **all eight at SKU grain** (~30 buyable offerings).
The lines sell in three pricing shapes: **published per-dose generics** (ED, hair, herpes — Ro's transparency
wedge), a **membership wrapping a separately-billed med roster** (weight loss), and **intake-gated kits with no
public price** (fertility).

**Where prices live (the capture's load-bearing finding).** Ro publishes a single all-condition `/pricing/`
page that lists per-SKU price + active ingredient + "Most popular" badge for every line **except** GLP-1s and
fertility. GLP-1 med prices live only on `/weight-loss/pricing/`; `/pricing/`'s "Weight management" block shows
**only the Ro Body membership** ($39/$74/$149). **Fertility has no published price anywhere** — the Modern
Fertility kits + Sperm Kit are quiz/intake-gated (`[on-request]`).

**The shape finding — "testosterone" at Ro is *not* TRT.** Ro's only testosterone offering is **Testosterone
Support**, an OTC "Daily supplement" (`$35/mo` monthly / `$29/mo` quarterly) shelved next to the men's
multivitamin — no prescription testosterone, no TRT gel/injection, no lab-and-treat path anywhere captured; the
page never names an active molecule ("you can't get this blend anywhere else"). Treat any "Ro does TRT" read as
**unsupported by this capture**. (Deep block below.)

**Visibility shapes, by line:**
- **`[published]`** — ED (Sparks, Daily Rise, generic/branded Viagra & Cialis), hair (men + women), PE, cold
  sores/herpes (valacyclovir), skin (Custom Rx, enriching cream, LATISSE), daily supplements: a full price /
  dose-ladder is shown on `/pricing/`.
- **`[partial]`** — the Ro Body membership wrapper is itself `[published]` (flat fee shown), but **every GLP-1
  med SKU is `[partial]`**: a promo "first month" price shows, yet the all-in rides a dose ladder **plus** the
  mandatory, separately-billed membership, and the med only ships after intake + Rx.
- **`[on-request]`** — fertility (Modern Fertility kits, Prenatal, Sperm Kit), Upneeq (FAQ-only), Saxenda
  (nav-listed, no price/molecule shown), and the hair-care add-ons (Revive Shampoo, Restore Conditioner).

**Prominence (calibrated).** Weight loss is the foregrounded hero **[HIGH]** — promo bar ("FDA-approved GLP-1s
at their lowest prices"), the first homepage product section, celebrity ambassadors (Serena Williams, Charles
Barkley), and the only line with a dedicated `/weight-loss/pricing/` page. Sexual health is the second homepage
section and legacy strength **[HIGH for the line]**, with **Ro Sparks carrying a "Best seller" badge** — an
own-label hero **[HIGH]**. Other own-label badges (the strongest prominence signal): **Roman Swipes** "Most
popular" (PE), **Custom Rx Treatment** "Most popular" (derm), **Modern Fertility Hormone Test** "Best seller"
(fertility) — all **[HIGH]** within their line. **No GLP-1 SKU carries a popularity badge** (only stock tags
"New"/"In stock"/"Supply available", which are availability not emphasis **[LOW]**); the GLP-1 card order leads
with the three cash-pay pills (Wegovy pill, Zepbound KwikPen, Foundayo) **[MED]**. Within ED/Cialis/Viagra, a
single dose carries "Most popular" (within-product dose emphasis, not line-level). Hair, women's hair, herpes,
and daily health show no badges — nav order only **[LOW]**.

## Roster

Complete at the indexed level across all eight lines. Within-company key = **Slug** (an attested URL from a
captured page; a card with no PDP notes `(no PDP — …)`). Price quoted verbatim with its on-page markers;
molecule/form is **page-attested** (never inferred from the brand — see the molecule audit under Verbatim
anchors). Same-molecule offerings here are **never** asserted equal to another brand's. The two Zepbound rows
share one slug (`/weight-loss/zepbound/`) — the cash (KwikPen) and insurance faces of one tirzepatide PDP.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| **Weight loss** | family | — | `/weight-loss/` | — | — | GLP-1 line; the Ro Body membership gates a med roster behind an online visit + Rx, med billed separately. |
| Ro Body membership | buyable | Weight loss | `/weight-loss/` | `$39 first month, $74/mo thereafter prepaid on annual plan` (monthly `$149/month`) | published | — · subscription · the cash-pay wrapper (GLP-1 access + insurance concierge + coaching/labs); **medication billed separately**; metabolic test = Quest (incl.) or `$75` at-home kit. [^mem] |
| Wegovy pill | buyable | Ro Body | `/weight-loss/wegovy-pill/` | `$149 first month` · `$199-$299 thereafter` | partial | semaglutide · oral pill · **cash-pay only**; "first FDA-approved GLP-1 pill"; dose ladder + membership gate the all-in. [^glp] |
| Foundayo pill | buyable | Ro Body | `/weight-loss/foundayo/` | `$149 first month` · `$199-$299 thereafter` | partial | orforglipron · oral pill · **cash-pay only**; "newest FDA-approved GLP-1 pill"; "same price as LillyDirect". [^glp] |
| Zepbound KwikPen | buyable | Ro Body | `/weight-loss/zepbound/` | `$299 first month` · `$399-$449/mo thereafter` | partial | tirzepatide · pen · **cash-pay only**; "fastest-working GLP-1"; full cash dose ladder + refill penalty in anchor. [^kwik][^glp] |
| Wegovy pen | buyable | Ro Body | `/weight-loss/wegovy/` | `$199 first month` · `$199-$399 thereafter` | partial | semaglutide · weekly injection pen · insurance-or-cash; "half the retail price when paying cash". [^glp] |
| Zepbound pen | buyable | Ro Body | `/weight-loss/zepbound/` | `Copays vary` (insurance); cash via KwikPen | partial | tirzepatide · pen · insurance face; cash buyers routed to the KwikPen variant. [^glp] |
| Ozempic | buyable | Ro Body | `/weight-loss/ozempic/` | `$900-$1100 a month without insurance` | partial | semaglutide · weekly injection · FDA-approved for T2D, **off-label** for weight loss; pick up + pay at pharmacy; also insurance-eligible. [^glp] |
| Saxenda | buyable | Ro Body | `/weight-loss/saxenda/` | — (no price shown) | on-request | **not stated** · injection · nav-listed PDP; no price or molecule on any captured page. |
| **Sexual health — ED** | family | — | `/erectile-dysfunction/` | — | — | "Up to 95% off with generics"; Sparks/Gummies compounded, generics/brands published. |
| Ro Sparks | buyable | ED | `/erectile-dysfunction/sparks/` | `4x $48/mo · 6x $72/mo · 8x $96/mo · 10x $120/mo` | published | sildenafil 55mg + tadalafil 22mg · compounded sublingual · **"Best seller"**; "works in 15 min, lasts up to 36 hrs"; not FDA-approved; quarterly $15 off. [^compound] |
| Daily Rise Gummies | buyable | ED | `/erectile-dysfunction/daily-rise-gummies/` | `1-month (30 doses) $89/mo · 3-month (90 doses) $69/mo` | published | tadalafil 7mg · compounded daily gummy · "sex-ready 24/7"; not FDA-approved; quarterly $20 off. [^compound] |
| Generic Viagra (Sildenafil) | buyable | ED | `/erectile-dysfunction/sildenafil/` | `25mg $4 · 50mg $6 · 100mg $10` (dose ladder `20mg $2 · 40mg $4 · 60mg $6 · 80mg $8 · 100mg $10`) | published | sildenafil · oral tablet · "up to 95% cheaper than branded"; 50/60mg = "Most popular". |
| Branded Viagra | buyable | ED | `/erectile-dysfunction/viagra/` | `25mg $90 · 50mg $90 · 100mg $90` | published | sildenafil (brand) · oral tablet · "ready in up to 60 min, lasts 6 hrs". |
| Generic Cialis (Tadalafil) | buyable | ED | `/erectile-dysfunction/cialis/` (also `/tadalafil/`) | `5mg $11 · 10mg $44 · 20mg $44`; daily `2.5mg $8 · 5mg $8` | published | tadalafil · oral tablet · as-needed + daily options; 5mg / daily 2.5mg = "Most popular"; *dosing minimums apply. |
| Branded Cialis | buyable | ED | `/erectile-dysfunction/cialis/` | `5mg $20 · 10mg $80 · 20mg $80` | published | tadalafil (brand) · oral tablet · 5mg = "Most popular"; *dosing minimums apply. |
| **Premature ejaculation** | family | — | `/premature-ejaculation/` | — | — | OTC Roman Swipes + oral Rx; monthly or quarterly, no commitment. |
| Roman Swipes | buyable | PE | `/products/swipes/` | `Monthly $27/mo` · `$22/mo` (save $60/yr) | published | 4% benzocaine · OTC topical wipes · **"Most popular"**. |
| Sertraline | buyable | PE | `/medications/sertraline/` | `Monthly plan $24/mo` | published | sertraline (generic Zoloft) · oral · off-label for PE; boxed warning. |
| **Hair loss — men** | family | — | `/hair-loss/` | — | — | Quarterly-only shipments; oral + topical finasteride/minoxidil. |
| Ro Mane Spray | buyable | Hair (men) | `/medications/ro-mane-spray/` | `Quarterly $50/mo` · `6-month $43/mo` | published | finasteride + minoxidil + tretinoin · 3-in-1 compounded topical spray · not FDA-approved. |
| Finasteride | buyable | Hair (men) | `/medications/finasteride/` | `Quarterly $20/mo · 6-month $18/mo · 12-month $16/mo` | published | finasteride (generic Propecia) · oral · men only. |
| Oral Minoxidil | buyable | Hair (men) | `/medications/oral-minoxidil/` | `Quarterly $30/mo · 6-month $27/mo · 12-month $24/mo` | published | minoxidil (generic Loniten) · oral · off-label, Black Box Warning. |
| Topical Minoxidil | buyable | Hair (men) | `/medications/minoxidil/` | `Quarterly $16/mo · 6-month $14/mo · 12-month $13/mo` | published | minoxidil (generic Rogaine) · 5% topical solution · for the crown. |
| Ro Revive Shampoo | buyable | Hair (men) | `(no PDP — hair-loss hub card; funnel start.ro.co/kwrssq)` | — (no price shown) | on-request | not stated · OTC shampoo · "Cleans & thickens". |
| Ro Restore Conditioner | buyable | Hair (men) | `(no PDP — hair-loss hub card; funnel start.ro.co/qcalmd)` | — (no price shown) | on-request | not stated · OTC conditioner · "Fortify & thicken". |
| **Hair loss — women** | family | — | `/womens-hair-loss/` | — | — | Dermatologist-designed; quarterly. |
| Women's Oral Minoxidil | buyable | Hair (women) | `/medications/womens-oral-minoxidil/` | `Quarterly $30/mo` | published | minoxidil · oral · off-label, cardiac warning. |
| Hair Solution Rx | buyable | Hair (women) | `/medications/hair-solution-rx/` | `Quarterly $40/mo` | published | minoxidil + tretinoin + melatonin · compounded topical · Rx only, not FDA-approved. |
| **Skin / dermatology** | family | — | `/dermatology/` | — | — | Compounded Rx skincare + LATISSE; "Join 250,000+ Ro patients". |
| Custom Rx Treatment | buyable | Skin | `/dermatology/custom-rx-treatment/` | `Bi-monthly $29/mo` | published | compounded blend (may incl. tretinoin, azelaic acid, niacinamide, vit E, tranexamic acid, ceramides, hyaluronic acid) · topical · **"Most popular"**; not FDA-approved; formerly "Nightly Defense". [^compound] |
| Enriching cream | buyable | Skin | `(no PDP — /pricing/ #Custom Rx Skincare; funnel start.ro.co/qyftkx)` | `Bi-monthly $8/mo` | published | not stated · topical cream · derm add-on. |
| LATISSE | buyable | Skin | `/medications/latisse/` | `1-month (3mL) $110` · `3-month (5mL) $159` | published | bimatoprost ophthalmic solution 0.03% · topical lash serum · FDA-approved; $20 off first 5mL. |
| Upneeq | buyable | Skin | `(no PDP — derm FAQ mention only)` | — (no price shown) | on-request | oxymetazoline HCl ophthalmic solution 0.1% · Rx eye drop · for acquired ptosis (low-lying lids). |
| **Cold sores / Genital herpes** | family | — | `/cold-sores/` · `/genital-herpes/` | — | — | One molecule, two condition framings. |
| Valacyclovir | buyable | Cold sores / herpes | `/medications/valacyclovir/` | `3 outbreaks (1000mg) $42/3mo · 6 outbreaks (1000mg) $60/3mo · prevent (500mg daily) $87/3mo · prevent (1000mg daily) $144/3mo` | published | valacyclovir (generic Valtrex) · oral antiviral · FDA-approved for herpes; off-label daily suppression. |
| **Daily health** | family | — | (supplements) | — | — | OTC men's supplements. |
| Ro Daily | buyable | Daily health | `/supplements/mens-daily-multivitamin/` | `Monthly $35/mo` · `Quarterly (3 mo) $29/mo` ($87/3 mo) | published | 23-nutrient multivitamin blend · OTC supplement · "$15 off first order". |
| Testosterone Support | buyable | Daily health | `/supplements/testosterone-support/` | `Monthly $35/mo` · `Quarterly (3 mo) $29/mo` ($87/3 mo) | published | **not stated** · OTC daily supplement · **NOT prescription TRT** ("this blend"); "$15 off first order". [deep block] |
| **Fertility** | family | — | `/fertility/` | — | — | Modern Fertility (acquired by Ro); no published price — quiz/intake-gated. |
| Modern Fertility Hormone Test | buyable | Fertility | `/testing/fertility-hormone-test/` | — (no price; "Take quiz") | on-request | at-home finger-prick hormone test · **"Best seller"**; CLIA/CAP-accredited lab. |
| Ovulation Test | buyable | Fertility | `/testing/ovulation-test/` | — (no price) | on-request | at-home ovulation test · pre-conception. |
| Pregnancy Test | buyable | Fertility | `/testing/pregnancy-test/` | — (no price) | on-request | at-home pregnancy test. |
| Prenatal Multivitamin | buyable | Fertility / Daily health | `/supplements/prenatal-vitamins/` | — (no price) | on-request | prenatal supplement · pre-conception. |
| Sperm Kit | buyable | Fertility | `(no PDP — spermkit.ro.co subdomain)` | — (no price) | on-request | at-home sperm test kit · men's fertility. |

### Verbatim anchors

The footnotes the Price column points at — what decides `[partial]` vs `[published]`, plus the molecule-sourcing
audit. Quoted exactly from the cited `captures/2026-06-04/` pages.

- **[^mem] Ro Body membership (the wrapper, `[published]`):** `/pricing/` tile — *"Ro Body · Weight loss
  medication · Monthly membership **$39 first month, $74/mo thereafter prepaid on annual plan**"*; the FAQ
  (weight-loss-pricing, weight-loss-how-it-works) restates *"The Ro Body membership costs **$39 for the first
  month** and as low as **$74/month** when you prepay for an annual plan. If you stay on a monthly plan, the
  ongoing cost is **$149/month**. … the cost of GLP-1 medication is not included."* Membership is **cash-pay
  only** (*"only available by cash pay only and does not accept insurance"*). Metabolic test: *"testing at any
  Quest location is included … Or you can purchase an at-home blood collection kit through Ro for **$75**."*
- **[^glp] every GLP-1 med SKU (the `[partial]` driver):** each tile footnotes *"**Additional Ro Body
  membership fee required.** The Ro Body membership fee is as low as $74/month when you prepay on an annual
  plan."* (weight-loss-pricing). Cash framing: *"Options start at **$149/month**\* and increases for higher
  doses"* (\* *"new patients can start on the lower doses of Wegovy pill for $149/mo"*). Insurance SKUs (Zepbound
  pen, Ozempic, Wegovy pen): *"**Copays vary** depending on your insurance."* "Prepay & Save unlocks the lowest
  medication prices — **Save $100/mo on the Wegovy pen and $50/mo on the Wegovy pill** with an annual plan."
  Lowest-cash claim: *"the same prices as LillyDirect®, NovoCare®, and TrumpRx."* → a starting number shows but
  the all-in = membership + dose ladder + Rx ⇒ `[partial]`.
- **[^kwik] Zepbound KwikPen full cash dose ladder + refill penalty (weight-loss-pricing FAQ):** *"$299/mo for
  2.5 mg dose; $399/mo for 5 mg dose; $449/mo for 7.5 mg, 10 mg, 12.5 mg, and 15 mg doses (with manufacturer
  offer)."* Miss the 45-day refill check-in: *"You'll be charged the full price for your refill: **$499** for a
  7.5 mg refill; **$699** for 10 mg, 12.5 mg, and 15 mg refills."* The tile summary is the roster's `$299 first
  month / $399-$449/mo thereafter`. (Wegovy pill/pen + Foundayo dose-by-dose ladders sit behind a client-side
  "See pricing details" expander that did not render — only their "first month" + "thereafter" ranges show.)
- **[^compound] compounded-but-priced (still `[published]`):** Ro Sparks, Daily Rise Gummies, Ro Mane Spray,
  Hair Solution Rx, and Custom Rx Treatment are compounded and *"not FDA-approved,"* yet each shows a full
  self-contained price on `/pricing/` — so `[published]`, with the not-FDA-approved status carried in **What**,
  not a visibility downgrade (visibility is "can I get a price?", not regulatory status).
- **Molecule sourcing (page-attested-only rule, audited):**
  - **GLP-1s** — *semaglutide* → Wegovy pill, Wegovy pen, Ozempic; *tirzepatide* → Zepbound KwikPen + pen;
    *orforglipron* → Foundayo. All attested verbatim under each card on weight-loss-pricing + the weight-loss
    hub. **Saxenda → "not stated"** (no captured page names its molecule; not inferred).
  - **ED** — *"Sildenafil 55mg, Tadalafil 22mg"* (Ro Sparks), *"Tadalafil 7mg"* (Daily Rise), *"Sildenafil"*
    (generic + branded Viagra), *"Tadalafil"* (all Cialis) — all on `/pricing/`.
  - **Hair** — Ro Mane Spray *"compounded prescription medication formulated with finasteride, minoxidil, and
    tretinoin"* (hair-loss hub); Hair Solution Rx *"formulated with minoxidil, tretinoin, and melatonin"*
    (`/pricing/`); finasteride / minoxidil are the SKU names (generic Propecia / Loniten / Rogaine).
  - **Skin** — LATISSE *"bimatoprost ophthalmic solution 0.03%"*; Upneeq *"oxymetazoline hydrochloride
    ophthalmic solution, 0.1%"*; Custom Rx *"may include: Tretinoin, Azelaic acid, Niacinamide, Vitamin E
    acetate, Tranexamic acid, Ceramides, Hyaluronic acid"* (all derm FAQ). Enriching cream → "not stated".
  - **Herpes** — valacyclovir (generic Valtrex), stated on `/pricing/`.
  - **Daily health** — Ro Daily *"23 nutrients"* (a multivitamin blend, not a single molecule); **Testosterone
    Support → "not stated"** — *"this blend," "every active ingredient,"* no hormone/compound named (the
    not-TRT finding; deep block).
  - **Fertility** — tests/supplements, no drug molecule.

## Deep blocks

One block earns its place — the not-TRT disambiguation a roster cell can't carry. Everything else (GLP-1 dose
ladders, the compounded-vs-published nuance, the valacyclovir cold-sores/herpes dual-listing) is fully resolved
by the roster + verbatim anchors; reproducing it as blocks would only restate cells. **No PDP-anatomy block** —
this run is a price/roster consumer, not a copy/structure one.

### Testosterone Support — an OTC supplement, *not* prescription TRT

- **Parent:** Daily health · **slug:** `/supplements/testosterone-support/` · **price:** `$35/mo` (monthly) ·
  `$29/mo` (quarterly, 3-mo supply, `$87/3 mo`) · **visibility:** `[published]`

> **Section + tile (verbatim, `/pricing/`):** "Created by doctors, backed by science. You can't get this blend
> anywhere else. Every active ingredient is backed by studies showing improvement in at least one area of male
> virility. Get $15 off your first order · Available monthly ($35/mo.) and quarterly ($87/3 mo.)"
> **Tile:** "Testosterone Support · Daily supplement · Monthly plan **$35 / mo** · Quarterly plan (3 mo supply)
> **$29 / mo**"
> **Molecule:** *not named on any captured page* — "this blend," "every active ingredient," no hormone or
> compound stated.

**Why this block earns its place:** the single most likely cross-brand mis-grouping against a telehealth roster
is "Ro testosterone = TRT." It isn't. Ro's only testosterone offering on these pages is an **OTC daily
supplement** at `$35/mo` — no prescription, no testosterone hormone, no gel/injection, no lab-and-treat path
appears anywhere in the captured set. The roster row flags this; the block carries the verbatim proof + the
**absence finding** a cell can't: a TRT line elsewhere on ro.co can't be ruled out by this sample, but within
this capture it is **not found**. (Contrast Hims, whose testosterone line *is* a prescription enclomiphene
product — same word, different shape.)

## Provenance

- **Pages read (8 priced/roster pages, all `captures/2026-06-04/`):** `pricing.md` (/pricing/ — the
  all-condition price + molecule + badge backbone), `weight-loss-pricing.md` (/weight-loss/pricing/ — GLP-1
  dose ladders + membership), `weight-loss.md` (/weight-loss/ — GLP-1 cards + prominence), `erectile-dysfunction.md`
  (ED prominence + Sparks/Gummies), `hair-loss.md` (men's hair molecules + Revive/Restore add-ons),
  `dermatology.md` (Custom Rx ingredients, LATISSE, Upneeq), `fertility.md` (Modern Fertility kits + Sperm Kit),
  `weight-loss-how-it-works.md` (membership FAQ). Cross-checked against `homepage.md` (full mega-nav — the second
  blind source for completeness). Context: `store/ro-co/profile.md`.
- **Completeness (blind-source agreement):** the published lines are confirmed by `/pricing/` ∩ the homepage
  mega-nav (two sources that don't see each other). Slug-bearing PDPs all trace to a captured page; non-PDP
  cards are flagged `(no PDP — …)` and never constructed.
- **Scope:** all eight lines enumerated at the indexed level. **Not enumerated:** per-dose GLP-1 ladders for
  Wegovy pill/pen + Foundayo (behind an unrendered "See pricing details" expander — only first-month/thereafter
  ranges shown; Zepbound KwikPen's full ladder *is* captured via FAQ); per-condition PDPs not individually
  scraped (prices read off `/pricing/` + the hubs).
- **Gated / unreachable / unpriced:** all fertility SKUs (Modern Fertility Hormone/Ovulation/Pregnancy Test,
  Prenatal, Sperm Kit — quiz/intake-gated, no public price); Upneeq (derm FAQ mention, no PDP/price); Saxenda
  (nav-listed, no price or molecule on captured pages); Revive Shampoo + Restore Conditioner (hub cards, funnel
  links, no price); GLP-1 medication all-in cash cost (dose-laddered + provider-titrated + separately-billed
  membership — "thereafter" ranges are floors, not totals); Testosterone Support / enriching cream molecules
  (unnamed blends).
- **Point-in-time snapshot, not fixed:** Ro runs its own A/B engine (`ro-experiments`) + promo-driven offers
  ("Prepay & Save", TrumpRx-matched cash pricing, a dated "$20 off your next ED order … through 6/7") — this
  module's `captured_at` + a short TTL are the guard; re-capture before trusting a price as current.
- **Run profile:** all-SKU expansion (2026-06-04) — prior `offerings.md` (2026-06-03, schema 1.0) enumerated
  only weight-loss + testosterone; this run re-captured fresh and enumerated **all eight lines** (~30 SKUs).
  Stamped schema 1.1 (added `site_notes`). No hero-image / PDP-anatomy modules (price/roster consumer).
