---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch R; deepen D1 2026-10-24)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages; Ellmann 1982 PDF; Letters I IA OCR"
  collected_on: 2026-10-18
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-18, by: "Grok Bot", summary: "Record created (stage 3 batch R, order P32: F 4, rank 104). Basics from Britannica (James Stephen Atherton, signed; body pages opening, 'Ulysses' and 'Finnegans Wake', read live). Worldview from his letters to Nora Barnacle (29 August 1904) and to Stanislaus Joyce (March 1907), quoted from Ellmann's editions on the RICORSO site, the 1904 passage also in Britannica's body; private letters, secondary quotations, both before the working years (P20 cap 0.5). Not a scientist (P30). primary_system and A BELOW_THRESHOLD (rejection of Christianity and the Church; no statement on God); B UNKNOWN (P16); mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-18, by: "Grok Bot", summary: "Batch R audit fixes (gs_0454445_R run 1). The pre-span letters now cite P31 (no documented change of view between them and the span; source ceiling 0.7), not P20's post-span cap, with 0.5 kept as the coder's call for indirectness (JO4). The in-span letters on the RICORSO page (to Harriet Shaw Weaver, February 1920, 9 October 1923, January 1925, 21 May 1926) were read and are cited; none states a view of God. No value changed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #103 / F4 rank 104). Goals: hunt in-span God/existence statements; keep A honest if still no locus; B likely UNKNOWN (P16 novelist). Dual bio Wikipedia EN James Joyce (S4, P50). P47 source_quality on S1–S6. Primary check: Letters of James Joyce vol. I ed. Gilbert (Viking 1957) IA OCR (S6) — Weaver 25 Feb 1920 (purgatory joke), 9 Oct 1923 (metempsychosis/Vico), Jan 1925 (Bruno dualism for Work in Progress), 21 May 1926 ('I would not pay overmuch attention to these theories') — none states a view of God (confirms S2). Ellmann James Joyce (1982 rev.; S5 monoskop PDF): Morris L. Ernst interview 'That's for the Church to say' (secondary via Ernst The Best Is Yet 1945 p. 118); Zurich party reply to cosmological proof ('reciprocal destruction') is reported speech (cannot score alone). No clear God locus; no P16 nature-order own-voice. primary_system and A stay BELOW_THRESHOLD; B stays UNKNOWN; mid_basin UNKNOWN. Not plotted. Chart-moving NO. Draft deepen report in drafts/ (untracked). No fallacy_catalog. No figures refresh."}

identity:
  id: joyce-james
  display_name: "James Joyce"
  roster:
    canonical_name: "James Joyce"
    rank: 104
    F: 4
    models: [Claude, DeepSeek, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: literature
    field_bucket: literature
  full_name: {value: "James Augustine Aloysius Joyce", certainty: 0.7, cites: [{source: S1, locator: "header ('Also known as')"}, {source: S4, locator: "lede / note a (birth registered Augusta)"}], how_known: "Britannica header line. Wikipedia notes the birth register had Augusta by mistake; confirmation name Aloysius (P25 form note; value keeps Britannica)."}
  native_name: {value: UNKNOWN, how_known: "English; same as the display name."}
  aliases:
    - {name: "James-Joyce", kind: "roster alias"}

basics:
  birth:
    date: {value: "1882-02-02", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "infobox / Early life"}], how_known: "Britannica and Wikipedia agree (2 February 1882)."}
    place: {value: "Dublin, Ireland", modern_name: "Dublin, Ireland", polity_then: "United Kingdom of Great Britain and Ireland", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "infobox (41 Brighton Square, Rathgar)"}], how_known: "Britannica; Wikipedia adds Rathgar address; polity is the coder's."}
  death:
    date: {value: "1941-01-13", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "Death"}], how_known: "Britannica and Wikipedia agree (13 January 1941)."}
    place: {value: "Zürich, Switzerland", modern_name: "Zürich, Switzerland", polity_then: "Switzerland", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Finnegans Wake'"}, {source: S4, locator: "Death"}], how_known: "Britannica and Wikipedia."}
  first_lasting_contribution_year: {value: 1914, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Dubliners (1914), the earliest work the body names as lasting (P13, P17); three stories appeared earlier in The Irish Homestead (1904) under a pseudonym (S1), but the collection is the listed work (coder's call)."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "1914 (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Ireland (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.5, cites: [{source: S1, locator: "'Early travels and works'; 'Ulysses'"}], how_known: "Zürich and Paris (Western Europe); Trieste and Pola (Southern Europe) before 1915; coder's call on the main region."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  occupations: {value: ["novelist", "short-story writer", "English teacher"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Early travels and works'"}], how_known: "Britannica (Berlitz School at Pola; private lessons in Zürich)."}

contribution:
  fields: {value: ["literature"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Dubliners (short stories)", year: 1914, kind: work, lasting: "named with his major works in the body's opening (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'A Jesuit education and a renounced faith'"}], how_known: "Britannica."}
    - {value: "A Portrait of the Artist as a Young Man", year: 1916, kind: work, lasting: "named with his major works in the body's opening (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Early travels and works'"}], how_known: "Published in book form 29 December 1916 by B. W. Huebsch (S1)."}
    - {value: "Ulysses, with the continuous stream-of-consciousness technique", year: 1922, kind: work, lasting: "'This stream-of-consciousness technique proved widely influential in much 20th-century fiction' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Ulysses'"}], how_known: "Published in Paris 2 February 1922 (S1)."}
    - {value: "Finnegans Wake", year: 1939, kind: work, lasting: "with Ulysses 'among the most groundbreaking and challenging reads in English-language literature' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Finnegans Wake'"}], how_known: "Published in its entirety in May 1939 (S1)."}
  evidence_of_impact:
    - {value: "'one of the seminal figures of Modernist literature and one of the most influential writers of the 20th century'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Roman Catholic", certainty: 0.7, cites: [{source: S1, locator: "'A Jesuit education and a renounced faith'"}], how_known: "Mother 'a devout Roman Catholic'; Jesuit schools (S1, body)."}
  family_religious_practice: {value: "Mother devout", certainty: 0.5, cites: [{source: S1, locator: "'A Jesuit education and a renounced faith'"}], how_known: "Britannica; the father's practice is not given."}
  parents_and_household:
    - {value: "Father John Stanislaus Joyce, a civil servant who drank and borrowed; mother Mary Jane ('May') Murray, a gifted singer and devout Roman Catholic; eldest of 10 surviving children", role: parents, certainty: 0.7, cites: [{source: S1, locator: "'A Jesuit education and a renounced faith'"}], how_known: "Britannica."}
  household_circumstances: {value: "Family sank into poverty", certainty: 0.7, cites: [{source: S1, locator: "'A Jesuit education and a renounced faith'"}], how_known: "Britannica."}
  schooling:
    - {value: "Clongowes Wood College (Jesuit boarding school)", stage: "grammar or secondary school", run_by: "religious body", years: "1888–1891", certainty: 0.5, cites: [{source: S1, locator: "'A Jesuit education and a renounced faith'"}], how_known: "Sent 'at age six' and 'did not return ... in 1891' (S1); start year from age six; stage the coder's reading of a boarding school taking boys from six (P21)."}
    - {value: "Belvedere College, Dublin (Jesuit grammar school)", stage: "grammar or secondary school", run_by: "religious body", years: "1893–", certainty: 0.7, cites: [{source: S1, locator: "'A Jesuit education and a renounced faith'"}], how_known: "Admitted April 1893; left 'under a cloud, as it was thought (correctly) that he had lost his Catholic faith' (S1)."}
    - {value: "University College Dublin (then staffed by Jesuits); languages", stage: university, run_by: "religious body", years: "1898–", certainty: 0.7, cites: [{source: S1, locator: "'A Jesuit education and a renounced faith'"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading:
    - {value: "Henrik Ibsen (learned Dano-Norwegian to read When We Dead Awaken)", certainty: 0.7, cites: [{source: S1, locator: "'A Jesuit education and a renounced faith'"}], how_known: "Britannica."}
  childhood_mentors: []
  languages_in_childhood: {value: ["English"], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "Lost his Catholic faith while at Belvedere College", year: UNKNOWN, certainty: 0.7, cites: [{source: S1, locator: "'A Jesuit education and a renounced faith'"}], how_known: "Britannica; adolescent, before the working years (P29)."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1914–1939", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Finnegans Wake'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read on science and religion."}
  primary_system: {value: BELOW_THRESHOLD, cites: [{source: S2, locator: "letter to Nora, 29 Aug. 1904; letter to Stanislaus, March 1907"}, {source: S1, locator: "'A Jesuit education and a renounced faith'"}, {source: S6, locator: "Weaver letters 25 Feb. 1920 (pp. 136–37); Oct. 1923 (p. 204); Jan. 1925 (pp. 224–25); 21 May 1926"}, {source: S5, locator: "Ernst interview; Zurich cosmological-proof anecdote (p. 648 n.)"}], how_known: "Letters reject Christianity and the Church but do not state a view of God (1904 Nora; 1907 Stanislaus; P31 continuity into the span). In-span Weaver letters re-checked in Letters I OCR (S6): purgatory joke (1920), Vico/Bruno as compositional tools (1923–1926) — none states a view of God. Ernst's later question 'When did you leave the Catholic Church?' got 'That's for the Church to say' (S5; hedged, no locus). Zurich reply to a cosmological proof ('reciprocal destruction') is reported speech and rejects the proof without placing God (S5). Candidates SECHUM, AGNOS, ATHE remain leads only. Too thin to score (P19). Portrait/Stephen Dedalus not used as authorial (P42)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: SECHUM, reason: "Lead: rejection of Christianity and 'religious doctrines' with no religious alternative stated (1904)."}
    - {code: AGNOS, reason: "Lead only; no statement on God read."}
    - {code: ATHE, reason: "Lead only; no denial of God read."}
    - {code: CHRIST, reason: "Rejected: he left the Church and 'make[s] open war upon it' (1904); Catholic symbolism in the works (S1) is not a profession."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, cites: [{source: S2, locator: "letters of 29 Aug. 1904 and March 1907"}, {source: S6, locator: "Weaver letters 1920–1926"}, {source: S5, locator: "Ernst 'That's for the Church to say'; Zurich reciprocal-destruction anecdote"}], how_known: "Church/doctrine rejection without a statement of where God is or whether God exists. In-span Weaver letters (S6 OCR of Gilbert Letters I) place God nowhere. Ernst interview hedges exit from the Church without a locus. Zurich cosmological-proof retort is reported speech and does not deny or locate God. Pre-span letters under P31 (no documented change; held at 0.5 for indirectness). Not enough to score (P19)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); novelist — P16 only on own-voice nature/physical-world claims. Weaver 1925–26 Bruno/Vico remarks are compositional tools ('I would not pay overmuch attention to these theories', S6), not a B score. Zurich 'reciprocal destruction' retort is reported speech against a design proof (S5), not a scorably authored nature-order claim. B not scored (P16)."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read; the rejection of 'religious doctrines' (1904) is a lead."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "B is UNKNOWN, which takes precedence (P19); A is BELOW_THRESHOLD."}
  statements:
    - text: "My mind rejects the whole present social order and Christianity - home, the recognised virtues, classes of life, and religious doctrines."
      cites: [{source: S2, locator: "letter to Nora Barnacle, 29 Aug. 1904 (Letters II, p. 48; Selected Letters, pp. 25–26)"}]
      date: "1904-08-29"
      context: "Letter to Nora Barnacle from 60 Shelbourne Road, Dublin, ten years before the working years; MS at Cornell (S2). The dash is RICORSO's rendering of Ellmann's dash."
      axes: [A_locus, D_authority]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "RICORSO transcription from Ellmann's Letters II (1966) and Selected Letters (1975); same letter also quoted at length in Ellmann biography (S5). Letters II print check still pending."
    - text: "Six years ago I left the Catholic Church, hating it most fervently. I found it impossible for me to remain in it on account of the impulses of my nature. I made secret war upon it when I was a student and declined to accept the positions it offered me. By doing this I made myself a beggar but I retained my pride. Now I make open war upon it by what I write and say and do."
      cites: [{source: S2, locator: "letter to Nora Barnacle, 29 Aug. 1904"}, {source: S1, locator: "'A Jesuit education and a renounced faith' (quoted with omissions)"}, {source: S5, locator: "1904 Nora letter quoted"}]
      date: "1904-08-29"
      context: "Same letter; Britannica's body quotes the first, third and fifth sentences; Ellmann biography also quotes it (S5)."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "As above; RICORSO's page marker '[25]' (Selected Letters pagination) removed from the quotation."
    - text: "I understand that anti-clerical history probably contains a large percentage of lies but this is not enough to drive me back howling to my gods."
      cites: [{source: S2, locator: "letter to Stanislaus Joyce, March 1907 (Letters II, pp. 217–219)"}]
      date: "1907"
      context: "Letter to Stanislaus Joyce from Rome, after the Giordano Bruno procession of 17 February 1907; RICORSO dates it '[1] March 1907' and its continuation 11 March 1907. Seven years before the working years."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "RICORSO transcription; exact day uncertain in the copy; print check pending."
    - text: "That's for the Church to say."
      cites: [{source: S5, locator: "citing Morris L. Ernst, The Best Is Yet (1945), p. 118"}, {source: S4, locator: "Religious views"}]
      context: "Reply to Morris L. Ernst's question 'When did you leave the Catholic Church?' Ellmann places it in later life (S5). Wikipedia Religious views repeats the exchange (S4). Around Ulysses legal work; working years 1914–1939. Hedged; does not place God."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Secondary via Ellmann citing Ernst's memoir; print of Ernst 1945 not opened this pass."
    - text: "What a pity that the whole thing depends upon reciprocal destruction."
      cites: [{source: S5, locator: "p. 648 n. (German: 'Schade dass alles von der gegenseitigen Zerstörung abhängt.')"}]
      context: "Ellmann reports Joyce at a Zurich party answering a priest's cosmological proof of God from the order of the stars. Zurich stays include 1915–1919 (in-span) and later visits; exact date not fixed in S5. Reported speech — cannot score an axis alone (schema kind). Rejects the design inference without stating whether God exists or where God is. Not used to score B (P16; reported speech)."
      axes: [A_locus, B_cause]
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Oral anecdote in Ellmann footnote; German wording as Ellmann gives it. Lead only."
  changes_over_life: []
  coder_notes: "Coder's call (D1). Pre-span Church-rejection letters and in-span Weaver letters (now OCR-checked in Letters I, S6) still give no God locus; Ernst hedge and Zurich reported-speech retort do not supply one. primary_system and A stay BELOW_THRESHOLD (P19); not ATHE/A 4. B stays UNKNOWN (P16; not a scientist P30). Portrait/Stephen Dedalus not scored as authorial (P42). Leads still open: Selected Letters / Letters II–III print for any missed in-span God statement; Stanislaus Dublin Diary / My Brother's Keeper for reported conversations (cannot score alone); Lernout Help My Unbelief (2010) as secondary map only."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Irish Catholic", certainty: 0.7, cites: [{source: S1, locator: "'A Jesuit education and a renounced faith'"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Roman Catholic", certainty: 0.7, cites: [{source: S1, locator: "'A Jesuit education and a renounced faith'"}], how_known: "Britannica body."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: "Jesuit schooling (Clongowes Wood, Belvedere); president of the Marian Society", certainty: 0.7, cites: [{source: S1, locator: "'A Jesuit education and a renounced faith'"}], how_known: "Britannica."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1914–1939", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Finnegans Wake'"}], how_known: "Dubliners (1914) to Finnegans Wake (1939), first to last listed lasting contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 32, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "1914 − 1882 = 32 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No axis scored at 3 or 4 (P27 anchor)."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "A BELOW_THRESHOLD; B UNKNOWN.", certainty: 0.5, cites: [{source: S2, locator: "letters of 1904 and 1907"}, {source: S6, locator: "Weaver 1920–1926"}], how_known: "Coder's reading."}
  worldview_during_major_work: {value: "Church rejected; no God locus in in-span letters read", certainty: 0.5, cites: [{source: S6, locator: "Weaver 1920–1926"}, {source: S5, locator: "Ernst interview"}], how_known: "In-span Weaver letters and hedged Ernst reply; no scored axis."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "Ulysses built on a scheme of Homeric correspondences, arts and organs per episode (S1).", certainty: 0.5, cites: [{source: S1, locator: "'Ulysses'"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'A Jesuit education and a renounced faith'"}], how_known: "Not read."}
  circle_present: {value: "unclear", rationale: "No clear God locus; Church rejected.", certainty: 0.5, cites: [{source: S2, locator: "letters"}, {source: S6, locator: "Weaver letters"}], how_known: "Coder's reading."}
  reading: "An apostate from Catholicism with no stated replacement and no scored God locus."
  notes: ""

institutions:
  - {value: "Berlitz School, Pola (Austria-Hungary)", role: "English teacher", years: "1904–1905", kind: employer, certainty: 0.5, cites: [{source: S1, locator: "'Early travels and works'"}], how_known: "Britannica; moved to Trieste in 1905 (end year the coder's reading)."}
  - {value: "Bank in Rome", role: clerk, years: "1906–1907", kind: commercial, certainty: 0.7, cites: [{source: S1, locator: "'Early travels and works'"}], how_known: "Britannica ('In 1906–07, for eight months')."}
collaborators:
  - {value: "Harriet Shaw Weaver", relation: other, note: "patron; editor of the Egoist; grants of more than £23,000 by 1930; published Portrait", certainty: 0.7, cites: [{source: S1, locator: "'Early travels and works'"}], how_known: "Britannica."}
  - {value: "Ezra Pound", relation: other, note: "invited him to Paris (1920)", certainty: 0.7, cites: [{source: S1, locator: "'Ulysses'"}], how_known: "Britannica."}
  - {value: "Nora Barnacle", relation: family, note: "partner from 1904, married 1931", certainty: 0.7, cites: [{source: S1, locator: "'A Jesuit education and a renounced faith'; 'Finnegans Wake'"}], how_known: "Britannica."}
  - {value: "Henrik Ibsen", relation: "influenced by", note: "admired; Joyce learned Dano-Norwegian to read him", certainty: 0.7, cites: [{source: S1, locator: "'A Jesuit education and a renounced faith'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 104"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Pre-span Nora/Stanislaus letters still from RICORSO web transcription (S2); Ellmann biography (S5) quotes the 1904 letter; Letters II print check pending."
    - "In-span Weaver letters verified in Letters I IA OCR (S6; archive scan OCR only)."
    - "Ernst interview and Zurich cosmological-proof reply are secondary via Ellmann (S5); Ernst 1945 memoir not opened."
    - "Full name: Wikipedia notes birth register Augusta vs Augustine (P25 form); value keeps Britannica."
  open_questions:
    - "Letters II–III / Selected Letters print for any further in-span God/existence statement."
    - "Ernst, The Best Is Yet (1945), p. 118, for primary interview wording."
    - "Any own-voice P16 nature-order claim that could score B (unlikely; not a scientist)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "James Stephen Atherton"
    citation: "Atherton, James Stephen. \"James Joyce.\" Encyclopaedia Britannica (revised 18 September 2026). https://www.britannica.com/biography/James-Joyce, with the pages 'Ulysses' and 'Finnegans Wake'. First read 2026-10-18; deepen D1 kept prior body cites (live re-fetch hit JS wall 2026-10-24)."
    url: "https://www.britannica.com/biography/James-Joyce"
    accessed: 2026-10-18
    reliability_note: "Signed article. Body and header only; the AI-generated Top Questions are not cited."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "Bruce Stewart (ed.), RICORSO"
    citation: "RICORSO. \"James Joyce: Quotations (5) - Extracts from the Letters.\" http://www.ricorso.net/rx/az-data/authors/j/Joyce_JA/quots/quots5.htm (transcribing Letters of James Joyce, vols. I–II, ed. Stuart Gilbert and Richard Ellmann, 1957/1966, and Selected Letters, ed. Richard Ellmann, Faber, 1975). Re-read 2026-10-24."
    url: "http://www.ricorso.net/rx/az-data/authors/j/Joyce_JA/quots/quots5.htm"
    accessed: 2026-10-24
    reliability_note: "Irish-literature reference site transcribing the printed letters with page references; secondary quotation for pre-span letters. In-span Weaver extracts cross-checked against Letters I OCR (S6)."
    source_quality: "unofficial web copy"
    used_for: [worldview, lane_b]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-18
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S4
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. \"James Joyce.\" Wikipedia. https://en.wikipedia.org/wiki/James_Joyce. Read live 2026-10-24 (P50 dual bio)."
    url: "https://en.wikipedia.org/wiki/James_Joyce"
    accessed: 2026-10-24
    reliability_note: "Dual-bio check against Britannica (P50). Agrees on birth 2 Feb 1882 Dublin, death 13 Jan 1941 Zurich, major works, Jesuit schooling and early break with Catholicism; Religious views section stresses complexity and quotes the Ernst exchange; birth register Augusta noted."
    source_quality: "reference entry"
    used_for: [identity, basics, worldview, review]
  - id: S5
    type: secondary
    kind: "scholarly book"
    author: "Ellmann, Richard"
    citation: "Ellmann, Richard. James Joyce. Rev. ed. Oxford University Press, 1982 (first ed. 1959). Read as PDF (monoskop.org copy) 2026-10-24: Ernst interview (early chapter; note cites Ernst, The Best Is Yet, 1945, p. 118); Zurich cosmological-proof anecdote (p. 648 n.); 1904 Nora letter quoted at length."
    url: "https://monoskop.org/images/e/ec/Ellmann_Richard_James_Joyce.pdf"
    accessed: 2026-10-24
    reliability_note: "Standard scholarly biography; reported-speech anecdotes and interview quotations are secondary for scoring. PDF page images/OCR used."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, review]
  - id: S6
    type: primary
    kind: "scholarly edition"
    author: "Joyce, James; Gilbert, Stuart (ed.)"
    citation: "Joyce, James. Letters of James Joyce. Vol. I. Ed. Stuart Gilbert. New York: Viking Press, 1957. IA OCR (in.ernet.dli.2015.225574) read 2026-10-24: Weaver 25 Feb. 1920 (purgatory / S. Aloysius), Oct. 1923 (metempsychosis / Vico), Jan. 1925 (Bruno dualism), 21 May 1926 (Vico/Bruno theories)."
    url: "https://archive.org/details/in.ernet.dli.2015.225574"
    accessed: 2026-10-24
    reliability_note: "Scholarly edition of Joyce's letters; read in archive OCR only (page images not viewed this pass)."
    source_quality: "archive scan (OCR only)"
    used_for: [worldview]
---

# James Joyce

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

James Joyce (1882–1941), Irish novelist [S1; S4]. Deepen D1: primary_system and A BELOW_THRESHOLD; B UNKNOWN (P16); mid_basin UNKNOWN. Not plotted. Chart-moving NO.

## Life and work

Dublin, Pola, Trieste, Rome, Zürich, Paris [S1].

## Contribution and impact

Dubliners (1914), Portrait (1916), Ulysses (1922), Finnegans Wake (1939) [S1].

## Childhood and education

Jesuit schools; lost his faith at Belvedere [S1].

## Adult working worldview

'Six years ago I left the Catholic Church, hating it most fervently' (1904) [S2; S1; S5]. In-span Weaver letters (1920–1926) place God nowhere [S6]. Ernst: 'That's for the Church to say' [S5; S4].

## Heritage (context only)

Irish Catholic [S1].

## Timing

1914–1939, from age 32 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No clear God locus in letters read; Church rejected [S2; S6].

## Open questions

- Letters II–III / Selected Letters print for further in-span God/existence statements.
- Ernst 1945 memoir p. 118 for interview wording.
- Any own-voice P16 nature claim for B (unlikely).

## Research log

- 2026-10-18: Read Britannica (live, three pages) and RICORSO's letters page directly.
- 2026-10-24 (D1): Wikipedia dual bio; Ellmann 1982 PDF (Ernst; Zurich anecdote; 1904 letter); Letters I Viking 1957 IA OCR for Weaver 1920–1926; RICORSO re-read. Axes unchanged.
