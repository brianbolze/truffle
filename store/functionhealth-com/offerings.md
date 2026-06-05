---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.2"
domain: functionhealth.com
captured_at: 2026-06-01     # rides the profile's 2026-06-01 capture (homepage, /pricing, /scans)
enumeration: indexed-complete   # every priced line rostered; only sub-indexed leaves skipped (the 160+ included biomarkers; app-gated add-on prices)
site_notes: "Webflow; the priced catalog is small — one membership (/pricing) + 5 scan SKUs (cards on /scans, NO per-scan PDP, all link to /scans#). Scan prices are MEMBER-ONLY ('*Pricing for Function members only') — MRIs show list→member strikethrough, the two CTs show member price only → all scans are member-gated → partial. Add-on advanced tests (Galleri®/brain/mold/sexual-health) are member-app-gated, NO public à-la-carte price → on-request. The 160+ lab biomarkers are INCLUDED in the membership (not separately priced) — leaf, not rostered. Pricing is promo-framed ($365 is first-year, was ~$499; scans carry strikethrough promos) → snapshot. Scans are also bookable via my.ezra.com at non-member pricing. FAQ markets 'MRI starting at $499' — the actual member SKU floor is the $899 Annual MRI."
---

## Portfolio overview

A **Flagship + companions** shape: one product carries the company — the **Function membership ($365/yr, "$1/day")** — with a small set of priced add-ons layered on top. The shape finding is that the catalog is *deliberately* tiny: *"There's just one Function membership"* (no tiers), and everything else is a member-only à-la-carte purchase. The 160+ lab biomarkers aren't separate SKUs — they're the membership's contents.

Two structures sit under the membership:
1. **The membership** — `$365/yr`, self-contained, fully shown → `published`. Includes 160+ lab tests annually (Annual + Mid-Year draw), clinician review, and a personalized protocol.
2. **Member-only add-ons** — **MRI/CT scans** (via the Ezra acquisition) and **advanced tests** (Galleri, brain, mold, sexual-health) are priced *for members only*; the scan price assumes the $365 membership on top → `partial`, and the advanced-test à-la-carte prices sit behind the member app → `on-request`.

**Prominence** (the company's own labels + hero, not a market read):
- **Function membership — `[HIGH]`.** The entire site sells it; the hero, the pricing page, every CTA ("Start testing"). The company's own framing: *"There's just one Function membership."*
- **MRI & CT scans — `[MED]`.** A standing primary-nav item ("MRI & CT scans") and the headline of the Ezra acquisition, but presented as an add-on *for members*, not the front door.
- **Add-on advanced tests — `[LOW]`.** Named on /pricing and /what-we-test ("Access to Galleri®… Alzheimers & brain… mold reactivity") but member-app-gated with no surfaced price.

## Roster

Complete at the indexed level: the one membership + the 5 scan SKUs carry verbatim prices; the member-app add-on tests, B2B, and gifting are rostered at the grain the site surfaces. The scans are **cards on /scans with no individual PDP** (all link to `/scans#`).

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| **Function membership** | buyable | — | /pricing | "$365 per year" ("$1/day") | published | 160+ lab biomarkers · 2×/yr venous draw at Quest (or Getlabs mobile) · annual membership, HSA/FSA · clinician-reviewed |
| **MRI & CT scans** (via Ezra) | family | — | /scans | — | — | member-priced imaging add-ons; booked via Function or directly with Ezra |
| Annual MRI | buyable | MRI & CT scans | (no PDP — card on /scans) | "$999" → "$899" * | partial | full-body MRI (head · neck · abdomen · pelvis) · ~22 min · member-only price |
| MRI Scan with Spine | buyable | MRI & CT scans | (no PDP — card on /scans) | "$1699" → "$1,499" * | partial | MRI + targeted spine coverage · ~47 min · member-only price |
| MRI Scan with Skeletal and Neurological Assessment | buyable | MRI & CT scans | (no PDP — card on /scans) | "$3,999" * | partial | MRI + MSK (hips/knees) + brain/neuro + MR angiogram + body composition · member-only price |
| Heart CT Scan | buyable | MRI & CT scans | (no PDP — card on /scans) | "$349" * | partial | low-dose cardiac CT · coronary artery calcium (CAC) score · ~5 min · member-only price |
| Lungs CT Scan | buyable | MRI & CT scans | (no PDP — card on /scans) | "$399" * | partial | low-dose lung CT (nodules/emphysema/early lung cancer) · ~3 min · member-only price |
| **Add-on advanced tests** | buyable | — | /what-we-test | — (member-only, à-la-carte) | on-request | Galleri® / GRAIL multi-cancer · brain/Alzheimer's · environmental-toxin & mold reactivity · sexual-health · pricing behind the member app |
| **Function for Work** (B2B) | buyable | — | /for-business | — | on-request | employer-sponsored memberships + engagement/reporting tooling · custom (exec / remote / frontline teams) |
| **Gift membership** | buyable | — | /gifting | "$365 per year" | published | giftable annual Function membership; referral rewards paid via Impact |

### Verbatim anchors

The footnotes the Price / Visibility columns point at (quoted exactly from `captures/2026-06-01/`):

- **\* All scans are `partial` — member-gated.** Every scan card carries *"\*Pricing for Function members only."* (`/scans`). The headline number is the member price, which assumes the **$365/yr membership** on top — so the shown scan price is not the standalone all-in. The two MRIs additionally show a **list → member strikethrough** (Annual MRI *"$999 … $899"*; MRI with Spine *"$1699 … $1,499"*); the Skeletal/Neuro MRI and both CTs show **one** (member) price. Members also get *"Up to a $200 credit off scans."* Non-members are routed to *"Book directly with Ezra"* (my.ezra.com) at non-member pricing (not shown on Function's site).
- **Membership `published`:** *"$365 per year"* / *"#### $1 /day · Charged annually at $365"* (`/pricing`) — the full, self-contained price. *"There's just one Function membership"* (no tiers). HSA/FSA eligible.
- **Marketed MRI floor ≠ SKU floor:** the /pricing FAQ markets *"starting at $499 for an MRI scan,"* but the lowest member SKU on /scans is the **$899** Annual MRI. The $499 figure is a marketing floor; rostered prices are the on-page SKU cards.
- **Molecule / form audit:** N/A — Function sells **no pharmaceuticals**. Every "What" is a test or scan (form = blood draw or MRI/CT), so there is no molecule to attest or guess.

## Deep blocks

One earned — the scan line is the only place a roster row can't carry the pricing nuance that defines the catalog (per OFFERINGS "earned, not default"). The membership needs none (one self-contained price); the add-on tests need none (uniformly on-request).

### MRI & CT scans — the member-gated `partial` line
Spine: the Ezra-acquired imaging add-ons, and the reason the roster's scan prices are `partial` rather than `published`. Verbatim gold (`/scans`): each card states *"\*Pricing for Function members only,"* and the page frames imaging as a member benefit — *"Function provides 160+ lab tests for $1/day and member pricing on MRI and CT scans. For imaging only, schedule directly with Ezra."* So the shown $899 / $1,499 / $3,999 / $349 / $399 are member prices that require the $365 membership; the standalone (non-member) price is **not** published on Function's site (it routes to Ezra). The two MRIs show a list→member strikethrough ($999→$899, $1699→$1,499); the rest show member price only. Scan exclusions are spelled out per card (e.g. Annual MRI excludes *"Chest, Lungs, Heart, Breasts, Arms/Legs, Spine…"*). Eligibility caveat (verbatim): *"Scans aren't available for those under 18, currently pregnant, or with a pacemaker or certain prosthetic implants."*

## Provenance

- **Pages read (cited captures, 2026-06-01):** `/pricing` (membership price + tiers), `/scans` (the 5 scan SKU cards + member-only footnotes), homepage. All in `store/functionhealth-com/captures/2026-06-01/`. Authored alongside the `telehealth.md` cohort pack and the `profile.md` 2.5 (logos) refresh.
- **Scope:** all priced lines are rostered (membership + 5 scans = complete at the indexed level). **Sub-indexed leaves, by design:** the **160+ individual lab biomarkers** (included in the membership, not separately priced) and the **à-la-carte advanced-test prices** (Galleri/brain/mold/sexual-health — behind the member app). No whole line omitted → `enumeration: indexed-complete`.
- **Gated / unreachable:** advanced add-on test pricing (member-app-gated); B2B "Function for Work" pricing (custom/contact); non-member scan pricing (routes to my.ezra.com).
- **Point-in-time caveat:** pricing is a **snapshot, not fixed** — $365 is explicitly *first-year* membership pricing (was ~$499), and scans carry strikethrough member promos ($999→$899, $1699→$1,499). Re-check next run.
- **Run profile:** non-vanilla — Express `/research-telehealth-brand` run; `offerings.md` authored over a warm (2026-06-01) base alongside `telehealth.md` + the `profile.md` `logos:{}` (2.5) addition. No hero-image capture this run (a diagnostics/imaging brand — no product renders to pull).
