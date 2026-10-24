---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch F)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch F, order P32: F 5, rank 36). Basics from Britannica (Wesley D. Smith). No text can be shown to be by Hippocrates himself: the Hippocratic Corpus 'cannot be by one person' and most of it 'not written by him' (S1). On the Sacred Disease (natural cause of epilepsy) is quoted for context but not attributed to him. His own disease theory is known only from Meno's report (reported speech). primary_system and A UNKNOWN; B BELOW_THRESHOLD; C, D, E UNKNOWN; mid_basin UNKNOWN. Undated works (P39). Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #36, F5 rank 36). Needs: A UNKNOWN; B BELOW_THRESHOLD. Re-opened Britannica Smith (S1); verified Sacred Disease against W. H. S. Jones Loeb vol. 2 OCR (S2; Adams MIT web copy retained as parallel). New: IEP Boylan (S4); Jouanna 'Hippocrates and the Sacred' Brill ch. (S5) + Exeter historiographical PDF quoting Jouanna Hippocrates JHUP 1999 (S6). P47 source_quality on every source. P42 reaffirmed: Jouanna allows that some Corpus works might reasonably be his 'without having absolute criteria'; scholars agree Sacred Disease and Airs, Waters, Places share one anonymous author, not that that author is the historical Hippocrates — so Sacred Disease stays context only and scores nothing. Meno/Anonymus Londinensis disease theory remains reported speech (§7). A stays UNKNOWN; B stays BELOW_THRESHOLD. Childhood/heritage lightly filled (Asclepiad family). Chart: still unplotted. No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: hippocrates
  display_name: "Hippocrates"
  roster:
    canonical_name: "Hippocrates"
    rank: 36
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: medicine
    field_bucket: medicine
  full_name: {value: "Hippocrates of Cos", certainty: 0.7, cites: [{source: S1, locator: "opening ('the Asclepiad of Cos', Plato)"}], how_known: "Britannica."}
  native_name: {value: "Ἱπποκράτης (Hippokratēs)", certainty: 0.5, cites: [{source: S4, locator: "title / opening"}], how_known: "Standard Greek form; IEP and scholarly convention. Not printed in Greek letters in S1."}
  aliases:
    - {name: "Hippocrates-of-Cos", kind: "roster alias"}
    - {name: "Hippocrates-Cos", kind: "other"}

basics:
  birth:
    date: {value: "-460", approx: true, calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "opening; 'Life and works'"}, {source: S4, locator: "title dates c. 450–c. 380"}], how_known: "Britannica: 'c. 460 bce'; dates 'are traditional but may well be approximately accurate' (0.5). IEP gives a slightly different traditional window."}
    place: {value: "Cos, Greece", modern_name: "Kos, Greece", polity_then: "Cos (Greek island polis)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; Plato calls him 'the Asclepiad of Cos'."}
  death:
    date: {value: "-375", approx: true, calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "opening; 'Life and works'"}], how_known: "Traditional date (0.5)."}
    place: {value: "Larissa, Thessaly", modern_name: "Larissa, Greece", polity_then: "Thessaly", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; later lives are 'largely traditional or imaginative' (0.5)."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "No listed contribution can be dated (P39)."}
  era_bucket: {value: "-500 to 499", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Every adult year on the traditional dates (c. 442–375 BCE) falls in '-500 to 499' (P39), at the certainty of the life dates (0.5)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Greece (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.5, cites: [{source: S1, locator: "'Life and works'"}], how_known: "Travelled 'in Greece and Asia Minor'; Cos as base (0.5)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [Greek], certainty: 0.7, cites: [{source: S1, locator: "'Life and works' (earliest Greek prose)"}], how_known: "Britannica."}
  occupations: {value: ["physician", "teacher of medicine"], certainty: 0.7, cites: [{source: S1, locator: "'Life and works'"}], how_known: "Britannica (Plato: taught students for fees)."}

contribution:
  fields: {value: ["medicine"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Theory of disease causation: undigested residues from unsuitable diet give off vapours that cause disease (reported by Meno)", year: UNKNOWN, kind: theory, lasting: "Hippocrates as the inspirational source for later medicine (S1); the specific theory is historical", certainty: 0.5, cites: [{source: S1, locator: "'Life and works' (Meno)"}], how_known: "Known only from Meno's history of medicine, as summarised by Britannica; undated. Reported speech under §7 / P42 — listed as contribution history, not used to score B alone."}
    - {value: "Practice and teaching of medicine at Cos, shaping the ideals and ethics of the physician", year: UNKNOWN, kind: "body of work", lasting: "'a permanent influence on the development of medicine and on the ideals and ethics of the physician' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Life and works'"}], how_known: "Britannica. The Oath is probably not his (S1)."}
  evidence_of_impact:
    - {value: "Called 'the Great Physician' (Aristotle, Politics); claimed as origin by later schools and by Galen", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S1, locator: "'Life and works'; 'Influence'"}], how_known: "Britannica."}
    - {value: "Named by Plato (Protagoras; Phaedrus) as a famous Asclepiad of Cos who taught for fees and had a philosophical approach to medicine", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S1, locator: "'Life and works'"}, {source: S5, locator: "opening (Protagoras and Phaedrus attest fame in his lifetime)"}], how_known: "Britannica and Jouanna."}
  major_works: []
  honours: []
  definition_fit: {value: "arguable", rationale: "Real and admired, but his own contributions cannot be separated from the Corpus (S1, S4, S5).", certainty: 0.5, cites: [{source: S1, locator: "'Life and works'"}, {source: S4, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Britannica: 'Asclepiad' means a family of physicians, not a temple priest; nothing on household cult. Legendary descent from Asclepius is family lore (S5/S6), not scored as childhood religion."}
  family_religious_practice: {value: UNKNOWN, how_known: "Nothing in the sources read."}
  parents_and_household:
    - {value: "A family that had produced well-known physicians for generations (an 'Asclepiad' of Cos)", role: family, certainty: 0.7, cites: [{source: S1, locator: "'Life and works'"}, {source: S5, locator: "opening (Asclepiad family of Cos)"}], how_known: "Britannica's reading of Plato; Jouanna concurs on Asclepiad family."}
  household_circumstances: {value: UNKNOWN, how_known: "Nothing in the sources read."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "Nothing."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Nothing."}
  early_science_exposure:
    - {value: "Raised in a multi-generation physicians' (Asclepiad) family on Cos", certainty: 0.7, cites: [{source: S1, locator: "'Life and works'"}], how_known: "Britannica."}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [Greek], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Born on Cos; Ionian Greek of the later Corpus is the language of the tradition, not a documented childhood fact."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: UNKNOWN, how_known: "Undated works (P39)."}
  nominal_affiliations:
    - {value: "Asclepiad of Cos (physicians' family; not a temple priest)", role: other, certainty: 0.7, cites: [{source: S1, locator: "'Life and works'"}], how_known: "Plato via Britannica; affiliation/heritage, not a worldview code."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No text of his own identified under P42 (S1, S4, S5). Corpus Sacred Disease (context only) argues natural causes while holding all diseases 'divine and human' alike — not attributed to him."}
  primary_system: {value: UNKNOWN, how_known: "No statement of his own under P42. The Corpus cannot be by one person and most of it was not written by him (S1); Jouanna: some works might reasonably be his 'without having absolute criteria' to identify them (S5) — that is not scholarly attribution of a specific text. HELLEN rejected as modern reconstructionist code."}
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: HELLEN, reason: "Modern reconstructionist code; not for ancient Greeks by default. Rejected.", cites: [{source: S1, locator: "text"}]}
    - {code: ATHE, reason: "Rejected: even On the Sacred Disease (not attributable to him under P42) still calls all diseases 'divine' as well as 'human' (S2).", cites: [{source: S2, locator: "closing ('they are all divine and all human')"}]}
    - {code: EMPIR, reason: "Rejected as a scored primary_system: Corpus empiricism/naturalism (Sacred Disease, Epidemics tradition) is authorial tradition under P42, not his own words.", cites: [{source: S4, locator: "biomedical methodology"}, {source: S5, locator: "Corpus plurality"}]}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "P19 researched silent / P42: nothing in words attributable to him. Sacred Disease's 'all divine and all human' is context only (author unknown). Plato and Meno say nothing on where God is. Named alternative: BELOW_THRESHOLD if a later source attributes a specific locus-bearing treatise to him with scholarly agreement.", note: "Blockers: Jouanna Budé / full JHUP Hippocrates page-check for any treatise he names as Hippocrates' own; Anonymus Londinensis Greek of Meno's report."}
    B_cause: {value: BELOW_THRESHOLD, how_known: "Scientist candidate under P30 (Meno reports a disease-causation theory), but that theory is known only from Meno's summary — reported speech, cannot score alone (§7, P42). On the Sacred Disease states natural causes for epilepsy and uniformity of nature, but its author is unknown: scholars pair it with Airs, Waters, Places as one anonymous hand, not as the historical Hippocrates (S1, S5, S6). Context only; scores nothing (P42). Named alternative: B 3 @ 0.5 if a specific treatise were attributed to him (P35 working science) or if Sacred Disease were so attributed.", note: "P42 was decided on this record (OPEN_DECISIONS 2026-10-15); deepen finds no new specific attribution that would lift B."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing attributable to him."}
    D_authority: {value: UNKNOWN, how_known: "Nothing attributable to him."}
    E_scope: {value: UNKNOWN, how_known: "Nothing in words attributable to him (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, which takes precedence (§6, P19)."}
  statements:
    - text: "I am about to discuss the disease called \"sacred.\" It is not, in my opinion, any more divine or more sacred than other diseases, but has a natural cause, and its supposed divine origin is due to men's inexperience, and to their wonder at its peculiar character."
      cites: [{source: S2, locator: "ch. I opening (Jones Loeb vol. 2)"}]
      date: "-400"
      context: "Opening of On the Sacred Disease (Hippocratic Corpus), on epilepsy. Author unknown; not attributed to the historical Hippocrates under P42 (S1, S5). Context only; not used to score."
      axes: [B_cause]
      kind: "other"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "W. H. S. Jones, Hippocrates vol. 2 (Loeb Classical Library, 1923), English; Archive.org OCR hippocrates02hippuoft this pass. Adams MIT web copy (prior pass) has the same sense with a transcription slip ('from the originates'). Date '-400' is conventional for the treatise, not a documented date for Hippocrates. P42: scores nothing."
    - text: "they are all divine and all human. Each has a nature and power of its own; none is hopeless or incapable of treatment."
      cites: [{source: S2, locator: "near end (Jones; 'all divine and all human')"}]
      date: "-400"
      context: "Same treatise, near the end: all diseases divine and human alike; natural causes (cold, sun, winds). Context only under P42."
      axes: [A_locus, B_cause]
      kind: "other"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Jones Loeb English via Archive OCR; Adams has 'all are divine, and all human.' Same P42 caveat."
  changes_over_life: []
  coder_notes: "Deepen D1: P42 still blocks Corpus scoring. Jouanna (S5) explicitly: some writings might reasonably be Hippocrates' without absolute criteria to identify them — fails P42's 'source attributes that specific text' / scholarly-agreement bar. Sacred Disease + Airs, Waters, Places = one anonymous author (scholarly consensus noted in S5/S6 secondary literature), not historical Hippocrates. Meno remains reported speech. A UNKNOWN; B BELOW_THRESHOLD. Chart unplotted."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Greek (Cos)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Asclepiad family lore includes legendary descent from Asclepius (S5/S6), but Britannica stresses Asclepiad = physicians' family, not temple priesthood. Not enough for a scored heritage label beyond UNKNOWN.", note: "Heritage only — never a worldview code."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "N/A (ancient Greek)."}
  childhood_catechism: {value: UNKNOWN, how_known: "Nothing."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "Undated works (P39)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "Undated works (P39)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement attributable to him under P42."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S1, locator: "'Life and works'"}, {source: S5, locator: "opening (no absolute criteria for attribution)"}], how_known: "No text of his own under P42."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Nothing attributable under P42."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Nothing on his mathematical training. Plato's Phaedrus remark (philosophical approach to medicine) is too thin for form (S1).", certainty: 0.5, cites: [{source: S1, locator: "'Life and works'"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Life and works'"}], how_known: "Nothing."}
  circle_present: {value: "unclear", rationale: "No text of his own. Sacred Disease's 'all divine and all human' is context only (P42).", certainty: 0.5, cites: [{source: S2, locator: "closing"}, {source: S1, locator: "'Life and works'"}], how_known: "Coder's reading."}
  reading: "As belief, not finding: form and circle unclear. Worldview unplottable (A UNKNOWN; B BELOW). H1 not tested. Corpus naturalism is tradition-context, not his scored view."
  notes: "P42 authorial-tradition case (with Homer)."

institutions: []
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 36"}], how_known: "Study roster."}
  controversies:
    - {value: "Authorship of the Hippocratic Corpus and the Oath: most works not by him; the Oath probably not; no absolute criteria to identify which (if any) are his (S1, S5)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Life and works'"}, {source: S5, locator: "opening"}], how_known: "Britannica and Jouanna."}
  data_quality_flags:
    - "Life dates traditional; later lives largely imaginative (S1)."
    - "P42: Corpus texts and Meno doxography cannot score axes; deepen found no new specific attribution."
    - "Sacred Disease statements verified in Jones Loeb OCR (Archive); print Loeb page-check pending."
  open_questions:
    - "Page-check Jouanna, Hippocrates (JHUP 1999 / Fayard 1992) and Budé La maladie sacrée for any treatise he names as Hippocrates' own with criteria that would meet P42."
    - "Read Anonymus Londinensis (Meno) Greek/English for the disease-theory report beyond Britannica's summary."
    - "Edelstein Ancient Medicine; Smith The Hippocratic Tradition (full) for any minority attribution of Sacred Disease to the historical Hippocrates."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Wesley D. Smith"
    citation: "Smith, Wesley D. \"Hippocrates.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Hippocrates."
    url: "https://www.britannica.com/biography/Hippocrates"
    accessed: 2026-10-24
    reliability_note: "Signed article by a Hippocratic scholar; Q&A header not used."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, review]
  - id: S2
    type: primary
    kind: other
    author: "Hippocratic Corpus (author unknown); trans. W. H. S. Jones"
    year: 1923
    citation: "On the Sacred Disease. Trans. W. H. S. Jones. In Hippocrates, vol. 2, Loeb Classical Library. Cambridge, MA: Harvard University Press, 1923. Archive.org OCR: hippocrates02hippuoft. Parallel: Francis Adams, The Genuine Works of Hippocrates (Sydenham Society, 1849), MIT Internet Classics Archive."
    url: "https://archive.org/stream/hippocrates02hippuoft/hippocrates02hippuoft_djvu.txt"
    accessed: 2026-10-24
    reliability_note: "Scholarly Loeb translation (OCR); treatise author unknown — not the historical Hippocrates on current scholarship (S1, S5). Tradition only. Used for context quotations under P42."
    source_quality: "archive scan (OCR only)"
    used_for: [worldview, lane_b]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S4
    type: secondary
    kind: encyclopedia
    author: "Michael Boylan"
    citation: "Boylan, Michael. \"Hippocrates.\" Internet Encyclopedia of Philosophy. https://iep.utm.edu/hippocra/."
    url: "https://iep.utm.edu/hippocra/"
    accessed: 2026-10-24
    reliability_note: "Signed IEP entry; stresses Corpus plurality and conventional 'Hippocrates' label."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, worldview]
  - id: S5
    type: secondary
    kind: book chapter
    author: "Jacques Jouanna"
    year: 2012
    citation: "Jouanna, Jacques. \"Hippocrates and the Sacred.\" In Greek Medicine from Hippocrates to Galen: Selected Papers, 97–118. Leiden: Brill, 2012. https://doi.org/10.1163/9789004232549_007 (chapter text read via publisher/search extract this pass)."
    url: "https://doi.org/10.1163/9789004232549_007"
    accessed: 2026-10-24
    reliability_note: "Leading Hippocratic philologist; states some Corpus writings might reasonably be Hippocrates' without absolute criteria; Sacred Disease as polemic against magico-religious medicine within Corpus rationalism, not a personal confession of the Cos physician."
    source_quality: "scholarly edition or monograph"
    used_for: [contribution, childhood, worldview, heritage, timing, review]
  - id: S6
    type: secondary
    kind: journal article
    author: "Vivian Nutton (historiographical survey citing Jouanna); Centre for Medical History, University of Exeter PDF"
    year: 2012
    citation: "Historiographical survey PDF, Centre for Medical History, University of Exeter: \"What does 'Hippocrates' mean? The Historiographical Construction of the Greek physician as the 'Father of Medicine'\" (quotes Jouanna, Hippocrates, JHUP 1999, on Corpus plurality: not all by one man; fewer than twenty from Hippocrates and close disciples as a Cos group). https://www.exeter.ac.uk/v8media/universityofexeter/collegeofhumanities/history/researchcentres/centreformedicalhistory/pdfsanddocs/3_-_The_Historiographical_Construction_of_Hippocrates_as_the_Father_of_Medicine.pdf"
    url: "https://www.exeter.ac.uk/v8media/universityofexeter/collegeofhumanities/history/researchcentres/centreformedicalhistory/pdfsanddocs/3_-_The_Historiographical_Construction_of_Hippocrates_as_the_Father_of_Medicine.pdf"
    accessed: 2026-10-24
    reliability_note: "Open PDF surveying Jouanna and others; used for Jouanna page citations on Corpus composition, not as independent A/B evidence."
    source_quality: "scholarly reconstruction"
    used_for: [worldview, heritage, review]
---

# Hippocrates

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Hippocrates of Cos (c. 460–c. 375 BCE), Greek physician, traditionally the father of medicine [S1]. No surviving text can be shown to be his under P42 [S1, S4, S5]. Deepen D1: primary_system and A UNKNOWN; B BELOW_THRESHOLD; mid_basin UNKNOWN. Chart still unplotted.

## Life and work

Admired physician and teacher in his lifetime, named by Plato and Aristotle; travelled in Greece and Asia Minor [S1, S5].

## Contribution and impact

Meno reports his theory that residues of bad diet give off disease-causing vapours [S1] — reported speech, not a scored B. The Corpus was assembled later at Alexandria and is not his alone [S1, S4, S5].

## Childhood and education

From an Asclepiad physicians' family of Cos (not temple priests) [S1, S5]. Family religion otherwise unknown.

## Adult working worldview

**Lane A.** Nothing attributable under P42. Sacred Disease's "all divine and all human" is Corpus context only [S2]. A UNKNOWN.

**Lane B (separate).** Scientist candidate via Meno's disease theory, but doxography cannot score alone. Sacred Disease naturalism (Jones Loeb) belongs to an anonymous author paired with *Airs, Waters, Places*, not the historical Hippocrates [S1, S5, S6]. B BELOW_THRESHOLD.

## Heritage (context only)

Greek, from Cos [S1]. Asclepiad lore (legendary Asclepius descent) not scored as religious heritage.

## Timing

Undated (P39) [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form and circle unclear. H1 not tested. P42 authorial-tradition case.

## Open questions

- Jouanna JHUP/Budé page-check for any specific treatise attributed to him.
- Anonymus Londinensis (Meno) full text.
- Edelstein; Smith *Hippocratic Tradition* full.

## Research log

- 2026-10-15: Read Britannica (W. D. Smith) and the Adams translation of On the Sacred Disease (MIT web copy).
- 2026-10-24 (D1): Jones Loeb OCR for Sacred Disease; IEP Boylan; Jouanna Brill chapter extract; Exeter PDF on Jouanna/Corpus. P42 reaffirmed. A UNKNOWN→UNKNOWN; B BELOW→BELOW. Chart-moving no.
