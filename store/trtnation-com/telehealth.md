---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"             # the telehealth-pack version (independent of profile.md's)
domain: trtnation.com            # company key (same as profile.md)
captured_at: 2026-06-04          # rides the 2026-06-04 profile.md + offerings.md capture
value_chain_role: DTC brand      # online men's-health clinic selling its own catalog; routes to outside pharmacies — it IS a brand, not a pharmacy/platform
pharmacy_model: third-party      # "licensed U.S. compounding pharmacies" / "our pharmacy partner" — plural, no ownership claim, no sibling pharmacy domain
audience: men-first              # men's-health-branded front door (TRT flagship, "adult male 24+"), but weight-loss + labs are not gender-gated (lab form accepts Female) — body note
compounding_posture: both        # compounded testosterone/tirzepatide/peptides alongside standard small-molecule generics (phentermine 37.5mg, sildenafil, tadalafil); no FDA brand-name drug
anchor_category: TRT             # brand namesake; homepage hero "#1 IN THE NATION… $99/mo"; first nav item
modality: sync                   # step 3 = "Meet with a licensed provider via video or phone" — a live consult gates treatment
access_model: à-la-carte/both    # no membership wrapper; each treatment is its own monthly subscription priced independently, consult/support bundled in
pay_model: cash-pay only         # "No confusing insurance red tape"; "One simple monthly fee" — insurance-free direct-pay; no HSA/FSA claim shown
---

## Fulfillment

- **Pharmacy (claim, verbatim):** "All medications prescribed through TRT Nation are sourced from **licensed U.S. compounding pharmacies**. You will never receive counterfeit or unregulated substances." — /faqs/. Also: "Medications are prescribed by licensed healthcare providers and **dispensed through regulated U.S. pharmacies** following a medical screening and provider consultation." — homepage FAQ; "Premium medications – **Direct from licensed USA pharmacy**" — /about/; "the return address is that of **our pharmacy partner**, not a branded medical company" — /faqs/. No owned-pharmacy claim, **no named partner**, no sibling pharmacy domain — routes to third-party compounding pharmacies.
- **Lane:** not stated — no 503A/503B language anywhere; only "licensed U.S. compounding pharmacies."

## Categories served

- **Categories:** TRT · GLP-1/weight (tirzepatide, phentermine) · sexual-health/ED · longevity/NAD · peptides (sermorelin · tesamorelin · IGF1-LR3) · labs

## Credibility & access

- **Health-merchant credibility:** **LegitScript-certified** (footer seal, cert #14914193, links to legitscript.com verification — y); **named clinicians NOT shown** (generic "licensed providers / clinicians who specialize exclusively in hormone optimization"; no /physicians roster or bios — n); pharmacy accreditation (PCAB/ACHC/NABP) not shown (n). Additional self-reported marks: "USA Made" seal, "Trusted Lab Network," 4.9★ / 1,943 Google reviews.
- **Controlled-substance Rx:** offers **Schedule-III (injectable testosterone / TRT)** — page-attested by the Testosterone ($99.99/mo) and TRT + HCG ($180/mo) SKUs on /testosterone-therapy/; FAQ notes "certain controlled medications may require an adult signature upon delivery."
- **Labs:** **required-step** — "labs are required before most treatments to ensure you receive the right protocol." Two draw models: **at-home/partner-lab** (TRT Nation orders digitally; blood draw at a local LabCorp / Quest; their panels $129/$179) **or bring-your-own** — "one of the few clinics that accepts outside lab work," using recent results (typically within ~120 days; required markers listed: Total Testosterone, CBC, CMP, Estradiol, PSA for men 40+). Ongoing monitoring required after 10 weeks, at 6 months, then yearly.
- **Payment & commitment:** **cash-pay only** — insurance-free positioning ("No confusing insurance red tape," "One simple monthly fee, no surprises"); no HSA/FSA claim shown. Commitment is per-product **minimum-purchase** terms (2.5-month minimum on testosterone/HCG/NAD+; 3-month on tirzepatide/tesamorelin), not a membership; a dedicated /cancellation-policy/ page exists; "no restrictive monthly subscriptions" (page-stated framing only — charged-after-cancel reality is out of scope).

## Notes

- **audience — men-first, not men-only.** The front door is unambiguously male: "America's Clinic" for "men's health and wellness," TRT flagship, "adult male (24+)" qualification, male hero imagery. But two lines aren't gender-restricted — the /lab-orders/ form offers a **Female** gender option and weight-loss qualification is BMI-based, and the blog markets "online tirzepatide clinics for women." Recorded `men-first` (men-origin, adjacent female eligibility on weight-loss/labs), read from the page structure, not the brand name.
- **compounding_posture — both.** The flagship products are compounded (testosterone cypionate, tirzepatide "compounding injection," and the peptide line — sermorelin/tesamorelin/IGF1-LR3/NAD+/glutathione), while the catalog also sells standard small-molecule generics at defined commercial doses (phentermine 37.5mg tablets, sildenafil, tadalafil, oral enclomiphene). No FDA brand-name drug (Ozempic®/Wegovy® etc.) is named; the site attributes all fulfillment to "licensed U.S. compounding pharmacies." Recorded `both` for the mix.
- **access_model — no membership.** Unlike a membership-wrapped peer, TRT Nation charges no platform/enrollment fee; each treatment is bought as its own monthly subscription priced independently, with the provider consult, ongoing support, and lab review bundled into the medication price ("no membership fees on top of products"). Hence `à-la-carte/both` rather than `all-in` or `membership-required`.
- **modality — sync.** The gating consult is synchronous: "Meet with a licensed provider via **video or phone**" (step 3 / FAQ). Intake is an async form, but treatment is gated on the live visit + provider lab review ("reviewed by your TRT Nation provider, not by a call center or automated system").
