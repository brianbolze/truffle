---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"          # the telehealth-pack version (independent of profile.md's)
domain: onemedical.com         # company key (same as profile.md)
captured_at: 2026-06-04        # base pages reused from 2026-06-02; +4 program pages (mindset, chronic-conditions, kids, lab-services) 2026-06-04
value_chain_role: DTC brand              # a consumer/employer-facing primary-care practice — sells care direct, not a pharmacy/lab/infra supplier
pharmacy_model: third-party              # full-scope PCP that e-prescribes to outside pharmacies; no captive pharmacy claimed (body)
audience: all-genders                    # whole-person/whole-family primary care — adults, kids, seniors; no gendered front door
compounding_posture: FDA-brand-only      # licensed medical practice prescribing standard commercial drugs; no compounded-med line, no FDA-compounding disclaimers
anchor_category: primary-care            # homepage title "Exceptional Primary Care"; the front door IS primary care, not a single vertical
modality: hybrid                         # app-first 24/7 virtual care + in-office visits + scheduled video — bricks-and-mortar + telehealth
access_model: membership-required        # annual membership ($199/yr; $99/yr via Amazon Prime) on top of insurance; seniors/Medicare line is the exception (body)
pay_model: bills insurance               # "we will bill your insurance" for visits; accepts Medicare — the cohort's payer-rail outlier (most peers are cash-pay)
---

## Fulfillment
- **Pharmacy:** No captive/owned pharmacy claimed on any captured page. As a full-scope primary-care practice it **e-prescribes to the patient's pharmacy of choice** — "request prescription renewals and refills right in our app" (/services/mindset); PCPs "prescribe, review, monitor, and even adjust your medications." Amazon Pharmacy exists as a **parent sibling** in Amazon Health, cross-sold post-acquisition, but is **not** One Medical's own pharmacy — so fulfillment reads `third-party`. No 503A/503B compounding lane (not a compounder).

## Categories served
- **Categories:** primary-care · everyday-care · wellness-and-prevention · annual-wellness-visit · chronic-conditions (Impact: diabetes · hypertension · obesity · lipids · heart disease) · mental-health (Mindset) · pediatrics/kids · sexual-health/STI · labs · LGBTQIA+ care · urgent-concerns · vaccines · seniors/Medicare (65+)

## Credibility & access
- **Health-merchant credibility:** A **licensed primary-care medical practice** (bricks-and-mortar + virtual), not an online-pharmacy storefront — so the DTC-pharmacy seals don't apply: **no LegitScript seal** observed (not the relevant credential for this model). **Named clinicians: yes** — public provider directory at /providers/ with bios, filterable by market and pediatric/seniors; board-certified pediatricians and family-medicine providers (/services/kids). Pharmacy accreditation: **N/A** (no pharmacy). On-site labs staffed by trained phlebotomists.
- **Controlled-substance Rx:** Full-scope primary care — "all of our primary care providers are qualified to prescribe medication when appropriate and manage dosing as needed" (/services/mindset); PCPs prescribe scheduled and non-scheduled meds **when clinically appropriate**. **No TRT/testosterone storefront SKU** — this is comprehensive primary care, not a controlled-substance-anchored vertical brand.
- **Labs:** `optional` (provider-ordered, not a mandatory intake step). **On-site drop-in phlebotomy** at every office during designated lab hours — "no appointment needed," but **requires established care** (≥1 prior appointment). Draw model: **own offices draw → third-party labs process** ("LabCorp and Quest"); results returned in-app in ~3–5 business days. Also fulfills outside providers' lab orders. Services: standard blood panels · STI testing · vaccines · specimen collection · PrEP monitoring (/services/lab-services).
- **Payment & commitment:** `bills insurance` — "For in-office appointments and remote visits, we will bill your insurance" (/insurance); accepts most carriers, Original Medicare, select Medicare Advantage, Medigap (**not Medicaid**). **Membership fee is cash and explicitly NOT HSA/FSA-covered** — "The Annual Membership Fee is not a covered benefit under most health insurance plans or other healthcare benefit plans such as the Health Saving Account or Flexible Spending Account" (/insurance). **Self-pay** option for the uninsured. Commitment: annual membership, **"continues until canceled"** (cancel-anytime, auto-renews at then-current price); copays/deductibles apply to visits. 24/7 Video Chat / Treat Me Now is included and **not billed to insurance**. Seniors (65+) Medicare line carries **no separate membership fee**.

## Notes
- **The cohort outlier, by design.** One Medical is the **insurance-integrated, bricks-and-mortar, FDA-brand primary-care** end of telehealth — the inverse of the cash-pay, ship-to-door, compounded-Rx men's-health brands the cohort is built around. The cuts capture that contrast crisply: `pay_model: bills insurance` (vs cash-pay), `modality: hybrid` (vs async), `anchor_category: primary-care` (vs TRT/GLP-1), `compounding_posture: FDA-brand-only` (vs compounded-only/both). Page-attested, not adjudicated.
</content>
</invoke>
