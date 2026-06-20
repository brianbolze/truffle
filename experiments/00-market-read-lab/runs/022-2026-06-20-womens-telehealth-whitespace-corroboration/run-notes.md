# Run Notes

```yaml
run_status: reviewed
evidence_mode: bounded-live
autonomous_eligible: yes
termination_reason: completed
pressure_lenses_fired: [denominator-reconciliation, source-panel, coverage-caveat, source-rigor]
```

> **Loop 2 outcome (2026-06-20):** Reviewed via a 3-pass adversarial workflow (evidence
> verifier + consumer + developer, Sonnet). **Verifier: PASS-WITH-FIXES** — independently
> reproduced all three load-bearing counts (store women-leaning **5** via grep; the
> **9**-brand cross-source intersection; **8 of 9 absent** via store token-match; Wisp
> `all-genders` confirmed) with zero substantive discrepancies. One fix: the 9-brand
> intersection is 7 exact-string matches + 2 name-variant matches (Allara/Allara Health;
> HerMD/HerMD Health) — the normalization step was implicit; now stated in the receipt's
> Method. State/bounded-live/Judgment boundary clean; absence language disciplined;
> membership-vs-size discipline held; bounded-live contract followed without violation.
> **Consumer: valuable (yes)** — converts run 020's store-only hypothesis into a dated,
> cited finding + an actionable tiered capture worklist; the store reconciliation is the
> Truffle-specific value generic Claude+web can't produce; biggest limit is 2 affiliate
> listicles + membership-only. **Developer: submit-candidate** — appended Evidence Logs to
> **MRL-001** (selection-bias flavor now *live-confirmed*; two-flavors-two-tools rule
> hardened — clock moves toward first-class-guardrail, not graduation), **MRL-002** (2nd
> sighting of the bounded-live external coverage-radar recipe — named, not built), **MRL-009**
> (concrete tiered capture worklist), and a new **MRL-013** watch (`menopause/HRT` as a
> first-class `anchor_category` — held behind capture confirmation). No graduation; no
> `store/` mutation; no `Human Notes` touched. Receipt normalization fix applied.

## 30-second operator read

- **Did the run work?** Yes — and it's the most decisive bounded-live result in the lab so
  far. The 3rd bounded-live run (after 011/012), 14 Firecrawl credits. It **converted run
  020's store-only selection-bias *hypothesis* into a market-grounded *finding***: a
  dedicated women's-menopause/HRT telehealth segment plainly exists (Midi, Winona, Evernow,
  Gennev, Stella, HerMD, Allara, + Alloy/Elektra/Pandia) and the store has captured ~none
  of it. 8 of 9 cross-source-recurrence brands are absent; the 1 present (Wisp) is captured
  `all-genders`.
- **What was awkward?** Nothing mechanical. The discipline is keeping it a **membership**
  read — who exists / who's captured — and *not* drifting into pricing/offer depth (the
  stated failure mode) or reading 2 affiliate listicles as a market census. Stop rule fired
  cleanly once the store-vs-market diff was computable.
- **What should the next agent know?** This is the cleanest proof that MRL-001's two
  denominator flavors are genuinely different: the **anchored-only under-count** is
  query-time fixable; the **selection-bias under-count** (run 020) is invisible to *every*
  store-only query and needs outside evidence or new capture. Bounded-live is the right —
  and only — tool for it. Concrete output: a tiered capture-candidate worklist (Pantry /
  MRL-009 shape). **No new primitive built; no store mutation; no write-back.**

## What happened

Confirmed the store side with `grep -rlE "^audience: *women" store/*/telehealth.md` → 5
women-leaning brands of 54. Ran 2 firecrawl_search queries (best menopause/HRT telehealth),
which surfaced two authoritative listicles + direct brand SERP results. Scraped the two
listicles (Everyday Health 17 / Flow Space 15) with a JSON schema to pull verbatim named
sets, took the cross-source intersection (9), and reconciled it against the store by token
match. Wrote `read.md` + one source-panel receipt. 14 credits; no crawl, no `store/`
mutation, no write-back.

## Inputs and scope

- **Store side (S3):** 54 `store/*/telehealth.md`; the 5 `audience: women*` packs; token
  match of the 9 cross-recurrence names against `store/*/`.
- **External panel:** Everyday Health "17 Best Online Menopause… 2026" (S1); Flow Space
  "15 Telehealth Companies… 2026" (S2); 2 SERP queries (S4, direction-finding).
- **Exclusions:** pricing/offer depth (out of scope by contract — membership read only);
  demand/size evidence; any non-menopause women's category beyond what the listicles named;
  brand owned-page deep reads (the stop rule fired before they were needed).
- **Receipt:** `receipts/womens-menopause-panel-2026-06-20.md` (S1–S4; C1–C5).

## Live evidence plan

Required only for `bounded-live`; leave `null` for `store-only` and `local-existing`.

```yaml
live_evidence_plan:
  approved_by: Brian
  approval_scope: autonomous Market Read Lab runs
  budget_class: light
  review_after: 3 bounded-live runs   # this IS the 3rd (after 011, 012) — review checkpoint
  evidence_goal: >-
    Determine whether dedicated women-anchored hormone/menopause/longevity telehealth brands
    exist in the market that the store has not captured (confirming run 020's selection-bias
    hypothesis) vs genuinely thin supply. Produce a tiered capture-candidate list and a clear
    coverage-vs-market statement on run 020's 15-vs-5 asymmetry.
  source_families_allowed: [SERP/listicle, owned/official brand pages, reviews/forums (light)]
  source_families_preferred: [authoritative "best women's menopause/HRT 2026" listicles, owned brand pages]
  source_families_disallowed: [login-only/paywalled, broad crawling, private data, ad/social scraping]
  stop_when:
    - ">=2 authoritative listicles yield a cross-recurrence named set and the store diff is computable with caveats"  # FIRED
    - the next source would expand the question (pricing/offer depth) rather than verify membership
    - remaining uncertainty is a framing judgment, not a sourcing gap
  disallowed_actions: [write-back to store/, code/schema/template changes, durable primitive creation, triage graduation]
```

## Live evidence used

Required for every outside source used in `bounded-live`. Leave `[]` for local-only runs.

```yaml
live_evidence_used:
  - source_or_query: "best menopause telehealth companies 2026"
    source_family: SERP/listicle
    action_taken: searched
    reason: discover authoritative listicles + confirm head brands surface as direct brand results
    source_grade: direction-finding
    captured_at: 2026-06-20
    spend_note: paid-credit   # 2 credits
    claim_ids_supported: [C5]
  - source_or_query: "best online menopause and women's hormone (HRT) telehealth platforms 2025"
    source_family: SERP/listicle
    action_taken: searched
    reason: second SERP angle to corroborate the brand set (Winona/Evernow/Gennev/Alloy)
    source_grade: direction-finding
    captured_at: 2026-06-20
    spend_note: paid-credit   # 2 credits
    claim_ids_supported: [C5]
  - source_or_query: https://www.everydayhealth.com/services/online-menopause-treatment/
    source_family: SERP/listicle (affiliate/SEO)
    action_taken: scraped
    reason: extract verbatim named set (17) for one authoritative listicle
    source_grade: secondary
    captured_at: 2026-06-20
    spend_note: paid-credit   # 5 credits
    claim_ids_supported: [C1, C3]
  - source_or_query: https://www.theflowspace.com/reproductive-health/menopause/online-menopause-treatment-2941951/
    source_family: SERP/listicle (women's media)
    action_taken: scraped
    reason: second authoritative listicle (15) for cross-source recurrence
    source_grade: secondary
    captured_at: 2026-06-20   # page modified 2026-04-27
    spend_note: paid-credit   # 5 credits
    claim_ids_supported: [C2, C3]
# Total spend: 14 Firecrawl credits. Stop rule fired after the diff was computable;
# no owned-page deep reads or third listicle were needed.
```

## Friction log

- **No mechanical friction.** The store-side grep is one line; the named-set extraction is
  two JSON scrapes. The only judgment work is the membership discipline (don't drift into
  pricing; don't read 2 affiliate lists as a census) — handled by the contract's stop rule.
- A reusable "external coverage-radar" recipe is now sighted twice (run 012 GLP-1, run 022
  menopause): SERP → ≥2 authoritative listicles → JSON-extract named sets → cross-source
  intersection → token-match store diff. Candidate for the MRL-002 family (a *bounded-live*
  variant), not built here.

## Evidence limits

- **Membership, not size.** "Store-absent segment" = real + uncaptured, NOT large. No
  demand/share/revenue claim is made.
- **2 listicles = coverage radar, not census** (run 012). Both monetize referrals; only the
  cross-source-recurrence head is a strong signal; the tail is affiliate-confounded.
- **Token-match reconciliation** could miss a renamed/parent domain. Manual `ls store/*/`
  scan found no extra hits, but this is "not found by token match," not "proven absent."
- **Brand audience framing** read from listicle descriptions + SERP, not a captured
  `audience` field — a capture run is needed to confirm each brand's front door.
- **Capture dates:** all external sources 2026-06-20; the Flow Space page was last modified
  2026-04-27 (carried in the receipt).

## Loop 1 exit check

Record `pass` / `fail` for the mandatory exit check before setting final `run_status`.

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`: **pass** (planned bounded-live)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` was present and followed: **pass** (plan present; stayed in allowed source families; stop rule fired before owned-page drift)
- If `bounded-live`, every outside source was logged in `live_evidence_used`: **pass** (4 sources: 2 searches + 2 scrapes)
- If `bounded-live`, stop rules and spend notes were recorded: **pass** (14 credits itemized; stop rule "diff computable" fired)
- No disallowed action happened: **pass** (no crawl, no `store/` mutation, no write-back, no durable primitive, no triage graduation)
- Required citations / receipts present and source-graded: **pass** (S1–S4 graded; receipt present)
- No snippet treated as evidence: **pass** (named sets from full list pages via JSON scrape; SERP titles used only as direction-finding corroboration, labeled)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (no pricing/policy claims made; listicles dated 2026-06-20, graded secondary; membership-only read)
- Absence language says "not found", not "not true": **pass** ("8 of 9 absent from store" framed as not-captured + token-match limit; no "doesn't exist" claim; store women-leaning 5 framed as a floor)

## Surprises

- **The store's women-leaning supply and the market's are almost disjoint by *category*,
  not just by brand.** I expected overlap (some store brands on the listicles). Instead the
  store's 5 women-leaning brands are 3/5 GLP-1 weight-loss, while the market's women-anchored
  supply the store misses is a *menopause/HRT* segment — two different lanes. Run 020's
  store-only read concluded "GLP-1 is where women-anchored brands exist"; that was a pure
  coverage artifact. The real women-anchored density is in menopause, which the store
  barely resolves (`womens-HRT = 1` cell = `innerbalance` alone).
- **The signal was decisive on the *first* two listicles** — no need for a third source or
  any owned-page read. A selection-bias gap this large is cheap to expose (14 credits).

## Pressure tags

Short `kebab-case` tags for system pressure this run exposed. These are recurrence handles, not a fixed taxonomy and not permission to build.

Use an existing tag when it fits; coin a narrow tag only when the guide misses the thing.

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
| `denominator-reconciliation` | The load-bearing event: a bounded-live external panel **confirmed and operationalized** MRL-001's run-020 *selection-bias* denominator flavor — the store's women-leaning cohort (5) is non-representative, and the missing segment is *nameable* (dedicated menopause/HRT specialists). First time the lab converted the selection-bias hypothesis into a finding + a capture worklist. | submit → MRL-001 Evidence Log (selection-bias flavor is now *live-confirmed*, not just hypothesized; bounded-live is its only resolution path) |
| `source-panel` | Second sighting of the **external coverage-radar recipe** (run 012 GLP-1 → run 022 menopause): SERP → ≥2 authoritative listicles → JSON-extract named sets → cross-source intersection → store token-diff. The cross-recurrence rule and affiliate-confound caveat held identically on a new category. | submit → MRL-002 (a *bounded-live* variant of the read-recipe family; 2 sightings — name it, don't build it) |
| `coverage-caveat` | The run's whole point is a coverage gap: dedicated women's-menopause/HRT is the store's single largest audience whitespace; `womens-HRT` is a 1-brand cell hiding a 10+-operator segment. | submit → capture-candidate worklist (Pantry / MRL-009 shape); MRL-003-adjacent depth-backfill |
| `source-rigor` | Listicles are affiliate/SEO; only cross-source recurrence is decision-grade; SERP titles kept as direction-finding. State/external-evidence/Judgment kept separable throughout. | no-op — reinforces MRL-008's listicle-inclusion-confound flavor (run 012); discipline held |

New tag needed? **No.** Existing tags fit. The new *content* is that bounded-live is the
**only** resolution path for a selection-bias denominator — a sharpening of MRL-001, not a
new tag.

## Triage submissions

For Loop 2 to weigh (append Evidence Logs / propose; do not implement or graduate):

1. **MRL-001 (Evidence Log) — selection-bias flavor is now LIVE-CONFIRMED.** Prior MRL-001
   entries logged the selection-bias denominator as a *hypothesis* (run 020, store-only,
   explicitly couldn't test it). This run tested it with a 14-credit bounded-live panel and
   confirmed it: 8 of 9 cross-recurrence menopause brands absent; store women-leaning set
   nearly disjoint from the market menopause set. The generalizable lesson: the two MRL-001
   flavors need **different tools** — the anchored-only under-count is query-time fixable; a
   selection-bias under-count is invisible to all store-only queries and needs outside
   evidence or new capture. A future QUERYING/whitespace recipe must say so.
2. **MRL-002 (reinforce) — bounded-live external coverage-radar recipe, 2nd sighting.** The
   run-012 method generalized cleanly to a new category. This is a *bounded-live* member of
   the read-recipe family (distinct from the store-only State-read surfaces). 2 sightings →
   name the recipe shape; do not build a helper.
3. **Capture-candidate worklist (Pantry / MRL-009 shape; relates to MRL-003 depth-backfill).**
   Tier-1 (cross-recurrence, not in store): Midi Health, Winona, Evernow, Gennev, Stella,
   HerMD, Allara. Tier-2 (strong single-source + SERP-confirmed): Alloy, Elektra Health,
   Pandia Health. This is a **proposed** worklist for a human-gated `/research-company`
   campaign — NOT a write-back, NOT executed here. Capturing it would let run 020's grid be
   recomputed honestly.
4. **Watch — `menopause/HRT` as a first-class `anchor_category` value.** Run 020's grid has
   `womens-HRT = 1`; the panel implies a 10+-operator category. One sighting; do **not**
   graduate a taxonomy value — revisit if the tier-1 capture run confirms the density.

**Do not implement, spike, or recommend immediate graduation from inside the run.**

## Next-run advice

- **The highest-value follow-up is a human-gated capture-first run** of the tier-1
  candidates (`/research-company` on Midi/Winona/Evernow/Gennev/Stella/HerMD/Allara). That
  converts this membership finding into captured State and *also* gives the lab the
  "second cohort with real depth" that runs 020/021 said was the other under-tested
  direction — killing two birds. It needs approval (Firecrawl spend) so it is **not**
  autonomous.
- **Operator checkpoint:** this is the **3rd bounded-live run** (011/012/022) — the
  `review_after: 3` point in the standing plan. Worth a human glance at all three together
  to decide whether to tighten the bounded-live contract. All three stayed light
  (5/?/14 credits) and stopped on their stop rules; no scope drift observed.
- **Avoid** re-running another store-only telehealth cohort cut (saturated — see run 021).
  If staying autonomous, the men's-side confirmatory mirror (C6 in scout.md) or a second
  bounded-live whitespace category would extend the coverage-radar recipe's evidence; the
  capture-first run above is higher value but needs approval.
