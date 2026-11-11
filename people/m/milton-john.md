---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA3)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to literature. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #180, F 3, rank 191). Hunt: corroborate A from in-span treatises / poet-voice; leave B UNKNOWN unless clear P16; De Doctrina Christiana not scored (authorship historically contested — Hunter 1990s; Campbell–Corns–Hale–Tweedie 2007 largely rehabilitated Miltonic provenance but debate not closed — Urban 2020; Clawson–Wilson 2022 Felbinger challenge). New own-voice A corroborators in-span: Areopagitica 1644 'God our deliverer' + 'high providence of God' (S4); PL Book 3 invocation (poet's voice, P42) 'God is light' / light at God's voice investing the rising world (S5; character dialogue after l.55 not scored); Sonnet 19 composed c.1652–55 'serve therewith my Maker' / 'Bear his mild yoke' (S6; published 1673). Dual bio P50 Britannica+Wikipedia. P47 source_quality on S1–S7. A support→corroborated; A stays 1 @0.5 (poetic/indirect); primary CHRIST @0.7 unchanged; B stays UNKNOWN (not a scientist; no clear own-voice P16 nature-order; do not force B from epic cosmology or Fallon monism readings). mid UNKNOWN unchanged; not plotted. Chart-moving NO. No fallacy_catalog. No figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Correction found while coding AA4: region_of_birth and region_of_work are Northern Europe, not Western Europe; the United Kingdom is M49 Northern Europe (P3, data/reference/regions.csv)."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA3, order P32: F 3, rank 191). Source: Britannica, signed by Albert C. Labriola (scholars edition, read in full). Lasting work: 'Lycidas' (published 1638; 'often considered the most outstanding example of the genre') and Paradise Lost ('widely regarded as the greatest epic poem in English', first published 1667); span 1638–1667 by publication (P30 #1), age 30. Own words: the opening invocation of Paradise Lost, Book 1, in the poet's own voice (not a character's, P42 addendum), read in the Dartmouth John Milton Reading Room (ed. Thomas H. Luxon): 'I may assert Eternal Providence, / And justifie the wayes of God to men'; within the span (1667). primary_system CHRIST 0.7 (written_profession), alt none at 0.7 (his anti-trinitarian leanings, per Labriola, stay within Christianity); A 1 at 0.5 (a creator Spirit who 'from the first / Wast present' and brooded on the Abyss, and an 'Eternal Providence': God beyond and acting on the world; poetic and indirect), alt 0; not a scientist, B UNKNOWN; C, D, E UNKNOWN; mid_basin UNKNOWN (A 1 at 0.5 and B UNKNOWN). Not plotted (B UNKNOWN). Draft, not reviewed."}

identity:
  id: milton-john
  display_name: "John Milton"
  roster:
    canonical_name: "John Milton"
    rank: 191
    F: 3
    models: [Claude, GPT, Grok]
    band: "core (3–4)"
    status: "core"
    field: "literature"
    field_bucket: "literature"
  full_name: {value: "John Milton", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S7, locator: "infobox"}], how_known: "Britannica + Wikipedia EN (P50 dual bio)."}
  native_name: {value: "John Milton", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  aliases:
    - {name: "John-Milton", kind: "roster alias"}

basics:
  birth:
    date: {value: "1608-12-09", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S7, locator: "infobox"}], how_known: "Britannica + Wikipedia EN."}
    place: {value: "London (Bread Street)", modern_name: "London, United Kingdom", polity_then: "Kingdom of England", certainty: 1.0, cites: [{source: S1, locator: "Introduction; Travel abroad"}, {source: S7, locator: "Early life"}], how_known: "Britannica + Wikipedia EN."}
  death:
    date: {value: "1674-11-08", certainty: 0.5, cites: [{source: S1, locator: "Introduction; later years"}, {source: S7, locator: "Death"}], how_known: "Britannica 'November 8?, 1674'; Wikipedia '9 or 10 November 1674' / infobox 9 Nov — date not settled at 1.0."}
    place: {value: "Bunhill Row, Middlesex (London)", modern_name: "London, United Kingdom", polity_then: "Kingdom of England", certainty: 0.7, cites: [{source: S7, locator: "Death / infobox"}], how_known: "Wikipedia: Bunhill Row; buried St Giles-without-Cripplegate."}
  first_lasting_contribution_year: {value: 1638, certainty: 0.7, cites: [{source: S1, locator: "Comus and Lycidas"}, {source: S7, locator: "Poetry"}], how_known: "'Lycidas', published 1638 in Justa Edouardo King Naufrago (S1, S7); publication (P30 #1)."}
  era_bucket: {value: "1600 to 1749", certainty: 1.0, cites: [{source: S1, locator: "Comus and Lycidas; Paradise Lost"}], how_known: "1638–1667 (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "United Kingdom (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S7, locator: "life"}], how_known: "London; Cambridge; Italian tour."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English", "Latin"], certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S7, locator: "Writing career"}], how_known: "Britannica + Wikipedia; also Greek, Hebrew, Italian, etc. (S7)."}
  occupations: {value: ["poet", "pamphleteer", "historian", "civil servant"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S7, locator: "lead"}], how_known: "Britannica + Wikipedia."}

contribution:
  primary_domain: literature
  fields: {value: ["poetry", "political and religious prose"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S7, locator: "lead"}], how_known: "Britannica + Wikipedia."}
  lasting_original_contributions:
    - {value: "Lycidas", year: 1638, kind: "work", lasting: "'often considered the most outstanding example of the genre'; with Comus, 'major literary achievements' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Comus and Lycidas"}, {source: S7, locator: "Poetry"}], how_known: "Britannica; Wikipedia; published 1638."}
    - {value: "Paradise Lost", year: 1667, kind: "work", lasting: "'widely regarded as the greatest epic poem in English' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Introduction; Paradise Lost"}, {source: S7, locator: "Paradise Lost"}], how_known: "Britannica; Wikipedia; first published in 10 books, 1667."}
  evidence_of_impact:
    - {value: "'Considered the most significant English author after William Shakespeare'; influence on the American and French revolutions", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  major_works:
    - {value: "Areopagitica", year: 1644, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "Tracts on education and free expression"}, {source: S4, locator: "title page 1644"}], how_known: "Britannica; Wikisource text."}
    - {value: "Paradise Regained and Samson Agonistes", year: 1671, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "Paradise Regained"}, {source: S7, locator: "Poetry"}], how_known: "Britannica; Wikipedia; published in one volume, 1671."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "The most significant English author after Shakespeare (S1).", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Protestant (father converted from Catholicism; disinherited for reading an English Bible)", certainty: 0.7, cites: [{source: S1, locator: "Early life and education"}, {source: S7, locator: "Early life and education"}], how_known: "Britannica + Wikipedia."}
  family_religious_practice: {value: UNKNOWN, how_known: "No household liturgy detail beyond father's Protestant conversion (S1, S7)."}
  parents_and_household:
    - {value: "Father John Milton (composer/scrivener), disinherited by devout Catholic grandfather Richard Milton for embracing Protestantism; mother Sarah Jeffrey", role: "family", certainty: 0.7, cites: [{source: S1, locator: "Early life and education"}, {source: S7, locator: "Early life and education"}], how_known: "Britannica + Wikipedia."}
  household_circumstances: {value: "Prosperous scrivener household in Bread Street, London; private tutor then St Paul's", certainty: 0.5, cites: [{source: S7, locator: "Early life and education"}], how_known: "Wikipedia."}
  schooling:
    - {value: "Private tutor Thomas Young (Scottish Presbyterian)", stage: "tutor", run_by: other, certainty: 0.7, cites: [{source: S1, locator: "Early life and education"}, {source: S7, locator: "Early life and education"}], how_known: "Britannica + Wikipedia."}
    - {value: "St Paul's School, London", stage: "grammar or secondary school", run_by: other, certainty: 0.7, cites: [{source: S1, locator: "Early life and education"}, {source: S7, locator: "Early life and education"}], how_known: "Britannica + Wikipedia."}
    - {value: "Christ's College, Cambridge (BA 1629, MA 1632)", stage: "university", run_by: other, certainty: 0.7, cites: [{source: S1, locator: "Early life and education"}, {source: S7, locator: "Early life and education"}], how_known: "Britannica + Wikipedia."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading:
    - {value: "Latin and Greek at St Paul's; intensive private study of theology, philosophy, history, literature after Cambridge", certainty: 0.5, cites: [{source: S7, locator: "Study, poetry, and travel"}], how_known: "Wikipedia."}
  childhood_mentors:
    - {value: "Thomas Young", role: "tutor", certainty: 0.7, cites: [{source: S1, locator: "Early life and education"}, {source: S7, locator: "Early life"}], how_known: "Britannica + Wikipedia."}
  languages_in_childhood: {value: ["English", "Latin", "Greek"], certainty: 0.5, cites: [{source: S7, locator: "Early life and education"}], how_known: "Wikipedia: St Paul's Latin and Greek."}
  notable_events:
    - {value: "Italian tour 1638–1639; met Galileo under house arrest at Arcetri (later recalled in Areopagitica)", certainty: 0.7, cites: [{source: S4, locator: "Galileo passage"}, {source: S7, locator: "Study, poetry, and travel"}], how_known: "Areopagitica own words; Wikipedia."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1638–1667", certainty: 0.7, cites: [{source: S1, locator: "Comus and Lycidas; Paradise Lost"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Protestant / Puritan Independent (anti-episcopal; later apart from all sects)", certainty: 0.5, cites: [{source: S1, locator: "theology"}, {source: S7, locator: "Theology"}], how_known: "Secondary summaries; not a scored code."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No scored own-voice science–religion relation statement read this pass."}
  primary_system:
    value: CHRIST
    basis: written_profession
    certainty: 0.7
    cites: [{source: S2, locator: "Book 1, lines 17–26"}, {source: S4, locator: "God our deliverer; high providence"}, {source: S5, locator: "Book 3 invocation ll. 1–55"}, {source: S6, locator: "Sonnet 19 Maker / yoke"}]
    how_known: "Multiple in-span own-voice professions: PL Book 1 and Book 3 invocations (poet's voice, P42); Areopagitica 1644; Sonnet 19. Heterodox leanings (anti-trinitarian tendency per Labriola on De Doctrina — authorship contested, not scored) stay within CHRIST."
    rationale: "Christian creator-providence God and Maker whom he serves (S2, S4, S5, S6). No alternative system at 0.7."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Coded at 0.7: PL invocations, Areopagitica, Sonnet 19."}
  lio_axes:
    A_locus:
      value: 1
      basis: written_profession
      certainty: 0.5
      cites: [{source: S2, locator: "Book 1, lines 17–26"}, {source: S4, locator: "high providence of God"}, {source: S5, locator: "Book 3 invocation ll. 1–12"}, {source: S6, locator: "my Maker"}]
      support: corroborated
      how_known: "Four independent in-span own-voice streams agree on a creator/providence God distinct from and acting on the world (S2, S4, S5, S6). Certainty stays 0.5: verse and providence language are poetic/indirect. P48 corroborated. De Doctrina not cited (authorship contested)."
      rationale: "Spirit brooding on the Abyss and Eternal Providence (S2); high providence of God who pours out desirable things (S4); holy light at the voice of God investing the rising world, since God is light (S5); personal Maker and mild yoke (S6): A 1. Alternative 0: providence read as wholly transcendent rule."
      alternatives:
        - {value: 0, note: "Providence as wholly transcendent rule (S2, S4).", cites: [{source: S2, locator: "Book 1, line 25"}, {source: S4, locator: "high providence"}]}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30). No clear own-voice P16 nature-order statement. Do not force B from epic cosmology, character speech in Paradise Lost (P42), or secondary Fallon monism / animist-materialism readings. De Doctrina creation ex Deo not scored (authorship contested)."}
    C_ledger: {value: UNKNOWN, how_known: "Lead: Lycidas St Peter retributive justice (S1); PL theodicy themes — not scored this pass."}
    D_authority: {value: UNKNOWN, how_known: "Lead: Areopagitica conscience / Scripture primacy (S1, S4); not scored this pass."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is 1 only at 0.5 and B_cause is UNKNOWN, so the P4 test cannot be completed."}
  statements:
    - text: >-
        And chiefly Thou O Spirit, that dost prefer / Before all Temples th' upright heart and pure, /
        Instruct me, for Thou know'st; Thou from the first / Wast present, and with mighty wings outspread /
        Dove-like satst brooding on the vast Abyss / And mad'st it pregnant: What in me is dark /
        Illumin, what is low raise and support; / That to the highth of this great Argument /
        I may assert Eternal Providence, / And justifie the wayes of God to men.
      cites: [{source: S2, locator: "Book 1, lines 17–26"}]
      date: "1667"
      context: "Paradise Lost, Book 1, opening invocation; first published 1667 (edition follows 1674 text, same lines)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "Poet's own voice, not a character's (P42 addendum). Dartmouth Reading Room, ed. Luxon."
    - text: >-
        it will bee attributed first, as is most due, to the strong assistance of God our deliverer,
        next to your faithfull guidance and undaunted Wisdome, Lords and Commons of England.
      cites: [{source: S4, locator: "opening address"}]
      date: "1644"
      context: "Areopagitica; published November 1644; in-span prose treatise in his own name."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Independent of Paradise Lost verse. Corroborates CHRIST and a personal intervening God."
    - text: >-
        This justifies the high providence of God, who though he command us temperance, justice,
        continence, yet powrs out before us ev'n to a profusenes all desirable things, and gives us
        minds that can wander beyond all limit and satiety.
      cites: [{source: S4, locator: "high providence of God"}]
      date: "1644"
      context: "Areopagitica, argument that God leaves choice and trial rather than removing occasions of sin."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Explicit 'providence of God' in prose. P48 corroborator for A 1."
    - text: >-
        Hail holy light, ofspring of Heav'n first-born, / Or of th' Eternal Coeternal beam /
        May I express thee unblam'd? since God is light, / And never but in unapproached light /
        Dwelt from Eternitie, dwelt then in thee, / Bright effluence of bright essence increate. /
        ... before the Sun, / Before the Heavens thou wert, and at the voice / Of God, as with a Mantle
        didst invest / The rising world of waters dark and deep, / Won from the void and formless infinite.
      cites: [{source: S5, locator: "Book 3, lines 1–12"}]
      date: "1667"
      context: "Paradise Lost, Book 3, opening invocation in the poet's own voice (blindness passage follows); character dialogue of Father and Son begins after line 55 and is not scored (P42)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Poet-voice only. Creator God whose voice orders the rising world."
    - text: >-
        When I consider how my light is spent, / E're half my days, in this dark world and wide, /
        And that one Talent which is death to hide, / Lodg'd with me useless, though my Soul more bent /
        To serve therewith my Maker, and present / My true account, least he returning chide, /
        Doth God exact day labour, light deny'd, / I fondly ask; But patience to prevent /
        That murmur, soon replies, God doth not need / Either man's work or his own gifts, who best /
        Bear his milde yoak, they serve him best...
      cites: [{source: S6, locator: "Sonnet 19 full text"}]
      date: "1655"
      context: "Sonnet on his blindness; composed after total blindness (1652), typically dated mid-1650s (here 1655 as midpoint of usual range); first printed Poems 1673. Own lyric voice."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Composition in-span; publication after span end 1667. Personal Maker / God — not epic character speech."
  changes_over_life: []
  coder_notes: "D1 2026-10-24: A corroborated from Areopagitica + PL Book 3 poet-voice + Sonnet 19; De Doctrina left unscored (authorship contested). B not forced from Fallon monism or PL cosmology. Chart-moving NO. No fallacy_catalog; figures/ untouched."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English", certainty: 0.5, cites: [{source: S7, locator: "Early life"}], how_known: "Wikipedia; London birth."}
  religious_heritage_by_birth: {value: "Protestant (father converted from Catholicism)", certainty: 0.7, cites: [{source: S1, locator: "Early life and education"}, {source: S7, locator: "Early life and education"}], how_known: "Britannica + Wikipedia. Heritage only — never a worldview code."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated in sources read."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated; Anglican/Cambridge priestly path abandoned (S7)."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1638–1667", certainty: 0.7, cites: [{source: S1, locator: "Comus and Lycidas; Paradise Lost"}], how_known: "From Lycidas (1638) to Paradise Lost (1667), the listed lasting works (P29, P30 #1)."}
  age_at_first_lasting_contribution: {value: 30, certainty: 0.7, cites: [{source: S1, locator: "Introduction; Comus and Lycidas"}], how_known: "1638 − 1608 = 30 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: "1644", certainty: 0.7, cites: [{source: S4, locator: "Areopagitica"}], how_known: "Earliest dated in-span prose profession of providence/God scored this pass (Areopagitica). PL Book 1 is 1667; Sonnet 19 composed mid-1650s."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S4, locator: "1644"}, {source: S2, locator: "1667"}, {source: S6, locator: "c.1652–55"}], how_known: "Areopagitica, Sonnet 19 composition, and PL invocations all fall in or at the end of 1638–1667."}
  worldview_during_major_work: {value: "CHRIST with A 1 (providence/creator God), evidenced in-span", certainty: 0.5, cites: [{source: S2, locator: "PL Book 1"}, {source: S4, locator: "Areopagitica"}], how_known: "Coded from in-span own words; certainty follows A (0.5)."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Epic and polemic, not geometric argument (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "Do not invent B from Paradise Lost cosmology or from secondary monism readings. Character speech is not the poet (P42)."
  notes: "De Doctrina Christiana authorship contested — not used for Lane B."

institutions:
  - {value: "Council of State of the Commonwealth", role: "secretary for foreign tongues (Latin secretary)", years: "1649–1660", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "Antimonarchical tracts"}, {source: S7, locator: "Secretary for Foreign Tongues"}], how_known: "Britannica + Wikipedia; end year the Restoration."}
  - {value: "Christ's College, Cambridge", role: "student (BA, MA)", years: "1625–1632", kind: "university", certainty: 0.7, cites: [{source: S7, locator: "Early life and education"}], how_known: "Wikipedia."}
collaborators:
  - {value: "Andrew Marvell", relation: "collaborator", note: "assisted him as Latin secretary; wrote prefatory verses for PL 1674", certainty: 0.7, cites: [{source: S1, locator: "Fame and reputation"}, {source: S7, locator: "Secretary for Foreign Tongues"}], how_known: "Britannica + Wikipedia."}
  - {value: "Thomas Young", relation: "teacher", note: "Presbyterian tutor; later Smectymnuus", certainty: 0.7, cites: [{source: S1, locator: "Early life and education"}, {source: S7, locator: "Early life"}], how_known: "Britannica + Wikipedia."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 191"}], how_known: "Study roster."}
  controversies:
    - {value: "De Doctrina Christiana authorship: Hunter challenged Miltonic authorship (1990s); Campbell–Corns–Hale–Tweedie 2007 largely rehabilitated it; later scholars (Urban 2020; Clawson–Wilson 2022) reopen caution. Not used to score A or B this pass.", certainty: 0.5, cites: [{source: S1, locator: "theology"}, {source: S7, locator: "Views / De doctrina"}], how_known: "Create note + Wikipedia + deepen research."}
  data_quality_flags:
    - "Scored verse lines are poet-voice invocations or lyric (P42); PL Book 3 Father/Son dialogue not scored."
    - "Sonnet 19 composed in-span, published 1673 (after span end)."
    - "Death day uncertain (8–10 Nov 1674)."
  open_questions:
    - "Whether a future pass should score D from Areopagitica conscience / Scripture lines."
    - "Stable scholarly consensus on De Doctrina for optional lead-only theology notes."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Albert C. Labriola"
    citation: "Labriola, Albert C. 'John Milton.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/John-Milton/108731"
    url: "https://kids.britannica.com/scholars/article/John-Milton/108731"
    accessed: 2026-10-19
    reliability_note: "Signed article, read in full at create; re-used D1 for bio."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators]
  - id: S2
    type: primary
    kind: "scholarly edition"
    author: "John Milton (ed. Thomas H. Luxon)"
    citation: "Milton, John. Paradise Lost, Book 1 (1667; 1674 text). The John Milton Reading Room, ed. Thomas H. Luxon, Dartmouth College. https://milton.host.dartmouth.edu/reading_room/pl/book_1/text.shtml"
    url: "https://milton.host.dartmouth.edu/reading_room/pl/book_1/text.shtml"
    accessed: 2026-10-19
    reliability_note: "Edited scholarly online text; Book 1 opening read."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview]
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
    type: primary
    kind: "published work by the subject"
    author: "John Milton"
    citation: "Milton, John. Areopagitica (1644). Wikisource transcription. https://en.wikisource.org/wiki/Areopagitica_(1644)"
    url: "https://en.wikisource.org/wiki/Areopagitica_(1644)"
    accessed: 2026-10-24
    reliability_note: "Own prose treatise, November 1644; 'God our deliverer' and 'high providence of God' verified against Wikisource text."
    source_quality: "primary / own words"
    used_for: [worldview, contribution, childhood]
  - id: S5
    type: primary
    kind: "scholarly edition"
    author: "John Milton (ed. Thomas H. Luxon)"
    citation: "Milton, John. Paradise Lost, Book 3 (1667; 1674 text). The John Milton Reading Room, ed. Thomas H. Luxon, Dartmouth College. https://milton.host.dartmouth.edu/reading_room/pl/book_3/text.shtml"
    url: "https://milton.host.dartmouth.edu/reading_room/pl/book_3/text.shtml"
    accessed: 2026-10-24
    reliability_note: "Book 3 invocation (poet's voice) read; Father/Son dialogue after l.55 not used for scoring (P42)."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview]
  - id: S6
    type: primary
    kind: "scholarly edition"
    author: "John Milton (ed. Thomas H. Luxon)"
    citation: "Milton, John. Sonnet 19 ('When I consider how my light is spent'), composed c.1652–55; Poems 1673. The John Milton Reading Room. https://milton.host.dartmouth.edu/reading_room/sonnets/sonnet_19/text.shtml"
    url: "https://milton.host.dartmouth.edu/reading_room/sonnets/sonnet_19/text.shtml"
    accessed: 2026-10-24
    reliability_note: "Own lyric; composition in-span; first print 1673."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, timing]
  - id: S7
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "'John Milton.' Wikipedia (English). https://en.wikipedia.org/wiki/John_Milton"
    url: "https://en.wikipedia.org/wiki/John_Milton"
    accessed: 2026-10-24
    reliability_note: "P50 dual bio with S1. Early life, career, death place, De Doctrina note, theology overview."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, heritage, institutions, collaborators, review]
---

## Summary

John Milton (1608–1674), poet and pamphleteer [S1, S7]. Deepen D1: CHRIST @0.7; A 1 @0.5 corroborated; B UNKNOWN. Not plotted.

## Life and work

London; Cambridge; Italy; Commonwealth Latin secretary; blindness by 1652; Paradise Lost 1667 [S1, S7]. Died Bunhill Row 1674 [S7].

## Contribution and impact

Lycidas (1638); Areopagitica (1644); Paradise Lost (1667) [S1, S4, S7].

## Childhood and education

Protestant scrivener household; tutor Young; St Paul's; Christ's College Cambridge [S1, S7].

## Adult working worldview

In-span own voice: PL Book 1 and Book 3 invocations (poet's voice); Areopagitica providence; Sonnet 19 Maker [S2, S4, S5, S6]. De Doctrina not scored (authorship contested). B not opened.

## Heritage (context only)

Protestant (father converted from Catholicism) [S1, S7]. Context only.

## Timing

1638–1667, age 30 [S1]. LIO-type views during major work (1644 onward).

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No B from epic cosmology.

## Open questions

- Score D from Areopagitica?
- De Doctrina consensus for lead-only notes?

## Research log

- 2026-10-24 (D1): Areopagitica Wikisource (S4); PL Book 3 Dartmouth (S5); Sonnet 19 Dartmouth (S6); Wikipedia dual bio (S7). De Doctrina left unscored. A support→corroborated. Chart-moving NO. No fallacy_catalog; no figures/.
- 2026-10-19: Correction found while coding AA4: region_of_birth and region_of_work are Northern Europe, not Western Europe; the United Kingdom is M49 Northern Europe (P3, data/reference/regions.csv).
- 2026-10-19: Read Britannica (Labriola); Paradise Lost Book 1 (Dartmouth).
