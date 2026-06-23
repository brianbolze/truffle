export const meta = {
  name: 'offerings-fanout-telehealth',
  description: 'Draft + adversarially verify offerings.md for the 3 remaining probe-seeded telehealth companies',
  phases: [
    { title: 'Draft', detail: 'one agent per company, from B1 seed + copied captures' },
    { title: 'Verify', detail: 'a separate adversarial agent greps every price + molecule against the source' },
    { title: 'Fix', detail: 'repair only where the verifier found defects, then re-lint' },
  ],
}

const REPO = '/Users/brianbolze/Library/Mobile Documents/com~apple~CloudDocs/Web Research'
const COMPANIES = ['ro-co', 'maximustribe-com', 'remedymeds-com']

const DRAFT_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  properties: {
    slug: { type: 'string' },
    file_written: { type: 'boolean' },
    sku_count: { type: 'integer' },
    not_stated_molecules: { type: 'array', items: { type: 'string' }, description: 'SKUs whose molecule you wrote "not stated" because no captured page states it' },
    visibility_split: { type: 'string', description: 'e.g. "8 partial, 3 on-request, 2 family"' },
    deep_blocks: { type: 'string', description: 'which block(s) earned a place, or "none earned"' },
    scope_note: { type: 'string' },
    every_price_grep_checked: { type: 'boolean' },
    self_lint: { type: 'string', enum: ['pass', 'fail'] },
  },
  required: ['slug', 'file_written', 'sku_count', 'every_price_grep_checked', 'self_lint'],
}

const VERIFY_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  properties: {
    slug: { type: 'string' },
    verdict: { type: 'string', enum: ['clean', 'defects'] },
    price_defects: { type: 'array', items: { type: 'string' }, description: 'each: the price + row + why (e.g. "$X on Foo not greppable in any capture")' },
    molecule_defects: { type: 'array', items: { type: 'string' }, description: 'molecules asserted but not page-attested for that SKU (should be "not stated")' },
    completeness_defects: { type: 'array', items: { type: 'string' }, description: 'SKUs on the pages missing from the roster, or rows with no page basis' },
    visibility_defects: { type: 'array', items: { type: 'string' } },
    canon_defects: { type: 'array', items: { type: 'string' }, description: 'any Molecule lead column or canonical-key frontmatter' },
    lint: { type: 'string', enum: ['pass', 'fail'] },
    lint_output: { type: 'string' },
    summary: { type: 'string' },
  },
  required: ['slug', 'verdict', 'lint', 'summary'],
}

const FIX_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  properties: {
    slug: { type: 'string' },
    applied: { type: 'boolean' },
    changes: { type: 'array', items: { type: 'string' } },
    relint: { type: 'string', enum: ['pass', 'fail', 'n/a'] },
    note: { type: 'string' },
  },
  required: ['slug', 'applied', 'relint'],
}

function draftPrompt(slug) {
  return [
    'You are drafting a per-SKU offerings.md for ONE telehealth company in the web-research engine.',
    'Correctness is paramount: a misattributed price or a molecule guessed from a brand name is the EXACT',
    'failure this module exists to prevent. A separate agent will adversarially verify your file against the source.',
    '',
    'Repo root (note the spaces): "' + REPO + '"  (also in $WEB_RESEARCH_HOME). cd there for every command. Use rg (ripgrep); grep -rn is the fallback.',
    'Company slug: ' + slug,
    '',
    'READ FIRST, in order:',
    '1. The settled exemplar — store/hims-com/offerings.md — match its shape EXACTLY (section order, roster columns, the Verbatim-anchors block, the earned deep block, Provenance).',
    '2. The contract — _design/2026-06-03-offerings-module.md — read "The record", "The recipe", and the prominence rules.',
    '3. The seed — experiments/2026-06-03-offerings-tournament/artifacts/B1-' + slug + '.md — a prior draft of THIS company. STARTING POINT ONLY: it predates the tightened molecule rule and may assert molecules inferred from brand names. Re-verify every molecule against the captures.',
    '4. The source of truth — store/' + slug + '/captures/2026-06-03/*.md — the verbatim captured pages. EVERYTHING in your file must trace here.',
    '5. Context — store/' + slug + '/profile.md — portfolio_shape + the family lines.',
    '',
    'WRITE store/' + slug + '/offerings.md with this EXACT structure (mirror the hims exemplar):',
    '- YAML frontmatter, doc-meta ONLY: the QUERYING pointer comment line, then schema_version: "1.0", domain: <the company domain>, captured_at: 2026-06-03. No other frontmatter.',
    '- ## Portfolio overview — brief: how the lines relate + the shape finding + a CALIBRATED prominence read. Tag each prominence claim [HIGH]/[MED]/[LOW] by signal stability (HIGH only for the company\'s own label or a corroborated hero; rotating heroes / carousel order are [LOW]). Ground every claim in a captured page.',
    '- ## Roster — the load-bearing table, complete at the indexed level. Columns EXACTLY:',
    '    | Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |',
    '  One row per offering. Kind = family or buyable. Slug = the relative URL = the within-company key (never blank; for a no-PDP item write "(no PDP — …)"). Price = verbatim WITH its footnote markers, or — for family rows. Visibility is one of {published, partial, on-request} per SKU (— for family rows). The What cell LEADS with "molecule · form · access" then a short clause.',
    '- ### Verbatim anchors — the footnotes the Price column points at (the † / * membership + dose notes that DECIDE partial vs published), quoted exactly; plus a molecule-sourcing note auditing every "not stated".',
    '- ## Deep blocks — EARNED ONLY. A rich block ONLY where a verbatim H1 / price footnote / disambiguation resolves an ambiguity a roster row cannot (e.g. a gated line whose only price is an FAQ figure; a "this is not actually TRT" disambiguation). Do NOT reproduce roster prices as blocks. If nothing earns one, write a line saying "None earned — the roster carries this company".',
    '- ## Provenance — pages read (list the capture files), scope, gated/unreachable, and a point-in-time-snapshot caveat.',
    '',
    'NON-NEGOTIABLE RULES:',
    '1. PRICE: every $ amount in your file MUST be greppable verbatim in store/' + slug + '/captures/2026-06-03/. Grep EACH before finalizing: rg -n "<price>" store/' + slug + '/captures/2026-06-03/. If it is not there, you may not write it. Cite the page each price sits on. (The known seed wart: a correct number with a fabricated location — cite the exact page.)',
    '2. MOLECULE + FORM: page-attested ONLY. If no captured page states a SKU\'s molecule, write "not stated" — NEVER infer from the brand name. Re-grep each: rg -ni "<molecule>" store/' + slug + '/captures/2026-06-03/. If the molecule is not tied to that SKU on a page, it is "not stated". (The seed wart to correct: e.g. tagging a brand "tirzepatide" when no page says so.)',
    '3. GATING IS A FINDING: a quiz/membership/app-gated SKU still gets a row — the floor that IS shown + the [partial]/[on-request] token.',
    '4. NO cross-company canonical key: no Molecule lead column, no canonical-id frontmatter. Molecule rides inside What; cross-brand grouping is query-time.',
    '',
    'BEFORE RETURNING: run  python3 scripts/offeringscheck.py --slug ' + slug + '  and fix anything it flags. It must pass (self_lint: pass).',
    'Return the structured summary. Your written file is the deliverable.',
  ].join('\n')
}

function verifyPrompt(slug) {
  return [
    'You are an ADVERSARIAL verifier. A DIFFERENT agent wrote store/' + slug + '/offerings.md; you did not write it and have no stake in it.',
    'Your job: find its defects against the source. Default to skepticism — a plausible-looking price or molecule is exactly what slips through. Author is not judge.',
    '',
    'Repo root: "' + REPO + '"  (also $WEB_RESEARCH_HOME). cd there. Use rg (fallback grep -rn).',
    'Company slug: ' + slug,
    '',
    'READ: store/' + slug + '/offerings.md (the draft, on trial) and ALL of store/' + slug + '/captures/2026-06-03/*.md (the source of truth, authoritative).',
    '',
    'RUN THESE CHECKS — do the work, do not eyeball:',
    '1. PRICE ATTESTATION (the costliest defect). Extract EVERY $ amount in the offerings.md. For each, grep it in the captures: rg -n "<amount>" store/' + slug + '/captures/2026-06-03/ . Record "FOUND on <page>" or "MISSING — defect". A price not greppable verbatim (allowing thousands-comma differences only) is a misattribution → price_defects.',
    '2. MOLECULE ATTESTATION (the exact tournament slip). For each molecule named in a What cell, grep it: rg -ni "<molecule>" store/' + slug + '/captures/2026-06-03/ . Confirm a captured page ties that molecule to THAT SKU. If a molecule is only inferable from the brand (not page-stated) and the row does NOT say "not stated" → molecule_defects. Check especially any brand whose molecule the pages never spell out — it must read "not stated".',
    '3. ROSTER COMPLETENESS. From the category/PDP captures, list the SKUs the company actually shows. Any SKU on the pages but missing from the roster, or any roster row with no page basis → completeness_defects.',
    '4. VISIBILITY. Spot-check 3 rows against the page: published (a price/floor shown) / partial (a floor shown but real all-in gated) / on-request (no price; intake/consult/quiz-gated). Mismatches → visibility_defects.',
    '5. NO CROSS-COMPANY CANON: confirm no standalone Molecule column and no canonical-key frontmatter → canon_defects if present.',
    '6. LINT: run  python3 scripts/offeringscheck.py --slug ' + slug + '  and put its verbatim output in lint_output; lint = pass/fail.',
    '',
    'Return the structured verdict. verdict = "clean" ONLY if checks 1–6 all pass with ZERO defects; else "defects" with specific, cold-actionable items (cite the exact price/molecule/SKU + the page).',
  ].join('\n')
}

function fixPrompt(slug, verify) {
  return [
    'A draft store/' + slug + '/offerings.md was adversarially verified and DEFECTS were found. Fix them — minimally, and faithfully to the captured source. Do not rewrite beyond the defects.',
    '',
    'Repo root: "' + REPO + '"  (also $WEB_RESEARCH_HOME). cd there. Use rg.',
    'Company slug: ' + slug,
    '',
    'The verifier\'s findings (JSON):',
    JSON.stringify(verify, null, 2),
    '',
    'For each defect, open store/' + slug + '/offerings.md and the source store/' + slug + '/captures/2026-06-03/*.md, and ground every change in a captured page:',
    '- MISSING price → find the correct verbatim string on a page and cite it, or remove the unsupported price (use the floor that IS shown, or "— (not captured)"). Never invent.',
    '- Molecule inferred from brand → change to "not stated" unless you can grep it tied to that SKU on a page.',
    '- Missing SKU → add the row from the page. Unfounded row → remove it.',
    '- Wrong visibility → correct per the page evidence.',
    '',
    'Then re-run  python3 scripts/offeringscheck.py --slug ' + slug + '  — it MUST pass. Return what you changed + the relint result.',
  ].join('\n')
}

log('Fan-out: ' + COMPANIES.join(', ') + ' — draft → adversarial verify → fix-if-needed')

const results = await pipeline(
  COMPANIES,
  (slug) => agent(draftPrompt(slug), { label: 'draft:' + slug, phase: 'Draft', schema: DRAFT_SCHEMA }),
  (draft, slug) => agent(verifyPrompt(slug), { label: 'verify:' + slug, phase: 'Verify', schema: VERIFY_SCHEMA }).then((v) => ({ slug, draft, verify: v })),
  async (vr, slug) => {
    const clean = vr.verify && vr.verify.verdict === 'clean' && vr.verify.lint === 'pass'
    if (clean) return { slug, draft: vr.draft, verify: vr.verify, fix: { slug, applied: false, relint: 'pass', note: 'clean on first pass' } }
    const fix = await agent(fixPrompt(slug, vr.verify), { label: 'fix:' + slug, phase: 'Fix', schema: FIX_SCHEMA })
    return { slug, draft: vr.draft, verify: vr.verify, fix }
  }
)

return results.filter(Boolean)
