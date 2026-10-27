---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 8
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, second batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 20c_early. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (second batch, RUNBOOK §1 order). Basics, contribution and childhood from Britannica (Badash), MacTutor and the Nobel biography. No writing by Fermi on religion was found; Laura Fermi's Atoms in the Family (p. 52, the usual source for 'agnostic') is lending-only on archive.org and was not read. primary_system BELOW_THRESHOLD (AGNOS candidate, stub). B_cause 4 at 0.5 from his working science (P6); A, C, D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 2 (finding #32): region_of_work locator now paragraphs 2–5, since Florence is in Nobel paragraph 2. Value and certainty unchanged. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Schema 1.1 → 1.2 (decision P8 adds basis recorded_interview and statement kind 'recorded interview'); no content change."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02). Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs; BELOW_THRESHOLD vs UNKNOWN per P19; kind lists (P21: research institute, school stage and run_by, scholarly edition); basis inference_from_work for 0.5 inference from working science (P24). Full before → after list: reports/stage3_rulings_changes.csv. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "P30 rule 5 age sweep: ages recomputed as event year − birth year, with no month adjustment (scripts/recompute_ages.py; every change is in reports/p30_age_changes.csv). No other value changed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Span alignment (P29, P30 and its addendum): timing.major_work_period checked, 1926–1942 unchanged; worldview.working_years 1921–1954 → 1926–1942, equal to the span (P30 addendum f); evidence for every headline value checked against the span; no value or certainty changed. Listed in reports/p30_span_alignment.csv. Not reviewed."}
    - {date: 2026-10-08, by: "Grok Bot", summary: "Lens audit of batch C (dd91009), ruling R1, logged as P35 (v8's pick): B_cause 4 → 3 at 0.5, alternative 4, because B rests on working science only. No other value changes; mid_basin unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #23, F5 rank 23). P47 source_quality on every source. New: S5 Nobel Lecture 1938 (primary / own words; neutron-induced radioactivity); S6 Emilio Segrè DSB / encyclopedia.com PDF via MacTutor ('Fermi was fundamentally an agnostic, although he had been baptized a Catholic'). primary_system UNKNOWN → AGNOS @ 0.5 scholarly_reconstruction (Segrè; AGNOS stub flagged); A_locus UNKNOWN → BELOW_THRESHOLD (P20: agnostic with no stated locus). B_cause stays 3 @ 0.5 inference_from_work; support labelled corroborated (S5+S3+S2; P48); alt 4 named (P35). Baptism filled from Segrè. Laura Fermi Atoms in the Family p. 52 still unread (lending-only; Wikipedia cites it for adult agnostic). Chart: still unplotted (A BELOW; B faded @ 0.5). No fallacy_catalog (Jason 2026-10-23). Draft, not reviewed."}

identity:
  id: fermi-enrico
  display_name: "Enrico Fermi"
  roster:
    canonical_name: "Enrico Fermi"
    rank: 23
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: physics
    field_bucket: physics
  full_name: {value: "Enrico Fermi", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S2, locator: "heading"}], how_known: "Sources agree."}
  native_name: {value: "Enrico Fermi (Italian)", certainty: 0.7, cites: [{source: S1, locator: "opening paragraph"}], how_known: "Same spelling in Italian."}
  aliases:
    - {name: "Enrico-Fermi", kind: "roster alias"}
    - {name: "Fermi-Enrico", kind: "roster alias"}

basics:
  birth:
    date: {value: "1901-09-29", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S3, locator: "first paragraph"}], how_known: "Two sources agree."}
    place: {value: "Rome", modern_name: "Rome, Italy", polity_then: "Kingdom of Italy", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S3, locator: "first paragraph"}], how_known: "Two sources agree."}
  death:
    date: {value: "1954-11-28", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "Quick Info"}], how_known: "Two sources agree."}
    place: {value: "Chicago, Illinois", modern_name: "Chicago, Illinois, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Britannica; MacTutor gives burial in Oak Woods Cemetery, Chicago (S2)."}
  first_lasting_contribution_year: {value: 1926, certainty: 1.0, cites: [{source: S3, locator: "paragraph 3"}, {source: S1, locator: "Fermi-Dirac statistics"}], how_known: "Fermi statistics (Fermi–Dirac statistics), 1926; two sources."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S3, locator: "paragraph 3"}], how_known: "From first_lasting_contribution_year (P2)."}
  region_of_birth: {value: "Southern Europe", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Italy is Southern Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S3, locator: "paragraphs 2–5 (Florence in paragraph 2)"}], how_known: "Fermi statistics, beta-decay theory and slow neutrons (1926–1934) were done in Florence and Rome. The first controlled chain reaction (1942) was in Chicago. Two regions, so 0.7.", alternatives: [{value: "North America", cites: [{source: S3, locator: "paragraphs 6–8"}], note: "Columbia 1939–1942; Chicago 1942–1954."}]}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S3, locator: "first paragraph ('the son of')"}], how_known: "As the sources record it."}
  languages_of_work: {value: [Italian, English], certainty: 0.7, cites: [{source: S2, locator: "Biography (Italian titles of 1921–1935 papers; English papers in Proc. Roy. Soc.)"}], how_known: "MacTutor lists papers in both languages."}
  occupations: {value: [physicist, "university professor"], certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S3, locator: "paragraphs 4–8"}], how_known: "Sources agree."}

contribution:
  era_bucket: 20c_early
  fields: {value: ["theoretical physics", "nuclear physics", "statistical mechanics", "particle physics"], certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S3, locator: "paragraphs 3–8"}], how_known: "Sources agree."}
  lasting_original_contributions:
    - {value: "Fermi(–Dirac) statistics for particles obeying the exclusion principle (fermions)", year: "1926", kind: theory, lasting: "Britannica: 'a contribution of exceptional importance to atomic and nuclear physics'", certainty: 1.0, cites: [{source: S1, locator: "Fermi-Dirac statistics"}, {source: S3, locator: "paragraph 3"}], how_known: "Two sources; developed independently by Dirac (S1)."}
    - {value: "Theory of beta decay", year: "1934", kind: theory, lasting: "standard nuclear physics", certainty: 0.7, cites: [{source: S3, locator: "paragraph 5"}], how_known: "Nobel biography."}
    - {value: "Neutron-induced radioactivity and slow neutrons", year: "1934", kind: discovery, lasting: "Nobel Prize 1938; led to the discovery of fission (S3)", certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S3, locator: "paragraph 5"}], how_known: "Two sources."}
    - {value: "First controlled nuclear chain reaction (Chicago Pile-1)", year: "1942", kind: invention, lasting: "the first nuclear reactor (S1)", certainty: 1.0, cites: [{source: S1, locator: "opening summary"}, {source: S2, locator: "Biography"}, {source: S3, locator: "paragraph 7"}], how_known: "Three sources."}
  evidence_of_impact:
    - {value: "Nobel Prize for Physics 1938", kind: "honours in lifetime", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}
    - {value: "Particles named fermions after him", kind: "named after them", certainty: 1.0, cites: [{source: S1, locator: "Fermi-Dirac statistics"}, {source: S3, locator: "paragraph 3"}], how_known: "Two sources."}
  major_works: []
  honours:
    - {value: "Nobel Prize for Physics", year: 1938, certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor quotes the citation."}
  definition_fit: {value: "clearly meets", rationale: "Several lasting original contributions in theory and experiment.", certainty: 0.7, cites: [{source: S1, locator: "opening paragraph"}], how_known: "Sources agree."}

childhood:
  family_religion: {value: "Nominally Catholic family background, but his own household was not religious; his father's relatives were devout Catholics", certainty: 1.0, cites: [{source: S2, locator: "Biography ('the family were not religious')"}, {source: S6, locator: "opening paragraph (baptized Catholic; fundamentally an agnostic)"}], how_known: "MacTutor and Segrè DSB agree on non-religious household / Catholic baptism as heritage only."}
  family_religious_practice: {value: "Not religious; his elementary school was chosen because it was secular", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}
  parents_and_household:
    - {value: "Father, Alberto Fermi, a railway official (chief inspector)", name: "Alberto Fermi", role: father, certainty: 1.0, cites: [{source: S1, locator: "early life"}, {source: S2, locator: "Biography"}, {source: S3, locator: "first paragraph"}], how_known: "Three sources (S3 says Ministry of Communications)."}
    - {value: "Mother, Ida de Gattis, an elementary schoolteacher", name: "Ida de Gattis", role: mother, certainty: 1.0, cites: [{source: S1, locator: "early life"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}
  household_circumstances: {value: "Civil-service family in Rome; brother Giulio died in 1915, when Enrico was 14", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}
  schooling:
    - {value: "Secular elementary school, from age six", stage: "elementary school", ages: "6–10", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}
    - {value: "Ginnasio (five years) and liceo (three years), Rome", stage: "grammar or secondary school", certainty: 0.7, cites: [{source: S2, locator: "Biography"}, {source: S3, locator: "first paragraph"}], how_known: "Two sources."}
    - {value: "Scuola Normale Superiore and University of Pisa; doctorate 1922", stage: university, years: "1918–1922", certainty: 1.0, cites: [{source: S1, locator: "early life"}, {source: S2, locator: "Biography"}, {source: S3, locator: "first paragraph"}], how_known: "Three sources."}
  early_mathematics: {value: "advanced mathematics", note: "Puzzling out the equation of a circle by about age ten; his 1918 entrance essay used partial differential equations and Fourier analysis", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Built electric motors and mechanical toys with his brother and sister; mathematics and physics encouraged by his father's colleague A. Amidei", certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S3, locator: "first paragraph"}], how_known: "Two sources."}
  key_early_reading: []
  childhood_mentors:
    - {value: "A. Amidei, a colleague of his father", certainty: 0.7, cites: [{source: S3, locator: "first paragraph"}], how_known: "Nobel biography."}
  languages_in_childhood: {value: [Italian], certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "Born and schooled in Rome."}
  notable_events:
    - {value: "Death of his brother Giulio", year: 1915, age: 14, certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1926–1942", certainty: 0.7, cites: [{source: S3, locator: "paragraphs 3–7"}], how_known: "Equal to timing.major_work_period (P30 addendum f; span check 2026-10-02). Was 1921–1954: First paper 1921 to death."}
  nominal_affiliations:
    - {value: "No church membership reported for his adult life in the sources read; his two children were Roman Catholics", role: other, certainty: 0.7, cites: [{source: S2, locator: "Biography (1938)"}], how_known: "MacTutor (one source)."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No statement by Fermi on science and religion in S1–S6."}
  primary_system:
    value: AGNOS
    basis: scholarly_reconstruction
    certainty: 0.5
    cites: [{source: S6, locator: "opening paragraph ('Fermi was fundamentally an agnostic, although he had been baptized a Catholic')"}]
    how_known: "Emilio Segrè's Dictionary of Scientific Biography article (close collaborator; later author of Enrico Fermi, Physicist, 1970) states he was fundamentally an agnostic. No first-person suspension statement by Fermi was read. Laura Fermi, Atoms in the Family (1954), p. 52 — the usual spouse-memoir locus for the adult-agnostic claim — remains unread (lending-only). AGNOS stub system file flagged. Named alternative: BELOW_THRESHOLD / UNKNOWN if v8 wants own-words only for an AGNOS code."
    rationale: "AGNOS = explicit suspension of judgement about God (CODING_GUIDE; systems/AGNOS.md). Segrè's scholarly label supplies the suspension stance at the P49 0.5 ceiling; baptism is heritage only (never a code)."
    note: "AGNOS is a stub system file (flag). Reading Laura Fermi p. 52 or Segrè 1970 full text could corroborate or quote own words; until then certainty stays 0.5."
  secondary_system: {value: UNKNOWN, how_known: "No second-system evidence in S1–S6."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Coded at 0.5 scholarly_reconstruction from Segrè DSB (S6). AGNOS stub flagged. Laura Fermi p. 52 unread.", cites: [{source: S6, locator: "opening paragraph"}]}
    - {code: CHRIST, reason: "Rejected: baptized Catholic (S6) and Catholic family background (S2) are heritage/membership; non-religious household and no adult practice (S2). Heritage is never a code.", cites: [{source: S2, locator: "Biography"}, {source: S6, locator: "opening paragraph"}]}
    - {code: ATHE, reason: "Rejected: Segrè labels him agnostic, not atheist; no positive-naturalism statement read. ATHE is also a stub system file (flag).", cites: [{source: S6, locator: "opening paragraph"}]}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "P20: an agnostic with no stated locus view is A BELOW_THRESHOLD. Segrè supplies the AGNOS label (S6) but no statement of Fermi's own placing or denying God was read. systems/AGNOS.md also sets A BELOW_THRESHOLD for explicit suspension. Named alternative: UNKNOWN if v8 withholds the AGNOS code pending Laura Fermi / own words.", note: "Gap: Laura Fermi 1954 p. 52 (lending-only); Segrè 1970 book (unread this pass; DSB used)."}
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      support: corroborated
      cites: [{source: S5, locator: "whole (neutron bombardment; artificial radioactivity as lawful nuclear processes)"}, {source: S3, locator: "paragraphs 3–7"}, {source: S2, locator: "Biography"}]
      how_known: "Coder's reading of his working science, as P6/P24/P30 direct for a scientist. No statement of his own about miracles or exceptions, so 0.5. Three independent source ids describing the same experimental/theoretical program (Nobel lecture own words + Nobel biography + MacTutor) → corroborated (P48). Named alternative 4, so 0.5 (P35)."
      rationale: "Scored on his account of nature (P6), which for a scientist is the working science. Statistical laws for fermions, beta decay, neutron-induced radioactivity and the chain reaction all treat nature as governed by law with no special cases. His 1938 Nobel lecture describes artificial radioactivity and neutron bombardment as repeatable nuclear processes without miracle, petition or exemption (S5). P35 (v8's pick, 2026-10-08): B inferred only from a scientist's working science, with no statement of their own on law and exception, is B 3 at 0.5 with 4 as the named alternative, never 4. Named alternative: 4, if a statement of their own shows no exception."
    C_ledger: {value: UNKNOWN, how_known: "Nothing on reward, punishment or afterlife in S1–S6."}
    D_authority: {value: UNKNOWN, how_known: "No statement on revelation in S1–S6.", note: "His practice is wholly empirical, but D asks about revelation versus observation, which needs a statement."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). His physics applies the same laws everywhere, but whether his account of events keeps any exception for a group is not addressed in any source read, so below 0.5.", note: "Not scored from the working science alone, unlike B, because P7 asks a second question (in-group exceptions) that needs a statement."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD and B_cause is only 0.5, under the P4 test's 0.7 bar (§6)."}
  statements: []
  changes_over_life: []
  coder_notes: "Deepen D1: primary_system AGNOS @ 0.5 from Segrè DSB scholarly reconstruction (S6); A BELOW_THRESHOLD (P20). No first-person religion quotation by Fermi found; statements empty. Laura Fermi Atoms in the Family p. 52 still unread (lending-only on IA; Wikipedia cites it for adult agnostic + grandparents' baptism wish) — logged as blocker, not scored as own words. Lutheran graveside (Hucke & Bielski via Wikipedia) is burial rite, not belief. B stays 3 @ 0.5 inference_from_work with support corroborated (P48); Nobel lecture (S5) is primary science text but not a no-exception claim, so not written_profession. Online anecdotes (stars remark) unused."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Italian", certainty: 0.7, cites: [{source: S1, locator: "opening paragraph"}], how_known: "Sources agree."}
  religious_heritage_by_birth: {value: "Catholic family background (his father's relatives devout Catholics)", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}
  baptism_or_initiation: {value: "Baptized Catholic", certainty: 0.7, cites: [{source: S6, locator: "opening paragraph"}], how_known: "Segrè DSB. Wikipedia's further detail (grandparents' wishes; Laura Fermi p. 52) not verified in a page read this pass.", note: "Heritage/initiation only — never a worldview code."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not mentioned in S1–S3; his elementary school was secular (S2)."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1926–1942", certainty: 0.7, cites: [{source: S3, locator: "paragraphs 3–7"}], how_known: "From Fermi statistics to the chain reaction."}
  age_at_first_lasting_contribution: {value: 25, certainty: 0.7, cites: [{source: S3, locator: "paragraph 3"}], how_known: "Born September 1901; the 1926 statistics paper. 24 or 25 depending on the month of the paper, which S3 does not give. P30 (rule 5): 1926 − 1901 = 25, with no month adjustment; was 24 until the P30 age sweep (2026-10-02)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No LIO-type view (P27) of his own was read; AGNOS/A BELOW rest on Segrè's reconstruction, not an LIO-type statement by Fermi."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "Nothing of his on God or nature at the P27 bar; B is inference_from_work only; AGNOS is scholarly reconstruction.", certainty: 0.5, cites: [{source: S6, locator: "opening paragraph"}, {source: S5, locator: "whole"}], how_known: "Absence at the P27 bar in sources read."}
  worldview_during_major_work: {value: "AGNOS (scholarly reconstruction, Segrè); A BELOW_THRESHOLD; B 3 @ 0.5 from working science", certainty: 0.5, cites: [{source: S6, locator: "opening paragraph"}, {source: S5, locator: "whole"}], how_known: "Synthesis of D1 sources; not a stronger code."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "A friend recalled that for him 'to know a theorem or law meant chiefly to know how to use it' (S2): a practical rather than axiomatic style.", certainty: 0.5, cites: [{source: S2, locator: "Biography (Persico)"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "Biography"}], how_known: "Coder's reading."}
  circle_present: {value: "no", rationale: "No God-Nature identity in anything read.", certainty: 0.5, cites: [{source: S2, locator: "Biography"}], how_known: "Absence in the sources read."}
  reading: "As belief, not finding: form unclear (practical style), circle absent. The record does not test H1."
  notes: ""

institutions:
  - {value: "University of Rome", role: "professor of theoretical physics", years: "1927–1938", kind: university, certainty: 1.0, cites: [{source: S3, locator: "paragraph 4"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}
  - {value: "Columbia University", role: "professor of physics", years: "1939–1942", kind: university, certainty: 1.0, cites: [{source: S1, locator: "opening summary"}, {source: S3, locator: "paragraph 6"}], how_known: "Two sources."}
  - {value: "University of Chicago (Manhattan Project; Institute for Nuclear Studies)", role: "group leader; professor", years: "1942–1954", kind: university, certainty: 1.0, cites: [{source: S1, locator: "opening summary"}, {source: S3, locator: "paragraphs 7–8"}], how_known: "Two sources."}
collaborators:
  - {value: "Max Born", relation: teacher, note: "Göttingen, 1923", certainty: 1.0, cites: [{source: S1, locator: "early life"}, {source: S3, locator: "paragraph 2"}], how_known: "Two sources."}
  - {value: "Paul Ehrenfest", relation: teacher, note: "Leiden, 1924", certainty: 1.0, cites: [{source: S1, locator: "early life"}, {source: S3, locator: "paragraph 2"}], how_known: "Two sources."}
  - {value: "Paul Dirac", roster_id: dirac-paul, relation: other, note: "developed the same statistics independently", certainty: 0.7, cites: [{source: S1, locator: "Fermi-Dirac statistics"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v7.1 (F 4) and v8 (F 5, all five models).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 23"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Academy of 1929: MacTutor says Mussolini appointed him to the Accademia dei Lincei; Britannica says the new Accademia d'Italia. Britannica's version is probably right; not settled from the sources read."
    - "Chicago professorship: MacTutor says the offer came in 1945; the Nobel biography and Britannica say 1946."
    - "AGNOS @ 0.5 rests on Segrè DSB scholarly reconstruction only; Laura Fermi p. 52 unread; no Fermi own-words on religion."
    - "AGNOS is a stub system file (flag)."
  open_questions:
    - "Read Laura Fermi, Atoms in the Family (1954), p. 52 (spouse memoir; Wikipedia cites for adult agnostic and grandparents' baptism wish) — lending-only on archive.org this pass."
    - "Read Emilio Segrè, Enrico Fermi, Physicist (1970) full text for any further religion discussion beyond the DSB sentence used as S6."
    - "Own-words locus or no-exception claim (letters, AIP interviews, Collected Papers commentary) to lift A or B."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Lawrence Badash"
    citation: "Badash, Lawrence. \"Enrico Fermi.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Enrico-Fermi."
    url: "https://www.britannica.com/biography/Enrico-Fermi"
    accessed: 2026-10-02
    reliability_note: "Signed article by a historian of science."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, heritage, institutions, collaborators]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "J. J. O'Connor and E. F. Robertson"
    citation: "O'Connor, J. J. and E. F. Robertson. \"Enrico Fermi.\" MacTutor History of Mathematics Archive, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Fermi/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Fermi/"
    accessed: 2026-10-02
    reliability_note: "Standard biographical archive; quotes Persico, Segrè and Laura Fermi."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions]
  - id: S3
    type: tertiary
    kind: "institutional page"
    author: "Nobel Foundation"
    citation: "\"Enrico Fermi – Biographical.\" NobelPrize.org (from Nobel Lectures, Physics 1922–1941, Elsevier, 1965). https://www.nobelprize.org/prizes/physics/1938/fermi/biographical/."
    url: "https://www.nobelprize.org/prizes/physics/1938/fermi/biographical/"
    accessed: 2026-10-02
    reliability_note: "Official biography; paragraphs counted from the top of the text."
    source_quality: "reference entry"
    used_for: [basics, contribution, childhood, timing, institutions, collaborators, worldview]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Enrico Fermi"
    citation: "Fermi, Enrico. \"Artificial Radioactivity Produced by Neutron Bombardment.\" Nobel Lecture, 12 December 1938. NobelPrize.org (from Nobel Lectures, Physics 1922–1941, Elsevier, 1965). https://www.nobelprize.org/prizes/physics/1938/fermi/lecture/."
    url: "https://www.nobelprize.org/prizes/physics/1938/fermi/lecture/"
    accessed: 2026-10-24
    reliability_note: "Fermi's own Nobel lecture; PDF text extracted this pass (pdftotext). Describes neutron-induced artificial radioactivity as lawful nuclear processes; no religion language."
    source_quality: "primary / own words"
    used_for: [contribution, worldview]
  - id: S6
    type: secondary
    kind: "encyclopedia"
    author: "Emilio Segrè"
    citation: "Segrè, Emilio. \"Fermi, Enrico.\" Complete Dictionary of Scientific Biography. Charles Scribner's Sons, 2008 (orig. DSB). Encyclopedia.com reprint; PDF mirror at MacTutor: https://mathshistory.st-andrews.ac.uk/DSB/Fermi.pdf."
    url: "https://mathshistory.st-andrews.ac.uk/DSB/Fermi.pdf"
    accessed: 2026-10-24
    reliability_note: "Signed DSB article by Fermi's close collaborator and later biographer; opening paragraph states baptism and 'fundamentally an agnostic'. Worldview sentence is scholarly reconstruction (basis), not Fermi's own words."
    source_quality: "reference entry"
    used_for: [worldview, childhood, heritage]
---

# Enrico Fermi

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Enrico Fermi (1901–1954), Italian-born physicist, developed Fermi statistics (1926), the theory of beta decay and neutron-induced radioactivity (1934), and directed the first controlled chain reaction (1942) [S1, opening paragraph; S3, paragraphs 3–7; S5]. Nobel Prize 1938 [S2, Biography]. Deepen D1 (P47–P50): primary_system AGNOS at 0.5 (scholarly reconstruction, Segrè DSB) [S6]; A_locus BELOW_THRESHOLD (P20); B_cause 3 at 0.5, inference_from_work, support corroborated (S5+S3+S2; P35 alt 4); C and D UNKNOWN; E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Still unplotted (A BELOW; B faded).

## Life and work

Born in Rome, he studied at the Scuola Normale in Pisa, worked with Born and Ehrenfest, held the Rome chair of theoretical physics from 1927, and left Italy in 1938 for Columbia and then Chicago [S3, paragraphs 1–8; S2, Biography].

## Contribution and impact

Fermi statistics, beta-decay theory, slow neutrons and the first reactor [S3, paragraphs 3–7]. Britannica calls him "one of the chief architects of the nuclear age" [S1, opening paragraph].

## Childhood and education

His household was not religious, which upset his father's devout Catholic relatives, and his elementary school was chosen because it was secular [S2, Biography]. By about ten he was working out why x² + y² = r² is a circle [S2, Biography].

## Adult working worldview

Segrè's DSB article states that Fermi "was fundamentally an agnostic, although he had been baptized a Catholic" [S6, opening paragraph]. No first-person religion statement by Fermi was found; Laura Fermi's *Atoms in the Family* (1954), p. 52, remains unread. primary_system AGNOS at 0.5 (scholarly reconstruction; AGNOS stub flagged). A BELOW_THRESHOLD (P20); B 3 at 0.5 from the working science with support corroborated (S5+S3+S2; alternative 4, P35); C and D UNKNOWN; E below threshold; mid_basin BELOW_THRESHOLD.

## Heritage (context only)

Italian, Catholic family background [S2, Biography]. Context only.

## Timing

First lasting contribution 1926, at about 25 [S3, paragraph 3]. No worldview statement to time.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. A practical, use-oriented style of knowing laws is reported [S2, Biography]; no circle.

## Open questions

- Laura Fermi, *Atoms in the Family* (1954), p. 52 (lending-only).
- Segrè, *Enrico Fermi, Physicist* (1970) full text beyond the DSB sentence.
- Own-words locus or no-exception claim to lift A or B.

## Research log

- 2026-10-02: Read Britannica (Badash), MacTutor and the Nobel biography. Searched for Fermi on religion; the agnostic claim traces (via Wikipedia's footnote) to Laura Fermi, Atoms in the Family, p. 52; archive.org copies are lending-only. Nothing quoted on religion.
- 2026-10-24 (D1): Read Segrè DSB PDF (MacTutor mirror) and Fermi's 1938 Nobel lecture PDF. Segrè supplies baptism + "fundamentally an agnostic". Laura Fermi still lending-only (401 on IA OCR). P47 labels; B support corroborated; AGNOS @ 0.5; A BELOW_THRESHOLD (P20). No fallacy_catalog.
