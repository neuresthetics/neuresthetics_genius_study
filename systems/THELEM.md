---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 7
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S9 for Jason)
  model_used: Grok Bot executor agent; direct reads of the cited pages
  collected_on: '2026-10-01'
  last_updated: '2026-10-25'
  change_log:
  - date: '2026-10-01'
    by: scripts/make_system_stubs.py
    summary: Stub created from v7.1 data book table 4 and section 7.
  - date: '2026-10-02'
    by: scripts/make_system_stubs.py
    summary: "Decision P7: E_scope note added. E is not scored in a stub; when it is, score it on the\
      \ world's order (same rules for every kind of being and event, no in-group exceptions in this-world\
      \ events). Salvation and moral community go on C_ledger."
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'Draft (systems batch S12): filled from Britannica "Thelema" (Doyle White). A BELOW_THRESHOLD;
      B 1 (0.5, alt 2); D 1 (0.5, alt 2); C, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from Britannica Thelema (Doyle White): Book of the Law 1904, True Will,
      magick, OTO/A∴A∴, Nuit/Hadit/Ra-Hoor-Khuit. Keep A BELOW_THRESHOLD; B=1 D=1; C E UNKNOWN.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill adherents/estimate gloss from existing sources (order-of-magnitude / qualitative). Axes
      unchanged.
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Score C_ledger 4 (0.7) from Britannica Thelema (True Will ethics, not cosmic ledger). A
      stays BELOW.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score E_scope 2 (0.5) from sources on file. Alternatives named.
identity:
  id: THELEM
  v7_1_number: 74
  v7_1_label: Thelema (Crowley/Ordo Templi Orientis)
  display_label: Thelema (Crowley/Ordo Templi Orientis)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: esoteric or occult tradition
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Esotericism/occultism; sometimes modern Paganism — 0.7.
  family:
    value: 'Thelema: religion of Aleister Crowley centered on The Book of the Law (1904); Do what thou
      wilt / True Will; magick'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; beliefs
    how_known: Britannica.
  parent_traditions:
    value:
    - Hermetic Order of the Golden Dawn ceremonial magic
    - Western esotericism
    - 'Asian religions (Hinduism, Buddhism, Yoga) as Crowley interests'
    - "Rabelais 'Do what thou wilt' phrase"
    certainty: 1.0
    cites:
    - source: S1
      locator: origins; beliefs
    how_known: Britannica.
  related_codes:
  - code: CHAOSM
    relation: neighbor (easily confused)
    note: Chaos Magick reacted against Thelemic dominance
  - code: WICCA
    relation: neighbor (easily confused)
    note: Gardner influenced by Crowley
  - code: SCIENT
    relation: neighbor (easily confused)
    note: Hubbard involved in Californian Thelemic group prior to Scientology
  - code: HERMET
    relation: overlaps
    note: Golden Dawn / ceremonial inheritance
origins:
  founding_era:
    value: '1904 Cairo revelation; religion developed 1900s; A∴A∴ 1907; Crowley heads British OTO 1912;
      Abbey of Thelema 1920–23'
    certainty: 1.0
    cites:
    - source: S1
      locator: origins
    how_known: Britannica.
  founding_region:
    value: 'Cairo revelation; England/Europe; OTO in Europe and North America; Abbey at Cefalù, Sicily'
    certainty: 1.0
    cites:
    - source: S1
      locator: origins
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - Aleister Crowley
    - Aiwass (claimed messenger)
    - George Cecil Jones
    - Theodor Reuss (OTO)
    - Karl Germer
    - Grady Louis McMurtry
    - Kenneth Grant (Typhonian)
    - Jack Parsons
    certainty: 1.0
    cites:
    - source: S1
      locator: origins
    how_known: Britannica.
  key_texts:
  - value: Liber AL vel Legis / The Book of the Law (1904)
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  - value: The Holy Books of Thelema (channeled collection; lesser than Liber AL)
    certainty: 1.0
    cites:
    - source: S1
      locator: origins
    how_known: Britannica.
metaphysics:
  god_nature_relation:
    value: 'Nuit, Hadit, Ra-Hoor-Khuit associated with successive aeons; Babalon; other entities (Pan).
      Theists vs atheist/symbolic readings among Thelemites.'
    stance: varies by school
    certainty: 1.0
    cites:
    - source: S1
      locator: beliefs
    how_known: Britannica.
  deity_personal:
    value: Some theists (literal deities); some atheists (symbolic).
    stance: both / disputed
    certainty: 1.0
    cites:
    - source: S1
      locator: beliefs
    how_known: Britannica.
  intervention:
    value: Crowley claimed audible delivery by Aiwass; magick causes change in conformity with Will; sex
      magic; spirit contact via ceremonial magic.
    stance: regular
    certainty: 0.7
    cites:
    - source: S1
      locator: origins; beliefs
    how_known: Britannica.
  miracles:
    value: Magick as science/art of change; not biblical miracle category.
    stance: affirmed
    certainty: 0.5
    cites:
    - source: S1
      locator: magick
    how_known: '0.5.'
  petition_and_prayer:
    value: Ceremonial contact and True Will pursuit more than petitionary prayer.
    stance: not addressed
    certainty: 0.5
    cites:
    - source: S1
      locator: beliefs
    how_known: Thin on petition.
  afterlife:
    value: Not a single afterlife doctrine in this article; Great Work / union with existence via Babalon
      (ego destruction).
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: beliefs
    how_known: Silence on afterlife.
  moral_ledger:
    value: 'True Will ethics, not cosmic ledger; Do what thou wilt / Love under will.'
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: beliefs
    how_known: Britannica.
  authority:
    value: Revelation via Aiwass / Book of the Law; Crowley as prophet; OTO/A∴A∴ initiatory degrees.
    stance: revelation
    certainty: 0.7
    cites:
    - source: S1
      locator: origins; beliefs
    how_known: Britannica.
  reserved_exemptions:
    value: Not addressed.
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
  teleology_in_nature:
    value: Aeonic history; True Will in harmony with cosmos.
    stance: immanent ends
    certainty: 0.5
    cites:
    - source: S1
      locator: beliefs
    how_known: '0.5.'
  necessity_and_freedom:
    value: Individualism / True Will discovery; not a determinism thesis.
    certainty: 0.7
    cites:
    - source: S1
      locator: beliefs
    how_known: Britannica.
lio_axes:
  A_locus:
    value: 'BELOW_THRESHOLD'
    how_known: "'Attitudes to this theology nevertheless vary among Thelemites. Some are theists and believe\
      \ that Thelema’s deities literally exist, whereas others are atheists and regard such entities as\
      \ symbolic figures' (S1)."
    note: P44(b).
  B_cause:
    value: 1
    rationale: "Crowley defined magick as 'the Science and Art of causing Change to occur in conformity\
      \ with Will'; sex magic is used 'to concentrate the Thelemite’s will to achieve specific aims'."
    certainty: 0.5
    cites: &id001
    - source: S1
      locator: Beliefs and practices
    how_known: '0.5: atheist Thelemites may read magick differently. Alternative 2.'
    alternatives:
    - value: 2
      note: Named alternative.
      cites: *id001
  C_ledger:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: ethics; Do what thou wilt
    how_known: '0.7 — True Will ethics, not cosmic ledger; moral_ledger stance none.'
    rationale: 'C=4: none. Not 3: Will is not karma law.'
    alternatives:
    - value: 3
      note: Named alternative if reading Love under will as impersonal law.
      cites:
      - source: S1
        locator: ethics
  D_authority:
    value: 1
    rationale: "'The tradition centers on a text, The Book of the Law, that Crowley claimed to have received\
      \ from a supernatural source in 1904', 'audibly delivered to him by Aiwass'."
    certainty: 0.5
    cites: &id002
    - source: S1
      locator: introduction
    - source: S1
      locator: Origins and history
    how_known: '0.5: revelation is central; no ranking against observation given. Alternative 2.'
    alternatives:
    - value: 2
      note: Named alternative.
      cites: *id002
  E_scope:
    value: 2
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — True Will individual + Aeonic cosmology'
    rationale: E=2 at 0.5.
    alternatives:
    - value: 4
      note: Named alternative if reading Liber AL as universal law.
      cites:
      - source: S1
        locator: opening
epistemology:
  value: Channeled revelation (Book of the Law); initiatory degrees; discover True Will (Great Work).
  certainty: 1.0
  cites:
  - source: S1
    locator: origins; beliefs
  how_known: Britannica.
ethics:
  value: 'Do what thou wilt shall be the whole of the Law; Love is the law, love under will; discover
    and pursue True Will — not amoral whim.'
  certainty: 1.0
  cites:
  - source: S1
    locator: beliefs
  how_known: Britannica.
practice:
  ritual_and_practice:
    value: 'Ceremonial magic; sex magic; Yoga; gnostic mass; feasts (Book of the Law delivery, Crowleymas);
      solo and OTO communal rites.'
    certainty: 1.0
    cites:
    - source: S1
      locator: beliefs
    how_known: Britannica.
  community_form:
    value: 'OTO lodges (~4000 members 2017); A∴A∴; many independent Thelemites; est. 5,000–10,000 total
      (2020).'
    certainty: 1.0
    cites:
    - source: S1
      locator: origins
    how_known: Britannica.
science:
  historical_stance:
    value: Magick defined as Science and Art of causing Change; not a science program.
    certainty: 0.7
    cites:
    - source: S1
      locator: magick
    how_known: Britannica.
  current_stance:
    value: Not addressed.
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
schools_and_variants:
- name: OTO Thelema
  form: modern
  how_it_differs: Lodge system; gnostic mass.
  lio_difference: B1 D1; A BELOW_THRESHOLD.
  certainty: 1.0
  cites:
  - source: S1
    locator: origins
- name: Typhonian Thelema (Grant)
  form: modern
  how_it_differs: 'Tantra, Advaita, Lovecraftian elements.'
  lio_difference: Same umbrella.
  certainty: 1.0
  cites:
  - source: S1
    locator: origins
- name: Independent / Tantric / witchcraft variants
  form: modern
  how_it_differs: Internet-era diversity.
  lio_difference: Same.
  certainty: 1.0
  cites:
  - source: S1
    locator: origins
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Ordo Templi Orientis / Thelemic groups; small organized occult presence
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — qualitative from listed source; not a genius-rate denominator.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 6
  P: 5
  E: 3
  V: 4
  X: 2
  total: 20
  scoring_note: 'Thelema scores low overall due to its heavy reliance on occult revelation and unverified
    magick, though it fosters individual empowerment and creative spiritual exploration.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 74 and section 7 scoring notes'
revised_rubric:
  status: not started
  L:
    score: 'TODO'
    rationale: ''
  P:
    score: 'TODO'
    rationale: ''
  E:
    score: 'TODO'
    rationale: ''
  V:
    score: 'TODO'
    rationale: ''
  X:
    score: 'TODO'
    rationale: ''
coding_guidance:
  use_when: Thelema / Book of the Law / Crowleyite Thelemic identity.
  do_not_use_when: Chaos Magick (CHAOSM). Wicca. Scientology.
  neighbors:
  - code: CHAOSM
    relation: neighbor (easily confused)
  - code: WICCA
    relation: neighbor (easily confused)
  - code: SCIENT
    relation: neighbor (easily confused)
review:
  data_quality_flags: []
  open_questions:
  - 'Adherents: Hedenborg White estimate 5,000–10,000 (2020), as reported in S1; cite directly.'
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Ethan Doyle White
  citation: 'Doyle White, Ethan. "Thelema." Encyclopaedia Britannica. https://www.britannica.com/topic/Thelema.
    Wayback Machine snapshot 2026-02-17 11:24:05 UTC: https://web.archive.org/web/20260217112405/https://www.britannica.com/topic/Thelema.'
  url: 'https://www.britannica.com/topic/Thelema'
  accessed: '2026-10-25'
  reliability_note: 'Signed article; full article read. P44(e): read in the Wayback copy (https://web.archive.org/web/20260217112405/https://www.britannica.com/topic/Thelema);
    live page not compared (live Britannica times out from the box).'
---
# Thelema (THELEM)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Thelema is the religion established by Aleister Crowley around The Book of the Law (1904 Cairo); True Will ethics; magick; OTO/A∴A∴ [S1].

## Core metaphysics

Nuit/Hadit/Ra-Hoor-Khuit theology varies theist vs symbolic; Aiwass revelation; Great Work [S1].

## Position on the LIO axes

- **A:** BELOW_THRESHOLD — theist/atheist split [S1].
- **B: 1** — magick / spirit contact [S1].
- **D: 1** — revelation / founder [S1].
- **C, E:** UNKNOWN.

## Schools and variants

OTO; Typhonian; independents [S1].

## Science

Magick as Science and Art of Change [S1].

## Coding guidance

Thelemic identity. Not CHAOSM.

## v7.1 scoring note

> THELEM (20/50) — Thelema (Crowley/Ordo Templi Orientis). Thelema scores low overall due to its heavy reliance on occult revelation and unverified magick, though it fosters individual empowerment and creative spiritual exploration.

## Open questions

- Afterlife doctrine thin in encyclopedia article.

## Research log

- Prior batch: Britannica Thelema; B D scored.
- 2026-10-25: deepened. Axes kept.
- 2026-10-25: adherents/estimate filled (qualitative).
- 2026-10-25: C_ledger scored 4.
- 2026-10-25: E_scope scored 2 (0.5).
