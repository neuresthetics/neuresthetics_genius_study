---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch M)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-17
  last_updated: 2026-10-17
  change_log:
    - {date: 2026-10-17, by: "Grok Bot", summary: "Record created (stage 3 batch M, order P32: F 5, rank 82). Basics from Britannica (Sadie, signed; body text only, Q&A boxes not cited). Worldview from letters 69 (1777), 107, 108 and 110 (1778) in Lady Wallace's translation, Gutenberg #5307. primary_system CHRIST (0.7); A 0 (0.7); B BELOW_THRESHOLD (Providence about events in his life, not nature, P16); C 0 (0.5, alt 1); mid_basin BELOW_THRESHOLD. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-17, by: "Grok Bot", summary: "Batch M audit fixes (/workspace/genius_study_audit/gs_159d60d_M/run1/, run 1: 16 hold, 3 weaken): A 0 and CHRIST lowered from 0.7 to 0.5 (letters predate the working years, P20; Franklin precedent). Values and mid_basin unchanged."}

identity:
  id: mozart-wolfgang-amadeus
  display_name: "Wolfgang Amadeus Mozart"
  roster:
    canonical_name: "Wolfgang Amadeus Mozart"
    rank: 82
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: music
    field_bucket: music
  full_name: {value: "Johann Chrysostom Wolfgang Amadeus Mozart", certainty: 0.7, cites: [{source: S1, locator: "header ('In full'; baptized Johannes Chrysostomus Wolfgangus Theophilus Mozart)"}], how_known: "Britannica."}
  native_name: {value: UNKNOWN, how_known: "German in Latin script; he 'most commonly called himself Wolfgang Amadé or Wolfgang Gottlieb' (S1)."}
  aliases:
    - {name: "Mozart-Wolfgang Amadeus", kind: "roster alias"}
    - {name: "Wolfgang-Amadeus-Mozart", kind: "roster alias"}

basics:
  birth:
    date: {value: "1756-01-27", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Salzburg, archbishopric of Salzburg", modern_name: "Salzburg, Austria", polity_then: "Archbishopric of Salzburg (Holy Roman Empire)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1791-12-05", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening; 'The last year'"}], how_known: "Britannica."}
    place: {value: "Vienna", modern_name: "Vienna, Austria", polity_then: "Habsburg Monarchy (Holy Roman Empire)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1784, certainty: 0.5, cites: [{source: S1, locator: "'The central Viennese period'"}], how_known: "The 1784 piano concertos, with which 'he established a new level of piano concerto writing' (S1), are the earliest work the body text marks as lasting (P13). Die Entführung (1782) is dated but not marked as lasting; earlier works are described as accomplished, not lasting. 0.5 because the choice is the coder's."}
  era_bucket: {value: "1750 to 1849", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "From 1784 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Salzburg (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Salzburg and Vienna; tours of western Europe and Italy."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [German, Italian], certainty: 0.5, cites: [{source: S1, locator: "opera sections"}], how_known: "German singspiels and Italian operas (S1); letters in German. Coder's summary."}
  occupations: {value: ["composer", "pianist", "court Konzertmeister (Salzburg)"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'The Italian tours'"}], how_known: "Britannica."}

contribution:
  fields: {value: ["music composition"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Piano concertos of 1784", year: 1784, kind: work, lasting: "'he established a new level of piano concerto writing' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'The central Viennese period'"}], how_known: "Britannica."}
    - {value: "Le nozze di Figaro (K 492)", year: 1786, kind: work, lasting: "staged May 1, 1786, 'warmly received' and revived in 1789–90 (S1)", certainty: 0.7, cites: [{source: S1, locator: "'From Figaro to Don Giovanni'"}], how_known: "Britannica."}
    - {value: "Don Giovanni", year: 1787, kind: work, lasting: "given in Prague on October 29, 1787 (S1)", certainty: 0.7, cites: [{source: S1, locator: "'From Figaro to Don Giovanni'"}], how_known: "Britannica."}
    - {value: "Die Zauberflöte", year: 1791, kind: work, lasting: "'soon the opera became the most loved of all of Mozart's works for the stage' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'The last year'"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "Haydn in 1785: 'Your son is the greatest composer known to me in person or by name'", kind: "other", certainty: 0.7, cites: [{source: S1, locator: "'The central Viennese period'"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "'widely recognized as one of the greatest composers in the history of Western music' (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father Leopold Mozart, violinist, author of a violin manual, deputy Kapellmeister at the Salzburg court", role: father, certainty: 0.7, cites: [{source: S1, locator: "'Early life and works'"}], how_known: "Britannica."}
    - {value: "Mother Anna Maria Pertl, of a middle-class family in local administration", role: mother, certainty: 0.7, cites: [{source: S1, locator: "'Early life and works'"}], how_known: "Britannica."}
  household_circumstances: {value: TODO}
  schooling: []
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Leopold Mozart (father), music teacher", certainty: 0.7, cites: [{source: S1, locator: "'Early life and works'"}], how_known: "Britannica."}
  languages_in_childhood: {value: [German], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading (Salzburg)."}
  notable_events:
    - {value: "Family tour of western Europe as a child performer", year: 1763, age: 7, certainty: 0.7, cites: [{source: S1, locator: "'Early life and works'"}], how_known: "Britannica (mid-1763 to November 1766)."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1784–1791", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Freemasonry (from the end of 1784)", certainty: 0.7, cites: [{source: S1, locator: "'From Figaro to Don Giovanni'"}], how_known: "Britannica: 'Freemasonry, which he had embraced at the end of 1784'. A membership, not by itself a worldview code."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read on science."}
  primary_system:
    value: CHRIST
    basis: consistent_private_letters
    certainty: 0.5
    cites: [{source: S2, locator: "Gutenberg letter 69 (Augsburg, 25 Oct. 1777); Gutenberg letter 107 (Paris, 3 July 1778)"}]
    rationale: "Practising Catholic in the letters read: he 'told over my beads, as I had vowed', and praises 'good, true, upright' Germans who live 'a good Christian life' (Gutenberg letter 107). Named alternative: none chosen; Freemasonry from late 1784 (S1) is noted, but the 1787 letter on death that Britannica ties to Masonic teaching was not read."
    how_known: "Several private letters to his father, 1777–1778, before the working years (1784–1791), so 0.5 under P20, as for Franklin (pre-working-years evidence). Wallace translation (1865) of Nohl's collection via Gutenberg; web copy, 0.7 ceiling. TODO: map the Gutenberg (Wallace) letter numbers to a modern edition (Anderson or Bauer–Deutsch)."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Rosary, 'good Catholics', submission to 'the will of God'."}
    - {code: CLTHEI, reason: "A providential personal God; CHRIST is more specific."}
  lio_axes:
    A_locus:
      value: 0
      basis: consistent_private_letters
      certainty: 0.5
      cites: [{source: S2, locator: "Gutenberg letter 69 (25 Oct. 1777); Gutenberg letter 108 (9 July 1778)"}]
      how_known: "Consistent across several private letters (0.7 ceiling; web copy), but all from 1777–78, before the working years (1784–1791), so 0.5 under P20, as for Franklin; no later letter read. TODO: map the Gutenberg (Wallace) letter numbers to a modern edition (Anderson or Bauer–Deutsch)."
      rationale: "A personal God apart from the world who rules over persons: 'I have always God before my eyes, I acknowledge His omnipotence, I dread His wrath; but I also know His love, His compassion and mercy towards His creatures' (1777); 'remember that God Almighty has ordained it, and how can we rebel against Him?' (1778)."
    B_cause: {value: BELOW_THRESHOLD, how_known: "The Providence statements are about events in his own life (his mother's death: 'It was the manifest will of God; her time was come', Gutenberg letter 110; his plans: 'If it be His almighty will, it must come to pass', Gutenberg letter 107), not about the order of nature (P16), as for Beethoven. No statement on nature's laws read."}
    C_ledger:
      value: 0
      basis: consistent_private_letters
      certainty: 0.5
      cites: [{source: S2, locator: "Gutenberg letter 69; Gutenberg letter 107; Gutenberg letter 108"}]
      how_known: "Private letters; 0.5 because the wording is conventional piety and an alternative is named. TODO: map the Gutenberg (Wallace) letter numbers to a modern edition (Anderson or Bauer–Deutsch)."
      rationale: "Reward and punishment of persons: 'I dread His wrath' (1777); on Voltaire's death, 'This is his reward!' (1778); his mother 'in the enjoyment of heavenly bliss' (1778). Named alternative: 1."
    D_authority: {value: UNKNOWN, how_known: "Nothing read on revelation against observation."}
    E_scope: {value: UNKNOWN, how_known: "'He will never forsake His servants' (1777) is about his own life; not scored (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 0 at 0.7, but B is BELOW_THRESHOLD, so neither branch can be tested (P4, P10)."}
  statements:
    - text: "Do not be uneasy on my account, for I have always God before my eyes, I acknowledge His omnipotence, I dread His wrath; but I also know His love, His compassion and mercy towards His creatures, and that He will never forsake His servants."
      cites: [{source: S2, locator: "Gutenberg letter 69, Augsburg, Oct. 25, 1777"}]
      date: "1777-10-25"
      context: "To his father."
      axes: [A_locus, C_ledger]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-17
      note: "Lady Wallace's translation (1865) via Gutenberg #5307; checked word for word against the Gutenberg text; web copy, 0.7 cap. TODO: map the Gutenberg (Wallace) letter numbers to a modern edition (Anderson or Bauer–Deutsch)."
    - text: "I must give you a piece of intelligence that you perhaps already know--namely, that the ungodly arch-villain Voltaire has died miserably like a dog--just like a brute. This is his reward!"
      cites: [{source: S2, locator: "Gutenberg letter 107, Paris, July 3, 1778"}]
      date: "1778-07-03"
      context: "To his father, written the night his mother died."
      axes: [C_ledger]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-17
      note: "As above. TODO: map the Gutenberg (Wallace) letter numbers to a modern edition (Anderson or Bauer–Deutsch)."
    - text: "remember that God Almighty has ordained it, and how can we rebel against Him? Let us rather pray to Him and thank Him for His goodness, for she died a happy death."
      cites: [{source: S2, locator: "Gutenberg letter 108, Paris, July 9, 1778"}]
      date: "1778-07-09"
      context: "To his father, on his mother's death."
      axes: [A_locus, B_cause]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-17
      note: "As above. TODO: map the Gutenberg (Wallace) letter numbers to a modern edition (Anderson or Bauer–Deutsch)."
    - text: "In the first place, I must tell you that NOTHING could have saved my mother. No doctor in the world could have restored her to health. It was the manifest will of God; her time was come, and God chose to take her to Himself."
      cites: [{source: S2, locator: "Gutenberg letter 110, Paris, July 31, 1778"}]
      date: "1778-07-31"
      context: "To his father."
      axes: [B_cause]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-17
      note: "As above. TODO: map the Gutenberg (Wallace) letter numbers to a modern edition (Anderson or Bauer–Deutsch). About a death in his family, not nature's order (P16)."
  changes_over_life:
    - {value: "Joined Freemasonry at the end of 1784", year: 1784, age: 28, certainty: 0.7, cites: [{source: S1, locator: "'From Figaro to Don Giovanni'"}], how_known: "Britannica."}
  coder_notes: "Coder's call. All letters read are to his father Leopold, who was devout (S1), and predate the working years; the April 1787 letter on death ('this best and truest friend of mankind', reported by S1 as based on Masonic teaching) is in Wallace volume 2, which is not on Gutenberg, and was not read. B could move if a letter speaks of nature's order."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Salzburg German-speaking", certainty: 0.5, cites: [{source: S1, locator: "'Early life and works'"}], how_known: "Coder's reading."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1784–1791", certainty: 0.5, cites: [{source: S1, locator: "'The central Viennese period'; 'The last year'"}], how_known: "First to last listed lasting contribution (P29, P30); the start is the coder's pick (see first_lasting_contribution_year)."}
  age_at_first_lasting_contribution: {value: 28, certainty: 0.5, cites: [{source: S1, locator: "opening; 1784"}], how_known: "1784 − 1756 = 28 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No LIO-type view found."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "Gutenberg letters 69–110"}], how_known: "The letters read are providentialist. TODO: map the Gutenberg (Wallace) letter numbers to a modern edition (Anderson or Bauer–Deutsch)."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Letters read are from 1777–78; none from 1784–91 read."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Nothing read.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Nothing read."}
  circle_present: {value: "unclear", rationale: "God as ruler of his life, but nothing on God as source or end of an order.", certainty: 0.5, cites: [{source: S2, locator: "Gutenberg letter 69"}], how_known: "Coder's reading. TODO: map the Gutenberg (Wallace) letter numbers to a modern edition (Anderson or Bauer–Deutsch)."}
  reading: "Providentialist Catholic in the early letters."
  notes: ""

institutions:
  - {value: "Salzburg court (honorary Konzertmeister, 1769; salaried Konzertmeister)", role: musician, years: "1769–1781", kind: other, certainty: 0.7, cites: [{source: S1, locator: "'Early life and works'; 'Vienna: the early years'"}], how_known: "Britannica; discharge granted June 9, 1781."}
collaborators:
  - {value: "Lorenzo Da Ponte", relation: collaborator, note: "librettist of Figaro and Don Giovanni", certainty: 0.7, cites: [{source: S1, locator: "'From Figaro to Don Giovanni'"}], how_known: "Britannica."}
  - {value: "Emanuel Schikaneder", relation: collaborator, note: "Die Zauberflöte", certainty: 0.7, cites: [{source: S1, locator: "'The last year'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 82"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Letters read in a 19th-century translation (Wallace, from Nohl), not a modern critical edition."
  open_questions:
    - "Read the letter of 4 April 1787 (Wallace vol. 2 or Anderson) and later letters for the working years; look for any statement on nature for B."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Stanley Sadie"
    citation: "Sadie, Stanley. \"Wolfgang Amadeus Mozart.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Wolfgang-Amadeus-Mozart. Read live (first pages) and in Wayback snapshots: main page 2026-10-12 15:37:40 UTC; sections 'The Italian tours' 20260902024550, 'Mannheim and Paris' 20250918141441, 'Vienna: the early years' 20250911111426, 'The central Viennese period' 20261004215915, 'From Figaro to Don Giovanni' 20260307234235, 'The last year' 20260820031618, 'Mozart's place' 20250911120103."
    url: "https://www.britannica.com/biography/Wolfgang-Amadeus-Mozart"
    accessed: 2026-10-17
    reliability_note: "Signed article (Sadie, editor of The New Grove); byline agrees live and in Wayback. Body text only; Q&A boxes and Top Questions not cited."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: scholarly edition
    author: "Wolfgang Amadeus Mozart"
    citation: "Mozart, Wolfgang Amadeus. The Letters of Wolfgang Amadeus Mozart, vol. 1, trans. Lady Wallace from the collection of Ludwig Nohl (1865). Project Gutenberg eBook #5307. https://www.gutenberg.org/ebooks/5307."
    url: "https://www.gutenberg.org/ebooks/5307"
    accessed: 2026-10-17
    reliability_note: "19th-century translation, keyed text; letters numbered as in this edition."
    used_for: [worldview, timing, lane_b]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-17
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Wolfgang Amadeus Mozart

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Wolfgang Amadeus Mozart (1756–1791), Austrian composer [S1]. Draft: primary_system CHRIST (0.7); A 0 at 0.7; B BELOW_THRESHOLD (Providence about his life, not nature, P16); C 0 at 0.5; mid_basin BELOW_THRESHOLD. Not plotted.

## Life and work

Child prodigy taught by his father; Salzburg court; Vienna from 1781 [S1].

## Contribution and impact

Piano concertos of 1784; Figaro (1786), Don Giovanni (1787), Die Zauberflöte (1791) [S1].

## Childhood and education

Taught by Leopold Mozart; toured western Europe 1763–66 [S1].

## Adult working worldview

'I have always God before my eyes, I acknowledge His omnipotence, I dread His wrath' (1777) [S2]. Freemason from the end of 1784 [S1].

## Heritage (context only)

Salzburg family [S1].

## Timing

First lasting contribution 1784, at 28 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Unclear.

## Open questions

- Letters from the working years, including 4 April 1787.

## Research log

- 2026-10-17: Read Britannica (Sadie) live and in Wayback section snapshots; read Gutenberg #5307 (Wallace vol. 1) and searched it for God, Providence, will of God, Catholic; volume 2 not on Gutenberg.
