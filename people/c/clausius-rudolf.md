---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, fourth batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (fourth batch, RUNBOOK §1 order). Basics from Britannica and MacTutor. No writing of his on religion was found; his father was a pastor and school principal (MacTutor). primary_system BELOW_THRESHOLD (no candidate supported). B 4 at 0.5 from his working science (P6); A, C, D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. No interview used. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 4 (two blind runs at b21655b). #124 (run 1): candidate_codes_considered was empty; CHRIST is now listed as considered, not coded (upbringing by a minister father is never a code, §1; CODING_GUIDE §5.3), and the primary_system note updated. #131–132 (minor): birth date and place and death date and place 0.7 → 1.0, now citing MacTutor's Quick Info as well as Britannica (two independent sources agree). No worldview value changed. Decisions P12/P13 recheck: first_lasting_contribution_year 1850 unchanged. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02). Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs; BELOW_THRESHOLD vs UNKNOWN per P19; kind lists (P21: research institute, school stage and run_by, scholarly edition); basis inference_from_work for 0.5 inference from working science (P24). Full before → after list: reports/stage3_rulings_changes.csv. Not reviewed."}

identity:
  id: clausius-rudolf
  display_name: "Rudolf Clausius"
  roster:
    canonical_name: "Rudolf Clausius"
    rank: 216
    F: 3
    models: [Claude, DeepSeek, Gemini]
    band: "core (3–4)"
    status: core
    field: physics
    field_bucket: physics
  full_name: {value: "Rudolf Julius Emanuel Clausius", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts ('In full')"}], how_known: "Britannica."}
  native_name: {value: "Rudolf Julius Emanuel Clausius (German)", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Britannica; German name."}
  aliases:
    - {name: "Clausius-Rudolf", kind: "roster alias"}

basics:
  birth:
    date: {value: "1822-01-02", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Quick Info"}], how_known: "Two independent sources agree (Britannica and MacTutor)."}
    place: {value: "Köslin, Prussia", modern_name: "Koszalin, Poland", polity_then: "Kingdom of Prussia", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Quick Info ('Koslin, Prussia (now Koszalin, Poland)')"}], how_known: "Two independent sources agree (Britannica and MacTutor)."}
  death:
    date: {value: "1888-08-24", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Quick Info"}], how_known: "Two independent sources agree (Britannica and MacTutor)."}
    place: {value: "Bonn", modern_name: "Bonn, Germany", polity_then: "German Empire", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Quick Info"}], how_known: "Two independent sources agree (Britannica and MacTutor)."}
  first_lasting_contribution_year: {value: 1850, certainty: 1.0, cites: [{source: S1, locator: "paragraph 2"}, {source: S2, locator: "Biography (1850 paper)"}], how_known: "Über die bewegende Kraft der Wärme, read to the Berlin Academy and published in Annalen der Physik in 1850; the second law."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "paragraph 2"}], how_known: "From first_lasting_contribution_year (P2)."}
  region_of_birth: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening ('Köslin, Prussia [Poland]')"}], how_known: "Modern Poland is Eastern Europe in data/reference/regions.csv (P3); then Prussia."}
  region_of_work: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "paragraphs 2–3"}, {source: S2, locator: "Biography"}], how_known: "Berlin, Zürich, Würzburg, Bonn."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "As the sources record it."}
  languages_of_work: {value: [German], certainty: 0.7, cites: [{source: S2, locator: "Biography (1850 paper title)"}], how_known: "Papers in Annalen der Physik in German."}
  occupations: {value: ["mathematical physicist", "university professor"], certainty: 1.0, cites: [{source: S1, locator: "opening; paragraphs 2–3"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}

contribution:
  fields: {value: ["thermodynamics", "kinetic theory of gases", "mathematical physics"], certainty: 1.0, cites: [{source: S1, locator: "opening; paragraph 2"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Second law of thermodynamics ('Heat cannot of itself pass from a colder to a hotter body')", year: "1850", kind: "law or principle", lasting: "foundation of thermodynamics", certainty: 1.0, cites: [{source: S1, locator: "paragraph 2"}, {source: S2, locator: "Biography (1850 paper)"}], how_known: "Two sources."}
    - {value: "Concept of entropy, applied to the theory of the steam engine", year: "1850s–1865", kind: "concept or term", lasting: "standard physics", certainty: 0.7, cites: [{source: S1, locator: "paragraph 2"}], how_known: "Britannica; year of the name 'entropy' not given on the page read."}
    - {value: "Idea that molecules continually exchange atoms, later the basis of electrolytic dissociation", year: "1857", kind: theory, lasting: "precursor of ionic theory", certainty: 0.7, cites: [{source: S1, locator: "paragraph 2"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "Credited with 'making thermodynamics a science'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Über die bewegende Kraft der Wärme", year: 1850, kind: "paper or paper series", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}
  honours:
    - {value: "Copley Medal", year: 1879, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Britannica."}
    - {value: "Iron Cross (for leading an ambulance corps in the Franco-Prussian War)", year: 1871, certainty: 0.7, cites: [{source: S2, locator: "Biography (1870–71)"}], how_known: "MacTutor."}
  definition_fit: {value: "clearly meets", rationale: "Formulated the second law and the concept of entropy.", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Pastor's family (father 'a minister of the church' and pastor of his own school); denomination not stated", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 1"}], how_known: "MacTutor."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father, Rev. C. E. G. Clausius, Councillor of the Royal Government School Board, who founded and led a small private school and served as its pastor", name: "C. E. G. Clausius", role: father, certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 1"}], how_known: "MacTutor."}
  household_circumstances: {value: "Large family; Rudolf the sixth son", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 1"}], how_known: "MacTutor."}
  schooling:
    - {value: "His father's private school", stage: "elementary school", years: "1820s–1830s", certainty: 0.5, cites: [{source: S2, locator: "Biography, paragraph 1"}], how_known: "MacTutor ('a few years'); 'religious school' is the nearest stage for a pastor-led school, a coder's judgement.", run_by: "private"}
    - {value: "Gymnasium in Stettin (Szczecin)", stage: "grammar or secondary school", years: "–1840", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 1"}], how_known: "MacTutor."}
    - {value: "University of Berlin: mathematics and physics (degree 1844); probationary year teaching at the Frederic-Werder Gymnasium", stage: university, years: "1840–1845", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 2"}], how_known: "MacTutor."}
    - {value: "Boeck's Royal Seminary (1846); doctorate from Halle on the colours of the sky (1848)", stage: university, years: "1846–1848", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 3"}], how_known: "MacTutor."}
  early_mathematics: {value: "advanced mathematics", note: "University mathematics and physics in Berlin; earlier mathematics not stated.", certainty: 0.5, cites: [{source: S2, locator: "Biography, paragraph 2"}], how_known: "MacTutor; university level only."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "His father, as principal of the school he attended", certainty: 0.5, cites: [{source: S2, locator: "Biography, paragraph 1"}], how_known: "MacTutor; mentorship is the coder's reading."}
  languages_in_childhood: {value: [German], certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 1"}], how_known: "Prussian family."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1844–1888", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "Degree to death."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No statement by him on science and religion was found in the sources read."}
  primary_system:
    value: UNKNOWN
    cites: [{source: S2, locator: "Biography"}]
    how_known: "No writing or reported speech of his on religion was read. A pastor father is upbringing, never a code."
    note: "No candidate is supported by evidence; CHRIST is the default guess from upbringing only; it is listed in candidate_codes_considered as considered, not coded. Would need his German biographies (e.g. the Neue Deutsche Biographie entry) or his rectorial address at Bonn."
  secondary_system: {value: UNKNOWN, how_known: "No system evidence in the sources read."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Considered, not coded: no statement of his on religion was read; being brought up by a father who was a minister and pastor of the school he attended (MacTutor) is upbringing, never a code (CODING_GUIDE §1).", cites: [{source: S2, locator: "Biography, paragraph 1"}]}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "No statement placing or denying God was read."}
    B_cause:
      value: 4
      basis: inference_from_work
      certainty: 0.5
      cites: [{source: S1, locator: "paragraphs 2–3"}, {source: S2, locator: "Biography (1850 paper)"}]
      how_known: "Coder's reading of his working science, as P6 directs (same treatment as Fermi and Dirac). No statement of his own about miracles read, so 0.5."
      rationale: "Scored on his account of nature (P6). His second law ('Heat cannot of itself pass from a colder to a hotter body', S1) and the mechanical theory of heat are general laws with no special cases; no miracle, petition or exemption in anything read."
    C_ledger: {value: UNKNOWN, how_known: "Nothing on judgement, afterlife or reward in the sources read."}
    D_authority: {value: UNKNOWN, how_known: "No statement on revelation in the sources read."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Nothing read addresses favour for a group in events. Working science bears on the first question (same laws everywhere) but not on favour for a group in events, so E stays BELOW_THRESHOLD; not scored from working science alone (P19)."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so mid_basin is UNKNOWN (§6 precedence, decision P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "No writing of his on religion was found, so statements is empty. His 1865 summary sentences on the energy and entropy of the world are widely quoted but were not checked against a scan of Annalen der Physik 125 and are not used. No interview used."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Prussian (Pomeranian) German; a German patriot", certainty: 0.7, cites: [{source: S2, locator: "Biography (Zürich and 1870 paragraphs)"}], how_known: "MacTutor ('a country he deeply loved'; 'a German patriot')."}
  religious_heritage_by_birth: {value: TODO, note: "Father a minister of the church (S2); denomination not stated."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1850–1865", certainty: 0.7, cites: [{source: S1, locator: "paragraphs 2–3"}, {source: S2, locator: "Biography"}], how_known: "Second law to entropy; coder's reading."}
  age_at_first_lasting_contribution: {value: 28, certainty: 1.0, cites: [{source: S1, locator: "opening; paragraph 2"}, {source: S2, locator: "Biography (read 18 February 1850)"}], how_known: "Born 2 January 1822; paper read 18 February 1850."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No worldview statement found."}
  lio_views_relative_to_major_work: {value: "unclear", rationale: "No worldview statement found.", certainty: 0.5, cites: [{source: S2, locator: "Biography"}], how_known: "Nothing to date."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "He built thermodynamics from two stated principles and worked out their mathematical consequences (S1; S2), an axiomatic style within physics.", certainty: 0.5, cites: [{source: S2, locator: "Biography (1850 paper)"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "Biography, paragraphs 1–2"}], how_known: "Nothing on method in his schooling."}
  circle_present: {value: "unclear", rationale: "No God-Nature statement found; not scored from absence.", certainty: 0.5, cites: [{source: S2, locator: "Biography"}], how_known: "No evidence either way."}
  reading: "As belief, not finding: form partly present (principles and consequences), circle unclear. The record does not test H1."
  notes: ""

institutions:
  - {value: "Royal Artillery and Engineering School, Berlin; Docent at the University of Berlin", role: "professor of physics", years: "1850–1855", kind: university, certainty: 1.0, cites: [{source: S1, locator: "paragraph 2"}, {source: S2, locator: "Biography (1850)"}], how_known: "Two sources."}
  - {value: "Polytechnikum and University of Zürich", role: "professor of mathematical physics", years: "1855–1867", kind: university, certainty: 1.0, cites: [{source: S1, locator: "paragraph 2"}, {source: S2, locator: "Biography (1855)"}], how_known: "Two sources."}
  - {value: "University of Würzburg", role: "professor of physics", years: "1867–1869", kind: university, certainty: 0.7, cites: [{source: S1, locator: "paragraph 3"}], how_known: "Britannica."}
  - {value: "University of Bonn", role: "professor of physics; rector 1884–85", years: "1869–1888", kind: university, certainty: 1.0, cites: [{source: S1, locator: "paragraph 3"}, {source: S2, locator: "Biography (1884)"}], how_known: "Two sources."}
collaborators:
  - {value: "Sadi Carnot", roster_id: carnot-sadi, relation: "influenced by", note: "he restated Carnot's principle on the efficiency of heat engines", certainty: 0.7, cites: [{source: S1, locator: "paragraph 3"}], how_known: "Britannica."}
  - {value: "Adelheid Rimpam", relation: family, note: "first wife (married 1859; died 1875)", certainty: 0.7, cites: [{source: S2, locator: "Biography (1859, 1875)"}], how_known: "MacTutor."}

review:
  roster_status_reason: {value: "Core in v8 (F 3: Claude, DeepSeek, Gemini).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 216"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "No worldview source of any kind."
    - "Birth and death facts from one source."
  open_questions:
    - "Read the Neue Deutsche Biographie and Allgemeine Deutsche Biographie entries and his Bonn rectorial address for any religious statement."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "The Editors of Encyclopaedia Britannica"
    citation: "The Editors of Encyclopaedia Britannica. \"Rudolf Clausius.\" Encyclopaedia Britannica (last updated 20 August 2026). https://www.britannica.com/biography/Rudolf-Clausius."
    url: "https://www.britannica.com/biography/Rudolf-Clausius"
    accessed: 2026-10-02
    reliability_note: "Unsigned short article. Paragraphs counted from the opening '(born January 2, 1822'."
    used_for: [identity, basics, contribution, worldview, timing, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "J J O'Connor and E F Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Rudolf Julius Emmanuel Clausius.\" MacTutor History of Mathematics, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Clausius/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Clausius/"
    accessed: 2026-10-02
    reliability_note: "Biography quoting his brother Robert's memoir; paragraphs counted from 'Rudolf Clausius's father'."
    used_for: [basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# Rudolf Clausius

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Rudolf Clausius (1822–1888), German mathematical physicist, stated the second law of thermodynamics (1850) and developed the concept of entropy [S1; S2]. No writing of his on religion was found; his father was a pastor and school principal [S2]. primary_system UNKNOWN. B 4 at 0.5 from the working science; A, C, D UNKNOWN (nothing in the sources read); E below threshold; mid_basin UNKNOWN.

## Life and work

Stettin Gymnasium, Berlin, Halle doctorate (1848); professor at Berlin, Zürich, Würzburg and Bonn; led a student ambulance corps in 1870–71 [S1; S2].

## Contribution and impact

Second law, entropy, kinetic theory, molecular exchange in electrolysis [S1].

## Childhood and education

Sixth son of a pastor who ran a private school, which he attended before the Stettin Gymnasium [S2].

## Adult working worldview

Not established from checkable sources.

## Heritage (context only)

Prussian German [S1; S2]. Context only.

## Timing

First lasting contribution 1850, at 28 [S1; S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form partly present; circle unclear.

## Open questions

- NDB and ADB entries; his Bonn rectorial address.

## Research log

- 2026-10-02: Read Britannica and MacTutor. Nothing on religion beyond his father's office.
