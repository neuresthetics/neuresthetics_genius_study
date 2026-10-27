---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 7
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, fourth batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to chemistry. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (fourth batch, RUNBOOK §1 order). Included by owner decision, borderline on the stage-2 date window (radiocarbon dating 1947–49; Jason, 2026-10-02). Basics from Britannica (Kauffman), the Nobel biography and Leona Marshall Libby's GSA memorial. No writing of his on religion was found. primary_system BELOW_THRESHOLD (no candidate supported). B 4 at 0.5 from his working science (P6); A, C, D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. No interview used. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 4 (two blind runs at b21655b). #148 (run 1) / decisions P12, P13: first_lasting_contribution_year 1947 → 1941, the start year of the earliest listed contribution (the gaseous-diffusion barrier, Manhattan Project 1941–1945; Britannica, and S3 p. 1 for its lasting use); age 38 → 32; era unchanged. The how_known no longer says the 1930s work is lasting per S3 (S3 does not say so); that work is not listed and does not set the year. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02). Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs; BELOW_THRESHOLD vs UNKNOWN per P19; basis inference_from_work for 0.5 inference from working science (P24). Full before → after list: reports/stage3_rulings_changes.csv. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "P30 rule 5 age sweep: ages recomputed as event year − birth year, with no month adjustment (scripts/recompute_ages.py; every change is in reports/p30_age_changes.csv). No other value changed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Span alignment (P29, P30 and its addendum): timing.major_work_period 1946–1952 → 1941–1947; worldview.working_years 1931–1980 → 1941–1947, equal to the span (P30 addendum f); evidence for every headline value checked against the span; no value or certainty changed. Listed in reports/p30_span_alignment.csv. Not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #211/228, F 3, rank 224). Goals: firm B with corroboration if possible; seek any A; do not force plot. Opened Nobel Lecture 12 Dec 1960 (S5, primary / own words); Wikipedia EN dual bio (S6, P50); NNDB 'Agnostic' label checked and rejected as unsupported tertiary (no scholarly reconstruction comparable to Segrè on Fermi). B_cause stays 3 @ 0.5 inference_from_work (P35); support single → corroborated (S1+S2+S5; P48); alt 4 named. A_locus / primary_system stay UNKNOWN (no own-voice or scholarly reconstruction on God). Childhood/heritage TODOs → UNKNOWN after search (P19). P47 source_quality on all sources. Chart-moving NO (A UNKNOWN; B faded @ 0.5). No fallacy_catalog; figures/ untouched. Draft, not reviewed."}
    - {date: 2026-10-08, by: "Grok Bot", summary: "Lens audit of batch C (dd91009), ruling R1, logged as P35 (v8's pick): B_cause 4 → 3 at 0.5, alternative 4, because B rests on working science only. No other value changes; mid_basin unchanged."}

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
  full_name: {value: "Willard Frank Libby", certainty: 1.0, cites: [{source: S1, locator: "heading"}, {source: S2, locator: "paragraph 1"}, {source: S6, locator: "lead"}], how_known: "Three sources (dual-bio Wikipedia P50)."}
  native_name: {value: "Willard Frank Libby (English)", certainty: 0.7, cites: [{source: S2, locator: "paragraph 1"}], how_known: "English name."}
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
  first_lasting_contribution_year: {value: 1941, certainty: 0.7, cites: [{source: S1, locator: "tritium paragraph, first sentence ('While associated with the Manhattan Project (1941–45), Libby helped develop a method for separating uranium isotopes by gaseous diffusion')"}, {source: S3, locator: "p. 1"}], how_known: "Start year of the earliest listed contribution, the gaseous-diffusion barrier (1941–1945), under decisions P12 and P13; S3 says the barrier was used for enrichment 'for more than 30 years'. 0.7 because the start year is the Manhattan Project's span, not a dated result, and the lasting judgement rests on his widow's memorial. His 1930s Geiger-counter and radioisotope work is not a listed contribution (no source read calls it lasting), so it does not set the year. Was 1947 (the first radiocarbon date) until the batch 4 lens audit."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "tritium paragraph, first sentence; radiocarbon paragraphs"}], how_known: "From first_lasting_contribution_year 1941 (P2); the radiocarbon work (1947) is in the same bucket."}
  region_of_birth: {value: "North America", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "USA is North America in data/reference/regions.csv (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S2, locator: "paragraphs 2–4"}], how_known: "Berkeley, Columbia, Chicago, Washington, UCLA."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "As the sources record it."}
  languages_of_work: {value: [English], certainty: 0.7, cites: [{source: S3, locator: "selected bibliography"}], how_known: "Papers and books in English."}
  occupations: {value: ["physical chemist", "university professor", "Atomic Energy Commissioner"], certainty: 1.0, cites: [{source: S2, locator: "paragraphs 2–5"}, {source: S1, locator: "paragraph 3"}], how_known: "Two sources."}

contribution:
  primary_domain: chemistry
  fields: {value: ["radiochemistry", "geochemistry", "nuclear chemistry"], certainty: 1.0, cites: [{source: S2, locator: "paragraph 6"}, {source: S1, locator: "opening"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Radiocarbon (carbon-14) dating", year: "1947", kind: method, lasting: "Nobel Prize in Chemistry 1960; more than 140 radiocarbon laboratories", certainty: 1.0, cites: [{source: S1, locator: "radiocarbon paragraphs"}, {source: S3, locator: "p. 1–2"}], how_known: "Two sources; first age determination 4 March 1947 (S1)."}
    - {value: "Natural tritium from cosmic rays and its use for dating water and wine and tracing water circulation", year: "1946", kind: discovery, lasting: "hydrology and geophysics tracer", certainty: 1.0, cites: [{source: S1, locator: "tritium paragraph"}, {source: S2, locator: "paragraph 6"}], how_known: "Two sources."}
    - {value: "Gaseous-diffusion barrier for separating uranium-235 (Manhattan Project, Columbia)", year: "1941–1945", kind: invention, lasting: "used in uranium enrichment for decades (S3)", certainty: 0.7, cites: [{source: S1, locator: "tritium paragraph, first sentence"}, {source: S3, locator: "p. 1"}], how_known: "Two sources; S3 is his widow's memorial."}
  evidence_of_impact:
    - {value: "Nominator: 'Seldom has a single discovery in chemistry had such an impact on the thinking in so many fields of human endeavour'", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S1, locator: "end of radiocarbon section"}], how_known: "Britannica quoting an unnamed nominator."}
  major_works:
    - {value: "Radiocarbon Dating", year: 1952, kind: book, certainty: 0.7, cites: [{source: S2, locator: "paragraph 8"}], how_known: "Nobel biography (second edition 1955)."}
  honours:
    - {value: "Nobel Prize in Chemistry", year: 1960, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "paragraph 7"}], how_known: "Two sources."}
    - {value: "Willard Gibbs Medal (American Chemical Society)", year: 1958, certainty: 0.7, cites: [{source: S2, locator: "paragraph 7"}], how_known: "Nobel biography."}
    - {value: "Albert Einstein Medal Award", year: 1959, certainty: 0.7, cites: [{source: S2, locator: "paragraph 7"}], how_known: "Nobel biography."}
  definition_fit: {value: "clearly meets", rationale: "Invented radiocarbon dating.", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated in Britannica, Nobel biography, GSA memorial, Nobel lecture, Wikipedia, or NNDB (P19)."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated in the sources read (P19)."}
  parents_and_household:
    - {value: "Father, Ora Edward Libby, a farmer", name: "Ora Edward Libby", role: father, certainty: 1.0, cites: [{source: S1, locator: "paragraph 2"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources."}
    - {value: "Mother, Eva May Rivers", name: "Eva May Libby (née Rivers)", role: mother, certainty: 1.0, cites: [{source: S1, locator: "paragraph 2"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources."}
  household_circumstances: {value: "Farming family", certainty: 0.7, cites: [{source: S1, locator: "paragraph 2"}], how_known: "Britannica."}
  schooling:
    - {value: "Grammar and high schools near Sebastopol, California", stage: "grammar or secondary school", years: "1913–1926", certainty: 0.7, cites: [{source: S2, locator: "paragraph 2"}], how_known: "Nobel biography."}
    - {value: "University of California, Berkeley: BSc 1931, PhD 1933", stage: university, years: "1927–1933", certainty: 1.0, cites: [{source: S2, locator: "paragraph 2"}, {source: S1, locator: "paragraph 2"}], how_known: "Two sources."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated in the sources read (P19)."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated in the sources read (P19)."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [English], certainty: 0.7, cites: [{source: S2, locator: "paragraphs 1–2"}], how_known: "American farm family."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1941–1947", certainty: 0.7, cites: [{source: S1, locator: "tritium and radiocarbon paragraphs"}, {source: S2, locator: "paragraphs 6, 8"}], how_known: "Equal to timing.major_work_period (P30 addendum f; span check 2026-10-02). Was 1931–1980: Berkeley to death."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No statement by him pairing science with religion was found. Nobel lecture (S5) is scientific method only; widow's memorial says he 'believed that education is our only hope and that science is basic to human success' (S3) — her summary, silent on God."}
  primary_system:
    value: UNKNOWN
    cites: [{source: S1, locator: "fallout-shelter paragraph"}, {source: S3, locator: "p. 3"}, {source: S5, locator: "full lecture"}, {source: S7, locator: "Religion: Agnostic"}]
    how_known: "Researched: Britannica, Nobel biography, GSA memorial, Nobel lecture (own words), Wikipedia dual-bio, NNDB. No writing or reported speech of his on religion was read. NNDB lists 'Religion: Agnostic' without citation (S7) — tertiary label only, not a scholarly reconstruction (contrast Segrè DSB on Fermi); not enough for AGNOS. Britannica's only God mention is Szilard's joke about the burned fallout shelter (Szilard's line). Widow's education/science hope line (S3) says nothing on God."
    note: "Would need UCLA Special Collections papers, AIP/UCLA oral-history transcripts (paywalled / not opened this pass), or a quotable scholarly biography for AGNOS or any other code."
  secondary_system: {value: UNKNOWN, how_known: "No second system (P29)."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Rejected this pass: NNDB 'Agnostic' (S7) is an unsupported tertiary label; no own words and no scholarly reconstruction (Segrè-grade) found. Keep as lead if a better source appears."}
    - {code: ATHE, reason: "Rejected: no denial of God read; NNDB does not say atheist."}
    - {code: DEISM, reason: "Rejected: no creator-by-reason profession read."}
    - {code: SECHUM, reason: "Rejected: widow's 'education is our only hope' (S3) is her summary, not his Humanist affiliation or statement."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "No statement placing or denying God was read (P19). NNDB agnostic label alone does not fix a locus (and is not used for coding)."}
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      support: corroborated
      cites: [{source: S1, locator: "radiocarbon paragraphs"}, {source: S2, locator: "paragraph 6"}, {source: S5, locator: "Radiocarbon Dating lecture (law of radioactive decay; cosmic-ray constancy)"}]
      how_known: "Coder's reading of his working science, as P6/P24/P30 direct for a scientist. No statement of his own about miracles or exceptions, so 0.5. Three independent source ids describing the same radiocarbon program (Britannica + Nobel biography + Nobel lecture own words) → corroborated (P48). Named alternative 4, so 0.5 (P35)."
      rationale: "Scored on his account of nature (P6). Radiocarbon dating rests on carbon-14 decaying at a constant rate after death, production that varied little with latitude, and a steady-state reservoir checked against tree rings and dated artefacts (S1; S2). Own Nobel lecture: 'according to the law of radioactive decay'; 'encouraging evidence that the cosmic rays have indeed remained constant in intensity over many thousands of years' and that ocean mixing/composition 'have not changed either' (S5). Uniform physical law with no special cases in the working science. P35: B inferred only from a scientist's working science, with no statement of their own on law and exception (miracle / no-exception claim), is B 3 at 0.5 with 4 as the named alternative, never 4 — Nobel lecture is primary science text but not a no-exception claim (same treatment as Fermi D1). Named alternative: 4, if a statement of his own shows no exception."
      alternatives:
        - {value: 4, note: "P35: if an own statement shows exceptionless natural order (not just working-science constancy assumptions).", cites: [{source: S5, locator: "law of radioactive decay paragraph"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing on judgement, afterlife or reward in the sources read (P19)."}
    D_authority: {value: UNKNOWN, how_known: "No statement on revelation in the sources read (P19)."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Nothing read addresses favour for a group in events. Working science bears on the first question (same laws everywhere) but not on favour for a group in events, so E stays BELOW_THRESHOLD; not scored from working science alone (P19)."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so mid_basin is UNKNOWN (§6 precedence, decision P19). B at 0.5 also fails the P4 ≥0.7 bar."}
  statements:
    - text: "At the time of death, however, the assimilation process stops abruptly. There is no longer any process by which the carbon-14 from the atmosphere can enter our bodies. Therefore, at the time of death the radioactive disintegration process takes over in an uncompensated manner and, according to the law of radioactive decay, after 5,600 years the carbon that is in our bodies while we are alive will show half the specific carbon-14 radioactivity that it shows now."
      cites: [{source: S5, locator: "Radiocarbon Dating lecture, living/dead equilibrium paragraphs"}]
      date: "1960-12-12"
      context: "Nobel Lecture; after the listed span under P31 (no documented change of scientific view; method from 1947)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Working-science statement of radioactive decay law; not a no-exception / miracle claim, so does not lift B off P35."
    - text: "Being so unrelated, we believe this to be very unlikely and conclude that the agreement between the predicted and observed assays is encouraging evidence that the cosmic rays have indeed remained constant in intensity over many thousands of years and that the mixing time, volume, and composition of the oceans have not changed either."
      cites: [{source: S5, locator: "Radiocarbon Dating lecture, reservoir-constancy paragraph"}]
      date: "1960-12-12"
      context: "Nobel Lecture; empirical constancy of cosmic-ray intensity and ocean reservoir."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Constancy assumption for dating; still not an explicit no-exception claim about nature (P35)."
  changes_over_life: []
  coder_notes: "D1: B corroborated via Nobel lecture own words but stays 3 @ 0.5 under P35 (Fermi/Dirac pattern). A and primary UNKNOWN — NNDB Agnostic unused. AIP oral history (Marlowe 1979) and UCLA Terrall oral history abstracts checked; full transcripts not opened. Emerson Unitarian Church 1967 Pacifica talk is venue-only. Collected Papers vols. 6–7 (Papers for the Public / Talking to People) unread. UCLA Special Collections papers unread. Chart-moving NO."


heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "American (Colorado and California farming family)", certainty: 0.7, cites: [{source: S1, locator: "paragraph 2"}, {source: S2, locator: "paragraphs 1–2"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated in the sources read; NNDB religion field is adult label only and unused for coding (P19, P50)."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated in the sources read (P19). Encyclopedia.com DSB-style article notes he was cremated — burial practice, not initiation."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated in the sources read (P19)."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1941–1947", certainty: 0.7, cites: [{source: S1, locator: "tritium and radiocarbon paragraphs"}, {source: S2, locator: "paragraphs 6, 8"}], how_known: "From the gaseous-diffusion barrier (1941–1945; classified work, dated by its work years, P30 #2) to radiocarbon dating (1947), the first and last listed lasting contributions (P29). Span check 2026-10-02 (P29, P30 and its addendum): was 1946–1952. The 1952 book Radiocarbon Dating sets out the 1947 method and is not a separate listed contribution."}
  age_at_first_lasting_contribution: {value: 33, certainty: 0.7, cites: [{source: S1, locator: "opening; tritium paragraph, first sentence"}], how_known: "Born 17 December 1908; the Manhattan Project work began in 1941, so 32 (33 only from 17 December 1941). Was 38 (from March 1947) until the batch 4 lens audit. P30 (rule 5): 1941 − 1908 = 33, with no month adjustment; was 32 until the P30 age sweep (2026-10-02)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No LIO-type view (P27): B rests on working-science inference, which is not an LIO-type view; no scored statement at 3/4 on any axis."}
  lio_views_relative_to_major_work: {value: "unclear", rationale: "No LIO-type view found to date against the span.", certainty: 0.5, cites: [{source: S3, locator: "p. 3"}, {source: S5, locator: "full lecture"}], how_known: "Working-science B is not an LIO-type view (P27)."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "primary_system UNKNOWN; only B 3 @ 0.5 from working science during/after the span (P31 for the 1960 lecture)."}

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
  - {value: "Harold Urey", roster_id: urey-harold, relation: collaborator, note: "Columbia war research, 1941–45", certainty: 0.7, cites: [{source: S1, locator: "paragraph 3"}], how_known: "Britannica."}
  - {value: "Edward Teller", roster_id: teller-edward, relation: collaborator, note: "fellow advocate of nuclear testing in the late 1950s", certainty: 0.7, cites: [{source: S1, locator: "fallout-shelter paragraph"}], how_known: "Britannica."}
  - {value: "Linus Pauling", roster_id: pauling-linus, relation: "rival or critic", note: "opposed Pauling's petition for a nuclear test ban", certainty: 0.7, cites: [{source: S1, locator: "fallout-shelter paragraph"}], how_known: "Britannica."}
  - {value: "Leona Woods Marshall", relation: family, note: "second wife (married 1966); author of S3", certainty: 1.0, cites: [{source: S1, locator: "paragraph 2"}, {source: S3, locator: "byline"}], how_known: "Two sources."}

review:
  roster_status_reason: {value: "Core in v8 (F 3: DeepSeek, Gemini, Grok). Included in the fourth batch by owner decision, borderline on the stage-2 date window (1600–1950).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 224"}], how_known: "Study roster; batch inclusion by Jason, 2026-10-02."}
  controversies:
    - {value: "Advocate of nuclear weapons testing; publicized fallout shelter at his house", certainty: 0.7, cites: [{source: S1, locator: "fallout-shelter paragraph"}], how_known: "Britannica."}
  data_quality_flags:
    - "Borderline on the stage-2 date window: radiocarbon dating 1947–49; included by owner decision (2026-10-02)."
    - "Deepen D1: still no usable religion source; NNDB Agnostic rejected; B corroborated but P35-capped at 0.5."
    - "Chicago and AEC years differ between S1 and S2."
  open_questions:
    - "UCLA Special Collections (Collection 1276) and AIP Marlowe / UCLA Terrall oral-history full transcripts for a religion statement."
    - "Collected Papers vols. 6–7 (Papers for the Public; Talking to People) unread."
    - "If a Segrè-grade scholarly reconstruction of agnosticism appears, revisit AGNOS @ 0.5 / A BELOW_THRESHOLD (P20)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "George B. Kauffman"
    citation: "Kauffman, George B. \"Willard Frank Libby.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Willard-Libby."
    url: "https://www.britannica.com/biography/Willard-Libby"
    accessed: 2026-10-02
    source_quality: "reference entry"
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
    source_quality: "reference entry"
    reliability_note: "Official biography; paragraphs counted from 'Willard Frank Libby was born'."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions]
  - id: S3
    type: secondary
    kind: "journal article"
    author: "Leona Marshall Libby"
    citation: "Libby, Leona Marshall. \"Memorial to Willard Frank Libby, 1908–1980.\" Geological Society of America Memorials, vol. 14. https://rock.geosociety.org/net/documents/gsa/memorials/v14/Libby-WF.pdf."
    url: "https://rock.geosociety.org/net/documents/gsa/memorials/v14/Libby-WF.pdf"
    accessed: 2026-10-02
    source_quality: "other"
    reliability_note: "Memorial by his widow; GSA's own PDF. Pages counted in the memorial (1–3) before the bibliography. Belief summaries are hers."
    used_for: [basics, contribution, worldview, timing, lane_b, collaborators]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    source_quality: "study roster"
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Willard F. Libby"
    year: 1960
    citation: 'Libby, Willard F. "Radiocarbon Dating." Nobel Lecture, 12 December 1960. In Nobel Lectures, Chemistry 1942–1962. Amsterdam: Elsevier, 1964. NobelPrize.org PDF. https://www.nobelprize.org/uploads/2018/06/libby-lecture.pdf'
    url: "https://www.nobelprize.org/uploads/2018/06/libby-lecture.pdf"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Own Nobel lecture; PDF from NobelPrize.org read in full. Working-science statements on radioactive decay and cosmic-ray constancy."
    used_for: [worldview, timing]
  - id: S6
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: 'Wikipedia. "Willard Libby." English Wikipedia. Dual-biography use only (P50).'
    url: "https://en.wikipedia.org/wiki/Willard_Libby"
    accessed: 2026-10-24
    source_quality: "other"
    reliability_note: "P50 dual-bio only; no religion section; not used for worldview scores."
    used_for: [identity, basics]
  - id: S7
    type: tertiary
    kind: other
    author: "NNDB (Soylent Communications)"
    citation: 'NNDB. "Willard F. Libby." Lists Religion: Agnostic. https://www.nndb.com/people/470/000100170/'
    url: "https://www.nndb.com/people/470/000100170/"
    accessed: 2026-10-24
    source_quality: "other"
    reliability_note: "Unsupported tertiary religion label with no citation; checked and rejected for coding (not Segrè-grade scholarly reconstruction). Logged only to document the AGNOS lead that was considered."
    used_for: [worldview]
---

# Willard Libby

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Willard Libby (1908–1980), American chemist, invented radiocarbon dating (first date March 1947) and won the 1960 Nobel Prize in Chemistry [S1; S2]. Deepen D1: primary_system UNKNOWN; A UNKNOWN; B 3 at 0.5 inference_from_work, support corroborated (S1+S2+S5; alternative 4, P35); C and D UNKNOWN; E below threshold; mid_basin UNKNOWN. Still unplotted (A UNKNOWN; B faded). Included in this batch by owner decision, borderline on the stage-2 date window.

## Life and work

Berkeley (BSc 1931, PhD 1933, faculty to 1945), Manhattan Project at Columbia, Chicago, the Atomic Energy Commission (1954–59), UCLA [S1; S2].

## Contribution and impact

Radiocarbon dating, natural tritium, the uranium diffusion barrier [S1; S3].

## Childhood and education

Son of a farmer; schools near Sebastopol, California [S1; S2].

## Adult working worldview

No usable religion statement found. NNDB's unsupported "Agnostic" label was considered and rejected for coding [S7]. Nobel lecture states the law of radioactive decay and cosmic-ray constancy for the radiocarbon method [S5] — corroborates working-science B under P35 but does not lift it to 0.7. primary_system UNKNOWN; A UNKNOWN; B 3 @ 0.5 corroborated.

## Heritage (context only)

American farming family [S1; S2]. Context only.

## Timing

First lasting contribution 1941, the start of the gaseous-diffusion work for the Manhattan Project, at 33 [S1; S3]. Radiocarbon dating followed in 1947 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form partly present; circle unclear.

## Open questions

- UCLA Special Collections papers; AIP / UCLA oral-history full transcripts; Collected Papers vols. 6–7.

## Research log

- 2026-10-24: Deepen D1. Nobel lecture PDF (S5); Wikipedia dual-bio (S6); NNDB Agnostic checked/rejected (S7); encyclopedia.com DSB-style Kauffman (cremated; no religion); AIP oral-history pages not opened (blocked/tiny response); Emerson Unitarian 1967 talk venue-only. B corroborated; A/primary UNKNOWN.
- 2026-10-02: Read Britannica (Kauffman), the Nobel biography and the GSA memorial (Leona Marshall Libby). Nothing on religion.
