---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Q)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-18
  last_updated: 2026-10-18
  change_log:
    - {date: 2026-10-18, by: "Grok Bot", summary: "Record created (stage 3 batch Q, order P32: F 4, rank 101). Basics from Britannica (Charles Issawi, signed; body pages opening, 'The Muqaddimah' and 'Later years', read live). Worldview from the Muqaddimah in Franz Rosenthal's translation (1958/1967) as reproduced on muslimphilosophy.com (Ch. I, sixth prefatory discussion; Ch. VI, §14), with Rosenthal's 'Textual History' for dates; web copies, secondary quotation. Not a scientist (P30, coder's call). primary_system ISLAM (Ashʿarite kalām; 0.7); A 0 (0.7); B 2 (0.5, alt 1); D 1 (0.5, alt 2); mid_basin BELOW_THRESHOLD. Plotted (faded), left of B 3. Draft, not reviewed."}
    - {date: 2026-10-18, by: "Grok Bot", summary: "Batch Q audit fixes (gs_0b3023d_Q run 1). First lasting year 1377 at 0.5, alternative 1382, now cites P30 #1 and the CODING_GUIDE undated-start clause instead of P30 addendum c (I7). D rationale softened: the Lawgiver's ban concerns the regress of causes towards God, not natural inquiry as such. Note added that the Muqaddimah was revised to about 1404 (possible later period end). Britannica body sections 'The Muqaddimah' and 'Journey to Egypt' re-fetched and the locators confirmed (1375 retreat, four years; first draft; best single source on Muslim North Africa; Tunis; 1382; Al-Azhar and the Qamḥiyyah college). Values unchanged."}

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
  full_name: {value: "Walī al-Dīn ʿAbd al-Raḥmān ibn Muḥammad ibn Muḥammad ibn Abī Bakr Muḥammad ibn al-Ḥasan Ibn Khaldūn", certainty: 0.5, cites: [{source: S1, locator: "header ('Also known as')"}], how_known: "Britannica header line (not the AI box); Rosenthal's intro (S2) gives a shorter form."}
  native_name: {value: "Ibn Khaldūn", certainty: 0.7, cites: [{source: S1, locator: "title"}], how_known: "Britannica transliteration."}
  aliases: []

basics:
  birth:
    date: {value: "1332-05-27", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica body."}
    place: {value: "Tunis", modern_name: "Tunis, Tunisia", polity_then: "Hafsid sultanate", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Background and early life'"}], how_known: "Britannica."}
  death:
    date: {value: "1406-03-17", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica body."}
    place: {value: "Cairo", modern_name: "Cairo, Egypt", polity_then: "Mamluk sultanate", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Rescue by Timur'"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1377, certainty: 0.5, cites: [{source: S3, locator: "§3 Gradual growth of the text"}, {source: S1, locator: "'The Muqaddimah' (1375 retreat, four years)"}], how_known: "Ibn Khaldun dates the first draft of the Muqaddimah to five months ending in the middle of 779 [November 1377] (Rosenthal, citing 3:480). The first documented public act is the presentation of the History (with the Muqaddimah) to the Hafsid ruler in Tunis (P30 #1), but it is undated in what was read, only bounded by his departure in 1382; under the undated-start clause of CODING_GUIDE §8 ('do not guess') that start is not given a year. Coder's call: the author's own composition date, 1377, at 0.5, with 1382 (the bound of the presentation) as the named alternative. P30 addendum c does not apply, because a public act in life exists. The Muqaddimah was revised to about 1404 (S3)."}
  era_bucket: {value: "500 to 1399", certainty: 0.7, cites: [{source: S3, locator: "§3"}], how_known: "First lasting year 1377 (P2); the alternative 1382 is in the same bucket."}
  region_of_birth: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Tunisia (P3)."}
  region_of_work: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'; 'The Muqaddimah'; 'Journey to Egypt'"}], how_known: "Tunis, Fez, Bejaïa, Tlemcen, Qalʿat ibn Salāmah (Algeria), Cairo; also Granada (Southern Europe) for a time."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Arabic"], certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Britannica."}
  occupations: {value: ["historian", "judge (Mālikī chief qāḍī)", "court official", "teacher"], certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'; 'Journey to Egypt'"}], how_known: "Britannica."}

contribution:
  fields: {value: ["historiography", "philosophy of history", "sociology", "economics"], certainty: 0.7, cites: [{source: S1, locator: "'The Muqaddimah'"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Muqaddimah: a philosophy of history and a new 'science of culture' (ʿilm al-ʿumrān), with the concept of ʿaṣabiyyah (social cohesion)", year: 1377, kind: theory, lasting: "Toynbee: 'undoubtedly the greatest work of its kind that has ever yet been created' (S1)", certainty: 0.5, cites: [{source: S1, locator: "'The Muqaddimah'"}, {source: S3, locator: "§3"}], how_known: "First draft dated November 1377 by the author (S3); revised until about 1404 (S3)."}
    - {value: "Kitāb al-ʿIbar: history of the Arabs and Berbers, 'the best single source on the history of Muslim North Africa'", year: "1377–1382", kind: work, lasting: "(S1)", certainty: 0.5, cites: [{source: S1, locator: "'Journey to Egypt'"}, {source: S3, locator: "§3"}], how_known: "Part written at Qalʿat ibn Salāmah, finished in Tunis and presented to the Hafsid ruler before he sailed for Egypt in 1382 (S1, S3); P30 #4 end year."}
  evidence_of_impact:
    - {value: "Ottoman interest from the 16th century; worldwide audience after the 1860s French translation", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "'Significance'"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father an administrator and soldier who turned to theology, law and letters; both parents died in the Black Death of 1349", role: parents, certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Britannica, from his autobiography."}
  household_circumstances: {value: "Andalusian family of high administrative rank, settled in Tunis", certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Britannica."}
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
    - {value: "Sunni Islam, Mālikī rite (chief judge in Cairo)", certainty: 0.7, cites: [{source: S1, locator: "'Journey to Egypt'"}], how_known: "Britannica; context only."}
  self_described_science_religion_relation: {value: "The intellect 'is a correct scale', certain within its level, but must not weigh God's oneness, the other world, prophecy or the divine attributes; preferring intellect to tradition there is wrong", certainty: 0.7, cites: [{source: S2, locator: "Ch. VI §14"}], how_known: "Rosenthal translation via web copy."}
  primary_system:
    value: ISLAM
    basis: written_profession
    certainty: 0.7
    cites: [{source: S2, locator: "Ch. VI §14; Ch. I sixth prefatory discussion"}]
    rationale: "His own writing affirms the Muslim articles of faith (God's oneness, prophecy, the Last Day, predestination) and follows the Ashʿarite kalām school ('the leader of the speculative theologians, Abul-Hasan al-Ash'ari'), which ISLAM's use_when keeps under ISLAM. Not CLASS_THEISM: he rejects causal necessity ('There is no maker but Him') and attacks the philosophers' necessary causation."
    how_known: "Published work in Rosenthal's translation via a web copy (secondary quotation, cap 0.7)."
  secondary_system: {value: UNKNOWN, how_known: "One system (P29)."}
  candidate_codes_considered:
    - {code: ISLAM, reason: "Ashʿarite articles of faith in his own text."}
    - {code: CLASS_THEISM, reason: "Rejected: he denies the falsafa necessary causality."}
  lio_axes:
    A_locus:
      value: 0
      basis: written_profession
      certainty: 0.7
      cites: [{source: S2, locator: "Ch. VI §14"}]
      rationale: "Transcendent, willing person outside the world: 'He in His essence cannot be compared with created beings'; the Creator is 'the sole source of all actions'; 'He has volition'; 'He determines the fate of each created thing'. No immanence stated."
      how_known: "Rosenthal translation via a web copy, secondary quotation, so 0.7 at most; Rosenthal notes he toned down one 'strong expression of monistic mysticism' (S3), not read."
    B_cause:
      value: 2
      basis: written_profession
      certainty: 0.5
      cites: [{source: S2, locator: "Ch. I sixth prefatory discussion; Ch. VI §14"}]
      rationale: "Account of nature (P6): the world 'has a certain order and solid construction' with 'nexuses between causes and things caused', but causes only bring things 'into the realm dominated by custom', 'There is no maker but Him', and 'the way in which the causes exercise their influence ... is unknown'. Exceptions are live and recurring, not limited: prophets' miracles ('actions the like of which it is impossible for other human beings to achieve'), saints' 'acts of divine grace' among Sufis ('None of these things is unworthy of them'), and supernatural perception he reports from his own dream visions. So B 2 (P27 anchor: exceptions not limited). Named alternative 1: Ashʿarite occasionalism read as every event a direct act of God."
      how_known: "Rosenthal translation via a web copy; contested reading, 0.5."
      alternatives:
        - {value: 1, note: "Occasionalism: God the only maker of every event.", cites: [{source: S2, locator: "Ch. VI §14"}]}
    C_ledger: {value: UNKNOWN, how_known: "Paradise and Hell are among the articles of faith he lists, but not scored at this reading (coder's call)."}
    D_authority:
      value: 1
      basis: written_profession
      certainty: 0.5
      cites: [{source: S2, locator: "Ch. VI §14"}]
      rationale: "Revelation outranks reason beyond the intellect's level ('those who give the intellect preference over (traditional) information in such matters are wrong'), and the Lawgiver's command bounds speculation on the chain of causes as it ascends towards God: 'we were forbidden by the Lawgiver (Muhammad) to study causes' (in context, the regress of causes and their hidden influence, not natural inquiry as such). The intellect keeps its own field ('a correct scale ... completely certain'). Named alternative 2: two domains, each with its own authority."
      how_known: "Rosenthal translation via a web copy; 0.5."
      alternatives:
        - {value: 2, note: "Intellect certain in its field; revelation in the divine.", cites: [{source: S2, locator: "Ch. VI §14"}]}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 0 (0.7) is ≤ 1, but B 2 at 0.5 is under the 0.7 bar and B 2 falls between the branches (§6, P19)."}
  statements:
    - text: "It should be known that the things that come into being in the world of existing things, whether they belong to essences or to either human or animal actions, require appropriate causes which are prior to (their coming into being). They introduce the things that come into being into the realm dominated by custom, and effect their coming into being."
      cites: [{source: S2, locator: "Ch. VI §14"}]
      context: "Muqaddimah VI.14, 'The science of speculative theology'; first drafted 1377 and revised to about 1404 (S3). No single year, so the date is left out."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "Rosenthal (Bollingen, 1958; 2nd ed. 1967) via muslimphilosophy.com; print check pending."
    - text: "There is no maker but Him. All (causes) lead up to Him and go back to His power."
      cites: [{source: S2, locator: "Ch. VI §14"}]
      context: "Same section."
      axes: [B_cause, A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "As above."
    - text: "The intellect, indeed, is a correct scale. Its indications are completely certain and in no way wrong. However, the intellect should not be used to weigh such matters as the oneness of God, the other world, the truth of prophecy, the real character of the divine attributes, or anything else that lies beyond the level of the intellect."
      cites: [{source: S2, locator: "Ch. VI §14"}]
      context: "Same section."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "As above."
    - text: "Therefore, we were forbidden by the Lawgiver (Muhammad) to study causes."
      cites: [{source: S2, locator: "Ch. VI §14"}]
      context: "Same section."
      axes: [D_authority, B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "As above."
    - text: "He made it our first obligation to believe that He in His essence cannot be compared with created beings."
      cites: [{source: S2, locator: "Ch. VI §14"}]
      context: "Same section, on the articles of faith."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "As above."
    - text: "are actions the like of which it is impossible for other human beings to achieve. They are, therefore, called \"miracles.\" They are not within the ability of men, but beyond their power."
      cites: [{source: S2, locator: "Ch. I, sixth prefatory discussion"}]
      context: "Muqaddimah I, sixth prefatory discussion, on prophets' 'wonders'; same dating as above."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "As above."
    - text: "With the help of these words, I have myself had remarkable dream visions, through which I learned things about myself that I wanted to know."
      cites: [{source: S2, locator: "Ch. I, sixth prefatory discussion ('Dream words')"}]
      context: "Same discussion."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "As above."
  changes_over_life: []
  coder_notes: "Coder's call: not a scientist under P30 rule 11; the science of culture is a theory of human society, not of physical or natural systems, and it is not the kind of testable claim about organisms the P35 addendum covers. B is scored from his own statements in any case. Britannica's Top Questions not cited (P26). The web copy could not be fetched from the box (timeout), so quotations were checked against the WebFetch reading of the pages."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Arab family of South Arabian descent, long settled in Seville", certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Britannica, from his autobiography."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1377–1382", certainty: 0.5, cites: [{source: S3, locator: "§3"}, {source: S1, locator: "'Journey to Egypt'"}], how_known: "Muqaddimah draft (1377) to the History finished in Tunis before he left in 1382 (P30 #4); 0.5. The Muqaddimah was revised until about 1404 (S3), so the period end could arguably run to 1404 if the revisions count as lasting work (note only, P30 addendum b)."}
  age_at_first_lasting_contribution: {value: 45, certainty: 0.5, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "§3"}], how_known: "1377 − 1332 = 45 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No axis scored at 3 or 4 (P27 anchor)."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "A 0, B 2, D 1.", certainty: 0.5, cites: [{source: S2, locator: "Ch. VI §14"}], how_known: "Coder's reading."}
  worldview_during_major_work: {value: "Ashʿarite Sunni theology: God the only maker; nature as custom", certainty: 0.5, cites: [{source: S2, locator: "Ch. VI §14"}], how_known: "Muqaddimah text; the passages may include later revisions (S3)."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not read.", certainty: 0.5, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Not read."}
  circle_present: {value: "no", rationale: "Transcendent maker; nature as custom.", certainty: 0.5, cites: [{source: S2, locator: "Ch. VI §14"}], how_known: "Coder's reading."}
  reading: "A transcendent God, the only maker, behind a customary natural order with live exceptions."
  notes: ""

institutions:
  - {value: "Court of Fez (Marinid sultan)", role: secretary, years: UNKNOWN, kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Britannica."}
  - {value: "Al-Azhar and the Qamḥiyyah college, Cairo", role: "teacher; professor of jurisprudence", years: "1382–", kind: university, certainty: 0.5, cites: [{source: S1, locator: "'Journey to Egypt'"}], how_known: "Britannica; the kind is the coder's."}
  - {value: "Mamluk judiciary, Cairo", role: "chief judge of the Mālikī rite", years: UNKNOWN, kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "'Journey to Egypt'"}], how_known: "Britannica."}
collaborators:
  - {value: "Ibn al-Khaṭīb", relation: other, note: "friend and rival, prime minister of Granada", certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Britannica."}
  - {value: "Averroës", relation: "influenced by", note: "he wrote summaries of several of his books", certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 101"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Muqaddimah quotations are Rosenthal's translation via a web copy; the text was revised to about 1404, so a passage's layer is not dated."
    - "First lasting year: composition 1377 (author's own date) against presentation in Tunis by 1382."
  open_questions:
    - "Check the quoted passages in the printed Rosenthal (1967) and the Arabic; read VI.30 (refutation of philosophy) and the sorcery sections for B and D; read Lubāb al-Muḥaṣṣal."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Charles Issawi"
    citation: "Issawi, Charles. \"Ibn Khaldūn.\" Encyclopaedia Britannica (revised 5 September 2026). https://www.britannica.com/biography/Ibn-Khaldun, with the pages 'The Muqaddimah: Ibn Khaldūn's philosophy of history' and 'Later years'. Read live 2026-10-18 (the Wayback Machine was rate-limiting)."
    url: "https://www.britannica.com/biography/Ibn-Khaldun"
    accessed: 2026-10-18
    reliability_note: "Signed article. Body only; the AI-generated Top Questions are not cited."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Ibn Khaldūn (trans. Franz Rosenthal)"
    citation: "Ibn Khaldūn. The Muqaddimah: An Introduction to History, trans. Franz Rosenthal (New York: Pantheon/Bollingen, 1958; 2nd ed. Princeton, 1967). Web edition, muslimphilosophy.com: Ch. I sixth prefatory discussion (http://www.muslimphilosophy.com/ik/Muqaddimah/Chapter1/Ch_1_06.htm) and Ch. VI §14 (http://www.muslimphilosophy.com/ik/Muqaddimah/Chapter6/Ch_6_14.htm)."
    url: "http://www.muslimphilosophy.com/ik/Muqaddimah/Chapter6/Ch_6_14.htm"
    accessed: 2026-10-18
    reliability_note: "Web copy of a scholarly translation; secondary quotation, cap 0.7, print check pending."
    used_for: [worldview, timing, lane_b]
  - id: S3
    type: secondary
    kind: "scholarly book"
    author: "Franz Rosenthal"
    citation: "Rosenthal, Franz. \"The Textual History of the Muqaddimah\", translator's introduction to The Muqaddimah (1958/1967). Web edition: http://www.muslimphilosophy.com/ik/Muqaddimah/TransIntro/TexualHistory.htm"
    url: "http://www.muslimphilosophy.com/ik/Muqaddimah/TransIntro/TexualHistory.htm"
    accessed: 2026-10-18
    reliability_note: "Scholarly introduction via a web copy."
    used_for: [basics, contribution, timing, worldview]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-18
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Ibn Khaldun

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Ibn Khaldūn (1332–1406), Arab historian and judge [S1]. Draft: primary_system ISLAM (0.7); A 0 at 0.7; B 2 at 0.5 (alt 1); D 1 at 0.5 (alt 2); mid_basin BELOW_THRESHOLD. Plotted (faded).

## Life and work

Tunis, Fez, Granada, Qalʿat ibn Salāmah, Cairo [S1].

## Contribution and impact

Muqaddimah (draft 1377) and Kitāb al-ʿIbar [S1; S3].

## Childhood and education

Qurʾān, law, letters; parents died in 1349 [S1].

## Adult working worldview

'There is no maker but Him' [S2, VI.14].

## Heritage (context only)

Andalusian Arab family [S1].

## Timing

1377–1382 [S3; S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Nature as custom [S2].

## Open questions

- Print checks of Rosenthal; VI.30.

## Research log

- 2026-10-18: Read Britannica (live, three pages), Rosenthal's translation and introduction on muslimphilosophy.com.
