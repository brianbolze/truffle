---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"
domain: getopt.com
captured_at: 2026-06-04                   # derives from the same 2026-06-04 profile.md capture
value_chain_role: DTC brand
pharmacy_model: integrated                # "we ship… from our pharmacy" claim (FAQ) — no named entity/lane; see Fulfillment
audience: men-first                       # men is the default vertical; a parallel /women track exists — see note
compounding_posture: both                 # compounded peptide menu ("specialized compounds") alongside conventional Rx (testosterone, PDE5 ED meds, semaglutide, thyroid)
anchor_category: TRT                       # "Popular" + protocols lead with TRT; wrapped in a longevity/optimization frame — see note
modality: sync                            # "consultations are conducted via video through our HIPAA-compliant telemedicine platform"
access_model: membership-required         # "our memberships ensure continuity of care" — no treatment without a membership
pay_model: HSA/FSA eligible               # "We do accept HSA/FSA"; no direct insurance billing (may reimburse out-of-network)
---

## Fulfillment
- **Pharmacy:** ownership **claimed** — *"We ship all supplements and prescriptions from **our pharmacy** directly and discreetly to your home."* (FAQ, /memberships + /medical-team). Recorded as the page-attested claim, not verified; **no named pharmacy entity** and **no 503A/503B lane** appear on the captured pages. Coarse `integrated` posture (merges owns + captive-affiliate — unresolvable from a page).

## Categories served
- **Categories:** TRT/hormone-optimization · peptides (Sermorelin · PT-141 · Semaglutide/GLP-1 · GHK-Cu · Oxytocin · VIP · Pinealon · Hexarelin · 5-amino-1MQ) · sexual-health/ED · weight-loss/GLP-1 · longevity/biological-age · thyroid · hair-loss · supplements/micronutrients · womens-HRT/menopause (parallel /women vertical)

## Credibility & access
- **Health-merchant credibility:** named clinicians — a full `/medical-team` page with 7+ credentialed physicians and bios (John Tidwell MD CMO, Jeremie Walker MD, Anna Fleytman-Pope DO, Danny Molinar MD, Alejandro Arenas MD, Samuel Sarmiento MD, Vinay Bhamidipati MD; Graham Simpson MD leads the women's track); physicians **ABHRT-certified** ("advanced training accredited by the prestigious ABHRT Certification program"); HIPAA-compliant telemedicine platform. **No LegitScript seal** or pharmacy accreditation (PCAB/NABP) observed on the captured pages.
- **Controlled-substance Rx:** offers Schedule-III (testosterone / TRT — injection, oral, or topical) — /learn/protocols/testosterone-replacement-therapy.
- **Labs:** required-step — every membership begins with a comprehensive blood panel (**55+ biomarkers**; **65+** + epigenetic/biological-age testing on the Longevity tier). Draw model: at-home nurse visit in **San Francisco, Los Angeles, San Diego, New York City** and surrounding areas, otherwise one of **2,000+ partner lab locations**.
- **Payment & commitment:** **HSA/FSA accepted**; "we do not work directly with any insurance companies" (out-of-network reimbursement possible). Membership-required, billed monthly — **Foundation $95/mo**, **Optimization $245/mo**, **Longevity $645/mo**, each after a one-time intake + lab fee (**$195 / $195 / $695**). Cancellation / lock-up terms not stated on the captured pages.

## Notes
- **audience:** men is the **default** vertical (getopt.com root; the homepage hero, testimonials, and the TRT/ED/peptide protocols all skew male), with a fully-built **parallel women's track** at `/women/*` (peri/menopause HRT, longevity, peptides). So `men-first`, not `all-genders` — the women's vertical is a sibling sub-site, not a co-equal toggle on the primary site. (Center-of-gravity / who-it-targets is otherwise a consumer-side judgment.)
- **anchor_category:** a point-in-time positioning read. The brand's **front door is a concierge longevity/optimization membership** (hero "Opt into a Better You," the Opt Performance Score, "Be 55. Feel 35."), but the most-foregrounded *specific* vertical is **TRT** — it's the #1 "Popular" footer link and the first Protocols entry, and men's hormone optimization is the brand's core. Recorded as `TRT`; the longevity/biological-age framing is the wrapper.
- **compounding_posture:** no explicit per-SKU "compounded" FDA disclaimer was captured, but the **peptide menu** (GHK-Cu, Epithalon, Pinealon, 5-amino-1MQ, VIP, Hexarelin, Sermorelin, etc.) is inherently compounded/specialty, and /memberships markets "specialized compounds designed for precise benefits" — set against conventional Rx (testosterone, PDE5 ED meds, semaglutide, thyroid), giving a `both` roll-up.
