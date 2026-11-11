---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 6
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, fourth batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 20c_early. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (fourth batch, RUNBOOK §1 order). Basics from Britannica (Rouzé) and the Institute for Advanced Study's page. Worldview: no statement of his on God or religion was read in a checkable source. His Los Alamos farewell speech (2 November 1945, Atomic Heritage Foundation excerpts) states a faith in the value of science; his 1965 televised interview (interview) recalls the Bhagavad Gita line at Trinity. primary_system BELOW_THRESHOLD (ETHCUL candidate, stub; HINDU rejected). B 4 at 0.5 from his working science (P6); A, C, D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. His AIP oral-history interviews carry quotation limits and were not used. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 4 (two blind runs at b21655b). #164/#165 (run 2): '1965 interview' reworded as an interview recorded c. 1964 for NBC's The Decision to Drop the Bomb, broadcast 5 January 1965; new sources S6 (Paley Center catalogue record T79:0489: NBC, 5 January 1965, producer Fred Freed) and S7 (Wikiquote, a second pointer to the programme); statement date '1965' → '1965-01-05' with the recording date given as unknown (c. 1964); S4 citation, HINDU candidate reason, coder notes and body updated. The words of #165 stay as they are: they follow the audio, with no 'he' before 'takes on' (Wikiquote's 'he' is noted). Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02). Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs; BELOW_THRESHOLD vs UNKNOWN per P19; kind lists (P21: research institute, school stage and run_by, scholarly edition); basis inference_from_work for 0.5 inference from working science (P24). Full before → after list: reports/stage3_rulings_changes.csv. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Span alignment (P29, P30 and its addendum): timing.major_work_period checked, 1927–1945 unchanged; worldview.working_years 1925–1967 → 1927–1945, equal to the span (P30 addendum f); evidence for every headline value checked against the span; no value or certainty changed. Listed in reports/p30_span_alignment.csv. Not reviewed."}
    - {date: 2026-10-08, by: "Grok Bot", summary: "Lens audit of batch C (dd91009), ruling R1, logged as P35 (v8's pick): B_cause 4 → 3 at 0.5, alternative 4, because B rests on working science only. No other value changes; mid_basin unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #174/228, F 3, rank 185). Goals: own words on God/ethics for primary/A; do not force plot. Opened Bird and Sherwin, American Prometheus (2005) ch.1 extract / NPR excerpt and Harvard/Horgan letter quotation (S8); Joravsky NYRB 1980 review quoting Smith and Weiner Letters and Recollections (S9); widely reprinted 1932 Frank discipline letter from that edition (S10). Family Ethical Culture / no synagogue filled from Bird-Sherwin. 1923 satirical third-person Horgan letter (pre-span): lists science/Freud instead of God — not enough for A or ATHE (P29; third-person satire). 1932 Frank letter (in span): ethics/discipline more fundamental than any metaphysical ground (Gita through Spinoza) — ETHCUL programme lead, not a Society profession. primary stays BELOW_THRESHOLD (ETHCUL lead strengthened; ATHE lead from 1923 pre-span; HINDU rejected, P42/P8). A UNKNOWN → BELOW_THRESHOLD. B stays 3 @0.5 alt 4 (P35); support corroborated S1+S3. mid UNKNOWN → BELOW_THRESHOLD. Not plotted. Smith and Weiner IA unused (unclear provenance). AIP oral history unused (quotation limits). P47 on S1–S10. No fallacy_catalog. No figures/. Draft, not reviewed."}

identity:
  id: oppenheimer-j-robert
  display_name: "J. Robert Oppenheimer"
  roster:
    canonical_name: "J. Robert Oppenheimer"
    rank: 185
    F: 3
    models: [Gemini, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: physics
    field_bucket: physics
  full_name: {value: "J. Robert Oppenheimer", certainty: 1.0, cites: [{source: S1, locator: "heading"}, {source: S2, locator: "heading"}, {source: S8, locator: "ch. 1 (birth certificate Julius Robert Oppenheimer)"}], how_known: "Britannica, IAS, and Bird and Sherwin; he insisted the J stood for nothing."}
  native_name: {value: "J. Robert Oppenheimer (English)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "English name."}
  aliases:
    - {name: "J-Robert-Oppenheimer", kind: "roster alias"}
    - {name: "Oppenheimer-J-Robert", kind: "roster alias"}
    - {name: "Robert Oppenheimer", kind: "roster alias"}
    - {name: "Julius Robert Oppenheimer", kind: "birth name"}

basics:
  birth:
    date: {value: "1904-04-22", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S8, locator: "ch. 1"}], how_known: "Britannica and Bird and Sherwin."}
    place: {value: "New York City", modern_name: "New York, New York, USA", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S8, locator: "ch. 1"}], how_known: "Two sources."}
  death:
    date: {value: "1967-02-18", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "closing paragraphs"}], how_known: "Two sources agree."}
    place: {value: "Princeton, New Jersey", modern_name: "Princeton, New Jersey, USA", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1927, certainty: 0.7, cites: [{source: S2, locator: "Göttingen paragraph ('worked with Born on the structure of molecules')"}], how_known: "IAS page: the Born–Oppenheimer work of 1927, the year of his doctorate."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S2, locator: "Göttingen paragraph"}], how_known: "From first_lasting_contribution_year (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "USA is North America in data/reference/regions.csv (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'; Manhattan Project section"}], how_known: "Berkeley, Caltech, Los Alamos, Princeton."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "As the sources record it."}
  languages_of_work: {value: [English], certainty: 1.0, cites: [{source: S3, locator: "speech"}, {source: S2, locator: "Reith Lectures"}], how_known: "Speeches and lectures in English."}
  occupations: {value: ["theoretical physicist", "science administrator", "university professor"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "opening"}], how_known: "Two sources."}

contribution:
  era_bucket: 20c_early
  fields: {value: ["quantum theory", "nuclear and particle physics", "astrophysics"], certainty: 1.0, cites: [{source: S1, locator: "'Early life and education', paragraph 3"}, {source: S2, locator: "Berkeley paragraphs"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Born–Oppenheimer treatment of molecular structure, with Max Born", year: "1927", kind: method, lasting: "standard approximation in molecular physics", certainty: 0.7, cites: [{source: S2, locator: "Göttingen paragraph"}], how_known: "IAS page."}
    - {value: "Work on neutron stars and black holes", year: "1930s", kind: theory, lasting: "described as 'groundbreaking' by Britannica", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education', paragraph 3"}], how_known: "Britannica; years not given on the page."}
    - {value: "Direction of the Los Alamos Laboratory, which built the first atomic bombs (Trinity test, 16 July 1945)", year: "1943–1945", kind: institution, lasting: "nuclear weapons and the national-laboratory model", certainty: 0.7, cites: [{source: S1, locator: "opening; Manhattan Project section"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "Trained 'a whole generation of U.S. physicists'", kind: "institutional or technological lineage", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education', paragraph 3"}], how_known: "Britannica."}
  major_works:
    - {value: "Science and the Common Understanding (BBC Reith Lectures)", year: 1953, kind: "lecture series", certainty: 0.7, cites: [{source: S2, locator: "Reith Lectures sentence"}], how_known: "IAS page."}
  honours:
    - {value: "Enrico Fermi Award of the Atomic Energy Commission", year: 1963, certainty: 1.0, cites: [{source: S1, locator: "'Oppenheimer's legacy'"}, {source: S2, locator: "closing paragraphs"}], how_known: "Two sources."}
  definition_fit: {value: "arguable", rationale: "A leading theorist (Born–Oppenheimer, neutron stars and black holes) and teacher; his fame rests mostly on directing Los Alamos, an administrative role.", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Early life and education'"}], how_known: "Coder's judgement from Britannica."}

childhood:
  family_religion: {value: "Ethical Culture Society (secular humanist / non-creedal); ethnically Jewish, no synagogue", certainty: 0.7, cites: [{source: S8, locator: "ch. 1 (Ethical Culture Society; no synagogue)"}, {source: S2, locator: "education paragraph"}], how_known: "Bird and Sherwin: ethnically and culturally Jewish, belonged to no synagogue; shaped identity in the Ethical Culture Society. IAS: Ethical Culture School."}
  family_religious_practice: {value: "Ethical Culture Society affiliation (father a trustee); Sunday Society meetings in childhood; Ethical Culture School (deed not creed); no bar mitzvah or synagogue practice", certainty: 0.7, cites: [{source: S8, locator: "ch. 1 (Julius trustee from 1907; married by Felix Adler; school motto Deed, not Creed)"}], how_known: "Bird and Sherwin."}
  parents_and_household:
    - {value: "Julius Oppenheimer (1871–), German immigrant from Hanau; textile importer in New York (Rothfeld, Stern & Company); Ethical Culture Society trustee from 1907; died 1937, leaving Robert a fortune", role: father, certainty: 0.7, cites: [{source: S8, locator: "ch. 1"}, {source: S1, locator: "'Early life and education'; Manhattan Project section, paragraph 1"}], how_known: "Bird and Sherwin (name and Society role); Britannica (fortune)."}
    - {value: "Ella Friedman Oppenheimer (1869–), painter; Bavarian-Jewish family settled in Baltimore; married Julius 23 March 1903 by Felix Adler", role: mother, certainty: 0.7, cites: [{source: S8, locator: "ch. 1"}], how_known: "Bird and Sherwin."}
  household_circumstances: {value: "Wealthy New York family; Riverside Drive apartment; Bay Shore summer home", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}, {source: S8, locator: "ch. 1"}], how_known: "Britannica; Bird and Sherwin."}
  schooling:
    - {value: "Ethical Culture School of New York (entered 1911; graduated top of his class / valedictorian, 1921)", stage: "grammar or secondary school", years: "1911–1921", certainty: 0.7, cites: [{source: S2, locator: "education paragraph"}, {source: S8, locator: "ch. 1 (enrolled September 1911; graduated spring 1921)"}], how_known: "IAS; Bird and Sherwin."}
    - {value: "Harvard University: Latin, Greek, physics and chemistry, Eastern philosophy; summa cum laude 1925", stage: university, years: "1922–1925", certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "education paragraph"}], how_known: "Two sources; start year after illness delayed 1921 entry."}
    - {value: "Cavendish Laboratory, Cambridge; then University of Göttingen (PhD 1927 with Max Born)", stage: university, years: "1925–1927", certainty: 1.0, cites: [{source: S1, locator: "'Early life and education', paragraphs 1–2"}, {source: S2, locator: "Göttingen paragraph"}], how_known: "Two sources."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Childhood mineral collecting; New York Mineralogical Club lecture at age twelve; high-school physics and chemistry with Augustus Klock", certainty: 0.7, cites: [{source: S8, locator: "ch. 1"}], how_known: "Bird and Sherwin."}
  key_early_reading: []
  childhood_mentors:
    - {value: "Herbert Winslow Smith (English teacher, Ethical Culture School); later correspondent", certainty: 0.7, cites: [{source: S8, locator: "ch. 1"}, {source: S9, locator: "letters to Herbert W. Smith"}], how_known: "Bird and Sherwin; Joravsky on Smith and Weiner letters."}
    - {value: "John Lovejoy Elliott (ethics teacher, Ethical Culture School)", certainty: 0.7, cites: [{source: S8, locator: "ch. 1"}], how_known: "Bird and Sherwin."}
  languages_in_childhood: {value: [English], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S8, locator: "ch. 1 (German not spoken at home)"}], how_known: "Born in New York; Bird and Sherwin: German not spoken at home."}
  notable_events:
    - {value: "Seventeen-year-old birthday poem for Julius included the line 'and he swallowed Dr. Adler like morality compressed'", year: "1921", certainty: 0.7, cites: [{source: S8, locator: "ch. 1"}], how_known: "Bird and Sherwin; teasing of father's Ethical Culture commitment, not a creed."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1927–1945", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education' to Manhattan Project section"}, {source: S2, locator: "Göttingen paragraph"}], how_known: "Equal to timing.major_work_period (P30 addendum f; span check 2026-10-02). Was 1925–1967: Research from 1925 to death."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No statement by him on science and religion as such was read. The 1945 farewell speech speaks of 'our faith' in the value of science (S3), which is about the worth of knowledge, not about religion. The 1932 Frank letter treats religious and philosophical metaphysics as disparate grounds that do not settle why discipline is good (S10), which is ethics vs dogma, not science vs religion."}
  primary_system:
    value: BELOW_THRESHOLD
    cites: [{source: S8, locator: "ch. 1 (Ethical Culture upbringing)"}, {source: S10, locator: "1932 letter to Frank (discipline / metaphysics)"}, {source: S3, locator: "speech"}, {source: S4, locator: "clip transcript (interview)"}]
    how_known: "No adult first-person profession of a named system inside the span reaches 0.5 (P19). Ethical Culture schooling and family Society membership are upbringing (S8); the 1932 Frank letter adopts ethics-without-unifying-metaphysical-dogma language (S10) but never names Ethical Culture or Adler — ETHCUL lead, not a coded score. The 1923 Horgan letter's science-instead-of-God line is pre-span satire in the third person (S8; P29). HINDU remains rejected (literary Gita, P42/P8)."
    note: "Leads: ETHCUL (stub system file; Bird-Sherwin + 1932 letter); ATHE (1923 Horgan satire, pre-span). Would need adult Society membership or a clearer system profession, or an in-span ontological God denial, to code."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: ETHCUL, reason: "Leading candidate, not coded (BELOW_THRESHOLD): schooled at Ethical Culture School; father a Society trustee; married parents by Felix Adler (S8). In-span 1932 Frank letter: discipline/ethics more fundamental than any metaphysical ground from the Bhagavad Gita through Spinoza (S10) — programme-adjacent, not a Society profession. systems/ETHCUL.md: membership alone does not set axes; score from own statements. Stub system file (flag).", cites: [{source: S8, locator: "ch. 1"}, {source: S10, locator: "1932 letter to Frank"}, {source: S2, locator: "education paragraph"}]}
    - {code: ATHE, reason: "Lead only, not coded: autumn 1923 satirical third-person letter to Paul Horgan (Bird and Sherwin) has him answer 'but you believe in God don't you?' with belief in the second law of thermodynamics, Hamilton's Principle, Bertrand Russell and Freud (S8). Pre-span (P29), satirical, third-person — Simon/schoolboy pattern; not an adult written profession.", cites: [{source: S8, locator: "Harvard chapter (Horgan letter, autumn 1923)"}]}
    - {code: HINDU, reason: "Rejected: he studied Eastern philosophy at Harvard (S1) and in a television interview (interview; recorded c. 1964 for NBC's The Decision to Drop the Bomb, broadcast 5 January 1965, S6) recalled 'the line from the Hindu scripture, the Bhagavad-Gita' at the Trinity test (S4); a literary recollection, not a profession of Hindu belief (P42/P8). The 1932 letter lists the Gita among disparate metaphysics that fail to ground ethics (S10) — the same rejection of dogma, not Hindu profession. Stub system file (flag).", cites: [{source: S1, locator: "'Early life and education'"}, {source: S4, locator: "clip transcript (interview)"}, {source: S10, locator: "1932 letter to Frank"}]}
    - {code: SECHUM, reason: "Rejected as code: Bird and Sherwin describe Ethical Culture as progressive secular humanism (S8), but he had no humanist-movement public identity (systems/SECHUM.md use_when). Upbringing evidence stays under ETHCUL lead.", cites: [{source: S8, locator: "ch. 1"}]}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Sources on God were opened this pass (P19): the 1923 Horgan letter is on-point for locus but pre-span, satirical and third-person (S8; P29) — not enough for a score (Simon schoolboy pattern). The 1932 Frank letter discusses metaphysics as grounds for ethics, not whether God exists (S10; off-point for locus). Gita recollection scores nothing (P8). No in-span first-person 'there is no God' or theist profession. Named reading (not scored): A 4 at 0.5 if the 1923 line were taken as adult denial. Do not force plot."}
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      support: corroborated
      cites: [{source: S1, locator: "'Early life and education', paragraph 3"}, {source: S3, locator: "speech, 'organic necessity' paragraph"}]
      how_known: "Scientist (P30, P35): working physics (subatomic particles, neutron stars and black holes, S1) is lawful quantum and relativistic theory; farewell speech: the scientist's belief 'that it is good to find out how the world works' (S3). No miracle, petition or exemption in anything read. No statement of his own about law and exception, so 3 at 0.5 with 4 as named alternative, never 4 (P24, P35). S1+S3 → corroborated (P48)."
      rationale: "Scored on his account of nature (P6). P35 (v8's pick, 2026-10-08, lens audit of batch C ruling R1): B inferred only from a scientist's working science, with no statement of their own on law and exception, is B 3 at 0.5 with 4 as the named alternative."
      alternatives:
        - {value: 4, note: "Working science cannot tell lawful-with-exceptions from exceptionless (P35).", cites: [{source: S1, locator: "'Early life and education', paragraph 3"}, {source: S3, locator: "speech"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing on judgement, afterlife or reward and punishment in the sources read."}
    D_authority: {value: UNKNOWN, how_known: "No statement on revelation in the sources read. The farewell speech's 'faith' in science (S3) is about the value of knowledge, not observation against revelation. The 1932 letter's distrust of unifying metaphysics is a D lead only, not scored."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Nothing read addresses favour for a group in events. Working science bears on the first question (same laws everywhere) but not on favour for a group in events, so E stays BELOW_THRESHOLD; not scored from working science alone (P19)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied (§6 / P19)."}
  statements:
    - text: "If you are a scientist you believe that it is good to find out how the world works; that it is good to find out what the realities are; that it is good to turn over to mankind at large the greatest possible power to control the world and to deal with it according to its lights and its values."
      cites: [{source: S3, locator: "speech, 'organic necessity' paragraph"}]
      date: "1945-11-02"
      context: "Farewell speech to the Association of Los Alamos Scientists, on why the scientists built the bomb; AHF excerpts."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
    - text: "You put a hard question on the virtue of discipline. What you say is true: I do value it — and I think that you do too — more than for its earthly fruit, proficiency. I think that one can give only a metaphysical ground for this evaluation; but the variety of metaphysics which gave an answer to your question has been very great, the metaphysics themselves very disparate: the bhagavad gita, Ecclesiastes, the Stoa, the beginning of the Laws, Hugo of St Victor, St Thomas, John of the Cross, Spinoza. This very great disparity suggests that the fact that discipline is good for the soul is more fundamental than any of the grounds given for its goodness."
      cites: [{source: S10, locator: "1932 letter to Frank (as in Smith and Weiner 1980; text as widely reprinted)"}, {source: S9, locator: "Joravsky quotation and paraphrase of the same letter"}]
      date: "1932"
      context: "Letter to younger brother Frank Oppenheimer on the virtue of discipline (in span). Ethics held more fundamental than any single metaphysical or scriptural ground — programme-adjacent to Ethical Culture (deed/ethics over unifying creed), not a Hindu or theist profession."
      axes: []
      kind: "published letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Supports the ETHCUL lead at programme-adjacent reading; does not alone code ETHCUL (never names the Society; single published letter). Axes empty: about ethics/discipline, not A–E locus/cause."
    - text: "[Oppenheimer] has grown to be quite a man now you have no idea how Harvard has changed him. I am afraid it is not for the good of his soul to study so hard. He says the most terrible things. Only the other night I was arguing with him and I said but you believe in God don't you? And he said I believe in the second law of thermodynamics, in Hamilton’s Principle, in Bertrand Russell, and would you believe it Siegfried [sic] Freud."
      cites: [{source: S8, locator: "Harvard chapter (satirical letter to Paul Horgan, autumn 1923)"}]
      date: "1923"
      context: "Satirical third-person letter to friend Paul Horgan while at Harvard (Bird and Sherwin). Before the coded span (P29). Wording follows Bird and Sherwin's quotation."
      axes: [A_locus]
      kind: "published letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Pre-span; satirical; third-person self-characterization. On-point for locus but cannot score A alone (P29; Simon schoolboy pattern). Backs ATHE as a lead only."
    - text: "I remembered the line from the Hindu scripture, the Bhagavad-Gita. Vishnu is trying to persuade the Prince that he should do his duty and to impress him takes on his multi-armed form and says, “Now, I am become Death, the destroyer of worlds.” I suppose we all thought that one way or another."
      cites: [{source: S4, locator: "clip transcript (interview)"}, {source: S6, locator: "catalogue record (programme and broadcast date)"}, {source: S7, locator: "programme source note"}]
      date: "1965-01-05"
      context: "(interview) Television interview recalling the Trinity test, for the NBC White Paper The Decision to Drop the Bomb (producer Fred Freed), broadcast 5 January 1965 (S6; also S7). The date is the broadcast date; the recording date is not given in the sources read and is presumably 1964 (c. 1964), before the broadcast. Words follow the clip's audio and the Atomic Archive transcript (no 'he' before 'takes on', which S7 prints). Published broadcast, so quotation is permitted; scores nothing (P8: a passing recollection, not a statement of belief)."
      axes: []
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
  changes_over_life: []
  coder_notes: "ETHCUL and HINDU remain stub system files (flag). Deepen D1: Bird and Sherwin (S8) fill Ethical Culture family/school; 1923 Horgan satire (pre-span) and 1932 Frank discipline letter (in span, S10 via Smith and Weiner edition as reprinted / Joravsky S9) open ethics and God-talk without coding primary or A. The farewell speech's 'belief in the value of science' is a professional ethic of knowledge, not a metaphysics; no code fits it (SCIENT is Scientology, not scientism). Interview-based content (marked '(interview)'): only the NBC clip (S4), a published broadcast, used in one statement and in the HINDU rejection; it scores no axis or code. His AIP oral-history interviews carry AIP quotation limits and were not used or quoted. S3 is the Atomic Heritage Foundation's excerpt of the farewell speech and S4 the Atomic Archive's transcript of the film clip; both are unofficial web copies (§7), marked secondary quotation. A copy of Smith and Weiner, Letters and Recollections, seen on the Internet Archive has unclear provenance and was not used; the 1932 Frank letter is taken from the published Harvard edition as quoted by Joravsky (S9) and standard reprints (S10), not from that IA scan. changes_over_life is empty after research."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German-Jewish immigrant family (New York textile trade); ethnically and culturally Jewish", certainty: 0.7, cites: [{source: S8, locator: "ch. 1"}, {source: S1, locator: "'Early life and education'"}], how_known: "Bird and Sherwin; Britannica."}
  religious_heritage_by_birth: {value: "Jewish by ethnicity; Ethical Culture Society affiliation (no synagogue; no bar mitzvah)", certainty: 0.7, cites: [{source: S8, locator: "ch. 1"}], how_known: "Bird and Sherwin: belonged to no synagogue; Ethical Culture Society."}
  baptism_or_initiation: {value: "none recorded (no bar mitzvah; Ethical Culture, not synagogue initiation)", certainty: 0.7, cites: [{source: S8, locator: "ch. 1"}], how_known: "Bird and Sherwin / JTA digest of same: never went to a synagogue or had a bar mitzvah."}
  childhood_catechism: {value: "Ethical Culture School ethics curriculum (Education in Life Problems; 'Deed, not Creed'); John Lovejoy Elliott's ethics seminars", certainty: 0.7, cites: [{source: S8, locator: "ch. 1"}], how_known: "Bird and Sherwin."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1927–1945", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education' to Manhattan Project section"}, {source: S2, locator: "Göttingen paragraph"}], how_known: "Born–Oppenheimer work to Trinity; coder's reading."}
  age_at_first_lasting_contribution: {value: 23, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Göttingen paragraph"}], how_known: "Born April 1904; 1927 work."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No scored LIO-type view (axis at 3 or 4 from own statement) found (P27). The 1923 Horgan letter is God-talk before the span and does not score A; B rests on inference_from_work only."}
  lio_views_relative_to_major_work: {value: "unclear", rationale: "No scored LIO-type view. Pre-span 1923 Horgan satire and in-span 1932 Frank ethics letter do not open A or B.", certainty: 0.5, cites: [{source: S8, locator: "Harvard chapter"}, {source: S10, locator: "1932 letter to Frank"}], how_known: "Deepen D1."}
  worldview_during_major_work: {value: "Ethics-without-unifying-metaphysics lead (1932 Frank letter); working science; no coded primary or A", certainty: 0.5, cites: [{source: S10, locator: "1932 letter to Frank"}, {source: S3, locator: "speech"}], how_known: "In-span ethics letter and farewell speech; still BELOW_THRESHOLD for primary."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Nothing read on his method beyond theoretical physics in general.", certainty: 0.5, cites: [{source: S1, locator: "'Early life and education', paragraph 3"}], how_known: "No evidence."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "education paragraph"}], how_known: "Classics, chemistry and physics at Harvard; nothing on method."}
  circle_present: {value: "unclear", rationale: "No God-Nature statement read that scores; 1923 satire and 1932 ethics letter do not settle circle.", certainty: 0.5, cites: [{source: S3, locator: "speech"}, {source: S8, locator: "Horgan letter"}], how_known: "No evidence either way."}
  reading: "As belief, not finding: form unclear, circle unclear. The record does not test H1."
  notes: "Lane B only. Ethical Culture upbringing and literary Gita use are not H1 evidence."

institutions:
  - {value: "University of California, Berkeley, and California Institute of Technology", role: "professor of physics", years: "1929–1943", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Early life and education', paragraph 2"}], how_known: "Britannica; years are the coder's reading (after 1927 visits to Leiden and Zürich; to Los Alamos 1943)."}
  - {value: "Los Alamos Laboratory (Manhattan Project)", role: director, years: "1943–1945", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "opening; Manhattan Project section"}], how_known: "Britannica."}
  - {value: "General Advisory Committee of the Atomic Energy Commission", role: chairman, years: "1947–1952", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "Manhattan Project section, last paragraph"}], how_known: "Britannica."}
  - {value: "Institute for Advanced Study, Princeton", role: director, years: "1947–1966", kind: "research institute", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "opening"}], how_known: "Two sources."}
collaborators:
  - {value: "Max Born", roster_id: born-max, relation: teacher, note: "doctoral work at Göttingen; Born–Oppenheimer (1927)", certainty: 1.0, cites: [{source: S1, locator: "'Early life and education', paragraph 2"}, {source: S2, locator: "Göttingen paragraph"}], how_known: "Two sources."}
  - {value: "Niels Bohr", roster_id: bohr-niels, relation: "influenced by", note: "met and studied with him in Göttingen", certainty: 0.7, cites: [{source: S2, locator: "Göttingen paragraph"}, {source: S1, locator: "'Early life and education', paragraph 2"}], how_known: "Two sources (Britannica: 'met')."}
  - {value: "Ernest Rutherford", roster_id: rutherford-ernest, relation: other, note: "research at the Cavendish Laboratory, then under Rutherford's leadership (IAS: research assistant to J. J. Thomson)", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education', paragraph 1"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3: Gemini, GPT, Grok).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 185"}], how_known: "Study roster."}
  controversies:
    - {value: "1954 security hearing: clearance withdrawn after accusations of past communist associations and opposition to the hydrogen bomb", certainty: 1.0, cites: [{source: S1, locator: "'Security hearing and later years'"}, {source: S2, locator: "later paragraphs"}], how_known: "Two sources."}
  data_quality_flags:
    - "primary_system and A remain BELOW_THRESHOLD after deepen; ETHCUL stub; no in-span ontological God statement."
    - "S3 and S4 are unofficial web copies (§7)."
    - "Smith and Weiner Letters and Recollections: IA scan unused (unclear provenance); 1932 letter taken via published-edition quotations (S9/S10)."
    - "AIP oral-history interviews unused (quotation limits)."
  open_questions:
    - "Library copy of Smith and Weiner, Robert Oppenheimer: Letters and Recollections (1980), for page locators and any further religion letters beyond the 1932 Frank letter."
    - "Bird and Sherwin print pages for the Horgan letter (exact page) and any adult Ethical Culture membership claim."
    - "Any in-span first-person statement placing or denying God (letters, lectures) that would open A."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Michel Rouzé"
    citation: "Rouzé, Michel. \"J. Robert Oppenheimer.\" Encyclopaedia Britannica. https://www.britannica.com/biography/J-Robert-Oppenheimer."
    url: "https://www.britannica.com/biography/J-Robert-Oppenheimer"
    accessed: 2026-10-02
    source_quality: "reference entry"
    reliability_note: "Signed article. Sections cited by heading."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators, review]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "Institute for Advanced Study"
    citation: "Institute for Advanced Study. \"J. Robert Oppenheimer.\" https://www.ias.edu/oppenheimer-legacy."
    url: "https://www.ias.edu/oppenheimer-legacy"
    accessed: 2026-10-02
    source_quality: "other"
    reliability_note: "Institutional biography by his employer of 1947–66. Cited by paragraph description."
    used_for: [identity, basics, contribution, childhood, worldview, timing, lane_b, institutions, collaborators, review]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "J. Robert Oppenheimer"
    year: 1945
    citation: "Oppenheimer, J. Robert. Speech to the Association of Los Alamos Scientists, Los Alamos, 2 November 1945. Excerpts as 'Oppenheimer's Farewell Speech', Atomic Heritage Foundation / National Museum of Nuclear Science & History, https://ahf.nuclearmuseum.org/ahf/key-documents/oppenheimers-farewell-speech/."
    url: "https://ahf.nuclearmuseum.org/ahf/key-documents/oppenheimers-farewell-speech/"
    accessed: 2026-10-02
    source_quality: "unofficial web copy"
    reliability_note: "His own speech in a museum's excerpt; the copy-text is not named on the page, so it is treated as an unofficial web copy (§7). Cited by paragraph."
    used_for: [basics, worldview, lane_b]
  - id: S4
    type: primary
    kind: other
    author: "J. Robert Oppenheimer"
    year: 1965
    citation: "Oppenheimer, J. Robert. Interview recorded c. 1964 for the NBC White Paper The Decision to Drop the Bomb (producer Fred Freed), broadcast 5 January 1965 (programme and date: S6). Clip and transcript: \"J. Robert Oppenheimer 'Now I am become death...'\", Atomic Archive, https://www.atomicarchive.com/media/videos/oppenheimer.html."
    url: "https://www.atomicarchive.com/media/videos/oppenheimer.html"
    accessed: 2026-10-02
    source_quality: "unofficial web copy"
    reliability_note: "(interview) His own words in a published broadcast; transcript by the Atomic Archive (unofficial web copy). Used for one recollection only; scores nothing."
    used_for: [worldview]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    source_quality: "study roster"
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
  - id: S6
    type: secondary
    kind: "archive record"
    author: "Paley Center for Media"
    year: 1965
    citation: "Paley Center for Media, collection catalogue. \"White Paper: The Decision to Drop the Bomb {Tape 2 of 2} (TV)\", catalogue no. T79:0489. NBC, broadcast January 5, 1965, 9:00 PM; producer Fred Freed; J. Robert Oppenheimer among those credited. https://www.paleycenter.org/collection/item?item=T79%3A0489."
    url: "https://www.paleycenter.org/collection/item?item=T79%3A0489"
    accessed: 2026-10-02
    source_quality: "other"
    reliability_note: "Broadcast archive's catalogue record. Cited for the programme, network, producer and broadcast date of the film that contains S4's clip; it gives no recording date."
    used_for: [worldview]
  - id: S7
    type: tertiary
    kind: other
    author: "Wikiquote contributors"
    citation: "\"Robert Oppenheimer.\" Wikiquote. https://en.wikiquote.org/wiki/Robert_Oppenheimer (Trinity quotation and its source note)."
    url: "https://en.wikiquote.org/wiki/Robert_Oppenheimer"
    accessed: 2026-10-02
    source_quality: "other"
    reliability_note: "Open wiki. Cited only as a second pointer that the Trinity clip was 'first broadcast as part of the television documentary The Decision to Drop the Bomb (1965), produced by Fred Freed, NBC White Paper'. Not used for his words: it prints 'he takes on', and no 'he' is spoken in the clip (S4)."
    used_for: [worldview]
  - id: S8
    type: secondary
    kind: "scholarly book"
    author: "Kai Bird and Martin J. Sherwin"
    year: 2005
    citation: "Bird, Kai, and Martin J. Sherwin. American Prometheus: The Triumph and Tragedy of J. Robert Oppenheimer. New York: Knopf, 2005. Ch. 1 extract (NPR / Lovereading); Harvard-era Horgan letter quotation as printed in the biography."
    url: "https://www.npr.org/2005/05/11/4648060/oppenheimer-american-prometheus"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Pulitzer Prize biography. Used for Ethical Culture family/school (ch. 1) and the autumn 1923 satirical letter to Paul Horgan (Harvard chapter). Print page numbers for the Horgan letter not verified this pass."
    used_for: [identity, basics, childhood, worldview, heritage, timing, review]
  - id: S9
    type: secondary
    kind: "journal article"
    author: "David Joravsky"
    year: 1980
    citation: "Joravsky, David. \"Sin and the Scientist.\" The New York Review of Books, 17 July 1980. Review of Smith and Weiner, Robert Oppenheimer: Letters and Recollections (Harvard University Press, 1980). https://www.nybooks.com/articles/1980/07/17/sin-and-the-scientist/."
    url: "https://www.nybooks.com/articles/1980/07/17/sin-and-the-scientist/"
    accessed: 2026-10-24
    source_quality: "scholarly reconstruction"
    reliability_note: "Scholarly review quoting and paraphrasing the Smith and Weiner letter edition (far from mysticism; 1932 Frank discipline letter). Not a substitute for a library copy of the edition."
    used_for: [childhood, worldview]
  - id: S10
    type: primary
    kind: letter
    author: "J. Robert Oppenheimer"
    year: 1932
    citation: "Oppenheimer, J. Robert. Letter to Frank Oppenheimer, 1932, on discipline. In Alice Kimball Smith and Charles Weiner, eds., Robert Oppenheimer: Letters and Recollections (Harvard University Press, 1980). Text as widely reprinted from that edition (e.g. standard quotation beginning 'You put a hard question on the virtue of discipline'); corroborated by Joravsky's quotation/paraphrase (S9). Internet Archive scan of the edition unused (unclear provenance)."
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "His own published letter in a scholarly edition; this pass verifies wording from standard reprints of the Smith and Weiner text plus Joravsky (S9), not from a library page check or the unused IA scan. Page locator TODO when a library copy is read."
    used_for: [worldview, timing]
---

# J. Robert Oppenheimer

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

J. Robert Oppenheimer (1904–1967), American theoretical physicist, worked with Born on molecular structure, did early work on neutron stars and black holes, directed Los Alamos (1943–45) and then the Institute for Advanced Study (1947–66) [S1; S2]. Deepen D1 opened Bird and Sherwin [S8] and the 1932 Frank discipline letter [S10]. primary_system BELOW_THRESHOLD (ETHCUL lead strengthened; ATHE lead from 1923 pre-span satire; HINDU rejected). A BELOW_THRESHOLD; B 3 at 0.5 from the working science (alternative 4, P35; support corroborated); C, D UNKNOWN; E below threshold; mid_basin BELOW_THRESHOLD. Not plotted.

## Life and work

Ethical Culture School (1921), Harvard (1925), Cavendish, Göttingen (PhD 1927), Berkeley and Caltech, Los Alamos, IAS; security hearing 1954; Fermi Award 1963 [S1; S2; S8].

## Contribution and impact

Born–Oppenheimer (1927), neutron stars and black holes, a generation of American physicists, and the Los Alamos laboratory [S1; S2].

## Childhood and education

Son of Julius Oppenheimer and Ella Friedman; ethnically Jewish, no synagogue; Ethical Culture Society (father a trustee; married by Felix Adler); Ethical Culture School [S8]. Classics and Eastern philosophy at Harvard [S1; S2].

## Adult working worldview

Not coded from checkable sources. In 1932 he told Frank that discipline is good for the soul more fundamentally than any metaphysical ground (Bhagavad Gita through Spinoza) [S10] — ethics-without-unifying-dogma, an ETHCUL lead, not a profession. In 1945 he spoke of the scientist's belief "that it is good to find out how the world works" [S3]. A 1923 satirical letter answers "believe in God?" with thermodynamics and Russell [S8] — before the span, not scored for A. In a television interview (interview), recorded c. 1964 and broadcast in NBC's The Decision to Drop the Bomb on 5 January 1965 [S6], he recalled a line of the Bhagavad Gita at Trinity [S4]; that is a recollection, not a profession, and scores nothing.

## Heritage (context only)

German-Jewish immigrant family; Ethical Culture affiliation; no synagogue [S8]. Context only.

## Timing

First lasting contribution 1927, at 23 [S2]. No scored LIO-type view for timing.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form unclear; circle unclear.

## Open questions

- Library copy of Letters and Recollections (1980) for page locators and further religion letters.
- Bird and Sherwin print page for the Horgan letter; any adult Ethical Culture membership.
- In-span first-person statement placing or denying God.

## Research log

- 2026-10-02: Read Britannica (Rouzé), the IAS page, the AHF excerpts of the farewell speech, the AHF 1965 Groueff interview (Manhattan Project organisation only; nothing on religion) and the Atomic Archive's transcript of the NBC clip (broadcast 5 January 1965). Batch 4 lens audit: read the Paley Center catalogue record (S6) and Wikiquote (S7) for the programme and broadcast date. The AIP oral history was not used (quotation limits).
- 2026-10-24 (D1): Read Bird and Sherwin ch.1 extract (NPR / Lovereading) and the biography's quotation of the autumn 1923 Horgan letter (S8); Joravsky NYRB review of Smith and Weiner (S9); 1932 Frank discipline letter from that edition as widely reprinted (S10). Smith and Weiner IA unused. AIP oral history unused. No fallacy_catalog. No figures/.
