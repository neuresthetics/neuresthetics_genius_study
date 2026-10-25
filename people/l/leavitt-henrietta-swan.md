---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 6
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, fourth batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (fourth batch, RUNBOOK §1 order). Basics from Britannica and Solon I. Bailey's obituary (Popular Astronomy 30, 1922, pp. 197–199), read in the NASA ADS page scan. No writing of hers on religion was found; Bailey, a colleague, describes her as 'deeply conscientious and sincere in her attachment to her religion and church' and names her father as the Rev. George Roswell Leavitt. primary_system BELOW_THRESHOLD (CHRIST candidate). B 4 at 0.5 from her working science (P6); A, C, D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. No interview used. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 4 (two blind runs at b21655b). #109 (both runs): the no-code note wrongly cited 'decision P9: paraphrase alone cannot score'; it now cites CODING_GUIDE §1 (church attachment is never a code on its own) and §7 (another person's description is not her words). Decision P12 recheck: the variable-star item '1900s–1921' → 'by 1921' (sources give totals only), so it does not set the year; first_lasting_contribution_year stays 1912, with a flag that a dated source could move it earlier. No coded value changed. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02). Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs; BELOW_THRESHOLD vs UNKNOWN per P19; basis inference_from_work for 0.5 inference from working science (P24). Full before → after list: reports/stage3_rulings_changes.csv. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "P30 rule 5 age sweep: ages recomputed as event year − birth year, with no month adjustment (scripts/recompute_ages.py; every change is in reports/p30_age_changes.csv). No other value changed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Span alignment (P29, P30 and its addendum): timing.major_work_period 1907–1921 → 1912–1921; worldview.working_years 1895–1921 → 1912–1921, equal to the span (P30 addendum f); evidence for every headline value checked against the span; no value or certainty changed. Listed in reports/p30_span_alignment.csv. Not reviewed."}
    - {date: 2026-10-08, by: "Grok Bot", summary: "Lens audit of batch C (dd91009), ruling R1, logged as P35 (v8's pick): B_cause 4 → 3 at 0.5, alternative 4, because B rests on working science only. No other value changes; mid_basin unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #169, F 3, rank 179). Goals: find her own words if any; otherwise keep silence; do not force plot. Hunt: MacTutor (S4) — father Congregationalist minister (Pilgrim Congregational Cambridge; later Beloit First Congregational); funeral Chapel of the First Congregational Church 14 Dec 1921; Pickering letters 1902 on eyes/hearing/employment only (no religion). Circular 173 (S5) read in full (UCLA CWP transcription) — pure working science; 'simple relation between the brightness of the variables and their periods'; no God/miracle/exception language. Johnson Miss Leavitt's Stars (via secondary): 'No diary has been found' (PBS SoCal / Johnson). Wikipedia 'remained deeply religious' (P50) cites Lightman Discoveries — secondary paraphrase of Bailey, not own words; unused for A/primary (§7). primary BELOW_THRESHOLD kept (CHRIST lead from Bailey + Congregational heritage only). A BELOW kept. B 3 @0.5 inference_from_work kept (P35); support: corroborated (P48) S1+S2+S5. mid BELOW; not plotted. Chart-moving NO. P47 source_quality on S1–S5. major_works gains 1912 Circular 173. Congregational denomination filled in heritage/family. No fallacy_catalog; no figures/. Draft, not reviewed."}

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
  first_lasting_contribution_year: {value: 1912, certainty: 1.0, cites: [{source: S1, locator: "'Leavitt's outstanding achievement was her discovery in 1912'"}, {source: S2, locator: "p. 198 ('the important law was derived')"}, {source: S5, locator: "title / March 3, 1912"}], how_known: "Period–luminosity relation for Cepheid variables, the earliest dated listed contribution (decisions P12, P13). Circular 173 (S5) is the 1912 announcement. The variable-star discoveries ('by 1921') have no dated start in the sources read; a source dating her first discoveries before 1912 would move the year earlier."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "Cepheid paragraph"}], how_known: "From first_lasting_contribution_year (P2)."}
  region_of_birth: {value: "North America", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "USA is North America in data/reference/regions.csv (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "paragraph 1"}], how_known: "Harvard College Observatory."}
  sex_as_recorded: {value: "female", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "p. 197"}], how_known: "As the sources record it."}
  languages_of_work: {value: [English], certainty: 0.7, cites: [{source: S2, locator: "p. 198 (Harvard Annals and Circulars)"}, {source: S5, locator: "whole circular"}], how_known: "Published in the Harvard Observatory's English series."}
  occupations: {value: ["astronomer", "head of photographic stellar photometry, Harvard College Observatory"], certainty: 1.0, cites: [{source: S1, locator: "paragraphs 1–2"}, {source: S2, locator: "p. 197"}], how_known: "Two sources."}

contribution:
  fields: {value: ["stellar photometry", "variable stars"], certainty: 1.0, cites: [{source: S1, locator: "paragraphs 2–4"}, {source: S2, locator: "pp. 197–198"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Period–luminosity relation of Cepheid variables (from 25 variables in the Magellanic Clouds)", year: "1912", kind: "law or principle", lasting: "the basis of Cepheid distances, used by Hubble, Shapley and others", certainty: 1.0, cites: [{source: S1, locator: "Cepheid paragraph"}, {source: S2, locator: "p. 198"}, {source: S5, locator: "whole circular"}], how_known: "Two secondary sources plus her Circular 173 text."}
    - {value: "North Polar Sequence and standard photographic magnitudes, adopted for the Astrographic Map of the Sky", year: "1912–1917", kind: method, lasting: "in general use until photoelectric photometry", certainty: 1.0, cites: [{source: S1, locator: "paragraphs 3–4"}, {source: S2, locator: "pp. 197–198"}], how_known: "Two sources."}
    - {value: "Discovery of about 2,400 variable stars and 4 novae", year: "by 1921", kind: discovery, lasting: "more than half of the variables known by 1930", certainty: 1.0, cites: [{source: S1, locator: "paragraph 4"}, {source: S2, locator: "p. 198"}], how_known: "Two sources give the totals by her death; neither dates her first discoveries, so the item has no start year and does not set first_lasting_contribution_year (decision P12). Was dated '1900s–1921' until the batch 4 lens audit."}
  evidence_of_impact:
    - {value: "Hubble used her relation in 1924 for the first distance to a galaxy beyond the Milky Way (Andromeda)", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S1, locator: "Cepheid paragraph"}], how_known: "Britannica."}
  major_works:
    - {value: "Periods of 25 Variable Stars in the Small Magellanic Cloud (Harvard College Observatory Circular 173)", year: 1912, kind: "paper or paper series", certainty: 1.0, cites: [{source: S5, locator: "title / Pickering preface ('prepared by Miss Leavitt')"}, {source: S1, locator: "Cepheid paragraph"}], how_known: "The circular itself (S5) plus Britannica."}
    - {value: "The North Polar Sequence (Annals of the Harvard College Observatory 71, no. 3)", year: 1917, kind: "paper or paper series", certainty: 0.7, cites: [{source: S2, locator: "pp. 197–198"}, {source: S1, locator: "paragraph 3 ('published in 1912 and 1917')"}], how_known: "Bailey gives Annals 71, No. 3; year from Britannica."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "The period–luminosity relation made the cosmic distance scale possible.", certainty: 0.7, cites: [{source: S1, locator: "Cepheid paragraph"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Congregationalist minister's family (father the Rev. George Roswell Leavitt, D.D.); Puritan ancestry", certainty: 1.0, cites: [{source: S2, locator: "p. 197"}, {source: S4, locator: "parents / Congregationalist minister paragraphs"}], how_known: "Bailey names the minister father; MacTutor names the Congregational denomination and Andover Theological Seminary doctorate."}
  family_religious_practice: {value: "Father's successive Congregational pastorates (Pilgrim Congregational Church, Cambridge; Plymouth Congregational, Cleveland; First Congregational, Beloit); household lived near the Cambridge church", certainty: 0.7, cites: [{source: S4, locator: "Cambridge / Beloit pastorate paragraphs"}], how_known: "MacTutor biography (one signed scholarly source → 0.7)."}
  parents_and_household:
    - {value: "Father, the Rev. George Roswell Leavitt, Congregationalist minister (Williams College; Andover Theological Seminary D.D.); descendant of Jordan Leavitt (Hingham, 1640)", name: "George Roswell Leavitt", role: father, certainty: 1.0, cites: [{source: S2, locator: "p. 197"}, {source: S4, locator: "parents paragraphs"}], how_known: "Bailey and MacTutor."}
    - {value: "Mother, Henrietta Swan Kendrick", name: "Henrietta Swan Kendrick", role: mother, certainty: 0.7, cites: [{source: S4, locator: "parents paragraphs"}], how_known: "MacTutor."}
  household_circumstances: {value: "Old New England colonial family on both sides; relatively well educated; siblings included Darwin Ashley Leavitt (later a Congregationalist minister) and George William Leavitt (missionary)", certainty: 0.7, cites: [{source: S2, locator: "p. 197"}, {source: S4, locator: "siblings / Beloit 1909 paragraphs"}], how_known: "Bailey for colonial stock; MacTutor for siblings' later vocations."}
  schooling:
    - {value: "Oberlin College (preparatory then undergraduate)", stage: university, years: "1885–1888", certainty: 0.7, cites: [{source: S1, locator: "paragraph 1"}, {source: S4, locator: "Oberlin paragraphs"}], how_known: "Britannica and MacTutor; MacTutor dates prep 1885–86 and undergrad 1886–88."}
    - {value: "Society for the Collegiate Instruction of Women (later Radcliffe College), graduated 1892", stage: university, years: "1888–1892", certainty: 1.0, cites: [{source: S1, locator: "paragraph 1"}, {source: S2, locator: "p. 197"}], how_known: "Two sources."}
  early_mathematics: {value: "advanced mathematics", note: "Radcliffe: analytic geometry and differential calculus (grade A); introductory physics; senior-year astronomy (A−)", certainty: 0.7, cites: [{source: S4, locator: "Radcliffe course paragraphs"}], how_known: "MacTutor."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Nothing on proof-style training in the sources read."}
  early_science_exposure:
    - {value: "Interest in astronomy aroused in her senior year at college; astronomy course taken at the Harvard Observatory", certainty: 0.7, cites: [{source: S1, locator: "paragraph 1"}, {source: S4, locator: "final-year astronomy"}], how_known: "Britannica and MacTutor."}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [English], certainty: 0.7, cites: [{source: S2, locator: "p. 197"}], how_known: "New England family."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1912–1921", certainty: 0.7, cites: [{source: S1, locator: "paragraphs 2–5"}], how_known: "Equal to timing.major_work_period (P30 addendum f; span check 2026-10-02). Was 1895–1921: Volunteer at the Harvard Observatory to death."}
  nominal_affiliations:
    - {value: "Congregational church member (denomination from father's Congregational ministry and her funeral at the Chapel of the First Congregational Church, Cambridge): Bailey — 'deeply conscientious and sincere in her attachment to her religion and church'", years: "–1921", role: "member", certainty: 0.7, cites: [{source: S2, locator: "p. 197"}, {source: S4, locator: "funeral 14 December 1921"}], how_known: "Colleague's obituary plus funeral location (MacTutor); still not her own words on creed."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No writing of hers on science and religion was found (S1–S5; deepen 2026-10-24)."}
  primary_system:
    value: BELOW_THRESHOLD
    cites: [{source: S2, locator: "p. 197"}, {source: S4, locator: "funeral / Congregationalist-father paragraphs"}]
    how_known: "Only a colleague's character sketch (S2) plus Congregational heritage and funeral place (S4). That is another person's description and institutional context, not her words; church attachment is never a code on its own (CODING_GUIDE §1), and another person's description is not her words (CODING_GUIDE §7)."
    note: "Candidate: CHRIST. Deepen D1 (2026-10-24) read MacTutor, Circular 173, and secondary Johnson/PBS notes; still no own-voice creed. Wikipedia/Lightman 'deeply religious' is secondary paraphrase of Bailey (P50) — unused. Would need Harvard University Archives letters or a biography that quotes her on religion."
  secondary_system: {value: UNKNOWN, how_known: "No system evidence in the sources read."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Leading candidate, not coded (BELOW_THRESHOLD): Congregational minister's daughter; Bailey's church-attachment sketch; funeral at First Congregational Chapel; no statement of her own read.", cites: [{source: S2, locator: "p. 197"}, {source: S4, locator: "funeral / parents paragraphs"}]}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "No statement placing or denying God was read in S1–S5 (deepen 2026-10-24).", note: "Stays BELOW_THRESHOLD (P19): Bailey's memorial sketch of her church attachment and Congregational funeral place are another person's report / institutional context, which bear on the point but cannot score it (§7). Wikipedia/Lightman paraphrase unused (P50)."}
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      support: corroborated
      cites: [{source: S1, locator: "Cepheid paragraph"}, {source: S2, locator: "p. 198"}, {source: S5, locator: "period–brightness paragraphs ('simple relation'; 'associated with their actual emission of light')"}]
      how_known: "Coder's reading of her working science, as P6 directs (same treatment as Fermi and Dirac). No statement of hers about miracles or exceptions read, so 0.5. Three independent source ids describing the same period–luminosity program → corroborated (P48)."
      rationale: "Scored on her account of nature (P6). Her Circular 173 states a 'simple relation between the brightness of the variables and their periods' and that periods are 'apparently associated with their actual emission of light, as determined by their mass, density, and surface brightness' (S5) — a law derived from measured cases that others then applied to stars everywhere (S1; S2, p. 198). No miracle, petition or exemption in anything read. P35 (v8's pick, 2026-10-08, lens audit of batch C ruling R1): B inferred only from a scientist's working science, with no statement of their own on law and exception, is B 3 at 0.5 with 4 as the named alternative, never 4, because working science cannot tell a lawful nature with one stated exception from one with none (Faraday, Maxwell and Newton did the same kind of science and are B 3 from their own statements). Named alternative: 4, if a statement of their own shows no exception. Circular 173 does not lift the basis above inference_from_work: it states the empirical relation, not a no-exception claim about nature (P35, P49)."
    C_ledger: {value: UNKNOWN, how_known: "Nothing on judgement, afterlife or reward in the sources read."}
    D_authority: {value: UNKNOWN, how_known: "No statement on revelation in the sources read."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Nothing read addresses favour for a group in events. Working science bears on the first question (same laws everywhere) but not on favour for a group in events, so E stays BELOW_THRESHOLD; not scored from working science alone (P19)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD and B_cause is only 0.5, under the P4 test's 0.7 bar."}
  statements: []
  changes_over_life: []
  coder_notes: "Deepen D1 2026-10-24: No writing of hers on religion found; statements stays empty. S2 Bailey remains a colleague's obituary (§7) — scores nothing for A/primary. S4 MacTutor fills Congregational denomination, funeral place, and Pickering-letter context (eyes/hearing/employment only). S5 Circular 173 is her own scientific text ('prepared by Miss Leavitt') — strengthens working-science B corroboration, does not lift P35. Johnson (via PBS SoCal): no diary found. Wikipedia/Lightman 'deeply religious' unused (P50). No interview used."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Old New England colonial (Puritan) ancestry on both sides", certainty: 0.7, cites: [{source: S2, locator: "p. 197"}], how_known: "Bailey."}
  religious_heritage_by_birth: {value: "Congregationalist (Puritan ancestry; Congregational minister father)", certainty: 1.0, cites: [{source: S2, locator: "p. 197"}, {source: S4, locator: "Congregationalist minister paragraphs"}], how_known: "Bailey and MacTutor."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not in the sources read (S1–S5)."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not in the sources read (S1–S5)."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1912–1921", certainty: 0.7, cites: [{source: S1, locator: "paragraphs 2–5"}, {source: S5, locator: "March 3, 1912"}], how_known: "From the period–luminosity relation (1912 Circular 173) to the variable-star count ('by 1921', an inclusive bound, so 1921), the first and last listed lasting contributions (P29). Span check 2026-10-02 (P29, P30 and its addendum): was 1907–1921, which started with Pickering's 1907 plan, not a listed contribution."}
  age_at_first_lasting_contribution: {value: 44, certainty: 0.7, cites: [{source: S1, locator: "opening; Cepheid paragraph"}], how_known: "Born July 1868; discovery 1912 (age 43 or 44 depending on the month). P30 (rule 5): 1912 − 1868 = 44, with no month adjustment; was 43 until the P30 age sweep (2026-10-02)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No worldview statement of hers found at the LIO-type-view bar (P27); B rests on working science, which is not an LIO-type view."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "Nothing of hers on God or nature was read at the LIO-type-view bar (P27).", certainty: 0.5, cites: [{source: S2, locator: "p. 197"}, {source: S5, locator: "whole circular"}], how_known: "Absence in the sources read; not evidence of absence."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "No LIO-type views of hers dated to the span; B is working-science inference only (P27, P35)."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Measurement and empirical law-finding from photographic plates (S1; S2; S5), not derivation from definitions and axioms.", certainty: 0.5, cites: [{source: S1, locator: "paragraphs 2–5"}, {source: S5, locator: "measurement paragraphs"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "paragraph 1"}, {source: S4, locator: "Radcliffe mathematics"}], how_known: "Secondary evidence of calculus/geometry coursework only; unclear for geometric form."}
  circle_present: {value: "unclear", rationale: "No God-Nature statement found; not scored from absence.", certainty: 0.5, cites: [{source: S2, locator: "p. 197"}, {source: S5, locator: "whole circular"}], how_known: "No evidence either way."}
  reading: "As belief, not finding: form absent, circle unclear. The record does not test H1."
  notes: ""

institutions:
  - {value: "Harvard College Observatory", role: "volunteer assistant (1895), permanent staff (1902), head of photographic stellar photometry", years: "1895–1921", kind: employer, certainty: 1.0, cites: [{source: S1, locator: "paragraphs 1–2"}, {source: S2, locator: "p. 197"}], how_known: "Two sources."}
collaborators:
  - {value: "Edward C. Pickering", relation: "mentor or employer", note: "observatory director; she was 'closely associated' with him for the rest of her life; Circular 173 issued under his name, prepared by her", certainty: 1.0, cites: [{source: S2, locator: "p. 197"}, {source: S1, locator: "paragraph 1"}, {source: S5, locator: "Pickering preface"}], how_known: "Two secondary sources plus the circular."}
  - {value: "Annie Jump Cannon", roster_id: cannon-annie-jump, relation: collaborator, note: "fellow staff member on the brightness project", certainty: 0.7, cites: [{source: S1, locator: "paragraph 1"}], how_known: "Britannica."}
  - {value: "Williamina Fleming", relation: collaborator, note: "older colleague on the same project", certainty: 0.7, cites: [{source: S1, locator: "paragraph 1"}], how_known: "Britannica."}
  - {value: "Edwin Hubble", roster_id: hubble-edwin, relation: influenced, note: "used her relation for the Andromeda distance (1924)", certainty: 0.7, cites: [{source: S1, locator: "Cepheid paragraph"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3: DeepSeek, Gemini, GPT).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 179"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "No first-hand worldview source on religion; Bailey (colleague obituary) and Congregational funeral place only (§7)."
    - "Britannica article is unsigned (Britannica editors)."
    - "Wikipedia/Lightman 'deeply religious' is secondary paraphrase of Bailey — unused for scoring (P50)."
  open_questions:
    - "Harvard University Archives / Harvard College Observatory correspondence for any statement of hers on religion (Pickering letters read via MacTutor are employment/health only)."
    - "George Johnson, Miss Leavitt's Stars (2005) full text — secondary notes say no diary found; confirm whether any letter quotes religion."
    - "Parish or church membership rolls for her own Congregational affiliation (funeral place alone is not a creed)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "The Editors of Encyclopaedia Britannica"
    citation: "The Editors of Encyclopaedia Britannica. \"Henrietta Swan Leavitt.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Henrietta-Swan-Leavitt."
    url: "https://www.britannica.com/biography/Henrietta-Swan-Leavitt"
    accessed: 2026-10-02
    reliability_note: "Unsigned article (one page). Paragraphs counted from the opening '(born July 4, 1868'."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "journal article"
    author: "Solon I. Bailey"
    year: 1922
    citation: "Bailey, Solon I. \"Henrietta Swan Leavitt.\" Popular Astronomy 30, no. 4 (April 1922): 197–199. NASA ADS scan, bibcode 1922PA.....30..197B, https://ui.adsabs.harvard.edu/abs/1922PA.....30..197B/abstract."
    url: "https://ui.adsabs.harvard.edu/abs/1922PA.....30..197B/abstract"
    accessed: 2026-10-02
    reliability_note: "Obituary by a Harvard Observatory colleague, dated Cambridge, January 1922; read on the ADS page images (library scan). Printed page numbers. Colleague description — not her words (§7)."
    source_quality: "scholarly edition or monograph"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S4
    type: secondary
    kind: "institutional page"
    author: "J. J. O'Connor and E. F. Robertson"
    year: 2017
    citation: "O'Connor, J. J., and E. F. Robertson. \"Henrietta Swan Leavitt.\" MacTutor History of Mathematics, University of St Andrews, August 2017. https://mathshistory.st-andrews.ac.uk/Biographies/Leavitt/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Leavitt/"
    accessed: 2026-10-24
    reliability_note: "Signed scholarly biography. Used for Congregational denomination, funeral place, parents/siblings, Radcliffe mathematics, and quoted Pickering correspondence (employment/health only — no religion)."
    source_quality: "reference entry"
    used_for: [childhood, worldview, heritage, timing, lane_b, review]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Henrietta S. Leavitt (statement prepared by; issued under Edward C. Pickering)"
    year: 1912
    citation: "Leavitt, Henrietta S., and Edward C. Pickering. \"Periods of 25 Variable Stars in the Small Magellanic Cloud.\" Harvard College Observatory Circular 173 (March 3, 1912): 1–3. Transcription: UCLA CWP, http://cwp.library.ucla.edu/articles/leavitt/leavitt.note.html. ADS bibcode 1912HarCi.173....1L."
    url: "http://cwp.library.ucla.edu/articles/leavitt/leavitt.note.html"
    accessed: 2026-10-24
    reliability_note: "Pickering preface states the statement was 'prepared by Miss Leavitt'. Read in the UCLA CWP HTML transcription (authoritative library copy of the scientific text). Pure working science — no religion language."
    source_quality: "primary / own words"
    used_for: [basics, contribution, worldview, timing, lane_b]
---

# Henrietta Swan Leavitt

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Henrietta Swan Leavitt (1868–1921), American astronomer at the Harvard College Observatory, discovered the period–luminosity relation of Cepheid variables (1912 Circular 173) and set standard photographic magnitudes [S1; S2; S5]. No writing of hers on religion was found; her colleague Solon Bailey wrote that she was "deeply conscientious and sincere in her attachment to her religion and church" [S2, p. 197]. She was the daughter of a Congregationalist minister and her funeral was held at the Chapel of the First Congregational Church, Cambridge [S4]. primary_system BELOW_THRESHOLD (CHRIST candidate). B 3 at 0.5 from the working science (alternative 4, P35; support corroborated); A and E below threshold, C and D UNKNOWN; mid_basin below threshold. Not plotted.

## Life and work

Oberlin (1885–1888), then Radcliffe (1892); volunteer at the Harvard Observatory from 1895 and staff from 1902; head of photographic stellar photometry [S1; S2; S4]. Progressive hearing loss; Pickering letters of 1902 concern eyes, hearing, and employment, not religion [S4].

## Contribution and impact

Period–luminosity relation (Circular 173, 1912), the North Polar Sequence, about 2,400 variables and 4 novae [S1; S2; S5]. Hubble used the relation for the Andromeda distance [S1].

## Childhood and education

Daughter of the Rev. George Roswell Leavitt, Congregationalist minister, and Henrietta Swan Kendrick, of old New England stock [S2, p. 197; S4]. Radcliffe coursework included analytic geometry, differential calculus, and senior-year astronomy [S4].

## Adult working worldview

Not established from her own words. Bailey's description is a colleague's [S2, p. 197] and scores nothing (§7). Circular 173 is working science only [S5]. Congregational heritage and funeral place are context, not a code [S4].

## Heritage (context only)

Puritan New England ancestry; Congregationalist by birth (minister father) [S2; S4]. Context only — never a worldview code.

## Timing

First lasting contribution 1912, at 44 [S1; S5]. Span 1912–1921. No LIO-type views of hers found relative to the span.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form absent; circle unclear.

## Open questions

- Harvard College Observatory / University Archives correspondence for any religious statement.
- Full Johnson *Miss Leavitt's Stars* (2005) for any quoted letters on religion (secondary notes: no diary found).
- Church membership rolls beyond funeral place.

## Research log

- 2026-10-02: Read Britannica and Bailey's obituary on the ADS page images (pp. 197–199).
- 2026-10-24 (deepen D1): Read MacTutor biography (S4); Circular 173 full text via UCLA CWP (S5); checked Wikipedia/Lightman (P50 unused); Johnson/PBS secondary notes (no diary). Kept silence on A/primary. Chart-moving NO.
