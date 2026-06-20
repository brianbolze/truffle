# Market Read

## Question

Does a dedicated behavioral / mental-health telehealth segment (online therapy +
psychiatry + behavioral Rx) exist that the captured telehealth corpus has *not* captured,
and where does the corpus's membership boundary actually fall — Rx-commerce/hormone lane
vs behavioral-health lane? Produce a tiered capture-candidate worklist and a clear
store-vs-market boundary statement. **Membership read only** (no pricing/offer/quality
depth).

## Direct Answer

**Yes — a large dedicated behavioral/mental-health telehealth segment exists, and the
captured corpus contains essentially none of it.** Two authoritative listicles (Forbes
Health, Healthline; both dated 2026, both affiliate-monetized) name a **5-brand
cross-source-recurrence head — BetterHelp, Talkspace, Brightside Health, Doctor on Demand,
MDLive — and 0 of the 5 are in the store** (no directory match; not even mentioned in any
of the 54 `telehealth.md` bodies). The broader union of named platforms (Grow Therapy,
Amwell, Teladoc Health, Sesame Care, LiveHealth Online) plus segment leaders surfaced by
SERP but not on these two lists (Cerebral, Talkiatry) are **also all store-absent.**

The boundary finding: **the captured "telehealth" corpus is not a telehealth corpus — it
is an Rx-commerce / metabolic-hormone corpus.** Its membership stops hard at the behavioral
lane. Of 54 packs, **0** are anchored to mental/behavioral/psychiatry; the `anchor_category`
values are GLP-1, TRT, longevity/NAD, sexual-health, peptides, hair, labs, primary-care,
womens-HRT, multi/none. This is the same selection-bias boundary run 020 hypothesized and
run 022 confirmed for women's menopause — but a **lane-level** gap (an entire care
modality) rather than an audience-level one.

This is a **membership** statement: store-absent = real + uncaptured, **not** a claim about
the segment's size, share, or quality.

## Gap Map

This is a `gap-probe`, so the gap *is* the result.

- **Where Truffle answered cleanly:** the store side is unambiguous and cheap — one grep
  proves 0/54 behavioral anchoring; one token scan proves 0 directory matches across all
  135 store domains; one body grep proves 0 mentions. The store can state its own boundary
  precisely.
- **Where Truffle fell short:** the store **cannot see the segment at all.** No store-only
  query can surface BetterHelp/Talkspace/Brightside/Cerebral/Talkiatry because the corpus
  was never built to include behavioral health. This is the run-022 lesson at lane scale:
  a **selection-bias** boundary is invisible to every store-only query and resolvable only
  with outside evidence or new capture.
- **What evidence would change the answer:** if a token-match false-negative hid a captured
  behavioral brand under a renamed/parent domain (checked: none found), or if a behavioral
  line lived inside a captured `multi/none` generalist (checked: 0 body mentions of the
  brand set). Both checks came back clean, so the boundary statement is robust at membership
  grain.

## Evidence Used

For `bounded-live`, this section lines up with `run-notes.md` `live_evidence_used`.

- **C1 — Forbes Health named set (S1, secondary, affiliate-disclosed):** "10 Best Online
  Therapy Platforms In 2026", modified 2026-05-07, captured 2026-06-20. Verbatim
  JSON-extracted set (10): Grow Therapy, BetterHelp, Talkspace, Brightside Health, Amwell,
  Teladoc Health, Sesame Care, LiveHealth Online, Doctor on Demand, MDLive. Page's own note:
  ranking is therapy/psychologist visits only; "Most Popular is calculated from the number
  of times each affiliate product was selected" → affiliate-confounded ordering (MRL-008
  listicle flavor).
- **C2 — Healthline named set (S2, secondary, affiliate-disclosed):** "The Best Online
  Therapy Services That Take Insurance in 2026", modified 2026-05-26, captured 2026-06-20.
  Verbatim JSON-extracted platform set (5, after excluding 7 insurance *payers*
  Cigna/Anthem/UnitedHealthcare/Aetna/Humana/BCBS/Kaiser that the extractor swept in):
  Brightside Health, Doctor on Demand, Talkspace, BetterHelp, MDLIVE.
- **C3 — cross-source recurrence head (derived from S1∩S2):** BetterHelp, Talkspace,
  Brightside Health, Doctor on Demand, MDLive — the 5 names on *both* authoritative lists.
  (Grow Therapy appears in Forbes's body and Healthline's `og:description` "Talkspace, Grow
  Therapy, and more" but was not in Healthline's extracted body set — counted as a *likely*
  6th, direction-finding only, not in the strict head.)
- **C4 — store diff (S3, derived/local-store):** the 5-brand head and the full union all
  return **0** matches against `ls store/` (135 domains) and **0** mentions across
  `store/*/telehealth.md` bodies (54 packs). Store behavioral anchoring = 0/54.
- **C5 — segment-exists corroboration (S4, direction-finding):** 2 SERP queries surfaced
  Cerebral and Brave Health as direct brand results plus the two listicles, corroborating a
  live, dense behavioral-telehealth market beyond the listicle heads.

## Companies Seen

- **Market behavioral-telehealth brands named (union, all store-absent):** BetterHelp,
  Talkspace, Brightside Health, Doctor on Demand, MDLive, Grow Therapy, Amwell, Teladoc
  Health, Sesame Care, LiveHealth Online; + SERP-surfaced Cerebral, Brave Health, Talkiatry.
- **Store behavioral-telehealth brands:** none. (`standishspring-com` token-matched "spring"
  but is not a behavioral-health brand — a false-positive token hit, excluded.)

## Missing / Stale Coverage

**Tiered capture-candidate worklist** (propose-don't-write; for a human-gated
`/research-company` campaign — NOT executed here, NOT written back to `store/`):

- **Tier-1 (cross-source recurrence across both authoritative listicles, store-absent):**
  BetterHelp, Talkspace, Brightside Health, Doctor on Demand, MDLive.
- **Tier-2 (single authoritative listicle, store-absent):** Grow Therapy (Forbes #1; also in
  Healthline's og description), Amwell, Teladoc Health, Sesame Care, LiveHealth Online.
- **Tier-3 (strong SERP-surfaced segment leaders not on these two lists, store-absent):**
  Cerebral, Talkiatry, Brave Health — the medication-management/psychiatry sub-lane that the
  two *therapy*-led listicles under-weight (Forbes explicitly scopes itself to therapy
  visits, not psychiatry).

Note: several Tier-1/2 names (Teladoc, Amwell, MDLive, Doctor on Demand, LiveHealth) are
**multi-service virtual-care platforms**, not behavioral-pure — they'd enter the store as
`multi/none`, with behavioral as one line. Brightside, Cerebral, Talkiatry, BetterHelp,
Talkspace, Brave Health are the behavioral-anchored pure-plays.

## Source Gaps

- **2 affiliate listicles = coverage radar, not census** (MRL-008/MRL-001 run-012 rule).
  Both monetize referrals; only the cross-source-recurrence head is decision-grade; the
  tails are affiliate-confounded. A third authoritative non-affiliate source (e.g. an
  academic or .gov directory) would harden the head but was not needed for a membership
  diff this lopsided (0/5).
- **Therapy-vs-psychiatry sub-lane split:** the two lists are *therapy*-led, so the
  *medication-management/psychiatry* sub-segment (Cerebral, Talkiatry, Brightside-Rx) is
  under-named by the panel and was filled in only at SERP/direction-finding grade.
- **Insurer contamination in extraction:** Healthline's structured extract swept in 7
  insurance payers as "brands"; corrected by hand (excluded from the platform set). A naive
  extract would have over-counted the named set by 7.

## Raw Learning to Preserve

See `run-notes.md` Discovery ledger: **O1** (boundary is lane-level, not audience-level),
**O2** (corpus is Rx-commerce-shaped, "telehealth" is a misnomer for it), **S1-idea**
(therapy-vs-psychiatry sub-lane split is a capture-scoping decision), **F1**
(insurer-contamination in listicle extraction), **G1** (3rd coverage-radar sighting →
the bounded-live recipe now spans GLP-1 / women's-menopause / behavioral — three lanes).

## External Completeness Check

The store-derived denominator (0 behavioral brands) was checked against the outside panel
(13 named market brands across 2 authoritative listicles + SERP). The two are **disjoint** —
the cleanest possible completeness result for a boundary probe: the store's behavioral
coverage is not thin, it is **empty**, and the outside panel proves the segment is real and
populated. Token-match reconciliation could in principle miss a renamed domain, but a manual
`ls store/` scan and a body grep both returned 0, so this is "not found by two independent
local methods," a strong floor for absence.

## Market Pattern

**The captured corpus's "telehealth" label overstates its scope by roughly one care
modality.** What the store actually holds is **direct-to-consumer Rx commerce** —
metabolic (GLP-1), hormone (TRT, menopause, longevity), and sexual-health/derm/hair Rx —
where the product is a prescribed molecule shipped to the door. Behavioral health is a
different *operating model* (recurring talk-therapy sessions, licensed-therapist matching,
insurance-billed visits, medication-*management* rather than medication-*commerce*), and the
corpus contains none of it. That is consistent with the corpus's construction history (seeded
by GLP-1/men's-hormone lab runs 000/001/008/014/016) and is the **third** confirmed
selection-bias boundary, now at **lane** scale:

- run 020 → audience asymmetry (men-heavy) — *hypothesized* store-only.
- run 022 → women's-menopause segment — *confirmed* bounded-live (audience-level lane gap).
- run 024 → behavioral-health modality — *confirmed* bounded-live (**care-modality**-level
  lane gap, the largest yet).

## What Would Change This Answer

- A capture campaign on the Tier-1/3 candidates would convert this membership finding into
  captured State and move the corpus boundary outward (and let a future "what does this
  store cover" read stop calling itself telehealth-complete).
- Evidence that any captured `multi/none` generalist already sells a behavioral line under a
  domain the token scan missed — checked, none found, but a deeper per-pack read could in
  principle surface one.
- A decision that behavioral health is **out of scope** for this store by design (a
  legitimate framing): then the finding flips from "coverage gap" to "scope boundary working
  as intended" — the read does not adjudicate which; it only maps where the edge is.
