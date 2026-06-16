---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.2"
domain: sermorelin.com
captured_at: 2026-06-16
enumeration: indexed-complete
site_notes: "Every priced line reads off 3 pages — homepage (sermorelin Injectable/Oral tabs) + /enclomifene + /ghk-cu; no per-SKU PDPs and no /pricing. Sermorelin & enclomiphene plan tiers (monthly/3-mo/6-mo) are leaf detail under one struck-$199 promo; GHK-Cu prices are per-variant (no plan ladder shown). GHK-Cu intake routes to meds.you.withrefill.com (Refill), not start.sermorelin.com. Prices are promo snapshots ('Save $50 every month', auto-applied) — re-check for rotation."
---

## Portfolio overview

A **flagship + companions** peptide catalog. **Sermorelin** is the hero (the brand name, the entire homepage, the only line in the header nav) `[HIGH]`; **enclomiphene** and **GHK-Cu** are companion lines reachable only by direct URL / SEO, absent from nav `[HIGH — nav/structure]`. Pricing is uniform and simple: sermorelin and enclomiphene share one plan ladder (struck-through **$199/mo** monthly → **$149/mo** on a 6-month commit), while GHK-Cu prices per variant ($190–$229/mo) with no plan ladder shown. Everything is physician-prescribed and compounded; no FDA-brand drug, no controlled substance. Shape finding: the "testosterone" line (enclomiphene) is a **SERM that raises endogenous testosterone**, explicitly *not* exogenous/TRT.

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Sermorelin | family | — | / | — | — | sermorelin (GHRH analog) · two delivery forms · Rx, compounded |
| Sermorelin Injection | buyable | Sermorelin | / | $149/mo–$199/mo † | published | sermorelin · subcutaneous injection (bedtime) · physician-prescribed, compounded; intake /intake |
| Sermorelin Oral Tablets | buyable | Sermorelin | / | $149/mo–$199/mo † | published | sermorelin · sublingual ODT (needle-free) · same price as injection; intake /intake |
| Enclomiphene | family | — | /enclomifene | — | — | enclomiphene (SERM) · oral capsule · "Optimize Your Testosterone Naturally" |
| Enclomiphene — Standard | buyable | Enclomiphene | /enclomifene | $149/mo ‡ | published | enclomiphene · oral capsule, **375mg/month** · raises LH/FSH → endogenous testosterone (not exogenous/TRT) |
| Enclomiphene — High Dose | buyable | Enclomiphene | /enclomifene | $179/mo ‡ | published | enclomiphene · oral capsule, **750mg/month** · high-dose tier |
| GHK-Cu | family | — | /ghk-cu | — | — | GHK-Cu (copper peptide) · 4 variants · skin / hair / regenerative; intake meds.you.withrefill.com |
| GHK-Cu Injectable | buyable | GHK-Cu | /ghk-cu | $199/mo | published | GHK-Cu · subcutaneous injection · "Market range $100 to $350 per month" |
| GHK-Cu Topical Skin | buyable | GHK-Cu | /ghk-cu | $190/mo · $214/mo · $225/mo | published | GHK-Cu · topical cream (Aquabiome+ GHK-Cu, **30g/month**) · 3 variants: $190 "Entry Level" · $214 "Postmenopausal" · $225 |
| GHK-Cu Hair Restoration | buyable | GHK-Cu | /ghk-cu | $229/mo | published | GHK-Cu · topical solution (**30mL/month**, 7.5mL/week) · "Market range $83 to $300 per month" |
| GHK-Cu with Epithalon | buyable | GHK-Cu | /ghk-cu | $219/mo | published | GHK-Cu + Epithalon · single weekly injection (**400 units/month**) · collagen + longevity combo; "Market range $99 to $275 per month" |

*Not a SKU:* **Sermorelin + GLP-1 combination** (`/glp1-combination`) is an education/positioning page — sermorelin pitched as a companion to GLP-1 for lean-mass preservation; no priced product. `[on-request]`

## Verbatim anchors

- **† Sermorelin plan ladder** (Injectable & Oral, same price), from the homepage product card: "Monthly Plan **$199/mo**" · "3-Month Plan — You save 15% — **$169/mo** ~~$199/mo~~" · "6-Month Plan — You save 25% — **$149/mo** ~~$199/mo~~ — Most Popular." "Save up to $50 every month! … Discount auto-applied at checkout." "180-day money-back guarantee on our 6-Month Plan."
- **‡ Enclomiphene tiers**, /enclomifene: "Available in standard and high dose plans." Standard "375mg per month. **$149/mo** — Most Popular"; High Dose "750mg per month **$179/mo**." Same struck-through ~~$199/mo~~ monthly anchor + "180-day money-back guarantee on our 6-Month Plan."
- **GHK-Cu Topical tiers**, /ghk-cu: "Aquabiome+ GHK-Cu Cream — 30g per month — **$190/mo** — Entry Level"; "30g per month — **$214/mo** — Postmenopausal"; "30g per month — **$225/mo**."
- **Molecule sourcing:** sermorelin = "growth hormone-releasing hormone (GHRH) analog" (homepage FAQ); enclomiphene = "Raises LH and FSH to restore natural testosterone production without suppressing sperm production like exogenous testosterone" (/enclomifene); GHK-Cu = "copper peptide" + Epithalon named (/ghk-cu). All page-attested.

## Deep blocks

None earned — the roster carries this company. Pricing is shallow and uniform (3 pages, published prices), and no single SKU has an ambiguity a row can't hold. The one disambiguation worth flagging (enclomiphene is a SERM, not TRT/exogenous testosterone) is captured in the roster `What` and Portfolio overview.

## Provenance

- **Pages read:** homepage (sermorelin Injectable/Oral tabs + plan ladder), /enclomifene, /ghk-cu, /glp1-combination — all in `captures/2026-06-16/`.
- **Scope note:** indexed-complete — all 3 sold lines rostered at SKU grain (sermorelin × 2 forms, enclomiphene × 2 doses, GHK-Cu × 4 variants). Leaf detail summarized, not separately rostered: sermorelin/enclomiphene plan tiers (monthly/3-mo/6-mo) live in Verbatim anchors. GLP-1 is a positioning page, not a SKU (recorded above, not rostered).
- **Every `$` price** is greppable in the cited captures (homepage / enclomifene / ghk_cu .md).
- **Point-in-time:** prices are a promotional snapshot (struck-$199 → discounted, "auto-applied at checkout"); GHK-Cu "Market range $X to $Y" lines are the brand's own framing, not third-party.
- **Run profile:** opt-in `offerings.md` added to an Express telehealth capture (deep gate: Companies `Direct competitor? = Yes`). No hero-image capture, no PDP-anatomy block.
