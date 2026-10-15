---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch E)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-15
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch E, order P32: F 5, rank 27). Basics from Britannica (Zelazko). No worldview statement of her own was found: the widely quoted 'I am an atheist' (1948) is Diego Rivera's, not hers. All worldview fields UNKNOWN. Draft, not reviewed."}

identity:
  id: kahlo-frida
  display_name: "Frida Kahlo"
  roster:
    canonical_name: "Frida Kahlo"
    rank: 27
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: art
    field_bucket: arts
  full_name: {value: "Magdalena Carmen Frieda Kahlo y Calderón", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts ('Original name')"}], how_known: "Britannica alone; married name Frida Kahlo de Rivera."}
  native_name: {value: UNKNOWN, how_known: "Spanish in Latin script."}
  aliases:
    - {name: "Frida-Kahlo", kind: "roster alias"}
    - {name: "Kahlo-Frida", kind: "roster alias"}

basics:
  birth:
    date: {value: "1907-07-06", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Britannica alone."}
    place: {value: "Coyoacán, Mexico", modern_name: "Coyoacán, Mexico City, Mexico", polity_then: "Mexico", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Britannica alone."}
  death:
    date: {value: "1954-07-13", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Britannica alone."}
    place: {value: "Coyoacán, Mexico", modern_name: "Coyoacán, Mexico City, Mexico", polity_then: "Mexico", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Britannica alone."}
  first_lasting_contribution_year: {value: 1926, certainty: 0.7, cites: [{source: S1, locator: "Key dates; accident section (Self-Portrait Wearing a Velvet Dress, 1926)"}], how_known: "Earliest listed lasting contribution (P13)."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "1926"}], how_known: "From 1926 (P2)."}
  region_of_birth: {value: "Latin America and Caribbean", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Mexico (P3)."}
  region_of_work: {value: "Latin America and Caribbean", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Mexico; 1930–33 in the United States."}
  sex_as_recorded: {value: "female", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [Spanish], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's inference from her Mexican life; Britannica does not state it."}
  occupations: {value: ["painter", "teacher (La Esmeralda)"], certainty: 0.7, cites: [{source: S1, locator: "opening; Key dates 1943–54"}], how_known: "Britannica."}

contribution:
  fields: {value: ["painting"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Self-Portrait Wearing a Velvet Dress (first known work)", year: 1926, kind: work, lasting: "start of the self-portraits she is best known for (S1)", certainty: 0.7, cites: [{source: S1, locator: "accident section"}], how_known: "Britannica."}
    - {value: "Henry Ford Hospital and My Birth", year: 1932, kind: work, lasting: "'some of her most harrowing works' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Marriage to Diego Rivera'"}], how_known: "Britannica."}
    - {value: "Self-Portrait with Cropped Hair", year: 1940, kind: work, lasting: "cited for her rejection of gender restrictions, which 'continues to inspire artists' (S1)", certainty: 0.7, cites: [{source: S1, locator: "intro Q&A on gender (signed page)"}], how_known: "Britannica. The Two Fridas, her most famous painting per S1, is undated in the text read."}
  evidence_of_impact:
    - {value: "First 20th-century Mexican artist in the French national collection (The Frame, 1939)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "Key dates 1939"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "arguable", rationale: "Lasting fame mostly posthumous ('Fridamania'); originality of the self-portraits widely recognised.", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father, a German photographer of Hungarian descent", role: father, certainty: 0.7, cites: [{source: S1, locator: "early life"}], how_known: "Britannica."}
    - {value: "Mother, Mexican, of Spanish and Native American descent", role: mother, certainty: 0.7, cites: [{source: S1, locator: "early life"}], how_known: "Britannica."}
  household_circumstances: {value: TODO}
  schooling:
    - {value: "National Preparatory School, Mexico City, aiming at medicine", stage: "grammar or secondary school", run_by: "state or municipal", years: "1922–1925", ages: "15–18", certainty: 0.7, cites: [{source: S1, locator: "early life"}], how_known: "Britannica; run_by is the coder's reading of a national school."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "More interested in science than drawing; planned to study medicine", year: 1922, age: 15, certainty: 0.7, cites: [{source: S1, locator: "early life"}], how_known: "Britannica."}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events:
    - {value: "Polio, leaving a slight limp", year: 1913, age: 6, certainty: 0.7, cites: [{source: S1, locator: "Key dates 1913"}], how_known: "Britannica."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1926–1940", certainty: 0.7, cites: [{source: S1, locator: "dates"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Mexican Communist Party (PCM)", certainty: 0.7, cites: [{source: S1, locator: "accident section"}], how_known: "Britannica. A political membership, not evidence for a worldview code."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Britannica (Zelazko) read; no statement of her own on religion or science found. Diary (Abrams, ed. Lowe) not read."}
  primary_system: {value: UNKNOWN, how_known: "No statement of her own read. The 1948 'I am an atheist' quote circulated online is Diego Rivera's (Marginalian, quoting Zamora), so not used."}
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Not supported by her own words in the sources read; the atheist quote is Rivera's."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing read in her own words."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist; nothing read on nature's order."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "A and B are UNKNOWN (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Coder's call: religious imagery in paintings is not a statement of belief and is not coded."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Mexican; German-Hungarian father, Mexican mother of Spanish and Native American descent", certainty: 0.7, cites: [{source: S1, locator: "early life"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1926–1940", certainty: 0.7, cites: [{source: S1, locator: "dates"}], how_known: "1926 to 1940 (P29, P30). Later works not dated in the source read; listing one would move the end."}
  age_at_first_lasting_contribution: {value: 19, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts; 1926"}], how_known: "1926 − 1907 = 19 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement read."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Nothing read."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Nothing read."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Nothing read.", certainty: 0.5, cites: [{source: S1, locator: "early life"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "early life"}], how_known: "Nothing read."}
  circle_present: {value: "unclear", rationale: "Nothing read.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No reading possible."
  notes: ""

institutions:
  - {value: "La Esmeralda (Ministry of Public Education's School of Painting and Sculpture)", role: teacher, years: "1943–1954", kind: other, certainty: 0.7, cites: [{source: S1, locator: "Key dates 1943–54"}], how_known: "Britannica."}
collaborators:
  - {value: "Diego Rivera", relation: family, note: "husband (married 1929, divorced 1939, remarried 1940)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 27"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "A widely shared 'atheist' quote attributed to Kahlo online is Diego Rivera's (1948)."
  open_questions:
    - "Read the diary (Abrams 1995, ed. Lowe) and Zamora's letters for statements on God."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Alicja Zelazko"
    citation: "Zelazko, Alicja. \"Frida Kahlo.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Frida-Kahlo."
    url: "https://www.britannica.com/biography/Frida-Kahlo"
    accessed: 2026-10-15
    reliability_note: "Signed article."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators]
  - id: S2
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Frida Kahlo

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Frida Kahlo (1907–1954), Mexican painter of self-portraits [S1]. No statement of her own on religion was found. Draft: all worldview fields UNKNOWN; mid_basin UNKNOWN.

## Life and work

Bus accident 1925; taught herself to paint; married Rivera [S1].

## Contribution and impact

Self-portraits from 1926 [S1].

## Childhood and education

Polio at six; National Preparatory School [S1].

## Adult working worldview

Unknown [S1].

## Heritage (context only)

German-Hungarian and Mexican parents [S1].

## Timing

First lasting contribution 1926, at 19 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Unclear.

## Open questions

- Diary and letters.

## Research log

- 2026-10-15: Read Britannica; web search for her religious statements found only Rivera's quote.
