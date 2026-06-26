# Implementation Notes: Source Page Tool

Date: 2026-06-26
Status: completed — graduated to `tools/source_page.py` (+ shared `tools/_firecrawl.py`); both reviews satisfied (proposal-review accept; packet-review hold-until-finding-1, now fixed); gate green, merged
Builds: `proposal.md` (Approved for implementation) + `proposal-review.md` (Accept, fold findings 1 & 2).

## What shipped

A narrow, print-only capture primitive: fetch ONE URL, reduce it to source-page evidence
(title / normalized text / absolute links), emit ONE envelope to stdout. Direct HTTP by default
(zero spend); `--firecrawl-fallback` spends at most one credit when direct HTTP fails. No store
write, no `page_role`, no classification, no cohort/candidate logic.

The two review findings the lead asked to fold in are both honored:
- **Finding 1 (negative spend check):** a unit test asserts exactly one Firecrawl call, no retry on
  a malformed response, and zero calls when direct HTTP already succeeded.
- **Finding 2 (`ok` floor + gzip/encoding):** `ok:true` now requires a 2xx/3xx status, a text body,
  a clean decode (U+FFFD ratio guard), AND ≥500 reduced chars. gzip/deflate are decompressed;
  undecodable bodies fail loud instead of emitting mojibake. Carried into `source_page.md` gotchas.

## Changed files

| File | Change |
|---|---|
| `tools/source_page.py` | new — the tool (direct HTTP + optional Firecrawl fallback, stdlib reducer) |
| `tools/source_page.md` | new — companion doc (CLI, `ok` contract, gotchas, output shape, exit codes, credits) |
| `tools/README.md` | edit — one table row added for `source_page.py` (page-grain source evidence) |
| `tests/test_source_page.py` | new — 22 tests (reducer, envelope, `ok` floor, spend boundary, capture-primitive boundary) |
| `tests/fixtures/source_page/listicle.html` | new — synthetic listicle fixture for the reducer tests |

No writes under `store/`, `cohorts/`, or experiment run dirs. The tool itself performs no file IO
(a negative test enforces this).

## Commands run + results

### Deterministic gate (no network, no spend)
- `ruff check tools/source_page.py tests/test_source_page.py` → **All checks passed**
- `ruff format --check …` → **2 files already formatted**
- `python3 -m pytest tests/test_source_page.py -q` → **22 passed**
- `python3 -m pytest tests/ -q` (full suite, regression) → **113 passed**

The 22 tests cover, per the acceptance checks:
- **Reducer** (#1): title extraction, script/style/noscript/svg skipped, whitespace-normalized text,
  relative→absolute link resolution against the final URL, www-stripped domains, link positions.
- **Envelope shape** (#7): required spine + payload keys present, `tool=source_page`,
  `source=direct_http`, `schema_drift=[]`, no `cost` key on the direct path, `text` capped but
  `text_chars` full-length.
- **`ok` floor + guards** (#4): thin shell → `ok:false` (keeps parsed text), HTTP 403 → loud,
  transport failure → envelope-not-crash, binary content-type → rejected unparsed, gzip-with-encoding
  → decompresses to `ok:true`, gzip-without-encoding → garbled → `ok:false`.
- **Firecrawl envelope** (#5): `ok` from success+markdown, `source=firecrawl.dev/scrape`,
  `cost.firecrawl_credits_estimate:1`, links normalized from both string and dict shapes.
- **Spend boundary** (#6): direct success never spends even with the flag; blocked-without-flag
  spends nothing; malformed Firecrawl response → exactly one call, no retry, 1 credit; Firecrawl
  transport error → one attempt, 0 credits.
- **Capture-primitive boundary** (#9): no classification/routing key tokens
  (`page_role`/`role`/`cohort`/`candidate`/`classif`/`worth`/`membership`) anywhere in the output;
  source has no file-write surface (`open(`/`Path(`/`.mkdir(`/`.write_text(`/`.write_bytes(`), no
  `sys.exit(3)`, no `PARSER_VERSION`, and never emits those classification literals as JSON keys.

### Live smoke checks (network)
| URL | Flag | Result |
|---|---|---|
| Flow Space menopause | none | `ok:true`, status 200, `text_chars=18095`, `link_count=249`, exit 0 |
| Tana Otter alternatives | none | `ok:true`, status 200, `text_chars=14514`, `link_count=33`, exit 0 |
| Forbes GLP-1 list | none | `ok:false`, status **403**, `error="HTTP 403: Forbidden"`, stderr warning, **exit 2** (loud, no spend) |
| Forbes GLP-1 list | `--firecrawl-fallback` | `ok:true`, `source=firecrawl.dev/scrape`, status 200, `text_chars=105611`, `link_count=496`, `cost.firecrawl_credits_estimate=1`, `input.direct_http_error="HTTP 403: Forbidden"`, exit 0 |

Both direct captures cleared the prior probe's blocked-page problem via the real browser UA (the
probe's bot UA is what got it 403'd). Forbes still hard-walls direct HTTP and is the intended
fallback case.

## Spend used

**1 Firecrawl base scrape credit**, total — the single approved fallback acceptance check on the
Forbes GLP-1 page (`markdown`+`links` only, no LLM/json, no enhanced proxy, no retry). Zero SerpAPI /
Exa / other spend. The negative spend boundary is enforced by tests, not just prose.

## Skipped / not done (by design)

- **No live network in the test suite.** Live smokes are documented here (they require network +
  optional spend); the committed tests are hermetic (mocked `fetch_url` / `firecrawl_scrape`).
- **No `<base href>` support.** Relative links resolve against the page's final URL; a `<base href>`
  page is a documented limitation (rare). Cut to stay small.
- **No `--min-text-chars` knob.** The 500-char usefulness floor is a documented constant, not a CLI
  flag — kept off the surface per "stay small".
- **No drift-sweep / MAINTAINING gate.** This is an additive `tools/` entry; it changes no contract
  (`SCHEMA.md`/`TAXONOMIES.md` untouched), so the contract blast-radius gate doesn't apply. ruff +
  the full test suite are the gate that does.

## Remaining risks

- **Anti-bot drift.** The hardcoded Chrome UA clears polite gates today; sites can tighten and push
  more pages onto the (paid) fallback. Mitigation: the fallback exists and is bounded; the UA is a
  one-line bump if a class of pages starts 403'ing.
- **`br` (brotli) bodies.** Not in the stdlib, so a brotli-encoded body that ignores `identity` fails
  loud (`ok:false`) rather than reducing. Acceptable per "fail loud before silently wrong"; if it
  shows up often, the fix is a scoped decode helper, not a new dep by default.
- **Firecrawl credit accounting is an estimate.** `firecrawl_credits_estimate:1` assumes one base
  scrape charge when Firecrawl answers; the true charge is whatever Firecrawl meters. Named as an
  estimate, consistent with the probe.
- **`_firecrawl.py` extraction trigger is now live — flagged, not acted on.** Honest tension: the
  approved proposal lists a shared `_firecrawl.py` under `escalate_if` and inlines the call (which I
  did), but `trustpilot.py`'s own comment says "lift a shared `_firecrawl.py` on the SECOND Firecrawl
  tool" — and `source_page.py` IS that second tool. So this packet leaves two inlined Firecrawl
  callers that the documented rule says should now be unified. I deferred per the proposal (source of
  truth; don't re-litigate), but the extraction is a clean, earned follow-up change for Brian to call
  — it's a refactor across `trustpilot.py` + `source_page.py`, not a hidden feature in this primitive.

## Follow-up (2026-06-26): shared `_firecrawl.py` lift + finding-1 fix + playbook alignment

Brian prioritized the `_firecrawl.py` lift, and the independent `change`-mode review
(`packet-review.md`) caught a real failure-path bug the first pass missed. Both addressed together,
since they touch the same code.

- **Lifted [`tools/_firecrawl.py`](../../../../tools/_firecrawl.py)** — the shared `/v2/scrape` caller
  (call + JSON parse + failure-classification only; the request recipe stays each caller's). Both
  `trustpilot.py` and `source_page.py` now route through it; their inlined POST/`json.load` is gone.
  It returns a `ScrapeResult{reached, raw, error}` and **never raises** for the four expected failure
  modes, so each caller keeps its own contract (`source_page` → one envelope; `trustpilot` → exit 2).
- **Fixed finding 1 (the bug):** the old `capture_firecrawl` called `load_key()` outside its `try` and
  caught only `URLError/TimeoutError/OSError`, so a **missing key** (`RuntimeError`) or a **non-JSON
  response** (`JSONDecodeError`) escaped before any envelope printed — breaking the one-envelope
  contract. The helper now classifies both into a `ScrapeResult`; `source_page` always emits `ok:false`.
  Credit is billed iff Firecrawl actually answered (`reached`): a missing key / pre-answer transport
  error = 0; an unparseable-but-received body = 1. The old redundant `error_transport` key is gone.
- **Playbook alignment (Brian's steer to `firecrawl-capture.md` + `fc.py`):** `source_page` now reports
  Firecrawl's own per-call `metadata.creditsUsed` (the attribution-grade billed number — catches a
  multi-page PDF's >1 charge) when present, falling back to the reached-based estimate; this matches
  `trustpilot.py` and `fc.py`. The recipe was already playbook-compliant (`maxAge:0` + `location:US` +
  `waitFor:3500`, `markdown,links` only, no `json`/enhanced-proxy/`/crawl`). Link-outs to the playbook
  added in `_firecrawl.py`, `source_page.md`, and `tools/README.md`. `fc.py`'s `post()` stays a
  separate caller on purpose (store-coupled, settings.json key source) — documented, not merged.

### Follow-up gate (no new spend)
- `ruff check` + `ruff format --check` on `_firecrawl.py`, `source_page.py`, `trustpilot.py`,
  `test_source_page.py`, `test_firecrawl.py` → **clean**.
- `pytest tests/` → **124 passed** (was 113): `test_source_page.py` 22→25 (added missing-key,
  unparseable-response, and `creditsUsed`-honored cases at the tool seam), plus new
  `test_firecrawl.py` (8 — the helper's four failure modes + auth-header/api-key plumbing, mocking
  `urlopen` where the bug actually lived).
- **Live direct-HTTP smoke (zero spend):** Tana listicle → `ok:true`, status 200, `text_chars=14514`,
  `link_count=33`, no `cost` key, exit 0 — byte-identical to the original receipt; the refactor
  preserved behavior.
- **Firecrawl fallback path not re-smoked** — no re-authorized spend for this follow-up; the 8 helper
  unit tests cover the wiring, and the original receipt already proved the live fallback. `trustpilot.py`
  has no test suite, so it was refactored conservatively to preserve its exact exit-2 behavior (key
  still pre-loaded in `fetch_and_parse`; only the POST/parse moved to the helper).
