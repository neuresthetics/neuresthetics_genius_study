---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch I)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-15
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch I, order P32: F 5, rank 61). Basics from Britannica (Hunt). Worldview from My Inventions (Electrical Experimenter, 1919), ch. VI, Wikisource transcription (web copy, 0.7 cap). Scientist/engineer under P30. primary_system BELOW_THRESHOLD (candidates DETERM, AGNOS); A BELOW_THRESHOLD (only 'faith in a supreme power of some kind' as a general human trait); B 4 at 0.5 (alt 3): 'We are automata entirely controlled by the forces of the medium' and no foundation for spiritual phenomena (near P40; RQ2 batch I); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Not plotted. Draft, not reviewed."}

identity:
  id: tesla-nikola
  display_name: "Nikola Tesla"
  roster:
    canonical_name: "Nikola Tesla"
    rank: 61
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: invention
    field_bucket: "invention / engineering"
  full_name: {value: "Nikola Tesla", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  native_name: {value: UNKNOWN, how_known: "Cyrillic form not in the sources read."}
  aliases: []

basics:
  birth:
    date: {value: "1856-07", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica gives 'July 9/10, 1856', so only the month is recorded."}
    place: {value: "Smiljan, Austrian Empire", modern_name: "Smiljan, Croatia", polity_then: "Austrian Empire", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1943-01-07", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "New York, New York, U.S.", modern_name: "New York City, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1883, certainty: 0.5, cites: [{source: S1, locator: "training paragraph"}], how_known: "First induction motor built at Strassburg in 1883, embodying the rotating-magnetic-field principle he had visualized earlier at Budapest (no year given) (P13); 0.5."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "His whole adult life falls in the bucket (P2)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Croatia is Southern Europe in regions.csv (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "from 1884"}], how_known: "United States from 1884."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [English], certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Wrote in English in the US; earlier languages not given (0.5)."}
  occupations: {value: ["inventor", "electrical engineer"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["electrical engineering"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Rotating magnetic field and induction motor (basis of most alternating-current machinery)", year: 1883, kind: discovery, lasting: "'the basis of most alternating-current machinery' (S1)", certainty: 0.5, cites: [{source: S1, locator: "opening; training paragraph"}], how_known: "Year of the first induction motor."}
    - {value: "Tesla coil", year: 1891, kind: invention, lasting: "'widely used today in radio and television sets' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; 1891 paragraph"}], how_known: "Britannica."}
    - {value: "Teleautomatic (remote-controlled) boat", year: 1898, kind: invention, lasting: "(S1)", certainty: 0.5, cites: [{source: S1, locator: "1898 paragraph"}], how_known: "Britannica; lasting status the coder's reading (0.5)."}
  evidence_of_impact:
    - {value: "Tesla Inc. named in his honour (2003)", kind: "named after them", certainty: 0.7, cites: [{source: S1, locator: "last paragraph"}], how_known: "Britannica."}
    - {value: "Edison Medal, 1917", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "turbines paragraph"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Serbian Orthodox (father an Orthodox priest)", certainty: 0.7, cites: [{source: S1, locator: "family paragraph"}], how_known: "Britannica."}
  family_religious_practice: {value: "Intended 'from my very birth for the clerical profession'", certainty: 0.7, cites: [{source: S2, locator: "ch. I"}], how_known: "Autobiography, web copy."}
  parents_and_household:
    - {value: "Father an Orthodox priest; mother 'unschooled but highly intelligent'", role: parents, certainty: 0.7, cites: [{source: S1, locator: "family paragraph"}], how_known: "Britannica."}
  household_circumstances: {value: TODO}
  schooling:
    - {value: "Technical University at Graz; University of Prague", stage: university, run_by: "state or municipal", certainty: 0.7, cites: [{source: S1, locator: "training paragraph"}], how_known: "Britannica; run_by the coder's reading."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1883–1898", certainty: 0.5, cites: [{source: S1, locator: "career paragraphs"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "'Religious dogmas are no longer accepted in their orthodox meaning, but every individual clings to faith in a supreme power of some kind'; any ideal serves 'so long as it fulfills the function of a dematerializing force'.", certainty: 0.7, cites: [{source: S2, locator: "ch. VI"}], how_known: "Published autobiography, web copy."}
  primary_system:
    value: BELOW_THRESHOLD
    basis: written_profession
    certainty: 0.5
    cites: [{source: S2, locator: "ch. VI"}]
    rationale: "Denies any foundation for 'psychical and spiritual phenomena'; holds 'the automatism of life'; treats faith in 'a supreme power of some kind' as a general human need, without saying whether he holds it. Candidates DETERM and AGNOS."
    how_known: "One chapter of a published autobiography in a web copy."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: DETERM, reason: "'We are automata entirely controlled by the forces of the medium'."}
    - {code: AGNOS, reason: "No personal statement on God read."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "The only God-type statement read ('every individual clings to faith in a supreme power of some kind') describes people generally, not his own view of where God is."}
    B_cause:
      value: 4
      basis: written_profession
      certainty: 0.5
      cites: [{source: S2, locator: "ch. VI"}]
      how_known: "Published autobiography, web copy; 0.5; alternative named."
      rationale: "Strict mechanism stated: 'We are automata entirely controlled by the forces of the medium'; no foundation for spiritual phenomena. Near P40 (stated strict necessity), but it is said of living beings, and the same chapter reports a 'cosmic' pain after which wrongdoers 'invariably' came to grief, a non-mechanical-sounding regularity he calls a discovery. So 0.5, alternative 3 (P35 working-science default). RQ2 (batch I)."
    C_ledger: {value: UNKNOWN, how_known: "The 'cosmic' law that wrongdoers 'came to grief' resembles a ledger but no agent is named; not scored."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A is BELOW_THRESHOLD."}
  statements:
    - text: "We are automata entirely controlled by the forces of the medium being tossed about like corks on the surface of the water, but mistaking the resultant of the impulses from the outside for free will."
      cites: [{source: S2, locator: "ch. VI"}]
      date: "1919"
      axes: [B_cause]
      kind: "autobiography"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "Wikisource transcription of the Electrical Experimenter text; web copy, 0.7 cap."
    - text: "I have never had the faintest reason since to change my views on psychical and spiritual phenomena, for which there is absolutely no foundation."
      cites: [{source: S2, locator: "ch. VI"}]
      date: "1919"
      axes: [B_cause]
      kind: "autobiography"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "As above."
    - text: "Religious dogmas are no longer accepted in their orthodox meaning, but every individual clings to faith in a supreme power of some kind."
      cites: [{source: S2, locator: "ch. VI"}]
      date: "1919"
      axes: [A_locus]
      kind: "autobiography"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "As above."
  changes_over_life: []
  coder_notes: "Coder's call; one chapter of the autobiography. RQ2 (batch I)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Serbian", certainty: 0.7, cites: [{source: S1, locator: "family paragraph"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Serbian Orthodox", certainty: 0.7, cites: [{source: S1, locator: "family paragraph"}], how_known: "Britannica (father an Orthodox priest)."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1883–1898", certainty: 0.5, cites: [{source: S1, locator: "career paragraphs"}], how_known: "First to last listed contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 27, certainty: 0.5, cites: [{source: S1, locator: "opening; training paragraph"}], how_known: "1883 − 1856 = 27 (P30)."}
  first_evidence_of_lio_type_views: {value: "1919", certainty: 0.5, cites: [{source: S2, locator: "ch. VI"}], how_known: "Earliest text read; he says the views were formed 'long ago'."}
  lio_views_relative_to_major_work: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "ch. VI"}], how_known: "Stated in 1919, held 'long ago' (undated)."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Not dated."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not read.", certainty: 0.5, cites: [{source: S1, locator: "training paragraph"}], how_known: "Coder's reading."}
  form_acquired: {value: "through the profession", certainty: 0.5, cites: [{source: S1, locator: "training paragraph"}], how_known: "Engineering training."}
  circle_present: {value: "no", rationale: "Mechanism without a stated God.", certainty: 0.5, cites: [{source: S2, locator: "ch. VI"}], how_known: "Coder's reading."}
  reading: "Mechanist automatism; God left as others' faith."
  notes: ""

institutions:
  - {value: "Continental Edison Company, Paris", role: engineer, years: "1882–1884", kind: commercial, certainty: 0.5, cites: [{source: S1, locator: "training paragraph"}], how_known: "From 1882; end year inferred from his sailing in 1884 (0.5)."}
collaborators:
  - {value: "George Westinghouse", relation: "mentor or employer", note: "bought the AC patents", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  - {value: "Thomas Edison", relation: "mentor or employer", note: "first US employer; later separation", certainty: 0.7, cites: [{source: S1, locator: "training paragraph"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 61"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags: []
  open_questions:
    - "Read 'The Problem of Increasing Human Energy' (1900) for any God statement; check the Electrical Experimenter scan; RQ2 batch I."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Inez Whitaker Hunt"
    citation: "Hunt, Inez Whitaker. \"Nikola Tesla.\" Encyclopaedia Britannica, updated 15 October 2026. https://www.britannica.com/biography/Nikola-Tesla."
    url: "https://www.britannica.com/biography/Nikola-Tesla"
    accessed: 2026-10-15
    reliability_note: "Signed body; Top Questions not cited."
    used_for: [identity, basics, contribution, childhood, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Nikola Tesla"
    year: 1919
    citation: "Tesla, Nikola. \"My Inventions.\" Electrical Experimenter, 1919. Wikisource transcription."
    url: "https://en.wikisource.org/wiki/My_Inventions"
    accessed: 2026-10-15
    reliability_note: "Wikisource transcription; §7 cap 0.7."
    used_for: [basics, childhood, worldview, timing, lane_b]
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

# Nikola Tesla

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Nikola Tesla (1856–1943), Serbian American inventor [S1]. Draft: primary_system BELOW_THRESHOLD; A BELOW_THRESHOLD; B 4 at 0.5 (RQ2); mid_basin BELOW_THRESHOLD. Not plotted.

## Life and work

Graz, Prague, Budapest, Paris; New York from 1884 [S1].

## Contribution and impact

Rotating magnetic field, AC system, Tesla coil [S1].

## Childhood and education

Son of an Orthodox priest; intended for the clergy [S1, S2].

## Adult working worldview

'We are automata entirely controlled by the forces of the medium' [S2].

## Heritage (context only)

Serbian Orthodox [S1].

## Timing

First lasting contribution 1883, at 27 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle [S2].

## Open questions

- RQ2.

## Research log

- 2026-10-15: Read Britannica (Hunt) and My Inventions ch. VI (Wikisource).
