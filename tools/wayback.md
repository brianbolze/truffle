# wayback.py — Internet Archive tenure + archived-content diff

Give it ONE URL. By default it asks the [Wayback Machine](https://web.archive.org)'s
[CDX Server](https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server) for archived
captures of that page and emits the **tenure signal**: first seen, last seen, distinct-content
snapshot count, and status lifecycle. In `diff` mode, it selects two CDX snapshots, fetches raw
`id_` replay content, extracts normalized text, and emits hashes plus a bounded unified diff.

No key. No store write. No cohort. No SKU/claim judgment.

```bash
python3 tools/wayback.py https://www.henrymeds.com/treatments/
python3 tools/wayback.py example.com
python3 tools/wayback.py tenure https://brand.com/products/sermorelin

python3 tools/wayback.py diff https://brand.com/products/sermorelin
python3 tools/wayback.py diff https://brand.com/products/sermorelin --from 2023 --to 2025
python3 tools/wayback.py diff example.com --context-lines 1 --max-diff-lines 80
```

## What It Captures

**Default / `tenure`: CDX metadata for one exact URL.** It reports when the Archive first and last
saw distinct content at that canonical URL key.

**`diff`: raw archived content for two snapshots.** It uses the same CDX query, chooses first/last
distinct snapshots by default, or nearest snapshots to `--from` / `--to`, then fetches:

```text
https://web.archive.org/web/<timestamp>id_/<original_url>
```

The `id_` suffix requests original/raw replay mode. The tool preserves the normal replay URL too, so
a human can inspect the Wayback-rendered page separately.

## URL Matching

The tool does **not** rewrite the caller's URL before sending it to CDX. `example.com` is passed as
`url=example.com`, not normalized by us to `https://example.com/`.

CDX exact matching is still canonicalized by Wayback's SURT key: HTTP/HTTPS, case, and `www.` are
not treated as separate in the same way a raw string comparison would be. Paths and trailing slashes
still matter. So:

- `example.com`, `http://example.com/`, and `https://www.example.com/` may land on the same canonical homepage key.
- `/treatments` and `/treatments/` can be different keys.
- If a deep SKU URL returns `insufficient`, try the slash variant before reading meaning into absence.

That is CDX behavior, not tool-side normalization.

## Lower-Bound Caveat

The output is "first **archived**," never "first existed." A page can predate its earliest snapshot
because the Archive crawled it late, was blocked, or never saw it.

`first_seen_confidence` is corroboration, not age:

| label | rule | read |
|---|---|---|
| `insufficient` | 0 captures | never archived; tenure unmeasurable, not an error |
| `provisional` | exactly 1 capture | first-seen exists but is uncorroborated |
| `measured` | >=2 distinct-content captures | archived tenure is real; first-seen is a solid lower bound |

The caller decides whether "old enough" or "meaningful change" follows from that evidence.

## Diff Mode Caveats

- **Mechanical text only.** HTML is parsed with a tiny stdlib parser that drops script/style-ish
  content and collapses whitespace. It does not render JavaScript, click through modals, resolve
  lazy content, or infer meaning.
- **CDX digest is provenance, not our byte hash.** CDX `digest` describes the archived response body
  as stored by the Archive. The tool also emits `content_sha256` over bytes fetched from replay and
  `text_sha256` over normalized extracted text.
- **Replay fetches can fail.** A selected CDX row can have a replay response that returns a non-2xx
  status. The JSON keeps `fetch_status`, `fetch_ok`, `fetch_error`, byte count, and hashes when a
  response body exists; `ok:false` marks that the comparison did not complete cleanly.
- **No-snapshot states are data.** `no_snapshots`, `insufficient_snapshots`, and
  `insufficient_distinct_selection` exit cleanly with `ok:true` and `diff:null`.
- **Diffs are bounded.** `diff.lines` is capped by `--max-diff-lines`; hashes and line counts still
  let callers compare outputs even when the visible diff is truncated.

## Output Shape

The shared envelope keys lead every output. Source/archive dates stay inside payload fields; top-level
`captured_at` is only this invocation's wall-clock.

Default tenure output, trimmed:

```jsonc
{
  "tool": "wayback",
  "source": "web.archive.org/cdx",
  "captured_at": "2026-06-08T18:10:05Z",
  "ok": true,
  "input": { "url": "https://www.henrymeds.com/treatments/" },
  "schema_drift": [],

  "first_seen": "2022-12-05T04:49:34Z",
  "last_seen": "2026-02-16T17:40:52Z",
  "first_seen_confidence": "measured",
  "tenure_days": 1281,
  "snapshot_count": 22,
  "snapshots_truncated": false,
  "status_trail": [
    { "status": "200", "from": "2022-12-05T04:49:34Z", "to": "2025-05-16T01:42:45Z" }
  ],
  "first_snapshot_url": "https://web.archive.org/web/20221205044934/https://henrymeds.com/treatments/",
  "last_snapshot_url": "https://web.archive.org/web/20260216174052/https://henrymeds.com/treatments/",
  "snapshots": [
    {
      "timestamp": "2022-12-05T04:49:34Z",
      "url": "https://henrymeds.com/treatments/",
      "status": "200",
      "digest": "S6TCGVNIVYRBL7YQU7VDSTGKGVSVUANQ"
    }
  ]
}
```

Diff output, trimmed:

```jsonc
{
  "tool": "wayback",
  "source": "web.archive.org/cdx",
  "captured_at": "2026-06-08T18:10:05Z",
  "ok": true,
  "input": {
    "mode": "diff",
    "url": "https://brand.com/products/sermorelin",
    "from": "2023",
    "to": "2025",
    "context_lines": 3,
    "max_diff_lines": 400
  },
  "schema_drift": [],
  "selection": {
    "strategy": "nearest_targets",
    "state": "selected",
    "note": null,
    "snapshot_count": 9
  },
  "selected_snapshots": [
    {
      "timestamp": "2023-02-01T12:30:00Z",
      "raw_timestamp": "20230201123000",
      "original_url": "https://brand.com/products/sermorelin",
      "replay_url": "https://web.archive.org/web/20230201123000/https://brand.com/products/sermorelin",
      "raw_replay_url": "https://web.archive.org/web/20230201123000id_/https://brand.com/products/sermorelin",
      "status": "200",
      "digest": "CDXDIGEST",
      "mimetype": "text/html",
      "length": 12345
    }
  ],
  "contents": [
    {
      "timestamp": "2023-02-01T12:30:00Z",
      "fetch_status": 200,
      "fetch_ok": true,
      "content_type": "text/html; charset=utf-8",
      "byte_count": 9421,
      "content_sha256": "…",
      "text_char_count": 2213,
      "text_line_count": 77,
      "text_sha256": "…"
    }
  ],
  "text_changed": true,
  "diff": {
    "format": "unified_diff",
    "context_lines": 3,
    "max_diff_lines": 400,
    "truncated": false,
    "line_counts": { "from": 77, "to": 81, "common": 72, "added": 9, "removed": 5 },
    "lines": ["--- 2023-02-01T12:30:00Z …", "+++ 2025-01-04T09:00:00Z …"]
  }
}
```

## Gotchas

- **`collapse=digest` makes counts useful.** Adjacent identical-content captures collapse to the
  first row in that run. `snapshot_count` is a distinct-content count, not raw crawl count.
- **`snapshots` is capped; summaries are not.** The default tenure payload emits at most 500
  snapshots, oldest first. `first_seen`, `last_seen`, `snapshot_count`, and `status_trail` are
  computed over the full CDX result.
- **`status` is verbatim.** `-`, redirects, `403`, `410`, and parked-domain failures are reported,
  not normalized.
- **Be polite.** One diff does one CDX request plus at most two replay fetches. Do not wrap it in an
  aggressive loop without sleeps/retries above this tool.

## Exit Codes

- `0` — clean capture, including empty/no-snapshot states.
- `2` — transport error: network failure, CDX HTTP error, or unexpected/garbled CDX body.
- `3` — unused today. CDX is treated as stable/no parser version; `schema_drift` remains `[]` for
  envelope uniformity.
