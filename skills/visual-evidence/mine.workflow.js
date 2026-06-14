export const meta = {
  name: 'visual-evidence-mine',
  description: 'Blind family mining + judge over a captured company\'s visual tiles → cited evidence cards',
  phases: [
    { title: 'Mine', detail: '4 family miners, blind, in parallel' },
    { title: 'Judge', detail: 'prune + merge across families' },
  ],
}

// The blind pass that makes evidence trustworthy: each miner is a fresh context that sees only the
// listed tiles. The graduation rests on this — perception, not reputation. Prompts live here (single
// source of truth) so no protocol doc can drift from what actually runs. args: {slug, tiles[], exclusions[]}

const FAMILIES = [
  { key: 'typography_hierarchy',
    focus: 'typography & hierarchy: type scale, weight/size contrast, leading, alignment, how many distinct levels, whether copy stays legible over imagery' },
  { key: 'layout_composition_components',
    focus: 'layout, composition & component finish: grid discipline, repeated component systems, alignment, collisions, density vs whitespace, section rhythm' },
  { key: 'color_brand_imagery',
    focus: 'color, brand system & imagery: palette control, accent discipline, owned vs stock/assembled photography, coherence of the image language' },
  { key: 'iconography_illustration',
    focus: 'iconography, illustration & product graphics: icon-system consistency, custom vs clip-art, chart/diagram craft, product-render quality' },
]
const FAMILY_KEYS = FAMILIES.map((f) => f.key)

const CALIBRATION = [
  'Default down when uncertain. Generic competence is common, not high quality.',
  'Distinctiveness is not maximalism; more design is not better design.',
  'Foundations are necessary but not sufficient; genericness and broken fundamentals cap top-end claims.',
  'One visible tell per claim. Every claim must cite a visible region in one listed tile.',
  'polarity is a DIRECTION (strong | mixed | poor), not a score. Emit no site-level rating, ranking, or number.',
].join(' ')

const BLIND = [
  'BLIND READ. Judge ONLY the visible tiles. You have no web access and no prior knowledge of this company —',
  'do not infer from its name, reputation, business, or copy claims. If a tile shows a cookie banner, modal,',
  'blank/grey hero, black media card, or compositing artifact, treat it as a capture caveat, never design evidence.',
].join(' ')

const CARD_PROPS = {
  family: { type: 'string', enum: FAMILY_KEYS },
  polarity: { type: 'string', enum: ['strong', 'mixed', 'poor'] },
  page_or_region: { type: 'string' },
  tile_path: { type: 'string' },
  claim: { type: 'string' },
  visible_tells: { type: 'array', items: { type: 'string' }, minItems: 1 },
  confidence: { type: 'string', enum: ['high', 'medium', 'low'] },
  contrast_with: { type: 'string' },
}
const CARD_REQUIRED = ['family', 'polarity', 'page_or_region', 'tile_path', 'claim', 'visible_tells', 'confidence']

const MINER_SCHEMA = {
  type: 'object',
  properties: { cards: { type: 'array', items: { type: 'object', properties: CARD_PROPS, required: CARD_REQUIRED } } },
  required: ['cards'],
}

const JUDGE_SCHEMA = {
  type: 'object',
  properties: {
    accepted_cards: {
      type: 'array',
      items: {
        type: 'object',
        properties: { id: { type: 'string' }, ...CARD_PROPS },
        required: ['id', ...CARD_REQUIRED],
      },
    },
    rejected_cards: {
      type: 'array',
      items: {
        type: 'object',
        properties: { family: { type: 'string' }, tile_path: { type: 'string' }, reason: { type: 'string' } },
        required: ['tile_path', 'reason'],
      },
    },
    notes: { type: 'string' },
  },
  required: ['accepted_cards', 'rejected_cards'],
}

// args may arrive as a parsed object or a JSON string depending on how it was passed — handle both.
let input = args
if (typeof input === 'string') {
  try { input = JSON.parse(input) } catch (err) { input = {} }
}
const tiles = (input && input.tiles) || []
const tileList = tiles.map((t) => `- ${t}`).join('\n')
log(`received ${tiles.length} tiles (args was ${typeof args})`)
if (!tiles.length) {
  return { accepted_cards: [], rejected_cards: [], notes: 'no active tiles' }
}

phase('Mine')
const mined = await parallel(
  FAMILIES.map((f) => () =>
    agent(
      `${BLIND}\n\nYou are mining **${f.key}** evidence from a company's website screenshots.\n` +
        `Focus on ${f.focus}.\n\nCalibration: ${CALIBRATION}\n\n` +
        `Read these native-resolution tiles, and cite only these paths:\n${tileList}\n\n` +
        `Return 8–14 evidence cards spanning strong, mixed, and poor where the tiles support it. ` +
        `Each card: family="${f.key}", polarity, page_or_region, tile_path (one listed path), ` +
        `claim (one calibrated sentence a reader can verify in that tile), visible_tells (≥1 concrete tell), ` +
        `confidence. Optional contrast_with: another listed tile path on the same site.`,
      { label: `mine:${f.key}`, phase: 'Mine', schema: MINER_SCHEMA },
    ),
  ),
)
const allCards = mined.filter(Boolean).flatMap((m) => m.cards || [])
log(`mined ${allCards.length} raw cards across ${mined.filter(Boolean).length}/4 families`)

phase('Judge')
const judged = await agent(
  `${BLIND}\n\nYou are the JUDGE. Prune and merge these visual-evidence cards. Do not score or rank the site.\n\n` +
    `REJECT a card when: its tile_path is not in the active list; it depends on a modal/cookie/blank/black/artifact; ` +
    `it is vague or taste-word-only with no visible tell; it is about business, copy, or reputation rather than visuals; ` +
    `it duplicates another card without adding a new tell; or its polarity flatters generic competence or visual ambition without finish.\n` +
    `KEEP or MERGE when a reader can verify the claim in the cited tile, it carries a concrete visible tell, ` +
    `or it adds useful within-site contrast. Keep a calibrated mix of strong/mixed/poor.\n` +
    `Give each accepted card an id "<family-stem>_<NN>" (e.g. typography_01, layout_03, color_02, iconography_01).\n\n` +
    `Active tiles:\n${tileList}\n\nCards (${allCards.length}):\n${JSON.stringify(allCards, null, 2)}`,
  { label: 'judge', phase: 'Judge', schema: JUDGE_SCHEMA },
)

return {
  accepted_cards: judged.accepted_cards,
  rejected_cards: judged.rejected_cards || [],
  notes: judged.notes || '',
  mined_count: allCards.length,
}
