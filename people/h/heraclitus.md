---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to philosophy. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #170, F 3, rank 180). Goals: corroborate or firm PANT/A/B; note darkness/fill on next chart refresh. Hunt: re-read SEP Graham (S1) Theology/Cosmology (B30, B32, B64, B67, B114); Kahn 1979 Art and Thought (S3) — B30/XXXVII, B67, B32, B64 translations + commentary (world = everliving fire; god = day/night…; wise one would/would not be called Zeus; thunderbolt steers). IEP Graham same author as S1 — unused for P48 independence. Neels PhilArchive blocked (Cloudflare). Graham Texts of Early Greek Philosophy not obtained. PANT kept @0.5 scholarly_reconstruction (two-part: B67 whole-of-opposites + B30 eternal measured kosmos/fire); alt BELOW (B32/B64 wise-one / steer tension; Kahn himself reads steering toward cosmic intelligence). A 4 @0.5 alt 3 kept; B 3 @0.5 alt 4 kept (lawful measures, not scientist; no exceptionless claim). support: corroborated on A and B (P48) S1+S3 — independent scholars. Certainty stays 0.5 (P49; do not invent 0.7). mid BELOW; PLOTTED faded. Chart-moving YES for fill (hollow→filled on next refresh); darkness unchanged (still faded). P47 source_quality. Statements add B67/B32/B64 (Kahn scholarly edition). No fallacy_catalog; no figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "AA1 audit fix (FAIL, P39 strict reading): era_bucket '-500 to 499' @0.5 -> UNKNOWN; life dates UNKNOWN and the c. 500 BCE floruit sits on the bucket edge. Plot unchanged (A 4 / B 3, faded)."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA1, order P32: F 3, rank 180). Source: SEP 'Heraclitus' (Daniel W. Graham, rev. 2023), a scholar's account with DK fragment numbers; the fragments are quoted in SEP's translation and attributed to him by scholarly agreement (P42), transmitted by later authors. Worldview by scholarly_reconstruction (0.5 cap): 'God is day night, winter summer, war peace ...' (B67) and 'This world-order ... no god nor man did create, but it ever was and is and will be: everliving fire, kindling in measures' (B30); 'all human laws are nourished by the one divine law' (B114). PANT 0.5 (two-part test: the divine identified with the whole of opposites, part 1; one eternal measured order, part 2), alt BELOW_THRESHOLD ('would and would not be called by the name of Zeus', B32). A 4 at 0.5 (alt 3); B 3 at 0.5 (alt 4): lawful measures, no exceptionless claim (P41-style); not counted a scientist (no listed theory about physical systems; the doctrines are metaphysical). C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD (A ≥ 3 only at 0.5, P10). Span UNKNOWN ('active around 500 BCE' is a floruit, not a composition range; P39). Plotted, faded, at A 4 / B 3. Draft, not reviewed."}

identity:
  id: heraclitus
  display_name: "Heraclitus"
  roster:
    canonical_name: "Heraclitus"
    rank: 180
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: "core"
    field: "philosophy"
    field_bucket: "philosophy"
  full_name: {value: "Heraclitus of Ephesus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  native_name: {value: "Ἡράκλειτος", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Greek spelling the coder's."}
  aliases:
    - {name: "Heraclitus", kind: "roster alias"}

basics:
  birth:
    date: {value: UNKNOWN, how_known: "SEP: 'active around 500 BCE'; no birth year."}
    place: {value: "Ephesus", modern_name: "near Kuşadası, Turkey", polity_then: "Ionia (Persian Empire)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  death:
    date: {value: UNKNOWN, how_known: "Not stated in the source read."}
    place: {value: UNKNOWN, how_known: "Not stated."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "Undated: 'active around 500 BCE' (S1) is a floruit, not a composition range or dating event (P39; RQ-Z9-N1 needs a composition range)."}
  era_bucket: {value: UNKNOWN, how_known: "P39 (strict reading, XW3): life dates UNKNOWN and the floruit 'around 500 BCE' (S1) sits on the -500 bucket edge, so no single bucket holds every adult year (AA1 audit)."}
  region_of_birth: {value: "Middle East and North Africa", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Ephesus, modern Turkey (P3)."}
  region_of_work: {value: "Middle East and North Africa", certainty: 0.5, cites: [{source: S1, locator: "1. Life and Work"}], how_known: "Ephesus."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Ancient Greek"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "SEP."}
  occupations: {value: ["philosopher"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}

contribution:
  primary_domain: philosophy
  fields: {value: ["philosophy", "cosmology"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  lasting_original_contributions:
    - {value: "Doctrines of flux and the unity of opposites; the Logos", year: UNKNOWN, kind: "body of work", lasting: "'Already in antiquity he was famous for advocating the coincidence of opposites, the flux doctrine' (S1); influence section", certainty: 0.7, cites: [{source: S1, locator: "opening; 3; 7. Influence"}], how_known: "SEP; a single book, undated."}
  evidence_of_impact:
    - {value: "Influence on Plato, Aristotle, the Stoics and Hegel", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "7. Influence"}], how_known: "SEP."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founding Presocratic (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}

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
  working_years: {value: UNKNOWN, how_known: "Equals timing.major_work_period (UNKNOWN, P39)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system:
    value: PANT
    basis: scholarly_reconstruction
    certainty: 0.5
    cites: [{source: S1, locator: "4. Cosmology; 5. Theology"}, {source: S3, locator: "XXXVII (D.30); CXXIII (D.67); intro §3"}]
    how_known: "SEP + Kahn 1979 (P42 fragments attributed by scholarly agreement; P49 reconstruction ceiling 0.5)."
    rationale: "Part 1: the divine identified with the whole of opposites — SEP B67 'God is day night, winter summer, war peace, satiety hunger'; Kahn CXXIII same pair-list as 'The god' that 'alters' like fire named by incense. Part 2: one eternal measured order — B30/Kahn XXXVII kosmos 'ever was and is and will be: fire everliving, kindled in measures and in measures going out'; Kahn commentary identifies world-order with that eternal fire (immanent source, not a craftsman outside). Alternative BELOW_THRESHOLD kept: B32 (Kahn: wise one alone 'unwilling and willing to be spoken of by the name of Zeus') and B64 ('Thunderbolt steers all things') leave a ruling-mind / cosmic-intelligence reading open; Kahn himself reads 'steering' toward cognition and intention. Tension not settled → stay 0.5; do not invent 0.7."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: PANT, reason: "Coded at 0.5: god as whole of opposites + eternal measured fire/kosmos (S1; S3)."}
    - {code: STOIC, reason: "Not used: Stoicism is later; the Stoics drew on him (S1)."}
  lio_axes:
    A_locus:
      value: 4
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S1, locator: "4. Cosmology; 5. Theology"}, {source: S3, locator: "XXXVII (D.30); CXXIII (D.67)"}]
      how_known: "SEP + Kahn; P49 0.5 cap."
      support: corroborated
      rationale: "Divine = world-order / unity of opposites (B67; B30 'no god nor man did create' the kosmos that is everliving fire): God as the order of nature, 4. Alternative 3: governing 'wise one' (B32) and thunderbolt that 'steers' (B64) read as a mind over the order — kept; Kahn commentary leans that way on steering."
      alternatives:
        - {value: 3, note: "Governing wise one / cosmic intelligence (B32, B64); Kahn on steering.", cites: [{source: S1, locator: "4. Cosmology"}, {source: S3, locator: "commentary on LIV (D.41); CXIX (D.64)"}]}
    B_cause:
      value: 3
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S1, locator: "4. Cosmology; 6"}, {source: S3, locator: "XXXVII (D.30); XXXIX (D.31B)"}]
      how_known: "SEP + Kahn; P49 0.5 cap. Not a scientist, so B rests on statements about nature (P16)."
      support: corroborated
      rationale: "Everliving fire 'kindled in measures and in measures going out' (B30 / Kahn XXXVII); sea 'measures up to the same amount' (B31B / Kahn XXXIX); human laws 'nourished by the one divine law' (B114, S1): lawful order, with no explicit no-exception claim, so 3 (P41-style). Alternative 4: uncreated world under fixed measures read as exceptionless."
      alternatives:
        - {value: 4, note: "Fixed measures read as exceptionless.", cites: [{source: S1, locator: "4. Cosmology"}, {source: S3, locator: "XXXVII (D.30)"}]}
    C_ledger: {value: UNKNOWN, how_known: "Soul fragments (B36) concern transformation, not reward; not scored."}
    D_authority: {value: UNKNOWN, how_known: "Not scored: 'Having harkened not to me but to the Word (Logos)' (B50) is a lead for reason over authority."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is at least 3 only at 0.5; P10 caps mid_basin below the 0.7 bar."}
  statements:
    - text: "The ordering, the same for all, no god nor man has made, but it ever was and is and will be: fire everliving, kindled in measures and in measures going out."
      cites: [{source: S3, locator: "XXXVII (D.30)"}, {source: S1, locator: "4. Cosmology (B30)"}]
      date: "-500"
      context: "Fragment B30 (DK); Kahn XXXVII; transmitted by Clement; date is the floruit."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Kahn 1979 translation; SEP has a close variant. Attributed by scholarly agreement (P42). Scores rest on scholarly_reconstruction, not on the quotation alone."
    - text: "The god: day and night, winter and summer, war and peace, satiety and hunger. It alters, as when mingled with perfumes, it gets named according to the pleasure of each one."
      cites: [{source: S3, locator: "CXXIII (D.67)"}, {source: S1, locator: "5. Theology (B67)"}]
      date: "-500"
      context: "Fragment B67 (DK); Kahn CXXIII."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Kahn 1979 translation. P42 attribution."
    - text: "The wise is one alone, unwilling and willing to be spoken of by the name of Zeus."
      cites: [{source: S3, locator: "CXVIII (D.32)"}, {source: S1, locator: "5. Theology (B32)"}]
      date: "-500"
      context: "Fragment B32 (DK); supports named alt A 3 / primary BELOW lead."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Kahn wording via scholarly edition / concordant SEP paraphrase. P42."
    - text: "Thunderbolt steers all things."
      cites: [{source: S1, locator: "4. Cosmology (B64)"}, {source: S3, locator: "CXIX (D.64)"}]
      date: "-500"
      context: "Fragment B64 (DK); named alt A 3 (steering / cosmic intelligence)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "SEP translation; Kahn edition has the same short fragment (pilots/steers). P42."
  changes_over_life: []
  coder_notes: "Deepen D1 2026-10-24: Kahn 1979 (S3) corroborates SEP on B30/B67 PANT path; B32/B64 keep cosmic-mind tension (Kahn on steering). Graham Texts of Early Greek Philosophy still wanted for critical apparatus. IEP is same Graham as SEP — not a second independent source for P48. Chart fill would go hollow→filled on next refresh; darkness stays faded at 0.5."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Ionian Greek (Ephesian aristocracy)", certainty: 0.5, cites: [{source: S1, locator: "1. Life and Work"}], how_known: "SEP."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "Undated: floruit around 500 BCE only (P39)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "Undated (P39)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Oracular aphorisms, not geometric argument (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions: []
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 180"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Fragments known only through later authors."
  open_questions:
    - "Graham Texts of Early Greek Philosophy critical apparatus for B32/B64/B67."
    - "Whether a fuller consensus edition would warrant lifting certainty above 0.5 (P49 — do not invent 0.7 this pass)."

sources:
  - id: S1
    type: secondary
    kind: "encyclopedia"
    author: "Daniel W. Graham"
    citation: "Graham, Daniel W. 'Heraclitus.' Stanford Encyclopedia of Philosophy (rev. 8 December 2023). https://plato.stanford.edu/entries/heraclitus/"
    url: "https://plato.stanford.edu/entries/heraclitus/"
    accessed: 2026-10-24
    reliability_note: "Signed scholarly reference article, re-read in full on deepen; DK fragment numbers and translations."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, worldview, heritage, lane_b]
  - id: S2
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [review]
  - id: S3
    type: secondary
    kind: "scholarly edition"
    author: "Charles H. Kahn"
    year: 1979
    citation: "Kahn, Charles H. The Art and Thought of Heraclitus: An Edition of the Fragments with Translation and Commentary. Cambridge: Cambridge University Press, 1979. Fragments XXXVII (D.30), CXXIII (D.67), CXVIII (D.32), CXIX (D.64); General introduction §3; commentary on XXXVII."
    url: "https://topologicalmedialab.net/xinwei/classes/readings/Heraclitus/Heraclitus_readings_flux.pdf"
    accessed: 2026-10-24
    reliability_note: "Standard scholarly edition with Greek, translation, and commentary. Read in a course PDF excerpt that includes the full general introduction, the B30/B67/B31 cluster with translation, and extended commentary on XXXVII–XL. Independent of Graham SEP (different author). Used for P48 corroboration."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview]
---

## Summary

Heraclitus of Ephesus (fl. c. 500 BCE), philosopher [S1; S3]. Deepen D1: PANT (0.5); A 4 / B 3 at 0.5 with support corroborated (S1+S3). Plotted (faded; fill would be filled on next chart refresh).

## Life and work

Ephesus [S1].

## Contribution and impact

Flux; unity of opposites; Logos [S1].

## Childhood and education

Self-taught (B101) [S1].

## Adult working worldview

God as day/night and the other opposites (B67); kosmos as everliving fire in measures (B30) — PANT path [S1; S3]. Wise one would/would not be called Zeus (B32); thunderbolt steers (B64) — named alt toward cosmic mind [S1; S3].

## Heritage (context only)

Ephesian aristocracy [S1].

## Timing

Undated (P39).

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Graham Texts apparatus for B32/B64/B67.
- Consensus bar for certainty >0.5 (P49).

## Research log

- 2026-10-24: Deepen D1. SEP re-read; Kahn 1979 edition (S3) corroborates A/B/PANT at 0.5; support corroborated; chart fill hollow→filled next refresh; darkness stays faded. IEP same Graham — unused for independence. No figures/.
- 2026-10-19: AA1 audit fix (FAIL, P39 strict reading): era_bucket '-500 to 499' @0.5 -> UNKNOWN; life dates UNKNOWN and the c. 500 BCE floruit sits on the bucket edge. Plot unchanged (A 4 / B 3, faded).
- 2026-10-19: Read SEP (Graham).
