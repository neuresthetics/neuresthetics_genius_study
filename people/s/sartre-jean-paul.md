---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA2)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA2, order P32: F 3, rank 187). Basics from Britannica (Wilfrid Desan, signed; scholars edition, read in full) and SEP 'Jean-Paul Sartre' (Reynolds and Renaudie, rev. 2026). Lasting work: Nausea (1938; SEP 'highly influential'; Britannica 'a most original ... piece of work') and Being and Nothingness (1943; Britannica 'a philosopher of remarkable originality and depth'; SEP 'his most famous philosophical book', what 'remains alive'); span 1938–1943 by publication (P30 #1), age 33. Own words: the public lecture Existentialism Is a Humanism (given late 1945, published 1946), two years after the span (P20 cap 0.5), read in an unofficial web copy of Mairet's translation (marxists.org; 0.7 cap, §7): 'Atheistic existentialism, of which I am a representative ...'; 'we only mean to say that God does not exist'. primary_system EXIST 0.5 (written_profession, P20), alt ATHE, as for de Beauvoir (systems/EXIST.md does not split atheist from theist existentialism); A 4 at 0.5, alt BELOW_THRESHOLD; not a scientist, B UNKNOWN; C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD (P10). Not plotted (B UNKNOWN). Draft, not reviewed."}

identity:
  id: sartre-jean-paul
  display_name: "Jean-Paul Sartre"
  roster:
    canonical_name: "Jean-Paul Sartre"
    rank: 187
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: "core"
    field: "philosophy"
    field_bucket: "philosophy"
  full_name: {value: "Jean-Paul Sartre", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica (no fuller form given)."}
  native_name: {value: "Jean-Paul Sartre", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  aliases:
    - {name: "Sartre-Jean-Paul", kind: "roster alias"}

basics:
  birth:
    date: {value: "1905-06-21", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "Paris", modern_name: "Paris, France", polity_then: "France", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  death:
    date: {value: "1980-04-15", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "Paris", modern_name: "Paris, France", polity_then: "France", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1938, certainty: 0.7, cites: [{source: S1, locator: "Early life and writings"}, {source: S2, locator: "opening"}], how_known: "Nausea, published 1938 (S1); called 'highly influential' (S2); publication (P30 #1)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "Early life and writings"}], how_known: "1938–1943 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "France (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Early life and writings"}], how_known: "Le Havre, Laon, Paris."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["French"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "French titles."}
  occupations: {value: ["philosopher", "novelist", "playwright"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

contribution:
  fields: {value: ["philosophy", "literature"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "La Nausée (Nausea)", year: 1938, kind: "work", lasting: "'highly influential works of literature ... like Nausea (1938)' (S2); 'a most original, fiercely individualistic ... piece of work' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Early life and writings"}, {source: S2, locator: "opening"}], how_known: "Britannica and SEP; published 1938."}
    - {value: "L’Être et le néant (Being and Nothingness)", year: 1943, kind: "work", lasting: "'it was above all in ... (1943; Being and Nothingness) that Sartre revealed himself as a philosopher of remarkable originality and depth' (S1); 'what remains alive ... his most famous philosophical book' (S2)", certainty: 0.7, cites: [{source: S1, locator: "Early life and writings"}, {source: S2, locator: "opening"}], how_known: "Britannica and SEP; published 1943."}
  evidence_of_impact:
    - {value: "Awarded (and declined) the 1964 Nobel Prize for Literature", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  major_works:
    - {value: "Existentialism Is a Humanism (public lecture)", year: 1945, kind: "lecture series", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "SEP: given 'towards the end of 1945'; published 1946."}
    - {value: "Critique of Dialectical Reason, vol. 1", year: 1960, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "Political activities"}], how_known: "Britannica: 'a major work'; not called lasting."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "The leading exponent of existentialism in the 20th century (S1).", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Father died early; raised in the home of his maternal grandfather Carl Schweitzer", role: "family", certainty: 0.7, cites: [{source: S1, locator: "Early life and writings"}], how_known: "Britannica."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Lycée Henri IV; École Normale Supérieure (graduated 1929)", certainty: 0.7, cites: [{source: S1, locator: "Early life and writings"}], how_known: "Britannica."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1938–1943", certainty: 0.7, cites: [{source: S1, locator: "Early life and writings"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: 
    value: EXIST
    basis: written_profession
    certainty: 0.5
    cites: [{source: S3, locator: "para. on 'atheistic existentialism'"}]
    how_known: "His own public lecture (late 1945, published 1946), two years after the span, so capped at 0.5 (P20); read in an unofficial web copy (0.7 cap, §7)."
    rationale: "'Atheistic existentialism, of which I am a representative' (S3). Named alternative ATHE: 'we only mean to say that God does not exist' (S3); systems/EXIST.md does not split atheist from theist existentialism, so ATHE stays the alternative, as for de Beauvoir."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: EXIST, reason: "Coded at 0.5: self-described atheistic existentialist."}
    - {code: ATHE, reason: "Named alternative: 'God does not exist'."}
  lio_axes:
    A_locus: 
      value: 4
      basis: written_profession
      certainty: 0.5
      cites: [{source: S3, locator: "para. on 'abandonment'"}]
      how_known: "His own published lecture, after the span (P20 cap 0.5); unofficial web copy."
      rationale: "'God does not exist, and ... it is necessary to draw the consequences of his absence right to the end' (S3): no God, so 4. Alternative BELOW_THRESHOLD: 'even if God existed that would make no difference from its point of view' (S3) sets the question aside."
      alternatives:
        - {value: BELOW_THRESHOLD, note: "'Even if God existed that would make no difference' (S3).", cites: [{source: S3, locator: "closing paragraph"}]}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); no statement on nature read."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Lead: man 'is nothing else but what he makes of himself' (S3); not scored."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "BELOW_THRESHOLD, not UNKNOWN: the A ≥ 3 branch reads A only (P10), and A 4 is scored only at 0.5."}
  statements:
    - text: "Atheistic existentialism, of which I am a representative, declares with greater consistency that if God does not exist there is at least one being whose existence comes before its essence, a being which exists before it can be defined by any conception of it."
      cites: [{source: S3, locator: "para. on 'atheistic existentialism'"}]
      date: "1945"
      context: "Public lecture Existentialism Is a Humanism, Paris, late 1945 (S2), published 1946; after the span."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-19
      note: "Mairet's translation (in Kaufmann, ed., 1956/1989) as posted at marxists.org; not checked against the Nagel 1946 text or the Yale 2007 edition (0.7 cap, §7)."
    - text: "And when we speak of “abandonment” – a favorite word of Heidegger – we only mean to say that God does not exist, and that it is necessary to draw the consequences of his absence right to the end."
      cites: [{source: S3, locator: "para. on 'abandonment'"}]
      date: "1945"
      context: "Same lecture."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-19
      note: "As above."
  changes_over_life: []
  coder_notes: "Read Being and Nothingness (1943) on God as the impossible in-itself-for-itself, inside the span, and Les Mots (1963) on his loss of faith; check the lecture against the Yale edition."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated in the sources read."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1938–1943", certainty: 0.7, cites: [{source: S1, locator: "Early life and writings"}], how_known: "Nausea (1938) to Being and Nothingness (1943), the listed lasting works (P29, P30 #1)."}
  age_at_first_lasting_contribution: {value: 33, certainty: 0.7, cites: [{source: S1, locator: "Introduction; Early life and writings"}], how_known: "1938 − 1905 = 33 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Phenomenological description, not geometric argument (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions: []
collaborators:
  - {value: "Simone de Beauvoir", relation: "collaborator", note: "lifelong partner; co-founded Les Temps Modernes", certainty: 0.7, cites: [{source: S1, locator: "Early life and writings; Post-World War II work"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 187"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Profession after the span, in a web copy."
  open_questions:
    - "Being and Nothingness on God (inside the span)."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Wilfrid Desan"
    citation: "Desan, Wilfrid. 'Jean-Paul Sartre.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/Jean-Paul-Sartre/65811"
    url: "https://kids.britannica.com/scholars/article/Jean-Paul-Sartre/65811"
    accessed: 2026-10-19
    reliability_note: "Signed article, read in full."
    used_for: [identity, basics, contribution, childhood, timing, collaborators]
  - id: S2
    type: secondary
    kind: "encyclopedia"
    author: "Jack Reynolds and Pierre-Jean Renaudie"
    citation: "Reynolds, Jack, and Pierre-Jean Renaudie. 'Jean-Paul Sartre.' Stanford Encyclopedia of Philosophy (rev. 10 July 2026). https://plato.stanford.edu/entries/sartre/"
    url: "https://plato.stanford.edu/entries/sartre/"
    accessed: 2026-10-19
    reliability_note: "Signed scholarly reference article."
    used_for: [basics, contribution, worldview]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Jean-Paul Sartre (trans. Philip Mairet)"
    citation: "Sartre, Jean-Paul. Existentialism Is a Humanism (lecture 1945; Paris: Nagel, 1946), trans. Philip Mairet, in Walter Kaufmann, ed., Existentialism from Dostoyevsky to Sartre (Meridian, 1989); web copy at marxists.org. https://www.marxists.org/reference/archive/sartre/works/exist/sartre.htm"
    url: "https://www.marxists.org/reference/archive/sartre/works/exist/sartre.htm"
    accessed: 2026-10-19
    reliability_note: "Unofficial web copy of a published translation (0.7 cap, §7)."
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

Jean-Paul Sartre (1905–1980), philosopher and writer [S1]. Draft: EXIST (0.5, alt ATHE); A 4 at 0.5; B UNKNOWN. Not plotted.

## Life and work

Paris; Le Havre [S1].

## Contribution and impact

Nausea (1938); Being and Nothingness (1943) [S1, S2].

## Childhood and education

Lycée Henri IV; ENS [S1].

## Adult working worldview

'Atheistic existentialism, of which I am a representative' (1945) [S3].

## Heritage (context only)

Not stated.

## Timing

1938–1943, age 33 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Being and Nothingness on God.

## Research log

- 2026-10-19: Read Britannica (Desan); SEP; the 1945 lecture (web copy).
