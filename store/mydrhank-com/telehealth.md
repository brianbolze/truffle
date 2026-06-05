---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"
domain: mydrhank.com
captured_at: 2026-06-03           # rides the 2026-06-03 profile.md capture
value_chain_role: DTC brand
pharmacy_model: third-party              # "ships from an accredited compounding pharmacy" — supplier language, no ownership claim, no named/sibling pharmacy
audience: men-first                       # masculine-leaning (a "Men's Health" section, ED + "Strength"/sermorelin, male imagery); gender-neutral flagship + female-safe hair — see note
compounding_posture: compounded-only      # everything dispensed is compounded — even the FDA-approved-ingredient SKUs (minoxidil, finasteride); no FDA-brand SKU sold
anchor_category: GLP-1                    # weight loss is the hero — "our most popular treatment," leads the nav, only line that shows prices
modality: async                          # quiz → provider review/Rx "within 48 hours," "no office visits required"; sync care is post-purchase messaging
access_model: all-in                     # "no insurance, no membership, no consult fee" — one per-month medication price bundles the (free) consult + shipping
pay_model: cash-pay only                 # "No insurance required / no insurance needed" site-wide; pay only the medication price — see note
---

## Fulfillment

- **Pharmacy (claim, verbatim):** "Your medication **ships from an accredited compounding pharmacy** in discreet packaging" (homepage / every category page); "**Compounded by accredited U.S. pharmacies**" / "shipped from accredited U.S. pharmacies" / "FDA-registered U.S. pharmacy" (PDPs). No owned-pharmacy claim, no named partner, no sibling pharmacy domain.
- **Lane:** not stated — "accredited compounding pharmacy" only; neither 503A nor 503B is named.
- **Everything is compounded** — "Compounded medications are not FDA-approved…" carries on every page; even the FDA-approved-ingredient SKUs (minoxidil, finasteride) are dispensed as compounded products.

## Categories served

- **Categories:** GLP-1 (weight loss) · longevity/NAD (+ glutathione) · sexual-health/ED · hair · peptides (Sermorelin, the one-product "Strength" line). 16 buyable SKUs across 5 lines — per-SKU roster in [`offerings.md`](offerings.md).

## Credibility & access

- **Health-merchant credibility:** LegitScript-certified (footer seal #3314240 → `legitscript.com/websites/?checker_keywords=mydrhank.com`, y); named clinicians — "U.S.-licensed providers review every case" but no `/physicians` roster and **no about/company page at all** (n); pharmacy accreditation (PCAB/ACHC/NABP) claimed generically ("accredited") but no body named (n).
- **Controlled-substance Rx:** **non-scheduled only** — the page-attested products are GLP-1, NAD+/glutathione, PDE5 ED (sildenafil/tadalafil), hair (minoxidil/finasteride), and sermorelin (a peptide). No testosterone/TRT or other scheduled SKU appears.
- **Labs:** **none** — the how-it-works is questionnaire → provider review → delivery → ongoing messaging; no lab/blood-work step on any captured page.
- **Payment & commitment:** "**No insurance required**" / "no insurance needed" site-wide; "Free consultation · Transparent pricing · Free delivery"; **no membership, no consult fee**. Displayed price is a "**From $X/mo**" floor — the binding all-in (dose/plan/formulation) is set inside the gated `join.mydrhank.com` intake. Commitment terms (cancel/lockup) not stated on the marketing site; "No commitment · 5-min intake" shown on the GLP-1 CTA.

## Notes

- **audience:** read off the pages, not the name. The hero is gender-neutral ("Personalized care for weight, longevity & sexual wellness") and the flagship GLP-1 weight-loss + longevity copy is gender-neutral, but the brand **skews male** — a labeled "**Men's Health**" section (ED), the masculine "**Strength**"/sermorelin line, and male/gym/couple imagery throughout; the Custom Hair Protocol offers "**female-safe formulations**." Male-led but not male-only ⇒ `men-first`, not `all-genders`.
- **pay_model:** "No insurance required / no insurance needed" is stated 6+ times across homepage, category, and PDP pages, with the program framed as "pay only a per-month medication price" — a direct-pay posture ⇒ `cash-pay only`. A "Do I need insurance?" FAQ exists on the PDPs but its answer is a collapsed accordion not captured; **no HSA/FSA signal** appears anywhere (contrast Remedy Meds, where HSA/FSA *is* page-stated).
- **anchor_category:** point-in-time — GLP-1 is the unambiguous front door today, but the bundle ships `/glp/lp/v1–v3` + `/sermorelin/lp/v1–v2` landing variants + GTM A/B testing of copy/IA; re-check on recapture.
