# Run Notes

```yaml
run_status: reviewed
evidence_mode: bounded-live
autonomous_eligible: yes
termination_reason: completed
pressure_lenses_fired: [coverage-caveat, denominator-reconciliation, source-panel, source-rigor]
```

> **Loop 2 outcome (2026-06-20):** Reviewed via a 3-pass adversarial workflow (evidence
> verifier + consumer + developer, Sonnet). **Verifier: PASS** — independently re-derived the
> store floor (0/54 behavioral anchors), the 0/135 directory diff + 0 body mentions, the strict
> S1∩S2 5-brand intersection, and the payer exclusion; absence language, membership-not-size
> discipline, and the State/Judgment (gap-vs-scope) boundary all held. One cosmetic fix applied:
> receipt S2 `Snippet-only?` cell now `no`. **Consumer: valuable (yes)** — highest-signal
> coverage-radar yet; clean binary result + tiered worklist + the "DTC Rx-commerce, not
> telehealth" corpus-identity reframe; biggest limit is 2 affiliate listicles + membership-only;
> the in-scope-vs-out-of-scope call is a human one. **Developer: submit 4 Evidence Logs, no new
> item** — appended to **MRL-001** (selection-bias now confirmed at *care-modality* scale, 3rd
> sighting, scale-invariant), **MRL-002** (3rd sighting of the bounded-live coverage-radar
> recipe — name it, don't build it), **MRL-008** (new platforms-vs-payers extraction confound,
> F1), and **MRL-009** (2nd tiered capture worklist). No graduation; no `store/` mutation; no
> `Human Notes` touched.

## 30-second operator read

- **Did the run work?** Yes — the 4th bounded-live run (after 011/012/022), **12 net
  Firecrawl credits** (14 gross − 2 refunded via search feedback). It is the most lopsided
  coverage-radar result in the lab: a 5-brand cross-source-recurrence head
  (BetterHelp, Talkspace, Brightside Health, Doctor on Demand, MDLive) with **0 of 5
  captured**, and the whole union (incl. Cerebral/Talkiatry) also store-absent.
- **What was awkward?** Nothing mechanical. The one judgment catch: Healthline's JSON extract
  swept in 7 **insurance payers** (Cigna, Anthem, UHC, …) as "brands" — hand-excluded. The
  discipline was keeping it a *membership* read (who exists / who's captured) and not drifting
  into pricing/offer/quality depth.
- **What should the next agent know?** This is the **third** confirmed selection-bias boundary
  (run 020 audience → run 022 women's-menopause → run 024 behavioral) and the **largest**:
  a whole *care modality* missing, not an audience slice. The headline reframes the corpus:
  what the store calls "telehealth" is really **DTC Rx-commerce** (metabolic/hormone), and
  its membership stops hard at the behavioral lane. Highest-value follow-up is a human-gated
  capture campaign (Tier-1/3 worklist) — **not autonomous** (Firecrawl spend).

## What happened

Store floor: `grep anchor_category mental|behavioral|psych` → 0/54; `anchor_category`
distribution confirms an Rx-commerce/hormone-shaped corpus. Ran 2 firecrawl_search queries →
Forbes Health + Healthline as the two authoritative listicles. JSON-scraped both for verbatim
`named_brands`, excluded 7 insurer names from the Healthline set, took the cross-source
intersection (5), and token-diffed the head + union against `ls store/` (135 domains) and
`telehealth.md` bodies (54). 0 directory matches, 0 body mentions. Stop rule fired once the
diff was computable. Wrote `read.md` + one source-panel receipt. No crawl, no owned-page deep
read, no `store/` mutation, no write-back. Submitted `good` feedback on both searches (2
credits refunded).

## Discovery ledger

Greedy, append-only raw learning. Preserve singletons here before triage compresses anything.

| ID | Kind | Raw observation / wish / friction / surprise / gap | Evidence or pointer | Why it matters | Later clock |
|---|---|---|---|---|---|
| O1 | observation | The boundary is **lane/modality-level**, not audience-level — an entire care model (talk-therapy/psychiatry) is absent, vs run 022's audience slice. | read.md Market Pattern; C3/C4 | First time the selection-bias boundary is shown at care-modality scale; biggest store gap yet found. | triage-candidate |
| O2 | surprise | The corpus's "telehealth" label overstates scope by ~one modality — it is really **DTC Rx-commerce** (metabolic/hormone). 0/54 behavioral anchoring; union disjoint from market panel. | C4; `anchor_category` distribution | Reframes what the store *is*; affects any "what does this store cover" claim. | watch |
| F1 | friction | Listicle JSON extract swept 7 **insurance payers** into the named-brand set (Healthline). | S2 raw vs corrected set in receipt | A naive coverage-radar would over-count the market set by 7; the extractor needs a "platforms, not payers" guard. | watch |
| S1 | source-idea | The two best-of lists are **therapy-led**; the psychiatry/medication-management sub-lane (Cerebral, Talkiatry, Brightside-Rx) is under-named by them. | Forbes og note "therapy/psychologist visits only"; S4 SERP | Behavioral capture scoping is itself a two-sub-lane decision (therapy vs psych-Rx), not one segment. | notice-only |
| G1 | observation | 3rd sighting of the bounded-live coverage-radar recipe — now spans **three lanes** (GLP-1/012, women's-menopause/022, behavioral/024), identical shape each time. | run-notes 012/022; this run | Recipe generalizes across maximally different verticals; strengthens MRL-002's bounded-live variant. | triage-candidate |
| R1 | observation (Loop 2 dev) | F1's payers-as-brands confound corrupts set **membership** (~60% inflation: 7 payers on a 5-platform set), categorically distinct from the affiliate-ordering confound (012) which only corrupts rank/tail. | developer-review.md Guardrails row; MRL-008 | Sharpens the confound family: a coverage-radar's named *set* can be wrong, not just its ordering — so the platforms-only filter is a membership prerequisite, not a polish step. | ready-for-triage |
| R2 | observation (Loop 2 consumer) | The headline is a **scope-vs-coverage** ambiguity the lab cannot adjudicate: behavioral may be a deliberate store scope boundary, not a defect. | consumer-review.md Verdict; read.md "What Would Change This Answer" | The same finding flips between "largest coverage gap" and "scope working as intended" on a human framing call — the worklist is informational until that call is made. | notice-only |

## Inputs and scope

- **Store side (S3):** `ls store/` (135 domains); `store/*/telehealth.md` (54 packs);
  `anchor_category` grep (0 behavioral); token-match of the head+union against both surfaces.
- **External panel:** Forbes Health "10 Best Online Therapy Platforms 2026" (S1); Healthline
  "Best Online Therapy … That Take Insurance 2026" (S2); 2 SERP queries (S4, direction-finding).
- **Exclusions (by contract):** pricing/offer/quality depth; demand/size evidence; owned-page
  deep reads (stop rule fired before they were needed); 7 insurance payers mis-extracted as
  brands; non-behavioral categories.
- **Receipt:** `receipts/behavioral-health-panel-2026-06-20.md` (S1–S4; C1–C5).

## Live evidence plan

```yaml
live_evidence_plan:
  approved_by: Brian
  approval_scope: autonomous Market Read Lab runs (standing bounded-live policy; runs 011/012/022 precedent)
  budget_class: light
  review_after: "this is the 4th bounded-live run (011/012/022 were the first 3, reviewed at the run-022 checkpoint)"
  evidence_goal: >-
    Determine whether a dedicated behavioral/mental-health telehealth segment exists that the
    store has not captured, and map where the captured telehealth corpus's membership boundary
    falls. Output: a tiered capture-candidate worklist + a store-vs-market boundary statement.
    Membership read only — no pricing/offer/quality depth.
  source_families_allowed: [SERP/listicle, owned/official brand pages (light, identity-confirm only), reviews/forums (light)]
  source_families_preferred: ["authoritative 'best online therapy / psychiatry / mental-health telehealth 2026' listicles", owned brand front-door pages]
  source_families_disallowed: [login-only/paywalled, broad crawling, private data, ad/social scraping, owned-page pricing/offer-depth reads]
  stop_when:
    - ">=2 authoritative listicles yield a cross-recurrence named set and the store diff is computable with caveats"  # FIRED
    - the next source would expand the question (pricing/offer/quality depth) rather than verify membership
    - remaining uncertainty is a framing judgment, not a sourcing gap
  disallowed_actions: [write-back to store/, code/schema/template changes, durable primitive creation, triage graduation]
```

## Live evidence used

```yaml
live_evidence_used:
  - source_or_query: "best online therapy and psychiatry telehealth platforms 2026"
    source_family: SERP/listicle
    action_taken: searched
    reason: surface authoritative listicles + confirm head brands appear as direct results
    source_grade: direction-finding
    captured_at: 2026-06-20
    spend_note: paid-credit   # 2 credits, 1 refunded (good feedback)
    claim_ids_supported: [C5]
  - source_or_query: "best online mental health services 2026 therapy psychiatry medication"
    source_family: SERP/listicle
    action_taken: searched
    reason: second SERP angle; corroborate Cerebral/Brave Health (psychiatry/med-management sub-lane)
    source_grade: direction-finding
    captured_at: 2026-06-20
    spend_note: paid-credit   # 2 credits, 1 refunded (good feedback)
    claim_ids_supported: [C5]
  - source_or_query: https://www.forbes.com/health/mind/best-online-therapy/
    source_family: SERP/listicle (affiliate)
    action_taken: scraped
    reason: extract verbatim named set (10) for one authoritative listicle
    source_grade: secondary
    captured_at: 2026-06-20   # page modified 2026-05-07
    spend_note: paid-credit   # 5 credits
    claim_ids_supported: [C1, C3]
  - source_or_query: https://www.healthline.com/health/mental-health/online-therapy-that-takes-insurance
    source_family: SERP/listicle (affiliate/SEO)
    action_taken: scraped
    reason: second authoritative listicle for cross-source recurrence
    source_grade: secondary
    captured_at: 2026-06-20   # page modified 2026-05-26
    spend_note: paid-credit   # 5 credits
    claim_ids_supported: [C2, C3]
# Total: 14 Firecrawl credits gross, 2 refunded via search feedback = 12 net.
# Stop rule fired after the store diff was computable; no third listicle or owned-page read.
```

## Friction log

- **No mechanical friction.** Store side is two greps; the named-set extraction is two JSON
  scrapes; the diff is a token grep. The only judgment work — exclude insurer payers (F1),
  hold the membership line — was handled by hand + the contract's stop rule.
- The bounded-live coverage-radar recipe is now sighted **three** times (012 GLP-1, 022
  menopause, 024 behavioral): SERP → ≥2 authoritative listicles → JSON-extract named sets →
  cross-source intersection → token-match store diff. Stable shape; candidate for naming in
  the MRL-002 family, not building.

## Evidence limits

- **2 affiliate listicles = coverage radar, not census** (MRL-008/MRL-001 run-012 rule). Only
  the cross-source-recurrence head is decision-grade; tails are affiliate-confounded.
- **Membership, not size.** "Store-absent segment" = real + uncaptured, NOT large/dominant.
- **Token-match absence** = "not found by directory + body grep," not "proven absent" under a
  renamed/parent domain (manual `ls` scan found no extra hits; `standishspring-com` excluded as
  a false-positive "spring" token).
- **Therapy-led panel** under-names the psychiatry/medication-management sub-lane; Cerebral/
  Talkiatry carried at SERP/direction-finding grade only.

## Loop 1 exit check

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`: **pass** (planned bounded-live)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` was present and followed: **pass** (stayed in allowed families; stop rule fired before owned-page drift)
- If `bounded-live`, every outside source was logged in `live_evidence_used`: **pass** (4 sources: 2 searches + 2 scrapes)
- If `bounded-live`, stop rules and spend notes were recorded: **pass** (14 gross / 2 refunded / 12 net itemized; stop rule "diff computable" fired)
- No disallowed action happened: **pass** (no crawl, no `store/` mutation, no write-back, no durable primitive, no triage graduation)
- Required citations / receipts present and source-graded: **pass** (S1–S4 graded; receipt present)
- No snippet treated as evidence: **pass** (named sets from full list pages via JSON scrape; SERP titles only direction-finding, labeled)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (no pricing/policy claims; listicles dated + graded secondary; membership-only)
- Absence language says "not found", not "not true": **pass** ("0 of 5 captured" framed as not-captured + token-match floor; "segment exists, store didn't capture it," never "doesn't exist"; behavioral-out-of-scope framing offered as a legitimate alternative)

## Surprises

- **The store and market behavioral sets are perfectly disjoint** — not "thin overlap" but
  *zero*. I expected at least one captured `multi/none` generalist to mention a behavioral line
  (Teladoc/Amwell-style); 0 body mentions. The corpus boundary is harder than any prior run
  found.
- **The signal was decisive on the *first* two listicles**, like run 022 — a lane-scale
  selection-bias gap is even cheaper to expose than an audience-scale one (12 credits).
- **Insurer contamination (F1):** the one place a naive automated coverage-radar would have
  silently over-counted — Healthline's extractor returned 7 payers as "brands."

## Pressure tags

| Tag | Use when |
|---|---|
| `denominator-reconciliation` | The answer depends on defining / cleaning / reconciling the company or source **set**. |
| `source-rigor` | Source grade blocks confidence: snippets, weak secondary sources, missing URLs, or missing capture dates. |
| `source-panel` | A repeated external source **set** seems needed to answer this kind of question. |
| `coverage-caveat` | Store coverage, stale captures, or incomplete modules materially limit the answer. |
| `depth-backfill` | A specific field/module is missing across otherwise relevant companies. |
| `query-time-grouping-enough` | The read was answerable by grouping existing store evidence; no durable category object is needed. |
| `freshness-monitoring` | Current pricing, news, policy, regulation, or launch motion could change or materially improve the answer. |
| `relation-pressure` | Competitors, named parents, suppliers, partners, or other counterparties seem repeatedly useful. |
| `tooling-ergonomics` | Repeated manual steps suggest a helper, query recipe, or template tweak. |

Which tags fired, if any? Did this run need a new or clearer tag?

"No new primitive needed" is a valid outcome.

| Fired tag | What fired in this run | Triage implication |
|---|---|---|
| `coverage-caveat` | The read's whole point is the corpus's single largest coverage gap: an entire behavioral care modality (0/54), invisible to all store-only queries. | submit → MRL-001 (lane-/modality-scale selection-bias flavor) + capture worklist (MRL-009 shape) |
| `denominator-reconciliation` | A bounded-live panel was needed to even *see* the missing set; the store-only denominator (0) is a floor that hides a 10+-operator market segment. | submit → MRL-001 Evidence Log (selection-bias now confirmed at modality scale; 3rd sighting) |
| `source-panel` | 3rd sighting of the bounded-live external coverage-radar recipe; identical shape on a 3rd lane (GLP-1 → menopause → behavioral). | submit → MRL-002 (bounded-live coverage-radar variant; now 3 sightings — name it, don't build) |
| `source-rigor` | Listicles affiliate/SEO; only cross-source recurrence decision-grade; **insurer-contamination** in extraction is a new confound sighting (F1). | submit → MRL-008 (listicle confound + a new "platform-vs-payer extraction" flavor) |

New tag needed? **No.** Existing tags fit. The new *content* is that the selection-bias
denominator (MRL-001) now bites at **care-modality** scale, and a new extraction confound
(payers-as-brands) joins MRL-008's listicle family.

## Triage submissions

For Loop 2 to weigh (append Evidence Logs / propose; do not implement or graduate):

1. **MRL-001 (Evidence Log) — selection-bias boundary at MODALITY scale (3rd confirmation).**
   Runs 020/022 confirmed it at audience scale (women's menopause). This run confirms it at
   *care-modality* scale: the corpus holds 0 of a 5-brand cross-recurrence behavioral head and
   0 of the full union. Generalizable lesson sharpens: the selection-bias under-count is not
   only invisible to store-only queries — it scales from audience slices up to entire care
   modalities, and a single bounded-live panel exposes either cheaply (12 credits here).
2. **MRL-002 (reinforce) — bounded-live coverage-radar recipe, 3rd sighting.** The run-012
   method generalized cleanly to a 3rd, maximally-different lane. 3 sightings → the bounded-live
   variant of the read-recipe family is worth *naming* in QUERYING (a few searches + 2 JSON
   scrapes + a token diff); still **do not build a helper**.
3. **MRL-008 (Evidence Log) — a new listicle-extraction confound flavor: platforms-vs-payers.**
   Healthline's structured extract returned 7 insurance payers among the named brands; a naive
   coverage-radar would over-count the market set. The integrity guard: a "best therapy
   platforms" named-set must be filtered to *care platforms*, excluding payers/carriers, before
   the diff. Distinct from the affiliate-ordering confound (run 012).
4. **Capture-candidate worklist (Pantry / MRL-009 shape).** Tier-1 (cross-recurrence, absent):
   BetterHelp, Talkspace, Brightside Health, Doctor on Demand, MDLive. Tier-2 (single-source,
   absent): Grow Therapy, Amwell, Teladoc Health, Sesame Care, LiveHealth Online. Tier-3 (SERP
   psychiatry sub-lane, absent): Cerebral, Talkiatry, Brave Health. **Proposed only** for a
   human-gated `/research-company` campaign — NOT executed, NOT written back. Note this is a
   *scope* decision as much as a coverage gap: behavioral health may be intentionally out of
   scope, in which case the worklist is informational, not a backlog.

**Do not implement, spike, or recommend immediate graduation from inside the run.**

## Next-run advice

- **The corpus boundary is now mapped on two axes** (audience: women's menopause, run 022;
  modality: behavioral, run 024). A natural 3rd boundary probe would be a different *lane*
  again (dermatology/skincare Rx, C2 in scout.md — but that's *within* the Rx-commerce lane,
  so a smaller reach) or fertility/repro (C3). Diminishing novelty on coverage-radar repeats
  beyond ~3 sightings — the recipe is now well-evidenced; further runs should either *name* it
  (QUERYING recipe, human-gated) or pivot.
- **Highest-value follow-up is human-gated capture**, not another lab read: a `/research-company`
  pass on the Tier-1/3 worklist would convert this membership finding into captured State and
  finally give the corpus a behavioral lane — but first someone should decide whether
  behavioral health is *in scope* for this store at all (a framing call the lab can't make).
- **Avoid** re-running store-only telehealth cuts (saturated, run 021) and avoid drifting a
  coverage-radar into pricing/offer depth (the contract failure mode — did not happen here).
- If staying autonomous, the **platforms-vs-payers extraction guard** (F1) is worth carrying
  into any future listicle scrape so the named set isn't silently inflated.
