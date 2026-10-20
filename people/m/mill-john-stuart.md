---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA4)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA4, order P32: F 3, rank 193). Sources: Britannica, signed by Richard Paul Anschutz (main article; the fetched copy covers the summary and 'Early life and career' only), Britannica students edition (read in full) for publication years, and his Autobiography (1873; Project Gutenberg transcription, chapter 2 read). Lasting work: A System of Logic (1843) and On Liberty (1859); Anschutz: 'remains of lasting interest as a logician and an ethical theorist'; span 1843–1859, age 37. Own words: Autobiography ch. 2, 'one who has not thrown off religious belief, but never had it: I grew up in a negative state with regard to it', with his father's teaching that 'Who made me?' 'cannot be answered'. Published 1873, after the span and describing his upbringing, so P20 caps it at 0.5. primary_system AGNOS 0.5 (written_profession), alt BELOW_THRESHOLD (the passage reports absence of belief, not a settled stance; his posthumous Theism, not read, is a lead the other way). A BELOW_THRESHOLD (no locus stated); philosopher, not a scientist, B UNKNOWN; C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD (Pavlov pattern). Not plotted. Draft, not reviewed."}

identity:
  id: mill-john-stuart
  display_name: "John Stuart Mill"
  roster:
    canonical_name: "John Stuart Mill"
    rank: 193
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: "core"
    field: "philosophy"
    field_bucket: "philosophy"
  full_name: {value: "John Stuart Mill", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  native_name: {value: "John Stuart Mill", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  aliases: []

basics:
  birth:
    date: {value: "1806-05-20", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "Pentonville, London", modern_name: "London, United Kingdom", polity_then: "United Kingdom of Great Britain and Ireland", certainty: 0.7, cites: [{source: S1, locator: "Early life and career"}], how_known: "Britannica."}
  death:
    date: {value: "1873-05-08", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "Avignon", modern_name: "Avignon, France", polity_then: "French Third Republic", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1843, certainty: 0.7, cites: [{source: S3, locator: "para. 4"}], how_known: "'He published his System of Logic (1843)' (S3); publication (P30 #1)."}
  era_bucket: {value: "1750 to 1849", certainty: 0.7, cites: [{source: S3, locator: "para. 4"}], how_known: "Keyed on the first lasting year, 1843 (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "United Kingdom (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "Early life and career"}], how_known: "London, India House."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S3, locator: "para. 4"}], how_known: "English books."}
  occupations: {value: ["philosopher", "economist", "civil servant", "member of Parliament"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S3, locator: "para. 3–4"}], how_known: "Britannica."}

contribution:
  fields: {value: ["logic", "ethics", "political philosophy", "political economy"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "A System of Logic (inductive methods)", year: 1843, kind: "work", lasting: "'remains of lasting interest as a logician' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S3, locator: "para. 4"}], how_known: "Anschutz; published 1843 (S3)."}
    - {value: "On Liberty", year: 1859, kind: "work", lasting: "'remains of lasting interest as ... an ethical theorist' (S1); listed among his notable works (S1)", certainty: 0.5, cites: [{source: S1, locator: "Introduction"}, {source: S3, locator: "para. 4"}], how_known: "Published 1859 (S3). Anschutz's lasting phrase is about him as an ethical theorist, not this book by name, so 0.5."}
  evidence_of_impact:
    - {value: "'Remains of lasting interest as a logician and an ethical theorist'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Anschutz."}
  major_works:
    - {value: "Principles of Political Economy", year: 1848, kind: "book", certainty: 0.7, cites: [{source: S3, locator: "para. 4"}], how_known: "Britannica students."}
    - {value: "The Subjection of Women", year: 1869, kind: "book", certainty: 0.7, cites: [{source: S3, locator: "para. 4"}], how_known: "Britannica students."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Lasting as logician and ethical theorist (S1).", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Eldest son of James Mill, historian, economist and philosopher, who educated him exclusively", role: "father", certainty: 0.7, cites: [{source: S1, locator: "Early life and career"}], how_known: "Britannica."}
    - {value: "Brought up 'without any religious belief'; his father, raised a Scotch Presbyterian, held that 'concerning the origin of things nothing whatever can be known'", role: "family", certainty: 0.7, cites: [{source: S2, locator: "ch. 2"}], how_known: "Autobiography."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Educated at home by his father", certainty: 0.7, cites: [{source: S1, locator: "Early life and career"}], how_known: "Britannica."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1843–1859", certainty: 0.7, cites: [{source: S3, locator: "para. 4"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: 
    value: AGNOS
    basis: written_profession
    certainty: 0.5
    cites: [{source: S2, locator: "ch. 2"}]
    how_known: "His own Autobiography, published 1873, after the span, and describing his upbringing (P20 cap 0.5); Project Gutenberg transcription."
    rationale: "He 'never had' religious belief and 'grew up in a negative state with regard to it', taught that 'Who made me?' 'cannot be answered' (S2). Alternative BELOW_THRESHOLD: the passage reports an upbringing and absence of belief, not a settled adult stance; Three Essays on Religion (1874, not read) is a lead toward a limited creator."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Coded at 0.5: Autobiography ch. 2."}
    - {code: SECHUM, reason: "Lead: 'Religion of Humanity' (later chapters; not scored)."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Agnosticism states no locus: 'Who made me?' 'cannot be answered' (S2)."}
    B_cause: {value: UNKNOWN, how_known: "Philosopher, not a scientist (P30): A System of Logic treats inductive method, not a result about natural systems; his view of causation is a lead (System of Logic, Book III), not read."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Lead: the duty 'of collecting and weighing evidence for himself' (S1); not scored."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied."}
  statements:
    - text: "I am thus one of the very few examples, in this country, of one who has not thrown off religious belief, but never had it: I grew up in a negative state with regard to it. I looked upon the modern exactly as I did upon the ancient religion, as something which in no way concerned me."
      cites: [{source: S2, locator: "ch. 2"}]
      date: "1873"
      context: "Autobiography, ch. 2, on his upbringing; published posthumously 1873, after the span."
      axes: [A_locus]
      kind: "autobiography"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Project Gutenberg eBook #10378."
    - text: "he impressed upon me from the first, that the manner in which the world came into existence was a subject on which nothing was known: that the question, \"Who made me?\" cannot be answered, because we have no experience or authentic information from which to answer it"
      cites: [{source: S2, locator: "ch. 2"}]
      date: "1873"
      context: "Autobiography, ch. 2: his father's teaching, which he reports he grew up within."
      axes: [A_locus]
      kind: "autobiography"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Reports his father's teaching; backs the AGNOS reading only together with the first statement."
  changes_over_life: []
  coder_notes: "Read 'Theism' in Three Essays on Religion (1874) and System of Logic Book III (causation, 'Of the Law of Universal Causation'); a scholar's account (Anschutz's later sections; SEP 'John Stuart Mill')."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: "none (father had rejected Scotch Presbyterianism)", certainty: 0.7, cites: [{source: S2, locator: "ch. 2"}], how_known: "Autobiography."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1843–1859", certainty: 0.7, cites: [{source: S3, locator: "para. 4"}], how_known: "From A System of Logic (1843) to On Liberty (1859), the listed lasting works (P29, P30 #1)."}
  age_at_first_lasting_contribution: {value: 37, certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S3, locator: "para. 4"}], how_known: "1843 − 1806 = 37 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Inductive logic and ethics (S1).", certainty: 0.5, cites: [{source: S1, locator: "Introduction"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "East India Company (India House)", role: "examiner", years: "1823–1858", kind: "employer", certainty: 0.5, cites: [{source: S1, locator: "Early life and career"}], how_known: "Britannica; chief examiner from 1856; end year the Company's dissolution (coder's knowledge)."}
collaborators:
  - {value: "James Mill", relation: "family", note: "father and teacher", certainty: 0.7, cites: [{source: S1, locator: "Early life and career"}], how_known: "Britannica."}
  - {value: "Jeremy Bentham", relation: "influenced by", note: "utilitarianism", certainty: 0.7, cites: [{source: S1, locator: "Early life and career"}], how_known: "Britannica."}
  - {value: "Harriet Taylor Mill", relation: "family", note: "wife from 1851; helped revise On Liberty", certainty: 0.7, cites: [{source: S3, locator: "para. 3–4"}], how_known: "Britannica students."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 193"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Profession after the span and about upbringing."
  open_questions:
    - "Theism (1874); System of Logic on causation."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Richard Paul Anschutz"
    citation: "Anschutz, Richard Paul. 'John Stuart Mill.' Encyclopaedia Britannica. https://www.britannica.com/biography/John-Stuart-Mill"
    url: "https://www.britannica.com/biography/John-Stuart-Mill"
    accessed: 2026-10-19
    reliability_note: "Signed article; the fetched copy covers the summary and 'Early life and career' only."
    used_for: [identity, basics, contribution, childhood, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "John Stuart Mill"
    citation: "Mill, John Stuart. Autobiography (London, 1873). Project Gutenberg eBook #10378. https://www.gutenberg.org/ebooks/10378"
    url: "https://www.gutenberg.org/ebooks/10378"
    accessed: 2026-10-19
    reliability_note: "Transcription of the 1873 text; chapter 2 read."
    used_for: [childhood, worldview, heritage]
  - id: S3
    type: tertiary
    kind: "encyclopedia"
    author: "Britannica Editors"
    citation: "'John Stuart Mill.' Britannica (students edition). https://kids.britannica.com/students/article/John-Stuart-Mill/275842"
    url: "https://kids.britannica.com/students/article/John-Stuart-Mill/275842"
    accessed: 2026-10-19
    reliability_note: "Encyclopedia article, read in full; unsigned."
    used_for: [basics, contribution, timing]
  - id: S4
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

John Stuart Mill (1806–1873), philosopher and economist [S1]. Draft: AGNOS (0.5); A BELOW_THRESHOLD. Not plotted.

## Life and work

London; Avignon [S1].

## Contribution and impact

A System of Logic (1843); On Liberty (1859) [S1, S3].

## Childhood and education

At home, by his father [S1].

## Adult working worldview

'never had' religious belief (1873) [S2].

## Heritage (context only)

No religion; father ex-Presbyterian [S2].

## Timing

1843–1859, age 37 [S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Theism; causation.

## Research log

- 2026-10-19: Read Britannica (Anschutz, partly; students); Autobiography ch. 2.
