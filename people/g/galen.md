---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch P; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-18
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-18, by: "Grok Bot", summary: "Record created (stage 3 batch P, order P32: F 4, rank 97). Basics from Britannica (Vivian Nutton, signed; body only) and SEP 'Galen' (P. N. Singer, 2021). Worldview from De usu partium XI.14 (written 169–176), in R. Walzer's translation (Galen on Jews and Christians, 1949) as reproduced on Roger Pearse's page, with his remarks on the 'undemonstrated laws' of the followers of Moses and Christ; secondary quotations, primary check pending. Scientist (P30). primary_system PLATO (0.5, alt HELLEN); A 1 (0.5, alt 2); B 3 (0.5, alt 4); D 4 (0.5, alt 3); mid_basin BELOW_THRESHOLD. Plotted (faded). Draft, not reviewed."}
    - {date: 2026-10-18, by: "Grok Bot", summary: "Batch P audit notes applied (gs_08be43b_P run 1: 39 hold, 6 weaken; no Galen weakens). Britannica byline now 'Vivian Nutton and Britannica Editors' (note 6); Pearse's inserted '( καὶ )' restored in the De usu partium XI.14 quotation (note 7). Ruling P2 (v8's pick on the auditor's advice): B stays 3 at 0.5, alternative 4. Values unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #96, F4 rank 97). Needs: A 1@0.5 alt 2; B 3@0.5 alt 4; primary PLATO@0.5 alt HELLEN; mid BELOW; plotted faded; scientist (P30). UP XI.14 primary check: Flemming 2017 (S5) quotes Helmreich II 158.19–159.3 Greek (ἀδύνατα φύσει; God chooses τὸ βέλτιστον among δυνατῶν γενέσθαι) with English matching Walzer (S3); SEP Singer §5.2 (S2) independently discusses the Moses contrast and Craftsman + material limitation. May 1968 IA borrow-restricted; Helmreich PDF downloaded but OCR garbled — Greek verified via Flemming's citation of the critical edition. Dual bio: Britannica (S1) + Wikipedia EN (S6) (P50). P47 source_quality on S1–S6. A 1 → 0.7 corroborated (S2+S3+S5); B 3 → 0.7 corroborated (S2+S3+S5), alt 4 kept (Asclepius interventions, Ruling P2 / P40 'certain things' limited scope). primary_system PLATO → 0.7 alt HELLEN. mid_basin BELOW → true @0.7. Chart-moving YES: faded→dark and hollow→filled. No fallacy_catalog. Draft, not reviewed."}

identity:
  id: galen
  display_name: "Galen"
  roster:
    canonical_name: "Galen"
    rank: 97
    F: 4
    models: [Claude, DeepSeek, Gemini, GPT]
    band: "core (3–4)"
    status: core
    field: medicine
    field_bucket: medicine
  full_name: {value: "Galen of Pergamum", certainty: 0.7, cites: [{source: S1, locator: "image caption ('Galen of Pergamum')"}, {source: S6, locator: "lead (Galen of Pergamon)"}], how_known: "Britannica and Wikipedia agree (P15 dual bio)."}
  native_name: {value: "Galēnos", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "SEP gives the Greek name."}
  aliases:
    - {name: "Galenus", kind: latinized}

basics:
  birth:
    date: {value: "129", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "§1"}], how_known: "Britannica and SEP agree on 129 CE."}
    place: {value: "Pergamum, Mysia, Anatolia", modern_name: "Bergama, Türkiye", polity_then: "Roman Empire (province of Asia)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "216", calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Britannica 'c. 216'; SEP gives 'c. 200' (S2). 0.5 for the disagreement."}
    place: {value: UNKNOWN, how_known: "Not given in the body texts read."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "The listed contributions are undated in the sources read (P39). SEP says he ascribes 'the writing-up of a large number of his major works in scientific and medical theory' to 169–76 (S2), which is a span for writing up, not the date of a contribution."}
  era_bucket: {value: "-500 to 499", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Every adult year (from c. 145 to c. 200 or 216) falls in this bucket (P39)."}
  region_of_birth: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Türkiye (P3: M49 Western Asia)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "Rome paragraph"}], how_known: "Rome from 162 (Italy)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Ancient Greek"], certainty: 0.7, cites: [{source: S1, locator: "Influence section (Greek manuscripts)"}], how_known: "Britannica."}
  occupations: {value: ["physician", "anatomist", "philosopher", "writer"], certainty: 0.7, cites: [{source: S1, locator: "opening; anatomy section"}], how_known: "Britannica."}

contribution:
  fields: {value: ["anatomy", "physiology", "medicine", "logic"], certainty: 0.7, cites: [{source: S1, locator: "anatomy section"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Demonstration that the arteries carry blood, not air", year: UNKNOWN, kind: discovery, lasting: "'One of his most important demonstrations' (S1)", certainty: 0.7, cites: [{source: S1, locator: "anatomy section"}], how_known: "Britannica; undated. A result about natural systems, so he is a scientist (P30)."}
    - {value: "Vivisection experiments on nerve and organ function (recurrent laryngeal nerve, spinal cord transections, ureters)", year: UNKNOWN, kind: method, lasting: "'Notable also were his vivisection experiments' (S1)", certainty: 0.7, cites: [{source: S1, locator: "anatomy section"}], how_known: "Britannica; undated."}
    - {value: "Galenic physiology and humoral pathology (imbalances located in specific organs)", year: UNKNOWN, kind: theory, lasting: "'a powerful influence in medicine for the next 1,400 years' (S1)", certainty: 0.7, cites: [{source: S1, locator: "physiology paragraphs"}], how_known: "Britannica; undated."}
  evidence_of_impact:
    - {value: "Dominant influence on medicine in Europe to the mid-17th century and in the Byzantine and Muslim worlds", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening; Influence section"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father a wealthy architect, who died in 149", role: father, certainty: 0.7, cites: [{source: S1, locator: "Early life paragraph"}, {source: S2, locator: "§1"}], how_known: "Britannica; year from SEP."}
  household_circumstances: {value: "Wealthy family of the Pergamene elite", certainty: 0.7, cites: [{source: S1, locator: "Early life paragraph"}, {source: S2, locator: "§1"}], how_known: "Britannica and SEP."}
  schooling:
    - {value: "Educated as a philosopher and man of letters; mathematics and geometry", stage: home, years: UNKNOWN, certainty: 0.5, cites: [{source: S1, locator: "Early life paragraph"}, {source: S2, locator: "§1"}], how_known: "Britannica and SEP; the stage label is the coder's."}
    - {value: "Medical study at Pergamum, Smyrna and Alexandria, from age 16", stage: other, years: "c. 145–157", certainty: 0.5, cites: [{source: S1, locator: "Early life paragraph"}], how_known: "Britannica ('more than a decade of study', return in 157)."}
  early_mathematics: {value: "geometry (Euclid-style proof)", certainty: 0.5, cites: [{source: S2, locator: "§1"}], how_known: "SEP: he 'lays great stress on his own early education in mathematics and geometry'."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["Ancient Greek"], certainty: 0.5, cites: [{source: S2, locator: "§1"}], how_known: "'the culturally Greek city of Pergamon' (S2)."}
  notable_events:
    - {value: "Changed his career to medicine at 16", year: 145, certainty: 0.5, cites: [{source: S1, locator: "Early life paragraph"}], how_known: "Britannica; year computed by the coder."}

worldview:
  unit: "adult working worldview"
  working_years: {value: UNKNOWN, how_known: "Equals timing.major_work_period (UNKNOWN, P39)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "He and 'the other Greeks who follow the right method in natural science' hold that 'certain things are impossible by nature', against Moses' view that 'everything [is] possible with God'", certainty: 0.7, cites: [{source: S3, locator: "Reference 2"}, {source: S5, locator: "UP 11.14 Helmreich II 158.19–159.3"}, {source: S2, locator: "§5.2"}], how_known: "UP XI.14: Walzer (S3) matched to Helmreich Greek via Flemming (S5); SEP §5.2 (S2)."}
  primary_system:
    value: PLATO
    basis: written_profession
    certainty: 0.7
    cites: [{source: S3, locator: "Reference 2"}, {source: S5, locator: "UP 11.14 Greek + English"}, {source: S2, locator: "§5.2 (teleology); §9 (theology)"}]
    rationale: "He names his own view as 'our own opinion and that of Plato and of the other Greeks': a divine craftsman (demiurge) who chooses the best but works within what matter allows. SEP calls it his '(Platonic) view' and reads UP as speaking 'interchangeably of the purposive force of Nature (phusis) and of the Platonic Craftsman'. Named alternative: HELLEN (SEP: he claims personal experience of interventions by Asclepius)."
    how_known: "Own written profession in UP XI.14 (Walzer + Helmreich Greek via Flemming) with SEP; 0.7 with an alternative named (§3)."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: PLATO, reason: "Self-identified Platonic craftsman theology."}
    - {code: HELLEN, reason: "Asclepius' interventions (S2)."}
    - {code: ARIST, reason: "UP's teleology is 'explicitly inspired by Aristotle' (S2); the theology is Platonic."}
  lio_axes:
    A_locus:
      value: 1
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S3, locator: "Reference 2 (De usu partium XI.14)"}, {source: S5, locator: "UP 11.14 Helmreich II 158.19–159.3"}, {source: S2, locator: "§5.2; §9"}]
      rationale: "A maker distinct from his material: 'the principle of the demiurge as the origin of every created thing', and 'God is the cause both of the choice of the best in the products of creation themselves and of the selection of the matter' (UP XI.14). Helmreich Greek (via S5): God chooses ἐκ τῶν δυνατῶν γενέσθαι τὸ βέλτιστον; matter constrains. Named alternative 2: SEP notes he speaks interchangeably of Nature and the Craftsman, and is 'not able to be specific about the nature or identity of this divine intelligence'. Compare Plato's record (A 1)."
      how_known: "Own written profession; Walzer English (S3) corroborated by Helmreich Greek via Flemming (S5) and SEP §5.2 (S2); secondary/web copies → 0.7 (§7). Distinct source ids → corroborated (P48)."
      alternatives:
        - {value: 2, note: "Nature and the Craftsman used interchangeably (S2).", cites: [{source: S2, locator: "§5.2; §9"}]}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S3, locator: "Reference 2 (De usu partium XI.14)"}, {source: S5, locator: "UP 11.14 Helmreich II 158.19–159.3"}, {source: S2, locator: "§5.2; §9"}]
      rationale: "Account of nature (P6 / P16): 'we say that certain things are impossible by nature and that God does not even attempt such things at all but that he chooses the best out of the possibilities of becoming'; Greek ἀδύνατα φύσει and τούτοις μηδ' ἐπιχειρεῖν ὅλως τὸν θεόν (S5). A lawful nature that binds even God, but limited to 'certain things', not a stated no-exception claim (P40); SEP reports 'personal experience of interventions by individual gods ... most notably by Asclepius', a stated, limited exception. So B 3, alternative 4 (Ruling P2). As a scientist (P30), working science alone would give the same (P35)."
      how_known: "Own written profession; Walzer (S3) + Helmreich Greek via Flemming (S5) + SEP (S2); Asclepius exception still from SEP summary (Pietrobelli 2013 / Singer 2019a unread). Cap 0.7 (§7). Distinct source ids → corroborated (P48)."
      alternatives:
        - {value: 4, note: "If the Asclepius episodes are read as within nature, nothing excepts nature's limits.", cites: [{source: S3, locator: "Reference 2"}, {source: S2, locator: "§9"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read."}
    D_authority:
      value: 4
      basis: written_profession
      certainty: 0.5
      cites: [{source: S3, locator: "References 1, 4, 5"}, {source: S5, locator: "Diff. Puls. 2.4 / 8.579 K (Greek)"}]
      rationale: "Demonstration over undemonstrated authority: he mocks hearing 'talk of undemonstrated laws' as 'in the school of Moses and Christ' (De differentiis pulsuum ii.4; Greek in S5), and the followers of Moses and Christ who 'order them to accept everything on faith' (On the Prime Mover, Arabic quotation). Named alternative 3: his reported personal experience of Asclepius (S2) may give religion a limited say. Coder's reading."
      how_known: "Walzer via Pearse plus Flemming's Greek Diff. Puls. cite; one passage still Arabic-only; Asclepius unread in Galen's own words → 0.5."
      alternatives:
        - {value: 3, note: "Asclepius (S2).", cites: [{source: S2, locator: "§9"}]}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: true, certainty: 0.7, cites: [{source: S3, locator: "Reference 2"}, {source: S5, locator: "UP 11.14 Helmreich II 158.19–159.3"}, {source: S2, locator: "§5.2"}], how_known: "P4/P6 test: A 1 (≤ 1) at 0.7 and B 3 (≥ 3) at 0.7, both corroborated (P48); B scored on his account of nature (P16). Named alternatives (A 2, B 4) still meet the branches. Certainty 0.7: lower of A and B. Chart-moving this pass: faded→dark and hollow→filled."}
  statements:
    - text: "It is precisely ( καὶ ) this point in which our own opinion and that of Plato and of the other Greeks who follow the right method in natural science differs from the position taken up by Moses. For the latter it seems enough to say that God simply willed the arrangement of matter and it was presently arranged in due order; for he believes everything to be possible with God, even should He wish to make a bull or a horse out of ashes. We however do not hold this; we say that certain things are impossible by nature and that God does not even attempt such things at all but that he chooses the best out of the possibilities of becoming."
      cites: [{source: S3, locator: "Reference 2 (De usu partium XI.14)"}, {source: S5, locator: "UP 11.14 Helmreich II 158.19–159.3"}]
      context: "De usu partium XI.14, on the eyelashes; written 169–176 per De libris propriis (S3; SEP also puts the writing-up of his major works in 169–76). No single year, so the date field is left out."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Walzer English (S3) matched to Flemming's quotation of Helmreich Greek II 158.19–159.3 (S5); May 1968 not opened (IA borrow-restricted)."
    - text: "We say thus that God is the cause both of the choice of the best in the products of creation themselves and of the selection of the matter."
      cites: [{source: S3, locator: "Reference 2 (De usu partium XI.14)"}, {source: S5, locator: "UP 11.14 (same chapter sequence)"}]
      context: "Same passage."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "As above."
    - text: "καὶ τοῦτ' ἔστι, καθ' ὃ τῆς Μωσοῦ δόξης ἥ θ' ἡμετέρα καὶ ἡ Πλάτωνος καὶ ἡ τῶν ἄλλων τῶν παρ' Ἕλλησιν ὀρθῶς μεταχειρισαμένων τοὺς περὶ φύσεως λόγους διαφέρει. τῷ μὲν γὰρ ἀρκεῖ τὸ βουληθῆναι τὸν θεὸν κοσμῆσαι τὴν ὕλην, ἡ δ' εὐθὺς κεκόσμηται πάντα γὰρ εἶναι νομίζει τῷ θεῷ δυνατά, κἂν εἰ τὴν τέφραν ἵππον ἢ βοῦν ἐθέλοι ποιεῖν. ἡμεῖς δ' οὐχ οὕτω γιγνώσκομεν, ἀλλ' εἶναι γάρ τινα λέγομεν ἀδύνατα φύσει καὶ τούτοις μηδ' ἐπιχειρεῖν ὅλως τὸν θεόν, ἀλλ' ἐκ τῶν δυνατῶν γενέσθαι τὸ βέλτιστον αἱρεῖσθαι."
      cites: [{source: S5, locator: "UP 11.14: Helmreich 1968, II 158.19–159.3"}]
      context: "Greek of the Moses contrast in UP XI.14, as printed by Flemming from Helmreich."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Critical-edition Greek; confirms Walzer's English on ἀδύνατα φύσει and choice of τὸ βέλτιστον among δυνατῶν γενέσθαι."
    - text: "in order that one should not at the very beginning, as if one had come into the school of Moses and Christ, hear talk of undemonstrated laws, and that where it is least appropriate."
      cites: [{source: S3, locator: "Reference 4 (De differentiis pulsuum ii.4)"}, {source: S5, locator: "Diff. Puls. 2.4: 8.579 K"}]
      context: "De differentiis pulsuum ii.4 (dated by Pearse to 176–192), Walzer's translation (S3); Greek cited by Flemming (S5)."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Greek preserved; Flemming quotes ὡς εἰς Μωϋσοῦ καὶ Χριστοῦ διατριβὴν … νόμων ἀναποδείκτων."
  changes_over_life: []
  coder_notes: "Deepen D1: craftsman-limited-by-matter (A 1 / B 3) now at 0.7 corroborated from UP XI.14 (Walzer + Helmreich Greek via Flemming + SEP §5.2). Asclepius exception still from SEP summary only — keeps B alt 4 and D alt 3; Pietrobelli 2013 / Singer 2019a unread. Death year c. 216 (Britannica) against c. 200 (SEP); Wikipedia gives c. 129–216."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Greek, of Pergamum's elite", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "No dated listed lasting contribution (P39)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "No dated listed lasting contribution (P39)."}
  first_evidence_of_lio_type_views: {value: "169–176: De usu partium XI.14 on God and the limits of nature", year: 169, certainty: 0.7, cites: [{source: S3, locator: "Reference 2"}, {source: S5, locator: "UP 11.14"}], how_known: "Start of the writing span; earlier works not read (P30 #7)."}
  lio_views_relative_to_major_work: {value: "unclear", rationale: "The major-work period is UNKNOWN (P39).", certainty: 0.5, cites: [{source: S3, locator: "Reference 2"}], how_known: "Coder's reading."}
  worldview_during_major_work: {value: "Platonic craftsman theology limited by matter (UP, 169–176)", certainty: 0.7, cites: [{source: S3, locator: "Reference 2"}, {source: S5, locator: "UP 11.14"}], how_known: "His text in Walzer + Helmreich Greek via Flemming."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "He took geometry as his model of secure proof (S2).", certainty: 0.5, cites: [{source: S2, locator: "§1"}], how_known: "Coder's reading."}
  form_acquired: {value: "childhood or adolescence", certainty: 0.5, cites: [{source: S2, locator: "§1"}], how_known: "Early education in mathematics and geometry (S2)."}
  circle_present: {value: "partly", rationale: "God acts within nature's possibilities.", certainty: 0.7, cites: [{source: S3, locator: "Reference 2"}, {source: S5, locator: "UP 11.14"}], how_known: "Coder's reading of UP XI.14."}
  reading: "A craftsman god who chooses the best among nature's possibilities."
  notes: "Deepen D1: A 1 and B 3 both 0.7 corroborated; mid_basin true; chart dark filled."

institutions:
  - {value: "Gladiators of the high priest of Asia, Pergamum", role: "chief physician", years: "157–", kind: employer, certainty: 0.7, cites: [{source: S1, locator: "Early life paragraph"}], how_known: "Britannica."}
  - {value: "Imperial court, Rome", role: "court physician to Marcus Aurelius and his successors", years: UNKNOWN, kind: "government or state body", certainty: 0.5, cites: [{source: S2, locator: "§1"}], how_known: "SEP ('Adopted as court physician by the emperor Marcus Aurelius')."}
collaborators:
  - {value: "Hippocrates", relation: "influenced by", note: "'the fount of all medical learning' for Galen", certainty: 0.7, cites: [{source: S1, locator: "physiology paragraph"}], how_known: "Britannica."}
  - {value: "Eudemus", relation: teacher, note: "his old philosophy teacher", certainty: 0.7, cites: [{source: S1, locator: "Rome paragraph"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 97"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Death year disputed (c. 216 Britannica / Wikipedia; c. 200 SEP)."
    - "May 1968 English translation of UP not opened (IA borrow-restricted); Greek verified via Flemming's Helmreich citation."
    - "Asclepius interventions still from SEP summary; Pietrobelli 2013 / Singer 2019a unread."
  open_questions:
    - "Open May 1968 (Cornell) for English of UP XI.14 beside Walzer."
    - "Read Galen's own accounts of Asclepius' interventions (B alt 4, D alt 3)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Vivian Nutton and Britannica Editors"
    citation: "Nutton, Vivian, and Britannica Editors. \"Galen.\" Encyclopaedia Britannica (revised 1 September 2026). https://www.britannica.com/biography/Galen. Read live 2026-10-18 (the Wayback Machine was rate-limiting)."
    url: "https://www.britannica.com/biography/Galen"
    accessed: 2026-10-18
    source_quality: "reference entry"
    reliability_note: "Signed article. Body only; the AI-generated Top Questions and Quick Facts are not cited."
    used_for: [identity, basics, contribution, childhood, institutions, collaborators]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "P. N. Singer"
    citation: "Singer, P. N. \"Galen.\" Stanford Encyclopedia of Philosophy (substantive revision 3 December 2021). https://plato.stanford.edu/entries/galen/"
    url: "https://plato.stanford.edu/entries/galen/"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Signed SEP entry, re-read deepen D1 (§5.2 teleology/Moses; §9 theology/Asclepius)."
    used_for: [identity, basics, childhood, worldview, heritage, lane_b, institutions]
  - id: S3
    type: secondary
    kind: other
    author: "Roger Pearse (reproducing R. Walzer)"
    citation: "Pearse, Roger. \"Galen on Jews and Christians\" (2011), reproducing R. Walzer's translations from Galen on Jews and Christians (Oxford: Oxford University Press, 1949). https://www.tertullian.org/rpearse/galen_on_jews_and_christians.htm"
    url: "https://www.tertullian.org/rpearse/galen_on_jews_and_christians.htm"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Personal web page reproducing a scholarly translation; UP XI.14 English corroborated against Helmreich Greek via S5."
    used_for: [worldview, timing, lane_b]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-18
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [identity, review]
  - id: S5
    type: secondary
    kind: book chapter
    author: "Rebecca Flemming"
    citation: "Flemming, Rebecca. \"Galen and the Christians.\" In Christianity in the Second Century: Themes and Developments, ed. James Carleton Paget and Judith Lieu, 171–187. Cambridge: Cambridge University Press, 2017. https://www.cambridge.org/core/books/christianity-in-the-second-century/galen-and-the-christians/B8100C10D0EB22543AD835BFB6592A3A. Quotes UP 11.14 Helmreich II 158.19–159.3 Greek and Diff. Puls. 2.4 / 8.579 K."
    url: "https://www.cambridge.org/core/books/christianity-in-the-second-century/galen-and-the-christians/B8100C10D0EB22543AD835BFB6592A3A"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Peer-reviewed CUP chapter quoting Helmreich's critical Greek of UP XI.14 and Kühn for Diff. Puls.; used to primary-check Walzer."
    used_for: [worldview, timing, lane_b]
  - id: S6
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. \"Galen.\" Wikipedia. https://en.wikipedia.org/wiki/Galen. Dual bio (P50). Read 2026-10-24."
    url: "https://en.wikipedia.org/wiki/Galen"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Used for dual-bio basics (Aelius/Claudius Galenus; c. 129–216). Worldview coding rests on S2/S3/S5, not Wikipedia."
    used_for: [identity, basics]
---

# Galen

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Galen (129–c. 216), Greek physician of Pergamum and Rome [S1; S2; S6]. Deepen D1: primary_system PLATO (0.7, alt HELLEN); A 1 at 0.7 corroborated (alt 2); B 3 at 0.7 corroborated (alt 4); D 4 at 0.5 (alt 3); mid_basin true at 0.7. Plotted (dark, filled). Chart-moving YES this pass.

## Life and work

Pergamum, Smyrna, Alexandria; Rome from 162 [S1; S6].

## Contribution and impact

Arteries carry blood; vivisection; humoral physiology [S1].

## Childhood and education

Son of a wealthy architect; geometry [S1; S2].

## Adult working worldview

Craftsman theology limited by matter: 'certain things are impossible by nature and ... God does not even attempt such things' (UP XI.14) [S3; S5; S2 §5.2]. Asclepius interventions keep B alt 4 [S2 §9].

## Heritage (context only)

Greek [S2].

## Timing

Undated lasting contributions (P39); UP writing-up 169–176 [S2; S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Geometry as model [S2]. Craftsman within nature's possibilities [S3; S5].

## Open questions

- May 1968 English of UP XI.14.
- Galen's own Asclepius accounts (Pietrobelli 2013; Singer 2019a).

## Research log

- 2026-10-18: Read Britannica (live), SEP and Pearse's page of Walzer's translations directly.
- 2026-10-24 deepen D1: Flemming 2017 CUP chapter (Helmreich Greek UP XI.14); SEP §5.2 re-read; Wikipedia dual bio; May IA borrow-restricted; Helmreich PDF OCR garbled.
