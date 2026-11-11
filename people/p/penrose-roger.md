---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 5
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch W)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to physics. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-25, by: "Grok Bot", summary: "Perpetual deepen: family_religion TODO→Quaker (paternal grandparents) @0.5 synced from heritage; baptism/catechism UNKNOWN. Chart-moving NO."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #126 / F4 rank 127). Goals: earlier own-voice on God/atheism; corroborate or lift B; keep honest BELOW/0.5 if not. Opened Tanner Lectures 1995 / LSAHM (S6); Road to Reality 2004 ch.1 (S7); Spectator Fink 2020 interview (S8); Wikipedia EN dual bio (S9, P50). BBC Radio 4 25 Sep 2010 religion quote still aggregator-only (Today archive page has no religion text; audio not transcribed) — unused for scoring. A stays BELOW_THRESHOLD (P20/P38): no explicit denial of God; Spectator 2020 'doesn't mean I'm an atheist' / agnostic; Brief History 1991 purpose remark secondary via Wikipedia. primary ATHE @0.5 alt AGNOS kept (W3); Spectator strengthens AGNOS alt. B 3 stays @0.5: basis inference_from_work→written_profession (S6 timeless mathematical laws / mathematical structure just there in nature; S7 entire physical world governed according to mathematical laws); P16 Hilbert / P35 keep 0.5 without exception/no-exception claim (alt 4); support corroborated. mid_basin BELOW_THRESHOLD. Chart-moving NO. P47 source_quality on S1–S9. No fallacy_catalog. No figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit fixes for batch W (gs_2584730_W run 1): ruling W3 (v8's call on the auditor's advice): ATHE at 0.5, alternative AGNOS, kept. (Note) the undated tilings cite P12 and P17 instead of P39. No scored value changes."}
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
  primary_domain: physics
  fields: {value: ["general relativity", "mathematical physics", "cosmology", "geometry (tilings)"], certainty: 0.7, cites: [{source: S3, locator: "body"}, {source: S2, locator: "body"}], how_known: "MacTutor and the Nobel biography."}
  lasting_original_contributions:
    - {value: "Singularity theorem: under the condition of a trapped surface, gravitational collapse must produce a space-time singularity; black hole formation is a robust prediction of general relativity", year: 1965, kind: "law or principle", lasting: "Nobel Prize in Physics 2020 'for the discovery that black hole formation is a robust prediction of the general theory of relativity' (S1); 'Roger's 1965 paper on this, earned his share of the 2020 Physics Nobel Prize' (S2)", certainty: 1.0, cites: [{source: S1, locator: "facts page (Prize motivation; Work)"}, {source: S2, locator: "singularity paragraphs"}, {source: S3, locator: "'In 1965, using topological methods'"}], how_known: "All three sources. A theorem about physical systems, so he is a scientist (P30)."}
    - {value: "Twistor theory", year: 1967, kind: theory, lasting: "De Morgan Medal citation (2004): 'His development of Twistor Theory has produced a beautiful and productive approach to the classical equations of mathematical physics' (quoted in S3); 'One of Penrose's major breakthroughs' (S3)", certainty: 0.7, cites: [{source: S2, locator: "spinor paragraph ('the theory of twistors, that Roger had introduced in 1967')"}, {source: S3, locator: "twistor paragraph; De Morgan citation"}], how_known: "Date from the Nobel biography; lasting from MacTutor's quotation of the LMS citation."}
    - {value: "Non-periodic tilings of the plane with two tiles (Penrose tilings)", kind: discovery, lasting: "De Morgan citation: 'His tilings of the plane underlie the newly discovered quasi-crystals' (quoted in S3)", certainty: 0.7, cites: [{source: S3, locator: "tilings paragraph; De Morgan citation"}], how_known: "MacTutor; undated in the sources read ('Further work over many years'), so it does not set the span: the item year is written as the sources give it and an undated item sets no first-lasting year (P12); the span runs from the earliest to the latest dated items (P17, P30 addendum)."}
  evidence_of_impact:
    - {value: "Nobel Prize in Physics 2020 (half share)", kind: "honours in lifetime", certainty: 1.0, cites: [{source: S1, locator: "facts page"}, {source: S3, locator: "honours list"}], how_known: "Nobel site."}
    - {value: "Wolf Prize in Physics (jointly with Stephen Hawking)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S3, locator: "honours paragraph"}], how_known: "MacTutor; year not given there."}
  major_works:
    - {value: "Spinors and Space-Time (with Wolfgang Rindler), 2 vols.", year: 1984, kind: book, certainty: 0.7, cites: [{source: S3, locator: "twistor paragraph (vol. 1 1984, vol. 2 'two years later')"}, {source: S2, locator: "spinor paragraph"}], how_known: "MacTutor dates 1984 and 1986; the Nobel biography also says 1984 and 1986."}
    - {value: "The Emperor's New Mind", year: 1989, kind: book, certainty: 1.0, cites: [{source: S3, locator: "popular books paragraph"}, {source: S4, locator: "question on consciousness"}], how_known: "MacTutor and the interview."}
    - {value: "The Large, the Small and the Human Mind (from 1995 Tanner Lectures)", year: 1997, kind: book, certainty: 0.7, cites: [{source: S6, locator: "title page / lecture 1"}], how_known: "Tanner Lectures delivered Cambridge Feb 1995; CUP book 1997 (S6)."}
    - {value: "The Road to Reality: A Complete Guide to the Laws of the Universe", year: 2004, kind: book, certainty: 1.0, cites: [{source: S7, locator: "title page"}, {source: S3, locator: "popular books paragraph"}], how_known: "Opened 2004 text (S7); MacTutor lists it."}
  honours:
    - {value: "Fellow of the Royal Society", year: 1972, certainty: 0.7, cites: [{source: S3, locator: "honours paragraph"}], how_known: "MacTutor."}
    - {value: "Knighthood", year: 1994, certainty: 0.7, cites: [{source: S3, locator: "honours paragraph"}], how_known: "MacTutor."}
    - {value: "Order of Merit", year: 2000, certainty: 0.7, cites: [{source: S3, locator: "honours paragraph"}], how_known: "MacTutor."}
    - {value: "De Morgan Medal (London Mathematical Society)", year: 2004, certainty: 0.7, cites: [{source: S3, locator: "honours paragraph"}], how_known: "MacTutor."}
    - {value: "Nobel Prize in Physics", year: 2020, certainty: 1.0, cites: [{source: S1, locator: "facts page"}, {source: S3, locator: "honours list"}], how_known: "Nobel site and MacTutor."}
  definition_fit: {value: "clearly meets", rationale: "Nobel-recognized theorem and twistor theory (S1, S3).", certainty: 0.7, cites: [{source: S1, locator: "facts page"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Quaker (paternal grandparents)", certainty: 0.5, cites: [{source: S2, locator: "opening"}], how_known: "Same as religious_heritage_by_birth; parents' practice not stated."}
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
  self_described_science_religion_relation: {value: "2022: 'I don't believe in any religion I've seen. So in that sense, I am an atheist' yet 'something going on that might resonate with a religious perspective'. 2020: 'a sense in which I would say I'm an agnostic' / 'doesn't mean I'm an atheist'; rejects Christianity as belief.", certainty: 0.5, cites: [{source: S4, locator: "question on inherent meaning in the universe"}, {source: S8, locator: "closing paragraphs on belief"}], how_known: "(interview) Two post-span interviews (P1 cap 0.5)."}
  primary_system:
    value: ATHE
    basis: recorded_interview
    certainty: 0.5
    cites: [{source: S4, locator: "question on inherent meaning in the universe"}, {source: S8, locator: "closing paragraphs on belief"}]
    rationale: "(interview) 2022 self-described: 'So in that sense, I am an atheist' (S4). Named alternative AGNOS strengthened by Spectator 2020: 'a sense in which I would say I'm an agnostic' and 'that doesn't mean I'm an atheist' (S8). Both post-span (P1 cap 0.5). ATHE's use_when asks for positive naturalism, which the qualifiers and purpose remarks weaken. Kept ATHE primary per ruling W3; AGNOS remains the named alternative."
    how_known: "(interview) Two interviews after the working years, so 0.5 (P1, P20). Ruling W3."
    alternatives:
      - {value: AGNOS, note: "Spectator 2020 own words reject the atheist label and prefer agnostic; 2022 hedges ('in that sense') and allows religious-resonance / purpose.", cites: [{source: S8, locator: "closing paragraphs on belief"}, {source: S4, locator: "question on inherent meaning in the universe"}]}
  secondary_system: {value: UNKNOWN, how_known: "One system (P29)."}
  candidate_codes_considered:
    - {code: ATHE, reason: "2022 self-label 'atheist' (qualified); kept primary at 0.5 (W3)."}
    - {code: AGNOS, reason: "Named alternative: 2020 Spectator prefers agnostic and rejects atheist label; 2022 hedges."}
    - {code: PLATO, reason: "Rejected as religious system: Road to Reality / Tanner mathematical Platonism is about mathematical objectivity and physical law, not a God/religion code (P21)."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "(interview) Disbelieves established religions / Christianity and uses a qualified 'atheist' label (S4, S8) but states no denial of God as such; Spectator 2020 explicitly: 'that doesn't mean I'm an atheist'; leaves room for purpose and 'something going on'. Not an explicit denial of a personal, intervening God (P20, P38; Feynman precedent). Named reading: 4 at 0.5 if the 2022 'atheist' label alone is taken as a denial."}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S6, locator: "lecture 1: timeless mathematical laws; mathematical structure just there in nature"}, {source: S7, locator: "§1.4: physical world governed according to mathematical laws"}, {source: S1, locator: "facts page (Work)"}]
      rationale: "Scored on his account of nature (P6). Written profession: Tanner 1995 — physical world as 'a structure precisely governed according to timeless mathematical laws'; 'the mathematical structure is just there in nature' (S6). Road to Reality 2004 — 'the entire physical world is depicted as being governed according to mathematical laws'; 'everything in the physical universe is indeed governed in completely precise detail by mathematical principles' (S7). Working science (S1) still shows GR lawfulness with no miracle read. No stated miracle, petition, or no-exception claim → B 3 at 0.5, alternative 4 (P16 Hilbert / P35), never 4."
      how_known: "Own published lectures/books (S6, S7). Independent source ids → corroborated (P48). Certainty held at 0.5: lawful-order remark without a stated no-exception or limited-exception claim (P16 Hilbert addendum / P35)."
      alternatives:
        - {value: 4, note: "P16 Hilbert / P35: lawful-order remark without a no-exception claim cannot score 4.", cites: [{source: S6, locator: "timeless mathematical laws"}, {source: S7, locator: "§1.4"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read on reward and punishment of persons (P19)."}
    D_authority: {value: UNKNOWN, how_known: "Working science and mathematical Platonism do not bear on D (P19); nothing read on revelation."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "(interview) Scored on the world's order (P7). Lead toward 4: consciousness, though 'beyond computable physics', depends on a physical 'theory that we don't know yet' (S4), so minds fall under physics. But it is one late remark about a future theory, with consciousness 'not an accident'; not enough for a score."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "P4 test: A_locus is BELOW_THRESHOLD and B_cause remains 0.5 under P16 Hilbert / P35, under the test's 0.7 bar. Deepen D1 did not darken B."}
  statements:
    - text: "They think about it in a rather different way, as a structure precisely governed according to timeless mathematical laws. Thus, they prefer to think of the physical world, more appropriately, as emerging out of the ('timeless') world of mathematics… The more we understand about the physical world, and the deeper we probe into the laws of nature, the more it seems as though the physical world almost evaporates and we are left only with mathematics… the mathematical structure is just there in nature, the theory really is out there in space — it has not been imposed upon nature by anyone."
      cites: [{source: S6, locator: "lecture 1 (Space-time and Cosmology), Platonic-world and GR-accuracy passages"}]
      date: "1995-02"
      context: "Tanner Lectures on Human Values, Cambridge, 13–15 February 1995; published as The Large, the Small and the Human Mind (CUP)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Own lecture text; post-span (P1). GR cited as accurate to about one part in 10^14."
    - text: "Thus, according to Fig. 1.3, the entire physical world is depicted as being governed according to mathematical laws… everything in the physical universe is indeed governed in completely precise detail by mathematical principles — perhaps by equations… or perhaps by some future mathematical notions fundamentally different from those which we would today label by the term 'equations'."
      cites: [{source: S7, locator: "§1.4 Three worlds and three deep mysteries"}]
      date: "2004"
      context: "The Road to Reality, chapter 1, on the relation of the Platonic mathematical world to the physical world."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Own published book; post-span (P1). Prefers the tight Fig. 1.3 picture while noting unease; no miracle/exception claim."
    - text: "There is a sense in which I would say I'm an agnostic. I certainly don't believe in Christianity. Maybe Jesus did a lot of the things described in the Bible, but certainly not all of them. But that doesn't mean I'm an atheist. Do I believe in something outside science? Well, it's a bit hard to know. What is science? Where are its boundaries?"
      cites: [{source: S8, locator: "closing paragraphs on belief"}]
      date: "2020-12-19"
      context: "Spectator interview (Thomas Fink) after the Nobel Prize; asked whether wonders of physics inspire belief beyond science."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Printed interview; his answers count as his words (P8)."
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
  coder_notes: "Deepen D1 (2026-10-24). B lifted to written_profession @0.5 corroborated via Tanner 1995 (S6) + Road to Reality 2004 (S7); P16 Hilbert / P35 hold certainty at 0.5. A stays BELOW (P20/P38): no God-denial; Spectator 2020 rejects atheist label. primary ATHE @0.5 alt AGNOS kept (W3). BBC Radio 4 25 Sep 2010 ('not a believer' / 'established religions'; aggregator also adds 'I would say I'm an atheist') — Today archive page has no religion text; audio not transcribed; unused for scoring (same blocker as creation). Wikipedia Brief History of Time film (1991) purpose remark seen only via Wikipedia citing a film-script site — secondary lead only, unused for A score. Humanists UK patronage via Wikipedia categories / search — not opened as primary. Emperor's New Mind (1989) not opened this pass (Road + Tanner suffice for B). RQ-W3 settled."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English; paternal Quaker family (grandfather James Doyle Penrose, grandmother of a Quaker banking family); maternal grandmother of a Jewish family from St Petersburg", certainty: 0.7, cites: [{source: S2, locator: "opening; Margaret paragraph"}], how_known: "Nobel biography."}
  religious_heritage_by_birth: {value: "Quaker (paternal grandparents)", certainty: 0.5, cites: [{source: S2, locator: "opening"}], how_known: "Grandparents only; his parents' practice is not stated."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Quaker heritage on grandparents' side; no baptism/initiation record for Roger opened."}
  childhood_catechism: {value: UNKNOWN, how_known: "No childhood catechism curriculum named."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1965–1967", certainty: 0.7, cites: [{source: S2, locator: "singularity and spinor paragraphs"}, {source: S3, locator: "1965 paragraph; twistor paragraph"}], how_known: "From the singularity theorem (1965) to twistor theory (1967) (P12, P30). The tilings are undated in the sources read, so they set neither end (P12, P17); alternative start 1964 (Nobel facts page)."}
  age_at_first_lasting_contribution: {value: 34, certainty: 0.7, cites: [{source: S1, locator: "facts page"}], how_known: "1965 − 1931; 33 or 34 by month of publication (P30)."}
  first_evidence_of_lio_type_views: {value: "1995 (Tanner Lectures): physical world precisely governed by timeless mathematical laws", year: 1995, certainty: 0.7, cites: [{source: S6, locator: "lecture 1"}], how_known: "First checkable own-voice LIO-type remark opened this pass (B-type written profession). Major-work span is 1965–1967, so this is after the span. 2020/2022 interviews are later A-type evidence."}
  lio_views_relative_to_major_work: {value: "after major work", rationale: "Tanner 1995 and Road to Reality 2004 are decades after major_work_period 1965–1967. No checkable LIO-type own voice inside the span was opened.", certainty: 0.7, cites: [{source: S6, locator: "lecture 1"}, {source: S7, locator: "§1.4"}], how_known: "Dates of S6/S7 vs timing.major_work_period."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "He 'tend[s] to think visually'; conformal and causal geometry of space-time; tilings.", certainty: 0.5, cites: [{source: S4, locator: "question on what first excited him"}, {source: S2, locator: "spinor paragraphs"}], how_known: "Coder's reading."}
  form_acquired: {value: "childhood or adolescence", certainty: 0.5, cites: [{source: S2, locator: "Canada paragraph (polyhedra with Lionel)"}], how_known: "Coder's reading."}
  circle_present: {value: "unclear", rationale: "Mathematical Platonism (Tanner / Road) and purpose remarks are not a circle claim (Deus sive Natura). Not scored from Platonism alone.", certainty: 0.5, cites: [{source: S6, locator: "lecture 1 Platonic world"}, {source: S4, locator: "question on inherent meaning"}], how_known: "Own words opened; still unclear as circle."}
  reading: "Visual-geometric physics; lawful mathematical nature (written); no established religion, open purpose / agnostic lean."
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
    - "Worldview A/primary still post-span interviews only (P1 cap 0.5); B now written_profession from post-span books/lectures."
    - "Return to England dated 1945 (MacTutor) vs 1949 (Nobel biography)."
    - "BBC Radio 4 25 Sep 2010 religion quote still without primary transcript."
  open_questions:
    - "Settled (ruling W3): ATHE at 0.5 with AGNOS the alternative; Spectator 2020 strengthens AGNOS alt but does not overturn W3 primary."
    - "BBC 2010 Today / Radio 4 audio transcript still needed if the aggregator 'I would say I'm an atheist' clause is to be scored."
    - "Emperor's New Mind (1989) and Cycles of Time (2010) not opened this pass (Road + Tanner suffice for B written_profession)."
    - "P16 Hilbert / P35: B stays 0.5 without exception/no-exception claim."

sources:
  - id: S1
    type: secondary
    kind: "institutional page"
    author: "Nobel Prize Outreach"
    citation: "\"Roger Penrose – Facts – 2020.\" NobelPrize.org. https://www.nobelprize.org/prizes/physics/2020/penrose/facts/"
    url: "https://www.nobelprize.org/prizes/physics/2020/penrose/facts/"
    accessed: 2026-10-19
    reliability_note: "Official prize record."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, worldview, timing, institutions]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "Nobel Prize Outreach (third-person biographical)"
    citation: "\"Roger Penrose – Biographical.\" NobelPrize.org (© The Nobel Foundation 2024). https://www.nobelprize.org/prizes/physics/2020/penrose/biographical/"
    url: "https://www.nobelprize.org/prizes/physics/2020/penrose/biographical/"
    accessed: 2026-10-19
    reliability_note: "Laureate biography written in the third person; unsigned (likely supplied by the laureate). Treated as secondary."
    source_quality: "reference entry"
    used_for: [basics, contribution, childhood, worldview, heritage, timing, lane_b, collaborators]
  - id: S3
    type: secondary
    kind: "institutional page"
    author: "J. J. O'Connor and E. F. Robertson (MacTutor)"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Roger Penrose.\" MacTutor History of Mathematics, University of St Andrews (last update September 2009). https://mathshistory.st-andrews.ac.uk/Biographies/Penrose/"
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Penrose/"
    accessed: 2026-10-19
    reliability_note: "Signed biography; honours list updated to 2020."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, timing, institutions, collaborators]
  - id: S4
    type: primary
    kind: other
    author: "Roger Penrose, with Michael Brooks"
    citation: "Brooks, Michael. \"Roger Penrose: 'Consciousness must be beyond computable physics'.\" New Scientist, 14 November 2022. https://www.newscientist.com/article/2346668-roger-penrose-consciousness-must-be-beyond-computable-physics/"
    url: "https://www.newscientist.com/article/2346668-roger-penrose-consciousness-must-be-beyond-computable-physics/"
    accessed: 2026-10-19
    reliability_note: "Printed Q&A interview; his answers count as his words (P8), the interviewer's framing does not. Long after the working years (P1 cap 0.5)."
    source_quality: "primary / own words"
    used_for: [childhood, worldview, timing, lane_b, collaborators, review, contribution]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]

  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Roger Penrose"
    citation: 'Penrose, Roger. "Space-time and Cosmology" (Tanner Lectures on Human Values), Cambridge University, 13–15 February 1995; published as The Large, the Small and the Human Mind (Cambridge University Press, 1997). https://tannerlectures.org/wp-content/uploads/2024/07/Penrose96.pdf'
    url: "https://tannerlectures.org/wp-content/uploads/2024/07/Penrose96.pdf"
    accessed: 2026-10-24
    reliability_note: "Own lecture text (primary). Post-span (P1). Used for B written_profession."
    source_quality: "primary / own words"
    used_for: [worldview, contribution, timing, lane_b]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "Roger Penrose"
    citation: "Penrose, Roger. The Road to Reality: A Complete Guide to the Laws of the Universe. London: Jonathan Cape, 2004. Chapter 1 (§1.4) opened via public PDF excerpt."
    url: "https://chaosbook.org/library/Penr04.pdf"
    accessed: 2026-10-24
    reliability_note: "Own published book (primary). Post-span (P1). Used for B written_profession."
    source_quality: "primary / own words"
    used_for: [worldview, contribution, timing, lane_b]
  - id: S8
    type: primary
    kind: other
    author: "Roger Penrose, with Thomas Fink"
    citation: 'Fink, Thomas. "A singular mind: Roger Penrose on his Nobel Prize." The Spectator, 19 December 2020. https://www.spectator.co.uk/article/a-singular-mind-roger-penrose-on-his-nobel-prize/'
    url: "https://www.spectator.co.uk/article/a-singular-mind-roger-penrose-on-his-nobel-prize/"
    accessed: 2026-10-24
    reliability_note: "Printed interview; his answers count as his words (P8). Post-span (P1 cap 0.5)."
    source_quality: "primary / own words"
    used_for: [worldview, timing]
  - id: S9
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: '"Roger Penrose." Wikipedia (English). https://en.wikipedia.org/wiki/Roger_Penrose'
    url: "https://en.wikipedia.org/wiki/Roger_Penrose"
    accessed: 2026-10-24
    reliability_note: "P50 dual bio: birth 1931-08-08 Colchester agrees with Nobel/MacTutor. Categories include English agnostics / English humanists; Brief History of Time film purpose quote cited to a film-script site — secondary only, unused for A score. BBC 2010 cite checked; archive page lacks religion text."
    source_quality: "reference entry"
    used_for: [basics, review]
---

# Roger Penrose

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Roger Penrose (b. 1931), English mathematical physicist; Nobel Prize in Physics 2020 for the singularity theorem [S1]. Deepen D1 opened Tanner 1995 [S6], Road to Reality 2004 [S7], and Spectator 2020 [S8]. primary_system ATHE (0.5, alt AGNOS, W3); A BELOW_THRESHOLD; B 3 (0.5 written_profession, alt 4); mid_basin BELOW_THRESHOLD. Not plotted.

## Life and work

UCL, Cambridge, Birkbeck, Oxford [S2, S3].

## Contribution and impact

Singularity theorem (1965), twistor theory (1967), tilings [S2, S3].

## Childhood and education

Scientific family; wartime in Philadelphia and Ontario [S2].

## Adult working worldview

Written profession on nature: the physical world is "precisely governed according to timeless mathematical laws" and "the mathematical structure is just there in nature" [S6]; "the entire physical world is depicted as being governed according to mathematical laws" [S7]. That lifts B to written_profession at 0.5 (P16 Hilbert / P35; alt 4). On God/religion: Spectator 2020 prefers agnostic and says that does not make him an atheist [S8]; New Scientist 2022 keeps a qualified "in that sense… atheist" with purpose / religious-resonance hedges [S4]. A stays BELOW_THRESHOLD (P20/P38). primary ATHE @0.5 alt AGNOS (W3).

## Heritage (context only)

Quaker paternal line [S2].

## Timing

1965–1967, from age 34 [S2, S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Visual geometry [S4].

## Open questions

- Settled W3: ATHE @0.5 alt AGNOS.
- BBC 2010 audio transcript still needed.
- ENM / Cycles of Time not opened this pass.

## Research log

- 2026-10-24: Deepen D1. Tanner Lectures 1995 [S6]; Road to Reality ch.1 [S7]; Spectator Fink 2020 [S8]; Wikipedia EN dual bio [S9, P50]. BBC 2010 Today archive lacks religion text. B → written_profession @0.5 corroborated; A/primary honest BELOW/0.5.
- 2026-10-19: Read the Nobel facts and biographical pages, MacTutor and the New Scientist interview.
