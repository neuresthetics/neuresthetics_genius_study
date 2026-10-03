---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 4
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, third batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages and library scans"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (third batch, RUNBOOK §1 order). Basics from Britannica (Donovan, first page), the Science History Institute biography and Grimaux's 1888 biography (Internet Archive scan of the University of Toronto copy). Worldview from his Traité élémentaire de chimie (1789, vol. 1, pp. 140–141, checked on the scan), one letter to Edward King (1788, quoted by Grimaux, p. 53) and his 1791 manuscript on Talleyrand's education plan (printed by Guillaume, 1908, pp. 363–364). primary_system BELOW_THRESHOLD (CHRIST considered). B 4 (0.7); A, C, D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Schema 1.1 → 1.2 (decision P8 adds basis recorded_interview and statement kind 'recorded interview'); no content change."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 3 (two blind runs at d9903b7). #64 (both runs): the King letter's date is Grimaux p. 53 n. 1, not n. 2; n. 2 (lay patron of the chapel of his château of Fréchines, chaplain named by deed of 7 Aug 1781 and paid 290 livres a year) added as a nominal affiliation and in the CHRIST candidate, cited to p. 53 n. 2. #51: single-letter rule cited as CODING_GUIDE §3 (secondary quotation §7). #61: first_lasting_contribution_year 1774 → 1772 (0.5): 1774 is Priestley's visit; his own combustion experiments date from 1772 (sealed note of 1 Nov 1772, Grimaux p. 103 and n. 1), with the Easter 1775 memoir (p. 108) as the alternative; age 31 → 29; era bucket unchanged. #65: trailing cut of the 1791 quotation marked [...]. No worldview score changed. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02). Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs; quote kinds relabelled (P18/P28); first lasting year per P13/P23, no coder's-choice wording; Britannica Top Questions cites removed (P26). Full before → after list: reports/stage3_rulings_changes.csv. Not reviewed."}

identity:
  id: lavoisier-antoine
  display_name: "Antoine Lavoisier"
  roster:
    canonical_name: "Antoine Lavoisier"
    rank: 84
    F: 4
    models: [Claude, DeepSeek, Gemini, Grok]
    band: "core (3–4)"
    status: core
    field: chemistry
    field_bucket: chemistry
  full_name: {value: "Antoine-Laurent Lavoisier", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts ('In full')"}, {source: S3, locator: "pp. 1–2 (baptismal names)"}], how_known: "Two sources; Grimaux explains the names Antoine and Laurent."}
  native_name: {value: "Antoine-Laurent Lavoisier (French)", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Same spelling in French; 'de Lavoisier' also appears in letters of the period (S5, p. 362)."}
  aliases:
    - {name: "Lavoisier-Antoine", kind: "roster alias"}

basics:
  birth:
    date: {value: "1743-08-26", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S3, locator: "p. 2"}], how_known: "Two sources agree."}
    place: {value: "Paris", modern_name: "Paris, France", polity_then: "Kingdom of France", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S3, locator: "p. 2"}], how_known: "Two sources agree."}
  death:
    date: {value: "1794-05-08", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts; opening"}, {source: S2, locator: "'Chemical Revolution and Political Revolution' (spring 1794)"}], how_known: "Britannica gives the day; SHI agrees on spring 1794."}
    place: {value: "Paris (guillotined)", modern_name: "Paris, France", polity_then: "French First Republic", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1772, certainty: 0.5, cites: [{source: S3, locator: "p. 103 and n. 1"}, {source: S2, locator: "'The Oxygen Revolution'; bibliography (Guerlac 1961)"}], how_known: "Year of his first combustion experiments, the start of the oxygen theory (the earliest item in lasting_original_contributions): in 1772 he found that phosphorus and sulphur gain weight on burning, and deposited a sealed note with the Académie on 1 November 1772 (Grimaux, p. 103 and n. 1, which prints the note); SHI's bibliography lists Guerlac's book on 'His First Experiments on Combustion in 1772'. 1774 (the earlier value) is the year of Priestley's Paris visit (SHI), not of Lavoisier's own work. The listed item's year is a range (1770s–1780s); the sources read do not settle whether it starts with the 1772 note or with the Easter 1775 memoir on the new air (Grimaux, p. 108), so 0.5 with 1775 named (P23, P25).", alternatives: [{value: 1775, cites: [{source: S3, locator: "p. 108 ('la séance publique de Pâques 1775')"}], note: "Memoir to the Académie distinguishing the new air from common and fixed air and attributing to it the weight gain of calcined metals."}]}
  era_bucket: {value: "1750 to 1849", certainty: 1.0, cites: [{source: S3, locator: "pp. 103, 108"}], how_known: "Any candidate first-contribution year (1772–1789) falls in this bucket (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}], how_known: "France is Western Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S2, locator: "'Early Career'"}], how_known: "Paris throughout."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "As the sources record it."}
  languages_of_work: {value: [French], certainty: 1.0, cites: [{source: S4, locator: "title page"}], how_known: "His own Traité is in French (primary). That he did not read English was only in the Top Questions box and is not used (P26)."}
  occupations: {value: [chemist, "tax farmer (Ferme générale)", "public administrator", "gunpowder administrator"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "'Early Career'"}], how_known: "Two sources."}

contribution:
  fields: {value: [chemistry, "physiology of respiration"], certainty: 1.0, cites: [{source: S1, locator: "opening; Quick Facts"}, {source: S2, locator: "opening"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Oxygen theory of combustion and respiration, overturning phlogiston", year: "1770s–1780s", kind: theory, lasting: "foundation of modern chemistry", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "'The Oxygen Revolution'"}], how_known: "Two sources."}
    - {value: "Conservation of mass made a working law of chemistry", year: "1789", kind: "law or principle", lasting: "taught in France as 'Lavoisier's law'", certainty: 1.0, cites: [{source: S1, locator: "'Conservation of mass'"}, {source: S4, locator: "pp. 140–141"}], how_known: "Britannica and his own statement of the principle."}
    - {value: "Composition of water from hydrogen and oxygen (with Laplace)", year: "1780s", kind: discovery, lasting: "standard chemistry", certainty: 0.7, cites: [{source: S2, locator: "'The New Chemistry'"}], how_known: "SHI."}
    - {value: "Modern chemical nomenclature (co-author) and the operational definition of an element", year: "1787–1789", kind: method, lasting: "names still in use", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "'The New Chemistry'"}], how_known: "Two sources."}
  evidence_of_impact:
    - {value: "Called the 'father of modern chemistry'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "SHI."}
  major_works:
    - {value: "Traité élémentaire de chimie", year: 1789, kind: book, certainty: 1.0, cites: [{source: S4, locator: "title page"}, {source: S2, locator: "opening"}], how_known: "Read in the 1789 first edition scan."}
    - {value: "Méthode de nomenclature chimique (with Guyton de Morveau, Berthollet and Fourcroy)", year: 1787, kind: book, certainty: 0.7, cites: [{source: S3, locator: "p. 52 ('la rédaction de la Nomenclature chimique', 1787)"}], how_known: "Grimaux dates his work on it to 1787; co-authors from general knowledge, not checked in a source read (flag)."}
  honours:
    - {value: "Elected to the Académie royale des sciences", year: 1768, certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "'Early Career'"}], how_known: "Two sources."}
  definition_fit: {value: "clearly meets", rationale: "Led the chemical revolution.", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Sources agree."}

childhood:
  family_religion: {value: "Catholic; Grimaux calls the family pious, with several priests among its members", certainty: 0.7, cites: [{source: S3, locator: "pp. 2, 53"}], how_known: "Grimaux, who wrote with the family's papers and the family's goodwill (see data_quality_flags). Baptism at Saint-Merry and a priest godfather (p. 2) are documented facts."}
  family_religious_practice: {value: TODO, note: "Grimaux's 'famille pieuse' (p. 53) is a characterisation, not a description of practice."}
  parents_and_household:
    - {value: "Father, Jean-Antoine Lavoisier, procureur at the Parlement of Paris", name: "Jean-Antoine Lavoisier", role: father, certainty: 1.0, cites: [{source: S3, locator: "pp. 1–2"}, {source: S1, locator: "'Early life and education'"}], how_known: "Grimaux; Britannica agrees the father was in the law."}
    - {value: "Mother, Émilie Punctis, daughter of a barrister; died 1748", name: "Émilie Lavoisier (née Punctis)", role: mother, certainty: 1.0, cites: [{source: S3, locator: "p. 2"}, {source: S2, locator: "'Early Career' (mother died when he was five)"}], how_known: "Two sources."}
    - {value: "Aunt, Constance Punctis, who raised the children after the mother's death", name: "Constance Punctis", role: "other relative", certainty: 0.7, cites: [{source: S3, locator: "pp. 2–3"}], how_known: "Grimaux."}
  household_circumstances: {value: "Wealthy bourgeois legal family; after 1748 the widowed father moved the two children into the household of their grandmother Mme Punctis and aunt Constance; his only sister died about 1760, aged 15", certainty: 0.7, cites: [{source: S3, locator: "pp. 2–3"}, {source: S1, locator: "'Early life and education'"}], how_known: "Grimaux, with Britannica on the family's wealth."}
  schooling:
    - {value: "Collège Mazarin (Collège des Quatre-Nations), Paris, as a day pupil; second prize for French discourse in the concours général, 1760", stage: "grammar or secondary school", years: "c. 1754–1761", certainty: 0.7, cites: [{source: S3, locator: "pp. 3–4"}, {source: S1, locator: "'Early life and education'"}], how_known: "Two sources on the college; years are the coder's estimate from Grimaux (the family fortune of 1754 and the 1760 prize)."}
    - {value: "Faculty of Law, Paris (bachelor 1763, licentiate 1764), while attending science lectures (La Caille, Bernard de Jussieu, Guettard, Rouelle)", stage: university, years: "1761–1764", certainty: 1.0, cites: [{source: S3, locator: "p. 4 and n. 1"}, {source: S1, locator: "'Early life and education'"}], how_known: "Two sources; dates from Grimaux's note on the faculty registers."}
  early_mathematics: {value: "advanced mathematics", note: "Studied mathematics and astronomy with La Caille as a law student, not in childhood; level not stated, so the stage is the coder's reading.", certainty: 0.5, cites: [{source: S3, locator: "p. 4"}], how_known: "Grimaux."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Took up the sciences in his philosophy year at the Collège Mazarin; then lectures in astronomy, botany, mineralogy and chemistry", certainty: 0.7, cites: [{source: S3, locator: "p. 4"}], how_known: "Grimaux."}
  key_early_reading: []
  childhood_mentors:
    - {value: "Jean-Étienne Guettard (mineralogy and geology)", certainty: 1.0, cites: [{source: S2, locator: "'Early Career'"}, {source: S3, locator: "p. 4"}], how_known: "Two sources."}
  languages_in_childhood: {value: [French], certainty: 0.7, cites: [{source: S3, locator: "pp. 1–4"}], how_known: "Parisian family."}
  notable_events:
    - {value: "Mother's death when he was about five", year: "1748", certainty: 1.0, cites: [{source: S3, locator: "p. 2"}, {source: S2, locator: "'Early Career'"}], how_known: "Two sources."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1764–1794", certainty: 0.7, cites: [{source: S3, locator: "p. 4"}, {source: S1, locator: "opening"}], how_known: "From the end of his law studies to his death."}
  nominal_affiliations:
    - {value: "Catholic by baptism (Saint-Merry, Paris, 1743)", years: "1743–", role: "member by baptism", certainty: 1.0, cites: [{source: S3, locator: "p. 2"}], how_known: "Primary document printed in S3: the birth and baptism record in Grimaux's appendix."}
    - {value: "Lay patron (patron laïc) of the chapel of his château of Fréchines; as such he named a chaplain, the abbé Bellavoine, by deed of 7 August 1781 and paid him 290 livres a year", years: "1781–", role: "other", certainty: 0.7, cites: [{source: S3, locator: "p. 53 n. 2"}], how_known: "Grimaux's note, citing the deed; one source. Patronage of a chapel that came with the estate is a practice and an office, not a statement of belief, so it does not lift primary_system (CODING_GUIDE §1, church membership)."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No statement by Lavoisier on how science and religion relate was found in the sources read."}
  primary_system:
    value: BELOW_THRESHOLD
    cites: [{source: S3, locator: "p. 53"}, {source: S5, locator: "pp. 363–364"}]
    how_known: "The only direct evidence is one private letter (to Edward King, 20 Aug 1788) praising King's defence of revelation, known only as quoted by Grimaux, against which stands his 1791 manuscript treating sixteen centuries of clerical education as lost to reason. One letter in a secondary quotation cannot carry a system (single-letter rule, CODING_GUIDE §3; secondary quotation, §7), and the two items pull in different directions. His lay patronage of the Fréchines chapel from 1781 (S3, p. 53 n. 2) is practice, not belief."
    note: "Candidate: CHRIST (draft system file). Would need the King letter in the Correspondance (Fric/Beretta edition) plus independent evidence of belief."
  secondary_system: {value: UNKNOWN, how_known: "No system evidence beyond the two items above."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Leading candidate, not coded (BELOW_THRESHOLD): Catholic baptism and upbringing and his lay patronage of the Fréchines chapel, with a chaplain he named and paid from 1781 (p. 53 n. 2) (never a code by themselves), and one polite letter calling the defence of revelation 'une belle cause'. Grimaux's 'il en avait gardé les croyances' is the biographer's claim, and the 1795 Almanach story of a prison reconciliation is hearsay about him, not his statement. CHRIST is a draft system file.", cites: [{source: S3, locator: "pp. 2, 53"}]}
    - {code: DEISM, reason: "Considered: an Enlightenment reformer hostile to clerical control of learning (S5). Not coded: nothing read states a creator who does not intervene or rejects revelation; anticlericalism is not deism.", cites: [{source: S5, locator: "pp. 363–364"}]}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Nothing read places or denies God; the King letter praises a defence of revelation but says nothing about where or what God is."}
    B_cause:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "pp. 140–141"}, {source: S1, locator: "'Conservation of mass'"}]
      how_known: "His own published account of nature (P6), checked on the 1789 first-edition scan. Below 1.0 because the passage states a law of nature and does not speak to miracle or providence directly."
      rationale: "Scored on his account of nature (P6). In the Traité he lays down that 'rien ne se crée, ni dans les opérations de l'art, ni dans celles de la nature', that matter is equal before and after every operation, and that chemical experiment rests on this 'véritable égalité ou équation' (pp. 140–141): one law for the laboratory and for nature, with no exceptions allowed. Britannica describes his programme of raising chemistry to the 'causal explanation found in contemporary experimental physics'. No miracle, providence or exemption appears in anything read."
    C_ledger: {value: BELOW_THRESHOLD, how_known: "Nothing read on judgement or reward and punishment. His prison letter to his wife, 'nous ne sommes pas sans espérance de nous rejoindre' (S3, p. 275), most plainly refers to hoped-for release (he goes on to her visits in the meantime), not to an afterlife, so it is not used."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "Two items, in tension: the King letter (single letter, secondary quotation) calls the defence of revelation and the authenticity of Scripture 'une belle cause' (S3, p. 53); the 1791 manuscript says clerical education put 'tout ce qui pouvait tendre à détruire les erreurs et les préjugés' in the hands of those with an interest in propagating them (S5, p. 364). The second is about who controls instruction, not about revelation as an authority, so neither settles D.", note: "Gap: the Correspondance de Lavoisier (ed. Fric and Beretta) for the full King letter and any other religious statements."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Nothing read addresses favour for a group in events; not scored from working science alone (same treatment as Fermi and Curie)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied."}
  statements:
    - text: "car rien ne se crée, ni dans les opérations de l'art, ni dans celles de la nature, & l'on peut poser en principes que dans toute opération, il y a une égale quantité de matière avant & après l'opération; que la qualité & la quantité des principes est la même, & qu'il n'y a que des changemens, des modifications."
      cites: [{source: S4, locator: "pp. 140–141 (ch. XIII, 'De la décomposition des oxides végétaux par la fermentation vineuse')"}]
      date: "1789"
      context: "On the analysis of wine fermentation. Long s is printed as 's'; spelling and punctuation otherwise as printed (checked on the page images)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "C'est une belle cause que vous entreprenés de deffendre que celle de la révélation et de l'authenticité des Saintes Écritures, et ce qui est remarquable, c'est que vous employés dans ce moment pour les deffendre précisément les mêmes armes qu'on a employées bien des fois pour les attaquer."
      cites: [{source: S3, locator: "p. 53 and n. 1 ('Lettre du 20 août 1788')"}]
      date: "1788-08-20"
      context: "Acknowledging a book of controversy sent by Edward King, an English writer and Fellow of the Royal Society. Known only as quoted by Grimaux (checked on the page image). Grimaux's note 1 gives the date; his note 2, called at the end of the quotation, is about the Fréchines chapel patronage (see nominal_affiliations)."
      axes: [D_authority]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
    - text: "C'est ainsi que, d'abord par un effet du hasard, et depuis par une marche très habilement combinée, tout ce qui pouvait tendre à détruire les erreurs et les préjugés s'est trouvé réuni dans les mains de ceux qui avaient intérêt de les propager. Cette époque, composée de seize siècles presque entièrement perdus pour la raison et la philosophie, [...] sera à jamais remarquable dans l'histoire de l'humanité [...]"
      cites: [{source: S5, locator: "p. 364"}]
      date: "1791"
      context: "Opening of his unpublished 'Réflexions sur le plan d'instruction publique' for Talleyrand (autumn 1791), as printed by Guillaume from the manuscript (checked on the page image). Guillaume's note reads 'remarquable' as a slip for 'mémorable'."
      axes: [D_authority]
      kind: "unpublished manuscript"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
  changes_over_life: []
  coder_notes: "CHRIST is a draft system file. Three often-repeated items are not used as his views: Grimaux's claim that he kept his family's beliefs (biographer's claim); the anonymous Almanach des gens de bien (1795) story that he was reconciled to the Church in prison (hearsay at two removes, via a letter of Delahante; see Scheler and Smeaton, Annals of Science 14, 1958, not read); and the prison letter's 'espérance de nous rejoindre' (most naturally hope of release). changes_over_life is empty: the possible prison reconciliation is unverified. The 1791 manuscript is a private draft, kind 'other'; Guillaume printed it in full in 1907 and part of it in 1894."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "French (Parisian legal bourgeoisie, family from Villers-Cotterêts)", certainty: 1.0, cites: [{source: S3, locator: "p. 1"}, {source: S1, locator: "'Early life and education'"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: "Catholic", certainty: 1.0, cites: [{source: S3, locator: "p. 2"}], how_known: "Primary document printed in S3: the baptism record in Grimaux's appendix."}
  baptism_or_initiation: {value: "Baptised the day of his birth at Saint-Merry, Paris; godfather his great-uncle Laurent Waroquier, a priest", certainty: 1.0, cites: [{source: S3, locator: "p. 2"}], how_known: "Primary document printed in S3: the parish record in Grimaux's appendix."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not described in the sources read."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1772–1789", certainty: 0.7, cites: [{source: S2, locator: "'The Oxygen Revolution'; 'The New Chemistry'"}, {source: S4, locator: "title page"}], how_known: "From the combustion work to the Traité; start year is the coder's estimate."}
  age_at_first_lasting_contribution: {value: 29, certainty: 0.5, cites: [{source: S3, locator: "pp. 2, 103 n. 1"}], how_known: "Born 26 August 1743; the sealed note is dated 1 November 1772. Computed from the coder's 1772 choice (31 for the 1775 alternative)."}
  first_evidence_of_lio_type_views: {value: "Traité élémentaire de chimie (conservation of matter in art and nature)", year: 1789, certainty: 1.0, cites: [{source: S4, locator: "pp. 140–141"}], how_known: "Earliest dated statement read bearing on an axis."}
  lio_views_relative_to_major_work: {value: "unclear", rationale: "The only scored axis (B) comes from the culmination of the major work itself.", certainty: 0.5, cites: [{source: S4, locator: "pp. 140–141"}], how_known: "Dates."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "The Traité poses conservation 'en principe' and builds chemical analysis on an 'équation' between reactants and products (pp. 140–141): a stated principle with consequences, but experimental, not definitional.", certainty: 0.5, cites: [{source: S4, locator: "pp. 140–141"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S3, locator: "p. 4"}], how_known: "Collège Mazarin and La Caille's mathematics; nothing on method."}
  circle_present: {value: "unclear", rationale: "Nothing read identifies or separates God and Nature.", certainty: 0.5, cites: [{source: S3, locator: "p. 53"}], how_known: "No evidence either way."}
  reading: "As belief, not finding: form partly present (principle-based analysis), circle unclear. The record does not test H1."
  notes: ""

institutions:
  - {value: "Académie royale des sciences, Paris", role: "member (from 1768)", years: "1768–1793", kind: "academy or learned society", certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "'Early Career'"}], how_known: "Two sources; end year is the Academy's suppression (general knowledge, flag)."}
  - {value: "Ferme générale", role: "tax farmer", years: "1768–1793", kind: employer, certainty: 0.7, cites: [{source: S2, locator: "'Early Career'"}], how_known: "SHI."}
  - {value: "Régie des poudres (royal gunpowder administration), Paris Arsenal", role: "inspector / commissioner; laboratory at the Arsenal", years: "1775–", kind: "government or state body", certainty: 1.0, cites: [{source: S2, locator: "'Early Career'"}, {source: S3, locator: "p. 52"}], how_known: "Two sources."}
  - {value: "Commission of Weights and Measures", role: member, years: "1790s", kind: "government or state body", certainty: 1.0, cites: [{source: S2, locator: "'Chemical Revolution and Political Revolution'"}, {source: S5, locator: "pp. 361–362, notes"}], how_known: "Two sources."}
collaborators:
  - {value: "Marie-Anne Paulze Lavoisier", relation: family, note: "wife (married 1771); collaborator, illustrator and translator", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "SHI."}
  - {value: "Pierre-Simon Laplace", roster_id: laplace-pierre-simon, relation: collaborator, note: "composition of water", certainty: 0.7, cites: [{source: S2, locator: "'The New Chemistry'"}], how_known: "SHI."}
  - {value: "Joseph Priestley", roster_id: priestley-joseph, relation: "rival or critic", note: "1774 Paris visit; Lavoisier reinterpreted his 'dephlogisticated air'", certainty: 0.7, cites: [{source: S2, locator: "'The Oxygen Revolution'"}], how_known: "SHI."}
  - {value: "Jean-Étienne Guettard", relation: teacher, note: "geology and mineralogy; field travels", certainty: 1.0, cites: [{source: S2, locator: "'Early Career'"}, {source: S3, locator: "p. 4"}], how_known: "Two sources."}
  - {value: "Guillaume-François Rouelle", relation: teacher, note: "chemistry lectures at the Jardin du Roi", certainty: 1.0, cites: [{source: S2, locator: "'Early Career'"}, {source: S3, locator: "pp. 4–5"}], how_known: "Two sources."}
  - {value: "Claude-Louis Berthollet", relation: collaborator, note: "potassium chlorate powder (1788)", certainty: 0.7, cites: [{source: S3, locator: "p. 53"}], how_known: "Grimaux."}
  - {value: "Edward King", relation: correspondent, note: "sent him a work of religious controversy (1788)", certainty: 0.7, cites: [{source: S3, locator: "p. 53"}], how_known: "Grimaux."}

review:
  roster_status_reason: {value: "Core in v8 (F 4: Claude, DeepSeek, Gemini, Grok).", certainty: 0.7, cites: [{source: S6, locator: "roster.csv, rank 84"}], how_known: "Study roster."}
  controversies:
    - {value: "Execution in the Terror with other financiers; the 'La République n'a pas besoin de savants' remark is legendary", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "p. 360"}], how_known: "Britannica on the execution; Guillaume on the legend."}
    - {value: "Whether he remained a believing Catholic: Grimaux (writing with the pious Chazelles family's papers) says yes; Guillaume (1907) published the anticlerical manuscript Grimaux had not printed in full", certainty: 0.7, cites: [{source: S3, locator: "p. 53"}, {source: S5, locator: "pp. 358–359, 363–364"}], how_known: "The two printed sources."}
  data_quality_flags:
    - "The King letter is known here only through Grimaux's quotation (S3), a biographer dependent on the descendants' goodwill; it is a single private letter (single-letter rule) and a secondary quotation (§7)."
    - "first_lasting_contribution_year 1772 is the source-dated start of the earliest listed lasting item, the oxygen theory (combustion experiments, sealed note of 1 Nov 1772; Grimaux p. 103). 0.5 because the sources read do not settle whether the item starts in 1772 or with the Easter 1775 memoir (named alternative); was 1774, Priestley's visit, until the lens audit batch 3 (#61). Britannica's later sections were not read."
    - "Co-authors of the 1787 Nomenclature and the 1793 end of the Académie are from general knowledge, flagged."
    - "Britannica read as its first page only."
  open_questions:
    - "Read the King letter and any religious remarks in the Correspondance de Lavoisier (Fric; Beretta), and Scheler and Smeaton (1958) on the prison reconciliation story."
    - "Read Britannica's later sections and a modern biography (Poirier 1993; Donovan 1993) for dates of the first combustion work."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Arthur L. Donovan"
    citation: "Donovan, Arthur L. \"Antoine Lavoisier.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Antoine-Lavoisier."
    url: "https://www.britannica.com/biography/Antoine-Lavoisier"
    accessed: 2026-10-02
    reliability_note: "Signed article; first page only (to 'Conservation of mass'). Sections cited by heading."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, institutions, collaborators, review]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "Science History Institute (updated by Samantha Wesner)"
    citation: "Science History Institute. \"Antoine-Laurent Lavoisier.\" Scientific Biographies, updated 6 July 2026. https://www.sciencehistory.org/education/scientific-biographies/antoine-laurent-lavoisier/."
    url: "https://www.sciencehistory.org/education/scientific-biographies/antoine-laurent-lavoisier/"
    accessed: 2026-10-02
    reliability_note: "Museum and library biography; cited by section heading."
    used_for: [basics, contribution, childhood, timing, institutions, collaborators]
  - id: S3
    type: secondary
    kind: "scholarly book"
    author: "Édouard Grimaux"
    year: 1888
    citation: "Grimaux, Édouard. Lavoisier, 1743–1794, d'après sa correspondance, ses manuscrits, ses papiers de famille et d'autres documents inédits. Paris: Félix Alcan, 1888. Internet Archive scan (University of Toronto copy): https://archive.org/details/lavoisier174317900grimuoft."
    url: "https://archive.org/details/lavoisier174317900grimuoft"
    accessed: 2026-10-02
    reliability_note: "Library scan. Biography built on the family archive, which prints letters; quotations from letters are secondary quotations. Written with the cooperation of Lavoisier's pious descendants (see Guillaume, S5, pp. 357–359). Page 53 checked on the image."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators, review]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Antoine-Laurent Lavoisier"
    year: 1789
    citation: "Lavoisier, Antoine-Laurent. Traité élémentaire de chimie, présenté dans un ordre nouveau et d'après les découvertes modernes. Vol. 1. Paris: Cuchet, 1789. Internet Archive scan (Countway Library of Medicine copy): https://archive.org/details/traitlmentairede01lavo."
    url: "https://archive.org/details/traitlmentairede01lavo"
    accessed: 2026-10-02
    reliability_note: "Library scan of the first edition. Pages 140–141 checked on the page images."
    used_for: [basics, contribution, worldview, timing, lane_b]
  - id: S5
    type: secondary
    kind: "book chapter"
    author: "James Guillaume"
    year: 1908
    citation: "Guillaume, James. \"Lavoisier anti-clérical et révolutionnaire\" (1907). In Études révolutionnaires, première série, 354–379. Paris: Stock, 1908. Internet Archive scan: https://archive.org/details/etudesrvolutio01guil."
    url: "https://archive.org/details/etudesrvolutio01guil"
    accessed: 2026-10-02
    reliability_note: "Library scan. Prints the surviving text of Lavoisier's 1791 manuscript from the original, which Guillaume had photographed (facsimile of the key paragraph facing pp. 372–373, not examined). Page 364 checked on the image."
    used_for: [identity, worldview, institutions, review]
  - id: S6
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# Antoine Lavoisier

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Antoine-Laurent Lavoisier (1743–1794), French chemist and tax farmer, led the chemical revolution with the oxygen theory, the new nomenclature and the Traité élémentaire de chimie (1789), and was guillotined in the Terror [S1, opening; S2]. In the Traité he lays down that "rien ne se crée, ni dans les opérations de l'art, ni dans celles de la nature" [S4, pp. 140–141]. His religious position is unclear: one letter praises a defence of revelation [S3, p. 53], and a 1791 manuscript is sharply anticlerical [S5, p. 364]. primary_system BELOW_THRESHOLD; B 4 (0.7); A, C, D, E below threshold; mid_basin below threshold.

## Life and work

Born in Paris to a family of lawyers, he studied at the Collège Mazarin and the Paris law faculty while attending science lectures, entered the Académie des sciences and the Ferme générale in 1768, and ran the gunpowder administration from 1775 [S1; S2, 'Early Career'; S3, pp. 2–4]. Arrested in 1793 with the other tax farmers, he was executed on 8 May 1794 [S1; S2].

## Contribution and impact

The oxygen theory of combustion and respiration, the composition of water (with Laplace), the new nomenclature and the conservation of mass as a working law [S1; S2].

## Childhood and education

Baptised Catholic at Saint-Merry, with a priest as godfather; his mother died in 1748 and an aunt raised him [S3, pp. 2–3].

## Adult working worldview

B is scored on the Traité's law of conservation "dans les opérations de l'art" and "dans celles de la nature" [S4, pp. 140–141]. To Edward King he wrote "C'est une belle cause que vous entreprenés de deffendre que celle de la révélation" [S3, p. 53], but this single letter, known only through Grimaux, cannot carry a system. In 1791 he wrote of "seize siècles presque entièrement perdus pour la raison et la philosophie" under clerical education [S5, p. 364]. Scores: B 4 (0.7); A, C, D, E below threshold.

## Heritage (context only)

French Catholic legal bourgeoisie [S3, pp. 1–2]. Context only.

## Timing

First lasting contribution 1772, his first combustion experiments and the sealed note of 1 November 1772 (the source-dated start of the earliest listed lasting item; 0.5, since the sources read leave open whether it starts here or with the Easter 1775 memoir) [S3, pp. 103, 108]. The worldview evidence read dates from 1788–1791.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form partly present (principle-based analysis); circle unclear.

## Open questions

- The Correspondance de Lavoisier for the King letter; Scheler and Smeaton (1958) on the prison story.

## Research log

- 2026-10-02: Read Britannica (Donovan, first page), the Science History Institute biography, Grimaux (1888; p. 53 checked on the image), the Traité (1789, vol. 1, pp. 140–141 checked on the images) and Guillaume (1908, p. 364 checked on the image). MacTutor has no Lavoisier page (404). Gallica blocked the fetch with a security check, so the Guillaume 1894 Procès-verbaux printing was not read.
