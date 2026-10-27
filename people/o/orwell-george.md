---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z9; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to literature. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #164, F 3, rank 173). Goals: first-person atheism/humanism for primary/A; open B only with real cause-order talk; do not force plot. In-span: Lear, Tolstoy and the Fool (Polemic, March 1947; orwell.ru web of CEJL reprint) — 'humanist attitude' vs Christian/next-world; 'one must choose between this world and the next'. Reflections on Gandhi (Partisan Review, Jan 1949; Orwell Foundation estate-permission text) — Man the measure / only earth we have; God-exists assumption incompatible; radicals 'have in effect chosen Man'. Before-span first person: As I Please, Tribune, 3 March 1944 (Tribune magazine archive reprint + telelib/orwell.ru) — 'I do not want the belief in life after death to return'; looks at Christian religion 'from the outside'. Such, Such Were the Joys (~1947 composition; web) — 'Till the age of about fourteen I believed in God'. Letter to Eleanor Jaques / Brenda Salkeld 1932 via Davison/Crick secondary — 'when one doesn't believe'. Notes on the Way 1940 re-checked (collective). P47 source_quality on S1–S8. P50 Wikipedia EN dual bio. CEJL/Davison Complete Works print volumes still unread (IA borrow-gated). B left UNKNOWN (P16: 'indifference to miracles' is about saints, not nature's causal order). primary_system BELOW→ATHE @0.5 (alt SECHUM); A BELOW→4 @0.5 support corroborated; C UNKNOWN→4 @0.5 support corroborated; mid stays BELOW (A only at 0.5, under P10 0.7 bar). Chart-moving NO (B UNKNOWN; still unplottable). No fallacy_catalog; no figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z10 audit fix (WEAKEN, P21; v8's call on the auditor's advice): statement label 'primary transcription' (reserved for keyed transcriptions such as TCP) -> 'unofficial web copy' (new verified_against value)."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z9 audit fixes (v8's calls on the auditor's advice). Statement label: 'secondary quotation' -> 'primary transcription' with the note that S2 is an unofficial web copy of his own text, capped at 0.7 (§7). C lead added: As I Please, 3 March 1944 (CEJL vol. 3 p. 127, web copy), 'I do not want the belief in life after death to return'. Values unchanged: BELOW_THRESHOLD."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z9, order P32: F 3, rank 173). Basics from Britannica (George Woodcock, signed). Own words: 'Notes on the Way' (Time and Tide, 1940; orwell.ru transcription of CEJL, unofficial web copy), before the span: religious belief 'had to be abandoned', 'in essence a lie'; hope for 'human brotherhood without the need for a \"next world\"'. Collective, not first-person, so primary_system BELOW_THRESHOLD (leads ATHE, SECHUM); A BELOW_THRESHOLD; B UNKNOWN (not a scientist); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Span 1945–1949, age 42. Not plotted. Draft, not reviewed."}

identity:
  id: orwell-george
  display_name: "George Orwell"
  roster:
    canonical_name: "George Orwell"
    rank: 173
    F: 3
    models: [DeepSeek, GPT, Grok]
    band: "core (3–4)"
    status: "core"
    field: "literature"
    field_bucket: "literature"
  full_name: {value: "Eric Arthur Blair", certainty: 0.7, cites: [{source: S1, locator: "Pseudonym of"}, {source: S4, locator: "lead"}], how_known: "Britannica + Wikipedia."}
  native_name: {value: "George Orwell", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica (pen name)."}
  aliases:
    - {name: "Eric Arthur Blair", kind: "birth name"}
    - {name: "George-Orwell", kind: "roster alias"}

basics:
  birth:
    date: {value: "1903-06-25", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "infobox"}], how_known: "Two sources."}
    place: {value: "Motihari, Bengal", modern_name: "Motihari, Bihar, India", polity_then: "British India", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "infobox"}], how_known: "Two sources."}
  death:
    date: {value: "1950-01-21", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "infobox"}], how_known: "Two sources."}
    place: {value: "London", modern_name: "London, United Kingdom", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "infobox"}], how_known: "Two sources."}
  first_lasting_contribution_year: {value: 1945, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Animal Farm (1945), one of his 'profoundly influential novels'."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "1945 (P2)."}
  region_of_birth: {value: "South Asia", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "India (P3; regions.csv)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "England."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "English."}
  occupations: {value: ["novelist", "essayist", "critic", "journalist"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  primary_domain: literature
  fields: {value: ["literature", "political writing"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Animal Farm", year: 1945, kind: "work", lasting: "'profoundly influential novels' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "Nineteen Eighty-four", year: 1949, kind: "work", lasting: "'profoundly influential novels'; 'solidified his reputation as an almost prophetic voice' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "An almost prophetic voice in 20th-century literature", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Homage to Catalonia", year: 1938, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "Lear, Tolstoy and the Fool", year: 1947, kind: "other", certainty: 0.7, cites: [{source: S5, locator: "Polemic, March 1947"}], how_known: "In-span essay used for worldview (not a lasting-contribution pivot)."}
    - {value: "Reflections on Gandhi", year: 1949, kind: "other", certainty: 0.7, cites: [{source: S6, locator: "Partisan Review, January 1949"}], how_known: "In-span essay used for worldview."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Profoundly influential novelist (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Anglican (Church of England household; paternal grandfather an Anglican clergyman)", certainty: 0.7, cites: [{source: S4, locator: "Early years; Religion"}, {source: S3, locator: "Joys, part V"}], how_known: "Wikipedia dual bio + own school memoir of childhood belief."}
  family_religious_practice: {value: "Church of England forms; school chapel and Prayer Book at St Cyprian's", certainty: 0.5, cites: [{source: S3, locator: "Joys, parts I–V"}], how_known: "Memoir of prep-school religion; household practice not separately documented this pass."}
  parents_and_household:
    - {value: "Father, Richard Walmesley Blair, minor official in the Indian Civil Service (Opium Department)", role: "father", certainty: 0.7, cites: [{source: S1, locator: "Early life"}, {source: S4, locator: "Early years"}], how_known: "Two sources."}
    - {value: "Mother, Ida Mabel Blair (née Limouzin)", role: "mother", certainty: 0.7, cites: [{source: S4, locator: "Early years"}], how_known: "Wikipedia."}
  household_circumstances: {value: "What he later called 'lower-upper-middle class'; reduced-fee prep school", certainty: 0.7, cites: [{source: S4, locator: "Early years"}, {source: S3, locator: "Joys, part II"}], how_known: "Own phrase + memoir."}
  schooling:
    - {value: "St Cyprian's School, Eastbourne", stage: "grammar or secondary school", years: "1911–1916", certainty: 0.7, cites: [{source: S4, locator: "Early years"}, {source: S3, locator: "Joys"}], how_known: "Two sources."}
    - {value: "Eton College", stage: "grammar or secondary school", years: "1917–1921", certainty: 0.7, cites: [{source: S1, locator: "Early life"}, {source: S4, locator: "Early years"}], how_known: "Two sources."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events:
    - {value: "Loss of childhood Christian belief around age fourteen (own retrospective)", year: 1917, certainty: 0.5, cites: [{source: S3, locator: "Joys, part V"}], how_known: "Retrospective memoir; year approximate (age ~14)."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1945–1949", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Church of England burial by request; two Anglican marriages; Richard baptised — cultural/sentimental practice, not a scored creed (own disbelief elsewhere)", certainty: 0.7, cites: [{source: S4, locator: "Religion"}, {source: S7, locator: "Davison on burial XX/237"}], how_known: "Wikipedia + Davison secondary; heritage/practice, not primary_system."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No systematic science-vs-religion essay scored this pass; 'indifference to miracles' (S8) is about saints, not a science relation."}
  primary_system:
    value: ATHE
    basis: written_profession
    certainty: 0.5
    cites: [{source: S6, locator: "Man is the measure / chosen Man"}, {source: S5, locator: "humanist attitude / this world and the next"}, {source: S3, locator: "believed in God till ~14"}, {source: S8, locator: "from the outside; life after death"}]
    rationale: "In-span essays take the no-God / this-world side: Gandhi's teaching 'make[s] sense only on the assumption that God exists', which he sets against the belief that 'Man is the measure of all things' and that radicals 'have in effect chosen Man' (S6, 1949); Lear contrasts the 'humanist attitude' with the Christian aim of escaping earthly life for Heaven (S5, 1947). Before-span first person: looks at the Christian religion 'from the outside' and does not want belief in life after death to return (S8, 1944); school memoir — believed in God only till about fourteen (S3). Named alternative SECHUM: Lear/Gandhi use 'humanist'/'humanistic' as the positive label, and Humanists UK/Walter read him as idiosyncratic humanist (S9), but he was not a public member of a humanist organisation (P15/SECHUM neighbor rule). 0.5: ATHE's philosophical-naturalism half is not stated in those words; disbelief is often framed as humanist this-world choice rather than a bald 'God does not exist'; CoE burial request is cultural practice, not a reverse creed."
    how_known: "In-span written professions (S5, S6) plus consistent adult first-person leads (S3, S8). CEJL/Complete Works print unread — Foundation estate text for Gandhi lifts the unofficial-web cap for that essay (§7); Lear and Joys remain web copies (0.7 ceiling unused because contested/indirect evidence already caps at 0.5)."
    alternatives:
      - {value: SECHUM, note: "Strongest in-span labels are 'humanist'/'humanistic' (S5, S6); Humanists UK (S9). Rejected as value because public identity was novelist/essayist, not humanist-movement membership; kept as named alt.", cites: [{source: S5, locator: "humanist attitude"}, {source: S6, locator: "humanistic / chosen Man"}, {source: S9, locator: "idiosyncratic humanism"}]}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: ATHE, reason: "No personal God in adult working years; outsider to Christianity; childhood belief ended ~14."}
    - {code: SECHUM, reason: "In-span Lear/Gandhi humanist framing; Humanists UK claim."}
    - {code: AGNOS, reason: "Rejected: own words are choice of Man/this world and non-belief, not suspension of judgement. Faulkner 'thoroughgoing agnostic' is secondary only."}
    - {code: CHRIST, reason: "Rejected: CoE burial/marriages are practice/sentiment; 1932 churchgoing was described by him as deception when he did not believe (S7)."}
  lio_axes:
    A_locus:
      value: 4
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S6, locator: "God exists assumption vs chosen Man"}, {source: S5, locator: "this world and the next; humanist attitude"}, {source: S3, locator: "believed in God till ~14"}, {source: S8, locator: "Christian religion from the outside"}]
      how_known: "Support corroborated (P48): independent in-span essays S6 (Foundation estate text) + S5 (Lear web), plus Joys S3 and As I Please S8. 0.5: no published sentence 'I do not believe in God' in those words; denial is by choosing Man over the God-exists assumption and by ending childhood belief; CoE burial is a named softener. Contested alt BELOW_THRESHOLD."
      rationale: "No transcendent personal God as locus (A 4, P38): adult essays refuse the God-exists / next-world side and place value in Man and this earth only. Named alternative BELOW_THRESHOLD: if 'chosen Man' is read as ethical priority without metaphysical denial."
      alternatives:
        - {value: BELOW_THRESHOLD, note: "If humanist this-world preference is only ethics, not a deny of God's existence.", cites: [{source: S6, locator: "chosen Man"}]}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30/P33). For a non-scientist, B needs an explicit remark on nature's causal order — laws, miracles in nature, chance vs necessity (P16). Checked and left unscored: As I Please 'indifference to miracles' (S8) concerns flying saints / Catholic wonder-claims, not a profession about the order of nature. Deliberately not scored (do not force plot)."}
    C_ledger:
      value: 4
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S8, locator: "I do not want the belief in life after death to return"}, {source: S5, locator: "death is the price of life; this world and the next"}]
      how_known: "First-person As I Please (1944, before span; adult evidence counts under P31 with no documented reverse change) + in-span Lear (1947). Support corroborated. 0.5: before-span weight on the strongest first-person line; CEJL print unread."
      rationale: "No personal afterlife ledger (C 4): he does not want belief in individual survival after death to return, and the humanist attitude takes death as the price of life rather than a gateway to reward/punishment."
    D_authority: {value: UNKNOWN, how_known: "Hostility to Catholic intellectual 'handy-pandy' with creeds (S8) is a lead for observation over revelation, not scored as a clear D profession this pass."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read on same laws everywhere (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus 4 is scored only at 0.5, under the 0.7 bar for the A ≥ 3 branch (P10). B UNKNOWN. If A reached 0.7 the result would be false."}
  statements:
    - text: "But one should, I think, realize that Gandhi's teachings cannot be squared with the belief that Man is the measure of all things, and that our job is to make life worth living on this earth, which is the only earth we have. They make sense only on the assumption that God exists and that the world of solid objects is an illusion to be escaped from."
      cites: [{source: S6, locator: "body; Partisan Review, January 1949"}]
      date: "1949-01"
      context: "'Reflections on Gandhi', within the major-work span."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Orwell Foundation site, reproduced with permission of the Orwell Estate (§7 authoritative estate/institution text). Wording also matches orwell.ru and Humanists UK quotations."
    - text: "But it is not necessary here to argue whether the other-worldly or the humanistic ideal is 'higher'. The point is that they are incompatible. One must choose between God and Man, and all 'radicals' and 'progressives', from the mildest Liberal to the most extreme Anarchist, have in effect chosen Man."
      cites: [{source: S6, locator: "body; Partisan Review, January 1949"}]
      date: "1949-01"
      context: "Same essay; identifies with the radical/progressive choice of Man."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Foundation estate text (S6)."
    - text: "Ultimately it is the Christian attitude which is self-interested and hedonistic, since the aim is always to get away from the painful struggle of earthly life and find eternal peace in some kind of Heaven or Nirvana. The humanist attitude is that the struggle must continue and that death is the price of life. … Often there is a seeming truce between the humanist and the religious believer, but in fact their attitudes cannot be reconciled: one must choose between this world and the next."
      cites: [{source: S5, locator: "Polemic, March 1947; toward end"}]
      date: "1947-03"
      context: "'Lear, Tolstoy and the Fool', within the span."
      axes: [A_locus, C_ledger]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "orwell.ru transcription of CEJL/Polemic text; CEJL print unread (0.7 cap). Wording matches Humanists UK long quotation (S9)."
    - text: "I do not want the belief in life after death to return, and in any case it is not likely to return."
      cites: [{source: S8, locator: "Tribune, 3 March 1944"}]
      date: "1944-03-03"
      context: "'As I Please', Tribune; before the span. First person. Also: looks at the Christian religion 'from the outside'."
      axes: [C_ledger, A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Tribune magazine archive reprint of the original column (S8) cross-checked against telelib/orwell.ru. CEJL vol. 3 print unread — coder_notes. Before-span; no documented reverse change before 1945–1949 (P31)."
    - text: "Till the age of about fourteen I believed in God, and believed that the accounts given of him were true. But I was well aware that I did not love him. On the contrary, I hated him, just as I hated Jesus and the Hebrew patriarchs."
      cites: [{source: S3, locator: "part V"}]
      date: "1947"
      context: "'Such, Such Were the Joys'; composition often dated ~1947 (within/near span); published Partisan Review 1952. Retrospective on childhood belief ending."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "orwell.ru web; CEJL/Davison XIX print unread. Past-tense childhood; implies adult non-belief at time of writing."
    - text: "It was absolutely necessary that the soul should be cut away. Religious belief, in the form in which we had known it, had to be abandoned. By the nineteenth century it was already in essence a lie, a semi-conscious device for keeping the rich rich and the poor poor."
      cites: [{source: S2, locator: "para. 1"}]
      date: "1940-03-30"
      context: "'Notes on the Way', Time and Tide; before the span. Collective 'we', not first-person profession — kept as context; not used alone to score primary_system or A."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Unofficial web (orwell.ru). Collective historical claim (create-pass finding stands). Later para hopes to 'reinstate the belief in human brotherhood without the need for a \"next world\"'."
  changes_over_life:
    - {value: "Childhood CoE belief until ~age 14 (Joys); adult working years take humanist this-world / no-afterlife side (Lear, Gandhi, As I Please). 1932 churchgoing described by him as keeping up a deception when he did not believe (Davison/Crick).", year: 1917, certainty: 0.5, cites: [{source: S3, locator: "Joys V"}, {source: S7, locator: "letter X/271"}, {source: S5, locator: "Lear"}, {source: S6, locator: "Gandhi"}], how_known: "Own memoir + letters via secondary + in-span essays."}
  coder_notes: "Deepen D1 (queue #164): first-person path opened via Lear (1947) + Gandhi (1949 Foundation) + As I Please (1944 Tribune archive) + Joys. B deliberately UNKNOWN — do not force plot; miracle-indifference is not P16 nature-order. CEJL / Complete Works (Davison) print still unread — main blocker for lifting web-copy caps on Lear/Joys/As I Please beyond Foundation Gandhi. Chart-moving NO. No fallacy_catalog (Jason)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English", certainty: 0.7, cites: [{source: S4, locator: "Early years"}], how_known: "Wikipedia."}
  religious_heritage_by_birth: {value: "Anglican (Church of England); paternal grandfather Thomas Richard Arthur Blair an Anglican clergyman", certainty: 0.7, cites: [{source: S4, locator: "Early years"}], how_known: "Wikipedia."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Infant baptism not separately documented this pass; Anglican household makes it likely."}
  childhood_catechism: {value: "Prayer Book / school chapel Christianity at St Cyprian's", certainty: 0.5, cites: [{source: S3, locator: "Joys, parts IV–V"}], how_known: "Memoir."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1945–1949", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Animal Farm (1945) to Nineteen Eighty-four (1949) (P29, P30)."}
  age_at_first_lasting_contribution: {value: 42, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "1945 − 1903 = 42 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: "1932 (letter: goes to Holy Communion 'when one doesn't believe')", certainty: 0.5, cites: [{source: S7, locator: "X/271 via Davison"}], how_known: "Secondary quotation of letter; earlier works not fully read (P30). Create-pass had 1940 Notes; letter is earlier adult first-person non-belief."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S5, locator: "1947"}, {source: S6, locator: "1949"}], how_known: "Lear and Gandhi fall inside 1945–1949."}
  worldview_during_major_work: {value: "Humanist this-world / no personal afterlife; chooses Man over God-assumption; outsider to Christian doctrine", certainty: 0.5, cites: [{source: S5, locator: "Lear"}, {source: S6, locator: "Gandhi"}, {source: S8, locator: "As I Please"}], how_known: "In-span essays + consistent before-span first person."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Fiction and essays (S1); no Euclidean ideal-geometry theology read.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data for geometric Lane B model."
  notes: "CoE burial and sentimental Anglican practice are heritage/practice, not a Lane A creed reverse."

institutions:
  - {value: "British Broadcasting Corporation (Indian service)", role: "talks producer / head of cultural broadcasts to India", years: "1941–1943", kind: "other", certainty: 0.7, cites: [{source: S1, locator: "From The Road to Wigan Pier to World War II"}, {source: S4, locator: "Second World War"}], how_known: "Two sources."}
  - {value: "Tribune", role: "literary editor; 'As I Please' columnist", years: "1943–1945", kind: "other", certainty: 0.7, cites: [{source: S4, locator: "Second World War"}, {source: S8, locator: "3 March 1944"}], how_known: "Two sources."}
collaborators:
  - {value: "Eileen O'Shaughnessy", relation: "family", note: "wife; typist and copy editor; died 1945", certainty: 0.7, cites: [{source: S1, locator: "Against imperialism"}, {source: S4, locator: "Relationships"}], how_known: "Two sources."}
  - {value: "Sonia Brownell", relation: "family", note: "second wife (1949)", certainty: 0.7, cites: [{source: S4, locator: "Final months"}], how_known: "Wikipedia."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S10, locator: "roster.csv, rank 173"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "CEJL / Complete Works print volumes unread (IA borrow-gated); Lear, Joys, As I Please still partly on unofficial web copies."
    - "1932 non-belief letter known via Davison/Crick secondary quotation only this pass."
  open_questions:
    - "CEJL vol. 3 (As I Please) and Davison Complete Works XIX (Joys) / XVI–XX print check."
    - "Letter to Humphrey House, 11 April 1940 ('without the need to tie it up with any transcendental belief') — Humanists UK quote; full letter unread."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "George Woodcock"
    citation: "Woodcock, George. 'George Orwell.' Encyclopaedia Britannica (rev. 2026). https://www.britannica.com/biography/George-Orwell"
    url: "https://www.britannica.com/biography/George-Orwell"
    accessed: 2026-10-19
    source_quality: "reference entry"
    reliability_note: "Signed article; body cited, question boxes not used (P26)."
    used_for: [identity, basics, contribution, childhood, worldview, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "George Orwell"
    citation: "Orwell, George. 'Notes on the Way.' Time and Tide (30 March and 6 April 1940); CEJL (1968). Transcription at orwell.ru. https://orwell.ru/library/articles/notes/english/e_notew"
    url: "https://orwell.ru/library/articles/notes/english/e_notew"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Unofficial web copy of a published essay (capped at 0.7, CODING_GUIDE §7). Collective 'we' — context only for scoring."
    used_for: [worldview, timing]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "George Orwell"
    citation: "Orwell, George. 'Such, Such Were the Joys.' Written ~1947; Partisan Review (Sept–Oct 1952); CEJL (1968). Transcription at orwell.ru. https://www.orwell.ru/library/essays/joys/english/e_joys"
    url: "https://www.orwell.ru/library/essays/joys/english/e_joys"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Unofficial web copy; Davison Complete Works XIX print unread."
    used_for: [worldview, childhood, heritage, timing]
  - id: S4
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "Wikipedia. 'George Orwell.' https://en.wikipedia.org/wiki/George_Orwell"
    url: "https://en.wikipedia.org/wiki/George_Orwell"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "P50 dual bio; Religion section used for heritage and burial; not for LIO scores."
    used_for: [identity, basics, childhood, heritage, institutions, collaborators, review]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "George Orwell"
    citation: "Orwell, George. 'Lear, Tolstoy and the Fool.' Polemic, No. 7 (March 1947); reprinted Shooting an Elephant (1950); CEJL. Transcription at orwell.ru. https://www.orwell.ru/library/essays/lear/english/e_ltf"
    url: "https://www.orwell.ru/library/essays/lear/english/e_ltf"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Unofficial web; wording cross-checked against Humanists UK long quotation (S9)."
    used_for: [worldview, contribution, timing]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "George Orwell"
    citation: "Orwell, George. 'Reflections on Gandhi.' Partisan Review (January 1949). Text at The Orwell Foundation (reproduced with permission of the Orwell Estate). https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/reflections-on-gandhi/"
    url: "https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/reflections-on-gandhi/"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Official estate/institution site (§7); lifts unofficial-web cap for this essay's wording."
    used_for: [worldview, contribution, timing]
  - id: S7
    type: secondary
    kind: "journal article"
    author: "Peter Davison"
    citation: "Davison, Peter. 'Orwell – religion and ethical values.' The Orwell Foundation (reprinted from Finlay Publisher). Quotes Complete Works letters (e.g. X/271 on Holy Communion 'when one doesn't believe') and burial (XX/237). https://www.orwellfoundation.com/the-orwell-foundation/orwell/articles/peter-davison-orwell-religion-and-ethical-values/"
    url: "https://www.orwellfoundation.com/the-orwell-foundation/orwell/articles/peter-davison-orwell-religion-and-ethical-values/"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Editor of Complete Works; letter wording is secondary quotation until CW volumes opened."
    used_for: [worldview, heritage, timing]
  - id: S8
    type: primary
    kind: "published work by the subject"
    author: "George Orwell"
    citation: "Orwell, George. 'As I Please.' Tribune, 3 March 1944. Tribune magazine archive reprint. https://tribunemag.co.uk/1944/03/as-i-please-by-george-orwell-15"
    url: "https://tribunemag.co.uk/1944/03/as-i-please-by-george-orwell-15"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Archive reprint on the original magazine's site of the column it published; wording cross-checked against telelib.com / orwell.ru unofficial copies. CEJL vol. 3 print unread."
    used_for: [worldview, institutions, timing]
  - id: S9
    type: secondary
    kind: "encyclopedia"
    author: "Alex Mortimer / Humanists UK"
    citation: "Mortimer, Alex. 'George Orwell (1903–1950).' Humanist Heritage (Humanists UK). https://heritage.humanists.uk/george-orwell/"
    url: "https://heritage.humanists.uk/george-orwell/"
    accessed: 2026-10-24
    source_quality: "other"
    reliability_note: "Advocacy heritage page; used for SECHUM alt context and long Lear/Gandhi quotations cross-check, not as sole Lane A support."
    used_for: [worldview]
  - id: S10
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [review]
---

## Summary

George Orwell (Eric Arthur Blair, 1903–1950), novelist and essayist [S1; S4]. Deepen D1: primary_system ATHE @0.5 (alt SECHUM); A 4 @0.5 corroborated; B UNKNOWN; C 4 @0.5 corroborated; mid_basin BELOW_THRESHOLD. Not plotted. Chart-moving NO.

## Life and work

Burma, Paris, London, Spain, Jura [S1; S4]. Tribune literary editor; BBC Eastern Service [S4; S8].

## Contribution and impact

Animal Farm; Nineteen Eighty-Four [S1]. In-span essays Lear (1947) and Reflections on Gandhi (1949) used for worldview [S5; S6].

## Childhood and education

St Cyprian's; Eton [S1; S4]. Anglican heritage; believed in God till about fourteen [S3; S4].

## Adult working worldview

Chooses Man / this world over God-assumption and next-world Christianity [S5; S6]. Does not want belief in life after death to return [S8]. B not scored (no nature-order profession) [coder_notes].

## Heritage (context only)

Anglican birth heritage; CoE burial by request — practice/sentiment, not the scored creed [S4; S7].

## Timing

1945–1949, age 42 [S1]. LIO-type views evidenced during the span (Lear, Gandhi) [S5; S6].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No geometric data.

## Open questions

- CEJL / Complete Works print check for As I Please, Joys, Lear.
- Humphrey House letter (11 April 1940) full text.

## Research log

- 2026-10-19: Read Britannica (Woodcock); Notes on the Way.
- 2026-10-24 (D1): Orwell Foundation Gandhi (estate); Lear (orwell.ru); As I Please (Tribune archive + telelib); Joys (orwell.ru); Davison religion essay; Wikipedia Religion/Early years; Humanists UK. B left UNKNOWN. No figures/.
