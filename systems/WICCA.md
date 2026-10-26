---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 6
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
    summary: 'Draft (systems batch S9): filled from Britannica "Wicca" (Doyle White). A BELOW_THRESHOLD;
      B 1 (0.5, alt 2); C, D, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from Britannica Wicca (Doyle White): Gardner 1950s, Rede, Wheel of the
      Year, coven/solitary, varied theology. Keep B=1; A BELOW_THRESHOLD; C D E UNKNOWN.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill adherents/estimate gloss from existing sources (order-of-magnitude / qualitative). Axes
      unchanged.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score D_authority 1 (0.7) and C_ledger 4 (0.5) from sources on file (Rede; tradition/Book
      of Shadows varies). A stays BELOW; B already 1.
identity:
  id: WICCA
  v7_1_number: 52
  v7_1_label: Wicca
  display_label: Wicca
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: new religious movement
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Largest modern Pagan/Neo-Pagan religion; 0.7 vs reconstructionist.
  family:
    value: 'Wicca: modern Pagan witchcraft religion drawing on pre-Christian European inspiration and
      Western esotericism'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  parent_traditions:
    value:
    - Western esotericism (incl. Crowley readings)
    - Pre-Christian European religious imagery
    - British occult community mid-20th century
    certainty: 1.0
    cites:
    - source: S1
      locator: origins
    how_known: Britannica.
  related_codes:
  - code: HEATH
    relation: neighbor (easily confused)
    note: Heathenry is Norse-Germanic reconstructionist; not Wicca
  - code: HELLEN
    relation: neighbor (easily confused)
    note: Hellenismos is Greek reconstructionist
  - code: THELEM
    relation: neighbor (easily confused)
    note: Crowley influence ≠ Thelema identity
  - code: CHAOSM
    relation: neighbor (easily confused)
    note: different occult method
origins:
  founding_era:
    value: Publicly emerged in England in the 1950s (Gardner; Witchcraft Today 1954); precursors claimed
      1939 New Forest
    certainty: 1.0
    cites:
    - source: S1
      locator: origins
    how_known: Britannica.
  founding_region:
    value: England; spread especially through English-speaking Western countries
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; origins
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - Gerald Brosseau Gardner
    - Doreen Valiente
    - Alexander Sanders (Alexandrian)
    - Victor and Cora Anderson (Feri)
    - Zsuzsanna Budapest (Dianic)
    - Starhawk (Reclaiming)
    certainty: 1.0
    cites:
    - source: S1
      locator: origins
    how_known: Britannica.
  key_texts:
  - value: 'Witchcraft Today (Gardner, 1954)'
    certainty: 1.0
    cites:
    - source: S1
      locator: origins
    how_known: Britannica.
  - value: 'The Spiral Dance (Starhawk, 1979)'
    certainty: 1.0
    cites:
    - source: S1
      locator: origins
    how_known: Britannica.
  - value: Wiccan Rede (ethical formula)
    certainty: 1.0
    cites:
    - source: S1
      locator: beliefs
    how_known: Britannica.
metaphysics:
  god_nature_relation:
    value: "Varies: Gardner's mother goddess + horned god under an unknowable deistic divinity; also goddess\
      \ monotheism, pantheism, polytheism from many mythologies; deities may be literal or archetypal."
    stance: varies by school
    certainty: 1.0
    cites:
    - source: S1
      locator: beliefs and practices
    how_known: Britannica stresses theological diversity.
  deity_personal:
    value: Often personal goddess/god; also pantheist or symbolic readings.
    stance: varies by school
    certainty: 1.0
    cites:
    - source: S1
      locator: beliefs
    how_known: Britannica.
  intervention:
    value: 'Rituals described as magical — focusing will to bring change (healing, assistance); drawing
      down the moon (deity possession).'
    stance: regular
    certainty: 0.7
    cites:
    - source: S1
      locator: beliefs and practices
    how_known: Magic as operative; 0.7.
  miracles:
    value: Magical efficacy affirmed in ritual practice; not framed as biblical miracles.
    stance: affirmed
    certainty: 0.5
    cites:
    - source: S1
      locator: rituals
    how_known: '0.5 mapping.'
  petition_and_prayer:
    value: Invocation and magical working; deity possession in circle.
    stance: petition answered
    certainty: 0.5
    cites:
    - source: S1
      locator: rituals
    how_known: '0.5.'
  afterlife:
    value: Varies; many believe in reincarnation or Summerland.
    stance: varies by school
    certainty: 1.0
    cites:
    - source: S1
      locator: beliefs
    how_known: Britannica.
  moral_ledger:
    value: 'Wiccan Rede: If it harm none, do what you will; cursing generally rejected. Not a cosmic judgment
      ledger.'
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: Rede
    how_known: 'Ethical maxim, not afterlife ledger.'
  authority:
    value: No central authority; coven initiation/lineage in older traditions; solitary self-initiation
      books from 1970s; shared ritual more than shared belief.
    stance: varies by school
    certainty: 1.0
    cites:
    - source: S1
      locator: beliefs; origins
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
    value: Self-described nature religion; Wheel of the Year seasonal cycle; re-enchantment of nature.
    stance: immanent ends
    certainty: 0.5
    cites:
    - source: S1
      locator: beliefs; Wheel
    how_known: '0.5.'
  necessity_and_freedom:
    value: Not addressed as determinism thesis; Rede emphasizes will within harm-none limit.
    certainty: 0.7
    cites:
    - source: S1
      locator: Rede
    how_known: Thin.
lio_axes:
  A_locus:
    value: 'BELOW_THRESHOLD'
    how_known: "Members differ (P44(b)): Gardner's goddess and horned god 'created by an unknowable deistic\
      \ divinity'; others 'goddess monotheism, pantheism, or polytheistic perspectives'; and divergence\
      \ 'as to whether the deities literally exist or are instead symbolic or archetypal figures' (S1)."
  B_cause:
    value: 1
    rationale: "Rituals are 'designed to focus the willpower of the assembled Wiccans in the belief that\
      \ doing so will bring about a desired change in the physical universe'; rites invoke 'a deity to\
      \ enter and possess a coven member'."
    certainty: 0.5
    cites: &id001
    - source: S1
      locator: Beliefs and practices
    how_known: '0.5: magic is stated as a belief of the rite, not a doctrine for every Wiccan. Alternative
      2.'
    alternatives:
    - value: 2
      note: Named alternative.
      cites: *id001
  C_ledger:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: Wiccan Rede
    how_known: '0.5 — Rede harm-none is this-world ethic; Threefold Law sometimes read as impersonal return.'
    rationale: 'C=4 at 0.5: no personal divine judge as family default. Alternative 3 for Threefold Law.'
    alternatives:
    - value: 3
      note: 'Named alternative: Threefold Law as impersonal moral return (karma-like).'
      cites:
      - source: S1
        locator: Threefold Law
  D_authority:
    value: 1
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — Book of Shadows / initiatory lineages; stance varies but tradition primary for many.'
    rationale: 'D=1: tradition/lineage. Not 0: not single closed scripture for all Wicca.'
    alternatives:
    - value: 2
      note: Named alternative if coding UPG + Rede as mixed.
      cites:
      - source: S1
        locator: opening
    - value: 'BELOW_THRESHOLD'
      note: Named alternative if Gardnerian vs eclectic variance blocks score.
      cites:
      - source: S1
        locator: opening
  E_scope:
    value: 'UNKNOWN'
    how_known: Not addressed in the sources read.
epistemology:
  value: Ritual practice and initiatory/lineage knowledge prioritized over uniform doctrine; magical will;
    some historical Murray thesis now widely abandoned by historians and many Wiccans.
  certainty: 1.0
  cites:
  - source: S1
    locator: beliefs; origins
  how_known: Britannica.
ethics:
  value: 'Wiccan Rede — If it harm none, do what you will; reject cursing as unethical.'
  certainty: 1.0
  cites:
  - source: S1
    locator: Rede
  how_known: Britannica.
practice:
  ritual_and_practice:
    value: 'Circle, altar, athame/wand/chalice/pentacle/censer; skyclad or robed; eight sabbats (Wheel
      of the Year); coven initiation degrees; solitary practice majority today.'
    certainty: 1.0
    cites:
    - source: S1
      locator: beliefs and practices
    how_known: Britannica.
  community_form:
    value: 'Covens (often high priest/priestess; ideal 13) and, today, mostly solitary practitioners;
      low hundreds of thousands estimated.'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; beliefs
    how_known: Britannica.
science:
  historical_stance:
    value: Nature religion framing; not a systematic science doctrine in Britannica article.
    certainty: 0.7
    cites:
    - source: S1
      locator: beliefs
    how_known: Thin.
  current_stance:
    value: Not addressed.
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
schools_and_variants:
- name: Gardnerian Wicca
  form: modern
  how_it_differs: Gardner/Valiente initiatory lineage; goddess and horned god.
  lio_difference: B=1 umbrella; theology varies.
  certainty: 1.0
  cites:
  - source: S1
    locator: origins
- name: Alexandrian Wicca
  form: modern
  how_it_differs: Alexander Sanders tradition.
  lio_difference: Same umbrella.
  certainty: 1.0
  cites:
  - source: S1
    locator: origins
- name: Dianic Wicca
  form: modern
  how_it_differs: "Women's tradition; goddess focus (Budapest, 1971)."
  lio_difference: A may differ by goddess monotheism — not rescored here.
  certainty: 1.0
  cites:
  - source: S1
    locator: origins
- name: Reclaiming
  form: modern
  how_it_differs: Starhawk; progressive/environmentalist inflection.
  lio_difference: Same umbrella.
  certainty: 1.0
  cites:
  - source: S1
    locator: origins
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Modern Pagan religion with self-identified practitioners; survey-based estimates vary widely
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — qualitative from listed source; not a genius-rate denominator.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 7
  P: 6
  E: 5
  V: 6
  X: 3
  total: 27
  scoring_note: 'Wicca scores moderately due to its nature-centered and magical framework, offering ethical
    and communal coherence but limited by supernatural elements and subjective authority over empirical
    rigor.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 52 and section 7 scoring notes'
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
  use_when: Self-identified Wicca / Gardnerian / Alexandrian / Dianic Wiccan practice.
  do_not_use_when: Heathenry/Ásatrú (HEATH). Thelema (THELEM). Generic Neo-Pagan without Wiccan identity.
  neighbors:
  - code: HEATH
    relation: neighbor (easily confused)
  - code: THELEM
    relation: neighbor (easily confused)
  - code: CHAOSM
    relation: neighbor (easily confused)
review:
  data_quality_flags: []
  open_questions:
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Ethan Doyle White
  citation: 'Doyle White, Ethan. "Wicca." Encyclopaedia Britannica. https://www.britannica.com/topic/Wicca.
    Wayback Machine snapshot 2026-09-07 13:28:17 UTC: https://web.archive.org/web/20260907132817/https://www.britannica.com/topic/Wicca.'
  url: 'https://www.britannica.com/topic/Wicca'
  accessed: '2026-10-25'
  reliability_note: 'Signed article (historian of modern Paganism). P44(e): read in the Wayback copy (https://web.archive.org/web/20260907132817/https://www.britannica.com/topic/Wicca);
    live page timed out on 2026-10-15, so no live comparison.'
---
# Wicca (WICCA)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Wicca is the largest modern Pagan religion, publicly emerging in England in the 1950s from Gerald Gardner's circle; followers typically identify as witches [S1].

## Core metaphysics

Theology varies (goddess/god, pantheism, polytheism; literal or archetypal). Magical ritual; Rede ethics; Wheel of the Year [S1].

## Position on the LIO axes

- **A_locus:** BELOW_THRESHOLD — theology too varied for a single locus score [S1].
- **B_cause: 1** — magical working / deity invocation [S1].
- **C, D, E:** UNKNOWN.

## Schools and variants

Gardnerian, Alexandrian, Dianic, Reclaiming, Feri; mostly solitary today [S1].

## Science

Nature-religion framing; no systematic science doctrine here [S1].

## Coding guidance

Wiccan identity. Not HEATH or THELEM.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> WICCA (27/50) — Wicca. Wicca scores moderately due to its nature-centered and magical framework, offering ethical and communal coherence but limited by supernatural elements and subjective authority over empirical rigor.

## Open questions

- Whether D should stay UNKNOWN vs tradition/founder mix (0.5) — left UNKNOWN (P44).

## Research log

- 2026-10-15 (batch S9): Britannica Wicca; B scored.
- 2026-10-25: deepened classification, origins, metaphysics, ethics, practice, schools. Axes kept.
- 2026-10-25: adherents/estimate filled (qualitative).
- 2026-10-25: D/C scored.
