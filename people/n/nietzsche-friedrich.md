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
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch E, order P32: F 5, rank 28). Basics from Britannica (Magnus). Worldview from The Joyful Wisdom (trans. Thomas Common, Levy ed., 1910; Gutenberg #52881) §§108, 109, 343 and Ecce Homo (trans. Anthony M. Ludovici, Levy ed., 1911; Gutenberg #52190). The madman of §125 and Zarathustra are characters and are not used. ATHE 0.7; A 4 (0.7); B 4 (0.7, P40); C 4 (0.5); D 4 (0.7); mid_basin false (0.7). Draft, not reviewed."}

identity:
  id: nietzsche-friedrich
  display_name: "Friedrich Nietzsche"
  roster:
    canonical_name: "Friedrich Nietzsche"
    rank: 28
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Friedrich Wilhelm Nietzsche", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Britannica gives 'Friedrich Nietzsche' and says he was named after King Friedrich Wilhelm IV; the middle name 'Wilhelm' is the coder's inference from that, so 0.5 (P24)."}
  native_name: {value: UNKNOWN, how_known: "German in Latin script; same as display name."}
  aliases:
    - {name: "Friedrich-Nietzsche", kind: "roster alias"}
    - {name: "Nietzsche-Friedrich", kind: "roster alias"}

basics:
  birth:
    date: {value: "1844-10-15", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "At a Glance; opening"}], how_known: "Britannica alone."}
    place: {value: "Röcken, Saxony, Prussia", modern_name: "Röcken, Germany", polity_then: "Kingdom of Prussia", certainty: 0.7, cites: [{source: S1, locator: "At a Glance"}], how_known: "Britannica alone."}
  death:
    date: {value: "1900-08-25", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "At a Glance"}], how_known: "Britannica alone."}
    place: {value: "Weimar, Thuringian States", modern_name: "Weimar, Germany", polity_then: "German Empire", certainty: 0.7, cites: [{source: S1, locator: "At a Glance"}], how_known: "Britannica alone."}
  first_lasting_contribution_year: {value: 1872, certainty: 0.7, cites: [{source: S1, locator: "'Basel years' (Die Geburt der Tragödie, 1872)"}], how_known: "Earliest listed lasting contribution (P13)."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "'Basel years'"}], how_known: "From 1872 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "At a Glance"}], how_known: "Germany (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "'Basel years'"}], how_known: "Basel, Switzerland, and Germany; both Western Europe."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [German], certainty: 0.7, cites: [{source: S1, locator: "German titles"}], how_known: "Britannica."}
  occupations: {value: ["classical philologist (professor at Basel)", "philosopher", "critic of culture"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Basel years'"}], how_known: "Britannica."}

contribution:
  fields: {value: ["philosophy", "classical philology", "aesthetics"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "The Birth of Tragedy: the Apollonian and Dionysian account of Greek tragedy", year: 1872, kind: work, lasting: "'remains a classic in the history of aesthetics to this day' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Basel years'"}], how_known: "Britannica."}
    - {value: "Thus Spake Zarathustra", year: "1883–1885", kind: work, lasting: "'the first thorough statement of [his] mature philosophy'; influence 'considerable in the arts as well as philosophy' (S1)", certainty: 0.7, cites: [{source: S1, locator: "intro ('What did Friedrich Nietzsche write?', signed text)"}], how_known: "Britannica. Later works (Twilight, Antichrist, Ecce Homo) are named but not dated in the text read; listing them would move the span end to 1888."}
  evidence_of_impact:
    - {value: "'one of the most influential of all modern thinkers'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Human, All-Too-Human", year: 1878, kind: book, certainty: 0.7, cites: [{source: S1, locator: "'Basel years'"}], how_known: "Britannica."}
    - {value: "The Gay Science (Die fröhliche Wissenschaft)", year: 1882, kind: book, certainty: 0.5, cites: [{source: S2, locator: "title page"}], how_known: "Year is the coder's knowledge, not stated in the sources read; 0.5. Book V (§343) was added in the second edition."}
  honours:
    - {value: "Doctorate conferred by Leipzig without examination", year: 1869, certainty: 0.7, cites: [{source: S1, locator: "'Basel years'"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "Among the most influential modern thinkers.", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Lutheran", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica: 'a stronghold of Lutheran piety'."}
  family_religious_practice: {value: "Pious; father a pastor, both grandfathers clergy or Protestant writers", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  parents_and_household:
    - {value: "Father, Carl Ludwig Nietzsche, pastor at Röcken; died 1849", name: "Carl Ludwig Nietzsche", role: father, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
    - {value: "Mother, Franziska", name: "Franziska Nietzsche", role: mother, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  household_circumstances: {value: "After 1849 a household of five women (mother, sister, grandmother, two aunts); moved to Naumburg 1850", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  schooling:
    - {value: "Domgymnasium, Naumburg (private preparatory school)", stage: "grammar or secondary school", run_by: private, years: "1850–", ages: "6–", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
    - {value: "Schulpforta, Protestant boarding school", stage: "grammar or secondary school", run_by: "religious body", years: "1858–1864", ages: "14–20", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
    - {value: "Universities of Bonn (theology, philology) and Leipzig", stage: university, years: "1864–1869", ages: "20–25", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events:
    - {value: "Death of his father", year: 1849, age: 5, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1872–1885", certainty: 0.7, cites: [{source: S1, locator: "'Basel years'; intro"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "'I am quite unacquainted with atheism as a result, and still less as an event in my life: in me it is inborn, instinctive.' God is 'a coarse and rude prohibition of us: ye shall not think!' (Ecce Homo, 1888).", certainty: 0.7, cites: [{source: S3, locator: "'Why I am so clever', §1"}], how_known: "Own text written for publication, in Ludovici's translation via a Gutenberg web copy; 0.7 cap (§7)."}
  primary_system:
    value: ATHE
    basis: written_profession
    certainty: 0.7
    cites: [{source: S2, locator: "§§108, 109, 343"}, {source: S3, locator: "'Why I am so clever', §1"}]
    rationale: "Positive naturalism: 'God is dead' in his own voice (§108, §343), atheism 'inborn, instinctive' (EH), and the call to have 'nature entirely undeified' (§109). Not AGNOS (no suspension). Not PANT: he warns against thinking the world a living being and wants nature undeified (fails S6 part 1). NIHIL was considered; ATHE fits the metaphysics."
    how_known: "Translations in Gutenberg web copies; 0.7 cap. Gutenberg TODO: map §§ to the Kaufmann or KSA text."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Chosen."}
    - {code: NIHIL, reason: "He diagnoses nihilism; his own metaphysics is naturalist, so not primary."}
    - {code: PANT, reason: "Rejected: 'nature entirely undeified'."}
  lio_axes:
    A_locus:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S2, locator: "§108; §343"}, {source: S3, locator: "'Why I am so clever', §1"}]
      rationale: "No separate God: 'God is dead' (§108, own voice) and atheism as instinct (EH). Scored as an explicit denial (§6)."
      how_known: "Gutenberg web copies, 0.7 cap. The madman (§125) is a character and is not used."
    B_cause:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S2, locator: "§109"}]
      rationale: "Account of nature (P6): 'There are only necessities: there is no one who commands, no one who obeys, no one who transgresses'; no design and so no chance. Necessity with no exceptions and no commander is the LIO pole. He rejects the word 'law' as anthropomorphic and says the world is 'chaos' only 'in the sense of the absence of order, structure, form, beauty, wisdom', 'not by the absence of necessity'. Named alternative: BELOW_THRESHOLD, if 'it also knows no law' is read as rejecting the lawful pole (P40). Contested, so 0.7."
      how_known: "Gutenberg web copy, 0.7 cap; alternative named (P40, v8's pick)."
    C_ledger:
      value: 4
      basis: written_profession
      certainty: 0.5
      cites: [{source: S3, locator: "'Why I am so clever', §1"}]
      rationale: "'\"God,\" \"the immortality of the soul,\" \"salvation,\" a \"beyond\"' are notions he 'never paid any attention' to: no personal ledger. Indirect on reward and punishment, so 0.5."
      how_known: "Gutenberg web copy; indirect."
    D_authority:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S3, locator: "'Why I am so clever', §1"}]
      rationale: "God is 'a coarse and rude prohibition of us: ye shall not think!': religion keeps no domain of its own."
      how_known: "Gutenberg web copy, 0.7 cap."
    E_scope: {value: UNKNOWN, how_known: "Scored on the world's order (P7); §109's 'exception' is astronomical, not an in-group exception; nothing else read."}
  mid_basin: {value: false, certainty: 0.7, cites: [{source: S2, locator: "§108"}], how_known: "A_locus 4 (≥ 3) at 0.7; this branch reads A only (P10)."}
  statements:
    - text: "God is dead: but as the human race is constituted, there will perhaps be caves for millenniums yet, in which people will show his shadow,—And we—we have still to overcome his shadow!"
      cites: [{source: S2, locator: "§108"}]
      date: "1882"
      context: "Aphorism 'New Struggles', author's own voice."
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-15
      axes: [A_locus]
      note: "Common translation, Levy edition 1910, via Gutenberg #52881. Gutenberg TODO: check against Kaufmann/KSA."
    - text: "Let us be on our guard against saying that there are laws in nature. There are only necessities: there is no one who commands, no one who obeys, no one who transgresses. When you know that there is no design, you know also that there is no chance"
      cites: [{source: S2, locator: "§109"}]
      date: "1882"
      context: "Aphorism 'Let us be on our Guard', against anthropomorphising nature."
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-15
      axes: [B_cause]
    - text: "The general character of the world, on the other hand, is to all eternity chaos; not by the absence of necessity, but in the sense of the absence of order, structure, form, beauty, wisdom, and whatever else our æsthetic humanities are called."
      cites: [{source: S2, locator: "§109"}]
      date: "1882"
      context: "Same aphorism."
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-15
      axes: [B_cause]
    - text: "I am quite unacquainted with atheism as a result, and still less as an event in my life: in me it is inborn, instinctive."
      cites: [{source: S3, locator: "'Why I am so clever', §1"}]
      date: "1888"
      context: "Ecce Homo, written 1888 for publication, published 1908."
      kind: "unpublished manuscript"
      verified_against: "scholarly edition"
      verified_on: 2026-10-15
      axes: [A_locus, D_authority]
      note: "Ludovici translation, Levy edition 1911, via Gutenberg #52190. Supports A alongside the published §108 and §343."
  changes_over_life:
    - {value: "Lutheran household and theology study at Bonn (1864) before the working years", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Childhood and student years; off-point for the axes (P29). EH says he never attended to God 'even as a child'."}
  coder_notes: "Coder's call: Zarathustra's and the madman's words are characters' words and are not used (task rule). B 4 rests on P40 (v8's pick)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Lutheran", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1872–1885", certainty: 0.7, cites: [{source: S1, locator: "'Basel years'; intro"}], how_known: "Birth of Tragedy (1872) to Zarathustra (range end 1885) (P29, P30 #4)."}
  age_at_first_lasting_contribution: {value: 28, certainty: 0.7, cites: [{source: S1, locator: "At a Glance; 'Basel years'"}], how_known: "1872 − 1844 = 28 (P30)."}
  first_evidence_of_lio_type_views: {value: "1882, age 38: 'God is dead' (§108) and 'There are only necessities' (§109)", year: 1882, age: 38, certainty: 0.5, cites: [{source: S2, locator: "§§108–109"}], how_known: "Earlier works (Birth of Tragedy, Human, All-Too-Human) not read: 'earlier works not read' (P30 #7); year 1882 from the coder's knowledge, 0.5."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.5, cites: [{source: S2, locator: "§§108–109"}], how_known: "Within 1872–1885; earlier works not read."}
  worldview_during_major_work: {value: "ATHE", certainty: 0.7, cites: [{source: S2, locator: "§108"}], how_known: "As coded."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Aphoristic, not definition-to-consequence.", certainty: 0.5, cites: [{source: S2, locator: "form of the work"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Early years'"}], how_known: "Classical schooling; nothing on proof."}
  circle_present: {value: "no", rationale: "Rejects the world as living being and wants nature undeified.", certainty: 0.5, cites: [{source: S2, locator: "§109"}], how_known: "Coder's reading."}
  reading: "As belief, not finding: lawful-necessity naturalism without geometric form or circle."
  notes: ""

institutions:
  - {value: "University of Basel", role: "professor of classical philology", years: "1869–1879", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Basel years'"}], how_known: "Britannica."}
collaborators:
  - {value: "Richard Wagner", relation: other, note: "friend; friendship broken by 1878", certainty: 0.7, cites: [{source: S1, locator: "'Basel years'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 28"}], how_known: "Study roster."}
  controversies:
    - {value: "His name was later invoked by fascists for aims he loathed", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  data_quality_flags:
    - "Quotes read in 1910–11 Levy-edition translations via Gutenberg; fields capped at 0.7."
  open_questions:
    - "Check §§108, 109, 343 and EH against Kaufmann and KSA; read Twilight and Antichrist and date them for the span end."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Bernd Magnus"
    citation: "Magnus, Bernd. \"Friedrich Nietzsche.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Friedrich-Nietzsche."
    url: "https://www.britannica.com/biography/Friedrich-Nietzsche"
    accessed: 2026-10-15
    reliability_note: "Signed article body."
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, collaborators, review]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Friedrich Nietzsche"
    year: 1882
    citation: "Nietzsche, Friedrich. The Joyful Wisdom (La Gaya Scienza). Trans. Thomas Common. Complete Works, vol. 10, ed. Oscar Levy. 1910. Project Gutenberg eBook #52881."
    url: "https://www.gutenberg.org/ebooks/52881"
    accessed: 2026-10-15
    reliability_note: "Older authorised translation, web copy; 0.7 cap."
    used_for: [worldview, timing, lane_b]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Friedrich Nietzsche"
    year: 1888
    citation: "Nietzsche, Friedrich. Ecce Homo. Trans. Anthony M. Ludovici. Complete Works, vol. 17, ed. Oscar Levy. 1911. Project Gutenberg eBook #52190."
    url: "https://www.gutenberg.org/ebooks/52190"
    accessed: 2026-10-15
    reliability_note: "Web copy; 0.7 cap."
    used_for: [worldview]
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

# Friedrich Nietzsche

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Friedrich Nietzsche (1844–1900), German philologist and philosopher; The Birth of Tragedy (1872), Thus Spake Zarathustra (1883–85) [S1]. In his own voice: 'God is dead' [S2, §108]; 'There are only necessities' [S2, §109]; atheism 'inborn, instinctive' [S3]. Draft: ATHE 0.7; A 4 at 0.7; B 4 at 0.7 (P40); D 4 at 0.7; mid_basin false at 0.7.

## Life and work

Schulpforta, Bonn, Leipzig; professor at Basel 1869–79 [S1].

## Contribution and impact

Birth of Tragedy; Zarathustra [S1].

## Childhood and education

Pastor's son in a pious Lutheran home [S1].

## Adult working worldview

Atheist naturalism; necessity without a commander [S2, S3].

## Heritage (context only)

German Lutheran [S1].

## Timing

First lasting contribution 1872, at 28 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No form, no circle [S2].

## Open questions

- Kaufmann/KSA check.

## Research log

- 2026-10-15: Read Britannica; searched Gutenberg #52881 and #52190.
