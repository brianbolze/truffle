---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"
domain: gogeviti.com
captured_at: 2026-06-04
value_chain_role: DTC brand              # DTC longevity-telehealth membership; tag what they ARE, not the bundled Rx/labs
pharmacy_model: third-party              # "Geviti's licensed compounding network" / "licensed pharmacies" — named as a network, no owned facility, no named partner
audience: all-genders                    # "founded with the mission to enhance the well-being of both men and women… regardless of gender" (/faq)
compounding_posture: compounded-only     # Rx clinic is "compounded and shipped" across the board; no FDA-brand drug surfaces on the marketing pages
anchor_category: longevity/NAD           # hero "We map your body / longevity"; data-stream-unification → protocol is the front door, not a single therapy
modality: hybrid                         # data-first intake (no required video; "No separate doctor visits needed") + bundled "Provider & coaching visits" / clinic "Virtual visits on as-needed basis"
access_model: membership-required        # "a membership is required to access Geviti's services" (/faq); every test/Rx/supplement gated by Plus
pay_model: HSA/FSA eligible              # "Geviti services are eligible for HSA/FSA reimbursement" (/faq); cash-pay, insurance/Medicare/Medicaid not accepted
---

## Fulfillment

- **Pharmacy (claim, verbatim):** "When clinically indicated, your practitioner can prescribe medications through **Geviti's licensed compounding network**" + "Legally compounded by **licensed pharmacies** · Shipped directly to your door · Managed in the app" — /clinic. "Peptides are **legally compounded by licensed pharmacies** and prescribed under physician supervision" — /faq. Framed as a *network*, not an owned or named pharmacy entity; no sibling pharmacy domain surfaced.
- **Lane:** **not stated on the captured pages.** The profile's "503A/503B" classification is a synthesis, not page-attested — no "503A"/"503B" string appears in any capture; recorded as a generic "licensed compounding network" claim only, no lane.
- **Owns-bit:** no owned-pharmacy claim. The footer disclaims the opposite posture — "GEVITI IS A HEALTHCARE TECHNOLOGY COMPANY AND NOT A LABORATORY OR MEDICAL PROVIDER. ALL LABORATORY AND MEDICAL SERVICES ARE PROVIDED BY INDEPENDENT THIRD PARTIES" (/clinic, /faq footer) → routes to third parties by its own statement.
- **Supplements (separate fulfillment):** custom blends "formulated by our clinical team using **Xymogen** pharmaceutical-grade ingredients" — /supplements (a named ingredient vendor, not a compounding pharmacy).

## Categories served

- **Categories:** longevity/NAD · labs · TRT · womens-HRT · GLP-1 · peptides · supplements · thyroid · skin · hair

## Credibility & access

- **Health-merchant credibility:** **LegitScript — not shown** (no seal in any capture); **named clinicians — no** (pages describe "board-certified longevity practitioners" / "licensed clinicians" but carry no `/physicians` roster — no individual named on the marketing site; founder Nathan Graville is named in profile/homepage, not as a clinician); **pharmacy accreditation — not shown** (no PCAB/NABP/ACHC seal); other trust signals page-stated: HIPAA-compliant, SOC 2 Type II, CLIA-certified partner labs, Quest Diagnostics + Mosaic GI360 + Xymogen + Truemed named.
- **Controlled-substance Rx:** **offers Schedule-III (testosterone/HRT)** — backed by the page-attested product: the gender-neutral **HRT** line and **"Enclomiphene Citrate"** appear on /clinic (hero product image) and the /genetics member-table "Rx catalog (HRT, peptides, GLP-1s, thyroid)"; profile attests testosterone/estrogen/progesterone behind the app. Per-molecule Rx and route are app-walled (no PDP, no price on-site).
- **Labs:** **required-step** inside Plus (100+ biomarker Longeviti Panel 2×/yr drives every protocol; "Schedule Bloodwork — your labs will guide your protocol," /clinic) **and** optional à-la-carte on Free (pay-per-test, app-priced). Draw model: **at-home mobile phlebotomy** (licensed phlebotomist) **or walk-in Quest Diagnostics** with a requisition; results 5–7 days from CLIA-certified labs (/faq). "No lab fees."
- **Payment & commitment:** cash-pay — "Geviti operates as a cash-pay service. **Insurance, Medicare, and Medicaid are not accepted**" (/faq); **HSA/FSA eligible** for reimbursement (itemized invoice; supplements need a Letter of Medical Necessity via the **Truemed** partnership). Commitment: **cancel anytime** ("No long-term contracts · Cancel anytime," /clinic); billed semi-annual or annual; membership fees non-refundable for the remaining period after cancellation (/faq).

## Notes

- **Anchor:** the hero leads with the data-unification / longevity-optimization frame ("We map your body," four data streams → protocol), not a single therapeutic vertical — tagged `longevity/NAD` as the closest closed-set fit for a longevity-membership front door. The site A/B-tests pricing (CRO variant on /pricing, profile-flagged) but the *positioning* anchor is stable across captures; recorded point-in-time.
- **Modality nuance:** front door is data-first and asynchronous (15-min intake questionnaire → bloodwork → AI + care-team protocol; "No separate doctor visits needed," homepage FAQ), but Plus bundles "Provider & coaching visits" and the clinic offers "Virtual visits on as-needed basis" — so synchronous care exists but is not the gate. Tagged `hybrid`.
- **Compounding posture:** tagged `compounded-only` because every Rx the marketing pages describe is "compounded and shipped"; no FDA-brand/commercial drug surfaces. Per-SKU lanes are app-walled, so this is the page-attested company-level roll-up, not an exhaustive audit.
