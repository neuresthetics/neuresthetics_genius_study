---
record:
  record_type: person
  schema_version: "1.2"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, fourth batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (fourth batch, RUNBOOK §1 order). Included by owner decision, borderline on the stage-2 date window (radiocarbon dating 1947–49; Jason, 2026-10-02). Basics from Britannica (Kauffman), the Nobel biography and Leona Marshall Libby's GSA memorial. No writing of his on religion was found. primary_system BELOW_THRESHOLD (no candidate supported). B 4 at 0.5 from his working science (P6); A, C, D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. No interview used. Not reviewed."}

identity:
  id: libby-willard
  display_name: "Willard Libby"
  roster:
    canonical_name: "Willard Libby"
    rank: 224
    F: 3
    models: [DeepSeek, Gemini, Grok]
    band: "core (3–4)"
    status: core
    field: chemistry
    field_bucket: chemistry
  full_name: {value: "Willard Frank Libby", certainty: 1.0, cites: [{source: S1, locator: "heading"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources."}
  native_name: {value: "Willard Frank Libby (English)", certainty: 1.0, cites: [{source: S2, locator: "paragraph 1"}], how_known: "English name."}
  aliases:
    - {name: "Libby-Willard", kind: "roster alias"}
    - {name: "Bill Libby", kind: other}

basics:
  birth:
    date: {value: "1908-12-17", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources agree."}
    place: {value: "Grand Valley, Colorado", modern_name: "Grand Valley, Colorado, USA", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources agree."}
  death:
    date: {value: "1980-09-08", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "p. 1"}], how_known: "Two sources agree."}
    place: {value: "Los Angeles, California", modern_name: "Los Angeles, California, USA", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1947, certainty: 0.7, cites: [{source: S1, locator: "'On March 4, 1947, Libby and his students obtained the first age determination'"}], how_known: "First radiocarbon age (4 March 1947). Earlier work (Geiger counters, radioisotopes, 1930s; tritium 1946) is also lasting per S3, so the year is a judgement."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "radiocarbon paragraphs"}], how_known: "From first_lasting_contribution_year (P2)."}
  region_of_birth: {value: "North America", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "USA is North America in data/reference/regions.csv (P3)."}
  region_of_work: {value: "North America", certainty: 1.0, cites: [{source: S2, locator: "paragraphs 2–4"}], how_known: "Berkeley, Columbia, Chicago, Washington, UCLA."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "As the sources record it."}
  languages_of_work: {value: [English], certainty: 1.0, cites: [{source: S3, locator: "selected bibliography"}], how_known: "Papers and books in English."}
  occupations: {value: ["physical chemist", "university professor", "Atomic Energy Commissioner"], certainty: 1.0, cites: [{source: S2, locator: "paragraphs 2–5"}, {source: S1, locator: "paragraph 3"}], how_known: "Two sources."}

contribution:
  fields: {value: ["radiochemistry", "geochemistry", "nuclear chemistry"], certainty: 1.0, cites: [{source: S2, locator: "paragraph 6"}, {source: S1, locator: "opening"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Radiocarbon (carbon-14) dating", year: "1947", kind: method, lasting: "Nobel Prize in Chemistry 1960; more than 140 radiocarbon laboratories", certainty: 1.0, cites: [{source: S1, locator: "radiocarbon paragraphs"}, {source: S3, locator: "p. 1–2"}], how_known: "Two sources; first age determination 4 March 1947 (S1)."}
    - {value: "Natural tritium from cosmic rays and its use for dating water and wine and tracing water circulation", year: "1946", kind: discovery, lasting: "hydrology and geophysics tracer", certainty: 1.0, cites: [{source: S1, locator: "tritium paragraph"}, {source: S2, locator: "paragraph 6"}], how_known: "Two sources."}
    - {value: "Gaseous-diffusion barrier for separating uranium-235 (Manhattan Project, Columbia)", year: "1941–1945", kind: invention, lasting: "used in uranium enrichment for decades (S3)", certainty: 0.7, cites: [{source: S1, locator: "tritium paragraph, first sentence"}, {source: S3, locator: "p. 1"}], how_known: "Two sources; S3 is his widow's memorial."}
  evidence_of_impact:
    - {value: "Nominator: 'Seldom has a single discovery in chemistry had such an impact on the thinking in so many fields of human endeavour'", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S1, locator: "end of radiocarbon section"}], how_known: "Britannica quoting an unnamed nominator."}
  major_works:
    - {value: "Radiocarbon Dating", year: 1952, kind: book, certainty: 1.0, cites: [{source: S2, locator: "paragraph 8"}], how_known: "Nobel biography (second edition 1955)."}
  honours:
    - {value: "Nobel Prize in Chemistry", year: 1960, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "paragraph 7"}], how_known: "Two sources."}
    - {value: "Willard Gibbs Medal (American Chemical Society)", year: 1958, certainty: 0.7, cites: [{source: S2, locator: "paragraph 7"}], how_known: "Nobel biography."}
    - {value: "Albert Einstein Medal Award", year: 1959, certainty: 0.7, cites: [{source: S2, locator: "paragraph 7"}], how_known: "Nobel biography."}
  definition_fit: {value: "clearly meets", rationale: "Invented radiocarbon dating.", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: TODO, note: "Not stated in the sources read."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father, Ora Edward Libby, a farmer", name: "Ora Edward Libby", role: father, certainty: 1.0, cites: [{source: S1, locator: "paragraph 2"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources."}
    - {value: "Mother, Eva May Rivers", name: "Eva May Libby (née Rivers)", role: mother, certainty: 1.0, cites: [{source: S1, locator: "paragraph 2"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources."}
  household_circumstances: {value: "Farming family", certainty: 0.7, cites: [{source: S1, locator: "paragraph 2"}], how_known: "Britannica."}
  schooling:
    - {value: "Grammar and high schools near Sebastopol, California", stage: "grammar or secondary school", years: "1913–1926", certainty: 1.0, cites: [{source: S2, locator: "paragraph 2"}], how_known: "Nobel biography."}
    - {value: "University of California, Berkeley: BSc 1931, PhD 1933", stage: university, years: "1927–1933", certainty: 1.0, cites: [{source: S2, locator: "paragraph 2"}, {source: S1, locator: "paragraph 2"}], how_known: "Two sources."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [English], certainty: 1.0, cites: [{source: S2, locator: "paragraphs 1–2"}], how_known: "American farm family."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1931–1980", certainty: 1.0, cites: [{source: S2, locator: "paragraphs 2–4"}, {source: S3, locator: "p. 1"}], how_known: "Berkeley to death."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No statement by him on science and religion was found."}
  primary_system:
    value: BELOW_THRESHOLD
    cites: [{source: S1, locator: "fallout-shelter paragraph"}, {source: S3, locator: "p. 3"}]
    how_known: "No writing or reported speech of his on religion was read. Britannica's only mention of God is Leo Szilard's joke about Libby's burned fallout shelter, which is Szilard's line, not Libby's view. His widow writes that he 'believed that education is our only hope and that science is basic to human success' (S3), which is her summary and says nothing on God."
    note: "No candidate is supported by evidence. Would need his papers (UCLA Library Special Collections) or an oral history that permits quotation."
  secondary_system: {value: UNKNOWN, how_known: "No system evidence in the sources read."}
  candidate_codes_considered: []
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "No statement placing or denying God was read."}
    B_cause:
      value: 4
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S1, locator: "radiocarbon paragraphs"}]
      how_known: "Coder's reading of his working science, as P6 directs (same treatment as Fermi and Dirac). No statement of his own about miracles read, so 0.5."
      rationale: "Scored on his account of nature (P6). Radiocarbon dating rests on carbon-14 decaying 'at a constant rate' after death and on production that 'varied little with latitude', checked against tree rings and dated artefacts (S1): uniform physical law with no special cases. No miracle, petition or exemption in anything read."
    C_ledger: {value: BELOW_THRESHOLD, how_known: "Nothing on judgement, afterlife or reward in the sources read."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "No statement on revelation in the sources read."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Nothing read addresses favour for a group in events."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD and B_cause is only 0.5, under the P4 test's 0.7 bar."}
  statements: []
  changes_over_life: []
  coder_notes: "No writing of his on religion was found, so statements is empty. S3 is a memorial by his second wife, Leona Marshall Libby; its summaries of his beliefs are hers. No interview used. The Shroud of Turin dating in S1 was done by others with his method and says nothing about his views."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "American (Colorado and California farming family)", certainty: 0.7, cites: [{source: S1, locator: "paragraph 2"}, {source: S2, locator: "paragraphs 1–2"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1946–1952", certainty: 0.7, cites: [{source: S1, locator: "tritium and radiocarbon paragraphs"}, {source: S2, locator: "paragraphs 6, 8"}], how_known: "Tritium (1946) to Radiocarbon Dating (1952); coder's reading."}
  age_at_first_lasting_contribution: {value: 38, certainty: 0.7, cites: [{source: S1, locator: "opening; 'On March 4, 1947'"}], how_known: "Born December 1908; first radiocarbon date March 1947."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No worldview statement found."}
  lio_views_relative_to_major_work: {value: "unclear", rationale: "No worldview statement found.", certainty: 0.5, cites: [{source: S3, locator: "p. 3"}], how_known: "Nothing to date."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "Britannica sets out his radiocarbon reasoning as a chain from stated premises (cosmic-ray neutrons, nitrogen capture, uptake by plants and animals, constant decay) to a dating rule, then tested it on known ages (S1); deductive in form but empirical.", certainty: 0.5, cites: [{source: S1, locator: "radiocarbon paragraphs"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "paragraph 2"}], how_known: "Nothing on method in his schooling."}
  circle_present: {value: "unclear", rationale: "No God-Nature statement found; not scored from absence.", certainty: 0.5, cites: [{source: S3, locator: "p. 3"}], how_known: "No evidence either way."}
  reading: "As belief, not finding: form partly present, circle unclear. The record does not test H1."
  notes: ""

institutions:
  - {value: "University of California, Berkeley", role: "instructor to associate professor of chemistry", years: "1933–1945", kind: university, certainty: 1.0, cites: [{source: S1, locator: "paragraph 2"}, {source: S2, locator: "paragraph 2"}], how_known: "Two sources."}
  - {value: "Columbia University War Research Division (Manhattan Project)", role: "chemist with Harold Urey", years: "1941–1945", kind: "government or state body", certainty: 1.0, cites: [{source: S1, locator: "paragraph 3"}, {source: S2, locator: "paragraph 2"}], how_known: "Two sources."}
  - {value: "University of Chicago (Institute for Nuclear Studies and chemistry department)", role: "professor of chemistry", years: "1945–1954", kind: university, certainty: 1.0, cites: [{source: S2, locator: "paragraph 3"}, {source: S1, locator: "paragraph 3"}], how_known: "Two sources (Britannica gives 1945–59)."}
  - {value: "U.S. Atomic Energy Commission", role: "commissioner", years: "1954–1959", kind: "government or state body", certainty: 1.0, cites: [{source: S2, locator: "paragraphs 3–4"}, {source: S1, locator: "paragraph 3 (1955–59)"}], how_known: "Two sources; start year differs (Nobel biography: appointed 1 October 1954)."}
  - {value: "University of California, Los Angeles", role: "professor of chemistry; director of the Institute of Geophysics and Planetary Physics from 1962", years: "1959–1980", kind: university, certainty: 1.0, cites: [{source: S2, locator: "paragraph 4"}, {source: S1, locator: "paragraph 3"}], how_known: "Two sources."}
collaborators:
  - {value: "Harold Urey", roster_id: urey-harold, relation: collaborator, note: "Columbia war research, 1941–45", certainty: 1.0, cites: [{source: S1, locator: "paragraph 3"}], how_known: "Britannica."}
  - {value: "Edward Teller", roster_id: teller-edward, relation: collaborator, note: "fellow advocate of nuclear testing in the late 1950s", certainty: 0.7, cites: [{source: S1, locator: "fallout-shelter paragraph"}], how_known: "Britannica."}
  - {value: "Linus Pauling", roster_id: pauling-linus, relation: "rival or critic", note: "opposed Pauling's petition for a nuclear test ban", certainty: 1.0, cites: [{source: S1, locator: "fallout-shelter paragraph"}], how_known: "Britannica."}
  - {value: "Leona Woods Marshall", relation: family, note: "second wife (married 1966); author of S3", certainty: 1.0, cites: [{source: S1, locator: "paragraph 2"}, {source: S3, locator: "byline"}], how_known: "Two sources."}

review:
  roster_status_reason: {value: "Core in v8 (F 3: DeepSeek, Gemini, Grok). Included in the fourth batch by owner decision, borderline on the stage-2 date window (1600–1950).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 224"}], how_known: "Study roster; batch inclusion by Jason, 2026-10-02."}
  controversies:
    - {value: "Advocate of nuclear weapons testing; publicized fallout shelter at his house", certainty: 1.0, cites: [{source: S1, locator: "fallout-shelter paragraph"}], how_known: "Britannica."}
  data_quality_flags:
    - "Borderline on the stage-2 date window: radiocarbon dating 1947–49; included by owner decision (2026-10-02)."
    - "No worldview source of any kind."
    - "Chicago and AEC years differ between S1 and S2."
  open_questions:
    - "Search his papers (UCLA Library Special Collections) and any published interview for a statement on religion."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "George B. Kauffman"
    citation: "Kauffman, George B. \"Willard Frank Libby.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Willard-Libby."
    url: "https://www.britannica.com/biography/Willard-Libby"
    accessed: 2026-10-02
    reliability_note: "Signed article. Paragraphs counted from the opening '(born Dec. 17, 1908'."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators, review]
  - id: S2
    type: tertiary
    kind: "institutional page"
    author: "Nobel Foundation"
    year: 1964
    citation: "\"Willard F. Libby – Biographical.\" From Nobel Lectures, Chemistry 1942–1962. Amsterdam: Elsevier, 1964. NobelPrize.org. https://www.nobelprize.org/prizes/chemistry/1960/libby/biographical/."
    url: "https://www.nobelprize.org/prizes/chemistry/1960/libby/biographical/"
    accessed: 2026-10-02
    reliability_note: "Official biography; paragraphs counted from 'Willard Frank Libby was born'."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions]
  - id: S3
    type: secondary
    kind: "journal article"
    author: "Leona Marshall Libby"
    citation: "Libby, Leona Marshall. \"Memorial to Willard Frank Libby, 1908–1980.\" Geological Society of America Memorials, vol. 14. https://rock.geosociety.org/net/documents/gsa/memorials/v14/Libby-WF.pdf."
    url: "https://rock.geosociety.org/net/documents/gsa/memorials/v14/Libby-WF.pdf"
    accessed: 2026-10-02
    reliability_note: "Memorial by his widow; GSA's own PDF. Pages counted in the memorial (1–3) before the bibliography."
    used_for: [basics, contribution, worldview, timing, lane_b, collaborators]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# Willard Libby

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Willard Libby (1908–1980), American chemist, invented radiocarbon dating (first date March 1947) and won the 1960 Nobel Prize in Chemistry [S1; S2]. No writing of his on religion was found. primary_system BELOW_THRESHOLD. B 4 at 0.5 from the working science; A, C, D, E below threshold; mid_basin below threshold. Included in this batch by owner decision, borderline on the stage-2 date window.

## Life and work

Berkeley (BSc 1931, PhD 1933, faculty to 1945), Manhattan Project at Columbia, Chicago, the Atomic Energy Commission (1954–59), UCLA [S1; S2].

## Contribution and impact

Radiocarbon dating, natural tritium, the uranium diffusion barrier [S1; S3].

## Childhood and education

Son of a farmer; schools near Sebastopol, California [S1; S2].

## Adult working worldview

Not established from checkable sources.

## Heritage (context only)

American farming family [S1; S2]. Context only.

## Timing

First lasting contribution 1947, at 38 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form partly present; circle unclear.

## Open questions

- His papers at UCLA.

## Research log

- 2026-10-02: Read Britannica (Kauffman), the Nobel biography and the GSA memorial (Leona Marshall Libby). Nothing on religion.
