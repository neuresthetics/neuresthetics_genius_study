---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch W)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch W, order P32: F 4, rank 127). Basics from the Nobel Prize site (facts page and biographical) and MacTutor (O'Connor and Robertson). Worldview from one recorded interview (New Scientist, 14 November 2022, Michael Brooks), long after the working years (P1 cap 0.5). Scientist (P30). primary_system ATHE (0.5, alt AGNOS); A BELOW_THRESHOLD (named reading 4); B 3 (0.5, alt 4); C, D UNKNOWN; E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Span 1965–1967 (0.7). Not plotted. Draft, not reviewed."}

identity:
  id: penrose-roger
  display_name: "Roger Penrose"
  roster:
    canonical_name: "Roger Penrose"
    rank: 127
    F: 4
    models: [Claude, DeepSeek, Gemini, GPT]
    band: "core (3–4)"
    status: core
    field: mathematics-physics
    field_bucket: mathematics
  full_name: {value: "Roger Penrose", certainty: 0.7, cites: [{source: S1, locator: "facts page"}, {source: S2, locator: "opening"}], how_known: "Nobel site; knighted 1994 (S3)."}
  native_name: {value: "Roger Penrose", certainty: 0.7, cites: [{source: S1, locator: "facts page"}], how_known: "English."}
  aliases:
    - {name: "Penrose-Roger", kind: "roster alias"}
    - {name: "Roger-Penrose", kind: "roster alias"}
    - {name: "Sir Roger Penrose", kind: "title or honorific"}

basics:
  birth:
    date: {value: "1931-08-08", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "facts page (Born)"}, {source: S3, locator: "Quick Info"}], how_known: "Nobel site and MacTutor agree."}
    place: {value: "Colchester, Essex", modern_name: "Colchester, England, United Kingdom", polity_then: "United Kingdom", certainty: 1.0, cites: [{source: S1, locator: "facts page (Born)"}, {source: S3, locator: "Quick Info"}], how_known: "Both sources."}
  death:
    date: {value: UNKNOWN, how_known: "Living when read (2026-10-19); no death date in the sources read."}
    place: {value: UNKNOWN, how_known: "As above."}
  first_lasting_contribution_year: {value: 1965, certainty: 0.7, cites: [{source: S2, locator: "singularity paragraphs ('Roger's 1965 paper on this, earned his share of the 2020 Physics Nobel Prize')"}, {source: S3, locator: "'In 1965, using topological methods'"}], how_known: "The singularity theorem, published 1965. The Nobel facts page says 'In 1964, Roger Penrose proposed critical mathematical tools' (S1): alternative 1964 (work vs publication, P12)."}
  era_bucket: {value: "1950 on", certainty: 0.7, cites: [{source: S3, locator: "'In 1965'"}], how_known: "1965 (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 1.0, cites: [{source: S1, locator: "facts page"}, {source: S3, locator: "Quick Info"}], how_known: "United Kingdom (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 1.0, cites: [{source: S3, locator: "appointments (Birkbeck 1964–1973, Oxford 1973–1998)"}, {source: S1, locator: "affiliation at the time of the award"}], how_known: "London and Oxford."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S3, locator: "body"}], how_known: "Coder's reading."}
  occupations: {value: ["mathematician", "mathematical physicist", "Rouse Ball Professor of Mathematics, Oxford (1973–1998)", "author of popular books"], certainty: 0.7, cites: [{source: S3, locator: "Summary; appointments; popular books paragraph"}], how_known: "MacTutor."}

contribution:
  fields: {value: ["general relativity", "mathematical physics", "cosmology", "geometry (tilings)"], certainty: 0.7, cites: [{source: S3, locator: "body"}, {source: S2, locator: "body"}], how_known: "MacTutor and the Nobel biography."}
  lasting_original_contributions:
    - {value: "Singularity theorem: under the condition of a trapped surface, gravitational collapse must produce a space-time singularity; black hole formation is a robust prediction of general relativity", year: 1965, kind: "law or principle", lasting: "Nobel Prize in Physics 2020 'for the discovery that black hole formation is a robust prediction of the general theory of relativity' (S1); 'Roger's 1965 paper on this, earned his share of the 2020 Physics Nobel Prize' (S2)", certainty: 1.0, cites: [{source: S1, locator: "facts page (Prize motivation; Work)"}, {source: S2, locator: "singularity paragraphs"}, {source: S3, locator: "'In 1965, using topological methods'"}], how_known: "All three sources. A theorem about physical systems, so he is a scientist (P30)."}
    - {value: "Twistor theory", year: 1967, kind: theory, lasting: "De Morgan Medal citation (2004): 'His development of Twistor Theory has produced a beautiful and productive approach to the classical equations of mathematical physics' (quoted in S3); 'One of Penrose's major breakthroughs' (S3)", certainty: 0.7, cites: [{source: S2, locator: "spinor paragraph ('the theory of twistors, that Roger had introduced in 1967')"}, {source: S3, locator: "twistor paragraph; De Morgan citation"}], how_known: "Date from the Nobel biography; lasting from MacTutor's quotation of the LMS citation."}
    - {value: "Non-periodic tilings of the plane with two tiles (Penrose tilings)", kind: discovery, lasting: "De Morgan citation: 'His tilings of the plane underlie the newly discovered quasi-crystals' (quoted in S3)", certainty: 0.7, cites: [{source: S3, locator: "tilings paragraph; De Morgan citation"}], how_known: "MacTutor; undated in the sources read ('Further work over many years'), so it does not set the span (P39)."}
  evidence_of_impact:
    - {value: "Nobel Prize in Physics 2020 (half share)", kind: "honours in lifetime", certainty: 1.0, cites: [{source: S1, locator: "facts page"}, {source: S3, locator: "honours list"}], how_known: "Nobel site."}
    - {value: "Wolf Prize in Physics (jointly with Stephen Hawking)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S3, locator: "honours paragraph"}], how_known: "MacTutor; year not given there."}
  major_works:
    - {value: "Spinors and Space-Time (with Wolfgang Rindler), 2 vols.", year: 1984, kind: book, certainty: 0.7, cites: [{source: S3, locator: "twistor paragraph (vol. 1 1984, vol. 2 'two years later')"}, {source: S2, locator: "spinor paragraph"}], how_known: "MacTutor dates 1984 and 1986; the Nobel biography also says 1984 and 1986."}
    - {value: "The Emperor's New Mind", year: 1989, kind: book, certainty: 1.0, cites: [{source: S3, locator: "popular books paragraph"}, {source: S4, locator: "question on consciousness"}], how_known: "MacTutor and the interview."}
  honours:
    - {value: "Fellow of the Royal Society", year: 1972, certainty: 0.7, cites: [{source: S3, locator: "honours paragraph"}], how_known: "MacTutor."}
    - {value: "Knighthood", year: 1994, certainty: 0.7, cites: [{source: S3, locator: "honours paragraph"}], how_known: "MacTutor."}
    - {value: "Order of Merit", year: 2000, certainty: 0.7, cites: [{source: S3, locator: "honours paragraph"}], how_known: "MacTutor."}
    - {value: "De Morgan Medal (London Mathematical Society)", year: 2004, certainty: 0.7, cites: [{source: S3, locator: "honours paragraph"}], how_known: "MacTutor."}
    - {value: "Nobel Prize in Physics", year: 2020, certainty: 1.0, cites: [{source: S1, locator: "facts page"}, {source: S3, locator: "honours list"}], how_known: "Nobel site and MacTutor."}
  definition_fit: {value: "clearly meets", rationale: "Nobel-recognized theorem and twistor theory (S1, S3).", certainty: 0.7, cites: [{source: S1, locator: "facts page"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father: Lionel Sharples Penrose FRS, medical geneticist (Galton Chair at UCL)", certainty: 1.0, cites: [{source: S2, locator: "opening"}, {source: S3, locator: "opening"}], how_known: "Both sources."}
    - {value: "Mother: Margaret (Leathes) Penrose, medically trained", certainty: 1.0, cites: [{source: S2, locator: "Margaret paragraph"}, {source: S3, locator: "opening"}], how_known: "Both sources."}
    - {value: "Brothers Oliver (physicist) and Jonathan (chess grandmaster); sister Shirley (geneticist)", certainty: 0.7, cites: [{source: S2, locator: "family paragraphs"}], how_known: "Nobel biography."}
  household_circumstances: {value: "Scientific, puzzle- and geometry-loving family; wartime years in the USA and Canada (1939–1945)", certainty: 0.7, cites: [{source: S2, locator: "Canada paragraphs"}], how_known: "Nobel biography."}
  schooling:
    - {value: "A Quaker school in Philadelphia", stage: "elementary school", run_by: "religious body", years: "1939", certainty: 0.7, cites: [{source: S2, locator: "1939 paragraph ('the three boys attended a Quaker school')"}], how_known: "Nobel biography; run_by the coder's reading of 'Quaker school'."}
    - {value: "Schools in London, Ontario", stage: "elementary school", run_by: other, years: "1939–1945", certainty: 0.5, cites: [{source: S2, locator: "London, Ontario paragraphs"}], how_known: "Nobel biography; school names not given."}
    - {value: "University College School, Hampstead", stage: "grammar or secondary school", run_by: private, years: "from c. 1945", certainty: 0.5, cites: [{source: S2, locator: "UCS paragraphs ('at the age of 14')"}, {source: S3, locator: "1945 paragraph"}], how_known: "Entered at 14 (S2); MacTutor puts the return to England in 1945, the Nobel biography in 'the summer of 1949' (conflict, so 0.5)."}
    - {value: "University College London, BSc Mathematics, first class", stage: university, run_by: other, years: "1949–1952", certainty: 0.7, cites: [{source: S2, locator: "UCL paragraph"}], how_known: "Nobel biography ('completed, in 1952, after three years')."}
    - {value: "St John's College, Cambridge, PhD (algebraic geometry under W. V. D. Hodge)", stage: university, run_by: other, years: "1952–1957", certainty: 0.7, cites: [{source: S2, locator: "Cambridge paragraphs ('obtaining his PhD somewhat belatedly in 1957')"}], how_known: "Nobel biography; start year the coder's."}
  early_mathematics: {value: "advanced mathematics", certainty: 0.7, cites: [{source: S2, locator: "UCS paragraphs (calculus from his father; geometry)"}], how_known: "Nobel biography."}
  early_geometric_style_reasoning: {value: "Made regular polyhedra with his father; 'natural grasp of mathematics – geometry in particular'", certainty: 0.7, cites: [{source: S2, locator: "Canada and UCS paragraphs"}, {source: S4, locator: "question on what first excited him"}], how_known: "Nobel biography and his interview."}
  early_science_exposure:
    - {value: "Older brother Oliver read science books to him", certainty: 0.7, cites: [{source: S2, locator: "Canada paragraph"}], how_known: "Nobel biography."}
  key_early_reading: []
  childhood_mentors:
    - {value: "Lionel Penrose (father)", certainty: 0.7, cites: [{source: S2, locator: "UCS paragraphs"}, {source: S4, locator: "question on what first excited him"}], how_known: "Nobel biography and interview."}
  languages_in_childhood: {value: ["English"], certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "Coder's reading."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1965–1967", certainty: 0.7, cites: [{source: S2, locator: "singularity and spinor paragraphs"}, {source: S3, locator: "1965 paragraph"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "'I don't believe in any religion I've seen. So in that sense, I am an atheist. However, I would say that there is something going on that might resonate with a religious perspective' (2022)", certainty: 0.5, cites: [{source: S4, locator: "question on inherent meaning in the universe"}], how_known: "(interview) One recorded interview, 55 years after the working years (P1 cap 0.5)."}
  primary_system:
    value: ATHE
    basis: recorded_interview
    certainty: 0.5
    cites: [{source: S4, locator: "question on inherent meaning in the universe"}]
    rationale: "(interview) Self-described: 'I don't believe in any religion I've seen. So in that sense, I am an atheist.' Named alternative AGNOS: the label is qualified ('in that sense'), and he adds that the universe may in 'a certain sense' have 'a purpose' and that 'something going on' might 'resonate with a religious perspective'. ATHE's use_when asks for positive naturalism, which the qualifiers weaken (RQ-W3)."
    how_known: "(interview) One interview after the working years, so 0.5 (P1, P20)."
    alternatives:
      - {value: AGNOS, note: "Qualified label; 'something going on that might resonate with a religious perspective'.", cites: [{source: S4, locator: "question on inherent meaning in the universe"}]}
  secondary_system: {value: UNKNOWN, how_known: "One system (P29)."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Self-label 'atheist' (qualified); chosen at 0.5."}
    - {code: AGNOS, reason: "Named alternative: the qualifiers."}
    - {code: PLATO, reason: "Rejected: his mathematical Platonism (The Road to Reality, not read) is a view about mathematics, not a religious system; no statement of it read."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "(interview) He disbelieves 'any religion I've seen' but states no denial of God as such, and leaves room for 'a purpose' and 'something going on'. Not an explicit denial of a personal, intervening God (P20, P38; Feynman precedent). Named reading: 4 at 0.5 if 'atheist' is taken as a denial."}
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      cites: [{source: S1, locator: "facts page (Work)"}, {source: S4, locator: "question on consciousness and science"}]
      rationale: "Scored on his account of nature (P6). His working science (general relativity, the singularity theorem) plus the remark that consciousness is not 'beyond what science can discern ... it's just beyond current science'. No statement on law and exception: B 3 at 0.5, alternative 4, never 4 (P35)."
      how_known: "Working science; the 2022 remark is after the span."
      alternatives:
        - {value: 4, note: "P35.", cites: [{source: S1, locator: "facts page (Work)"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read on reward and punishment of persons (P19)."}
    D_authority: {value: UNKNOWN, how_known: "Working science does not bear on D (P19); nothing read on revelation."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "(interview) Scored on the world's order (P7). Lead toward 4: consciousness, though 'beyond computable physics', depends on a physical 'theory that we don't know yet', so minds fall under physics. But it is one late remark about a future theory, with consciousness 'not an accident'; not enough for a score."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A is BELOW_THRESHOLD and B only at 0.5; no branch of the P4 test is met."}
  statements:
    - text: "In a certain sense you might say that the universe has a purpose, but I'm not sure what the purpose is. I don't believe in any religion I've seen. So in that sense, I am an atheist. However, I would say that there is something going on that might resonate with a religious perspective."
      cites: [{source: S4, locator: "question on inherent meaning in the universe"}]
      date: "2022-11-14"
      context: "Asked whether decades of thinking about the universe and consciousness give him 'any sense of whether there is inherent meaning in the universe'."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "New Scientist's printed Q&A (edited interview); date is the publication date."
    - text: "No, it's just beyond current science. My claim is much worse, much more serious, much more outrageous than \"it's quantum mechanics in the brain\". It's not that consciousness depends on quantum mechanics, it's that it depends on where our current theories of quantum mechanics go wrong. It's to do with a theory that we don't know yet."
      cites: [{source: S4, locator: "question on consciousness and science"}]
      date: "2022-11-14"
      context: "Asked whether consciousness being beyond computation puts it 'beyond what science can discern'."
      axes: [B_cause, E_scope]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "As above."
  changes_over_life: []
  coder_notes: "Coder's call. All worldview evidence is one 2022 interview, 55 years after the span (P1 cap 0.5). A 2010 BBC Radio 4 remark ('I'm not a believer myself. I don't believe in established religions of any kind. I would say I'm an atheist') was seen only on aggregator pages and is not used. Humanists UK patronage also seen only in search (not used). RQ-W3: ATHE vs AGNOS for a qualified atheist label."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English; paternal Quaker family (grandfather James Doyle Penrose, grandmother of a Quaker banking family); maternal grandmother of a Jewish family from St Petersburg", certainty: 0.7, cites: [{source: S2, locator: "opening; Margaret paragraph"}], how_known: "Nobel biography."}
  religious_heritage_by_birth: {value: "Quaker (paternal grandparents)", certainty: 0.5, cites: [{source: S2, locator: "opening"}], how_known: "Grandparents only; his parents' practice is not stated."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1965–1967", certainty: 0.7, cites: [{source: S2, locator: "singularity and spinor paragraphs"}, {source: S3, locator: "1965 paragraph; twistor paragraph"}], how_known: "From the singularity theorem (1965) to twistor theory (1967) (P12, P30). The tilings are undated in the sources read (P39); alternative start 1964 (Nobel facts page)."}
  age_at_first_lasting_contribution: {value: 34, certainty: 0.7, cites: [{source: S1, locator: "facts page"}], how_known: "1965 − 1931; 33 or 34 by month of publication (P30)."}
  first_evidence_of_lio_type_views: {value: "2022 (interview): no religion, consciousness within a future physics", year: 2022, certainty: 0.5, cites: [{source: S4, locator: "question on inherent meaning"}], how_known: "(interview) Earliest source read; his books not read (P30 #7)."}
  lio_views_relative_to_major_work: {value: "after major work", certainty: 0.5, cites: [{source: S4, locator: "question on inherent meaning"}], how_known: "(interview) First evidence read is 55 years after the span."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "He 'tend[s] to think visually'; conformal and causal geometry of space-time; tilings.", certainty: 0.5, cites: [{source: S4, locator: "question on what first excited him"}, {source: S2, locator: "spinor paragraphs"}], how_known: "Coder's reading."}
  form_acquired: {value: "childhood or adolescence", certainty: 0.5, cites: [{source: S2, locator: "Canada paragraph (polyhedra with Lionel)"}], how_known: "Coder's reading."}
  circle_present: {value: "unclear", rationale: "A possible cosmic 'purpose' and consciousness 'not an accident', but no unity claim read.", certainty: 0.5, cites: [{source: S4, locator: "question on inherent meaning"}], how_known: "Coder's reading."}
  reading: "Visual-geometric physics; no religion, an open question of purpose."
  notes: ""

institutions:
  - {value: "Birkbeck College, London", role: "Reader (1964), Professor of Applied Mathematics (1966)", years: "1964–1973", kind: university, certainty: 0.7, cites: [{source: S3, locator: "appointments"}], how_known: "MacTutor."}
  - {value: "University of Oxford", role: "Rouse Ball Professor of Mathematics, later emeritus", years: "1973–1998", kind: university, certainty: 0.7, cites: [{source: S3, locator: "appointments"}, {source: S1, locator: "affiliation at the time of the award"}], how_known: "MacTutor; Nobel site."}
  - {value: "St John's College, Cambridge", role: "Research Fellow", years: "1957–1960", kind: university, certainty: 0.7, cites: [{source: S3, locator: "appointments ('a three year post')"}], how_known: "MacTutor; end year the coder's from 'three year post'."}
  - {value: "King's College London", role: "Research associate", years: "1961–1963", kind: university, certainty: 0.7, cites: [{source: S3, locator: "appointments"}], how_known: "MacTutor."}
collaborators:
  - {value: "Stephen Hawking", relation: collaborator, note: "Wolf Prize jointly; 'collaborated with Stephen Hawking to uncover the secrets of the big bang'", certainty: 0.7, cites: [{source: S3, locator: "honours paragraph"}, {source: S4, locator: "introduction"}], how_known: "MacTutor; New Scientist's introduction (the magazine's words)."}
  - {value: "Wolfgang Rindler", relation: collaborator, note: "Spinors and Space-Time", certainty: 0.7, cites: [{source: S2, locator: "spinor paragraph"}, {source: S3, locator: "twistor paragraph"}], how_known: "Both sources."}
  - {value: "Stuart Hameroff", relation: collaborator, note: "Orch OR theory of consciousness", certainty: 0.7, cites: [{source: S4, locator: "question on The Emperor's New Mind"}], how_known: "His interview."}
  - {value: "W. V. D. Hodge", relation: teacher, note: "PhD supervision at Cambridge", certainty: 0.7, cites: [{source: S2, locator: "Cambridge paragraphs"}], how_known: "Nobel biography."}
  - {value: "Lionel Penrose", relation: family, note: "father", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "Nobel biography."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 127"}], how_known: "Study roster."}
  controversies:
    - {value: "Conformal cyclic cosmology and Orch OR are minority views; 'very few' cosmologists take CCC seriously (his words)", certainty: 0.7, cites: [{source: S4, locator: "questions on CCC and Orch OR"}], how_known: "(interview) His own account."}
  data_quality_flags:
    - "All worldview evidence is one 2022 interview."
    - "Return to England dated 1945 (MacTutor) vs 1949 (Nobel biography)."
  open_questions:
    - "RQ-W3: ATHE vs AGNOS."
    - "Read The Road to Reality (2004) and The Emperor's New Mind (1989) for written statements on God and nature."

sources:
  - id: S1
    type: secondary
    kind: "institutional page"
    author: "Nobel Prize Outreach"
    citation: "\"Roger Penrose – Facts – 2020.\" NobelPrize.org. https://www.nobelprize.org/prizes/physics/2020/penrose/facts/"
    url: "https://www.nobelprize.org/prizes/physics/2020/penrose/facts/"
    accessed: 2026-10-19
    reliability_note: "Official prize record."
    used_for: [identity, basics, contribution, worldview, timing, institutions]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "Nobel Prize Outreach (third-person biographical)"
    citation: "\"Roger Penrose – Biographical.\" NobelPrize.org (© The Nobel Foundation 2024). https://www.nobelprize.org/prizes/physics/2020/penrose/biographical/"
    url: "https://www.nobelprize.org/prizes/physics/2020/penrose/biographical/"
    accessed: 2026-10-19
    reliability_note: "Laureate biography written in the third person; unsigned (likely supplied by the laureate). Treated as secondary."
    used_for: [basics, contribution, childhood, worldview, heritage, timing, lane_b, collaborators]
  - id: S3
    type: secondary
    kind: "institutional page"
    author: "J. J. O'Connor and E. F. Robertson (MacTutor)"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Roger Penrose.\" MacTutor History of Mathematics, University of St Andrews (last update September 2009). https://mathshistory.st-andrews.ac.uk/Biographies/Penrose/"
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Penrose/"
    accessed: 2026-10-19
    reliability_note: "Signed biography; honours list updated to 2020."
    used_for: [identity, basics, contribution, childhood, worldview, timing, institutions, collaborators]
  - id: S4
    type: primary
    kind: other
    author: "Roger Penrose, with Michael Brooks"
    citation: "Brooks, Michael. \"Roger Penrose: 'Consciousness must be beyond computable physics'.\" New Scientist, 14 November 2022. https://www.newscientist.com/article/2346668-roger-penrose-consciousness-must-be-beyond-computable-physics/"
    url: "https://www.newscientist.com/article/2346668-roger-penrose-consciousness-must-be-beyond-computable-physics/"
    accessed: 2026-10-19
    reliability_note: "Printed Q&A interview; his answers count as his words (P8), the interviewer's framing does not. Long after the working years (P1 cap 0.5)."
    used_for: [childhood, worldview, timing, lane_b, collaborators, review, contribution]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Roger Penrose

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Roger Penrose (b. 1931), English mathematical physicist; Nobel Prize in Physics 2020 for the singularity theorem [S1]. Draft (interview only): primary_system ATHE (0.5, alt AGNOS); A BELOW_THRESHOLD; B 3 (0.5, alt 4); mid_basin BELOW_THRESHOLD. Not plotted.

## Life and work

UCL, Cambridge, Birkbeck, Oxford [S2, S3].

## Contribution and impact

Singularity theorem (1965), twistor theory (1967), tilings [S2, S3].

## Childhood and education

Scientific family; wartime in Philadelphia and Ontario [S2].

## Adult working worldview

(Interview, 2022.) 'So in that sense, I am an atheist' [S4].

## Heritage (context only)

Quaker paternal line [S2].

## Timing

1965–1967, from age 34 [S2, S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Visual geometry [S4].

## Open questions

- RQ-W3.

## Research log

- 2026-10-19: Read the Nobel facts and biographical pages, MacTutor and the New Scientist interview.
