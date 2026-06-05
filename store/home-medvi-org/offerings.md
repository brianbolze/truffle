---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: home.medvi.org
captured_at: 2026-06-04
site_notes: "Products live on 3 separate Framer funnel subdomains, NOT under home.medvi.org: glp1.medvi.org (weight loss — 5 SKU cards + prices + a pricing FAQ; every CTA → /intake quiz; NO per-SKU PDPs, so SKU slugs are '(no PDP — card)'), quad.medvi.org (a single QUAD product + price), meals.medvi.org (white-label meal storefront on mfg-whitelabel-prod S3 — Classic/Premium programs, plan grid 6/10/15/20 meals/wk, prices on-page). Prices are promo-driven (glp1 'SUMMER Sale Only $179'; meals 'MEDVI20' 20% off + a live countdown) — point-in-time, re-check next run. Branded-GLP-1 (Wegovy®/Zepbound®) medication cost is intake-gated; only the '$99 Membership' floor shows. Molecule named on-page only for the compounded semaglutide injection (FAQ) and QUAD's four actives — brand names are NOT mapped to molecules on the page."
---

## Portfolio overview

MEDVi is **Multi-product but flagship-heavy**: three live lines on three funnel subdomains, plus five
"Coming Soon" verticals (Women's Health, Peptides & Longevity, Supplements, Hair, Skincare) that have **no
SKUs or prices yet** and are therefore noted, not rostered.

- **Weight Loss (compounded GLP-1) is the lead line `[HIGH]`** — the homepage + /about-us are almost entirely
  weight loss, the 500,000-patient claim is GLP-1, and it's the only line with a full SKU lineup *and* a
  pricing FAQ. Five cards: two compounded ("GLP-1 Injections" / "GLP-1 Tablets") and three brand
  ("Wegovy® Pill / Injection," "Zepbound® Injection").
- **A two-pattern pricing split, on the company's own labels `[HIGH]`:** the **compounded** SKUs are
  **`published`** and self-contained — *"No membership or hidden fees,"* `$179` first month → `$299` refills
  (a model that *undercuts* membership-stacking rivals like Hims). The **branded** SKUs are **`partial`** —
  *"$99 Membership + Medication Cost,"* with the medication cost gated behind intake.
- **Men's Health = QUAD™, and it is NOT TRT `[HIGH]` (shape finding).** The homepage men's card promises
  "hormones, energy and performance," but the **live** product (quad.medvi.org) is purely a **sexual-performance
  ED sublingual** — a 4-in-1 stack of apomorphine + vardenafil + sildenafil + tadalafil. No testosterone /
  hormone SKU is actually buyable. A single hero product at `$114`/mo.
- **MEDVi Meals `[MED]`** — a live, separately-platformed meal-delivery storefront positioned as the GLP-1
  companion ("protect your progress / preserve muscle"); Classic & Premium programs, priced per box/serving.

**Visibility rule (stated once, applied to every row):**
- **`published`** — the shown number is the full, self-contained entry price (compounded GLP-1 `$179`/`$299`;
  QUAD `$114`; Meals Classic box `$99.90`). A "Starting at" floor still counts as published when that entry
  tier is itself purchasable — the floor is quoted verbatim.
- **`partial`** — the headline **excludes a mandatory separate cost**: the three **branded** GLP-1 SKUs show
  only *"$99 Membership + Medication Cost,"* so the real all-in is higher than the `$99` shown.
- **`on-request`** — no price on the captured page (Meals **Premium** program box price; the Coming-Soon lines).

## Roster

Complete at the indexed level (MEDVi's product cards / lines). The weight-loss SKUs are cards on a single
funnel page with no per-SKU PDP (every CTA → `/intake`), so their slug notes `(no PDP — …)`. Price quoted
verbatim with on-page markers; molecule page-attested only (never inferred from a brand name — see the audit
under Verbatim anchors).

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| **Weight Loss** | family | — | `glp1.medvi.org` | — | — | Compounded + branded GLP-1 line; intake-quiz gated, provider-reviewed, shipped. |
| GLP-1 Injections | buyable | Weight Loss | `(no PDP — glp1.medvi.org card → /intake)` | `Starting at $179` (first month; refills `locked in at $299`) | published | semaglutide (compounded) · once-weekly injection · "No membership or hidden fees," cash-pay, HSA/FSA. |
| GLP-1 Tablets | buyable | Weight Loss | `(no PDP — glp1.medvi.org card → /intake)` | `Starting at $249` | published | not stated · once-daily dissolvable oral tablet · compounded GLP-1, no membership. |
| Wegovy® Pill | buyable | Weight Loss | `(no PDP — glp1.medvi.org card → /intake)` | `$99 Membership + Medication Cost` | partial | not stated · once-daily oral pill · brand Wegovy®; medication cost intake-gated. |
| Wegovy® Injection | buyable | Weight Loss | `(no PDP — glp1.medvi.org card → /intake)` | `$99 Membership + Medication Cost` | partial | not stated · injection · brand Wegovy®; "Availability is subject to change." |
| Zepbound® Injection | buyable | Weight Loss | `(no PDP — glp1.medvi.org card → /intake)` | `$99 Membership + Medication Cost` | partial | not stated · injection · brand Zepbound®; "Availability is subject to change." |
| **Men's Health — QUAD™** | buyable | — | `quad.medvi.org` | `$114` /month (`Starting at`; struck `$179`, "36% Off Retail") | published | apomorphine + vardenafil + sildenafil + tadalafil · sublingual rapid-absorb liquid (under-tongue) · 3-min intake, doctor consult + free rush shipping included, cancel anytime. |
| **MEDVi Meals** | family | — | `meals.medvi.org` | — | — | Chef-prepared, macro-friendly ready-to-eat meal delivery; weekly subscription; 75+ weekly / 300+ rotating meals. |
| Meals — Classic program | buyable | MEDVi Meals | `meals.medvi.org/pages/programs` | 10-meal box `$124.88` → `$99.90` (`$12.49` → `$9.99`/serving; first box `$24.98 off (20%)` w/ "MEDVI20") | published | meals · 6/10/15/20 per week · standard portion sizes. |
| Meals — Premium program | buyable | MEDVi Meals | `meals.medvi.org/pages/programs` | — (box price not shown on captured page) | on-request | meals · premium tier (Ultra-Premium menu, larger portions) · price gated to program selector. |

## Verbatim anchors

The footnotes the Price column points at (what *decides* `partial` vs `published`), quoted exactly:

- **Compounded GLP-1 → `published`** (glp1.medvi.org): *"**No membership or hidden fees!** Everything you need
  is included"* · *"**Start for just $179**, no insurance required + free shipping"* · banner *"**SUMMER Sale!**
  Only $179 + Fast, Free Shipping."*
- **GLP-1 pricing FAQ** (glp1.medvi.org — names the molecule + the refill price): *"The **MEDVi Semaglutide
  program** starts at **$179** for your first month with no contract. This cost covers your physician review,
  full personalized plan, 1:1 guidance, metabolic report, and the cost of the prescription medication shipped
  right to your door. **Refills are locked in at $299** and include all the same program benefits."*
- **Branded GLP-1 → `partial`** (glp1.medvi.org, on each of the 3 brand cards): *"**$99 Membership + Medication
  Cost**"* (the medication cost itself is never shown; gated behind `/intake`).
- **QUAD** (quad.medvi.org): *"MEDVi QUAD™ Prescription · MOST POPULAR · **$114** ~~$179~~ /month · Starting at
  · Or Bundle & Save More · 36% Off Retail · Doctor Consultation Included · Free Rush Shipping."*
- **Meals — Classic 10-meal** (meals.medvi.org): *"Most Popular · 10 Meals per week · Box Price **$124.88
  $99.90** · Price per serving **$12.49 $9.99** · First box total **$24.98 off (20%)** · You have applied the
  discount **MEDVI20**."*

**Molecule-sourcing audit (rule 2 — page-attested only, never from the brand name):**
- **semaglutide** — attested only for **GLP-1 Injections** (FAQ: *"MEDVi Semaglutide program"*). Not extended to
  GLP-1 Tablets (page says only "GLP-1").
- **Wegovy® Pill / Injection, Zepbound® Injection** → **not stated.** The page shows the brand names and a
  footnote that Wegovy®/Ozempic®/Zepbound® are trademarks, but never writes "semaglutide"/"tirzepatide" beside
  the SKU — so the molecule is *not* inferred from the brand.
- **QUAD** → **apomorphine, vardenafil, sildenafil, tadalafil** all explicitly named on quad.medvi.org with
  per-ingredient mechanisms (not inferred).

## Deep blocks

Earned where a real ambiguity a roster row can't carry needs resolving; both also reference the run's opt-in
hero product renders.

### Weight Loss — the two-tier pricing the roster collapses

The flagship funnel sells **two pricing models on one page**, and the roster's per-row token is the only place
that shows it: the **compounded** path is a clean `published` program — `$179` first month, `$299` refills,
"no membership, no hidden fees," cash-pay (HSA/FSA-eligible) — while the **branded** path (real Wegovy®/Zepbound®)
flips to `partial`: a `$99 Membership` floor with the drug cost itself withheld until after intake. The headline
"$179" that brands the whole funnel therefore only applies to the compounded injection; the branded cards are a
different, more-gated deal. Compounded GLP-1s are explicitly **not FDA-approved** (dispensed by partner pharmacies
Triad Rx / RedRock / Beaker under OpenLoop / CareGLP clinician oversight).
- **Hero renders** (clean isolated product shots, `captures/2026-06-04/images/`): `glp1-injection.png`,
  `glp1-tablet.png`, `wegovy-pill.png`, `wegovy-injection.png`, `zepbound-injection.png`.

### Men's Health — QUAD™ is an ED stack, not the "hormones" the homepage implies

The homepage men's-health card markets "hormones, energy and performance," which reads like a TRT line; the
**live** product is nothing of the sort. QUAD™ is a **single sublingual liquid combining four actives** —
*apomorphine* (desire / dopamine), *vardenafil* (rapid onset), *sildenafil* (peak strength), *tadalafil*
(up to 36 h) — pitched as "4 meds in 1 dose," "ready in 10–15 minutes," "lasts all weekend." A buyer comparing
MEDVi's "men's health" to a hormone/TRT brand would be comparing different categories. One price: `$114`/mo
(from `$179`).
- **Hero render:** `captures/2026-06-04/images/quad.png` (the black "QUAD" labeled bottle).

## Provenance

- **Pages read:** `glp1.medvi.org` (weight-loss SKUs + pricing FAQ), `quad.medvi.org` (QUAD + price),
  `meals.medvi.org` (Meals programs + Classic price), homepage + /about-us (line inventory / "Coming Soon").
  All in `store/home-medvi-org/captures/2026-06-04/`.
- **Scope:** enumerated = the 3 live lines and every priced card/program shown. Noted-but-not-enumerated =
  the 5 "Coming Soon" verticals (pre-launch, no SKUs); the branded-GLP-1 medication cost (intake-gated); Meals
  **Premium** box price (gated to the program selector); the full 300+ Meals menu items (a rotating food menu,
  not a fixed SKU set).
- **Point-in-time caveat:** prices are promo-driven and **not fixed** — glp1 ran a "SUMMER Sale Only $179,"
  meals applied a live "MEDVI20" 20% discount with a countdown. Re-check next run.
- **Run profile:** guided — no emphasis; **+hero product images** (opt-in `fc.py hero` asset capture;
  framerusercontent CDN blocked the headed scorer, so the clean per-SKU renders were fetched directly with a
  browser UA + referer and promoted to `captures/2026-06-04/images/`).
