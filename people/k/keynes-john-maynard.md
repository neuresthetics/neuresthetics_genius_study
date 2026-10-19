---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch T)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch T, order P32: F 4, rank 111). Basics from Britannica (Britannica Editors, unsigned; body only). Worldview from 'My Early Beliefs' (read to the Memoir Club 9 September 1938; published 1949; Collected Writings vol. 10, pp. 433–450), read in an excerpt web copy with CW page numbers. Not a scientist (P30). primary_system BELOW_THRESHOLD; A BELOW_THRESHOLD; B UNKNOWN (P16, P19); C, E UNKNOWN; D BELOW_THRESHOLD; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: keynes-john-maynard
  display_name: "John Maynard Keynes"
  roster:
    canonical_name: "John Maynard Keynes"
    rank: 111
    F: 4
    models: [Claude, DeepSeek, Gemini, GPT]
    band: "core (3–4)"
    status: core
    field: economics
    field_bucket: "social science"
  full_name: {value: "John Maynard Keynes", certainty: 0.7, cites: [{source: S1, locator: "title; opening"}], how_known: "Britannica."}
  native_name: {value: "John Maynard Keynes", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "English; same as the display name."}
  aliases:
    - {name: "John-Maynard-Keynes", kind: "roster alias"}
    - {name: "Keynes-John Maynard", kind: "roster alias"}

basics:
  birth:
    date: {value: "1883-06-05", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "facts box (Born)"}], how_known: "Britannica."}
    place: {value: "Cambridge, Cambridgeshire, England", modern_name: "Cambridge, United Kingdom", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "facts box (Born)"}], how_known: "Britannica."}
  death:
    date: {value: "1946-04-21", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "facts box (Died)"}], how_known: "Britannica."}
    place: {value: "Firle, Sussex", modern_name: "Firle, East Sussex, United Kingdom", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "facts box (Died)"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1919, certainty: 0.5, cites: [{source: S1, locator: "Background and early career"}], how_known: "The Economic Consequences of the Peace (1919), whose 'permanent importance' Britannica names. Alternative 1913: Indian Currency and Finance, 'his first major work ... a definitive examination' (S1), not called lasting; coder's call, so 0.5."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "Background and early career"}], how_known: "1919 (P2); 1913 gives the same bucket."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "facts box"}], how_known: "United Kingdom (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "Key contributions"}], how_known: "Cambridge and London."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "works named"}], how_known: "Britannica."}
  occupations: {value: ["economist", "journalist", "financier", "civil servant (India Office, Treasury)", "fellow of King's College, Cambridge"], certainty: 0.7, cites: [{source: S1, locator: "opening; Background and early career; Later works"}], how_known: "Britannica."}

contribution:
  fields: {value: ["economics"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "The Economic Consequences of the Peace: analysis of the Versailles reparations", year: 1919, kind: work, lasting: "'The permanent importance of this polemical essay lies in its economic analysis of the stringent reparations' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Background and early career"}], how_known: "Britannica."}
    - {value: "The General Theory of Employment, Interest and Money: theory of prolonged unemployment and government-sponsored full employment (Keynesian economics)", year: 1936, kind: theory, lasting: "'one of the most influential economics books in history' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; Key contributions"}], how_known: "Britannica dates it 1935–36; 1936 is the publication year. The latest listed lasting contribution (P30 addendum b): 'The General Theory was Keynes's last major written work' (S1). A theory of society, not of physical or natural systems, so not a scientist (P30)."}
  evidence_of_impact:
    - {value: "The Keynesian model 'was a core part of economics textbooks from the late 1940s until the late 1980s'", kind: "standard textbook canon", certainty: 0.7, cites: [{source: S1, locator: "Later works and assessment"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father: John Neville Keynes, economist and academic administrator at Cambridge", certainty: 0.7, cites: [{source: S1, locator: "Background and early career"}], how_known: "Britannica."}
    - {value: "Mother: one of the first female graduates of Cambridge", certainty: 0.7, cites: [{source: S1, locator: "Background and early career"}], how_known: "Britannica (unnamed)."}
  household_circumstances: {value: "Moderately prosperous academic family", certainty: 0.7, cites: [{source: S1, locator: "Background and early career"}], how_known: "Britannica."}
  schooling:
    - {value: "King's College, Cambridge, from 1902: B.A. 1905, M.A. 1909", stage: university, run_by: other, years: "1902–1909", certainty: 0.7, cites: [{source: S1, locator: "Background and early career"}], how_known: "Britannica body; Eton (1897–1902) is only in the Top Questions box, not cited."}
  early_mathematics: {value: "advanced mathematics", certainty: 0.5, cites: [{source: S1, locator: "Background and early career"}], how_known: "Marshall moved his interests 'from mathematics and the classics' to economics (S1)."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading:
    - {value: "G. E. Moore, Principia Ethica (1903)", certainty: 0.7, cites: [{source: S2, locator: "p. 435"}], how_known: "His memoir."}
  childhood_mentors: []
  languages_in_childhood: {value: ["English"], certainty: 0.5, cites: [{source: S1, locator: "facts box"}], how_known: "Coder's reading."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1919–1936", certainty: 0.5, cites: [{source: S1, locator: "Background and early career; Key contributions"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Moore's ethics as a 'religion' ('one’s attitude towards oneself and the ultimate'), regarded at the time 'as entirely rational and scientific in character'; 'It is still my religion under the surface' (1938)", certainty: 0.5, cites: [{source: S2, locator: "pp. 435, 437, 441–442"}], how_known: "Memoir read to a private club in 1938, after the working years (P1 cap 0.5); an excerpt web copy."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "No statement on God's existence or nature was found in the source read. His 'religion' is Moore's ethics of good states of mind, not a theistic or naturalistic system; the Christians were 'the enemy' as 'representatives of tradition, convention and hocus-pocus' (S2, p. 445). Candidates ATHE, AGNOS and SECHUM all need a statement of his own on God or the humanist movement. Secondary reports of disbelief seen in search results are leads, not evidence of a positive code."}
  secondary_system: {value: UNKNOWN, how_known: "One system (P29)."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Rejected: no denial of God read in his words."}
    - {code: AGNOS, reason: "Rejected: no stated suspension read (secondary reports only)."}
    - {code: SECHUM, reason: "Rejected: an ethic of private goods, and his public identity was not the humanist movement."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "No locus view read; 'Our Ideal was a merciful God' (S2, p. 441) describes Moore's ethical Ideal, a figure of speech. Secondary reports of disbelief (search results only) are leads."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); the source read says nothing on nature (P16, P19)."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing on reward and punishment of persons; Moore's 'vindictive punishment' (S2, p. 441) is Moore's view, not his."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "Lead only: 'We used to regard the Christians as the enemy, because they appeared as the representatives of tradition, convention and hocus-pocus' (S2, p. 445) describes the group's early view and is retracted in the same sentence ('In truth it was the Benthamite calculus ...'); it is not a statement on revelation against observation. After the working years in any case (P1)."}
    E_scope: {value: UNKNOWN, how_known: "Nothing on the world's order (P19)."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN, which takes precedence (P19)."}
  statements:
    - text: "It seems to me looking back, that this religion of ours was a very good one to grow up under. It remains nearer the truth than any other that I know, with less irrelevant extraneous matter and nothing to be ashamed of"
      cites: [{source: S2, locator: "pp. 441–442"}]
      date: "1938-09-09"
      context: "'My Early Beliefs', a paper read to the Memoir Club at Tilton, defending the Cambridge circle of 1902–14 against D. H. Lawrence; the 'religion' is Moore's ethics. The passage ends 'It is still my religion under the surface.'"
      axes: []
      kind: "unpublished manuscript"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "Collected Writings vol. 10 text, read in an excerpt web copy (cuts marked '…' in the copy)."
    - text: "We used to regard the Christians as the enemy, because they appeared as the representatives of tradition, convention and hocus-pocus. In truth it was the Benthamite calculus, based on an over-valuation of the economic criterion, which was destroying the quality of the popular Ideal."
      cites: [{source: S2, locator: "p. 445"}]
      date: "1938-09-09"
      context: "Same paper."
      axes: [D_authority]
      kind: "unpublished manuscript"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "As above."
  changes_over_life: []
  coder_notes: "Coder's call. The memoir is after the working years (1938; P1 cap) and states no view of God. Leads: Skidelsky and Moggridge on his religion (secondary); secondary reports that he never believed in a deity (search results only, not read). Not plotted."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1919–1936", certainty: 0.5, cites: [{source: S1, locator: "Background and early career; Key contributions"}], how_known: "The Economic Consequences of the Peace (1919) to The General Theory (1936), first to last listed lasting contribution (P29, P30). 0.5: the start is a coder's call (alternative 1913, Indian Currency and Finance)."}
  age_at_first_lasting_contribution: {value: 36, certainty: 0.5, cites: [{source: S1, locator: "facts box; Background and early career"}], how_known: "1919 − 1883 = 36 (P30); 30 with the 1913 alternative."}
  first_evidence_of_lio_type_views: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "pp. 433–450"}], how_known: "None in the source read."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "pp. 433–450"}], how_known: "None in the source read."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "Background and early career"}], how_known: "Mathematics degree; not assessed."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "Background and early career"}], how_known: "Not read."}
  circle_present: {value: "no", rationale: "No God-Nature identity read.", certainty: 0.5, cites: [{source: S2, locator: "pp. 433–450"}], how_known: "Coder's reading."}
  reading: "A Moorean ethic of good states of mind called a 'religion', with no stated theology."
  notes: ""

institutions:
  - {value: "King's College, Cambridge", role: fellow, years: "1909–1946", kind: university, certainty: 0.7, cites: [{source: S1, locator: "Key contributions"}], how_known: "Britannica (fellow; election year from the Top Questions box is not cited, so years are the coder's)."}
  - {value: "HM Treasury", role: "adviser (World War I and II)", years: "1915–1919; 1940–1946", kind: "government or state body", certainty: 0.5, cites: [{source: S1, locator: "Background and early career; Later works"}], how_known: "Britannica; years partly the coder's."}
collaborators:
  - {value: "Alfred Marshall", relation: teacher, note: "turned his interests to economics", certainty: 0.7, cites: [{source: S1, locator: "Background and early career"}], how_known: "Britannica."}
  - {value: "G. E. Moore", relation: "influenced by", note: "Principia Ethica as 'our religion'", certainty: 0.7, cites: [{source: S2, locator: "pp. 435–442"}], how_known: "His memoir."}
  - {value: "Lytton Strachey", relation: "other", note: "introduced him to 'the Society' (the Apostles)", certainty: 0.7, cites: [{source: S1, locator: "Background and early career"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 111"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Britannica article unsigned (Britannica Editors)."
    - "Worldview source is a 1938 memoir read in an excerpt web copy; after the working years."
  open_questions:
    - "Read his letters (to Strachey, Grant) and Skidelsky for statements on God."
    - "Childhood religion."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"John Maynard Keynes.\" Encyclopaedia Britannica (updated 29 September 2026). https://www.britannica.com/money/John-Maynard-Keynes. Read live 2026-10-19."
    url: "https://www.britannica.com/money/John-Maynard-Keynes"
    accessed: 2026-10-19
    reliability_note: "Unsigned article. Body and facts box only; the AI-generated question boxes are not cited."
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "John Maynard Keynes"
    citation: "Keynes, John Maynard. 'My Early Beliefs' (read to the Memoir Club, Tilton, 9 September 1938; first published in Two Memoirs, 1949). The Collected Writings of John Maynard Keynes, vol. 10, pp. 433–450. Excerpt read at https://neilhacker.com/wp-content/uploads/2021/01/my-early-beliefs.pdf"
    url: "https://neilhacker.com/wp-content/uploads/2021/01/my-early-beliefs.pdf"
    accessed: 2026-10-19
    reliability_note: "Unofficial web copy of an anthology excerpt (with an editor's headnote and cuts marked '…'), keeping the CW page numbers in brackets; not checked against the printed volume (0.7 cap), and after the working years (0.5)."
    used_for: [worldview, childhood, timing, lane_b, collaborators]
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

# John Maynard Keynes

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

John Maynard Keynes (1883–1946), English economist [S1]. Draft: primary_system BELOW_THRESHOLD; A BELOW_THRESHOLD; B UNKNOWN; D BELOW_THRESHOLD; C, E UNKNOWN; mid_basin UNKNOWN. Not plotted.

## Life and work

Cambridge, the India Office, the Treasury [S1].

## Contribution and impact

The Economic Consequences of the Peace (1919) to The General Theory (1936) [S1].

## Childhood and education

King's College, Cambridge [S1].

## Adult working worldview

Moore's ethics as 'still my religion under the surface' [S2, p. 442].

## Heritage (context only)

English [S1].

## Timing

1919–1936, from age 36 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No theology stated [S2].

## Open questions

- Letters and biographies for statements on God.

## Research log

- 2026-10-19: Read Britannica (live) and the excerpt of 'My Early Beliefs' (CW 10).
