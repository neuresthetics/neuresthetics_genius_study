---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA3)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #179, F 3, rank 190). Hunt: in-span A corroboration; B only if P16 nature-order. No 1955–1960 religion/nature own words found. Post-span own-voice atheist line corroborated across independent pages (all still P20-capped at 0.5): Usenet saying 1992 (S5); Bush-vote essay Dec 2004 'I am an atheist' (S6); commentary Wed Mar 7 2007 'By the way I'm an atheist' + werewolf criterion (S6; Wikipedia's '2003' date is wrong — Henig NYT piece is Mar 2007); personal.html Dawkins 'come out' text present by Jan 2007 Wayback, absent Apr 2003–2006 captures (S3); Scientific Forms of the Religious Hypothesis 6 Apr 2008 'atheist rather than an agnostic' (S7). Memorial Church atheist speech remains undated secondary (S8 Wikipedia). Dual bio P50 Nilsson+Wikipedia. P47 source_quality on S1–S8. A support single→corroborated; A stays 4 @0.5 (P20); primary ATHE @0.5 alt AGNOS unchanged; B stays UNKNOWN (not scientist as listed P30/P33; RQ-AA3-1 open; no in-span P16; post-span 'I'm a Darwinian' / no-evidence-for-intervention is not scored as B). mid BELOW_THRESHOLD unchanged; not plotted. Chart-moving NO. No fallacy_catalog. No figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA3, order P32: F 3, rank 190). Sources: Nils Nilsson's National Academy of Sciences Biographical Memoir (2012, read in full) and Stanford Computer Science's memorial notice. Lasting work: the term and field 'artificial intelligence', named in the Dartmouth proposal 'submitted to the Rockefeller Foundation in August 1955' (formal submission, P30 #1), and LISP, 'the language of choice for AI research', whose 1960 paper 'established the theoretical foundations'; span 1955–1960, age 28. Own words: his Stanford home page, 'I mention that I am indeed an atheist ... the evidence on the god question is in about the same state as the evidence on the werewolf question' (also quoted by Nilsson). Undated; the reference to Dawkins's 'come out' campaign places it decades after the span, so P20 caps it at 0.5. primary_system ATHE 0.5 (written_profession), alt AGNOS (he disclaims proof); A 4 at 0.5, alt BELOW_THRESHOLD; not a scientist as listed (P30, P33: a term, a programming language and logic-based AI are not testable claims about nature), B UNKNOWN, and scientist status is ruling question RQ-AA3-1 (not result-changing unless B is scored); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD (P10). Not plotted. Draft, not reviewed."}

identity:
  id: mccarthy-john
  display_name: "John McCarthy"
  roster:
    canonical_name: "John McCarthy"
    rank: 190
    F: 3
    models: [Claude, DeepSeek, GPT]
    band: "core (3–4)"
    status: "core"
    field: "computer science"
    field_bucket: "computer science / AI"
  full_name: {value: "John McCarthy", certainty: 1.0, cites: [{source: S1, locator: "p. 3"}, {source: S8, locator: "infobox"}], how_known: "Nilsson + Wikipedia EN (P50 dual bio)."}
  native_name: {value: "John McCarthy", certainty: 0.7, cites: [{source: S1, locator: "p. 3"}], how_known: "Nilsson."}
  aliases:
    - {name: "John-McCarthy", kind: "roster alias"}

basics:
  birth:
    date: {value: "1927-09-04", certainty: 1.0, cites: [{source: S1, locator: "p. 3"}, {source: S8, locator: "infobox"}], how_known: "Nilsson + Wikipedia EN."}
    place: {value: "Boston, Massachusetts", modern_name: "Boston, Massachusetts, United States", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "p. 3"}, {source: S8, locator: "infobox"}], how_known: "Nilsson + Wikipedia EN."}
  death:
    date: {value: "2011-10-24", certainty: 1.0, cites: [{source: S1, locator: "p. 1"}, {source: S2, locator: "para. 1"}, {source: S8, locator: "infobox"}], how_known: "Nilsson; Stanford; Wikipedia EN."}
    place: {value: "Stanford, California", modern_name: "Stanford, California, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S8, locator: "Personal life / infobox"}], how_known: "Wikipedia: died at his home in Stanford."}
  first_lasting_contribution_year: {value: 1955, certainty: 0.7, cites: [{source: S1, locator: "p. 5"}, {source: S2, locator: "para. 1"}, {source: S8, locator: "Contributions"}], how_known: "Dartmouth proposal naming 'artificial intelligence' submitted to Rockefeller Foundation August 1955 (S1); Wikipedia agrees on 1955 coining / proposal (S8); formal submission (P30 #1)."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "p. 5"}], how_known: "1955–1960 (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "p. 3"}], how_known: "USA (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S2, locator: "para. 3"}, {source: S8, locator: "Academic career"}], how_known: "Dartmouth, MIT, Stanford."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "English papers; also spoke Russian (S8; heritage/context)."}
  occupations: {value: ["computer scientist", "mathematician"], certainty: 0.7, cites: [{source: S2, locator: "para. 1, 3"}, {source: S8, locator: "lead"}], how_known: "Stanford + Wikipedia."}

contribution:
  fields: {value: ["artificial intelligence", "computer science"], certainty: 0.7, cites: [{source: S2, locator: "para. 1"}, {source: S8, locator: "lead"}], how_known: "Stanford + Wikipedia."}
  lasting_original_contributions:
    - {value: "The name and research programme 'artificial intelligence' (Dartmouth proposal)", year: 1955, kind: "concept or term", lasting: "'one of the founders of artificial intelligence (AI), coining that name in 1955' (S2); the proposal's definition and the field 'to which McCarthy devoted his scientific career' (S1)", certainty: 0.7, cites: [{source: S1, locator: "p. 5"}, {source: S2, locator: "para. 1"}, {source: S8, locator: "Contributions"}], how_known: "Nilsson; Stanford; Wikipedia; submitted August 1955."}
    - {value: "LISP", year: 1960, kind: "invention", lasting: "'LISP soon became the language of choice for AI research' (S1); 'became the language of choice for programming AI systems' (S2)", certainty: 0.7, cites: [{source: S1, locator: "p. 7"}, {source: S2, locator: "para. 1"}, {source: S8, locator: "Contributions"}], how_known: "Designed from 1958; dated by the 1960 paper 'Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I' (publication, P30 #1)."}
  evidence_of_impact:
    - {value: "ACM Turing Award; National Medal of Science; Kyoto Prize", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S2, locator: "para. 4"}, {source: S8, locator: "Awards and honors"}], how_known: "Stanford + Wikipedia."}
  major_works:
    - {value: "Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I", year: 1960, kind: "paper or paper series", certainty: 0.7, cites: [{source: S1, locator: "p. 7"}, {source: S8, locator: "Major publications"}], how_known: "Nilsson + Wikipedia."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founder and namer of the field of AI; LISP (S1, S2, S8).", certainty: 0.7, cites: [{source: S2, locator: "para. 1"}], how_known: "Stanford."}

childhood:
  family_religion: {value: "Mixed Irish Catholic and Lithuanian Jewish immigrant parents; both active Communist Party members in the 1930s (secular/left household practice inferred, not a creed statement)", certainty: 0.5, cites: [{source: S1, locator: "p. 3"}, {source: S8, locator: "Early life and education"}], how_known: "Nilsson + Wikipedia. Heritage/political context — not a worldview code."}
  family_religious_practice: {value: UNKNOWN, how_known: "No household liturgy or practice detail beyond Communist Party activism (S1, S8)."}
  parents_and_household:
    - {value: "Father John Patrick McCarthy, Irish Catholic immigrant (Cromane, County Kerry); mother Ida Glatt McCarthy, Lithuanian Jewish immigrant; both Communist Party members in the 1930s; family relocated in the Depression; father later organizer for Amalgamated Clothing Workers in Los Angeles", role: "family", certainty: 0.7, cites: [{source: S1, locator: "p. 3"}, {source: S8, locator: "Early life and education"}], how_known: "Nilsson + Wikipedia."}
  household_circumstances: {value: "Frequent moves in the Great Depression until father found work in Los Angeles; parents encouraged learning and critical thinking", certainty: 0.5, cites: [{source: S8, locator: "Early life and education"}], how_known: "Wikipedia."}
  schooling:
    - {value: "Belmont High School, Los Angeles (graduated two years early)", stage: "grammar or secondary school", run_by: other, certainty: 0.7, cites: [{source: S8, locator: "Early life and education"}], how_known: "Wikipedia."}
    - {value: "Caltech, BS mathematics 1948 (suspended for missing PE; US Army service; readmitted); early math self-study from Caltech textbooks", stage: "university", run_by: other, certainty: 0.7, cites: [{source: S2, locator: "para. 3"}, {source: S8, locator: "Early life and education"}], how_known: "Stanford + Wikipedia."}
    - {value: "Princeton University, PhD mathematics 1951 (dissertation Projection operators and partial differential equations; advisor Donald C. Spencer)", stage: "university", run_by: other, certainty: 0.7, cites: [{source: S2, locator: "para. 3"}, {source: S8, locator: "Early life and education"}], how_known: "Stanford + Wikipedia."}
  early_mathematics: {value: "advanced mathematics", certainty: 0.7, cites: [{source: S8, locator: "Early life and education"}], how_known: "Wikipedia: taught himself college mathematics from Caltech textbooks as a teen; skipped first two years of math at Caltech."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure:
    - {value: "Read a translation of 100,000 Whys (Russian popular science for children) before high school", certainty: 0.5, cites: [{source: S8, locator: "Early life and education"}], how_known: "Wikipedia."}
  key_early_reading:
    - {value: "100,000 Whys (Russian popular science)", certainty: 0.5, cites: [{source: S8, locator: "Early life and education"}], how_known: "Wikipedia."}
  childhood_mentors: []
  languages_in_childhood: {value: ["English"], certainty: 0.5, cites: [{source: S8, locator: "Early life"}], how_known: "Inferred US upbringing; later fluent in Russian (S8)."}
  notable_events:
    - {value: "Attended a Caltech lecture by John von Neumann that inspired later AI interest", certainty: 0.5, cites: [{source: S8, locator: "Early life and education"}], how_known: "Wikipedia."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1955–1960", certainty: 0.7, cites: [{source: S1, locator: "p. 5, 7"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Post-span essays treat religion as a (superstitious) theory displaced by science in cases like lightning (S6, S7); not scored as an in-span relation statement (P20)."}
  primary_system:
    value: ATHE
    basis: written_profession
    certainty: 0.5
    cites: [{source: S3, locator: "closing paragraph (Dawkins come-out)"}, {source: S5, locator: "1992 werewolf saying"}, {source: S6, locator: "Wed Mar 7 2007; Dec 2004 Bush vote §11"}, {source: S7, locator: "closing atheist rather than agnostic"}, {source: S1, locator: "p. 21, n. 34"}]
    how_known: "Multiple post-span own-voice pages (P20 cap 0.5). Earliest dated line: 1992 Usenet saying (S5). No in-span (1955–1960) profession found."
    rationale: "Repeated written self-description as atheist (S3, S5, S6, S7). Alternative AGNOS: he disclaims proof that no gods exist and defines atheism by evidence-state comparison to werewolves (S3, S5, S6, S7)."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Coded at 0.5 (P20): repeated self-described atheist."}
    - {code: AGNOS, reason: "Alternative: disclaims proof; evidence-state criterion."}
  lio_axes:
    A_locus:
      value: 4
      basis: written_profession
      certainty: 0.5
      cites: [{source: S3, locator: "closing paragraph"}, {source: S5, locator: "1992 werewolf saying"}, {source: S6, locator: "Wed Mar 7 2007 atheist + werewolf"}, {source: S7, locator: "atheist rather than agnostic"}]
      support: corroborated
      how_known: "Four independent post-span own-voice pages agree on atheist + werewolf evidence criterion (S3, S5, S6, S7). All after the 1955–1960 span → P20 caps certainty at 0.5. No in-span corroboration found. P48 corroborated."
      rationale: "Evidence for gods like that for werewolves; self-labels atheist rather than agnostic (S3, S5, S6, S7): no God → A 4. Alternative BELOW_THRESHOLD: the claim is framed as an evidence-state judgment, not an explicit 'there is no God locus' sentence."
      alternatives:
        - {value: BELOW_THRESHOLD, note: "A claim about evidence-state, not a stated locus (S3, S5, S6, S7).", cites: [{source: S3, locator: "closing paragraph"}, {source: S5, locator: "1992 saying"}]}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist as listed (P30, P33): naming a field, a programming language and logic-based AI make no testable claims about nature. No in-span P16 nature-order statement. Post-span 'I'm a Darwinian' and 'I don't see any' evidence for creation/intervention (S6, S7) are not opened as B under standing deepen rule / P20. Ruling question RQ-AA3-1 remains open."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Post-span essays prefer scientific test over superstition (S6); not scored as in-span revelation-vs-observation (P20)."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "BELOW_THRESHOLD, not UNKNOWN: the A ≥ 3 branch reads A only (P10), and A 4 is scored only at 0.5."}
  statements:
    - text: >-
        Responding to Richard Dawkins's pestering his fellow atheists to "come out",
        I mention that I am indeed an atheist. To count oneself as an atheist one need
        not claim to have a proof that no gods exist. One need merely think that the
        evidence on the god question is in about the same state as the evidence on the
        werewolf question.
      cites: [{source: S3, locator: "closing paragraph"}]
      context: "Stanford personal home page 'About John McCarthy'; present in Jan 2007 Wayback capture; absent in Apr 2003–2006 captures; after the span (Dawkins Out Campaign)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Wayback-bracketed to ~2006–2007 addition. Same text quoted by Nilsson (S1, n. 34). P20."
    - text: >-
        An atheist doesn't have to be someone who thinks he has a proof that there can't
        be a god. He only has to be someone who believes that the evidence on the God
        question is at a similar level to the evidence on the werewolf question.
      cites: [{source: S5, locator: "1992 saying; gnuspostings=4017909"}]
      context: "Sayings page; dated jmc 1992 (Usenet). Earliest dated own-voice atheist criterion found this pass."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Post-span (P20). Independent of personal.html Dawkins paragraph."
    - text: >-
        By the way I'm an atheist. I don't claim to have a proof that God cannot exist.
        It's just that I consider the state of the evidence on the God question to be
        similar to that on the werewolf question.
      cites: [{source: S6, locator: "Wed Mar 7 11:12, 2007: Religion as a theory"}]
      context: "Commentary page entry reacting to Robin Marantz Henig, NYT Magazine (Darwin's God / evolutionary biology of belief), week of 4 Mar 2007."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Wikipedia cites this page as 'March 7, 2003' — date is 2007 (Henig article). P20."
    - text: >-
        By the way, I count myself as an atheist rather than an agnostic. My criterion
        for being an atheist is believing that the evidence on the god question is in a
        similar state to the evidence on the werewolf question.
      cites: [{source: S7, locator: "closing paragraph"}]
      context: "Scientific Forms of the Religious Hypothesis, dated 6 April 2008."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Explicit atheist-vs-agnostic self-sort. P20. Essay also says he sees no evidence for creation or intervention — not scored as B."
    - text: >-
        There are important issues on which I disagree with Bush. He wants to make the
        US more religious, whereas I am an atheist.
      cites: [{source: S6, locator: "Why I Voted for George Bush, 2004 Dec 6, §11"}]
      context: "Political commentary essay on the same commentary.html page."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Independent 'I am an atheist' line, Dec 2004. P20."
  changes_over_life: []
  coder_notes: "D1 2026-10-24: No in-span (1955–1960) A or B own words found. Post-span atheist cluster is dense and consistent (1992–2008) but P20 keeps 0.5. P48 A support→corroborated; still unplotted because B UNKNOWN. Do not force B from LISP/logic AI or from post-span Darwinian/ID essays. RQ-AA3-1 scientist status remains open (not result-changing unless B scored). Memorial Church speech undated — blocker. Chart-moving NO. No fallacy_catalog; figures/ untouched."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Irish (father) and Lithuanian Jewish (mother)", certainty: 0.7, cites: [{source: S1, locator: "p. 3"}, {source: S8, locator: "Early life and education"}], how_known: "Nilsson + Wikipedia."}
  religious_heritage_by_birth: {value: "Mixed: Irish Catholic father; Lithuanian Jewish mother", certainty: 0.7, cites: [{source: S1, locator: "p. 3"}, {source: S8, locator: "Early life and education"}], how_known: "Nilsson + Wikipedia. Heritage only — never a worldview code."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated in sources read."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated; Communist Party household (S1, S8) implies no conventional catechism recorded."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1955–1960", certainty: 0.7, cites: [{source: S1, locator: "p. 5, 7"}], how_known: "From the 1955 proposal to the 1960 LISP paper, the listed lasting works (P29, P30 #1)."}
  age_at_first_lasting_contribution: {value: 28, certainty: 0.7, cites: [{source: S1, locator: "p. 3, 5"}], how_known: "1955 − 1927 = 28 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: "1992", certainty: 0.5, cites: [{source: S5, locator: "1992 werewolf saying"}], how_known: "Earliest dated atheist own-voice found this pass (Usenet saying). Decades after span (P20 / P38)."}
  lio_views_relative_to_major_work: {value: "after major work", certainty: 0.5, cites: [{source: S5, locator: "1992"}, {source: S3, locator: "Dawkins paragraph ~2006–2007"}], how_known: "All dated atheist lines are after 1955–1960."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "No in-span profession; post-span evidence not projected backward (P20)."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Formal logic, recursive function theory, situation calculus (S1, S8).", certainty: 0.5, cites: [{source: S1, locator: "p. 7"}, {source: S8, locator: "Contributions"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable as a scored nature model."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "Logic/AI formalisms are tools for intelligence, not a Lane B cosmology of nature. Do not invent B from LISP or situation calculus."
  notes: "RQ-AA3-1: scientist-as-listed status for P30/B remains open."

institutions:
  - {value: "Stanford University", role: "professor; founder of the Stanford AI Laboratory", years: "1962–2011", kind: "university", certainty: 0.7, cites: [{source: S2, locator: "para. 3"}, {source: S8, locator: "Academic career"}], how_known: "Stanford + Wikipedia; end year his death."}
  - {value: "Massachusetts Institute of Technology", role: "faculty; co-founded the MIT AI Project", years: "1958–1962", kind: "university", certainty: 0.7, cites: [{source: S2, locator: "para. 3"}, {source: S8, locator: "Academic career"}], how_known: "Stanford + Wikipedia."}
  - {value: "Dartmouth College", role: "assistant professor; Dartmouth AI workshop organizer", years: "1955–1956", kind: "university", certainty: 0.7, cites: [{source: S1, locator: "p. 5"}, {source: S8, locator: "Academic career"}], how_known: "Nilsson + Wikipedia."}
collaborators:
  - {value: "Marvin Minsky", relation: "collaborator", note: "MIT AI Project; Dartmouth proposal co-author", certainty: 0.7, cites: [{source: S2, locator: "para. 3"}, {source: S8, locator: "Contributions"}], how_known: "Stanford + Wikipedia."}
  - {value: "Claude E. Shannon", relation: "collaborator", note: "Dartmouth AI proposal co-author", certainty: 0.7, cites: [{source: S8, locator: "Contributions"}], how_known: "Wikipedia."}
  - {value: "Nathaniel Rochester", relation: "collaborator", note: "IBM; Dartmouth proposal co-author", certainty: 0.7, cites: [{source: S1, locator: "p. 5"}, {source: S8, locator: "Contributions"}], how_known: "Nilsson + Wikipedia."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 190"}], how_known: "Study roster."}
  controversies:
    - {value: "RQ-AA3-1: whether McCarthy (and similar AI/CS founders) counts as a scientist under P30 for scoring B — left open; B stays UNKNOWN.", certainty: 0.5, cites: [{source: S1, locator: "career summary"}], how_known: "Create-time ruling question; deepen does not resolve it."}
  data_quality_flags:
    - "All atheist professions are post-span (earliest dated 1992); P20 caps A and primary at 0.5."
    - "No in-span (1955–1960) religion or nature own words found this pass."
    - "Wikipedia 'March 7, 2003' commentary date is incorrect (entry is Wed Mar 7 2007)."
  open_questions:
    - "RQ-AA3-1 scientist status for P30/B."
    - "Date and transcript of the Stanford Memorial Church AI speech (Wikipedia undated secondary)."
    - "Any 1950s–1960s letter, interview, or memo on religion (none found this pass)."

sources:
  - id: S1
    type: secondary
    kind: "book chapter"
    author: "Nils J. Nilsson"
    citation: "Nilsson, Nils J. 'John McCarthy, 1927–2011.' Biographical Memoirs, National Academy of Sciences (2012). https://ai.stanford.edu/~nilsson/John_McCarthy.pdf"
    url: "https://ai.stanford.edu/~nilsson/John_McCarthy.pdf"
    accessed: 2026-10-24
    reliability_note: "Scholarly memoir by a colleague, read in full at create; D1 re-used for bio + n. 34 quote of personal.html."
    source_quality: "scholarly edition or monograph"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, collaborators]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "Stanford University, Department of Computer Science"
    citation: "'Professor John McCarthy.' Stanford Computer Science, In Memoriam (October 2011). https://legacy.cs.stanford.edu/memoriam/professor-john-mccarthy"
    url: "https://legacy.cs.stanford.edu/memoriam/professor-john-mccarthy"
    accessed: 2026-10-19
    reliability_note: "Departmental memorial notice, read in full."
    source_quality: "other"
    used_for: [identity, basics, contribution, institutions, collaborators]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "John McCarthy"
    citation: "McCarthy, John. 'About John McCarthy.' Personal home page, Stanford University. https://www-formal.stanford.edu/jmc/personal.html (Wayback: atheist/Dawkins paragraph present by 2007-01; absent 2003–2006 captures)."
    url: "https://www-formal.stanford.edu/jmc/personal.html"
    accessed: 2026-10-24
    reliability_note: "His own page; live fetch failed 2026-10-24; text verified via Wayback 2007-09-19 capture. Undated page; Dawkins Out Campaign places addition ~2006–2007."
    source_quality: "primary / own words"
    used_for: [worldview]
  - id: S4
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [review]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "John McCarthy"
    citation: "McCarthy, John. 'The Sayings of John McCarthy.' Stanford formal site. Saying dated jmc 1992 (gnuspostings=4017909): atheist / werewolf evidence criterion. https://www-formal.stanford.edu/jmc/sayings.html"
    url: "https://www-formal.stanford.edu/jmc/sayings.html"
    accessed: 2026-10-24
    reliability_note: "Own sayings list; 1992 date on the werewolf atheist definition. Verified via Wayback 2007-10 capture when live fetch was empty."
    source_quality: "primary / own words"
    used_for: [worldview, timing]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "John McCarthy"
    citation: "McCarthy, John. 'Commentary on World, Us, and Scientific Affairs.' Stanford formal site. Includes 'Why I Voted for George Bush, 2004 Dec 6' (§11 'I am an atheist') and 'Wed Mar 7 11:12, 2007: Religion as a theory' ('By the way I'm an atheist' + werewolf). https://www-formal.stanford.edu/jmc/commentary.html"
    url: "https://www-formal.stanford.edu/jmc/commentary.html"
    accessed: 2026-10-24
    reliability_note: "Own commentary page; verified via Wayback 2013-10-04 (and 2008-03 for Mar 2007 entry). Wikipedia's 'March 7, 2003' is a misdate — Henig NYT Magazine piece is March 2007."
    source_quality: "primary / own words"
    used_for: [worldview]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "John McCarthy"
    citation: "McCarthy, John. 'Scientific Forms of the Religious Hypothesis.' 6 April 2008. https://www-formal.stanford.edu/jmc/religion.html (also jmc.stanford.edu/commentary/religion.html)"
    url: "https://www-formal.stanford.edu/jmc/religion.html"
    accessed: 2026-10-24
    reliability_note: "Own dated essay; atheist-rather-than-agnostic self-sort; no evidence seen for creation/intervention. Verified via Wayback when live fetch failed."
    source_quality: "primary / own words"
    used_for: [worldview]
  - id: S8
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "'John McCarthy (computer scientist).' Wikipedia (English). https://en.wikipedia.org/wiki/John_McCarthy_(computer_scientist)"
    url: "https://en.wikipedia.org/wiki/John_McCarthy_(computer_scientist)"
    accessed: 2026-10-24
    reliability_note: "P50 dual bio with S1. Early life, career, personal life (Memorial Church atheist claim — undated; cites personal.html and commentary). Death at Stanford home."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, heritage, institutions, collaborators, review]
---

## Summary

John McCarthy (1927–2011), computer scientist [S1, S2, S8]. Deepen D1: ATHE @0.5 (alt AGNOS); A 4 @0.5 corroborated post-span (P20); B UNKNOWN. Not plotted.

## Life and work

Boston; Los Angeles; Caltech; Princeton; Dartmouth; MIT; Stanford [S1, S2, S8]. Died Stanford 2011-10-24 [S8].

## Contribution and impact

Artificial intelligence (1955 Dartmouth proposal); LISP (1960) [S1, S2, S8].

## Childhood and education

Irish Catholic / Lithuanian Jewish immigrant parents; Communist Party household in the 1930s; Belmont High; Caltech BS; Princeton PhD [S1, S8].

## Adult working worldview

Repeated post-span own-voice atheist profession (1992 Usenet; 2004 Bush essay; 2007 commentary; ~2007 personal.html; 2008 religion essay) with werewolf evidence criterion [S3, S5, S6, S7]. No in-span (1955–1960) lines found. P20 keeps 0.5. B not opened.

## Heritage (context only)

Irish Catholic father; Lithuanian Jewish mother [S1, S8]. Context only.

## Timing

1955–1960, age 28 [S1]. First dated LIO-type evidence 1992 (after).

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Logic/AI formalisms ≠ nature cosmology. RQ-AA3-1 open.

## Open questions

- RQ-AA3-1 scientist status.
- Memorial Church speech date/transcript.
- Any 1950s–60s religion memo (none found).

## Research log

- 2026-10-24 (D1): Wikipedia EN (S8); Wayback personal.html (atheist para ~2007); sayings 1992 (S5); commentary 2004/2007 (S6); religion essay 2008 (S7). No in-span A/B. A support→corroborated; scores otherwise unchanged. Chart-moving NO. No fallacy_catalog; no figures/.
- 2026-10-19: Read Nilsson's memoir; Stanford notice; his home page.
