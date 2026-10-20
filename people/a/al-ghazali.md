---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z2)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z2 audit fixes (blind audit /workspace/genius_study_audit/gs_f70a593_Z2/run1/): Z2-21: ISLAM 0.7 -> 0.5, basis scholarly_reconstruction (SEP's summary, no quotation of his own). Z2-23 / RQ-Z2-2 (v8's call on the auditor's advice): the Revival's year is UNKNOWN and the span end is UNKNOWN (P12). A and B how_known now say 0.5 is the pending-check cap. Plot unchanged (A 0 / B 3, faded)."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z2, order P32: F 3, rank 141). Source: SEP 'al-Ghazali' (Frank Griffel, rev. 2026), with his own words as secondary quotations of Marmura's translation of the Incoherence (2nd ed. 2000; primary check pending, §7): the connection between cause and effect 'is not necessary ... according to us' and is due to 'the prior decision (taqdīr) of God' (p. 166); 'within divine power to create satiety without eating' (p. 166); for prophets God 'suspends His habit' (Griffel on p. 171). Span 1095–1106 at 0.5. primary_system ISLAM (0.7); A 0 (0.5, alt 1); B 3 (0.5, alt 2); C UNKNOWN; D BELOW_THRESHOLD; E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Plotted (faded) at the next chart refresh. Draft, not reviewed."}

identity:
  id: al-ghazali
  display_name: "Al-Ghazali"
  roster:
    canonical_name: "Al-Ghazali"
    rank: 141
    F: 3
    models: [Claude, DeepSeek, Gemini]
    band: "core (3–4)"
    status: core
    field: philosophy-theology
    field_bucket: philosophy
  full_name: {value: "Abū Ḥāmid Muḥammad ibn Muḥammad al-Ghazālī", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
  native_name: {value: "Abū Ḥāmid Muḥammad ibn Muḥammad al-Ghazālī", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP (transliterated Arabic)."}
  aliases: []

basics:
  birth:
    date: {value: "1056", calendar: gregorian, certainty: 0.5, cites: [{source: S1, locator: "§1 Life"}], how_known: "His letters and autobiography indicate 1055 or 1056 (Griffel 2009, per S1); medieval historians say 1058 or 1059. A dispute, so 0.5.", alternatives: [{value: "1058", note: "Medieval historians: 1058 or 1059.", cites: [{source: S1, locator: "§1 Life"}]}]}
    place: {value: "Ṭabarān-Ṭūs", modern_name: "near Mashhad, Iran", polity_then: "Seljuq empire", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP: '15 miles north of modern Meshed, NE Iran'."}
  death:
    date: {value: "1111-12", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP: died in December 1111."}
    place: {value: "Ṭūs", modern_name: "near Mashhad, Iran", polity_then: "Seljuq empire", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
  first_lasting_contribution_year: {value: 1095, certainty: 0.5, cites: [{source: S1, locator: "§2 ('published around 1095 a number of books' on falsafa and the Ismāʿīlites)"}], how_known: "The Incoherence of the Philosophers, written in his third year at the Baghdad Niẓāmiyya (appointed 1091) and published 'around 1095' (S1), so 0.5."}
  era_bucket: {value: "500 to 1399", certainty: 1.0, cites: [{source: S1, locator: "§1 Life"}], how_known: "Every adult year falls in '500 to 1399' (P2)."}
  region_of_birth: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "Iran, which the study places in MENA (P3)."}
  region_of_work: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "Nishapur, Baghdad, Damascus, Jerusalem, Ṭūs."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "As recorded."}
  languages_of_work: {value: ["Arabic"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Arabic works throughout S1."}
  occupations: {value: ["Ashʿarite theologian", "jurist", "professor (Niẓāmiyya madrasas of Baghdad and Nishapur)", "Sufi"], certainty: 0.7, cites: [{source: S1, locator: "opening; §1 Life"}], how_known: "SEP."}

contribution:
  fields: {value: ["theology (kalām)", "philosophy", "law", "Sufism"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  lasting_original_contributions:
    - {value: "The Incoherence of the Philosophers (Tahāfut al-falāsifa)", year: 1095, kind: work, lasting: "his critique of falsafa and its account of causality, discussed in S1 §7", certainty: 0.5, cites: [{source: S1, locator: "§2; §7"}], how_known: "SEP; 'around 1095'."}
    - {value: "The Revival of the Religious Sciences (Iḥyāʾ ʿulūm al-dīn)", year: UNKNOWN, kind: work, lasting: "'his most widely read work' (S1)", certainty: 0.5, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP; undated in the source (before the Nishapur controversy that followed his 1106 return, itself undated), so it does not set a year (P12)."}
  evidence_of_impact:
    - {value: "The Revival is his 'most widely read work'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
  major_works:
    - {value: "The Decisive Criterion for Distinguishing Islam from Clandestine Unbelief", year: UNKNOWN, kind: book, certainty: 0.7, cites: [{source: S1, locator: "§4"}], how_known: "SEP; undated in the part read."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Author of 'the most widely read' work of its kind and a central critic of falsafa (S1).", certainty: 0.7, cites: [{source: S1, locator: "§1; §2"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Muslim", certainty: 0.5, cites: [{source: S1, locator: "§1 Life"}], how_known: "Not stated outright; early education in Ṭūs with his brother Aḥmad, a later Sufi preacher, so 0.5."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Brother Aḥmad al-Ghazālī (c. 1060–1123 or 1126), later a famous preacher and Sufi scholar", role: sibling, certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Early education in Ṭūs", stage: "elementary school", run_by: other, years: UNKNOWN, certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
    - {value: "Niẓāmiyya Madrasa, Nishapur, under al-Juwaynī", stage: university, run_by: "religious body", years: "to 1085", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP; al-Juwaynī died 1085."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: UNKNOWN, how_known: "Equals timing.major_work_period (end UNKNOWN)."}
  nominal_affiliations:
    - {value: "Sunni Islam (Ashʿarite kalām)", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "Student of the Ashʿarite al-Juwaynī; defends Ashʿarite positions (S1)."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read states one in his words."}
  primary_system:
    value: ISLAM
    basis: scholarly_reconstruction
    certainty: 0.5
    cites: [{source: S1, locator: "§1; §3; §4"}]
    how_known: "His own writing (via S1) defines Islam's boundaries by three fundamental doctrines (monotheism, Muhammad's prophecy, the Qurʾānic teachings on the afterlife) and condemns as unbelief teachings that cross them; he regarded himself as a renewer (muḥyī) of religion."
    rationale: "ISLAM use_when: Muslim belief in his own writing. CLASS_THEISM rejected: he attacks falsafa, the Aristotelian-Neoplatonic natural theology. Rests on SEP's summary of his doctrine with no quotation of his own, so a scholarly reconstruction at 0.5 (Z2-21)."
  secondary_system: {value: UNKNOWN, how_known: "Sufism is practice within ISLAM here."}
  candidate_codes_considered:
    - {code: ISLAM, reason: "Coded at 0.5 (S1, scholarly reconstruction)."}
    - {code: CLASS_THEISM, reason: "Rejected: he is its critic (S1 §2–§4)."}
  lio_axes:
    A_locus:
      value: 0
      basis: written_profession
      certainty: 0.5
      cites: [{source: S1, locator: "§7 (Marmura 2000a, pp. 166–167)"}]
      how_known: "Secondary quotation: the connection of cause and effect is 'due to the prior decision (taqdīr) of God, who creates them side by side' (2000a, p. 166, in S1); the efficient cause of burning 'is God—either through the mediation of the angels or without mediation' (p. 167). Primary check pending (§7): 0.5 is the pending-check cap."
      rationale: "A separate personal God who decides and creates: 0. Alternative 1, since the reading rests on one text via S1."
      alternatives:
        - {value: 1, note: "Not verified against the primary text.", cites: [{source: S1, locator: "§7"}]}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.5
      cites: [{source: S1, locator: "§7 (Marmura 2000a, pp. 166, 171, 222)"}]
      how_known: "Secondary quotations: 'it is within divine power to create satiety without eating, to create death without a deep cut ... in the neck' (p. 166); for a prophet's miracle God 'suspends His habit and omits to create the effect' (S1 on p. 171); he chides those who 'deny magic, sorcery, the talismanic arts, [prophetic] miracles, and the wondrous deeds [done by saints]' (p. 222). Griffel: he assumes the habitual order otherwise holds. Primary check pending: 0.5 is the pending-check cap."
      rationale: "A habitual order with God's stated exceptions (miracles): B 3. Alternative 2: the exceptions include saints' wonders and magic, and every event is God's creation, so intervention may count as frequent."
      alternatives:
        - {value: 2, note: "Occasionalist reading with wider exceptions.", cites: [{source: S1, locator: "§7 (p. 222)"}]}
    C_ledger: {value: UNKNOWN, how_known: "Redemption in the afterlife and bodily resurrection are affirmed (S1 §1, §3), but the mechanism of reward is not stated in what was read (P19)."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "Neither observation nor revelation gives 'a decisive proof' on the nature of causality (S1 §7, Griffel's words): no ranking in his own words."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Nothing read in his own words on the scope of God's order beyond §7's causality."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 0 at 0.5 and B 3 at 0.5: both need 0.7 (P10)."}
  statements:
    - text: "The connection (iqtirān) between what is habitually believed to be a cause and what is habitually believed to be an effect is not necessary (ḍarūrī), according to us."
      cites: [{source: S1, locator: "§7 (Ghazālī 2000a, 166)"}]
      date: "1095"
      context: "Incoherence of the Philosophers, 17th discussion; Marmura's translation as quoted in SEP."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-19
      note: "Primary check pending (§7)."
    - text: "it is within divine power to create satiety without eating, to create death without a deep cut (ḥaẓẓ) in the neck, to continue life after having received a deep cut in the neck, and so on to all connected things."
      cites: [{source: S1, locator: "§7 (Ghazālī 2000a, 166)"}]
      date: "1095"
      context: "Incoherence, 17th discussion, as quoted in SEP."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-19
      note: "Primary check pending."
  changes_over_life:
    - {value: "Left Baghdad in 1095 for an ascetic Sufi life, vowing never to serve the authorities; returned to state teaching in Nishapur in 1106", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
  coder_notes: "Span end UNKNOWN: the Revival is undated (P12). ISLAM rests on SEP's summary of his doctrine, so 0.5 until a primary text (the Munqidh, or the fatwā closing the Incoherence) is read in print. The Marmura quotations should be checked in the printed translation; A and B carry the pending-check cap (0.5)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Persian (Khorasan)", certainty: 0.5, cites: [{source: S1, locator: "§1 Life"}], how_known: "Coder's inference from birth in Ṭūs."}
  religious_heritage_by_birth: {value: "Muslim", certainty: 0.5, cites: [{source: S1, locator: "§1 Life"}], how_known: "Inferred."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not applicable or not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "Starts with the Incoherence (c. 1095); the latest lasting work, the Revival, is undated, so the end is UNKNOWN (P12, P29; v8's call on the auditor's advice, Z2-23)."}
  age_at_first_lasting_contribution: {value: 39, certainty: 0.5, cites: [{source: S1, locator: "§1 Life"}], how_known: "1095 − 1056 = 39 (P30); 37 under the 1058 birth."}
  first_evidence_of_lio_type_views: {value: "c. 1095 (Incoherence)", certainty: 0.5, cites: [{source: S1, locator: "§7"}], how_known: "Secondary quotation."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.5, cites: [{source: S1, locator: "§7"}], how_known: "In the Incoherence itself."}
  worldview_during_major_work: {value: "Ashʿarite Muslim; Sufi after 1095", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Logic in theology is discussed in SEP; nothing on geometry read.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not stated."}
  circle_present: {value: "no", rationale: "God is separate from the world He creates (S1 §7).", certainty: 0.5, cites: [{source: S1, locator: "§7"}], how_known: "Coder's reading."}
  reading: "Transcendent creator with habitual causation: no circle."
  notes: ""

institutions:
  - {value: "Niẓāmiyya Madrasa, Baghdad", role: professor, years: "1091–1095", kind: other, certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
  - {value: "Niẓāmiyya Madrasa, Nishapur", role: teacher, years: "1106–", kind: other, certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
collaborators:
  - {value: "al-Juwaynī", relation: teacher, note: "Ashʿarite theologian (1028–85)", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
  - {value: "Ibn Sina (Avicenna)", relation: "rival or critic", note: "target of the Incoherence", certainty: 0.7, cites: [{source: S1, locator: "§2; §7"}], how_known: "SEP."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 141"}], how_known: "Study roster."}
  controversies:
    - {value: "Birth year 1055/56 vs 1058/59", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  data_quality_flags:
    - "Own words only as secondary quotations in SEP (primary check pending)."
  open_questions:
    - "Check the Marmura quotations in print; date the Revival."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Frank Griffel"
    citation: "Griffel, Frank. \"al-Ghazali.\" Stanford Encyclopedia of Philosophy (first published 2007; substantive revision 15 January 2026). https://plato.stanford.edu/entries/al-ghazali/"
    url: "https://plato.stanford.edu/entries/al-ghazali/"
    accessed: 2026-10-19
    reliability_note: "Signed scholarly reference by a leading Ghazali scholar; quotes Marmura's translation of the Incoherence (2nd ed. 2000)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators, review]
  - id: S2
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [review]
---

# Al-Ghazali

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Abū Ḥāmid al-Ghazālī (c. 1056–1111), Ashʿarite theologian, jurist and Sufi [S1]. Draft: ISLAM (0.5); A 0 (0.5, alt 1); B 3 (0.5, alt 2); C UNKNOWN; D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Plotted (faded) at the next chart refresh.

## Life and work

Ṭūs, Nishapur, Baghdad (1091–1095), Sufi retreat, Nishapur again from 1106 [S1].

## Contribution and impact

The Incoherence (c. 1095); the Revival [S1].

## Childhood and education

Ṭūs; al-Juwaynī at Nishapur [S1].

## Adult working worldview

Habitual causation under God's decision, with miracles as suspensions of God's habit [S1, §7].

## Heritage (context only)

Muslim, Khorasan [S1].

## Timing

From 1095 (end UNKNOWN), age about 39 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle [S1].

## Open questions

- Primary check of Marmura.

## Research log

- 2026-10-19: Read SEP (Griffel) in full.
