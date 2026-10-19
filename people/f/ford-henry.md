---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Q)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-18
  last_updated: 2026-10-18
  change_log:
    - {date: 2026-10-18, by: "Grok Bot", summary: "Record created (stage 3 batch Q, order P32: F 4, rank 100). Basics from Britannica (Carol W. Gelderman, signed; body through the 1914 wage, read live). Worldview from two interviews: William L. Stidger's syndicated interview (Universal Service, printed 4 February 1923; OCR page image text on historyworm.com) and the San Francisco Examiner interview of 26 August 1928 as quoted by The Henry Ford (museum blog). Inventor, not a scientist (P33). primary_system BELOW_THRESHOLD (candidates CHRIST, THEOS); A 1 (0.5, alt 0); B UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-18, by: "Grok Bot", summary: "Batch Q audit notes (gs_0b3023d_Q run 1). Masthead reasoning added: most likely Hearst's Washington Herald (Universal Service was Hearst's wire; 'Washington Radio Herald' items on the page; the Times-Herald dates from 1939); the running head's '1928' is a slip (4 February 1923 was a Sunday). Creation entry's 'reincarnation belief' aligned to the candidate code THEOS. Values unchanged."}

identity:
  id: ford-henry
  display_name: "Henry Ford"
  roster:
    canonical_name: "Henry Ford"
    rank: 100
    F: 4
    models: [Claude, DeepSeek, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: invention
    field_bucket: "invention / engineering"
  full_name: {value: "Henry Ford", certainty: 0.7, cites: [{source: S1, locator: "title"}], how_known: "Britannica."}
  native_name: {value: UNKNOWN, how_known: "English."}
  aliases: []

basics:
  birth:
    date: {value: "1863-07-30", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "header dates; 'Early life'"}], how_known: "Britannica; born on the family farm near Dearborn."}
    place: {value: "Wayne county, Michigan (family farm near Dearborn)", modern_name: "Dearborn, Michigan, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  death:
    date: {value: "1947-04-07", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "header dates"}], how_known: "Britannica; 'when he died at age 83' (body)."}
    place: {value: "Dearborn, Michigan", modern_name: "Dearborn, Michigan, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "header dates"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1908, certainty: 0.7, cites: [{source: S1, locator: "'Early life' (Model T announced October 1908)"}], how_known: "Model T, announced October 1908; the 1896 Quadricycle is not called lasting in the body read (P23)."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "First lasting year 1908 (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "United States (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Detroit and Highland Park, Michigan."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  occupations: {value: ["industrialist", "engineer", "automobile manufacturer"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Early life'"}], how_known: "Britannica."}

contribution:
  fields: {value: ["automotive engineering", "mass production"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Model T automobile, 'the ordinary man's utility'", year: 1908, kind: invention, lasting: "'the chief instrument of one of the greatest and most rapid changes in the lives of the common people in history' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
    - {value: "Moving assembly line system at Highland Park (with his engineers)", year: "1913–1914", kind: method, lasting: "'the most advanced production technology yet conceived' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica ('the system that had evolved by 1913–14')."}
    - {value: "Five-dollar day and eight-hour shift", year: 1914, kind: method, lasting: "'these innovations changed the very structure of society' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "15,500,000 Model Ts sold in the United States over 19 years", kind: other, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "One of eight children of William and Mary Ford, farmers near Dearborn", role: parents, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  household_circumstances: {value: "Family farm", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  schooling:
    - {value: "One-room school for eight years", stage: "elementary school", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
    - {value: "Detroit machine shops from 16", stage: apprenticeship, run_by: other, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "Walked to Detroit to work in machine shops", year: 1879, certainty: 0.7, cites: [{source: S1, locator: "opening ('left his father's farm in 1879')"}], how_known: "Britannica."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1908–1914", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "'I was brought up in the church'", certainty: 0.5, cites: [{source: S2, locator: "column 1"}], how_known: "(interview) Context only; denomination not named in the text read."}
  self_described_science_religion_relation: {value: "Religion is 'like electricity': he does not understand it but sees its results", certainty: 0.5, cites: [{source: S2, locator: "'Reaction electric'"}], how_known: "(interview) Stidger, 1923; OCR web copy."}
  primary_system:
    value: BELOW_THRESHOLD
    basis: recorded_interview
    cites: [{source: S2, locator: "column 1; closing paragraph"}, {source: S3, locator: "quoted interview"}]
    how_known: "(interview) Two interviews point different ways: 'I believe in God and in Jesus Christ' (1923) against 'I adopted the theory of Reincarnation when I was twenty six. Religion offered nothing to the point' (1928; The Henry Ford says he took it from Orlando J. Smith's 'Eternalism'). Candidates CHRIST and THEOS; no system file fits a Christian with a reincarnation belief, and neither interview is checked against a facsimile (P19)."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "'I believe in God and in Jesus Christ' (1923); the Sermon on the Mount."}
    - {code: THEOS, reason: "Reincarnation as 'a universal plan' (1928); coder's nearest neighbour, not named by him."}
  lio_axes:
    A_locus:
      value: 1
      basis: recorded_interview
      certainty: 0.5
      cites: [{source: S2, locator: "column 1; closing paragraph"}]
      rationale: "A maker distinct from his work: 'I believe in God and in Jesus Christ', and, of John Muir, 'There must be a Gardener, you know, for all this beauty' (a design inference to a Gardener distinct from the garden). Features of the transcendent pole present but limited: nothing on God's acting in events. Named alternative 0 (a personal God, from 'I believe in God and in Jesus Christ')."
      how_known: "(interview) Stidger's 1923 interview, quoted in the first person by a Methodist pastor, read as OCR text of the newspaper page (secondary quotation); 0.5."
      alternatives:
        - {value: 0, note: "Personal Christian God.", cites: [{source: S2, locator: "column 1"}]}
    B_cause: {value: UNKNOWN, how_known: "(interview) Inventor, not a scientist (P33: a device is not a theory or result); no statement of his about nature's order or exceptions in the sources read (P16). The Gardener remark concerns nature's origin and beauty, not law or exception (off-point, P19)."}
    C_ledger: {value: UNKNOWN, how_known: "(interview) Reincarnation ('the experience we collect in one life in the next') bears on C; not scored at this reading (coder's call)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN (§6, P19)."}
  statements:
    - text: "I believe in God and in Jesus Christ. I was brought up in the church."
      cites: [{source: S2, locator: "column 1"}]
      date: "1923-02-04"
      context: "William L. Stidger (pastor, St. Mark's Methodist Church, Detroit), 'Ford affirms faith in God', written for Universal Service, datelined Detroit 3 February 1923; page dated 4 February 1923 (historyworm labels it the Washington Post; the OCR running head on the same page reads 'WASHINGTON TIMES-HERALD … SUNDAY, FEBRUARY 4, 1928'). The '1928' is a slip: 4 February 1923 was a Sunday and 4 February 1928 a Saturday. The masthead is most likely Hearst's Washington Herald: the Times-Herald did not exist until the 1939 merger, the page carries 'Washington Radio Herald' items, and Universal Service was Hearst's wire service. Facsimile check open."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "OCR text of a newspaper page image; the newspaper title and the OCR year in the running head are uncertain; facsimile check pending."
    - text: "No, Mr. Muir didn’t seem to find the Gardener. It’s too bad. There must be a Gardener, you know, for all this beauty."
      cites: [{source: S2, locator: "closing paragraph"}]
      date: "1923-02-04"
      context: "Same interview, replying to Bishop Quayle's remark that John Muir 'knew the garden, but he never found the Gardener'."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "OCR reads “‘No, Mr. Muir didn’t seem to find’ the Gardener”; stray marks normalised; facsimile check pending."
    - text: "I adopted the theory of Reincarnation when I was twenty six. Religion offered nothing to the point. Even work could not give me complete satisfaction. Work is futile if we cannot utilise [sic] the experience we collect in one life in the next."
      cites: [{source: S3, locator: "quoted interview"}]
      date: "1928-08-26"
      context: "San Francisco Examiner interview, 26 August 1928, as quoted by The Henry Ford (Patrice Fisher, 2015)."
      axes: [C_ledger]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "Museum blog quotation; the '[sic]' is the blog's; primary check pending."
  changes_over_life:
    - {value: "Adopted reincarnation at about 26 (c. 1889), by his own 1928 account", certainty: 0.5, cites: [{source: S3, locator: "quoted interview"}], how_known: "(interview) Before the span; does not split it (P31)."}
  coder_notes: "Coder's call. A rests on one 1923 interview by a sympathetic pastor, read as newspaper OCR; the 1928 reincarnation interview does not place God. Ford's antisemitic Dearborn Independent campaign is not in the part of Britannica read and is not coded. Britannica's question boxes not cited (P26)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "American, Michigan farm family", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1908–1914", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Model T (1908) to the assembly line and five-dollar day (1913–14) (P30)."}
  age_at_first_lasting_contribution: {value: 45, certainty: 0.7, cites: [{source: S1, locator: "header dates; 'Early life'"}], how_known: "1908 − 1863 = 45 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No axis scored at 3 or 4 (P27 anchor)."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "A 1; nothing else scored.", certainty: 0.5, cites: [{source: S2, locator: "column 1"}], how_known: "Coder's reading."}
  worldview_during_major_work: {value: BELOW_THRESHOLD, how_known: "As primary_system."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not read.", certainty: 0.5, cites: [{source: S1, locator: "'Early life'"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Early life'"}], how_known: "Not read."}
  circle_present: {value: "unclear", rationale: "Reincarnation as a 'universal plan'.", certainty: 0.5, cites: [{source: S3, locator: "quoted interview"}], how_known: "Coder's reading."}
  reading: "A designer God and a reincarnation 'plan', both from interviews."
  notes: ""

institutions:
  - {value: "Detroit Edison Company", role: "chief engineer", years: "1893–", kind: commercial, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  - {value: "Ford Motor Company", role: founder, years: "1903–", kind: commercial, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 100"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "The 1923 interview is read only as OCR text; the newspaper is most likely Hearst's Washington Herald (not the Post, as historyworm labels it), and the running head's '1928' is a slip for 1923; facsimile check open."
    - "The 1928 interview is quoted by a museum blog, not read in facsimile."
    - "Only the first part of Britannica's article (through 1914) was returned."
  open_questions:
    - "Check both interviews in facsimile (Chronicling America; SF Examiner archive); read the rest of Britannica and the Benson Ford Research Center files on his religion."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Carol W. Gelderman"
    citation: "Gelderman, Carol W. \"Henry Ford.\" Encyclopaedia Britannica (updated 29 September 2026). https://www.britannica.com/biography/Henry-Ford. Read live 2026-10-18 (the Wayback Machine was rate-limiting); the fetch returned the introduction and 'Early life'."
    url: "https://www.britannica.com/biography/Henry-Ford"
    accessed: 2026-10-18
    reliability_note: "Signed article. Body only; question boxes not cited."
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions]
  - id: S2
    type: secondary
    kind: other
    author: "William L. Stidger (Universal Service), via historyworm.com"
    citation: "Stidger, William L. \"Ford Affirms Faith in God.\" Universal Service, Detroit, 3 February 1923; newspaper page of 4 February 1923, p. 10, OCR text at https://www.historyworm.com/gazete/washington_post/1923-02-04/10"
    url: "https://www.historyworm.com/gazete/washington_post/1923-02-04/10"
    accessed: 2026-10-18
    reliability_note: "OCR of a newspaper page; first-person quotations reported by the interviewer; secondary quotation, interview (P8)."
    used_for: [worldview, timing]
  - id: S3
    type: secondary
    kind: "institutional page"
    author: "Patrice Fisher (The Henry Ford)"
    citation: "Fisher, Patrice. \"Henry Ford and Reincarnation.\" The Henry Ford, 13 August 2015. https://www.thehenryford.org/collections/explore/articles/henry-ford-and-reincarnation"
    url: "https://www.thehenryford.org/collections/explore/articles/henry-ford-and-reincarnation"
    accessed: 2026-10-18
    reliability_note: "Museum blog quoting the 1928 interview; secondary quotation."
    used_for: [worldview, lane_b]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-18
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Henry Ford

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Henry Ford (1863–1947), American industrialist [S1]. Draft: primary_system BELOW_THRESHOLD; A 1 at 0.5 (alt 0); B UNKNOWN; mid_basin UNKNOWN. Not plotted.

## Life and work

Dearborn farm, Detroit machine shops, Edison Company, Ford Motor Company (1903) [S1].

## Contribution and impact

Model T (1908); moving assembly line (1913–14); five-dollar day (1914) [S1].

## Childhood and education

One-room school; machine shops at 16 [S1].

## Adult working worldview

'I believe in God and in Jesus Christ' (1923) [S2]; reincarnation (1928) [S3].

## Heritage (context only)

Michigan farm family [S1].

## Timing

1908–1914 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Designer and 'universal plan' [S2; S3].

## Open questions

- Facsimile checks of both interviews.

## Research log

- 2026-10-18: Read Britannica (live), the 1923 interview OCR page and The Henry Ford's blog.
