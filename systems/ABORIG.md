---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 5
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
    summary: 'Draft (systems batch S9): filled from Britannica "The Dreaming" (editors). A 3 (0.5, alt
      2); D 1 (0.5); B, C, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from Britannica the Dreaming: mythic beings shape land and law, eternal
      presence, totemism, common life force. Keep A=3 D=1; B C E UNKNOWN.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill adherents/estimate gloss from existing sources (order-of-magnitude / qualitative). Axes
      unchanged.
identity:
  id: ABORIG
  v7_1_number: 53
  v7_1_label: Aboriginal Traditions (Australian Aboriginal Dreamtime)
  display_label: Aboriginal Traditions (Australian Aboriginal Dreamtime)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: indigenous or traditional religion
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Australian Aboriginal Dreaming as coordinated belief and action.
  family:
    value: 'Australian Aboriginal Dreaming (Dreamtime): mythic period and ongoing spiritual order in which
      mythic beings shaped land, social order, and law'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  parent_traditions:
    value:
    - "Australian Aboriginal peoples' localized traditions (many language groups)"
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  related_codes:
  - code: NATAM
    relation: neighbor (easily confused)
    note: different continents; do not merge
  - code: ANIM
    relation: overlaps
    note: common life force with animals/mythic beings
origins:
  founding_era:
    value: Dreaming as mythological period with a beginning but no foreseeable end — not a historical
      founding date
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  founding_region:
    value: Australia; localized sacred sites where mythic beings acted or metamorphosed
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - 'Mythic beings of the Dreaming (human, animal/totemic, fertility mothers, male genitors) — not historical
      founders'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  key_texts:
  - value: Oral song/narrative cycles and ritual focused on sacred places; tjurunga ritual objects
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
metaphysics:
  god_nature_relation:
    value: 'Mythic beings shaped and humanized the natural environment; metamorphosed as landforms; spiritually
      alive today. Man part of nature, sharing common life force with mythic beings and animal species.'
    stance: many gods within nature
    certainty: 0.7
    cites:
    - source: S1
      locator: opening; totemism
    how_known: Not classical theism; many mythic beings in/as land.
  deity_personal:
    value: Mythic beings credited with establishing social order and creating first people; eternal and
      spiritually alive.
    stance: personal
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: Personal agency of beings; 0.5 vs impersonal land-power reading.
  intervention:
    value: Essential quality of mythic beings undiminished; ritual at places of their actions; totem places
      humans in the Dreaming.
    stance: regular
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 ongoing spiritual presence.'
  miracles:
    value: Not framed as miracles vs natural law.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
  petition_and_prayer:
    value: Ritual focused on sacred places; not detailed as petition theology in this short article.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Thin article.
  afterlife:
    value: Indestructible identity via totem continues from beginning of time through present into future;
      not a Western heaven doctrine.
    stance: impersonal survival or eternity
    certainty: 0.5
    cites:
    - source: S1
      locator: totemism
    how_known: '0.5 mapping of continuous identity.'
  moral_ledger:
    value: Mythic beings established local social order and its laws; not an afterlife scorekeeping ledger
      in this article.
    stance: none
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: Laws yes; ledger no.
  authority:
    value: Laws established by mythic beings; ritual at sacred sites; totemic placement in the Dreaming.
    stance: tradition or ancestors
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
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
    value: Land shaped and humanized by mythic action; places of metamorphosis become sacred.
    stance: immanent ends
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5.'
  necessity_and_freedom:
    value: Not addressed.
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
lio_axes:
  A_locus:
    value: 3
    rationale: 'Eternal mythic beings shaped the land and live on in it; humans, beings and species share
      a common life force.'
    certainty: 0.5
    cites: &id001
    - source: S1
      locator: introduction
    how_known: '0.5: some beings created the first people, so 2 is the alternative.'
    alternatives:
    - value: 2
      note: Named alternative.
      cites: *id001
  B_cause:
    value: 'UNKNOWN'
    how_known: Not addressed in the sources read.
  C_ledger:
    value: 'UNKNOWN'
    how_known: Not addressed in the sources read.
  D_authority:
    value: 1
    rationale: "The mythic beings 'were credited with having established the local social order and its\
      \ “laws”'."
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction
    how_known: '0.5: law from the Dreaming, not reason.'
  E_scope:
    value: 'UNKNOWN'
    how_known: Not addressed in the sources read.
epistemology:
  value: Song/narrative and ritual knowledge of sacred places; totem as agent placing person within the
    Dreaming.
  certainty: 1.0
  cites:
  - source: S1
    locator: opening; totemism
  how_known: Britannica.
ethics:
  value: Local social order and laws established by mythic beings; details vary by group (article short).
  certainty: 0.7
  cites:
  - source: S1
    locator: opening
  how_known: Britannica.
practice:
  ritual_and_practice:
    value: Ritual focused on sacred places of mythic action/metamorphosis; tjurunga and totemic practice.
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  community_form:
    value: Localized by people who sing particular beings; not a single church.
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
science:
  historical_stance:
    value: 'Man regarded as part of nature, not fundamentally dissimilar to mythic beings or animal species.'
    certainty: 1.0
    cites:
    - source: S1
      locator: totemism
    how_known: Britannica.
  current_stance:
    value: Not addressed.
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
schools_and_variants:
- name: Local Dreaming/songline traditions (umbrella)
  form: regional
  how_it_differs: Many language-group variants; shared Dreaming/totem pattern.
  lio_difference: A=3 D=1 umbrella from short article.
  certainty: 1.0
  cites:
  - source: S1
    locator: opening
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Australian Aboriginal traditions; diverse peoples; not one membership church
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
  V: 5
  X: 3
  total: 26
  scoring_note: 'Aboriginal Traditions score moderately due to their deep connection to land and ancestors
    through Dreamtime narratives, offering rich cultural coherence but limited by oral revelation and
    lack of empirical grounding.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 53 and section 7 scoring notes'
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
  use_when: Australian Aboriginal Dreaming / Dreamtime identity.
  do_not_use_when: Native American traditions (NATAM). Generic animism without Aboriginal identity.
  neighbors:
  - code: NATAM
    relation: neighbor (easily confused)
  - code: ANIM
    relation: neighbor (easily confused)
review:
  data_quality_flags:
  - v7.1 table 4 label is truncated; v7_1_label is taken from the section 7 scoring note.
  - Short editors’ article on the Dreaming only; Britannica has no full article on Australian Aboriginal
    religion.
  open_questions:
  - A fuller source.
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Britannica Editors
  citation: 'The Editors of Encyclopaedia Britannica. "The Dreaming." Encyclopaedia Britannica. https://www.britannica.com/topic/the-Dreaming-Australian-Aboriginal-mythology.
    Wayback Machine snapshot 2026-10-07 14:39:10 UTC: https://web.archive.org/web/20261007143910/https://www.britannica.com/topic/the-Dreaming-Australian-Aboriginal-mythology.'
  url: 'https://www.britannica.com/topic/the-Dreaming-Australian-Aboriginal-mythology'
  accessed: '2026-10-25'
  reliability_note: 'Short unsigned editors’ article. P44(e): read in the Wayback copy (https://web.archive.org/web/20261007143910/https://www.britannica.com/topic/the-Dreaming-Australian-Aboriginal-mythology);
    live page timed out on 2026-10-15, so no live comparison.'
---
# Aboriginal Traditions (Australian Aboriginal Dreamtime) (ABORIG)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

The Dreaming is the mythological period (with a beginning but no foreseeable end) when mythic beings shaped the land and established social order and law; they remain spiritually alive; totemism places humans in that order [S1].

## Core metaphysics

Mythic beings eternal; landforms as metamorphoses; common life force with nature [S1].

## Position on the LIO axes

- **A_locus: 3** — sacred immanent in land/beings [S1].
- **B, C, E:** UNKNOWN.
- **D_authority: 1** — mythic law / tradition [S1].

## Schools and variants

Localized song/people traditions under one Dreaming pattern [S1].

## Science

Humans part of nature with mythic beings and animals [S1].

## Coding guidance

Australian Aboriginal Dreaming. Not NATAM.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> ABORIG (26/50) — Aboriginal Traditions (Australian Aboriginal Dreamtime). Aboriginal Traditions score moderately due to their deep connection to land and ancestors through Dreamtime narratives, offering rich cultural coherence but limited by oral revelation and lack of empirical grounding.

## Open questions

- Fuller ethnography beyond this short Britannica page.
- Petition/ritual detail.

## Research log

- 2026-10-15 (batch S9): Britannica the Dreaming; A and D scored.
- 2026-10-25: deepened classification, origins, metaphysics, practice. Axes kept.
- 2026-10-25: adherents/estimate filled (qualitative).
