---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 5
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, fourth batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-08
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (fourth batch, RUNBOOK §1 order). Basics from Britannica and Solon I. Bailey's obituary (Popular Astronomy 30, 1922, pp. 197–199), read in the NASA ADS page scan. No writing of hers on religion was found; Bailey, a colleague, describes her as 'deeply conscientious and sincere in her attachment to her religion and church' and names her father as the Rev. George Roswell Leavitt. primary_system BELOW_THRESHOLD (CHRIST candidate). B 4 at 0.5 from her working science (P6); A, C, D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. No interview used. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 4 (two blind runs at b21655b). #109 (both runs): the no-code note wrongly cited 'decision P9: paraphrase alone cannot score'; it now cites CODING_GUIDE §1 (church attachment is never a code on its own) and §7 (another person's description is not her words). Decision P12 recheck: the variable-star item '1900s–1921' → 'by 1921' (sources give totals only), so it does not set the year; first_lasting_contribution_year stays 1912, with a flag that a dated source could move it earlier. No coded value changed. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02). Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs; BELOW_THRESHOLD vs UNKNOWN per P19; basis inference_from_work for 0.5 inference from working science (P24). Full before → after list: reports/stage3_rulings_changes.csv. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "P30 rule 5 age sweep: ages recomputed as event year − birth year, with no month adjustment (scripts/recompute_ages.py; every change is in reports/p30_age_changes.csv). No other value changed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Span alignment (P29, P30 and its addendum): timing.major_work_period 1907–1921 → 1912–1921; worldview.working_years 1895–1921 → 1912–1921, equal to the span (P30 addendum f); evidence for every headline value checked against the span; no value or certainty changed. Listed in reports/p30_span_alignment.csv. Not reviewed."}
    - {date: 2026-10-08, by: "Grok Bot", summary: "Lens audit of batch C (dd91009), ruling R1, logged as P35 (v8's pick): B_cause 4 → 3 at 0.5, alternative 4, because B rests on working science only. No other value changes; mid_basin unchanged."}

identity:
  id: leavitt-henrietta-swan
  display_name: "Henrietta Swan Leavitt"
  roster:
    canonical_name: "Henrietta Swan Leavitt"
    rank: 179
    F: 3
    models: [DeepSeek, Gemini, GPT]
    band: "core (3–4)"
    status: core
    field: astronomy
    field_bucket: astronomy
  full_name: {value: "Henrietta Swan Leavitt", certainty: 1.0, cites: [{source: S1, locator: "heading"}, {source: S2, locator: "p. 197, title"}], how_known: "Two sources."}
  native_name: {value: "Henrietta Swan Leavitt (English)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "English name."}
  aliases:
    - {name: "Henrietta-Leavitt", kind: "roster alias"}
    - {name: "Leavitt-Henrietta Swan", kind: "roster alias"}

basics:
  birth:
    date: {value: "1868-07-04", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "p. 197"}], how_known: "Two sources agree."}
    place: {value: "Lancaster, Massachusetts", modern_name: "Lancaster, Massachusetts, USA", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "p. 197"}], how_known: "Two sources agree."}
  death:
    date: {value: "1921-12-12", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "p. 197"}], how_known: "Two sources agree."}
    place: {value: "Cambridge, Massachusetts", modern_name: "Cambridge, Massachusetts, USA", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "p. 197"}], how_known: "Two sources agree."}
  first_lasting_contribution_year: {value: 1912, certainty: 1.0, cites: [{source: S1, locator: "'Leavitt's outstanding achievement was her discovery in 1912'"}, {source: S2, locator: "p. 198 ('the important law was derived')"}], how_known: "Period–luminosity relation for Cepheid variables, the earliest dated listed contribution (decisions P12, P13). The variable-star discoveries ('by 1921') have no dated start in the sources read; a source dating her first discoveries before 1912 would move the year earlier."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "Cepheid paragraph"}], how_known: "From first_lasting_contribution_year (P2)."}
  region_of_birth: {value: "North America", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "USA is North America in data/reference/regions.csv (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "paragraph 1"}], how_known: "Harvard College Observatory."}
  sex_as_recorded: {value: "female", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "p. 197"}], how_known: "As the sources record it."}
  languages_of_work: {value: [English], certainty: 0.7, cites: [{source: S2, locator: "p. 198 (Harvard Annals and Circulars)"}], how_known: "Published in the Harvard Observatory's English series."}
  occupations: {value: ["astronomer", "head of photographic stellar photometry, Harvard College Observatory"], certainty: 1.0, cites: [{source: S1, locator: "paragraphs 1–2"}, {source: S2, locator: "p. 197"}], how_known: "Two sources."}

contribution:
  fields: {value: ["stellar photometry", "variable stars"], certainty: 1.0, cites: [{source: S1, locator: "paragraphs 2–4"}, {source: S2, locator: "pp. 197–198"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Period–luminosity relation of Cepheid variables (from 25 variables in the Magellanic Clouds)", year: "1912", kind: "law or principle", lasting: "the basis of Cepheid distances, used by Hubble, Shapley and others", certainty: 1.0, cites: [{source: S1, locator: "Cepheid paragraph"}, {source: S2, locator: "p. 198"}], how_known: "Two sources."}
    - {value: "North Polar Sequence and standard photographic magnitudes, adopted for the Astrographic Map of the Sky", year: "1912–1917", kind: method, lasting: "in general use until photoelectric photometry", certainty: 1.0, cites: [{source: S1, locator: "paragraphs 3–4"}, {source: S2, locator: "pp. 197–198"}], how_known: "Two sources."}
    - {value: "Discovery of about 2,400 variable stars and 4 novae", year: "by 1921", kind: discovery, lasting: "more than half of the variables known by 1930", certainty: 1.0, cites: [{source: S1, locator: "paragraph 4"}, {source: S2, locator: "p. 198"}], how_known: "Two sources give the totals by her death; neither dates her first discoveries, so the item has no start year and does not set first_lasting_contribution_year (decision P12). Was dated '1900s–1921' until the batch 4 lens audit."}
  evidence_of_impact:
    - {value: "Hubble used her relation in 1924 for the first distance to a galaxy beyond the Milky Way (Andromeda)", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S1, locator: "Cepheid paragraph"}], how_known: "Britannica."}
  major_works:
    - {value: "The North Polar Sequence (Annals of the Harvard College Observatory 71, no. 3)", year: 1917, kind: "paper or paper series", certainty: 0.7, cites: [{source: S2, locator: "pp. 197–198"}, {source: S1, locator: "paragraph 3 ('published in 1912 and 1917')"}], how_known: "Bailey gives Annals 71, No. 3; year from Britannica."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "The period–luminosity relation made the cosmic distance scale possible.", certainty: 0.7, cites: [{source: S1, locator: "Cepheid paragraph"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Protestant minister's family (father the Rev. George Roswell Leavitt); Puritan ancestry", certainty: 0.7, cites: [{source: S2, locator: "p. 197"}], how_known: "Bailey's obituary; the denomination is not named there."}
  family_religious_practice: {value: TODO, note: "Not described in the sources read."}
  parents_and_household:
    - {value: "Father, the Rev. George Roswell Leavitt, a descendant of Jordan Leavitt (Hingham, 1640)", name: "George Roswell Leavitt", role: father, certainty: 0.7, cites: [{source: S2, locator: "p. 197"}], how_known: "Bailey."}
  household_circumstances: {value: "Old New England colonial family on both sides", certainty: 0.7, cites: [{source: S2, locator: "p. 197"}], how_known: "Bailey."}
  schooling:
    - {value: "Oberlin College", stage: university, years: "1886–1888", certainty: 0.7, cites: [{source: S1, locator: "paragraph 1"}], how_known: "Britannica."}
    - {value: "Society for the Collegiate Instruction of Women (later Radcliffe College), graduated 1892", stage: university, years: "1888–1892", certainty: 1.0, cites: [{source: S1, locator: "paragraph 1"}, {source: S2, locator: "p. 197"}], how_known: "Two sources."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Interest in astronomy aroused in her senior year at college", certainty: 0.7, cites: [{source: S1, locator: "paragraph 1"}], how_known: "Britannica."}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [English], certainty: 0.7, cites: [{source: S2, locator: "p. 197"}], how_known: "New England family."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1912–1921", certainty: 0.7, cites: [{source: S1, locator: "paragraphs 2–5"}], how_known: "Equal to timing.major_work_period (P30 addendum f; span check 2026-10-02). Was 1895–1921: Volunteer at the Harvard Observatory to death."}
  nominal_affiliations:
    - {value: "Church member (denomination not named): 'deeply conscientious and sincere in her attachment to her religion and church'", years: "–1921", role: "member", certainty: 0.7, cites: [{source: S2, locator: "p. 197"}], how_known: "A colleague's obituary (one source)."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No writing of hers on science and religion was found."}
  primary_system:
    value: BELOW_THRESHOLD
    cites: [{source: S2, locator: "p. 197"}]
    how_known: "Only a colleague's character sketch: she 'inherited in a somewhat chastened form the stern virtues of her puritan ancestors' and was sincere in her attachment to 'her religion and church'. That is another person's description, not her words, and church attachment is never a code on its own (CODING_GUIDE §1), and another person's description is not her words (CODING_GUIDE §7)."
    note: "Candidate: CHRIST. Would need her letters (Harvard University Archives, Harvard College Observatory records) or a biography that quotes her."
  secondary_system: {value: UNKNOWN, how_known: "No system evidence in the sources read."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Leading candidate, not coded (BELOW_THRESHOLD): minister's daughter, sincere church attachment as reported by Bailey; no statement of her own read.", cites: [{source: S2, locator: "p. 197"}]}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "No statement placing or denying God was read.", note: "Stays BELOW_THRESHOLD (P19): her colleague Solon Bailey's memorial sketch of her church attachment is another person's report, which bears on the point but cannot score it."}
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      cites: [{source: S1, locator: "Cepheid paragraph"}, {source: S2, locator: "p. 198"}]
      how_known: "Coder's reading of her working science, as P6 directs (same treatment as Fermi and Dirac). No statement of hers about miracles read, so 0.5."
      rationale: "Scored on her account of nature (P6). Her work found that a Cepheid's period 'is highly regular and is determined by the actual luminosity of the star' (S1), a law derived from measured cases (S2, p. 198) that others then applied to stars everywhere. No miracle, petition or exemption in anything read. P35 (v8's pick, 2026-10-08, lens audit of batch C ruling R1): B inferred only from a scientist's working science, with no statement of their own on law and exception, is B 3 at 0.5 with 4 as the named alternative, never 4, because working science cannot tell a lawful nature with one stated exception from one with none (Faraday, Maxwell and Newton did the same kind of science and are B 3 from their own statements). Named alternative: 4, if a statement of their own shows no exception."
    C_ledger: {value: UNKNOWN, how_known: "Nothing on judgement, afterlife or reward in the sources read."}
    D_authority: {value: UNKNOWN, how_known: "No statement on revelation in the sources read."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Nothing read addresses favour for a group in events. Working science bears on the first question (same laws everywhere) but not on favour for a group in events, so E stays BELOW_THRESHOLD; not scored from working science alone (P19)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD and B_cause is only 0.5, under the P4 test's 0.7 bar."}
  statements: []
  changes_over_life: []
  coder_notes: "No writing of hers on religion was found, so statements is empty. S2 is a colleague's obituary read on the NASA ADS page scans (a library scan, authoritative under §7); its remarks on her religion and character are Bailey's, not hers, and score nothing. No interview used. The 1912 Harvard circular announcing the period–luminosity relation was not read directly and is not listed in major_works."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Old New England colonial (Puritan) ancestry on both sides", certainty: 0.7, cites: [{source: S2, locator: "p. 197"}], how_known: "Bailey."}
  religious_heritage_by_birth: {value: "Protestant (Puritan ancestry; minister father)", certainty: 0.7, cites: [{source: S2, locator: "p. 197"}], how_known: "Bailey."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1912–1921", certainty: 0.7, cites: [{source: S1, locator: "paragraphs 2–5"}], how_known: "From the period–luminosity relation (1912) to the variable-star count ('by 1921', an inclusive bound, so 1921), the first and last listed lasting contributions (P29). Span check 2026-10-02 (P29, P30 and its addendum): was 1907–1921, which started with Pickering's 1907 plan, not a listed contribution."}
  age_at_first_lasting_contribution: {value: 44, certainty: 0.7, cites: [{source: S1, locator: "opening; Cepheid paragraph"}], how_known: "Born July 1868; discovery 1912 (age 43 or 44 depending on the month). P30 (rule 5): 1912 − 1868 = 44, with no month adjustment; was 43 until the P30 age sweep (2026-10-02)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No worldview statement of hers found."}
  lio_views_relative_to_major_work: {value: "unclear", rationale: "No worldview statement of hers found.", certainty: 0.5, cites: [{source: S2, locator: "p. 197"}], how_known: "Nothing to date."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Measurement and empirical law-finding from photographic plates (S1; S2), not derivation from definitions and axioms.", certainty: 0.5, cites: [{source: S1, locator: "paragraphs 2–5"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "paragraph 1"}], how_known: "Nothing on method in her schooling."}
  circle_present: {value: "unclear", rationale: "No God-Nature statement found; not scored from absence.", certainty: 0.5, cites: [{source: S2, locator: "p. 197"}], how_known: "No evidence either way."}
  reading: "As belief, not finding: form absent, circle unclear. The record does not test H1."
  notes: ""

institutions:
  - {value: "Harvard College Observatory", role: "volunteer assistant (1895), permanent staff (1902), head of photographic stellar photometry", years: "1895–1921", kind: employer, certainty: 1.0, cites: [{source: S1, locator: "paragraphs 1–2"}, {source: S2, locator: "p. 197"}], how_known: "Two sources."}
collaborators:
  - {value: "Edward C. Pickering", relation: "mentor or employer", note: "observatory director; she was 'closely associated' with him for the rest of her life", certainty: 1.0, cites: [{source: S2, locator: "p. 197"}, {source: S1, locator: "paragraph 1"}], how_known: "Two sources."}
  - {value: "Annie Jump Cannon", roster_id: cannon-annie-jump, relation: collaborator, note: "fellow staff member on the brightness project", certainty: 0.7, cites: [{source: S1, locator: "paragraph 1"}], how_known: "Britannica."}
  - {value: "Williamina Fleming", relation: collaborator, note: "older colleague on the same project", certainty: 0.7, cites: [{source: S1, locator: "paragraph 1"}], how_known: "Britannica."}
  - {value: "Edwin Hubble", roster_id: hubble-edwin, relation: influenced, note: "used her relation for the Andromeda distance (1924)", certainty: 0.7, cites: [{source: S1, locator: "Cepheid paragraph"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3: DeepSeek, Gemini, GPT).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 179"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "No first-hand worldview source; only a colleague's obituary."
    - "Britannica article is unsigned (Britannica editors)."
  open_questions:
    - "Search the Harvard College Observatory records and her correspondence (Harvard University Archives) for any statement on religion; check the denomination of her father's ministry and her own church."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "The Editors of Encyclopaedia Britannica"
    citation: "The Editors of Encyclopaedia Britannica. \"Henrietta Swan Leavitt.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Henrietta-Swan-Leavitt."
    url: "https://www.britannica.com/biography/Henrietta-Swan-Leavitt"
    accessed: 2026-10-02
    reliability_note: "Unsigned article (one page). Paragraphs counted from the opening '(born July 4, 1868'."
    used_for: [identity, basics, contribution, childhood, worldview, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "journal article"
    author: "Solon I. Bailey"
    year: 1922
    citation: "Bailey, Solon I. \"Henrietta Swan Leavitt.\" Popular Astronomy 30, no. 4 (April 1922): 197–199. NASA ADS scan, bibcode 1922PA.....30..197B, https://ui.adsabs.harvard.edu/abs/1922PA.....30..197B/abstract."
    url: "https://ui.adsabs.harvard.edu/abs/1922PA.....30..197B/abstract"
    accessed: 2026-10-02
    reliability_note: "Obituary by a Harvard Observatory colleague, dated Cambridge, January 1922; read on the ADS page images (library scan). Printed page numbers."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
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

# Henrietta Swan Leavitt

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Henrietta Swan Leavitt (1868–1921), American astronomer at the Harvard College Observatory, discovered the period–luminosity relation of Cepheid variables (1912) and set standard photographic magnitudes [S1; S2]. No writing of hers on religion was found; her colleague Solon Bailey wrote that she was "deeply conscientious and sincere in her attachment to her religion and church" [S2, p. 197]. primary_system BELOW_THRESHOLD (CHRIST candidate). B 3 at 0.5 from the working science (alternative 4, P35); A and E below threshold, C and D UNKNOWN; mid_basin below threshold.

## Life and work

Oberlin, then Radcliffe (1892); volunteer at the Harvard Observatory from 1895 and staff from 1902; head of photographic stellar photometry [S1; S2].

## Contribution and impact

Period–luminosity relation, the North Polar Sequence, about 2,400 variables and 4 novae [S1; S2].

## Childhood and education

Daughter of the Rev. George Roswell Leavitt, of old New England stock [S2, p. 197].

## Adult working worldview

Not established from her own words. Bailey's description is a colleague's [S2, p. 197] and scores nothing.

## Heritage (context only)

Puritan New England ancestry [S2]. Context only.

## Timing

First lasting contribution 1912, at 44 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form absent; circle unclear.

## Open questions

- Her correspondence in the Harvard archives.

## Research log

- 2026-10-02: Read Britannica and Bailey's obituary on the ADS page images (pp. 197–199).
