---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch C)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-08
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to medieval. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-08, by: "Grok Bot", summary: "Record created (stage 3 batch C, order P32). Basics from SEP 'al-Farabi' (Druart 2024) and Britannica (editors); worldview from SEP 'al-Farabi's Philosophy of Society and Religion' (Germann 2021), a scholarly reconstruction; his own words only as SEP quotes them (secondary quotation, primary check pending). Works undated, so first-lasting year, span and age UNKNOWN (P12). primary_system CLASS_THEISM 0.5 (Straussian reading named); A 1, B 4, C 4, D 4, E 4, all 0.5 (scholarly_reconstruction); mid_basin BELOW_THRESHOLD. Draft, not reviewed."}
    - {date: 2026-10-08, by: "Grok Bot", summary: "Lens audit of batch C (dd91009), run 1: #7 B_cause 4 → 3 at 0.5, alternative 4, citing Germann §3.1 (free will set against acting by nature) under the B 3 anchor and P36 (ruling R2, v8's pick). mid_basin unchanged (BELOW_THRESHOLD)."}
    - {date: 2026-10-23, by: "Grok Bot", summary: "Deepen pass D1 (queue #3). P47 source_quality on every source. Primary check: Butterworth Political Regime (2015; new S5) and Selected Aphorisms / Book of Religion (2001; new S6–S7). A_locus 1 and B_cause 3 raised from scholarly_reconstruction 0.5 → written_profession 0.7 (contested Straussian/alt caps; P26 primary check). B support single → corroborated (S2+S5+S6). A support stays corroborated (S1+S2+S5). mid_basin BELOW_THRESHOLD → true (A≤1 and B≥3 both at ≥0.7). Chart person-dot: faded hollow → dark filled. Book of Religion quote verified against Butterworth. Native name filled. No fallacy_catalog (Jason 2026-10-23). Draft, not reviewed."}

identity:
  id: al-farabi
  display_name: "Al-Farabi"
  roster:
    canonical_name: "Al-Farabi"
    rank: 3
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Abū Naṣr Muḥammad ibn Muḥammad al-Fārābī", certainty: 0.7, cites: [{source: S1, locator: "opening ('Abū Naṣr al-Fārābī')"}, {source: S3, locator: "Also known as ('Muḥammad ibn Muḥammad ibn Ṭarkhān ibn Awzalagh al-Fārābī')"}], how_known: "SEP gives the kunya; Britannica the fuller name, with variant spellings of the last element."}
  native_name: {value: "Abū Naṣr Muḥammad al-Fārābī", certainty: 0.7, cites: [{source: S1, locator: "opening ('Abū Naṣr al-Fārābī')"}], how_known: "SEP transliterated Arabic (same pattern as al-Ghazali / al-Razi records)."}
  aliases:
    - {name: "Farabi", kind: "roster alias"}
    - {name: "Alpharabius", kind: latinized}
    - {name: "Alfarabius", kind: latinized}
    - {name: "Avennasar", kind: latinized}

basics:
  birth:
    date:
      value: "870"
      certainty: 0.5
      cites: [{source: S1, locator: "opening ('probably born in 870 CE (AH 257)')"}]
      how_known: "SEP says 'probably'; Britannica gives c. 878. A real disagreement and both hedged, so 0.5."
      alternatives:
        - {value: "878", cites: [{source: S3, locator: "Born line ('c. 878')"}], note: "Britannica, approximate."}
    place:
      value: "Farab (or Farayb)"
      modern_name: "probably Otrar district, Kazakhstan"
      polity_then: "Samanid realm (Transoxiana)"
      certainty: 0.5
      cites: [{source: S1, locator: "opening ('a place called Farab or Farayb')"}, {source: S3, locator: "Born line ('Turkistan')"}]
      how_known: "SEP names the place; Britannica gives the region 'Turkistan'. The modern location and the polity are the coder's identification, not stated in the sources read, so 0.5."
      alternatives:
        - {value: "Faryab, Khorasan (modern Afghanistan)", cites: [{source: S1, locator: "opening ('Farayb')"}], note: "Coder's reading of the variant 'Farayb'; not stated in the sources read."}
  death:
    date:
      value: "950"
      certainty: 0.7
      cites: [{source: S1, locator: "opening ('December 950 CE or January 951 CE (AH 339)')"}, {source: S3, locator: "Died line ('c. 950')"}]
      how_known: "Both give 950 or about 950; SEP allows January 951, so 0.7 with the alternative."
      alternatives:
        - {value: "951-01", cites: [{source: S1, locator: "opening"}], note: "SEP's second possibility."}
    place:
      value: "Damascus"
      modern_name: "Damascus, Syria"
      polity_then: "Ikhshidid domains"
      certainty: 0.7
      cites: [{source: S1, locator: "opening ('died in Damascus')"}, {source: S3, locator: "Died line ('Damascus?')"}]
      how_known: "SEP states Damascus; Britannica queries it and says he lived mostly in Aleppo from 942. Polity is the coder's identification."
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "No source read dates any of his lasting works; Britannica says only that most were written in Baghdad (P12: undated items do not set the year)."}
  era_bucket: {value: "500 to 1399", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "Born and Died lines"}], how_known: "Every work falls between his birth (870 or 878) and death (950 or 951), so any first-lasting year gives the same bucket (P2)."}
  region_of_birth:
    value: "Central Asia"
    certainty: 0.5
    cites: [{source: S3, locator: "Born line ('Turkistan'); paragraph 2 ('moved from Central Asia to Baghdad')"}, {source: S1, locator: "opening"}]
    how_known: "Britannica places his origin in Central Asia; Farab on the Syr Darya is in modern Kazakhstan, which is Central Asia in data/reference/regions.csv (P3). 0.5 because the place is uncertain."
    alternatives:
      - {value: "South Asia", cites: [{source: S1, locator: "opening ('Farayb')"}], note: "If Faryab in modern Afghanistan (South Asia in regions.csv); coder's reading."}
  region_of_work: {value: "Middle East and North Africa", certainty: 1.0, cites: [{source: S1, locator: "opening (Baghdad; Syria and Damascus)"}, {source: S3, locator: "paragraph 2 (Baghdad; Aleppo)"}], how_known: "Iraq and Syria are Middle East and North Africa in regions.csv."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S1, locator: "throughout"}, {source: S3, locator: "throughout"}], how_known: "As the sources record it."}
  languages_of_work: {value: [Arabic], certainty: 1.0, cites: [{source: S1, locator: "§1 (Arabic titles)"}, {source: S3, locator: "paragraph 3 ('Arabic Aristotelian teachings')"}], how_known: "His works are in Arabic."}
  occupations: {value: ["philosopher", "logician", "music theorist"], certainty: 1.0, cites: [{source: S1, locator: "opening (two main interests)"}, {source: S3, locator: "heading"}], how_known: "Two sources."}

contribution:
  era_bucket: medieval
  fields: {value: ["logic", "political philosophy", "metaphysics", "music theory"], certainty: 1.0, cites: [{source: S1, locator: "opening; §§3, 4, 7"}, {source: S3, locator: "paragraphs 1, 3"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Works on Aristotelian logic and the classification of the sciences, for which he was called 'the second master' after Aristotle", kind: "body of work", lasting: "Latin translation of the Enumeration of the Sciences by Gerard of Cremona; basis of later Arabic logic (S1)", certainty: 1.0, cites: [{source: S1, locator: "opening ('the second master'); §§1, 3"}, {source: S3, locator: "paragraph 1 ('the greatest philosophical authority after Aristotle')"}], how_known: "Two sources; undated."}
    - {value: "Political philosophy of the virtuous city (The Opinions of the People of the Perfect City; The Political Regime)", kind: theory, lasting: "founding texts of Islamic political philosophy (S2; S3)", certainty: 1.0, cites: [{source: S1, locator: "§§6–7"}, {source: S2, locator: "§§3–4"}, {source: S3, locator: "paragraph 3"}], how_known: "Three sources; undated."}
    - {value: "Great Book of Music (Kitāb al-mūsīqā al-kabīr)", kind: work, lasting: "'the most important medieval musical treatise in Islamic lands' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; §4"}], how_known: "SEP alone; undated."}
  evidence_of_impact:
    - {value: "Known as 'the second master' after Aristotle", kind: "other", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "paragraph 1"}], how_known: "Two sources."}
  major_works:
    - {value: "The Opinions of the People of the Perfect City (Mabādiʾ ārāʾ ahl al-madīna al-fāḍila)", kind: book, certainty: 1.0, cites: [{source: S1, locator: "§6"}, {source: S2, locator: "§3"}], how_known: "Two sources; undated."}
    - {value: "The Political Regime (al-Siyāsa al-madaniyya)", kind: book, certainty: 0.7, cites: [{source: S1, locator: "§6"}], how_known: "SEP; undated."}
    - {value: "Book of Religion (Kitāb al-milla)", kind: book, certainty: 0.7, cites: [{source: S2, locator: "§4.1"}], how_known: "SEP; undated."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "The leading philosophical authority of medieval Islam after Aristotle (S3) and founder of Islamic political philosophy (S2).", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "paragraph 1"}], how_known: "Two sources."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "'We know little that is really reliable about al-Fārābī's life' (S1); nothing on his family."}
  family_religious_practice: {value: UNKNOWN, how_known: "Same."}
  parents_and_household: []
  household_circumstances: {value: UNKNOWN, how_known: "Not in the sources read."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "Not in the sources read."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not in the sources read."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Ethnic origin disputed (S1; S3); childhood language not known."}
  notable_events:
    - {value: "Moved in his youth to Iraq and Baghdad", certainty: 0.7, cites: [{source: S1, locator: "opening ('In his youth he moved to Iraq and Baghdad')"}, {source: S3, locator: "paragraph 2 ('eventually moved')"}], how_known: "SEP says in his youth; Britannica only 'eventually'."}

worldview:
  unit: "adult working worldview"
  working_years: {value: UNKNOWN, how_known: "Equals timing.major_work_period, which is UNKNOWN because no lasting work is dated (P12, P29)."}
  nominal_affiliations: []
  self_described_science_religion_relation:
    value: "Religion gives in symbols, for the many, the same truth that philosophy knows by demonstration; philosophy is epistemically superior. In the Book of Religion, religion is 'opinions and actions ... prescribed for a community by their first ruler'."
    certainty: 0.5
    cites: [{source: S2, locator: "§4.1"}, {source: S3, locator: "paragraph 3 ('He saw human reason as being superior to revelation')"}]
    how_known: "Scholarly reconstruction (Germann; Britannica), with his own words only as SEP quotes them in translation (secondary quotation, P26), so 0.5."
  primary_system:
    value: CLASS_THEISM
    basis: scholarly_reconstruction
    certainty: 0.5
    cites: [{source: S2, locator: "§2.1; §3.1; §4.1"}, {source: S1, locator: "§6"}, {source: S3, locator: "paragraph 3"}]
    how_known: "Scholars place him in Arabic Peripatetic philosophy: a single first cause from which the cosmos proceeds by Neoplatonic emanation (S1 §6; S2 §4.1), now also in his Political Regime (S5). The CLASS_THEISM system file names 'Arabic falsafa (al-Farabi, Avicenna, Averroes)' as a parent tradition. Held at 0.5: Straussian reading (S1 §6) still names a non-theistic alternative for the system code, so system certainty stays at the reconstruction/contest ceiling even though A is now written_profession."
    rationale: "Draft judgment (one line): CLASS_THEISM at 0.5. Named alternative (SEP §6): the Straussian reading (Butterworth), on which the emanation scheme is 'simply a rhetorical appeal' to make his views palatable to religious authorities; on that reading his working view would be philosophical rationalism (RATN or ARIST), not theism."
  secondary_system: {value: UNKNOWN, how_known: "No second system in the sources read."}
  candidate_codes_considered:
    - {code: CLASS_THEISM, reason: "Coded at 0.5: single first cause, emanation, a cosmos that is the best possible order (S1 §6; S2 §§3.1, 4.1). Against: the Straussian reading (S1 §6).", cites: [{source: S1, locator: "§6"}, {source: S2, locator: "§§3.1, 4.1"}]}
    - {code: ISLAM, reason: "Muslim philosopher (S3). Against: he treats religion as symbolic imitation of philosophy and an 'instrument of rulership' (S2 §4.1), and holds a purely intellectual afterlife 'in striking contrast to Islamic teachings' (S2 §2.1).", cites: [{source: S2, locator: "§§2.1, 4.1"}, {source: S3, locator: "paragraph 3"}]}
    - {code: ARIST, reason: "'The second master'; Aristotelian ontology (S1 §6). Against: the emanationist first parts of his political works (S1 §6). ARIST is a stub system file.", cites: [{source: S1, locator: "opening; §6"}]}
    - {code: RATN, reason: "Reason above revelation (S3). Considered as the Straussian alternative; not coded because Gutas, Menn and Druart take the emanation as core (S1 §6).", cites: [{source: S1, locator: "§6"}, {source: S3, locator: "paragraph 3"}]}
  lio_axes:
    A_locus:
      value: 1
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S5, locator: "Political Regime §§1–2, 20 (Butterworth 2015)"}, {source: S1, locator: "§6"}, {source: S2, locator: "§3.1; §4.1"}]
      how_known: "His own Political Regime (Butterworth translation, scholarly edition): the first cause is 'what ought to be believed to be the deity', unique and prior, from which secondary causes and the active intellect receive existence; lower existents 'emanate' from what is more perfect (§§2, 16). Written_profession ceiling allows 1.0; held at 0.7 because the record names alternative 2 (emanation continuity) and the Straussian reading that the emanation scheme is rhetorical cover (S1 §6; CODING_GUIDE contested readings)."
      rationale: "Draft judgment (one line): the first cause is above and prior to the cosmos, which proceeds from it by emanation through intermediate principles; God is not in nature but its source (Political Regime §§1–2, 20; S2 §4.1). Named alternative: 2, since emanation makes the cosmos a continuous outflow of the first cause rather than a separate creation. Straussian alternative (system-level, S1 §6): if the descent is rhetoric only, A would not be scored from these passages."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S5, locator: "Political Regime §§1–4, 10 (Butterworth 2015)"}, {source: S6, locator: "Selected Aphorisms 74 (Butterworth 2001, pp. 47–48)"}, {source: S2, locator: "§2.1; §3.1; §4.1"}]
      how_known: "Two of his own works on nature (P16), in Butterworth's scholarly translations: Political Regime (hierarchical natural order from the first cause; natural bodies; practical action 'by means of his volition'; 'nothing in natural existents is in vain') and Selected Aphorisms 74 (evil has no place in what is not due to human volition; natural worlds are good/ordered; evils are voluntary). Written_profession; held at 0.7 for named alternative 4 (CODING_GUIDE contested). Germann's reconstruction (S2) agrees and supplied the B 3 / free-will framing under P36; primary now carries the score."
      rationale: "Draft judgment (one line): nature runs as an ordered hierarchy from the first cause (Political Regime §§1–2, 10); Aphorism 74: 'Evil does not exist at all … in that whose existence is not at all due to human volition. Rather, all of that is good,' while both evils and the opposing goods 'are voluntary' — a lawful natural order with human volition/free will as the stated, limited exception, so B 3 (P30 #14; lens audit batch C #7). Named alternative: 4, if volition is read as itself natural within the same exceptionless order, or if Aphorism 74's 'all good' is taken as no-exception necessity without a real free-will carve-out."
    C_ledger:
      value: 4
      basis: scholarly_reconstruction
      certainty: 0.5
      support: single
      cites: [{source: S2, locator: "§2.1"}]
      how_known: "Scholarly reconstruction, so at most 0.5. Still a single scholarly source for the scored value; Perfect State afterlife passages not yet primary-checked this pass."
      rationale: "Draft judgment (one line): the afterlife is 'exclusively psychic or rather intellectual', with 'no room for corporeal resurrection'; its felicity is 'greater or lesser' 'in function of the excellence an individual has achieved during her life' (S2 §2.1): reward follows from the soul's own state, not from a judge. Named alternative: 3, since the excellence is measured against 'natural duties' that a ruler's religion prescribes."
    D_authority:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S7, locator: "Book of Religion 1 and 5 (Butterworth 2001)"}, {source: S2, locator: "§4.1"}, {source: S3, locator: "paragraph 3"}]
      how_known: "Book of Religion verified against Butterworth 2001 (primary check of the SEP quotation, P26). Religion is defined as opinions and actions prescribed by a first ruler; philosophy is the demonstrative counterpart (S2 §4.1 citing BR 5). Written_profession; held at 0.7 for named alternative 3."
      rationale: "Draft judgment (one line): religion is an instrument of rulership — 'opinions and actions … prescribed for a community by their first ruler' (Book of Religion 1, Butterworth) — while philosophy knows things as they are; philosophy is epistemically superior (S2 §4.1; S3). Named alternative: 3, because Germann adds that the superiority 'concerns only the respective epistemic levels' and that pragmatically religion is 'no less important than philosophy'."
    E_scope:
      value: 4
      basis: scholarly_reconstruction
      certainty: 0.5
      support: single
      cites: [{source: S2, locator: "§2.1; §4.1"}]
      how_known: "Scholarly reconstruction, so at most 0.5. Political Regime's one-world hierarchy (S5) supports one order but was not scored alone for E this pass."
      rationale: "Scored on the world's order (P7). Germann: 'there is one objective reality and, epistemologically, one objectively true account of it' (§4.1), and humans are subject to natural laws 'just like every other inhabitant of the sublunary world' (§2.1). One order for all; no favoured community in this-world events. Named alternative: 3, since the supralunary realm has its own (also regular) order."
  mid_basin: {value: true, certainty: 0.7, cites: [{source: S5, locator: "Political Regime §§1–2, 20"}, {source: S6, locator: "Selected Aphorisms 74"}], how_known: "P4: A_locus 1 ≤ 1 and B_cause 3 ≥ 3, both at certainty 0.7 (written_profession, contested caps). mid_basin certainty is the lower of the two axes (P10)."}
  statements:
    - text: "Religion is opinions and actions, determined and restricted with stipulations and prescribed for a community by their first ruler, who seeks to obtain through their practicing it a specific purpose with respect to them or by means of them. …. If the first ruler is virtuous and his rulership truly virtuous, then in what he prescribes he seeks only to obtain, for himself and for everyone under his rulership, the ultimate happiness that is truly happiness; and that religion will be virtuous religion."
      cites: [{source: S7, locator: "Book of Religion 1 (Butterworth 2001, p. 93)"}]
      context: "Opening definition in the Book of Religion."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-23
      note: "Primary check (P26): wording follows Butterworth 2001 ('virtuous' not Germann's 'excellent'/'slightly modified'). Undated."
    - text: "The first [cause] is what ought to be believed to be the deity. It is the proximate cause for the existence of the secondary [causes] and for the existence of the active intellect."
      cites: [{source: S5, locator: "Political Regime §2 (Butterworth 2015)"}]
      context: "Opening metaphysical ranking of principles."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-23
      note: "Butterworth translation; undated (among his later works per S1)."
    - text: "Evil does not exist at all, not in anything of these worlds and, in general, in that whose existence is not at all due to human volition. Rather, all of that is good. …. So both evils are voluntary and, similarly, the two goods opposite to them."
      cites: [{source: S6, locator: "Selected Aphorisms 74 (Butterworth 2001, pp. 47–48)"}]
      context: "Aphorism on evil, good, and volition in the natural worlds vs human action."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-23
      note: "Butterworth translation from Najjar's Arabic edition. Undated."
    - text: "By the practical, a human being becomes cognizant of what is such as to be carried out by means of his volition. …. Nothing in natural existents is in vain."
      cites: [{source: S5, locator: "Political Regime §§4, 10 (Butterworth 2015)"}]
      context: "Rational faculties; form and material in natural bodies."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-23
      note: "Two short excerpts from the same treatise, joined for the B rationale (volition vs natural order)."
  changes_over_life: []
  coder_notes: "Deepen 2026-10-23: A, B and D now rest on Butterworth scholarly translations of Political Regime, Selected Aphorisms and Book of Religion (written_profession at 0.7 under contested caps). C and E stay scholarly_reconstruction at 0.5 (single Germann). The Straussian dispute (S1 §6) remains named: it caps A/system and is why certainty is not 1.0. mid_basin now true under P4. Not a scientist under P30 (few physics texts; B from philosophical account of nature, P16). Coder's call: region of birth Central Asia at 0.5 with South Asia named; childhood still largely UNKNOWN ('little that is really reliable', S1)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage:
    value: "Disputed: Persian (recent research) or Turkish"
    certainty: 0.5
    cites: [{source: S1, locator: "opening ('Some claimed he was Turkish but more recent research points to him being a Persian (Rudolph 2017)')"}, {source: S3, locator: "paragraph 2 ('his ethnic origin is a matter of dispute')"}]
    how_known: "Both sources say it is disputed."
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not in the sources read."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not in the sources read."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not in the sources read."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "No lasting work is dated in the sources read (P12, P29)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "First-lasting year UNKNOWN (P12)."}
  first_evidence_of_lio_type_views: {value: "Political Regime / Selected Aphorisms / Book of Religion (undated; among works commonly placed late)", year: UNKNOWN, certainty: 0.5, cites: [{source: S5, locator: "throughout"}, {source: S6, locator: "Aphorism 74"}, {source: S7, locator: "Book of Religion 1"}, {source: S1, locator: "opening (Perfect State and Political Regime may be among his latest)"}], how_known: "Primary texts now read, but still undated (P12); S1 notes Perfect State and Political Regime may be late. Year left UNKNOWN."}
  lio_views_relative_to_major_work: {value: "unclear", rationale: "Neither the views nor the works are dated.", certainty: 0.5, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "§4.1"}], how_known: "Undated texts."}
  worldview_during_major_work: {value: "Arabic Peripatetic philosophy with Neoplatonic emanation; religion as symbolic imitation of philosophy (on the majority reading)", certainty: 0.5, cites: [{source: S1, locator: "§6"}, {source: S2, locator: "§4.1"}], how_known: "Scholarly reconstruction; no change of view is recorded."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Demonstrative (Aristotelian syllogistic) philosophy is for him the highest knowledge, 'resulting in objective certitude' (S2 §4.1); logic is his main interest (S1).", certainty: 0.5, cites: [{source: S2, locator: "§4.1"}, {source: S1, locator: "opening; §3"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Nothing reliable on his education (S1)."}
  circle_present: {value: "partly", rationale: "Nature's laws flow from the first cause through intermediate principles (S2 §4.1), but the first cause stays above the cosmos.", certainty: 0.5, cites: [{source: S2, locator: "§4.1"}], how_known: "Coder's reading."}
  reading: "As belief, not finding: form present, circle partly; timing unknown."
  notes: ""

institutions:
  - {value: "Court of Sayf al-Dawla (Hamdanid)", role: "resident philosopher", years: "942–", kind: "patron or funder", certainty: 0.7, cites: [{source: S3, locator: "paragraph 2"}], how_known: "Britannica alone (P15); SEP gives Syria from 943."}
collaborators:
  - {value: "Aristotle (aristotle)", relation: "influenced by", note: "'the second master' after 'the first'", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "paragraphs 1, 3"}], how_known: "Two sources."}

review:
  roster_status_reason: {value: "Core in v8 (F 5: Claude, DeepSeek, Gemini, GPT, Grok).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 3"}], how_known: "Study roster."}
  controversies:
    - {value: "Whether his Neoplatonic emanation is his real view or a rhetorical cover (Straussian reading)", certainty: 0.7, cites: [{source: S1, locator: "§6"}], how_known: "SEP states the debate; still caps A/system at 0.7."}
  data_quality_flags:
    - "Birth 870 (SEP, 'probably') vs c. 878 (Britannica)."
    - "Residence after 942/943: Damascus (SEP) vs mostly Aleppo (Britannica)."
    - "Chart-moving this pass: A and B 0.5→0.7; support B single→corroborated; mid_basin false/BELOW→true; person-dot faded hollow → dark filled."
    - "Walzer Perfect State (1985) not read in full this pass; Political Regime and Selected Aphorisms carry the new primary load."
  open_questions:
    - "Read Walzer Perfect State (1985) for A/B/C primary parallels and any dating apparatus."
    - "Keep CLASS_THEISM at 0.5, or revisit system certainty once Perfect State is primary-checked?"
    - "Childhood / ethnic origin: ODNB-level biography or Rudolph 2017 for anything beyond SEP's 'little that is really reliable'."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Thérèse-Anne Druart"
    year: 2024
    citation: "Druart, Thérèse-Anne. \"al-Farabi.\" Stanford Encyclopedia of Philosophy, first published 15 July 2016, substantive revision 14 May 2024. https://plato.stanford.edu/entries/al-farabi/."
    url: "https://plato.stanford.edu/entries/al-farabi/"
    accessed: 2026-10-23
    source_quality: "reference entry"
    reliability_note: "Peer-reviewed reference article. Re-read 2026-10-23 for deepen (life, metaphysics debate, free will note in logic)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, collaborators]
  - id: S2
    type: secondary
    kind: encyclopedia
    author: "Nadja Germann"
    year: 2021
    citation: "Germann, Nadja. \"al-Farabi's Philosophy of Society and Religion.\" Stanford Encyclopedia of Philosophy, first published 15 June 2016, substantive revision 20 January 2021. https://plato.stanford.edu/entries/al-farabi-soc-rel/."
    url: "https://plato.stanford.edu/entries/al-farabi-soc-rel/"
    accessed: 2026-10-23
    source_quality: "scholarly reconstruction"
    reliability_note: "Peer-reviewed reference article; worldview reconstruction that framed B 3 (free will vs by nature). Re-read 2026-10-23; primary texts now carry A/B/D."
    used_for: [contribution, worldview, lane_b, collaborators]
  - id: S3
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"al-Fārābī.\" Encyclopaedia Britannica. https://www.britannica.com/biography/al-Farabi."
    url: "https://www.britannica.com/biography/al-Farabi"
    accessed: 2026-10-08
    source_quality: "reference entry"
    reliability_note: "Unsigned editors' article; first page read 2026-10-08. Re-fetch blocked (JS/Cloudflare) on 2026-10-23; prior facts retained."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, institutions, collaborators]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-08
    source_quality: "study roster"
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Al-Farabi"
    year: 2015
    citation: "Alfarabi. The Political Writings, Volume II: \"Political Regime\" and \"Summary of Plato's Laws\". Translated and annotated by Charles E. Butterworth. Ithaca: Cornell University Press, 2015. Political Regime §§1–4, 10, 16, 20."
    url: "https://cornellpress.cornell.edu/book/9780801453809/the-political-writings/"
    accessed: 2026-10-23
    source_quality: "primary / own words"
    reliability_note: "Scholarly English translation (Butterworth) of al-Siyāsa al-madaniyya. Scored passages verified 2026-10-23 against a complete online text of the Butterworth translation. Composition undated; S1 notes it may be among his later works."
    used_for: [worldview, timing]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Al-Farabi"
    year: 2001
    citation: "Alfarabi. The Political Writings: \"Selected Aphorisms\" and Other Texts. Translated and annotated by Charles E. Butterworth. Ithaca: Cornell University Press, 2001. Selected Aphorisms 74, pp. 47–48."
    url: "https://archive.org/details/alfarabipolitica0000fara_y5a9"
    accessed: 2026-10-23
    source_quality: "primary / own words"
    reliability_note: "Scholarly English translation from Najjar's Arabic edition. Aphorism 74 verified 2026-10-23 against the archive.org full text of the Butterworth volume."
    used_for: [worldview]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "Al-Farabi"
    year: 2001
    citation: "Alfarabi. \"Book of Religion.\" In The Political Writings: \"Selected Aphorisms\" and Other Texts, translated by Charles E. Butterworth, 93–113. Ithaca: Cornell University Press, 2001. Book of Religion 1 (and 5 as cited via S2)."
    url: "https://archive.org/details/alfarabipolitica0000fara_y5a9"
    accessed: 2026-10-23
    source_quality: "primary / own words"
    reliability_note: "Same Butterworth 2001 volume as S6; separate id because it is a distinct Farabi treatise. Opening definition verified against Butterworth (replaces SEP secondary quotation)."
    used_for: [worldview]
---

# Al-Farabi

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Al-Farabi (c. 870/878–950/951), 'the second master' after Aristotle, worked in Baghdad and Syria on logic, political philosophy and music [S1; S3]. Political Regime states a unique first cause ('the deity') from which existence emanates [S5]; Selected Aphorisms 74 places evil only in what is due to human volition, with the natural worlds all good [S6]; Book of Religion defines religion as opinions and actions prescribed by a first ruler [S7]. Draft: CLASS_THEISM 0.5; A 1 (0.7, corroborated); B 3 (0.7, corroborated); C 4 (0.5, single); D 4 (0.7, corroborated); E 4 (0.5, single); mid_basin true. Chart person-dot: dark filled (was faded hollow).

## Life and work

'We know little that is really reliable' [S1]. Born probably at Farab, moved young to Baghdad, to Syria in 942/943, died probably in Damascus [S1; S3].

## Contribution and impact

Logic and the classification of the sciences; political philosophy; the Great Book of Music [S1; S2; S3].

## Childhood and education

Not known [S1].

## Adult working worldview

Primary: Political Regime, Selected Aphorisms 74, Book of Religion [S5–S7]. Scholarly frame and Straussian contest [S1, §6; S2]. A 1 and B 3 at 0.7; mid_basin true.

## Heritage (context only)

Persian or Turkish, disputed [S1; S3].

## Timing

Works undated; timing UNKNOWN.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form present; circle partly [S1; S2].

## Open questions

- Walzer Perfect State (1985) full primary pass.
- System certainty for CLASS_THEISM after Perfect State.
- Childhood / Rudolph 2017 on ethnic origin.

## Research log

- 2026-10-08: Read SEP 'al-Farabi' (Druart 2024), SEP 'al-Farabi's Philosophy of Society and Religion' (Germann 2021) and Britannica (editors). No primary text read.
- 2026-10-23: Deepen D1 (queue #3). Re-read both SEP entries. Primary-checked Butterworth Political Regime (2015), Selected Aphorisms 74 and Book of Religion 1 (2001). Britannica re-fetch blocked (Cloudflare). P47 labels. No fallacy_catalog (Jason 2026-10-23).
