---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"          # the telehealth-pack version (independent of profile.md's)
domain: telolife.com
captured_at: 2026-06-04         # rides the 2026-06-04 profile.md pages (homepage, /packages, /pricing, /financing, /legal/terms.html)
value_chain_role: DTC brand              # "TeloLife is a technology platform that facilitates access to telehealth services" fronting a consumer GLP-1 weight-loss brand
pharmacy_model: third-party              # "Coordination with licensed compounding pharmacies"; meds "prepared by FDA-registered, state-licensed compounding pharmacies" — no owned/named pharmacy (see Fulfillment)
audience: all-genders                    # no gendered front door — gender-neutral "Weight loss, made simple."; no /mens or /womens hub (lone testimonial is a woman, not a structural cut)
compounding_posture: compounded-only     # "Medications dispensed through TeloLife are compounded GLP-1 medications… not FDA-approved drug products" (Terms §9); no FDA-brand SKU
anchor_category: GLP-1                    # entire site is GLP-1 weight loss — single-category brand
modality: async                          # front-door consult is the online questionnaire → clinician review; "asynchronous (store-and-forward)… and where applicable, video or audio" (Terms §5)
access_model: all-in                     # "ALL-INCLUSIVE REGARDLESS OF DOSAGE… No consultation fees, No shipping fees, No membership fees" (/pricing) — the monthly plan IS the all-in, no separate membership
pay_model: HSA/FSA eligible              # "TeloLife services may be eligible for payment using HSA or FSA funds" (Terms §7); cash-pay, no insurance — HSA/FSA is the page-stated positive payer signal
---

## Fulfillment

- **Pharmacy:** **third-party, unnamed.** TeloLife "facilitates access to telehealth services" and its services include *"Coordination with licensed compounding pharmacies for medication dispensing and delivery"* (Terms §2); meds are *"compounded GLP-1 medications prepared by FDA-registered, state-licensed compounding pharmacies… prepared pursuant to valid prescriptions for individual patients"* (Terms §9). **No owned pharmacy and no named pharmacy partner** appear anywhere on the captured pages — no owned-pharmacy sibling domain, no PCAB/NABP entity. The "prepared pursuant to valid prescriptions for individual patients" language is **patient-specific compounding (503A-style)**, but the pages **do not state a 503A/503B lane** — recorded as not-stated, not inferred. Coarse posture is `third-party` (explicit coordination with outside compounding pharmacies, no ownership claim to merge into `integrated`).

## Categories served

- **Categories:** GLP-1 / weight-loss — **single-category.** Two molecules (semaglutide · tirzepatide), no other vertical (no TRT, sexual-health, hair, skin, labs, mental-health). `anchor_category: GLP-1` is the whole of it, not a slice.

## Credibility & access

- **Health-merchant credibility:** **LegitScript-certified** — footer seal linking to LegitScript verification (*"verified for safe, transparent telehealth practices"*). **Named clinicians: no** — care is delivered by anonymous *"independent, licensed Provider Groups"*; no /physicians or /medical-team page, no provider named. **Pharmacy accreditation: none shown** (no PCAB/ACHC/NABP; no named pharmacy at all). HIPAA-compliance stated (footer + HIPAA Notice page).
- **Controlled-substance Rx:** **non-scheduled only** — the page-attested product is compounded GLP-1 (semaglutide/tirzepatide), which are not controlled substances; no TRT/testosterone or other scheduled SKU appears. *"A completed intake form does not guarantee a prescription. All prescribing decisions are made exclusively by our licensed Provider Groups"* (Terms §3).
- **Labs:** **none** — intake is an online health questionnaire only (*"Answer a quick online health questionnaire"*, ~5 min); no bloodwork/lab panel is a step, required or optional, in the captured flow.
- **Payment & commitment:** **HSA/FSA eligible** (*"may be eligible for payment using Health Savings Account (HSA) or Flexible Spending Account (FSA) funds"*, Terms §7) and **cash-pay, no insurance** (*"No insurance required"*; *"No insurance headaches, no surprise bills"*). Third-party **Cherry financing** (soft credit check, ~30s, up to $50,000, qualifying 0% APR) plus pay-in-4 (Affirm/Klarna/Afterpay) and Apple/Google Pay; cards processed by Stripe. Commitment: **cancel-anytime** (*"cancel your subscription at any time… Cancellation takes effect at the end of your current billing period"*, Terms §8), monthly auto-renew, or a **prepaid 3/6/9/12-month bundle**. Refund: full refund if the Provider Group declines candidacy pre-prescription; **no refund after medication is dispensed** (Terms §8). The "results guarantee" is a plan-adjustment, not money-back.

## Notes

- **modality:** `async` — the gating/front-door consult is the store-and-forward questionnaire reviewed by a clinician; Terms §5 names synchronous video/audio only *"where applicable,"* so the default GLP-1 journey is asynchronous (not a co-equal hybrid).
- **access_model:** `all-in` (not `membership-required`) — TeloLife explicitly charges **"No membership fees"**; the monthly plan price bundles platform + clinician oversight + medication + shipping into one all-inclusive figure, so there's no separate membership rail to gate on.
- **pay_model:** asymmetric fill — the strongest **positive** payer signal is page-stated **HSA/FSA eligibility**; it does **not** bill insurance (cash-pay only otherwise). HSA/FSA is the load-bearing distinction over a bare `cash-pay only`.
- **value_chain_role:** `DTC brand` despite the self-description as a "technology platform" — it transacts directly with consumers under its own brand for GLP-1 weight loss; the platform/Provider-Group/pharmacy split is the standard DTC-telehealth legal structure, not a `platform/infra` (B2B) play.
