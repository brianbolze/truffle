---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"
domain: hydramed.com
captured_at: 2026-06-04           # from the same 2026-06-04 profile.md capture
value_chain_role: DTC brand
pharmacy_model: third-party              # named partner compounding pharmacies — body Fulfillment carries the verbatim claim
audience: all-genders                    # "discreet online medical services for men and women" (/about-us); men's TRT + women's BHRT
compounding_posture: compounded-only     # every captured Rx SKU is 503A-compounded; FAQ mentions some ready-made/generic dispensing + about-us OTC/supplements (no FDA-brand SKU captured) — see note
anchor_category: multi/none              # leads with a broad mobile-IV menu + a broad Rx grid, not one vertical — see note (literal front door = mobile IV hydration, outside this set)
modality: hybrid                         # "Some states require a synchronous [phone/video] consultation… states that allow for an asynchronous consultation… secure online messaging" (/faq)
access_model: à-la-carte/both            # IV = pay-per-visit; Rx = per-product one-time OR monthly/annual subscription; no required membership
pay_model: HSA/FSA eligible              # homepage explains HSA/FSA + accepts those cards; no insurance billing stated
---

## Fulfillment
- **Pharmacy:** third-party — "our partnerships with FDA-registered pharmacies"; "Every prescription is fulfilled by our FDA-registered, licensed US pharmacy partner" (/faq, /compounded-medication-policy). No owned facility; partners are **named verbatim**: **Olympia Pharmaceuticals** (Orlando, FL), **Empower Pharmacy** (Houston, TX), **Casa Pharma RX** (Stafford, TX), **Valiant Pharmacy** (Ypsilanti, MI).
- **Lane:** "503A compounding pharmacies for HydraMed RX and 503B outsourcing facilities for HydraMed IV therapy products" (/faq) — patient-specific compounding for the Rx line, 503B outsourcing for the IV-drip inputs. Partner accreditations claimed: PCAB, cGMP, LegitScript, NABP; USP 800 handling; COA per batch.

## Categories served
- **Categories:** mobile-IV-hydration · GLP-1 (semaglutide/tirzepatide) · TRT · peptides (sermorelin/PT-141/GHK-Cu) · longevity/NAD · sexual-health (PT-141/tadalafil/trimix) · skin · lipotropic/weight · womens-HRT (BHRT) · labs

## Credibility & access
- **Health-merchant credibility:** partner-pharmacy accreditations claimed — LegitScript, NABP, PCAB, cGMP, 503A/503B (`/compounded-medication-policy`, `/faq`); named clinician — Chief Medical Director **Dr. Thomas Paluska, MD** (bio + LinkedIn, licensed in 13 states); self-reported Google 5.0 / JSON-LD AggregateRating 5 of 8,263 (rating lives in profile.md Credibility).
- **Controlled-substance Rx:** offers Schedule-III — **Testosterone Replacement Therapy** (testosterone cypionate, IM injection; /rx/testosterone), with providers stating they hold "controlled substance permits, and specific state DEA licenses." TRT gated to **Colorado residents only** at capture.
- **Labs:** optional overall, **required-step for TRT** — "Lab work is crucial; acquire it through us for a mere **$99**, or you're welcome to provide your own"; retest at 3 months then every 6 months (/rx/testosterone). Standalone lab testing offered at /labs. IV therapy and most Rx (e.g. semaglutide) proceed on intake without labs.
- **Payment & commitment:** **HSA/FSA eligible** (homepage payment section); cash-pay, no insurance billing stated; "NO travel fees" (IV) and "FREE shipping" (Rx). Rx is per-product one-time or monthly/annual subscription with "flexibility to pause or adjust your plan… hassle-free"; IV is per-visit.

## Notes
- **compounding_posture:** every captured Rx SKU is 503A-compounded (semaglutide, tirzepatide, testosterone cypionate, sermorelin, PT-141, NAD+, GHK-Cu, tadalafil — all page-attested), so `compounded-only`. Two softeners kept it from `both`: /faq says partner pharmacies "function as traditional retail pharmacies, offering both custom formulations and ready-made medications" and that some generics "may originate from the US or other FDA-approved countries," and /about-us references "over-the-counter treatments and nutritional supplements" — but no FDA-brand or OTC SKU was captured to roster, so the page-attested lane is compounded.
- **anchor_category:** the literal front door is **mobile IV hydration** ("Ranked #1 in Mobile IV since 2020"), a category outside this cohort's Rx-oriented anchor set; the Rx side leads with a co-equal grid (weight-loss, TRT, peptides, NAD+). Recorded `multi/none` as the honest generalist read rather than forcing one vertical.
- **modality:** state-dependent by design — synchronous phone/video where a state requires it (and always for TRT: a "30-minute video consultation"), asynchronous secure messaging where permitted; hence `hybrid`.
