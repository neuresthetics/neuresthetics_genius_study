---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch K)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-15
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch K, order P32: F 5, rank 72). Basics from Britannica (Britannica Editors, unsigned; Top Questions not cited) and SEP (Bergoffen and Burke, rev. 2023). Worldview from The Ethics of Ambiguity (1947; Frechtman translation 1948, marxists.org web copy), Part I. Not a scientist (P30). primary_system EXIST (0.5, alt ATHE); A 4 (0.5, alt BELOW_THRESHOLD); B UNKNOWN (P16); mid_basin BELOW_THRESHOLD. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Audit fixes (fallacy_catalog audit of 2d75649, run 1). mid_basin how_known explains BELOW_THRESHOLD: the A ≥ 3 branch reads A only (P10). SEP's 'at age fourteen' line cited explicitly for A 4. EXIST kept (0.5, alternative ATHE), with a note that the EXIST system file does not separate atheist from theist existentialism."}

identity:
  id: de-beauvoir-simone
  display_name: "Simone de Beauvoir"
  roster:
    canonical_name: "Simone de Beauvoir"
    rank: 72
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Simone-Lucie-Ernestine-Marie Bertrand de Beauvoir", certainty: 0.7, cites: [{source: S1, locator: "header ('In full')"}], how_known: "Britannica."}
  native_name: {value: UNKNOWN, how_known: "French, Latin script."}
  aliases: []

basics:
  birth:
    date: {value: "1908-01-09", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "§1"}], how_known: "Britannica and SEP agree."}
    place: {value: "Paris, France", modern_name: "Paris, France", polity_then: "France", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "§1"}], how_known: "Two sources."}
  death:
    date: {value: "1986-04-14", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Paris, France", modern_name: "Paris, France", polity_then: "France", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1943, certainty: 0.7, cites: [{source: S1, locator: "novels paragraph"}], how_known: "L'Invitée (1943; She Came To Stay), first listed work (P30)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Birth year bucket (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "France (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Paris."}
  sex_as_recorded: {value: "female", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [French], certainty: 0.7, cites: [{source: S1, locator: "titles"}], how_known: "Britannica."}
  occupations: {value: ["writer", "philosopher", "teacher"], certainty: 0.7, cites: [{source: S1, locator: "opening; paragraph 2"}], how_known: "Britannica."}
contribution:
  fields: {value: ["philosophy", "literature", "feminist theory"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "L'Invitée (She Came To Stay)", year: 1943, kind: work, lasting: "novel expounding existential themes (S1)", certainty: 0.7, cites: [{source: S1, locator: "novels paragraph"}], how_known: "Britannica."}
    - {value: "Le Deuxième Sexe (The Second Sex)", year: 1949, kind: work, lasting: "'a classic of feminist literature' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "Les Mandarins (The Mandarins)", year: 1954, kind: work, lasting: "Prix Goncourt (S1)", certainty: 0.7, cites: [{source: S1, locator: "novels paragraph"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "The Second Sex 'became a classic of feminist literature'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours:
    - {value: "Prix Goncourt", year: 1954, certainty: 0.7, cites: [{source: S1, locator: "novels paragraph"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "(S1, S2).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Catholic", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP: 'a traditional bourgeois, Catholic upbringing'."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father Georges Bertrand de Beauvoir; mother Françoise (née Brasseur); sister Hélène", role: parents, certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP."}
  household_circumstances: {value: "Bourgeois family that lost class status in 1919", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP."}
  schooling:
    - {value: "Institut Adeline Désir, private Catholic school for girls", stage: "grammar or secondary school", run_by: "religious body", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP."}
    - {value: "Sorbonne; agrégation in philosophy, 1929", stage: university, run_by: "state or municipal", certainty: 0.7, cites: [{source: S1, locator: "paragraph 2"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [French], certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "Rejected the existence of God at fourteen", year: 1922, certainty: 0.5, cites: [{source: S2, locator: "§1"}], how_known: "SEP gives the age; year computed as 1908 + 14 (0.5)."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1943–1954", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system:
    value: EXIST
    basis: scholarly_reconstruction
    certainty: 0.5
    cites: [{source: S2, locator: "opening; §5"}, {source: S1, locator: "opening"}]
    rationale: "SEP: she 'identifies herself as an existentialist'; Britannica: one of the philosopher-writers of existentialism. Named alternative: ATHE, since SEP calls The Ethics of Ambiguity 'a secularism that rejects the ideas of God and Humanity'."
    how_known: "Reconstruction in SEP and Britannica (0.5 cap)."
    note: "systems/EXIST.md does not separate atheist from theist existentialism; her EXIST is the atheist kind (A 4), so ATHE stays the named alternative."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: EXIST, reason: "Self-identified existentialist (S2)."}
    - {code: ATHE, reason: "Rejected God at fourteen; writes of 'God's absence' (S3)."}
  lio_axes:
    A_locus:
      value: 4
      basis: written_profession
      certainty: 0.5
      cites: [{source: S3, locator: "Part I"}, {source: S2, locator: "§1 ('at age fourteen Beauvoir rejected the existence of God')"}]
      how_known: "Published treatise, web copy of the translation, supported by SEP §1: 'Although initially devout in her faith, at age fourteen Beauvoir rejected the existence of God'; alternative named, so 0.5."
      rationale: "At the LIO pole on the reading 'no God': 'far from God's absence authorizing all license, the contrary is the case'; man bears responsibility for 'a world which is not the work of a strange power'. Named alternative: BELOW_THRESHOLD, since the key line is phrased as a conditional ('if God does not exist')."
    B_cause: {value: UNKNOWN, how_known: "Not a scientist; no statement on nature read (P16)."}
    C_ledger: {value: UNKNOWN, how_known: "'A God can pardon, efface, and compensate. But if God does not exist, man's faults are inexpiable' bears on C, but it is conditional and about human responsibility; not scored (coder's call)."}
    D_authority: {value: UNKNOWN, how_known: "'the genuine man will not agree to recognize any foreign absolute' may bear on D; not scored at this reading."}
    E_scope: {value: UNKNOWN, how_known: "Not read (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "BELOW_THRESHOLD, not UNKNOWN: the A ≥ 3 branch reads A only (P10), so B UNKNOWN is not a needed axis, and A 4 is scored only at 0.5, under the 0.7 bar. P19's UNKNOWN precedence would apply only on A's named alternative (BELOW_THRESHOLD), where B becomes needed.", note: "If A reached 0.7 the result would be false."}
  statements:
    - text: "However, far from God’s absence authorizing all license, the contrary is the case, because man is abandoned on the earth, because his acts are definitive, absolute engagements."
      cites: [{source: S3, locator: "Part I"}]
      date: "1947"
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "Frechtman translation (1948), marxists.org web copy; 0.7 cap."
    - text: "A God can pardon, efface, and compensate. But if God does not exist, man’s faults are inexpiable."
      cites: [{source: S3, locator: "Part I"}]
      date: "1947"
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "As above."
  changes_over_life:
    - {value: "Initially devout Catholic; rejected the existence of God at fourteen", year: 1922, certainty: 0.5, cites: [{source: S2, locator: "§1"}], how_known: "SEP; year computed."}
  coder_notes: "Coder's call; Part I of The Ethics of Ambiguity only. Memoirs of a Dutiful Daughter (1958) is the lead for her own account of losing faith."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "French bourgeois", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP."}
  religious_heritage_by_birth: {value: "Catholic", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1943–1954", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "First to last listed lasting contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 35, certainty: 0.7, cites: [{source: S1, locator: "opening; novels paragraph"}], how_known: "1943 − 1908 = 35 (P30)."}
  first_evidence_of_lio_type_views: {value: "1947, age 39: 'far from God’s absence authorizing all license'", year: 1947, age: 39, certainty: 0.5, cites: [{source: S3, locator: "Part I"}], how_known: "Earlier works (L'Invitée 1943, Pyrrhus et Cinéas 1944) not read: 'earlier works not read' (P30 #7)."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.5, cites: [{source: S3, locator: "Part I"}], how_known: "1947 falls in 1943–1954."}
  worldview_during_major_work: {value: EXIST, certainty: 0.5, cites: [{source: S2, locator: "opening"}], how_known: "As primary_system."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Essays and novels, not deductive.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Not read."}
  circle_present: {value: "no", rationale: "No God as source or end.", certainty: 0.5, cites: [{source: S3, locator: "Part I"}], how_known: "Coder's reading."}
  reading: "Secular existentialism."
  notes: ""

institutions:
  - {value: "Les Temps modernes (co-founder and editor, 1945)", role: editor, kind: other, certainty: 0.7, cites: [{source: S1, locator: "paragraph 2"}], how_known: "Britannica."}
collaborators:
  - {value: "Jean-Paul Sartre", relation: collaborator, certainty: 0.7, cites: [{source: S1, locator: "paragraph 2"}], how_known: "Lifelong association."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 72"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags: []
  open_questions:
    - "Read Memoirs of a Dutiful Daughter for her own account of losing faith; read Pyrrhus et Cinéas (1944)."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Simone de Beauvoir.\" Encyclopaedia Britannica, updated 11 September 2026. https://www.britannica.com/biography/Simone-de-Beauvoir."
    url: "https://www.britannica.com/biography/Simone-de-Beauvoir"
    accessed: 2026-10-15
    reliability_note: "Unsigned editors' body; Top Questions not cited."
    used_for: [identity, basics, contribution, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: encyclopedia
    author: "Debra Bergoffen and Megan Burke"
    citation: "Bergoffen, Debra, and Megan Burke. \"Simone de Beauvoir.\" Stanford Encyclopedia of Philosophy, substantive revision 11 January 2023. https://plato.stanford.edu/entries/beauvoir/."
    url: "https://plato.stanford.edu/entries/beauvoir/"
    accessed: 2026-10-15
    reliability_note: "Signed scholarly entry."
    used_for: [basics, childhood, worldview, heritage, timing]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Simone de Beauvoir"
    citation: "Beauvoir, Simone de. The Ethics of Ambiguity. 1947. Trans. Bernard Frechtman. New York: Philosophical Library, 1948. Marxists Internet Archive web copy, Part I. https://www.marxists.org/reference/subject/ethics/de-beauvoir/ambiguity/ch01.htm."
    url: "https://www.marxists.org/reference/subject/ethics/de-beauvoir/ambiguity/ch01.htm"
    accessed: 2026-10-15
    reliability_note: "Web transcription of the translation; 0.7 cap."
    used_for: [worldview, timing, lane_b]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Simone de Beauvoir

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Simone de Beauvoir (1908–1986), French existentialist philosopher, novelist and feminist [S1, S2]. Draft: primary_system EXIST (0.5, alt ATHE); A 4 at 0.5; B UNKNOWN; mid_basin BELOW_THRESHOLD. Not plotted.

## Life and work

Sorbonne; teaching 1931–43; Les Temps modernes [S1].

## Contribution and impact

L'Invitée (1943); The Second Sex (1949); The Mandarins (1954) [S1].

## Childhood and education

Catholic upbringing; rejected God at fourteen [S2].

## Adult working worldview

'far from God’s absence authorizing all license, the contrary is the case' [S3].

## Heritage (context only)

Catholic, bourgeois [S2].

## Timing

First lasting contribution 1943, at 35 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle [S3].

## Open questions

- Memoirs of a Dutiful Daughter.

## Research log

- 2026-10-15: Read Britannica (Editors), SEP (Bergoffen and Burke) and The Ethics of Ambiguity Part I.
