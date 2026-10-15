---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch I)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-15
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch I, order P32: F 5, rank 59). Basics from Britannica (Gilbert), signed body through the early works only (the fetch returned only that part). Worldview from Sonnet LXV (dated 19 September 1554, sent to Vasari), Symonds's translation, Gutenberg #10314 (web copy). Not a scientist. primary_system CHRIST 0.5; A 0 at 0.5 (alt 1); B UNKNOWN (P16); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Not plotted. Draft, not reviewed."}

identity:
  id: michelangelo
  display_name: "Michelangelo"
  roster:
    canonical_name: "Michelangelo"
    rank: 59
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: art
    field_bucket: arts
  full_name: {value: "Michelangelo di Lodovico Buonarroti Simoni", certainty: 0.7, cites: [{source: S1, locator: "header ('In full')"}], how_known: "Britannica."}
  native_name: {value: UNKNOWN, how_known: "Italian, Latin script."}
  aliases:
    - {name: "Michelangelo Buonarroti", kind: "roster alias"}
    - {name: "Michael Angelo", kind: other}

basics:
  birth:
    date: {value: "1475-03-06", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; before 1582, so Julian."}
    place: {value: "Caprese, Republic of Florence", modern_name: "Caprese Michelangelo, Italy", polity_then: "Republic of Florence", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Britannica gives Caprese; the modern name is the coder's (0.5)."}
  death:
    date: {value: "1564-02-18", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; Julian."}
    place: {value: "Rome, Papal States", modern_name: "Rome, Italy", polity_then: "Papal States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1498, certainty: 0.5, cites: [{source: S1, locator: "'Early life and works' (Pietà commission, 1498)"}], how_known: "The Pietà, 'today the most famous example' of its type, commissioned 1498 (P13); completion year not in the body read, so 0.5."}
  era_bucket: {value: "1400 to 1599", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "His whole life (1475–1564) falls in the bucket (P2)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Italy is Southern Europe in regions.csv (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "'Early life and works'"}], how_known: "Florence, Bologna, Rome."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [Italian], certainty: 0.7, cites: [{source: S2, locator: "notes (Italian originals)"}], how_known: "Poems and letters in Italian."}
  occupations: {value: ["sculptor", "painter", "architect", "poet"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["sculpture", "painting", "architecture"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Pietà (St. Peter's Basilica)", year: 1498, kind: work, lasting: "'today the most famous example' (S1)", certainty: 0.5, cites: [{source: S1, locator: "'Early life and works'"}], how_known: "Commission year."}
    - {value: "David", year: 1504, kind: work, lasting: "'the prime statement of the Renaissance ideal of perfect humanity' (S1)", certainty: 0.5, cites: [{source: S1, locator: "'Early life and works' (commission 1501; image caption 1501–04)"}], how_known: "End year from the caption (0.5)."}
    - {value: "Sistine Chapel frescoes", kind: work, lasting: "'probably the best known of Michelangelo's works' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "No year in the signed body read (P39)."}
  evidence_of_impact:
    - {value: "First Western artist whose biography was published in his lifetime (Vasari 1550; Condivi 1553)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "opening section"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father held occasional government posts; administrator of Caprese at the birth", role: father, certainty: 0.7, cites: [{source: S1, locator: "'Early life and works'"}], how_known: "Britannica."}
  household_circumstances: {value: "Minor Florentine nobility that had lost its patrimony and status", certainty: 0.7, cites: [{source: S1, locator: "'Early life and works'"}], how_known: "Britannica."}
  schooling:
    - {value: "Apprenticed to Domenico Ghirlandaio (left after one year)", stage: apprenticeship, run_by: private, ages: "13–14", certainty: 0.7, cites: [{source: S1, locator: "'Early life and works'"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Lorenzo de' Medici took him under his wing; Bertoldo di Giovanni 'the nearest... to a teacher of sculpture'", certainty: 0.7, cites: [{source: S1, locator: "'Early life and works'"}], how_known: "Britannica."}
  languages_in_childhood: {value: TODO}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1498–1504", certainty: 0.5, cites: [{source: S1, locator: "'Early life and works'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system:
    value: CHRIST
    basis: consistent_private_letters
    certainty: 0.5
    cites: [{source: S2, locator: "Sonnet LXV and note"}]
    rationale: "Turns from art to 'His great love on high, Whose arms to clasp us on the cross were spread' (Sonnet LXV, 1554): Christian devotion. One poem, so 0.5."
    how_known: "Poem sent with a letter to Vasari, in Symonds's rhymed translation (web copy)."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Chosen."}
    - {code: PLATO, reason: "Not chosen; the Neoplatonic reading of his earlier love poetry is not in the passages read."}
  lio_axes:
    A_locus:
      value: 0
      basis: consistent_private_letters
      certainty: 0.5
      cites: [{source: S2, locator: "Sonnet LXV"}]
      how_known: "One private poem in a rhymed translation; alternative named."
      rationale: "A personal God 'on high' who loves and redeems, before the 'final reckoning... Of good and evil for eternity'. Named alternative: 1. Rhymed translation may shift wording, so 0.5."
    B_cause: {value: UNKNOWN, how_known: "No statement on nature read (P16)."}
    C_ledger: {value: UNKNOWN, how_known: "The 'final reckoning... Of good and evil' in Sonnet LXV is in a rhymed translation of one poem; not scored."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "B is UNKNOWN; A at 0.5."}
  statements:
    - text: "Painting nor sculpture now can lull to rest / My soul that turns to His great love on high, / Whose arms to clasp us on the cross were spread."
      cites: [{source: S2, locator: "Sonnet LXV"}]
      date: "1554-09-19"
      context: "Sonnet sent to Giorgio Vasari with a letter dated 19 September 1554 (Symonds's note)."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "Symonds's rhymed English (1878) via Gutenberg #10314; the Italian is in Guasti's edition (not read). Web copy."
  changes_over_life: []
  coder_notes: "Coder's call; one late poem."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Florentine", certainty: 0.7, cites: [{source: S1, locator: "'Early life and works'"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1498–1504", certainty: 0.5, cites: [{source: S1, locator: "'Early life and works'"}], how_known: "First to last dated listed contribution (P29, P30); later works undated in the part read, so the end year is too early."}
  age_at_first_lasting_contribution: {value: 23, certainty: 0.5, cites: [{source: S1, locator: "opening; 'Early life and works'"}], how_known: "1498 − 1475 = 23 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "B is UNKNOWN."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "Sonnet LXV"}], how_known: "Nothing on nature read."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Poem is from 1554, after the listed period."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not read.", certainty: 0.5, cites: [{source: S1, locator: "'Early life and works'"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Early life and works'"}], how_known: "Not read."}
  circle_present: {value: "no", rationale: "Personal redeeming God; nothing on lawful order.", certainty: 0.5, cites: [{source: S2, locator: "Sonnet LXV"}], how_known: "Coder's reading."}
  reading: "Late Christian devotion."
  notes: ""

institutions:
  - {value: "Medici household of Lorenzo de' Medici", role: protégé, kind: "patron or funder", certainty: 0.7, cites: [{source: S1, locator: "'Early life and works'"}], how_known: "Britannica."}
collaborators:
  - {value: "Domenico Ghirlandaio", relation: teacher, certainty: 0.7, cites: [{source: S1, locator: "'Early life and works'"}], how_known: "Britannica."}
  - {value: "Giorgio Vasari", relation: correspondent, certainty: 0.7, cites: [{source: S2, locator: "note to Sonnet LXV"}, {source: S1, locator: "opening section"}], how_known: "Biographer (S1) and recipient of Sonnet LXV (S2)."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 59"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags: []
  open_questions:
    - "Read the rest of the Britannica body for later dates; read the Italian of Sonnet LXV."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Creighton E. Gilbert"
    citation: "Gilbert, Creighton E. \"Michelangelo.\" Encyclopaedia Britannica, updated 15 October 2026. https://www.britannica.com/biography/Michelangelo."
    url: "https://www.britannica.com/biography/Michelangelo"
    accessed: 2026-10-15
    reliability_note: "Signed body (opening and 'Early life and works'); Top Questions not cited."
    used_for: [identity, basics, contribution, childhood, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "scholarly edition"
    author: "Michelangelo Buonarroti; trans. John Addington Symonds"
    year: 1878
    citation: "The Sonnets of Michael Angelo Buonarroti and Tommaso Campanella. Trans. John Addington Symonds. 1878. Project Gutenberg eBook #10314."
    url: "https://www.gutenberg.org/ebooks/10314"
    accessed: 2026-10-15
    reliability_note: "Rhymed translation from Guasti's text of the autographs, unofficial web copy; §7 cap 0.7."
    used_for: [basics, worldview, timing, lane_b, collaborators]
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

# Michelangelo

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Michelangelo (1475–1564), Italian sculptor, painter and architect [S1]. Draft: primary_system CHRIST 0.5; A 0 at 0.5; B UNKNOWN; mid_basin BELOW_THRESHOLD. Not plotted.

## Life and work

Florence, Bologna, Rome [S1].

## Contribution and impact

Pietà, David, Sistine Chapel [S1].

## Childhood and education

Apprenticed to Ghirlandaio at 13 [S1].

## Adult working worldview

Sonnet LXV (1554): his soul 'turns to His great love on high' [S2].

## Heritage (context only)

Florentine [S1].

## Timing

First lasting contribution 1498, at 23 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle [S2].

## Open questions

- Later dates.

## Research log

- 2026-10-15: Read Britannica (Gilbert, opening and early works) and Symonds's Sonnet LXV with note (Gutenberg #10314).
