---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA4)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #183, F 3, rank 194). Hunt: firm AGNOS from interviews/essays near span; leave B UNKNOWN; fiction/character speech not first-person (P42); do not force plot. Near-span check: Latitud Feb 1945 'Contesta' (S8 reprint path) is literary ambition only (Redentor/Judas as destiny figures — not scored). New: Don Bell Montreal CBC interview 1968 (S5 AGNI/National Post text) — self-described agnostic 'as Spencer was', 'all things are possible', 'nothing should be affirmed, nothing denied'. Re-checked Shenker NYT 1971 (S2). Mundo Argentino 11 July 1956 '¿Cree usted en Dios?' (S6; Textos Recobrados reprint via unofficial web) — denies personal/trinitarian judge-God; affirms moral/mental purpose in the universe (DEISM/process lead, not used to recode primary). primary_system AGNOS 0.5→0.7 recorded_interview, support corroborated (S5+S2); named alts DEISM (1956) and ATHE (1978 Hildebrandt lead via S7). A stays BELOW_THRESHOLD (P20 suspension; 1956 personal-God denial = P38 A 4 @0.5 lead only — do not force plot). B UNKNOWN (not a scientist; 1956 'orden en el universo' not scored as P16). mid BELOW; not plotted. Dual bio P50; P47 source_quality S1–S8; heritage mother Catholic / English Protestant grandmother. Chart-moving NO. No fallacy_catalog. No figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "AA5 audit fix (v8's call on the auditor's advice): the 1941 alternative is now cited to the Borges Center chronology (S4), not the auditor's note."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "AA4 audit fix (v8's call on the auditor's advice): verified_against relabelled 'newspaper interview' (new P21 value); 1941 (El jardín de senderos que se bifurcan) added as an alternative first-lasting year, age 42."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA4, order P32: F 3, rank 194). Sources: Britannica, signed by Emir Rodriguez Monegal (read in full), and Israel Shenker's New York Times interview-profile (6 April 1971, read in full). Lasting work: the fantastic stories collected in Ficciones (1944), 'his best fantastic stories'; his works 'now considered classics of 20th-century literature'; span 1944, age 45. Own words, quoted by Shenker: 'Being an agnostic means all things are possible, even God, even the Holy Trinity'; he says the Lord's Prayer nightly for his mother, 'I don't know whether there's anybody at the other end of the line'. 1971, after the span (P20 cap 0.5). primary_system AGNOS 0.5 (recorded_interview), alt BELOW_THRESHOLD; A BELOW_THRESHOLD ('all things are possible, even God'); not a scientist, B UNKNOWN; mid_basin BELOW_THRESHOLD. Not plotted. Draft, not reviewed."}

identity:
  id: borges-jorge-luis
  display_name: "Jorge Luis Borges"
  roster:
    canonical_name: "Jorge Luis Borges"
    rank: 194
    F: 3
    models: [Claude, Gemini, GPT]
    band: "core (3–4)"
    status: "core"
    field: "literature"
    field_bucket: "literature"
  full_name: {value: "Jorge Luis Borges", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S7, locator: "infobox"}], how_known: "Britannica + Wikipedia EN (P50 dual bio)."}
  native_name: {value: "Jorge Luis Borges", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  aliases:
    - {name: "Borges-Jorge Luis", kind: "roster alias"}
    - {name: "Jorge-Luis-Borges", kind: "roster alias"}
    - {name: "H. Bustos Domecq", kind: "pen or art name"}
    - {name: "Jorge Francisco Isidoro Luis Borges", kind: "other"}

basics:
  birth:
    date: {value: "1899-08-24", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S7, locator: "infobox"}], how_known: "Britannica + Wikipedia EN."}
    place: {value: "Buenos Aires", modern_name: "Buenos Aires, Argentina", polity_then: "Argentina", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S7, locator: "infobox"}], how_known: "Britannica + Wikipedia EN."}
  death:
    date: {value: "1986-06-14", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S7, locator: "infobox"}], how_known: "Britannica + Wikipedia EN."}
    place: {value: "Geneva", modern_name: "Geneva, Switzerland", polity_then: "Switzerland", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S7, locator: "infobox"}], how_known: "Britannica + Wikipedia EN."}
  first_lasting_contribution_year: {value: 1944, certainty: 0.7, cites: [{source: S1, locator: "Life"}, {source: S4, locator: "1941, Books"}], how_known: "'his best fantastic stories, those later collected in Ficciones (1944, revised 1956)' (S1); dated by the collection's publication (P30 #1). Alternative 1941: El jardín de senderos que se bifurcan (Buenos Aires: Sur, 1941), 'Published at the end of December 1941, actually distributed in 1942. Later became the first half of Ficciones' (S4), age 42."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "Life"}], how_known: "1944 (P2)."}
  region_of_birth: {value: "Latin America and Caribbean", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Argentina (P3)."}
  region_of_work: {value: "Latin America and Caribbean", certainty: 0.7, cites: [{source: S1, locator: "Life"}], how_known: "Buenos Aires."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Spanish", "English"], certainty: 0.7, cites: [{source: S1, locator: "Life"}, {source: S7, locator: "lead"}], how_known: "Spanish titles; bilingual household / English from grandmother (S7)."}
  occupations: {value: ["poet", "essayist", "short-story writer", "librarian"], certainty: 0.7, cites: [{source: S1, locator: "Introduction; Life"}, {source: S7, locator: "infobox"}], how_known: "Britannica + Wikipedia."}

contribution:
  fields: {value: ["literature"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Ficciones (fantastic stories)", year: 1944, kind: "work", lasting: "'his collections of poems and stories are now considered classics of 20th-century literature'; his 'best fantastic stories' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Life; Legacy"}], how_known: "Britannica; published 1944."}
  evidence_of_impact:
    - {value: "Formentor Prize (1961, with Beckett); 'Latin American literature emerged from the academic realm into the realm of generally educated readers'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Legacy"}], how_known: "Britannica."}
  major_works:
    - {value: "Otras inquisiciones", year: 1952, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "Life"}], how_known: "Britannica."}
    - {value: "El Aleph", year: 1949, kind: "book", certainty: 0.7, cites: [{source: S7, locator: "Notable works"}], how_known: "Wikipedia; collection after Ficciones."}
    - {value: "El libro de arena", year: 1975, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "Life"}], how_known: "Britannica."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Classics of 20th-century world literature (S1).", certainty: 0.7, cites: [{source: S1, locator: "Legacy"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "mother devout Catholic; English Protestant grandmother (Bible / Protestant line); father freethinking / not scored as household creed", certainty: 0.5, cites: [{source: S2, locator: "Lord's Prayer for mother"}, {source: S7, locator: "Religion; Death"}], how_known: "Wikipedia Religion + Shenker (mother's request); grandmother Protestant (S7). Father's stance not primary-quoted this pass."}
  family_religious_practice: {value: "nightly Lord's Prayer (and Hail Mary per Wikipedia) at mother's request — practice, not his belief (S2, S7)", certainty: 0.7, cites: [{source: S2, locator: "Lord's Prayer"}, {source: S7, locator: "Religion"}], how_known: "Own words in Shenker; Wikipedia."}
  parents_and_household:
    - {value: "Father Jorge Guillermo Borges, 'a man of wide-ranging intellect who taught at an English school'; family with British ancestry", role: "father", certainty: 0.7, cites: [{source: S1, locator: "Life"}, {source: S7, locator: "infobox"}], how_known: "Britannica + Wikipedia."}
    - {value: "Mother Leonor Acevedo Suárez, devout Catholic", role: "mother", certainty: 0.7, cites: [{source: S7, locator: "Religion; infobox"}, {source: S2, locator: "mother"}], how_known: "Wikipedia + Shenker."}
  household_circumstances: {value: "Buenos Aires; Europe (Switzerland/Spain) from 1914 during WWI; returned Argentina 1921", certainty: 0.7, cites: [{source: S1, locator: "Life"}, {source: S7, locator: "Early life"}], how_known: "Britannica + Wikipedia."}
  schooling:
    - {value: "Collège de Genève (B.A.)", stage: "university", run_by: other, certainty: 0.7, cites: [{source: S1, locator: "Life"}, {source: S7, locator: "Early life"}], how_known: "Britannica + Wikipedia."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated in sources read."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading:
    - {value: "Father's English library; Bible taught by English Protestant grandmother", certainty: 0.5, cites: [{source: S7, locator: "Early life; Religion"}], how_known: "Wikipedia."}
  childhood_mentors: []
  languages_in_childhood: {value: ["Spanish", "English"], certainty: 0.7, cites: [{source: S7, locator: "Early life"}], how_known: "Wikipedia: bilingual home / English grandmother."}
  notable_events:
    - {value: "Family in Switzerland 1914–; studies at Collège de Genève; return to Argentina 1921", certainty: 0.7, cites: [{source: S1, locator: "Life"}, {source: S7, locator: "Early life"}], how_known: "Britannica + Wikipedia."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1944", certainty: 0.7, cites: [{source: S1, locator: "Life"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No scored science–religion relation statement this pass."}
  primary_system:
    value: AGNOS
    basis: recorded_interview
    certainty: 0.7
    cites: [{source: S5, locator: "supernaturalist / agnostic passage"}, {source: S2, locator: "para. 'Being an agnostic'"}]
    how_known: "(interview) Two independent recorded interviews after the span: Bell (Montreal, 1968; S5) and Shenker (NYT, 1971; S2). No sourced change of view between the 1944 span and these AGNOS self-descriptions that would trigger a P31 retrospective cap (P31). Ceiling 0.7 for recorded_interview; Bell + Shenker agree (corroborated evidence noted in rationale)."
    rationale: "Self-described agnostic: 'I am, as Spencer was, an agnostic. I don't think we're capable of knowledge, but I like to keep an open mind... all things are possible... nothing should be affirmed, nothing denied' (S5); 'Being an agnostic means all things are possible, even God, even the Holy Trinity' (S2). Named alternative DEISM: 1956 Mundo Argentino survey denies a personal judge-God but affirms a moral/mental purpose in the universe and a God 'toward which the universe tends' (S6) — process/moral-purpose reading, not chosen as primary. Named alternative ATHE: Wikipedia cites 1978 Hildebrandt 'certain that God does not exist' (S7) — later lead only, not used to recode. No in-span first-person profession found (1945 Latitud literary only per S8 interview list + secondary reprint; Ficciones = fiction, P42)."
  secondary_system: {value: UNKNOWN, how_known: "DEISM and ATHE kept as named alternatives on primary, not scored as secondary."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Coded at 0.7: Bell 1968 + Shenker 1971 self-description."}
    - {code: DEISM, reason: "Named alternative: 1956 Mundo Argentino moral/mental purpose / evolutionary God (S6)."}
    - {code: ATHE, reason: "Named alternative: 1978 Hildebrandt lead (S7); rejected for span coding."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "P20: agnostic suspension states no locus — 'all things are possible, even God' (S5, S2). 1956 denies a personal/trinitarian judge-God ('no creo en ese ser') while affirming cosmic moral purpose (S6): P38 A 4 at most 0.5 with BELOW as named alternative is a lead only — do not force plot; A stays BELOW_THRESHOLD. Fiction (Ficciones) not scored (P42)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30). No clear own-voice P16 nature-order / law-and-exception statement. 1956 'orden en el universo, un sistema de periodicidades' (S6) is a cosmic-order remark tied to moral purpose / God, not scored as B. Do not force B from fiction cosmology (Tlön, Aleph) — P42."}
    C_ledger: {value: UNKNOWN, how_known: "Lead: fear of immortality of the soul (S2); 1956 rejects personal immortality (S6) — not scored."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied."}
  statements:
    - text: "Being an agnostic means all things are possible, even God, even the Holy Trinity. This world is so strange that anything may happen, or may not happen. Being an agnostic makes me live in a larger, a more fantastic kind of world, almost uncanny. It makes me more tolerant."
      cites: [{source: S2, locator: "para. 'Being an agnostic'"}]
      date: "1971"
      context: "Interview-profile by Israel Shenker, New York Times, 6 April 1971; after the span."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "newspaper interview"
      verified_on: 2026-10-24
      note: "Shenker's own interview (first-hand, P8); re-checked D1 in NYT archive copy."
    - text: "as to the question of an afterlife and immortality, living in other bodies or other minds, I am, as Spencer was, an agnostic. I don't think we're capable of knowledge, but I like to keep an open mind. So if you ask me whether I believe in an afterlife or not, whether I believe in God or not, I can only answer you that all things are possible. And if all things are possible, heaven and hell and the angels are also possible. They're not to be ruled out. ... all things are possible, so that nothing should be affirmed, nothing denied."
      cites: [{source: S5, locator: "supernaturalist / agnostic passage"}]
      date: "1968"
      context: "Don Bell interview, Montreal (CBC Tuesday Night), during Harvard year; published National Post 1999 / AGNI 52."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "newspaper interview"
      verified_on: 2026-10-24
      note: "Independent of Shenker; corroborates AGNOS (P48)."
    - text: "Si por Dios se entiende una personalidad unitaria o trinitaria, una especie de hombre sobrenatural, un juez de nuestros actos y pensamientos, no creo en ese ser. En cambio, si por Dios entendemos un propósito moral o mental en el universo, creo ciertamente en Él. ... Que hay un orden en el universo, un sistema de periodicidades y una evolución general, me parece evidente. ... No sé si Dios está en el principio del proceso cósmico, pero posiblemente está en el fin. Dios es tal vez algo hacia lo cual tiende el universo."
      cites: [{source: S6, locator: "¿Cree usted en Dios?"}]
      date: "1956"
      context: "Mundo Argentino survey, 11 July 1956; after the 1944 span. DEISM/process lead — not used to recode primary or force A."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Textos Recobrados 1956–1986 reprint via borgestodoelanio.blogspot.com (unofficial). Denies personal God; affirms moral purpose."
    - text: "Long ago, he promised his mother to say the Lord's Prayer every night. \"And ever since then I always say it. I don't know whether there's anybody at the other end of the line.\""
      cites: [{source: S2, locator: "Lord's Prayer"}]
      date: "1971"
      context: "Shenker NYT; practice for mother, not belief profession."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "newspaper interview"
      verified_on: 2026-10-24
      note: "Heritage/practice context; supports suspension, not CHRIST."
  changes_over_life:
    - {value: "1956 Mundo Argentino: denies personal/trinitarian judge-God; affirms moral/mental purpose in the universe and a God possibly at the end of cosmic process (DEISM/process lead). 1968–1971 interviews: explicit self-description as agnostic — all things possible, nothing affirmed/denied. 1978 Hildebrandt (per Wikipedia): stated certainty that God does not exist (ATHE lead). Deathbed 1986: Catholic priest and Protestant pastor at his request (heritage/memory of mother and grandmother — not a worldview recode). Spans after 1944; AGNOS kept for working years under P31 from consistent 1968–71 self-label; 1956 and 1978 noted as alternatives/leads.", year: 1956, certainty: 0.5, cites: [{source: S6, locator: "¿Cree usted en Dios?"}, {source: S5, locator: "agnostic"}, {source: S2, locator: "Being an agnostic"}, {source: S7, locator: "Religion"}], how_known: "Primary survey text (S6 unofficial reprint); interviews S5/S2; Wikipedia for 1978/deathbed (S7)."}
  coder_notes: "No in-span (1944) first-person God profession found. Latitud 1945 literary only. Do not score Ficciones/Aleph character or metafictional theology (P42). Burgin Conversations (1967–69) not opened first-hand this pass (IA borrow wall). Historia de la eternidad (1936) not opened. No fallacy_catalog; figures/ untouched."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Argentine with Spanish, Portuguese, and English ancestry", certainty: 0.5, cites: [{source: S5, locator: "roots"}, {source: S7, locator: "Early life"}], how_known: "Own words in Bell; Wikipedia."}
  religious_heritage_by_birth: {value: "Catholic mother; English Protestant grandmother; not a childhood creed for him", certainty: 0.5, cites: [{source: S7, locator: "Religion"}, {source: S2, locator: "mother"}], how_known: "Wikipedia + Shenker. Heritage only."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated in sources read."}
  childhood_catechism: {value: UNKNOWN, how_known: "Bible reading with Protestant grandmother noted (S7); not a catechism score."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1944", certainty: 0.7, cites: [{source: S1, locator: "Life"}], how_known: "The one listed lasting work, dated by publication (P29, P30 #1)."}
  age_at_first_lasting_contribution: {value: 45, certainty: 0.7, cites: [{source: S1, locator: "Introduction; Life"}], how_known: "1944 − 1899 = 45 (P30 year difference); 42 on the 1941 alternative."}
  first_evidence_of_lio_type_views: {value: "1956 (Mundo Argentino God survey); clearer AGNOS self-label 1968 (Bell)", certainty: 0.7, cites: [{source: S6, locator: "¿Cree usted en Dios?"}, {source: S5, locator: "agnostic"}, {source: S8, locator: "1956 ¿Cree usted en Dios?; 1945 Latitud"}], how_known: "After the 1944 span; near-span interview survey via Borges Center list (S8); Latitud 1945 literary only."}
  lio_views_relative_to_major_work: {value: "after major work", certainty: 0.7, cites: [{source: S6, locator: "1956"}, {source: S5, locator: "1968"}, {source: S2, locator: "1971"}], how_known: "All scored professions after 1944."}
  worldview_during_major_work: {value: "AGNOS (inferred for span under P31 from later consistent self-description; no in-span first-person found)", certainty: 0.5, cites: [{source: S5, locator: "1968"}, {source: S2, locator: "1971"}], how_known: "P31: no change documented between 1944 and the 1968–71 AGNOS interviews that would force a retrospective-only reading; certainty kept moderate because evidence is after span."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Fiction and essay (S1); labyrinths/mirrors are literary motifs, not scored geometric form.", certainty: 0.5, cites: [{source: S1, locator: "Life"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No chart-moving A/B change. Do not derive B from ficciones cosmology."
  notes: "P42: character speech and metafiction out."

institutions:
  - {value: "National Library of Argentina", role: "director", years: "1955", kind: "government or state body", certainty: 0.5, cites: [{source: S1, locator: "Life"}, {source: S7, locator: "career"}], how_known: "Britannica: from 1955; end year not settled this pass."}
collaborators:
  - {value: "Adolfo Bioy Casares", relation: "collaborator", note: "co-wrote as H. Bustos Domecq", certainty: 0.7, cites: [{source: S1, locator: "Life"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 194"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "No in-span first-person God profession; AGNOS firmed from 1968+1971 interviews under P31."
    - "1956 survey is unofficial web reprint of Textos Recobrados (S6)."
    - "1978 atheist line and deathbed clergy are Wikipedia-mediated leads (S7)."
  open_questions:
    - "Burgin Conversations (1967–69) first-hand for God passages."
    - "Historia de la eternidad (1936) / Otras inquisiciones essays for near-span written profession."
    - "Hildebrandt 1978 primary text for ATHE lead."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Emir Rodriguez Monegal"
    citation: "Rodriguez Monegal, Emir. 'Jorge Luis Borges.' Encyclopaedia Britannica. https://www.britannica.com/biography/Jorge-Luis-Borges"
    url: "https://www.britannica.com/biography/Jorge-Luis-Borges"
    accessed: 2026-10-19
    reliability_note: "Signed article, read in full at create; bio reused D1."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, timing, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "other"
    author: "Israel Shenker"
    citation: "Shenker, Israel. 'Borges, a Blind Writer With Insight.' The New York Times, 6 April 1971. https://archive.nytimes.com/www.nytimes.com/books/97/08/31/reviews/borges-insight.html"
    url: "https://archive.nytimes.com/www.nytimes.com/books/97/08/31/reviews/borges-insight.html"
    accessed: 2026-10-24
    reliability_note: "Newspaper interview-profile quoting him, re-read in full D1."
    source_quality: "newspaper interview"
    used_for: [worldview, heritage, childhood]
  - id: S3
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [review]
  - id: S4
    type: secondary
    kind: "database"
    author: "Borges Center, University of Pittsburgh"
    citation: "Borges Center. '1941.' Bibliography and chronology, University of Pittsburgh. https://www.borges.pitt.edu/bibliography/1941-1"
    url: "https://www.borges.pitt.edu/bibliography/1941-1"
    accessed: 2026-10-19
    reliability_note: "Scholarly bibliographic chronology, page read in full."
    source_quality: "scholarly edition or monograph"
    used_for: [basics]
  - id: S5
    type: secondary
    kind: "other"
    author: "Don Bell"
    citation: "Bell, Don. 'A Master in Montreal: A 1968 Interview with Jorge Luis Borges.' National Post, 24 August 1999; rpt. AGNI 52 (2000). https://agnionline.bu.edu/conversation/a-master-in-montreal-a-1968-interview-with-jorge-luis-borges/"
    url: "https://agnionline.bu.edu/conversation/a-master-in-montreal-a-1968-interview-with-jorge-luis-borges/"
    accessed: 2026-10-24
    reliability_note: "CBC radio interview transcript (1968); AGNI republication read in full D1. Independent of Shenker."
    source_quality: "newspaper interview"
    used_for: [worldview, childhood, heritage]
  - id: S6
    type: primary
    kind: "other"
    author: "Jorge Luis Borges"
    citation: "Borges, Jorge Luis. Answers in '¿Cree usted en Dios?' Mundo Argentino (Buenos Aires), 11 July 1956. Rpt. Textos Recobrados 1956–1986 (Emecé). Unofficial web copy: https://borgestodoelanio.blogspot.com/2017/08/jorge-luis-borges-encuestado-cree-usted.html"
    url: "https://borgestodoelanio.blogspot.com/2017/08/jorge-luis-borges-encuestado-cree-usted.html"
    accessed: 2026-10-24
    reliability_note: "Unofficial blog reprint of Textos Recobrados text; composition/publication 1956 after span. Used as DEISM/process lead, not to force A or primary."
    source_quality: "unofficial web copy"
    used_for: [worldview, timing, review]
  - id: S7
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "'Jorge Luis Borges.' Wikipedia (English). https://en.wikipedia.org/wiki/Jorge_Luis_Borges"
    url: "https://en.wikipedia.org/wiki/Jorge_Luis_Borges"
    accessed: 2026-10-24
    reliability_note: "P50 dual bio with S1. Religion section: agnostic/atheist over life; 1978 Hildebrandt; deathbed clergy — leads only where not primary-checked."
    source_quality: "reference entry"
    used_for: [identity, basics, childhood, heritage, worldview, contribution, institutions, review]
  - id: S8
    type: secondary
    kind: "database"
    author: "Borges Center, University of Pittsburgh"
    citation: "Borges Center. 'Interviews with Borges' (chronological list; Hanson annotated bibliography). https://www.borges.pitt.edu/interviews-borges"
    url: "https://www.borges.pitt.edu/interviews-borges"
    accessed: 2026-10-24
    reliability_note: "Used to locate near-span interviews (Latitud 1945 literary; Mundo Argentino 1956). Latitud full text checked via secondary reprint path (borgestodoelanio) — not scored for worldview."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, review]
---

## Summary

Jorge Luis Borges (1899–1986), writer [S1, S7]. Deepen D1: AGNOS @0.7 (Bell 1968 + Shenker 1971); A BELOW_THRESHOLD; B UNKNOWN. Not plotted.

## Life and work

Buenos Aires; Geneva [S1, S7]. National Library director from 1955.

## Contribution and impact

Ficciones (1944); El Aleph (1949) [S1, S7].

## Childhood and education

Bilingual home; Collège de Genève; mother Catholic, English Protestant grandmother [S1, S7].

## Adult working worldview

AGNOS @0.7 from Bell 1968 + Shenker 1971 (all things possible; nothing affirmed/denied) [S5, S2]. A BELOW_THRESHOLD. 1956 Mundo Argentino = DEISM/process lead (denies personal God; affirms cosmic moral purpose) [S6]. 1978 atheist lead [S7]. No in-span profession; Ficciones not scored (P42). B UNKNOWN.

## Heritage (context only)

Catholic mother; Protestant grandmother; Lord's Prayer for mother [S2, S7].

## Timing

1944, age 45 [S1]. LIO evidence after major work (1956+).

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No B from fiction cosmology.

## Open questions

- Burgin; Historia de la eternidad; Hildebrandt primary.

## Research log

- 2026-10-24 (D1): Bell 1968 (S5); Shenker re-check (S2); Mundo Argentino 1956 (S6); Wikipedia dual bio (S7); Borges Center interviews list (S8); Latitud 1945 literary only. AGNOS 0.5→0.7; A BELOW; B UNKNOWN. Chart-moving NO. No fallacy_catalog; no figures/.
- 2026-10-19: AA4/AA5 audit fixes; create from Britannica + NYT 1971.
