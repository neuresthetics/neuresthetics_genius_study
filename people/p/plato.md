---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch J)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-15
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch J, order P32: F 5, rank 65). Basics from Britannica (Meinwald). Worldview from the Timaeus and Laws X (Jowett, Gutenberg #1572 and #1750; web copies), attributed to Plato himself by SEP 'Plato's Timaeus' (Zeyl and Sattler), so they count under P42; spoken by characters (Timaeus, the Athenian Stranger), so 0.5. Not a scientist (Britannica: 'not a research mathematician'). primary_system PLATO 0.5; A 1 at 0.5 (alt 0); B 3 at 0.5 (alt 4); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Plotted (faded). Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Audit fixes (fallacy_catalog audit of 81b9098, run 1). Laws X dropped from the B rationale and cites: no source read attributes its theology to Plato (P42). SEP's opening sentence ('In the Timaeus Plato presents...') cited explicitly as the P42 attribution for the Timaeus. B stays 3 (0.5, alternative 4)."}

identity:
  id: plato
  display_name: "Plato"
  roster:
    canonical_name: "Plato"
    rank: 65
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Plato", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  native_name: {value: UNKNOWN, how_known: "Greek form not in the sources read."}
  aliases: []

basics:
  birth:
    date: {value: "-428", calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "opening ('428/427 bce')"}], how_known: "Britannica gives 428/427 BCE; the earlier year is recorded (0.5); proleptic Julian."}
    place: {value: "Athens", modern_name: "Athens, Greece", polity_then: "Athens", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "-348", calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "opening ('348/347')"}], how_known: "Britannica gives 348/347 BCE (0.5)."}
    place: {value: "Athens", modern_name: "Athens, Greece", polity_then: "Athens", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "The order and dates of the dialogues 'cannot be known' (S1, 'Dating, editing, translation'); the Academy is dated only to 'the 380s' (P39)."}
  era_bucket: {value: "-500 to 499", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "His whole adult life falls in the bucket on either birth year (P2, P39)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Greece is Southern Europe in regions.csv (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Athens; trips to Syracuse."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [Greek], certainty: 0.7, cites: [{source: S1, locator: "'Dating, editing, translation'"}], how_known: "Britannica (Greek authors)."}
  occupations: {value: ["philosopher", "teacher"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["metaphysics", "ethics", "political philosophy", "cosmology", "epistemology"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Theory of forms", kind: theory, lasting: "(S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; undated (P39)."}
    - {value: "The dialogues (Republic, Timaeus and others)", kind: work, lasting: "'philosophical works of unparalleled influence' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Undated (P39)."}
    - {value: "The Academy", kind: institution, lasting: "'the ultimate ancestor of the modern university' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Founded in the 380s (S1)."}
  evidence_of_impact:
    - {value: "One of the major figures of Classical antiquity", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father Ariston, mother Perictione; aristocratic family related on the mother's side to Solon", role: parents, certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  household_circumstances: {value: "Aristocratic and distinguished Athenian family", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  schooling: []
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Socrates (as a young man, member of his circle)", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  languages_in_childhood: {value: TODO}
  notable_events:
    - {value: "Trial and execution of Socrates", year: -399, certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica; adult event recorded for context; age omitted because the birth year is uncertain."}

worldview:
  unit: "adult working worldview"
  working_years: {value: UNKNOWN, how_known: "Equals timing.major_work_period (UNKNOWN, P39)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system:
    value: PLATO
    basis: scholarly_reconstruction
    certainty: 0.5
    cites: [{source: S1, locator: "opening"}, {source: S3, locator: "§1"}]
    rationale: "The system is his own: forms as 'the most important constituents of reality' (S1); a universe that is 'the product of rational, purposive, and beneficent agency' (S3)."
    how_known: "Britannica and SEP reconstruct his doctrine; scholarly_reconstruction caps at 0.5."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: PLATO, reason: "Chosen."}
  lio_axes:
    A_locus:
      value: 1
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S2, locator: "Timaeus, the creator passage (within SEP's 29d7–47e2) and the closing sentence"}, {source: S3, locator: "§1 and the questions on the Craftsman"}]
      how_known: "Dialogue speech attributed to Plato by SEP's opening sentence ('In the Timaeus Plato presents...', P42); Jowett web copy; 0.5."
      rationale: "A maker ('the father and maker of all') who orders the world, which itself becomes 'a living creature truly endowed with soul and intelligence by the providence of God' and finally 'the sensible God who is the image of the intellectual' (Timaeus): a world that is itself divine, made by a maker. Named alternative: 0 (SEP notes the question whether the Craftsman is 'an entity that is ontologically distinct from both the model and its copy')."
    B_cause:
      value: 3
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S2, locator: "Timaeus, opening of the Necessity section (SEP: from 47d3)"}, {source: S3, locator: "account of Necessity"}]
      how_known: "Dialogue speech attributed to Plato by SEP's opening sentence ('In the Timaeus Plato presents an elaborately wrought account of the formation of the universe'), which satisfies P42; web copy; 0.5 as character speech."
      rationale: "'The creation is mixed, being made up of necessity and mind. Mind, the ruling power, persuaded necessity' (Timaeus); per SEP, the properties fixed by Necessity are such that 'it is not open to the Craftsman to change or eliminate' them. That leans toward 4, but the account is called merely likely, and no exceptionless order is stated (P40). Named alternative: 4. Laws X is not used: no source read attributes its theology to Plato (P42)."
    C_ledger: {value: UNKNOWN, how_known: "Laws X argues against the view that gods can be appeased by gifts, but no source read attributes the Laws X theology to Plato (P42); not scored."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 1 and B 3 would satisfy A ≤ 1 and B ≥ 3, but both are at 0.5, below the 0.7 bar (§6, P19)."}
  statements:
    - text: "Wherefore, using the language of probability, we may say that the world became a living creature truly endowed with soul and intelligence by the providence of God."
      cites: [{source: S2, locator: "Timaeus, the creator passage (Jowett)"}]
      context: "Timaeus's account of why the creator made the world."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "Spoken by Timaeus; attributed to Plato by SEP (P42). Jowett via Gutenberg #1572; web copy."
    - text: "for the creation is mixed, being made up of necessity and mind. Mind, the ruling power, persuaded necessity to bring the greater part of created things to perfection"
      cites: [{source: S2, locator: "Timaeus, opening of the Necessity section (Jowett)"}]
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "As above; SEP's outline puts the Necessity section at 47d3–69a5."
    - text: "the sensible God who is the image of the intellectual, the greatest, best, fairest, most perfect—the one only-begotten heaven."
      cites: [{source: S2, locator: "Timaeus, closing sentence"}]
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "As above."
  changes_over_life: []
  coder_notes: "Coder's call. Dialogues are character speech; SEP's attribution of the Timaeus cosmology to Plato ('In the Timaeus Plato presents...') satisfies P42's scholarly-agreement clause, but the 0.5 reflects the dialogue form and the 'likely account'."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Athenian aristocracy", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "Undated works (P39)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "Undated (P39)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "Undated dialogues."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.5, cites: [{source: S2, locator: "Timaeus"}], how_known: "The Timaeus is itself a major work."}
  worldview_during_major_work: {value: "PLATO", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "As primary_system."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "The Academy fostered mathematics; Plato used the mathematicians' results (S1).", certainty: 0.5, cites: [{source: S1, locator: "'Life'"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Life'"}], how_known: "Not read."}
  circle_present: {value: "yes", rationale: "A maker whose mind orders the world by persuading necessity.", certainty: 0.5, cites: [{source: S2, locator: "Timaeus"}], how_known: "Coder's reading."}
  reading: "A divine maker and a divine ordered world; necessity persuaded by mind."
  notes: ""

institutions:
  - {value: "The Academy, Athens", role: founder, kind: "academy or learned society", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica (founded in the 380s)."}
collaborators:
  - {value: "Socrates", relation: teacher, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  - {value: "Aristotle", relation: "student or assistant", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Life'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 65"}], how_known: "Study roster."}
  controversies:
    - {value: "Authenticity of the Letters (including the Seventh) is disputed", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  data_quality_flags: []
  open_questions:
    - "Add Stephanus numbers from a numbered edition."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Constance C. Meinwald"
    citation: "Meinwald, Constance C. \"Plato.\" Encyclopaedia Britannica, updated 28 August 2026. https://www.britannica.com/biography/Plato."
    url: "https://www.britannica.com/biography/Plato"
    accessed: 2026-10-15
    reliability_note: "Signed body; Top Questions not cited."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators, review]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Plato; trans. Benjamin Jowett"
    citation: "Plato. Timaeus. Trans. Benjamin Jowett. Project Gutenberg eBook #1572."
    url: "https://www.gutenberg.org/ebooks/1572"
    accessed: 2026-10-15
    reliability_note: "Translation in an unofficial web copy; quotes taken from the dialogue text, not Jowett's introduction; §7 cap 0.7."
    used_for: [worldview, timing, lane_b]
  - id: S3
    type: secondary
    kind: encyclopedia
    author: "Donald Zeyl and Barbara Sattler"
    year: 2022
    citation: "Zeyl, Donald, and Barbara Sattler. \"Plato's Timaeus.\" Stanford Encyclopedia of Philosophy, first published 25 October 2005, substantive revision 13 May 2022. https://plato.stanford.edu/entries/plato-timaeus/."
    url: "https://plato.stanford.edu/entries/plato-timaeus/"
    accessed: 2026-10-15
    reliability_note: "Peer-reviewed reference article."
    used_for: [worldview]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Plato; trans. Benjamin Jowett"
    citation: "Plato. Laws. Trans. Benjamin Jowett. Project Gutenberg eBook #1750."
    url: "https://www.gutenberg.org/ebooks/1750"
    accessed: 2026-10-15
    reliability_note: "Translation in an unofficial web copy; Book X read but not used for any score (no attribution source, P42)."
    used_for: [worldview]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Plato

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Plato (428/427–348/347 BCE), Athenian philosopher, founder of the Academy [S1]. Draft: primary_system PLATO 0.5; A 1 at 0.5; B 3 at 0.5; mid_basin BELOW_THRESHOLD. Plotted (faded).

## Life and work

Circle of Socrates; Syracuse; the Academy [S1].

## Contribution and impact

Forms; dialogues; Academy [S1].

## Childhood and education

Aristocratic Athenian family [S1].

## Adult working worldview

'the creation is mixed, being made up of necessity and mind' [S2, S3].

## Heritage (context only)

Athenian aristocracy [S1].

## Timing

Works undated [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Circle present [S2].

## Open questions

- Add Stephanus numbers.

## Research log

- 2026-10-15: Read Britannica (Meinwald), SEP 'Plato's Timaeus', Timaeus and Laws X (Gutenberg #1572, #1750).
- 2026-10-15: Batch J audit fixes: Laws X dropped from B; SEP's opening sentence cited for P42.
