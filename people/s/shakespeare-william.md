---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 5
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch M)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-17
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to literature. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-17, by: "Grok Bot", summary: "Record created (stage 3 batch M, order P32: F 5, rank 81). Basics from Britannica (John Russell Brown, Terence Spencer and others, signed; Wayback copies; body only). No worldview statement in his own voice was read: the plays and poems are character or persona speech (P42), and the will's religious preamble was not read. All worldview fields UNKNOWN; mid_basin UNKNOWN (P19). Not plotted. Draft, not reviewed."}
    - {date: 2026-10-17, by: "Grok Bot", summary: "Batch M audit fixes (/workspace/genius_study_audit/gs_159d60d_M/run1/, run 1: 16 hold, 3 weaken): will read (Folger, PROB 1/4); by v8's ruling on RQ1 (on the auditor's advice) its formulaic preamble is lawyer drafting, not his statement (P42); 'only merits of Jesus Christ' recorded under nominal_affiliations as context. A stays UNKNOWN."}
    - {date: 2026-10-17, by: "Grok Bot", summary: "Batch N audit fix (#4): primary_system how_known no longer says the will was not read; it now says the will is read (S3)."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #80, F5 rank 81). Needs: A UNKNOWN; B UNKNOWN. Re-opened Britannica via Wayback (S1). New: Wikipedia EN dual-bio (S4, P50); Wikipedia Religious views (S5); Folger Venus and Adonis and Lucrece dedications — his signed own voice, no LIO content (S6, S7); Steggle Shakespeare Quarterly 2024 / Bristol on Spiritual Testament reattribution to Joan Shakespeare Hart, not John (S8); Modern Philology review of Kastan A Will to Believe — biographically 'impossible to know', plays' 'inclusive… Christianity' is about the dramas not a scored personal A (S9). P47 source_quality on S1–S9. Own-voice checks (dedications, will preamble under P42) and drama/character speech (P42; reconstructions labelled P49) leave A UNKNOWN and B UNKNOWN. Chart: still unplotted. No fallacy_catalog (Jason). Draft, not reviewed."}

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
  full_name: {value: "William Shakespeare", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lead"}], how_known: "Britannica and Wikipedia agree (P50)."}
  native_name: {value: UNKNOWN, how_known: "English."}
  aliases:
    - {name: "Shakespeare-William", kind: "roster alias"}
    - {name: "William-Shakespeare", kind: "roster alias"}
    - {name: "the Bard", kind: "other"}
    - {name: "Bard of Avon", kind: "other"}

basics:
  birth:
    date: {value: "1564-04-26", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening; 'Early life in Stratford'"}, {source: S4, locator: "lead / Early life"}], how_known: "Baptism date from the Holy Trinity parish register (S1, S4); the birth date itself is unknown ('his birthday is traditionally celebrated on April 23'). Recorded as the baptism date."}
    place: {value: "Stratford-upon-Avon, Warwickshire, England", modern_name: "Stratford-upon-Avon, United Kingdom", polity_then: "Kingdom of England", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "infobox"}], how_known: "Two sources agree (P50)."}
  death:
    date: {value: "1616-04-23", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening; 'Career in the theatre'"}, {source: S4, locator: "infobox"}], how_known: "Britannica and Wikipedia; cause unknown (S1)."}
    place: {value: "Stratford-upon-Avon, Warwickshire, England", modern_name: "Stratford-upon-Avon, United Kingdom", polity_then: "Kingdom of England", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "infobox"}], how_known: "Two sources agree."}
  first_lasting_contribution_year: {value: 1589, approx: true, certainty: 0.5, cites: [{source: S1, locator: "'Chronology of Shakespeare's plays'"}], how_known: "Henry VI, Part 1 and Titus Andronicus are dated 1589–92 (S1); a range counts from its start year (P12, P13). Love's Labour's Lost (1588–97) is not listed as lasting here because its range is too wide to place it. 'The first reference to Shakespeare in the literary world of London comes in 1592' (S1). 0.5."}
  era_bucket: {value: "1400 to 1599", certainty: 0.5, cites: [{source: S1, locator: "chronology"}], how_known: "From 1589 (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "England (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "London and Stratford."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [English], certainty: 1.0, cites: [{source: S1, locator: "text"}, {source: S4, locator: "Writing career"}], how_known: "Two sources."}
  occupations: {value: ["dramatist", "poet", "actor"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "infobox"}], how_known: "Two sources."}

contribution:
  primary_domain: literature
  fields: {value: ["drama", "poetry"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lead"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Henry VI, Part 1; Titus Andronicus", year: 1589, kind: work, lasting: "earliest plays in the chronology (1589–92) (S1)", certainty: 0.5, cites: [{source: S1, locator: "'Chronology of Shakespeare's plays'"}], how_known: "Britannica table, 1589–92; start year (P12)."}
    - {value: "Hamlet", year: 1599, kind: work, lasting: "(S1)", certainty: 0.5, cites: [{source: S1, locator: "'Chronology of Shakespeare's plays'"}], how_known: "Dated 1599–1601 in the table; start year (P12)."}
    - {value: "King Lear", year: 1605, kind: work, lasting: "(S1)", certainty: 0.5, cites: [{source: S1, locator: "'Chronology of Shakespeare's plays'"}], how_known: "Dated 1605–06; start year (P12)."}
    - {value: "The Tempest", year: 1611, kind: work, lasting: "(S1)", certainty: 0.7, cites: [{source: S1, locator: "'Chronology of Shakespeare's plays'"}], how_known: "Dated 1611."}
    - {value: "Henry VIII", year: 1613, kind: work, lasting: "last play listed (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Chronology of Shakespeare's plays'"}], how_known: "Dated 1613."}
    - {value: "Venus and Adonis (narrative poem with signed dedication)", year: 1593, kind: work, lasting: "first published work under his name; dedication in his signed own voice (S6)", certainty: 0.7, cites: [{source: S6, locator: "dedication"}, {source: S4, locator: "Poetry"}], how_known: "Folger text of the dedication signed William Shakespeare; Wikipedia dates 1593."}
  evidence_of_impact:
    - {value: "'often called the English national poet'; plays 'performed and read more often and in more countries than ever before'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "'widely regarded as the greatest writer in the English language and the world's pre-eminent dramatist'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S4, locator: "lead"}], how_known: "Wikipedia (P50 dual bio with S1)."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "'considered by many to be the greatest dramatist of all time' (S1); 'greatest writer in the English language' (S4).", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lead"}], how_known: "Coder's reading of two reference sources."}

childhood:
  family_religion: {value: "Church of England (conforming parish household); father held Stratford offices that required church membership in good standing", certainty: 0.7, cites: [{source: S1, locator: "'Early life in Stratford'"}, {source: S5, locator: "'Shakespeare's known religious affiliation'"}], how_known: "Baptism and municipal offices in the established church (S1, S5). The lost 'Spiritual Testament' formerly attributed to John Shakespeare is reattributed by Steggle (2024) to Joan Shakespeare Hart and is not used as evidence of John's Catholicism (S8)."}
  family_religious_practice: {value: "Parish baptism and burial entries; John Shakespeare as alderman/bailiff participated in whitewashing Catholic images in the Guild Chapel (S5). Private practice beyond conformity is not documented in what was read.", certainty: 0.5, cites: [{source: S5, locator: "'Shakespeare's known religious affiliation'"}], how_known: "Wikipedia Religious views summary of municipal conformity; certainty 0.5 (secondary)."}
  parents_and_household:
    - {value: "Father John Shakespeare, burgess, alderman (1565) and bailiff (1568) of Stratford, in trade", role: father, certainty: 0.7, cites: [{source: S1, locator: "'Early life in Stratford'"}], how_known: "Britannica."}
    - {value: "Mother Mary Arden of Wilmcote, heiress to some land", role: mother, certainty: 0.7, cites: [{source: S1, locator: "'Early life in Stratford'"}], how_known: "Britannica."}
  household_circumstances: {value: "Burgess household in Stratford; father's prosperity fluctuated; mother's Arden land was a step up socially (S1). Sister Joan Shakespeare Hart later lived in part of the Henley Street house (S8).", certainty: 0.7, cites: [{source: S1, locator: "'Early life in Stratford'"}, {source: S8, locator: "Bristol news summary of Steggle 2024"}], how_known: "Britannica plus Steggle context on Joan."}
  schooling:
    - {value: "Stratford grammar school (presumed; no pupil lists survive)", stage: "grammar or secondary school", run_by: "state or municipal", certainty: 0.5, cites: [{source: S1, locator: "'Early life in Stratford'"}], how_known: "Britannica: 'it would be absurd to suppose the bailiff of the town did not send his son there'; the master was paid by the borough."}
  early_mathematics: {value: UNKNOWN, how_known: "Sources read say nothing."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Sources read say nothing."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [English], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "Marriage licence bond with Anne Hathaway", year: 1582, age: 18, certainty: 0.7, cites: [{source: S1, locator: "'Early life in Stratford'"}, {source: S4, locator: "Marriage"}], how_known: "Bond dated November 28, 1582 (S1); Wikipedia agrees."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1589–1613", certainty: 0.5, cites: [{source: S1, locator: "'Chronology of Shakespeare's plays'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Baptized at Holy Trinity Church, Stratford-upon-Avon (Church of England); conforming member of the established church in the documentary record", certainty: 0.7, cites: [{source: S1, locator: "'Early life in Stratford'"}, {source: S5, locator: "'Shakespeare's known religious affiliation'"}], how_known: "Parish register (S1); Wikipedia: he and his immediate family were conforming members (S5). Context, not a code."}
    - {value: "Lay rector of Holy Trinity as lessee of Stratford parish tithes; buried in the chancel (S4, S5)", certainty: 0.7, cites: [{source: S4, locator: "Later years / burial"}, {source: S5, locator: "'Shakespeare's known religious affiliation'"}], how_known: "Wikipedia; fiscal/parish role, not a creedal profession."}
    - {value: "Will (25 March 1616) commends his soul 'into the hands of God my creator, hoping and assuredly believing through the only merits of Jesus Christ my Saviour to be made partaker of life everlasting' (a Protestant formula)", certainty: 0.5, cites: [{source: S3, locator: "modernized transcription; description"}], how_known: "Context only, not his own statement: v8's ruling on RQ1 (on the auditor's advice) (batch M audit), recorded in OPEN_DECISIONS P42: a formulaic will preamble is lawyer drafting (Francis Collins is named as a creator of the document; Folger calls the preamble 'very formulaic'). Kastan likewise treats the preamble as possibly conventional by 1616 (S9 via review). 'Protestant formula' is the coder's reading of 'only merits'."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing in his own voice on science and religion (P19). Dedications (S6, S7) are literary patronage, not that relation."}
  primary_system: {value: UNKNOWN, how_known: "The surviving record is 'mostly gleaned from documents of an official character' (S1). Speeches in the plays are characters' and the Sonnets' speaker is a persona, so neither is attributed to him (P42). The will (1616) is read (S3); its preamble is formulaic lawyer drafting and is context only (P42). Dedications of Venus and Adonis and Lucrece (S6, S7) are his signed own voice but contain no confessional profession. Scholarly debate (Catholic vs Protestant vs syncretic) remains unsettled; Kastan: biographically 'impossible to know' (S9). CHRIST stays a candidate under nominal affiliations only."}
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Baptized and buried in the parish church; conforming C of E record; will preamble is Protestant formula but P42 context only. Named but not coded: no attributable own-voice profession of Christian doctrine (P42). Secret-Catholic reconstructions from plays or family documents do not clear P42 / P49 for a system code (Kastan 'impossible to know', S9; Steggle removes John's Spiritual Testament, S8)."}
    - {code: ATHE, reason: "Rejected: Birch (1848) and similar atheist readings rest on character speech and are not accepted scholarly consensus (S5). Orwell's essay on Lear is literary, not a documented profession."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "P19 researched silent under P42. Checked: (1) plays and Sonnets — character/persona speech, not the author's view unless adopted in his own voice (P42 addendum; none read); (2) will preamble — lawyer drafting, context under nominal_affiliations only (P42); (3) Venus and Adonis and Lucrece dedications (S6, S7) — signed own voice, patronage language only, no God/locus profession; (4) grave epitaph ('Good friend, for Jesus' sake forbear…') — traditional burial text, authorship not established as his scored profession (S4); (5) Kastan / Woods / Wikipedia Religious views — scholarly debate on affiliation and on religion *in the plays*; Kastan's 'inclusive and theologically minimalist Christianity' is what he 'see[s] in the plays', not a P49 reconstruction of Shakespeare's personal locus that would score A (S9). Named alternative: BELOW_THRESHOLD only if a non-formulaic own-voice locus remark were found — none this pass.", note: "P49 reconstructions that score A need a scholar reconstructing the *person's* view; readings of the dramas' theology stay context (Lane A)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); B needs a statement about nature (P16). Character lines (e.g. Gloucester's 'As flies to wanton boys…' in Lear) are narrative, not his account of nature (P42). No scholarly reconstruction of Shakespeare's personal account of natural order was found that meets P49 (sources read discuss religion in the plays / affiliation, not laws of nature). Named alternative: none.", note: "P16 Austen prayer addendum does not apply; no own petitionary prayer document read."}
    C_ledger: {value: UNKNOWN, how_known: "As for A — nothing attributable on judgement, afterlife, or personal reward/punishment beyond the will's formulaic everlasting-life clause (P42 context only)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing attributable on revelation vs observation (P19). Drama's friars, Bibles, and sermons are character/stage religion (P42)."}
    E_scope: {value: UNKNOWN, how_known: "Nothing attributable (P7, P19)."}
  mid_basin: {value: UNKNOWN, how_known: "A and B are UNKNOWN (P19)."}
  statements:
    - text: "I know not how I shall offend in dedicating my unpolished lines to your Lordship, nor how the world will censure me for choosing so strong a prop to support so weak a burden; only if your Honor seem but pleased, I account myself highly praised and vow to take advantage of all idle hours till I have honored you with some graver labor."
      cites: [{source: S6, locator: "Venus and Adonis dedication (Folger text)"}]
      date: "1593"
      context: "Signed dedication to Henry Wriothesley, Earl of Southampton. His own voice (P42: attributed and signed). Patronage; no LIO content. Context only; not used to score."
      axes: []
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: "2026-10-24"
      note: "Own-voice check for deepen D1; scores nothing on A–E."
    - text: "The love I dedicate to your Lordship is without end; whereof this pamphlet without beginning is but a superfluous moiety. … What I have done is yours; what I have to do is yours; being part in all I have, devoted yours."
      cites: [{source: S7, locator: "Lucrece dedication (Folger text)"}]
      date: "1594"
      context: "Signed dedication to Southampton. Own voice; patronage; no LIO content. Context only."
      axes: []
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: "2026-10-24"
    - text: "In the name of God, Amen. I, William Shakespeare … first I commend my soul into the hands of God my creator, hoping and assuredly believing through the only merits of Jesus Christ my Saviour to be made partaker of life everlasting, and my body to the earth whereof it is made."
      cites: [{source: S3, locator: "modernized transcription, opening"}]
      date: "1616-03-25"
      context: "Will preamble. Folger: 'very formulaic'; creators include Francis Collins. P42: lawyer drafting, not his statement — logged under nominal_affiliations; quoted here as context only (P49 N/A). Does not score A or primary_system."
      axes: []
      kind: "other"
      verified_against: "primary facsimile"
      verified_on: "2026-10-17"
      note: "P42 addendum (will preamble). Reconstruction/label: formulaic set form, not scholarly reconstruction of belief."
  changes_over_life: []
  coder_notes: "Deepen D1 (queue #80): A UNKNOWN; B UNKNOWN after own-voice checks and scholarship. P42 blocks drama/character speech and the will preamble; dedications are own voice but empty for LIO; Kastan's play-Christianity is not a P49 personal-A reconstruction (he also says personal belief is 'impossible to know'). Steggle 2024 removes John's Spiritual Testament as evidence of a Catholic father. Lane B left unclear (no H1 test). Chart unplotted."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Church of England parish (Elizabethan settlement); family Catholicism claims for John Shakespeare weakened by Steggle 2024 reattribution of the Spiritual Testament to Joan (S8); Mary Arden's family often cited as Catholic-sympathetic in secondary literature (S5) — context only", certainty: 0.5, cites: [{source: S5, locator: "'Shakespeare's family'"}, {source: S8, locator: "Steggle / Bristol"}], how_known: "Secondary debate; not a code."}
  baptism_or_initiation: {value: "Baptized at Holy Trinity Church, Stratford-upon-Avon, April 26, 1564", certainty: 0.7, cites: [{source: S1, locator: "'Early life in Stratford'"}], how_known: "Parish register, per Britannica."}
  childhood_catechism: {value: UNKNOWN, how_known: "Grammar-school religious instruction presumed for the period but not documented for him in sources read."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1589–1613", certainty: 0.5, cites: [{source: S1, locator: "'Chronology of Shakespeare's plays'"}], how_known: "First to last listed lasting contribution (P29, P30); ranges counted from their start years (P12)."}
  age_at_first_lasting_contribution: {value: 25, certainty: 0.5, cites: [{source: S1, locator: "opening; chronology"}], how_known: "1589 − 1564 = 25 (P30), from the baptism year."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "Nothing attributable that scores an LIO axis (P27)."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S6, locator: "dedication"}, {source: S7, locator: "dedication"}, {source: S3, locator: "preamble"}], how_known: "Deepen D1 own-voice and P42 checks; still no scored LIO-type view."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Nothing attributable for the span."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Nothing attributable on method of definition from first principles.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Nothing read."}
  circle_present: {value: "unclear", rationale: "Drama's cosmic order language is character/narrative (P42), not a person-level circle claim.", certainty: 0.5, cites: [{source: S5, locator: "textual-evidence section"}], how_known: "Coder's reading; H1 not tested."}
  reading: "Lane B: no person-level form/circle finding. Religion-in-the-plays scholarship is literary history, not H1."
  notes: "Keep Lane A (unknown personal LIO) separate from Lane B (belief-model labels)."

institutions:
  - {value: "Lord Chamberlain's Men (King's Men from 1603)", role: member, years: "c. 1594–1613", kind: other, certainty: 0.7, cites: [{source: S1, locator: "'Career in the theatre'"}, {source: S4, locator: "infobox"}], how_known: "Britannica and Wikipedia."}
  - {value: "Holy Trinity Church, Stratford-upon-Avon (lay rector via tithe lease)", role: "lay rector / tithe lessee", years: "c. 1605–1616", kind: other, certainty: 0.7, cites: [{source: S4, locator: "Later years"}, {source: S5, locator: "known religious affiliation"}], how_known: "Wikipedia; fiscal parish role."}
collaborators:
  - {value: "Richard Burbage", relation: collaborator, note: "lead actor of the company", certainty: 0.7, cites: [{source: S1, locator: "'Career in the theatre'"}], how_known: "Britannica."}
  - {value: "John Heminge and Henry Condell", relation: collaborator, note: "fellow actors who collected the First Folio (1623); mourning-ring bequests in the will (S3)", certainty: 0.7, cites: [{source: S1, locator: "'Career in the theatre'"}, {source: S3, locator: "bequests to fellows"}], how_known: "Britannica and will."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 81"}], how_known: "Study roster."}
  controversies:
    - {value: "Authorship / anti-Stratfordian theories (rejected by scholarly consensus; not used here)", certainty: 0.7, cites: [{source: S4, locator: "Authorship"}], how_known: "Wikipedia notes the fringe; study uses Stratford attribution."}
    - {value: "Catholic vs Protestant personal-faith debate; biographically unsettled (S5, S9)", certainty: 0.7, cites: [{source: S5, locator: "lead"}, {source: S9, locator: "review of Kastan p. 29 'impossible to know'"}], how_known: "Ongoing scholarly debate; deepen D1 does not resolve it into a code."}
  data_quality_flags:
    - "No document in his own voice that scores A–E was found this pass (P42)."
    - "Kastan's A Will to Believe was not read in full; Modern Philology review (S9) supplies the 'impossible to know' / plays-Christianity quotations."
    - "Steggle Shakespeare Quarterly 75.1 (2024) read via University of Bristol news summary and Wikipedia Religious views citation (S8), not the paywalled PDF."
    - "Grave epitaph authorship not treated as his scored profession."
  open_questions:
    - "Settled (RQ1, P42): the will's formulaic preamble is not his own statement."
    - "Print-check Kastan A Will to Believe (OUP 2014) pp. 28–37 for full biographical survey wording."
    - "Schoenbaum Documentary Life / Compact Documentary Life for any overlooked non-dramatic document."
    - "ODNB Shakespeare article if accessible for dual-bio strengthening beyond Wikipedia."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "John Russell Brown, Terence John Bew Spencer and others"
    citation: "Brown, John Russell, Terence John Bew Spencer et al. \"William Shakespeare.\" Encyclopaedia Britannica. https://www.britannica.com/biography/William-Shakespeare. Read in Wayback snapshots: main page 2025-12-19 16:25:14 UTC; 'Career in the theatre' 20260902004320; 'Chronology of Shakespeare's plays' 20260829053559; 'Early posthumous documentation' 20260815145150. Deepen D1 reopened Wayback 20251219162514."
    url: "https://www.britannica.com/biography/William-Shakespeare"
    accessed: 2026-10-24
    reliability_note: "Signed, multi-author article. Live page often bot-blocked; Wayback body used. Body only; Top Questions not cited."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-17
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S3
    type: primary
    kind: "archive record"
    author: "Folger Shakespeare Library (Shakespeare Documented)"
    citation: "\"Shakespeare's last will and testament: made 25 March 1616, proved 22 June 1616.\" Shakespeare Documented, Folger Shakespeare Library. The National Archives, Kew, PROB 1/4. doi:10.37078/110. https://shakespearedocumented.folger.edu/resource/document/william-shakespeares-last-will-and-testament-original-copy-including-three"
    url: "https://shakespearedocumented.folger.edu/resource/document/william-shakespeares-last-will-and-testament-original-copy-including-three"
    accessed: 2026-10-24
    reliability_note: "Folger's description and modernized transcription of the original will; creator listed as 'Francis Collins, esq. et al.; William Shakespeare'. Preamble formulaic (P42)."
    source_quality: "primary / own words"
    used_for: [worldview, collaborators, review]
  - id: S4
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "\"William Shakespeare.\" Wikipedia. https://en.wikipedia.org/wiki/William_Shakespeare."
    url: "https://en.wikipedia.org/wiki/William_Shakespeare"
    accessed: 2026-10-24
    reliability_note: "Dual-source biography with S1 (P50). Used for life facts, burial/epitaph, tithe lease; not to score A/B from drama."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, review]
  - id: S5
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "\"Religious views of William Shakespeare.\" Wikipedia. https://en.wikipedia.org/wiki/Religious_views_of_William_Shakespeare."
    url: "https://en.wikipedia.org/wiki/Religious_views_of_William_Shakespeare"
    accessed: 2026-10-24
    reliability_note: "Survey of the affiliation debate and play-based arguments. Secondary; used for what evidence exists and for Steggle 2024 citation, not to score character speech as his view (P42)."
    source_quality: "reference entry"
    used_for: [childhood, worldview, heritage, review]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "William Shakespeare"
    year: 1593
    citation: "Shakespeare, William. Venus and Adonis, dedication to Henry Wriothesley. Folger Shakespeare Library text. https://www.folger.edu/explore/shakespeares-works/venus-and-adonis/read/dedication/"
    url: "https://www.folger.edu/explore/shakespeares-works/venus-and-adonis/read/dedication/"
    accessed: 2026-10-24
    reliability_note: "Signed 'William Shakespeare'. Own voice under P42; no confessional or nature content."
    source_quality: "primary / own words"
    used_for: [contribution, worldview, timing]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "William Shakespeare"
    year: 1594
    citation: "Shakespeare, William. The Rape of Lucrece, dedication to Henry Wriothesley. Folger Shakespeare Library text. https://www.folger.edu/explore/shakespeares-works/lucrece/read/dedication/"
    url: "https://www.folger.edu/explore/shakespeares-works/lucrece/read/dedication/"
    accessed: 2026-10-24
    reliability_note: "Signed own voice; patronage only."
    source_quality: "primary / own words"
    used_for: [worldview, timing]
  - id: S8
    type: secondary
    kind: "journal article"
    author: "Matthew Steggle"
    year: 2024
    citation: "Steggle, Matthew. \"John Shakespeare's 'Spiritual Testament' Is Not John Shakespeare's.\" Shakespeare Quarterly 75, no. 1 (2024): 44–71. doi:10.1093/sq/quae003. Access this pass: University of Bristol news summary (21 March 2024) and Wikipedia Religious views citation of the article."
    url: "https://www.bristol.ac.uk/news/2024/march/joan-shakespeare.html"
    accessed: 2026-10-24
    reliability_note: "Peer-reviewed finding summarized in university press release; paywalled SQ PDF not opened this pass. Reattributes the Spiritual Testament to Joan Shakespeare Hart (1569–1646)."
    source_quality: "scholarly edition or monograph"
    used_for: [childhood, worldview, heritage, review]
  - id: S9
    type: secondary
    kind: "journal article"
    author: "review of David Scott Kastan; Modern Philology"
    year: 2015
    citation: "Review of David Scott Kastan, A Will to Believe: Shakespeare and Religion (Oxford: Oxford University Press, 2014). Modern Philology 113, no. 1. https://www.journals.uchicago.edu/doi/10.1086/681090. Quotes Kastan's biographical 'impossible to know' (p. 29) and plays' 'inclusive and theologically minimalist Christianity' (p. 37)."
    url: "https://www.journals.uchicago.edu/doi/10.1086/681090"
    accessed: 2026-10-24
    reliability_note: "Review of a scholarly monograph (Oxford Wells lectures). Used for Kastan's published stance that personal belief cannot be fixed and that play-Christianity is not a key to private faith. Full Kastan volume unread."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, review]
---

# William Shakespeare

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

William Shakespeare (1564–1616), English dramatist and poet [S1, S4]. Deepen D1: own-voice dedications checked [S6, S7]; will preamble remains P42 context [S3]; drama/character speech not attributed [P42]. A UNKNOWN; B UNKNOWN; mid_basin UNKNOWN. Not plotted.

## Life and work

Stratford; London with the Lord Chamberlain's Men from about 1594; New Place bought 1597; tithe lease / lay rector [S1, S4, S5].

## Contribution and impact

Plays dated 1589–1613 [S1]; Venus and Adonis 1593 with signed dedication [S6].

## Childhood and education

Son of John Shakespeare and Mary Arden; Stratford grammar school presumed [S1]. Spiritual Testament reattributed to sister Joan (Steggle 2024), not John [S8].

## Adult working worldview

Unknown after deepen: no attributable LIO profession [S1, S3, S5, S6, S7, S9]. Scholarly affiliation debate unsettled; Kastan: biographically impossible to know [S9].

## Heritage (context only)

English; baptized at Holy Trinity, Stratford [S1].

## Timing

First lasting contribution about 1589, at 25 [S1]. No LIO-type views found [P27].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form/circle unclear; H1 not tested. Keep separate from Lane A UNKNOWN.

## Open questions

- Settled: the will's formulaic preamble is context only (P42).
- Print-check Kastan 2014; Schoenbaum Documentary Life; ODNB if available.

## Research log

- 2026-10-17: Read Britannica (Brown, Spencer et al.) in Wayback copies; live page and newest snapshot not available.
- 2026-10-17 (batch M audit fixes): read the will on Shakespeare Documented (Folger; TNA PROB 1/4); preamble recorded as context under nominal_affiliations (P42, v8's ruling on RQ1 (on the auditor's advice)).
- 2026-10-24 (deepen D1, queue #80): Wayback Britannica; Wikipedia main + Religious views; Folger Venus/Lucrece dedications; Steggle 2024 via Bristol; Kastan via Modern Philology review. A/B stay UNKNOWN. No fallacy_catalog.
