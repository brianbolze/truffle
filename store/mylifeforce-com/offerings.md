---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: mylifeforce.com
captured_at: 2026-06-04
site_notes: "Catalog = Next.js/Storyblok; product cards live on /collections/* grids (clean 3600x3600 *_clp.png renders, NO prices), per-SKU prices ONLY on /product/<slug> PDPs (client-side-loaded — NOT in rawHtml; /products.json + /collections/all.json soft-200 the SPA shell, no Shopify registry → budget ≈1 scrape/SKU). Supplements = published one-time + 'Save 15%' subscribe; Pharmaceuticals = price shown but members-only + clinician-gated; Advanced Panels = 'Members Only' collection, PDP shows full one-time price. Membership/diagnostic prices live on /pages/{membership,one-time-diagnostic}, not /product. Prices are promo-volatile (struck-through enrollment) — re-check next run. 5 /product PDPs error client-side + absent from grids (orphaned): peak-rise, zepbound, bpc-157, cjc-1295, ipamorelin. /product/peptide-telehealth + /product/membership are membership-enrollment choosers, not buyable SKUs."
---

## Portfolio overview

Lifeforce is a **diagnostic-anchored longevity membership** with an unusually deep companion catalog — the membership/diagnostic is the flagship funnel, and ~39 buyable SKUs (10 own-brand supplements, ~21 prescription meds across 7 health goals, 5 add-on diagnostic panels) hang off it. The shape finding: **two price regimes**. Supplements are openly priced and à-la-carte (one-time + subscribe-and-save, members 30% off) — `[published]`. Everything clinical (pharmaceuticals, panels) shows a number but is **gated**: pharma is members-only ($149/mo membership + a $599 diagnostic + a clinician video consult + state eligibility), panels are "Members Only" — `[partial]`. Lifeforce owns **no pharmacy** (third-party compounders Tailor Made + Precision), so the catalog's depth is a clinician-prescribed menu, not vertical fulfillment.

Prominence (calibrated):
- **Membership + One-Time Diagnostic** — the hero everywhere (homepage, every PDP's "Explore Membership" CTA, the comparison table). `[HIGH]` (company's own framing).
- **Supplements** — the only openly-shoppable line; collection grid leads Peak NMN → DHEA → Peak Cognition → Methylation → Peak Healthspan. `[MED]` (grid order).
- **Pharmaceuticals** — nav goal order leads with Hormone Health, then Vitality/Cardiac/Weight Loss/Brain/Sexual/Longevity; TRT + GLP-1 are the deepest sub-lines. `[MED]` (nav depth).

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Membership | family | — | /pages/membership | — | — | the flagship — recurring longevity-care subscription gating Rx access |
| Monthly Membership | buyable | Membership | /pages/membership | "~~$349~~$199" enrollment, then "$149/month (cancel anytime)" | published | 4×/yr at-home draw + 4×/yr consults + Rx access + coaching + 30% off supplements · subscription |
| Core Annual Membership | buyable | Membership | /pages/membership | "~~$699~~$599" one-time | published | 2×/yr draws + 1×/yr consult + Rx access + 30% off supplements · annual |
| Premium Annual Membership | buyable | Membership | /pages/membership | "$1449" annually | published | everything in Monthly Membership, billed annually |
| Maintenance Membership | buyable | Membership | /product/annual-lifeforce-maintenance-membership | "$499 annually" ("Only $41 a month", billed annually) | published | 2×/yr at-home draws · annual renewal/maintenance tier |
| HRT Membership | buyable | Membership | /product/lifeforce-hrt-membership | — (no price shown; "Add to Cart") | on-request | hormone-therapy-specific membership bundle · price not shown on PDP |
| Diagnostics | family | — | /pages/one-time-diagnostic | — | — | the at-home blood-test wedge |
| One-Time Diagnostic | buyable | Diagnostics | /pages/one-time-diagnostic | "$599" | published | 50+ biomarkers · at-home phlebotomist draw + 45-min clinician consult + Lifescore/bio-age · HSA/FSA; results 5–7 days |
| Supplements | family | — | /collections/supplements | — | — | own-brand "Peak" line + companions; one-time + "Save 15%" subscribe, members 30% off |
| Peak Healthspan™ | buyable | Supplements | /product/peak-healthspan | "$120" one-time · "~~$120~~$102" subscribe | published | NAD3® / fisetin healthy-aging blend · capsule · à-la-carte |
| Peak Rest | buyable | Supplements | /product/peak-rest | "$110" one-time · "~~$110~~$93.50" subscribe | published | sleep & recovery blend · capsule · à-la-carte |
| Peak NMN | buyable | Supplements | /product/peak-nmn | "$100" one-time · "~~$100~~$85" subscribe | published | NMN (cellular energy / DNA) · capsule · à-la-carte |
| Peak Cognition | buyable | Supplements | /product/peak-cognition | "$85" one-time · "~~$85~~$72.25" subscribe | published | cognition / neuroinflammation blend · capsule · à-la-carte |
| Omega | buyable | Supplements | /product/omega | "$70" one-time · "~~$70~~$59.50" subscribe | published | omega-3 (heart/brain/immune) · softgel · à-la-carte |
| Magnesium | buyable | Supplements | /product/magnesium | "$55" one-time · "~~$55~~$46.75" subscribe | published | magnesium (300+ enzymatic processes) · capsule · à-la-carte |
| DHEA | buyable | Supplements | /product/dhea | "$50" one-time · "~~$50~~$42.50" subscribe | published | DHEA (hormone/sexual/weight) · capsule · à-la-carte |
| Methylation | buyable | Supplements | /product/methylation | "$50" one-time · "~~$50~~$42.50" subscribe | published | methylation / liver-detox support · capsule · à-la-carte |
| Vitamin D+K | buyable | Supplements | /product/vitamin-d-k | "$50" one-time · "~~$50~~$42.50" subscribe | published | vitamin D + K (bone/immune/cognition) · capsule · à-la-carte |
| CoQ10 | buyable | Supplements | /product/coq10 | "$40" one-time · "~~$40~~$34" subscribe | published | CoQ10 (antioxidant/cardiovascular) · capsule · à-la-carte |
| Pharmaceuticals | family | — | /collections/pharmaceuticals | — | — | members-only Rx menu across 7 health goals; price shown, gated (see anchors) |
| Semaglutide | buyable | Pharmaceuticals | /product/semaglutide | "$270" (ships every 25 days) | partial | weight loss · GLP-1, compounded semaglutide + B12 · once-weekly injection · members-only Rx |
| Testosterone Injectable | buyable | Pharmaceuticals | /product/testosterone-injection | "$80" (ships every 25 days) | partial | TRT/hormone · testosterone cypionate · injection · members-only Rx |
| Testosterone Cream | buyable | Pharmaceuticals | /product/testosterone-gel | "$80" | partial | TRT/hormone · bio-identical testosterone · topical gel/cream · members-only Rx |
| Kyzatrex® | buyable | Pharmaceuticals | /product/kyzatrex | "$250" | partial | TRT/hormone · oral testosterone (FDA-approved) · oral · members-only Rx |
| Clomiphene | buyable | Pharmaceuticals | /product/clomiphene | "$50" | partial | hormone · clomiphene (raises endogenous T) · form not stated · members-only Rx |
| Anastrozole | buyable | Pharmaceuticals | /product/anastrozole | "$30" | partial | hormone · anastrozole (aromatase inhibitor) · form not stated · members-only Rx |
| Estradiol Patch | buyable | Pharmaceuticals | /product/estradiol-patch | "$110" | partial | women's HRT · estradiol (FDA-approved) · transdermal patch · members-only Rx |
| Estriol Face Cream | buyable | Pharmaceuticals | /product/estriol-face-cream | "$95" | partial | women's skin · estriol · topical face cream · members-only Rx |
| Estradiol Cream | buyable | Pharmaceuticals | /product/estradiol-cream | "$60" | partial | women's HRT · estradiol · topical vaginal cream · members-only Rx |
| Micronized Progesterone | buyable | Pharmaceuticals | /product/micronized-progesterone | "$50" | partial | women's HRT · micronized progesterone · form not stated · members-only Rx |
| Tadalafil | buyable | Pharmaceuticals | /product/tadalafil | "$75" | partial | sexual health · tadalafil (ED) · form not stated (daily/as-needed) · members-only Rx |
| Sildenafil Arousal Cream | buyable | Pharmaceuticals | /product/sildenafil-arousal-cream | "$95" | partial | sexual health · sildenafil · topical arousal cream · members-only Rx |
| PT-141 | buyable | Pharmaceuticals | /product/pt-141 | "$160" | partial | sexual health · PT-141 peptide (libido/arousal) · subcutaneous injection · members-only Rx |
| Minoxidil + Finasteride | buyable | Pharmaceuticals | /product/minoxidil-finasteride | "$85" | partial | hair · minoxidil + finasteride · topical · members-only Rx |
| Levothyroxine | buyable | Pharmaceuticals | /product/levothyroxine | "$45" | partial | thyroid · levothyroxine (T4) · form not stated · members-only Rx |
| Liothyronine | buyable | Pharmaceuticals | /product/liothyronine | "$60" | partial | thyroid · liothyronine (T3) · form not stated · members-only Rx |
| Levothyroxine/Liothyronine (T4+T3) | buyable | Pharmaceuticals | /product/levothyroxine-liothyronine-t4-t3 | "$85" | partial | thyroid · levothyroxine + liothyronine · form not stated · members-only Rx |
| Rosuvastatin | buyable | Pharmaceuticals | /product/rosuvastatin | "$30" | partial | cardiometabolic · rosuvastatin (statin) · form not stated · members-only Rx |
| Ezetimibe | buyable | Pharmaceuticals | /product/ezetimibe | "$30" | partial | cardiometabolic · ezetimibe (LDL) · form not stated · members-only Rx |
| Metformin | buyable | Pharmaceuticals | /product/metformin | "$35" | partial | cardiometabolic · metformin (insulin sensitivity) · form not stated · members-only Rx |
| Sermorelin | buyable | Pharmaceuticals | /product/sermorelin | "$160" | partial | peptide/GH · sermorelin (secretagogue) · subcutaneous injection · members-only Rx |
| Advanced Panels | family | — | /collections/advanced-panels | — | — | add-on diagnostic panels; "Members Only" collection, PDP shows full one-time price |
| Brain Protection Panel | buyable | Advanced Panels | /product/brain-protection-panel | "$850" | partial | brain/neuro biomarkers (incl. GFAP, p-tau 217, ApoE) · one-time · members-only |
| Brain Protection Panel (Follow-Up) | buyable | Advanced Panels | /product/brain-protection-panel-follow-up | "$700" | partial | brain-panel re-test · one-time · members-only |
| Cardiovascular Panel | buyable | Advanced Panels | /product/cardiovascular-panel | "$200" | partial | cardiovascular biomarkers · one-time · members-only |
| Metabolic Panel | buyable | Advanced Panels | /product/metabolic-panel | "$200" | partial | metabolic biomarkers · one-time · members-only |
| Heavy Metals Panel | buyable | Advanced Panels | /product/heavy-metals-panel | "$200" | partial | heavy-metals biomarkers · one-time · members-only |

### Verbatim anchors

- **Pharma gating (decides every `[partial]` on a pharmaceutical), /product/semaglutide + every Rx PDP:** *"Pharmaceutical products are only available to members of the Lifeforce Membership ($149/month) and are contingent on blood tests results and clinician video consult. To qualify for the program you must reside in an eligible state* and purchase a Lifeforce Diagnostic ($599)."* The price shown is the med only; the all-in adds the $149/mo membership + $599 diagnostic. Refill cadence shown as **"Ships every 25 days"** (confirmed on semaglutide + testosterone-injection).
- **Supplement subscribe/membership note, every supplement PDP:** *"Members save 30% on supplement subscriptions"* + per-SKU "Monthly Save 15%" (the struck-through subscribe price) vs "One-Time Purchase" (the higher number). Both numbers grep in each `prod_*` capture.
- **Advanced Panels gating, /collections/supplements + /collections/advanced-panels nav:** *"Advanced Panels  Members Only"* (and *"Pharmaceuticals  Members Only"*) — the collection badge that gates panel access; the panel PDP itself shows the full one-time price with no on-page membership disclaimer.
- **Membership price ladder (promo-volatile):** /pages/membership shows *"Save $150 Today"*, *"$199 Today (Was $349)"*, *"Get started for $199, then $149/month (cancel anytime)"*, Core Annual *"~~$699~~$599"*, and *"Start for $1449 annually"*. The membership-enrollment chooser at /product/peptide-telehealth (and /product/membership) shows the **non-promo** *"~~$0~~$349"* enrollment + *"Ongoing monthly fee $149"* with the diagnostic at *"$0"* in-flow — i.e. $349 is the standard enrollment, $199 the current promo.
- **Molecule sourcing (the `form not stated` rows):** clomiphene, anastrozole, micronized progesterone, levothyroxine, liothyronine, T4+T3, rosuvastatin, ezetimibe, metformin, and tadalafil name the molecule in their PDP body but **do not state a dosage form** on the SKU's own page (no "tablet/capsule/oral" in product copy) — recorded `not stated` per the no-inference rule, even where the molecule is conventionally oral.

## Deep blocks

Earned only on ambiguity (not a per-flagship quota).

- **Semaglutide — "same active as Ozempic®/Wegovy®," but compounded.** /product/semaglutide: *"This is a unique compounded Semaglutide (combined with B12) that has the same active weight loss ingredient as the commercial brands Ozempic® and Wegovy®… available to people who meet the criteria for use."* So the GLP-1 line is **compounded semaglutide+B12**, not branded Ozempic/Wegovy — the molecule is page-attested, the brand-equivalence is a claim. Zepbound (tirzepatide) routes but its PDP errors and it is absent from every grid → **not currently offered** (don't read a tirzepatide line into the catalog).
- **Testosterone comes in three forms.** Lifeforce sells injectable (testosterone cypionate, $80), topical (bio-identical cream/gel, $80), and **oral** (Kyzatrex®, an FDA-approved oral testosterone, $250) — plus the endogenous-T raiser clomiphene ($50) and the estrogen-control anastrozole ($30). A TRT buyer comparison-shops these as distinct routes, not one SKU.
- **"Peptides" is thinner than the URL space suggests.** Only **sermorelin** ($160, subcutaneous) and the sexual-health **PT-141** ($160) are live peptide SKUs. The individual-peptide pages **bpc-157, cjc-1295, ipamorelin** route but throw a client-side exception and are absent from every grid (orphaned/discontinued); **/product/peptide-telehealth** is a membership-enrollment chooser, not a peptide product.
- **Flagship hero renders (opt-in asset set).** Clean isolated 3600×3600 product renders for the 10 own-brand supplements are saved at `captures/2026-06-04/images/<slug>.png` (peak-healthspan, peak-nmn, peak-rest, peak-cognition, omega, magnesium, dhea, methylation, vitamin-d-k, coq10). **Note:** the source CMS serves a **byte-identical render** for `peak-cognition` and `vitamin-d-k` (same white-capsule asset on a.storyblok.com — a Lifeforce-side collision, confirmed at source), so those two files are duplicates, not distinct shots. Pharma/panel `_clp.png` renders exist too (enumerated in the collection captures) but were not promoted — flagship = the own-brand supplement line.

## Provenance

- **Pages read:** 39 /product/* PDPs + /pages/{membership, one-time-diagnostic} + /collections/{supplements, pharmaceuticals, advanced-panels, all} (the priced backbone), captured 2026-06-04 (see `captures/2026-06-04/`).
- **Scope — enumerated:** all 37 SKUs in the master /collections/all grid (10 supplements + 21 pharmaceuticals + 4 panels + the membership chooser), plus 3 map-only variant SKUs with rendered prices (Maintenance Membership, HRT Membership, Brain Protection Panel Follow-Up). Completeness = rendered grid ∩ /map /product census agree on the 37.
- **Scope — noted, not enumerated:** /product/gift-card (a gift card, not a health offering); 5 orphaned/erroring PDPs (peak-rise, zepbound, bpc-157, cjc-1295, ipamorelin — client-side exception + absent from every grid).
- **Gated / unreachable:** no per-SKU price for HRT Membership (no price on PDP) or the 5 orphaned PDPs (page errors). Pharma/panel all-in cost requires the $149/mo membership + $599 diagnostic on top of the shown med/panel price.
- **Point-in-time caveat:** membership/diagnostic prices run a persistent struck-through promo and supplement subscribe prices have A/B-flickered historically — this roster is a 2026-06-04 snapshot, not fixed.
- **Credits:** rides the same 2026-06-04 capture as `profile.md` (54 attributed; see profile Provenance). No separate spend.

### Run profile

Express opt-in: full per-SKU roster requested alongside the profile refresh. Vanilla columns (no project-local grouping column added). One opt-in asset deviation: **flagship hero product images** captured for the 10 own-brand supplements (`captures/2026-06-04/images/`). No PDP-anatomy archetype block (not requested).
