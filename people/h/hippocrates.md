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
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch F, order P32: F 5, rank 36). Basics from Britannica (Wesley D. Smith). No text can be shown to be by Hippocrates himself: the Hippocratic Corpus 'cannot be by one person' and most of it 'not written by him' (S1). On the Sacred Disease (natural cause of epilepsy) is quoted for context but not attributed to him. His own disease theory is known only from Meno's report (reported speech). primary_system and A UNKNOWN; B BELOW_THRESHOLD; C, D, E UNKNOWN; mid_basin UNKNOWN. Undated works (P39). Draft, not reviewed."}

identity:
  id: hippocrates
  display_name: "Hippocrates"
  roster:
    canonical_name: "Hippocrates"
    rank: 36
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: medicine
    field_bucket: medicine
  full_name: {value: "Hippocrates of Cos", certainty: 0.7, cites: [{source: S1, locator: "opening ('the Asclepiad of Cos', Plato)"}], how_known: "Britannica."}
  native_name: {value: UNKNOWN, how_known: "Greek form not recorded in the source read."}
  aliases: []

basics:
  birth:
    date: {value: "-460", approx: true, calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "opening; 'Life and works'"}], how_known: "Britannica: 'c. 460 bce'; the dates 'are traditional but may well be approximately accurate' (0.5)."}
    place: {value: "Cos, Greece", modern_name: "Kos, Greece", polity_then: "Cos (Greek island polis)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; Plato calls him 'the Asclepiad of Cos'."}
  death:
    date: {value: "-375", approx: true, calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "opening; 'Life and works'"}], how_known: "Traditional date (0.5)."}
    place: {value: "Larissa, Thessaly", modern_name: "Larissa, Greece", polity_then: "Thessaly", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; later lives are 'largely traditional or imaginative' (0.5)."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "No listed contribution can be dated (P39)."}
  era_bucket: {value: "-500 to 499", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Every adult year on the traditional dates (c. 442–375 BCE) falls in '-500 to 499' (P39), at the certainty of the life dates (0.5)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Greece (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.5, cites: [{source: S1, locator: "'Life and works'"}], how_known: "Travelled 'in Greece and Asia Minor'; Cos as base (0.5)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [Greek], certainty: 0.7, cites: [{source: S1, locator: "'Life and works' (earliest Greek prose)"}], how_known: "Britannica."}
  occupations: {value: ["physician", "teacher of medicine"], certainty: 0.7, cites: [{source: S1, locator: "'Life and works'"}], how_known: "Britannica (Plato: taught students for fees)."}

contribution:
  fields: {value: ["medicine"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Theory of disease causation: undigested residues from unsuitable diet give off vapours that cause disease (reported by Meno)", year: UNKNOWN, kind: theory, lasting: "Hippocrates as the inspirational source for later medicine (S1); the specific theory is historical", certainty: 0.5, cites: [{source: S1, locator: "'Life and works' (Meno)"}], how_known: "Known only from Meno's history of medicine, as summarised by Britannica; undated."}
    - {value: "Practice and teaching of medicine at Cos, shaping the ideals and ethics of the physician", year: UNKNOWN, kind: "body of work", lasting: "'a permanent influence on the development of medicine and on the ideals and ethics of the physician' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Life and works'"}], how_known: "Britannica. The Oath is probably not his (S1)."}
  evidence_of_impact:
    - {value: "Called 'the Great Physician' (Aristotle, Politics); claimed as origin by later schools and by Galen", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S1, locator: "'Life and works'; 'Influence'"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "arguable", rationale: "Real and admired, but his own contributions cannot be separated from the Corpus (S1).", certainty: 0.5, cites: [{source: S1, locator: "'Life and works'"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Britannica: 'Asclepiad' means a family of physicians, not a temple priest; nothing on religion."}
  family_religious_practice: {value: UNKNOWN, how_known: "Nothing in the source read."}
  parents_and_household:
    - {value: "A family that had produced well-known physicians for generations (an 'Asclepiad')", role: family, certainty: 0.5, cites: [{source: S1, locator: "'Life and works'"}], how_known: "Britannica's reading of Plato's word."}
  household_circumstances: {value: UNKNOWN, how_known: "Nothing in the source read."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "Nothing."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Nothing."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Nothing."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: UNKNOWN, how_known: "Undated works (P39)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No text of his own identified (S1)."}
  primary_system: {value: UNKNOWN, how_known: "No statement of his own. The Corpus 'cannot be by one person' and most of it was 'not written by him' (S1), so its views are not his."}
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: HELLEN, reason: "Modern reconstructionist code; not for ancient Greeks by default. Rejected."}
    - {code: ATHE, reason: "On the Sacred Disease (not attributable to him) still calls all diseases 'divine'. Rejected."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing in his own words."}
    B_cause: {value: BELOW_THRESHOLD, how_known: "He is a scientist under P30 (a theory of disease causation), but that theory is known only from Meno's summary, which is reported speech and cannot score alone (§7). On the Sacred Disease states natural causes, but its author is unknown (S1).", note: "If a Corpus text were accepted as his, B would be 3 at 0.5 from working science (P35), or scored from On the Sacred Disease."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing."}
    D_authority: {value: UNKNOWN, how_known: "Nothing."}
    E_scope: {value: UNKNOWN, how_known: "Nothing in his own words (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, which takes precedence (§6, P19)."}
  statements:
    - text: "it appears to me to be nowise more divine nor more sacred than other diseases, but has a natural cause from which it originates like other affections"
      cites: [{source: S2, locator: "opening sentence"}]
      date: "-400"
      context: "Opening of On the Sacred Disease (Hippocratic Corpus), on epilepsy. Author unknown; not attributed to Hippocrates (S1). Context only; not used to score."
      axes: [B_cause]
      kind: "other"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "Francis Adams translation, Internet Classics Archive web copy, wording corrected to Adams's 'from which it originates' (the web copy prints 'from the originates', a transcription slip; fallacy_catalog audit of 64605bd). Check against Adams, The Genuine Works of Hippocrates (London: Sydenham Society, 1849), or W. H. S. Jones, Loeb vol. 2 (1923), pending. No section numbers in the web copy. Date '-400' is the archive's nominal 'Written 400 B.C.E', not a documented date."
    - text: "And these things are divine, so that there is no necessity for making a distinction, and holding this disease to be more divine than the others, but all are divine, and all human."
      cites: [{source: S2, locator: "closing section (on causes: cold, the sun, the winds)"}]
      date: "-400"
      context: "Same treatise, near the end. Context only."
      axes: [A_locus, B_cause]
      kind: "other"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "Same web copy; same pending check."
  changes_over_life: []
  coder_notes: "Coder's call: Corpus texts are treated like a work of unknown authorship, not as Hippocrates' own words, so they do not score his axes. Coder's call: Meno's report counts as reported speech."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Greek (Cos)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Nothing."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Nothing."}
  childhood_catechism: {value: UNKNOWN, how_known: "Nothing."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "Undated works (P39)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "Undated works (P39)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement of his own."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S1, locator: "'Life and works'"}], how_known: "No text of his own."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Nothing."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Nothing on his training.", certainty: 0.5, cites: [{source: S1, locator: "'Life and works'"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Life and works'"}], how_known: "Nothing."}
  circle_present: {value: "unclear", rationale: "No text of his own.", certainty: 0.5, cites: [{source: S1, locator: "'Life and works'"}], how_known: "Coder's reading."}
  reading: "No reading possible."
  notes: ""

institutions: []
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 36"}], how_known: "Study roster."}
  controversies:
    - {value: "Authorship of the Hippocratic Corpus and the Oath: most works not by him, the Oath probably not", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Life and works'"}], how_known: "Britannica."}
  data_quality_flags:
    - "Life dates traditional; later lives largely imaginative (S1)."
  open_questions:
    - "Check whether any scholar (e.g. Jouanna) attributes a specific treatise to Hippocrates himself; if so, re-read it for B."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Wesley D. Smith"
    citation: "Smith, Wesley D. \"Hippocrates.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Hippocrates."
    url: "https://www.britannica.com/biography/Hippocrates"
    accessed: 2026-10-15
    reliability_note: "Signed article by a Hippocratic scholar; Q&A header not used."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, review]
  - id: S2
    type: primary
    kind: other
    author: "Hippocratic Corpus (author unknown); trans. Francis Adams"
    citation: "On the Sacred Disease. Trans. Francis Adams. The Internet Classics Archive, MIT. From Adams, The Genuine Works of Hippocrates (London: Sydenham Society, 1849)."
    url: "https://classics.mit.edu/Hippocrates/sacred.html"
    accessed: 2026-10-15
    reliability_note: "Unofficial web copy of a named translation; the treatise's author is unknown and is not Hippocrates on current scholarship (S1). Attributed to him by tradition only."
    used_for: [worldview]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Hippocrates

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Hippocrates of Cos (c. 460–c. 375 BCE), Greek physician, traditionally the father of medicine [S1]. No surviving text can be shown to be his [S1]. Draft: primary_system and A UNKNOWN; B BELOW_THRESHOLD; mid_basin UNKNOWN.

## Life and work

Admired physician and teacher in his lifetime, named by Plato and Aristotle; travelled in Greece and Asia Minor [S1].

## Contribution and impact

Meno reports his theory that residues of bad diet give off disease-causing vapours [S1]. The Corpus was assembled later at Alexandria and is not his alone [S1].

## Childhood and education

From a family of physicians [S1].

## Adult working worldview

Not documented. On the Sacred Disease argues that epilepsy has a natural cause and that all diseases are 'divine' and 'human' alike [S2], but its author is unknown [S1], so it is not used to score him.

## Heritage (context only)

Greek, from Cos [S1].

## Timing

Undated (P39) [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Unclear [S1].

## Open questions

- Any treatise attributed to him by scholars.

## Research log

- 2026-10-15: Read Britannica (W. D. Smith) and the Adams translation of On the Sacred Disease (MIT web copy).
