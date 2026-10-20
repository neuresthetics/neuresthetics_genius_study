---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z2)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z2 audit fixes (blind audit /workspace/genius_study_audit/gs_f70a593_Z2/run1/): Z2-42 (FAIL): primary_system and A_locus BELOW_THRESHOLD -> UNKNOWN (V3, as Kurosawa), keeping CHRIST and the Oklahoma story as leads; mid_basin -> UNKNOWN. Z2-44: span re-dated by first publications (P30 #1): 1922 (lysozyme, Proc. R. Soc. B) to 1929 (penicillin, Br. J. Exp. Pathol.), age 41; S4 and S5 added. Maurois citation gives the 1963 Penguin edition scanned. Still not plotted."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z2, order P32: F 3, rank 143). Basics from Britannica (Kevin Brown, signed). Religion from Maurois's Life (trans. Hopkins, 1959; Penguin scan on archive.org): 'the young Scot, who never spoke about religion' (ch. 4); the remark 'I can only suppose that God wanted penicillin, and that that was His reason for creating Alexander Fleming' is a story 'current in Oklahoma' that 'he is said to have' made, and Maurois only infers it is 'probably true' (ch. 16): reported speech at second hand, below threshold. The ch. 9 epigraph 'God took care to hide that country ...' is Maurois's epigraph (coder's identification: Kipling's 'The Explorer'), not Fleming's words; the 'finger of God' line is from Pannett's funeral oration (Epilogue). A scientist (P30). Span 1921–1928. primary_system BELOW_THRESHOLD (lead: Presbyterian upbringing); A BELOW_THRESHOLD; B 3 (0.5, alt 4); C UNKNOWN; D BELOW_THRESHOLD; E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not plotted (no A). Draft, not reviewed."}

identity:
  id: fleming-alexander
  display_name: "Alexander Fleming"
  roster:
    canonical_name: "Alexander Fleming"
    rank: 143
    F: 3
    models: [Claude, DeepSeek, Gemini]
    band: "core (3–4)"
    status: core
    field: medicine
    field_bucket: medicine
  full_name: {value: "Sir Alexander Fleming", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  native_name: {value: "Alexander Fleming", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  aliases:
    - {name: "Fleming-Alexander", kind: "roster alias"}

basics:
  birth:
    date: {value: "1881-08-06", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Lochfield Farm, Darvel, Ayrshire, Scotland", modern_name: "Darvel, East Ayrshire, United Kingdom", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1955-03-11", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "London", modern_name: "London, United Kingdom", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1922, certainty: 0.7, cites: [{source: S4, locator: "Proc. R. Soc. B 93: 306–317 (1922)"}], how_known: "First public statement of lysozyme (discovered November 1921, S1): 'On a remarkable bacteriolytic element found in tissues and secretions', 1922 (P30 #1)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "text"}], how_known: "1921 (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United Kingdom (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "St Mary's Hospital, London."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  occupations: {value: ["bacteriologist", "physician", "professor of bacteriology (University of London, St Mary's)"], certainty: 0.7, cites: [{source: S1, locator: "opening; text"}], how_known: "Britannica."}

contribution:
  fields: {value: ["bacteriology", "medicine"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Lysozyme", year: 1922, kind: discovery, lasting: "an antibacterial enzyme in body fluids (S1)", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S4, locator: "Proc. R. Soc. B 93 (1922)"}], how_known: "Discovered November 1921 (S1); first published 1922 (P30 #1)."}
    - {value: "Penicillin", year: 1929, kind: discovery, lasting: "the first antibiotic; Nobel Prize 1945 (S1)", certainty: 0.7, cites: [{source: S1, locator: "text (3 September 1928)"}, {source: S5, locator: "Br. J. Exp. Pathol. 10: 226–236 (1929)"}], how_known: "Observed 3 September 1928 (S1); first published 1929 (P30 #1)."}
  evidence_of_impact:
    - {value: "Nobel Prize for Physiology or Medicine 1945, with Howard Florey and Ernst Chain", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours:
    - {value: "Knighted", year: 1944, certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "Discoverer of penicillin (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Scottish Presbyterian milieu", certainty: 0.5, cites: [{source: S2, locator: "ch. 1"}], how_known: "Maurois describes the austere Presbyterianism of 19th-century Scotland as his background; his family's own church is not stated in what was read, so 0.5."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated for the family."}
  parents_and_household: []
  household_circumstances: {value: "Farm family at Lochfield, Ayrshire", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  schooling:
    - {value: "Kilmarnock Academy", stage: "grammar or secondary school", run_by: other, years: "1894–", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica; run_by not stated."}
    - {value: "Regent Street Polytechnic, London", stage: "grammar or secondary school", run_by: other, years: UNKNOWN, certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Britannica; stage the coder's reading."}
    - {value: "St Mary's Hospital Medical School, London", stage: university, run_by: other, years: "1901–1908", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica; gold medal 1908."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["English"], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Inferred."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1922–1929", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing in his own words read."}
  primary_system: {value: UNKNOWN, how_known: "No own words read (V3; Z2-42, as Kurosawa Z1-41). Leads: He 'never spoke about religion' (S2, ch. 4); the only remark on God is second-hand and hedged by Maurois (S2, ch. 16). CHRIST from the Scottish Presbyterian background (S2, ch. 1)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Lead only: upbringing; no adult profession read."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "No own words read (V3; Z2-42). Lead only, a second-hand anecdote: 'There is a story current in Oklahoma ... He is said to have replied: \"I can only suppose that God wanted penicillin, and that that was His reason for creating Alexander Fleming.\"' Maurois judges it 'probably true' because Fleming did not put it in his 'Fleming Myth' dossier (S2, ch. 16, pp. 258–259). Reported speech at second hand and possibly a joke (§7, P8)."}
    B_cause:
      value: 3
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S1, locator: "text"}]
      how_known: "A scientist with working science only (P30: bacteriology, lysozyme, penicillin), so B 3 at 0.5, alternative 4 (P35)."
      rationale: "P35."
      alternatives:
        - {value: 4, note: "P35 alternative.", cites: [{source: S1, locator: "text"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read (P19)."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "Nothing in his words."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Not scored from science alone (P19)."}
  mid_basin: {value: UNKNOWN, how_known: "A UNKNOWN."}
  statements:
    - text: "I can only suppose that God wanted penicillin, and that that was His reason for creating Alexander Fleming."
      cites: [{source: S2, locator: "ch. 16, pp. 258–259"}]
      date: "1945"
      context: "A story 'current in Oklahoma': an old lady who had given to the Foundation asked what he attributed his success to. Year the coder's estimate (his post-Nobel American tour)."
      axes: [A_locus]
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-19
      note: "Second-hand; 'He is said to have replied'. After the span. Not used for a score."
  changes_over_life: []
  coder_notes: "Do not credit Fleming with two lines often quoted from Maurois: 'God took care to hide that country till He judged His people ready' is the epigraph of ch. 9 (Kipling's 'The Explorer', coder's identification), and 'We can almost see the finger of God' is from Professor Pannett's funeral oration (Epilogue, p. 306). The span is dated by the first publications (1922, 1929), P30 #1; the bibliographic details are confirmed by citations in the history-of-medicine literature (Garrison-Morton; Mayo Clin Proc), not read in facsimile."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Scottish (Ayrshire farming family)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Presbyterian milieu", certainty: 0.5, cites: [{source: S2, locator: "ch. 1"}], how_known: "Maurois, general."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1922–1929", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Lysozyme paper (1922) to penicillin paper (1929) (P29, P30 #1)."}
  age_at_first_lasting_contribution: {value: 41, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "1922 − 1881 = 41 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None in his own words."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "He 'never spoke about religion' (S2, ch. 4)."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Experimental bacteriologist (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "No views read.", certainty: 0.5, cites: [{source: S2, locator: "ch. 4"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "St Mary's Hospital, London (Inoculation Department; Wright-Fleming Institute)", role: "bacteriologist; professor of bacteriology", years: "1906–1955", kind: other, certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Britannica; years the coder's summary."}
collaborators:
  - {value: "Almroth Wright", relation: "mentor or employer", note: "head of the Inoculation Department", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S2, locator: "ch. 4"}], how_known: "Britannica; Maurois."}
  - {value: "Howard Florey", relation: other, note: "shared the 1945 Nobel", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  - {value: "Ernst Chain", relation: other, note: "shared the 1945 Nobel", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 143"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Popular quotations about God are misattributed (see coder_notes)."
  open_questions:
    - "Any first-person statement on religion (letters, Rectorial address at Edinburgh)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Kevin Brown"
    citation: "Brown, Kevin. \"Alexander Fleming.\" Encyclopaedia Britannica (updated 11 September 2026). https://www.britannica.com/biography/Alexander-Fleming"
    url: "https://www.britannica.com/biography/Alexander-Fleming"
    accessed: 2026-10-19
    reliability_note: "Signed article by a Fleming historian."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "scholarly book"
    author: "André Maurois (trans. Gerard Hopkins)"
    citation: "Maurois, André. The Life of Sir Alexander Fleming, Discoverer of Penicillin. Trans. Gerard Hopkins. London: Jonathan Cape, 1959; Harmondsworth: Penguin, 1963 (the edition scanned on archive.org; page numbers are this edition's)."
    url: "https://archive.org/details/B-001-014-322"
    accessed: 2026-10-19
    reliability_note: "Authorised biography written with the widow's access to his papers; page numbers from the Penguin scan's running heads."
    used_for: [childhood, worldview, heritage, lane_b, collaborators]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [review]
  - id: S4
    type: primary
    kind: "journal article"
    author: "Alexander Fleming"
    citation: "Fleming, Alexander. \"On a remarkable bacteriolytic element found in tissues and secretions.\" Proceedings of the Royal Society of London, Series B 93 (1922): 306–317. doi:10.1098/rspb.1922.0023"
    url: "https://doi.org/10.1098/rspb.1922.0023"
    accessed: 2026-10-19
    reliability_note: "Bibliographic details only (year of first publication); not read."
    used_for: [basics, contribution, timing]
  - id: S5
    type: primary
    kind: "journal article"
    author: "Alexander Fleming"
    citation: "Fleming, Alexander. \"On the antibacterial action of cultures of a Penicillium, with special reference to their use in the isolation of B. influenzae.\" British Journal of Experimental Pathology 10 (1929): 226–236."
    url: "https://pubmed.ncbi.nlm.nih.gov/?term=Fleming+1929+antibacterial+action+penicillium"
    accessed: 2026-10-19
    reliability_note: "Bibliographic details only (year of first publication); not read."
    used_for: [contribution, timing]
---

# Alexander Fleming

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Sir Alexander Fleming (1881–1955), Scottish bacteriologist, discoverer of lysozyme and penicillin [S1]. Draft: primary_system UNKNOWN (lead CHRIST); A UNKNOWN; B 3 (0.5, alt 4); mid_basin UNKNOWN. Not plotted.

## Life and work

Ayrshire, Kilmarnock, St Mary's [S1].

## Contribution and impact

Lysozyme (published 1922), penicillin (published 1929), Nobel 1945 [S1; S4; S5].

## Childhood and education

Farm family; Presbyterian milieu [S1; S2, ch. 1].

## Adult working worldview

He 'never spoke about religion' [S2, ch. 4].

## Heritage (context only)

Scottish [S1].

## Timing

1922–1929, from age 41 [S4; S5].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- A first-person statement on religion.

## Research log

- 2026-10-19: Read Britannica (Brown) and searched Maurois's Life.
