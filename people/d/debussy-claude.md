---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch D)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-15
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch D, order P32: F 5, rank 18). Basics and works from Britannica (Lockspeiser). Worldview: the 1911 Excelsior interview with Henry Malherbe, read only as quoted in English in Vallas (1933), pp. 224–225 (archive.org scan). Not a scientist. primary_system BELOW_THRESHOLD (PANT fails the two-part test); A, B, D BELOW_THRESHOLD; C, E UNKNOWN; mid_basin BELOW_THRESHOLD. Draft, not reviewed."}

identity:
  id: debussy-claude
  display_name: "Claude Debussy"
  roster:
    canonical_name: "Claude Debussy"
    rank: 18
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: music
    field_bucket: music
  full_name: {value: "Achille-Claude Debussy", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts ('In full')"}], how_known: "Britannica alone."}
  native_name: {value: TODO}
  aliases:
    - {name: "Claude-Debussy", kind: "roster alias"}
    - {name: "Debussy-Claude", kind: "roster alias"}

basics:
  birth:
    date: {value: "1862-08-22", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts; opening sentence"}], how_known: "Britannica alone."}
    place: {value: "Saint-Germain-en-Laye, France", modern_name: "Saint-Germain-en-Laye, France", polity_then: "Second French Empire", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Britannica alone."}
  death:
    date: {value: "1918-03-25", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Britannica alone."}
    place: {value: "Paris", modern_name: "Paris, France", polity_then: "French Third Republic", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Britannica alone."}
  first_lasting_contribution_year: {value: 1894, certainty: 0.7, cites: [{source: S1, locator: "opening; Middle period"}], how_known: "Prélude à l'après-midi d'un faune (1894), the earliest listed lasting contribution; Britannica's year, taken as the premiere year (P30). Clair de lune is dated '1890–1905' (published within the suite later), so it is not listed as the earliest dated item."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "From 1894 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "France (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Early and Middle period (Paris)"}], how_known: "Britannica."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [French], certainty: 0.7, cites: [{source: S1, locator: "works"}], how_known: "French titles and texts."}
  occupations: {value: ["composer", "pianist"], certainty: 0.7, cites: [{source: S1, locator: "opening; Early period"}], how_known: "Britannica."}

contribution:
  fields: {value: ["composition"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Prélude à l'après-midi d'un faune", year: 1894, kind: work, lasting: "a 'seminal force' in 20th-century music (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; Middle period"}], how_known: "Britannica."}
    - {value: "Pelléas et Mélisande (opera)", year: 1902, kind: work, lasting: "his single completed opera; standard repertory", certainty: 0.7, cites: [{source: S1, locator: "Middle period ('first performed in 1902')"}], how_known: "Britannica."}
    - {value: "La Mer", year: 1905, kind: work, lasting: "orchestral repertory", certainty: 0.7, cites: [{source: S1, locator: "opening; Middle period"}], how_known: "Britannica."}
    - {value: "Douze Préludes, 2 books", year: "1910–1913", kind: work, lasting: "piano repertory", certainty: 0.7, cites: [{source: S1, locator: "Late period"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "Developed 'a highly original system of harmony and musical structure'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours:
    - {value: "Grand Prix de Rome (L'Enfant prodigue)", year: 1884, certainty: 0.7, cites: [{source: S1, locator: "Early period"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "Original harmonic system; seminal for 20th-century music.", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household: []
  household_circumstances: {value: "Lived with his parents in a poverty-stricken suburb of Paris", certainty: 0.7, cites: [{source: S1, locator: "Early period"}], how_known: "Britannica."}
  schooling:
    - {value: "Paris Conservatory (piano and composition)", stage: university, run_by: "state or municipal", years: "1873–", ages: "11–", certainty: 0.7, cites: [{source: S1, locator: "Early period"}], how_known: "Britannica; 'university' is the nearest stage for a conservatory."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Madame Mauté de Fleurville, associated with Chopin", certainty: 0.7, cites: [{source: S1, locator: "Early period"}], how_known: "Britannica."}
  languages_in_childhood: {value: TODO}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1894–1913", certainty: 0.7, cites: [{source: S1, locator: "opening; Late period"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "(interview) 'I do not practise religion in accordance with the sacred rites. I have made mysterious Nature my religion.' (1911)", certainty: 0.5, cites: [{source: S2, locator: "p. 225"}], how_known: "(interview) His words in a 1911 newspaper interview, known only in English translation as quoted by Vallas (secondary quotation), so 0.5."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "(interview) The only evidence read is one interview passage in translation, quoted secondhand (S2).", note: "Vallas calls it 'a pantheistic profession of faith', but under S6 PANT needs God identified with Nature as a claim about what exists plus a further mark; the passage is reverent language about nature ('an extraordinary emotion overwhelms me', 'that is what I call prayer') and names God separately ('any nearer to God'). It fails part 1, so not PANT; nothing supports ATHE or AGNOS either."}
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: PANT, reason: "Vallas's label; fails the two-part test (reverent language only)."}
    - {code: CHRIST, reason: "Rejected: 'I do not practise religion in accordance with the sacred rites'."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, note: "(interview) 'I do not believe that a man is any nearer to God for being clad in priestly garments' names God but says nothing of where God is. Draft judgment: too indirect.", how_known: "(interview) BELOW_THRESHOLD under P19."}
    B_cause: {value: BELOW_THRESHOLD, note: "Not a scientist; the interview praises nature's beauty but says nothing on law or exception (P16).", how_known: "BELOW_THRESHOLD under P19."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing on reward or afterlife in the passage read."}
    D_authority: {value: BELOW_THRESHOLD, note: "(interview) Rejects priestly garments and sacred rites as bringing one nearer to God, but says nothing of revelation against observation.", how_known: "(interview) BELOW_THRESHOLD under P19."}
    E_scope: {value: UNKNOWN, how_known: "Nothing on the world's order (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus and B_cause are BELOW_THRESHOLD."}
  statements:
    - text: "I do not practise religion in accordance with the sacred rites. I have made mysterious Nature my religion. I do not believe that a man is any nearer to God for being clad in priestly garments, nor that one place in a town is better adapted to meditation than another."
      cites: [{source: S2, locator: "p. 225"}]
      date: "1911-02-11"
      context: "Interview by Henry Malherbe for Excelsior, published 11 February 1911, while he was writing Le Martyre de saint Sébastien; Vallas introduces it as 'a pantheistic profession of faith'."
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "English translation as printed in Vallas 1933 (translated by Maire and Grace O'Brien), read on the archive.org scan (in.ernet.dli.2015.57948), pp. 224–225; OCR checked against the text flow, page image not viewed. French original in Excelsior not seen (primary check pending)."
  changes_over_life: []
  coder_notes: "Coder's call: the interview is used only for the self-described relation and notes, at 0.5, because it is a translation quoted secondhand. Wikiquote also gives a 1911 Martyre interview ('I have no profession of faith to utter to you') via Woolfe (2001); not read, not used."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "French", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1894–1913", certainty: 0.7, cites: [{source: S1, locator: "opening; Late period"}], how_known: "Prélude (1894) to Préludes book 2 (1913) (P29, P30). The Cello Sonata (1915) is named by Britannica but not listed; listing it would move the end to 1915."}
  age_at_first_lasting_contribution: {value: 32, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts; opening"}], how_known: "1894 − 1862 = 32 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement scored at 3 or 4 (P27)."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "The nature-religion passage is not scored at 3 or 4.", certainty: 0.5, cites: [{source: S2, locator: "p. 225"}], how_known: "Coder's reading."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Nothing read on proof-style training.", certainty: 0.5, cites: [{source: S1, locator: "Early period"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "Early period"}], how_known: "Nothing read."}
  circle_present: {value: "partly", rationale: "(interview) 'Nature in all its vastness is truthfully reflected in my sincere though feeble soul' maps nature into the self, without identifying God and Nature.", certainty: 0.5, cites: [{source: S2, locator: "p. 225"}], how_known: "(interview) Coder's reading of a secondhand translation."}
  reading: "As belief, not finding: form unclear, circle partly present."
  notes: ""

institutions:
  - {value: "Paris Conservatory", role: student, years: "1873–1884", kind: university, certainty: 0.7, cites: [{source: S1, locator: "Early period"}], how_known: "Britannica."}
collaborators:
  - {value: "Maurice Maeterlinck", relation: collaborator, note: "librettist of Pelléas", certainty: 0.7, cites: [{source: S1, locator: "Middle period"}], how_known: "Britannica."}
  - {value: "Nadezhda von Meck", relation: "mentor or employer", note: "patron", certainty: 0.7, cites: [{source: S1, locator: "Early period"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 18"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "The worldview passage is a translation quoted secondhand; the Excelsior original was not seen."
  open_questions:
    - "Find the Excelsior issue of 11 February 1911 on Gallica and check the French; read Lockspeiser, Debussy: His Life and Mind."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Edward Lockspeiser"
    citation: "Lockspeiser, Edward. \"Claude Debussy.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Claude-Debussy."
    url: "https://www.britannica.com/biography/Claude-Debussy"
    accessed: 2026-10-15
    reliability_note: "Signed encyclopedia article; the AI 'Top Questions' box was not used (P26)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "scholarly book"
    author: "Léon Vallas"
    year: 1933
    citation: "Vallas, Léon. Claude Debussy: His Life and Works. Translated by Maire and Grace O'Brien. London: Oxford University Press, 1933. Scan: archive.org, in.ernet.dli.2015.57948."
    url: "https://archive.org/details/in.ernet.dli.2015.57948"
    accessed: 2026-10-15
    reliability_note: "Standard early biography; quotes the 1911 interview in translation."
    used_for: [worldview, lane_b]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Claude Debussy

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Claude Debussy (1862–1918), French composer of the Prélude à l'après-midi d'un faune (1894), Pelléas et Mélisande (1902) and La Mer (1905) [S1]. In a 1911 interview, known in translation through Vallas, he said 'I have made mysterious Nature my religion' [S2, p. 225]. Draft: primary_system BELOW_THRESHOLD (interview); A, B BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD.

## Life and work

Paris Conservatory from 1873; Prix de Rome 1884 [S1].

## Contribution and impact

Faune, Pelléas, La Mer, Préludes [S1].

## Childhood and education

Poor suburb of Paris; Conservatory at 11 [S1].

## Adult working worldview

Nature-religion in one interview (interview, 0.5) [S2].

## Heritage (context only)

French [S1].

## Timing

First lasting contribution 1894, at 32 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form unclear; circle partly [S2].

## Open questions

- Excelsior original on Gallica.

## Research log

- 2026-10-15: Read Britannica (Lockspeiser) and Vallas 1933 (archive.org OCR, pp. 224–225). Wikiquote used only as a lead.
