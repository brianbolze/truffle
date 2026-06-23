---
created: 2026-06-20
last_updated: 2026-06-20
authors: both
status: raw idea harvest — first ~20 runs (000–023)
companion: 2026-06-20-first-20-runs-retro.md
---

# Idea harvest: mining the raw runs

> **The thinness was the triage's fault, not the lab's.** Five agents read all 24 runs' raw files (not the merged backlog) and pulled **~345 distinct observations**. The triage had compressed all of it into ~2 ideas + 3 decisions. The runs were generating plenty — the clean-backlog funnel downstream threw the divergence away. This doc is the anti-triage: lightly clustered for navigation, **nothing merged out**, every idea traceable to the runs that raised it.

**Counts (raw, pre-cluster):** ingredient-wishes ~114 · friction ~71 · category-shape ~47 · use-cases ~50 · surprises ~63.

**The big one for the "we found no new ingredients" worry:** there are **~15 distinct new-ingredient ideas** in here, not zero. They're section A/B below.

*Method note: clustering here is for navigation only — it groups sightings, it does not dedup-to-backlog. Each cluster keeps its run references so you can pull the raw item. This is the "divergent idea stream that never gets merged" the retro calls for.*

---

## A. New outside-the-store sources (genuinely new "farm inputs")

*The richest vein, and the one the lab barely touched. These are sources we don't capture at all today.*

- **"Best-of" listicles as a missing-segment radar.** Periodically run SERP → ≥2 authoritative "best [category] [year]" lists → cross-source intersection → diff against the store. Not to research a brand — to detect *entire categories the store has never seen*. Run 022 found 8+ missing women's-menopause brands for 14 credits. *(012, 022)* — **strongest single idea here**; it's the direct fix for the selection-bias blind spot. **Implemented 2026-06-22 as [`QUERYING.md` Recipe 9](../../../../QUERYING.md#recipes): bounded-live coverage radar; no helper, stored Signal, category object, or capture campaign.**
- **What buyers actually cross-shop (demand-side).** "Alternatives to X" SERPs, owned `/compare` + `/vs` pages, Trustpilot "people also looked at," Exa neighbors, search co-occurrence. Turns every competitor/substitute read from a supply-side *guess* into evidence. *(005, 017, 019)*
- **The real price floor outside the brands.** Manufacturer-direct (NovoCare, LillyDirect) and retail (Walmart) pricing. A DTC-only cohort literally cannot see the cheapest access path — it's invisible by construction. *(000, 002)*
- **Category-wide regulatory status.** FDA 503A/503B compounding legality, shortage lists, warning letters. Governs an entire cohort at once but has no company domain to attach to — the "homeless signal" problem. *(002)*
- **Corporate events.** Partnerships, M&A, funding rounds (Hims×Novo, Noom's pivot). Real market moves that are invisible inside a static company snapshot. *(002)*
- **Does the trust badge actually hold.** Verify a claimed LegitScript seal / clinician license / pharmacy accreditation against the *issuing registry*, and whether it's still current (seals lapse between captures). *(021)*
- **Market size / search demand.** Google Trends or keyword volume + category population estimates (IBISWorld, CB Insights, trade rosters). Answers "how big is the whitespace?" and gives a neutral denominator for "is our cohort representative?" *(020, 022)*
- **Brand age / launch date (WHOIS / registration).** The corroborating fact that turns Wayback's misleading `tenure_days` into a confirmable brand-era marker. *(006)*
- **Outcome / clinical-evidence citations.** Per-brand study, FDA, or PubMed references — makes the "proof vs promise" axis machine-readable instead of a read of hero copy. *(009)*
- **Shared-legal-entity (CIK) layer.** Catches rollups the domain key can't see (Niagen → two brand domains, one issuer). *Borders the anti-Doro line — flag, don't rush.* *(007)*

## B. Deeper capture of sources we already touch

*Less "new farm," more "harvest the field we already planted." Mostly depth/schema, but high-leverage.*

- **Review/forum BODY text** — not just the star rating. The complaint taxonomy and objection clusters carry the real story (the henrymeds distress, the billing-after-cancel pattern). The one new ingredient the lab actually used. Pairs naturally with the store's *already-captured* billing terms as the rebuttal half. *(005, 008, 009, 011)*
- **Review-platform integrity metadata** — paid-profile / invited-review / merged-profile / sample-size, so two scores are actually comparable (remedymeds 4.6 vs hims 3.0 are *not* the same number). *(005, 011)*
- **Real "what changed" tracking** — a rendered-content fingerprint on *our own* cadence. Today's Wayback signal measures the archiver's re-crawl, not the page; the freshness job wants the latter. *(018)*
- **Behind-login / behind-intake content** — dose ladders and true per-dose prices that live inside the quiz or member app (gogeviti, ~half the GLP-1 cohort). A whole class Firecrawl can't reach. *(009, 010, 023)*
- **Structured pricing** — numeric price, all-in vs teaser, mandatory bundled fee, billing cadence, commitment length, promo-vs-steady-state, and the checkout page as the authoritative surface. So "$X/mo" stops lying (Eden's `$99` is really `~$198`). *(000, 010, 023)*
- **Supplier profiles + the supply-side mirror** — capture the pharmacy/clinical backends as their own profiles, *and* capture their client-recruitment pages. Concentration can be read from the supply side far more cheaply than re-scraping every DTC brand. *(001, 014, 016)*
- **Image-provenance field** — bespoke/owned vs stock vs manufacturer imagery; the visual layer holds this as prose but not as a field that aggregates. *(019)*
- **Promote reliability siblings to fields** — Wayback snapshot-density, signal integrity flags — so the headline number can't mislead at the point of capture rather than needing per-run repair. *(006)*

---

## C. Structural / category-shape insights

*How a "market" actually behaves — the conceptual raw material for any future category capability.*

- **DTC brands are thin skins over shared backend infra.** The modal brand is a marketing/UX layer over a third-party clinical network + compounding pharmacy. The backend map is often more informative than the front-door map. *(001, 004, 014, 016)*
- **"Anchors-to" ≠ "serves."** A brand anchors one category but sells into many; the anchor-only grep silently drops `multi/none` generalists (LifeMD, Nurx, Wisp) from *every* cohort census. Membership needs to be its own dimension. *(012, 013, 015, 016)*
- **Category boundaries are surface-dependent.** The store and the listicles describe two different "GLP-1 markets." A "default brand" only means something across ≥2 independent sources. *(012)*
- **Competitive/substitute is a buyer-relative *judgment*, not a fact.** The same brand is a substitute for one buyer and adjacent for another — a different *kind* of primitive than a joinable backend edge. *(017)*
- **Two denominator problems compound and need different fixes.** Selection-bias (the corpus was built men's-hormone-heavy) enters at capture time and no query can fix it; the anchored-only under-count enters at query time and a wider grep fixes it. *(020, 022)*
- **Judgment-dense layers aggregate by prose-convergence, not field-rollup.** The visual layer's `polarity` field can't be summed; independent agreement across separately-mined impression paragraphs is the trust mechanism. *(019)*
- **Change-pulse needs a capture-cadence denominator + pinned subject identity** — "same domain + same source" is *not* a diffable pair. Distinct from market-membership. *(018)*
- **Derived cross-run judgments are homeless** — too ephemeral for the store, too buried to find without re-reading every run. *(008)*
- **The taxonomy under-resolves real segments** — `womens-HRT` is one cell hiding a 10+-operator menopause market. *(022)*

## D. Recurring friction (where Truffle fought the analyst)

- **Cohort boundaries are hand-drawn every run** — anchor grep → term grep → hand-tier. The single most recurrent toil. *(000, 008, 013)*
- **Load-bearing facts live in prose, not fields** — offer structure, membership, pharmacy partners, pricing shape, proof-device flags. Forces re-derive-from-prose, the lab's #1 error source. *(010, 013, 014, 021, 023)*
- **The signal-reading loop is rebuilt from scratch** each time — latest-per-dir + frontmatter join. *(005, 006, 007)*
- **Relations split across two files/shapes** — `parent`/`owns` in frontmatter, partners in prose. *(001, 014)*
- **Entity resolution is manual** — `ls store/*name*`, Allara vs "Allara Health." No canonical name normalization. *(000, 016, 022)*
- **Enumeration-grain footguns** — company-grain glob misses page-grain Wayback; `grep -v` on the full line over-drops; whole-file grep inflates counts to 100%; archived copies overcount the cohort. *(004, 016, 018, 021)*
- **No promo-vs-steady-state / price-staleness convention.** *(010, 023)*

## E. Use-cases the runs actually served

- **Brief-ready strategist/creative one-pagers** (the Scott-Witt "lands in 5 seconds" cut). *(009, 015, 019, 021)*
- **New-entrant positioning / whitespace attack vectors** (billing-fairness as the unclaimed trust device). *(010, 011, 013)*
- **AI-safety guardrail** — stop a downstream agent sorting by a misleading score or a fake-comparable price. *(005, 006, 023)*
- **Capture-prioritization worklist** — what to research next; Pantry intake queue. *(012, 022)*
- **Supply-chain / vendor-risk reads** — who's the category's single point of failure. *(001, 014, 016)*
- **Due-diligence / investor triage** — funding × reputation, dedup false-positive "funded" reads. *(007)*
- **Company-health early warning** — review bodies surfaced henrymeds distress before any press. *(011)*
- **Longitudinal corroboration** — only a persistent store enables cross-run confirmation. *(008)*

## F. Sharpest surprises

- **The headline field is always the wrong field.** Trustpilot *score*, Wayback *tenure_days*, SEC *total_hits* — across all three signals, the easiest-to-grep number is the most misleading one. A profound, repeated pattern. *(005, 006, 007)*
- **Store-only reads can be the *inverse* of reality.** "Women-anchored brands live in GLP-1" (run 020) was 100% a coverage artifact — the real segment is menopause/HRT (run 022). Eden's cheapest-looking price is the most expensive. *(020→022, 023)*
- **The convenient grain is the wrong grain** — the delta-able metric is the least useful; the greppable visual field is the one that won't aggregate. *(018, 019)*
- **Marketing language contradicts itself** — BlueChew's "our own pharmacy" names three third parties on the same page; "no membership" is itself a positioning move. *(001, 010)*
- **The backend axis flips by cohort** — clinical edges join in GLP-1, pharmacy edges join in non-GLP-1. *(014, 016)*
- **Sticker price is theater, category-wide** — not one aberrant brand, three convergent mechanisms across 19. *(010)*
- **The store both out-completes and under-covers** — it beat the Notion seed (000) yet missed a whole segment (022); coverage is uneven, not uniformly thin/deep. *(000, 022)*
