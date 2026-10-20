---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA2)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "AA2 audit fixes (FAIL; v8's call on the auditor's advice, RQ-Z9-N1, P12): span 1353 -> 1355 at 0.5, alternative 1354; age 49 -> 51 (alt 50). Dated by the colophon, 'Its dictation was finished on 3rd Dhu'l-hijja 756 [December 9, 1355]' (Gibb's translation, new S3); Britannica's 'dictated in 1353' is impossible (he left Mali on 27 February 1353). The unsupported 1356 alternative and its source (Project MUSE excerpt) dropped. Not plotted."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA2, order P32: F 3, rank 183; roster status review). Basics from Britannica (students and scholars editions, body; the main site's Top Questions box not used, P26). The Rihlah was dictated to Ibn Juzayy, who 'embellished the simple prose of Ibn Baṭṭūṭah with an ornate style and fragments of poetry' (S2), so its wording is Ibn Juzayy's and its attribution to him as author is shared (P42). Dating: Britannica's Travels article says 'dictated in 1353'; a journal article (Project MUSE, 2024) has Ibn Juzayy completing it in 1356; Berkeley's ORIAS page puts the dictation after his 1354 return to Fez. The encyclopedia year is used at 0.5 (RQ-Z9-N1: a manuscript-era work dated from article text), with 1355/1356 as the alternative. No own-voice religious text read: primary_system UNKNOWN (lead ISLAM: Muslim jurist, pilgrimage, 'the traveler of Islam'); A UNKNOWN; not a scientist, B UNKNOWN; C, D, E UNKNOWN; mid_basin UNKNOWN. Span 1353, age 49. Not plotted. Draft, not reviewed."}

identity:
  id: ibn-battuta
  display_name: "Ibn Battuta"
  roster:
    canonical_name: "Ibn Battuta"
    rank: 183
    F: 3
    models: [Gemini, GPT, Grok]
    band: "core (3–4)"
    status: "review"
    field: "exploration"
    field_bucket: "exploration"
  full_name: {value: "Abu ʿAbd Allah Muhammad ibn ʿAbd Allah al-Lawati al-Tanji ibn Battutah", certainty: 0.7, cites: [{source: S1, locator: "para. 1"}], how_known: "Britannica (students)."}
  native_name: {value: "ابن بطوطة", certainty: 0.5, cites: [{source: S1, locator: "heading"}], how_known: "Arabic spelling the coder's."}
  aliases:
    - {name: "Battuta-Ibn", kind: "roster alias"}
    - {name: "Ibn-Battuta", kind: "roster alias"}
    - {name: "Ibn Battutah", kind: "other"}

basics:
  birth:
    date: {value: "1304-02-24", certainty: 0.7, cites: [{source: S1, locator: "para. 1"}], how_known: "Britannica (students)."}
    place: {value: "Tangier", modern_name: "Tangier, Morocco", polity_then: "Marinid sultanate", certainty: 0.7, cites: [{source: S1, locator: "para. 1"}], how_known: "Britannica."}
  death:
    date: {value: UNKNOWN, how_known: "Britannica: 'It has been suggested that he died in 1368/69 or 1377.'"}
    place: {value: UNKNOWN, how_known: "Not stated (buried, it is suggested, in Tangier)."}
  first_lasting_contribution_year: {value: 1355, certainty: 0.5, cites: [{source: S3, locator: "colophon"}, {source: S4, locator: "text"}], how_known: "The colophon (Gibb's translation, S3): 'Its dictation was finished on 3rd Dhu'l-hijja 756 [December 9, 1355]'. Alternative 1354, the start of the dictation range after his return to Fez in 1354 (S4; RQ-Z9-N1, P12). Britannica's 'dictated in 1353' (S2) is impossible: he left Mali only on 27 February 1353 (S3). v8's call on the auditor's advice (AA2)."}
  era_bucket: {value: "500 to 1399", certainty: 0.7, cites: [{source: S1, locator: "para. 1"}], how_known: "Born 1304; died 1368/69 or 1377; every adult year in one bucket (P39)."}
  region_of_birth: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "para. 1"}], how_known: "Morocco (P3)."}
  region_of_work: {value: "Middle East and North Africa", certainty: 0.5, cites: [{source: S2, locator: "para. 1"}], how_known: "Travels across the Muslim world; dictated at Fez."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Arabic"], certainty: 0.7, cites: [{source: S2, locator: "heading"}], how_known: "Arabic title."}
  occupations: {value: ["traveller", "jurist (qadi)"], certainty: 0.5, cites: [{source: S1, locator: "para. 1, 3"}], how_known: "Britannica: legal education; 'reportedly held the office of qadi'."}

contribution:
  fields: {value: ["travel writing", "geography"], certainty: 0.7, cites: [{source: S2, locator: "para. 1"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Travels (Riḥlah, Tuḥfat al-nuẓẓār)", year: 1355, kind: "work", lasting: "'an important document shedding light on many aspects of the social, cultural, and political history of a great part of the Muslim world'; 'a major source for the histories of these areas' (S2, body)", certainty: 0.5, cites: [{source: S2, locator: "para. 1–2"}], how_known: "Britannica; dictated to and written up by Ibn Juzayy (P42); dated by the colophon, 9 December 1355 (S3), at 0.5, alternative 1354."}
  evidence_of_impact:
    - {value: "Major source for the histories of Asia Minor, East and West Africa, the Maldives and India", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S2, locator: "para. 2"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "arguable", rationale: "The lasting work is a travel record written up by another hand (S2); originality rests on the observation, not a new idea.", certainty: 0.5, cites: [{source: S2, locator: "para. 2"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household: []
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
  working_years: {value: "1355", certainty: 0.5, cites: [{source: S3, locator: "colophon"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "No own-voice religious text read; the Rihlah's wording is Ibn Juzayy's (S2, P42). Lead ISLAM: legal education, began travelling on the pilgrimage, 'the traveler of Islam' (S1), qadi (S1)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: ISLAM, reason: "Lead: jurist, pilgrim (S1)."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing first-hand read (P19)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); no statement on nature read."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Read Gibb's translation (Hakluyt Society) for first-person passages on faith, and Dunn (1986/2012) on the dating of the dictation (1354–1355) and Ibn Juzayy's share; Dunn dates the commission to early 1356 (reported, not read), which conflicts with the colophon."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated in a citable body source (the 'family of qadis' line is in a Top Questions box, P26)."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1355", certainty: 0.5, cites: [{source: S3, locator: "colophon"}], how_known: "The one listed lasting work (P29), dated by the colophon (S3); alternative 1354 (S4)."}
  age_at_first_lasting_contribution: {value: 51, certainty: 0.5, cites: [{source: S1, locator: "para. 1"}, {source: S3, locator: "colophon"}], how_known: "1355 − 1304 = 51 (P30 year difference); 50 on the 1354 alternative."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Narrative travel account (S2).", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions: []
collaborators:
  - {value: "Ibn Juzayy", relation: "collaborator", note: "wrote up the dictated Rihlah", certainty: 0.7, cites: [{source: S2, locator: "para. 1"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Review in v8 (F 3).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 183"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Text written up by Ibn Juzayy (P42)."
    - "Britannica's 1353 conflicts with the colophon (1355)."
  open_questions:
    - "Dating of the dictation; first-person faith passages."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Britannica Editors"
    citation: "'Ibn Battutah.' Britannica (students edition). https://kids.britannica.com/students/article/Ibn-Battutah/275019"
    url: "https://kids.britannica.com/students/article/Ibn-Battutah/275019"
    accessed: 2026-10-19
    reliability_note: "Encyclopedia body, seen as a search excerpt."
    used_for: [identity, basics, worldview]
  - id: S2
    type: tertiary
    kind: "encyclopedia"
    author: "Britannica Editors"
    citation: "'Travels.' Britannica (scholars edition). https://kids.britannica.com/scholars/article/Travels/486948"
    url: "https://kids.britannica.com/scholars/article/Travels/486948"
    accessed: 2026-10-19
    reliability_note: "Encyclopedia article, read in full."
    used_for: [basics, contribution, timing, collaborators]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Ibn Battuta (dictated to Ibn Juzayy; trans. H. A. R. Gibb)"
    citation: "Ibn Battuta. Travels in Asia and Africa 1325–1354, trans. H. A. R. Gibb (1929), pp. 323–339 extract, as given in A. S. Chughtai, 'Ibn Battuta', Topics in Global History, John Jay College (CUNY), from the Fordham Medieval Sourcebook. https://jjcweb.jjay.cuny.edu/history/worldspring09/ibnbattuta.html"
    url: "https://jjcweb.jjay.cuny.edu/history/worldspring09/ibnbattuta.html"
    accessed: 2026-10-19
    reliability_note: "Course page read in full; Gibb's translation of the Mali section and colophon, unofficial web copy (§7); used for dates only."
    used_for: [basics, timing]
  - id: S4
    type: secondary
    kind: "institutional page"
    author: "ORIAS, University of California, Berkeley"
    citation: "'Writing the Rihla: 1355.' The Travels of Ibn Battuta, ORIAS. https://orias.berkeley.edu/resources-teachers/travels-ibn-battuta/journey/writing-rihla-1355"
    url: "https://orias.berkeley.edu/resources-teachers/travels-ibn-battuta/journey/writing-rihla-1355"
    accessed: 2026-10-19
    reliability_note: "Teaching resource, seen as a search excerpt."
    used_for: [basics]
  - id: S5
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [review]
---

## Summary

Ibn Battuta (1304–1368/69 or 1377), traveller [S1]. Draft: UNKNOWN (lead ISLAM). Not plotted.

## Life and work

Tangier; travels; Fez [S1, S2].

## Contribution and impact

The Rihlah [S2].

## Childhood and education

Legal and literary education [S1].

## Adult working worldview

None read (the Rihlah's wording is Ibn Juzayy's).

## Heritage (context only)

Not stated in a citable body.

## Timing

1355, age 51 (0.5) [S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Gibb in full.

## Research log

- 2026-10-19: AA2 audit fixes (FAIL; v8's call on the auditor's advice, RQ-Z9-N1, P12): span 1353 -> 1355 at 0.5, alternative 1354; age 49 -> 51 (alt 50). Dated by the colophon, 'Its dictation was finished on 3rd Dhu'l-hijja 756 [December 9, 1355]' (Gibb's translation, new S3); Britannica's 'dictated in 1353' is impossible (he left Mali on 27 February 1353). The unsupported 1356 alternative and its source (Project MUSE excerpt) dropped. Not plotted.
- 2026-10-19: Read Britannica (students, scholars); the colophon in Gibb's translation (course page); ORIAS excerpt.
