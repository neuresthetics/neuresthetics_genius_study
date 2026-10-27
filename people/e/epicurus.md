---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z7; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to ancient. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #157, F 3, rank 165). Needs: corroborate A/B to ≥0.7 if justified. A 3 0.5→0.7 written_profession (Menoeceus X.123 + Principal Doctrine I / Sovran Maxims X.139 dual own-voice; Loeb S4 pp. 649, 663). Named alt 4 kept (Obbink atheism / gods-as-images residual; CODING_GUIDE §3 named-alt ceiling 0.7). B stays 3 @0.5 alt 4 (P16 addendum / P40 / P41: lawful atomic order without stated no-exception; swerve later sources = chance). Support corroborated on A (S1+S2+S4) and B (S1+S2+S4). mid_basin BELOW→false @0.7 (A≥3 branch, P10; A and alt 4 both ≥3 so P30 uses condition evidence). P50 Wikipedia dual bio (S5). P47 source_quality on S1–S5. primary EPICUR @1.0; C 4 @1.0; D/E UNKNOWN; span UNKNOWN. Plotted faded (min(A,B)=0.5). Chart-moving NO (B still 0.5). No fallacy_catalog. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z7 audit fixes: mid_basin false 0.5 -> BELOW_THRESHOLD (P10). Wikisource Hicks checked against the printed Loeb vol. 2 (1925; archive.org livesofeminentph02diog): X.76–77 on p. 607 and X.123 on p. 649 (the auditor's check, re-read), X.124–125 on p. 651 (coder's check); edition cited as S4. The web-copy cap (CODING_GUIDE §7) no longer applies, so primary_system EPICUR 0.7 -> 1.0 and C 4 0.7 -> 1.0 (written_profession ceiling 1.0, no named alternative)."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z7, order P32: F 3, rank 165; Edwin Hubble, rank 164, already coded). Own words from his three letters preserved in Diogenes Laertius X (Hicks translation, Wikisource transcription) and SEP 'Epicurus' (Konstan). primary_system EPICUR (0.7, Z7 draft; founder, written profession; Wikisource copy not yet checked against a printing). A 3 (0.5, alt 4): 'verily there are gods ... but they are not such as the multitude believe'; gods material and within the cosmos, as the EPICUR system. B 3 (0.5, alt 4): heavenly motions 'without the ministration or command ... of any being who ... enjoys perfect bliss'; invariable recurrence from 'the original ... conglomeration of atoms'; no stated no-exception claim, and the swerve (later sources) is chance (P40). C 4 (0.7): 'death is nothing to us'. D, E UNKNOWN. mid_basin false (0.5; A ≥ 3). Works undated: span UNKNOWN, era '-500 to 499' (as Aristotle). Plotted (A 3, B 3). Draft, not reviewed."}

identity:
  id: epicurus
  display_name: "Epicurus"
  roster:
    canonical_name: "Epicurus"
    rank: 165
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: "core"
    field: "philosophy"
    field_bucket: "philosophy"
  full_name: {value: "Epicurus, son of Neocles, of Gargettus", certainty: 0.7, cites: [{source: S1, locator: "X.1"}, {source: S5, locator: "lead"}], how_known: "Diogenes Laertius and Wikipedia agree (P50)."}
  native_name: {value: "Ἐπίκουρος", certainty: 0.7, cites: [{source: S2, locator: "§2"}, {source: S5, locator: "lead"}], how_known: "SEP and Wikipedia agree (P50)."}
  aliases: []

basics:
  birth:
    date: {value: "-341", certainty: 0.7, cites: [{source: S2, locator: "§2"}, {source: S5, locator: "lead / infobox"}], how_known: "SEP and Wikipedia agree (P50); SEP cites DL X.14."}
    place: {value: "Samos", modern_name: "Samos, Greece", polity_then: "Athenian cleruchy on Samos", certainty: 0.7, cites: [{source: S2, locator: "§2"}, {source: S5, locator: "Early life"}], how_known: "SEP and Wikipedia: born on Samos (Athenian settlement); DL X.1 names him of Gargettus (P50)."}
  death:
    date: {value: "-270", certainty: 0.7, cites: [{source: S2, locator: "§2"}, {source: S5, locator: "lead / infobox"}], how_known: "SEP and Wikipedia agree (P50)."}
    place: {value: "Athens", modern_name: "Athens, Greece", polity_then: "Athens", certainty: 0.7, cites: [{source: S1, locator: "X.15"}, {source: S2, locator: "§2"}, {source: S5, locator: "Death"}], how_known: "DL, SEP, and Wikipedia agree (P50)."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "Letters and On Nature undated; he founded his school at 32 (DL X.15, c. 310/309 BCE) and the Garden in Athens in 307/306 (S2 §2). As Aristotle, left UNKNOWN."}
  era_bucket: {value: "-500 to 499", certainty: 0.7, cites: [{source: S2, locator: "§2"}], how_known: "Every candidate year (c. 310–270 BCE) is in '-500 to 499' (P2)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.5, cites: [{source: S2, locator: "§2"}], how_known: "Samos, Greece (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S2, locator: "§2"}], how_known: "Athens from 307/306; earlier Mytilene and Lampsacus (now Turkey)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S2, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Ancient Greek"], certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP."}
  occupations: {value: ["philosopher", "head of the Garden school"], certainty: 0.7, cites: [{source: S2, locator: "§2"}], how_known: "SEP."}

contribution:
  era_bucket: ancient
  fields: {value: ["ethics", "physics (atomism)", "epistemology"], certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "SEP."}
  lasting_original_contributions:
    - {value: "Epicurean system (atomist physics, empiricist canon, ethics of tranquillity)", year: UNKNOWN, kind: "body of work", lasting: "the school 'continues for ever without interruption' (DL X.9); system intact in SEP", certainty: 0.7, cites: [{source: S1, locator: "X.9"}, {source: S2, locator: "opening"}], how_known: "DL; SEP; undated."}
  evidence_of_impact:
    - {value: "School lasted centuries; Lucretius and Diogenes of Oenoanda carried it on", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP."}
  major_works:
    - {value: "Letter to Herodotus; Letter to Menoeceus; On Nature (37 books)", year: UNKNOWN, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "X.27–29"}], how_known: "DL; undated."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founder of a lasting school (S2).", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "SEP."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Neocles, father, schoolmaster", role: "father", certainty: 0.5, cites: [{source: S1, locator: "X.1–4"}], how_known: "DL; the schoolmaster report comes from hostile witnesses."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events:
    - {value: "Turned to philosophy at 14 (or 12)", certainty: 0.5, cites: [{source: S1, locator: "X.2; X.14"}], how_known: "DL; reports differ."}

worldview:
  unit: "adult working worldview"
  working_years: {value: UNKNOWN, how_known: "Works undated; equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: 
    value: EPICUR
    basis: written_profession
    certainty: 1.0
    cites: [{source: S1, locator: "X.123; X.76–77"}, {source: S4, locator: "pp. 607, 649"}, {source: S2, locator: "opening"}]
    how_known: "Founder; his letters. The Wikisource Hicks text was checked against the printed Loeb vol. 2 (1925) scan (S4: X.76–77 p. 607, X.123 p. 649), so the web-copy cap (CODING_GUIDE §7) no longer applies."
    rationale: "He founded the system the EPICUR code names."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: EPICUR, reason: "Founder."}
  lio_axes:
    A_locus: 
      value: 3
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S1, locator: "X.123; X.139"}, {source: S4, locator: "pp. 649, 663"}, {source: S2, locator: "§4–5"}]
      how_known: "Dual own-voice: Letter to Menoeceus (X.123) plus Principal Doctrine I / Sovran Maxims (X.139), both Loeb-checked (S4). Named alternative, so 0.7 not 1.0 (CODING_GUIDE §3). Independent source ids → corroborated (P48)."
      rationale: "'Verily there are gods ... but they are not such as the multitude believe' (X.123); PD I: 'A blessed and eternal being has no trouble himself and brings no trouble upon any other being' (X.139). Gods are immortal and blessed living beings, material (S2), not concerned with human affairs. Divine beings within nature, no transcendent person: 3. Alternative 4 kept honest (Obbink 1989 atheism / gods-as-images residual in S2 bibliography; mainstream SEP and Wikipedia affirm the gods exist)."
      alternatives:
        - {value: 4, note: "Obbink atheism / gods read as images or within nature's order only (residual).", cites: [{source: S2, locator: "§5 / bibliography"}]}
    B_cause: 
      value: 3
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S1, locator: "X.76–77; X.97"}, {source: S4, locator: "pp. 606–607, 623–624"}, {source: S2, locator: "§3; §4"}]
      how_known: "Letters to Herodotus and Pythocles (own voice, Loeb-checked). Lawful atomic order without a stated no-exception claim (P16 addendum / P41); swerve only in later sources and is chance (P40) → 0.5, never 4. Support corroborated (P48)."
      rationale: "Heavenly motions occur 'without the ministration or command, either now or in the future, of any being who ... enjoys perfect bliss' (X.76); 'where we find phenomena invariably recurring, the invariableness ... must be ascribed to the original interception and conglomeration of atoms' (X.77); 'the divine nature must not on any account be adduced to explain' celestial regularity (X.97). 3, not 4 (P16 addendum; P40; P41); as the EPICUR system."
      alternatives:
        - {value: 4, note: "If the swerve is read as natural indeterminacy compatible with 4, or if invariable recurrence is stretched to exceptionless.", cites: [{source: S2, locator: "§4"}]}
    C_ledger: {value: 4, basis: written_profession, certainty: 1.0, cites: [{source: S1, locator: "X.124–125"}, {source: S4, locator: "p. 651"}], how_known: "Written profession: 'death is nothing to us ... death is the privation of all sentience'; no afterlife reward or punishment (S2 §4)."}
    D_authority: {value: UNKNOWN, how_known: "Not scored."}
    E_scope: {value: UNKNOWN, how_known: "Not scored."}
  mid_basin: {value: false, certainty: 0.7, cites: [{source: S1, locator: "X.123; X.139"}, {source: S4, locator: "pp. 649, 663"}], how_known: "A_locus 3 at 0.7 with named alt 4; both ≥ 3, so P30 uses the certainty of the A≥3 condition (Menoeceus + Principal Doctrine I), not the exact-value contest. A≥3 branch reads A only (P10). Deepen D1 lifted A past the Z7 0.5 BELOW_THRESHOLD."}
  statements:
    - text: "For verily there are gods, and the knowledge of them is manifest; but they are not such as the multitude believe, seeing that men do not steadfastly maintain the notions they form respecting them."
      cites: [{source: S1, locator: "X.123"}]
      context: "Letter to Menoeceus."
      axes: [A_locus]
      kind: "published letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "Hicks translation via Wikisource; checked against the Loeb vol. 2 scan, p. 649 (S4)."
    - text: "Nay more: we are bound to believe that in the sky revolutions, solstices, eclipses, risings and settings, and the like, take place without the ministration or command, either now or in the future, of any being who at the same time enjoys perfect bliss along with immortality."
      cites: [{source: S1, locator: "X.76"}]
      context: "Letter to Herodotus."
      axes: [B_cause]
      kind: "published letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "Hicks translation via Wikisource; checked against the Loeb vol. 2 scan, p. 607 (S4)."
    - text: "A blessed and eternal being has no trouble himself and brings no trouble upon any other being; hence he is exempt from movements of anger and partiality, for every such movement implies weakness."
      cites: [{source: S1, locator: "X.139"}, {source: S4, locator: "p. 663"}]
      context: "Principal Doctrines / Sovran Maxims I (Kuriai Doxai), preserved in Diogenes Laertius X."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Hicks translation via Wikisource; checked against the Loeb vol. 2 scan, p. 663 (S4). Own-voice catechism; not a P49 reconstruction."
    - text: "And further, let the regularity of their orbits be explained in the same way as certain ordinary incidents within our own experience; the divine nature must not on any account be adduced to explain this, but must be kept free from the task and in perfect bliss."
      cites: [{source: S1, locator: "X.97"}, {source: S4, locator: "pp. 623–624"}]
      context: "Letter to Pythocles, on celestial phenomena."
      axes: [B_cause, A_locus]
      kind: "published letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Hicks translation via Wikisource; checked against the Loeb vol. 2 scan, pp. 623–624 (S4)."
  changes_over_life: []
  coder_notes: "Hicks wording checked against the Loeb vol. 2 scan (S4; Z7 audit and deepen D1). A lifted on Menoeceus + PD I; B held at 0.5 under P16/P40/P41 (swerve not in the three letters). Obbink 1989 kept as residual alt 4, not a real dispute against own-voice 'verily there are gods'."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Athenian (deme Gargettus)", certainty: 0.7, cites: [{source: S1, locator: "X.1"}], how_known: "DL."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "Works undated (S2 §1); founded his school at 32 (DL X.15) and worked until 270 BCE (P30)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "First-lasting year unknown."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Empiricist inference from the senses; little interest in mathematics (S2 §3).", certainty: 0.5, cites: [{source: S2, locator: "§3"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "The Garden (his school, Athens)", role: "founder and head", years: "306 BCE–270 BCE", kind: "other", certainty: 0.7, cites: [{source: S1, locator: "X.10–11"}, {source: S2, locator: "§2"}], how_known: "DL; SEP."}
collaborators:
  - {value: "Nausiphanes", relation: "teacher", note: "Democritean; Epicurus denied it", certainty: 0.5, cites: [{source: S1, locator: "X.13"}, {source: S2, locator: "§2"}], how_known: "DL; SEP."}
  - {value: "Metrodorus of Lampsacus", relation: "student or assistant", note: "closest disciple", certainty: 0.7, cites: [{source: S1, locator: "X.22–23"}], how_known: "DL."}
  - {value: "Democritus", relation: "influenced by", note: "atomism", certainty: 0.7, cites: [{source: S2, locator: "§3"}], how_known: "SEP."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 165"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Letters read in Hicks's translation (checked against the Loeb scan), not the Greek."
  open_questions:
    - "Dating of the letters and On Nature."

sources:
  - id: S1
    type: primary
    kind: "scholarly edition"
    author: "Diogenes Laertius (tr. R. D. Hicks)"
    citation: "Diogenes Laertius. Lives of Eminent Philosophers, Book X. Tr. R. D. Hicks (Loeb, 1925). Wikisource transcription. https://en.wikisource.org/wiki/Lives_of_the_Eminent_Philosophers/Book_X"
    url: "https://en.wikisource.org/wiki/Lives_of_the_Eminent_Philosophers/Book_X"
    accessed: 2026-10-19
    reliability_note: "Preserves Epicurus's three letters and Principal Doctrines; unofficial web copy of a published translation; wording checked against S4."
    source_quality: "unofficial web copy"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, institutions, collaborators]
  - id: S2
    type: tertiary
    kind: "encyclopedia"
    author: "David Konstan"
    citation: "Konstan, David. 'Epicurus.' Stanford Encyclopedia of Philosophy (rev. 8 Jul 2022). https://plato.stanford.edu/entries/epicurus/"
    url: "https://plato.stanford.edu/entries/epicurus/"
    accessed: 2026-10-19
    reliability_note: "Peer-reviewed reference entry."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, worldview, lane_b, institutions, collaborators]
  - id: S3
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [review]
  - id: S4
    type: primary
    kind: "scholarly edition"
    author: "Diogenes Laertius (tr. R. D. Hicks)"
    citation: "Diogenes Laertius. Lives of Eminent Philosophers, vol. 2. Tr. R. D. Hicks. Loeb Classical Library (London: Heinemann; New York: Putnam, 1925). Archive.org scan. https://archive.org/details/livesofeminentph02diog"
    url: "https://archive.org/details/livesofeminentph02diog"
    accessed: 2026-10-19
    reliability_note: "Library scan of the printed Loeb edition; used to check the Wikisource text (CODING_GUIDE §7). OCR txt used this pass for X.97 and X.139 page locators."
    source_quality: "archive scan (OCR only)"
    used_for: [worldview]
  - id: S5
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. \"Epicurus.\" Wikipedia, English. https://en.wikipedia.org/wiki/Epicurus (rev. 1379475008, 2026-10-10)."
    url: "https://en.wikipedia.org/wiki/Epicurus"
    accessed: 2026-10-24
    reliability_note: "P50 dual bio with SEP. Lead affirms gods exist with no involvement in human affairs; notes swerve from the Epicurean tradition. Category labels ignored for coding."
    source_quality: "reference entry"
    used_for: [identity, basics]
---

## Summary

Epicurus (341–270 BCE), founder of the Garden [S1, S2, S5]. Deepen D1: EPICUR @1.0; A 3 @0.7 (alt 4); B 3 @0.5 (alt 4); C 4 @1.0; mid false @0.7; plotted faded.

## Life and work

Samos, Colophon, Mytilene, Lampsacus, Athens [S1, S2].

## Contribution and impact

Atomist physics; ethics of tranquillity [S2].

## Childhood and education

Schoolmaster's son; philosophy from 14 [S1].

## Adult working worldview

Gods exist but do not govern the world (Menoeceus; PD I); nature runs by atoms without divine ministration (Herodotus; Pythocles) [S1, S4].

## Heritage (context only)

Athenian [S1].

## Timing

Works undated.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Dating of the letters.

## Research log

- 2026-10-24 (deepen D1, queue #157): Loeb OCR (IA livesofeminentph02diog_djvu.txt) for PD I p. 663 and Pythocles X.97 pp. 623–624; Wikisource Hicks for PD I wording; SEP Konstan + Wikipedia EN (P50). A 0.5→0.7; B stays 0.5 under P16/P40/P41; mid BELOW→false @0.7. P47 on S1–S5; P48 A/B corroborated. No fallacy_catalog. No figures/.
- 2026-10-19: Read DL X (Hicks) and SEP.
