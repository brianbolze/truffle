---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"          # the telehealth-pack version (independent of profile.md's)
domain: fountaintrt.com
captured_at: 2026-06-20        # rides the same homepage / terms / consent / assessment capture as profile.md
value_chain_role: DTC brand
pharmacy_model: third-party              # Fountain collects/remits payments to pharmacies that work with the Platform; no owned/named pharmacy claim
audience: men-only                       # public copy is explicitly men's Low T / TRT; no women's line surfaced
compounding_posture: unclear             # testosterone cream/injection/oral enclomiphene are stated; compounded vs FDA-brand status is not
anchor_category: TRT
modality: sync                           # prescription decision follows a scheduled real-time, two-way video visit after labs
access_model: membership-required        # "FountainTRT membership"; all-inclusive monthly membership
pay_model: cash-pay only                 # terms say users choose cash-basis care outside insurance; lab billing may be separate
---

## Fulfillment

- **Pharmacy:** no owned or named pharmacy is stated. Terms say Fountain collects/remits payment for services rendered by Providers **and pharmacies that work with the Platform**; homepage says **"Let Fountain deal with the pharmacy for you."** This supports third-party/unspecified pharmacy fulfillment, not integrated ownership. 503A/503B lane: not stated. Clinical care is separate from Fountain's platform/admin layer: terms say Fountain does **not** own, employ, supervise, or control the Providers, and the consent page names **Quaker Ridge Medical, PLLC** or other affiliated professional medical entities.

## Categories served

- **Categories:** TRT / Low T / testosterone optimization (topical testosterone cream on homepage; assessment app adds injection/topical testosterone and oral enclomiphene). Sexual-health/ED appears in consent-risk language for PDE5i treatment, but not as a public nav or marketed product line in this capture.

## Credibility & access

- **Health-merchant credibility:** LegitScript-certified (footer verification link); named clinician **yes** — Doron Stember, MD, board-certified urologist and co-founder; pharmacy accreditation not shown; Trustpilot widget on assessment page shows **4.5 / 293 reviews**.
- **Controlled-substance Rx:** offers Schedule-III (testosterone/TRT) — page-attested by the TRT/testosterone cream product and assessment-page testosterone options.
- **Labs:** required-step — homepage says users get a blood test at partner labs, then a Fountain doctor reviews the lab report before the video visit/prescription decision.
- **Payment & commitment:** cash-pay platform/services outside insurance; lab provider may bill a managed-care plan/third-party payer or the user directly. Membership price floor is **"$199 per month--All Inclusive"**; assessment says money-back if the user does not qualify; homepage FAQ says **"You can cancel at any time."**

## Notes

- **compounding_posture:** kept `unclear` deliberately. The site says topical testosterone cream and the assessment says injection/topical testosterone or oral enclomiphene, but no captured page states whether those are compounded medications, FDA-brand finished drugs, or both.
- **modality:** `sync` because the site describes a scheduled **"real time, two-way video visit"** as the pre-prescription consultation step after labs; the initial assessment is async, but the gating consult is live.
- **pay_model:** `cash-pay only` follows the explicit financial-responsibility language, while preserving the lab carve-out in the body because lab billing can route to a plan or direct bill.
