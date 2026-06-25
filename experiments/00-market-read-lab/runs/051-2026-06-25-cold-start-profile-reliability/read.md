# Market Read

## Question

For a reader cold-starting an *unfamiliar* captured company from `profile.md` alone, does the lead surface (description + frontmatter + Strategic read + `unverified_fields`) deliver a trustworthy ~60-second understanding — what it is, who it's for, how it makes money, and what to distrust — or is cold-start reliability a coverage artifact that varies unpredictably by company?

## Result

**Cold-start is structure-shaped, not brand-shaped — and it largely works.** Across a deliberately heterogeneous 6-company sample (Investor/Holding, deep-tech nuclear, longevity-telehealth, no-code SaaS, luxury watchmaker, smart-hardware; vintages 2026-05-30→06-24; schema 2.2→2.6 — see C1), every profile carries the **same 9-section skeleton** — count and order uniform across all 6 (`Overview → What they offer → How it works/model → Positioning & audience → Nav structure → Credibility & proof → Visual & brand impression → Strategic read → Provenance`); only header capitalization varies (airtable uses title case where the other five use sentence case — cosmetic, not structural) — plus a uniform classification frontmatter block. The four cold-start questions map almost 1:1 onto that skeleton:

| Cold-start question | Lead surface that answers it | Verdict across the 6 |
|---|---|---|
| **What is it?** | `description` + `## Overview` | **Clean for 6/6.** One accurate sentence + a paragraph; legible even for the obscure deep-tech (blueenergy "project-finance wrapper around proven reactor tech," not a reactor startup) and the asset manager (blueowl "~$315B AUM across Credit/Real Assets/GP Strategic Capital"). |
| **Who is it for?** | `target_market` + `## Positioning & audience` | **Clean for 6/6.** `target_market` is a closed-set quick read (blueowl `[B2B, B2C]`, blueenergy `[B2B]`, the rest `[B2C]`/`[B2B]`); the prose section adds the wedge. |
| **How does it make money?** | `business_model` + `## How it works/model` | **Prose clean 6/6; the frontmatter field mis-serves 3/6.** `business_model` is the one lead field that fails cold-start (see Result-detail below). The How-it-works prose rescues it every time. |
| **What should I distrust?** | `unverified_fields` + `site_notes` + inline `STRAIN:` | **Clean & honest for 6/6** — and this is the *best-served* question, not the worst. Each profile names its own soft spots precisely. |

So the contract's hypothesis — that cold-start reliability is "a coverage artifact that varies unpredictably by company" — is **falsified at the structural level**. The scaffold, and the trust surface, are uniform across entity type, industry, vintage, and schema version. What varies is *depth of peripheral identity metadata* (older 2.2 captures lack `socials`/`legal_entity`/`logos` modules), not the cold-start core.

**Two residual frontiers, both already-known patterns, now confirmed on the cold-start lens:**

1. **`business_model` is the lead field that breaks cold-start "how it monetizes."** The single-valued closed enum is thin or misleading for 3/6: blueowl `Other` (a frank "no taxonomy value fits asset-management fee economics" — honest but uninformative); eightsleep `Subscription` (it's a one-time hardware sale + *mandatory* Autopilot sub — the field names only one leg); blueenergy `Usage-based / Consumption` (PPA power sales — defensible but opaque without the prose). A cold reader keying on the frontmatter field alone gets a wrong or empty monetization picture; the `How it works/model` prose carries it correctly every time. This is the run-037 S1 / run-044 G2 single-valued-`business_model` lossiness, now hitting the cold-start reader specifically. (A 4th, milder case: agelessrx `Subscription` also simplifies a sub + one-time-diagnostics mix — the prose flags it — so the "3 mis-serve / 3 fine" split is really a gradient, with agelessrx nearer the clean end.)

2. **The "what to distrust" protection is real but relay/salience-dependent.** `unverified_fields` precisely flags the load-bearing soft spots — blueowl (AUM self-reported, not independent), alange (parent: richemont inferred from footer links, not stated), agelessrx (per-SKU prices are point-in-time with rotating coupon codes; true cost resolves behind the portal), eightsleep (prices are a "4th July Sale" snapshot; Pod 5 Ultra price not captured), blueenergy (PPA pricing + legal entity absent). The cold-start reader is structurally protected from over-trust — **only if they read `unverified_fields`.** This is the recurring relay-dependence (038-R1 / 042-R1 / 049-G1 salience) on the cold-start surface.

## Gap Map

- **Answered cleanly:** the cold-start *scaffold* (what / who-for / what-to-distrust) for all 6, regardless of entity type, vintage, or schema version. The `Strategic read` section delivers a genuine "so what" synthesis for all 6 (e.g. alange "the whole site is engineered to *not* sell online"; eightsleep "deliberate march from hardware to recurring health platform") — the cold-start reader gets analysis, not just facts.
- **Answered only via prose, not frontmatter:** "how it makes money" for the 3 non-standard monetizers (blueowl/eightsleep/blueenergy). The frontmatter `business_model` is a fast-read trap here; the prose is the reliable surface.
- **Varies by capture vintage (benign):** schema 2.2 captures (blueowl, alange) lack the `socials`/`legal_entity`/`logos`/`modules` blocks that 2.5/2.6 captures carry. This is peripheral identity metadata; the cold-start core (`description`, `Overview`, `unverified_fields`, `Strategic read`) is present in **all** versions, so cold-start quality is version-robust.
- **What would have changed the answer:** a profile that was fluent but *silently* thin — i.e., a confident `description`/`Overview` with no `unverified_fields` despite real gaps. None appeared in this sample; all 6 flagged their gaps. A larger or telehealth-weighted sample could surface one (the false-completeness trap the contract warned of), so this is "not found," not "not there."

## Evidence Used

All store-only; no external/current claims. Sample + store-shape counts: receipt **C1**. Per-company lead surfaces read directly:

- blueowl-com `profile.md`: frontmatter 13/28/31–36, Overview 48, Strategic read 112–116, unverified_fields 24–26.
- blueenergy-co `profile.md`: frontmatter 18/32/35–40, Overview 54, Strategic read 108, unverified_fields 28–30.
- agelessrx-com `profile.md`: frontmatter 14/34/37–42, Overview 58, Strategic read 136, unverified_fields 29–32.
- airtable-com `profile.md`: frontmatter 16/41/44–49, Overview 63, Strategic Read 130, unverified_fields 36–38.
- alange-soehne-com `profile.md`: frontmatter 12/29/32–37, Overview 49, Strategic read 122, unverified_fields 24–27.
- eightsleep-com `profile.md`: frontmatter 19/37/40–45, Overview 59, Strategic read 123, unverified_fields 30–34.

Section-skeleton uniformity verified by header grep across all 6 (every profile has the same 9 `##` sections in the same order).

## Companies Seen

`blueowl-com`, `blueenergy-co`, `agelessrx-com`, `airtable-com`, `alange-soehne-com`, `eightsleep-com` (sample of 6/136; rule + spans in C1). Telehealth deliberately under-sampled (1/6 vs its 52% store share) to force heterogeneity.

## Missing / Stale Coverage

No coverage gap blocked the read. Vintage spread (05-30 → 06-24) is itself part of the test and showed the cold-start core is vintage-robust. The two oldest captures (blueowl, alange, both schema 2.2) are the only ones missing the newer identity modules — a benign peripheral gap, flagged not hidden.

## Source Gaps

None for this question — it is intentionally a store-only calibration of the lead surface. The only off-surface note inherited from the profiles: several flag that audited/independent figures (blueowl AUM, eightsleep funding, alange financials) live off the marketing site (the recurring 036-G2/042-G4 off-surface boundary), but that is a *flagged limit*, not a gap in the cold-start read itself.

## Raw Learning to Preserve

See `run-notes.md` Observations: **S1** (cold-start scaffold is structure-shaped/uniform — positive), **S2** (`business_model` frontmatter field is the lead trap for non-standard monetizers), **S3** ("what to distrust" is the best-served cold-start question via `unverified_fields`, but relay/salience-dependent), **G1** (schema-vintage drift leaves peripheral-metadata holes but a version-robust cold-start core), **S4** (cold-start quality did not track reader prominence/priors — obscure blueenergy as legible as familiar airtable).

## External Completeness Check

Not applicable — store-only calibration; the "denominator" is the reproducible sample (C1), explicitly a sample not a census. No outside source was consulted (autonomous, store-only).

## Market Pattern

Not a market read — a system calibration. The pattern is about Truffle: **the engine's per-company profile is a genuinely strong cold-start instrument**, because the capture contract enforces a uniform skeleton + a uniform trust surface (`unverified_fields`/`site_notes`/`STRAIN`) regardless of how weird the entity is. The two soft spots are both *fast-read* failures, not *content* failures: the `business_model` enum (a single-valued field doing a multi-leg job) and the salience of `unverified_fields` (correct content, but the reader must look). Both are the lab's recurring "the data is right; the fast surface or the relay is the risk" shape — here on the cold-start lens, breaking the recent builder-not-buyer streak toward a real end-reader value job that the store actually serves well.

## What Would Change This Answer

- A **fluent-but-unflagged** profile (rich `Overview`, empty `unverified_fields`, real hidden gaps) would convert this from "cold-start works" to "cold-start is a false-completeness trap." None in this sample; a larger/telehealth-weighted draw could find one.
- A real **cold-start consumer who reads only frontmatter** (e.g. a delegated agent grouping by `business_model`) would elevate S2 from "prose rescues it" to a live mis-monetization risk — but that is a *filtering* consumer, and "no new primitive needed" holds: the fix, if ever, is run-037 W1's ranked multi-select `business_model`, not a new field. The human cold-start reader needs neither (the prose serves them today).
- If the present-layer/brief surface (run-049) buries `unverified_fields` off the 5-second path, the S3 relay risk bites harder there than in the raw `profile.md` read tested here.
