---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z5)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z5 audit fixes (Z5-10, Z5-11; RQ-Z5-1 answered: B 2 and D 1 stand at 0.5): al-Biruni's sincerity doubt named as an alternative (BELOW_THRESHOLD) under B and D, quoting Sachau vol. 2 p. 110 ('simply in order to mock them, or under the compulsion of some mental derangement') and p. 112 ('a calamitous fate, like that of Socrates'); S2 cites now give pp. 110–112 (the margin 'Page 256/257' is the Arabic page). Values unchanged; not plotted."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z5, order P32: F 3, rank 152). Basics from MacTutor (O'Connor and Robertson). Own words: Brahmasphutasiddhanta ch. 1 as quoted by al-Biruni (India, c. 1030, ch. LIX) in Sachau's English (1888, vol. 2, archive.org scan): the Head (Rahu) eclipses; 'The Veda, which is the word of God from the mouth of Brahman, says that the Head eclipses'; Aryabhata and others oppose this 'from enmity against the just-mentioned dogma'; 'everything which is in the Veda, Smriti, and Samhita is true'. A translation of an Arabic rendering, and al-Biruni suggests he may have spoken under compulsion or to mock, so 0.5. A scientist (P30: astronomy), but his own words override the P35 default. Span 628 (first ten chapters' version; Khandakhadyaka 665 not called lasting). primary_system HINDU (0.5, alt BELOW_THRESHOLD); A BELOW_THRESHOLD; B 2 (0.5, alt 3); C, E UNKNOWN; D 1 (0.5, alt 0); mid_basin BELOW_THRESHOLD. Not plotted (no A). Draft, not reviewed."}

identity:
  id: brahmagupta
  display_name: "Brahmagupta"
  roster:
    canonical_name: "Brahmagupta"
    rank: 152
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Brahmagupta", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "MacTutor."}
  native_name: {value: "Brahmagupta", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "MacTutor."}
  aliases: []

basics:
  birth:
    date: {value: "0598", calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "Biography (Khandakhadyaka 665 'when he was 67')"}], how_known: "665 − 67."}
    place: {value: UNKNOWN, how_known: "Not stated (he wrote at Bhillamala)."}
  death:
    date: {value: "0670", calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "heading"}], how_known: "MacTutor heading; conventional."}
    place: {value: UNKNOWN, how_known: "Not stated."}
  first_lasting_contribution_year: {value: 628, certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Brahmasphutasiddhanta, 628."}
  era_bucket: {value: "500 to 1399", certainty: 1.0, cites: [{source: S1, locator: "Biography"}], how_known: "628 (P2)."}
  region_of_birth: {value: "South Asia", certainty: 0.5, cites: [{source: S1, locator: "Biography"}], how_known: "India (P3); birthplace not stated."}
  region_of_work: {value: "South Asia", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Bhillamala (Bhinmal); Ujjain."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Sanskrit"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Sanskrit titles."}
  occupations: {value: ["astronomer", "mathematician", "head of the Ujjain observatory"], certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}

contribution:
  fields: {value: ["astronomy", "mathematics"], certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  lasting_original_contributions:
    - {value: "Brahmasphutasiddhanta (rules for zero and negative numbers, quadratic equations)", year: 628, kind: work, lasting: "'understanding of the number systems went far beyond that of others of the period' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  evidence_of_impact:
    - {value: "His works remained the standard in India c. 770–1020 (Sachau)", kind: "scholarly consensus", certainty: 0.5, cites: [{source: S2, locator: "vol. 1, preface xxxvi"}], how_known: "Sachau's preface (vol. 1), via search excerpt."}
  major_works:
    - {value: "Khandakhadyaka", year: 665, kind: book, certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Arithmetic of zero and negatives (S1).", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated (father Jisnugupta)."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Jisnugupta, father", role: father, certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
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
  working_years: {value: "628", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Astronomers must 'cease to oppose the generality, for everything which is in the Veda, Smriti, and Samhita is true'", certainty: 0.5, cites: [{source: S2, locator: "vol. 2, ch. LIX, pp. 110–112"}], how_known: "Via al-Biruni, in Sachau's English."}
  primary_system:
    value: HINDU
    basis: written_profession
    certainty: 0.5
    cites: [{source: S2, locator: "vol. 2, ch. LIX, pp. 110–112"}]
    how_known: "Brahmasphutasiddhanta ch. 1 as quoted by al-Biruni: the Veda is 'the word of God from the mouth of Brahman'; Brahmanical eclipse rites defended. English of an Arabic rendering; al-Biruni doubts his sincerity; 0.5."
    rationale: "HINDU (Brahmanical). Alternative BELOW_THRESHOLD: al-Biruni suggests he spoke under compulsion or in mockery."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: HINDU, reason: "Coded at 0.5."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "'the word of God from the mouth of Brahman' names a revealer but no locus (via al-Biruni)."}
    B_cause:
      value: 2
      basis: written_profession
      certainty: 0.5
      cites: [{source: S2, locator: "vol. 2, ch. LIX, pp. 110–112"}]
      how_known: "Own words via al-Biruni (translation of a translation), contested by al-Biruni's report that he computes eclipses from shadows; 0.5."
      rationale: "Account of nature (P6): eclipses are caused by the Head (Rahu), a personal agent, against the shadow theory; yet he computes eclipses by the shadow method (al-Biruni). An agent behind a recurring natural event, not limited: B 2. Alternative 3: P35 default for a working astronomer, with Rahu as a stated exception. Named alternative on sincerity: al-Biruni's sincerity doubt (pp. 110, 112): he may have spoken 'simply in order to mock them, or under the compulsion of some mental derangement', and al-Biruni settles on 'something of a calamitous fate, like that of Socrates' at age thirty; if the words are insincere, B is BELOW_THRESHOLD (0.5 either way)."
      alternatives:
        - {value: 3, note: "P35 default; Rahu as one stated exception.", cites: [{source: S1, locator: "Biography"}]}
        - {value: BELOW_THRESHOLD, note: "al-Biruni's sincerity doubt (mockery, compulsion, 'calamitous fate').", cites: [{source: S2, locator: "vol. 2, ch. LIX, pp. 110, 112"}]}
    C_ledger: {value: UNKNOWN, how_known: "Eclipse rites 'rewarded by heavenly bliss' not scored (coder's call)."}
    D_authority:
      value: 1
      basis: written_profession
      certainty: 0.5
      cites: [{source: S2, locator: "vol. 2, ch. LIX, pp. 110–112"}]
      how_known: "Via al-Biruni; 0.5."
      rationale: "Revelation outranks the astronomers on a question of natural fact ('everything which is in the Veda, Smriti, and Samhita is true'; dissenters 'must cease to oppose'), while his own computations use observation. Alternative 0. Named alternative on sincerity: al-Biruni's sincerity doubt (pp. 110, 112): he may have spoken 'simply in order to mock them, or under the compulsion of some mental derangement', and al-Biruni settles on 'something of a calamitous fate, like that of Socrates' at age thirty; if the words are insincere, D is BELOW_THRESHOLD."
      alternatives:
        - {value: 0, note: "Scripture decides the eclipse question outright.", cites: [{source: S2, locator: "vol. 2, ch. LIX, pp. 110–112"}]}
        - {value: BELOW_THRESHOLD, note: "al-Biruni's sincerity doubt (mockery, compulsion, 'calamitous fate').", cites: [{source: S2, locator: "vol. 2, ch. LIX, pp. 110, 112"}]}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied."}
  statements:
    - text: "The Veda, which is the word of God from the mouth of Brahman, says that the Head eclipses, likewise the book Smriti, composed by Manu, and the Samhita, composed by Garga the son of Brahman."
      cites: [{source: S2, locator: "vol. 2, ch. LIX, pp. 110–112"}]
      date: "628"
      context: "Brahmasphutasiddhanta ch. 1, as quoted by al-Biruni (c. 1030), Sachau's English."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-19
      note: "Diacritics dropped from the scan."
    - text: "Therefore people practise the well-known works of piety, and therefore those authors must cease to oppose the generality, for everything which is in the Veda, Smriti, and Samhita is true."
      cites: [{source: S2, locator: "vol. 2, ch. LIX, pp. 110–112"}]
      date: "628"
      context: "Same passage."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-19
  changes_over_life: []
  coder_notes: "Al-Biruni: 'he shirks the truth and lends his support to imposture, if he did not ... speak as he spoke simply in order to mock them, or under the compulsion of some mental derangement'. Sincerity is the ruling question."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: "Brahman (per al-Biruni)", certainty: 0.5, cites: [{source: S2, locator: "vol. 2, ch. LIX, pp. 110–112"}], how_known: "Al-Biruni: 'he was one of the Brahmans'."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "628", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Brahmasphutasiddhanta, the lasting work (P29, P30)."}
  age_at_first_lasting_contribution: {value: 30, certainty: 0.5, cites: [{source: S1, locator: "Biography"}], how_known: "628 − 598 = 30 (P30 year difference); al-Biruni also says 'only thirty'."}
  first_evidence_of_lio_type_views: {value: "628", certainty: 0.5, cites: [{source: S2, locator: "vol. 2, ch. LIX, pp. 110–112"}], how_known: "Same work."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.5, cites: [{source: S2, locator: "vol. 2, ch. LIX, pp. 110–112"}], how_known: "Same work."}
  worldview_during_major_work: {value: "HINDU", certainty: 0.5, cites: [{source: S2, locator: "vol. 2, ch. LIX, pp. 110–112"}], how_known: "Via al-Biruni."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Computational rules (S1).", certainty: 0.5, cites: [{source: S1, locator: "Biography"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not stated."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "Biography"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Astronomical observatory at Ujjain", role: head, years: UNKNOWN, kind: "research institute", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
collaborators:
  - {value: "Aryabhata", roster_id: aryabhata, relation: "rival or critic", note: "attacked his eclipse view", certainty: 0.7, cites: [{source: S2, locator: "vol. 2, ch. LIX, pp. 110–112"}], how_known: "Via al-Biruni."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 152"}], how_known: "Study roster."}
  controversies:
    - {value: "Sincerity of his defence of Rahu (al-Biruni)", certainty: 0.7, cites: [{source: S2, locator: "vol. 2, ch. LIX, pp. 110–112"}], how_known: "Al-Biruni."}
  data_quality_flags:
    - "Own words only through al-Biruni's Arabic, in Sachau's English."
  open_questions:
    - "Sanskrit of Brahmasphutasiddhanta 1 and the sphere chapter."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "J. J. O'Connor and E. F. Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Brahmagupta.\" MacTutor History of Mathematics Archive, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Brahmagupta/"
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Brahmagupta/"
    accessed: 2026-10-19
    reliability_note: "Signed biographical archive."
    used_for: [identity, basics, contribution, childhood, timing, lane_b, institutions]
  - id: S2
    type: secondary
    kind: "scholarly book"
    author: "al-Biruni, tr. Edward C. Sachau"
    citation: "Alberuni's India, tr. Edward C. Sachau (London: Trübner, 1888), vol. 2, ch. LIX. Scan: https://archive.org/details/alberunisindiaac02biruuoft"
    url: "https://archive.org/details/alberunisindiaac02biruuoft"
    accessed: 2026-10-19
    reliability_note: "Al-Biruni's quotation of Brahmagupta, in English from Arabic; OCR text checked."
    used_for: [contribution, worldview, heritage, timing, collaborators, review]
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

Brahmagupta (598–c. 670), astronomer and mathematician [S1]. Draft: HINDU (0.5); A BELOW_THRESHOLD; B 2 (0.5, alt 3); D 1 (0.5, alt 0). Not plotted.

## Life and work

Bhillamala; Ujjain [S1].

## Contribution and impact

Brahmasphutasiddhanta (628) [S1].

## Childhood and education

Not known.

## Adult working worldview

Defends Rahu and scripture against Aryabhata, per al-Biruni [S2].

## Heritage (context only)

Brahman [S2].

## Timing

628, age 30 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- See review.open_questions.

## Research log

- 2026-10-19: Read MacTutor; Sachau's al-Biruni vol. 2 ch. LIX.
