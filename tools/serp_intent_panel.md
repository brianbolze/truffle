# serp_intent_panel.py — repeatable buyer-intent SERP panels

Builds a small evidence panel over captured `serpapi.py` envelopes: query in, cohort in, comparable
own-page / third-party mention / AI Overview ranked-brand and reference output out.

This is a consumer helper, not a capture tool. It can optionally call `serpapi.py` for missing
captures, but only with `--fetch-missing`.

```bash
python3 tools/serp_intent_panel.py \
  --queries queries.json \
  --cohort cohort.json \
  --captures captures/

python3 tools/serp_intent_panel.py \
  --queries queries.json \
  --cohort cohort.json \
  --captures captures/ \
  --format markdown
```

## Inputs

Query set JSON can be a bare list:

```json
[
  "online payroll software",
  { "id": "expense", "category": "finance", "query": "best expense management software" }
]
```

Or an object with defaults:

```json
{
  "defaults": { "gl": "us", "hl": "en", "device": "desktop" },
  "queries": [
    { "id": "payroll", "category": "finance", "query": "online payroll software" }
  ]
}
```

Cohort JSON is the `_match.py` shape:

```json
[
  { "slug": "alphapay", "domain": "alphapay.com", "aliases": ["AlphaPay"] },
  { "slug": "betaledger", "domain": "betaledger.com", "aliases": ["Beta Ledger"] }
]
```

Captures are existing `serpapi.py` JSON envelopes. Pass files or directories to `--captures`; a
directory is scanned recursively for `.json`. If multiple captures exist for the same query, the
latest `captured_at` is used.

## Output

Default output is JSON with one row per query:

- `organic_top10_match_count`
- `own_page_matches`
- `third_party_mention_matches`
- `ai_overview.ranked_brand_matches`
- `ai_overview.reference_matches`
- `serp_character` counts and sample unmatched results
- `query_usefulness_labels`

Labels are deliberately plain and mechanical:

- `clean`
- `noisy`
- `listicle-heavy`
- `local-clinic-heavy`
- `supplement/retail drift`
- `no cohort signal`
- `no_capture`

These labels help decide whether a query is worth tracking. They are not traction judgments.

## Live capture

No live calls happen by default. To fill missing captures:

```bash
python3 tools/serp_intent_panel.py \
  --queries queries.json \
  --cohort cohort.json \
  --captures captures/ \
  --fetch-missing \
  --write-fetched-captures captures/
```

`--organic-only` applies only to live missing captures. It does not alter existing capture files.

## Boundary

This tool measures cohort visibility inside a query surface. It does **not** estimate demand, spend,
conversion, market share, or market traction. Category-specific interpretations, stop/continue gates,
and project ledgers belong outside Web Research.
