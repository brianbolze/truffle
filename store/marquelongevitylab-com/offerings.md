---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.2"
domain: marquelongevitylab.com
captured_at: 2026-06-10
enumeration: indexed-complete
site_notes: "Treatment menu lives ONLY on /services (the #aesthetics/#hormone/#medical-weight-management/#recovery/#lab-testing anchors) + the /about FAQ — the per-service detail pages (/services/<slug>) are unbuilt Lorem-Ipsum stubs, do not roster from them. NO prices anywhere on the site: booking, à la carte service prices, and membership tiers all sit behind the Zenoti webstore (themarque.zenoti.com) → every row is on-request. No per-treatment PDPs exist, so within-company keys are the /services anchors, not URLs. Specific drug/filler/peptide brands are mostly unnamed; weight-management molecules are named only in the FAQ."
---

## Portfolio overview

A `Multi-product` clinic menu: **five service lines**, each holding a handful of named treatments. The menu is shallow by design — The Marque indexes at the **treatment grain** (e.g. "wrinkle relaxers," "NAD+," "HBOT"), not per-dose/brand SKUs, and exposes **no prices or PDPs** on the marketing site (all booking + pricing is gated in a Zenoti webstore). So this roster is a complete *menu*, not a priced catalog — every line is `on-request`.

Prominence (calibrated): the five lines are presented as **co-equal, numbered 01–05** in the same order on the homepage, /services, and the nav `[MED]` — section order is the only cue; no line is badged or hero'd above the others, and the brand's whole pitch ("Applied Wellness") is that they're used *together*. Within lines, no treatment is flagged as a lead `[LOW]`. Weight management is the only line whose specific molecules are named (in the FAQ) `[HIGH]`.

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Aesthetics & Skin Treatments | family | — | /services#aesthetics | — | — | Injectables + skin-health line, "natural results" |
| Wrinkle relaxers | buyable | /services#aesthetics | (no PDP — /services#aesthetics) | — | on-request | not stated (neuromodulator) · injectable · in-clinic — smooths wrinkles/fine lines, preserves expression |
| Dermal fillers & bio-stimulators | buyable | /services#aesthetics | (no PDP — /services#aesthetics) | — | on-request | not stated · injectable · in-clinic — restores volume/contour, stimulates collagen |
| Body contouring | buyable | /services#aesthetics | (no PDP — /services#aesthetics) | — | on-request | not stated · device/non-invasive · in-clinic — fat reduction, skin tightening, muscle toning |
| Microneedling | buyable | /services#aesthetics | (no PDP — /services#aesthetics) | — | on-request | n/a · device · in-clinic — collagen induction; texture/scarring/dullness |
| Hormone & Longevity Optimization | family | — | /services#hormone | — | — | Hormones + peptides + NAD+ + supplements |
| Hormone therapy | buyable | /services#hormone | (no PDP — /services#hormone) | — | on-request | bioidentical hormones · per "bioidentical strategies", form not stated · clinician-supervised, lab-gated — mapping + monitoring + dose adjustment |
| Peptides | buyable | /services#hormone | (no PDP — /services#hormone) | — | on-request | not stated (specific peptides unnamed) · physician-guided dosing · biomarker-based — recovery, cognition, metabolism, repair |
| NAD+ | buyable | /services#hormone | (no PDP — /services#hormone) | — | on-request | NAD+ · form not stated · in-clinic — cellular repair, mitochondrial function, focus/energy |
| Supplements & Nutraceuticals | buyable | /services#hormone | (no PDP — /services#hormone) | — | on-request | incl. **Thorne** · oral · recommended per diagnostics — curated to the program |
| Medical Weight Management | family | — | /services#medical-weight-management | — | — | GLP-1 / peptide-assisted metabolic protocols + coaching |
| Weight control (medical) | buyable | /services#medical-weight-management | (no PDP — /services#medical-weight-management) | — | on-request | **semaglutide, tirzepatide** (GLP-1), plus **tesofensine, phentermine, naltrexone** — all FAQ-attested · oral/injectable · "when clinically appropriate and monitored" — metabolic protocols + progress tracking |
| Exercise & Nutrition Guidance | buyable | /services#medical-weight-management | (no PDP — /services#medical-weight-management) | — | on-request | n/a · coaching · labs/goal-aligned — training + nutrition + nutraceuticals |
| Recovery & Performance Therapy | family | — | /services#recovery | — | — | Light/oxygen/injection/IV recovery modalities |
| Red Light Therapy | buyable | /services#recovery | (no PDP — /services#recovery) | — | on-request | n/a · device · in-clinic — cellular energy, inflammation, recovery, skin |
| Hyperbaric Oxygen Therapy (HBOT) | buyable | /services#recovery | (no PDP — /services#recovery) | — | on-request | oxygen · chamber · in-clinic — tissue healing, cognition, circulation, recovery |
| Metabolic Repletion (injections) | buyable | /services#recovery | (no PDP — /services#recovery) | — | on-request | **B12, amino blends, taurine, L-carnitine, glutathione** (FAQ-attested) · injectable · in-clinic — energy, joint, metabolism, immune |
| Infusion Therapy (IV) | buyable | /services#recovery | (no PDP — /services#recovery) | — | on-request | not stated (custom blends) · IV · in-clinic, medical oversight — hydration, energy, immunity, recovery |
| Lab Testing & Diagnostics | family | — | /services#lab-testing | — | — | Biomarker panels + body composition + bloodwork |
| Integrated Diagnostics & Testing | buyable | /services#lab-testing | (no PDP — /services#lab-testing) | — | on-request | n/a · blood/biomarker + body-composition testing · licensed clinical staff — hormones, metabolism, inflammation, thyroid, micronutrients, lipids, recovery, longevity markers; many repeat every 3–4 months |

## Verbatim anchors

Pricing footnotes: **none exist** — no price, "from $X", or floor appears on any captured page; the only purchase surface is the gated Zenoti webstore, so every row is `on-request` (no membership/dose footnote decides `partial` vs `published` because no number is shown at all).

Molecule sourcing (page-attested, `not stated` audit):
- **Weight Management** — "Do you offer GLP-1 medications like **semaglutide or tirzepatide**? Yes — when clinically appropriate and monitored closely." and "Other options such a **tesofensine, phentermine, naltrexone** or other medications have a role in weight management" (/about FAQ; the aesthetics stub's FAQ also). These are the only named drug molecules on the site.
- **Metabolic Repletion injections** — "nutrient, anti-inflammatory, metabolic, and performance-enhancing injections including **B12, amino blends, taurine, L-carnitine, glutathione**, and more" (/about FAQ).
- **Hormone therapy** — page says "bioidentical and clinically validated therapies"; **no specific hormone named** → molecule `bioidentical hormones`, not a specific agent.
- **Peptides** — "targeted peptides for recovery, cognition, metabolism, and repair"; **no specific peptide named** → `not stated`.
- **Aesthetics (relaxers/fillers)** — no neurotoxin or filler brand named → `not stated`.

## Deep blocks

None earned — the roster carries this company. No SKU has a price footnote, disambiguation, or verbatim H1 that a roster row can't hold; the menu is shallow (treatment grain, no PDPs).

## Provenance

- **Pages read:** `captures/2026-06-10/services.md` (the authoritative treatment menu, all five #anchors), `captures/2026-06-10/about.md` (FAQ — the molecule names, à la carte vs membership, pharmacy, telehealth states), `homepage.md` (line order/prominence). The 5 `/services/<slug>` detail pages were captured but are **unbuilt Lorem-Ipsum stubs** — excluded from rostering.
- **Scope note:** `indexed-complete` for a `Multi-product` shape — all 5 lines rostered at the treatment grain the site indexes at. **Leaf detail deliberately not enumerated** (none is published): per-dose/quantity tiers, specific filler/neurotoxin/peptide brands, individual lab-panel SKUs, and membership tiers/perks — all live in the gated Zenoti webstore or are simply unnamed on the site.
- **Gated/unreachable:** all pricing + membership tiers (Zenoti login wall); no public price surface to enumerate.
- **Point-in-time caveat:** the site is freshly launched and partially built (placeholder detail pages, a placeholder contact phone) — this menu is a snapshot; treatments and naming may change as the site is completed.
- **Credits:** rode the `profile.md` capture (same /services + /about pages) — no additional spend.
- **### Run profile:** express — user asked for offerings on a services company with no published prices. Rostered the treatment *menu* (enumerable) at `on-request`; recorded the no-price-surface finding rather than declining, since the menu is genuinely enumerable.
