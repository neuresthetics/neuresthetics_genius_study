---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch U)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch U, order P32: F 4, rank 118; taken in place of Louis Pasteur, already coded). Basics from Britannica (Anne J. Cruz). Worldview from his own dedication (19 April 1616) and prologue to Los trabajos de Persiles y Sigismunda (published 1617), read in the Calpe 1920 edition on Wikisource; after the span (P1 cap 0.5). Characters' words in the novels are not his (P42). Not a scientist (P30). primary_system CHRIST (0.5, alt BELOW_THRESHOLD); A BELOW_THRESHOLD; B BELOW_THRESHOLD; C BELOW_THRESHOLD; D UNKNOWN; E UNKNOWN; mid_basin BELOW_THRESHOLD. Not plotted. Draft, not reviewed."}

identity:
  id: de-cervantes-miguel
  display_name: "Miguel de Cervantes"
  roster:
    canonical_name: "Miguel de Cervantes"
    rank: 118
    F: 4
    models: [Claude, DeepSeek, Gemini, Grok]
    band: "core (3–4)"
    status: core
    field: literature
    field_bucket: literature
  full_name: {value: "Miguel de Cervantes Saavedra", certainty: 0.7, cites: [{source: S1, locator: "facts box (In full)"}], how_known: "Britannica."}
  native_name: {value: "Miguel de Cervantes Saavedra", certainty: 0.7, cites: [{source: S1, locator: "facts box"}], how_known: "Spanish; same as the full name."}
  aliases:
    - {name: "Cervantes-Miguel de", kind: "roster alias"}

basics:
  birth:
    date: {value: "1547-09-29", calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "facts box (Born); body, first paragraph after the opening"}], how_known: "Britannica: 'probably on September 29 (the day of San Miguel)'; baptized 9 October 1547 ('certainly'). Before the 1582 Gregorian reform in Spain, so Julian."}
    place: {value: "Alcalá de Henares", modern_name: "Alcalá de Henares, Madrid, Spain", polity_then: "Crown of Castile (Spain)", certainty: 0.7, cites: [{source: S1, locator: "facts box (Born)"}], how_known: "Britannica."}
  death:
    date: {value: "1616-04-22", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "facts box (Died)"}], how_known: "Britannica."}
    place: {value: "Madrid", modern_name: "Madrid, Spain", polity_then: "Crown of Castile (Spain)", certainty: 0.7, cites: [{source: S1, locator: "facts box (Died)"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1605, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Don Quixote, Part I (1605)."}
  era_bucket: {value: "1600 to 1749", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "1605 (P2)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "facts box"}], how_known: "Spain (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Spain (Madrid)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Pronouns in Britannica."}
  languages_of_work: {value: ["Spanish"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  occupations: {value: ["novelist, playwright and poet", "soldier", "royal messenger, commissary of provisions for the Armada, tax collector"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Soldier and slave'; question box on his living"}], how_known: "Britannica; the later posts from the question box only."}

contribution:
  fields: {value: ["novel", "short story", "drama", "poetry"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Don Quixote, Part I (El ingenioso hidalgo don Quijote de la Mancha)", year: 1605, kind: work, lasting: "translated into 'more than 60 languages'; critical discussion 'unabated since the 18th century' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "Novelas ejemplares (Exemplary Stories)", year: 1613, kind: work, lasting: "'a few ... attain a level close to that of Don Quixote' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "Don Quixote, Part II", year: 1615, kind: work, lasting: "as Part I (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica dates Don Quixote '(1605, 1615)'. Fiction, so not a scientist (P30)."}
  evidence_of_impact:
    - {value: "'the most important and celebrated figure in Spanish literature'; Don Quixote and Sancho Panza 'probably familiar visually to more people than any other imaginary characters in world literature'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Los trabajos de Persiles y Sigismunda", year: 1617, certainty: 0.7, cites: [{source: S2, locator: "Dedicatorias, pp. 9–10"}], how_known: "Posthumous; dedication dated 19 April 1616. Not listed as lasting in the sources read."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "'the most important and celebrated figure in Spanish literature' (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father: a barber-surgeon who set bones and performed bloodlettings", certainty: 0.7, cites: [{source: S1, locator: "body, first paragraph after the opening"}], how_known: "Britannica."}
  household_circumstances: {value: "Fourth of seven children of a family of minor gentry origins 'come down in the world'; moved from town to town; may have been converso", certainty: 0.7, cites: [{source: S1, locator: "body, first paragraph after the opening"}], how_known: "Britannica."}
  schooling:
    - {value: "Possibly a pupil (or pupil-teacher) of Juan López de Hoyos, head of a municipal school in Madrid, who in 1569 called a Miguel de Cervantes his 'beloved pupil'; no university", stage: "grammar or secondary school", run_by: "state or municipal", years: "by 1569", certainty: 0.5, cites: [{source: S1, locator: "body, first paragraph after the opening"}], how_known: "Britannica; identity of the pupil not certain. Jesuit schooling is 'conjectural' (S1)."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Juan López de Hoyos (if the same Cervantes), a man 'with Erasmist intellectual leanings'", certainty: 0.5, cites: [{source: S1, locator: "body, first paragraph after the opening"}], how_known: "Britannica."}
  languages_in_childhood: {value: ["Spanish"], certainty: 0.5, cites: [{source: S1, locator: "body"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "Baptized 9 October 1547", certainty: 0.7, cites: [{source: S1, locator: "body, first paragraph after the opening"}], how_known: "Britannica ('certainly')."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1605–1615", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Baptized Catholic; ransomed from Algiers in 1580 with the aid of the Trinitarian friars", certainty: 0.7, cites: [{source: S1, locator: "body; 'Soldier and slave'"}], how_known: "Britannica. Context, not a code."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing in his own voice read on the topic."}
  primary_system:
    value: CHRIST
    basis: written_profession
    certainty: 0.5
    cites: [{source: S2, locator: "Dedicatorias, pp. 9–10; Prólogo, p. 13"}]
    rationale: "Christian practice and belief in his own published words: 'Ayer me dieron la extremaunción, y hoy escribo ésta' (the sacrament of the Church, dedication of 19 April 1616) and the prologue's farewell 'que yo me voy muriendo, y deseando veros presto contentos en la otra vida'. Catholic branch. Named alternative BELOW_THRESHOLD: receiving a sacrament is practice, and 'cúmplase la voluntad de los cielos' and 'guarde Dios a vuesa excelencia' are set courtesy formulas of a dedication (compare P42's will-preamble addendum), so the text may show no belief beyond convention."
    how_known: "Dedication and prologue written for publication (Persiles, 1617), in his own voice, a few days before his death and after the working years, so 0.5 (P1). Don Quixote's characters, its narrators and the novellas' events are not his view (P42)."
    alternatives:
      - {value: BELOW_THRESHOLD, note: "Sacrament as practice; formulas as convention.", cites: [{source: S2, locator: "Dedicatorias, pp. 9–10"}]}
  secondary_system: {value: UNKNOWN, how_known: "One system (P29)."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Chosen at 0.5 (P1 cap)."}
    - {code: CLTHEI, reason: "Rejected: 'milagro' is a figure for an unlikely recovery, not stressed petition."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Lead only: 'cúmplase la voluntad de los cielos' and 'guarde Dios a vuesa excelencia como puede' (S2, pp. 9–10) are courtesy formulas of a dedication and do not place God."}
    B_cause: {value: BELOW_THRESHOLD, how_known: "Not a scientist (P30). Lead only: 'Si a dicha, por buena ventura mía, que ya no sería ventura, sino milagro, me diese el cielo vida' (S2, p. 10) treats recovery as a miracle heaven might grant, but as a figure for how unlikely it is, not a statement on nature's order (P16); after the span (P1)."}
    C_ledger: {value: BELOW_THRESHOLD, how_known: "Lead only: 'deseando veros presto contentos en la otra vida' (S2, p. 13) hopes for an afterlife but says nothing of reward or punishment."}
    D_authority: {value: UNKNOWN, how_known: "Nothing on revelation against observation in his own voice read (P19)."}
    E_scope: {value: UNKNOWN, how_known: "Nothing on the world's order read (P7, P19)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "P4 test: A and B are BELOW_THRESHOLD; neither is UNKNOWN."}
  statements:
    - text: "Ayer me dieron la extremaunción, y hoy escribo ésta; el tiempo es breve, las ansias crecen, las esperanzas menguan, y, con todo esto, llevo la vida sobre el deseo que tengo de vivir"
      cites: [{source: S2, locator: "Dedicatorias, p. 9"}]
      date: "1616-04-19"
      context: "Dedication of Persiles to the Conde de Lemos, opening with the old couplet 'Puesto ya el pie en el estribo'; dated Madrid, 19 April 1616, three days before his death."
      axes: []
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Wikisource proofread transcription of the Calpe (Colección Universal) 1920 edition, vol. 1; printed page 9 (scan page 11)."
    - text: "Pero si está decretado que la haya de perder, cúmplase la voluntad de los cielos"
      cites: [{source: S2, locator: "Dedicatorias, pp. 9–10"}]
      date: "1616-04-19"
      context: "Same dedication; 'la' is his life."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Across the page break (scan pages 11–12)."
    - text: "Si a dicha, por buena ventura mía, que ya no sería ventura, sino milagro, me diese el cielo vida, las verá"
      cites: [{source: S2, locator: "Dedicatorias, p. 10"}]
      date: "1616-04-19"
      context: "Same dedication, on works he hopes to finish (Semanas del jardín, Bernardo, the end of La Galatea)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
    - text: "¡A Dios, gracias; a Dios, donaires; a Dios, regocijados amigos; que yo me voy muriendo, y deseando veros presto contentos en la otra vida!"
      cites: [{source: S2, locator: "Prólogo, p. 13"}]
      context: "Close of the Persiles prologue, after his account of meeting a student on the road from Esquivias; written in his last days."
      axes: [C_ledger]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "'A Dios' as spelled in this edition (adiós). Undated; written by April 1616."
  changes_over_life: []
  coder_notes: "Coder's call. The only own-voice evidence read is the Persiles dedication and prologue (1616), after the span (P1). CHRIST rests on the sacrament and the hope of 'la otra vida', with BELOW_THRESHOLD as the named alternative because dedication formulas are conventional. The novels are fiction: no character's words are taken as his (P42), and no own-voice adoption was read. Leads: the prologues to Don Quixote I and II and the Novelas ejemplares; his entry into the Franciscan Third Order (not in the sources read). Not plotted."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Castilian; family possibly converso (of Jewish descent)", certainty: 0.5, cites: [{source: S1, locator: "question box 'early life'"}], how_known: "Britannica: 'may have been converso'."}
  religious_heritage_by_birth: {value: "Catholic", certainty: 0.7, cites: [{source: S1, locator: "body, first paragraph after the opening"}], how_known: "Baptized 1547."}
  baptism_or_initiation: {value: "Baptized 9 October 1547", certainty: 0.7, cites: [{source: S1, locator: "body, first paragraph after the opening"}], how_known: "Britannica."}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1605–1615", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "From Don Quixote Part I (1605) to Part II (1615) (P30)."}
  age_at_first_lasting_contribution: {value: 58, certainty: 0.7, cites: [{source: S1, locator: "facts box; opening"}], how_known: "1605 − 1547 = 58 (P30); 57 if Part I appeared before his birthday."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No LIO-type statement read."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "Dedicatorias; Prólogo"}], how_known: "None in the texts read."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Not assessed."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Not assessed."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  reading: "Not assessed."
  notes: ""

institutions:
  - {value: "Household of Cardinal Giulio Acquaviva, Rome", role: "chamberlain ('It seems')", kind: employer, certainty: 0.5, cites: [{source: S1, locator: "'Soldier and slave'"}], how_known: "Britannica, hedged."}
  - {value: "Spanish infantry regiment, Naples", role: "soldier; wounded at Lepanto (7 October 1571), losing the use of his left hand", years: "1570–1575", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "'Soldier and slave'"}], how_known: "Britannica."}
  - {value: "Trinitarian friars", role: "helped raise his ransom from Algiers", years: "1580", kind: "religious body", certainty: 0.7, cites: [{source: S1, locator: "'Soldier and slave'"}], how_known: "Britannica."}
  - {value: "Conde de Lemos", role: "patron; dedicatee of Persiles", kind: "patron or funder", certainty: 0.7, cites: [{source: S2, locator: "Dedicatorias, pp. 9–10"}], how_known: "The dedication."}
collaborators:
  - {value: "Rodrigo de Cervantes", relation: family, note: "brother, captive with him in Algiers, freed 1577", certainty: 0.7, cites: [{source: S1, locator: "'Soldier and slave'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 118"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Own-voice evidence is two paratexts of 1616, after the span (P1)."
    - "Britannica body read through 'Soldier and slave'; later sections not fetched."
  open_questions:
    - "Read the prologues to Don Quixote I and II and the Novelas ejemplares for own-voice statements."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Anne J. Cruz (Britannica)"
    citation: "Cruz, Anne J. \"Miguel de Cervantes.\" Encyclopaedia Britannica (updated 2 October 2026). https://www.britannica.com/biography/Miguel-de-Cervantes. Read live 2026-10-19."
    url: "https://www.britannica.com/biography/Miguel-de-Cervantes"
    accessed: 2026-10-19
    reliability_note: "Signed article; fetched text ran through 'Soldier and slave'. Question boxes cited only where marked."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Miguel de Cervantes"
    citation: "Cervantes Saavedra, Miguel de. Los trabajos de Persiles y Sigismunda, tomo I. Madrid: Calpe (Colección Universal 237–240), 1920. Dedicatoria al Conde de Lemos (dated 19 April 1616), pp. 9–10; Prólogo, pp. 11–13. Wikisource (es) proofread transcription of the Google Books scan Ws44AAAAYAAJ, pages 11–15 of the scan. First published Madrid, 1617."
    url: "https://es.wikisource.org/wiki/Los_trabajos_de_Persiles_y_Sigismunda_(1920)/Tomo_I/Dedicatorias"
    accessed: 2026-10-19
    reliability_note: "Popular edition of the text; Wikisource page quality 3 (proofread). Pages from the printed numbers in the transcription."
    used_for: [worldview, contribution, institutions, timing]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Miguel de Cervantes

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Miguel de Cervantes (1547–1616), Spanish novelist, playwright and poet, creator of Don Quixote [S1]. Draft: primary_system CHRIST (0.5, alt BELOW_THRESHOLD); A, B and C BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not plotted.

## Life and work

Soldier at Lepanto, captive in Algiers 1575–1580 [S1].

## Contribution and impact

Don Quixote (1605, 1615) and the Novelas ejemplares (1613) [S1].

## Childhood and education

Son of a barber-surgeon; schooling little known [S1].

## Adult working worldview

'Ayer me dieron la extremaunción, y hoy escribo ésta' (1616) [S2, p. 9].

## Heritage (context only)

Catholic; family possibly converso [S1].

## Timing

1605–1615, from age 58 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Not assessed.

## Open questions

- The prologues to Don Quixote and the Novelas ejemplares.

## Research log

- 2026-10-19: Read Britannica (through 'Soldier and slave') and the Persiles dedication and prologue on Wikisource.
