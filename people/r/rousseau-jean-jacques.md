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
    - {date: 2026-10-18, by: "Grok Bot", summary: "Record created (stage 3 batch S, order P32: F 4, rank 109). Basics from Britannica (Maurice Cranston, signed; opening and 'Formative years', read live) and SEP (Christopher Bertram, 'Life'). Worldview from his own published French texts in the Geneva Collection complète (1782), read in Wikisource's page-linked transcription: the Profession de foi du vicaire savoyard (Émile IV, 1762), the Lettre à Christophe de Beaumont (dated 18 November 1762) and the third Lettre écrite de la montagne (1764). primary_system CHRIST (0.5; alternatives DEISM, which P27 blocks, and CLASS_THEISM); A 1 (0.7, alt 0); B 3 (0.7, alt 4; P27 free-will anchor); D 3 (0.5, alt 4); mid_basin true (0.7). Plotted. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit fixes for batch S (blind audit of c5d448a, run 1: RO6 WEAKEN; rulings S1 and S2, v8's calls on the auditor's advice). Scoring the Vicar's speech now cites P42 and its v8 addendum (ruling S2: a character's words count as the author's view when a text in the author's own voice adopts them, at that text's certainty), with the own-voice texts and the counter-evidence: Émile t. 5, p. 112 ('non comme une regle'); Beaumont t. 6, pp. 36 and 52; Lettres écrites de la montagne II, t. 6, p. 171 ('mes articles fondamentaux') and III, pp. 182–183 with its note. Ruling S1: P27's 'declines to contest it' covers the Vicar's suspension, so CHRIST stays (ruling question closed). The 1764 cap cites P1 (under P20). Rameau dispute dated 1752. No value changes."}

identity:
  id: rousseau-jean-jacques
  display_name: "Jean-Jacques Rousseau"
  roster:
    canonical_name: "Jean-Jacques Rousseau"
    rank: 109
    F: 4
    models: [Claude, Gemini, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Jean-Jacques Rousseau", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  native_name: {value: "Jean-Jacques Rousseau", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "French; same as the display name."}
  aliases:
    - {name: "Jean-Jacques-Rousseau", kind: "roster alias"}
    - {name: "Rousseau-Jean-Jacques", kind: "roster alias"}

basics:
  birth:
    date: {value: "1712-06-28", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica body."}
    place: {value: "Geneva", modern_name: "Geneva, Switzerland", polity_then: "Republic of Geneva", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "§1 ('the independent Calvinist city-state of Geneva')"}], how_known: "Britannica; polity from SEP."}
  death:
    date: {value: "1778-07-02", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica body."}
    place: {value: "Ermenonville, France", modern_name: "Ermenonville, France", polity_then: "Kingdom of France", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1750, certainty: 0.7, cites: [{source: S1, locator: "'Formative years'"}], how_known: "Discours sur les sciences et les arts, dated 1750 by Britannica (the Dijon prize essay); SEP gives its publication as 1751 (S2, §1). The prize award is the earliest public statement (P30), so 1750; noted in data_quality_flags."}
  era_bucket: {value: "1750 to 1849", certainty: 0.7, cites: [{source: S1, locator: "'Formative years'"}], how_known: "1750 (P2: an edge year goes to the later bucket); 1751 gives the same bucket."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Switzerland (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "'Formative years'"}, {source: S2, locator: "§1"}], how_known: "Paris and Montmorency (France); Switzerland in exile."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["French"], certainty: 0.7, cites: [{source: S3, locator: "title pages"}], how_known: "His works as printed."}
  occupations: {value: ["philosopher", "writer", "political theorist", "composer", "music copyist"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Formative years'"}, {source: S2, locator: "§1"}], how_known: "Britannica and SEP."}

contribution:
  fields: {value: ["political philosophy", "moral philosophy", "philosophy of education", "literature", "music"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "§1"}], how_known: "Britannica and SEP."}
  lasting_original_contributions:
    - {value: "Discours sur les sciences et les arts (the First Discourse): people good by nature, corrupted by society", year: 1750, kind: work, lasting: "'its central theme was to inform almost everything else he wrote' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Formative years'"}, {source: S2, locator: "§1"}], how_known: "Britannica dates it 1750; SEP gives publication 1751 and calls it 'mainly important because Rousseau used it to introduce themes that he developed further in later work'."}
    - {value: "Discourse on the Origin and Foundations of Inequality (the Second Discourse)", year: 1755, kind: work, lasting: "'a far more accomplished work', where he 'begins to develop his theories of human social development and moral psychology' (S2)", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP."}
    - {value: "Julie, ou La Nouvelle Héloïse", year: 1761, kind: work, lasting: "'an immediate success' and 'an important supplementary source for the interpretation of Rousseau’s social philosophy' (S2)", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP."}
    - {value: "The Social Contract (Du contrat social)", year: 1762, kind: work, lasting: "with Émile, 'the high point of Rousseau’s intellectual achievement' (S2); his treatises 'inspired the leaders of the French Revolution' (S1)", certainty: 0.7, cites: [{source: S2, locator: "§1"}, {source: S1, locator: "opening"}], how_known: "SEP."}
    - {value: "Émile, ou De l'éducation", year: 1762, kind: work, lasting: "with The Social Contract, 'the high point of Rousseau’s intellectual achievement' (S2); 'he taught parents to take a new interest in their children and to educate them differently' (S1)", certainty: 0.7, cites: [{source: S2, locator: "§1"}, {source: S1, locator: "opening"}], how_known: "SEP; the latest listed item (coder's call: the Confessions, completed in later life and published 1782–89, are not listed; see timing)."}
  evidence_of_impact:
    - {value: "'the least academic of modern philosophers and in many ways ... the most influential'; his works 'inspired the leaders of the French Revolution and the Romantic generation'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1, S2).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Genevan Calvinist", certainty: 0.5, cites: [{source: S2, locator: "§1"}, {source: S1, locator: "'Formative years' ('his Calvinist blood')"}], how_known: "Born a citizen's son in Calvinist Geneva and later 'reconverting to Calvinism' (S2); the household's practice is not given."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not in the sources read."}
  parents_and_household:
    - {value: "Father Isaac Rousseau, a watchmaker; mother Suzanne Bernard, who died nine days after his birth; raised and educated by his father until ten", role: parents, certainty: 0.7, cites: [{source: S2, locator: "§1"}, {source: S1, locator: "'Formative years'"}], how_known: "SEP; Britannica says she died in childbirth."}
  household_circumstances: {value: "After his father fled Geneva, he lived six years as 'a poor relation in his mother’s family'", certainty: 0.7, cites: [{source: S1, locator: "'Formative years'"}], how_known: "Britannica."}
  schooling:
    - {value: "Father's 'haphazard education' (Plutarch and historians of ancient republics)", stage: home, run_by: family, certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP."}
    - {value: "In the care of a pastor at Bossey", stage: tutor, run_by: "religious body", certainty: 0.5, cites: [{source: S2, locator: "§1"}], how_known: "SEP; stage and run_by are the coder's reading of 'put in the care of a pastor'."}
    - {value: "Apprenticed to an engraver", stage: apprenticeship, certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP; Britannica says he 'had never been to school'."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading:
    - {value: "Plutarch and historians of ancient republicanism", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP."}
  childhood_mentors: []
  languages_in_childhood: {value: ["French"], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading (Geneva)."}
  notable_events:
    - {value: "Left Geneva at sixteen; converted to Roman Catholicism in Turin", year: 1728, certainty: 0.7, cites: [{source: S2, locator: "§1 ('April 1728')"}, {source: S1, locator: "'Formative years'"}], how_known: "SEP."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1750–1762", certainty: 0.7, cites: [{source: S1, locator: "'Formative years'"}, {source: S2, locator: "§1"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Genevan Reformed church (readmitted 1754, regaining his citizenship)", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP; context only."}
  self_described_science_religion_relation: {value: "God is known from motion and its laws: 'la matiere mue selon de certaines loix me montre une intelligence' (1762); miracles, as exceptions to laws, can never be known to be miracles, since that would need knowledge of all the laws of nature (1764)", certainty: 0.7, cites: [{source: S3, locator: "t. 5, p. 29"}, {source: S5, locator: "t. 6, pp. 192–195"}], how_known: "His published texts in a web transcription of the 1782 edition (cap 0.7); the 1764 letter is after the working years (P1, under P20)."}
  primary_system:
    value: CHRIST
    basis: written_profession
    certainty: 0.5
    cites: [{source: S4, locator: "t. 6, p. 52"}, {source: S3, locator: "t. 5, pp. 97–100"}]
    rationale: "Self-description in his reply to the Archbishop of Paris (dated 18 November 1762): 'je suis Chrétien, & sincérement Chrétien, selon la doctrine de l’Evangile ... non comme un disciple des Prêtres, mais comme un disciple de Jésus-Christ', with the Profession de foi named as his own best writing. The creed is a natural religion: God known from motion and order, conscience, the Gospel's 'majesté' admired, but revelation neither admitted nor rejected. Named alternatives: DEISM (creator known by reason; miracles and church authority rejected as sources), which P27 blocks because the Profession says of revelation 'je ne l’admets ni ne la rejette' (DEISM's do_not_use_when: 'declines to contest it'); and CLASS_THEISM (an a posteriori argument from motion to a first will, P22), rejected because God is not held simple or immutable in what was read."
    how_known: "Published works in a web transcription of the 1782 Geneva edition (cap 0.7); contested between three codes, and the self-label is a defence against censure, so 0.5 (coder's call). Ruling S1 (v8's call on the auditor's advice): P27's 'declines to contest it' covers the Vicar's 'je ne l’admets ni ne la rejette', so DEISM stays blocked. In his own voice he goes further: 'Je me déclare Chrétien'; 'il n’est pas vrai que je rejette les autres preuves' of revelation; his persecutors count for nothing 'que je l’admette sur les preuves qui me convainquent'; and a note says the Vicar's scepticism 'ne prouve en aucune façon le mien' (S5, Lettre III, t. 6, pp. 182–183; after the working years, P1)."
  secondary_system: {value: UNKNOWN, how_known: "One system (P29)."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Self-label 'sincérement Chrétien, selon la doctrine de l’Evangile' (1762)."}
    - {code: DEISM, reason: "Natural religion from motion and order; miracles not proofs; 'Que d’hommes entre Dieu & moi !' (S3, t. 5, p. 76). Blocked by P27 (ruling S1): he neither admits nor rejects revelation (S3, t. 5, p. 97), and in his own voice admits it on the proofs that convince him (S5, Lettre III, t. 6, p. 183)."}
    - {code: CLASS_THEISM, reason: "First-cause argument from motion to a will (S3, t. 5, pp. 25–26); rejected: no simple, immutable God stated."}
  lio_axes:
    A_locus:
      value: 1
      basis: written_profession
      certainty: 0.7
      cites: [{source: S3, locator: "t. 5, pp. 33–34"}, {source: S4, locator: "t. 6, p. 52"}]
      rationale: "Transcendent person, limited: God is 'Cet Être qui veut et qui peut, cet Être actif par lui-même', with 'intelligence', 'puissance', 'volonté' and 'bonté'; he 'existe par lui-même' and 'mon existence est subordonnée à la sienne'. The limit: God is perceived 'par-tout dans ses œuvres, je le sens en moi', and his nature 'm’échappe'; no petition or particular intervention is described. Named alternative 0 (a willing, intelligent creator outside the world), on the same side of the mid_basin test."
      how_known: "P42: the Vicar's words are a character's, so they count as Rousseau's only because texts in his own voice adopt them, at the certainty of the adopting text (P42 addendum, v8's call, ruling S2). Inside the working years, the 1762 letter owns the Profession (S4, t. 6, p. 52: 'je la tiendrai toujours pour l’Ecrit le meilleur & le plus utile'); after them, Lettres écrites de la montagne II names its first part, which carries A and B, as his own: 'toute la premiere partie de celle du Vicaire est affirmative ... Voilà, Messieurs, mes articles fondamentaux' (S5, t. 6, p. 171; P1). Counter-evidence weighed: the narrator's 'J’ai transcrit cet écrit, non comme une regle des sentimens qu’on doit suivre en matiere de religion, mais comme un exemple de la maniere dont on peut raisonner avec son Éleve' (S3, t. 5, p. 112) concerns teaching method, not belief; and he keeps the voices apart ('c’est moi-même, & non le Vicaire', S4, t. 6, p. 36, of a passage in the body of the book). Web transcription, cap 0.7."
      alternatives:
        - {value: 0, note: "A willing, intelligent creator distinct from the world.", cites: [{source: S3, locator: "t. 5, pp. 33–34"}]}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      cites: [{source: S3, locator: "t. 5, pp. 25–29; p. 41"}, {source: S5, locator: "t. 6, pp. 192–195"}]
      rationale: "Scored on his account of nature (P6). Lawful nature: matter moves 'selon de certaines loix', and 'L’expérience & l’observation nous ont fait connoître les loix du mouvement'; the stated exception is a free will not bound by mechanism: 'L’homme est donc libre dans ses actions, &, comme tel animé d’une substance immatérielle ; c’est mon troisieme article de foi' (P27 anchor: a free will gives B 3 as the value, as for Descartes and Kant). Miracles are not admitted as part of how events go: in 1764 he defines one as 'une exception réelle & visible à ses Loix', grants that God can work them, says the highest ideas of divine wisdom 'seroient pour la négative', and that no one can know a fact to be a miracle ('Ils seroient mille, que je ne les en croirois pas'). Named alternative 4: no miracle is accepted, and the free will may be read as outside nature."
      how_known: "The 1762 Profession (inside the working years, owned in the 1762 letter) carries the score; the 1764 letter is after the working years and counts at 0.5 for its own point (P1, under P20). The Vicar's words count as his under P42 and its addendum (ruling S2), as set out under A_locus. Web transcription, cap 0.7."
      alternatives:
        - {value: 4, note: "No miracle admitted; strict lawfulness with the will placed outside nature.", cites: [{source: S5, locator: "t. 6, p. 193"}]}
    C_ledger: {value: UNKNOWN, how_known: "The Profession's pages on the soul's survival and Providence's justice (t. 5, pp. 42–50) were not coded (coder's call; lead)."}
    D_authority:
      value: 3
      basis: written_profession
      certainty: 0.5
      cites: [{source: S3, locator: "t. 5, pp. 76; 97–100"}]
      rationale: "Reason and conscience lead: 'Que d’hommes entre Dieu & moi !'; he rejects 'l’obligation de la reconnoître' (revelation) as incompatible with God's justice, and 'quant aux dogmes qui n’influent ni sur les actions, ni sur la morale ... je ne m’en mets nullement en peine'. Religion keeps one limited say: the Gospel is to be respected 'en silence' where it can be neither rejected nor understood. Named alternative 4: no domain where revelation decides."
      how_known: "The Profession, owned in the 1762 letter (P42 addendum, ruling S2); contested reading, 0.5."
      alternatives:
        - {value: 4, note: "Revelation keeps no deciding say.", cites: [{source: S3, locator: "t. 5, p. 97"}]}
    E_scope: {value: UNKNOWN, how_known: "Not coded from what was read (P7)."}
  mid_basin: {value: true, certainty: 0.7, cites: [{source: S3, locator: "t. 5, pp. 29–41"}], how_known: "P4 test: A 1 (≤ 1, alternative 0 on the same side) at 0.7 and B 3 (≥ 3, alternative 4 on the same side) at 0.7, B scored on his account of nature (P6); the cap uses the certainty of the condition (P30, §6)."}
  statements:
    - text: "Je crois donc qu’une volonté meut l’Univers & anime la Nature. Voilà mon premier dogme, ou mon premier article de foi."
      cites: [{source: S3, locator: "t. 5, p. 26"}]
      date: "1762"
      context: "Profession de foi du vicaire savoyard, in Émile IV (1762), after the argument that 'Les premieres causes du mouvement ne sont point dans la matiere'. Spoken by the Vicar; Rousseau owns the Profession in S4."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-18
      note: "Wikisource transcription linked to page images of the Geneva 1782 Collection complète; treated as a web copy (cap 0.7)."
    - text: "Si la matiere mue me montre une volonté, la matiere mue selon de certaines loix me montre une intelligence : c’est mon second article de foi."
      cites: [{source: S3, locator: "t. 5, p. 29"}]
      date: "1762"
      context: "Same text."
      axes: [B_cause, A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-18
      note: "As above."
    - text: "Cet Être qui veut et qui peut, cet Être actif par lui-même ; cet Être, enfin, quel qu’il soit, qui meut l’Univers & ordonne toutes choses, je l’appelle Dieu."
      cites: [{source: S3, locator: "t. 5, pp. 33–34"}]
      date: "1762"
      context: "Same text; he goes on: 'J’apperçois Dieu par-tout dans ses œuvres, je le sens en moi, je le vois tout autour de moi ; mais sitôt que je veux le contempler en lui-même ... il m’échappe'."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-18
      note: "'et' as in the transcription."
    - text: "L’homme est donc libre dans ses actions, &, comme tel animé d’une substance immatérielle ; c’est mon troisieme article de foi."
      cites: [{source: S3, locator: "t. 5, p. 41"}]
      date: "1762"
      context: "Same text, after 'Le principe de toute action est dans la volonté d’un être libre'."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-18
      note: ""
    - text: "Il y a tant de raisons solides pour & contre, que ne sachant à quoi me déterminer, je ne l’admets ni ne la rejette ; je rejette seulement l’obligation de la reconnoître, parce que cette obligation prétendue est incompatible avec la justice de Dieu"
      cites: [{source: S3, locator: "t. 5, p. 97"}]
      date: "1762"
      context: "Same text, on revelation ('À l’égard de la révélation ...'); the passage that blocks DEISM under P27."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-18
      note: "Sentence continues in the source."
    - text: "Monseigneur, je suis Chrétien, & sincérement Chrétien, selon la doctrine de l’Evangile. Je suis Chrétien, non comme un disciple des Prêtres, mais comme un disciple de Jésus-Christ."
      cites: [{source: S4, locator: "t. 6, p. 52"}]
      date: "1762-11-18"
      context: "Jean-Jacques Rousseau, citoyen de Genève, à Christophe de Beaumont, Archevêque de Paris, answering the archbishop's pastoral letter condemning Émile; dated 18 November 1762, published 1763. Just before, he says he will always hold the Profession 'pour l’Ecrit le meilleur & le plus utile dans le siecle où je l’ai publié'."
      axes: [A_locus, D_authority]
      kind: "published letter"
      verified_against: "primary transcription"
      verified_on: 2026-10-18
      note: "As above."
    - text: "Un miracle est, dans un fait particulier, un acte immédiat de la puissance divine, un changement sensible dans l’ordre de la nature, une exception réelle & visible à ses Loix."
      cites: [{source: S5, locator: "t. 6, p. 192 (Lettre III)"}]
      date: "1764"
      context: "Lettres écrites de la montagne, third letter, answering the Genevan condemnation; he grants 'quel homme a jamais nié que Dieu pût faire des miracles ?', says the highest ideas of divine wisdom 'seroient pour la négative', and of witnesses 'Ils seroient mille, que je ne les en croirois pas' (p. 193). After the working years (P1, under P20)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-18
      note: "As above."
    - text: "Presque toute la profession de foi de la Julie est affirmative ; toute la premiere partie de celle du Vicaire est affirmative, la moitié de la seconde partie est encore affirmative ; une partie du chapitre de la Religion civile est affirmative ; la Lettre à M. l’Archevêque de Paris est affirmative. Voilà, Messieurs, mes articles fondamentaux : voyons les vôtres."
      cites: [{source: S5, locator: "t. 6, p. 171 (Lettre II)"}]
      date: "1764"
      context: "Lettres écrites de la montagne, second letter, answering the Genevan ministers' charge that he left the fundamentals of his Christianity unstated. After the working years (P1, under P20)."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Own-voice adoption of the Profession's first part (P42 addendum, ruling S2)."
    - text: "J’Ai transcrit cet écrit, non comme une regle des sentimens qu’on doit suivre en matiere de religion, mais comme un exemple de la maniere dont on peut raisonner avec son Éleve, pour ne point s’écarter de la méthode que j’ai tâché d’établir."
      cites: [{source: S3, locator: "t. 5, p. 112"}]
      date: "1762"
      context: "Émile IV, the narrator's words straight after the Profession's 'Amen'."
      axes: []
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Counter-evidence to the adoption, weighed under P42: it concerns teaching method, not belief (ruling S2)."
  changes_over_life:
    - {value: "Converted to Roman Catholicism in Turin (April 1728); readmitted to the Genevan Reformed church in 1754, regaining his citizenship", year: 1754, certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP. The 1754 return precedes four of the five listed works; the affiliation change does not bear on the axes read (coder's call)."}
  coder_notes: "Coder's call. The Profession is the Vicar's speech (P42), but Rousseau owns it in his own voice in the letter to Beaumont (dated 18 November 1762, inside the working years) and names its first part as 'mes articles fondamentaux' in 1764 (LEM II, t. 6, p. 171), so it is scored as his written profession under the P42 addendum (ruling S2, v8's call). Span ends with Émile and The Social Contract (1762); the Confessions (finished in later life, published 1782–89) would extend it to about 1770 without changing a value, and the 1764 Lettres would then fall inside it. Ruling S1 (v8's call): P27's 'declines to contest it' covers the Vicar's 'je ne l’admets ni ne la rejette', so CHRIST stays. Leads: the Lettre à Voltaire sur la Providence (1756); the Rêveries, third walk."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Genevan citizen family", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP."}
  religious_heritage_by_birth: {value: "Calvinist (Geneva)", certainty: 0.5, cites: [{source: S2, locator: "§1"}], how_known: "SEP (Calvinist city-state; he later reconverted to Calvinism)."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1750–1762", certainty: 0.7, cites: [{source: S1, locator: "'Formative years'"}, {source: S2, locator: "§1"}], how_known: "First Discourse (1750) to Émile and The Social Contract (1762), first to last listed lasting contribution (P29, P30). Coder's call on the end: the Confessions are not listed (alternative end about 1770)."}
  age_at_first_lasting_contribution: {value: 38, certainty: 0.7, cites: [{source: S1, locator: "opening; 'Formative years'"}], how_known: "1750 − 1712 = 38 (P30)."}
  first_evidence_of_lio_type_views: {value: "1762: matter moved 'selon de certaines loix'; a free will the one exception (Profession de foi)", year: 1762, certainty: 0.5, cites: [{source: S3, locator: "t. 5, pp. 29, 41"}], how_known: "Earlier works not read (the 1756 letter to Voltaire on Providence is a lead)."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S3, locator: "t. 5, p. 29"}], how_known: "1762 falls inside 1750–1762."}
  worldview_during_major_work: {value: "Natural religion professed as Gospel Christianity: a willing, intelligent God known from motion and order; revelation neither admitted nor rejected", certainty: 0.5, cites: [{source: S3, locator: "t. 5, pp. 26–34, 97"}, {source: S4, locator: "t. 6, p. 52"}], how_known: "His 1762 texts."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "The Profession proceeds by numbered 'articles de foi' deduced from first principles ('De ces trois premiers vous déduirez aisément tous les autres').", certainty: 0.5, cites: [{source: S3, locator: "t. 5, p. 41"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Formative years'"}], how_known: "Self-taught under Mme de Warens (S1); not read further."}
  circle_present: {value: "no", rationale: "God distinct from the world, perceived in his works.", certainty: 0.5, cites: [{source: S3, locator: "t. 5, pp. 33–34"}], how_known: "Coder's reading."}
  reading: "A mid-basin natural religion: a willing God behind a lawful nature, with human freedom as the one exception."
  notes: ""

institutions:
  - {value: "French embassy in Venice", role: "secretary to the ambassador", years: "1743–1744", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "'Controversy with Rameau'"}, {source: S2, locator: "§1"}], how_known: "Britannica."}
  - {value: "Encyclopédie of Diderot and d'Alembert", role: "contributor (music)", years: UNKNOWN, kind: other, certainty: 0.7, cites: [{source: S1, locator: "'Formative years'"}], how_known: "Britannica."}
collaborators:
  - {value: "Françoise-Louise de la Tour, baronne de Warens", relation: "mentor or employer", note: "benefactor; furthered his education; he became her steward", certainty: 0.7, cites: [{source: S1, locator: "'Formative years'"}, {source: S2, locator: "§1"}], how_known: "Britannica and SEP."}
  - {value: "Denis Diderot", relation: collaborator, note: "the Encyclopédie circle", certainty: 0.7, cites: [{source: S1, locator: "'Formative years'"}], how_known: "Britannica."}
  - {value: "Jean-Philippe Rameau", relation: "rival or critic", note: "melody against harmony (1752)", certainty: 0.7, cites: [{source: S1, locator: "'Controversy with Rameau'"}], how_known: "Britannica."}
  - {value: "David Hume", roster_id: hume-david, relation: other, note: "invited him to England (1766); Rousseau came to think Hume plotted against him", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S6, locator: "roster.csv, rank 109"}], how_known: "Study roster."}
  controversies:
    - {value: "Émile condemned in Paris; Émile and The Social Contract condemned in Geneva 'on grounds of their religious heterodoxy' (1762)", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP."}
  data_quality_flags:
    - "First Discourse: Britannica 1750, SEP publication 1751; 1750 kept (prize, P30)."
    - "Mother's death: Britannica 'in childbirth', SEP 'nine days after his birth'."
    - "Primary texts read in Wikisource's transcription of the 1782 Collection complète (page images linked); treated as a web copy (cap 0.7); page numbers are the printed ones."
  open_questions:
    - "Code C from the Profession's pages on the soul and Providence (t. 5, pp. 42–50)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Maurice Cranston"
    citation: "Cranston, Maurice. \"Jean-Jacques Rousseau.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Jean-Jacques-Rousseau. Read live 2026-10-18 (opening, 'Formative years', 'Controversy with Rameau'; later sections did not load)."
    url: "https://www.britannica.com/biography/Jean-Jacques-Rousseau"
    accessed: 2026-10-18
    reliability_note: "Signed article. Body only; the AI-generated Top Questions and At a Glance are not cited."
    used_for: [identity, basics, contribution, childhood, institutions, collaborators, lane_b]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Christopher Bertram"
    citation: "Bertram, Christopher. \"Jean Jacques Rousseau.\" Stanford Encyclopedia of Philosophy (substantive revision 21 April 2023). https://plato.stanford.edu/entries/rousseau/"
    url: "https://plato.stanford.edu/entries/rousseau/"
    accessed: 2026-10-18
    reliability_note: "Signed scholarly encyclopedia; §1 'Life' used."
    used_for: [basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators, review]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Jean-Jacques Rousseau"
    citation: "Rousseau, J.-J. Émile, ou De l'éducation, Livre IV (Profession de foi du vicaire savoyard), in Collection complète des œuvres de J. J. Rousseau, t. 5 (Genève, 1782). Wikisource transcription: https://fr.wikisource.org/wiki/Émile,_ou_De_l’éducation/Édition_1782/Livre_IV"
    url: "https://fr.wikisource.org/wiki/%C3%89mile,_ou_De_l%E2%80%99%C3%A9ducation/%C3%89dition_1782/Livre_IV"
    accessed: 2026-10-18
    reliability_note: "Proofread transcription keyed to page images of the 1782 edition; printed page numbers from the page links; web copy, cap 0.7."
    used_for: [worldview, timing, lane_b]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Jean-Jacques Rousseau"
    citation: "Rousseau, J.-J. Jean-Jacques Rousseau, citoyen de Genève, à Christophe de Beaumont, archevêque de Paris (dated 18 November 1762), in Collection complète des œuvres de J. J. Rousseau, t. 6 (Genève, 1782), pp. 3–118. Wikisource transcription: https://fr.wikisource.org/wiki/À_Christophe_de_Beaumont"
    url: "https://fr.wikisource.org/wiki/%C3%80_Christophe_de_Beaumont"
    accessed: 2026-10-18
    reliability_note: "As S3."
    used_for: [worldview, timing]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Jean-Jacques Rousseau"
    citation: "Rousseau, J.-J. Lettres écrites de la montagne (1764), Lettre II (p. 171) and Lettre III (pp. 179–216), in Collection complète des œuvres de J. J. Rousseau, t. 6 (Genève, 1782). Wikisource transcription: https://fr.wikisource.org/wiki/Lettres_écrites_de_la_montagne/Texte_entier"
    url: "https://fr.wikisource.org/wiki/Lettres_%C3%A9crites_de_la_montagne/Texte_entier"
    accessed: 2026-10-18
    reliability_note: "As S3. After the working years (P1 cap 0.5, under P20)."
    used_for: [worldview]
  - id: S6
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-18
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Jean-Jacques Rousseau

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Jean-Jacques Rousseau (1712–1778), Genevan-born philosopher and writer [S1]. Draft: primary_system CHRIST (0.5; DEISM blocked by P27, CLASS_THEISM rejected); A 1 at 0.7 (alt 0); B 3 at 0.7 (alt 4); D 3 at 0.5 (alt 4); mid_basin true (0.7). Plotted.

## Life and work

Geneva, Savoy, Paris, exile [S1; S2].

## Contribution and impact

The two Discourses, Julie, The Social Contract and Émile (1750–1762) [S1; S2].

## Childhood and education

Calvinist Geneva; Catholic convert at sixteen; self-taught [S1; S2].

## Adult working worldview

'une volonté meut l’Univers & anime la Nature'; 'la matiere mue selon de certaines loix me montre une intelligence' [S3, t. 5, pp. 26, 29]; 'je suis Chrétien, & sincérement Chrétien, selon la doctrine de l’Evangile' [S4, t. 6, p. 52].

## Heritage (context only)

Genevan Calvinist [S2].

## Timing

1750–1762, from age 38 [S1; S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. A willing God behind lawful nature [S3].

## Open questions

- Ruling question R-S1 (DEISM and P27).
- C from the Profession (t. 5, pp. 42–50).

## Research log

- 2026-10-18: Read Britannica (live, first sections), SEP §1, and the three French texts in Wikisource (page-linked 1782 edition).
