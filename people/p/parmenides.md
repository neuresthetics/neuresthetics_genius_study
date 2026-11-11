---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA7; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to philosophy. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA7, order P32: F 3, rank 207). Sources: SEP 'Parmenides' (John Palmer, read in full) and Britannica 'Eleaticism' (signed by Starkey and Calogero, scholars edition, read in part). Born about 515 BCE, inferred from Plato's Parmenides (S1); 'active during the early to mid-fifth century BCE' (S1). Lasting work: the poem On Nature, 'founder of metaphysics or ontology' (S1); undated, so first-lasting year, span and age UNKNOWN (P39). Era UNKNOWN, candidate -500 to 499 (AA7 audit, v8's call on the auditor's advice): Diogenes Laertius 9.23 (S4) says 'He flourished in the 69th Olympiad' (504–501 BCE), which implies birth about 540 BCE and an adult life across the -500 edge (P39 strict; Pythagoras and Heraclitus precedent). Worldview: the goddess of the proem is the poem's narrator-device; SEP: 'Parmenides himself never in the extant fragments calls What Is divine or otherwise suggests that it is a god'. primary_system UNKNOWN; A UNKNOWN; not a scientist; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #194/228, F3 rank 207). Goals: scholarly warrant for A/B with reconstruction labels; keep silence if none; do not force plot. Re-read SEP Palmer (S1; substantive revision 4 Mar 2025): What Is never called divine; ontology distinct from theology; goddess = proem device; Way of Opinion cosmology not a scored scientist account. Dual bio Wikipedia EN (S5, P50) + Britannica Parmenides (S6): Elea, ~515 vs ~540 birth, undated poem agree. IEP (S7) corroborates A-D Paradox / goddess literary frame — same interpretive family as Palmer, used for dual overview not P48 independence on divinity. Bryan 2021 'The Non-Divinity of Parmenides' What-is' (S8): scholarly reconstruction arguing poem's gods are anthropomorphic agents of change incompatible with What Is; divinity not a necessary property of What Is — corroborates Palmer against divine-What-Is readings (P49 labeled). Fr. 12 daimōn / Opinion cosmology unused for B (P30; standing rule). Goddess voice careful (P42) — not first-person creed. primary_system UNKNOWN→BELOW_THRESHOLD (HELLEN literary only; IDEAL/PLATO later reception; divine-What-Is reconstructions rejected by S1+S8). A stays UNKNOWN (no locus to score; silence corroborated). B UNKNOWN; mid UNKNOWN. Not plotted. Chart-moving NO. P47 source_quality S1–S8. No fallacy_catalog; no figures/. Draft, not reviewed."}

identity:
  id: parmenides
  display_name: "Parmenides"
  roster:
    canonical_name: "Parmenides"
    rank: 207
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: "core"
    field: "philosophy"
    field_bucket: "philosophy"
  full_name: {value: "Parmenides of Elea", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Writings"}, {source: S5, locator: "lede"}], how_known: "SEP + Wikipedia."}
  native_name: {value: "Παρμενίδης ὁ Ἐλεάτης", certainty: 0.5, cites: [{source: S5, locator: "lede"}], how_known: "Wikipedia EN Greek form."}
  aliases: []

basics:
  birth:
    date: {value: "-515", certainty: 0.5, cites: [{source: S1, locator: "1. Life and Writings"}, {source: S4, locator: "IX.23"}, {source: S5, locator: "Date of birth"}], how_known: "SEP: 'born about 515 BCE', inferred from the dramatic date of Plato's Parmenides. Competing date: about 540 BCE, implied by Apollodorus's floruit in the 69th Olympiad (504–501 BCE) as reported by Diogenes Laertius 9.23 (S4); Wikipedia dual (S5) same fork."}
    place: {value: "Elea", modern_name: "Velia, Campania, Italy", polity_then: "Elea (Greek colony)", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Writings"}, {source: S2, locator: "Introduction"}, {source: S6, locator: "text"}], how_known: "SEP; Britannica Eleaticism; Britannica Parmenides."}
  death:
    date: {value: UNKNOWN, how_known: "Death date not given (S1, S5)."}
    place: {value: UNKNOWN, how_known: "Death place not given."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "On Nature is undated; 'active during the early to mid-fifth century BCE' (S1) is a floruit, not a composition range (P39; RQ-Z9-N1)."}
  era_bucket: {value: UNKNOWN, how_known: "P39 strict (AA7 audit): on Plato's chronology (born about 515 BCE, S1) every adult year falls in -500 to 499, but Diogenes Laertius's floruit in the 69th Olympiad, 504–501 BCE (S4), puts his adult life across the -500 edge. Candidate: -500 to 499."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Writings"}], how_known: "Elea, southern Italy (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S2, locator: "Introduction"}], how_known: "Elea."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Ancient Greek"], certainty: 0.7, cites: [{source: S1, locator: "2. Overview of Parmenides' Poem"}], how_known: "Hexameter poem."}
  occupations: {value: ["philosopher", "poet", "lawgiver"], certainty: 0.5, cites: [{source: S1, locator: "1. Life and Writings"}, {source: S5, locator: "Anecdotes"}], how_known: "SEP: Speusippus reportedly said he established Elea's laws; Wikipedia same Speusippus/Plutarch line."}

contribution:
  primary_domain: philosophy
  fields: {value: ["philosophy", "metaphysics"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "SEP."}
  lasting_original_contributions:
    - {value: "On Nature (Way of Truth; Way of Opinion): the ontology of What Is", year: UNKNOWN, kind: "work", lasting: "SEP: his derivation of the attributes of what must be qualifies him 'to be seen as the founder of metaphysics or ontology as a domain of inquiry distinct from theology'; Britannica: Eleaticism 'one of the principal schools' of pre-Socratic philosophy", certainty: 0.7, cites: [{source: S1, locator: "closing section"}, {source: S2, locator: "Introduction"}, {source: S6, locator: "text"}], how_known: "SEP; Britannica. Undated."}
  evidence_of_impact:
    - {value: "Plato's dialogue Parmenides; reception by Plato and Aristotle", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Writings"}, {source: S5, locator: "Plato"}], how_known: "SEP + Wikipedia."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founder of metaphysics or ontology (S1).", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "SEP."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated. Velia inscription associates him with Apollo Oulios / healing cult (S1) — adult civic/cult context, not childhood religion."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Father Pyres (Pyres / Pires); aristocratic Elea family", role: "family", certainty: 0.5, cites: [{source: S1, locator: "1. Life and Writings"}, {source: S5, locator: "Biography"}], how_known: "SEP inscription + Wikipedia / Diogenes."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated beyond aristocratic family (S5)."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Ancient reports variously link him to Xenophanes, the Pythagorean Ameinias, or Anaximander (doxography)", certainty: 0.5, cites: [{source: S4, locator: "IX.21–23"}, {source: S5, locator: "Biography"}, {source: S7, locator: "4.a"}], how_known: "Diogenes / Wikipedia / IEP; reported associations, not scored as worldview (P42)."}
  languages_in_childhood: {value: ["Ancient Greek"], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Inferred from Elea and the poem."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: UNKNOWN, how_known: "Undated (P39)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "SEP places his ontology as distinct from theology (S1 closing); not a first-person science–religion equation."}
  primary_system:
    value: BELOW_THRESHOLD
    how_known: "Hunt D1: SEP Palmer (S1) — What Is never called divine; founder of ontology distinct from theology. Bryan 2021 (S8) — scholarly reconstruction arguing poem divinities are changing anthropomorphic agents incompatible with What Is; divinity not necessary to What Is. Goddess of the proem is literary narrator-device (S1, S7; P42 — poem voice careful, not scored as creed). HELLEN is mythic frame only, not a profession. IDEAL/PLATO fit later reception (Plato/Aristotle/Neoplatonist aspectual readings), not his professed system. No MONISM code. Keep silence: do not force a primary from Opinion cosmology or from divine-What-Is reconstructions (P19/P49)."
    note: "Named alternatives HELLEN / IDEAL / PLATO / divine-What-Is reconstructions stay leads or rejected leads only."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: HELLEN, reason: "Lead only: proem goddess, Justice, daughters of Helios, Night halls (S1 §2.1). Literary/religious frame of revelation, not a self-identified Hellenismos profession (HELLEN do_not_use: interest in ancient myth alone is not enough)."}
    - {code: IDEAL, reason: "Rejected: IDEAL requires reality as mental/thought-like in the person's own writing; fr. 3 thinking/being line is contested and does not clear that bar (S1, S7)."}
    - {code: PLATO, reason: "Rejected as his code: Platonic Forms and aspectual two-world readings are reception (S1 §3.4), not Parmenides' profession."}
    - {code: PANT, reason: "Rejected: unlike Heraclitus B67, What Is is never identified as god with the world; Palmer and Bryan argue against divinity of What Is (S1, S8)."}
  lio_axes:
    A_locus:
      value: UNKNOWN
      how_known: "SEP: 'Parmenides himself never in the extant fragments calls What Is divine or otherwise suggests that it is a god' (S1 closing). Bryan 2021 corroborates non-divinity of What Is (S8; P49 scholarly reconstruction against the divine reading). Goddess voice is poem device (P42) — not used to score a personal/immanent God locus. Silence kept; do not force A from Xenophanes-analogue or from Opinion daimōn."
    B_cause:
      value: UNKNOWN
      how_known: "Not a scientist (P30). Way of Opinion cosmology (light/night, celestial rings, fr. 12 daimōn who steers) is explicitly not scored as a P16 nature-order / scientist B (standing deepen rule; S1 §2.4). Astronomical innovations (moonlight from sun, etc.) stay contribution facts, not Lane A B."
    C_ledger: {value: UNKNOWN, how_known: "Proem katabasis / halls of Night motifs are literary (S1 §2.1); no scored afterlife/reward profession."}
    D_authority: {value: UNKNOWN, how_known: "Goddess commands 'judge by reason' (fr. 7; S1) is a reason-over-habit lead only — not scored as D (epistemic method, not religious authority axis)."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read for in-group exemptions (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied (P19)."}
  statements:
    - text: "Although What Is in Parmenides has its nearest analogue in these divine principles, Parmenides himself never in the extant fragments calls What Is divine or otherwise suggests that it is a god."
      cites: [{source: S1, locator: "closing section (§3.5 Modal Interpretation)"}]
      context: "Palmer's reading of the extant fragments; settles why A is not scored."
      axes: [A_locus]
      kind: "other"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Scholar's statement (re-confirmed D1 against Mar 2025 SEP). Not Parmenides' own words."
    - text: "What Is is ungenerated and deathless, whole and uniform, and still and perfect."
      cites: [{source: S1, locator: "fr. 8.1–4 (Palmer tr.)"}]
      context: "Goddess's programmatic attributes of What Is (Way of Conviction). Metaphysical markers; not used to score A as divine (S1+S8)."
      axes: []
      kind: "other"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Fragment via goddess voice (P42 careful). Attributes are ontology, not a god-profession. P49: text from Palmer SEP translation."
    - text: "Divinity as it is represented in Parmenides' poem is incompatible with what-is… Divinity is not a relevant or necessary property of what-is."
      cites: [{source: S8, locator: "abstract / closing argument"}]
      context: "Bryan 2021 scholarly reconstruction against divine-What-Is readings."
      axes: [A_locus]
      kind: "other"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Secondary reconstruction (P49 labeled). Corroborates S1; not a fragment."
  changes_over_life: []
  coder_notes: "Deepen D1 2026-10-24: create-pass already had SEP non-divinity. Hunt added Bryan 2021 (S8) + Wikipedia/Britannica dual + IEP overview. Result: silence corroborated, not lifted. primary UNKNOWN→BELOW (candidates considered/rejected). A/B stay UNKNOWN. Fr. 12 daimōn and Opinion cosmology unused for B. Goddess voice not scored as creed (P42). Lane A separate from Lane B geometric labels (sphere of What Is stays lane_b). No fallacy_catalog (Jason)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Greek (Elea / Magna Graecia; Phocaean colony stock)", certainty: 0.5, cites: [{source: S5, locator: "lede / Life"}, {source: S7, locator: "1. Life"}], how_known: "Wikipedia + IEP; heritage only."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated. Adult Velia inscription links to Apollo Oulios healing cult (S1) — not birth religion."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not applicable / not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "Undated (P39)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "Undated (P39)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No axis scored."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S1, locator: "closing"}, {source: S8, locator: "abstract"}], how_known: "A UNKNOWN; B UNKNOWN."}
  worldview_during_major_work: {value: "Ontology of What Is without calling it divine; goddess is poem device; Opinion cosmology not scored as creed or scientist B", certainty: 0.5, cites: [{source: S1, locator: "closing; §2.1; §2.4"}, {source: S8, locator: "abstract"}], how_known: "SEP + Bryan."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "What Is 'like the bulk of a well-rounded globe' (fr. 8.42–49; S1).", certainty: 0.5, cites: [{source: S1, locator: "§2.3"}], how_known: "Coder's reading of fragment via SEP."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable as a scored acquisition path."}
  circle_present: {value: "unclear", rationale: "Sphere simile for limit/perfection; not assessed as Deus-sive-Natura circle.", certainty: 0.5, cites: [{source: S1, locator: "§2.3"}], how_known: "Coder's reading."}
  reading: "No scored Lane A axes. Do not invent B from Opinion cosmology or from the sphere image."
  notes: "P42: goddess voice careful. Opinion cosmology out of scientist B."

institutions: []
collaborators:
  - {value: "Zeno of Elea", relation: "student or assistant", note: "younger associate", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Writings"}, {source: S2, locator: "Introduction"}, {source: S5, locator: "lede"}], how_known: "SEP; Britannica; Wikipedia."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 207"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Era UNKNOWN: 515 vs 540 BCE birth (P39)."
    - "Poem undated (P39); first_lasting_contribution_year UNKNOWN."
    - "Worldview: silence on divinity corroborated (S1+S8); Opinion cosmology deliberately unscored for B."
  open_questions:
    - "Poem date (Wheelwright 470–460 BCE remains a lead only)."
    - "Whether a consensus fragment edition (Coxon / Laks–Most) would change the Palmer/Bryan non-divinity reading (unlikely; not obtained end-to-end this pass)."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "John Palmer"
    citation: "Palmer, John. 'Parmenides.' Stanford Encyclopedia of Philosophy. First published 8 Feb 2008; substantive revision 4 Mar 2025. https://plato.stanford.edu/entries/parmenides/"
    url: "https://plato.stanford.edu/entries/parmenides/"
    accessed: 2026-10-24
    reliability_note: "Signed entry, re-read in full at D1 (Mar 2025 revision). Non-divinity of What Is and ontology-vs-theology close are decisive for A/primary silence."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, worldview, collaborators, timing]
  - id: S2
    type: tertiary
    kind: "encyclopedia"
    author: "Lawrence H. Starkey; Guido Calogero"
    citation: "Starkey, Lawrence H., and Guido Calogero. 'Eleaticism.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/Eleaticism/108668"
    url: "https://kids.britannica.com/scholars/article/Eleaticism/108668"
    accessed: 2026-10-19
    reliability_note: "Signed article; introduction and Parmenides sections read at create."
    source_quality: "reference entry"
    used_for: [identity, contribution, collaborators]
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
    kind: "other"
    author: "Diogenes Laertius, tr. R.D. Hicks"
    citation: "Diogenes Laertius. Lives of the Eminent Philosophers, Book IX, tr. R.D. Hicks (1925). Wikisource. https://en.wikisource.org/wiki/Lives_of_the_Eminent_Philosophers/Book_IX"
    url: "https://en.wikisource.org/wiki/Lives_of_the_Eminent_Philosophers/Book_IX"
    accessed: 2026-10-19
    reliability_note: "Ancient biography in translation; the Parmenides chapter (IX.21–23) read."
    source_quality: "other"
    used_for: [identity, basics, childhood]
  - id: S5
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "Wikipedia. 'Parmenides' (English). https://en.wikipedia.org/wiki/Parmenides"
    url: "https://en.wikipedia.org/wiki/Parmenides"
    accessed: 2026-10-24
    reliability_note: "Dual-bio check against SEP/Britannica (P50). Agrees Elea, poem On Nature fragments, 515 vs 540 birth fork, Zeno associate, founder-of-ontology claim (via Palmer). Not used alone for worldview codes."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, heritage, collaborators]
  - id: S6
    type: tertiary
    kind: "encyclopedia"
    author: "Encyclopaedia Britannica"
    citation: "'Parmenides.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/Parmenides/58531"
    url: "https://kids.britannica.com/scholars/article/Parmenides/58531"
    accessed: 2026-10-24
    reliability_note: "Signed scholars article; birth c. 515, Elea, On Nature, 'all is one' / founder of metaphysics summary read."
    source_quality: "reference entry"
    used_for: [basics, contribution]
  - id: S7
    type: tertiary
    kind: "encyclopedia"
    author: "Internet Encyclopedia of Philosophy"
    citation: "'Parmenides of Elea.' Internet Encyclopedia of Philosophy. https://iep.utm.edu/parmenid/"
    url: "https://iep.utm.edu/parmenid/"
    accessed: 2026-10-24
    reliability_note: "Signed IEP entry, read for Proem / A-D Paradox / goddess literary frame and predecessor reports. Same interpretive neighborhood as Palmer; not treated as independent P48 warrant for divinity claims."
    source_quality: "reference entry"
    used_for: [worldview, childhood]
  - id: S8
    type: secondary
    kind: "journal article"
    author: "Jenny Bryan"
    citation: "Bryan, Jenny. 'The Non-Divinity of Parmenides' What-Is.' Anais de Filosofia Clássica 14.27 (2021): 71–95. https://doi.org/10.47661/afcl.v14i27.38885"
    url: "https://doi.org/10.47661/afcl.v14i27.38885"
    accessed: 2026-10-24
    reliability_note: "Peer-reviewed article (abstract and argument summary read via publisher/DOI landing). Explicit scholarly reconstruction against reading What Is as divine; used as P49-labeled corroboration of S1, not as a fragment edition."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview]
---

## Summary

Parmenides of Elea (b. c. 515 or c. 540 BCE), founder of Eleatic ontology [S1; S6]. Deepen D1: primary_system BELOW_THRESHOLD; A UNKNOWN; B UNKNOWN; mid_basin UNKNOWN. Not plotted. Chart-moving NO.

## Life and work

Elea (Velia); laws for the city (Speusippus via D.L.); associate of Zeno [S1; S5].

## Contribution and impact

Poem *On Nature* (fragments): Way of Truth / Way of Opinion; founder of metaphysics distinct from theology [S1; S6].

## Childhood and education

Aristocratic Elea family; father Pyres; ancient reports link Xenophanes / Ameinias / Anaximander (doxography only) [S4; S5; S7].

## Adult working worldview

What Is never called divine in extant fragments [S1]; Bryan 2021 argues divinity incompatible with What Is [S8]. Goddess = poem device (P42). Opinion cosmology unused for B (P30). primary BELOW_THRESHOLD; A/B UNKNOWN.

## Heritage (context only)

Greek Elea / Magna Graecia [S5; S7]. Velia Apollo Oulios inscription = adult cult context, not birth religion [S1].

## Timing

Poem undated (P39); era UNKNOWN (515 vs 540 birth fork).

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Well-rounded sphere image for What Is [S1]. No scored Lane A axes.

## Open questions

- Poem date.
- Full Coxon / Laks–Most editions end-to-end (Palmer/Bryan already settle non-divinity for this pass).

## Research log

- 2026-10-19: Read SEP (Palmer); Britannica Eleaticism; D.L. IX.23.
- 2026-10-24 (D1): Re-read SEP Palmer (Mar 2025); Wikipedia dual (S5); Britannica Parmenides (S6); IEP (S7); Bryan 2021 non-divinity (S8). primary UNKNOWN→BELOW; A/B UNKNOWN. Chart-moving NO. No fallacy_catalog; no figures/.
