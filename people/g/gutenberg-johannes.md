---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA3)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to medieval. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #178, F 3, rank 189). Hunt: any documentary religion/nature statements. Read: Wikipedia EN dual bio (S4); Lehmann-Haupt Britannica fuller (S3); Deutsche Biographie NDB Ruppel + authority data katholisch / Franziskanerkirche burial (S5); Mainz city Gutenberg timeline baptism tradition St. Christoph / death 1468-02-03 / Franciscan burial (S6). Surviving record is legal/business (Helmasperger 1455 notarial instrument; Strasbourg suits) — no first-person diaries/letters on God or nature. Helmasperger opens with formulaic 'In Gottes Namen Amen' (notary Ulrich Helmasperger), not Gutenberg's theology (P42). Printing Bible / Cypriot indulgences / Psalter groundwork / later Aquinas Summa attributions = craft/client work, not personal profession (standing rule; P47–P50). Kapr Cusanus liturgical-motivation link is explicit hypothesis, not evidence. Catholicon 1460 colophon God-language not securely Gutenberg's own voice (authorship contested). P47 source_quality on S1–S6. P50 dual bio S1+S4. Heritage filled (late-medieval Latin Catholic Mainz; baptism tradition only). primary_system stays UNKNOWN (CHRIST lead only); A–E UNKNOWN; mid UNKNOWN; not plotted. Chart-moving NO. No fallacy_catalog. No figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "AA3 audit fix (v8's call on the auditor's advice): alternative birth about 1400, age about 55. Signed Britannica article (Lehmann-Haupt) added as S3; only part of it was read and it did not confirm the Bible date in the body, so the span stays 0.5."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA3, order P32: F 3, rank 189). Source: Britannica (students edition, read in full). Lasting work: printing with movable metal type, 'one of the world's greatest inventions' whose method 'endured almost unchanged for five centuries'; dated by the Gutenberg Bible, 'completed before or in 1455' (publication, P30 #1), at 0.5 with 1454 (the Türkenkalender, 'printed in 1454') as the alternative. Birth '1395?' and death 'probably ... February 3, 1468', so age about 60 at 0.5; alternative birth about 1400, age about 55 (AA3 audit advice). The signed Britannica article (Lehmann-Haupt, S3) gives 'born 14th century, Mainz' and the Fust judgment of 6 November 1455. An invention, not a theory (P33): not a scientist, B UNKNOWN. No own words: worldview all UNKNOWN (lead CHRIST: printed the Bible; pension from the archbishop of Mainz). Not plotted. Draft, not reviewed."}

identity:
  id: gutenberg-johannes
  display_name: "Johannes Gutenberg"
  roster:
    canonical_name: "Johannes Gutenberg"
    rank: 189
    F: 3
    models: [Gemini, GPT, Grok]
    band: "core (3–4)"
    status: "core"
    field: "invention"
    field_bucket: "invention / engineering"
  full_name: {value: "Johannes Gensfleisch zur Laden zum Gutenberg", certainty: 1.0, cites: [{source: S1, locator: "para. 3"}, {source: S4, locator: "lead / infobox"}], how_known: "Britannica students + Wikipedia EN (P50 dual bio)."}
  native_name: {value: "Johannes Gensfleisch zur Laden zum Gutenberg", certainty: 0.7, cites: [{source: S4, locator: "lead"}], how_known: "German Latin-script full form (Wikipedia EN)."}
  aliases:
    - {name: "Gutenberg-Johannes", kind: "roster alias"}
    - {name: "Johannes-Gutenberg", kind: "roster alias"}
    - {name: "Johann Gutenberg", kind: "other"}
    - {name: "Henne / Henchin zu Gudenberg", kind: "other"}

basics:
  birth:
    date: {value: "1395", certainty: 0.5, cites: [{source: S1, locator: "heading"}, {source: S3, locator: "Introduction"}, {source: S4, locator: "Early life"}, {source: S5, locator: "NDB dates"}], how_known: "Britannica students '1395?'; Wikipedia scholarly range c. 1393–1406, commonly 1400 'for convenience'; NDB 'zwischen 1394 und 1399'. Alternative about 1400 (AA3), age about 55."}
    place: {value: "Mainz", modern_name: "Mainz, Germany", polity_then: "Free City / Electorate of Mainz (Holy Roman Empire)", certainty: 1.0, cites: [{source: S1, locator: "para. 3"}, {source: S4, locator: "infobox"}], how_known: "Britannica + Wikipedia EN."}
  death:
    date: {value: "1468-02-03", certainty: 0.7, cites: [{source: S1, locator: "para. 5"}, {source: S4, locator: "Later life"}, {source: S5, locator: "NDB † 3.2.1468"}, {source: S6, locator: "1468"}], how_known: "NDB and Mainz city timeline give 3 February 1468; Britannica students 'probably'; Wikipedia year 1468. Dual scholarly/city → 0.7."}
    place: {value: "Mainz", modern_name: "Mainz, Germany", polity_then: "Electorate of Mainz (Holy Roman Empire)", certainty: 0.7, cites: [{source: S1, locator: "para. 5"}, {source: S4, locator: "Later life"}, {source: S6, locator: "1468 Hof zum Algesheimer"}], how_known: "Britannica + Wikipedia + Mainz timeline (Hof zum Algesheimer)."}
  first_lasting_contribution_year: {value: 1455, certainty: 0.5, cites: [{source: S1, locator: "para. 5"}, {source: S4, locator: "Printing press / Printed books"}], how_known: "42-line Bible completed before or in 1455 (S1; Wikipedia); publication (P30 #1). Alternative 1454: Türkenkalender / Cypriot indulgences."}
  era_bucket: {value: "1400 to 1599", certainty: 1.0, cites: [{source: S1, locator: "para. 4–5"}, {source: S4, locator: "lead"}], how_known: "1454–1455 lasting work in bucket (P2); dual bio."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "para. 3"}], how_known: "Germany (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "para. 3–5"}, {source: S4, locator: "Early life / Printing press"}], how_known: "Strasbourg; Mainz."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Latin", "German"], certainty: 0.7, cites: [{source: S1, locator: "para. 5"}, {source: S4, locator: "Printed books"}], how_known: "Latin Bible / Donatus; German poem / calendar / Türkenbulle (Britannica + Wikipedia)."}
  occupations: {value: ["metalworker", "goldsmith", "printer", "inventor"], certainty: 0.7, cites: [{source: S1, locator: "para. 1, 3"}, {source: S4, locator: "infobox / Education"}], how_known: "Britannica + Wikipedia EN."}

contribution:
  era_bucket: medieval
  fields: {value: ["printing"], certainty: 0.7, cites: [{source: S1, locator: "para. 1"}, {source: S4, locator: "lead"}], how_known: "Britannica + Wikipedia EN."}
  lasting_original_contributions:
    - {value: "Printing with movable metal type (the Gutenberg press; the 42-line Bible)", year: 1455, kind: "invention", lasting: "'his method of using movable metal type endured almost unchanged for five centuries'; 'one of the world's greatest inventions' (S1); Time-Life 'most important of the second millennium' (S4)", certainty: 0.5, cites: [{source: S1, locator: "para. 1–2, 5"}, {source: S4, locator: "lead / Printed books"}], how_known: "Britannica + Wikipedia; dated by Bible completion 'before or in 1455' (0.5)."}
  evidence_of_impact:
    - {value: "Led to a great increase in literacy and the spread of knowledge; factor in Renaissance, Reformation, humanist print culture", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "para. 2"}, {source: S4, locator: "Influence"}], how_known: "Britannica + Wikipedia EN."}
  major_works:
    - {value: "Türkenkalender", year: 1454, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "para. 5"}], how_known: "Britannica: printed 1454."}
    - {value: "42-line Bible (Gutenberg Bible)", year: 1455, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "para. 5"}, {source: S4, locator: "Printed books"}], how_known: "Britannica + Wikipedia."}
  honours:
    - {value: "Pension / Hofmann title from Archbishop Adolf von Nassau of Mainz", year: 1465, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "para. 6"}, {source: S4, locator: "Later life"}, {source: S6, locator: "1465"}], how_known: "Britannica + Wikipedia + Mainz timeline (court outfit, grain, wine, tax freedom)."}
  definition_fit: {value: "clearly meets", rationale: "One of the world's greatest inventions (S1); Wikipedia consensus on movable-type press impact.", certainty: 0.7, cites: [{source: S1, locator: "para. 2"}, {source: S4, locator: "lead"}], how_known: "Britannica + Wikipedia."}

childhood:
  family_religion: {value: "Late-medieval Latin Catholic (Mainz patrician household)", certainty: 0.5, cites: [{source: S5, locator: "Religious Denomination katholisch"}, {source: S4, locator: "Early life"}], how_known: "Deutsche Biographie authority data 'katholisch'; Mainz parish/mint-patrician context. No household creed statement. Heritage only — not a worldview code."}
  family_religious_practice: {value: UNKNOWN, how_known: "No household liturgy or practice detail in sources read."}
  parents_and_household:
    - {value: "Father Friele Gensfleisch zur Laden, Mainz patrician / merchant, Münzerhausgenosse (mint companion)", role: "father", certainty: 0.7, cites: [{source: S1, locator: "para. 3"}, {source: S4, locator: "Early life"}, {source: S5, locator: "NDB Genealogy"}], how_known: "Britannica + Wikipedia + NDB."}
    - {value: "Mother Else Wirich (Wyrich), daughter of a Mainz shopkeeper; not of patrician lineage", role: "mother", certainty: 0.7, cites: [{source: S4, locator: "Early life"}, {source: S5, locator: "NDB Genealogy"}], how_known: "Wikipedia + NDB."}
  household_circumstances: {value: "Patrician Hof zum Gutenberg beside St. Christoph's; family left Mainz in guild–patrician conflicts (c. 1411, 1413) for Eltville; returned intermittently", certainty: 0.5, cites: [{source: S4, locator: "Early life"}, {source: S6, locator: "1400–1434"}], how_known: "Wikipedia + Mainz timeline."}
  schooling:
    - {value: "Expected patrician education in reading, arithmetic, and likely Latin; school site unknown (Mainz parish, Eltville, private tutor, or St. Victor's — speculative)", stage: "other", run_by: other, certainty: 0.5, cites: [{source: S4, locator: "Education"}], how_known: "Wikipedia (Kapr/Wagner trail); no documentary school record."}
    - {value: "Possible University of Erfurt enrollment as 'Johannes de Altavilla' (Eltville) winter 1419/20 — identity not certain", stage: "university", run_by: other, certainty: 0.5, cites: [{source: S4, locator: "Education"}, {source: S6, locator: "1419/20"}], how_known: "Wikipedia + Mainz timeline; Erfurt ID uncertain."}
  early_mathematics: {value: UNKNOWN, how_known: "Arithmetic expected for a patrician son (S4); no documentary detail."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["German"], certainty: 0.5, cites: [{source: S4, locator: "Early life"}], how_known: "Inferred Mainz German; Latin probable later (S4)."}
  notable_events:
    - {value: "Family exile from Mainz amid patrician–guild conflict (c. 1411 / 1413) to Eltville", year: 1411, certainty: 0.5, cites: [{source: S4, locator: "Early life"}, {source: S6, locator: "around 1428"}], how_known: "Wikipedia; Mainz timeline places a related departure around 1428."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1455", certainty: 0.5, cites: [{source: S1, locator: "para. 5"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No own words survive on science–religion relation (sparse early-modern documentary record)."}
  primary_system: {value: UNKNOWN, how_known: "No first-person profession of faith or theology survives in the sources read (P19 silence). Lead CHRIST only: printed the 42-line Bible and Cypriot indulgences; pension/Hofmann from Archbishop Adolf von Nassau; buried in the Franciscan church at Mainz (S1, S4, S5, S6). Standing rule: Bible/Psalter/indulgence printing and later Aquinas Summa attributions are occupation/client work, not personal theology — do not open CHRIST from craft alone. Kapr's Cusanus liturgical-standardization motivation is an explicit hypothesis, not documentary evidence. Catholicon 1460 colophon God-language is not securely Gutenberg's signed voice (authorship contested; S4). Helmasperger 1455 'In Gottes Namen Amen' is the notary's formula, not Gutenberg (P42)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Lead only: Bible/indulgence printing; archbishop pension; Franciscan burial; Deutsche Biographie 'katholisch'. Not opened as adult profession (standing rule; craft ≠ theology; no first-person)."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "No first-person statement on God/locus survives (P19). Legal/business documents and printed sacred texts do not supply locus (standing rule)."}
    B_cause: {value: UNKNOWN, how_known: "An invention, not a theory of nature (P33); not a scientist (P30). No P16 nature-order statement read."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing first-hand read (P19)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing first-hand read (P19)."}
    E_scope: {value: UNKNOWN, how_known: "Nothing first-hand read (P19)."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus and B_cause are UNKNOWN, so the P4 test cannot be applied (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "D1 2026-10-24: Documentary silence confirmed. Surviving papers are lawsuits, loans, tax/militia lists, and the Helmasperger notarial instrument (business partnership for the 'work of the books') — not diaries or theological letters. Do not force A from Bible printing or archbishop pension. Do not score Helmasperger invocatio or contested Catholicon colophon as own words. Kapr (1996) unread in full this pass; his Cusanus hypothesis noted as blocker, not evidence. Chart-moving NO — leave unplotted. No fallacy_catalog; figures/ untouched."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German (Mainz patrician Gensfleisch)", certainty: 0.7, cites: [{source: S4, locator: "Early life"}, {source: S5, locator: "NDB Genealogy"}], how_known: "Wikipedia + NDB."}
  religious_heritage_by_birth: {value: "Late-medieval Latin (Roman) Catholic", certainty: 0.7, cites: [{source: S5, locator: "Religious Denomination katholisch"}, {source: S4, locator: "Early life / Later life"}, {source: S6, locator: "baptism tradition; Franciscan burial"}], how_known: "Deutsche Biographie denomination 'katholisch'; Mainz parish context; Franciscan church burial. Heritage only — never a worldview code."}
  baptism_or_initiation: {value: "Local tradition: baptized around birth at parish church of St. Christoph, Mainz, often linked to St. John's Day (24 June); no contemporary baptismal register cited", certainty: 0.5, cites: [{source: S4, locator: "Early life note d (Man 2002)"}, {source: S6, locator: "Around 1400"}], how_known: "Mainz city timeline states 'probably baptized' at St. Christoph; Wikipedia notes local tradition without documentary evidence. Not a scored profession."}
  childhood_catechism: {value: UNKNOWN, how_known: "No named catechism or household instruction text in sources read."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1455", certainty: 0.5, cites: [{source: S1, locator: "para. 5"}, {source: S4, locator: "Printed books"}], how_known: "The one listed lasting work, dated by the Bible's completion (P29, P30 #1); alternative 1454."}
  age_at_first_lasting_contribution: {value: 60, certainty: 0.5, cites: [{source: S1, locator: "heading; para. 5"}], how_known: "1455 − 1395 = 60 (P30 year difference); birth year uncertain ('1395?'); alternative about 55 on a birth about 1400."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None — silence (P19)."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None scored."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None scored."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Craft invention of movable type and press (S1, S4); not a geometric cosmology.", certainty: 0.5, cites: [{source: S1, locator: "text"}, {source: S4, locator: "Printing method"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data for a Lane B belief model of nature. Invention ≠ theory (P33)."
  notes: "Do not invent a geometric reading from type design or press mechanics."

institutions: []
collaborators:
  - {value: "Johann Fust", relation: "mentor or employer", note: "financier and partner from c. 1450; Helmasperger instrument 6 Nov 1455; won control of Bible workshop", certainty: 0.7, cites: [{source: S1, locator: "para. 5"}, {source: S3, locator: "Invention of the press"}, {source: S4, locator: "Court case"}], how_known: "Britannica + Wikipedia."}
  - {value: "Peter Schöffer", relation: "collaborator", note: "joined Fust enterprise; Mainz Psalter 1457 under Fust–Schöffer name", certainty: 0.7, cites: [{source: S4, locator: "Printing press / Court case"}], how_known: "Wikipedia."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 189"}], how_known: "Study roster."}
  controversies:
    - {value: "Catholicon (Mainz 1460) often attributed to Gutenberg's shop; modern scholarship divides (Fust–Schöffer vs Gutenberg). Colophon God-language therefore not used as Gutenberg first-person.", certainty: 0.5, cites: [{source: S4, locator: "Court case / Printed books"}, {source: S5, locator: "NDB Catholicon note"}], how_known: "Wikipedia debate; NDB assigns Catholicon fairly securely to Fust–Schöffer."}
    - {value: "Albert Kapr hypothesized a motivational link to Nicholas of Cusa's call for uniform liturgical books; Kapr himself frames it as Vermutung (hypothesis), not documented contact.", certainty: 0.5, cites: [{source: S4, locator: "Sources (Kapr 1996)"}], how_known: "Kapr excerpts / secondary trail; not treated as evidence for CHRIST profession."}
  data_quality_flags:
    - "Birth year uncertain (scholarly range c. 1393–1406)."
    - "No surviving first-person religious or nature statements (sparse early-modern documentary record)."
    - "Baptism at St. Christoph is local tradition without cited register."
  open_questions:
    - "Full Kapr 1996 monograph (English Martin translation) for any overlooked documentary trail on religious life."
    - "Critical edition / full English of Helmasperger instrument for any non-formulaic Gutenberg speech beyond the business dispute."
    - "Whether any Strasbourg or Mainz parish register names Gutenberg as sponsor/godparent (unlikely to yield locus)."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Britannica Editors"
    citation: "'Johannes Gutenberg.' Britannica (students edition). https://kids.britannica.com/students/article/Johannes-Gutenberg/274706"
    url: "https://kids.britannica.com/students/article/Johannes-Gutenberg/274706"
    accessed: 2026-10-24
    reliability_note: "Encyclopedia article, read in full; unsigned students edition."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, timing, collaborators]
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
    author: "Hellmut E. Lehmann-Haupt"
    citation: "Lehmann-Haupt, Hellmut E. 'Johannes Gutenberg.' Encyclopaedia Britannica. https://www.britannica.com/biography/Johannes-Gutenberg"
    url: "https://www.britannica.com/biography/Johannes-Gutenberg"
    accessed: 2026-10-24
    reliability_note: "Signed article (Professor of Bibliography). D1 re-fetch: introduction, Life, Invention of the press through Helmasperger / Fust judgment; punch-matrix revision note. Bible completion date still mainly from S1/S4."
    source_quality: "reference entry"
    used_for: [identity, basics, collaborators]
  - id: S4
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "'Johannes Gutenberg.' Wikipedia (English). https://en.wikipedia.org/wiki/Johannes_Gutenberg"
    url: "https://en.wikipedia.org/wiki/Johannes_Gutenberg"
    accessed: 2026-10-24
    reliability_note: "P50 dual bio with S1. Early life, Education, Printing press, Court case, Later life, Influence read. Notes baptism tradition without documentary evidence; Franciscan burial; Catholicon debate; cites Kapr 1996, Wagner 2000, Füssel 2019."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, collaborators, review]
  - id: S5
    type: tertiary
    kind: "encyclopedia"
    author: "Aloys Ruppel (NDB); Deutsche Biographie authority data"
    citation: "Ruppel, Aloys. 'Gutenberg (eigentlich Gensfleisch zur Laden genannt Gutenberg), Johannes.' Neue Deutsche Biographie 7 (1966), pp. 339–342; Deutsche Biographie entry (Religious Denomination: katholisch). https://www.deutsche-biographie.de/sfz24786.html"
    url: "https://www.deutsche-biographie.de/sfz24786.html?language=en"
    accessed: 2026-10-24
    reliability_note: "National biography; authority data lists denomination katholisch; NDB gives genealogy, Strasbourg/Mainz career, burial Franziskanerkirche, and Catholicon attribution note. Older ADB van der Linde layer is polemical — used only with caution; NDB preferred."
    source_quality: "reference entry"
    used_for: [basics, childhood, worldview, heritage, review]
  - id: S6
    type: tertiary
    kind: "other"
    author: "City of Mainz (Gutenberg microsite)"
    citation: "'Gutenberg and his time in data.' Mainz.de Gutenberg microsite timeline. https://www.mainz.de/en/microsite/gutenberg/zeit/zeitleiste_gutenberg"
    url: "https://www.mainz.de/en/microsite/gutenberg/zeit/zeitleiste_gutenberg"
    accessed: 2026-10-24
    reliability_note: "Municipal chronological digest: baptism tradition St. Christoph; Helmasperger 1455; archbishop pension 1465; death 1468-02-03 Hof zum Algesheimer; Franciscan church burial; 1499 Gelthuß obituary trail."
    source_quality: "other"
    used_for: [basics, childhood, worldview, heritage, review]
---

## Summary

Johannes Gutenberg (c. 1395–1468), printer and inventor of European movable-type printing [S1, S4]. Deepen D1: documentary silence — primary UNKNOWN (CHRIST lead only); A–E UNKNOWN; mid UNKNOWN. Not plotted.

## Life and work

Born Mainz (patrician Gensfleisch); Strasbourg metalwork and early press experiments (1430s–1444); Mainz press and 42-line Bible with Fust (c. 1450–1455); Helmasperger suit 6 Nov 1455; Archbishop Adolf von Nassau pension 1465; died Mainz 3 Feb 1468; buried Franciscan church (grave later lost) [S1, S3, S4, S5, S6].

## Contribution and impact

Movable metal type and press; 42-line Bible (completed by 1455); lasting method for centuries; literacy and print culture impact [S1, S4].

## Childhood and education

Father Friele (mint companion); mother Else Wirich; Hof zum Gutenberg by St. Christoph's; expected patrician literacy/Latin; Erfurt 'Johannes de Altavilla' 1419/20 uncertain [S4, S5, S6].

## Adult working worldview

No first-person religion or nature statements survive. Legal and business papers only. Bible/indulgence printing and archbishop pension are craft and patronage context, not scored profession (standing rule). CHRIST remains lead only; axes UNKNOWN [S1, S4, S5, S6].

## Heritage (context only)

Late-medieval Latin Catholic Mainz; Deutsche Biographie 'katholisch'; local baptism tradition at St. Christoph; Franciscan burial. Context only — never a worldview code [S4, S5, S6].

## Timing

Major work 1455 (Bible), age about 60, or about 55 on birth ~1400 (0.5) [S1, S4]. No LIO-timed views.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Craft invention, not a geometric cosmology (P33). No data.

## Open questions

- Full Kapr 1996 for any overlooked religious documentary trail.
- Critical Helmasperger text for non-formulaic Gutenberg speech.
- Parish register traces (sponsors/godparents) — unlikely to yield locus.

## Research log

- 2026-10-24 (D1): Wikipedia EN (S4); Lehmann-Haupt Britannica re-read (S3); Deutsche Biographie NDB/authority (S5); Mainz timeline (S6). Silence confirmed. Heritage filled. Scores unchanged (UNKNOWN). Chart-moving NO. No fallacy_catalog; no figures/.
- 2026-10-19: AA3 audit fix (v8's call on the auditor's advice): alternative birth about 1400, age about 55. Signed Britannica article (Lehmann-Haupt) added as S3; only part of it was read and it did not confirm the Bible date in the body, so the span stays 0.5.
- 2026-10-19: Read Britannica (students); signed Britannica (Lehmann-Haupt), partly.
