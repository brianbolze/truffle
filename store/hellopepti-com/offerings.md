---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.2"
domain: hellopepti.com
captured_at: 2026-06-09
enumeration: indexed-complete
site_notes: "Roster backbone = the 11 /category/<slug> pages, which render ALL their cards server-side (name + /peptide/<slug> + $X/mo + 'Popular' badge + descriptor) — the homepage '## All treatments' grid is JS-tabbed and shows only the active tab. All 40 base PDPs at /peptide/<slug>; +50 /peptide/<slug>/<state> availability variants are roster noise. Prices are a single clean monthly med figure on both card and PDP (card == PDP base); every PDP adds 3-mo (−10%) / 6-mo (−15%) prepay tiers. A mandatory $99 one-time onboarding fee precedes any monthly price (/how-it-works) — not a recurring membership."
---

## Portfolio overview

Pepti runs a **flat, 40-SKU compounded-Rx + cosmetic/supplement catalog** across 11 marketed categories — the explicit "one platform, every category" wedge. Every SKU is an individually-priced monthly subscription; there is **no recurring membership**, but a **$99 one-time onboarding fee** (covers the physician evaluation) gates the entire catalog before any monthly price applies. Pricing is uniform in structure: one monthly med price shown on card + PDP, with 3-month (−10%) and 6-month (−15%) prepay tiers. **All 40 prices are `published`** — fully shown, self-contained monthly figures (the $99 is disclosed site-wide and carried in *Verbatim anchors*, not a per-SKU hidden cost).

Prominence read (the site's own signals):
- **Weight loss / GLP-1 leads** `[HIGH]` — the title tag leads "GLP-1," weight loss is the first category, and Semaglutide/Tirzepatide head the "Most popular" rail and the all-treatments grid's default tab.
- **"Popular" badges** `[HIGH]` (company's own label) on 11 SKUs: lipo-b, semaglutide, melanotan-i, trt-cypionate, trt-cypionate-ai, enclomiphene, bhrt-bi-est, bhrt-progesterone, bhrt-bundle, tretinoin-ghkcu-cream, methylene-blue, sildenafil-troche, tadalafil-troche.
- **Hormones is the deepest line** `[MED]` — 15 of 40 SKUs (men's TRT + women's BHRT + fertility), by count the catalog's center of gravity.
- Self-reported breadth claims **conflict**: this grid enumerates **40**; /about says **"90+ peptide therapies"**; /press says **"50+ treatments."** Roster trusts the enumerated 40.

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Semaglutide | buyable | — | /peptide/semaglutide | $349/mo | published | semaglutide · subcutaneous injection · Rx (provider review) — GLP-1 receptor agonist, weight management |
| Semaglutide (Oral) | buyable | — | /peptide/semaglutide-oral | $299/mo | published | semaglutide · oral tablet · Rx — "same active ingredient," needle-free |
| Tirzepatide | buyable | — | /peptide/tirzepatide | $399/mo | published | tirzepatide · subcutaneous injection · Rx — dual GIP/GLP-1 agonist |
| Tirzepatide (Oral) | buyable | — | /peptide/tirzepatide-oral | $349/mo | published | tirzepatide · oral tablet · Rx — dual GIP/GLP-1, needle-free |
| Lipo-B (B12 + MIC) | buyable | — | /peptide/lipo-b | $99/mo | published | methionine + inositol + choline + B12 · injection · Rx — fat-metabolism/energy ★Popular |
| L-Carnitine Injection | buyable | — | /peptide/l-carnitine | $119/mo | published | L-carnitine 500mg/ml · injection · Rx — fat-burner/recovery |
| Testosterone Cypionate | buyable | — | /peptide/trt-cypionate | $149/mo | published | testosterone cypionate · injection (or cream) · Rx — standard TRT (Schedule III) ★Popular |
| TRT + Anastrozole | buyable | — | /peptide/trt-cypionate-ai | $179/mo | published | testosterone + anastrozole · injection · Rx — TRT w/ estrogen control ★Popular |
| Testosterone Low-Dose | buyable | — | /peptide/trt-low-dose | $129/mo | published | testosterone · low-dose · Rx — for women / sensitive patients |
| Testosterone Cream | buyable | — | /peptide/trt-cream | $149/mo | published | testosterone · topical cream · Rx — needle-free TRT |
| Anastrozole | buyable | — | /peptide/anastrozole | $79/mo | published | anastrozole · oral · Rx — aromatase inhibitor / estrogen control |
| Enclomiphene | buyable | — | /peptide/enclomiphene | $119/mo | published | enclomiphene · oral · Rx — natural testosterone booster ★Popular |
| Clomiphene | buyable | — | /peptide/clomiphene | $89/mo | published | clomiphene · oral · Rx — fertility / natural-T support |
| Gonadorelin | buyable | — | /peptide/gonadorelin | $179/mo | published | gonadorelin · injection · Rx — hormone support & fertility |
| HCG | buyable | — | /peptide/hcg | $199/mo | published | hCG · injection · Rx — hormone optimization & fertility |
| Bi-Est Cream (BHRT) | buyable | — | /peptide/bhrt-bi-est | $129/mo | published | bi-est (estriol/estradiol) · cream · Rx — bioidentical estrogen, women ★Popular |
| Bioidentical Progesterone | buyable | — | /peptide/bhrt-progesterone | $119/mo | published | progesterone · (oral/cream) · Rx — hormone balance, women ★Popular |
| Estradiol | buyable | — | /peptide/bhrt-estradiol | $99/mo | published | estradiol · capsules or cream · Rx — bioidentical estradiol |
| Testosterone for Women (Low-Dose) | buyable | — | /peptide/bhrt-trt-women | $119/mo | published | testosterone · low-dose · Rx — libido/energy, women |
| Complete BHRT Bundle | buyable | — | /peptide/bhrt-bundle | $249/mo | published | bi-est + progesterone + testosterone · bundle · Rx — women's HRT stack ★Popular |
| Natural Desiccated Thyroid | buyable | — | /peptide/natural-thyroid | $79/mo | published | desiccated thyroid (T4/T3) · oral · Rx — whole-thyroid replacement |
| Sermorelin | buyable | — | /peptide/sermorelin | $229/mo | published | sermorelin · capsule or injection · Rx — GH secretagogue |
| Hexarelin | buyable | — | /peptide/hexarelin | $239/mo | published | hexarelin · injection · Rx — GH secretagogue, recovery/anti-aging |
| NAD+ Injection | buyable | — | /peptide/nad-injection | $279/mo | published | NAD+ · injection · Rx — cellular energy & repair |
| NAD+ Capsules | buyable | — | /peptide/nad-oral | $159/mo | published | NAD+ · oral capsule · (supplement) — cellular energy |
| Glutathione | buyable | — | /peptide/glutathione | $199/mo | published | glutathione · injection · — master antioxidant / detox |
| GHK-Cu Capsules | buyable | — | /peptide/ghk-cu-oral | $149/mo | published | GHK-Cu copper peptide · oral capsule · — skin & systemic support |
| PT-141 | buyable | — | /peptide/pt-141 | $279/mo | published | PT-141 (bremelanotide) · injection or troche · Rx — sexual wellness |
| Trimix Injection | buyable | — | /peptide/trimix | $199/mo | published | tri-mix (alprostadil/papaverine/phentolamine) · injection · Rx — ED, harder cases |
| Sildenafil Troche | buyable | — | /peptide/sildenafil-troche | $199/mo | published | sildenafil · sublingual troche · Rx — "generic Viagra" ★Popular |
| Tadalafil Troche | buyable | — | /peptide/tadalafil-troche | $89/mo | published | tadalafil · sublingual troche · Rx — "generic Cialis" ★Popular |
| Oxytocin | buyable | — | /peptide/oxytocin | $229/mo | published | oxytocin · (nasal/troche) · Rx — connection & bonding |
| GHK-Cu (Topical Cream) | buyable | — | /peptide/ghk-cu-topical | $169/mo | published | GHK-Cu copper peptide · topical cream · — anti-aging skin |
| Tretinoin + GHK-Cu Cream | buyable | — | /peptide/tretinoin-ghkcu-cream | $149/mo | published | tretinoin + GHK-Cu · cream · Rx — anti-aging ★Popular |
| Hydroquinone Cream (Rx) | buyable | — | /peptide/hydroquinone-cream | $149/mo | published | hydroquinone · cream · Rx — skin lightening |
| Clarity Cream (Acne Rx) | buyable | — | /peptide/clarity-cream | $109/mo | published | triple-action acne (not stated per-ingredient) · cream · Rx |
| Luminous Brightening Gel | buyable | — | /peptide/luminous-gel | $149/mo | published | kojic acid + tranexamic acid + tretinoin · gel · Rx — brightening |
| Melanotan I | buyable | — | /peptide/melanotan-i | $249/mo | published | melanotan I (afamelanotide-class) · injection · Rx — pigmentation/tanning ★Popular |
| Methylene Blue | buyable | — | /peptide/methylene-blue | $109/mo | published | methylene blue · (oral) · — mitochondrial / cognitive ★Popular |
| Methylcobalamin (Active B12) | buyable | — | /peptide/methylcobalamin | $129/mo | published | methylcobalamin (active B12) · injection · — energy & cognition |

### Verbatim anchors

- **Universal onboarding fee:** *"$99 to get started… one-time onboarding fee… covers the physician evaluation"* — /how-it-works. *"No hidden fees. Just two costs… Onboarding $99 one-time… [then] transparent monthly pricing on every medication."* Applies before **every** monthly price above; it's a one-time platform fee, not a per-SKU recurring cost, so the monthly figures remain `published`.
- **Prepay tiers (every PDP):** *"Monthly · 3 months Save 10% · 6 months Save 15%"* — the quoted `$X/mo` is the monthly base; the discount tiers reduce the effective monthly on prepay.
- **Compounded-vs-brand framing** (PDP cost compares, self-reported): Semaglutide *"$1349 per month at brand-name pricing"* vs *"$349 — same active ingredient, ~75% less"*; Tirzepatide *"$1429"* vs *"$399 — ~72% less."*
- **Brand-name GLP-1 (separate, NOT in this cash-pay roster):** Zepbound/Wegovy/Mounjaro/Ozempic offered via insurance **/coverage-check** only — *"pepti providers may prescribe FDA-approved brand-name GLP-1 medications when clinically appropriate."* No cash price; routed to a retail pharmacy that accepts the plan. Excluded from the roster (no published price; insurance-gated → would be `on-request`).
- **Molecule sourcing note:** each SKU's molecule = the product page's own H1/name (page-attested, not inferred). `clarity-cream` ("triple-action acne") and `oxytocin`/`methylene-blue` forms are stated only loosely on the captured pages — forms in parentheses are best-read from descriptor, not a per-SKU PDP attestation.

## Deep blocks

**None earned by ambiguity** — the roster is uniform (clean `published` monthly price per SKU, molecule = page name), so no per-SKU disambiguation block is warranted. The one cross-cutting finding (the $99 onboarding gate + prepay tiers + the brand-vs-compounded cost framing) is captured in *Verbatim anchors* above. Flagship PDPs captured for evidence (tirzepatide, semaglutide, trt-cypionate, pt-141, sermorelin) sit verbatim in `captures/2026-06-09/`.

## Provenance

- **Pages read** (cited captures): `captures/2026-06-09/cat_{hormones, anti-aging, skin-hair, gh-support, intimacy, cognitive, recovery, immune}.md` (roster backbone — all cards) + `captures/2026-06-07/homepage.md` (weight-loss tab, 6 SKUs) + PDPs `pdp_{tirzepatide, semaglutide, trt-cypionate, pt-141, sermorelin, methylcobalamin}.md`.
- **Scope note:** all **40** distinct SKUs rostered at SKU grain — `enumeration: indexed-complete`. Deliberately not enumerated: the 3-mo/6-mo prepay tiers (leaf dose/quantity grain) and the 50 per-state `/peptide/<slug>/<state>` availability variants (roster noise). The insurance-gated brand-name GLP-1 line is noted but excluded (no published price).
- **Point-in-time:** prices are a 2026-06-09 snapshot; the brand foregrounds GLP-1/weight-loss in a rotating "Most popular" rail, so anchor prominence may shift.
- **Run profile:** Deep run (direct competitor) — backbone via category pages, 5 flagship PDPs deepened for evidence, no per-SKU deep block earned.
