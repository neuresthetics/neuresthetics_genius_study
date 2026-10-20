---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z9)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z9 audit fix (FAIL, P26; RQ-Z9-N1, v8's call on the auditor's advice): the 1387 start was cited to the biography opening, but the only '1387–1400' there is in the Top Questions box. Re-sourced to the Britannica topic article 'The Canterbury Tales' (S3, body read: 'written in Middle English in 1387–1400'). Under RQ-Z9-N1 a scholar's composition range dates a manuscript-era work (P12 start), so the span stays 1387–1400 and age 45. Retraction summary (S3) added as a lead. Not plotted."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z9, order P32: F 3, rank 170). Source: Britannica (R. M. Lumiansky, signed; opening, 'Forebears and early years'). No own-voice religious statement read: the Retraction at the end of The Canterbury Tales is a lead, not read here, and his first-person narrator 'both is and is not the poet himself' (S1). Religious themes in the poems are work, not profession (P16). Not a scientist. primary_system UNKNOWN (lead CHRIST); A, B, C, D, E UNKNOWN; mid_basin UNKNOWN. Span 1387–1400, age 45. Not plotted. Draft, not reviewed."}

identity:
  id: chaucer-geoffrey
  display_name: "Geoffrey Chaucer"
  roster:
    canonical_name: "Geoffrey Chaucer"
    rank: 170
    F: 3
    models: [Claude, Gemini, Grok]
    band: "core (3–4)"
    status: "core"
    field: "literature"
    field_bucket: "literature"
  full_name: {value: "Geoffrey Chaucer", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  native_name: {value: "Geffrey Chaucer", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Middle English spelling the coder's."}
  aliases:
    - {name: "Chaucer-Geoffrey", kind: "roster alias"}

basics:
  birth:
    date: {value: "1342", certainty: 0.5, cites: [{source: S1, locator: "Forebears and early years"}], how_known: "Britannica: 'c. 1342/43'; 1342 or 1343 'probably a closer guess' than c. 1340."}
    place: {value: "London", modern_name: "London, United Kingdom", polity_then: "Kingdom of England", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Britannica: 'London?'."}
  death:
    date: {value: "1400-10-25", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "London", modern_name: "London, United Kingdom", polity_then: "Kingdom of England", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1387, certainty: 0.5, cites: [{source: S3, locator: "Introduction (body)"}], how_known: "The Canterbury Tales, 'written in Middle English in 1387–1400' (Britannica topic article body, S3); a pre-print work circulated in manuscript, so the scholar's composition range is the dating event and 1387 is its start (RQ-Z9-N1, P12); earlier poems not called lasting in the body read."}
  era_bucket: {value: "500 to 1399", certainty: 1.0, cites: [{source: S3, locator: "Introduction (body)"}], how_known: "1387 (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "England, UK (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "Forebears and early years"}], how_known: "London and the court; missions abroad."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Middle English"], certainty: 0.7, cites: [{source: S1, locator: "Forebears and early years"}], how_known: "Britannica."}
  occupations: {value: ["poet", "courtier", "diplomat", "civil servant"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["poetry", "English literature"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "The Canterbury Tales", year: 1387, kind: "work", lasting: "'ranks as one of the greatest poetic works in the English language' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "Introduction (body)"}], how_known: "Lasting from the Lumiansky body (S1); dated by the topic article body, 'written in Middle English in 1387–1400', unfinished at his death (S3; RQ-Z9-N1: manuscript-era composition range; P12 start, P30 end). The 1387–1400 in the biography's Top Questions box is not cited (P26)."}
  evidence_of_impact:
    - {value: "The outstanding English poet before Shakespeare; 'the first finder of our language'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Book of the Duchess", year: 1370, kind: "book", certainty: 0.5, cites: [{source: S1, locator: "Forebears and early years"}], how_known: "Britannica: 'probably written in late 1369 or early 1370'."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Outstanding English poet before Shakespeare (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "John Chaucer, London vintner, deputy to the king's butler", role: "father", certainty: 0.7, cites: [{source: S1, locator: "Forebears and early years"}], how_known: "Britannica."}
    - {value: "Agnes Copton", role: "mother", certainty: 0.7, cites: [{source: S1, locator: "Forebears and early years"}], how_known: "Britannica."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1387–1400", certainty: 0.5, cites: [{source: S3, locator: "Introduction (body)"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "No own-voice statement read. Lead CHRIST: the Retraction closing The Canterbury Tales (not read here); poems range to 'spiritual union with God' (S1), which is work (P16), and his narrator 'both is and is not the poet himself' (S1)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Lead: Retraction; religious themes (work)."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing first-hand read (P19)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); no statement on nature read."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "A and B are UNKNOWN (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "The topic article (S3, body) summarizes the Retraction: 'Chaucer as poet and pilgrim states his conclusion that the concern for this world fades into insignificance before the prospect for the next' and asks forgiveness for writings of 'worldly vanities'; a scholar's summary of a lead, not his words read, and the speaker is poet and pilgrim (P42). Read the Retraction (Riverside Chaucer) and decide whether its first person is the author's own voice; the Treatise on the Astrolabe (1391) may hold statements on nature."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English (London merchant family)", certainty: 0.7, cites: [{source: S1, locator: "Forebears and early years"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1387–1400", certainty: 0.5, cites: [{source: S3, locator: "Introduction (body)"}], how_known: "The Canterbury Tales, 1387–1400 from the topic article body (S3); composition range accepted for a manuscript-era work (RQ-Z9-N1); P29; P12 start, range end; never past death, P30."}
  age_at_first_lasting_contribution: {value: 45, certainty: 0.5, cites: [{source: S1, locator: "Forebears and early years"}, {source: S3, locator: "Introduction (body)"}], how_known: "1387 − 1342 = 45 (P30 year difference); birth 1342 or 1343."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Poetry (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions: []
collaborators:
  - {value: "John of Gaunt", relation: "mentor or employer", note: "patron; Book of the Duchess", certainty: 0.7, cites: [{source: S1, locator: "Forebears and early years"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 170"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "No own-voice religious text read."
  open_questions:
    - "The Retraction; Treatise on the Astrolabe."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "R. M. Lumiansky"
    citation: "Lumiansky, R. M. 'Geoffrey Chaucer.' Encyclopaedia Britannica (rev. 2026). https://www.britannica.com/biography/Geoffrey-Chaucer"
    url: "https://www.britannica.com/biography/Geoffrey-Chaucer"
    accessed: 2026-10-19
    reliability_note: "Signed article; body cited, question boxes not used (P26)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, collaborators]
  - id: S2
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [review]
  - id: S3
    type: tertiary
    kind: "encyclopedia"
    author: "The Editors of Encyclopaedia Britannica"
    citation: "'The Canterbury Tales.' Encyclopaedia Britannica (Scholars edition). https://kids.britannica.com/scholars/article/The-Canterbury-Tales/484183"
    url: "https://kids.britannica.com/scholars/article/The-Canterbury-Tales/484183"
    accessed: 2026-10-19
    reliability_note: "Topic article; body read in full (introduction: 'written in Middle English in 1387–1400'); not a question box."
    used_for: [basics, contribution, worldview, timing]
---

## Summary

Geoffrey Chaucer (c. 1342–1400), poet [S1]. Draft: all worldview fields UNKNOWN (lead CHRIST). Not plotted.

## Life and work

London; court service; diplomacy [S1].

## Contribution and impact

The Canterbury Tales [S1].

## Childhood and education

Vintner's son [S1].

## Adult working worldview

Not read first-hand.

## Heritage (context only)

English [S1].

## Timing

1387–1400, age 45 [S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- The Retraction.

## Research log

- 2026-10-19: Read Britannica (Lumiansky).
