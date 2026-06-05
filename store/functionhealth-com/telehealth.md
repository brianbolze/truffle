---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"          # the telehealth-pack version (independent of profile.md's)
domain: functionhealth.com
captured_at: 2026-06-01        # rides the profile's 2026-06-01 capture (homepage, /pricing, /scans)
value_chain_role: diagnostics/labs        # a consumer lab-testing + imaging membership; self-describes "healthcare technology company — not a lab or medical provider" (Quest runs labs, Ezra the scans)
pharmacy_model: none/diagnostics-only     # owns no pharmacy, sells no meds — diagnostics + imaging only
audience: all-genders                     # parallel "Male Health" + "Female Health" test areas; no gendered hero or /mens|/womens hub
compounding_posture:                      # N/A — sells no pharmaceuticals (diagnostics/imaging only); left empty over a guessed value
anchor_category: labs                     # front door leads with "160+ lab tests", "Test twice a year for $365"
modality: async                           # no gating consult — join & test; clinicians review every result, critical results trigger a provider call
access_model: membership-required         # "There's just one Function membership"; scans + advanced tests are member-only à-la-carte add-ons on top
pay_model: HSA/FSA eligible               # "HSA/FSA Eligible" on membership + scans; "No insurance, transparent pricing" (cash-pay, no insurance billing)
---

## Fulfillment

No pharmacy and no medications — Function is a **diagnostics + imaging** membership, and explicitly *not* a provider:
- **Self-description (verbatim):** *"healthcare technology company — not a lab or medical provider"* — independent third parties run the labs and medical services. Function facilitates access; labs/imaging/medical services are billed and provided by those third parties.
- **Labs:** drawn by **Quest Diagnostics** (third-party) — *"2,000+ lab test locations across the US"* — plus **Getlabs** mobile phlebotomy in select areas. **No at-home kits by design** ("they risk sample integrity").
- **Imaging:** full-body MRI/CT via **Ezra** (acquired 2025; runs as a named brand under Function — Ezra's CEO Emi Gal and CMO Danna Chung MD sit on Function's team). Scans booked through Function signup or *"Book directly with Ezra"* (my.ezra.com). **No 503A/503B lane** — not applicable (no compounding, no Rx).

## Categories served

- **Categories:** labs/biomarkers (anchor) · full-body MRI/CT imaging · multi-cancer screening (Galleri®/GRAIL) · longevity/biological-age · hormones & fertility · metabolic · cardiovascular (beyond-cholesterol) · brain/Alzheimer's · environmental toxins & mold · sexual-health (testing) · autoimmunity · thyroid

## Credibility & access

- **Health-merchant credibility:** named clinicians — **yes** (Medical & Scientific Advisory Board: JoAnn Manson/Harvard, Andrew Huberman/Stanford, Toby Cosgrove/ex-Cleveland Clinic, Daniel Sodickson/NYU, Azra Raza/Columbia, et al.; **Mark Hyman MD** as Co-Founder/CMO); **SOC 2 Type II + HIPAA-aligned**. LegitScript seal / pharmacy accreditation — **N/A** (not a pharmacy). Press: TIME100, Fast Company.
- **Controlled-substance Rx:** **none** — diagnostics/imaging only; **no prescription products** on the captured pages (testosterone, hormones, etc. appear only as *biomarkers tested*, never as Rx SKUs).
- **Labs:** **the product itself** — 160+ biomarkers drawn **2×/year** (Annual Test + a Mid-Year retest), at Quest (2,000+ locations) or Getlabs mobile; **clinician-reviewed every result**, critical results trigger a provider call. No at-home kits.
- **Payment & commitment:** **HSA/FSA eligible**; cash-pay, **no insurance billing** (*"No insurance, transparent pricing"*). Annual membership **$365/year** ("$1/day"). The Mid-Year Test **doesn't roll over** (must be used before annual renewal). Cancellation terms not stated on captured pages.
