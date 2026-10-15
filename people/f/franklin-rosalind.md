---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch K)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-15
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch K, order P32: F 5, rank 70). Basics from Britannica (Britannica Editors, unsigned; Top Questions not cited) and NIH/NLM Profiles in Science. Worldview from her 1940 letter to her father, quoted by NLM and in Brenda Maddox's New Humanist article (2007), both secondary quotations of a private letter. Scientist under P30 (coal micro-structure, DNA, virus structure). primary_system AGNOS (0.5, alt ATHE); A 4 (0.5, alt 3); B 3 (0.5, alt 4) from working science (P35); mid_basin BELOW_THRESHOLD. Plotted (faded). Draft, not reviewed."}

identity:
  id: franklin-rosalind
  display_name: "Rosalind Franklin"
  roster:
    canonical_name: "Rosalind Franklin"
    rank: 70
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: biology
    field_bucket: "biology / life science"
  full_name: {value: "Rosalind Elsie Franklin", certainty: 0.7, cites: [{source: S1, locator: "header ('In full')"}], how_known: "Britannica."}
  native_name: {value: UNKNOWN, how_known: "English."}
  aliases: []

basics:
  birth:
    date: {value: "1920-07-25", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "paragraph 1"}], how_known: "Britannica and NLM agree."}
    place: {value: "London, England", modern_name: "London, United Kingdom", polity_then: "United Kingdom", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources."}
  death:
    date: {value: "1958-04-16", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "cancer paragraph"}], how_known: "Two sources."}
    place: {value: "London, England", modern_name: "London, United Kingdom", polity_then: "United Kingdom", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "cancer paragraph"}], how_known: "Two sources."}
  first_lasting_contribution_year: {value: 1945, certainty: 0.5, cites: [{source: S2, locator: "BCURA paragraph"}, {source: S1, locator: "paragraph 2"}], how_known: "Coal micro-structure ('molecular sieves') work at BCURA, 1942–46, documented in her 1945 Cambridge doctoral thesis; the thesis is the earliest dated public record read (P30); the papers are not individually dated in what was read (0.5)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Birth year bucket (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United Kingdom (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "London and Cambridge; Paris 1947–50."}
  sex_as_recorded: {value: "female", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [English, French], certainty: 0.5, cites: [{source: S2, locator: "paragraph 1; Paris paragraph"}], how_known: "Coder's reading (0.5)."}
  occupations: {value: ["physical chemist", "crystallographer"], certainty: 0.7, cites: [{source: S2, locator: "paragraph 1"}], how_known: "NLM."}
contribution:
  fields: {value: ["physical chemistry", "X-ray crystallography", "structural biology"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "text"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Micro-structure of coals: pores with molecular-level constrictions acting as 'molecular sieves'", year: 1945, kind: discovery, lasting: "'made it possible to classify coals and predict their performance' (S2)", certainty: 0.5, cites: [{source: S2, locator: "BCURA paragraph"}], how_known: "Dated by the 1945 thesis (0.5)."}
    - {value: "X-ray evidence that DNA is helical; both forms with two helices", year: 1953, kind: discovery, lasting: "'laid the foundation' for the Watson–Crick double helix (S1)", certainty: 0.5, cites: [{source: S1, locator: "King's College paragraph"}, {source: S2, locator: "King's paragraph"}], how_known: "Conclusion reached 'by early 1953' (S2); her DNA papers are not individually dated in what was read (0.5)."}
  evidence_of_impact:
    - {value: "Crick 'later admitted that Franklin was two steps away from realizing the correct structure'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S2, locator: "Cavendish paragraph"}], how_known: "NLM."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1, S2).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Anglo-Jewish", certainty: 0.7, cites: [{source: S2, locator: "paragraph 1"}, {source: S3, locator: "family paragraph"}], how_known: "NLM; Maddox: 'not overly religious', father expected the rituals to be followed."}
  family_religious_practice: {value: "Observant of rituals by the father's expectation, 'not overly religious'", certainty: 0.5, cites: [{source: S3, locator: "family paragraph"}], how_known: "Maddox (0.5)."}
  parents_and_household:
    - {value: "Father Ellis Franklin, partner at Keyser's Bank; mother Muriel", role: parents, certainty: 0.7, cites: [{source: S2, locator: "paragraph 1"}], how_known: "NLM."}
  household_circumstances: {value: "Second of five children in a prominent Anglo-Jewish banking and publishing family", certainty: 0.7, cites: [{source: S2, locator: "paragraph 1"}], how_known: "NLM."}
  schooling:
    - {value: "St Paul's Girls' School, London", stage: "grammar or secondary school", run_by: private, certainty: 0.7, cites: [{source: S1, locator: "paragraph 2"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources."}
    - {value: "Newnham College, Cambridge (1938–41), physical chemistry", stage: university, run_by: other, certainty: 0.7, cites: [{source: S1, locator: "paragraph 2"}, {source: S2, locator: "paragraph 2"}], how_known: "Two sources."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Early aptitude for math and science; took science 'at sixteen'", certainty: 0.7, cites: [{source: S2, locator: "paragraphs 1–2"}], how_known: "NLM, quoting her mother."}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [English], certainty: 0.5, cites: [{source: S2, locator: "paragraph 1"}], how_known: "Coder's reading."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1945–1953", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Joined the Jewish Society at Cambridge 'to please her grandfather, but disliked it'", years: "1938", role: "nominal member", certainty: 0.5, cites: [{source: S3, locator: "family paragraph"}], how_known: "Maddox (0.5)."}
  self_described_science_religion_relation: {value: "'Science and everyday life cannot and should not be separated. Science, for me, gives a partial explanation of life' (letter to her father, 1940).", certainty: 0.5, cites: [{source: S2, locator: "epigraph"}, {source: S3, locator: "letter quotation"}], how_known: "Private letter, secondary quotation in two sources; one letter, so 0.5."}
  primary_system:
    value: AGNOS
    basis: consistent_private_letters
    certainty: 0.5
    cites: [{source: S3, locator: "letter quotation ('a creator ..., if such there be')"}]
    rationale: "In the 1940 letter she rejects belief in life after death as the content of faith and leaves a creator open ('if such there be') while denying it would be interested in us. Maddox calls her 'passionately secular'. Named alternative: ATHE (no positive belief stated), or SECHUM ('faith in this world')."
    how_known: "One private letter, secondary quotation (0.5); the letter predates the working years by five years."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "'if such there be' leaves a creator open."}
    - {code: ATHE, reason: "Rejects an afterlife and any interested creator; Maddox: 'passionately secular'."}
    - {code: SECHUM, reason: "'faith in this world is perfectly possible without faith in another world'; improvement of the lot of mankind."}
  lio_axes:
    A_locus:
      value: 4
      basis: consistent_private_letters
      certainty: 0.5
      cites: [{source: S3, locator: "letter quotation"}]
      how_known: "One private letter, secondary quotation; dated 1940, before the working years (P20), so 0.5; alternative named."
      rationale: "An explicit denial of a personal, interested God is scored (§ A_locus, P20): 'I see no reason to believe that a creator of protoplasm or primeval matter, if such there be, has any reason to be interested in our insignificant race'. Named alternative: 3, since a remote creator is left open."
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      cites: [{source: S2, locator: "text"}]
      how_known: "Working science only (P35)."
      rationale: "Physical chemistry and crystallography; 'Science ... is based on fact, experience and experiment' is about method, not about law and exception in nature (P16). B 3 at 0.5, alternative 4 (P35)."
    C_ledger: {value: UNKNOWN, how_known: "She rejects 'belief in life after death' as the definition of faith, but says nothing of moral reckoning; not scored."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "The creator would not be interested 'in our insignificant race'; this concerns A, not group favour (P7); not scored."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 4 is scored only at 0.5, under the 0.7 bar for the A ≥ 3 branch (P10).", note: "If A reached 0.7 the result would be false."}
  statements:
    - text: "I agree that faith is essential to success in life (success of any sort) but I do not accept your definition of faith, i.e. belief in life after death."
      cites: [{source: S2, locator: "epigraph"}, {source: S3, locator: "letter quotation"}]
      date: "1940"
      context: "Letter to her father Ellis Franklin, summer 1940, at Cambridge (S3)."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
    - text: "I see no reason to believe that a creator of protoplasm or primeval matter, if such there be, has any reason to be interested in our insignificant race in a tiny corner of the universe, and still less in us, as still more insignificant individuals."
      cites: [{source: S3, locator: "letter quotation"}]
      date: "1940"
      context: "Same letter; Maddox prints an ellipsis '[ ]' before it."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "Only S3 prints this passage; Maddox's biography (2002), ch. 4, is the printed source (per Quote Investigator, not read)."
  changes_over_life: []
  coder_notes: "Coder's call; one 1940 letter in two secondary quotations. Maddox's 'deathbed test' remark (S3) is the author's, not hers. Maddox, The Dark Lady of DNA (2002), ch. 4 is the lead for the full letter."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Anglo-Jewish", certainty: 0.7, cites: [{source: S2, locator: "paragraph 1"}], how_known: "NLM."}
  religious_heritage_by_birth: {value: "Jewish", certainty: 0.7, cites: [{source: S2, locator: "paragraph 1"}, {source: S3, locator: "family paragraph"}], how_known: "Two sources."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1945–1953", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "First to last dated listed contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 25, certainty: 0.5, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "BCURA paragraph"}], how_known: "1945 − 1920 = 25 (P30)."}
  first_evidence_of_lio_type_views: {value: "1940, age 20: a creator, 'if such there be', has no reason 'to be interested in our insignificant race'", year: 1940, age: 20, certainty: 0.5, cites: [{source: S3, locator: "letter quotation"}], how_known: "Earliest document read; nothing earlier known."}
  lio_views_relative_to_major_work: {value: "before major work", certainty: 0.5, cites: [{source: S3, locator: "letter quotation"}], how_known: "1940 letter; work dated from 1945."}
  worldview_during_major_work: {value: AGNOS, certainty: 0.5, cites: [{source: S3, locator: "letter quotation"}], how_known: "As primary_system; no later statement read."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not read.", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Not read."}
  circle_present: {value: "no", rationale: "No God placed as source or end in what was read.", certainty: 0.5, cites: [{source: S3, locator: "letter quotation"}], how_known: "Coder's reading."}
  reading: "Secular; one letter."
  notes: ""

institutions:
  - {value: "British Coal Utilisation Research Association", role: researcher, kind: "research institute", certainty: 0.7, cites: [{source: S1, locator: "paragraph 2"}], how_known: "Britannica."}
  - {value: "King's College London (Biophysics Unit)", role: "research fellow", kind: university, certainty: 0.7, cites: [{source: S1, locator: "King's College paragraph"}], how_known: "Britannica."}
  - {value: "Birkbeck College, London", role: researcher, kind: university, certainty: 0.7, cites: [{source: S1, locator: "Birkbeck paragraph"}], how_known: "Britannica."}
collaborators:
  - {value: "Raymond Gosling", relation: "student or assistant", certainty: 0.7, cites: [{source: S2, locator: "King's paragraph"}], how_known: "NLM."}
  - {value: "Aaron Klug", relation: collaborator, certainty: 0.7, cites: [{source: S2, locator: "Birkbeck paragraph"}], how_known: "NLM."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 70"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags: []
  open_questions:
    - "Read the full 1940 letter in Maddox (2002), ch. 4, and date her first coal paper."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Rosalind Franklin.\" Encyclopaedia Britannica, updated 14 October 2026. https://www.britannica.com/biography/Rosalind-Franklin."
    url: "https://www.britannica.com/biography/Rosalind-Franklin"
    accessed: 2026-10-15
    reliability_note: "Unsigned editors' body; Top Questions not cited."
    used_for: [identity, basics, contribution, childhood, timing, institutions]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "U.S. National Library of Medicine"
    citation: "U.S. National Library of Medicine. \"Biographical Overview.\" Rosalind Franklin Papers, Profiles in Science. https://profiles.nlm.nih.gov/spotlight/kr/feature/biographical."
    url: "https://profiles.nlm.nih.gov/spotlight/kr/feature/biographical"
    accessed: 2026-10-15
    reliability_note: "Unsigned institutional overview; quotes the 1940 letter with an ellipsis."
    used_for: [basics, contribution, childhood, worldview, heritage, timing, collaborators]
  - id: S3
    type: secondary
    kind: other
    author: "Brenda Maddox"
    citation: "Maddox, Brenda. \"Mother of DNA.\" New Humanist, 31 May 2007. https://newhumanist.org.uk/articles/mother-of-dna/."
    url: "https://newhumanist.org.uk/articles/mother-of-dna/"
    accessed: 2026-10-15
    reliability_note: "By her biographer, in a humanist magazine; quotes the 1940 letter at length."
    used_for: [childhood, worldview, heritage, timing, lane_b]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Rosalind Franklin

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Rosalind Franklin (1920–1958), British physical chemist and crystallographer [S1, S2]. Draft: primary_system AGNOS (0.5, alt ATHE); A 4 at 0.5 (alt 3); B 3 at 0.5 (P35); mid_basin BELOW_THRESHOLD. Plotted (faded).

## Life and work

Cambridge; BCURA; Paris; King's College; Birkbeck [S1, S2].

## Contribution and impact

Coal micro-structure; DNA helical structure; virus structure [S1, S2].

## Childhood and education

St Paul's Girls' School; Newnham College [S2].

## Adult working worldview

1940 letter: faith 'in this world is perfectly possible without faith in another world' [S3].

## Heritage (context only)

Anglo-Jewish [S2].

## Timing

First lasting contribution dated 1945, at 25 [S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle [S3].

## Open questions

- Full 1940 letter (Maddox 2002).

## Research log

- 2026-10-15: Read Britannica (Editors), NLM Profiles in Science overview and Maddox in New Humanist (2007).
