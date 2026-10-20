---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA9)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-20, by: "Grok Bot", summary: "AA9 audit fixes: span certainty 0.7 (weakest-work rule); note that the P42 pseudonym treatment rests on analogy."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA9, order P32: F 3, rank 218). Source: SEP 'Søren Kierkegaard' (John Lippitt and C. Stephen Evans, 2023, read in full). Lasting: the authorship, 'almost all of which was written in the 1840s', from Either/Or (1843), which 'he considered properly to begin his authorship'; 'often dubbed the \"father of existentialism\"', it influenced Heidegger, Sartre, Jaspers, Wittgenstein and others (S1). Span 1843–1850 at 0.7 (Either/Or to Practice in Christianity), alternative 1843–1855 (The Moment), age 30. Worldview: CHRIST at 0.5 (scholarly_reconstruction; S1: 'known as a defender of Christian faith'; in The Point of View, in his own voice, he 'claims that he was from first to last a religious author'; S1 paraphrase, not quoted). A UNKNOWN: the one quoted line on God (Sickness Unto Death) is pseudonymous (Anti-Climacus), so not his own voice (P42, applied by analogy: P42 has no explicit pseudonym clause; this follows its character-voice addendum). Not a scientist; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: kierkegaard-soren
  display_name: "Søren Kierkegaard"
  roster:
    canonical_name: "Søren Kierkegaard"
    rank: 218
    F: 3
    models: [Claude, Gemini, Grok]
    band: "core (3–4)"
    status: "core"
    field: "philosophy"
    field_bucket: "philosophy"
  full_name: {value: "Søren Aabye Kierkegaard", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  native_name: {value: "Søren Aabye Kierkegaard", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  aliases:
    - {name: "Soren Kierkegaard", kind: "transliteration"}

basics:
  birth:
    date: {value: "1813-05-05", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "SEP."}
    place: {value: "Copenhagen", modern_name: "Copenhagen, Denmark", polity_then: "Denmark–Norway", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "SEP."}
  death:
    date: {value: "1855-11-11", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "SEP."}
    place: {value: "Copenhagen", modern_name: "Copenhagen, Denmark", polity_then: "Denmark", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "SEP: died in hospital in Copenhagen."}
  first_lasting_contribution_year: {value: 1843, certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "Either/Or 'was published in 1843' (S1); P30 publication."}
  era_bucket: {value: "1750 to 1849", certainty: 1.0, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "1843 (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "Denmark (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "Copenhagen."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Danish"], certainty: 0.7, cites: [{source: S1, locator: "Bibliography"}], how_known: "Works in Danish (SKS)."}
  occupations: {value: ["philosopher", "theologian", "writer"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}

contribution:
  fields: {value: ["philosophy", "theology", "psychology"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  lasting_original_contributions:
    - {value: "The authorship of 1843–1850 (pseudonymous and signed works, from Either/Or and Fear and Trembling to The Sickness Unto Death and Practice in Christianity)", year: 1843, kind: "body of work", lasting: "'often dubbed the \"father of existentialism\"'; it 'has certainly influenced thinkers in the phenomenological and existential traditions (including Heidegger, Sartre, Jaspers, Marcel, and Lévinas)' and Wittgenstein (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; 1. Life and Works"}], how_known: "Either/Or 1843 to Practice in Christianity 1850 (S1)."}
  evidence_of_impact:
    - {value: "Wittgenstein called him 'by far the most profound thinker' of the nineteenth century", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
    - {value: "'father of existentialism'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP, which notes the label 'obscures at least as much as it reveals'."}
  major_works:
    - {value: "Either/Or", year: 1843, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "SEP."}
    - {value: "Concluding Unscientific Postscript", year: 1846, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "SEP."}
    - {value: "Works of Love", year: 1847, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "SEP."}
    - {value: "The Sickness Unto Death", year: 1849, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "SEP."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Wide influence across philosophy, theology, literature and psychotherapy (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Father Michael Pedersen Kierkegaard, wealthy Copenhagen merchant, 'devoutly religious'; mother Anne (Lund); youngest of seven", role: "family", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "SEP."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "University of Copenhagen: first degree in theology; Magister in philosophy (On the Concept of Irony); pastoral seminary, never ordained", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "SEP."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1843–1850", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: 
    value: CHRIST
    basis: scholarly_reconstruction
    certainty: 0.5
    cites: [{source: S1, locator: "1. Life and Works"}]
    how_known: "Scholar's reconstruction: SEP (Lippitt and Evans)."
    rationale: "'known as a defender of Christian faith'; attacked the state church 'in the name of \"New Testament Christianity\"'; at the end 'affirmed to Emil Boesen ... that he was still a believer in Christ'; in The Point of View (written 1848), in his own voice, he 'claims that he was from first to last a religious author' (S1). 0.5: S1 paraphrases rather than quoting him; his signed works (Works of Love; Upbuilding Discourses) would give written_profession at 0.7."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Coded at 0.5 (S1)."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "The one quoted line on God in S1 ('releasing it from his hand, as it were', The Sickness Unto Death) is by the pseudonym Anti-Climacus, not his own voice (P42 by analogy with its character-voice addendum; P42 has no explicit pseudonym clause; he signed the book only as editor). Lead A 0 from his signed discourses."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); no statement on nature read."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Not plotted either way: B is UNKNOWN (not a scientist; see RQ-AA8-1 for the open question on scholars' reconstructions of philosophers' views of nature)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: "Christian (Lutheran, with Moravian influence)", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "SEP: 'brought up as a Lutheran but was also shaped by a Moravian congregation'."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1843–1850", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "The body of work runs from Either/Or (1843) to Practice in Christianity (1850) (P29, P30); 0.7, following the one lasting item (AA4 weakest-work rule); both ends are dated in S1. Alternative 1843–1855 (the 1854–55 attack on the church, The Moment)."}
  age_at_first_lasting_contribution: {value: 30, certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "1843 − 1813 = 30 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Existence, faith, inwardness (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "University of Copenhagen", role: "student (theology; Magister in philosophy)", years: UNKNOWN, kind: "university", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "SEP."}
collaborators:
  - {value: "Regine Olsen", relation: "other", note: "fiancée 1840–1841", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "SEP."}
  - {value: "Emil Boesen", relation: "other", note: "lifelong friend, priest", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "SEP."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 218"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Worldview from scholar's paraphrase only."
    - "Span end 1850 vs 1855."
  open_questions:
    - "Own-voice statement from signed works for CHRIST at 0.7 and A."
    - "Span end: 1850 or 1855?"

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "John Lippitt; C. Stephen Evans"
    citation: "Lippitt, John, and C. Stephen Evans. 'Søren Kierkegaard.' Stanford Encyclopedia of Philosophy (first published 22 May 2023). https://plato.stanford.edu/entries/kierkegaard/"
    url: "https://plato.stanford.edu/entries/kierkegaard/"
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

Søren Kierkegaard (1813–1855), Danish philosopher and theologian [S1]. Draft: CHRIST 0.5; A UNKNOWN. Not plotted.

## Life and work

Copenhagen; brief stays in Berlin [S1].

## Contribution and impact

Authorship 1843–1850 [S1].

## Childhood and education

University of Copenhagen [S1].

## Adult working worldview

Christian (scholar's reading) [S1].

## Heritage (context only)

Lutheran.

## Timing

1843–1850, age 30 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Own-voice statements; span end.

## Research log

- 2026-10-20: AA9 audit fixes: span certainty 0.7 (weakest-work rule); note that the P42 pseudonym treatment rests on analogy.
- 2026-10-20: Read SEP (Lippitt and Evans, 2023).
