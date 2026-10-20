---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
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
  native_name: {value: "أبو الريحان محمد بن أحمد البيروني", certainty: 0.5, cites: [{source: S1, locator: "'In full'"}], how_known: "Coder's Arabic script for the transliterated name."}
  aliases:
    - {name: "Abu Rayhan al-Biruni", kind: "roster alias"}
    - {name: "Alberuni", kind: transliteration}

basics:
  birth:
    date: {value: "973-09-04", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening ('born Sept. 4, 973 ce')"}, {source: S2, locator: "heading (362/973)"}], how_known: "Britannica gives the day; Iranica the year 362/973. The day rests on one source, so 0.7."}
    place: {value: "Khwārezm (an outer suburb, bīrūn, of Kāṯ)", modern_name: "Khorezm region, Uzbekistan", polity_then: "Afrighid Khwārezm-Shāhs", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "'i. Life', paragraph 1"}], how_known: "Britannica (Khwārezm) and Iranica (suburb of Kāṯ, hence his nisba)."}
  death:
    date: {value: "1052", approx: true, calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "opening ('died c. 1052')"}], how_known: "Britannica says c. 1052. Iranica: he wrote his pharmacology when 'over 80 (hence after 442/1050)', and Tashkent scholars give 11 December 1048, which Iranica reports with 'cf.' (S2). A real dispute (P30), so 0.5.", alternatives: [{value: "1048-12-11", note: "Tashkent scholars (Karimov), as reported by Iranica.", cites: [{source: S2, locator: "'i. Life', Ghaznavid paragraph"}]}]}
    place: {value: "Ghazna", modern_name: "Ghazni, Afghanistan", polity_then: "Ghaznavid sultanate", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1000, certainty: 0.5, cites: [{source: S2, locator: "'i. Life' (al-Āṯār al-bāqīa written at Qābūs's court 'probably in about 390/1000')"}], how_known: "The Chronology of Ancient Nations, his 'first major work', 'probably in about 390/1000, though he made later emendations' (Iranica); a hedged date, so 0.5 (P24)."}
  era_bucket: {value: "500 to 1399", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Every adult year (c. 990–1052) falls in '500 to 1399' (P2)."}
  region_of_birth: {value: "Central Asia", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Uzbekistan (P3)."}
  region_of_work: {value: "South Asia", certainty: 0.5, cites: [{source: S1, locator: "'Life'"}, {source: S2, locator: "'i. Life'"}], how_known: "Coder's call: Ghazna (Afghanistan, South Asia) from 1017 to the end of his life, where the Taḥdīd, India and Canon were finished; earlier Gurgān (Iran, MENA) and Khwārezm (Central Asia). Several regions, so 0.5."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Arabic", "Persian"], certainty: 0.7, cites: [{source: S1, locator: "'Works' (preference 'to be criticized in Arabic rather than be praised in Persian')"}], how_known: "Britannica; Iranica doubts the Persian Tafhīm is his own (S3), so Persian is uncertain."}
  occupations: {value: ["astronomer", "mathematician", "geographer", "historian", "court astrologer"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "'i. Life' ('famed as court astrologer')"}], how_known: "Britannica and Iranica."}

contribution:
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
  self_described_science_religion_relation: {value: "The Koran's sentences on the shape of heaven and earth and 'other subjects necessary for man to know' are 'perfectly clear' and need no 'strained interpretation', unlike the Hindu treatments (India I, p. 263).", certainty: 0.7, cites: [{source: S4, locator: "vol. I, ch. XXXVI, p. 263"}], how_known: "His own published work in Sachau's translation."}
  primary_system:
    value: ISLAM
    basis: written_profession
    certainty: 0.7
    cites: [{source: S4, locator: "vol. I, ch. IX, p. 100; ch. XXXVI, pp. 263–264"}, {source: S3, locator: "paragraphs 2–3"}]
    how_known: "His own published India in translation: 'We Muslims, of course, stand entirely on the other side of the question, considering all men as equal, except in piety' (p. 100); the Koran's sentences are 'in perfect harmony with the other religious codes' and 'perfectly clear', and sectarians read out passages 'of which not a single word was ever created (i.e. revealed) by God' (pp. 263–264). Iranica: his approach to other religions 'must be viewed against the background of his own Muslim convictions' (S3)."
    rationale: "ISLAM use_when: the person's own writing shows Muslim belief (the Qurʾān as revealed, the community of Muslims). CLASS_THEISM rejected: nothing read argues to God from the world in the falsafa manner, and his science is astronomy and geography, not metaphysics (S1: no interest in cosmology). One work read, in translation, so 0.7."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: ISLAM, reason: "Coded at 0.7 (S4, pp. 100, 263–264; S3)."}
    - {code: CLASS_THEISM, reason: "Rejected: no a posteriori argument to God read (P22)."}
  lio_axes:
    A_locus:
      value: 0
      basis: written_profession
      certainty: 0.5
      cites: [{source: S4, locator: "vol. I, ch. XXXVI, pp. 263–264"}]
      how_known: "His own text, but only indirectly on locus: God reveals the Koran's words (pp. 263–264), and the Hindu notion of creation is set against creation as 'a formation of something out of nothing' (vol. I, p. 322, by contrast; coder's reading). A code does not set the axes (§6), so 0.5, as for al-Khwarizmi."
      rationale: "Draft judgment: God as a transcendent person who speaks in revelation: the interventionist pole's locus. Named alternative: 1, since he states no doctrine of transcendence in his own words read."
      alternatives:
        - {value: 1, note: "No explicit doctrine of transcendence read.", cites: [{source: S4, locator: "vol. I, pp. 263–264"}]}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.5
      cites: [{source: S4, locator: "vol. I, p. 353"}, {source: S4, locator: "vol. I, ch. XVI, p. 179"}, {source: S1, locator: "'Works'"}]
      rationale: "Scored on his account of nature (P6). A scientist (P30: the Canon's apogee and precession results; the coordinates of places). In his own words he rejects a Hindu theory because the Great Bear would then 'form an exception to the laws of nature' (p. 353), and he treats a very rare thing as 'something like a miracle, which is no longer in accordance with the ordinary laws of nature' (p. 179): a general lawfulness with miracles as the departure from the ordinary, but no stated exceptionless order. So B 3 at 0.5, alternative 4 (P35, P41 by analogy). His astrology does not cut the inference as it did for al-Khwarizmi: he taught it while holding his own opinion of it 'as weak as that of its least adherents' (S1)."
      how_known: "His own published work in translation, plus working science (P35)."
      alternatives:
        - {value: 4, note: "No stated exceptionless law (P35).", cites: [{source: S4, locator: "vol. I, p. 353"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read on reward and punishment; 'all men as equal, except in piety' (p. 100) is the moral community, which goes to C only as context (P7), and states no ledger."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "Reading 2: the Koran is clear and certain on what man needs to know (p. 263), while he defended the mathematical sciences against religious scholars who could not see their use (S1, Taḥdīd). No statement of how the two rank when they conflict (P19, coder's call)."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Not scored from working science alone (P19). 'All fixed stars revolve at the same distance from the earth and in the same time' (p. 353) is Sachau's bracketed gloss on 'the laws of nature', and concerns the stars only (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 0 and B 3 are both only at 0.5, under the test's 0.7 bar (§6, P19)."}
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
      cites: [{source: S4, locator: "vol. I, p. 353"}]
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
  changes_over_life:
    - {value: "Shiʿite sympathies 'less apparent' in the works written after his removal to Ghazna (1017)", certainty: 0.7, cites: [{source: S3, locator: "paragraph 2"}], how_known: "Iranica (de Blois). Within Islam; no code change."}
  coder_notes: "Coder's calls: (1) span 1000–1030 (Chronology, 'probably' c. 1000, to the India and Canon, 1030); Gems (1041–49) and Pharmacology (after 1050) are listed as major works, not lasting; ending the span at 1050 would not change any score; (2) B 3 rests on his own two 'laws of nature' sentences plus working science, at 0.5 with alternative 4; astrology does not cut it because he discounted it himself (S1); (3) the Taḥdīd year 1025 rests on a search summary, not on a cited source; (4) no ruling question: A and B at 0.5 cannot make mid_basin true without a firmer source."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Khwarezmian (Iranian)", certainty: 0.5, cites: [{source: S1, locator: "'Works'"}, {source: S2, locator: "'i. Life'"}], how_known: "Coder's reading: born in Khwārezm, an outsider to Arabic and Persian (S1)."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated; family unknown (S1)."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: "Studied fiqh and theology in Khwārezm in his first twenty-five years", certainty: 0.7, cites: [{source: S2, locator: "'i. Life', paragraph 1"}], how_known: "Iranica; not limited to childhood."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1000–1030", certainty: 0.5, cites: [{source: S2, locator: "'i. Life'"}], how_known: "The Chronology (c. 1000, 0.5) to the India and Canon (1030) (P29, P30)."}
  age_at_first_lasting_contribution: {value: 27, certainty: 0.5, cites: [{source: S2, locator: "'i. Life'"}], how_known: "1000 − 973 = 27 (P30); the first year is at 0.5."}
  first_evidence_of_lio_type_views: {value: "1030 (India), age 57", certainty: 0.5, cites: [{source: S4, locator: "vol. I, p. 353"}], how_known: "B 3 from his own words; earlier works not read (§8)."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.5, cites: [{source: S4, locator: "vol. I, p. 353"}], how_known: "The India (1030) is at the end of the span; earlier works not read."}
  worldview_during_major_work: {value: "Muslim throughout; Shiʿite sympathy early, less apparent after 1017 (S3)", certainty: 0.7, cites: [{source: S3, locator: "paragraph 2"}], how_known: "Iranica."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Not assessed."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Not assessed."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S4, locator: "vol. I, p. 353"}], how_known: "Not assessed."}
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
    - "Death year: Britannica c. 1052; Iranica after 1050 (over 80 when writing the Pharmacology); Tashkent scholars 1048 (via Iranica)."
    - "Britannica dates the Ghazna move to after 998 without a year; Iranica gives 408/1017."
    - "Iranica (de Blois) argues the Persian version of the Tafhīm is not his own work."
  open_questions:
    - "Read the Chronology (Sachau 1879) and the Taḥdīd (Ali 1967) for earlier statements on God and nature; check the India quotes against a second translation or the Arabic."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "George Saliba; Britannica Editors"
    citation: "Saliba, George. \"al-Bīrūnī.\" Encyclopaedia Britannica (31 Aug 2026). https://www.britannica.com/biography/al-Biruni. Read live 2026-10-19."
    url: "https://www.britannica.com/biography/al-Biruni"
    accessed: 2026-10-19
    reliability_note: "Signed article by a historian of Arabic science; body cited, AI question boxes not cited (P26)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, institutions, collaborators]
  - id: S2
    type: secondary
    kind: encyclopedia
    author: "C. Edmund Bosworth"
    citation: "Bosworth, C. Edmund. \"BĪRŪNĪ, ABŪ RAYḤĀN i. Life.\" Encyclopaedia Iranica IV/3 (1989; updated 2017). https://www.iranicaonline.org/articles/biruni-abu-rayhan-index/biruni-abu-rayhan-i-life/"
    url: "https://www.iranicaonline.org/articles/biruni-abu-rayhan-index/biruni-abu-rayhan-i-life/"
    accessed: 2026-10-19
    reliability_note: "Signed scholarly encyclopedia entry."
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions]
  - id: S3
    type: secondary
    kind: encyclopedia
    author: "François de Blois"
    citation: "de Blois, François. \"BĪRŪNĪ, ABŪ RAYḤĀN vii. History of Religions.\" Encyclopaedia Iranica (2000; updated 2013). https://www.iranicaonline.org/articles/biruni-abu-rayhan-index/biruni-abu-rayhan-vii/"
    url: "https://www.iranicaonline.org/articles/biruni-abu-rayhan-index/biruni-abu-rayhan-vii/"
    accessed: 2026-10-19
    reliability_note: "Signed scholarly encyclopedia entry."
    used_for: [basics, worldview, timing, institutions]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "al-Bīrūnī, translated by Edward C. Sachau"
    citation: "Alberuni's India. Translated by Edward C. Sachau. 2 vols. London: Kegan Paul, Trench, Trübner, 1910 (vol. I). Archive.org scan and OCR text, https://archive.org/details/alberunisindia_201612"
    url: "https://archive.org/details/alberunisindia_201612"
    accessed: 2026-10-19
    reliability_note: "Scholarly translation of his published work, read as a library scan (OCR text); page numbers from the running heads."
    used_for: [worldview, timing, lane_b]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Al-Biruni

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Abū al-Rayḥān al-Bīrūnī (973–c. 1052), Muslim astronomer, mathematician, geographer and historian of India [S1]. Draft: primary_system ISLAM (0.7); A 0 (0.5, alt 1); B 3 (0.5, alt 4); C UNKNOWN; D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Plotted (faded) at the next chart refresh.

## Life and work

Khwārezm, Gurgān under Qābūs, then Ghazna from 1017 [S1; S2; S3].

## Contribution and impact

Chronology (c. 1000), coordinates of places, India and the Masʿudic Canon (1030) [S1; S2].

## Childhood and education

Did not know his father; taught by Abū Naṣr Manṣūr ibn ʿIrāq [S1; S2].

## Adult working worldview

Writes as a Muslim ("We Muslims") and treats the Koran as clear revelation [S4, I, pp. 100, 263–264]; rejects a theory that would make an exception to "the laws of nature" [S4, I, p. 353].

## Heritage (context only)

Khwarezmian [S1; S2].

## Timing

1000–1030, from age 27 [S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Not assessed [S1].

## Open questions

- The Chronology and the Taḥdīd for earlier statements.

## Research log

- 2026-10-19: Read Britannica (Saliba), Iranica (Bosworth; de Blois) and Sachau's India, vol. I (archive.org OCR).
