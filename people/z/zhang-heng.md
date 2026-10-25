---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 single run AB-Z)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-21
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #215/228, F 3, rank 230). Opened Needham SCC vol. 3 (1959) DjVuTXT OCR (IA cftri.9621…): Ling Hsien pp.216–217 (自然相生 / tzu-jan hsiang séng EN; Taoist-influence footnote; cosmogony omitted; hun sphere / wu chi); p.414 moonlight and lunar/solar eclipse EN ('about +120'); Hun I Chu egg cosmology p.217. Re-read MacTutor; Wikisource Lingxian Chinese; Hou Han shu placement already on file. Wikipedia EN + New World Encyclopedia dual bio (P50): death Luoyang. Lifted A 3 from written_profession @0.5 (coder gloss of unofficial Chinese) to written_profession @0.7 corroborated (Needham EN of spontaneity/mutual production + Chinese Wikisource; alt 4 kept). B 3: basis inference_from_work → written_profession; certainty stays 0.5 with alt 4 (P16 Hilbert / P35; Archimedes pattern); support corroborated (Needham eclipse EN + Chinese). mid_basin BELOW_THRESHOLD → false @0.7 (A≥3 branch, P10). primary_system stays BELOW_THRESHOLD (TAO/CONFUC/CHNFOLK mix). P42: Lingxian survives as Qing-assembled fragments (Ma Kuo-Han YHSF); Hou Han shu + Needham attribute to Zhang Heng — own words with reliability flag, not doxography. P47 source_quality; P49 not used for A/B (published translation, not reconstruction). Chart-moving: hollow→filled (both axes corroborated); faded stays (min=B@0.5); mid newly false. Do not force plot. No fallacy_catalog; no figures/. Draft, not reviewed."}
    - {date: 2026-10-21, by: "Grok Bot", summary: "ABZ audit fixes (blind audit /workspace/genius_study_audit/gs_eece863_ABZ/run1/: 25 HOLD, 3 WEAKEN, 0 FAIL). #13: moonlight/eclipse theory was adopted from Jing Fang and Wang Chong (S2 para 8); lasting contribution and P30 scientist case now rest on his distance-speed theory of the seven luminaries ('innovative', S2). #14: locator para 8. #25: Hou Han shu ch. 59 (S5, read) places the Lingxian after his appointment as Grand Astrologer; span alternative 115–120 at 0.5 (RQ-Z9-N1), age about 37–42; main span 132 kept. RQ-ABZ-1 (v8's call on the auditor's advice): portent lines are omen-reading, B 3 at 0.5 alt 4, note only. Own gloss carries A at 0.5 (v8's call on the auditor's advice); 聖人無心，因茲以生心 added as support for alt A 4. No score change."}
    - {date: 2026-10-21, by: "Grok Bot", summary: "Record created (single run at Jason's request, order P32: last uncoded F 3, rank 230). Basics from MacTutor (O'Connor and Robertson, 2003) and chinaknowledge.de (Theobald, 2025, signed). Own words from the Lingxian (Chinese text, Wikisource web copy of the fragments), coder's English gloss. Lasting: seismoscope (132, a device, P33) and the Lingxian's theory of moonlight and lunar eclipses (undated in the sources read), so span 132 only (dated item), age 54. Scientist (P30) on the Lingxian eclipse theory. A 3 at 0.5, alt 4 (Dao as root, things 'arise of themselves', with Heaven's 'mind' shown in portents). B 3 at 0.5, alt 4 (P35), with a B 2 lead from the portent passage (RQ-ABZ-1). primary_system BELOW_THRESHOLD (TAO / CONFUC / CHNFOLK leads). Plots, faded. Draft, not reviewed."}

identity:
  id: zhang-heng
  display_name: "Zhang Heng"
  roster:
    canonical_name: "Zhang Heng"
    rank: 230
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: "core"
    field: "invention"
    field_bucket: "invention / engineering"
  full_name: {value: "Zhang Heng", certainty: 1.0, cites: [{source: S1, locator: "Quick Info"}, {source: S2, locator: "opening paragraph"}], how_known: "Both sources."}
  native_name: {value: "張衡", certainty: 0.7, cites: [{source: S2, locator: "opening paragraph"}], how_known: "Theobald."}
  aliases:
    - {name: "Pingzi 平子 (courtesy name)", kind: "other"}
    - {name: "Chang Heng / Chang Hêng (Wade-Giles)", kind: "other"}

basics:
  birth:
    date: {value: "0078", calendar: julian, certainty: 1.0, cites: [{source: S1, locator: "Quick Info"}, {source: S2, locator: "opening paragraph"}], how_known: "Both give 78; year only."}
    place: {value: "Nanyang (E county, Nanyang commandery)", modern_name: "Nanyang, Henan, China", polity_then: "Eastern Han", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}, {source: S2, locator: "opening paragraph"}], how_known: "MacTutor 'Nan-yang'; Theobald 'from E 鄂 in the commandery of Nanyang'. Agree on the commandery; county from S2 only."}
  death:
    date: {value: "0139", calendar: julian, certainty: 1.0, cites: [{source: S1, locator: "Quick Info"}, {source: S2, locator: "opening paragraph"}], how_known: "Both give 139."}
    place: {value: "Luoyang", modern_name: "Luoyang, Henan, China", polity_then: "Eastern Han", certainty: 1.0, cites: [{source: S7, locator: "infobox Died"}, {source: S8, locator: "infobox Died; Retirement and death"}], how_known: "Wikipedia EN and New World Encyclopedia both give Luoyang (P50 dual bio). MacTutor (S1) said only 'China'."}
  first_lasting_contribution_year: {value: 132, certainty: 0.5, cites: [{source: S1, locator: "Biography, seismograph paragraph"}, {source: S5, locator: "張衡傳"}], how_known: "Seismoscope 'In 132' (S1), the only lasting item with a year (P30 #1). Alternative 115 under RQ-Z9-N1: S5 places the Lingxian in his Grand Astrologer tenure; Needham dates the Ling Hsien eclipse passage 'about +120' (S6 p.414).", alternatives: [{value: 115, note: "Start of the c. 115–120 range for the Lingxian (RQ-Z9-N1); Needham 'about +120' (S6).", cites: [{source: S5, locator: "張衡傳"}, {source: S6, locator: "p. 414 ('Ling Hsien about + 120')"}]}]}
  era_bucket: {value: "-500 to 499", certainty: 1.0, cites: [{source: S1, locator: "Quick Info"}], how_known: "132 (P2); his whole life (78–139) is in this bucket."}
  region_of_birth: {value: "East Asia", certainty: 1.0, cites: [{source: S1, locator: "Quick Info"}, {source: S2, locator: "opening paragraph"}], how_known: "China (P3)."}
  region_of_work: {value: "East Asia", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Imperial court at Luoyang."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "As recorded."}
  languages_of_work: {value: ["Classical Chinese"], certainty: 0.7, cites: [{source: S3, locator: "full text"}], how_known: "Text of the Lingxian."}
  occupations: {value: ["astronomer", "court official (Grand Astrologer)", "poet", "inventor", "mathematician"], certainty: 1.0, cites: [{source: S1, locator: "Summary; Biography"}, {source: S2, locator: "opening paragraph"}], how_known: "Both sources."}

contribution:
  fields: {value: ["astronomy", "invention", "literature", "mathematics"], certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  lasting_original_contributions:
    - {value: "Seismoscope (Hou Feng Di Dong Yi)", year: 132, kind: "invention", lasting: "'In 132 Zhang invented the first seismograph for measuring earthquakes' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Biography, seismograph paragraph"}], how_known: "Device (P33): does not by itself make him a scientist. Mechanism reconstructions (Needham and later) are P49 context only — not used for A/B."}
    - {value: "Lingxian: theory linking the speeds of the Sun, Moon and five planets to their distance from heaven (近天則遟，遠天則速)", year: UNKNOWN, kind: "theory", lasting: "'Zhang Heng introduced an innovative theory linking the speeds of the Sun, Moon, and five visible planets to their distances'; 'His insights into the varying speeds of celestial bodies were groundbreaking' (S2)", certainty: 0.7, cites: [{source: S2, locator: "paragraphs 3 and 8"}, {source: S3, locator: "近天則遟，遠天則速"}], how_known: "Year not given in S1–S3; S5 places the Lingxian after his appointment as Grand Astrologer; Needham dates a Ling Hsien passage 'about +120' (S6 p.414). The moonlight and eclipse explanations in the same text are views he 'adopted' from Jing Fang and Wang Chong (S2 para 8), so not listed as original lasting contribution (ABZ audit #13) — they still count as his own published account of nature for B (S6 EN)."}
  evidence_of_impact:
    - {value: "Seismoscope reported a distant earthquake (138) confirmed days later", kind: "other", certainty: 0.7, cites: [{source: S1, locator: "Biography, seismograph paragraph"}], how_known: "MacTutor."}
  major_works:
    - {value: "Lingxian 靈憲 (Spiritual Constitution of the Universe)", year: UNKNOWN, kind: "book", certainty: 0.7, cites: [{source: S2, locator: "opening paragraph"}, {source: S6, locator: "pp. 216–217, 414"}], how_known: "Survives in fragments; Needham and Theobald."}
    - {value: "Huntian yi zhu (Commentary on the Armillary Sphere)", year: UNKNOWN, kind: "book", certainty: 0.7, cites: [{source: S2, locator: "opening paragraph"}, {source: S6, locator: "p. 217 (Hun I Chu)"}], how_known: "Theobald; Needham quotes egg cosmology."}
    - {value: "Liangjing fu (rhapsodies on the two capitals)", year: UNKNOWN, kind: "other", certainty: 0.7, cites: [{source: S2, locator: "opening paragraph"}], how_known: "Theobald."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founding figure in Chinese astronomy and instrument making (S1, S2).", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Born into an important family", role: "family", certainty: 0.7, cites: [{source: S1, locator: "Biography, paragraph 2"}], how_known: "MacTutor."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated beyond 'important family'."}
  schooling:
    - {value: "Educated in Confucian moral and political philosophy; ten years studying literature", certainty: 0.7, cites: [{source: S1, locator: "Biography, paragraph 2"}], how_known: "MacTutor."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "132", certainty: 0.5, cites: [{source: S1, locator: "Biography, seismograph paragraph"}], how_known: "Equals timing.major_work_period (alternative 115–120). The Lingxian is adult work and counts for the span at its normal certainty (P31)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No explicit statement read."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "The Lingxian frames cosmogony through the Dao ('道之根', '道之幹', '道之實') and quotes the Daodejing ('有物渾成，先天地生') (S3); Needham notes 'Taoist influence' at the spontaneity passage (S6 p.217 n.f). S2 reads its 'spirit' as 'corresponding to the Daoist concept of Dao'. S1 says his 'strong moral beliefs' were 'based in Confucianism', and his office read portents (S1). NWE lists 'Daoism, Chinese folk religion' as religious stance (S8) — tertiary, not own-voice. Han correlative cosmology mixes TAO, CONFUC and CHNFOLK; no single code reaches 0.5."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: TAO, reason: "Dao cosmogony and Daodejing quotation in the Lingxian (S3; S2); Needham Taoist-influence note (S6)."}
    - {code: CONFUC, reason: "Confucian education and moral beliefs (S1)."}
    - {code: CHNFOLK, reason: "Portent reading: Heaven's 'mind' shown in the luminaries (S3); NWE folk-religion label (S8)."}
  lio_axes:
    A_locus:
      value: 3
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S6, locator: "pp. 216–217 (tzu-jan hsiang séng; Taoist-influence n.f)"}, {source: S3, locator: "情性萬殊…自然相生; 太素之前…道之根…自無生有; 天心於是見矣"}]
      how_known: "Needham SCC vol. 3 (1959) publishes English of the Ling Hsien spontaneity passage: things 'follow a natural principle of spontaneity, mutually producing each other (tzu-jan hsiang séng)' with a 'Taoist influence' footnote (S6 pp.216–217) — the published translation that RQ-ABZ-1 said A needed for 0.7. Chinese Wikisource (S3) corroborates 自然相生 and supplies the Dao-root cosmogony Needham omitted ('[cosmogonic passage, here omitted]') plus 天心. Contested alt 4 → certainty at most 0.7. P42: fragments Qing-assembled (YHSF); attributed to Zhang Heng by Hou Han shu (S5) and Needham — treated as own words with reliability flag."
      rationale: "Immanent pole features (Needham EN + Chinese): the cosmos follows spontaneity / mutual production (自然相生); no creator person outside the world in the translated cosmography. Chinese fills Dao as root ('道之根…自無生有') omitted by Needham. Limited personal feature (Chinese): 'the mind of Heaven is seen' (天心於是見矣) in the luminaries' portents. So 3. Alternative 4 if 天心 is read impersonally, supported by the preface: '聖人無心，因茲以生心' (coder's gloss: 'the sage has no mind [of his own]; from this he forms his mind'), where mind is taken from the cosmic pattern."
      alternatives:
        - {value: 4, note: "天心 read as an impersonal order, not a mind; preface 聖人無心，因茲以生心; Needham spontaneity reading leans process/identity.", cites: [{source: S3, locator: "天心於是見矣; preface 聖人無心，因茲以生心"}, {source: S6, locator: "pp. 216–217 (tzu-jan hsiang séng)"}]}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S6, locator: "p. 414 (sun/moon fire-water; lunar eclipse an-hsü; solar eclipse)"}, {source: S3, locator: "故月光生於日之所照…; 近天則遟，遠天則速"}, {source: S2, locator: "paragraphs 3 and 8"}]
      how_known: "Scientist (P30): lasting contribution is the Lingxian distance-speed theory (S2, S3). Deepen: Needham publishes EN of his moonlight and eclipse account as natural obstruction/reflection (S6 p.414), so basis lifts from inference_from_work to written_profession. Certainty stays 0.5 with named alt 4 — lawful regularities in his own words with no stated no-exception claim (P16 Hilbert addendum; P35; Archimedes pattern). Corroborated: Needham EN + Chinese Wikisource (+ Theobald on distance-speed)."
      rationale: "Scored on his account of nature (P6). Needham: 'The sun is like fire and the moon like water… the moon's brightness is produced from the radiance of the sun… obstruction of the earth itself—this is called an-hsü, a lunar eclipse… when the moon passes across (the sun's path) then there is a solar eclipse.' Distance-speed (近天則遟，遠天則速) states regular motion by distance. No stated exceptionless / miracle-denial claim → B 3 at 0.5, alternative 4 (P35). Note (RQ-ABZ-1): portent lines (歷示吉凶…用告禍福; stars 其見無期，其行無度) are omen-reading from regular motion and signs from irregular objects — correlative signification, not a stated agent-suspension of law; no score change."
      alternatives:
        - {value: 4, note: "P35 / P16 Hilbert alternative: written lawful regularities without a no-exception claim cannot tell lawful-with-exceptions from exceptionless.", cites: [{source: S6, locator: "p. 414"}, {source: S3, locator: "近天則遟，遠天則速"}]}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Hou Han shu memorial against chenwei unread in full this pass; working science does not bear on D (P19)."}
    E_scope: {value: BELOW_THRESHOLD, note: "Scientist; Needham translates 'what is beyond (the celestial sphere) no one knows… no end and no bounds' (S6 p.217) — cosmographic limit, not a statement that the same laws hold everywhere (P19).", how_known: "BELOW_THRESHOLD under P19: not scored from working science alone."}
  mid_basin: {value: false, certainty: 0.7, cites: [{source: S6, locator: "pp. 216–217"}, {source: S3, locator: "自然相生; 道之根"}], how_known: "A_locus 3 at 0.7 with named alt 4; both ≥ 3, so P30 uses the certainty of the A≥3 condition, not the exact-value contest. A≥3 branch reads A only (P10). Deepen D1 lifted A past the prior 0.5 BELOW_THRESHOLD."}
  statements:
    - text: "They follow a natural principle of spontaneity, mutually producing each other (tzu-jan hsiang séng)."
      cites: [{source: S6, locator: "pp. 216–217"}, {source: S3, locator: "情性萬殊，旁通感薄，自然相生，莫之能紀"}]
      context: "Ling Hsien cosmography (Needham EN). Footnote: 'Taoist influence here'. Chinese parallel: 自然相生."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
    - text: "聖人無心，因茲以生心，故靈憲作興。"
      cites: [{source: S3, locator: "preface"}]
      context: "Lingxian preface. Coder's gloss: 'The sage has no mind [of his own]; from this he forms his mind, and so the Lingxian was made.' Support for alt A 4. Needham translates the preceding sage-kings / hun-sphere setup but not this line."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
    - text: "斯謂溟涬，蓋乃道之根也。道根旣建，自無生有。"
      cites: [{source: S3, locator: "second paragraph, opening"}]
      context: "Lingxian cosmogony. Coder's gloss: 'This is called the Dark Sediment; it is the root of the Dao. The root of the Dao once established, being arose from non-being.' Needham omits this cosmogonic passage (S6 p.216: '[There follows a cosmogonic passage, here omitted.]')."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
    - text: "日月運行，歷示吉凶，五緯躔次，用告禍福，則天心於是見矣。"
      cites: [{source: S3, locator: "second paragraph, star passage"}]
      context: "Coder's gloss: 'The movements of Sun and Moon show good and ill fortune; the stations of the five planets announce calamity and blessing; thus the mind of Heaven is seen.' Keeps A at 3 vs 4; RQ-ABZ-1: omen-reading, not B exception."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
    - text: "The sun is like fire and the moon like water. The fire gives out light and the water reflects it. Thus the moon's brightness is produced from the radiance of the sun, and the moon's darkness is due to (the light of) the sun being obstructed. … The light pouring forth from the sun does not always reach the moon owing to the obstruction of the earth itself—this is called 'an-hsü', a lunar eclipse. … when the moon passes across (the sun's path) then there is a solar eclipse."
      cites: [{source: S6, locator: "p. 414"}, {source: S3, locator: "夫日譬猶火，月譬猶水…故月光生於日之所照，魄生於日之所蔽…是謂闇虛…月過則食"}]
      context: "Ling Hsien about +120 (Needham). Natural reflection/obstruction account of moonlight and eclipses — B written profession. S2 notes adoption from Jing Fang / Wang Chong for originality of lasting contribution; still his published wording for B."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
    - text: "近天則遟，遠天則速"
      cites: [{source: S3, locator: "seven luminaries passage"}, {source: S2, locator: "paragraphs 3 and 8"}]
      context: "Distance-speed theory of the seven luminaries — P30 scientist case and lasting original contribution (S2). Coder's gloss: 'near heaven then slow, far from heaven then fast'."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
  changes_over_life: []
  coder_notes: "Deepen 2026-10-24: Needham SCC3 supplies the published EN that lifts A to 0.7 and B's basis to written_profession; B certainty stays 0.5 (P35/Hilbert). Cosmogony Dao-root and 天心 remain Chinese-only (Needham omitted cosmogony). primary_system still BELOW (mix). Death place filled Luoyang (Wiki+NWE). Hou Han shu chenwei memorial still unread for D. Seismoscope reconstructions = P49 context only."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not applicable / not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period:
    value: "132"
    certainty: 0.5
    cites: [{source: S1, locator: "Biography, seismograph paragraph"}, {source: S5, locator: "張衡傳: 再遷為太史令 ... 著靈憲"}, {source: S6, locator: "p. 414 ('about + 120')"}]
    how_known: "The seismoscope (132) is the only lasting item with a year (P29, P30). S5 places the Lingxian after his appointment as Grand Astrologer but gives no year; Needham dates a Ling Hsien passage about +120. 0.5 because the alternative is real (P25)."
    alternatives:
      - {value: "115–120", note: "RQ-Z9-N1: Lingxian during Grand Astrologer tenure (S5); court appointment 'In around 116' (S1); Needham 'about +120' (S6). Age about 37–42.", cites: [{source: S5, locator: "張衡傳"}, {source: S1, locator: "Biography, paragraph 2"}, {source: S6, locator: "p. 414"}]}
  age_at_first_lasting_contribution: {value: 54, certainty: 0.5, cites: [{source: S1, locator: "Quick Info; seismograph paragraph"}], how_known: "132 − 78 = 54 (P30 year difference); about 37–42 under the 115–120 span alternative."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "Lingxian year still not exact; S5 tenure + Needham about +120."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "Same text as one lasting item; no exact year."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "primary_system BELOW_THRESHOLD."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Needham translates gnomon / two right-angled triangles for cosmic dimensions (S6 p.217); Chinese 重差鉤股 (S3). Computational, not assessed as geometric-form proofs.", certainty: 0.5, cites: [{source: S6, locator: "p. 217"}, {source: S3, locator: "八極之維 ... 皆移千里而差一寸得之"}], how_known: "Coder's reading of Needham + Chinese."}
  form_acquired: {value: UNKNOWN, how_known: "Not stated."}
  circle_present: {value: "unclear", rationale: "Hun I Chu: heavens 'like a hen's egg and as round as a crossbow bullet; the earth is like the yolk' (S6 p.217; S1). Not assessed further.", certainty: 0.5, cites: [{source: S6, locator: "p. 217"}, {source: S1, locator: "armillary sphere paragraph"}], how_known: "Needham EN of Hun I Chu."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Eastern Han imperial court, Luoyang", role: "official; Grand Astrologer (taishi ling)", years: "c. 116–", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "Biography, paragraph 2"}, {source: S2, locator: "opening paragraph"}], how_known: "MacTutor 'In around 116'; end year not stated."}
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 230"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Lingxian survives as Qing-assembled fragments (Ma Kuo-Han YHSF); Needham translates from that tradition (P42 reliability flag). Attribution to Zhang Heng is standard (Hou Han shu; Needham; Theobald)."
    - "Needham omits the Dao cosmogony passage; A 3 personal-feature (天心) and Dao-root lines still rest on Chinese Wikisource + coder gloss."
    - "Span 132 at 0.5; alternative 115–120 (RQ-Z9-N1) with Needham about +120."
    - "Roster field 'invention'; scientist status rests on the Lingxian distance-speed theory, not the seismoscope (P33)."
  open_questions:
    - "Authoritative critical Chinese edition of the Lingxian fragments (beyond Wikisource) for the Dao-root and 天心 lines Needham omitted."
    - "Full Hou Han shu memorial against chenwei for D_authority."
    - "A scholarly year for the Lingxian that settles the span (Needham about +120 is approximate)."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "J. J. O'Connor and E. F. Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Zhang Heng.\" MacTutor History of Mathematics Archive, University of St Andrews (last update December 2003). https://mathshistory.st-andrews.ac.uk/Biographies/Zhang_Heng/"
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Zhang_Heng/"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Signed biographical archive, re-read on deepen."
    used_for: [identity, basics, contribution, childhood, worldview, timing, lane_b, institutions]
  - id: S2
    type: tertiary
    kind: "encyclopedia"
    author: "Ulrich Theobald"
    citation: "Theobald, Ulrich. \"Lingxian 靈憲.\" ChinaKnowledge.de, 24 March 2025. http://www.chinaknowledge.de/Literature/Science/lingxian.html"
    url: "http://www.chinaknowledge.de/Literature/Science/lingxian.html"
    accessed: 2026-10-21
    source_quality: "reference entry"
    reliability_note: "Signed reference page by a sinologist, with a bibliography; read in full on create. Re-fetch timed out on deepen; citations retained from prior full read."
    used_for: [identity, basics, contribution, worldview, institutions]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Zhang Heng"
    citation: "Zhang Heng 張衡. Lingxian 靈憲 (fragments). Chinese text, Wikisource. https://zh.wikisource.org/wiki/靈憲"
    url: "https://zh.wikisource.org/wiki/靈憲"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Unofficial web copy of Qing-assembled fragments (P42 flag); edition not stated on the page. Corroborates Needham EN for overlapping passages; Dao cosmogony and 天心 not in Needham EN."
    used_for: [basics, contribution, worldview, lane_b]
  - id: S5
    type: primary
    kind: "other"
    author: "Fan Ye"
    citation: "Fan Ye 范曄. Hou Han shu 後漢書, juan 59, 張衡列傳 (biography of Zhang Heng). Chinese text, Wikisource. https://zh.wikisource.org/wiki/後漢書/卷59"
    url: "https://zh.wikisource.org/wiki/後漢書/卷59"
    accessed: 2026-10-21
    source_quality: "unofficial web copy"
    reliability_note: "Standard history (5th c.); unofficial web copy; read the passage on his appointment and the Lingxian."
    used_for: [timing]
  - id: S4
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-21
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [review]
  - id: S6
    type: secondary
    kind: "scholarly book"
    author: "Joseph Needham"
    citation: "Needham, Joseph. Science and Civilisation in China, Vol. 3: Mathematics and the Sciences of the Heavens and the Earth. Cambridge: Cambridge University Press, 1959. Ling Hsien / Chang Hêng translations at pp. 216–217 (cosmology; tzu-jan hsiang séng), 217 (Hun I Chu egg), 414 (moonlight and eclipses, 'about +120'). OCR: Internet Archive cftri.9621sciencecivilisat0000jose_djvu.txt."
    url: "https://archive.org/details/cftri.9621sciencecivilisat0000jose"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Needham's own English translations (tr. auct.) from YHSF / CSHK fragment collections. Cosmogonic passage explicitly omitted at p.216. Used for A and B written_profession lifts."
    used_for: [contribution, worldview, timing, lane_b]
  - id: S7
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Zhang Heng.\" https://en.wikipedia.org/wiki/Zhang_Heng"
    url: "https://en.wikipedia.org/wiki/Zhang_Heng"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "P50 dual bio with S8: death place Luoyang; Grand Astrologer 115–120 / 126–132. Not used for A/B scores."
    used_for: [basics]
  - id: S8
    type: tertiary
    kind: "encyclopedia"
    author: "New World Encyclopedia contributors"
    citation: "New World Encyclopedia. \"Zhang Heng.\" https://www.newworldencyclopedia.org/entry/Zhang_Heng"
    url: "https://www.newworldencyclopedia.org/entry/Zhang_Heng"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "P50 dual bio with S7: death Luoyang; lists religious stance 'Daoism, Chinese folk religion' (tertiary — does not lift primary_system)."
    used_for: [basics, worldview]
---

## Summary

Zhang Heng (78–139), Eastern Han astronomer, inventor and poet [S1, S2]. A 3 @0.7 and B 3 @0.5, both corroborated. mid_basin false. Plots, faded filled.

## Life and work

Nanyang; court official at Luoyang from about 116, several times Grand Astrologer; died Luoyang 139 [S1, S2, S7, S8].

## Contribution and impact

Seismoscope of 132 [S1]; the Lingxian's distance-speed theory of the seven luminaries [S2, S3]; moonlight and eclipse explanations in Needham's EN of the same text [S6] (adopted from Jing Fang and Wang Chong per S2 for originality of lasting contribution).

## Childhood and education

Confucian education and ten years of literary study [S1].

## Adult working worldview

Needham: things follow spontaneity and mutually produce each other (Taoist influence noted); moonlight and eclipses as natural reflection and obstruction [S6]. Chinese: Dao as root, Heaven's mind in portents [S3]. No single system code reaches 0.5.

## Heritage (context only)

Not stated.

## Timing

Span 132 (seismoscope), age 54 [S1], at 0.5. Alternative 115–120, age about 37–42: Lingxian after he became Grand Astrologer [S5]; Needham about +120 [S6].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Geometric form and circle unclear (computational gnomon / egg cosmology).

## Open questions

- Critical Chinese edition for Dao-root / 天心 lines Needham omitted; Hou Han shu chenwei memorial for D; exact Lingxian year.

## Research log

- 2026-10-21: Read MacTutor (S1) and Theobald's Lingxian page (S2) in full; read the Lingxian Chinese text on Wikisource (S3). Britannica timed out; encyclopedia.com DSB page 404. Wikipedia and New World Encyclopedia used only as leads (Needham translation, c. 120 date), not cited. Hou Han shu biography not read.
- 2026-10-21: ABZ audit fixes. Read Hou Han shu juan 59 on Wikisource (S5): '再遷為太史令 ... 遂乃研核陰陽 ... 作渾天儀，著靈憲'. Distance-speed theory now carries the scientist case. Rulings RQ-ABZ-1 and gloss-for-A recorded in OPEN_DECISIONS.
- 2026-10-24: Deepen D1. Needham SCC3 OCR (S6) for published EN; Wikipedia (S7) and NWE (S8) dual bio death Luoyang. Theobald re-fetch timed out — prior full read retained. A → 0.7; B basis → written_profession @0.5; mid_basin → false. No figures/.
