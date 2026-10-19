---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch R)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-18
  last_updated: 2026-10-18
  change_log:
    - {date: 2026-10-18, by: "Grok Bot", summary: "Record created (stage 3 batch R, order P32: F 4, rank 102). Basics from Britannica (Erwin I. J. Rosenthal, signed; body pages opening, 'Early life', 'Commentaries on Aristotle', 'Averroës’ defense of philosophy' and 'Contents and significance of works', read live). Worldview from the Faṣl al-Maqāl with its appendix in George F. Hourani's translation (1961/1976) and the Tahāfut al-Tahāfut (natural-science discussions) in Simon van den Bergh's translation (1954), both as reproduced on muslimphilosophy.com; web copies, secondary quotation, cap 0.7. Not a scientist (P30, coder's call). primary_system CLASS_THEISM (0.7, alt ISLAM); A 1 (0.7, alt 0); B 3 (0.7, alt 4); D 3 (0.5, alt 2); mid_basin true (0.7). Plotted. Draft, not reviewed."}
    - {date: 2026-10-18, by: "Grok Bot", summary: "Batch R audit fixes (gs_0454445_R run 1). D's second locator is now S3 'Natural Sciences, First Discussion', where the 'divine things which surpass human understanding' sentence stands (IR11); the rationale now says that sentence is about religious principles, among them the prophets' miracles. No value changed."}

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
  full_name: {value: "Abū al-Walīd Muḥammad ibn Aḥmad ibn Muḥammad ibn Rushd", certainty: 0.7, cites: [{source: S1, locator: "header ('Also known as')"}], how_known: "Britannica header line, not Quick Facts or Top Questions; Hourani's text opens 'Abul Walid Muhammad Ibn Ahmad Ibn Rushd' (S2)."}
  native_name: {value: "Ibn Rushd", certainty: 0.7, cites: [{source: S1, locator: "header"}], how_known: "Arabic name; Averroës is the Latin form."}
  aliases:
    - {name: "Averroes", kind: "roster alias"}
    - {name: "Ibn Rushd", kind: "roster alias"}
    - {name: "Ibn Rushd - Averroes", kind: "roster alias"}

basics:
  birth:
    date: {value: "1126", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica body gives the year only."}
    place: {value: "Córdoba", modern_name: "Córdoba, Spain", polity_then: "Almoravid realm (al-Andalus)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Early life'"}], how_known: "Britannica; polity from 'under the Almoravids' (his grandfather's office)."}
  death:
    date: {value: "1198", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica body gives the year only."}
    place: {value: "Marrakech", modern_name: "Marrakech, Morocco", polity_then: "Almohad empire", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1169, certainty: 0.7, cites: [{source: S1, locator: "opening; 'Commentaries on Aristotle'"}], how_known: "The commentaries on Aristotle, written 'Between 1169 and 1195' (S1); a range gives its start year (P12). General Medicine (Kulliyāt, 1162–1169) is his first work, but the body read makes no lasting claim for it, so it is not listed (coder's call; note only)."}
  era_bucket: {value: "500 to 1399", certainty: 0.7, cites: [{source: S1, locator: "'Commentaries on Aristotle'"}], how_known: "1169 (P2)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Spain (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.5, cites: [{source: S1, locator: "'Early life'; 'Averroës’ defense of philosophy'"}], how_known: "Seville and Córdoba as judge and commentator; also Marrakech (Middle East and North Africa) as court physician and at the end; coder's call on the main region."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Arabic"], certainty: 0.7, cites: [{source: S1, locator: "'Commentaries on Aristotle'"}], how_known: "Commentaries 'extant in the Arabic original or Hebrew translations' (S1)."}
  occupations: {value: ["philosopher", "judge (chief qāḍī of Córdoba)", "court physician"], certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}

contribution:
  fields: {value: ["philosophy", "Islamic law", "medicine"], certainty: 0.7, cites: [{source: S1, locator: "'Early life'; 'Averroës’ defense of philosophy'"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Summaries, middle and long commentaries on most of Aristotle's works (and a commentary on Plato's Republic)", year: "1169–1195", kind: "body of work", lasting: "'Averroës’ commentaries exerted considerable influence on Jews and Christians in the following centuries' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Commentaries on Aristotle'"}], how_known: "Britannica dates the series 'Between 1169 and 1195'; start year for the period start (P12), end year for the period end (P30 addendum d)."}
    - {value: "Three religious-philosophical treatises in defence of philosophy: Faṣl al-Maqāl (Decisive Treatise) with its appendix, Kashf al-Manāhij, Tahāfut al-Tahāfut (The Incoherence of the Incoherence)", year: "1179–1180", kind: work, lasting: "'Undoubtedly his most important writings' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Averroës’ defense of philosophy'"}], how_known: "Britannica: 'composed in the years 1179 and 1180'."}
  evidence_of_impact:
    - {value: "Commentaries incorporated in the Latin version of Aristotle's complete works", kind: "institutional or technological lineage", certainty: 0.7, cites: [{source: S1, locator: "'Commentaries on Aristotle'"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Born into a distinguished family of jurists; his grandfather of the same name was chief qāḍī of Córdoba under the Almoravids", role: other, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  household_circumstances: {value: "Distinguished family of jurists at Córdoba", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  schooling:
    - {value: "Traditional Muslim sciences (Qurʾān exegesis, Ḥadīth, fiqh), medicine and philosophy", stage: other, years: UNKNOWN, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica ('Thoroughly versed in ... trained in medicine, and accomplished in philosophy'); stage and years not given."}
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
    - {value: "Sunni Islam; Mālikī jurist (chief qāḍī of Córdoba)", certainty: 0.5, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica names the office; the rite is the coder's reading of Andalusian practice; context only."}
  self_described_science_religion_relation: {value: "The Law commands the demonstrative study of beings, and 'truth does not oppose truth'; where demonstration conflicts with the apparent meaning of Scripture, the text is interpreted allegorically, but the principles of religion (God, prophecy, the next life) and miracles are not to be examined or denied", certainty: 0.7, cites: [{source: S2, locator: "ch. 1; ch. 2 ('Demonstrative truth and scriptural truth cannot conflict')"}, {source: S3, locator: "Natural Sciences, introduction ('The ancient philosophers did not discuss the problem of miracles')"}], how_known: "Hourani and van den Bergh translations via web copies."}
  primary_system:
    value: CLASS_THEISM
    basis: written_profession
    certainty: 0.7
    cites: [{source: S2, locator: "ch. 2 (three classes of being); Appendix (Damima)"}, {source: S3, locator: "Natural Sciences, First Discussion"}, {source: S1, locator: "'Contents and significance of works'"}]
    rationale: "Falsafa in his own writing: God is the pre-eternal being 'apprehended by demonstration ... the Maker, Giver of being and Sustainer of the universe'; God's eternal Knowledge 'is a cause and reason for beings', not an effect of them; the world as a whole is 'neither really originated nor really pre-eternal'; and he defends necessary causes against the Ashʿarites, who 'deny many necessary truths such as ... the existence of necessary causes for effects'. ISLAM's do_not_use_when names Averroes for CLASS_THEISM, and CLASS_THEISM lists him among its key figures. Named alternative ISLAM: Britannica stresses that 'there is only one truth for Averroës, that of the religious law', that he was 'a sincere Muslim', and that the Faṣl calls philosophy 'the companion and foster-sister of the Sharīʿah'."
    how_known: "Published works in scholarly translations via web copies (secondary quotation, cap 0.7); the named alternative also caps at 0.7 (§3)."
  secondary_system: {value: UNKNOWN, how_known: "One system (P29); ISLAM is the named alternative and the nominal affiliation."}
  candidate_codes_considered:
    - {code: CLASS_THEISM, reason: "Demonstrative God, eternal Knowledge as cause of beings, causal necessity in nature (S2, S3)."}
    - {code: ISLAM, reason: "Alternative: the Sharīʿah as the one truth, binding on the philosopher (S1, 'Contents and significance of works')."}
    - {code: ARIST, reason: "Rejected: he keeps prophecy, revelation and the next life as principles that may not be denied (S2, ch. 2)."}
  lio_axes:
    A_locus:
      value: 1
      basis: written_profession
      certainty: 0.7
      cites: [{source: S2, locator: "ch. 2; Appendix (Damima)"}]
      rationale: "Leans to the transcendent pole: God is the pre-eternal being 'not made from or by anything and not preceded by time', the Maker and Sustainer of the universe, whose eternal Knowledge is 'a cause and reason for beings' and 'transcends qualification as \"universal\" or \"particular\"'. A transcendent source whose knowing is unlike any human knowing ('by sheer homonymy'), less personal than the 0 pole, so 1, as for Ibn Sina. Named alternative 0: he insists God knows particulars and acts by knowing ('their issuing from Him is solely due to His knowing')."
      how_known: "Hourani translation via a web copy, secondary quotation, so 0.7 at most."
      alternatives:
        - {value: 0, note: "God knows and makes the world by His knowing; the Damima's 'Does He not know, He who created?'", cites: [{source: S2, locator: "Appendix (Damima)"}]}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      cites: [{source: S3, locator: "Natural Sciences, introduction and First Discussion"}, {source: S2, locator: "ch. 3 (Ashʿarite principles 'sophistical')"}]
      rationale: "Account of nature (P6): denying efficient causes 'observed in sensible things is sophistry'; 'he who denies causes must deny the intellect'; 'this is the wisdom of God and God’s course in created things, and you will never find in God’s course any alteration'. The one stated, limited exception is the prophetic miracle: what is true of the prophet, 'that he can interrupt the ordinary course of nature, is impossible for man, but possible in itself', with the clearest miracle being the Qurʾān, which is 'not an interruption of the course of nature'; miracles are religious principles that 'must not be examined and questioned'. That is the B 3 anchor (accepted miracles as rare, past events; P27). Named alternative 4: the general lawfulness is stated without qualification and the Qurʾān is not an exception."
      how_known: "Van den Bergh and Hourani translations via web copies, secondary quotation, cap 0.7; the named alternative caps at 0.7 (§3)."
      alternatives:
        - {value: 4, note: "No alteration in God's course; the central miracle is not an interruption.", cites: [{source: S3, locator: "Natural Sciences, First Discussion; introduction"}]}
    C_ledger: {value: UNKNOWN, how_known: "Happiness and misery in the next life are among the principles that may not be denied (S2, ch. 2), and the Kashf extract treats the mode of the future life as open to interpretation; not scored at this reading (coder's call)."}
    D_authority:
      value: 3
      basis: written_profession
      certainty: 0.5
      cites: [{source: S2, locator: "ch. 2 ('truth does not oppose truth'; allegorical interpretation; three classes of texts)"}, {source: S3, locator: "Natural Sciences, First Discussion"}]
      rationale: "Leans to reason: 'whenever the conclusion of a demonstration is in conflict with the apparent meaning of Scripture, that apparent meaning admits of allegorical interpretation', and the demonstrative class alone judges such texts. The stated, limited exception: the principles of religion (acknowledgement of God, the prophetic missions, happiness and misery in the next life) are known by every method and may not be interpreted away, and religious principles, among them the prophets' miracles ('they are the principles on which religion is based'), are 'divine things which surpass human understanding, but must be acknowledged although their causes are unknown' (Natural Sciences, First Discussion). So 3. Named alternative 2: Britannica reads the Sharīʿah as the one truth that binds the philosopher, with teachings 'that surpass human understanding but that must be accepted by all believers' (S1)."
      how_known: "Translations via web copies; contested reading, 0.5."
      alternatives:
        - {value: 2, note: "Religious law and philosophy each authoritative; the Sharīʿah binds the philosopher (S1).", cites: [{source: S1, locator: "'Contents and significance of works'"}]}
    E_scope: {value: UNKNOWN, how_known: "Nothing read on the world's order for different kinds of beings (P7)."}
  mid_basin: {value: true, certainty: 0.7, cites: [{source: S2, locator: "ch. 2; Appendix"}, {source: S3, locator: "Natural Sciences, First Discussion"}], how_known: "P4 test: A 1 (≤ 1) at 0.7 and B 3 (≥ 3) at 0.7, B scored on his account of nature (P6, P16). Both at the 0.7 bar, so true; the named alternatives (A 0, B 4) give true as well. Certainty 0.7: no surer than the less certain of A and B (§3)."}
  statements:
    - text: "Now since this religion is true and summons to the study which leads to knowledge of the Truth, we the Muslim community know definitely that demonstrative study does not lead to [conclusions] conflicting with what Scripture has given us; for truth does not oppose truth but accords with it and bears witness to it."
      cites: [{source: S2, locator: "ch. 2 ('Demonstrative truth and scriptural truth cannot conflict')"}]
      context: "Faṣl al-Maqāl, composed 1179–1180 (S1); no single year, so the date is left out. Brackets are Hourani's."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "Hourani, Averroes on the Harmony of Religion and Philosophy (Gibb Memorial, 1961; repr. 1976), e-text on muslimphilosophy.com without Müller's page numbers; print check pending."
    - text: "This being is apprehended by demonstration; it is God, Blessed and Exalted, Who is the Maker, Giver of being and Sustainer of the universe; may He be praised and His Power exalted!"
      cites: [{source: S2, locator: "ch. 2 (three classes of being)"}]
      context: "Same treatise, on the 'pre-eternal' extreme among the three classes of being."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "As above."
    - text: "The way to resolve this difficulty, in our opinion, is to recognize that the position of the eternal Knowledge with respect to beings is different from the position of originated knowledge with respect to beings, in that the existence of beings is a cause and reason for our knowledge, while the eternal Knowledge is a cause and reason for beings."
      cites: [{source: S2, locator: "Appendix (Damima)"}]
      context: "Appendix to the Faṣl on God's knowledge; same period."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "As above."
    - text: "Further, many of the principles on which the Ash’arites based their knowledge are sophistical, for they deny many necessary truths such as the permanence of accidents, the action of things on other things, the existence of necessary causes for effects, of substantial forms, and of secondary causes."
      cites: [{source: S2, locator: "ch. 3"}]
      context: "Faṣl, chapter 3, on the sects."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "As above."
    - text: "To deny the existence of efficient causes which are observed in sensible things is sophistry, and he who defends this doctrine either denies with his tongue what is present in his mind or is carried away by a sophistical doubt which occurs to him concerning this question."
      cites: [{source: S3, locator: "Natural Sciences, First Discussion"}]
      context: "Tahāfut al-Tahāfut, reply to al-Ghazālī's Seventeenth Discussion; composed 1179–1180 (S1)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "Van den Bergh, Averroes' Tahafut al-Tahafut (Gibb Memorial, 1954), e-text on muslimphilosophy.com; print check pending. The web copy carries no page numbers; secondary works cite pp. 318–319 of the 1954 edition for the next passage (lead only)."
    - text: "Now intelligence is nothing but the perception of things with their causes, and in this it distinguishes itself from all the other faculties of apprehension, and he who denies causes must deny the intellect."
      cites: [{source: S3, locator: "Natural Sciences, First Discussion"}]
      context: "Same discussion."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "As above."
    - text: "And this is the wisdom of God and God’s course in created things, and you will never find in God’s course any alteration."
      cites: [{source: S3, locator: "Natural Sciences, First Discussion (end)"}]
      context: "Same discussion, closing the argument that correlates cannot be separated; the phrase echoes Qurʾān 33:62."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "As above."
    - text: "Most things which are possible in themselves are impossible for man, and what is true of the prophet, that he can interrupt the ordinary course of nature, is impossible for man, but possible in itself; and because of this one need not assume that things logically impossible are possible for the prophets"
      cites: [{source: S3, locator: "Natural Sciences, introduction"}]
      context: "Same work, introduction to the natural-science discussions, on miracles."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "As above. The quotation stops mid-sentence; it continues 'and if you observe those miracles whose existence is confirmed, you will find that they are of this kind.'"
    - text: "The ancient philosophers did not discuss the problem of miracles, since according to them such things must not be examined and questioned; for they are the principles of the religions, and the man who inquires into them and doubts them merits punishment"
      cites: [{source: S3, locator: "Natural Sciences, introduction"}]
      context: "Same passage; he states the philosophers' position as his reply ('I say')."
      axes: [D_authority, B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "As above."
  changes_over_life: []
  coder_notes: "Coder's call: not a scientist under P30 rule 11. The commentaries expound Aristotle's natural treatises ('considerable power of observation', S1) but are not listed as his own theory about natural systems, and General Medicine has no lasting claim in what was read. B is scored from his own statements in any case. The Tahāfut passages answer al-Ghazālī, who is quoted at length in the same pages; only sentences after Ibn Rushd's 'I say' are used. Britannica's Top Questions not cited (P26). Leads: SEP 'Ibn Rushd [Averroes]' (Ben Ahmed and Pasnau, 2021/2025) for the mature view of God as final cause (cited in systems/CLASS_THEISM.md, not read here); the Kashf for C and E."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Andalusian Arab family of jurists", certainty: 0.5, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica says 'distinguished family of jurists at Córdoba'; 'Arab' is the coder's reading."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1169–1195", certainty: 0.7, cites: [{source: S1, locator: "'Commentaries on Aristotle'"}], how_known: "First to last listed lasting contribution (P29, P30): the commentaries 1169–1195 contain the 1179–1180 treatises; the range gives its end year (P30 addendum d)."}
  age_at_first_lasting_contribution: {value: 43, certainty: 0.7, cites: [{source: S1, locator: "opening; 'Commentaries on Aristotle'"}], how_known: "1169 − 1126 = 43 (P30)."}
  first_evidence_of_lio_type_views: {value: "1179–1180: causal necessity in nature defended against the Ashʿarites and al-Ghazālī; demonstration decides the reading of Scripture", year: 1179, certainty: 0.5, cites: [{source: S1, locator: "'Averroës’ defense of philosophy'"}, {source: S2, locator: "ch. 2; ch. 3"}, {source: S3, locator: "Natural Sciences, First Discussion"}], how_known: "Earliest dated works read; the commentaries were not read (P30 #7)."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "1179–1180 falls inside 1169–1195.", certainty: 0.7, cites: [{source: S1, locator: "'Averroës’ defense of philosophy'"}], how_known: "Dates of what was read."}
  worldview_during_major_work: {value: "Falsafa within Islam: a demonstrative God, causal necessity in nature, prophetic miracles accepted as principles", certainty: 0.7, cites: [{source: S2, locator: "ch. 2"}, {source: S3, locator: "Natural Sciences"}], how_known: "His own treatises in translation."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "Demonstrative (syllogistic) method made a duty of the Law (S2, ch. 1).", certainty: 0.5, cites: [{source: S2, locator: "ch. 1"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Early life'"}], how_known: "Not read."}
  circle_present: {value: "partly", rationale: "A transcendent Maker whose knowledge causes a lawful order.", certainty: 0.5, cites: [{source: S2, locator: "Appendix"}], how_known: "Coder's reading."}
  reading: "A demonstrative, transcendent cause behind a necessary natural order, with prophecy kept as a principle."
  notes: ""

institutions:
  - {value: "Judiciary of Seville and Córdoba (Almohad state)", role: "judge; chief qāḍī of Córdoba", years: UNKNOWN, kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica; 'The exact year of his appointment ... is not known'."}
  - {value: "Almohad court", role: "personal physician to the caliphs", years: "1182–1195", kind: "government or state body", certainty: 0.5, cites: [{source: S1, locator: "'Early life'; 'Averroës’ defense of philosophy'"}], how_known: "Britannica: physician from 1182; dismissed and banished in 1195; end year is the coder's reading."}
collaborators:
  - {value: "Ibn Ṭufayl", relation: "mentor or employer", note: "introduced him to the caliph; he succeeded him as court physician", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  - {value: "Abū Yaʿqūb Yūsuf", relation: "mentor or employer", note: "caliph who requested the commentaries; dedicatee of the Republic commentary", certainty: 0.7, cites: [{source: S1, locator: "'Early life'; 'Averroës’ defense of philosophy'"}], how_known: "Britannica."}
  - {value: "al-Ghazālī", relation: "rival or critic", note: "the Tahāfut al-Tahāfut answers his attack on the philosophers", certainty: 0.7, cites: [{source: S1, locator: "'Averroës’ defense of philosophy'"}], how_known: "Britannica."}
  - {value: "Aristotle", relation: "influenced by", note: "commented on most of his works", certainty: 0.7, cites: [{source: S1, locator: "'Commentaries on Aristotle'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 102"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Quotations are scholarly translations read in web copies (Hourani; van den Bergh); print check pending."
    - "Birth and death are given by year only in the body read."
  open_questions:
    - "Check the quoted passages in print (Hourani 1961, Müller pagination; van den Bergh 1954) and read SEP 'Ibn Rushd' on God as final cause (A) and on miracles (B)."
    - "Read the Kashf al-Manāhij for C and E."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Erwin I. J. Rosenthal"
    citation: "Rosenthal, Erwin I. J. \"Averroës.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Averroes, with the page 'Contents and significance of works' (https://www.britannica.com/biography/Averroes/Contents-and-significance-of-works). Read live 2026-10-18; no revision date shown on the pages read."
    url: "https://www.britannica.com/biography/Averroes"
    accessed: 2026-10-18
    reliability_note: "Signed article. Body only; the AI-generated Top Questions and the At a Glance box are not cited."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Ibn Rushd (trans. George F. Hourani)"
    citation: "Averroes. On the Harmony of Religion and Philosophy: A Translation, with Introduction and Notes, of Ibn Rushd's Kitāb faṣl al-maqāl, with its Appendix (Ḍamīma) and an Extract from Kitāb al-kashf ʿan manāhij al-adilla, trans. George F. Hourani (London: Luzac for the E. J. W. Gibb Memorial Trust, 1961; repr. 1976). E-text (introduction, notes and Müller page numbers omitted): https://www.muslimphilosophy.com/ir/fasl.htm"
    url: "https://www.muslimphilosophy.com/ir/fasl.htm"
    accessed: 2026-10-18
    reliability_note: "Web copy of a scholarly translation; secondary quotation, cap 0.7; print check pending."
    used_for: [worldview, timing, lane_b]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Ibn Rushd (trans. Simon van den Bergh)"
    citation: "Averroes. Tahafut al-Tahafut (The Incoherence of the Incoherence), trans. Simon van den Bergh (London: Luzac for the E. J. W. Gibb Memorial Trust, 1954). E-text of the natural-science discussions: https://muslimphilosophy.com/ir/tt/tt-ns.htm"
    url: "https://muslimphilosophy.com/ir/tt/tt-ns.htm"
    accessed: 2026-10-18
    reliability_note: "Web copy of a scholarly translation, read in full by direct download; secondary quotation, cap 0.7; print check pending."
    used_for: [worldview, timing]
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

# Ibn Rushd (Averroes)

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Ibn Rushd (1126–1198), Andalusian philosopher, judge and physician [S1]. Draft: primary_system CLASS_THEISM (0.7, alt ISLAM); A 1 at 0.7 (alt 0); B 3 at 0.7 (alt 4); D 3 at 0.5 (alt 2); mid_basin true (0.7). Plotted.

## Life and work

Córdoba, Seville, Marrakech; chief qāḍī and court physician; banished in 1195 and recalled [S1].

## Contribution and impact

Commentaries on Aristotle (1169–1195); Faṣl al-Maqāl, Kashf and Tahāfut al-Tahāfut (1179–1180) [S1].

## Childhood and education

Family of jurists; Qurʾān, Ḥadīth, law, medicine, philosophy [S1].

## Adult working worldview

'truth does not oppose truth' [S2, ch. 2]; 'he who denies causes must deny the intellect' [S3].

## Heritage (context only)

Andalusian family of jurists [S1].

## Timing

1169–1195, from age 43 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. A demonstrative God behind necessary causes [S2; S3].

## Open questions

- Print checks; SEP 'Ibn Rushd'; the Kashf.

## Research log

- 2026-10-18: Read Britannica (live, two pages), Hourani's Faṣl translation (WebFetch) and van den Bergh's Tahāfut natural-science discussions (downloaded by curl) on muslimphilosophy.com.
