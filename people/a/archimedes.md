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
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch D, order P32: F 5, rank 8). Basics and works from MacTutor (O'Connor and Robertson). No statement by Archimedes on gods, religion or the order of nature was found; the surviving works are mathematical and mechanical treatises. primary_system UNKNOWN; B_cause 3 at 0.5 from working science (P24, P35; alternative 4); A, C, D UNKNOWN; E BELOW_THRESHOLD (P19); mid_basin UNKNOWN. Draft, not reviewed."}

identity:
  id: archimedes
  display_name: "Archimedes"
  roster:
    canonical_name: "Archimedes"
    rank: 8
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Archimedes of Syracuse", certainty: 0.7, cites: [{source: S1, locator: "Biography, paragraph 1 ('a native of Syracuse')"}], how_known: "MacTutor alone (P15)."}
  native_name: {value: TODO}
  aliases: []

basics:
  birth:
    date: {value: "-287", approx: true, certainty: 0.7, cites: [{source: S1, locator: "Quick Info ('Born 287 BC')"}], how_known: "MacTutor alone; the year is a traditional estimate (ancient report that he was 75 at death), so approx."}
    place: {value: "Syracuse, Sicily", modern_name: "Syracuse, Italy", polity_then: "Syracuse (Greek city-state)", certainty: 0.7, cites: [{source: S1, locator: "Quick Info; Biography paragraph 1"}], how_known: "MacTutor alone (P15)."}
  death:
    date: {value: "-212", certainty: 0.7, cites: [{source: S1, locator: "Quick Info; final paragraphs (killed in 212 BC during the capture of Syracuse)"}], how_known: "MacTutor alone (P15). Plutarch's three versions of the killing differ on how, not when."}
    place: {value: "Syracuse, Sicily", modern_name: "Syracuse, Italy", polity_then: "Syracuse (under Roman siege)", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}], how_known: "MacTutor alone."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "No work of his is dated in the sources read; MacTutor says 'The order in which Archimedes wrote his works is not known for certain' (S1). Every candidate year lies between his adulthood and his death in 212 BC (P30 death cap)."}
  era_bucket: {value: "-500 to 499", certainty: 0.7, cites: [{source: S1, locator: "Quick Info (287–212 BC)"}], how_known: "Every candidate year (his adult life, c. 270–212 BC) falls in '-500 to 499', so the bucket holds although the year is unknown (P2, §3 derived-field rule); MacTutor alone, so 0.7."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}], how_known: "Italy is Southern Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.5, cites: [{source: S1, locator: "Biography, paragraphs 1–2"}], how_known: "He worked in Syracuse; a stay in Alexandria is 'highly likely' but conjecture (S1), so 0.5."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "Biography ('his father')"}], how_known: "As the source records it."}
  languages_of_work: {value: [Greek], certainty: 0.7, cites: [{source: S1, locator: "last paragraph (Dorian dialect)"}], how_known: "MacTutor: the test of a text's closeness to the original is whether it keeps 'Archimedes' Dorian dialect'."}
  occupations: {value: ["mathematician", "engineer"], certainty: 0.7, cites: [{source: S1, locator: "Summary"}], how_known: "MacTutor alone."}

contribution:
  fields: {value: ["geometry", "mechanics", "hydrostatics"], certainty: 0.7, cites: [{source: S1, locator: "Biography (works)"}], how_known: "MacTutor alone."}
  lasting_original_contributions:
    - {value: "Method of exhaustion applied to areas, volumes and surfaces (sphere and cylinder: volume and surface two-thirds of the circumscribed cylinder; quadrature of the parabola)", year: "undated (before 212 BC)", kind: "law or principle", lasting: "Chasles: it 'gave birth to the calculus of the infinite'", certainty: 0.7, cites: [{source: S1, locator: "Biography (On the sphere and cylinder; Quadrature of the parabola; Chasles quotation)"}], how_known: "MacTutor; works undated."}
    - {value: "Archimedes' principle and the basic principles of hydrostatics (On floating bodies)", year: "undated (before 212 BC)", kind: "law or principle", lasting: "standard law of hydrostatics", certainty: 0.7, cites: [{source: S1, locator: "Biography (On floating bodies)"}], how_known: "MacTutor."}
    - {value: "Fundamental theorems on centres of gravity and the principles of mechanics (On plane equilibriums)", year: "undated (before 212 BC)", kind: "law or principle", lasting: "basis of statics", certainty: 0.7, cites: [{source: S1, locator: "Biography (On plane equilibriums)"}], how_known: "MacTutor."}
  evidence_of_impact:
    - {value: "Archimedes' principle", kind: "named after them", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  major_works:
    - {value: "On the sphere and cylinder", year: "undated", kind: book, certainty: 0.7, cites: [{source: S1, locator: "list of surviving works"}], how_known: "MacTutor."}
    - {value: "The Sandreckoner", year: "undated", kind: book, certainty: 0.7, cites: [{source: S1, locator: "list of surviving works"}], how_known: "MacTutor; dedicated to Gelon, son of Hieron II."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Exhaustion-method results and hydrostatics still taught and built on.", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "MacTutor says nothing on it."}
  family_religious_practice: {value: UNKNOWN, how_known: "Same."}
  parents_and_household:
    - {value: "Father Phidias, an astronomer", name: "Phidias", role: father, certainty: 1.0, cites: [{source: S1, locator: "Biography paragraph 1 (known only from The Sandreckoner)"}], how_known: "His own statement in The Sandreckoner, as reported by MacTutor (primary document printed in S1, read only through S1)."}
  household_circumstances: {value: TODO}
  schooling: []
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: UNKNOWN, how_known: "No work is dated (S1); equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing of his on religion in MacTutor's account of his works and prefaces."}
  primary_system:
    value: UNKNOWN
    cites: [{source: S1, locator: "whole article"}]
    how_known: "No statement of his on gods, religion or the order of nature was found in MacTutor or in a web search (2026-10-15). Plutarch's portrait of him (pure mathematics as the only worthy pursuit) is reported character, not a worldview (P19)."
    note: "Lead: Dijksterhuis, Archimedes (1956/1987); the Heath translation of the works."
  secondary_system: {value: UNKNOWN, how_known: "No system evidence."}
  candidate_codes_considered: []
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing of his on gods or the divine in the sources read (P19)."}
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      cites: [{source: S1, locator: "Biography (On plane equilibriums; On floating bodies)"}]
      how_known: "Coder's reading of his working science (P24, P30): the law of the lever, centres of gravity and the hydrostatic principle are results about physical systems, so he is a scientist under P30. No statement of his own on law and exception."
      rationale: "Scored on his account of nature (P6), which for a scientist is the working science. His mechanics and hydrostatics state general results about bodies and fluids with no exception, miracle or petition. P35: B inferred only from working science is B 3 at 0.5 with 4 as the named alternative, never 4. Named alternative: 4."
    C_ledger: {value: UNKNOWN, how_known: "Nothing in the sources read (P19)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing on revelation; working science does not bear on D (P19)."}
    E_scope: {value: BELOW_THRESHOLD, note: "Scored on the world's order (P7). Working science bears on E's first question but E is not scored from it alone (P19).", how_known: "BELOW_THRESHOLD under P19: not scored from working science alone."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, which takes precedence (§6, P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "statements is empty: no religious or metaphysical statement of his was found. The Plutarch passages in MacTutor (contempt for practical engineering, absorption in geometry) are reported speech and character, used for nothing. Ancient-source caution: everything biographical outside his prefaces comes from Plutarch, Livy and Cicero, writing a century or more later."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Greek of Syracuse", certainty: 0.5, cites: [{source: S1, locator: "Biography"}], how_known: "Coder's inference from his city and dialect (P24)."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not in the source read."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not in the source read."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not in the source read."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "No work is dated in the sources read (S1: order of works 'not known for certain'); the period ends by 212 BC at the latest (P30)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "First-lasting year unknown."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement scored at 3 or 4; B rests on working science (P27)."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "Nothing of his on gods or nature was read.", certainty: 0.5, cites: [{source: S1, locator: "whole article"}], how_known: "Absence in the source read."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "His treatises proceed by definition, postulate and proof; even results found mechanically 'had to be proved by geometry afterwards' (The Method, quoted in S1).", certainty: 0.7, cites: [{source: S1, locator: "Biography (The Method; Heath on the treatises)"}], how_known: "MacTutor."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "Biography paragraph 2 (likely study with Euclid's successors)"}], how_known: "Training is conjecture."}
  circle_present: {value: "unclear", rationale: "No God–Nature statement read.", certainty: 0.5, cites: [{source: S1, locator: "whole article"}], how_known: "No evidence either way."}
  reading: "As belief, not finding: form present, circle unclear. The record does not test H1."
  notes: ""

institutions: []
collaborators:
  - {value: "Conon of Samos", relation: correspondent, note: "mathematician at Alexandria and close friend", certainty: 0.7, cites: [{source: S1, locator: "Biography paragraph 2"}], how_known: "MacTutor."}

review:
  roster_status_reason: {value: "Core in v8 (F 5: Claude, DeepSeek, Gemini, GPT, Grok).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 8"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Britannica could not be read (Cloudflare check, 2026-10-15); basics rest on MacTutor alone, so 0.7."
    - "No work of his is dated; first-lasting year, period and age are UNKNOWN."
  open_questions:
    - "Read Dijksterhuis (1987) and Netz's editions for any religious remark in the prefaces and for a dated chronology of the works."

sources:
  - id: S1
    type: secondary
    kind: "institutional page"
    author: "J. J. O'Connor and E. F. Robertson"
    year: 1999
    citation: "O'Connor, J. J., and E. F. Robertson. \"Archimedes.\" MacTutor History of Mathematics Archive, University of St Andrews, last update January 1999. https://mathshistory.st-andrews.ac.uk/Biographies/Archimedes/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Archimedes/"
    accessed: 2026-10-15
    reliability_note: "Standard reference biography; draws on Heath, Clagett and Dijksterhuis."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, collaborators]
  - id: S2
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# Archimedes

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Archimedes of Syracuse (c. 287–212 BC), mathematician and engineer, found areas, volumes and surfaces by the method of exhaustion, set out the principles of statics and hydrostatics, and stated Archimedes' principle [S1]. No statement of his on gods, religion or the order of nature was found. Draft: primary_system UNKNOWN; B_cause 3 at 0.5 from working science (alternative 4, P35); A UNKNOWN; mid_basin UNKNOWN.

## Life and work

Son of the astronomer Phidias, native of Syracuse, probably in touch with Euclid's successors in Alexandria; killed in 212 BC when the Romans took Syracuse [S1].

## Contribution and impact

On the sphere and cylinder, Quadrature of the parabola, On plane equilibriums, On floating bodies, The Method [S1].

## Childhood and education

Nothing beyond his father's name and profession [S1].

## Adult working worldview

Not established. B is scored 3 at 0.5 from his working science, as P24 and P35 direct [S1].

## Heritage (context only)

Greek of Syracuse [S1].

## Timing

No work is dated; first-lasting year unknown.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form present; circle unclear [S1].

## Open questions

- Dated chronology of the works; any religious remark in the prefaces.

## Research log

- 2026-10-15: Read MacTutor. Britannica blocked (Cloudflare). Web search for his religious views found nothing citable.
