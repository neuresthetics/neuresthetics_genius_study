---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AB1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-20
  change_log:
    - {date: 2026-10-20, by: "Grok Bot", summary: "AB1 audit note: A 1 now rests on §6.2/§7.2; B stays UNKNOWN, held with Plotinus and Duns Scotus under RQ-AA8-1 pending Jason."}
    - {date: 2026-10-20, by: "Grok Bot", summary: "Record created (stage 3 batch AB1, order P32: F 3, rank 227). Source: SEP 'William of Ockham' (Spade, Panaccio and Pelletier, 2024, read in full). Lasting: metaphysical nominalism, for which he is 'probably best known today', and 'Ockham's Razor', 'named after him' (S1). Dated by the academic writings, begun with the Sentences commentary (1317–18) and largely finished by about 1325 (S1): composition range 1317–1325 at 0.5 (RQ-Z9-N1), age 30 (born c. 1287). Worldview: Franciscan friar and theologian; CLASS_THEISM at 0.5 (scholarly_reconstruction; Duns Scotus precedent); A 1 at 0.5 (God's power can override natural causes; divine command ethics; S1). B: S1 §5–6 sets out his natural philosophy (natural causes act 'in the natural order and in the absence of divine intervention'; God 'can always' neutralize a natural effect), but that is a scholar's reconstruction for a non-scientist, so B stays UNKNOWN pending RQ-AA8-1 (Jason undecided). Note for Jason: the Duns Scotus record already carries a reconstruction-based B 3 (0.5). Not plotted. Draft, not reviewed."}

identity:
  id: william-of-ockham
  display_name: "William of Ockham"
  roster:
    canonical_name: "William of Ockham"
    rank: 227
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: "core"
    field: "philosophy"
    field_bucket: "philosophy"
  full_name: {value: "William of Ockham", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  native_name: {value: UNKNOWN, how_known: "Latin form (Guillelmus de Ockham) not printed in S1."}
  aliases:
    - {name: "Occam", kind: "transliteration"}

basics:
  birth:
    date: {value: "1287", certainty: 0.5, cites: [{source: S1, locator: "opening; 1.1"}], how_known: "SEP: 'c. 1287'."}
    place: {value: "Ockham, Surrey", modern_name: "Ockham, Surrey, United Kingdom", polity_then: "Kingdom of England", certainty: 0.5, cites: [{source: S1, locator: "1.1"}], how_known: "SEP: village of Ockham; 'probably' schooled there."}
  death:
    date: {value: "1347-04-10", certainty: 0.5, cites: [{source: S1, locator: "1.3"}], how_known: "SEP: 'on the night of April 9/10, 1347'; alternative 1347-04-09."}
    place: {value: "Munich", modern_name: "Munich, Germany", polity_then: "Holy Roman Empire (Duchy of Bavaria)", certainty: 0.5, cites: [{source: S1, locator: "1.3"}], how_known: "SEP: stayed in Munich 'or at any rate in areas under imperial control, until his death'."}
  first_lasting_contribution_year: {value: 1317, certainty: 0.5, cites: [{source: S1, locator: "2. Writings"}], how_known: "Commentary on the Sentences (1317–18), the first of the academic writings where his nominalism is set out (S1); composition range start (RQ-Z9-N1); 0.5."}
  era_bucket: {value: "500 to 1399", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "1317, and every year of his life, falls in 500 to 1399 (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.5, cites: [{source: S1, locator: "1.1"}], how_known: "England (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "1.1; 2"}], how_known: "Oxford and London, where the academic writings were done (AA6 rule); alternatives Western Europe (Avignon, Munich)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Latin"], certainty: 0.7, cites: [{source: S1, locator: "notes"}], how_known: "SEP note 2."}
  occupations: {value: ["philosopher", "theologian", "Franciscan friar"], certainty: 0.7, cites: [{source: S1, locator: "opening; 1.1"}], how_known: "SEP."}

contribution:
  fields: {value: ["philosophy", "logic", "theology", "political philosophy"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  lasting_original_contributions:
    - {value: "Metaphysical nominalism and ontological reduction to substance and quality (academic writings, Sentences commentary to Summa of Logic)", year: 1317, kind: "theory", lasting: "'He is probably best known today for his espousal of metaphysical nominalism' (S1)", certainty: 0.5, cites: [{source: S1, locator: "opening; 2; 4.2–4.3"}], how_known: "Academic writings 1317–c.1325 (S1); composition range start (RQ-Z9-N1)."}
    - {value: "Ockham's Razor (methodological principle of parsimony)", year: UNKNOWN, kind: "law or principle", lasting: "'the principle known as \"Ockham's Razor\" is named after him' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; 4.1"}], how_known: "S1 does not date his fullest formulation."}
  evidence_of_impact:
    - {value: "Ockham's Razor", kind: "named after them", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  major_works:
    - {value: "Summa of Logic", year: 1323, kind: "book", certainty: 0.5, cites: [{source: S1, locator: "2"}], how_known: "SEP: 'c. 1323–25'."}
    - {value: "Seven Quodlibets", year: 1322, kind: "book", certainty: 0.5, cites: [{source: S1, locator: "2"}], how_known: "SEP: London disputations 1322–24, revised 1324–25."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Among the most prominent late-medieval philosophers (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Given to the Franciscan Order as an oblate between ages seven and thirteen", role: "other", certainty: 0.7, cites: [{source: S1, locator: "1.1"}], how_known: "SEP."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "London Greyfriars; theology from about 1310; Oxford by 1318–19", certainty: 0.7, cites: [{source: S1, locator: "1.1"}], how_known: "SEP."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1317–1325", certainty: 0.5, cites: [{source: S1, locator: "2"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: 
    value: CLASS_THEISM
    basis: scholarly_reconstruction
    certainty: 0.5
    cites: [{source: S1, locator: "1.1; 4.4; 6.2; 7.2"}]
    how_known: "Scholar's reconstruction: SEP (Spade, Panaccio, Pelletier)."
    rationale: "A Franciscan friar and theologian whose metaphysics, epistemology and ethics turn on God's power and decrees (S1: 'certain intentions, become morally obligatory ... simply because God decrees so'). Duns Scotus precedent (CLASS_THEISM 0.5, scholarly_reconstruction). 0.5: no own words quoted."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CLASS_THEISM, reason: "Coded at 0.5 (S1)."}
    - {code: CHRIST, reason: "Franciscan; the more specific Christian code is an alternative."}
  lio_axes:
    A_locus: 
      value: 1
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S1, locator: "6.2; 7.2"}]
      how_known: "SEP's reconstruction; no primary text read; 0.5 (Duns Scotus precedent)."
      rationale: "Main basis §6.2 and §7.2: God can 'neutralize the natural causal effect' of a cognition, 'something He can always do, according to Ockham' (§6.2); moral obligation follows God's decree (§7.2). (§4.4's 'in the absence of divine intervention' concerns parts uniting into a whole and is weak support.) A personal God outside the world who acts in it: A 1."
      alternatives:
        - {value: 0, note: "A personal God wholly outside the world, if the decree-based ethics is read as strict voluntarism.", cites: [{source: S1, locator: "7.2"}]}
    B_cause: {value: UNKNOWN, how_known: "Held UNKNOWN: Jason has not ruled on RQ-AA8-1 (whether a scholar's reconstruction of a non-scientist's account of nature gives B), so no reconstruction-based B is applied. S1 §4.4 and §6.2 reconstruct an account of nature (natural causes act in the absence of divine intervention; God can always override); the B 3 reading is held, as for Plotinus. Not a scientist (natural philosophy of a broadly Aristotelian sort, S1 §5)."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN, so the P4 test cannot be applied."}
  statements: []
  changes_over_life: []
  coder_notes: "Duns Scotus (people/s/scotus-duns.md) carries B 3 at 0.5 from SEP's reconstruction, which is the same kind of call RQ-AA8-1 holds; flagged for Jason, not changed."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: "Christian (Catholic)", certainty: 0.5, cites: [{source: S1, locator: "1.1"}], how_known: "Oblate to the Franciscans as a child (S1); inferred."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1317–1325", certainty: 0.5, cites: [{source: S1, locator: "2"}], how_known: "Academic writings from the Sentences commentary (1317–18) to the Summa of Logic (c. 1323–25) (P29, P30, RQ-Z9-N1); the Razor is undated. 0.5."}
  age_at_first_lasting_contribution: {value: 30, certainty: 0.5, cites: [{source: S1, locator: "opening; 2"}], how_known: "1317 − 1287 = 30 (P30 year difference); birth year 'c.'."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Logic and metaphysics (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Franciscan Order", role: "friar", years: UNKNOWN, kind: "religious body", certainty: 0.7, cites: [{source: S1, locator: "1.1"}], how_known: "SEP."}
  - {value: "Court of Ludwig of Bavaria, Munich", role: "refugee and polemicist", years: "1328/29–1347", kind: "patron or funder", certainty: 0.7, cites: [{source: S1, locator: "1.3"}], how_known: "SEP."}
collaborators:
  - {value: "Michael of Cesena", relation: "collaborator", note: "Franciscan minister general; fled Avignon with him in 1328", certainty: 0.7, cites: [{source: S1, locator: "1.3"}], how_known: "SEP."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 227"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "B held under RQ-AA8-1."
    - "Duns Scotus precedent conflict (reconstruction-based B already in the repo)."
  open_questions:
    - "B under RQ-AA8-1 (reconstruction gives 3 at 0.5)."
    - "Date of the Razor's fullest formulation."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Paul Vincent Spade; Claude Panaccio; Jenny Pelletier"
    citation: "Spade, Paul Vincent, Claude Panaccio, and Jenny Pelletier. 'William of Ockham.' Stanford Encyclopedia of Philosophy (substantive revision 11 September 2024). https://plato.stanford.edu/entries/ockham/"
    url: "https://plato.stanford.edu/entries/ockham/"
    accessed: 2026-10-19
    reliability_note: "Signed encyclopedia entry, read in full."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators]
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

William of Ockham (c. 1287–1347), Franciscan philosopher [S1]. Draft: CLASS_THEISM 0.5, A 1 at 0.5, B held. Not plotted.

## Life and work

Ockham; London; Oxford; Avignon; Munich [S1].

## Contribution and impact

Nominalism 1317–c.1325; the Razor [S1].

## Childhood and education

Greyfriars; Oxford [S1].

## Adult working worldview

Classical theism (scholar's reading) [S1].

## Heritage (context only)

Catholic (inferred).

## Timing

1317–1325, age 30 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- B (RQ-AA8-1).

## Research log

- 2026-10-20: AB1 audit note: A 1 now rests on §6.2/§7.2; B stays UNKNOWN, held with Plotinus and Duns Scotus under RQ-AA8-1 pending Jason.
- 2026-10-20: Read SEP (Spade, Panaccio, Pelletier, 2024).
