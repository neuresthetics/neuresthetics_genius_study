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
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z9 audit fixes (v8's calls on the auditor's advice). WEAKEN on CHRIST: p. 424 ('profess an intellectual allegiance to the Father of Lights') is others' profession, not his; his own p. 159 'Author of Nature' fits CHRIST and DEISM equally, so primary_system CHRIST 0.5 -> BELOW_THRESHOLD (leads CHRIST, DEISM). A 1 at 0.5 now rests on p. 159 alone. Notes say only the OCR was read. RQ-Z9-2: no (algebra of logic is not a theory of mind). Still plotted at A 1 / B 3."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z9, order P32: F 3, rank 172). Basics from MacTutor (O'Connor and Robertson). Own words in An Investigation of the Laws of Thought (1854; archive.org library scan, OCR read), within the span: 'all that we know of the uniformity of Nature, and all that we believe of the immutable constancy of the Author of Nature' (ch. XI, p. 159); the closing page contrasts those who acknowledge 'nothing higher than ... collective humanity' with those who 'profess an intellectual allegiance to the Father of Lights' (ch. XXII, p. 424). Not a scientist (logic and algebra; P30). primary_system CHRIST (0.5, alt DEISM); A 1 (0.5, alt 0); B 3 (0.5, alt 4) from his own statement on nature (P16); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD (A and B at 0.5). Span 1854, age 39. Plotted (A 1, B 3). Draft, not reviewed."}

identity:
  id: boole-george
  display_name: "George Boole"
  roster:
    canonical_name: "George Boole"
    rank: 172
    F: 3
    models: [Claude, DeepSeek, Gemini]
    band: "core (3–4)"
    status: "core"
    field: "mathematics-logic"
    field_bucket: "mathematics"
  full_name: {value: "George Boole", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}], how_known: "MacTutor."}
  native_name: {value: "George Boole", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}], how_known: "MacTutor."}
  aliases:
    - {name: "Boole-George", kind: "roster alias"}

basics:
  birth:
    date: {value: "1815-11-02", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}], how_known: "MacTutor."}
    place: {value: "Lincoln", modern_name: "Lincoln, United Kingdom", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}], how_known: "MacTutor."}
  death:
    date: {value: "1864-12-08", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}], how_known: "MacTutor."}
    place: {value: "Ballintemple, County Cork", modern_name: "Cork, Ireland", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}], how_known: "MacTutor."}
  first_lasting_contribution_year: {value: 1854, certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "An Investigation of the Laws of Thought (1854), 'Boole's most important work'."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "Biography"}], how_known: "1854 (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}], how_known: "England, UK (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Queen's College, Cork (Ireland)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S2, locator: "title page"}], how_known: "English text."}
  occupations: {value: ["mathematician", "logician", "professor"], certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}

contribution:
  fields: {value: ["logic", "mathematics"], certainty: 0.7, cites: [{source: S1, locator: "Summary"}], how_known: "MacTutor."}
  lasting_original_contributions:
    - {value: "Boolean algebra of logic (An Investigation of the Laws of Thought)", year: 1854, kind: "theory", lasting: "'reducing it to a simple algebra, incorporating logic into mathematics' (S1, his 'most important work')", certainty: 0.7, cites: [{source: S1, locator: "Summary; Biography"}], how_known: "MacTutor."}
  evidence_of_impact:
    - {value: "Approached logic in a new way, incorporating logic into mathematics", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Summary"}], how_known: "MacTutor."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founder of the algebra of logic (S1).", certainty: 0.7, cites: [{source: S1, locator: "Summary"}], how_known: "MacTutor."}

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
  working_years: {value: "1854", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "Laws of Thought (1854), within the span: his own words show belief in an 'Author of Nature' of 'immutable constancy' (ch. XI, p. 159), which fits CHRIST and DEISM equally. The p. 424 'profess an intellectual allegiance to the Father of Lights' describes others' profession, not his own (Z9 audit), so nothing specific favours CHRIST over DEISM. A creator is professed but no code is supported, so BELOW_THRESHOLD. Leads: CHRIST (he once meant to enter the Church, S1; the Father of Lights passage reads sympathetically) and DEISM (immutable, non-intervening Author)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Lead: early plan to enter the Church (S1); p. 424 is others' profession, not his."}
    - {code: DEISM, reason: "Lead: immutable Author of Nature; nothing on revelation read."}
  lio_axes:
    A_locus: 
      value: 1
      basis: written_profession
      certainty: 0.5
      cites: [{source: S2, locator: "ch. XI, p. 159"}]
      how_known: "Laws of Thought, within the span; indirect, so 0.5. Rests on p. 159 ('all that we believe'); p. 424 is others' profession and is not used."
      rationale: "An Author of Nature distinct from nature, whose 'immutable constancy' is a matter of his belief: a creator outside the world, 1 (constancy rather than intervention). Alternative 0."
      alternatives:
        - {value: 0, note: "Author of Nature read as fully transcendent.", cites: [{source: S2, locator: "ch. XI, p. 159"}]}
    B_cause: 
      value: 3
      basis: written_profession
      certainty: 0.5
      cites: [{source: S2, locator: "ch. XI, p. 159; ch. XXII, p. 423"}]
      how_known: "His own statement about nature (P16), within the span; he is not a scientist (P30), so this rests on his words, not on working science."
      rationale: "'the uniformity of Nature'; 'the material universe in its boundless magnitude, and pervading order, and constancy of law' (p. 423): lawful order stated, no explicit no-exception claim (P16 addendum), so 3. Alternative 4: 'immutable constancy of the Author of Nature' read as excluding exceptions."
      alternatives:
        - {value: 4, note: "Immutable constancy read as no exceptions.", cites: [{source: S2, locator: "ch. XI, p. 159"}]}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus and B_cause are scored only at 0.5, under the P4 test's 0.7 bar."}
  statements:
    - text: "It consists with all that we know of the uniformity of Nature, and all that we believe of the immutable constancy of the Author of Nature, to suppose, that in the mind, which has been endowed with such high capabilities, not only for converse with surrounding scenes, but for the knowledge of itself, and for reflection upon the laws of its own constitution, there should exist a harmony and uniformity not less real than that which the study of the physical sciences makes known to us."
      cites: [{source: S2, locator: "ch. XI, p. 159"}]
      date: "1854"
      context: "An Investigation of the Laws of Thought, opening of ch. XI (Of Secondary Propositions)."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-19
      note: "Only the archive.org OCR of the 1854 Walton and Maberly printing (Google scan) was read, not the page images; OCR slips silently corrected ('surroumling', 'lees')."
  changes_over_life: []
  coder_notes: "RQ-Z9-2 answered no (Z9 audit): his lasting item is an algebra of logic, not testable claims about organisms, so he is not a scientist; B rests on his own words. Only the archive.org OCR was read; the page images were not viewed. Ch. XIII's treatment of Clarke and Spinoza and his letters (MacHale) would firm up the system."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}], how_known: "MacTutor."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1854", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Laws of Thought (1854), the one listed lasting work (P29, P30)."}
  age_at_first_lasting_contribution: {value: 39, certainty: 0.7, cites: [{source: S1, locator: "Quick Info; Biography"}], how_known: "1854 − 1815 = 39 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Algebraic, deductive treatment of the laws of thought (S1, S2).", certainty: 0.5, cites: [{source: S2, locator: "ch. XXII"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Queen's College, Cork", role: "professor of mathematics", years: "1849–1864", kind: "university", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor: took up the post in November (1849) and taught there for the rest of his life."}
collaborators:
  - {value: "Augustus De Morgan", relation: "correspondent", note: "letter of 17 October 1850", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 172"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Religious words are brief passages in one book."
  open_questions:
    - "Ch. XIII; letters; MacHale's biography."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "J. J. O'Connor and E. F. Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. 'George Boole.' MacTutor History of Mathematics, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Boole/"
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Boole/"
    accessed: 2026-10-19
    reliability_note: "Signed reference biography."
    used_for: [identity, basics, contribution, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "George Boole"
    citation: "Boole, George. An Investigation of the Laws of Thought, on Which Are Founded the Mathematical Theories of Logic and Probabilities (London: Walton and Maberly, 1854). Archive.org scan. https://archive.org/details/aninvestigation00boolgoog"
    url: "https://archive.org/details/aninvestigation00boolgoog"
    accessed: 2026-10-19
    reliability_note: "Library scan of the first edition (page images of the work as issued, so primary facsimile); only the OCR text was read, the page images were not viewed."
    used_for: [basics, worldview, lane_b]
  - id: S3
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

George Boole (1815–1864), logician and mathematician [S1]. Draft: BELOW_THRESHOLD (leads CHRIST, DEISM); A 1, B 3 at 0.5. Plotted.

## Life and work

Lincoln; Queen's College, Cork [S1].

## Contribution and impact

Algebra of logic [S1].

## Childhood and education

Not read.

## Adult working worldview

Belief in an immutable Author of Nature; uniformity of nature [S2].

## Heritage (context only)

English [S1].

## Timing

1854, age 39 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Ch. XIII; letters.

## Research log

- 2026-10-19: Read MacTutor; Laws of Thought (1854) OCR.
