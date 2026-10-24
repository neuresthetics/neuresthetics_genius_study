---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch S; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-18
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-18, by: "Grok Bot", summary: "Record created (stage 3 batch S, order P32: F 4, rank 108). Basics from Britannica (Britannica Editors, unsigned; body only, read live). Worldview from his published lecture Immanentisme et foi religieuse (Geneva, Libr. H. Robert, 1930; given at Rolle on 16 June 1929), read in full in the University of Geneva's online Piaget edition. Scientist (P30, P35 addendum: testable claims about children's cognition). primary_system IDEAL (0.5; alternatives KANT, CHRIST); A 4 (0.7, alt 3); B 3 (0.7, alt 4; P27 free-mind anchor); C BELOW_THRESHOLD; D 4 (0.7); E 4 (0.7); mid_basin false (0.7). Plotted. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit notes for batch S (blind audit of c5d448a, run 1). first_evidence_of_lio_type_views dated 1929 (the lecture given at Rolle on 16 June 1929; printed 1930). primary_system now also cites part I, where 'le Dieu immanent est un Dieu-valeur' stands (the definitions part). No value changes."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #107 / F4 rank 108). Goals: corroborate A and B (hollow→filled); keep scores honest. Dual bio: Britannica (S1) + Wikipedia EN (S7) (P50). P47 source_quality on every source. Read in full: 1928 Deux types d'attitudes religieuses (S4, unige; La Sarraz, Mar 1928; published with de la Harpe 1928) and 1929 Encore «Immanence et transcendance» (S5, Cahiers protestants); Insights and Illusions of Philosophy ch.1 (S6, Meridian 1971; own retrospective on Bergson→immanentism and the 1920s lectures). A stays 4 @0.7 alt 3; support single→corroborated (P48: S2 1930 + S4 1928; S5 agrees). B stays 3 @0.7 alt 4 (P27 free-mind); support single→corroborated (S2 + S4 reject miracle / divine intervention in nature). D and E also support→corroborated. first_evidence→1928. mid false @0.7. Chart-moving YES (fill only: dark hollow→dark filled). No fallacy_catalog. No figures/. Draft, not reviewed."}

identity:
  id: piaget-jean
  display_name: "Jean Piaget"
  roster:
    canonical_name: "Jean Piaget"
    rank: 108
    F: 4
    models: [Claude, DeepSeek, Gemini, GPT]
    band: "core (3–4)"
    status: core
    field: psychology
    field_bucket: "psychology / neuroscience"
  full_name: {value: "Jean Piaget", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "lead / infobox (Jean William Fritz Piaget)"}], how_known: "Britannica and Wikipedia agree (P15). Wikipedia gives the fuller form Jean William Fritz Piaget."}
  native_name: {value: "Jean Piaget", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "lead"}], how_known: "French; Britannica and Wikipedia agree."}
  aliases:
    - {name: "Jean-Piaget", kind: "roster alias"}

basics:
  birth:
    date: {value: "1896-08-09", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "infobox"}], how_known: "Britannica and Wikipedia agree."}
    place: {value: "Neuchâtel, Switzerland", modern_name: "Neuchâtel, Switzerland", polity_then: "Switzerland", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "infobox"}], how_known: "Britannica and Wikipedia agree."}
  death:
    date: {value: "1980-09-16", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "infobox / Death"}], how_known: "Britannica and Wikipedia agree."}
    place: {value: "Geneva, Switzerland", modern_name: "Geneva, Switzerland", polity_then: "Switzerland", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "Death (Cimetière des Rois, Plainpalais)"}], how_known: "Britannica and Wikipedia agree."}
  first_lasting_contribution_year: {value: 1923, certainty: 0.7, cites: [{source: S1, locator: "major works paragraph"}], how_known: "Le Langage et la pensée chez l'enfant (1923), the earliest of the major works the body names (P13, P17); he had 'begun to publish his findings' by 1921 (S1), undated items not listed (CODING_GUIDE §8: the year might be earlier)."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "major works paragraph"}], how_known: "1923 (P2); 1921 gives the same bucket."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Switzerland (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "career paragraph"}], how_known: "Geneva and Neuchâtel; Paris 1919–21."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["French"], certainty: 0.7, cites: [{source: S1, locator: "major works paragraph"}], how_known: "French titles (S1)."}
  occupations: {value: ["psychologist", "professor of child psychology", "zoologist"], certainty: 0.7, cites: [{source: S1, locator: "opening; career paragraph"}], how_known: "Britannica."}

contribution:
  fields: {value: ["developmental psychology", "genetic epistemology"], certainty: 0.7, cites: [{source: S1, locator: "opening; career paragraph"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Le Langage et la pensée chez l'enfant (The Language and Thought of the Child): the first systematic study of children's understanding", year: 1923, kind: work, lasting: "'the first to make a systematic study of the acquisition of understanding in children' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; major works paragraph"}], how_known: "Britannica. A theory of mind with testable claims about children, so he is a scientist (P30, P35 addendum)."}
    - {value: "Stage theory of cognitive development: 'the mind of the child evolves through a series of set stages to adulthood'", year: 1923, kind: theory, lasting: "'caused a reevaluation of older ideas of the child, of learning, and of education' (S1)", certainty: 0.5, cites: [{source: S1, locator: "career paragraph; stages paragraph"}], how_known: "Britannica gives no single year ('the theme he had first discovered in Paris', 1919–21); dated with the first listed book (coder's call)."}
    - {value: "La Naissance de l'intelligence chez l'enfant (The Origins of Intelligence in Children)", year: 1948, kind: work, lasting: "named among his major works (S1)", certainty: 0.7, cites: [{source: S1, locator: "major works paragraph"}], how_known: "Britannica; the latest listed lasting work (coder's call: later genetic-epistemology works were not read)."}
  evidence_of_impact:
    - {value: "'thought by many to have been the major figure in 20th-century developmental psychology'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Protestant (mother); father a nonbeliever", certainty: 0.7, cites: [{source: S6, locator: "ch.1 ('I was brought up in the Protestant faith')"}, {source: S7, locator: "Early life"}], how_known: "His own Insights retrospective (S6); Wikipedia agrees on Protestant upbringing."}
  family_religious_practice: {value: "Mother insisted on a six-week 'instruction religieuse' around age fifteen; father did not go to church", certainty: 0.7, cites: [{source: S6, locator: "ch.1"}], how_known: "Insights; Autobiographie 1966 (unige) agrees."}
  parents_and_household: []
  household_circumstances: {value: TODO}
  schooling:
    - {value: "University of Neuchâtel: zoology and philosophy; doctorate in zoology 1918", stage: university, run_by: "state or municipal", years: "–1918", certainty: 0.7, cites: [{source: S1, locator: "early-interests paragraph"}], how_known: "Britannica; run_by the coder's."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Published on an albino sparrow as a youth; by 15 his papers on mollusks had made his name among European zoologists", certainty: 0.7, cites: [{source: S1, locator: "early-interests paragraph"}], how_known: "Britannica."}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["French"], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading (Neuchâtel)."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1923–1948", certainty: 0.7, cites: [{source: S1, locator: "major works paragraph"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Swiss Protestant milieu: lectured to the Association chrétienne d'étudiants and its former members (1928, 1929)", certainty: 0.7, cites: [{source: S2, locator: "editors' foreword (note a)"}], how_known: "The brochure's foreword; context only."}
  self_described_science_religion_relation: {value: "'Il n’y a de connaissance que la connaissance scientifique'; there is no place beside science for 'une causalité métaphysique à côté ou au-dessus de la causalité naturelle', and it is 'absurde — et même à certains égards scandaleux — de vouloir démontrer l’existence de Dieu en s’appuyant sur la considération des frontières de la science' (1930)", certainty: 0.7, cites: [{source: S2, locator: "part II"}], how_known: "His published lecture (S2)."}
  primary_system:
    value: IDEAL
    basis: written_profession
    certainty: 0.5
    cites: [{source: S2, locator: "part I ('un Dieu-valeur'); parts II–III"}, {source: S4, locator: "part III (Essai d'évaluation)"}]
    rationale: "Critical idealism: 'La pensée qui pose l’être est, en effet, antérieure à l’être'; 'la valeur étant condition de la pensée et la pensée condition de l’être'; God is 'immanent à la pensée', 'un Dieu-valeur', identified 'avec la pensée dans ce qu’elle a de normatif par rapport au moi' (S2). The 1928 lecture agrees: 'Dieu est pensée. Il n'est pas un être mais la condition de l'existence'; immanentism 'identifier Dieu, non pas au moi psychologique, mais aux normes de la pensée' (S4). IDEAL's use_when ('reality is mental or thought-like') fits only partly: he calls his position 'exactement intermédiaire entre le réalisme et l’idéalisme' and IDEAL is a stub. Named alternatives: KANT (critical philosophy, but not the moral postulates; KANT's use_when needs both) and CHRIST (he takes Jesus as 'la conscience religieuse la plus pure qui ait jamais existé' and calls immanentism a 'doctrine de vie' within Protestant faith)."
    how_known: "Two independent published lectures (1928, 1930), University of Geneva online editions; contested between three codes, so 0.5 (coder's call)."
  secondary_system: {value: UNKNOWN, how_known: "One system (P29)."}
  candidate_codes_considered:
    - {code: IDEAL, reason: "'la pensée condition de l’être'; God immanent to thought (S2, parts II–III)."}
    - {code: KANT, reason: "Critical philosophy and freedom as a condition of thought; rejected: no moral postulates of God and immortality."}
    - {code: CHRIST, reason: "Disciple of Jesus within liberal Protestantism; rejected as primary: transcendence, miracles and expiation are denied."}
    - {code: PANT, reason: "Rejected: God is identified with the norms of thought, not with Nature (two-part test fails)."}
  lio_axes:
    A_locus:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S2, locator: "parts I and III"}, {source: S4, locator: "part III"}]
      support: corroborated
      rationale: "Immanent pole: he chooses 'l’immanentisme' against the transcendent 'Dieu-cause'; 'Dieu ... est donc immanent à la pensée, c’est-à-dire qu’il agit comme Valeur au cœur même des relations de l’esprit et de l’univers, et non comme Cause'; 'Dieu n’est donc pas un Être qui s’impose à nous du dehors' (S2). The 1928 lecture independently: 'le divin est en nous'; 'Dieu est pensée. Il n'est pas un être mais la condition de l'existence'; immanentism identifies God with 'les normes de la pensée elle-même', not the psychological moi (S4). Named alternative 3: 'Un Dieu immanent à la pensée demeure donc transcendant par rapport au moi' (S2); 1928's three-term scheme (transcendance / moi / normes impersonnelles) agrees. Two independent source ids → corroborated (P48)."
      how_known: "Two published lectures inside the working years (1928, 1930); alternative named, so 0.7."
      alternatives:
        - {value: 3, note: "'transcendant par rapport au moi' (S2); norms impersonal vs moi (S4).", cites: [{source: S2, locator: "part III"}, {source: S4, locator: "part III"}]}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      cites: [{source: S2, locator: "parts I–III"}, {source: S4, locator: "part III"}]
      support: corroborated
      rationale: "Scored on his account of nature (P6). Law without divine exceptions: the transcendent God would be cause 'd’événements particuliers ... c’est-à-dire source de miracles', which he rejects; 'y a-t-il place, dans la nature, pour une autre causalité que la causalité naturelle ? ... nous allons répondre par la négative'; petitionary prayer 'implique ... la croyance en une causalité divine intervenant du dehors' and is 'contradictoire avec l’immanentisme' (S2). The 1928 lecture independently rejects the transcendent God as 'source du miracle (et j'entends par miracle l'intervention directe soit sur l'esprit des hommes soit sur les êtres physiques)' and says transcendence cannot be a useful working hypothesis any more than 'expliquer une réaction moléculaire par l'intervention divine' (S4). The stated limit (S2) is a free mind: 'tout, dans le phénomène, est déterminé ... mais le phénomène suppose un esprit libre pour l’élaborer'. Under the P27 anchor a free will outside natural law gives B 3 as the value (Kant's noumenal freedom is the precedent). Named alternative 4: everything in phenomena is determined, and the freedom is only 'la condition de toute science', not an exception within nature. Two independent source ids → corroborated (P48)."
      how_known: "Two published lectures inside the working years; alternative named, so 0.7."
      alternatives:
        - {value: 4, note: "'Il n’y a ainsi jamais ... que du déterminisme' in phenomena (S2); 1928 likewise excludes divine intervention from nature.", cites: [{source: S2, locator: "part II"}, {source: S4, locator: "part III"}]}
    C_ledger: {value: BELOW_THRESHOLD, how_known: "Lead only: he rejects 'le drame de l’expiation en tant que voulue par la justice divine' and collective responsibility as 'un scandale moral' (part III), but states no general view of reward and punishment of persons; alternative 3 or 4 (coder's call)."}
    D_authority:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S2, locator: "parts II–III"}, {source: S4, locator: "parts I–III"}]
      support: corroborated
      rationale: "Observation and reason outrank revelation, which keeps no domain: 'Il n’y a de connaissance que la connaissance scientifique'; an external supernatural revelation is 'le produit naturel et humain de la contrainte psycho-sociale'; 'la révélation se réduit aux prescriptions intérieures de la conscience' (S2). The 1928 lecture likewise treats classical theology as mythological symbol, excludes transcendence from scientific method, and locates the divine in norms discovered by critical thought (S4). Named alternative 3: conscience keeps a normative say he calls religious, though not as revelation. Two independent source ids → corroborated (P48)."
      how_known: "Two published lectures; alternative named, so 0.7."
      alternatives:
        - {value: 3, note: "Conscience's norms as the 'révélation intérieure'.", cites: [{source: S2, locator: "part III"}, {source: S4, locator: "part III"}]}
    E_scope:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S2, locator: "parts II–III"}, {source: S4, locator: "part III"}]
      support: corroborated
      rationale: "Scored on the world's order (P7). Same rules everywhere: 'Aucune réalité — réalités sociales et psychiques autant que mécaniques ou chimiques, expériences mystiques les plus intimes autant qu’expérience externe et mesurable — aucune réalité ne paraît aujourd’hui étrangère à ses compétences'; and no favour for petitioners: 'Pourquoi surtout aurait-il créé les choses d’une certaine manière pour les corriger ensuite au profit de ceux qui pactisent avec lui et lui adressent leurs demandes ?' (S2). The 1928 lecture rejects miracle as intervention on physical beings and treats divine favour / expiation mythology as incompatible with critical immanentism (S4). Named alternative 3 on the free mind (as on B). Two independent source ids → corroborated (P48)."
      how_known: "Two published lectures; alternative named, so 0.7."
      alternatives:
        - {value: 3, note: "The free mind as on B.", cites: [{source: S2, locator: "part II"}, {source: S4, locator: "part III"}]}
  mid_basin: {value: false, certainty: 0.7, cites: [{source: S2, locator: "parts I and III"}, {source: S4, locator: "part III"}], how_known: "P4 test: A 4 (alternative 3, both ≥ 3) at 0.7; the A ≥ 3 branch reads A only (P10)."}
  statements:
    - text: "Le Dieu immanent, au contraire, ne se résout pas en termes de causalité mais d’implications."
      cites: [{source: S2, locator: "part I"}]
      date: "1930"
      context: "Immanentisme et foi religieuse, lecture to the former members of the Association chrétienne d'étudiants at Rolle, 16 June 1929, published Geneva 1930; the definitions part, where the transcendent God is 'triplement cause' (creator, 'source de miracles', cause of mystical states)."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-18
      note: "University of Geneva online edition of the 1930 brochure (pp. 1–54); no page numbers shown, so part numbers are used."
    - text: "La question est donc celle-ci : y a-t-il place, dans la nature, pour une autre causalité que la causalité naturelle ? Y a-t-il place, à côté de la connaissance scientifique, pour une autre connaissance de la réalité ? Pour le dire d’emblée, nous allons répondre par la négative."
      cites: [{source: S2, locator: "part II, opening"}]
      date: "1930"
      context: "Same lecture."
      axes: [B_cause, D_authority]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-18
      note: ""
    - text: "En bref, tout, dans le phénomène, est déterminé, même ce que nous connaissons de nous-mêmes, mais le phénomène suppose un esprit libre pour l’élaborer."
      cites: [{source: S2, locator: "part II, on freedom"}]
      date: "1930"
      context: "Same lecture; freedom 'n’est pas un fait psychologique, mais elle est la condition de toute science'."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-18
      note: ""
    - text: "Dieu, dans une telle doctrine, est donc immanent à la pensée, c’est-à-dire qu’il agit comme Valeur au cœur même des relations de l’esprit et de l’univers, et non comme Cause dans un esprit et un univers conçus indépendamment l’un de l’autre."
      cites: [{source: S2, locator: "part III, opening"}]
      date: "1930"
      context: "Same lecture; he then says 'nous choisissons l’immanentisme' because of the problems of evil and of the irrational."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-18
      note: ""
    - text: "Un Dieu immanent à la pensée demeure donc transcendant par rapport au moi."
      cites: [{source: S2, locator: "part III"}]
      date: "1930"
      context: "Same lecture, after 'Nier la transcendance ne revient pas à faire de Dieu le moi, mais à identifier Dieu avec la pensée dans ce qu’elle a de normatif par rapport au moi. Nous ne sommes pas Dieu.' The basis of A's alternative 3."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-18
      note: ""
    - text: "Pourquoi surtout aurait-il créé les choses d’une certaine manière pour les corriger ensuite au profit de ceux qui pactisent avec lui et lui adressent leurs demandes ?"
      cites: [{source: S2, locator: "part III, on prayer"}]
      date: "1930"
      context: "Same lecture, on petitionary ('égocentrique') prayer, which 'implique ... la croyance en une causalité divine intervenant du dehors dans la contexture même des phénomènes'."
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-18
      note: ""
    - text: "Pour dire les choses en toute sincérité, je crois donc que le Dieu transcendant, substance spirituelle, créateur du monde, source du miracle (et j’entends par miracle l’intervention directe soit sur l’esprit des hommes soit sur les êtres physiques), n’est qu’un symbole dû à l’imagination mythologique et enfantine, et sans aucun rapport avec le Dieu en esprit et en vérité que postule la conscience."
      cites: [{source: S4, locator: "part III (Essai d'évaluation)"}]
      date: "1928"
      context: "Deux types d'attitudes religieuses: immanence et transcendance, 31e Conférence d'étudiants des universités romandes at La Sarraz, March 1928; Piaget's personal evaluation part."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "University of Geneva online edition (piaget1928a06); no page numbers shown."
    - text: "Dieu est pensée. Il n’est pas un être mais la condition de l’existence, et la condition de l’existence c’est la pensée."
      cites: [{source: S4, locator: "part III"}]
      date: "1928"
      context: "Same 1928 lecture; critical-idealist identification of God with thought/norms rather than an external Being."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: ""
    - text: "Or l’immanentisme revient à identifier Dieu, non pas au moi psychologique, mais aux normes de la pensée elle-même."
      cites: [{source: S4, locator: "part III"}]
      date: "1928"
      context: "Same lecture; three-term scheme (transcendance / moi / normes impersonnelles)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Corroborates A's alt 3 structure (norms transcend the moi)."
    - text: "Chercher Dieu dans les valeurs suprêmes, sans lui attribuer une « existence » au sens naïf du réalisme, telle est l’attitude de l’immanence."
      cites: [{source: S5, locator: "Cahiers protestants 13 (1929)"}]
      date: "1929"
      context: "Encore «Immanence et transcendance», reply to Arnold Reymond clarifying the 1928 lecture."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "University of Geneva online edition (piaget1929a06). Agreeing third stream; not required for P48 fill."
    - text: "Internal unity was thus achieved in the direction of an immanentism which has long satisfied me."
      cites: [{source: S6, locator: "ch.1 (Bergson / adolescent crisis)"}]
      date: "1965"
      context: "Insights and Illusions of Philosophy, retrospective on reading Bergson (God = Life / élan vital) in adolescence; he notes it later took 'other, increasingly rational forms'."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Post-span for scoring (P20); used as continuity evidence (P31) and childhood context, not to raise certainty. Meridian 1971 translation via unofficial PDF host."
  changes_over_life:
    - {value: "From adolescent Bergsonian identification of God with Life (élan vital) to critical-idealist immanentism (God as norms of thought; no supernatural causality), c. 1915–1928", certainty: 0.7, cites: [{source: S6, locator: "ch.1"}, {source: S4, locator: "part III"}, {source: S5, locator: "full reply"}], how_known: "Insights describes the Bergson ecstasy then increasingly rational forms; the 1928 lecture is the worked public form; the 1929 Cahiers protestants reply (S5) reaffirms immanence without external finality."}
  coder_notes: "Deepen 2026-10-24: A and B now cite two independent in-span lectures (S4 1928 + S2 1930), so support→corroborated (P48); scores unchanged (A 4 / B 3 @0.7, alts named). B 3 still follows the P27 free-will anchor from S2; if the auditor reads his freedom as a condition of thought rather than an exception to natural law, B would be 4 (alternative named; the plotted point would move from A4/B3 to A4/B4). S5 (1929 reply to Reymond) and S6 (Insights) agree on immanentism but are not needed for the P48 fill. IDEAL stays 0.5 (stub + contested with KANT/CHRIST)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Swiss (Neuchâtel)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Swiss Protestant (mother's side)", certainty: 0.7, cites: [{source: S6, locator: "ch.1"}, {source: S7, locator: "Early life"}], how_known: "Insights and Wikipedia."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1923–1948", certainty: 0.7, cites: [{source: S1, locator: "major works paragraph"}], how_known: "Le Langage et la pensée (1923) to La Naissance de l'intelligence (1948), first to last listed lasting contribution (P29, P30). Coder's call: later works (genetic epistemology; the Centre founded 1955) not listed."}
  age_at_first_lasting_contribution: {value: 27, certainty: 0.7, cites: [{source: S1, locator: "opening; major works paragraph"}], how_known: "1923 − 1896 = 27 (P30)."}
  first_evidence_of_lio_type_views: {value: "1928: transcendent God as mythological symbol / source of miracle rejected; God as thought/norms (La Sarraz lecture, Mar 1928)", year: 1928, certainty: 0.7, cites: [{source: S4, locator: "part III"}, {source: S2, locator: "parts I–III"}], how_known: "1928 brochure is the earliest in-span published profession read; the 1929/1930 Rolle lecture repeats and sharpens the same axes."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S2, locator: "editors' foreword"}], how_known: "Lecture of 1929, published 1930, inside 1923–1948."}
  worldview_during_major_work: {value: "Religious immanentism within critical idealism: God as the norms of thought, no supernatural causality", certainty: 0.7, cites: [{source: S2, locator: "parts II–III"}], how_known: "His 1930 lecture."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "He takes mathematics as the model of the mind's construction ('pas de physique possible sans une mathématique').", certainty: 0.5, cites: [{source: S2, locator: "part II"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "early-interests paragraph"}], how_known: "Not read."}
  circle_present: {value: "no", rationale: "God identified with the norms of thought, not with Nature.", certainty: 0.5, cites: [{source: S2, locator: "part III"}], how_known: "Coder's reading."}
  reading: "An immanentist scientist: God as value, nature left wholly to natural causes."
  notes: ""

institutions:
  - {value: "Institut J.-J. Rousseau, Geneva", role: director, years: "1921–", kind: "research institute", certainty: 0.7, cites: [{source: S1, locator: "career paragraph"}], how_known: "Britannica."}
  - {value: "University of Neuchâtel", role: professor, years: "1925–1929", kind: university, certainty: 0.7, cites: [{source: S1, locator: "career paragraph"}], how_known: "Britannica."}
  - {value: "University of Geneva", role: "professor of child psychology", years: "1929–1980", kind: university, certainty: 0.7, cites: [{source: S1, locator: "career paragraph ('remaining there until his death')"}], how_known: "Britannica."}
  - {value: "International Centre of Genetic Epistemology, Geneva", role: "founder and director", years: "1955–", kind: "research institute", certainty: 0.7, cites: [{source: S1, locator: "career paragraph"}], how_known: "Britannica."}
collaborators:
  - {value: "Carl Jung", roster_id: jung-carl, relation: teacher, note: "studied under him in Zürich", certainty: 0.7, cites: [{source: S1, locator: "early-interests paragraph"}], how_known: "Britannica."}
  - {value: "Eugen Bleuler", relation: teacher, note: "studied under him in Zürich", certainty: 0.7, cites: [{source: S1, locator: "early-interests paragraph"}], how_known: "Britannica."}
  - {value: "Léon Brunschvicg", relation: "influenced by", note: "quoted at length on God as 'la réalité pure et intime qui commande en chacun de nous la vie spirituelle'", certainty: 0.7, cites: [{source: S2, locator: "part III"}], how_known: "His lecture."}
  - {value: "Jean de la Harpe", relation: collaborator, note: "co-author of the 1928 brochure Deux types d'attitudes religieuses", certainty: 0.7, cites: [{source: S2, locator: "note 1"}], how_known: "His lecture."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 108"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Britannica article is unsigned (Britannica Editors); read live."
    - "Chart-moving this pass: dark hollow → dark filled (A and B support single→corroborated); scores unchanged."
  open_questions:
    - "Full French Sagesse et illusions de la philosophie (1965) beyond the Insights English ch.1 retrospective — any late retreat from immanentism?"
    - "Baptism / childhood catechism details (still thin)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Jean Piaget.\" Encyclopaedia Britannica (revised 12 September 2026). https://www.britannica.com/biography/Jean-Piaget. Read live 2026-10-18; re-checked 2026-10-24."
    url: "https://www.britannica.com/biography/Jean-Piaget"
    accessed: 2026-10-24
    reliability_note: "Unsigned article. Body only; the AI-generated Top Questions and At a Glance are not cited."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, timing, heritage, institutions, collaborators, lane_b]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Jean Piaget"
    citation: "Piaget, Jean. Immanentisme et foi religieuse. Conférence donnée aux anciens membres de l'Association chrétienne d'étudiants à Rolle, le 16 juin 1929. Genève: Libr. H. Robert, 1930, pp. 1–54. Online edition: https://www.unige.ch/piaget/piaget1930a04"
    url: "https://www.unige.ch/piaget/piaget1930a04"
    accessed: 2026-10-18
    reliability_note: "Full text in the University of Geneva's online Piaget edition, with the editors' foreword and notes; an institutional edition, not cut. No page numbers shown."
    source_quality: "primary / own words"
    used_for: [worldview, timing, lane_b, collaborators]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-18
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Jean Piaget"
    citation: "Piaget, Jean. \"Deux types d'attitudes religieuses : immanence et transcendance.\" In Jean Piaget & J. de la Harpe, Deux types d'attitudes religieuses : Immanence et Transcendance. Genève: Éditions de l'Association chrétienne d'étudiants de Suisse romande, 1928, pp. 7–40 (31e Conférence d'étudiants, La Sarraz, March 1928). Online: https://www.unige.ch/piaget/piaget1928a06"
    url: "https://www.unige.ch/piaget/piaget1928a06"
    accessed: 2026-10-24
    reliability_note: "Full text in the University of Geneva's online Piaget edition; institutional transcription of the 1928 brochure. Piaget's part only (de la Harpe's half not used for scoring)."
    source_quality: "primary / own words"
    used_for: [worldview, timing, collaborators]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Jean Piaget"
    citation: "Piaget, Jean. \"Encore « Immanence et transcendance ».\" Cahiers protestants 13 (1929): 325–330. Online: https://www.unige.ch/piaget/piaget1929a06"
    url: "https://www.unige.ch/piaget/piaget1929a06"
    accessed: 2026-10-24
    reliability_note: "Reply to Arnold Reymond clarifying the 1928 lecture; University of Geneva online edition. Used as agreeing third stream, not required for P48 fill."
    source_quality: "primary / own words"
    used_for: [worldview]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Jean Piaget"
    citation: "Piaget, Jean. Insights and Illusions of Philosophy. Translated by Wolfe Mays. New York: Meridian / World Publishing, 1971 (French: Sagesse et illusions de la philosophie, PUF 1965). Chapter 1 autobiographical pages on Bergson, Sabatier, and the 1920s immanentism lectures. PDF consulted 2026-10-24."
    url: "https://rexresearch1.com/PiagetChildPsychologyLibrary/InsightsIllusionsPhilosophyPiaget.pdf"
    accessed: 2026-10-24
    reliability_note: "Published English translation of his 1965 book; ch.1 is own retrospective. Unofficial host PDF; wording checked against the sense of the parallel Autobiographie (1966, unige piaget1966a01). Post-span for axis scoring (P20); used for childhood and P31 continuity."
    source_quality: "primary / own words"
    used_for: [childhood, heritage, worldview]
  - id: S7
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. \"Jean Piaget.\" Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/wiki/Jean_Piaget. Read live 2026-10-24."
    url: "https://en.wikipedia.org/wiki/Jean_Piaget"
    accessed: 2026-10-24
    reliability_note: "Dual-bio check against Britannica (P50). Used for identity/basics consensus and Early-life Protestant note; not for axis scores."
    source_quality: "reference entry"
    used_for: [identity, basics, childhood, heritage]
---

# Jean Piaget

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Jean Piaget (1896–1980), Swiss developmental psychologist [S1; S7]. Draft: primary_system IDEAL (0.5); A 4 at 0.7 corroborated (alt 3); B 3 at 0.7 corroborated (alt 4); D 4 and E 4 at 0.7 corroborated; mid_basin false (0.7). Chart person-dot: dark filled (was dark hollow).

## Life and work

Neuchâtel, Zürich, Paris, Geneva [S1].

## Contribution and impact

Stage theory; The Language and Thought of the Child (1923) to The Origins of Intelligence (1948) [S1].

## Childhood and education

Zoology at Neuchâtel [S1].

## Adult working worldview

'Dieu ... est donc immanent à la pensée' [S2, part III]; 'Dieu est pensée' / miracle rejected as mythological symbol [S4, part III]. Insights: lifelong 'immanentism' from Bergson onward, later more rational [S6].

## Heritage (context only)

Swiss Protestant mother; father a nonbeliever [S6; S7].

## Timing

1923–1948, from age 27 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. God as value [S2].

## Open questions

- Full French *Sagesse et illusions* beyond Insights ch.1 — any late retreat from immanentism?
- Baptism / childhood catechism details.

## Research log

- 2026-10-18: Read Britannica (live) and the full 1930 lecture (University of Geneva online edition).
- 2026-10-24: Deepen D1 — full 1928 Deux types (unige); 1929 Encore reply; Insights ch.1 PDF; Wikipedia EN dual bio. A/B support single→corroborated. No fallacy_catalog. No figures/.
