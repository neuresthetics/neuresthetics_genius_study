---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, deepen D1 queue #29)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to literature. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch E, order P32: F 5, rank 29). Basics from Britannica (Morson) and the chronology in Mayne's 1914 translation of his letters. Worldview: the March 1854 letter to N. D. Fonvisin (Mayne, Letter XXII, pp. 70–71, archive.org scan). Characters (Zosima, Ivan, Shatov) not used. CHRIST 0.5; A BELOW_THRESHOLD; B UNKNOWN; D BELOW_THRESHOLD; mid_basin UNKNOWN. Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Audit fixes (fallacy_catalog audit of 2332880, run 1): primary_system basis scholarly_reconstruction -> consistent_private_letters (his own letter; single letter, so 0.5 kept); locators standardised to Letter 22, begins p. 69, quote pp. 70-71."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #29, next-50 batch). Needs were A BELOW_THRESHOLD and B UNKNOWN. Opened Diary of a Writer (Brasol 1949 via archive.org OCR): Old People (Belinsky / radiant personality of Christ / God-man); Arbitrary Assertions (immortality of the soul as the one sublime idea); 1873 miracles disclaimer (refuses personal declaration on miracles); Pushkin speech (Aug 1880 Diary: Gospel of Christ; Christ traversed / born in a manger; God saw otherwise) and Gradovsky reply (people enlightened by embracing Christ). Osmidov letter Feb 1878 (Mayne Letter LXX: personal immortality and God identical; science's precise laws for organisms). Wikipedia EN dual-sources bio. P47 source_quality on every source. primary_system CHRIST 0.5→0.7 written_profession. C_ledger UNKNOWN→1 @ 0.5 corroborated; D_authority BELOW→1 @ 0.5 corroborated. A stays BELOW_THRESHOLD (personal God / Christ language still no locus where God is; P19). B stays UNKNOWN (not a scientist; Osmidov organism-laws and miracles refusal are not a P16 nature-order statement; P41 does not apply — he refuses to declare on miracles rather than rejecting them). mid_basin UNKNOWN. Chart-moving NO (still unplotted). Characters unused. No fallacy_catalog (Jason 2026-10-23/24). Draft, not reviewed."}

identity:
  id: dostoevsky-fyodor
  display_name: "Fyodor Dostoevsky"
  roster:
    canonical_name: "Fyodor Dostoevsky"
    rank: 29
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: literature
    field_bucket: literature
  full_name: {value: "Fyodor Mikhaylovich Dostoyevsky", certainty: 1.0, cites: [{source: S1, locator: "header ('Also known as')"}, {source: S4, locator: "lead ('Fyodor Mikhailovich Dostoevsky')"}], how_known: "Britannica + Wikipedia EN; transliteration varies (Dostoevsky / Dostoyevsky)."}
  native_name: {value: "Фёдор Михайлович Достоевский", certainty: 1.0, cites: [{source: S4, locator: "infobox Cyrillic"}, {source: S1, locator: "header"}], how_known: "Wikipedia EN infobox Cyrillic; Britannica gives transliterations."}
  aliases:
    - {name: "Dostoevsky-Fyodor", kind: "roster alias"}
    - {name: "Fyodor-Dostoevsky", kind: "roster alias"}
    - {name: "Fyodor Dostoyevsky", kind: "transliteration"}

basics:
  birth:
    date: {value: "1821-11-11", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "At a Glance ('November 11 [October 30, Old Style], 1821')"}, {source: S4, locator: "infobox / lead"}], how_known: "Britannica + Wikipedia EN (O.S. 30 October)."}
    place: {value: "Moscow", modern_name: "Moscow, Russia", polity_then: "Russian Empire", certainty: 1.0, cites: [{source: S1, locator: "At a Glance"}, {source: S4, locator: "infobox"}], how_known: "Britannica + Wikipedia EN."}
  death:
    date: {value: "1881-02-09", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "At a Glance"}, {source: S4, locator: "infobox / lead"}], how_known: "Britannica + Wikipedia EN (O.S. 28 January)."}
    place: {value: "St. Petersburg", modern_name: "Saint Petersburg, Russia", polity_then: "Russian Empire", certainty: 1.0, cites: [{source: S1, locator: "At a Glance"}, {source: S4, locator: "infobox"}], how_known: "Britannica + Wikipedia EN."}
  first_lasting_contribution_year: {value: 1846, certainty: 1.0, cites: [{source: S2, locator: "chronological table, 1846 ('Nekrassov's Petersburg Almanac appears, with Dostoevsky's first book, \"Poor Folk\"')"}, {source: S4, locator: "Early career / Works ('Poor Folk' 1846)"}], how_known: "Poor Folk, published 15 January 1846 (S2 chronology; S4)."}
  era_bucket: {value: "1750 to 1849", certainty: 1.0, cites: [{source: S2, locator: "chronological table, 1846"}, {source: S4, locator: "Works"}], how_known: "From 1846 (P2)."}
  region_of_birth: {value: "Eastern Europe", certainty: 1.0, cites: [{source: S1, locator: "At a Glance"}, {source: S4, locator: "infobox"}], how_known: "Russia (P3)."}
  region_of_work: {value: "Eastern Europe", certainty: 1.0, cites: [{source: S1, locator: "text"}, {source: S4, locator: "lead / biography"}], how_known: "St. Petersburg and Siberia; Russia."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S1, locator: "text"}, {source: S4, locator: "lead"}], how_known: "As recorded."}
  languages_of_work: {value: [Russian], certainty: 1.0, cites: [{source: S1, locator: "text"}, {source: S4, locator: "Writing career"}], how_known: "Britannica + Wikipedia EN."}
  occupations: {value: ["novelist", "short-story writer", "journalist", "essayist"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "infobox occupations / lead"}], how_known: "Britannica + Wikipedia EN (also military engineer early; not lasting vocation)."}

contribution:
  primary_domain: literature
  fields: {value: ["fiction"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lead"}], how_known: "Britannica + Wikipedia EN."}
  lasting_original_contributions:
    - {value: "Poor Folk", year: 1846, kind: work, lasting: "acclaimed debut; Russia's first 'social novel' in Belinsky's reading (S4)", certainty: 1.0, cites: [{source: S2, locator: "chronological table, 1846"}, {source: S4, locator: "Early career"}], how_known: "Mayne chronology + Wikipedia EN."}
    - {value: "Notes from Underground", year: 1864, kind: work, lasting: "often treated as a founding work of existentialist literature (S4)", certainty: 0.7, cites: [{source: S4, locator: "lead / Works"}], how_known: "Wikipedia EN; Britannica groups it with the major fiction."}
    - {value: "Crime and Punishment", year: 1866, kind: work, lasting: "one of the four (or five) long novels he is best known for", certainty: 1.0, cites: [{source: S1, locator: "'Major works'"}, {source: S4, locator: "Works"}], how_known: "Britannica + Wikipedia EN."}
    - {value: "The Brothers Karamazov", year: "1879–1880", kind: work, lasting: "largest novel; often cited as his magnum opus alongside Crime and Punishment (S4)", certainty: 1.0, cites: [{source: S2, locator: "chronological table, 1879–80 ('Appearance of \"The Brothers Karamazov\"')"}, {source: S1, locator: "'Major works'"}, {source: S4, locator: "Works"}], how_known: "Serialised 1879–80 (S2); dual tertiary confirm."}
  evidence_of_impact:
    - {value: "Literary modernism, existentialism and schools of psychology and theology 'profoundly shaped by his ideas'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica body."}
    - {value: "Translated into over 170 languages; influence on Camus, Sartre, Nietzsche, Freud, Kafka among others", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S4, locator: "Reception and influence / Reputation"}], how_known: "Wikipedia EN reception section."}
  major_works:
    - {value: "Diary of a Writer (A Writer's Diary)", year: "1873–1881", kind: other, certainty: 1.0, cites: [{source: S2, locator: "chronological table, 1876–77"}, {source: S4, locator: "Works / Essay collections"}, {source: S5, locator: "title pages / contents"}], how_known: "Periodical nonfiction; opened this deepen for worldview (S5)."}
    - {value: "The Idiot", year: "1868–1869", kind: book, certainty: 0.7, cites: [{source: S1, locator: "'Major works'"}, {source: S4, locator: "Works"}], how_known: "Britannica + Wikipedia EN."}
    - {value: "Demons (The Possessed / The Devils)", year: "1871–1872", kind: book, certainty: 0.7, cites: [{source: S1, locator: "'Major works'"}, {source: S4, locator: "Works"}], how_known: "Britannica + Wikipedia EN."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "One of the finest novelists; wide influence on literature, existentialism and religious thought.", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lead"}], how_known: "Britannica + Wikipedia EN."}

childhood:
  family_religion: {value: "Russian Orthodox", certainty: 0.7, cites: [{source: S1, locator: "'Background and early life' ('the old-fashioned piety of his family')"}, {source: S4, locator: "Parents / Religious beliefs ('Orthodox Christian'; paternal ancestors Orthodox; mother taught him to read from the Bible)"}], how_known: "Wikipedia EN states Orthodox family/practice; Britannica's 'piety' alone was weaker — dual-sourced as Orthodox at 0.7."}
  family_religious_practice: {value: "Old-fashioned piety; Sunday liturgies; Bible reading; pilgrimages (S4)", certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}, {source: S4, locator: "Religious beliefs"}], how_known: "Britannica + Wikipedia EN."}
  parents_and_household:
    - {value: "Father, Mikhail Andreyevich Dostoevsky, a retired military surgeon at the Mariinsky Hospital for the Poor, Moscow", role: father, certainty: 1.0, cites: [{source: S1, locator: "'Background and early life'"}, {source: S4, locator: "Parents"}], how_known: "Britannica + Wikipedia EN."}
    - {value: "Mother, Maria Fyodorovna (née Nechayeva), from a merchant family; died of tuberculosis 1837", role: mother, certainty: 1.0, cites: [{source: S1, locator: "'Background and early life'"}, {source: S4, locator: "Parents / Youth"}], how_known: "Britannica + Wikipedia EN."}
  household_circumstances: {value: "Not landed gentry; father ennobled 1828, bought Darovoye estate c. 1831", certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}, {source: S4, locator: "Parents"}], how_known: "Britannica + Wikipedia EN."}
  schooling:
    - {value: "Educated at home until 1833", stage: home, years: "–1833", ages: "–12", certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Britannica."}
    - {value: "French boarding school, then Chermak boarding school", stage: "grammar or secondary school", years: "1833–", ages: "12–", certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}, {source: S4, locator: "Childhood"}], how_known: "Britannica + Wikipedia EN."}
    - {value: "Nikolayev Military Engineering Institute (Academy of Military Engineering), St. Petersburg (entered 1838; graduated / commissioned 1843)", stage: university, years: "1838–1843", certainty: 1.0, cites: [{source: S1, locator: "'Background and early life'"}, {source: S4, locator: "infobox Education / Youth"}], how_known: "Britannica + Wikipedia EN."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading:
    - {value: "Scott, Radcliffe, Karamzin, Schiller, Pushkin, Homer, Goethe, Cervantes; mother taught reading from the Bible", certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}, {source: S4, locator: "Childhood"}], how_known: "Britannica + Wikipedia EN."}
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events:
    - {value: "Death of his mother", year: 1837, age: 16, certainty: 1.0, cites: [{source: S1, locator: "'Background and early life'"}, {source: S4, locator: "Youth"}], how_known: "Britannica + Wikipedia EN."}
    - {value: "Father's death (officially apoplexy; contested serf-murder story later)", year: 1839, age: 17, certainty: 0.7, cites: [{source: S4, locator: "Youth"}], how_known: "Wikipedia EN; Britannica less detailed on the contested story."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1846–1880", certainty: 0.7, cites: [{source: S2, locator: "chronological table"}, {source: S4, locator: "Works (Poor Folk 1846; Karamazov 1880)"}], how_known: "Equals timing.major_work_period (Poor Folk to Karamazov / Pushkin speech)."}
  nominal_affiliations:
    - {value: "Russian Orthodox Church (nominal / cultural; practiced irregularly)", certainty: 0.5, cites: [{source: S4, locator: "Religious beliefs (Orthodox Christian; Wrangel: rather pious, did not often go to church, disliked Siberian priests, spoke of Christ ecstatically)"}, {source: S5, locator: "Gradovsky reply / Old People"}], how_known: "Wikipedia EN Orthodoxy + Wrangel report; own Diary affirms Christ and people's Orthodoxy. Not scored as automatic CHRIST — primary_system rests on own words."}
  self_described_science_religion_relation: {value: "'I am a child of this age, a child of unfaith and scepticism'; yet 'If anyone could prove to me that Christ is outside the truth, and if the truth really did exclude Christ, I should prefer to stay with Christ and not with truth.' (1854). Later: Western science/trades welcome; spiritual enlightenment is Christ / the people's Orthodoxy, not Western sources (1880 Gradovsky reply).", certainty: 0.7, cites: [{source: S2, locator: "Letter 22 to N. D. Fonvisin, beginning of March 1854 (begins p. 69), quote pp. 70–71"}, {source: S5, locator: "reply to Gradovsky after Pushkin speech (enlightenment = spiritual light from Christ)"}], how_known: "Private letter (0.5 alone) plus published Diary reply — written_profession stream raises the combined claim."}
  primary_system:
    value: CHRIST
    basis: written_profession
    certainty: 0.7
    cites: [{source: S5, locator: "Old People (1873; radiant personality of Christ / God-man)"}, {source: S5, locator: "Pushkin speech (Aug 1880; Gospel of Christ; Christ traversed / born in a manger; God saw otherwise)"}, {source: S5, locator: "reply to Gradovsky (people long enlightened by embracing Christ)"}, {source: S2, locator: "Letter 22 (begins p. 69), p. 71"}, {source: S1, locator: "'Background and early life' ('Dostoyevsky's lifelong attachment to religion')"}]
    rationale: "Published own nonfiction centres Christ as God-man and the Gospel as the law of final brotherhood (Pushkin speech; Old People; Gradovsky reply), continuous with the 1854 private creed ('nothing lovelier… than the Saviour'; prefer Christ to truth). Russian Orthodoxy is the confessional frame (S4; Gradovsky reply), not a second system. Certainty 0.7 not 1.0: he also calls himself a lifelong 'child of unfaith and scepticism' (S2) and refuses a personal public declaration on miracles (S5)."
    how_known: "Multiple published Diary pieces in his own name during the major-work years (written_profession), plus the Fonvisin letter and tertiary Orthodox framing."
  secondary_system: {value: UNKNOWN, how_known: "No second system. Pochvennichestvo / Slavophile leanings are political-cultural, not a separate worldview code here."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Chosen at 0.7 written_profession from Diary + Pushkin speech + Fonvisin creed."}
    - {code: AGNOS, reason: "'child of unfaith and scepticism' — rejected as code: the same letter and later Diary state a Christ-centred creed; doubt is confessed inside CHRIST, not suspension of judgment."}
    - {code: ATHE, reason: "Rejected: he attacks Belinsky's atheism (Old People) and treats disbelief in immortality as Russia's dread (Arbitrary Assertions)."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Opened Fonvisin, Osmidov, Diary (Old People, Arbitrary Assertions, Pushkin speech, Gradovsky reply): abundant personal-God and Christ-as-agent language, still no statement that places where God is (transcendent person outside the world vs immanent / identical with the world). Named reading: 0 if a clear transcendent-locus line (e.g. Scanlan's reported late notebook 'other world… laws different from the real (created) world') is verified in a scholarly edition and treated as own words; notebook not opened this pass.", note: "'God gives me sometimes moments of perfect peace' (S2); 'personal immortality and God are one and the same' (S2 Osmidov); Christ 'born in a manger' / 'God saw otherwise' (S5 Pushkin) imply a personal God who acts — implication only under P19, as at create. Osmidov's 'I' with a law that 'transcends the earthly' is about the soul/self, not God's locus."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P16). Researched: Fonvisin, Osmidov, Diary — Osmidov affirms science's 'very precise laws' for organisms existing to live, but that is a biological/moral axiom, not nature's causal order as miracle vs exceptionless law. In 1873 he explicitly refuses to declare personally on miracles ('Never did I declare myself personally as regards my faith in miracles', S5). P41 (non-scientist who rejects miracles → B 3 @ 0.5 alt 4) does not apply: refusal to declare is not rejection. Character speeches (Ivan's Euclidean mind; Underground Man against 'laws of nature' as piano-key determinism; the logical suicide's 'laws of nature') unused by task rule."}
    C_ledger:
      value: 1
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S5, locator: "Arbitrary Assertions (1876; immortality of the human soul as the one sublime idea)"}, {source: S2, locator: "Letter LXX to N. L. Osmidov, February 1878, pp. 233–234"}]
      how_known: "Published Diary plus private letter (independent ids) → corroborated (P48). 0.5: he argues immortality/God as necessary for virtue and meaning rather than spelling out a full heaven/hell reward schedule; named alternative 0."
      rationale: "DRAFT. Leans interventionist personal ledger: without faith in the soul's immortality, existence is 'unnatural, unthinkable, impossible' (Arbitrary Assertions); 'personal immortality and God are one and the same' and without them 'why am I to live decently and do good' / why not kill (Osmidov). Salvation/afterlife scope stays on C (P7). Limited vs pole 0 because these passages stress necessity of belief for moral life more than a detailed personal judgment scene. Same direction as CHRIST system C 1."
    D_authority:
      value: 1
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S2, locator: "Letter 22 (begins p. 69), p. 71"}, {source: S5, locator: "reply to Gradovsky (spiritual enlightenment = Christ / people's Orthodoxy; Western science for trades only)"}]
      how_known: "Private Fonvisin letter plus published Gradovsky reply → corroborated. 0.5: Fonvisin is a hypothetical ('if anyone could prove'); Gradovsky reply sets spiritual enlightenment against Western sources without a full observation-vs-revelation epistemology. Named alternative 0."
      rationale: "DRAFT. Leans revelation/faith over proof for ultimate questions: he would 'stay with Christ and not with truth' if they conflicted (Fonvisin); spiritual enlightenment is Christ embraced in the people's heart, while Western science is welcomed only for trades and useful knowledge (Gradovsky reply). Not D 0: he does not ban reason or science, and he confesses lifelong scepticism."
    E_scope: {value: UNKNOWN, how_known: "Scored on the world's order (P7). Immortality, virtue, and salvation language scored on C. Nothing read that same rules govern stars/insects/humans or that denies/affirms hidden in-group exceptions in this-world events."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN, which takes precedence (P19); A_locus is BELOW_THRESHOLD."}
  statements:
    - text: "I want to say to you, about myself, that I am a child of this age, a child of unfaith and scepticism, and probably (indeed I know it) shall remain so to the end of my life."
      cites: [{source: S2, locator: "Letter 22 to N. D. Fonvisin, beginning of March 1854 (begins p. 69), quote pp. 70–71"}]
      date: "1854-03"
      context: "Letter from Omsk to N. D. Fonvisin, beginning of March 1854, after release from the prison camp."
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-15
      note: "Mayne translation (1914), archive.org scan lettersoffyodorm00dostuoft, OCR checked; Wikiquote's 'Letter XXI, p. 71' is wrong: it is Letter XXII."
    - text: "If anyone could prove to me that Christ is outside the truth, and if the truth really did exclude Christ, I should prefer to stay with Christ and not with truth."
      cites: [{source: S2, locator: "Letter 22 (begins p. 69), p. 71"}]
      date: "1854-03"
      context: "Same letter, after his 'creed' naming nothing lovelier than the Saviour."
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-15
      axes: [D_authority]
    - text: "Now suppose that there is no God, and no personal immortality (personal immortality and God are one and the same — an identical idea). Tell me then: Why am I to live decently and do good, if I die irrevocably here below?"
      cites: [{source: S2, locator: "Letter LXX to N. L. Osmidov, February 1878, pp. 233–234"}]
      date: "1878-02"
      context: "Private letter answering Osmidov's 'momentous question'; also affirms science's precise laws that organisms exist to live, then argues the moral 'I' seeks what transcends earth."
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      axes: [C_ledger]
      note: "Underwrites C 1. Organism-laws clause not scored for B (P16: not nature's causal order as miracle vs exceptionless law)."
    - text: "My article — The Verdict — refers to the basic and loftiest idea of human existence — the necessity and inevitability of a belief in the immortality of the human soul. … without faith in one's soul and its immortality, man's existence is unnatural, unthinkable, impossible. … Neither man nor nation can exist without a sublime idea. And on earth there is but one sublime idea — namely, the idea of the immortality of man's soul."
      cites: [{source: S5, locator: "Arbitrary Assertions (1876; Brasol pp. 538–540 region)"}]
      date: "1876"
      context: "Diary of a Writer essay clarifying 'The Verdict' (logical-suicide piece). Published nonfiction in his own name."
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      axes: [C_ledger]
      note: "Own published voice on immortality; characters unused. OCR via archive.org djvu.txt of Brasol Scribner's 1949."
    - text: "At this juncture, however, there remained the radiant personality of Christ himself to contend with, which was the most difficult problem. … Even so, there remained the beatific image of God-man, its moral inaccessibility, its wonderful and miraculous beauty."
      cites: [{source: S5, locator: "Old People (1873; Belinsky reminiscence)"}]
      date: "1873"
      context: "Diary of a Writer, recalling Belinsky's attempt to convert him to atheistic socialism; Dostoevsky narrates Belinsky attacking Christ while noting his own facial reaction."
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Published own reminiscence treating Christ as God-man; underwrites CHRIST primary_system. Not used for A locus (no where-God-is claim)."
    - text: "At last it may be that Russia pronounces the final Word of the great general harmony, of the final brotherly communion of all nations in accordance with the law of the gospel of Christ! … Let our country be poor, but this poor land 'Christ traversed with blessing, in the garb of a serf'. Why then should we not contain His final word? Was not He Himself born in a manger? … But God saw otherwise. Pushkin died in the full maturity of his powers."
      cites: [{source: S5, locator: "Pushkin speech (Diary of a Writer, August 1880)"}, {source: S6, locator: "Kimball English text of Pushkin speech"}]
      date: "1880-06-08"
      context: "Speech at the Pushkin memorial celebration, Moscow, 8 June 1880; published with introduction in Diary of a Writer, August 1880."
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Published own words: Gospel of Christ; Christ as historical agent; 'God saw otherwise'. Underwrites CHRIST; still no A locus. S6 is a pedagogical web copy of the same speech for reading convenience."
    - text: "Never did I declare myself personally as regards my faith in miracles. All this is your invention, and I challenge you to state where you have found it."
      cites: [{source: S5, locator: "1873 Diary reply to 'priest Kastorsky' / mummer (miracles passage)"}]
      date: "1873"
      context: "Diary of a Writer, answering a hostile piece that claimed he had 'protractedly announced' Orthodox belief in 'the most amazing miracles'."
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Blocks P41-style B scoring from miracle rejection or affirmation. He refuses to declare; not a nature-order statement."
    - text: "I assert that our people have long been enlightened, having embraced in their hearts Christ and His teachings. … If this be so, I wish to state to you that there is no reason for us to borrow such an enlightenment from Western European sources because Russian sources are fully available — and not absent."
      cites: [{source: S5, locator: "reply to Gradovsky after Pushkin speech"}, {source: S6, locator: "Kimball Gradovsky polemic section"}]
      date: "1880"
      context: "Published Diary reply to Aleksandr Gradovsky's critique of the Pushkin speech; distinguishes Western science/trades (welcome) from spiritual enlightenment (Christ / Orthodoxy)."
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      axes: [D_authority]
  changes_over_life:
    - {value: "Arrest 1849 (Petrashevsky circle), mock execution, Siberian hard labour; New Testament his only permitted book in camp", certainty: 1.0, cites: [{source: S1, locator: "text"}, {source: S4, locator: "Siberian exile / Religious beliefs"}], how_known: "Britannica + Wikipedia EN. Intensifies Christ-focus; does not by itself score axes."}
    - {value: "1854 Fonvisin letter already states Christ-creed inside confessed lifelong doubt; 1873–1880 Diary publishes Christ/immortality/Orthodoxy in his own name", certainty: 0.7, cites: [{source: S2, locator: "Letter 22"}, {source: S5, locator: "Old People; Arbitrary Assertions; Pushkin speech"}], how_known: "Continuity of CHRIST frame across working years; doubt confessed throughout."}
  coder_notes: "Characters (Zosima, Ivan, Shatov, Underground Man, logical suicide of The Verdict) unused by task rule. Scanlan's reported late notebook infinity→God/'other world' argument not opened (would be private notebook; scholarly reconstruction ceiling 0.5 if only via Scanlan). Chart-moving NO: A BELOW and B UNKNOWN leave the person unplotted."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Russian", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lead"}], how_known: "Britannica + Wikipedia EN."}
  religious_heritage_by_birth: {value: "Russian Orthodox", certainty: 0.7, cites: [{source: S4, locator: "Parents / Religious beliefs"}, {source: S1, locator: "'Background and early life'"}], how_known: "Wikipedia EN Orthodox family; Britannica piety."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: "Mother taught him to read and write using the Bible; Sunday liturgies and pilgrimages (S4)", certainty: 0.5, cites: [{source: S4, locator: "Religious beliefs / Childhood"}], how_known: "Wikipedia EN; not dual-sourced in detail."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1846–1880", certainty: 0.7, cites: [{source: S2, locator: "chronological table"}, {source: S4, locator: "Works"}], how_known: "Poor Folk (1846) to Karamazov / Pushkin speech (1880) (P29, P30 #4)."}
  age_at_first_lasting_contribution: {value: 25, certainty: 1.0, cites: [{source: S1, locator: "At a Glance"}, {source: S2, locator: "chronological table, 1846"}, {source: S4, locator: "infobox"}], how_known: "1846 − 1821 = 25 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement scored at 3 or 4 on A or B."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "Letter 22; Letter LXX"}, {source: S5, locator: "Diary pieces opened"}], how_known: "A BELOW; B UNKNOWN; C and D lean interventionist, not LIO."}
  worldview_during_major_work: {value: "CHRIST with confessed doubt; personal immortality as moral necessity; Christ preferred to 'truth' if they conflicted", certainty: 0.7, cites: [{source: S2, locator: "Letter 22; Letter LXX"}, {source: S5, locator: "Arbitrary Assertions; Pushkin speech; Old People"}], how_known: "Own words across 1854–1880 working years."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Military engineering academy; nothing read showing Euclidean proof training as a lived method. Ivan's 'Euclidean mind' is a character speech — unused.", certainty: 0.5, cites: [{source: S1, locator: "'Background and early life'"}, {source: S4, locator: "Youth (disliked science/mathematics at the academy)"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Nothing read."}
  circle_present: {value: "no", rationale: "Christ preferred even over truth; spiritual enlightenment from Christ/Orthodoxy outranks Western science for ultimate questions.", certainty: 0.5, cites: [{source: S2, locator: "Letter 22 (begins p. 69), p. 71"}, {source: S5, locator: "Gradovsky reply"}], how_known: "Coder's reading of D lean."}
  reading: "As belief, not finding: no circle."
  notes: "Lane B separate from Lane A axis scores."

institutions:
  - {value: "Nikolayev Military Engineering Institute (Academy of Military Engineering), St. Petersburg", role: student, years: "1838–1843", kind: university, certainty: 1.0, cites: [{source: S1, locator: "'Background and early life'"}, {source: S4, locator: "infobox Education"}], how_known: "Britannica + Wikipedia EN."}
collaborators:
  - {value: "Mikhail Dostoyevsky", relation: family, note: "brother; co-publisher of Vremya / Epoch", certainty: 1.0, cites: [{source: S1, locator: "'Background and early life'"}, {source: S4, locator: "biography"}], how_known: "Britannica + Wikipedia EN."}
  - {value: "Anna Grigoryevna Snitkina (Dostoevskaya)", relation: family, note: "second wife; stenographer; managed publishing", certainty: 0.7, cites: [{source: S4, locator: "Second marriage"}], how_known: "Wikipedia EN."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 29"}], how_known: "Study roster."}
  controversies:
    - {value: "Antisemitism charges in Diary / correspondence; ethnic and political nationalism (Pan-Slavism)", certainty: 0.7, cites: [{source: S4, locator: "Ethnic beliefs / Political beliefs"}], how_known: "Wikipedia EN; not opened in primary this pass."}
  data_quality_flags:
    - "Wikiquote cites the Fonvisin letter as Letter XXI; the scan shows Letter XXII."
    - "Mayne gives Fonvisin as 'Beginning of March, 1854'; secondary sources say February or March."
    - "Brasol Diary accessed as archive.org OCR (djvu.txt); page numbers approximate from OCR headers."
    - "Pushkin speech also read via Kimball pedagogical web copy (S6); substance checked against Brasol OCR."
    - "Novel characters deliberately unused."
  open_questions:
    - "Scanlan Dostoevsky the Thinker late-notebook infinity→God / 'other world' argument — open scholarly edition for possible A ≤ 1 at reconstruction ceiling."
    - "Lantz English of full Diary or PSS critical edition page-check for Brasol OCR quotes."
    - "A clear own-voice locus ('where God is') or nature-order / miracle stance would reopen A or B."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Gary Saul Morson"
    citation: "Morson, Gary Saul. \"Fyodor Dostoyevsky.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Fyodor-Dostoyevsky."
    url: "https://www.britannica.com/biography/Fyodor-Dostoyevsky"
    accessed: 2026-10-24
    reliability_note: "Signed article body; AI boxes not used (P26)."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators]
  - id: S2
    type: primary
    kind: "scholarly edition"
    author: "Fyodor Dostoevsky; trans. Ethel Colburn Mayne"
    year: 1914
    citation: "Letters of Fyodor Michailovitch Dostoevsky to His Family and Friends. Trans. Ethel Colburn Mayne. London: Chatto & Windus, 1914. Scan: archive.org, lettersoffyodorm00dostuoft."
    url: "https://archive.org/details/lettersoffyodorm00dostuoft"
    accessed: 2026-10-24
    reliability_note: "Edited translation with chronology; library scan. Fonvisin Letter XXII; Osmidov Letter LXX (Feb 1878)."
    source_quality: "scholarly edition or monograph"
    used_for: [basics, contribution, worldview, timing, lane_b]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S4
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Fyodor Dostoevsky.\" https://en.wikipedia.org/wiki/Fyodor_Dostoevsky."
    url: "https://en.wikipedia.org/wiki/Fyodor_Dostoevsky"
    accessed: 2026-10-24
    reliability_note: "Used for dual-source bio, Works list, Religious beliefs summary (Wrangel; Orthodoxy). Contested claims (serf-murder story; antisemitism debates) flagged, not scored as worldview."
    source_quality: "other"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators, review]
  - id: S5
    type: primary
    kind: "scholarly edition"
    author: "Fyodor Dostoevsky; trans. Boris Brasol"
    year: 1949
    citation: "Dostoevsky, Fyodor. The Diary of a Writer. Trans. Boris Brasol. New York: Charles Scribner's Sons, 1949. Archive.org OCR: the-diary-of-a-writer (djvu.txt)."
    url: "https://archive.org/details/the-diary-of-a-writer"
    accessed: 2026-10-24
    reliability_note: "Published translation of his periodical nonfiction. OCR used for Old People, Arbitrary Assertions, miracles disclaimer, Pushkin speech, Gradovsky reply; locators approximate from OCR headers."
    source_quality: "archive scan (OCR only)"
    used_for: [contribution, worldview, timing]
  - id: S6
    type: secondary
    kind: "other"
    author: "Alan Kimball (ed.); Fyodor Dostoevsky"
    year: 1880
    citation: "Kimball, Alan. \"The Great Pushkin Celebration\" (English text of Dostoevsky's Pushkin speech and Gradovsky polemic). University of Oregon. https://pages.uoregon.edu/kimball/DstF.Puw.lct.htm."
    url: "https://pages.uoregon.edu/kimball/DstF.Puw.lct.htm"
    accessed: 2026-10-24
    reliability_note: "Pedagogical web edition of the speech also printed in Diary (S5); used as reading aid. Substance cross-checked against Brasol OCR."
    source_quality: "unofficial web copy"
    used_for: [worldview]
---

# Fyodor Dostoevsky

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Fyodor Dostoevsky (1821–1881), Russian novelist and journalist: Poor Folk (1846) through The Brothers Karamazov and the Pushkin speech (1880) [S1, S2, S4]. In 1854 he called himself 'a child of unfaith and scepticism' who would 'stay with Christ and not with truth' [S2]; in the Diary he published Christ-as-God-man reminiscence, immortality as the one sublime idea, and the Pushkin speech's Gospel of Christ [S5]. Deepen draft: CHRIST 0.7; A BELOW_THRESHOLD; B UNKNOWN; C 1 @ 0.5; D 1 @ 0.5; mid_basin UNKNOWN. Chart-moving: no (unplotted).

## Life and work

Military engineering academy; arrest 1849 and Siberian hard labour; novels, journals, and A Writer's Diary [S1, S4].

## Contribution and impact

Notes from Underground, Crime and Punishment, The Idiot, Demons, The Brothers Karamazov; wide influence on existentialism, psychology and religious thought [S1, S4].

## Childhood and education

Doctor's son in Orthodox piety; home and boarding schools; Nikolayev Military Engineering Institute [S1, S4].

## Adult working worldview

Christ-centred creed in private letters and published Diary nonfiction [S2, S5]. A: no locus statement (BELOW). B: no own-voice nature-order statement; refuses miracle declaration (UNKNOWN). C: immortality/God as moral necessity (1 @ 0.5). D: Christ preferred to 'truth'; spiritual enlightenment from Christ/Orthodoxy (1 @ 0.5). Characters unused.

## Heritage (context only)

Russian; Orthodox by birth [S1, S4].

## Timing

First lasting contribution 1846, at 25 [S2, S4]. Major-work period 1846–1880.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle [S2, S5].

## Open questions

- Scanlan notebook infinity→God for possible A.
- Critical-edition page-check of Brasol OCR.

## Research log

- 2026-10-15: Read Britannica and Mayne 1914 (archive.org OCR).
- 2026-10-24: Deepen D1 — Wikipedia EN; Brasol Diary OCR (Old People, Arbitrary Assertions, miracles disclaimer, Pushkin speech, Gradovsky reply); Osmidov letter in Mayne; Kimball Pushkin web copy. No fallacy_catalog.
