---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AB1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-20
  change_log:
    - {date: 2026-10-20, by: "Grok Bot", summary: "AB1 audit fixes: 'ultimate opacity' quote dated 1881 (reprinted 1897), before the span (no score change). RQ-AB1-1, v8's call on the auditor's advice: scientist under the P35 theories-of-mind addendum, B 3 at 0.5, alt 4; 'piecemeal supernaturalism' (Varieties postscript) noted as a B 2 lead. Still not plotted (A BELOW_THRESHOLD)."}
    - {date: 2026-10-20, by: "Grok Bot", summary: "Record created (stage 3 batch AB1, order P32: F 3, rank 226). Source: SEP 'William James' (Russell Goodman, 2021, read in full). Lasting: The Principles of Psychology (1890), which 'influenced generations of thinkers in Europe and America' (S1), and Pragmatism (1907), 'influential', in the 'pragmatist tradition that he founded (along with Charles Peirce)' (S1). Span 1890–1907, age 48. Worldview: he advocated a 'theism' positing 'an ultimate opacity in things' ('Reflex Action and Theism', 1881, reprinted 1897) and wrote 'if the hypothesis of God works satisfactorily in the widest sense of the word, it is true' (Pragmatism, 1907); S1: he 'oscillated' between a naturalistic 'Science of Religion' and 'an altogether supernatural domain'. primary_system BELOW_THRESHOLD (theistic and pragmatist leads); A BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. B 3 at 0.5, alt 4 (P35; RQ-AB1-1). Not plotted. Draft, not reviewed."}

identity:
  id: james-william
  display_name: "William James"
  roster:
    canonical_name: "William James"
    rank: 226
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: "core"
    field: "psychology"
    field_bucket: "psychology / neuroscience"
  full_name: {value: "William James", certainty: 0.7, cites: [{source: S1, locator: "1. Chronology"}], how_known: "SEP."}
  native_name: {value: "William James", certainty: 0.7, cites: [{source: S1, locator: "1. Chronology"}], how_known: "SEP."}
  aliases: []

basics:
  birth:
    date: {value: "1842", certainty: 0.7, cites: [{source: S1, locator: "1. Chronology"}], how_known: "SEP gives the year."}
    place: {value: "New York City", modern_name: "New York City, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "1. Chronology"}], how_known: "SEP."}
  death:
    date: {value: "1910", certainty: 0.7, cites: [{source: S1, locator: "1. Chronology"}], how_known: "SEP gives the year."}
    place: {value: "Chocorua, New Hampshire", modern_name: "Chocorua, New Hampshire, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "1. Chronology"}], how_known: "SEP: 'at summer home in Chocorua, New Hampshire'."}
  first_lasting_contribution_year: {value: 1890, certainty: 0.7, cites: [{source: S1, locator: "opening; 3"}], how_known: "The Principles of Psychology (1890) (S1); P30 publication."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "1890 (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "1. Chronology"}], how_known: "United States (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "1. Chronology"}], how_known: "Harvard."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "English."}
  occupations: {value: ["psychologist", "philosopher", "physiologist"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}

contribution:
  fields: {value: ["psychology", "philosophy"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  lasting_original_contributions:
    - {value: "The Principles of Psychology", year: 1890, kind: "work", lasting: "'has given us such ideas as \"the stream of thought\"'; it 'influenced generations of thinkers in Europe and America, including Edmund Husserl, Bertrand Russell, John Dewey, and Ludwig Wittgenstein' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "1890 (S1)."}
    - {value: "Pragmatism (with Peirce, founder of the pragmatist tradition)", year: 1907, kind: "work", lasting: "'his influential Pragmatism (1907)'; 'the pragmatist tradition that he founded (along with Charles Peirce)' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; 6"}], how_known: "1907 (S1)."}
  evidence_of_impact:
    - {value: "Husserl incorporated his notions of the 'fringe' and 'halo'; Russell's Analysis of Mind is indebted to him", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S1, locator: "6"}], how_known: "SEP."}
  major_works:
    - {value: "The Will to Believe and Other Essays", year: 1897, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "4"}], how_known: "SEP."}
    - {value: "The Varieties of Religious Experience", year: 1902, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "5"}], how_known: "SEP."}
    - {value: "A Pluralistic Universe", year: 1909, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "6"}], how_known: "SEP."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founder of American psychology and pragmatism (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "First child of Henry James (Sr.) and Mary Walsh James; brother of the novelist Henry James", role: "family", certainty: 0.7, cites: [{source: S1, locator: "1. Chronology"}], how_known: "SEP."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Tutors and schools in New York, Geneva, Paris, Boulogne; Lawrence Scientific School (1861) and Harvard Medical School (from 1864)", certainty: 0.7, cites: [{source: S1, locator: "1. Chronology"}], how_known: "SEP."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1890–1907", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "Own words: a 'theism' that posits 'an ultimate opacity in things, a dimension of being which escapes our theoretic control' (1881, reprinted in The Will to Believe 1897, WB 143) and 'if the hypothesis of God works satisfactorily in the widest sense of the word, it is true' (Pragmatism, 1907) (S1). S1: he 'oscillated' between a 'Science of Religion' and 'an altogether supernatural domain'. A pragmatic, pluralistic theism fits no coded system at 0.5."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: PRAG, reason: "His own pragmatic test for religious hypotheses (S1 §6)."}
    - {code: CLASS_THEISM, reason: "'Theism' in The Will to Believe (S1 §4); but his God is pluralistic and not classical."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "'a dimension of being which escapes our theoretic control' (1897) and the 'supernatural domain' of religious experience suggest a locus beyond nature (A 1–2 lead), but the pragmatic test of God and the 'study in human nature' reading pull the other way (S1); no reading reaches 0.5."}
    B_cause: 
      value: 3
      basis: inference_from_work
      certainty: 0.5
      cites: [{source: S1, locator: "1. Chronology; 3"}]
      how_known: "Scientist (P30). B from working science with no statement of their own on law and exception, so 3 at 0.5, alternative 4, never 4 (P35)."
      rationale: "RQ-AB1-1 (v8's call on the auditor's advice): a scientist under the P35 theories-of-mind addendum (trained in physiology and medicine; first American psychology laboratory, 1874–75; the Principles makes testable claims about organisms). 0.5 because S1 calls his writings 'as much philosophical as scientific'. Lead for B 2: his own 'piecemeal supernaturalism' (Varieties postscript, 1902), not yet read first-hand."
      alternatives:
        - {value: 4, note: "Working science cannot tell lawful-with-exceptions from exceptionless (P35).", cites: [{source: S1, locator: "1. Chronology; 3"}]}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied (Pavlov pattern)."}
  statements:
    - text: "an ultimate opacity in things, a dimension of being which escapes our theoretic control"
      cites: [{source: S1, locator: "4. Essays in Popular Philosophy"}]
      date: "1881"
      context: "'Reflex Action and Theism' (1881 lecture and essay), reprinted in The Will to Believe, 1897 (WB 143); James advocates a 'theism' that posits this."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-19
      note: "Quoted in S1; before the span (1881; reprinted 1897)."
    - text: "if the hypothesis of God works satisfactorily in the widest sense of the word, it is true"
      cites: [{source: S1, locator: "6. Late Writings"}]
      date: "1907"
      context: "Pragmatism, lecture 'Pragmatism and Religion' (p. 143)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-19
      note: "A test for religious hypotheses, not a profession of a system."
  changes_over_life: []
  coder_notes: "Read Varieties (1902) postscript, where he describes his own 'piecemeal supernaturalism', for a possible A reading."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated in S1."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1890–1907", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "The Principles (1890) to Pragmatism (1907), the first and last lasting items (P29, P30)."}
  age_at_first_lasting_contribution: {value: 48, certainty: 0.7, cites: [{source: S1, locator: "1. Chronology; opening"}], how_known: "1890 − 1842 = 48 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Psychology and philosophy (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Harvard University", role: "instructor in physiology and psychology; professor of philosophy", years: "1873–1907", kind: "university", certainty: 0.5, cites: [{source: S1, locator: "1. Chronology"}], how_known: "SEP chronology; end year is the coder's reading."}
collaborators:
  - {value: "Charles Sanders Peirce", relation: "collaborator", note: "co-founder of pragmatism", certainty: 0.7, cites: [{source: S1, locator: "6"}], how_known: "SEP."}
  - {value: "Louis Agassiz", relation: "teacher", note: "Amazon expedition 1865", certainty: 0.7, cites: [{source: S1, locator: "1. Chronology"}], how_known: "SEP."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 226"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Scientist under the P35 theories-of-mind addendum (RQ-AB1-1)."
    - "Worldview BELOW_THRESHOLD."
  open_questions:
    - "B 2 lead: Varieties postscript 'piecemeal supernaturalism' (1902)."
    - "A_locus from the Varieties postscript."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Russell Goodman"
    citation: "Goodman, Russell. 'William James.' Stanford Encyclopedia of Philosophy (substantive revision 3 November 2021). https://plato.stanford.edu/entries/james/"
    url: "https://plato.stanford.edu/entries/james/"
    accessed: 2026-10-19
    reliability_note: "Signed encyclopedia entry, read in full."
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
---

## Summary

William James (1842–1910), psychologist and philosopher [S1]. Draft: worldview BELOW_THRESHOLD. Not plotted.

## Life and work

New York; Europe; Harvard [S1].

## Contribution and impact

Principles 1890; Pragmatism 1907 [S1].

## Childhood and education

Lawrence Scientific School; Harvard Medical School [S1].

## Adult working worldview

Pragmatic, pluralistic theism [S1].

## Heritage (context only)

Not stated.

## Timing

1890–1907, age 48 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Scientist call; A.

## Research log

- 2026-10-20: AB1 audit fixes: 'ultimate opacity' quote dated 1881 (reprinted 1897), before the span (no score change). RQ-AB1-1, v8's call on the auditor's advice: scientist under the P35 theories-of-mind addendum, B 3 at 0.5, alt 4; 'piecemeal supernaturalism' (Varieties postscript) noted as a B 2 lead. Still not plotted (A BELOW_THRESHOLD).
- 2026-10-20: Read SEP (Goodman, 2021).
