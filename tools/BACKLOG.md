# tools backlog

Reusable method capabilities for `tools/`: small capture scripts plus generic consumers that make
repeat research boring, auditable, and comparable. The north star is a fresh agent running the same
panel next week and producing evidence that can be diffed without relitigating the method.

`tools/` is still source-capture first: fetch, parse, emit JSON, preserve provenance. Matching,
batching, diffing, and source-aware comparators may live nearby as reusable consumers, but they
should not smuggle in project judgment. Project calls like "credible traction," "supply only," or
"vetoed" stay project-side.

**Not this file:**
- Root [`BACKLOG.md`](../BACKLOG.md) — engine-level schema, verbs, and workflow decisions.
- Tool companion docs (`*.md`) — durable gotchas and output examples for a specific source.
- Project workflows — Teleprescribe-specific panels, ledgers, and strategic reads stay project-side
  unless they prove a reusable method capability.

**Item format.** A bold punchline + tags on one scannable line, then 1-3 tight sentences. Tags:
`[weakness]` gap likely to bite · `[idea]` possible improvement · `[bug]` confirmed defect ·
`[tbd]` pending decision · `[simplification]` removes surface area / prescriptiveness.

**Bias to remove.** Prefer small generic consumers over bigger source tools. If an item adds a helper,
name the ad hoc loop, fragile comparison, or repeatable caller pain it replaces.

**Soft cap: <=15 open items.** Over that, cut or graduate before adding more.

---

## Highest leverage

- **Batch runner for repeated captures, not per-project loops** `[idea]`
  SERP, Trustpilot, Exa, and Wayback each do one focused capture; agents should not keep writing
  throwaway loops for 15-brand panels or 50-URL ledgers. Add a generic runner that reads CSV / JSON /
  JSONL / stdin rows, invokes one capture command repeatedly, records row id + args + exit code +
  stderr + cost, and emits JSONL or one combined run envelope. Keep destination writes out of scope.
  **Act when:** running the same capture across a panel by hand feels silly twice.

- **Envelope comparator / delta layer before any traction score** `[idea]`
  We need repeat captures to become comparable evidence: Trustpilot review deltas, SERP rank movement,
  Trends window changes, Wayback tenure/content changes. Build a generic comparator that understands
  the shared envelope spine and has small source-aware payload branches, but emits deltas and
  comparability notes only. No blended score, no market-share read.
  **Act when:** there are two captures of the same panel or source.

- **Trustpilot velocity + integrity comparator belongs beside the capture tool** `[idea]`
  `trustpilot.py` correctly captures profile state and raw flags; velocity and comparability need a
  separate consumer over two or more envelopes. Output review-count deltas, monthly velocity,
  profile-state vetoes, paid/merged comparability flags, solicitation flags, and duplicate/template
  hints. Keep SKU/category claims out unless review text names the SKU.
  **Act when:** the D7/D14 review panel is run from captured JSON instead of a markdown hand table.

## Tool hardening

- **Clarify partial-capture exit semantics for orchestration** `[tbd]`
  `trends.py` can emit useful partial JSON with top-level `ok:false` while still exiting `0`. That
  may be right, but a batch runner needs one rule: exit code is transport/drift only and callers read
  `ok` for completeness, or partial data exits non-zero. Pick once and update `tools/README.md`.
  **Act when:** the batch runner depends on shell exit status.

- **Golden fixture tests for capture parser contracts** `[weakness]`
  `_match.py` now has regression tests, but the capture parsers still rely mostly on prose gotchas.
  Add small fixtures for SerpAPI inline AIO / async error / list rejection, Trustpilot active-empty-
  removed-not-found plus Cloudflare challenge classification, Exa missing `results`, and Wayback
  empty CDX / malformed header. No live API calls.

- **Tiny envelope validator before an envelope builder** `[idea]`
  Every capture tool repeats the reserved JSON spine. Do not jump straight to a shared factory; a
  lightweight validator or test helper can pin top-level keys, UTC `captured_at`, `schema_drift`
  behavior, JSON-object output, and optional `cost` / `parser_version` rules while preserving local
  construction inside each tool.
  **Act when:** adding fixture tests or the next capture tool.

- **Small docs/install smoke pass for the tools surface** `[weakness]`
  Keep the setup discoverable without turning `tools/` into a package: optional dependency notes for
  `pytrends`, import/help smoke commands, and docs that reflect `_match.py` / `serp_match.py` as
  current rather than planned. Also keep generated `__pycache__/` files out of staged changes.
  **Act when:** preparing the tools directory for commit or handoff.

## Graduated

- **Wayback content fetch + diff** `[done]`
  `wayback.py diff <url>` now selects two exact-URL CDX snapshots, fetches raw `id_` replay content,
  preserves per-snapshot provenance, emits byte/text hashes, and returns a bounded unified diff. The
  bare-domain/exact-URL behavior is pinned as documented CDX canonicalization, not tool-side URL
  rewriting.

## Deliberate deferrals

- **SKU ledger builder should wait for the primitives to prove the axes** `[idea]`
  The ledger shape is useful, but most of it is orchestration: seed SKUs, run Wayback/SERP/Trustpilot
  axes, then label supply, visibility, plausible movement, not measurable, or vetoed. Build it as a
  project-side or recipe-level consumer only after Wayback content/diff, SERP panels, and repeat
  Trustpilot captures show the axes separate real evidence.

- **Avoid blended traction scores until repeat captures and backtests exist** `[simplification]`
  A single number will hide the evidence boundary we are trying to protect: presence/supply,
  visibility, push, and movement are different signals. Keep outputs axis-specific until we have
  repeat panels, known misses, and enough backtest examples to justify weights.

- **Do not migrate Reddit into `tools/` by inertia** `[simplification]`
  Prior traction work found raw Reddit/forum counts sparse, rate-limit-frictiony, and easy to
  overread. Keep `reddit.py` deferred unless a new consumer has a narrow source, query, and
  text-classification reason that beats the old failure mode.

- **Do not add Ad Library until capture stability and language are pinned** `[tbd]`
  Meta ads can be a useful push signal, but the old route depended on an Apify actor and unstable
  placeholders. Before promoting it, confirm the actor/build pin, schema-drift path, cost envelope,
  and explicit framing as push signal, not demand. Otherwise it will look quantitative while mostly
  measuring capture artifacts.
