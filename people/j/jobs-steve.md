---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Y)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit fixes for batch Y (gs_7b46f24_Y run 1): (JO12) definition_fit and the iPhone's lasting note now cite Britannica's article body ('a charismatic pioneer of the personal computer era'; 'near-messianic belief in the computer revolution'), not the 'Why is Steve Jobs significant?' question box (P26). Ruling Y1 (v8's call on the auditor's advice): primary_system stays BELOW_THRESHOLD (recorded under P43, beside V3). No score changes."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Y, order P32: F 4, rank 132; roster status provisional). Basics from Britannica (Steven Levy, updated 29 Sep 2026). Own voice read in the prepared text of the 2005 Stanford commencement address (in the span). His words on God reach us only as the Washington Post's quotations of Isaacson's 2011 biography (secondary quotation, after the span): 'I'm about fifty-fifty on believing in God'. Not a scientist (P33). Span 1977–2007 at 0.7 (Apple II to iPhone). primary_system BELOW_THRESHOLD (AGNOS lead, BUDDH lead; RQ-Y1); A BELOW_THRESHOLD; B, C, E UNKNOWN; D BELOW_THRESHOLD; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: jobs-steve
  display_name: "Steve Jobs"
  roster:
    canonical_name: "Steve Jobs"
    rank: 132
    F: 4
    models: [DeepSeek, Gemini, GPT, Grok]
    band: "core (3–4)"
    status: provisional
    field: technology
    field_bucket: "invention / engineering"
  full_name: {value: "Steven Paul Jobs", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts (Also Known As)"}], how_known: "Britannica."}
  native_name: {value: "Steven Paul Jobs", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "English is his own language."}
  aliases:
    - {name: "Jobs-Steve", kind: "roster alias"}
    - {name: "Steve-Jobs", kind: "roster alias"}

basics:
  birth:
    date: {value: "1955-02-24", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts (Born)"}], how_known: "Britannica."}
    place: {value: "San Francisco, California", modern_name: "San Francisco, California, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts (Born)"}], how_known: "Britannica."}
  death:
    date: {value: "2011-10-05", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts (Died)"}], how_known: "Britannica."}
    place: {value: "Palo Alto, California", modern_name: "Palo Alto, California, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts (Died)"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1977, certainty: 0.7, cites: [{source: S1, locator: "'Founding of Apple'"}], how_known: "The Apple II, completed in 1977, 'an immediate success, becoming synonymous with the boom in personal computers' (S1). The Apple I (1976) is not called lasting. Designed by Wozniak 'with Jobs's encouragement', so attribution is shared (roster note)."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "'Founding of Apple'"}], how_known: "From 1977 (P2)."}
  region_of_birth: {value: "North America", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}], how_known: "United States (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "'Founding of Apple'"}], how_known: "Silicon Valley."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S2, locator: "text"}], how_known: "His address."}
  occupations: {value: ["businessman", "cofounder and CEO of Apple", "founder of NeXT", "owner of Pixar"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'NeXT and Pixar'"}], how_known: "Britannica."}

contribution:
  fields: {value: ["personal computing", "consumer electronics", "product design"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Reinventing Apple'"}], how_known: "Britannica; labels the coder's."}
  lasting_original_contributions:
    - {value: "Apple II personal computer (with Steve Wozniak)", year: 1977, kind: invention, lasting: "'becoming synonymous with the boom in personal computers' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Founding of Apple'"}], how_known: "Britannica; Wozniak designed it, Jobs pushed the design and case and found financing (S1)."}
    - {value: "Macintosh, with its graphical user interface", year: 1984, kind: invention, lasting: "'the model for all subsequent computer interfaces' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Insanely great'"}], how_known: "Britannica: Jobs headed the project and introduced it in January 1984."}
    - {value: "iPod and the iTunes ecosystem", year: 2001, kind: invention, lasting: "'quickly became the market leader' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Reinventing Apple'"}], how_known: "Britannica."}
    - {value: "iPhone", year: 2007, kind: invention, lasting: "took Apple 'into the telecommunications business' (S1); the Apple II, Macintosh, iPod and iPhone are the dated products in 'Reinventing Apple' and earlier sections (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Reinventing Apple'"}], how_known: "Britannica. Latest dated lasting item, so it ends the span (P30 addendum b); the iPad (2010) appears only in a photo caption, so it is not listed."}
  evidence_of_impact:
    - {value: "Presidential Medal of Freedom (2022, posthumous)", kind: "other", certainty: 0.7, cites: [{source: S1, locator: "'Health issues'"}], how_known: "Britannica; after his death."}
    - {value: "The Mac interface became 'the model for all subsequent computer interfaces'", kind: "institutional or technological lineage", certainty: 0.7, cites: [{source: S1, locator: "'Insanely great'"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "arguable", rationale: "Britannica's body calls him 'a charismatic pioneer of the personal computer era' and notes his 'near-messianic belief in the computer revolution'; the roster flags 'attribution vs. team' (S4).", certainty: 0.5, cites: [{source: S1, locator: "introduction; 'Founding of Apple'"}, {source: S4, locator: "roster.csv, rank 132"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated in the sources read."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Adopted at birth; his biological mother was 'a young, unwed graduate student'", role: family, certainty: 0.7, cites: [{source: S2, locator: "first story"}], how_known: "His own address."}
    - {value: "Adoptive parents in Cupertino, California; adoptive father Paul Jobs, who tinkered with cars", role: family, certainty: 0.7, cites: [{source: S1, locator: "'Founding of Apple'"}, {source: S3, locator: "'Why are you . . . so mean?' section"}], how_known: "Britannica; the father's name from the Washington Post."}
  household_circumstances: {value: "Working-class: 'my mother had never graduated from college, and ... my father had never graduated from high school'", certainty: 0.7, cites: [{source: S2, locator: "first story"}], how_known: "His own address."}
  schooling:
    - {value: "Reed College, Portland, Oregon (dropped out after six months; stayed as a drop-in for about 18 months, including a calligraphy class)", stage: university, run_by: private, years: "c. 1972–1974", certainty: 0.5, cites: [{source: S2, locator: "first story"}, {source: S1, locator: "'Founding of Apple'"}], how_known: "His address and Britannica; years the coder's (college at 17; Atari job early 1974)."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading:
    - {value: "The Whole Earth Catalog ('one of the bibles of my generation')", certainty: 0.7, cites: [{source: S2, locator: "closing"}], how_known: "His own address."}
  childhood_mentors: []
  languages_in_childhood: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "Pilgrimage to India 'to experience Buddhism' (seven months)", year: 1974, certainty: 0.7, cites: [{source: S1, locator: "'Founding of Apple'"}, {source: S3, locator: "'Why are you . . . so mean?' section"}], how_known: "Britannica (back by autumn 1974); 'seven-month trip' from the Washington Post. Adult event (age 19), recorded here as formative."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1977–2007", certainty: 0.7, cites: [{source: S1, locator: "'Founding of Apple'; 'Reinventing Apple'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read on science and religion."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "Leads only. AGNOS: 'I'm about fifty-fifty on believing in God' and 'different religions are different doors to the same house. Sometimes I think the house exists, and sometimes I don't. It's the great mystery' (S3), an explicit suspension in his own words, but known only as the Washington Post's quotations of Isaacson's 2011 biography (secondary quotation, §7) and said late in life, after the span (P1). BUDDH: years studying Zen (S3) and the India pilgrimage (S1); study and practice alone are not BUDDH (do_not_use_when), and he states no adherence. His 2005 address (in the span) names no system: 'You have to trust in something: your gut, destiny, life, karma, whatever' (S2). Ruling Y1 (v8's call on the auditor's advice): stays BELOW_THRESHOLD. The words are read only as the Washington Post's quotation of Isaacson (secondary quotation, P26; V3) and fall after the span (P1). Path to AGNOS at 0.5 (interview), BELOW_THRESHOLD alternative: read the passages in the biography itself, the interviewer's own first publication of his words (P8)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Lead: 'fifty-fifty on believing in God' (S3, secondary quotation, after the span)."}
    - {code: BUDDH, reason: "Lead: Zen study and the India pilgrimage; no stated adherence (BUDDH do_not_use_when)."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "An explicit suspension ('fifty-fifty on believing in God'; 'Sometimes I think the house exists, and sometimes I don't', S3) is BELOW_THRESHOLD in any case (§6, P20), and it is known only by secondary quotation after the span. The 2005 address mentions heaven only as others' hope ('Even people who want to go to heaven don't want to die to get there', S2)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P33: products, not theories). Nothing read on law and exception in nature; 'karma' in the 2005 address is a thing to trust, not a statement about nature (P16, P19)."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing on reward or punishment of persons; his hope that 'something survives after you die' against 'perhaps it's like an on-off switch' (S3) concerns survival, not a ledger (P19)."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "Lead from his own address (2005, in the span): 'Don't be trapped by dogma, which is living with the results of other people's thinking. Don't let the noise of others' opinions drown out your own inner voice' (S2). It sets the inner voice against received dogma, not observation against revelation, so it does not reach a value."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7, P19)."}
  mid_basin: {value: UNKNOWN, how_known: "B is UNKNOWN (P19)."}
  statements:
    - text: "You have to trust in something: your gut, destiny, life, karma, whatever. Because believing that the dots will connect down the road will give you the confidence to follow your heart, even when it leads you off the well-worn path."
      cites: [{source: S2, locator: "first story"}]
      date: "2005"
      context: "Stanford commencement address, 12 June 2005, on dropping out of Reed."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Stanford Report's prepared text of the address, read in a Wayback Machine snapshot (20251219); web copy. Off-point for the axes; recorded as the only system-like words in his own voice."
    - text: "Don't be trapped by dogma, which is living with the results of other people's thinking. Don't let the noise of others' opinions drown out your own inner voice."
      cites: [{source: S2, locator: "third story"}]
      date: "2005"
      context: "Same address, after his account of the 2004 cancer diagnosis."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "As above."
    - text: "I'm about fifty-fifty on believing in God."
      cites: [{source: S3, locator: "closing paragraphs"}]
      date: "2011"
      context: "Told to Walter Isaacson late in life, quoted from the biography Steve Jobs (2011) by the Washington Post on its release; the paper also quotes 'different religions are different doors to the same house'."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-19
      note: "Secondary quotation of the biography (book not read); interview year not given (the Post: he talked to Isaacson 'as he was close to death'), so dated by publication. After the span (P1)."
  changes_over_life: []
  coder_notes: "Coder's call on the span: Apple II (1977) to iPhone (2007), the dated items Britannica's body calls lasting; the iPad appears only in a caption. Not a scientist (P33). His religious words are all reported through the Isaacson biography; reading the book (and the 1985 Playboy interview) is the open lead. Ruling Y1 (v8's call on the auditor's advice): stays BELOW_THRESHOLD. The words are read only as the Washington Post's quotation of Isaacson (secondary quotation, P26; V3) and fall after the span (P1). Path to AGNOS at 0.5 (interview), BELOW_THRESHOLD alternative: read the passages in the biography itself, the interviewer's own first publication of his words (P8). A stays BELOW_THRESHOLD either way (explicit suspension, §6)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated in the sources read."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1977–2007", certainty: 0.7, cites: [{source: S1, locator: "'Founding of Apple'; 'Reinventing Apple'"}], how_known: "Apple II (1977) to iPhone (2007) (P29, P30)."}
  age_at_first_lasting_contribution: {value: 22, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts; 'Founding of Apple'"}], how_known: "1977 − 1955 = 22 (P30)."}
  first_evidence_of_lio_type_views: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Nothing scored at 3 or 4."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "As above."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Only the 2005 address, which names no system."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Not assessed."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Not assessed."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Not assessed."}
  reading: "Trust in 'gut, destiny, life, karma, whatever'."
  notes: ""

institutions:
  - {value: "Atari", role: "video game designer", years: "1974", kind: employer, certainty: 0.7, cites: [{source: S1, locator: "'Founding of Apple'"}], how_known: "Britannica."}
  - {value: "Apple Computer, Inc. (Apple Inc.)", role: "cofounder; CEO from 1997", years: "1976–1985; 1997–2011", kind: employer, certainty: 0.7, cites: [{source: S1, locator: "'Founding of Apple'; 'Saving Apple'; 'Health issues'"}], how_known: "Britannica."}
  - {value: "NeXT Inc.", role: "founder", years: "1985–1997", kind: employer, certainty: 0.7, cites: [{source: S1, locator: "'NeXT and Pixar'; 'Saving Apple'"}], how_known: "Britannica."}
  - {value: "Pixar", role: "controlling owner", years: "1986–2006", kind: employer, certainty: 0.7, cites: [{source: S1, locator: "'NeXT and Pixar'"}], how_known: "Britannica."}
collaborators:
  - {value: "Steve Wozniak", relation: collaborator, note: "cofounder; designed the Apple I and II", certainty: 0.7, cites: [{source: S1, locator: "'Founding of Apple'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Provisional in v8 (F 4; four models, not Claude); roster note 'Product/design synthesis; attribution vs. team'.", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 132"}], how_known: "Study roster."}
  controversies:
    - {value: "Attribution of Apple's products to Jobs rather than his engineers", certainty: 0.5, cites: [{source: S4, locator: "roster.csv, rank 132 (note)"}, {source: S1, locator: "'Founding of Apple'"}], how_known: "Roster note; Britannica credits Wozniak with the design."}
  data_quality_flags:
    - "All words on God are secondary quotations of the 2011 biography."
  open_questions:
    - "Ruling Y1: BELOW_THRESHOLD. Open lead: read the Isaacson biography itself (P8) and the 1985 Playboy interview."
    - "Read Isaacson's Steve Jobs (2011) and the 1985 Playboy interview."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Steven Levy (Britannica)"
    citation: "Levy, Steven. \"Steve Jobs.\" Encyclopaedia Britannica (updated 29 Sep 2026). https://www.britannica.com/money/Steve-Jobs. Read live 2026-10-19."
    url: "https://www.britannica.com/money/Steve-Jobs"
    accessed: 2026-10-19
    reliability_note: "Signed article, fact-checked by the Editors; most recently revised by the Editors. Body cited; question boxes not cited (P26)."
    used_for: [identity, basics, contribution, childhood, worldview, timing, institutions, collaborators, review]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Steve Jobs"
    citation: "Jobs, Steve. Commencement address, Stanford University, 12 June 2005. Prepared text, \"'You've got to find what you love,' Jobs says\", Stanford Report. https://news.stanford.edu/stories/2005/06/youve-got-find-love-jobs-says (Wayback Machine snapshot 20251219224344)."
    url: "https://news.stanford.edu/stories/2005/06/youve-got-find-love-jobs-says"
    accessed: 2026-10-19
    reliability_note: "His prepared public text, published by the university; read in a Wayback snapshot because the live page refuses the fetch (403). Web copy."
    used_for: [childhood, worldview, lane_b]
  - id: S3
    type: secondary
    kind: other
    author: "Peter Whoriskey and Ariana Eunjung Cha"
    citation: "Whoriskey, Peter, and Ariana Eunjung Cha. \"Steve Jobs opens up about adoption, loves, faith in new biography.\" The Washington Post, 21 October 2011."
    url: "https://www.washingtonpost.com/business/economy/steve-jobs-opens-up-about-adoption-loves-faith-in-new-biography/2011/10/21/gIQAMZpu4L_story.html"
    accessed: 2026-10-19
    reliability_note: "Newspaper report quoting Isaacson's authorized biography on its release; his words here are secondary quotations."
    used_for: [childhood, worldview]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [identity, contribution, review]
---

# Steve Jobs

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Steve Jobs (1955–2011), cofounder of Apple [S1]. Draft: primary_system BELOW_THRESHOLD (AGNOS and BUDDH leads, ruling Y1); A and D BELOW_THRESHOLD; B, C, E UNKNOWN; mid_basin UNKNOWN. Not plotted.

## Life and work

Apple, NeXT, Pixar, and Apple again from 1997 [S1].

## Contribution and impact

Apple II, Macintosh, iPod, iPhone [S1].

## Childhood and education

Adopted; Reed College dropout [S1; S2].

## Adult working worldview

'Fifty-fifty on believing in God', known only through the biography [S3].

## Heritage (context only)

Not stated.

## Timing

1977–2007, from age 22 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Not assessed [S2].

## Open questions

- RQ-Y1, settled by ruling Y1 (BELOW_THRESHOLD).

## Research log

- 2026-10-19: Read Britannica (Levy), the 2005 Stanford address and the Washington Post report on the Isaacson biography.
