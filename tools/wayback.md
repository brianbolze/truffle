# wayback.py — Internet Archive first-seen / tenure lookup

Give it ONE URL; it asks the [Wayback Machine](https://web.archive.org)'s **CDX Server** for every
archived capture of that page and emits the **tenure signal** — first seen, last seen, how many
distinct content snapshots exist, and the status lifecycle (`200 → 301 → 404` = launched, moved,
died). One free GET, **no key**. Parsed JSON to stdout — no store write, no cohort, no vertical
baked in. The caller loops a roster; this tool does one page.

```bash
python3 tools/wayback.py https://www.henrymeds.com/treatments/
python3 tools/wayback.py example.com                       # bare domain -> the homepage (exact match)
python3 tools/wayback.py https://brand.com/products/sermorelin
```

**Why it earns a place:** page/SKU *tenure* is the strongest age proxy we have, and a first-seen
date doesn't rot — unlike a price or a roster line, it's a fact about the past that only accretes.
It's the **Tenure axis** of the candidate-SKU ledger (`first_seen_date` / `first_seen_method` /
`first_seen_confidence`).

## first-seen is a LOWER BOUND (the load-bearing caveat)

The output is "first **archived**," never "first existed." Three things make a page's true birth
*earlier* than its first snapshot — so treat every `first_seen` as a floor, never a birthday:

- **Under-archiving.** Fresh or obscure pages get crawled late; a SKU page can be live for months
  before the Archive notices it. Empty CDX (`first_seen: null`) means *never archived* — too new,
  too obscure, or `robots.txt`/exclusion-blocked — **not** that the page never existed.
- **Domain ≠ brand.** A first-seen on a *domain* can predate the current brand by years if someone
  else owned the domain first. Live: `wayback.py hims.com` → `first_seen: 2001` (a prior owner; the
  telehealth brand is ~2017). For brand/SKU tenure, query the **specific deep URL**, not the apex —
  or read the apex result as "the domain has existed since," nothing more.
- **Confidence is about corroboration, not age.** `first_seen_confidence` mirrors the SKU ledger's
  labels and reacts to *how many captures back the date up*, never to how old it is:

  | label | rule | read |
  |---|---|---|
  | `insufficient` | 0 captures | never archived — tenure unmeasurable (data, not an error) |
  | `provisional` | exactly 1 capture | a first-seen exists but is uncorroborated; the page may predate its lone snapshot |
  | `measured` | ≥2 distinct-content captures | archived tenure is real; `first_seen` is a solid lower bound (the ledger's "≥2 real captures" bar) |

  It does **not** check whether the captures span meaningful *time* — two captures a day apart are
  still `measured`. A caller that needs "first seen ≥6 months ago" reads `first_seen` / `tenure_days`
  itself; that time-span judgment is the caller's, kept out on purpose.

## The captured_at split (why this tool exists to test the convention)

This is the exact case the library's envelope rule warns about. The Wayback snapshot dates **are**
the signal, so they live *inside the payload* under their own names — `first_seen`, `last_seen`,
per-snapshot `timestamp`. The envelope's `captured_at` is **this lookup's wall-clock** (when we asked
CDX), never an archive date. Conflating the two would destroy the whole field: you'd "freshen" a
roster's tenure to today every time you re-ran it. The split is the point.

## What it does now vs. what it could grow into

**Now — CDX metadata for one exact URL.** The capture list and what you derive from it. That's the
whole scope. Each growth path below is a *scoped* addition (a new endpoint or param + its own
handling), not a rediscovery — all latent, none built:

| Growth path | What it would add | Note |
|---|---|---|
| Historical **content** fetch + diff | CDX picks snapshots at target dates → fetch `web.archive.org/web/<ts>id_/<url>` (the `id_` suffix = raw archived bytes, no Wayback chrome) → optionally clean via Firecrawl → diff what the page *said* over time | The big one: turns tenure into "when did this SKU/price/claim first appear." `first_snapshot_url` is the seed. |
| [Availability API](https://archive.org/help/wayback_api.php) | closest single snapshot to a given date (`/wayback/available?url=…&timestamp=…`) | A one-shot "what did this look like on date X" — lighter than walking the full CDX list. |
| `matchType=prefix` / `domain` | whole-section history (`/products/*`, or every URL on a domain) | Section-level tenure / "when did this catalog branch appear." This tool is **exact-URL only**. |
| CDX `from` / `to`, `limit=-N`, `fastLatest` | date-windowed or cheap-latest queries | For a pure first-seen headline you only need the first row; for "still alive?" only the last. v1 always fetches the full history (tenure needs the count + trail). |

Keep the boundary deliberate: add an endpoint/param + its handler, **not** a general Archive client
wedged into this file.

## The gotchas (most of the value)

These cost a probe or a real bug to learn. Carry them forward; don't relitigate them live.

- **`collapse=digest` makes the count mean something.** CDX folds *adjacent* captures with an
  identical content hash, so a snapshot row = "content that differs from the row before it," and
  `snapshot_count` is a **distinct-content** count, not a raw crawl count (a page crawled 500× with
  no change collapses to 1). That's what makes `≥2` a real corroboration bar rather than a crawl-rate
  artifact. Collapse keeps the *earliest* row of each content-run — i.e. *when that content first
  appeared* — which is exactly the tenure semantics we want.
- **Empty CDX is data, not failure.** A never-archived URL returns HTTP 200 with an **empty body**
  (not `[]`). The tool normalizes that to `first_seen: null`, `confidence: "insufficient"`,
  `ok: true`, **exit 0**. Never confuse "the Archive never saw it" with "the lookup failed."
- **`status` is verbatim — including `-`.** CDX emits `-` for revisit / unknown-status records;
  redirects (`301`/`302`/`307`/`308`), `403`, `410`, `400` all show up live. We report the code, we
  don't normalize or judge it. The `status_trail` collapses *consecutive* same-status captures into
  runs, so a launch→redirect→death lifecycle reads at a glance (e.g. `pets.com`: a long `301`/`403`
  parked-death tail after the dot-com bust). The trail is computed over the **full** history and sits
  top-level, so the snapshots cap below never hides a page's death.
- **`snapshots` is capped; the summary isn't.** The emitted `snapshots` list is bounded at
  **500 rows** (oldest first — this tool's first-seen focus) to keep the blob sane; `snapshots_truncated`
  flags when it's trimmed. The headline fields (`first_seen` / `last_seen` / `snapshot_count` /
  `status_trail`) are **always** computed over the full set, so truncation is cosmetic — a 16,877-capture
  domain like `theranos.com` still reports the true count and full trail.
- **Exact-URL match, and it's SURT-canonicalized.** CDX matches the canonical form, so `http://`
  vs `https://` and a `www.` prefix collapse to the same key — but a **trailing slash and a deep path
  are significant**. `/treatments` and `/treatments/` can be different keys; if a SKU returns
  `insufficient`, try the slash variant (and the apex) before concluding it was never archived.
- **No key, but be polite.** CDX is free and unauthenticated. The Archive can be slow (a deep-history
  domain is a multi-thousand-row response) and will rate-limit an aggressive loop — space the calls
  when sweeping a roster. Timeout is 60s.

## Output shape

The shared **envelope** keys lead; wayback's payload sits beside them — and critically, the archive
dates are *in the payload*, never lifted to `captured_at`. **No `parser_version`** (CDX is a frozen
feed — no version-pinned parser, so no schema-drift path), **no `cost`** (free), **no key**. Real
capture (trimmed):

```jsonc
{
  // --- shared envelope ---
  "tool": "wayback",
  "source": "web.archive.org/cdx",       // the external system hit (the CDX Server)
  "captured_at": "2026-06-08T18:10:05Z", // THIS lookup's wall-clock (UTC) — NOT an archive date
  "ok": true,                            // transport failures exit 2 before this; empty CDX is still ok
  "input": { "url": "https://www.henrymeds.com/treatments/" },
  "schema_drift": [],                    // always [] — frozen feed, kept for envelope uniformity
  // --- payload (the archive dates the envelope must NOT carry) ---
  "first_seen": "2022-12-05T04:49:34Z",  // earliest archived capture — a LOWER BOUND on the page's age
  "last_seen": "2026-02-16T17:40:52Z",   // most recent capture (a still-alive proxy)
  "first_seen_confidence": "measured",   // insufficient | provisional | measured
  "tenure_days": 1281,                   // captured_at - first_seen, in days; a lower bound
  "snapshot_count": 22,                  // distinct-content captures (post collapse=digest) — full count
  "snapshots_truncated": false,          // true when `snapshots` (below) is capped at 500; summary stays full
  "status_trail": [                      // consecutive same-status captures collapsed into lifecycle runs
    { "status": "200", "from": "2022-12-05T04:49:34Z", "to": "2025-05-16T01:42:45Z" },
    { "status": "308", "from": "2025-05-24T00:42:34Z", "to": "2025-05-24T00:42:34Z" },
    { "status": "200", "from": "2025-05-24T00:42:34Z", "to": "2026-02-16T17:40:52Z" }
  ],
  "first_snapshot_url": "https://web.archive.org/web/20221205044934/https://henrymeds.com/treatments/",
  "last_snapshot_url":  "https://web.archive.org/web/20260216174052/https://henrymeds.com/treatments/",
  "snapshots": [                         // oldest-first; capped at 500 rows (see snapshots_truncated)
    { "timestamp": "2022-12-05T04:49:34Z", "url": "https://henrymeds.com/treatments/",
      "status": "200", "digest": "S6TCGVNIVYRBL7YQU7VDSTGKGVSVUANQ" }
  ]
}
```

A never-archived URL is the same envelope with `first_seen`/`last_seen`/`tenure_days` `null`,
`first_seen_confidence: "insufficient"`, `snapshot_count: 0`, and `snapshots: []` — `ok: true`,
exit 0.

## Exit codes

- `0` — clean capture (**including** a never-archived URL → `insufficient`, the empty-CDX signal).
- `2` — fetch error: network, an Archive HTTP error (4xx/5xx), or an unexpected/garbled CDX body
  (a non-list response, or a header missing a required column — surfaced loud rather than parsed-on).
- `3` — unused. CDX is a frozen feed with no version-pinned parser to drift, so this never fires; the
  `schema_drift`→exit-3 wiring is kept only to stay uniform with the drift-prone tools (serpapi,
  trustpilot).
