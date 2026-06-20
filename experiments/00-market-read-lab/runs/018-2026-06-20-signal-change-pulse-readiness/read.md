# Market Read

## Question

Across the captured telehealth store, which brands' signals show a **detectable change between their two-or-more captures** (Trustpilot review velocity, SEC/Form-D funding footprint, SERP visibility), and what does this first temporal/diff read teach about whether the store can support a **"trust the cache over time" / change-pulse** read **store-only** today?

## Direct Answer

**The store can answer a change-pulse read today on two signal types (Trustpilot review-velocity and Wayback archive-presence) across ~13 domains — but every readable delta is a *noisy proxy* for the change a consumer actually wants, not the decision-grade change itself.** This is the lab's first temporal/diff read (all 18 prior runs were point-in-time), and the honest verdict is: **the append-only signals layer + `signal_delta.py` are the right shape — no new primitive is needed — but change-pulse readiness is bounded by capture *cadence matched to each signal's own refresh rate*, plus the same MRL-008 confound discipline carried onto the temporal axis — not by schema.** (Judgment, from C1–C9.)

> **Loop 2 correction (folded in):** the first pass of this read swept only company-grain signal dirs (`store/<domain>/signals/<type>/*.json`) and **silently missed Wayback entirely**, because Wayback is captured one level deeper at *page* grain (`signals/wayback/<page-slug>/*.json`). The adversarial evidence verifier caught it. Wayback has a working delta branch and 15 page-subjects with ≥2 captures across 10 domains; including it both adds a second answerable source and confirms the distinct-domain count is 13 (the original "~13" was loosely right, but for the wrong reason). The corrected read is below.

Concretely, running `signal_delta.py` first-vs-last over every store directory with ≥2 captures, across all four signal types:

- **Trustpilot review velocity — answerable, with a heavy caveat.** 6 brands yield a clean per-day review-count velocity over a real ~6.5-day gap: honehealth (+66, 10.0/day), hims (+54, 8.7/day), joinamble (+51, 7.8/day), agelessrx (+17, 2.6/day), joinfridays (+13, 2.0/day), maximustribe (+7, 1.1/day). (State/Signal, C2.) **But every one carries `paid_profile`** — velocity measures review-*solicitation* cadence, not organic sentiment — and the only metric that diffs cleanly is cumulative `review_count`; `reviews_last_12m` returns `delta: null` by design (rolling window) and `trust_score` is level-only. So the delta-able number is the one a buyer cares about least. (Judgment, C3/C7.)
- **Trustpilot — 3 of 9 pairs void.** eden-health (subject realigned to tryeden-com → unpaired), hydramed (profile empty between captures), sermorelin (D0 capture not ok). The tool **vetoes rather than silently skipping** — the disagreement is itself the signal. (State, C4.)
- **Wayback page-archive — answerable but almost entirely flat, and the flatness is the lesson.** 15 page-subjects across 10 domains diff cleanly (working delta branch: `archive_presence`, `snapshot_count`, `content_digest`, `last_seen`). **13 of 15 show delta=0** — identical snapshot count, identical content digest — because the captures are days apart while the *archive itself* only re-crawls on Wayback's own (≈monthly) cadence, so a day/week-spaced re-capture reads the same archive state. The metric measures "has Wayback re-crawled this page," not "did the brand change the page." Two exceptions: honehealth `mens/sermorelin` went `archive_presence False→True` / `snapshot_count 0→1` (a page entering the archive — a real, coarse detectable change), and **onemedical root showed `snapshot_count 2517→2516` (delta −1) with `last_seen` moving *backwards* (2026-06-15→2026-06-09)** — impossible for a monotone archive, i.e. a **CDX API nondeterminism confound**, not a real loss. (State/Signal C8; confound = Judgment C9.)
- **SEC/Form-D funding footprint — not answerable.** All 4 pairs return `no source-aware delta for 'sec_edgar' — add a branch or compare by hand`: the comparator has no sec_edgar delta branch, and the captures are intra-day anyway (no funding-window change to read). (State, C5.)
- **SERP visibility — not answerable.** Each `serpapi/` directory holds captures of *different query subjects*, so every subject has only one capture → unpaired, level-read only. There is no repeat capture of the same query to diff. (State, C6.)

**Net for the freshness pillar:** "trust the cache over time" is operable *today* on two surfaces — Trustpilot review-velocity (~6 brands) and Wayback archive-presence (~10 domains) — but **both readable deltas are proxies confounded by capture/source mechanics** (solicitation cadence; archive re-crawl cadence; CDX flakiness), not the sentiment-trend or page-content change a consumer would act on. The fixes are all *outside* the schema: **capture each subject on a cadence matched to its own refresh rate** (re-capturing Wayback weekly is near-useless when the archive refreshes monthly; Trustpilot counts move daily), a small `sec_edgar` diff branch, and carrying MRL-008's confound-sibling discipline onto the temporal axis (the onemedical −1 must read as "API artifact," not "lost snapshot"). **No new change/diff primitive is needed.** (Judgment.)

## Evidence Used

All evidence is local and derived from already-captured signal envelopes; see `receipts/signal-delta-sweep-2026-06-20.md` (claims C1–C9). No external fetch, no spend.

- **C1** — denominator: 135 domains, 49 with `signals/`, **13 distinct domains** with ≥2 captures in some source_type — trustpilot ×9 (company-grain), sec_edgar ×4, serpapi ×2, **wayback ×15 page-subjects across 10 domains (page-grain, one level deeper)**. Distinct union = 13 (wayback adds onemedical, struthealth beyond the other three types' 11).
- **C2** — 6 clean Trustpilot velocity deltas (table above), gap 6.2–6.6 days.
- **C3** — only `review_count` diffs; `reviews_last_12m` delta=null (rolling), `trust_score` level-only.
- **C4** — 3 Trustpilot vetoes (subject realignment / empty-between / D0-not-ok).
- **C5** — SEC: no delta branch + intra-day captures.
- **C6** — SERP: one-capture-per-query (unpaired).
- **C7** — every clean velocity carries `paid_profile`.
- **C8** — Wayback: 15 page-subjects diff cleanly (working branch); 13/15 delta=0 (archive static between captures); honehealth mens/sermorelin `archive_presence False→True`; the only non-trivial moves are archive-state, not page-content.
- **C9** — Wayback confound: onemedical `snapshot_count 2517→2516` (−1) with `last_seen` moving backwards = CDX API nondeterminism, must not read as a real lost snapshot.

## Companies Seen

Trustpilot ≥2-capture: agelessrx, eden-health, hims, honehealth, hydramed, joinamble, joinfridays, maximustribe, sermorelin. SEC ≥2-capture: hims, honehealth, maximustribe, waldo. SERP ≥2-capture: niagenplus, waldo. Wayback ≥2-capture (page-grain): agelessrx, eden-health, hims, honehealth, hydramed, joinamble, maximustribe, niagenplus, onemedical, struthealth. (**13 distinct domains**; 6 produced a usable Trustpilot velocity delta, 1 a real Wayback archive-presence change, the rest flat or unsupported.)

## Missing / Stale Coverage

- **86 of 135 domains have no `signals/` at all**, and only 13 have a second capture — the temporal substrate exists for a thin slice, not the corpus.
- Repeat-captures exist for SEC, SERP and Wayback but are **mis-matched to each signal's refresh rate**: SEC pairs are intra-day; SERP "pairs" are different queries, not repeats; Wayback re-captures are days apart while the archive re-crawls ~monthly, so 13/15 read delta=0. The cadence-vs-refresh-rate mismatch, not the coverage count, is what's missing.

## Source Gaps

- No `sec_edgar` delta branch in `signal_delta.py` — SEC change must be hand-compared today (the tool correctly vetoes rather than guessing).
- Trustpilot `trust_score` and review *bodies* (the decision-grade sentiment surface, cf. MRL-010) are not delta-tracked; only cumulative counts are. The temporal read inherits MRL-008's "headline metric misleads without its confound sibling" exactly — and Wayback's onemedical −1 (C9) is a second, source-mechanics flavor of the same confound family.
- Wayback's delta surface is archive-state (`snapshot_count`/`archive_presence`), a proxy for "did the archiver re-crawl," not "did the brand change the page" — the page-content change a freshness consumer wants is not what this signal moves on.

## External Completeness Check

N/A — completeness here is internal and temporal ("which on-disk subjects have ≥2 comparable captures"), not market membership, so there is no outside denominator to check against.

## Market Pattern

Among the 6 brands with readable velocity, raw review-acquisition rate spreads ~10× (honehealth ~10/day vs maximustribe ~1/day), tracking brand size/solicitation intensity rather than any momentum story — and on `paid_profile` profiles this is a *marketing-cadence* reading, not a market-demand reading. **No market conclusion is drawn from it**; the run's payload is the readiness verdict, not a growth ranking. Treating "+66 reviews, growing fast" as a demand signal would be the headline false-confidence trap this run exists to flag.

## What Would Change This Answer

- **A capture cadence matched to each signal's own refresh rate** — the same subject (trustpilot profile, SERP query, SEC issuer, Wayback page) re-captured on a schedule tuned to how fast that source actually moves — would widen the denominator from ~6 brands/one metric to a genuine cross-cohort change-pulse read. Tuning matters: Trustpilot counts move daily (a weekly gap is fine), but Wayback re-crawls ~monthly (a weekly re-capture mostly yields delta=0, as 13/15 here did). This is the single highest-leverage change and it is an *ops* change, not a build.
- **A `sec_edgar` delta branch** would turn 4 vetoes into Form-D footprint deltas (new filings between captures), the funding-pulse the store can't read today. This is ~one function, not an ops decision.
- **Pinning subject-identity at capture time** (a canonical query string for SERP, a canonical issuer for SEC) would fix the SERP unpaired problem — which is *not* a cadence gap but a capture-contract one: a second SERP capture was taken, just of a *different query*, so there's nothing to pair. "Same domain + same source_type" does not guarantee a diffable pair.
- **The 6 clean-velocity Trustpilot brands** (honehealth, hims, joinamble, agelessrx, joinfridays, maximustribe) are the concrete starting list for any cadence re-capture trial — they already have a working second capture and a real gap.
- **Delta-tracking a decision-grade Trustpilot surface** (score trend, or bodies/objection-mix per MRL-010) would fix the "only the least-relevant metric diffs" problem — but that is a graduation decision for the human steward, not this run's to make.
