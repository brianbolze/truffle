---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"
domain: defymedical.com
captured_at: 2026-06-04
value_chain_role: DTC brand
pharmacy_model: third-party              # "a network of pharmacies" — no owned facility named (body Fulfillment carries the verbatim claim)
audience: men-first                      # leads Men's Health + TRT ("specializes in Men's Health"); full parallel women's line — see note
compounding_posture: both                # custom Trimix/Bimix/Quadmix + BHRT (compounded by nature) alongside FDA-approved generics (Sildenafil, Tadalafil); see note
anchor_category: TRT                     # "The World's Leading Hormone Replacement Clinic"; TRT first nav + "Popular"
modality: sync                           # extended 1-hour live telemedicine consult is the gating step (+ in-person Tampa clinic)
access_model: à-la-carte/both            # "No subscriptions or contracts… only pay for what you need" — per-consult + à-la-carte meds/labs/supplements
pay_model: cash-pay only                 # "does not accept insurance or communicate with insurance companies directly"
---

## Fulfillment
- **Pharmacy:** third-party network, no owned facility named. Verbatim: *"Defy Medical prescribes a variety of medications from a network of pharmacies as appropriate for the patient. Our prescription management is included in the overall cost of care. We prescribe medications from pharmacies that meet high standards, follow USP and Good Manufacturing Practices, and utilize FDA-approved active ingredients."* (/about-us). Also: *"Progressive hormone therapies… involve a variety of medications from different pharmacies. Using an expansive pharmacy network allows our providers to… offer extended patient choice"* (/about-us/about-us-vendor-information). Lane: no 503A/503B statement — but the custom penile-injection formulas (Trimix/Bimix/Quadmix) and bioidentical-hormone preparations are compounded by nature.

## Categories served
- **Categories:** TRT · ED/sexual-health · BHRT/womens-HRT · menopause · GLP-1/weight-loss · thyroid · labs · peptides/anabolic · ketamine/mental-health · IV/nutrition · hair-loss · skin/aesthetics · joint-pain · primary-care

## Credibility & access
- **Health-merchant credibility:** Trustpilot 5/5 across "3784" reviews (rating itself lives in profile.md Credibility); named clinicians — Dr. Justin Saya, MD (medical director) + full provider roster at /about-us/team-bios; HIPAA/CFR-compliant platform; pharmacy partners follow USP + GMP. LegitScript certification + pharmacy accreditation seals (PCAB/NABP/ACHC) not shown on captured pages.
- **Controlled-substance Rx:** offers Schedule-III (injectable / topical / pellet / nasal-gel testosterone — TRT) — /services/trt
- **Labs:** required-step for HRT monitoring — partner **laboratory physician cooperative** contracting accredited national labs ("an average of 92% off the retail price"); at-home mobile phlebotomy via Getlabs (FAQ); plus a standalone on-demand lab store at **testdefy.com**.
- **Payment & commitment:** cash-pay only — *"To provide reliable and affordable pricing, Defy Medical does not accept insurance or communicate with insurance companies directly"* (/services/semaglutide-for-weight-loss). **No subscriptions or contracts** — "you control your schedule and cost decisions, and only pay for what you need" (/get-started); per-consult + à-la-carte.

## Notes
- **audience:** treats men and women, but the site leads men: "Our care team specializes in Men's Health and uses the latest research and advancements in TRT" (/get-started, /services/trt), TRT is the first nav item + "Popular", and the anchor positioning is the "World's Leading Hormone Replacement Clinic." A full **parallel women's line** exists (Hormone Therapy/BHRT, Menopause, Female Sexual Dysfunction, a Women's Questionnaire), and the homepage hero is mixed-gender — hence `men-first` (men-lead, women fully served), not `men-only`.
- **compounding_posture:** the site never uses the literal word "compounded," instead emphasizing "FDA-approved active ingredients / USP / GMP." But it sells custom-formulated preparations that are compounded by definition — the Trimix family (Phentolamine + Alprostadil + Papaverine and its Super/Bi/Quad variants) and bioidentical hormone injectables/creams/capsules — alongside FDA-approved generics (Sildenafil, Tadalafil). Hence `both`. Per-SKU lane labeling is absent (see profile `unverified_fields`).
- **modality:** the gating consult is a live, **extended 1-hour telemedicine** visit (sync); an in-person **Tampa clinic** (walk-ins) is a secondary channel, and international patients get advice-only consults.
