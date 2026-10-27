---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch L)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to ancient. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch L, order P32: F 5, rank 73). Basics from Britannica (Richard Kraut), signed body through 'Xenophon'; Top Questions not cited. Socrates wrote nothing; his words survive only as character speech in Plato and Xenophon, and scholars disagree which dialogues convey the historical Socrates (S1), so nothing is scored (P42). primary_system UNKNOWN; A–E UNKNOWN; mid_basin UNKNOWN (P19). First lasting contribution UNKNOWN (undated, P39). Not plotted. Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #72, F5 rank 73). Needs: A UNKNOWN; B UNKNOWN; 1 source. Dual bio: Britannica Kraut (S1) + Wikipedia EN (S4) + SEP Socrates Nails (S3) (P50). P47 source_quality on S1–S8. Thin-source / no own writings: Plato Apology and Xenophon are reported speech / character speech (P42 Analects-style addendum); scores rest on scholars' reconstructions (P49), not on dialogue wording alone. A_locus UNKNOWN → 0 @0.5 scholarly_reconstruction (alt 1): SEP Religion and Morality (Hare, S5) and IEP Socrates (Ambury, S6) reconstruct historical Socrates as believing in gods, observant, objecting to the atheism charge, guided by the daimonion and Apollo's Delphic oracle; personal intervening divinities → interventionist pole. Named alt 1: reformed theology (gods perfectly good; reject Homeric immoral myths) still personal and intervening. Support corroborated (S5+S6). Illustrative Fowler Loeb Apology via Perseus (S7 scholarly edition): daimonion 31d; oracle 21a; divine sign 40a — kind reported speech. B_cause stays UNKNOWN: not a scientist (P30); Plato's Socrates denies cosmological inquiry (Apology); Xenophon Memorabilia 1.4 design argument is contested as Xenophon's and not used (P42); no scholarly consensus reconstruction of a P16 nature-order account. primary_system stays UNKNOWN (no listed code fits contested historical Socratic piety; HELLEN is modern reconstructionist paganism). mid_basin stays UNKNOWN (B UNKNOWN, P19). Chart-moving NO (still unplotted). Filled parents, family religion, childhood notes from SEP/Wikipedia. No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: socrates
  display_name: "Socrates"
  roster:
    canonical_name: "Socrates"
    rank: 73
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Socrates", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lead"}], how_known: "Britannica and Wikipedia agree (P15)."}
  native_name: {value: "Σωκράτης", certainty: 0.7, cites: [{source: S3, locator: "title / Greek form"}, {source: S4, locator: "lead"}], how_known: "SEP and Wikipedia; Greek form."}
  aliases: []

basics:
  birth:
    date: {value: "-470", calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "opening ('c. 470 bce')"}, {source: S4, locator: "lead ('c. 470–399 BC')"}, {source: S3, locator: "opening (469–399)"}], how_known: "Britannica c. 470; Wikipedia 470 or 469; SEP 469. Approximate (0.5); proleptic Julian."}
    place: {value: "Athens (deme Alopece)", modern_name: "Athens, Greece", polity_then: "Athens", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "§3 (Alopece)"}, {source: S4, locator: "Birth and early life"}], how_known: "Britannica Athens; SEP/Wikipedia deme Alopece."}
  death:
    date: {value: "-399", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "§3 (trial 399)"}, {source: S4, locator: "lead"}], how_known: "Britannica, SEP, Wikipedia agree on 399 BCE."}
    place: {value: "Athens", modern_name: "Athens, Greece", polity_then: "Athens", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lead"}], how_known: "Two sources."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "He wrote nothing; his conversations are undated (P39)."}
  era_bucket: {value: "-500 to 499", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Whole life in the bucket (P2)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Greece (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Athens."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [Ancient Greek], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "opening"}], how_known: "Athenian; SEP and Britannica."}
  occupations: {value: ["philosopher"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
contribution:
  era_bucket: ancient
  fields: {value: ["philosophy", "ethics"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "opening"}], how_known: "Britannica; SEP."}
  lasting_original_contributions:
    - {value: "Socratic conversation (questioning about the human excellences), known through Plato and Xenophon", kind: method, lasting: "'profound influence on Classical antiquity and Western philosophy' (S1); founding figure of Western philosophy (S3, S4)", certainty: 0.5, cites: [{source: S1, locator: "opening; 'Philosophical and literary sources'"}, {source: S3, locator: "opening"}], how_known: "Undated (P39); reconstructed from others' writings (0.5)."}
  evidence_of_impact:
    - {value: "His thought 'exerted a profound influence on Classical antiquity and Western philosophy'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "opening"}], how_known: "Britannica; SEP."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1, S3).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Athenian civic polytheism (traditional Olympian cult)", certainty: 0.5, cites: [{source: S3, locator: "§3 (phratry; civic initiation)"}, {source: S6, locator: "§1.a.ii Greek Religion"}], how_known: "SEP chronology: presented to phratry and deme under conventional Athenian male socialization; IEP on the religious culture he was raised in. Not a personal confession (0.5)."}
  family_religious_practice: {value: "Civic cult participation expected of citizens (festivals, phratry)", certainty: 0.5, cites: [{source: S3, locator: "§3"}, {source: S6, locator: "§1.a.ii"}], how_known: "IEP/SEP on Athenian civic religion; specific household rites not read."}
  parents_and_household:
    - {value: "Father Sophroniscus (stonemason / stoneworker); mother Phaenarete (midwife); half-brother Patrocles", role: parents, certainty: 0.7, cites: [{source: S3, locator: "§3"}, {source: S4, locator: "Birth and early life"}, {source: S6, locator: "§1.a.i"}], how_known: "SEP, Wikipedia, IEP agree."}
  household_circumstances: {value: "Not extremely poor, not wealthy; deme Alopece", certainty: 0.5, cites: [{source: S6, locator: "§1.a.i"}, {source: S3, locator: "§3"}], how_known: "IEP; SEP deme."}
  schooling:
    - {value: "Formal literacy / elementary education typical of Athenian males; later acquaintance with Anaxagoras's books", stage: "grammar or secondary school", run_by: "other", certainty: 0.5, cites: [{source: S3, locator: "§3"}, {source: S6, locator: "§1.a.i"}], how_known: "SEP on widespread male literacy; Phaedo 98b via SEP on Anaxagoras scrolls."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "As a youth eager for Anaxagoras's books (scrolls), per Plato Phaedo 98b as reported in SEP", certainty: 0.5, cites: [{source: S3, locator: "§3"}], how_known: "SEP chronology; Plato's report, not own writing (P42)."}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [Ancient Greek], certainty: 0.7, cites: [{source: S3, locator: "§3"}], how_known: "Athens."}
  notable_events:
    - {value: "Dokimasia / citizenship enrollment at about eighteen; military service as hoplite (Potidaea, Delium, Amphipolis)", year: UNKNOWN, certainty: 0.5, cites: [{source: S3, locator: "§3"}, {source: S6, locator: "§1.a.i"}], how_known: "SEP chronology; IEP battles. Years approximate."}

worldview:
  unit: "adult working worldview"
  working_years: {value: UNKNOWN, how_known: "Equals timing.major_work_period (UNKNOWN, P39)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "He wrote nothing; Plato's Apology has him deny studying the heavens as charged (character speech)."}
  primary_system: {value: UNKNOWN, how_known: "No listed code fits contested historical Socratic piety. HELLEN is modern Greek reconstructionist paganism (systems/HELLEN.md), not classical civic cult. He wrote nothing; Plato/Xenophon are reported speech (P42). Scholars reconstruct belief in gods and a daimonion (S5, S6) but disagree on how far his theology matches traditional Athenian gods (Socratic problem, S3). Not scored to a system."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: HELLEN, reason: "Lead: Athenian civic polytheism and cult practice (S6). Rejected: HELLEN labels modern reconstructionist paganism, not fifth-century Athens."}
    - {code: PLATO, reason: "Lead: views known mainly through Plato. Rejected: PLATO is Plato's own system; Vlastos and others separate early Socratic from middle Platonic doctrines (S3)."}
  lio_axes:
    A_locus:
      value: 0
      basis: scholarly_reconstruction
      certainty: 0.5
      support: corroborated
      cites: [{source: S5, locator: "§1 Socrates paragraph"}, {source: S6, locator: "§1.a.ii Greek Religion and Socrates' Impiety"}, {source: S7, locator: "31d; 21a; 40a (illustrative reported speech)"}]
      how_known: "P49: scholars' reconstructions score at most 0.5. He wrote nothing; Apology wording is Plato's character speech / reported speech (P42) and cannot score alone. Two independent scholarly reconstructions (SEP Religion and Morality; IEP Socrates) attribute to the historical Socrates belief in gods, observance, objection to the charge of not believing in the city's gods, a childhood daimonion that holds him back, and a mission under Apollo's Delphic oracle. Fowler Loeb Apology (S7) illustrates; scores rest on S5+S6."
      rationale: "Interventionist pole (A 0): personal divinities who act — daimonion as a sort of voice from childhood that opposes actions; Delphic oracle / Apollo's charge; life as service to god; gods invited his death when the sign did not oppose (S5, S6, S7). Named alternative: 1 (leans interventionist) — he rejects Homeric stories that attribute immorality to the gods and holds divinity to be good, truthful, and rational (S5, S6), a reformed theology that still keeps personal intervening gods. Not A ≥ 3: he is not an atheist on these reconstructions. Certainty stays 0.5 (scholarly_reconstruction ceiling + Socratic problem)."
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30; lasting contribution is method/ethics, not a theory of physical systems). Plato's Socrates denies studying the heavens (Apology; S6). Xenophon Memorabilia 1.4 teleological 'maker' argument is often treated as Xenophon's and is not used here (P42; S6 notes Plato's Timaeus craftsman is Timaeus, not Socrates). No source read gives a scholarly consensus reconstruction of a P16 exceptionless natural-order claim for the historical Socrates (P49 not stretched)."}
    C_ledger: {value: UNKNOWN, how_known: "Afterlife options in Apology (dreamless sleep vs converse with the dead) and Phaedo immortality are dialogue theology; not scored for historical Socrates without a firm P49 reconstruction this pass."}
    D_authority: {value: UNKNOWN, how_known: "Euthyphro and Apology raise piety and divine command themes; not scored this pass."}
    E_scope: {value: UNKNOWN, how_known: "Not read (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "A 0 at 0.5 would lean A ≤ 1, but B_cause is UNKNOWN, which takes precedence (P19)."}
  statements:
    - text: "…at many times and places, is that something divine and spiritual comes to me, the very thing which Meletus ridiculed in his indictment. I have had this from my childhood; it is a sort of voice that comes to me, and when it comes it always holds me back from what I am thinking of doing, but never urges me forward."
      cites: [{source: S7, locator: "31d"}]
      date: "-399"
      context: "Plato, Apology 31d (Fowler Loeb). Character speech in Plato; illustrates the daimonion that S5/S6 attribute to the historical Socrates. Dramatic date of the trial: 399 BCE."
      axes: [A_locus]
      kind: "reported speech"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "P42: not own words. Score rests on scholarly reconstruction (P49), not on this quotation alone."
    - text: "Well, once he went to Delphi and made so bold as to ask the oracle this question… for he asked if there were anyone wiser than I. Now the Pythia replied that there was no one wiser."
      cites: [{source: S7, locator: "21a"}]
      date: "-399"
      context: "Plato, Apology 21a (Fowler Loeb). Chaerephon's report of the Delphic oracle; Socrates takes it as assigning his examining mission (S5)."
      axes: [A_locus]
      kind: "reported speech"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "As above."
    - text: "…the greatest of evils has come upon me; but the divine sign did not oppose me."
      cites: [{source: S7, locator: "40a"}]
      date: "-399"
      context: "Plato, Apology 40a (Fowler Loeb). Socrates reads the silence of the daimonion as divine invitation regarding his death (S5)."
      axes: [A_locus]
      kind: "reported speech"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "As above."
  changes_over_life: []
  coder_notes: "Coder's call. P49 used for A only. Did not stretch P49 to B from Xenophon Mem. 1.4 or Aristophanes Clouds caricature. Impiety charge is the accusers' claim (S1); Britannica Top Questions AI box not cited. No fallacy_catalog (Jason)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Athenian", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "Birth and early life"}], how_known: "Britannica; Wikipedia."}
  religious_heritage_by_birth: {value: "Athenian civic polytheism", certainty: 0.5, cites: [{source: S3, locator: "§3"}, {source: S6, locator: "§1.a.ii"}], how_known: "Civic cult context (0.5)."}
  baptism_or_initiation: {value: "Phratry presentation and deme dokimasia (civic, not baptism)", certainty: 0.5, cites: [{source: S3, locator: "§3"}], how_known: "SEP chronology."}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "Undated (P39)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "Undated (P39)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No dated own text; reconstructions place daimonion from childhood and the oracle mission in adult life, but years unknown."}
  lio_views_relative_to_major_work: {value: "unclear", certainty: 0.5, cites: [{source: S5, locator: "§1"}, {source: S3, locator: "§2"}], how_known: "Working views reconstructed for adult life; major work undated (P39)."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "primary_system UNKNOWN; A scored only via P49 reconstruction."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Wrote nothing; method is elenchus / conversation, not geometric demonstration (S1, S3).", certainty: 0.5, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "opening"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Not known."}
  circle_present: {value: "yes", rationale: "Reconstructed belief in gods who guide (daimonion, oracle) and to whom life is owed (S5, S6).", certainty: 0.5, cites: [{source: S5, locator: "§1"}, {source: S6, locator: "§1.a.ii"}], how_known: "Lane B reading of P49 reconstructions; not a finding."}
  reading: "Reconstructed Socratic piety: personal intervening gods; A 0 @0.5; B UNKNOWN; unplotted."
  notes: "Lane B only. Chart-moving NO."

institutions: []
collaborators:
  - {value: "Plato", relation: "student or assistant", certainty: 0.7, cites: [{source: S1, locator: "'Philosophical and literary sources'"}, {source: S3, locator: "§2.1"}], how_known: "Member of his circle."}
  - {value: "Xenophon", relation: "student or assistant", certainty: 0.7, cites: [{source: S1, locator: "'Xenophon'"}, {source: S3, locator: "§2.1"}], how_known: "Member of his circle."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 73"}], how_known: "Study roster."}
  controversies:
    - {value: "Socratic problem: which dialogues convey the historical Socrates", certainty: 0.7, cites: [{source: S1, locator: "'Philosophical and literary sources'"}, {source: S3, locator: "§2"}], how_known: "Britannica; SEP."}
    - {value: "Reconstruction of Socratic religion: McPherran 1996 is the standard monograph; pages not scored this pass", certainty: 0.5, cites: [{source: S8, locator: "title / SEP bibliography pointer"}, {source: S3, locator: "bibliography"}], how_known: "Pointer only (S8); not a warrant for A."}
  data_quality_flags:
    - "No own writings; all dialogue evidence is reported speech / character speech (P42)."
    - "A scored only via scholarly reconstruction (P49), certainty 0.5."
  open_questions:
    - "Optional: McPherran The Religion of Socrates (1996) monograph pages for a tighter P49 reconstruction (may confirm A or refine alt)."
    - "Optional: Xenophon Memorabilia 1.1 and Apology on sacrifices — only if a source read attributes the piety claims to the historical Socrates without treating them as Xenophon's apology alone."
    - "B remains blocked unless a P16 nature-order reconstruction for historical Socrates appears (unlikely)."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Richard Kraut"
    citation: "Kraut, Richard. \"Socrates.\" Encyclopaedia Britannica, updated 29 August 2026. https://www.britannica.com/biography/Socrates."
    url: "https://www.britannica.com/biography/Socrates"
    accessed: 2026-10-24
    reliability_note: "Signed body through 'Xenophon'; Top Questions not cited. Live fetch sometimes thin; create-pass body retained."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, worldview, heritage, timing, lane_b, collaborators, review]
  - id: S2
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S3
    type: secondary
    kind: encyclopedia
    author: "Debra Nails"
    citation: "Nails, Debra. \"Socrates.\" Stanford Encyclopedia of Philosophy, first published 16 September 2005, substantive revision 26 May 2022. https://plato.stanford.edu/entries/socrates/."
    url: "https://plato.stanford.edu/entries/socrates/"
    accessed: 2026-10-24
    reliability_note: "Signed scholarly entry; Socratic problem and chronology."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, heritage, timing, collaborators, review, worldview]
  - id: S4
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. \"Socrates.\" Wikipedia, English. https://en.wikipedia.org/wiki/Socrates."
    url: "https://en.wikipedia.org/wiki/Socrates"
    accessed: 2026-10-24
    reliability_note: "P50 dual bio with Britannica. Parents, trial, religion/daimonion sections; not sole warrant for A."
    source_quality: "reference entry"
    used_for: [identity, basics, childhood, heritage]
  - id: S5
    type: secondary
    kind: encyclopedia
    author: "John Hare and others (SEP entry)"
    citation: "Hare, John. \"Religion and Morality in Western Philosophy.\" Stanford Encyclopedia of Philosophy, first published 27 September 2006, substantive revision 25 September 2024. §1 Ancient Greek Philosophy, Socrates paragraph. https://plato.stanford.edu/entries/religion-morality/."
    url: "https://plato.stanford.edu/entries/religion-morality/"
    accessed: 2026-10-24
    reliability_note: "Signed SEP entry reconstructing Socrates' piety (not atheist; observant; daimonion; Apollo's charge). Used as P49 scholarly reconstruction for A."
    source_quality: "scholarly reconstruction"
    used_for: [worldview, lane_b]
  - id: S6
    type: secondary
    kind: encyclopedia
    author: "James M. Ambury"
    citation: "Ambury, James M. \"Socrates.\" Internet Encyclopedia of Philosophy. https://iep.utm.edu/socrates/."
    url: "https://iep.utm.edu/socrates/"
    accessed: 2026-10-24
    reliability_note: "Signed IEP entry; §1.a.ii on Greek religion, impiety, daimonion, and reformed conception of divinity. Independent of S5 for P48 corroboration."
    source_quality: "scholarly reconstruction"
    used_for: [basics, childhood, heritage, worldview, lane_b]
  - id: S7
    type: primary
    kind: scholarly edition
    author: "Plato; trans. Harold North Fowler"
    citation: "Plato. Apology. Translated by Harold North Fowler. Plato in Twelve Volumes, Vol. 1. Cambridge, MA: Harvard University Press; London: William Heinemann, 1966. Read on Perseus Digital Library (Stephanus sections 21a, 26b, 31d, 40a)."
    url: "https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0170:text=Apol."
    accessed: 2026-10-24
    reliability_note: "Loeb Classical Library scholarly English. Character speech / reported speech about Socrates (P42); illustrative only for A. Greek text available on Perseus in parallel."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview]
  - id: S8
    type: secondary
    kind: encyclopedia
    author: "Mark L. McPherran (cited via SEP bibliography / Wikipedia Religion section)"
    citation: "McPherran, Mark L. The Religion of Socrates. University Park: Pennsylvania State University Press, 1996. Noted in SEP Socrates bibliography (S3) and Wikipedia Socrates §Religion; monograph pages not borrowed this pass."
    url: "https://plato.stanford.edu/entries/socrates/"
    accessed: 2026-10-24
    reliability_note: "Standard monograph on Socratic religion; used only as a pointer in open_questions, not as a warrant for scores this pass (pages unread)."
    source_quality: "scholarly edition or monograph"
    used_for: [review]
---

# Socrates

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Socrates (c. 470–399 BCE), Athenian philosopher who wrote nothing [S1, S3, S4]. Deepen D1: primary_system UNKNOWN; **A 0 at 0.5** (scholarly_reconstruction, P49; alt 1; corroborated S5+S6); B UNKNOWN; mid_basin UNKNOWN. Not plotted. Chart-moving NO.

## Life and work

Athens, deme Alopece; parents Sophroniscus and Phaenarete [S3, S4, S6]. Tried for impiety and corrupting the youth; executed 399 BCE [S1, S3, S4].

## Contribution and impact

Socratic questioning known through Plato and Xenophon [S1, S3].

## Childhood and education

Athenian civic polytheism context; phratry / dokimasia [S3, S6]. Hoplite service [S3, S6].

## Adult working worldview

No own writings (P42). P49 reconstructions (S5, S6): believed in gods; observant; daimonion; Apollo's oracle mission; rejected Homeric immoral myths but not the gods. Illustrative Apology (Fowler Loeb) 21a, 31d, 40a [S7]. B not scored.

## Heritage (context only)

Athenian; civic polytheism by birth [S1, S3, S6].

## Timing

Undated (P39) [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Circle present on P49 reading; geometric form no [S5, S6].

## Open questions

- McPherran 1996 page check.
- Xenophon Mem. 1.1 only with clear historical attribution.
- B blocked without a P16 nature-order reconstruction.

## Research log

- 2026-10-15: Read Britannica (Kraut) opening through 'Xenophon'.
- 2026-10-24 (D1): SEP Socrates (Nails); Wikipedia dual bio; SEP Religion and Morality §1 Socrates; IEP Ambury §1.a.ii; Fowler Loeb Apology 21a/26b/31d/40a via Perseus. A → 0 @0.5 (P49); B UNKNOWN; chart-moving NO. No fallacy_catalog.
