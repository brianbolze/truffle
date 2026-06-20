# Scout

## Prior Context Read

- `triage.md`: 10 items. Live pressure clusters: MRL-002 (State/Signals query recipes, P1, Acknowledged), MRL-008 (source-rigor/confound convention, P1), MRL-001 (denominator reconciliation, P2), MRL-010 (reviews/forum *bodies* as a source ingredient — 3rd sighting + first use, graduation-decision-ready, human-gated). bounded-live `review_after`-3-runs clock at **2/3**.
- `scout-context.md`: bias to **Strategist** questions, go **wide on basic archetypes not yet tried**, prefer fresh cohorts; choose `store-only` only when cached State is genuinely enough; don't let triage crowd out plain market reads.
- Last 3 completed `run-notes.md` (010 GLP-1 offer-ladder, 011 GLP-1 trust-gap reviews, 012 GLP-1 default-brand leaderboard): **all three are GLP-1**, and 011/012 were the lab's only two bounded-live runs. State-read recipe (filter cohort → latest capture → field-extract → group/label) is now well-worn on GLP-1/TRT/longevity **pricing/positioning/offer** surfaces.
- Store scoping (frontmatter grep, not an answer): sexual-health/ED is a real, **never-run** cohort — `anchor_category: sexual-health` anchors rugiet, rexmd, bluechew; hims is the origin franchise (now GLP-1 front door); keeps carries ED as a hair companion; several `multi/none` generalists also sell ED. Structural fields `pay_model`, `modality`, `compounding_posture` exist in telehealth.md frontmatter and have **not** been the load-bearing cut in any prior run (all prior cuts were `Visibility`/pricing/`access_model`/`Credibility`).

## Candidate Questions

| Question | Type | Autonomous eligible? | Evidence mode | Why this is worth a run | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|
| In the ED / sexual-health telehealth cohort, what **access & offer models** do brands use (cash-pay vs insurance, async vs hybrid, compounded vs FDA-brand, subscription vs one-off, membership wedge) and which **buyer identity** does each speak to? | mixed | yes | store-only | **Fresh cohort + fresh archetype.** First sexual-health run; first read whose load-bearing cut is the structural `pay_model`/`modality`/`compounding_posture` frontmatter rather than pricing/positioning. Tests whether those fields are populated consistently enough to support an access-map read. | Per-brand frontmatter (`pay_model`, `modality`, `compounding_posture`, `access_model`) quoted verbatim + the offer/identity claim quoted from `site_notes`. | Re-deriving structural fields from prose (the MRL-009/010 guard); a fuzzy cohort boundary (which generalists count as "ED"). |
| Who are bluechew's closest competitors / substitutes in the store, and what would distinguish a new ED entrant? | market (neighborhood) | yes | store-only | Untried **company-neighborhood** archetype on a single anchor brand; tests substitute/peer resolution from cohort cuts. | Cohort membership list + per-brand offer/price/molecule cuts. | Calling a partial store cohort the whole competitive set. |
| Across the **whole** telehealth corpus, how do access models (cash-pay / insurance / hybrid / compounded) cluster by category? | system-test | yes | store-only | Tests the access-map cut at corpus scale; would expose field-coverage gaps. | Corpus-wide frontmatter grep + coverage accounting. | Denominator sprawl; silent under-count from `anchor_category` grep (MRL-001 finding). |
| What objections / regrets show up in ED-brand reviews, and which brands answer them on owned pages? | market (trust/pain) | yes | bounded-live | Strategist trust-gap shape on a fresh cohort; would be MRL-010's **4th** sighting + push bounded-live clock to 3/3. | Trustpilot/Reddit **bodies** + owned-page rebuttal capture, dated, source-graded. | Same as 011 — sprawl past a light panel; snippet-as-evidence. |
| Who is framed as the "default" ED/sexual-health brand on third-party surfaces vs the store's universe? | market (competitor narrative) | yes | bounded-live | Repeats run 012's leaderboard shape on a new cohort — useful recurrence test but **not** a fresh archetype. | ≥2 authoritative listicles + affiliate-disclosure flags. | Re-running 012 with no new learning. |
| What's the entry offer / upsell ladder across ED brands (per-dose vs subscription vs bundle)? | market (offer packaging) | yes | store-only | Offer-ladder shape (run 010) on a new cohort; partly fresh. | `site_notes`/Visibility prose quoted verbatim per brand. | Overlaps run 010's recipe; less new than candidate 1. |

## Selected Question(s)

1. **Candidate 1** — the ED/sexual-health access & offer-model + buyer-identity map (`store-only`). Picked because it is the strongest "go wide" move on the table: a **never-run cohort** *and* a **never-run load-bearing cut** (structural access/modality/compounding frontmatter), while staying cheap and unattended-safe. It breaks three straight GLP-1 runs without spending the bounded-live clock, and it stress-tests whether the structural fields are populated well enough to carry a read — a coverage signal the pricing-only runs never produced.

Runner-up: Candidate 4 (ED trust-gap, bounded-live) — strong strategist shape and a clean MRL-010 4th sighting, but it spends the bounded-live review clock (→3/3) and re-exercises run 011's exact recipe rather than testing a new cut. Hold it for a deliberate bounded-live cycle.

## Selected Run Contract

```yaml
selected_question: "In the ED / sexual-health telehealth cohort the store has captured, what access and offer models do brands use (cash-pay vs insurance, async vs hybrid, compounded vs FDA-brand, subscription vs one-off, membership wedge), and which buyer identity does each brand speak to?"
selected_slug:          sexual-health-access-identity-map
run_type:               mixed
autonomous_eligible:    yes
evidence_mode:          store-only
expected_denominator:   "Store brands whose captured telehealth.md anchors or materially sells ED/sexual-health. Seed: anchor_category: sexual-health (rugiet, rexmd, bluechew) + origin/companion sellers (hims, keeps) + any multi/none generalist whose captured offerings include an ED line. Treat as partial; name the inclusion rule and the straddlers (generalists) rather than forcing a silent call."
likely_source_panel:    "store/<domain>/telehealth.md frontmatter (pay_model, modality, compounding_posture, access_model, anchor_category) + offerings.md + profile.md site_notes. No external sources."
allowed_sources:
  - "store/"
  - "experiments/00-market-read-lab/triage.md"
disallowed_actions:
  - "live browsing / WebSearch / Firecrawl spend"
  - "store/ mutation or write-back"
  - "creating durable categories, cohorts, or relation objects"
  - "triage graduation"
live_evidence_plan: null
approval_needed:        no
why_autonomous_safe: "Answerable entirely from cached store State (frontmatter + offerings + site_notes) plus existing lab artifacts. No outside sources, no spend, no write-back. The only judgment is the cohort boundary, which is surfaced as a named inclusion rule + straddler list, not a silent call."
loop1_failure_mode: "Re-deriving structural fields (pay_model/modality/compounding_posture) from prose instead of quoting frontmatter verbatim (MRL-009/010 guard); overstating completeness from a partial, fuzzy ED cohort denominator (MRL-001)."
```

## Selection Notes

Question-selection policy lives in `scout-context.md`. This Scout deliberately broke the three-run GLP-1 streak by moving to the store's only untouched anchor cohort (sexual-health) and to a structural access/identity cut no prior run has leaned on, while staying `store-only` to preserve the bounded-live review clock at 2/3 for a future deliberate bounded-live run.
