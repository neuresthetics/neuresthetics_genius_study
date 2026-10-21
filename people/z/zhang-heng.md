---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 single run AB-Z)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-21
  last_updated: 2026-10-21
  change_log:
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

basics:
  birth:
    date: {value: "0078", calendar: julian, certainty: 1.0, cites: [{source: S1, locator: "Quick Info"}, {source: S2, locator: "opening paragraph"}], how_known: "Both give 78; year only."}
    place: {value: "Nanyang (E county, Nanyang commandery)", modern_name: "Nanyang, Henan, China", polity_then: "Eastern Han", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}, {source: S2, locator: "opening paragraph"}], how_known: "MacTutor 'Nan-yang'; Theobald 'from E 鄂 in the commandery of Nanyang'. Agree on the commandery; county from S2 only."}
  death:
    date: {value: "0139", calendar: julian, certainty: 1.0, cites: [{source: S1, locator: "Quick Info"}, {source: S2, locator: "opening paragraph"}], how_known: "Both give 139."}
    place: {value: UNKNOWN, how_known: "MacTutor says only 'China'; S2 silent."}
  first_lasting_contribution_year: {value: 132, certainty: 0.5, cites: [{source: S1, locator: "Biography, seismograph paragraph"}, {source: S5, locator: "張衡傳"}], how_known: "Seismoscope 'In 132' (S1), the only lasting item with a year (P30 #1). Alternative 115 under RQ-Z9-N1: S5 places the Lingxian in his Grand Astrologer tenure (see timing).", alternatives: [{value: 115, note: "Start of the c. 115–120 range for the Lingxian (RQ-Z9-N1).", cites: [{source: S5, locator: "張衡傳"}]}]}
  era_bucket: {value: "-500 to 499", certainty: 1.0, cites: [{source: S1, locator: "Quick Info"}], how_known: "132 (P2); his whole life (78–139) is in this bucket."}
  region_of_birth: {value: "East Asia", certainty: 1.0, cites: [{source: S1, locator: "Quick Info"}, {source: S2, locator: "opening paragraph"}], how_known: "China (P3)."}
  region_of_work: {value: "East Asia", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Imperial court at Luoyang."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "As recorded."}
  languages_of_work: {value: ["Classical Chinese"], certainty: 0.7, cites: [{source: S3, locator: "full text"}], how_known: "Text of the Lingxian."}
  occupations: {value: ["astronomer", "court official (Grand Astrologer)", "poet", "inventor", "mathematician"], certainty: 1.0, cites: [{source: S1, locator: "Summary; Biography"}, {source: S2, locator: "opening paragraph"}], how_known: "Both sources."}

contribution:
  fields: {value: ["astronomy", "invention", "literature", "mathematics"], certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  lasting_original_contributions:
    - {value: "Seismoscope (Hou Feng Di Dong Yi)", year: 132, kind: "invention", lasting: "'In 132 Zhang invented the first seismograph for measuring earthquakes' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Biography, seismograph paragraph"}], how_known: "Device (P33): does not by itself make him a scientist."}
    - {value: "Lingxian: theory linking the speeds of the Sun, Moon and five planets to their distance from heaven (近天則遟，遠天則速)", year: UNKNOWN, kind: "theory", lasting: "'Zhang Heng introduced an innovative theory linking the speeds of the Sun, Moon, and five visible planets to their distances'; 'His insights into the varying speeds of celestial bodies were groundbreaking' (S2)", certainty: 0.7, cites: [{source: S2, locator: "paragraphs 3 and 8"}, {source: S3, locator: "近天則遟，遠天則速"}], how_known: "Year not given in S1–S3; S5 places the Lingxian after his appointment as Grand Astrologer (span alternative 115–120, timing). The moonlight and eclipse explanations in the same text are views he 'adopted' from Jing Fang and Wang Chong (S2 para 8), so not listed as original (ABZ audit #13)."}
  evidence_of_impact:
    - {value: "Seismoscope reported a distant earthquake (138) confirmed days later", kind: "other", certainty: 0.7, cites: [{source: S1, locator: "Biography, seismograph paragraph"}], how_known: "MacTutor."}
  major_works:
    - {value: "Huntian yi zhu (on the armillary sphere)", year: UNKNOWN, kind: "book", certainty: 0.7, cites: [{source: S2, locator: "opening paragraph"}], how_known: "Theobald."}
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
  primary_system: {value: BELOW_THRESHOLD, how_known: "The Lingxian frames cosmogony through the Dao ('道之根', '道之幹', '道之實') and quotes the Daodejing ('有物渾成，先天地生') (S3); S2 reads its 'spirit' as 'corresponding to the Daoist concept of Dao'. S1 says his 'strong moral beliefs' were 'based in Confucianism', and his office read portents (S1). Han correlative cosmology mixes TAO, CONFUC and CHNFOLK; no single code reaches 0.5."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: TAO, reason: "Dao cosmogony and Daodejing quotation in the Lingxian (S3; S2)."}
    - {code: CONFUC, reason: "Confucian education and moral beliefs (S1)."}
    - {code: CHNFOLK, reason: "Portent reading: Heaven's 'mind' shown in the luminaries (S3)."}
  lio_axes:
    A_locus:
      value: 3
      basis: written_profession
      certainty: 0.5
      cites: [{source: S3, locator: "太素之前 ... 自然相生; 天心於是見矣"}, {source: S2, locator: "paragraph 4"}]
      how_known: "His own published treatise, but read in an unofficial web copy of fragments assembled in the Qing (S2) and through the coder's own gloss of the Classical Chinese, so 0.5. The coder's gloss of verbatim cited text carries A at 0.5 (v8's call on the auditor's advice, ABZ); 0.7 needs a published translation or authoritative edition."
      rationale: "Immanent pole features: the cosmos emerges from the Dao's 'root' ('自無生有', 'from non-being arises being') and things 'arise of themselves from one another' ('自然相生'); no creator person outside the world. Limited personal feature: 'the mind of Heaven is seen' (天心於是見矣) in the luminaries' portents. So 3. Alternative 4 if 天心 is read impersonally, supported by the preface: '聖人無心，因茲以生心' (coder's gloss: 'the sage has no mind [of his own]; from this he forms his mind'), where mind is taken from the cosmic pattern."
      alternatives:
        - {value: 4, note: "天心 read as an impersonal order, not a mind; preface 聖人無心，因茲以生心.", cites: [{source: S3, locator: "天心於是見矣; preface 聖人無心，因茲以生心"}]}
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      cites: [{source: S2, locator: "paragraphs 3 and 8"}, {source: S3, locator: "近天則遟，遠天則速"}]
      how_known: "Scientist (P30): the Lingxian's distance-speed theory of the seven luminaries (S2 para 8, 'innovative') is a theory about natural systems. B from working science, no statement of his own on law and exception, so 3 at 0.5, alternative 4, never 4 (P35)."
      rationale: "P35. Note (RQ-ABZ-1, v8's call on the auditor's advice: omen-reading, not a stated exception to law; no score change): the same text says the luminaries' motions 'show good and ill fortune' and the planets 'announce calamity and blessing' (歷示吉凶 ... 用告禍福), and that certain stars 'appear at no fixed time and move with no fixed measure' (其見無期，其行無度) as portents. Portents read from regular motions, and irregular objects (comets, novae) read as signs, are correlative signification; neither states that an agent suspends regular motion."
      alternatives:
        - {value: 4, note: "P35 alternative.", cites: [{source: S2, locator: "paragraph 8"}]}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 3 is scored only at 0.5, under the 0.7 bar for the A ≥ 3 branch (P10).", note: "If A reached 0.7 the result would be false."}
  statements:
    - text: "聖人無心，因茲以生心，故靈憲作興。"
      cites: [{source: S3, locator: "preface"}]
      context: "Lingxian preface. Coder's gloss: 'The sage has no mind [of his own]; from this he forms his mind, and so the Lingxian was made.' Support for alt A 4 (ABZ audit)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-21
    - text: "斯謂溟涬，蓋乃道之根也。道根旣建，自無生有。"
      cites: [{source: S3, locator: "second paragraph, opening"}]
      context: "Lingxian cosmogony. Coder's gloss: 'This is called the Dark Sediment; it is the root of the Dao. The root of the Dao once established, being arose from non-being.'"
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-21
    - text: "情性萬殊，旁通感薄，自然相生，莫之能紀。"
      cites: [{source: S3, locator: "second paragraph"}]
      context: "Coder's gloss: 'Their natures differ in ten thousand ways; they interpenetrate and affect one another, arise of themselves from one another, beyond anyone's reckoning.'"
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-21
    - text: "日月運行，歷示吉凶，五緯躔次，用告禍福，則天心於是見矣。"
      cites: [{source: S3, locator: "second paragraph, star passage"}]
      context: "Coder's gloss: 'The movements of Sun and Moon show good and ill fortune; the stations of the five planets announce calamity and blessing; thus the mind of Heaven is seen.'"
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-21
    - text: "故月光生於日之所照，魄生於日之所蔽"
      cites: [{source: S3, locator: "second paragraph, Sun and Moon passage"}, {source: S2, locator: "paragraph 8"}]
      context: "Moonlight as reflected sunlight. Coder's gloss: 'Thus the Moon's light arises from where the Sun shines on it, and its dark part from where the Sun's light is blocked.'"
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-21
  changes_over_life: []
  coder_notes: "A and B rest on one fragmentary text in an unofficial web copy with the coder's gloss. A published translation (Needham, SCC vol. 3, p. 414 per a lead; Cullen) would let the statements be checked and might lift A to 0.7, which would make mid_basin false. The Hou Han shu biography (his memorial against the chenwei prognostication texts) is unread and bears on D."

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
    cites: [{source: S1, locator: "Biography, seismograph paragraph"}, {source: S5, locator: "張衡傳: 再遷為太史令 ... 著靈憲"}]
    how_known: "The seismoscope (132) is the only lasting item with a year (P29, P30). S5 places the Lingxian after his appointment as Grand Astrologer but gives no year; 0.5 because the alternative is real (P25)."
    alternatives:
      - {value: "115–120", note: "RQ-Z9-N1 start of range: Lingxian written during his Grand Astrologer tenure (S5); court appointment 'In around 116' (S1); range c. 115–120 per the ABZ audit (the 120 end and 115 start are from zh encyclopedic sources the coder has not read). Age about 37–42.", cites: [{source: S5, locator: "張衡傳"}, {source: S1, locator: "Biography, paragraph 2"}]}
  age_at_first_lasting_contribution: {value: 54, certainty: 0.5, cites: [{source: S1, locator: "Quick Info; seismograph paragraph"}], how_known: "132 − 78 = 54 (P30 year difference); about 37–42 under the 115–120 span alternative."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "The Lingxian has no year in the sources read; S5 places it in his Grand Astrologer tenure (c. 115–120 alternative)."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "Same text as one lasting item; no year."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "primary_system BELOW_THRESHOLD."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Cosmic dimensions computed by 重差鉤股 (double differences and right triangles) (S3), not proofs.", certainty: 0.5, cites: [{source: S3, locator: "八極之維 ... 皆移千里而差一寸得之"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not stated."}
  circle_present: {value: "unclear", rationale: "Sky 'like a hen's egg ... as round as a crossbow pellet' (S1); not assessed further.", certainty: 0.5, cites: [{source: S1, locator: "armillary sphere paragraph"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Eastern Han imperial court, Luoyang", role: "official; Grand Astrologer (taishi ling)", years: "c. 116–", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "Biography, paragraph 2"}, {source: S2, locator: "opening paragraph"}], how_known: "MacTutor 'In around 116'; end year not stated."}
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 230"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "A and B statements read only in an unofficial web copy of the Chinese text (Qing-assembled fragments), with the coder's own gloss."
    - "Lingxian has no year in the sources read; S5 places it in his Grand Astrologer tenure. Span 132 at 0.5, alternative 115–120 (RQ-Z9-N1)."
    - "Roster field 'invention'; scientist status rests on the Lingxian theory, not the seismoscope (P33)."
  open_questions:
    - "A published translation (Needham SCC 3; Cullen) could lift A to 0.7, which would make mid_basin false."
    - "A scholarly year for the Lingxian (c. 115–120; 118 in some Chinese sources) would settle the span."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "J. J. O'Connor and E. F. Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Zhang Heng.\" MacTutor History of Mathematics Archive, University of St Andrews (last update December 2003). https://mathshistory.st-andrews.ac.uk/Biographies/Zhang_Heng/"
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Zhang_Heng/"
    accessed: 2026-10-21
    reliability_note: "Signed biographical archive, read in full."
    used_for: [identity, basics, contribution, childhood, worldview, timing, lane_b, institutions]
  - id: S2
    type: tertiary
    kind: "encyclopedia"
    author: "Ulrich Theobald"
    citation: "Theobald, Ulrich. \"Lingxian 靈憲.\" ChinaKnowledge.de, 24 March 2025. http://www.chinaknowledge.de/Literature/Science/lingxian.html"
    url: "http://www.chinaknowledge.de/Literature/Science/lingxian.html"
    accessed: 2026-10-21
    reliability_note: "Signed reference page by a sinologist, with a bibliography; read in full."
    used_for: [identity, basics, contribution, worldview, institutions]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Zhang Heng"
    citation: "Zhang Heng 張衡. Lingxian 靈憲 (fragments). Chinese text, Wikisource. https://zh.wikisource.org/wiki/靈憲"
    url: "https://zh.wikisource.org/wiki/靈憲"
    accessed: 2026-10-21
    reliability_note: "Unofficial web copy of the surviving fragments; edition not stated on the page; not checked against an authoritative edition. English glosses are the coder's."
    used_for: [basics, contribution, worldview, lane_b]
  - id: S5
    type: primary
    kind: "other"
    author: "Fan Ye"
    citation: "Fan Ye 范曄. Hou Han shu 後漢書, juan 59, 張衡列傳 (biography of Zhang Heng). Chinese text, Wikisource. https://zh.wikisource.org/wiki/後漢書/卷59"
    url: "https://zh.wikisource.org/wiki/後漢書/卷59"
    accessed: 2026-10-21
    reliability_note: "Standard history (5th c.); unofficial web copy; read the passage on his appointment and the Lingxian."
    used_for: [timing]
  - id: S4
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-21
    reliability_note: "Study's own roster."
    used_for: [review]
---

## Summary

Zhang Heng (78–139), Eastern Han astronomer, inventor and poet [S1, S2]. A 3 and B 3, both at 0.5. Plots, faded.

## Life and work

Nanyang; court official at Luoyang from about 116, several times Grand Astrologer [S1, S2].

## Contribution and impact

Seismoscope of 132 [S1]; the Lingxian's distance-speed theory of the seven luminaries [S2, S3]; its moonlight and eclipse views were adopted from Jing Fang and Wang Chong [S2].

## Childhood and education

Confucian education and ten years of literary study [S1].

## Adult working worldview

The Lingxian's cosmos grows from the Dao and things arise of themselves, while Heaven's "mind" shows in portents [S3, S2]. No single system code reaches 0.5.

## Heritage (context only)

Not stated.

## Timing

Span 132 (seismoscope), age 54 [S1], at 0.5. Alternative 115–120, age about 37–42: the Lingxian was written after he became Grand Astrologer [S5].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Published translation for A; scholarly year for the Lingxian.

## Research log

- 2026-10-21: Read MacTutor (S1) and Theobald's Lingxian page (S2) in full; read the Lingxian Chinese text on Wikisource (S3). Britannica timed out; encyclopedia.com DSB page 404. Wikipedia and New World Encyclopedia used only as leads (Needham translation, c. 120 date), not cited. Hou Han shu biography not read.
- 2026-10-21: ABZ audit fixes. Read Hou Han shu juan 59 on Wikisource (S5): '再遷為太史令 ... 遂乃研核陰陽 ... 作渾天儀，著靈憲'. Distance-speed theory now carries the scientist case. Rulings RQ-ABZ-1 and gloss-for-A recorded in OPEN_DECISIONS.
