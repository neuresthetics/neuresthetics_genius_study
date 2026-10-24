---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z5)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #146, F 3, rank 152). Opened Sharma et al. Brahmasphutasiddhanta Sanskrit–Hindi (IA Brahmasphutasiddhanta, S4) Goladhyaya: verses naming Varahamihira, Srishena, Aryabhata, Vishnucandra; lokaviruddham … veda-smriti-samhita-bahyam; Rahu-caused eclipses defended so homa/japa/snana fruits stand; sruti/samhita/smriti agreement; then shadow-diameter reconciliation. Al-Biruni's 'first chapter' is Goladhyaya (ch. 21), not madhyama ch. 1. Sengupta Khandakhadyaka (S5) opened: computational, no Rahu/Veda profession. Sachau LIX re-read (S2). primary HINDU 0.5→0.7; B 2 0.5→0.7 support corroborated (S2+S4; sincerity alt BELOW and P35 alt 3 remain, contested caps ≤0.7); D 1 0.5→0.7; A stays BELOW_THRESHOLD (no locus of the sacred in Sanskrit or Sachau). mid BELOW; not plotted. P47 source_quality on S1–S5. Chart-moving NO. No figures/; no fallacy_catalog. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z5 audit fixes (Z5-10, Z5-11; RQ-Z5-1 answered: B 2 and D 1 stand at 0.5): al-Biruni's sincerity doubt named as an alternative (BELOW_THRESHOLD) under B and D, quoting Sachau vol. 2 p. 110 ('simply in order to mock them, or under the compulsion of some mental derangement') and p. 112 ('a calamitous fate, like that of Socrates'); S2 cites now give pp. 110–112 (the margin 'Page 256/257' is the Arabic page). Values unchanged; not plotted."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z5, order P32: F 3, rank 152). Basics from MacTutor (O'Connor and Robertson). Own words: Brahmasphutasiddhanta ch. 1 as quoted by al-Biruni (India, c. 1030, ch. LIX) in Sachau's English (1888, vol. 2, archive.org scan): the Head (Rahu) eclipses; 'The Veda, which is the word of God from the mouth of Brahman, says that the Head eclipses'; Aryabhata and others oppose this 'from enmity against the just-mentioned dogma'; 'everything which is in the Veda, Smriti, and Samhita is true'. A translation of an Arabic rendering, and al-Biruni suggests he may have spoken under compulsion or to mock, so 0.5. A scientist (P30: astronomy), but his own words override the P35 default. Span 628 (first ten chapters' version; Khandakhadyaka 665 not called lasting). primary_system HINDU (0.5, alt BELOW_THRESHOLD); A BELOW_THRESHOLD; B 2 (0.5, alt 3); C, E UNKNOWN; D 1 (0.5, alt 0); mid_basin BELOW_THRESHOLD. Not plotted (no A). Draft, not reviewed."}

identity:
  id: brahmagupta
  display_name: "Brahmagupta"
  roster:
    canonical_name: "Brahmagupta"
    rank: 152
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Brahmagupta", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "MacTutor."}
  native_name: {value: "Brahmagupta", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "MacTutor."}
  aliases: []

basics:
  birth:
    date: {value: "0598", calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "Biography (Khandakhadyaka 665 'when he was 67')"}], how_known: "665 − 67."}
    place: {value: UNKNOWN, how_known: "Not stated (he wrote at Bhillamala)."}
  death:
    date: {value: "0670", calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "heading"}], how_known: "MacTutor heading; conventional."}
    place: {value: UNKNOWN, how_known: "Not stated."}
  first_lasting_contribution_year: {value: 628, certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Brahmasphutasiddhanta, 628."}
  era_bucket: {value: "500 to 1399", certainty: 1.0, cites: [{source: S1, locator: "Biography"}], how_known: "628 (P2)."}
  region_of_birth: {value: "South Asia", certainty: 0.5, cites: [{source: S1, locator: "Biography"}], how_known: "India (P3); birthplace not stated."}
  region_of_work: {value: "South Asia", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Bhillamala (Bhinmal); Ujjain."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Sanskrit"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Sanskrit titles."}
  occupations: {value: ["astronomer", "mathematician", "head of the Ujjain observatory"], certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}

contribution:
  fields: {value: ["astronomy", "mathematics"], certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  lasting_original_contributions:
    - {value: "Brahmasphutasiddhanta (rules for zero and negative numbers, quadratic equations)", year: 628, kind: work, lasting: "'understanding of the number systems went far beyond that of others of the period' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  evidence_of_impact:
    - {value: "His works remained the standard in India c. 770–1020 (Sachau)", kind: "scholarly consensus", certainty: 0.5, cites: [{source: S2, locator: "vol. 1, preface xxxvi"}], how_known: "Sachau's preface (vol. 1), via search excerpt."}
  major_works:
    - {value: "Khandakhadyaka", year: 665, kind: book, certainty: 0.7, cites: [{source: S1, locator: "Biography"}, {source: S5, locator: "title page / preface"}], how_known: "MacTutor; Sengupta 1941 edition opened (computational; no Rahu/Veda profession)."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Arithmetic of zero and negatives (S1).", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated (father Jisnugupta)."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Jisnugupta, father", role: father, certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "628", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Astronomers must 'cease to oppose the generality, for everything which is in the Veda, Smriti, and Samhita is true' (Sachau); Sanskrit: lokaviruddham … veda-smriti-samhita-bahyam", certainty: 0.7, cites: [{source: S2, locator: "vol. 2, ch. LIX, pp. 110–112"}, {source: S4, locator: "Goladhyaya ~v. 39"}], how_known: "Sachau English + Sharma BSS Sanskrit (S4)."}
  primary_system:
    value: HINDU
    basis: written_profession
    certainty: 0.7
    cites: [{source: S4, locator: "Goladhyaya, Rahu/Veda verses (OCR; ~vv. 38–43)"}, {source: S2, locator: "vol. 2, ch. LIX, pp. 110–112"}]
    how_known: "Own Sanskrit in BSS Goladhyaya (S4): veda-smriti-samhita as binding; Rahu eclipses defended against Varahamihira/Aryabhata et al.; sruti/samhita/smriti agreement. Sachau (S2) English of al-Biruni's Arabic matches the substance (al-Biruni mislabels the chapter 'first'). Contested sincerity alt BELOW caps ≤0.7."
    rationale: "HINDU (Brahmanical scripture and rites). Alternative BELOW_THRESHOLD: al-Biruni suggests he spoke under compulsion or in mockery."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: HINDU, reason: "Coded at 0.7."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Sachau (S2) 'word of God from the mouth of Brahman' names a revealer; Sanskrit Goladhyaya (S4) binds Veda/Smriti/Samhita as authorities — still no locus of the sacred (heaven/elsewhere vs immanent). Not lifted."}
    B_cause:
      value: 2
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S4, locator: "Goladhyaya, Rahu verses + preceding shadow/diameter verses"}, {source: S2, locator: "vol. 2, ch. LIX, pp. 110–112"}]
      how_known: "Own Sanskrit (S4 Goladhyaya): Rahu causes both eclipses; Varahamihira, Srishena, Aryabhata, Vishnucandra opposed; same chapter computes shadow/diameters (al-Biruni's point). Sachau (S2) matches. Independent Sanskrit edition + Arabic→English quotation → corroborated (P48). Contested sincerity alt BELOW and P35 alt 3 cap ≤0.7."
      rationale: "Account of nature (P6): eclipses caused by Rahu (personal agent) while shadow geometry is also computed — agent behind a recurring natural event, not limited: B 2. Alternative 3: P35 default for a working astronomer, Rahu as stated exception (same Goladhyaya has the shadow math). Named alternative on sincerity: al-Biruni (pp. 110, 112) — mockery, compulsion, or 'calamitous fate, like that of Socrates' at age thirty; if insincere, B is BELOW_THRESHOLD."
      alternatives:
        - {value: 3, note: "P35 default; Rahu as one stated exception (Goladhyaya also computes shadow eclipses).", cites: [{source: S4, locator: "Goladhyaya shadow/diameter verses"}, {source: S2, locator: "vol. 2, ch. LIX, pp. 110–112"}]}
        - {value: BELOW_THRESHOLD, note: "al-Biruni's sincerity doubt (mockery, compulsion, 'calamitous fate').", cites: [{source: S2, locator: "vol. 2, ch. LIX, pp. 110, 112"}]}
    C_ledger: {value: UNKNOWN, how_known: "Eclipse rites 'rewarded by heavenly bliss' not scored (coder's call)."}
    D_authority:
      value: 1
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S4, locator: "Goladhyaya ~vv. 39–43 (veda-smriti-samhita / sruti agreement)"}, {source: S2, locator: "vol. 2, ch. LIX, pp. 110–112"}]
      how_known: "Sanskrit (S4): what opposes the people is outside Veda/Smriti/Samhita; sruti-samhita-smriti agreement; homa/japa/snana fruits require Rahu-eclipses. Sachau (S2): 'everything which is in the Veda, Smriti, and Samhita is true'; dissenters must cease. Corroborated (P48). Contested sincerity alt BELOW caps ≤0.7."
      rationale: "Revelation outranks the named astronomers on a natural-fact question, while the same chapter still uses observational shadow math. Alternative 0: scripture decides outright. Sincerity alt BELOW if al-Biruni's doubt holds."
      alternatives:
        - {value: 0, note: "Scripture decides the eclipse question outright.", cites: [{source: S4, locator: "Goladhyaya ~vv. 39–43"}, {source: S2, locator: "vol. 2, ch. LIX, pp. 110–112"}]}
        - {value: BELOW_THRESHOLD, note: "al-Biruni's sincerity doubt (mockery, compulsion, 'calamitous fate').", cites: [{source: S2, locator: "vol. 2, ch. LIX, pp. 110, 112"}]}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied."}
  statements:
    - text: "The Veda, which is the word of God from the mouth of Brahman, says that the Head eclipses, likewise the book Smriti, composed by Manu, and the Samhita, composed by Garga the son of Brahman."
      cites: [{source: S2, locator: "vol. 2, ch. LIX, pp. 110–112"}]
      date: "628"
      context: "BSS Goladhyaya as quoted by al-Biruni (c. 1030); Sachau's English. Al-Biruni calls it the 'first chapter' — Sanskrit places the Rahu defence in Goladhyaya (S4)."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Diacritics dropped from the scan. 'Mouth of Brahman' phrasing is al-Biruni's Arabic→English; Sanskrit has veda-smriti-samhita / Garga."
    - text: "Therefore people practise the well-known works of piety, and therefore those authors must cease to oppose the generality, for everything which is in the Veda, Smriti, and Samhita is true."
      cites: [{source: S2, locator: "vol. 2, ch. LIX, pp. 110–112"}]
      date: "628"
      context: "Same Sachau passage; substance matches S4 Goladhyaya (lokaviruddham / veda-smriti-samhita-bahyam; rite fruits)."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
    - text: "lokaviruddham abhihitam veda-smriti-samhita-bahyam / yad evam grahana-phalam gargadyaih samhitasu udayabhihitam"
      cites: [{source: S4, locator: "Goladhyaya ~v. 39 (Sharma IA OCR; sandhi/OCR normalized)"}]
      date: "628"
      context: "BSS Goladhyaya: what is said against the people is outside Veda, Smriti and Samhita; eclipse-fruits taught by Garga etc. in the Samhitas. Follows naming of Varahamihira, Srishena, Aryabhata, Vishnucandra."
      axes: [D_authority, B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "IA djvu OCR of Devanagari; reading cross-checked against variant notes in the same edition and against Sachau's paraphrase."
    - text: "tad-abhave homa-japa-snanadi-phalasya cabhavah / rahukritam grahana-dvayam … siddham idam"
      cites: [{source: S4, locator: "Goladhyaya ~v. 40 (Sharma IA OCR; normalized)"}]
      date: "628"
      context: "Without Rahu-caused eclipses, fruits of homa, japa, bathing etc. would be absent; both eclipses caused by Rahu are established."
      axes: [B_cause, D_authority]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
  changes_over_life: []
  coder_notes: "Al-Biruni sincerity doubt kept as named alt BELOW under B/D/primary (mockery, compulsion, or 'calamitous fate, like that of Socrates'). Sanskrit Goladhyaya shows a sustained multi-verse defence plus shadow math in the same chapter — authenticity of the words is no longer Arabic-only; sincerity remains the open contest. Al-Biruni's 'first chapter' corrected to Goladhyaya (ch. 21)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: "Brahman (per al-Biruni)", certainty: 0.5, cites: [{source: S2, locator: "vol. 2, ch. LIX, pp. 110–112"}], how_known: "Al-Biruni: 'he was one of the Brahmans'."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "628", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Brahmasphutasiddhanta, the lasting work (P29, P30)."}
  age_at_first_lasting_contribution: {value: 30, certainty: 0.5, cites: [{source: S1, locator: "Biography"}], how_known: "628 − 598 = 30 (P30 year difference); al-Biruni also says 'only thirty'."}
  first_evidence_of_lio_type_views: {value: "628", certainty: 0.7, cites: [{source: S4, locator: "Goladhyaya Rahu verses"}, {source: S2, locator: "vol. 2, ch. LIX, pp. 110–112"}], how_known: "BSS Goladhyaya (same work as span)."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S4, locator: "Goladhyaya"}, {source: S2, locator: "vol. 2, ch. LIX, pp. 110–112"}], how_known: "Same work."}
  worldview_during_major_work: {value: "HINDU", certainty: 0.7, cites: [{source: S4, locator: "Goladhyaya"}, {source: S2, locator: "vol. 2, ch. LIX, pp. 110–112"}], how_known: "Sanskrit + Sachau."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Computational rules (S1).", certainty: 0.5, cites: [{source: S1, locator: "Biography"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not stated."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "Biography"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Astronomical observatory at Ujjain", role: head, years: UNKNOWN, kind: "research institute", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
collaborators:
  - {value: "Aryabhata", roster_id: aryabhata, relation: "rival or critic", note: "attacked his eclipse view", certainty: 0.7, cites: [{source: S2, locator: "vol. 2, ch. LIX, pp. 110–112"}], how_known: "Via al-Biruni."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 152"}], how_known: "Study roster."}
  controversies:
    - {value: "Sincerity of his defence of Rahu (al-Biruni)", certainty: 0.7, cites: [{source: S2, locator: "vol. 2, ch. LIX, pp. 110–112"}], how_known: "Al-Biruni."}
  data_quality_flags:
    - "Al-Biruni sincerity doubt (mockery/compulsion) remains a named alternative under B, D, and primary."
    - "Goladhyaya Sanskrit read via IA djvu OCR of Sharma edition (Devanagari OCR noise); no complete published English of these verses opened this pass."
  open_questions:
    - "Clean published English of BSS Goladhyaya Rahu verses (Colebrooke Essays II / Asiatic Researches XII cited in S4 intro not opened as primary this pass)."
    - "Whether later tradition (Bhaskara synthesis of Rahu-as-shadow) should affect reading of Brahmagupta's own B 2."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "J. J. O'Connor and E. F. Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Brahmagupta.\" MacTutor History of Mathematics Archive, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Brahmagupta/"
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Brahmagupta/"
    accessed: 2026-10-19
    reliability_note: "Signed biographical archive."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, timing, lane_b, institutions]
  - id: S2
    type: secondary
    kind: "scholarly book"
    author: "al-Biruni, tr. Edward C. Sachau"
    citation: "Alberuni's India, tr. Edward C. Sachau (London: Trübner, 1888), vol. 2, ch. LIX. Scan: https://archive.org/details/alberunisindiaac02biruuoft"
    url: "https://archive.org/details/alberunisindiaac02biruuoft"
    accessed: 2026-10-24
    reliability_note: "Al-Biruni's quotation in English from Arabic; djvu OCR re-checked pp. 110–112. Mislabels the Rahu defence as BSS 'first chapter' — Sanskrit places it in Goladhyaya (S4)."
    source_quality: "scholarly edition or monograph"
    used_for: [contribution, worldview, heritage, timing, collaborators, review]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [review]
  - id: S4
    type: primary
    kind: "scholarly edition"
    author: "Brahmagupta; ed. Ram Swarup Sharma et al."
    citation: "Brahmasphutasiddhanta (Sanskrit with Hindi Vasana/Vijnana). Chief editor Ram Swarup Sharma. Internet Archive: https://archive.org/details/Brahmasphutasiddhanta (djvu OCR). Goladhyaya Rahu/Veda verses."
    url: "https://archive.org/details/Brahmasphutasiddhanta"
    accessed: 2026-10-24
    reliability_note: "Scholarly Sanskrit–Hindi edition; IA djvu OCR of Devanagari is noisy — readings normalized against variant footnotes and Sachau."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, timing, review]
  - id: S5
    type: primary
    kind: "scholarly edition"
    author: "Brahmagupta; ed. Prabodh Chandra Sengupta"
    citation: "The Khandakhadyaka, an Astronomical Treatise by Brahmagupta, with the commentary of Caturveda Prthudaka Svamin. Ed. Prabodh Chandra Sengupta. Calcutta University, 1941. IA: https://archive.org/details/KhandakhadyakaAnAstronomicalTreatisePrabodhaChandraSengupta"
    url: "https://archive.org/details/KhandakhadyakaAnAstronomicalTreatisePrabodhaChandraSengupta"
    accessed: 2026-10-24
    reliability_note: "Opened this pass; computational handbook — no Rahu/Veda profession found (negative for lifting)."
    source_quality: "scholarly edition or monograph"
    used_for: [contribution, review]
---

## Summary

Brahmagupta (598–c. 670), astronomer and mathematician [S1]. Draft: HINDU (0.7); A BELOW_THRESHOLD; B 2 (0.7, alt 3 / sincerity BELOW); D 1 (0.7, alt 0 / sincerity BELOW). Not plotted (no A).

## Life and work

Bhillamala; Ujjain [S1].

## Contribution and impact

Brahmasphutasiddhanta (628) [S1].

## Childhood and education

Not known.

## Adult working worldview

Defends Rahu and Veda/Smriti/Samhita against Varahamihira, Aryabhata et al. in BSS Goladhyaya [S4]; al-Biruni/Sachau matches and doubts sincerity [S2]. Khandakhadyaka has no parallel profession [S5].

## Heritage (context only)

Brahman [S2].

## Timing

628, age 30 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- See review.open_questions.

## Research log

- 2026-10-19: Read MacTutor; Sachau's al-Biruni vol. 2 ch. LIX.
- 2026-10-24: Deepen D1 — Sharma BSS Goladhyaya Sanskrit (S4 IA OCR); Sengupta Khandakhadyaka (S5); Sachau LIX re-read. primary/B/D lifted 0.5→0.7; A held BELOW; chart-moving NO.
