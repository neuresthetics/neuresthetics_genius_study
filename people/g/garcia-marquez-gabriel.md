---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, deepen D1 queue #30)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch F, order P32: F 5, rank 30). Basics from Britannica (González Echevarría) and the Nobel Prize biographical note. The only statement on God found is 'No creo en Dios, pero le temo', known only as reported speech (biographer Gerald Martin, who calls it possibly a joke; Alfa y Omega). Characters' words in the novels are not his view. primary_system and A BELOW_THRESHOLD; B, C, D, E UNKNOWN; mid_basin UNKNOWN. Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #30, next-50 batch). Needs were A BELOW_THRESHOLD and B UNKNOWN. Opened El olor de la guayaba (1982 Mendoza interview book; Spanish excerpts via El Tiempo / Revista BOCAS): affirms 'El que no tenga Dios, que tenga supersticiones' as 'muy serio'; superstitions as natural faculties repudiated by Western rationalism; yellow flowers for protection; 'prejuicios de mi formación católica' as inherited double standard, not adult CHRIST. Opened El País 27 Jan 1981 essay (Scandal of the Century / LitHub): literary credo affirming biblical/literary wonders still happen against 'obscurantist rationalism' of bad teachers — aesthetic method, not scored as P16 B. Paris Review 1981 and UNESCO Courier: Caribbean reality / realist self-description; not God-locus. Wikipedia EN dual-sources bio (full name; death place; Zipaquirá). P47 on every source. 'No creo en Dios, pero le temo' still reported speech only (Martin joke; Alfa y Omega; Guardian misattributes Cholera character line). primary_system stays BELOW_THRESHOLD (lead ATHE; P38 unmet). A stays BELOW_THRESHOLD. B stays UNKNOWN (not a scientist; superstition practice and wonder-creed ≠ nature's causal order, P16; P41 does not apply — he affirms wonders/superstitions rather than rejecting miracles). C/D/E UNKNOWN; mid_basin UNKNOWN. Chart-moving NO. Characters unused. No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: garcia-marquez-gabriel
  display_name: "Gabriel García Márquez"
  roster:
    canonical_name: "Gabriel García Márquez"
    rank: 30
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: literature
    field_bucket: literature
  full_name: {value: "Gabriel José García Márquez", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "lead / infobox"}], how_known: "Britannica short form + Wikipedia EN full form Gabriel José García Márquez."}
  native_name: {value: UNKNOWN, how_known: "Spanish in Latin script; no distinct native orthography beyond the accented Spanish form already in display_name."}
  aliases:
    - {name: "Gabriel Garcia Marquez", kind: "roster alias"}
    - {name: "Gabriel-Garcia-Marquez", kind: "roster alias"}
    - {name: "García Márquez-Gabriel", kind: "roster alias"}
    - {name: "Gabo", kind: "other"}
    - {name: "Gabito", kind: "other"}

basics:
  birth:
    date: {value: "1927-03-06", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "infobox / lead ('6 March 1927')"}, {source: S2, locator: "first sentence (year)"}], how_known: "Britannica + Wikipedia EN (full date); Nobel confirms year. Some older editions / self-report used 1928 — Wikipedia notes the dispute; memoir Vivir para contarla confirms 1927 (via S6)."}
    place: {value: "Aracataca, Colombia", modern_name: "Aracataca, Magdalena, Colombia", polity_then: "Colombia", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "first sentence"}, {source: S6, locator: "infobox"}], how_known: "Britannica, Nobel, Wikipedia EN."}
  death:
    date: {value: "2014-04-17", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "closing line"}, {source: S6, locator: "infobox / Death"}], how_known: "Britannica, Nobel page, Wikipedia EN."}
    place: {value: "Mexico City, Mexico", modern_name: "Mexico City, Mexico", polity_then: "Mexico", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "infobox / Death"}], how_known: "Britannica + Wikipedia EN."}
  first_lasting_contribution_year: {value: 1955, certainty: 0.7, cites: [{source: S1, locator: "'Works'"}, {source: S2, locator: "Bibliography (La hojarasca, 1955)"}, {source: S6, locator: "Works"}], how_known: "Earliest listed lasting contribution, La hojarasca (1955) (P13). 0.7 because whether the first novel is itself lasting is the coder's reading."}
  era_bucket: {value: "1950 on", certainty: 0.7, cites: [{source: S1, locator: "'Works'"}], how_known: "From 1955 (P2)."}
  region_of_birth: {value: "Latin America and Caribbean", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "first sentence"}], how_known: "Colombia (P3)."}
  region_of_work: {value: "Latin America and Caribbean", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}, {source: S6, locator: "biography"}], how_known: "Colombia and Mexico, with periods in Paris, Spain and Havana; Mexico City is where he wrote Cien años (S1)."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S1, locator: "text"}, {source: S6, locator: "lead"}], how_known: "As recorded."}
  languages_of_work: {value: [Spanish], certainty: 1.0, cites: [{source: S1, locator: "'Works' (Spanish titles)"}, {source: S2, locator: "Bibliography"}, {source: S6, locator: "infobox Language"}], how_known: "Britannica, Nobel, Wikipedia EN."}
  occupations: {value: ["novelist", "short-story writer", "journalist", "screenwriter"], certainty: 1.0, cites: [{source: S1, locator: "opening; 'Life'"}, {source: S2, locator: "first paragraph"}, {source: S6, locator: "lead / occupations"}], how_known: "Britannica, Nobel, Wikipedia EN."}

contribution:
  fields: {value: ["fiction", "journalism"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "lead"}], how_known: "Britannica + Wikipedia EN."}
  lasting_original_contributions:
    - {value: "La hojarasca (Leaf Storm), first novel; first Macondo fiction", year: 1955, kind: work, lasting: "first of the books that build the Macondo world (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Works'"}, {source: S2, locator: "Bibliography"}], how_known: "Dated by both; lasting is the coder's reading."}
    - {value: "Cien años de soledad (One Hundred Years of Solitude)", year: 1967, kind: work, lasting: "his 'masterpiece'; main basis of the 1982 Nobel Prize (S1); the model case of 'magic realism'", certainty: 1.0, cites: [{source: S1, locator: "opening; 'Works'"}, {source: S2, locator: "Bibliography"}, {source: S6, locator: "Notable works"}], how_known: "Three sources."}
    - {value: "El amor en los tiempos del cólera (Love in the Time of Cholera)", year: 1985, kind: work, lasting: "among 'the best' of his later books (S1)", certainty: 1.0, cites: [{source: S1, locator: "'Works'"}, {source: S2, locator: "Bibliography"}], how_known: "Two sources."}
    - {value: "Vivir para contarla (Living to Tell the Tale), memoir", year: 2002, kind: work, lasting: "major late public work, the memoir of his first 30 years (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Works'"}, {source: S6, locator: "Works"}], how_known: "Britannica + Wikipedia EN."}
  evidence_of_impact:
    - {value: "Nobel Prize in Literature, 1982", kind: "honours in lifetime", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "page title"}], how_known: "Two sources."}
    - {value: "One Hundred Years of Solitude sold over fifty million copies; most-translated Spanish-language author of the 21st century (as of 2023)", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S6, locator: "lead"}], how_known: "Wikipedia EN."}
  major_works:
    - {value: "El olor de la guayaba (Fragrance of Guava), interview book with Plinio Apuleyo Mendoza", year: 1982, kind: other, certainty: 1.0, cites: [{source: S7, locator: "BOCAS / El Tiempo headnote (Oveja Negra / Penguin editions)"}, {source: S6, locator: "Works / interviews"}], how_known: "Published interview book opened this deepen for worldview."}
    - {value: "Crónica de una muerte anunciada (Chronicle of a Death Foretold)", year: 1981, kind: book, certainty: 0.7, cites: [{source: S1, locator: "'Works'"}, {source: S6, locator: "Notable works"}], how_known: "Britannica + Wikipedia EN."}
    - {value: "El otoño del patriarca (The Autumn of the Patriarch)", year: 1975, kind: book, certainty: 0.7, cites: [{source: S1, locator: "'Works'"}, {source: S6, locator: "Works"}], how_known: "Britannica + Wikipedia EN."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Nobel Prize; Britannica ranks him with Borges as the best-known Latin American writer.", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "lead"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Roman Catholic (family practice; mother devout)", certainty: 0.5, cites: [{source: S7, locator: "sexual-freedom answer ('prejuicios de mi formación católica')"}, {source: S3, locator: "Martin: almost his entire family very Catholic; he respected mother's beliefs"}], how_known: "Own interview names Catholic formation as prejudice source; Martin reports family Catholicism. Heritage, not adult code."}
  family_religious_practice: {value: "Mother kept a candle burning and prayed when sons flew; grandmother told hair-raising stories unselfconsciously (superstitious household)", certainty: 0.7, cites: [{source: S9, locator: "mother candle anecdote; grandmother night stories"}], how_known: "(interview) UNESCO Osorio interview."}
  parents_and_household:
    - {value: "Raised for his first eight years by his maternal grandparents, Colonel Nicolás Márquez and Tranquilina Iguarán Cotes de Márquez", role: grandparents, certainty: 1.0, cites: [{source: S1, locator: "'Life'"}, {source: S2, locator: "first sentence"}, {source: S6, locator: "Early life"}], how_known: "Britannica, Nobel, Wikipedia EN."}
    - {value: "Father, Gabriel Eligio García (telegrafist / pharmacist); mother, Luisa Santiaga Márquez Iguarán", role: parents, certainty: 1.0, cites: [{source: S6, locator: "Early life"}, {source: S7, locator: "Los suyos"}], how_known: "Wikipedia EN + Guayaba."}
  household_circumstances: {value: "Aracataca grandparents' house; banana-company town; later poverty with parents after grandfather's death", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}, {source: S7, locator: "Orígenes / Los suyos"}], how_known: "Britannica + Guayaba."}
  schooling:
    - {value: "Liceo Nacional de Varones de Zipaquirá (boarding; Jesuit / religious secondary tradition in sources varies — Nobel says Jesuit college; Wikipedia names Zipaquirá liceo)", stage: "grammar or secondary school", run_by: "religious body", years: UNKNOWN, ages: "about 13–", certainty: 0.5, cites: [{source: S2, locator: "first paragraph (Jesuit college)"}, {source: S6, locator: "infobox Alma mater / Early life"}], how_known: "Nobel 'Jesuit college' + Wikipedia Zipaquirá; years not pinned this pass."}
    - {value: "Began law at National University of Colombia (Bogotá); left incomplete for journalism", stage: university, years: UNKNOWN, certainty: 0.7, cites: [{source: S1, locator: "'Life'"}, {source: S6, locator: "lead / Education"}], how_known: "Britannica + Wikipedia EN."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading:
    - {value: "Kafka Metamorphosis (age ~17–19); Joyce, Woolf, Faulkner via Barranquilla group; Bible as 'libro cojonudo' of fantastic events (Guayaba)", certainty: 0.7, cites: [{source: S7, locator: "La formación / Lecturas"}, {source: S8, locator: "Paris Review (Kafka first line)"}], how_known: "Interview book + Paris Review."}
  childhood_mentors:
    - {value: "Grandfather Nicolás Márquez, whose stories he called his most important literary source", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}, {source: S7, locator: "Los suyos"}], how_known: "Britannica + Guayaba."}
    - {value: "Grandmother Tranquilina Iguarán — told atrocious stories without emotion; model for Cien años narrative voice", certainty: 0.7, cites: [{source: S7, locator: "El oficio ('En primer término, mi abuela')"}, {source: S9, locator: "grandmother stories"}], how_known: "Guayaba + UNESCO."}
  languages_in_childhood: {value: [Spanish], certainty: 0.7, cites: [{source: S6, locator: "infobox"}], how_known: "Wikipedia EN."}
  notable_events:
    - {value: "Grandfather's death ended Aracataca childhood; sent toward Bogotá / Zipaquirá schooling", year: 1937, age: 8, certainty: 0.7, cites: [{source: S6, locator: "Early life"}, {source: S7, locator: "Los suyos"}], how_known: "Wikipedia EN + Guayaba."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1955–2002", certainty: 0.7, cites: [{source: S1, locator: "'Works'"}, {source: S6, locator: "Works"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Superstitions (or so-called) may be natural faculties that Western rationalist thought repudiated; 'El que no tenga Dios, que tenga supersticiones' affirmed as very serious (S7). Literary credo against 'obscurantist rationalism' of bad teachers; wonders still happening if we could see them (S10). Not a science–religion equation.", certainty: 0.7, cites: [{source: S7, locator: "Supersticiones, manías y gustos (BOCAS excerpt)"}, {source: S10, locator: "El País 1981 / Scandal of the Century"}], how_known: "(interview) Guayaba + published essay."}
  primary_system:
    value: BELOW_THRESHOLD
    how_known: "Lead ATHE from biographer Martin ('no era religioso'; S3), Spanish Wikipedia 'Religión: Ninguna' / Ateos category (S6 via S3), and the circulating 'No creo en Dios, pero le temo' — still only reported speech (Martin: perhaps a joke; Alfa y Omega anecdote; Guardian quotes the line from Love in the Time of Cholera, i.e. a character). Guayaba (S7) affirms the proverb 'El que no tenga Dios, que tenga supersticiones' as serious and names Catholic formation as prejudice, without a first-person 'I do not believe in God'. P38 / Joyce–Monet–Kahlo precedent: no scored ATHE or A 4 without own-words God denial."
    note: "Candidates ATHE and AGNOS stay below 0.5 for the code. CHRIST rejected for adult working years (Martin; Guayaba double-moral remark is heritage prejudice)."
  secondary_system: {value: UNKNOWN, how_known: "No second system. Magical realism is a literary label, not a worldview code."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Lead: Martin 'no era religioso' (S3); ES Wikipedia Ninguna/Ateos (reconstruction); reported 'No creo en Dios'. Rejected as scored code: no first-person God-denial in Guayaba, Paris Review, UNESCO, or El País essay opened this pass."}
    - {code: AGNOS, reason: "Fear-clause of the reported joke could read as suspension; still reported speech only. Guayaba superstition affirmative is not suspension-of-judgment language."}
    - {code: CHRIST, reason: "Rejected for adult years: Catholic baptism/formation and devout mother are heritage (S7 'formación católica'); Martin says not religious; biblical material in novels is craft, not profession."}
    - {code: PANT, reason: "Rejected: Caribbean 'supernatural side of things' (S9) is cultural/literary realism, not God-as-Nature."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Opened Guayaba (S7), El País 1981 essay (S10), Paris Review (S8), UNESCO (S9), Martin/Alfa y Omega (S3/S4): still no own-words locus placing God (or denying God's existence). Named reading: 4 (ATHE) if 'No creo en Dios, pero le temo' is verified as his own published/interviewed words (not Cholera character; not joke-only anecdote).", note: "Guayaba 'quien no tenga Dios' is conditional proverb, not 'I have no God'. Literary wonder-creed (S10) and superstition practice do not locate God."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P16). Researched: Guayaba superstition chapter (yellow flowers protect; 13 is good luck; superstitions as natural faculties vs Western rationalism); El País 1981 ('I believe other similar wonders are still happening'); UNESCO Caribbean 'reality that ignores the laws of reason' / 'I see myself as a realist'. These are folk practice and literary epistemology, not a statement that nature's causal order is miracle-exempt or exceptionless. P41 (reject miracles → B 3 @ 0.5) does not apply: he affirms wonders/superstitions rather than rejecting miracles. Named reading: B 1 or 0 if the wonder-essay is treated as metaphysical rather than aesthetic."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read in his own words on personal reward/punishment or afterlife ledger. Fiction unused."}
    D_authority: {value: UNKNOWN, how_known: "Anti-Cartesian / anti-'obscurantist rationalism' language (S7, S10) repudiates a style of reason, not a scored revelation-vs-observation claim. No statement that revelation outranks observation or the reverse."}
    E_scope: {value: UNKNOWN, how_known: "Nothing on the world's order as one/many (P7). Magical-realist fiction unused."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN, which takes precedence (§6, P19); A_locus is BELOW_THRESHOLD."}
  statements:
    - text: "Lo dijiste alguna vez: «El que no tenga Dios, que tenga supersticiones». Es un tema serio para ti. — Muy serio. — ¿Por qué? — Creo que las supersticiones —o lo que llaman supersticiones— pueden corresponder a facultades naturales que un pensamiento racionalista, como el que domina en Occidente, ha resuelto repudiar."
      cites: [{source: S7, locator: "Supersticiones, manías y gustos (El Tiempo / Revista BOCAS excerpt of El olor de la guayaba)"}]
      date: "1982"
      context: "Published interview book El olor de la guayaba (conversations with Plinio Apuleyo Mendoza). Mendoza quotes back a line García Márquez had said; García Márquez affirms it as very serious and explains superstitions as natural faculties repudiated by Western rationalism."
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "(interview) Own words affirming the proverb and the rationalism critique. Does not deny God's existence; conditional 'quien no tenga Dios'. Underwrites BELOW lead ATHE / anti-rationalist stance; not scored for A or B (P38, P16)."
    - text: "Mientras haya flores amarillas nada malo puede ocurrirme. Para estar seguro necesito tener flores amarillas (de preferencia rosas amarillas) o estar rodeado de mujeres."
      cites: [{source: S7, locator: "Supersticiones, manías y gustos (BOCAS excerpt)"}]
      date: "1982"
      context: "Same Guayaba superstition chapter; personal protective practice."
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "(interview) Folk luck practice; not scored as B nature-order (P16)."
    - text: "En la práctica, no puedo escapar a los prejuicios de mi formación católica y de mi sociedad burguesa, y estoy a merced, como todos nosotros, de una doble moral."
      cites: [{source: S7, locator: "sexual-freedom answer (BOCAS excerpt)"}]
      date: "1982"
      context: "Guayaba, answering whether sexual freedom has limits; names Catholic formation as source of prejudice, not as adult faith."
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "(interview) Heritage/prejudice marker; supports rejecting adult CHRIST code."
    - text: "I believe that in reality there was a time when carpets flew and genies were imprisoned in bottles. I believe Balaam's ass spoke—as the Bible tells us—and the only regrettable thing is that his voice was not recorded… Even more: I believe other similar wonders are still happening, and if we don't see them it is in large measure because we are impeded by the obscurantist rationalism inculcated in us by bad literature teachers."
      cites: [{source: S10, locator: "El País, 27 January 1981; English in The Scandal of the Century (Vintage / LitHub)"}]
      date: "1981-01-27"
      context: "Published newspaper essay against over-interpretation by literature teachers; mixes literary belief (Kafka, Gargantua, Cervantes's glass lawyer) with biblical wonders. Closing: 'That's what I think, here in the back room.'"
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Own published words. Literary/anti-pedagogy credo; named possible B lean if read as metaphysics — kept out of B score under P16 (not nature's causal order as exceptionless law)."
    - text: "In the Caribbean, and in Latin America in general, we consider so-called magical situations part of everyday life, like any other aspect of reality. It seems quite natural to us to believe in portents, telepathy, premonitions, a whole host of superstitions and fantastical ways of coming to terms with reality. I never try to explain or justify such phenomena in my books. I see myself as a realist, pure and simple."
      cites: [{source: S9, locator: "UNESCO Courier interview (Manuel Osorio)"}]
      date: "1996"
      context: "UNESCO Courier interview on Latin American culture and magical realism. 'We' is Caribbean/Latin American cultural voice; closes with personal 'I see myself as a realist'."
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "(interview) Cultural realism claim; not a personal God-locus or P16 B score."
    - text: "It always amuses me that the biggest praise for my work comes for the imagination, while the truth is that there's not a single line in all my work that does not have a basis in reality. The problem is that Caribbean reality resembles the wildest imagination."
      cites: [{source: S8, locator: "Paris Review, The Art of Fiction No. 69 (Winter 1981)"}]
      date: "1981"
      context: "Paris Review interview; on invention vs reality in his fiction."
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "(interview) Craft/reality claim; not scored for A or B."
    - text: "Alguna vez dijo, en tono de broma, que no creía en Dios pero le tenía miedo."
      cites: [{source: S3, locator: "Caracol Radio interview with Gerald Martin, April 2014"}, {source: S4, locator: "Alfa y Omega paraphrase"}]
      date: "2014-04"
      context: "Authorised biographer Gerald Martin on radio after García Márquez's death; Alfa y Omega separately narrates the line at a 1973 Havana gathering and to John Paul II (1979) without a primary transcript."
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Reported speech — cannot score an axis alone (CODING_GUIDE §7). Kept as data-quality control. Guardian's Cholera attribution is a character line, not his."
  changes_over_life:
    - {value: "Catholic formation and devout family → adult non-religious / humanist stance per Martin; superstition practice retained as anti-rationalist defense (Guayaba 1982)", certainty: 0.5, cites: [{source: S3, locator: "interview"}, {source: S7, locator: "Supersticiones"}], how_known: "Biographer + interview book; not a scored conversion narrative."}
  coder_notes: "Characters unused (including Cholera 'I don't believe in God' line). Chart-moving NO: A BELOW and B UNKNOWN leave the person unplotted. Guayaba read via BOCAS/El Tiempo authorized excerpts (secondary quotation); book page images not opened."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Colombian, Caribbean coast (mestizo Caribbean culture; African / Indigenous / Andalusian mix in his own account)", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}, {source: S7, locator: "La formación (Angola / mestizo)"}, {source: S9, locator: "Caribbean culture"}], how_known: "Britannica + own interviews."}
  religious_heritage_by_birth: {value: "Roman Catholic", certainty: 0.5, cites: [{source: S7, locator: "'formación católica'"}, {source: S3, locator: "Martin: family very Catholic"}], how_known: "Own interview + biographer."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1955–2002", certainty: 0.7, cites: [{source: S1, locator: "'Works'"}, {source: S6, locator: "Works"}], how_known: "1955 to 2002, first to last listed lasting contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 28, certainty: 1.0, cites: [{source: S1, locator: "opening; 'Works'"}, {source: S6, locator: "infobox"}], how_known: "1955 − 1927 = 28 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement scored at 3 or 4 on A or B."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S7, locator: "Supersticiones"}, {source: S10, locator: "El País 1981"}], how_known: "A BELOW; B UNKNOWN."}
  worldview_during_major_work: {value: BELOW_THRESHOLD, how_known: "(interview) Guayaba superstition affirmative + reported non-belief; no scored code.", note: "Martin: 'no era religioso' (S3)."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Nothing read on formal Euclidean-style reasoning as a lived method.", certainty: 0.5, cites: [{source: S1, locator: "'Life'"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Life'"}], how_known: "Nothing read."}
  circle_present: {value: "unclear", rationale: "No own-words statement that places God and nature on the circle poles; anti-rationalist superstition practice is not a circle finding.", certainty: 0.5, cites: [{source: S7, locator: "Supersticiones"}, {source: S3, locator: "interview"}], how_known: "Coder's reading."}
  reading: "No reading possible."
  notes: "Lane B separate from Lane A axis scores."

institutions:
  - {value: "Liceo Nacional de Varones de Zipaquirá", role: student, years: UNKNOWN, kind: other, certainty: 0.5, cites: [{source: S6, locator: "infobox Alma mater"}], how_known: "Wikipedia EN."}
  - {value: "National University of Colombia", role: student, years: UNKNOWN, kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Life'"}, {source: S6, locator: "infobox"}], how_known: "Britannica + Wikipedia EN."}
collaborators:
  - {value: "Mercedes Barcha Pardo", relation: family, note: "wife from 1958; two sons Rodrigo and Gonzalo", certainty: 1.0, cites: [{source: S6, locator: "lead / Family"}, {source: S7, locator: "Los suyos"}], how_known: "Wikipedia EN + Guayaba."}
  - {value: "Plinio Apuleyo Mendoza", relation: collaborator, note: "friend; interviewer for El olor de la guayaba (1982)", certainty: 1.0, cites: [{source: S7, locator: "headnote"}], how_known: "Interview book."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 30"}], how_known: "Study roster."}
  controversies:
    - {value: "Friendship with Fidel Castro and left politics; criticisms of Cuban intellectual repression he would not echo", certainty: 0.7, cites: [{source: S6, locator: "Political and ideological views"}, {source: S7, locator: "Fidel friendship answer"}], how_known: "Wikipedia EN + Guayaba."}
  data_quality_flags:
    - "The Nobel note says he was first sent to Rome in 1954; its own footnote says his memoir names Geneva."
    - "Birth year 1927 vs 1928: some editions and self-report used 1928; Britannica/Wikipedia/memoir settle on 1927."
    - "Guardian 'I don't believe in God…' attributed to Love in the Time of Cholera — character speech, not his."
    - "Guayaba read via authorized BOCAS/El Tiempo excerpts (secondary quotation), not page images of the 1982 book."
    - "ES Wikipedia 'Ateos de Colombia' / Religión Ninguna rests on Martin Caracol (S3), not a primary denial."
  open_questions:
    - "Page-check El olor de la guayaba (Bruguera/Oveja Negra 1982) superstition chapter against BOCAS excerpt."
    - "Gerald Martin, Gabriel García Márquez: A Life (2008) — primary quotation of the God-fear line if any."
    - "Vivir para contarla for own-words religion passages."
    - "A first-person 'No creo en Dios' in print would reopen A toward 4 at interview/written_profession ceiling."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Roberto González Echevarría"
    citation: "González Echevarría, Roberto. \"Gabriel García Márquez.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Gabriel-Garcia-Marquez."
    url: "https://www.britannica.com/biography/Gabriel-Garcia-Marquez"
    accessed: 2026-10-24
    reliability_note: "Signed article body; AI 'Top Questions' box not used."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions]
  - id: S2
    type: tertiary
    kind: institutional page
    author: "Nobel Foundation"
    citation: "\"Gabriel García Márquez – Biographical.\" NobelPrize.org. From Nobel Lectures, Literature 1981–1990, ed. Tore Frängsmyr and Sture Allén (Singapore: World Scientific, 1993)."
    url: "https://www.nobelprize.org/prizes/literature/1982/marquez/biographical/"
    accessed: 2026-10-24
    reliability_note: "Written at the time of the award (Les Prix Nobel); bibliography with editions."
    source_quality: "reference entry"
    used_for: [basics, contribution, childhood]
  - id: S3
    type: secondary
    kind: other
    author: "Gerald Martin (interviewed by Caracol Radio)"
    citation: "\"Gabo no era religioso pero respetaba las creencias de los otros.\" Caracol Radio, 6AM Hoy por Hoy, April 2014 (page dated 28/09/2015)."
    url: "https://caracol.com.co/programa/2014/04/21/6am_hoy_por_hoy/1398053520_186352.html"
    accessed: 2026-10-24
    reliability_note: "Authorised biographer on radio; reported speech about García Márquez."
    source_quality: "other"
    used_for: [worldview, timing, lane_b, heritage, childhood]
  - id: S4
    type: secondary
    kind: other
    author: "Alfa y Omega"
    citation: "\"Gabo no creía en Dios, pero le temía.\" Alfa y Omega (Madrid)."
    url: "https://alfayomega.es/gabo-no-creia-en-dios-pero-le-temia/"
    accessed: 2026-10-24
    reliability_note: "Catholic weekly; narrates the God-fear remark and 1979 papal meeting without a primary transcript."
    source_quality: "other"
    used_for: [worldview]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S6
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Gabriel García Márquez.\" https://en.wikipedia.org/wiki/Gabriel_Garc%C3%ADa_M%C3%A1rquez. Spanish Wikipedia consulted for religión/infobox cross-check."
    url: "https://en.wikipedia.org/wiki/Gabriel_Garc%C3%ADa_M%C3%A1rquez"
    accessed: 2026-10-24
    reliability_note: "Dual-source bio. ES Wikipedia Religión Ninguna / Ateos category cites Caracol/Martin (S3) — reconstruction, not a primary denial."
    source_quality: "other"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators, review]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "Gabriel García Márquez; Plinio Apuleyo Mendoza"
    year: 1982
    citation: "Mendoza, Plinio Apuleyo. El olor de la guayaba: conversaciones con Gabriel García Márquez. Bogotá: Editorial La Oveja Negra / later Penguin. Excerpts: \"Gabo y su gran entrevista de 'El olor de la guayaba',\" Revista BOCAS / El Tiempo, 31 March 2021 (authorized excerpts)."
    url: "https://www.eltiempo.com/cultura/gabo-y-su-gran-entrevista-de-el-olor-de-la-guayaba-revista-bocas-571901"
    accessed: 2026-10-24
    reliability_note: "Interview book in his own words (recorded_interview ceiling). Verified this pass against BOCAS/El Tiempo authorized Spanish excerpts, not 1982 page images."
    source_quality: "primary / own words"
    used_for: [contribution, childhood, worldview, heritage, timing, collaborators]
  - id: S8
    type: primary
    kind: "published work by the subject"
    author: "Gabriel García Márquez; interviewed by Peter Stone"
    year: 1981
    citation: "\"Gabriel García Márquez, The Art of Fiction No. 69.\" The Paris Review 82 (Winter 1981). https://www.theparisreview.org/interviews/3196/the-art-of-fiction-no-69-gabriel-garcia-marquez."
    url: "https://www.theparisreview.org/interviews/3196/the-art-of-fiction-no-69-gabriel-garcia-marquez"
    accessed: 2026-10-24
    reliability_note: "Recorded interview; sons translated. Craft/reality statements used."
    source_quality: "primary / own words"
    used_for: [childhood, worldview]
  - id: S9
    type: primary
    kind: "published work by the subject"
    author: "Gabriel García Márquez; interviewed by Manuel Osorio"
    year: 1996
    citation: "\"Interview with Gabriel García Márquez.\" The UNESCO Courier (English republication). https://courier.unesco.org/en/articles/interview-gabriel-garcia-marquez."
    url: "https://courier.unesco.org/en/articles/interview-gabriel-garcia-marquez"
    accessed: 2026-10-24
    reliability_note: "Interview; Caribbean realism / superstition-as-everyday-life passage."
    source_quality: "primary / own words"
    used_for: [childhood, worldview, heritage]
  - id: S10
    type: primary
    kind: "published work by the subject"
    author: "Gabriel García Márquez"
    year: 1981
    citation: "García Márquez, Gabriel. Essay of 27 January 1981, El País (Madrid); English in The Scandal of the Century: And Other Writings, trans. Anne McLean et al. (Vintage, 2019). Web: Literary Hub, \"On Taking Writers at Their Word,\" 2 Nov 2020."
    url: "https://lithub.com/gabriel-garcia-marquez-on-taking-writers-at-their-word/"
    accessed: 2026-10-24
    reliability_note: "Published newspaper essay in his own name; English via posthumous scholarly collection (Vintage)."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview]
---

# Gabriel García Márquez

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Gabriel García Márquez (1927–2014), Colombian novelist, Nobel Prize 1982, author of *Cien años de soledad* [S1, S2, S6]. Deepen: Guayaba interview book affirms superstition-over-God proverb and anti-rationalist faculties claim [S7]; El País 1981 literary wonder-creed [S10]; still no own-words God denial or nature-order statement. Draft: primary_system and A **BELOW_THRESHOLD**; B, C, D, E **UNKNOWN**; mid_basin **UNKNOWN**. Chart-moving: **no**.

## Life and work

Raised by grandparents in Aracataca; Zipaquirán/Jesuit secondary tradition; law abandoned for journalism; lived in Mexico City, Spain, Paris and Havana [S1, S2, S6].

## Contribution and impact

*La hojarasca* (1955), *Cien años de soledad* (1967), *El amor en los tiempos del cólera* (1985), *Vivir para contarla* (2002); Nobel 1982 [S1, S2, S6].

## Childhood and education

Grandparents' supernatural household; Catholic formation as later prejudice source; Zipaquirá liceo; National University [S1, S6, S7].

## Adult working worldview

(interview) Guayaba: superstitions as natural faculties repudiated by Western rationalism; yellow-flower protection; Catholic formation as double-moral prejudice [S7]. El País 1981: wonders still happening if rationalism did not block sight [S10]. Reported 'No creo en Dios, pero le temo' still cannot score [S3, S4]. A BELOW; B UNKNOWN.

## Heritage (context only)

Colombian Caribbean; Catholic by family formation [S1, S7, S3].

## Timing

First lasting contribution 1955, at 28 [S1, S6].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Unclear / no circle reading.

## Open questions

- Page-check Guayaba 1982; Martin biography; *Vivir para contarla* religion lines.
- Verified first-person 'No creo en Dios' would reopen A.

## Research log

- 2026-10-15: Britannica, Nobel; Martin/Alfa y Omega reported speech only.
- 2026-10-24: Deepen D1 — Wikipedia EN; Guayaba via BOCAS/El Tiempo; Paris Review; UNESCO Courier; El País 1981 / Scandal of the Century (LitHub). No fallacy_catalog.
