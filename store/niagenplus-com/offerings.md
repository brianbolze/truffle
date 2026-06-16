---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: niagenplus.com
captured_at: 2026-06-15
site_notes: "Shopify storefront (prod-niagen-plus-mdi.myshopify.com). /products.json lists ONLY the 2 at-home SKUs ($299 each, both available=True as of 2026-06-15 — the Jun-03 capture had 'More stock coming soon'; stock is a point-in-time snapshot) — the in-clinic Niagen IV + Niagen Shots are NOT in the product registry (clinician-administered, no e-commerce price; access via clinic locator), so enumerate them from the /collections/niagen-iv page, not the registry. At-home prices include a $20 consult fee (in the $299, not on top) and are Rx-gated (intake → physician review). Kit contents (PDP how-to): one (500 mg) vial + a 2-piece reconstitution syringe set + 10× 1 mL injection syringes + swabs + QR-code instructions → a ~10-dose, 'daily injection routine' regimen, dose/frequency provider-set."
---

## Portfolio overview

**One molecule, three formats, two channels.** Every Niagen Plus offering is the same active — **Niagen® (nicotinamide riboside chloride, NRCl)**, an NAD⁺ precursor — delivered as (1) an at-home subcutaneous injection kit (DTC telehealth) and (2) clinician-administered IV and intramuscular therapy (in-clinic). Prominence:

- **Niagen At-Home Injection Kit `[HIGH]`** — the company's own hero: the only buyable-online SKU, the homepage "Get Started" hero CTA, and the first nav pillar.
- **Niagen In-Clinic (Niagen IV + Niagen Shots) `[MED]`** — co-equal second nav pillar and homepage section, but routes to a clinic locator, not a cart (no online price).
- **At-Home Refill `[LOW]`** — a companion reorder SKU, surfaced mainly from the product registry.

A `Flagship + companions` shape: deepen the kit, note the rest.

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Niagen At-Home Injection Kit | buyable | — | /products/niagen-at-home-injection-kit | $299 † | published | Niagen® (NRCl) · Rx subcutaneous injection kit · telehealth-gated (intake → physician Rx; ships 503A) |
| Niagen At-Home Injection Kit Refill | buyable | — | /products/niagen-at-home-injection-kit-refill | $299 † | published | Niagen® (NRCl) · subcutaneous injection refill · telehealth-gated |
| Niagen In-Clinic | family | — | /collections/niagen-iv | — | — | clinician-administered NAD⁺ therapy at 1,200+ partner clinics |
| Niagen IV | buyable | Niagen In-Clinic | /collections/niagen-iv | — | on-request | Niagen® (NRCl) · IV infusion · clinic-administered (no online price; clinic-set) |
| Niagen Shots | buyable | Niagen In-Clinic | /collections/niagen-iv | — | on-request | Niagen® (NRCl) · intramuscular injection (<15 min) · clinic-administered at select clinics |

*Niagen IV and Niagen Shots have **no standalone PDP** — both are described on the `/collections/niagen-iv` landing page (their within-company location); neither is purchasable online.*

### Verbatim anchors

- **† At-home price (kit + refill PDPs):** *"Regular price $299"* and *"Price includes a doctor consultation fee of $20."* The $20 consult is **inside** the $299, so the shown number is the full, self-contained price → **`published`** (not `partial`). State limit: *"Currently not available to ship to Alabama, California, Iowa, Massachusetts, Texas, Washington, and West Virginia."*
- **Molecule (page-attested, every format):** *"Patented Niagen® (NRCl)—an NAD+ precursor and form of vitamin B3"* (kit/refill PDP); *"Niagen Plus is a pharmaceutical-grade form of Niagen® (nicotinamide riboside chloride)"* and *"Niagen IV … delivers pharmaceutical-grade Niagen® (nicotinamide riboside chloride)"* (FAQs). NRCl is thus attested for the at-home and IV formats; Niagen Shots is attested as *"pharmaceutical-grade Niagen® via intramuscular injection,"* with Niagen® defined as NRCl on the same captures — **not** inferred from the brand name.
- **In-clinic = on-request:** no price appears on `/collections/niagen-iv`; *"administered by licensed healthcare professionals at select premium clinics nationwide,"* accessed via *"Find a Clinic."* Niagen IV vs NAD⁺ IV is a clinical claim, not a price.

## Deep blocks

**None earned.** The roster + verbatim anchors carry this company: the at-home `published` $299 (consult-inclusive) and the in-clinic `on-request` are both unambiguous, and the molecule is cleanly attested per format. No per-SKU ambiguity needs a block. A **PDP-template anatomy** block and **hero-image** capture are opt-in and were **not requested** by this run (the emphasis was science/ingredients, which lands in `profile.md`'s Credibility section, not the roster) — so both are skipped.

## Provenance

- **Pages read:** at-home kit (PDP), at-home refill (PDP), at-home how-to, in-clinic Niagen IV collection, homepage, FAQs — cited `captures/2026-06-15/` (refresh of the 2026-06-03 capture, archived under `captures/_archive/`).
- **Scope:** 5 offerings enumerated (2 buyable at-home SKUs + a Niagen In-Clinic family spanning 2 administered formats). The buyable set was cross-checked against the Shopify `/products.json` registry (2 SKUs, both $299) — **agreement**; the in-clinic line is non-commerce (absent from the registry) and was enumerated from the collection page.
- **Gated / unreachable:** in-clinic Niagen IV / Shots pricing is clinic-set (on-request, no online figure); at-home SKUs are Rx-gated (intake → physician review, approval not guaranteed).
- **Point-in-time:** at-home stock flagged *"More stock coming soon"*; all prices are a snapshot, not fixed.

### Run profile
Guided — emphasis "science & ingredients"; **+offerings** enabled this module. **Exploratory:** niagenplus is not a telehealth-cohort member and has no live downstream consumer yet, so this `offerings.md` is a test of the module on a supplement/clinical-NAD⁺ brand, not a cohort deliverable. No PDP-anatomy or hero-image block (not requested).
