---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA7)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to mathematics. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (skip catch-up 13/13 LAST; F3 rank 206). Goals: any firm A/B; do not force plot. Opened Clay CMI 2008 interview PDF (S5, own voice); Quanta Klarreich 2014 (S6, own-voice quotes); Guardian 2014 republication of Clay Q&A (S7); Wikipedia EN dual bio (S8, P50); AMS Notices 2018 memorial excerpt (S9, friends: religious beliefs unknown). No own-voice place/deny of God; no nature-order remark for P16 B. primary_system / A / B stay UNKNOWN. Rejected: Iranian birth or reported Muslim marriage ceremony (PBS documentary, secondary) as ISLAM — heritage ≠ worldview. Pure-math Platonism / 'connections with theoretical physics' (Clay) do not score B (P16; Tao/Hilbert path needs explicit lawful-nature remark). Birth date → 1977-05-12; death place Stanford Hospital; native مریم میرزاخانی. Childhood/schooling enriched. P47 source_quality on S1–S9. Chart-moving NO. No fallacy_catalog. No figures/. Draft, not reviewed."}
    - {date: 2026-10-20, by: "Grok Bot", summary: "AA8 audit fix: ICM 2022 survey locator §2.2."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA7, order P32: F 3, rank 206, provisional). Sources: the IMU's 2014 Fields Medal statement 'The Work of Maryam Mirzakhani' (read in full) and the Simons Foundation obituary (Sumner, 2017, read in full). Lasting work (after the AA7 audit, v8's call on the auditor's advice): the Eskin–Mirzakhani(–Mohammadi) 'magic wand' theorems (arXiv preprints 2013); the ICM 2022 survey by Jon Chaika and Barak Weiss (S4, EMS Press, read in full; authors and wording verified) says 'This work has revolutionized the study of dynamics on translation surfaces and has already had many applications in geometry'. The 2004 thesis results are dropped as lasting (P13, Lamarr/Johnson precedent: 'decisive step forward' and 'new and unexpected proof' are prize-time praise) and kept as a major work. Span 2013, age 36, at 0.5. Mathematician, not a scientist. Worldview: no own words read. primary_system UNKNOWN; A UNKNOWN; B UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: mirzakhani-maryam
  display_name: "Maryam Mirzakhani"
  roster:
    canonical_name: "Maryam Mirzakhani"
    rank: 206
    F: 3
    models: [Claude, GPT, Grok]
    band: "core (3–4)"
    status: "provisional"
    field: "mathematics"
    field_bucket: "mathematics"
  full_name: {value: "Maryam Mirzakhani", certainty: 0.7, cites: [{source: S1, locator: "Biography"}, {source: S8, locator: "lead"}], how_known: "IMU; Wikipedia (P50)."}
  native_name: {value: "مریم میرزاخانی", certainty: 0.7, cites: [{source: S8, locator: "infobox native_name"}], how_known: "Wikipedia Persian script (P50)."}
  aliases:
    - {name: "Maryam-Mirzakhani", kind: "roster alias"}

basics:
  birth:
    date: {value: "1977-05-12", certainty: 0.7, cites: [{source: S8, locator: "infobox / Early life"}, {source: S1, locator: "Biography"}], how_known: "Wikipedia full date (P50); IMU year 1977."}
    place: {value: "Tehran", modern_name: "Tehran, Iran", polity_then: "Imperial State of Iran", certainty: 0.7, cites: [{source: S1, locator: "Biography"}, {source: S8, locator: "Early life and education"}], how_known: "IMU; Wikipedia."}
  death:
    date: {value: "2017-07-14", certainty: 0.7, cites: [{source: S2, locator: "para. 2"}, {source: S8, locator: "death"}], how_known: "Simons Foundation; Wikipedia."}
    place: {value: "Stanford Hospital, Stanford, California", modern_name: "Stanford, California, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S8, locator: "died … at Stanford Hospital"}], how_known: "Wikipedia (P50)."}
  first_lasting_contribution_year: {value: 2013, certainty: 0.5, cites: [{source: S1, locator: "References"}, {source: S4, locator: "§2.2"}], how_known: "Eskin–Mirzakhani preprint arXiv:1302.3320 (2013), the first public statement (P30); lasting per S4 ('has revolutionized the study of dynamics on translation surfaces'). 0.5: one lasting source."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "Biography"}], how_known: "2013 (P2)."}
  region_of_birth: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Iran (P3 exception: MENA)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Harvard, Princeton, Stanford; home-region alternative MENA (AA6 rule)."}
  sex_as_recorded: {value: "female", certainty: 0.7, cites: [{source: S2, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English", "Persian"], certainty: 0.7, cites: [{source: S1, locator: "References"}, {source: S8, locator: "class notes in Persian"}], how_known: "English papers; Wikipedia: took class notes in Persian at Harvard."}
  occupations: {value: ["mathematician", "professor"], certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "IMU."}

contribution:
  primary_domain: mathematics
  fields: {value: ["mathematics", "geometry", "dynamical systems"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "IMU."}
  lasting_original_contributions:
    - {value: "Eskin–Mirzakhani(–Mohammadi) 'magic wand' theorems: rigidity of the SL2(R) action on moduli space (with Alex Eskin and Amir Mohammadi)", year: 2013, kind: "discovery", lasting: "'This work has revolutionized the study of dynamics on translation surfaces and has already had many applications in geometry' (S4, Chaika and Weiss, ICM 2022); 'a major breakthrough' (S1)", certainty: 0.5, cites: [{source: S1, locator: "p. 3; References"}, {source: S4, locator: "§2.2"}], how_known: "arXiv preprints 1302.3320 and 1305.3015 (2013), the first public statements (P30). 0.5: one lasting source."}
  evidence_of_impact:
    - {value: "Fields Medal 2014, the first woman to receive it", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S2, locator: "para. 1"}], how_known: "Simons Foundation."}
  major_works:
    - {value: "PhD thesis, Harvard (simple closed geodesics; Weil–Petersson volumes; new proof of Witten's conjecture)", year: 2004, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "pp. 2–3; Biography"}], how_known: "IMU; not lasting under P13 (AA7 audit)."}
    - {value: "'Growth of the number of simple closed geodesics on hyperbolic surfaces', Annals of Mathematics", year: 2008, kind: "paper or paper series", certainty: 0.7, cites: [{source: S1, locator: "References"}], how_known: "IMU."}
    - {value: "'Ergodic theory of the earthquake flow'", year: 2008, kind: "paper or paper series", certainty: 0.7, cites: [{source: S1, locator: "References"}], how_known: "IMU."}
  honours:
    - {value: "Fields Medal", year: 2014, certainty: 0.7, cites: [{source: S2, locator: "para. 1"}], how_known: "Simons Foundation."}
    - {value: "Satter Prize (AMS)", year: 2013, certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "IMU."}
    - {value: "Blumenthal Award", year: 2009, certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "IMU."}
  definition_fit: {value: "clearly meets", rationale: "Fields Medal; striking and highly original contributions (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "IMU."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated in own voice; friends report religious beliefs unknown (S9)."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Grew up in a family with three siblings; parents supportive of meaningful professions over achievement", role: "family", certainty: 0.7, cites: [{source: S5, locator: "earliest memories"}, {source: S7, locator: "earliest memories"}], how_known: "Own voice (Clay / Guardian)."}
    - {value: "Older brother interested her in science; told her the Gauss 1-to-100 story", role: "sibling", certainty: 0.7, cites: [{source: S5, locator: "earliest memories"}, {source: S6, locator: "Tehran"}], how_known: "Own voice (Clay); Quanta narrative."}
  household_circumstances: {value: "Tehran childhood during and after the Iran–Iraq war; 'lucky generation' when things got more stable", certainty: 0.5, cites: [{source: S5, locator: "hard times during the Iran-Iraq war"}, {source: S6, locator: "lucky generation"}], how_known: "Own voice / Quanta quotation."}
  schooling:
    - {value: "Farzanegan (NODET) middle and high school for girls, Tehran", stage: "grammar or secondary school", run_by: "state or municipal", certainty: 0.7, cites: [{source: S5, locator: "Farzanegan"}, {source: S8, locator: "Early life and education"}], how_known: "Own voice (Clay); Wikipedia."}
    - {value: "Iranian IMO team — gold 1994 (Hong Kong), gold with perfect score 1995 (Toronto)", stage: other, certainty: 0.7, cites: [{source: S2, locator: "para. 3"}, {source: S8, locator: "Early life and education"}], how_known: "Simons; Wikipedia."}
    - {value: "Sharif University of Technology, Tehran (BSc mathematics 1999)", stage: university, certainty: 0.7, cites: [{source: S1, locator: "Biography"}, {source: S8, locator: "Early life and education"}], how_known: "IMU; Wikipedia."}
    - {value: "Harvard University PhD 2004 under Curtis McMullen", stage: university, certainty: 0.7, cites: [{source: S1, locator: "Biography"}, {source: S5, locator: "profile"}], how_known: "IMU; Clay."}
  early_mathematics: {value: "advanced mathematics", certainty: 0.7, cites: [{source: S5, locator: "earliest memories; Olympiads"}, {source: S8, locator: "IMO golds"}], how_known: "Own voice: Olympiad problem-solving after a poor middle-school math year; Gauss 1–100 story from brother (S5); IMO golds (S8).", note: "Enum 'advanced mathematics' for Olympiad-level; narrative in how_known."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated as childhood geometric style; adult work is hyperbolic geometry."}
  early_science_exposure:
    - {value: "TV biographies of Marie Curie and Helen Keller; novel Lust for Life (van Gogh)", certainty: 0.5, cites: [{source: S6, locator: "Tehran"}], how_known: "Quanta (paraphrase of her childhood reading); Clay/AMS profiles echo writer ambition."}
  key_early_reading:
    - {value: "Novels as chief pastime; dreamt of becoming a writer before high-school math turn", certainty: 0.7, cites: [{source: S5, locator: "earliest memories"}, {source: S7, locator: "earliest memories"}], how_known: "Own voice."}
  childhood_mentors:
    - {value: "Roya Beheshti (lifelong friend from first week of middle school; later collaborator)", role: "peer", certainty: 0.7, cites: [{source: S5, locator: "Roya Beheshti"}, {source: S6, locator: "Tehran"}], how_known: "Own voice / Quanta."}
    - {value: "Farzanegan school principal (arranged math Olympiad classes for girls)", role: "teacher", certainty: 0.5, cites: [{source: S6, locator: "principal of the school"}], how_known: "Quanta quotation of Mirzakhani."}
  languages_in_childhood: {value: ["Persian"], certainty: 0.7, cites: [{source: S8, locator: "native language Persian"}], how_known: "Wikipedia; Iran upbringing."}
  notable_events:
    - {value: "First Iranian woman to win IMO gold (1994); perfect score / two golds (1995)", year: 1994, certainty: 0.7, cites: [{source: S8, locator: "Early life and education"}, {source: S2, locator: "para. 3"}], how_known: "Wikipedia; Simons."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "2013", certainty: 0.5, cites: [{source: S1, locator: "Biography; References"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Clay/Quanta/Guardian interviews discuss mathematics practice only; no science–religion creed."}
  primary_system: {value: UNKNOWN, how_known: "No own-voice system label in Clay (S5), Quanta (S6), Guardian (S7), IMU, or Simons. Friends: deepest religious beliefs unknown (S9). Iranian birth and a reported Muslim marriage ceremony (secondary documentary report) are heritage/practice context only — never a worldview code."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: ISLAM, reason: "Rejected: Iranian upbringing and secondary report of a Muslim marriage ceremony are not own-voice doctrine (heritage ≠ worldview)."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing first-hand that places or denies a personal intervening God (P19). Own-voice interviews (S5–S7) are silent on God/religion. S9: close friends did not know her religious beliefs."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30: pure mathematics; moduli / dynamics of surfaces, not a theory of physical systems). Clay remark that moduli spaces have 'connections with theoretical physics' is bibliographic adjacency, not a P16 lawful-order-of-nature statement (contrast Tao Lex path). Math beauty / patience remarks (S5) are practice, not nature-order."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read; not scored from pure math alone (P19)."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied (P19)."}
  statements:
    - text: "There are also connections with theoretical physics, topology, and combinatorics. I find it fascinating that you can look at the same problem from different perspectives, and approach it using different methods."
      cites: [{source: S5, locator: "research description"}]
      date: "2008"
      context: "Clay Mathematics Institute research-fellow interview; describing moduli-space work."
      axes: [B_cause]
      kind: "recorded interview"
      verified_against: "newspaper interview"
      verified_on: 2026-10-24
      note: "Documented and rejected for B under P16: 'connections with theoretical physics' is not an explicit lawful-order-of-nature remark (Hilbert/Tao path). Pure-math practice."
    - text: "I can see that without being excited mathematics can look pointless and cold. The beauty of mathematics only shows itself to more patient followers."
      cites: [{source: S5, locator: "advice to lay persons"}, {source: S7, locator: "advice"}]
      date: "2008"
      context: "Clay interview (also Guardian 2014 republication); about mathematics, not creed."
      axes: [B_cause]
      kind: "recorded interview"
      verified_against: "newspaper interview"
      verified_on: 2026-10-24
      note: "Math aesthetics / practice; not used to score A or B."
  changes_over_life: []
  coder_notes: "Deepen D1: searched Clay, Quanta, Guardian, Wikipedia, AMS Notices memorials, web for God/faith/atheist/Muslim own-voice — none. S9 friends: religious beliefs unknown. Do not invent ISLAM from heritage or wedding rite. Do not score B from pure math or physics-adjacency (P16). Chart-moving NO. No fallacy_catalog (Jason)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Iranian", certainty: 0.7, cites: [{source: S8, locator: "lead"}, {source: S1, locator: "Biography"}], how_known: "Wikipedia; IMU."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated in sources read; do not infer Islam from Iranian nationality."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated. Secondary documentary report of a Muslim marriage ceremony (with civil marriage) is not coded as initiation or worldview."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "2013", certainty: 0.5, cites: [{source: S1, locator: "References"}, {source: S4, locator: "§2.2"}], how_known: "The one listed lasting item (P29, P30); 0.5."}
  age_at_first_lasting_contribution: {value: 36, certainty: 0.5, cites: [{source: S1, locator: "Biography"}, {source: S8, locator: "birth 1977"}], how_known: "2013 − 1977 = 36 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No LIO-scoring own-voice found."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "No LIO scores."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "primary_system UNKNOWN; A/B UNKNOWN."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Hyperbolic geometry and moduli spaces (S1); Lane B geometric cue only — does not score A/B.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable as worldview evidence."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "Pure mathematician; no creed or nature-order own-voice; not plotted."
  notes: "Lane B only. Geometric research form is not a substitute for scored A/B."

institutions:
  - {value: "Princeton University; Clay Mathematics Institute", role: "assistant professor; research fellow", years: "2004–2008", kind: "university", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "IMU."}
  - {value: "Stanford University", role: "professor", years: "2008–2017", kind: "university", certainty: 0.7, cites: [{source: S2, locator: "para. 4"}, {source: S8, locator: "full professor 2009"}], how_known: "Simons; Wikipedia."}
collaborators:
  - {value: "Curtis McMullen", relation: "teacher", note: "PhD advisor", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "IMU."}
  - {value: "Alex Eskin", relation: "collaborator", note: "rigidity theorem", certainty: 0.7, cites: [{source: S1, locator: "p. 3"}], how_known: "IMU."}
  - {value: "Jan Vondrák", relation: "other", note: "Spouse (theoretical computer scientist)", certainty: 0.7, cites: [{source: S6, locator: "future husband"}, {source: S8, locator: "spouse"}], how_known: "Quanta; Wikipedia."}

review:
  roster_status_reason: {value: "Provisional in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 206"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Worldview: no own-voice creed or nature-order statement after deepen (S5–S9)."
    - "One lasting source (S4); span at 0.5."
    - "Intensely private on religion per friends (S9)."
  open_questions:
    - "A lasting source for the 2004 thesis results would restore 2004 (age 27) as an alternative."
    - "Any unpublished letter or private creed statement (unlikely to surface; friends report silence)."

sources:
  - id: S1
    type: secondary
    kind: "institutional page"
    author: "International Mathematical Union"
    citation: "International Mathematical Union. 'The Work of Maryam Mirzakhani.' Fields Medal 2014 news release. https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2014/news_release_mirzakhani.pdf"
    url: "https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2014/news_release_mirzakhani.pdf"
    accessed: 2026-10-19
    reliability_note: "Prize statement, read in full."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, timing, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "Thomas Sumner"
    citation: "Sumner, Thomas. 'Remembering the Life and Contributions of Fields Medalist Maryam Mirzakhani.' Simons Foundation, 20 July 2017. https://www.simonsfoundation.org/news/fields-medalist-maryam-mirzakhani-dies-at-40/"
    url: "https://www.simonsfoundation.org/news/fields-medalist-maryam-mirzakhani-dies-at-40/"
    accessed: 2026-10-19
    reliability_note: "Obituary, read in full."
    source_quality: "reference entry"
    used_for: [identity, contribution, childhood, institutions]
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
    type: secondary
    kind: "book chapter"
    author: "Jon Chaika; Barak Weiss"
    citation: "Chaika, Jon, and Barak Weiss. 'The horocycle flow on the moduli space of translation surfaces.' Proceedings of the International Congress of Mathematicians 2022, vol. 5, pp. 3412–3430. EMS Press. doi:10.4171/ICM2022/89"
    url: "https://ems.press/books/standalone/277/5520"
    accessed: 2026-10-19
    reliability_note: "Open-access survey, read in full; authors and wording verified."
    source_quality: "scholarly edition or monograph"
    used_for: [basics, contribution, timing]
  - id: S5
    type: primary
    kind: "other"
    author: "Maryam Mirzakhani, interviewed for Clay Mathematics Institute"
    citation: "'Interview with Research Fellow Maryam Mirzakhani.' Clay Mathematics Institute Annual Report 2008, pp. 11–13. https://www.claymath.org/library/annual_report/ar2008/08Interview.pdf"
    url: "https://www.claymath.org/library/annual_report/ar2008/08Interview.pdf"
    accessed: 2026-10-24
    reliability_note: "Published PDF interview; own-voice on education and research; silent on religion/God; physics-adjacency line documented and rejected for B (P16)."
    source_quality: "newspaper interview"
    used_for: [childhood, worldview]
  - id: S6
    type: secondary
    kind: "other"
    author: "Erica Klarreich"
    citation: "Klarreich, Erica. 'A Tenacious Explorer of Abstract Surfaces.' Quanta Magazine, 12 August 2014. https://www.quantamagazine.org/maryam-mirzakhani-is-first-woman-fields-medalist-20140812/"
    url: "https://www.quantamagazine.org/maryam-mirzakhani-is-first-woman-fields-medalist-20140812/"
    accessed: 2026-10-24
    reliability_note: "Long profile with many direct quotations; math practice and biography; no creed."
    source_quality: "newspaper interview"
    used_for: [childhood, worldview, collaborators]
  - id: S7
    type: primary
    kind: "other"
    author: "Maryam Mirzakhani (Clay interview republished)"
    citation: "'Maryam Mirzakhani: \"The more I spent time on maths, the more excited I got\".' The Guardian, 13 August 2014 (republication of Clay CMI interview). https://www.theguardian.com/science/2014/aug/13/interview-maryam-mirzakhani-fields-medal-winner-mathematician"
    url: "https://www.theguardian.com/science/2014/aug/13/interview-maryam-mirzakhani-fields-medal-winner-mathematician"
    accessed: 2026-10-24
    reliability_note: "Guardian republication of S5 Clay Q&A; same own-voice text."
    source_quality: "newspaper interview"
    used_for: [childhood, worldview]
  - id: S8
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "'Maryam Mirzakhani.' Wikipedia (English). Accessed via MediaWiki API / page text, 24 October 2026."
    url: "https://en.wikipedia.org/wiki/Maryam_Mirzakhani"
    accessed: 2026-10-24
    reliability_note: "Dual bio (P50) for birth/death dates and places, native name, schooling; not used for A/B."
    source_quality: "reference entry"
    used_for: [identity, basics, childhood, heritage, institutions, collaborators]
  - id: S9
    type: secondary
    kind: "journal article"
    author: "AMS Notices memorial contributors (graduate-school friends)"
    citation: "'Maryam Mirzakhani' (memorial article). Notices of the American Mathematical Society 65, no. 10 (November 2018): 1221ff. https://www.ams.org/journals/notices/201810/rnoti-p1221.pdf"
    url: "https://www.ams.org/journals/notices/201810/rnoti-p1221.pdf"
    accessed: 2026-10-24
    reliability_note: "Friends: 'Even after knowing her for so many years, we do not know her deepest religious, social, or political beliefs.' Used only to document silence — not a creed score."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, review]
---

## Summary

Maryam Mirzakhani (1977–2017), Iranian mathematician, Fields Medal 2014 [S1; S2; S8]. Deepen D1: primary_system UNKNOWN; A UNKNOWN; B UNKNOWN; mid_basin UNKNOWN. Not plotted. Chart-moving NO.

## Life and work

Born Tehran, 12 May 1977 [S8]. Farzanegan / Sharif / Harvard PhD 2004 (McMullen) [S1; S5; S8]. Princeton and Clay fellow; Stanford professor [S1; S2]. Died 14 July 2017 at Stanford Hospital [S8].

## Contribution and impact

Eskin–Mirzakhani(–Mohammadi) magic-wand / rigidity theorems, arXiv 2013 [S1; S4]. Fields Medal 2014 [S2]. Thesis 2004 kept as major work, not lasting (P13) [S1].

## Childhood and education

Tehran; supportive family; brother sparked science interest [S5]. Farzanegan NODET; IMO golds 1994–95 [S8]. Writer ambition before high-school math turn [S5].

## Adult working worldview

No own-voice creed or nature-order statement in Clay, Quanta, or Guardian [S5–S7]. Friends report religious beliefs unknown [S9]. Pure mathematician: B not scored from math or physics-adjacency (P16). Heritage/Muslim marriage reports not coded as ISLAM.

## Heritage (context only)

Iranian [S8]. Religious heritage UNKNOWN — not inferred from nationality.

## Timing

2013 (0.5), age 36 [S1; S4].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Geometric research form present; no scored A/B. Not plotted.

## Open questions

- Lasting source for the 2004 thesis.
- Any private creed document (friends report silence).

## Research log

- 2026-10-24: Deepen D1 (LAST catch-up 13/13). Clay PDF, Quanta, Guardian, Wikipedia, AMS Notices. A/B/primary stay UNKNOWN. Chart NO. No fallacy_catalog; no figures/.
- 2026-10-20: AA8 audit fix: ICM 2022 survey locator §2.2.
- 2026-10-19: Read IMU Fields statement; Simons obituary.
