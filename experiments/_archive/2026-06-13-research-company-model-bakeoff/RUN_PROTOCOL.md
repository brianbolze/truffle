# Model run protocol

You are generating candidate `/research-company` artifacts from a frozen evidence packet.

## Hard Boundaries

- Use only the packet files and copied contract docs.
- Do not open `store/<slug>/profile.md`, `offerings.md`, or `telehealth.md`.
- Do not use live web, Firecrawl, Notion, company memory, or prior knowledge.
- Do not infer volatile facts. Prices, dates, counts, claims, certifications, and named partners must be traceable to packet evidence.
- If a fact is plausible but not packet-attested, put it in `unverified_fields` or omit it.
- Candidate outputs must live under the requested `_out/<model>/<sample_id>/` directory, never in canonical `store/`.

## Inputs

Each packet contains:

- `PACKET.md` - manifest, output request, source paths, screenshot paths, and notes.
- `contracts/` - copied schema and module contracts for this run.
- `sources/*.md` - captured page markdown.
- `logos/` - logo candidates and measured logo assets when available.
- `signals/homepage.txt` - homepage structured-layer slice when available.
- `payloads/manifest.jsonl` and map payloads when available.
- `screenshots/*.png` - symlinks to cached page screenshots.

## Output

Write the requested files:

- `profile.md` for every sample.
- `offerings.md` only when requested in `PACKET.md`.
- `telehealth.md` only when requested in `PACKET.md`.
- `RUN_NOTES.md` with:
  - packet id, model id, run date
  - files written
  - evidence files actually used
  - uncertain or weak areas
  - any contract point you intentionally left empty

Every sample requests the `logos:{}` profile module. Fill `logo_url` and `logos:` in `profile.md` from `logos/LOGO_EVIDENCE.md` and `contracts/SCHEMA.md` §Logos. If a packet provides a decoded wordmark candidate, copy it into `assets/wordmark.svg` in your output directory and set `logo_url: assets/wordmark.svg`. Use measured `logomark` and `og` assets/URLs where available. Omit a logo slot only on true absence, and record the reason in `RUN_NOTES.md`.

## Profile Guidance

Follow `contracts/SCHEMA.md` and `contracts/TAXONOMIES.md`.

Keep the profile tight. Prefer fewer, better-supported facts over a full-looking artifact with soft claims.

Use closed-set values exactly. Leave fields empty when unsupported.

For new candidates in this experiment, `logos:{}` is not optional. The point is to test the current `/research-company` capture surface, including the slide/Notion-ready brand-mark set.

For `What they offer`, every enumerated line should carry the price-visibility token:

- `[published]`
- `[partial]`
- `[on-request]`

For `Provenance`, say that pages were analyzed from a frozen packet, not freshly captured. Do not invent credit spend.

## Module Guidance

For `offerings.md`, use the copied `contracts/OFFERINGS.md`.

For `telehealth.md`, use the copied `contracts/TELEHEALTH.md`.

If the packet requests a module but the evidence is too thin, still write the file only if the contract can be obeyed. Otherwise write a short `MODULE_SKIPPED.md` explaining why.

## Quality Bar

A strong candidate is:

- traceable: the reviewer can grep the packet for every important fact
- complete enough: it captures the offering/model/audience/credibility surface
- queryable: a later `/query-companies` consumer can answer practical questions
- restrained: it does not pad, over-classify, or turn marketing emphasis into market verdicts
