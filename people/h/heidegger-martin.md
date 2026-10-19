---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch U)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch U, order P32: F 4, rank 115). Basics from Britannica (Arne D. Naess), SEP (Mark Wrathall) and IEP (W. J. Korab-Karpowicz). No text of his own on God or nature read: Phänomenologie und Theologie (1927) and the 1919 letter are leads only (P26). Not a scientist (P30). primary_system BELOW_THRESHOLD; A BELOW_THRESHOLD; B UNKNOWN; C UNKNOWN; D BELOW_THRESHOLD; E UNKNOWN; mid_basin UNKNOWN. Single-year span 1927 (Being and Time). Not plotted. Draft, not reviewed."}

identity:
  id: heidegger-martin
  display_name: "Martin Heidegger"
  roster:
    canonical_name: "Martin Heidegger"
    rank: 115
    F: 4
    models: [Claude, DeepSeek, Gemini, Grok]
    band: "core (3–4)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Martin Heidegger", certainty: 0.7, cites: [{source: S1, locator: "facts box"}, {source: S2, locator: "§1 Life and Work"}], how_known: "Britannica and SEP."}
  native_name: {value: "Martin Heidegger", certainty: 0.7, cites: [{source: S1, locator: "facts box"}], how_known: "German; same as the full name."}
  aliases:
    - {name: "Heidegger-Martin", kind: "roster alias"}

basics:
  birth:
    date: {value: "1889-09-26", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "facts box (Born)"}, {source: S2, locator: "§1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}], how_known: "Britannica, SEP and IEP agree."}
    place: {value: "Messkirch", modern_name: "Meßkirch, Baden-Württemberg, Germany", polity_then: "Grand Duchy of Baden, German Empire", certainty: 1.0, cites: [{source: S1, locator: "facts box (Born)"}, {source: S2, locator: "§1 Life and Work"}], how_known: "Britannica and SEP; polity the coder's."}
  death:
    date: {value: "1976-05-26", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "facts box (Died)"}, {source: S3, locator: "§1 Life and Works, last paragraph"}], how_known: "Britannica and IEP."}
    place: {value: "Freiburg im Breisgau", modern_name: "Freiburg im Breisgau, Germany", polity_then: "West Germany", certainty: 0.7, cites: [{source: S1, locator: "facts box (Died)"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1927, certainty: 0.7, cites: [{source: S2, locator: "§1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}], how_known: "Being and Time, published February 1927 (S3)."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S3, locator: "§1 Life and Works"}], how_known: "1927 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "facts box"}], how_known: "Germany (P3)."}
  region_of_work: {value: "Western Europe", certainty: 1.0, cites: [{source: S2, locator: "§1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}], how_known: "Freiburg and Marburg."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S2, locator: "§1 Life and Work"}], how_known: "Pronouns in SEP."}
  languages_of_work: {value: ["German"], certainty: 0.7, cites: [{source: S2, locator: "§1 Life and Work"}], how_known: "Coder's reading."}
  occupations: {value: ["philosopher", "university lecturer and professor (Freiburg, Marburg)", "rector of the University of Freiburg (1933–1934)"], certainty: 0.7, cites: [{source: S2, locator: "§1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}], how_known: "SEP and IEP."}

contribution:
  fields: {value: ["philosophy", "phenomenology", "ontology"], certainty: 0.7, cites: [{source: S2, locator: "opening"}, {source: S3, locator: "opening"}], how_known: "SEP and IEP."}
  lasting_original_contributions:
    - {value: "Being and Time (Sein und Zeit): the question of the meaning of being pursued through a phenomenological analysis of human existence (Dasein) and its temporality", year: 1927, kind: work, lasting: "'his most important work' (S2); 'recognized as a truly epoch-making work of 20th century philosophy' and 'his most influential work' (S3)", certainty: 1.0, cites: [{source: S2, locator: "opening; §1 Life and Work"}, {source: S3, locator: "§1 Life and Works; §3"}], how_known: "SEP and IEP. The only contribution the sources read call lasting in so many words. Not a theory about natural systems, so not a scientist (P30)."}
  evidence_of_impact:
    - {value: "Being and Time influenced Arendt, Sartre, Beauvoir, Merleau-Ponty, Gadamer, Derrida, Foucault, Deleuze, the Frankfurt School, the Kyoto School and fields from theology to cognitive science", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "SEP."}
    - {value: "Being and Time 'generated a level of excitement that few other works of philosophy have matched'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "'Being and Time'"}], how_known: "Britannica."}
  major_works:
    - {value: "Sein und Zeit (Being and Time)", year: 1927, certainty: 1.0, cites: [{source: S2, locator: "§1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}], how_known: "SEP and IEP."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Being and Time 'profoundly influenced' twentieth-century philosophy (S2).", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "SEP."}

childhood:
  family_religion: {value: "Catholic", certainty: 1.0, cites: [{source: S2, locator: "§1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}], how_known: "Father a sexton in the Catholic Church (S2); 'a Catholic family' (S3)."}
  family_religious_practice: {value: "Father served as sexton of the local church; the son was prepared for the priesthood", certainty: 0.7, cites: [{source: S3, locator: "§1 Life and Works"}], how_known: "IEP."}
  parents_and_household:
    - {value: "Father: Friedrich Heidegger, master cooper and sexton in the Catholic Church", certainty: 1.0, cites: [{source: S2, locator: "§1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}], how_known: "SEP and IEP."}
  household_circumstances: {value: "Provincial craftsman's family in a small rural town; conservative upbringing", certainty: 0.7, cites: [{source: S2, locator: "§1 Life and Work"}], how_known: "SEP."}
  schooling:
    - {value: "High school in Konstanz from 1903, with a church scholarship", stage: "grammar or secondary school", run_by: other, years: "1903–1906", certainty: 0.7, cites: [{source: S3, locator: "§1 Life and Works"}], how_known: "IEP; who ran the school is not stated, the scholarship came from the church."}
    - {value: "High school in Freiburg", stage: "grammar or secondary school", run_by: other, years: "1906–1909", certainty: 0.7, cites: [{source: S3, locator: "§1 Life and Works"}], how_known: "IEP; operator not stated."}
    - {value: "Jesuit novitiate, discharged within a month for health", stage: other, run_by: "religious body", years: "1909", certainty: 0.7, cites: [{source: S3, locator: "§1 Life and Works"}], how_known: "IEP."}
    - {value: "University of Freiburg: Catholic theology (seminary), then philosophy, mathematics and natural sciences; doctorate 1913; habilitation on Duns Scotus 1915", stage: university, run_by: "state or municipal", years: "1909–1915", certainty: 0.7, cites: [{source: S2, locator: "§1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}], how_known: "SEP and IEP; operator the coder's reading (German state university)."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Studied mathematics and natural sciences at Freiburg after leaving the seminary in 1911", certainty: 0.7, cites: [{source: S3, locator: "§1 Life and Works"}], how_known: "IEP."}
  key_early_reading:
    - {value: "Franz Brentano, On the Manifold Meaning of Being according to Aristotle (read at seventeen; 'by his own account' the start of his quest for the meaning of being)", certainty: 0.7, cites: [{source: S3, locator: "§1 Life and Works"}], how_known: "IEP."}
    - {value: "Edmund Husserl, Logical Investigations", certainty: 0.7, cites: [{source: S3, locator: "§1 Life and Works"}], how_known: "IEP."}
  childhood_mentors: []
  languages_in_childhood: {value: ["German"], certainty: 0.5, cites: [{source: S2, locator: "§1 Life and Work"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "Prepared for the priesthood; Jesuit novice in 1909; left the seminary in 1911", certainty: 0.7, cites: [{source: S3, locator: "§1 Life and Works"}], how_known: "IEP."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1927", certainty: 0.5, cites: [{source: S2, locator: "§1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Raised Catholic; in 1915 'regarded himself as standing in the service of the Catholic world-view'", certainty: 0.7, cites: [{source: S3, locator: "§1 Life and Works"}], how_known: "IEP's report; before the span and before the 1919 break. Context, not a code."}
    - {value: "Buried in the churchyard in Messkirch", certainty: 0.7, cites: [{source: S3, locator: "§1 Life and Works, last paragraph"}], how_known: "IEP. Context only."}
  self_described_science_religion_relation: {value: BELOW_THRESHOLD, how_known: "Lead only: the 1927 lecture Phänomenologie und Theologie (in Wegmarken / Pathmarks, S3 bibliography) sets faith against philosophy; seen only as a secondary quotation, not checked against the text (P26)."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "No statement of his own on God's existence or nature in the working span was read. He broke with the 'system of Catholicism' on 9 January 1919 (S3, reporting his letter; the letter not read), and Britannica says the framework of Being and Time is 'suffused by a sensibility—derived from secularized Protestantism' (S1), a reading of the book's tone, not a profession. Candidates CHRIST, ATHE and AGNOS all need his own words."}
  secondary_system: {value: UNKNOWN, how_known: "One system (P29)."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Rejected: Catholic until 1919 (S3) and a 'secularized Protestant' sensibility (S1); no profession in the span read."}
    - {code: ATHE, reason: "Rejected: no denial of God read."}
    - {code: AGNOS, reason: "Rejected: no stated suspension read; the 'methodological atheism' readings in the literature are leads."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "No locus view in his words read; the break with the Catholic 'system' (S3) does not say what, if anything, replaced it."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); the sources read say nothing of his on natural law or exception (P16, P19). Being and Time's discussion of 'reality' (S2 §2.6) is about realism, not lawfulness."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing on reward and punishment of persons read (P19)."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "Lead only: Phänomenologie und Theologie (lecture 1927, published 1970) is reported to call faith the 'mortal enemy' (Todfeind) of philosophy, which would read as two separate domains (D 2 candidate). Seen only as a secondary quotation; the primary text was not reachable (P26)."}
    E_scope: {value: UNKNOWN, how_known: "Nothing on the world's order read (P7, P19)."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN, which takes precedence (P19)."}
  statements: []
  changes_over_life:
    - {value: "Catholic: in 1915 'in the service of the Catholic world-view'; announced his break with the 'system of Catholicism' on 9 January 1919, after marrying the Protestant Elfride Petri in 1917", certainty: 0.7, cites: [{source: S3, locator: "§1 Life and Works"}], how_known: "IEP; before the 1927 span."}
  coder_notes: "Coder's call. The span is one year (Being and Time, 1927), the only contribution the sources read call lasting; SEP's 'his many essays and lectures ... profoundly influenced' (S2, opening) is the named alternative for a longer span, but names no dated item. No primary text on God or nature was reached: the Bard digital-commons copy of Phenomenology and Theology sat behind a Cloudflare check, and Internet Archive copies are access-restricted. Leads: Phänomenologie und Theologie (1927); the letter to Engelbert Krebs (9 January 1919); the Spiegel interview (1966, published 1976; after the span). Not plotted."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German (Swabian-Badenese provincial)", certainty: 0.5, cites: [{source: S2, locator: "§1 Life and Work"}], how_known: "Coder's reading of 'southwest Germany'."}
  religious_heritage_by_birth: {value: "Catholic", certainty: 1.0, cites: [{source: S2, locator: "§1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}], how_known: "SEP and IEP."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1927", certainty: 0.5, cites: [{source: S2, locator: "§1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}], how_known: "Only one dated lasting contribution (P29, P30, P39; Wiles, Rembrandt and Edison precedents). Coder's call: the later essays are named in SEP's opening but undated and unranked, so they do not extend the span."}
  age_at_first_lasting_contribution: {value: 38, certainty: 0.7, cites: [{source: S1, locator: "facts box"}, {source: S3, locator: "§1 Life and Works"}], how_known: "1927 − 1889 = 38 (P30); 37 in February 1927."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No LIO-type statement read."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S3, locator: "§1 Life and Works"}], how_known: "None in the sources read."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "§2"}], how_known: "Not assessed."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S3, locator: "§1 Life and Works"}], how_known: "Not read."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S2, locator: "§2"}], how_known: "Coder's reading."}
  reading: "The question of the meaning of being, approached through temporal human existence."
  notes: ""

institutions:
  - {value: "University of Freiburg", role: "Privatdozent, then Husserl's assistant (1919)", years: "1915–1923", kind: university, certainty: 0.7, cites: [{source: S2, locator: "§1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}], how_known: "SEP and IEP."}
  - {value: "University of Marburg", role: "associate professor, full professor 1927", years: "1923–1928", kind: university, certainty: 1.0, cites: [{source: S2, locator: "§1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}], how_known: "SEP and IEP."}
  - {value: "University of Freiburg", role: "chair of philosophy (succeeding Husserl); rector April 1933 – April 1934; dismissed 1946, ban lifted 1949", years: "1928–1946", kind: university, certainty: 0.7, cites: [{source: S2, locator: "§1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}], how_known: "SEP and IEP."}
collaborators:
  - {value: "Edmund Husserl", relation: "mentor or employer", note: "Heidegger was his assistant from 1919; Being and Time is dedicated to him", certainty: 1.0, cites: [{source: S2, locator: "§1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}], how_known: "SEP and IEP."}
  - {value: "Heinrich Rickert", relation: teacher, note: "directed the doctorate (IEP) and the habilitation (SEP)", certainty: 0.7, cites: [{source: S2, locator: "§1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}], how_known: "SEP and IEP."}
  - {value: "Hannah Arendt", relation: "student or assistant", note: "student at Marburg; long relationship", certainty: 0.7, cites: [{source: S2, locator: "§1 Life and Work"}], how_known: "SEP."}
  - {value: "Ernst Cassirer", relation: "rival or critic", note: "Davos disputation, 1929", certainty: 0.7, cites: [{source: S2, locator: "§1 Life and Work"}], how_known: "SEP."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 115"}], how_known: "Study roster."}
  controversies:
    - {value: "Nazi Party member from May 1933; rector of Freiburg 1933–34; dismissed from his chair in 1946", certainty: 1.0, cites: [{source: S2, locator: "§1 Life and Work; §3"}, {source: S3, locator: "§1 Life and Works"}], how_known: "SEP and IEP."}
  data_quality_flags:
    - "No primary text on God or nature read; every worldview field rests on encyclopedia reports."
    - "Single-year span (1927)."
  open_questions:
    - "Read Phänomenologie und Theologie (1927) in Wegmarken (GA 9) for D and the God question."
    - "Read the 9 January 1919 letter to Engelbert Krebs."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Arne D. Naess (Britannica)"
    citation: "Naess, Arne D. \"Martin Heidegger.\" Encyclopaedia Britannica (updated 22 September 2026). https://www.britannica.com/biography/Martin-Heidegger-German-philosopher. Read live 2026-10-19."
    url: "https://www.britannica.com/biography/Martin-Heidegger-German-philosopher"
    accessed: 2026-10-19
    reliability_note: "Signed article; the fetched text stopped after the 'Being and Time' section; facts box and body cited, question boxes not."
    used_for: [identity, basics, contribution, worldview]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Mark Wrathall"
    citation: "Wrathall, Mark. \"Martin Heidegger.\" Stanford Encyclopedia of Philosophy (2025 revision). https://plato.stanford.edu/entries/heidegger/"
    url: "https://plato.stanford.edu/entries/heidegger/"
    accessed: 2026-10-19
    reliability_note: "Signed scholarly encyclopedia; opening and §1 used, §2.6 checked."
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, collaborators, review]
  - id: S3
    type: tertiary
    kind: encyclopedia
    author: "W. J. Korab-Karpowicz"
    citation: "Korab-Karpowicz, W. J. \"Martin Heidegger (1889–1976).\" Internet Encyclopedia of Philosophy. https://iep.utm.edu/heidegge/"
    url: "https://iep.utm.edu/heidegge/"
    accessed: 2026-10-19
    reliability_note: "Signed scholarly encyclopedia; §1 Life and Works and the bibliography used."
    used_for: [basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators, review]
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

# Martin Heidegger

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Martin Heidegger (1889–1976), German philosopher, author of Being and Time (1927) [S2, S3]. Draft: primary_system BELOW_THRESHOLD; A BELOW_THRESHOLD; B UNKNOWN; mid_basin UNKNOWN. Not plotted.

## Life and work

Freiburg, Marburg, Freiburg; rector 1933–34 and Nazi Party member [S2, S3].

## Contribution and impact

Being and Time, 'a truly epoch-making work' [S3].

## Childhood and education

Son of a Catholic sexton, prepared for the priesthood; Jesuit novice in 1909 [S2, S3].

## Adult working worldview

Broke with the 'system of Catholicism' in 1919 [S3]; no statement of his own on God or nature read.

## Heritage (context only)

Catholic [S2, S3].

## Timing

1927, at 38 [S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Not assessed.

## Open questions

- Phänomenologie und Theologie (1927); the 1919 letter to Krebs.

## Research log

- 2026-10-19: Read Britannica (to the Being and Time section), SEP and IEP. Primary texts behind Cloudflare or access-restricted.
