---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA1, order P32: F 3, rank 181). Basics from NobelPrize.org (facts; autobiography 1978) and Britannica (archived 2020, body: 'his influential book Administrative Behavior (1947)'). Own words: Models of My Life (draft, Carnegie Mellon University Libraries, Simon papers), after the span: as a schoolboy in Christian Endeavor 'while insisting on his agnosticism' (before the span); at Chicago, 'neither of us being swept up by the theologies we encountered'; 'a logical positivism that I have never relinquished (I would prefer to call it empiricism now)'. A secondary account (Velupillai and Venkatachalam) says he 'described himself as an atheist' (no locator). No adult statement on God read, so primary_system BELOW_THRESHOLD (leads AGNOS, ATHE); A BELOW_THRESHOLD. Scientist: his decision theory makes testable claims about decision behaviour in organizations (P35 addendum), so B 3 at 0.5 from working science, alt 4. C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Span 1947, age 31. Not plotted. Draft, not reviewed."}

identity:
  id: simon-herbert
  display_name: "Herbert Simon"
  roster:
    canonical_name: "Herbert Simon"
    rank: 181
    F: 3
    models: [Claude, DeepSeek, GPT]
    band: "core (3–4)"
    status: "core"
    field: "computer science"
    field_bucket: "computer science / AI"
  full_name: {value: "Herbert Alexander Simon", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "Britannica."}
  native_name: {value: "Herbert A. Simon", certainty: 0.7, cites: [{source: S1, locator: "heading"}], how_known: "NobelPrize.org."}
  aliases:
    - {name: "Simon-Herbert", kind: "roster alias"}

basics:
  birth:
    date: {value: "1916-06-15", certainty: 0.7, cites: [{source: S1, locator: "Born"}], how_known: "NobelPrize.org."}
    place: {value: "Milwaukee, Wisconsin", modern_name: "Milwaukee, Wisconsin, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "Born"}], how_known: "NobelPrize.org."}
  death:
    date: {value: "2001-02-09", certainty: 0.7, cites: [{source: S1, locator: "Died"}], how_known: "NobelPrize.org."}
    place: {value: "Pittsburgh, Pennsylvania", modern_name: "Pittsburgh, Pennsylvania, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "Died"}], how_known: "NobelPrize.org."}
  first_lasting_contribution_year: {value: 1947, certainty: 0.7, cites: [{source: S2, locator: "para. 3"}], how_known: "'his influential book Administrative Behavior (1947)' (S2, body); publication (P30 #1)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S2, locator: "para. 3"}], how_known: "1947 (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "Born"}], how_known: "USA (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "Life"}], how_known: "Chicago; Pittsburgh."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S3, locator: "text"}], how_known: "English text."}
  occupations: {value: ["economist", "political scientist", "psychologist", "computer scientist"], certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["economics", "organization theory", "cognitive psychology", "artificial intelligence"], certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Theory of decision making in organizations and satisficing (Administrative Behavior)", year: 1947, kind: "theory", lasting: "'his influential book Administrative Behavior (1947)' (S2); Nobel Prize 1978 'for his pioneering research into the decision-making process within economic organizations' (S1)", certainty: 0.7, cites: [{source: S2, locator: "para. 3–4"}, {source: S1, locator: "Prize motivation"}], how_known: "Britannica body (archived) and NobelPrize.org."}
  evidence_of_impact:
    - {value: "Nobel Prize in Economic Sciences 1978; Turing Award 1975 (with Newell)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Nobel and Turing laureate (S2).", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Father an electrical engineer (Technische Hochschule Darmstadt diploma), an immigrant from Germany", role: "father", certainty: 0.7, cites: [{source: S1, locator: "autobiography"}], how_known: "NobelPrize.org autobiography."}
    - {value: "Mother an accomplished pianist, third-generation American", role: "mother", certainty: 0.7, cites: [{source: S1, locator: "autobiography"}], how_known: "NobelPrize.org autobiography."}
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
  working_years: {value: "1947", certainty: 0.7, cites: [{source: S2, locator: "para. 3"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "No adult statement on God read. Own words (Models of My Life, after the span): a schoolboy 'insisting on his agnosticism' (before the span); at Chicago 'neither of us being swept up by the theologies we encountered'; a lifelong 'logical positivism ... (I would prefer to call it empiricism now)'. A secondary account says he 'described himself as an atheist' (Velupillai and Venkatachalam, no locator, not read in full). Leads AGNOS and ATHE; neither is a first-person profession inside or about the span."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Lead: schoolboy agnosticism (own words, before the span)."}
    - {code: ATHE, reason: "Lead: secondary report that he called himself an atheist."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "No locus view read; logical positivism is a lead (God-talk meaningless), not a stated view on God."}
    B_cause: 
      value: 3
      basis: inference_from_work
      certainty: 0.5
      cites: [{source: S2, locator: "para. 3–4"}, {source: S1, locator: "Prize motivation"}]
      how_known: "Scientist (P30, P35 addendum): his decision theory makes testable empirical claims about decision processes in organizations (S1, S2). B from working science with no statement of his own on law and exception, so 3 at 0.5, alternative 4, never 4 (P24, P35)."
      rationale: "Theory of how people actually decide in organizations (S1, S2); lawful, empirically testable behaviour. Alternative 4."
      alternatives:
        - {value: 4, note: "Working science cannot tell lawful-with-exceptions from exceptionless (P35).", cites: [{source: S2, locator: "para. 3–4"}]}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read; logical positivism is a lead for D."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied."}
  statements:
    - text: "I had already embraced a logical positivism that I have never relinquished (I would prefer to call it empiricism now)"
      cites: [{source: S3, locator: "ch. 3, 'Education in Chicago, 1933–1937'"}]
      date: "1991"
      context: "Models of My Life (draft in the Simon papers); about his Chicago years, after the span in writing."
      axes: [D_authority]
      kind: "autobiography"
      verified_against: "primary facsimile"
      verified_on: 2026-10-19
      note: "Read from the OCR of the CMU Libraries scan of his typescript; page images not viewed. Not scored (no axis view on God or nature)."
  changes_over_life: []
  coder_notes: "Read the published Models of My Life (1991) for any adult statement on religion; check Velupillai's 'described himself as an atheist' at its source."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Lutheran and Jewish forebears; attended Congregational Sunday school", certainty: 0.5, cites: [{source: S1, locator: "autobiography"}, {source: S3, locator: "ch. 1"}], how_known: "Nobel autobiography lists the Lutheran Merkels and Prague Goldschmidts; Models of My Life: 'not a religious Jew ... attended Congregational Sunday school'."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1947", certainty: 0.7, cites: [{source: S2, locator: "para. 3"}], how_known: "Administrative Behavior (1947), the one listed lasting work (P29, P30)."}
  age_at_first_lasting_contribution: {value: 31, certainty: 0.7, cites: [{source: S1, locator: "Born"}, {source: S2, locator: "para. 3"}], how_known: "1947 − 1916 = 31 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Formal models of decision (S2).", certainty: 0.5, cites: [{source: S2, locator: "para. 3–4"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Carnegie Institute of Technology (Carnegie Mellon University)", role: "professor", years: "1949–2001", kind: "university", certainty: 0.7, cites: [{source: S2, locator: "para. 2"}], how_known: "Britannica; end year his death."}
collaborators:
  - {value: "Allen Newell", relation: "collaborator", note: "Turing Award 1975", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "Britannica."}
  - {value: "Harold Guetzkow", relation: "collaborator", note: "Chicago friend; organizational studies", certainty: 0.7, cites: [{source: S3, locator: "ch. 3"}], how_known: "Own words."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 181"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "No adult statement on God read."
  open_questions:
    - "Published Models of My Life; Velupillai."

sources:
  - id: S1
    type: tertiary
    kind: "institutional page"
    author: "Nobel Foundation"
    citation: "'Herbert A. Simon – Facts' and 'Biographical.' NobelPrize.org. https://www.nobelprize.org/prizes/economic-sciences/1978/simon/facts/"
    url: "https://www.nobelprize.org/prizes/economic-sciences/1978/simon/facts/"
    accessed: 2026-10-19
    reliability_note: "Official prize pages; autobiography written at the award."
    used_for: [identity, basics, contribution, childhood]
  - id: S2
    type: tertiary
    kind: "encyclopedia"
    author: "The Editors of Encyclopaedia Britannica (rev. William L. Hosch)"
    citation: "'Herbert A. Simon.' Encyclopaedia Britannica (last updated 11 June 2020). Archived 2020-07-31. https://web.archive.org/web/20200731075041/https://www.britannica.com/biography/Herbert-A-Simon"
    url: "https://web.archive.org/web/20200731075041/https://www.britannica.com/biography/Herbert-A-Simon"
    accessed: 2026-10-19
    reliability_note: "Archived article body, read in full."
    used_for: [identity, basics, contribution, timing, institutions, collaborators]
  - id: S3
    type: primary
    kind: "archive record"
    author: "Herbert A. Simon"
    citation: "Simon, Herbert A. Models of My Life (typescript draft). Herbert A. Simon Papers, Carnegie Mellon University Libraries, box 76, folder 5972. https://iiif.library.cmu.edu/file/Simon_box00076_fld05972_bdl0001_doc0001/Simon_box00076_fld05972_bdl0001_doc0001.pdf"
    url: "https://iiif.library.cmu.edu/file/Simon_box00076_fld05972_bdl0001_doc0001/Simon_box00076_fld05972_bdl0001_doc0001.pdf"
    accessed: 2026-10-19
    reliability_note: "Institution's scan of his typescript; read in OCR."
    used_for: [worldview, heritage, collaborators]
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

Herbert A. Simon (1916–2001), social scientist [S1, S2]. Draft: BELOW_THRESHOLD (leads AGNOS, ATHE); B 3 (0.5). Not plotted.

## Life and work

Milwaukee; Chicago; Carnegie Mellon [S1, S2].

## Contribution and impact

Decision making and satisficing; Administrative Behavior (1947) [S2].

## Childhood and education

Milwaukee public schools [S1].

## Adult working worldview

Schoolboy agnosticism; lifelong logical positivism [S3].

## Heritage (context only)

Jewish father; Congregational Sunday school [S3].

## Timing

1947, age 31 [S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Adult religious statement.

## Research log

- 2026-10-19: Read NobelPrize.org; Britannica (archived); Models of My Life typescript.
