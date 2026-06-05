---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: ivyrx.com
captured_at: 2026-06-04
site_notes: "Catalog = Webflow mega-nav + /treatments (the full price grid; category pages show only a few prices). Most Rx prices are a PDP 'From $X' floor with a templated footnote on every PDP: '$49.75/week = $199/mo (paid upfront with a 12-month plan)' — advertised numbers are per-month floors, lowest rate assumes a 12-month prepay; GLP-1 also scales by dose ('4 doses/month'). /products/glp1-oral-melts 404s (nav-listed, dead PDP). /products/glutathione-nasal-spray serves the glutathione-injection page byte-for-byte (no distinct PDP). Branded Ozempic®/Mounjaro® listed at $1,399. Re-check prices — plan/promo-driven."
---

## Portfolio overview

~19 distinct SKUs across four nav families — **Weight loss**, **Anti-aging**, **Peptides**, **Supplements** — a `Multi-product` shape under a "longevity" umbrella. The lines overlap (metformin, sermorelin, BPC-157, GLP-1 Boost each sit in two families); each is rostered once under its primary family with the cross-listing noted.

**Pricing shape — almost everything is `partial`.** Advertised Rx prices are *per-month floors*, not self-contained: every PDP carries a templated footnote — *"$49.75/week = $199/mo (paid upfront with a 12-month plan)"* — so the lowest rate assumes a 12-month prepay, and compounded GLP-1 is priced "From $197 $175 (4 doses/month)," i.e. it also moves with dose. Only the **oral supplements** (GLP-1 Boost, Gut Peptide Complex, Methylene Blue) and the cheap **anti-nausea companion** show flat, self-contained prices → `published`.

**Prominence** (order/nav/CTA signals, no "best-seller" badges seen):
- **Compounded GLP-1 weight loss** `[MED]` — the front door: the hero ("Lose weight with GLP-1 Injection"), the first nav family, and the most-repeated CTA.
- **NAD+** `[MED]` — the #2 hero/carousel slot and the face of the "anti-aging / longevity" pillar.
- Everything else `[LOW]` — carousel/nav order only.

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Weight loss | family | — | /weight-loss | — | — | Compounded + branded GLP-1 and weight-loss companions |
| Personalized GLP-1 Injections | buyable | Weight loss | /products/personalized-glp-1-injections | "From $197 $175 (4 doses/month)" | partial | tirzepatide **or** semaglutide · subcutaneous injection · Rx (online visit) |
| GLP-1 Microdose | buyable | Weight loss | /products/microdose-glp-1-injections | "$155" | partial | semaglutide/tirzepatide, microdose · injection · Rx (online visit) |
| GLP-1 Oral Melts | buyable | Weight loss | /products/glp1-oral-melts | — | on-request | molecule not stated · oral melt · Rx — **no live price (PDP 404s)** |
| MIC + B12 Injection | buyable | Weight loss | /products/lipotropic-mic-b12-injection | "$179" | partial | methionine · inositol · choline + B12 · injection · Rx |
| Anti-Nausea Tablets | buyable | Weight loss | /products/anti-nausea-tablets | "$19.99" | published | ondansetron · oral tablet · Rx companion |
| Ozempic® | buyable | Weight loss | /products/ozempic | "$1,399" | partial | semaglutide (FDA brand) · injection · Rx (online visit) |
| Mounjaro® | buyable | Weight loss | /products/mounjaro | "$1,399" | partial | tirzepatide (FDA brand) · injection · Rx (online visit) |
| Metformin | buyable | Weight loss | /products/metformin | "$90" | partial | metformin · oral tablet · Rx (off-label); also listed under Anti-aging |
| Anti-aging | family | — | /anti-aging | — | — | NAD+, glutathione, sermorelin, B12 — the "longevity" line |
| NAD+ Injection | buyable | Anti-aging | /products/nad-injection | "$199" | partial | NAD+ (nicotinamide adenine dinucleotide) · injection (IM/SubQ) · Rx |
| NAD+ Nasal Spray | buyable | Anti-aging | /products/nad-nasal-spray | "From $179 (used daily)" | partial | NAD+ · nasal spray · Rx — plan ladder (see anchors) |
| Glutathione Injection | buyable | Anti-aging | /products/glutathione-injection | "From $179" | partial | glutathione · injection (SubQ/IM) · Rx |
| Glutathione Nasal Spray | buyable | Anti-aging | /products/glutathione-nasal-spray | "From $179" | partial | glutathione · nasal spray · Rx — **PDP serves the glutathione-injection page** |
| B12 Injection | buyable | Anti-aging | /products/vitamin-b12-injection | "$179" | partial | methylcobalamin (vitamin B12) · injection · Rx |
| Sermorelin | buyable | Anti-aging | /products/sermorelin-injection | "$175" | partial | sermorelin (GHRH analog) · subcutaneous injection · Rx |
| Peptides | family | — | /peptides | — | — | Sermorelin (legacy page) + BPC-157 |
| Sermorelin (peptides) | buyable | Peptides | /products/sermorelin-injection-old | "$225" | partial | sermorelin · injection · Rx — legacy "-old" page; priced higher than the anti-aging sermorelin |
| BPC 157 | buyable | Peptides | /products/bpc-157 | "$129" | published | BPC-157 peptide · injection · platform purchase; also cross-listed under Supplements |
| Supplements | family | — | /supplements | — | — | Oral, non-Rx products |
| GLP-1 Boost | buyable | Supplements | /products/glp-1-boost | "$72" | published | oral supplement (ingredients not enumerated in capture) · non-Rx; also cross-listed under Weight loss |
| Gut Peptide Complex | buyable | Supplements | /products/gut-peptide-complex | "$89" | published | peptide complex (ingredients not stated) · oral · non-Rx |
| Methylene Blue | buyable | Supplements | /products/methylene-blue | "$89" | published | methylene blue · oral · non-Rx (page-tagged "Supplement") |

### Verbatim anchors

- **Flagship GLP-1 floor** — `"From $197 $175 (4 doses/month)"` (/products/personalized-glp-1-injections). Molecule: *"Ivy Rx compounded GLP-1 medications (with **tirzepatide** or **semaglutide**)…"* (same page).
- **Templated plan footnote (on every PDP — the reason Rx rows are `partial`):** *"Actual price to the consumer will depend on the product and plan purchased. $49.75 per week = $199/mo ( paid upfront with a 12-month plan ) divided by 4 weeks."*
- **NAD+ nasal-spray plan ladder** (/products/nad-nasal-spray): headline `"From $179 (used daily)"`, with plan totals/rates `$2,388` → `$199`, `$1,374` → `$229`, `$747` → `$249`, `$279` → `$279`.
- **Sermorelin price split:** `$175` on the anti-aging page (/products/sermorelin-injection) vs `$225` on the peptides page (/products/sermorelin-injection-old) — two live pages for the same molecule.
- **Compounding lane:** *"the treatments are compounded in pharmacies compliant with **503B / USP <797>** standards"* (GLP-1 PDP + homepage FAQ).
- **Molecule sourcing for `not stated`:** GLP-1 Oral Melts (PDP 404, nothing to attest); GLP-1 Boost / Gut Peptide Complex ingredients aren't enumerated on the captured category pages — page-tagged "Supplement" only.

## Deep blocks

None earned — the roster + verbatim anchors carry this company. The single cross-cutting subtlety (the plan-based "From $X" pricing that makes nearly every Rx row `partial`) is captured in the overview and the templated-footnote anchor; no per-SKU ambiguity needs a dedicated block. No PDP-anatomy block and no hero-image capture were requested this run.

## Provenance

- **Pages read:** /treatments (full price grid), /weight-loss, /anti-aging, /peptides, /supplements, homepage; PDPs: personalized-glp-1-injections, nad-nasal-spray, glutathione-injection, methylene-blue, ozempic, mounjaro, glp1-oral-melts (404). All in `captures/2026-06-04/`.
- **Scope:** all 19 nav/treatments products enumerated at the SKU level; the four overlapping products (metformin, sermorelin, BPC-157, GLP-1 Boost) are rostered once under a primary family with cross-listings noted, not double-counted. Every `$` price is greppable in a cited capture.
- **Gated / unreachable:** GLP-1 Oral Melts PDP returns 404 (no price); glutathione-nasal-spray URL serves the injection PDP (no distinct content).
- **Point-in-time caveat:** prices are plan/promo-driven and advertised as per-month floors assuming multi-month upfront commitments — treat as a snapshot, re-verify on next capture.
- **Run profile:** part of a guided run (+telehealth, +offerings, +logos); vanilla offerings roster — no added columns, no PDP-anatomy block, no hero-image capture.
