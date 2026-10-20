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
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA1, order P32: F 3, rank 178). Basics from Britannica (Roy Donald McMullen, signed; body). Lasting work and dating from the Met's Heilbrunn essay 'Henri Matisse (1869–1954)' (body, seen as a search excerpt): Woman with a Hat, 'when exhibited at the 1905 Salon d'Automne', gave rise to Fauvism; public exhibition is the P30 #1 dating event (RQ-Z7-N1). Own words: Jazz (published 30 September 1947), after the span, in Jack Flam's translation (web copy of Matisse on Art): 'Do I believe in God? Yes, when I work ... I feel no gratitude toward Him'. Conditional, work-bound belief with refused acknowledgement, so primary_system BELOW_THRESHOLD (leads CHRIST: Vence chapel, not read; PANT not supported); A BELOW_THRESHOLD; not a scientist, B UNKNOWN; C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Span 1905, age 36 (1905 − 1869). Not plotted. Draft, not reviewed."}

identity:
  id: matisse-henri
  display_name: "Henri Matisse"
  roster:
    canonical_name: "Henri Matisse"
    rank: 178
    F: 3
    models: [Claude, Gemini, GPT]
    band: "core (3–4)"
    status: "core"
    field: "art"
    field_bucket: "arts"
  full_name: {value: "Henri-Émile-Benoît Matisse", certainty: 0.7, cites: [{source: S1, locator: "heading"}], how_known: "Britannica."}
  native_name: {value: "Henri Matisse", certainty: 0.7, cites: [{source: S1, locator: "heading"}], how_known: "Britannica."}
  aliases:
    - {name: "Matisse-Henri", kind: "roster alias"}

basics:
  birth:
    date: {value: "1869-12-31", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Le Cateau, Picardy", modern_name: "Le Cateau-Cambrésis, France", polity_then: "France", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1954-11-03", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Nice", modern_name: "Nice, France", polity_then: "France", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1905, certainty: 0.7, cites: [{source: S2, locator: "Fauvist period"}], how_known: "Woman with a Hat exhibited at the 1905 Salon d'Automne, which 'gave rise to the first of the avant-garde movements ... named \"Fauvism\"' (S2); public exhibition dates artworks (P30 #1, RQ-Z7-N1)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S2, locator: "Fauvist period"}], how_known: "1905 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "France (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Formative years"}], how_known: "Paris; later Nice."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["French"], certainty: 0.7, cites: [{source: S3, locator: "Jazz text"}], how_known: "French text."}
  occupations: {value: ["painter", "sculptor", "printmaker"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["painting"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Fauvism (Woman with a Hat)", year: 1905, kind: "work", lasting: "'leader of the Fauvist movement' (S1, body); Woman with a Hat 'gave rise to the first of the avant-garde movements' (S2, body)", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Fauvist period"}], how_known: "Britannica and the Met essay; dated by the 1905 Salon d'Automne showing (S2)."}
  evidence_of_impact:
    - {value: "Often regarded as the most important French painter of the 20th century", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Le Bonheur de vivre", year: 1906, kind: "artwork", certainty: 0.5, cites: [{source: S2, locator: "Fauvist period"}], how_known: "Met: 1905–6; shown at the 1906 Salon des Indépendants (not in the source read); not called lasting."}
    - {value: "Jazz", year: 1947, kind: "book", certainty: 0.7, cites: [{source: S3, locator: "introduction"}], how_known: "Published 30 September 1947 (Flam)."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Most important French painter of the 20th century (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

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
  working_years: {value: "1905", certainty: 0.7, cites: [{source: S2, locator: "Fauvist period"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "Jazz (1947, after the span; P20): 'Do I believe in God? Yes, when I work' and a 'someone who makes me do things that surpass myself', yet 'I feel no gratitude toward Him'. Belief tied to working moods, with no doctrine, so BELOW_THRESHOLD. Leads: CHRIST (the Vence Chapel of the Rosary, 1948–51, not read; 'communicant approaching the Lord's Table' is a simile); PANT fails part 1 (no God-Nature identity)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Lead: Vence chapel (not read); Christian imagery in Jazz."}
    - {code: AGNOS, reason: "Lead: belief only 'when I work'."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "A helper 'who makes me do things that surpass myself' suggests an agent beyond him, but the belief is conditional and the text is after the span; no locus stated."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); no statement on nature read."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied."}
  statements:
    - text: "Do I believe in God? Yes, when I work. When I am submissive and modest. I sense myself helped immensely by someone who makes me do things that surpass myself. Still, I feel no gratitude toward Him because it is as if I were watching a conjurer whose tricks I cannot see through."
      cites: [{source: S3, locator: "Jazz, 'Do I believe in God?'"}]
      date: "1947"
      context: "Jazz (Tériade, 1947), his handwritten text; after the span."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-19
      note: "Jack Flam's translation (Matisse on Art) as posted by Private Print; French original quoted in web copies: 'Si je crois en Dieu? Oui, quand je travaille.' Not checked against the 1947 printing or Flam's book (0.7 cap, §7)."
  changes_over_life: []
  coder_notes: "Read the Vence chapel texts (1951 letter to the bishop of Nice; Chapelle du Rosaire statements) and Flam's notes; the Répertoire variant ('the divine pilot is not with me', Schneider 1984, p. 710 n. 35) is a lead."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated in the source read."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1905", certainty: 0.7, cites: [{source: S2, locator: "Fauvist period"}], how_known: "The 1905 Salon d'Automne showing, the one supported lasting work (P29, P30 #1)."}
  age_at_first_lasting_contribution: {value: 36, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "1905 − 1869 = 36 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Expressive colour (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions: []
collaborators:
  - {value: "Gustave Moreau", relation: "teacher", note: "atelier, École des Beaux-Arts", certainty: 0.7, cites: [{source: S1, locator: "Formative years"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 178"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Only one religious text read, after the span, in a web copy."
  open_questions:
    - "Vence chapel texts."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Roy Donald McMullen"
    citation: "McMullen, Roy Donald. 'Henri Matisse.' Encyclopaedia Britannica (rev. 28 August 2026). https://www.britannica.com/biography/Henri-Matisse"
    url: "https://www.britannica.com/biography/Henri-Matisse"
    accessed: 2026-10-19
    reliability_note: "Signed article; body cited, question boxes not used (P26)."
    used_for: [identity, basics, contribution, childhood, lane_b, collaborators]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "The Metropolitan Museum of Art (Heilbrunn Timeline of Art History)"
    citation: "'Henri Matisse (1869–1954).' Heilbrunn Timeline of Art History, The Metropolitan Museum of Art. https://www.metmuseum.org/essays/henri-matisse-1869-1954"
    url: "https://www.metmuseum.org/essays/henri-matisse-1869-1954"
    accessed: 2026-10-19
    reliability_note: "Museum reference essay body, seen as a search excerpt; author not recorded."
    used_for: [basics, contribution, timing]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Henri Matisse (trans. Jack Flam)"
    citation: "Matisse, Henri. Jazz (Paris: Tériade, 1947), text in Jack Flam, Matisse on Art; web copy at Private Print (2019). https://privateprint.mk/en/blog/dzhez"
    url: "https://privateprint.mk/en/blog/dzhez"
    accessed: 2026-10-19
    reliability_note: "Unofficial web copy of Flam's translation with notes (0.7 cap, §7)."
    used_for: [worldview]
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

Henri Matisse (1869–1954), painter [S1]. Draft: BELOW_THRESHOLD (leads CHRIST, AGNOS). Not plotted.

## Life and work

Paris; Nice [S1].

## Contribution and impact

Fauvism, 1905 [S1, S2].

## Childhood and education

Saint-Quentin; law clerk [S1].

## Adult working worldview

'Do I believe in God? Yes, when I work' (1947) [S3].

## Heritage (context only)

Not stated.

## Timing

1905, age 36 [S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Vence chapel.

## Research log

- 2026-10-19: Read Britannica (McMullen); Met essay excerpt; Jazz text (Flam).
