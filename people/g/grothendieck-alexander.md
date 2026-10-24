---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z3; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #140): primary-checked La Clef des songes (Carmona PDF, §§30–31) and Récoltes et Semailles (footnote 302 on creative intelligence / atheist-to-deist). Two own-voice documents → basis consistent_private_letters; DEISM, A 1, B 3 lifted 0.5→0.7 (retrospective self-report cap P20/P29; contested-alt ceiling 0.7). B stays 3 (CODING_GUIDE: lawfulness + stated limited past exceptions = evolutionary sauts; alt 4 kept; sauts-as-B-2 tug logged in coder_notes, not scored as alt). mid_basin BELOW→true @0.7 (A≤1 and B≥3 both @0.7; alt 4 also B≥3, P30 #10). P47 source_quality; P48 support corroborated; P50 Wikipedia EN (birth agrees; death place Saint-Girons vs Saint-Lizier noted). Chart-moving YES (faded→dark eligible). No figures/; no fallacy_catalog."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z5 audit fixes (Z5-03 note, Z5-04 WEAKEN): coder_notes now say Scharlau backs only the lawfulness half of B, and add his 'spiritual desert for decades' line (ch. 24). No value changed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z4 audit fixes (blind audit /workspace/genius_study_audit/gs_a19c474_Z4/run1/), v8's call on the auditor's advice: Z4-05 (FAIL, RQ-Z4-N1): La Clef des songes is a single unpublished document, so under CODING_GUIDE §3 0.5 needs a scholar's backing. Scharlau (Who Is Alexander Grothendieck? Part 3, ch. 24 and ch. 26 note 3) backs the creative-intelligence reading ('Before the eighties, he spoke more of a creative intelligence or creative power than of a personal God'); added as S4, basis of primary_system, A and B now scholarly_reconstruction; values and 0.5 kept. Still plotted."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z3 audit fixes (blind audit /workspace/genius_study_audit/gs_0b45e66_Z3/run1/): Z3-13: labels made to agree with an unpublished typescript: statements stay 'unpublished manuscript', basis of primary_system, A and B now consistent_private_letters (private ceiling 0.7; certainty 0.5 unchanged), S2 kind now other. Esquisse d'un programme dated 1984, not 1983. Values unchanged."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z3, order P32: F 3, rank 144). Basics from MacTutor (O'Connor and Robertson). Own voice: La Clef des songes (1987; typescript transcribed by Mateo Carmona), his retrospective of his relation to God: atheist parents; in March 1944, aged nearly 16, he accepted 'cette Intelligence souveraine, infinie, créatrice de la Vie et ... de l'Univers tout entier, et des lois qui le régissent' and called himself 'déiste' (§§30–31), a view held 'ma vie durant' without doubt; he saw 'aucun signe d'une intervention de Dieu dans le présent' but an Intelligence that 'intervient' at each great evolutionary leap (§30). Span 1953–1970 (end at 0.5), age 25. primary_system DEISM (0.5, alt BELOW_THRESHOLD); A 1 (0.5, alt 0); B 3 (0.5, alt 4); C UNKNOWN; D BELOW_THRESHOLD; E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Plotted (faded) at the next chart refresh. Draft, not reviewed."}

identity:
  id: grothendieck-alexander
  display_name: "Alexander Grothendieck"
  roster:
    canonical_name: "Alexander Grothendieck"
    rank: 144
    F: 3
    models: [Claude, Gemini, GPT]
    band: "core (3–4)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Alexander Grothendieck", certainty: 0.7, cites: [{source: S1, locator: "Biography"}, {source: S6, locator: "lead"}], how_known: "MacTutor; Wikipedia EN agrees. Birth registered as Alexander Raddatz."}
  native_name: {value: "Alexander Grothendieck", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor; 'Alexandre' in France."}
  aliases:
    - {name: "Alexander-Grothendieck", kind: "roster alias"}
    - {name: "Grothendieck-Alexander", kind: "roster alias"}
    - {name: "Alexandre Grothendieck", kind: transliteration}
    - {name: "Alexander Raddatz", kind: "birth name"}

basics:
  birth:
    date: {value: "1928-03-28", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}, {source: S6, locator: "infobox"}], how_known: "P50: MacTutor and Wikipedia EN agree (28 March 1928)."}
    place: {value: "Berlin", modern_name: "Berlin, Germany", polity_then: "Germany (Weimar Republic)", certainty: 0.7, cites: [{source: S1, locator: "Quick Info; Biography"}, {source: S6, locator: "infobox"}], how_known: "P50: MacTutor and Wikipedia EN agree."}
  death:
    date: {value: "2014-11-13", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}, {source: S6, locator: "infobox"}], how_known: "P50: MacTutor and Wikipedia EN agree (13 November 2014)."}
    place: {value: "Saint-Girons", modern_name: "Saint-Girons, Ariège, France", polity_then: "France", certainty: 0.5, cites: [{source: S1, locator: "Quick Info"}, {source: S6, locator: "Retirement into reclusion and death"}], how_known: "P50: MacTutor gives Saint-Girons; Wikipedia EN infobox Saint-Lizier, body 'hospital of Saint-Lizier or Saint-Girons'. Kept MacTutor; 0.5 for the place dispute."}
  first_lasting_contribution_year: {value: 1953, certainty: 0.7, cites: [{source: S1, locator: "Biography (thesis defended 28 February 1953)"}], how_known: "Doctoral thesis on topological tensor products and nuclear spaces, defended 1953; first on the list of his best-known contributions quoted by MacTutor."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "Biography"}], how_known: "1953 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}], how_known: "Germany (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Nancy, Paris (IHES), Montpellier."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "As recorded."}
  languages_of_work: {value: ["French"], certainty: 0.7, cites: [{source: S1, locator: "Biography (titles)"}], how_known: "MacTutor."}
  occupations: {value: ["mathematician", "researcher (CNRS; IHES)", "professor (Montpellier)"], certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}

contribution:
  fields: {value: ["algebraic geometry", "functional analysis", "homological algebra", "category theory"], certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  lasting_original_contributions:
    - {value: "Topological tensor products and nuclear spaces (thesis)", year: 1953, kind: theory, lasting: "first in the list of his best-known contributions quoted by MacTutor", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
    - {value: "Schemes, topoi, étale cohomology and the Séminaire de Géométrie Algébrique at the IHES", year: 1970, kind: "body of work", lasting: "'established the IHES as a world centre of algebraic geometry'; schemes allowed Weil's conjectures to be solved (S1)", certainty: 0.5, cites: [{source: S1, locator: "Biography (IHES 1959–70)"}], how_known: "MacTutor; a body of work across 1959–1970, dated by its end (P30 addendum on ranges); 0.5."}
  evidence_of_impact:
    - {value: "Fields Medal 1966", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  major_works:
    - {value: "Récoltes et Semailles", year: 1985, kind: book, certainty: 0.7, cites: [{source: S1, locator: "Biography (1983–85)"}, {source: S5, locator: "title page"}], how_known: "MacTutor; text itself (circulated MS; Gallimard 2022)."}
    - {value: "La Clef des songes", year: 1987, kind: book, certainty: 0.7, cites: [{source: S2, locator: "§1 (dated 30 April 1987)"}], how_known: "The text itself (MacTutor gives 1986)."}
  honours:
    - {value: "Fields Medal", year: 1966, certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor; declined the Crafoord Prize 1988."}
  definition_fit: {value: "clearly meets", rationale: "Founder of modern algebraic geometry (S1).", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "None: his parents were atheists", certainty: 0.7, cites: [{source: S2, locator: "§27 ('Mes parents étaient athées')"}, {source: S5, locator: "note 302"}], how_known: "His own words (La Clef; ReS)."}
  family_religious_practice: {value: "Fostered 1934–39 by the Hamburg pastor Wilhelm Heydorn", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  parents_and_household:
    - {value: "Alexander Schapiro (Tanaroff), Russian Jewish anarchist, died at Auschwitz 1942", role: father, certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
    - {value: "Johanna (Hanka) Grothendieck, left-wing writer from Hamburg", role: mother, certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  household_circumstances: {value: "Revolutionary émigré parents; foster family in Hamburg; internment camps in France", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  schooling:
    - {value: "Elementary school and Gymnasium in Hamburg", stage: "grammar or secondary school", run_by: other, years: "1934–1939", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
    - {value: "Collège Cévenol, Le Chambon-sur-Lignon (baccalauréat 1945)", stage: "grammar or secondary school", run_by: private, years: "1942–1945", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
    - {value: "University of Montpellier; ENS Paris; Nancy (doctorate 1953)", stage: university, run_by: "state or municipal", years: "1945–1953", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  early_mathematics: {value: "other", note: "dissatisfied with school definitions of length, area and volume; rediscovered the Lebesgue integral at Montpellier", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["German", "French"], certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Berlin and Hamburg, then France from 1939."}
  notable_events:
    - {value: "In March 1944, aged nearly 16, after a talk on evolution by his science teacher Monsieur Friedel, became a 'déiste' and wrote so to his mother", year: 1944, certainty: 0.7, cites: [{source: S2, locator: "§§30–31"}, {source: S5, locator: "note 302"}], how_known: "Two own-voice retrospectives (La Clef dated March 1944 / nearly 16; ReS says age fourteen — slight age discrepancy noted)."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1953–1970", certainty: 0.5, cites: [{source: S1, locator: "Biography"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Mathematical laws are 'part of the very nature of God', accessible to reason alone (1987 note); deist creative-intelligence reading of evolution from 1944", certainty: 0.7, cites: [{source: S2, locator: "§31, note 72"}, {source: S5, locator: "note 302"}], how_known: "Own words; note 72 is time-of-writing on math laws; deism of 1944 is retrospective for the span."}
  primary_system:
    value: DEISM
    basis: consistent_private_letters
    certainty: 0.7
    cites: [{source: S2, locator: "§§30–31"}, {source: S5, locator: "note 302"}, {source: S4, locator: "ch. 24; ch. 26 note 3"}]
    how_known: "Deepen D1: two own-voice documents (La Clef §§30–31; ReS note 302) call the 1944 turn 'déiste' / 'intelligence créatrice' and say the intellectual understanding persisted through the math years (ReS: refined after leaving the scene in 1970). Private ceiling: more than one unpublished/circulated MS → consistent_private_letters 0.7 (CODING_GUIDE §3). Retrospective about the span after the 1976 theism shift → 0.7 cap (P20/P29); not hedged ('sans ... le moindre doute'). Scharlau (S4) still backs the creative-intelligence reading. P27: he set the Creator far from OT/Gospel revelation and saw no present intervention."
    rationale: "DEISM use_when: creator known by reason (design/evolution), rejects biblical revelation and present miracles as sources. Alt BELOW_THRESHOLD: P27 if 'declines to contest' revelation is read as insufficient rejection. Not coded on post-1976 mystical theism (outside the span; changes_over_life)."
    alternatives:
      - {value: BELOW_THRESHOLD, note: "If the 1944–70 stance is read as not clearly rejecting revelation (P27).", cites: [{source: S2, locator: "§31"}]}
  secondary_system: {value: UNKNOWN, how_known: "None for the span."}
  candidate_codes_considered:
    - {code: DEISM, reason: "Coded at 0.7 (S2 §§30–31; S5 note 302)."}
    - {code: ATHE, reason: "Rejected: atheist only before 1944, by his account."}
    - {code: BUDDH, reason: "Rejected: contact with Buddhist monks in the 1970s, after the span (S2; S5)."}
  lio_axes:
    A_locus:
      value: 1
      basis: consistent_private_letters
      certainty: 0.7
      support: corroborated
      cites: [{source: S2, locator: "§31"}, {source: S5, locator: "note 302"}, {source: S4, locator: "ch. 24; ch. 26 note 3"}]
      how_known: "Deepen D1: two own-voice texts. 'cette Intelligence souveraine, infinie, créatrice de la Vie et ... de l'Univers tout entier, et des lois qui le régissent' (S2 §31); ReS note 302: 'présence d'une intelligence créatrice à l'oeuvre dans l'Univers'. Transcendent creator, thin/distant for the span (not the later Rêveur theism). Retrospective cap 0.7."
      rationale: "A transcendent creator who stays apart from daily life: 1 (as DEISM). Alternative 0: an 'Intelligence' with an 'Intention' / Dessein (S2 §30)."
      alternatives:
        - {value: 0, note: "A personal creator with a Design (Intention/Dessein in §30).", cites: [{source: S2, locator: "§30"}]}
    B_cause:
      value: 3
      basis: consistent_private_letters
      certainty: 0.7
      support: corroborated
      cites: [{source: S2, locator: "§§30–31"}, {source: S5, locator: "note 302"}, {source: S4, locator: "ch. 24"}]
      how_known: "Deepen D1: own-voice nature account (P16), not math career alone (P35). Creator of the laws (S2 §31); 'aucun signe d'une intervention de Dieu dans le présent' (S2 §31); same Intelligence 'intervient ... lors de chacun des grands \"sauts\" qualitatifs' of evolution (S2 §30) — a stated limited past exception. ReS note 302 corroborates creative intelligence in the Universe from 1944 through the math years. Two documents → 0.7. Scharlau backs the lawfulness half."
      rationale: "B 3: stated general lawfulness with stated limited past exceptions (evolutionary sauts / creation-scale; CODING_GUIDE B 3). Alternative 4: stark non-interference reading of 'aucun signe ... dans le présent'. Sauts-as-B-2 tug noted in coder_notes (not scored as alt — B 3 definition already covers rare past exceptions)."
      alternatives:
        - {value: 4, note: "'aucun signe d'une intervention de Dieu dans le présent'.", cites: [{source: S2, locator: "§31"}]}
    C_ledger: {value: UNKNOWN, how_known: "The Creator was far from 'the God of ... Retribution' (§31), a lead only (P19)."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "Reason alone grasps the Creator (§30); revelation not discussed for this period as a ranked authority."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Nothing further read for the span; not scored from mathematics alone (P19)."}
  mid_basin:
    value: true
    certainty: 0.7
    cites: [{source: S2, locator: "§§30–31"}, {source: S5, locator: "note 302"}]
    how_known: "Deepen D1: A 1 ≤ 1 and B 3 ≥ 3, both at 0.7; named B alt 4 also satisfies B ≥ 3 (P30 #10). Deists usually pass (METHOD §1.1)."
  statements:
    - text: "Je comprenais bien que ce “Dieu” qu’on mettait à toutes les sauces pour Lui faire avaliser tout ce qu’on voulait, Il était en tous cas cette Intelligence souveraine, infinie, créatrice de la Vie et (cela allait alors de soi) créatrice aussi de l’Univers tout entier, et des lois qui le régissent."
      cites: [{source: S2, locator: "§31"}]
      date: "1987"
      context: "La Clef des songes, 'Les retrouvailles perdues': his conversion of March 1944, aged nearly 16."
      axes: [A_locus, B_cause]
      kind: "unpublished manuscript"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Carmona provisional edition (geotoppos.org/divers/clef.pdf); primary-checked this pass. Retrospective (P20)."
    - text: "Rien dans mon expérience directe ne me conduisait à penser que le Créateur, une fois mis en marche l’immense Manège de la Création, continuait encore à s’occuper de ce qui s’y passe et à y participer si peu que ce soit. [...] je ne percevais aucun signe d’une intervention de Dieu dans le présent."
      cites: [{source: S2, locator: "§31"}]
      date: "1987"
      context: "Same passage, on the deism of 1944 onward."
      axes: [B_cause]
      kind: "unpublished manuscript"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "As above."
    - text: "Elle intervient de façon irrécusable, pour le moins, lors de chacun des grands “sauts” qualitatifs, des “innovations évolutionnistes”..."
      cites: [{source: S2, locator: "§30"}]
      date: "1987"
      context: "La Clef des songes §30: the same Creative Intelligence at evolutionary leaps."
      axes: [B_cause]
      kind: "unpublished manuscript"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Stated limited past exception supporting B 3 (not present miracles)."
    - text: "Par l’éducation reçue par mes parents j’ai été athée (avec une nuance antireligieuse) jusqu’à l’âge de quatorze ans. Un exposé remarquable de mon prof de sciences naturelles, sur l’histoire de l’évolution de la vie sur la terre, m’a fait alors comprendre, sans possibilité du moindre doute, la présence d’une intelligence créatrice à l’oeuvre dans l’Univers. Cette compréhension, qui restait alors au niveau du seul intellect, s’est élargie et s’est affinée au cours de ma maturation ultérieure, se poursuivant après mon départ de la scène mathématique en 1970."
      cites: [{source: S5, locator: "note 302"}]
      date: "1985"
      context: "Récoltes et Semailles, note on not belonging to a confession; corroborates the La Clef conversion story and that the intellectual deism ran through the math years."
      axes: [A_locus, B_cause]
      kind: "unpublished manuscript"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Age 'quatorze' vs La Clef March 1944 / nearly 16 — slight discrepancy; substance agrees. Circulated MS (private ceiling)."
    - text: "Alors que je me disais “athée” jusque-là, me voilà donc soudain changé de catégorie - dorénavant, je me dirai “déiste” !"
      cites: [{source: S2, locator: "§31"}]
      date: "1987"
      context: "La Clef des songes §31: self-label after the 1944 talk."
      axes: [A_locus]
      kind: "unpublished manuscript"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Own-voice code word for primary_system DEISM."
  changes_over_life:
    - {value: "Atheist upbringing; deist from 1944 (intellectual); mystical theism from 1976 (meditation, dreams: 'Dieu est le Rêveur')", certainty: 0.7, cites: [{source: S2, locator: "§§17, 27, 31"}, {source: S5, locator: "note 302"}], how_known: "Own retrospectives; 1976 shift after the span, so span evidence from 1980s texts is retrospective self-report (0.7 cap)."}
  coder_notes: "Span end 1970 (IHES body of work) at 0.5; Esquisse d'un programme (1984) is a later candidate. Deepen D1: B kept at 3 (not flipped to 2) because CODING_GUIDE B 3 covers lawfulness plus stated limited past exceptions (sauts / creation-scale); 'aucun signe ... dans le présent' is alt 4. A B-2 reading of the sauts as ongoing mixed intervention was considered and rejected for the span deism. Scharlau (S4) still backs mainly the lawfulness half and reports 'spiritual desert for decades' until 1970 — in tension with 'ma vie durant' but ReS note 302 clarifies intellectual-level persistence through the math years. Chart-moving: A and B both now 0.7 (was faded). figures/ not refreshed this pass."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Russian Jewish (father) and German (mother)", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  religious_heritage_by_birth: {value: "Jewish (paternal); none in practice", certainty: 0.5, cites: [{source: S1, locator: "Biography"}, {source: S2, locator: "§27"}], how_known: "MacTutor; his own account."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1953–1970", certainty: 0.5, cites: [{source: S1, locator: "Biography"}], how_known: "Thesis (1953) to the end of the IHES period (1970) (P29, P30); end at 0.5."}
  age_at_first_lasting_contribution: {value: 25, certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}], how_known: "1953 − 1928 = 25 (P30 year difference; he was 24 at the February 1953 defence)."}
  first_evidence_of_lio_type_views: {value: "1944 (by his 1980s accounts)", certainty: 0.7, cites: [{source: S2, locator: "§31"}, {source: S5, locator: "note 302"}], how_known: "Two retrospectives."}
  lio_views_relative_to_major_work: {value: "before major work", certainty: 0.7, cites: [{source: S2, locator: "§31"}, {source: S5, locator: "note 302"}], how_known: "Deist from 1944."}
  worldview_during_major_work: {value: "Deist at intellectual level, of little personal consequence to him until after 1970", certainty: 0.7, cites: [{source: S2, locator: "§31"}, {source: S5, locator: "note 302"}], how_known: "Retrospectives; ReS: 'au niveau du seul intellect' until after leaving mathematics."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Algebraic geometry (S1).", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  form_acquired: {value: "adulthood, before major work", certainty: 0.5, cites: [{source: S1, locator: "Biography"}], how_known: "Montpellier and Nancy."}
  circle_present: {value: "no", rationale: "A creator apart from daily life during the span (S2 §31).", certainty: 0.7, cites: [{source: S2, locator: "§31"}, {source: S5, locator: "note 302"}], how_known: "Coder's reading of the span deism."}
  reading: "Deist creator of the laws; mathematics as 'part of the nature of God' only in the 1987 note (time-of-writing)."
  notes: "Lane A and Lane B kept separate (P49)."

institutions:
  - {value: "Institut des Hautes Études Scientifiques", role: professor, years: "1959–1970", kind: other, certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  - {value: "University of Montpellier", role: professor, years: "1973–1988", kind: university, certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
collaborators:
  - {value: "Jean Dieudonné", relation: teacher, note: "Nancy", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  - {value: "Laurent Schwartz", relation: teacher, note: "Nancy", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  - {value: "Jean-Pierre Serre", relation: collaborator, note: "fellow student; Fields report", certainty: 0.7, cites: [{source: S1, locator: "Biography; references"}], how_known: "MacTutor."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 144"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Worldview for the span known from 1980s retrospectives written after the 1976 theism shift (P20 0.7 cap)."
    - "ReS age 'quatorze' vs La Clef March 1944 / nearly 16 — slight discrepancy."
    - "Death place: Saint-Girons (MacTutor) vs Saint-Lizier (Wikipedia infobox)."
  open_questions:
    - "Span end (1970 or 1984)."
    - "Any contemporaneous 1950s–60s letter stating the deism (would confirm without retrospective cap)."

sources:
  - id: S1
    type: secondary
    kind: database
    author: "J J O'Connor and E F Robertson"
    citation: "O'Connor, J J, and E F Robertson. \"Alexander Grothendieck.\" MacTutor History of Mathematics, University of St Andrews (updated November 2014). https://mathshistory.st-andrews.ac.uk/Biographies/Grothendieck/"
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Grothendieck/"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Signed biographical database entry."
    used_for: [identity, basics, contribution, childhood, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: other
    author: "Alexandre Grothendieck"
    citation: "Grothendieck, Alexandre. La Clef des songes, ou Dialogue avec le bon Dieu (typescript, 1987). Provisional transcription ed. Mateo Carmona. https://geotoppos.org/divers/clef.pdf"
    url: "https://geotoppos.org/divers/clef.pdf"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Own unpublished typescript in Carmona's provisional transcription; §§30–31 primary-checked this pass (pdftotext of the PDF)."
    used_for: [childhood, worldview, heritage, timing, lane_b]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [review]
  - id: S4
    type: secondary
    kind: "scholarly book"
    author: "Winfried Scharlau, tr. Melissa Schneps"
    citation: "Scharlau, Winfried. Who Is Alexander Grothendieck? Anarchy, Mathematics, Spirituality, Solitude. Part 3: Spirituality, tr. Melissa Schneps (German: Wer ist Alexander Grothendieck? Teil 3: Spiritualität). Chapters 24 ('La Clef des Songes') and 26 ('Les Mutants'), via the Grothendieck Circle. https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/Spirituality/Spirituality24.pdf"
    url: "https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/Spirituality/Spirituality24.pdf"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Published biography by a mathematician-biographer; chapter PDFs of the English translation re-read this pass."
    used_for: [worldview]
  - id: S5
    type: primary
    kind: other
    author: "Alexandre Grothendieck"
    citation: "Grothendieck, Alexandre. Récoltes et Semailles: Réflexions et témoignage sur un passé de mathématicien (circulated typescript, ca. 1983–1986; Gallimard 2022). Note 302 (on not belonging to a confession). PDF used: https://matematicas.unex.es/~navarro/res/res.pdf"
    url: "https://matematicas.unex.es/~navarro/res/res.pdf"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Own circulated autobiographical MS; note 302 primary-checked. Private ceiling (not published by him in life). Gallimard 2022 is posthumous."
    used_for: [childhood, worldview, timing]
  - id: S6
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Alexander Grothendieck.\" English Wikipedia (accessed 2026-10-24). https://en.wikipedia.org/wiki/Alexander_Grothendieck"
    url: "https://en.wikipedia.org/wiki/Alexander_Grothendieck"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "P50 dual bio: birth date/place and death date agree with MacTutor; death place disputed (Saint-Lizier vs Saint-Girons)."
    used_for: [identity, basics, review]
---

# Alexander Grothendieck

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Alexander Grothendieck (1928–2014), mathematician [S1]. Deepen D1: DEISM (0.7, alt BELOW_THRESHOLD); A 1 (0.7, alt 0); B 3 (0.7, alt 4); mid_basin true (0.7). Chart-moving YES (was faded @0.5; figures/ not refreshed here).

## Life and work

Berlin, Hamburg, French camps, Montpellier, Nancy, IHES [S1].

## Contribution and impact

Nuclear spaces; schemes and the IHES school; Fields Medal 1966 [S1].

## Childhood and education

Atheist parents; deist at nearly 16 by his own account [S2, §§27, 31; S5, note 302].

## Adult working worldview

Deist (intellectual) during the span, by two 1980s retrospectives [S2, §31; S5, note 302].

## Heritage (context only)

Russian Jewish and German [S1].

## Timing

1953–1970, from age 25 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle in the span [S2].

## Open questions

- Span end.
- Contemporaneous 1950s–60s deism letter.

## Research log

- 2026-10-19: Read MacTutor and La Clef des songes §§27–31.
- 2026-10-24: Deepen D1 — re-read La Clef Carmona PDF §§30–31; ReS note 302; Scharlau ch. 24; Wikipedia EN P50.
