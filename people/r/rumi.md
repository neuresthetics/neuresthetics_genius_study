---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA9)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-20, by: "Grok Bot", summary: "AA9 audit fix: Mas̄navī dated c.1258 at 0.5 by the start of its composition range (Iranica S3; Mojaddedi S4), alternative 1262."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA9, order P32: F 3, rank 217). Source: Britannica scholars edition, signed by Annemarie Schimmel (read in full). Lasting: his lyric poetry (Dīvān-e Shams), begun after Shams disappeared in 1247 ('This experience of love, longing, and loss turned Rūmī into a poet'), and the Mas̄navī, which 'widely influenced mystical thought and literature throughout the Muslim world' (S1); 'By the end of the 20th century, his popularity had become a global phenomenon' (S1). Composition range (RQ-Z9-N1): lyrics from 1247; the Mas̄navī begun c.1258 at 0.5 (after Ṣalāḥ al-Dīn's death in 1258, S4; Book I finished about 660/1262, S3), alternative 1262, and worked on until his death in 1273; span 1247–1273 at 0.5, age 40. Worldview: ISLAM at 0.5 (scholarly_reconstruction: 'the greatest Sufi mystic'; S1); no own words quoted, so A UNKNOWN (P19); not a scientist; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: rumi
  display_name: "Rumi"
  roster:
    canonical_name: "Rumi"
    rank: 217
    F: 3
    models: [Gemini, GPT, Grok]
    band: "core (3–4)"
    status: "core"
    field: "poetry"
    field_bucket: "literature"
  full_name: {value: "Jalāl al-Dīn Rūmī", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  native_name: {value: UNKNOWN, how_known: "Persian script not printed in S1."}
  aliases:
    - {name: "Mawlānā", kind: "title or honorific"}
    - {name: "Jalal al-Din al-Rumi", kind: "transliteration"}

basics:
  birth:
    date: {value: "1207-09-30", certainty: 0.5, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica: 'born c. September 30, 1207'."}
    place: {value: "Balkh", modern_name: "Balkh, Afghanistan", polity_then: "UNKNOWN", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica: 'Balkh [now in Afghanistan]'."}
  death:
    date: {value: "1273-12-17", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "Konya", modern_name: "Konya, Turkey", polity_then: "Seljuq sultanate of Rūm", certainty: 0.7, cites: [{source: S1, locator: "Introduction; Early life"}], how_known: "Britannica: Konya, capital under the Seljuqs."}
  first_lasting_contribution_year: {value: 1247, certainty: 0.5, cites: [{source: S1, locator: "The influence of Shams al-Dīn"}], how_known: "Shams disappeared 'one night in 1247'; 'This experience ... turned Rūmī into a poet' (S1): start of the lyric composition range (RQ-Z9-N1); inferred, 0.5."}
  era_bucket: {value: "500 to 1399", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}], how_known: "1247, and every year of his life, falls in 500 to 1399 (P2)."}
  region_of_birth: {value: "South Asia", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Balkh, Afghanistan (P3; al-Biruni precedent puts Afghanistan in South Asia)."}
  region_of_work: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "Early life; Death and legacy"}], how_known: "Konya, Anatolia (Heraclitus precedent: modern Turkey is MENA); home-region alternative South Asia."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Persian", "Arabic"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica: Persian and Arabic, 'some Turkish and less Greek'."}
  occupations: {value: ["poet", "mystic", "teacher"], certainty: 0.7, cites: [{source: S1, locator: "Introduction; Early life"}], how_known: "Britannica: succeeded his father at a madrasah in 1231."}

contribution:
  fields: {value: ["poetry", "Sufism"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Lyric poetry: the Dīvān-e Shams (ghazals, about 30,000 verses) and robāʿīyāt", year: 1247, kind: "body of work", lasting: "'famous for his lyrics'; 'By the end of the 20th century, his popularity had become a global phenomenon, with his poetry achieving a wide circulation in western Europe and the United States' (S1)", certainty: 0.5, cites: [{source: S1, locator: "Introduction; The influence of Shams al-Dīn"}], how_known: "Begun after Shams's disappearance in 1247 (S1); composition range start (RQ-Z9-N1); inferred."}
    - {value: "Mas̄navī-yi Maʿnavī ('Spiritual Couplets', nearly 26,000 couplets)", year: 1258, kind: "work", lasting: "'which widely influenced mystical thought and literature throughout the Muslim world' (S1)", certainty: 0.5, cites: [{source: S1, locator: "Introduction; The influence of Shams al-Dīn; Death and legacy"}, {source: S3, locator: "para. 3"}, {source: S4, locator: "Introduction"}], how_known: "Dated by the start of its composition range (RQ-Z9-N1): begun under Ḥusām al-Dīn after Ṣalāḥ al-Dīn's death (S1), which Mojaddedi dates to 1258 (S4), so c.1258 at 0.5. Alternative 1262: Book I was 'completed, in around 660/1262' (S3, citing Lewis pp. 221–3), and S4 says he began it 'some fifteen years after Shams had disappeared'. Worked on until shortly before his death in 1273 (S1)."}
  evidence_of_impact:
    - {value: "Mawlawiyyah order (Whirling Dervishes) organized by his disciples", kind: "institutional or technological lineage", certainty: 0.7, cites: [{source: S1, locator: "Death and legacy"}], how_known: "Britannica."}
    - {value: "Claimed by both Turkish and Persian literature; substantial influence in the Indian subcontinent", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  major_works:
    - {value: "Fīhi mā fīhi (talks)", year: UNKNOWN, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "Death and legacy"}], how_known: "Britannica; undated."}
    - {value: "Maktūbāt (letters)", year: UNKNOWN, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "Death and legacy"}], how_known: "Britannica; undated."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Greatest Sufi poet in Persian (S1).", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Father Bahāʾ al-Dīn Walad, a noted mystical theologian, author and teacher", role: "family", certainty: 0.7, cites: [{source: S1, locator: "Early life and travels"}], how_known: "Britannica."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Trained by his father and by Burhān al-Dīn Muḥaqqiq (from 1232) in mystical theory", certainty: 0.7, cites: [{source: S1, locator: "Early life and travels"}], how_known: "Britannica."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1247–1273", certainty: 0.5, cites: [{source: S1, locator: "The influence of Shams al-Dīn; Death and legacy"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: 
    value: ISLAM
    basis: scholarly_reconstruction
    certainty: 0.5
    cites: [{source: S1, locator: "Introduction; Death and legacy"}]
    how_known: "Scholar's reconstruction: Britannica (Schimmel)."
    rationale: "'the greatest Sufi mystic and poet in the Persian language' (S1); a madrasah teacher whose Mas̄navī 'shows all the different aspects of Sufism in the 13th century' (S1). Sufism is coded under ISLAM (al-Ghazali precedent). 0.5: one scholarly source, no own words quoted."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: ISLAM, reason: "Coded at 0.5 (S1)."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "No own words quoted in S1 (P19); S1: 'It is impossible to systematize his ideas, which at times contradict each other'. Lead: the Mas̄navī (Nicholson translation)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); no statement on nature read."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "The S1 description of the Mas̄navī as reflecting 'the experience of divine love' is the scholar's, not his words, so it is not listed as a statement (AA8 ruling on encyclopedia entries)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: "Muslim", certainty: 0.5, cites: [{source: S1, locator: "Early life and travels"}], how_known: "Father a mystical theologian teaching at a madrasah (S1); inferred."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1247–1273", certainty: 0.5, cites: [{source: S1, locator: "The influence of Shams al-Dīn; Death and legacy"}], how_known: "Lyric poetry from 1247 to the end of work on the Mas̄navī at his death in 1273 (begun c.1258) (P29, P30, RQ-Z9-N1); both ends inferred."}
  age_at_first_lasting_contribution: {value: 40, certainty: 0.5, cites: [{source: S1, locator: "Introduction; The influence of Shams al-Dīn"}], how_known: "1247 − 1207 = 40 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Mystical poetry (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Madrasah in Konya", role: "teacher (succeeded his father)", years: "1231–UNKNOWN", kind: "religious body", certainty: 0.7, cites: [{source: S1, locator: "Early life and travels"}], how_known: "Britannica."}
collaborators:
  - {value: "Shams al-Dīn of Tabrīz", relation: "influenced by", note: "wandering dervish, met 30 November 1244", certainty: 0.7, cites: [{source: S1, locator: "The influence of Shams al-Dīn"}], how_known: "Britannica."}
  - {value: "Ḥusām al-Dīn Chelebi", relation: "collaborator", note: "deputy; wrote down the Mas̄navī", certainty: 0.7, cites: [{source: S1, locator: "The influence of Shams al-Dīn"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 217"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Composition range inferred (1247–1273)."
    - "Worldview from scholar's reconstruction only."
  open_questions:
    - "A_locus from his own verses (Mas̄navī, Nicholson)."
    - "Mas̄navī start: c.1258 vs 1262."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Annemarie Schimmel"
    citation: "Schimmel, Annemarie, and the Editors of Encyclopaedia Britannica. 'Rūmī.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/R%C5%ABm%C4%AB/43269"
    url: "https://kids.britannica.com/scholars/article/R%C5%ABm%C4%AB/43269"
    accessed: 2026-10-19
    reliability_note: "Signed article, scholars edition, read in full."
    used_for: [identity, basics, contribution, childhood, worldview, timing, institutions, collaborators]
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
    author: "Mohammad Estelami"
    citation: "Estelami, Mohammad. 'Ḥosām-al-Din Čalabi.' Encyclopaedia Iranica (2004, updated 2017). https://www.iranicaonline.org/articles/hosam-al-din-calabi/"
    url: "https://www.iranicaonline.org/articles/hosam-al-din-calabi/"
    accessed: 2026-10-19
    reliability_note: "Signed entry, read in full."
    used_for: [contribution]
  - id: S4
    type: secondary
    kind: "book chapter"
    author: "Jawid Mojaddedi"
    citation: "Mojaddedi, Jawid (tr.). Rumi, The Masnavi, Book One. Oxford World's Classics (Oxford University Press, 2004), Introduction."
    url: "https://archive.org/details/92ab-848bb-546f-0680916811d-74c-136"
    accessed: 2026-10-19
    reliability_note: "Translator's introduction read (online copy)."
    used_for: [contribution]
---

## Summary

Rumi (1207–1273), Sufi mystic and Persian poet [S1]. Draft: ISLAM 0.5; A UNKNOWN. Not plotted.

## Life and work

Balkh; Konya [S1].

## Contribution and impact

Dīvān-e Shams from 1247; Mas̄navī from c.1258 [S1, S3, S4].

## Childhood and education

Father; Burhān al-Dīn [S1].

## Adult working worldview

Sufi (scholar's reading) [S1].

## Heritage (context only)

Muslim (inferred).

## Timing

1247–1273, age 40 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- A from own verses.

## Research log

- 2026-10-20: AA9 audit fix: Mas̄navī dated c.1258 at 0.5 by the start of its composition range (Iranica S3; Mojaddedi S4), alternative 1262.
- 2026-10-20: Read Britannica (Schimmel, scholars edition).
