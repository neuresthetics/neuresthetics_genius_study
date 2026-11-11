---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to astronomy. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #136, F3 rank 140). Opened Chronology of Ancient Nations (Sachau 1879 Eng., S6 archive.org PDF/OCR): Creator 'high above' anthropomorphic essence/qualities (p. 23); 'all-wise and almighty Creator' who created mountains (pp. 252–253); Jesus 'in His earthly life subject to the laws of nature' (p. 290); nature preserves genera/species, irregularities show Creator designed deviations from the 'general tenor of things' (p. 295). A_locus 0 0.5→0.7 (written_profession; support corroborated India+Chronology); B_cause 3 0.5→0.7 (same; alt 4 held — Creator-designed deviations + miracle-as-departure block exceptionless B 4); mid_basin BELOW→true @0.7. Chart-moving YES (faded→dark; hollow→filled). P47 source_quality on S1–S7; P50 Wikipedia EN (S7) dual bio (birth agrees; death still disputed). No fallacy_catalog; no figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z1 audit fixes (blind audit /workspace/genius_study_audit/gs_8813a47_Z1/run1/): Z1-11: the Great Bear 'laws of nature' sentence is on Sachau vol. I p. 352 (was 353) everywhere. No score changed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z1, order P32: F 3, rank 140). Basics from Britannica (George Saliba, signed) and Encyclopaedia Iranica (Bosworth, 'Life'; de Blois, 'History of Religions'). Own voice read in Sachau's translation of the India (1910, archive.org scan): 'We Muslims ... considering all men as equal, except in piety' (I, p. 100); the Koran's sentences 'perfectly clear' and revealed (I, pp. 263–264); a Hindu theory rejected because the Great Bear would 'form an exception to the laws of nature' (I, p. 353); the rare thing becomes 'something like a miracle, which is no longer in accordance with the ordinary laws of nature' (I, p. 179). A scientist (P30: Masʿudic Canon, coordinates of places); his astrology is taught but personally discounted (S1), so it does not cut the inference (contrast al-Khwarizmi). Span 1000–1030 (first year at 0.5). primary_system ISLAM (0.7); A 0 (0.5, alt 1); B 3 (0.5, alt 4); C UNKNOWN; D BELOW_THRESHOLD; E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Plotted (faded) at the next chart refresh. Draft, not reviewed."}

identity:
  id: al-biruni
  display_name: "Al-Biruni"
  roster:
    canonical_name: "Al-Biruni"
    rank: 140
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: core
    field: polymath
    field_bucket: polymath
  full_name: {value: "Abū al-Rayḥān Muḥammad ibn Aḥmad al-Bīrūnī", certainty: 1.0, cites: [{source: S1, locator: "'In full'"}, {source: S2, locator: "heading ('BĪRŪNĪ, ABŪ RAYḤĀN MOḤAMMAD b. Aḥmad')"}], how_known: "Britannica and Iranica agree, differing only in transliteration (P15 name form gives 0.7 if read strictly; both give the same name, so 1.0 is kept for the name itself)."}
  native_name: {value: "أبو الريحان محمد بن أحمد البيروني", certainty: 0.5, cites: [{source: S1, locator: "'In full'"}, {source: S7, locator: "infobox (Arabic)"}], how_known: "Coder's Arabic script for the transliterated name; Wikipedia EN agrees (P50)."}
  aliases:
    - {name: "Abu Rayhan al-Biruni", kind: "roster alias"}
    - {name: "Alberuni", kind: transliteration}

basics:
  birth:
    date: {value: "973-09-04", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening ('born Sept. 4, 973 ce')"}, {source: S2, locator: "heading (362/973)"}, {source: S7, locator: "infobox (4 September 973)"}], how_known: "Britannica gives the day; Iranica the year 362/973; Wikipedia EN agrees on 4 September 973 (P50). The day rests on Britannica/Wikipedia, so 0.7."}
    place: {value: "Khwārezm (an outer suburb, bīrūn, of Kāṯ)", modern_name: "Khorezm region, Uzbekistan", polity_then: "Afrighid Khwārezm-Shāhs", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "'i. Life', paragraph 1"}, {source: S7, locator: "infobox (Kath, Khwarazm)"}], how_known: "Britannica (Khwārezm) and Iranica (suburb of Kāṯ, hence his nisba); Wikipedia EN agrees (P50)."}
  death:
    date: {value: "1052", approx: true, calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "opening ('died c. 1052')"}, {source: S7, locator: "infobox (9 December 1048) / lead (c. 1050)"}], how_known: "Britannica says c. 1052. Iranica: he wrote his pharmacology when 'over 80 (hence after 442/1050)', and Tashkent scholars give 11 December 1048, which Iranica reports with 'cf.' (S2). Wikipedia EN gives 9 December 1048 in the infobox and c. 1050 in the lead (P50). A real dispute (P30), so 0.5.", alternatives: [{value: "1048-12-11", note: "Tashkent scholars (Karimov), as reported by Iranica.", cites: [{source: S2, locator: "'i. Life', Ghaznavid paragraph"}]}, {value: "1048-12-09", note: "Wikipedia EN infobox.", cites: [{source: S7, locator: "infobox"}]}]}
    place: {value: "Ghazna", modern_name: "Ghazni, Afghanistan", polity_then: "Ghaznavid sultanate", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "infobox (Ghazni)"}], how_known: "Britannica; Wikipedia EN agrees (P50)."}
  first_lasting_contribution_year: {value: 1000, certainty: 0.5, cites: [{source: S2, locator: "'i. Life' (al-Āṯār al-bāqīa written at Qābūs's court 'probably in about 390/1000')"}], how_known: "The Chronology of Ancient Nations, his 'first major work', 'probably in about 390/1000, though he made later emendations' (Iranica); a hedged date, so 0.5 (P24)."}
  era_bucket: {value: "500 to 1399", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Every adult year (c. 990–1052) falls in '500 to 1399' (P2)."}
  region_of_birth: {value: "Central Asia", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Uzbekistan (P3)."}
  region_of_work: {value: "South Asia", certainty: 0.5, cites: [{source: S1, locator: "'Life'"}, {source: S2, locator: "'i. Life'"}], how_known: "Coder's call: Ghazna (Afghanistan, South Asia) from 1017 to the end of his life, where the Taḥdīd, India and Canon were finished; earlier Gurgān (Iran, MENA) and Khwārezm (Central Asia). Several regions, so 0.5."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Arabic", "Persian"], certainty: 0.7, cites: [{source: S1, locator: "'Works' (preference 'to be criticized in Arabic rather than be praised in Persian')"}], how_known: "Britannica; Iranica doubts the Persian Tafhīm is his own (S3), so Persian is uncertain."}
  occupations: {value: ["astronomer", "mathematician", "geographer", "historian", "court astrologer"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "'i. Life' ('famed as court astrologer')"}], how_known: "Britannica and Iranica."}

contribution:
  primary_domain: astronomy
  fields: {value: ["astronomy", "mathematics", "mathematical geography", "chronology", "ethnography of India", "mineralogy", "pharmacology"], certainty: 0.7, cites: [{source: S1, locator: "'Works'"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "The Chronology of Ancient Nations (al-Āṯār al-bāqiya)", year: 1000, kind: work, lasting: "with the India, 'the best premodern description of the cultures al-Bīrūnī came to know'; the most elaborate medieval treatment of the Jewish calendar (S1)", certainty: 0.5, cites: [{source: S1, locator: "'Works'"}, {source: S2, locator: "'i. Life'"}], how_known: "Britannica (lasting); Iranica (date, 'probably in about 390/1000')."}
    - {value: "Determination of the Coordinates of Places (Taḥdīd nihāyāt al-amākin)", year: 1025, kind: work, lasting: "'masterpiece in mathematical geography' (S1), with a spherical-trigonometric solution for the direction of Mecca", certainty: 0.5, cites: [{source: S1, locator: "'Works'"}], how_known: "Britannica (lasting, undated); the year 416/1025 is from a search summary of secondary literature, not read in a cited source, so 0.5 (coder's call)."}
    - {value: "India (Taḥqīq mā li-l-Hind)", year: 1030, kind: work, lasting: "'by far the most important of his encyclopaedic works' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Works'"}, {source: S2, locator: "'i. Life' ('completed in 421/1030 just after Maḥmūd's death')"}], how_known: "Britannica and Iranica."}
    - {value: "The Masʿudic Canon (al-Qānūn al-Masʿūdī)", year: 1030, kind: work, lasting: "new algebraic techniques for cubic equations; distinction between the motion of the solar apogee and precession (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Works'"}, {source: S2, locator: "'i. Life' ('421/1030')"}], how_known: "Britannica and Iranica; latest dated lasting item, so it ends the span (P30 addendum)."}
  evidence_of_impact:
    - {value: "'The most original polymath the Islamic world had ever known'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica (Saliba)."}
  major_works:
    - {value: "Elements of Astrology (al-Tafhīm)", year: UNKNOWN, kind: book, certainty: 0.7, cites: [{source: S1, locator: "'Works'"}, {source: S2, locator: "'i. Life' ('shortly before' the India)"}], how_known: "Britannica; Iranica dates it shortly before 1030."}
    - {value: "Gems (Kitāb al-jamāhir)", year: UNKNOWN, kind: book, certainty: 0.7, cites: [{source: S1, locator: "'Works'"}, {source: S2, locator: "'i. Life' (reign of Mawdūd, 1041–1048/9)"}], how_known: "Britannica; Iranica dates it to 1041–1049."}
    - {value: "Pharmacology (Kitāb al-ṣaydana)", year: UNKNOWN, kind: book, certainty: 0.7, cites: [{source: S1, locator: "'Works'"}, {source: S2, locator: "'i. Life' (after 442/1050)"}], how_known: "Britannica; Iranica dates it after 1050."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "'The most original polymath the Islamic world had ever known' (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "He says he did not know his own father or family origins (S1)."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Did not know his own father 'much less his family origins', by his own poem", role: father, certainty: 0.7, cites: [{source: S1, locator: "'Life', paragraph 2"}], how_known: "Britannica, reporting a poem preserved in a medieval biographical dictionary."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Educated by the Khwārezm-Shāh prince Abū Naṣr Manṣūr ibn ʿIrāq (mathematics)", stage: tutor, run_by: other, years: "to c. 995", certainty: 0.7, cites: [{source: S1, locator: "'Life', paragraph 1"}], how_known: "Britannica; years the coder's."}
    - {value: "In Khwārezm, both the 'Arab sciences' (fiqh, theology, grammar) and the 'non-Arab sciences' (mathematics, astronomy, medicine)", stage: other, run_by: other, years: "to c. 998", certainty: 0.7, cites: [{source: S2, locator: "'i. Life', paragraph 1"}], how_known: "Iranica."}
  early_mathematics: {value: UNKNOWN, how_known: "Level before 18 not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Abū Naṣr Manṣūr ibn ʿIrāq", certainty: 0.7, cites: [{source: S1, locator: "'Life', paragraph 1"}], how_known: "Britannica."}
  languages_in_childhood: {value: ["Khwarezmian"], certainty: 0.5, cites: [{source: S1, locator: "'Works'"}], how_known: "Coder's reading: he 'posed as an outsider to both Arabic and Persian' (S1)."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1000–1030", certainty: 0.5, cites: [{source: S2, locator: "'i. Life'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Muslim, with marked early sympathy for Shiʿism and later recognition of the first caliphs (Iranica: 'some uncertainty about Bīrūnī's own religious position within Islam')", certainty: 0.7, cites: [{source: S3, locator: "paragraph 2"}], how_known: "Iranica (de Blois). Membership, not a code."}
  self_described_science_religion_relation: {value: "The Koran's sentences on the shape of heaven and earth and 'other subjects necessary for man to know' are 'perfectly clear' and need no 'strained interpretation', unlike the Hindu treatments (India I, p. 263). He also rebukes those who attribute to God's wisdom what they do not know of physical sciences (Chronology pp. 252–253).", certainty: 0.7, cites: [{source: S4, locator: "vol. I, ch. XXXVI, p. 263"}, {source: S6, locator: "pp. 252–253"}], how_known: "His own published works in Sachau's translations."}
  primary_system:
    value: ISLAM
    basis: written_profession
    certainty: 0.7
    cites: [{source: S4, locator: "vol. I, ch. IX, p. 100; ch. XXXVI, pp. 263–264"}, {source: S6, locator: "p. 23 (Creator; Sura citations); p. 290 (Creator finished creation)"}, {source: S3, locator: "paragraphs 2–3"}]
    how_known: "His own published India in translation: 'We Muslims, of course, stand entirely on the other side of the question, considering all men as equal, except in piety' (p. 100); the Koran's sentences are 'in perfect harmony with the other religious codes' and 'perfectly clear', and sectarians read out passages 'of which not a single word was ever created (i.e. revealed) by God' (pp. 263–264). Chronology (c. 1000) independently speaks as a Muslim of the Creator and cites the Qurʾān (S6). Iranica: his approach to other religions 'must be viewed against the background of his own Muslim convictions' (S3)."
    rationale: "ISLAM use_when: the person's own writing shows Muslim belief (the Qur'an as revealed, the community of Muslims). CLASS_THEISM rejected: nothing read argues to God from the world in the falsafa manner, and his science is astronomy and geography, not metaphysics (S1: no interest in cosmology). Named alternative keeps 0.7 (Shi'i vs Sunni position uncertain within Islam; S3)."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: ISLAM, reason: "Coded at 0.7 (S4, pp. 100, 263–264; S6; S3)."}
    - {code: CLASS_THEISM, reason: "Rejected: no a posteriori argument to God read (P22)."}
  lio_axes:
    A_locus:
      value: 0
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S4, locator: "vol. I, ch. XXXVI, pp. 263–264"}, {source: S6, locator: "p. 23; pp. 252–253; p. 290"}]
      how_known: "Deepen D1: India (God reveals the Koran's words, pp. 263–264) plus Chronology own voice — anthropomorphic descriptions 'cannot be referred to the essence of the Creator, nor to his qualities, he being high above such things' (p. 23); 'all-wise and almighty Creator' who created the mountains (pp. 252–253); 'the Creator finished the creation of the world' (p. 290). Two independent published works (Chronology c. 1000; India 1030). Named alternative 1 keeps the ceiling at 0.7 (§3 contested readings)."
      rationale: "Draft judgment: God as a transcendent Creator who speaks in revelation and stands 'high above' anthropomorphic essence/qualities: the interventionist pole's locus (A 0). Named alternative: 1, since the Chronology transcendence line is brief and the India revelation lines do not themselves spell out a full doctrine of transcendence."
      alternatives:
        - {value: 1, note: "No extended doctrine of transcendence; Chronology 'high above' is brief.", cites: [{source: S6, locator: "p. 23"}, {source: S4, locator: "vol. I, pp. 263–264"}]}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S4, locator: "vol. I, p. 352"}, {source: S4, locator: "vol. I, ch. XVI, p. 179"}, {source: S6, locator: "p. 290; p. 295"}, {source: S1, locator: "'Works'"}]
      rationale: "Scored on his account of nature (P6). A scientist (P30: the Canon's apogee and precession results; the coordinates of places). Own words in India: rejects a Hindu theory because the Great Bear would then 'form an exception to the laws of nature' (p. 352); a very rare thing is 'something like a miracle, which is no longer in accordance with the ordinary laws of nature' (p. 179). Chronology corroborates: Jesus 'was in His earthly life subject to the laws of nature' (p. 290); nature 'preserves its genera and species', yet irregularities show 'the Creator who had designed something deviating from the general tenor of things' (p. 295). Lawfulness with divine/miracle departure: B 3. Named alternative 4 (no stated exceptionless order — Creator-designed deviations and miracle-as-departure block B 4; P35/P41 by analogy). Contested alternative keeps ceiling 0.7. Astrology does not cut the inference: he taught it while holding his own opinion of it 'as weak as that of its least adherents' (S1)."
      how_known: "Deepen D1: two independent published works in translation (India 1030; Chronology c. 1000), plus working science (P35). Raised from 0.5 because Chronology supplies a second own-voice 'laws of nature' / nature-order statement, not because working science alone was upgraded."
      alternatives:
        - {value: 4, note: "No stated exceptionless law; Chronology p. 295 allows Creator-designed deviations (P35).", cites: [{source: S4, locator: "vol. I, p. 352"}, {source: S6, locator: "p. 295"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read on reward and punishment; 'all men as equal, except in piety' (p. 100) is the moral community, which goes to C only as context (P7), and states no ledger."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "Reading 2: the Koran is clear and certain on what man needs to know (p. 263), while he defended the mathematical sciences against religious scholars who could not see their use (S1, Taḥdīd) and rebuked attributing physical ignorance to God's wisdom (S6, pp. 252–253). No statement of how the two rank when they conflict (P19, coder's call)."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Not scored from working science alone (P19). 'All fixed stars revolve at the same distance from the earth and in the same time' (p. 352) is Sachau's bracketed gloss on 'the laws of nature', and concerns the stars only (P7)."}
  mid_basin:
    value: true
    certainty: 0.7
    cites: [{source: S4, locator: "vol. I, pp. 263–264, 352, 179"}, {source: S6, locator: "pp. 23, 290, 295"}]
    how_known: "Deepen D1: A_locus 0 ≤ 1 and B_cause 3 ≥ 3, both now at certainty 0.7 (§6, P4, P19). Named alternatives (A 1; B 4) still meet the mid-basin branch, so the certainty used is that of the evidence for the condition (P30)."
  statements:
    - text: "We Muslims, of course, stand entirely on the other side of the question, considering all men as equal, except in piety; and this is the greatest obstacle which prevents any approach or understanding between Hindus and Muslims."
      cites: [{source: S4, locator: "vol. I, ch. IX, p. 100"}]
      date: "1030"
      context: "India, chapter on castes."
      axes: [C_ledger]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "Sachau's translation (1910), archive.org scan; OCR checked by eye."
    - text: "The sentences of the Koran on these and other subjects necessary for man to know are not such as to require a strained interpretation in order to become positive certainties in the minds of the hearers, and the same may be said regarding the holy codes revealed before the Koran."
      cites: [{source: S4, locator: "vol. I, ch. XXXVI, p. 263"}]
      date: "1030"
      context: "India, opening of the chapter on the shape of heaven and earth according to the Hindu astronomers."
      axes: [A_locus, D_authority]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "As above."
    - text: "we do not see why it should revolve so much more rapidly than the other fixed stars (for, in that case, the diameter of its course would be much larger than that of the others), nor why it should form an exception to the laws of nature (according to which all fixed stars revolve at the same distance from the earth and in the same time)"
      cites: [{source: S4, locator: "vol. I, p. 352"}]
      date: "1030"
      context: "India, against a theory of a 'year of the Great Bear'; he concludes its author was 'entirely devoid of scientific education'."
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "Parentheses are Sachau's explanatory insertions; OCR 'shonld' read as 'should'."
    - text: "If such strangeness reaches a high degree, the thing becomes a curiosity, or even something like a miracle, which is no longer in accordance with the ordinary laws of nature, and which seems chimerical as long as it has not been witnessed."
      cites: [{source: S4, locator: "vol. I, p. 179"}]
      date: "1030"
      context: "India, introducing 'strange manners and customs of the Hindus'."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "As above."
    - text: "the (anthropomorphic) descriptions, which are inherent in them, cannot be referred to the essence of the Creator, nor to his qualities, he being high above such things."
      cites: [{source: S6, locator: "p. 23"}]
      date: "1000"
      context: "Chronology, on Deuteronomy xxxiii. 2 and the founders of religions; within the span (c. 1000)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Sachau 1879 Chronology, archive.org PDF/OCR; page from running head 'ON THE NATURE OF THE ERAS. 23'."
    - text: "Jesus, though he had no human father, and though supported by the Holy Ghost, was in His earthly life subject to the laws of nature."
      cites: [{source: S6, locator: "p. 290"}]
      date: "1000"
      context: "Chronology, Syrian calendar, Annunciation (25 Adhar); within the span."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Sachau 1879; OCR 'eartbly' for 'earthly'."
    - text: "on the whole, one must say nature preserves its genera and species such as they are. ... Frequently, however, you find in the functions (actions) of nature which it is her office to fulfil, some fault (some irregularity), but this only serves to show that the Creator who had designed something deviating from the general tenor of things, is infinitely sublime beyond everything which we poor sinners may conceive and predicate of Him."
      cites: [{source: S6, locator: "p. 295"}]
      date: "1000"
      context: "Chronology, on the number of flower leaves conforming to geometry; within the span."
      axes: [B_cause, A_locus]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Sachau 1879; Creator-designed deviations keep B at 3 (not 4)."
  changes_over_life:
    - {value: "Shiʿite sympathies 'less apparent' in the works written after his removal to Ghazna (1017)", certainty: 0.7, cites: [{source: S3, locator: "paragraph 2"}], how_known: "Iranica (de Blois). Within Islam; no code change."}
  coder_notes: "Deepen D1 2026-10-24: (1) span still 1000–1030; (2) Chronology opens second own-voice work → A 0 and B 3 both 0.7, support corroborated; mid_basin true @0.7; (3) B stays 3 not 4 — Chronology p. 295 Creator-designed deviations + India miracle-as-departure; (4) Taḥdīd (Ali 1967) and Masʿudic Canon still unread; (5) Chart-moving YES (certainty and mid); figures/ not refreshed this pass."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Khwarezmian (Iranian)", certainty: 0.5, cites: [{source: S1, locator: "'Works'"}, {source: S2, locator: "'i. Life'"}, {source: S7, locator: "lead (Iranian Khwarazmian)"}], how_known: "Coder's reading: born in Khwārezm, an outsider to Arabic and Persian (S1); Wikipedia EN agrees Iranian Khwarazmian (P50)."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated; family unknown (S1)."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: "Studied fiqh and theology in Khwārezm in his first twenty-five years", certainty: 0.7, cites: [{source: S2, locator: "'i. Life', paragraph 1"}], how_known: "Iranica; not limited to childhood."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1000–1030", certainty: 0.5, cites: [{source: S2, locator: "'i. Life'"}], how_known: "The Chronology (c. 1000, 0.5) to the India and Canon (1030) (P29, P30)."}
  age_at_first_lasting_contribution: {value: 27, certainty: 0.5, cites: [{source: S2, locator: "'i. Life'"}], how_known: "1000 − 973 = 27 (P30); the first year is at 0.5."}
  first_evidence_of_lio_type_views: {value: "c. 1000 (Chronology), age ~27", certainty: 0.5, cites: [{source: S6, locator: "p. 290; p. 23"}], how_known: "Deepen D1: Chronology (span start) already has Creator transcendence and 'laws of nature'; India (1030) corroborates. First year hedged, so 0.5."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S6, locator: "p. 290"}, {source: S4, locator: "vol. I, p. 352"}], how_known: "Chronology at span start and India at span end both carry the scored views."}
  worldview_during_major_work: {value: "Muslim throughout; Shiʿite sympathy early, less apparent after 1017 (S3)", certainty: 0.7, cites: [{source: S3, locator: "paragraph 2"}], how_known: "Iranica."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Not assessed."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Not assessed."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S4, locator: "vol. I, p. 352"}], how_known: "Not assessed."}
  reading: "Not assessed."
  notes: ""

institutions:
  - {value: "Court of Qābūs ibn Voshmgīr, Gurgān", role: "scholar; dedicated the Chronology to Qābūs", years: "c. 998–c. 1004", kind: other, certainty: 0.7, cites: [{source: S1, locator: "'Life'"}, {source: S2, locator: "'i. Life'"}], how_known: "Britannica and Iranica; years from Iranica (388/998) and the coder."}
  - {value: "Ghaznavid court, Ghazna", role: "scholar and court astrologer", years: "1017–c. 1050", kind: other, certainty: 0.7, cites: [{source: S1, locator: "'Life'"}, {source: S3, locator: "paragraph 2 (removal to Ghazna, 408/1017)"}], how_known: "Britannica and Iranica."}
collaborators:
  - {value: "Ibn Sina", roster_id: ibn-sina, relation: correspondent, note: "philosophical correspondence 'that did not lack jealousies and slighting'", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  - {value: "Abū Naṣr Manṣūr ibn ʿIrāq", relation: teacher, note: "Khwārezm-Shāh prince; wrote mathematical works for him", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 140"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Death year: Britannica c. 1052; Iranica after 1050 (over 80 when writing the Pharmacology); Tashkent scholars 11 Dec 1048 (via Iranica); Wikipedia EN 9 Dec 1048 / c. 1050 (P50)."
    - "Britannica dates the Ghazna move to after 998 without a year; Iranica gives 408/1017."
    - "Iranica (de Blois) argues the Persian version of the Tafhīm is not his own work."
    - "Chronology and India read in Sachau English via archive.org PDF/OCR; Arabic not checked this pass."
  open_questions:
    - "Optional: Taḥdīd (Jamil Ali 1967) and Masʿudic Canon for further nature/God lines."
    - "Check India/Chronology quotes against Arabic editions."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "George Saliba; Britannica Editors"
    citation: "Saliba, George. \"al-Bīrūnī.\" Encyclopaedia Britannica (31 Aug 2026). https://www.britannica.com/biography/al-Biruni. Read live 2026-10-19; rechecked 2026-10-24."
    url: "https://www.britannica.com/biography/al-Biruni"
    accessed: 2026-10-24
    reliability_note: "Signed article by a historian of Arabic science; body cited, AI question boxes not cited (P26)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, institutions, collaborators]
    source_quality: "reference entry"
  - id: S2
    type: secondary
    kind: encyclopedia
    author: "C. Edmund Bosworth"
    citation: "Bosworth, C. Edmund. \"BĪRŪNĪ, ABŪ RAYḤĀN i. Life.\" Encyclopaedia Iranica IV/3 (1989; updated 2017). https://www.iranicaonline.org/articles/biruni-abu-rayhan-index/biruni-abu-rayhan-i-life/"
    url: "https://www.iranicaonline.org/articles/biruni-abu-rayhan-index/biruni-abu-rayhan-i-life/"
    accessed: 2026-10-24
    reliability_note: "Signed scholarly encyclopedia entry."
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions]
    source_quality: "reference entry"
  - id: S3
    type: secondary
    kind: encyclopedia
    author: "François de Blois"
    citation: "de Blois, François. \"BĪRŪNĪ, ABŪ RAYḤĀN vii. History of Religions.\" Encyclopaedia Iranica (2000; updated 2013). https://www.iranicaonline.org/articles/biruni-abu-rayhan-index/biruni-abu-rayhan-vii/"
    url: "https://www.iranicaonline.org/articles/biruni-abu-rayhan-index/biruni-abu-rayhan-vii/"
    accessed: 2026-10-24
    reliability_note: "Signed scholarly encyclopedia entry."
    used_for: [basics, worldview, timing, institutions]
    source_quality: "reference entry"
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "al-Bīrūnī, translated by Edward C. Sachau"
    citation: "Alberuni's India. Translated by Edward C. Sachau. 2 vols. London: Kegan Paul, Trench, Trübner, 1910 (vol. I). Archive.org scan and OCR text, https://archive.org/details/alberunisindia_201612"
    url: "https://archive.org/details/alberunisindia_201612"
    accessed: 2026-10-24
    reliability_note: "Scholarly translation of his published work, read as a library scan (OCR text); page numbers from the running heads."
    used_for: [worldview, timing, lane_b]
    source_quality: "archive scan (OCR only)"
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [identity, review]
    source_quality: "study roster"
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "al-Bīrūnī, translated by C. Edward Sachau"
    citation: "The Chronology of Ancient Nations (al-Āthār al-bāqiya). Translated by C. Edward Sachau. London: W. H. Allen, 1879. Archive.org PDF/OCR, https://archive.org/details/chronologyofanci00biru (download chronologyofanci00biru.pdf). Read 2026-10-24."
    url: "https://archive.org/details/chronologyofanci00biru"
    accessed: 2026-10-24
    reliability_note: "Scholarly translation of his first major published work; read as archive.org PDF with pdftotext OCR. Page numbers from printed running heads (pp. 23, 252–253, 290, 295)."
    used_for: [worldview, timing]
    source_quality: "archive scan (OCR only)"
  - id: S7
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "\"Al-Biruni.\" Wikipedia (English). https://en.wikipedia.org/wiki/Al-Biruni. Read 2026-10-24."
    url: "https://en.wikipedia.org/wiki/Al-Biruni"
    accessed: 2026-10-24
    reliability_note: "P50 dual-bio check against Britannica/Iranica; birth agrees; death date disputed. Not used for worldview codes."
    used_for: [identity, basics, heritage, review]
    source_quality: "reference entry"
---

# Al-Biruni

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Abū al-Rayḥān al-Bīrūnī (973–c. 1052), Muslim astronomer, mathematician, geographer and historian of India [S1]. Deepen D1: primary_system ISLAM (0.7); A 0 (0.7, alt 1, support corroborated); B 3 (0.7, alt 4, support corroborated); C UNKNOWN; D, E BELOW_THRESHOLD; mid_basin true (0.7). Chart-moving YES (faded→dark; hollow→filled). Plotted.

## Life and work

Khwārezm, Gurgān under Qābūs, then Ghazna from 1017 [S1; S2; S3].

## Contribution and impact

Chronology (c. 1000), coordinates of places, India and the Masʿudic Canon (1030) [S1; S2].

## Childhood and education

Did not know his father; taught by Abū Naṣr Manṣūr ibn ʿIrāq [S1; S2].

## Adult working worldview

Writes as a Muslim ("We Muslims") and treats the Koran as clear revelation [S4, I, pp. 100, 263–264]; Chronology: Creator "high above" anthropomorphic essence/qualities [S6, p. 23]. Rejects theories that would make an exception to "the laws of nature" [S4, I, p. 352]; Chronology: Jesus "subject to the laws of nature" [S6, p. 290]; nature's irregularities show Creator-designed deviations [S6, p. 295] — B 3 not 4.

## Heritage (context only)

Khwarezmian [S1; S2; S7].

## Timing

1000–1030, from age 27 [S2]. LIO views from Chronology at span start [S6].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Not assessed [S1].

## Open questions

- Taḥdīd (Ali 1967) and Masʿudic Canon (optional).
- Arabic check of India/Chronology quotes.

## Research log

- 2026-10-19: Read Britannica (Saliba), Iranica (Bosworth; de Blois) and Sachau's India, vol. I (archive.org OCR).
- 2026-10-24: Deepen D1. Opened Chronology Sachau 1879 (S6); Wikipedia EN P50 (S7). A/B 0.5→0.7; mid_basin true; Chart-moving YES. No figures/.
