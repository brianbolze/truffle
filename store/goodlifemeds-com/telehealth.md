---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"
domain: goodlifemeds.com
captured_at: 2026-06-04
value_chain_role: DTC brand
pharmacy_model: third-party              # "partners with U.S.-based, state-licensed pharmacies" — no named/owned facility
audience: all-genders                    # gender-neutral weight-loss + wellness; explicit for-men/for-women splits in sexual-health + hair
compounding_posture: both                # compounded tirzepatide/semaglutide/peptides + FDA-brand Wegovy/Ozempic/Zepbound/Mounjaro/Cialis/Viagra
anchor_category: GLP-1                    # weight loss is line "01," hero = Compounded Tirzepatide ("Most Popular")
modality: async                          # free medical-intake form reviewed by a licensed provider; no video/sync visit surfaced
access_model: all-in                     # "one affordable cost" (visit + meds + shipping); "No memberships requirements" (lone exception: Wegovy Pill's $74 fee)
pay_model: cash-pay only                 # "Insurance isn't needed at Good Life"; no HSA/FSA/insurance rail mentioned
---

## Fulfillment

- **Pharmacy (claim, verbatim):** *"Good Life partners with U.S.-based, state-licensed pharmacies"* (PDPs) and *"we connect patients across all 50 states with licensed healthcare professionals and pharmacies"* (homepage FAQ). No pharmacy entity is named and no owned facility is claimed → recorded as `third-party`; ownership not adjudicated.
- **Lane (page-stated):** both **503A and 503B** — *"503A pharmacies are licensed by state boards of pharmacy, while 503B pharmacies are registered and overseen by the FDA. Both types… are subject to FDA regulations"* (homepage FAQ). Compounded SKUs carry the patient-specific **Section 503A** dispensing disclaimer.
- **Quality (claim):** *"All formulations undergo third-party analytical testing to confirm potency and strength as labeled"*; PDPs add per-batch Potency / Sterility (USP 797) / pH / Endotoxicity (USP 85) testing under "cGMP regulations."

## Categories served

- **Categories:** GLP-1/weight-loss · sexual-health/ED · hair · longevity/NAD · peptides (sermorelin) · daily-wellness/vitamins (B12 · MIC · glutathione)

## Credibility & access

- **Health-merchant credibility:** **Trustpilot** "Excellent — 4.5 out of 5… 1,884 reviews" (self-embedded TrustBox); *"Board certified physicians"* trust-bar claim. **LegitScript** seal — not shown in captures. **Named clinicians** — no /physicians page (none named). **Pharmacy accreditation** (PCAB/ACHC/NABP) — not shown.
- **Controlled-substance Rx:** **non-scheduled only** — no TRT/testosterone product in the catalog; offerings are GLP-1, ED (sildenafil/tadalafil), hair, and wellness injectables (all non-scheduled). Backed by the absence of any testosterone SKU.
- **Labs:** **none** — the front door is a self-reported medical-intake + health-history form; no bloodwork/lab draw step (the BMI calculator is informational only, "does not determine eligibility").
- **Payment & commitment:** **cash-pay only** — *"Insurance isn't needed… your medication, medical visit, and shipping are all included in one affordable cost."* Medications are **auto-renewing subscriptions** ("automatically renews at the selected billing interval unless cancelled before the next renewal date"); intervals vary by SKU (monthly / quarterly / 6-month on tirzepatide). **Full refund if not approved** ("you will be notified and receive a full refund… includes a cancellation of any subscription memberships you selected"). Page-stated terms only.
