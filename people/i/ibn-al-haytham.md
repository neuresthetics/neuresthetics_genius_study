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
    - {date: 2026-10-19, by: "Grok Bot", summary: "AA1 audit fixes: era certainty 0.7 -> 0.5 (P39, c. life dates; WEAKEN). Span set from Smith's critical edition, 'Sometime between 1028 and 1038' (S3, added), under RQ-Z9-N1: start 1028 (P12), span 1028–1038, age 63 (1028 − c. 965); v8's call on the auditor's advice. Coder note corrected: the 1011–1021 date (Tbakhi and Amr 2007) is not used. Still not plotted (A UNKNOWN)."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA1, order P32: F 3, rank 182). Basics from Britannica (Richard Lorch, signed; body) and MacTutor (O'Connor and Robertson). No own-voice religious text read. MacTutor reports that in his autobiography he concluded as a youth that none of the religious movements 'represented the truth'; Britannica notes it 'has recently been plausibly argued' that the autobiography is by a different Ibn al-Haytham (Muhammad ibn al-Hasan), so its attribution is disputed (P42) and it is a lead only. primary_system UNKNOWN (lead ISLAM); A UNKNOWN. Scientist: the Optics gives a theory of vision and the laws of reflection and refraction (P30), so B 3 at 0.5 from working science, alt 4 (P24, P35). C, D, E UNKNOWN; mid_basin UNKNOWN. Span 1028–1038 (Smith's composition range, RQ-Z9-N1; AA1 audit fix), age 63. Not plotted. Draft, not reviewed."}

identity:
  id: ibn-al-haytham
  display_name: "Ibn al-Haytham (Alhazen)"
  roster:
    canonical_name: "Ibn al-Haytham (Alhazen)"
    rank: 182
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: "core"
    field: "polymath"
    field_bucket: "polymath"
  full_name: {value: "Abū ʿAlī al-Ḥasan ibn al-Haytham", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica ('in full'); Britannica names the optics author al-Ḥasan ibn al-Ḥasan."}
  native_name: {value: "ابن الهيثم", certainty: 0.5, cites: [{source: S1, locator: "heading"}], how_known: "Arabic spelling the coder's."}
  aliases:
    - {name: "Ibn al-Haytham", kind: "roster alias"}
    - {name: "Alhazen", kind: "latinized"}

basics:
  birth:
    date: {value: "965", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Britannica: c. 965."}
    place: {value: "Basra", modern_name: "Basra, Iraq", polity_then: "Buyid emirate (Abbasid caliphate)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1040", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Britannica: c. 1040."}
    place: {value: "Cairo", modern_name: "Cairo, Egypt", polity_then: "Fatimid caliphate", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1028, certainty: 0.5, cites: [{source: S3, locator: "Preface"}], how_known: "Smith: 'Sometime between 1028 and 1038, Ibn al-Haytham completed his monumental optical synthesis, Kitab al-Manazir'; a specialist's composition range in article text dates a manuscript-era work, start as the year (RQ-Z9-N1, P12); v8's call on the auditor's advice (AA1)."}
  era_bucket: {value: "500 to 1399", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Lifetime c. 965–1040 (P2); certainty of the c. life dates (P39; AA1 audit)."}
  region_of_birth: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Iraq (P3)."}
  region_of_work: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "Life"}], how_known: "Cairo."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Arabic"], certainty: 0.7, cites: [{source: S1, locator: "Major works"}], how_known: "Britannica."}
  occupations: {value: ["mathematician", "astronomer", "physicist"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["optics", "mathematics", "astronomy"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Kitāb al-manāẓir (Optics): theory of vision by received light; laws of reflection; refraction", year: 1028, kind: "theory", lasting: "'Ibn al-Haytham's most important work is Kitāb al-manāẓir (\"Optics\") ... it contains the correct model of vision' (S1, body)", certainty: 0.7, cites: [{source: S1, locator: "Major works"}], how_known: "Britannica body; dated 1028–1038 by Smith (S3), start 1028 (P12)."}
  evidence_of_impact:
    - {value: "Made significant contributions to the principles of optics and the use of scientific experiments", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "al-Shukūk ʿalā Baṭlamyūs (Doubts about Ptolemy)", year: UNKNOWN, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "Major works"}], how_known: "Britannica."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Optics: correct model of vision (S1).", certainty: 0.7, cites: [{source: S1, locator: "Major works"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household: []
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
  working_years: {value: "1028–1038", certainty: 0.5, cites: [{source: S3, locator: "Preface"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "No own-voice religious text read. Lead ISLAM (Muslim setting; Cairo near al-Azhar, S2). The autobiography's report that as a youth he found none of the religious movements 'represented the truth' (S2) is a lead only: its attribution to the optics author is disputed (S1; P42)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: ISLAM, reason: "Lead: setting; autobiography disputed."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing first-hand read (P19)."}
    B_cause: 
      value: 3
      basis: inference_from_work
      certainty: 0.5
      cites: [{source: S1, locator: "Major works"}]
      how_known: "Scientist (P30): the Optics states a theory of vision and laws of reflection and refraction, with experiment (S1). B inferred from working science with no statement of his own on law and exception, so 3 at 0.5, alternative 4, never 4 (P24, P35)."
      rationale: "Laws of reflection; refraction 'correctly explained by light's moving slower in denser mediums' (S1): lawful nature in his science. Alternative 4."
      alternatives:
        - {value: 4, note: "Working science cannot tell lawful-with-exceptions from exceptionless (P35).", cites: [{source: S1, locator: "Major works"}]}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Lead: he will 'seek the truth and not be swayed by opinions' (Optics I, as quoted by MacTutor, S2); not scored."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Read Sabra's translation of Optics I–III and the autobiography (Ibn Abi Usaybi'a) and settle its attribution (Rashed's two-Ibn-al-Haytham thesis); the span uses Smith's specialist range 1028–1038 (El-Bizri and the Peterhouse manuscript note give the same, per the AA1 audit; not read); the 1011–1021 date in Tbakhi and Amr (2007), a physicians' overview, conflicts with it and is not used."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated in the sources read."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1028–1038", certainty: 0.5, cites: [{source: S3, locator: "Preface"}], how_known: "Smith's composition range for the Optics, the one listed lasting work (RQ-Z9-N1, P12, P30 end); v8's call on the auditor's advice (AA1)."}
  age_at_first_lasting_contribution: {value: 63, certainty: 0.5, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "Preface"}], how_known: "1028 − 965 = 63 (P30 year difference); birth c. 965, so about 63."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Geometrical optics; conic sections (S1).", certainty: 0.5, cites: [{source: S1, locator: "Major works"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions: []
collaborators:
  - {value: "al-Ḥākim", relation: "mentor or employer", note: "Fatimid caliph; Nile scheme", certainty: 0.7, cites: [{source: S2, locator: "text"}], how_known: "MacTutor (Ibn al-Qifṭī's account)."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 182"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Autobiography's attribution disputed."
  open_questions:
    - "Optics composition range; autobiography."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Richard Lorch"
    citation: "Lorch, Richard. 'Ibn al-Haytham.' Encyclopaedia Britannica. https://www.britannica.com/biography/Ibn-al-Haytham"
    url: "https://www.britannica.com/biography/Ibn-al-Haytham"
    accessed: 2026-10-19
    reliability_note: "Signed article; body read, question boxes not used (P26)."
    used_for: [identity, basics, contribution, worldview, lane_b, collaborators]
  - id: S2
    type: tertiary
    kind: "encyclopedia"
    author: "J. J. O'Connor and E. F. Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. 'Abu Ali al-Hasan ibn al-Haytham.' MacTutor History of Mathematics. https://mathshistory.st-andrews.ac.uk/Biographies/Al-Haytham/"
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Al-Haytham/"
    accessed: 2026-10-19
    reliability_note: "Signed reference biography."
    used_for: [worldview]
  - id: S3
    type: secondary
    kind: "scholarly edition"
    author: "A. Mark Smith"
    citation: "Smith, A. Mark. Alhacen's Theory of Visual Perception, vol. 1. Transactions of the American Philosophical Society 91, no. 4 (2001), Preface and Introduction pp. xvi–xviii. https://dlib.biblhertz.it/perspectiva/doc01.html"
    url: "https://dlib.biblhertz.it/perspectiva/doc01.html"
    accessed: 2026-10-19
    reliability_note: "Critical edition by a specialist; preface read (Bibliotheca Hertziana; Internet Archive text of the introduction)."
    used_for: [basics, contribution, timing]
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

Ibn al-Haytham (c. 965–c. 1040), mathematician and physicist [S1]. Draft: UNKNOWN (lead ISLAM); B 3 (0.5). Not plotted.

## Life and work

Basra; Cairo [S1].

## Contribution and impact

Optics [S1].

## Childhood and education

Not read.

## Adult working worldview

None read; autobiography disputed [S1, S2].

## Heritage (context only)

Not stated.

## Timing

1028–1038, age about 63 [S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Autobiography.

## Research log

- 2026-10-19: AA1 audit fixes: era certainty 0.7 -> 0.5 (P39, c. life dates; WEAKEN). Span set from Smith's critical edition, 'Sometime between 1028 and 1038' (S3, added), under RQ-Z9-N1: start 1028 (P12), span 1028–1038, age 63 (1028 − c. 965); v8's call on the auditor's advice. Coder note corrected: the 1011–1021 date (Tbakhi and Amr 2007) is not used. Still not plotted (A UNKNOWN).
- 2026-10-19: Read Britannica (Lorch); MacTutor; Smith's edition (preface).
