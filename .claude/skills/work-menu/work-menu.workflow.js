export const meta = {
  name: 'work-menu',
  description: 'Scan Truffle\'s scattered local evidence → blind fan-out → adversarial graduation gate → a short routed work menu',
  phases: [
    { title: 'Read', detail: 'one blind reader per surface, in parallel' },
    { title: 'Synthesize', detail: 'dedupe across surfaces, apply the focus lens, cluster' },
    { title: 'Gate', detail: 'one adversarial gate per candidate — default is leave-as-watch' },
    { title: 'Render', detail: 'route, cap at 5–7, render the two views' },
  ],
}

// WHY A HARNESS, not one window: the corpus is small enough to fit one context, but one context
// does two things badly that this skill must do well — (1) read each surface BLIND so no surface
// anchors the others, and (2) judge graduation EGOLESS so the agent that proposed a candidate is
// not the one that waves it through. Phase 1 buys the blindness; Phase 3 buys the egoless gate.
// That gate is the spine: it borrows /learning-review's posture verbatim (strip specifics, "what
// does it replace?", ≥2 sightings or a severe risk-miss, default to leave-it-as-a-watch). The
// failure it exists to prevent is over-promotion — the old triage death (345 observations → 2).
//
// Prompts live HERE (single source of truth) so SKILL.md can stay a recipe and never drift from
// what actually runs. args: { lens?: string, engineRoot?: string, roadmap?: boolean }

let input = args
if (typeof input === 'string') {
  try { input = JSON.parse(input) } catch (err) { input = {} }
}
input = input || {}
const lens = (input.lens || '').trim()
const roadmap = input.roadmap === true
const engineRoot = (input.engineRoot || '').replace(/\/+$/, '')
const at = (p) => (engineRoot ? `${engineRoot}/${p}` : p)

// ---- closed sets (kept in lockstep with the frame's buckets + the system's real routes) ----
const BUCKETS = [
  'capture-state', 'tools-signals', 'querying-consumption', 'freshness',
  'internal-tools-workflows', 'advanced-frontier', 'system-hardening',
]
const AUTHORITY = [
  'curated-high',          // a BACKLOG item, esp. [@brian] or a fired "Act when"
  'accepted-lesson',       // a graduated lesson in lessons.md
  'raw-observation',       // a single sighting — low authority, waits for a 2nd
  'in-flight-packet',      // an open or implemented-but-unclosed change packet
  'operational-telemetry', // run-record coverage / health
  'durable-intent',        // a parked frame, retro, or open design question
]
const ROUTES = [
  'agent-build-propose',   // a bounded, framed change → /agent-build-propose
  'direct-fix',            // small + obvious → just do it
  'learning-review',       // observations have piled up → /learning-review <target>
  'capture-worklist',      // coverage/freshness → /deepen-offerings or /research-company refresh
  'roadmap-watch',         // roadmap-adjacent → note it, Notion owns the ordering
  'park',                  // real but not now → park with revive_if
  'no-op',                 // leave as a watch — the honest default
]

// ---- the surfaces, each read BLIND by its own reader. Paths + the authority grain it carries. ----
const SURFACES = [
  { key: 'backlog', model: 'sonnet',
    look: 'BACKLOG.md — curated engine weaknesses/ideas/TBDs.',
    paths: ['BACKLOG.md'],
    grain: 'curated-high. Flag: any "Act when" trigger that has plausibly FIRED, and any item untouched >60 days (the file\'s own stale-cut rule). [@brian] items carry more weight.' },
  { key: 'mrl-learning', model: 'sonnet',
    look: 'Market Read Lab learning — raw observations vs accepted lessons.',
    paths: ['experiments/00-market-read-lab/learning/observations.md',
            'experiments/00-market-read-lab/learning/lessons.md',
            'experiments/00-market-read-lab/learning/passes/'],
    grain: 'observations.md rows are raw-observation (low). lessons.md entries are accepted-lesson (high) — an accepted lesson NOT yet graduated into a skill/recipe is process debt worth surfacing.' },
  { key: 'ab-learning', model: 'sonnet',
    look: 'Agentic Build learning — one file per raw sighting vs accepted lessons.',
    paths: ['experiments/01-agentic-build/learning/observations/',
            'experiments/01-agentic-build/learning/lessons.md',
            'experiments/01-agentic-build/learning/reviews/'],
    grain: 'observations/*.md are raw-observation (low). Repeats across files are the signal — count them. lessons.md = accepted-lesson; an accepted lesson with no graduated-into stamp is debt.' },
  { key: 'ab-packets', model: 'sonnet',
    look: 'Agentic Build change packets — in-flight + implemented-but-unclosed.',
    paths: ['experiments/01-agentic-build/changes/'],
    grain: 'in-flight-packet. Flag: a packet in _completed/ with no decision/close record, or an open packet stalled mid-stage (proposal with no review, review with no decision). This is the frame\'s "stale process debt".' },
  { key: 'run-records', model: 'sonnet',
    look: 'Run-record telemetry — coverage + health.',
    paths: ['store/'],
    grain: 'operational-telemetry. Look ONLY at runs/ coverage: completed captures whose captures/<date>/ has no paired runs/*.json (the unaudited-coverage hole BACKLOG already names). Do NOT read company content — this is a meta health pass, not a capture review.' },
  { key: 'design-notes', model: 'sonnet',
    look: 'Design notes, retros, parked frames, open questions.',
    paths: ['_design/', 'experiments/00-market-read-lab/_design/', 'experiments/01-agentic-build/_design/'],
    grain: 'durable-intent. Flag: an Open Question marked unresolved, a parked frame whose trigger may have fired, a retro whose fix was never made. Not every doc — only ones carrying an unmet, actionable intent.' },
]
if (roadmap) {
  SURFACES.push({ key: 'roadmap', model: 'sonnet',
    look: 'Notion roadmap (EXPLICIT roadmap mode only) — low-risk steps toward a big rock.',
    paths: ['(Notion — use the notion MCP via ToolSearch; the Truffle teamspace Roadmap database)'],
    grain: 'durable-intent. Surface ONLY low-risk, roadmap-adjacent quick wins. Do NOT re-rank the big rocks — agents do not own that ordering (frame non-goal).' })
}

const NO_FIX = 'Record the SYMPTOM, not the fix. If a patch is screaming at you, name the pressure, not the patch — routing happens later, by a different agent.'
const BLIND =
  'BLIND READ. You see ONE surface. Do not assume what the other surfaces contain, and do not invent ' +
  'cross-surface links — the synthesis step does that with all surfaces in view. Cite only what you can ' +
  'point at in your assigned paths.'

const CANDIDATE_PROPS = {
  surface: { type: 'string' },
  authority: { type: 'string', enum: AUTHORITY },
  title: { type: 'string' },
  what: { type: 'string' },
  anchor: { type: 'string' },        // file:line or a short verbatim quote — the provenance
  sighting_hint: { type: 'string' }, // "single sighting" | "repeated in N files" | "Act when fired" | ...
  bucket_hint: { type: 'string', enum: BUCKETS },
}
const READER_SCHEMA = {
  type: 'object',
  properties: { candidates: { type: 'array', items: { type: 'object', properties: CANDIDATE_PROPS, required: ['surface', 'authority', 'title', 'what', 'anchor'] } } },
  required: ['candidates'],
}

phase('Read')
log(`scanning ${SURFACES.length} surfaces${lens ? ` · lens: "${lens}"` : ' · balanced (no lens)'}`)
const read = await parallel(
  SURFACES.map((s) => () =>
    agent(
      `${BLIND}\n\nYou are the reader for the **${s.key}** surface: ${s.look}\n\n` +
        `Read these paths (relative to the repo root${engineRoot ? `, i.e. under ${engineRoot}` : ''}):\n` +
        s.paths.map((p) => `- ${at(p)}`).join('\n') +
        `\n\nAuthority grain for this surface: ${s.grain}\n\n` +
        `Return candidate work signals — a concrete gap, opportunity, or piece of process debt this ` +
        `surface genuinely supports. ${NO_FIX}\n` +
        `Each candidate: surface="${s.key}", authority (from the grain above), title (sharp, one line), ` +
        `what (1–2 concrete sentences), anchor (file:line or a short verbatim quote — the provenance a ` +
        `reader can verify), sighting_hint (single vs repeated — repeats are the signal), bucket_hint.\n` +
        `Be comprehensive but honest: no fixed count, and do NOT pad. A surface with nothing actionable ` +
        `returns an empty list — that is a valid, useful answer.`,
      { label: `read:${s.key}`, phase: 'Read', schema: READER_SCHEMA, model: s.model },
    ),
  ),
)
const raw = read.filter(Boolean).flatMap((r) => r.candidates || [])
log(`read ${raw.length} raw candidates across ${read.filter(Boolean).length}/${SURFACES.length} surfaces`)
if (!raw.length) return { brian_digest_md: 'No actionable candidates surfaced. Every surface is quiet.', cards: [], left: [], overflow_note: '' }

// ---- Phase 2: synthesize. Barrier — needs ALL candidates at once to dedupe across surfaces. ----
const SYNTH_SCHEMA = {
  type: 'object',
  properties: {
    candidates: {  // plausible enough to spend an adversarial gate on
      type: 'array',
      items: {
        type: 'object',
        properties: {
          ...CANDIDATE_PROPS,
          bucket: { type: 'string', enum: BUCKETS },
          cross_sightings: { type: 'integer' },          // how many surfaces/observations point here
          provenance: { type: 'array', items: { type: 'string' } },
          lens_fit: { type: 'string', enum: ['high', 'medium', 'low', 'na'] },
        },
        required: ['title', 'what', 'bucket', 'authority', 'cross_sightings', 'provenance'],
      },
    },
    parked: {  // not plausible enough to gate — goes straight to the honest "left" list
      type: 'array',
      items: { type: 'object', properties: { title: { type: 'string' }, reason: { type: 'string' } }, required: ['title', 'reason'] },
    },
  },
  required: ['candidates', 'parked'],
}

phase('Synthesize')
const synth = await agent(
  `You are the SYNTHESIS step. You have candidate signals read BLIND from ${SURFACES.length} different surfaces. ` +
    `Your job is to merge and weigh them — NOT to decide what graduates (a separate gate does that next).\n\n` +
    `Rules:\n` +
    `- DEDUPE across surfaces: the same underlying gap sighted on 3 surfaces is ONE candidate with cross_sightings=3, ` +
    `not three. Cross-surface agreement is the strongest signal you have — count it, merge the provenance.\n` +
    `- cross_sightings counts INDEPENDENT sightings — distinct runs, packets, or sessions. Two artifacts of the SAME ` +
    `packet, or one event echoed in a proposal and its own review, is ONE sighting, not two. Do not inflate; the gate ` +
    `will check, but get it right here.\n` +
    `- PRESERVE the authority grain. A raw-observation and a curated BACKLOG item are not the same kind of evidence; ` +
    `never let them masquerade as one queue. Keep the highest authority among merged sources, but note the mix.\n` +
    `- CLUSTER each candidate into exactly one bucket (${BUCKETS.join(', ')}).\n` +
    (lens
      ? `- FOCUS LENS: "${lens}". Set lens_fit per candidate. Weight toward the lens; do NOT hard-drop off-lens ` +
        `items unless the lens is plainly exclusive — set them lens_fit:low and let render decide.\n`
      : `- No focus lens this pass — set lens_fit:"na" for all and weigh on merit + cross_sightings.\n`) +
    `- TRIAGE, don't graduate: put genuinely plausible candidates in "candidates" (these earn an adversarial gate). ` +
    `Put clear non-starters — vague, n=1 and non-severe, already-handled, off-engine — in "parked" with a one-line reason. ` +
    `Most raw observations should park here; that is correct, and the honest half of the work. Aim to pass roughly ` +
    `the top ~12 (fewer is fine) to the gate, not everything.\n\n` +
    `Raw candidates (${raw.length}):\n${JSON.stringify(raw, null, 2)}`,
  { label: 'synthesize', phase: 'Synthesize', schema: SYNTH_SCHEMA },
)
const plausible = synth.candidates || []
log(`synthesis → ${plausible.length} plausible to gate · ${(synth.parked || []).length} parked to the left-list`)

// ---- Phase 3: the adversarial graduation gate. One INDEPENDENT agent per candidate. ----
// This is the egoless check the single-window version can't do: the agent here did NOT propose the
// candidate, and is told to default to leave-it-as-a-watch. Over-promotion dies here, by design.
const GATE_SCHEMA = {
  type: 'object',
  properties: {
    verdict: { type: 'string', enum: ['surface', 'watch'] },
    survives_stripping: { type: 'boolean' },  // strip company/packet/run specifics — does a sharp, ACTIONABLE item survive?
    replaces: { type: 'string' },             // what it retires, or "nothing — purely additive" (a weakness)
    basis: { type: 'string', enum: ['>=2-sightings', 'severe-risk-miss', 'curated-trigger-fired', 'none'] },
    justification: { type: 'string' },
  },
  required: ['verdict', 'survives_stripping', 'replaces', 'basis', 'justification'],
}
phase('Gate')
const gated = await parallel(
  plausible.map((c) => () =>
    agent(
      `You are an independent GRADUATION GATE for ONE candidate work item. You did not propose it. ` +
        `Your DEFAULT verdict is "watch" (leave it as a watch) — only return "surface" if it clears the bar.\n\n` +
        `Borrowed verbatim from /learning-review, because this is the same failure mode (over-promotion):\n` +
        `1. STRIP THE SPECIFICS — remove company names, packet ids, run slugs. Does a sharp, ACTIONABLE item ` +
        `survive? If it dissolves into one case, it is still a watch (survives_stripping=false → verdict=watch).\n` +
        `2. "WHAT DOES IT REPLACE?" — an item that RETIRES surface area beats one that only adds. Purely additive ` +
        `is suspect (mirrors Brian's simplify-don't-add reflex). Name what it retires, or admit it's additive.\n` +
        `3. BASIS TO BEAT THE WATCH DEFAULT — needs ONE of: ≥2 independent sightings (cross_sightings≥2), a SEVERE ` +
        `risk-miss (store correctness, a contract, live behavior, write authority, or Brian's decision surface), ` +
        `or a curated trigger that has genuinely fired (a BACKLOG "Act when"). A lone non-severe sighting → watch.\n\n` +
        `Be skeptical. If you're unsure, the answer is "watch". A short, honest watch list is the goal, not a long menu.\n\n` +
        `Candidate:\n${JSON.stringify(c, null, 2)}`,
      { label: `gate:${(c.title || '').slice(0, 32)}`, phase: 'Gate', schema: GATE_SCHEMA },
    ).then((v) => (v ? { candidate: c, ...v } : null)),
  ),
)
const surfaced = gated.filter(Boolean).filter((g) => g.verdict === 'surface')
const watched = gated.filter(Boolean).filter((g) => g.verdict !== 'surface')
log(`gate → ${surfaced.length} surfaced · ${watched.length} held as watch`)

// ---- Phase 4: route, cap at 5–7, render the two views. Honest overflow — no silent truncation. ----
const RENDER_SCHEMA = {
  type: 'object',
  properties: {
    brian_digest_md: { type: 'string' },  // the skim: 5–7 candidates grouped by bucket, lens-fit first
    cards: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          title: { type: 'string' }, bucket: { type: 'string', enum: BUCKETS },
          route: { type: 'string', enum: ROUTES }, why_route: { type: 'string' },
          authority: { type: 'string', enum: AUTHORITY }, cross_sightings: { type: 'integer' },
          provenance: { type: 'array', items: { type: 'string' } }, why_now: { type: 'string' },
        },
        required: ['title', 'bucket', 'route', 'provenance'],
      },
    },
    left: { type: 'array', items: { type: 'object', properties: { title: { type: 'string' }, reason: { type: 'string' } }, required: ['title', 'reason'] } },
    overflow_note: { type: 'string' },
    second_opinion: { type: 'array', items: { type: 'string' } },  // the 1–2 calls render least trusts
  },
  required: ['brian_digest_md', 'cards', 'left', 'overflow_note'],
}
phase('Render')
const parkedLeft = (synth.parked || []).map((p) => ({ title: p.title, reason: p.reason }))
const watchLeft = watched.map((g) => ({ title: g.candidate.title, reason: `gate: ${g.justification}` }))
const render = await agent(
  `You are the RENDER step. Produce Brian's work menu from the gate-surfaced candidates.\n\n` +
    `Hard rules:\n` +
    `- CAP at 5–7 cards. If more than 7 survived, rank by ${lens ? 'lens_fit, then ' : ''}cross_sightings then authority, ` +
    `keep the top 5–7, and move the rest into "left" with reason "over the 5–7 cap" — state this in overflow_note. ` +
    `NEVER silently drop a survivor.\n` +
    `- ROUTE each card to exactly one of: ${ROUTES.join(', ')}. Match the route to the work: a bounded framed change → ` +
    `agent-build-propose; small+obvious → direct-fix; piled-up observations → learning-review; coverage/freshness → ` +
    `capture-worklist; roadmap-adjacent → roadmap-watch (note, don't act); real-but-not-now → park; thin → no-op.\n` +
    `- GROUP the brian_digest_md by BUCKET (${BUCKETS.join(', ')})${lens ? ', and within a bucket lead with the highest lens_fit' : ''}. ` +
    `Per card give a sharper title, a one-line problem, why-it-matters-now, the gate verdict (ready vs watch + why), and the ` +
    `recommended route. Keep it skimmable — this is the menu, not a research report. The cards array is the drill-down audit ` +
    `trail (full provenance).\n` +
    `- Carry EVERY non-surfaced item into "left" (I pass them below), plus the honest unsurfaced count. Name in ` +
    `"second_opinion" the 1–2 surfaced-or-parked calls you trust least.\n\n` +
    `Gate-surfaced candidates (${surfaced.length}):\n${JSON.stringify(surfaced, null, 2)}\n\n` +
    `Already-left items to carry through (${parkedLeft.length + watchLeft.length}):\n${JSON.stringify([...parkedLeft, ...watchLeft], null, 2)}`,
  { label: 'render', phase: 'Render', schema: RENDER_SCHEMA },
)

const cards = render.cards || []
log(`menu → ${cards.length} cards · ${(render.left || []).length} left as watch${render.overflow_note ? ' · overflow noted' : ''}`)
return {
  brian_digest_md: render.brian_digest_md,
  cards,
  left: render.left || [],
  overflow_note: render.overflow_note || '',
  second_opinion: render.second_opinion || [],
  counts: { raw: raw.length, plausible: plausible.length, surfaced: surfaced.length, on_menu: cards.length, left: (render.left || []).length },
  lens: lens || null,
}
