---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch S)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-18
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-18, by: "Grok Bot", summary: "Record created (stage 3 batch S, order P32: F 4, rank 108). Basics from Britannica (Britannica Editors, unsigned; body only, read live). Worldview from his published lecture Immanentisme et foi religieuse (Geneva, Libr. H. Robert, 1930; given at Rolle on 16 June 1929), read in full in the University of Geneva's online Piaget edition. Scientist (P30, P35 addendum: testable claims about children's cognition). primary_system IDEAL (0.5; alternatives KANT, CHRIST); A 4 (0.7, alt 3); B 3 (0.7, alt 4; P27 free-mind anchor); C BELOW_THRESHOLD; D 4 (0.7); E 4 (0.7); mid_basin false (0.7). Plotted. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit notes for batch S (blind audit of c5d448a, run 1). first_evidence_of_lio_type_views dated 1929 (the lecture given at Rolle on 16 June 1929; printed 1930). primary_system now also cites part I, where 'le Dieu immanent est un Dieu-valeur' stands (the definitions part). No value changes."}

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
  full_name: {value: "Jean Piaget", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  native_name: {value: "Jean Piaget", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "French; same as the display name."}
  aliases:
    - {name: "Jean-Piaget", kind: "roster alias"}

basics:
  birth:
    date: {value: "1896-08-09", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica body."}
    place: {value: "Neuchâtel, Switzerland", modern_name: "Neuchâtel, Switzerland", polity_then: "Switzerland", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1980-09-16", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica body."}
    place: {value: "Geneva, Switzerland", modern_name: "Geneva, Switzerland", polity_then: "Switzerland", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
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
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
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
    cites: [{source: S2, locator: "part I ('un Dieu-valeur'); parts II–III"}]
    rationale: "Critical idealism: 'La pensée qui pose l’être est, en effet, antérieure à l’être'; 'la valeur étant condition de la pensée et la pensée condition de l’être'; God is 'immanent à la pensée', 'un Dieu-valeur', identified 'avec la pensée dans ce qu’elle a de normatif par rapport au moi'. IDEAL's use_when ('reality is mental or thought-like') fits only partly: he calls his position 'exactement intermédiaire entre le réalisme et l’idéalisme' and IDEAL is a stub. Named alternatives: KANT (critical philosophy, but not the moral postulates; KANT's use_when needs both) and CHRIST (he takes Jesus as 'la conscience religieuse la plus pure qui ait jamais existé' and calls immanentism a 'doctrine de vie' within Protestant faith)."
    how_known: "His published lecture, read in the University of Geneva's online edition; contested between three codes, so 0.5 (coder's call)."
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
      cites: [{source: S2, locator: "parts I and III"}]
      rationale: "Immanent pole: he chooses 'l’immanentisme' against the transcendent 'Dieu-cause'; 'Dieu ... est donc immanent à la pensée, c’est-à-dire qu’il agit comme Valeur au cœur même des relations de l’esprit et de l’univers, et non comme Cause'; 'Dieu n’est donc pas un Être qui s’impose à nous du dehors'. God is not a person beyond the norms: 'la personnalité divine ... est précisément identique aux normes de vérité et de bonté'. Named alternative 3: 'Un Dieu immanent à la pensée demeure donc transcendant par rapport au moi' (a stated, limited transcendence)."
      how_known: "Published lecture (1930), inside the working years; alternative named, so 0.7."
      alternatives:
        - {value: 3, note: "'transcendant par rapport au moi'.", cites: [{source: S2, locator: "part III"}]}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      cites: [{source: S2, locator: "parts I–III"}]
      rationale: "Scored on his account of nature (P6). Law without divine exceptions: the transcendent God would be cause 'd’événements particuliers ... c’est-à-dire source de miracles', which he rejects; 'y a-t-il place, dans la nature, pour une autre causalité que la causalité naturelle ? ... nous allons répondre par la négative'; petitionary prayer 'implique ... la croyance en une causalité divine intervenant du dehors' and is 'contradictoire avec l’immanentisme'. The stated limit is a free mind: 'tout, dans le phénomène, est déterminé ... mais le phénomène suppose un esprit libre pour l’élaborer'. Under the P27 anchor a free will outside natural law gives B 3 as the value (Kant's noumenal freedom is the precedent). Named alternative 4: everything in phenomena is determined, and the freedom is only 'la condition de toute science', not an exception within nature."
      how_known: "Published lecture inside the working years; alternative named, so 0.7."
      alternatives:
        - {value: 4, note: "'Il n’y a ainsi jamais ... que du déterminisme' in phenomena.", cites: [{source: S2, locator: "part II"}]}
    C_ledger: {value: BELOW_THRESHOLD, how_known: "Lead only: he rejects 'le drame de l’expiation en tant que voulue par la justice divine' and collective responsibility as 'un scandale moral' (part III), but states no general view of reward and punishment of persons; alternative 3 or 4 (coder's call)."}
    D_authority:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S2, locator: "parts II–III"}]
      rationale: "Observation and reason outrank revelation, which keeps no domain: 'Il n’y a de connaissance que la connaissance scientifique'; an external supernatural revelation is 'le produit naturel et humain de la contrainte psycho-sociale'; 'la révélation se réduit aux prescriptions intérieures de la conscience'. Named alternative 3: conscience keeps a normative say he calls religious, though not as revelation."
      how_known: "Published lecture; alternative named, so 0.7."
      alternatives:
        - {value: 3, note: "Conscience's norms as the 'révélation intérieure'.", cites: [{source: S2, locator: "part III"}]}
    E_scope:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S2, locator: "parts II–III"}]
      rationale: "Scored on the world's order (P7). Same rules everywhere: 'Aucune réalité — réalités sociales et psychiques autant que mécaniques ou chimiques, expériences mystiques les plus intimes autant qu’expérience externe et mesurable — aucune réalité ne paraît aujourd’hui étrangère à ses compétences'; and no favour for petitioners: 'Pourquoi surtout aurait-il créé les choses d’une certaine manière pour les corriger ensuite au profit de ceux qui pactisent avec lui et lui adressent leurs demandes ?' Named alternative 3 on the free mind (as on B)."
      how_known: "Published lecture; alternative named, so 0.7."
      alternatives:
        - {value: 3, note: "The free mind as on B.", cites: [{source: S2, locator: "part II"}]}
  mid_basin: {value: false, certainty: 0.7, cites: [{source: S2, locator: "parts I and III"}], how_known: "P4 test: A 4 (alternative 3, both ≥ 3) at 0.7; the A ≥ 3 branch reads A only (P10)."}
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
  changes_over_life: []
  coder_notes: "Coder's call. One published lecture (1929/1930), inside the working years, carries every axis; the 1928 lecture (Deux types d'attitudes religieuses, with J. de la Harpe) is a lead. No later change of view was read (P31). B 3 follows the P27 free-will anchor by analogy with Kant; if the auditor reads his freedom as a condition of thought rather than an exception to natural law, B would be 4 (alternative named; the plotted point would move from A4/B3 to A4/B4)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Swiss (Neuchâtel)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1923–1948", certainty: 0.7, cites: [{source: S1, locator: "major works paragraph"}], how_known: "Le Langage et la pensée (1923) to La Naissance de l'intelligence (1948), first to last listed lasting contribution (P29, P30). Coder's call: later works (genetic epistemology; the Centre founded 1955) not listed."}
  age_at_first_lasting_contribution: {value: 27, certainty: 0.7, cites: [{source: S1, locator: "opening; major works paragraph"}], how_known: "1923 − 1896 = 27 (P30)."}
  first_evidence_of_lio_type_views: {value: "1929: no causality in nature beside natural causality; God immanent to thought (lecture at Rolle, 16 June 1929; printed 1930)", year: 1929, certainty: 0.5, cites: [{source: S2, locator: "title page; parts I–III"}], how_known: "Dated by the public lecture, not the 1930 printing. Earlier works not read (the 1928 lecture is a lead)."}
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
    - "Worldview rests on one published lecture (1930)."
  open_questions:
    - "Read the 1928 lecture and later writings (Sagesse et illusions de la philosophie, 1965) for a change of view."
    - "Childhood religion (not in the sources read)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Jean Piaget.\" Encyclopaedia Britannica (revised 12 September 2026). https://www.britannica.com/biography/Jean-Piaget. Read live 2026-10-18."
    url: "https://www.britannica.com/biography/Jean-Piaget"
    accessed: 2026-10-18
    reliability_note: "Unsigned article. Body only; the AI-generated Top Questions and At a Glance are not cited."
    used_for: [identity, basics, contribution, childhood, timing, heritage, institutions, collaborators, lane_b]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Jean Piaget"
    citation: "Piaget, Jean. Immanentisme et foi religieuse. Conférence donnée aux anciens membres de l'Association chrétienne d'étudiants à Rolle, le 16 juin 1929. Genève: Libr. H. Robert, 1930, pp. 1–54. Online edition: https://www.unige.ch/piaget/piaget1930a04"
    url: "https://www.unige.ch/piaget/piaget1930a04"
    accessed: 2026-10-18
    reliability_note: "Full text in the University of Geneva's online Piaget edition, with the editors' foreword and notes; an institutional edition, not cut. No page numbers shown."
    used_for: [worldview, timing, lane_b, collaborators]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-18
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Jean Piaget

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Jean Piaget (1896–1980), Swiss developmental psychologist [S1]. Draft: primary_system IDEAL (0.5); A 4 at 0.7 (alt 3); B 3 at 0.7 (alt 4); D 4 and E 4 at 0.7; mid_basin false (0.7). Plotted.

## Life and work

Neuchâtel, Zürich, Paris, Geneva [S1].

## Contribution and impact

Stage theory; The Language and Thought of the Child (1923) to The Origins of Intelligence (1948) [S1].

## Childhood and education

Zoology at Neuchâtel [S1].

## Adult working worldview

'Dieu ... est donc immanent à la pensée' [S2, part III].

## Heritage (context only)

Swiss [S1].

## Timing

1923–1948, from age 27 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. God as value [S2].

## Open questions

- Later writings on religion.

## Research log

- 2026-10-18: Read Britannica (live) and the full 1930 lecture (University of Geneva online edition).
