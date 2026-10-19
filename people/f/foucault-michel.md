---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch U)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch U, order P32: F 4, rank 117). Basics from Britannica (James Faubion, Britannica Editors) and SEP (Gutting and Oksala); Catholic upbringing and the absence of belief from Michael C. Behrent's Commonweal interview (15 October 2026). No text of his own on God or nature read. Not a scientist (P30). primary_system BELOW_THRESHOLD; A BELOW_THRESHOLD; B, C, D, E UNKNOWN; mid_basin UNKNOWN. Span 1975–1979 (0.5). Not plotted. Draft, not reviewed."}

identity:
  id: foucault-michel
  display_name: "Michel Foucault"
  roster:
    canonical_name: "Michel Foucault"
    rank: 117
    F: 4
    models: [Claude, DeepSeek, Gemini, Grok]
    band: "core (3–4)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Paul-Michel Foucault", certainty: 0.7, cites: [{source: S1, locator: "facts box (In full)"}], how_known: "Britannica."}
  native_name: {value: "Paul-Michel Foucault", certainty: 0.7, cites: [{source: S1, locator: "facts box"}], how_known: "French; same as the full name."}
  aliases:
    - {name: "Foucault-Michel", kind: "roster alias"}

basics:
  birth:
    date: {value: "1926-10-15", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "facts box (Born)"}, {source: S2, locator: "§1 Biographical Sketch"}], how_known: "Britannica and SEP agree."}
    place: {value: "Poitiers", modern_name: "Poitiers, France", polity_then: "France", certainty: 1.0, cites: [{source: S1, locator: "facts box (Born)"}, {source: S2, locator: "§1 Biographical Sketch"}], how_known: "Britannica and SEP."}
  death:
    date: {value: "1984-06-25", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "facts box (Died)"}, {source: S2, locator: "§1 Biographical Sketch"}], how_known: "Britannica and SEP."}
    place: {value: "Paris", modern_name: "Paris, France", polity_then: "France", certainty: 1.0, cites: [{source: S1, locator: "facts box (Died)"}, {source: S2, locator: "§1 Biographical Sketch"}], how_known: "Britannica and SEP; an early victim of AIDS (S2)."}
  first_lasting_contribution_year: {value: 1975, certainty: 0.5, cites: [{source: S2, locator: "§3.4 History of the Prison"}, {source: S3, locator: "answer on where newcomers should start"}], how_known: "Discipline and Punish (1975). Coder's call between this and The Order of Things (1966); see timing.major_work_period."}
  era_bucket: {value: "1950 on", certainty: 0.5, cites: [{source: S2, locator: "§3.4 History of the Prison"}], how_known: "1975 (P2); 1966 under the alternative, same bucket."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "facts box"}, {source: S2, locator: "§1 Biographical Sketch"}], how_known: "France (P3)."}
  region_of_work: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "'Education and career'"}, {source: S2, locator: "§1 Biographical Sketch"}], how_known: "France, chiefly Paris (Collège de France)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "'Education and career'"}], how_known: "'The son and grandson of a physician'."}
  languages_of_work: {value: ["French"], certainty: 0.7, cites: [{source: S1, locator: "'Education and career'"}], how_known: "Coder's reading."}
  occupations: {value: ["philosopher and historian", "professor of the history of systems of thought, Collège de France", "cultural attaché (Uppsala, Warsaw, Hamburg)"], certainty: 0.7, cites: [{source: S1, locator: "'Education and career'"}, {source: S2, locator: "§1 Biographical Sketch"}], how_known: "Britannica and SEP."}

contribution:
  fields: {value: ["philosophy", "history of systems of thought", "social theory"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "opening; §1"}], how_known: "Britannica and SEP."}
  lasting_original_contributions:
    - {value: "Discipline and Punish (Surveiller et punir): the modern prison and disciplinary power as subject formation", year: 1975, kind: work, lasting: "'The critical impact of Discipline and Punish' (S2); among 'His best-known works' (S1, question box); 'The orthodox answer' for where to start (S3)", certainty: 0.7, cites: [{source: S1, locator: "'Education and career'"}, {source: S2, locator: "§3.4 History of the Prison"}, {source: S3, locator: "answer on where newcomers should start"}], how_known: "SEP and Behrent. Not a theory about natural systems, so not a scientist (P30)."}
    - {value: "The History of Sexuality, vol. 1: power as productive and diffuse ('microphysics of power')", year: 1976, kind: work, lasting: "'one of the most influential contemporary understandings of power' (S2); 'canonical for gay and lesbian studies and queer theory' (S1, question box)", certainty: 0.7, cites: [{source: S2, locator: "§3.5 History of Modern Sexuality"}, {source: S3, locator: "answer on the fourth volume"}], how_known: "SEP; date from Behrent ('published the first volume in 1976')."}
    - {value: "Collège de France lectures Security, Territory, Population (1977–78) and The Birth of Biopolitics (1978–79): government and governmentality", year: 1977, kind: "body of work", lasting: "'have been especially influential' (S2)", certainty: 0.5, cites: [{source: S2, locator: "§4 Foucault after Foucault"}], how_known: "SEP. Published posthumously; dated by delivery (P30), range 1977–1979, start year (P12). Whether a posthumously published lecture course sets the span end is the coder's call; 1976 is the named alternative end."}
  evidence_of_impact:
    - {value: "'one of the most influential and controversial scholars of the post-World War II period'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "'regularly reported to be the most cited scholar in the social sciences and humanities'", kind: other, certainty: 0.5, cites: [{source: S3, locator: "question on summarizing his thought"}], how_known: "The interviewer's words, not Behrent's; 0.5."}
  major_works:
    - {value: "Folie et déraison (History of Madness)", year: 1961, certainty: 0.7, cites: [{source: S1, locator: "'Education and career'"}], how_known: "Britannica: 'critical praise but a limited audience'."}
    - {value: "Les Mots et les choses (The Order of Things)", year: 1966, certainty: 0.7, cites: [{source: S1, locator: "'Education and career'"}, {source: S3, locator: "answer on The Order of Things"}], how_known: "Britannica ('wide notice'); Behrent: 'basically a forgotten book'."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "'one of the most influential' scholars after 1945 (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Catholic (nominal)", certainty: 0.5, cites: [{source: S3, locator: "first answer"}], how_known: "Behrent: 'nominally Catholic'; parents married in church; the maternal Malapert side had 'a Voltairian streak'. One scholar's account."}
  family_religious_practice: {value: "Maternal grandmother went to Mass almost daily and the boys sometimes went with her; he served as an altar boy at Saint-Porchaire", certainty: 0.5, cites: [{source: S3, locator: "first answer"}], how_known: "Behrent, citing the brother's memory."}
  parents_and_household:
    - {value: "Father: Paul Foucault, surgeon and obstetrician in Poitiers, of a family of doctors", certainty: 0.7, cites: [{source: S1, locator: "'Education and career'"}, {source: S3, locator: "first answer"}], how_known: "Britannica ('son and grandson of a physician') and Behrent."}
    - {value: "Mother: of the Malapert family, pharmacists in Poitiers; died 1987", certainty: 0.5, cites: [{source: S3, locator: "first answer"}], how_known: "Behrent."}
  household_circumstances: {value: "'solidly bourgeois' provincial medical family", certainty: 0.7, cites: [{source: S1, locator: "'Education and career'"}, {source: S3, locator: "first answer"}], how_known: "Britannica and Behrent."}
  schooling:
    - {value: "Collège Saint-Stanislas, Poitiers, run by the Brothers of the Christian Schools (De La Salle); most of his high-school years; taught philosophy by the Benedictine Marcel Pierrot", stage: "grammar or secondary school", run_by: "religious body", years: "to 1943", certainty: 0.5, cites: [{source: S3, locator: "first answer"}], how_known: "Behrent; end year the coder's reading of the 1942–43 baccalaureate year."}
    - {value: "State lycée in Poitiers, before Saint-Stanislas and again to prepare for the ENS entrance exam", stage: "grammar or secondary school", run_by: "state or municipal", certainty: 0.5, cites: [{source: S3, locator: "first answer"}], how_known: "Behrent; years not stated."}
    - {value: "École Normale Supérieure, Paris: psychology and philosophy; graduated 1952", stage: university, run_by: "state or municipal", years: "1946–1952", certainty: 0.7, cites: [{source: S1, locator: "'Education and career'"}], how_known: "Britannica; operator the coder's reading."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Marcel Pierrot, Benedictine monk of Ligugé, his philosophy teacher", certainty: 0.5, cites: [{source: S3, locator: "first answer"}], how_known: "Behrent, from Pierrot's handwritten autobiography."}
  languages_in_childhood: {value: ["French"], certainty: 0.5, cites: [{source: S1, locator: "'Education and career'"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "His expected philosophy teacher, the priest Georges Duret, was arrested by the Gestapo in September 1942", certainty: 0.5, cites: [{source: S3, locator: "first answer"}], how_known: "Behrent."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1975–1979", certainty: 0.5, cites: [{source: S2, locator: "§3.4; §4"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Raised nominally Catholic; altar boy; Catholic secondary school", certainty: 0.5, cites: [{source: S3, locator: "first answer"}], how_known: "Behrent. Upbringing only; no code (CHRIST do_not_use_when)."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing in his own words read."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "No statement of his own on God read. Behrent: 'nowhere in Foucault’s writings, published or otherwise, and nowhere in any testimony about Foucault ... is there the slightest bit of evidence to suggest he believed in God or any other doctrine of the Catholic Church' and 'In many respects, he was an anti-Catholic one' (S3). Absence of belief is not a stated denial (ATHE) or suspension (AGNOS); a scholar's report of an absence, so a lead toward ATHE only."}
  secondary_system: {value: UNKNOWN, how_known: "One system (P29)."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Lead: no evidence of belief (S3); no denial in his words read."}
    - {code: AGNOS, reason: "Rejected: no stated suspension read."}
    - {code: CHRIST, reason: "Rejected: upbringing only (S3)."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "No locus view read; Behrent's report of no belief (S3) does not say what he held."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); the sources read give nothing of his on natural law or exception (P16, P19). A 1967 interview text seen only on a mailing list was not used."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing on reward and punishment of persons in his own view (P19); his histories of Christian confession and 'salvation' (S2 §3.5, S3) describe others' views."}
    D_authority: {value: UNKNOWN, how_known: "Nothing on revelation against observation read (P19)."}
    E_scope: {value: UNKNOWN, how_known: "Nothing on the world's order read (P7, P19)."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN, which takes precedence (P19)."}
  statements: []
  changes_over_life:
    - {value: "Catholic upbringing and schooling; 'embraced and then abandoned communism' at the ENS", certainty: 0.5, cites: [{source: S1, locator: "'Education and career'"}, {source: S3, locator: "first answer"}], how_known: "Britannica (communism) and Behrent (upbringing); before the span."}
  coder_notes: "Coder's call on the span. Start 1975 (Discipline and Punish: SEP 'critical impact', Behrent's 'orthodox' starting point); alternative start 1966 (The Order of Things: Britannica 'wide notice', but Behrent calls it 'basically a forgotten book'). End 1979 (The Birth of Biopolitics, delivered 1978–79, published posthumously; SEP 'especially influential'; dated by delivery, P30); alternative end 1976 (History of Sexuality vol. 1, 'most influential'). The span does not move any score: every axis is unscored. Leads: the 1952–53 Lille course 'Knowledge of Man and Transcendental Reflection' (published 2022; per S3, a philosophy of man impossible while knowledge was 'anchored in the belief in an infinite being'); interviews in Dits et écrits. Not plotted."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "French provincial bourgeoisie", certainty: 0.5, cites: [{source: S1, locator: "'Education and career'"}], how_known: "Coder's reading of 'solidly bourgeois'."}
  religious_heritage_by_birth: {value: "Catholic", certainty: 0.5, cites: [{source: S3, locator: "first answer"}], how_known: "Behrent."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1975–1979", certainty: 0.5, cites: [{source: S2, locator: "§3.4; §3.5; §4"}, {source: S3, locator: "answer on where newcomers should start"}], how_known: "From Discipline and Punish (1975) to the end of The Birth of Biopolitics lectures (1979) (P12, P30). Coder's call; alternatives 1966 for the start and 1976 for the end (coder_notes)."}
  age_at_first_lasting_contribution: {value: 49, certainty: 0.5, cites: [{source: S1, locator: "facts box"}, {source: S2, locator: "§3.4"}], how_known: "1975 − 1926 = 49 (P30); 40 under the 1966 alternative."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No LIO-type statement read."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S3, locator: "first answer"}], how_known: "None in the sources read."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "§3"}], how_known: "Not assessed."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "§3"}], how_known: "Not assessed."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S2, locator: "§3"}], how_known: "Coder's reading."}
  reading: "Power and knowledge as inseparable; the subject formed by practices."
  notes: ""

institutions:
  - {value: "University of Lille", role: "teacher", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Education and career'"}], how_known: "Britannica; years not stated (after 1952)."}
  - {value: "French cultural service (Uppsala, Warsaw, Hamburg)", role: "cultural attaché", years: "1955–1960", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "'Education and career'"}], how_known: "Britannica."}
  - {value: "University of Clermont-Ferrand", role: "teacher", years: "1960–1966", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Education and career'"}], how_known: "Britannica."}
  - {value: "University of Tunis", role: "teacher", years: "1966–1968", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Education and career'"}], how_known: "Britannica."}
  - {value: "Collège de France", role: "professor of the history of systems of thought", years: "1970–1984", kind: "research institute", certainty: 0.5, cites: [{source: S1, locator: "'Education and career'"}, {source: S2, locator: "§1 Biographical Sketch"}], how_known: "Britannica says awarded the chair in 1970; SEP says elected in 1969. 0.5."}
collaborators:
  - {value: "Marcel Pierrot", relation: teacher, note: "Benedictine monk; school philosophy teacher (1942–43)", certainty: 0.5, cites: [{source: S3, locator: "first answer"}], how_known: "Behrent."}
  - {value: "Friedrich Nietzsche", relation: "influenced by", note: "'his greatest philosophical influence' (S3)", certainty: 0.5, cites: [{source: S3, locator: "first answer"}], how_known: "Behrent."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 117"}], how_known: "Study roster."}
  controversies:
    - {value: "Vilified by the right as deviant and subversive in his lifetime; some on the left later rejected his approach", certainty: 0.5, cites: [{source: S3, locator: "standfirst"}], how_known: "Commonweal's introduction."}
  data_quality_flags:
    - "No primary text on God or nature read; the religion fields rest on one scholar's interview answers."
    - "Span is a coder's call with named alternatives."
  open_questions:
    - "Interviews in Dits et écrits for statements on God, religion or nature."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "James Faubion; Britannica Editors"
    citation: "Faubion, James, and Britannica Editors. \"Michel Foucault.\" Encyclopaedia Britannica (updated 11 October 2026). https://www.britannica.com/biography/Michel-Foucault. Read live 2026-10-19."
    url: "https://www.britannica.com/biography/Michel-Foucault"
    accessed: 2026-10-19
    reliability_note: "Signed article; facts box and 'Education and career' cited; question boxes cited only where marked."
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Gary Gutting and Johanna Oksala"
    citation: "Gutting, Gary, and Johanna Oksala. \"Michel Foucault.\" Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/entries/foucault/"
    url: "https://plato.stanford.edu/entries/foucault/"
    accessed: 2026-10-19
    reliability_note: "Signed scholarly encyclopedia; §1, §3.4, §3.5 and §4 used."
    used_for: [basics, contribution, worldview, timing, institutions]
  - id: S3
    type: secondary
    kind: other
    author: "Michael C. Behrent, interviewed by Daniel Steinmetz-Jenkins"
    citation: "Steinmetz-Jenkins, Daniel. \"Foucault at a Hundred: An interview with Michael C. Behrent.\" Commonweal, 15 October 2026. https://www.commonwealmagazine.org/steinmetz-jenkins-foucault-interview-Behrent"
    url: "https://www.commonwealmagazine.org/steinmetz-jenkins-foucault-interview-Behrent"
    accessed: 2026-10-19
    reliability_note: "Email interview with the intellectual historian Michael C. Behrent (author of Becoming Foucault: The Poitiers Years). Behrent's answers are a scholar's account; the interviewer's lines are not cited as fact. Locators by answer."
    used_for: [childhood, heritage, worldview, contribution, timing, collaborators, review]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Michel Foucault

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Michel Foucault (1926–1984), French philosopher and historian [S1]. Draft: primary_system BELOW_THRESHOLD; A BELOW_THRESHOLD; B UNKNOWN; mid_basin UNKNOWN. Not plotted.

## Life and work

ENS, Lille, Uppsala, Warsaw, Hamburg, Clermont-Ferrand, Tunis, the Collège de France [S1, S2].

## Contribution and impact

Discipline and Punish (1975), The History of Sexuality vol. 1 (1976), the governmentality lectures [S2].

## Childhood and education

A nominally Catholic medical family in Poitiers; Catholic school [S1, S3].

## Adult working worldview

No evidence 'to suggest he believed in God' (Behrent) [S3]; nothing in his own words read.

## Heritage (context only)

Catholic [S3].

## Timing

1975–1979, from age 49 [S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Not assessed.

## Open questions

- Dits et écrits interviews.

## Research log

- 2026-10-19: Read Britannica, SEP and the Commonweal interview.
