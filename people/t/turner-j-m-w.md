---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA2)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Correction found while coding AA4: region_of_birth and region_of_work are Northern Europe, not Western Europe; the United Kingdom is M49 Northern Europe (P3, data/reference/regions.csv)."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "AA3 audit fix: the Tate (Wilton) and National Gallery (Egerton) entries were fetched and read in full on 2026-10-19 and are relabelled 'read in full'."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "AA2 audit fix: the span ends are now dated by exhibition, The Shipwreck at Turner's gallery in 1805 (Tate, S2) and Rain, Steam, and Speed at the RA in 1844 (Egerton, National Gallery, S3), so first-lasting year, span, working_years and age rise from 0.5 to 0.7. Not plotted."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA2, order P32: F 3, rank 186). Source: Britannica, signed by Martin R. F. Butlin (scholars edition, read in full). Lasting claim: 'perhaps the greatest landscapist of the 19th century ... a pioneer in the study of light, color, and atmosphere' (Legacy), a body of work. Span: from The Shipwreck and the Thames sketches of 1805, when he 'was developing his original approach to landscape', to Rain, Steam, and Speed (1844), the last dated work Britannica names among the 'outstanding examples of his late work'; dates as Britannica gives them. No religious statement read: worldview all UNKNOWN; not a scientist. Span 1805–1844, age 30. Not plotted. Draft, not reviewed."}

identity:
  id: turner-j-m-w
  display_name: "J.M.W. Turner"
  roster:
    canonical_name: "J.M.W. Turner"
    rank: 186
    F: 3
    models: [Claude, Gemini, Grok]
    band: "core (3–4)"
    status: "core"
    field: "art"
    field_bucket: "arts"
  full_name: {value: "Joseph Mallord William Turner", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  native_name: {value: "Joseph Mallord William Turner", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  aliases:
    - {name: "J-M-W Turner", kind: "roster alias"}
    - {name: "Turner-J-M-W", kind: "roster alias"}

basics:
  birth:
    date: {value: "1775-04-23", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "London", modern_name: "London, United Kingdom", polity_then: "Kingdom of Great Britain", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  death:
    date: {value: "1851-12-19", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "Chelsea, London", modern_name: "London, United Kingdom", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "Later life and works"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1805, certainty: 0.7, cites: [{source: S1, locator: "Early life and works"}, {source: S2, locator: "Study for 'The Shipwreck'"}], how_known: "'The Shipwreck (1805) suggests that at this time Turner was developing his original approach to landscape' (S1); Tate: 'The painting The Shipwreck was exhibited in Turner's own gallery in 1805' (S2); exhibition is the P30 #1 dating event."}
  era_bucket: {value: "1750 to 1849", certainty: 0.7, cites: [{source: S1, locator: "Early life and works; Later life and works"}], how_known: "1805–1844, one bucket (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "United Kingdom (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "London; tours of Britain and the Continent."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "Middle years"}], how_known: "Titles and appended verse in English."}
  occupations: {value: ["painter", "printmaker"], certainty: 0.7, cites: [{source: S1, locator: "Introduction; Liber Studiorum"}], how_known: "Britannica."}

contribution:
  fields: {value: ["painting"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Landscape painting as the study of light, colour and atmosphere (body of work, 1805–1844)", year: 1805, kind: "body of work", lasting: "'perhaps the greatest landscapist of the 19th century ... a pioneer in the study of light, color, and atmosphere'; 'one of the most innovative and technically gifted painters of his century' (S1, Legacy)", certainty: 0.7, cites: [{source: S1, locator: "Legacy; Early life and works; Later life and works"}], how_known: "Britannica (Butlin); span from The Shipwreck (exhibited 1805, S2) to Rain, Steam, and Speed (exhibited 1844, S3)."}
  evidence_of_impact:
    - {value: "Ruskin's Modern Painters (1843) written to prove his superiority; the Turner Bequest", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Legacy; Later life and works"}], how_known: "Britannica."}
  major_works:
    - {value: "The Fighting Temeraire", year: 1839, kind: "artwork", certainty: 0.7, cites: [{source: S1, locator: "Later life and works"}], how_known: "Britannica: dated (1839)."}
    - {value: "Rain, Steam, and Speed—the Great Western Railway", year: 1844, kind: "artwork", certainty: 0.7, cites: [{source: S1, locator: "Later life and works"}, {source: S3, locator: "Exhibited"}], how_known: "Exhibited RA 1844 (62) (S3); end of the body-of-work span."}
    - {value: "Liber Studiorum", year: 1807, kind: "artwork", certainty: 0.7, cites: [{source: S1, locator: "Early life and works"}], how_known: "Britannica: first part June 1807, abandoned 1819 after 71 plates."}
  honours:
    - {value: "Full member of the Royal Academy", year: 1802, kind: "membership", certainty: 0.7, cites: [{source: S1, locator: "Early life and works"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "Perhaps the greatest landscapist of the 19th century (S1).", certainty: 0.7, cites: [{source: S1, locator: "Legacy"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Son of a barber; mother later committed to a mental hospital", role: "family", certainty: 0.7, cites: [{source: S1, locator: "Early life and works"}], how_known: "Britannica."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Royal Academy schools, from 1789", certainty: 0.7, cites: [{source: S1, locator: "Early life and works"}], how_known: "Britannica."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1805–1844", certainty: 0.7, cites: [{source: S1, locator: "Early life and works; Later life and works"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "No religious statement read. Britannica notes his narrative themes, including 'the power of nature as manifested in the terror of the storm or the beneficence of the sun' (S1), a subject, not a profession."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered: []
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing first-hand read (P19)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); no statement on nature read."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Read his perspective lectures (Royal Academy, from 1811) and Fallacies of Hope verses; Ruskin and Hamilton (1997) on his views; the reported last words 'The sun is God' are a lead of doubtful provenance (not read in a citable source)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated in the source read."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1805–1844", certainty: 0.7, cites: [{source: S1, locator: "Early life and works; Later life and works"}], how_known: "Body of work from The Shipwreck (exhibited 1805, S2) to Rain, Steam, and Speed (exhibited RA 1844, S3) (P29, P31, P30 #1)."}
  age_at_first_lasting_contribution: {value: 30, certainty: 0.7, cites: [{source: S1, locator: "Introduction; Early life and works"}], how_known: "1805 − 1775 = 30 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Colour and atmosphere over drawn structure (S1); he was professor of perspective (1807).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Royal Academy of Arts", role: "member; professor of perspective 1807–1838", years: "1799–1851", kind: "academy or learned society", certainty: 0.5, cites: [{source: S1, locator: "Early life and works; Later life and works"}], how_known: "Britannica; associate 1799, full 1802; end year his death."}
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 186"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "No religious statement read."
  open_questions:
    - "Any religious statement."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Martin R. F. Butlin"
    citation: "Butlin, Martin R. F. 'J.M.W. Turner.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/JMW-Turner/73869"
    url: "https://kids.britannica.com/scholars/article/JMW-Turner/73869"
    accessed: 2026-10-19
    reliability_note: "Signed article, read in full."
    used_for: [identity, basics, contribution, childhood, worldview, lane_b, institutions]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "Tate"
    citation: "'Study for The Shipwreck', c.1799–1805, in J.M.W. Turner: Sketchbooks, Drawings and Watercolours, Tate Research Publication. https://www.tate.org.uk/art/research-publications/jmw-turner/joseph-mallord-william-turner-study-for-the-shipwreck-r1178107"
    url: "https://www.tate.org.uk/art/research-publications/jmw-turner/joseph-mallord-william-turner-study-for-the-shipwreck-r1178107"
    accessed: 2026-10-19
    reliability_note: "Signed museum catalogue entry (Andrew Wilton, May 2013), read in full: 'The painting The Shipwreck was exhibited in Turner's own gallery in 1805'."
    used_for: [basics, timing]
  - id: S3
    type: secondary
    kind: "institutional page"
    author: "Judy Egerton"
    citation: "Egerton, Judy. 'Rain, Steam, and Speed – The Great Western Railway.' The British Paintings (National Gallery, 2000), online catalogue. https://www.nationalgallery.org.uk/paintings/catalogues/egerton-2000/rain-steam-and-speed-the-great-western-railway"
    url: "https://www.nationalgallery.org.uk/paintings/catalogues/egerton-2000/rain-steam-and-speed-the-great-western-railway"
    accessed: 2026-10-19
    reliability_note: "Signed museum catalogue entry, read in full: 'Exhibited RA 1844 (62)'."
    used_for: [contribution, timing]
  - id: S4
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [review]
---

## Summary

J.M.W. Turner (1775–1851), landscape painter [S1]. Draft: all UNKNOWN. Not plotted.

## Life and work

London; travels [S1].

## Contribution and impact

Light, colour and atmosphere, 1805–1844 [S1].

## Childhood and education

Royal Academy schools [S1].

## Adult working worldview

None read.

## Heritage (context only)

Not stated.

## Timing

1805–1844, age 30 [S1, S2, S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Religious statements.

## Research log

- 2026-10-19: AA2 audit fix: the span ends are now dated by exhibition, The Shipwreck at Turner's gallery in 1805 (Tate, S2) and Rain, Steam, and Speed at the RA in 1844 (Egerton, National Gallery, S3), so first-lasting year, span, working_years and age rise from 0.5 to 0.7. Not plotted.
- 2026-10-19: AA3 audit fix: the Tate (Wilton) and National Gallery (Egerton) entries were fetched and read in full on 2026-10-19 and are relabelled 'read in full'.
- 2026-10-19: Correction found while coding AA4: region_of_birth and region_of_work are Northern Europe, not Western Europe; the United Kingdom is M49 Northern Europe (P3, data/reference/regions.csv).
- 2026-10-19: Read Britannica (Butlin).
