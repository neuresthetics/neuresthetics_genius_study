---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z8; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 19c. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #161, F3 rank 169). Hunt: Deutsch 1914 page images of no. 593 pp. 264–265 (Allmächtige / Frömmigkeit / Andacht confirmed; S2 verified_against page image); lost diary March 1824 nos. 469–472 (Glaube/Verstand epistemic; Fantasie vs Aufklärung; not locus, not P16 nature); Mein Traum 3 July 1822 no. 330 (allegory); Savile EN Letters 1928 (S4) cross-check; Wikipedia EN S5 baptism (P50 dual-bio with S1 parish/court chapel); Moon 2013 D.M. and Harnoncourt NPR skimmed as contested secondary — no clean §3 scholar backing to lift CHRIST/A from the one private letter. primary_system stays BELOW_THRESHOLD (lead CHRIST); A stays BELOW_THRESHOLD; B stays UNKNOWN (diary faith ≠ cause-order); mid BELOW; not plotted. Span still 1814; 1825 letter after span, counts under P31 (no changes_over_life). Mass 'Et unam sanctam' omission remains P16 work not profession. P47 source_quality on S1–S5. No fallacy_catalog; figures/ untouched. Draft, not reviewed."}
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
    date: {value: "1797-01-31", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "Early life"}], how_known: "Britannica; Wikipedia."}
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
  era_bucket: 19c
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
  family_religion: {value: "Catholic", certainty: 0.7, cites: [{source: S5, locator: "Early life"}, {source: S1, locator: "Early life and career"}], how_known: "Baptized in the Catholic Church the day after birth (S5); parish-church organist instruction and imperial court chapel choir (S1). Heritage only."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated beyond baptism and parish/chapel training."}
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
  primary_system: {value: BELOW_THRESHOLD, how_known: "One private letter (25 July 1825; S2 no. 593) speaks of 'meine Frömmigkeit', involuntary Andacht, and 'der Allmächtige' (page image confirmed). Lost diary March 1824 (S2 nos. 469–472; S4 EN) treats Glaube as epistemic prior to Verstand, not a Christian confession. Mein Traum (S2 no. 330) is allegory. Secondary debate continues (Moon 2013 D.M. leans on Huttenbrenner reported speech; Harnoncourt vs Mass-omission camp) — not clean §3 scholar backing to score CHRIST at 0.5. Lead CHRIST (Catholic setting: baptism, court chapel, masses). Mass 'Et unam sanctam' omission is work not profession (P16)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Lead: devotion in one private letter; Catholic heritage and masses; no clean §3 scholar backing after D1."}
    - {code: DEISM, reason: "Not supported: no statement against revelation read."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "'der Allmächtige sei gepriesen' (S2, page image) is a set phrase of thanks for health; Frömmigkeit/Andacht concerns composing a Marian hymn when involuntarily overcome — artistic devotion, no locus view stated (P20). Diary Glaube (1824) is epistemic, not where God is."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30). Diary Glaube/Verstand and anti-Aufklärung Fantasie praise are about belief and imagination, not nature's causal order (P16). No cause-order statement read."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied."}
  statements:
    - text: "Auch wunderte man sich sehr über meine Frömmigkeit, die ich in einer Hymne an die heil. Jungfrau ausgedrückt habe, und, wie es scheint, alle Gemüther ergreift und zur Andacht stimmt. Ich glaube, das kommt daher, weil ich mich zur Andacht nie forcire, und, außer wenn ich von ihr unwillkürlich übermannt werde, nie dergleichen Hymnen oder Gebete componire, dann aber ist sie auch gewöhnlich die rechte und wahre Andacht."
      cites: [{source: S2, locator: "no. 593, pp. 264–265"}]
      date: "1825-07-25"
      context: "Letter to his father and stepmother from Steyr; after the 1814 working span (P31 adult evidence; no changes_over_life). Savile EN (S4): 'my piety' / 'involuntarily overcome by a sense of devotion'."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Verified against archive.org PDF page images of the Deutsch 1914 Fraktur scholarly edition (print pp. 264–265); confirms Allmächtige / Frömmigkeit / Andacht / heil. Jungfrau. Same letter also: 'zu dem ich, der Allmächtige sei gepriesen, auch das meinige hinzufügen kann' (set-phrase thanks for health)."
    - text: "Man comes into the world armed with faith, which is far superior to knowledge and understanding: for in order to understand a thing one must first of all believe in it. Faith is that high fundament in which the weaker intellect erects the first pillars of conviction. Reason is nothing more than analysed belief."
      cites: [{source: S4, locator: "From his lost diary, 28 March 1824"}, {source: S2, locator: "nos. 469–472, pp. 199–201"}]
      date: "1824-03-28"
      context: "Lost diary entries March 1824 (Deutsch nos. 469–472). German: 'Auf dem Glauben tritt der Mensch in die Welt… Verstand ist nichts als ein analysierter Glaube.' Adjacent 29 March praises Fantasie against 'sogenannten Aufklärung'. Epistemic / anti-Enlightenment, not a Christian locus or nature-order claim."
      axes: []
      kind: "notebook or diary"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Not scored on A or B: Glaube here is epistemic prior to Verstand, not God-locus (P20) and not nature's law vs exception (P16)."
    - text: "I went forward, however, slowly and devoutly, with my eyes lowered towards the gravestone, and before I knew it I was in the circle, from which the loveliest melody sounded. And I felt, pressed as it were into a moment's space, the whole measure of eternal bliss. My father I saw too, loving and reconciled."
      cites: [{source: S4, locator: "My Dream, 3 July 1822"}, {source: S2, locator: "no. 330, pp. 134–135"}]
      date: "1822-07-03"
      context: "Allegorical prose 'Mein Traum' (Deutsch no. 330). German: innen Andacht und fester Glaube; ewige Seligkeit. Literary allegory of father-reconciliation and song, not a doctrinal profession."
      axes: []
      kind: "unpublished manuscript"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Not scored: allegory, not worldview code evidence."
  changes_over_life: []
  coder_notes: "D1 done: Deutsch 1914 page image of no. 593; 1824 diary and Mein Traum read (S2/S4); Wikipedia baptism (S5). Mass 'Et unam sanctam' omission remains work not profession (P16). Contested secondary (Moon 2013; Harnoncourt NPR) does not lift CHRIST/A under §3. Do not force plot without B."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: "Catholic", certainty: 0.7, cites: [{source: S5, locator: "Early life"}, {source: S1, locator: "Early life and career"}], how_known: "Baptized in the Catholic Church the following day (S5); parish church and imperial court chapel choir (S1). Heritage only — not a worldview code."}
  baptism_or_initiation: {value: "Baptized in the Catholic Church the day after birth (1 February 1797)", certainty: 0.7, cites: [{source: S5, locator: "Early life"}], how_known: "Wikipedia EN (revid 1381384316). Dual-bio: S1 parish/court chapel."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1814", certainty: 0.5, cites: [{source: S1, locator: "Early life and career; opening"}], how_known: "Gretchen am Spinnrade (1814) is the only supported lasting work; the 1828 end had no dating event or lasting source (Z8 audit; P13, P30 #1), so the span is the latest supported lasting work, 1814 (P29)."}
  age_at_first_lasting_contribution: {value: 17, certainty: 0.7, cites: [{source: S1, locator: "opening; Early life and career"}], how_known: "1814 − 1797 = 17 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None scored; 1825 letter and 1824 diary remain below threshold / off-axis."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None scored for the 1814 span."}

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
    - "One private letter for CHRIST lead; page image now checked (D1)."
    - "1824 diary and Mein Traum read; neither lifts A or opens B."
  open_questions:
    - "Further letters beyond Deutsch II/1 and Savile 1928 (e.g. Deutsch Dokumente later ed.) for any locus or nature-order own words."
    - "Peer-reviewed monograph on Schubert's religion that would count as §3 scholar backing (Moon 2013 D.M. and Harnoncourt interview are contested / reported-speech leaning, not used to score)."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Maurice J. E. Brown"
    citation: "Brown, Maurice J. E. 'Franz Schubert.' Encyclopaedia Britannica (rev. 2026). https://www.britannica.com/biography/Franz-Schubert"
    url: "https://www.britannica.com/biography/Franz-Schubert"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Signed article; body cited, question boxes not used (P26). Re-fetched 2026-10-24."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, collaborators]
  - id: S2
    type: primary
    kind: "scholarly edition"
    author: "Otto Erich Deutsch (ed.)"
    citation: "Deutsch, Otto Erich (ed.). Franz Schubert: Die Dokumente seines Lebens und Schaffens, vol. II, part 1 (Munich: Georg Müller, 1914), no. 593, pp. 264–265; also nos. 330 (Mein Traum), 469–472 (lost diary March 1824). https://archive.org/details/franzschubertdie21deut"
    url: "https://archive.org/details/franzschubertdie21deut"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Documentary edition. Letter 593 verified against archive.org PDF page images of print pp. 264–265 (D1). Diary and Mein Traum from the same volume (OCR + layout extract)."
    used_for: [worldview]
  - id: S3
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [review]
  - id: S4
    type: primary
    kind: "scholarly edition"
    author: "Otto Erich Deutsch (ed.); Venetia Savile (trans.)"
    citation: "Deutsch, Otto Erich (ed.); Savile, Venetia (trans.). Franz Schubert's Letters and Other Writings (London: Faber & Gwyer, 1928; Greenwood reprint 1970). Diary 25–29 March 1824; My Dream 3 July 1822; letter Steyr 25 July 1825. https://archive.org/details/bwb_Y0-BEA-509"
    url: "https://archive.org/details/bwb_Y0-BEA-509"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "English translation of Deutsch documents; used to cross-check diary and Mein Traum. Letter 593 EN softens 'Allmächtige' to 'God be praised' — German page image (S2) controls."
    used_for: [worldview]
  - id: S5
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "Wikipedia. 'Franz Schubert.' EN revid 1381384316 (2026-10-22). https://en.wikipedia.org/wiki/Franz_Schubert"
    url: "https://en.wikipedia.org/wiki/Franz_Schubert"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "P50 dual-bio with Britannica (S1) for baptism / Catholic heritage only. Not used for worldview scores."
    used_for: [basics, childhood, heritage]
---

## Summary

Franz Schubert (1797–1828), composer [S1]. Primary BELOW_THRESHOLD (lead CHRIST); A BELOW_THRESHOLD; B UNKNOWN. Not plotted. D1: page image and diary confirm hunt; scores unchanged.

## Life and work

Vienna; Zseliz 1818 [S1].

## Contribution and impact

The German lied; symphonies, masses, chamber music [S1].

## Childhood and education

Schoolmaster's son; Catholic baptism; court choir and Stadtkonvikt; Salieri [S1, S5].

## Adult working worldview

1825 letter: unforced Frömmigkeit when composing a Marian hymn; Allmächtige set phrase [S2]. 1824 diary: Glaube as epistemic prior to Verstand — not scored on A/B [S2, S4]. Mein Traum allegory — not scored [S2, S4]. No clean §3 scholar backing to lift CHRIST.

## Heritage (context only)

Catholic by baptism and parish/chapel upbringing [S5, S1]. Not a worldview code.

## Timing

1814, age 17 [S1]. Own-words evidence 1822–1825 is after the span; counts under P31 with no documented change of view.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Further letters / peer-reviewed religion monograph for §3 backing or any B cause-order statement.

## Research log

- 2026-10-19: Read Britannica (Brown); Deutsch 1914 no. 593 (OCR).
- 2026-10-24 (D1): Deutsch 1914 page images of no. 593; diary nos. 469–472; Mein Traum no. 330; Savile 1928 EN; Wikipedia baptism; Moon 2013 / Harnoncourt NPR skimmed (not scored). Scores unchanged. Chart-moving NO.
