---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA2; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (skip catch-up 11/13; F3 rank 183). Needs: firm A/primary if attribution allows; P42 Rihlah/Ibn Juzayy; not scientist for B; do not force plot. Dual bio Wikipedia EN (S8, P50). P47 source_quality on S1–S8. Primary check: Fordham Medieval Sourcebook Gibb extracts (S6) — pilgrimage intention to Holy House and Tomb of the Prophet; 'If God decrees my death, it shall be on the road with my face set toward Mecca'; Medina salutation to Muhammad. Dunn UCLA keynote (S7): Juzayy prune/polish of language while reporting travels faithfully; Maliki family education; prison Qurʾān recitation / 'sufficient for us is God' (secondary). ORIAS (S4) re-read: Juzayy kept to his telling + borrowed place-descriptions (Jubayr) for Mecca/Medina/Damascus — creed lines are journey autobiography, not borrowed topography. primary_system ISLAM @0.5 written_profession (P42 Juzayy wording / Craft analogy cap); A 0 @0.5 single; B UNKNOWN (not scientist P30; no P16 nature-order); mid_basin UNKNOWN. Chart-moving NO (need A&B ≥0.7). Draft deepen report in drafts/ (untracked). No fallacy_catalog. No figures refresh."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "AA2 audit fixes (FAIL; v8's call on the auditor's advice, RQ-Z9-N1, P12): span 1353 -> 1355 at 0.5, alternative 1354; age 49 -> 51 (alt 50). Dated by the colophon, 'Its dictation was finished on 3rd Dhu'l-hijja 756 [December 9, 1355]' (Gibb's translation, new S3); Britannica's 'dictated in 1353' is impossible (he left Mali on 27 February 1353). The unsupported 1356 alternative and its source (Project MUSE excerpt) dropped. Not plotted."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA2, order P32: F 3, rank 183; roster status review). Basics from Britannica (students and scholars editions, body; the main site's Top Questions box not used, P26). The Rihlah was dictated to Ibn Juzayy, who 'embellished the simple prose of Ibn Baṭṭūṭah with an ornate style and fragments of poetry' (S2), so its wording is Ibn Juzayy's and its attribution to him as author is shared (P42). Dating: Britannica's Travels article says 'dictated in 1353'; a journal article (Project MUSE, 2024) has Ibn Juzayy completing it in 1356; Berkeley's ORIAS page puts the dictation after his 1354 return to Fez. The encyclopedia year is used at 0.5 (RQ-Z9-N1: a manuscript-era work dated from article text), with 1355/1356 as the alternative. No own-voice religious text read: primary_system UNKNOWN (lead ISLAM: Muslim jurist, pilgrimage, 'the traveler of Islam'); A UNKNOWN; not a scientist, B UNKNOWN; C, D, E UNKNOWN; mid_basin UNKNOWN. Span 1353, age 49. Not plotted. Draft, not reviewed."}

identity:
  id: ibn-battuta
  display_name: "Ibn Battuta"
  roster:
    canonical_name: "Ibn Battuta"
    rank: 183
    F: 3
    models: [Gemini, GPT, Grok]
    band: "core (3–4)"
    status: "review"
    field: "exploration"
    field_bucket: "exploration"
  full_name: {value: "Abu ʿAbd Allah Muhammad ibn ʿAbd Allah al-Lawati al-Tanji ibn Battutah", certainty: 0.7, cites: [{source: S1, locator: "para. 1"}, {source: S8, locator: "Name / Early life"}], how_known: "Britannica (students); Wikipedia EN corroborates Lawati/Tanji form (P50)."}
  native_name: {value: "ابن بطوطة", certainty: 0.5, cites: [{source: S1, locator: "heading"}], how_known: "Arabic spelling the coder's."}
  aliases:
    - {name: "Battuta-Ibn", kind: "roster alias"}
    - {name: "Ibn-Battuta", kind: "roster alias"}
    - {name: "Ibn Battutah", kind: "other"}

basics:
  birth:
    date: {value: "1304-02-24", certainty: 0.7, cites: [{source: S1, locator: "para. 1"}, {source: S8, locator: "Early life"}], how_known: "Britannica (students); Wikipedia EN same date (P50)."}
    place: {value: "Tangier", modern_name: "Tangier, Morocco", polity_then: "Marinid sultanate", certainty: 0.7, cites: [{source: S1, locator: "para. 1"}, {source: S8, locator: "Early life"}], how_known: "Britannica; Wikipedia."}
  death:
    date: {value: "1368", certainty: 0.5, cites: [{source: S7, locator: "biographical mentions / 1368 or 1369"}, {source: S8, locator: "summary / Britannica cite 1368/69 or 1377"}], how_known: "Dunn: brief biographical mentions say 1368 or 1369. Britannica keeps 1368/69 or 1377. Preferred 1368 at 0.5; alternatives 1369 and 1377."}
    place: {value: "Morocco", certainty: 0.5, cites: [{source: S7, locator: "Tangiers tomb tradition"}, {source: S1, locator: "text"}], how_known: "Dunn: tradition places remains in Tangier; inscription uncertain. Britannica: suggested buried in Tangier."}
  first_lasting_contribution_year: {value: 1355, certainty: 0.5, cites: [{source: S3, locator: "colophon"}, {source: S4, locator: "text"}], how_known: "The colophon (Gibb's translation, S3): 'Its dictation was finished on 3rd Dhu'l-hijja 756 [December 9, 1355]'. Alternative 1354, the start of the dictation range after his return to Fez in 1354 (S4; RQ-Z9-N1, P12). Britannica's 'dictated in 1353' (S2) is impossible: he left Mali only on 27 February 1353 (S3). v8's call on the auditor's advice (AA2)."}
  era_bucket: {value: "500 to 1399", certainty: 0.7, cites: [{source: S1, locator: "para. 1"}], how_known: "Born 1304; died c.1368/69 or 1377; every adult year in one bucket (P39)."}
  region_of_birth: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "para. 1"}], how_known: "Morocco (P3)."}
  region_of_work: {value: "Middle East and North Africa", certainty: 0.5, cites: [{source: S2, locator: "para. 1"}], how_known: "Travels across the Muslim world; dictated at Fez."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Arabic"], certainty: 0.7, cites: [{source: S2, locator: "heading"}], how_known: "Arabic title."}
  occupations: {value: ["traveller", "jurist (qadi)"], certainty: 0.7, cites: [{source: S1, locator: "para. 1, 3"}, {source: S7, locator: "qadi Delhi / Maldives"}, {source: S8, locator: "Early life"}], how_known: "Britannica; Dunn (Delhi and Maldives judgeships); Wikipedia."}

contribution:
  fields: {value: ["travel writing", "geography"], certainty: 0.7, cites: [{source: S2, locator: "para. 1"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Travels (Riḥlah, Tuḥfat al-nuẓẓār)", year: 1355, kind: "work", lasting: "'an important document shedding light on many aspects of the social, cultural, and political history of a great part of the Muslim world'; 'a major source for the histories of these areas' (S2, body)", certainty: 0.5, cites: [{source: S2, locator: "para. 1–2"}], how_known: "Britannica; dictated to and written up by Ibn Juzayy (P42); dated by the colophon, 9 December 1355 (S3), at 0.5, alternative 1354."}
  evidence_of_impact:
    - {value: "Major source for the histories of Asia Minor, East and West Africa, the Maldives and India", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S2, locator: "para. 2"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "arguable", rationale: "The lasting work is a travel record written up by another hand (S2); originality rests on the observation, not a new idea.", certainty: 0.5, cites: [{source: S2, locator: "para. 2"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Sunni Islam (Mālikī legal milieu)", certainty: 0.5, cites: [{source: S8, locator: "Early life"}, {source: S7, locator: "family of legal scholars / Maliki"}], how_known: "Wikipedia: family of Islamic legal scholars (qadis); Sunni Maliki school dominant in North Africa. Dunn: family of legal scholars; Maliki education. Heritage/context — not primary_system alone (ISLAM do_not_use_when: birth into Muslim society alone)."}
  family_religious_practice: {value: UNKNOWN, how_known: "Practice intensity not stated beyond legal-scholar household."}
  parents_and_household: []
  household_circumstances: {value: "Family of Islamic legal scholars (qadis) of the Lawata Berber clan; urban Tangier", certainty: 0.5, cites: [{source: S8, locator: "Early life"}, {source: S7, locator: "Al-Lawati / Berber origin; Tangiers"}], how_known: "Wikipedia and Dunn."}
  schooling:
    - {value: "Sunni Mālikī legal and religious education in Tangier (Qurʾān circle then advanced religious/legal sciences)", stage: other, run_by: "religious body", years: "to c.1325", certainty: 0.5, cites: [{source: S8, locator: "Early life"}, {source: S7, locator: "Maliki system; Quran lesson circle then advanced studies"}], how_known: "Wikipedia: studied at a Sunni Maliki school. Dunn: basic education in religious and legal sciences; Quran lesson circle then advanced studies. Stage 'other' (ibn-rushd pattern); not university."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["Arabic"], certainty: 0.5, cites: [{source: S7, locator: "Arabic native language; no evidence he spoke Berber"}], how_known: "Dunn: Arabic-speaking city Arab culture; Berber tribal name only."}
  notable_events:
    - {value: "Left Tangier 14 June 1325 (age ~21) intending pilgrimage to Mecca and the Prophet's tomb at Medina", year: 1325, certainty: 0.5, cites: [{source: S6, locator: "p. 43 opening"}], how_known: "Gibb via Fordham; Rihlah wording shared with Juzayy (P42)."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1355", certainty: 0.5, cites: [{source: S3, locator: "colophon"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Sunni Islam — Mālikī school; qadi (Delhi, Maldives, later Morocco)", years: "working years", certainty: 0.5, cites: [{source: S7, locator: "Maliki; qadi Delhi / Maldives"}, {source: S8, locator: "Early life"}, {source: S1, locator: "para. 3"}], how_known: "Office and school are public record; primary_system rests on attributed Rihlah faith lines, not affiliation alone."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not a scientist; no science–religion relation scored."}
  primary_system:
    value: ISLAM
    basis: written_profession
    certainty: 0.5
    cites: [{source: S6, locator: "p. 43 opening — Pilgrimage / Tomb of the Prophet; God decrees my death"}, {source: S6, locator: "Medina — salutation to Muhammad"}, {source: S7, locator: "Juzayy prune/polish; prison Qurʾān / 'sufficient for us is God'"}, {source: S2, locator: "embellished / ornate style (P42)"}]
    how_known: "Deepen D1: scholars treat the Rihlah's autobiographical journey narrative as his dictation (S7 Dunn: Juzayy to report travels faithfully while pruning and polishing language; S4 ORIAS: generally kept to his telling). Fordham/Gibb (S6): left Tangier 'with the intention of making the Pilgrimage to the Holy House [at Mecca] and the Tomb of the Prophet [at Medina]'; on fever, 'If God decrees my death, it shall be on the road with my face set toward Mecca'; at Medina, salutation to 'Muhammad' as Prophet and intercessor. Dunn (S7, secondary): imprisoned under Ibn Tughluq he recited 'sufficient for us is God and excellent the protector' and the Qurʾān cover to cover. Meets ISLAM use_when (Qurʾān, Prophet, personal God) beyond birth-alone. Certainty capped at 0.5: wording is Juzayy's polish (S2/S7; P42 shared authorship — Craft/Stravinsky analogy). Contested alt BELOW_THRESHOLD if one holds Juzayy invented the creed framing."
    rationale: "ISLAM use_when: Muslim belief in attributed own writing (Prophet's tomb and pilgrimage; Qurʾān recitation; God as decreer/protector) without falsafa. CLASS_THEISM rejected: no Aristotelian-Neoplatonic natural theology. CLTHEI not needed as primary when ISLAM fits the confession. Birth into a Muslim society alone is insufficient (do_not_use_when); the scored lines go beyond affiliation. Named alternative BELOW_THRESHOLD keeps ceiling at 0.5 (§3 / P42)."
    alternatives:
      - {value: BELOW_THRESHOLD, note: "If Juzayy's literary polish is treated as inventing the creed lines rather than reporting Battuta's dictation, no attributable own-voice profession remains at ≥0.5.", cites: [{source: S2, locator: "embellished the simple prose"}, {source: S7, locator: "pruning and polishing of its language"}]}
  secondary_system: {value: UNKNOWN, how_known: "Sufi saint/baraka devotion (S7) stays practice within ISLAM (al-Ghazali / Rumi pattern); not a separate scored system."}
  candidate_codes_considered:
    - {code: ISLAM, reason: "Coded at 0.5 written_profession under P42 Juzayy cap (S6, S7)."}
    - {code: CLASS_THEISM, reason: "Rejected: no falsafa / Necessary Being natural theology in what was read."}
    - {code: CLTHEI, reason: "Rejected as primary: interventionist personal God language sits inside ordinary Sunni confession; ISLAM fits."}
  lio_axes:
    A_locus:
      value: 0
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S6, locator: "p. 43 — 'If God decrees my death… face set toward Mecca'"}, {source: S7, locator: "'sufficient for us is God and excellent the protector' (prison; secondary)"}]
      how_known: "Deepen D1: Gibb via Fordham — personal God who decrees death on the pilgrimage road (transcendent person outside the world who decides events): A 0. Dunn (S7) independently reports the prison protector prayer from the Rihlah. Support corroborated (P48): S6 primary extract + S7 scholarly account agree on personal intervening God. Certainty 0.5 under P42 Juzayy wording (Craft analogy). Named alternative 1 keeps ceiling ≤0.7; P42 already caps at 0.5."
      rationale: "A separate personal God who decrees and protects: 0. Alternative 1: formulaic pilgrimage piety without a strong locus claim once Juzayy's polish is discounted."
      alternatives:
        - {value: 1, note: "Formulaic / limited interventionist reading of the same decree and protector lines.", cites: [{source: S6, locator: "p. 43 God decrees my death"}]}
    B_cause: {value: UNKNOWN, how_known: "Deepen D1: not a scientist (P30 — travel writing / geography observation, no theory of physical systems). No P16 nature-order account in own words. Prison petitionary prayer and divine-decree lines are A evidence; own petitionary prayer is not a statement about nature (P16 addendum — Austen). Nile/geography descriptions are itinerary, not lawfulness doctrine. Do not invent B."}
    C_ledger: {value: UNKNOWN, how_known: "Not scored this pass (P19)."}
    D_authority: {value: UNKNOWN, how_known: "Not scored this pass (P19)."}
    E_scope: {value: UNKNOWN, how_known: "Not scored this pass (P19)."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN, so the P4 test cannot be applied (P19). A 0 @0.5 would meet A ≤ 1 if certainty were ≥0.7, but B is missing and A is below the mid-basin certainty floor."}
  statements:
    - text: "I left Tangier, my birthplace, on Thursday, 2nd Rajab 725 [June 14, 1325], being at that time twenty-two years of age [22 lunar years; 21 and 4 months by solar reckoning], with the intention of making the Pilgrimage to the Holy House [at Mecca] and the Tomb of the Prophet [at Medina]."
      cites: [{source: S6, locator: "p. 43 opening"}]
      date: "1325"
      context: "Rihlah opening; start of first journey. Dictated c.1354–1355; working-years evidence for adult creed (P20/P31 — adult life inside span of the one lasting work)."
      axes: [A_locus]
      kind: "autobiography"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Gibb 1929 selection via Fordham Medieval Sourcebook (P21 unofficial-web). P42: wording polished by Ibn Juzayy; scholars treat the autobiographical journey frame as Battuta's."
    - text: "If God decrees my death, it shall be on the road with my face set toward Mecca."
      cites: [{source: S6, locator: "pp. 43–45 Bijaya fever"}]
      date: "1325"
      context: "Reply when advised to halt for fever at Bijaya en route to Tunis/Mecca."
      axes: [A_locus]
      kind: "autobiography"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Same Gibb/Fordham extract; P42 Juzayy polish."
    - text: "Having paid our meed of salutation to the lord of men from first to last, the intercessor for sinners, the Prophet of Mecca, Muhammad, as well as to his two companions who share his grave, Abu Bakr and 'Omar, we returned to our camp, rejoicing at this great favour bestowed upon us, praising God for our having reached the former abodes and the magnificent sanctuaries of His holy Prophet…"
      cites: [{source: S6, locator: "pp. 74–77 Medina"}]
      date: "1326"
      context: "First arrival at the Prophet's mosque in Medina."
      axes: [A_locus]
      kind: "autobiography"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Prophet veneration for ISLAM use_when; P42 Juzayy polish. Not used alone for A (locus), but corroborates Muslim profession."
  changes_over_life: []
  coder_notes: "Deepen D1: P42 caps mediated Rihlah first-person at 0.5 (Craft analogy). Borrowed Jubayr topography (ORIAS) not used as creed. Not a scientist — B stays UNKNOWN; do not force plot. Lane A public-record only; Lane B unused for beliefs-as-findings."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Arabised Berber (Lawata clan)", certainty: 0.5, cites: [{source: S8, locator: "Early life"}, {source: S7, locator: "Al-Lawati; Berber origin; Arabic speech/culture"}], how_known: "Wikipedia: Arabised Berber descent, Lawata clan. Dunn: Berber origin; Arabic-speaking city culture."}
  religious_heritage_by_birth: {value: "Muslim (Sunni Mālikī legal family)", certainty: 0.5, cites: [{source: S8, locator: "Early life"}, {source: S7, locator: "family of legal scholars"}], how_known: "Wikipedia and Dunn; not a scored adult primary_system by itself."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not applicable / not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Maliki schooling noted under childhood.schooling; no separate catechism label."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1355", certainty: 0.5, cites: [{source: S3, locator: "colophon"}], how_known: "The one listed lasting work (P29), dated by the colophon (S3); alternative 1354 (S4)."}
  age_at_first_lasting_contribution: {value: 51, certainty: 0.5, cites: [{source: S1, locator: "para. 1"}, {source: S3, locator: "colophon"}], how_known: "1355 − 1304 = 51 (P30 year difference); 50 on the 1354 alternative."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None (interventionist theism is not LIO-type)."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S6, locator: "p. 43 God decrees my death"}], how_known: "Personal intervening God; no lawful-order LIO statement."}
  worldview_during_major_work: {value: "ISLAM (mediated Rihlah); A 0 @0.5; B UNKNOWN", certainty: 0.5, cites: [{source: S6, locator: "p. 43"}, {source: S7, locator: "Juzayy / Maliki"}], how_known: "As primary_system and axes."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Narrative travel account (S2); no geometric form in the lasting contribution.", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "no", rationale: "Personal intervening God (decree/protector); no exceptionless lawful-order statement (B UNKNOWN).", certainty: 0.5, cites: [{source: S6, locator: "p. 43"}], how_known: "Coder's reading."}
  reading: "Interventionist Muslim traveler-jurist on mediated evidence at 0.5; not a mid-basin case (B missing). H1 stress test does not apply — not plotted."
  notes: "Lane B only; not a finding."

institutions: []
collaborators:
  - {value: "Ibn Juzayy", relation: "collaborator", note: "wrote up the dictated Rihlah (prune/polish language; P42 shared wording)", certainty: 0.7, cites: [{source: S2, locator: "para. 1"}, {source: S7, locator: "pruning and polishing"}], how_known: "Britannica; Dunn."}

review:
  roster_status_reason: {value: "Review in v8 (F 3).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 183"}], how_known: "Study roster."}
  controversies:
    - {value: "Rihlah wording shared with Ibn Juzayy; some place-descriptions borrowed from Ibn Jubayr / al-Abdari (ORIAS). Creed scores capped at 0.5 (P42).", certainty: 0.7, cites: [{source: S2, locator: "embellished"}, {source: S4, locator: "Writing the Rihla"}, {source: S7, locator: "prune/polish"}], how_known: "Britannica, ORIAS, Dunn."}
  data_quality_flags:
    - "Text written up by Ibn Juzayy (P42); certainty ceiling 0.5 for worldview scores from Rihlah wording."
    - "Britannica's 1353 conflicts with the colophon (1355)."
    - "Fordham/Gibb extracts are unofficial web copies (P21)."
  open_questions:
    - "Full Hakluyt Society Gibb (or Defrémery-Sanguinetti) for prison-prayer Arabic locus and further A/B nature remarks."
    - "Whether any document in Battuta's own hand exists for a written_profession lift above 0.5."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Britannica Editors"
    citation: "'Ibn Battutah.' Britannica (students edition). https://kids.britannica.com/students/article/Ibn-Battutah/275019"
    url: "https://kids.britannica.com/students/article/Ibn-Battutah/275019"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Encyclopedia body (P47). Cloudflare wall on re-fetch this pass; create-pass body excerpts retained."
    used_for: [identity, basics, worldview]
  - id: S2
    type: tertiary
    kind: "encyclopedia"
    author: "Britannica Editors"
    citation: "'Travels.' Britannica (scholars edition). https://kids.britannica.com/scholars/article/Travels/486948"
    url: "https://kids.britannica.com/scholars/article/Travels/486948"
    accessed: 2026-10-19
    source_quality: "reference entry"
    reliability_note: "Encyclopedia article, read in full on create pass; Juzayy embellishment line."
    used_for: [basics, contribution, timing, collaborators, worldview]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Ibn Battuta (dictated to Ibn Juzayy; trans. H. A. R. Gibb)"
    citation: "Ibn Battuta. Travels in Asia and Africa 1325–1354, trans. H. A. R. Gibb (1929), pp. 323–339 extract (Mali / colophon), as given in A. S. Chughtai, 'Ibn Battuta', Topics in Global History, John Jay College (CUNY), from the Fordham Medieval Sourcebook. https://jjcweb.jjay.cuny.edu/history/worldspring09/ibnbattuta.html"
    url: "https://jjcweb.jjay.cuny.edu/history/worldspring09/ibnbattuta.html"
    accessed: 2026-10-19
    source_quality: "unofficial web copy"
    reliability_note: "Course page; Gibb translation of Mali section and colophon (P21 unofficial-web). Used for dates; faith quotes taken from S6 Fordham."
    used_for: [basics, timing]
  - id: S4
    type: secondary
    kind: "institutional page"
    author: "ORIAS, University of California, Berkeley"
    citation: "'Writing the Rihla: 1355.' The Travels of Ibn Battuta, ORIAS. https://orias.berkeley.edu/resources-teachers/travels-ibn-battuta/journey/writing-rihla-1355"
    url: "https://orias.berkeley.edu/resources-teachers/travels-ibn-battuta/journey/writing-rihla-1355"
    accessed: 2026-10-24
    source_quality: "scholarly reconstruction"
    reliability_note: "Teaching resource (Berkeley ORIAS); Juzayy kept to Battuta's telling; borrowed Jubayr descriptions for Mecca/Medina/Damascus."
    used_for: [basics, worldview]
  - id: S5
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [review]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Ibn Battuta (dictated to Ibn Juzayy; trans. H. A. R. Gibb)"
    citation: "Ibn Battuta. Travels in Asia and Africa 1325–1354, selections, trans. H. A. R. Gibb (1929). Internet History Sourcebooks Project, Fordham University. https://sourcebooks.fordham.edu/source/1354-ibnbattuta.asp"
    url: "https://sourcebooks.fordham.edu/source/1354-ibnbattuta.asp"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Gibb selection hosted by Fordham (P21 unofficial-web; P42 Juzayy wording). Primary for pilgrimage opening, God-decrees-death, Medina Prophet salutation."
    used_for: [worldview, childhood]
  - id: S7
    type: secondary
    kind: "other"
    author: "Ross E. Dunn"
    citation: "Ross Dunn. Keynote address at Ibn Battuta event (drawing on The Adventures of Ibn Battuta: A Muslim Traveler of the 14th Century, University of California Press). UCLA Center for Chinese Studies, published 2 March 2005. https://www.international.ucla.edu/ccs/article/21336"
    url: "https://www.international.ucla.edu/ccs/article/21336"
    accessed: 2026-10-24
    source_quality: "scholarly reconstruction"
    reliability_note: "Author of the standard English biography; Juzayy prune/polish quote; Maliki education; prison Qurʾān episode; death 1368/69."
    used_for: [worldview, childhood, heritage, basics, collaborators]
  - id: S8
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "'Ibn Battuta.' Wikipedia EN. https://en.wikipedia.org/wiki/Ibn_Battuta"
    url: "https://en.wikipedia.org/wiki/Ibn_Battuta"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Dual bio (P50) for Early life (Lawata, Maliki qadi family, 24 Feb 1304). Not used alone for worldview scores."
    used_for: [identity, basics, childhood, heritage]
---

## Summary

Ibn Battuta (1304–c.1368), Maghrebi Muslim traveller and Mālikī jurist [S1, S8]. Deepen D1: primary_system ISLAM @0.5 (mediated Rihlah; P42); A 0 @0.5; B UNKNOWN; not plotted.

## Life and work

Tangier; hajj and decades of travel across Dar al-Islam; dictated the Rihlah at Fez with Ibn Juzayy [S1, S2, S7].

## Contribution and impact

The Rihlah as major source for social and political history of much of the 14th-century Muslim world [S2].

## Childhood and education

Lawata Berber family of qadis; Sunni Mālikī education in Tangier [S7, S8].

## Adult working worldview

Attributed Rihlah autobiography (Gibb/Fordham): pilgrimage to the Holy House and Tomb of the Prophet; God who decrees death toward Mecca; Prophet veneration at Medina [S6]. Juzayy polish caps certainty at 0.5 [S2, S7, P42]. Not a scientist; B UNKNOWN.

## Heritage (context only)

Arabised Berber (Lawata); Muslim Mālikī legal household — context only, not the scored code [S7, S8].

## Timing

1355, age 51 (0.5) [S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Interventionist Muslim traveler-jurist on mediated evidence; not mid-basin (B missing); not plotted.

## Open questions

- Full Gibb / Arabic for further nature-order lines.
- Own-hand document to lift above 0.5.

## Research log

- 2026-10-24: Deepen D1 (skip 11/13). Fordham Gibb (S6); Dunn UCLA (S7); Wikipedia Early life (S8); ORIAS re-read (S4). primary ISLAM @0.5; A 0 @0.5; B UNKNOWN; Chart NO. No fallacy_catalog; no figures/.
- 2026-10-19: AA2 audit fixes (FAIL; v8's call on the auditor's advice, RQ-Z9-N1, P12): span 1353 -> 1355 at 0.5, alternative 1354; age 49 -> 51 (alt 50). Dated by the colophon, 'Its dictation was finished on 3rd Dhu'l-hijja 756 [December 9, 1355]' (Gibb's translation, new S3); Britannica's 'dictated in 1353' is impossible (he left Mali on 27 February 1353). The unsupported 1356 alternative and its source (Project MUSE excerpt) dropped. Not plotted.
- 2026-10-19: Read Britannica (students, scholars); the colophon in Gibb's translation (course page); ORIAS excerpt.
