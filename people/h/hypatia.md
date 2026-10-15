---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch G)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-15
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch G, order P32: F 5, rank 38). Basics from Britannica (Deakin) and MacTutor (O'Connor and Robertson). All her works are lost (S1, S2); her Neoplatonism is known only from later reports, which are reported speech (§7, P42). Not a scientist under P30: no original result is known (S2). Birth year disputed (c. 355 vs c. 370). Undated works (P39). primary_system BELOW_THRESHOLD (candidate PLATO, as Neoplatonism); A BELOW_THRESHOLD; B, C, D, E UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: hypatia
  display_name: "Hypatia"
  roster:
    canonical_name: "Hypatia"
    rank: 38
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Hypatia of Alexandria", certainty: 0.7, cites: [{source: S2, locator: "Biography, first sentence"}], how_known: "MacTutor."}
  native_name: {value: UNKNOWN, how_known: "Greek form not recorded in the sources read."}
  aliases: []

basics:
  birth:
    date:
      value: "355"
      approx: true
      calendar: julian
      certainty: 0.5
      cites: [{source: S1, locator: "opening ('c. 355 ce')"}]
      how_known: "Real dispute (P25): Britannica (Deakin) c. 355; MacTutor about 370."
      alternatives:
        - {value: "370", cites: [{source: S2, locator: "Quick Info ('Born about 370')"}], note: "MacTutor (1999); Britannica's later article (Deakin, author of a Hypatia monograph) prefers c. 355."}
    place: {value: "Alexandria, Egypt", modern_name: "Alexandria, Egypt", polity_then: "Roman Empire (Egypt)", certainty: 0.5, cites: [{source: S2, locator: "Quick Info"}], how_known: "MacTutor; Britannica gives only the death place (0.5)."}
  death:
    date: {value: "0415-03", calendar: julian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Quick Info"}], how_known: "Both give March 415."}
    place: {value: "Alexandria, Egypt", modern_name: "Alexandria, Egypt", polity_then: "Roman Empire (Egypt)", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Quick Info"}], how_known: "Both agree."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "No listed contribution can be dated (P39)."}
  era_bucket: {value: "-500 to 499", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Quick Info"}], how_known: "Every adult year on either birth date (c. 355 or c. 370) to 415 falls in '-500 to 499' (P39); both sources agree on 415."}
  region_of_birth: {value: "Middle East and North Africa", certainty: 0.5, cites: [{source: S2, locator: "Quick Info"}], how_known: "Egypt (P3); birthplace from MacTutor only (0.5)."}
  region_of_work: {value: "Middle East and North Africa", certainty: 1.0, cites: [{source: S1, locator: "text"}, {source: S2, locator: "Biography"}], how_known: "Alexandria, both sources."}
  sex_as_recorded: {value: "female", certainty: 1.0, cites: [{source: S1, locator: "text"}, {source: S2, locator: "Biography"}], how_known: "Both sources."}
  languages_of_work: {value: [Greek], certainty: 0.5, cites: [{source: S1, locator: "text ('the Greek mathematical and astronomical heritage')"}], how_known: "Inferred."}
  occupations: {value: ["mathematician", "astronomer", "philosopher", "teacher"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Biography"}], how_known: "Both sources."}

contribution:
  fields: {value: ["mathematics", "astronomy", "philosophy"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Biography"}], how_known: "Both sources."}
  lasting_original_contributions:
    - {value: "Commentaries on Apollonius's Conics and Diophantus's Arithmetica, and an astronomical table (all lost)", kind: work, lasting: "attempts to reconstruct aspects of them (S1); Deakin calls her an excellent compiler, editor and preserver (S2)", certainty: 0.7, cites: [{source: S1, locator: "text, third paragraph"}, {source: S2, locator: "Biography (Suidas)"}], how_known: "Both report the attribution, which rests on the Suda; MacTutor says 'most historians doubt' any Ptolemy commentary beyond joint work with Theon. Undated (P39)."}
    - {value: "Assisted Theon's commentary on the Almagest and edition of Euclid's Elements", kind: work, lasting: "Theon's Elements 'became the basis for all later editions' (S2)", certainty: 0.5, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor: 'It is also thought'; one source, hedged (0.5). Undated."}
  evidence_of_impact:
    - {value: "Head of the Platonist school at Alexandria; later a symbol of learning", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S2, locator: "Biography"}], how_known: "Both sources; MacTutor dates the headship to about 400."}
  major_works: []
  honours: []
  definition_fit: {value: "arguable", rationale: "Leading mathematician of her time (S1), but 'no evidence that Hypatia undertook original mathematical research' (S2) and all work is lost.", certainty: 0.5, cites: [{source: S1, locator: "text"}, {source: S2, locator: "Biography"}], how_known: "Coder's reading; the sources differ in emphasis."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father Theon of Alexandria, mathematician and astronomer", role: parents, certainty: 1.0, cites: [{source: S1, locator: "text"}, {source: S2, locator: "Biography"}], how_known: "Both sources."}
  household_circumstances: {value: TODO}
  schooling: []
  early_mathematics: {value: "other", certainty: 0.5, cites: [{source: S2, locator: "Biography ('fairly certain that she studied mathematics under ... her father')"}], how_known: "MacTutor, hedged."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Theon of Alexandria (father)", certainty: 0.5, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor, hedged."}
  languages_in_childhood: {value: TODO}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: UNKNOWN, how_known: "No dated work (P39)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No writing of hers survives (S1, S2)."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "Both sources say she taught Neoplatonism (S1: 'Her philosophy was Neoplatonist'; S2: based on Plotinus and Iamblichus), but no text of hers survives: this is later report, which cannot score alone (§7, P42).", note: "Candidate PLATO (Neoplatonism; no separate code)."}
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: PLATO, reason: "Both sources report Neoplatonist teaching (no separate Neoplatonism code exists, so PLATO is the nearest); report only, so not coded."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Britannica describes her Neoplatonism as 'concerned with the approach to the One, an underlying reality'; a reported doctrine, not her own words (P42).", note: "Would point to a non-personal One if her own text existed."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist under P30 (no known original result, S2); no statement on nature survives (P16)."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing survives."}
    D_authority: {value: UNKNOWN, how_known: "Nothing survives."}
    E_scope: {value: UNKNOWN, how_known: "Nothing survives (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN, which takes precedence (§6, P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Coder's call: Synesius's letters to her survive but are his words, not hers (S2); Socrates Scholasticus and the Suda are later reports. Nothing scores."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Greek-speaking Alexandrian", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Inferred."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "No dated work (P39)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "No dated work (P39)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "Nothing of hers survives."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Nothing survives."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Nothing survives."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Commentary on Apollonius's Conics; Euclid edition with Theon (S1, S2).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "childhood or adolescence", certainty: 0.5, cites: [{source: S2, locator: "Biography"}], how_known: "Taught by her father (hedged)."}
  circle_present: {value: "unclear", rationale: "Reported Neoplatonism only.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No reading possible: no text of hers survives."
  notes: ""

institutions:
  - {value: "Platonist school at Alexandria", role: head, years: "c. 400–415", kind: "other", certainty: 0.5, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor 'in about 400 AD'."}
collaborators:
  - {value: "Theon of Alexandria", relation: family, note: "father; joint work on Ptolemy and Euclid", certainty: 0.5, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}
  - {value: "Synesius of Cyrene", relation: "student or assistant", note: "pupil and correspondent", certainty: 1.0, cites: [{source: S1, locator: "text"}, {source: S2, locator: "Biography"}], how_known: "Both sources."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 38"}], how_known: "Study roster."}
  controversies:
    - {value: "Birth year c. 355 vs c. 370; how much original work is hers", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Quick Info; Biography"}], how_known: "The two sources differ."}
  data_quality_flags: []
  open_questions:
    - "Dzielska (1995) or Watts (2017) for any surviving testimony bearing on her own views."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Michael Deakin"
    citation: "Deakin, Michael. \"Hypatia.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Hypatia."
    url: "https://www.britannica.com/biography/Hypatia"
    accessed: 2026-10-15
    reliability_note: "Signed article body; the Top Questions box is not used."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, collaborators, review]
  - id: S2
    type: secondary
    kind: encyclopedia
    author: "J. J. O'Connor and E. F. Robertson"
    year: 1999
    citation: "O'Connor, J. J., and E. F. Robertson. \"Hypatia of Alexandria.\" MacTutor History of Mathematics, University of St Andrews, last update April 1999. https://mathshistory.st-andrews.ac.uk/Biographies/Hypatia/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Hypatia/"
    accessed: 2026-10-15
    reliability_note: "Signed biography."
    used_for: [identity, basics, contribution, childhood, worldview, lane_b, institutions, collaborators, review]
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

# Hypatia

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Hypatia of Alexandria (c. 355 or c. 370–415), mathematician, astronomer and Neoplatonist teacher [S1, S2]. All her works are lost. Draft: primary_system and A BELOW_THRESHOLD; B, C, D, E UNKNOWN; mid_basin UNKNOWN. Not plotted.

## Life and work

Daughter of Theon; head of the Platonist school at Alexandria; murdered by a Christian mob in March 415 [S1, S2].

## Contribution and impact

Commentaries on Apollonius and Diophantus and an astronomical table, all lost [S1, S2].

## Childhood and education

Probably taught by her father [S2].

## Adult working worldview

Reported to have taught Neoplatonism, the approach to 'the One' [S1, S2]. No text of hers survives, so nothing is scored (P42).

## Heritage (context only)

Greek-speaking Alexandria [S1].

## Timing

No dated work (P39).

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Geometry present; circle unclear [S1].

## Open questions

- Dzielska; Watts.

## Research log

- 2026-10-15: Read Britannica (Deakin) and MacTutor.
