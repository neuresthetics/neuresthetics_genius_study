---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch L)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-15
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch L, order P32: F 5, rank 77). Basics from Britannica (Michael Aaron Dennis); Top Questions not cited. Worldview from his own essay 'The World Wide Web and the \"Web of Life\"' (1998, w3.org). Not a scientist under P30 (computer science). primary_system BELOW_THRESHOLD (Unitarian Universalist, no study code); A BELOW_THRESHOLD; B UNKNOWN (P16); mid_basin UNKNOWN (P19). Not plotted. Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Audit fixes (fallacy_catalog audit of 2742382, run 1). No change: primary_system stays BELOW_THRESHOLD (no UU code, not mapped to SECHUM); UU recorded under nominal_affiliations."}

identity:
  id: berners-lee-tim
  display_name: "Tim Berners-Lee"
  roster:
    canonical_name: "Tim Berners-Lee"
    rank: 77
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: computer science
    field_bucket: "computer science / AI"
  full_name: {value: "Timothy Berners-Lee", certainty: 0.5, cites: [{source: S1, locator: "header"}], how_known: "Britannica gives 'Sir Tim Berners-Lee'; full given name not shown (0.5)."}
  native_name: {value: UNKNOWN, how_known: "English."}
  aliases:
    - {name: "Sir Tim Berners-Lee", kind: "title or honorific"}

basics:
  birth:
    date: {value: "1955-06-08", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "London, England", modern_name: "London, United Kingdom", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: UNKNOWN, how_known: "Living (Britannica gives age 71)."}
    place: {value: UNKNOWN, how_known: "Living."}
  first_lasting_contribution_year: {value: 1989, certainty: 0.7, cites: [{source: S1, locator: "CERN paragraph"}], how_known: "Proposal for a global hypertext system (1989), the Web's founding document (P30)."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Birth year bucket (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United Kingdom (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.5, cites: [{source: S1, locator: "CERN paragraph"}], how_known: "CERN, Geneva, for the Web's invention; later the United States (0.5)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [English], certainty: 0.7, cites: [{source: S2, locator: "text"}], how_known: "His own essay."}
  occupations: {value: ["computer scientist", "software engineer"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
contribution:
  fields: {value: ["computer science"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Proposal for a global hypertext document system using the Internet", year: 1989, kind: invention, lasting: "the World Wide Web (S1)", certainty: 0.7, cites: [{source: S1, locator: "CERN paragraph"}], how_known: "Britannica."}
    - {value: "First Web server and first Web client (browser)", year: 1991, kind: invention, lasting: "'one of the technological wonders of the computer age' (S1)", certainty: 0.7, cites: [{source: S1, locator: "CERN paragraph"}], how_known: "Written October 1990 to summer 1991; end year used."}
  evidence_of_impact:
    - {value: "Knighthood and inaugural Millennium Technology Prize (2004)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours:
    - {value: "Millennium Technology Prize", year: 2004, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Church of England (Protestant)", certainty: 0.7, cites: [{source: S2, locator: "'Where I'm coming from'"}], how_known: "His own essay."}
  family_religious_practice: {value: "Religious upbringing; confirmed as a teenager", certainty: 0.7, cites: [{source: S2, locator: "'Where I'm coming from'"}], how_known: "His own essay."}
  parents_and_household:
    - {value: "Both parents worked on the Ferranti Mark I computer", role: parents, certainty: 0.7, cites: [{source: S1, locator: "paragraph 2"}], how_known: "Britannica."}
  household_circumstances: {value: TODO}
  schooling:
    - {value: "University of Oxford (graduated 1976)", stage: university, run_by: other, certainty: 0.7, cites: [{source: S1, locator: "paragraph 2"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [English], certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "Rejected his Church of England upbringing as a teenager, just after confirmation", certainty: 0.7, cites: [{source: S2, locator: "'Where I'm coming from'"}], how_known: "His own essay; no year given."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1989–1991", certainty: 0.7, cites: [{source: S1, locator: "CERN paragraph"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Unitarian Universalist congregation (Boston area), joined after having children", years: "by 1998", role: member, certainty: 0.7, cites: [{source: S2, locator: "'Where I'm coming from'"}], how_known: "His own essay; he 'came across Unitarian Universalism' after developing the Web."}
  self_described_science_religion_relation: {value: "UUs 'allow or even require their belief to be compatible with reason' (1998).", certainty: 0.7, cites: [{source: S2, locator: "'Where I'm coming from'"}], how_known: "His own essay."}
  primary_system:
    value: BELOW_THRESHOLD
    basis: written_profession
    certainty: 0.5
    cites: [{source: S2, locator: "'Where I'm coming from'; 'Tolerance'"}]
    rationale: "A Unitarian Universalist from after the working years; the study has no UU system code, and the essay states no view of God ('those who believe in some sort of a God different from theirs (if they use the term)'). Candidates SECHUM and CHRIST (liberal, 'Christian philosophy but without the dogma'). Kept BELOW_THRESHOLD after the batch L audit; UU is recorded under nominal_affiliations."
    how_known: "His own essay (1998), after the working years (1989–91)."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: SECHUM, reason: "Values of 'the fundamental value and dignity of every human being'; no God stated."}
    - {code: CHRIST, reason: "Sought 'the basis for Christian philosophy but without the dogma'."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "The essay places no God and leaves the term optional ('if they use the term')."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist under P30; no statement about nature read (P16)."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Rejecting dogma and 'the One True Churches' bears on D; not scored at this reading (coder's call)."}
    E_scope: {value: UNKNOWN, how_known: "Not read (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "B is UNKNOWN; UNKNOWN takes precedence (P19)."}
  statements:
    - text: "Like many people, I had a religious upbringing which I rejected as a teenager: in my case it was a protestant Christian (Church of England) upbringing."
      cites: [{source: S2, locator: "'Where I'm coming from'"}]
      date: "1998"
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-15
      note: "His own page on w3.org."
    - text: "They respect those who believe in some sort of a God different from theirs (if they use the term)."
      cites: [{source: S2, locator: "'Tolerance'"}]
      date: "1998"
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-15
      note: "About UUs in general, not a statement of his own belief."
  changes_over_life:
    - {value: "Rejected Church of England upbringing as a teenager; joined a Unitarian Universalist church after having children", certainty: 0.7, cites: [{source: S2, locator: "'Where I'm coming from'"}], how_known: "His own essay; no years given."}
  coder_notes: "Coder's call; one essay. The study's system list has no Unitarian Universalist code (flag for a decision if UU members recur)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Church of England", certainty: 0.7, cites: [{source: S2, locator: "'Where I'm coming from'"}], how_known: "His own essay."}
  baptism_or_initiation: {value: "Confirmed in the Church of England as a teenager", certainty: 0.7, cites: [{source: S2, locator: "'Where I'm coming from'"}], how_known: "His own essay."}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1989–1991", certainty: 0.7, cites: [{source: S1, locator: "CERN paragraph"}], how_known: "First to last listed lasting contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 34, certainty: 0.7, cites: [{source: S1, locator: "opening; CERN paragraph"}], how_known: "1989 − 1955 = 34 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None scored."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "None scored."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "He joined UU after the Web; nothing read from 1989–91."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not read.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Not read."}
  circle_present: {value: "unclear", rationale: "No God statement.", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Coder's reading."}
  reading: "Liberal religious humanism; God not stated."
  notes: ""

institutions:
  - {value: "CERN", role: "software engineer", kind: "research institute", certainty: 0.7, cites: [{source: S1, locator: "CERN paragraph"}], how_known: "Britannica."}
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 77"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags: []
  open_questions:
    - "Find any statement of his own on God or on nature."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Michael Aaron Dennis"
    citation: "Dennis, Michael Aaron. \"Tim Berners-Lee.\" Encyclopaedia Britannica, updated 26 September 2026. https://www.britannica.com/biography/Tim-Berners-Lee."
    url: "https://www.britannica.com/biography/Tim-Berners-Lee"
    accessed: 2026-10-15
    reliability_note: "Signed body (with Britannica Editors); Top Questions (AI-generated) not cited."
    used_for: [identity, basics, contribution, childhood, heritage, timing, lane_b, institutions]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Tim Berners-Lee"
    citation: "Berners-Lee, Tim. \"The World Wide Web and the 'Web of Life'.\" 1998. https://www.w3.org/People/Berners-Lee/UU.html."
    url: "https://www.w3.org/People/Berners-Lee/UU.html"
    accessed: 2026-10-15
    reliability_note: "His own page on the W3C site."
    used_for: [basics, childhood, worldview, heritage, timing, lane_b]
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

# Tim Berners-Lee

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Tim Berners-Lee (born 1955), British computer scientist, inventor of the World Wide Web [S1]. Draft: primary_system BELOW_THRESHOLD (Unitarian Universalist); A BELOW_THRESHOLD; B UNKNOWN; mid_basin UNKNOWN. Not plotted.

## Life and work

Oxford; Plessey; CERN [S1].

## Contribution and impact

Web proposal (1989); first server and browser (1990–91) [S1].

## Childhood and education

Church of England upbringing, rejected as a teenager [S2].

## Adult working worldview

Unitarian Universalist by 1998 [S2].

## Heritage (context only)

Church of England [S2].

## Timing

First lasting contribution 1989, at 34 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Unclear [S2].

## Open questions

- A statement of his own on God or nature.

## Research log

- 2026-10-15: Read Britannica (Dennis) and his 1998 UU essay on w3.org.
