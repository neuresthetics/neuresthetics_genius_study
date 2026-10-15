---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch I)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-15
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch I, order P32: F 5, rank 55). Basics from Britannica (Bokser). Worldview from The Guide for the Perplexed, Part II chs. XXV and XXIX (Friedländer, 2nd ed., Gutenberg #73584; web copy, 0.7 cap). Physician, not a natural scientist under P30. primary_system JUDA 0.7; A 0 at 0.7 (alt 1); B 3 at 0.7 (alt 4): the universe keeps its created properties 'except by way of miracle in some individual instances', miracles not permanent (P27 B 3 anchor, rare past miracles); C, D, E UNKNOWN; mid_basin true at 0.7. Plotted. Draft, not reviewed."}

identity:
  id: maimonides
  display_name: "Maimonides"
  roster:
    canonical_name: "Maimonides"
    rank: 55
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Moses ben Maimon", certainty: 0.7, cites: [{source: S1, locator: "header ('Original name')"}], how_known: "Britannica."}
  native_name: {value: "Abū ʿImran Mūsā ibn Maymūn ibn ʿUbayd Allāh", certainty: 0.7, cites: [{source: S1, locator: "header ('Also known as')"}], how_known: "Britannica (Arabic name, transliterated)."}
  aliases:
    - {name: "Moses Maimonides", kind: "roster alias"}
    - {name: "Rambam", kind: other}

basics:
  birth:
    date: {value: "1135-03-30", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; before 1582, so Julian."}
    place: {value: "Córdoba, Almoravid al-Andalus", modern_name: "Córdoba, Spain", polity_then: "Almoravid realm (al-Andalus)", certainty: 0.5, cites: [{source: S1, locator: "opening; 'Life'"}], how_known: "Britannica gives Córdoba, 'part of Islamic Spain'; the ruling dynasty is the coder's addition (0.5)."}
  death:
    date: {value: "1204-12-13", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Egypt", modern_name: "Egypt", polity_then: "Ayyubid Egypt", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Britannica gives Egypt only; polity is the coder's (0.5). Buried in Tiberias (S1)."}
  first_lasting_contribution_year: {value: 1168, certainty: 0.5, cites: [{source: S1, locator: "opening; 'Works'"}], how_known: "Commentary on the Mishna (with the Thirteen Articles of Faith), completed at age 33: 1135 + 33 = 1168 (derived, 0.5) (P13)."}
  era_bucket: {value: "500 to 1399", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "His whole life (1135–1204) falls in the bucket (P2)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Spain is Southern Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "'Life'; 'Works'"}], how_known: "Fez, then al-Fusṭāṭ, Egypt; Egypt is Middle East and North Africa in regions.csv."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [Arabic, Hebrew], certainty: 0.7, cites: [{source: S1, locator: "'Works'"}], how_known: "Britannica."}
  occupations: {value: ["philosopher", "jurist", "physician", "communal leader"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Life'"}], how_known: "Britannica."}

contribution:
  fields: {value: ["Jewish law", "philosophy", "medicine"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Commentary on the Mishna, with the creed of Thirteen Articles of Faith", year: 1168, kind: work, lasting: "creed 'became part of the orthodox liturgy' (S1)", certainty: 0.5, cites: [{source: S1, locator: "'Works'; 'Significance'"}], how_known: "Completed at 33 (derived year)."}
    - {value: "Mishne Torah (code of Jewish law)", kind: work, lasting: "'a brilliant systematization of all Jewish law and doctrine' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Works'"}], how_known: "Ten years after the commentary; no exact year given (P39)."}
    - {value: "The Guide for the Perplexed", year: 1191, kind: work, lasting: "'exerted a marked influence on the history of religious thought' (S1)", certainty: 0.5, cites: [{source: S1, locator: "'Works'"}], how_known: "Begun 1176 and laboured on for 15 years: 1176 + 15 = 1191 (derived, 0.5)."}
  evidence_of_impact:
    - {value: "Influenced the Scholastics, Spinoza and Leibniz", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "'Significance'"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "'the foremost intellectual figure of medieval Judaism' (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Jewish", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  family_religious_practice: {value: "Practised Judaism privately while appearing Muslim in public under the Almohads, from 1148", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  parents_and_household:
    - {value: "Father Maimon, a learned man and his first teacher", role: father, certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  household_circumstances: {value: "Distinguished family; persecution after the Almohad capture of Córdoba (1148)", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  schooling:
    - {value: "Studied with his father and other masters; Judaic studies and the sciences", stage: tutor, run_by: family, certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events:
    - {value: "Almohads capture Córdoba", year: 1148, age: 13, certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica; age 1148 − 1135."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1168–1191", certainty: 0.5, cites: [{source: S1, locator: "'Works'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Judaism (rabbinic)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Significance'"}], how_known: "Britannica."}
  self_described_science_religion_relation: {value: "Agrees 'with Aristotle in one half of his theory' (the universe keeps its properties) but holds it had a beginning; Aristotle's eternity would oppose 'the foundation of our religion'.", certainty: 0.7, cites: [{source: S2, locator: "Part II, chs. XXV and XXIX"}], how_known: "Published work in a web-copy translation."}
  primary_system:
    value: JUDA
    basis: written_profession
    certainty: 0.7
    cites: [{source: S2, locator: "Part II, ch. XXV"}, {source: S1, locator: "'Works'; 'Significance'"}]
    rationale: "Creation, revelation and miracles defended as 'the foundation of our religion' (S2); author of the Thirteen Articles and the Mishne Torah (S1)."
    how_known: "Guide (Friedländer translation, web copy), 0.7 cap."
  secondary_system: {value: ARIST, certainty: 0.5, basis: written_profession, cites: [{source: S2, locator: "Part II, ch. XXIX"}], rationale: "'we agree with Aristotle in one half of his theory'.", how_known: "Coder's reading of a partial agreement, 0.5."}
  candidate_codes_considered:
    - {code: JUDA, reason: "Chosen."}
    - {code: ARIST, reason: "Secondary: half-agreement with Aristotle on a stable universe."}
  lio_axes:
    A_locus:
      value: 0
      basis: written_profession
      certainty: 0.7
      cites: [{source: S2, locator: "Part II, chs. XXV and XXIX"}]
      how_known: "Published work, web copy, 0.7 cap; alternative named."
      rationale: "A Creator distinct from the universe, who 'has the power to change the whole Universe, to annihilate it, or to remove any of its properties' and who revealed the Law (ch. XXIX, ch. XXV); Scripture 'teaches the Incorporeality of God' (ch. XXV). Named alternative: 1 (the incorporeal Primal Cause read in Aristotelian terms)."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      cites: [{source: S2, locator: "Part II, ch. XXIX"}]
      how_known: "Published work, web copy, 0.7 cap; alternative named."
      rationale: "The P27 B 3 anchor, accepted rare past miracles: the universe 'remains perpetually with the same properties with which the Creator has endowed it, and that none of these will ever be changed except by way of miracle in some individual instances'; miracles 'were not permanent... the Universe since continues its regular course'. He reports, approvingly, the Sages' view that miracles were built into creation, which 'held it to be impossible that there should be a change in the laws of Nature'. Named alternative: 4 (if the built-in-miracle view is read as his own); he presents it as the Sages' and says 'This is my opinion' only of the exception view, so 3."
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Ch. XXV says the eternity theory 'has not been proved' and so 'we take the text of the Bible literally'; this concerns unproved theory, not observation against revelation. Not scored."}
    E_scope: {value: UNKNOWN, how_known: "Not read (P7)."}
  mid_basin: {value: true, certainty: 0.7, cites: [{source: S2, locator: "Part II, chs. XXV, XXIX"}], how_known: "A 0 (≤ 1) and B 3 (≥ 3), both at 0.7."}
  statements:
    - text: "For we believe that this Universe remains perpetually with the same properties with which the Creator has endowed it, and that none of these will ever be changed except by way of miracle in some individual instances, although the Creator has the power to change the whole Universe, to annihilate it, or to remove any of its properties."
      cites: [{source: S2, locator: "Part II, ch. XXIX"}]
      context: "After discussing the Sages' view of miracles."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "Friedländer, 2nd ed., via Gutenberg #73584; web copy, 0.7 cap. Undated within 1176–1191 (P39)."
    - text: "these changes were not permanent, they have not become a physical property. On the contrary, the Universe since continues its regular course. This is my opinion; this should be our belief."
      cites: [{source: S2, locator: "Part II, ch. XXIX"}]
      context: "On the rod, the water turned to blood, and the leprous hand."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "As above."
    - text: "Accepting the Creation, we find that miracles are possible, that Revelation is possible, and that every difficulty in this question is removed."
      cites: [{source: S2, locator: "Part II, ch. XXV"}]
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "As above."
  changes_over_life: []
  coder_notes: "Coder's call; Part II chs. XXV and XXIX only."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Andalusian Jewish", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Jewish", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1168–1191", certainty: 0.5, cites: [{source: S1, locator: "'Works'"}], how_known: "First to last dated (derived) contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 33, certainty: 0.7, cites: [{source: S1, locator: "'Works'"}], how_known: "Britannica: completed at the age of 33."}
  first_evidence_of_lio_type_views: {value: "1191", certainty: 0.5, cites: [{source: S2, locator: "Part II, ch. XXIX"}], how_known: "The Guide (begun 1176, completed about 1191); earlier works not read."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.5, cites: [{source: S1, locator: "'Works'"}], how_known: "The Guide is itself a major work."}
  worldview_during_major_work: {value: "JUDA", certainty: 0.7, cites: [{source: S2, locator: "Part II, ch. XXV"}], how_known: "As primary_system."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not read.", certainty: 0.5, cites: [{source: S1, locator: "'Works'"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Life'"}], how_known: "Not read."}
  circle_present: {value: "yes", rationale: "A Creator outside the world whose created order runs regularly, with rare past exceptions.", certainty: 0.5, cites: [{source: S2, locator: "Part II, ch. XXIX"}], how_known: "Coder's reading."}
  reading: "Creator plus stable created order with rare miracles."
  notes: ""

institutions:
  - {value: "Court of Saladin and al-Afḍal", role: "court physician", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
collaborators:
  - {value: "Joseph ibn ʿAqnīn", relation: "student or assistant", note: "the Guide was sent to him as a private communication", certainty: 0.7, cites: [{source: S1, locator: "'Works'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 55"}], how_known: "Study roster."}
  controversies:
    - {value: "The Guide was burned by church authorities at Montpellier in 1233 at a rabbi's instigation", certainty: 0.7, cites: [{source: S1, locator: "'Significance'"}], how_known: "Britannica."}
  data_quality_flags: []
  open_questions:
    - "Check the B quotes against a modern translation (Pines)."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Ben Zion Bokser"
    citation: "Bokser, Ben Zion. \"Moses Maimonides.\" Encyclopaedia Britannica, updated 21 September 2026. https://www.britannica.com/biography/Moses-Maimonides."
    url: "https://www.britannica.com/biography/Moses-Maimonides"
    accessed: 2026-10-15
    reliability_note: "Signed article body ('Life', 'Works', 'Significance'); Top Questions not cited."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators, review]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Moses Maimonides; trans. M. Friedländer"
    citation: "Maimonides, Moses. The Guide for the Perplexed. Trans. M. Friedländer. Second edition, revised throughout. Project Gutenberg eBook #73584."
    url: "https://www.gutenberg.org/ebooks/73584"
    accessed: 2026-10-15
    reliability_note: "Translation from the Arabic in an unofficial web copy; §7 cap 0.7."
    used_for: [worldview, timing, lane_b]
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

# Maimonides

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Moses Maimonides (1135–1204), Jewish philosopher, jurist and physician [S1]. Draft: primary_system JUDA 0.7; A 0 at 0.7; B 3 at 0.7; mid_basin true at 0.7. Plotted.

## Life and work

Córdoba; Fez; al-Fusṭāṭ; physician to Saladin [S1].

## Contribution and impact

Mishna commentary, Mishne Torah, Guide for the Perplexed [S1].

## Childhood and education

Taught by his father; persecution under the Almohads [S1].

## Adult working worldview

The universe keeps its created properties 'except by way of miracle in some individual instances' [S2].

## Heritage (context only)

Andalusian Jewish [S1].

## Timing

First lasting contribution 1168 (derived), at 33 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Circle present [S2].

## Open questions

- Pines translation check.

## Research log

- 2026-10-15: Read Britannica (Bokser) and Guide Part II chs. XXV, XXIX (Gutenberg #73584).
