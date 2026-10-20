---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z7)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z7, order P32: F 3, rank 162). Source: SEP 'John Duns Scotus' (Thomas Williams, rev. 2025), a scholar's account of his works with Ordinatio and Lectura locators. No Latin or translated primary text read, so the worldview rests on scholarly_reconstruction (0.7 cap). Franciscan friar, priest (1291) and master of theology at Paris. primary_system CLASS_THEISM (0.5, scholarly_reconstruction cap). A 1 (0.5, alt 0): first agent with intellect and will, infinite being; univocity makes the God–creature difference 'one of degree'. B 3 (0.5, alt 2): certainty about 'causal judgments derived from experience', but God 'can cause immediately ... whatever he ordinarily causes through a secondary cause' and all contingent truth hangs on his free will. C, D, E UNKNOWN. mid_basin BELOW_THRESHOLD (A and B at 0.5). Plotted (A 1, B 3). Span 1298–1308. Draft, not reviewed."}

identity:
  id: scotus-duns
  display_name: "John Duns Scotus"
  roster:
    canonical_name: "Duns Scotus"
    rank: 162
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: "core"
    field: "philosophy"
    field_bucket: "philosophy"
  full_name: {value: "John Duns Scotus", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}], how_known: "SEP."}
  native_name: {value: "Iohannes Duns Scotus", certainty: 0.5, cites: [{source: S1, locator: "§1.1"}], how_known: "SEP gives the family name Duns; the Latin form is the coder's."}
  aliases:
    - {name: "John Duns Scotus", kind: "roster alias"}
    - {name: "the Subtle Doctor", kind: "title or honorific"}

basics:
  birth:
    date: {value: "1263", certainty: 0.5, cites: [{source: S1, locator: "§1.1"}], how_known: "SEP: 'a birth year of 1263 or 1264 is therefore likely' (Dumont 2023)."}
    place: {value: "Duns", modern_name: "Duns, Scotland, United Kingdom", polity_then: "Kingdom of Scotland", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}], how_known: "SEP."}
  death:
    date: {value: "1308-11-08", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "§1.1"}], how_known: "SEP."}
    place: {value: "Cologne", modern_name: "Cologne, Germany", polity_then: "Holy Roman Empire", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}], how_known: "SEP."}
  first_lasting_contribution_year: {value: 1298, certainty: 0.7, cites: [{source: S1, locator: "§1.1; §2.2"}], how_known: "Lectura (Oxford lectures 1298–99), with his proof of God (Lectura 1 d. 2 q. 1), 'one of the most outstanding contributions ever made to natural theology'."}
  era_bucket: {value: "500 to 1399", certainty: 1.0, cites: [{source: S1, locator: "§1.1"}], how_known: "1298 (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}], how_known: "Scotland, UK (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.5, cites: [{source: S1, locator: "§1.1"}], how_known: "Oxford 1298–1302 and 1303–04; Paris 1302–03 and 1304–07 (Western Europe). Coder's call on a near-even split, 0.5."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Latin"], certainty: 0.7, cites: [{source: S1, locator: "Bibliography"}], how_known: "Latin works."}
  occupations: {value: ["Franciscan friar", "priest", "master of theology"], certainty: 0.7, cites: [{source: S1, locator: "§1.1"}], how_known: "SEP."}

contribution:
  fields: {value: ["philosophy", "theology", "metaphysics"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  lasting_original_contributions:
    - {value: "Proof of the existence of God (triple primacy)", year: 1298, kind: "concept or term", lasting: "'one of the most outstanding contributions ever made to natural theology' (S1)", certainty: 0.7, cites: [{source: S1, locator: "§2.2"}], how_known: "SEP; first version in the Lectura, 1298–99."}
    - {value: "Univocity of being; haecceity; formal distinction (Ordinatio)", year: 1308, kind: "body of work", lasting: "'left a mark' on religious language, universals, freedom (S1)", certainty: 0.5, cites: [{source: S1, locator: "opening; §1.2; §3.3"}], how_known: "SEP; the Ordinatio was revised until his death, so the span end is 0.5."}
  evidence_of_impact:
    - {value: "One of the most important and influential philosopher-theologians of the High Middle Ages", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  major_works:
    - {value: "Ordinatio", year: 1308, kind: "book", certainty: 0.5, cites: [{source: S1, locator: "§1.2"}], how_known: "SEP: begun by June 1300, unfinished at death."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Among the most influential medieval philosophers (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}

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
  working_years: {value: "1298–1308", certainty: 0.5, cites: [{source: S1, locator: "§1.1; §1.2"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: 
    value: CLASS_THEISM
    basis: scholarly_reconstruction
    certainty: 0.5
    cites: [{source: S1, locator: "§1.1; §2.2; §2.3"}]
    how_known: "SEP reconstruction of the Lectura and Ordinatio; Franciscan priest and master of theology; no primary text read; scholarly_reconstruction caps at 0.5."
    rationale: "Natural theology proving a first agent with intellect and will, infinite and unique (S1 §2.2), within Catholic theology: CLASS_THEISM, as for Aquinas."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CLASS_THEISM, reason: "Coded."}
    - {code: CHRIST, reason: "Broader label; CLASS_THEISM is the closer system (as Aquinas)."}
  lio_axes:
    A_locus: 
      value: 1
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S1, locator: "§2.2; §2.3"}]
      how_known: "SEP's reconstruction; no primary text read; contested reading, so 0.5."
      rationale: "God is the first efficient cause with intellect and will, infinite and one (Lectura/Ordinatio 1 d. 2). Univocity makes the God–creature difference 'ultimately one of degree' (Cross, quoted in S1), which weakens transcendence less than it strengthens personhood. 1, as CLASS_THEISM; alternative 0."
      alternatives:
        - {value: 0, note: "Infinite will and intellect, univocally personal.", cites: [{source: S1, locator: "§2.3"}]}
    B_cause: 
      value: 3
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S1, locator: "§3.2; §4.3; §5.1"}]
      how_known: "SEP's reconstruction; account of nature (P6); 0.5 because the voluntarist reading is contested (S1 cites Borland and Hillman 2017; Ward 2019)."
      rationale: "Nature runs through secondary causes and we have certainty 'with respect to quite a lot of causal judgments derived from experience' (S1 §4.3). The stated exception: 'God can cause immediately ... whatever he ordinarily causes through a secondary cause' (§3.2), and every contingent truth depends on his free will (§5.1). Alternative 2 if divine absolute power is read as reaching ordinarily into nature."
      alternatives:
        - {value: 2, note: "Strong voluntarism: nature's order wholly contingent on divine will.", cites: [{source: S1, locator: "§5.1"}]}
    C_ledger: {value: UNKNOWN, how_known: "Not scored from the sections read (soul's survival known 'only through faith', §3.2)."}
    D_authority: {value: UNKNOWN, how_known: "Not scored (natural theology vs revelation not fully read)."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus and B_cause are scored only at 0.5, under the P4 test's 0.7 bar."}
  statements: []
  changes_over_life: []
  coder_notes: "Read Ordinatio I d. 2 (Wolter, Philosophical Writings) and the miracles questions first-hand to lift A and B above 0.5."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Scottish", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}], how_known: "SEP."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1298–1308", certainty: 0.5, cites: [{source: S1, locator: "§1.1; §1.2"}], how_known: "Lectura (1298–99) to his death with the Ordinatio unfinished (P29, P30)."}
  age_at_first_lasting_contribution: {value: 35, certainty: 0.5, cites: [{source: S1, locator: "§1.1"}], how_known: "1298 − 1263 = 35 (P30 year difference); birth year 1263 or 1264."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "Metaphysics as a science from self-evident principles by deduction; stepwise proof of God (S1).", certainty: 0.5, cites: [{source: S1, locator: "§2.2; §3.1"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "University of Paris (Franciscan chair)", role: "master of theology", years: "1305–1307", kind: "university", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}], how_known: "SEP."}
  - {value: "Order of Friars Minor (Franciscans)", role: "friar; priest from 1291", years: "–1308", kind: "religious body", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}], how_known: "SEP."}
collaborators:
  - {value: "Thomas Aquinas", relation: "rival or critic", note: "Scotus argues against analogy and Aquinas's view of freedom", certainty: 0.7, cites: [{source: S1, locator: "§2.1; §5.2"}], how_known: "SEP."}
  - {value: "Henry of Ghent", relation: "rival or critic", note: "illuminationism", certainty: 0.7, cites: [{source: S1, locator: "§4.3"}], how_known: "SEP."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 162"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Worldview from one scholarly reference only; no primary text read."
  open_questions:
    - "Ordinatio first-hand."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Thomas Williams"
    citation: "Williams, Thomas. 'John Duns Scotus.' Stanford Encyclopedia of Philosophy (rev. 15 Dec 2025). https://plato.stanford.edu/entries/duns-scotus/"
    url: "https://plato.stanford.edu/entries/duns-scotus/"
    accessed: 2026-10-19
    reliability_note: "Peer-reviewed reference entry by a Scotus scholar."
    used_for: [identity, basics, contribution, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
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

John Duns Scotus (c. 1263–1308), Franciscan philosopher-theologian [S1]. Draft: CLASS_THEISM (0.5); A 1 and B 3 at 0.5. Plotted.

## Life and work

Cambridge, Paris, Oxford, Cologne [S1].

## Contribution and impact

Proof of God; univocity; haecceity [S1].

## Childhood and education

Not read.

## Adult working worldview

Classical theism with a strong doctrine of divine freedom [S1].

## Heritage (context only)

Scottish [S1].

## Timing

1298–1308, age 35 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Ordinatio first-hand.

## Research log

- 2026-10-19: Read SEP.
