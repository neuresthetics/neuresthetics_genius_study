---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Y)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Y, order P32: F 4, rank 133). Basics from Britannica (Britannica Editors, 14 Sep 2026): the 'reputed author' of The Art of War, which is 'more likely to have been written early in the Warring States period'. Lorge (Cambridge, 2022) holds that many hands wrote it under the name of a 'fictional Master Sun'. No source read attributes the text to him, so it is context only (P42): it scores no code or axis. Giles's 1910 translation read for leads (ch. XI §26 against omens; ch. XIII §5 foreknowledge not from spirits). primary_system, A, C, E UNKNOWN; B, D BELOW_THRESHOLD as leads; mid_basin UNKNOWN. Life dates and span UNKNOWN (P39); era '-500 to 499' at 0.5. Not plotted. Draft, not reviewed."}

identity:
  id: sun-tzu
  display_name: "Sun Tzu"
  roster:
    canonical_name: "Sun Tzu"
    rank: 133
    F: 4
    models: [DeepSeek, Gemini, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: military strategy
    field_bucket: "politics / law / military"
  full_name: {value: "Sun Wu", certainty: 0.5, cites: [{source: S1, locator: "Quick Facts (personal name)"}], how_known: "Britannica gives the personal name Sun Wu; Lorge calls Master Sun 'fictional' (S3), so 0.5."}
  native_name: {value: "Sunzi (pinyin)", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Britannica: pinyin romanization Sunzi ('Master Sun')."}
  aliases:
    - {name: "Sun-Tzu", kind: "roster alias"}
    - {name: "Sunzi", kind: transliteration}

basics:
  birth:
    date: {value: UNKNOWN, how_known: "Britannica gives only 'flourished 5th century bce'."}
    place: {value: UNKNOWN, how_known: "Not given in the body read."}
  death:
    date: {value: UNKNOWN, how_known: "Not given."}
    place: {value: UNKNOWN, how_known: "Not given."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "The Art of War is undated; Britannica places its writing more likely early in the Warring States period (475–221 BCE) (P39)."}
  era_bucket: {value: "-500 to 499", certainty: 0.5, cites: [{source: S1, locator: "opening ('flourished 5th century bce')"}], how_known: "No dated lasting work (P39). Britannica's 'flourished 5th century bce' and the Warring States dating of the text both fall in '-500 to 499'; filled at the certainty of the life dates (0.5). If he served Wu before 500 BCE (the end of the Spring and Autumn period is 476 BCE in S1), the bucket could be 'before -500'."}
  region_of_birth: {value: "East Asia", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "China (P3); Britannica gives no birthplace."}
  region_of_work: {value: "East Asia", certainty: 0.7, cites: [{source: S1, locator: "opening ('served the state of Wu')"}], how_known: "Britannica."}
  sex_as_recorded: {value: "male", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "As recorded; the figure may be fictional (S3)."}
  languages_of_work: {value: ["Classical Chinese"], certainty: 0.5, cites: [{source: S2, locator: "title page ('Translated from the Chinese')"}], how_known: "Coder's reading."}
  occupations: {value: ["military strategist", "general"], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Britannica, as tradition."}

contribution:
  fields: {value: ["military strategy"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "The Art of War (Bingfa), attributed", year: UNKNOWN, kind: work, lasting: "'the earliest known treatise on war and military science'; its stress on politics and war 'greatly influenced some modern strategists', including Mao Zedong (S1)", certainty: 0.5, cites: [{source: S1, locator: "opening; body"}, {source: S3, locator: "abstract"}], how_known: "He is the 'reputed author' (S1); the work 'is more likely to have been written early in the Warring States period' (S1), and Lorge holds 'Many hands wrote, compiled, and edited the work' (S3). So 0.5, and the text is context only for his worldview (P42)."}
  evidence_of_impact:
    - {value: "Mao Zedong and the Chinese communists took many tactics from The Art of War", kind: "institutional or technological lineage", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "arguable", rationale: "The work clearly meets the bar; whether a single person wrote it is doubtful (S1, S3).", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading, as for Homer."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Nothing known."}
  family_religious_practice: {value: UNKNOWN, how_known: "Nothing known."}
  parents_and_household: []
  household_circumstances: {value: UNKNOWN, how_known: "Nothing known."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "Nothing known."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Nothing known."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Nothing known."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: UNKNOWN, how_known: "Equals timing.major_work_period (UNKNOWN, P39)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing attributable."}
  primary_system: {value: UNKNOWN, how_known: "Nothing attributable to him. The Art of War is context only (P42): no source read attributes it to him (S1 'reputed author'; S3 'many hands'). Even read as context it names no god or doctrine; its 'Heaven' is 'night and day, cold and heat, times and seasons' (S2 ch. I §7). Candidate considered: CHNFOLK (rejected: no evidence)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHNFOLK, reason: "Rejected: no evidence; the text forbids omens (S2 ch. XI §26), context only."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing attributable; the text's 'Heaven' is weather and seasons (S2 ch. I §7), context only (P42)."}
    B_cause: {value: BELOW_THRESHOLD, how_known: "Context only (P42), a lead: 'Prohibit the taking of omens, and do away with superstitious doubts' (S2 ch. XI §26) and 'foreknowledge cannot be elicited from spirits' (ch. XIII §5) treat events as known from men, not portents; a reading toward 3. Not his words by any source read."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read (P19)."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "Context only (P42), a lead toward 4: 'this foreknowledge cannot be elicited from spirits; it cannot be obtained inductively from experience, nor by any deductive calculation. Knowledge of the enemy's dispositions can only be obtained from other men' (S2 ch. XIII §§5–6): spies, not divination. Scope is military intelligence only."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7, P19)."}
  mid_basin: {value: UNKNOWN, how_known: "A is UNKNOWN (P19)."}
  statements:
    - text: "Now this foreknowledge cannot be elicited from spirits; it cannot be obtained inductively from experience, nor by any deductive calculation."
      cites: [{source: S2, locator: "ch. XIII §5"}]
      context: "On the use of spies: knowledge of the enemy 'can only be obtained from other men' (§6)."
      axes: [D_authority, B_cause]
      kind: other
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Context only (P42): the text is not attributed to him by any source read. Giles's 1910 translation in the Project Gutenberg text (web copy); Giles's interleaved commentary removed."
    - text: "Prohibit the taking of omens, and do away with superstitious doubts. Then, until death itself comes, no calamity need be feared."
      cites: [{source: S2, locator: "ch. XI §26"}]
      context: "On the conduct of an army deep in hostile territory."
      axes: [B_cause]
      kind: other
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Context only (P42); as above."
  changes_over_life: []
  coder_notes: "Coder's call. Treated like Homer and Confucius: the text is handed down under his name but not attributed to him by a source read, so it scores nothing (P42). Unlike Homer's poems the treatise is expository, so its passages on omens and spirits are recorded as leads (B, D BELOW_THRESHOLD) rather than left UNKNOWN; A has nothing even as context. Not result-changing: A is UNKNOWN, so he is unplotted either way."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Nothing known."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Nothing known."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Nothing known."}
  childhood_catechism: {value: UNKNOWN, how_known: "Nothing known."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "No dated lasting contribution (P39)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "No dated lasting contribution (P39)."}
  first_evidence_of_lio_type_views: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Nothing attributable (P42)."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "As above."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Nothing attributable."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not read for this.", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Not read."}
  circle_present: {value: "unclear", rationale: "Text not attributable.", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  reading: "Intelligence from men, not spirits, in an unattributed text."
  notes: ""

institutions:
  - {value: "State of Wu", role: "general and strategist (traditional)", years: UNKNOWN, kind: employer, certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Britannica, as tradition."}
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 133"}], how_known: "Study roster."}
  controversies:
    - {value: "Authorship and historicity: 'reputed author' (S1); 'many hands' and a 'fictional Master Sun' (S3)", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "abstract"}], how_known: "Both sources."}
  data_quality_flags:
    - "S3 read as the chapter abstract only."
    - "Britannica's Quick Facts give two 'Flourished' values (5th century BCE; 400–301 BCE); the body's 'flourished 5th century bce' is used."
  open_questions:
    - "Read a signed scholarly account of the text's date and authorship (Lorge's book; the Yinqueshan slips)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors (revised by Ethan Teekah)"
    citation: "Britannica Editors. \"Sun Tzu.\" Encyclopaedia Britannica (14 Sep 2026). https://www.britannica.com/biography/Sunzi. Read live 2026-10-19."
    url: "https://www.britannica.com/biography/Sunzi"
    accessed: 2026-10-19
    reliability_note: "Editors' article, most recently revised by Ethan Teekah."
    used_for: [identity, basics, contribution, worldview, timing, institutions, review]
  - id: S2
    type: primary
    kind: "scholarly edition"
    author: "Sun Tzu (attributed); trans. Lionel Giles"
    citation: "Sun Tzŭ on The Art of War. Translated from the Chinese with Introduction and Critical Notes by Lionel Giles. 1910. Project Gutenberg eBook #132."
    url: "https://www.gutenberg.org/ebooks/132"
    accessed: 2026-10-19
    reliability_note: "Scholarly translation (web copy, not scan-checked). Attributed text, context only for his worldview (P42). The Gutenberg front matter gives the year (1910) but no publisher."
    used_for: [basics, worldview, lane_b]
  - id: S3
    type: secondary
    kind: "scholarly book"
    author: "Peter Lorge"
    citation: "Lorge, Peter. Sun Tzu in the West: The Anglo-American Art of War. Cambridge: Cambridge University Press, 2022. Conclusion (doi:10.1017/9781108902687.011)."
    url: "https://doi.org/10.1017/9781108902687.011"
    accessed: 2026-10-19
    reliability_note: "Signed scholarly monograph; only the chapter abstract was read (via the DOI record), so used for the authorship question only."
    used_for: [identity, contribution, worldview, review]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Sun Tzu

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Sun Tzu (fl. 5th century BCE), reputed author of The Art of War [S1]. Draft: the text is not attributed to him by a source read (P42), so nothing scores; primary_system and A UNKNOWN; B and D leads only; mid_basin UNKNOWN. Not plotted.

## Life and work

General of Wu by tradition [S1].

## Contribution and impact

The Art of War, attributed [S1; S3].

## Childhood and education

Nothing known.

## Adult working worldview

Nothing attributable; the text forbids omens and seeks knowledge from men, not spirits [S2].

## Heritage (context only)

Nothing known.

## Timing

Undated (P39).

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Not read [S2].

## Open questions

- Date and authorship of the text.

## Research log

- 2026-10-19: Read Britannica, the Lorge chapter abstract and Giles's translation (chs. I, XI, XIII).
