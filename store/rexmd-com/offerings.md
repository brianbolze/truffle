---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: rexmd.com           # company key; each offering's slug (its relative url) is its key *within* Rex MD
captured_at: 2026-06-04     # own freshness; captures/2026-06-04/ holds the source pages
site_notes: "Per-SKU prices for ED/hair/sleep/PE/herpes live on the master /our-medications/ index grid (dose+price cards) AND as 'From $X per use' floors on category pages — cheapest backbone is /our-medications (one rich scrape carries the whole grid). TRT + WM are NOT per-SKU priced — they're bundled PROGRAMS ($99 one-time + from $250/mo; $75) and individual SKU costs are set after consult/labs. GLP-1 meds are FDA-brand routed to manufacturer cash-pay (Wegovy→NovoCare $499; Zepbound→Eli Lilly $349) — Rex no longer compounds semaglutide (shortage exemption ended). Pricing is promo-driven: a sitewide 'up to 95% off ED / $2 per tablet' banner pins the ED floor — re-check next run. Anxiety/beta-blocker line is on rx.rexmd.com (not captured)."
---

## Portfolio overview

Rex MD is **Multi-product** — **eight condition lines** at SKU grain: erectile dysfunction, premature
ejaculation, weight management (GLP-1), the testosterone program, hair loss, sleep/insomnia, herpes, and
anxiety. Two pricing patterns split the roster:

1. **Self-contained per-med subscriptions** (`published`) — ED, hair, sleep, PE, herpes price each SKU directly
   on the `/our-medications/` grid with a verbatim floor ("From $6 per use", "$27 per month"). The displayed
   number is the full cash-pay price; the consult and free follow-ups are bundled in.
2. **Bundled programs** (`partial` / `on-request`) — **testosterone** ($99 one-time lab+consult, then "as low
   as $250 per month") and **weight management** ($75 program) price the *program*, not the molecule. The
   individual SKUs inside them are `on-request` (set after consult/labs), and the GLP-1 meds are bought through
   a **manufacturer** channel (NovoCare/Eli Lilly), so the all-in stacks the $75 program on top of the drug.

**Shape finding:** Rex's GLP-1 line is now **FDA-brand only** — it states plainly that the compounded-semaglutide
shortage exemption has ended ("pharmacies can no longer compound semaglutide"), so weight loss routes to Wegovy®
/ Zepbound® / Saxenda® at manufacturer cash-pay. Compounding survives elsewhere as **sermorelin** (a compounded
peptide) inside the testosterone program. The testosterone line is **real Schedule-III TRT** (cypionate
injection, gel 1.62% CIII) gated by labs + a video visit — not an OTC "test booster."

**Prominence (calibrated):**
- **Sexual health / ED is the anchor [HIGH]** — the brand's own "Featured" badge sits on **Generic Viagra
  (Sildenafil)** and **Branded Viagra by Pfizer** in the homepage "Top Products" rail, nav leads with Sexual
  Health, and a sitewide sale banner is ED-pinned ("$2 Per Tablet").
- **Zepbound® Vial GLP-1 is Featured [HIGH]** and **Ramelteon is badged "Popular" [HIGH]** in the same rail —
  weight loss and sleep are the next-promoted lines.
- **Testosterone reads as the deepest program [MED]** by section weight (4 SKUs, its own $99/$250 economics) —
  inferred from nav depth + the index grid, not a badge.

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Erectile Dysfunction | family | — | /our-medications/erectile-dysfunction/ | — | — | ED med family; intake → partner-pharmacy ship |
| Generic Viagra (Sildenafil) | buyable | ED | /our-medications/erectile-dysfunction/generic-viagra-sildenafil/ | "From $6 per use" (20mg $2 / 100mg $6 common); "$6 a pill"; promo "$2 Per Tablet" | published | sildenafil · tablet · async intake, taken ~1hr before sex |
| Branded Viagra® | buyable | ED | /our-medications/erectile-dysfunction/branded-viagra/ | "From $96 per use" (50/100mg $96) | published | sildenafil (Pfizer brand) · tablet |
| Generic Cialis (Tadalafil) | buyable | ED | /our-medications/erectile-dysfunction/generic-cialis-tadalafil/ | "From $6 per use" (10/20mg $6) | published | tadalafil · tablet (as-needed) |
| Branded Cialis® | buyable | ED | /our-medications/erectile-dysfunction/branded-cialis/ | "From $29 per use" (10/20mg $29) | published | tadalafil (Lilly brand) · tablet |
| Daily Generic Cialis (Tadalafil) | buyable | ED | /our-medications/erectile-dysfunction/daily-generic-cialis-tadalafil/ | "From $2 per use" (2.5/5mg $2) | published | tadalafil · daily low-dose tablet |
| Premature Ejaculation | family | — | /our-medications/premature-ejaculation/ | — | — | PE line |
| Sertraline | buyable | PE | /our-medications/premature-ejaculation/sertraline/ | "$27 per month" (1 month $27); "as little as $27 a month" | published | sertraline (generic Zoloft) · tablet · off-label for PE |
| Weight Management Program | family | — | /our-medications/weight-management/ | "starts at $75" | partial | GLP-1 program (clinician consult + Rx); med billed separately via manufacturer |
| Semaglutide (Wegovy®) | buyable | Weight Management Program | /our-medications/weight-management/semaglutide/ | "$499 per month" (via NovoCare®, flat any dose) | partial | semaglutide (Wegovy brand) · injection pen · cash-pay via NovoCare; $75 program on top |
| Tirzepatide (Zepbound®) | buyable | Weight Management Program | (no PDP — named on /our-medications/weight-management/) | "$349 per month" (Eli Lilly vial, cash-pay) | partial | tirzepatide (Zepbound brand) · vial/pen · cash-pay via Eli Lilly; $75 program on top |
| Testosterone Program ("TestoRx") | family | — | /our-medications/testosterone-program/ | "$99" one-time (lab panel + video consult); then "as low as $250 per month" | partial | Schedule-III TRT program; labs + video visit required; $250/mo covers quarterly shipments + ongoing labs + ≥1 video consult/yr |
| Testosterone Cypionate | buyable | Testosterone Program | /our-medications/testosterone-program/cypionate/ | incl. (Testosterone Program from $250/mo) | on-request | testosterone cypionate · injection · Schedule III; video visit + labs required |
| Testosterone Gel | buyable | Testosterone Program | /our-medications/testosterone-program/testosterone-gel/ | incl. (Testosterone Program from $250/mo) | on-request | testosterone gel 1.62% · topical · Schedule III (CIII) |
| Clomid® | buyable | Testosterone Program | /our-medications/testosterone-program/clomid/ | incl. (Testosterone Program from $250/mo) | on-request | clomiphene citrate · oral tablet |
| Sermorelin | buyable | Testosterone Program | /our-medications/testosterone-program/sermorelin/ | incl. (Testosterone Program from $250/mo) | on-request | sermorelin · injection · compounded peptide (GH-supporting) |
| Hair Loss | family | — | /our-medications/hair-loss/ | — | — | hair line |
| Finasteride | buyable | Hair Loss | /our-medications/hair-loss/finasteride/ | "$13.50 per month" (per-dose $0.90 / $0.72 / $0.45 at 1 / 6 / 12-mo plans); faq.php: "as low as $18 per month supply" | published | finasteride · tablet · men only (price varies by plan length — see anchors) |
| Insomnia & Sleep | family | — | /our-medications/insomnia/ | — | — | sleep line |
| Ramelteon | buyable | Insomnia & Sleep | /our-medications/insomnia/ramelteon/ | "$2.11 a dose" (8mg) | published | ramelteon · tablet · melatonin-receptor agonist ("Popular" badge) |
| Doxepin | buyable | Insomnia & Sleep | /our-medications/insomnia/doxepin/ | "$1.70 a dose" (10mg) | published | doxepin · low-dose tablet · sedating |
| Herpes | family | — | /our-medications/herpes/ | — | — | herpes line |
| Valacyclovir | buyable | Herpes | /our-medications/herpes/valacyclovir/ | "$27 per month" (3-month supply) | published | valacyclovir · tablet · herpes outbreaks |
| Anxiety | family | — | https://rx.rexmd.com/beta-blockers/ | — | — | situational/performance anxiety (separate rx. subdomain) |
| Beta blocker | buyable | Anxiety | https://rx.rexmd.com/beta-blockers/ | not captured | on-request | not stated (beta-blocker) · tablet · rx.rexmd.com page not scraped this run |

## Verbatim anchors

The footnotes the Price column points at, quoted exactly (cited to the captured page):

- **ED floors** (`ed-category.md`, `ed-sildenafil.md`): *"Treatments for as little as $2 per dose"*; *"From $6 per use" / "From $29 per use" / "From $2 per use" / "From $96 per use"*; *"patients can get sildenafil (generic Viagra) for as little as $6 a pill."* Sitewide promo banner (all pages): *"Memorial Day Sale Save Up To 95% Off ED Meds & Pay $2 Per Tablet."* Index grid (`our-medications.md`) dose→price: sildenafil 20mg $2 / 100mg $6; branded Viagra $96; generic Cialis 10–20mg $6; branded Cialis 10–20mg $29; daily generic Cialis 2.5–5mg $2.
- **Testosterone Program** (`trt-category.md`, `faq.php`): *"The Rex MD Testosterone Program begins with an initial offering of a one-time purchase for $99, which includes a lab panel and a video consultation with a provider or nurse practitioner.†"* … *"the program costs as low as $250 per month, covering quarterly shipments of the prescribed treatment, ongoing lab tests, and a minimum of one video consult per year."* †(faq): *"Initial $99 fee is for lab tests and provider consultation; monthly [cost is for medication]."*
- **Weight management** (`wm-category.md`, `wm-semaglutide.md`, `faq.php`): *"The Rex MD Weight Management Program starts at $75, with the flexibility to cancel anytime."* … *"Zepbound® is available in two forms: vials or pens. The vial is available directly through manufacturer Eli Lilly, starting at $349 per month, cash-pay. Wegovy® is available through NovoCare® at a flat cash-pay rate of $499 per month for any dose."* … *"The Rex MD GLP-1 Weight Management Program does not accept insurance at this time. Rex MD's parent company LifeMD accepts insurance for qualifying patients."*
- **Hair / sleep / PE / herpes** (`our-medications.md`, `faq.php`): finasteride *"$13.50 / per month"* (grid) vs *"as low as $18 per month supply… reduced price for patients who order six months"* (faq) — **discrepancy left unresolved, both quoted**; *"sertraline (generic Zoloft) costs as little as $27 a month"*; *"Ramelteon costs as low as $2.11 a dose and doxepin costs as low as $1.70 a dose"*; *"care and medication for herpes outbreaks starts as low as $27 per month when you order a three-month supply."*
- **Molecule sourcing audit** — every molecule above is page-attested: *sildenafil* ("Meet sildenafil", ed-sildenafil), *testosterone cypionate / Schedule III* ("a Schedule III controlled substance", trt-cypionate), *testosterone gel 1.62% CIII* (our-medications), *clomiphene citrate* ("CLOMID® (clomiphene citrate)"), *sermorelin* ("A compounded peptide therapy"), *semaglutide/Wegovy · tirzepatide/Zepbound · liraglutide/Saxenda* (wm pages). The **beta-blocker** molecule is **not stated** — the page lives on rx.rexmd.com and was not captured, so no molecule is asserted (propranolol not page-confirmed).

## Deep blocks

Earned blocks — each resolves a roster ambiguity a row can't, and references a captured flagship hero render.

### Testosterone Program — the bundle that hides per-SKU price
The roster's four testosterone SKUs all read `on-request` because Rex prices the **program**, not the molecule:
*"$99"* buys a lab panel + video consult; *"as low as $250 per month"* then covers "quarterly shipments of the
prescribed treatment, ongoing lab tests, and a minimum of one video consult per year." Which SKU you land on
(cypionate injection / gel / Clomid / sermorelin) and its cost are set by the provider after labs — so no
per-SKU price is published. This is the line's real shape: a clinical TRT program, not a catalogue.
Hero render: `captures/2026-06-04/images/testosterone-cypionate.webp` (clean navy-label REX MD "Testosterone
Cypionate" multi-dose vial).

### Weight management — FDA-brand GLP-1 at manufacturer cash-pay
Rex's "$75" weight program is the consult/Rx wedge; the **drug** is bought through the manufacturer, so the
all-in stacks (program + med). Wegovy® routes to **NovoCare® at "$499 per month" flat for any dose**; Zepbound®
vials to **Eli Lilly at "$349 per month"**. Rex states the compounded-semaglutide window has closed ("the FDA
has since declared that the shortage is over… pharmacies can no longer compound semaglutide"), which is why this
line is brand-only and `partial` (med priced/bought off-platform). Hero render:
`captures/2026-06-04/images/semaglutide.webp` (clean white-bg branded **Wegovy® 2.4 mg semaglutide injection** pen).

### Generic Viagra (Sildenafil) — the anchor floor, and the promo wedge
The "From $6 per use" / "$6 a pill" sildenafil SKU is Rex's most-promoted product (homepage "Featured" badge),
and the sitewide "$2 Per Tablet / up to 95% off" banner is the acquisition hook that pulls the displayed floor
below the grid price. Molecule page-attested ("Meet sildenafil… typically taken about one hour before you plan
to have sex"). Hero render: `captures/2026-06-04/images/generic-viagra-sildenafil.webp` (clean white-bg pair of
blue sildenafil tablets).

## Provenance

- **Pages read:** `/our-medications/` (rich index — the price backbone) + ED/TRT/WM/hair category pages + 3 flagship PDPs (sildenafil, cypionate, semaglutide, captured with `--images`) + `faq.php` for program pricing. All under `store/rexmd-com/captures/2026-06-04/`.
- **Scope:** all 8 lines enumerated; ED enumerated to 5 SKUs, testosterone to 4, sleep to 2. Zepbound rostered from copy (no PDP). The **anxiety/beta-blocker** SKU is noted-but-not-priced (rx.rexmd.com not captured). PE/herpes/hair/sleep are single-SKU lines.
- **Snapshot caveat:** pricing runs promo (sitewide "up to 95% off ED / $2 per tablet"); the finasteride monthly figure disagrees across pages ($13.50 grid vs $18 FAQ). Treat all prices as point-in-time.
- **### Run profile:** offerings + hero images requested. Captured the 3 flagship PDPs with `--images`; promoted clean isolated renders (sildenafil tablets, cypionate vial, Wegovy pen) to `captures/2026-06-04/images/`. No PDP-template-anatomy block (not requested).
