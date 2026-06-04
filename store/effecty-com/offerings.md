---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: effecty.com
captured_at: 2026-06-04
site_notes: "Webflow. The full priced roster renders twice — homepage 'Treatments' grid AND /treatments — so every standard monthly price (1/3/12-mo) reads off those two pages, no PDP needed for the index. PDP-only detail: the GLP-1 page splits into TWO lanes (Compounded GLP-1 vs Compounded GLP-1 + GIP) each with a first-month-promo ladder ($60 first / $160 after, etc.) the grid collapses to one '$160' number. Molecule is NEVER in product copy for the GLP-1 line or the branded pens — only in excluded alt-text (vial/pen labels); record 'not stated'. Prices are point-in-time under the EFFECTY100 first-month promo."
---

## Portfolio overview

Three co-equal `Multi-product` lines — **Weight Loss**, **Longevity**, **Hormone Therapy (menopause)** — 16 buyable SKUs plus a free progesterone companion. The shape finding: this is a **price-transparent, no-membership** roster where the *same* monthly price is shown at every dose, and longer plans step the price down (1-mo → 12-mo). The GLP-1 line is **two lanes** the grid hides behind one "$160" — a base "Compounded GLP-1" and a pricier "Compounded GLP-1 + GIP."

Prominence (de-facto flagship = **GLP-1 / weight loss**):
- GLP-1 / weight-loss owns **100% of testimonials and outcome stats** sitewide — `[HIGH]` (corroborated proof concentration).
- Nav leads with **Weight Loss**; homepage treatment grid leads with **GLP-1 Injection** — `[MED]` (nav/section order).
- The hero H1 rotates across all three verticals (captured "Hormone therapy" / "Longevity" in one run) — so the *hero* reads co-equal, not GLP-1-led — `[LOW]` (rotating/A-B).

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Weight Loss | family | — | /weight-loss | — | — | the weight-loss line (GLP-1 + metformin + FDA-brand pens) |
| GLP-1 Injection | buyable | /weight-loss | /weight-loss/glp-1 | "$205 / $190 / $160 /month" (1/3/12-mo); PDP "Starting at $160/month" | published | molecule **not stated** (copy: "Compounded GLP-1," "weekly GLP-1 injection") · weekly injection · async-Rx, compounded. PDP 2nd lane "Compounded GLP-1 + GIP" → "$305 / $280 / $265 / $240" (1/3/6/12-mo after) |
| Metformin | buyable | /weight-loss | /weight-loss/metformin | "$80 /month" | published | metformin (named in copy) · form not stated · async-Rx |
| Mounjaro® | buyable | /weight-loss | /weight-loss/mounjaro | "$1,300 /month" | published | molecule **not stated** (brand-name SKU; FDA-brand pen) · injection pen · async-Rx |
| Ozempic® | buyable | /weight-loss | /weight-loss/ozempic | "$1,300 /month" | published | molecule **not stated** (brand-name SKU; FDA-brand pen) · injection pen · async-Rx |
| Wegovy® | buyable | /weight-loss | /weight-loss/wegovy | "$1,600 /month" | published | molecule **not stated** (brand-name SKU; FDA-brand pen) · injection pen · async-Rx |
| Zepbound® | buyable | /weight-loss | /weight-loss/zepbound | "$1,400 /month" | published | molecule **not stated** (brand-name SKU; FDA-brand pen) · injection pen · async-Rx |
| Longevity | family | — | /longevity | — | — | the longevity / peptide line |
| NAD+ Injection | buyable | /longevity | /longevity/nad | "$225 / $195 / $160 /month" | published | NAD+ (named in copy) · injection · async-Rx |
| Sermorelin | buyable | /longevity | /longevity/sermorelin | "$225 / $200 /month" | published | sermorelin (named in copy) · injection · async-Rx |
| Sermorelin ODT | buyable | /longevity | /longevity/sermorelin-odt | "$190 / $170 /month" | published | sermorelin (named in copy) · orally-disintegrating tablet (per SKU name) · async-Rx |
| Glutathione | buyable | /longevity | /longevity/glutathione | "$175 / $147 / $125 /month" | published | glutathione (named in copy) · injection · async-Rx |
| NAD+ Nasal Spray | buyable | /longevity | /longevity/nad-nasal-spray | "$180 /month" | published | NAD+ (named in copy) · nasal spray (per SKU name) · async-Rx |
| Lipotropic (MIC) + B12 | buyable | /longevity | /longevity/lipotropic-b12 | "$150 / $109 / $95 /month" | published | lipotropic MIC + B12 (named in copy) · injection · async-Rx |
| Hormone Therapy | family | — | /hormones | — | — | the menopause/HRT line |
| Estradiol Patch | buyable | /hormones | /hormones/estradiol-patch | "$180 / $125 / $105 /month" | published | estradiol (named in copy) · transdermal patch (per SKU name) · async-Rx |
| Estradiol Cream | buyable | /hormones | /hormones/estradiol-cream | "$180 / $125 / $95 /month" | published | estradiol (named in copy) · topical cream (per SKU name) · async-Rx |
| Estradiol Tablet | buyable | /hormones | /hormones/estradiol-tablet | "$140 / $90 / $55 /month" | published | estradiol (named in copy) · oral tablet (per SKU name) · async-Rx |
| Oral Progesterone | buyable | /hormones | (no PDP — added during intake) | "added for free to your treatment plan during your initial intake" | partial | progesterone (named in copy) · oral · companion to systemic estrogen, not sold standalone |

## Verbatim anchors

- **Plan-tier footnotes** (every priced SKU, on homepage + /treatments): `"* Price for purchase of 3 month supply."` and `"* Price for purchase of 12 month supply."` — so a 3-price cell reads **1-mo / 3-mo / 12-mo** (highest → lowest).
- **GLP-1 PDP price ladder** (/weight-loss/glp-1), the detail the grid's single "$160" hides:
  - **Compounded GLP-1** — 12-mo "$60 first month / $160/mo after"; 6-mo "$75 / $175"; 3-mo "$90 / $190"; 1-mo "$105 / $205".
  - **Compounded GLP-1 + GIP** — 12-mo "$140 first month / $240/mo after"; 6-mo "$165 / $265"; 3-mo "$180 / $280"; 1-mo "$205 / $305".
  - `"* Price for purchase of 12 month supply. EFFECTY100 offer valid for first time customers only."` · `"Same price at every dose"` · `"No membership fee"` · `"HSA & FSA eligible"`.
- **Molecule-sourcing audit** (why the "not stated" tags hold): the GLP-1 line's only molecule cues are **alt-text** — an /about-us vial reads *"effecty Liraglutide Rx Injectable,"* and the Ozempic/Mounjaro pen alt-texts read *"semaglutide" / "tirzepatide."* Per the attestation rule, **alt-text is excluded** (only product copy attests), so these are **not stated** in copy; recorded here as non-attesting hints, never inferred onto the SKU. Wegovy/Zepbound carry no molecule cue at all.

## Deep blocks

**One earned — the GLP-1 PDP** (`/weight-loss/glp-1`). It resolves two real ambiguities the roster row can't: (1) the **two-lane split** — the homepage shows one "GLP-1 Injection / $160," but the PDP is actually *Compounded GLP-1* **and** *Compounded GLP-1 + GIP*, a ~$80/mo step up; (2) **promo vs steady-state** — the headline "$160" is the 12-mo *after-promo* monthly, while the first month is "$60" under EFFECTY100. Both lanes' verbatim ladders are quoted in the Verbatim anchors above. Provider voice on-page: *"Dr. Nunzio Pagano, MD, Licensed Physician."* The PDP also carries the company-wide FDA disclaimer (compounded meds not FDA-approved). No PDP-anatomy block and no hero-image capture this run (vanilla offerings scope).

*None earned for the longevity or hormone lines — the roster + the homepage grid carry them (molecule is self-naming in each SKU title; prices are fully published).*

## Provenance

- **Pages read:** homepage, /treatments, /weight-loss/glp-1, /hormones (+ /about-us, /faq for context) — `captures/2026-06-04/`. Every `$` above is greppable in one of these.
- **Scope:** all **16 buyable SKUs + 3 family hubs + 1 free companion** enumerated — complete at the indexed level by blind-source agreement (homepage grid ∩ /treatments grid ∩ /map census all return the same set). Per-SKU PDPs beyond GLP-1/hormones not individually scraped — their prices already publish on the two grids.
- **Gated / unreachable:** nothing price-gated — the whole roster publishes. The `go.effecty.com/start-online-visit/…` intake funnel (where the card hold + eligibility happen) was not entered.
- **Point-in-time caveat:** prices run under the sitewide **EFFECTY100** first-month promo and a rotating hero — a snapshot, re-check next run.
- **Run profile:** vanilla offerings (roster + 1 earned deep block); no PDP-anatomy archetype, no hero images.
