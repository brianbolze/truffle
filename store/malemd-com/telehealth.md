---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"
domain: malemd.com
captured_at: 2026-06-04
value_chain_role: DTC brand
pharmacy_model: third-party              # partner pharmacy named "Curexa" (footer modal); "our partner pharmacies", no owned facility
audience: men-only                       # "MaleMD", "Men's Health, Simplified"; no women's line
compounding_posture: both                # compounded peptides/ED combos + FDA generics (sildenafil/tadalafil/finasteride/metformin/sertraline)
anchor_category: multi/none              # co-equal 5-category grid; hero A/B-rotates "Better Sex" <-> "Better Energy"
modality: async                          # online questionnaire -> physician reviews "in a few short hours"; no scheduled video in front-door flow
access_model: all-in                     # "medical visit, ongoing shipments, and provider messaging are all included in one low price"
pay_model: cash-pay only                 # "MaleMD doesn't require insurance"; transparent direct-pay
---

## Fulfillment

- **Pharmacy:** third-party. "Your medication ships directly from trusted US-based pharmacies" and "filled by licensed pharmacies" (homepage / /about-us); "ships discreetly and for free from our US-based, FDA-approved pharmacy" (homepage). No owned-pharmacy claim. **Named partner pharmacy:** "Pharmacy: **Curexa**" with `https://curexa.com/about/`, 3007 Ocean Heights Ave, Egg Harbor Township, NJ 08234 (footer "Partner Pharmacy" modal).
- **Lane:** both referenced — "503A pharmacies are licensed by state boards of pharmacy and 503B pharmacies are registered by the FDA. Both types of pharmacies are regulated by the FDA" (FAQ). Compounded products flagged on Rx pages: "featured products include compounded products which have not been approved by the FDA" (/knockout). Page does not assign a specific lane to Curexa.

## Categories served

- **Categories:** sexual-health (ED · PE) · longevity/NAD · peptides (sermorelin · BPC-157) · metabolic (metformin) · sleep · hair · pain

## Credibility & access

- **Health-merchant credibility:** LegitScript-certified (footer seal, cert #10453213, links to LegitScript verification); HIPAA-compliant + "FDA Regulated Pharmacies" badges. Named clinicians: **no** (claims "100% physicians… no nurse practitioners," "U.S.-licensed, board-certified," but no `/physicians` roster or named doctors). Pharmacy accreditation (PCAB/ACHC/NABP): not shown.
- **Controlled-substance Rx:** **non-scheduled only** — no TRT/testosterone or other scheduled SKU on the site; lineup is PDE5 inhibitors, sertraline, metformin, sleep generics (hydroxyzine/ramelteon/trazodone), finasteride/minoxidil, diclofenac, and peptides (sermorelin/NAD+/BPC-157).
- **Labs:** **none** — no bloodwork/lab step required or offered; intake is questionnaire-only.
- **Payment & commitment:** cash-pay only ("doesn't require insurance," "transparent pricing… no hidden fees"); recurring subscription / auto-refill (Sublytics rebill stack). Metformin "billed $55 first shipment, shipped quarterly"; other lines monthly. Explicit cancel terms not stated on captured pages.

<!-- anchor_category is A/B-volatile: the hero rotates between sexual-health ("Better Sex") and longevity/energy ("Better Energy") framings (Convert + Google Optimize). Recorded multi/none; see profile.md unverified_fields for the point-in-time snapshot caveat. -->
