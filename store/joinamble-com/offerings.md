---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: joinamble.com
captured_at: 2026-06-18
site_notes: "Two distinct lines on two purchase models. (1) Therapeutic subscription PDPs (7 live SKUs) — nav-driven, one Webflow PDP each, plan-length table (12-mo cheapest → 1-mo dearest) + 'same price, every dose'; prices PDP-only; UNCHANGED 6/04→6/18. (2) NEW /medkits/ line (8 SKUs) — one-time upfront purchase ('Total price represents a one time purchase paid upfront'), curated sets of named generic Rx (+ OTC/supplies), built on a SEPARATE Webflow CDN project (691513c1de5d326f0f8e5ba1). /tesamorelin-injection in nav but PDP 404s (re-confirmed 6/18) — depublished. A/B site (rotating hero, run-to-run stat flicker) — pricing is a point-in-time snapshot."
---

## Portfolio overview

Amble now runs **15 live prescription SKUs across two lines on two purchase models** — a clean **Multi-product** shape, every SKU enumerable at one PDP each.

- **Subscription therapeutics (7 live)** — `[HIGH]` the original business. Compounded injectables + skincare on the plan-length subscription template (longer commit → lower per-month price), each PDP claiming "same price, every dose." Weight loss (GLP-1) is the flagship: rotating hero leads with it, referral counts only Weight Loss, Amble Cares is weight-loss-only. Anti-aging is a six-injectable menu (5 live + a **dead Tesamorelin page**). Skin is the cheapest entry ("Starting at $55").
- **Medkits (8 live, NEW since 6/04)** — `[HIGH-watch]` one-time prescription emergency/preparedness kits, $285–$945 paid upfront. The Jase Medical / Duration Health "stockpile antibiotics, just in case" category. Different buyer, different purchase model, different CDN section — but the same physician-review + pharmacy-network rails.

**Shape findings:** the therapeutic catalog is **100% compounded** — even the GLP-1 line is compounded semaglutide/tirzepatide, not branded Wegovy/Zepbound. The medkits are **named FDA-approved generics** (amoxicillin-clavulanate, doxycycline, ivermectin, valacyclovir, potassium iodide, etc.) filled through the partner pharmacy network — so the company is now `both` compounded + FDA-brand, not compounded-only. Therapeutic prices held **identical** to the 6/04 capture.

## Roster

Two purchase models in one table: Line-1 therapeutics are **per-month subscription** (price shows the 12-mo → 1-mo ladder); Line-2 medkits are **one-time upfront** (single price). Counts/contents for medkits are PDP-stated; full medication lists transcribed for Just in Case + Panic Pack, sampled for the rest.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule/contents · form · access) |
|---|---|---|---|---|---|---|
| Weight loss | family | — | /glp-1-injections | — | — | The flagship line; one buyable (GLP-1) |
| GLP-1 injection | buyable | Weight loss | /glp-1-injections | 12-mo **$135** · 6-mo **$145** · 3-mo **$160** · 1-mo **$179** /mo (homepage "From $179") | published | compounded **semaglutide & tirzepatide** · subcutaneous, once weekly · async intake → physician review (live consult where state law requires) |
| Anti aging | family | — | /glp-1-injections (dropdown; no own page) | — | — | Six-injectable menu; 5 live + 1 dead |
| NAD+ injection | buyable | Anti aging | /nad-injections | 12-mo **$125** · 6-mo **$167** · 3-mo **$183** · 1-mo **$199** /mo | published | compounded **NAD+** · subcutaneous, max 0.5 mL/injection |
| Sermorelin injection | buyable | Anti aging | /sermorelin-injections | 6-mo **$135** · 3-mo **$149** · 1-mo **$159** /mo (no 12-mo tier) | published | compounded **sermorelin** (synthetic GHRH peptide) · subcutaneous, once daily (evening) |
| Glutathione injection | buyable | Anti aging | /glutathione | 12-mo **$75** · 6-mo **$83** · 3-mo **$92** · 1-mo **$100** /mo | published | compounded **glutathione** (antioxidant tripeptide) · subQ or IM, 200–800 mg, 1–3×/week |
| Lipo-B (MIC+B12) injection | buyable | Anti aging | /lipo-b | 12-mo **$120** · 6-mo **$125** · 3-mo **$133** · 1-mo **$149** /mo | published | compounded **MIC + B12** (may include L-carnitine, inositol, methionine, choline, B6) · subQ or IM, once weekly |
| Lipo-C injection | buyable | Anti aging | /lipo-c | 12-mo **$120** · 6-mo **$125** · 3-mo **$133** · 1-mo **$149** /mo | published | compounded **MIC + B-complex + vitamin C** · subcutaneous |
| Tesamorelin injection | buyable | Anti aging | /tesamorelin-injection | — | on-request | **not stated** — PDP 404s (re-confirmed 6/18); nav label only; not a live SKU |
| Skin (prescription skincare) | buyable | — | /skin | **Starting at $55** /month | published | compounded topical actives — tretinoin, clindamycin, azelaic acid, niacinamide, GHK-Cu, hydroquinone, tranexamic acid, etc. (personalized per concern) · topical |
| Medkits | family | — | /medkits | — | — | NEW one-time Rx emergency/prep kit line; 8 buyables |
| Just in Case Kit | buyable | Medkits | /medkits/just-in-case-kit | **$285** one-time | published | "first line of defense" · **9 Rx** (antibiotics, antivirals, anti-parasitics, antifungals, anti-nausea): amox-clav 875/125 (28), azithromycin 250 (12), doxycycline 100 (60), metronidazole 500 (30), TMP-SMX 800/160 (28), ivermectin… |
| Mayday (Travel Emergency Kit) | buyable | Medkits | /medkits/mayday-kit | **$325** one-time | published | travel · **10 meds** for travel infections, nausea, traveler's stomach, altitude sickness, persistent cough |
| Breathe Easy (Mold & Allergy Kit) | buyable | Medkits | /medkits/breathe-easy-kit | **$325** one-time | published | mold/allergy/respiratory · Rx for inflammation, asthma, nasal/airway irritation, allergy, infections |
| Cold Reaper (Cold & Immunity Kit) | buyable | Medkits | /medkits/cold-reaper-kit | **$325** one-time | published | cold & flu season · **8 Rx** for respiratory infections, inflammation, nausea, fever; "broad-spectrum bacterial support" |
| Viral Ick Kit | buyable | Medkits | /medkits/viral-ick-kit | **$325** one-time | published | antiviral · **7 Rx** (antivirals, anti-inflammatories, immune meds) + a **nebulizer**; ivermectin seen |
| Oh Sht (Radiation Emergency Kit) | buyable | Medkits | /medkits/oh-sht-kit | **$345** one-time | published | radiological exposure · emergency-prep meds incl. **potassium iodide** (PDP carries shared compounded GLP-1 ISI template) |
| Ouch Pouch (first-aid kit) | buyable | Medkits | /medkits/ouch-pouch-kit | **$425** one-time | published | first aid · **Rx + OTC**: topical antibiotics, creams, painkillers, antihistamines, motion-sickness patch, **epinephrine auto-injector**, Rx antibiotics |
| Panic Pack (Field Emergency Kit) | buyable | Medkits | /medkits/panic-pack-kit | **$945** one-time | published | comprehensive/field · broadest tier: amox-clav, azithromycin, cephalexin 500 (20), doxycycline 100 (60), metronidazole 500 (30), mupirocin 2%, **hydroxychloroquine 200 (20)**, **ivermectin 18 mg (30)**, valacyclovir 500 (42), epinephrine, respiratory, GI rescue, radiation prep, wound/trauma supplies |

## Verbatim anchors

- **Plan-table model (Line 1):** "Per Month" column over rows "12 Month / 6 Month / 3 Month / 1 Month" per PDP. The 1-month rate is the homepage "From $X."
- **"Same price, every dose"** (Line 1 PDP badge) — terms: *"Any 'same price at every dose' promotion expires within 24 hours of any price updates… Introductory or promotional pricing, including 'first month' offers, are not governed by the 'same price per dose' policy."*
- **One-time purchase (Line 2):** *"Total price represents a one time purchase paid upfront."* (every medkit PDP) — single price, no plan-length table.
- **HSA/FSA (payment, not a price):** *"HSA and FSA cards are accepted for 3-month or longer plans."* (Line 1 PDPs). Amble Cares pricing explicitly cannot be combined with FSA/HSA or insurance.
- **Managed-services disclaimer (both lines):** *"Amble acts as a managed services provider and does not offer medical advice, fill prescriptions, or function as a licensed healthcare facility or pharmacy… Prescriptions issued through Amble may be filled by licensed pharmacies within its affiliated network."*

## Deep blocks

- **Medkits — the strategic expansion.** Eight SKUs on the `/medkits/` path, built on a **separate Webflow CDN project** (691513c1…) from the core site (67fec0a6…) — a distinct section, consistent with a recently-launched line. One-time AOVs of $285–$945 sit far above a monthly injectable and need no subscription retention. The category (mass-dispensed antibiotics + ivermectin/HCQ + potassium iodide "just in case") is a different regulatory surface than the rest of the catalog and the one to watch. Same physician-review + pharmacy-network rails as Line 1.
- **Tesamorelin — the live-in-nav, dead-on-page SKU.** `/tesamorelin-injection` is linked from the top nav strip and the Anti-aging dropdown ("Naturally boost growth hormone") but returns **HTTP 404** (re-confirmed via curl 6/18). The anti-aging menu *advertises* six injectables but *sells* five.
- **PDP-anatomy (Line 1):** every live therapeutic PDP is the same shell (hero vial render → plan-table → "same price every dose" → "What you get" → "How to take" → side effects → ISI → How-it-works → reviews → referral). Reading one (e.g. [glutathione](captures/2026-06-18/glutathione.md)) teaches the line.

## Provenance

- **Pages read:** all 6 live injectable PDPs + /skin + all 8 /medkits/ PDPs (`captures/2026-06-18/`), cross-checked against the homepage; Tesamorelin re-confirmed 404 via curl (not scraped).
- **Scope:** all 15 live SKUs enumerated and priced; Tesamorelin rostered as a dead-PDP finding. Line-1 prices verified UNCHANGED vs 6/04. Medkit medication rosters: full lists transcribed for Just in Case + Panic Pack; the other 6 captured by count + category + named samples (full per-kit transcription deferred — **lines-omitted**, not exhaustive). Completeness cross-check: homepage medkit grid lists 8 kits; all 8 PDPs scraped and live.
- **Point-in-time caveat:** A/B-tested site (rotating hero, run-to-run stat flicker) — snapshot, not fixed truth. "Same price, every dose" promos expire within 24h of any price update.
- **Run profile:** express fresh re-capture (Deep gate — direct competitor, High importance). No flagship hero-render images captured this run (the 6/04 archive holds the injectable vial renders).
