---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z8; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to mathematics. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #158, F 3, rank 166). Needs: hunt own-voice; keep UNKNOWN if silent; do not force plot. Read Dupuy 1896 (Wikisource full text / NUMDAM ASENS; S3): mother Adélaïde-Marie remained a lifelong professing Christian who reduced religion to a moral envelope — MacTutor's 'imparted her own scepticism' is a tertiary paraphrase that contradicts Dupuy, so the AGNOS lead is weakened, not confirmed. Own letter to Chevalier of 25 May 1832 rejects Saint-Simonian 'conversion' efforts ('la vanité de tes efforts'); not a statement about God (Z8 lead kept, now with Dupuy quote). Deathbed refusal of a priest is Dupuy/Wikipedia reported account, not own words — cannot score (CODING_GUIDE §1 / reported speech). 'Je prends le ciel à témoin' in the 29 May farewell is a figurative oath, not theology. No own-voice locus, nature-order, or afterlife statement found. Not a scientist (P30 pure algebra). primary/A/B/C/D/E/mid stay UNKNOWN; not plotted. P50 Wikipedia dual bio (S4). P47 source_quality on S1–S4. Chart-moving NO. No fallacy_catalog. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z8 audit fix (v8's call on the auditor's advice): 1832 Chevalier letter added as a non-scoring lead in coder_notes. Values unchanged."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z8, order P32: F 3, rank 166). Source: MacTutor biography (O'Connor and Robertson, signed). No own words on religion found; MacTutor says his mother taught him religion and 'imparted her own scepticism to her son' (the biographers' words, not his). Not a scientist (pure algebra; Knuth, Tao, Noether-algebra precedents; P30). primary_system UNKNOWN (lead AGNOS from the mother's scepticism); A, B, C, D, E UNKNOWN; mid_basin UNKNOWN. Span 1829–1832, age 18. Not plotted. Draft, not reviewed."}

identity:
  id: galois-evariste
  display_name: "Évariste Galois"
  roster:
    canonical_name: "Évariste Galois"
    rank: 166
    F: 3
    models: [Claude, Gemini, Grok]
    band: "core (3–4)"
    status: "core"
    field: "mathematics"
    field_bucket: "mathematics"
  full_name: {value: "Évariste Galois", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}, {source: S4, locator: "lead / infobox"}], how_known: "MacTutor and Wikipedia agree (P50)."}
  native_name: {value: "Évariste Galois", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}, {source: S4, locator: "lead"}], how_known: "MacTutor and Wikipedia agree (P50)."}
  aliases:
    - {name: "Galois-Évariste", kind: "roster alias"}

basics:
  birth:
    date: {value: "1811-10-25", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}, {source: S4, locator: "infobox"}], how_known: "MacTutor and Wikipedia agree (P50)."}
    place: {value: "Bourg-la-Reine", modern_name: "Bourg-la-Reine, France", polity_then: "First French Empire / Kingdom of France", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}, {source: S4, locator: "infobox"}], how_known: "MacTutor and Wikipedia agree (P50)."}
  death:
    date: {value: "1832-05-31", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}, {source: S4, locator: "infobox"}], how_known: "MacTutor and Wikipedia agree (P50)."}
    place: {value: "Paris", modern_name: "Paris, France", polity_then: "July Monarchy (France)", certainty: 0.7, cites: [{source: S1, locator: "Quick Info; Biography"}, {source: S4, locator: "Death"}], how_known: "Hôpital Cochin after the duel; MacTutor and Wikipedia agree (P50)."}
  first_lasting_contribution_year: {value: 1829, certainty: 0.5, cites: [{source: S1, locator: "Biography"}], how_known: "Articles on the algebraic solution of equations submitted to the Académie on 25 May and 1 June 1829; those versions are lost, later versions 1830 and 1831, so 0.5."}
  era_bucket: {value: "1750 to 1849", certainty: 1.0, cites: [{source: S1, locator: "Biography"}], how_known: "1829 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}], how_known: "France (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Paris."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["French"], certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "French papers."}
  occupations: {value: ["mathematician"], certainty: 0.7, cites: [{source: S1, locator: "Summary"}], how_known: "MacTutor."}

contribution:
  primary_domain: mathematics
  fields: {value: ["algebra", "group theory"], certainty: 0.7, cites: [{source: S1, locator: "Summary"}], how_known: "MacTutor."}
  lasting_original_contributions:
    - {value: "Galois theory: solubility of equations by radicals, early group theory", year: 1829, kind: "theory", lasting: "'The theory that Galois outlined in these papers is now called Galois theory'; Liouville: 'as correct as it is deep' (S1)", certainty: 0.5, cites: [{source: S1, locator: "Biography (Liouville, 1843–46)"}], how_known: "MacTutor; worked on from 1829 to the letter of 29 May 1832 (range 1829–1832; P12 start). Published by Liouville in 1846."}
  evidence_of_impact:
    - {value: "Famous for his development of early group theory", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Summary"}], how_known: "MacTutor."}
  major_works:
    - {value: "Mémoire sur les conditions de résolubilité des équations par radicaux (third version)", year: 1831, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Submitted 17 January 1831; rejected by Poisson."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founder of Galois theory and early group theory (S1).", certainty: 0.7, cites: [{source: S1, locator: "Summary"}], how_known: "MacTutor."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Parents well educated in philosophy, classical literature and religion (S1). Mother lifelong professing Christian who reduced religion to moral principles (S3 Dupuy); not used as his profession."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household: []
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Lycée Louis-le-Grand", stage: "grammar or secondary school", years: "1823–1829", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Adélaïde-Marie Demante, mother, his sole teacher to age 12", certainty: 0.7, cites: [{source: S1, locator: "Biography"}, {source: S3, locator: "Enfance (mother)"}, {source: S4, locator: "Early life"}], how_known: "MacTutor, Dupuy, and Wikipedia agree she taught him to 12. MacTutor's 'imparted her own scepticism' is not in Dupuy: Dupuy says she remained a lifelong professing Christian without feminine devotion (S3)."}
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events:
    - {value: "Father's suicide after a forged-epigram scandal involving the village priest", year: 1829, certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1829–1832", certainty: 0.5, cites: [{source: S1, locator: "Biography"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "No own words on God or a belief system found (P19). Former AGNOS lead from MacTutor's 'mother's scepticism' is weakened: Dupuy (S3) has the mother as a lifelong professing Christian. Saint-Simon refusal (25 May 1832 letter) and priest-refusal report are not professions of AGNOS/ATHE. Ardent republicanism and the village-priest scandal around his father are political context, not a scored stance."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Former lead from MacTutor mother-scepticism paraphrase; contradicted by Dupuy (S3); kept only as a weak lead, not opened."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "No own-voice locus statement (P19). Deathbed priest refusal is reported speech (S3/S4); Chevalier letter targets Saint-Simonism, not God."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (pure algebra; P30, Knuth/Tao/Noether precedents), and no statement on nature found (P16, P19). Deepen D1 found none in Dupuy letters."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing found."}
    D_authority: {value: UNKNOWN, how_known: "Nothing found."}
    E_scope: {value: UNKNOWN, how_known: "Nothing found."}
  mid_basin: {value: UNKNOWN, how_known: "A and B are UNKNOWN (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: >-
    Deepen D1 non-scoring leads (Dupuy S3 read): (1) Letter to Auguste Chevalier,
    25 May 1832: "Cela veut dire, de ta part, que tu te crois, quant à toi, obligé
    à faire de ton mieux pour me convertir. Mais il est de mon devoir de te prévenir,
    comme je l'ai fait cent fois, de la vanité de tes efforts" — Saint-Simonian
    conversion, not a God-locus claim (Z8). (2) Dupuy: "En pleine connaissance, il
    refusa l'assistance d'un prêtre" (also Wikipedia); reported account, cannot score
    alone. (3) 29 May farewell: "Je prends le ciel à témoin" is a figurative oath.
    (4) Mother: Dupuy has lifelong Christian profession, not MacTutor scepticism.
    Bourgne–Azra Écrits et mémoires (mathematical MSS) not re-read for theology;
    mathematical testament of 29 May is equations only.

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "French", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}], how_known: "MacTutor."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Mother lifelong professing Christian (S3); not recorded as his affiliation."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1829–1832", certainty: 0.5, cites: [{source: S1, locator: "Biography"}], how_known: "Galois theory, first submitted 1829, to the letter and marginal notes of 29 May 1832 (P29, P30; range end)."}
  age_at_first_lasting_contribution: {value: 18, certainty: 0.5, cites: [{source: S1, locator: "Quick Info; Biography"}], how_known: "1829 − 1811 = 18 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "Abstract algebraic proof; studied Legendre's Géométrie (S1).", certainty: 0.5, cites: [{source: S1, locator: "Biography"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "École Normale (préparatoire)", role: "student", years: "1829–1830", kind: "university", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor; expelled 1830."}
collaborators:
  - {value: "Auguste Chevalier", relation: "other", note: "copied and circulated his papers", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  - {value: "Augustin-Louis Cauchy", relation: "rival or critic", note: "referee of the 1829 paper", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 166"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "No own words on religion found after Dupuy letter hunt."
    - "MacTutor mother-scepticism line is a tertiary paraphrase contradicted by Dupuy."
  open_questions:
    - "Bourgne–Azra Écrits et mémoires (non-mathematical marginalia) if any touch religion."
    - "Chevalier 1832 Revue encyclopédique notice for any further reported speech."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "J. J. O'Connor and E. F. Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. 'Évariste Galois.' MacTutor History of Mathematics, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Galois/"
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Galois/"
    accessed: 2026-10-19
    reliability_note: "Signed reference biography with references. Mother-'scepticism' line treated as unreliable paraphrase after Dupuy (S3)."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
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
    kind: "scholarly book"
    author: "Paul Dupuy"
    citation: "Dupuy, Paul. 'La vie d'Évariste Galois.' Annales scientifiques de l'École normale supérieure, 3e série, 13 (1896): 197–266. Wikisource full text; NUMDAM. https://fr.wikisource.org/wiki/La_vie_d%E2%80%99%C3%89variste_Galois/Texte_entier"
    url: "https://fr.wikisource.org/wiki/La_vie_d%E2%80%99%C3%89variste_Galois/Texte_entier"
    accessed: 2026-10-24
    reliability_note: "Standard scholarly biography; prints the 25 May 1832 Chevalier letter and reports the deathbed priest refusal. Family testimony on the mother via Gabriel Demante."
    source_quality: "scholarly edition or monograph"
    used_for: [childhood, worldview, heritage]
  - id: S4
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. \"Évariste Galois.\" Wikipedia, English. https://en.wikipedia.org/wiki/%C3%89variste_Galois (rev. 1381816610, 2026-10-25)."
    url: "https://en.wikipedia.org/wiki/%C3%89variste_Galois"
    accessed: 2026-10-24
    reliability_note: "P50 dual bio with MacTutor. Confirms death after refusing a priest (reported); silent on personal creed. Category labels ignored for coding."
    source_quality: "reference entry"
    used_for: [identity, basics, worldview]
---

## Summary

Évariste Galois (1811–1832), mathematician [S1, S4]. Deepen D1: all worldview fields UNKNOWN (AGNOS lead weakened by Dupuy). Not plotted.

## Life and work

Bourg-la-Reine, Paris; prison 1831–32; killed in a duel [S1].

## Contribution and impact

Galois theory; early group theory [S1].

## Childhood and education

Taught by his mother to 12 (Dupuy: she remained Christian); Louis-le-Grand [S1, S3].

## Adult working worldview

No own-voice creed found. 25 May 1832 letter rejects Saint-Simonian conversion (S3); priest refusal at death is reported speech (S3, S4).

## Heritage (context only)

French [S1].

## Timing

1829–1832, age 18 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Bourgne–Azra non-mathematical marginalia; Chevalier 1832 notice.

## Research log

- 2026-10-24 (deepen D1, queue #158): Dupuy 1896 Wikisource (mother Christian; 25 May Chevalier convert letter; priest refusal report); Wikipedia EN (P50, rev 1381816610); MacTutor re-checked; encyclopedia.com/DSB-style silent on creed; Britannica 403. Kept all worldview UNKNOWN. P47 on S1–S4. No fallacy_catalog. No figures/.
- 2026-10-19: Read MacTutor.
