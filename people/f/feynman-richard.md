---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, fourth batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (fourth batch, RUNBOOK §1 order). Included by owner decision, borderline on the stage-2 date window (major work 1946–49; Jason, 2026-10-02). Basics from Britannica (Gleick), MacTutor and the Nobel biography. Worldview from his own talk 'The Relation of Science and Religion' (Caltech YMCA Lunch Forum, 2 May 1956), printed in Engineering and Science 19:9 (June 1956), pp. 20–23, read on Caltech's own site and checked on the page images. primary_system AGNOS at 0.7 (stub; ATHE named). B 4, D 2, E 4, all at 0.7; A, C BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 4 (two blind runs at b21655b). #59 (both runs): birth place 'New York City (Manhattan; ...)' at 1.0 → 'New York City' at 1.0; the borough is noted as contested (0.5), Far Rockaway, Queens, per Britannica and MacTutor's Quick Info, with Manhattan (implied by MacTutor's Biography, paragraph 2) as the alternative. MacTutor Biography locators renumbered to the page's visible paragraphs (paragraph 1 is the parents, 2 the Manhattan apartment, 3 the move to Far Rockaway). #63 / decision P13: the 1939 MIT thesis ('an original and enduring approach to calculating forces in molecules', Britannica) is now a listed contribution (0.7), so first_lasting_contribution_year 1939 (0.7) and age 21 rest on a listed item; values unchanged. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02). Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs; A_locus note (P20). Full before → after list: reports/stage3_rulings_changes.csv. Not reviewed."}

identity:
  id: feynman-richard
  display_name: "Richard Feynman"
  roster:
    canonical_name: "Richard Feynman"
    rank: 69
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: physics
    field_bucket: physics
  full_name: {value: "Richard Phillips Feynman", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts ('In full')"}, {source: S3, locator: "paragraph 1 ('Richard P. Feynman')"}], how_known: "Britannica gives the full name; the Nobel biography and the 1956 byline give 'Richard P.'."}
  native_name: {value: "Richard Feynman (English)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "English name."}
  aliases:
    - {name: "Feynman-Richard", kind: "roster alias"}
    - {name: "Richard-Feynman", kind: "roster alias"}
    - {name: "Richard P. Feynman", kind: other}

basics:
  birth:
    date: {value: "1918-05-11", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "paragraph 1"}], how_known: "Two sources agree."}
    place: {value: "New York City", modern_name: "New York, New York, USA", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "paragraph 1"}, {source: S2, locator: "Quick Info"}], how_known: "All three sources agree on New York City. The borough is not part of the coded value because the sources point different ways (see note). Was 'New York City (Manhattan; ...)' at 1.0 until the batch 4 lens audit (#59).", note: "Borough contested (0.5): Far Rockaway, Queens, is stated by Britannica (opening: 'Born in the Far Rockaway section of New York City') and MacTutor's Quick Info ('Far Rockaway, New York, USA'), the better-supported reading. MacTutor's Biography implies Manhattan (alternative).", alternatives: [{value: "New York City (Manhattan)", cites: [{source: S2, locator: "Biography, paragraph 2 ('moved into a Manhattan apartment and, in the following year, their first child Richard was born')"}], note: "Implied, not stated: the biography puts the parents in a Manhattan apartment the year before his birth, and (paragraph 3) says the family moved several times and settled in Far Rockaway when he was ten."}]}
  death:
    date: {value: "1988-02-15", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "closing note"}], how_known: "Two sources agree."}
    place: {value: "Los Angeles, California", modern_name: "Los Angeles, California, USA", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1939, certainty: 0.7, cites: [{source: S1, locator: "paragraph 3 ('his undergraduate thesis (1939) proposed an original and enduring approach')"}], how_known: "The MIT undergraduate thesis on forces in molecules, listed as a contribution because Britannica calls it 'original and enduring'; it is the earliest listed contribution (decision P13). His main work (QED) is 1946–49."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "paragraph 3"}], how_known: "From first_lasting_contribution_year (P2); the QED work (by 1948) is in the same bucket."}
  region_of_birth: {value: "North America", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "USA is North America in data/reference/regions.csv (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S3, locator: "paragraph 1"}], how_known: "Princeton, Los Alamos, Cornell, Caltech."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "As the sources record it."}
  languages_of_work: {value: [English], certainty: 1.0, cites: [{source: S4, locator: "p. 20"}, {source: S1, locator: "lectures paragraph"}], how_known: "American physicist; papers, lectures and books in English."}
  occupations: {value: ["theoretical physicist", "university professor"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "paragraph 1"}], how_known: "Two sources."}

contribution:
  fields: {value: ["quantum electrodynamics", "theoretical physics", "particle physics"], certainty: 1.0, cites: [{source: S1, locator: "paragraphs 2 and 'Five particular achievements'"}, {source: S3, locator: "paragraph 1"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Reconstruction of quantum electrodynamics, removing the meaningless results of the older theory", year: "1946–1949", kind: theory, lasting: "Nobel Prize 1965 (shared with Schwinger and Tomonaga)", certainty: 0.7, cites: [{source: S1, locator: "paragraph 2; 'Five particular achievements' ('By 1948 Feynman completed this reconstruction')"}], how_known: "Britannica (start year is the coder's reading of 'At war's end ... returned to studying the fundamental issues of quantum electrodynamics')."}
    - {value: "Feynman diagrams", year: "1948–1949", kind: method, lasting: "permeated theoretical physics", certainty: 0.7, cites: [{source: S1, locator: "paragraph 2; 'Second, he introduced simple diagrams'"}], how_known: "Britannica."}
    - {value: "Approach to calculating forces in molecules (MIT undergraduate thesis)", year: "1939", kind: method, lasting: "Britannica: 'an original and enduring approach to calculating forces in molecules'", certainty: 0.7, cites: [{source: S1, locator: "paragraph 3 ('his undergraduate thesis (1939) proposed an original and enduring approach to calculating forces in molecules')"}], how_known: "One source calls it lasting; added in the batch 4 lens audit so that first_lasting_contribution_year rests on a listed contribution (P13)."}
    - {value: "Path-integral (least-action, sum-over-paths) approach to quantum mechanics, with Wheeler at Princeton", year: "1942", kind: method, lasting: "standard formulation", certainty: 0.7, cites: [{source: S1, locator: "paragraph 3"}], how_known: "Britannica; year is the doctorate year."}
    - {value: "Quantum-mechanical explanation of superfluidity; V–A theory of the weak force with Gell-Mann; parton model", year: "1950s–1968", kind: theory, lasting: "standard physics", certainty: 0.7, cites: [{source: S1, locator: "paragraph after 'Five particular achievements'"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "Britannica calls him 'the most brilliant, influential, and iconoclastic figure in his field in the post-World War II era'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "One signed article."}
    - {value: "The Feynman Lectures on Physics became a classic textbook", kind: "standard textbook canon", certainty: 0.7, cites: [{source: S1, locator: "lectures paragraph"}], how_known: "Britannica."}
  major_works:
    - {value: "The Feynman Lectures on Physics, 3 vols.", year: 1963, kind: book, certainty: 0.7, cites: [{source: S1, locator: "lectures paragraph (1963–65)"}], how_known: "Britannica."}
    - {value: "Quantum Electrodynamics", year: 1961, kind: book, certainty: 0.7, cites: [{source: S1, locator: "lectures paragraph"}], how_known: "Britannica."}
  honours:
    - {value: "Nobel Prize in Physics (shared with Schwinger and Tomonaga)", year: 1965, certainty: 0.7, cites: [{source: S1, locator: "paragraph 2"}], how_known: "Britannica."}
    - {value: "Albert Einstein Award", year: 1954, certainty: 0.7, cites: [{source: S3, locator: "paragraph 3"}], how_known: "Nobel biography."}
    - {value: "Lawrence Award", year: 1962, certainty: 0.7, cites: [{source: S3, locator: "paragraph 3"}], how_known: "Nobel biography."}
    - {value: "Foreign Member of the Royal Society", year: 1965, certainty: 0.7, cites: [{source: S3, locator: "paragraph 2"}], how_known: "Nobel biography."}
  definition_fit: {value: "clearly meets", rationale: "Remade quantum electrodynamics; Feynman diagrams.", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Jewish (both parents from Jewish families)", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 1"}, {source: S1, locator: "paragraph 3 ('descendant of Russian and Polish Jews')"}], how_known: "Two sources give the Jewish family background; the household's practice is not described."}
  family_religious_practice: {value: TODO, note: "Not described in the sources read. The often-quoted 1967 letter about leaving Sunday school was seen only on a blog and is not used."}
  parents_and_household:
    - {value: "Father, Melville Feynman, born into a Jewish family in Minsk, came to the US at five; a businessman fascinated by science who wanted his son to be a scientist", name: "Melville Feynman", role: father, certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraphs 1–2"}], how_known: "MacTutor, drawing on Gleick."}
    - {value: "Mother, Lucille Phillips, born in the US into a Jewish family of Polish immigrants; trained as a primary school teacher", name: "Lucille Feynman (née Phillips)", role: mother, certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 1"}], how_known: "MacTutor."}
  household_circumstances: {value: "A brother died at four weeks when Richard was five; sister Joan born when he was nine; settled in Far Rockaway at ten", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 3"}], how_known: "MacTutor."}
  schooling:
    - {value: "Far Rockaway High School; won the New York University Math Championship in his final year", stage: "grammar or secondary school", years: "–1935", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraphs 4–5"}], how_known: "MacTutor; end year is the coder's reading (MIT from 1935, BSc 1939)."}
    - {value: "Massachusetts Institute of Technology (BSc 1939)", stage: university, years: "–1939", certainty: 1.0, cites: [{source: S3, locator: "paragraph 1"}, {source: S1, locator: "paragraph 3"}], how_known: "Two sources."}
    - {value: "Princeton University (PhD 1942, adviser John Archibald Wheeler)", stage: university, years: "1939–1942", certainty: 1.0, cites: [{source: S3, locator: "paragraph 1"}, {source: S1, locator: "paragraph 3"}], how_known: "Two sources."}
  early_mathematics: {value: "advanced mathematics", note: "Taught himself trigonometry, calculus and complex numbers before meeting them at school.", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraphs 4–5"}], how_known: "MacTutor."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Home laboratory: circuits, a burglar alarm, radio repair; science from the Encyclopaedia Britannica; father's encouragement", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraphs 2, 4"}], how_known: "MacTutor."}
  key_early_reading:
    - {value: "Encyclopaedia Britannica", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 4"}], how_known: "MacTutor."}
  childhood_mentors:
    - {value: "His father, Melville Feynman", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 2"}], how_known: "MacTutor."}
  languages_in_childhood: {value: [English], certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 1"}], how_known: "American-born."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1939–1988", certainty: 0.7, cites: [{source: S3, locator: "paragraph 1"}], how_known: "MIT thesis to death."}
  nominal_affiliations: []
  self_described_science_religion_relation:
    value: "Conflict over metaphysics, none over ethics: science cannot disprove God, but its habit of doubt turns 'Is there a God?' into 'How sure is it that there is a God?', and there is 'definitely a conflict [...] over the metaphysical aspects of religion'; moral questions are 'outside of the scientific realm'; Western civilization stands on two heritages, the scientific spirit of uncertainty and Christian ethics."
    certainty: 0.7
    cites: [{source: S4, locator: "pp. 20, 21, 23"}]
    how_known: "His own talk, printed by Caltech and checked on the page images. Capped at 0.7: much of the talk follows an imagined student and panel, so the first-person views are framed through that device."
  primary_system:
    value: AGNOS
    basis: written_profession
    certainty: 0.7
    cites: [{source: S4, locator: "pp. 20–21"}]
    how_known: "His own published talk: 'I do not believe that science can disprove the existence of God; I think that is impossible' (p. 20); a scientist can never have 'that real knowledge that there is a God' (p. 21)."
    rationale: "AGNOS (explicit suspension): he holds that the existence of God can be neither disproved by science nor known with certainty, and makes uncertainty 'vital to the scientist' (p. 21). Named alternative: ATHE, since he says the theory that the universe is 'a stage for God to watch man's struggle' seems 'inadequate' (pp. 21–22) and speaks of 'my atheistic scientific colleagues' (p. 22). The talk's student-and-panel framing also limits how directly the views are his, so 0.7. AGNOS is a stub system file (flag)."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Coded at 0.7: God neither disprovable nor knowable with certainty; doubt as the scientist's attitude. Stub system file (flag).", cites: [{source: S4, locator: "pp. 20–21"}]}
    - {code: ATHE, reason: "Named alternative: the conventional God's world-as-stage seems 'inadequate', and he counts atheists among his colleagues; but he does not deny God in this text. Stub system file (flag).", cites: [{source: S4, locator: "pp. 21–22"}]}
    - {code: JUDA, reason: "Rejected: Jewish family background is heritage, never a code; no adult Jewish belief or practice in the sources read.", cites: [{source: S2, locator: "Biography, paragraph 1"}]}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "He leaves God's existence uncertain and places no God anywhere; nothing scores the locus. The 'stage for God' theory 'seems to be inadequate' (p. 22) is a hedged rejection, not an explicit denial of a personal intervening God, so A stays BELOW_THRESHOLD (P20)."}
    B_cause:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "pp. 21–22"}, {source: S1, locator: "paragraph 2"}]
      how_known: "His own talk; 0.7 for the student framing."
      rationale: "Scored on his account of nature (P6). 'the atoms of which all appears to be constructed, following immutable laws. Nothing can escape it' (p. 21); his imagined student comes to believe 'that individual prayer, for example, is not heard' (p. 22). His working physics (QED's 'experimentally perfect package', S1) is lawful throughout. No miracle, petition or exemption."
    C_ledger: {value: BELOW_THRESHOLD, how_known: "The talk mentions doubt about 'an after-life' only as a question the student comes to scrutinize (p. 21); he states no view on judgement or reward."}
    D_authority:
      value: 2
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "p. 23"}]
      how_known: "His own talk; a named alternative, so 0.7."
      rationale: "Two domains, each with its own authority, so D 2 (same-pattern rule, as for Einstein, Heisenberg and Hubble). On metaphysics science and religion conflict 'both in fact and in spirit', and religion cannot find metaphysical ideas safe from 'an ever-advancing and always-changing science' (p. 23); but 'moral questions are outside of the scientific realm' (p. 23). Named alternative: 3, since on every question of fact observation wins and revelation keeps only the ethical domain."
    E_scope:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "pp. 21–22"}]
      how_known: "His own talk; 0.7 for the framing."
      rationale: "Scored on the world's order (P7). Same rules for stars, animals and humans: 'the stars are made of the same stuff, and the animals are made of the same stuff, but in such complexity as to mysteriously appear alive – like man himself' (p. 21); man is 'a latecomer in a vast evolving drama', and a universe arranged 'as a stage for God to watch man's struggle' seems 'inadequate' (pp. 21–22). No favoured group in events."
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD (the P4 test needs A at certainty ≥ 0.7)."}
  statements:
    - text: "I do not believe that science can disprove the existence of God; I think that is impossible."
      cites: [{source: S4, locator: "p. 20"}]
      date: "1956"
      context: "Talk at the Caltech YMCA Lunch Forum, 2 May 1956, printed in Engineering and Science; answering the suggestion that the young scientist who stops believing 'doesn't understand science correctly'."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "I do not believe that a scientist can ever obtain that view – that really religious understanding, that real knowledge that there is a God – that absolute certainty which religious people have."
      cites: [{source: S4, locator: "p. 21"}]
      date: "1956"
      context: "Same talk, section 'Attitude of uncertainty'."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "Yet again, there are the atoms of which all appears to be constructed, following immutable laws. Nothing can escape it; the stars are made of the same stuff, and the animals are made of the same stuff, but in such complexity as to mysteriously appear alive – like man himself."
      cites: [{source: S4, locator: "p. 21"}]
      date: "1956"
      context: "Same talk, section 'Belief in God—and the facts of science': the facts that make belief in the God of the religious type seem unlikely."
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "These scientific views end in awe and mystery, lost at the edge in uncertainty, but they appear to be so deep and so impressive that the theory that it is all arranged simply as a stage for God to watch man's struggle for good and evil seems to be inadequate."
      cites: [{source: S4, locator: "pp. 21–22"}]
      date: "1956"
      context: "Same section, concluding the list of scientific facts."
      axes: [E_scope]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "There is definitely a conflict, I believe – both in fact and in spirit – over the metaphysical aspects of religion."
      cites: [{source: S4, locator: "p. 23"}]
      date: "1956"
      context: "Same talk, after the history of 'retreats' of the religious metaphysical view (earth's motion, man's animal ancestry)."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "On the other hand, I don't believe that a real conflict with science will arise in the ethical aspect, because I believe that moral questions are outside of the scientific realm."
      cites: [{source: S4, locator: "p. 23"}]
      date: "1956"
      context: "Same talk, section 'Science and moral questions'."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
  changes_over_life: []
  coder_notes: "AGNOS and ATHE are stub system files (flag). S4 is the printed transcript of a talk, published by Caltech in its own magazine and read on Caltech's library site (HTML text checked against the PDF page images for page numbers), so it is an authoritative copy, not an unofficial web copy; the 0.7 caps come from the talk's framing (an imagined student and panel) and named alternatives. Not used: the 1967 letter to Levitan about Sunday school (blog copy only) and his AIP oral history (did not load). changes_over_life is empty after research: no dated change of belief in what was read."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Jewish (Russian-Belarusian and Polish immigrant families)", certainty: 1.0, cites: [{source: S1, locator: "paragraph 3"}, {source: S2, locator: "Biography, paragraph 1"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: "Jewish", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 1"}], how_known: "MacTutor ('born into a Jewish family' for both parents)."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1946–1949", certainty: 0.7, cites: [{source: S1, locator: "'At war's end'; 'By 1948 Feynman completed this reconstruction'"}], how_known: "QED reconstruction and diagrams; years are the coder's reading of Britannica."}
  age_at_first_lasting_contribution: {value: 21, certainty: 0.7, cites: [{source: S1, locator: "opening; paragraph 3"}], how_known: "Born May 1918; MIT thesis 1939 (the earliest listed contribution, P13)."}
  first_evidence_of_lio_type_views: {value: "Caltech YMCA talk on science and religion", year: 1956, certainty: 1.0, cites: [{source: S4, locator: "p. 20"}], how_known: "Earliest dated statement read."}
  lio_views_relative_to_major_work: {value: "after major work", rationale: "The statement read is from 1956, after the 1946–49 work; earlier views not read.", certainty: 0.5, cites: [{source: S4, locator: "p. 20"}], how_known: "Dates."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "He describes science as a method of trying things and seeing what happens ('Try it and see', S4, p. 23), not derivation from definitions and axioms.", certainty: 0.5, cites: [{source: S4, locator: "p. 23"}], how_known: "Coder's reading of one talk."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "Biography, paragraphs 4–5"}], how_known: "Self-taught mathematics; nothing on method."}
  circle_present: {value: "no", rationale: "He leaves God uncertain and does not identify God with Nature.", certainty: 0.5, cites: [{source: S4, locator: "pp. 20–21"}], how_known: "Coder's reading."}
  reading: "As belief, not finding: form absent, circle absent. The record does not test H1."
  notes: ""

institutions:
  - {value: "Manhattan Project (Princeton, then Los Alamos)", role: "group leader in the theoretical division", years: "1941–1945", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "World War II paragraph"}], how_known: "Britannica."}
  - {value: "Cornell University", role: "professor of theoretical physics", years: "1945–1950", kind: university, certainty: 1.0, cites: [{source: S3, locator: "paragraph 1"}, {source: S1, locator: "'At war's end'"}], how_known: "Two sources."}
  - {value: "California Institute of Technology", role: "professor of theoretical physics; Richard Chace Tolman Professor", years: "1950–1988", kind: university, certainty: 1.0, cites: [{source: S3, locator: "paragraph 1"}, {source: S1, locator: "'In 1950 he became professor'"}], how_known: "Two sources."}
collaborators:
  - {value: "John Archibald Wheeler", relation: teacher, note: "doctoral adviser at Princeton; least-action approach", certainty: 0.7, cites: [{source: S1, locator: "paragraph 3"}], how_known: "Britannica."}
  - {value: "Hans Bethe", roster_id: bethe-hans, relation: "mentor or employer", note: "head of the Los Alamos theoretical division; yield formula", certainty: 0.7, cites: [{source: S1, locator: "World War II paragraph"}], how_known: "Britannica."}
  - {value: "Murray Gell-Mann", roster_id: gell-mann-murray, relation: collaborator, note: "theory of the weak force (1958)", certainty: 0.7, cites: [{source: S1, locator: "paragraph after 'Five particular achievements'"}], how_known: "Britannica."}
  - {value: "Julian Schwinger", roster_id: schwinger-julian, relation: other, note: "shared the 1965 Nobel Prize (independent equivalent theory)", certainty: 0.7, cites: [{source: S1, locator: "paragraph 2"}], how_known: "Britannica."}
  - {value: "Sin-Itiro Tomonaga", roster_id: tomonaga-sin-itiro, relation: other, note: "shared the 1965 Nobel Prize", certainty: 0.7, cites: [{source: S1, locator: "paragraph 2"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 5, all five models). Included in the fourth batch by owner decision, borderline on the stage-2 date window (1600–1950).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 69"}], how_known: "Study roster; batch inclusion by Jason, 2026-10-02."}
  controversies: []
  data_quality_flags:
    - "Borderline on the stage-2 date window: main work 1946–49; included by owner decision (2026-10-02)."
    - "Britannica read as its main page only."
  open_questions:
    - "Find a printed edition of his letters (for the 1967 Sunday-school letter) or a published interview for first-person statements on religion. His AIP oral history carries a no-quotation notice, so under P8 it cannot score an axis or code on its own and must not be quoted without permission (interview)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "James Gleick"
    citation: "Gleick, James. \"Richard Feynman.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Richard-Feynman."
    url: "https://www.britannica.com/biography/Richard-Feynman"
    accessed: 2026-10-02
    reliability_note: "Signed article by his biographer. Paragraphs counted from the opening '(born May 11, 1918'."
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "J J O'Connor and E F Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Richard Phillips Feynman.\" MacTutor History of Mathematics, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Feynman/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Feynman/"
    accessed: 2026-10-02
    reliability_note: "Biography drawing on Gleick; paragraphs counted from 'Richard Feynman's parents'."
    used_for: [basics, childhood, worldview, heritage, lane_b]
  - id: S3
    type: tertiary
    kind: "institutional page"
    author: "Nobel Foundation"
    year: 1972
    citation: "\"Richard P. Feynman – Biographical.\" From Nobel Lectures, Physics 1963–1970. Amsterdam: Elsevier, 1972. NobelPrize.org. https://www.nobelprize.org/prizes/physics/1965/feynman/biographical/."
    url: "https://www.nobelprize.org/prizes/physics/1965/feynman/biographical/"
    accessed: 2026-10-02
    reliability_note: "Official biography; paragraphs counted from 'Richard P. Feynman was born'."
    used_for: [identity, basics, contribution, childhood, worldview, institutions]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Richard P. Feynman"
    year: 1956
    citation: "Feynman, Richard P. \"The Relation of Science and Religion.\" Engineering and Science 19, no. 9 (June 1956): 20–23 (transcript of a talk at the Caltech YMCA Lunch Forum, 2 May 1956). Caltech Library: https://calteches.library.caltech.edu/49/2/Religion.htm; page images https://calteches.library.caltech.edu/1640/1/Religion.pdf."
    url: "https://calteches.library.caltech.edu/49/2/Religion.htm"
    accessed: 2026-10-02
    reliability_note: "His own talk as printed in Caltech's magazine, on Caltech's library site (authoritative). Page numbers are the printed magazine pages, read from the PDF page images."
    used_for: [basics, worldview, timing, lane_b]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# Richard Feynman

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Richard Feynman (1918–1988), American theoretical physicist, remade quantum electrodynamics and introduced Feynman diagrams; he shared the 1965 Nobel Prize [S1]. In a 1956 Caltech talk he said science cannot disprove God but that a scientist can never have "real knowledge that there is a God", and that science and religion conflict over metaphysics but not ethics [S4, pp. 20–23]. primary_system AGNOS at 0.7 (stub; ATHE named). B 4, D 2, E 4, all at 0.7; A, C below threshold; mid_basin below threshold. Included in this batch by owner decision, borderline on the stage-2 date window.

## Life and work

Born in New York City (Far Rockaway per Britannica; the borough is contested) [S1; S2]; Far Rockaway High School; MIT (1939) and Princeton (PhD 1942); Los Alamos; Cornell (1945–50); Caltech from 1950 [S1; S2; S3].

## Contribution and impact

QED and diagrams (by 1948–49), path integrals, superfluidity, the weak force with Gell-Mann, partons, and the Feynman Lectures [S1].

## Childhood and education

Both parents came from Jewish families; his father pushed him toward science; he taught himself calculus [S2, Biography, paragraphs 1–3].

## Adult working worldview

From his 1956 talk: God neither disprovable nor certain [S4, pp. 20–21]; atoms "following immutable laws. Nothing can escape it" [S4, p. 21]; moral questions "outside of the scientific realm" [S4, p. 23]. Much of the talk follows an imagined student, so its views are capped at 0.7.

## Heritage (context only)

Jewish immigrant families [S1; S2]. Context only.

## Timing

First lasting contribution 1939, at 21 [S1]. Main work 1946–49. The worldview statement read is from 1956.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form absent; circle absent.

## Open questions

- The 1967 letter in a printed edition; a published interview. (The AIP oral history (interview) forbids quotation without permission, so it cannot score on its own.)

## Research log

- 2026-10-02: Read Britannica (Gleick), MacTutor, the Nobel biography, and the 1956 talk on Caltech's site (HTML, with page numbers from the PDF images). The AIP interview page did not load; the 1967 letter was found only on a blog.
