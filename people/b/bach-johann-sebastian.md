---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch G)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-15
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch G, order P32: F 5, rank 44). Basics from Britannica (Emery). Worldview evidence: one marginal note in his Calov Bible (2 Chronicles 5:13), read only as quoted on the Bach studies site (bach-studies.wursten.be); his lifelong Lutheran church posts (S1). primary_system CHRIST at 0.5 (inferred from work and conduct, P24); A BELOW_THRESHOLD; B, C, D, E UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: bach-johann-sebastian
  display_name: "Johann Sebastian Bach"
  roster:
    canonical_name: "Johann Sebastian Bach"
    rank: 44
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: music
    field_bucket: music
  full_name: {value: "Johann Sebastian Bach", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  native_name: {value: UNKNOWN, how_known: "German in Latin script."}
  aliases:
    - {name: "Bach-Johann Sebastian", kind: "roster alias"}
    - {name: "Johann-Sebastian-Bach", kind: "roster alias"}

basics:
  birth:
    date: {value: "1685-03-21", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica: 'March 21 [March 31, New Style], 1685'. Protestant Thuringia used the Julian calendar until 1700, so the source date is kept as julian (data dictionary)."}
    place: {value: "Eisenach, Thuringia", modern_name: "Eisenach, Germany", polity_then: "Ernestine Saxon Duchies (Saxe-Eisenach)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1750-07-28", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening; 'Last years'"}], how_known: "Britannica."}
    place: {value: "Leipzig", modern_name: "Leipzig, Germany", polity_then: "Electorate of Saxony", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1708, certainty: 0.5, cites: [{source: S1, locator: "'The Mühlhausen period'"}], how_known: "Cantata No. 71, Gott ist mein König, 4 February 1708, his first published composition (S1). Earlier works (Capriccio BWV 992, 1704) are dated only by ascription 'with anything more than a show of plausibility' (S1), so the year might be earlier (0.5)."}
  era_bucket: {value: "1600 to 1749", certainty: 0.7, cites: [{source: S1, locator: "'The Mühlhausen period'"}], how_known: "From 1708 (P2); any earlier work also falls in the bucket."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Germany is Western Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "career sections"}], how_known: "Arnstadt, Mühlhausen, Weimar, Köthen, Leipzig."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [German], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's inference from his posts and texts set; not stated."}
  occupations: {value: ["composer", "organist", "Kapellmeister", "cantor"], certainty: 0.7, cites: [{source: S1, locator: "career sections"}], how_known: "Britannica."}

contribution:
  fields: {value: ["music"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Cantata No. 71, Gott ist mein König, his first published composition", year: 1708, kind: work, lasting: "first of the cantata output (S1)", certainty: 0.7, cites: [{source: S1, locator: "'The Mühlhausen period'"}], how_known: "Britannica."}
    - {value: "Brandenburg Concertos", year: 1721, kind: work, lasting: "among the works he is 'celebrated as the creator of' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'The Köthen period'"}], how_known: "Finished by 24 March 1721 (S1)."}
    - {value: "The Well-Tempered Clavier, Book 1", year: 1722, kind: work, lasting: "named in Britannica's lead (S1)", certainty: 0.7, cites: [{source: S1, locator: "'The Köthen period'"}], how_known: "Britannica."}
    - {value: "St. Matthew Passion", year: 1729, kind: work, lasting: "(S1)", certainty: 0.7, cites: [{source: S1, locator: "'Symbolism'"}], how_known: "Britannica."}
    - {value: "The Musical Offering", year: 1747, kind: work, lasting: "(S1)", certainty: 0.7, cites: [{source: S1, locator: "'Last years'"}], how_known: "Britannica; The Art of the Fugue was unfinished and posthumous (1751), so the period ends at 1747 (P30)."}
  evidence_of_impact:
    - {value: "'generally regarded as one of the greatest composers of all time'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Canonical composer (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Lutheran", certainty: 0.5, cites: [{source: S1, locator: "opening (Veit Bach, 'a Lutheran baker'); 'Early years'"}], how_known: "Inferred: Britannica calls his ancestor Veit Bach Lutheran and has the boy attending the Georgenkirche; the parents' confession is not stated (0.5)."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father Johann Ambrosius Bach, string player for the town council and ducal court; mother Elisabeth Lämmerhirt; both dead by 1695", role: parents, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
    - {value: "Eldest brother Johann Christoph, organist at Ohrdruf, took him in", role: guardian, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  household_circumstances: {value: "Orphaned by 1695 (age 10)", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  schooling:
    - {value: "School at Eisenach", stage: "grammar or secondary school", run_by: "other", years: "1692 or 1693–", ages: "7–", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
    - {value: "School at the Michaelskirche, Lüneburg (choir of poor boys)", stage: "grammar or secondary school", run_by: "religious body", years: "1700–1702", ages: "15–17", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Johann Christoph Bach (brother), first formal keyboard lessons", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  languages_in_childhood: {value: TODO}
  notable_events:
    - {value: "Both parents dead", year: 1695, age: 10, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1708–1747", certainty: 0.5, cites: [{source: S1, locator: "career sections"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Lutheran church (official posts as organist and cantor)", certainty: 0.7, cites: [{source: S1, locator: "'The Arnstadt period'; 'Years at Leipzig'"}], how_known: "Britannica: 'the orthodox Lutheran service'; director of church music for Leipzig."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read on science and religion."}
  primary_system:
    value: CHRIST
    basis: inference_from_work
    certainty: 0.5
    cites: [{source: S1, locator: "'The Arnstadt period'; 'Years at Leipzig'"}, {source: S2, locator: "2 Chronicles 5:13 annotation"}]
    rationale: "Lifelong Lutheran church musician (S1); his own marginal note in Calov's Lutheran Bible commentary says God is always present with his grace in devotional music (S2). Conduct and one private note read in secondary quotation, so inference_from_work at 0.5 (P24). No statement on revelation, so DEISM is not in play (P27)."
    how_known: "Inferred from his posts and one annotation; The site lists four musical annotations, only one quoted in full here."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Chosen at 0.5: Lutheran posts and Calov annotation."}
    - {code: CLTHEI, reason: "Not chosen: the annotation speaks of God's gracious presence, not intervention in events."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "The Calov note (S2) names God's 'Gnadengegenwart' (gracious presence) in devotional music, which implies a personal God but says nothing on where God is relative to the world. One private note, secondary quotation.", note: "Heritage and church posts are not a locus statement (§1)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); no statement on the order of nature read (P16)."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN, which takes precedence (§6, P19)."}
  statements:
    - text: "NB. Bey einer andächtigen Musique ist allezeit Gott mit seiner Gnadengegenwart."
      cites: [{source: S2, locator: "'II Chron 5:13' entry"}]
      context: "Marginal note in his copy of Abraham Calov's Bible commentary, beside 2 Chronicles 5:13 (the cloud filling the temple as the priests make music). The site's English: 'When devotional music is performed, God is always there with his graceful presence.'"
      axes: [A_locus]
      kind: "document in own hand"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "Primary check pending against Bach-Dokumente (the note is reported as printed in Bach-Dokumente III, ed. H.-J. Schulze, 1972, via a blog citing Badura-Skoda; not read) or a facsimile of the Calov Bible (Concordia Seminary, St. Louis). Date of the note not established (no date field). Spelling varies between copies ('Musiq'/'Musique', 'Gnaden Gegenwart'/'Gnadengegenwart'); the site's spelling is kept."
  changes_over_life: []
  coder_notes: "Coder's call: primary_system CHRIST at 0.5 from conduct and one note; A BELOW_THRESHOLD because 'gracious presence' does not locate God. The 'S.D.G.' / 'J.J.' score headings and the 1738 thoroughbass precepts ('the glory of God') were not read in a citable text; the precepts are also of disputed authorship (adapted from Niedt), which would bring P42 into play."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German (Thuringian musical family)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Lutheran", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Inferred from the family's Lutheran ancestry (S1)."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1708–1747", certainty: 0.5, cites: [{source: S1, locator: "'The Mühlhausen period'; 'Last years'"}], how_known: "1708 to 1747, first to last listed lasting contribution (P29, P30); the start year might be earlier (0.5)."}
  age_at_first_lasting_contribution: {value: 23, certainty: 0.5, cites: [{source: S1, locator: "opening; 'The Mühlhausen period'"}], how_known: "1708 − 1685 = 23 (P30); start year at 0.5."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No LIO-type view read."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Nothing read."}
  worldview_during_major_work: {value: "CHRIST", certainty: 0.5, cites: [{source: S1, locator: "'Years at Leipzig'"}], how_known: "As primary_system."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Fugue and canon are rule-governed forms (S1), but that is music, not geometry.", certainty: 0.5, cites: [{source: S1, locator: "'The Köthen period'"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Early years'"}], how_known: "Nothing on mathematics."}
  circle_present: {value: "unclear", rationale: "No statement on God and nature.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No reading possible: worldview not documented beyond church practice and one note."
  notes: ""

institutions:
  - {value: "Thomaskirche and Thomasschule, Leipzig", role: "cantor and director of church music", years: "1723–1750", kind: "religious body", certainty: 0.7, cites: [{source: S1, locator: "'Years at Leipzig'"}], how_known: "Britannica."}
  - {value: "Court of Prince Leopold of Köthen", role: "musical director", years: "1717–1723", kind: "employer", certainty: 0.7, cites: [{source: S1, locator: "'The Köthen period'"}], how_known: "Britannica."}
collaborators:
  - {value: "Johann Matthias Gesner", relation: other, note: "rector of the Thomasschule, an admirer", certainty: 0.7, cites: [{source: S1, locator: "'Nonmusical duties'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 44"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags: []
  open_questions:
    - "Leads from fallacy_catalog's audit of 5ff29b4, not added as sources because their full bibliographic details were not verified: a Van Wijnen (2017) facsimile of the 2 Chronicles page, shown on the Bach studies site (reading 'Musiq[ue]'), and Renate Steiger's essay on 'Gnadengegenwart'."
    - "Read the Calov annotations in Leaver (ed.), J. S. Bach and Scripture (Concordia, 1985) or Bach-Dokumente; check a second biography (Wolff) for basics."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Walter Emery"
    citation: "Emery, Walter. \"Johann Sebastian Bach.\" Encyclopaedia Britannica, updated 25 August 2026. https://www.britannica.com/biography/Johann-Sebastian-Bach."
    url: "https://www.britannica.com/biography/Johann-Sebastian-Bach"
    accessed: 2026-10-15
    reliability_note: "Signed article body; the Top Questions box is not used."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "Bach studies (bach-studies.wursten.be)"
    citation: "\"Bach's annotations in Calov's Bible commentary.\" Bach studies. https://bach-studies.wursten.be/bachs-annotations/."
    url: "https://bach-studies.wursten.be/bachs-annotations/"
    accessed: 2026-10-15
    reliability_note: "Personal research site on Bach and the Calov Bible; not peer-reviewed; secondary quotation only. Author not named in the page text read; the site name is used."
    used_for: [worldview]
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

# Johann Sebastian Bach

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Johann Sebastian Bach (1685–1750), German Baroque composer and organist: Brandenburg Concertos, The Well-Tempered Clavier, St. Matthew Passion, Mass in B Minor [S1]. Draft: primary_system CHRIST at 0.5; A BELOW_THRESHOLD; B, C, D, E UNKNOWN; mid_basin UNKNOWN. Not plotted.

## Life and work

Arnstadt, Mühlhausen, Weimar, Köthen; cantor at Leipzig from 1723 [S1].

## Contribution and impact

Cantatas, Passions, keyboard and orchestral works [S1].

## Childhood and education

Eisenach; orphaned by 1695; Ohrdruf with his brother; Lüneburg from 1700 [S1].

## Adult working worldview

Lifelong Lutheran church musician [S1]. A note in his Calov Bible says God is always present with his grace in devotional music [S2]. Nothing on nature or God's locus was read.

## Heritage (context only)

Thuringian Lutheran musical family [S1].

## Timing

First lasting contribution 1708 (first published work), at 23 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Unclear [S1].

## Open questions

- Calov annotations in a scholarly edition; a second biography.

## Research log

- 2026-10-15: Read Britannica (Emery); the Bach studies annotation page; search excerpts on the Calov note (not cited).
