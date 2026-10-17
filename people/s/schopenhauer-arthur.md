---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch N)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-17
  last_updated: 2026-10-17
  change_log:
    - {date: 2026-10-17, by: "Grok Bot", summary: "Record created (stage 3 batch N, order P32: F 4, rank 85). Basics from Britannica (Arthur Hübscher, signed; body only). Worldview from The World as Will and Idea (Haldane and Kemp translation, Gutenberg #38427 and #40868: vol. 1 §§55, 63, 68; vol. 3 ch. L) and SEP 'Arthur Schopenhauer' (Wicks, 2021). primary_system IDEAL (0.5, alt ATHE); A 4 (0.7); B 4 (0.5, alt 3: his own named exception, freedom appearing in the phenomenon in the denial of the will); C 3 (0.5, alt 4); E 3 (0.5, alt 4); mid_basin false (0.7). Plotted (faded). Draft, not reviewed."}

identity:
  id: schopenhauer-arthur
  display_name: "Arthur Schopenhauer"
  roster:
    canonical_name: "Arthur Schopenhauer"
    rank: 85
    F: 4
    models: [Claude, Gemini, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Arthur Schopenhauer", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  native_name: {value: "Arthur Schopenhauer", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "German; same spelling."}
  aliases:
    - {name: "Arthur-Schopenhauer", kind: "roster alias"}
    - {name: "Schopenhauer-Arthur", kind: "roster alias"}

basics:
  birth:
    date: {value: "1788-02-22", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Danzig, Prussia", modern_name: "Gdańsk, Poland", polity_then: "Free City of Danzig (Polish–Lithuanian Commonwealth protection)", certainty: 0.5, cites: [{source: S1, locator: "opening; 'In 1793, when Danzig came under Prussian sovereignty'"}], how_known: "Britannica gives 'Danzig, Prussia [now Gdańsk, Poland]' but also says Danzig came under Prussian sovereignty only in 1793; polity_then is the coder's reconciliation."}
  death:
    date: {value: "1860-09-21", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Frankfurt am Main", modern_name: "Frankfurt am Main, Germany", polity_then: "Free City of Frankfurt", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; polity_then is the coder's addition."}
  first_lasting_contribution_year: {value: 1819, certainty: 0.5, cites: [{source: S1, locator: "'Active maturity'"}], how_known: "Die Welt als Wille und Vorstellung (1819), 'his main work'; 'The book marked the summit of Schopenhauer's thought' (S1). On the Fourfold Root (1813) is dated but not marked as lasting (P13)."}
  era_bucket: {value: "1750 to 1849", certainty: 0.5, cites: [{source: S1, locator: "'Active maturity'"}], how_known: "From 1819 (P2)."}
  region_of_birth: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Poland (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "'Active maturity'; 'Scholarly retirement in Frankfurt'"}], how_known: "Dresden, Berlin, Frankfurt (Germany)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [German], certainty: 0.7, cites: [{source: S1, locator: "titles"}], how_known: "Britannica (German titles)."}
  occupations: {value: ["philosopher", "privatdozent (University of Berlin)"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Active maturity'"}], how_known: "Britannica."}

contribution:
  fields: {value: ["metaphysics", "aesthetics", "ethics"], certainty: 0.7, cites: [{source: S1, locator: "'Active maturity'"}], how_known: "Britannica (the four books of the main work)."}
  lasting_original_contributions:
    - {value: "The World as Will and Idea (Die Welt als Wille und Vorstellung): the metaphysics of the will", year: 1819, kind: work, lasting: "'The book marked the summit of Schopenhauer's thought' (S1); influenced existential philosophy and Freudian psychology (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Active maturity'"}], how_known: "Britannica."}
    - {value: "Parerga und Paralipomena", year: 1851, kind: work, lasting: "'brought the beginning of worldwide recognition' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Scholarly retirement in Frankfurt'"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "'His writings influenced later existential philosophy and Freudian psychology'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Die Welt als Wille und Vorstellung (2nd ed. with a second volume, 1844)", year: 1819, kind: book, certainty: 0.7, cites: [{source: S1, locator: "'Active maturity'; 'Scholarly retirement in Frankfurt'"}], how_known: "Britannica."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father Heinrich Floris Schopenhauer, wealthy merchant (died April 1805)", role: father, certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica."}
    - {value: "Mother Johanna Schopenhauer, later a novelist and travel writer", role: mother, certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica."}
  household_circumstances: {value: "Wealthy merchant family; moved from Danzig to Hamburg in 1793", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica."}
  schooling:
    - {value: "Private education, then a private business school (where he met 'a Pietistic attitude')", stage: tutor, years: UNKNOWN, certainty: 0.5, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica ('a gentlemanly private education'); stage is the coder's reading."}
    - {value: "University of Göttingen (medicine, then humanities), 1809–1811; Berlin 1811–1813; PhD Jena 1813", stage: university, years: "1809–1813", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Lectures mainly on the natural sciences at Göttingen (age 21)", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica; adult, not childhood."}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [German], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "Death of his father, April 1805", year: 1805, age: 17, certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1819–1851", certainty: 0.5, cites: [{source: S1, locator: "'Active maturity'; 'Scholarly retirement in Frankfurt'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not scored at this reading."}
  primary_system:
    value: IDEAL
    basis: written_profession
    certainty: 0.5
    cites: [{source: S2, locator: "vol. 1, §1"}, {source: S1, locator: "'Active maturity'"}]
    rationale: "The main work opens: '\"The world is my idea:\"—this is a truth which holds good for everything that lives' (S2, §1); Britannica: the world 'is only comprehensible with the aid of the constructs of man's intellect—space, time, and causality', showing it 'only as appearance' (S1). Named alternative: ATHE. He denies God (A below), but the ATHE label adds that nature is all there is, and for him the thing-in-itself, the will, lies outside the phenomenal world."
    how_known: "Published main work in a web copy of a translation (0.7 ceiling); 0.5 because an alternative is named and Britannica says the doctrine arose 'in immediate reaction against Hegelian idealism', so the IDEAL label is the coder's fit."
  secondary_system: {value: UNKNOWN, how_known: "Affinity with Vedanta and Buddhism (S1) is influence, not membership."}
  candidate_codes_considered:
    - {code: IDEAL, reason: "Transcendental idealism: the world as representation."}
    - {code: ATHE, reason: "Explicit atheism (S3), but not naturalism."}
    - {code: KANT, reason: "Builds on Kant (S1) but rejects Kant's moral theology."}
    - {code: BUDDH, reason: "Affinity only, no membership."}
  lio_axes:
    A_locus:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S2, locator: "vol. 3, ch. L ('Epiphilosophy')"}, {source: S3, locator: "§4"}]
      rationale: "No God (P38): 'With the Pantheists, then, I have certainly that ἑν και παν in common, but not the παν θεος; because I do not go beyond experience' (vol. 3, ch. L), and 'the world exists, with me as with Spinoza, by its inner power and through itself' (same chapter). SEP: 'Within Schopenhauer's vision of the world as Will, there is no God to be comprehended', and his thought 'assumed an explicitly atheistic quality' from 1814 (S3)."
      how_known: "Published main work (vol. 3 of the translation = the 1844 second volume), web copy of a translation, 0.7 ceiling; SEP agrees."
    B_cause:
      value: 4
      basis: written_profession
      certainty: 0.5
      cites: [{source: S2, locator: "vol. 1, §55; §68"}]
      rationale: "Account of nature (P6): 'The whole content of Nature, the collective sum of its phenomena, is thus throughout necessary, and the necessity of every part, of every phenomenon, of every event, can always be proved ... This admits of no exception: it follows from the unrestricted validity of the principle of sufficient reason' (§55). That is the explicit no-exception statement P40 asks for, with no lawgiver behind it. Named alternative 3: he names one exception himself, in man: the denial of the will 'by no means proceeds from suffering with the necessity of an effect from its cause, but the will remains free; for this is indeed the one point at which its freedom appears directly in the phenomenon' (§68), where freedom 'contradicts the phenomenon' yet 'may yet possibly, in his case, appear in the phenomenon also' (§55)."
      how_known: "Published main work, web copy of a translation; 0.5 because his own stated exception (human, not divine) is a named alternative."
    C_ledger:
      value: 3
      basis: written_profession
      certainty: 0.5
      cites: [{source: S2, locator: "vol. 1, §63"}]
      rationale: "An impersonal moral ledger with no judge: 'eternal justice ... rules not the state but the world ... infallible, fixed, and sure'; 'The punishment must here be so bound up with the offence that both are one'; 'the world itself is the judgment of the world'. He quotes Euripides against a Zeus who records and punishes sins. By analogy with the karma rule (P44(d)): C 3 at 0.5, alternative 4."
      how_known: "Published main work, web copy; scored by analogy, so 0.5."
    D_authority: {value: UNKNOWN, how_known: "Not scored at this reading; his critique of revelation in vol. 2 (ch. XVII) is a lead."}
    E_scope:
      value: 3
      basis: written_profession
      certainty: 0.5
      cites: [{source: S2, locator: "vol. 1, §55"}]
      rationale: "Scored on the world's order (P7). Necessity holds for every phenomenon, but man 'is distinguished from all the other phenomena of will by the fact that freedom ... may yet possibly, in his case, appear in the phenomenon also' (§55): one kind of being has an exception in this-world events. Alternative 4 if that freedom is read as outside nature."
      how_known: "Published main work, web copy; coder's reading, 0.5."
  mid_basin: {value: false, certainty: 0.7, cites: [{source: S2, locator: "vol. 3, ch. L"}, {source: S3, locator: "§4"}], how_known: "A 4 at 0.7: the A ≥ 3 branch reads A only (P10)."}
  statements:
    - text: "The whole content of Nature, the collective sum of its phenomena, is thus throughout necessary, and the necessity of every part, of every phenomenon, of every event, can always be proved, because it must be possible to find the reason from which it follows as a consequent. This admits of no exception: it follows from the unrestricted validity of the principle of sufficient reason."
      cites: [{source: S2, locator: "vol. 1, §55"}]
      date: "1819"
      context: "The World as Will and Idea, Book IV, §55 (first edition 1819; Haldane and Kemp translation)."
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-17
      note: "Checked word for word against the Gutenberg text of the translation."
    - text: "In general, the denial of the will to live by no means proceeds from suffering with the necessity of an effect from its cause, but the will remains free; for this is indeed the one point at which its freedom appears directly in the phenomenon"
      cites: [{source: S2, locator: "vol. 1, §68"}]
      date: "1819"
      context: "Book IV, §68, on the saint's denial of the will."
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-17
      note: "His own named exception; basis of the alternatives."
    - text: "the world itself is the judgment of the world"
      cites: [{source: S2, locator: "vol. 1, §63"}]
      date: "1819"
      context: "Book IV, §63, on eternal justice."
      axes: [C_ledger]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-17
    - text: "With the Pantheists, then, I have certainly that ἑν και παν in common, but not the παν θεος; because I do not go beyond experience (taken in its widest sense), and still less do I put myself in contradiction with the data which lie before me."
      cites: [{source: S2, locator: "vol. 3, ch. L ('Epiphilosophy')"}]
      date: "1844"
      context: "Supplements to Book IV, chapter 50, second edition (1844)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-17
  changes_over_life:
    - {value: "Called himself an 'illuminated theist' in his notebooks in 1812; explicitly atheistic from about 1814", year: 1814, age: 26, certainty: 0.5, cites: [{source: S3, locator: "§4 (Manuscript Remains, vol. 2, p. 373)"}], how_known: "SEP's reconstruction; notebooks not read."}
  coder_notes: "Coder's call. Gutenberg is a web copy of the Haldane–Kemp translation (1883–86), so 0.7 is the ceiling. B is 4 on the strength of 'This admits of no exception'; the 0.5 and alternative 3 record his own exception for the denial of the will, which is not divine action. Verified_against is 'scholarly edition' for the published translation."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German (Danzig merchant family)", certainty: 0.5, cites: [{source: S1, locator: "opening; 'Early life and education'"}], how_known: "Coder's reading."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1819–1851", certainty: 0.5, cites: [{source: S1, locator: "'Active maturity'; 'Scholarly retirement in Frankfurt'"}], how_known: "First to last listed lasting contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 31, certainty: 0.5, cites: [{source: S1, locator: "opening; 1819"}], how_known: "1819 − 1788 = 31 (P30)."}
  first_evidence_of_lio_type_views: {value: "1819: nature necessary without exception (WWR §55)", year: 1819, certainty: 0.5, cites: [{source: S2, locator: "vol. 1, §55"}], how_known: "SEP dates explicit atheism to about 1814 (notebooks, not read)."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S2, locator: "vol. 1, §55; vol. 3, ch. L"}], how_known: "Stated in the main work itself (1819, 1844)."}
  worldview_during_major_work: {value: "No God; the will as thing-in-itself; phenomena necessary without exception, except freedom in the denial of the will", certainty: 0.5, cites: [{source: S2, locator: "vol. 1, §§55, 68; vol. 3, ch. L"}], how_known: "Coder's summary."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not read for this.", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Not read."}
  circle_present: {value: "no", rationale: "No God as source or end; the will 'with no end in view' (S3).", certainty: 0.5, cites: [{source: S3, locator: "§4"}], how_known: "Coder's reading."}
  reading: "No God; one blind will behind necessary appearances."
  notes: ""

institutions:
  - {value: "University of Berlin", role: "lecturer (privatdozent)", years: "1820–1831", kind: university, certainty: 0.5, cites: [{source: S1, locator: "'Active maturity'"}], how_known: "Britannica: qualified March 1820, 'a member of the university for 24 semesters', only his first lecture held; end year computed."}
collaborators:
  - {value: "Johann Wolfgang von Goethe", relation: "influenced by", note: "discussed philosophy with him in Weimar, 1813–14; On Vision and Colours (1816) supports Goethe against Newton", certainty: 0.7, cites: [{source: S1, locator: "'Active maturity'"}], how_known: "Britannica."}
  - {value: "G.W.F. Hegel", relation: "rival or critic", note: "scheduled his lectures against Hegel's", certainty: 0.7, cites: [{source: S1, locator: "'Active maturity'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 85"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Main work read in a web copy of a 19th-century translation; German original not compared."
  open_questions:
    - "Does his own exception (freedom appearing in the phenomenon in the denial of the will, §§55, 68) keep B below 4 under P40? Scored 4 at 0.5 with alternative 3."
    - "Check the German original of §55 and ch. 50 (Löhneysen or Hübscher edition)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Arthur Hübscher"
    citation: "Hübscher, Arthur. \"Arthur Schopenhauer.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Arthur-Schopenhauer. Read in Wayback snapshots: main page 20261001181634; 'Scholarly retirement in Frankfurt' 20260926092729."
    url: "https://www.britannica.com/biography/Arthur-Schopenhauer"
    accessed: 2026-10-17
    reliability_note: "Signed article (director, Schopenhauer Archives). Body only; Top Questions not cited."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Arthur Schopenhauer"
    citation: "Schopenhauer, Arthur. The World as Will and Idea. Translated by R. B. Haldane and J. Kemp. 3 vols. London: Trübner, 1883–86. Project Gutenberg #38427 (vol. 1) and #40868 (vol. 3). https://www.gutenberg.org/ebooks/38427; https://www.gutenberg.org/ebooks/40868"
    url: "https://www.gutenberg.org/ebooks/38427"
    accessed: 2026-10-17
    reliability_note: "Web copy of a published translation (0.7 ceiling); quotations checked word for word."
    used_for: [worldview, timing, lane_b]
  - id: S3
    type: tertiary
    kind: encyclopedia
    author: "Robert Wicks"
    citation: "Wicks, Robert. \"Arthur Schopenhauer.\" Stanford Encyclopedia of Philosophy (substantive revision 9 September 2021). https://plato.stanford.edu/entries/schopenhauer/"
    url: "https://plato.stanford.edu/entries/schopenhauer/"
    accessed: 2026-10-17
    reliability_note: "Signed SEP entry, read directly."
    used_for: [worldview, lane_b]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-17
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Arthur Schopenhauer

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Arthur Schopenhauer (1788–1860), German philosopher of the will [S1]. Draft: primary_system IDEAL (0.5, alt ATHE); A 4 at 0.7; B 4 at 0.5 (alt 3); C 3 at 0.5; E 3 at 0.5; mid_basin false (0.7). Plotted (faded).

## Life and work

Dresden, Berlin, then Frankfurt from 1833 [S1].

## Contribution and impact

The World as Will and Idea (1819), Parerga und Paralipomena (1851) [S1].

## Childhood and education

Son of a Danzig merchant and the writer Johanna Schopenhauer [S1].

## Adult working worldview

Nature necessary without exception [S2, vol. 1, §55], save freedom in the denial of the will [S2, §68]; no God [S2, vol. 3, ch. L; S3].

## Heritage (context only)

Danzig merchant family [S1].

## Timing

First lasting contribution 1819, at 31 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle [S3].

## Open questions

- Does his own exception keep B below 4?

## Research log

- 2026-10-17: Read Britannica (Hübscher) in Wayback copies, SEP (Wicks) and the Gutenberg translation (vols. 1 and 3) directly; quotations checked word for word.
