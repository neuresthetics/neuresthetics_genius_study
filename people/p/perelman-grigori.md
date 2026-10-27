---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z10)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to living_or_recent. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (skip catch-up 10/13): New Yorker Manifold Destiny 2006 (S3) — only substantial own-voice interview; ethics/prize quotes, no creed or P16 nature-order. Wikipedia EN dual bio (S4, P50). Rejected Zabrovsky/KP 2011 interview as likely fake (Wikipedia + Gessen/Snob). Gessen Perfect Rigor never interviewed him; reviewer 'talking with God' framing is not his words. primary/A/B stay UNKNOWN (silence; heritage ≠ worldview; topology not physical science under P30). mid UNKNOWN. Chart-moving NO. P47 source_quality on all sources."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z10, order P32: F 3, rank 175). Source: MacTutor (O'Connor and Robertson). No own-voice statement on religion or nature read; Jewish parents (heritage only). Not a scientist (topology; P30). primary_system UNKNOWN; A, B, C, D, E UNKNOWN; mid_basin UNKNOWN. Span 2002–2003 (the three arXiv postings, publication; MacTutor's 'April 2002' return before the July instalment is read as 2003 from context), age 36. Not plotted. Draft, not reviewed."}

identity:
  id: perelman-grigori
  display_name: "Grigori Perelman"
  roster:
    canonical_name: "Grigori Perelman"
    rank: 175
    F: 3
    models: [Claude, GPT, Grok]
    band: "core (3–4)"
    status: "provisional"
    field: "mathematics"
    field_bucket: "mathematics"
  full_name: {value: "Grigori Yakovlevich Perelman", certainty: 0.7, cites: [{source: S1, locator: "heading"}, {source: S4, locator: "infobox"}], how_known: "MacTutor; Wikipedia EN."}
  native_name: {value: "Григорий Яковлевич Перельман", certainty: 0.7, cites: [{source: S4, locator: "infobox / lead"}], how_known: "Wikipedia EN (dual bio, P50)."}
  aliases:
    - {name: "Grigori-Perelman", kind: "roster alias"}
    - {name: "Grisha", kind: "other"}
    - {name: "Grigory Perelman", kind: "other"}

basics:
  birth:
    date: {value: "1966-06-13", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}, {source: S4, locator: "infobox"}], how_known: "MacTutor; Wikipedia EN."}
    place: {value: "Leningrad", modern_name: "Saint Petersburg, Russia", polity_then: "Soviet Union", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}, {source: S4, locator: "infobox"}], how_known: "MacTutor; Wikipedia EN."}
  death:
    date: {value: UNKNOWN, how_known: "Living (reclusive in Saint Petersburg per S4)."}
    place: {value: UNKNOWN, how_known: "Living."}
  first_lasting_contribution_year: {value: 2002, certainty: 0.7, cites: [{source: S1, locator: "Biography"}, {source: S4, locator: "Perelman's work"}], how_known: "First Ricci-flow paper posted 11 November 2002 (P12 range start)."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "Biography"}], how_known: "2002 (P2)."}
  region_of_birth: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}], how_known: "Russia (P3)."}
  region_of_work: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "Biography"}, {source: S4, locator: "Steklov / St Petersburg"}], how_known: "Steklov Institute, St Petersburg, for the 2002–2003 arXiv work (US fellowships were earlier)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English", "Russian"], certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Papers in English and Russian."}
  occupations: {value: ["mathematician"], certainty: 0.7, cites: [{source: S1, locator: "Summary"}, {source: S4, locator: "lead"}], how_known: "MacTutor; Wikipedia EN."}

contribution:
  era_bucket: living_or_recent
  fields: {value: ["geometry", "topology", "geometric analysis"], certainty: 0.7, cites: [{source: S1, locator: "Biography"}, {source: S4, locator: "lead"}], how_known: "MacTutor; Wikipedia EN."}
  lasting_original_contributions:
    - {value: "Proof of the Poincaré Conjecture (and Thurston geometrization) via Ricci flow", year: 2002, kind: "discovery", lasting: "'proved the Poincaré Conjecture' (S1, Summary); Fields Medal 2006 and Clay Prize 2010 (both refused)", certainty: 0.7, cites: [{source: S1, locator: "Summary; Biography"}, {source: S4, locator: "Perelman's work"}], how_known: "MacTutor / Wikipedia: three papers posted 11 November 2002, March 2003 and July 2003 (range; P12 start). Pure mathematics / topology — not a theory of physical systems (P30)."}
  evidence_of_impact:
    - {value: "Fields Medal (2006) and Clay Millennium Prize (2010), both refused", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "Biography"}, {source: S4, locator: "Fields Medal and Millennium Prize"}], how_known: "MacTutor; Wikipedia EN."}
    - {value: "Science Breakthrough of the Year 2006 for the Poincaré proof", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S4, locator: "lead / Breakthrough of the Year"}], how_known: "Wikipedia EN."}
  major_works:
    - {value: "Proof of the soul conjecture of Cheeger and Gromoll", year: 1994, kind: "paper or paper series", certainty: 0.7, cites: [{source: S1, locator: "Biography"}, {source: S4, locator: "Comparison geometry"}], how_known: "MacTutor / Wikipedia; not the span-setting lasting item (P12)."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Solved the Poincaré Conjecture (S1).", certainty: 0.7, cites: [{source: S1, locator: "Summary"}], how_known: "MacTutor."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Parents described as Jewish (ethnic/communal, S1/S4); no statement of household religious practice (heritage ≠ worldview)."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Yakov Perelman, electrical engineer (later emigrated to Israel)", certainty: 0.7, cites: [{source: S1, locator: "Biography"}, {source: S3, locator: "father / chess / books"}, {source: S4, locator: "Early life"}], how_known: "MacTutor; New Yorker; Wikipedia EN."}
    - {value: "Lyubov (Lubov Lvovna) Perelman, mathematics teacher", certainty: 0.7, cites: [{source: S1, locator: "Biography"}, {source: S4, locator: "Early life"}], how_known: "MacTutor; Wikipedia EN."}
  household_circumstances: {value: "Soviet Jewish family; antisemitism affected university admissions strategies for gifted Jewish students (context; S4/S1)", certainty: 0.5, cites: [{source: S1, locator: "Biography"}, {source: S4, locator: "Early life"}], how_known: "MacTutor; Wikipedia EN (Gessen-cited)."}
  schooling:
    - {value: "Sergei Rukshin mathematics club, Palace of Pioneers; Leningrad Special Mathematics and Physics School Number 239", stage: "grammar or secondary school", years: "c. 1980–1982", certainty: 0.7, cites: [{source: S1, locator: "Biography"}, {source: S4, locator: "Early life and education"}], how_known: "MacTutor; Wikipedia EN."}
    - {value: "Leningrad State University (Mathematics and Mechanics)", stage: "university", years: "1982–1987", certainty: 0.7, cites: [{source: S1, locator: "Biography"}, {source: S4, locator: "Early life and education"}], how_known: "MacTutor; Wikipedia EN."}
  early_mathematics: {value: "advanced mathematics", ages: "c. 10–16", description: "District competitions by age ten; Sergei Rukshin club; IMO gold with perfect score 1982", certainty: 0.7, cites: [{source: S1, locator: "Biography"}, {source: S4, locator: "Early life"}], how_known: "MacTutor; Wikipedia EN."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated as a childhood geometric style beyond club/Olympiad training."}
  early_science_exposure:
    - {value: "Father gave Physics for Entertainment and logic/math puzzles; chess", certainty: 0.5, cites: [{source: S3, locator: "Physics for Entertainment / chess"}], how_known: "(interview) New Yorker Manifold Destiny."}
  key_early_reading: []
  childhood_mentors:
    - {value: "Sergei Rukshin (math club coach)", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  languages_in_childhood: {value: ["Russian"], certainty: 0.5, cites: [{source: S1, locator: "Biography"}], how_known: "Inferred; English tutored for School 239 entry (S1)."}
  notable_events:
    - {value: "IMO gold medal, perfect score, Budapest 1982", certainty: 0.7, cites: [{source: S1, locator: "Biography"}, {source: S4, locator: "Early life"}], how_known: "MacTutor; Wikipedia EN."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "2002–2003", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read."}
  primary_system: {value: UNKNOWN, how_known: "No own-voice system label or creed profession. Jewish parents are heritage only (S1/S4). New Yorker (S3) covers ethics, prizes, childhood math — not religion. Do not invent from silence (brief / P19)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Rejected: no own-voice denial of God. Silence and reclusion are not ATHE."}
    - {code: AGNOS, reason: "Rejected: no own-voice suspension of judgment on God's existence (Hilbert/Gates AGNOS pattern)."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing first-hand that places or denies a personal intervening God (P19). New Yorker own-voice is ethics/prizes/opera/childhood (S3). Zabrovsky/KP 2011 rejected as likely fake. Gessen never interviewed him."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30): listed lasting contribution is topology / Ricci-flow proof of Poincaré — pure mathematics, not a theory or result about physical or natural systems (Tao RQ-Y3 / create note). Needs an explicit nature remark (P16). New Yorker and MacTutor yield none about lawful order of nature; journalists' cosmology framing of Poincaré is not his P16 statement. Do not force B from silence or from math Platonism."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read; topology of 3-manifolds is not an E claim about physical laws everywhere (P7/P19)."}
  mid_basin: {value: UNKNOWN, how_known: "A and B are UNKNOWN (P19). Chart-moving NO (deepen 2026-10-24)."}
  statements:
    - text: "I'm not interested in money or fame, I don't want to be on display like an animal in a zoo. I'm not a hero of mathematics. I'm not even that successful; that is why I don't want to have everybody looking at me."
      cites: [{source: S4, locator: "Fields Medal quotation (via BBC / Wikipedia)"}]
      date: "2006"
      context: "Fields Medal refusal; after the span; ethics/privacy, not creed."
      axes: []
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
    - text: "It is not people who break ethical standards who are regarded as aliens. It is people like me who are isolated."
      cites: [{source: S3, locator: "closing interview / ethical standards"}]
      date: "2006-06"
      context: "New Yorker Manifold Destiny walking interview, St Petersburg; after the span; math-community ethics, not creed or nature-order."
      axes: []
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
  changes_over_life: []
  coder_notes: "Deepen D1: silence on creed and on P16 is the finding, not a score. Heritage Jewish ≠ a scored adult system (no JEWISH systems/ file; heritage ≠ worldview). Not ATHE from silence. Topology → not scientist (P30). Zabrovsky 'Formula of the Universe' / KP interview rejected (fake per Wikipedia citations to Gessen/Snob). Perfect Rigor unread first-hand; Gessen states she had no conversations with him — third-party bio only. Do not force plot."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Jewish (Soviet)", certainty: 0.7, cites: [{source: S1, locator: "Biography"}, {source: S4, locator: "Early life"}], how_known: "MacTutor: parents 'were Jewish'; Wikipedia EN."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Ethnic/communal Jewish heritage recorded; religious practice of the household not stated."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "2002–2003", certainty: 0.7, cites: [{source: S1, locator: "Biography"}, {source: S4, locator: "Perelman's work"}], how_known: "The three Ricci-flow papers, November 2002 to July 2003 (P29; P12 start, P30 #4 latest year)."}
  age_at_first_lasting_contribution: {value: 36, certainty: 0.7, cites: [{source: S1, locator: "Quick Info; Biography"}], how_known: "2002 − 1966 = 36 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No creed or P16 evidence found."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None scored."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "primary_system and A–E UNKNOWN."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Geometric analysis / Ricci flow on 3-manifolds (S1/S4).", certainty: 0.5, cites: [{source: S1, locator: "Biography"}, {source: S4, locator: "Perelman's work"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not assessed for H1."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No creed or B data for H1; geometric work is Lane A contribution, not a worldview score."
  notes: ""

institutions:
  - {value: "Steklov Mathematical Institute, St Petersburg branch (PDMI)", role: "researcher", years: "1990–2005", certainty: 0.7, cites: [{source: S1, locator: "Biography"}, {source: S4, locator: "Career / resigned 2005"}], how_known: "MacTutor; Wikipedia EN (resigned December 2005)."}
  - {value: "University of California, Berkeley (Miller Research Fellowship)", role: "fellow", years: "1993–1995", certainty: 0.7, cites: [{source: S1, locator: "Biography"}, {source: S4, locator: "Early life / Career"}], how_known: "MacTutor; Wikipedia EN."}
collaborators:
  - {value: "Richard Hamilton", relation: "influenced by", note: "Ricci flow program", certainty: 0.7, cites: [{source: S1, locator: "Biography"}, {source: S3, locator: "Hamilton"}, {source: S4, locator: "Hamilton program"}], how_known: "MacTutor; New Yorker; Wikipedia EN."}
  - {value: "Mikhael Gromov", relation: "collaborator", note: "Aleksandrov spaces (1992)", certainty: 0.7, cites: [{source: S1, locator: "Biography"}, {source: S4, locator: "Alexandrov spaces"}], how_known: "MacTutor; Wikipedia EN."}
  - {value: "Yuri Burago", relation: "teacher", note: "PhD / Steklov", certainty: 0.7, cites: [{source: S1, locator: "Biography"}, {source: S4, locator: "Doctoral advisor"}], how_known: "MacTutor; Wikipedia EN."}

review:
  roster_status_reason: {value: "Provisional in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 175"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Reclusive; declined interviews after 2006; creed and P16 silence after New Yorker + search."
    - "Zabrovsky/KP 2011 interview rejected as likely fake — not used."
  open_questions:
    - "Any future verified own-voice on God/nature (unlikely given seclusion)."
    - "Optional: first-hand read of Gessen Perfect Rigor for second-hand leads only (she did not interview him)."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "J. J. O'Connor and E. F. Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. 'Grigori Yakovlevich Perelman.' MacTutor History of Mathematics, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Perelman/"
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Perelman/"
    accessed: 2026-10-19
    reliability_note: "Signed reference biography."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [review]
  - id: S3
    type: primary
    kind: "other"
    author: "Sylvia Nasar and David Gruber (interviewing Grigori Perelman)"
    citation: "Nasar, Sylvia, and David Gruber. 'Manifold Destiny.' The New Yorker, 28 August 2006 (published online 21 August 2006). https://www.newyorker.com/magazine/2006/08/28/manifold-destiny"
    url: "https://www.newyorker.com/magazine/2006/08/28/manifold-destiny"
    accessed: 2026-10-24
    reliability_note: "Only substantial verified own-voice interview (walking tour, St Petersburg, June 2006). Ethics and prize refusal; no creed or P16 nature-order quotes. PDF copy also checked."
    source_quality: "newspaper interview"
    used_for: [childhood, worldview, collaborators]
  - id: S4
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "'Grigori Perelman.' Wikipedia (English). https://en.wikipedia.org/wiki/Grigori_Perelman"
    url: "https://en.wikipedia.org/wiki/Grigori_Perelman"
    accessed: 2026-10-24
    reliability_note: "Dual bio (P50). Flags Zabrovsky interview as disputed/fake. Not used alone to invent creed scores."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, collaborators, worldview]
---

## Summary

Grigori Perelman (b. 1966), mathematician [S1][S4]. Deepen D1: primary UNKNOWN; A UNKNOWN; B UNKNOWN (topology / P30; no P16). mid UNKNOWN. Not plotted. Chart-moving NO. Silence is the finding.

## Life and work

Leningrad / St Petersburg; Steklov; US fellowships early 1990s; resigned Steklov 2005; seclusion thereafter [S1][S4].

## Contribution and impact

Poincaré Conjecture and Thurston geometrization via Ricci flow (arXiv 2002–2003); Fields and Clay prizes refused [S1][S4].

## Childhood and education

Jewish parents (heritage); School 239; Leningrad University; IMO gold 1982 [S1][S4]. Father's puzzles and *Physics for Entertainment* [S3].

## Adult working worldview

No own-voice creed or nature-order statement found [S3][S4]. New Yorker quotes concern mathematical ethics and prize refusal, not God or lawful nature. Do not invent from silence. Heritage ≠ worldview.

## Heritage (context only)

Jewish (Soviet) parents [S1][S4]. Not a scored primary_system.

## Timing

2002–2003, age 36 [S1][S4].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Geometric analysis is the contribution; no H1 worldview data.

## Open questions

- Verified future own-voice on God or P16 nature (unlikely).
- Optional first-hand Gessen for leads only (she did not interview him).

## Research log

- 2026-10-19: Read MacTutor.
- 2026-10-24: Deepen D1. Read New Yorker Manifold Destiny (S3, PDF); Wikipedia EN dual bio (S4). Searched for God/religion/atheist/P16 own-voice — none reliable. Rejected Zabrovsky/KP 2011. Noted Gessen never interviewed him. Wrote drafts/deepen_perelman-grigori.md (untracked). Local commit person file only. No figures/. No fallacy_catalog.
