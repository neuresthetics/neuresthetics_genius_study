---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch M)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-17
  last_updated: 2026-10-17
  change_log:
    - {date: 2026-10-17, by: "Grok Bot", summary: "Record created (stage 3 batch M, order P32: F 5, rank 81). Basics from Britannica (John Russell Brown, Terence Spencer and others, signed; Wayback copies; body only). No worldview statement in his own voice was read: the plays and poems are character or persona speech (P42), and the will's religious preamble was not read. All worldview fields UNKNOWN; mid_basin UNKNOWN (P19). Not plotted. Draft, not reviewed."}
    - {date: 2026-10-17, by: "Grok Bot", summary: "Batch M audit fixes (/workspace/genius_study_audit/gs_159d60d_M/run1/, run 1: 16 hold, 3 weaken): will read (Folger, PROB 1/4); by v8's ruling on RQ1 (on the auditor's advice) its formulaic preamble is lawyer drafting, not his statement (P42); 'only merits of Jesus Christ' recorded under nominal_affiliations as context. A stays UNKNOWN."}
    - {date: 2026-10-17, by: "Grok Bot", summary: "Batch N audit fix (#4): primary_system how_known no longer says the will was not read; it now says the will is read (S3)."}

identity:
  id: shakespeare-william
  display_name: "William Shakespeare"
  roster:
    canonical_name: "William Shakespeare"
    rank: 81
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: literature
    field_bucket: literature
  full_name: {value: "William Shakespeare", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  native_name: {value: UNKNOWN, how_known: "English."}
  aliases:
    - {name: "Shakespeare-William", kind: "roster alias"}
    - {name: "William-Shakespeare", kind: "roster alias"}

basics:
  birth:
    date: {value: "1564-04-26", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening; 'Early life in Stratford'"}], how_known: "Baptism date from the Holy Trinity parish register (S1); the birth date itself is unknown ('his birthday is traditionally celebrated on April 23'). Recorded as the baptism date."}
    place: {value: "Stratford-upon-Avon, Warwickshire, England", modern_name: "Stratford-upon-Avon, United Kingdom", polity_then: "Kingdom of England", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1616-04-23", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening; 'Career in the theatre'"}], how_known: "Britannica."}
    place: {value: "Stratford-upon-Avon, Warwickshire, England", modern_name: "Stratford-upon-Avon, United Kingdom", polity_then: "Kingdom of England", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1589, approx: true, certainty: 0.5, cites: [{source: S1, locator: "'Chronology of Shakespeare's plays'"}], how_known: "Henry VI, Part 1 and Titus Andronicus are dated 1589–92 (S1); a range counts from its start year (P12, P13). Love's Labour's Lost (1588–97) is not listed as lasting here because its range is too wide to place it. 'The first reference to Shakespeare in the literary world of London comes in 1592' (S1). 0.5."}
  era_bucket: {value: "1400 to 1599", certainty: 0.5, cites: [{source: S1, locator: "chronology"}], how_known: "From 1589 (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "England (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "London and Stratford."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [English], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  occupations: {value: ["dramatist", "poet", "actor"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["drama", "poetry"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Henry VI, Part 1; Titus Andronicus", year: 1589, kind: work, lasting: "earliest plays in the chronology (1589–92) (S1)", certainty: 0.5, cites: [{source: S1, locator: "'Chronology of Shakespeare's plays'"}], how_known: "Britannica table, 1589–92; start year (P12)."}
    - {value: "Hamlet", year: 1599, kind: work, lasting: "(S1)", certainty: 0.5, cites: [{source: S1, locator: "'Chronology of Shakespeare's plays'"}], how_known: "Dated 1599–1601 in the table; start year (P12)."}
    - {value: "King Lear", year: 1605, kind: work, lasting: "(S1)", certainty: 0.5, cites: [{source: S1, locator: "'Chronology of Shakespeare's plays'"}], how_known: "Dated 1605–06; start year (P12)."}
    - {value: "The Tempest", year: 1611, kind: work, lasting: "(S1)", certainty: 0.7, cites: [{source: S1, locator: "'Chronology of Shakespeare's plays'"}], how_known: "Dated 1611."}
    - {value: "Henry VIII", year: 1613, kind: work, lasting: "last play listed (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Chronology of Shakespeare's plays'"}], how_known: "Dated 1613."}
  evidence_of_impact:
    - {value: "'often called the English national poet'; plays 'performed and read more often and in more countries than ever before'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "'considered by many to be the greatest dramatist of all time' (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father John Shakespeare, burgess, alderman (1565) and bailiff (1568) of Stratford, in trade", role: father, certainty: 0.7, cites: [{source: S1, locator: "'Early life in Stratford'"}], how_known: "Britannica."}
    - {value: "Mother Mary Arden of Wilmcote, heiress to some land", role: mother, certainty: 0.7, cites: [{source: S1, locator: "'Early life in Stratford'"}], how_known: "Britannica."}
  household_circumstances: {value: TODO}
  schooling:
    - {value: "Stratford grammar school (presumed; no pupil lists survive)", stage: "grammar or secondary school", run_by: "state or municipal", certainty: 0.5, cites: [{source: S1, locator: "'Early life in Stratford'"}], how_known: "Britannica: 'it would be absurd to suppose the bailiff of the town did not send his son there'; the master was paid by the borough."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [English], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "Marriage licence bond with Anne Hathaway", year: 1582, age: 18, certainty: 0.7, cites: [{source: S1, locator: "'Early life in Stratford'"}], how_known: "Bond dated November 28, 1582 (S1)."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1589–1613", certainty: 0.5, cites: [{source: S1, locator: "'Chronology of Shakespeare's plays'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Baptized at Holy Trinity Church, Stratford-upon-Avon (Church of England)", certainty: 0.5, cites: [{source: S1, locator: "'Early life in Stratford'"}], how_known: "Britannica names the parish register; 'Church of England' is the coder's reading of the parish. Context, not a code."}
    - {value: "Will (25 March 1616) commends his soul 'into the hands of God my creator, hoping and assuredly believing through the only merits of Jesus Christ my Saviour to be made partaker of life everlasting' (a Protestant formula)", certainty: 0.5, cites: [{source: S3, locator: "modernized transcription; description"}], how_known: "Context only, not his own statement: v8's ruling on RQ1 (on the auditor's advice) (batch M audit), recorded in OPEN_DECISIONS P42: a formulaic will preamble is lawyer drafting (Francis Collins is named as a creator of the document; Folger calls the preamble 'very formulaic'). 'Protestant formula' is the coder's reading of 'only merits'."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing in his own voice read."}
  primary_system: {value: UNKNOWN, how_known: "The surviving record is 'mostly gleaned from documents of an official character' (S1). Speeches in the plays are characters' and the Sonnets' speaker is a persona, so neither is attributed to him (P42). The will (1616) is now read (S3); its preamble is formulaic lawyer drafting and is context only (P42, v8's pick on RQ1 of the batch M audit, on the auditor's advice); see nominal_affiliations."}
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Baptized in the parish church; nothing in his own voice read."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing attributable read (P42)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist; nothing attributable read on nature (P16, P42)."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing attributable read."}
    D_authority: {value: UNKNOWN, how_known: "Nothing attributable read."}
    E_scope: {value: UNKNOWN, how_known: "Nothing attributable read (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "A and B are UNKNOWN (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Coder's call. The will's preamble is read (S3) and, by v8's ruling on RQ1 (on the auditor's advice) (P42), is lawyer drafting, not his statement; it is recorded under nominal_affiliations as context and A stays UNKNOWN."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: "Baptized at Holy Trinity Church, Stratford-upon-Avon, April 26, 1564", certainty: 0.7, cites: [{source: S1, locator: "'Early life in Stratford'"}], how_known: "Parish register, per Britannica."}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1589–1613", certainty: 0.5, cites: [{source: S1, locator: "'Chronology of Shakespeare's plays'"}], how_known: "First to last listed lasting contribution (P29, P30); ranges counted from their start years (P12)."}
  age_at_first_lasting_contribution: {value: 25, certainty: 0.5, cites: [{source: S1, locator: "opening; chronology"}], how_known: "1589 − 1564 = 25 (P30), from the baptism year."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "Nothing attributable read."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Nothing attributable read."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Nothing attributable read."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Nothing read.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Nothing read."}
  circle_present: {value: "unclear", rationale: "Nothing attributable read.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No reading possible."
  notes: ""

institutions:
  - {value: "Lord Chamberlain's Men (King's Men from 1603)", role: member, years: "c. 1594–1613", kind: other, certainty: 0.7, cites: [{source: S1, locator: "'Career in the theatre'"}], how_known: "Britannica: 'from roughly 1594 onward'."}
collaborators:
  - {value: "Richard Burbage", relation: collaborator, note: "lead actor of the company", certainty: 0.7, cites: [{source: S1, locator: "'Career in the theatre'"}], how_known: "Britannica."}
  - {value: "John Heminge and Henry Condell", relation: collaborator, note: "fellow actors who collected the First Folio (1623)", certainty: 0.7, cites: [{source: S1, locator: "'Career in the theatre'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 81"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "No document in his own voice on religion is known to the sources read."
  open_questions:
    - "Settled (RQ1, P42): the will's formulaic preamble is not his own statement."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "John Russell Brown, Terence John Bew Spencer and others"
    citation: "Brown, John Russell, Terence John Bew Spencer et al. \"William Shakespeare.\" Encyclopaedia Britannica. https://www.britannica.com/biography/William-Shakespeare. Read in Wayback snapshots: main page 2025-12-19 16:25:14 UTC; 'Career in the theatre' 20260902004320; 'Chronology of Shakespeare's plays' 20260829053559; 'Early posthumous documentation' 20260815145150."
    url: "https://www.britannica.com/biography/William-Shakespeare"
    accessed: 2026-10-17
    reliability_note: "Signed, multi-author article (JSON-LD lists John Russell Brown; the chronology page byline begins Terence John Bew Spencer). Newest 2026 snapshot of the main page was a bot-check page, so the December 2025 copy was used. Live page timed out from the fetch tool. Body only; Top Questions not cited."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-17
    reliability_note: "Study's own roster."
    used_for: [identity, review]
  - id: S3
    type: primary
    kind: "archive record"
    author: "Folger Shakespeare Library (Shakespeare Documented)"
    citation: "\"Shakespeare's last will and testament: made 25 March 1616, proved 22 June 1616.\" Shakespeare Documented, Folger Shakespeare Library. The National Archives, Kew, PROB 1/4. doi:10.37078/110. https://shakespearedocumented.folger.edu/resource/document/william-shakespeares-last-will-and-testament-original-copy-including-three"
    url: "https://shakespearedocumented.folger.edu/resource/document/william-shakespeares-last-will-and-testament-original-copy-including-three"
    accessed: 2026-10-17
    reliability_note: "Folger's description and modernized transcription of the original will, read directly; creator listed as 'Francis Collins, esq. et al.; William Shakespeare'."
    used_for: [worldview]
---

# William Shakespeare

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

William Shakespeare (1564–1616), English dramatist and poet [S1]. Nothing in his own voice on religion was read. Draft: all worldview fields UNKNOWN; mid_basin UNKNOWN. Not plotted.

## Life and work

Stratford; London with the Lord Chamberlain's Men from about 1594; New Place bought 1597 [S1].

## Contribution and impact

Plays dated 1589–1613 [S1].

## Childhood and education

Son of John Shakespeare and Mary Arden; Stratford grammar school presumed [S1].

## Adult working worldview

Unknown [S1].

## Heritage (context only)

English; baptized at Holy Trinity, Stratford [S1].

## Timing

First lasting contribution about 1589, at 25 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Unclear.

## Open questions

- Settled: the will's preamble is context only (P42).

## Research log

- 2026-10-17: Read Britannica (Brown, Spencer et al.) in Wayback copies; live page and newest snapshot not available.
- 2026-10-17 (batch M audit fixes): read the will on Shakespeare Documented (Folger; TNA PROB 1/4); preamble recorded as context under nominal_affiliations (P42, v8's ruling on RQ1 (on the auditor's advice)).
