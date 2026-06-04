---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: mydrhank.com         # company key; each offering's slug (its relative url) is its key *within* MyDrHank
captured_at: 2026-06-03      # own freshness; captures/2026-06-03/ holds the source pages
---

## Portfolio overview

MyDrHank (mydrhank.com; "MyDrHank Telehealth Plaform" [sic, per the `<title>`]) is a D2C telehealth Rx brand
selling **compounded** medications through a free online intake → U.S.-licensed provider review → ship-to-door.
The storefront is a **custom React/Vite SPA** (hashed `/assets/index-*.js`; no WordPress/Shopify/Next backend —
see Provenance), and the **entire catalog is a hard-coded data array inside that JS bundle**, not a CMS. This
doc enumerates the **complete roster: 16 buyable Rx SKUs** across **5 lines** — Weight Loss (GLP-1), Longevity,
Sexual Health, Hair Growth, and a one-product "Strength" line (Sermorelin). **15 SKUs are shown in the nav; the
16th (`/products/hair-combo`) is a live PDP the bundle deliberately filters out of every menu** — the one SKU
the grid hides (see anchors). Every line sells the same way: a category page (non-buyable, except "Strength"
has no page) → product cards → a SKU PDP with its own slug + a single `From $X/mo` price → a free, gated online
intake sets the binding plan.

**Shape finding #1 — the bundle *is* the catalog; the nav hides one SKU.** There is no `/products.json`,
`/wp-json`, or sitemap; the SPA serves its `index.html` shell (HTTP 200) for *any* unmatched path, so the
authoritative product list is the `Ep=[{slug,name,category,…}]` registry inside `assets/index-BgxAAauF.js`. It
holds 15 entries; the nav swaps the registry's `hair-combo` ("3-in-1 Hair Combo") for a hand-built
`custom-hair-protocol` entry and **explicitly filters `hair-combo` out** (`Ep.filter(d=>d.slug!=="hair-combo")`).
`hair-combo` still renders as a full live PDP at `/products/hair-combo` (`From $52/mo`) — a distinct SKU (fixed
3-in-1 combo) from the visible `custom-hair-protocol` (a 5-formulation custom quiz), not a dupe. Net true
catalog: **16 buyable SKUs.**

**Shape finding #2 — one visibility pattern site-wide: floors, no flats, no membership.** *Every* SKU's price
is rendered **"From $X/mo"** — an explicit floor — with **"Free consultation"** beside it. There is **no
membership tier, no separate consult fee, and no drug-bought-elsewhere** anywhere on the site (a structural
contrast with cohort peers Hone/Hims, whose `$X + membership` stacks drive their `partial` calls). The gap
between the shown floor and the real all-in is **dose / plan / formulation chosen inside the gated intake** —
e.g. Compounded Tirzepatide's `+ B-12 / + Glycine` toggle and "dose is optimized" titration. **My visibility
rule (stated once, applied to all 16): a `From $X` floor whose self-contained all-in is only set behind the
intake = `partial`; a flat, fully-shown number = `published`.** Because the binding price is gated and the
displayed number is explicitly a floor, **all 16 SKUs are `partial`; none qualifies as `published`.** The
underlying mechanic (universal "From" floor · free consult · no membership) is quoted verbatim under anchors so
the call stays recoverable in a cross-brand comparison.

**Shape finding #3 — everything is compounded + Rx-gated, free consult, no membership.** Every PDP carries the
verbatim *"Compounded medications are not FDA-approved…"* line and routes through a *"~5 minute"* online
questionnaire → provider review *"within 48 hours"* → ship from an *"FDA-registered U.S. pharmacy."* Even the
"FDA-approved active ingredient" SKUs (minoxidil, finasteride) are dispensed as compounded products. There is
no upsell membership — the consult and shipping are free; you pay only the medication floor.

**Prominence (calibrated).** **Weight Loss / GLP-1 is the flagship [HIGH]** — the homepage's own eyebrow over
the hero is *"our most popular treatment"* above *"## GLP-1s for weight loss,"* it leads the nav, it is the
**only line whose category page shows prices** (the other three hide them), and it owns the homepage's
interactive weight-loss calculator. **Nav/section order [MED]:** Weight Loss → Longevity → Sexual Health → Hair
Growth → Strength, so Longevity reads second and Sexual Health third. **Sermorelin ("Strength") is the lightest
line [MED→LOW]** — a single SKU with **no category page** (registry category "Growth & Recovery," nav label
"Strength"). **Card order within a category is [LOW]** — and the bundle ships `/glp/lp/v1–v3` and
`/sermorelin/lp/v1–v2` landing-page variants + GTM, so marketing copy is A/B-tested; treat IA as a snapshot
(prices, though, are hard-coded in the bundle — stable per deploy, not server-flickered).

## Roster

Complete at the indexed (PDP) level — **16 buyable SKUs across 5 lines**, reconciled against the bundle's
product registry (the authoritative backend here). Within-company key = **Slug** (the relative URL, quoted
exactly). Price quoted verbatim with its on-page "From" marker. **Form** = the page-attested delivery mechanism
as the Notion Delivery-Mechanisms slug; **Category** = the SKU's best-fit Notion Product-Category (slugified),
grounded in the site's own line (Parent). **What** leads with the molecule **as the page prints it** (never
inferred from the brand — see the molecule audit under anchors); `not stated` where the page names none. An
offering here is never asserted equal to a same-molecule offering at another brand.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | Form | Category | What (molecule · access) |
|---|---|---|---|---|---|---|---|---|
| Weight Loss | family | — | `/weight-loss` | — | — | — | `glp-1-medical-weight-loss` | GLP-1 line; the flagship — "our most popular treatment." 3 SKUs, oral + injectable. |
| Oral Semaglutide | buyable | Weight Loss | `/products/oral-semaglutide` | `From $171/mo` | partial | `pill` | `glp-1-medical-weight-loss` | semaglutide + low-dose ondansetron · daily compounded tablet; gated intake. Anti-nausea co-formulation. |
| Compounded Semaglutide | buyable | Weight Loss | `/products/compounded-semaglutide` | `From $178/mo` | partial | `injection` | `glp-1-medical-weight-loss` | semaglutide + vitamin B-12 · weekly injection · gated intake. |
| Compounded Tirzepatide | buyable | Weight Loss | `/products/compounded-tirzepatide` | `From $240/mo` | partial | `injection` | `glp-1-medical-weight-loss` | tirzepatide + vitamin B-12 (or `+ Glycine` variant) · weekly injection · gated; dose optimized over time. [deep] [anchor: from-floor] |
| Longevity | family | — | `/longevity` | — | — | — | `nad` | NAD+ / antioxidant line; 4 SKUs, nasal-spray + injection pairs. |
| NAD+ Nasal Spray | buyable | Longevity | `/products/nad-nasal-spray` | `From $137/mo` | partial | `nasal-spray` | `nad` | NAD+ · nasal spray ("no needles") · gated. |
| NAD+ Injection | buyable | Longevity | `/products/nad-injection` | `From $155/mo` | partial | `injection` | `nad` | NAD+ · subcutaneous injection ("maximum-potency") · gated. |
| Glutathione Nasal Spray | buyable | Longevity | `/products/glutathione-nasal-spray` | `From $103/mo` | partial | `nasal-spray` | `longevity-rx-non-nad` | glutathione · nasal spray · gated. "Master antioxidant." |
| Glutathione Injection | buyable | Longevity | `/products/glutathione-injection` | `From $103/mo` | partial | `injection` | `longevity-rx-non-nad` | glutathione · injection ("maximum-strength") · gated. |
| Sexual Health | family | — | `/sexual-health` | — | — | — | `ed` | Men's ED line; 4 SKUs, all PDE5 inhibitors. |
| MDH Drive | buyable | Sexual Health | `/products/2-in-1-rdt` | `From $45/mo` | partial | `sublingual-troche` | `ed` | sildenafil + tadalafil · rapid-dissolve tablet — "dissolves under the tongue," works in 15 min · gated. [deep] |
| Generic Sildenafil | buyable | Sexual Health | `/products/sildenafil` | `From $25/mo` | partial | `pill` | `ed` | sildenafil ("the active ingredient in Viagra®") · tablet · gated. |
| Generic Tadalafil | buyable | Sexual Health | `/products/generic-tadalafil` | `From $30/mo` | partial | `pill` | `ed` | tadalafil ("the active ingredient in Cialis®") · as-needed tablet, up to 36h · gated. |
| Daily Tadalafil | buyable | Sexual Health | `/products/daily-tadalafil` | `From $35/mo` | partial | `pill` | `ed` | tadalafil, low daily dose · once-daily tablet · gated. |
| Hair Growth | family | — | `/hair-growth` | — | — | — | `hair-loss` | Hair-loss line; 3 visible SKUs + 1 hidden (`hair-combo`). |
| Custom Hair Protocol | buyable | Hair Growth | `/products/custom-hair-protocol` | `From $41/mo` | partial | `pill`/`topical-gel` (varies) [?] | `hair-loss` | molecule **not stated** — "five compounded formulations," men "include finasteride," female-safe options · "oral or topical — tablets, capsules, and sprays" · quiz-gated (Formula Finder). [deep] |
| Minoxidil | buyable | Hair Growth | `/products/minoxidil` | `From $30/mo` | partial | `pill` | `hair-loss` | minoxidil — **oral** ("convenient oral tablet… no messy topicals") · daily tablet · gated. |
| Finasteride | buyable | Hair Growth | `/products/finasteride` | `From $38/mo` | partial | `pill` | `hair-loss` | finasteride · tablet · gated. "Lowers DHT by up to 70%." |
| 3-in-1 Hair Combo | buyable (hidden) | Hair Growth | `/products/hair-combo` | `From $52/mo` | partial | `pill` | `hair-loss` | minoxidil + finasteride + biotin · one daily tablet · gated; "Not for use by women." **Registry SKU filtered out of the nav** — live PDP only. [anchor: hidden] |
| Strength | family | — | (no category page — nav label only) | — | — | — | `peptides` | One-product line; registry category "Growth & Recovery." |
| Sermorelin | buyable | Strength | `/products/sermorelin` | `From $137/mo` | partial | `injection` | `peptides` | sermorelin — "a growth hormone-releasing peptide" · injectable · gated. "Fewer side effects than synthetic HGH." |

**Buyable count: 16** (3 Weight Loss + 4 Longevity + 4 Sexual Health + 4 Hair Growth incl. the hidden
`hair-combo` + 1 Sermorelin). The 5 `family` rows are non-buyable groupings, not counted.

### Verbatim anchors

The footnotes the Price/Visibility columns point at — they decide the universal `partial` call and carry the
molecule-sourcing + hidden-SKU audit. Quoted exactly from the cited captures.

- **[anchor: from-floor] The universal "From" floor + free consult + no membership (decides `partial`).**
  Every PDP renders the price block as **`From$X/mo`** immediately beside **"No insurance required · Free
  consultation · Transparent pricing · Free delivery."** No page anywhere shows a flat self-contained price, a
  membership, or a consult fee. The all-in is set inside the gated intake: Compounded Tirzepatide's PDP offers
  *"Choose your formulation — + B-12 / + Glycine"* and its timeline says *"Progressive weight loss as **dose is
  optimized**"* — i.e. the `From $240` is the entry floor, not the bound price. Applied uniformly: a `From $X`
  floor with the binding number behind the intake → **`partial`** for all 16. (Contrast Hone/Hims, where
  `partial` comes from a `+ membership` stack — MyDrHank has none; its gap is dose/plan only, but the displayed
  number is still a floor, not the all-in.)
- **[anchor: hidden] The one SKU the grid hides — `/products/hair-combo`.** The bundle's product registry
  `Ep=[…]` lists `{slug:"hair-combo",name:"3-in-1 Hair Combo",category:"Hair Growth"}`, but both the nav and the
  Hair-Growth category page build their lists with `…Ep.filter(d=>d.slug!=="hair-combo")` and inject a separate
  hand-built `custom-hair-protocol` tile in its place. So `hair-combo` appears in **no** menu — yet
  `/products/hair-combo` returns a complete live PDP (H1 *"3-in-1 Hair Combo"*, *"Minoxidil + Finasteride +
  Biotin in one daily tablet,"* `From$52/mo`, *"Not for use by women"*). It is a **distinct SKU** from the
  visible `custom-hair-protocol` (a 5-formulation custom quiz at `From$41/mo`), not a marketing dupe — listed
  on its own row, marked hidden.
- **Molecule sourcing (page-attested-only rule, audited).** Every molecule in the roster is named on the SKU's
  own PDP: **semaglutide** (*"semaglutide combined with a low dose of ondansetron"*; *"semaglutide and vitamin
  B-12"*); **tirzepatide** (*"tirzepatide and vitamin B-12"*); **NAD+**, **glutathione** (named in their H1s);
  **sildenafil/tadalafil** (*"Sildenafil + Tadalafil"*; *"the active ingredient in Viagra®/Cialis®"*);
  **minoxidil + finasteride + biotin** (*"Minoxidil + Finasteride + Biotin in one daily tablet"*);
  **sermorelin** (*"a growth hormone-releasing peptide"*). **`custom-hair-protocol` → "not stated"** — the PDP
  names no specific molecule ("five compounded hair-loss formulations"; only "men… include finasteride" as an
  aside), so the SKU's molecule is recorded `not stated`, not inferred.
- **Form note — MDH Drive is page-attested sublingual.** The RDT maps to `sublingual-troche` on the page's own
  words, not a guess: *"Sublingual absorption — Dissolves under the tongue for faster entry into the
  bloodstream."* **`custom-hair-protocol` form is genuinely multi-mechanism** — *"Oral or topical — tablets,
  capsules, and sprays"* — so no single Delivery-Mechanism slug fits; recorded `pill`/`topical-gel` (varies)
  with a `[?]`.

## Deep blocks

Three earned blocks, spanning three forms/categories — they carry what a roster row can't: the flagship's
visibility mechanic, a sublingual combo's anatomy, and a quiz-gated SKU with no single molecule.

### Compounded Tirzepatide — the flagship, and the `From`-floor mechanic in full

- **Parent:** Weight Loss · **slug:** `/products/compounded-tirzepatide` · **price:** `From $240/mo` ·
  **visibility:** `partial` · **form:** `injection` · **category:** `glp-1-medical-weight-loss`

> **H1:** "Compounded Tirzepatide" (eyebrow: "Weight Loss · Compounded injectable GLP-1/GIP with B-12")
> **Formulation toggle (verbatim):** "Choose your formulation — **+ B-12 / + Glycine**. One weekly injection —
> tirzepatide and vitamin B-12 in a single compounded dose."
> **Price block (verbatim):** "**From$240/mo** · No insurance required · Free consultation · Transparent
> pricing · Free delivery."
> **Molecule (page-attested):** "A single compounded injection — **tirzepatide** combined with vitamin B-12…";
> "Tirzepatide targets both GLP-1 and GIP receptors."
> **The floor moves (verbatim):** timeline reads "Weeks 8–16 — Progressive weight loss as **dose is
> optimized**"; the headline claim is footnoted "of FDA-approved tirzepatide at **highest dose (15mg)**.
> Compounded tirzepatide is not FDA-approved."
> **Gating (verbatim):** "Step 1 Online Questionnaire… 100% online, takes about 5 minutes. Step 2 Provider
> Review… Step 3 Delivered to Your Door. If prescribed, your medication ships discreetly from an FDA-registered
> pharmacy."

**Why it earns a block:** it is the flagship (homepage "our most popular treatment") and it makes the site-wide
`partial` call legible — a `+ B-12 / + Glycine` formulation choice **and** explicit dose optimization sit
behind a free, gated intake, so the shown `$240` is a floor, never the all-in. This is the figure a
cheapest-compounded-tirzepatide comparison turns on, and the reason it's `partial` not `published`.

### MDH Drive — a sublingual ED combo (the structurally different PDP)

- **Parent:** Sexual Health · **slug:** `/products/2-in-1-rdt` · **price:** `From $45/mo` · **visibility:**
  `partial` · **form:** `sublingual-troche` · **category:** `ed`

> **H1:** "MDH Drive" (eyebrow: "Sexual Health")
> **Molecule + form (verbatim):** "**Sildenafil + Tadalafil** in a rapid-dissolve tablet — works in 15
> minutes"; "**Sublingual absorption** — Dissolves under the tongue for faster entry into the bloodstream";
> "Dual PDE5 inhibition — Sildenafil provides fast onset while tadalafil extends the window… up to 36 hours."
> **Price block (verbatim):** "**From$45/mo** · No insurance required · Free consultation · Transparent
> pricing."
> **Compounding disclosure (verbatim):** "This is a compounded medication. Compounded drugs are not
> FDA-approved… not equivalent to any FDA-approved drug. Compounded in an FDA-registered U.S. pharmacy."

**Why it earns a block:** the slug `2-in-1-rdt` is opaque and the form is non-obvious — the deep read is what
attests **two molecules in one sublingual rapid-dissolve tablet**, fixing both the `sublingual-troche` Form and
the dual-molecule `What` that a one-line roster cell would flatten.

### Custom Hair Protocol — a quiz-gated SKU with no single molecule or form

- **Parent:** Hair Growth · **slug:** `/products/custom-hair-protocol` · **price:** `From $41/mo` ·
  **visibility:** `partial` · **form:** `pill`/`topical-gel` (varies) `[?]` · **category:** `hair-loss`

> **H1:** "One protocol. Built for your scalp." (eyebrow: "Custom Formulation · Hair Loss")
> **Molecule = not stated (verbatim):** "a licensed provider matches you to **one of five compounded hair-loss
> formulations**"; "**Oral or topical** — tablets, capsules, and sprays — male and female-safe options."
> **Quiz gating (verbatim):** "Formula Finder — Find the formulation built for you. **Three short questions.**
> We'll surface the one or two physician-grade formulations that best match your biology… Step 01 Who is this
> protocol for? **Men** (Includes finasteride options) / **Women** (Female-safe formulations only)."
> **Price (verbatim):** "**From $41/month** — compounded in FDA-registered U.S. pharmacies, shipped discreetly."

**Why it earns a block:** it is the SKU a roster row genuinely can't carry — **no single molecule** (five
formulations, only "finasteride options" named in passing → `not stated`) and **no single form** ("oral or
topical" → the Form `[?]` flag). The deep read is what justifies both flags and records that the SKU resolves
to a specific formulation only *after* a gated quiz — so even its molecule and form, not just its price, are
set behind the intake.

## Provenance

- **Pages read (22 captures, all `captures/2026-06-03/`):** `homepage.md`; 4 category pages
  (`category-weight-loss`, `category-longevity`, `category-sexual-health`, `category-hair-growth`); and **16
  PDPs** — one per buyable SKU (`pdp-oral-semaglutide`, `pdp-compounded-semaglutide`, `pdp-compounded-tirzepatide`,
  `pdp-nad-nasal-spray`, `pdp-nad-injection`, `pdp-glutathione-nasal-spray`, `pdp-glutathione-injection`,
  `pdp-2-in-1-rdt`, `pdp-sildenafil`, `pdp-generic-tadalafil`, `pdp-daily-tadalafil`, `pdp-custom-hair-protocol`,
  `pdp-minoxidil`, `pdp-finasteride`, `pdp-sermorelin`, `pdp-hair-combo`). All 16 PDPs returned unique content
  md5s (no geo/cache contamination). **Spend: 22 Firecrawl credits** (1 map + 1 homepage + 4 category + 16 PDP);
  this is a fresh per-SKU capture (no warm profile.md existed for this domain).
- **Sources reconciled for completeness (4 ways):** (1) the rendered **homepage + nav** (5 lines, 15 product
  cards); (2) the **no-search `/map` census** (12 URLs — sparse, but surfaced the root marketing variants
  `/generic-sildenafil`, `/generic-tadalafil` and the `/cloud/new-product-cards-*` builder pages); (3) the
  **JS-bundle product registry** `Ep=[…]` + the React-Router route table inside `assets/index-BgxAAauF.js` —
  the authoritative backend, which revealed the **hidden `hair-combo` SKU** and confirmed the 16-SKU total; (4)
  **per-SKU PDP scrapes** for verbatim prices/molecules/forms. Conventional CMS backends were probed and **do
  not exist**: `/products.json` → 404, `/sitemap.xml` → 404, and `/wp-json/wp/v2/types` returns the SPA's
  `index.html` shell (a **soft-200**, not WordPress) — the site is a custom React/Vite SPA whose catch-all
  serves HTTP 200 + HTML for every unmatched path.
- **Confidence the roster is complete: HIGH.** The bundle's hard-coded `Ep` registry is the single source of
  product truth (no runtime product API; `/api/broadcast` is the only API reference and is non-catalog), and it
  enumerates exactly 16 distinct buyable slugs — every one captured. The dedup is clean: root `/generic-*` and
  `/glp/lp/*`, `/sermorelin/lp/*`, `/promo`, `/home` are marketing/landing variants of catalogued PDPs (handled
  by the catch-all, not distinct SKUs), and `custom-hair-protocol` vs `hair-combo` are two real SKUs, not one.
- **Gated / unreachable:** the binding all-in price for every SKU (dose/plan/formulation set inside the
  `join.mydrhank.com` intake — never shown on the marketing site); Compounded Tirzepatide's `+ B-12` vs
  `+ Glycine` price delta (both display the same `From $240`); the per-dose price ladder behind each "From"
  floor.
- **Point-in-time snapshot, not fixed:** prices are hard-coded in the JS bundle, so they're stable per deploy
  (no server-side A/B flicker), but the bundle ships `/glp/lp/v1–v3` + `/sermorelin/lp/v1–v2` landing variants
  and GTM — marketing copy/IA is A/B-tested. This module's own `captured_at` + a short TTL are the guard;
  re-capture before trusting a price as current.
