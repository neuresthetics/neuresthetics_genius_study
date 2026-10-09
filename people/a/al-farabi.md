---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch C)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-08
  last_updated: 2026-10-08
  change_log:
    - {date: 2026-10-08, by: "Grok Bot", summary: "Record created (stage 3 batch C, order P32). Basics from SEP 'al-Farabi' (Druart 2024) and Britannica (editors); worldview from SEP 'al-Farabi's Philosophy of Society and Religion' (Germann 2021), a scholarly reconstruction; his own words only as SEP quotes them (secondary quotation, primary check pending). Works undated, so first-lasting year, span and age UNKNOWN (P12). primary_system CLASS_THEISM 0.5 (Straussian reading named); A 1, B 4, C 4, D 4, E 4, all 0.5 (scholarly_reconstruction); mid_basin BELOW_THRESHOLD. Draft, not reviewed."}

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
  native_name: {value: TODO}
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
    how_known: "Scholars place him in Arabic Peripatetic philosophy: a single first cause from which the cosmos proceeds by Neoplatonic emanation (S1 §6; S2 §4.1: 'ultimately all founded in a single, first cause'), with the cosmos 'the effect of the over-perfect first cause' (S2 §3.1). The CLASS_THEISM system file names 'Arabic falsafa (al-Farabi, Avicenna, Averroes)' as a parent tradition. Scholarly reconstruction, so at most 0.5."
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
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S1, locator: "§6"}, {source: S2, locator: "§3.1; §4.1"}]
      how_known: "Scholarly reconstruction, so at most 0.5."
      rationale: "Draft judgment (one line): the first cause is above and prior to the cosmos, which proceeds from it by emanation through intermediate principles ('intelligence, soul, and matter', S2 §4.1); God is not in nature but its source. Named alternative: 2, since emanation makes the cosmos a continuous outflow of the first cause rather than a separate creation."
    B_cause:
      value: 4
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S2, locator: "§2.1; §3.1; §4.1"}]
      how_known: "Scholarly reconstruction of his account of nature (P16), so at most 0.5."
      rationale: "Draft judgment (one line): Germann: human beings, like every sublunary being, 'are subject to the natural laws determining corporeal substances' (§2.1); each part of the cosmos has a function that keeps it 'running smoothly, without interruptions and disturbances' (§3.1); 'the things constituting reality, their behavior, and the underlying natural laws' are effects of principles 'ultimately all founded in a single, first cause' (§4.1). No miracle or intervention appears in the reconstruction. Named alternative: 3, since the active intellect's influence on the human intellect (§2.1) is a non-bodily cause, though a regular one."
    C_ledger:
      value: 4
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S2, locator: "§2.1"}]
      how_known: "Scholarly reconstruction, so at most 0.5."
      rationale: "Draft judgment (one line): the afterlife is 'exclusively psychic or rather intellectual', with 'no room for corporeal resurrection'; its felicity is 'greater or lesser' 'in function of the excellence an individual has achieved during her life' (S2 §2.1): reward follows from the soul's own state, not from a judge. Named alternative: 3, since the excellence is measured against 'natural duties' that a ruler's religion prescribes."
    D_authority:
      value: 4
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S2, locator: "§4.1"}, {source: S3, locator: "paragraph 3"}]
      how_known: "Scholarly reconstruction, so at most 0.5."
      rationale: "Draft judgment (one line): 'philosophy is therefore superior to religion, as is often underscored by scholarship and acknowledged by al-Farabi himself' (S2 §4.1, citing Book of Religion 5); 'He saw human reason as being superior to revelation' (S3). Religion is symbolic representation for those who cannot grasp things 'as they really are'. Named alternative: 3, because Germann adds that the superiority 'concerns only the respective epistemic levels' and that pragmatically religion is 'no less important than philosophy'."
    E_scope:
      value: 4
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S2, locator: "§2.1; §4.1"}]
      how_known: "Scholarly reconstruction, so at most 0.5."
      rationale: "Scored on the world's order (P7). Germann: 'there is one objective reality and, epistemologically, one objectively true account of it' (§4.1), and humans are subject to natural laws 'just like every other inhabitant of the sublunary world' (§2.1). One order for all; no favoured community in this-world events. Named alternative: 3, since the supralunary realm has its own (also regular) order."
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus 1 and B_cause 4 are both scored only at 0.5 (scholarly_reconstruction), so the P4 test is not met (§6, P19)."}
  statements:
    - text: "Religion is opinions and actions, determined and restricted with stipulations and prescribed for a community by their first ruler, who seeks to obtain through their practicing it a specific purpose with respect to them or by means of them. …. If the first ruler is excellent and his rulership truly excellent, then in what he prescribes he seeks only to obtain, for himself and for everyone under his rulership, the ultimate happiness that is truly happiness; and that religion will be the excellent religion."
      cites: [{source: S2, locator: "§4.1 (quoting Book of Religion 1: 93, 'slightly modified')"}]
      context: "Opening definition in the Book of Religion, in English translation as given by Germann."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-08
      note: "Primary check pending (P26): translation as modified by the SEP author; the Arabic and Mahdi's translation were not read. Undated."
  changes_over_life: []
  coder_notes: "Every axis rests on scholarly reconstruction (Germann for B–E; Druart for the emanation), so every score is capped at 0.5 and mid_basin cannot be met. His own words appear only as SEP quotes them in translation (secondary quotation; primary check pending). The scholarly dispute (S1 §6) is whether the Neoplatonic emanation is his real view (Gutas, Menn, Druart) or a rhetorical cover for a philosophy-first politics (Straussians, Butterworth); either reading keeps B, D and E at the lawful end, but it changes the system code and A. Not a scientist under P30: the sources read do not list a lasting theory or result about physical or natural systems (SEP §5 says few physics texts survive); B rests on a reconstruction of his statements about nature (P16). Coder's call (CODING_GUIDE §8): region of birth Central Asia at 0.5 with South Asia named, since Farab/Farayb is not located by the sources."

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
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "The texts behind the reconstructed views are undated (P12)."}
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
    - {value: "Whether his Neoplatonic emanation is his real view or a rhetorical cover (Straussian reading)", certainty: 0.7, cites: [{source: S1, locator: "§6"}], how_known: "SEP states the debate."}
  data_quality_flags:
    - "Birth 870 (SEP, 'probably') vs c. 878 (Britannica)."
    - "Residence after 942/943: Damascus (SEP) vs mostly Aleppo (Britannica)."
    - "All quotations of his own words are secondary (SEP translations)."
  open_questions:
    - "Read the Book of Religion and the Perfect State (Walzer 1985) for primary quotations; any dating of the works."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Thérèse-Anne Druart"
    year: 2024
    citation: "Druart, Thérèse-Anne. \"al-Farabi.\" Stanford Encyclopedia of Philosophy, first published 15 July 2016, substantive revision 14 May 2024. https://plato.stanford.edu/entries/al-farabi/."
    url: "https://plato.stanford.edu/entries/al-farabi/"
    accessed: 2026-10-08
    reliability_note: "Peer-reviewed reference article."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, collaborators]
  - id: S2
    type: secondary
    kind: encyclopedia
    author: "Nadja Germann"
    year: 2021
    citation: "Germann, Nadja. \"al-Farabi's Philosophy of Society and Religion.\" Stanford Encyclopedia of Philosophy, first published 15 June 2016, substantive revision 20 January 2021. https://plato.stanford.edu/entries/al-farabi-soc-rel/."
    url: "https://plato.stanford.edu/entries/al-farabi-soc-rel/"
    accessed: 2026-10-08
    reliability_note: "Peer-reviewed reference article; source of the worldview reconstruction and of the translated quotation."
    used_for: [contribution, worldview, lane_b, collaborators]
  - id: S3
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"al-Fārābī.\" Encyclopaedia Britannica. https://www.britannica.com/biography/al-Farabi."
    url: "https://www.britannica.com/biography/al-Farabi"
    accessed: 2026-10-08
    reliability_note: "Unsigned editors' article; first page read."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, institutions, collaborators]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-08
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# Al-Farabi

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Al-Farabi (c. 870/878–950/951), 'the second master' after Aristotle, worked in Baghdad and Syria on logic, political philosophy and music [S1; S3]. On the majority scholarly reading he held a single first cause from which the cosmos proceeds by emanation, a nature governed by natural laws, a purely intellectual afterlife, and philosophy above religion [S1, §6; S2]. Draft: CLASS_THEISM 0.5; A 1, B 4, C 4, D 4, E 4, all 0.5 (scholarly reconstruction); mid_basin BELOW_THRESHOLD.

## Life and work

'We know little that is really reliable' [S1]. Born probably at Farab, moved young to Baghdad, to Syria in 942/943, died probably in Damascus [S1; S3].

## Contribution and impact

Logic and the classification of the sciences; political philosophy; the Great Book of Music [S1; S2; S3].

## Childhood and education

Not known [S1].

## Adult working worldview

Scholarly reconstruction only [S2]; contested by the Straussian reading [S1, §6].

## Heritage (context only)

Persian or Turkish, disputed [S1; S3].

## Timing

Works undated; timing UNKNOWN.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form present; circle partly [S1; S2].

## Open questions

- Primary texts in translation.

## Research log

- 2026-10-08: Read SEP 'al-Farabi' (Druart 2024), SEP 'al-Farabi's Philosophy of Society and Religion' (Germann 2021) and Britannica (editors). No primary text read.
