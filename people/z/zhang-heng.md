---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 single run AB-Z)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-21
  last_updated: 2026-10-21
  change_log:
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
  first_lasting_contribution_year: {value: 132, certainty: 0.7, cites: [{source: S1, locator: "Biography, seismograph paragraph"}], how_known: "Seismoscope 'In 132' (S1); the only dated lasting item. The Lingxian is undated in the sources read (P30 #1)."}
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
    - {value: "Lingxian: theory of moonlight as reflected sunlight and of lunar eclipses as the Earth's obstruction", year: UNKNOWN, kind: "theory", lasting: "'an important theoretical work on astronomy' offering 'scientific explanations for moonlight and lunar eclipses' (S2)", certainty: 0.7, cites: [{source: S2, locator: "paragraphs 3 and 7"}, {source: S3, locator: "夫日譬猶火 ... 是謂闇虛"}], how_known: "Undated in S1–S3 (c. 120 is a lead only, from an uncitable wiki)."}
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
  working_years: {value: "132", certainty: 0.7, cites: [{source: S1, locator: "Biography, seismograph paragraph"}], how_known: "Equals timing.major_work_period. The undated Lingxian is adult work and counts for the span at its normal certainty (P31)."}
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
      how_known: "His own published treatise, but read in an unofficial web copy of fragments assembled in the Qing (S2) and through the coder's own gloss of the Classical Chinese, so 0.5."
      rationale: "Immanent pole features: the cosmos emerges from the Dao's 'root' ('自無生有', 'from non-being arises being') and things 'arise of themselves from one another' ('自然相生'); no creator person outside the world. Limited personal feature: 'the mind of Heaven is seen' (天心於是見矣) in the luminaries' portents. So 3. Alternative 4 if 天心 is read impersonally."
      alternatives:
        - {value: 4, note: "天心 read as an impersonal order, not a mind.", cites: [{source: S3, locator: "天心於是見矣"}]}
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      cites: [{source: S2, locator: "paragraphs 3 and 7"}, {source: S3, locator: "夫日譬猶火 ... 是謂闇虛"}]
      how_known: "Scientist (P30): the Lingxian's theory of moonlight and lunar eclipses is a theory about natural systems. B from working science, no statement of his own on law and exception, so 3 at 0.5, alternative 4, never 4 (P35)."
      rationale: "P35. Lead for B 2 (RQ-ABZ-1): the same text says the luminaries' motions 'show good and ill fortune' and the planets 'announce calamity and blessing' (歷示吉凶 ... 用告禍福), and that certain stars 'appear at no fixed time and move with no fixed measure' (其見無期，其行無度) as portents. Not counted here, because portents read from regular motions are not stated exceptions to law."
      alternatives:
        - {value: 4, note: "P35 alternative.", cites: [{source: S2, locator: "paragraph 7"}]}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 3 is scored only at 0.5, under the 0.7 bar for the A ≥ 3 branch (P10).", note: "If A reached 0.7 the result would be false."}
  statements:
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
      cites: [{source: S3, locator: "second paragraph, Sun and Moon passage"}, {source: S2, locator: "paragraph 7"}]
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
  major_work_period: {value: "132", certainty: 0.7, cites: [{source: S1, locator: "Biography, seismograph paragraph"}], how_known: "The only dated lasting item (P29, P30); the Lingxian is undated."}
  age_at_first_lasting_contribution: {value: 54, certainty: 0.7, cites: [{source: S1, locator: "Quick Info; seismograph paragraph"}], how_known: "132 − 78 = 54 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "The Lingxian is undated in the sources read."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "Lingxian undated."}
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
    - "Lingxian undated in the sources read, so the span is the seismoscope year alone."
    - "Roster field 'invention'; scientist status rests on the Lingxian theory, not the seismoscope (P33)."
  open_questions:
    - "RQ-ABZ-1: do the Lingxian portent passages (吉凶, 禍福, stars 'with no fixed measure') lower B to 2, or stay outside B as readings of regular motion?"
    - "Can a coder's own gloss of a Classical Chinese text carry A, or does it need a published translation?"
    - "Date of the Lingxian (c. 120 lead) would add it to the span."

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

Seismoscope of 132 [S1]; the Lingxian explains moonlight and lunar eclipses [S2, S3].

## Childhood and education

Confucian education and ten years of literary study [S1].

## Adult working worldview

The Lingxian's cosmos grows from the Dao and things arise of themselves, while Heaven's "mind" shows in portents [S3, S2]. No single system code reaches 0.5.

## Heritage (context only)

Not stated.

## Timing

Span 132 (seismoscope), age 54 [S1]. The Lingxian is undated in the sources read.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- RQ-ABZ-1 (portents and B); coder's gloss as basis for A; date of the Lingxian.

## Research log

- 2026-10-21: Read MacTutor (S1) and Theobald's Lingxian page (S2) in full; read the Lingxian Chinese text on Wikisource (S3). Britannica timed out; encyclopedia.com DSB page 404. Wikipedia and New World Encyclopedia used only as leads (Needham translation, c. 120 date), not cited. Hou Han shu biography not read.
