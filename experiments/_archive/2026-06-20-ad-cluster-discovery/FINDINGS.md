---
created: 2026-06-20
status: experiment verdict — ad-cluster discovery v1
runs: runs/2026-06-20/ (corpus.json, ad-cluster-map.md)
---

# Findings — ad-cluster discovery verb (v1)

## Verdict

**The verb works and is worth graduating — lean.** A *space* query ("what ads are compounded-Rx
D2C brands running?") → **top-K verified messaging-angle clusters, keyed to the store, with a
propose-capture worklist** — came out genuinely useful in one bake-off pass for ~$5–7 all-in.

Graduate it as **one small capture tool + one reusable workflow recipe**, not infrastructure:

- **Capture → `tools/ad_library.py`** (the deferred tool the BACKLOG named, now validated against the
  *right* actor). Apify `apify/facebook-ads-scraper`, keyword Ad-Library search URL → standard
  envelope; per-company envelopes persist to `store/<domain>/signals/ads_meta/`. Add a capture-side
  junk filter (drop `{{template}}` + empty copy). This is durable State/Signal capture — fits the engine.
- **Cluster → keep the workflow as a recipe** (`workflow.js` here is the template). The cluster-map is
  **Judgment-layer synthesis** (angles / "trending" / relevance are reader-relative) → stays
  experiment/project-side, never the shared store. Matches the judgments-out line.
- **Track B (Google) stays optional/deferred** — see below.

## What the v1 produced (runs/2026-06-20/ad-cluster-map.md)

275 captured creatives (189 valid after junk drop) → **10 adversarially-verified angles**. Headline:
**the market leads with price, not transformation** — flat-rate price-transparency, explicitly
anchored against brand-name Ozempic/Wegovy/Ro/Hims, is the runaway top angle (66 creatives / 18
advertisers), overwhelmingly on Meta. Then convenience/access (cross-channel), TRT identity-restoration,
education/myth-busting, social-proof, ED split into performance-vs-destigmatization, and a distinct
"food-noise / sell-the-silence" angle.

## What worked

- **Track A (Apify/Meta) is the spine.** One actor call with a keyword Ad-Library search URL did space
  discovery *and* full-copy enrichment. 249 creatives / ~$1.35. The probe-validated load-bearing claim held.
- **The clustering bake-off earned its keep.** Two methods (freeform induction vs seeded taxonomy) →
  comparative judge → **adversarial verify killed 2 of 12 clusters**. The judge favored freeform; the
  verify pass is what makes the map trustworthy rather than plausible.
- **Corpus byproduct is real.** A ranked `/research-company` worklist fell out: Rx Pros Wellness Online
  (39×), Beyond the Scale/TrimRx (15×), Wellmedr, Dad Club Co., Taurus Medical, Mars Men, Blue Haven RX,
  Gameday Men's Health — long-tail compounding DTC brands the store doesn't have.
- **Push-not-demand discipline held** throughout; every angle is quote-grounded.

## What's weak / to fix for v2

- **Track B (Google) is asymmetric + thin.** It can't discover a space (topic→0), only enrich known
  domains, and at the capped sample (26 records) only **hims** was well-supported for channel-divergence
  (Meta = emotional/brand + new-product; Google = generic-drug keyword intent — hair-loss, anxiety). The
  finding is interesting but under-powered. v2: either drop Track B, or spend more per-domain — but it's
  credit-heavy. **Recommend: keep optional, not core.**
- **Junk rate 31%** (86/275): `{{product.brand}}` dynamic-template placeholders + empty Google image-ads.
  Move the filter capture-side so the corpus is clean before clustering.
- **Keying needs the store's own aliases.** Legal-entity vs brand-name gap (Hims Inc. / Roman Health
  Ventures Inc. / GOOD LIFE MEDS LLC) forced manual aliasing → only 21% auto-keyed. The store already
  holds `aliases` + `legal_entity` in `profile.md`; enrich the seed with those for better auto-keying.
- **"Trending" is not yet real** — v1 is prevalent-now (by decision). Persisting per-company envelopes
  to the store leaves the time-axis open: a repeat run could diff for genuinely rising/new angles.
- **Minor:** the workflow's `args.out` came through `undefined` (the synth wrote to the run's canonical
  home anyway). Trivial arg-passing fixup.

## Open / next (human-gated, spends)

1. **Graduate `tools/ad_library.py`** (capture) + commit `workflow.js` as the cluster recipe.
2. **Capture the worklist** — run `/research-company` on the top propose-capture brands (Rx Pros
   Wellness Online, Beyond the Scale/TrimRx, Wellmedr, Dad Club Co., Taurus Medical, Mars Men …).
3. **Decide Track B's fate** — defer, or invest in deeper Google enrichment.
4. **Repeat-capture for true trending** — only if a consumer needs the velocity.
