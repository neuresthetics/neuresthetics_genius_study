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
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch D, order P32: F 5, rank 19). Basics and works from Britannica (Seitz), first part of the article only. No statement of his on religion, God or nature's order was read. Not a scientist. primary_system UNKNOWN; all axes UNKNOWN; mid_basin UNKNOWN. Draft, not reviewed."}

identity:
  id: monet-claude
  display_name: "Claude Monet"
  roster:
    canonical_name: "Claude Monet"
    rank: 19
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: art
    field_bucket: arts
  full_name: {value: "Oscar-Claude Monet", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts ('In full')"}], how_known: "Britannica alone."}
  native_name: {value: TODO}
  aliases:
    - {name: "Claude-Monet", kind: "roster alias"}
    - {name: "Monet-Claude", kind: "roster alias"}

basics:
  birth:
    date: {value: "1840-11-14", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts; opening sentence"}], how_known: "Britannica alone."}
    place: {value: "Paris", modern_name: "Paris, France", polity_then: "Kingdom of France (July Monarchy)", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Britannica alone."}
  death:
    date: {value: "1926-12-05", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Britannica alone."}
    place: {value: "Giverny", modern_name: "Giverny, France", polity_then: "French Third Republic", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Britannica alone."}
  first_lasting_contribution_year: {value: 1865, certainty: 0.5, cites: [{source: S1, locator: "Early work ('In the beach and sea pictures of 1865–67, Monet was [...] attempting to record on the spot the impression')"}], how_known: "Start year of the range Britannica gives for the pictures that show his advance toward the Impressionist style (P12). Dated by painting years, not by first public showing, which the part read does not give (P30), so 0.5; the coder's choice of these pictures as the first lasting item is an inference (P24)."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "Early work"}], how_known: "Every candidate year (1865–1874) is in this bucket (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "France (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening; Early work"}], how_known: "Paris, Normandy, Giverny."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [French], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's inference; a painter."}
  occupations: {value: ["painter"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["painting"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Impressionist method: recording on the spot the impression of a momentary view, in broken touches", year: "1865–67", kind: method, lasting: "he was 'the initiator, leader, and unswerving advocate of the Impressionist style' (S1)", certainty: 0.5, cites: [{source: S1, locator: "opening; Early work"}], how_known: "Britannica; the start year is the range Britannica gives for the pictures that show the advance (inference, 0.5)."}
    - {value: "Series painting: repeated studies of one motif under changing light (stacks of wheat, Rouen Cathedral)", year: "1890–1894", kind: method, lasting: "exhibited in groups; a model for later serial art", certainty: 0.7, cites: [{source: S1, locator: "opening ('stacks of wheat (1890/91 [...]) and the Rouen Cathedral (1894)')"}], how_known: "Britannica."}
    - {value: "Water-lily paintings from his pond at Giverny, his last series", year: "before 1926", kind: "body of work", lasting: "his last series", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; the part read does not date the series, so the end is the death cap (P30)."}
  evidence_of_impact: []
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Initiator of Impressionism.", certainty: 0.7, cites: [{source: S1, locator: "opening sentence"}], how_known: "Britannica signed body."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Eldest son of Adolphe Monet, a grocer; family moved near Le Havre when he was five", name: "Adolphe Monet", role: father, certainty: 0.7, cites: [{source: S1, locator: "Childhood section"}], how_known: "Britannica."}
  household_circumstances: {value: "Father managed the family grocery and ship-chandlering business near Le Havre", certainty: 0.7, cites: [{source: S1, locator: "Childhood section"}], how_known: "Britannica."}
  schooling:
    - {value: "Drawing lessons with a local artist; later the Académie Suisse and Gleyre's atelier in Paris", stage: other, certainty: 0.7, cites: [{source: S1, locator: "Childhood section; Early work"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Eugène Boudin, who introduced him to painting in the open air", certainty: 0.7, cites: [{source: S1, locator: "Childhood section"}], how_known: "Britannica."}
  languages_in_childhood: {value: TODO}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1865–1926", certainty: 0.5, cites: [{source: S1, locator: "Early work; opening"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing of his on religion in the part of Britannica read; a web search found only unsourced quotation sites."}
  primary_system: {value: UNKNOWN, cites: [{source: S1, locator: "sections read"}], how_known: "No statement of his on religion or God in the sources read (P19).", note: "Lead: Wildenstein's catalogue raisonné (letters); Clemenceau's memoir is reported speech."}
  secondary_system: {value: UNKNOWN, how_known: "No system evidence."}
  candidate_codes_considered: []
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing in the sources read (P19)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); no statement of his about nature's order read (P16)."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing in the sources read."}
    D_authority: {value: UNKNOWN, how_known: "Nothing in the sources read."}
    E_scope: {value: UNKNOWN, how_known: "Nothing in the sources read."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus and B_cause are UNKNOWN (§6, P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Only the first sections of the Britannica article were read (the fetch returned the article through 'Early work'). Britannica's question boxes at the top of the article may be AI-generated and are not cited (P26)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "French", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1865–1926", certainty: 0.5, cites: [{source: S1, locator: "Early work; opening"}], how_known: "First listed item (1865, start of 1865–67) to the water lilies, whose end is the death cap 1926 (P29, P30); 0.5 because both ends are inferred."}
  age_at_first_lasting_contribution: {value: 25, certainty: 0.5, cites: [{source: S1, locator: "Quick Facts; Early work"}], how_known: "1865 − 1840 = 25 (P30); takes the 0.5 of the year."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement read."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "Nothing read.", certainty: 0.5, cites: [{source: S1, locator: "sections read"}], how_known: "Absence in the source read."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Nothing read.", certainty: 0.5, cites: [{source: S1, locator: "Childhood section"}], how_known: "No evidence."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "Childhood section"}], how_known: "No evidence."}
  circle_present: {value: "unclear", rationale: "Nothing read.", certainty: 0.5, cites: [{source: S1, locator: "sections read"}], how_known: "No evidence."}
  reading: "As belief, not finding: unclear. Does not test H1."
  notes: ""

institutions: []
collaborators:
  - {value: "Eugène Boudin", relation: teacher, certainty: 0.7, cites: [{source: S1, locator: "Childhood section"}], how_known: "Britannica."}
  - {value: "Frédéric Bazille, Alfred Sisley and Pierre-Auguste Renoir", relation: collaborator, note: "met in Gleyre's atelier", certainty: 0.7, cites: [{source: S1, locator: "Childhood section"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 19"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Only the first part of the Britannica article was read; Impression, Sunrise and the 1874 exhibition are not in the part read, so the first public showing is not dated."
  open_questions:
    - "Read the rest of Britannica and a museum source (Musée d'Orsay, Met) to date the first public showing; search his letters for any statement on religion or nature."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "William C. Seitz"
    citation: "Seitz, William C. \"Claude Monet.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Claude-Monet."
    url: "https://www.britannica.com/biography/Claude-Monet"
    accessed: 2026-10-15
    reliability_note: "Signed encyclopedia article; read through the 'Early work' section."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, collaborators]
  - id: S2
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Claude Monet

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Claude Monet (1840–1926), French painter, initiator and leader of Impressionism, known for series paintings of one motif under changing light and for the water lilies of Giverny [S1]. No statement of his on religion, God or nature's order was read. Draft: primary_system UNKNOWN; all axes UNKNOWN; mid_basin UNKNOWN.

## Life and work

Childhood near Le Havre; Boudin; Paris (Académie Suisse, Gleyre); Giverny [S1].

## Contribution and impact

Impressionist method; series; water lilies [S1].

## Childhood and education

Son of a grocer; drawing lessons; Boudin [S1].

## Adult working worldview

Not established.

## Heritage (context only)

French [S1].

## Timing

First lasting item 1865 (0.5), at 25.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Unclear.

## Open questions

- Rest of Britannica; letters.

## Research log

- 2026-10-15: Read Britannica (Seitz) through 'Early work'. The Met essay fetch timed out.
