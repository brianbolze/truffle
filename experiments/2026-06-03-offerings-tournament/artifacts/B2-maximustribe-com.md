<!-- design: B2 molecule-pivoted offerings | company: maximustribe.com | scope: GLP-1 + TRT/testosterone only | built: 2026-06-03 from persisted captures -->

# Maximus — offerings (B2: molecule-pivoted)

`maximustribe.com` · Multi-product DTC performance-medicine telehealth. Direct-pay subscription; no insurance. Scope of this doc: **GLP-1 weight-loss** and **TRT / testosterone** lines only (the company also sells GHRH peptides, labs, oxytocin cream, hair, blood-flow, multivitamin — out of scope here).

> **Molecule is a query-time attribute, not a stored entity.** The `Molecule` column exists so a cross-company query can group "every semaglutide row" or "every enclomiphene row" on a shared, greppable string. It is NOT a canonical key and asserts **no** equivalence between Maximus's molecule and any other brand's — Maximus's own copy stresses base-form vs salt-form differences and its patent-pending combinations. The within-company key is the **page slug** (`Slug` column). Prices are verbatim; footnotes cite the captured page.

## Portfolio overview

Two molecule families in scope, 9 distinct buyable SKUs.

- **GLP-1 weight loss (2 SKUs)** — `semaglutide` and `tirzepatide`, both compounded, once-weekly self-inject, sold as month-to-month subscriptions with a discounted anchor ("from $149.99/mo ~~$229.99~~" / "from $249.99/mo ~~$329.99~~"). Dose is prescriber-set and **not** chosen on the public page; copy says "flat-rate monthly plans that include access to all dose tiers," so the shown "from" price is an anchor, not the full ladder → **[partial]**. Available all states **but AL, MS, LA**. Both men and women.
- **TRT / testosterone (7 SKUs)** — the flagship line. Three single-molecule protocols (`enclomiphene`, oral `testosterone`, topical `testosterone` cream, injectable `testosterone`) plus three combinations (`enclomiphene + testosterone` cream, `enclomiphene + oral testosterone`, `testosterone + hCG`). The four protocols with a dedicated product page expose a **full 3-tier price ladder** (1-/3-/12-month) → **[published]**. The three seen only as cards on the `/testosterone` roster page show a single "Starting at" anchor → **[partial]**. Flagship copy: *"Protocols start at $99.99/month… combination protocols… range from $149.99–$199.99/mo,"* top combo $299.99/mo.

Cross-line mechanics (apply to every SKU below): free at-home lab test or recent bloodwork required before a prescription; ongoing doctor messaging + monitoring bundled at no extra cost; **50% off first month** on the longest plan for new clients; HSA/FSA eligible; compounded by US-based LegitScript-certified pharmacies. **No public price is a true all-in checkout number** — every protocol is intake/lab-gated on `app.maximustribe.com`, and the page disclaimer notes price "may vary slightly by state" and by dosage.

## Deep blocks (flagships only)

Only the two genuine flagships get a block: **Injectable TRT** (the origin/most-studied testosterone protocol, full ladder) and **Semaglutide** (the volume GLP-1). Everything else lives in the Roster.

### Injectable Testosterone — `/testosterone/Injectable-TRT` · [published]
Molecule: testosterone (injectable, compounded). "Tried-and-true TRT… 1-2 shots weekly," MCT-oil formulation, subcutaneous. Full ladder shown on page:

| Plan | Price (verbatim) |
|---|---|
| 1 Month | **$199.99/mo** |
| 3-Month Plan (MOST POPULAR) | **$149.99/mo** |
| 12-Month Plan (BEST VALUE) | **$99.99/mo** |

Page also states it plainly: *"**Injectable Testosterone** starting at **$99.99**/mo."* Caveat printed on page: *"Pricing varies by dosage and plan length. May vary slightly by state."* Lab work required (Total T, SHBG/free T, LH, PSA, Hematocrit). The $99.99 floor is real and shown, but the actual charged amount is dose- and state-dependent — ladder is published; the per-patient final is set at intake.

### Semaglutide — `/weight-loss/semaglutide-standard` · [partial]
Molecule: semaglutide (compounded, GLP-1). "Personalized doses from **$149.99**/mo ~~$229.99~~, Save $80." Once-weekly self-inject. Page is explicit that dose is prescriber-set ("Your dose, your plan… Not a flat protocol") and that higher doses cost no more ("flat-rate monthly plans that include access to all dose tiers") — so the $149.99 is a starting anchor, with the operative price determined after evaluation in-app. Base form only (page contrasts against salt forms). Not available in AL, MS, LA. **[partial]** — a price shows, but the buyable all-in is gated behind the dose/plan selection in the intake flow.

## Roster — one row per buyable SKU, pivoted for molecule comparison

`Branded/Compounded`: all in-scope Maximus medications are **compounded** (the brand sells no branded-pharma SKU; "Brand SKU name" is therefore Maximus's own protocol name, not a manufacturer brand). `Price` is verbatim from the cited page. `Visibility`: **[published]** = full price/ladder shown; **[partial]** = a "from/Starting at" price shows but real all-in is dose/plan/state-gated; **[on-request]** = no price without intake. (No in-scope SKU is fully [on-request] — every one shows at least a starting anchor.)

| Molecule (query-time attr) | Form | Branded/Compounded | Brand SKU name | Dose/strength | Price (verbatim) | Visibility | Slug |
|---|---|---|---|---|---|---|---|
| semaglutide | injectable (weekly) | Compounded | Semaglutide (Weight Loss Protocol) | personalized, prescriber-set (not shown) | "Personalized doses from **$149.99**/mo ~~$229.99~~" [^sema] | [partial] | `/weight-loss/semaglutide-standard` |
| tirzepatide | injectable (weekly) | Compounded | Tirzepatide (Weight Loss Protocol) | personalized, prescriber-set (not shown) | "Personalized doses from **$249.99**/mo ~~$329.99~~" [^tirz] | [partial] | `/weight-loss/tirzepatide-standard` |
| enclomiphene | oral (daily pill) | Compounded | Enclomiphene | "once-a-day pill"; dose set at intake | 1mo **$199.99/mo** · 3mo **$149.99/mo** · 12mo **$99.99/mo** [^enclo] | [published] | `/testosterone/enclomiphene-only` |
| testosterone | topical (daily cream) | Compounded | Testosterone Cream | daily; "peak ~1,321 ng/dL (results vary)" | 1mo **$209.99/mo** · 3mo **$159.99/mo** · 12mo **$109.99/mo** [^cream] | [published] | `/testosterone/Testosterone-Cream` |
| testosterone | injectable (1-2×/week) | Compounded | Injectable Testosterone | weekly; MCT-oil; dose set at intake | 1mo **$199.99/mo** · 3mo **$149.99/mo** · 12mo **$99.99/mo** [^inj] | [published] | `/testosterone/Injectable-TRT` |
| testosterone | oral (daily pills) | Compounded | Oral Testosterone | "daily pills (typically 3-4)" | "Starting at **$149.99/mo**" [^oral] | [partial] | `/testosterone/oral-testosterone` |
| enclomiphene + testosterone | oral pill + topical cream | Compounded | Enclomiphene + Testosterone Cream (patented) | daily pill + daily cream | 1mo **$289.99/mo** · 3mo **$239.99/mo** · 12mo **$189.99/mo** [^combo] | [published] | `/testosterone/Testosterone-Cream-and-Enclomiphene` |
| enclomiphene + testosterone | oral pill + oral T | Compounded | Enclomiphene + Oral Testosterone (patented) | all-oral, daily | "Starting at **$199.99/mo**" [^oralcombo] | [partial] | `/testosterone/oral-testosterone-and-enclomiphene` |
| testosterone + hCG | injectable (weekly) | Compounded | Injectable Testosterone + hCG | weekly injection | "Starting at **$299.99/mo**" [^hcg] | [partial] | `/testosterone/Injectable-TRT-and-hCG` |

**Add-on noted, not a standalone SKU:** the `/testosterone` roster repeatedly offers *"Add Tadalafil to your protocol for free"* on the enclomiphene-family cards. A separate triple-combo slug `/testosterone/enclomiphene-tadalafil-testosterone-cream` is linked from one hero CTA but was **not given its own price card** on any captured page — not counted as a distinct buyable row (see Notes).

### Molecule → SKU rollup (query convenience)
- **semaglutide** → 1 SKU (weight loss)
- **tirzepatide** → 1 SKU (weight loss)
- **testosterone** (alone) → 3 SKUs: oral, topical cream, injectable
- **enclomiphene** (alone) → 1 SKU
- **enclomiphene + testosterone** (combo) → 2 SKUs: + cream, + oral
- **testosterone + hCG** (combo) → 1 SKU

## Provenance & footnotes

All prices pulled from pages persisted at `experiments/2026-06-03-offerings-tournament/captures/maximustribe-com/`, fetched 2026-06-03 via Firecrawl (US, maxAge:0). The four single-protocol ladders come from their own dedicated product pages; the three "Starting at" combo/oral anchors come from the `/testosterone` roster page's product cards (no dedicated page was captured for those three).

[^sema]: `weight-loss-semaglutide-standard.md` — "Personalized doses / from **$149.99**/mo ~~$229.99~~ / Save $80"; also "**Weight Loss Protocol Semaglutide** starting at **$149.99**/mo"; "We offer flat-rate monthly plans that include access to all dose tiers."
[^tirz]: `weight-loss-tirzepatide-standard.md` — "Personalized doses / from **$249.99**/mo ~~$329.99~~ / Save $80"; also "**Weight Loss Protocol Tirzepatide** starting at **$249.99**/mo."
[^enclo]: `testosterone-enclomiphene-only.md` — "1 Month $199.99/mo / 3-Month Plan MOST POPULAR $149.99/mo / 12-Month Plan BEST VALUE $99.99/mo"; "**Enclomiphene** starting at **$99.99**/mo." Confirmed on roster: "Starting at $99.99/mo."
[^cream]: `testosterone-cream.md` — "1 Month $209.99/mo / 3-Month Plan MOST POPULAR $159.99/mo / 12-Month Plan BEST VALUE $109.99/mo"; "**Testosterone Cream** starting at **$109.99**/mo." Roster card confirms "Starting at $109.99/mo."
[^inj]: `testosterone-injectable-trt.md` — "1 Month $199.99/mo / 3-Month Plan MOST POPULAR $149.99/mo / 12-Month Plan BEST VALUE $99.99/mo"; "**Injectable Testosterone** starting at **$99.99**/mo." Roster card confirms "Starting at $99.99/mo."
[^oral]: `testosterone-category.md` (roster card; no dedicated page captured) — "### Oral Testosterone … Starting at$149.99/mo", CTA `?sub_product=oral_trt`.
[^combo]: `testosterone-cream-and-enclomiphene.md` — "1 Month $289.99/mo / 3-Month Plan MOST POPULAR $239.99/mo / 12-Month Plan BEST VALUE $189.99/mo"; "**Enclomiphene + Testosterone Cream** starting at **$189.99**/mo"; "Patented formulation available exclusively through Maximus."
[^oralcombo]: `testosterone-category.md` (roster card; no dedicated page captured) — "### Enclomiphene +  Oral Testosterone … Starting at$199.99/mo", CTA `?sub_product=oral_trt+enclo`.
[^hcg]: `testosterone-category.md` (roster card; no dedicated page captured) — "### Injectable Testosterone + hCG … Starting at$299.99/mo", CTA `?sub_product=inj_trt+hcg`.
