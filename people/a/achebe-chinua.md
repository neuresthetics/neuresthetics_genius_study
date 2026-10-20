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
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z5, order P32: F 3, rank 156; Caroline Herschel at rank 155 already coded). Basics from the Paris Review interview (Jerome Brooks, Art of Fiction No. 139, Winter 1994) and Innes's Cambridge study (chapter 'Origins', via excerpt). Own words: memoir There Was a Country (2012) as excerpted in Guernica (15 October 2012): 'I often had periods of oscillating faith as I grew older, periods of doubt'; struggled with 'the certitude of Christianity'; Igbo proverbs 'far more valuable to me ... than the doctrinaire, self-righteous strain of the Christian faith I was taught'. After the span (P20). Not a scientist. Span 1958 at 0.5. primary_system BELOW_THRESHOLD (lead CHRIST); A BELOW_THRESHOLD; B UNKNOWN; C, D, E UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: achebe-chinua
  display_name: "Chinua Achebe"
  roster:
    canonical_name: "Chinua Achebe"
    rank: 156
    F: 3
    models: [Gemini, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: literature
    field_bucket: literature
  full_name: {value: "Albert Chinualumogu Achebe", certainty: 0.7, cites: [{source: S3, locator: "opening"}], how_known: "Innes: 'christened Albert Chinualumogu'."}
  native_name: {value: "Chinua Achebe", certainty: 0.7, cites: [{source: S1, locator: "headnote"}], how_known: "Paris Review."}
  aliases:
    - {name: "Achebe-Chinua", kind: "roster alias"}
    - {name: "Chinua-Achebe", kind: "roster alias"}

basics:
  birth:
    date: {value: "1930-11-16", calendar: gregorian, certainty: 0.7, cites: [{source: S3, locator: "opening"}], how_known: "Innes."}
    place: {value: "Ogidi, Eastern Nigeria", modern_name: "Ogidi, Anambra State, Nigeria", polity_then: "British colony of Nigeria", certainty: 0.5, cites: [{source: S3, locator: "opening"}], how_known: "Innes: born in Eastern Nigeria; family settled in Ogidi five years after the fifth child's birth, so birthplace 0.5."}
  death:
    date: {value: UNKNOWN, how_known: "Not in the sources read."}
    place: {value: UNKNOWN, how_known: "Not in the sources read."}
  first_lasting_contribution_year: {value: 1958, certainty: 0.7, cites: [{source: S1, locator: "headnote"}], how_known: "Things Fall Apart, 1958."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "headnote"}], how_known: "1958 (P2)."}
  region_of_birth: {value: "Sub-Saharan Africa", certainty: 0.7, cites: [{source: S3, locator: "opening"}], how_known: "Nigeria (P3)."}
  region_of_work: {value: "Sub-Saharan Africa", certainty: 0.7, cites: [{source: S1, locator: "headnote"}], how_known: "Nigerian Broadcasting Corporation, Lagos."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Paris Review."}
  occupations: {value: ["novelist", "radio producer", "editor", "professor"], certainty: 0.7, cites: [{source: S1, locator: "headnote"}], how_known: "Paris Review."}

contribution:
  fields: {value: ["literature"], certainty: 0.7, cites: [{source: S1, locator: "headnote"}], how_known: "Paris Review."}
  lasting_original_contributions:
    - {value: "Things Fall Apart", year: 1958, kind: work, lasting: "first of his five novels, title discussed at length (S1); the coder's call that it is lasting", certainty: 0.5, cites: [{source: S1, locator: "headnote"}], how_known: "Paris Review lists it; lastingness not stated in what was read."}
  evidence_of_impact: []
  major_works:
    - {value: "Arrow of God", year: 1964, kind: book, certainty: 0.7, cites: [{source: S1, locator: "headnote"}], how_known: "Paris Review."}
    - {value: "Anthills of the Savannah", year: 1987, kind: book, certainty: 0.7, cites: [{source: S1, locator: "headnote"}], how_known: "Paris Review."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founding novelist of modern African literature in English (coder's reading; not stated in what was read).", certainty: 0.5, cites: [{source: S1, locator: "headnote"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Anglican (Church Missionary Society) converts", certainty: 0.7, cites: [{source: S1, locator: "first answer"}, {source: S3, locator: "opening"}], how_known: "(interview) 'My parents were early converts to Christianity'; father a CMS catechist (Innes)."}
  family_religious_practice: {value: "Bible readings at prayer time, memorization, Sunday school", certainty: 0.5, cites: [{source: S2, locator: "excerpt"}], how_known: "Memoir (2012)."}
  parents_and_household:
    - {value: "Isaiah Okafor Achebe, father, CMS catechist and evangelist", role: father, certainty: 0.7, cites: [{source: S3, locator: "opening"}], how_known: "Innes."}
    - {value: "Janet Achebe, mother, Christian convert", role: mother, certainty: 0.7, cites: [{source: S3, locator: "opening"}], how_known: "Innes."}
  household_circumstances: {value: "Fifth of six children; father retired to the ancestral village", certainty: 0.7, cites: [{source: S1, locator: "first answer"}], how_known: "(interview)."}
  schooling:
    - {value: "University College, Ibadan (London degree)", stage: university, run_by: "state or municipal", years: "1940s–1950s", certainty: 0.5, cites: [{source: S1, locator: "Ibadan answer"}], how_known: "(interview); run_by and years the coder's."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading:
    - {value: "Igbo translation of The Pilgrim's Progress", certainty: 0.5, cites: [{source: S2, locator: "excerpt"}], how_known: "Memoir."}
  childhood_mentors:
    - {value: "Udoh Osinyi, great-uncle, ozo titleholder", certainty: 0.5, cites: [{source: S2, locator: "excerpt"}], how_known: "Memoir."}
  languages_in_childhood: {value: ["Igbo", "English"], certainty: 0.5, cites: [{source: S1, locator: "first answer"}], how_known: "Inferred."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1958", certainty: 0.5, cites: [{source: S1, locator: "headnote"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "(memoir, 2012, after the span, P20) Raised Anglican; 'periods of oscillating faith ... periods of doubt'; questions Christian 'certitude' but not 'its accuracy'; prefers Igbo proverbs. No profession stated. Lead CHRIST (upbringing); Igbo traditional religion is an interest, not a profession."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Lead: upbringing; doubts stated."}
    - {code: ANIM, reason: "Rejected: admiration for Igbo religion is artistic and cultural ('far more artistically satisfying')."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "(memoir, after the span) Doubt and oscillation; no locus stated."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); nothing read on nature."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN, which takes precedence (§6, P19)."}
  statements:
    - text: "I often had periods of oscillating faith as I grew older, periods of doubt, when I quietly pondered, and deeply questioned, the absolutist teachings or the interpretations of religion. I struggled with the certitude of Christianity—“I am the Way, the Truth and the Life”—not its accuracy, because as a writer one understands that there should be such latitude, but the desolation, the acerbity of its meaning, the lack of options for the outsider, the other."
      cites: [{source: S2, locator: "excerpt"}]
      date: "2012"
      context: "There Was a Country (2012), excerpt in Guernica; after the span."
      axes: [A_locus]
      kind: "autobiography"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
  changes_over_life: []
  coder_notes: "Read 'Named for Victoria, Queen of England' (1973) and in-span interviews for a stated position."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Igbo", certainty: 0.7, cites: [{source: S1, locator: "first answer"}], how_known: "(interview)."}
  religious_heritage_by_birth: {value: "Anglican Christian", certainty: 0.7, cites: [{source: S3, locator: "opening"}], how_known: "Innes."}
  baptism_or_initiation: {value: "Christened Albert Chinualumogu", certainty: 0.7, cites: [{source: S3, locator: "opening"}], how_known: "Innes."}
  childhood_catechism: {value: "Sunday school", certainty: 0.5, cites: [{source: S2, locator: "excerpt"}], how_known: "Memoir."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1958", certainty: 0.5, cites: [{source: S1, locator: "headnote"}], how_known: "Things Fall Apart, the only work the coder takes as lasting from what was read (P29, P30); later novels are candidates."}
  age_at_first_lasting_contribution: {value: 28, certainty: 0.7, cites: [{source: S3, locator: "opening"}, {source: S1, locator: "headnote"}], how_known: "1958 − 1930 = 28 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None in span."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Fiction (S1).", certainty: 0.5, cites: [{source: S1, locator: "headnote"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "headnote"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Nigerian Broadcasting Corporation", role: "radio producer; Director of External Broadcasting", years: "1950s–1960s", kind: "government or state body", certainty: 0.5, cites: [{source: S1, locator: "headnote"}], how_known: "Paris Review; years the coder's."}
collaborators:
  - {value: "Geoffrey Parrinder", relation: teacher, note: "West African religions at Ibadan", certainty: 0.7, cites: [{source: S1, locator: "Ibadan answer"}], how_known: "(interview)."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 156"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Britannica would not load; basics from the Paris Review and Innes."
  open_questions:
    - "Death date and place from a tertiary source; in-span words on religion."

sources:
  - id: S1
    type: primary
    kind: other
    author: "Chinua Achebe, interviewed by Jerome Brooks"
    citation: "Brooks, Jerome. \"Chinua Achebe, The Art of Fiction No. 139.\" The Paris Review 133 (Winter 1994). https://www.theparisreview.org/interviews/1720/the-art-of-fiction-no-139-chinua-achebe"
    url: "https://www.theparisreview.org/interviews/1720/the-art-of-fiction-no-139-chinua-achebe"
    accessed: 2026-10-19
    reliability_note: "Published interview transcript (P8) with an editorial headnote."
    used_for: [identity, basics, contribution, childhood, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Chinua Achebe"
    citation: "Achebe, Chinua. \"How Things Fell Apart\" (excerpt from There Was a Country, Penguin 2012). Guernica, 15 October 2012. https://www.guernicamag.com/how-things-fell-apart/"
    url: "https://www.guernicamag.com/how-things-fell-apart/"
    accessed: 2026-10-19
    reliability_note: "Authorized excerpt of his memoir."
    used_for: [childhood, worldview, heritage]
  - id: S3
    type: secondary
    kind: "book chapter"
    author: "C. L. Innes"
    citation: "Innes, C. L. \"Origins.\" In Chinua Achebe (Cambridge University Press, 1990). doi:10.1017/cbo9780511554407.003"
    url: "https://doi.org/10.1017/cbo9780511554407.003"
    accessed: 2026-10-19
    reliability_note: "Scholarly monograph; opening read via excerpt."
    used_for: [identity, basics, childhood, heritage, timing]
  - id: S4
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

Chinua Achebe (b. 1930), novelist [S1]. Draft: primary and A BELOW_THRESHOLD (lead CHRIST); B UNKNOWN. Not plotted.

## Life and work

Ogidi, Ibadan, Lagos, upstate New York [S1, S3].

## Contribution and impact

Things Fall Apart (1958) [S1].

## Childhood and education

Catechist's son at the 'crossroads of cultures' [S2, S3].

## Adult working worldview

Oscillating faith, by his 2012 account [S2].

## Heritage (context only)

Igbo; Anglican [S1, S3].

## Timing

1958, age 28 [S1, S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- In-span words.

## Research log

- 2026-10-19: Read Paris Review interview; Guernica memoir excerpt; Innes excerpt.
