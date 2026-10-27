---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z6)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to visual_arts. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z7 audit notes: 1453 kept (installation; RQ-Z7-N1 now codifies unveiling or installation as the P30 #1 event for artworks). S3 note corrected: the Gattamelata article text was read."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z6 audit fixes (blind audit at 85859f0, run 1; Z6-40 FAIL, not result-changing): Gattamelata's lasting status and the span end re-cited from the question box (P26) to Britannica's 'Gattamelata' topic article (S3): 'established a prototype for equestrian monuments in the West'. Year 1453 kept as the public installation (P30 #1), completion 1447–1450 noted. Span 1415–1453, age 29 unchanged."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z6, order P32: F 3, rank 160). Source: Britannica (H. W. Janson, signed; opening and 'Early career' read). No own words on religion read; religious commissions are work, not profession (P16). Not a scientist. Span 1415–1453 (St. Mark and St. George, c. 1415; Gattamelata 1447–53). primary_system UNKNOWN (lead CHRIST); A, B, C, D, E UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #153, F3 rank 160). Needs: enrich sources; do not force plot from commissions. Dual bio Wikipedia EN (S4) + retained Britannica Janson (S1): birth c.1386 from catasto age claim; death 13 Dec 1466 Florence. Herzner Regesti donatelliani 1979 (S6): archival catasto age declarations (reg. 95: age 41 in 1427) and death date note (Bartolomeo Ponzio: 10 Dec 1466 at 76 — dual with Vasari/Britannica 13 Dec). Vasari Life of Donato, de Vere EN Gutenberg (S5): character anecdotes and burial at San Lorenzo near Cosimo 'as he had himself directed' — reported speech / second-hand (~100 years later); aesthetic 'ploughman' Crucifix exchange and 'By the faith that I place in my Zuccone' are art talk, not creed. No own-word religion in catasto summaries or Vasari. primary_system UNKNOWN (lead CHRIST only); A/B/C/D/E UNKNOWN; mid_basin UNKNOWN. P47 on S1–S6. Chart-moving NO. No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: donatello
  display_name: "Donatello"
  roster:
    canonical_name: "Donatello"
    rank: 160
    F: 3
    models: [Gemini, GPT, Grok]
    band: "core (3–4)"
    status: "core"
    field: "art"
    field_bucket: "arts"
  full_name: {value: "Donato di Niccolò di Betto Bardi", certainty: 0.7, cites: [{source: S1, locator: "Original name in full"}, {source: S4, locator: "lede"}], how_known: "Britannica and Wikipedia EN (dual-source)."}
  native_name: {value: "Donatello", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lede"}], how_known: "Diminutive of Donato (Britannica; Wikipedia)."}
  aliases:
    - {name: "Donato di Niccolò di Betto Bardi", kind: "birth name"}
    - {name: "Donato", kind: other}

basics:
  birth:
    date: {value: "1386", certainty: 0.7, cites: [{source: S1, locator: "Born"}, {source: S4, locator: "lede; Early life — catasto age 41 in July 1427"}, {source: S6, locator: "reg. 95 (1427): dichiara di avere 41 anni"}], how_known: "Britannica c. 1386; Wikipedia and Herzner archival catasto: he declared himself 41 in 1427 → c. 1386. Vasari's 1403 (S5) is superseded by the tax declaration. Certainty 0.7 (approximate year from age claim)."}
    place: {value: "Florence", modern_name: "Florence, Italy", polity_then: "Republic of Florence", certainty: 0.7, cites: [{source: S1, locator: "Born"}, {source: S4, locator: "lede"}], how_known: "Britannica and Wikipedia EN."}
  death:
    date: {value: "1466-12-13", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "Died"}, {source: S4, locator: "lede"}, {source: S5, locator: "Life of Donato — died December 13, 1466"}, {source: S6, locator: "reg. entry 1466-10 dicembre — Morte … secondo Bartolomeo Ponzio"}], how_known: "Britannica, Wikipedia, and Vasari give 13 December 1466; Herzner also registers Bartolomeo Ponzio's 10 December 1466 (age 76). Day 13 kept as the widely printed date; Ponzio noted (P25 dual). Julian."}
    place: {value: "Florence", modern_name: "Florence, Italy", polity_then: "Republic of Florence", certainty: 0.7, cites: [{source: S1, locator: "Died"}, {source: S4, locator: "lede"}, {source: S5, locator: "Via del Cocomero; buried S. Lorenzo"}], how_known: "Britannica, Wikipedia; Vasari places final illness in Florence and burial in San Lorenzo."}
  first_lasting_contribution_year: {value: 1415, certainty: 0.5, cites: [{source: S1, locator: "'Early career'"}, {source: S4, locator: "Early career — St. Mark / St. George"}], how_known: "St. Mark and St. George, both completed c. 1415: Britannica 'The full power of Donatello first appeared'; Wikipedia dual."}
  era_bucket: {value: "1400 to 1599", certainty: 1.0, cites: [{source: S1, locator: "'Early career'"}], how_known: "1415 (P2)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "Born"}], how_known: "Italy (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S4, locator: "lede — Rome, Padua, Siena"}], how_known: "Florence, Rome, Siena, Padua."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Italian", "Latin"], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Inferred (Latin inscriptions); no literary corpus of his own."}
  occupations: {value: ["sculptor"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lede"}], how_known: "Britannica and Wikipedia."}

contribution:
  primary_domain: visual_arts
  fields: {value: ["sculpture"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lede"}], how_known: "Britannica and Wikipedia."}
  lasting_original_contributions:
    - {value: "St. Mark and St. George, Orsanmichele", year: 1415, kind: work, lasting: "'for the first time since Classical antiquity ... the human body is rendered as a self-activating functional organism' (S1)", certainty: 0.5, cites: [{source: S1, locator: "'Early career'"}, {source: S4, locator: "Early career"}], how_known: "Britannica; Wikipedia dual; c. 1415."}
    - {value: "Schiacciato relief (St. George Killing the Dragon)", year: 1417, kind: method, lasting: "his 'bold new mode of relief' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Early career'"}], how_known: "Britannica: 1416–17."}
    - {value: "Gattamelata equestrian monument", year: 1453, kind: work, lasting: "'The statue established a prototype for equestrian monuments in the West' (S3)", certainty: 0.5, cites: [{source: S3, locator: "opening"}, {source: S4, locator: "Padua — Gattamelata"}], how_known: "Britannica 'Gattamelata' (S3): 'completed between 1447 and 1450 but was not installed on its pedestal ... until 1453'. Year 1453 = public installation, a single dated year (P30 #1), so P12's range rule does not apply; RQ-Z7-N1 (Z7 audit) codifies installation or unveiling as the dating event for artworks; the completion range 1447–1450 is noted (by P12 it would give item year 1447 and, as the period end, 1450 under P30 rule 4). Wikipedia dual."}
  evidence_of_impact:
    - {value: "One of the greatest of all Italian Renaissance artists", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lede"}], how_known: "Britannica; Wikipedia scholarly consensus framing."}
  major_works:
    - {value: "Feast of Herod (Siena font)", year: 1427, kind: artwork, certainty: 0.7, cites: [{source: S1, locator: "'Early career'"}, {source: S4, locator: "Siena"}], how_known: "Britannica: 1423–27; Wikipedia dual."}
    - {value: "Bronze David (Medici)", year: UNKNOWN, kind: artwork, certainty: 0.5, cites: [{source: S1, locator: "text"}, {source: S4, locator: "Florence — David"}], how_known: "Famous freestanding nude; dating debated — not used to end the span."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "One of the greatest Renaissance artists (S1, S4).", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lede"}], how_known: "Dual tertiary."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated; baptism record not read."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Niccolò di Betto Bardi, father, wool carder (tiratore di lana)", role: father, certainty: 0.7, cites: [{source: S1, locator: "'Early career'"}, {source: S4, locator: "Early life"}], how_known: "Britannica and Wikipedia."}
  household_circumstances: {value: "Humble origins (wool carder's son)", certainty: 0.7, cites: [{source: S1, locator: "'Early career'"}, {source: S4, locator: "Early life"}], how_known: "Britannica and Wikipedia."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Italian assumed; not sourced."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1415–1453", certainty: 0.5, cites: [{source: S1, locator: "'Early career'"}, {source: S3, locator: "opening"}, {source: S4, locator: "Early career; Padua — Gattamelata"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Florentine Catholic working milieu (church and civic commissions; San Lorenzo burial per Vasari)", role: member, certainty: 0.5, cites: [{source: S1, locator: "text — Orsanmichele, Duomo, S. Croce commissions"}, {source: S5, locator: "buried in the Church of S. Lorenzo, near the tomb of Cosimo, as he had himself directed"}, {source: S4, locator: "commissions overview"}], how_known: "Institutional/milieu membership and burial place — not a scored creed profession (P16)."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not a scientist; no science–religion remark."}
  primary_system: {value: UNKNOWN, how_known: "No own-word profession of CHRIST (or any other system). Checked and off-point: (1) religious commissions (S1, S4) = work, not profession (P16); (2) Vasari burial wish near Cosimo in San Lorenzo (S5) = patronage/loyalty report, second-hand; (3) Vasari 'ploughman' Crucifix exchange and 'By the faith that I place in my Zuccone' (S5) = aesthetic/art talk, reported speech; (4) catasto portate (S6) = tax/age/property, no creed language in the regesti read. CHRIST remains heritage/milieu lead only."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Lead only: Catholic Florence milieu, church commissions, San Lorenzo burial (S5). Not scored — no own-word redeeming/personal God statement (contrast Michelangelo sonnets)."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing in his words on locus of the divine (P19). Vasari reported speech (S5) and religious subjects in sculpture do not score A. Named alternative if a personal-God profession appears in unread letters/contracts: A 0."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30/P33). No statement of his own on nature's causal order (P16). Perspective/anatomy in the art is craft, not a B claim."}
    C_ledger: {value: UNKNOWN, how_known: "No own-word sin/grace/ledger statement. Penitent Magdalene is a commission subject, not his ledger profession."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read."}
    E_scope: {value: UNKNOWN, how_known: "Not a scientist; nothing read (P7/P19)."}
  mid_basin: {value: UNKNOWN, how_known: "A is UNKNOWN; UNKNOWN takes precedence (P19)."}
  statements:
    - text: "Donatello dichiara di avere 41 anni."
      cites: [{source: S6, locator: "reg. 95 — 1427, 7–11 aprile (Portata al Catasto)"}]
      date: "1427"
      context: "Florence catasto tax declaration; Herzner notes the portata was written by Michelozzo in the first person. Age claim → birth c. 1386 (S4/S6)."
      axes: []
      kind: "other"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Own-voice archival for age only — not a creed statement. Not used to score worldview."
    - text: "By the faith that I place in my Zuccone"
      cites: [{source: S5, locator: "Life of Donato — Campanile prophets / Il Zuccone"}]
      context: "Vasari reports Donatello's habitual oath when he wished to be believed, naming his Campanile statue Il Zuccone; also the 'Speak, speak' apostrophe while carving."
      axes: []
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Second-hand Vasari (~1550). Artistic oath about a statue, not a religious profession. Not used to score A or primary_system."
    - text: "it is thy work to make Christ and mine to make ploughmen."
      cites: [{source: S5, locator: "Life of Donato — wooden Crucifix / Brunelleschi anecdote"}]
      context: "Vasari anecdote: Brunelleschi criticizes Donatello's Crucifix as a 'ploughman' on the Cross; after seeing Brunelleschi's rival Crucifix, Donatello replies thus."
      axes: []
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Second-hand Vasari. Aesthetic self-deprecation, not theology. Not used to score worldview."
  changes_over_life: []
  coder_notes: "Deepen D1 2026-10-24 (queue #153): Hunt of Britannica, Wikipedia, Vasari (de Vere), and Herzner regesti found no own-word creed. Keep primary UNKNOWN / lead CHRIST; A–E UNKNOWN. Do not code from commissions (P16), San Lorenzo burial (Vasari), or popular-web 'agnostic' claims (donatello.net — unreliable; Vasari does not say that). Chart-moving NO. No fallacy_catalog (Jason)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Florentine", certainty: 0.7, cites: [{source: S1, locator: "Born"}, {source: S4, locator: "lede"}], how_known: "Britannica and Wikipedia."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Baptism/family religion not stated in sources read; Florence Catholic milieu is context only."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "No baptism record read."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1415–1453", certainty: 0.5, cites: [{source: S1, locator: "'Early career'"}, {source: S3, locator: "opening"}, {source: S4, locator: "Early career; Padua"}], how_known: "St. Mark and St. George (c. 1415) to the Gattamelata's installation in 1453 (S3; completed 1447–1450; P29, P30 #1)."}
  age_at_first_lasting_contribution: {value: 29, certainty: 0.5, cites: [{source: S1, locator: "Born; 'Early career'"}, {source: S4, locator: "birth c. 1386; Early career"}, {source: S6, locator: "reg. 95 age claim"}], how_known: "1415 − 1386 = 29 (P30 year difference); both years approximate."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None — Vasari and catasto checked off-point."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S5, locator: "Life of Donato"}, {source: S6, locator: "catasto regesti"}], how_known: "No scorable A/B own words in the working years from sources read."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Axes UNKNOWN."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Classical revival of the nude and schiacciato relief show geometric/proportional form in the sculpture (S1, S4) — form in the art, not a worldview score.", certainty: 0.5, cites: [{source: S1, locator: "'Early career'"}, {source: S4, locator: "lede"}], how_known: "Coder's reading of dual bio."}
  form_acquired: {value: UNKNOWN, how_known: "Training path (Ghiberti workshop) clear; H1 acquisition not tested."}
  circle_present: {value: "unclear", rationale: "No worldview statement that would feed H1 circle.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "Lane B only: geometric form present in the work; no H1 circle from worldview. Form ≠ A/B score."
  notes: "Do not treat religious subject matter or Vasari piety anecdotes as Lane A creed."

institutions: []
collaborators:
  - {value: "Lorenzo Ghiberti", relation: "mentor or employer", note: "workshop member 1404–07", certainty: 0.7, cites: [{source: S1, locator: "'Early career'"}, {source: S4, locator: "Early career"}], how_known: "Britannica and Wikipedia."}
  - {value: "Filippo Brunelleschi", relation: "rival or critic", note: "friends; Vasari Crucifix anecdote (S5)", certainty: 0.7, cites: [{source: S1, locator: "'Early career'"}, {source: S5, locator: "Crucifix anecdote"}], how_known: "Britannica; Vasari story is second-hand."}
  - {value: "Michelozzo", relation: collaborator, note: "partnership; wrote Donatello's 1427 catasto in first person (S6)", certainty: 0.7, cites: [{source: S1, locator: "'Early career'"}, {source: S6, locator: "Portata al Catasto di Donatello, scritta da Michelozzo"}], how_known: "Britannica and Herzner."}
  - {value: "Cosimo de' Medici", relation: other, note: "patron; lifelong Medici support; Vasari burial near Cosimo", certainty: 0.7, cites: [{source: S4, locator: "Working and personal life"}, {source: S5, locator: "burial near Cosimo"}], how_known: "Wikipedia; Vasari."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 160"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "No own-voice creed text found; worldview stays UNKNOWN."
    - "Vasari is second-hand (~1550); character anecdotes are reported speech only."
    - "Death day: Vasari/Britannica/Wikipedia 13 Dec 1466 vs Herzner/Ponzio 10 Dec 1466 — day 13 kept, Ponzio noted."
    - "Popular site donatello.net 'agnostic' claim ignored (not a scholarly source; Vasari does not say that)."
  open_questions:
    - "Unread full ASFi catasto transcriptions / any private letter with religious language beyond Herzner regesti summaries."
    - "Any notarized will or inter vivos donation text with creed clauses (1460 property donation reported in secondary press; full ASFi text unread this pass)."
    - "Coonin monograph pages behind Wikipedia's catasto cite (Herzner reg. 95 already duals the age claim)."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "H. W. Janson"
    citation: "Janson, H. W. 'Donatello.' Encyclopaedia Britannica. https://www.britannica.com/biography/Donatello"
    url: "https://www.britannica.com/biography/Donatello"
    accessed: 2026-10-19
    reliability_note: "Signed article; body cited, question boxes flagged (P26). Re-opened 2026-10-24: 'little is known about his character and personality'."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, collaborators]
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
    author: "The Editors of Encyclopaedia Britannica (revised by Kathleen Kuiper)"
    citation: "'Gattamelata.' Encyclopaedia Britannica. https://www.britannica.com/topic/Gattamelata"
    url: "https://www.britannica.com/topic/Gattamelata"
    accessed: 2026-10-19
    reliability_note: "Topic article body, read (opening; same text on Britannica's scholars edition); not a question box."
    source_quality: "reference entry"
    used_for: [contribution, timing]
  - id: S4
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "Wikipedia. 'Donatello.' https://en.wikipedia.org/wiki/Donatello"
    url: "https://en.wikipedia.org/wiki/Donatello"
    accessed: 2026-10-24
    reliability_note: "P50 dual bio with Britannica. Catasto age claim cited to Coonin; cross-checked against Herzner (S6)."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, collaborators, review]
  - id: S5
    type: secondary
    kind: "other"
    author: "Giorgio Vasari (tr. Gaston du C. de Vere)"
    citation: "Vasari, Giorgio. 'Life of Donato [Donatello].' In Lives of the Most Eminent Painters Sculptors and Architects, tr. Gaston du C. de Vere. Project Gutenberg #25759. https://www.gutenberg.org/files/25759/25759-h/25759-h.htm"
    url: "https://www.gutenberg.org/files/25759/25759-h/25759-h.htm"
    accessed: 2026-10-24
    reliability_note: "Written ~1550, ~84 years after death. Character anecdotes and burial wish are reported speech / second-hand — cannot score worldview alone. Birth year 1403 in Vasari is wrong vs catasto."
    source_quality: "unofficial web copy"
    used_for: [basics, worldview, timing, collaborators, review]
  - id: S6
    type: secondary
    kind: "scholarly edition"
    author: "Volker Herzner"
    citation: "Herzner, Volker. 'Regesti donatelliani.' Rivista dell'Istituto Nazionale d'Archeologia e Storia dell'Arte, s. III (1979): 169–228. PDF: https://www.inasaroma.org/patrimonio/wp-content/uploads/2018/02/Herzner-Regesti-donatelliani-RIASA-1979.pdf"
    url: "https://www.inasaroma.org/patrimonio/wp-content/uploads/2018/02/Herzner-Regesti-donatelliani-RIASA-1979.pdf"
    accessed: 2026-10-24
    reliability_note: "Scholarly regesti of archival documents (ASFi catasto, Opera del Duomo, etc.). Age declarations and death-date note used; no creed language found in entries skimmed."
    source_quality: "scholarly edition or monograph"
    used_for: [basics, worldview, timing, collaborators, review]
---

## Summary

Donatello (c. 1386–1466), Florentine sculptor [S1; S4]. Deepen D1: still no own-word creed — primary_system UNKNOWN (lead CHRIST); A–E UNKNOWN; mid_basin UNKNOWN. Not plotted.

## Life and work

Born Florence c. 1386 (catasto age claim, S4/S6); died Florence 13 Dec 1466 (S1/S4/S5; Ponzio 10 Dec noted in S6). Worked Florence, Rome, Siena, Padua [S1; S4]. Vasari: buried San Lorenzo near Cosimo [S5].

## Contribution and impact

St. Mark, St. George, schiacciato, David, Gattamelata [S1; S3; S4].

## Childhood and education

Wool carder's son; Ghiberti's workshop [S1; S4].

## Adult working worldview

No own words on religion found. Religious commissions = work (P16). Vasari anecdotes = second-hand art talk. Catasto = tax/age only. All LIO axes UNKNOWN; CHRIST lead only.

## Heritage (context only)

Florentine [S1; S4]. Family religion UNKNOWN (baptism unread).

## Timing

1415–1453, age 29 [S1; S3; S4].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Geometric form in the sculpture; no H1 circle from worldview.

## Open questions

- Full ASFi catasto / letter / donation texts for any creed clause.
- Coonin pages behind Wikipedia's catasto cite (Herzner already duals age).

## Research log

- 2026-10-19: Read Britannica (Janson), opening and 'Early career'.
- 2026-10-19: Z6 audit fixes: Gattamelata re-cited to Britannica's topic article.
- 2026-10-24: Deepen D1 — Wikipedia EN dual bio; Vasari de Vere Life of Donato (Gutenberg #25759); Herzner Regesti 1979 PDF (catasto age; death-date dual). Met Heilbrunn 429 this pass. No fallacy_catalog. No figures/.
