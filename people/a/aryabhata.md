---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z4)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z4 audit fixes (blind audit /workspace/genius_study_audit/gs_a19c474_Z4/run1/): B basis now inference_from_work (P24; ceiling unchanged); statements verified_against 'scholarly edition' (Clark's translation read directly, not a secondary quotation); coder_notes add the Gola 49–50 condition. RQ-Z4-1: invocation carries primary and A at 0.5. Values unchanged."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z4, order P32: F 3, rank 149). Basics from MacTutor (O'Connor and Robertson). Own words from the Aryabhatiya in W. E. Clark's translation (1930) via Wikisource: Dasagitika opening invocation ('Having paid reverence to Brahman, who is one ... many ..., the true deity, the Supreme Spirit'; Clark's parenthetical glosses not counted), Gola 47 (natural account of a solar eclipse), Gola 49 ('By the grace of God'), Gola 50 (astronomy 'formerly was revealed by Svayambhu'). Van der Waerden doubts the Dasagitika's authenticity (MacTutor), so the invocation is flagged. A scientist (P30: astronomy). Span 499. Age 23 from his own statement. primary_system HINDU (0.5); A 1 (0.5, alt 2); B 3 (0.5, alt 4; P35); C, E UNKNOWN; D BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Plotted (faded). Draft, not reviewed."}

identity:
  id: aryabhata
  display_name: "Aryabhata"
  roster:
    canonical_name: "Aryabhata"
    rank: 149
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Aryabhata", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "MacTutor (Aryabhata I)."}
  native_name: {value: "Āryabhaṭa", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Standard transliteration."}
  aliases:
    - {name: "Aryabhata I", kind: "other"}

basics:
  birth:
    date: {value: "0476", calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "text (aged 23 in 499)"}], how_known: "From his own statement that he was 23 at 3600 years of the Kali age (499)."}
    place: {value: "Kusumapura (uncertain; Asmaka proposed)", modern_name: "Patna, Bihar, India (uncertain)", polity_then: "Gupta Empire", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "MacTutor: 'numerous other places proposed'."}
  death:
    date: {value: "0550", calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "MacTutor heading; conventional."}
    place: {value: UNKNOWN, how_known: "Not stated."}
  first_lasting_contribution_year: {value: 499, certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Aryabhatiya, written in 499 at age 23."}
  era_bucket: {value: "-500 to 499", certainty: 1.0, cites: [{source: S1, locator: "text"}], how_known: "499 (P2)."}
  region_of_birth: {value: "South Asia", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "India (P3), whichever birthplace."}
  region_of_work: {value: "South Asia", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Kusumapura."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Sanskrit"], certainty: 0.7, cites: [{source: S2, locator: "title page"}], how_known: "Sanskrit verse."}
  occupations: {value: ["astronomer", "mathematician"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "MacTutor."}

contribution:
  fields: {value: ["astronomy", "mathematics"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "MacTutor."}
  lasting_original_contributions:
    - {value: "Aryabhatiya", year: 499, kind: work, lasting: "place-value arithmetic, sine table, axial rotation of the Earth, natural theory of eclipses (S1)", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "MacTutor."}
  evidence_of_impact:
    - {value: "Correctly explained eclipses against the earlier belief in the demon Rahu", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "MacTutor."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founding figure of classical Indian astronomy (S1).", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}

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
  working_years: {value: "499", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Astronomy 'formerly was revealed by Svayambhu' and rescued 'by means of the boat of my own knowledge'", certainty: 0.5, cites: [{source: S2, locator: "Gola 49–50"}], how_known: "Clark translation via Wikisource."}
  primary_system:
    value: HINDU
    basis: written_profession
    certainty: 0.5
    cites: [{source: S2, locator: "Dasagitika 1; Gola 49–50"}]
    how_known: "Invocation of Brahman as 'the true deity, the Supreme Spirit'; 'By the grace of God'; Svayambhu as revealer. Translation web copy and doubted authenticity of the Dasagitika (S1), so 0.5."
    rationale: "HINDU (Brahmanical): invocation and Svayambhu. Alternative BELOW_THRESHOLD if the invocation is set aside as later."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: HINDU, reason: "Coded at 0.5."}
  lio_axes:
    A_locus:
      value: 1
      basis: written_profession
      certainty: 0.5
      cites: [{source: S2, locator: "Dasagitika 1; Gola 49"}]
      how_known: "Clark translation via Wikisource; Clark's parentheses (creator / manifestations, after Paramesvara) not counted; Dasagitika authenticity doubted (S1). 0.5."
      rationale: "Brahman 'one ... many', 'the Supreme Spirit', with 'the grace of God': a supreme deity with some immanence. Alternative 2: one-and-many read as panentheist."
      alternatives:
        - {value: 2, note: "One and many as panentheism.", cites: [{source: S2, locator: "Dasagitika 1"}]}
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      cites: [{source: S1, locator: "text"}, {source: S2, locator: "Gola 47"}]
      how_known: "A scientist with working science (P30: astronomy; natural eclipse theory against Rahu, S1; Gola 47 explains a partial eclipse by the Sun's brightness and the Moon's transparency), so B 3 at 0.5, alternative 4 (P35)."
      rationale: "P35."
      alternatives:
        - {value: 4, note: "P35 alternative.", cites: [{source: S1, locator: "text"}]}
    C_ledger: {value: UNKNOWN, how_known: "Gola 50 (disparager 'loses his good deeds and his long life') is a conventional curse, not scored."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "Gola 50 says astronomy was revealed by Svayambhu, Gola 49 that he rescued it by his own knowledge; no ranking stated."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 1 and B 3 both at 0.5, under the 0.7 bar (§6, P19)."}
  statements:
    - text: "Having paid reverence to Brahman, who is one (in causality, as the creator of the universe, but) many (in his manifestations), the true deity, the Supreme Spirit, Aryabhata sets forth three things: mathematics"
      cites: [{source: S2, locator: "Dasagitika 1"}]
      date: "499"
      context: "Opening invocation; parentheses are Clark's gloss after Paramesvara. Authenticity of the Dasagitika doubted by van der Waerden (S1)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
    - text: "By the grace of God the precious sunken jewel of true knowledge has been rescued by me, by means of the boat of my own knowledge, from the ocean which consists of true and false knowledge."
      cites: [{source: S2, locator: "Gola 49"}]
      date: "499"
      context: "Closing verses, Clark translation."
      axes: [A_locus, D_authority]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
    - text: "When the Moon eclipses the Sun even though an eighth part of the Sun is covered this is not preceptible because of the brightness of the Sun and the transparency of the Moon."
      cites: [{source: S2, locator: "Gola 47"}]
      date: "499"
      context: "Eclipse theory (spelling as in the Wikisource text)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
  changes_over_life: []
  coder_notes: "Dasagitika authenticity (van der Waerden) bears on primary and A; RQ-Z4-1 holds them at 0.5. He would leave the plot only if Gola 49–50 were also among the verses van der Waerden takes as added; MacTutor does not say which verses those are."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "499", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "The Aryabhatiya, the only lasting work (P29, P30)."}
  age_at_first_lasting_contribution: {value: 23, certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "His own statement; 499 − 476 = 23."}
  first_evidence_of_lio_type_views: {value: "499", certainty: 0.5, cites: [{source: S2, locator: "Dasagitika 1"}], how_known: "Only work."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.5, cites: [{source: S2, locator: "Dasagitika 1"}], how_known: "Same work."}
  worldview_during_major_work: {value: "HINDU", certainty: 0.5, cites: [{source: S2, locator: "Dasagitika 1"}], how_known: "Invocation."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Verse rules for computation, not proofs (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not stated."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions: []
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 149"}], how_known: "Study roster."}
  controversies:
    - {value: "Authenticity of the Dasagitika introduction (van der Waerden)", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "MacTutor."}
  data_quality_flags:
    - "Invocation from a section whose authenticity is doubted; 1930 translation via Wikisource."
  open_questions:
    - "Sanskrit text of Dasagitika 1 and Gola 49–50."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "J. J. O'Connor and E. F. Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Aryabhata I.\" MacTutor History of Mathematics Archive, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Aryabhata_I/"
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Aryabhata_I/"
    accessed: 2026-10-19
    reliability_note: "Signed biographical archive."
    used_for: [identity, basics, contribution, worldview, timing, lane_b, review]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Aryabhata, tr. Walter Eugene Clark"
    citation: "Aryabhata. The Aryabhatiya of Aryabhata, tr. W. E. Clark (Chicago, 1930), via Wikisource. https://en.wikisource.org/wiki/The_Aryabhatiya_of_Aryabhata"
    url: "https://en.wikisource.org/wiki/The_Aryabhatiya_of_Aryabhata"
    accessed: 2026-10-19
    reliability_note: "Public-domain translation, web transcription."
    used_for: [basics, worldview, timing]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [review]
---

## Summary

Aryabhata (476–c. 550), astronomer and mathematician [S1]. Draft: HINDU (0.5); A 1 (0.5, alt 2); B 3 (0.5, alt 4). Plotted (faded).

## Life and work

Kusumapura; the Aryabhatiya of 499 [S1].

## Contribution and impact

Place value, sines, Earth's rotation, eclipses [S1].

## Childhood and education

Not known.

## Adult working worldview

Invocation of Brahman; astronomy revealed by Svayambhu and rescued by his own knowledge [S2].

## Heritage (context only)

Not known.

## Timing

499, age 23 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Sanskrit text.

## Research log

- 2026-10-19: Read MacTutor; Clark translation on Wikisource.
