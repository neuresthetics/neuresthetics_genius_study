---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z4)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z4, order P32: F 3, rank 150). Basics from SEP (Christian Tornau, 2019, rev. 2024). Own words from City of God in Marcus Dods' translation (NPNF 1st ser. vol. 2) as reproduced on New Advent: XXI.8 (a portent 'happens not contrary to nature, but contrary to what we know as nature'; 'the will of so mighty a Creator is certainly the nature of each created thing') and XXII.8 ('even now miracles are wrought in the name of Christ'). Web copy of a translation, secondary quotation (Ibn Khaldun precedent). Not a scientist. Span 400–426 (Confessions ca. 396–400, latest year per P30 #4; City of God 412–426). primary_system CHRIST (0.7); A 0 (0.7, alt 1); B 2 (0.5, alt 1); C, E UNKNOWN; D BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Plotted (faded), left of B 3. Draft, not reviewed."}

identity:
  id: augustine-of-hippo
  display_name: "Augustine of Hippo"
  roster:
    canonical_name: "Augustine of Hippo"
    rank: 150
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Aurelius Augustinus", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Conventional Latin name; 'Aurelius' not in the section read, so 0.5."}
  native_name: {value: "Augustinus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  aliases:
    - {name: "Saint Augustine", kind: "title or honorific"}

basics:
  birth:
    date: {value: "0354-11-13", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP: 13 November 354."}
    place: {value: "Thagaste, Numidia", modern_name: "Souk Ahras, Algeria", polity_then: "Roman Empire", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
  death:
    date: {value: "0430-08-28", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
    place: {value: "Hippo Regius", modern_name: "Annaba, Algeria", polity_then: "Roman Empire", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP (bishop of Hippo; died during the Vandal siege)."}
  first_lasting_contribution_year: {value: 400, certainty: 0.5, cites: [{source: S1, locator: "§2 Works ('Confessiones (ca. 396–400)')"}], how_known: "Confessions dated ca. 396–400; latest year the source allows (P30 #4); range, so 0.5."}
  era_bucket: {value: "-500 to 499", certainty: 1.0, cites: [{source: S1, locator: "§2 Works"}], how_known: "400 (P2)."}
  region_of_birth: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "Algeria (P3; regions.csv)."}
  region_of_work: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "Hippo, bishop c. 396–430, covers the span."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Latin"], certainty: 0.7, cites: [{source: S1, locator: "§2 Works"}], how_known: "Latin titles."}
  occupations: {value: ["rhetor", "priest", "bishop of Hippo", "philosopher", "theologian"], certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}

contribution:
  fields: {value: ["philosophy", "theology"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  lasting_original_contributions:
    - {value: "Confessiones", year: 400, kind: work, lasting: "'probably his most original work'; 'greatly influenced the modern tradition of autobiography' (S1)", certainty: 0.5, cites: [{source: S1, locator: "opening; §2 Works"}], how_known: "SEP; dated ca. 396–400."}
    - {value: "De civitate dei", year: 426, kind: work, lasting: "one of the 'five long treatises' of wide scope (S1)", certainty: 0.7, cites: [{source: S1, locator: "§2 Works"}], how_known: "SEP: 412–426."}
  evidence_of_impact:
    - {value: "Often listed as the first medieval philosopher", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  major_works:
    - {value: "De trinitate", year: 419, kind: book, certainty: 0.5, cites: [{source: S1, locator: "§2 Works"}], how_known: "SEP: 399–419 (or 426)."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Foundational for medieval philosophy (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Mixed: mother Monnica a devout Christian; father Patricius baptized only on his deathbed", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
  family_religious_practice: {value: "Made a catechumen as a child", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
  parents_and_household:
    - {value: "Monnica, mother, devout Christian", role: mother, certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
    - {value: "Patricius, father", role: father, certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated in the section read."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["Latin"], certainty: 0.5, cites: [{source: S1, locator: "§1 Life"}], how_known: "Inferred."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "400–426", certainty: 0.5, cites: [{source: S1, locator: "§2 Works"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Catholic Church (bishop of Hippo)", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not scored."}
  primary_system:
    value: CHRIST
    basis: written_profession
    certainty: 0.7
    cites: [{source: S1, locator: "§1 Life"}, {source: S2, locator: "XXII.8"}]
    how_known: "Converted 386, baptized 387, bishop c. 396 (S1); City of God professes Christ throughout (S2). Web copy of a translation, so 0.7."
    rationale: "CHRIST: public written profession across the span."
  secondary_system: {value: UNKNOWN, how_known: "None scored (Neoplatonist influence is philosophical, not a second profession)."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Coded at 0.7."}
    - {code: PANENT, reason: "Rejected: SEP reports creation out of nothing (Conf. 12.6)."}
  lio_axes:
    A_locus:
      value: 0
      basis: written_profession
      certainty: 0.7
      cites: [{source: S2, locator: "XXI.8"}, {source: S1, locator: "creation section (Conf. 12.6)"}]
      how_known: "'the will of so mighty a Creator is certainly the nature of each created thing' (S2); creation out of nothing (S1). Translation web copy, 0.7."
      rationale: "A personal Creator distinct from creation. Alternative 1: nature identified with the Creator's will could be read as closer immanence."
      alternatives:
        - {value: 1, note: "Nature as God's will.", cites: [{source: S2, locator: "XXI.8"}]}
    B_cause:
      value: 2
      basis: written_profession
      certainty: 0.5
      cites: [{source: S2, locator: "XXI.8; XXII.8"}]
      how_known: "Translation web copy; contested reading, 0.5."
      rationale: "Account of nature (P6): a portent 'happens not contrary to nature, but contrary to what we know as nature' (XXI.8), yet miracles are live and recurring: 'even now miracles are wrought in the name of Christ, whether by His sacraments or by the prayers or relics of His saints' (XXII.8). Exceptions not limited, so B 2 (P27 anchor; Ibn Khaldun precedent). Alternative 1: nature is itself the Creator's will, every event His act."
      alternatives:
        - {value: 1, note: "Nature as the Creator's will.", cites: [{source: S2, locator: "XXI.8"}]}
    C_ledger: {value: UNKNOWN, how_known: "Eternal punishment (City of God XXI) not scored at this reading (coder's call)."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "SEP: 'committed to the truth of biblical revelation' yet 'surprisingly undogmatic'; no own passage on ranking authorities read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 0 (0.7) is ≤ 1, but B 2 at 0.5 is under the 0.7 bar and B 2 falls between the branches (§6, P19)."}
  statements:
    - text: "For how is that contrary to nature which happens by the will of God, since the will of so mighty a Creator is certainly the nature of each created thing? A portent, therefore, happens not contrary to nature, but contrary to what we know as nature."
      cites: [{source: S2, locator: "XXI.8"}]
      date: "426"
      context: "City of God XXI (books 412–426), Dods translation."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-19
      note: "Translation via a web copy; date is the work's completion year."
    - text: "For even now miracles are wrought in the name of Christ, whether by His sacraments or by the prayers or relics of His saints; but they are not so brilliant and conspicuous"
      cites: [{source: S2, locator: "XXII.8"}]
      date: "426"
      context: "City of God XXII, Dods translation."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-19
  changes_over_life:
    - {value: "Manichean 'hearer' c. 373 for nine years; conversion summer 386; baptism Easter 387", year: 386, certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP; before the span."}
  coder_notes: "B 2 vs 1 vs 3 is the ruling question."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Roman North African", certainty: 0.5, cites: [{source: S1, locator: "§1 Life"}], how_known: "Coder's summary."}
  religious_heritage_by_birth: {value: "Christian mother, pagan father", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
  baptism_or_initiation: {value: "Catechumen as a child; baptized Easter 387 by Ambrose in Milan", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "400–426", certainty: 0.5, cites: [{source: S1, locator: "§2 Works"}], how_known: "Confessions (ca. 396–400, P30 #4 latest year) to City of God (412–426) (P29, P30)."}
  age_at_first_lasting_contribution: {value: 46, certainty: 0.5, cites: [{source: S1, locator: "§1 Life; §2 Works"}], how_known: "400 − 354 = 46 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "Only City of God read."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "Not assessed."}
  worldview_during_major_work: {value: "CHRIST", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "Bishop throughout."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Philosophy and theology (S1).", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Church of Hippo", role: "priest (391), bishop (c. 396–430)", years: "391–430", kind: "religious body", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
collaborators:
  - {value: "Ambrose of Milan", relation: "influenced by", note: "baptized him", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 150"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Own words read in a 19th-century translation via a web copy."
  open_questions:
    - "Latin text of XXI.8; De Genesi ad litteram on rationes seminales for B."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Christian Tornau"
    citation: "Tornau, Christian. \"Saint Augustine.\" Stanford Encyclopedia of Philosophy (first published 25 September 2019; revised 26 April 2024). https://plato.stanford.edu/entries/augustine/"
    url: "https://plato.stanford.edu/entries/augustine/"
    accessed: 2026-10-19
    reliability_note: "Signed scholarly encyclopedia article."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Augustine of Hippo, tr. Marcus Dods"
    citation: "Augustine. The City of God, tr. Marcus Dods. Nicene and Post-Nicene Fathers, First Series, vol. 2 (1887), via New Advent. https://www.newadvent.org/fathers/1201.htm"
    url: "https://www.newadvent.org/fathers/1201.htm"
    accessed: 2026-10-19
    reliability_note: "Public-domain translation, web copy."
    used_for: [worldview]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [review]
---

## Summary

Augustine of Hippo (354–430), bishop and philosopher [S1]. Draft: CHRIST (0.7); A 0; B 2 (0.5, alt 1). Plotted (faded).

## Life and work

Thagaste, Carthage, Rome, Milan, Hippo [S1].

## Contribution and impact

Confessions; City of God [S1].

## Childhood and education

Christian mother, catechumen [S1].

## Adult working worldview

Creator whose will is nature; miracles continue [S2].

## Heritage (context only)

Roman North African [S1].

## Timing

400–426, age 46 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Latin of XXI.8.

## Research log

- 2026-10-19: Read SEP (Tornau); City of God XXI.8, XXII.8 (Dods).
