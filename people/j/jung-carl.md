---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 5
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch N; deepen D1 queue #86)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-17
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 20c_early. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-17, by: "Grok Bot", summary: "Record created (stage 3 batch N, order P32: F 4, rank 87). Basics from Britannica (Michael S.M. and Frieda Fordham, signed; body only). Worldview from the 1959 BBC 'Face to Face' interview (transcript as printed in C.G. Jung Speaking, pp. 424–439, read on a blog) and his letter to The Listener of 21 January 1960 (blog transcription): secondary transcriptions, primary check pending. primary_system BELOW_THRESHOLD (CHRIST leading candidate); A BELOW_THRESHOLD (alt 3); B UNKNOWN; mid_basin UNKNOWN (P19). Not plotted. Draft, not reviewed."}
    - {date: 2026-10-17, by: "Grok Bot", summary: "Ruling noted (v8, 2026-10-17): theories of the psyche do not count as science about physical nature for P35, so B stays UNKNOWN; open question closed."}
    - {date: 2026-10-17, by: "Grok Bot", summary: "Batch N audit (#23, RQ3): the P35 addendum states the criterion (testable, empirical claims about organisms count; interpretive theories of the psyche do not), which keeps his B UNKNOWN; Synchronicity (1952) named as the lead."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #86, F4 rank 87). Needs: re-read Face to Face / Goodrich letter / MDR for any A place/deny that clears BELOW; for B, only score if own-voice on physical nature order/exception (Synchronicity 1952). Re-read: Face to Face blog reprint of C.G. Jung Speaking (S2); Listener 21 Jan 1960 letter in two matching unofficial transcriptions (S3 Uncertaintist PDF + S9 Jung Depth Psychology blog); MDR IA djvu OCR (S7) — psyche cannot announce absolute metaphysical truths / declines hypostasis of God-claims; Henriette Goodrich letter 20 May 1940 via jungiancenter quoting Letters I (S10) — 'grace of God' / 'light within', no locus place or deny. A stays BELOW_THRESHOLD (honest: he still declines hypostasis/place; named alt 4 for the conditional immanent image). Synchronicity: An Acausal Connecting Principle (1952/1955 CW8 English, unofficial web PDF S6): natural laws are statistical truths (absolute validity shattered); causality only relatively valid; acausal connecting principle as coequal explanation — own-voice on physical nature (P16). B UNKNOWN → 2 @0.7 corroborated alt 3 (S6+S4; P48). P35 psyche-theories ruling unchanged for working-science default; B scored from own nature statement, not archetypes/types. Added Synchronicity 1952 as lasting contribution; span 1921–1952. mid_basin UNKNOWN → BELOW_THRESHOLD (A BELOW; Pavlov/James pattern). P47 source_quality on S1–S10; Wikipedia EN (S8, P50). Chart-moving NO (still not plotted: A BELOW). No fallacy_catalog (Jason). Draft, not reviewed."}

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
  full_name: {value: "Carl Gustav Jung", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S8, locator: "infobox / lead"}], how_known: "Britannica body; Wikipedia 'Karl Gustav Jung' / Carl Gustav Jung (P50 dual-bio)."}
  native_name: {value: "Carl Gustav Jung", certainty: 0.5, cites: [{source: S8, locator: "infobox Born"}], how_known: "Swiss German; Wikipedia gives birth form 'Karl Gustav Jung'."}
  aliases:
    - {name: "Carl-Jung", kind: "roster alias"}
    - {name: "Jung-Carl", kind: "roster alias"}
    - {name: "C. G. Jung", kind: "other"}

basics:
  birth:
    date: {value: "1875-07-26", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S8, locator: "infobox"}], how_known: "Britannica; Wikipedia (P50)."}
    place: {value: "Kesswil, Switzerland", modern_name: "Kesswil, Switzerland", polity_then: "Switzerland", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S8, locator: "infobox"}], how_known: "Britannica; Wikipedia."}
  death:
    date: {value: "1961-06-06", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S8, locator: "infobox"}], how_known: "Britannica; Wikipedia."}
    place: {value: "Küsnacht", modern_name: "Küsnacht, Switzerland", polity_then: "Switzerland", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S8, locator: "infobox"}], how_known: "Britannica; Wikipedia."}
  first_lasting_contribution_year: {value: 1921, certainty: 0.5, cites: [{source: S1, locator: "'His first achievement was to differentiate two classes of people'"}], how_known: "Britannica calls the extravert/introvert types 'His first achievement', embodied in Psychologische Typen (1921). The term 'complex' from the Burghölzli association studies (from 1900) is called 'now famous' but is undated in the body (P13, P39). 1921 is the coder's pick; an earlier date for the complex is the alternative."}
  era_bucket: {value: "1850 to 1949", certainty: 0.5, cites: [{source: S1, locator: "types paragraph"}], how_known: "From 1921 (P2); the complex alternative gives the same bucket."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Switzerland (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Zürich, Basel, Küsnacht."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [German], certainty: 0.7, cites: [{source: S1, locator: "titles"}], how_known: "Britannica (German titles)."}
  occupations: {value: ["psychiatrist", "psychologist", "professor"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Character of his psychotherapy'"}], how_known: "Britannica."}

contribution:
  era_bucket: 20c_early
  fields: {value: ["analytical psychology", "psychiatry", "psychology of religion"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Extraverted and introverted attitude types; four functions (Psychological Types)", year: 1921, kind: theory, lasting: "'His first achievement' (S1); named among the concepts he 'proposed and developed' (S1, opening)", certainty: 0.7, cites: [{source: S1, locator: "opening; types paragraph"}], how_known: "Britannica."}
    - {value: "Complex (association studies at the Burghölzli)", year: UNKNOWN, kind: "concept or term", lasting: "'the now famous term complex' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Burghölzli paragraph"}], how_known: "Britannica; undated (from 1900)."}
    - {value: "Collective unconscious and archetypes", year: UNKNOWN, kind: theory, lasting: "named in the opening among his concepts; 'much-contested' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; collective unconscious paragraph"}], how_known: "Britannica; undated."}
    - {value: "Aion: Researches into the Phenomenology of the Self", year: 1951, kind: work, lasting: "listed among his 'major individual publications' (S1)", certainty: 0.5, cites: [{source: S1, locator: "'Character of his psychotherapy', bibliography paragraph"}], how_known: "Britannica; lasting status is the coder's reading."}
    - {value: "Synchronicity: An Acausal Connecting Principle", year: 1952, kind: theory, lasting: "Major monograph (Naturerklärung und Psyche / CW8); Wikipedia lists Synchronicity among known-for concepts (S8); own-voice account of nature used for B (S6)", certainty: 0.7, cites: [{source: S6, locator: "title / Exposition §§818–823"}, {source: S8, locator: "infobox Known for"}], how_known: "Own 1952 monograph (English 1955); deepens D1 added to close B from own-voice nature statement."}
  evidence_of_impact:
    - {value: "'His work has been influential in psychiatry and in the study of religion, literature, and related fields'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Psychology and Religion", year: 1938, kind: book, certainty: 0.7, cites: [{source: S1, locator: "bibliography paragraph"}], how_known: "Britannica."}
    - {value: "Synchronicity: An Acausal Connecting Principle", year: 1952, kind: book, certainty: 0.7, cites: [{source: S6, locator: "title page / foreword note"}], how_known: "Own monograph (S6)."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Swiss Reformed", certainty: 0.5, cites: [{source: S2, locator: "interview, upbringing exchange"}, {source: S1, locator: "'Early life and career'"}, {source: S8, locator: "Early life / Paul Jung"}], how_known: "(interview) 'Oh, we were Swiss Reformed' (S2); father a rural pastor in the Swiss Reformed Church (S1; S8)."}
  family_religious_practice: {value: "Church every Sunday", certainty: 0.5, cites: [{source: S2, locator: "interview, upbringing exchange"}], how_known: "(interview) 'Everybody went to church on Sunday.'"}
  parents_and_household:
    - {value: "Father Paul Achilles Jung, philologist and pastor of the Swiss Reformed Church, with 'failing belief in religion'", role: father, certainty: 0.7, cites: [{source: S1, locator: "'Early life and career'"}, {source: S8, locator: "Early life"}], how_known: "Britannica; Wikipedia (P50)."}
    - {value: "Mother Emilie Jung (née Preiswerk)", role: mother, certainty: 0.7, cites: [{source: S8, locator: "Early life"}], how_known: "Wikipedia (P50)."}
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
  working_years: {value: "1921–1952", certainty: 0.5, cites: [{source: S1, locator: "text"}, {source: S6, locator: "1952 monograph"}], how_known: "Equals timing.major_work_period (extended D1 to include Synchronicity 1952)."}
  nominal_affiliations:
    - {value: "Swiss Reformed upbringing", certainty: 0.5, cites: [{source: S2, locator: "interview, upbringing exchange"}], how_known: "(interview) Context only."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not scored at this reading."}
  primary_system:
    value: BELOW_THRESHOLD
    basis: written_profession
    certainty: 0.5
    cites: [{source: S3, locator: "first and third paragraphs"}, {source: S9, locator: "full letter text"}]
    rationale: "Leading candidate CHRIST: 'I think of myself as a Christian since I am entirely based upon Christian concepts', but his 'knowledge of God' is 'an unconventional way of thinking', and 'God' names 'a factor unknown in itself' met 'in my own psychical system' (1960 letter, S3/S9). He refuses to say that this is 'the universal, metaphysical Being of the confessions'. No study code fits without the coder's reading."
    how_known: "Published letter (Listener 21 Jan 1960), read in two matching unofficial web transcriptions (S3, S9); primary page images of The Listener still pending (P26)."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Self-description as a Christian 'based upon Christian concepts', with an unconventional God."}
    - {code: AGNOS, reason: "Declines metaphysical claims ('the impertinence of a hypostasis'), but says 'I know of God'."}
    - {code: PANENT, reason: "Only the conditional image 'a God ... just as much dwelling in myself as everywhere else'; not his stated view."}
  lio_axes:
    A_locus:
      value: BELOW_THRESHOLD
      cites: [{source: S2, locator: "interview, upbringing exchange"}, {source: S3, locator: "second and last paragraphs"}, {source: S9, locator: "full letter"}, {source: S7, locator: "Late Thoughts / psyche cannot announce absolute truths"}, {source: S10, locator: "Letter to Henriette Goodrich, 20 May 1940"}]
      how_known: "Deepen D1 re-read. Face to Face (1959): 'Do you now believe in God?' — 'Now? [Pause.] Difficult to answer. I know. I don't need to believe. I know' (S2). Listener letter (1960): this did not mean 'I do know a certain God' but 'a factor unknown in itself, which I call \"God\"'; he will not commit 'the impertinence of a hypostasis'; only 'if I should venture the illegitimate hypostasis of my image' would he speak 'of a God beyond good and evil, just as much dwelling in myself as everywhere else' (S3/S9). MDR (S7): the psyche 'cannot announce absolute truths' such as 'God is One' / 'God is All'; science is convinced a transcendental object exists but he will not over-claim. Goodrich letter 20 May 1940 (S10): 'grace of God' / 'nothing can put out the light within' — wartime counsel, no place or deny of locus. He still declines to place God, so A is not fixed (keep honest). Named alternative 4: the conditional immanent image if the hypostasis were ventured."
      note: "Named alternative 4 (conditional 'dwelling in myself as everywhere else'). Alt 3 (psychic factor only, neither transcendent nor world-identical) also live. No reading clears 0.5 without overclaiming past his refusal of hypostasis."
    B_cause:
      value: 2
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S6, locator: "Exposition §§818–823; §855–856; Conclusion §948"}, {source: S4, locator: "§5.3"}]
      rationale: "Account of physical nature (P6, P16) — not psyche-types/archetypes (P35 addendum still bars those as working-science default). Synchronicity 1952 (own monograph): modern physics has 'shattered the absolute validity of natural law and made it relative'; 'Natural laws are statistical truths'; causality is 'only statistically valid and only relatively true', so 'the connection of events may in certain circumstances be other than causal, and requires another principle of explanation' (S6 §§818–819). He maintains synchronicity as 'exactly the same category of events' whose interconnection 'must necessarily be thought of as acausal' (§855); Conclusion names 'causeless order, or rather, of meaningful orderedness' (§948). Lawfulness that covers only part of nature / exceptions (acausal meaningful coincidences) as a live, recurring explanatory category → B 2 (P27 B-2 anchor; Augustine/Pascal precedent for live exceptions, here framed as natural acausality not Church miracle). Named alternative 3: if statistical natural law is read as the general order and synchronicity as a stated, limited exception on top of LIO. SEP (S4 §5.3) corroborates the mind-matter / acausal reading. P35 scientist-of-behaviour default does not apply (interpretive psyche theories); score is from the nature statement itself."
      how_known: "Own published 1952 monograph (English Bollingen/CW text in unofficial web PDF, S6), at end of extended working years; SEP scholarly corroboration (S4). Named alternative → 0.7 ceiling. Independent source ids S6+S4 → corroborated (P48)."
      alternatives:
        - {value: 3, note: "If statistical natural law is the general order and synchronicity is only a limited stated exception (B 3 lean-LIO), rather than causality covering only part of nature.", cites: [{source: S6, locator: "§§818–819"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read that scores reward/punishment; 'Only my experience can be good or evil' (S3) is not a ledger claim (P19)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read that scores revelation vs observation as authority (P19)."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read on same rules for every kind of being / hidden in-group exceptions (P7, P19)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied (Pavlov/James pattern). B is now scored (2 @0.7) but cannot alone decide mid_basin."}
  statements:
    - text: "And did you believe in God? Oh, yes. Do you now believe in God? Now? [Pause.] Difficult to answer. I know. I don’t need to believe. I know."
      cites: [{source: S2, locator: "interview, upbringing exchange"}]
      date: "1959"
      context: "BBC 'Face to Face', John Freeman's interview filmed at Küsnacht in March 1959, broadcast 22 October 1959; transcript as printed in C.G. Jung Speaking (1977), pp. 424–439 (S2)."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Deepen D1 re-read on the Jung Depth Psychology blog reprint. Film / Princeton volume page images still unchecked (P26). The S3/S9 Listener letter has 'I needn't, I don't need to believe'."
    - text: "I did not say in the broadcast, ‘There is a God’, I said ‘I do not need to believe in God; I know’. Which does not mean: I do know a certain God (Zeus, Jahwe, Allah, the Trinitarian God, etc.) but rather: I do know that I am obviously confronted with a factor unknown in itself, which I call 'God' in consensu omnium"
      cites: [{source: S3, locator: "second paragraph"}, {source: S9, locator: "full letter"}]
      date: "1960-01-21"
      context: "Letter to The Listener, 21 January 1960, p. 133, replying to letters about the broadcast. Two matching unofficial transcriptions (S3, S9)."
      axes: [A_locus]
      kind: "published letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Primary check pending (P26): The Listener page images not read. Dual web transcriptions agree."
    - text: "Yet I think of myself as a Christian since I am entirely based upon Christian concepts."
      cites: [{source: S3, locator: "first paragraph"}, {source: S9, locator: "full letter"}]
      date: "1960-01-21"
      context: "Same letter."
      axes: [A_locus]
      kind: "published letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Primary check pending (P26)."
    - text: "I do neither commit the impertinence of a hypostasis, nor of an arrogant qualification such as: 'God can only be good'. ... if I should venture the illegitimate hypostasis of my image, I would say, of a God beyond good and evil, just as much dwelling in myself as everywhere else"
      cites: [{source: S3, locator: "last paragraph"}, {source: S9, locator: "full letter"}]
      date: "1960-01-21"
      context: "Same letter — the refusal of hypostasis and the conditional immanent image (A named alt 4)."
      axes: [A_locus]
      kind: "published letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Basis of keeping A at BELOW_THRESHOLD."
    - text: "The discoveries of modern physics have, as we know, brought about a significant change in our scientific picture of the world, in that they have shattered the absolute validity of natural law and made it relative. Natural laws are statistical truths, which means that they are completely valid only when we are dealing with macrophysical quantities. ... the causal principle is only of relative use for explaining natural processes and therefore presupposes the existence of one or more other factors which would be necessary for an explanation. This is as much as to say that the connection of events may in certain circumstances be other than causal, and requires another principle of explanation."
      cites: [{source: S6, locator: "Exposition §§818–819"}]
      date: "1952"
      context: "Synchronicity: An Acausal Connecting Principle (CW8 English; first German 1952 with Pauli)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Unofficial web PDF of the CW English text (S6); IA Pantheon 1955 volume also exists."
    - text: "An unexpected content which is directly or indirectly connected with some objective external event coincides with the ordinary psychic state: this is what I call synchronicity, and I maintain that we are dealing with exactly the same category of events whether their objectivity appears separated from my consciousness in space or in time. ... synchronistic phenomena cannot in principle be associated with any conceptions of causality. Hence the interconnection of meaningfully coincident factors must necessarily be thought of as acausal."
      cites: [{source: S6, locator: "§855"}]
      date: "1952"
      context: "Same monograph, Exposition."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "As S6."
    - text: "Above all it is the fact of causeless order, or rather, of meaningful orderedness, that may throw light on psychophysical parallelism."
      cites: [{source: S6, locator: "Conclusion §948"}]
      date: "1952"
      context: "Same monograph, Conclusion."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "As S6."
  changes_over_life: []
  coder_notes: "Deepen D1: A kept BELOW_THRESHOLD on purpose — he declines hypostasis/place even after Face to Face, Listener letter (dual transcription), MDR, and Goodrich check. B lifted from UNKNOWN via Synchronicity own-voice on physical nature (P16), not via archetypes/types (P35). Named B alt 3. Answer to Job (1952) and Psychology and Religion (1938) remain leads for C/D if a later pass wants them. Listener / Jung Speaking page images still pending."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Swiss", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Swiss Reformed (pastor's son)", certainty: 0.5, cites: [{source: S1, locator: "'Early life and career'"}, {source: S2, locator: "interview, upbringing exchange"}, {source: S8, locator: "Early life"}], how_known: "As family_religion."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1921–1952", certainty: 0.5, cites: [{source: S1, locator: "types paragraph; bibliography paragraph"}, {source: S6, locator: "1952"}], how_known: "First to last dated listed lasting contribution (P29, P30); D1 added Synchronicity 1952 after Aion 1951."}
  age_at_first_lasting_contribution: {value: 46, certainty: 0.5, cites: [{source: S1, locator: "opening; 1921"}], how_known: "1921 − 1875 = 46 (P30)."}
  first_evidence_of_lio_type_views: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S6, locator: "Exposition"}], how_known: "B 2 (acausal exceptions) is not an LIO-type view (P27; Stravinsky precedent). A stays BELOW_THRESHOLD."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S6, locator: "Exposition"}], how_known: "As above."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "primary_system still BELOW_THRESHOLD; B 2 scored from 1952 at end of span."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not read for this.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Not read."}
  circle_present: {value: "partly", rationale: "He quotes 'Deus est circulus cuius centrum est ubique' only as the image he would use if he hypostasized (S3/S9).", certainty: 0.5, cites: [{source: S3, locator: "last paragraph"}], how_known: "Coder's reading."}
  reading: "God as a known but unplaced psychic factor; nature as statistically lawful with acausal synchronicity (Lane B label only)."
  notes: ""

institutions:
  - {value: "Burghölzli Asylum, University of Zürich", role: "staff psychiatrist", years: "1900–", kind: employer, certainty: 0.7, cites: [{source: S1, locator: "Burghölzli paragraph"}], how_known: "Britannica."}
  - {value: "Federal Polytechnical University, Zürich (ETH)", role: "professor of psychology", years: "1933–1941", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Character of his psychotherapy'"}], how_known: "Britannica."}
  - {value: "University of Basel", role: "professor of medical psychology", years: "1943", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Character of his psychotherapy'"}], how_known: "Britannica."}
collaborators:
  - {value: "Sigmund Freud", relation: collaborator, note: "close collaborator 1907–1912; break over the sexual basis of neurosis", certainty: 0.7, cites: [{source: S1, locator: "'Association with Freud'"}], how_known: "Britannica."}
  - {value: "Eugen Bleuler", relation: "mentor or employer", note: "director of the Burghölzli", certainty: 0.7, cites: [{source: S1, locator: "Burghölzli paragraph"}], how_known: "Britannica."}
  - {value: "Wolfgang Pauli", relation: collaborator, note: "joint 1952 Naturerklärung und Psyche volume (Synchronicity + Pauli on Kepler)", certainty: 0.7, cites: [{source: S6, locator: "foreword note"}, {source: S4, locator: "§5.2–5.3"}], how_known: "S6; SEP."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 87"}], how_known: "Study roster."}
  controversies:
    - {value: "Views on the Nazi revolution 'led to his being wrongly branded as a Nazi sympathizer'", certainty: 0.7, cites: [{source: S1, locator: "'Character of his psychotherapy'"}], how_known: "Britannica's wording."}
  data_quality_flags:
    - "Listener letter and Face to Face still from unofficial web transcriptions of published texts (dual match on the letter); The Listener / C.G. Jung Speaking page images pending."
    - "Synchronicity read in unofficial web PDF of CW English, not Pantheon 1955 page images."
    - "MDR is Jaffé-edited / collaborative; used only to confirm decline of absolute metaphysical God-claims, not to place A."
  open_questions:
    - "Settled (v8, 2026-10-17): theories of the psyche do not count as science about physical nature for P35; B now scored from Synchronicity own-voice on nature instead."
    - "Check the interview against the film or C.G. Jung Speaking, and the letter against The Listener (21 Jan. 1960, p. 133) or C.G. Jung Letters vol. 2."
    - "Answer to Job (1952) and Psychology and Religion (1938) remain leads for C/D."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Michael S.M. Fordham and Frieda Fordham"
    citation: "Fordham, Michael S.M., and Frieda Fordham. \"Carl Jung.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Carl-Jung. Read in Wayback snapshots: main page 20261012135306; 'Character of his psychotherapy' 20260910185927. Re-checked 2026-10-24."
    url: "https://www.britannica.com/biography/Carl-Jung"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Signed article (the Red Book paragraph is by Britannica Editors). Body only; Top Questions not cited."
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, collaborators, review]
  - id: S2
    type: secondary
    kind: other
    author: "Carl Jung Depth Psychology site (Purrington); McGuire and Hull (eds.)"
    citation: "\"From C.G. Jung, C.G. Jung Speaking: The 'Face to Face' Interview.\" Carl Jung Depth Psychology, 30 October 2025, reproducing McGuire and Hull (eds.), C.G. Jung Speaking: Interviews and Encounters (Princeton, 1977), pp. 424–439. https://carljungdepthpsychologysite.blog/2025/10/30/speak-2/ Re-read 2026-10-24."
    url: "https://carljungdepthpsychologysite.blog/2025/10/30/speak-2/"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Blog reproduction of a published transcript; matches the Uncertaintist interview extract (S3) except 'I needn't'. Film / Princeton pages unchecked."
    used_for: [childhood, worldview, heritage, timing]
  - id: S3
    type: secondary
    kind: other
    author: "The Uncertaintist (blog)"
    citation: "\"Carl Jung's letter to The Listener, January 21, 1960 p. 133.\" The Uncertaintist, PDF transcription. https://uncertaintist.wordpress.com/wp-content/uploads/2012/04/jung-on-god.pdf Re-read 2026-10-24."
    url: "https://uncertaintist.wordpress.com/wp-content/uploads/2012/04/jung-on-god.pdf"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Anonymous blog transcription of a published letter, with an interview extract; text matches S9. Lower reliability; The Listener page images pending."
    used_for: [identity, worldview, lane_b]
  - id: S4
    type: tertiary
    kind: encyclopedia
    author: "Harald Atmanspacher"
    citation: "Atmanspacher, Harald. \"Quantum Approaches to Consciousness.\" Stanford Encyclopedia of Philosophy (2024). https://plato.stanford.edu/entries/qt-consciousness/ §§5.2–5.3 (Pauli–Jung conjecture / synchronicity as meaningful mind-matter correlations)."
    url: "https://plato.stanford.edu/entries/qt-consciousness/"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Signed SEP entry; used as scholarly corroboration of the B reading of Synchronicity, not as own-voice."
    used_for: [worldview, collaborators]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-17
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [identity, review]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "C. G. Jung"
    citation: "Jung, C. G. \"Synchronicity: An Acausal Connecting Principle.\" In The Structure and Dynamics of the Psyche (Collected Works vol. 8), English translation (from Synchronizität als ein Prinzip akausaler Zusammenhänge, Naturerklärung und Psyche, Zürich 1952; Pantheon/Bollingen 1955). Unofficial web PDF read 2026-10-24: https://www.rhesusnegative.net/staynegative/wp-content/uploads/2022/05/synchronicity_an_acausal_connecting_principlp-CG_Jung.pdf (CW paragraph numbers §§818ff)."
    url: "https://www.rhesusnegative.net/staynegative/wp-content/uploads/2022/05/synchronicity_an_acausal_connecting_principlp-CG_Jung.pdf"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Unofficial PDF of the CW English text with standard § numbers; content matches known Bollingen wording (Exposition opening also on IA Pantheon 1955 extracts). Not Pantheon page images."
    used_for: [contribution, worldview, timing, collaborators]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "C. G. Jung; Aniela Jaffé (recorder/editor)"
    citation: "Jung, C. G. Memories, Dreams, Reflections. Recorded and edited by Aniela Jaffé; tr. Richard and Clara Winston, revised edition. Internet Archive djvu/full text: https://archive.org/stream/MemoriesDreamsReflectionsCarlJung_201811/Memories%2C%20Dreams%2C%20Reflections%20-%20Carl%20Jung_djvu.txt Read 2026-10-24 for Late Thoughts / limits of psyche on metaphysical God-statements."
    url: "https://archive.org/stream/MemoriesDreamsReflectionsCarlJung_201811/Memories%2C%20Dreams%2C%20Reflections%20-%20Carl%20Jung_djvu.txt"
    accessed: 2026-10-24
    source_quality: "archive scan (OCR only)"
    reliability_note: "Collaborative/posthumous (Jaffé); used only to confirm decline of absolute metaphysical God-claims, not to place A. OCR text."
    used_for: [worldview]
  - id: S8
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Carl Jung.\" https://en.wikipedia.org/wiki/Carl_Jung Read 2026-10-24 (P50 dual-bio with Britannica)."
    url: "https://en.wikipedia.org/wiki/Carl_Jung"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Used for identity/parents/known-for Synchronicity and Face to Face mention; worldview scores do not rest on Wikipedia alone."
    used_for: [identity, basics, childhood, heritage, contribution]
  - id: S9
    type: secondary
    kind: other
    author: "Carl Jung Depth Psychology site (Purrington)"
    citation: "\"1. I did not say in the broadcast, ‘There is a God’.\" Carl Jung Depth Psychology, 15 May 2020 (updated), reproducing the Listener 21 January 1960 letter. https://carljungdepthpsychologysite.blog/2020/05/15/god-37/ Read 2026-10-24."
    url: "https://carljungdepthpsychologysite.blog/2020/05/15/god-37/"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Second independent unofficial transcription of the same published letter; wording matches S3. Strengthens transcription confidence; still not The Listener page images."
    used_for: [worldview]
  - id: S10
    type: secondary
    kind: other
    author: "Jungian Center for the Spiritual Sciences (quoting Letters)"
    citation: "\"Jung on Surviving Politically Perilous Times.\" Jungian Center, quoting \"Letter to Henriette Goodrich,\" 20 May 1940, in C. G. Jung Letters, vol. I, p. 282. https://jungiancenter.org/jung-on-surviving-politically-perilous-times/ Read 2026-10-24."
    url: "https://jungiancenter.org/jung-on-surviving-politically-perilous-times/"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Secondary quotation of a published letter from Letters I; checked for A place/deny — none (wartime 'grace of God' / 'light within' only). Off-point for A."
    used_for: [worldview]
---

# Carl Jung

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Carl Jung (1875–1961), Swiss psychiatrist, founder of analytical psychology [S1]. Deepen D1: primary_system BELOW_THRESHOLD (CHRIST leading); A BELOW_THRESHOLD (still declines hypostasis/place; named alt 4); B 2 @0.7 corroborated alt 3 (Synchronicity 1952); mid_basin BELOW_THRESHOLD. Not plotted.

## Life and work

Burghölzli from 1900; with Freud 1907–1912; ETH 1933–41; Pauli collaboration on the 1952 nature/psyche volume [S1; S6; S4].

## Contribution and impact

Psychological types (1921), complex, collective unconscious and archetypes [S1]; synchronicity as an acausal connecting principle (1952) [S6; S8].

## Childhood and education

Pastor's son, Swiss Reformed; parents Paul Achilles Jung and Emilie (Preiswerk) [S1; S2; S8].

## Adult working worldview

'I don't need to believe. I know' (1959) [S2]; God as 'a factor unknown in itself', hypostasis refused (1960) [S3; S9]. Natural laws statistical; causality relative; synchronicity acausal (1952) [S6].

## Heritage (context only)

Swiss, clergy family [S1].

## Timing

First lasting contribution 1921, at 46; major-work period 1921–1952 (Synchronicity added D1) [S1; S6].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. The circle image is conditional [S3; S9]. Acausal synchronicity is scored on B in Lane A from the monograph, not from archetypes.

## Open questions

- Listener / Jung Speaking page images; Answer to Job and Psychology and Religion for C/D.

## Research log

- 2026-10-17: Read Britannica (Fordham) in Wayback copies; the interview transcript (S2) and the Listener letter (S3) on blogs; SEP (Atmanspacher) §§5.2–5.3. IEP and SEP have no Jung entry (404). The Association of Jungian Analysts page on the broadcast did not load from the box.
- 2026-10-24 (D1): Re-read Face to Face (S2), Listener letter dual transcriptions (S3+S9), MDR IA OCR (S7), Goodrich 1940 via jungiancenter (S10, off-point for A). Synchronicity CW English unofficial PDF (S6) for B. Wikipedia (S8, P50). A kept BELOW; B 2 @0.7 corr alt 3; mid_basin BELOW; not plotted.
