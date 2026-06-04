---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: ford.com
captured_at: 2026-06-04
site_notes: "Roster backbone = /showroom (every model + starting MSRP, on one page). Per-trim prices are gated behind Build & Price — only base + halo-trim MSRPs show on the model PDPs. Prices are time-stamped ('Pricing for June 4, 2026') under a rotating 'Employee Pricing for All' promo — re-check next run. Model slugs attested from captures (/showroom, model PDPs, map); commercial chassis appear only on /showroom (no marketing landing). Clean isolated 'jellybean'/configurator renders live on acslibs/build.ford.com which hard-block fetches (http=000); flagship heroes were pulled from the fetchable www.assets.ford.com DAM (marketing beauty shots, not isolated-on-white)."
---

## Portfolio overview

Ford's US consumer lineup, as indexed on `/showroom` — **~22 model lines** across six groupings (SUVs & Crossovers, Trucks & Vans, Cars, Electric & Hybrid, Commercial, Performance). The catalog is **fully priced on one page**: every model shows a starting MSRP, so the roster is `[published]` at the model grain; trim-level prices are gated behind Build & Price (only base + halo trims surface on the PDPs). This is a `Multi-product` shape — enumerable lines, deepened below for the five flagships.

**Prominence read** (what the site foregrounds — observation, not a market verdict):
- **`[HIGH]`** — **F-150, Explorer, Bronco** are the homepage "Featured Offers" cards (the company's own hero placement + active $1,000-cash / Employee-Pricing offers).
- **`[MED]`** — the **"Find Your Ford"** tiles split the lineup three ways: *Trucks & Vans · Electric & Hybrid · SUVs & Cars* — equal billing, with electrification pulled out as its own pillar. Mustang anchors "Cars" as the sole remaining car line.
- **`[LOW]`** — Commercial (Ford Pro) is barely surfaced on the consumer site (walled to fordpro.com); the GT is a no-price halo.

Cars are now a one-model line (Mustang). "Electrified" SKUs (Mach-E, F-150 Lightning, Escape Hybrid/PHEV, E-Transit) are **cross-listed** — they appear in both their body-style group and the Electric & Hybrid group.

## Roster

Every `$` is verbatim from `/showroom` unless a footnote cites a PDP. Visibility is `published` for all priced rows; `on-request` only where no price shows. `What` leads with `body group · powertrain (page-attested only) · access`.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (group · powertrain · access) |
|---|---|---|---|---|---|---|
| Maverick | buyable | Trucks & Vans | /trucks/maverick | MSRP starting at $28,145 | published | compact pickup · powertrain not stated on captured pages · Build & Price → dealer |
| Ranger | buyable | Trucks & Vans | /trucks/ranger | MSRP starting at $33,550 | published | midsize pickup · not stated · Build & Price → dealer |
| F-150 | buyable | Trucks & Vans | /trucks/f150 | MSRP starting at $39,330 | published | full-size pickup · gas (2.7L/multiple engines, page-attested) · 8 trims, see deep block |
| Super Duty | buyable | Trucks & Vans | /trucks/super-duty | MSRP starting at $45,975 | published | heavy-duty pickup · not stated · Build & Price → dealer |
| F-150 Lightning | buyable | Trucks & Vans · Electric | /trucks/f150-lightning | MSRP starting at $54,780 | published | electric pickup · BEV (Electrified section) · 2025 MY |
| Transit | buyable | Trucks & Vans | /new-commercial-trucks | MSRP starting at $59,180 | published | full-size van · not stated · also a commercial line |
| Escape | buyable | SUVs & Crossovers | /suvs-crossovers/escape | MSRP starting at $30,350 | published | SUV/crossover · gas (Hybrid & PHEV are separate SKUs) · Build & Price → dealer |
| Bronco Sport | buyable | SUVs & Crossovers | /suvs/bronco-sport | MSRP starting at $31,845 | published | off-road crossover · not stated · Build & Price → dealer |
| Mustang Mach-E | buyable | SUVs · Electric | /suvs/mach-e | MSRP starting at $37,795 | published | electric SUV · BEV (RWD/eAWD/GT, page-attested) · see deep block |
| Explorer | buyable | SUVs & Crossovers | /suvs/explorer | MSRP starting at $38,465 | published | 3-row SUV · gas (2.3L I-4 / 3.0L V6, page-attested) · 6 trims, see deep block |
| Bronco | buyable | SUVs & Crossovers | /suvs/bronco | MSRP starting at $39,995 | published | off-road SUV · gas (3.0L EcoBoost V6, page-attested) · 2025 MY ($40,795 for 2026); see deep block |
| Expedition | buyable | SUVs & Crossovers | /suvs/expedition | MSRP starting at $62,700 | published | full-size SUV · not stated · Build & Price → dealer |
| Mustang | buyable | Cars | /cars/mustang | MSRP starting at $32,640 | published | sports car · gas (EcoBoost turbo / GT V8, page-attested) · see deep block |
| Escape Hybrid | buyable | Electric & Hybrid | shop.ford.com/escape-hybrid | MSRP starting at $33,890 | published | SUV · hybrid (name-attested) · Build & Price → dealer |
| Escape Plug-In Hybrid | buyable | Electric & Hybrid | shop.ford.com/escape-plug-in-hybrid | MSRP starting at $35,400 | published | SUV · plug-in hybrid (name-attested) · Build & Price → dealer |
| E-Series Stripped Chassis | buyable | Commercial | /new-commercial-trucks | MSRP starting at $38,135 | published | commercial chassis · not stated · 2027 MY; /showroom only |
| E-Series Cutaway | buyable | Commercial | /new-commercial-trucks | MSRP starting at $41,330 | published | commercial cutaway · not stated · /showroom only |
| Transit CC-CA (chassis) | buyable | Commercial | /new-commercial-trucks | MSRP starting at $44,890 | published | commercial chassis · not stated · /showroom only |
| F-Stripped Chassis | buyable | Commercial | /new-commercial-trucks | MSRP starting at $45,025 | published | commercial chassis · not stated · /showroom only |
| Super Duty (Commercial) | buyable | Commercial | /trucks/super-duty | MSRP starting at $45,975 | published | HD commercial pickup · not stated · /showroom only |
| E-Transit | buyable | Commercial · Electric | /new-commercial-trucks | MSRP starting at $48,150 | published | electric van · BEV (name-attested) · /showroom only |
| Transit (Commercial) | buyable | Commercial | /new-commercial-trucks | MSRP starting at $48,400 | published | commercial van · not stated · /showroom only |
| Chassis Cab | buyable | Commercial | /new-commercial-trucks | MSRP starting at $50,540 | published | commercial chassis cab · not stated · /showroom only |
| F-650 / F-750 | buyable | Commercial | /trucks/f-600-super-duty-chassis-cab | MSRP starting at $69,995 | published | medium-duty truck · not stated · 2027 MY |
| Explorer ST | buyable | Performance | /suvs/explorer | Starting at MSRP $54,905 | published | performance SUV · gas · Explorer ST trim |
| Ford GT | buyable | Performance | shop.ford.com/gt | (no price shown) | on-request | halo supercar · not stated · build/inquire |

### Verbatim anchors

- **The S1 MSRP footnote** (every starting price points at it): *"Current Manufacturer Suggested Retail Price (MSRP) for base vehicle. Excludes destination/delivery fee plus government fees and taxes, any finance charges, any dealer processing charge, any electronic filing charge, and any emission testing charge. Optional equipment not included."* → the all-in is **not** the shown number, but the starting figure itself is published, so rows stay `published` (a starting MSRP is a real, self-contained floor — unlike a med-only "from $X" that hides a mandatory membership).
- **Employee Pricing for All²** (live promo, sitewide): *"Employee Pricing (PGM #95388). Available on the purchase or lease of an eligible new 2025 or 2026 Ford vehicle from a participating dealer."* with a long exclusion list (Escape, Explorer, Super Duty Lariat/King Ranch/Platinum, Raptors, Mustang Dark Horse SC/GTD, Ford GT, …). Prices are a **point-in-time snapshot**, not fixed.
- **Powertrain "not stated":** for models without a captured PDP (Maverick, Ranger, Super Duty, Expedition, Bronco Sport, Transit, commercial chassis), the captured pages don't attest a powertrain to the SKU — recorded `not stated` rather than inferred from common knowledge (Maverick's standard hybrid, etc. are real but page-unattested here).

## Deep blocks

Earned for the five flagships — each resolves the trim ladder a roster row collapses, and carries a captured hero render. (`images/<sku>.jpg` = a clean Ford DAM beauty shot; the isolated-on-white configurator render is on a blocked host — see `site_notes`.)

### F-150 — `/trucks/f150` · hero: `captures/2026-06-04/images/f-150.jpg`
Ford's volume flagship. Trim ladder (PDP "Models"): **XL → STX → XLT → Lariat → Tremor → King Ranch → Platinum → Raptor**. Starts at **$39,330** (base XL); the off-road **Raptor** tops the range — its starting MSRP shows on the PDP but glued to a footnote marker in `f150.md`, so it's noted, not roster-quoted. Multiple gas engines attested (2.7L EcoBoost on STX/XLT cards).

### Mustang — `/cars/mustang` · hero: `captures/2026-06-04/images/mustang.jpg`
The sole car line. Ladder: **EcoBoost (Fastback/Convertible) → GT (V8) → Dark Horse → Dark Horse SC**, plus packages (FX, GT Performance, Nite Pony, Bronze Appearance, Troy Lee Designs TLD edition). Starts at **$32,640** (base EcoBoost); the **Dark Horse SC / TLD** halo tops the range (its six-figure MSRP is footnote-glued on the PDP — see `mustang.md`).

### Bronco — `/suvs/bronco` · hero: `captures/2026-06-04/images/bronco.jpg`
Off-road SUV, 3.0L EcoBoost V6 attested. Ladder: **Base → Big Bend → Outer Banks → Badlands → Heritage Edition → Stroppe Edition → Raptor**. Starts at **$39,995** (2025 base; **$40,795** for 2026); the **Raptor / Stroppe** trims top the range (their MSRPs are footnote-glued on the PDP — see `bronco.md`). A 2027 Bronco Filson special is also merchandised (no price).

### Mustang Mach-E — `/suvs/mach-e` · hero: `captures/2026-06-04/images/mustang-mach-e.jpg`
Electric SUV. Configured by drivetrain/trim: **Select RWD → Premium (RWD/eAWD) → California Special → GT / GT Performance Upgrade**, with drive modes (Engage/Whisper/Unbridle/RallySport). Starting **$37,795**; higher trims gated behind Build & Price (not shown on-page).

### Explorer — `/suvs/explorer` · hero: `captures/2026-06-04/images/explorer.jpg`
3-row SUV, 2.3L EcoBoost I-4 / 3.0L EcoBoost V6 attested; BlueCruise-capable. Ladder: **Active → ST-Line → Tremor → Platinum → ST**. Range **$38,465** (base) → **$54,905** (ST¹).
> ¹ Explorer ST "Starting at MSRP $54,905" — `captures/2026-06-04/showroom.md` / `explorer.md`.

## Provenance

- **Pages read (cited captures):** `/showroom` (roster backbone — all starting MSRPs), the five flagship PDPs (`/trucks/f150`, `/cars/mustang`, `/suvs/bronco`, `/suvs/mach-e`, `/suvs/explorer`), 4 category landings, and `/technology/bluecruise`. All under `captures/2026-06-04/`.
- **Scope:** all ~22 `/showroom` model lines enumerated at the model grain (the level Ford indexes at). **Trims are enumerated only for the 5 flagships** (deep blocks); other models' trims/per-trim prices are noted-but-not-enumerated (gated behind Build & Price).
- **Gated / unreachable:** per-trim MSRPs (Build & Price app); Ford GT price (none shown → `on-request`); commercial chassis have no marketing landing (slugs point to `/new-commercial-trucks` / `/showroom`, the attested sources).
- **Point-in-time caveat:** pricing is a snapshot — "Pricing for June 4, 2026" under an active sitewide Employee-Pricing promo; figures move run-to-run.
- **### Run profile:** opt-in run — per-SKU roster + **flagship hero images** captured (5 of them, promoted to `captures/2026-06-04/images/`). Heroes sourced from the fetchable `assets.ford.com` DAM (marketing beauty shots), since Ford's isolated configurator renders sit on hard-blocked hosts.
