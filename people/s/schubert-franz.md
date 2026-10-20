---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z8)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z8 audit fixes (v8's calls on the auditor's advice). CHRIST 0.5 -> BELOW_THRESHOLD, lead CHRIST: one private letter, no backing scholar found (§3). S2 verified_against 'primary facsimile' -> 'scholarly edition' (Deutsch 1914 edited text). Symphony No. 9 (1828) had no in-life premiere or publication and no lasting source, so it moves to major_works (year UNKNOWN); span 1814–1828 -> 1814 (latest supported lasting work, Gretchen am Spinnrade). Age 17 unchanged. Not plotted."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z8, order P32: F 3, rank 169). Basics from Britannica (Maurice J. E. Brown, signed). Own words: letter to his father and stepmother, Steyr, 25 July 1825 (Deutsch, Die Dokumente seines Lebens und Schaffens II/1, 1914, no. 593, pp. 264–265; archive.org OCR of the Fraktur), within the span: wonder at 'meine Frömmigkeit' in the hymn to the Virgin (Ave Maria); he never 'forces' devotion, and composes such hymns only when 'unwillkürlich übermannt', 'dann aber ist sie auch gewöhnlich die rechte und wahre Andacht'; 'der Allmächtige sei gepriesen'. One private letter. Not a scientist. primary_system CHRIST (0.5, alt BELOW_THRESHOLD); A BELOW_THRESHOLD (set phrase, no locus view); B UNKNOWN; C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Span 1814–1828, age 17. Not plotted. Draft, not reviewed."}

identity:
  id: schubert-franz
  display_name: "Franz Schubert"
  roster:
    canonical_name: "Franz Schubert"
    rank: 169
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: "core"
    field: "music"
    field_bucket: "music"
  full_name: {value: "Franz Peter Schubert", certainty: 0.7, cites: [{source: S1, locator: "In full"}], how_known: "Britannica."}
  native_name: {value: "Franz Schubert", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  aliases:
    - {name: "Franz Peter Schubert", kind: "birth name"}

basics:
  birth:
    date: {value: "1797-01-31", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Himmelpfortgrund, near Vienna", modern_name: "Vienna, Austria", polity_then: "Habsburg Monarchy", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1828-11-19", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Vienna", modern_name: "Vienna, Austria", polity_then: "Austrian Empire", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1814, certainty: 0.7, cites: [{source: S1, locator: "Early life and career"}], how_known: "'Gretchen am Spinnrade', 19 October 1814: 'in this masterpiece he created at one stroke the German lied'."}
  era_bucket: {value: "1750 to 1849", certainty: 1.0, cites: [{source: S1, locator: "Early life and career"}], how_known: "1814 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Austria (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Vienna."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["German"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "German lieder."}
  occupations: {value: ["composer", "schoolmaster"], certainty: 0.7, cites: [{source: S1, locator: "Early life and career"}], how_known: "Britannica."}

contribution:
  fields: {value: ["music", "lied", "chamber music"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "The German lied ('Gretchen am Spinnrade')", year: 1814, kind: "work", lasting: "'in this masterpiece he created at one stroke the German lied (art song)' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Early life and career"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "Bridged the worlds of Classical and Romantic music", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Symphony No. 9 in C Major (The Great)", year: UNKNOWN, kind: "composition", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Britannica: 1828 (begun 1825), a completion date; no premiere or publication in his lifetime (P30 #1) and no source calling it lasting (P13), so not a lasting contribution and not the span end (Z8 audit)."}
    - {value: "Symphony in B Minor (Unfinished)", year: 1822, kind: "composition", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "Mass in C major", year: 1816, kind: "composition", certainty: 0.7, cites: [{source: S1, locator: "Early life and career"}], how_known: "Britannica."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Creator of the German lied (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Franz Theodor Schubert, schoolmaster", role: "father", certainty: 0.7, cites: [{source: S1, locator: "Early life and career"}], how_known: "Britannica."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Stadtkonvikt, Vienna (court chapel choir scholarship)", stage: "grammar or secondary school", years: "1808–1812", certainty: 0.7, cites: [{source: S1, locator: "Early life and career"}], how_known: "Britannica."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Antonio Salieri", certainty: 0.7, cites: [{source: S1, locator: "Early life and career"}], how_known: "Britannica."}
  languages_in_childhood: {value: ["German"], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Inferred."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1814", certainty: 0.5, cites: [{source: S1, locator: "Early life and career; opening"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "One private letter (25 July 1825; S2, no. 593, pp. 264–265) speaks of 'meine Frömmigkeit', 'die rechte und wahre Andacht' and 'der Allmächtige'. A single private letter with no scholar's backing cannot score (§3; Z8 audit, v8's call), so BELOW_THRESHOLD. Lead CHRIST (Catholic setting: court chapel choir, masses)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Lead: devotion in one private letter; no backing scholar found (§3)."}
    - {code: DEISM, reason: "Not supported: no statement against revelation read."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "'der Allmächtige sei gepriesen' (S2) is a set phrase of thanks; no locus view stated (P20)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); no statement on nature's order."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied."}
  statements:
    - text: "Auch wunderte man sich sehr über meine Frömmigkeit, die ich in einer Hymne an die heil. Jungfrau ausgedrückt habe, und, wie es scheint, alle Gemüther ergreift und zur Andacht stimmt. Ich glaube, das kommt daher, weil ich mich zur Andacht nie forcire, und, außer wenn ich von ihr unwillkürlich übermannt werde, nie dergleichen Hymnen oder Gebete componire, dann aber ist sie auch gewöhnlich die rechte und wahre Andacht."
      cites: [{source: S2, locator: "no. 593, pp. 264–265"}]
      date: "1825-07-25"
      context: "Letter to his father and stepmother from Steyr; within the span."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "Reconstructed from the archive.org OCR of the 1914 Fraktur printing; the page image was not viewed."
  changes_over_life: []
  coder_notes: "Check the page image of Deutsch 1914 pp. 264–265; read the 1824 diary and other letters; the omission of 'Et unam sanctam catholicam' in his mass settings is work, not profession (P16), and is only a lead."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated in the sources read (Catholic Vienna; not stated)."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1814", certainty: 0.5, cites: [{source: S1, locator: "Early life and career; opening"}], how_known: "Gretchen am Spinnrade (1814) is the only supported lasting work; the 1828 end had no dating event or lasting source (Z8 audit; P13, P30 #1), so the span is the latest supported lasting work, 1814 (P29)."}
  age_at_first_lasting_contribution: {value: 17, certainty: 0.7, cites: [{source: S1, locator: "opening; Early life and career"}], how_known: "1814 − 1797 = 17 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Music (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions: []
collaborators:
  - {value: "Johann Michael Vogl", relation: "collaborator", note: "baritone; sang his songs", certainty: 0.7, cites: [{source: S1, locator: "Early life and career"}], how_known: "Britannica."}
  - {value: "Franz von Schober", relation: "other", note: "host and patron", certainty: 0.7, cites: [{source: S1, locator: "Early life and career"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 169"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "One private letter only; read from OCR of a Fraktur printing."
  open_questions:
    - "Page-image check; diary and other letters."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Maurice J. E. Brown"
    citation: "Brown, Maurice J. E. 'Franz Schubert.' Encyclopaedia Britannica (rev. 2026). https://www.britannica.com/biography/Franz-Schubert"
    url: "https://www.britannica.com/biography/Franz-Schubert"
    accessed: 2026-10-19
    reliability_note: "Signed article; body cited, question boxes not used (P26)."
    used_for: [identity, basics, contribution, childhood, worldview, timing, lane_b, collaborators]
  - id: S2
    type: primary
    kind: "scholarly edition"
    author: "Otto Erich Deutsch (ed.)"
    citation: "Deutsch, Otto Erich (ed.). Franz Schubert: Die Dokumente seines Lebens und Schaffens, vol. II, part 1 (Munich: Georg Müller, 1914), no. 593, pp. 264–265. https://archive.org/details/franzschubertdie21deut"
    url: "https://archive.org/details/franzschubertdie21deut"
    accessed: 2026-10-19
    reliability_note: "Documentary edition of his letters; read in the archive.org OCR text."
    used_for: [worldview]
  - id: S3
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [review]
---

## Summary

Franz Schubert (1797–1828), composer [S1]. Primary BELOW_THRESHOLD (lead CHRIST); A BELOW_THRESHOLD; B UNKNOWN. Not plotted.

## Life and work

Vienna; Zseliz 1818 [S1].

## Contribution and impact

The German lied; symphonies, masses, chamber music [S1].

## Childhood and education

Schoolmaster's son; court choir and Stadtkonvikt; Salieri [S1].

## Adult working worldview

Devotion that comes unforced, in his 1825 letter [S2].

## Heritage (context only)

Not stated.

## Timing

1814, age 17 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Page-image check of the 1825 letter.

## Research log

- 2026-10-19: Read Britannica (Brown); Deutsch 1914 no. 593 (OCR).
