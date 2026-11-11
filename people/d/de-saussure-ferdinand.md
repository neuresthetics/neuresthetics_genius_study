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
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #159, F 3, rank 167). Needs: hunt own-voice; keep UNKNOWN if silent; do not force plot. Hunted Course in General Linguistics (Baskin / archive.org OCR of student-note compilation, S6): Dieu and religion appear only as linguistic examples (mordieu etymology; 'Dieu est bon' syntagm) or as ethnic/civilizational context — not a personal creed; CLG is editors' reconstruction from student notes, not a book in his hand. Hutton & Joseph 1998 (S7) print his 29 Jul 1907 Journal de Genève review of Oltramare (La théosophie brahmanique): own words distinguishing scholarly Indian 'theosophy' from Blavatsky occultism — clears the create-note theosophy lead as scholarly interest, not a belief code. EPHE prosopo (S5) and Wikipedia (S4, P50 with Britannica): Genevan Protestant aristocracy / Calvinist heritage confirmed as context only. No baptism or parish profession found for him. Joseph OUP 2012 still unread in full (family crisis 'economic and religious reasons' remains a review lead). Not a scientist (P30; Lévi-Strauss). primary/A/B/C/D/E/mid stay UNKNOWN; CHRIST heritage lead only. Not plotted. P47 source_quality on S1–S7. Chart-moving NO. No fallacy_catalog. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z8, order P32: F 3, rank 167). Source: Britannica (body). No own words on religion read; Calvinist Genevan family per a review of Joseph's biography (S3, context only). Not a scientist (linguistics as social and interpretive theory; Lévi-Strauss precedent, Z6). primary_system UNKNOWN (lead CHRIST, heritage only); A, B, C, D, E UNKNOWN; mid_basin UNKNOWN. Span 1878–1911, age 21. Not plotted. Draft, not reviewed."}

identity:
  id: de-saussure-ferdinand
  display_name: "Ferdinand de Saussure"
  roster:
    canonical_name: "Ferdinand de Saussure"
    rank: 167
    F: 3
    models: [Claude, DeepSeek, GPT]
    band: "core (3–4)"
    status: "core"
    field: "linguistics"
    field_bucket: "linguistics"
  full_name: {value: "Ferdinand Mongin de Saussure", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lead"}], how_known: "Britannica short form Ferdinand de Saussure; Wikipedia gives Ferdinand Mongin de Saussure (P50)."}
  native_name: {value: "Ferdinand de Saussure", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lead"}], how_known: "Usual French form; Britannica and Wikipedia agree (P50)."}
  aliases:
    - {name: "Ferdinand-de-Saussure", kind: "roster alias"}
    - {name: "Ferdinand Mongin de Saussure", kind: "other"}

basics:
  birth:
    date: {value: "1857-11-26", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lead / infobox"}], how_known: "Britannica and Wikipedia agree (P50)."}
    place: {value: "Geneva", modern_name: "Geneva, Switzerland", polity_then: "Switzerland", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "Biography"}], how_known: "Britannica and Wikipedia agree (P50)."}
  death:
    date: {value: "1913-02-22", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lead"}], how_known: "Britannica and Wikipedia agree (P50)."}
    place: {value: "Vufflens-le-Château", modern_name: "Vufflens-le-Château, Switzerland", polity_then: "Switzerland", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "Biography"}], how_known: "Britannica and Wikipedia agree (P50); EPHE: Vufflens (S5)."}
  first_lasting_contribution_year: {value: 1878, certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Mémoire sur le système primitif des voyelles (1878), 'a brilliant contribution to comparative linguistics'."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "body"}], how_known: "1878 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Switzerland (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Paris 1881–91; Geneva 1891–1913."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["French"], certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "French works."}
  occupations: {value: ["linguist", "professor"], certainty: 0.7, cites: [{source: S1, locator: "opening; body"}], how_known: "Britannica."}

contribution:
  era_bucket: 19c
  fields: {value: ["linguistics", "Indo-European studies"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Mémoire sur le système primitif des voyelles dans les langues indo-européennes", year: 1878, kind: "theory", lasting: "'established his reputation with a brilliant contribution to comparative linguistics' (S1)", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Britannica."}
    - {value: "Structural linguistics (langue/parole, synchrony/diachrony) in the Geneva lectures, published as the Cours de linguistique générale", year: 1907, kind: "theory", lasting: "'considered the starting point of 20th-century structural linguistics' (S1)", certainty: 0.5, cites: [{source: S1, locator: "body"}], how_known: "Britannica: general-linguistics lectures 1907–11 (P12 start 1907); the Cours was compiled from students' notes and printed in 1916, after his death, so the span ends at 1911 (P30)."}
  evidence_of_impact:
    - {value: "Ideas on structure in language laid the foundation for much of 20th-century linguistics", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Cours de linguistique générale (posthumous, ed. Bally and Sechehaye)", year: 1916, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Britannica."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founder of structural linguistics (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Calvinist / Reformed Protestant (Genevan patrician)", certainty: 0.7, cites: [{source: S3, locator: "Part I"}, {source: S5, locator: "Origines familiales"}], how_known: "Anuario review of Joseph: 'orígenes ginebrinos calvinistas'; EPHE: 'aristocratie protestante de Genève' / cité de Calvin. Heritage context only — not his adult profession."}
  family_religious_practice: {value: UNKNOWN, how_known: "No catechism or parish practice stated for his childhood."}
  parents_and_household:
    - {value: "Henri Louis Frédéric de Saussure (father), mineralogist / entomologist", role: father, certainty: 0.7, cites: [{source: S4, locator: "Biography"}, {source: S5, locator: "Origines familiales"}], how_known: "Wikipedia and EPHE."}
    - {value: "Louise de Pourtalès (mother), Countess", role: mother, certainty: 0.7, cites: [{source: S5, locator: "Origines familiales"}], how_known: "EPHE."}
  household_circumstances: {value: "Genevan patrician scientific family; summer seat at Château de Vufflens", certainty: 0.5, cites: [{source: S4, locator: "Biography"}, {source: S5, locator: "Origines familiales"}], how_known: "Secondary biographies; not used for worldview."}
  schooling:
    - {value: "Institution Martine (Geneva)", stage: "grammar or secondary school", years: "from 1870", certainty: 0.7, cites: [{source: S4, locator: "Biography"}], how_known: "Wikipedia."}
    - {value: "Collège de Genève / Gymnase", stage: "grammar or secondary school", years: "c. 1872", certainty: 0.5, cites: [{source: S4, locator: "Biography"}], how_known: "Wikipedia (his complaint of a wasted year)."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated (classical languages at school later)."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1878–1911", certainty: 0.5, cites: [{source: S1, locator: "body"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No own-voice statement found (P19)."}
  primary_system: {value: UNKNOWN, how_known: "No own words scoring a belief system (P19). Lead CHRIST (Calvinist) remains heritage only (S3/S5); not a worldview code. 1907 Oltramare review (S7) is scholarly theosophy, not a creed. Joseph's interpretive 'Calvinist linguistics' is historiography, not his profession."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Lead only: Calvinist Genevan family (S3/S5); heritage context, not opened as primary_system."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "No own-voice locus statement (P19). CLG (S6) uses Dieu/Church only as linguistic or ethnic examples; 1907 Oltramare review (S7) is scholarly classification, not a God-locus claim."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist: linguistics here is social and interpretive theory of language, not testable claims about natural systems (P30; Lévi-Strauss, Z6). No statement on nature found in CLG hunt or secondary bios."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing found."}
    D_authority: {value: UNKNOWN, how_known: "Nothing found."}
    E_scope: {value: UNKNOWN, how_known: "Nothing found."}
  mid_basin: {value: UNKNOWN, how_known: "A and B are UNKNOWN (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: >-
    Deepen D1 non-scoring leads: (1) CLG (S6, Baskin; editors Bally/Sechehaye from
    student notes): mordieu < mort Dieu; example sentence 'Dieu est bon'; religion
    as ethnic/civilizational bond — institutional/semiotic, not creed. (2) Journal de
    Genève 29 Jul 1907 review of Oltramare (quoted in Hutton & Joseph 1998, S7):
    distinguishes scholarly Indian 'théosophie' from Blavatsky occultism; clears
    create-note theosophy interest as scholarly, not a belief code. (3) Flournoy /
    Hélène Smith mediumship: linguistic observation context in S7, not conversion.
    (4) Literary Review / NBN portrayals of 'austere Calvinist intellectual' or
    'aristocrat with a Calvinist upbringing' are biographer framing. Joseph OUP 2012
    full text still unread (family crisis 'for economic and religious reasons' per
    Anuario S3 remains a review lead). Une vie en lettres (2014) not mined.

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Genevan patrician family (from Lorraine Saulxures; Protestant refugees)", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "Part I"}, {source: S5, locator: "Origines familiales"}], how_known: "Britannica; Anuario/Joseph; EPHE."}
  religious_heritage_by_birth: {value: "Calvinist (Reformed Protestant)", certainty: 0.7, cites: [{source: S3, locator: "Part I"}, {source: S5, locator: "Origines familiales"}], how_known: "Anuario review of Joseph; EPHE 'aristocratie protestante' / cité de Calvin. Context only."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "No baptism record found for him in sources read."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1878–1911", certainty: 0.5, cites: [{source: S1, locator: "body"}], how_known: "Mémoire (1878) to the last Geneva general-linguistics lectures (1907–11, range end; P29, P30)."}
  age_at_first_lasting_contribution: {value: 21, certainty: 0.7, cites: [{source: S1, locator: "opening; body"}], how_known: "1878 − 1857 = 21 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Linguistic system theory; no proof form (S1).", certainty: 0.5, cites: [{source: S1, locator: "body"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "École pratique des Hautes Études, Paris", role: "instructor", years: "1881–1891", kind: "university", certainty: 0.7, cites: [{source: S1, locator: "body"}, {source: S5, locator: "Carrière"}], how_known: "Britannica; EPHE (grammaire comparée)."}
  - {value: "University of Geneva", role: "professor", years: "1891–1913", kind: "university", certainty: 0.7, cites: [{source: S1, locator: "body"}, {source: S5, locator: "Carrière"}], how_known: "Britannica and EPHE; general-linguistics lectures 1907–11."}
collaborators:
  - {value: "Charles Bally", relation: "student or assistant", note: "co-editor of the Cours", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Britannica."}
  - {value: "Albert Sechehaye", relation: "student or assistant", note: "co-editor of the Cours", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 167"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "No own words scoring religion after CLG and Oltramare-review hunt."
    - "CLG is a student-note / editorial reconstruction (1916), not a book in his hand."
    - "Joseph OUP 2012 full biography still unread."
  open_questions:
    - "Joseph, Saussure (OUP 2012) full text for private letters and the family crisis 'for economic and religious reasons'."
    - "Une vie en lettres, 1866–1913 (Mejía Quijano ed., 2014) for any creed wording."
    - "Baptism or parish register for Ferdinand personally (Lane A)."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Britannica Editors"
    citation: "'Ferdinand de Saussure.' Encyclopaedia Britannica. https://www.britannica.com/biography/Ferdinand-de-Saussure"
    url: "https://www.britannica.com/biography/Ferdinand-de-Saussure"
    accessed: 2026-10-19
    reliability_note: "Unsigned editorial article; body cited (P26). 403 on re-fetch 2026-10-24; earlier create read kept; dual-bio with Wikipedia (P50)."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, worldview, heritage, timing, lane_b, institutions, collaborators]
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
    type: secondary
    kind: "other"
    author: "Anuario Filosófico (reviewer)"
    citation: "Review of John E. Joseph, Saussure (Oxford University Press, 2012). Anuario Filosófico 45/3 (2012), pp. 681–684. https://doi.org/10.15581/009.45.1104"
    url: "https://doi.org/10.15581/009.45.1104"
    accessed: 2026-10-19
    reliability_note: "Book review summarising a scholarly biography; heritage context only. PDF blocked by journal challenge on re-fetch 2026-10-24; create-pass content retained."
    source_quality: "other"
    used_for: [childhood, worldview, heritage]
  - id: S4
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. \"Ferdinand de Saussure.\" Wikipedia, English. https://en.wikipedia.org/wiki/Ferdinand_de_Saussure (rev. 1374534704, 2026-09-12)."
    url: "https://en.wikipedia.org/wiki/Ferdinand_de_Saussure"
    accessed: 2026-10-24
    reliability_note: "P50 dual bio with Britannica. Silent on personal creed; biography and Mongin full name used. Category labels ignored for coding."
    source_quality: "reference entry"
    used_for: [identity, basics, childhood, institutions]
  - id: S5
    type: tertiary
    kind: "encyclopedia"
    author: "Dictionnaire prosopographique de l'EPHE"
    citation: "'Ferdinand de Saussure.' Dictionnaire prosopographique de l'EPHE. https://prosopo.ephe.psl.eu/ferdinand-de-saussure"
    url: "https://prosopo.ephe.psl.eu/ferdinand-de-saussure"
    accessed: 2026-10-24
    reliability_note: "Scholarly prosopography; Protestant Genevan aristocracy and career dates. Heritage context only."
    source_quality: "reference entry"
    used_for: [basics, childhood, heritage, institutions]
  - id: S6
    type: secondary
    kind: "scholarly book"
    author: "Ferdinand de Saussure (lectures); Charles Bally and Albert Sechehaye (eds.); Wade Baskin (trans.)"
    citation: "Saussure, Ferdinand de. Course in General Linguistics. Ed. Charles Bally and Albert Sechehaye; trans. Wade Baskin. New York: Philosophical Library / later reprints. Archive.org OCR (courseingenerall00saus)."
    url: "https://archive.org/details/courseingenerall00saus"
    accessed: 2026-10-24
    reliability_note: "Posthumous compilation from student notes (1916 French); not a book in Saussure's hand. Used only for negative hunt (Dieu/religion as linguistic examples). OCR of Baskin translation."
    source_quality: "scholarly reconstruction"
    used_for: [worldview]
  - id: S7
    type: secondary
    kind: "journal article"
    author: "Christopher M. Hutton and John E. Joseph"
    citation: "Hutton, Christopher M., and John E. Joseph. 'Back to Blavatsky: the impact of theosophy on modern linguistics.' Language & Communication 18 (1998): 181–204. https://languagelog.ldc.upenn.edu/myl/BackToBlavatsky.pdf"
    url: "https://languagelog.ldc.upenn.edu/myl/BackToBlavatsky.pdf"
    accessed: 2026-10-24
    reliability_note: "Quotes Saussure's Journal de Genève review of Oltramare (29 Jul 1907) at length; scholarly article, not a creed source. Clears theosophy as personal belief."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview]
---

## Summary

Ferdinand de Saussure (1857–1913), linguist [S1, S4]. Deepen D1: all worldview fields UNKNOWN (CHRIST heritage lead only). Not plotted.

## Life and work

Geneva, Leipzig, Paris, Geneva; died at Vufflens-le-Château [S1, S4, S5].

## Contribution and impact

Mémoire (1878); structural linguistics via the Cours (student notes, 1916) [S1].

## Childhood and education

Calvinist Genevan patrician family (heritage only) [S3, S5]; Institution Martine / Collège de Genève [S4].

## Adult working worldview

No own-voice creed found. CLG uses Dieu only linguistically [S6]. 1907 Oltramare review is scholarly theosophy, not belief [S7]. primary_system / A–E / mid UNKNOWN.

## Heritage (context only)

Calvinist / Reformed Protestant Genevan aristocracy [S3, S5]. Not a worldview code.

## Timing

1878–1911, age 21 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Joseph OUP 2012 full text; Une vie en lettres (2014); personal baptism register.

## Research log

- 2026-10-19: Read Britannica; a review of Joseph.
- 2026-10-24 (deepen D1, queue #159): Wikipedia EN (P50, rev 1374534704); EPHE prosopo; CLG Baskin OCR (Dieu/religion hunt negative for creed); Hutton & Joseph 1998 Oltramare/Blavatsky quotes; Literary Review / NBN Calvinist-upbringing framing (biographer only); Britannica 403 on re-fetch. Kept all worldview UNKNOWN. P47 on S1–S7. No fallacy_catalog. No figures/.
