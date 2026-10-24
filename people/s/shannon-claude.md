---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch O)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-17
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-17, by: "Grok Bot", summary: "Record created (stage 3 batch O, order P32: F 4, rank 89). Basics from Britannica (George Markowsky, signed; body only). Worldview from Anthony Liversidge's interview (Omni, August 1987), read in the version printed in Shannon's Collected Papers (IEEE Press, 1993; PDF on gwern.net). primary_system ATHE (0.7); A 4 (0.7); B 3 (0.5, alt 4; P41); mid_basin false (0.7). Plotted (faded on B). Draft, not reviewed."}
    - {date: 2026-10-17, by: "Grok Bot", summary: "Batch O audit fixes (#8, #9): the 1987 interview is after the working years (1940–1948), so ATHE and A 4 drop to 0.5 (P20, Hawking precedent); mid_basin false → BELOW_THRESHOLD (A ≥ 3 branch needs 0.7). B cites P35 first (value unchanged). 1938 AIEE paper noted as a working-years lead. Still plotted (faded)."}
    - {date: 2026-10-18, by: "Grok Bot", summary: "Carry-over from the batch P audit (gs_08be43b_P run 1, note 9): B_cause basis corrected from recorded_interview to inference_from_work, since B 3 rests on his working science (P35) and the interview only agrees. Values unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #88, F4 rank 89). Needs: working-years/near-period A/ATHE; lift B if nature-order; P20 ceiling check. Re-verified Liversidge Collected Papers scan (S2, gwern PDF) — 'I am an atheist to begin with' / 'I see no God involved' / 'I don't happen to be a religious man'. Added Wikipedia EN (S4, P50 dual-bio): Methodist youth family; 'apolitical and an atheist' via Poundstone. Read Soni/Goodman A Mind at Play (S5): family active in Methodist church (p. 6); Norma Levor (later Barzman) 1939–40 courtship — she said she was a third-generation atheist; he replied 'How can you be anything else?' (p. 63; Norma Barzman interview 21 Dec 2014); biographer 'avowed atheist' vs Weaver (p. 84; index atheism 46, 84). Poundstone Fortune's Formula (S6) p. 18 atheist line footed to Liversidge 1987 and Timothy M. Johnson unpublished 1982 LOC interview paper (Johnson unread). 1938 AIEE PDF image-scan only — no extractable worldview text (technical switching). MTC/Weaver reprint: no Shannon nature-order / God statements. P20 corrected (Hawking D1): adult evidence counts for the working span absent sourced changes_over_life — none here; 1939–40 Norma reply is inside/at the start of the span. primary_system ATHE 0.5→0.7; A 4 0.5→0.7 support single→corroborated (S2+S5); B 3 @0.5 alt 4 stays (no P16 exceptionless order); support single→corroborated (S1+S2; P35/P41); mid_basin BELOW_THRESHOLD→false @0.7 (A≥3 branch, P10). P47 on S1–S6. Chart: faded hollow → faded filled. Chart-moving YES (fill). No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: shannon-claude
  display_name: "Claude Shannon"
  roster:
    canonical_name: "Claude Shannon"
    rank: 89
    F: 4
    models: [Claude, DeepSeek, Gemini, GPT]
    band: "core (3–4)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Claude Elwood Shannon", certainty: 1.0, cites: [{source: S2, locator: "profile, opening"}, {source: S4, locator: "lead / infobox"}], how_known: "Collected Papers profile and Wikipedia agree (P15)."}
  native_name: {value: UNKNOWN, how_known: "English."}
  aliases:
    - {name: "Claude-Shannon", kind: "roster alias"}
    - {name: "Shannon-Claude", kind: "roster alias"}

basics:
  birth:
    date: {value: "1916-04-30", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lead"}], how_known: "Britannica and Wikipedia agree."}
    place: {value: "Petoskey, Michigan, U.S.", modern_name: "Petoskey, Michigan, United States", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "Childhood"}], how_known: "Two sources; born in Petoskey hospital, family in Gaylord."}
  death:
    date: {value: "2001-02-24", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lead"}], how_known: "Two sources."}
    place: {value: "Medford, Massachusetts", modern_name: "Medford, Massachusetts, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1940, certainty: 0.7, cites: [{source: S1, locator: "master's thesis paragraph"}], how_known: "A Symbolic Analysis of Relay and Switching Circuits (1940), 'called one of the most significant master's theses of the 20th century' (S1). 1938 AIEE journal printing of the same thesis noted in open_questions; not moved this pass."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "master's thesis paragraph"}], how_known: "From 1940 (P2); 1948 gives the same bucket."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United States (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Bell Labs, MIT."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [English], certainty: 0.7, cites: [{source: S1, locator: "titles"}], how_known: "Britannica."}
  occupations: {value: ["mathematician", "electrical engineer", "professor"], certainty: 0.7, cites: [{source: S1, locator: "opening; MIT sentence"}], how_known: "Britannica."}

contribution:
  fields: {value: ["information theory", "switching theory", "cryptography"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Boolean algebra as the theory of relay and switching circuits (A Symbolic Analysis of Relay and Switching Circuits)", year: 1940, kind: theory, lasting: "'established the theoretical underpinnings of digital circuits' (S1)", certainty: 0.7, cites: [{source: S1, locator: "master's thesis paragraph"}], how_known: "Britannica. A theory about physical circuits, so he is counted a scientist (P30, coder's call)."}
    - {value: "Information theory ('A Mathematical Theory of Communication')", year: 1948, kind: theory, lasting: "'his framework and terminology are still used' (S1)", certainty: 0.7, cites: [{source: S1, locator: "1948 paragraph"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "Framework and terminology of information theory 'still used'; applied in cognition, biology, linguistics, psychology, economics and physics", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "1948 paragraphs"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Methodist (family active in the Methodist church in Gaylord during his youth)", certainty: 0.7, cites: [{source: S5, locator: "p. 6 (Claude Sr. and Mabel 'active in the Methodist church')"}, {source: S4, locator: "Childhood (citing Soni/Goodman p. 6)"}], how_known: "Soni/Goodman biography; Wikipedia agrees. Family practice, not his adult confession."}
  family_religious_practice: {value: "Active in the local Methodist church (parents)", certainty: 0.7, cites: [{source: S5, locator: "p. 6"}], how_known: "Soni/Goodman."}
  parents_and_household:
    - {value: "Father Claude Elwood Shannon Sr. (1862–1934), businessman / probate judge in Gaylord; furniture and funeral business", name: "Claude Elwood Shannon Sr.", role: father, certainty: 0.7, cites: [{source: S4, locator: "Childhood"}, {source: S5, locator: "p. 6"}], how_known: "Wikipedia; Soni/Goodman."}
    - {value: "Mother Mabel Wolf Shannon (1880–1945), language teacher; principal of Gaylord High School", name: "Mabel Wolf Shannon", role: mother, certainty: 0.7, cites: [{source: S4, locator: "Childhood"}, {source: S1, locator: "opening"}], how_known: "Wikipedia; Britannica."}
  household_circumstances: {value: "Gaylord, Michigan small-town household; father a prominent local businessman", certainty: 0.7, cites: [{source: S5, locator: "pp. 5–6"}, {source: S4, locator: "Childhood"}], how_known: "Soni/Goodman; Wikipedia."}
  schooling:
    - {value: "Gaylord High School (graduated 1932)", stage: "grammar or secondary school", years: "–1932", certainty: 0.7, cites: [{source: S4, locator: "Childhood"}], how_known: "Wikipedia."}
    - {value: "University of Michigan (B.S. mathematics and electrical engineering, 1936); MIT (S.M., Ph.D., 1940)", stage: university, years: "–1940", certainty: 0.7, cites: [{source: S1, locator: "education paragraph"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Built models of planes, a radio-controlled boat, and a barbed-wire telegraph to a friend's house", certainty: 0.7, cites: [{source: S4, locator: "Childhood"}], how_known: "Wikipedia."}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [English], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United States."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1940–1948", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Information theory is not 'a substitute for belief in a God': 'I certainly would not!'", certainty: 0.7, cites: [{source: S2, locator: "interview, religion exchange"}], how_known: "(interview) His own words (P8)."}
  primary_system:
    value: ATHE
    basis: recorded_interview
    certainty: 0.7
    cites: [{source: S2, locator: "interview, Wiener question"}, {source: S5, locator: "p. 63 (Norma courtship reply, 1939–40)"}]
    rationale: "'I am an atheist to begin with. I believe in evolutionary theory and that we are basically machines, but a very complex type ... A natural device. I see no God involved or anything like that' (S2). Both halves of the ATHE label are stated: no God, and humans as natural devices. Near-period agree: when Norma Levor said she was a third-generation atheist (courtship 1939–40), he replied 'How can you be anything else?' (S5). No sourced change of view (changes_over_life empty)."
    how_known: "(interview) Own words in the 1987 Liversidge interview (P8), plus spouse recollection of a working-years reply (S5). P20: adult evidence counts for the span absent a sourced change; recorded_interview ceiling 0.7."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Self-described atheist; humans 'a natural device'; 1939–40 'How can you be anything else?'"}
    - {code: DETERM, reason: "'basically machines' is about humans, not a general determinism."}
  lio_axes:
    A_locus:
      value: 4
      basis: recorded_interview
      certainty: 0.7
      support: corroborated
      cites: [{source: S2, locator: "interview, Wiener question"}, {source: S5, locator: "p. 63 (Norma courtship reply)"}]
      rationale: "No God (P38): 'I am an atheist to begin with ... I see no God involved or anything like that'; 'I don't happen to be a religious man' (S2). Working-years agree via Norma recollection: 'How can you be anything else?' to her atheism (S5, p. 63)."
      how_known: "(interview) Own words (P8) at recorded_interview ceiling 0.7; P20 adult-evidence rule (Hawking D1 correction of Batch O's post-work 0.5 drop). Second independent trail: Soni/Goodman report of Norma's 2014 interview on 1939–40 courtship (reported speech supports, does not alone score). Two source ids → corroborated (P48)."
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      support: corroborated
      cites: [{source: S1, locator: "master's thesis / 1948 paragraphs (physical switching; information theory)"}, {source: S2, locator: "interview, Wiener question"}]
      rationale: "Account of nature (P6): scientist under P30 (switching theory is a theory about physical circuits; information theory). Working science gives B 3 at 0.5, alternative 4 (P35). Own interview words agree: humans 'basically machines', 'A natural device', 'no God involved', evolution accepted — they deny intervention in human nature but state no exceptionless order (P40), which gives the same B 3 at 0.5, alternative 4 (P41). MTC and 1938 AIEE yield no P16 nature-order / law-of-nature statement from Shannon."
      how_known: "Inference from his working science (P35), so the basis is inference_from_work; the 1987 interview words (P8, P41) only agree. Two source ids (S1+S2) → corroborated (P48). Certainty stays 0.5 (P35/P41 ceiling with named alt 4)."
      alternatives:
        - {value: 4, note: "P35/P41 alternative: no stated exceptionless law.", cites: [{source: S2, locator: "interview, Wiener question"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin:
    value: false
    certainty: 0.7
    cites: [{source: S2, locator: "interview, Wiener question"}, {source: S5, locator: "p. 63"}]
    how_known: "A 4 at 0.7 on the A ≥ 3 branch (P10); B is 3 but mid_basin on this branch reads A only. Certainty follows A (0.7)."
  statements:
    - text: "That's a heavily loaded question! Let me say this. I am an atheist to begin with. I believe in evolutionary theory and that we are basically machines, but a very complex type, far more so than any machine man has made yet. So in a way that's both a Yes and a No. We are kind of an extreme case of mechanical device - by mechanical I don't mean just metals are involved, of course, gears and so on. A natural device. I see no God involved or anything like that."
      cites: [{source: S2, locator: "interview, Wiener question"}]
      date: "1987"
      context: "Reply to whether he agrees with Norbert Wiener that there is no basic distinction between man and machine; Liversidge interview, Omni, August 1987, as printed in the Collected Papers (S2). Interview transcript dated 21 Aug 1986 in Shannon LOC papers (Poundstone)."
      axes: [A_locus, B_cause]
      kind: "recorded interview"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "S2 says the Omni text appeared 'in a slightly different form'; Wikiquote Omni wording ('I'm an atheist to begin with ... I see no God involved') agrees on the denial of God. Re-verified against gwern Collected Papers PDF this pass."
    - text: "I don't happen to be a religious man and I don't think it would help if I were! OMNI: You wouldn't want to say information theory is a substitute for belief in a God? Shannon: I certainly would not!"
      cites: [{source: S2, locator: "interview, religion exchange"}]
      date: "1987"
      context: "Same interview."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
    - text: "How can you be anything else?"
      cites: [{source: S5, locator: "p. 63"}]
      date: "1940"
      context: "Reply to Norma Levor (first wife; later Norma Barzman) when she said she was a third-generation atheist, during their MIT/Radcliffe courtship before the Jan 1940 wedding. Reported in Soni/Goodman from Norma Barzman interview, 21 Dec 2014 (reported speech)."
      axes: [A_locus]
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "P8: spouse interview is reported speech — supports A/ATHE already resting on S2; does not alone score. Places atheist stance at the start of the working years."
  changes_over_life: []
  coder_notes: "Deepen D1 2026-10-24. Batch O's 0.5 post-work cap on A/ATHE reversed under corrected P20 (adult evidence counts unless changes_over_life). 1938 AIEE 'A Symbolic Analysis of Relay and Switching Circuits' PDF is an image scan (no extractable text); title/venue confirm technical switching content — no worldview lead recovered. MTC has no Shannon God/nature-order statements (Weaver's devout contrast is Weaver's, not Shannon's). B stays P35/P41 at 0.5 with alt 4; no P16 lift. Chart fill moves hollow→filled because both A and B now cite ≥2 source ids; darkness stays faded (B @0.5)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "American (father New Jersey settlers; mother German immigrant family)", certainty: 0.7, cites: [{source: S4, locator: "Childhood"}], how_known: "Wikipedia."}
  religious_heritage_by_birth: {value: "Methodist family milieu (Gaylord)", certainty: 0.7, cites: [{source: S5, locator: "p. 6"}, {source: S4, locator: "Childhood"}], how_known: "Family church activity; not his adult label."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1940–1948", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "First to last listed lasting contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 24, certainty: 0.7, cites: [{source: S1, locator: "opening; 1940"}], how_known: "1940 − 1916 = 24 (P30)."}
  first_evidence_of_lio_type_views: {value: "1939–1940: 'How can you be anything else?' to Norma's atheism (reported); 1987: self-described atheist", year: 1940, certainty: 0.5, cites: [{source: S5, locator: "p. 63"}, {source: S2, locator: "interview"}, {source: S6, locator: "p. 18 (atheist self-description; note to Liversidge 1987 and Johnson 1982)"}], how_known: "Earliest dated trail is Norma recollection of courtship reply (reported speech, 0.5); own-words interview 1987 (P30 #7); Poundstone biographical agree (S6)."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.5, cites: [{source: S5, locator: "p. 63"}, {source: S2, locator: "interview"}], how_known: "Norma reply at the 1940 start of the span (reported); 1987 interview after 1948 agrees; no sourced change."}
  worldview_during_major_work: {value: "ATHE (supported by Norma 1939–40 reply; full self-label in 1987 interview)", certainty: 0.5, cites: [{source: S5, locator: "p. 63"}, {source: S2, locator: "interview"}], how_known: "Working-years trail is reported speech; scored axes still rest on the recorded interview under P20."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not read for this.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Not read."}
  circle_present: {value: "no", rationale: "'I see no God involved'.", certainty: 0.7, cites: [{source: S2, locator: "interview"}], how_known: "Coder's reading of the interview."}
  reading: "Atheist; humans as natural machines; no exceptionless nature-order statement scored for B 4."
  notes: ""

institutions:
  - {value: "Bell Telephone Laboratories", role: "mathematician (research)", years: "1941–1972", kind: "research institute", certainty: 0.7, cites: [{source: S1, locator: "Bell Labs sentences"}], how_known: "Britannica."}
  - {value: "Massachusetts Institute of Technology", role: "professor", years: "1956–1978", kind: university, certainty: 0.7, cites: [{source: S1, locator: "MIT sentence"}], how_known: "Britannica (visiting 1956, faculty 1958, emeritus 1978)."}
collaborators:
  - {value: "Vannevar Bush", relation: "mentor or employer", note: "differential analyzer at MIT", certainty: 0.7, cites: [{source: S1, locator: "education paragraph"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 89"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Interview read in the Collected Papers version; the Omni magazine text differs slightly (Wikiquote agrees on the atheist denial)."
    - "Norma 1939–40 reply is reported speech via 2014 interview (S5), not Shannon's own recorded words."
    - "Johnson 1982 LOC unpublished interview paper cited by Poundstone unread."
  open_questions:
    - "Whether first_lasting_contribution_year should move from 1940 to 1938 (AIEE journal printing of the switching thesis)."
    - "Timothy M. Johnson, 'Claude Elwood Shannon: Information Theorist,' 10 Feb 1982, Shannon papers LOC — unread (Poundstone n.18)."
    - "Omni August 1987 original magazine pages (IA item metadata present; full OCR fetch thin this pass) — Collected Papers wording re-verified."
sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "George Markowsky"
    citation: "Markowsky, George. \"Claude Shannon.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Claude-Shannon. Read in Wayback snapshot 20261011204843."
    url: "https://www.britannica.com/biography/Claude-Shannon"
    accessed: 2026-10-17
    source_quality: "reference entry"
    reliability_note: "Signed article. Body only; Top Questions not cited."
    used_for: [identity, basics, contribution, childhood, timing, institutions, collaborators, worldview]
  - id: S2
    type: primary
    kind: "scholarly edition"
    author: "Anthony Liversidge"
    citation: "Liversidge, Anthony. \"Profile of Claude Shannon.\" In Claude Elwood Shannon: Collected Papers, ed. N. J. A. Sloane and A. D. Wyner (New York: IEEE Press, 1993), pp. xix ff.; first in Omni, August 1987. PDF: https://gwern.net/doc/cs/algorithm/information/1987-liversidge.pdf"
    url: "https://gwern.net/doc/cs/algorithm/information/1987-liversidge.pdf"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Scan of the Collected Papers printing, re-read directly this pass; question-and-answer interview in his own words (P8). Omni magazine OCR not fully recovered; Wikiquote Omni wording agrees on the atheist denial."
    used_for: [identity, worldview, timing, lane_b]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-17
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [identity, review]
  - id: S4
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Claude Shannon.\" https://en.wikipedia.org/wiki/Claude_Shannon. Read 2026-10-24."
    url: "https://en.wikipedia.org/wiki/Claude_Shannon"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Dual bio with Britannica (P50). Childhood Methodist cite → Soni/Goodman p. 6; Personal life atheist cite → Poundstone p. 18. Used for identity/basics/childhood, not as a sole worldview scorer."
    used_for: [identity, basics, childhood, heritage, review]
  - id: S5
    type: secondary
    kind: "scholarly book"
    author: "Jimmy Soni; Rob Goodman"
    citation: "Soni, Jimmy, and Rob Goodman. A Mind at Play: How Claude Shannon Invented the Information Age. New York: Simon & Schuster, 2017. Methodist family p. 6; Norma courtship atheism exchange p. 63 (Norma Barzman interview, 21 Dec 2014); index 'atheism of' CS at 46, 84; Weaver contrast p. 84."
    url: "https://www.simonandschuster.com/books/A-Mind-at-Play/Jimmy-Soni/9781476766690"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Full biography PDF read this pass. Norma reply is reported speech from a 2014 author interview with the first wife (P8 support role). Biographer 'avowed atheist' vs Weaver is secondary characterization."
    used_for: [childhood, heritage, worldview, timing]
  - id: S6
    type: secondary
    kind: "scholarly book"
    author: "William Poundstone"
    citation: "Poundstone, William. Fortune's Formula: The Untold Story of the Scientific Betting System. New York: Hill and Wang / Farrar, Straus and Giroux, 2005, p. 18. Note: atheist claim footed to Liversidge 1987 and Timothy M. Johnson, 'Claude Elwood Shannon: Information Theorist,' 10 Feb 1982, Shannon papers, LOC (Johnson unread)."
    url: "https://us.macmillan.com/books/9780809045990/fortunesformula/"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "PDF read; p. 18 and endnote checked. Not used as a second A cite because the Liversidge foot overlaps S2; Johnson 1982 remains unread."
    used_for: [timing, review]
---

# Claude Shannon

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Claude Shannon (1916–2001), American mathematician and electrical engineer, founder of information theory [S1]. Draft (D1): primary_system ATHE (0.7, interview); A 4 at 0.7 corroborated (interview); B 3 at 0.5 corroborated (alt 4; P35); mid_basin false at 0.7. Plotted faded filled.

## Life and work

Michigan, MIT; Bell Labs 1941–72; MIT faculty from 1956 [S1]. Family active in the Methodist church in Gaylord during his youth [S5; S4].

## Contribution and impact

Switching-circuit theory (1940) and information theory (1948) [S1].

## Childhood and education

Gaylord High School (1932); University of Michigan; MIT [S1; S4]. Methodist family milieu [S5].

## Adult working worldview

'I am an atheist to begin with' / 'I see no God involved' (1987 interview) [S2]. Near the start of the working years, when Norma Levor said she was a third-generation atheist, he replied 'How can you be anything else?' (reported, S5). No exceptionless nature-order statement found for B 4; B stays 3 at 0.5 alt 4 (P35/P41) [S1; S2].

## Heritage (context only)

American; Methodist family heritage by birth [S4; S5]. Not an outcome and not a worldview code.

## Timing

First lasting contribution 1940, at 24 [S1]. First LIO-type trail 1939–40 (Norma reply, reported) [S5]; own-words interview 1987 [S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle [S2].

## Open questions

- Move first_lasting_contribution_year to 1938 (AIEE printing)?
- Johnson 1982 LOC interview paper (Poundstone n.18) unread.
- Omni August 1987 original magazine pages (Collected Papers wording re-verified).

## Research log

- 2026-10-17: Read Britannica (Markowsky, Wayback 20261011204843) and the Liversidge profile (Collected Papers scan) directly.
- 2026-10-24 (D1): Re-read Liversidge gwern PDF; Wikipedia EN; Soni/Goodman A Mind at Play; Poundstone Fortune's Formula p. 18 + note; 1938 AIEE image PDF (no text); MTC PDF (no Shannon worldview). P47/P48/P50. No fallacy_catalog.
