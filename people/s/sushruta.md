---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA10; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA10, order P32: F 3, rank 219). Source: Britannica scholars edition (unsigned, read in full; three paragraphs). He 'flourished c. 6th century bce'; birth and death UNKNOWN. Lasting: the Sushruta-samhita, 'the main source of knowledge about surgery in ancient India', an 'influential treatise' with 'groundbreaking operations' (S1); lasting at 0.5 (thin wording, P13 borderline). No year: first lasting year, span, age UNKNOWN; era UNKNOWN under P39 (no dated work; candidate 'before -500' from the floruit). Attribution: S1 credits the treatise to him without qualification, but only one short source was read; the text's own date and authorship are not tested here (P42, Sun Tzu precedent). Worldview UNKNOWN. B UNKNOWN pending attribution, alternative B 3 at 0.5 (Galen precedent: empirical surgery and dissection). Not plotted. Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #206, F 3, rank 219). Needs: primary/A/B/mid UNKNOWN; held B alt 3@0.5 Galen if attribution holds (P42 untested). Authorship hunt: Wujastyk 2026 blog summarizing Meulenbeld HIML (S4) — composite multi-layer text; composition may begin last centuries BCE; Uttaratantra later; known to Dṛḍhabala fl. 300–500 CE; Meulenbeld: historical Suśruta as author 'not based on uncontrovertible evidence and may be illusory'; teachings attributed to Kāśirāja Divodāsa; name Suśruta like Hippocrates covers many hands. Wikipedia EN Sushruta (S3) + Samhita date/authorship (via S4/S3): Hoernle 600 BCE rejected; earliest firm name-link Bower Manuscript (6th c. CE). P50 dual bio Britannica (S1) + Wikipedia (S3). P47 source_quality on S1–S5. P42 reaffirmed: Samhitā context only, scores nothing. P49 not stretched (no dual scholarly reconstruction of personal A/B for a recoverable historical Suśruta). primary/A stay UNKNOWN; B UNKNOWN→BELOW_THRESHOLD (Galen/P35 lead kept as named alt only); mid UNKNOWN. Chart still unplotted. No fallacy_catalog; no figures/. Draft, not reviewed."}

identity:
  id: sushruta
  display_name: "Sushruta"
  roster:
    canonical_name: "Sushruta"
    rank: 219
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: "core"
    field: "medicine"
    field_bucket: "medicine"
  full_name: {value: "Sushruta", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "lead"}], how_known: "Britannica; Wikipedia EN (P50)."}
  native_name: {value: "सुश्रुत", certainty: 0.7, cites: [{source: S3, locator: "lead (IAST Suśruta)"}], how_known: "Wikipedia EN: Sanskrit सुश्रुत, IAST Suśruta."}
  aliases:
    - {name: "Suśruta", kind: "transliteration"}
    - {name: "Susruta", kind: "transliteration"}

basics:
  birth:
    date: {value: UNKNOWN, how_known: "Not recoverable; S1 floruit 'c. 6th century bce' is the rejected Hoernle dating of the text, not a life date (S3, S4)."}
    place: {value: UNKNOWN, how_known: "Wikipedia traditional Kanyakubja (S3) not used as scored place under P39 / thin historicity."}
  death:
    date: {value: UNKNOWN, how_known: "Not stated."}
    place: {value: UNKNOWN, how_known: "Wikipedia traditional Varanasi (S3) not scored as life fact."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "Samhitā undated as a single work; multi-layer (S3, S4); P39 / Sun Tzu–Hippocrates precedent."}
  era_bucket: {value: UNKNOWN, how_known: "No dated lasting work of a recoverable author (P39). Floruit 'c. 6th century bce' (S1) tracks Hoernle, rejected by Meulenbeld/Wujastyk consensus (S4). Text layers span last centuries BCE through early CE — not a single adult-life bucket."}
  region_of_birth: {value: "South Asia", certainty: 0.5, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "lead"}], how_known: "'ancient Indian surgeon' (S1); tradition places the teaching frame at Kāśī/Varanasi (S3, S4)."}
  region_of_work: {value: "South Asia", certainty: 0.5, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "Authorship; Date"}], how_known: "Ancient India; teaching frame Kāśī (S3, S4)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S3, locator: "lead"}], how_known: "As recorded."}
  languages_of_work: {value: ["Sanskrit"], certainty: 0.7, cites: [{source: S3, locator: "lead"}, {source: S4, locator: "opening"}], how_known: "Treatise in Sanskrit (S3, S4); own authorship of that treatise not established (P42)."}
  occupations: {value: ["surgeon", "physician"], certainty: 0.5, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "lead"}], how_known: "Traditional attribution (S1, S3); historical person as practicing surgeon not independently documented (S4 Meulenbeld)."}

contribution:
  fields: {value: ["medicine", "surgery"], certainty: 0.7, cites: [{source: S1, locator: "opening; para. 2"}, {source: S3, locator: "lead"}], how_known: "Britannica: shalya tantra; Ayurveda. Wikipedia: plastic/cataract surgery tradition under the name."}
  lasting_original_contributions:
    - {value: "Sushruta-samhita (treatise on surgery and Ayurveda: rhinoplasty, lithotomy, removal of a dead fetus, dissection methods) — attributed", year: UNKNOWN, kind: "work", lasting: "'his influential treatise Sushruta-samhita, the main source of knowledge about surgery in ancient India' (S1); foundational Ayurvedic surgical text in tradition (S3)", certainty: 0.5, cites: [{source: S1, locator: "opening; para. 2"}, {source: S3, locator: "lead; Authorship"}, {source: S4, locator: "Summary of more recent scholarship; Authorship"}], how_known: "Undated single-author work rejected: Meulenbeld/Wujastyk multi-layer composite (S4); 0.5 lasting (P13 borderline) and attribution untested for the historical person (P42). Text is context only for worldview."}
  evidence_of_impact: []
  major_works: []
  honours: []
  definition_fit: {value: "arguable", rationale: "Surgical tradition attached to the name is lasting (S1, S3); dating and single-author historicity rejected by current university scholarship (S4).", certainty: 0.5, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "Authorship (Meulenbeld quote)"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not recoverable for a historical person."}
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
  working_years: {value: UNKNOWN, how_known: "Equals timing.major_work_period (UNKNOWN)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No own words under P42. Samhitā frame (context only) presents Ayurveda as transmitted from Brahmā via deities to Divodāsa/Dhanvantari then pupils including Suśruta (S5) — tradition narrative, not a scored personal profession."}
  primary_system: {value: UNKNOWN, how_known: "Nothing attributable to a historical Suśruta under P42. Samhitā is multi-hand / composite (S3, S4); Meulenbeld: assumption of a historical Suśruta as author 'may be illusory' and the composer attributed teachings to Kāśirāja Divodāsa (S4). P49 not stretched: no dual scholarly reconstruction of a personal belief system for a recoverable historical Suśruta (no SEP/IEP personal-LIO entry). Candidate HINDU rejected: divine-transmission frame is text tradition, not his scored primary."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: HINDU, reason: "Rejected as scored primary: Brahmā–Prajāpati–Aśvins–Indra–Dhanvantari/Divodāsa transmission and deity frame belong to the Samhitā tradition (S5 context), not words attributable to a historical Suśruta under P42 / Meulenbeld authorship doubt (S4).", cites: [{source: S5, locator: "ch. 1 frame"}, {source: S4, locator: "Authorship (Meulenbeld)"}]}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "P19 researched silent / P42: nothing in words attributable to him. Samhitā deity/transmission frame and any nature-theology in Ayurveda are context only (composite text; S4, S5). P49 considered and not stretched — no Confucius-style dual reconstruction of personal A for historical Suśruta. Named alternative: BELOW_THRESHOLD or a scored locus only if a source with scholarly agreement attributes a specific locus-bearing layer to him.", note: "Blockers: full Meulenbeld HIML IA 333–357 page-check; Wujastyk Roots of Ayurveda selections; Nepalese MS critical edition for any layer scholars name as his alone."}
    B_cause: {value: BELOW_THRESHOLD, how_known: "Scientist candidate under P30 if the Samhitā's surgery and dissection methods were his working science (Galen precedent; prior hold B 3 @ 0.5 alt 4 under P35). Authorship hunt fails P42: Meulenbeld/Wujastyk treat the text as several hands; historical Suśruta as author may be illusory; teachings framed as Divodāsa's (S4). Context only; scores nothing. Named alternative: B 3 @ 0.5 (alt 4) if a specific surgical/anatomical layer were attributed to him with scholarly agreement (P35 working science).", note: "Deepen D1 converts the prior UNKNOWN hold into BELOW_THRESHOLD lead (Hippocrates / Sun Tzu pattern), not a scored value."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing attributable (P42)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing attributable (P42). Samhitā names Perception, Inference, Analogy, and Scriptural Truths (Āgama) as testimonies for surgery's primacy (S5) — context only."}
    E_scope: {value: UNKNOWN, how_known: "Nothing attributable (P42)."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, which takes precedence (§6, P19)."}
  statements:
    - text: "Well, we shall now describe the origin of the Science of Medicine, as disclosed by the holy Dhanvantari to his disciple Sushruta."
      cites: [{source: S5, locator: "Volume 1 / Chapter 1 opening"}, {source: S3, locator: "Authorship (Nepalese vs printed frame)"}]
      date: "200"
      context: "Opening of Sūtrasthāna ch. 1 in Bhishagratna's English (vulgate). Nepalese MSS cast Divodāsa (not Dhanvantari) as teacher (S3). Context only under P42 — composite / tradition narrative; not used to score."
      axes: [A_locus]
      kind: "other"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "P42: scores nothing. Date '200' is a conventional placeholder near early-CE redaction / Dṛḍhabala horizon (S4), not a documented year for a historical Suśruta. Retained to document the divine-transmission frame that must not be coded as personal HINDU/A without attribution."
  changes_over_life: []
  coder_notes: "Deepen D1: P42 / Hippocrates analogy explicit in Wujastyk (S4): 'Like \"Hippocrates,\" the name \"Suśruta\" refers to the work of many authors working over several centuries.' Meulenbeld (via S4): historical-author assumption may be illusory. P49 not stretched. Chart unplotted. No fallacy_catalog; figures not refreshed."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated beyond South Asian medical tradition."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not recoverable."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "No dated lasting item of a recoverable author (P29, P30, P39)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "Birth and work dates UNKNOWN."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "Nothing attributable under P42."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S4, locator: "Authorship"}, {source: S3, locator: "Authorship; Date"}], how_known: "No text of his own under P42."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Nothing attributable under P42."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Surgery/medicine (S1); no geometric-form evidence for a historical person.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed; no own text under P42.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "As belief, not finding: form and circle unclear. Worldview unplottable (A UNKNOWN; B BELOW). H1 not tested. Samhitā naturalism/surgery is tradition-context, not his scored view."
  notes: "P42 authorial-tradition case (with Hippocrates, Homer, Sun Tzu)."

institutions: []
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 219"}], how_known: "Study roster."}
  controversies:
    - {value: "Date and authorship of the Suśrutasaṃhitā: Hoernle ~600 BCE still repeated in popular/medical literature; university consensus is multi-layer composite (last centuries BCE beginning; Uttaratantra later; known by Dṛḍhabala 4th–5th c. CE); historical Suśruta as sole author may be illusory (Meulenbeld via S4).", certainty: 0.7, cites: [{source: S4, locator: "full essay"}, {source: S3, locator: "Date; Authorship"}], how_known: "Wujastyk 2026; Wikipedia summarizing Meulenbeld."}
  data_quality_flags:
    - "Life and work undated; era UNKNOWN (P39)."
    - "Samhitā composite / multi-hand; scores no worldview under P42."
    - "P49 reconstructions not available for personal A/B — silence kept."
  open_questions:
    - "Full Meulenbeld HIML IA pp. 333–357 / Wujastyk Roots of Ayurveda page-check — unlikely to unlock own-voice scoring."
    - "Any layer scholars name as a single historical Suśruta's with agreement meeting P42?"
    - "Optional: Nepalese MS critical edition (Suśruta Project) for frame variants only — still tradition, not personal LIO."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "The Editors of Encyclopaedia Britannica"
    citation: "'Sushruta.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/Sushruta/599307"
    url: "https://kids.britannica.com/scholars/article/Sushruta/599307"
    accessed: 2026-10-24
    reliability_note: "Unsigned article, scholars edition, read in full. Retains traditional floruit and sole-author credit; corrected by S3/S4 on dating/authorship."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, lane_b, review]
  - id: S2
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [review]
  - id: S3
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "\"Sushruta.\" Wikipedia. https://en.wikipedia.org/wiki/Sushruta"
    url: "https://en.wikipedia.org/wiki/Sushruta"
    accessed: 2026-10-24
    reliability_note: "P50 dual bio with Britannica (S1). Authorship/Date sections summarize Meulenbeld and note Nepalese vs printed Dhanvantari frame; traditional birth/death places not used as scored life facts (P39)."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, worldview, timing, review]
  - id: S4
    type: secondary
    kind: "other"
    author: "Dominik Wujastyk"
    year: 2026
    citation: "Wujastyk, Dominik. \"On the Date of the Suśrutasaṃhitā.\" The Compendium of Suśruta in Time and Space (Suśruta Project blog), 17 July 2026. https://sushrutaproject2.github.io/blog/2026/On-the-date-of-the-Susrutasamhita/"
    url: "https://sushrutaproject2.github.io/blog/2026/On-the-date-of-the-Susrutasamhita/"
    accessed: 2026-10-24
    reliability_note: "Signed specialist essay by the leading historian of Ayurvedic literature; summarizes Meulenbeld HIML (1999) with quotations on composite layers, Dṛḍhabala terminus, and illusory historical-author assumption; explicit Hippocrates analogy for the name Suśruta."
    source_quality: "scholarly reconstruction"
    used_for: [contribution, worldview, timing, review]
  - id: S5
    type: primary
    kind: "other"
    author: "Suśrutasaṃhitā tradition (translator Kaviraj Kunja Lal Bhishagratna)"
    year: 1907
    citation: "Bhishagratna, Kaviraj Kunja Lal, trans. An English Translation of the Sushruta Samhita, vol. 1, ch. 1 (Vedotpatti). Calcutta, 1907. Wikisource: https://en.wikisource.org/wiki/Sushruta_Samhita,_Volume_1/Chapter_1"
    url: "https://en.wikisource.org/wiki/Sushruta_Samhita%2C_Volume_1/Chapter_1"
    accessed: 2026-10-24
    reliability_note: "English of the printed vulgate frame narrative. Not the historical Suśruta's own words under P42 (S3, S4). Context quotations only; Nepalese MSS differ on Dhanvantari vs Divodāsa (S3)."
    source_quality: "unofficial web copy"
    used_for: [worldview]

---

## Summary

Sushruta (traditional fl. c. 6th century BCE; historicity thin), name attached to the *Suśrutasaṃhitā*, main ancient Indian surgical treatise [S1]. Deepen D1: Meulenbeld/Wujastyk treat the Samhitā as multi-layer composite; historical sole author may be illusory [S4]; text context only (P42). primary_system and A UNKNOWN; B BELOW_THRESHOLD; mid_basin UNKNOWN. Not plotted.

## Life and work

Ancient India; teaching frame at Kāśī/Varanasi in the tradition [S1; S3]. Life dates UNKNOWN. Britannica floruit tracks Hoernle’s rejected ~600 BCE dating of the text [S1; S4].

## Contribution and impact

*Sushruta-samhita*: surgery (rhinoplasty, lithotomy, fetal removal), dissection methods, Ayurveda branches [S1; S3]. Lasting as a textual tradition; not scored as a single person’s own-voice work under P42 [S4].

## Childhood and education

Not recoverable.

## Adult working worldview

**Lane A.** Nothing attributable under P42. Samhitā deity/transmission frame is tradition context [S5; S3]. A UNKNOWN. P49 not stretched [S4].

**Lane B (separate).** Surgery/dissection would make a scientist candidate (Galen / P35 → B 3 @ 0.5 alt 4) if methods were his, but authorship fails P42 [S4]. B BELOW_THRESHOLD.

## Heritage (context only)

Not recoverable for a historical person.

## Timing

UNKNOWN (P39).

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form and circle unclear. H1 not tested. P42 authorial-tradition case (Hippocrates / Sun Tzu).

## Open questions

- Full Meulenbeld HIML / Roots of Ayurveda page-check — unlikely to unlock own-voice scoring.
- Any layer with scholarly agreement naming a historical Suśruta alone (P42 bar)?

## Research log

- 2026-10-20: Read Britannica (scholars edition).
- 2026-10-24 (D1): Wujastyk 2026 date essay (Meulenbeld); Wikipedia EN Sushruta; Bhishagratna Wikisource ch. 1 context. P42/P49/P47/P50. primary/A UNKNOWN; B UNKNOWN→BELOW. Chart-moving no.
