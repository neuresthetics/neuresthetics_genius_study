---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Q; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-18
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-18, by: "Grok Bot", summary: "Record created (stage 3 batch Q, order P32: F 4, rank 101). Basics from Britannica (Charles Issawi, signed; body pages opening, 'The Muqaddimah' and 'Later years', read live). Worldview from the Muqaddimah in Franz Rosenthal's translation (1958/1967) as reproduced on muslimphilosophy.com (Ch. I, sixth prefatory discussion; Ch. VI, §14), with Rosenthal's 'Textual History' for dates; web copies, secondary quotation. Not a scientist (P30, coder's call). primary_system ISLAM (Ashʿarite kalām; 0.7); A 0 (0.7); B 2 (0.5, alt 1); D 1 (0.5, alt 2); mid_basin BELOW_THRESHOLD. Plotted (faded), left of B 3. Draft, not reviewed."}
    - {date: 2026-10-18, by: "Grok Bot", summary: "Batch Q audit fixes (gs_0b3023d_Q run 1). First lasting year 1377 at 0.5, alternative 1382, now cites P30 #1 and the CODING_GUIDE undated-start clause instead of P30 addendum c (I7). D rationale softened: the Lawgiver's ban concerns the regress of causes towards God, not natural inquiry as such. Note added that the Muqaddimah was revised to about 1404 (possible later period end). Britannica body sections 'The Muqaddimah' and 'Journey to Egypt' re-fetched and the locators confirmed (1375 retreat, four years; first draft; best single source on Muslim North Africa; Tunis; 1382; Al-Azhar and the Qamḥiyyah college). Values unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #100 / F4 rank 101). Needs: corroborate A 0; lift B 2 if Muqaddimah nature-as-custom / occasionalism holds; not a scientist (P30). Dual bio Wikipedia EN (S5, P50). P47 source_quality on S1–S6. Primary check: IA OCR of Rosenthal Bollingen printed vols (IGNCA: vol.1 in.gov.ignca.16173 Ch. I sixth prefatory; vol.3 in.gov.ignca.16175 Ch. VI §14) as S6 — confirms 'realm dominated by custom', 'There is no maker but Him', 'cannot be compared with created beings', intellect-as-correct-scale, miracles / acts of divine grace, dream-visions self-report, Baqillani 'accident does not persist two moments'. A 0 stays @0.7 support corroborated (S2 web + S6 IA OCR; distinct ids P48). B 2 lifted 0.5→0.7 support corroborated (same; contested alt 1 caps ≤0.7 P25; nature-as-custom with live miracles = P27 B 2). primary ISLAM @0.7 kept. mid_basin BELOW (A≤1 with B=2 between branches). Chart-moving YES: faded→dark (min cert 0.7); hollow→filled (both A&B corroborated). Draft deepen report in drafts/ (untracked). No fallacy_catalog. No figures refresh."}

identity:
  id: ibn-khaldun
  display_name: "Ibn Khaldun"
  roster:
    canonical_name: "Ibn Khaldun"
    rank: 101
    F: 4
    models: [Claude, DeepSeek, Gemini, Grok]
    band: "core (3–4)"
    status: core
    field: polymath
    field_bucket: polymath
  full_name: {value: "Walī al-Dīn ʿAbd al-Raḥmān ibn Muḥammad ibn Muḥammad ibn Abī Bakr Muḥammad ibn al-Ḥasan Ibn Khaldūn", certainty: 0.7, cites: [{source: S1, locator: "header ('Also known as')"}, {source: S5, locator: "lead / Early life (full name forms)"}], how_known: "Britannica header; Wikipedia lead forms agree on the Khaldūn lineage (P15)."}
  native_name: {value: "ابن خلدون", certainty: 0.5, cites: [{source: S5, locator: "infobox native name"}], how_known: "Wikipedia Arabic; Britannica uses Latin-script Ibn Khaldūn."}
  aliases:
    - {name: "Ibn Khaldūn", kind: "transliteration"}
    - {name: "Abū Zayd ʿAbd al-Raḥmān ibn Muḥammad ibn Khaldūn al-Ḥaḍramī", kind: "other"}

basics:
  birth:
    date: {value: "1332-05-27", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "infobox / lead (27 May 1332)"}], how_known: "Britannica and Wikipedia agree."}
    place: {value: "Tunis", modern_name: "Tunis, Tunisia", polity_then: "Hafsid sultanate", certainty: 1.0, cites: [{source: S1, locator: "opening; 'Background and early life'"}, {source: S5, locator: "Early life"}], how_known: "Britannica and Wikipedia."}
  death:
    date: {value: "1406-03-17", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "infobox / lead (17 March 1406)"}], how_known: "Britannica and Wikipedia agree."}
    place: {value: "Cairo", modern_name: "Cairo, Egypt", polity_then: "Mamluk sultanate", certainty: 1.0, cites: [{source: S1, locator: "opening; 'Rescue by Timur'"}, {source: S5, locator: "Death"}], how_known: "Britannica and Wikipedia."}
  first_lasting_contribution_year: {value: 1377, certainty: 0.5, cites: [{source: S3, locator: "§3 Gradual growth of the text"}, {source: S1, locator: "'The Muqaddimah' (1375 retreat, four years)"}], how_known: "Ibn Khaldun dates the first draft of the Muqaddimah to five months ending in the middle of 779 [November 1377] (Rosenthal, citing 3:480). The first documented public act is the presentation of the History (with the Muqaddimah) to the Hafsid ruler in Tunis (P30 #1), but it is undated in what was read, only bounded by his departure in 1382; under the undated-start clause of CODING_GUIDE §8 ('do not guess') that start is not given a year. Coder's call: the author's own composition date, 1377, at 0.5, with 1382 (the bound of the presentation) as the named alternative. P30 addendum c does not apply, because a public act in life exists. The Muqaddimah was revised to about 1404 (S3)."}
  era_bucket: {value: "500 to 1399", certainty: 0.7, cites: [{source: S3, locator: "§3"}], how_known: "First lasting year 1377 (P2); the alternative 1382 is in the same bucket."}
  region_of_birth: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "infobox"}], how_known: "Tunisia (P3)."}
  region_of_work: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'; 'The Muqaddimah'; 'Journey to Egypt'"}, {source: S5, locator: "Biography"}], how_known: "Tunis, Fez, Bejaïa, Tlemcen, Qalʿat ibn Salāmah (Algeria), Cairo; also Granada (Southern Europe) for a time."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S5, locator: "lead"}], how_known: "As recorded."}
  languages_of_work: {value: ["Arabic"], certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Britannica."}
  occupations: {value: ["historian", "judge (Mālikī chief qāḍī)", "court official", "teacher"], certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'; 'Journey to Egypt'"}, {source: S5, locator: "lead"}], how_known: "Britannica and Wikipedia."}

contribution:
  fields: {value: ["historiography", "philosophy of history", "sociology", "economics"], certainty: 0.7, cites: [{source: S1, locator: "'The Muqaddimah'"}, {source: S5, locator: "lead"}], how_known: "Britannica and Wikipedia."}
  lasting_original_contributions:
    - {value: "Muqaddimah: a philosophy of history and a new 'science of culture' (ʿilm al-ʿumrān), with the concept of ʿaṣabiyyah (social cohesion)", year: 1377, kind: theory, lasting: "Toynbee: 'undoubtedly the greatest work of its kind that has ever yet been created' (S1)", certainty: 0.5, cites: [{source: S1, locator: "'The Muqaddimah'"}, {source: S3, locator: "§3"}, {source: S5, locator: "Muqaddimah"}], how_known: "First draft dated November 1377 by the author (S3); revised until about 1404 (S3)."}
    - {value: "Kitāb al-ʿIbar: history of the Arabs and Berbers, 'the best single source on the history of Muslim North Africa'", year: "1377–1382", kind: work, lasting: "(S1)", certainty: 0.5, cites: [{source: S1, locator: "'Journey to Egypt'"}, {source: S3, locator: "§3"}], how_known: "Part written at Qalʿat ibn Salāmah, finished in Tunis and presented to the Hafsid ruler before he sailed for Egypt in 1382 (S1, S3); P30 #4 end year."}
  evidence_of_impact:
    - {value: "Ottoman interest from the 16th century; worldwide audience after the 1860s French translation", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "'Significance'"}], how_known: "Britannica."}
    - {value: "Compared by modern scholars to forerunners of historiography, sociology, economics, demography", kind: "scholarly consensus", certainty: 0.5, cites: [{source: S5, locator: "lead"}], how_known: "Wikipedia lead epithets — secondary consensus claim."}
  major_works:
    - {value: "Muqaddimah (Prolegomena)", year: 1377, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "'The Muqaddimah'"}, {source: S6, locator: "title pages (Rosenthal Bollingen)"}, {source: S5, locator: "Works"}], how_known: "Britannica; Rosenthal edition; Wikipedia."}
    - {value: "Kitāb al-ʿIbar", year: "1377–1382", kind: "book", certainty: 0.7, cites: [{source: S1, locator: "'Journey to Egypt'"}, {source: S5, locator: "Works"}], how_known: "Britannica and Wikipedia."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1; S5).", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "lead"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Sunni Islam (Andalusian Arab Muslim administrative family settled in Tunis)", certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}, {source: S5, locator: "Early life"}], how_known: "Britannica and Wikipedia; context only."}
  family_religious_practice: {value: "Qurʾān memorization and study of commentaries, law and letters in childhood schooling", certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Britannica."}
  parents_and_household:
    - {value: "Father an administrator and soldier who turned to theology, law and letters; both parents died in the Black Death of 1349", role: parents, certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Britannica, from his autobiography."}
  household_circumstances: {value: "Andalusian family of high administrative rank, settled in Tunis", certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}, {source: S5, locator: "Early life"}], how_known: "Britannica and Wikipedia."}
  schooling:
    - {value: "Memorized the Qurʾān, studied its commentaries, Muslim law and Arabic literature", stage: other, years: "–1352", certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Britannica; formal education ended at 20."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["Arabic"], certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Britannica."}
  notable_events:
    - {value: "Black Death took both parents", year: 1349, certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Britannica."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1377–1382", certainty: 0.5, cites: [{source: S3, locator: "§3"}, {source: S1, locator: "'Journey to Egypt'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Sunni Islam, Mālikī rite (chief judge in Cairo)", certainty: 0.7, cites: [{source: S1, locator: "'Journey to Egypt'"}, {source: S5, locator: "Biography / Egypt"}], how_known: "Britannica and Wikipedia; context only."}
    - {value: "Ashʿarite kalām (follows Abū l-Ḥasan al-Ashʿarī; recounts Baqillānī atomic premises)", certainty: 0.7, cites: [{source: S2, locator: "Ch. VI §14"}, {source: S6, locator: "vol.3 Ch. VI §14 (IA OCR)"}], how_known: "Own Muqaddimah text (Rosenthal); affiliation context for primary_system."}
  self_described_science_religion_relation: {value: "The intellect 'is a correct scale', certain within its level, but must not weigh God's oneness, the other world, prophecy or the divine attributes; preferring intellect to tradition there is wrong", certainty: 0.7, cites: [{source: S2, locator: "Ch. VI §14"}, {source: S6, locator: "vol.3 Ch. VI §14 (IA OCR)"}], how_known: "Rosenthal translation; web copy corroborated by IA OCR of printed Bollingen."}
  primary_system:
    value: ISLAM
    basis: written_profession
    certainty: 0.7
    cites: [{source: S2, locator: "Ch. VI §14; Ch. I sixth prefatory discussion"}, {source: S6, locator: "vol.3 Ch. VI §14; vol.1 Ch. I sixth prefatory (IA OCR)"}]
    rationale: "His own writing affirms the Muslim articles of faith (God's oneness, prophecy, the Last Day, predestination) and follows the Ashʿarite kalām school ('the leader of the speculative theologians, Abul-Hasan al-Ash'ari'), which ISLAM's use_when keeps under ISLAM. Not CLASS_THEISM: he rejects causal necessity ('There is no maker but Him') and attacks the philosophers' necessary causation."
    how_known: "Published work in Rosenthal's translation; muslimphilosophy web (S2) corroborated by IA OCR of printed Bollingen vols (S6). Certainty stays 0.7 (translation; text revised to ~1404)."
  secondary_system: {value: UNKNOWN, how_known: "One system (P29)."}
  candidate_codes_considered:
    - {code: ISLAM, reason: "Ashʿarite articles of faith in his own text."}
    - {code: CLASS_THEISM, reason: "Rejected: he denies the falsafa necessary causality."}
  lio_axes:
    A_locus:
      value: 0
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S2, locator: "Ch. VI §14"}, {source: S6, locator: "vol.3 Ch. VI §14 (IA OCR, 'cannot be compared with created beings'; 'sole source of all actions'; volition; fate)"}]
      rationale: "Transcendent, willing person outside the world: 'He in His essence cannot be compared with created beings'; the Creator is 'the sole source of all actions'; 'He has volition'; 'He determines the fate of each created thing'. No immanence stated."
      how_known: "Rosenthal via muslimphilosophy web (S2) corroborated by IA OCR of printed Bollingen vol.3 (S6) — distinct source ids → corroborated (P48). Certainty 0.7 (translation / revision layer; not Arabic facsimile)."
    B_cause:
      value: 2
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S2, locator: "Ch. I sixth prefatory discussion; Ch. VI §14"}, {source: S6, locator: "vol.1 Ch. I sixth prefatory; vol.3 Ch. VI §14 (IA OCR)"}]
      rationale: "Account of nature (P6/P16): the world has causes that introduce things 'into the realm dominated by custom'; causes' influence is 'only known through customary (experience)' and an 'apparent (causal) relationship', while 'There is no maker but Him' and 'the way in which the causes exercise their influence … is unknown'. Exceptions are live and recurring, not limited: prophets' miracles ('actions the like of which it is impossible for other human beings to achieve'), saints' 'acts of divine grace', and supernatural perception he reports from his own dream visions. So B 2 (P27 anchor: exceptions not limited). Named alternative 1: Ashʿarite occasionalism read as every event a direct act of God (Baqillānī premises he recounts: 'An accident does not persist two moments')."
      how_known: "IA OCR of printed Rosenthal (S6) confirms the web copy (S2) on custom / no-maker / miracles — distinct ids → corroborated (P48). Contested alt 1 keeps certainty at most 0.7 (P25); lifted from 0.5 now that the archive scan holds the passages. Not a scientist (P30): scored from own-voice nature account, not working science."
      alternatives:
        - {value: 1, note: "Occasionalism: God the only maker of every event (Ashʿarite atomism he recounts).", cites: [{source: S2, locator: "Ch. VI §14"}, {source: S6, locator: "vol.3 Ch. VI §14 (Baqillānī premises)"}]}
    C_ledger: {value: UNKNOWN, how_known: "Paradise and Hell are among the articles of faith he lists, but not scored at this reading (coder's call)."}
    D_authority:
      value: 1
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S2, locator: "Ch. VI §14"}, {source: S6, locator: "vol.3 Ch. VI §14 (IA OCR)"}]
      rationale: "Revelation outranks reason beyond the intellect's level ('those who give the intellect preference over (traditional) information in such matters are wrong'), and the Lawgiver's command bounds speculation on the chain of causes as it ascends towards God: 'we were forbidden by the Lawgiver (Muhammad) to study causes' (in context, the regress of causes and their hidden influence, not natural inquiry as such). The intellect keeps its own field ('a correct scale … completely certain'). Named alternative 2: two domains, each with its own authority."
      how_known: "S2 + S6 agree; contested alt 2 → certainty stays 0.5 (coder's call; D not a deepen target)."
      alternatives:
        - {value: 2, note: "Intellect certain in its field; revelation in the divine.", cites: [{source: S2, locator: "Ch. VI §14"}, {source: S6, locator: "vol.3 Ch. VI §14"}]}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 0 @0.7 is ≤ 1 and B 2 @0.7 falls between the branches (needs B ≥ 3 for true, or B ≤ 1 for false via the A≤1 branch) (§6, P19). Deepen D1 lifted B certainty but not the value."}
  statements:
    - text: "It should be known that the things that come into being in the world of existing things, whether they belong to essences or to either human or animal actions, require appropriate causes which are prior to (their coming into being). They introduce the things that come into being into the realm dominated by custom, and effect their coming into being."
      cites: [{source: S6, locator: "vol.3 Ch. VI §14 (IA OCR)"}, {source: S2, locator: "Ch. VI §14"}]
      context: "Muqaddimah VI.14, 'The science of speculative theology'; first drafted 1377 and revised to about 1404 (S3). No single year, so the date is left out."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Deepen D1: checked against IA OCR of Rosenthal Bollingen vol.3 (IGNCA 16175)."
    - text: "There is no maker but Him. All (causes) lead up to Him and go back to His power."
      cites: [{source: S6, locator: "vol.3 Ch. VI §14 (IA OCR)"}, {source: S2, locator: "Ch. VI §14"}]
      context: "Same section."
      axes: [B_cause, A_locus]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "As above."
    - text: "The intellect, indeed, is a correct scale. Its indications are completely certain and in no way wrong. However, the intellect should not be used to weigh such matters as the oneness of God, the other world, the truth of prophecy, the real character of the divine attributes, or anything else that lies beyond the level of the intellect."
      cites: [{source: S6, locator: "vol.3 Ch. VI §14 (IA OCR)"}, {source: S2, locator: "Ch. VI §14"}]
      context: "Same section."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "As above."
    - text: "Therefore, we were forbidden by the Lawgiver (Muhammad) to study causes."
      cites: [{source: S6, locator: "vol.3 Ch. VI §14 (IA OCR)"}, {source: S2, locator: "Ch. VI §14"}]
      context: "Same section."
      axes: [D_authority, B_cause]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "As above; context is the ascending regress of causes toward God, not natural craft inquiry."
    - text: "He made it our first obligation to believe that He in His essence cannot be compared with created beings."
      cites: [{source: S6, locator: "vol.3 Ch. VI §14 (IA OCR)"}, {source: S2, locator: "Ch. VI §14"}]
      context: "Same section, on the articles of faith."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "As above."
    - text: "are actions the like of which it is impossible for other human beings to achieve. They are, therefore, called \"miracles.\" They are not within the ability of men, but beyond their power."
      cites: [{source: S6, locator: "vol.1 Ch. I sixth prefatory discussion (IA OCR)"}, {source: S2, locator: "Ch. I, sixth prefatory discussion"}]
      context: "Muqaddimah I, sixth prefatory discussion, on prophets' 'wonders'; same dating as above."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Deepen D1: IA OCR vol.1 (IGNCA 16173) confirms."
    - text: "With the help of these words, I have myself had remarkable dream visions, through which I learned things about myself that I wanted to know."
      cites: [{source: S6, locator: "vol.1 Ch. I sixth prefatory ('Dream words', IA OCR)"}, {source: S2, locator: "Ch. I, sixth prefatory discussion ('Dream words')"}]
      context: "Same discussion."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "As above; live supernatural exception he reports of himself."
    - text: "He affirmed, for instance, the existence of the atom (al-jawhar al-fard) and of the vacuum. He made statements such as \"An accident cannot sustain another accident,\" and \"An accident does not persist two moments.\""
      cites: [{source: S6, locator: "vol.3 Ch. VI §14 (Baqillānī premises, IA OCR)"}, {source: S2, locator: "Ch. VI §14"}]
      context: "Muqaddimah VI.14 recounting Judge Abū Bakr al-Baqillānī's Ashʿarite logical premises."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "He recounts Ashʿarite occasionalist atomism as the school premises; supports named alt B 1. Not scored as his sole voice over the custom+miracles B 2 reading."
  changes_over_life: []
  coder_notes: "Deepen D1. Not a scientist under P30 (ʿilm al-ʿumrān is a theory of human society, not physical/natural systems; P35 addendum does not apply). B scored from own-voice Muqaddimah nature account. Chart cues after D1: dark + filled (A&B both @0.7 corroborated). mid_basin stays BELOW (B 2 between branches). Britannica Top Questions not cited (P26). Arabic text and printed page-image of Rosenthal still open; IA OCR used."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Arab family of South Arabian (Ḥaḍramawt) descent, long settled in Seville, then Tunis", certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}, {source: S5, locator: "Early life"}], how_known: "Britannica and Wikipedia, from his autobiography."}
  religious_heritage_by_birth: {value: "Sunni Islam", certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}, {source: S5, locator: "Early life"}], how_known: "Britannica and Wikipedia; context only."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1377–1382", certainty: 0.5, cites: [{source: S3, locator: "§3"}, {source: S1, locator: "'Journey to Egypt'"}], how_known: "Muqaddimah draft (1377) to the History finished in Tunis before he left in 1382 (P30 #4); 0.5. The Muqaddimah was revised until about 1404 (S3), so the period end could arguably run to 1404 if the revisions count as lasting work (note only, P30 addendum b)."}
  age_at_first_lasting_contribution: {value: 45, certainty: 0.5, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "§3"}], how_known: "1377 − 1332 = 45 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No axis scored at 3 or 4 (P27 anchor)."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "A 0, B 2, D 1 — none is LIO-type (3 or 4).", certainty: 0.5, cites: [{source: S2, locator: "Ch. VI §14"}, {source: S6, locator: "vol.3 Ch. VI §14"}], how_known: "Coder's reading."}
  worldview_during_major_work: {value: "Ashʿarite Sunni theology: God the only maker; nature as custom", certainty: 0.7, cites: [{source: S2, locator: "Ch. VI §14"}, {source: S6, locator: "vol.3 Ch. VI §14"}], how_known: "Muqaddimah text; the passages may include later revisions (S3)."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not read as a geometric-form claim.", certainty: 0.5, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Not read."}
  circle_present: {value: "no", rationale: "Transcendent maker; nature as custom with live miracles.", certainty: 0.7, cites: [{source: S2, locator: "Ch. VI §14"}, {source: S6, locator: "vol.3 Ch. VI §14"}], how_known: "Coder's reading of Muqaddimah."}
  reading: "Lane B only: a transcendent God, the only maker, behind a customary natural order with live exceptions (miracles, grace, dream visions)."
  notes: "Ashʿarite occasionalism is the named B alt 1; main score keeps custom+exceptions as B 2."

institutions:
  - {value: "Court of Fez (Marinid sultan)", role: secretary, years: UNKNOWN, kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Britannica."}
  - {value: "Al-Azhar and the Qamḥiyyah college, Cairo", role: "teacher; professor of jurisprudence", years: "1382–", kind: university, certainty: 0.5, cites: [{source: S1, locator: "'Journey to Egypt'"}], how_known: "Britannica; the kind is the coder's."}
  - {value: "Mamluk judiciary, Cairo", role: "chief judge of the Mālikī rite", years: UNKNOWN, kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "'Journey to Egypt'"}, {source: S5, locator: "Egypt"}], how_known: "Britannica and Wikipedia."}
collaborators:
  - {value: "Ibn al-Khaṭīb", relation: other, note: "friend and rival, prime minister of Granada", certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Britannica."}
  - {value: "Averroës", relation: "influenced by", note: "he wrote summaries of several of his books", certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 101"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Muqaddimah quotations checked in IA OCR of Rosenthal Bollingen printed vols (S6); Arabic text and clean print page-images still open; text revised to about 1404 so a passage's layer is not dated."
    - "First lasting year: composition 1377 (author's own date) against presentation in Tunis by 1382."
    - "Dawood abridged edition borrow-restricted on IA this pass; full three-volume IGNCA OCR used instead."
  open_questions:
    - "Arabic text check; printed Rosenthal page-images (not OCR); VI.30 refutation of philosophy; Lubāb al-Muḥaṣṣal."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Charles Issawi"
    citation: "Issawi, Charles. \"Ibn Khaldūn.\" Encyclopaedia Britannica (revised 5 September 2026). https://www.britannica.com/biography/Ibn-Khaldun, with the pages 'The Muqaddimah: Ibn Khaldūn's philosophy of history' and 'Later years'. Read live 2026-10-18. Deepen D1 2026-10-24: body retained; dual bio with S5."
    url: "https://www.britannica.com/biography/Ibn-Khaldun"
    accessed: 2026-10-18
    source_quality: "reference entry"
    reliability_note: "Signed article. Body only; the AI-generated Top Questions are not cited (P26)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Ibn Khaldūn (trans. Franz Rosenthal)"
    citation: "Ibn Khaldūn. The Muqaddimah: An Introduction to History, trans. Franz Rosenthal (New York: Pantheon/Bollingen, 1958; 2nd ed. Princeton, 1967). Web edition, muslimphilosophy.com: Ch. I sixth prefatory discussion (http://www.muslimphilosophy.com/ik/Muqaddimah/Chapter1/Ch_1_06.htm) and Ch. VI §14 (http://www.muslimphilosophy.com/ik/Muqaddimah/Chapter6/Ch_6_14.htm)."
    url: "http://www.muslimphilosophy.com/ik/Muqaddimah/Chapter6/Ch_6_14.htm"
    accessed: 2026-10-18
    source_quality: "unofficial web copy"
    reliability_note: "Web copy of a scholarly translation. Deepen D1: wording checked against IA OCR of the printed Bollingen (S6)."
    used_for: [worldview, timing, lane_b]
  - id: S3
    type: secondary
    kind: "scholarly book"
    author: "Franz Rosenthal"
    citation: "Rosenthal, Franz. \"The Textual History of the Muqaddimah\", translator's introduction to The Muqaddimah (1958/1967). Web edition: http://www.muslimphilosophy.com/ik/Muqaddimah/TransIntro/TexualHistory.htm"
    url: "http://www.muslimphilosophy.com/ik/Muqaddimah/TransIntro/TexualHistory.htm"
    accessed: 2026-10-18
    source_quality: "unofficial web copy"
    reliability_note: "Scholarly introduction via a web copy."
    used_for: [basics, contribution, timing, worldview]
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
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. \"Ibn Khaldun.\" Wikipedia. https://en.wikipedia.org/wiki/Ibn_Khaldun. Dual bio (P50). Read 2026-10-24."
    url: "https://en.wikipedia.org/wiki/Ibn_Khaldun"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Used for dual-bio basics, name forms, works list. Worldview A/B scoring does not rest on Wikipedia paraphrases of theology."
    used_for: [identity, basics, contribution, childhood, heritage, institutions]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Ibn Khaldūn (trans. Franz Rosenthal)"
    citation: "Ibn Khaldūn. The Muqaddimah: An Introduction to History, trans. Franz Rosenthal (Bollingen Series XLIII; Pantheon, 1958). Internet Archive OCR of Government of India / IGNCA scans: vol.1 https://archive.org/details/in.gov.ignca.16173 (Ch. I sixth prefatory discussion — miracles, dream words); vol.3 https://archive.org/details/in.gov.ignca.16175 (Ch. VI §14 — custom, no maker, intellect scale, Ashʿarī/Baqillānī). Read 2026-10-24."
    url: "https://archive.org/details/in.gov.ignca.16175"
    accessed: 2026-10-24
    source_quality: "archive scan (OCR only)"
    reliability_note: "OCR of the printed scholarly translation. Primary check for deepen D1 A/B quotes; Arabic and clean page-images still open. Distinct id from S2 web copy → P48 corroborated."
    used_for: [worldview, timing, lane_b, contribution]
---

# Ibn Khaldun

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Ibn Khaldūn (1332–1406), Arab historian and judge [S1; S5]. Deepen D1: primary_system ISLAM (0.7); A 0 at 0.7 corroborated; B 2 at 0.7 corroborated (alt 1); D 1 at 0.5 (alt 2); mid_basin BELOW_THRESHOLD. Plotted dark filled (was faded hollow). Chart-moving YES.

## Life and work

Tunis, Fez, Granada, Qalʿat ibn Salāmah, Cairo [S1; S5].

## Contribution and impact

Muqaddimah (draft 1377) and Kitāb al-ʿIbar [S1; S3; S6].

## Childhood and education

Qurʾān, law, letters; parents died in 1349 [S1]. Sunni Muslim family [S1; S5].

## Adult working worldview

'There is no maker but Him'; nature as 'realm dominated by custom'; miracles and dream visions [S2; S6, VI.14 and I.6].

## Heritage (context only)

Andalusian Arab family; Sunni Islam [S1; S5].

## Timing

1377–1382 [S3; S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Nature as custom with live exceptions [S2; S6]; occasionalism named as B alt 1.

## Open questions

- Arabic and clean Rosenthal page-images; VI.30.

## Research log

- 2026-10-18: Read Britannica (live, three pages), Rosenthal's translation and introduction on muslimphilosophy.com.
- 2026-10-24: Deepen D1 — IA OCR Rosenthal Bollingen vols 1 and 3 (IGNCA); Wikipedia dual bio; A corroborated; B 2 @0.7 corroborated; person-file-only commit.
