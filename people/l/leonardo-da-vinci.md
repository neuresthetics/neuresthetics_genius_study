---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch H)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-15
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch H, order P32: F 5, rank 51). Basics from Britannica (Heydenreich). Worldview from the notebooks (Richter's English edition, 1888, Gutenberg #5000; private manuscript in a web-copy translation, 0.7 cap). Scientist under P30 (anatomy, mechanics; S1). primary_system BELOW_THRESHOLD (candidates CHRIST, DEISM); A 0 at 0.5 (alt 1); B 3 at 0.5 (alt 4) — No. 1134 says no force fails of its necessary results, but No. 1132 prays to a Lord who 'canst shorten or prolong the lives of men' (RQ2 batch H); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Plotted (faded). Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Batch H audit (cae9cb2, run 1: hold): RQ2 resolved, B stays 3 at 0.5 (alternative 4); reasoning recorded in coder_notes. No value changes."}

identity:
  id: leonardo-da-vinci
  display_name: "Leonardo da Vinci"
  roster:
    canonical_name: "Leonardo da Vinci"
    rank: 51
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: polymath
    field_bucket: polymath
  full_name: {value: "Leonardo da Vinci", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  native_name: {value: UNKNOWN, how_known: "Italian, same Latin-script form."}
  aliases: []

basics:
  birth:
    date: {value: "1452-04-15", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; before 1582, so Julian."}
    place: {value: "Anchiano, near Vinci, Republic of Florence", modern_name: "Anchiano, Vinci, Italy", polity_then: "Republic of Florence", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1519-05-02", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; Julian."}
    place: {value: "Cloux (now Clos-Lucé), near Amboise, France", modern_name: "Clos-Lucé, Amboise, France", polity_then: "Kingdom of France", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Later life in France'"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1498, certainty: 0.5, cites: [{source: S1, locator: "'Last Supper'"}], how_known: "Last Supper (1495–98), 'one of the most famous artworks in the world'; completion year used (P13). Earlier works (Ginevra de' Benci c. 1474/78, Benois Madonna 1478–80, Vitruvian Man c. 1490) could count, so 0.5."}
  era_bucket: {value: "1400 to 1599", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "His whole adult life (1470–1519) falls in the bucket (P2)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Italy is Southern Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "Florentine, Milanese and Roman periods"}], how_known: "Florence, Milan, Rome until 1516."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [Italian], certainty: 0.7, cites: [{source: S1, locator: "'Starting the notebooks' (scientific prose in the Italian vernacular)"}], how_known: "Britannica."}
  occupations: {value: ["painter", "draftsman", "sculptor", "architect", "engineer"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["painting", "anatomy", "mechanics", "engineering"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Anatomical studies and drawings'; 'Mechanics and cosmology'"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Last Supper", year: 1498, kind: work, lasting: "'one of the most famous artworks in the world' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Last Supper'"}], how_known: "Britannica: 1495–98."}
    - {value: "Mona Lisa", year: 1519, kind: work, lasting: "'set the standard for all future portraits' (S1)", certainty: 0.5, cites: [{source: S1, locator: "'Mona Lisa'"}], how_known: "Britannica: 1503–19; end year used, 0.5."}
    - {value: "Anatomical drawings", kind: work, lasting: "'among the most significant achievements of Renaissance science' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Anatomical studies and drawings'"}], how_known: "Britannica; kept private and unpublished in his lifetime, undated as a body (P39)."}
  evidence_of_impact:
    - {value: "Last Supper influenced Rubens and Rembrandt; anatomical drawings 'forged the basic principles of modern scientific illustration'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "'Last Supper'; 'Anatomical studies and drawings'"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father Ser Piero da Vinci, Florentine notary; mother possibly Caterina di Meo Lippi; parents unmarried", role: parents, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  household_circumstances: {value: "Grew up on his father's family estate, treated as a 'legitimate' son", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  schooling:
    - {value: "Usual elementary education: reading, writing, arithmetic", stage: "elementary school", run_by: other, certainty: 0.5, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica; provider not named."}
    - {value: "Apprenticed to Andrea del Verrocchio", stage: apprenticeship, run_by: private, ages: "about 15–", certainty: 0.7, cites: [{source: S1, locator: "'Apprenticeships'"}], how_known: "Britannica."}
  early_mathematics: {value: "arithmetic only", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1498–1519", certainty: 0.5, cites: [{source: S1, locator: "'Last Supper'; 'Mona Lisa'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system:
    value: BELOW_THRESHOLD
    basis: consistent_private_letters
    certainty: 0.5
    cites: [{source: S2, locator: "Nos. 1132–1135, 1208, 1210"}]
    rationale: "Prayers to a Lord and God (Nos. 1132–1133); God as 'first Mover' who lets no force fail of its necessary results (No. 1134); 'false miracles' denounced (No. 1208); 'the mind of God in which the universe is included' (No. 1210). Too thin for a system: CHRIST (prayers, sacred commissions) and DEISM (first Mover, necessity; but no rejection of revelation, P27) both fit. Britannica notes that debate continues over his religious beliefs (S1)."
    how_known: "Private notebooks in a web-copy translation; the dating and order of the notes are not given in the passages read."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Prayers to 'Lord' and 'God'; but nothing distinctively Christian in the notes read."}
    - {code: DEISM, reason: "'first Mover'; necessity as 'the eternal curb and law of nature'; no rejection of revelation stated (P27)."}
  lio_axes:
    A_locus:
      value: 0
      basis: consistent_private_letters
      certainty: 0.5
      cites: [{source: S2, locator: "Nos. 1132–1134"}]
      how_known: "Private notebooks (no single document is a public profession), web copy; alternative named."
      rationale: "A personal God outside the world, addressed in prayer as 'Thee Lord' who 'canst shorten or prolong the lives of men' and as 'Thou first Mover'. Named alternative: 1, since 'the mind of God in which the universe is included' (No. 1210) points to a God containing the world. Only a few short notes, so 0.5."
    B_cause:
      value: 3
      basis: consistent_private_letters
      certainty: 0.5
      cites: [{source: S2, locator: "Nos. 1134, 1135, 1208"}]
      how_known: "Private notebooks, web copy, 0.5."
      rationale: "Nature runs by necessity: God 'hast not permitted that any force should fail of the order or quality of its necessary results' (No. 1134); 'Necessity is ... the eternal curb and law of nature' (No. 1135); 'false miracles' are a trade in delusion (No. 1208). No. 1134 is close to a stated exceptionless necessity (P40, B 4), but No. 1132 credits the Lord with power to 'shorten or prolong the lives of men', a possible exception, and No. 1208 condemns false miracles without denying true ones. Also B 3 at 0.5 by P35 for a scientist. Named alternative: 4. Kept after the batch H audit (RQ2); see coder_notes."
    C_ledger: {value: UNKNOWN, how_known: "'Thou, O God, dost sell us all good things at the price of labour' (No. 1133) is about effort, not reward by God for conduct; not scored."}
    D_authority: {value: UNKNOWN, how_known: "Britannica says he 'scorned speculative book knowledge' in favour of experience (S1), but nothing read sets revelation against observation."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 0 and B 3 would satisfy A ≤ 1 and B ≥ 3, but both are at 0.5, below the 0.7 bar (§6, P19)."}
  statements:
    - text: "I obey Thee Lord, first for the love I ought, in all reason to bear Thee; secondly for that Thou canst shorten or prolong the lives of men."
      cites: [{source: S2, locator: "No. 1132"}]
      axes: [A_locus, B_cause]
      kind: "notebook or diary"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "Richter's English (1888) via Gutenberg #5000; web copy; manuscript source and date not given in the passage read (P39)."
    - text: "O admirable impartiality of Thine, Thou first Mover; Thou hast not permitted that any force should fail of the order or quality of its necessary results."
      cites: [{source: S2, locator: "No. 1134"}]
      axes: [A_locus, B_cause]
      kind: "notebook or diary"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "As above."
    - text: "Necessity is the mistress and guide of nature. Necessity is the theme and the inventress, the eternal curb and law of nature."
      cites: [{source: S2, locator: "No. 1135"}]
      axes: [B_cause]
      kind: "notebook or diary"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "As above."
    - text: "And many have made a trade of delusions and false miracles, deceiving the stupid multitude."
      cites: [{source: S2, locator: "No. 1208"}]
      axes: [B_cause]
      kind: "notebook or diary"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "As above."
  changes_over_life: []
  coder_notes: "Coder's call. Richter introduces these notes as showing 'a broad spirit of naturalism' (S2, editor's note) — an editor's reading, not scored. Batch H audit RQ2 (2026-10-15): B stays 3 at 0.5, alternative 4. Reasons: No. 1134 is addressed to God as guarantor ('Thou hast not permitted') and says forces do not fail, short of the explicit no-exception, no-chance statement P40 requires; No. 1132 credits God with a live power to 'shorten or prolong the lives of men'; No. 1208 condemns false miracles only; and P35 caps inference from a scientist's work at B 3 at 0.5. B 4 would need No. 1132 read as conventional piety, which the sources read do not support."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Tuscan (Florentine notary family)", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1498–1519", certainty: 0.5, cites: [{source: S1, locator: "'Last Supper'; 'Mona Lisa'"}], how_known: "First to last dated listed lasting contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 46, certainty: 0.5, cites: [{source: S1, locator: "opening; 'Last Supper'"}], how_known: "1498 − 1452 = 46 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "The notes read are undated (P39)."}
  lio_views_relative_to_major_work: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "Nos. 1134–1135"}], how_known: "Notes undated."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Notes undated."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Vitruvian Man imposes 'the principles of geometry' on the body; studied higher mathematics from 30.", certainty: 0.5, cites: [{source: S1, locator: "'Vitruvian Man'; 'Early life'"}], how_known: "Coder's reading."}
  form_acquired: {value: "adulthood, before major work", certainty: 0.5, cites: [{source: S1, locator: "'Early life'"}], how_known: "From age 30."}
  circle_present: {value: "unclear", rationale: "First Mover with necessary laws, but a God who can prolong lives.", certainty: 0.5, cites: [{source: S2, locator: "Nos. 1132–1135"}], how_known: "Coder's reading."}
  reading: "Necessity as the law of nature under a first Mover, held alongside prayer."
  notes: ""

institutions:
  - {value: "Court of Ludovico Sforza, Milan", role: "painter and engineer of the duke", years: "1482–1499", kind: "patron or funder", certainty: 0.7, cites: [{source: S1, locator: "'First Milanese period'"}], how_known: "Britannica."}
  - {value: "Francis I of France", role: "First painter, architect and engineer to the King", years: "1516–1519", kind: "patron or funder", certainty: 0.7, cites: [{source: S1, locator: "'Later life in France'"}], how_known: "Britannica."}
collaborators:
  - {value: "Andrea del Verrocchio", relation: teacher, certainty: 0.7, cites: [{source: S1, locator: "'Apprenticeships'"}], how_known: "Britannica."}
  - {value: "Luca Pacioli", relation: collaborator, certainty: 0.7, cites: [{source: S1, locator: "'Vitruvian Man'"}], how_known: "Britannica."}
  - {value: "Marcantonio della Torre", relation: collaborator, certainty: 0.7, cites: [{source: S1, locator: "'Anatomical studies and drawings'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 51"}], how_known: "Study roster."}
  controversies:
    - {value: "Religious beliefs debated", certainty: 0.7, cites: [{source: S1, locator: "'Legacy'"}], how_known: "Britannica."}
  data_quality_flags: []
  open_questions:
    - "Find manuscript sigla and dates for Nos. 1132–1135."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Ludwig Heinrich Heydenreich"
    citation: "Heydenreich, Ludwig Heinrich. \"Leonardo da Vinci.\" Encyclopaedia Britannica, updated 26 September 2026. https://www.britannica.com/biography/Leonardo-da-Vinci."
    url: "https://www.britannica.com/biography/Leonardo-da-Vinci"
    accessed: 2026-10-15
    reliability_note: "Signed article body; no Top Questions content used."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators, review]
  - id: S2
    type: primary
    kind: "scholarly edition"
    author: "Leonardo da Vinci; ed. and trans. Jean Paul Richter"
    citation: "Leonardo da Vinci. The Notebooks of Leonardo Da Vinci, complete. Ed. and trans. Jean Paul Richter, 1888. Project Gutenberg eBook #5000."
    url: "https://www.gutenberg.org/ebooks/5000"
    accessed: 2026-10-15
    reliability_note: "Private notes in a nineteenth-century translation, read in an unofficial web copy; §7 cap 0.7; scored at 0.5."
    used_for: [worldview, timing, lane_b]
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

# Leonardo da Vinci

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Leonardo da Vinci (1452–1519), Italian painter, engineer and anatomist [S1]. Draft: primary_system BELOW_THRESHOLD; A 0 at 0.5; B 3 at 0.5; C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Plotted (faded).

## Life and work

Verrocchio's workshop; Milan 1482–99; Florence, Milan, Rome; France from 1516 [S1].

## Contribution and impact

Last Supper, Mona Lisa, anatomical drawings [S1].

## Childhood and education

Son of the notary Ser Piero; elementary schooling; apprenticed at about 15 [S1].

## Adult working worldview

Prays to a Lord who 'canst shorten or prolong the lives of men'; 'Necessity is ... the eternal curb and law of nature' [S2].

## Heritage (context only)

Tuscan [S1].

## Timing

First lasting contribution 1498, at 46 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Unclear [S2].

## Open questions

- Manuscript dates.

## Research log

- 2026-10-15: Read Britannica (Heydenreich) and Richter's Notebooks Nos. 1132–1135, 1208, 1210 (Gutenberg #5000).
