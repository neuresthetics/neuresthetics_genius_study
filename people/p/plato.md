---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 4
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch J)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to ancient. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-25, by: "Grok Bot", summary: "Perpetual deepen: religious_heritage_by_birth / baptism / catechism / family_religion TODO→UNKNOWN (no explicit birth-religion line in S1–S8; refuse Hellenic-milieu invention). Chart-moving NO."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch J, order P32: F 5, rank 65). Basics from Britannica (Meinwald). Worldview from the Timaeus and Laws X (Jowett, Gutenberg #1572 and #1750; web copies), attributed to Plato himself by SEP 'Plato's Timaeus' (Zeyl and Sattler), so they count under P42; spoken by characters (Timaeus, the Athenian Stranger), so 0.5. Not a scientist (Britannica: 'not a research mathematician'). primary_system PLATO 0.5; A 1 at 0.5 (alt 0); B 3 at 0.5 (alt 4); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Plotted (faded). Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Audit fixes (fallacy_catalog audit of 81b9098, run 1). Laws X dropped from the B rationale and cites: no source read attributes its theology to Plato (P42). SEP's opening sentence ('In the Timaeus Plato presents...') cited explicitly as the P42 attribution for the Timaeus. B stays 3 (0.5, alternative 4)."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #64, F5 rank 65). Needs: A faded; B faded. Added Lamb Loeb Timaeus via Perseus (S7 scholarly edition) with Stephanus 28a–30b, 47e–48a, 68e, 92c confirming Jowett A/B passages; support labelled corroborated (S2+S7+S3). Wikipedia EN (S6) + SEP Plato Kraut (S8) dual bio (P50); native_name Πλάτων. P47 source_quality on S1–S8. A/B statements verified_against → scholarly edition (Lamb). Values/certainties stay A 1 @0.5 and B 3 @0.5 (dialogue character speech + scholarly_reconstruction; P42). mid_basin BELOW_THRESHOLD. Chart: already faded filled — chart-moving NO. No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: plato
  display_name: "Plato"
  roster:
    canonical_name: "Plato"
    rank: 65
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Plato", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "lead ('Plato')"}], how_known: "Britannica and Wikipedia agree (P15)."}
  native_name: {value: "Πλάτων (Plátōn)", certainty: 0.7, cites: [{source: S6, locator: "lead (Ancient Greek: Πλάτων, Plátōn)"}], how_known: "Wikipedia lead."}
  aliases: []

basics:
  birth:
    date: {value: "-428", calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "opening ('428/427 bce')"}, {source: S6, locator: "infobox / lead (c. 428–7 BC)"}, {source: S8, locator: "opening ('429?–347 B.C.E.')"}], how_known: "Britannica 428/427; Wikipedia c. 428–7; SEP 429?. Exact year uncertain across dual sources (0.5); earlier Britannica year recorded; proleptic Julian."}
    place: {value: "Athens", modern_name: "Athens, Greece", polity_then: "Athens", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "infobox / lead"}], how_known: "Britannica and Wikipedia agree (P15)."}
  death:
    date: {value: "-348", calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "opening ('348/347')"}, {source: S6, locator: "infobox / lead (c. 348–7 BC)"}, {source: S8, locator: "opening ('429?–347 B.C.E.')"}], how_known: "Britannica 348/347; Wikipedia c. 348–7; SEP 347. Exact year uncertain (0.5)."}
    place: {value: "Athens", modern_name: "Athens, Greece", polity_then: "Athens", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "infobox / Final years and death"}], how_known: "Britannica and Wikipedia agree (P15)."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "The order and dates of the dialogues 'cannot be known' (S1, 'Dating, editing, translation'); the Academy is dated only to 'the 380s' (P39)."}
  era_bucket: {value: "-500 to 499", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "lead"}], how_known: "His whole adult life falls in the bucket on either birth year (P2, P39)."}
  region_of_birth: {value: "Southern Europe", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "lead"}], how_known: "Greece is Southern Europe in regions.csv (P3); dual-sourced."}
  region_of_work: {value: "Southern Europe", certainty: 1.0, cites: [{source: S1, locator: "'Life'"}, {source: S6, locator: "Later years: Syracuse and the Academy"}], how_known: "Athens; trips to Syracuse (Britannica; Wikipedia)."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S1, locator: "text"}, {source: S6, locator: "lead"}], how_known: "As recorded; dual-sourced."}
  languages_of_work: {value: [Greek], certainty: 1.0, cites: [{source: S1, locator: "'Dating, editing, translation'"}, {source: S6, locator: "lead (Ancient Greek)"}], how_known: "Britannica; Wikipedia."}
  occupations: {value: ["philosopher", "teacher"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "lead"}], how_known: "Britannica and Wikipedia."}

contribution:
  era_bucket: ancient
  fields: {value: ["metaphysics", "ethics", "political philosophy", "cosmology", "epistemology"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "Main interests"}], how_known: "Britannica; Wikipedia."}
  lasting_original_contributions:
    - {value: "Theory of forms", kind: theory, lasting: "(S1; S6)", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "The Forms"}], how_known: "Britannica; Wikipedia; undated (P39)."}
    - {value: "The dialogues (Republic, Timaeus and others)", kind: work, lasting: "'philosophical works of unparalleled influence' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "Notable works"}], how_known: "Undated (P39)."}
    - {value: "The Academy", kind: institution, lasting: "'the ultimate ancestor of the modern university' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}, {source: S6, locator: "Foundation of the Academy"}], how_known: "Founded in the 380s (S1); Wikipedia ~383 BC."}
  evidence_of_impact:
    - {value: "One of the major figures of Classical antiquity; foundational for Western philosophy", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S8, locator: "opening"}], how_known: "Britannica; SEP Plato."}
  major_works:
    - {value: "Republic", year: "undated", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "Notable works"}], how_known: "Britannica; Wikipedia; undated (P39)."}
    - {value: "Timaeus", year: "undated", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "§1"}, {source: S6, locator: "Notable works"}], how_known: "Britannica; SEP Timaeus; Wikipedia; undated (P39)."}
    - {value: "Laws", year: "undated", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "Notable works"}], how_known: "Britannica; Wikipedia; undated (P39)."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1; S8).", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S8, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated in sources read."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father Ariston, mother Perictione; aristocratic family related on the mother's side to Solon", role: parents, certainty: 0.7, cites: [{source: S1, locator: "'Life'"}, {source: S6, locator: "Life (Perictione; Solon)"}], how_known: "Britannica; Wikipedia."}
  household_circumstances: {value: "Aristocratic and distinguished Athenian family", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}, {source: S6, locator: "Life"}], how_known: "Britannica; Wikipedia."}
  schooling: []
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Socrates (as a young man, member of his circle)", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}, {source: S6, locator: "Socrates"}], how_known: "Britannica; Wikipedia."}
  languages_in_childhood: {value: TODO}
  notable_events:
    - {value: "Trial and execution of Socrates", year: -399, certainty: 0.7, cites: [{source: S1, locator: "'Life'"}, {source: S6, locator: "Thirty tyrants and Trial of Socrates"}], how_known: "Britannica; Wikipedia; adult event recorded for context; age omitted because the birth year is uncertain."}

worldview:
  unit: "adult working worldview"
  working_years: {value: UNKNOWN, how_known: "Equals timing.major_work_period (UNKNOWN, P39)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system:
    value: PLATO
    basis: scholarly_reconstruction
    certainty: 0.5
    cites: [{source: S1, locator: "opening"}, {source: S3, locator: "§1"}, {source: S8, locator: "§1"}]
    rationale: "The system is his own: forms as 'the most important constituents of reality' (S1); a universe that is 'the product of rational, purposive, and beneficent agency' (S3)."
    how_known: "Britannica and SEP reconstruct his doctrine; scholarly_reconstruction caps at 0.5. Dialogues are character speech (S6: Plato never speaks in his own voice)."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: PLATO, reason: "Chosen."}
  lio_axes:
    A_locus:
      value: 1
      basis: scholarly_reconstruction
      certainty: 0.5
      support: corroborated
      cites: [{source: S7, locator: "Tim. 28a–30b, 92c (Lamb Loeb: artificer/Constructor; 'He was good… devoid of envy'; cosmos as 'Living Creature… owing to the providence of God'; closing 'perceptible God… image of the Intelligible')"}, {source: S2, locator: "Timaeus, creator passage and closing (Jowett: 'father and maker'; 'living creature… providence of God'; 'sensible God')"}, {source: S3, locator: "§1 (Craftsman / Demiurge 28a6; living thing; questions on Craftsman distinctness)"}]
      how_known: "Dialogue speech attributed to Plato by SEP's opening sentence ('In the Timaeus Plato presents...', P42); Lamb Loeb scholarly edition (Stephanus) + Jowett web copy; 0.5 as character speech / scholarly_reconstruction. Two independent English editions of the primary + SEP → corroborated (P48)."
      rationale: "A maker (Lamb: 'artificer' / 'Constructor'; Jowett: 'father and maker of all') who orders a disorderly visible into a cosmos that is itself a living, ensouled, divine image (Tim. 29e–30b, 92c): a world that is itself divine, made by a maker. Named alternative: 0 (SEP notes the question whether the Craftsman is 'an entity that is ontologically distinct from both the model and its copy'). Certainty stays 0.5: Timaeus speaks, not Plato in his own voice (P42 character-speech addendum; S6)."
    B_cause:
      value: 3
      basis: scholarly_reconstruction
      certainty: 0.5
      support: corroborated
      cites: [{source: S7, locator: "Tim. 47e–48a, 68e (Lamb: 'Reason was controlling Necessity by persuading her'; two kinds of causes, 'the necessary and the divine')"}, {source: S2, locator: "Timaeus, opening of the Necessity section (Jowett: 'mind persuading necessity')"}, {source: S3, locator: "§1 (Intellect persuades Necessity 48a2–5; properties Necessity fixes not open to Craftsman to change)"}]
      how_known: "Dialogue speech attributed to Plato by SEP's opening sentence (P42); Lamb Loeb with Stephanus + Jowett; 0.5 as character speech. Independent editions + SEP → corroborated (P48)."
      rationale: "Lamb: 'this Cosmos in its origin was generated as a compound, from the combination of Necessity and Reason… Reason was controlling Necessity by persuading her' (48a); SEP: Necessity's fixed properties are such that 'it is not open to the Craftsman to change or eliminate' them. That leans toward 4, but the account is called merely likely, and no exceptionless order is stated (P40). Named alternative: 4. Laws X is not used: no source read attributes its theology to Plato (P42)."
    C_ledger: {value: UNKNOWN, cites: [{source: S4, locator: "Book X (read; unused for scores)"}], how_known: "Laws X argues against the view that gods can be appeased by gifts, but no source read attributes the Laws X theology to Plato (P42); not scored."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 1 and B 3 would satisfy A ≤ 1 and B ≥ 3, but both are at 0.5, below the 0.7 bar (§6, P19). Dialogue form / scholarly_reconstruction keeps the ceiling at 0.5 without a Jason ruling."}
  statements:
    - text: "For God desired that, so far as possible, all things should be good and nothing evil; wherefore, when He took over all that was visible, seeing that it was not in a state of rest but in a state of discordant and disorderly motion, He brought it into order out of disorder, deeming that the former state is in all ways better than the latter. […] Thus, then, in accordance with the likely account, we must declare that this Cosmos has verily come into existence as a Living Creature endowed with soul and reason owing to the providence of God."
      cites: [{source: S7, locator: "Tim. 30a–30b (Lamb Loeb)"}, {source: S2, locator: "Timaeus, creator passage (Jowett parallel)"}]
      date: "-348"
      context: "Timaeus's account of why the creator made the world. Date is death-cap terminus; dialogue undated (P39)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Spoken by Timaeus; attributed to Plato by SEP (P42). Lamb Loeb via Perseus; Jowett Gutenberg #1572 for parallel."
    - text: "For, in truth, this Cosmos in its origin was generated as a compound, from the combination of Necessity and Reason. And inasmuch as Reason was controlling Necessity by persuading her to conduct to the best end the most part of the things coming into existence, thus and thereby it came about, through Necessity yielding to intelligent persuasion, that this Universe of ours was being in this wise constructed at the beginning."
      cites: [{source: S7, locator: "Tim. 48a (Lamb Loeb)"}, {source: S2, locator: "Timaeus, opening of the Necessity section (Jowett parallel)"}, {source: S3, locator: "§1 (48a2–5)"}]
      date: "-348"
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "As above; SEP outline puts Necessity section at 47d3–69a5."
    - text: "itself a visible Living Creature embracing the visible creatures, a perceptible God made in the image of the Intelligible, most great and good and fair and perfect in its generation—even this one Heaven sole of its kind."
      cites: [{source: S7, locator: "Tim. 92c (Lamb Loeb)"}, {source: S2, locator: "Timaeus, closing sentence (Jowett: 'sensible God… only-begotten heaven')"}]
      date: "-348"
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Closing of Timaeus; Lamb vs Jowett wording of the same Stephanus locus."
  changes_over_life: []
  coder_notes: "Coder's call. Dialogues are character speech (Wikipedia: Plato never speaks in his own voice); SEP's attribution of the Timaeus cosmology to Plato ('In the Timaeus Plato presents...') satisfies P42's scholarly-agreement clause, but the 0.5 reflects the dialogue form, the 'likely account', and scholarly_reconstruction. Certainty cannot reach the 0.7 darkness bar without a Jason ruling on dialogue cosmology. D1 added Lamb Loeb Stephanus + dual bio; fill already corroborated."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Athenian aristocracy", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}, {source: S6, locator: "Life"}], how_known: "Britannica; Wikipedia."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated as a childhood confession in S1–S8; Athenian civic cult milieu is not coded as a scored heritage label without an explicit source line (cf. Aristotle UNKNOWN)."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "No baptism/initiation record applicable or opened."}
  childhood_catechism: {value: UNKNOWN, how_known: "No childhood catechism curriculum named."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "Undated works (P39)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "Undated (P39)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "Undated dialogues."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.5, cites: [{source: S2, locator: "Timaeus"}, {source: S7, locator: "Timaeus"}], how_known: "The Timaeus is itself a major work."}
  worldview_during_major_work: {value: "PLATO", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S8, locator: "§1"}], how_known: "As primary_system."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "The Academy fostered mathematics; Plato used the mathematicians' results (S1).", certainty: 0.5, cites: [{source: S1, locator: "'Life'"}, {source: S6, locator: "Mathematics"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Life'"}], how_known: "Not read."}
  circle_present: {value: "yes", rationale: "A maker whose mind orders the world by persuading necessity (Tim. 29e–30b, 48a).", certainty: 0.5, cites: [{source: S7, locator: "Tim. 30a–30b, 48a"}, {source: S2, locator: "Timaeus"}], how_known: "Coder's reading."}
  reading: "A divine maker and a divine ordered world; necessity persuaded by mind."
  notes: "Lane B only — not a finding."

institutions:
  - {value: "The Academy, Athens", role: founder, kind: "academy or learned society", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}, {source: S6, locator: "Foundation of the Academy"}], how_known: "Britannica (founded in the 380s); Wikipedia ~383 BC."}
collaborators:
  - {value: "Socrates", relation: teacher, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "Socrates"}], how_known: "Britannica; Wikipedia."}
  - {value: "Aristotle", relation: "student or assistant", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Life'"}, {source: S6, locator: "Notable students"}], how_known: "Britannica; Wikipedia."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 65"}], how_known: "Study roster."}
  controversies:
    - {value: "Authenticity of the Letters (including the Seventh) is disputed", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}, {source: S6, locator: "Authenticity"}], how_known: "Britannica; Wikipedia."}
  data_quality_flags: []
  open_questions:
    - "Certainty ceiling: A/B stay at 0.5 while cosmology is scored from character speech (P42). Jason ruling needed to raise toward darkness (≥0.7)."
    - "Optional Cornford Plato's Cosmology (1937) print/OCR as a second scholarly English beside Lamb — IA download blocked this pass."
    - "Laws X theology still unused without a P42 attribution source."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Meinwald, Constance C."
    citation: "Meinwald, Constance C. \"Plato.\" Encyclopaedia Britannica, updated 28 August 2026. https://www.britannica.com/biography/Plato."
    url: "https://www.britannica.com/biography/Plato"
    accessed: 2026-10-15
    reliability_note: "Signed body; Top Questions not cited."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators, review]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Plato; trans. Benjamin Jowett"
    citation: "Plato. Timaeus. Trans. Benjamin Jowett. Project Gutenberg eBook #1572."
    url: "https://www.gutenberg.org/ebooks/1572"
    accessed: 2026-10-15
    reliability_note: "Translation in an unofficial web copy; quotes taken from the dialogue text, not Jowett's introduction; §7 cap 0.7. Parallel to Lamb Loeb (S7) for A/B."
    source_quality: "unofficial web copy"
    used_for: [worldview, timing, lane_b]
  - id: S3
    type: secondary
    kind: encyclopedia
    author: "Zeyl, Donald; Sattler, Barbara"
    year: 2022
    citation: "Zeyl, Donald, and Barbara Sattler. \"Plato's Timaeus.\" Stanford Encyclopedia of Philosophy, first published 25 October 2005, substantive revision 13 May 2022. https://plato.stanford.edu/entries/plato-timaeus/."
    url: "https://plato.stanford.edu/entries/plato-timaeus/"
    accessed: 2026-10-15
    reliability_note: "Peer-reviewed reference article; P42 attribution sentence and Craftsman/Necessity analysis."
    source_quality: "reference entry"
    used_for: [worldview, contribution]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Plato; trans. Benjamin Jowett"
    citation: "Plato. Laws. Trans. Benjamin Jowett. Project Gutenberg eBook #1750."
    url: "https://www.gutenberg.org/ebooks/1750"
    accessed: 2026-10-15
    reliability_note: "Translation in an unofficial web copy; Book X read but not used for any score (no attribution source, P42)."
    source_quality: "unofficial web copy"
    used_for: [worldview]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S6
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    year: 2026
    citation: "Wikipedia contributors. \"Plato.\" Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/wiki/Plato. Dual-source bio (P50)."
    url: "https://en.wikipedia.org/wiki/Plato"
    accessed: 2026-10-24
    reliability_note: "Used for dual bio (dates/places, native name, Academy, Socrates, Aristotle, Letters authenticity, 'never speaks in his own voice'). Not sole support for A/B scores."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators, review]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "Plato; trans. W. R. M. Lamb"
    year: 1925
    citation: "Plato. Timaeus. Translated by W. R. M. Lamb. Plato in Twelve Volumes, Vol. 9. Cambridge, MA: Harvard University Press; London: William Heinemann, 1925. Read on Perseus Digital Library (Stephanus sections)."
    url: "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0180%3Atext%3DTim."
    accessed: 2026-10-24
    reliability_note: "Loeb Classical Library scholarly edition (Lamb), via Perseus, with Stephanus numbers. Independent English of the A_locus and B_cause Timaeus passages."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, timing, lane_b]
  - id: S8
    type: secondary
    kind: encyclopedia
    author: "Kraut, Richard"
    year: 2026
    citation: "Kraut, Richard. \"Plato.\" Stanford Encyclopedia of Philosophy, first published 20 March 2004, substantive revision 24 April 2026. https://plato.stanford.edu/entries/plato/."
    url: "https://plato.stanford.edu/entries/plato/"
    accessed: 2026-10-24
    reliability_note: "Peer-reviewed reference entry; dual bio and dialogue-form context."
    source_quality: "reference entry"
    used_for: [basics, contribution, worldview, timing]
---

# Plato

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Plato (Πλάτων; c. 428/427–348/347 BCE), Athenian philosopher, founder of the Academy [S1, S6, S8]. Draft after D1: primary_system PLATO 0.5; A 1 at 0.5 (corroborated); B 3 at 0.5 (corroborated); mid_basin BELOW_THRESHOLD. Plotted (faded, filled). Chart-moving NO this pass — darkness still capped by dialogue character speech.

## Life and work

Circle of Socrates; Syracuse; the Academy [S1, S6].

## Contribution and impact

Forms; dialogues (Republic, Timaeus, Laws); Academy [S1, S3, S6].

## Childhood and education

Aristocratic Athenian family (Ariston, Perictione) [S1, S6].

## Adult working worldview

Timaeus cosmology scored under P42 (SEP: "In the Timaeus Plato presents…") but spoken by the character Timaeus, so 0.5 [S3, S7]. Maker orders a living divine cosmos [S7, Tim. 30a–30b, 92c]; Reason persuades Necessity [S7, Tim. 48a]. Lamb Loeb (Stephanus) corroborates Jowett [S2, S7].

## Heritage (context only)

Athenian aristocracy [S1, S6].

## Timing

Works undated [S1, P39].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Circle present [S7, S2].

## Open questions

- Certainty ceiling at 0.5 for dialogue cosmology (needs Jason ruling for darkness).
- Optional Cornford *Plato's Cosmology* as second scholarly English.
- Laws X still unused without P42 attribution.

## Research log

- 2026-10-15: Read Britannica (Meinwald), SEP 'Plato's Timaeus', Timaeus and Laws X (Gutenberg #1572, #1750).
- 2026-10-15: Batch J audit fixes: Laws X dropped from B; SEP's opening sentence cited for P42.
- 2026-10-24 (D1): Lamb Loeb Timaeus via Perseus (28a–30b, 47e–48a, 68e, 92c); Wikipedia + SEP Plato Kraut dual bio; P47 on all sources; A/B support corroborated labelled; statements verified against scholarly edition. Cornford IA download blocked. No fallacy_catalog.
