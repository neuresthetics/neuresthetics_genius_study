---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA9)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to medieval. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #204/228, F 3, rank 217): score A if a clear reading ≥0.5; leave mixed as BELOW; do not force plot. Re-read Schimmel Britannica (S1); Nicholson Mathnawí Books I–II translation + Book V.590–591 via masnavi.net Nicholson English (S5); Arberry Discourses / Fihi as Marman modernization (S6); Mojaddedi Iranica Teachings (S7); Chittick 'Rumi and wahdat al-wujud' (S8); Wikipedia EN dual bio (S9). primary ISLAM scholarly_reconstruction 0.5 → written_profession 0.7 (Book I Arabic prose preface: roots of Mohammedan Religion; expounder of the Qur'an; blessing on Mohammed; Amen O Lord of all created beings). A UNKNOWN→BELOW_THRESHOLD: A 0–1 pole (Lord of created beings; First and the Last; world = prison / finite vs infinite other) against fana / 'except God… all the rest is gone' and Fihi 'I am not, God is all' (A 2–3+ lead); Schimmel S1: ideas contradict / cannot systematize; Chittick: never uses wahdat al-wujud; Nicholson Ibn Arabi parallels scant; not PANT (no Deus sive Natura; world is prison). B UNKNOWN→BELOW_THRESHOLD: Masnavi I.88 moral-cosmic correspondence under poetry/P42 caution; not a scientist (P30). Mid BELOW. Dual bio P50 (Britannica Balkh vs Wikipedia Wakhsh). P47 source_quality on all. Not plotted. Fallacy audit none; figures not refreshed."}
    - {date: 2026-10-20, by: "Grok Bot", summary: "AA10 audit fix: Mas̄navī c.1262 at 0.5 (Mojaddedi: 'started probably around 1262'), earliest possible 1258; S4 labelled unofficial web copy."}
    - {date: 2026-10-20, by: "Grok Bot", summary: "AA9 audit fix: Mas̄navī dated c.1258 at 0.5 by the start of its composition range (Iranica S3; Mojaddedi S4), alternative 1262."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA9, order P32: F 3, rank 217). Source: Britannica scholars edition, signed by Annemarie Schimmel (read in full). Lasting: his lyric poetry (Dīvān-e Shams), begun after Shams disappeared in 1247 ('This experience of love, longing, and loss turned Rūmī into a poet'), and the Mas̄navī, which 'widely influenced mystical thought and literature throughout the Muslim world' (S1); 'By the end of the 20th century, his popularity had become a global phenomenon' (S1). Composition range (RQ-Z9-N1): lyrics from 1247; the Mas̄navī begun c.1262 at 0.5 (S4; Book I finished about 660/1262, S3), earliest possible 1258 (Ṣalāḥ al-Dīn's death), and worked on until his death in 1273; span 1247–1273 at 0.5, age 40. Worldview: ISLAM at 0.5 (scholarly_reconstruction: 'the greatest Sufi mystic'; S1); no own words quoted, so A UNKNOWN (P19); not a scientist; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: rumi
  display_name: "Rumi"
  roster:
    canonical_name: "Rumi"
    rank: 217
    F: 3
    models: [Gemini, GPT, Grok]
    band: "core (3–4)"
    status: "core"
    field: "poetry"
    field_bucket: "literature"
  full_name: {value: "Jalāl al-Dīn Rūmī", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  native_name: {value: "جلال‌الدین محمّد رومی", certainty: 0.7, cites: [{source: S9, locator: "lead / infobox native_name"}], how_known: "Wikipedia EN Persian script (also مولانا جلال‌الدین محمد رومی)."}
  aliases:
    - {name: "Mawlānā", kind: "title or honorific"}
    - {name: "Jalal al-Din al-Rumi", kind: "transliteration"}
    - {name: "Jalāl al-Dīn Muḥammad Balkhī", kind: "other"}

basics:
  birth:
    date: {value: "1207-09-30", certainty: 0.5, cites: [{source: S1, locator: "Introduction"}, {source: S9, locator: "infobox"}], how_known: "Britannica: 'born c. September 30, 1207'; Wikipedia agrees 30 September 1207."}
    place: {value: "Balkh (traditional) / Wakhsh (modern scholarship)", modern_name: "Balkh, Afghanistan or Wakhsh, Tajikistan", polity_then: "Khwarazmian Empire (Wikipedia)", certainty: 0.5, cites: [{source: S1, locator: "Introduction"}, {source: S9, locator: "infobox / birth_place"}], how_known: "P50 dual bio: Britannica 'Balkh [now in Afghanistan]'; Wikipedia EN 'Wakhsh, Khwarazmian Empire (present-day Tajikistan)'. Nicholson Book I prose preface self-identifies 'of (the city of) Balkh' (S5) — family/nisba, not decisive for birth town. 0.5 while place is disputed."}
  death:
    date: {value: "1273-12-17", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "Konya", modern_name: "Konya, Turkey", polity_then: "Seljuq sultanate of Rūm", certainty: 0.7, cites: [{source: S1, locator: "Introduction; Early life"}], how_known: "Britannica: Konya, capital under the Seljuqs."}
  first_lasting_contribution_year: {value: 1247, certainty: 0.5, cites: [{source: S1, locator: "The influence of Shams al-Dīn"}], how_known: "Shams disappeared 'one night in 1247'; 'This experience ... turned Rūmī into a poet' (S1): start of the lyric composition range (RQ-Z9-N1); inferred, 0.5."}
  era_bucket: {value: "500 to 1399", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}], how_known: "1247, and every year of his life, falls in 500 to 1399 (P2)."}
  region_of_birth: {value: "South Asia", certainty: 0.5, cites: [{source: S1, locator: "Introduction"}, {source: S9, locator: "infobox"}], how_known: "P50: Balkh (Afghanistan) or Wakhsh (Tajikistan). Kept South Asia at 0.5 (al-Biruni Afghanistan precedent); Central Asia is a live alternative if Wakhsh is preferred."}
  region_of_work: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "Early life; Death and legacy"}], how_known: "Konya, Anatolia (Heraclitus precedent: modern Turkey is MENA); home-region alternative South Asia."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Persian", "Arabic"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica: Persian and Arabic, 'some Turkish and less Greek'."}
  occupations: {value: ["poet", "mystic", "teacher"], certainty: 0.7, cites: [{source: S1, locator: "Introduction; Early life"}], how_known: "Britannica: succeeded his father at a madrasah in 1231."}

contribution:
  era_bucket: medieval
  fields: {value: ["poetry", "Sufism"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Lyric poetry: the Dīvān-e Shams (ghazals, about 30,000 verses) and robāʿīyāt", year: 1247, kind: "body of work", lasting: "'famous for his lyrics'; 'By the end of the 20th century, his popularity had become a global phenomenon, with his poetry achieving a wide circulation in western Europe and the United States' (S1)", certainty: 0.5, cites: [{source: S1, locator: "Introduction; The influence of Shams al-Dīn"}], how_known: "Begun after Shams's disappearance in 1247 (S1); composition range start (RQ-Z9-N1); inferred."}
    - {value: "Mas̄navī-yi Maʿnavī ('Spiritual Couplets', nearly 26,000 couplets)", year: 1262, kind: "work", lasting: "'which widely influenced mystical thought and literature throughout the Muslim world' (S1)", certainty: 0.5, cites: [{source: S1, locator: "Introduction; The influence of Shams al-Dīn; Death and legacy"}, {source: S3, locator: "para. 3"}, {source: S4, locator: "Introduction"}], how_known: "Dated by the start of its composition range (RQ-Z9-N1): 'The process of producing the Masnavi was started probably around 1262' (S4, Introduction p. xx; chronology 'c.1262 The Masnavi is started'), consistent with Book I 'completed, in around 660/1262' (S3, citing Lewis pp. 221–3); c.1262 at 0.5. Earliest possible year 1258: begun under Ḥusām al-Dīn after Ṣalāḥ al-Dīn's death in 1258 (S1, S4). Worked on until shortly before his death in 1273 (S1)."}
  evidence_of_impact:
    - {value: "Mawlawiyyah order (Whirling Dervishes) organized by his disciples", kind: "institutional or technological lineage", certainty: 0.7, cites: [{source: S1, locator: "Death and legacy"}], how_known: "Britannica."}
    - {value: "Claimed by both Turkish and Persian literature; substantial influence in the Indian subcontinent", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  major_works:
    - {value: "Fīhi mā fīhi (talks)", year: UNKNOWN, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "Death and legacy"}], how_known: "Britannica; undated."}
    - {value: "Maktūbāt (letters)", year: UNKNOWN, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "Death and legacy"}], how_known: "Britannica; undated."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Greatest Sufi poet in Persian (S1).", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Father Bahāʾ al-Dīn Walad, a noted mystical theologian, author and teacher", role: "family", certainty: 0.7, cites: [{source: S1, locator: "Early life and travels"}], how_known: "Britannica."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Trained by his father and by Burhān al-Dīn Muḥaqqiq (from 1232) in mystical theory", certainty: 0.7, cites: [{source: S1, locator: "Early life and travels"}], how_known: "Britannica."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1247–1273", certainty: 0.5, cites: [{source: S1, locator: "The influence of Shams al-Dīn; Death and legacy"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not a scientist; no science–religion relation scored."}
  primary_system:
    value: ISLAM
    basis: written_profession
    certainty: 0.7
    cites: [{source: S5, locator: "Book I Arabic prose preface (Nicholson tr.)"}, {source: S1, locator: "Introduction; Death and legacy"}, {source: S7, locator: "Teachings"}]
    how_known: "Deepen D1: own-voice Book I prose preface (S5) — 'roots of the roots of the roots of the (Mohammedan) Religion'; 'expounder of the Qur'an'; self as 'Muhammad son of Muhammad son of al-Husayn of (the city of) Balkh'; closes 'Amen, O Lord of all created beings!' and 'God bless the best of His creatures, Mohammed, and his kin'. Schimmel (S1) frames him as the greatest Sufi mystic/poet; Sufism coded under ISLAM (al-Ghazali precedent). Contested-reading ceiling 0.7 held (love-mysticism / subversion of dry dogma in Mojaddedi S7) — still within ISLAM, not a rival system code."
    rationale: "ISLAM use_when: Muslim belief in his own writing (Qur'an-centered Mathnawi self-description; blessing on Mohammed). PANT rejected (candidate_codes). CLASS_THEISM not needed as a primary when ISLAM fits."
  secondary_system: {value: UNKNOWN, how_known: "None required; Sufi practice stays under ISLAM."}
  candidate_codes_considered:
    - {code: ISLAM, reason: "Coded; raised to written_profession 0.7 on Book I preface (S5)."}
    - {code: PANT, reason: "Lead only, rejected: no Deus sive Natura circle; Masnavi I.525 world is prison / finite vs infinite other (S5); Chittick (S8) — never employs wahdat al-wujud; Nicholson Ibn Arabi influence claims scant; pantheism label applies at most as general Sufi tawhid language, not a pantheist system. Standing rule: Sufi/fana unity needs clear own-voice warrant for PANT; keep A BELOW instead."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Deepen D1: mixed own-voice poles, neither ≥0.5 (Gandhi/Plotinus pattern; deepen standing rule; P42 poetry caution). A 0–1 lead: Book I preface 'Lord of all created beings' + blessing on Mohammed (S5); Masnavi V.591 'Verily, He is the First and the Last' (S5 via masnavi.net Nicholson English); I.525–526 'This world, indeed, is the prison of your souls' / 'This world is finite, and truly that (other) is infinite' (S5) — Creator/Lord distinct from the world. A 2–3+ / fana lead: Masnavi V.590 'There remains except God: all the rest is gone' (S5); Fihi mā fīhi (Arberry via Marman modernization, S6) on 'I am God' as 'I am not, God is all. There is no existence but God' (humility / annihilation, not ontological identity of world with God). Schimmel (S1): 'It is impossible to systematize his ideas, which at times contradict each other'. Chittick (S8) blocks reading him as Ibn Arabi pantheist. Do not invent certainty; do not force plot.", note: "Fihi quote is from an unofficial modernization of Arberry (P21 unofficial-web cap). The mix itself, corroborated by Schimmel, blocks the score — not edition status alone."}
    B_cause: {value: BELOW_THRESHOLD, how_known: "Deepen D1: not a scientist (P30). Masnavi I.88 (S5) links withholding poor-tax to absent rain-clouds and fornication to plague — moral-cosmic correspondence / intervening special causation in poetic homily. Miracle and discipline narratives elsewhere (I.85–92 area) do not yield a clear single account of nature's lawfulness vs special cases at ≥0.5 under P42 poetry/character caution. Evidence present but too weak/mixed (P19 BELOW, not UNKNOWN)."}
    C_ledger: {value: UNKNOWN, how_known: "Not scored this pass."}
    D_authority: {value: UNKNOWN, how_known: "Not scored this pass."}
    E_scope: {value: UNKNOWN, how_known: "Not scored this pass."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied (Pavlov pattern / P19)."}
  statements:
    - text: "This is the Book of the Mathnawi, which is the roots of the roots of the roots of the (Mohammedan) Religion in respect of (its) unveiling the mysteries of attainment (to the Truth) and of certainty… the expounder of the Qur'an… Saith the feeble slave who hath need of the mercy of God most High, Muhammad son of Muhammad son of al-Husayn of (the city of) Balkh… Amen, O Lord of all created beings! … Glory be to God, the Lord of all created beings, and God bless the best of His creatures, Mohammed, and his kin, the noble, the pure!"
      cites: [{source: S5, locator: "Book I Arabic prose preface (Nicholson tr., opening)"}]
      date: "1262"
      context: "Masnavi Book I prose preface; composition start of Book I ~1262 (S3/S4). Own-voice profession of Islamic framing."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Primary check: archive.org Nicholson Vol. II djvu OCR (RUMITheMathnawiVol1Vol2)."
    - text: "This world, indeed, is the prison of your souls: oh, go in yonder direction, for there lies your open country. This world is finite, and truly that (other) is infinite: image and form are a barrier to that Reality."
      cites: [{source: S5, locator: "Book I, vv. 525–526 (Nicholson)"}]
      date: "1262"
      context: "Masnavi I.525–526; world distinct from / lesser than the infinite Reality."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Primary check: Nicholson Book I OCR."
    - text: "There remains except God: all the rest is gone. Hail, O mighty Love, destroyer of polytheism! Verily, He is the First and the Last: do not regard polytheism as arising from aught except the eye that sees double."
      cites: [{source: S5, locator: "Book V, vv. 590–591 (Nicholson English via masnavi.net)"}]
      date: "1270"
      context: "Masnavi V.590–591; fana / tawhid couplet beside First-and-Last personal God language — the A mix in one breath. Date mid-to-late Masnavi composition (worked until 1273); 1270 at 0.5 placeholder year within span."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Nicholson English as hosted on masnavi.net (not the archive Books I–II OCR)."
    - text: "Take the famous utterance, 'I am God.' Some people think this is a great pretension, but 'I am God' is in fact a great humility. Those who say, instead, 'I am a servant of God' believe that two exist, themselves and God. But those who say, 'I am God' have become nothing and have cast themselves to the winds. They say, 'I am God' meaning, 'I am not, God is all. There is no existence but God. I have lost all separation. I am nothing.' In this the humility is greater."
      cites: [{source: S6, locator: "Discourses / Fihi mā fīhi (Arberry 1961 via Marman modernization; ~pp. 83–84)"}]
      date: "1260"
      context: "Prose discourses; explains Bayazid-style 'I am God' as annihilation/humility, not a claim that the speaker is the Creator. P42: own teaching voice in discourse form; edition is unofficial modernization of Arberry. Date approximate within working years."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Marman modernization of Arberry; P21 unofficial-web cap."
    - text: "On account of withholding the poor-tax no rain-clouds arise, and in consequence of fornication the plague spreads in all directions."
      cites: [{source: S5, locator: "Book I, v. 88 (Nicholson)"}]
      date: "1262"
      context: "Masnavi I.88; moral-cosmic correspondence in poetic homily — B evidence too thin alone."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Primary check: Nicholson Book I OCR."

  changes_over_life: []
  coder_notes: "Deepen D1: poetry/character voice (P42) and Schimmel's contradict-warning keep A below threshold. Do not code PANT from fana slogans. Lane A stays public-record only; Lane B unused for beliefs-as-findings."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Persian", certainty: 0.5, cites: [{source: S9, locator: "Life / Overview"}], how_known: "Wikipedia: born to Persian parents; 0.5 (one tertiary)."}
  religious_heritage_by_birth: {value: "Muslim", certainty: 0.5, cites: [{source: S1, locator: "Early life and travels"}], how_known: "Father a mystical theologian teaching at a madrasah (S1); inferred."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1247–1273", certainty: 0.5, cites: [{source: S1, locator: "The influence of Shams al-Dīn; Death and legacy"}], how_known: "Lyric poetry from 1247 to the end of work on the Mas̄navī at his death in 1273 (begun c.1262; earliest possible 1258) (P29, P30, RQ-Z9-N1); both ends inferred."}
  age_at_first_lasting_contribution: {value: 40, certainty: 0.5, cites: [{source: S1, locator: "Introduction; The influence of Shams al-Dīn"}], how_known: "1247 − 1207 = 40 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: "1262", certainty: 0.5, cites: [{source: S5, locator: "Book I Arabic prose preface"}], how_known: "Book I preface (own-voice Islamic framing + Lord of created beings) at Masnavi start ~1262; earlier lyric A not scored this pass."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.5, cites: [{source: S5, locator: "Book I preface; I.525–526; V.590–591"}], how_known: "Within the Masnavi composition span (major work)."}
  worldview_during_major_work: {value: "ISLAM (Sufi); A BELOW_THRESHOLD; B BELOW_THRESHOLD", certainty: 0.5, cites: [{source: S5, locator: "Book I preface"}], how_known: "Equals deepen D1 coding."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Mystical poetry (S1); no geometric form claimed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed for a circle claim; PANT already rejected on textual grounds.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "Lane B unused: A/B mid stay BELOW; no H1 timing claim."
  notes: ""

institutions:
  - {value: "Madrasah in Konya", role: "teacher (succeeded his father)", years: "1231–UNKNOWN", kind: "religious body", certainty: 0.7, cites: [{source: S1, locator: "Early life and travels"}], how_known: "Britannica."}
collaborators:
  - {value: "Shams al-Dīn of Tabrīz", relation: "influenced by", note: "wandering dervish, met 30 November 1244", certainty: 0.7, cites: [{source: S1, locator: "The influence of Shams al-Dīn"}], how_known: "Britannica."}
  - {value: "Ḥusām al-Dīn Chelebi", relation: "collaborator", note: "deputy; wrote down the Mas̄navī", certainty: 0.7, cites: [{source: S1, locator: "The influence of Shams al-Dīn"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 217"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Composition range inferred (1247–1273)."
    - "Birth place disputed (Balkh vs Wakhsh); P50 dual bio."
    - "A_locus mixed under poetry/P42; Schimmel contradict-warning."
    - "Fihi quote via unofficial modernization of Arberry (S6)."
  open_questions:
    - "Mas̄navī start: c.1262 (earliest possible 1258)."
    - "Optional: score C/D/E from further Masnavi/Fihi if a later pass needs them."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Annemarie Schimmel"
    citation: "Schimmel, Annemarie, and the Editors of Encyclopaedia Britannica. 'Rūmī.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/R%C5%ABm%C4%AB/43269"
    url: "https://kids.britannica.com/scholars/article/R%C5%ABm%C4%AB/43269"
    accessed: 2026-10-24
    reliability_note: "Signed article, scholars edition, re-read on deepen."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, timing, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [review]
  - id: S3
    type: tertiary
    kind: "encyclopedia"
    author: "Mohammad Estelami"
    citation: "Estelami, Mohammad. 'Ḥosām-al-Din Čalabi.' Encyclopaedia Iranica (2004, updated 2017). https://www.iranicaonline.org/articles/hosam-al-din-calabi/"
    url: "https://www.iranicaonline.org/articles/hosam-al-din-calabi/"
    accessed: 2026-10-19
    reliability_note: "Signed entry, read in full."
    source_quality: "reference entry"
    used_for: [contribution]
  - id: S4
    type: secondary
    kind: "book chapter"
    author: "Jawid Mojaddedi"
    citation: "Mojaddedi, Jawid (tr.). Rumi, The Masnavi, Book One. Oxford World's Classics (Oxford University Press, 2004), Introduction."
    url: "https://archive.org/details/92ab-848bb-546f-0680916811d-74c-136"
    accessed: 2026-10-19
    reliability_note: "Unofficial web copy (archive.org PDF of the in-copyright OUP edition); translator's introduction read."
    source_quality: "unofficial web copy"
    used_for: [contribution]
  - id: S5
    type: primary
    kind: "scholarly edition"
    author: "Jalāl al-Dīn Rūmī (tr. Reynold A. Nicholson)"
    citation: "Nicholson, Reynold A. (ed./tr.). The Mathnawí of Jalálu'ddín Rúmí, Vol. II containing the translation of the First & Second Books (Gibb Memorial / Cambridge UP). Book I Arabic prose preface; I.88; I.525–526. Book V.590–591 Nicholson English as hosted at masnavi.net. Archive OCR: https://archive.org/details/RUMITheMathnawiVol1Vol2"
    url: "https://archive.org/details/RUMITheMathnawiVol1Vol2"
    accessed: 2026-10-24
    reliability_note: "Standard scholarly English translation (public-domain Gibb Memorial). Books I–II from archive.org djvu OCR; V.590–591 from masnavi.net Nicholson English hosting. Own-voice via translation."
    source_quality: "primary / own words"
    used_for: [worldview, basics, timing]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Jalāl al-Dīn Rūmī (tr. A. J. Arberry; modernized Marman)"
    citation: "Arberry, A. J. (tr.). Discourses of Rumi (Fihi ma Fihi) (1961), as modernized in the Omphaloskepsis/Marman archive text. 'I am God' humility passage (~pp. 83–84)."
    url: "https://archive.org/details/sufism_tasawwuf_outlook_Dis"
    accessed: 2026-10-24
    reliability_note: "Unofficial web modernization of Arberry (P21 unofficial-web cap). Used only for the well-known Fihi 'I am God' humility teaching; A mix already established from Nicholson Masnavi alone."
    source_quality: "unofficial web copy"
    used_for: [worldview]
  - id: S7
    type: tertiary
    kind: "encyclopedia"
    author: "Jawid Mojaddedi"
    citation: "Mojaddedi, Jawid. 'Rumi, Jalāl-al-Din viii. Teachings.' Encyclopaedia Iranica. https://www.iranicaonline.org/articles/rumi-jalal-al-din-teachings"
    url: "https://www.iranicaonline.org/articles/rumi-jalal-al-din-teachings"
    accessed: 2026-10-24
    reliability_note: "Signed Iranica teachings entry; used for contested-reading ceiling note on love-mysticism vs orthodoxy."
    source_quality: "reference entry"
    used_for: [worldview]
  - id: S8
    type: secondary
    kind: "book chapter"
    author: "William C. Chittick"
    citation: "Chittick, William C. 'Rumi and wahdat al-wujud.' In Poetry and Mysticism in Islam: The Heritage of Rumi, ed. Amin Banani et al. (Cambridge, 1994). Archive OCR: https://archive.org/stream/... (djvu.txt consulted)."
    url: "https://archive.org/details/poetrymysticismi0000unse"
    accessed: 2026-10-24
    reliability_note: "Scholarly monograph chapter; OCR. Key: Rumi never employs wahdat al-wujud; Nicholson Ibn Arabi parallels scant; only general Sufi tawhid sense applies."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview]
  - id: S9
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "Wikipedia. 'Rumi.' https://en.wikipedia.org/wiki/Rumi"
    url: "https://en.wikipedia.org/wiki/Rumi"
    accessed: 2026-10-24
    reliability_note: "Used for P50 dual bio (Wakhsh birth) and Persian native_name; not for worldview coding."
    source_quality: "reference entry"
    used_for: [identity, basics, heritage]
---

## Summary

Rumi (1207–1273), Sufi mystic and Persian poet [S1]. Deepen D1: ISLAM 0.7 (written_profession, Book I preface); A BELOW_THRESHOLD (mixed Creator/Lord vs fana poles; Schimmel contradict-warning); B BELOW_THRESHOLD; mid BELOW. Not plotted.

## Life and work

Birth place disputed: Balkh (Britannica; nisba in preface) vs Wakhsh, Tajikistan (Wikipedia) [S1, S5, S9]. Worked and died in Konya [S1].

## Contribution and impact

Dīvān-e Shams from 1247; Mas̄navī from c.1262 [S1, S3, S4].

## Childhood and education

Father Bahāʾ al-Dīn Walad; Burhān al-Dīn [S1].

## Adult working worldview

ISLAM (Sufi) by own Book I prose preface [S5]. A mixed under poetry (P42): Lord of created beings / First and Last / world-as-prison against 'except God… all the rest is gone' and Fihi fana humility [S5, S6]; Schimmel: ideas contradict [S1]; Chittick: not wahdat al-wujud / Ibn Arabi school [S8]. PANT rejected. B not scorable from poetic moral-cosmic verses. Mid BELOW.

## Heritage (context only)

Muslim (inferred); Persian parents (Wikipedia, 0.5).

## Timing

1247–1273, age 40 [S1]. LIO-type evidence during Masnavi (~1262+).

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No geometric-form / H1 claim.

## Open questions

- Mas̄navī start: c.1262 (earliest possible 1258).
- Optional later C/D/E.

## Research log

- 2026-10-24: Deepen D1 — Nicholson Mathnawí I–II (archive OCR) + V.590–591 (masnavi.net Nicholson English); Fihi via Arberry/Marman; Schimmel; Mojaddedi Iranica Teachings; Chittick wahdat al-wujud; Wikipedia dual bio. A/B mid → BELOW; ISLAM → 0.7 written_profession. Person file only local commit; drafts/deepen_rumi.md untracked; no figures/; no fallacy_catalog.
- 2026-10-20: AA9 audit fix: Mas̄navī dated c.1258 at 0.5 by the start of its composition range (Iranica S3; Mojaddedi S4), alternative 1262.
- 2026-10-20: AA10 audit fix: Mas̄navī c.1262 at 0.5 (Mojaddedi: 'started probably around 1262'), earliest possible 1258; S4 labelled unofficial web copy.
- 2026-10-19: Read Britannica (Schimmel, scholars edition).
