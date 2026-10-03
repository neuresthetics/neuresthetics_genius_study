---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 7
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, third batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (third batch, RUNBOOK §1 order). Basics from Britannica (Beyler, first page), MacTutor and the Nobel biography. Worldview from his own Guardini Prize lecture (Munich 1973), read in the English translation 'Scientific Truth and Religious Truth', CrossCurrents 24:4 (1975), 463–473, as a scan of the JSTOR page images. primary_system PLATO at 0.7 (CHRIST named). A 2 (0.7), B 4 (0.7), D 2 (0.7); C, E BELOW_THRESHOLD; mid_basin TODO (A = 2). Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Self-described relation lowered from 1.0 to 0.7 under the CODING_GUIDE §7 unofficial-web-copy cap (S4 read from a user upload of the JSTOR PDF, not JSTOR itself)."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "record_version corrected to 3 (the 1f3c4bf fix did not raise it). Decision P9: the §7 cap (0.7) on fields resting on the JSTOR-PDF copy is kept, since its provenance cannot be confirmed from the copy; reading the article on JSTOR would lift it. Notes only; no score changed. Schema 1.1 → 1.2."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 3 (two blind runs at d9903b7). #33 (run 1; verified on the CrossCurrents text): primary_system PLATO (0.7) → BELOW_THRESHOLD, with PLATO (leading) and CHRIST as candidates. PLATO's use_when needs the intelligible reality to be the ultimate origin of both existence and values; the lecture makes the realm behind phenomena the ground of ethics and trust (p. 467), not of existence, and pairs Plato with the Bible (p. 467) while speaking from inside the Christian 'linguistic area' (p. 471). PLATO's do_not_use_when sends Platonism inside Christianity to the host religion unless the Platonism clearly dominates, which the record does not show; CHRIST's use_when (specifically Christian belief) is not met either. No axis changed; mid_basin unchanged (TODO, A = 2). #41 (run 2): nominal affiliation reworded; MacTutor gives the parents' affiliation, not his own. #44 (run 2): Nobel biography locators recounted from 'Werner Heisenberg was born': the 1925 / Nobel sentence is paragraph 10 (was 7), Berlin paragraph 6 (was 5), the Max Planck Institute paragraphs 7 and 9 (were 6, 8). Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02). Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs; BELOW_THRESHOLD vs UNKNOWN per P19; kind lists (P21: research institute, school stage and run_by, scholarly edition). Full before → after list: reports/stage3_rulings_changes.csv. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "P30 rule 5 age sweep: ages recomputed as event year − birth year, with no month adjustment (scripts/recompute_ages.py; every change is in reports/p30_age_changes.csv). No other value changed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Span alignment (P29, P30 and its addendum): timing.major_work_period checked, 1925–1932 unchanged; worldview.working_years 1922–1976 → 1925–1932, equal to the span (P30 addendum f); 4 headline values rest on evidence outside the span and are left unchanged for a ruling (open questions). Listed in reports/p30_span_alignment.csv. Not reviewed."}

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
    - {value: "Born to an Evangelical Lutheran family (father Lutheran; mother converted from Catholicism at marriage); his own baptism and membership are not stated", years: "1901–", role: "member by upbringing", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 3"}], how_known: "Inferred from the parents' affiliation: MacTutor says the father 'was an Evangelical Lutheran' and the mother had converted, and that the parents 'brought up their children to follow Christian ethics'. MacTutor says nothing of Werner's own baptism or membership; adult membership not checked in the sources read (lens audit batch 3, #41)."}
  self_described_science_religion_relation:
    value: "Two truths in two languages: 'I am convinced of the unassailability of scientific truth in its own sphere', yet he could never dismiss religious thinking or 'doubt the truth of what they are pointing to'; religion is a poetic language of images and parables for the order behind phenomena and the basis of ethics, and the two languages must not be confused."
    certainty: 0.7
    cites: [{source: S4, locator: "pp. 463, 467, 471–472"}]
    how_known: "His own published lecture (1973; English 1975), checked on the journal page images in a user-uploaded copy of the JSTOR PDF. Capped at 0.7 under CODING_GUIDE §7: the copy is unofficial and its wording was not checked on JSTOR itself (lending/subscription). Decision P9 (2026-10-02) keeps the cap because the copy's provenance cannot be confirmed from the copy itself; reading the article directly on JSTOR (stable/24457901) would lift it."
  primary_system:
    value: BELOW_THRESHOLD
    cites: [{source: S4, locator: "pp. 464–465, 467, 471"}]
    how_known: "His own public lecture. The divine is a 'God of order', and 'we do not know whether he is identical with the one to whom we turn in need' (pp. 464–465); religious precepts rest 'on tht realm behind it, which Plato referred to as the realm of ideas, and which the Bible speaks of in the words “God is a spirit.”' (p. 467); religion's images help us understand 'the ordered world perceptible behind phenomena', and its language 'is in principle as replaceable as any other language' (p. 471). Applying the PLATO file as written (lens audit batch 3, #33): its use_when needs an intelligible reality that is 'the ultimate origin of both existence and values'; the lecture makes the realm behind phenomena the basis of ethics and of trust (p. 467) but says nothing of it as the origin of existence, and the one sentence naming Plato names the Bible with him (p. 467). Its do_not_use_when sends Platonism inside Christianity to the host religion unless the Platonism clearly dominates; he speaks of 'the European world moulded by the Christian religion' and of being born into 'a definite linguistic area' (p. 471), and the replaceability of religious language argues against a specific confession, not for Platonism. CHRIST's use_when needs specifically Christian belief (Christ, scripture, creeds, church), which the lecture does not affirm. So neither code reaches 0.5 on this one lecture."
    note: "Candidates: PLATO (leading) and CHRIST. Was PLATO at 0.7 (written_profession) until the lens audit batch 3 fix. Reading Der Teil und das Ganze (1969) or Physics and Philosophy (1958) for his own Platonist passages on the origin of things, or a scholar's study of his religion, could lift PLATO to 0.5 or above."
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
      cites: [{source: S4, locator: "pp. 464–465, 467, 471"}]
      how_known: "His own lecture; the reading is mixed, so 0.7."
      rationale: "Mixed. A 'God of order' who makes visible 'partial structures from the divine order of the world' (p. 471) leans to the immanent pole; but the order is located 'behind' the visible world in Plato's realm of ideas ('God is a spirit', p. 467), and whether this God is 'the one to whom we turn in need' is left open (pp. 464–465), so neither a transcendent person nor identity with the world is asserted. Named alternatives: 3 if the 'divine order of the world' is read as immanent; 1 if the open question about the God of petition is resolved toward a person."
    B_cause:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "p. 465"}, {source: S1, locator: "'Uncertainty principle'"}]
      how_known: "His own lecture and Britannica's account of his physics; a named alternative, so 0.7."
      rationale: "Scored on his account of nature (P6), his working physics. Laws and repeatable experiment rule: 'The repeatable nature of experiments finally always permits a consensus on the true behaviour of nature' (p. 465), and modern science 'has brought to light laws of wide scope' (p. 472). His uncertainty principle made 'absolute causal determinism' impossible and atomic theory probabilistic (S1), which is statistical law, not miracle or exemption. Named alternative: 3, if the 'limits' of causal description 'through experience with atoms' (p. 465) are read as a standing exception."
    C_ledger: {value: UNKNOWN, how_known: "He makes religion 'the basis of ethics' (p. 467) but says nothing in what was read about judgement, afterlife, or reward and punishment of persons.", note: "Gap: Der Teil und das Ganze (1969), chs. 7 and 17, and Physics and Philosophy (1958); lending-only scans."}
    D_authority:
      value: 2
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "pp. 463, 471–472"}]
      how_known: "His own lecture; a named alternative, so 0.7."
      rationale: "Two domains, each with its own authority, so D 2 (same-pattern rule, as for Einstein, Planck and Galileo). 'The correctness of proven scientific results cannot sensibly be doubted by religious thinking, and, vice versa, the ethical demands which proceed from the heart of religious thinking should not be dissolved by extreme rational arguments from the sphere of science' (p. 472); 'We must not confuse both languages' (p. 471). Named alternative: 3, since on questions of fact science decides and religious language is 'not scientific' (p. 470)."
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). The lecture speaks of one 'divine order of the world' and laws of wide scope, but nothing read addresses whether the same rules govern every kind of being or whether any group is favoured in events; the Russians' experience of 'the workings of God in the world' (p. 468) is his report of Dostoevsky's characters, not his own view."}
  mid_basin: {value: TODO, how_known: "A_locus = 2 at 0.7 and B_cause = 4 at 0.7. Both axes are scored at 0.7 but A falls between the branches: the P4 test has no branch for A_locus = 2 (CODING_GUIDE §6).", note: "Same case as Planck; needs a decision, not more evidence."}
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
  changes_over_life: []
  coder_notes: "PANENT is a stub system file (flag); PLATO and CHRIST are drafts. The lecture was given in German (published in Universitas, 1974) and is read in the anonymous English translation of CrossCurrents (1975); quotations are that translation. S4's access copy is an Internet Archive upload of the JSTOR PDF (page images with JSTOR's cover sheet); quotations were checked on its OCR and, for p. 467, on the page image. Heisenberg's memoir Der Teil und das Ganze (1969) reconstructs conversations decades later; its dialogues were not read and would need care (other speakers' lines are not his views). changes_over_life is empty after research: no dated change of belief in what was read."

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
  first_evidence_of_lio_type_views: {value: "Guardini Prize lecture (lawful order and two truths)", year: 1973, certainty: 1.0, cites: [{source: S4, locator: "pp. 463–472"}], how_known: "Earliest dated statement read; earlier views (Der Teil und das Ganze, 1969) not read."}
  lio_views_relative_to_major_work: {value: "unclear", rationale: "The statement read is from 1973, long after the major work; his memoir places such conversations in 1927 and 1952 but was not read.", certainty: 0.5, cites: [{source: S4, locator: "p. 463"}], how_known: "Dates."}
  worldview_during_major_work: {value: TODO}

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
    - "Britannica read as its first page only."
  open_questions:
    - "Read Der Teil und das Ganze (1969), chs. 7 and 17, and Physics and Philosophy (1958), keeping his own lines apart from the reconstructed lines of Pauli, Dirac and Bohr."
    - "Check his adult church membership (Cassidy, Uncertainty; Elisabeth Heisenberg, Inner Exile)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Richard Beyler"
    citation: "Beyler, Richard. \"Werner Heisenberg.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Werner-Heisenberg."
    url: "https://www.britannica.com/biography/Werner-Heisenberg"
    accessed: 2026-10-02
    reliability_note: "Signed article; first page only. Sections cited by heading."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators, review]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "J J O'Connor and E F Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Werner Karl Heisenberg.\" MacTutor History of Mathematics, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Heisenberg/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Heisenberg/"
    accessed: 2026-10-02
    reliability_note: "Biography drawing on Cassidy (1992); paragraphs counted from 'Werner Heisenberg's father'."
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
    used_for: [identity, basics, contribution, childhood, worldview, timing, institutions, collaborators]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Werner Heisenberg"
    year: 1975
    citation: "Heisenberg, Werner. \"Scientific Truth and Religious Truth.\" CrossCurrents 24, no. 4 (Winter 1975): 463–473 (English translation of the 1973 Guardini Prize lecture, first published in Universitas 16, no. 1, 1974). JSTOR stable URL https://www.jstor.org/stable/24457901; access copy https://archive.org/details/heisenberg-scientifictruthreligious-1975."
    url: "https://archive.org/details/heisenberg-scientifictruthreligious-1975"
    accessed: 2026-10-02
    reliability_note: "His own lecture in published English translation. Access copy: an Internet Archive upload of the JSTOR PDF (page images of the journal). Page numbers are the journal's, printed at the foot of each page. Page 467 was checked on the image."
    used_for: [contribution, childhood, worldview, timing, lane_b, collaborators]
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

# Werner Heisenberg

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Werner Heisenberg (1901–1976), German physicist, founded matrix mechanics in 1925, stated the uncertainty principle in 1927 and won the Nobel Prize in Physics for 1932 [S1, opening]. In his 1973 Guardini Prize lecture he held that scientific and religious truth are two languages for one order, grounding ethics in "tht realm behind" the visible world "which Plato referred to as the realm of ideas, and which the Bible speaks of in the words “God is a spirit.”" [S4, pp. 463, 467]. System below threshold (PLATO leading, CHRIST named); A 2, B 4, D 2 (all 0.7); C UNKNOWN, E below threshold; mid_basin TODO (A = 2).

## Life and work

Born in Würzburg, he studied under Sommerfeld in Munich and Born in Göttingen, worked with Bohr in Copenhagen, and held the Leipzig chair from 1927 [S3, paragraphs 1–4]. He directed the Kaiser Wilhelm Institute for Physics in Berlin from 1941 and, after internment in England, the Max Planck Institute for Physics in Göttingen and Munich until 1970 [S3, paragraphs 6–9; S2].

## Contribution and impact

Matrix mechanics (1925), the uncertainty principle (1927), the ortho/para forms of hydrogen and the neutron–proton nucleus (1932) [S1; S2; S3, paragraph 10].

## Childhood and education

His parents (an Evangelical Lutheran father and a mother who had converted from Catholicism) were religious by convention only and brought the children up "to follow Christian ethics but showed total disbelief in the historical side of Christianity" [S2, Biography, paragraph 3]. He read Guardini "as a young person" [S4, p. 463].

## Adult working worldview

"I am convinced of the unassailability of scientific truth in its own sphere", but he could never "doubt the truth of what they are pointing to" [S4, p. 463]. The God of the early scientists "is a God of order, and we do not know whether he is identical with the one to whom we turn in need" [S4, pp. 464–465]. Religion is a poetic language, "in principle as replaceable as any other language" [S4, p. 471], and science and religion must each keep to its sphere [S4, p. 472]. System below threshold: PLATO's use_when needs the realm of ideas as the origin of existence as well as values, and Platonism inside a Christian frame goes to the host religion unless it clearly dominates [S4, pp. 467, 471]. Scores: A 2, B 4, D 2 (0.7); C UNKNOWN, E below threshold.

## Heritage (context only)

German; Evangelical Lutheran family [S2, Biography, paragraph 3]. Context only.

## Timing

First lasting contribution 1925, at 24 [S3, paragraph 10]. The worldview evidence read is from 1973 [S4].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form partly present; circle partly present (a divine order of the world, placed behind phenomena).

## Open questions

- Span check (2026-10-02, P29/P30): A_locus (2 at 0.7), B_cause (4 at 0.7), D_authority (2 at 0.7), mid_basin (TODO) rest on evidence outside the new span 1925–1932. Values left unchanged pending a ruling; details in reports/p30_span_alignment.csv.
- Der Teil und das Ganze (1969) and Physics and Philosophy (1958); his adult church membership.

## Research log

- 2026-10-02: Read Britannica (Beyler, first page), MacTutor, the Nobel biography and the CrossCurrents translation of the Guardini Prize lecture (Internet Archive copy of the JSTOR PDF; OCR checked, p. 467 checked on the image). Physics and Beyond, Der Teil und das Ganze and Physics and Philosophy are lending-only on archive.org.
