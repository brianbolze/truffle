# Scout

## Prior Context Read

- `triage.md`: queue is **system pressure, not a question backlog**. Open: denominator
  reconciliation (MRL-001), reusable query ergonomics (MRL-002, now P1 after run 004),
  in-cohort module gaps (MRL-003), named-counterparty edge + capture grain (MRL-005/006),
  category-scoped exogenous signals (MRL-007), minimal-monitor source rigor (MRL-008),
  standard "write-back candidates" section (MRL-009). All held for recurrence; none graduated.
- `scout-context.md`: lead with **plain operator questions**, system lesson second. Go wide
  on archetypes before narrow recurrence probes. Prefer store-only + autonomous-safe for
  unattended Loop 1.
- Last 3 completed `run-notes.md`:
  - **Run 002 (GLP-1 news monitoring):** external panel load-bearing for *event/freshness*
    questions, but snippets are leads, not evidence; reputation/forum reads need primary URLs.
  - **Run 004 (category crowdedness):** store-only; GLP-1 most crowded front door (19/53),
    GLP-1 bolt-on everywhere (22/53). Third sighting of the denominator/query-ergonomics
    pressure → MRL-002 to P1.
  - (Run 003 was an abandoned Scout slate, same slug; mined as hypothesis, not copied.)
- **Store census (today): 126 profiles, 54 `telehealth.md`, 66 `offerings.md`, 44 `visual.md`,
  49 `signals/` dirs.** Signal source-types captured: wayback (47), trustpilot (20),
  sec_edgar (20), trends (5), serpapi (2), exa_similar (2), ads_transparency (1).
- **Key gap I see:** every prior run (000-004) read only **State** (`telehealth.md` /
  `offerings.md` / `profile.md`). The **Signals** layer (Trustpilot, Wayback, SEC) and the
  **visual** layer are captured for dozens of companies and **completely unexercised by any
  market read.** Reputation was always parked as `live-external-needs-approval` — but
  Trustpilot/Wayback are already captured locally, which turns several of those archetypes
  into clean store-only reads. That is where the freshest both-useful-and-system-testing
  question lives.

## Candidate Questions

Wide slate; the recommended pick is the first reputation row (it opens an unexercised layer).

| Question | Type | autonomous_eligible | evidence_mode | Why this is worth a run | Trustworthy evidence would require | Failure mode to watch |
|---|---|---:|---|---|---|---|
| Across the captured brands with Trustpilot signals, what's the reputation landscape — who's trusted vs distrusted, and how concentrated is the bad sentiment? | market | yes | store-only | Canonical reputation archetype prior runs could only do live-external — but Trustpilot is **already captured for 20 brands**. First read to exercise the Signals layer; tests whether captured signals are query-ready and whether reputation is a State/Signal/Judgment boundary case. | The 20 `signals/trustpilot/*.json` (trust_score, review_count, rating_distribution, profile_flags); latest capture per brand; flag paid/claimed profiles as a confound. | Treating Trustpilot score as ground-truth quality (selection + paid-profile bias); comparing brands with 8k reviews to ones with 30; ignoring capture date. |
| Using captured Wayback signals, which brands are long-tenured vs recently-launched, and does tenure track category? | market | yes | store-only | Tenure/maturity is a real investor question; Wayback is captured for 47 brands. Tests whether the Signals layer supports an "establishment" read and exercises wayback grain. | `signals/wayback/*` first-seen timestamps per brand; join to `anchor_category`; explicit "Wayback first-capture ≠ founding date" caveat. | Reading Wayback first-snapshot as founding date; page-level vs domain-level tenure confusion. |
| Across the 44 captured `visual.md` layers, what brand/design postures recur (premium-clinical vs consumer-friendly vs budget) and does posture track category or price tier? | market | yes | store-only | Opens the **visual** layer, also unexercised. Useful brand-positioning read; tests whether visual evidence is query-aggregatable without a score (the layer deliberately emits no ranking). | `store/*/visual.md` impression + cards; join to category/price; respect the "no score/ranking" contract — group impressions, don't rank. | Inventing a quality score the layer refuses to emit; over-reading one impression line per brand. |
| Generalize Run 000: across all captured cash-pay categories, which are most price-transparent vs most intake-gated? | mixed | yes | store-only | High reuse pressure — proves whether `Visibility` works cross-category, not a GLP-1 fluke. | Per-category denominators; `offerings.md` `Visibility` tokens; brand- and SKU-weighted cuts. | Re-running GLP-1 narrowly; conflating not-priced-by-brand with hidden. |
| Do brands with captured SEC EDGAR signals (public/filing) differ in pricing transparency or offer breadth from private DTC peers? | mixed | yes | store-only | Joins Signals (sec_edgar, 20 brands) to State (offerings) — a structure question about whether public-market presence correlates with offer posture. | `signals/sec_edgar/*` presence; join to offerings breadth + visibility; tiny-N caveat. | Over-reading a 20-brand, presence-only signal as causal; conflating "has EDGAR signal" with "is public." |
| Which parent companies/platforms operate multiple front-door brands across health categories (rollups hiding behind storefronts)? | market | yes | store-only | Basic market-structure read on proven fields (`parent`/`owns`). | `profile.md` `parent`/`owns` frontmatter; per-brand category tags. | Collapsing distinct brand strategies into one parent-competitor. |
| Who are Hims & Hers' closest true competitors vs adjacent peers across its category footprint? | market | yes | store-only | Clean company-neighborhood archetype on the store's most multi-category brand. Note: Trustpilot `people_also_looked_at` is a *captured* competitor-adjacency signal worth testing here. | Hims profile/offerings/telehealth + comparable brands; explicit true-substitute vs adjacent criteria; the captured `people_also_looked_at` list as one input. | Generic "other telehealth brands" list; treating category overlap as substitutability. |
| What changed recently across major model providers (Claude / OpenAI / Google) this week? | market | no | live-external-needs-approval | Pure current-change-watch archetype; deliberate non-store freshness test. | Approval; official provider pages first; exact URLs, dates, source type. | Answering from stale memory/snippets. |
| What do customers complain about most in GLP-1 / men's-health telehealth (price, access, side effects, support, refills, cancellation)? | market | no | live-external-needs-approval | Reputation/pain archetype at the *review-text* grain — deeper than captured Trustpilot aggregates. | Approval for live review/forum research; defined panel; exact URLs + dates; coded complaint sample. | Treating samples as representative; unattributed snippets. |
| Re-test Run 000's 33/42/25 GLP-1 visibility split against current store captures — has it drifted? | system-test | yes | store-only | Cheap reproducibility probe Run 002 recommended. | Same GLP-1 roster + `Visibility` tokens; diff vs Run 000 receipt. | Re-deriving the denominator differently and blaming drift. |

## Selected Question(s)

1. **Across the captured brands with Trustpilot signals, what's the reputation landscape —
   who's trusted vs distrusted, and how concentrated is the bad sentiment?** — recommended
   for Loop 1.
2. Wayback tenure read (which brands are long-tenured vs recently-launched) — strong store-only
   alternative that also opens the Signals layer.

Recommendation rationale below; the contract selects #1.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: "Across the captured brands with Trustpilot signals, what is the reputation landscape — which brands are trusted vs distrusted, how concentrated is negative sentiment, and what does the captured Trustpilot signal reliably support vs not?"
run_type: market
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: "The 20 brands with a captured store/<domain>/signals/trustpilot/*.json (agelessrx-com, defymedical-com, directmeds-com, eden-health, getpetermd-com, gogeviti-com, hims-com, honehealth-com, hydramed-com, joinamble-com, joinfridays-com, marekhealth-com, maximustribe-com, mylifeforce-com, niagenplus-com, sermorelin-com, struthealth-com, trtnation-com, truniagen-com, waldo-fyi). Use the latest capture per brand. This is a captured-signal floor, NOT the full store and NOT a market census; brands without a Trustpilot capture are 'not captured', not 'no reputation'."
likely_source_panel: "None external. Internal store only: store/*/signals/trustpilot/<captured_at>.json (trust_score, review_count, reviews_last_12m, rating_distribution, profile_flags, profile_state, people_also_looked_at). Join to store/*/profile.md or telehealth.md frontmatter (anchor_category, value_chain_role) for category context. scripts/store.py only if name reconciliation is needed."
allowed_sources:
  - store/*/signals/trustpilot/
  - store/*/profile.md
  - store/*/telehealth.md
  - scripts/store.py
  - SIGNALS.md
  - QUERYING.md
disallowed_actions:
  - live browsing / WebSearch / Firecrawl scrape or crawl (no spend; do NOT re-capture Trustpilot)
  - writing to store/
  - creating durable category/cohort/signal primitives or other engine objects
  - writing back to Notion or any project KB
  - filling read.md / review files / triage.md beyond Loop 1's own read.md
approval_needed: no
why_autonomous_safe: "Answerable entirely from already-captured local signal JSON in store/. No live spend, no re-capture, no external claims, no primitive creation. The Trustpilot capture date is already in each file, so freshness is auditable without browsing. Exercises the previously-untouched Signals layer and the reputation archetype that prior runs had to park as live-external — now store-answerable."
loop1_failure_mode: "Treating Trustpilot trust_score as objective product quality rather than a self-selected, paid-profile-influenced sentiment signal (hims is paid_profile + asks_for_reviews + claimed — a confound to surface, not hide). Also: comparing brands with thousands of reviews against brands with a handful as if equivalent; ignoring per-file capture_at; and stating absence as 'no reputation' rather than 'not captured'. Mitigation: report review_count alongside every score, flag profile_flags confounds, weight confidence by volume, and label every cross-brand comparison as a captured-signal read, not a market verdict. Keep score = Signal, trusted/distrusted ranking = clearly-labeled Judgment tied back to the signal."
```

## Selection Notes

Decision leverage + system-test value pick #1: reputation is one of the most-recognized
operator/investor questions, and it's the **first chance to exercise the Signals layer** —
captured for dozens of companies but read by zero prior runs. It directly pressures the
State/Signals/Judgment boundary (a trust_score is a Signal; "who's trusted" is a Judgment),
which is exactly the open edge the engine docs flag. It's also the cleanest store-only version
of an archetype prior runs could only mark `live-external-needs-approval`, so it tests whether
the signal-capture investment actually pays off at read time.

#2 (Wayback tenure) is held as the alternative because it opens the same layer with a different
signal grain; reputation is the higher-leverage, more operator-recognizable read.

The two live-external candidates (model-provider change-watch, review-text complaint mining) stay
on the slate to keep the freshness/reputation-depth archetypes visible, but both are
`approval_needed` and must not run unattended.

Prior-run pressure treated as hypothesis, not default: this run will test whether MRL-007/008
(signals grain + source-rigor for monitoring) recur once a read actually consumes captured
signals — and whether reputation needs anything new or is just query-time grouping over existing
Signals.
