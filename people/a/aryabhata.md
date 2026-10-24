---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z4)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #144, F 3, rank 149). Opened Clark 1930 Chicago University Press PDF/OCR via Internet Archive (S4; TheAryabhatiyaOfAryabhata): confirmed Wikisource readings of Dasagitika A, Gola 47, Gola 49–50; added Ganitapada 1 (Brahman reverence outside the Dasagitika authenticity dispute) and Gola 37 (Moon obscures Sun; Earth's shadow obscures Moon — natural eclipse mechanism). Clark preface defends Dasagitika against Kaye (Brahmagupta quotes stanzas 1, 3, 4, 5); van der Waerden doubt (S1 MacTutor: Introduction later; some verses added) still flagged — which Gola verses he rejects remains unspecified. Shukla/Sarma 1976 English (IA) OCR unusable this pass. primary HINDU stays 0.5; A 1 stays 0.5 alt 2 (support single); B 3 stays 0.5 alt 4 (P35/P16: Gola 37/47 are the natural eclipse account, not a lift past 0.5) but basis inference_from_work → written_profession; support single → corroborated (S4/S2 + S1). mid BELOW_THRESHOLD; plotted faded. P47 source_quality on S1–S4. Chart-moving NO. No figures/; no fallacy_catalog. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z4 audit fixes (blind audit /workspace/genius_study_audit/gs_a19c474_Z4/run1/): B basis now inference_from_work (P24; ceiling unchanged); statements verified_against 'scholarly edition' (Clark's translation read directly, not a secondary quotation); coder_notes add the Gola 49–50 condition. RQ-Z4-1: invocation carries primary and A at 0.5. Values unchanged."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z4, order P32: F 3, rank 149). Basics from MacTutor (O'Connor and Robertson). Own words from the Aryabhatiya in W. E. Clark's translation (1930) via Wikisource: Dasagitika opening invocation ('Having paid reverence to Brahman, who is one ... many ..., the true deity, the Supreme Spirit'; Clark's parenthetical glosses not counted), Gola 47 (natural account of a solar eclipse), Gola 49 ('By the grace of God'), Gola 50 (astronomy 'formerly was revealed by Svayambhu'). Van der Waerden doubts the Dasagitika's authenticity (MacTutor), so the invocation is flagged. A scientist (P30: astronomy). Span 499. Age 23 from his own statement. primary_system HINDU (0.5); A 1 (0.5, alt 2); B 3 (0.5, alt 4; P35); C, E UNKNOWN; D BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Plotted (faded). Draft, not reviewed."}

identity:
  id: aryabhata
  display_name: "Aryabhata"
  roster:
    canonical_name: "Aryabhata"
    rank: 149
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Aryabhata", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "MacTutor (Aryabhata I)."}
  native_name: {value: "Āryabhaṭa", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Standard transliteration."}
  aliases:
    - {name: "Aryabhata I", kind: "other"}

basics:
  birth:
    date: {value: "0476", calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "text (aged 23 in 499)"}], how_known: "From his own statement that he was 23 at 3600 years of the Kali age (499)."}
    place: {value: "Kusumapura (uncertain; Asmaka proposed)", modern_name: "Patna, Bihar, India (uncertain)", polity_then: "Gupta Empire", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "MacTutor: 'numerous other places proposed'."}
  death:
    date: {value: "0550", calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "MacTutor heading; conventional."}
    place: {value: UNKNOWN, how_known: "Not stated."}
  first_lasting_contribution_year: {value: 499, certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Aryabhatiya, written in 499 at age 23."}
  era_bucket: {value: "-500 to 499", certainty: 1.0, cites: [{source: S1, locator: "text"}], how_known: "499 (P2)."}
  region_of_birth: {value: "South Asia", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "India (P3), whichever birthplace."}
  region_of_work: {value: "South Asia", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Kusumapura."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Sanskrit"], certainty: 0.7, cites: [{source: S2, locator: "title page"}], how_known: "Sanskrit verse."}
  occupations: {value: ["astronomer", "mathematician"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "MacTutor."}

contribution:
  fields: {value: ["astronomy", "mathematics"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "MacTutor."}
  lasting_original_contributions:
    - {value: "Aryabhatiya", year: 499, kind: work, lasting: "place-value arithmetic, sine table, axial rotation of the Earth, natural theory of eclipses (S1)", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "MacTutor."}
  evidence_of_impact:
    - {value: "Correctly explained eclipses against the earlier belief in the demon Rahu", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "MacTutor."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founding figure of classical Indian astronomy (S1).", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household: []
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
  working_years: {value: "499", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Astronomy 'formerly was revealed by Svayambhu' and rescued 'by means of the boat of my own knowledge'", certainty: 0.5, cites: [{source: S4, locator: "Gola 49–50"}], how_known: "Clark 1930 (S4 IA PDF/OCR; matches Wikisource S2)."}
  primary_system:
    value: HINDU
    basis: written_profession
    certainty: 0.5
    cites: [{source: S4, locator: "Dasagitika A; Ganitapada 1; Gola 49–50"}]
    how_known: "Dasagitika A Brahman as 'the true deity, the Supreme Spirit'; Ganitapada 1 'Having paid reverence to Brahman' (outside Dasagitika); Gola 49 'By the grace of God'; Gola 50 Svayambhu as revealer (S4=S2 Clark). Van der Waerden doubts Dasagitika authenticity and some added verses (S1); which Gola verses he rejects is unspecified, so 0.5 held."
    rationale: "HINDU (Brahmanical): Brahman invocations and Svayambhu. Alternative BELOW_THRESHOLD if Dasagitika and Gola 49–50 were both set aside as later; Ganitapada 1 alone is a thin mangala."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: HINDU, reason: "Coded at 0.5."}
  lio_axes:
    A_locus:
      value: 1
      basis: written_profession
      certainty: 0.5
      support: single
      cites: [{source: S4, locator: "Dasagitika A; Gola 49"}]
      how_known: "Clark 1930 Chicago (S4 IA PDF/OCR; matches Wikisource S2, same translation so not a second independent source): Dasagitika A Brahman 'one ... many', 'the Supreme Spirit'; Gola 49 'grace of God'. Clark's parentheses (creator / manifestations, after Paramesvara) not counted. Support single (P48). Dasagitika authenticity doubted by van der Waerden (S1). 0.5."
      rationale: "Brahman 'one ... many', 'the Supreme Spirit', with 'the grace of God': a supreme deity with some immanence. Alternative 2: one-and-many read as panentheist. Ganitapada 1 Brahman reverence is outside the Dasagitika dispute but too thin alone to lift certainty."
      alternatives:
        - {value: 2, note: "One and many as panentheism.", cites: [{source: S4, locator: "Dasagitika A"}]}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S4, locator: "Gola 37; Gola 47"}, {source: S1, locator: "text (eclipses vs Rahu)"}]
      how_known: "Own words in Clark 1930 (S4/S2): Gola 37 — Moon obscures the Sun; Earth's shadow obscures the Moon; Gola 47 — partial solar eclipse not perceptible from brightness/transparency. MacTutor (S1) corroborates natural eclipse theory against Rahu. Scientist (P30 astronomy). Independent sources → corroborated (P48). Certainty stays 0.5: P35/P16 — natural eclipse account alone does not lift B to 0.7."
      rationale: "P35/P16: working science and the natural eclipse mechanism (Gola 37/47) score B 3 at 0.5 with named alternative 4; no explicit cause talk beyond that account."
      alternatives:
        - {value: 4, note: "P35 alternative.", cites: [{source: S1, locator: "text"}, {source: S4, locator: "Gola 37"}]}
    C_ledger: {value: UNKNOWN, how_known: "Gola 50 (disparager 'loses his good deeds and his long life') is a conventional curse, not scored."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "Gola 50 says astronomy was revealed by Svayambhu, Gola 49 that he rescued it by his own knowledge; no ranking stated."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 1 and B 3 both at 0.5, under the 0.7 bar (§6, P19)."}
  statements:
    - text: "Having paid reverence to Brahman, who is one (in causality, as the creator of the universe, but) many (in his manifestations), the true deity, the Supreme Spirit, Aryabhata sets forth three things: mathematics"
      cites: [{source: S4, locator: "Dasagitika A (p. 1 Clark)"}, {source: S2, locator: "Dasagitika 1"}]
      date: "499"
      context: "Opening invocation; parentheses are Clark's gloss after Paramesvara. Authenticity of the Dasagitika doubted by van der Waerden (S1); Clark (preface) defends the section against Kaye via Brahmagupta quotations."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
    - text: "Having paid reverence to Brahman, the Earth, the Moon, Mercury, Venus, the Sun, Mars, Jupiter, Saturn, and the asterisms, Aryabhata sets forth here [in this work] the science which is honored at Kusumapura."
      cites: [{source: S4, locator: "Ganitapada 1 (p. 21 Clark)"}]
      date: "499"
      context: "Opening of the Mathematics section — outside the Dasagitika authenticity dispute. Thin mangala (Brahman listed with planets); supports HINDU/A at 0.5 but does not lift certainty alone."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
    - text: "The Moon consists of water, the Sun of fire, the Earth of earth, and the Earth's shadow of darkness. The Moon obscures the Sun and the great shadow of the Earth obscures the Moon."
      cites: [{source: S4, locator: "Gola 37"}]
      date: "499"
      context: "Natural eclipse mechanism (shadow), against the demon Rahu (S1). Core B evidence; P35 keeps certainty at 0.5."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
    - text: "When the Moon eclipses the Sun even though an eighth part of the Sun is covered this is not preceptible because of the brightness of the Sun and the transparency of the Moon."
      cites: [{source: S4, locator: "Gola 47"}, {source: S2, locator: "Gola 47"}]
      date: "499"
      context: "Partial eclipse perceptibility (spelling as in the Wikisource text; confirmed in S4 OCR)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
    - text: "By the grace of God the precious sunken jewel of true knowledge has been rescued by me, by means of the boat of my own knowledge, from the ocean which consists of true and false knowledge."
      cites: [{source: S4, locator: "Gola 49"}, {source: S2, locator: "Gola 49"}]
      date: "499"
      context: "Closing verses, Clark translation (S4 OCR matches S2)."
      axes: [A_locus, D_authority]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
    - text: "He who disparages this universally true science of astronomy, which formerly was revealed by Svayambhu, and is now described by me in this Aryabhatiya, loses his good deeds and his long life."
      cites: [{source: S4, locator: "Gola 50"}, {source: S2, locator: "Gola 50"}]
      date: "499"
      context: "Closing; Svayambhu as revealer (D not scored — no ranking). Conventional curse on disparagers not scored for C."
      axes: [A_locus, D_authority]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
  changes_over_life: []
  coder_notes: "Dasagitika authenticity (van der Waerden via S1) bears on primary and A; RQ-Z4-1 holds them at 0.5. Clark 1930 preface defends Dasagitika against Kaye (Brahmagupta quotes), but van der Waerden's later argument (Introduction written later; some verses added) is a separate doubt — MacTutor does not name which Gola verses. Ganitapada 1 Brahman reverence is outside Dasagitika but thin. Gola 37 strengthens B evidence as written_profession; P35/P16 keep B at 0.5. Chart stays faded / hollow (A single, both axes 0.5)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "499", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "The Aryabhatiya, the only lasting work (P29, P30)."}
  age_at_first_lasting_contribution: {value: 23, certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "His own statement; 499 − 476 = 23."}
  first_evidence_of_lio_type_views: {value: "499", certainty: 0.5, cites: [{source: S2, locator: "Dasagitika 1"}], how_known: "Only work."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.5, cites: [{source: S2, locator: "Dasagitika 1"}], how_known: "Same work."}
  worldview_during_major_work: {value: "HINDU", certainty: 0.5, cites: [{source: S2, locator: "Dasagitika 1"}], how_known: "Invocation."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Verse rules for computation, not proofs (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not stated."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions: []
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 149"}], how_known: "Study roster."}
  controversies:
    - {value: "Authenticity of the Dasagitika introduction and some added verses (van der Waerden); Clark 1930 defends Dasagitika against Kaye", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S4, locator: "preface pp. xi–xii"}], how_known: "MacTutor (van der Waerden); Clark preface (vs Kaye / Brahmagupta quotes)."}
  data_quality_flags:
    - "Dasagitika authenticity doubted (van der Waerden); which Gola verses he rejects unspecified."
    - "Shukla/Sarma 1976 English critical edition not usable this pass (IA OCR garbage)."
  open_questions:
    - "Which verses van der Waerden takes as later additions (esp. whether Gola 49–50)."
    - "Shukla/Sarma 1976 English translation when a clean text is available."
    - "Sanskrit text of Dasagitika A, Ganitapada 1, Gola 37/47/49–50."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "J. J. O'Connor and E. F. Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Aryabhata I.\" MacTutor History of Mathematics Archive, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Aryabhata_I/"
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Aryabhata_I/"
    accessed: 2026-10-24
    reliability_note: "Signed biographical archive; cites van der Waerden on Dasagitika layout/authenticity."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, worldview, timing, lane_b, review]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Aryabhata, tr. Walter Eugene Clark"
    citation: "Aryabhata. The Aryabhatiya of Aryabhata, tr. W. E. Clark (Chicago, 1930), via Wikisource. https://en.wikisource.org/wiki/The_Aryabhatiya_of_Aryabhata"
    url: "https://en.wikisource.org/wiki/The_Aryabhatiya_of_Aryabhata"
    accessed: 2026-10-24
    reliability_note: "Public-domain translation, web transcription; readings confirmed against S4 book OCR."
    source_quality: "unofficial web copy"
    used_for: [basics, worldview, timing]
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
    kind: "published work by the subject"
    author: "Aryabhata, tr. Walter Eugene Clark"
    citation: "Aryabhata. The Aryabhatiya of Aryabhata: An Ancient Indian Work on Mathematics and Astronomy, tr. Walter Eugene Clark (University of Chicago Press, 1930). Internet Archive TheAryabhatiyaOfAryabhata (PDF/OCR)."
    url: "https://archive.org/details/TheAryabhatiyaOfAryabhata"
    accessed: 2026-10-24
    reliability_note: "Scholarly translation of the Sanskrit treatise; IA PDF OCR used this pass (Dasagitika A, Ganitapada 1, Gola 37/47/49–50, preface on authenticity vs Kaye)."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, timing, review]
---

## Summary

Aryabhata (476–c. 550), astronomer and mathematician [S1]. Draft: HINDU (0.5); A 1 (0.5, alt 2); B 3 (0.5, alt 4). Plotted (faded).

## Life and work

Kusumapura; the Aryabhatiya of 499 [S1].

## Contribution and impact

Place value, sines, Earth's rotation, eclipses [S1].

## Childhood and education

Not known.

## Adult working worldview

Invocation of Brahman (Dasagitika A; also Ganitapada 1 mangala); astronomy revealed by Svayambhu and rescued by his own knowledge; natural eclipse by the Earth's shadow [S4, S2].

## Heritage (context only)

Not known.

## Timing

499, age 23 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Which verses van der Waerden takes as later additions (esp. Gola 49–50).
- Shukla/Sarma 1976 English when clean text is available.
- Sanskrit text of key verses.

## Research log

- 2026-10-24: Deepen D1 — Clark 1930 Chicago via IA PDF/OCR (S4); MacTutor re-read for van der Waerden scope; Shukla/Sarma 1976 IA OCR unusable. Codes held; B basis → written_profession; support A single / B corroborated. Chart-moving NO.
- 2026-10-19: Read MacTutor; Clark translation on Wikisource.
