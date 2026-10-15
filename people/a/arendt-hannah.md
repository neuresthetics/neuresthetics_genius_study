---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch F)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-15
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch F, order P32: F 5, rank 34). Basics from SEP (Tömmel and Passerin d'Entrèves) and Britannica. Worldview evidence: one private letter to Jaspers (4 March 1951) stating a 'trust' in God distinct from faith and no interest in traditional religion, read only as a Spanish quotation in Araos (Humanitas). Single private letter, secondary quotation, and no locus or nature statement: primary_system and A BELOW_THRESHOLD; B, C, D, E UNKNOWN; mid_basin UNKNOWN. Draft, not reviewed."}

identity:
  id: arendt-hannah
  display_name: "Hannah Arendt"
  roster:
    canonical_name: "Hannah Arendt"
    rank: 34
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Hannah Arendt", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "opening"}], how_known: "Name as both sources give it; a fuller birth name was not found in the sources read."}
  native_name: {value: UNKNOWN, how_known: "German in Latin script."}
  aliases:
    - {name: "Arendt-Hannah", kind: "roster alias"}
    - {name: "Hannah-Arendt", kind: "roster alias"}

basics:
  birth:
    date: {value: "1906-10-14", calendar: gregorian, certainty: 0.7, cites: [{source: S2, locator: "opening"}, {source: S1, locator: "§1 (year only)"}], how_known: "Day from Britannica alone; SEP confirms 1906."}
    place: {value: "Hannover, Germany", modern_name: "Hannover, Lower Saxony, Germany", polity_then: "German Empire (Prussia)", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "opening"}], how_known: "SEP and Britannica agree."}
  death:
    date: {value: "1975-12-04", calendar: gregorian, certainty: 0.7, cites: [{source: S2, locator: "opening"}, {source: S1, locator: "§1 (year only)"}], how_known: "Day from Britannica alone."}
    place: {value: "New York, New York, U.S.", modern_name: "New York City, United States", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "opening"}], how_known: "Two sources."}
  first_lasting_contribution_year: {value: 1951, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "Origins paragraph"}], how_known: "Earliest listed lasting contribution, The Origins of Totalitarianism (1951) (P13). The 1929 dissertation (S1 §1) is not listed: SEP treats it as background, not as itself lasting."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "From 1951 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "opening"}], how_known: "Germany (P3)."}
  region_of_work: {value: "North America", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "text"}], how_known: "New York from 1941; all listed works written in the US."}
  sex_as_recorded: {value: "female", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [English, German], certainty: 0.7, cites: [{source: S1, locator: "§1 (German dissertation; English books)"}], how_known: "SEP."}
  occupations: {value: ["political philosopher", "professor", "editor"], certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "text"}], how_known: "Two sources."}

contribution:
  fields: {value: ["political philosophy"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "opening"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "The Origins of Totalitarianism", year: 1951, kind: work, lasting: "'generated a wide-ranging debate on the nature and historical antecedents of the totalitarian phenomenon' (S1)", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Origins paragraph"}], how_known: "Two sources."}
    - {value: "The Human Condition (vita activa: labor, work, action)", year: 1958, kind: work, lasting: "'an original philosophical study' (S1)", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Human Condition paragraph"}], how_known: "Two sources."}
    - {value: "Eichmann in Jerusalem; the 'banality of evil'", year: 1963, kind: work, lasting: "coined 'banality of evil' (S1)", certainty: 1.0, cites: [{source: S1, locator: "opening; §6.1"}, {source: S2, locator: "Eichmann paragraph"}], how_known: "Two sources."}
    - {value: "The Life of the Mind (thinking, willing, judging), unfinished, published 1978", year: 1975, kind: work, lasting: "'her last major philosophical work' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "last paragraph"}], how_known: "Posthumous: dated by the death year, as no later documented act in life was read (P30). Two volumes complete at her death (S1)."}
  evidence_of_impact:
    - {value: "Origins became 'a classic' (SEP)", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "SEP: 'one of the most influential political philosophers of the twentieth century'.", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}

childhood:
  family_religion: {value: "German-Jewish family", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP; family practice not stated."}
  family_religious_practice: {value: TODO}
  parents_and_household: []
  household_circumstances: {value: "Grew up in Hannover and Königsberg", certainty: 0.7, cites: [{source: S2, locator: "second paragraph"}], how_known: "Britannica."}
  schooling:
    - {value: "Universities of Marburg (with Heidegger), Freiburg and Heidelberg (with Jaspers); doctorate, Der Liebesbegriff bei Augustin", stage: university, run_by: "state or municipal", years: "1924–1929", ages: "18–23", certainty: 0.5, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "second paragraph"}], how_known: "Start 1924 from Britannica. End year conflicts: SEP gives 1929 for the dissertation, Britannica 1928 for the degree (P25: 0.5)."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1951–1975", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: BELOW_THRESHOLD, how_known: "Only the 1951 private letter to Jaspers, known here through a Spanish quotation (S3).", note: "Single private letter; secondary quotation; translation of a translation."}
  primary_system:
    value: BELOW_THRESHOLD
    how_known: "One private letter to Jaspers (4 March 1951), read only as quoted in Spanish by Araos (S3): a 'trust' in God, 'distinct from faith', and traditional religion, 'Jewish or Christian', no longer interests her. A single private letter is below 0.5 unless a scholar backs a reading (§3); Araos backs 'creía en Dios', but that names no system."
    note: "The letter supports belief in God of some kind but excludes JUDA and CHRIST as practised, and says nothing on revelation, creation or intervention. No code fits without a guess. Coder's call: BELOW_THRESHOLD."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: JUDA, reason: "Jewish identity is central to her writing, but the 1951 letter says traditional Jewish religion no longer interests her. Rejected (heritage, not worldview)."}
    - {code: CHRIST, reason: "Same letter; Augustine dissertation is scholarship, not profession. Rejected."}
    - {code: DEISM, reason: "Would need a stated rejection of revelation (P27). Not found. Rejected."}
    - {code: CLTHEI, reason: "No statement on intervention or petition. Rejected."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "The 1951 letter states trust in God but nothing on where God is (S3).", note: "Single private letter via secondary quotation."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); no statement on the order of nature found in SEP or Britannica."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read."}
    D_authority: {value: UNKNOWN, how_known: "The letter says traditional religion cannot ground law (S3), which is about politics, not revelation against observation. Nothing else read."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN, which takes precedence (§6, P19)."}
  statements:
    - text: "Abro mi camino en la vida con una especie de confianza (¿infantil? Porque es incuestionada) en Dios"
      cites: [{source: S3, locator: "opening paragraph and note 1"}]
      date: "1951-03-04"
      context: "Letter to Karl Jaspers, answering his question whether Yahweh had not vanished too far from view, after he received The Origins of Totalitarianism."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "Spanish rendering by Araos, read through a search-index excerpt. Primary check pending against Hannah Arendt/Karl Jaspers, Correspondence 1926–1969, ed. Lotte Köhler and Hans Saner, trans. Robert and Rita Kimber (New York: Harcourt Brace Jovanovich, 1992), letter of 4 March 1951 (not read), or Briefwechsel 1926–1969 (Piper)."
  changes_over_life: []
  coder_notes: "Coder's call: the code stays BELOW_THRESHOLD because the only statement is one private letter, read in a Spanish secondary quotation, and it names no system. A 1965 Denktagebuch entry ('since I was seven I have always thought about God, but never reflected on God', via S3) and a published 1950 essay on religion and intellectuals (via a magazine column) were seen only in secondary excerpts and not used."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German-Jewish", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "second paragraph"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: "Jewish", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP 'German-Jewish family'."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1951–1975", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "1951 to 1975, first to last listed lasting contribution; the last is posthumous and dated by death (P29, P30), so 0.7."}
  age_at_first_lasting_contribution: {value: 45, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "opening"}], how_known: "1951 − 1906 = 45 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No scored statement."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S3, locator: "opening paragraph"}], how_known: "Only the 1951 letter, unscored."}
  worldview_during_major_work: {value: BELOW_THRESHOLD, how_known: "The 1951 letter falls in the span but is below 0.5.", note: "S3."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Philosophy doctorate; no documented exposure to proof read.", certainty: 0.5, cites: [{source: S1, locator: "§1"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "§1"}], how_known: "Nothing read."}
  circle_present: {value: "unclear", rationale: "Trust in God stated, nothing on God and nature.", certainty: 0.5, cites: [{source: S3, locator: "opening paragraph"}], how_known: "Coder's reading."}
  reading: "No reading possible."
  notes: ""

institutions:
  - {value: "University of Chicago", role: professor, years: "1963–1967", kind: university, certainty: 0.7, cites: [{source: S2, locator: "third paragraph"}], how_known: "Britannica."}
  - {value: "New School for Social Research", role: professor, years: "1967–1975", kind: university, certainty: 0.7, cites: [{source: S2, locator: "third paragraph"}, {source: S1, locator: "§1"}], how_known: "Britannica gives 'thereafter'; SEP has her teaching until death."}
collaborators:
  - {value: "Karl Jaspers", relation: teacher, note: "dissertation supervisor and lifelong correspondent", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "second paragraph"}], how_known: "Two sources."}
  - {value: "Martin Heidegger", relation: teacher, note: "teacher at Marburg; relationship", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "second paragraph"}], how_known: "Two sources."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 34"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Doctorate year: SEP 1929 (dissertation), Britannica 1928 (degree)."
    - "Arendt 1951 letter read only in Spanish secondary quotation."
  open_questions:
    - "Read the 4 March 1951 letter in the English Correspondence (Kimber trans., 1992) and the Denktagebuch; if confirmed and backed by a scholar, consider a code at 0.5."
    - "Ruling question candidate: can a stated 'trust in God' with no tradition, locus or revelation statement support any code? Coder's call for now: no (BELOW_THRESHOLD)."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Tatjana Tömmel and Maurizio Passerin d'Entrèves"
    year: 2024
    citation: "Tömmel, Tatjana, and Maurizio Passerin d'Entrèves. \"Hannah Arendt.\" Stanford Encyclopedia of Philosophy, first published 27 July 2006, substantive revision 12 February 2024. https://plato.stanford.edu/entries/arendt/."
    url: "https://plato.stanford.edu/entries/arendt/"
    accessed: 2026-10-15
    reliability_note: "Peer-reviewed reference article."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors (revised by Mindy Johnston)"
    citation: "Britannica Editors. \"Hannah Arendt.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Hannah-Arendt."
    url: "https://www.britannica.com/biography/Hannah-Arendt"
    accessed: 2026-10-15
    reliability_note: "Article body only; the AI 'Top Questions' box is not used."
    used_for: [basics, contribution, childhood, heritage, timing, institutions, collaborators]
  - id: S3
    type: secondary
    kind: journal article
    author: "Josefina Araos"
    citation: "Araos, Josefina. \"Esbozos sobre la presencia de Dios en Hannah Arendt.\" Humanitas (Pontificia Universidad Católica de Chile), no. 109."
    url: "https://www.humanitas.cl/filosofia/esbozos-sobre-la-presencia-de-dios-en-hannah-arendt"
    accessed: 2026-10-15
    reliability_note: "Scholarly essay; read only through search-index excerpts (the page and PDF did not load directly). Page numbers not seen; locators are to the opening paragraph and its note 1."
    used_for: [worldview, timing, lane_b]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Hannah Arendt

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Hannah Arendt (1906–1975), German-born American political philosopher, author of The Origins of Totalitarianism, The Human Condition and Eichmann in Jerusalem [S1, S2]. The only worldview evidence found is one private letter to Jaspers (1951), read in Spanish quotation [S3]. Draft: primary_system and A BELOW_THRESHOLD; B, C, D, E UNKNOWN; mid_basin UNKNOWN.

## Life and work

Studied with Heidegger and Jaspers; fled Germany in 1933 and France in 1941; taught in Chicago and at the New School [S1, S2].

## Contribution and impact

Origins (1951), The Human Condition (1958), Eichmann in Jerusalem (1963), The Life of the Mind (unfinished at death) [S1, S2].

## Childhood and education

German-Jewish family; Hannover and Königsberg; doctorate on Augustine [S1, S2].

## Adult working worldview

To Jaspers in 1951 she wrote of a 'trust' in God distinct from faith, and said traditional religion, Jewish or Christian, no longer interested her [S3]. One private letter, read only in secondary quotation, names no system and no locus, so nothing is scored.

## Heritage (context only)

German-Jewish [S1, S2].

## Timing

First lasting contribution 1951, at 45 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Unclear [S1].

## Open questions

- English text of the 1951 letter; Denktagebuch.

## Research log

- 2026-10-15: Read SEP and Britannica; web search found the 1951 Jaspers letter via Araos (Spanish). The Araos page and PDF did not load directly; excerpts only.
