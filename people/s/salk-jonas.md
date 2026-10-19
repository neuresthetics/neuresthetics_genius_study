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
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch T, order P32: F 4, rank 112). Basics from Britannica (Britannica Editors; revised by Kara Rogers), the Science History Institute and the Salk Institute. Worldview from The John Callaway Interviews (WTTW; broadcast 30 June 1981), AAPB transcript (status 'Correct'). Scientist (P30). All worldview fields rest on one recorded interview after the working years (P1 cap 0.5). primary_system PANT (0.5, alt ATHE); A 4 (0.5, alt BELOW_THRESHOLD); B 3 (0.5, alt 4); C UNKNOWN; D BELOW_THRESHOLD; E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD (A 4 at 0.5). Plotted (faded). Draft, not reviewed."}

identity:
  id: salk-jonas
  display_name: "Jonas Salk"
  roster:
    canonical_name: "Jonas Salk"
    rank: 112
    F: 4
    models: [Claude, DeepSeek, Gemini, Grok]
    band: "core (3–4)"
    status: core
    field: medicine
    field_bucket: medicine
  full_name: {value: "Jonas Edward Salk", certainty: 1.0, cites: [{source: S1, locator: "facts box (In full)"}, {source: S3, locator: "opening"}], how_known: "Britannica and the Salk Institute."}
  native_name: {value: "Jonas Edward Salk", certainty: 0.7, cites: [{source: S1, locator: "facts box"}], how_known: "English; same as the full name."}
  aliases:
    - {name: "Jonas-Salk", kind: "roster alias"}
    - {name: "Salk-Jonas", kind: "roster alias"}

basics:
  birth:
    date: {value: "1914-10-28", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "facts box (Born)"}, {source: S3, locator: "opening"}], how_known: "Britannica and the Salk Institute agree."}
    place: {value: "New York, New York", modern_name: "New York City, United States", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "facts box (Born)"}, {source: S3, locator: "opening"}], how_known: "Britannica and the Salk Institute."}
  death:
    date: {value: "1995-06-23", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "facts box (Died)"}, {source: S3, locator: "closing paragraph"}], how_known: "Britannica and the Salk Institute."}
    place: {value: "La Jolla, California", modern_name: "La Jolla, San Diego, California, United States", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "facts box (Died)"}, {source: S3, locator: "closing paragraph"}], how_known: "Britannica and the Salk Institute."}
  first_lasting_contribution_year: {value: 1952, certainty: 0.7, cites: [{source: S2, locator: "The 'Killed-Virus' Principle"}], how_known: "The killed-virus polio vaccine, first tested in humans in 1952 (S2); proven in the 1954 field trial and announced 12 April 1955 (S2, S3). A range date sets the span start (P12)."}
  era_bucket: {value: "1950 on", certainty: 0.7, cites: [{source: S2, locator: "The 'Killed-Virus' Principle"}], how_known: "1952 (P2)."}
  region_of_birth: {value: "North America", certainty: 1.0, cites: [{source: S1, locator: "facts box"}, {source: S3, locator: "opening"}], how_known: "United States (P3)."}
  region_of_work: {value: "North America", certainty: 1.0, cites: [{source: S1, locator: "body"}, {source: S2, locator: "The Virus Research Laboratory and Poliovirus"}], how_known: "Pittsburgh."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S3, locator: "opening"}], how_known: "'the eldest of three sons'."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Coder's reading."}
  occupations: {value: ["physician", "virologist and medical researcher", "professor of bacteriology, preventive and experimental medicine (Pittsburgh)", "founding director of the Salk Institute"], certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Britannica."}

contribution:
  fields: {value: ["virology", "immunology", "medicine"], certainty: 0.7, cites: [{source: S1, locator: "body"}, {source: S2, locator: "Salk's Education and Work on Influenza"}], how_known: "Britannica and the Science History Institute."}
  lasting_original_contributions:
    - {value: "First safe and effective (inactivated, killed-virus) polio vaccine: killed virus of each of the three types induces antibodies; human testing 1952; national field trial 1954; declared safe and effective 12 April 1955", year: 1952, kind: invention, lasting: "'developed the first safe and effective vaccine for polio' (S1); recommended again for US use in 1999 and 2009 'because it cannot accidentally cause polio' (S2)", certainty: 1.0, cites: [{source: S1, locator: "body"}, {source: S2, locator: "The 'Killed-Virus' Principle; Field Trials; Live-Virus versus Killed-Virus Controversy"}], how_known: "Britannica and the Science History Institute. Range 1952–1955: work and its proof (P12, P29). A theory about natural systems tested by experiment (antibody induction in monkeys and children), so he is a scientist (P30)."}
  evidence_of_impact:
    - {value: "US polio cases fell from an average of more than 45,000 a year before the vaccine to 910 by 1962", kind: other, certainty: 0.7, cites: [{source: S3, locator: "1954–1955 paragraph"}], how_known: "Salk Institute page."}
    - {value: "Presidential Medal of Freedom, 1977", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "last paragraph"}], how_known: "Britannica."}
  major_works: []
  honours:
    - {value: "Presidential Medal of Freedom", year: 1977, certainty: 0.7, cites: [{source: S1, locator: "last paragraph"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "(S1, S2).", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Britannica."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father: Daniel Salk, son of Jewish immigrants (S2); 'Russian-Jewish immigrant' per S3", certainty: 0.5, cites: [{source: S2, locator: "Salk's Education"}, {source: S3, locator: "opening"}], how_known: "The two pages differ on the father; 0.5."}
    - {value: "Mother: Dora Salk, Russian-Jewish immigrant", certainty: 1.0, cites: [{source: S2, locator: "Salk's Education"}, {source: S3, locator: "opening"}], how_known: "Both pages."}
  household_circumstances: {value: "Immigrant family; eldest of three sons; first in the family to attend college", certainty: 0.7, cites: [{source: S3, locator: "opening"}], how_known: "Salk Institute."}
  schooling:
    - {value: "City College of New York, degree in science 1933 (entered after high school at 15)", stage: university, run_by: "state or municipal", years: "c. 1929–1933", certainty: 0.7, cites: [{source: S2, locator: "Salk's Education"}], how_known: "Science History Institute; start year is the coder's."}
    - {value: "New York University School of Medicine, M.D. 1939", stage: university, run_by: other, years: "1933–1939", certainty: 1.0, cites: [{source: S1, locator: "body"}, {source: S2, locator: "Salk's Education"}], how_known: "Britannica and SHI; start year the coder's from 'At 19' (S2)."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["English"], certainty: 0.5, cites: [{source: S3, locator: "opening"}], how_known: "Coder's reading (New York birth)."}
  notable_events:
    - {value: "Prayed to God as a child, then 'soon realized that I had to do something about it myself'; his mother's saying 'God helps those who help themselves'", certainty: 0.5, cites: [{source: S4, locator: "transcript, religion exchange"}], how_known: "(interview) His recollection in 1981."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1952–1955", certainty: 0.7, cites: [{source: S2, locator: "The 'Killed-Virus' Principle; Field Trials"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Religion 'serves a very important purpose'; 'my use of the term order is the same as the word God'; scientists 'perform the kinds of miracles' people pray for (1981)", certainty: 0.5, cites: [{source: S4, locator: "transcript, religion exchange; closing segment"}], how_known: "(interview) One recorded interview, 26 years after the working years (P1 cap 0.5)."}
  primary_system:
    value: PANT
    basis: recorded_interview
    certainty: 0.5
    cites: [{source: S4, locator: "transcript, religion exchange; closing segment"}]
    rationale: "(interview) Two-part test (PANT use_when). Part 1: 'some might say that my use of the term order is the same as the word God. We're both describing the same phenomenon', against 'an anthropomorphic God ... a personal God that looks after me personally'; and 'I'm very much aware of the miracle of life ... And for me, that's where God is. That's where creation exists now.' Part 2 (a mark beyond feeling, unity as one order): 'it is the existence of order that is fundamental to our existence, that we are manifestations of the existence of order.' Named alternative ATHE: 'God was invented because of the necessity for having a form of order' reads the God-term as a human construct for order, i.e. naturalism that drops the entity-term (PANT do_not_use_when)."
    how_known: "(interview) Spoken, not written (the use_when names the person's writing); one interview after the working years, so 0.5 (P1, P20)."
    alternatives:
      - {value: ATHE, note: "'God was invented'; order is the reality, God a name for it.", cites: [{source: S4, locator: "transcript, religion exchange"}]}
  secondary_system: {value: UNKNOWN, how_known: "One system (P29)."}
  candidate_codes_considered:
    - {code: PANT, reason: "God and order 'the same phenomenon'; God 'where' life and creation are; chosen at 0.5."}
    - {code: ATHE, reason: "'God was invented'; named alternative."}
    - {code: SECHUM, reason: "Rejected: his public identity was not the humanist movement."}
    - {code: JUDA, reason: "Heritage only (S2, S3); never a code."}
  lio_axes:
    A_locus:
      value: 4
      basis: recorded_interview
      certainty: 0.5
      cites: [{source: S4, locator: "transcript, religion exchange; closing segment"}]
      rationale: "(interview) Immanent pole: God is the order of which 'we are manifestations', and 'that's where God is' — in life and man; he sets this against a God 'in the form of a person'. Named alternative BELOW_THRESHOLD: 'God was invented' may make the God-talk a figure of speech."
      how_known: "(interview) One recorded interview, his own words (P8), after the working years, so 0.5."
      alternatives:
        - {value: BELOW_THRESHOLD, note: "God-talk as figure of speech.", cites: [{source: S4, locator: "transcript, religion exchange"}]}
    B_cause:
      value: 3
      basis: recorded_interview
      certainty: 0.5
      cites: [{source: S4, locator: "transcript, religion exchange"}]
      rationale: "(interview) A remark on lawful order with no stated no-exception claim: 'it is the existence of order that is fundamental to our existence'; he answers 'Yes' to the interviewer's 'we get up tomorrow, this table will still be here ... The sun will come up' (the interviewer's words, not his). B 3 at 0.5, alternative 4 (P16 addendum, P35). His 'miracles' performed by scientists and 'the miracle of life' are figures of speech for human achievement and wonder, not exceptions to order."
      how_known: "(interview) One remark plus working science (P35); after the working years."
      alternatives:
        - {value: 4, note: "P16 addendum: a remark on lawful order cannot rule out a no-exception nature.", cites: [{source: S4, locator: "transcript, religion exchange"}]}
    C_ledger: {value: UNKNOWN, how_known: "(interview) Nothing on reward and punishment of persons (P19)."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "(interview) Lead only: the line 'new means are needed for inner self regulation based on naturalistic rather than on arbitrary moralistic formulations' is the interviewer reading from The Survival of the Wisest (1973), which was not read; Salk answers only 'Yes'. Reported text cannot score alone."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "(interview) 'we are manifestations of the existence of order' is a lead that humans fall under the same order, not a statement that the same rules govern human choice."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "P4 test: A 4 at 0.5, below the 0.7 threshold the branch needs (Hawking, Watson, Shannon precedents)."}
  statements:
    - text: "Now, to me, it is the existence of order that is fundamental to our existence, that we are manifestations of the existence of order."
      cites: [{source: S4, locator: "transcript, religion exchange"}]
      date: "1981-06-30"
      context: "Answering John Callaway's question on reverence for religion; he has just said religion 'is based upon a belief system ... in a certain way in which the world is put together'."
      axes: [B_cause, A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "AAPB transcript (status 'Correct'); broadcast date from the AAPB record."
    - text: "Now, some might say that my use of the term order is the same as the word God. We're both describing the same phenomenon. The difference between the idea of order and the idea of an anthropomorphic God. A God that is in the form of a person that thinks like a person and a personal God that looks after me personally and individually."
      cites: [{source: S4, locator: "transcript, religion exchange"}]
      date: "1981-06-30"
      context: "Same exchange, after Callaway's lines about the table and the sun."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Transcript line breaks joined."
    - text: "Well, that's why God was invented. You see God was invented because of the necessity for having a form of order."
      cites: [{source: S4, locator: "transcript, religion exchange"}]
      date: "1981-06-30"
      context: "Reply to Callaway's 'It's why they made a god out of you.'"
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Basis of the ATHE and BELOW_THRESHOLD alternatives."
    - text: "I'm very much aware of the miracle of life and very much aware of the miracle of man. And for me, that's where that's where God is. That's where creation exists now."
      cites: [{source: S4, locator: "transcript, closing segment"}]
      date: "1981-06-30"
      context: "Closing segment, on the Salk Institute's 'temple'-like architecture and scientists as 'the new priesthood'."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Repetition as transcribed."
  changes_over_life:
    - {value: "Childhood prayer gave way to self-reliance ('I had to do something about it myself')", certainty: 0.5, cites: [{source: S4, locator: "transcript, religion exchange"}], how_known: "(interview) His recollection; undated."}
  coder_notes: "Coder's call. Every worldview claim rests on one 1981 interview, 26 years after the working years, so all are capped at 0.5 (P1). PANT against ATHE is the main question: he accepts that his 'order' and others' 'God' describe 'the same phenomenon' and locates God in life, but also says God 'was invented'. Leads: Man Unfolding (1972), The Survival of the Wisest (1973), Anatomy of Reality (1983); not read."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Jewish (Russian-Jewish immigrant parents)", certainty: 0.7, cites: [{source: S2, locator: "Salk's Education"}, {source: S3, locator: "opening"}], how_known: "Both pages; they differ on the father's generation."}
  religious_heritage_by_birth: {value: "Jewish", certainty: 0.5, cites: [{source: S2, locator: "Salk's Education"}, {source: S3, locator: "opening"}], how_known: "Inferred from 'Jewish immigrants'; practice not stated."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1952–1955", certainty: 0.7, cites: [{source: S2, locator: "The 'Killed-Virus' Principle; Field Trials"}], how_known: "From the first human tests (1952) to the announced field-trial result (12 April 1955): one lasting contribution dated as a range (P12, P29, P30)."}
  age_at_first_lasting_contribution: {value: 38, certainty: 0.7, cites: [{source: S1, locator: "facts box"}, {source: S2, locator: "The 'Killed-Virus' Principle"}], how_known: "1952 − 1914 = 38 (P30); 37 or 38 depending on the month of the first tests."}
  first_evidence_of_lio_type_views: {value: "1981 (interview): 'that's where God is' — A 4", year: 1981, certainty: 0.5, cites: [{source: S4, locator: "transcript"}], how_known: "(interview) The earliest source read; earlier works not read (P30 #7); the 1970s books are leads."}
  lio_views_relative_to_major_work: {value: "after major work", certainty: 0.5, cites: [{source: S4, locator: "transcript"}], how_known: "(interview) First evidence read is 26 years after the span; no earlier evidence read."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "Salk's Education"}], how_known: "Not assessed."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "Salk's Education"}], how_known: "Not read."}
  circle_present: {value: "unclear", rationale: "God and order 'the same phenomenon' and humans 'manifestations' of order would suggest it, but only in a late interview, with 'God was invented' against it.", certainty: 0.5, cites: [{source: S4, locator: "transcript"}], how_known: "(interview) Coder's reading."}
  reading: "Order as the fundamental reality, named God by others, located in life and man; human self-reliance in place of prayer."
  notes: ""

institutions:
  - {value: "University of Pittsburgh School of Medicine (Virus Research Laboratory)", role: "associate professor of bacteriology and head of the laboratory, later professor", years: "1947–1963", kind: university, certainty: 0.7, cites: [{source: S1, locator: "body"}, {source: S2, locator: "The Virus Research Laboratory"}], how_known: "Britannica and SHI; end year the coder's."}
  - {value: "University of Michigan School of Public Health", role: "research fellow, later assistant professor of epidemiology", years: "1942–1947", kind: university, certainty: 0.7, cites: [{source: S1, locator: "body"}, {source: S3, locator: "1942 paragraph"}], how_known: "Britannica and the Salk Institute."}
  - {value: "National Foundation for Infantile Paralysis (March of Dimes)", role: "funded the polio work and the field trial", kind: "patron or funder", certainty: 0.7, cites: [{source: S2, locator: "The Virus Research Laboratory; Field Trials"}, {source: S3, locator: "1947 paragraph"}], how_known: "SHI and the Salk Institute."}
  - {value: "Salk Institute for Biological Studies", role: "founder, fellow and director", years: "1963–1995", kind: "research institute", certainty: 0.5, cites: [{source: S1, locator: "last paragraph"}, {source: S3, locator: "1963 paragraph"}], how_known: "Britannica and the Salk Institute say 1963; SHI says 1962. 0.5."}
collaborators:
  - {value: "Thomas Francis Jr.", relation: teacher, note: "mentor at NYU and Michigan; directed the 1954 field trial", certainty: 1.0, cites: [{source: S2, locator: "Salk's Education; Field Trials"}, {source: S3, locator: "1942 paragraph"}], how_known: "SHI and the Salk Institute."}
  - {value: "Albert Sabin", relation: "rival or critic", note: "live-virus oral vaccine; long dispute", certainty: 0.7, cites: [{source: S2, locator: "Live-Virus versus Killed-Virus Controversy"}], how_known: "SHI."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 112"}], how_known: "Study roster."}
  controversies:
    - {value: "Not awarded a Nobel Prize nor elected to the National Academy of Sciences; colleagues' animosity ('publicity hound')", certainty: 0.7, cites: [{source: S2, locator: "Later Research"}], how_known: "SHI."}
  data_quality_flags:
    - "All worldview evidence is one recorded interview after the working years."
    - "Sources differ on the father's birthplace and on the Salk Institute's founding year (1962/1963)."
  open_questions:
    - "Read Man Unfolding (1972), The Survival of the Wisest (1973) and Anatomy of Reality (1983) for written statements on God and order."
    - "Family religious practice."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors (revised by Kara Rogers)"
    citation: "Britannica Editors. \"Jonas Salk.\" Encyclopaedia Britannica (updated 10 September 2026). https://www.britannica.com/biography/Jonas-Salk. Read live 2026-10-19."
    url: "https://www.britannica.com/biography/Jonas-Salk"
    accessed: 2026-10-19
    reliability_note: "Unsigned body; facts box and body cited, the question boxes not."
    used_for: [identity, basics, contribution, timing, institutions]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "Science History Institute"
    citation: "Science History Institute. \"Jonas Salk and Albert Bruce Sabin.\" Scientific Biographies. https://www.sciencehistory.org/education/scientific-biographies/jonas-salk/"
    url: "https://www.sciencehistory.org/education/scientific-biographies/jonas-salk/"
    accessed: 2026-10-19
    reliability_note: "Museum and library biography; unsigned."
    used_for: [basics, contribution, childhood, heritage, timing, institutions, collaborators, review]
  - id: S3
    type: secondary
    kind: "institutional page"
    author: "Salk Institute for Biological Studies"
    citation: "Salk Institute. \"About Jonas Salk.\" History of Salk. https://www.salk.edu/about/history-of-salk/jonas-salk/"
    url: "https://www.salk.edu/about/history-of-salk/jonas-salk/"
    accessed: 2026-10-19
    reliability_note: "The institute he founded; may be laudatory."
    used_for: [identity, basics, contribution, childhood, heritage, institutions, collaborators]
  - id: S4
    type: primary
    kind: other
    author: "Jonas Salk, with John Callaway"
    citation: "\"Jonas Salk.\" The John Callaway Interviews, WTTW (Chicago), broadcast 30 June 1981. American Archive of Public Broadcasting, cpb-aacip-526-g73707xt6p; transcript (AAPB status 'Correct')."
    url: "https://americanarchive.org/catalog/cpb-aacip-526-g73707xt6p"
    accessed: 2026-10-19
    reliability_note: "Archive transcript of a recorded broadcast interview; his own words count (P8), the interviewer's lines and quotations do not. After the working years (P1 cap 0.5)."
    used_for: [worldview, childhood, timing, lane_b]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Jonas Salk

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Jonas Salk (1914–1995), American physician and virologist who developed the first safe and effective polio vaccine [S1]. Draft (interview only): primary_system PANT (0.5, alt ATHE); A 4 (0.5); B 3 (0.5, alt 4); mid_basin BELOW_THRESHOLD. Plotted (faded).

## Life and work

NYU, Michigan, Pittsburgh, the Salk Institute [S1, S2, S3].

## Contribution and impact

The killed-virus polio vaccine, 1952–1955 [S2].

## Childhood and education

Eldest son of Jewish immigrant parents in New York [S2, S3].

## Adult working worldview

(Interview, 1981.) 'my use of the term order is the same as the word God' [S4].

## Heritage (context only)

Jewish [S2, S3].

## Timing

1952–1955, from age 38 [S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Order as the fundamental reality [S4].

## Open questions

- His 1970s–80s books.

## Research log

- 2026-10-19: Read Britannica, SHI, the Salk Institute page and the AAPB transcript.
