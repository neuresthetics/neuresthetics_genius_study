---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA4)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "AA4 audit fix (v8's call on the auditor's advice): Real Algebraic Manifolds (1952, 'seminal', S1) added as lasting; span 1950–1952; the January 1950 PNAS note mentioned (start year unchanged)."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA4, order P32: F 3, rank 192). Sources: Britannica (scholars edition, read in full) and his Nobel autobiography (Les Prix Nobel 1994, read in full). Lasting work: the Nash bargaining solution ('The Bargaining Problem', Econometrica, April 1950) and the Nash equilibrium (thesis 'Non-Cooperative Games', Annals of Mathematics, September 1951), 'Nash thus established the mathematical principles of game theory'; dated by publication (P30 #1). Span 1950–1952 (Real Algebraic Manifolds, November 1952, added as lasting on the AA4 audit), age 22. The 1950 PNAS note on equilibrium points is not in the sources read. Mathematician: game theory makes no testable claim about natural systems (P30), so not a scientist; B UNKNOWN. No profession read: the autobiography's Zarathustra passage is about rationality and madness, not belief. Worldview all UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: nash-john
  display_name: "John Nash"
  roster:
    canonical_name: "John Nash"
    rank: 192
    F: 3
    models: [Claude, GPT, Grok]
    band: "core (3–4)"
    status: "core"
    field: "mathematics"
    field_bucket: "mathematics"
  full_name: {value: "John Forbes Nash, Jr.", certainty: 0.7, cites: [{source: S1, locator: "para. 1"}], how_known: "Britannica."}
  native_name: {value: "John Nash", certainty: 0.7, cites: [{source: S1, locator: "para. 1"}], how_known: "Britannica."}
  aliases:
    - {name: "John-Nash", kind: "roster alias"}

basics:
  birth:
    date: {value: "1928-06-13", certainty: 0.7, cites: [{source: S1, locator: "para. 1"}, {source: S2, locator: "opening paragraph"}], how_known: "Britannica; autobiography."}
    place: {value: "Bluefield, West Virginia", modern_name: "Bluefield, West Virginia, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S2, locator: "opening paragraph"}], how_known: "Autobiography."}
  death:
    date: {value: "2015-05-23", certainty: 0.7, cites: [{source: S1, locator: "para. 1"}], how_known: "Britannica."}
    place: {value: "near Monroe Township, New Jersey", modern_name: "Monroe Township, New Jersey, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "para. 1"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1950, certainty: 0.7, cites: [{source: S1, locator: "para. 3"}], how_known: "'Nash published (April 1950) his first paper, \"The Bargaining Problem,\" in the journal Econometrica' (S1); publication (P30 #1)."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "para. 3"}], how_known: "1950–1951 (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S2, locator: "opening paragraph"}], how_known: "USA (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "para. 2"}], how_known: "Princeton; MIT."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "para. 3"}], how_known: "English papers."}
  occupations: {value: ["mathematician"], certainty: 0.7, cites: [{source: S1, locator: "para. 1"}], how_known: "Britannica."}

contribution:
  fields: {value: ["game theory", "geometry", "partial differential equations"], certainty: 0.7, cites: [{source: S1, locator: "para. 3–4"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Nash bargaining solution ('The Bargaining Problem')", year: 1950, kind: "theory", lasting: "his 'mathematical model for bargaining', expanded in his 'influential' thesis; part of establishing 'the mathematical principles of game theory' (S1)", certainty: 0.7, cites: [{source: S1, locator: "para. 3"}], how_known: "Britannica; Econometrica, April 1950."}
    - {value: "Nash equilibrium ('Non-Cooperative Games')", year: 1951, kind: "theory", lasting: "'Nash thus established the mathematical principles of game theory'; 'the Nash equilibrium was widely applied' (S1); Nobel Prize 1994", certainty: 0.7, cites: [{source: S1, locator: "para. 1, 3"}], how_known: "Britannica; Annals of Mathematics, September 1951 (an earlier PNAS note, January 1950, is not in the sources read; the start year is unchanged)."}
    - {value: "Real Algebraic Manifolds (Nash's theorem on real algebraic varieties)", year: 1952, kind: "theory", lasting: "'his seminal paper' (S1)", certainty: 0.7, cites: [{source: S1, locator: "para. 4"}], how_known: "Britannica; Annals of Mathematics, November 1952. Added as lasting on the AA4 audit (v8's call on the auditor's advice)."}
  evidence_of_impact:
    - {value: "Nobel Prize in Economics (1994); Abel Prize (2015)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "para. 1"}], how_known: "Britannica."}
  major_works:
    - {value: "Nash embedding theorems", kind: "paper or paper series", certainty: 0.5, cites: [{source: S1, locator: "para. 4"}, {source: S2, locator: "paragraph on the embedding problem"}], how_known: "Britannica: 'among the most original results in geometric analysis of the twentieth century' (Norwegian Academy); undated in the sources read."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founded the mathematics of non-cooperative games; embedding theorems (S1).", certainty: 0.7, cites: [{source: S1, locator: "para. 3–4"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Father an electrical engineer; mother a former teacher of English and Latin", role: "family", certainty: 0.7, cites: [{source: S2, locator: "paragraphs on his parents"}], how_known: "Autobiography."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Carnegie Tech (BS, MS 1948); Princeton (PhD 1950)", certainty: 0.7, cites: [{source: S1, locator: "para. 2"}], how_known: "Britannica."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1950–1952", certainty: 0.7, cites: [{source: S1, locator: "para. 3"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "No profession read. His Nobel autobiography (1995, after the span) says 'rationality of thought imposes a limit on a person's concept of his relation to the cosmos' and discusses Zarathustra's 'madness' (S2): about rationality, not a stated belief."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered: []
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing first-hand on God read (P19)."}
    B_cause: {value: UNKNOWN, how_known: "Mathematician: game theory and geometry make no testable claims about natural systems (P30); no statement on nature read."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Look in Nasar's A Beautiful Mind (1998) for his own words on religion, and in later interviews."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated in the sources read."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1950–1952", certainty: 0.7, cites: [{source: S1, locator: "para. 3"}], how_known: "From 'The Bargaining Problem' (1950) to 'Real Algebraic Manifolds' (1952), the listed lasting works (P29, P30 #1)."}
  age_at_first_lasting_contribution: {value: 22, certainty: 0.7, cites: [{source: S1, locator: "para. 1, 3"}], how_known: "1950 − 1928 = 22 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Riemannian embedding, a geometric problem (S2).", certainty: 0.5, cites: [{source: S2, locator: "paragraph on the embedding problem"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Massachusetts Institute of Technology", role: "mathematics faculty", years: "1951–1959", kind: "university", certainty: 0.7, cites: [{source: S2, locator: "paragraph on M.I.T., 1951–1959"}], how_known: "Autobiography."}
  - {value: "Princeton University", role: "senior research mathematician", years: "1995–2015", kind: "university", certainty: 0.7, cites: [{source: S1, locator: "para. 2"}], how_known: "Britannica; end year his death."}
collaborators:
  - {value: "A. W. Tucker", relation: "teacher", note: "recruited him to Princeton", certainty: 0.5, cites: [{source: S2, locator: "paragraph on choosing Princeton"}], how_known: "Autobiography: Tucker wrote encouraging him to come; supervision not stated."}
  - {value: "Louis Nirenberg", relation: "collaborator", note: "suggested Hilbert's 19th problem; shared the Abel Prize", certainty: 0.7, cites: [{source: S1, locator: "para. 4"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 192"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "No worldview source."
  open_questions:
    - "Own words on religion (Nasar; interviews)."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Britannica Editors"
    citation: "'John Nash.' Britannica (scholars edition). https://kids.britannica.com/scholars/article/John-Nash/1531"
    url: "https://kids.britannica.com/scholars/article/John-Nash/1531"
    accessed: 2026-10-19
    reliability_note: "Encyclopedia article, read in full; unsigned (The Editors)."
    used_for: [identity, basics, contribution, timing, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "John F. Nash Jr."
    citation: "Nash, John F., Jr. 'Biographical.' Les Prix Nobel 1994, ed. Tore Frängsmyr (Nobel Foundation, 1995). https://www.nobelprize.org/prizes/economic-sciences/1994/nash/biographical/"
    url: "https://www.nobelprize.org/prizes/economic-sciences/1994/nash/biographical/"
    accessed: 2026-10-19
    reliability_note: "His Nobel autobiography, read in full on the Nobel Foundation site."
    used_for: [identity, childhood, worldview, institutions, collaborators]
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

John Nash (1928–2015), mathematician [S1]. Draft: all UNKNOWN. Not plotted.

## Life and work

Bluefield; Pittsburgh; Princeton; MIT [S1, S2].

## Contribution and impact

Bargaining (1950); equilibrium (1951); real algebraic manifolds (1952) [S1].

## Childhood and education

Carnegie Tech; Princeton [S1].

## Adult working worldview

None read.

## Heritage (context only)

Not stated.

## Timing

1950–1952, age 22 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Own words on religion.

## Research log

- 2026-10-19: AA4 audit fix (v8's call on the auditor's advice): Real Algebraic Manifolds (1952, 'seminal', S1) added as lasting; span 1950–1952; the January 1950 PNAS note mentioned (start year unchanged).
- 2026-10-19: Read Britannica (scholars); Nobel autobiography.
