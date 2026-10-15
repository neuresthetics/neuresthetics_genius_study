---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch D)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-15
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch D, order P32: F 5, rank 10). Basics from her Nobel autobiographical note and the NLM Profiles in Science overview; paper dates from Europe PMC records of PNAS. No statement of hers on religion, God or nature was read. primary_system UNKNOWN; B_cause 3 at 0.5 from working science (P35, alternative 4); A, C, D UNKNOWN; E BELOW_THRESHOLD; mid_basin UNKNOWN. Draft, not reviewed."}

identity:
  id: mcclintock-barbara
  display_name: "Barbara McClintock"
  roster:
    canonical_name: "Barbara McClintock"
    rank: 10
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: genetics
    field_bucket: "biology / life science"
  full_name: {value: "Barbara McClintock", certainty: 1.0, cites: [{source: S1, locator: "heading"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources."}
  native_name: {value: TODO}
  aliases:
    - {name: "Barbara-McClintock", kind: "roster alias"}
    - {name: "McClintock-Barbara", kind: "roster alias"}

basics:
  birth:
    date: {value: "1902-06-16", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "table ('Hartford, Connecticut, U.S.A, 16 June, 1902')"}, {source: S2, locator: "paragraph 1"}], how_known: "Her own Nobel note and NLM agree."}
    place: {value: "Hartford, Connecticut", modern_name: "Hartford, Connecticut, USA", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "table"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources."}
  death:
    date: {value: "1992-09-02", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "closing note"}, {source: S2, locator: "last paragraph"}], how_known: "Two sources."}
    place: {value: "Huntington Hospital, near Cold Spring Harbor, New York", modern_name: "Huntington, New York, USA", polity_then: "United States", certainty: 0.7, cites: [{source: S2, locator: "last paragraph"}], how_known: "NLM alone."}
  first_lasting_contribution_year: {value: 1931, certainty: 1.0, cites: [{source: S3, locator: "PNAS 17(8):492–497, August 1931"}, {source: S2, locator: "paragraph 4 (physical correlate of crossing-over)"}], how_known: "Creighton and McClintock's cytological proof of crossing-over, published August 1931 (primary journal record), the earliest listed lasting contribution (P30)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S3, locator: "1931"}], how_known: "From 1931 (P2)."}
  region_of_birth: {value: "North America", certainty: 1.0, cites: [{source: S1, locator: "table"}, {source: S2, locator: "paragraph 1"}], how_known: "USA (P3)."}
  region_of_work: {value: "North America", certainty: 1.0, cites: [{source: S1, locator: "positions held"}, {source: S2, locator: "paragraphs 2–3"}], how_known: "Cornell, Missouri, Cold Spring Harbor."}
  sex_as_recorded: {value: "female", certainty: 1.0, cites: [{source: S2, locator: "paragraph 1 ('She')"}, {source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [English], certainty: 1.0, cites: [{source: S3, locator: "title"}, {source: S4, locator: "title"}], how_known: "Her papers are in English."}
  occupations: {value: ["cytogeneticist", "research scientist"], certainty: 1.0, cites: [{source: S1, locator: "text and positions"}, {source: S2, locator: "paragraphs 1–3"}], how_known: "Two sources."}

contribution:
  fields: {value: ["cytogenetics", "maize genetics"], certainty: 1.0, cites: [{source: S1, locator: "paragraph 3"}, {source: S2, locator: "paragraph 4"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Cytological proof that genetic crossing-over goes with physical exchange between chromosomes (with Harriet Creighton)", year: 1931, kind: discovery, lasting: "physical basis of genetic recombination", certainty: 1.0, cites: [{source: S3, locator: "PNAS 17:492–497 (1931)"}, {source: S2, locator: "paragraph 4"}], how_known: "Primary record and NLM."}
    - {value: "Transposition ('mobile genetic elements') and gene control in maize", year: 1950, kind: discovery, lasting: "Nobel Prize 1983 for mobile genetic elements", certainty: 1.0, cites: [{source: S4, locator: "PNAS 36:344–355 (June 1950)"}, {source: S2, locator: "paragraphs 4–6"}], how_known: "Earliest documented public statement read is the 1950 PNAS paper; NLM places the work in the 1940s and 1950s, so the year might be earlier (a 1948 Carnegie Year Book report was not read)."}
  evidence_of_impact:
    - {value: "Nobel Prize in Physiology or Medicine 1983, unshared", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S2, locator: "paragraph 6"}], how_known: "NLM."}
  major_works:
    - {value: "The origin and behavior of mutable loci in maize, PNAS 36: 344–355", year: 1950, kind: "paper or paper series", certainty: 1.0, cites: [{source: S4, locator: "record"}], how_known: "Primary record."}
  honours:
    - {value: "National Medal of Science", year: 1970, certainty: 0.5, cites: [{source: S1, locator: "awards (1970)"}, {source: S2, locator: "paragraph 6 (1971)"}], how_known: "Real dispute on the year: her Nobel list says 1970, NLM says 1971.", alternatives: [{value: "1971", cites: [{source: S2, locator: "paragraph 6"}]}]}
  definition_fit: {value: "clearly meets", rationale: "Discovered transposition; physical basis of crossing-over.", certainty: 1.0, cites: [{source: S2, locator: "paragraphs 4–6"}, {source: S3, locator: "record"}], how_known: "Two sources."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not in the sources read."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not in the sources read."}
  parents_and_household:
    - {value: "One of four children of Thomas Henry McClintock and Sara Handy McClintock", role: other, certainty: 0.7, cites: [{source: S2, locator: "paragraph 1"}], how_known: "NLM alone."}
  household_circumstances: {value: TODO}
  schooling:
    - {value: "Erasmus Hall High School, Brooklyn; graduated 1919", stage: "grammar or secondary school", years: "–1919", certainty: 1.0, cites: [{source: S1, locator: "table"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1931–1950", certainty: 1.0, cites: [{source: S3, locator: "1931"}, {source: S4, locator: "1950"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No statement of hers on science and religion in the Nobel note or the NLM overview; a web search found only secondary paraphrase of Keller's 1983 biography, not read."}
  primary_system: {value: UNKNOWN, cites: [{source: S1, locator: "whole note"}, {source: S2, locator: "whole overview"}], how_known: "Nothing on religion or God in the sources read (P19).", note: "Lead: Evelyn Fox Keller, A Feeling for the Organism (1983), based on interviews; Nathaniel Comfort, The Tangled Field (2001). Her reported interest in Tibetan Buddhism and mysticism is known to the coder only from secondary paraphrase and is not used."}
  secondary_system: {value: UNKNOWN, how_known: "No system evidence."}
  candidate_codes_considered: []
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing of hers on God in the sources read (P19)."}
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      cites: [{source: S3, locator: "1931 paper"}, {source: S4, locator: "1950 paper"}]
      how_known: "Coder's reading of her working science (P24, P30); no statement of her own on law and exception."
      rationale: "Scored on her account of nature (P6). Her results explain heredity and mutation by physical mechanisms (chromosome exchange, transposable elements), with no exception or intervention. P35: B 3 at 0.5, named alternative 4."
    C_ledger: {value: UNKNOWN, how_known: "Nothing in the sources read (P19)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing on revelation; working science does not bear on D (P19)."}
    E_scope: {value: BELOW_THRESHOLD, note: "Scored on the world's order (P7); not scored from working science alone.", how_known: "BELOW_THRESHOLD under P19."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, which takes precedence (§6, P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "statements is empty: no religious or metaphysical statement of hers was read. The NLM epigraph ('I never felt the need nor the desire to defend my views') is about science and is not used."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: TODO}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not in the sources read."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not in the sources read."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not in the sources read."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1931–1950", certainty: 1.0, cites: [{source: S3, locator: "1931"}, {source: S4, locator: "1950"}], how_known: "First to last listed lasting contribution (P29, P30). Her later South American maize work (published 1981) is not listed as lasting."}
  age_at_first_lasting_contribution: {value: 29, certainty: 1.0, cites: [{source: S3, locator: "1931"}, {source: S1, locator: "1902"}], how_known: "1931 − 1902 = 29 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement scored at 3 or 4 (P27)."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "Nothing on God or nature read.", certainty: 0.5, cites: [{source: S2, locator: "whole overview"}], how_known: "Absence in the sources read."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Experimental cytogenetics; nothing read on proof training.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Nothing read."}
  circle_present: {value: "unclear", rationale: "No God–Nature statement read.", certainty: 0.5, cites: [{source: S2, locator: "whole"}], how_known: "No evidence."}
  reading: "As belief, not finding: form and circle unclear. Does not test H1."
  notes: ""

institutions:
  - {value: "Cornell University", role: "student (B.S. 1923, M.A. 1925, Ph.D. 1927), instructor, research associate", years: "1919–1936", kind: university, certainty: 1.0, cites: [{source: S1, locator: "table"}, {source: S2, locator: "paragraphs 1–3"}], how_known: "Two sources."}
  - {value: "Carnegie Institution of Washington, Department of Genetics, Cold Spring Harbor", role: "staff member", years: "1942–1967", kind: "research institute", certainty: 1.0, cites: [{source: S1, locator: "positions"}, {source: S2, locator: "paragraph 3"}], how_known: "Two sources."}
collaborators:
  - {value: "Harriet B. Creighton", relation: collaborator, note: "co-author of the 1931 paper", certainty: 1.0, cites: [{source: S3, locator: "authors"}], how_known: "Primary record."}
  - {value: "George W. Beadle and Marcus M. Rhoades", relation: collaborator, note: "Cornell maize cytogenetics group", certainty: 0.7, cites: [{source: S1, locator: "paragraph 5"}], how_known: "Her own Nobel note (autobiographical; one source)."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 10"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "National Medal of Science year: 1970 (Nobel note) vs 1971 (NLM)."
    - "Britannica blocked (Cloudflare, 2026-10-15)."
  open_questions:
    - "Read Keller (1983) and Comfort (2001) for her own words on religion, mysticism and nature."

sources:
  - id: S1
    type: primary
    kind: "published work by the subject"
    author: "Barbara McClintock"
    year: 1984
    citation: "McClintock, Barbara. \"Barbara McClintock – Biographical.\" In Les Prix Nobel 1983, ed. Wilhelm Odelberg. Stockholm: Nobel Foundation, 1984. NobelPrize.org."
    url: "https://www.nobelprize.org/prizes/medicine/1983/mcclintock/biographical/"
    accessed: 2026-10-15
    reliability_note: "Autobiographical note written at the time of the award, with a table of dates and positions."
    used_for: [identity, basics, contribution, childhood, worldview, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "National Library of Medicine"
    citation: "National Library of Medicine. \"Biographical Overview.\" The Barbara McClintock Papers, Profiles in Science. https://profiles.nlm.nih.gov/spotlight/ll/feature/biographical-overview."
    url: "https://profiles.nlm.nih.gov/spotlight/ll/feature/biographical-overview"
    accessed: 2026-10-15
    reliability_note: "Archival institution's overview."
    used_for: [identity, basics, contribution, childhood, worldview, timing, lane_b, institutions]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Harriet B. Creighton and Barbara McClintock"
    year: 1931
    citation: "Creighton, Harriet B., and Barbara McClintock. \"A Correlation of Cytological and Genetical Crossing-Over in Zea Mays.\" PNAS 17, no. 8 (1931): 492–497. https://doi.org/10.1073/pnas.17.8.492."
    url: "https://doi.org/10.1073/pnas.17.8.492"
    accessed: 2026-10-15
    reliability_note: "Europe PMC record (PMC1076098) read for title, authors, volume and date."
    used_for: [basics, contribution, worldview, timing, collaborators]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Barbara McClintock"
    year: 1950
    citation: "McClintock, Barbara. \"The Origin and Behavior of Mutable Loci in Maize.\" PNAS 36, no. 6 (1950): 344–355. https://doi.org/10.1073/pnas.36.6.344."
    url: "https://doi.org/10.1073/pnas.36.6.344"
    accessed: 2026-10-15
    reliability_note: "Europe PMC record (PMC1063197) read for bibliographic data."
    used_for: [basics, contribution, worldview, timing]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Barbara McClintock

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Barbara McClintock (1902–1992), American cytogeneticist, gave with Harriet Creighton the cytological proof of crossing-over (1931) and discovered transposition in maize (1950 paper), for which she received the unshared 1983 Nobel Prize [S2; S3; S4]. No statement of hers on religion, God or nature was read. Draft: primary_system UNKNOWN; B 3 at 0.5 from working science (alternative 4, P35); A UNKNOWN; mid_basin UNKNOWN.

## Life and work

Cornell (Ph.D. 1927), Missouri (1936–1941), Cold Spring Harbor from 1942 [S1; S2].

## Contribution and impact

Crossing-over proof [S3]; mobile genetic elements [S4; S2].

## Childhood and education

Erasmus Hall High School, Brooklyn [S1; S2].

## Adult working worldview

Not established [S1; S2].

## Heritage (context only)

Not researched.

## Timing

First lasting contribution 1931, at 29 [S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Unclear.

## Open questions

- Keller (1983), Comfort (2001).

## Research log

- 2026-10-15: Read the Nobel note, NLM overview and Europe PMC records. Britannica blocked.
