---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"
domain: eden.health
captured_at: 2026-05-30                   # rides the 2026-05-30 profile.md pages (homepage/about/how-it-works/glp1/faq)
value_chain_role: DTC brand               # "connects you with a network of pharmacies and medical providers" — a brand, not the pharmacy
pharmacy_model: integrated                # owns edenpharmacy.com (footer "More from Eden") + a named 503A partner network — body carries both claims verbatim
audience: all-genders                     # no gendered front door; co-equal Men/Women hair sub-nav, women's-hormones card alongside men's strength lines (see note)
compounding_posture: both                 # compounded semaglutide/tirzepatide/NAD+/sermorelin + branded Ozempic®/Wegovy®/Zepbound®/Mounjaro® + non-Rx Cell Theory
anchor_category: GLP-1                     # front door = weight-loss/GLP-1 (announcement bar, only priced nav tile, BMI funnel) — point-in-time, see note
modality: sync                            # gating consult = "meet with a licensed medical provider 100% online"; "same-day doctor visits"
access_model: membership-required         # mandatory Eden Membership ($39 first mo → $99/mo); "Medication is not available without a membership"
pay_model: HSA/FSA eligible               # "FSA & HSA eligible with all plans"; cash-pay / no-insurance detail in body
---

## Fulfillment
- **Pharmacy:** vertically integrated on paper, on two tracks the captured pages keep distinct.
  - *Owned sibling:* the footer "More from Eden" links **Eden Pharmacy (edenpharmacy.com)** alongside Eden Health Club / Eden Meals (profile `owns:`) — an owned-brand pharmacy domain, but the marketing pages never say "we dispense from our own pharmacy," so ownership-of-dispensing is a claim, not resolved.
  - *Named partner network:* /about names **"a network of pharmacies including GoGoMeds (KY), Precision (NY), Enovex (CA), and AbsolutePharmacy (FL)"** that "offer service to all 50 states and Washington, D.C." — *"Quality-audited & US-licensed 503A pharmacies"* (/about). GLP-1 PDP: *"prepared in compounding pharmacies licensed by the State Board of Pharmacy or in FDA-licensed 503(a) outsourcing facilities… licensed in all 50 states."*
  - **Lane: 503A** (page-stated, repeatedly); no 503B claim. Posture recorded `integrated` for the owned-domain + captive-network mix; neither dispensing-ownership claim is adjudicated.

## Categories served
- **Categories:** GLP-1/weight-loss · longevity/NAD · peptides (sermorelin/GHK-Cu) · sexual-health/ED (vardenafil+tadalafil) · hair · womens-HRT · mental-health/mood (MIC+B12, methylene blue) · skin · supplements (non-Rx Cell Theory)

## Credibility & access
- **Health-merchant credibility:** LegitScript-certified (footer/about seal); named clinicians (/about medical team — Dr. Halland Chen MD, Dr. Rebecca Emch PharmD, advisory board Dr. Matthew Bennett MD, Dr. William Lee MD); pharmacy accreditations shown on /about — **NABP, PCAB (compounding), ACHC**
- **Controlled-substance Rx:** non-scheduled only — no TRT/testosterone SKU on the captured catalog; the testosterone-adjacent line is **Sermorelin** (a non-scheduled GH secretagogue), and "Strength" is sermorelin + vardenafil/tadalafil, not Schedule-III androgens
- **Labs:** none as a gating step — journey is "quick form → meet a provider 100% online → ship"; "FDA-registered labs" appears as a trust badge, but no biomarker panel is required to start (no lab step in the 3-step flow)
- **Payment & commitment:** **HSA/FSA eligible "with all plans"**; explicitly cash-pay / insurance-free — *"Medication made affordable / Without the need for insurance"* (GLP-1 PDP), *"you don't need insurance… You can use an HSA or FSA card for most visits and prescriptions"* (FAQ). Commitment: **cancel-anytime, no long-term contracts** (per-PDP + portal-cancel); buy-now-pay-later via Klarna/Afterpay. Membership is the recurring annuity ($99/mo) decoupled from the med price ("Same Price at Every Dose" guarantee).

## Notes
- **anchor_category:** point-in-time snapshot, not fixed. The homepage H1 is an animated rotator cycling goal words ("Weight loss · Muscle growth · Anti-aging · Hormones · Mental health · Hair regrowth · tailored to you"), so the literal first word is non-stable. Recorded `GLP-1` off the **durable** front-door signals: the persistent announcement bar ("Compounded semaglutide for $99/mo"), the only nav tile carrying a price + the `*Plus Eden Membership` asterisk ("Personalized GLP-1 Treatments — From $99/mo"), the BMI-calculator homepage funnel, and the first homepage card ("Personalized GLP-1 Treatments for weight loss"). Weight-loss is unambiguously the wedge; the goal-quiz still defaults to "Lose weight."
- **audience:** no single-gender front door — the goal selector and homepage cards span weight loss, muscle, anti-aging, hair (with **co-equal Men/Women** hair sub-nav), and a women's-hormones card. Women-only (Hormone Therapy for Women) and men-leaning (finasteride, the "Strength" line) offerings sit side by side, so `all-genders` rather than men-/women-first.
- **modality:** the gating consult is a synchronous provider visit, not a pure async questionnaire — "Submit your application and **meet with a doctor**," "meet with a licensed medical provider 100% online," "Same-day doctor visits & prescriptions," "Start your free telehealth consultation… with a licensed provider." Per-SKU consult mix stays in `offerings.md`.
