---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch S)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-18
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-18, by: "Grok Bot", summary: "Record created (stage 3 batch S, order P32: F 4, rank 107). Basics from Britannica (Britannica Editors, unsigned; body only, read live) and Nature's page for her 1964 paper. Worldview from two interviews in her own words, both after the working years (1964–1986): On Being with Krista Tippett (recorded 2020; producer's transcript) and The Guardian (Stephen Moss, 13 January 2010). Scientist (P30). primary_system BELOW_THRESHOLD (candidates CHRIST, DEISM blocked by P27, PANENT, AGNOS); A 2 (0.5, interview; alt BELOW_THRESHOLD); B 3 (0.5, P35; alt 4); C UNKNOWN; D BELOW_THRESHOLD; E BELOW_THRESHOLD (P19); mid_basin BELOW_THRESHOLD. Plotted (faded) at A2/B3; A 2 sits between the branches of the mid-basin test. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit fixes for batch S (blind audit of c5d448a, run 1: GO5 WEAKEN; note). The 'just chance' line is marked as reported: it is what 'all of these great brains have said' (after Francis Collins), not her own argument. A 1 named as a second alternative. No value changes."}

identity:
  id: goodall-jane
  display_name: "Jane Goodall"
  roster:
    canonical_name: "Jane Goodall"
    rank: 107
    F: 4
    models: [Claude, Gemini, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: biology
    field_bucket: "biology / life science"
  full_name: {value: "Dame Jane Goodall", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts ('In full')"}], how_known: "Britannica Quick Facts (not the AI Top Questions box)."}
  native_name: {value: "Valerie Jane Morris-Goodall", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts ('Original name')"}], how_known: "Britannica: original name."}
  aliases:
    - {name: "Goodall-Jane", kind: "roster alias"}
    - {name: "Jane-Goodall", kind: "roster alias"}

basics:
  birth:
    date: {value: "1934-04-03", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica body."}
    place: {value: "London, England", modern_name: "London, United Kingdom", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "2025-10-01", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "programme note"}], how_known: "Britannica and On Being's memorial note agree (independent)."}
    place: {value: "Los Angeles, California, U.S.", modern_name: "Los Angeles, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1964, certainty: 0.5, cites: [{source: S4, locator: "article page"}], how_known: "Her paper on chimpanzee tool-using in Nature, published 28 March 1964 (S4); the earliest dated item listed (P13, P30). The paper cites her own earlier papers (Ann. N.Y. Acad. Sci. 102, 1962; Symp. Zool. Soc. Lond. 10, 1963), not read, so the year might be 1962 or 1963 (named alternatives; coder's call at 0.5).", alternatives: [{value: 1963, note: "Symposium paper (unread).", cites: [{source: S4, locator: "references 7"}]}, {value: 1962, note: "Annals paper (unread).", cites: [{source: S4, locator: "references 12"}]}]}
  era_bucket: {value: "1950 on", certainty: 0.7, cites: [{source: S4, locator: "article page"}], how_known: "1964 and both alternatives fall in the same bucket (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United Kingdom (P3)."}
  region_of_work: {value: "Sub-Saharan Africa", certainty: 0.7, cites: [{source: S1, locator: "camp paragraph"}], how_known: "Gombe Stream, Tanzania (P3); writing done partly in Cambridge."}
  sex_as_recorded: {value: "female", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "books paragraph"}], how_known: "English titles (S1)."}
  occupations: {value: ["ethologist", "primatologist", "conservationist"], certainty: 0.7, cites: [{source: S1, locator: "opening; books paragraph"}], how_known: "Britannica ('British ethologist'; wrote and lectured on conservation)."}

contribution:
  fields: {value: ["ethology", "primatology"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Chimpanzees make and use tools: 'Tool-Using and Aimed Throwing in a Community of Free-Living Chimpanzees' (Nature)", year: 1964, kind: discovery, lasting: "Britannica lists tool-making among the misunderstandings she corrected (S1)", certainty: 0.5, cites: [{source: S4, locator: "article page"}, {source: S1, locator: "findings paragraph"}], how_known: "Britannica does not date the finding; the Nature page dates the paper (28 March 1964). Earlier papers not read (see first_lasting_contribution_year). A result about animal behaviour from field observation, so she is a scientist (P30, P35 addendum)."}
    - {value: "Long-term field findings on chimpanzees: omnivorous diet and 'complex and highly developed social behaviors'", year: "1960s–1986", kind: "body of work", lasting: "corrected 'a number of misunderstandings about chimpanzees' (S1)", certainty: 0.7, cites: [{source: S1, locator: "findings paragraph"}], how_known: "Britannica gives no year; not used for the span (CODING_GUIDE §8)."}
    - {value: "In the Shadow of Man", year: 1971, kind: work, lasting: "named as notable (S1)", certainty: 0.7, cites: [{source: S1, locator: "books paragraph"}], how_known: "Britannica."}
    - {value: "The Chimpanzees of Gombe: Patterns of Behavior, the summary of her years of observation", year: 1986, kind: work, lasting: "her summary work (S1)", certainty: 0.7, cites: [{source: S1, locator: "books paragraph"}], how_known: "Britannica; the latest listed lasting contribution (P30 addendum). Her later work was advocacy (S1, S2)."}
  evidence_of_impact:
    - {value: "Templeton Prize (2021); DBE (2003); Stephen Hawking Medal for Science Communication (2022); Presidential Medal of Freedom (2025)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "honours paragraph"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Long-term field research that changed the scientific account of chimpanzees (S1).", certainty: 0.7, cites: [{source: S1, locator: "findings paragraph"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Christian (Congregational): grandfather a Congregational minister", certainty: 0.7, cites: [{source: S2, locator: "childhood exchange"}, {source: S3, locator: "Christian paragraph"}], how_known: "(interview) 'my grandfather was a Congregational minister. I never met him' (S2); 'I was raised as a Christian' (S3). Two interviews, her own words."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Lived in Bournemouth with her mother, sister, grandmother and her mother's two sisters", certainty: 0.7, cites: [{source: S2, locator: "childhood exchange"}], how_known: "(interview) Her own account (S2)."}
  household_circumstances: {value: TODO}
  schooling:
    - {value: "Left school at 18; no undergraduate degree", stage: "grammar or secondary school", years: "–1952", certainty: 0.7, cites: [{source: S1, locator: "early-life paragraph"}], how_known: "Britannica; school not named; years by the coder from age 18."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "'interested in animal behavior from an early age'", certainty: 0.7, cites: [{source: S1, locator: "early-life paragraph"}], how_known: "Britannica."}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["English"], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1964–1986", certainty: 0.5, cites: [{source: S4, locator: "article page"}, {source: S1, locator: "books paragraph"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "'I suppose so; I was raised as a Christian' (asked if she was still a Christian, 2010)", certainty: 0.5, cites: [{source: S3, locator: "Christian paragraph"}], how_known: "(interview) Her words; the interviewer calls the answer 'somewhat ambiguous'. Context only: upbringing gives no code (CHRIST do_not_use_when)."}
  self_described_science_religion_relation: {value: "(interview) She 'sees no contradiction between evolution and a belief in God' (2010, interviewer's paraphrase); 'there are some answers that, at least on this planet, this life, this life-form, we will not be able to answer' (2020)", certainty: 0.5, cites: [{source: S3, locator: "Christian paragraph"}, {source: S2, locator: "closing exchange"}], how_known: "(interview) The first part is a paraphrase (S3); the second her own words (S2); both after the working years (P20 ruling P1)."}
  primary_system:
    value: BELOW_THRESHOLD
    how_known: "(interview) Coder's call. Her words name an unknown 'intelligence behind the universe', 'probably what it is', of which she has not 'the faintest idea' (S2, 2020), and a nominal Christianity (S3, 2010). No code's use_when is met: CHRIST needs Christian belief in her writing, not upbringing; DEISM needs the rejection of revelation (P27), which she does not state; PANENT needs a divine reality that includes the world and exceeds it, which she does not say; AGNOS is ruled out by 'I'm absolutely sure that there is something'. Both interviews fall after the working years, so any code would be capped at 0.5 anyway."
    note: "Lead: Reason for Hope (1999), quoted by The Guardian: 'I was utterly convinced there was a great spiritual power that we call God, Allah or Brahma, although I knew, equally certainly, that my finite mind could never comprehend its form or nature' (secondary quotation; the book is lending-only on the Internet Archive and was not read). Also a lead: the Reader's Digest interview (September 2010, 'some great spiritual power'), known only from blog quotations."
  secondary_system: {value: UNKNOWN, how_known: "No system coded."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "'I suppose so; I was raised as a Christian' (S3); rejected: upbringing and a hedged label give no code."}
    - {code: DEISM, reason: "An intelligence behind the universe, which she introduces by reporting what 'all of these great brains have said', that 'there is no way that what's happened is just chance' (S2; reported, after Francis Collins, not her own argument); blocked: revelation is not rejected (P27)."}
    - {code: PANENT, reason: "Spiritual connection felt in the natural world (S2); rejected: no statement that the divine includes and exceeds the world."}
    - {code: AGNOS, reason: "'I haven't the faintest idea' what it is (S2); rejected: she is 'absolutely sure that there is something'."}
  lio_axes:
    A_locus:
      value: 2
      basis: recorded_interview
      certainty: 0.5
      cites: [{source: S2, locator: "closing exchange"}]
      rationale: "Mixed: an intelligence 'behind the universe' (beyond it, toward the transcendent pole) that is 'probably what it is', not who (not clearly a person, toward the LIO pole), and a 'spiritual connection to the natural world' felt in the forest. The features of both poles are present and neither is stated as limited, so 2. Named alternatives: BELOW_THRESHOLD (she has not 'the faintest idea' what it is) and 1 ('behind the universe' read as a transcendent locus)."
      how_known: "(interview) One recorded interview, her own words (P8), from 2020, after the working years (1964–1986), so 0.5 (P20 ruling P1, Shannon and Watson precedent)."
      alternatives:
        - {value: BELOW_THRESHOLD, note: "'I haven't the faintest idea'.", cites: [{source: S2, locator: "closing exchange"}]}
        - {value: 1, note: "'behind the universe' read as a transcendent locus; mid_basin stays BELOW_THRESHOLD at 0.5.", cites: [{source: S2, locator: "closing exchange"}]}
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      cites: [{source: S4, locator: "article page"}, {source: S1, locator: "findings paragraph"}]
      rationale: "Scored on her account of nature (P6). She is a scientist (P30), so B comes from her working science: lawful field observation of animal behaviour, B 3 with 4 as the named alternative, never 4 (P35). The line 'there is no way that what's happened is just chance' (S2, 2020) is reported speech: she gives it as what 'all of these great brains have said' (philosophers of science, physicists, Francis Collins), not as her own argument; in any case it states no exception within nature, so it does not move B."
      how_known: "Inferred from her working science (P24, P35)."
      alternatives:
        - {value: 4, note: "P35 alternative.", cites: [{source: S4, locator: "article page"}]}
    C_ledger: {value: UNKNOWN, how_known: "(interview) Nothing on reward and punishment in the sources read (S1–S4)."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "(interview) She says some questions 'we will not be able to answer' and is 'peeved' by scientists who think the Big Bang settles origins (S2), but names no source that outranks observation; revelation is not mentioned. Too indirect (P19)."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Not scored from working science alone (P19); no statement on the world's order read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "(interview) P4 test: A 2 sits between the branches and is scored only at 0.5, under the 0.7 bar; B 3 at 0.5. A needed axis is scored only at 0.5, so BELOW_THRESHOLD (§6)."}
  statements:
    - text: "What that intelligence behind the universe is — what it is, who it is; probably what it is — I haven’t the faintest idea, but I’m absolutely sure that there is something. And seeking for that something is part of being human."
      cites: [{source: S2, locator: "closing exchange"}]
      date: "2020"
      context: "On Being with Krista Tippett, recorded over Zoom from Bournemouth in 2020 (original air date 6 August 2020); her closing answer on what it means to be human, straight after she reports that 'all of these great brains have said there is no way that what’s happened is just chance' (reported, after Francis Collins; not her own argument)."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-18
      note: "The producer's own transcript on onbeing.org (official site of the producing institution)."
    - text: "And that’s where I felt that deep, spiritual connection to the natural world, and also came to understand the interconnectedness of all living things in this tapestry of life where each species, no matter how insignificant, plays a probably vital role in the whole pattern."
      cites: [{source: S2, locator: "1986 exchange"}]
      date: "2020"
      context: "Same interview (2020), looking back on the years up to 1986; on her years in the rainforest before the 1986 Chicago conference. A retrospective self-report about the working years."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-18
      note: ""
    - text: "I suppose so; I was raised as a Christian."
      cites: [{source: S3, locator: "Christian paragraph"}]
      date: "2010"
      context: "The Guardian, Stephen Moss, 13 January 2010; asked whether she is still a Christian. Context only (nominal_affiliations)."
      axes: []
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-18
      note: "Quoted in the interviewer's article, read on the publisher's site."
  changes_over_life:
    - {value: "1986: from field science to conservation advocacy after the Chicago conference (her 'Road to Damascus moment' in the interviewer's words); not a documented change of religious view", year: 1986, certainty: 0.7, cites: [{source: S2, locator: "1986 exchange"}], how_known: "(interview) Her account (S2); off-point for A–E."}
  coder_notes: "Coder's call throughout. Every first-person statement read is from after the working years (2010, 2020), so the P20 cap (ruling P1) keeps every worldview field at 0.5 at most. The book Reason for Hope (1999) is the main unread lead; a reading of it could give a code. A 2 is a coder's call: if the auditor reads 'behind the universe' as a transcendent locus, A would be 1, which still leaves mid_basin BELOW_THRESHOLD at 0.5."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica ('British')."}
  religious_heritage_by_birth: {value: "Congregationalist family", certainty: 0.7, cites: [{source: S2, locator: "childhood exchange"}, {source: S3, locator: "Christian paragraph"}], how_known: "(interview) Two interviews."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1964–1986", certainty: 0.5, cites: [{source: S4, locator: "article page"}, {source: S1, locator: "books paragraph"}], how_known: "Nature paper (1964) to The Chimpanzees of Gombe (1986), first to last listed lasting contribution (P29, P30). Start might be 1962 or 1963 (see first_lasting_contribution_year)."}
  age_at_first_lasting_contribution: {value: 30, certainty: 0.5, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "article page"}], how_known: "1964 − 1934 = 30 (P30); 28 or 29 under the alternatives."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement of hers is scored at 3 or 4 (A 2; B 3 is inferred from working science, so not an LIO-type view, P27)."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "closing exchange"}], how_known: "(interview) In the sources read."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "(interview) No statement from the working years was read; her 2020 retrospective names only a 'spiritual connection to the natural world' (S2)."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Field naturalist; no definition-to-consequence work read.", certainty: 0.5, cites: [{source: S1, locator: "findings paragraph"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "early-life paragraph"}], how_known: "Not read."}
  circle_present: {value: "no", rationale: "An intelligence 'behind' the universe, not identified with it.", certainty: 0.5, cites: [{source: S2, locator: "closing exchange"}], how_known: "(interview) Coder's reading."}
  reading: "A field scientist with a late, undefined spiritual theism; nothing from the working years read."
  notes: ""

institutions:
  - {value: "Gombe Stream Game Reserve camp (now Gombe Stream National Park), Tanzania", role: "founder of the research camp", years: "1960–", kind: "research institute", certainty: 0.7, cites: [{source: S1, locator: "camp paragraph"}], how_known: "Britannica ('establishment in June 1960 of a camp'); kind the coder's."}
  - {value: "University of Cambridge", role: "Ph.D. in ethology", years: "–1965", kind: university, certainty: 0.7, cites: [{source: S1, locator: "Ph.D. paragraph"}, {source: S4, locator: "affiliation"}], how_known: "Britannica; Nature lists her at the Sub-Department of Animal Behaviour, Madingley."}
  - {value: "Jane Goodall Institute", role: founder, years: UNKNOWN, kind: other, certainty: 0.7, cites: [{source: S2, locator: "guest note"}], how_known: "On Being guest note; founding year not given in the sources read."}
collaborators:
  - {value: "Louis Leakey", relation: "mentor or employer", note: "she began by assisting him", certainty: 0.7, cites: [{source: S1, locator: "early-life paragraph"}], how_known: "Britannica."}
  - {value: "Hugo van Lawick", relation: other, note: "photographer who filmed her work; husband 1964, later divorced", certainty: 0.7, cites: [{source: S1, locator: "camp paragraph"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 107"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Britannica article is unsigned (Britannica Editors); read live; Top Questions box not used."
    - "Every worldview statement read is from after the working years (P20 cap)."
    - "Reason for Hope (1999) not read: lending-only on the Internet Archive; its sentence on 'a great spiritual power that we call God, Allah or Brahma' is known only from The Guardian."
  open_questions:
    - "Read Reason for Hope (1999), especially the Notre-Dame passage, and any statement from 1960–1986."
    - "Read her 1962 and 1963 papers to fix the first-lasting year."
    - "Find the Reader's Digest interview (September 2010) in print."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Jane Goodall.\" Encyclopaedia Britannica (revised 27 September 2026). https://www.britannica.com/biography/Jane-Goodall. Read live 2026-10-18."
    url: "https://www.britannica.com/biography/Jane-Goodall"
    accessed: 2026-10-18
    reliability_note: "Unsigned article. Body and Quick Facts only; the AI-generated Top Questions are not cited."
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, collaborators, lane_b]
  - id: S2
    type: primary
    kind: other
    author: "Jane Goodall, with Krista Tippett"
    citation: "Tippett, Krista. \"Jane Goodall, in Memoriam — What It Means to Be Human.\" On Being (The On Being Project); conversation recorded over Zoom in 2020, original air date 6 August 2020; transcript on the programme page. https://onbeing.org/programs/jane-goodall-what-it-means-to-be-human/"
    url: "https://onbeing.org/programs/jane-goodall-what-it-means-to-be-human/"
    accessed: 2026-10-18
    reliability_note: "Producer's transcript of a recorded conversation; her first-person words (P8). An editor's note in the transcript corrects one of her remarks (on Francis Collins)."
    used_for: [worldview, childhood, heritage, institutions, timing, lane_b]
  - id: S3
    type: primary
    kind: other
    author: "Stephen Moss"
    citation: "Moss, Stephen. \"Jane Goodall: 'My job is to give people hope'.\" The Guardian, 13 January 2010 (online 12 January 2010, 19.05 EST). https://www.theguardian.com/science/2010/jan/13/jane-goodall"
    url: "https://www.theguardian.com/science/2010/jan/13/jane-goodall"
    accessed: 2026-10-18
    reliability_note: "Interview article: her quoted words count as hers (P8); the interviewer's paraphrases do not."
    used_for: [worldview, childhood, heritage]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Jane Goodall"
    citation: "Goodall, Jane. \"Tool-Using and Aimed Throwing in a Community of Free-Living Chimpanzees.\" Nature 201 (1964): 1264–1266; published 28 March 1964. https://www.nature.com/articles/2011264a0"
    url: "https://www.nature.com/articles/2011264a0"
    accessed: 2026-10-18
    reliability_note: "Publisher's article page (title, date, affiliation, reference list); the article text is paywalled and was not read."
    used_for: [basics, contribution, timing, institutions, worldview]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-18
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Jane Goodall

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Jane Goodall (1934–2025), British ethologist of the Gombe chimpanzees [S1]. Draft: primary_system BELOW_THRESHOLD; A 2 at 0.5 (interview); B 3 at 0.5 (P35); mid_basin BELOW_THRESHOLD. Plotted (faded).

## Life and work

London, Gombe (from 1960), Cambridge Ph.D. 1965 [S1].

## Contribution and impact

Tool use (Nature, 1964) [S4]; In the Shadow of Man (1971); The Chimpanzees of Gombe (1986) [S1].

## Childhood and education

Grandfather a Congregational minister [S2]; left school at 18 [S1].

## Adult working worldview

'that intelligence behind the universe ... I haven’t the faintest idea, but I’m absolutely sure that there is something' (2020, interview) [S2].

## Heritage (context only)

Congregationalist family [S2, S3].

## Timing

1964–1986, from age 30 [S1, S4].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle [S2].

## Open questions

- Read Reason for Hope (1999).

## Research log

- 2026-10-18: Read Britannica (live), the On Being transcript, The Guardian interview and Nature's article page. Reason for Hope is lending-only on the Internet Archive (full text not available).
