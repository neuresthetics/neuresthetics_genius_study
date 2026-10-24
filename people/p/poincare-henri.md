---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch F)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch F, order P32: F 5, rank 35). Basics from SEP (Heinzmann and Stump) and MacTutor (O'Connor and Robertson). A scientist under P30 (three-body problem, celestial mechanics). No statement of his own on God or on exceptions in nature was read; the 'free thinker at 18' claim is from an unsigned popular site and is not cited. primary_system and A UNKNOWN; B 3 at 0.5 from working science (P24, P35; alternative 4); C, D UNKNOWN; E BELOW_THRESHOLD (P19); mid_basin UNKNOWN. Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #35, F5 rank 35). Needs: A UNKNOWN; B 3 @0.5 faded. Read Chance / Le hasard (S4, FR Wikisource Science et méthode Livre I §IV; primary); Libre examen 1909 (S5, Wayback of henripoincarepapers HTML); Morale et science (S6, UQAC PDF of Dernières pensées ch.VIII). P47 source_quality on every source. Childhood filled from MacTutor (diphtheria; mother teaching; Lycée). A stays UNKNOWN (P19 researched silent on locus): Libre examen 'sans adhérer à aucune église' is first-person plural about freethinkers' impartiality, not a personal locus; Morale's 'si nous aimons ce Dieu' is hypothetical for religious morale; popular free-thinker@18 and fr.wiki 'cessé d'être croyant à 18' are unsigned / need_ref (RUNBOOK §3.1) — unused for A. B stays 3 @0.5 written_profession (Chance: absolute determinists; every phenomenon has a cause; for an infinitely informed mind 'il n'y aurait pas de hasard'), alt 4 (P16/P35/P40: he rehabilitates chance as sensitive dependence under laws; prayer-for-rain vs eclipse is epistemic; no no-exception / no-miracle claim). support corroborated (S4 + S1 working science). Chart: still unplotted. No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: poincare-henri
  display_name: "Henri Poincaré"
  roster:
    canonical_name: "Henri Poincaré"
    rank: 35
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Jules Henri Poincaré", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP alone."}
  native_name: {value: "Jules Henri Poincaré", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "French in Latin script; same form."}
  aliases:
    - {name: "Henri-Poincare", kind: "roster alias"}
    - {name: "Poincaré-Henri", kind: "roster alias"}

basics:
  birth:
    date: {value: "1854-04-29", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "Quick Info"}], how_known: "SEP and MacTutor agree (P15)."}
    place: {value: "Nancy, Lorraine, France", modern_name: "Nancy, France", polity_then: "France (Second Empire)", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "Quick Info"}], how_known: "SEP and MacTutor agree (P15)."}
  death:
    date: {value: "1912-07-17", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "Quick Info"}], how_known: "SEP and MacTutor agree (P15)."}
    place: {value: "Paris, France", modern_name: "Paris, France", polity_then: "France (Third Republic)", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "Quick Info"}], how_known: "SEP and MacTutor agree (P15)."}
  first_lasting_contribution_year: {value: 1882, certainty: 0.7, cites: [{source: S1, locator: "§5 ('theory of Fuchsian functions in 1882 (Poincaré 1882: 1167)')"}], how_known: "Earliest listed lasting contribution (P13). SEP cites a 1882 publication; his first Comptes rendus notes may be earlier (not read), so the year might be earlier."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "§5"}], how_known: "From 1882 (P2); any earlier note would also fall after 1850."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "France (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "Caen, then Paris."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [French], certainty: 0.7, cites: [{source: S1, locator: "§2 (La Science et l'hypothèse)"}], how_known: "SEP."}
  occupations: {value: ["mathematician", "mathematical physicist", "philosopher of science", "mine engineer"], certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}

contribution:
  fields: {value: ["mathematics", "celestial mechanics", "mathematical physics", "philosophy of science"], certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "Biography"}], how_known: "SEP and MacTutor."}
  lasting_original_contributions:
    - {value: "Theory of Fuchsian (automorphic) functions", year: 1882, kind: theory, lasting: "later called automorphic functions (S2)", certainty: 0.7, cites: [{source: S1, locator: "§5"}, {source: S2, locator: "Biography (Fuchsian functions)"}], how_known: "SEP dates it 1882; MacTutor describes it."}
    - {value: "Prize memoir on the three-body problem: stability of such systems cannot in general be demonstrated; recurrence theorem", year: 1889, kind: theory, lasting: "'a founding document in chaos theory' (S1)", certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "Biography (Birthday Competition)"}], how_known: "SEP gives the 1889 prize; the submission was earlier but its date was not read, so the year might be earlier (§8)."}
    - {value: "La Science et l'hypothèse (Science and Hypothesis), conventionalism", year: 1902, kind: work, lasting: "his geometric conventionalism is still debated (S1)", certainty: 0.7, cites: [{source: S1, locator: "§2, §4"}], how_known: "SEP."}
    - {value: "Poincaré conjecture", year: 1904, kind: other, lasting: "a major unsolved problem until Perelman (S1)", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
    - {value: "The three philosophical books (Science and Hypothesis, The Value of Science, Science and Method) completed", year: 1908, kind: work, lasting: "basis of his election to the Académie française in 1908 (S1)", certainty: 0.5, cites: [{source: S1, locator: "§1 ('elected to the Académie Française in 1908 on the basis of his three books')"}], how_known: "Listed so the span does not leave out his last major public work (P30 addendum). SEP gives 1908 for the election; the third book's year is inferred to be no later than 1908 (0.5)."}
  evidence_of_impact:
    - {value: "Prize of the King of Sweden (1889); President of the Academy of Sciences (1906); Académie française (1908)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founding work in topology and chaos theory (S1, S2).", certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "Summary"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "SEP and MacTutor say nothing on family religion. Unsigned popular sites and a fr.wikipedia sentence tagged need_ref ('pieux… cessé d'être croyant à dix-huit ans') are not citable (RUNBOOK §3.1); left for Aline Boutroux / Bellivier / Rollet."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated in S1–S6."}
  parents_and_household:
    - {value: "Father, Léon Poincaré, professor of medicine at the University of Nancy", name: "Léon Poincaré", role: father, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "Biography"}], how_known: "SEP and MacTutor agree."}
    - {value: "Mother, Eugénie Launois; gave him special instruction during childhood illness", name: "Eugénie Launois", role: mother, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "Biography"}], how_known: "SEP and MacTutor agree."}
  household_circumstances: {value: "University medical family in Nancy; childhood diphtheria with poor muscular coordination and nearsightedness; mother taught him at home during illness", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}
  schooling:
    - {value: "Lycée in Nancy (now Lycée Henri Poincaré); eleven years; mathematics teacher called him a 'monster of mathematics'", stage: "grammar or secondary school", run_by: "state or municipal", years: "1862–1873", ages: "8–19", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}
    - {value: "École Polytechnique (graduated 1875), then École des Mines", stage: university, run_by: "state or municipal", years: "1873–", ages: "19–", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  early_mathematics: {value: "advanced mathematics", note: "First in the national concours général in elementary mathematics after 1871; Lycée teacher called him a 'monster of mathematics' (S2); preparatory classes before Polytechnique 1873", certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "Biography"}], how_known: "SEP and MacTutor."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Excelled in written composition while still in elementary school; special home instruction from his mother during diphtheria recovery", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [French], certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "Biography"}], how_known: "Born and schooled in Nancy; SEP notes a German official billeted with the family in 1870 (German exposure possible but not scored as a childhood language)."}
  notable_events:
    - {value: "Serious childhood illness with diphtheria; mother gave special instruction", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor (year not given)."}
    - {value: "German occupation of Nancy; family billeted a German official", year: 1870, age: 16, certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1882–1908", certainty: 0.5, cites: [{source: S1, locator: "§1, §5"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Science needs unlimited free inquiry and must not submit to dogma; Catholics may do science if they set faith aside in the laboratory (Pasteur as example); science cannot found a morality (indicative premises never yield an imperative); religions are powerful when love of God supplies the moral motive, not demonstration", certainty: 0.7, cites: [{source: S5, locator: "whole (Libre examen 1909; Pasteur / catholiques / dogme / 'sans adhérer à aucune église')"}, {source: S6, locator: "La Morale et la Science ('Il ne peut pas y avoir de morale scientifique'; 'si nous aimons ce Dieu')"}], how_known: "Own published essays (S5, S6). About science–religion practice and morale foundations, not a personal locus confession."}
  primary_system: {value: UNKNOWN, how_known: "No citable own-words confession of belief, suspension, or denial of God. Libre examen's 'sans adhérer à aucune église' is first-person plural about freethinkers' impartiality, not a personal creed. Morale's God-talk is hypothetical for religious morale. Popular 'free thinker at 18' (famousscientists / ladissertation) and fr.wiki need_ref sentence unused (RUNBOOK §3.1)."}
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Rejected this pass: no explicit suspension of judgement about God in S1–S6; 'free thinker' reports are unsigned/popular or need_ref.", cites: [{source: S5, locator: "'sans adhérer à aucune église' passage"}]}
    - {code: ATHE, reason: "Rejected: Libre examen criticizes positivist 'catholicisme sans Dieu' as a new church; no positive denial of God.", cites: [{source: S5, locator: "positivistes / catholicisme sans Dieu"}]}
    - {code: CHRIST, reason: "Rejected: Catholic family claims are popular/unsourced; heritage never a code. Funeral at a Paris church (fr.wiki) is burial practice, not adult belief.", cites: [{source: S1, locator: "§1 (no religion passage)"}]}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "P19 researched silent on locus. S4–S6 read: Chance is about determinism and chance, not where God is; Libre examen and Morale discuss free inquiry and morale foundations without placing or denying God. Rhetorical 'bon Dieu' / 'merveilleux artiste' in Libre examen is not a locus profession. Named alternative: BELOW_THRESHOLD if a later scholarly biography (Bellivier, Rollet, Aline Boutroux) or a first-person suspension statement is treated as AGNOS under P20.", note: "Blockers: Aline Boutroux memoir; Bellivier; Rollet; English Last Essays print check for Morale."}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S4, locator: "Livre I §IV opening ('nous sommes devenus des déterministes absolus'; 'Tout phénomène… a une cause'; for an infinitely informed mind 'il n'y aurait pas de hasard')"}, {source: S1, locator: "§1 (three-body problem; recurrence; celestial mechanics)"}]
      how_known: "Own essay Chance / Le hasard in Science et méthode (1908), within working years; FR Wikisource primary text read. Second stream: SEP documents his lasting celestial-mechanics program (P48 corroborated). Certainty 0.5 because P40 is not met (alt 4)."
      rationale: "Scientist under P30 (three-body, celestial mechanics). Chance states absolute determinism for the inorganic world and that every phenomenon has a cause, so that for an infinitely informed mind chance would not exist — an explicit nature-order remark (P16). He then rehabilitates chance as sensitive dependence on initial conditions under those laws, and contrasts prayer for rain with the absurdity of praying for an eclipse (epistemic unpredictability, not miracle). No statement that rules out exceptions or miracles for all of nature (P40). Per P16 addendum / P35 logic: lawful remark without no-exception → B 3 @ 0.5, alternative 4, never 4."
      alternatives:
        - {value: 4, note: "No stated exceptionless / no-miracle claim (P40); Chance keeps a scientific role for chance under determinism.", cites: [{source: S4, locator: "sensitive-dependence and meteorology passages"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing on reward, punishment or afterlife in S1–S6 (Morale discusses moral motive, not afterlife)."}
    D_authority: {value: UNKNOWN, how_known: "Libre examen rejects submission of thought to dogma, but D asks revelation versus observation as a source of truth about the world; no scored revelation claim read (P19)."}
    E_scope: {value: BELOW_THRESHOLD, note: "Scored on the world's order (P7). Working science and Chance bear on E's first question but E is not scored from them alone without the in-group-exception question (P19).", how_known: "BELOW_THRESHOLD under P19."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, which takes precedence (§6, P19)."}
  statements:
    - text: "Mais cette conception n'est plus la nôtre ; nous sommes devenus des déterministes absolus, et ceux mêmes qui veulent réserver les droits du libre arbitre humain laissent du moins le déterminisme régner sans partage dans le monde inorganique. Tout phénomène, si minime qu'il soit, a une cause, et un esprit infiniment puissant, infiniment bien informé des lois de la nature, aurait pu le prévoir dès le commencement des siècles. … Pour lui en effet le mot de hasard n'aurait pas de sens, ou plutôt il n'y aurait pas de hasard."
      cites: [{source: S4, locator: "Livre I §IV, opening section I"}]
      date: "1908"
      context: "Essay 'Le Hasard' (Chance), Science et méthode, Book I ch. IV. Continues by defining chance via sensitive dependence on initial conditions and the meteorology / prayer-for-rain vs eclipse example."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "FR Wikisource transcription of Flammarion édition définitive; English IA OCR (sciencemethod00poinuoft) checked for the rain/eclipse parallel. Print Flammarion check pending."
    - text: "N'allez pas comprendre au moins que je veux interdire la Science aux hommes de foi, et en particulier aux catholiques. A Dieu ne plaise ! Je ne serais pas assez bête pour priver l'humanité des services d'un Pasteur. Il y a des hommes qui oublient leur foi en entrant au laboratoire… Mais, sans adhérer à aucune église, sommes-nous bien certains d'avoir toujours conservé l'impartialité qui convient au savant…"
      cites: [{source: S5, locator: "Pasteur / catholiques passage; later 'sans adhérer à aucune église'"}]
      date: "1909"
      context: "Address 'Le libre examen en matière scientifique', Revue de l'Université de Bruxelles 15 (1909), 285–295. First-person plural about freethinkers' impartiality; not coded as personal locus."
      axes: []
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Read via Wayback Machine capture of henripoincarepapers.univ-lorraine.fr HTML (2023-06-15). Used for self_described_science_religion_relation, not A."
    - text: "Il ne peut pas y avoir de morale scientifique ; mais il ne peut pas y avoir non plus de science immorale. … On ne peut pas démontrer qu'on doit obéir à un Dieu… Mais si nous aimons ce Dieu, toute démonstration deviendra inutile… La science ne peut donc à elle seule créer une morale."
      cites: [{source: S6, locator: "La Morale et la Science (indicative/imperative argument; 'si nous aimons ce Dieu')"}]
      date: "1913"
      context: "Chapter 'La Morale et la Science' in Dernières pensées (posthumous 1913/1917). Hypothetical about religious morale's motive; not a confession of belief."
      axes: []
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "UQAC Classiques des sciences sociales PDF of the 1917 Flammarion text (pdftotext). Used for science–religion relation, not A."
  changes_over_life: []
  coder_notes: "Deepen D1: A stays UNKNOWN (no locus). B stays 3 @ 0.5 with basis upgraded inference_from_work → written_profession (Chance), support corroborated, alt 4. P40 not applied: Chance keeps chance under laws. Conventionalism about geometry/laws is not a B claim. Free-thinker@18 popular claim and fr.wiki need_ref unused for scoring. Chart still unplotted (A UNKNOWN; B faded)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "French (Lorraine)", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated in S1–S6. Popular Catholic-family claims and fr.wiki need_ref unused (RUNBOOK §3.1)."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated in S1–S6."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated in S1–S6."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1882–1908", certainty: 0.5, cites: [{source: S1, locator: "§1, §5"}], how_known: "1882 to 1908, first to last listed lasting contribution (P29, P30); the end year is inferred (0.5)."}
  age_at_first_lasting_contribution: {value: 28, certainty: 0.7, cites: [{source: S1, locator: "§1, §5"}], how_known: "1882 − 1854 = 28 (P30)."}
  first_evidence_of_lio_type_views: {value: "1908: Chance / Le hasard (absolute determinism; chance as sensitive dependence)", year: 1908, certainty: 0.7, cites: [{source: S4, locator: "Livre I §IV"}], how_known: "LIO-type nature-order remark (P27) in own words within the major-work span. Earlier writings not re-read for earlier B remarks."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S4, locator: "Livre I §IV"}, {source: S1, locator: "§1"}], how_known: "Science et méthode 1908 closes the listed span; Chance is inside it."}
  worldview_during_major_work: {value: "A UNKNOWN; B 3 @ 0.5 from Chance (written_profession) plus working celestial mechanics; science–religion: free inquiry, no scientific morale", certainty: 0.5, cites: [{source: S4, locator: "Livre I §IV"}, {source: S5, locator: "whole"}, {source: S6, locator: "La Morale et la Science"}], how_known: "Synthesis of D1 primaries; not a stronger code."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Top of his class in mathematics; École Polytechnique; lasting work in topology and celestial mechanics.", certainty: 0.5, cites: [{source: S1, locator: "§1"}], how_known: "Coder's reading."}
  form_acquired: {value: "childhood or adolescence", certainty: 0.5, cites: [{source: S1, locator: "§1 (teacher's remark at age 13)"}, {source: S2, locator: "Biography ('monster of mathematics')"}], how_known: "Coder's reading."}
  circle_present: {value: "unclear", rationale: "No God–Nature identity statement. Chance is about determinism and ignorance, not pantheism.", certainty: 0.5, cites: [{source: S4, locator: "Livre I §IV"}], how_known: "Coder's reading."}
  reading: "As belief, not finding: geometric form present from adolescence; circle unclear. Worldview still unplottable (A UNKNOWN; B faded). The record does not test H1."
  notes: ""

institutions:
  - {value: "University of Paris, Faculty of Sciences", role: professor, years: "1881–1912", kind: university, certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  - {value: "Bureau des Longitudes", role: member, years: "1893–1912", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  - {value: "French Academy of Sciences", role: "member (1887), president (1906)", years: "1887–1912", kind: "academy or learned society", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
collaborators:
  - {value: "Gösta Mittag-Leffler", relation: correspondent, note: "fifty letters on the prize memoir, 1887–1890", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 35"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Family religion / free-thinker@18: popular sites and fr.wikipedia need_ref sentence not used for scoring (RUNBOOK §3.1)."
    - "Libre examen read via Wayback unofficial HTML of henripoincarepapers; print Revue de l'Université de Bruxelles 15 (1909) check pending."
    - "Morale et science read via UQAC PDF of 1917 Flammarion; Dover/Bolduc English Last Essays print unread."
  open_questions:
    - "Read Aline Boutroux (sister) memoir and André Bellivier, Henri Poincaré ou la vocation souveraine, for childhood religion / free-thinker claim with citation."
    - "Read Laurent Rollet biographical work for any documented adult religious stance."
    - "Print check: Flammarion Science et méthode (Chance); Revue de l'Université de Bruxelles 15 (1909) Libre examen; Flammarion Dernières pensées / Bolduc Last Essays for Morale."
    - "Any first-person locus or no-exception claim (letters, Cahiers) that would lift A or apply P40 to B."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Gerhard Heinzmann and David Stump"
    year: 2026
    citation: "Heinzmann, Gerhard, and David Stump. \"Henri Poincaré.\" Stanford Encyclopedia of Philosophy, first published 3 September 2013, substantive revision 10 September 2026. https://plato.stanford.edu/entries/poincare/."
    url: "https://plato.stanford.edu/entries/poincare/"
    accessed: 2026-10-24
    reliability_note: "Peer-reviewed reference article; no religion section."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions]
  - id: S2
    type: secondary
    kind: encyclopedia
    author: "J. J. O'Connor and E. F. Robertson"
    year: 2003
    citation: "O'Connor, J. J., and E. F. Robertson. \"Henri Poincaré.\" MacTutor History of Mathematics, University of St Andrews, last update October 2003. https://mathshistory.st-andrews.ac.uk/Biographies/Poincare/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Poincare/"
    accessed: 2026-10-24
    reliability_note: "Signed biography; childhood diphtheria and mother instruction."
    source_quality: "reference entry"
    used_for: [basics, contribution, childhood, worldview, collaborators]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Henri Poincaré"
    year: 1908
    citation: "Poincaré, Henri. \"Le Hasard\" (Book I, ch. IV). In Science et méthode. Paris: Flammarion, 1908 (édition définitive). French text: Wikisource, Science et méthode/Livre premier, § IV. https://fr.wikisource.org/wiki/Science_et_m%C3%A9thode/Livre_premier,_%C2%A7_IV. English parallel: Science and Method, Internet Archive sciencemethod00poinuoft (OCR)."
    url: "https://fr.wikisource.org/wiki/Science_et_m%C3%A9thode/Livre_premier,_%C2%A7_IV"
    accessed: 2026-10-24
    reliability_note: "Primary philosophical essay; Wikisource transcription of Flammarion; rain/eclipse parallel checked in English IA OCR."
    source_quality: "primary / own words"
    used_for: [worldview, timing, lane_b]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Henri Poincaré"
    year: 1909
    citation: "Poincaré, Henri. \"Le libre examen en matière scientifique.\" Revue de l'Université de Bruxelles 15 (1909): 285–295. HTML at henripoincarepapers.univ-lorraine.fr/chp/text/hp1909ru.html; read via Wayback Machine capture 2023-06-15."
    url: "https://web.archive.org/web/20230615063024/https://henripoincarepapers.univ-lorraine.fr/chp/text/hp1909ru.html"
    accessed: 2026-10-24
    reliability_note: "Primary address; unofficial HTML via Wayback (print journal check pending)."
    source_quality: "primary / own words"
    used_for: [worldview]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Henri Poincaré"
    year: 1913
    citation: "Poincaré, Henri. \"La Morale et la Science.\" In Dernières pensées. Paris: Flammarion, 1913/1917. Electronic text: Les Classiques des sciences sociales (UQAC) PDF of the 1917 edition (pdftotext this pass)."
    url: "https://fr.wikisource.org/wiki/Derni%C3%A8res_pens%C3%A9es/Chapitre_8"
    accessed: 2026-10-24
    reliability_note: "Primary posthumous essay; UQAC PDF of 1917 Flammarion; Wikisource chapter page exists. Bolduc English Last Essays unread."
    source_quality: "primary / own words"
    used_for: [worldview]
---

# Henri Poincaré

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Henri Poincaré (1854–1912), French mathematician, physicist and philosopher of science: Fuchsian functions, the three-body problem, the Poincaré conjecture, conventionalism [S1, S2]. Deepen D1: A UNKNOWN (no locus in own words); B 3 at 0.5 written_profession from Chance / Le hasard (alternative 4; P16/P35/P40); mid_basin UNKNOWN. Chart still unplotted.

## Life and work

Nancy, Polytechnique, Mines; Caen, then the University of Paris; Academy of Sciences and Académie française [S1].

## Contribution and impact

Fuchsian functions (1882), the prize memoir on the three-body problem (1889), Science and Hypothesis (1902), the conjecture (1904), Science and Method (1908) [S1, S2, S4].

## Childhood and education

University medical family in Nancy; childhood diphtheria with home instruction from his mother Eugénie; Lycée at Nancy (teacher: "monster of mathematics"); first in the concours général in mathematics; Polytechnique then Mines [S1, S2]. Family religion not documented in citable sources this pass.

## Adult working worldview

**Lane A.** No citable own-words placing or denying of God. Libre examen (1909) defends unlimited free inquiry and allows Catholics in the laboratory if they set faith aside; "sans adhérer à aucune église" is first-person plural about freethinkers' impartiality, not a personal locus [S5]. Morale et science argues science cannot found a morality; "si nous aimons ce Dieu" is hypothetical for religious morale [S6]. Popular free-thinker-at-18 claims unused. A UNKNOWN; primary_system UNKNOWN.

**Lane B (separate).** Chance / Le hasard: "nous sommes devenus des déterministes absolus"; every phenomenon has a cause; for an infinitely informed mind there would be no chance — then chance as sensitive dependence under laws; prayer for rain vs eclipse [S4]. Lawful nature-order remark without no-exception (P40 not met) → B 3 @ 0.5, alt 4. Corroborated by SEP celestial-mechanics program [S1].

## Heritage (context only)

French, from Lorraine [S1]. Religious heritage by birth UNKNOWN in S1–S6.

## Timing

First lasting contribution 1882, at 28 [S1]. Chance (1908) is an LIO-type nature-order remark during major work [S4].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Mathematical training from adolescence [S1, S2]; circle unclear. H1 not tested.

## Open questions

- Aline Boutroux; Bellivier; Rollet for childhood/adult religion with citation.
- Print checks for Chance, Libre examen, Morale / Last Essays.
- Any first-person locus or P40 no-exception claim.

## Research log

- 2026-10-15: Read SEP and MacTutor; web search on his religion found only an unsigned popular site and a 2024 article excerpt; neither used for a score.
- 2026-10-24 (D1): Read Chance (Wikisource FR + IA English OCR), Libre examen (Wayback HTML), Morale et science (UQAC PDF). MacTutor childhood reopened. A UNKNOWN→UNKNOWN; B 3@0.5→3@0.5 (basis written_profession). Chart-moving no.
