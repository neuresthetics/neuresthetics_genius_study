---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch E)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-15
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch E, order P32: F 5, rank 20). Basics from Britannica (Quinones). Worldview from Monarchia III.xvi in Prue Shaw's edition and English translation (Dante Online, Società Dantesca Italiana). The Commedia's speakers, including the pilgrim, are characters and are not used. Not a scientist. CHRIST 0.7; A 0 (0.7); B 3 (0.5); D 2 (0.7); mid_basin BELOW_THRESHOLD. Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Audit fix (fallacy_catalog audit of 2332880, run 1): B_cause 3 (0.5) -> BELOW_THRESHOLD (alternative 4); Mon. III.xvi.12-13 is political and God acts through the order of the heavens, so no stated exception. mid_basin stays BELOW_THRESHOLD. Drops off the person chart."}

identity:
  id: alighieri-dante
  display_name: "Dante Alighieri"
  roster:
    canonical_name: "Dante Alighieri"
    rank: 20
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: literature
    field_bucket: literature
  full_name: {value: "Dante Alighieri", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts ('In full')"}], how_known: "Britannica alone."}
  native_name: {value: UNKNOWN, how_known: "Italian in Latin script; same as display name."}
  aliases:
    - {name: "Dante-Alighieri", kind: "roster alias"}

basics:
  birth:
    date: {value: "1265", approx: true, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts ('c. May 21–June 20, 1265')"}], how_known: "Britannica alone; day uncertain."}
    place: {value: "Florence", modern_name: "Florence, Italy", polity_then: "Republic of Florence", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Britannica alone."}
  death:
    date: {value: "1321-09-13", approx: true, calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts ('September 13/14, 1321')"}], how_known: "Britannica alone; 13 or 14 September."}
    place: {value: "Ravenna", modern_name: "Ravenna, Italy", polity_then: "Ravenna (da Polenta lordship)", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Britannica alone."}
  first_lasting_contribution_year: {value: 1293, certainty: 0.5, cites: [{source: S1, locator: "'Who was Dante's muse?' ('La vita nuova (c. 1293)')"}], how_known: "Earliest listed lasting contribution; Britannica dates it 'c. 1293', so 0.5 (circa date)."}
  era_bucket: {value: "500 to 1399", certainty: 0.7, cites: [{source: S1, locator: "dates"}], how_known: "Every candidate year (c. 1293, 1308) is in '500 to 1399' (derived-field exception, §3)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Italy (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "exile; Ravenna"}], how_known: "Florence, then Italian exile."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [Italian, Latin], certainty: 0.7, cites: [{source: S1, locator: "opening (vernacular rather than Latin; De monarchia)"}], how_known: "Britannica."}
  occupations: {value: ["poet", "prose writer", "political thinker"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["poetry", "literary theory", "moral and political philosophy"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "La vita nuova", year: "c. 1293", kind: work, lasting: "chronicle of his love for Beatrice; canon of Italian literature", certainty: 0.5, cites: [{source: S1, locator: "'Who was Dante's muse?'"}], how_known: "Britannica; circa date."}
    - {value: "La commedia (The Divine Comedy), in the Tuscan vernacular", year: "c. 1308–1321", kind: work, lasting: "'one of the world's most important and influential works of literature'; made Italian a literary language (S1)", certainty: 0.7, cites: [{source: S1, locator: "intro; opening"}], how_known: "Britannica; finished shortly before his death."}
  evidence_of_impact:
    - {value: "'considered the greatest Italian poet'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "intro"}], how_known: "Britannica."}
  major_works:
    - {value: "De monarchia", year: "undated", kind: book, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica names it, undated in the text read."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Commedia; founding influence on literary Italian.", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Family of lesser nobility in Florence; mother died before he was 14, father before 1283", role: other, certainty: 0.7, cites: [{source: S1, locator: "'early life'"}], how_known: "Britannica."}
  household_circumstances: {value: "Lesser nobility", certainty: 0.7, cites: [{source: S1, locator: "'early life'"}], how_known: "Britannica."}
  schooling: []
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events:
    - {value: "Met Beatrice Portinari", year: 1274, age: 9, certainty: 0.7, cites: [{source: S1, locator: "'early life'"}], how_known: "Britannica gives age nine; year = 1265 + 9 (P30)."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1293–1321", certainty: 0.5, cites: [{source: S1, locator: "dates"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Two goals and two means: 'we attain the first through the teachings of philosophy [...] whereas we attain the second through spiritual teachings which transcend human reason' (Monarchia III.xvi.8).", certainty: 1.0, cites: [{source: S2, locator: "Mon. III.xvi.8"}], how_known: "His published treatise in a critical edition and translation (Shaw)."}
  primary_system:
    value: CHRIST
    basis: written_profession
    certainty: 0.7
    cites: [{source: S2, locator: "Mon. III.xvi.7–10, 18"}]
    rationale: "The Holy Spirit 'through Jesus Christ the son of God, coeternal with him [...] has revealed to us the transcendent truth we cannot do without', and the Pontiff leads mankind 'in conformity with revealed truth': the religion as confessed. CLASS_THEISM is the named alternative (Aristotle cited, God 'one in the citadel of its own simplicity of nature', III.xvi.15), but the chapter's route is revelation, not an a posteriori argument (P22), so 0.7."
    how_known: "Critical edition and translation (Shaw); alternative named, so 0.7."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Chosen."}
    - {code: CLASS_THEISM, reason: "Alternative: Aristotelian-scholastic frame; God simple."}
    - {code: CLTHEI, reason: "Rejected as primary: God's choice of the emperor works through the preordained disposition of the heavens."}
  lio_axes:
    A_locus:
      value: 0
      basis: written_profession
      certainty: 0.7
      cites: [{source: S2, locator: "Mon. III.xvi.2, 12–13, 18"}]
      rationale: "God is 'the prince of the universe', who 'alone chooses' the emperor and is 'ruler over all things spiritual and temporal': a transcendent person outside the world. Alternative 1 (the simple God of III.xvi.15), so 0.7."
      how_known: "Critical edition; alternative named."
    B_cause:
      value: BELOW_THRESHOLD
      cites: [{source: S2, locator: "Mon. III.xvi.12–13"}]
      how_known: "Coder's call (conservative option, P30 #16), after the fallacy_catalog audit of 2332880. The only passage read touches nature in passing, in a political argument."
      note: "'The disposition of this world is a result of the disposition inherent in the circling of the heavens', which God 'preordained [...] making provision through it to bind all things in due order' states a general order. 'God alone chooses' the emperor works through that order and concerns politics, not nature, so it is not a stated exception; no miracle or exception is stated in the text read. Named alternative 4 (lawful order with no stated exception). Keep 3 only if a stated miracle is found."
    C_ledger: {value: UNKNOWN, how_known: "Not treated in the chapter read; the Commedia's afterlife is a poem's fiction and is not used."}
    D_authority:
      value: 2
      basis: written_profession
      certainty: 0.7
      cites: [{source: S2, locator: "Mon. III.xvi.8–10"}]
      rationale: "Two domains each with its own authority (P27 anchor): philosophy and the Emperor for 'temporal happiness', revelation and the Pontiff for 'eternal life'. Indirect on observation as such, so 0.7."
      how_known: "Critical edition; indirect."
    E_scope: {value: UNKNOWN, how_known: "Scored on the world's order (P7); nothing read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus 0 at 0.7, but B_cause is BELOW_THRESHOLD (P4, §6)."}
  statements:
    - text: "Now these two kinds of happiness must be reached by different means, as representing different ends. For we attain the first through the teachings of philosophy, provided that we follow them putting into practice the moral and intellectual virtues; whereas we attain the second through spiritual teachings which transcend human reason, provided that we follow them putting into practice the theological virtues, i.e. faith, hope and charity."
      cites: [{source: S2, locator: "Mon. III.xvi.8"}]
      date: "1321"
      context: "Final chapter of Monarchia, on the two ends of man. Undated work; death year used as the evidence date (P39 practice)."
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-15
      axes: [D_authority]
      note: "Shaw's translation; Latin 'per phylosophica documenta [...] per documenta spiritualia que humanam rationem transcendunt'. Monarchia's date is disputed; the death year bounds it (P39 practice)."
    - text: "And since the disposition of this world is a result of the disposition inherent in the circling of the heavens, in order that useful teachings concerning freedom and peace can be applied appropriately to times and places, it is necessary for provision for this protector to be made by Him who takes in at a glance the whole disposition of the heavens. For he alone is the one who preordained this disposition, making provision through it to bind all things in due order."
      cites: [{source: S2, locator: "Mon. III.xvi.12"}]
      date: "1321"
      context: "Argument that the emperor depends directly on God."
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-15
      axes: [B_cause, A_locus]
    - text: "If this is so, then God alone chooses, he alone confirms, since he has none above him."
      cites: [{source: S2, locator: "Mon. III.xvi.13"}]
      date: "1321"
      context: "Same argument."
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-15
      axes: [A_locus, B_cause]
  changes_over_life: []
  coder_notes: "Coder's call: the Commedia is not used for axes (fictional speakers, including the narrator-pilgrim). Monarchia III.xvi alone was read."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Florentine", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1293–1321", certainty: 0.5, cites: [{source: S1, locator: "dates"}], how_known: "Vita nuova (c. 1293) to the Commedia (range end 1321, his death year) (P29, P30)."}
  age_at_first_lasting_contribution: {value: 28, certainty: 0.5, cites: [{source: S1, locator: "dates"}], how_known: "1293 − 1265 = 28 (P30); circa year, so 0.5."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "B is BELOW_THRESHOLD and the passage is undated; no dated LIO-type statement found."}
  lio_views_relative_to_major_work: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "Mon. III.xvi"}], how_known: "Monarchia undated."}
  worldview_during_major_work: {value: "CHRIST", certainty: 0.7, cites: [{source: S2, locator: "Mon. III.xvi"}], how_known: "As coded."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "Monarchia argues by syllogism and reductio ('a reductio ad absurdum', III.xvi.1).", certainty: 0.5, cites: [{source: S2, locator: "Mon. III.xvi.1"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "opening (scholastic learning)"}], how_known: "Nothing read on his schooling."}
  circle_present: {value: "no", rationale: "God rules from outside the world.", certainty: 0.5, cites: [{source: S2, locator: "Mon. III.xvi.18"}], how_known: "Coder's reading."}
  reading: "As belief, not finding: scholastic form with a transcendent God."
  notes: ""

institutions: []
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 20"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Britannica gives birth as a range of dates and death as 13/14 September."
  open_questions:
    - "Read Convivio and Monarchia I.xii (free will) for B; date Monarchia."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Ricardo J. Quinones"
    citation: "Quinones, Ricardo J. \"Dante.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Dante-Alighieri."
    url: "https://www.britannica.com/biography/Dante-Alighieri"
    accessed: 2026-10-15
    reliability_note: "Signed article; the intro Q&A blocks are part of the article page and were used only for dates also in the body."
    used_for: [identity, basics, contribution, childhood, heritage, timing]
  - id: S2
    type: primary
    kind: "scholarly edition"
    author: "Dante Alighieri; ed. and trans. Prue Shaw"
    citation: "Dante Alighieri. Monarchia. Ed. and trans. Prue Shaw. Società Dantesca Italiana digital edition (2nd ed., 2019), Book III, ch. xvi."
    url: "https://www.danteonline.it/monarchia/index.php?c=English-III-xvi-16"
    accessed: 2026-10-15
    reliability_note: "Critical edition on the official site of the Società Dantesca Italiana."
    used_for: [worldview, timing, lane_b]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Dante Alighieri

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Dante (1265–1321), Florentine poet of La vita nuova (c. 1293) and the Commedia (c. 1308–21) [S1]. In Monarchia he sets two ends, reached by philosophy and by revelation [S2, III.xvi.8]. Draft: CHRIST 0.7; A 0 at 0.7; B BELOW_THRESHOLD (alternative 4); D 2 at 0.7; mid_basin BELOW_THRESHOLD.

## Life and work

Exiled from Florence in 1302; died at Ravenna [S1].

## Contribution and impact

Vita nuova; Commedia in the vernacular [S1].

## Childhood and education

Lesser nobility; met Beatrice at nine [S1].

## Adult working worldview

Two ends, two guides; God chooses the emperor through the preordained order of the heavens [S2].

## Heritage (context only)

Florentine [S1].

## Timing

First lasting contribution c. 1293, at about 28 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Scholastic form partly; no circle [S2].

## Open questions

- Convivio; Monarchia I.xii.

## Research log

- 2026-10-15: Read Britannica and Monarchia III.xvi (Shaw, Dante Online).
