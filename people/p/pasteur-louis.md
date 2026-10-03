---
record:
  record_type: person
  schema_version: "1.2"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, third batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages and library scans"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (third batch, RUNBOOK §1 order). Basics from Britannica (Ullmann; opening, 'Research career', 'Spontaneous generation', 'Vaccine development') and the ENS portrait page. Worldview from his Académie française reception speech of 27 April 1882, read in the 1882 Calmann Lévy printing (Wellcome Collection scan; pp. 3–4, 20, 23–24, 26 checked on the page images) and compared with the Académie française's own online text. primary_system BELOW_THRESHOLD (CHRIST considered). B 4 (0.7), D 2 (0.7); A, C, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Decision P9: death place now Marnes-la-Coquette (the Villeneuve-l'Étang estate) at 0.5, with Saint-Cloud as the alternative (new source S6, EPHE prosopography; certainty 0.7 → 0.5 because the sources name different communes); era 1750 to 1849 applied literally from 1848, boundary noted (unchanged); French spiritualism recorded as a named candidate without a code. No worldview score changed. Schema 1.1 → 1.2."}

identity:
  id: pasteur-louis
  display_name: "Louis Pasteur"
  roster:
    canonical_name: "Louis Pasteur"
    rank: 114
    F: 4
    models: [Claude, DeepSeek, Gemini, Grok]
    band: "core (3–4)"
    status: core
    field: chemistry
    field_bucket: chemistry
  full_name: {value: "Louis Pasteur", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources."}
  native_name: {value: "Louis Pasteur (French)", certainty: 1.0, cites: [{source: S3, locator: "title page"}], how_known: "Same spelling in French."}
  aliases:
    - {name: "Pasteur-Louis", kind: "roster alias"}

basics:
  birth:
    date: {value: "1822-12-27", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "paragraph 1 (year)"}], how_known: "Britannica gives the day; ENS agrees on the year and place."}
    place: {value: "Dole, Jura", modern_name: "Dole, Jura, France", polity_then: "Kingdom of France", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources agree."}
  death:
    date: {value: "1895-09-28", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening; 'Vaccine development'"}, {source: S2, locator: "death paragraph"}], how_known: "Two sources agree."}
    place: {value: "Marnes-la-Coquette (the Villeneuve-l'Étang estate)", modern_name: "Marnes-la-Coquette, Hauts-de-Seine, France", polity_then: "French Third Republic", certainty: 0.5, cites: [{source: S2, locator: "death paragraph ('Marnes-la-Coquette')"}, {source: S6, locator: "'Décès' line ('Villeneuve-l'Etang (act. Marnes-la-Coquette, France)')"}], how_known: "ENS gives Marnes-la-Coquette; the EPHE notice gives the estate, Villeneuve-l'Étang, 'act. Marnes-la-Coquette'. Britannica gives Saint-Cloud, the form most sources use (the estate adjoins the Saint-Cloud park). Reliable sources name different communes, so 0.5 with the alternative (CODING_GUIDE §3). Value chosen by decision P9 (2026-10-02).", alternatives: [{value: "Saint-Cloud", cites: [{source: S1, locator: "opening ('Saint-Cloud')"}], note: "The form most general sources give."}]}
  first_lasting_contribution_year: {value: 1848, certainty: 0.5, cites: [{source: S1, locator: "'Research career', paragraph 2"}], how_known: "Molecular asymmetry, which Britannica places 'soon after graduating' (doctorate 1847, Dijon post 1848) without a year; 1848 is the coder's dating."}
  era_bucket: {value: "1750 to 1849", certainty: 0.5, cites: [{source: S1, locator: "'Research career'"}], how_known: "P2 applied literally to the recorded first_lasting_contribution_year (1848), as decision P9 (2026-10-02) directs; the certainty follows the year's 0.5. He is on the boundary: a first lasting contribution dated 1850 or later (for example the 1857 germ theory of fermentation) would give 1850 to 1949. Membership in the 1600–1950 pool is not affected either way."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "France is Western Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "'Research career'"}], how_known: "Strasbourg, Lille and Paris."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "As the sources record it."}
  languages_of_work: {value: [French], certainty: 1.0, cites: [{source: S3, locator: "title page"}], how_known: "His works and speeches are in French."}
  occupations: {value: [chemist, microbiologist, "university professor", "institute director"], certainty: 1.0, cites: [{source: S1, locator: "opening; 'Research career'"}, {source: S2, locator: "paragraphs 1–3"}], how_known: "Two sources."}

contribution:
  fields: {value: [chemistry, microbiology, immunology], certainty: 1.0, cites: [{source: S1, locator: "opening; 'Vaccine development'"}, {source: S2, locator: "paragraphs 2–5"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Molecular asymmetry (optical isomerism of tartrates), the foundation of stereochemistry", year: "c. 1848", kind: discovery, lasting: "foundation of stereochemistry", certainty: 1.0, cites: [{source: S1, locator: "'Research career', paragraph 2"}], how_known: "Britannica; year is the coder's dating."}
    - {value: "Germ theory of fermentation; aerobic and anaerobic life", year: "1857–1861", kind: theory, lasting: "basis of microbiology", certainty: 1.0, cites: [{source: S1, locator: "'Research career', paragraphs 4–5"}, {source: S2, locator: "paragraph 2"}], how_known: "Two sources."}
    - {value: "Experimental refutation of spontaneous generation (swan-neck flasks)", year: "1859–1864", kind: discovery, lasting: "grounded sterile technique and bacteriology", certainty: 1.0, cites: [{source: S1, locator: "'Spontaneous generation', paragraph 1"}, {source: S3, locator: "pp. 3–4"}], how_known: "Britannica and his own account."}
    - {value: "Pasteurization", year: "1863–1865", kind: invention, lasting: "in universal use", certainty: 1.0, cites: [{source: S1, locator: "'Research career'"}, {source: S2, locator: "pasteurization paragraph (1865 patent)"}], how_known: "Two sources."}
    - {value: "Attenuated vaccines (chicken cholera, anthrax, rabies) and the general principle of vaccination", year: "1879–1885", kind: method, lasting: "foundation of immunology", certainty: 1.0, cites: [{source: S1, locator: "'Vaccine development'"}, {source: S2, locator: "vaccination paragraph"}], how_known: "Two sources."}
  evidence_of_impact:
    - {value: "Some 30 institutes and many hospitals, schools and streets bear his name", kind: "named after them", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Discours de réception à l'Académie française (eulogy of Littré)", year: 1882, kind: "other", certainty: 1.0, cites: [{source: S3, locator: "title page"}], how_known: "Library scan of the 1882 printing."}
  honours:
    - {value: "Elected to the Académie des sciences", year: 1862, certainty: 1.0, cites: [{source: S1, locator: "'Spontaneous generation', paragraph 2"}], how_known: "Britannica."}
    - {value: "Elected to the Académie française (seat of Littré)", year: 1882, certainty: 1.0, cites: [{source: S1, locator: "'Vaccine development'"}, {source: S4, locator: "page heading"}], how_known: "Two sources."}
    - {value: "Legion of Honour", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica (no year given)."}
  definition_fit: {value: "clearly meets", rationale: "Founder of medical microbiology.", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Sources agree."}

childhood:
  family_religion: {value: TODO, note: "Catholic by general report; not stated in the sources read."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father, Jean-Joseph Pasteur, tanner and decorated sergeant major of the Napoleonic Wars", name: "Jean-Joseph Pasteur", role: father, certainty: 1.0, cites: [{source: S1, locator: "'Early education'; Top Questions"}], how_known: "Britannica (two passages)."}
  household_circumstances: {value: "Relatively poor family of a tanner, one of four children; the family moved from Dole to Arbois", certainty: 0.7, cites: [{source: S1, locator: "Top Questions; 'Early education'"}], how_known: "Britannica."}
  schooling:
    - {value: "Primary school, Arbois", stage: "dame or charity school", years: TODO, certainty: 0.7, cites: [{source: S1, locator: "'Early education'"}], how_known: "Britannica; nearest stage."}
    - {value: "Collège royal (lycée), Besançon: bachelier ès lettres 1840; bachelier ès sciences 1842 (Besançon per Britannica, Dijon per ENS)", stage: "grammar or secondary school", years: "–1842", certainty: 0.7, cites: [{source: S1, locator: "'Early education'"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources, which differ on where the science degree was taken."}
    - {value: "École normale supérieure, Paris (entered 1843; licence 1845; doctorate 1847), assistant to Dumas", stage: university, years: "1843–1847", certainty: 1.0, cites: [{source: S1, locator: "'Research career', paragraph 1"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [French], certainty: 1.0, cites: [{source: S1, locator: "'Early education'"}], how_known: "Jura family."}
  notable_events:
    - {value: "Pastels and portraits of his parents and friends made at 15, later kept at the Pasteur Institute museum", year: "c. 1838", certainty: 0.7, cites: [{source: S1, locator: "'Early education'"}], how_known: "Britannica."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1847–1895", certainty: 1.0, cites: [{source: S1, locator: "'Research career'; 'Vaccine development'"}], how_known: "From his doctorate to his death."}
  nominal_affiliations: []
  self_described_science_religion_relation:
    value: "Two orders kept apart: experimental science 'jamais [...] ne fait intervenir la considération de l'essence des choses, de l'origine du monde et de ses destinées' and has nothing to learn from metaphysics; but the questions of God and the soul seem to him 'd'essence éternelle', and the notion of the infinite, which imposes itself and is incomprehensible, puts 'le surnaturel [...] au fond de tous les cœurs'."
    certainty: 1.0
    cites: [{source: S3, locator: "pp. 20, 23–24"}]
    how_known: "His own public speech, read in the 1882 printing (library scan) and matching the Académie française's online text."
  primary_system:
    value: BELOW_THRESHOLD
    cites: [{source: S3, locator: "pp. 3–4, 20, 23–26"}]
    how_known: "The speech defends 'la doctrine spiritualiste' and the reality of the infinite against positivism, treats the idea of God as 'une forme de l'idée de l'infini' whatever its name ('Brahma, Allah, Jéhova ou Jésus'), and counts the 'vertus de l'Évangile' as one ideal among four. It affirms the supernatural infinite but no particular doctrine of God, so no system file fits at 0.5."
    note: "Candidates: CHRIST (draft) and IDEAL (stub). Named candidate without a code: French spiritualism (spiritualisme, Victor Cousin's school: God, the soul, freedom), which the 1882 speech defends by name ('la doctrine spiritualiste', S3, pp. 3–4). It has no system file; under decision S4 it cannot be coded in v8, and decision P9 (2026-10-02) lists it in systems/README.md under 'Systems to consider'. Would need his letters or a scholarly study of his religion (e.g. Geison 1995) to reach 0.5."
  secondary_system: {value: UNKNOWN, how_known: "No second system in what was read."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Leading candidate, not coded (BELOW_THRESHOLD): 'idéal des vertus de l'Évangile' (p. 26) and his admiration for the 'fervente catholique' Mme Littré (p. 26), but the speech's God is any name for the infinite (p. 24). The Notre-Dame funeral (S1) is not his act, and Catholic upbringing is not in a source read. CHRIST is a draft system file.", cites: [{source: S3, locator: "pp. 24, 26"}]}
    - {code: IDEAL, reason: "Considered: the 'conception de l'idéal' as a 'reflet de l'infini' and the ideals as a 'dieu intérieur' (pp. 24, 26). Not coded: the speech is not a philosophical idealism about mind and world. IDEAL is a stub system file (flag).", cites: [{source: S3, locator: "pp. 24, 26"}]}
    - {code: DEISM, reason: "Rejected: no creator argued from design and no rejection of revelation; DEISM is a draft.", cites: [{source: S3, locator: "pp. 23–24"}]}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "The speech speaks of the notion and idea of the infinite and of God in the human mind ('le surnaturel est au fond de tous les cœurs', 'Un Dieu intérieur' as the meaning of enthousiasme, S3, pp. 24, 26), not of where God is or whether God is a person. A mixed reading (2) is possible but would be scored from implication.", note: "Gap: letters and the Œuvres (vol. 7, Mélanges) for direct statements on God."}
    B_cause:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S3, locator: "pp. 3–4, 20"}, {source: S1, locator: "'Spontaneous generation'"}]
      how_known: "His own public speech and Britannica's account of his working science (P6); a named alternative, so 0.7."
      rationale: "Scored on his account of nature (P6). His science ran on strict experimental control: the method 'qui a pour guide et pour contrôle incessant l'observation et l'expérience, dégagées [...] de tout préjugé métaphysique' (p. 4), with no spontaneous generation and a specific organism for each fermentation and disease (S1). No miracle, petition or exemption in his account of nature. Named alternative: 3, since he says that by showing that life 'ne s'est jamais montrée à l'homme comme un produit des forces qui régissent la matière' he served 'la doctrine spiritualiste' (pp. 3–4), which may hold life apart from the forces governing matter; the claim is hedged ('jusqu'à ce jour') and names no exception to law."
    C_ledger: {value: BELOW_THRESHOLD, how_known: "Nothing read on judgement, afterlife or reward and punishment; the soul's 'hautes préoccupations' (p. 20) are named but not described."}
    D_authority:
      value: 2
      basis: written_profession
      certainty: 0.7
      cites: [{source: S3, locator: "pp. 4, 20, 23–24"}]
      how_known: "His own public speech; a named alternative, so 0.7."
      rationale: "Two domains, each with its own authority, so D 2 (same-pattern rule). Experimental science 'n'aurait rien à apprendre d'aucune spéculation métaphysique' and never considers the essence of things or the origin and destiny of the world (p. 20); but no discovery 'philosophique ou scientifique' can remove the questions of God and the soul (p. 20), and before the infinite 'il faut demander grâce à sa raison' (p. 24). Named alternative: 3, because the second domain is reached by reason's own question ('Qu'y a-t-il au delà ?', p. 23), not by revelation, which the speech never invokes."
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Nothing read addresses favour for a group in events. That 'tous les hommes sont égaux' before the infinite (p. 25) concerns human dignity and the moral community, which belongs on C, not E."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied."}
  statements:
    - text: "En prouvant que, jusqu'à ce jour, la vie ne s'est jamais montrée à l'homme comme un produit des forces qui régissent la matière, j'ai pu servir la doctrine spiritualiste fort délaissée ailleurs, mais assurée du moins de trouver dans vos rangs un glorieux refuge."
      cites: [{source: S3, locator: "pp. 3–4"}]
      date: "1882-04-27"
      context: "Opening of his reception speech at the Académie française, on what his work on the origin of microscopic life had served."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "Admirable et souveraine méthode, qui a pour guide et pour contrôle incessant l'observation et l'expérience, dégagées, comme la raison qui les met en œuvre, de tout préjugé métaphysique; méthode si féconde que des intelligences supérieures, éblouies par les conquêtes que lui doit l'esprit humain, ont cru qu'elle pouvait résoudre tous les problèmes."
      cites: [{source: S3, locator: "p. 4"}]
      date: "1882-04-27"
      context: "On the experimental method of Galileo, Pascal and Newton; the next sentence says Littré shared 'cette illusion'."
      axes: [B_cause, D_authority]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "Quant à moi, qui juge que les mots progrès et invention sont synonymes, je me demande au nom de quelle découverte nouvelle, philosophique ou scientifique, on peut arracher de l'âme humaine ces hautes préoccupations. Elles me paraissent d'essence éternelle, parce que le mystère qui enveloppe l'univers et dont elles sont une émanation est lui-même éternel de sa nature."
      cites: [{source: S3, locator: "p. 20"}]
      date: "1882-04-27"
      context: "After describing Littré's positivist refusal to consider 'ni de Dieu, ni de l'âme'."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "La science expérimentale est essentiellement positiviste en ce sens que, dans ses conceptions, jamais elle ne fait intervenir la considération de l'essence des choses, de l'origine du monde et de ses destinées. Elle n'en a nul besoin. Elle sait qu'elle n'aurait rien à apprendre d'aucune spéculation métaphysique."
      cites: [{source: S3, locator: "p. 20"}]
      date: "1882-04-27"
      context: "Distinguishing the experimental method from Comte's system."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "Celui qui proclame l'existence de l'infini, et personne ne peut y échapper, accumule dans cette affirmation plus de surnaturel qu'il n'y en a dans tous les miracles de toutes les religions; car la notion de l'infini a ce double caractère de s'imposer et d'être incompréhensible."
      cites: [{source: S3, locator: "pp. 23–24"}]
      date: "1882-04-27"
      context: "On 'la grande et visible lacune' of positivism: it ignores the notion of the infinite."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "Par elle, le surnaturel est au fond de tous les cœurs. L'idée de Dieu est une forme de l'idée de l'infini. Tant que le mystère de l'infini pèsera sur la pensée humaine, des temples seront élevés au culte de l'infini, que le Dieu s'appelle Brahma, Allah, Jéhova ou Jésus."
      cites: [{source: S3, locator: "p. 24"}]
      date: "1882-04-27"
      context: "Continuing on the notion of the infinite. The 1882 printing has 'Jéhova'; the Académie française's online text has 'Jehova'."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
  changes_over_life: []
  coder_notes: "CHRIST and DEISM are drafts; IDEAL is a stub system file (flag). The Faraday anecdote in the speech (p. 20) reports Faraday's words and is not scored as Pasteur's view. Not used: 'Plus je sais, plus ma foi est celle du paysan breton' and similar sayings, which were not traced to a primary text; reports of his last sacraments (not in a source read). The speech is a public profession before the Académie, partly a eulogy of the positivist Littré; Renan's reply in the same printing is not Pasteur's view. changes_over_life is empty: no dated change in what was read."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "French (Jura artisan family)", certainty: 1.0, cites: [{source: S1, locator: "'Early education'; Top Questions"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: TODO, note: "Catholic by general report; not in a source read."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1848–1885", certainty: 1.0, cites: [{source: S1, locator: "'Research career' to 'Vaccine development'"}], how_known: "Molecular asymmetry to the rabies vaccine."}
  age_at_first_lasting_contribution: {value: 25, certainty: 0.5, cites: [{source: S1, locator: "'Research career'"}], how_known: "Computed from the coder's 1848."}
  first_evidence_of_lio_type_views: {value: "Académie française reception speech", year: 1882, certainty: 1.0, cites: [{source: S3, locator: "pp. 3–4, 20"}], how_known: "Earliest dated statement read."}
  lio_views_relative_to_major_work: {value: "unclear", rationale: "The speech (1882) comes late in the major work; nothing earlier was read.", certainty: 0.5, cites: [{source: S3, locator: "p. 3"}], how_known: "Dates of what was read."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "He describes his method as experiment and observation with hypotheses held 'sous la réserve d'un sévère contrôle' (S3, pp. 20–21), not deduction from definitions.", certainty: 0.5, cites: [{source: S3, locator: "pp. 20–21"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Early education'"}], how_known: "Nothing on method in childhood."}
  circle_present: {value: "no", rationale: "The infinite is 'surnaturel' and incomprehensible (S3, pp. 23–24), not identified with Nature.", certainty: 0.5, cites: [{source: S3, locator: "pp. 23–24"}], how_known: "Coder's reading of one speech."}
  reading: "As belief, not finding: form absent (experimental method), circle absent (a supernatural infinite). The record does not test H1."
  notes: ""

institutions:
  - {value: "University of Strasbourg", role: "professor of chemistry", years: "1849–1854", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Research career', paragraph 1"}], how_known: "Britannica; end year from the 1854 Lille appointment."}
  - {value: "University of Lille", role: "professor of chemistry and dean of the science faculty", years: "1854–1857", kind: university, certainty: 1.0, cites: [{source: S1, locator: "'Research career', paragraph 3"}, {source: S2, locator: "paragraph 2"}], how_known: "Two sources."}
  - {value: "École normale supérieure", role: "administrator and director of scientific studies; laboratory of physiological chemistry", years: "1857–1867", kind: university, certainty: 1.0, cites: [{source: S1, locator: "'Research career', paragraph 4"}, {source: S2, locator: "paragraphs 2–3"}], how_known: "Two sources."}
  - {value: "Sorbonne", role: "professor of chemistry", years: "1867–", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Spontaneous generation', paragraph 3"}], how_known: "Britannica."}
  - {value: "Académie des sciences", role: member, years: "1862–1895", kind: "academy or learned society", certainty: 1.0, cites: [{source: S1, locator: "'Spontaneous generation', paragraph 2"}], how_known: "Britannica."}
  - {value: "Académie française", role: member, years: "1881–1895", kind: "academy or learned society", certainty: 0.7, cites: [{source: S4, locator: "page heading"}, {source: S1, locator: "'Vaccine development'"}], how_known: "Received 1882; election year 1881 is general knowledge (flag)."}
  - {value: "Institut Pasteur, Paris", role: "founder and director", years: "1888–1895", kind: "academy or learned society", certainty: 0.7, cites: [{source: S1, locator: "'Vaccine development' (inaugurated 14 Nov 1888)"}], how_known: "Britannica gives the inauguration; his directorship is general knowledge (flag)."}
collaborators:
  - {value: "Jean-Baptiste Dumas", relation: teacher, note: "lecturer at the ENS; Pasteur was his assistant; later urged the silkworm work", certainty: 1.0, cites: [{source: S1, locator: "'Research career', paragraph 1; 'Spontaneous generation', paragraph 2"}], how_known: "Britannica (two passages)."}
  - {value: "Robert Koch", roster_id: koch-robert, relation: "rival or critic", note: "independent proof of the anthrax bacillus", certainty: 0.7, cites: [{source: S1, locator: "'Vaccine development', paragraph 3"}], how_known: "Britannica describes parallel work; the rivalry is general knowledge (flag)."}
  - {value: "Émile Littré", relation: other, note: "predecessor in his Académie française seat; the reception speech is his eulogy and a critique of his positivism", certainty: 1.0, cites: [{source: S3, locator: "pp. 4–26"}], how_known: "The speech."}
  - {value: "Ernest Renan", relation: other, note: "replied to his reception speech", certainty: 1.0, cites: [{source: S3, locator: "title page"}], how_known: "The 1882 printing includes Renan's reply."}

review:
  roster_status_reason: {value: "Core in v8 (F 4: Claude, DeepSeek, Gemini, Grok); field tie across models.", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 114"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Death place differs: Marnes-la-Coquette (ENS; EPHE: Villeneuve-l'Étang estate) vs Saint-Cloud (Britannica and most general sources). Value Marnes-la-Coquette at 0.5 with Saint-Cloud as the alternative (decision P9)."
    - "first_lasting_contribution_year 1848 is the coder's dating, on the era-bucket boundary (1849/1850); era applied literally from 1848 (decision P9)."
    - "The ENS page says pasteurization came from a request of 'Napoléon Bonaparte'; Britannica says Napoleon III. The ENS slip is not used."
    - "Small differences between the 1882 printing and the Académie française web text ('Jéhova'/'Jehova'; in the Faraday quotation 'joies'/'voies'); quotations follow the 1882 printing."
  open_questions:
    - "Read his letters (Correspondance, ed. Pasteur Vallery-Radot) and Geison, The Private Science of Louis Pasteur (1995), for private statements on religion."
    - "Check family religion and practice in Vallery-Radot's Vie de Pasteur (archive.org scans exist), keeping reported speech apart."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Agnes Ullmann"
    citation: "Ullmann, Agnes. \"Louis Pasteur.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Louis-Pasteur (with the section pages 'Research-career', 'Spontaneous-generation' and 'Vaccine-development')."
    url: "https://www.britannica.com/biography/Louis-Pasteur"
    accessed: 2026-10-02
    reliability_note: "Signed article by an Institut Pasteur scientist; all four section pages read. Cited by section heading."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators, review]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "École normale supérieure"
    citation: "École normale supérieure – PSL. \"Louis Pasteur (1822–1895).\" Portraits de normaliens. https://www.ens.psl.eu/portraits-de-normaliens/louis-pasteur-1822-1895."
    url: "https://www.ens.psl.eu/portraits-de-normaliens/louis-pasteur-1822-1895"
    accessed: 2026-10-02
    reliability_note: "Institutional portrait; paragraphs counted from 'Louis Pasteur est né'. Contains at least one slip (see flags)."
    used_for: [identity, basics, contribution, childhood, institutions]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Louis Pasteur"
    year: 1882
    citation: "Pasteur, Louis. Discours de réception de M. Louis Pasteur [...] Réponse de M. Ernest Renan. Séance de l'Académie française du 27 avril 1882. Paris: Calmann Lévy, 1882. Wellcome Collection scan on the Internet Archive: https://archive.org/details/b30478145."
    url: "https://archive.org/details/b30478145"
    accessed: 2026-10-02
    reliability_note: "Library scan of the 1882 printing. Pages 3–4, 20–21, 23–26 checked on the page images (leaf = page + 7)."
    used_for: [identity, contribution, worldview, timing, lane_b, collaborators]
  - id: S4
    type: primary
    kind: "institutional page"
    author: "Académie française"
    citation: "Académie française. \"Discours de réception de Louis Pasteur.\" https://www.academie-francaise.fr/discours-de-reception-de-louis-pasteur."
    url: "https://www.academie-francaise.fr/discours-de-reception-de-louis-pasteur"
    accessed: 2026-10-02
    reliability_note: "Official site of the institution; the text matches S3 except for small variants noted in the flags."
    used_for: [contribution, institutions]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
  - id: S6
    type: secondary
    kind: database
    author: "Thierry Dupressoir"
    citation: "Dupressoir, Thierry. \"Louis Pasteur.\" Dictionnaire prosopographique de l'EPHE, École pratique des hautes études (updated 16 February 2021). https://prosopo.ephe.psl.eu/louis-pasteur."
    url: "https://prosopo.ephe.psl.eu/louis-pasteur"
    accessed: 2026-10-02
    reliability_note: "Signed notice in an institutional prosopographical dictionary; used only for the place of death."
    used_for: [basics]
---

# Louis Pasteur

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Louis Pasteur (1822–1895), French chemist and microbiologist, discovered molecular asymmetry, founded the germ theory of fermentation, refuted spontaneous generation and developed the anthrax and rabies vaccines [S1]. In his 1882 Académie française speech he kept experimental science free of metaphysics yet held that the notion of the infinite puts "le surnaturel [...] au fond de tous les cœurs" and that "L'idée de Dieu est une forme de l'idée de l'infini" [S3, pp. 20, 24]. primary_system BELOW_THRESHOLD; B 4 (0.7), D 2 (0.7); A, C, E below threshold; mid_basin below threshold.

## Life and work

Born in Dole, he studied at Besançon and the École normale supérieure, taught at Strasbourg and Lille, directed scientific studies at the ENS from 1857 and founded the Institut Pasteur, inaugurated in 1888 [S1; S2].

## Contribution and impact

Molecular asymmetry, fermentation, the refutation of spontaneous generation, pasteurization and attenuated vaccines [S1, 'Research career' to 'Vaccine development'].

## Childhood and education

Son of a tanner who had been a decorated sergeant major; an average pupil gifted in drawing [S1, 'Early education'].

## Adult working worldview

By showing that life "ne s'est jamais montrée à l'homme comme un produit des forces qui régissent la matière" he served "la doctrine spiritualiste" [S3, pp. 3–4]. Experimental science "n'aurait rien à apprendre d'aucune spéculation métaphysique" [S3, p. 20], but the infinite carries "plus de surnaturel qu'il n'y en a dans tous les miracles de toutes les religions" [S3, p. 24]. Scores: B 4, D 2 (0.7); A, C, E below threshold.

## Heritage (context only)

French, from a Jura artisan family [S1]. Religious heritage not stated in the sources read. Context only.

## Timing

First lasting contribution about 1848 (coder's dating, 0.5) [S1]. The worldview evidence read is from 1882.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form absent; circle absent.

## Open questions

- His correspondence and Geison (1995); family religion.

## Research log

- 2026-10-02: Read Britannica (Ullmann, all four section pages), the ENS portrait, the 1882 printing of the reception speech (Wellcome scan; pp. 3–4, 20–21, 23–26 checked on the images) and the Académie française's online text. MacTutor has no Pasteur page (404); the Institut Pasteur history page did not return article text.
