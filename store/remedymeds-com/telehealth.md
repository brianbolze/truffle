---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"
domain: remedymeds.com
captured_at: 2026-06-01           # rides the same 2026-06-01 profile.md capture
value_chain_role: DTC brand
pharmacy_model: third-party              # "direct from licensed U.S. compounding pharmacies" — supplier language, no ownership claim, no named/sibling pharmacy
audience: women-first                     # hero imagery + pain-copy lead female (postpartum/perimenopause); male images + a male testimonial present — read from pages, not the name (see note)
compounding_posture: both                # compounded sema/tirz ("FDA has not evaluated") + a "name brand" Ozempic®/Zepbound® card
anchor_category: GLP-1                    # whole front door is GLP-1 weight loss — "Personalized GLP-1 treatment"
modality: async                          # gating intake = quiz → clinician builds plan within 24h (no video gates the Rx); video/chat is post-purchase care
access_model: all-in                     # "Your plan includes Everything. All-in." — one monthly fee bundles med + care + labs + shipping (see note on the "No Memberships" tension)
pay_model: HSA/FSA eligible              # "HSA/FSA accepted" (hero) — page-attested positive signal; insurance posture not captured (see note)
---

## Fulfillment

- **Pharmacy (claim, verbatim):** "Remedy Meds offers compounded GLP-1s exclusively from U.S. pharmacies. Compounded medications are regulated and compounding pharmacies are licensed and inspected by Boards of Pharmacy" (homepage / both med pages). Fulfillment step reads "Direct from licensed U.S. compounding pharmacies" (homepage Step 3). No owned-pharmacy claim, no named partner, no sibling pharmacy domain on the captured pages.
- **Lane:** not stated — "compounding pharmacies" only; neither 503A nor 503B is named.
- **Footer badge:** "Compounded By U.S.A. Licensed Pharmacies."

## Categories served

- **Categories:** GLP-1 (weight loss) — single vertical. Sold as four GLP-1 plan variants (compounded Semaglutide · compounded Tirzepatide · Microdose · branded Ozempic®/Zepbound®); no TRT, sexual-health, or non-weight-loss line on any captured page.

## Credibility & access

- **Health-merchant credibility:** LegitScript-certified (footer seal #145059 → legitscript.com, y); named clinicians in the patient manual — Mohit Joshipura (CMO), Jordan Cobb (Clinical Education Director), Rebecca Aaron (Clinical Quality Director) — but no public `/physicians` roster page (n); pharmacy accreditation (PCAB/ACHC/NABP) not shown (n).
- **Controlled-substance Rx:** non-scheduled only — the only page-attested products are GLP-1s (semaglutide, tirzepatide; branded Ozempic®/Zepbound®). No TRT/testosterone or other scheduled SKU appears.
- **Labs:** required-step — "Free lab work" included; the manual orders TSH, A1C, CMP, and a lipid panel through partner labs (Quest Diagnostics or LabCorp; Bioreference for NY/NJ). Partner-lab draw; prior results within 24 months accepted.
- **Payment & commitment:** "HSA/FSA accepted" / "FSA & HSA eligible" (hero + marquee) — the page-attested payer signal. A "Do you require insurance?" FAQ exists on the homepage and both med pages, but its answer is a collapsed accordion not captured in this scrape, so the insurance posture is not page-attested either way (not recorded as direct-pay). Month-to-month, "charged automatically every 28 days," "No Long-Term Contract," cancel anytime — but the manual states "once a prescription has been written, we are unable to issue a refund."

## Notes

- **audience:** the brand name is gender-neutral, so this is read off the pages, not inferred. The front door leads **female** — hero marquee imagery (two-women, woman-inject, women, dr-emily) and the pain narrative (postpartum weight, perimenopause, pregnancy, "food noise") skew strongly female; profile.md's own read is "heavily female-coded." But the site is not women-*only*: male hero images (man.png, doctors), a male before/after testimonial (Chris -42 lbs), and gender-neutral copy ("U.S. adults") all appear. Recorded `women-first`, not `women-only`.
- **anchor_category:** point-in-time snapshot, not fixed — Remedy runs a single A/B-tested funnel (the homepage is a `lander/variant_3` build; "New!" / "64% of members" are live marketing claims). The front door is unambiguously GLP-1 today; re-check on recapture.
- **access_model / "No Memberships" tension:** the homepage marquee says "No Memberships or Hidden Fees," yet the patient manual calls the recurring charge a "membership" billed "automatically every 28 days." The all-in fee *is* the unit (med + unlimited care + free labs + shipping bundled); "no hidden fees" means nothing is added on top, not that there's no recurring charge. Recorded `all-in` for the one-bundled-fee architecture.
- **modality:** the gating consult is asynchronous — quiz → a clinician "builds your plan" within 24h, with no video visit required to be prescribed. Sync care (same-day video calls, unlimited video/messaging, monthly clinician check-ins) is ongoing post-purchase support, not the intake gate; hence `async`, not `hybrid`.
- **pay_model:** per the contract's asymmetric-fill rule, the positive payer-rail signal is recorded — `HSA/FSA eligible` (hero "HSA/FSA accepted," marquee "FSA & HSA eligible"). The site does **not** state it bills insurance, but it also does not state it's direct-pay: the "Do you require insurance?" FAQ answer is a JS-collapsed accordion absent from the capture. So this is **not** `cash-pay only` — that value needs a page-stated direct-pay claim, which isn't captured; the HSA/FSA signal is the only attested fact.
