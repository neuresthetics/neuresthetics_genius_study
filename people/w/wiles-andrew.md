---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch N)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-17
  last_updated: 2026-10-17
  change_log:
    - {date: 2026-10-17, by: "Grok Bot", summary: "Record created (stage 3 batch N, order P32: F 4, rank 83). Basics from Britannica (Britannica Editors, unsigned; body only) and MacTutor (O'Connor and Robertson). Worldview: the 2016 Heidelberg Laureate Forum press conference (Plus magazine transcript), where he declines the question 'Who created this landscape?' and calls mathematics 'discovered'. primary_system UNKNOWN; A UNKNOWN; B BELOW_THRESHOLD (a view on mathematical truth alone, P30); mid_basin UNKNOWN (P19). Not plotted. Draft, not reviewed."}
    - {date: 2026-10-17, by: "Grok Bot", summary: "Batch N audit fix (#18): B BELOW_THRESHOLD now cites P16 (a view on mathematical truth alone), not P30; value unchanged."}

identity:
  id: wiles-andrew
  display_name: "Andrew Wiles"
  roster:
    canonical_name: "Andrew Wiles"
    rank: 83
    F: 4
    models: [Claude, DeepSeek, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Sir Andrew John Wiles", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts ('In full')"}], how_known: "Britannica."}
  native_name: {value: UNKNOWN, how_known: "English."}
  aliases:
    - {name: "Andrew-Wiles", kind: "roster alias"}

basics:
  birth:
    date: {value: "1953-04-11", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Cambridge, England", modern_name: "Cambridge, United Kingdom", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: UNKNOWN, how_known: "Living (Britannica gives 'age 73')."}
    place: {value: UNKNOWN, how_known: "Living."}
  first_lasting_contribution_year: {value: 1995, certainty: 0.5, cites: [{source: S1, locator: "Fermat paragraphs"}], how_known: "The proof of Fermat's last theorem: announced in June 1993 with gaps, completed in 1995 with Richard Taylor and published in Annals of Mathematics 141:3 (1995) (S1). His earlier work on Iwasawa theory and Birch–Swinnerton-Dyer is named but not dated in the body (P39). 1995 is the coder's pick (the completed proof); 1993 is the alternative."}
  era_bucket: {value: "1950 on", certainty: 0.5, cites: [{source: S1, locator: "Fermat paragraphs"}], how_known: "From 1995 (P2); 1993 gives the same bucket."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United Kingdom (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "career paragraph"}], how_known: "Princeton from 1982, where the proof was done (S1); Oxford later."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [English], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading (English-language posts and papers)."}
  occupations: {value: ["mathematician", "professor"], certainty: 0.7, cites: [{source: S1, locator: "opening; career paragraph"}], how_known: "Britannica."}

contribution:
  fields: {value: ["number theory"], certainty: 0.7, cites: [{source: S1, locator: "'Wiles worked on a number of outstanding problems in number theory'"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Proof of Fermat's last theorem (via the semistable case of the Shimura–Taniyama–Weil conjecture; gap closed with Richard Taylor)", year: 1995, kind: theory, lasting: "'a British mathematician who proved Fermat's last theorem' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; Fermat paragraphs"}], how_known: "Britannica; a mathematical result, not a theory about physical or natural systems (P30)."}
  evidence_of_impact:
    - {value: "IMU special silver plaque (1998), Wolf Prize (1995–96), Abel Prize (2016), Copley Medal (2017); knighted 2000", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "opening; last paragraph"}], how_known: "Britannica."}
  major_works:
    - {value: "Modular Elliptic Curves and Fermat's Last Theorem", year: 1995, kind: "paper or paper series", certainty: 0.7, cites: [{source: S1, locator: "last paragraph"}], how_known: "Britannica (Annals of Mathematics 141:3, pp. 443–551)."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Proof of a centuries-old conjecture (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Church of England (father an ordained clergyman and theologian)", certainty: 0.5, cites: [{source: S2, locator: "opening paragraph"}], how_known: "MacTutor: father 'trained for ordination at Ridley Hall', curate, chaplain, later lecturer in New Testament studies and dean of Clare College. The denomination is the coder's reading of Ridley Hall (an Anglican college); context only."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father Maurice Frank Wiles (1923–2005), theologian and clergyman", role: father, certainty: 0.7, cites: [{source: S2, locator: "opening paragraph"}], how_known: "MacTutor."}
    - {value: "Mother Patricia Margaret Mowll (1927–2005)", role: mother, certainty: 0.7, cites: [{source: S2, locator: "opening paragraph"}], how_known: "MacTutor."}
  household_circumstances: {value: "Lived in Ibadan, Nigeria, 1955–1959, where his father lectured; returned to Cambridge in 1959", certainty: 0.7, cites: [{source: S2, locator: "opening paragraph"}], how_known: "MacTutor."}
  schooling:
    - {value: "King's College School, Cambridge", stage: "elementary school", years: "1959–", certainty: 0.7, cites: [{source: S2, locator: "opening paragraph"}], how_known: "MacTutor ('a preparatory school')."}
  early_mathematics: {value: "advanced mathematics", certainty: 0.5, cites: [{source: S1, locator: "'fascinated by the problem from the age of 10'"}], how_known: "Fascinated by Fermat's problem from age 10 (S1); the level reached is the coder's reading."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [English], certainty: 0.5, cites: [{source: S2, locator: "opening paragraph"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "Met Fermat's last theorem at about age 10", year: 1963, age: 10, certainty: 0.5, cites: [{source: S1, locator: "'from the age of 10'"}], how_known: "Britannica; year computed."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1995", certainty: 0.5, cites: [{source: S1, locator: "Fermat paragraphs"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read."}
  primary_system: {value: UNKNOWN, how_known: "(interview) No statement on God or religion found; asked 'Who created this landscape?' he declines ('mathematicians are not that philosophical'). His father's profession is context only."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: PLATO, reason: "Mathematics 'discovered' is a view on mathematical truth only, not a worldview code."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "(interview) The one question about a creator was declined: 'Well, mathematicians are not that philosophical. (Laughter) We're artists, we just enjoy it and we leave it' (S3). Nothing else read."}
    B_cause: {value: BELOW_THRESHOLD, how_known: "(interview) A mathematician with no listed contribution about physical or natural systems, so not a scientist (P30), and neither P33 nor P35 applies; B needs a statement about nature (P16). The only statement read is on mathematical truth: 'I don't think I know a mathematician who doesn't think that it's discovered' (S3). A view on mathematical truth alone gives BELOW_THRESHOLD (P16)."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "A is UNKNOWN (P19)."}
  statements:
    - text: "To tell you the truth, I don't think I know a mathematician who doesn't think that it's discovered. So we're all on one side, I think."
      cites: [{source: S3, locator: "answer to 'Do you think mathematics is discovered or invented?'"}]
      date: "2016-09"
      context: "Press conference at the Heidelberg Laureate Forum, September 2016, as published by Plus magazine (S3)."
      axes: [B_cause]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-17
      note: "On mathematical truth only (P16)."
    - text: "Well, mathematicians are not that philosophical. (Laughter) We're artists, we just enjoy it and we leave it. There are philosophers and people at the more philosophical end of mathematics, there are some who do worry about that kind of thing, but we're not Bertrand Russells."
      cites: [{source: S3, locator: "answer to 'Who created this landscape?'"}]
      date: "2016-09"
      context: "Same press conference; a reply to 'Who created this landscape?'"
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-17
      note: "A declined question; not scored."
  changes_over_life: []
  coder_notes: "Coder's call. The press conference is after the working year (1995). The Abel interview (Raussen and Skau, EMS Newsletter 101, 2016) and the Oxford/Hannah Fry conversation are leads, not read."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading of 'British', born in Cambridge."}
  religious_heritage_by_birth: {value: "Church of England (clergy family)", certainty: 0.5, cites: [{source: S2, locator: "opening paragraph"}], how_known: "As family_religion."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1995", certainty: 0.5, cites: [{source: S1, locator: "Fermat paragraphs"}], how_known: "Only one dated lasting contribution (P29, P30, P39)."}
  age_at_first_lasting_contribution: {value: 42, certainty: 0.5, cites: [{source: S1, locator: "opening; 1995"}], how_known: "1995 − 1953 = 42 (P30)."}
  first_evidence_of_lio_type_views: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S3, locator: "press conference"}], how_known: "Only the 2016 press conference read."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S3, locator: "press conference"}], how_known: "As above."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Nothing read from 1995."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Nothing read.", certainty: 0.5, cites: [{source: S3, locator: "press conference"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S3, locator: "press conference"}], how_known: "Nothing read."}
  circle_present: {value: "unclear", rationale: "Nothing read on God.", certainty: 0.5, cites: [{source: S3, locator: "press conference"}], how_known: "Coder's reading."}
  reading: "Mathematics as a discovered landscape; no theology stated."
  notes: ""

institutions:
  - {value: "Princeton University", role: professor, years: "1982–2012", kind: university, certainty: 0.7, cites: [{source: S1, locator: "career paragraph"}], how_known: "Britannica (emeritus 2012)."}
  - {value: "University of Oxford", role: "faculty", years: UNKNOWN, kind: university, certainty: 0.7, cites: [{source: S1, locator: "career paragraph"}], how_known: "Britannica ('subsequently joined the faculty at Oxford')."}
collaborators:
  - {value: "Richard Taylor", relation: collaborator, note: "helped close the gap in the proof; co-author of the Hecke algebras paper", certainty: 0.7, cites: [{source: S1, locator: "Fermat paragraphs"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 83"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Britannica article is unsigned (Britannica Editors)."
  open_questions:
    - "Read the Abel interview (EMS Newsletter 101, 2016) for any remark on God or on nature."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Andrew Wiles.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Andrew-Wiles. Read in Wayback snapshot 20260603100827."
    url: "https://www.britannica.com/biography/Andrew-Wiles"
    accessed: 2026-10-17
    reliability_note: "Unsigned article. Body only; Quick Facts used for the full name; Top Questions not cited."
    used_for: [identity, basics, contribution, childhood, timing, institutions, collaborators]
  - id: S2
    type: secondary
    kind: other
    author: "J J O'Connor and E F Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Andrew Wiles.\" MacTutor History of Mathematics Archive, University of St Andrews (last update December 2023). https://mathshistory.st-andrews.ac.uk/Biographies/Wiles/"
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Wiles/"
    accessed: 2026-10-17
    reliability_note: "Signed biography, read directly."
    used_for: [childhood, heritage]
  - id: S3
    type: secondary
    kind: other
    author: "The Plus Team"
    citation: "The Plus Team. \"Andrew Wiles: what does it feel like to do maths?\" Plus magazine, 1 December 2016. Based on a press conference at the Heidelberg Laureate Forum, September 2016. https://plus.maths.org/andrew-wiles-what-does-if-feel-do-maths"
    url: "https://plus.maths.org/andrew-wiles-what-does-if-feel-do-maths"
    accessed: 2026-10-17
    reliability_note: "Published transcript of his own first-person answers (P8), read directly."
    used_for: [worldview, timing, lane_b]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-17
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Andrew Wiles

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Andrew Wiles (born 1953), British mathematician who proved Fermat's last theorem [S1]. Draft: primary_system UNKNOWN; A UNKNOWN (interview); B BELOW_THRESHOLD (interview); mid_basin UNKNOWN. Not plotted.

## Life and work

Princeton from 1982, later Oxford [S1].

## Contribution and impact

Proof of Fermat's last theorem, completed 1995 with Taylor's help [S1].

## Childhood and education

Son of the theologian Maurice Wiles; early years in Nigeria; King's College School, Cambridge [S2].

## Adult working worldview

Calls mathematics 'discovered' and declines the question of who created it [S3].

## Heritage (context only)

Clergy family [S2].

## Timing

First lasting contribution 1995, at 42 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Nothing read on God [S3].

## Open questions

- Abel interview (2016).

## Research log

- 2026-10-17: Read Britannica (Wayback 20260603100827), MacTutor and the Plus transcript directly. Web search for any statement on religion found none.
