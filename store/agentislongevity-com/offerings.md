---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.2"
domain: agentislongevity.com
captured_at: 2026-06-25
enumeration: indexed-complete    # the consumer offering set (LQ flagship + Boundless + membership) is fully rostered; partner-clinic service menus are out of scope (priced per-clinic, not Agentis SKUs) — a scope note, not a missing line
site_notes: "Consumer pricing is thin and single-homed: the ONLY published price ($149 LQ assessment, AGENTIS15 → $126.65) lives on /boundless-protocols-v2. /longevity-quotient and /services carry NO prices. The Boundless recurring tier and the LQ membership are unpriced ('billed monthly', 'Tiers and add-ons are separate'). Live DTC checkout sits on the lq.agentislongevity.com subdomain (promo ?promo=AGENTIS15). Partner-clinic services (TRT etc.) are priced on each clinic's own site, not here."
---

## Portfolio overview

Agentis sells a **flagship-led** consumer program, not a catalog. One product gates everything: the **Longevity Quotient (LQ) assessment** — the only published-price item ($149) and the entry baseline the company frames as the start of all care ("The test starts your plan") `[HIGH — company's own framing + sole pricing CTA]`. From there two **companions** open up, both unpriced on-site: the **Boundless Protocols** 12-week peptide-and-supplement program (a recurring monthly tier) and a broader **LQ Membership** (quarterly retesting + wearables + concierge). Below that sits delivered clinical care (TRT-led) at the 14 partner clinics — priced per-clinic, **out of scope for this roster** (not Agentis-priced SKUs).

The shape finding: despite an 11-pillar "services" page and a large clinic network, the **directly-buyable Agentis surface is just three lines**, and only one carries a number. Pricing depth is genuinely shallow, not just un-captured.

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Longevity Quotient (LQ) assessment | buyable | — | /boundless-protocols-v2 | **$149** → **$126.65** (code AGENTIS15, "15% off automatically applied") | published | diagnostic · 60+-biomarker blood panel + COSEHC-17, Cognivue, InBody, grip-strength · one-time, no membership required, HSA/FSA eligible |
| Boundless Protocols (12-week program) | buyable | — | /boundless-protocols-v2 | "recurring tier billed monthly" — amount not shown | on-request | peptide + supplement protocol · 12 weeks, physician-supervised, dispensed by a licensed compounding pharmacy · Path A in-clinic (Arete, Nashville) or Path B at-home telemedicine (Ultrahuman app) |
| LQ Membership | buyable | — | /longevity-quotient | not shown | on-request | longevity membership · unlimited LQ scoring + quarterly retest + 60+-biomarker panels each cycle + Ultrahuman Ring/CGM integration + concierge provider access · recurring |

## Verbatim anchors

- **LQ price:** "$149  $126.65  Longevity Quotient (LQ) assessment" · "Code AGENTIS15 — 15% off automatically applied at checkout" (/boundless-protocols-v2). The $149 is the **assessment only**; "HSA/FSA eligible · No commitment to start · Quarterly retest available."
- **Pricing structure:** "You start with a one-time Longevity Quotient (LQ) assessment ($149, AGENTIS15 applied). After your results, you can enroll in a recurring tier billed monthly, only if your plan calls for it… Tiers and add-ons are separate. Cancel anytime." (/boundless-protocols-v2 FAQ).
- **Two draw paths, same price:** Path B at-home scores **six** blood-based domains; in-clinic at Arete adds Cognivue, InBody, and grip strength for the **full eight-domain** LQ (/boundless-protocols-v2 FAQ).
- **Molecule sourcing:** the peptides/meds named on /boundless-protocols-v2 (TRT, Tadalafil, Semaglutide, Tirzepatide, BPC-157, MOTS-c, AOD-9604, Semax, Epitalon, Dihexa, TB-500, GHK-Cu, NAD+, TA-1, LL-37, KPV, SS-31, Selank, Oxytocin) are labeled **"Example protocols, personalized to your panel by your clinical team. Not a prescription."** — illustrative routing, **not** an enumerable priced SKU set, so they are not rostered as offerings.

## Deep blocks

**The three price layers (disambiguation — earned).** The single visible number hides a three-tier structure a roster row flattens:
1. **$149 LQ assessment** — one-time, no membership, the only published price. Buys the panel + score + a results review + a personalized protocol *plan*.
2. **Boundless Protocols** — a **separate recurring monthly tier** you enroll in *after* results "only if your plan calls for it." This is where the 12-week peptide/supplement shipments + Ben Greenfield modules live; **no price shown**.
3. **LQ Membership** (framed on /longevity-quotient) — the ongoing "unlimited LQ scoring + quarterly retest + wearables + concierge" relationship; **no price shown**.

So the headline "$149" is the *cheapest possible* entry, not the cost of the program a converting patient actually runs — the recurring economics are entirely gated behind the post-results consult.

## Provenance

- **Pages:** /boundless-protocols-v2 (the only priced page), /longevity-quotient, /services — captured 2026-06-25 (cited in `captures/2026-06-25/`).
- **Scope:** enumerated the three directly-buyable Agentis consumer offerings. **Not enumerated** (by design): the 11 clinical "service pillars" and the 14 partner clinics' service menus (TRT, peptides, IV, HBOT, etc.) — these are delivered/priced at the clinic level, not Agentis-priced SKUs; the illustrative peptide/med list (see Verbatim anchors).
- **Point-in-time:** the $149 is shown with promo AGENTIS15 pre-applied (→ $126.65) — promo-dependent, re-check next run.
- **Run profile:** guided — `offerings.md` added per the run's explicit module ask; thin roster is real (one published price), above the OFFERINGS hard floor.
