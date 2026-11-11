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
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 20c_late. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (fourth batch, RUNBOOK §1 order). Included by owner decision, borderline on the stage-2 date window (major work 1946–49; Jason, 2026-10-02). Basics from Britannica (Gleick), MacTutor and the Nobel biography. Worldview from his own talk 'The Relation of Science and Religion' (Caltech YMCA Lunch Forum, 2 May 1956), printed in Engineering and Science 19:9 (June 1956), pp. 20–23, read on Caltech's own site and checked on the page images. primary_system AGNOS at 0.7 (stub; ATHE named). B 4, D 2, E 4, all at 0.7; A, C BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 4 (two blind runs at b21655b). #59 (both runs): birth place 'New York City (Manhattan; ...)' at 1.0 → 'New York City' at 1.0; the borough is noted as contested (0.5), Far Rockaway, Queens, per Britannica and MacTutor's Quick Info, with Manhattan (implied by MacTutor's Biography, paragraph 2) as the alternative. MacTutor Biography locators renumbered to the page's visible paragraphs (paragraph 1 is the parents, 2 the Manhattan apartment, 3 the move to Far Rockaway). #63 / decision P13: the 1939 MIT thesis ('an original and enduring approach to calculating forces in molecules', Britannica) is now a listed contribution (0.7), so first_lasting_contribution_year 1939 (0.7) and age 21 rest on a listed item; values unchanged. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02). Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs; A_locus note (P20). Full before → after list: reports/stage3_rulings_changes.csv. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Span alignment (P29, P30 and its addendum): timing.major_work_period 1946–1949 → 1939–1968; worldview.working_years 1939–1988 → 1939–1968, equal to the span (P30 addendum f); lio_views_relative_to_major_work set to 'during major work'; evidence for every headline value checked against the span; no value or certainty changed. Listed in reports/p30_span_alignment.csv. Not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #68, F5 rank 69). Needs: A BELOW_THRESHOLD. Opened What Do You Care What Other People Think? (Norton 1988; WDYC pp. 25–28 'avowed atheist' / 'gradually came to disbelieve the whole religion'), Denis Brian Voice of Genius (1995/2001 p. 49: 'An atheist. Agnostic for me would be trying to weasel out'), Pleasure of Finding Things Out (BBC Horizon 1981 / Robbins 1999: rejects special God-to-earth stories; lives with doubt), Perfectly Reasonable Deviations (Michelle Feynman ed. 2005: Levitan 1967 pp. 234–236 during span; 1982 'as strong an atheist' pp. 349–351). Wikipedia EN dual bio (P50). P47 source_quality on every source. primary_system AGNOS→ATHE @0.5 (post-span self-labels; AGNOS named from 1956); A BELOW→4 @0.5 (explicit denial; alt BELOW from 1956 suspension; P1 post-span / Watson); B stays 4 @0.7, support corroborated (P48); mid_basin stays BELOW_THRESHOLD. Chart: unplotted → faded filled. No fallacy_catalog (Jason). Draft, not reviewed."}

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
    place: {value: "Los Angeles, California", modern_name: "Los Angeles, California, USA", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S10, locator: "infobox / Death section"}], how_known: "Britannica and Wikipedia agree."}
  first_lasting_contribution_year: {value: 1939, certainty: 0.7, cites: [{source: S1, locator: "paragraph 3 ('his undergraduate thesis (1939) proposed an original and enduring approach')"}], how_known: "The MIT undergraduate thesis on forces in molecules, listed as a contribution because Britannica calls it 'original and enduring'; it is the earliest listed contribution (decision P13). His main work (QED) is 1946–49."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "paragraph 3"}], how_known: "From first_lasting_contribution_year (P2); the QED work (by 1948) is in the same bucket."}
  region_of_birth: {value: "North America", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "USA is North America in data/reference/regions.csv (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S3, locator: "paragraph 1"}], how_known: "Princeton, Los Alamos, Cornell, Caltech."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "As the sources record it."}
  languages_of_work: {value: [English], certainty: 1.0, cites: [{source: S4, locator: "p. 20"}, {source: S1, locator: "lectures paragraph"}], how_known: "American physicist; papers, lectures and books in English."}
  occupations: {value: ["theoretical physicist", "university professor"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "paragraph 1"}], how_known: "Two sources."}

contribution:
  era_bucket: 20c_late
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
  family_religious_practice: {value: "Reform Jewish temple and Sunday school in Far Rockaway; synagogue attendance; youth center at the temple; left Sunday school at almost thirteen before confirmation", certainty: 0.7, cites: [{source: S6, locator: "pp. 25–28 (youth center; 'avowed atheist')"}, {source: S9, locator: "pp. 234–236 (Levitan letters, 1967)"}, {source: S10, locator: "Early life / Religion"}], how_known: "Own WDYC narrative and 1967 letters in PRD; Wikipedia maps the temple/Sunday-school outline."}
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
  working_years: {value: "1939–1968", certainty: 0.7, cites: [{source: S1, locator: "'At war's end'; 'By 1948 Feynman completed this reconstruction'"}], how_known: "Equal to timing.major_work_period (P30 addendum f; span check 2026-10-02). Was 1939–1988: MIT thesis to death."}
  nominal_affiliations: []
  self_described_science_religion_relation:
    value: "Conflict over metaphysics, none over ethics: science cannot disprove God, but its habit of doubt turns 'Is there a God?' into 'How sure is it that there is a God?', and there is 'definitely a conflict [...] over the metaphysical aspects of religion'; moral questions are 'outside of the scientific realm'; Western civilization stands on two heritages, the scientific spirit of uncertainty and Christian ethics. Later own words reject special religious stories about our place in the universe as too provincial."
    certainty: 0.7
    cites: [{source: S4, locator: "pp. 20, 21, 23"}, {source: S8, locator: "Doubt and Uncertainty section"}]
    how_known: "1956 talk (during span) plus 1981 Pleasure interview (post-span continuity under P31; no documented change)."
  primary_system:
    value: ATHE
    basis: written_profession
    certainty: 0.5
    cites: [{source: S6, locator: "pp. 25–28 ('avowed atheist'; 'gradually came to disbelieve the whole religion')"}, {source: S7, locator: "p. 49 ('An atheist. Agnostic for me would be trying to weasel out')"}, {source: S9, locator: "pp. 349–351 ('as strong an atheist as he was likely to find', 12 Sep 1982)"}]
    how_known: "Own WDYC narrative and Brian interview self-label 'atheist', plus 1982 letter; all after the 1939–1968 span, so capped at 0.5 (P1 / Watson, Hawking, Crick). No change of view is documented in changes_over_life (P31)."
    rationale: "ATHE: he calls himself an 'avowed atheist', says he 'gradually came to disbelieve the whole religion', refuses the agnostic label as 'trying to weasel out', and later writes he was 'as strong an atheist as [anyone] was likely to find'. Named alternative: AGNOS, from the 1956 talk's during-span suspension ('science can [not] disprove the existence of God'; a scientist can never have 'real knowledge that there is a God'). ATHE and AGNOS are stub system files (flag)."
    note: "Create-pass AGNOS @0.7 rested only on the 1956 talk. Post-span own-word atheist self-labels flip the primary code; certainty stays 0.5 under the post-span cap."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Coded at 0.5: 'avowed atheist'; 'disbelieve the whole religion'; rejects 'agnostic' as weaseling; 1982 'as strong an atheist'. Stub system file (flag).", cites: [{source: S6, locator: "pp. 25–28"}, {source: S7, locator: "p. 49"}, {source: S9, locator: "pp. 349–351"}]}
    - {code: AGNOS, reason: "Named alternative from the 1956 talk (during span): God neither disprovable nor knowable with certainty; doubt as the scientist's attitude. Stub system file (flag).", cites: [{source: S4, locator: "pp. 20–21"}]}
    - {code: JUDA, reason: "Rejected: Jewish family background is heritage, never a code; 1967 letters refuse ethnic/religious counting among Jewish Nobel winners and record leaving Sunday school / 'chosen people'.", cites: [{source: S9, locator: "pp. 234–236"}, {source: S2, locator: "Biography, paragraph 1"}]}
  lio_axes:
    A_locus:
      value: 4
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S6, locator: "pp. 25–28 ('avowed atheist'; 'gradually came to disbelieve the whole religion')"}, {source: S7, locator: "p. 49 ('An atheist')"}, {source: S8, locator: "Doubt and Uncertainty ('I can't believe these special stories' about God coming to the earth)"}]
      how_known: "Own published narrative and interview self-descriptions after the span, so 0.5 (P1 post-span / Watson). Independent source ids → corroborated (P48)."
      rationale: "Explicit denial of a personal intervening God (P20): he was an 'avowed atheist', 'came to disbelieve the whole religion', and rejects special stories of God coming to the earth as too provincial. Named alternative: BELOW_THRESHOLD from the 1956 talk's suspension (science cannot disprove God; no locus placed). P38's 0.5-for-agnostic-self-label does not bind (he refuses 'agnostic'); the 0.5 here is the post-span cap."
    B_cause:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S4, locator: "pp. 21–22"}, {source: S1, locator: "paragraph 2"}, {source: S8, locator: "Doubt and Uncertainty / Rules of the Game"}]
      how_known: "His own 1956 talk (during span) plus Pleasure's lawful-nature / no-special-stories framing; 0.7 for the 1956 student framing."
      rationale: "Scored on his account of nature (P6). 'the atoms of which all appears to be constructed, following immutable laws. Nothing can escape it' (S4, p. 21); imagined student comes to believe 'that individual prayer, for example, is not heard' (p. 22). Pleasure: nature's laws are there to be found; special religious stories about our relation to the universe are unbelievable. Working physics (QED) is lawful throughout. No miracle, petition or exemption."
    C_ledger: {value: BELOW_THRESHOLD, how_known: "The 1956 talk mentions doubt about 'an after-life' only as a question the student comes to scrutinize (p. 21); Pleasure leaves purpose and 'why we're here' unanswered. No view on judgement or reward stated."}
    D_authority:
      value: 2
      basis: written_profession
      certainty: 0.7
      support: single
      cites: [{source: S4, locator: "p. 23"}]
      how_known: "His own talk; a named alternative, so 0.7."
      rationale: "Two domains, each with its own authority, so D 2 (same-pattern rule, as for Einstein, Heisenberg and Hubble). On metaphysics science and religion conflict 'both in fact and in spirit', and religion cannot find metaphysical ideas safe from 'an ever-advancing and always-changing science' (p. 23); but 'moral questions are outside of the scientific realm' (p. 23). Named alternative: 3, since on every question of fact observation wins and revelation keeps only the ethical domain."
    E_scope:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S4, locator: "pp. 21–22"}, {source: S8, locator: "Doubt and Uncertainty ('too local, too provincial')"}]
      how_known: "1956 talk plus Pleasure; 0.7 for the 1956 framing."
      rationale: "Scored on the world's order (P7). Same rules for stars, animals and humans (S4, p. 21); man is 'a latecomer in a vast evolving drama'; a universe arranged 'as a stage for God to watch man's struggle' seems 'inadequate' (pp. 21–22). Pleasure: special stories of God coming to the earth are 'too simple, too connected, too local, too provincial'."
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus 4 is scored only at 0.5, under the 0.7 bar for the A ≥ 3 branch (P10).", note: "If A reached 0.7 the result would be false (A 4, B 4)."}
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
    - text: "Somebody nominated me for president of the youth center. The elders began getting nervous, because I was an 'avowed atheist' by that time. [...] I thought nature itself was so interesting that I didn't want it distorted like that [by miracle stories]. And so I gradually came to disbelieve the whole religion."
      cites: [{source: S6, locator: "pp. 25–28"}]
      date: "1988"
      context: "What Do You Care What Other People Think?, Far Rockaway youth-center episode; as told to Ralph Leighton. Narrative of youth; published post-span. Page locators from Wikipedia/Haught; Norton images not opened."
      axes: [A_locus]
      kind: autobiography
      verified_against: secondary quotation
      verified_on: 2026-10-24
    - text: "[I call myself] an atheist. Agnostic for me would be trying to weasel out and sound a little nicer than I am about this."
      cites: [{source: S7, locator: "p. 49"}]
      date: "1995"
      context: "Denis Brian, The Voice of Genius p. 49 (post-span publication); asked whether he called himself an atheist or an agnostic. Book not page-imaged; Wikiquote/Wikipedia locator."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: secondary quotation
      verified_on: 2026-10-24
    - text: "I can't believe these special stories that have been made up about our relationship to the universe at large because they seem to be too simple, too connected, too local, too provincial. The earth, He came to the earth, one of the aspects of God came to the earth, mind you, and look at what's out there. It isn't in proportion. [...] I don't feel frightened by not knowing things, by being lost in a mysterious universe without having any purpose, which is the way it really is so far as I can tell."
      cites: [{source: S8, locator: "Doubt and Uncertainty section"}]
      date: "1981"
      context: "BBC Horizon / Nova interview The Pleasure of Finding Things Out (post-span)."
      axes: [A_locus, E_scope]
      kind: "recorded interview"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
    - text: "At the age of thirteen I was converted to non-Jewish religious views."
      cites: [{source: S9, locator: "p. 234 (letter to Tina Levitan, January 1967)"}]
      date: "1967-01"
      context: "Declining inclusion in a book on Jewish Nobel Prize winners; during the major-work span. Companion letter (7 Feb 1967, pp. 235–236) explains leaving Sunday school and stopping belief in 'the chosen people'. Not an explicit 'no God' denial by itself."
      axes: [A_locus]
      kind: "published letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
  changes_over_life: []
  coder_notes: "ATHE and AGNOS are stub system files (flag). Create-pass AGNOS @0.7 from S4 alone; D1 flips primary to ATHE @0.5 on post-span own-word atheist self-labels (WDYC, Brian, PRD 1982) with AGNOS named from the 1956 talk. A 4 @0.5 (post-span cap; alt BELOW from 1956 suspension). B/D/E unchanged in value. AIP oral history still unused (P8 no-quotation). Gleick Genius (Kaddish refusal) not used to score A (secondary; Joan's memory). PRD Levitan letters are during span but do not alone state 'no God'. No fallacy_catalog (Jason 2026-10-23)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Jewish (Russian-Belarusian and Polish immigrant families)", certainty: 1.0, cites: [{source: S1, locator: "paragraph 3"}, {source: S2, locator: "Biography, paragraph 1"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: "Jewish", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 1"}], how_known: "MacTutor ('born into a Jewish family' for both parents)."}
  baptism_or_initiation: {value: "none recorded (Jewish household; left Sunday school before confirmation)", certainty: 0.5, cites: [{source: S9, locator: "p. 235 ('at almost thirteen' / before confirmation)"}, {source: S10, locator: "Early life / Religion"}], how_known: "Jewish heritage; no Christian baptism. He left Sunday school just before confirmation (PRD)."}
  childhood_catechism: {value: "Sunday school at the Far Rockaway temple until almost thirteen", certainty: 0.7, cites: [{source: S9, locator: "pp. 234–236"}, {source: S6, locator: "pp. 25–28"}], how_known: "Own letters and WDYC."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1939–1968", certainty: 0.7, cites: [{source: S1, locator: "'At war's end'; 'By 1948 Feynman completed this reconstruction'"}], how_known: "From the 1939 MIT thesis on forces in molecules to the parton model (listed as 1950s–1968, so 1968; P30 #4), the first and last listed lasting contributions (P29). Span check 2026-10-02 (P29, P30 and its addendum): was 1946–1949, the QED years only."}
  age_at_first_lasting_contribution: {value: 21, certainty: 0.7, cites: [{source: S1, locator: "opening; paragraph 3"}], how_known: "Born May 1918; MIT thesis 1939 (the earliest listed contribution, P13)."}
  first_evidence_of_lio_type_views: {value: "Caltech YMCA talk on science and religion", year: 1956, certainty: 1.0, cites: [{source: S4, locator: "p. 20"}], how_known: "Earliest dated statement read."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "The statement read is from 1956, inside the 1939–1968 span (span check 2026-10-02; it was 'after major work' against the old 1946–1949 span); earlier views not read.", certainty: 0.5, cites: [{source: S4, locator: "p. 20"}], how_known: "Dates."}
  worldview_during_major_work: {value: "During-span public talk (1956) frames God as neither disprovable nor certain and nature as under immutable laws; 1967 letters record leaving Jewish religious identity. Post-span own words label the continuous stance atheist (P31; no documented change).", certainty: 0.5, cites: [{source: S4, locator: "pp. 20–23"}, {source: S9, locator: "pp. 234–236"}, {source: S6, locator: "pp. 25–28"}], how_known: "1956 and 1967 inside the span; atheist self-labels after it under continuity (P31)."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "He describes science as a method of trying things and seeing what happens ('Try it and see', S4, p. 23), not derivation from definitions and axioms.", certainty: 0.5, cites: [{source: S4, locator: "p. 23"}], how_known: "Coder's reading of one talk."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "Biography, paragraphs 4–5"}], how_known: "Self-taught mathematics; nothing on method."}
  circle_present: {value: "no", rationale: "He denies a personal God (atheist self-label) and does not identify God with Nature.", certainty: 0.5, cites: [{source: S6, locator: "pp. 25–28"}, {source: S4, locator: "pp. 20–21"}], how_known: "Coder's reading."}
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
    - "A and primary_system rest on post-span own-word atheist labels (0.5 under P1); during-span 1956 talk remains AGNOS-framed."
  open_questions:
    - "Norton page images of WDYC pp. 25–28 and Brian Voice of Genius p. 49 (now cited via secondary locators / Wikiquote); full PRD PDF page-check of pp. 234–236 and 349–351."
    - "AIP oral history still unused (P8 no-quotation)."
    - "Whether a during-span interview (e.g. 1959 KNXT Viewpoint, PRD Appendix I) can lift A or primary_system above the post-span 0.5 cap."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "James Gleick"
    citation: "Gleick, James. \"Richard Feynman.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Richard-Feynman."
    url: "https://www.britannica.com/biography/Richard-Feynman"
    accessed: 2026-10-02
    source_quality: "reference entry"
    reliability_note: "Signed article by his biographer. Paragraphs counted from the opening '(born May 11, 1918'."
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "J J O'Connor and E F Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Richard Phillips Feynman.\" MacTutor History of Mathematics, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Feynman/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Feynman/"
    accessed: 2026-10-02
    source_quality: "reference entry"
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
    source_quality: "reference entry"
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
    source_quality: "primary / own words"
    reliability_note: "His own talk as printed in Caltech's magazine, on Caltech's library site (authoritative). Page numbers are the printed magazine pages, read from the PDF page images."
    used_for: [basics, worldview, timing, lane_b]
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
    type: primary
    kind: "published work by the subject"
    author: "Richard P. Feynman (as told to Ralph Leighton)"
    year: 1988
    citation: "Feynman, Richard P. What Do You Care What Other People Think?: Further Adventures of a Curious Character. Edited by Ralph Leighton. New York: W. W. Norton, 1988."
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "As-told-to memoir published after the span; youth-crisis and 'avowed atheist' passage pp. 25–28 located via Wikipedia Religion cite to Feynman 1988a p. 25 and Positive Atheism / Haught quotation of WDYC pp. 25–28. Norton page images not opened this pass."
    used_for: [childhood, worldview, heritage]
  - id: S7
    type: primary
    kind: other
    author: "Denis Brian (interviewer); Richard P. Feynman"
    year: 1995
    citation: "Brian, Denis. The Voice of Genius: Conversations with Nobel Scientists and Other Luminaries. Cambridge, MA: Perseus / Basic Books, 1995 (repr. 2001), p. 49."
    accessed: 2026-10-24
    source_quality: "newspaper interview"
    reliability_note: "Published interview; atheist/agnostic exchange quoted on Wikiquote and Wikipedia (Brian 2001 p. 49). Interview date within Feynman's life not fixed this pass; publication is after the span. Book not page-imaged."
    used_for: [worldview]
  - id: S8
    type: primary
    kind: other
    author: "Richard P. Feynman"
    year: 1981
    citation: 'Feynman, Richard P. "The Pleasure of Finding Things Out." BBC Horizon (1981); printed in Jeffrey Robbins, ed., The Pleasure of Finding Things Out (Perseus, 1999). Transcript: MIT OCW PDF.'
    url: "https://learning.media.mit.edu/courses/mas713/readings/Finding_Things_Out.pdf"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Broadcast interview (post-span) in a commonly reprinted transcript; MIT course PDF checked for the Doubt and Uncertainty passage."
    used_for: [worldview, lane_b]
  - id: S9
    type: primary
    kind: "published work by the subject"
    author: "Richard P. Feynman; Michelle Feynman (ed.)"
    year: 2005
    citation: "Feynman, Michelle, ed. Perfectly Reasonable Deviations from the Beaten Track: The Letters of Richard P. Feynman. New York: Basic Books, 2005. Levitan correspondence pp. 234–236 (Jan–Feb 1967); 'as strong an atheist' letter 12 Sep 1982 pp. 349–351."
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Scholarly edition of his letters. Levitan Jan 1967 line verified in Quotable Feynman excerpt (PRD p. 234); pp. 235–236 and 349–351 mapped via livesofunbelievers notes citing PRD running heads. Full Basic Books PDF not opened."
    used_for: [childhood, worldview, heritage]
  - id: S10
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: 'Wikipedia, "Richard Feynman," https://en.wikipedia.org/wiki/Richard_Feynman (Early life / Religion; death place).'
    url: "https://en.wikipedia.org/wiki/Richard_Feynman"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Featured article used as dual bio (P50) and to map religion citations (WDYC p. 25; Brian p. 49; PRD Levitan). Not used alone to score A."
    used_for: [basics, childhood, heritage, review]
---

# Richard Feynman

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Richard Feynman (1918–1988), American theoretical physicist, remade quantum electrodynamics and introduced Feynman diagrams; he shared the 1965 Nobel Prize [S1]. In a 1956 Caltech talk he said science cannot disprove God but that a scientist can never have "real knowledge that there is a God" [S4]. Later own words call him an "avowed atheist" who "came to disbelieve the whole religion" [S6] and refuse the agnostic label [S7]. primary_system ATHE at 0.5 (stub; AGNOS named from 1956). A 4 at 0.5; B 4, D 2, E 4 at 0.7; C and mid_basin below threshold. Included by owner decision, borderline on the stage-2 date window.

## Life and work

Born in New York City (Far Rockaway per Britannica; the borough is contested) [S1; S2]; Far Rockaway High School; MIT (1939) and Princeton (PhD 1942); Los Alamos; Cornell (1945–50); Caltech from 1950 [S1; S2; S3].

## Contribution and impact

QED and diagrams (by 1948–49), path integrals, superfluidity, the weak force with Gell-Mann, partons, and the Feynman Lectures [S1].

## Childhood and education

Both parents came from Jewish families; temple and Sunday school in Far Rockaway until he left at almost thirteen [S6; S9; S10]; his father pushed him toward science; he taught himself calculus [S2, Biography, paragraphs 1–3].

## Adult working worldview

During-span 1956 talk: God neither disprovable nor certain [S4, pp. 20–21]; atoms "following immutable laws. Nothing can escape it" [S4, p. 21]; moral questions "outside of the scientific realm" [S4, p. 23]. Post-span own words: "avowed atheist" / "disbelieve the whole religion" [S6]; "An atheist. Agnostic for me would be trying to weasel out" [S7]; rejects special God-to-earth stories [S8]. primary_system ATHE at 0.5; A 4 at 0.5; B 4 at 0.7.

## Heritage (context only)

Jewish immigrant families [S1; S2]. Context only.

## Timing

First lasting contribution 1939, at 21 [S1]. Main work 1946–49. The worldview statement read is from 1956.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form absent; circle absent.

## Open questions

- Norton page images of WDYC pp. 25–28; Brian p. 49; full PRD pp. 234–236 and 349–351.
- 1959 KNXT Viewpoint transcript (PRD Appendix I) for a possible during-span lift above 0.5.
- AIP oral history unused (P8 no-quotation).

## Research log

- 2026-10-02: Read Britannica (Gleick), MacTutor, the Nobel biography, and the 1956 talk on Caltech's site (HTML, with page numbers from the PDF images). The AIP interview page did not load; the 1967 letter was found only on a blog.
- 2026-10-24 (D1): WDYC / Brian / Pleasure / PRD Levitan and 1982 atheist letter (via Quotable Feynman, Wikipedia, Wikiquote, livesofunbelievers locators); Wikipedia dual bio. A BELOW→4 @0.5; primary AGNOS→ATHE @0.5; B stays 4 @0.7 corroborated.
