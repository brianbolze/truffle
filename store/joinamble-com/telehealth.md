---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"
domain: joinamble.com
captured_at: 2026-06-18
value_chain_role: DTC brand
pharmacy_model: third-party
audience: all-genders
compounding_posture: both
anchor_category: GLP-1
modality: hybrid
access_model: all-in
pay_model: HSA/FSA eligible
---

## Fulfillment
- **Pharmacy:** third-party / affiliated network, stated verbatim — *"Amble acts as a managed services provider and does not offer medical advice, fill prescriptions, or function as a licensed healthcare facility or pharmacy. Instead, it provides technology and administrative support…"* and *"Prescriptions issued through Amble may be filled by licensed pharmacies within its affiliated network."* **No owned pharmacy, no named partner, no sibling pharmacy domain.** Same rails fill both the subscription therapeutics and the new medkit line.
- **Lane (page-stated):** 503A + 503B — *"503A pharmacies are licensed by state boards of pharmacy, while 503B pharmacies are registered by the FDA. Both… operate under state and FDA regulations"* (/faq). An educational mention, not a claim to operate either.

## Categories served
- **Categories:** GLP-1/weight-loss · longevity/NAD · peptides (sermorelin) · metabolic/lipotropic (Lipo-B/B12, Lipo-C) · skin · **emergency/preparedness Rx kits (NEW)** — 8 one-time "just in case" kits (travel, cold/flu, mold-allergy, antiviral, radiation, first-aid, field) of named generic antibiotics/antivirals/antiparasitics + supplies.

## Credibility & access
- **Health-merchant credibility:** **no LegitScript seal** found in the footer; providers described as *"physicians… licensed in all 50 states"* but **no named-clinician / `/physicians` page**; no PCAB/ACHC/NABP accreditation shown.
- **Controlled-substance Rx:** non-scheduled only — GLP-1, peptides (sermorelin), NAD+, lipotropic/B12, topical skincare, and the medkit generics (antibiotics, antivirals, antiparasitics incl. ivermectin/HCQ, potassium iodide, epinephrine); **no TRT/testosterone or other scheduled product appears**.
- **Labs:** none — the journey is questionnaire → physician review → (consult where state law requires) → ship; **no required or optional bloodwork step is stated**.
- **Payment & commitment:** cash-pay, **no insurance** (*"transparent, all-inclusive pricing"*); **HSA/FSA accepted for 3-month-or-longer plans** (itemized receipts). Therapeutics sold as plan-length subscriptions (1/3/6/12-month, longer = cheaper per month); medkits sold **one-time upfront** ($285–$945). BNPL via Affirm/Klarna/Afterpay. Explicit cancellation terms not page-stated. Amble Cares (GLP-1 access program) is direct-pay only — cannot combine with insurance or FSA/HSA.

## Notes
- **`compounding_posture: both` (CHANGED 6/04→6/18, was `compounded-only`)** — the therapeutic line is still 100% compounded (incl. compounded semaglutide/tirzepatide, not branded), but the new medkit line dispenses **named FDA-approved generics** (amoxicillin-clavulanate, doxycycline, azithromycin, metronidazole, valacyclovir, ivermectin, potassium iodide, etc.). So the company-level roll-up is now `both`, not compounded-only.
- **`access_model: all-in`** — no membership fee on the care relationship; the medkit line is a one-time à-la-carte product purchase layered on top, not a separate membership tier (kept `all-in` as the dominant fee architecture; one-time kits noted under Payment).
- **`anchor_category: GLP-1` is A/B-volatile** — the hero rotates Anti-aging ⇄ Weight loss (showed Anti-aging first this run); GLP-1/weight-loss is the durable lead (referral counts only Weight Loss; Amble Cares is weight-loss-only). The medkit line is homepage-featured but has no `anchor_category` enum value and is not the front-door lead. Point-in-time per the profile's snapshot caveat.
- **`modality: hybrid`** — async online questionnaire is the front door; a *"live video or phone consultation"* runs only *"where required by state law,"* so the gating consult is async-default with sync-where-mandated.
