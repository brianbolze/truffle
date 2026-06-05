---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"
domain: niagenplus.com
captured_at: 2026-06-04
value_chain_role: DTC brand              # sells its own Rx Niagen® kit direct via a telehealth-gated Shopify cart — tag what they ARE, not the 503B compounder they bundle
pharmacy_model: unclear                  # ships from an unnamed "licensed 503A pharmacy"; compounded by an unnamed "licensed 503B outsourcing facility" — no ownership claim, no named partner, brand explicitly disclaims being the compounder
audience: all-genders                    # no gendered hub or hero; longevity/cellular-health framing; PDP + IV imagery shows both men and women
compounding_posture: compounded-only     # every format is compounded by a 503B outsourcing facility / ships from a 503A pharmacy; no FDA-brand drug, not OTC (Rx-gated)
anchor_category: longevity/NAD           # hero "A new way to access Niagen®… the science of cellular health"; Niagen® = NAD+ precursor
modality: async                          # front-door gating consult is a "medical intake questionnaire… reviewed by a licensed physician" — no live video required
access_model: per-visit                  # $299 one-time per kit (consult fee bundled in); no membership, no on-site subscription captured
pay_model: unclear                       # only Amex/MC/Visa logos shown; site is silent on insurance / HSA-FSA / direct-pay — no payer-rail signal either way
---

## Fulfillment
- **Pharmacy (claim, verbatim):** "The Niagen® At-Home Injection Kit ships from a licensed **503A** [compounding] pharmacy" and "Compounding is performed by a licensed **503B outsourcing facility**" — homepage / kit-PDP / about disclaimers. The brand explicitly distances itself: "**Niagen Bioscience is not the manufacturer or compounder of this product**" (kit PDP). No pharmacy entity is **named**, no owned-facility claim, no sibling pharmacy domain — so vertical integration is page-undetermined (`pharmacy_model: unclear`), recorded as a claim, not adjudicated.
- **Lane:** **503A** dispensing pharmacy + **503B** outsourcing facility (cGMP, "federally registered, FDA-inspected," "third-party verification of purity and potency") — page-stated on the kit PDP and the in-clinic page. In-clinic Niagen Shots are likewise "compounded by a licensed 503B outsourcing facility."

## Categories served
- **Categories:** longevity/NAD (single vertical — one molecule, Niagen® / NRCl, across at-home subcutaneous · in-clinic IV · in-clinic intramuscular)

## Credibility & access
- **Health-merchant credibility:** LegitScript certification — **not shown** (no footer seal); named clinicians — **no `/physicians` roster** (consults handled by an unnamed "licensed physician"; only an external KOL, **Dr. Rachele Pojednic, CSO at Restore Hyper Wellness**, is named in an IV-page testimonial); pharmacy accreditation (PCAB/ACHC/NABP) — **not shown** (503A/503B framework cited, no seal).
- **Controlled-substance Rx:** **non-scheduled only** — page-attested by product: the entire catalog is Niagen® (nicotinamide riboside chloride, "a form of vitamin B3"), an NAD+ precursor. No TRT/testosterone or other scheduled SKU appears.
- **Labs:** **none** — no lab panel or blood draw is sold or required; eligibility is set by the intake questionnaire + physician review, not a lab result.
- **Payment & commitment:** payer rail **unclear** — only Amex / Mastercard / Visa accepted; no insurance, HSA, FSA, or direct-pay copy on any captured page. Commitment is **per-purchase** — $299 one-time per at-home kit (the $20 consult fee is *inside* the $299, not added), no membership, no subscription captured. Refund terms (page-stated): full refund if the Rx is declined, the buyer is ineligible, or the intake lapses after 30 days; **"once a prescription has been approved and issued, the order is final"** (kit PDP / FAQs). Not shipped to AL, CA, IA, MA, TX, WA, WV.

## Notes
- **In-clinic channel is sync/in-person** (Niagen IV infusion + Niagen Shots IM injection, "administered by licensed healthcare professionals at select premium clinics nationwide," 1,200+ locations, accessed via a clinic locator) — but the *front-door telehealth consult* that gates the buyable at-home kit is async (questionnaire → physician review), which sets `modality`.
- **Anchor is stable, not rotating:** the hero leads single-mindedly with Niagen®/NAD+ cellular health across every captured page — no A/B-rotating multi-category grid — so `anchor_category: longevity/NAD` is not a point-in-time snapshot of a rotating hero.
