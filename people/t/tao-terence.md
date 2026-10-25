---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Y)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit fixes for batch Y (gs_7b46f24_Y run 1): (TA7) Solving mathematical problems dated 1992, its first edition (written 1990; MacTutor). Ruling Y3 (v8's call on the auditor's advice): not a scientist; B stays UNKNOWN (recorded under P30). No score changes."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Y, order P32: F 4, rank 134; roster status provisional). Basics from Britannica (Jeremy John Gray, 18 Oct 2026) and MacTutor (O'Connor and Robertson, December 2023). The Green–Tao theorem dated by its arXiv submission (8 April 2004; Annals of Mathematics 2008). No statement on religion or nature found in a reliable source; web pages offering 'quotes' on his faith are unsourced and not used. Not a scientist (pure mathematics; RQ-Y3). Span 2004 at 0.5. primary_system and all axes UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (catch-up 3/13; F4 rank 134). Needs: firm A/B if sources allow; Hilbert/P16 for B (not P35 — ruling Y3 not scientist). Opened Lex Fridman Podcast #472 transcript (S5, 2025); Quanta / Joy of Why 1 Feb 2024 (S6); blog 'What are the odds?' 3 Oct 2022 (S7); Wikipedia EN dual bio (S8, P50). Rejected: St Augustine 'Quiet Faith' and parallel unsourced faith pages (fabricated/unsourced quotes); Medium 'Terence Tao' Christian blog is a different person. A_locus stays UNKNOWN (no own-voice place/deny of God; blog divine-lottery example is epistemic, not creed). primary_system stays UNKNOWN. B_cause UNKNOWN → 3 @0.5 alt 4 (interview): Lex own-voice that the universe is comprehensible (Einstein endorsement), that simple laws emerge (universality; bell curve 'everywhere in nature'), and that the laws of physics are translation/rotation/time invariant (Noether explanation) — Hilbert P16 addendum lawful-order remark, not math Platonism alone (Quanta S6 Platonism about mathematical objects would be BELOW under P16). Support single. After span (P20). mid_basin UNKNOWN (A UNKNOWN, P19). Chart-moving NO. P47 source_quality on S1–S8. Native name 陶哲轩 from Wikipedia. No fallacy_catalog. No figures/. Draft, not reviewed."}

identity:
  id: tao-terence
  display_name: "Terence Tao"
  roster:
    canonical_name: "Terence Tao"
    rank: 134
    F: 4
    models: [Claude, Gemini, GPT, Grok]
    band: "core (3–4)"
    status: provisional
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Terence Chi-Shen Tao", certainty: 0.7, cites: [{source: S2, locator: "Quick Info"}, {source: S8, locator: "infobox birth_name"}], how_known: "MacTutor; Wikipedia."}
  native_name: {value: "陶哲轩", certainty: 0.7, cites: [{source: S8, locator: "infobox native_name"}], how_known: "Wikipedia Chinese characters."}
  aliases:
    - {name: "Tao-Terence", kind: "roster alias"}
    - {name: "Terence-Tao", kind: "roster alias"}
    - {name: "Terry Tao", kind: other}

basics:
  birth:
    date: {value: "1975-07-17", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "Quick Info"}, {source: S8, locator: "infobox"}], how_known: "Britannica, MacTutor, Wikipedia."}
    place: {value: "Adelaide, South Australia", modern_name: "Adelaide, South Australia, Australia", polity_then: "Australia", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "Quick Info"}, {source: S8, locator: "infobox"}], how_known: "All three bios."}
  death:
    date: {value: UNKNOWN, how_known: "Living (Britannica; Wikipedia; Lex Fridman 2025 interview)."}
    place: {value: UNKNOWN, how_known: "Living."}
  first_lasting_contribution_year: {value: 2004, certainty: 0.5, cites: [{source: S2, locator: "Fields Medal paragraphs ('work with Ben Green on the distribution of prime numbers'; 'This fantastic achievement')"}, {source: S3, locator: "arXiv math/0404188, submitted 8 Apr 2004"}], how_known: "The Green–Tao theorem (the primes contain arbitrarily long arithmetic progressions), dated by its first public statement, the arXiv preprint of 8 April 2004 (S3; P30); published in Annals of Mathematics 167 (2008), 481–547 (Crossref). His earlier work on the Kakeya problem and the nonlinear Schrödinger equation is undated in the sources read and may be earlier (P12), so 0.5."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Born 1975; every adult year falls in '1950 on' (P2)."}
  region_of_birth: {value: "Oceania", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "Quick Info"}], how_known: "Australia (P3)."}
  region_of_work: {value: "North America", certainty: 1.0, cites: [{source: S1, locator: "body ('joined the faculty at the University of California, Los Angeles')"}, {source: S2, locator: "career paragraphs"}, {source: S8, locator: "Personal life"}], how_known: "UCLA from 1996; lives in Los Angeles."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S2, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S3, locator: "paper"}], how_known: "His papers."}
  occupations: {value: ["mathematician", "professor at the University of California, Los Angeles"], certainty: 1.0, cites: [{source: S1, locator: "body"}, {source: S2, locator: "career paragraphs"}], how_known: "Both sources."}

contribution:
  fields: {value: ["partial differential equations", "combinatorics", "harmonic analysis", "additive number theory"], certainty: 1.0, cites: [{source: S1, locator: "opening (Fields Medal citation)"}, {source: S2, locator: "Summary"}], how_known: "Fields Medal citation in both sources."}
  lasting_original_contributions:
    - {value: "Green–Tao theorem: the primes contain arbitrarily long arithmetic progressions (with Ben Green)", year: 2004, kind: "law or principle", lasting: "'This fantastic achievement' (S2); cited in the 2006 Fields Medal press release (S2)", certainty: 0.5, cites: [{source: S2, locator: "Fields Medal paragraphs"}, {source: S3, locator: "arXiv math/0404188"}], how_known: "MacTutor for lasting; date from arXiv (P30). Pure mathematics (P30), so not a scientist."}
    - {value: "Existence theorems for the nonlinear Schrödinger equation (with collaborators)", year: UNKNOWN, kind: "law or principle", lasting: "'established crucial existence theorems' (S1); 'giving the subject a whole new look' (S2)", certainty: 0.7, cites: [{source: S1, locator: "body"}, {source: S2, locator: "Schrödinger paragraph"}], how_known: "Both sources; undated in the sources read, so it sets no span (P12). Theorems about an equation used in physics; the coder reads this as mathematics, not a theory of a physical system (RQ-Y3)."}
    - {value: "Contributions to the Kakeya problem", year: UNKNOWN, kind: "body of work", lasting: "'a great resurgence of interest' (S2)", certainty: 0.7, cites: [{source: S2, locator: "Kakeya paragraph"}], how_known: "MacTutor; undated (P12)."}
  evidence_of_impact:
    - {value: "Fields Medal (2006)", kind: "honours in lifetime", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Summary; honours"}], how_known: "Both sources."}
    - {value: "Fellow of the Royal Society (2007); Crafoord Prize (2012); Breakthrough Prize in Mathematics (2014)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S2, locator: "honours paragraph"}], how_known: "MacTutor."}
  major_works:
    - {value: "Solving mathematical problems: A personal perspective", year: 1992, kind: book, certainty: 0.7, cites: [{source: S2, locator: "1989–1990 paragraph ('The first edition was published in 1992')"}], how_known: "MacTutor: written in 1990, at 15; first edition 1992 (batch Y audit, TA7)."}
  honours:
    - {value: "Salem Prize", year: 2000, certainty: 1.0, cites: [{source: S1, locator: "last paragraph"}, {source: S2, locator: "honours paragraph"}], how_known: "Both sources."}
    - {value: "Fields Medal", year: 2006, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "honours paragraph"}], how_known: "Both sources."}
  definition_fit: {value: "clearly meets", rationale: "'a supreme problem-solver whose spectacular work has had an impact across several mathematical areas' (Fields citation, quoted in S2).", certainty: 0.7, cites: [{source: S2, locator: "Fields Medal paragraphs"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated in the sources read (Britannica, MacTutor, Wikipedia Personal life)."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Father Billy Tao, a Chinese-born paediatrician; mother Grace, born in Hong Kong, with a degree in physics and mathematics; they emigrated to Australia in 1972", role: family, certainty: 0.7, cites: [{source: S2, locator: "opening of Biography"}], how_known: "MacTutor."}
  household_circumstances: {value: "Eldest of three brothers, all later PhDs", certainty: 0.7, cites: [{source: S2, locator: "opening of Biography"}], how_known: "MacTutor."}
  schooling:
    - {value: "Blackwood High School, Adelaide", stage: "grammar or secondary school", run_by: "state or municipal", years: "1983–1988", certainty: 0.5, cites: [{source: S2, locator: "Blackwood paragraph"}], how_known: "MacTutor gives the school and years; run_by is the coder's reading (an Adelaide public high school), so 0.5."}
    - {value: "Flinders University (B.Sc. Honours 1991; master's 1992)", stage: university, run_by: "state or municipal", years: "1989–1992", certainty: 0.7, cites: [{source: S2, locator: "Flinders paragraphs"}, {source: S1, locator: "body"}], how_known: "Both sources; classes there from age about 11 (S2)."}
    - {value: "Princeton University (PhD 1996)", stage: university, run_by: private, years: "1992–1996", certainty: 1.0, cites: [{source: S1, locator: "body"}, {source: S2, locator: "graduate school paragraphs"}], how_known: "Both sources."}
  early_mathematics: {value: "advanced mathematics", certainty: 0.7, cites: [{source: S2, locator: "Clements paragraph ('reading a hardback book with the title Calculus' at seven)"}], how_known: "MacTutor."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Garth Gaudry (Flinders University)", certainty: 0.7, cites: [{source: S2, locator: "Flinders paragraphs"}], how_known: "MacTutor."}
  languages_in_childhood: {value: ["English"], certainty: 0.5, cites: [{source: S2, locator: "text"}, {source: S8, locator: "Personal life (speaks Cantonese)"}], how_known: "Coder's reading for English home language; Wikipedia notes he speaks Cantonese but cannot write Chinese — childhood bilingualism not dated, so English kept at 0.5."}
  notable_events:
    - {value: "International Mathematical Olympiad medals from age ten", year: 1986, certainty: 0.5, cites: [{source: S2, locator: "Olympiad paragraph"}], how_known: "MacTutor: 'at the age of ten'; year the coder's."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "2004", certainty: 0.5, cites: [{source: S3, locator: "arXiv math/0404188"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing found; Lex and Quanta discuss math vs physics / mathematical reality, not science vs religion as creed."}
  primary_system: {value: UNKNOWN, how_known: "No own-voice system label. Rejected unsourced 'Quiet Faith' / religious-belief aggregator pages (no verifiable quotes). Blog S7 stays agnostic on a divine-lottery hypothesis as a Bayesian example, not a personal creed. Wikipedia Personal life silent on religion (S8)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Lead only: public silence on creed + blog epistemic agnosticism about a divine sign. Rejected for scoring: no own-voice suspension of judgment on God's existence (CODING_GUIDE / Hilbert AGNOS pattern)."}
    - {code: PLATO, reason: "Lead: Quanta 2024 — mathematical objects feel real; 'it helps to believe it's real' (S6). Rejected as primary_system: working metaphysics of math practice, not a scored religion/system code for this study; also P16 says math Platonism alone does not score B."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing found that places or denies a personal intervening God (P19). Lex 'I have faith' about a physics theory of everything is confidence in scientific progress, not religious faith (S5). Blog S7 does not state a creed. Unsourced web faith quotes rejected."}
    B_cause:
      value: 3
      basis: recorded_interview
      certainty: 0.5
      support: single
      cites: [{source: S5, locator: "Nature of reality / Theory of everything chapters (~00:47–01:08): Einstein comprehensibility; universality; laws of physics invariant"}]
      rationale: "Not a scientist (ruling Y3 / P30): PDE existence results do not give P35. Needs an explicit nature remark (P16). Lex Fridman #472 (S5): endorses Einstein that 'the most incomprehensible thing about the universe is that it is comprehensible'; explains the compressibility of the physical world by universality (simple laws / few parameters emerge; 'bell curve shows up everywhere in nature'); states that 'the laws of physics are translation invariant' (and rotation/time) in explaining Noether. Lawful order of nature, no stated no-exception claim (P40) → B 3 at 0.5, alternative 4 (P16 Hilbert addendum / RQ O2). Quanta S6 math Platonism alone would be BELOW under P16 and is not used to score B."
      how_known: "(interview) Lex Fridman Podcast #472 transcript (human-generated; published on lexfridman.com). After major-work span 2004 (P20) and P16 alt-4 rule → 0.5. Support single: one interview."
      alternatives:
        - {value: 4, note: "No stated exceptionless law (P40).", cites: [{source: S5, locator: "universality / laws of physics passages"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing found (P19)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing found (P19)."}
    E_scope: {value: UNKNOWN, how_known: "Lead: 'everywhere in nature' / invariant laws may bear on E; not scored this pass (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so P19 takes precedence over B 3 @0.5; mid_basin stays UNKNOWN (cannot apply P4)."}
  statements:
    - text: "Yeah, Einstein had a quote like that. 'The most incomprehensible thing about the universe is that it is comprehensible.' … There is actually some possible explanation for that. So there's this phenomenon in mathematics called universality. … [Y]ou just need to know is temperature and pressure and volume, and a few parameters, like five or six, and it models almost everything you need to know about these 10 to 23 or whatever particles. … [T]he central limit theorem that explains why the bell curve shows up everywhere in nature…"
      cites: [{source: S5, locator: "Nature of reality (~00:47:40–00:49:18)"}]
      date: "2025"
      context: "Lex Fridman Podcast #472 with Terence Tao; transcript published on lexfridman.com (posted 14 June 2025 per page)."
      axes: [B_cause]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Human-generated transcript; timestamps from the published page. Used for B lawful-order coding (P16 Hilbert path)."
    - text: "So the laws of physics are translation invariant. Like if I move 10 steps to the left, I experience the same laws of physics as if I was here, and that corresponds to conservation momentum. If I turn around by some angle, again, I experience the same laws of physics. This corresponds to the conservation of angular momentum. If I wait for 10 minutes, I still have the same laws of physics. … So there's time transition invariance. This corresponds to the law of the conservation of energy."
      cites: [{source: S5, locator: "General relativity / Noether (~01:05:17–01:06:00)"}]
      date: "2025"
      context: "Same Lex Fridman #472 interview; explaining Noether's theorem as a fact about physical law."
      axes: [B_cause]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Own-voice description of exception-tolerant but law-governed physics; no no-exception claim."
    - text: "When you do good mathematics, like, it's not just pushing symbols around. You do feel like there is some actual object that you're trying to understand, and all our equations we have are just sort of approximations of that, or shadows. … Whether — how real you want to call it. But I guess the point is that for the purpose of actually doing mathematics, it helps to believe it's real."
      cites: [{source: S6, locator: "platonic elephant / mathematical objects passage"}]
      date: "2024-02-01"
      context: "Quanta Magazine / Joy of Why interview with Steven Strogatz ('What Makes for Good Mathematics?')."
      axes: [B_cause]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Math Platonism about mathematical objects. Documented as rejected path for B under P16 (alone → BELOW_THRESHOLD); B score rests on Lex S5 nature remarks, not this."
  changes_over_life: []
  coder_notes: "Coder's call. Did not score A or primary from unsourced faith pages. Did not use P35 from NLS/Kakeya (ruling Y3). Did not score B from Quanta Platonism alone (P16). Lex 'faith' about TOE not used for A. Blog divine-lottery stays epistemic. Chart-moving NO. Figures not refreshed. No fallacy_catalog (Jason)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Chinese (father Chinese-born; mother from Hong Kong)", certainty: 0.7, cites: [{source: S2, locator: "opening of Biography"}, {source: S8, locator: "lead / Personal life"}], how_known: "MacTutor; Wikipedia."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "2004", certainty: 0.5, cites: [{source: S3, locator: "arXiv math/0404188"}, {source: S2, locator: "Fields Medal paragraphs"}], how_known: "Only one dated lasting contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 29, certainty: 0.5, cites: [{source: S1, locator: "Quick Facts"}], how_known: "2004 − 1975 = 29 (P30); 28 by month."}
  first_evidence_of_lio_type_views: {value: "2025: Lex Fridman #472 nature-of-reality / laws-of-physics remarks (B); Quanta 2024 math Platonism not used for B", year: 2025, certainty: 0.5, cites: [{source: S5, locator: "Nature of reality"}, {source: S6, locator: "platonic passage"}], how_known: "First scored B evidence is Lex 2025 (interview)."}
  lio_views_relative_to_major_work: {value: "after major work", certainty: 0.5, cites: [{source: S5, locator: "podcast"}], how_known: "Lex 2025 after span 2004 (P20)."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "primary_system UNKNOWN; A UNKNOWN; B evidence is after span."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "Professional proof culture and definition-to-consequence work across analysis and number theory (S2); a mathematical style, not a theology.", certainty: 0.5, cites: [{source: S2, locator: "Fields Medal paragraphs"}], how_known: "Coder's reading."}
  form_acquired: {value: "through the profession", certainty: 0.5, cites: [{source: S2, locator: "career / Fields paragraphs"}], how_known: "Coder's reading."}
  circle_present: {value: "unclear", rationale: "A UNKNOWN; no scored personal intervening God; nature-order B only.", certainty: 0.5, cites: [{source: S5, locator: "Nature of reality"}], how_known: "Lane B reading; not a finding."}
  reading: "B 3 @0.5 (interview) lawful nature (Lex); A UNKNOWN; unplotted."
  notes: "Lane B only. Chart-moving NO."

institutions:
  - {value: "University of California, Los Angeles", role: "faculty", years: "from 1996", kind: university, certainty: 1.0, cites: [{source: S1, locator: "body"}, {source: S2, locator: "career paragraphs"}], how_known: "Both sources."}
collaborators:
  - {value: "Ben Green", relation: collaborator, note: "Green–Tao theorem", certainty: 0.7, cites: [{source: S2, locator: "Fields Medal paragraphs"}], how_known: "MacTutor."}
  - {value: "Elias Stein", relation: teacher, note: "doctoral adviser at Princeton", certainty: 0.7, cites: [{source: S2, locator: "graduate school paragraph ('advised by Elias Stein')"}], how_known: "MacTutor."}

review:
  roster_status_reason: {value: "Provisional in v8 (F 4; four models).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 134"}], how_known: "Study roster."}
  controversies:
    - {value: "Whether Lex pedagogical remarks on universality / Noether count as a Hilbert-strength 'lawful order of nature' statement or only science-practice explanation — coded as B 3 @0.5 (P16 addendum); refusing would leave B UNKNOWN", certainty: 0.5, cites: [{source: S5, locator: "Nature of reality / Noether"}], how_known: "Coder's call."}
  data_quality_flags:
    - "B rests on one interview transcript (human-generated); support single; certainty 0.5 (P16/P20)."
    - "A/primary: public silence; unsourced faith pages rejected."
    - "Contribution year taken from arXiv, not from S1 or S2."
  open_questions:
    - "Settled by ruling Y3: not a scientist (no P35 from PDE)."
    - "Optional: further long-form interviews / blog posts that place or deny God (could firm A or AGNOS)."
    - "Optional: E from 'everywhere in nature' / invariant laws; not scored."
    - "Settled this pass: Lex nature remarks score B; Quanta Platonism alone does not."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Jeremy John Gray (Britannica)"
    citation: "Gray, Jeremy John. \"Terence Tao.\" Encyclopaedia Britannica (18 Oct 2026). https://www.britannica.com/biography/Terence-Tao. Read live 2026-10-19; create-pass kept."
    url: "https://www.britannica.com/biography/Terence-Tao"
    accessed: 2026-10-19
    reliability_note: "Signed short article."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, timing, institutions]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "J. J. O'Connor and E. F. Robertson (MacTutor)"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Terence Chi-Shen Tao.\" MacTutor History of Mathematics, University of St Andrews (last update December 2023). https://mathshistory.st-andrews.ac.uk/Biographies/Tao/"
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Tao/"
    accessed: 2026-10-19
    reliability_note: "Signed biography."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, collaborators]
  - id: S3
    type: primary
    kind: "journal article"
    author: "Ben Green and Terence Tao"
    citation: "Green, Ben, and Terence Tao. \"The primes contain arbitrarily long arithmetic progressions.\" arXiv:math/0404188 (submitted 8 April 2004); Annals of Mathematics 167 (2008): 481–547."
    url: "https://arxiv.org/abs/math/0404188"
    accessed: 2026-10-19
    reliability_note: "Abstract page read for the submission date; journal details from the Crossref record (doi:10.4007/annals.2008.167.481)."
    source_quality: "primary / own words"
    used_for: [basics, contribution, worldview, timing]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S5
    type: primary
    kind: other
    author: "Terence Tao (interviewed by Lex Fridman)"
    citation: "Fridman, Lex. \"Terence Tao: Hardest Problems in Mathematics, Physics & the Future of AI.\" Lex Fridman Podcast #472. Transcript: https://lexfridman.com/terence-tao-transcript/ (page dated 14 June 2025). Read 2026-10-24."
    url: "https://lexfridman.com/terence-tao-transcript/"
    accessed: 2026-10-24
    reliability_note: "Human-generated transcript of a recorded interview; Tao's first-person words. Used for B. 'Faith' about TOE not used for A."
    source_quality: "primary / own words"
    used_for: [worldview, timing, lane_b]
  - id: S6
    type: primary
    kind: other
    author: "Terence Tao (interviewed by Steven Strogatz)"
    citation: "Strogatz, Steven. \"What Makes for 'Good' Mathematics?\" Quanta Magazine / Joy of Why (1 February 2024). https://www.quantamagazine.org/what-makes-for-good-mathematics-20240201/. Read 2026-10-24."
    url: "https://www.quantamagazine.org/what-makes-for-good-mathematics-20240201/"
    accessed: 2026-10-24
    reliability_note: "Published interview transcript. Math Platonism about mathematical objects — documented; not used alone to score B (P16)."
    source_quality: "primary / own words"
    used_for: [worldview]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "Terence Tao"
    citation: "Tao, Terence. \"What are the odds?\" What's new (blog), 3 October 2022. https://terrytao.wordpress.com/2022/10/03/what-are-the-odds/. Read 2026-10-24."
    url: "https://terrytao.wordpress.com/2022/10/03/what-are-the-odds/"
    accessed: 2026-10-24
    reliability_note: "Own blog. Divine-being lottery hypothesis used as Bayesian example ('we (literally) stay agnostic'); not a personal creed statement for A/primary."
    source_quality: "primary / own words"
    used_for: [worldview]
  - id: S8
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Terence Tao.\" https://en.wikipedia.org/wiki/Terence_Tao. Read via API wikitext 2026-10-24."
    url: "https://en.wikipedia.org/wiki/Terence_Tao"
    accessed: 2026-10-24
    reliability_note: "Dual-bio second source (P50) for dates/places/native name; Personal life silent on religion."
    source_quality: "reference entry"
    used_for: [identity, basics, childhood, heritage, review]
---

# Terence Tao

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Terence Tao (born 1975), Australian-American mathematician, Fields Medal 2006 [S1; S2; S8]. Deepen D1: primary_system UNKNOWN; A UNKNOWN; B 3 @0.5 alt 4 (interview, Lex); mid_basin UNKNOWN. Not plotted. Chart-moving NO.

## Life and work

Adelaide, Flinders, Princeton, UCLA [S1; S2; S8]. Married to Laura Tao; two children; lives in Los Angeles [S8].

## Contribution and impact

Green–Tao theorem; nonlinear Schrödinger equations; Kakeya [S1; S2; S3].

## Childhood and education

Prodigy; Flinders University from age 14 [S2].

## Adult working worldview

No own-voice creed for A/primary [S5; S7; S8]. B 3 at 0.5 (interview): Lex remarks on a comprehensible universe, universality, and invariant laws of physics [S5]. Quanta math Platonism not used alone for B (P16) [S6]. Ruling Y3: not a scientist.

## Heritage (context only)

Chinese [S2; S8]. Religious heritage UNKNOWN.

## Timing

2004, at 29 [S1; S3]. B evidence 2025 after major work.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Professional geometric form [S2]; A UNKNOWN; B 3 @0.5 (interview); unplotted.

## Open questions

- RQ-Y3 settled (not a scientist).
- Optional: own-voice A/AGNOS; E from 'everywhere in nature'.

## Research log

- 2026-10-19: Read Britannica (Gray), MacTutor and the Green–Tao arXiv record; searched for statements on religion.
- 2026-10-24: Deepen D1. Lex Fridman #472 transcript; Quanta/Joy of Why 2024; blog 'What are the odds?'; Wikipedia dual bio. Rejected unsourced faith pages. Wrote drafts/deepen_tao-terence.md (untracked). No figures refresh. No fallacy_catalog.
