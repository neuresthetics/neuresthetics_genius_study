---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch N)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-17
  last_updated: 2026-10-17
  change_log:
    - {date: 2026-10-17, by: "Grok Bot", summary: "Record created (stage 3 batch N, order P32: F 4, rank 87). Basics from Britannica (Michael S.M. and Frieda Fordham, signed; body only). Worldview from the 1959 BBC 'Face to Face' interview (transcript as printed in C.G. Jung Speaking, pp. 424–439, read on a blog) and his letter to The Listener of 21 January 1960 (blog transcription): secondary transcriptions, primary check pending. primary_system BELOW_THRESHOLD (CHRIST leading candidate); A BELOW_THRESHOLD (alt 3); B UNKNOWN; mid_basin UNKNOWN (P19). Not plotted. Draft, not reviewed."}
    - {date: 2026-10-17, by: "Grok Bot", summary: "Ruling noted (v8, 2026-10-17): theories of the psyche do not count as science about physical nature for P35, so B stays UNKNOWN; open question closed."}

identity:
  id: jung-carl
  display_name: "Carl Jung"
  roster:
    canonical_name: "Carl Jung"
    rank: 87
    F: 4
    models: [Claude, DeepSeek, Gemini, GPT]
    band: "core (3–4)"
    status: core
    field: psychology
    field_bucket: "psychology / neuroscience"
  full_name: {value: "Carl Gustav Jung", certainty: 0.7, cites: [{source: S3, locator: "signature"}], how_known: "Signature of the 1960 letter as transcribed (S3); Britannica body gives 'Carl Jung'."}
  native_name: {value: "Carl Gustav Jung", certainty: 0.5, cites: [{source: S3, locator: "signature"}], how_known: "Swiss German; same spelling."}
  aliases:
    - {name: "Carl-Jung", kind: "roster alias"}
    - {name: "Jung-Carl", kind: "roster alias"}

basics:
  birth:
    date: {value: "1875-07-26", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Kesswil, Switzerland", modern_name: "Kesswil, Switzerland", polity_then: "Switzerland", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1961-06-06", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Küsnacht", modern_name: "Küsnacht, Switzerland", polity_then: "Switzerland", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1921, certainty: 0.5, cites: [{source: S1, locator: "'His first achievement was to differentiate two classes of people'"}], how_known: "Britannica calls the extravert/introvert types 'His first achievement', embodied in Psychologische Typen (1921). The term 'complex' from the Burghölzli association studies (from 1900) is called 'now famous' but is undated in the body (P13, P39). 1921 is the coder's pick; an earlier date for the complex is the alternative."}
  era_bucket: {value: "1850 to 1949", certainty: 0.5, cites: [{source: S1, locator: "types paragraph"}], how_known: "From 1921 (P2); the complex alternative gives the same bucket."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Switzerland (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Zürich, Basel, Küsnacht."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [German], certainty: 0.7, cites: [{source: S1, locator: "titles"}], how_known: "Britannica (German titles)."}
  occupations: {value: ["psychiatrist", "psychologist", "professor"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Character of his psychotherapy'"}], how_known: "Britannica."}

contribution:
  fields: {value: ["analytical psychology", "psychiatry", "psychology of religion"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Extraverted and introverted attitude types; four functions (Psychological Types)", year: 1921, kind: theory, lasting: "'His first achievement' (S1); named among the concepts he 'proposed and developed' (S1, opening)", certainty: 0.7, cites: [{source: S1, locator: "opening; types paragraph"}], how_known: "Britannica."}
    - {value: "Complex (association studies at the Burghölzli)", year: UNKNOWN, kind: "concept or term", lasting: "'the now famous term complex' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Burghölzli paragraph"}], how_known: "Britannica; undated (from 1900)."}
    - {value: "Collective unconscious and archetypes", year: UNKNOWN, kind: theory, lasting: "named in the opening among his concepts; 'much-contested' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; collective unconscious paragraph"}], how_known: "Britannica; undated."}
    - {value: "Aion: Researches into the Phenomenology of the Self", year: 1951, kind: work, lasting: "listed among his 'major individual publications' (S1)", certainty: 0.5, cites: [{source: S1, locator: "'Character of his psychotherapy', bibliography paragraph"}], how_known: "Britannica; lasting status is the coder's reading; used to close the period."}
  evidence_of_impact:
    - {value: "'His work has been influential in psychiatry and in the study of religion, literature, and related fields'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Psychology and Religion", year: 1938, kind: book, certainty: 0.7, cites: [{source: S1, locator: "bibliography paragraph"}], how_known: "Britannica."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Swiss Reformed", certainty: 0.5, cites: [{source: S2, locator: "interview, upbringing exchange"}, {source: S1, locator: "'Early life and career'"}], how_known: "(interview) 'Oh, we were Swiss Reformed' (S2); father a pastor (S1). Secondary transcription."}
  family_religious_practice: {value: "Church every Sunday", certainty: 0.5, cites: [{source: S2, locator: "interview, upbringing exchange"}], how_known: "(interview) 'Everybody went to church on Sunday.' Secondary transcription."}
  parents_and_household:
    - {value: "Father a philologist and pastor, with 'failing belief in religion'", role: father, certainty: 0.7, cites: [{source: S1, locator: "'Early life and career'"}], how_known: "Britannica."}
  household_circumstances: {value: "Clergy family; 'a number of clergymen on both sides of his family'", certainty: 0.7, cites: [{source: S1, locator: "'Early life and career'"}], how_known: "Britannica."}
  schooling:
    - {value: "University of Basel (1895–1900), Zürich (M.D., 1902)", stage: university, years: "1895–1902", certainty: 0.7, cites: [{source: S1, locator: "'Early life and career'"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading:
    - {value: "Philosophy, read widely in his teens", certainty: 0.7, cites: [{source: S1, locator: "'Early life and career'"}], how_known: "Britannica."}
  childhood_mentors: []
  languages_in_childhood: {value: [German], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "Tried to tell his father of 'his own experience of God'", year: UNKNOWN, certainty: 0.7, cites: [{source: S1, locator: "'Early life and career'"}], how_known: "Britannica."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1921–1951", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Swiss Reformed upbringing", certainty: 0.5, cites: [{source: S2, locator: "interview, upbringing exchange"}], how_known: "(interview) Context only."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not scored at this reading."}
  primary_system:
    value: BELOW_THRESHOLD
    basis: written_profession
    certainty: 0.5
    cites: [{source: S3, locator: "first and third paragraphs"}]
    rationale: "Leading candidate CHRIST: 'I think of myself as a Christian since I am entirely based upon Christian concepts', but his 'knowledge of God' is 'an unconventional way of thinking', and 'God' names 'a factor unknown in itself' met 'in my own psychical system' (1960 letter). He refuses to say that this is 'the universal, metaphysical Being of the confessions'. No study code fits without the coder's reading."
    how_known: "Published letter, read only in a blog transcription (primary check pending, P26)."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Self-description as a Christian 'based upon Christian concepts', with an unconventional God."}
    - {code: AGNOS, reason: "Declines metaphysical claims ('the impertinence of a hypostasis'), but says 'I know of God'."}
    - {code: PANENT, reason: "Only the conditional image 'a God ... just as much dwelling in myself as everywhere else'; not his stated view."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "(interview) Asked 'Do you now believe in God?' he answered 'Now? [Pause.] Difficult to answer. I know. I don't need to believe. I know' (S2). His 1960 letter says this did not mean 'I do know a certain God' but 'a factor unknown in itself, which I call \"God\"', and that he will not hypostasize it; only 'if I should venture the illegitimate hypostasis of my image' would he speak 'of a God beyond good and evil, just as much dwelling in myself as everywhere else' (S3). He declines to place God, so A is not fixed. Named alternative 3 (the conditional image)."}
    B_cause: {value: UNKNOWN, cites: [{source: S4, locator: "§5.3"}], how_known: "Nothing read on law and exception in nature. Synchronicity (with Pauli) is the lead: SEP describes synchronistic events as meaningful 'mind-matter correlations' (S4, §5.3) but gives no wording of his on exceptions. Ruling (v8, 2026-10-17, batch N): theories of the psyche (types, archetypes, the collective unconscious) are not science about physical nature for P35, so no working-science default applies and B stays UNKNOWN until a statement of his own on nature is read."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read; 'Only my experience can be good or evil' (S3) is not about reward or punishment."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "B is UNKNOWN and A BELOW_THRESHOLD (P19)."}
  statements:
    - text: "And did you believe in God? Oh, yes. Do you now believe in God? Now? [Pause.] Difficult to answer. I know. I don’t need to believe. I know."
      cites: [{source: S2, locator: "interview, upbringing exchange"}]
      date: "1959"
      context: "BBC 'Face to Face', John Freeman's interview filmed at Küsnacht in March 1959, broadcast 22 October 1959; transcript as printed in C.G. Jung Speaking (1977), pp. 424–439 (S2)."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-17
      note: "Primary check pending (P26): the film and C.G. Jung Speaking not checked. The S3 transcription has 'I needn't, I don't need to believe'."
    - text: "I did not say in the broadcast, ‘There is a God’, I said ‘I do not need to believe in God; I know’. Which does not mean: I do know a certain God (Zeus, Jahwe, Allah, the Trinitarian God, etc.) but rather: I do know that I am obviously confronted with a factor unknown in itself, which I call 'God' in consensu omnium"
      cites: [{source: S3, locator: "second paragraph"}]
      date: "1960-01-21"
      context: "Letter to The Listener, 21 January 1960, p. 133, replying to letters about the broadcast."
      axes: [A_locus]
      kind: "published letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-17
      note: "Primary check pending (P26): The Listener not read; blog transcription."
    - text: "Yet I think of myself as a Christian since I am entirely based upon Christian concepts."
      cites: [{source: S3, locator: "first paragraph"}]
      date: "1960-01-21"
      context: "Same letter."
      axes: [A_locus]
      kind: "published letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-17
      note: "Primary check pending (P26)."
  changes_over_life: []
  coder_notes: "Coder's call. Both statements are 1959–60, after the working years. Both are read in blog transcriptions (a Jung blog quoting C.G. Jung Speaking; a personal blog transcribing The Listener), so nothing here scores above BELOW_THRESHOLD. Answer to Job (1952) and Psychology and Religion (1938) are the leads for A and C."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Swiss", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Swiss Reformed (pastor's son)", certainty: 0.5, cites: [{source: S1, locator: "'Early life and career'"}, {source: S2, locator: "interview, upbringing exchange"}], how_known: "As family_religion."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1921–1951", certainty: 0.5, cites: [{source: S1, locator: "types paragraph; bibliography paragraph"}], how_known: "First to last dated listed lasting contribution (P29, P30); end is the coder's pick."}
  age_at_first_lasting_contribution: {value: 46, certainty: 0.5, cites: [{source: S1, locator: "opening; 1921"}], how_known: "1921 − 1875 = 46 (P30)."}
  first_evidence_of_lio_type_views: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "interview"}], how_known: "Only the 1959 interview and 1960 letter read."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "interview"}], how_known: "As above."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Nothing read from 1921–1951."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not read for this.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Not read."}
  circle_present: {value: "partly", rationale: "He quotes 'Deus est circulus cuius centrum est ubique' only as the image he would use if he hypostasized (S3).", certainty: 0.5, cites: [{source: S3, locator: "last paragraph"}], how_known: "Coder's reading."}
  reading: "God as a known but unplaced psychic factor."
  notes: ""

institutions:
  - {value: "Burghölzli Asylum, University of Zürich", role: "staff psychiatrist", years: "1900–", kind: employer, certainty: 0.7, cites: [{source: S1, locator: "Burghölzli paragraph"}], how_known: "Britannica."}
  - {value: "Federal Polytechnical University, Zürich (ETH)", role: "professor of psychology", years: "1933–1941", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Character of his psychotherapy'"}], how_known: "Britannica."}
  - {value: "University of Basel", role: "professor of medical psychology", years: "1943", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Character of his psychotherapy'"}], how_known: "Britannica."}
collaborators:
  - {value: "Sigmund Freud", relation: collaborator, note: "close collaborator 1907–1912; break over the sexual basis of neurosis", certainty: 0.7, cites: [{source: S1, locator: "'Association with Freud'"}], how_known: "Britannica."}
  - {value: "Eugen Bleuler", relation: "mentor or employer", note: "director of the Burghölzli", certainty: 0.7, cites: [{source: S1, locator: "Burghölzli paragraph"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 87"}], how_known: "Study roster."}
  controversies:
    - {value: "Views on the Nazi revolution 'led to his being wrongly branded as a Nazi sympathizer'", certainty: 0.7, cites: [{source: S1, locator: "'Character of his psychotherapy'"}], how_known: "Britannica's wording."}
  data_quality_flags:
    - "Worldview sources are blog transcriptions; primary check pending."
  open_questions:
    - "Settled (v8, 2026-10-17): theories of the psyche do not count as science about physical nature for P35; B stays UNKNOWN."
    - "Check the interview against the film or C.G. Jung Speaking, and the letter against The Listener (21 Jan. 1960, p. 133) or C.G. Jung Letters vol. 2."
    - "Read Synchronicity (1952) for his own wording on causality and exceptions (B)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Michael S.M. Fordham and Frieda Fordham"
    citation: "Fordham, Michael S.M., and Frieda Fordham. \"Carl Jung.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Carl-Jung. Read in Wayback snapshots: main page 20261012135306; 'Character of his psychotherapy' 20260910185927."
    url: "https://www.britannica.com/biography/Carl-Jung"
    accessed: 2026-10-17
    reliability_note: "Signed article (the Red Book paragraph is by Britannica Editors). Body only; Top Questions not cited."
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, collaborators, review]
  - id: S2
    type: secondary
    kind: other
    author: "Carl Jung Depth Psychology site (Purrington)"
    citation: "\"From C.G. Jung, C.G. Jung Speaking: The 'Face to Face' Interview.\" Carl Jung Depth Psychology, 30 October 2025, reproducing McGuire and Hull (eds.), C.G. Jung Speaking: Interviews and Encounters (Princeton, 1977), pp. 424–439. https://carljungdepthpsychologysite.blog/2025/10/30/speak-2/"
    url: "https://carljungdepthpsychologysite.blog/2025/10/30/speak-2/"
    accessed: 2026-10-17
    reliability_note: "Blog reproduction of a published transcript, read directly; matches the transcription in S3 except 'I needn't'."
    used_for: [childhood, worldview, heritage, timing]
  - id: S3
    type: secondary
    kind: other
    author: "The Uncertaintist (blog)"
    citation: "\"Carl Jung's letter to The Listener, January 21, 1960 p. 133.\" The Uncertaintist, PDF transcription. https://uncertaintist.wordpress.com/wp-content/uploads/2012/04/jung-on-god.pdf"
    url: "https://uncertaintist.wordpress.com/wp-content/uploads/2012/04/jung-on-god.pdf"
    accessed: 2026-10-17
    reliability_note: "Anonymous blog transcription of a published letter, with an interview transcript; read directly. Lower reliability; primary check pending."
    used_for: [identity, worldview, lane_b]
  - id: S4
    type: tertiary
    kind: encyclopedia
    author: "Harald Atmanspacher"
    citation: "Atmanspacher, Harald. \"Quantum Approaches to Consciousness.\" Stanford Encyclopedia of Philosophy (2024). https://plato.stanford.edu/entries/qt-consciousness/"
    url: "https://plato.stanford.edu/entries/qt-consciousness/"
    accessed: 2026-10-17
    reliability_note: "Signed SEP entry; §§5.2–5.3 (Pauli–Jung conjecture) read. Lead only."
    used_for: [worldview]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-17
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Carl Jung

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Carl Jung (1875–1961), Swiss psychiatrist, founder of analytical psychology [S1]. Draft: primary_system BELOW_THRESHOLD (CHRIST leading candidate); A BELOW_THRESHOLD (interview); B UNKNOWN; mid_basin UNKNOWN. Not plotted.

## Life and work

Burghölzli from 1900; with Freud 1907–1912; ETH 1933–41 [S1].

## Contribution and impact

Psychological types (1921), complex, collective unconscious and archetypes [S1].

## Childhood and education

Pastor's son, Swiss Reformed [S1; S2].

## Adult working worldview

'I don't need to believe. I know' (1959) [S2]; God as 'a factor unknown in itself' (1960) [S3].

## Heritage (context only)

Swiss, clergy family [S1].

## Timing

First lasting contribution 1921, at 46 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. The circle image is conditional [S3].

## Open questions

- Primary checks; Synchronicity for B (P35 does not apply: theories of the psyche are not science about physical nature).

## Research log

- 2026-10-17: Read Britannica (Fordham) in Wayback copies; the interview transcript (S2) and the Listener letter (S3) on blogs; SEP (Atmanspacher) §§5.2–5.3. IEP and SEP have no Jung entry (404). The Association of Jungian Analysts page on the broadcast did not load from the box.
