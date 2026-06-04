---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: lifemd.com          # company key; each offering's slug (its relative url) is its key *within* lifemd
captured_at: 2026-06-04     # own freshness; captures/2026-06-04/ (+ reused 2026-06-02/) hold the source pages
site_notes: "Catalog is PROGRAMS, not product PDPs — lifemd.com sells care programs; commerce is a walled funnel on care.lifemd.com (booking) + rx.lifemd.com (enrollment), no public CMS/products.json. Backbone = nav links + /map census + site:lifemd.com map passes (all converge on ~6 priced program pages; /map is /learn-blog + /drugs-index dominated — filter both). Named med SKUs live only INSIDE the Weight-Mgmt + Mental-Health + Women's-Health program pages; each med card links to a real lifemd.com/drugs/<letter>/<molecule> PDP (molecule is IN the slug). Prices are split: care/program fee on /membership + each program page; medication priced separately and A/B-volatile (Wegovy Pen 'from $199' ↔ 'from $499' on one page) — re-check next run. No standalone /labs page; the 7 lab panels enroll via rx.lifemd.com/plus. ED/PE + Sleep route OFF-domain (rexmd.com, rx.lifemd.com/sleep-xp1) — not LifeMD's own funnel."
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
included"). Weight Management is the sharpest case — the homepage hero says "Wegovy® … starting at just $149‡",
but the `‡` footnote reveals that number is *medication only* and excludes "the monthly program & provider fee
of $149 (first month discounted to $75 today)." So GLP-1 weight loss is unambiguously **`partial`** (two stacked
costs, neither self-contained), and Women's Health is `partial` for the same reason ("plus the cost of your
medication"). Mental Health and Urgent/Primary Care are **`published`** — the program fee *includes* medication
("Medication is included in the cost of your monthly membership"), so the shown floor is the real entry price.
Cardiovascular Health is **`on-request`** — its page shows **no price at all**, only "Insurance accepted*".

**Two things the family-grain profile collapsed, now surfaced per-SKU:**
- **Mental Health is a 9-SKU branded grid**, not a single line — Wellbutrin SR®, Lexapro®, Prozac®, Inderal®,
  Buspar®, Celexa®, Cymbalta®, Effexor®, Zoloft®, each card naming its molecule + dose + a real `/drugs/*` PDP.
- **Women's-Health estradiol cream is a compounded product** — the page states it "has not been FDA-approved or
  evaluated" (the others are FDA-approved). The one compounding flag in LifeMD's main-domain catalog.

**Prominence (calibrated).**
- **Weight Management is the lead program [HIGH]** — it owns the homepage's only dollar hero ("Access FDA-approved
  Wegovy®, starting at just $149‡"), the widest SKU lineup (8 GLP-1/oral cards), its own "Money Back Guarantee,"
  and the first nav slot after LifeMD+. Within it, **Zepbound® Vial ($349/mo) and Wegovy® Pen ($199) are the
  badged hero SKUs [HIGH]** (named in the rotating hero banner).
- **Nav order = the program ranking [MED]:** LifeMD+ · Weight Management · Women's Health · Mental Health (top
  nav), with Cardiovascular + Urgent/Primary Care added in the Specialty Care mega-menu. The homepage "Specialty
  Care" grid repeats this order.
- **Weight-Mgmt card order within the grid [LOW]** — Wegovy Pill → Foundayo → Wegovy → Zepbound KwikPen → Zepbound
  Vial → Zepbound → Ozempic → Saxenda; the four "New"-badged cards (Wegovy Pill, Foundayo, Zepbound KwikPen) lead,
  but card order is a weak signal, not used for ranking.

## Roster

Complete **at the indexed level** — every priced program LifeMD nav-indexes, plus the named medication SKUs
rendered inside the three programs whose pages show a med-card grid. Care/program prices quoted verbatim from
`/membership` + each program page; medication prices from `/weight-management` + homepage `‡` footnote. Molecule
page-attested only (the Mental-Health molecules are attested in the card slug **and** product copy; see Verbatim
anchors). Every `/drugs/*` slug was HEAD-verified to resolve (200). A slug here is never asserted equal to another
brand's. The 80+ `/treatment/<condition>` pages are **sub-indexed condition content, not priced SKUs** (catalog
breadth — see Provenance), so they are not rostered; ED/PE (→ rexmd.com) and Sleep (→ rx.lifemd.com/sleep-xp1)
route off-domain and are noted, not rostered.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| **LifeMD+ Membership** | family | — | `/lifemd-plus` | `$19/month` | published | — · the front-door subscription; 24/7 urgent & primary care, video + message consults, lab-testing access. "No commitment. Cancel anytime." |
| Urgent & Primary Care | buyable | LifeMD+ Membership | `/membership` | care `Starting at $49 /visit` (cash) / `$19 + copay/visit` (insurance); video visit `$50 (cash)`; message consults `$20` | published | — · same-day refills + common conditions (colds, flu, rashes) via care.lifemd.com booking; self-contained per-visit/per-consult. |
| **Weight Management** | family | — | `/weight-management` | care `as low as $75 for your first month, and just $149 a month thereafter` (cash) / `$29` /month (insurance) | partial | GLP-1 + oral program; care/program fee is SEPARATE from medication ("Medication cost is not included"). Money-back guarantee. |
| Wegovy® Pill | buyable | Weight Management | `/drugs/w/wegovy` | `starting at $149 (pill)`‡ (med-only) | partial | semaglutide · daily tablet · "Insurance accepted"; badge "New". Med price excludes the $75→$149/mo program fee. |
| Wegovy® Pen | buyable | Weight Management | `/drugs/w/wegovy` | `Wegovy® Pen Starting At Just $199` / `$499`‡ (med-only); `As Low As $0 Copay … with insurance°` | partial | semaglutide · weekly injection · A/B-volatile $199↔$499; med-only, program fee on top. |
| Wegovy® | buyable | Weight Management | `/drugs/w/wegovy` | (no distinct med price on page; line floor `$199`/`$499`‡) | partial | semaglutide · weekly injection · the brand entry card (distinct grid card from Pill/Pen); "Insurance accepted". |
| Foundayo™ | buyable | Weight Management | (no PDP — rx.lifemd.com/wc-primary enroll) | (no med price on page) | on-request | orforglipron · daily tablet · "Insurance accepted"; badge "New". Oral GLP-1, no on-page price. |
| Zepbound® KwikPen® | buyable | Weight Management | (no PDP — rx.lifemd.com/wc-primary enroll) | (no med price on page; brand `$0 copay` with insurance°) | on-request | tirzepatide · weekly injection · "Insurance accepted"; badge "New". |
| Zepbound® Vial | buyable | Weight Management | (no PDP — rx.lifemd.com/wc-primary enroll) | `Zepbound® Vial Starting At $349/mo` | partial | tirzepatide · weekly injection · the badged hero SKU; med-only, program fee on top. |
| Zepbound® | buyable | Weight Management | `/drugs/z/zepbound` | (no distinct med price; brand `$0 copay`° / line `$349`) | partial | tirzepatide · weekly injection · brand entry card distinct from the $349 Vial; "Insurance accepted". |
| Ozempic® | buyable | Weight Management | `/drugs/o/ozempic` | (no med price on page; `$0 copay`° with insurance) | on-request | semaglutide · injection (card says "Daily injection") · "Insurance accepted"; off-label weight loss, FDA-approved T2D. |
| Saxenda® | buyable | Weight Management | `/drugs/s/saxenda` | (no med price on page) | on-request | liraglutide · daily injection · "Insurance accepted". |
| Triple Therapy | buyable | Weight Management | `/weight-management` | (included in program fee — `$75`/`$149`/mo) | published | metformin + bupropion + topiramate · oral medication pack · "included in the cost of the program"; for patients who don't meet GLP-1 BMI threshold. |
| **Women's Health** | family | — | `/womens-health` | care `starting at $79 per month, plus the cost of your medication` | partial | HRT for perimenopause/menopause; care fee separate from medication. Includes a LifeMD+ membership + 6S Lifestyle Program. |
| Estradiol Topical Cream | buyable | Women's Health | (no PDP — rx.lifemd.com/womens-health enroll) | (no med price; line `$79/mo` + med) | partial | estradiol · topical cream · **compounded, "has not been FDA-approved or evaluated"** (page ISI); reduces hot flashes/night sweats. |
| Estradiol Patch | buyable | Women's Health | (no PDP — rx.lifemd.com/womens-health enroll) | (no med price; line `$79/mo` + med) | partial | estradiol · transdermal patch · FDA-approved; steady estrogen delivery. |
| Estradiol Vaginal Insert | buyable | Women's Health | (no PDP — rx.lifemd.com/womens-health enroll) | (no med price; line `$79/mo` + med) | partial | estradiol · vaginal insert · FDA-approved; targeted vaginal comfort/health. |
| Micronized Progesterone | buyable | Women's Health | (no PDP — rx.lifemd.com/womens-health enroll) | (no med price; line `$79/mo` + med) | partial | micronized progesterone · oral capsule · supports hormone-plan balance. |
| **Mental Health / Psychiatry** | family | — | `/psychiatry` | care `Starting at $49 /month` (cash AND insurance) | published | Async/video psychiatry for anxiety/depression; **medication INCLUDED in the program fee**. Two plans: Social/Performance Anxiety (as-needed) + Anxiety & Depression (daily). No controlled substances. |
| Wellbutrin SR® | buyable | Mental Health / Psychiatry | `/drugs/b/bupropion` | (no per-drug price; program `$49/mo` incl. med) | published | bupropion SR · 150mg tablet · "Generic available". |
| Lexapro® | buyable | Mental Health / Psychiatry | `/drugs/e/escitalopram` | (no per-drug price; program `$49/mo` incl. med) | published | escitalopram · 10mg tablet · "Generic available". |
| Prozac® | buyable | Mental Health / Psychiatry | `/drugs/f/fluoxetine` | (no per-drug price; program `$49/mo` incl. med) | published | fluoxetine · 10–20mg capsule · "Generic available". |
| Inderal® | buyable | Mental Health / Psychiatry | `/drugs/p/propranolol` | (no per-drug price; program `$49/mo` incl. med) | published | propranolol · 40mg tablet · beta-blocker (performance anxiety); "Generic available". |
| Buspar® | buyable | Mental Health / Psychiatry | `/drugs/b/buspirone` | (no per-drug price; program `$49/mo` incl. med) | published | buspirone · 15mg tablet · "Generic available". |
| Celexa® | buyable | Mental Health / Psychiatry | `/drugs/c/citalopram` | (no per-drug price; program `$49/mo` incl. med) | published | citalopram · 20mg tablet · "Generic available". |
| Cymbalta® | buyable | Mental Health / Psychiatry | `/drugs/d/duloxetine` | (no per-drug price; program `$49/mo` incl. med) | published | duloxetine · 30mg capsule · "Generic available". |
| Effexor® | buyable | Mental Health / Psychiatry | `/drugs/v/venlafaxine` | (no per-drug price; program `$49/mo` incl. med) | published | venlafaxine · 37.5–75mg tablet · "Generic available". |
| Zoloft® | buyable | Mental Health / Psychiatry | `/drugs/s/sertraline` | (no per-drug price; program `$49/mo` incl. med) | published | sertraline · 50–100mg tablet · "Generic available". |
| **Cardiovascular Health** | family | — | `/cardiovascular-health` | (no price shown — `Insurance accepted*`) | on-request | "Virtual Heart Care" — board-certified cardiologists managing blood pressure, cholesterol, long-term risk; enroll via rx.lifemd.com/cardiology. |
| **Labs** | family | — | `/membership` | (program-ordered labs `at no cost` at Quest/Labcorp; else insurance/self-pay) | on-request | At-home / lab-network panels: Diabetes, Heart Health, Cholesterol, Thyroid Function, Female/Male Hormone, Inflammation. No standalone /labs page or per-panel price; enroll via rx.lifemd.com/plus. Excl. NY/NJ/RI by state rule. |

### Verbatim anchors

The footnotes the Price column points at — what decides `partial`/`published`/`on-request`, plus the molecule
audit. Quoted exactly from the captured pages.

- **‡ (the load-bearing weight-loss footnote, `homepage`):** *"Initial Wegovy® pricing starting at $149 (pill)
  and $199 (pen) is for new patients eligible for prescription without insurance coverage. Price does not include
  the monthly program & provider fee of $149 (first month discounted to $75 today). If using insurance, eligible
  and qualified patients may pay as low as $0-$25 co-pay for medication."* → the GLP-1 number is **medication
  only**; the all-in stacks the $75→$149/mo program fee on top, hence **`partial`** for the priced GLP-1 SKUs.
- **° (copay, `homepage` / `weight_management`):** *"Copay for initial supply of medication may be as low as $0
  for commercially insured patients depending on coverage. Prescription required. Not all insurance plans
  accepted."* The `$0` is an insurance-conditional copay, not a self-pay price.
- **Weight-Mgmt program fee (`weight_management`):** *"Our program starts as low as $75 for your first month, and
  just $149 a month thereafter… Medication cost is not included and varies based on insurance coverage or self-pay
  options."* And on `/membership`: Weight Management *"Care Starting at $75 /month"* (cash) / *"$29 /month"*
  (insurance), with *"Medication cost starting at $149/month"* / *"as low as $0/month"*.
- **A/B-volatile Wegovy Pen (`weight_management`):** the rotating hero banner shows *"Wegovy® Pen Starting At Just
  $199"* and *"Wegovy® Pen Starting At Just $499"* on the **same captured page** — a point-in-time A/B flicker;
  both quoted, unreconciled (the higher is likely the without-insurance number per the `‡` note).
- **Triple Therapy is included (`membership` / `weight_management`):** *"Triple Therapy is included in the cost of
  the program. Medication costs for GLP-1 medications are not included unless stated at the time of purchase."* and
  *"Triple Therapy is a doctor-trusted treatment plan that consists of three medications (Metformin, Bupropion,
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
    *"Semaglutide"*; Foundayo™ → *"ORFORGLIPRON"*; Zepbound® KwikPen® / Zepbound® Vial / Zepbound® → *"Tirzepatide"*;
    Ozempic® → *"Semaglutide"*; Saxenda® → *"Liraglutide"*. (Ozempic's card reads *"Daily injection"* — quoted as
    shown though semaglutide is weekly; recorded verbatim, not corrected.) Triple Therapy → *"Metformin, Bupropion,
    and Topiramate"* (FAQ).
  - **Mental Health** — molecule is attested **both** in the slug and in product copy: the hero cards show
    *"Escitalopram / Lexapro®"* and *"Wellbutrin SR® / Bupropion SR"*, and every card's "Get Started" link points
    to `/drugs/<letter>/<molecule>` (bupropion, escitalopram, fluoxetine, propranolol, buspirone, citalopram,
    duloxetine, venlafaxine, sertraline) — all HEAD-verified to resolve.
  - **Women's Health** — *"estradiol"* (cream/patch/vaginal insert) and *"micronized progesterone"* attested on the
    treatment-option cards + FAQ (*"Medications that may be considered are estradiol… micronized progesterone, and
    thyroid replacement if necessary"*). Thyroid replacement is mentioned as a possible add-on but has **no card** —
    not rostered.

## Deep blocks

**One earned** — the Weight-Management GLP-1 pricing trap, where the roster cell alone can't carry the disambiguation.
The Mental-Health grid is fully legible from the roster (uniform `$49/mo`-incl-med `published` SKUs), and
Cardiovascular/Labs are simple `on-request` lines — none earn a block.

### Weight Management — the two-price GLP-1 trap (`/weight-management`)

- **Parent:** none (top-level program) · **care price:** `$75` first mo → `$149/mo` (cash) / `$29/mo` (insurance) ·
  **med price:** Zepbound Vial `$349/mo`, Wegovy Pen `$199`/`$499`‡ · **visibility:** `partial`

Why it earns a block: the single most misattributable number in LifeMD's catalog is the homepage hero **"Access
FDA-approved Wegovy®, starting at just $149‡"**. Read alone it looks like an all-in price. The `‡` footnote (quoted
in full under Verbatim anchors) reveals it is **medication only**, and that a **separate** "$149/mo program &
provider fee (first month discounted to $75 today)" stacks on top — so the real entry cost for cash-pay GLP-1 is
roughly *medication $149–$349 **+** program $75→$149/mo*, two independently-quoted numbers neither of which is the
whole. This is exactly the cross-brand-comparison trap the module exists to defuse: a price consumer rolling up
"cheapest compounded/branded semaglutide" must not treat LifeMD's `$149` as comparable to a competitor's all-in.
The page also runs an **A/B flicker** on the med number (Wegovy Pen `$199` ↔ `$499` in the same capture) and leans
entirely on insurance-conditional `$0 copay°` language — both reasons to treat any single figure as point-in-time.
Note the compounding-posture read for the telehealth pack: LifeMD's **GLP-1s are all branded** (Wegovy®, Zepbound®,
Ozempic®, Saxenda® — no compounded semaglutide/tirzepatide SKU on the main domain); the **one** compounded product
in the catalog is Women's-Health **estradiol cream**, not a weight-loss drug.

## Provenance

- **Sources reconciled (programs backbone + 2 gap scrapes):**
  - **Reused from `captures/2026-06-02/` (no re-scrape, 0 credits):** homepage, `/membership`, `/lifemd-plus`,
    `/weight-management`, `/womens-health`, `/treatment`, `/how-it-works`, `/about` — these carry the program
    structure, the care-fee floors, the WM med-card grid + prices, the WH HRT cards, and the homepage `‡` footnote.
    (Verified md5-unique in the 2026-06-02 profile run.)
  - **Fresh this run (`captures/2026-06-04/`, 2 scrapes `--homepage`):** `/cardiovascular-health` (confirmed the
    profile's flagged-unverified price: genuinely **no price shown**) and `/psychiatry` (surfaced the **9-SKU
    branded med grid** the profile collapsed to one line). Both 200, md5-unique, screenshots saved.
  - **Census / blind-source reconciliation:** `fc.py map` no-search (65 URLs, `/learn`-blog + `/drugs`-index
    dominated) + 2 `site:lifemd.com` map passes (labs; psychiatry/mental-health). **All three converge on the same
    ~6 priced program pages** (`/lifemd-plus`, `/weight-management`, `/womens-health`, `/psychiatry`,
    `/cardiovascular-health`, `/membership`) — agreement that licenses "complete at the indexed level (program)."
    Nav links (profile) + census + `site:` are the three sources; on this walled funnel they don't see the
    enrollment app, so completeness is asserted for **lifemd.com programs**, not for SKUs gated inside rx.lifemd.com.
  - **Slug verification:** all 13 rostered `/drugs/*` PDP slugs (4 WM + 9 Mental-Health) HEAD-checked → 200. The
    no-PDP cards (Foundayo, Zepbound KwikPen/Vial, the 4 HRT meds) note `(no PDP — …)`; no slug was constructed.
- **Scope — enumerated vs noted-not-enumerated:**
  - **Enumerated:** 6 program families + 24 buyable rows (8 WM cards + Triple Therapy + Urgent/Primary Care, 4 WH
    HRT meds, 9 Mental-Health meds) = **30 rows**.
  - **Noted, not rostered:** the **80+ `/treatment/<condition>` pages** — these are sub-indexed *condition* content
    (acne, UTI, GERD, hypertension, type-2 diabetes…), treated through the membership, **not** separately-priced
    SKUs (profile already captured them as "catalog breadth"). The **7 lab panels** roll up to one Labs row (no
    standalone page or per-panel price). **Thyroid replacement** (WH) — mentioned, no card. **Sleep/Insomnia** →
    routes to `rx.lifemd.com/sleep-xp1` (off-domain funnel, no lifemd.com page or price). **ED + Premature
    Ejaculation** → route to **rexmd.com** (sibling brand), not LifeMD's own funnel — out of scope for this slug.
- **Gated / unreachable (a finding, not a skip):** every med's actual cash price and the program all-in (care fee +
  dose-titrated medication) live **behind the rx.lifemd.com quiz/enrollment** — shown as the floor that *is* public
  + `[partial]`/`[on-request]`. Cardiovascular shows no price pre-enrollment. The `$0 copay` figures are
  insurance-conditional, not self-pay prices.
- **Credit spend:** `fc.py spend` (2026-06-04) = **5 credits** — 1 census map + 2 `site:` map passes + 2 scrapes
  (cardiovascular_health, psychiatry). The 8 backbone pages were reused at 0 credits.
- **Point-in-time snapshot, not fixed:** LifeMD runs A/B pricing (Wegovy Pen `$199`↔`$499` in one capture) and the
  site loads PostHog (analytics + session replay + **surveys**) — captured pricing/IA is a snapshot. This module's
  own `captured_at` + a short TTL are the guard; re-capture before trusting a price as current.
- **### Run profile:** vanilla per-SKU offerings capture with one deviation worth naming — the catalog's indexed
  level is **programs**, not product PDPs (a walled-funnel telehealth shape), so med SKUs are nested *under*
  programs and most carry a care-fee floor rather than an own med price. Hero-image capture **skipped** (default).
  No PDP-anatomy block (programs share no repeated PDP shell — the PDPs are off-domain). 2 new scrapes; 8 reused.
