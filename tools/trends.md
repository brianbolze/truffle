# trends.py — Google Trends (pytrends) branded-interest capture

Give it a **list of keywords**; it captures each one's Google Trends interest-over-time series in
its **own single-keyword call**, sequentially, and emits one envelope with a per-keyword `series`
payload. Parsed JSON to stdout — no store write, no cohort, no vertical baked in. The caller decides
which names to capture, which to disambiguate, and where the result lands.

```bash
python3 tools/trends.py "Hone Health" "AgelessRx" "Lifeforce"
python3 tools/trends.py "Hims & Hers::Hims"                       # clean label, disambiguated query
python3 tools/trends.py "Eden::Eden hormone therapy" "Ro::ro.co"  # collision / too-short overrides
python3 tools/trends.py "Hone Health" --geo US --timeframe "today 12-m" --sleep 8
```

**No API key.** pytrends is the *unofficial, unauthed* Google Trends client. Free, unmetered — and
unsupported (see gotchas).

## Why this tool owns the loop (it's the one that does)

serpapi and exa take one input per call and leave looping to the caller. `trends.py` is deliberately
the opposite: **it takes the whole keyword list and runs the loop itself.** The value here isn't the
single call — it's the *capture shape across the list*: solo-per-brand normalization + sequential
rate-limit management (sleeps, a 429 retry). Hand that to the caller and every consumer re-derives
the same gotchas. So the loop lives in the tool; per-keyword results come back in one envelope.

The optional `{label, query}` shape rides the `::` seam: a plain keyword is both label and query;
`Label::query` keeps a clean display label while overriding the query string. That's the *only*
caller-judgment knob — **which** names collide and need an override (or a skip) is the caller's
call, not the tool's. The tool captures what each side resolves to and surfaces the raw signal.

## What it does now vs. what it could grow into

**Now — `interest_over_time`, solo-per-brand, one timeframe.** Per-keyword series + within-keyword
tier/trajectory reads. That's the whole scope.

**Could grow into** — pytrends exposes more surfaces behind the same client. Each is a *scoped*
addition (a new pytrends call + its own payload field), not a rediscovery:

| pytrends surface | Signal it would add | Note |
|---|---|---|
| `related_queries` / `related_topics` | demand *language* — the phrases people pair with the brand | Returns empty on low-volume brands; useful only for mid+ tier. A quarterly capture, not weekly. |
| `interest_by_region` | geographic concentration of branded interest | A second payload field beside `series`. |
| multi-timeframe | `today 3-m` (daily) + `today 12-m` (weekly) + `today 5-y` (monthly) for short- vs long-run | `--timeframe` already parameterizes one; capturing several per keyword in one run is the latent step. |

Keep the boundary deliberate: add a surface + its payload field, **not** a general pytrends client
wedged into this file. And note the boundary above it — *dated events* (news/funding spikes) and
*judgments* (tier bands, "who's winning") belong to the consumer, not this capture.

## The gotchas (most of the value)

These cost a probe or a real bug to learn — distilled from the competitive-traction Phase 9 work
(2026-05-24) and its Google-Trends primer (in the Teleprescribe agent-docs). Carry them forward;
don't relitigate them live.

- **Solo-per-brand is the capture shape; multi-batch + pivot-normalization is NOT.** pytrends'
  0-100 is normalized to the daily max *across the batch*, not each keyword's own peak. Batch brands
  of different magnitudes and the big ones crush the small ones — AgelessRx measured 15.6 solo vs
  0.5 in a production 5-batch (**30× swing, same brand, same week**), and pivot-normalization
  *amplifies* the swing rather than fixing it. So: one keyword per call, normalized to its own peak.
- **Scores are within-keyword, NOT cross-keyword comparable for absolute volume.** `Hone mean=49`
  and `Ro mean=59` does **not** mean Ro has more search volume — each is a fraction of *its own*
  peak day. Use `mean_to_peak_ratio` for **tier** (sustained ≈ high ratio vs spiky ≈ low) and
  `delta_7d_vs_prior_7d_pct` for **trajectory**. The payload `note` says this in-band so a consumer
  can't misread it. For a genuine "is X N× Y?" answer, ad-hoc pair-batch those two keywords — don't
  rebuild it into this capture.
- **Trajectory is robust; mean-to-peak less so; absolute magnitude not at all.** The within-keyword
  `7d vs prior 7d` delta shares one peak normalization across both windows, so it's reliable. Don't
  trust trajectory labels on near-zero series (a +48% on a base of 2 is noise) — that's a consumer
  read, which is why the tool emits the number and a mechanical label, not a "watch/act" verdict.
- **Common-word collisions silently inflate, and look *strong* not noisy.** "Eden" → 67 (biblical/
  city), "Fridays" → 99 (day of week), "Gala" → 8.8 (events). Eden at 67 reads like a Tier-1 brand;
  it's dictionary noise. The tool can't know — pass a `Label::disambiguating query`, or just don't
  pass the name. Sanity-check any single-common-noun name before trusting its score.
- **Bare brand name almost always wins.** A 16-brand bake-off found bare name beat `<name> reviews
  / cost / login` for 14/16. Don't waste capture slots on phrasing fallbacks — bare name, or a
  `::query` override when collision-prone. (One real surprise: `Hims & Hers` the literal phrase
  returns ~0.7; `::Hims` returns ~34. The ampersand kills it.)
- **≥4-char keywords only.** GTrends won't meaningfully match "Ro"/"Ulo". The tool **skips** a
  sub-4-char query with a reason rather than capturing noise; override with a longer anchor
  (`Ro::ro.co`).
- **Rate limits: ~20 sequential calls/min before 429.** Default `--sleep 7`; bump to 8 if you ran
  other pytrends work in the same hour. One 30s back-off retry clears most transient 429s; a second
  failure is usually keyword-level limiting (we hit persistent 429s on "Function Health" across runs
  5 min apart) — the tool records it in `fetch_errors` and moves on. Don't add longer back-off loops.
- **pytrends is unofficial — no SLA.** It breaks when Google changes the unauth endpoint (~3× in two
  years). When it breaks it **errors** (→ exit 2), it doesn't silently reshape — so there's no
  version-pinned parser and no exit 3 here. **Don't migrate to paid SerpAPI Trends ($50/mo) without
  a Brian decision**: same underlying data + same batch-normalization, only uptime differs.
- **Capture zeros as data.** A flat-zero or near-zero series is `ok: true` — "this brand is rarely
  searched by name" is itself a signal, not a failed fetch. Don't filter it.

## Output shape

The shared **envelope** keys lead; the trends payload sits beside them. Two library-shape notes:
**no `parser_version`** (pytrends isn't a parsed surface — the capture *methodology* is carried as
payload `method`/`method_version` instead), and **no `cost`** (pytrends is free/unmetered, so the
key is omitted rather than set to zero). `schema_drift` stays `[]` for envelope uniformity.

```jsonc
{
  // --- shared envelope ---
  "tool": "trends",
  "source": "trends.google.com",          // external system hit (via the unofficial pytrends client)
  "captured_at": "2026-06-08T17:51:12Z",  // the RUN's start (UTC) — per-keyword times are inside each series item
  "ok": false,                            // true iff EVERY keyword yielded a series (no errors, no skips)
  "input": { "keywords": [ { "label": "Ro", "query": "ro.co" } ], "timeframe": "today 3-m", "geo": "US", "sleep_seconds": 7.0 },
  "schema_drift": [],                     // always [] — no version-pinned parser; kept for uniformity (no exit 3)
  // --- payload (method/method_version stand in for parser_version; no cost key) ---
  "method": "solo-per-brand",
  "method_version": "v2",                 // bump on an intentional methodology change, not a transient hiccup
  "timeframe": "today 3-m",
  "geo": "US",
  "note": "Solo-per-brand: each keyword normalized to its OWN peak day … NOT cross-keyword comparable …",
  "keywords_in_scope": 3,
  "keywords_captured": 2,
  "fetch_errors": [],                     // [{ label, query, error }] for keywords that failed after retry
  "series": [                             // one entry per keyword, in input order
    {
      "label": "Hone Health", "query": "Hone Health",
      "captured_at": "2026-06-08T17:51:13Z",   // THIS keyword's fetch time (run start + sleeps/retries)
      "ok": true,
      "peak_value": 100.0, "peak_date": "2026-05-19",  // peak 0-100 + its date (the normalization anchor)
      "mean": 49.31,
      "mean_to_peak_ratio": 0.493,             // tier proxy: sustained (high) vs spiky (low)
      "delta_7d_vs_prior_7d_pct": 7.6,         // within-keyword momentum; null if <14 points or prior==0
      "trajectory": "flat",                    // rising | flat | fading | unknown
      "points": [ { "date": "2026-03-08", "value": 27 }, … ]  // raw daily 0-100 — the actual capture
    },
    { "label": "Ro", "query": "Ro", "captured_at": "…", "ok": false,
      "reason": "query shorter than 4 chars — GTrends won't match (override via 'Ro::<longer query>')" }
  ]
}
```

`points` is the raw signal; `peak_value`/`peak_date`/`mean`/`mean_to_peak_ratio`/`delta`/`trajectory`
are all derived from it — a consumer that wants a different window can recompute from `points`.
`peak_date` is the per-keyword normalization anchor (pytrends pins the 0-100 scale to the peak day), so
a cross-capture point-level delta is only comparable when both captures share it — the comparator
(`signal_delta.py`) reads it to veto a renorm-basis mismatch. Tiers and cross-keyword rankings are
**not** emitted: those are cohort-relative judgments for the consumer.

## Exit codes

- `0` — clean capture, **including** zero/near-zero series and **partial** runs (some keywords
  failed or were skipped; the captured rest is still emitted, gaps in `series[].ok` + `fetch_errors`).
- `2` — total failure: pytrends not installed, or **every attempted** keyword failed even after its
  retry (endpoint down / hard rate-limit). Partial JSON is still printed first.
- `3` — unused. pytrends breaks loudly rather than reshaping silently, so there's no version-pinned
  parser to drift; the `schema_drift`→exit-3 wiring is omitted (only `schema_drift: []` is kept).
```
