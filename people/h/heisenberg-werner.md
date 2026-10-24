---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 9
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, third batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (third batch, RUNBOOK §1 order). Basics from Britannica (Beyler, first page), MacTutor and the Nobel biography. Worldview from his own Guardini Prize lecture (Munich 1973), read in the English translation 'Scientific Truth and Religious Truth', CrossCurrents 24:4 (1975), 463–473, as a scan of the JSTOR page images. primary_system PLATO at 0.7 (CHRIST named). A 2 (0.7), B 4 (0.7), D 2 (0.7); C, E BELOW_THRESHOLD; mid_basin TODO (A = 2). Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Self-described relation lowered from 1.0 to 0.7 under the CODING_GUIDE §7 unofficial-web-copy cap (S4 read from a user upload of the JSTOR PDF, not JSTOR itself)."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "record_version corrected to 3 (the 1f3c4bf fix did not raise it). Decision P9: the §7 cap (0.7) on fields resting on the JSTOR-PDF copy is kept, since its provenance cannot be confirmed from the copy; reading the article on JSTOR would lift it. Notes only; no score changed. Schema 1.1 → 1.2."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 3 (two blind runs at d9903b7). #33 (run 1; verified on the CrossCurrents text): primary_system PLATO (0.7) → BELOW_THRESHOLD, with PLATO (leading) and CHRIST as candidates. PLATO's use_when needs the intelligible reality to be the ultimate origin of both existence and values; the lecture makes the realm behind phenomena the ground of ethics and trust (p. 467), not of existence, and pairs Plato with the Bible (p. 467) while speaking from inside the Christian 'linguistic area' (p. 471). PLATO's do_not_use_when sends Platonism inside Christianity to the host religion unless the Platonism clearly dominates, which the record does not show; CHRIST's use_when (specifically Christian belief) is not met either. No axis changed; mid_basin unchanged (TODO, A = 2). #41 (run 2): nominal affiliation reworded; MacTutor gives the parents' affiliation, not his own. #44 (run 2): Nobel biography locators recounted from 'Werner Heisenberg was born': the 1925 / Nobel sentence is paragraph 10 (was 7), Berlin paragraph 6 (was 5), the Max Planck Institute paragraphs 7 and 9 (were 6, 8). Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02). Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs; BELOW_THRESHOLD vs UNKNOWN per P19; kind lists (P21: research institute, school stage and run_by, scholarly edition). Full before → after list: reports/stage3_rulings_changes.csv. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "P30 rule 5 age sweep: ages recomputed as event year − birth year, with no month adjustment (scripts/recompute_ages.py; every change is in reports/p30_age_changes.csv). No other value changed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Span alignment (P29, P30 and its addendum): timing.major_work_period checked, 1925–1932 unchanged; worldview.working_years 1922–1976 → 1925–1932, equal to the span (P30 addendum f); 4 headline values rest on evidence outside the span and are left unchanged for a ruling (open questions). Listed in reports/p30_span_alignment.csv. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "P31 (continuity rule, v8's pick, 2026-10-02): the 4 values the span check flagged as resting on evidence outside the span are resolved, since changes_over_life documents no change of view between the span and that evidence; no value or certainty changed; the Open questions pointer line was removed. Listed in reports/p30_span_alignment.csv. Not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #79, F5 rank 80). Needs: A single source. New S6: Der Teil und das Ganze (Piper 1969; Würzburg WueCampus scan of ISBN 3-492-03080-7, 6. Aufl. 1986) Kap. 17 — own-words rephrase of Pauli's 'persönlichen Gott' as 'zentralen Ordnung der Dinge oder des Geschehens' and 'Aber dieser Text [Pascal Feuer] würde nicht für mich gelten' (scan PDF pp. 116–117); English Physics and Beyond / Wilber reprints omit the Pascal-refusal clause (flag). S7 Wikipedia EN dual-bio (P50) with S1 Britannica. S8 Physics and Philosophy (1958) ost-physics IA open text — Plato/Pythagoras vs Democritus; Descartes 'God is in the world and in the I'. P47 source_quality on S1–S8. A 2 @0.7 support single → corroborated (S4+S6); B 4 @0.7 labelled corroborated (S4+S1); D 2 @0.7 support single → corroborated (S4+S6). primary_system stays BELOW_THRESHOLD (PLATO leading, CHRIST named; Teil und Ganze read, still no use_when for existence-origin). mid_basin unchanged TODO (no P4 branch for A=2). Chart-moving YES: hollow → filled (A and B both corroborated; darkness already dark @ min 0.7). No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: heisenberg-werner
  display_name: "Werner Heisenberg"
  roster:
    canonical_name: "Werner Heisenberg"
    rank: 80
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: physics
    field_bucket: physics
  full_name: {value: "Werner Karl Heisenberg", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Britannica's heading; the middle name is not in S2 or S3."}
  native_name: {value: "Werner Heisenberg (German)", certainty: 0.7, cites: [{source: S3, locator: "paragraph 1"}], how_known: "Same spelling in German."}
  aliases:
    - {name: "Heisenberg-Werner", kind: "roster alias"}
    - {name: "Werner-Heisenberg", kind: "roster alias"}

basics:
  birth:
    date: {value: "1901-12-05", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S3, locator: "paragraph 1"}], how_known: "Two sources agree."}
    place: {value: "Würzburg", modern_name: "Würzburg, Germany", polity_then: "Kingdom of Bavaria, German Empire", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S3, locator: "paragraph 1"}], how_known: "Two sources agree."}
  death:
    date: {value: "1976-02-01", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S3, locator: "note at end"}], how_known: "Two sources agree."}
    place: {value: "Munich", modern_name: "Munich, Germany", polity_then: "West Germany", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1925, certainty: 1.0, cites: [{source: S1, locator: "'Founding of quantum mechanics'"}, {source: S3, locator: "paragraph 10"}], how_known: "The July 1925 paper founding matrix mechanics."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "'Founding of quantum mechanics'"}], how_known: "From first_lasting_contribution_year (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Germany is Western Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S3, locator: "paragraphs 2–6"}], how_known: "Göttingen, Leipzig, Berlin and Munich, with stays in Copenhagen (Northern Europe)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S3, locator: "paragraph 1"}], how_known: "As the sources record it."}
  languages_of_work: {value: [German], certainty: 0.7, cites: [{source: S1, locator: "German paper titles"}], how_known: "His main papers are in German; English versions of his books exist."}
  occupations: {value: [physicist, "university professor", "institute director"], certainty: 1.0, cites: [{source: S3, locator: "paragraphs 3–6"}, {source: S1, locator: "opening"}], how_known: "Two sources."}

contribution:
  fields: {value: ["quantum mechanics", "nuclear physics", "theoretical physics"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Matrix mechanics, the first form of quantum mechanics (with Born and Jordan)", year: "1925", kind: theory, lasting: "foundation of quantum mechanics; Nobel Prize for 1932", certainty: 1.0, cites: [{source: S1, locator: "'Founding of quantum mechanics'"}, {source: S2, locator: "1925 paragraph"}], how_known: "Two sources."}
    - {value: "Uncertainty principle", year: "1927", kind: "law or principle", lasting: "standard textbook canon", certainty: 1.0, cites: [{source: S1, locator: "'Uncertainty principle'"}, {source: S2, locator: "1927 paragraph"}], how_known: "Two sources."}
    - {value: "Prediction of the two forms of molecular hydrogen (ortho- and para-hydrogen)", year: "1927", kind: discovery, lasting: "cited in the Nobel award", certainty: 1.0, cites: [{source: S3, locator: "paragraph 10"}, {source: S2, locator: "Nobel citation"}], how_known: "Two sources."}
    - {value: "Neutron–proton model of the nucleus (three-part paper)", year: "1932", kind: theory, lasting: "basis of nuclear structure theory", certainty: 0.7, cites: [{source: S2, locator: "1932 paragraph"}], how_known: "MacTutor."}
  evidence_of_impact:
    - {value: "Nobel Prize in Physics for 1932 for the creation of quantum mechanics", kind: "honours in lifetime", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "paragraph 10"}], how_known: "Two sources."}
  major_works:
    - {value: "Über quantentheoretische Umdeutung kinematischer und mechanischer Beziehungen", year: 1925, kind: "paper or paper series", certainty: 0.7, cites: [{source: S1, locator: "'Founding of quantum mechanics'"}], how_known: "Britannica gives the title and date."}
    - {value: "Über den anschaulichen Inhalt der quantentheoretischen Kinematik und Mechanik", year: 1927, kind: "paper or paper series", certainty: 0.7, cites: [{source: S1, locator: "'Uncertainty principle'"}], how_known: "Britannica (which misprints 'anschulichen')."}
    - {value: "Die physikalischen Prinzipien der Quantentheorie (The Physical Principles of the Quantum Theory)", year: 1930, kind: book, certainty: 0.7, cites: [{source: S2, locator: "1928 paragraph"}], how_known: "MacTutor dates it 1928; the English edition is 1930. Year uncertain."}
  honours:
    - {value: "Nobel Prize in Physics (for 1932)", year: 1932, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "paragraph 10"}], how_known: "Two sources."}
    - {value: "Romano Guardini Prize of the Catholic Academy in Bavaria", year: 1973, certainty: 1.0, cites: [{source: S4, locator: "p. 463 (editor's note)"}], how_known: "The published lecture's editorial note."}
  definition_fit: {value: "clearly meets", rationale: "Founded quantum mechanics.", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Sources agree."}

childhood:
  family_religion: {value: "Evangelical Lutheran (mother converted from Catholicism at marriage); the parents were religious only by convention", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 3"}], how_known: "MacTutor, drawing on Cassidy's biography (its reference [3])."}
  family_religious_practice: {value: "Conventional only: in private the parents expressed their lack of belief; the children were brought up 'to follow Christian ethics but showed total disbelief in the historical side of Christianity'", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 3"}], how_known: "MacTutor only."}
  parents_and_household:
    - {value: "Father, August Heisenberg, classics teacher, later professor of Middle and Modern Greek at Munich", name: "August Heisenberg", role: father, certainty: 1.0, cites: [{source: S3, locator: "paragraph 1"}, {source: S1, locator: "'Education'"}], how_known: "Two sources."}
    - {value: "Mother, Anna Wecklein, daughter of the headmaster of the Maximilians-Gymnasium, Munich", name: "Anna Heisenberg (née Wecklein)", role: mother, certainty: 1.0, cites: [{source: S1, locator: "'Education'"}, {source: S2, locator: "Biography, paragraph 1"}], how_known: "Two sources."}
  household_circumstances: {value: "Academic family; an older brother, Erwin; moved from Würzburg to Munich in 1910", certainty: 1.0, cites: [{source: S2, locator: "Biography, paragraphs 1, 4"}, {source: S1, locator: "'Education'"}], how_known: "Two sources."}
  schooling:
    - {value: "Primary school, Würzburg; Elisabethenschule, Munich", stage: "elementary school", years: "1906–1911", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 4"}], how_known: "MacTutor; 'primary school' mapped to the nearest stage."}
    - {value: "Maximilians-Gymnasium, Munich (Abitur 1920)", stage: "grammar or secondary school", years: "1911–1920", certainty: 1.0, cites: [{source: S1, locator: "'Education'"}, {source: S3, locator: "paragraph 2"}], how_known: "Two sources."}
    - {value: "University of Munich under Sommerfeld (doctorate 1923, on turbulence), with study under Born at Göttingen", stage: university, years: "1920–1923", certainty: 1.0, cites: [{source: S1, locator: "'Education'"}, {source: S3, locator: "paragraph 2"}], how_known: "Two sources."}
  early_mathematics: {value: "advanced mathematics", note: "Tutored a university student in calculus in 1917 and read Kronecker on number theory as a schoolboy.", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraphs 5–6"}], how_known: "MacTutor only."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Mathematics and physics were his best school subjects, with religion", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 5"}], how_known: "MacTutor."}
  key_early_reading:
    - {value: "Kronecker on number theory; Weyl; Bachmann's survey of number theory", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraphs 6, 9"}], how_known: "MacTutor."}
    - {value: "Romano Guardini's writings, read 'as a young person'", certainty: 1.0, cites: [{source: S4, locator: "p. 463"}], how_known: "His own statement."}
  childhood_mentors:
    - {value: "His father, whose influence on his interest in mathematics the Nobel biography notes", certainty: 0.7, cites: [{source: S3, locator: "paragraph 1"}], how_known: "Nobel biography ('probably due to his influence')."}
  languages_in_childhood: {value: [German], certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "German home and schools."}
  notable_events:
    - {value: "Took part, at 17, in the suppression of the Bavarian Soviet Republic, which he later called 'a kind of adventure'", year: "1919", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 8"}], how_known: "MacTutor, quoting him."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1925–1932", certainty: 1.0, cites: [{source: S1, locator: "'Founding of quantum mechanics'; 'Uncertainty principle'"}, {source: S2, locator: "1925–1932 paragraphs"}], how_known: "Equal to timing.major_work_period (P30 addendum f; span check 2026-10-02). Was 1922–1976: From his first research to his death."}
  nominal_affiliations:
    - {value: "Raised and lived as a Lutheran Christian (Evangelical); parents Evangelical Lutheran by convention (father Lutheran; mother converted from Catholicism)", years: "1901–1976", role: "member by upbringing / adult affiliation", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 3"}, {source: S7, locator: "lead / Personal life (Lutheran Christian)"}], how_known: "MacTutor on parents and Christian-ethics upbringing; Wikipedia states he 'was raised and lived as a Lutheran Christian' (S7). Adult baptismal record still unread; membership is not a worldview code."}
  self_described_science_religion_relation:
    value: "Two truths in two languages: 'I am convinced of the unassailability of scientific truth in its own sphere', yet he could never dismiss religious thinking or 'doubt the truth of what they are pointing to'; religion is a poetic language of images and parables for the order behind phenomena and the basis of ethics, and the two languages must not be confused."
    certainty: 0.7
    cites: [{source: S4, locator: "pp. 463, 467, 471–472"}]
    how_known: "His own published lecture (1973; English 1975), checked on the journal page images in a user-uploaded copy of the JSTOR PDF. Capped at 0.7 under CODING_GUIDE §7: the copy is unofficial and its wording was not checked on JSTOR itself (lending/subscription). Decision P9 (2026-10-02) keeps the cap because the copy's provenance cannot be confirmed from the copy itself; reading the article directly on JSTOR (stable/24457901) would lift it."
  primary_system:
    value: BELOW_THRESHOLD
    cites: [{source: S4, locator: "pp. 464–465, 467, 471"}]
    how_known: "His own public lecture. The divine is a 'God of order', and 'we do not know whether he is identical with the one to whom we turn in need' (pp. 464–465); religious precepts rest 'on tht realm behind it, which Plato referred to as the realm of ideas, and which the Bible speaks of in the words “God is a spirit.”' (p. 467); religion's images help us understand 'the ordered world perceptible behind phenomena', and its language 'is in principle as replaceable as any other language' (p. 471). Applying the PLATO file as written (lens audit batch 3, #33): its use_when needs an intelligible reality that is 'the ultimate origin of both existence and values'; the lecture makes the realm behind phenomena the basis of ethics and of trust (p. 467) but says nothing of it as the origin of existence, and the one sentence naming Plato names the Bible with him (p. 467). Its do_not_use_when sends Platonism inside Christianity to the host religion unless the Platonism clearly dominates; he speaks of 'the European world moulded by the Christian religion' and of being born into 'a definite linguistic area' (p. 471), and the replaceability of religious language argues against a specific confession, not for Platonism. CHRIST's use_when needs specifically Christian belief (Christ, scripture, creeds, church), which the lecture does not affirm. So neither code reaches 0.5 on this one lecture."
    note: "Candidates: PLATO (leading) and CHRIST. Was PLATO at 0.7 until lens audit batch 3. Deepen D1 read Der Teil und das Ganze Kap. 17 (zentrale Ordnung; Pascal Feuer 'würde nicht für mich gelten') and Physics and Philosophy ch. 5 (Plato cave / 'God is in the world and in the I' as critique of Descartes) — still no clear statement that the intelligible realm is the ultimate origin of existence as well as values (PLATO use_when); CHRIST still lacks creed/Christ affirmation. Kept BELOW_THRESHOLD."
  secondary_system: {value: UNKNOWN, how_known: "No second system published in what was read."}
  candidate_codes_considered:
    - {code: PLATO, reason: "Leading candidate, not coded (BELOW_THRESHOLD): the order 'behind' phenomena, named with Plato's realm of ideas, grounds ethics; religious languages are interchangeable images of it. Not coded: PLATO's use_when needs the realm to be the origin of existence as well as values, which the lecture does not say, and the Plato sentence also names the Bible (p. 467), so Platonism is not shown to dominate the Christian frame (do_not_use_when).", cites: [{source: S4, locator: "pp. 467, 471"}]}
    - {code: CHRIST, reason: "Candidate, not coded: Lutheran family; he speaks from within the Christian 'linguistic area' and admires Guardini's Christian world, but affirms no specifically Christian doctrine in what was read. Membership and upbringing are never a code.", cites: [{source: S4, locator: "pp. 463, 467, 471"}, {source: S2, locator: "Biography, paragraph 3"}]}
    - {code: DEISM, reason: "Rejected: no creator-who-does-not-intervene doctrine, and he does not reject revelation; he leaves open whether the God of order is the God of petition.", cites: [{source: S4, locator: "pp. 464–465"}]}
    - {code: PANENT, reason: "Considered: an order both in the world ('the divine order of the world', p. 471) and behind it (p. 467). Not coded: the forms-like realm of ideas fits PLATO, whose do_not_use_when sends 'a God both in and beyond the world without the forms' to PANENT. PANENT is a stub system file (flag).", cites: [{source: S4, locator: "pp. 467, 471"}]}
  lio_axes:
    A_locus:
      value: 2
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S4, locator: "pp. 464–465, 467, 471"}, {source: S6, locator: "Kap. 17 (1952), Würzburg scan PDF pp. 116–117"}]
      how_known: "Two independent own-words works (Guardini Prize lecture S4; memoir dialogue S6). Mixed reading, so 0.7. Independent source ids → corroborated (P48)."
      rationale: "Mixed, held at 2. Guardini: a 'God of order' and 'partial structures from the divine order of the world' (p. 471) lean immanent; the order is 'behind' phenomena with Plato's realm of ideas / 'God is a spirit' (p. 467); whether this God is 'the one to whom we turn in need' is left open (pp. 464–465). Teil und das Ganze Kap. 17: when Pauli asks if he believes in a 'persönlichen Gott', he rephrases to whether one can meet the 'zentralen Ordnung der Dinge oder des Geschehens' as directly as another's soul, answers yes, and adds that Pascal's 'Feuer' text (God of Abraham) 'würde nicht für mich gelten' (scan PDF pp. 116–117) — not a personal biblical God, not bare identity with the world. Named alternatives: 3 if 'göttliche Ordnung der Welt' / zentrale Ordnung is read as immanent pantheism; 1 if the open petition-God question or Wikipedia's 'devout Christian' label is preferred over his own rephrase."
    B_cause:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S4, locator: "p. 465"}, {source: S1, locator: "'Uncertainty principle'"}]
      how_known: "His own lecture and Britannica's account of his physics; a named alternative, so 0.7. Independent source ids → corroborated (P48)."
      rationale: "Scored on his account of nature (P6), his working physics. Laws and repeatable experiment rule: 'The repeatable nature of experiments finally always permits a consensus on the true behaviour of nature' (p. 465), and modern science 'has brought to light laws of wide scope' (p. 472). His uncertainty principle made 'absolute causal determinism' impossible and atomic theory probabilistic (S1), which is statistical law, not miracle or exemption. Named alternative: 3, if the 'limits' of causal description 'through experience with atoms' (p. 465) are read as a standing exception."
    C_ledger: {value: UNKNOWN, how_known: "He makes religion 'the basis of ethics' (p. 467) but says nothing in what was read about judgement, afterlife, or reward and punishment of persons.", note: "Gap: Der Teil und das Ganze (1969), chs. 7 and 17, and Physics and Philosophy (1958); lending-only scans."}
    D_authority:
      value: 2
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S4, locator: "pp. 463, 471–472"}, {source: S6, locator: "Kap. 17; also Kap. 7 (1927) on science/religion languages"}]
      how_known: "Guardini lecture (S4) plus memoir (S6) keep science and religion as distinct languages/spheres; a named alternative, so 0.7. Independent source ids → corroborated (P48)."
      rationale: "Two domains, each with its own authority, so D 2 (same-pattern rule, as for Einstein, Planck and Galileo). Guardini: 'The correctness of proven scientific results cannot sensibly be doubted by religious thinking, and, vice versa, the ethical demands which proceed from the heart of religious thinking should not be dissolved by extreme rational arguments from the sphere of science' (p. 472); 'We must not confuse both languages' (p. 471). Memoir: zentrale Ordnung grounds ethics/compass while science has its own sphere (Kap. 17); 1927 reconstructed talk resists sharp knowledge/faith split but still treats religious language as non-objectifying (Kap. 7). Named alternative: 3, since on questions of fact science decides and religious language is 'not scientific' (S4 p. 470)."
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). The lecture speaks of one 'divine order of the world' and laws of wide scope, but nothing read addresses whether the same rules govern every kind of being or whether any group is favoured in events; the Russians' experience of 'the workings of God in the world' (p. 468) is his report of Dostoevsky's characters, not his own view."}
  mid_basin: {value: TODO, how_known: "A_locus = 2 at 0.7 (corroborated) and B_cause = 4 at 0.7 (corroborated). Both axes are scored at 0.7 but A falls between the branches: the P4 test has no branch for A_locus = 2 (CODING_GUIDE §6).", note: "Same case as Planck; needs a decision, not more evidence. Deepen D1 filled the hollow ring (A corroborated) but does not resolve mid_basin."}
  statements:
    - text: "Although I am convinced of the unassailability of scientific truth in its own sphere, I have never been able to dismiss the content of religious thinking simply as a stage in human consciousness which we have superseded, as a part which we can dispense with in future. So I have continually been forced during my life to ponder on the relationship between these two worlds of the spirit, for I have never been able to doubt the truth of what they are pointing to."
      cites: [{source: S4, locator: "p. 463"}]
      date: "1973"
      context: "Opening of his speech accepting the Romano Guardini Prize of the Catholic Academy in Bavaria, Munich; English translation in CrossCurrents."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "Of course, the God we are speaking of here is a God of order, and we do not know whether he is identical with the one to whom we turn in need, to whom we refer our lives."
      cites: [{source: S4, locator: "pp. 464–465"}]
      date: "1973"
      context: "On Kepler and the early modern scientists who saw mathematical laws as 'the visible expression of the divine will'."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "only recently have we been forced to realize the limits of this method through experience with atoms. Even bearing in mind this experience, we have a seemingly unassailable criterion for truth. The repeatable nature of experiments finally always permits a consensus on the true behaviour of nature."
      cites: [{source: S4, locator: "p. 465"}]
      date: "1973"
      context: "On trust in 'the causal course of events' as a basic postulate of modern science."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "And these precepts are not based on the directly visible world, but on tht realm behind it, which Plato referred to as the realm of ideas, and which the Bible speaks of in the words “God is a spirit.”"
      cites: [{source: S4, locator: "p. 467"}]
      date: "1973"
      context: "On religion as speaking not of norms but of precepts. 'tht' is the printed text (checked on the page image), kept uncorrected."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "The correctness of proven scientific results cannot sensibly be doubted by religious thinking, and, vice versa, the ethical demands which proceed from the heart of religious thinking should not be dissolved by extreme rational arguments from the sphere of science."
      cites: [{source: S4, locator: "p. 472"}]
      date: "1973"
      context: "On keeping religious and scientific language apart."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02

    - text: "Darf ich die Frage auch anders formulieren? Dann würde sie lauten: Kannst du, oder kann man der zentralen Ordnung der Dinge oder des Geschehens, an der ja nicht zu zweifeln ist, so unmittelbar gegenübertreten, mit ihr so unmittelbar in Verbindung treten, wie dies bei der Seele eines anderen Menschen möglich ist? … Wenn du so fragst, würde ich mit Ja antworten. Und ich könnte … an den berühmten Text erinnern, den Pascal immer bei sich trug und den er mit dem Wort ›Feuer‹ begonnen hatte. Aber dieser Text würde nicht für mich gelten."
      cites: [{source: S6, locator: "Kap. 17 (1952), Würzburg scan PDF pp. 116–117"}]
      date: "1969"
      context: "Reconstructed 1952 Copenhagen harbour walk with Pauli (Der Teil und das Ganze Kap. 17). Pauli asked whether he believed in a personal God; Heisenberg rephrased to the central order and refused Pascal's personal 'Feuer' text for himself. English Physics and Beyond / Wilber reprints of this exchange omit the final refusal clause — German governs."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-24
      note: "Memoir reconstructs dialogue decades later (author's Thucydides preface); his own lines only. P26: do not prefer the incomplete English reprint."
    - text: "If one uses the fundamental concepts of Descartes at all, it is essential that God is in the world and in the I and it is also essential that the I cannot be really separated from the world."
      cites: [{source: S8, locator: "ch. 5 (Development of Philosophical Ideas Since Descartes)"}]
      date: "1958"
      context: "Physics and Philosophy — critique of the Cartesian God–world–I split; historical-philosophical, not a creedal profession, but consistent with A 2's refusal of a God raised wholly above the world."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-24
  changes_over_life: []
  coder_notes: "PANENT is a stub system file (flag); PLATO and CHRIST are drafts. Guardini lecture read in CrossCurrents English (S4, §7 unofficial JSTOR-PDF copy). Deepen D1: Der Teil und das Ganze Kap. 17 read in German on the Würzburg Piper scan (S6); only Heisenberg's own lines used; Pauli/Bohr/Dirac lines are not his views. English Physics and Beyond / Wilber Quantum Questions p. 38 omit 'Aber dieser Text würde nicht für mich gelten' — flag, German governs. Physics and Philosophy ch. 5 checked on ost-physics IA open text (S8). Edge.org web copy of the 1927 'Science and Religion' chapter used only as a finding aid (speakers carefully attributed: 'personal God is foreign to me' is Bohr in that reconstruction, not Heisenberg). changes_over_life empty: no dated reversal between 1927 reconstruction, 1952 reconstruction, 1958 book and 1973 lecture."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German (Bavarian academic family)", certainty: 1.0, cites: [{source: S1, locator: "'Education'"}, {source: S2, locator: "Biography, paragraph 1"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: "Evangelical Lutheran (father); mother a convert from Catholicism", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 3"}], how_known: "MacTutor."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: "Religion was among his best school subjects", certainty: 0.5, cites: [{source: S2, locator: "Biography, paragraph 5"}], how_known: "MacTutor; content of the instruction not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1925–1932", certainty: 1.0, cites: [{source: S1, locator: "'Founding of quantum mechanics'; 'Uncertainty principle'"}, {source: S2, locator: "1925–1932 paragraphs"}], how_known: "Matrix mechanics to the nuclear model."}
  age_at_first_lasting_contribution: {value: 24, certainty: 1.0, cites: [{source: S3, locator: "paragraph 10 ('when he was only 23 years old')"}], how_known: "Nobel biography. P30 (rule 5): 1925 − 1901 = 24, with no month adjustment; was 23 until the P30 age sweep (2026-10-02)."}
  first_evidence_of_lio_type_views: {value: "Der Teil und das Ganze Kap. 7 (1927 Solvay talk, reconstructed) and Kap. 17 (1952 zentrale Ordnung); earliest published own-words book 1969", year: 1969, certainty: 0.7, cites: [{source: S6, locator: "Kap. 7 and 17"}, {source: S4, locator: "pp. 463–472"}], how_known: "Memoir published 1969 reconstructs 1927/1952 talks; Guardini lecture 1973 is later. Certainty 0.7: reconstruction, not contemporaneous transcript."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "Memoir Kap. 7 places the Solvay science-and-religion talk in 1927, inside major_work_period 1925–1932; Kap. 17 (1952) and Guardini (1973) are later. P31: no documented change of view between span and later evidence.", certainty: 0.5, cites: [{source: S6, locator: "Kap. 7 (1927)"}, {source: S4, locator: "p. 463"}], how_known: "Memoir dates are reconstructed (0.5)."}
  worldview_during_major_work: {value: "Same A 2 / B 4 pattern as adult working worldview, on the 1927 Solvay reconstruction (Kap. 7) plus working physics; not a separate code", certainty: 0.5, cites: [{source: S6, locator: "Kap. 7"}, {source: S1, locator: "'Uncertainty principle'"}], how_known: "Memoir reconstruction of 1927 plus physics in the span; certainty 0.5 (reconstructed dialogue)."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", certainty: 0.5, cites: [{source: S1, locator: "'Founding of quantum mechanics'"}], how_known: "Coder's reading: matrix mechanics starts from the rule that theory 'should be based only on observable quantities' (S1) and works out consequences, but this is not a definitional method."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "Biography, paragraphs 5–6"}], how_known: "Strong early mathematics; nothing on method."}
  circle_present: {value: "partly", rationale: "A 'divine order of the world' made visible by science (p. 471), but placed 'behind' phenomena, not identified with Nature.", certainty: 0.5, cites: [{source: S4, locator: "pp. 467, 471"}], how_known: "Coder's reading of one lecture."}
  reading: "As belief, not finding: form partly present; circle partly present (order of the world, but behind phenomena). The record does not test H1."
  notes: ""

institutions:
  - {value: "University of Copenhagen (Bohr's institute)", role: "Rockefeller fellow (1924–25); lecturer (1926–27)", years: "1924–1927", kind: university, certainty: 1.0, cites: [{source: S3, locator: "paragraphs 3–4"}, {source: S2, locator: "1924–1926 paragraphs"}], how_known: "Two sources."}
  - {value: "University of Leipzig", role: "professor of theoretical physics", years: "1927–1941", kind: university, certainty: 1.0, cites: [{source: S3, locator: "paragraph 4"}, {source: S2, locator: "1927 paragraph"}], how_known: "Two sources."}
  - {value: "Kaiser Wilhelm Institute for Physics, Berlin", role: director, years: "1941–1945", kind: "research institute", certainty: 1.0, cites: [{source: S3, locator: "paragraph 6"}, {source: S2, locator: "1941"}], how_known: "Two sources."}
  - {value: "German nuclear research programme (Uranverein)", role: "leading scientist", years: "1939–1945", kind: "government or state body", certainty: 0.7, cites: [{source: S2, locator: "Second World War paragraph"}, {source: S1, locator: "opening ('Considerable controversy')"}], how_known: "MacTutor says he headed it; Britannica notes the controversy."}
  - {value: "Max Planck Institute for Physics (Göttingen, then Munich)", role: director, years: "1946–1970", kind: "research institute", certainty: 1.0, cites: [{source: S3, locator: "paragraphs 7, 9"}, {source: S2, locator: "post-war paragraph"}], how_known: "Two sources."}
collaborators:
  - {value: "Arnold Sommerfeld", relation: teacher, note: "doctoral supervisor in Munich", certainty: 1.0, cites: [{source: S1, locator: "'Education'"}, {source: S3, locator: "paragraph 2"}], how_known: "Two sources."}
  - {value: "Max Born", roster_id: born-max, relation: collaborator, note: "Göttingen; matrix mechanics with Jordan", certainty: 1.0, cites: [{source: S1, locator: "'Founding of quantum mechanics'"}, {source: S2, locator: "1925 paragraph"}], how_known: "Two sources."}
  - {value: "Niels Bohr", roster_id: bohr-niels, relation: "mentor or employer", note: "Copenhagen 1924–27; 'physics from Bohr'", certainty: 1.0, cites: [{source: S2, locator: "1924 paragraph"}, {source: S3, locator: "paragraphs 3–4"}], how_known: "Two sources."}
  - {value: "Wolfgang Pauli", roster_id: pauli-wolfgang, relation: collaborator, note: "fellow student; later lattice work", certainty: 1.0, cites: [{source: S2, locator: "university and 1930s paragraphs"}, {source: S4, locator: "p. 472"}], how_known: "Two sources."}
  - {value: "Otto Hahn", roster_id: hahn-otto, relation: collaborator, note: "wartime reactor work", certainty: 0.7, cites: [{source: S2, locator: "Second World War paragraph"}], how_known: "MacTutor."}

review:
  roster_status_reason: {value: "Core in v8 (F 5, all five models).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 80"}], how_known: "Study roster."}
  controversies:
    - {value: "His role in the German nuclear weapons programme during World War II", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Second World War paragraph"}], how_known: "Two sources."}
  data_quality_flags:
    - "S4 is an anonymous English translation of a German lecture; the German text (Universitas 1974; Schritte über Grenzen) was not compared."
    - "S4's access copy is a user upload to the Internet Archive of the JSTOR PDF (apparently the publisher's page images). Its provenance cannot be confirmed from the copy itself, so fields resting on it are capped at 0.7 under CODING_GUIDE §7 (decision P9, 2026-10-02). Reading the article directly on JSTOR (https://www.jstor.org/stable/24457901) would lift the cap."
    - "Britannica read as its first page only (deepen D1: fetch returned 403; S1 retained from prior read)."
    - "S6 English Physics and Beyond / Wilber Quantum Questions p. 38 omit Heisenberg's German clause 'Aber dieser Text würde nicht für mich gelten' after the Pascal Feuer allusion; German Piper text governs for A."
    - "Wikipedia 'devout Christian' [S7] is a secondary label; not used to flip A or primary_system against his own zentrale-Ordnung rephrase and Pascal refusal."
  open_questions:
    - "Cassidy Uncertainty and Elisabeth Heisenberg Inner Exile for adult church membership / practice beyond Wikipedia's Lutheran label."
    - "Compare Guardini lecture German (Universitas 1974 / Schritte über Grenzen) with CrossCurrents English to lift or confirm the §7 cap on S4."
    - "Harper & Row 1971 Physics and Beyond print pages for Kap. 17 English; confirm Wilber's omission of the Pascal-refusal clause against the Harper text."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Richard Beyler"
    citation: "Beyler, Richard. \"Werner Heisenberg.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Werner-Heisenberg."
    url: "https://www.britannica.com/biography/Werner-Heisenberg"
    accessed: 2026-10-02
    reliability_note: "Signed article; first page only. Sections cited by heading."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators, review]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "J J O'Connor and E F Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Werner Karl Heisenberg.\" MacTutor History of Mathematics, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Heisenberg/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Heisenberg/"
    accessed: 2026-10-02
    reliability_note: "Biography drawing on Cassidy (1992); paragraphs counted from 'Werner Heisenberg's father'."
    source_quality: "reference entry"
    used_for: [basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators, review]
  - id: S3
    type: tertiary
    kind: "institutional page"
    author: "Nobel Foundation"
    year: 1965
    citation: "\"Werner Heisenberg – Biographical.\" From Nobel Lectures, Physics 1922–1941. Amsterdam: Elsevier, 1965. NobelPrize.org. https://www.nobelprize.org/prizes/physics/1932/heisenberg/biographical/."
    url: "https://www.nobelprize.org/prizes/physics/1932/heisenberg/biographical/"
    accessed: 2026-10-02
    reliability_note: "Official biography; paragraphs counted from 'Werner Heisenberg was born'."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, timing, institutions, collaborators]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Werner Heisenberg"
    year: 1975
    citation: "Heisenberg, Werner. \"Scientific Truth and Religious Truth.\" CrossCurrents 24, no. 4 (Winter 1975): 463–473 (English translation of the 1973 Guardini Prize lecture, first published in Universitas 16, no. 1, 1974). JSTOR stable URL https://www.jstor.org/stable/24457901; access copy https://archive.org/details/heisenberg-scientifictruthreligious-1975."
    url: "https://archive.org/details/heisenberg-scientifictruthreligious-1975"
    accessed: 2026-10-02
    reliability_note: "His own lecture in published English translation. Access copy: an Internet Archive upload of the JSTOR PDF (page images of the journal). Page numbers are the journal's, printed at the foot of each page. Page 467 was checked on the image. §7 unofficial-copy cap kept (P9)."
    source_quality: "unofficial web copy"
    used_for: [contribution, childhood, worldview, timing, lane_b, collaborators]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Werner Heisenberg"
    year: 1969
    citation: "Heisenberg, Werner. Der Teil und das Ganze: Gespräche im Umkreis der Atomphysik. München: R. Piper, 1969; 6. Aufl. 1986 (ISBN 3-492-03080-7). Kap. 17 „Positivismus, Metaphysik und Religion (1952)“ and Kap. 7 „Erste Gespräche über das Verhältnis von Naturwissenschaft und Religion (1927)“. Access: Würzburg WueCampus scan PDF (Heisenberg_Der_Teil_und_das_Ganze.pdf)."
    url: "https://wuecampus.uni-wuerzburg.de/moodle/pluginfile.php/2854542/mod_resource/content/0/Heisenberg_Der_Teil_und_das_Ganze.pdf"
    accessed: 2026-10-24
    reliability_note: "His own published memoir. Dialogues are reconstructed (Thucydides preface); only his lines used for scores. German checked on the Piper scan; PDF page numbers are the scan's (dialogue at scan pp. 116–117). English Physics and Beyond (Harper & Row 1971) / Wilber Quantum Questions (2001) p. 38 are incomplete on the Pascal clause."
    source_quality: "primary / own words"
    used_for: [worldview, timing, review]
  - id: S7
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: '"Werner Heisenberg." Wikipedia. https://en.wikipedia.org/wiki/Werner_Heisenberg.'
    url: "https://en.wikipedia.org/wiki/Werner_Heisenberg"
    accessed: 2026-10-24
    reliability_note: "Dual-source biography with S1 (P50). Used for Lutheran affiliation label and cross-check; 'devout Christian' secondary label not used to score A or primary_system."
    source_quality: "reference entry"
    used_for: [identity, worldview, heritage, review]
  - id: S8
    type: primary
    kind: "published work by the subject"
    author: "Werner Heisenberg"
    year: 1958
    citation: "Heisenberg, Werner. Physics and Philosophy: The Revolution in Modern Science. New York: Harper & Row, 1958 (Allen & Unwin UK 1959). Ch. 5. Access copy: Internet Archive ost-physics-heisenberg-physicsphilosophy DjVu text."
    url: "https://archive.org/stream/ost-physics-heisenberg-physicsphilosophy/Heisenberg-PhysicsPhilosophy_djvu.txt"
    accessed: 2026-10-24
    reliability_note: "His own Gifford-lectures book. Open IA text; chapter locator used (printed page not stable in the DjVu). Supports A as philosophical critique of Cartesian transcendence; not a creedal profession alone."
    source_quality: "archive scan (OCR only)"
    used_for: [worldview, contribution]
---

# Werner Heisenberg

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Werner Heisenberg (1901–1976), German physicist, founded matrix mechanics in 1925, stated the uncertainty principle in 1927 and won the Nobel Prize in Physics for 1932 [S1, opening; S7]. In his 1973 Guardini Prize lecture he held scientific and religious truth as two languages for one order, grounding ethics in the realm behind phenomena that Plato called the realm of ideas [S4, pp. 463, 467]. In Der Teil und das Ganze Kap. 17 he rephrased belief in a personal God as encounter with the "zentralen Ordnung der Dinge oder des Geschehens" and said Pascal's "Feuer" text would not apply to him [S6, scan pp. 116–117]. System below threshold (PLATO leading, CHRIST named); A 2, B 4, D 2 (all 0.7, support corroborated); C UNKNOWN, E below threshold; mid_basin TODO (A = 2). Deepen D1: chart hollow → filled.

## Life and work

Born in Würzburg, he studied under Sommerfeld in Munich and Born in Göttingen, worked with Bohr in Copenhagen, and held the Leipzig chair from 1927 [S3, paragraphs 1–4]. He directed the Kaiser Wilhelm Institute for Physics in Berlin from 1941 and, after internment in England, the Max Planck Institute for Physics in Göttingen and Munich until 1970 [S3, paragraphs 6–9; S2].

## Contribution and impact

Matrix mechanics (1925), the uncertainty principle (1927), the ortho/para forms of hydrogen and the neutron–proton nucleus (1932) [S1; S2; S3, paragraph 10].

## Childhood and education

His parents (an Evangelical Lutheran father and a mother who had converted from Catholicism) were religious by convention only and brought the children up "to follow Christian ethics but showed total disbelief in the historical side of Christianity" [S2, Biography, paragraph 3]. He read Guardini "as a young person" [S4, p. 463].

## Adult working worldview

"I am convinced of the unassailability of scientific truth in its own sphere", but he could never "doubt the truth of what they are pointing to" [S4, p. 463]. The God of the early scientists "is a God of order, and we do not know whether he is identical with the one to whom we turn in need" [S4, pp. 464–465]. Asked about a "persönlichen Gott", he rephrased to the "zentralen Ordnung" and refused Pascal's personal Feuer text for himself [S6, Kap. 17]. Religion is a poetic language, "in principle as replaceable as any other language" [S4, p. 471], and science and religion must each keep to its sphere [S4, p. 472]. System below threshold (PLATO leading, CHRIST named) after Teil und Ganze / Physics and Philosophy [S6; S8]. Scores: A 2, B 4, D 2 (0.7 each, support corroborated); C UNKNOWN, E below threshold.

## Heritage (context only)

German; Evangelical Lutheran family [S2, Biography, paragraph 3]. Context only.

## Timing

First lasting contribution 1925, at 24 [S3, paragraph 10]. The worldview evidence read is from 1973 [S4].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form partly present; circle partly present (a divine order of the world, placed behind phenomena).

## Open questions

- Cassidy / Elisabeth Heisenberg on adult church practice; Guardini German vs CrossCurrents; Harper Physics and Beyond print vs Wilber English omission.

## Research log

- 2026-10-02: Read Britannica (Beyler, first page), MacTutor, the Nobel biography and the CrossCurrents translation of the Guardini Prize lecture (Internet Archive copy of the JSTOR PDF; OCR checked, p. 467 checked on the image). Physics and Beyond, Der Teil und das Ganze and Physics and Philosophy are lending-only on archive.org.
- 2026-10-24 (deepen D1, queue #79): Würzburg Piper scan of Der Teil und das Ganze Kap. 17 (and Kap. 7) — German primary for A corroboration; Pascal-refusal clause. Physics and Philosophy ch. 5 via ost-physics IA DjVu. Wikipedia EN dual-bio. Edge.org Physics and Beyond English used as finding aid only (speaker attribution). Britannica.com 403 this pass. P47 on S1–S8; A&B&D support corroborated. Chart-moving YES (hollow → filled). No fallacy_catalog (Jason).
