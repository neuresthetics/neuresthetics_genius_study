---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z9; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #162, F3 rank 170). Hunt: Retraction Middle English read in full (S4 UMSL/standard CT text; present in 28 MSS); scholarship divides on sincerity/authenticity and on whether it is a disavowal vs prayer for intercession (S5 Wikipedia; Herman Chaucer Review 2022 abstract; Harvard Chaucer site) — stays lead, not scored as profession (§3 / P42 / standing deepen rule). Treatise on the Astrolabe prologue + II.4 (S6 Skeat): 'lewd compilatour'; rejects 'observauncez of iudicial matiere and rytes of payens, in which my spirit ne hath no feith' — not locus, not P16 nature-order (Part IV on celestial causes unfinished). Pilgrim speech not coded (P42). primary_system stays UNKNOWN (lead CHRIST); A–E stay UNKNOWN; mid UNKNOWN; not plotted. P47 source_quality on S1–S6. No fallacy_catalog; figures/ untouched. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z9 audit fix (FAIL, P26; RQ-Z9-N1, v8's call on the auditor's advice): the 1387 start was cited to the biography opening, but the only '1387–1400' there is in the Top Questions box. Re-sourced to the Britannica topic article 'The Canterbury Tales' (S3, body read: 'written in Middle English in 1387–1400'). Under RQ-Z9-N1 a scholar's composition range dates a manuscript-era work (P12 start), so the span stays 1387–1400 and age 45. Retraction summary (S3) added as a lead. Not plotted."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z9, order P32: F 3, rank 170). Source: Britannica (R. M. Lumiansky, signed; opening, 'Forebears and early years'). No own-voice religious statement read: the Retraction at the end of The Canterbury Tales is a lead, not read here, and his first-person narrator 'both is and is not the poet himself' (S1). Religious themes in the poems are work, not profession (P16). Not a scientist. primary_system UNKNOWN (lead CHRIST); A, B, C, D, E UNKNOWN; mid_basin UNKNOWN. Span 1387–1400, age 45. Not plotted. Draft, not reviewed."}

identity:
  id: chaucer-geoffrey
  display_name: "Geoffrey Chaucer"
  roster:
    canonical_name: "Geoffrey Chaucer"
    rank: 170
    F: 3
    models: [Claude, Gemini, Grok]
    band: "core (3–4)"
    status: "core"
    field: "literature"
    field_bucket: "literature"
  full_name: {value: "Geoffrey Chaucer", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  native_name: {value: "Geffrey Chaucer", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Middle English spelling the coder's."}
  aliases:
    - {name: "Chaucer-Geoffrey", kind: "roster alias"}

basics:
  birth:
    date: {value: "1342", certainty: 0.5, cites: [{source: S1, locator: "Forebears and early years"}], how_known: "Britannica: 'c. 1342/43'; 1342 or 1343 'probably a closer guess' than c. 1340."}
    place: {value: "London", modern_name: "London, United Kingdom", polity_then: "Kingdom of England", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Britannica: 'London?'."}
  death:
    date: {value: "1400-10-25", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "London", modern_name: "London, United Kingdom", polity_then: "Kingdom of England", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1387, certainty: 0.5, cites: [{source: S3, locator: "Introduction (body)"}], how_known: "The Canterbury Tales, 'written in Middle English in 1387–1400' (Britannica topic article body, S3); a pre-print work circulated in manuscript, so the scholar's composition range is the dating event and 1387 is its start (RQ-Z9-N1, P12); earlier poems not called lasting in the body read."}
  era_bucket: {value: "500 to 1399", certainty: 1.0, cites: [{source: S3, locator: "Introduction (body)"}], how_known: "1387 (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "England, UK (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "Forebears and early years"}], how_known: "London and the court; missions abroad."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Middle English"], certainty: 0.7, cites: [{source: S1, locator: "Forebears and early years"}], how_known: "Britannica."}
  occupations: {value: ["poet", "courtier", "diplomat", "civil servant"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["poetry", "English literature"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "The Canterbury Tales", year: 1387, kind: "work", lasting: "'ranks as one of the greatest poetic works in the English language' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "Introduction (body)"}], how_known: "Lasting from the Lumiansky body (S1); dated by the topic article body, 'written in Middle English in 1387–1400', unfinished at his death (S3; RQ-Z9-N1: manuscript-era composition range; P12 start, P30 end). The 1387–1400 in the biography's Top Questions box is not cited (P26)."}
  evidence_of_impact:
    - {value: "The outstanding English poet before Shakespeare; 'the first finder of our language'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Book of the Duchess", year: 1370, kind: "book", certainty: 0.5, cites: [{source: S1, locator: "Forebears and early years"}], how_known: "Britannica: 'probably written in late 1369 or early 1370'."}
    - {value: "A Treatise on the Astrolabe", year: 1391, kind: "book", certainty: 0.7, cites: [{source: S6, locator: "Prologue; Part II examples dated 1391"}, {source: S5, locator: "Literary works"}], how_known: "Prose treatise for his son Lewis; dated by internal examples (yeer of oure lord 1391). Not a lasting contribution for the span (poetry is)."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Outstanding English poet before Shakespeare (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated (medieval Christian England is context only)."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "John Chaucer, London vintner, deputy to the king's butler", role: "father", certainty: 0.7, cites: [{source: S1, locator: "Forebears and early years"}], how_known: "Britannica."}
    - {value: "Agnes Copton", role: "mother", certainty: 0.7, cites: [{source: S1, locator: "Forebears and early years"}], how_known: "Britannica."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1387–1400", certainty: 0.5, cites: [{source: S3, locator: "Introduction (body)"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Astrolabe rejects judicial astrology as pagan rite without faith (S6 II.4); not a scored science–religion relation statement."}
  primary_system: {value: UNKNOWN, how_known: "Retraction read in full (S4): first-person appeal to Crist / Jhesu Crist for mercy, revocation of 'worldly vanitees', thanks for Boece and books of saints/devocioun, prayer for verray penitence and salvacioun. Scholarship divides on sincerity and authenticity and on whether the passage is a disavowal of the corpus or mainly a request for intercessory prayer (S5; Herman 2022; Harvard Chaucer site) — stays CHRIST lead, not scored as profession (standing deepen rule; P42). Narrator of the Tales 'both is and is not the poet himself' (S1); pilgrim speech not coded (P42). Religious themes in poems are work (P16)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Lead: Retraction Christ/mercy/penitence language; sincerity contested — not scored."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Retraction would speak of Christ as mercy/salvation if taken as sincere authorial profession, but scholarship divides — not scored (P19). No other non-fiction locus statement read."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30; lasting work is poetry). Astrolabe is a 'lewd compilatour' translation of old astrologers (S6); planned Part IV on celestial 'causes' unfinished. Rejection of judicial astrology (II.4) is not a statement of nature's lawful order (P16)."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Astrolabe II.4 rejects pagan horoscope rites; not scored as revelation-vs-observation."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "A and B are UNKNOWN (P19)."}
  statements:
    - text: "Wherfore I biseke yow mekely, for the mercy of God, that ye preye for me that Crist have mercy on me and foryeve me my giltes; and namely of my translacions and enditynges of worldly vanitees, the whiche I revoke in my retracciouns: as is the book of Troilus; the book also of Fame; the book of the XXV. Ladies; the book of the Duchesse; the book of Seint Valentynes day of the Parlement of Briddes; the tales of Caunterbury, thilke that sownen into synne; the book of the Leoun; and many another book. If they were in my remembrance, and many a song and many a leccherous lay; that Crist for his grete mercy foryeve me the synne. But of the translacion of Boece de Consolacione, and othere bookes of legendes of seintes, and omelies and moralitee, and devocioun. That thanke I oure lord Jhesu Crist and his blisful mooder, and alle the seintes of hevene, bisekynge hem that they from hennes forth unto my lyves ende sende me grace to biwayle my giltes, and to studie to the salvacioun of my soule, and graunte me grace of verray penitence, confessioun and satisfaccioun to doon in this present lyf … so that is may been oon of hem at the day of doom that shulle be saved."
      cites: [{source: S4, locator: "Chaucer's Retraction (end of Parson's Tale / CT)"}]
      date: "1400"
      context: "Closing prose of The Canterbury Tales (within the working span). First person lists his own titled works. Present in 28 MSS of the CT (S4). Scholarship divides on sincerity/authenticity and on disavowal vs prayer (S5) — lead only, not scored."
      axes: []
      kind: "other"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Kind other: literary closing, not a free-standing written profession. Not scored under P42 / contested sincerity. Riverside Chaucer page-image not collated; text matches standard CT editions (UMSL / Wikisource / Michigan CME wording)."
    - text: "Natheles, thise ben observauncez of iudicial matiere and rytes of payens, in which my spirit ne hath no feith, ne no knowing of hir horoscopum."
      cites: [{source: S6, locator: "Treatise on the Astrolabe, Part II, §4"}]
      date: "1391"
      context: "Non-fiction prose treatise for his son Lewis (within span). After explaining astrologers' rules for a 'fortunat' ascendant, he disclaims faith in judicial astrology / pagan horoscope rites. Prologue: 'I nam but a lewd compilatour of the labour of olde Astrologiens'."
      axes: []
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Own-voice rejection of judicial astrology; not scored on A (not a God-locus claim) or B (not nature's law vs exception; P16). Part IV on celestial causes was planned and unfinished."
  changes_over_life: []
  coder_notes: "D1: Retraction read; stays CHRIST lead (sincerity contested). Astrolabe II.4 read; no A/B lift. Do not code pilgrim tales (P42). Do not force plot. Riverside Chaucer (Benson) page not collated."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English (London merchant family)", certainty: 0.7, cites: [{source: S1, locator: "Forebears and early years"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated in sources read (medieval Christian England is ambient context only, not coded)."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1387–1400", certainty: 0.5, cites: [{source: S3, locator: "Introduction (body)"}], how_known: "The Canterbury Tales, 1387–1400 from the topic article body (S3); composition range accepted for a manuscript-era work (RQ-Z9-N1); P29; P12 start, range end; never past death, P30."}
  age_at_first_lasting_contribution: {value: 45, certainty: 0.5, cites: [{source: S1, locator: "Forebears and early years"}, {source: S3, locator: "Introduction (body)"}], how_known: "1387 − 1342 = 45 (P30 year difference); birth 1342 or 1343."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "Retraction and Astrolabe read but not scored on axes."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None scored."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None scored."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Poetry (S1); Astrolabe is instructional compilation, not lasting geometric science.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions: []
collaborators:
  - {value: "John of Gaunt", relation: "mentor or employer", note: "patron; Book of the Duchess", certainty: 0.7, cites: [{source: S1, locator: "Forebears and early years"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 170"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Retraction sincerity/authenticity contested in scholarship; kept as CHRIST lead only."
    - "Retraction text from unofficial web copy of standard CT wording; Riverside page-image not collated."
  open_questions:
    - "Riverside Chaucer (Benson) critical text and notes for Retraction."
    - "Peer-reviewed monograph that would settle sincerity enough for §3 scoring (Herman 2022 argues against over-reading disavowal)."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "R. M. Lumiansky"
    citation: "Lumiansky, R. M. 'Geoffrey Chaucer.' Encyclopaedia Britannica (rev. 2026). https://www.britannica.com/biography/Geoffrey-Chaucer"
    url: "https://www.britannica.com/biography/Geoffrey-Chaucer"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Signed article; body cited, question boxes not used (P26). Re-fetched 2026-10-24."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, collaborators]
  - id: S2
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [review]
  - id: S3
    type: tertiary
    kind: "encyclopedia"
    author: "The Editors of Encyclopaedia Britannica"
    citation: "'The Canterbury Tales.' Encyclopaedia Britannica (Scholars edition). https://kids.britannica.com/scholars/article/The-Canterbury-Tales/484183"
    url: "https://kids.britannica.com/scholars/article/The-Canterbury-Tales/484183"
    accessed: 2026-10-19
    source_quality: "reference entry"
    reliability_note: "Topic article; body read in full (introduction: 'written in Middle English in 1387–1400'); not a question box."
    used_for: [basics, contribution, worldview, timing]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Geoffrey Chaucer"
    citation: "Chaucer, Geoffrey. 'Chaucer's Retraction' (closing The Canterbury Tales). Middle English text as at University of Missouri–St. Louis Chaucer pages (standard CT wording; present in 28 MSS). https://www.umsl.edu/~gradyf/chaucer/retraction.htm"
    url: "https://www.umsl.edu/~gradyf/chaucer/retraction.htm"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Teaching-site copy of standard Middle English Retraction; wording matches Wikisource/Michigan CME extracts. Riverside Chaucer not collated. Used as lead text only, not scored."
    used_for: [worldview]
  - id: S5
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "Wikipedia. 'Geoffrey Chaucer.' EN revid 1380585352 (2026-10-16). https://en.wikipedia.org/wiki/Geoffrey_Chaucer"
    url: "https://en.wikipedia.org/wiki/Geoffrey_Chaucer"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "P50 dual-bio with Britannica (S1) for Astrolabe dating / Retraction debate summary only. Explicitly: sincerity and authenticity of the Retraction have been questioned. Not used to score worldview."
    used_for: [contribution, worldview]
  - id: S6
    type: primary
    kind: "scholarly edition"
    author: "Geoffrey Chaucer; Walter W. Skeat (ed.)"
    citation: "Chaucer, Geoffrey. A Treatise on the Astrolabe. In The Complete Works of Geoffrey Chaucer, vol. 3, ed. Walter W. Skeat. Wikisource text of Skeat. https://en.wikisource.org/wiki/Chaucer%27s_Works_(ed._Skeat)_Vol._III/Treatise_on_the_Astrolabe"
    url: "https://en.wikisource.org/wiki/Chaucer%27s_Works_(ed._Skeat)_Vol._III/Treatise_on_the_Astrolabe"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Skeat scholarly edition via Wikisource. Prologue and Part II §4 read for own-voice prose."
    used_for: [contribution, worldview]
---

## Summary

Geoffrey Chaucer (c. 1342–1400), poet [S1]. Primary UNKNOWN (lead CHRIST); A–E UNKNOWN. Not plotted. D1: Retraction and Astrolabe read; scores unchanged.

## Life and work

London; court service; diplomacy [S1].

## Contribution and impact

The Canterbury Tales [S1]. Treatise on the Astrolabe (prose, c. 1391) [S6].

## Childhood and education

Vintner's son [S1].

## Adult working worldview

Retraction (S4): Christ/mercy/penitence language — CHRIST lead; sincerity contested in scholarship (S5) — not scored. Astrolabe (S6): rejects judicial astrology; no A/B profession. Pilgrim speech not coded (P42).

## Heritage (context only)

English [S1]. Religious heritage not stated.

## Timing

1387–1400, age 45 [S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Riverside Chaucer critical text; monograph settling Retraction sincerity for §3.

## Research log

- 2026-10-19: Read Britannica (Lumiansky); Z9 span fix via S3.
- 2026-10-24 (D1): Retraction full text (S4); Astrolabe Skeat (S6); Wikipedia Retraction debate (S5); Herman 2022 / Harvard Chaucer site skimmed. Scores unchanged. Chart-moving NO.
