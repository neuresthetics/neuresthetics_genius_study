---
record:
  record_type: person
  schema_version: "1.1"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (overnight agent run for Jason, first pool)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages and translations"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created. Basics, contribution, childhood, worldview (CLASS_THEISM at 1.0) and all five LIO axes filled from Horten's 1907 German translation of the Metaphysics of The Cure, Arberry's translation of the Autobiography (paraphrase only), two SEP entries, IEP, Britannica and MacTutor. mid_basin true under P4. Not reviewed."}

identity:
  id: ibn-sina
  display_name: "Ibn Sina (Avicenna)"
  roster:
    canonical_name: "Ibn Sina (Avicenna)"
    rank: 39
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: polymath
    field_bucket: polymath
  full_name: {value: "Abū ʿAlī al-Ḥusayn ibn ʿAbd Allāh ibn Sīnā", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts ('In full')"}, {source: S2, locator: "opening paragraph"}, {source: S4, locator: "opening paragraph"}], how_known: "Three sources agree, with small differences of transliteration."}
  native_name: {value: "Ibn Sīnā (Arabic)", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts ('Arabic')"}], how_known: "Britannica gives the Arabic form; 'Avicenna' is the Latin form (S4)."}
  aliases:
    - {name: "Avicenna", kind: latinized}
    - {name: "Ibn Sina", kind: "roster alias"}
    - {name: "Ibn Sina - Avicenna", kind: "roster alias"}
    - {name: "Sina-Ibn", kind: "roster alias"}
    - {name: "al-Shaykh al-Raʾīs (The Preeminent Master)", kind: "title or honorific"}

basics:
  birth:
    date:
      value: "980"
      approx: true
      calendar: gregorian
      certainty: 0.5
      cites: [{source: S1, locator: "Quick Facts; opening sentence"}, {source: S4, locator: "§1 ('in around 980')"}, {source: S5, locator: "Quick Info"}, {source: S8, locator: "opening sentence (980–1037)"}]
      how_known: "Four sources give 980, but SEP's main entry (Gutas) says the year cannot be fixed. The sources disagree by up to 16 years, so 0.5."
      alternatives:
        - {value: "970", cites: [{source: S2, locator: "opening paragraph ('ca. 970–1037'); §1.1"}], note: "Gutas: 'some time in the 70s of the tenth century, perhaps as early as 964'."}
    place:
      value: "Afshana, a village near Bukhara"
      modern_name: "Afshana, near Bukhara, Uzbekistan"
      polity_then: "Samanid realm (Transoxania)"
      certainty: 1.0
      cites: [{source: S2, locator: "§1.1"}, {source: S4, locator: "§1"}, {source: S7, locator: "Autobiography, p. 9"}]
      how_known: "Three sources, including his own account. MacTutor names Kharmaithen, the district his father governed (S5); Afshana lies next to it (S7)."
  death:
    date: {value: "1037", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts; Life and education (in Ramadan)"}, {source: S2, locator: "§1.1"}, {source: S5, locator: "Quick Info (June 1037)"}], how_known: "All sources agree on 1037; MacTutor gives June, Britannica the month of Ramadan."}
    place:
      value: "Hamadan"
      modern_name: "Hamadan, Iran"
      polity_then: "Kakuyid and Buyid lands (western Iran)"
      certainty: 1.0
      cites: [{source: S2, locator: "§1.1"}, {source: S1, locator: "Quick Facts"}, {source: S5, locator: "Quick Info"}]
      how_known: "Three sources. He fell ill on a campaign with ʿAlāʾ al-Dawla (S1, S4)."
  first_lasting_contribution_year: {value: 1016, approx: true, certainty: 0.5, cites: [{source: S4, locator: "§2 (The Cure solicited in Hamadan in 1016, completed in Isfahan by 1027)"}, {source: S5, locator: "Biography (Cure and Canon begun at Hamadan)"}], how_known: "Year The Cure was begun, per IEP. The Canon was also begun at Hamadan (S5) but no source read dates it. His earliest works (Compendium on the Soul, about age 18) are not counted as lasting. Approximate and from one source, so 0.5."}
  era_bucket: {value: "500 to 1399", certainty: 1.0, cites: [{source: S4, locator: "§2"}], how_known: "From first_lasting_contribution_year under the era buckets (decision P2). Any date in his career gives the same bucket."}
  region_of_birth: {value: "Central Asia", certainty: 1.0, cites: [{source: S5, locator: "Quick Info ('now Uzbekistan')"}, {source: S1, locator: "Quick Facts ('now in Uzbekistan')"}], how_known: "Uzbekistan is Central Asia in data/reference/regions.csv (UN M49 sub-region, decision P3)."}
  region_of_work: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S2, locator: "§1.1"}, {source: S4, locator: "§1"}], how_known: "He worked in Bukhara and Gurganj (Central Asia) until about 1012, then in Jurjan, Rayy, Hamadan and Isfahan. The Cure and the Canon were written in Hamadan and Isfahan, in Iran, which the study places in MENA (regions.csv, exception P3). Central Asia is an alternative for the early years, so 0.7."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S2, locator: "§1.1"}], how_known: "As the sources record it."}
  languages_of_work: {value: [Arabic, Persian], certainty: 1.0, cites: [{source: S4, locator: "§1; §2 (the Persian Book of Knowledge)"}, {source: S2, locator: "§1.2"}], how_known: "Most works in Arabic; at least one summa in Persian."}
  occupations:
    value: [physician, philosopher, "court official and vizier", "political counsellor"]
    certainty: 1.0
    cites: [{source: S1, locator: "Top Questions; Life and education"}, {source: S2, locator: "§1.1"}, {source: S4, locator: "§1"}, {source: S5, locator: "Biography"}]
    how_known: "Four sources agree."

contribution:
  fields: {value: [philosophy, metaphysics, logic, medicine, psychology, "natural philosophy", astronomy, mathematics], certainty: 1.0, cites: [{source: S1, locator: "opening paragraph; Influence in philosophy and science"}, {source: S5, locator: "Biography"}, {source: S2, locator: "§1.2"}], how_known: "Three sources agree."}
  lasting_original_contributions:
    - {value: "The Cure (al-Shifāʾ): an encyclopaedic summa of logic, natural science, mathematics and metaphysics", year: "1016–1027", kind: work, lasting: "translated into Latin in the 12th–13th centuries; shaped scholasticism (S4)", certainty: 1.0, cites: [{source: S4, locator: "§2; §3"}, {source: S1, locator: "Influence in philosophy and science"}, {source: S2, locator: "§1.2"}], how_known: "Three sources."}
    - {value: "The Canon of Medicine (al-Qānūn fī al-ṭibb)", kind: work, lasting: "basis of medical teaching in European universities until the 17th century", certainty: 1.0, cites: [{source: S2, locator: "opening paragraph"}, {source: S1, locator: "Influence in medicine"}, {source: S5, locator: "Biography"}], how_known: "Three sources. Not dated in the sources read beyond 'begun at Hamadan' (S5)."}
    - {value: "The distinction between necessary and possible existence, with God as the Necessary Existent and the existence of the world from it", kind: theory, lasting: "foundation for later Islamic philosophy and theology and for Latin metaphysics (S4)", certainty: 1.0, cites: [{source: S3, locator: "§3; §4.1–4.2"}, {source: S4, locator: "opening paragraph; §5"}], how_known: "Two reference sources."}
    - {value: "The 'flying man' argument for the soul's awareness of itself", kind: "concept or term", lasting: "compared to Descartes' cogito (S4)", certainty: 0.7, cites: [{source: S4, locator: "§7"}], how_known: "One source."}
  evidence_of_impact:
    - {value: "Called 'The Preeminent Master' (al-shaykh al-raʾīs) in the Islamic world; SEP ranks his influence on intellectual history in the West (of India) second only to Aristotle", kind: "scholarly consensus", certainty: 1.0, cites: [{source: S2, locator: "opening paragraph"}], how_known: "SEP (Gutas)."}
    - {value: "al-Ghazali and al-Shahrastani attacked him as the main representative of philosophy in Islam; his metaphysics became the foundation for later Islamic philosophical theology", kind: "assessment by a later major figure", certainty: 1.0, cites: [{source: S4, locator: "opening paragraph; §9"}], how_known: "IEP."}
    - {value: "Latin translations guided the 13th-century reception of Aristotle, notably in Albertus Magnus and Thomas Aquinas", kind: "institutional or technological lineage", certainty: 1.0, cites: [{source: S1, locator: "Top Questions"}, {source: S4, locator: "§3"}], how_known: "Two sources."}
  major_works:
    - {value: "Compendium on the Soul (Maqāla fī l-nafs), his first work", year: "c. 998", kind: book, certainty: 0.5, cites: [{source: S2, locator: "§1.1"}, {source: S4, locator: "§2"}], how_known: "Written shortly after age 18 (S2); the year depends on the birth year."}
    - {value: "The Cure (al-Shifāʾ)", year: "1016–1027", kind: book, certainty: 1.0, cites: [{source: S4, locator: "§2"}, {source: S2, locator: "§1.1"}], how_known: "Two sources."}
    - {value: "The Canon of Medicine (al-Qānūn fī al-ṭibb)", kind: book, certainty: 1.0, cites: [{source: S1, locator: "Influence in medicine"}, {source: S5, locator: "Biography"}], how_known: "Two sources; undated in them."}
    - {value: "The Salvation (al-Najāt), an epitome of The Cure", kind: book, certainty: 1.0, cites: [{source: S4, locator: "§2"}, {source: S2, locator: "§1.2"}], how_known: "Two sources."}
    - {value: "Book of Knowledge for ʿAlāʾ al-Dawla (Dānishnāma-yi ʿAlāʾī), in Persian", kind: book, certainty: 1.0, cites: [{source: S4, locator: "§1; §2"}, {source: S1, locator: "Life and education"}], how_known: "Two sources."}
    - {value: "Pointers and Reminders (al-Ishārāt wa-l-tanbīhāt)", year: "1030s or earlier (disputed)", kind: book, certainty: 0.7, cites: [{source: S4, locator: "§2"}], how_known: "IEP reports Gutas (early 1030s, Isfahan) and Michot (earlier, Hamadan)."}
  honours: [{value: UNKNOWN, how_known: "No formal honours are recorded in the sources read. He held court posts, including vizier at Hamadan (S4, S5); those are under occupations and institutions."}]
  definition_fit: {value: "clearly meets", rationale: "The Canon was a standard medical text for six centuries; The Cure shaped both Islamic and Latin philosophy; SEP ranks his influence second only to Aristotle's.", certainty: 1.0, cites: [{source: S2, locator: "opening paragraph"}, {source: S1, locator: "Influence in medicine"}], how_known: "Lane A definition applied to the contributions above."}

childhood:
  family_religion: {value: "Muslim. His father, and his brother too, had listened to the Ismaʿili missionaries of the Egyptian (Fatimid) movement and discussed their teaching at home; Ibn Sina says he listened but did not assent.", certainty: 0.7, cites: [{source: S7, locator: "Autobiography, p. 9"}, {source: S4, locator: "§1 ('His father, who may have been Ismaili')"}], how_known: "His own account (Arberry's translation, read in a poor OCR scan, so paraphrased) and one reference source, which hedges. The family's wider practice is not described."}
  family_religious_practice: {value: "Put under teachers of the Qurʾān and of letters at Bukhara; had mastered the Qurʾān by about age 10. The father and brother discussed Ismaʿili teaching on the soul and the intellect at home.", certainty: 0.7, cites: [{source: S7, locator: "Autobiography, p. 9"}, {source: S1, locator: "Life and education"}, {source: S5, locator: "Biography"}], how_known: "His own account plus two reference sources on the Qurʾān by age 10. Paraphrase only."}
  parents_and_household:
    - {value: "Father from Balkh who moved to Bukhara and served the Samanids as governor of the village district of Kharmaythan; he married Ibn Sina's mother at Afshana nearby. The father died before Ibn Sina left Bukhara.", role: parents, certainty: 1.0, cites: [{source: S2, locator: "§1.1"}, {source: S7, locator: "Autobiography, p. 9"}, {source: S4, locator: "§1"}], how_known: "Three sources agree. The mother's name is not given in the sources read."}
    - {value: "One younger brother, born after him at Afshana", role: sibling, certainty: 0.7, cites: [{source: S7, locator: "Autobiography, p. 9"}], how_known: "His own account only."}
  household_circumstances: {value: "Family of a provincial state official in the Samanid administration; his father's house in Bukhara was a meeting place for learned men", certainty: 0.7, cites: [{source: S2, locator: "§1.1"}, {source: S5, locator: "Biography"}], how_known: "SEP on the father's post; MacTutor on the house as a meeting place."}
  schooling:
    - {value: "Teachers of the Qurʾān and of letters at Bukhara; the Qurʾān mastered by about age 10", stage: "religious school", institution: "teachers at Bukhara", years: "to c. 990", ages: "to c. 10", certainty: 1.0, cites: [{source: S1, locator: "Life and education"}, {source: S5, locator: "Biography"}, {source: S7, locator: "Autobiography, p. 9"}], how_known: "Three sources."}
    - {value: "Hanafi jurisprudence (fiqh) with Ismaʿil the Ascetic (Ismaʿil Zahid)", stage: tutor, institution: "Bukhara", ages: "c. 10–16", certainty: 0.7, cites: [{source: S4, locator: "§1"}, {source: S7, locator: "Autobiography, p. 9"}], how_known: "Two sources; ages approximate."}
    - {value: "Logic (Porphyry's Isagoge), the first figures of Euclid and the start of the Almagest with Abu ʿAbd Allah al-Natili, a philosopher who stayed in his father's house", stage: tutor, institution: "family house, Bukhara", ages: "c. 10–14", certainty: 0.7, cites: [{source: S7, locator: "Autobiography, pp. 9–10"}, {source: S1, locator: "Life and education"}], how_known: "His own account (paraphrased) and Britannica on al-Natili teaching logic. Ages approximate."}
    - {value: "Studied the rest of logic, natural science, mathematics, metaphysics and medicine on his own, and says he had mastered the sciences by 18", stage: "self-directed", years: "to c. 998", ages: "c. 14–18", certainty: 1.0, cites: [{source: S2, locator: "§1.1"}, {source: S7, locator: "Autobiography, pp. 10–11"}, {source: S1, locator: "Life and education"}], how_known: "Three sources. Gutas reads the Autobiography as making a philosophical point about self-study, so the account is shaped (S2, S4)."}
  early_mathematics: {value: "geometry (Euclid-style proof)", ages: "c. 10–16", description: "Learned Indian arithmetic from a vegetable seller; read the first five or six figures of Euclid with al-Natili and solved the rest of the book on his own; then worked through the geometrical figures of Ptolemy's Almagest.", certainty: 0.7, cites: [{source: S7, locator: "Autobiography, pp. 9–10"}, {source: S2, locator: "§1.1 (quadrivium studied by himself)"}], how_known: "His own account (Arberry's translation, paraphrased because the OCR is poor) and SEP. Ages are not given exactly."}
  early_geometric_style_reasoning: {value: "Euclid and logic as a boy; during the next eighteen months he set out the premises of each proof he examined in files and worked out what followed from them.", certainty: 0.7, cites: [{source: S7, locator: "Autobiography, p. 11"}], how_known: "His own account, paraphrased. Facts only; the Lane B reading is in lane_b."}
  early_science_exposure:
    - {value: "Studied medicine from about 13 and treated patients by 16; cured the Samanid ruler Nuh ibn Mansur and was given the royal library", year: "c. 993–997", age: "c. 13–17", certainty: 1.0, cites: [{source: S5, locator: "Biography"}, {source: S1, locator: "Life and education"}, {source: S2, locator: "§1.1"}], how_known: "Three sources."}
  key_early_reading:
    - {value: "Aristotle's Metaphysics, which he says he read forty times without understanding it until he bought al-Farabi's short book on its aims", age: "c. 17–18", certainty: 0.7, cites: [{source: S7, locator: "Autobiography, p. 12"}, {source: S4, locator: "§1"}, {source: S1, locator: "opening paragraph"}], how_known: "His own account (paraphrased) and two reference sources."}
  childhood_mentors:
    - {value: "Abu ʿAbd Allah al-Natili, who taught him logic, Euclid and the start of the Almagest", name: "al-Natili", years: "c. 990s", certainty: 0.7, cites: [{source: S7, locator: "Autobiography, pp. 9–10"}, {source: S1, locator: "Life and education"}], how_known: "Two sources."}
    - {value: "Ismaʿil the Ascetic, his teacher in jurisprudence", name: "Ismaʿil Zahid", certainty: 0.7, cites: [{source: S4, locator: "§1"}, {source: S7, locator: "Autobiography, p. 9"}], how_known: "Two sources."}
  languages_in_childhood: {value: [Persian, Arabic], certainty: 0.5, cites: [{source: S2, locator: "§1.1 (Samanid Persian revival with Arabic-Islamic culture)"}], how_known: "Arabic from Qurʾānic schooling; Persian from the Samanid setting. The sources do not state his home language, so 0.5."}
  notable_events:
    - {value: "Given use of the Samanid royal library after curing the ruler", age: "c. 17–18", certainty: 1.0, cites: [{source: S2, locator: "§1.1"}, {source: S1, locator: "Life and education"}, {source: S5, locator: "Biography"}], how_known: "Three sources."}
    - {value: "The Qarakhanids took Bukhara in 999; after his father's death he left, saying 'necessity' led him away", year: "999–c. 1000", age: "c. 19–20", certainty: 1.0, cites: [{source: S2, locator: "§1.1"}, {source: S4, locator: "§1"}], how_known: "Two sources."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "c. 998–1037", certainty: 0.7, cites: [{source: S2, locator: "§1.1"}], how_known: "From his first work at about 18 to his death. Start date depends on the birth year."}
  nominal_affiliations:
    - {value: "Muslim; trained in Hanafi jurisprudence and served as a jurist at Gurganj", years: "lifelong", role: "believer; jurist", certainty: 1.0, cites: [{source: S1, locator: "Top Questions ('Avicenna's religion was Islam')"}, {source: S4, locator: "§1"}, {source: S5, locator: "Biography"}], how_known: "Three sources. Britannica's Top Questions box is a summary feature; the IEP and MacTutor facts carry the claim."}
  self_described_science_religion_relation:
    value: "Philosophy is demonstrative science, and the prophet is a human of the highest intellect who knows the truths by their middle terms, not on authority. The prophet gives the many the law and teaches them about God and the afterlife in images and parables they can grasp; those fit for philosophy are invited to work out the truth by demonstration. The soul's bliss and misery after death can be proved; bodily resurrection cannot, and he accepts it on the authority of the religious law and the Prophet."
    certainty: 1.0
    cites: [{source: S6, locator: "IX, ch. 9 ('Zehntes Kapitel'), p. 633; X, ch. 2, pp. 664–666"}, {source: S2, locator: "§4"}]
    how_known: "His own Metaphysics of The Cure in Horten's German translation, and SEP's account with translated quotations. Paraphrase; quotations are in statements."
  primary_system:
    value: CLASS_THEISM
    basis: written_profession
    certainty: 1.0
    cites: [{source: S6, locator: "IX, ch. 8, pp. 617–618; X, ch. 1, pp. 656–657; X, ch. 2, p. 664"}, {source: S3, locator: "§4; §5; §6.1"}, {source: S9, locator: "§3"}]
    how_known: "His own main philosophical work (written profession) in a scholarly translation, so 1.0."
    rationale: "The coding guide defines CLASS_THEISM as the 'Aristotelian-Thomistic-Falsafa God: simple, immutable, known through reason'. Ibn Sina proves a Necessary Existent with no cause and no multiplicity (S3, §4), from which the world proceeds by emanation through a fixed order of intellects and causes (S3, §5.4; S6, IX ch. 8). He is named as a founder of the falsafa form in the CLASS_THEISM system record, and the founders rule applies. The ISLAM record's own guidance says to code falsafa as CLASS_THEISM, not ISLAM. Al-Ghazali judged three of his teachings (a world with no beginning in time, God's knowledge of universals only, no return of souls to bodies) to be against Islam and unbelief (S9, §3), which marks his working view as distinct from the confessed religion."
  secondary_system: {value: UNKNOWN, how_known: "No second system. His Qurʾān commentaries (S4) read revelation through his philosophy rather than adding a second system."}
  candidate_codes_considered:
    - {code: CLASS_THEISM, reason: "Chosen. Necessary Existent, simple and immutable; world by emanation through intermediate causes; providence as the order of the good; demonstration first.", cites: [{source: S3, locator: "§4; §5.4"}, {source: S6, locator: "IX ch. 8"}]}
    - {code: ISLAM, reason: "Rejected as primary. He was a Muslim and a jurist and accepts bodily resurrection on the Prophet's word (S6, IX ch. 9). But his working metaphysics is falsafa: the ISLAM system record's do_not_use_when sends falsafa to CLASS_THEISM, and al-Ghazali declared three of his teachings unbelief (S9, §3). Recorded as nominal affiliation.", cites: [{source: S9, locator: "§3"}, {source: S6, locator: "IX ch. 9, p. 633"}]}
    - {code: PLATO, reason: "Rejected. He takes Neoplatonic emanation (S2, §5; S3, §5.4), but SEP calls the system Aristotelian physics and metaphysics capped with emanation, and IEP says he rejected Neoplatonic epistemology and the pre-existent soul. The PLATO guidance sends Platonism inside Islam to the host religion or CLASS_THEISM.", cites: [{source: S2, locator: "§5"}, {source: S4, locator: "opening paragraph"}]}
    - {code: ARIST, reason: "Rejected. He renews Aristotle but adds a creator who is the Necessary Existent, creation from it without time, prophecy and providence.", cites: [{source: S3, locator: "§1; §5.3"}]}
    - {code: DEISM, reason: "Rejected. Deism rejects revelation; he proves the need for a prophet and lawgiver and gives revelation a real place (S6, X ch. 2).", cites: [{source: S6, locator: "X ch. 2, pp. 661–664"}]}
  lio_axes:
    A_locus:
      value: 1
      basis: written_profession
      certainty: 1.0
      cites: [{source: S6, locator: "X ch. 2, p. 664"}, {source: S3, locator: "§4; §6.1"}, {source: S4, locator: "§6"}]
      how_known: "Metaphysics of The Cure, in a scholarly translation; written profession, so 1.0."
      rationale: "Leans to the transcendent pole. God is neither outside nor inside the world and is not like any earthly thing (S6, X ch. 2); it is the Necessary Existent, distinct from all things that exist through it (S3, §4). It knows itself, wills and loves, but its will is identical with its act of thinking and has no deliberation or time (S3, §6.1), and it knows individual things only in a universal way (S4, §6). That is a transcendent source, less personal than the 0 pole, so 1. Same score as the CLASS_THEISM system record."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 1.0
      cites: [{source: S6, locator: "IX ch. 8, pp. 617–618; X ch. 1, pp. 656–657; X ch. 2, p. 664"}, {source: S8, locator: "§1 (natures and the kalam critique)"}]
      how_known: "Metaphysics of The Cure, in a scholarly translation; written profession, so 1.0."
      rationale: "Leans to law. The causes of the heavens cannot act for our sake (S6, p. 617). Providence is God knowing the order of the good, from which things flow in a fixed order (p. 618). Everything comes to be through other causes, and answered prayer is explained inside that order, not by God changing course (pp. 656–657). The stated exception: a prophet must be marked out by things other people do not see, so he must work miracles (p. 664). Al-Ghazali's attack on causal necessity was aimed at this kind of view (S8). So 3. SEP describes religious and 'paranormal' phenomena as functions of the rational soul (S2, §4), which would point to 4; the record keeps 3 because he states the miracles as an exception."
    C_ledger:
      value: 3
      basis: written_profession
      certainty: 1.0
      cites: [{source: S6, locator: "IX ch. 9, pp. 633–643; X ch. 2, pp. 664–665"}, {source: S2, locator: "§4; §5"}]
      how_known: "Metaphysics of The Cure, in a scholarly translation; written profession, so 1.0."
      rationale: "Leans to consequence. The soul's bliss after death follows from its own state: the more it contemplates, the more it is disposed to bliss (S6, p. 643), and real happiness is the perfection of the rational soul through knowledge (S2, §4). The stated exception: bodily reward and punishment at the resurrection, which he accepts on the authority of the religious law (S6, p. 633). The prophet's teaching that God rewards obedience and punishes disobedience is framed as instruction for the many in parables (S6, pp. 664–665). So 3."
    D_authority:
      value: 3
      basis: written_profession
      certainty: 1.0
      cites: [{source: S6, locator: "IX ch. 9, p. 633; X ch. 2, pp. 664–666"}, {source: S2, locator: "§4"}]
      how_known: "Metaphysics of The Cure, in a scholarly translation, and his De anima as quoted by SEP; written profession, so 1.0."
      rationale: "Leans to reason. Demonstration decides; even the prophet knows by middle terms, since beliefs taken on authority about things known through their causes 'possess no intellectual certainty' (S2, §4). Religion gives the many images and parables, and those fit for philosophy are invited to find the truth by demonstration (S6, pp. 665–666). The stated exception: truths about the afterlife of the body, which cannot be proved and which he accepts on revelation (S6, p. 633). So 3."
    E_scope:
      value: 3
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S2, locator: "§4"}, {source: S6, locator: "IX ch. 9, p. 643; X ch. 1, p. 651"}, {source: S10, locator: "Avicenna section"}]
      how_known: "Coder's reading of SEP's account and the translated text; neither addresses the axis directly, so 0.5."
      rationale: "Leans to same rules for all. One graded order runs from the intellects through the spheres to matter, plants, animals and humans (S6, p. 651); all humans have the means to reach knowledge and bliss but must work for it, with no free gift for the idle (S2, §4). The limited exception is the prophet, a rare soul whose matter suits a perfection that few human mixtures can receive (S6, X ch. 3 opening, via S10). Gutas reads the prophet as a natural extreme of the intellect (S2); Horten reads him as raised above nature (S10). That disagreement is why this is 0.5."
  mid_basin:
    value: true
    certainty: 1.0
    cites: [{source: S6, locator: "IX ch. 8, pp. 617–618; X ch. 1, p. 657; X ch. 2, p. 664"}, {source: S3, locator: "§4"}]
    how_known: "P4 test applied to the scores above: A_locus = 1 (≤ 1) at 1.0 and B_cause = 3 (≥ 3) at 1.0, B scored for the domain of his work (philosophy, natural science and medicine). Both certainties are at least 0.7, so true. F = 5, so first-rank is met."
  statements:
    - text: "noch auch außerhalb oder innerhalb der Welt sich befindet, noch irgend ein Ding darstellt, das beschaffen ist, wie die irdischen Dinge"
      cites: [{source: S6, locator: "X. Abhandlung, 2. Kapitel, p. 664"}]
      context: "Metaphysics of The Cure (completed in Isfahan by 1027, S4). Why the prophet should not burden the many with proofs about God: God cannot be pointed to in a place, is not divisible, is neither outside nor inside the world, and is not like earthly things. ('[God] is neither outside nor inside the world, nor any thing made like earthly things.')"
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
      note: "German translation by Max Horten (1907) from the Arabic; checked against the archive.org OCR of the University of Toronto copy. English gloss in context is the coder's."
    - text: "daß die Ursachen der himmlischen Welt nicht etwa unseretwegen ihre Wirkungen ausüben können"
      cites: [{source: S6, locator: "IX. Abhandlung, 8. Kapitel, p. 617"}]
      context: "Opening of the chapter on providence and evil (Cairo numbering IX.6, as SEP cites it). ('that the causes of the heavenly world cannot exert their effects for our sake')"
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
      note: "Horten's German translation."
    - text: "Deshalb strömt von ihm dasjenige aus, was er denkt, in einer bestimmten Ordnung und nach der Art des Guten in der vollkommensten Weise, die er denkt"
      cites: [{source: S6, locator: "IX. Abhandlung, 8. Kapitel, p. 618"}]
      context: "His definition of providence; the next sentence reads 'Dies ist das, was man unter göttlicher Vorsehung versteht.' ('Therefore what he thinks flows from him in a fixed order and in the way of the good, in the most perfect manner that he thinks.')"
      axes: [B_cause, A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
      note: "Horten's German translation."
    - text: "Bei ihm entsteht das Werden alles dessen, was entsteht; jedoch entsteht dasselbe durch Vermittlung anderer Ursachen."
      cites: [{source: S6, locator: "X. Abhandlung, 1. Kapitel, p. 657"}]
      context: "Chapter on inspiration, answered prayer, heavenly punishment, prophecy and astrology. Answered prayers and successful sacrifices are then said to be explained by these relations. ('From him comes the becoming of all that comes to be; yet it comes to be through the mediation of other causes.')"
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
      note: "Horten's German translation."
    - text: "Er muß also Wunder wirken, wie wir solche auch von unseren Propheten gehört haben."
      cites: [{source: S6, locator: "X. Abhandlung, 2. Kapitel, p. 664"}]
      context: "On the need for a prophet: he must have traits others lack so that people see in him things they do not otherwise see. ('So he must work miracles, as we have also heard of from our prophets.')"
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
      note: "Horten's German translation."
    - text: "daß betreffs des Jenseitigen Lebens einige Wahrheiten auf Grund des Religionsgesetzes feststehen, ohne daß man diese beweisen könnte"
      cites: [{source: S6, locator: "IX. Abhandlung, ch. on the afterlife ('Zehntes Kapitel' in the text, '9. Kapitel' in the contents), p. 633"}]
      context: "These truths concern the body at the resurrection; the next paragraph says the soul's bliss and punishment can be known by reason and demonstration. ('that some truths about the afterlife are fixed by the religious law, without its being possible to prove them')"
      axes: [D_authority, C_ledger]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
      note: "Horten's German translation."
    - text: "Andere Wahrheiten betreffs des Jenseitigen Lebens sind durch den Verstand und durch den demonstrativen Beweis erkennbar."
      cites: [{source: S6, locator: "IX. Abhandlung, ch. on the afterlife, p. 633"}]
      context: "Same chapter. ('Other truths about the afterlife can be known by the intellect and by demonstrative proof.')"
      axes: [D_authority, C_ledger]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
      note: "Horten's German translation."
    - text: "So oft der Betreffende (in diesem Leben) in seiner Betrachtung intensiver denkt, vermehrt sich auch die Disposition für seine Glückseligkeit."
      cites: [{source: S6, locator: "IX. Abhandlung, ch. on the afterlife, p. 643"}]
      context: "On what the soul's bliss consists in. The words in parentheses are Horten's. ('The more intensely a person thinks in contemplation (in this life), the more his disposition for bliss grows.')"
      axes: [C_ledger, E_scope]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
      note: "Horten's German translation."
    - text: "Daher muß er die Lehre über das Glück und das Unglück des jenseitigen Lebens in Gleichnissen vorführen"
      cites: [{source: S6, locator: "X. Abhandlung, 2. Kapitel, p. 665"}]
      context: "The prophet's teaching for the many. ('Therefore he must present the teaching about the happiness and unhappiness of the next life in parables.')"
      axes: [D_authority, C_ledger]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
      note: "Horten's German translation."
    - text: "for beliefs accepted on authority concerning those things which are known only through their causes possess no intellectual certainty"
      cites: [{source: S2, locator: "§4 (quoting The Cure, De anima, 249–250, trans. Gutas)"}]
      context: "On how the prophet acquires knowledge: in an order that includes the middle terms, not by uncritical reception on authority."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
      note: "Known here only through SEP's quotation of Gutas's English translation. Supports D only together with the Horten passages."
  changes_over_life:
    - {value: UNKNOWN, how_known: "No change of system is reported in S2–S5. IEP notes debate over a later 'Eastern' philosophy and mystical leanings in some late works (S4, §8); not treated as a change of system here."}
  coder_notes: "Code and axes rest mainly on Horten's 1907 German translation of the Metaphysics of The Cure, which is public domain but loose in places and adds words in parentheses; Marmura's English translation (2005) was not read. Horten's notes (not his translation) and Gutas disagree on whether prophecy is natural or supernatural; the record uses the text, not Horten's notes. Al-Ghazali says Ibn Sina taught that souls never return to bodies (S9), while the Metaphysics of The Cure accepts bodily resurrection on religious authority (S6, p. 633). Both are recorded; C and D were scored from The Cure."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Persian; his father came from Balkh", certainty: 0.7, cites: [{source: S1, locator: "heading ('Persian philosopher and scientist')"}, {source: S2, locator: "§1.1"}], how_known: "Britannica's label and SEP on the father's origin."}
  religious_heritage_by_birth: {value: "Muslim, in a household touched by Ismaʿili preaching", certainty: 0.7, cites: [{source: S7, locator: "Autobiography, p. 9"}, {source: S4, locator: "§1"}], how_known: "His own account and IEP, which hedges."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not applicable as an initiation rite in his setting, and no event recorded in S1–S7."}
  childhood_catechism: {value: "Qurʾān mastered by about age 10 under teachers of the Qurʾān and letters", certainty: 1.0, cites: [{source: S1, locator: "Life and education"}, {source: S5, locator: "Biography"}, {source: S7, locator: "Autobiography, p. 9"}], how_known: "Three sources."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "c. 1012–1037", certainty: 0.7, cites: [{source: S4, locator: "§1; §2"}, {source: S5, locator: "Biography"}], how_known: "From Jurjan and Hamadan, where the Canon and The Cure were begun, to his death. Start approximate."}
  age_at_first_lasting_contribution: {value: 36, certainty: 0.5, cites: [{source: S4, locator: "§2"}, {source: S1, locator: "Quick Facts"}], how_known: "The Cure begun 1016 and birth about 980. The birth year is disputed (S2: about 970), so the age could be 46."}
  first_evidence_of_lio_type_views: {value: "The Metaphysics of The Cure states providence as the fixed order of the good, with everything coming to be through intermediate causes.", year: 1027, certainty: 0.5, cites: [{source: S6, locator: "IX ch. 8; X ch. 1"}, {source: S4, locator: "§2 (completed by 1027)"}], how_known: "Latest date for The Cure's completion; the passages may be earlier. Earlier works (Compendium on the Soul, Philosophy for ʿArudi) were not read, so 0.5."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "The lawful-order statements read are in The Cure, his main work.", certainty: 0.7, cites: [{source: S6, locator: "IX ch. 8"}], how_known: "Dated work; earlier works not read."}
  worldview_during_major_work: {value: "The same falsafa system throughout The Cure and the later summae, as far as the sources read show.", certainty: 0.7, cites: [{source: S2, locator: "§1.2; §5"}], how_known: "SEP describes one self-consistent system."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "His philosophy is built as demonstrative science from premises and middle terms, and even the prophet's knowledge is ordered by middle terms (S2, §3–§4). Inside nature, the stated exceptions are few (prophetic miracles, bodily resurrection on faith).", certainty: 0.5, cites: [{source: S2, locator: "§3; §4"}, {source: S5, locator: "Biography (geometry in The Cure)"}], how_known: "Coder's reading."}
  form_acquired: {value: "childhood or adolescence", rationale: "Euclid and logic with al-Natili as a boy, and his own account of setting out premises and deductions in files before 18 (S7).", certainty: 0.7, cites: [{source: S7, locator: "Autobiography, pp. 9–11"}, {source: S2, locator: "§1.1"}], how_known: "His own account and SEP."}
  circle_present: {value: "no", rationale: "God is neither in nor outside the world and is not like any created thing (S6, X ch. 2). Emanation from God and the soul's return to God form a procession and return, not an identity of God and Nature.", certainty: 0.5, cites: [{source: S6, locator: "X ch. 2, p. 664; contents, IX"}, {source: S3, locator: "§5.4"}], how_known: "Coder's reading; a reviewer could argue 'partly' because of emanation."}
  reading: "As belief, not finding: the form is present and was acquired in adolescence, without the identity circle. Emanation is the nearest thing to a circle. The record does not test H1."
  notes: ""

institutions:
  - {value: "Samanid court, Bukhara", role: "physician to the ruler; post in the financial administration", years: "c. 997–999", kind: employer, certainty: 1.0, cites: [{source: S2, locator: "§1.1"}, {source: S4, locator: "§1"}], how_known: "Two sources."}
  - {value: "Court of Khwarazm, Gurganj", role: "jurist and scholar", years: "c. 999–1012", kind: employer, certainty: 0.7, cites: [{source: S2, locator: "§1.1"}, {source: S5, locator: "Biography"}], how_known: "Two sources; MacTutor gives the jurist role."}
  - {value: "Buyid court, Hamadan", role: "physician; twice vizier to Shams al-Dawla", years: "1015–c. 1022", kind: "government or state body", certainty: 1.0, cites: [{source: S4, locator: "§1"}, {source: S5, locator: "Biography"}, {source: S2, locator: "§1.1"}], how_known: "Three sources; end year varies (see flags)."}
  - {value: "Kakuyid court of ʿAlāʾ al-Dawla, Isfahan", role: "physician, counsellor and scholar", years: "c. 1022–1037", kind: "patron or funder", certainty: 1.0, cites: [{source: S1, locator: "Life and education"}, {source: S2, locator: "§1.1"}, {source: S4, locator: "§1"}], how_known: "Three sources."}

collaborators:
  - {value: "Abu ʿAbd Allah al-Natili", relation: teacher, note: "logic, Euclid, Almagest", certainty: 0.7, cites: [{source: S7, locator: "Autobiography, pp. 9–10"}, {source: S1, locator: "Life and education"}], how_known: "Two sources."}
  - {value: "Abu ʿUbayd al-Juzjani", relation: "student or assistant", note: "student, companion and scribe from about 1012; wrote the Biography continuing the Autobiography", years: "c. 1012–1037", certainty: 1.0, cites: [{source: S2, locator: "§1.1"}, {source: S4, locator: "§1"}], how_known: "Two sources."}
  - {value: "al-Biruni", roster_id: al-biruni, relation: correspondent, note: "answered his questions on Aristotelian physics and cosmology", certainty: 1.0, cites: [{source: S2, locator: "§1.2"}, {source: S5, locator: "Biography"}], how_known: "Two sources."}
  - {value: "al-Farabi", roster_id: al-farabi, relation: "influenced by", note: "his short book on the aims of Aristotle's Metaphysics; his early works were written under al-Farabi's influence", certainty: 1.0, cites: [{source: S4, locator: "§1; §2"}, {source: S1, locator: "opening paragraph"}], how_known: "Two sources."}
  - {value: "Aristotle", roster_id: aristotle, relation: "influenced by", note: "the curriculum he reworked; called 'The First Teacher'", certainty: 1.0, cites: [{source: S2, locator: "opening paragraph; §5"}, {source: S3, locator: "§1"}], how_known: "Two sources."}
  - {value: "al-Ghazali", roster_id: al-ghazali, relation: "rival or critic", note: "posthumous critic; judged three of his teachings unbelief", certainty: 1.0, cites: [{source: S9, locator: "§3"}, {source: S4, locator: "opening paragraph"}], how_known: "Two sources."}
  - {value: "Thomas Aquinas", roster_id: aquinas-thomas, relation: influenced, note: "Latin metaphysics; internal senses", certainty: 1.0, cites: [{source: S4, locator: "opening paragraph; §3"}, {source: S1, locator: "Top Questions"}], how_known: "Two sources."}
  - {value: "Moses Maimonides", roster_id: maimonides, relation: influenced, note: "accepted most of his ideas in the Guide of the Perplexed", certainty: 0.7, cites: [{source: S2, locator: "opening paragraph"}], how_known: "One source."}

review:
  roster_status_reason: {value: "Core in v7.1 (F 9) and v8; F fell to 5 because the v8 roster counts five models.", certainty: 0.7, cites: [{source: S11, locator: "roster.csv, rank 39"}], how_known: "Study roster (F_change_vs_v7 = -4). The reason for the drop is the coder's reading of the column."}
  controversies:
    - {value: "Al-Ghazali's Incoherence judged three of his teachings (world without a beginning in time; God's knowledge only of universals; no return of souls to bodies) to be unbelief, and declared those who teach them publicly apostates", certainty: 1.0, cites: [{source: S9, locator: "§3"}], how_known: "SEP (Griffel)."}
  data_quality_flags:
    - "Birth year: Britannica, IEP, MacTutor and SEP Natural Philosophy give 980; SEP's main entry (Gutas) gives about 970, 'perhaps as early as 964'."
    - "Birthplace: SEP, IEP and the Autobiography say Afshana; MacTutor says Kharmaithen, which was his father's district."
    - "Britannica's Quick Facts puts Bukhara in 'Iran [now in Uzbekistan]'; Bukhara is in Uzbekistan, and the record uses that."
    - "Isfahan years: SEP '1024?–1037'; IEP has him join ʿAlāʾ al-Dawla after Shams al-Dawla's death in 1021; MacTutor says he left Hamadan in 1022."
    - "Bodily resurrection: al-Ghazali says Ibn Sina taught that souls never return into bodies (S9); the Metaphysics of The Cure accepts bodily resurrection on the authority of the religious law (S6, p. 633)."
    - "God's knowledge of particulars: IEP says 'God only knows kinds of existents and not individuals'; Horten's chapter title says God knows all individual things in their causes, and the text says he knows them insofar as they are universal (S6, VIII ch. 6, pp. 523–524)."
    - "Prophecy: Gutas (S2) says the divine 'flow' of knowledge 'has nothing mystical about it'; Horten (S10) reads the prophet's soul as supernatural."
    - "S6 chapter numbers are Horten's; they differ from the Cairo edition used by SEP (Horten IX ch. 8 = Cairo IX.6). The afterlife chapter is headed 'Zehntes Kapitel' in the text but listed as '9. Kapitel' in Horten's contents."
    - "S7 (Arberry) was read in a poor OCR scan; all S7 material is paraphrased and page numbers are approximate."
    - "Britannica's 'Top Questions' box (S1) may be AI-generated; it is used only alongside other sources."
  open_questions:
    - "Read Marmura's English translation of the Metaphysics of The Cure (2005) to check the Horten passages and get Cairo chapter numbers."
    - "Read Gohlman's edition of the Autobiography (1974) for exact quotations on his schooling and religion."
    - "B_cause 3 or 4: decide whether prophetic miracles, explained as powers of the soul, count as a stated exception."
    - "Resolve the bodily-resurrection conflict between The Cure and his other works (al-Ghazali's charge)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Michael Flannery"
    citation: "Flannery, Michael. \"Avicenna.\" Encyclopaedia Britannica. Last updated September 11, 2026. https://www.britannica.com/biography/Avicenna."
    url: "https://www.britannica.com/biography/Avicenna"
    accessed: 2026-10-02
    reliability_note: "Signed article by a historian of medicine; fact-checked by Britannica editors. Its Top Questions box may be AI-generated and is not relied on alone."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, institutions, collaborators]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Dimitri Gutas"
    year: 2025
    citation: "Gutas, Dimitri. \"Ibn Sina [Avicenna].\" Stanford Encyclopedia of Philosophy, first published 15 September 2016, substantive revision 31 October 2025. https://plato.stanford.edu/entries/ibn-sina/."
    url: "https://plato.stanford.edu/entries/ibn-sina/"
    accessed: 2026-10-02
    reliability_note: "Peer-reviewed entry by a leading Avicenna scholar. Quotes his own translations of Ibn Sina."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators, review]
  - id: S3
    type: tertiary
    kind: encyclopedia
    author: "Olga Lizzini"
    year: 2026
    citation: "Lizzini, Olga. \"Ibn Sina's Metaphysics.\" Stanford Encyclopedia of Philosophy, first published 2 December 2015, substantive revision 9 June 2026. https://plato.stanford.edu/entries/ibn-sina-metaphysics/."
    url: "https://plato.stanford.edu/entries/ibn-sina-metaphysics/"
    accessed: 2026-10-02
    reliability_note: "Peer-reviewed reference entry."
    used_for: [contribution, worldview, lane_b, collaborators]
  - id: S4
    type: tertiary
    kind: encyclopedia
    author: "Sajjad H. Rizvi"
    citation: "Rizvi, Sajjad H. \"Avicenna (Ibn Sina).\" Internet Encyclopedia of Philosophy. https://iep.utm.edu/avicenna-ibn-sina/."
    url: "https://iep.utm.edu/avicenna-ibn-sina/"
    accessed: 2026-10-02
    reliability_note: "Peer-reviewed reference entry."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators]
  - id: S5
    type: tertiary
    kind: encyclopedia
    author: "J. J. O'Connor and E. F. Robertson"
    year: 1999
    citation: "O'Connor, J. J., and E. F. Robertson. \"Abu Ali al-Husain ibn Abdallah ibn Sina (Avicenna).\" MacTutor History of Mathematics Archive, University of St Andrews, last update November 1999. https://mathshistory.st-andrews.ac.uk/Biographies/Avicenna/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Avicenna/"
    accessed: 2026-10-02
    reliability_note: "University reference archive; strongest on his mathematics and astronomy."
    used_for: [basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S6
    type: primary
    kind: "scholarly edition"
    author: "Ibn Sina (trans. Max Horten)"
    year: 1907
    citation: "Avicenna. Die Metaphysik Avicennas, enthaltend die Metaphysik, Theologie, Kosmologie und Ethik. Übersetzt und erläutert von M. Horten. Halle a. S. and New York: Rudolf Haupt, 1907 (Das Buch der Genesung der Seele, II. Serie, III. Gruppe, XIII. Teil). University of Toronto copy, https://archive.org/details/diemetaphysikavi00avicuoft."
    url: "https://archive.org/details/diemetaphysikavi00avicuoft"
    accessed: 2026-10-02
    reliability_note: "Complete German translation of the Metaphysics (Ilāhiyyāt) of The Cure, his own published work; public domain. Horten's translation is loose in places and his parentheses and notes are his own. Page numbers from the printed page markers in the OCR."
    used_for: [worldview, timing, lane_b]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "Ibn Sina (trans. A. J. Arberry)"
    year: 1951
    citation: "Avicenna on Theology. Trans. A. J. Arberry. London: John Murray, 1951 (Wisdom of the East). Autobiography of Avicenna, pp. 9–13. Scan: Indira Gandhi National Centre for the Arts, https://archive.org/details/in.gov.ignca.7274."
    url: "https://archive.org/details/in.gov.ignca.7274"
    accessed: 2026-10-02
    reliability_note: "His own account of his early life, dictated to al-Juzjani. Read in a poor OCR text, so only paraphrased; Gutas warns the Autobiography is shaped to make a philosophical point (S2, S4)."
    used_for: [basics, childhood, heritage, lane_b, collaborators]
  - id: S8
    type: tertiary
    kind: encyclopedia
    author: "Jon McGinnis"
    year: 2025
    citation: "McGinnis, Jon. \"Ibn Sina's Natural Philosophy.\" Stanford Encyclopedia of Philosophy, first published 29 July 2016, substantive revision 20 March 2025. https://plato.stanford.edu/entries/ibn-sina-natural/."
    url: "https://plato.stanford.edu/entries/ibn-sina-natural/"
    accessed: 2026-10-02
    reliability_note: "Peer-reviewed reference entry."
    used_for: [basics, worldview]
  - id: S9
    type: tertiary
    kind: encyclopedia
    author: "Frank Griffel"
    year: 2026
    citation: "Griffel, Frank. \"Al-Ghazali.\" Stanford Encyclopedia of Philosophy, first published 14 August 2007, substantive revision 15 January 2026. https://plato.stanford.edu/entries/al-ghazali/."
    url: "https://plato.stanford.edu/entries/al-ghazali/"
    accessed: 2026-10-02
    reliability_note: "Peer-reviewed reference entry."
    used_for: [worldview, collaborators, review]
  - id: S10
    type: secondary
    kind: "scholarly book"
    author: "Max Horten"
    year: 1913
    citation: "Horten, M. Texte zu dem Streite zwischen Glauben und Wissen im Islam: Die Lehre vom Propheten und der Offenbarung bei den islamischen Philosophen Farabi, Avicenna und Averroes. Bonn: Marcus und Weber, 1913. Avicenna section, pp. 7–9. https://archive.org/details/textezudemstreit00hortuoft."
    url: "https://archive.org/details/textezudemstreit00hortuoft"
    accessed: 2026-10-02
    reliability_note: "Older scholarly reading that treats the prophet as supernatural; used only to show the disagreement with Gutas."
    used_for: [worldview, review]
  - id: S11
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv and data/roster/person_ids.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# Ibn Sina (Avicenna)

> Status: draft — unreviewed. Worldview coded CLASS_THEISM at 1.0; all five LIO axes scored; mid_basin true under the P4 test.

## Summary

Ibn Sina (about 980–1037; Latin Avicenna) was a philosopher and physician from near Bukhara who worked at courts in Central Asia and Iran [S2, §1.1; S4, §1]. He wrote The Cure, an encyclopaedia of philosophy and science, and the Canon of Medicine, which was taught in European universities until the 17th century [S2; S1]. SEP ranks his influence second only to Aristotle's [S2, opening paragraph].

## Life and work

He grew up in Bukhara, where his father served the Samanids [S2, §1.1]. He studied with tutors, then largely by himself, and says he had mastered the sciences by 18 [S2; S7]. After curing the Samanid ruler he was given the use of the royal library [S1; S2]. He left Bukhara after it fell in 999 and served rulers at Gurganj, Jurjan, Rayy, Hamadan (as vizier) and Isfahan [S2, §1.1; S4, §1]. He completed The Cure in Isfahan by 1027 [S4, §2]. He died at Hamadan in 1037 [S2].

## Contribution and impact

- The Cure (1016–1027): logic, natural science, mathematics and metaphysics [S4, §2].
- The Canon of Medicine [S1, Influence in medicine].
- The necessary and possible in existence; God as the Necessary Existent [S3, §4].
- The "flying man" argument [S4, §7].

## Childhood and education

He learned the Qurʾān by about 10 [S1; S5]. His own account says his father and brother listened to Ismaʿili missionaries, and that he listened but did not agree [S7, p. 9]. He learned Indian arithmetic from a vegetable seller, and logic and the first figures of Euclid from al-Natili, then went on alone [S7, pp. 9–10]. He began medicine at about 13 [S5].

## Adult working worldview

God is the Necessary Existent, not in the world or outside it, and not like any earthly thing [S3, §4; S6, p. 664]. Providence is the order of the good that flows from God's thinking [S6, p. 618]. Everything comes to be through other causes [S6, p. 657]. A prophet must work miracles [S6, p. 664]. Bliss after death follows the soul's state of knowledge; bodily resurrection is accepted on the religious law [S6, pp. 633, 643]. The prophet teaches the many in parables [S6, p. 665]. Al-Ghazali judged three of his teachings to be unbelief [S9, §3].

Coding: CLASS_THEISM at 1.0. A 1, B 3, C 3, D 3 at 1.0; E 3 at 0.5. mid_basin true.

## Heritage (context only)

Persian, with a father from Balkh; a Muslim household touched by Ismaʿili preaching [S1; S2; S7]. Heritage is recorded for context only. It is not a worldview code.

## Timing

His first lasting work, The Cure, was begun in 1016, at about 36 [S4, §2]. Its lawful-order statements fall inside the major work.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. The form (demonstrative science) is present and was acquired in adolescence through Euclid and logic [S7; S2]. There is no identity circle; emanation and return is the nearest thing to one [S3, §5.4; S6].

## Open questions

- Check the Horten passages against Marmura's English translation.
- Read Gohlman's Autobiography edition for exact quotations.
- B_cause 3 or 4.
- The bodily-resurrection conflict between The Cure and al-Ghazali's charge.

## Research log

- 2026-10-02: Read Britannica (S1), SEP entries by Gutas (S2), Lizzini (S3), McGinnis (S8) and Griffel (S9), IEP (S4) and MacTutor (S5). Read the providence, prayer, afterlife and prophecy chapters of the Metaphysics of The Cure in Horten's 1907 German translation (S6), and the Autobiography in Arberry's 1951 translation through a poor OCR scan (S7, paraphrased only). Horten 1913 (S10) for an older reading. Wikipedia not used. Every quotation was checked word for word against the fetched text with a script (verify_quotes.py) before commit. Marmura's and Gohlman's translations were not read.
