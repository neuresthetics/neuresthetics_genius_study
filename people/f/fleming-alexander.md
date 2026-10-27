---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z2; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to medicine. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #139): opened Nobel Lecture 'Penicillin' (11 Dec 1945) in primary PDF — chance observation / bacteriologist account; no God, church, faith, or providence. A stays UNKNOWN (V3: Oklahoma God-wanted-penicillin still Maurois second-hand; Christian Heritage 'I thank God' / Kipling-whisper lines remain unverified second-hand). primary_system stays UNKNOWN (CHRIST lead only). B stays 3 @0.5 (P35/P16: Nobel is discovery narrative, not explicit cause-order talk; alt 4 kept; support single→corroborated via S1+S6). mid UNKNOWN; still not plotted. P47 source_quality; P50 Wikipedia EN dual bio (birth/death agree with Britannica). 1929 paper PDF blocked this pass (still bibliographic). No figures/; no fallacy_catalog."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z3 audit note: S5 now cites the PMC record (PMCID PMC2048009; the 1929 article has no PMID or DOI in PubMed Central; the 2001 WHO Bulletin reprint is PMID 11545337) instead of a search link. Values unchanged."}
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
  full_name: {value: "Sir Alexander Fleming", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "lead"}], how_known: "Britannica; Wikipedia EN agrees."}
  native_name: {value: "Alexander Fleming", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  aliases:
    - {name: "Fleming-Alexander", kind: "roster alias"}

basics:
  birth:
    date: {value: "1881-08-06", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "infobox"}], how_known: "P50: Britannica and Wikipedia EN agree (6 August 1881)."}
    place: {value: "Lochfield Farm, Darvel, Ayrshire, Scotland", modern_name: "Darvel, East Ayrshire, United Kingdom", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "Early life"}], how_known: "Britannica; Wikipedia EN."}
  death:
    date: {value: "1955-03-11", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "infobox"}], how_known: "P50: Britannica and Wikipedia EN agree (11 March 1955)."}
    place: {value: "London", modern_name: "London, United Kingdom", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "Death"}], how_known: "Britannica; Wikipedia EN."}
  first_lasting_contribution_year: {value: 1922, certainty: 0.7, cites: [{source: S4, locator: "Proc. R. Soc. B 93: 306–317 (1922)"}], how_known: "First public statement of lysozyme (discovered November 1921, S1): 'On a remarkable bacteriolytic element found in tissues and secretions', 1922 (P30 #1)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "text"}], how_known: "1921 (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United Kingdom (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "St Mary's Hospital, London."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  occupations: {value: ["bacteriologist", "physician", "professor of bacteriology (University of London, St Mary's)"], certainty: 0.7, cites: [{source: S1, locator: "opening; text"}], how_known: "Britannica."}

contribution:
  primary_domain: medicine
  fields: {value: ["bacteriology", "medicine"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Lysozyme", year: 1922, kind: discovery, lasting: "an antibacterial enzyme in body fluids (S1)", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S4, locator: "Proc. R. Soc. B 93 (1922)"}], how_known: "Discovered November 1921 (S1); first published 1922 (P30 #1)."}
    - {value: "Penicillin", year: 1929, kind: discovery, lasting: "the first antibiotic; Nobel Prize 1945 (S1)", certainty: 0.7, cites: [{source: S1, locator: "text (3 September 1928)"}, {source: S5, locator: "Br. J. Exp. Pathol. 10: 226–236 (1929)"}, {source: S6, locator: "Nobel Lecture 1945"}], how_known: "Observed 3 September 1928 (S1); first published 1929 (P30 #1); Nobel lecture recounts the discovery (S6)."}
  evidence_of_impact:
    - {value: "Nobel Prize for Physiology or Medicine 1945, with Howard Florey and Ernst Chain", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "title / occasion"}], how_known: "Britannica; Nobel lecture."}
  major_works:
    - {value: "Nobel Lecture: Penicillin", year: 1945, kind: other, certainty: 0.7, cites: [{source: S6, locator: "title"}], how_known: "NobelPrize.org PDF."}
  honours:
    - {value: "Knighted", year: 1944, certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "Discoverer of penicillin (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Scottish Presbyterian milieu", certainty: 0.5, cites: [{source: S2, locator: "ch. 1"}, {source: S7, locator: "Personal life"}], how_known: "Maurois describes the austere Presbyterianism of 19th-century Scotland as his background; Wikipedia EN 'Presbyterian background'. Family's own church not stated in what was read, so 0.5."}
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
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nobel lecture (S6) is silent on religion; no own-voice relation statement found."}
  primary_system: {value: UNKNOWN, how_known: "Deepen D1: Nobel lecture has no religion (S6). Still no own-voice adult profession (V3). Leads: CHRIST from Scottish Presbyterian background (S2 ch. 1; S7 Personal life — 'not particularly religious' per Brown). Oklahoma God remark remains Maurois second-hand (S2 ch. 16). Do not force a code."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Lead only: Presbyterian upbringing; Wikipedia/Brown say not particularly religious as adult; no adult profession read."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Deepen D1 keeps UNKNOWN (V3). Nobel lecture contains no God/providence language (S6). Oklahoma story still Maurois 'he is said to have replied' / 'probably true' (S2 ch. 16). Christian Heritage Edinburgh and similar pages quote 'I thank God for sending me penicillin' and the Kipling 'whisper' line without a primary citation — treated as unverified second-hand, not scored."}
    B_cause:
      value: 3
      basis: scholarly_reconstruction
      certainty: 0.5
      support: corroborated
      cites: [{source: S1, locator: "text"}, {source: S6, locator: "Nobel Lecture 1945 (chance observation; bacteriologist pursuit)"}]
      how_known: "Deepen D1: still P35 ceiling 0.5. Scientist (P30: bacteriology, lysozyme, penicillin). Nobel lecture (S6) confirms working-science practice ('penicillin started as a chance observation'; 'pursued the subject as a bacteriologist') but is a discovery narrative, not an explicit account of nature's causal order or miracles (P16/P35: working science alone does not lift B to 0.7). Alt 4 kept. Support corroborated (S1+S6; alt ⊆ main)."
      rationale: "P35. Not raised."
      alternatives:
        - {value: 4, note: "P35 alternative.", cites: [{source: S1, locator: "text"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read (P19)."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "Nothing in his words ranking revelation vs observation."}
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
      note: "Second-hand; 'He is said to have replied'. After the span. Not used for a score (V3)."
    - text: "In my first publication I might have claimed that I had come to the conclusion, as a result of serious study of the literature and deep thought, that valuable antibacterial substances were made by moulds and that I set out to investigate the problem. That would have been untrue and I preferred to tell the truth that penicillin started as a chance observation. My only merit is that I did not neglect the observation and that I pursued the subject as a bacteriologist."
      cites: [{source: S6, locator: "Nobel Lecture, opening pages"}]
      date: "1945-12-11"
      context: "Nobel Lecture 'Penicillin', Stockholm."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Own voice on discovery process; supports working-science B 3 at 0.5 only — does not lift past P35 (no explicit cause-order / miracle talk). No religion language in the lecture."
  changes_over_life: []
  coder_notes: "Do not credit Fleming with Maurois epigraph / Pannett funeral lines (see prior note). Deepen D1: Nobel lecture primary-checked — no God talk. Popular 'I thank God for sending me penicillin' remains untraced to a primary text. Still not plotted (A UNKNOWN)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Scottish (Ayrshire farming family)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Presbyterian milieu", certainty: 0.5, cites: [{source: S2, locator: "ch. 1"}, {source: S7, locator: "Personal life"}], how_known: "Maurois; Wikipedia EN."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1922–1929", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Lysozyme paper (1922) to penicillin paper (1929) (P29, P30 #1)."}
  age_at_first_lasting_contribution: {value: 41, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "1922 − 1881 = 41 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None in his own words on locus/cause of the world."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "He 'never spoke about religion' (S2, ch. 4); Nobel lecture (after the span) is silent on religion (S6)."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Experimental bacteriologist (S1; S6).", certainty: 0.5, cites: [{source: S1, locator: "text"}, {source: S6, locator: "Nobel Lecture"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "No worldview on God/nature identity read in own words.", certainty: 0.5, cites: [{source: S2, locator: "ch. 4"}, {source: S6, locator: "Nobel Lecture (silent on religion)"}], how_known: "Coder's reading."}
  reading: "No data for a circle score."
  notes: "Lane A and Lane B kept separate (P49)."

institutions:
  - {value: "St Mary's Hospital, London (Inoculation Department; Wright-Fleming Institute)", role: "bacteriologist; professor of bacteriology", years: "1906–1955", kind: other, certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Britannica; years the coder's summary."}
collaborators:
  - {value: "Almroth Wright", relation: "mentor or employer", note: "head of the Inoculation Department", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S2, locator: "ch. 4"}], how_known: "Britannica; Maurois."}
  - {value: "Howard Florey", relation: other, note: "shared the 1945 Nobel", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "Nobel Lecture"}], how_known: "Britannica; Nobel lecture."}
  - {value: "Ernst Chain", relation: other, note: "shared the 1945 Nobel", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "Nobel Lecture"}], how_known: "Britannica; Nobel lecture."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 143"}], how_known: "Study roster."}
  controversies:
    - {value: "Popular God-and-penicillin quotations (Oklahoma story; 'I thank God'; Kipling 'whisper' line) are second-hand or misattributed", certainty: 0.7, cites: [{source: S2, locator: "ch. 9 epigraph; ch. 16; Epilogue"}, {source: S6, locator: "Nobel Lecture (no God language)"}], how_known: "Maurois; Nobel primary check."}
  data_quality_flags:
    - "Popular quotations about God are misattributed or second-hand (see coder_notes)."
    - "1929 Br. J. Exp. Pathol. PDF fetch blocked this pass; still bibliographic for publication year."
    - "Rectorial address (Edinburgh 1951) not obtained."
  open_questions:
    - "Any first-person statement on religion in letters (Brown / British Library) or the Edinburgh Rectorial address."
    - "Open 1929 penicillin paper text if a free PDF becomes available."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Kevin Brown"
    citation: "Brown, Kevin. \"Alexander Fleming.\" Encyclopaedia Britannica (updated 11 September 2026). https://www.britannica.com/biography/Alexander-Fleming"
    url: "https://www.britannica.com/biography/Alexander-Fleming"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Signed article by a Fleming historian (also author of Penicillin Man)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "scholarly book"
    author: "André Maurois (trans. Gerard Hopkins)"
    citation: "Maurois, André. The Life of Sir Alexander Fleming, Discoverer of Penicillin. Trans. Gerard Hopkins. London: Jonathan Cape, 1959; Harmondsworth: Penguin, 1963 (the edition scanned on archive.org; page numbers are this edition's)."
    url: "https://archive.org/details/B-001-014-322"
    accessed: 2026-10-19
    source_quality: "scholarly edition or monograph"
    reliability_note: "Authorised biography written with the widow's access to his papers; page numbers from the Penguin scan's running heads. Oklahoma God remark is hedged second-hand."
    used_for: [childhood, worldview, heritage, lane_b, collaborators, review]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [review]
  - id: S4
    type: primary
    kind: "journal article"
    author: "Alexander Fleming"
    citation: "Fleming, Alexander. \"On a remarkable bacteriolytic element found in tissues and secretions.\" Proceedings of the Royal Society of London, Series B 93 (1922): 306–317. doi:10.1098/rspb.1922.0023"
    url: "https://doi.org/10.1098/rspb.1922.0023"
    accessed: 2026-10-19
    source_quality: "primary / own words"
    reliability_note: "Bibliographic details only (year of first publication); full text not re-read this pass."
    used_for: [basics, contribution, timing]
  - id: S5
    type: primary
    kind: "journal article"
    author: "Alexander Fleming"
    citation: "Fleming, Alexander. \"On the antibacterial action of cultures of a Penicillium, with special reference to their use in the isolation of B. influenzae.\" British Journal of Experimental Pathology 10 (1929): 226–236. PMCID: PMC2048009."
    url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC2048009/"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Bibliographic details only (year of first publication); PMC PDF fetch returned a stub this pass."
    used_for: [contribution, timing]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Alexander Fleming"
    citation: "Fleming, Alexander. \"Penicillin.\" Nobel Lecture, 11 December 1945. In Nobel Lectures, Physiology or Medicine 1942–1962. Amsterdam: Elsevier, 1964. PDF: https://www.nobelprize.org/uploads/2018/06/fleming-lecture.pdf"
    url: "https://www.nobelprize.org/uploads/2018/06/fleming-lecture.pdf"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Official NobelPrize.org PDF; read in full (pdftotext). No God/religion language. After the major-work span."
    used_for: [contribution, worldview, timing, lane_b, collaborators, review]
  - id: S7
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Alexander Fleming.\" English Wikipedia (accessed 2026-10-24). https://en.wikipedia.org/wiki/Alexander_Fleming"
    url: "https://en.wikipedia.org/wiki/Alexander_Fleming"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "P50 dual bio (birth/death agree with S1); Personal life notes Presbyterian background and 'not particularly religious' (citing Brown)."
    used_for: [identity, basics, childhood, worldview, heritage, review]
---

# Alexander Fleming

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Sir Alexander Fleming (1881–1955), Scottish bacteriologist, discoverer of lysozyme and penicillin [S1]. Deepen D1: primary_system UNKNOWN (CHRIST lead); A UNKNOWN; B 3 (0.5, alt 4, corroborated); mid_basin UNKNOWN. Still not plotted (figures/ not touched).

## Life and work

Ayrshire, Kilmarnock, St Mary's [S1].

## Contribution and impact

Lysozyme (published 1922), penicillin (published 1929), Nobel 1945 [S1; S4; S5; S6].

## Childhood and education

Farm family; Presbyterian milieu [S1; S2, ch. 1; S7].

## Adult working worldview

He 'never spoke about religion' [S2, ch. 4]. Nobel lecture is silent on religion; discovery described as a chance observation pursued as a bacteriologist [S6].

## Heritage (context only)

Scottish [S1].

## Timing

1922–1929, from age 41 [S4; S5].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data for a circle score.

## Open questions

- Letters or Edinburgh Rectorial address with first-person religion.
- 1929 paper full text if a free PDF becomes available.

## Research log

- 2026-10-19: Read Britannica (Brown) and searched Maurois's Life.
- 2026-10-24: Deepen D1 — Nobel Lecture PDF (NobelPrize.org) in full; Wikipedia EN dual bio; 1929 PMC PDF blocked; Christian Heritage / 'I thank God' quotes left unscored (V3).
