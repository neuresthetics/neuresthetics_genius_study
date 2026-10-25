---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA8)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #197, F3 rank 210). P47–P50. Dual bio Wikipedia EN (S4) + Britannica (S1). Own-voice B: 1 Jan 1662 letter to Cureau de la Chambre (DBNL / Huygens Oeuvres IV No. 990; S5) — 'la nature agit tousjours par les voyes les plus courtes' / 'par les moyens les plus aysez'. Own-voice A/CHRIST: Latin poem 'Cede Deo, seu Christus moriens' (Œuvres I, Tannery; S6) — incarnation and Passion. Secondary Catholic frame: Society of Catholic Scientists (S7); Laffont/Académie Toulouse (S8); Augustins epitaph nesciri ama from Imitation of Christ (S9). B support single→corroborated (S1+S5); value stays 3 @0.5 alt 4 (P16 addendum: lawful-order remark, no stated no-exception claim). A UNKNOWN→0 @0.7 support single (poem; Laffont/SCS are CHRIST practice/frame, not a second A locus source). primary_system UNKNOWN→CHRIST @0.5 (poem is literary devotion; working-years creed thinner than Euler/Pascal). mid_basin BELOW_THRESHOLD (B at 0.5). Chart-moving YES: A scored so now plottable (faded hollow). No fallacy_catalog; no figures/. Draft, not reviewed."}
    - {date: 2026-10-20, by: "Grok Bot", summary: "AA10 audit fix: birth date 1601 lowered to 0.5 (1601 vs 1607 is a real dispute)."}
    - {date: 2026-10-20, by: "Grok Bot", summary: "AA9 audit fix: birth year 1607 (Pengelley, S3) recorded as the alternative; age 37 lowered to 0.5 with 31 as the alternative."}
    - {date: 2026-10-20, by: "Grok Bot", summary: "AA8 audit fixes: least-time item and span end take 1662 as alternative (1638–1662); lesser theorem 0.7 on the 18 October 1640 letter to Frenicle (Pengelley, S3)."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA8, order P32: F 3, rank 210). Source: Britannica, signed by Carl B. Boyer (scholars edition, read in full). Lasting work: his method for tangents and maxima and minima, defended in the 1638 controversy with Descartes through Mersenne and 'fully justified some 30 years later in the calculus of Sir Isaac Newton' (he is 'regarded as the inventor of the differential calculus'); 'Fermat's lesser theorem', announced in letters (1640; 'A more important result'); and the principle of least time for refraction, 'twenty years' after Descartes's 1637 Dioptrique (so about 1657), later 'verified experimentally' by Fizeau (S1). Span 1638–1657 at 0.5 (1657 is inferred from 'twenty years later'; alternative end 1662, the 'Analysis ad refractiones' of 1 January 1662, where the least-time minimisation itself is first worked out; the August 1657 letter states only the qualitative shortest-path principle), age 37. AA8 audit: lesser theorem now 0.7 on the letter to Frenicle of 18 October 1640 (Œuvres de Fermat II, pp. 206–212, as quoted by Pengelley, S3). Scientist (P30): the principle of least time is a law about light; B 3 at 0.5, alternative 4 (P35). Worldview: no own words read; primary education in a Franciscan school (S1). primary_system UNKNOWN; A UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: de-fermat-pierre
  display_name: "Pierre de Fermat"
  roster:
    canonical_name: "Pierre de Fermat"
    rank: 210
    F: 3
    models: [Claude, Gemini, Grok]
    band: "core (3–4)"
    status: "core"
    field: "mathematics"
    field_bucket: "mathematics"
  full_name: {value: "Pierre de Fermat", certainty: 0.7, cites: [{source: S1, locator: "Introduction; Life and early work"}, {source: S4, locator: "lead"}], how_known: "Britannica and Wikipedia EN: Pierre de Fermat."}
  native_name: {value: "Pierre de Fermat", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  aliases:
    - {name: "Fermat-Pierre de", kind: "roster alias"}

basics:
  birth:
    date: {value: "1601-08-17", certainty: 0.5, cites: [{source: S1, locator: "Introduction"}, {source: S3, locator: "§1 heading"}, {source: S4, locator: "infobox; Note a"}], how_known: "Britannica and Wikipedia give 17 August 1601. Alternative 1607: Pengelley (S3) and a real birth-year dispute (AA9/AA10; Wikipedia Note a)."}
    place: {value: "Beaumont-de-Lomagne", modern_name: "Beaumont-de-Lomagne, France", polity_then: "Kingdom of France", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S4, locator: "Biography"}], how_known: "Britannica and Wikipedia."}
  death:
    date: {value: "1665-01-12", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S4, locator: "infobox"}], how_known: "Britannica and Wikipedia."}
    place: {value: "Castres", modern_name: "Castres, France", polity_then: "Kingdom of France", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S4, locator: "Death"}], how_known: "Britannica and Wikipedia."}
  first_lasting_contribution_year: {value: 1638, certainty: 0.7, cites: [{source: S1, locator: "Disagreement with other Cartesian views"}], how_known: "1638 controversy with Descartes, through Mersenne, on the validity of their tangent methods (S1): the earliest documented public statement of the method (P30)."}
  era_bucket: {value: "1600 to 1749", certainty: 1.0, cites: [{source: S1, locator: "text"}], how_known: "1638 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "France (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Life and early work"}], how_known: "Toulouse."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Latin", "French"], certainty: 0.7, cites: [{source: S1, locator: "Analyses of curves"}, {source: S4, locator: "Biography"}, {source: S5, locator: "letter French"}, {source: S6, locator: "Latin poem"}], how_known: "Latin papers and poem; scientific letters in French (S5); Wikipedia: six languages."}
  occupations: {value: ["lawyer", "magistrate", "mathematician"], certainty: 0.7, cites: [{source: S1, locator: "Life and early work"}, {source: S4, locator: "lead"}], how_known: "Councillor at the Parlement of Toulouse; mathematics as sustained private work."}

contribution:
  fields: {value: ["mathematics", "number theory", "optics"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S4, locator: "Work"}], how_known: "Britannica and Wikipedia."}
  lasting_original_contributions:
    - {value: "Method of tangents and of maxima and minima (equivalent to differentiation)", year: 1638, kind: "method", lasting: "'led him to be regarded as the inventor of the differential calculus'; 'Fermat's views were fully justified some 30 years later in the calculus of Sir Isaac Newton' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Introduction; Disagreement with other Cartesian views"}], how_known: "Developed in the mid-1630s; first documented public statement the 1638 controversy (S1)."}
    - {value: "Fermat's lesser (little) theorem", year: 1640, kind: "discovery", lasting: "'now known as Fermat's lesser theorem'; he is 'often called the founder of the modern theory of numbers' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Work on theory of numbers"}, {source: S3, locator: "§1 (letter of 18 October 1640)"}], how_known: "Letter to Frenicle, 18 October 1640: 'Without fail, every prime number measures one of the powers −1 of any progression whatever, and the exponent of the said power is a submultiple of the given prime number −1' (S3, citing Œuvres de Fermat II, pp. 206–212). A June 1640 letter already gives the case a = 2 (S3)."}
    - {value: "Principle of least time (law of refraction)", year: 1657, kind: "law or principle", lasting: "'His argument concerning the speed of light was found later to be in agreement with the wave theory of ... Huygens, and in 1849 it was verified experimentally by A.-H.-L. Fizeau' (S1)", certainty: 0.5, cites: [{source: S1, locator: "Disagreement with other Cartesian views"}, {source: S5, locator: "No. 990, 1 Jan 1662"}], how_known: "'Twenty years later' than Descartes's Dioptrique (1637), so about 1657 (August 1657 letter to Cureau de la Chambre, qualitative principle); 0.5. Alternative 1662: least-time minimisation in the 1 January 1662 letter (S5) and 'Analysis ad refractiones' (AA8)."}
  evidence_of_impact:
    - {value: "'often called the founder of the modern theory of numbers'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    - {value: "Fermat's last theorem, proved by Wiles (1994/1995)", kind: "named after them", certainty: 0.7, cites: [{source: S1, locator: "Work on theory of numbers"}, {source: S4, locator: "Work"}], how_known: "Britannica; Wikipedia."}
  major_works:
    - {value: "'De Linearum Curvarum cum Lineis Rectis Comparatione' (his only mathematical work published in his lifetime)", year: 1660, kind: "paper or paper series", certainty: 0.7, cites: [{source: S1, locator: "Analyses of curves"}], how_known: "Britannica."}
    - {value: "Introduction to Loci (analytic geometry; posthumous 1679)", year: 1679, kind: "paper or paper series", certainty: 0.7, cites: [{source: S1, locator: "Life and early work"}], how_known: "Britannica."}
    - {value: "'Cede Deo, seu Christus moriens' (Latin poem to Balzac)", year: UNKNOWN, kind: "other", certainty: 0.5, cites: [{source: S6, locator: "Œuvres I, pp. 390ff / Wikisource djvu 439–440"}], how_known: "Printed in Tannery–Henry Œuvres I; year of composition not fixed here (Balzac d. 1654)."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founder of modern number theory (S1).", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Roman Catholic", certainty: 0.5, cites: [{source: S7, locator: "closing paragraph"}, {source: S8, locator: "Introduction (idées religieuses… Église catholique)"}], how_known: "SCS: family 'devoutly Catholic'. Laffont: religious ideas inscribed in the Catholic Church. Scholarly/secondary; 0.5."}
  family_religious_practice: {value: "Daughters entered religious life; one son became archdeacon of Fimarens", certainty: 0.5, cites: [{source: S7, locator: "closing paragraph"}], how_known: "Society of Catholic Scientists (secondary institutional page)."}
  parents_and_household:
    - {value: "Of Basque origin; father Dominique Fermat, leather merchant and consul of Beaumont-de-Lomagne; mother Claire de Long", role: "family", certainty: 0.7, cites: [{source: S1, locator: "Life and early work"}, {source: S4, locator: "Biography"}], how_known: "Britannica (Basque); Wikipedia names parents."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated beyond merchant prosperity (S4)."}
  schooling:
    - {value: "Local Franciscan school; law probably at Toulouse, perhaps Bordeaux; baccalaureate in civil law, Orléans (1626)", certainty: 0.7, cites: [{source: S1, locator: "Life and early work"}, {source: S4, locator: "Biography"}], how_known: "Britannica Franciscan school; Wikipedia Orléans BCL 1626 (Britannica had said 1631)."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1638–1657", certainty: 0.5, cites: [{source: S1, locator: "Disagreement with other Cartesian views"}], how_known: "Equals timing.major_work_period; alternative 1638–1662 (least-time letter)."}
  nominal_affiliations:
    - {value: "Roman Catholic (family practice; Franciscan schooling)", certainty: 0.5, cites: [{source: S1, locator: "Life and early work"}, {source: S7, locator: "closing paragraph"}], how_known: "Heritage and family practice (S1, S7); not alone a worldview code (CHRIST guidance)."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No direct science–religion essay read."}
  primary_system:
    value: CHRIST
    basis: written_profession
    certainty: 0.5
    cites: [{source: S6, locator: "Cede Deo, seu Christus moriens (Œuvres I)"}, {source: S8, locator: "Introduction — idées religieuses… Église catholique"}, {source: S7, locator: "closing paragraph"}]
    how_known: "Own Latin poem confesses Christ incarnate and dying (S6). Laffont places his religious ideas in the Catholic Church (S8); SCS reports devout Catholic family practice (S7). Certainty 0.5: the poem is literary devotion (carmen to Balzac), not a working-years creed treatise; named alternative UNKNOWN if the poem is judged rhetorical display only."
    rationale: "Own writing shows Christian belief with Christ (incarnation and Passion): 'Assumpsit veros morituræ carnis amictus' and the Passion narrative under the title Christus moriens (S6). Nature acknowledges God as parent ('Deus ecce Deus, quem prona parentem / Agnoscit natura suum') — creator distinct from creation, not Deus sive Natura. Named alternative UNKNOWN: Latin humanistic poetry may not fix adult working worldview the way Pensées or Lettres do. CLASS_THEISM rejected (no a posteriori argument from the world to God read; P22). DEISM rejected (incarnation/Christ accepted; P27). CLTHEI not primary (no petition/miracle doctrine for nature scored from the poem)."
  secondary_system: {value: UNKNOWN, how_known: "One system."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Chosen at 0.5: poem Christus moriens + Catholic scholarly frame (S6, S8). Own writing shows Christ/church piety (CHRIST use_when).", cites: [{source: S6, locator: "title and incarnation lines"}]}
    - {code: CLASS_THEISM, reason: "Rejected: no first-cause or design argument from the world to God read (P22).", cites: [{source: S6, locator: "poem"}]}
    - {code: CLTHEI, reason: "Rejected as primary: poem is Christological devotion, not a doctrine of ongoing petitionary intervention in nature.", cites: [{source: S6, locator: "poem"}]}
    - {code: DEISM, reason: "Rejected: accepts Christ/incarnation; does not reject revelation (P27).", cites: [{source: S6, locator: "Assumpsit… carnis amictus"}]}
  lio_axes:
    A_locus:
      value: 0
      basis: written_profession
      certainty: 0.7
      support: single
      cites: [{source: S6, locator: "Cede Deo — Deus ecce Deus; Assumpsit veros morituræ carnis amictus"}]
      how_known: "Own poem (Tannery Œuvres I / Wikisource). Named alternative 1 (nature-parent wording could be read as lean rather than pole). Support single: Laffont/SCS corroborate Catholic practice/frame, not a second independent locus statement."
      rationale: "At the interventionist (transcendent-person) pole: 'Deus ecce Deus, quem prona parentem / Agnoscit natura suum' — God whom nature acknowledges as its parent, distinct from the world; the eternal Son 'Assumpsit veros morituræ carnis amictus' (took true garments of mortal flesh). Not PANT (parent of nature ≠ identical with nature). Named alternative: 1, if the parent-of-nature line is judged lean rather than pole."
      alternatives:
        - {value: 1, note: "Lean reading of creator-parent language without full pole features.", cites: [{source: S6, locator: "prona parentem Agnoscit natura"}]}
    B_cause:
      value: 3
      basis: consistent_private_letters
      certainty: 0.5
      support: corroborated
      cites: [{source: S5, locator: "No. 990, 1 Jan 1662 — nature toujours voies les plus courtes / moyens les plus aisés"}, {source: S1, locator: "Disagreement with other Cartesian views"}]
      how_known: "Own scientific letter (S5) states a general economy of nature; Britannica (S1) reports the least-time principle. P16 addendum (Hilbert pattern): lawful-order remark with no stated no-exception claim → B 3 at 0.5, alternative 4, never forced to 4. Independent ids → corroborated (P48)."
      rationale: "Scored on his account of nature (P6/P16). Scientist via least-time (P30). Own words (1 Jan 1662 to Cureau): 'ce principe si commun & si estably que la nature agit tousjours par les voyes les plus courtes'; and 'la nature agist tousiours par les moyens les plus aysez, c'est à dire ou par les lignes les plus courtes… ou en tout cas par le temps le plus court' (S5). Lawful teleological economy of light paths. No stated miracle exception or explicit exceptionless metaphysics beyond the optics principle → value 3 at 0.5, named alternative 4 (P16 addendum / P35). Prior inference_from_work alone is now backed by the letter."
      alternatives:
        - {value: 4, note: "'tousjours' / always could be read as exceptionless; P16/P35 keep value at 3 @0.5.", cites: [{source: S5, locator: "No. 990"}]}
    C_ledger: {value: UNKNOWN, how_known: "Poem has Passion/salvation imagery but no scored doctrine of personal reward and punishment read for C."}
    D_authority: {value: UNKNOWN, how_known: "Poem rejects pagan oracles for Christian God ('Cede Deo') but no revelation-vs-observation split on science read."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scientist (P30); no own statement on same-rules/in-group exceptions. Working science alone does not score E (P19)."}
  mid_basin: {value: BELOW_THRESHOLD, certainty: 0.5, cites: [{source: S6, locator: "Cede Deo"}, {source: S5, locator: "No. 990"}], how_known: "P4: A 0 (0.7) ≤ 1 and B 3 (0.5) ≥ 3, but B is only at 0.5, below the test's 0.7 bar → BELOW_THRESHOLD (P4/P10)."}
  statements:
    - text: "si nous voulions employer dans ceste recherche ce principe si commun & si estably que la nature agit tousjours par les voyes les plus courtes, nous pourrions y trouver facilement nostre compte"
      cites: [{source: S5, locator: "No. 990, P. de Fermat à Cureau de la Chambre, 1 Jan 1662"}]
      date: "1662-01-01"
      context: "Letter on refraction: introducing the common principle that nature always acts by the shortest ways."
      axes: [B_cause]
      kind: "published letter"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "DBNL text of Huygens Oeuvres complètes IV, No. 990 (copy published by Clerselier among Descartes letters). Long-s/orthography as in DBNL."
    - text: "bien que je fusse asseuré de la verité de mon principe, et qu'il n'y ayt rien de si probable ni de si apparent que ceste supposition, que la nature agist tousiours par les moyens les plus aysez, c'est à dire ou par les lignes les plus courtes lors qu'elles n'emportent pas plus de temps, ou en tout cas par le temps le plus court afin d'accourcir son trauail & de venir plustost à bout de son operation"
      cites: [{source: S5, locator: "No. 990, same letter"}]
      date: "1662-01-01"
      context: "Same letter: restates the principle as easiest means — shortest lines when time equal, else least time."
      axes: [B_cause]
      kind: "published letter"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Same DBNL No. 990."
    - text: "Cede Deo. Cessit veterum numerosa propago / Cœlicolûm : Deus ecce Deus, quem prona parentem / Agnoscit natura suum, cui terra, salumque / Paret"
      cites: [{source: S6, locator: "Œuvres I / Wikisource djvu 439"}]
      context: "Latin poem 'Cede Deo, seu Christus moriens', carmen amoebaeum to Balzac: yield to God; nature acknowledges God as parent."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Tannery–Henry Œuvres de Fermat I via Wikisource page images. Composition year not fixed (Balzac d. 1654)."
    - text: "Deus unus erat, natusque supremi / Æterna æternùm manans de mente parentis / Assumpsit veros morituræ carnis amictus"
      cites: [{source: S6, locator: "Œuvres I / Wikisource djvu 439"}]
      context: "Same poem: one God; the eternal Son took true garments of mortal flesh (incarnation)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Same Wikisource pages; Passion continuation on djvu 440."
  changes_over_life: []
  coder_notes: "Deepen D1. B firmed with primary letter (support corroborated; certainty still 0.5 under P16 addendum). A from poem only (single). Mahoney Mathematical Career (IA print-disabled) not opened for religion. Laffont HAL chapter (hal-02454784) 403; used Académie Toulouse 2022 PDF excerpt instead. Do not force plot beyond A becoming scorable. No fallacy_catalog; figures/ untouched."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Basque origin (Britannica); Gascon / Beaumont-de-Lomagne", certainty: 0.5, cites: [{source: S1, locator: "Life and early work"}, {source: S4, locator: "Biography"}], how_known: "Britannica Basque; Wikipedia Gascony."}
  religious_heritage_by_birth: {value: "Roman Catholic", certainty: 0.5, cites: [{source: S7, locator: "closing paragraph"}, {source: S1, locator: "Life and early work"}], how_known: "Franciscan schooling (S1); SCS devout Catholic family (S7). Heritage only."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Franciscan school implies Catholic instruction; not documented as catechism text."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1638–1657", certainty: 0.5, cites: [{source: S1, locator: "Disagreement with other Cartesian views"}], how_known: "Tangent-method controversy (1638) to the least-time principle (about 1657), the first and last lasting items (P29, P30); 0.5, following the weakest lasting item. Alternative 1638–1662 (least-time letter S5)."}
  age_at_first_lasting_contribution: {value: 37, certainty: 0.5, cites: [{source: S1, locator: "Introduction; Disagreement with other Cartesian views"}, {source: S3, locator: "§1 heading"}], how_known: "1638 − 1601 = 37 (P30 year difference); 0.5 because the birth year is disputed. Alternative 31 (1638 − 1607, S3)."}
  first_evidence_of_lio_type_views: {value: "1662-01-01", certainty: 0.7, cites: [{source: S5, locator: "No. 990"}], how_known: "Least-time letter states the nature-economy principle (B). Poem date UNKNOWN."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.5, cites: [{source: S5, locator: "No. 990"}], how_known: "1662 least-time letter is the alternative span end (1638–1662); poem undated (before Balzac d. 1654)."}
  worldview_during_major_work: {value: "CHRIST @0.5; A 0; B 3 @0.5", certainty: 0.5, cites: [{source: S6, locator: "poem"}, {source: S5, locator: "No. 990"}], how_known: "As coded; poem year not fixed."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Analytic geometry of curves (S1).", certainty: 0.5, cites: [{source: S1, locator: "Analyses of curves"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "no", rationale: "Poem: God as parent of nature, not identical with nature (S6).", certainty: 0.5, cites: [{source: S6, locator: "prona parentem Agnoscit natura"}], how_known: "Coder's reading of poem vs PANT circle."}
  reading: "Lane B only: Christian transcendent God (poem) with a lawful least-time economy of nature (1662 letter). Not a chart finding."
  notes: "Do not treat Lane B as evidence for mid_basin beyond the scored axes."

institutions:
  - {value: "Parlement of Toulouse", role: "councillor; Criminal Court", years: "1631–1665", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "Life and early work"}, {source: S4, locator: "Biography"}], how_known: "Wikipedia: sworn May 1631; Britannica councillor from 1634 / Criminal Court 1638."}
collaborators:
  - {value: "Blaise Pascal", relation: "correspondent", note: "probability (1654)", certainty: 0.7, cites: [{source: S1, locator: "Disagreement with other Cartesian views"}], how_known: "Britannica."}
  - {value: "René Descartes", relation: "rival or critic", note: "tangents; refraction", certainty: 0.7, cites: [{source: S1, locator: "Disagreement with other Cartesian views"}], how_known: "Britannica."}
  - {value: "Marin Mersenne", relation: "correspondent", note: "intermediary", certainty: 0.7, cites: [{source: S1, locator: "Disagreement with other Cartesian views"}], how_known: "Britannica."}
  - {value: "Marin Cureau de la Chambre", relation: "correspondent", note: "optics / least-time letters 1657–1662", certainty: 0.7, cites: [{source: S5, locator: "No. 990"}], how_known: "1662 letter (S5)."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 210"}], how_known: "Study roster."}
  controversies:
    - {value: "Birth year 1601 vs 1607", certainty: 0.7, cites: [{source: S4, locator: "Note a"}, {source: S3, locator: "§1 heading"}], how_known: "Wikipedia and Pengelley."}
    - {value: "Posthumous Augustins epitaph uses Imitation of Christ maxim nesciri ama (funerary; not scored as A)", certainty: 0.5, cites: [{source: S9, locator: "RA 572 inscription"}, {source: S8, locator: "Introduction — devise"}], how_known: "Musée des Augustins transcription (S9); Laffont ties motto to Imitation (S8)."}
  data_quality_flags:
    - "A support single (poem only for locus)."
    - "B certainty capped at 0.5 (P16 addendum) despite primary letter."
    - "Poem composition year UNKNOWN."
    - "Mahoney unread; Laffont HAL chapter 403."
  open_questions:
    - "Date and full text context of Cede Deo (Balzac correspondence)."
    - "Mahoney or full Laffont chapter for further creed evidence (could raise CHRIST certainty or corroborate A)."
    - "Whether 'tousjours' should ever flip B to 4 under P40 ( presently held at 3 @0.5)."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Carl B. Boyer"
    citation: "Boyer, Carl B. 'Pierre de Fermat.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/Pierre-de-Fermat/34048"
    url: "https://kids.britannica.com/scholars/article/Pierre-de-Fermat/34048"
    accessed: 2026-10-19
    reliability_note: "Signed article, scholars edition, read in full at creation; deepen re-used for dual bio / least-time."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, timing, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [review]
  - id: S3
    type: secondary
    kind: "journal article"
    author: "David Pengelley"
    citation: "Pengelley, David. 'How did Fermat discover his theorem?' arXiv:2502.11165 (2025). https://arxiv.org/abs/2502.11165"
    url: "https://arxiv.org/abs/2502.11165"
    accessed: 2026-10-19
    reliability_note: "Preprint quoting the 18 October 1640 letter from Tannery and Henry, Œuvres de Fermat II, pp. 206–212; the letter section read."
    source_quality: "other"
    used_for: [contribution, basics]
  - id: S4
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "Wikipedia. 'Pierre de Fermat.' https://en.wikipedia.org/wiki/Pierre_de_Fermat"
    url: "https://en.wikipedia.org/wiki/Pierre_de_Fermat"
    accessed: 2026-10-24
    reliability_note: "P50 dual bio with S1; birth-year note and biography read."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, institutions, review]
  - id: S5
    type: primary
    kind: "letter"
    author: "Pierre de Fermat"
    citation: "Fermat to Marin Cureau de la Chambre, 1 January 1662. In Christiaan Huygens, Oeuvres complètes, Tome IV, No. 990 (DBNL). https://www.dbnl.org/tekst/huyg003oeuv04_01/huyg003oeuv04_01_0044.php"
    url: "https://www.dbnl.org/tekst/huyg003oeuv04_01/huyg003oeuv04_01_0044.php"
    accessed: 2026-10-24
    reliability_note: "Primary letter text (Carcavy/BN copies as edited in Huygens Oeuvres); also printed by Clerselier among Descartes letters."
    source_quality: "primary / own words"
    used_for: [worldview, contribution, collaborators, timing]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Pierre de Fermat"
    citation: "Fermat, Pierre de. 'Cede Deo, seu Christus moriens' (carmen ad Balzacum). In Œuvres de Fermat, ed. Paul Tannery and Charles Henry, Tome I (Paris: Gauthier-Villars, 1891), via Wikisource page images djvu 439–440. https://fr.wikisource.org/wiki/Page:%C5%92uvres_de_Fermat,_Tannery,_tome_1,_1891.djvu/439"
    url: "https://fr.wikisource.org/wiki/Page:%C5%92uvres_de_Fermat,_Tannery,_tome_1,_1891.djvu/439"
    accessed: 2026-10-24
    reliability_note: "Scholarly edition page images (Tannery–Henry); Latin poem read for incarnation and Cede Deo lines; Passion continuation on djvu 440."
    source_quality: "primary / own words"
    used_for: [worldview, contribution]
  - id: S7
    type: secondary
    kind: "institutional page"
    author: "Society of Catholic Scientists"
    citation: "Society of Catholic Scientists. 'Pierre de Fermat.' Scientists of the Past. https://catholicscientists.org/scientists-of-the-past/pierre-de-fermat/"
    url: "https://catholicscientists.org/scientists-of-the-past/pierre-de-fermat/"
    accessed: 2026-10-24
    reliability_note: "Short institutional biography; family devout Catholic / children in orders — heritage and practice context, not own words."
    source_quality: "other"
    used_for: [childhood, heritage, worldview]
  - id: S8
    type: secondary
    kind: "book chapter"
    author: "Jean-Luc Laffont and Yves Le Pestipon (eds./intro)"
    citation: "Laffont, Jean-Luc, and Yves Le Pestipon. Introduction to Nouveaux regards sur Pierre de Fermat, Mémoires de l'Académie des Sciences, Inscriptions et Belles-Lettres de Toulouse, vol. 182 (2020–2021 / published PDF 2022). https://www.academie-sciences-lettres-toulouse.fr/wp-content/uploads/2023/02/2022_Fermat.pdf"
    url: "https://www.academie-sciences-lettres-toulouse.fr/wp-content/uploads/2023/02/2022_Fermat.pdf"
    accessed: 2026-10-24
    reliability_note: "Scholarly academy volume; introduction states religious ideas 'indubitablement inscrites dans le cadre de l'Église catholique' and ties tomb motto nesciri ama to Imitation of Christ. Full Laffont chapter 'Autour des idées religieuses' (HAL) was 403."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, childhood]
  - id: S9
    type: secondary
    kind: "other"
    author: "Musée des Augustins (Toulouse)"
    citation: "Musée des Augustins. 'Epitaphe de Pierre de Fermat' (RA 572), inscription transcription including 'Vis scire quiddam quod juvet? nesciri ama'. https://collections.augustins.toulouse.fr/fr/notice/ra-572-epitaphe-de-dom-petri-de-fermat-2e6a3a71-41ad-4b17-a4b9-f29e11881b22"
    url: "https://collections.augustins.toulouse.fr/fr/notice/ra-572-epitaphe-de-dom-petri-de-fermat-2e6a3a71-41ad-4b17-a4b9-f29e11881b22"
    accessed: 2026-10-24
    reliability_note: "Posthumous epitaph transcription; Christian maxim from Imitation of Christ. Context for heritage/piety; not scored as A alone (funerary voice)."
    source_quality: "other"
    used_for: [review]
---

## Summary

Pierre de Fermat (1601–1665), French magistrate and mathematician [S1, S4]. Deepen D1: primary_system CHRIST (0.5); A 0 @0.7 (single, poem S6); B 3 @0.5 (corroborated S5+S1; alt 4); mid_basin BELOW_THRESHOLD. Chart-moving YES (A scored → plottable, faded hollow).

## Life and work

Beaumont-de-Lomagne; Parlement of Toulouse; Castres [S1, S4].

## Contribution and impact

Tangents 1638; lesser theorem 1640 [S3]; least time c. 1657 / letter 1 Jan 1662 [S1, S5].

## Childhood and education

Franciscan school; Orléans law [S1, S4]. Family reported devoutly Catholic; daughters in religious life, son archdeacon [S7].

## Adult working worldview

Poem *Cede Deo, seu Christus moriens*: yield to God; nature acknowledges God as parent; eternal Son took mortal flesh [S6]. Optics letter: nature always acts by the shortest / easiest ways, or least time [S5]. CHRIST @0.5; A 0; B 3 @0.5.

## Heritage (context only)

Roman Catholic family/schooling [S1, S7]. Not a code.

## Timing

1638–1657 (0.5), age 37; alt span end 1662 [S1, S5].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Christian transcendent God (poem) with lawful least-time nature (letter).

## Open questions

- Poem date; full Laffont chapter; Mahoney on religion.
- B 3 vs 4 under "tousjours".

## Research log

- 2026-10-24: Deepen D1. Opened DBNL 1662 letter (S5), Wikisource poem (S6), Wikipedia (S4), SCS (S7), Académie/Laffont PDF (S8), Augustins epitaph (S9). B firmed; A scored; CHRIST @0.5. No figures/; no fallacy_catalog.
- 2026-10-20: AA8–AA10 audit fixes (span, birth, lesser theorem).
- 2026-10-19: Read Britannica (Boyer, scholars edition).
