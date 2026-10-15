---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch E)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-15
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch E, order P32: F 5, rank 25). Britannica (van der Waerden): 'Of Euclid's life nothing is known' beyond Proclus. Undated works (P39). Mathematician with no listed contribution about natural systems; no worldview statement survives in the source read. All worldview fields UNKNOWN. Draft, not reviewed."}

identity:
  id: euclid
  display_name: "Euclid"
  roster:
    canonical_name: "Euclid"
    rank: 25
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Euclid", certainty: 0.7, cites: [{source: S1, locator: "header"}], how_known: "Britannica."}
  native_name: {value: "Eukleides", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts ('Greek: Eukleides')"}], how_known: "Britannica's transliteration."}
  aliases: []

basics:
  birth:
    date: {value: UNKNOWN, how_known: "Britannica gives only 'flourished c. 300 bce'."}
    place: {value: UNKNOWN, how_known: "Britannica gives no birthplace; 'from Alexandria' refers to where he taught."}
  death:
    date: {value: UNKNOWN, how_known: "Not given."}
    place: {value: UNKNOWN, how_known: "Not given."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "The Elements is undated; Britannica places him only in the reign of Ptolemy I Soter (323–285 BC) (P39)."}
  era_bucket: {value: "-500 to 499", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts; 'Life'"}], how_known: "Every possible working year (reign of Ptolemy I, 323–285 BC; flourished c. 300 BC) is in '-500 to 499' (P39); Britannica alone, 0.7."}
  region_of_birth: {value: UNKNOWN, how_known: "Birthplace unknown."}
  region_of_work: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "'Life' (taught at Alexandria)"}], how_known: "Egypt (Northern Africa) (P3)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [Greek], certainty: 0.7, cites: [{source: S1, locator: "text (Greek terms)"}], how_known: "Britannica."}
  occupations: {value: ["mathematician", "teacher"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Life'"}], how_known: "Britannica."}

contribution:
  fields: {value: ["geometry", "number theory"], certainty: 0.7, cites: [{source: S1, locator: "'Sources and contents'"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "The Elements: axiomatic geometry from definitions, postulates and common notions; Euclidean algorithm; infinitude of primes", year: "undated (c. 300 BC)", kind: work, lasting: "'one of the most influential books ever written'; 'the whole design of his work was his own' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening caption; 'Sources and contents'"}], how_known: "Britannica. Pure mathematics, so not a scientist under P30 #11."}
  evidence_of_impact:
    - {value: "Contemporaries 'considered his work final and authoritative'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "'Sources and contents', end"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Axiomatic method; the Elements.", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Nothing known of his life (S1)."}
  family_religious_practice: {value: UNKNOWN, how_known: "Nothing known (S1)."}
  parents_and_household: []
  household_circumstances: {value: UNKNOWN, how_known: "Nothing known (S1)."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "Nothing known (S1)."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Nothing known (S1)."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Nothing known (S1)."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: UNKNOWN, how_known: "Undated works (P39)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Britannica read; no statement survives. The 'no royal road' remark is Proclus's anecdote (reported speech) and is not about religion."}
  primary_system: {value: UNKNOWN, how_known: "Nothing in the source read."}
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered: []
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing read."}
    B_cause: {value: UNKNOWN, how_known: "Pure mathematics gives no B (P16); no statement about nature read."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "A and B are UNKNOWN (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Coder's call: the Optics was not listed or read; if listed as a theory about vision it could make him a scientist (P30 #11) and give B 3 at 0.5 under P35."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Greek", certainty: 0.5, cites: [{source: S1, locator: "opening ('mathematician of Greco-Roman antiquity')"}], how_known: "Inferred from language and setting."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Nothing known."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Nothing known."}
  childhood_catechism: {value: UNKNOWN, how_known: "Nothing known."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "Undated works (P39)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "Birth and work years unknown (P39)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S1, locator: "'Life'"}], how_known: "Nothing survives."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Nothing read."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "He is the source of definition-to-consequence geometry.", certainty: 0.7, cites: [{source: S1, locator: "'Sources and contents'"}], how_known: "Britannica."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Life'"}], how_known: "Nothing known of his training."}
  circle_present: {value: "unclear", rationale: "Nothing known.", certainty: 0.5, cites: [{source: S1, locator: "'Life'"}], how_known: "Coder's reading."}
  reading: "No reading possible beyond form."
  notes: ""

institutions: []
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 25"}], how_known: "Study roster."}
  controversies:
    - {value: "How much of the Elements is his own versus compiled from predecessors", certainty: 0.7, cites: [{source: S1, locator: "'Sources and contents', end"}], how_known: "Britannica."}
  data_quality_flags:
    - "Medieval editors confused him with Eukleides of Megara (S1)."
  open_questions:
    - "Decide whether the Optics belongs on the lasting list (it would change B under P35)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Bartel Leendert van der Waerden"
    citation: "van der Waerden, B. L. \"Euclid.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Euclid-Greek-mathematician."
    url: "https://www.britannica.com/biography/Euclid-Greek-mathematician"
    accessed: 2026-10-15
    reliability_note: "Signed article body; 'Top Questions' not used."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, review]
  - id: S2
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Euclid

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Euclid (flourished c. 300 BC, Alexandria), author of the Elements [S1]. Nothing is known of his life or beliefs [S1]. Draft: all worldview fields UNKNOWN; mid_basin UNKNOWN.

## Life and work

Taught at Alexandria under Ptolemy I [S1].

## Contribution and impact

The Elements [S1].

## Childhood and education

Unknown [S1].

## Adult working worldview

Unknown [S1].

## Heritage (context only)

Greek-speaking [S1].

## Timing

Undated (P39) [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Geometric form yes [S1].

## Open questions

- Optics.

## Research log

- 2026-10-15: Read Britannica.
