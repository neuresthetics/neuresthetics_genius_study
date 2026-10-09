---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch C)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-08
  last_updated: 2026-10-08
  change_log:
    - {date: 2026-10-08, by: "Grok Bot", summary: "Record created (stage 3 batch C, order P32). Basics from MacTutor and Britannica (editors); worldview from the Author's Preface of the Algebra in Rosen's 1831 translation (archive.org scan, pp. 1–4), with Rosen's own doubt about the preface noted. Works dated only 'after 813', so first-lasting year, span and age UNKNOWN (P12). primary_system ISLAM 0.7 (written_profession; alternative BELOW_THRESHOLD as a conventional formula); A_locus 0 (0.7); C_ledger 1 (0.5); B BELOW_THRESHOLD (coder's call); D BELOW_THRESHOLD; E UNKNOWN; mid_basin BELOW_THRESHOLD. Draft, not reviewed."}

identity:
  id: al-khwarizmi
  display_name: "Al-Khwarizmi"
  roster:
    canonical_name: "Al-Khwarizmi"
    rank: 4
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Abu Jaʿfar Muḥammad ibn Mūsā al-Khwārizmī", certainty: 0.7, cites: [{source: S1, locator: "heading ('Abu Ja'far Muhammad ibn Musa Al-Khwarizmi')"}, {source: S2, locator: "In full ('Muḥammad ibn Mūsā al-Khwārizmī')"}], how_known: "Two sources; the kunya Abu Jaʿfar is MacTutor's alone."}
  native_name: {value: TODO}
  aliases:
    - {name: "Muhammad ibn Musa al-Khwarizmi", kind: "roster alias"}
    - {name: "Algoritmi", kind: latinized}
    - {name: "Mohammed ben Musa", kind: transliteration}

basics:
  birth:
    date:
      value: "780"
      approx: true
      certainty: 0.5
      cites: [{source: S1, locator: "Quick Info ('about 780')"}, {source: S2, locator: "Born line ('c. 780')"}]
      how_known: "Both sources give an approximate year; approximate, so 0.5."
    place:
      value: "possibly Baghdad"
      modern_name: "Baghdad, Iraq"
      polity_then: "Abbasid Caliphate"
      certainty: 0.5
      cites: [{source: S1, locator: "Quick Info ('possibly Baghdad'); Biography, paragraph 1"}]
      how_known: "MacTutor hedges ('possibly'); Toomer, quoted there, suggests the name may point to Khwarizm, or to forebears from there, with the epithet al-Qutrubbulli pointing to a district near Baghdad. 0.5."
      alternatives:
        - {value: "Khwarizm, south of the Aral Sea", cites: [{source: S1, locator: "Biography, paragraph 1 (Toomer)"}], note: "From the name al-Khwarizmi."}
  death:
    date: {value: "850", approx: true, certainty: 0.5, cites: [{source: S1, locator: "Quick Info ('about 850')"}, {source: S2, locator: "Died line ('c. 850')"}], how_known: "Approximate in both sources, so 0.5."}
    place: {value: UNKNOWN, how_known: "Neither source gives a place of death."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "The Algebra and the astronomical tables are dedicated to the caliph al-Ma'mun, who ruled from 813 (S1), so both are after 813; no source read gives a year (P12: undated items do not set the year)."}
  era_bucket: {value: "500 to 1399", certainty: 1.0, cites: [{source: S1, locator: "Biography (al-Ma'mun from 813)"}, {source: S2, locator: "opening (c. 780–c. 850)"}], how_known: "Any year between 813 and his death about 850 gives the same bucket (P2)."}
  region_of_birth:
    value: "Middle East and North Africa"
    certainty: 0.5
    cites: [{source: S1, locator: "Quick Info ('possibly Baghdad (now in Iraq)')"}]
    how_known: "Iraq is Middle East and North Africa in regions.csv (P3). The birthplace itself is uncertain, so 0.5."
    alternatives:
      - {value: "Central Asia", cites: [{source: S1, locator: "Biography, paragraph 1 (Khwarizm 'in central Asia')"}], note: "If born in Khwarizm (modern Uzbekistan/Turkmenistan)."}
  region_of_work: {value: "Middle East and North Africa", certainty: 1.0, cites: [{source: S1, locator: "Biography (House of Wisdom, Baghdad)"}, {source: S2, locator: "paragraph 2 ('lived in Baghdad')"}], how_known: "Two sources."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S1, locator: "throughout"}, {source: S2, locator: "throughout"}], how_known: "As the sources record it."}
  languages_of_work: {value: [Arabic], certainty: 1.0, cites: [{source: S1, locator: "Biography ('wrote in Arabic')"}, {source: S2, locator: "paragraph 2 (Arabic title)"}], how_known: "Two sources."}
  occupations: {value: ["mathematician", "astronomer", "geographer", "scholar at the House of Wisdom"], certainty: 1.0, cites: [{source: S1, locator: "Biography"}, {source: S2, locator: "opening; paragraph 2"}], how_known: "Two sources."}

contribution:
  fields: {value: ["algebra", "arithmetic", "astronomy", "geography"], certainty: 1.0, cites: [{source: S1, locator: "Summary; Biography"}, {source: S2, locator: "Top Questions; paragraphs 2–4"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Al-Kitāb al-mukhtaṣar fī ḥisāb al-jabr waʾl-muqābala: systematic, demonstrative rules for solving linear and quadratic equations", year: "after 813", kind: work, lasting: "the word 'algebra'; Latin translation in the 12th century; 'the first book to be written on algebra' (S1)", certainty: 1.0, cites: [{source: S1, locator: "Biography (algebra paragraphs)"}, {source: S2, locator: "paragraph 2"}, {source: S3, locator: "Author's Preface, pp. 1–4"}], how_known: "Three sources; dated only by the dedication to al-Ma'mun (caliph from 813)."}
    - {value: "Treatise on Hindu-Arabic numerals and their arithmetic (Algoritmi de numero Indorum)", kind: work, lasting: "introduced Hindu-Arabic numerals to the West; the word 'algorithm'", certainty: 1.0, cites: [{source: S1, locator: "Summary; Biography"}, {source: S2, locator: "paragraph 3"}], how_known: "Two sources; undated."}
    - {value: "Astronomical tables (Sindhind zij), including tables of sines and tangents", kind: "body of work", lasting: "translated into Latin by Adelard of Bath from al-Majriti's revision (S1)", certainty: 1.0, cites: [{source: S1, locator: "Biography (Sindhind zij)"}, {source: S2, locator: "paragraph 4"}], how_known: "Two sources; dated only by the dedication to al-Ma'mun (S1)."}
  evidence_of_impact:
    - {value: "The words 'algebra' and 'algorithm' derive from his book title and his name", kind: "named after them", certainty: 1.0, cites: [{source: S1, locator: "Summary"}, {source: S2, locator: "opening"}], how_known: "Two sources."}
  major_works:
    - {value: "Al-Kitāb al-mukhtaṣar fī ḥisāb al-jabr waʾl-muqābala", kind: book, certainty: 1.0, cites: [{source: S2, locator: "paragraph 2"}, {source: S3, locator: "title page"}], how_known: "Two sources."}
    - {value: "Geography giving latitudes and longitudes for 2402 localities", kind: book, certainty: 0.7, cites: [{source: S1, locator: "Biography (geography)"}], how_known: "MacTutor alone."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Author of the first systematic algebra and the vehicle of Hindu-Arabic numerals to Europe.", certainty: 1.0, cites: [{source: S1, locator: "Summary"}, {source: S2, locator: "opening"}], how_known: "Two sources."}

childhood:
  family_religion:
    value: BELOW_THRESHOLD
    note: "Toomer reads al-Tabari's epithet 'al-Majusi' as meaning that his forebears, and perhaps he in his youth, were Zoroastrians; Rashed says the epithet belongs to a second person, the word 'and' having dropped out of an early copy (S1). Draft judgment (one line): too disputed to score."
    how_known: "BELOW_THRESHOLD under P19: evidence exists but is disputed."
  family_religious_practice: {value: UNKNOWN, how_known: "Not in the sources read."}
  parents_and_household: []
  household_circumstances: {value: UNKNOWN, how_known: "Not in the sources read."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "Not in the sources read."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not in the sources read."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not in the sources read."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: UNKNOWN, how_known: "Equals timing.major_work_period, which is UNKNOWN because no lasting work is dated (P12, P29)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "The preface praises God and the caliph's 'fondness for science, by which God has distinguished' him (S3, p. 3), but says nothing on how science and religion relate."}
  primary_system:
    value: ISLAM
    basis: written_profession
    certainty: 0.7
    cites: [{source: S3, locator: "Author's Preface, pp. 1–2, 4"}, {source: S1, locator: "Biography, paragraph 1 (Toomer: 'an orthodox Muslim')"}]
    how_known: "His own published preface: praise of God who 'sent Mohammed ... with the mission of a prophet', 'besides whom there is no God', blessing on 'Mohammed the Prophet and on his descendants' (S3, pp. 1–2). A named alternative, so 0.7."
    rationale: "Draft judgment (one line): ISLAM at 0.7. Named alternative: BELOW_THRESHOLD, because a pious opening was a conventional formula for a book dedicated to the caliph and says little about his working metaphysics. Toomer reads it as showing 'an orthodox Muslim' (S1)."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: ISLAM, reason: "Coded at 0.7 on the preface (S3, pp. 1–4). Against: possibly a conventional formula.", cites: [{source: S3, locator: "pp. 1–4"}]}
    - {code: ZORO, reason: "Rejected: rests on the epithet 'al-Majusi', which Toomer applies only to his forebears and Rashed to another person (S1).", cites: [{source: S1, locator: "Biography, paragraph 1"}]}
  lio_axes:
    A_locus:
      value: 0
      basis: written_profession
      certainty: 0.7
      cites: [{source: S3, locator: "Author's Preface, pp. 1–2, 4"}]
      how_known: "His own published preface; a named alternative, so 0.7."
      rationale: "Draft judgment (one line): God is the transcendent Lord who sends prophets and grants mercy: 'My confidence rests with God, in this as in every thing, and in Him I put my trust. He is the Lord of the Sublime Throne' (p. 4). Named alternative: 1, since a short devotional formula need not express a full doctrine of transcendence."
    B_cause: {value: BELOW_THRESHOLD, note: "He counts as a scientist under P30 (the zij is a listed lasting result on the motions of sun, moon and planets), so B could come from working science at 0.5. But MacTutor lists 'astrological tables' among the zij's topics and a political history 'containing horoscopes', so his working science covers only part of what B scores (P19). Draft judgment (one line): coder's call, not scored; the alternative is B 3 at 0.5 from working science.", how_known: "BELOW_THRESHOLD under P19 (coder's call, CODING_GUIDE §8)."}
    C_ledger:
      value: 1
      basis: written_profession
      certainty: 0.5
      cites: [{source: S3, locator: "Author's Preface, p. 1; Notes, p. 175"}]
      how_known: "His own preface, but Rosen says he is 'very doubtful whether I have correctly understood the author's meaning in several passages of his preface' (Notes, p. 175), naming exactly these lines, so 0.5."
      rationale: "Draft judgment (one line): God's bounty goes 'towards those who deserve it by their virtuous acts', which God has 'prescribed to his adoring creatures'; by them we 'render ourselves worthy of the continuance (of his mercy)' (p. 1), and the author hopes the learned will obtain for him 'through their prayers the excellence of the Divine mercy' (p. 4): reward granted by God, and intercession. Named alternative: 0."
    D_authority: {value: BELOW_THRESHOLD, note: "The preface affirms prophecy ('He sent Mohammed ... with the mission of a prophet ... when the true way of life was sought for in vain', p. 1) but says nothing on revelation against reason or observation. Draft judgment (one line): too indirect to score.", how_known: "BELOW_THRESHOLD under P19."}
    E_scope: {value: UNKNOWN, how_known: "Nothing in the preface or the sources read on the world's order (P7, P19)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "B_cause is BELOW_THRESHOLD, so the P4 test cannot be applied (§6, P19). A_locus 0 alone would not meet it."}
  statements:
    - text: "Praised be God for his bounty towards those who deserve it by their virtuous acts: in performing which, as by him prescribed to his adoring creatures, we express our thanks, and render ourselves worthy of the continuance (of his mercy), and preserve ourselves from change: acknowledging his might, bending before his power, and revering his greatness ! He sent Mohammed (on whom may the blessing of God repose !) with the mission of a prophet, long after any messenger from above had appeared, when justice had fallen into neglect, and when the true way of life was sought for in vain."
      cites: [{source: S3, locator: "Author's Preface, p. 1"}]
      context: "Opening of the Algebra, dedicated to the caliph al-Ma'mun. Rosen doubts his reading of these lines (Notes, p. 175) and prints Shakespear's alternative rendering there."
      axes: [A_locus, C_ledger, D_authority]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-08
      note: "Facsimile of Rosen's printed translation (1831), not of the Arabic; translator's doubt noted."
    - text: "My confidence rests with God, in this as in every thing, and in Him I put my trust. He is the Lord of the Sublime Throne. May His blessing descend upon all the prophets and heavenly messengers !"
      cites: [{source: S3, locator: "Author's Preface, p. 4"}]
      context: "Close of the preface."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-08
      note: "Rosen's translation."
  changes_over_life: []
  coder_notes: "All worldview evidence is one formulaic preface in an 1831 English translation from a manuscript that Rosen says lacks most diacritical points; he is 'very doubtful' about several passages (Notes, p. 175). Coder's calls (CODING_GUIDE §8): B_cause BELOW_THRESHOLD although he counts as a scientist under P30, because his astronomy includes astrological tables and horoscopes (S1), so the working science covers only part of the axis; the conservative option is taken. Lawful-nature evidence for a mathematician is not taken from the Algebra itself (its subject is calculation, not the physical world). No LIO-type views found."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage:
    value: "Possibly of Khwarazmian (and possibly Zoroastrian) forebears; disputed"
    certainty: 0.5
    cites: [{source: S1, locator: "Biography, paragraph 1 (Toomer; Rashed)"}]
    how_known: "Toomer's reading of the name and the epithets; Rashed rejects the Zoroastrian inference."
  religious_heritage_by_birth: {value: BELOW_THRESHOLD, note: "See childhood.family_religion: Toomer's Zoroastrian reading vs Rashed.", how_known: "BELOW_THRESHOLD under P19."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not in the sources read."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not in the sources read."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "Works dated only as after 813 (P12, P29)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "First-lasting year UNKNOWN (P12)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement of his scored at 3 or 4 (P27)."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "The only worldview text read is the preface, which scores at the low end.", certainty: 0.5, cites: [{source: S3, locator: "pp. 1–4"}], how_known: "Absence in what was read."}
  worldview_during_major_work: {value: "Muslim devotional language in the preface of the Algebra", certainty: 0.7, cites: [{source: S3, locator: "pp. 1–4"}], how_known: "His own preface, in translation."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "The Algebra gives rules 'together with demonstrations' from 'intuitive geometric arguments' (S2), not axiomatic proof.", certainty: 0.5, cites: [{source: S2, locator: "paragraph 2"}], how_known: "Coder's reading of Britannica."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "Biography, paragraph 1"}], how_known: "Nothing known of his education."}
  circle_present: {value: "no", rationale: "The preface places God as transcendent Lord; nothing ties God to nature's order.", certainty: 0.5, cites: [{source: S3, locator: "pp. 1–4"}], how_known: "Coder's reading."}
  reading: "As belief, not finding: form partly, circle absent; no LIO-type views found."
  notes: ""

institutions:
  - {value: "House of Wisdom (Bayt al-Ḥikma), Baghdad", role: scholar, kind: "research institute", certainty: 1.0, cites: [{source: S1, locator: "Biography"}, {source: S2, locator: "paragraph 2"}], how_known: "Two sources."}
  - {value: "Caliph al-Ma'mun", role: "patron; dedicatee of the Algebra and the astronomy", years: "813–", kind: "patron or funder", certainty: 1.0, cites: [{source: S1, locator: "Biography"}, {source: S3, locator: "Author's Preface, p. 3"}], how_known: "MacTutor and his own preface."}
collaborators:
  - {value: "Banu Musa", relation: collaborator, note: "colleagues at the House of Wisdom", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor alone."}
  - {value: "Ptolemy (ptolemy)", relation: "influenced by", note: "the Geography and, probably, the tables in Theon's revision", certainty: 0.7, cites: [{source: S1, locator: "Biography (astronomy; geography)"}], how_known: "MacTutor alone, quoting Toomer ('highly likely')."}

review:
  roster_status_reason: {value: "Core in v8 (F 5: Claude, DeepSeek, Gemini, GPT, Grok).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 4"}], how_known: "Study roster."}
  controversies:
    - {value: "Whether al-Tabari's epithet 'al-Majusi' (Zoroastrian) belongs to him (Toomer) or to a second person (Rashed)", certainty: 0.7, cites: [{source: S1, locator: "Biography, paragraph 1"}], how_known: "MacTutor reports both."}
  data_quality_flags:
    - "MacTutor's page title gives 790–850 while its Quick Info gives about 780; Britannica gives c. 780."
    - "Rosen (1831) doubts his own translation of the preface (Notes, p. 175)."
  open_questions:
    - "Check the preface against a modern edition (Rashed 2007) for the C passage."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "J. J. O'Connor and E. F. Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Abu Ja'far Muhammad ibn Musa Al-Khwarizmi.\" MacTutor History of Mathematics, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Al-Khwarizmi/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Al-Khwarizmi/"
    accessed: 2026-10-08
    reliability_note: "Standard reference biography; quotes Toomer (DSB) and Rashed."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"al-Khwārizmī.\" Encyclopaedia Britannica. https://www.britannica.com/biography/al-Khwarizmi."
    url: "https://www.britannica.com/biography/al-Khwarizmi"
    accessed: 2026-10-08
    reliability_note: "Unsigned editors' article; whole article read."
    used_for: [identity, basics, contribution, lane_b, institutions]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Muhammad ibn Musa al-Khwarizmi; tr. Frederic Rosen"
    year: 1831
    citation: "Mohammed ben Musa. The Algebra of Mohammed ben Musa. Edited and translated by Frederic Rosen. London: Oriental Translation Fund, 1831. Scan: archive.org, algebraofmohamme00khuwuoft."
    url: "https://archive.org/details/algebraofmohamme00khuwuoft"
    accessed: 2026-10-08
    reliability_note: "Arabic text with English translation; the Author's Preface (pp. 1–4) and Rosen's Notes (p. 175) read on the OCR of the scan. Translator's doubt about the preface noted."
    used_for: [identity, contribution, worldview, timing, lane_b, institutions]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-08
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# Al-Khwarizmi

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Al-Khwarizmi (c. 780–c. 850), scholar at the House of Wisdom in Baghdad under al-Ma'mun, wrote the first systematic algebra, a treatise that carried Hindu-Arabic numerals to Europe, and astronomical tables [S1; S2]. The only worldview text is the pious preface of the Algebra [S3, pp. 1–4]. Draft: ISLAM 0.7; A 0 (0.7); C 1 (0.5); B BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD.

## Life and work

Little is known [S1]. Worked in Baghdad after 813 [S1; S2].

## Contribution and impact

Algebra; Hindu-Arabic numerals; zij; geography [S1; S2].

## Childhood and education

Not known; Zoroastrian forebears disputed [S1].

## Adult working worldview

Muslim devotional preface [S3]; possibly formulaic.

## Heritage (context only)

Disputed [S1].

## Timing

Works after 813, undated; timing UNKNOWN.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form partly; circle absent [S2; S3].

## Open questions

- Modern edition of the preface.

## Research log

- 2026-10-08: Read MacTutor, Britannica (editors) and Rosen 1831 (preface and notes, archive.org OCR).
