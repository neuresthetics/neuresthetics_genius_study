---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch T)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages and page images"
  collected_on: 2026-10-18
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #112 / F4 rank 113). Goals: corroborate A and B (hollow→filled); resolve B alt if stronger evidence. Read Rettung der Göttlichen Offenbahrung (1747) in French 1805 Défense de la révélation (IA dfensedelarv00eule; S5) with English E092trans (Euler Archive via Wayback) for navigation — independent of the Lettres. Dual bio: Britannica (S1) + Wikipedia EN (S6) (P50). P47 source_quality on S1–S6. A stays 0 @0.7 support single→corroborated (S3 Lettres + S5 Rettung: monde ouvrage de sa toute-puissance; opération immédiate de Dieu; résurrection miracle de Dieu seul). B stays 3 @0.7 alt 2 support single→corroborated (S3 + S5: lois du mouvement; miracle as exceptional change to the world-state; P27 T1 free-will / conceded present-tense miracles keep value 3 and alt 2 — Rettung does not force flip to 2). D 1 @0.7 alt 2 support single→corroborated (S3 + S5 revelation over freethinker objections). E stays 2 @0.7 alt 3 support single. primary CHRIST @0.7 unchanged (Rettung defends Christian revelation / résurrection). first_evidence_of_lio_type_views 1768→1747 (Rettung). mid_basin true @0.7 unchanged. Chart-moving YES: hollow→filled; already dark. No fallacy_catalog. No figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch T, order P32: F 4, rank 113). Basics from Britannica (Boyer) and MacTutor (O'Connor and Robertson). Worldview from Lettres à une princesse d'Allemagne (St Petersburg 1768–72), vol. 2, Lettres LXXXVII, LXXXVIII and XC, read in the page images of the 1775 reprint (vol. 2, Internet Archive) and compared with Hunter's English translation (1795). Scientist (P30: Mechanica, fluid equations). primary_system CHRIST (0.7, alt CLTHEI); A 0 (0.7); B 3 (0.7, alt 2; P27 free-spirits anchor, miracles conceded); C BELOW_THRESHOLD; D 1 (0.7, alt 2); E 2 (0.7, alt 3); mid_basin true (0.7). Plotted. Draft, not reviewed."}

identity:
  id: euler-leonhard
  display_name: "Leonhard Euler"
  roster:
    canonical_name: "Leonhard Euler"
    rank: 113
    F: 4
    models: [Claude, DeepSeek, Gemini, Grok]
    band: "core (3–4)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Leonhard Euler", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Quick Info"}], how_known: "Britannica and MacTutor agree."}
  native_name: {value: "Leonhard Euler", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "German; same as the display name."}
  aliases:
    - {name: "Euler-Leonhard", kind: "roster alias"}

basics:
  birth:
    date: {value: "1707-04-15", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Quick Info"}], how_known: "Britannica and MacTutor agree."}
    place: {value: "Basel, Switzerland", modern_name: "Basel, Switzerland", polity_then: "Swiss Confederacy", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Quick Info"}], how_known: "Britannica and MacTutor agree; brought up in Riehen (S2)."}
  death:
    date: {value: "1783-09-18", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Quick Info; last paragraph of the life"}], how_known: "Britannica and MacTutor agree."}
    place: {value: "St Petersburg, Russia", modern_name: "Saint Petersburg, Russia", polity_then: "Russian Empire", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Quick Info"}], how_known: "Britannica and MacTutor agree."}
  first_lasting_contribution_year: {value: 1735, certainty: 0.7, cites: [{source: S2, locator: "Basel problem paragraph"}], how_known: "Solution of the Basel problem, 'Euler showed in 1735 that ζ(2) = π²/6' (S2), 'the result that brought Euler the most fame in his young days'; Mechanica (1736) follows a year later. Earlier papers (1726–27) are not listed as lasting."}
  era_bucket: {value: "1600 to 1749", certainty: 0.7, cites: [{source: S2, locator: "Basel problem paragraph"}], how_known: "1735 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Switzerland (P3)."}
  region_of_work: {value: "Eastern Europe", certainty: 0.5, cites: [{source: S2, locator: "St Petersburg and Berlin paragraphs"}], how_known: "Split: St Petersburg 1727–41 and 1766–83 (about 31 years, with Mechanica and the Basel problem), Berlin 1741–66 (25 years, with the Introductio and the fluid equations). Coder's call by years; Western Europe (Germany) is the alternative."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S2, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Latin", "French", "German"], certainty: 0.7, cites: [{source: S2, locator: "works named"}, {source: S3, locator: "title page, vol. 2"}], how_known: "Latin treatises (Mechanica, Introductio), French Lettres (S3); German autobiographical writings and letters (S2)."}
  occupations: {value: ["mathematician", "physicist", "academician (St Petersburg and Berlin academies)"], certainty: 1.0, cites: [{source: S1, locator: "opening; St Petersburg to Berlin"}, {source: S2, locator: "career paragraphs"}], how_known: "Britannica and MacTutor."}

contribution:
  fields: {value: ["mathematical analysis", "number theory", "mechanics", "fluid dynamics", "astronomy"], certainty: 1.0, cites: [{source: S1, locator: "opening; Foundational works"}, {source: S2, locator: "mathematical achievements"}], how_known: "Britannica and MacTutor."}
  lasting_original_contributions:
    - {value: "Solution of the Basel problem: ζ(2) = π²/6, with ζ(4) to ζ(12), and the Euler product for ζ(s) (1737)", year: 1735, kind: discovery, lasting: "'the result that brought Euler the most fame in his young days' (S2)", certainty: 0.7, cites: [{source: S2, locator: "Basel problem paragraph"}], how_known: "MacTutor."}
    - {value: "Mechanica: Newtonian dynamics presented 'in the form of mathematical analysis for the first time'", year: 1736, kind: work, lasting: "'a major advance in mechanics' (S2)", certainty: 0.7, cites: [{source: S2, locator: "career paragraph; mechanics paragraph"}], how_known: "MacTutor; a theory about physical systems, so he is a scientist (P30)."}
    - {value: "Introductio in analysin infinitorum: the function as the organizing concept of analysis; e^{ix} = cos x + i sin x", year: 1748, kind: work, lasting: "'He did for modern analytic geometry and trigonometry what the Elements of Euclid had done for ancient geometry' (S1)", certainty: 1.0, cites: [{source: S1, locator: "Foundational works and new concepts"}, {source: S2, locator: "analysis paragraph"}], how_known: "Britannica and MacTutor."}
    - {value: "Euler equations of fluid motion (continuity equation, motion of an inviscid incompressible fluid)", year: 1757, kind: theory, lasting: "'setting up the main formulae for the topic' (S2)", certainty: 0.5, cites: [{source: S2, locator: "fluid mechanics paragraph"}], how_known: "MacTutor dates the work only to 'the 1750s' (his 1752 remark quoted); 1757 is the coder's dating of the main papers, not read. Inside the span either way."}
    - {value: "Law of quadratic reciprocity", year: 1783, kind: "law or principle", lasting: "'his greatest discovery, in 1783, was the law of quadratic reciprocity, which has become an essential part of modern number theory' (S1)", certainty: 0.5, cites: [{source: S1, locator: "Later years"}], how_known: "Britannica's date; the dating is contested (earlier statements in his correspondence are a lead, not read), so 0.5. The latest listed lasting contribution (P30 addendum b); alternative end 1772 (second lunar theory; Lettres completed)."}
  evidence_of_impact:
    - {value: "'regarded as the greatest mathematicians of the 18th century' (with Lagrange); 'never been excelled either in productivity or in the skillful and imaginative use of algorithmic devices'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Legacy"}], how_known: "Britannica."}
    - {value: "Notation f(x), e, i, π, Σ", kind: "standard textbook canon", certainty: 0.7, cites: [{source: S2, locator: "notation sentence"}], how_known: "MacTutor."}
  major_works: []
  honours:
    - {value: "Fellow of the Royal Society", year: 1747, certainty: 0.7, cites: [{source: S2, locator: "Honours"}], how_known: "MacTutor."}
  definition_fit: {value: "clearly meets", rationale: "One of the founders of pure mathematics and of analytical mechanics (S1, S2).", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "summary"}], how_known: "Britannica and MacTutor."}

childhood:
  family_religion: {value: "Reformed Protestant: father Paul Euler a Protestant minister, mother a minister's daughter", certainty: 0.7, cites: [{source: S2, locator: "opening paragraph"}], how_known: "MacTutor."}
  family_religious_practice: {value: "Father wanted him to enter the church and sent him to Basel to prepare for the ministry", certainty: 0.7, cites: [{source: S2, locator: "opening paragraph"}], how_known: "MacTutor."}
  parents_and_household:
    - {value: "Father: Paul Euler, Protestant minister, who had attended Jacob Bernoulli's lectures and taught his son elementary mathematics", certainty: 0.7, cites: [{source: S2, locator: "opening paragraph"}], how_known: "MacTutor."}
    - {value: "Mother: Margaret Brucker, daughter of a Protestant minister", certainty: 0.7, cites: [{source: S2, locator: "opening paragraph"}], how_known: "MacTutor."}
  household_circumstances: {value: "Pastor's household in Riehen near Basel", certainty: 0.7, cites: [{source: S2, locator: "opening paragraph"}], how_known: "MacTutor."}
  schooling:
    - {value: "School in Basel (a poor one; 'learnt no mathematics at all from the school')", stage: "grammar or secondary school", run_by: "state or municipal", years: "–1720", certainty: 0.5, cites: [{source: S2, locator: "opening paragraph"}], how_known: "MacTutor; run_by the coder's guess."}
    - {value: "University of Basel: master's in philosophy 1723 (Descartes and Newton compared); theology from autumn 1723, then mathematics with Johann Bernoulli's Sunday guidance; finished 1726", stage: university, run_by: "state or municipal", years: "1720–1726", certainty: 0.7, cites: [{source: S2, locator: "university paragraph"}], how_known: "MacTutor."}
  early_mathematics: {value: "advanced mathematics", certainty: 0.7, cites: [{source: S2, locator: "university paragraph"}], how_known: "Read advanced texts (Varignon, Descartes, Newton, Jacob Bernoulli) under Johann Bernoulli's advice by 1726 (S2)."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Paper on isochronous curves in a resisting medium in print by 1726; second prize, Paris Academy, 1727 (masting of ships)", certainty: 0.7, cites: [{source: S2, locator: "university paragraph"}], how_known: "MacTutor."}
  key_early_reading: []
  childhood_mentors:
    - {value: "Johann Bernoulli", certainty: 0.7, cites: [{source: S2, locator: "university paragraph"}], how_known: "MacTutor."}
  languages_in_childhood: {value: ["German"], certainty: 0.5, cites: [{source: S2, locator: "opening paragraph"}], how_known: "Coder's reading (Basel)."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1735–1783", certainty: 0.5, cites: [{source: S2, locator: "Basel problem paragraph"}, {source: S1, locator: "Later years"}], how_known: "Equals timing.major_work_period; the end rests on the contested 1783 date (alternative 1772)."}
  nominal_affiliations:
    - {value: "Reformed (Calvinist) Protestant; 'a devout Christian all his life' (S2)", certainty: 0.7, cites: [{source: S2, locator: "university paragraph"}], how_known: "MacTutor; context."}
  self_described_science_religion_relation: {value: "'si la vraie philosophie semble quelquefois contraire à la réligion; cette contradiction n'est qu'apparente' (Lettre XC)", certainty: 0.7, cites: [{source: S3, locator: "vol. 2, Lettre XC, p. 42"}], how_known: "His published Lettres, read in a 1775 reprint (see S3); 0.7 for the reprint."}
  primary_system:
    value: CHRIST
    basis: written_profession
    certainty: 0.7
    cites: [{source: S3, locator: "vol. 2, Lettres XC (pp. 42–44) and XCI (title in the table)"}, {source: S5, locator: "§§ XIX–XXXVI (French 1805 pp. 19–25); esp. XXXVI on the résurrection"}]
    rationale: "(Lettres + Rettung) The confessed religion as his working view: a merciful Father ('ce pére miséricordieux') who has heard every worthy prayer 'depuis toute l'éternité' and arranged the world in its favour; 'les vérités divines devroient bien l'emporter sur les rèveries humaines'; Lettre XCI argues that the liberty of intelligent beings agrees with the dogmas of the Christian religion (its title in the table). Named alternative CLTHEI: God answers petition and 'fasse encore quelquefois de vrais miracles'. Rejected as primary because prayer is answered through the course of nature fixed from the start, 'sans faire de miracles', not by God responding at the time (CLTHEI use_when (1))."
    how_known: "(Lettres + Rettung) Both published inside the working years (1747; 1768–72); alternative named, so 0.7. Independent source ids agree on Christian revelation."
  secondary_system: {value: UNKNOWN, how_known: "One system (P29)."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Prayer, providence and revelation as the confessed Reformed faith (Lettres); Rettung defends divine revelation and the résurrection of Christ; chosen."}
    - {code: CLTHEI, reason: "Petition is heard and present-day miracles are allowed; rejected as primary: the answer is built into the course of nature, not a response at the time."}
    - {code: CLASS_THEISM, reason: "Prayer does not change God's eternal plan; rejected: no a posteriori argument to God read (P22)."}
    - {code: DEISM, reason: "Rejected: revelation is accepted and outranks philosophy (P27)."}
  lio_axes:
    A_locus:
      value: 0
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S3, locator: "vol. 2, Lettres LXXXVII (p. 29), LXXXVIII (p. 36), XC (pp. 43–44)"}, {source: S5, locator: "§ II (French 1805 p. 2); §§ L–LII (pp. 36–38)"}]
      rationale: "(Lettres + Rettung) Interventionist pole: a transcendent person outside the world. Lettres: 'maître du monde', 'ce pére miséricordieux', 'le throne du Tout-puissant', who governs spirits 'par des commandemens ou des défenses' and arranged the world as its Creator. Rettung: 'Dieu est la vérité ; et le monde est l'ouvrage de sa toute-puissance et de son infinie sagesse'; the present world-structure 'produite dans un temps déterminé par l'opération immédiate de Dieu'; humans 'l'ouvrage de Dieu, par lequel ils ont été créés dans un temps déterminé'. No limiting feature is stated."
      how_known: "(Lettres + Rettung) Both published inside the working years. Lettres read in a 1775 reprint (false imprint), so 0.7; Rettung read in the 1805 French reprint / English translation of the 1747 German, not the German original, so 0.7. Independent source ids → corroborated (P48)."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S3, locator: "vol. 2, Lettres LXXXVII (p. 29), LXXXVIII (p. 36), XC (pp. 43–44)"}, {source: S5, locator: "§§ XLIX–L (French 1805 pp. 36–37); § XXXVI (p. 25)"}]
      rationale: "(Lettres + Rettung) Scored on his account of nature (P6). Lettres: bodies follow fixed laws ('Dieu a établi pour les corps les loix du repos & du mouvement, conformément auxquelles tous les changemens arrivent nécessairement'); God answers prayer 'sans faire de miracles', since the answer is 'une suite du cours naturel des évènemens'. The stated exception is the freedom of spirits ('les esprits ne sont susceptibles d'aucune force ou contrainte'). Under the P27 anchor a free will not bound by natural law gives B 3 (Descartes, Kant). Rettung agrees on lawful planetary motion ('conforme aux lois du mouvement') with miracle as an exceptional change to the world-state ('À moins donc que quelque miracle n'opère un changement dans l'état actuel du monde') and accepts biblical miracles (résurrection 'un fait incontestable'). Named alternative 2: Lettres add 'quoiqu'il n'y ait aucune raison de nier que Dieu ait fait & fasse encore quelquefois de vrais miracles' (present tense) — P27 T1: a conceded but unasserted possibility of rare miracles beside an explicit denial that miracles are part of the ordinary course keeps B 3, with B 2 as the named alternative. Rettung's biblical miracles and future-exception language do not force a flip to 2."
      how_known: "(Lettres + Rettung) Both inside the working years; alternative named, so 0.7. Independent source ids → corroborated (P48)."
      alternatives:
        - {value: 2, note: "P27 T1: present-tense 'fasse encore quelquefois de vrais miracles' (Lettres); Rettung accepts biblical miracles and names miracle as a possible change to the world-state.", cites: [{source: S3, locator: "vol. 2, Lettre XC, p. 44"}, {source: S5, locator: "§ XXXVI (French 1805 p. 25); § L (p. 36)"}]}
    C_ledger: {value: BELOW_THRESHOLD, how_known: "Lead only: the Lettres on liberty say bodies cannot be rewarded or punished while free spirits are responsible (vol. 2, Lettres LXXXV–LXXXVI; read only in OCR and in Hunter's translation, 'no reward, no punishment can possibly take place'), and Lettre XCI treats the conversion of sinners. No statement of divine reward and punishment of persons was verified in the page images."}
    D_authority:
      value: 1
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S3, locator: "vol. 2, Lettre XC, p. 42"}, {source: S5, locator: "§§ XIX–XXXVI (French 1805 pp. 19–25); title and bookseller's note"}]
      rationale: "(Lettres + Rettung) Leans to the interventionist pole. Lettres: where philosophical systems contradict religion, 'les vérités divines devroient bien l'emporter sur les rèveries humaines'; limited: a true philosophy only seems contrary ('cette contradiction n'est qu'apparente'), and his physics in the same Lettres is argued from observation. Rettung: whole pamphlet defends divine revelation and the divinity of Scripture against freethinkers; résurrection grounds the Christian religion as 'un ouvrage de Dieu'. Named alternative 2: the Lettres passage sets revelation against speculative systems ('rèveries'), not against observation, so it may describe two domains, each with its own authority."
      how_known: "(Lettres + Rettung) Both inside the working years; alternative named, so 0.7. Independent source ids → corroborated (P48)."
      alternatives:
        - {value: 2, note: "Revelation against speculative systems only (Lettres); Rettung is apologetic, not a physics-vs-revelation split.", cites: [{source: S3, locator: "vol. 2, Lettre XC, p. 42"}, {source: S5, locator: "§§ XIX–XXXVI (French 1805 pp. 19–25)"}]}
    E_scope:
      value: 2
      basis: written_profession
      certainty: 0.7
      support: single
      cites: [{source: S3, locator: "vol. 2, Lettres LXXXVIII (p. 36) and XC (pp. 43–44)"}]
      rationale: "Scored on the world's order (P7). The same laws of rest and motion govern all bodies, but providence arranged the course of events 'en faveur de cette priére' for 'les fidèles': answered petition for the faithful, built into the plan. Mixed: 2. Named alternative 3: the favour works only through the natural course, a stated, limited exception. Salvation and conversion are not scored here (C)."
      how_known: "Published Lettres; alternative named, so 0.7."
      alternatives:
        - {value: 3, note: "Favour only through the natural course.", cites: [{source: S3, locator: "vol. 2, Lettre XC, p. 43"}]}
  mid_basin: {value: true, certainty: 0.7, cites: [{source: S3, locator: "vol. 2, Lettres LXXXVIII and XC"}, {source: S5, locator: "§§ II, L–LII"}], how_known: "P4 test: A 0 (0.7) ≤ 1 and B 3 (0.7) ≥ 3, both at ≥ 0.7, so true; certainty the lower of the two (0.7). Both A and B now corroborated (P48) — filled, still dark. B's named alternative 2 would leave the test without a branch (TODO); P27 T1 keeps value at 3."}
  statements:
    - text: "Et si Dieu, comme maître du monde, changeoit immédiatement quelque chose dans le cours des évènemens successifs, ce changement n'appartiendroit plus à la machine: ce seroit alors un miracle."
      cites: [{source: S3, locator: "vol. 2, Lettre LXXXVII, p. 29"}]
      date: "1768"
      context: "Lettres à une princesse d'Allemagne, Lettre LXXXVII ('Influence de la liberté des esprits dans les évènemens'), on a world of bodies alone as a machine like a musical clock."
      axes: [A_locus, B_cause]
      kind: "published letter"
      verified_against: "primary facsimile"
      verified_on: 2026-10-19
      note: "Page image of the 1775 reprint (false London imprint, 'Chez la Société typographique'), vol. 2, p. 29. Long s normalised."
    - text: "Dieu a établi pour les corps les loix du repos & du mouvement, conformément auxquelles tous les changemens arrivent nécessairement, les corps n'étant que des êtres passifs, qui se maintiennent dans leur état, ou qui obéissent nécessairement aux impressions que les uns font sur les autres, comme j'ai eu l'honneur de l'expliquer à V. A. au lieu que les esprits ne sont susceptibles d'aucune force ou contrainte, & que c'est par des commandemens ou des défenses que Dieu les gouverne."
      cites: [{source: S3, locator: "vol. 2, Lettre LXXXVIII, p. 36"}]
      date: "1768"
      context: "Lettre LXXXVIII, on natural, supernatural and moral events."
      axes: [A_locus, B_cause, E_scope]
      kind: "published letter"
      verified_against: "primary facsimile"
      verified_on: 2026-10-19
      note: "Same reprint, vol. 2, p. 36."
    - text: "Plusieurs systêmes philosophiques sont réellement en contradiction avec elle; mais les vérités divines devroient bien l'emporter sur les rèveries humaines, si l'orgueil des philosophes n'y mettoit pas obstacle; & si la vraie philosophie semble quelquefois contraire à la réligion; cette contradiction n'est qu'apparente, & il ne faut jamais se laisser éblouïr par des objections."
      cites: [{source: S3, locator: "vol. 2, Lettre XC, p. 42"}]
      date: "1768"
      context: "Opening of Lettre XC, on the connection of the preceding letters with religion; 'elle' is religion."
      axes: [D_authority]
      kind: "published letter"
      verified_against: "primary facsimile"
      verified_on: 2026-10-19
      note: "Same reprint, vol. 2, p. 42. Hunter (1795) prints this passage as a quoted footnote; the 1775 French has it in the text."
    - text: "Il a déja entendu cette priére depuis toute l'éternité, & [...] si ce pére miséricordieux l'a jugée digne d'être exaucée, il a arrangé exprès le monde en faveur de cette priére, ensorte que l'accomplissement fut une suite du cours naturel des évènemens. C'est ainsi que Dieu éxauce les priéres des fidèles sans faire de miracles : quoiqu'il n'y ait aucune raison de nier que Dieu ait fait & fasse encore quelquefois de vrais miracles."
      cites: [{source: S3, locator: "vol. 2, Lettre XC, pp. 43–44"}]
      date: "1768"
      context: "Same letter, his answer to the objection against prayer drawn from the fixed course of nature."
      axes: [A_locus, B_cause, E_scope]
      kind: "published letter"
      verified_against: "primary facsimile"
      verified_on: 2026-10-19
      note: "Same reprint, vol. 2, pp. 43–44; the cut is a doubled '&' at the line break on p. 43."

    - text: "Dieu est la vérité ; et le monde est l'ouvrage de sa toute-puissance et de son infinie sagesse."
      cites: [{source: S5, locator: "§ II, French 1805 p. 2"}]
      date: "1747"
      context: "Rettung der Göttlichen Offenbahrung (1747), opening argument that perfection of the understanding has God and His works as its principal object; read in the 1805 French Défense."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "IA OCR of the 1805 Paris printing (dfensedelarv00eule), printed page (2); long s / spacing normalised. English E092trans used for navigation only."
    - text: "La résurrection de J. C. est encore un fait incontestable ; et un pareil miracle ne pouvant être l'ouvrage que de Dieu seul, il est impossible après cela de révoquer en doute la divinité de la mission du Sauveur."
      cites: [{source: S5, locator: "§ XXXVI, French 1805 p. 25"}]
      date: "1747"
      context: "Same work, on the resurrection as proof of the divinity of Christ's mission and of Scripture."
      axes: [A_locus, B_cause, D_authority]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Same 1805 printing, printed page (25); OCR 'J'ouvrage' read as 'l'ouvrage'."
    - text: "C'est de là que procède la diminution des orbites des planètes, qui arrive d'une manière conforme aux lois du mouvement, et qui s'accorde en même temps avec les observations. [...] À moins donc que quelque miracle n'opère un changement dans l'état actuel du monde, il faut qu'à la fin la terre se trouve si près du soleil, que ni hommes ni animaux ne pourront plus y subsister."
      cites: [{source: S5, locator: "§§ XLIX–L, French 1805 pp. 36–37"}]
      date: "1747"
      context: "Same work, arguing from ether-resistance and the laws of motion that the present world-state cannot be eternal; miracle named as the only exceptional change."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Same 1805 printing, printed pages (36)–(37); cut joins the end of § XLIX to the opening of § L."
    - text: "Cela fournit une preuve incontestable, que la structure présente du monde ne sauroit être éternelle, mais qu'il faut qu'elle ait été produite dans un temps déterminé par l'opération immédiate de Dieu."
      cites: [{source: S5, locator: "§ LI, French 1805 p. 37"}]
      date: "1747"
      context: "Same work, creation of the present world-structure in finite time by God's immediate operation."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Same 1805 printing, printed page (37)."
  changes_over_life: []
  coder_notes: "Coder's call. Deepen D1 reads the Rettung (1747) in the 1805 French Défense (IA) and English E092trans; A and B move single→corroborated (hollow→filled). P27 T1 already settled B 3 alt 2 for the present-tense miracles concession; Rettung's biblical miracles and 'à moins que quelque miracle' language do not force a flip. The religious letters were left out of the Condorcet edition (the 1805 Défense reprints some; the record still uses the 1775 Lettres reprint for those letters). Long s normalised silently. German 1747 original (SLUB) and 1768 St Petersburg Lettres not opened this pass."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Swiss (Basel)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Reformed Protestant (pastor's family)", certainty: 0.7, cites: [{source: S2, locator: "opening paragraph"}], how_known: "MacTutor."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1735–1783", certainty: 0.5, cites: [{source: S2, locator: "Basel problem paragraph"}, {source: S1, locator: "Later years"}], how_known: "Basel problem (1735) to quadratic reciprocity (1783, Britannica's date), first to last listed lasting contribution (P29, P30). The end is contested: alternative 1772 if the 1783 date is not kept. The Lettres (1768–72) fall inside either way."}
  age_at_first_lasting_contribution: {value: 28, certainty: 0.7, cites: [{source: S2, locator: "Quick Info; Basel problem paragraph"}], how_known: "1735 − 1707 = 28 (P30)."}
  first_evidence_of_lio_type_views: {value: "1747: world as God's work by immediate operation; planetary motion under the laws of motion; biblical miracles defended", year: 1747, certainty: 0.7, cites: [{source: S5, locator: "§§ II, XXXVI, XLIX–LII"}], how_known: "Rettung (1747) now read (S5); inside the working years. Lettres (1768) remain the fuller B/E account."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S3, locator: "vol. 2"}], how_known: "Lettres published 1768–72, inside 1735–1783."}
  worldview_during_major_work: {value: "Reformed Christian: lawful mechanics for bodies, free spirits, prayer answered through a pre-arranged course, miracles conceded; divine revelation and the résurrection defended", certainty: 0.7, cites: [{source: S3, locator: "vol. 2, Lettres LXXXVII–XC"}, {source: S5, locator: "§§ II, XIX–XXXVI, XLIX–LII"}], how_known: "Lettres + Rettung."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Mechanics recast as analysis; a world of bodies alone compared to a clock 'une fois montée'.", certainty: 0.5, cites: [{source: S3, locator: "vol. 2, p. 29"}, {source: S2, locator: "mechanics paragraph"}], how_known: "Coder's reading."}
  form_acquired: {value: "adulthood, before major work", certainty: 0.5, cites: [{source: S2, locator: "university paragraph"}], how_known: "Coder's reading (Bernoulli's guidance, 1720s)."}
  circle_present: {value: "no", rationale: "God is the transcendent Creator.", certainty: 0.7, cites: [{source: S3, locator: "vol. 2, Lettre XC"}], how_known: "Coder's reading."}
  reading: "A mid-basin theist on the P4 test: a lawful mechanics of bodies, free spirits, and a providence that works through the fixed course; A and B now corroborated (filled)."
  notes: ""

institutions:
  - {value: "St Petersburg Academy of Sciences", role: "associate, professor of physics, then chair of mathematics", years: "1727–1741; 1766–1783", kind: "academy or learned society", certainty: 1.0, cites: [{source: S1, locator: "From St. Petersburg to Berlin"}, {source: S2, locator: "St Petersburg paragraphs"}], how_known: "Britannica and MacTutor."}
  - {value: "Berlin Academy", role: "director of mathematics", years: "1741–1766", kind: "academy or learned society", certainty: 1.0, cites: [{source: S1, locator: "From St. Petersburg to Berlin"}, {source: S2, locator: "Berlin paragraphs"}], how_known: "Britannica and MacTutor."}
collaborators:
  - {value: "Johann Bernoulli", relation: teacher, note: "guided his reading at Basel", certainty: 1.0, cites: [{source: S1, locator: "From St. Petersburg to Berlin"}, {source: S2, locator: "university paragraph"}], how_known: "Britannica and MacTutor."}
  - {value: "Daniel Bernoulli", relation: collaborator, note: "colleague and housemate in St Petersburg", certainty: 0.7, cites: [{source: S2, locator: "St Petersburg paragraph"}], how_known: "MacTutor."}
  - {value: "Christian Goldbach", relation: correspondent, note: "number theory correspondence", certainty: 0.7, cites: [{source: S2, locator: "number theory paragraph"}], how_known: "MacTutor."}
  - {value: "Joseph-Louis Lagrange", relation: influenced, note: "his successor in analysis (S1)", certainty: 0.7, cites: [{source: S1, locator: "Legacy"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 113"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Worldview Lettres read in a 1775 reprint (false imprint), not the 1768 first edition."
    - "Rettung read in 1805 French reprint / English translation, not the 1747 German original (SLUB)."
    - "Span end rests on Britannica's 1783 date for quadratic reciprocity (contested)."
  open_questions:
    - "Check the Lettres passages against the 1768 St Petersburg edition or Opera Omnia III.11–12."
    - "Check Rettung against the 1747 German (SLUB id424129752) or Opera Omnia III.12."
    - "Date quadratic reciprocity (1783 vs earlier statements)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Carl B. Boyer"
    citation: "Boyer, Carl B. \"Leonhard Euler.\" Encyclopaedia Britannica (revised 14 September 2026). https://www.britannica.com/biography/Leonhard-Euler. Read live 2026-10-18."
    url: "https://www.britannica.com/biography/Leonhard-Euler"
    accessed: 2026-10-18
    reliability_note: "Signed article. Body only; the AI-generated Top Questions are not cited."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, institutions, collaborators, heritage]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "J. J. O'Connor and E. F. Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Leonhard Euler.\" MacTutor History of Mathematics, University of St Andrews (last update September 1998). https://mathshistory.st-andrews.ac.uk/Biographies/Euler/"
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Euler/"
    accessed: 2026-10-18
    reliability_note: "Signed biography, with references (Youschkevitch's DSB article, Calinger)."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators, lane_b]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Leonhard Euler"
    citation: "[Euler, Leonhard.] Lettres à une princesse d'Allemagne sur divers sujets de physique et de philosophie. Tome second. 'Londres: Chez la Société typographique', 1775 (reprint; first edition St Petersburg: Académie impériale des sciences, 1768–72). Page images: Internet Archive, bim_eighteenth-century_lettres-a-une-princesse-_euler-leonhard_1775_2 (p. N = leaf n(N+7)). Compared with: Letters of Euler to a German Princess, tr. Henry Hunter, vol. 1 (London, 1795), Internet Archive bim_eighteenth-century_letters-of-euler-to-a-ge_euler-leonhard_1795_1."
    url: "https://archive.org/details/bim_eighteenth-century_lettres-a-une-princesse-_euler-leonhard_1775_2"
    accessed: 2026-10-18
    reliability_note: "Microfilm scan of a 1775 printing; the catalogue notes 'The imprint is false; probably printed in The Hague.' Text and letter numbers agree with Hunter's 1795 translation of the original edition for the passages used. Not checked against the 1768 edition or the Opera Omnia."
    source_quality: "primary / own words"
    used_for: [worldview, timing, lane_b]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-18
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Leonhard Euler"
    citation: "Euler, Leonhard. Rettung der Göttlichen Offenbahrung gegen die Einwürfe der Freygeister (Berlin: Haude and Spener, 1747). Read in: Défense de la révélation contre les objections des esprits-forts, par M. Euler, suivie des pensées de cet auteur sur la religion… (Paris: A. Le Clère, 1805), Internet Archive dfensedelarv00eule (French reprint of the 1755 Bibliothèque impartiale translation). English navigation: A Defense of the Revelation against the Objections of Freethinkers, Euler Archive E092trans.pdf (via Wayback Machine)."
    url: "https://archive.org/details/dfensedelarv00eule"
    accessed: 2026-10-24
    reliability_note: "Posthumous French reprint (1805) of a mid-century journal translation of the 1747 German original; not checked against the German (SLUB) or Opera Omnia III.12. French quotes taken from IA PDF OCR (archive scan). English E092trans used for section navigation only, not as the quoted text."
    source_quality: "primary / own words"
    used_for: [worldview, timing, lane_b]
  - id: S6
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Leonhard Euler.\" English Wikipedia. https://en.wikipedia.org/wiki/Leonhard_Euler. Read live 2026-10-24."
    url: "https://en.wikipedia.org/wiki/Leonhard_Euler"
    accessed: 2026-10-24
    reliability_note: "Crowdsourced; used for dual bio (P50) and the Personal philosophy section's pointer to Lettres + Rettung. Body facts cross-checked against S1/S2 where cited."
    source_quality: "reference entry"
    used_for: [identity, basics, childhood, heritage, worldview]
---

# Leonhard Euler

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Leonhard Euler (1707–1783), Swiss mathematician and physicist [S1, S2, S6]. Deepen D1: primary_system CHRIST (0.7, alt CLTHEI); A 0 at 0.7 (corroborated S3+S5); B 3 at 0.7 (alt 2; corroborated S3+S5; P27 T1); C BELOW_THRESHOLD; D 1 at 0.7 (alt 2; corroborated S3+S5); E 2 at 0.7 (alt 3; single); mid_basin true (0.7). Plotted (dark, now filled).

## Life and work

Basel, St Petersburg (1727–41, 1766–83), Berlin (1741–66) [S1, S2, S6].

## Contribution and impact

Basel problem (1735), Mechanica (1736), Introductio (1748), fluid equations, quadratic reciprocity [S1, S2].

## Childhood and education

Pastor's son (Reformed Church); Basel, under Johann Bernoulli [S2, S6].

## Adult working worldview

'C'est ainsi que Dieu éxauce les priéres des fidèles sans faire de miracles' [S3, vol. 2, p. 44]. Rettung: 'Dieu est la vérité ; et le monde est l'ouvrage de sa toute-puissance et de son infinie sagesse' [S5, § II].

## Heritage (context only)

Swiss Reformed [S2, S6].

## Timing

1735–1783, from age 28 [S1, S2]. First LIO-type evidence 1747 (Rettung) [S5].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. A clockwork of bodies with free spirits [S3]; A and B corroborated by Rettung [S5].

## Open questions

- Check Lettres against the 1768 edition or Opera Omnia III.11–12; check Rettung against the 1747 German (SLUB).

## Research log

- 2026-10-18/19: Read Britannica (live), MacTutor, and the page images of vol. 2 of the 1775 reprint of the Lettres (pp. 29, 36, 42–44), with Hunter's 1795 translation for comparison.
- 2026-10-24: Deepen D1. Read Rettung (1747) via 1805 French Défense IA OCR + E092trans English; Wikipedia EN dual bio; P47 source_quality; A/B/D corroborated (hollow→filled); B alt 2 kept (P27 T1).
