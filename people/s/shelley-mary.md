---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA7; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to literature. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA7, order P32: F 3, rank 205). Source: Britannica, signed by René Ostberg and Kathleen Kuiper (scholars edition, read in full). Lasting work: Frankenstein; or, The Modern Prometheus (January 1818), 'a seminal work of Romanticism and a Gothic horror classic that is also considered to be one of the first science-fiction novels'; its 'subsequent influence on literature and popular culture cannot be overstated' (S1). Span 1818, age 21 (P30 year difference; S1's 'Only 20 years old' at publication is her exact age, kept as a note). Worldview: no own words on belief read; daughter of the radical philosopher William Godwin and Mary Wollstonecraft (S1); her husband was expelled from Oxford over a pamphlet 'endorsing atheism' (S1), a fact about him, not her. primary_system UNKNOWN; A UNKNOWN; not a scientist; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #193/228, F3 rank 205). Goals: letters/journals own words if any; keep silence if none; do not force plot from Frankenstein theology. Dual bio Wikipedia EN (S3, P50). Scholarly: Airey Religion Around Mary Shelley via Acosta NCGS review (S4) — never held an atheist position; early works (Frankenstein, Last Man) explore absence/malevolence of God as fiction themes; later Christian domesticity. Hogsette Christianity & Literature 2011 (S5) quotes Jones Journal: Dec 1822 'I trust in a hereafter—I have ever done so'; Oct 1822 Power that rules / Providence; Dante 1822 thank-God / Thy-will musing; 5 Oct 1839 'The God that made this beautiful world… beneficent and gentle Power' (all after 1818 span). 1831 Frankenstein Intro 'Creator of the world' / invention-vs-creation is authorial after-span literary framing — not used to score axes. Novel character/theology unused (P42). Archive.org Jones Journal OCR opened for 1814–early London entries — no in-span (1818) first-person creed found; May 1815–July 1816 journal volume lost (Jones preface). Parents' radicalism and Percy's atheist pamphlet remain context (S1). Children's baptism St Giles-in-the-Fields 9 Mar 1818 and her marriage at St Mildred's 30 Dec 1816 are practice/legal facts, not adult creed (S3; Exploring London S6). primary_system UNKNOWN→BELOW_THRESHOLD (leads CLTHEI from after-span journals; CHRIST/DEISM/ATHE leads only; P19). A UNKNOWN→BELOW_THRESHOLD (personal-God / hereafter leads after-span at most A 0 @0.5 — do not force for 1818 span; Joyce/Proust pattern). B stays UNKNOWN (not a scientist; P16/P30). C/D/E UNKNOWN; mid_basin UNKNOWN. Not plotted. Chart-moving NO. P47 source_quality S1–S7. No fallacy_catalog. No figures/. Draft, not reviewed."}

identity:
  id: shelley-mary
  display_name: "Mary Shelley"
  roster:
    canonical_name: "Mary Shelley"
    rank: 205
    F: 3
    models: [Gemini, GPT, Grok]
    band: "core (3–4)"
    status: "core"
    field: "literature"
    field_bucket: "literature"
  full_name: {value: "Mary Wollstonecraft Shelley", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S3, locator: "lede"}], how_known: "Britannica + Wikipedia; née Mary Wollstonecraft Godwin."}
  native_name: {value: "Mary Wollstonecraft Shelley", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  aliases:
    - {name: "Mary-Shelley", kind: "roster alias"}
    - {name: "Shelley-Mary", kind: "roster alias"}
    - {name: "Mary Wollstonecraft Godwin", kind: "birth name"}

basics:
  birth:
    date: {value: "1797-08-30", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S3, locator: "infobox"}], how_known: "Britannica + Wikipedia."}
    place: {value: "London", modern_name: "London, United Kingdom", polity_then: "Kingdom of Great Britain", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S3, locator: "Early life"}], how_known: "Somers Town, London (S3)."}
  death:
    date: {value: "1851-02-01", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S3, locator: "infobox"}], how_known: "Britannica + Wikipedia."}
    place: {value: "London", modern_name: "London, United Kingdom", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S3, locator: "Final years"}], how_known: "Chester Square (S3)."}
  first_lasting_contribution_year: {value: 1818, certainty: 0.7, cites: [{source: S1, locator: "Publishing Frankenstein"}, {source: S3, locator: "Bath and Marlow"}], how_known: "Frankenstein published January 1818 (S1); publication (P30)."}
  era_bucket: {value: "1750 to 1849", certainty: 1.0, cites: [{source: S1, locator: "Publishing Frankenstein"}], how_known: "1818 (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "United Kingdom (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.5, cites: [{source: S1, locator: "The 'haunted summer' of 1816; Publishing Frankenstein"}, {source: S3, locator: "Lake Geneva"}], how_known: "Begun at Cologny near Geneva (1816), finished and published in England (1817–18); alternative Western Europe (Switzerland)."}
  sex_as_recorded: {value: "female", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "English novels."}
  occupations: {value: ["novelist", "editor", "travel writer"], certainty: 0.7, cites: [{source: S1, locator: "Introduction; Later life and other works"}, {source: S3, locator: "lede"}], how_known: "Britannica + Wikipedia."}

contribution:
  primary_domain: literature
  fields: {value: ["literature"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Frankenstein; or, The Modern Prometheus", year: 1818, kind: "work", lasting: "'a seminal work of Romanticism and a Gothic horror classic that is also considered to be one of the first science-fiction novels'; 'Frankenstein's subsequent influence on literature and popular culture cannot be overstated' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Introduction; Death and legacy"}, {source: S3, locator: "lede"}], how_known: "Britannica + Wikipedia."}
  evidence_of_impact:
    - {value: "Influence of Frankenstein on literature, film and popular culture", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Death and legacy"}, {source: S3, locator: "Reputation"}], how_known: "Britannica + Wikipedia."}
  major_works:
    - {value: "History of a Six Weeks' Tour (with Percy Shelley)", year: 1817, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "The 'haunted summer' of 1816"}], how_known: "Britannica."}
    - {value: "The Last Man", year: 1826, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "Later life and other works"}, {source: S3, locator: "Selected works"}], how_known: "Britannica: 'often ranked as her best work'."}
    - {value: "Percy Bysshe Shelley, Poetical Works (editor)", year: 1839, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "Later life and other works"}], how_known: "Britannica."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Author of a seminal Romantic novel and early science fiction (S1).", certainty: 0.7, cites: [{source: S1, locator: "Death and legacy"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Father from English Dissenting line; later atheist then vaguely theist (Coleridge influence). Mother Anglican background / rational-dissent circle. Household was radical-intellectual, not orthodox church practice.", certainty: 0.5, cites: [{source: S3, locator: "Early life"}, {source: S4, locator: "ch. 2 summary"}, {source: S5, locator: "Godwin theism via Coleridge"}], how_known: "Wikipedia + Airey review + Hogsette on Godwin; heritage context only."}
  family_religious_practice: {value: UNKNOWN, how_known: "No regular family worship described in sources read."}
  parents_and_household:
    - {value: "Father William Godwin, radical philosopher; mother Mary Wollstonecraft, feminist writer, who died 11 days after her birth; stepmother Mary Jane Clairmont from 1801", role: "family", certainty: 0.7, cites: [{source: S1, locator: "Early life and intellectual upbringing"}, {source: S3, locator: "Early life"}], how_known: "Britannica + Wikipedia."}
  household_circumstances: {value: "Godwin often in debt; Juvenile Library with stepmother; rich informal education among visitors (Coleridge, Burr)", certainty: 0.5, cites: [{source: S3, locator: "Early life"}], how_known: "Wikipedia."}
  schooling:
    - {value: "Little formal education; governess and daily tutor; six months Ramsgate boarding school (1811); two stays with Baxter family near Dundee (1812–14)", certainty: 0.7, cites: [{source: S1, locator: "Early life and intellectual upbringing"}, {source: S3, locator: "Early life"}], how_known: "Britannica + Wikipedia."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure:
    - {value: "Davy chemistry lectures / Elements of Chemical Philosophy in reading circle (vitalism–materialism context for Frankenstein)", certainty: 0.5, cites: [{source: S5, locator: "Davy / journals Jones 67–68, 73"}], how_known: "Hogsette citing Jones Journal; secondary."}
  key_early_reading:
    - {value: "Mother's works; father's library; Coleridge; Milton Paradise Lost; Volney Ruins (early novel influences)", certainty: 0.5, cites: [{source: S3, locator: "Early life"}, {source: S4, locator: "ch. 2"}], how_known: "Wikipedia + Airey review."}
  childhood_mentors: []
  languages_in_childhood: {value: ["English"], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Inferred; later Greek study noted in journals (S7)."}
  notable_events:
    - {value: "Mother died of puerperal fever 11 days after Mary's birth (10 Sept 1797)", certainty: 0.7, cites: [{source: S1, locator: "Early life"}, {source: S3, locator: "Early life"}], how_known: "Britannica + Wikipedia."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1818", certainty: 0.7, cites: [{source: S1, locator: "Publishing Frankenstein"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "1831 Intro discusses principle of life / galvanism as literary origin story (S3); not a scored science–religion equation. Novel theology unused (P42)."}
  primary_system:
    value: BELOW_THRESHOLD
    how_known: "No in-span (1818) first-person creed found in journals/letters opened this pass (Jones Journal volume covering May 1815–July 1816 lost — S7 preface; 1818 entries largely factual). After-span journals (Jones via Hogsette S5): Dec 1822 hereafter trust 'I have ever done so'; Oct 1822 Power that rules human affairs; 5 Oct 1839 God who made the world / 'beneficent and gentle Power' — personal-God / hereafter leads (CLTHEI lead) under P20/P31, not enough to pin a code for the 1818 working year without overclaim (P19). Airey (S4): never atheist; early fiction explores divine absence/malevolence — fiction unused (P42). Parents' radicalism and Percy's atheist pamphlet are context, not her profession (S1). Marriage/children's baptisms are practice/legal, not creed (S3, S6)."
    note: "Named alternatives CLTHEI / CHRIST / DEISM / ATHE stay leads only. Frankenstein unused (P42)."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: CLTHEI, reason: "Lead: after-span journals name God / beneficent Power, Providence, hereafter reunion with Percy (S5). Cap below 0.5 for 1818 span (after-span + no in-span creed; P19/P20)."}
    - {code: CHRIST, reason: "Lead only from later 'Christian domesticity' scholarly reading (S4) and children's 1818 baptism / her 1816 church marriage (S3, S6) — practice/legal and secondary label, not adult written profession of Christ/Trinity/church."}
    - {code: DEISM, reason: "Weaker lead: creator-distinct language in 1831 Intro (S3) could fit thin creator; after-span Providence and personal hereafter pull against classic non-intervening deism."}
    - {code: ATHE, reason: "Rejected as primary: Airey states she never held an atheist position (S4); husband's atheism is his, not hers (S1). Fiction exploring absent/malevolent deity unused (P42)."}
  lio_axes:
    A_locus:
      value: BELOW_THRESHOLD
      how_known: "After-span journal 'God that made this beautiful world' / 'beneficent and gentle Power' (1839) and Providence / thank-God lines (1822) are personal-God leads (at most A 0 @0.5 after-span with BELOW alt) — not forced onto the 1818 span (P19; Joyce/Proust pattern). No in-span first-person God locus or denial. Frankenstein Creator/creature theology is novel/character (P42 unused). 1831 Intro 'Creator of the world' is after-span literary framing, not scored as A."
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30). No own-voice P16 exceptionless-nature / law-and-exception profession read. Vitalism–materialism context and 1831 Intro 'vital warmth' are literary/scientific-discussion report, not scored as B. Do not force B from Frankenstein (P42)."}
    C_ledger: {value: UNKNOWN, how_known: "Dec 1822 'I trust in a hereafter—I have ever done so' (S5) is a strong afterlife lead (after-span); not scored as C for the 1818 working year (P19/P20). Novel afterlife speech unused (P42)."}
    D_authority: {value: UNKNOWN, how_known: "Oct 1838 journal on not being a person of reforming opinions / speaking when it will benefit (S5) is political silence, not a scored religious-authority axis."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "B is UNKNOWN, which takes precedence (P19); A is BELOW_THRESHOLD."}
  statements:
    - text: "I trust in a hereafter—I have ever done so. I know that it shall be mine—even with thee, glorious spirit! Who surely lookest on, pitiest, and lovest thy Mary."
      cites: [{source: S5, locator: "Jones 186 (Dec 1822)"}]
      date: "1822-12"
      context: "Journal after Percy Shelley's death (July 1822). After span (major_work_period 1818). Claims lifelong continuity ('I have ever done so') — P31 lead only, not used to force C or primary for 1818."
      axes: [C_ledger, A_locus]
      kind: "notebook or diary"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "English as Hogsette quotes Jones. Feldman/Scott-Kilvert print unread."
    - text: "The God that made this beautiful world (and I was then at Lerici, surrounded by the most beautiful manifestation of the visible creation) made that into which I go; as there is beauty and love here, such is there, and I felt as if my spirit would when it left my frame be received and sustained by a beneficent and gentle Power."
      cites: [{source: S5, locator: "Jones 208 (5 Oct 1839)"}]
      date: "1839-10-05"
      context: "Journal reflecting on near-death. Long after span. Clearest personal-God / hereafter own words found this pass."
      axes: [A_locus, C_ledger]
      kind: "notebook or diary"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "English as Hogsette quotes Jones. Elsewhere Mag reprint of Life and Letters agrees on wording (spot-check)."
    - text: "They say that Providence is shown by the extraction that may be ever made of good from evil… So I am to thank God for making me weak. I might say, 'Thy will be done,' but I cannot applaud the permitter of self-degradation…"
      cites: [{source: S5, locator: "Jones 168 (1822, after reading Dante)"}]
      date: "1822"
      context: "Journal after reading Dante. After span. Struggles with providential theodicy without denying Providence/God."
      axes: [A_locus]
      kind: "notebook or diary"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "English as Hogsette quotes Jones."
    - text: "Frightful must it be; for supremely frightful would be the effect of any human endeavour to mock the stupendous mechanism of the Creator of the world."
      cites: [{source: S3, locator: "1831 Introduction quotation"}]
      date: "1831"
      context: "Author's Introduction to the 1831 Frankenstein. After span. Literary framing of the waking-dream origin; not used to score A (authorial rhetoric, not a creed; P42-adjacent)."
      axes: []
      kind: "other"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Unused for axes; recorded to document the hunt."
  changes_over_life:
    - {value: "Scholarly arc (Airey): early fiction explores divine absence/malevolence; later domestic devotion/charity. After-span journals (1822–1839) affirm God, Providence, hereafter (S5). Early novels unused for Lane A (P42). Not a scored change forcing an 1818 code.", year: 1822, age: 25, certainty: 0.5, cites: [{source: S4, locator: "ch. 2–5 summary"}, {source: S5, locator: "journal cluster"}], how_known: "Secondary scholarly reading + after-span journals."}
  coder_notes: "Deepen D1 2026-10-24: queue need was A/B UNKNOWN with only Britannica. Own-words hunt found after-span Jones Journal quotes via Hogsette (S5) and Airey never-atheist (S4). In-span silence + lost 1815–16 journal + P42 bar on Frankenstein → UNKNOWN→BELOW on primary and A (Proust/Joyce pattern); do not force CLTHEI/A0 for 1818 from 1822–39 journals alone. B left UNKNOWN (P16/P30). Parents' and Percy's beliefs stay context. Feldman/Scott-Kilvert Journals and Bennett Selected Letters print unread (secondary quotations only). Lane A separate from Lane B. No fallacy_catalog (Jason)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English", certainty: 0.5, cites: [{source: S3, locator: "Early life"}], how_known: "Wikipedia; not further specified."}
  religious_heritage_by_birth: {value: "Radical Dissenting / post-Christian intellectual household (Godwin); mother from Anglican / rational-dissent milieu", certainty: 0.5, cites: [{source: S3, locator: "Early life"}, {source: S4, locator: "ch. 2"}], how_known: "Wikipedia + Airey review. Heritage only."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Her own infant baptism not stated in sources read. Children William and Clara (and Allegra) baptized at St Giles-in-the-Fields 9 March 1818 (S6) — their rite, not hers."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated; Godwin wished her raised 'like a philosopher, even like a cynic' (S3)."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1818", certainty: 0.7, cites: [{source: S1, locator: "Publishing Frankenstein"}], how_known: "The one listed lasting item (P29, P30)."}
  age_at_first_lasting_contribution: {value: 21, certainty: 0.7, cites: [{source: S1, locator: "Introduction; Publishing Frankenstein"}], how_known: "1818 − 1797 = 21 (P30 year difference); S1 notes she was 20 at publication in January 1818."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No axis scored at 3 or 4 (P27 anchor); after-span journal leads only."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "A BELOW_THRESHOLD; B UNKNOWN. Densest God/hereafter own words are 1822–1839 (after major work).", certainty: 0.5, cites: [{source: S5, locator: "Jones 168, 186, 208"}], how_known: "Coder's reading."}
  worldview_during_major_work: {value: "No in-span first-person creed found; parents' radicalism and husband's atheism are context; Frankenstein theology is fiction (P42 unused)", certainty: 0.5, cites: [{source: S1, locator: "text"}, {source: S7, locator: "lost 1815–16 volume"}, {source: S4, locator: "never atheist"}], how_known: "Silence / BELOW for scored axes (P19)."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Gothic / early science-fiction novel (S1); not a scored cosmology of nature.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable to a scored LIO form."}
  circle_present: {value: "unclear", rationale: "Not assessed as Lane B geometry.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No scored Lane A axes. Novel Creator/creature allegory stays outside Lane A (P42)."
  notes: "P42: character speech and novel theology out. Do not invent B from galvanism / vitalism plot."

institutions: []
collaborators:
  - {value: "Percy Bysshe Shelley", relation: "family", note: "husband; collaborator on History of a Six Weeks' Tour; edited his works; his atheism is his, not hers", certainty: 0.7, cites: [{source: S1, locator: "Relationship with Percy Bysshe Shelley; Later life and other works"}, {source: S3, locator: "lede"}], how_known: "Britannica + Wikipedia."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 205"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Worldview: in-span silence; after-span journals via secondary quotation (Jones via Hogsette); Feldman/Scott-Kilvert and Bennett Letters print unread."
    - "May 1815–July 1816 journal volume lost (Jones preface)."
    - "Frankenstein theology unused (P42)."
  open_questions:
    - "Any 1816–1818 letter with first-person God/hereafter profession (Bennett Selected Letters print unread)."
    - "Feldman and Scott-Kilvert Journals full check of 1817–1819 for creed lines beyond Hogsette cluster."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "René Ostberg; Kathleen Kuiper"
    citation: "Ostberg, René, and Kathleen Kuiper. 'Mary Wollstonecraft Shelley.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/Mary-Wollstonecraft-Shelley/67263"
    url: "https://kids.britannica.com/scholars/article/Mary-Wollstonecraft-Shelley/67263"
    accessed: 2026-10-19
    reliability_note: "Signed article, scholars edition, read in full at create; re-used D1 for bio."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, timing, collaborators]
  - id: S2
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [review]
  - id: S3
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "Wikipedia. 'Mary Shelley' (English). https://en.wikipedia.org/wiki/Mary_Shelley"
    url: "https://en.wikipedia.org/wiki/Mary_Shelley"
    accessed: 2026-10-24
    reliability_note: "Dual-bio check against Britannica (P50). Agrees on birth 30 Aug 1797 London, death 1 Feb 1851 London, Frankenstein Jan 1818, parents Godwin/Wollstonecraft, marriage 30 Dec 1816 St Mildred's. Adds 1831 Intro Creator quotation and editorial work on Percy. Not used alone for worldview codes."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, heritage, timing, collaborators]
  - id: S4
    type: secondary
    kind: "other"
    author: "Ana M. Acosta (reviewing Jennifer L. Airey)"
    citation: "Acosta, Ana M. Review of Jennifer L. Airey, Religion Around Mary Shelley. Nineteenth-Century Gender Studies 16.2 (Summer 2020). https://www.ncgsjournal.com/issue162/acosta.html"
    url: "https://www.ncgsjournal.com/issue162/acosta.html"
    accessed: 2026-10-24
    reliability_note: "Scholarly review summarizing Airey 2019: never atheist; early works ponder absent/malevolent deity; later Christian domesticity. Airey monograph itself not opened end-to-end."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, childhood, heritage]
  - id: S5
    type: secondary
    kind: "journal article"
    author: "David S. Hogsette"
    citation: "Hogsette, David S. 'Metaphysical Intersections in Frankenstein: Mary Shelley's Theistic Investigation of Scientific Materialism and Transgressive Autonomy.' Christianity and Literature 60.4 (2011): 531–559. Author PDF: https://davidhogsette.com/wp-content/uploads/2012/03/Hogsette_frankenstein_article.pdf"
    url: "https://davidhogsette.com/wp-content/uploads/2012/03/Hogsette_frankenstein_article.pdf"
    accessed: 2026-10-24
    reliability_note: "Peer-reviewed article, read in full (PDF). Quotes Frederick L. Jones, Mary Shelley's Journal (1947) for Dec 1822 hereafter, Oct 1822 Power/Providence, Dante 1822, 5 Oct 1839 beneficent Power, ~1823 immutable laws of right. Jones print unread; quotations treated as secondary."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, childhood, timing]
  - id: S6
    type: secondary
    kind: "other"
    author: "Exploring London"
    citation: "'10 sites from Mary Shelley's London…6. St Giles-in-the-Fields…' Exploring London, 17 Oct 2018. https://exploring-london.com/2018/10/17/10-sites-from-mary-shelleys-london6-st-giles-in-the-fields/"
    url: "https://exploring-london.com/2018/10/17/10-sites-from-mary-shelleys-london6-st-giles-in-the-fields/"
    accessed: 2026-10-24
    reliability_note: "Local-history post on children's baptism 9 March 1818 at St Giles-in-the-Fields (William, Clara, Allegra). Practice fact about children, not Mary's creed."
    source_quality: "other"
    used_for: [heritage]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "Mary Shelley (ed. Frederick L. Jones)"
    citation: "Jones, Frederick L., ed. Mary Shelley's Journal. Norman: University of Oklahoma Press, 1947. Archive.org OCR (DLI scan): https://archive.org/stream/in.ernet.dli.2015.54863/2015.54863.Mary-Shelleys-Journal1947_djvu.txt"
    url: "https://archive.org/stream/in.ernet.dli.2015.54863/2015.54863.Mary-Shelleys-Journal1947_djvu.txt"
    accessed: 2026-10-24
    reliability_note: "Primary journal via Jones edition OCR. Preface confirms May 1815–July 1816 volume lost (~432 days). Early 1814–1815 London entries sampled; no creed statements found in sampled span-adjacent pages. Post-1822 reflective entries cited via Hogsette (S5) rather than this OCR (OCR noise / truncation)."
    source_quality: "primary / own words"
    used_for: [worldview, timing]
---

## Summary

Mary Shelley (1797–1851), English novelist [S1; S3]. Deepen D1: primary_system and A BELOW_THRESHOLD; B UNKNOWN; mid_basin UNKNOWN. Not plotted. Chart-moving NO.

## Life and work

London; Geneva (1816); Italy; return to England after Percy's death (1822) [S1; S3].

## Contribution and impact

Frankenstein (1818) [S1; S3]. Later novels include The Last Man (1826); edited Percy's Poetical Works (1839) [S1].

## Childhood and education

Little formal schooling; raised in Godwin's radical intellectual household; Dundee stays with Baxter family [S1; S3].

## Adult working worldview

No in-span (1818) first-person creed found. After-span journals (Jones via Hogsette): hereafter trust Dec 1822; God / beneficent Power Oct 1839; Providence struggle 1822 [S5]. Airey: never atheist [S4]. Frankenstein theology unused (P42). primary and A BELOW_THRESHOLD; B UNKNOWN.

## Heritage (context only)

Godwin Dissenter line / later theism; Wollstonecraft Anglican–rational-dissent milieu [S3; S4]. Children's baptism St Giles 9 Mar 1818 is theirs, not a scored creed for her [S6].

## Timing

1818, age 21 [S1]. Densest God/hereafter own words 1822–1839 (after major work) [S5].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No scored Lane A axes. Novel Creator allegory out (P42).

## Open questions

- Bennett Selected Letters / Feldman–Scott-Kilvert Journals print for any 1816–1818 creed line.
- Full Airey monograph beyond the Acosta review.

## Research log

- 2026-10-19: Read Britannica (Ostberg and Kuiper, scholars edition).
- 2026-10-24 (D1): Wikipedia dual bio (S3); Acosta/Airey (S4); Hogsette PDF Jones quotes (S5); St Giles baptism note (S6); Jones Journal OCR preface + early entries (S7). Frankenstein unused (P42). primary/A UNKNOWN→BELOW; B UNKNOWN. Chart-moving NO. No fallacy_catalog; no figures/.
