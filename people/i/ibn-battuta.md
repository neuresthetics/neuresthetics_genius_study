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
  first_lasting_contribution_year: {value: 1353, certainty: 0.5, cites: [{source: S2, locator: "para. 1"}, {source: S3, locator: "Introduction"}, {source: S4, locator: "text"}], how_known: "'The narrative was dictated in 1353 to Ibn Juzayy' (S2, body); dictation of a manuscript-era work from article text (RQ-Z9-N1). Alternative 1355/1356: Ibn Juzayy 'completed the manuscript' in 1356 (S3); ORIAS puts the dictation after his 1354 return (S4). Sources conflict, so 0.5."}
  era_bucket: {value: "500 to 1399", certainty: 0.7, cites: [{source: S1, locator: "para. 1"}], how_known: "Born 1304; died 1368/69 or 1377; every adult year in one bucket (P39)."}
  region_of_birth: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "para. 1"}], how_known: "Morocco (P3)."}
  region_of_work: {value: "Middle East and North Africa", certainty: 0.5, cites: [{source: S2, locator: "para. 1"}], how_known: "Travels across the Muslim world; dictated at Fez."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Arabic"], certainty: 0.7, cites: [{source: S2, locator: "heading"}], how_known: "Arabic title."}
  occupations: {value: ["traveller", "jurist (qadi)"], certainty: 0.5, cites: [{source: S1, locator: "para. 1, 3"}], how_known: "Britannica: legal education; 'reportedly held the office of qadi'."}

contribution:
  fields: {value: ["travel writing", "geography"], certainty: 0.7, cites: [{source: S2, locator: "para. 1"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Travels (Riḥlah, Tuḥfat al-nuẓẓār)", year: 1353, kind: "work", lasting: "'an important document shedding light on many aspects of the social, cultural, and political history of a great part of the Muslim world'; 'a major source for the histories of these areas' (S2, body)", certainty: 0.5, cites: [{source: S2, locator: "para. 1–2"}], how_known: "Britannica; dictated to and written up by Ibn Juzayy (P42); year 1353 at 0.5, sources conflict."}
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
  working_years: {value: "1353", certainty: 0.5, cites: [{source: S2, locator: "para. 1"}], how_known: "Equals timing.major_work_period."}
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
  coder_notes: "Read Gibb's translation (Hakluyt Society) for first-person passages on faith, and Dunn (1986/2012) on the dating of the dictation (1354–1355) and Ibn Juzayy's share; settle the 1353 vs 1355/1356 conflict."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated in a citable body source (the 'family of qadis' line is in a Top Questions box, P26)."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1353", certainty: 0.5, cites: [{source: S2, locator: "para. 1"}], how_known: "The one listed lasting work (P29); dictation year from S2, conflicting sources (S3, S4)."}
  age_at_first_lasting_contribution: {value: 49, certainty: 0.5, cites: [{source: S1, locator: "para. 1"}, {source: S2, locator: "para. 1"}], how_known: "1353 − 1304 = 49 (P30 year difference); 51 or 52 on the alternative."}
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
    - "Dictation year conflicts across sources."
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
    type: secondary
    kind: "journal article"
    author: "Project MUSE article (authors not recorded)"
    citation: "'The Colonial Adventures of Confiscated Arabic Texts: Ibn Battuta's Rihla Manuscript from North Africa to the French National Library.' Project MUSE 944675 (2024), PDF at makatib.org. https://makatib.org/wp-content/uploads/2024/12/project_muse_944675_ibn_batuta_article.pdf"
    url: "https://makatib.org/wp-content/uploads/2024/12/project_muse_944675_ibn_batuta_article.pdf"
    accessed: 2026-10-19
    reliability_note: "Journal article, seen as a search excerpt; authors not recorded."
    used_for: [basics]
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

1353, age 49 (0.5) [S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Dictation date; Gibb.

## Research log

- 2026-10-19: Read Britannica (students, scholars); MUSE article and ORIAS excerpts.
