---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 4
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z2; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to theology. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-25, by: "Grok Bot", summary: "Perpetual deepen: B_cause support single→corroborated (P48) by adding independent SEP Griffel §7.2 / §7.4 cites (S1) agreeing with Marmura Discussion 17/20 habit-miracle reading already primary-checked in S3. A already corroborated. Chart cue: dark hollow→dark filled. Axes values/certainty unchanged (A 0@0.7, B 3@0.7, mid_basin true@0.7). No fallacy_catalog; no figures/."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #137): primary-checked Marmura Incoherence 2nd ed. (Discussion 17 pp. 166–172; Discussion 20 p. 222; Conclusion pp. 226–227) and Watt Munqidh. ISLAM scholarly_reconstruction 0.5 → written_profession 0.7. A 0 and B 3 pending-check 0.5 → 0.7 (written_profession; alt 1 / alt 2 kept). mid_basin BELOW → true @0.7. P47 source_quality; P48 support (A corroborated via Incoherence+Munqidh; B single). P50 Wikipedia EN dual bio (birth still disputed; death Dec 1111 agrees). Statements re-verified against Marmura OCR. No figures/; no fallacy_catalog."}
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
  full_name: {value: "Abū Ḥāmid Muḥammad ibn Muḥammad al-Ghazālī", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}, {source: S5, locator: "lead"}], how_known: "SEP; Wikipedia EN agrees on the Arabic form."}
  native_name: {value: "Abū Ḥāmid Muḥammad ibn Muḥammad al-Ghazālī", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP (transliterated Arabic)."}
  aliases: []

basics:
  birth:
    date: {value: "1056", calendar: gregorian, certainty: 0.5, cites: [{source: S1, locator: "§1 Life"}, {source: S5, locator: "infobox / Biography"}], how_known: "P50 dual bio: SEP (letters and autobiography indicate 1055 or 1056; Griffel 2009) vs Wikipedia EN c. 1058 and medieval historians 1058/1059. Real dispute, so 0.5.", alternatives: [{value: "1058", note: "Wikipedia EN c. 1058; medieval historians 1058 or 1059.", cites: [{source: S5, locator: "infobox"}, {source: S1, locator: "§1 Life"}]}]}
    place: {value: "Ṭabarān-Ṭūs", modern_name: "near Mashhad, Iran", polity_then: "Seljuq empire", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}, {source: S5, locator: "Biography"}], how_known: "SEP and Wikipedia EN (Tus / Tabaran)."}
  death:
    date: {value: "1111-12", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}, {source: S5, locator: "infobox (19 December 1111)"}], how_known: "P50: SEP died in December 1111; Wikipedia EN 19 December 1111. Month/year agree; day from Wikipedia only, so date kept as 1111-12 at 0.7."}
    place: {value: "Ṭūs", modern_name: "near Mashhad, Iran", polity_then: "Seljuq empire", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}, {source: S5, locator: "Biography"}], how_known: "SEP and Wikipedia EN."}
  first_lasting_contribution_year: {value: 1095, certainty: 0.5, cites: [{source: S1, locator: "§2 ('published around 1095 a number of books' on falsafa and the Ismāʿīlites)"}, {source: S3, locator: "title page / Translator's Introduction"}], how_known: "The Incoherence of the Philosophers, written in his third year at the Baghdad Niẓāmiyya (appointed 1091) and published 'around 1095' (S1), so 0.5."}
  era_bucket: {value: "500 to 1399", certainty: 1.0, cites: [{source: S1, locator: "§1 Life"}], how_known: "Every adult year falls in '500 to 1399' (P2)."}
  region_of_birth: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "Iran, which the study places in MENA (P3)."}
  region_of_work: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "Nishapur, Baghdad, Damascus, Jerusalem, Ṭūs."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "As recorded."}
  languages_of_work: {value: ["Arabic"], certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S5, locator: "Works in Persian"}], how_known: "Arabic works throughout S1; Wikipedia notes some Persian (Alchemy of Happiness) — Arabic remains the coded working language of the Incoherence and Munqidh."}
  occupations: {value: ["Ashʿarite theologian", "jurist", "professor (Niẓāmiyya madrasas of Baghdad and Nishapur)", "Sufi"], certainty: 0.7, cites: [{source: S1, locator: "opening; §1 Life"}, {source: S5, locator: "lead / School affiliations"}], how_known: "SEP; Wikipedia EN (Shafiʿi Ashʿari)."}

contribution:
  primary_domain: theology
  fields: {value: ["theology (kalām)", "philosophy", "law", "Sufism"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  lasting_original_contributions:
    - {value: "The Incoherence of the Philosophers (Tahāfut al-falāsifa)", year: 1095, kind: work, lasting: "his critique of falsafa and its account of causality, discussed in S1 §7; primary-checked in Marmura (S3)", certainty: 0.5, cites: [{source: S1, locator: "§2; §7"}, {source: S3, locator: "Discussion 17; Conclusion"}], how_known: "SEP; Marmura 2nd ed.; 'around 1095'."}
    - {value: "The Revival of the Religious Sciences (Iḥyāʾ ʿulūm al-dīn)", year: UNKNOWN, kind: work, lasting: "'his most widely read work' (S1)", certainty: 0.5, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP; undated in the source (before the Nishapur controversy that followed his 1106 return, itself undated), so it does not set a year (P12)."}
  evidence_of_impact:
    - {value: "The Revival is his 'most widely read work'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
  major_works:
    - {value: "The Decisive Criterion for Distinguishing Islam from Clandestine Unbelief", year: UNKNOWN, kind: book, certainty: 0.7, cites: [{source: S1, locator: "§4"}], how_known: "SEP; undated in the part read."}
    - {value: "Deliverance from Error (al-Munqidh min al-Ḍalāl)", year: UNKNOWN, kind: book, certainty: 0.7, cites: [{source: S4, locator: "Deliverance from Error"}, {source: S1, locator: "§1 (autobiography)"}], how_known: "Watt translation (S4); written after the 1106 return (mentions Dhu'l-Qa'dah 499 / July 1106), so year UNKNOWN for P12 span purposes."}
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
    - {value: "Sunni Islam (Ashʿarite kalām)", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}, {source: S5, locator: "School affiliations"}], how_known: "Student of the Ashʿarite al-Juwaynī; Wikipedia EN Shafiʿi Ashʿari."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Munqidh warns against denying mathematical sciences in religion's name, but no single ranking sentence was taken as a D score (see D_authority)."}
  primary_system:
    value: ISLAM
    basis: written_profession
    certainty: 0.7
    cites: [{source: S3, locator: "Conclusion, pp. 226–227"}, {source: S4, locator: "Deliverance: return to Nishapur / century renewer; closing profession"}, {source: S1, locator: "§1; §3; §4"}]
    how_known: "Deepen D1: own voice in Marmura's Incoherence Conclusion — three doctrines 'do not agree with Islam in any respect' and believing them is 'manifest infidelity' (pp. 226–227); Watt Munqidh — God promised 'to revive His religion at the beginning of each century', and 'I believe, however, both by certain faith and by intuition that there is no power and no might save with God, the high, the mighty' (return-to-Nishapur section). Raised from scholarly_reconstruction 0.5 (Z2-21)."
    rationale: "ISLAM use_when: Muslim belief in his own writing (Islam's boundaries; renewer of religion; profession of power belonging to God alone). CLASS_THEISM rejected: he attacks falsafa, the Aristotelian-Neoplatonic natural theology (S3; S1 §2–§4). Contested-reading ceiling 0.7 not forced by a rival system code; kept at 0.7 to match the Munqidh+Incoherence written_profession pattern used for other roster Muslims."
  secondary_system: {value: UNKNOWN, how_known: "Sufism is practice within ISLAM here (Munqidh: mystics 'walk on the road of God')."}
  candidate_codes_considered:
    - {code: ISLAM, reason: "Coded at 0.7 (S3 Conclusion; S4 Munqidh)."}
    - {code: CLASS_THEISM, reason: "Rejected: he is its critic (S3; S1 §2–§4)."}
  lio_axes:
    A_locus:
      value: 0
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S3, locator: "Discussion 17, pp. 166–167"}, {source: S4, locator: "Deliverance: 'no power and no might save with God'"}]
      how_known: "Deepen D1 primary check: Marmura p. 166 — connection of cause and effect is due to 'the prior decree of God, who creates them side by side'; p. 167 — 'The one who enacts the burning ... is God, either through the mediation of His angels or without mediation.' Munqidh independently: 'there is no power and no might save with God, the high, the mighty.' Two independent published works → corroborated (P48). Named alternative 1 keeps the ceiling at 0.7 (§3)."
      rationale: "A separate personal God who decides and creates: 0. Alternative 1: the same passages allow angel-mediation / secondary-cause readings that some take as softening a pure occasionalist transcendence, without denying a personal Creator."
      alternatives:
        - {value: 1, note: "Angel-mediation / secondary-cause reading of the same God-as-agent lines.", cites: [{source: S3, locator: "Discussion 17, p. 167"}]}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S3, locator: "Discussion 17, pp. 166, 171–172; Discussion 20, p. 222"}, {source: S1, locator: "§7.2 (Discussion 17 opening; habit / taqdīr); §7.4 (habit disruption; miracles programmed into lawful habit)"}]
      how_known: "Deepen D1 primary check: Marmura p. 166 — 'within [divine] power to create satiety without eating' etc.; p. 171 — 'If, then, God disrupts the habitual [course of nature] by making [the miracle] occur...'; p. 222 — 'habitual [patterns] can be disrupted'. Perpetual deepen 2026-10-25: SEP Griffel §7.2 independently quotes the same opening and frames habitual course with possible miracle disruption; §7.4 notes miracles as extraordinary within God's habit, not suspension of law as chaos. Two independent source ids (S3 primary + S1 scholarly secondary) agreeing on B 3 → corroborated (P48). Named alternative 2 keeps the ceiling at 0.7."
      rationale: "Scored on his account of nature (P6). Ashʿarite occasionalism / divine habit (ʿāda): a habitual course God can disrupt for miracles — B 3, not B 4. Alternative 2 (honest): every event is God's creation, and the named exceptions include saints' wonders and magic as well as prophetic miracles, so intervention may count as frequent/wide (occasionalist reading)."
      alternatives:
        - {value: 2, note: "Occasionalist reading with wider exceptions (saints' wonders, magic; every event God's creation).", cites: [{source: S3, locator: "Discussion 20, p. 222; Discussion 17, pp. 166–171"}]}
    C_ledger: {value: UNKNOWN, how_known: "Redemption in the afterlife and bodily resurrection are affirmed (S3 Conclusion; S1 §1, §3), but the mechanism of reward is not stated in what was primary-checked (P19)."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "Incoherence: neither observation nor (elsewhere) a decisive proof settles whether causes mediate (S3 p. 222; S1 §7). Munqidh warns against denying mathematics in religion's name, but no own-words ranking of revelation vs observation when they conflict was taken as a score (P19)."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Nothing primary-checked in his own words on the scope of God's order beyond §7's causality (P19)."}
  mid_basin:
    value: true
    certainty: 0.7
    cites: [{source: S3, locator: "Discussion 17, pp. 166–172; Discussion 20, p. 222"}, {source: S4, locator: "Deliverance: power belongs to God alone"}]
    how_known: "Deepen D1: A_locus 0 ≤ 1 and B_cause 3 ≥ 3, both now at certainty 0.7 (P4, P10). A alt 1 still meets A ≤ 1. B's named alternative 2 would leave the test without a branch (TODO); preferred value B 3 stands (Euler pattern)."
  statements:
    - text: "The connection between what is habitually believed to be a cause and what is habitually believed to be an effect is not necessary, according to us. ... Their connection is due to the prior decree of God, who creates them side by side, not to its being necessary in itself, incapable of separation."
      cites: [{source: S3, locator: "Discussion 17, p. 166"}]
      date: "1095"
      context: "Incoherence of the Philosophers, 17th discussion (On causality and miracles); Marmura 2nd ed."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Primary check: archive.org Marmura PDF/OCR; matches SEP secondary quotation (taqdīr rendered 'prior decree' in Marmura)."
    - text: "On the contrary, it is within [divine] power to create satiety without eating, to create death without decapitation, to continue life after decapitation, and so on to all connected things."
      cites: [{source: S3, locator: "Discussion 17, p. 166"}]
      date: "1095"
      context: "Incoherence, 17th discussion; Marmura 2nd ed."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Primary check; SEP had 'deep cut (ḥaẓẓ) in the neck' — Marmura uses 'decapitation'."
    - text: "The one who enacts the burning by creating blackness in the cotton, [causing] separation in its parts, and making it cinder or ashes is God, either through the mediation of His angels or without mediation."
      cites: [{source: S3, locator: "Discussion 17, p. 167"}]
      date: "1095"
      context: "Incoherence, 17th discussion, first position."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Primary check."
    - text: "If, then, God disrupts the habitual [course of nature] by making [the miracle] occur at the time in which disruptions of habitual [events] take place, these cognitions [of the nonoccurrence of such unusual possibilities] slip away from [people's] hearts, and [God] does not create them."
      cites: [{source: S3, locator: "Discussion 17, p. 171"}]
      date: "1095"
      context: "Incoherence, 17th discussion, first approach under the second position."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Primary check of the 'suspend His habit' claim (Griffel paraphrase); Marmura wording is 'disrupts the habitual [course of nature]'."
    - text: "[There we stated] that the connection of connected things in existence is not by way of necessity, but that habitual [patterns] can be disrupted, whereby these matters would come about through God's power without the existence of their causes. ... Rather, in the treasury of things [enactable by divine] power there are unknown wondrous and strange things denied by someone who thinks that nothing exists but what he experiences, in the same way that some people deny magic, sorcery, the talismanic arts, [prophetic] miracles, and the miracles [of saints]"
      cites: [{source: S3, locator: "Discussion 20, p. 222"}]
      date: "1095"
      context: "Incoherence, 20th discussion (bodily resurrection), recalling Discussion 17."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Primary check; supports B 3 with honest alt 2 (wider exceptions)."
    - text: "Pronouncing them infidels is necessary in three questions. ... These three doctrines do not agree with Islam in any respect. ... This is manifest infidelity which none of the Islamic sects have believed."
      cites: [{source: S3, locator: "Conclusion, pp. 226–227"}]
      date: "1095"
      context: "Incoherence, The Book's Conclusion (fatwā on the philosophers)."
      axes: []
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Own-voice ISLAM boundary statement; three doctrines = world's pre-eternity, God's knowledge not of particulars, denial of bodily resurrection."
    - text: "I believe, however, both by certain faith and by intuition that there is no power and no might save with God, the high, the mighty, and that I do not move of myself but am moved by Him, I do not work of myself but am used by Him."
      cites: [{source: S4, locator: "Deliverance from Error, return-to-Nishapur section"}]
      date: "1106"
      context: "Munqidh, after describing the 499/1106 return to teaching at Nishapur."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Watt translation on ghazali.org; corroborates A 0 / ISLAM."
    - text: "My resolution was further strengthened by numerous visions of good men in all of which alike I was given the assurance that this impulse was a source of good was genuine guidance, and had been determined by God most high for the beginning of this century; for God most high has promised to revive His religion at the beginning of each century."
      cites: [{source: S4, locator: "Deliverance from Error, return-to-Nishapur section"}]
      date: "1106"
      context: "Munqidh, justifying the return to teaching."
      axes: []
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Watt; mujaddid / renewer self-understanding within ISLAM."
  changes_over_life:
    - {value: "Left Baghdad in 1095 for an ascetic Sufi life, vowing never to serve the authorities; returned to state teaching in Nishapur in 1106", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}, {source: S4, locator: "Deliverance (Dhu'l-Qa'dah 488 leave; 499 return)"}], how_known: "SEP; Munqidh dates."}
  coder_notes: "Span end UNKNOWN: the Revival is undated (P12). Deepen D1 lifted the Marmura pending-check cap; A/B now 0.7. Ihya primary text not opened this pass (SEP cosmology of Book 35 remains secondary). B alt 2 kept honest for Ashʿarite occasionalism / wider exceptions."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Persian (Khorasan)", certainty: 0.5, cites: [{source: S1, locator: "§1 Life"}, {source: S5, locator: "Biography (Persian Muslim descent)"}], how_known: "Coder's inference from birth in Ṭūs; Wikipedia EN agrees on Persian descent."}
  religious_heritage_by_birth: {value: "Muslim", certainty: 0.5, cites: [{source: S1, locator: "§1 Life"}], how_known: "Inferred."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not applicable or not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "Starts with the Incoherence (c. 1095); the latest lasting work, the Revival, is undated, so the end is UNKNOWN (P12, P29; v8's call on the auditor's advice, Z2-23). Munqidh dates the 1106 return but does not date the Revival."}
  age_at_first_lasting_contribution: {value: 39, certainty: 0.5, cites: [{source: S1, locator: "§1 Life"}], how_known: "1095 − 1056 = 39 (P30); 37 under the 1058 birth."}
  first_evidence_of_lio_type_views: {value: "c. 1095 (Incoherence)", certainty: 0.7, cites: [{source: S3, locator: "Discussion 17"}], how_known: "Primary-checked Marmura Discussion 17."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S3, locator: "Discussion 17"}], how_known: "In the Incoherence itself."}
  worldview_during_major_work: {value: "Ashʿarite Muslim; Sufi after 1095", certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S4, locator: "Deliverance"}], how_known: "SEP; Munqidh."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Logic in theology is discussed in SEP; nothing on geometry read.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not stated."}
  circle_present: {value: "no", rationale: "God is separate from the world He creates (S3 Discussion 17).", certainty: 0.7, cites: [{source: S3, locator: "Discussion 17, pp. 166–167"}], how_known: "Primary-checked."}
  reading: "Transcendent creator with habitual causation: no circle."
  notes: ""

institutions:
  - {value: "Niẓāmiyya Madrasa, Baghdad", role: professor, years: "1091–1095", kind: other, certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
  - {value: "Niẓāmiyya Madrasa, Nishapur", role: teacher, years: "1106–", kind: other, certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}, {source: S4, locator: "Deliverance (Dhu'l-Qa'dah 499)"}], how_known: "SEP; Munqidh."}
collaborators:
  - {value: "al-Juwaynī", relation: teacher, note: "Ashʿarite theologian (1028–85)", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
  - {value: "Ibn Sina (Avicenna)", relation: "rival or critic", note: "target of the Incoherence", certainty: 0.7, cites: [{source: S1, locator: "§2; §7"}, {source: S3, locator: "Translator's Introduction"}], how_known: "SEP; Marmura."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 141"}], how_known: "Study roster."}
  controversies:
    - {value: "Birth year 1055/56 vs 1058/59 (P50: SEP vs Wikipedia EN c. 1058)", certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S5, locator: "infobox"}], how_known: "SEP; Wikipedia EN."}
  data_quality_flags:
    - "Marmura Incoherence verified from archive.org PDF OCR (not a print page-image collation)."
    - "Watt Munqidh from unofficial web copy (ghazali.org)."
    - "Revival still undated (P12 span end UNKNOWN)."
  open_questions:
    - "Date the Revival; open Ihya Book 35 (Tawḥīd) in a primary translation for C/D/E leads."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Frank Griffel"
    citation: "Griffel, Frank. \"al-Ghazali.\" Stanford Encyclopedia of Philosophy (first published 2007; substantive revision 15 January 2026). https://plato.stanford.edu/entries/al-ghazali/"
    url: "https://plato.stanford.edu/entries/al-ghazali/"
    accessed: 2026-10-19
    source_quality: "reference entry"
    reliability_note: "Signed scholarly reference by a leading Ghazali scholar; quotes Marmura's translation of the Incoherence (2nd ed. 2000)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators, review]
  - id: S2
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [review]
  - id: S3
    type: primary
    kind: scholarly edition
    author: "Al-Ghazālī; Michael E. Marmura (trans.)"
    citation: "Al-Ghazālī. The Incoherence of the Philosophers / Tahāfut al-falāsifa: A Parallel English-Arabic Text. Translated, introduced, and annotated by Michael E. Marmura. 2nd ed. Provo, Utah: Brigham Young University Press, 2000."
    url: "https://archive.org/details/imamghazali_201510"
    accessed: 2026-10-24
    source_quality: "archive scan (OCR only)"
    reliability_note: "Scholarly bilingual edition (BYU Islamic Translation Series); read from Internet Archive PDF OCR (Discussion 17 pp. 166–172; Discussion 20 p. 222; Conclusion pp. 226–227)."
    used_for: [contribution, worldview, timing, lane_b, collaborators]
  - id: S4
    type: primary
    kind: published work by the subject
    author: "Al-Ghazālī; W. Montgomery Watt (trans.)"
    citation: "Watt, W. Montgomery. The Faith and Practice of al-Ghazali (translation of al-Munqidh min al-Ḍalāl / Deliverance from Error). London: George Allen and Unwin, 1953. E-text at ghazali.org/works/watt3.htm."
    url: "https://www.ghazali.org/works/watt3.htm"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Standard English translation of the Munqidh; web copy of the Allen & Unwin text. Used for ISLAM own voice and A corroboration."
    used_for: [contribution, worldview, timing, institutions]
  - id: S5
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Al-Ghazali.\" English Wikipedia (accessed 2026-10-24). https://en.wikipedia.org/wiki/Al-Ghazali"
    url: "https://en.wikipedia.org/wiki/Al-Ghazali"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "P50 dual bio only (birth c. 1058 / death 19 Dec 1111 vs SEP)."
    used_for: [identity, basics, heritage, review]
---

# Al-Ghazali

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Abū Ḥāmid al-Ghazālī (c. 1056–1111), Ashʿarite theologian, jurist and Sufi [S1]. Deepen D1: ISLAM (0.7, written_profession); A 0 (0.7, alt 1, corroborated); B 3 (0.7, alt 2, single); C UNKNOWN; D, E BELOW_THRESHOLD; mid_basin true @0.7. Would plot dark hollow at the next chart refresh (figures/ not touched).

## Life and work

Ṭūs, Nishapur, Baghdad (1091–1095), Sufi retreat, Nishapur again from 1106 [S1; S4].

## Contribution and impact

The Incoherence (c. 1095) [S3]; the Revival [S1]; Deliverance from Error [S4].

## Childhood and education

Ṭūs; al-Juwaynī at Nishapur [S1].

## Adult working worldview

Habitual causation under God's decree, with miracles as disruptions of God's habit [S3, Discussion 17]. Own-voice Muslim profession in the Incoherence Conclusion and the Munqidh [S3; S4].

## Heritage (context only)

Muslim, Khorasan [S1; S5].

## Timing

From 1095 (end UNKNOWN — Revival undated, P12), age about 39 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle [S3].

## Open questions

- Date the Revival; open Ihya Book 35 in a primary translation.

## Research log

- 2026-10-19: Read SEP (Griffel) in full.
- 2026-10-24: Deepen D1 — Marmura Incoherence 2nd ed. (archive.org PDF OCR) Discussion 17, 20, Conclusion; Watt Munqidh (ghazali.org); Wikipedia EN dual bio.
