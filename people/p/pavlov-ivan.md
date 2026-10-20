---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA2)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA2, order P32: F 3, rank 184). Source: Britannica, signed by W. Horsley Gantt (his former collaborator; scholars edition, read in full). Lasting work: the conditioned reflex ('known chiefly for his development of the concept'); dated by its first public exposition at the XIV International Medical Congress, Madrid, 1903 (Campos-Bueno, journal article), the public reading as dating event (P30 #1). Worldview from Gantt's account: 'Although Pavlov held to scientific agnosticism, he considered true religion beneficial; he said that he envied no one anything except his wife her devout religious faith' (undated; a scholar's account, so scholarly_reconstruction, 0.5). primary_system AGNOS 0.5, alt BELOW_THRESHOLD; A BELOW_THRESHOLD (agnosticism states no locus); scientist (laws of the conditioned reflex: testable claims about organisms), so B 3 at 0.5 from working science, alt 4 (P24, P35); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Span 1903, age 54. Not plotted. Draft, not reviewed."}

identity:
  id: pavlov-ivan
  display_name: "Ivan Pavlov"
  roster:
    canonical_name: "Ivan Pavlov"
    rank: 184
    F: 3
    models: [Claude, DeepSeek, Gemini]
    band: "core (3–4)"
    status: "core"
    field: "psychology"
    field_bucket: "psychology / neuroscience"
  full_name: {value: "Ivan Petrovich Pavlov", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  native_name: {value: "Иван Петрович Павлов", certainty: 0.5, cites: [{source: S1, locator: "Introduction"}], how_known: "Cyrillic spelling the coder's."}
  aliases:
    - {name: "Pavlov-Ivan", kind: "roster alias"}

basics:
  birth:
    date: {value: "1849-09-26", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica: September 14 Old Style, September 26 New Style."}
    place: {value: "Ryazan", modern_name: "Ryazan, Russia", polity_then: "Russian Empire", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  death:
    date: {value: "1936-02-27", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "Leningrad", modern_name: "Saint Petersburg, Russia", polity_then: "Soviet Union", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1903, certainty: 0.7, cites: [{source: S2, locator: "text"}], how_known: "First public exposition of his theory of conditional reflexes at the XIV International Medical Congress, Madrid, 1903 (S2); public reading of a paper is the P30 #1 dating event (Z10 ruling)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S2, locator: "text"}], how_known: "1903 (P2)."}
  region_of_birth: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Russia (P3)."}
  region_of_work: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "Life"}], how_known: "St Petersburg."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Russian", "French"], certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Madrid lecture in French (S2)."}
  occupations: {value: ["physiologist"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

contribution:
  fields: {value: ["physiology", "psychology"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "The conditioned (conditional) reflex and its laws", year: 1903, kind: "theory", lasting: "'known chiefly for his development of the concept of the conditioned reflex'; 'Pavlov's work laid the basis for the scientific analysis of behaviour' (S1, body)", certainty: 0.7, cites: [{source: S1, locator: "Introduction; Legacy"}, {source: S2, locator: "text"}], how_known: "Britannica (Gantt); dated by the Madrid lecture, 1903 (S2)."}
  evidence_of_impact:
    - {value: "Nobel Prize for Physiology or Medicine, 1904 (digestive secretions)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  major_works:
    - {value: "Lectures on the Work of the Digestive Glands", year: 1897, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "Life"}], how_known: "Britannica: the digestion work 'culminated in his book ... in 1897'; not called lasting in the body."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Laid the basis for the scientific analysis of behaviour (S1).", certainty: 0.7, cites: [{source: S1, locator: "Legacy"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "First son of a priest, grandson of a sexton; church school and theological seminary in Ryazan", role: "family", certainty: 0.7, cites: [{source: S1, locator: "Life"}], how_known: "Britannica."}
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
  working_years: {value: "1903", certainty: 0.7, cites: [{source: S2, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: 
    value: AGNOS
    basis: scholarly_reconstruction
    certainty: 0.5
    cites: [{source: S1, locator: "Opposition to communism, last para."}]
    how_known: "Gantt (Britannica, signed), his former collaborator: 'Pavlov held to scientific agnosticism'. A scholar's account, undated, so 0.5 (no own words read)."
    rationale: "'Scientific agnosticism' while he 'considered true religion beneficial' (S1). Alternative BELOW_THRESHOLD: the account is undated and gives no statement of his own; 'considered true religion beneficial' is about religion's use, not its truth."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Coded at 0.5 on Gantt's account."}
    - {code: CHRIST, reason: "Not used: priest's son left the seminary in 1870 (S1); 1924 'I also am the son of a priest' is solidarity, not profession."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Agnosticism states no locus; nothing first-hand read."}
    B_cause: 
      value: 3
      basis: inference_from_work
      certainty: 0.5
      cites: [{source: S1, locator: "Laws of conditioned reflex"}]
      how_known: "Scientist (P30, P35 addendum): the laws of the conditioned reflex are testable claims about organisms. B from working science with no statement of his own on law and exception, so 3 at 0.5, alternative 4, never 4 (P24, P35)."
      rationale: "He 'was led to formulate the laws of the conditioned reflex' and insisted mental phenomena be reduced 'to measurable physiological quantities' (S1): lawful nature in his science. Alternative 4."
      alternatives:
        - {value: 4, note: "Working science cannot tell lawful-with-exceptions from exceptionless (P35).", cites: [{source: S1, locator: "Legacy"}]}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Lead: insisted that mental phenomena could be dealt with scientifically only by measurable quantities (S1); not scored."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied."}
  statements:
    - text: "Although Pavlov held to scientific agnosticism, he considered true religion beneficial; he said that he envied no one anything except his wife her devout religious faith."
      cites: [{source: S1, locator: "Opposition to communism, last para."}]
      date: "1936"
      context: "Gantt's summary of his views in the Britannica article; undated; date is his death year (latest possible)."
      axes: [A_locus]
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-19
      note: "Gantt's paraphrase, not Pavlov's words; not a written profession (§7). Backs the 0.5 scholarly reading only."
  changes_over_life: []
  coder_notes: "Read Todes, Ivan Pavlov: A Russian Life in Science (2015), and Babkin (1949) on his religious views; the 'letter to the students' and alleged statements of belief circulating online are leads of doubtful provenance."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: "Russian Orthodox (priest's son)", certainty: 0.7, cites: [{source: S1, locator: "Life"}], how_known: "Britannica."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1903", certainty: 0.7, cites: [{source: S2, locator: "text"}], how_known: "The Madrid lecture, the dating event for the one listed lasting work (P29, P30 #1)."}
  age_at_first_lasting_contribution: {value: 54, certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S2, locator: "text"}], how_known: "1903 − 1849 = 54 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Experimental physiology, not geometric argument (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Imperial Medical Academy, St Petersburg", role: "professor of physiology", years: "1890–1924", kind: "university", certainty: 0.7, cites: [{source: S1, locator: "Life"}], how_known: "Britannica."}
  - {value: "Institute of Experimental Medicine", role: "head of physiology", years: UNKNOWN, kind: "research institute", certainty: 0.5, cites: [{source: S1, locator: "Life"}], how_known: "Britannica."}
collaborators:
  - {value: "Carl Ludwig", relation: "teacher", note: "Leipzig, 1884–86", certainty: 0.7, cites: [{source: S1, locator: "Life"}], how_known: "Britannica."}
  - {value: "Rudolf Heidenhain", relation: "teacher", note: "Breslau", certainty: 0.7, cites: [{source: S1, locator: "Life"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 184"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Worldview rests on one scholar's undated account."
  open_questions:
    - "Todes 2015 on religion."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "W. Horsley Gantt"
    citation: "Gantt, W. Horsley. 'Ivan Pavlov.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/Ivan-Pavlov/58811"
    url: "https://kids.britannica.com/scholars/article/Ivan-Pavlov/58811"
    accessed: 2026-10-19
    reliability_note: "Signed article by his former collaborator; read in full."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "journal article"
    author: "J. J. Campos-Bueno"
    citation: "Campos-Bueno, J. J. 'Neuron Doctrine and Conditional Reflexes at the XIV International Medical Congress of Madrid of 1903.' Universidad Complutense eprint 15010. https://eprints.ucm.es/id/eprint/15010/1/jjcamposbueno_pavlov-cajal_art24.pdf"
    url: "https://eprints.ucm.es/id/eprint/15010/1/jjcamposbueno_pavlov-cajal_art24.pdf"
    accessed: 2026-10-19
    reliability_note: "Scholarly article, seen as a search excerpt: 'the first public exposition in French of his theory on conditional and unconditional reflexes'."
    used_for: [basics, timing]
  - id: S3
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

Ivan Pavlov (1849–1936), physiologist [S1]. Draft: AGNOS (0.5); B 3 (0.5). Not plotted.

## Life and work

Ryazan; St Petersburg [S1].

## Contribution and impact

Conditioned reflex [S1]; Madrid 1903 [S2].

## Childhood and education

Church school and seminary [S1].

## Adult working worldview

'Scientific agnosticism' (Gantt) [S1].

## Heritage (context only)

Priest's son [S1].

## Timing

1903, age 54 [S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Todes 2015.

## Research log

- 2026-10-19: Read Britannica (Gantt); Campos-Bueno excerpt.
