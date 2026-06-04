---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: eden.health          # company key; each offering's slug (its relative url) is its key *within* Eden
captured_at: 2026-06-03      # own freshness; captures/2026-06-03/ holds the source pages
---

## Portfolio overview

Eden (eden.health; legal entity Eden Health International Inc.; intake/portal on `tryeden.com` / `app.eden.health`)
is a GLP-1-led DTC telehealth roll-up — **Multi-product**, six nav lines (Weight Loss, Strength, Anti-Aging,
Hair Growth, Mood, plus a "More" bucket of Daily Essentials / Hormones & Intimacy) on a single Webflow catalog.
This doc enumerates the **complete prescription roster: 25 distinct `/treatment/*` PDPs**, which resolve to
**27 buyable offerings** once the GLP-1 hub is split into its two compounded sub-SKUs (Compounded Semaglutide,
Compounded Tirzepatide), plus the mandatory **Eden Membership** that gates them all. Every line sells the same
way: a nav category → a `/treatment/<sku>` PDP carrying a **med-only "From $X" price + a separate mandatory
membership** → a free online intake/telehealth consult → if prescribed, a compounded (or branded) med shipped
from a 503A network pharmacy with 24/7 care-team messaging.

**Shape finding #1 — the price you see is never the all-in: every treatment is `partial`, only the membership
is `published`.** Identical to the Hims archetype. Each PDP shows a medication price, but the universal footnote
(on all 25 PDPs, verbatim) is: *"Price includes medication only, if prescribed. An active Eden Membership is
required ($39 for the first month, auto-renews at $99/month thereafter)… Medication is not available without a
membership."* So the all-in = the shown med price **+ $99/mo membership**, and the only self-contained,
fully-shown number on the whole site is the **membership fee itself**. The nav prints the `*Plus Eden Membership`
asterisk **only** on the GLP-1 tile, but the full membership-required footnote sits on every PDP — so the
membership is genuinely universal, not weight-loss-only.

**Shape finding #2 — two flavors of "incomplete," one token.** Eden splits into branded vs everything-else:
- **Branded GLP-1s** (Ozempic®/Zepbound®/Mounjaro® `$1,399/month`, Wegovy® `$1,695/month`) show a flat monthly
  number — but still med-only, membership stacked → `partial`.
- **Compounded / personalized lines** mostly show **"Starting at $X first month"** — an *intro* price whose
  ongoing recurring rate is withheld, on top of the membership → doubly `partial`.

  Notably, Eden's **"Same Price at Every Dose"** guarantee removes the dose-tier movement that made Hone's
  hormone SKUs partial — so here the `partial` call rests squarely on the **separate mandatory membership**
  (and the intro-only "first month" framing), *not* on a dose floor that moves. The visibility rule applied
  across the roster: **`partial` = med-only price + the mandatory $99/mo membership and/or an intro-"first
  month" rate; `published` = a flat self-contained price with no separate membership** (only the Eden Membership
  row qualifies). The lone non-Rx item (Cell Theory, a dietary supplement) is marked `partial` for the
  intro-pricing reason only — its membership footnote is generic boilerplate that arguably doesn't apply (see
  anchors).

**Prominence (calibrated).**
- **Weight Loss / GLP-1 is unambiguously the flagship [HIGH].** It owns the company's *own* lead signals: the
  only nav tile carrying a price + the `*Plus Eden Membership` asterisk ("Personalized GLP-1 Treatments — From
  $99/mo*"), the widest single lineup (2 compounded + 4 branded + a kit = 7 SKUs), the entire homepage funnel
  (BMI/BMR/TDEE calculators, before/after sliders), and the deepest PDP (its own multi-SKU comparison carousel).
- **NAD+ is the Anti-Aging anchor [MED].** Four delivery forms (injection/nasal/cream + the non-Rx Cell Theory
  supplement) and a dedicated nav tile ("NAD+ Injections — From $119 first month") — the broadest non-weight line.
- **Sermorelin, Hair Kit, and MIC+B12 carry their own nav tiles with "from" prices [MED]** — the company gives
  Strength, Hair, and Mood a promoted hero each, signaling they're real lines, not afterthoughts.
- Card/section order within the mega-nav and the "In Stock" tags are **[LOW]** — not used for ranking.

## Roster

Complete at the indexed (PDP) level — the 25 `/treatment/*` pages from the homepage nav, cross-checked against
the `/map` census (which returned exactly the same 25; see Provenance). Within-company key = **Slug** (the
relative URL, quoted exactly). Price quoted verbatim with its on-page markers; the universal **+ Eden Membership**
is the mandatory separate cost (see anchors). **Form** = the page-attested delivery mechanism as the matching
[Delivery Mechanisms](https://notion.so/getdoro/293c8c60d33840efb1ef4eb30cf6a959) slug; **Category** = the
slugified best-fit [Product Category](https://notion.so/getdoro/534f9c5eb01c4c8099cf0419f1834e6a) (`[?]` = a
genuine cross-cutting call, explained in the anchor). Molecule/form is **page-attested only**, never inferred
from the brand. An offering here is never asserted equal to a same-molecule offering at another brand.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | Form | Category | What (molecule · access) |
|---|---|---|---|---|---|---|---|---|
| **Eden Membership** | buyable | — | (recurring fee — no standalone PDP; terms in every price footnote) | `$39 for the first month, auto-renews at $99/month thereafter` | published | not a drug | — | subscription · the mandatory access fee that gates every Rx SKU; billed separately from medication. |
| **Weight Loss** | family | — | (nav category — no standalone page) | — | — | — | glp-1-medical-weight-loss | The GLP-1-led flagship line: 2 compounded + 4 branded GLP-1s + a non-injectable oral kit. |
| GLP-1 Treatments (hub) | buyable | Weight Loss | `/treatment/glp-1-treatments` | `From $99/mo*` | partial | injection | glp-1-medical-weight-loss | the compounded-GLP-1 hub PDP; sells the two sub-SKUs below + lists the 4 branded SKUs. |
| Compounded Semaglutide | buyable | GLP-1 Treatments | `/treatment/glp-1-treatments` (sub-SKU on the hub page — no own slug) | `$99/mo*` | partial | injection | glp-1-medical-weight-loss | semaglutide · membership-gated; the cheapest GLP-1 entry. |
| Compounded Tirzepatide | buyable | GLP-1 Treatments | `/treatment/glp-1-treatments` (sub-SKU; marketing variant `/shop/compounded-tirzepatide-m`) | `$199/mo*` | partial | injection | glp-1-medical-weight-loss | tirzepatide · membership-gated. |
| Ozempic® | buyable | Weight Loss | `/treatment/ozempic` | `$1,399/month` | partial | injection | glp-1-medical-weight-loss | not stated · membership-gated; "injectable… type 2 diabetes." Semaglutide named only in a page citation — see anchor. |
| Zepbound® | buyable | Weight Loss | `/treatment/zepbound` | `$1,399/month` | partial | injection | glp-1-medical-weight-loss | tirzepatide · injection, once-weekly · membership-gated. "Zepbound contains tirzepatide." |
| Wegovy® | buyable | Weight Loss | `/treatment/wegovy` | `$1,695/month` | partial | injection | glp-1-medical-weight-loss | semaglutide · injection, 2.4 mg · membership-gated. "Wegovy® (semaglutide) injection." The priciest SKU. |
| Mounjaro® | buyable | Weight Loss | `/treatment/mounjaro` | `$1,399/month` | partial | injection | glp-1-medical-weight-loss | not stated · injection, weekly · membership-gated; "FDA-approved weekly injectable… type 2 diabetes" (tirzepatide not named on page). |
| Custom Weight Loss Kit | buyable | Weight Loss | `/treatment/custom-weight-loss-kits` | `Starting at $34 first month` | partial | pill | glp-1-medical-weight-loss | metformin · bupropion · low-dose naltrexone · acarbose · orlistat (+ inositol, acetyl-L-carnitine, B6, B12) · "no injections," membership-gated. |
| **Strength** | family | — | (nav category — no standalone page) | — | — | — | — | Peptide + ED line. |
| Sermorelin Injection | buyable | Strength | `/treatment/sermorelin` | `Starting at $126 first month` | partial | injection | peptides | sermorelin (GHRH analog; "supporting natural HGH production… without anabolic steroids") · membership-gated. |
| Sermorelin ODT | buyable | Strength | `/treatment/sermorelin-odt` | `Starting at $126 first month` | partial | sublingual-troche | peptides | sermorelin · orally-dissolving tablet ("without… injections") · membership-gated; needle-free twin of the injection. |
| Vardenafil + Tadalafil | buyable | Strength | `/treatment/vardenafil-tadalafil` | `Starting at $44 first month` | partial | sublingual-troche | ed | vardenafil + tadalafil (PDE-5 inhibitors) · "dual-action sublingual tablet" · membership-gated. |
| **Anti-Aging** | family | — | (nav category — no standalone page) | — | — | — | nad | NAD+ across 3 Rx forms + a non-Rx supplement, plus glutathione. |
| NAD+ Injection | buyable | Anti-Aging | `/treatment/nad` | `Starting at $119 first month` (`Only $15/shot*, homekit included`) | partial | injection | nad | NAD+ (nicotinamide adenine dinucleotide) · 500–1000mg/vial, 200mg/mL · membership-gated. |
| NAD+ Nasal Spray | buyable | Anti-Aging | `/treatment/nad-nasal-spray` | `Starting at $112 first month` | partial | nasal-spray | nad | NAD+ · no-needle nasal delivery · membership-gated. |
| NAD+ Face Cream | buyable | Anti-Aging | `/treatment/nad-facial-cream` | `From $84/month` | partial | topical-gel | nad [?] | NAD+ · daily topical cream for skin · membership-gated. Skincare cross-listing — see anchor. |
| Glutathione | buyable | Anti-Aging | `/treatment/glutathione` | `Starting at $95 first month` | partial | injection | wellness-injectables [?] | glutathione ("master antioxidant") · injection · membership-gated. Catalog-context call — see anchor. |
| Cell Theory NAD+ Supplement | buyable | Anti-Aging | `/treatment/cell-theory` | `Starting at $25 first month` | partial | pill | nad [?] | NAD+ (Niacinamide + Liposomal NAD+ + NADH) + 8 longevity compounds · **non-Rx** oral supplement · intro-priced; membership footnote is boilerplate — see anchor. |
| **Hair Growth** | family | — | (nav category — no standalone page) | — | — | — | hair-loss | Sex-specific men's + women's hair lines; finasteride/minoxidil/GHK-Cu + two kits. |
| Finasteride for Men | buyable | Hair Growth | `/treatment/finasteride-for-men` | `From $25/month` | partial | pill | hair-loss | finasteride · oral tablet, FDA-approved (DHT blocker) · membership-gated. |
| Minoxidil for Men | buyable | Hair Growth | `/treatment/minoxidil-for-men` | `From $25/month` | partial | pill | hair-loss | minoxidil · low-dose **oral** tablet (off-label) · membership-gated. |
| GHK-Cu Foam for Men | buyable | Hair Growth | `/treatment/ghk-cu-for-men` | `From $68/month` | partial | topical-gel | hair-loss | GHK-Cu (copper peptide) · topical scalp foam (cosmetic) · membership-gated. |
| Custom Hair Growth Kit for Men | buyable | Hair Growth | `/treatment/hair-growth-kits-for-men` | `From $83/month` | partial | pill + topical-gel | hair-loss | oral finasteride + oral minoxidil + GHK-Cu foam (kit) · membership-gated. |
| Minoxidil for Women | buyable | Hair Growth | `/treatment/minoxidil-for-women` | `From $25/month` | partial | pill | hair-loss | minoxidil · low-dose **oral** tablet (off-label for women) · membership-gated. |
| GHK-Cu Foam for Women | buyable | Hair Growth | `/treatment/ghk-cu-for-women` | `From $68/month` | partial | topical-gel | hair-loss | GHK-Cu (copper peptide) · topical scalp foam · membership-gated. |
| Custom Hair Growth Kit for Women | buyable | Hair Growth | `/treatment/hair-growth-kits-for-women` | `From $83/month` | partial | pill + topical-gel | hair-loss | low-dose oral minoxidil + GHK-Cu foam (kit; no finasteride) · membership-gated. |
| **Mood** | family | — | (nav category — no standalone page) | — | — | — | — | "Improved Mood" line — a wellness-injectable + a longevity Rx. |
| MIC+B12 | buyable | Mood | `/treatment/mic-b12` | `Starting at $73 first month` | partial | injection | wellness-injectables [?] | methionine + inositol + choline + methylcobalamin (B12) · injection · membership-gated. Filed under Mood — see anchor. |
| Methylene Blue | buyable | Mood | `/treatment/methylene-blue` | `From $89/month` | partial | pill | longevity-rx-non-nad | methylene blue · oral capsule/tablet ("No mess Rx Tablets… unlike troches & drops") · membership-gated. |
| **More — Daily Essentials & Hormones** | family | — | (nav bucket — no standalone page) | — | — | — | — | The "More" grab-bag: a daily metabolic program + women's hormone therapy. |
| Everyday+ | buyable | More | `/treatment/everyday-plus` | `$95/month` | partial | pill | supplements [?] | "doctor-determined metabolic health program" — low-dose naltrexone + L-carnitine + inositol (contains Rx) · membership-gated. DB files Eden Everyday+ as a supplement — see anchor. |
| Hormone Therapy for Women (My Custom Hormone Kit) | buyable | More | `/treatment/hormone-kit-for-women` | `Starting at $79 first month` | partial | patch + topical-gel + pill | hrt-womens-menopause | estradiol (patch / vaginal cream) + progesterone (compounded oral caps) · membership-gated. |

**Buyable count (in scope): 27** — 24 single-SKU Rx PDPs + the GLP-1 hub's 2 compounded sub-SKUs + the Eden
Membership. The 6 `family` rows are nav groupings, not counted. Dedup: the GLP-1 hub and its 2 sub-SKUs share
one slug (listed distinctly); the marketing URLs `/shop/compounded-tirzepatide-m`, `/offer/glp1micro`,
`/weight`, `/weight-loss`, `/weight-loss-quiz` are funnel variants of the GLP-1 line, **not** separate
offerings (noted in Provenance, not rostered).

### Verbatim anchors

The footnotes the Price/Visibility/Category columns point at — they decide the `partial` calls and carry the
molecule + category audit. Quoted exactly from the cited captures.

- **The universal membership (the `partial` driver), verbatim on all 25 PDPs:** *"Price includes medication
  only, if prescribed. An active Eden Membership is required ($39 for the first month, auto-renews at $99/month
  thereafter). Membership does not include or guarantee a prescription. Medication is not available without a
  membership. Membership fee is not included."* → every med price is real but med-only; all-in = price + $99/mo.
- **"Same Price at Every Dose" (why the call is membership-based, not dose-tier):** *"Our 'Same Price at Every
  Dose' policy ensures consistent pricing regardless of dosage adjustments throughout your program (excluding
  new member discounts or specific plans)."* (GLP-1 PDP footer.) So unlike Hone's dose tiers, Eden's floor
  doesn't move with dose — the `partial` rests on the separate mandatory membership + the intro "first month" rate.
- **Molecule sourcing (page-attested-only, audited):**
  - **Zepbound® → tirzepatide** — attested: *"Zepbound contains tirzepatide…"* **Wegovy® → semaglutide** —
    attested: *"Wegovy® (semaglutide) injection 2.4 mg…"*
  - **Ozempic® → not stated; Mounjaro® → not stated.** Neither product page names its molecule in product copy.
    Ozempic's page mentions "semaglutide" **only inside a reference-list citation** (*"Clinical Review Report:
    Semaglutide (Ozempic)"*), not as a "contains" statement — so recorded **not stated**, paralleling the
    page-attested discipline (a citation title ≠ a product attestation; cf. Hims's Mounjaro call).
  - **Compounded Semaglutide → semaglutide; Compounded Tirzepatide → tirzepatide** — attested by the SKU labels
    themselves (the cards read "Compounded Semaglutide" / "Compounded Tirzepatide").
  - **Sermorelin → "supporting natural HGH production… without anabolic steroids"** (GHRH-analog peptide);
    **MIC+B12 → "Methionine, Inositol, Choline, and Methylcobalamin"**; **Cell Theory → "Niacinamide, Liposomal
    NAD+, and NADH"** + 8 compounds (Quercetin, Pterostilbene, Apigenin, ALA, Ergothioneine, Piperine,
    Methylfolate); **Custom WL Kit → "metformin, bupropion, low-dose naltrexone (LDN), acarbose, or orlistat…
    inositol, acetyl-L-carnitine, and vitamins B6 and B12"**; **Everyday+ → "low-dose naltrexone, L-Carnitine,
    inositol, or others"**; **Hormone Kit → "estradiol cream and patch… compounded… oral progesterone"** — all
    quoted from product copy.
  - **GHK-Cu → "a copper peptide"; Vardenafil + Tadalafil → "PDE-5 inhibitors… dual-action sublingual tablet";
    Finasteride/Minoxidil → "Finasteride tablets… DHT" / "low-dose oral Minoxidil"** — page-attested.
- **Category `[?]` calls (genuine cross-cutting; flagged, not forced):**
  - **NAD+ Face Cream → `nad [?]`** — molecule-anchored (Eden files it under Anti-Aging *and* "Skin"), but the
    Product-Categories DB carves "NAD+ face cream" *out* of NAD toward skincare, so **`aesthetics-dermatology`**
    is the defensible alternative. Kept `nad` for cross-brand NAD comparability; flag preserves the ambiguity.
  - **Glutathione → `wellness-injectables [?]`** — a standalone injectable antioxidant fits Wellness Injectables
    precisely, but the DB's rule "*glutathione sold inside a longevity-Rx catalog → Longevity Rx*" + Eden's
    Anti-Aging/Antioxidants framing argue **`longevity-rx-non-nad`**. Chose the molecule/form fit.
  - **Cell Theory → `nad [?]`** — the NAD category explicitly includes oral NAD supplement forms, so `nad` (most
    useful for cross-brand NAD queries); but as a **non-Rx** dietary supplement it could read `supplements`.
  - **MIC+B12 → `wellness-injectables [?]`** — Eden files it under **Mood**, but an injectable B12/MIC vitamin
    shot is a textbook Wellness Injectable, *not* a psychiatric med, so `mental-health` was rejected.
  - **Everyday+ → `supplements [?]`** — the Product-Categories DB names "Eden Everyday+" as its own Supplements
    exemplar, so honored — but it contains Rx low-dose naltrexone, so `longevity-rx-non-nad` is arguable.
- **Cell Theory visibility (`partial`, with caveat):** hero reads *"Starting at $25 first month"* with **no
  asterisk**, and the page carries *"Statements regarding dietary supplements have not been evaluated by the
  FDA…"* — it's a **dietary supplement**, so the medication-membership footnote is generic site boilerplate
  that likely doesn't apply. Marked `partial` only because the **recurring rate is withheld** behind a "first
  month" intro price; were the ongoing price shown and no membership applied, this would be the one extra `published`.

## Deep blocks

Three earn their place — the three requested deep-dives, spanning three forms, three categories, three
*structures*: a multi-brand price carousel (GLP-1), a single-molecule injectable (NAD+), and a multi-ingredient
kit (Hair). Each maps the PDP anatomy in page order, then quotes the load-bearing parts verbatim.

### GLP-1 Treatments — the flagship (a one-page price carousel for 6 SKUs)

- **Parent:** Weight Loss · **slug:** `/treatment/glp-1-treatments` · **price:** `From $99/mo*` (hero) ·
  **visibility:** `partial` · **form:** injection · **category:** glp-1-medical-weight-loss

> **Page anatomy (in order):** mega-nav → **H1 "Personalized GLP‑1 Treatments"** ("A personalized weight loss
> plan built around you") → **dual hero price block** (Compounded Semaglutide **$99/mo** + Eden Membership* /
> Compounded Tirzepatide **$199/mo** + Eden Membership*) → Klarna/Afterpay → benefit icons ("Same price at
> every dose. No long-term contracts." / "Free expedited shipping." / "Doctor-led plans") → **"Medication made
> affordable" carousel** (the 6-SKU price list, below) → 3-step how-it-works → before/after testimonials
> (Jamie −43 lb, Melissa −47 lb) → Dr. Rebecca Emch quote → FAQ accordion → final CTA + ISI.
> **The 6-SKU carousel (verbatim, the roster's price source):** "Compounded Semaglutide **$99/mo\***" ·
> "Compounded Tirzepatide **$199/mo\***" · "Ozempic® **$1,399/mo**" · "Zepbound® **$1,399/mo**" · "Wegovy®
> **$1,695/mo**" · "Mounjaro® **$1,399/mo**."
> **Membership footnote (verbatim):** "Price includes medication only, if prescribed. An active Eden Membership
> is required ($39 for the first month, auto-renews at $99/month thereafter)… Medication is not available
> without a membership. Membership fee is not included."
> **Molecule honesty (verbatim FAQ):** "…active ingredients such as semaglutide, tirzepatide, liraglutide,
> setmelanotide, phentermine, orlistat, and naltrexone-bupropion… All treatment decisions are made by licensed
> providers." (Names the class, not which branded SKU = which molecule — why Ozempic/Mounjaro stay "not stated.")

**Why it earns a block:** this single page *is* the weight-loss roster — six SKUs' verbatim prices live in one
carousel, and it's the one place the compounded $99/$199 sub-SKUs (which have no own `/treatment/` slug) are
priced. It also demonstrates the brand-wide pricing mechanic (med-only + mandatory membership) that flips every
roster row to `partial`.

### NAD+ Injection — the Anti-Aging anchor (single molecule, per-shot framing)

- **Parent:** Anti-Aging · **slug:** `/treatment/nad` · **price:** `Starting at $119 first month` ·
  **visibility:** `partial` · **form:** injection · **category:** nad

> **Page anatomy (in order):** mega-nav → **H1 "NAD+ Injection"** → **"Starting at $119 first month"** →
> Klarna/Afterpay + "FSA/HSA Eligible" → benefit icons (incl. **"Only $15/shot\*, homekit included"** and
> **"Full-strength dosages of 500-1000mg per vial (200mg/mL)"**) → "What is NAD+" Q&A → **Related Products**
> (NAD+ Nasal Spray, NAD+ Face Cream — the cross-form line) → "Feel stronger and age with confidence" →
> benefit tiles (focus / energy / healthy aging) → ISI + membership footnote.
> **Molecule (verbatim, page-attested):** "NAD+ (Nicotinamide Adenine Dinucleotide) injections help replenish a
> vital coenzyme that declines with age—playing a key role in energy metabolism, DNA repair, and cellular
> resilience."
> **Dose (verbatim):** "Full-strength dosages of 500-1000mg per vial (200mg/mL)." · per-unit "Only $15/shot\*,
> homekit included."
> **Membership footnote (verbatim):** identical "An active Eden Membership is required ($39 for the first month,
> auto-renews at $99/month thereafter)…" → `partial`.

**Why it earns a block:** it's the structural opposite of the GLP-1 page — one molecule, one form, but the head
of a **3-form NAD+ family** (injection → nasal spray → face cream) that the roster lists as separate slugs; the
"$15/shot" + "$119 first month" pairing shows Eden's intro-price-with-withheld-recurring pattern that (with the
membership) makes the line `partial`.

### My Custom Hair Growth Kit for Men — the multi-ingredient kit (mixed forms in one SKU)

- **Parent:** Hair Growth · **slug:** `/treatment/hair-growth-kits-for-men` · **price:** `From $83/month` ·
  **visibility:** `partial` · **form:** pill + topical-gel · **category:** hair-loss

> **Page anatomy (in order):** mega-nav → **H1 "My Custom Hair Growth Kit" / "Built for Men"** → **"From
> $83/month"** → Klarna/Afterpay + FSA/HSA → benefit icons ("Combines targeted internal treatment and external
> scalp care" / "Premium, clinically-backed ingredients") → **kit composition** (below) → "How do Finasteride,
> Minoxidil, and GHK-Cu support hair health?" Q&A → benefit tiles → **"Lab tested for quality & potency"** panel
> (Potency / Sterility / Endotoxicity — Passed) → ISI + membership footnote.
> **Kit composition (verbatim):** "My Custom Hair Growth Kit for Men **may include a combination** of the
> following treatments, prescribed based on your clinical evaluation: **Oral Finasteride** (FDA-approved for
> male pattern hair loss) · **Oral Minoxidil** (off-label) · **GHK-Cu Foam** (a topical copper peptide)."
> **Form honesty (verbatim):** "Easy oral tablet + quick-absorbing cosmetic foam." → two delivery mechanisms in
> one SKU (`pill + topical-gel`).
> **Compliance (verbatim):** "Oral Finasteride is FDA-approved for male-pattern hair loss. GHK-Cu Foam is a
> non-drug cosmetic and not approved to treat or prevent hair loss."

**Why it earns a block:** it's the only roster shape that bundles **multiple molecules across two delivery
forms** into one buyable, so the single `Form` cell ("pill + topical-gel") and the single `hair-loss` category
can't carry the composition — the block makes the kit's three page-attested ingredients explicit, and shows the
women's twin (`/treatment/hair-growth-kits-for-women`) is the *same* kit minus finasteride (minoxidil + GHK-Cu).

## Provenance

- **Pages read — 25 fresh PDP captures + 1 census map, all `captures/2026-06-03/`:** every `/treatment/*` PDP
  (the 3 deep-dives — `glp1-treatments`, `nad`, `hair-kit-men` — captured rich via `--homepage`: rawHtml +
  full-page screenshot + `onlyMainContent:false`; the other 22 via standard scrape: markdown + links +
  screenshot). Context: `store/eden-health/profile.md` (2026-05-30) + the prior 2026-05-30 homepage/about/faq/
  glp1/reviews captures. **Verify:** 25/25 sourceURLs matched, all 25 bodies md5-unique (no geo/cache
  contamination). **Credits this run: 27** (1 census map + 1 `treatment` search map + 25 PDP scrapes, 1 each).
- **Completeness — high confidence.** The roster was reconciled across two independent sources that **agreed
  exactly**: (a) the homepage mega-nav's enumerated treatment links, and (b) the `/v2/map` census
  (`includeSubdomains:false`), which returned **25 `/treatment/*` URLs — the same 25**. Eden is a **Webflow**
  site, so the CMS-REST rung (WordPress `/wp-json`, Shopify `/products.json`) **does not apply** — Webflow has
  no public catalog API; the nav + map census are the authoritative backbone here. The `treatment` search-map
  pass returned only SEO blog noise (`/post/*`) and surfaced no new SKUs. **What I couldn't reach:** the two
  compounded GLP-1 sub-SKUs (Semaglutide/Tirzepatide) are configured *on* the hub page, not separate PDPs —
  priced from the hub carousel, not an own slug.
- **Dedup / excluded as funnel variants (not separate offerings):** `/shop/compounded-tirzepatide-m`,
  `/offer/glp1micro`, `/weight`, `/weight-loss`, `/weight-loss-quiz` — marketing/quiz landing pages for the
  GLP-1 line, the same SKUs at different URLs. Intake/checkout (`app.eden.health`, `tryeden.com/intake/*`,
  `app.tryeden.com`) not entered.
- **Gated / unreachable:** the **real all-in** for any SKU (med price + the $99/mo membership + the post-intro
  recurring rate behind every "first month" price); which exact molecule a branded GLP-1 contains beyond what
  the page states (Ozempic/Mounjaro left "not stated"); the personalized composition + dose of the two kits and
  Everyday+/Hormone Kit (set at consult); whether the non-Rx Cell Theory truly requires a membership (footnote
  is generic boilerplate).
- **Point-in-time snapshot, not fixed:** Eden runs promo/intro pricing ("first month" rates recur across the
  catalog) and the profile flags this Webflow catalog as funnel-heavy; this module's own `captured_at` + a short
  TTL are the guard — re-capture before trusting a price as current. The "Same Price at Every Dose" guarantee
  means the *med* price is dose-stable, but the membership and intro-vs-recurring gap are the moving parts.
