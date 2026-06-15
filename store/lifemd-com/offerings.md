---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.2"
domain: lifemd.com          # company key; each offering's slug (its relative url) is its key *within* lifemd
captured_at: 2026-06-15     # own freshness; captures/2026-06-15/ holds the source pages
enumeration: indexed-complete   # capture-scope reached vs portfolio_shape — gates count-trust (see Provenance)
site_notes: "Catalog is PROGRAMS, not product PDPs — lifemd.com sells care programs; commerce is a walled funnel on care.lifemd.com (booking) + rx.lifemd.com (enrollment), no public CMS/products.json. Backbone = nav links + /map census + site:lifemd.com map passes (all converge on ~6 priced program pages; /map is /learn-blog + /drugs-index dominated — filter both). Named med SKUs live only INSIDE the Weight-Mgmt + Mental-Health + Women's-Health program pages; each Mental-Health card links to a real lifemd.com/drugs/<letter>/<molecule> PDP (molecule is IN the slug). Prices are split: care/program fee on /membership + each program page; medication priced separately and A/B-volatile (Wegovy Pen 'from $199' ↔ 'from $499' on one page; homepage ‡ first-month discount was $75 in 2026-06-04 capture, now $39 — re-check next run). The wegovy.com PDP footnote still says '$75 today' while the homepage ‡ says '$39 today' on the same 2026-06-15 run — A/B pricing. /mental-health renders the homepage (no dedicated program page); the branded med grid and all MH pricing live on /psychiatry. ED/PE + Sleep route OFF-domain (rexmd.com, rx.lifemd.com/sleep-xp1) — not LifeMD's own funnel."
---

## Portfolio overview

LifeMD (NASDAQ: LFMD) is **Multi-product**, and its catalog is organized at the level of **care programs, not
product PDPs.** The company sells a $19/mo membership front door, then layers four specialty programs on top
(weight management, women's health, mental health, cardiovascular) plus urgent/primary care and at-home labs.
The whole commerce funnel is **walled** — every "Get Started" CTA leaves lifemd.com for the `rx.lifemd.com`
enrollment app or `care.lifemd.com` booking app behind a quiz/intake — so there are **no public per-SKU PDPs for
programs**. The indexed level this roster captures is therefore the **program** (the unit LifeMD prices and
nav-indexes), with the **named medication SKUs enumerated inside three programs** (Weight Management, Mental
Health, Women's Health) where the program page renders a labeled med-card grid.

**The shape finding: a program here bundles two prices that the headline hides.** Almost every program quotes a
**care/program fee** ("Starting at $X/month") that is *separate* from **medication cost** ("Medication is not
included"). Weight Management is the sharpest case — the homepage hero says "Access FDA-approved Wegovy®,
starting at just $149‡", but the `‡` footnote reveals that number is *medication only* and excludes "the
monthly program & provider fee of $149 (first month discounted to $39 today)." So GLP-1 weight loss is
unambiguously **`partial`** (two stacked costs, neither self-contained), and Women's Health is `partial` for
the same reason ("plus the cost of your medication"). Mental Health and Urgent/Primary Care are
**`published`** — the program fee *includes* medication ("Medication is included in the cost of your monthly
membership"), so the shown floor is the real entry price. Cardiovascular Health is **`on-request`** — its page
shows **no price at all**, only "Insurance accepted*".

**Two things the family-grain profile collapsed, now surfaced per-SKU:**
- **Mental Health is a 9-SKU branded grid**, not a single line — Wellbutrin SR®, Lexapro®, Prozac®, Inderal®,
  Buspar®, Celexa®, Cymbalta®, Effexor®, Zoloft®, each card naming its molecule + dose + a real `/drugs/*` PDP.
- **Women's-Health estradiol cream is a compounded product** — the page states it "has not been FDA-approved or
  evaluated" (the others are FDA-approved). The one compounding flag in LifeMD's main-domain catalog.

**`/mental-health` is the homepage, not a program page.** The URL `/mental-health` renders identical content
to the homepage with "Explore Mental Health" CTAs pointing to `/psychiatry`. No price, no product grid, no
dedicated program page at that slug. The branded med grid and all program pricing live on `/psychiatry` — the
prior (which only had `/psychiatry`) was correct.

**Prominence (calibrated).**
- **Weight Management is the lead program [HIGH]** — it owns the homepage's only dollar hero ("Access FDA-approved
  Wegovy®, starting at just $149‡"), the widest SKU lineup (8 GLP-1/oral cards), its own "Money Back Guarantee,"
  and the first nav slot after LifeMD+. Within it, **Zepbound® Vial ($349/mo) and Wegovy® Pen ($199) are the
  badged hero SKUs [HIGH]** (named in the rotating hero banner).
- **Nav order = the program ranking [MED]:** LifeMD+ · Weight Management · Women's Health · Mental Health (top
  nav), with Cardiovascular + Urgent/Primary Care added in the Specialty Care mega-menu. The homepage "Specialty
  Care" grid repeats this order.
- **Weight-Mgmt card order within the grid [LOW]** — Wegovy Pill → Foundayo → Wegovy → Zepbound KwikPen → Zepbound
  Vial → Zepbound → Ozempic → Saxenda; the three "New"-badged cards (Wegovy Pill, Foundayo, Zepbound KwikPen) lead,
  but card order is a weak signal, not used for ranking.

## Roster

Complete **at the indexed level** — every priced program LifeMD nav-indexes, plus the named medication SKUs
rendered inside the three programs whose pages show a med-card grid. Care/program prices quoted verbatim from
`/membership` + each program page; medication prices from `/weight-management` + homepage `‡` footnote. Molecule
page-attested only (the Mental-Health molecules are attested in the card slug **and** product copy; see Verbatim
anchors). Every `/drugs/*` slug was HEAD-verified to resolve (200) on 2026-06-15. A slug here is never asserted
equal to another brand's. The 80+ `/treatment/<condition>` pages are **sub-indexed condition content, not priced
SKUs** (catalog breadth — see Provenance), so they are not rostered; ED/PE (→ rexmd.com) and Sleep (→
rx.lifemd.com/sleep-xp1) route off-domain and are noted, not rostered.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| **LifeMD+ Membership** | family | — | `/lifemd-plus` | `$19/month` | published | — · the front-door subscription; 24/7 urgent & primary care, video + message consults, lab-testing access. "No commitment. Cancel anytime." |
| Urgent & Primary Care | buyable | LifeMD+ Membership | `/membership` | care `Starting at $49 /visit` (cash) / `$19 + copay/visit` (insurance); video visit `$50 (cash)`; message consults `$20` | published | — · same-day refills + common conditions (colds, flu, rashes) via care.lifemd.com booking; self-contained per-visit/per-consult. |
| **Weight Management** | family | — | `/weight-management` | care `$39 for your first month, and just $149 a month thereafter`‡ (cash) / `$29` /month (insurance) | partial | GLP-1 + oral program; care/program fee is SEPARATE from medication ("Medication cost is not included"). Money-back guarantee. |
| Wegovy® Pill | buyable | Weight Management | `/drugs/w/wegovy` | `starting at $149 (pill)`‡ (med-only) | partial | semaglutide · daily tablet · "Insurance accepted"; badge "New". Med price excludes the $39→$149/mo program fee‡. |
| Wegovy® Pen | buyable | Weight Management | `/drugs/w/wegovy` | `Wegovy® Pen Starting At Just $199` / `$499`‡ (med-only); `As Low As $0 Copay … with insurance°` | partial | semaglutide · weekly injection · A/B-volatile $199↔$499; med-only, program fee on top. |
| Wegovy® | buyable | Weight Management | `/drugs/w/wegovy` | (no distinct med price on page; line floor `$149`/`$199`/`$499`‡) | partial | semaglutide · weekly injection · the brand entry card (distinct grid card from Pill/Pen); "Insurance accepted". |
| Foundayo™ | buyable | Weight Management | (no PDP — rx.lifemd.com/weight-management enroll) | (no med price on page) | on-request | orforglipron · daily tablet · "Insurance accepted"; badge "New". Oral GLP-1, no on-page price. |
| Zepbound® KwikPen® | buyable | Weight Management | (no PDP — rx.lifemd.com/weight-management enroll) | (no med price on page; brand `$0 copay` with insurance°) | on-request | tirzepatide · weekly injection · "Insurance accepted"; badge "New". |
| Zepbound® Vial | buyable | Weight Management | (no PDP — rx.lifemd.com/weight-management enroll) | `Zepbound® Vial Starting At $349/mo` | partial | tirzepatide · weekly injection · the badged hero SKU; med-only, program fee on top. |
| Zepbound® | buyable | Weight Management | `/drugs/z/zepbound` | (no distinct med price; brand `$0 copay`° / line `$349`) | partial | tirzepatide · weekly injection · brand entry card distinct from the $349 Vial; "Insurance accepted". |
| Ozempic® | buyable | Weight Management | `/drugs/o/ozempic` | (no med price on page; `$0 copay`° with insurance) | on-request | semaglutide · daily injection (card reads "Daily injection" — quoted verbatim) · "Insurance accepted"; off-label weight loss, FDA-approved T2D. |
| Saxenda® | buyable | Weight Management | `/drugs/s/saxenda` | (no med price on page) | on-request | liraglutide · daily injection · "Insurance accepted". |
| Triple Therapy | buyable | Weight Management | `/weight-management` | (included in program fee — `$39`/`$149`/mo) | published | metformin + bupropion + topiramate · oral medication pack · "Triple Therapy is included in the cost of the program"; for patients who don't meet GLP-1 BMI threshold. |
| **Women's Health** | family | — | `/womens-health` | care `starting at $79 per month, plus the cost of your medication` | partial | HRT for perimenopause/menopause; care fee separate from medication. |
| Estradiol Topical Cream | buyable | Women's Health | (no PDP — rx.lifemd.com/womens-health-insurance enroll) | (no med price; line `$79/mo` + med) | partial | estradiol · topical cream · **compounded, "has not been FDA-approved or evaluated"** (page ISI); reduces hot flashes/night sweats. |
| Estradiol Patch | buyable | Women's Health | (no PDP — rx.lifemd.com/womens-health-insurance enroll) | (no med price; line `$79/mo` + med) | partial | estradiol · transdermal patch · FDA-approved; steady estrogen delivery. |
| Estradiol Vaginal Insert | buyable | Women's Health | (no PDP — rx.lifemd.com/womens-health-insurance enroll) | (no med price; line `$79/mo` + med) | partial | estradiol · vaginal insert · FDA-approved; targeted vaginal comfort/health. |
| Micronized Progesterone | buyable | Women's Health | (no PDP — rx.lifemd.com/womens-health-insurance enroll) | (no med price; line `$79/mo` + med) | partial | micronized progesterone · oral capsule · supports hormone-plan balance. |
| **Mental Health / Psychiatry** | family | — | `/psychiatry` | care `Starting at $49 /month` (cash AND insurance) | published | Async/video psychiatry for anxiety/depression; **medication INCLUDED in the program fee**. Two plans: Social/Performance Anxiety (as-needed) + Anxiety & Depression (daily). No controlled substances. |
| Wellbutrin SR® | buyable | Mental Health / Psychiatry | `/drugs/b/bupropion` | (no per-drug price; program `$49/mo` incl. med) | published | bupropion SR · 150mg tablet · "Generic available". |
| Lexapro® | buyable | Mental Health / Psychiatry | `/drugs/e/escitalopram` | (no per-drug price; program `$49/mo` incl. med) | published | escitalopram · 10mg tablet · "Generic available". |
| Prozac® | buyable | Mental Health / Psychiatry | `/drugs/f/fluoxetine` | (no per-drug price; program `$49/mo` incl. med) | published | fluoxetine · 10mg–20mg capsule · "Generic available". |
| Inderal® | buyable | Mental Health / Psychiatry | `/drugs/p/propranolol` | (no per-drug price; program `$49/mo` incl. med) | published | propranolol · 40mg tablet · beta-blocker (performance anxiety); "Generic available". |
| Buspar® | buyable | Mental Health / Psychiatry | `/drugs/b/buspirone` | (no per-drug price; program `$49/mo` incl. med) | published | buspirone · 15mg tablet · "Generic available". |
| Celexa® | buyable | Mental Health / Psychiatry | `/drugs/c/citalopram` | (no per-drug price; program `$49/mo` incl. med) | published | citalopram · 20mg tablet · "Generic available". |
| Cymbalta® | buyable | Mental Health / Psychiatry | `/drugs/d/duloxetine` | (no per-drug price; program `$49/mo` incl. med) | published | duloxetine · 30mg capsule · "Generic available". |
| Effexor® | buyable | Mental Health / Psychiatry | `/drugs/v/venlafaxine` | (no per-drug price; program `$49/mo` incl. med) | published | venlafaxine · 37.5mg–75mg tablet · "Generic available". |
| Zoloft® | buyable | Mental Health / Psychiatry | `/drugs/s/sertraline` | (no per-drug price; program `$49/mo` incl. med) | published | sertraline · 50mg–100mg tablet · "Generic available". |
| **Cardiovascular Health** | family | — | `/cardiovascular-health` | (no price shown — `Insurance accepted*`) | on-request | "Virtual Heart Care" — board-certified cardiologists managing blood pressure, cholesterol, long-term risk; enroll via rx.lifemd.com/cardiology. |
| **Labs** | family | — | `/membership` | (program-ordered labs `at no cost` at Quest/Labcorp; else insurance/self-pay) | on-request | At-home / lab-network panels: Diabetes, Heart Health, Cholesterol, Thyroid Function, Female/Male Hormone, Inflammation. No standalone /labs page or per-panel price; enroll via rx.lifemd.com/plus. Excl. NY/NJ/RI by state rule. |

### Verbatim anchors

The footnotes the Price column points at — what decides `partial`/`published`/`on-request`, plus the molecule
audit. Quoted exactly from the captured pages.

- **‡ (the load-bearing weight-loss footnote, `homepage` 2026-06-15):** *"Initial Wegovy® pricing starting at
  $149 (pill) and $199 (pen) is for new patients eligible for prescription without insurance coverage. Price does
  not include the monthly program & provider fee of $149 (first month discounted to $39 today). If using insurance,
  eligible and qualified patients may pay as low as $0-$25 co-pay for medication."* → the GLP-1 number is
  **medication only**; the all-in stacks the $39→$149/mo program fee on top, hence **`partial`** for the priced
  GLP-1 SKUs. **Δ from 2026-06-04:** prior footnote said "$75 today" — fresh homepage ‡ says **$39 today**. The
  `wegovy.md` PDP footnote on the same 2026-06-15 run still says "$75 today" — unreconciled A/B pricing across
  pages, both recorded.
- **‡ (wegovy PDP variant, `wegovy.md` 2026-06-15):** *"Initial Wegovy® pricing starting at $199 is for new
  patients eligible for prescription without insurance coverage. Price does not include the program & provider fee
  of $149 (discounted to $75 today). If using insurance, eligible and qualified patients may pay as low as $0
  co-pay for medication."* → contradicts the homepage footnote on the first-month discount ($75 vs $39).
- **° (copay, `homepage` / `weight_management`):** *"Copay for initial supply of medication may be as low as $0
  for commercially insured patients depending on coverage. Prescription required. Not all insurance plans
  accepted."* The `$0` is an insurance-conditional copay, not a self-pay price.
- **Weight-Mgmt program fee (`weight_management`):** *"Our program starts as low as $39 for your first month,
  and just $149 a month thereafter with the flexibility to cancel anytime. … Medication cost is not included and
  varies based on insurance coverage or self-pay options."* And on `/membership`: Weight Management *"Care
  Starting at $75 /month"* (cash, ongoing floor) / *"$29 /month"* (insurance), with *"Medication cost starting
  at $149/month"* / *"as low as $0/month"*. Note: the `$75` on `/membership` is the ongoing program floor (no
  discount), consistent with `$39` first month then `$149`.
- **A/B-volatile Wegovy Pen (`weight_management`):** the rotating hero banner shows *"Wegovy® Pen Starting At
  Just $199"* and *"Wegovy® Pen Starting At Just $499"* on the **same captured page** — a point-in-time A/B
  flicker; both quoted, unreconciled (the higher is likely the without-insurance number per the `‡` note).
- **Triple Therapy is included (`membership` / `weight_management`):** *"Triple Therapy is included in the cost
  of the program. Medication costs for GLP-1 medications are not included unless stated at the time of purchase."*
  and *"Triple Therapy is a doctor-trusted treatment plan that consists of three medications (Metformin, Bupropion,
  and Topiramate)…"* → its cost rides the program fee, so **`published`**.
- **Women's-Health program fee + the compounding flag (`womens_health`):** *"The program includes monthly provider
  consultations, a personalized treatment plan, secure messaging, and prescription management — starting at $79
  per month, plus the cost of your medication. Medication cost may vary based on prescribed treatment and is not
  included in this program."* → care fee + separate medication = **`partial`**. The compounding flag: *"**Estradiol
  cream**, Rx only, is a **compounded product and has not been FDA-approved or evaluated** for safety, efficacy, or
  quality but may be used to treat menopausal symptoms"* — the other three (patch, vaginal insert, progesterone)
  carry standard FDA-approved-drug ISI, not the compounded disclaimer.
- **Mental-Health is `published` (medication included) (`lifemd_plus` FAQ / `membership`):** *"Medication is
  included in the cost of your monthly membership"* (stated for both the as-needed and daily plans). The floor is
  *"Mental Health … Starting at $49 /month"* on `/membership` — **identical with and without insurance** — and the
  `/psychiatry` page's own "Clear pricing" section shows no separate med charge. So the $49/mo is the real,
  self-contained entry price.
- **Cardiovascular is `on-request` (`cardiovascular_health`):** the page shows **no dollar figure anywhere** — only
  *"Insurance accepted*"*, *"Insurance and cash pay options"*, and a *"Book your virtual visit"* CTA to
  `rx.lifemd.com/cardiology/`. No price is shown until enrollment.
- **Urgent/Primary Care figures (`lifemd_plus` FAQ):** *"Membership is $19/month with access to video visits ($50
  cash or your copay). Labs can be covered by insurance; message consults are $20."* All self-contained →
  **`published`**.
- **Molecule sourcing (page-attested-only, audited):**
  - **Weight Management** — molecules are attested on each grid card's subhead: Wegovy® Pill / Wegovy® →
    *"Semaglutide"*; Foundayo™ → *"ORFORGLIPRON"*; Zepbound® KwikPen® / Zepbound® Vial / Zepbound® →
    *"Tirzepatide"*; Ozempic® → *"Semaglutide"*; Saxenda® → *"Liraglutide"*. (Ozempic's card reads *"Daily
    injection"* — quoted as shown though semaglutide is weekly; recorded verbatim, not corrected.) Triple Therapy
    → *"Metformin, Bupropion, and Topiramate"* (FAQ).
  - **Mental Health** — molecule is attested **both** in the slug and in product copy: the hero cards show
    *"Wellbutrin SR® / Bupropion SR"*, *"Lexapro® / Escitalopram"*, etc., and every card's "Get Started" link
    points to `/drugs/<letter>/<molecule>` (bupropion, escitalopram, fluoxetine, propranolol, buspirone,
    citalopram, duloxetine, venlafaxine, sertraline) — all HEAD-verified to resolve on 2026-06-15.
  - **Women's Health** — *"estradiol"* (cream/patch/vaginal insert) and *"micronized progesterone"* attested on
    the treatment-option cards + FAQ (*"Medications that may be considered are estradiol (patch, insert, or gel),
    micronized progesterone, and thyroid replacement if necessary"*). Thyroid replacement mentioned as a possible
    add-on but has **no card** — not rostered.

## Deep blocks

**One earned** — the Weight-Management GLP-1 pricing trap, where the roster cell alone can't carry the
disambiguation. The Mental-Health grid is fully legible from the roster (uniform `$49/mo`-incl-med `published`
SKUs), and Cardiovascular/Labs are simple `on-request` lines — none earn a block.

### Weight Management — the two-price GLP-1 trap (`/weight-management`)

- **Parent:** none (top-level program) · **care price:** `$39` first mo → `$149/mo` (cash) / `$29/mo` (insurance) ·
  **med price:** Zepbound Vial `$349/mo`, Wegovy Pen `$199`/`$499`‡ · **visibility:** `partial`

Why it earns a block: the single most misattributable number in LifeMD's catalog is the homepage hero **"Access
FDA-approved Wegovy®, starting at just $149‡"**. Read alone it looks like an all-in price. The `‡` footnote (quoted
in full under Verbatim anchors) reveals it is **medication only**, and that a **separate** "$149/mo program &
provider fee (first month discounted to $39 today)" stacks on top — so the real entry cost for cash-pay GLP-1 is
roughly *medication $149–$349 **+** program $39→$149/mo*, two independently-quoted numbers neither of which is the
whole. This is exactly the cross-brand-comparison trap the module exists to defuse: a price consumer rolling up
"cheapest compounded/branded semaglutide" must not treat LifeMD's `$149` as comparable to a competitor's all-in.
The page also runs an **A/B flicker** on the med number (Wegovy Pen `$199` ↔ `$499` in the same capture) and a
**cross-page A/B on the first-month discount** (homepage ‡: `$39 today`; wegovy PDP: `$75 today`) — both reasons
to treat any single figure as point-in-time. Note the compounding-posture read for the telehealth pack: LifeMD's
**GLP-1s are all branded** (Wegovy®, Zepbound®, Ozempic®, Saxenda® — no compounded semaglutide/tirzepatide SKU on
the main domain); the **one** compounded product in the catalog is Women's-Health **estradiol cream**, not a
weight-loss drug.

## Provenance

- **Sources reconciled (fresh 2026-06-15 captures):**
  - **Fresh this run (`captures/2026-06-15/`):** homepage, `/membership`, `/lifemd-plus`, `/weight-management`,
    `/womens-health`, `/cardiovascular-health`, `/psychiatry`, `/mental-health`, `/treatment`, `/how-it-works`,
    `/about`, `/medical-team`, and the `/drugs/w/wegovy` PDP (as `wegovy.md`). These carry the program structure,
    the care-fee floors, the WM med-card grid + prices, the WH HRT cards, the MH 9-SKU grid, and the homepage `‡`
    footnote.
  - **Census / blind-source reconciliation:** nav links + program-page census converge on the same ~6 priced
    program pages (`/lifemd-plus`, `/weight-management`, `/womens-health`, `/psychiatry`, `/cardiovascular-health`,
    `/membership`) — licenses "complete at the indexed level (program)." No enrollment-app pages (rx.lifemd.com)
    captured — the walled funnel is noted, not rostered.
  - **Slug verification:** all 13 rostered `/drugs/*` PDP slugs (4 WM + 9 Mental-Health) HEAD-checked → 200 on
    2026-06-15. The no-PDP cards (Foundayo, Zepbound KwikPen/Vial, the 4 HRT meds) note `(no PDP — …)`; no slug
    was constructed.
- **`/mental-health` vs `/psychiatry` reconciliation (new finding this run):** The prior (2026-06-04) only had
  `/psychiatry`. This run captured both. `/mental-health` renders the homepage content verbatim — same program
  overview, same "Explore Mental Health" link to `/psychiatry`, same footer. It carries no dedicated med grid and
  no program price; it is not a distinct program page. The branded 9-SKU grid and all MH pricing live exclusively
  on `/psychiatry`. **Resolution: `/psychiatry` is the canonical program slug; `/mental-health` is noted here as
  the homepage-at-another-URL and is not rostered separately.**
- **Scope — enumerated vs noted-not-enumerated:**
  - **Enumerated:** 6 program families + 24 buyable rows (8 WM cards + Triple Therapy + Urgent/Primary Care, 4 WH
    HRT meds, 9 Mental-Health meds) = **30 rows** (unchanged from prior).
  - **Noted, not rostered:** the **80+ `/treatment/<condition>` pages** — sub-indexed *condition* content (acne,
    UTI, GERD, hypertension, type-2 diabetes…), treated through the membership, **not** separately-priced SKUs.
    The **7 lab panels** roll up to one Labs row (no standalone page or per-panel price). **Thyroid replacement**
    (WH) — mentioned in FAQ, no card. **Sleep/Insomnia** → routes to `rx.lifemd.com/sleep-xp1` (off-domain funnel).
    **ED + Premature Ejaculation** → route to **rexmd.com** (sibling brand), out of scope for this slug.
    **Paxil® (paroxetine)** — appears in homepage "Most Popular" Mental Health carousel linking to `/psychiatry`,
    but is **not on the `/psychiatry` product grid** (which remains the same 9 SKUs). Not rostered.
    **Mounjaro®** — appears only in the WM ISI/legal section as a tirzepatide comparator, not as a product card.
    Not rostered. **Estradiol Topical Gel / Vaginal Ring** — appear in the homepage Women's Health carousel, but
    are **not on the `/womens-health` product grid** (which shows only 4 SKUs). Not rostered.
- **Gated / unreachable (a finding, not a skip):** every med's actual cash price and the program all-in (care fee
  + dose-titrated medication) live **behind the rx.lifemd.com quiz/enrollment** — shown as the floor that *is*
  public + `[partial]`/`[on-request]`. Cardiovascular shows no price pre-enrollment. The `$0 copay` figures are
  insurance-conditional, not self-pay prices.
- **A/B-volatile prices this run:** (1) Wegovy Pen `$199` ↔ `$499` in the same weight_management.md capture.
  (2) First-month program fee discount: homepage ‡ says `$39 today`; wegovy PDP says `$75 today` — same capture
  date, two different pages, two different numbers. Both recorded verbatim; the lower ($39) is the homepage hero
  value.
- **Point-in-time snapshot:** LifeMD runs A/B pricing and the site loads PostHog (analytics + surveys) — captured
  pricing/IA is a snapshot. This module's own `captured_at` + a short TTL are the guard; re-capture before
  trusting a price as current.
- **### Run profile:** refresh run against 2026-06-15 fresh captures. Prior baseline: 2026-06-04. Key change: ‡
  footnote first-month discount updated from `$75 today` (prior) to `$39 today` (homepage) — but the wegovy PDP
  still shows `$75 today` on the same date. `/mental-health` page captured for the first time; determined to be
  homepage-at-another-URL, not a distinct program page (full reconciliation in Provenance). No new SKUs added or
  removed. Hero-image capture **skipped** (default). No PDP-anatomy block.
