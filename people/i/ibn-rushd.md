---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch R; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-18
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-18, by: "Grok Bot", summary: "Record created (stage 3 batch R, order P32: F 4, rank 102). Basics from Britannica (Erwin I. J. Rosenthal, signed; body pages opening, 'Early life', 'Commentaries on Aristotle', 'Averroës’ defense of philosophy' and 'Contents and significance of works', read live). Worldview from the Faṣl al-Maqāl with its appendix in George F. Hourani's translation (1961/1976) and the Tahāfut al-Tahāfut (natural-science discussions) in Simon van den Bergh's translation (1954), both as reproduced on muslimphilosophy.com; web copies, secondary quotation, cap 0.7. Not a scientist (P30, coder's call). primary_system CLASS_THEISM (0.7, alt ISLAM); A 1 (0.7, alt 0); B 3 (0.7, alt 4); D 3 (0.5, alt 2); mid_basin true (0.7). Plotted. Draft, not reviewed."}
    - {date: 2026-10-18, by: "Grok Bot", summary: "Batch R audit fixes (gs_0454445_R run 1). D's second locator is now S3 'Natural Sciences, First Discussion', where the 'divine things which surpass human understanding' sentence stands (IR11); the rationale now says that sentence is about religious principles, among them the prophets' miracles. No value changed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #101 / F4 rank 102). Needs: corroborate A and/or B (hollow→filled if both). Dual bio Wikipedia EN Averroes (S5, P50). P47 source_quality on S1–S7. Primary checks: IA folkscanomy Hourani Decisive Treatise OCR (S6) confirms Faṣl 'Maker, Giver of being', 'truth does not oppose truth', Ashʿarite 'necessary causes' denial; IA open van den Bergh Tahāfut OCR (S7, averroes-incoherence-of-the-incoherence) confirms Natural Sciences efficient-causes / intellect / God's course / miracles passages. A 1 stays @0.7 support corroborated (S2 web + S6 IA Hourani; contested alt 0). B 3 stays @0.7 support corroborated (S3 web + S7 IA Tahāfut + S2 Fasl causes; contested alt 4). primary CLASS_THEISM @0.7 alt ISLAM kept. mid_basin true @0.7 kept. Chart-moving YES: hollow→filled (both A&B corroborated); darkness already dark. Draft deepen report in drafts/ (untracked). No fallacy_catalog. No figures refresh."}

identity:
  id: ibn-rushd
  display_name: "Ibn Rushd (Averroes)"
  roster:
    canonical_name: "Ibn Rushd (Averroes)"
    rank: 102
    F: 4
    models: [Claude, DeepSeek, Gemini, Grok]
    band: "core (3–4)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Abū al-Walīd Muḥammad ibn Aḥmad ibn Muḥammad ibn Rushd", certainty: 0.7, cites: [{source: S1, locator: "header ('Also known as')"}, {source: S5, locator: "Name / lead"}], how_known: "Britannica header; Wikipedia lead forms agree (P15)."}
  native_name: {value: "ابن رشد", certainty: 0.7, cites: [{source: S5, locator: "infobox native name"}], how_known: "Wikipedia Arabic; Averroës is the Latin form."}
  aliases:
    - {name: "Averroes", kind: "roster alias"}
    - {name: "Ibn Rushd", kind: "roster alias"}
    - {name: "Ibn Rushd - Averroes", kind: "roster alias"}
    - {name: "The Commentator", kind: "other"}

basics:
  birth:
    date: {value: "1126-04-14", calendar: gregorian, certainty: 0.7, cites: [{source: S5, locator: "infobox / lead (14 April 1126)"}, {source: S1, locator: "opening (year 1126)"}], how_known: "Wikipedia day+month; Britannica year-only agrees on 1126."}
    place: {value: "Córdoba", modern_name: "Córdoba, Spain", polity_then: "Almoravid realm (al-Andalus)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Early life'"}, {source: S5, locator: "Early life"}], how_known: "Britannica and Wikipedia."}
  death:
    date: {value: "1198-12-11", calendar: gregorian, certainty: 0.7, cites: [{source: S5, locator: "infobox / Death (11 December 1198)"}, {source: S1, locator: "opening (year 1198)"}], how_known: "Wikipedia day+month; Britannica year-only agrees on 1198."}
    place: {value: "Marrakech", modern_name: "Marrakech, Morocco", polity_then: "Almohad empire", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "Death"}], how_known: "Britannica and Wikipedia."}
  first_lasting_contribution_year: {value: 1169, certainty: 0.7, cites: [{source: S1, locator: "opening; 'Commentaries on Aristotle'"}, {source: S5, locator: "Career (commentaries begin 1169)"}], how_known: "The commentaries on Aristotle, written 'Between 1169 and 1195' (S1); a range gives its start year (P12). General Medicine (Kulliyāt, ~1162) is earlier, but lasting claim in what was read is for the commentaries (coder's call)."}
  era_bucket: {value: "500 to 1399", certainty: 0.7, cites: [{source: S1, locator: "'Commentaries on Aristotle'"}], how_known: "1169 (P2)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "infobox"}], how_known: "Spain (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.5, cites: [{source: S1, locator: "'Early life'; 'Averroës’ defense of philosophy'"}, {source: S5, locator: "Career"}], how_known: "Seville and Córdoba as judge and commentator; also Marrakech (Middle East and North Africa) as court physician and at the end; coder's call on the main region."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S5, locator: "lead"}], how_known: "As recorded."}
  languages_of_work: {value: ["Arabic"], certainty: 0.7, cites: [{source: S1, locator: "'Commentaries on Aristotle'"}], how_known: "Commentaries 'extant in the Arabic original or Hebrew translations' (S1)."}
  occupations: {value: ["philosopher", "judge (chief qāḍī of Córdoba)", "court physician"], certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S5, locator: "Career"}], how_known: "Britannica and Wikipedia."}

contribution:
  fields: {value: ["philosophy", "Islamic law", "medicine"], certainty: 0.7, cites: [{source: S1, locator: "'Early life'; 'Averroës’ defense of philosophy'"}, {source: S5, locator: "lead"}], how_known: "Britannica and Wikipedia."}
  lasting_original_contributions:
    - {value: "Summaries, middle and long commentaries on most of Aristotle's works (and a commentary on Plato's Republic)", year: "1169–1195", kind: "body of work", lasting: "'Averroës’ commentaries exerted considerable influence on Jews and Christians in the following centuries' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Commentaries on Aristotle'"}, {source: S5, locator: "Commentaries on Aristotle"}], how_known: "Britannica dates the series 'Between 1169 and 1195'; start year for the period start (P12), end year for the period end (P30 addendum d)."}
    - {value: "Three religious-philosophical treatises in defence of philosophy: Faṣl al-Maqāl (Decisive Treatise) with its appendix, Kashf al-Manāhij, Tahāfut al-Tahāfut (The Incoherence of the Incoherence)", year: "1179–1180", kind: work, lasting: "'Undoubtedly his most important writings' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Averroës’ defense of philosophy'"}, {source: S5, locator: "Islamic theology"}], how_known: "Britannica: 'composed in the years 1179 and 1180'; Wikipedia dates Faṣl ~1178, Kashf 1179, Tahāfut 1180."}
  evidence_of_impact:
    - {value: "Commentaries incorporated in the Latin version of Aristotle's complete works", kind: "institutional or technological lineage", certainty: 0.7, cites: [{source: S1, locator: "'Commentaries on Aristotle'"}], how_known: "Britannica."}
    - {value: "Latin Averroism and condemnations of 1270 and 1277; Jewish reception from Maimonides onward", kind: "scholarly consensus", certainty: 0.5, cites: [{source: S5, locator: "Legacy"}], how_known: "Wikipedia secondary consensus."}
  major_works:
    - {value: "Faṣl al-Maqāl (Decisive Treatise / On the Harmony of Religion and Philosophy)", year: "1179–1180", kind: "book", certainty: 0.7, cites: [{source: S1, locator: "'Averroës’ defense of philosophy'"}, {source: S6, locator: "title (Hourani)"}, {source: S5, locator: "Islamic theology"}], how_known: "Britannica; Hourani edition; Wikipedia."}
    - {value: "Tahāfut al-Tahāfut (The Incoherence of the Incoherence)", year: 1180, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "'Averroës’ defense of philosophy'"}, {source: S7, locator: "title (van den Bergh)"}, {source: S5, locator: "Islamic theology"}], how_known: "Britannica; van den Bergh edition; Wikipedia."}
    - {value: "Commentaries on Aristotle (short, middle, long)", year: "1169–1195", kind: "other", certainty: 0.7, cites: [{source: S1, locator: "'Commentaries on Aristotle'"}, {source: S5, locator: "Commentaries on Aristotle"}], how_known: "Britannica and Wikipedia."}
    - {value: "al-Kulliyāt fī al-Ṭibb (Colliget)", year: "c. 1162–1169", kind: "book", certainty: 0.5, cites: [{source: S5, locator: "Medicine"}, {source: S1, locator: "'Early life'"}], how_known: "Wikipedia; Britannica notes medical training without dating the lasting claim."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1; S5).", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "lead"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Sunni Islam (Andalusian Mālikī jurist family)", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S5, locator: "Early life and education"}], how_known: "Britannica and Wikipedia; context only."}
  family_religious_practice: {value: "Grandfather and father served as chief qāḍī of Córdoba; childhood training in ḥadīth, fiqh, medicine", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S5, locator: "Early life and education"}], how_known: "Britannica and Wikipedia."}
  parents_and_household:
    - {value: "Born into a distinguished family of jurists; his grandfather of the same name was chief qāḍī of Córdoba under the Almoravids; father also a judge", role: other, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S5, locator: "Early life"}], how_known: "Britannica and Wikipedia."}
  household_circumstances: {value: "Distinguished family of jurists at Córdoba", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S5, locator: "Early life"}], how_known: "Britannica and Wikipedia."}
  schooling:
    - {value: "Traditional Muslim sciences (Qurʾān exegesis, Ḥadīth, fiqh), medicine and philosophy; Mālikī jurisprudence; studied Ashʿarī kalām which he later criticized", stage: other, years: UNKNOWN, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S5, locator: "Early life and education"}], how_known: "Britannica and Wikipedia; stage and years not given."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["Arabic"], certainty: 0.5, cites: [{source: S1, locator: "'Early life'"}], how_known: "Coder's reading."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1169–1195", certainty: 0.7, cites: [{source: S1, locator: "'Commentaries on Aristotle'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Sunni Islam; Mālikī jurist (chief qāḍī of Córdoba)", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S5, locator: "Career / Jurisprudence"}], how_known: "Britannica and Wikipedia; context only."}
  self_described_science_religion_relation: {value: "The Law commands the demonstrative study of beings, and 'truth does not oppose truth'; where demonstration conflicts with the apparent meaning of Scripture, the text is interpreted allegorically, but the principles of religion (God, prophecy, the next life) and miracles are not to be examined or denied", certainty: 0.7, cites: [{source: S2, locator: "ch. 1; ch. 2 ('Demonstrative truth and scriptural truth cannot conflict')"}, {source: S6, locator: "Faṣl (IA OCR, same passages)"}, {source: S3, locator: "Natural Sciences, introduction ('The ancient philosophers did not discuss the problem of miracles')"}, {source: S7, locator: "Natural Sciences introduction (IA OCR)"}], how_known: "Hourani and van den Bergh; web copies corroborated by IA OCR."}
  primary_system:
    value: CLASS_THEISM
    basis: written_profession
    certainty: 0.7
    cites: [{source: S2, locator: "ch. 2 (three classes of being); Appendix (Damima)"}, {source: S6, locator: "Faṣl ch. 2 (IA OCR)"}, {source: S3, locator: "Natural Sciences, First Discussion"}, {source: S7, locator: "Natural Sciences, First Discussion (IA OCR)"}, {source: S1, locator: "'Contents and significance of works'"}]
    rationale: "Falsafa in his own writing: God is the pre-eternal being 'apprehended by demonstration ... the Maker, Giver of being and Sustainer of the universe'; God's eternal Knowledge 'is a cause and reason for beings', not an effect of them; the world as a whole is 'neither really originated nor really pre-eternal'; and he defends necessary causes against the Ashʿarites, who 'deny many necessary truths such as ... the existence of necessary causes for effects'. ISLAM's do_not_use_when names Averroes for CLASS_THEISM, and CLASS_THEISM lists him among its key figures. Named alternative ISLAM: Britannica stresses that 'there is only one truth for Averroës, that of the religious law', that he was 'a sincere Muslim', and that the Faṣl calls philosophy 'the companion and foster-sister of the Sharīʿah'."
    how_known: "Published works in scholarly translations; muslimphilosophy web (S2, S3) corroborated by IA OCR of Hourani (S6) and van den Bergh (S7). Contested alt ISLAM keeps certainty at most 0.7 (§3)."
    alternatives:
      - {value: ISLAM, note: "Sharīʿah as the one truth; sincere Muslim jurist; philosophy the milk-sister of religion (S1, S2/S6).", cites: [{source: S1, locator: "'Contents and significance of works'"}, {source: S2, locator: "ch. 3 (philosophy friend and milk-sister of religion)"}, {source: S6, locator: "Faṣl closing (IA OCR)"}]}
  secondary_system: {value: UNKNOWN, how_known: "One system (P29); ISLAM is the named alternative and the nominal affiliation."}
  candidate_codes_considered:
    - {code: CLASS_THEISM, reason: "Demonstrative God, eternal Knowledge as cause of beings, causal necessity in nature (S2, S3, S6, S7)."}
    - {code: ISLAM, reason: "Alternative: the Sharīʿah as the one truth, binding on the philosopher (S1, 'Contents and significance of works')."}
    - {code: ARIST, reason: "Rejected: he keeps prophecy, revelation and the next life as principles that may not be denied (S2/S6, ch. 2)."}
  lio_axes:
    A_locus:
      value: 1
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S2, locator: "ch. 2; Appendix (Damima)"}, {source: S6, locator: "Faṣl ch. 2 (IA OCR: 'Maker, Giver of being'; Knowledge transcends universal/particular; sheer homonymy)"}]
      rationale: "Leans to the transcendent pole: God is the pre-eternal being 'not made from or by anything and not preceded by time', the Maker and Sustainer of the universe, whose eternal Knowledge is 'a cause and reason for beings' and 'transcends qualification as \"universal\" or \"particular\"'. A transcendent source whose knowing is unlike any human knowing ('by sheer homonymy'), less personal than the 0 pole, so 1, as for Ibn Sina. Named alternative 0: he insists God knows particulars and acts by knowing ('their issuing from Him is solely due to His knowing'; Damima 'Does He not know, He who created?')."
      how_known: "Hourani via muslimphilosophy web (S2) corroborated by IA folkscanomy OCR of Hourani Decisive Treatise (S6) — distinct source ids → corroborated (P48). Contested alt 0 keeps certainty at most 0.7 (P25). Damima appendix wording checked on S2; Fasl Maker/Knowledge passages hold on both."
      alternatives:
        - {value: 0, note: "God knows and makes the world by His knowing; the Damima's 'Does He not know, He who created?'", cites: [{source: S2, locator: "Appendix (Damima)"}]}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S3, locator: "Natural Sciences, introduction and First Discussion"}, {source: S7, locator: "Natural Sciences, introduction and First Discussion (IA OCR van den Bergh)"}, {source: S2, locator: "ch. 3 (Ashʿarite principles 'sophistical')"}, {source: S6, locator: "Faṣl ch. 3 (IA OCR, necessary causes)"}]
      rationale: "Account of nature (P6): denying efficient causes 'observed in sensible things is sophistry'; 'he who denies causes must deny the intellect'; 'this is the wisdom of God and God’s course in created things, and you will never find in God’s course any alteration'. The one stated, limited exception is the prophetic miracle: what is true of the prophet, 'that he can interrupt the ordinary course of nature, is impossible for man, but possible in itself', with the clearest miracle being the Qurʾān, which is 'not an interruption of the course of nature'; miracles are religious principles that 'must not be examined and questioned'. That is the B 3 anchor (accepted miracles as rare, past events; P27). Named alternative 4: the general lawfulness is stated without qualification and the Qurʾān is not an exception."
      how_known: "Van den Bergh web (S3) corroborated by IA open OCR of the same translation (S7); Fasl Ashʿarite-causes passage on S2+S6. Distinct ids → corroborated (P48). Contested alt 4 keeps certainty at most 0.7 (P25). Not a scientist (P30): scored from own-voice nature account."
      alternatives:
        - {value: 4, note: "No alteration in God's course; the central miracle is not an interruption.", cites: [{source: S3, locator: "Natural Sciences, First Discussion; introduction"}, {source: S7, locator: "Natural Sciences, First Discussion; introduction (IA OCR)"}]}
    C_ledger: {value: UNKNOWN, how_known: "Happiness and misery in the next life are among the principles that may not be denied (S2/S6, ch. 2), and the Kashf extract treats the mode of the future life as open to interpretation; not scored at this reading (coder's call)."}
    D_authority:
      value: 3
      basis: written_profession
      certainty: 0.5
      support: single
      cites: [{source: S2, locator: "ch. 2 ('truth does not oppose truth'; allegorical interpretation; three classes of texts)"}, {source: S6, locator: "Faṣl ch. 2 (IA OCR)"}, {source: S3, locator: "Natural Sciences, First Discussion"}, {source: S7, locator: "Natural Sciences, First Discussion (IA OCR)"}]
      rationale: "Leans to reason: 'whenever the conclusion of a demonstration is in conflict with the apparent meaning of Scripture, that apparent meaning admits of allegorical interpretation', and the demonstrative class alone judges such texts. The stated, limited exception: the principles of religion (acknowledgement of God, the prophetic missions, happiness and misery in the next life) are known by every method and may not be interpreted away, and religious principles, among them the prophets' miracles ('they are the principles on which religion is based'), are 'divine things which surpass human understanding, but must be acknowledged although their causes are unknown' (Natural Sciences, First Discussion). So 3. Named alternative 2: Britannica reads the Sharīʿah as the one truth that binds the philosopher, with teachings 'that surpass human understanding but that must be accepted by all believers' (S1)."
      how_known: "S2+S6 and S3+S7 agree; contested alt 2 → certainty stays 0.5 (coder's call; D not a deepen target)."
      alternatives:
        - {value: 2, note: "Religious law and philosophy each authoritative; the Sharīʿah binds the philosopher (S1).", cites: [{source: S1, locator: "'Contents and significance of works'"}]}
    E_scope: {value: UNKNOWN, how_known: "Nothing read on the world's order for different kinds of beings (P7)."}
  mid_basin: {value: true, certainty: 0.7, cites: [{source: S2, locator: "ch. 2; Appendix"}, {source: S6, locator: "Faṣl ch. 2 (IA OCR)"}, {source: S3, locator: "Natural Sciences, First Discussion"}, {source: S7, locator: "Natural Sciences, First Discussion (IA OCR)"}], how_known: "P4 test: A 1 (≤ 1) at 0.7 and B 3 (≥ 3) at 0.7, B scored on his account of nature (P6, P16). Both at the 0.7 bar, so true; the named alternatives (A 0, B 4) give true as well. Certainty 0.7: no surer than the less certain of A and B (§3). Deepen D1 did not change values."}
  statements:
    - text: "Now since this religion is true and summons to the study which leads to knowledge of the Truth, we the Muslim community know definitely that demonstrative study does not lead to [conclusions] conflicting with what Scripture has given us; for truth does not oppose truth but accords with it and bears witness to it."
      cites: [{source: S6, locator: "Faṣl ch. 2 (IA OCR)"}, {source: S2, locator: "ch. 2 ('Demonstrative truth and scriptural truth cannot conflict')"}]
      context: "Faṣl al-Maqāl, composed 1179–1180 (S1); no single year, so the date is left out. Brackets are Hourani's."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Deepen D1: checked against IA folkscanomy Hourani OCR (S6)."
    - text: "This being is apprehended by demonstration; it is God, Blessed and Exalted, Who is the Maker, Giver of being and Sustainer of the universe; may He be praised and His Power exalted!"
      cites: [{source: S6, locator: "Faṣl ch. 2 three classes of being (IA OCR)"}, {source: S2, locator: "ch. 2 (three classes of being)"}]
      context: "Same treatise, on the 'pre-eternal' extreme among the three classes of being."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "As above."
    - text: "The way to resolve this difficulty, in our opinion, is to recognize that the position of the eternal Knowledge with respect to beings is different from the position of originated knowledge with respect to beings, in that the existence of beings is a cause and reason for our knowledge, while the eternal Knowledge is a cause and reason for beings."
      cites: [{source: S2, locator: "Appendix (Damima)"}]
      context: "Appendix to the Faṣl on God's knowledge; same period. Folkscanomy OCR used this pass covers the main Faṣl; Damima wording re-checked on the muslimphilosophy web copy (S2)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Damima still web-only this pass; Fasl Maker passages hold on S6."
    - text: "Further, many of the principles on which the Ash’arites based their knowledge are sophistical, for they deny many necessary truths such as the permanence of accidents, the action of things on other things, the existence of necessary causes for effects, of substantial forms, and of secondary causes."
      cites: [{source: S6, locator: "Faṣl ch. 3 (IA OCR)"}, {source: S2, locator: "ch. 3"}]
      context: "Faṣl, chapter 3, on the sects."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "As above."
    - text: "To deny the existence of efficient causes which are observed in sensible things is sophistry, and he who defends this doctrine either denies with his tongue what is present in his mind or is carried away by a sophistical doubt which occurs to him concerning this question."
      cites: [{source: S7, locator: "Natural Sciences, First Discussion (IA OCR)"}, {source: S3, locator: "Natural Sciences, First Discussion"}]
      context: "Tahāfut al-Tahāfut, reply to al-Ghazālī's Seventeenth Discussion; composed 1179–1180 (S1)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Deepen D1: checked against IA open van den Bergh OCR (S7)."
    - text: "Now intelligence is nothing but the perception of things with their causes, and in this it distinguishes itself from all the other faculties of apprehension, and he who denies causes must deny the intellect."
      cites: [{source: S7, locator: "Natural Sciences, First Discussion (IA OCR)"}, {source: S3, locator: "Natural Sciences, First Discussion"}]
      context: "Same discussion."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "As above."
    - text: "And this is the wisdom of God and God’s course in created things, and you will never find in God’s course any alteration."
      cites: [{source: S7, locator: "Natural Sciences, First Discussion end (IA OCR)"}, {source: S3, locator: "Natural Sciences, First Discussion (end)"}]
      context: "Same discussion, closing the argument that correlates cannot be separated; the phrase echoes Qurʾān 33:62."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "As above."
    - text: "Most things which are possible in themselves are impossible for man, and what is true of the prophet, that he can interrupt the ordinary course of nature, is impossible for man, but possible in itself; and because of this one need not assume that things logically impossible are possible for the prophets"
      cites: [{source: S7, locator: "Natural Sciences, introduction (IA OCR)"}, {source: S3, locator: "Natural Sciences, introduction"}]
      context: "Same work, introduction to the natural-science discussions, on miracles."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "As above. Continues 'and if you observe those miracles whose existence is confirmed, you will find that they are of this kind.'"
    - text: "The ancient philosophers did not discuss the problem of miracles, since according to them such things must not be examined and questioned; for they are the principles of the religions, and the man who inquires into them and doubts them merits punishment"
      cites: [{source: S7, locator: "Natural Sciences, introduction (IA OCR)"}, {source: S3, locator: "Natural Sciences, introduction"}]
      context: "Same passage; he states the philosophers' position as his reply ('I say')."
      axes: [D_authority, B_cause]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "As above."
  changes_over_life: []
  coder_notes: "Deepen D1. Not a scientist under P30 rule 11. B scored from own-voice nature account. Chart cues after D1: dark + filled (A&B both @0.7 corroborated). mid_basin true @0.7 unchanged. Britannica Top Questions not cited (P26). Damima appendix still web-only; print Hourani with Müller pagination and borrow-restricted Gibb Tahāfut still open. Leads: SEP 'Ibn Rushd' (Ben Ahmed and Pasnau); Kashf for C and E; Butterworth parallel Faṣl."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Andalusian Arab family of jurists", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S5, locator: "Early life"}], how_known: "Britannica and Wikipedia."}
  religious_heritage_by_birth: {value: "Sunni Islam", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S5, locator: "Early life and education"}], how_known: "Britannica and Wikipedia; context only."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1169–1195", certainty: 0.7, cites: [{source: S1, locator: "'Commentaries on Aristotle'"}], how_known: "First to last listed lasting contribution (P29, P30): the commentaries 1169–1195 contain the 1179–1180 treatises; the range gives its end year (P30 addendum d)."}
  age_at_first_lasting_contribution: {value: 43, certainty: 0.7, cites: [{source: S1, locator: "opening; 'Commentaries on Aristotle'"}, {source: S5, locator: "infobox (b. 1126)"}], how_known: "1169 − 1126 = 43 (P30)."}
  first_evidence_of_lio_type_views: {value: "1179–1180: causal necessity in nature defended against the Ashʿarites and al-Ghazālī; demonstration decides the reading of Scripture", year: 1179, certainty: 0.5, cites: [{source: S1, locator: "'Averroës’ defense of philosophy'"}, {source: S2, locator: "ch. 2; ch. 3"}, {source: S3, locator: "Natural Sciences, First Discussion"}], how_known: "Earliest dated works read; the commentaries were not read (P30 #7)."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "1179–1180 falls inside 1169–1195.", certainty: 0.7, cites: [{source: S1, locator: "'Averroës’ defense of philosophy'"}], how_known: "Dates of what was read."}
  worldview_during_major_work: {value: "Falsafa within Islam: a demonstrative God, causal necessity in nature, prophetic miracles accepted as principles", certainty: 0.7, cites: [{source: S2, locator: "ch. 2"}, {source: S6, locator: "Faṣl ch. 2"}, {source: S3, locator: "Natural Sciences"}, {source: S7, locator: "Natural Sciences"}], how_known: "His own treatises in translation."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "Demonstrative (syllogistic) method made a duty of the Law (S2/S6, ch. 1).", certainty: 0.5, cites: [{source: S2, locator: "ch. 1"}, {source: S6, locator: "Faṣl ch. 1"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Early life'"}], how_known: "Not read."}
  circle_present: {value: "partly", rationale: "A transcendent Maker whose knowledge causes a lawful order.", certainty: 0.5, cites: [{source: S2, locator: "Appendix"}, {source: S6, locator: "Faṣl ch. 2"}], how_known: "Coder's reading."}
  reading: "A demonstrative, transcendent cause behind a necessary natural order, with prophecy kept as a principle."
  notes: "Lane B only. B 3 with named alt 4; A 1 with named alt 0."

institutions:
  - {value: "Judiciary of Seville and Córdoba (Almohad state)", role: "judge; chief qāḍī of Córdoba", years: UNKNOWN, kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S5, locator: "Career"}], how_known: "Britannica and Wikipedia."}
  - {value: "Almohad court", role: "personal physician to the caliphs", years: "1182–1195", kind: "government or state body", certainty: 0.5, cites: [{source: S1, locator: "'Early life'; 'Averroës’ defense of philosophy'"}, {source: S5, locator: "Career"}], how_known: "Britannica: physician from 1182; dismissed and banished in 1195; end year is the coder's reading."}
collaborators:
  - {value: "Ibn Ṭufayl", relation: "mentor or employer", note: "introduced him to the caliph; he succeeded him as court physician", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S5, locator: "Career"}], how_known: "Britannica and Wikipedia."}
  - {value: "Abū Yaʿqūb Yūsuf", relation: "mentor or employer", note: "caliph who requested the commentaries; dedicatee of the Republic commentary", certainty: 0.7, cites: [{source: S1, locator: "'Early life'; 'Averroës’ defense of philosophy'"}, {source: S5, locator: "Career"}], how_known: "Britannica and Wikipedia."}
  - {value: "al-Ghazālī", relation: "rival or critic", note: "the Tahāfut al-Tahāfut answers his attack on the philosophers", certainty: 0.7, cites: [{source: S1, locator: "'Averroës’ defense of philosophy'"}, {source: S5, locator: "Islamic theology"}], how_known: "Britannica and Wikipedia."}
  - {value: "Aristotle", relation: "influenced by", note: "commented on most of his works", certainty: 0.7, cites: [{source: S1, locator: "'Commentaries on Aristotle'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 102"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Faṣl and Tahāfut quotations checked in IA OCR of Hourani folkscanomy (S6) and open van den Bergh (S7); Damima appendix still web-only; borrow-restricted Gibb print Tahāfut and clean Hourani print with Müller pagination still open."
    - "Birth/death day-month from Wikipedia; Britannica year-only agrees."
  open_questions:
    - "Print Hourani 1961 with Müller pagination; borrow-restricted Gibb Tahāfut page-images; Butterworth parallel Faṣl; SEP 'Ibn Rushd' on God as final cause (A) and miracles (B)."
    - "Read the Kashf al-Manāhij for C and E."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Erwin I. J. Rosenthal"
    citation: "Rosenthal, Erwin I. J. \"Averroës.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Averroes, with the page 'Contents and significance of works'. Read live 2026-10-18. Deepen D1 2026-10-24: body retained; dual bio with S5."
    url: "https://www.britannica.com/biography/Averroes"
    accessed: 2026-10-18
    source_quality: "reference entry"
    reliability_note: "Signed article. Body only; the AI-generated Top Questions and the At a Glance box are not cited (P26)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Ibn Rushd (trans. George F. Hourani)"
    citation: "Averroes. On the Harmony of Religion and Philosophy: A Translation, with Introduction and Notes, of Ibn Rushd's Kitāb faṣl al-maqāl, with its Appendix (Ḍamīma) and an Extract from Kitāb al-kashf ʿan manāhij al-adilla, trans. George F. Hourani (London: Luzac for the E. J. W. Gibb Memorial Trust, 1961; repr. 1976). E-text: https://www.muslimphilosophy.com/ir/fasl.htm"
    url: "https://www.muslimphilosophy.com/ir/fasl.htm"
    accessed: 2026-10-18
    source_quality: "unofficial web copy"
    reliability_note: "Web copy of a scholarly translation. Deepen D1: Faṣl main wording checked against IA OCR (S6); Damima appendix still from this web copy."
    used_for: [worldview, timing, lane_b]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Ibn Rushd (trans. Simon van den Bergh)"
    citation: "Averroes. Tahafut al-Tahafut (The Incoherence of the Incoherence), trans. Simon van den Bergh (London: Luzac for the E. J. W. Gibb Memorial Trust, 1954). E-text of the natural-science discussions: https://muslimphilosophy.com/ir/tt/tt-ns.htm"
    url: "https://muslimphilosophy.com/ir/tt/tt-ns.htm"
    accessed: 2026-10-18
    source_quality: "unofficial web copy"
    reliability_note: "Web copy of a scholarly translation. Deepen D1: Natural Sciences passages checked against IA open OCR (S7)."
    used_for: [worldview, timing]
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
    citation: "Wikipedia contributors. \"Averroes.\" Wikipedia. https://en.wikipedia.org/wiki/Averroes. Dual bio (P50). Read 2026-10-24."
    url: "https://en.wikipedia.org/wiki/Averroes"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Used for dual-bio basics, dates, works list, family. Worldview A/B scoring does not rest on Wikipedia paraphrases of theology."
    used_for: [identity, basics, contribution, childhood, heritage, institutions, collaborators]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Ibn Rushd (trans. George F. Hourani)"
    citation: "Ibn Rushd. The Decisive Treatise [Hourani]. Internet Archive folkscanomy OCR: https://archive.org/details/ibn-rushd-averroes-the-decisive-treatise-hourani (DjVuTXT). Faṣl main text including Maker / truth-does-not-oppose / Ashʿarite necessary-causes passages. Read 2026-10-24. (Gibb print Hourani also at averroesonharmon0000geor, borrow-restricted this pass.)"
    url: "https://archive.org/details/ibn-rushd-averroes-the-decisive-treatise-hourani"
    accessed: 2026-10-24
    source_quality: "archive scan (OCR only)"
    reliability_note: "OCR of Hourani translation. Distinct id from S2 web copy → P48 corroborated for A and Fasl B cites. Damima appendix not in this scan."
    used_for: [worldview, contribution, timing, lane_b]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "Ibn Rushd (trans. Simon van den Bergh)"
    citation: "Averroes. Tahafut al-Tahafut (The Incoherence of the Incoherence), trans. Simon van den Bergh. Internet Archive open OCR: https://archive.org/details/averroes-incoherence-of-the-incoherence (DjVuTXT). Natural Sciences introduction and First Discussion — efficient causes, intellect, God's course, miracles. Read 2026-10-24. (Gibb print items averroestahafuta0000simo* were 401/borrow-restricted this pass.)"
    url: "https://archive.org/details/averroes-incoherence-of-the-incoherence"
    accessed: 2026-10-24
    source_quality: "archive scan (OCR only)"
    reliability_note: "OCR of van den Bergh translation. Distinct id from S3 web copy → P48 corroborated for B. Clean print page-images still open."
    used_for: [worldview, contribution, timing]
---

# Ibn Rushd (Averroes)

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Ibn Rushd (1126–1198), Andalusian philosopher, judge and physician [S1; S5]. Deepen D1: primary_system CLASS_THEISM (0.7, alt ISLAM); A 1 at 0.7 corroborated (alt 0); B 3 at 0.7 corroborated (alt 4); D 3 at 0.5 (alt 2); mid_basin true (0.7). Plotted dark filled (was dark hollow). Chart-moving YES (fill).

## Life and work

Córdoba, Seville, Marrakech; chief qāḍī and court physician; banished in 1195 and recalled [S1; S5].

## Contribution and impact

Commentaries on Aristotle (1169–1195); Faṣl al-Maqāl, Kashf and Tahāfut al-Tahāfut (1179–1180) [S1; S5; S6; S7].

## Childhood and education

Family of Mālikī jurists; Qurʾān, Ḥadīth, law, medicine, philosophy [S1; S5].

## Adult working worldview

'truth does not oppose truth' [S2; S6]; 'he who denies causes must deny the intellect' [S3; S7].

## Heritage (context only)

Andalusian Arab family of jurists; Sunni Islam [S1; S5].

## Timing

1169–1195, from age 43 [S1; S5].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. A demonstrative God behind necessary causes [S2; S3; S6; S7].

## Open questions

- Print Hourani / Gibb Tahāfut page-images; Damima on archive; SEP; Kashf.

## Research log

- 2026-10-18: Read Britannica (live, two pages), Hourani's Faṣl translation (WebFetch) and van den Bergh's Tahāfut natural-science discussions (downloaded by curl) on muslimphilosophy.com.
- 2026-10-24: Deepen D1 — IA Hourani folkscanomy OCR (S6), IA open van den Bergh Tahāfut OCR (S7), Wikipedia dual bio; A and B corroborated; person-file-only commit.
