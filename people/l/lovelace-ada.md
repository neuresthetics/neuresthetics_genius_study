---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch C)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-08
  last_updated: 2026-10-08
  change_log:
    - {date: 2026-10-08, by: "Grok Bot", summary: "Record created (stage 3 batch C, order P32). Basics from MacTutor and Britannica (editors); worldview from her letter to Faraday of 16 October 1844 (Epsilon transcription of IEE MS SC 2) and her letter to Andrew Crosse of about 16 November 1844 (MacTutor transcription, secondary quotation). Not a scientist under P30/P33 (the Notes describe a machine). primary_system CHRIST 0.5 (consistent_private_letters, held below the ceiling; alternative BELOW_THRESHOLD, eclectic); A_locus 1 (0.5); B_cause 4 (0.5); C UNKNOWN; D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Draft, not reviewed."}
    - {date: 2026-10-08, by: "Grok Bot", summary: "Lens audit of batch C (dd91009), run 1: #3 A_locus 1 → 0 at 0.5, alternative 1 (coder's call: the 'ONE' and 'naturally related and interconnected' wording is about the unity of the works, not a limiting feature of God's transcendence). Quote hygiene: stray transcription spaces removed; S3 locators corrected to paragraphs 5 and 6 (were 'paragraph 2'). The 'secondary quotation' reason for CHRIST at 0.5 dropped; the hedge alone holds it at 0.5 (P29). mid_basin unchanged (BELOW_THRESHOLD)."}

identity:
  id: lovelace-ada
  display_name: "Ada Lovelace"
  roster:
    canonical_name: "Ada Lovelace"
    rank: 1
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Augusta Ada King, Countess of Lovelace (born Augusta Ada Byron)", certainty: 1.0, cites: [{source: S1, locator: "Biography, paragraph 1 and the 1835/1838 paragraph"}, {source: S2, locator: "In full; Original name"}], how_known: "Two sources."}
  native_name: {value: "Augusta Ada King", certainty: 1.0, cites: [{source: S2, locator: "In full"}, {source: S3, locator: "signature ('Augusta Ada Lovelace')"}], how_known: "English; married name."}
  aliases:
    - {name: "Ada-Lovelace", kind: "roster alias"}
    - {name: "Augusta Ada Byron", kind: "birth name"}

basics:
  birth:
    date: {value: "1815-12-10", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Info"}, {source: S2, locator: "Born line"}], how_known: "Two sources agree."}
    place: {value: "Piccadilly (Piccadilly Terrace), Middlesex", modern_name: "London, England, UK", polity_then: "United Kingdom of Great Britain and Ireland", certainty: 1.0, cites: [{source: S1, locator: "Quick Info"}, {source: S2, locator: "Born line"}], how_known: "Two sources agree."}
  death:
    date: {value: "1852-11-27", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Info"}, {source: S2, locator: "Died line"}], how_known: "Two sources agree."}
    place: {value: "Marylebone, London", modern_name: "London, England, UK", polity_then: "United Kingdom of Great Britain and Ireland", certainty: 1.0, cites: [{source: S1, locator: "Quick Info"}, {source: S2, locator: "Died line"}], how_known: "Two sources agree."}
  first_lasting_contribution_year: {value: 1843, certainty: 1.0, cites: [{source: S1, locator: "Biography ('published in Richard Taylor's Scientific Memoirs Volume 3 in 1843')"}, {source: S2, locator: "paragraph 3 ('in 1843 came to translate and annotate')"}], how_known: "The Notes on Menabrea's memoir, published 1843 (P30, first public statement). Two sources."}
  era_bucket: {value: "1750 to 1849", certainty: 1.0, cites: [{source: S1, locator: "Biography (1843)"}, {source: S2, locator: "paragraph 3"}], how_known: "From 1843 under P2."}
  region_of_birth: {value: "Northern Europe", certainty: 1.0, cites: [{source: S1, locator: "Quick Info"}, {source: S2, locator: "Born line"}], how_known: "UK is Northern Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 1.0, cites: [{source: S1, locator: "Biography"}, {source: S3, locator: "address (Ashley Combe, Somerset)"}], how_known: "All her work was done in England."}
  sex_as_recorded: {value: "female", certainty: 1.0, cites: [{source: S1, locator: "Biography"}, {source: S2, locator: "opening"}], how_known: "As the sources record it."}
  languages_of_work: {value: [English, French], certainty: 0.7, cites: [{source: S1, locator: "Biography (translation of Menabrea's French memoir)"}, {source: S2, locator: "paragraph 3"}], how_known: "She wrote in English and translated from French; French as a working language is the coder's inference from the translation."}
  occupations: {value: ["mathematician", "writer on the Analytical Engine"], certainty: 1.0, cites: [{source: S1, locator: "Summary"}, {source: S2, locator: "opening ('English mathematician')"}], how_known: "Two sources."}

contribution:
  fields: {value: ["mathematics", "computing"], certainty: 1.0, cites: [{source: S1, locator: "Summary"}, {source: S2, locator: "opening"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Notes to her translation of Menabrea's memoir on Babbage's Analytical Engine: how the engine could be programmed, including the computation of Bernoulli numbers, and that it 'might act upon other things besides number'", year: "1843", kind: work, lasting: "regarded as the first published computer program; she is 'considered the first computer programmer' (S2)", certainty: 1.0, cites: [{source: S1, locator: "Biography (Notes paragraphs)"}, {source: S2, locator: "opening; paragraph 3"}], how_known: "Two sources."}
  evidence_of_impact:
    - {value: "Ada Lovelace Day, the second Tuesday of October, honours women in STEM", kind: "named after them", certainty: 0.7, cites: [{source: S2, locator: "opening paragraph"}], how_known: "Britannica."}
    - {value: "Turing named 'Lady Lovelace's Objection' after her remark that the engine 'has no pretensions whatever to originate anything'", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S2, locator: "Top Questions ('Did Ada Lovelace predict artificial intelligence?')"}], how_known: "Britannica."}
  major_works:
    - {value: "Sketch of the Analytical Engine invented by Charles Babbage, by L. F. Menabrea, with Notes by the translator (signed AAL), in Taylor's Scientific Memoirs vol. 3", year: 1843, kind: "paper or paper series", certainty: 1.0, cites: [{source: S1, locator: "Biography"}, {source: S2, locator: "paragraph 3"}], how_known: "Two sources."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "One published work; its originality is accepted by both sources, and Babbage credits the algebraic working to her except the Bernoulli problem, which he offered to do and she corrected (S1, quoting Babbage 1864).", certainty: 0.7, cites: [{source: S1, locator: "Biography (Babbage's account)"}, {source: S2, locator: "Top Questions"}], how_known: "Two sources; the extent of her authorship has been debated, which the sources read do not discuss."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father the poet Lord Byron; parents separated about a month after her birth and she never saw him again", role: father, certainty: 1.0, cites: [{source: S1, locator: "Biography, paragraph 1"}, {source: S2, locator: "paragraph 2"}], how_known: "Two sources."}
    - {value: "Mother Anne Isabella (Annabella) Milbanke, Lady Byron, who had studied mathematics and pushed her daughter towards it", role: mother, certainty: 1.0, cites: [{source: S1, locator: "Biography, paragraphs 1–2"}, {source: S2, locator: "paragraph 2"}], how_known: "Two sources for the mother; the mathematical push is MacTutor's."}
  household_circumstances: {value: "Aristocratic; brought up by her mother and grandmother Lady Noel (d. 1822); a Ward in Chancery from 1817", certainty: 0.7, cites: [{source: S1, locator: "Biography, paragraphs 1–3"}], how_known: "MacTutor alone (P15)."}
  schooling:
    - {value: "Private tutors, including Miss Lamont (about age 6), William Frend, Dr William King (from 1829) and Miss Arabella Lawrence", stage: tutor, run_by: family, ages: "about 6–17", certainty: 1.0, cites: [{source: S1, locator: "Biography, tutors paragraph"}, {source: S2, locator: "paragraph 2 ('educated privately by tutors')"}], how_known: "Britannica gives private tutors; MacTutor names them."}
    - {value: "Advanced mathematics with Augustus De Morgan by correspondence", stage: tutor, run_by: private, years: "1841–", ages: "26–", certainty: 1.0, cites: [{source: S1, locator: "Biography (1841)"}, {source: S2, locator: "paragraph 2"}], how_known: "Two sources; the year is MacTutor's."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Saw Babbage's Difference Engine in his London studio, two weeks after meeting him on 5 June 1833", year: 1833, age: 18, certainty: 0.7, cites: [{source: S1, locator: "Biography (1833)"}], how_known: "MacTutor alone (P15)."}
  key_early_reading: []
  childhood_mentors:
    - {value: "Mary Somerville, from 1834: sent her mathematics books, set problems and talked mathematics with her", certainty: 0.7, cites: [{source: S1, locator: "Biography (1834)"}], how_known: "MacTutor, quoting Baum (1986)."}
  languages_in_childhood: {value: TODO}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1843–1843", certainty: 1.0, cites: [{source: S1, locator: "Biography (1843)"}, {source: S2, locator: "paragraph 3"}], how_known: "Equals timing.major_work_period: one listed lasting contribution (P29, P30)."}
  nominal_affiliations: []
  self_described_science_religion_relation:
    value: "Science is the reading of God's works: 'Religion to me is science, and science is religion' (to Crosse, 1844); she hoped 'to die the High-Priestess of God's works as manifested on this earth' and held that the highest intellect needs 'a high spiritual & moral development' (to Faraday, 1844)."
    certainty: 0.7
    cites: [{source: S3, locator: "letter text"}, {source: S4, locator: "letter text"}]
    how_known: "Two private letters of autumn 1844; the Crosse letter is a secondary transcription (MacTutor), so 0.7."
  primary_system:
    value: CHRIST
    basis: consistent_private_letters
    certainty: 0.5
    cites: [{source: S3, locator: "letter text ('I am myself a Unitarian Christian; as far as regards some of their views of Christ that is')"}, {source: S4, locator: "letter text ('a biblical and scriptural truth too')"}]
    how_known: "Her own profession in a private letter: 'I am myself a Unitarian Christian; as far as regards some of their views of Christ that is. But in truth, I cannot be said to be anything but myself' (S3). The second letter (S4) appeals to 'a biblical and scriptural truth' but is a secondary quotation (P26). Held at 0.5, below the 0.7 ceiling, because she qualifies the label herself (a hedged self-report, P29)."
    rationale: "Draft judgment (one line): CHRIST at 0.5 on her own Unitarian self-description; the named alternative is BELOW_THRESHOLD as an eclectic ('Swedenborgian in feelings', 'slightly Roman Catholic', 'my alliance with the older Rosecrucians', S3) whom no single code fits."
  secondary_system: {value: UNKNOWN, how_known: "No second system; she published only the Notes, which contain no worldview."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Coded at 0.5: 'I am myself a Unitarian Christian' (S3); appeal to 'biblical and scriptural truth' (S4). Against: she qualifies it at once and lists Swedenborgian, Catholic and Rosicrucian leanings.", cites: [{source: S3, locator: "letter text"}, {source: S4, locator: "letter text"}]}
    - {code: HERMET, reason: "Considered for the 'alliance with the older Rosecrucians' and the 'occult influences of nature' (S3). Rejected: one phrase, and the editors gloss 'occult influences' as mesmerism, not Hermetic doctrine.", cites: [{source: S3, locator: "letter text; editor's note 3"}]}
    - {code: PANT, reason: "Considered for 'all the works and the feelings He has called into existence are ONE' (S4). Rejected: God 'has called into existence' and 'has chosen to create' the works (S3, S4), so God is not identified with nature.", cites: [{source: S4, locator: "letter text"}, {source: S3, locator: "letter text"}]}
  lio_axes:
    A_locus:
      value: 0
      basis: consistent_private_letters
      certainty: 0.5
      cites: [{source: S3, locator: "letter text, paragraph 5"}, {source: S4, locator: "letter text"}]
      how_known: "Two private letters of 1844; held at 0.5 because the reading of 0 against 1 is the coder's (lens audit of batch C, #3)."
      rationale: "Draft judgment (one line): God is the creator, distinct from the creation, who 'has chosen to create moral beings fitted to hold relations with each other, & with Him' (S3) and 'has called into existence' all the works (S4): a personal creator outside his works, the Maxwell and Boyle pattern, so 0. Coder's call on the audit's question: her 'ONE' passage says that God is one and that the works He 'has called into existence are ONE', and 'all and everything is naturally related and interconnected' (S4); both describe the unity of the created works with each other, not God's presence in them, so neither names a limiting feature (as Newton's substantial omnipresence does) that would justify 1. Named alternative: 1, if the 'ONE' passage is read as joining God and his works."
    B_cause:
      value: 4
      basis: consistent_private_letters
      certainty: 0.5
      cites: [{source: S3, locator: "letter text"}, {source: S4, locator: "letter text"}]
      how_known: "Her own statements about nature in two private letters (P16: a non-scientist needs a statement about nature, which these are). One is a secondary quotation, so 0.5."
      rationale: "Draft judgment (one line): she expects to bring 'the nervous & vital system within the domain of mathematical science' and to find 'some great vital law of molecular action, similar for the universe of life, to gravitation for the sidereal universe' (S3), and holds that 'all and everything is naturally related and interconnected' (S4). Named alternative: 3, because she rebukes philosophers 'full of selfish feelings, and of a tendency to war against circumstances and Providence' (S4) and links the highest intellect to 'a high spiritual & moral development' (S3), which may leave room for special providence."
    C_ledger: {value: UNKNOWN, how_known: "Nothing in the letters read on judgement, reward or an afterlife (P19)."}
    D_authority: {value: BELOW_THRESHOLD, note: "She calls the oneness of God's works 'a biblical and scriptural truth too' (S4) but treats science as the reading of God's works; nothing says which wins in a conflict. Draft judgment (one line): too indirect to score.", how_known: "BELOW_THRESHOLD under P19."}
    E_scope: {value: BELOW_THRESHOLD, note: "Scored on the world's order (P7). 'All and everything is naturally related and interconnected' (S4) and her being 'one particular case of the general formula' of God's moral beings (S3) point towards a universal order, but both are in one letter each and one is secondary. Draft judgment (one line): too indirect to score; the alternative is E 4 at 0.5.", how_known: "BELOW_THRESHOLD under P19."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is 0 and B_cause is 4, but both only at 0.5, so the P4 test is not met at the required 0.7 (§6, P19)."}
  statements:
    - text: "You will be kind enough to think of me simply as one of God's children. The mere accidents of my being an inhabitant of this particular planet, of this particular corner of it England, & of my wearing the female form, (with a human coronet to boot stuck at the apex), these constitute only one particular case of the general formula in which God has chosen to create moral beings fitted to hold relations with each other, & with Him."
      cites: [{source: S3, locator: "letter text, paragraph 5"}]
      date: "1844-10-16"
      context: "Opening of her request to study Faraday's Researches with him."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "primary transcription"
      verified_on: 2026-10-08
    - text: "I hope to die the High-Priestess of God's works as manifested on this earth, & to earn a right to bequeath to my posterity the following motto, \"Dei Naturaeque Interpres\"."
      cites: [{source: S3, locator: "letter text, paragraph 6"}]
      date: "1844-10-16"
      context: "The editors translate the motto as 'Interpreter of God and Nature' (note 2)."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "primary transcription"
      verified_on: 2026-10-08
    - text: "I expect to bring the actions of the nervous & vital system within the domain of mathematical science, & possibly to discover some great vital law of molecular action, similar for the universe of life, to gravitation for the sidereal universe."
      cites: [{source: S3, locator: "letter text, 'great scientific object' paragraph"}]
      date: "1844-10-16"
      context: "Her plan to study the nervous system and 'the more occult influences of nature' (the editors note: mesmerism)."
      axes: [B_cause]
      kind: "private letter"
      verified_against: "primary transcription"
      verified_on: 2026-10-08
    - text: "I am myself a Unitarian Christian; as far as regards some of their views of Christ that is. But in truth, I cannot be said to be anything but myself. In some points I am Swedenborgian in feelings. Again in others I am slightly Roman Catholic; & I have also my alliance with the older Rosecrucians."
      cites: [{source: S3, locator: "letter text, closing paragraph"}]
      date: "1844-10-16"
      context: "After asking Faraday to what sect of Christians he belongs."
      axes: []
      kind: "private letter"
      verified_against: "primary transcription"
      verified_on: 2026-10-08
    - text: "Religion to me is science, and science is religion. In that deeply-felt truth lies the secret of my intense devotion to the reading of God's natural works ..."
      cites: [{source: S4, locator: "letter text"}]
      date: "1844-11"
      context: "Letter to Andrew Crosse before her visit to Broomfield; MacTutor dates it 'probably on 16 November 1844'."
      axes: [A_locus, B_cause]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-08
      note: "Primary check pending (P26): MacTutor gives the text with ellipses and does not name its printed source on the page; Toole (1992) is the likely source."
    - text: "That God is one, and all that all the works and the feelings He has called into existence are ONE; this is a truth (a biblical and scriptural truth too) not in my opinion developed to the apprehension of most people in its really deep and unfathomable meaning. There is too much tendency to making separate and independent bundles of both the physical and the moral facts of the universe. Whereas, all and everything is naturally related and interconnected."
      cites: [{source: S4, locator: "letter text"}]
      date: "1844-11"
      context: "Same letter."
      axes: [A_locus, B_cause, D_authority, E_scope]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-08
      note: "Primary check pending (P26)."
  changes_over_life: []
  coder_notes: "Not a scientist under P30/P33: her lasting contribution describes a machine and its programming, not a theory or result about physical or natural systems, so B needs her own statement about nature (P16), which the 1844 letters supply. Coder's call (CODING_GUIDE §8): primary_system CHRIST held at 0.5, below the 0.7 ceiling for consistent private letters, because she qualifies the label herself (P29 hedged self-report). 'Rosecrucians' is her spelling as transcribed. Both letters are from autumn 1844, a year after the Notes; nothing earlier was read. Her 'occult influences of nature' refers to mesmerism (editor's note 3 in S3), not to a break in natural law."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English aristocracy; daughter of Lord Byron", certainty: 1.0, cites: [{source: S1, locator: "Biography, paragraph 1"}, {source: S2, locator: "paragraph 2"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1843–1843", certainty: 1.0, cites: [{source: S1, locator: "Biography (1843)"}, {source: S2, locator: "paragraph 3"}], how_known: "One listed lasting contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 28, certainty: 1.0, cites: [{source: S1, locator: "Quick Info; Biography (1843)"}, {source: S2, locator: "Born line; paragraph 3"}], how_known: "1843 − 1815 = 28 (P30)."}
  first_evidence_of_lio_type_views: {value: "Letter to Faraday: a 'great vital law of molecular action' for living things like gravitation for the heavens (B_cause 4)", year: 1844, age: 29, certainty: 0.5, cites: [{source: S3, locator: "letter text"}], how_known: "The earliest dated statement of hers read that is scored at 3 or 4 (P27). Earlier letters were not read ('earlier works not read'), so 0.5."}
  lio_views_relative_to_major_work: {value: "after major work", rationale: "The 1844 letters come a year after the 1843 Notes; earlier writings were not read.", certainty: 0.5, cites: [{source: S3, locator: "date line"}, {source: S1, locator: "Biography (1843)"}], how_known: "Dated texts only; earlier works not read."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Nothing read from 1843 bears on her worldview; the letters are from 1844 (P31 continuity would carry them back, but no source states her view in 1843)."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "The Notes work out algebraic procedures step by step for a machine (S1); not definition-to-theorem proof.", certainty: 0.5, cites: [{source: S1, locator: "Biography (Notes)"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "tutors paragraph"}], how_known: "Mathematics from tutors as a child, advanced study from 1841; no source says when the form was learned."}
  circle_present: {value: "partly", rationale: "She ties God and nature together ('Interpreter of God and Nature'; science as reading God's works) but keeps God as creator of the works.", certainty: 0.5, cites: [{source: S3, locator: "letter text"}, {source: S4, locator: "letter text"}], how_known: "Coder's reading."}
  reading: "As belief, not finding: form partly present, circle partly present; the letters come after the work."
  notes: ""

institutions: []
collaborators:
  - {value: "Charles Babbage (babbage-charles)", relation: collaborator, note: "met 5 June 1833; the Notes were written with his suggestions", certainty: 1.0, cites: [{source: S1, locator: "Biography (1833; Babbage's account)"}, {source: S2, locator: "paragraph 3"}], how_known: "Two sources."}
  - {value: "Augustus De Morgan (de-morgan-augustus)", relation: teacher, note: "advanced mathematics from 1841", certainty: 1.0, cites: [{source: S1, locator: "Biography (1841)"}, {source: S2, locator: "paragraph 2"}], how_known: "Two sources."}
  - {value: "Mary Somerville (somerville-mary)", relation: "mentor or employer", note: "mentor from 1834", certainty: 1.0, cites: [{source: S1, locator: "Biography (1834)"}, {source: S2, locator: "paragraph 3"}], how_known: "Two sources."}
  - {value: "Michael Faraday (faraday-michael)", relation: correspondent, certainty: 1.0, cites: [{source: S3, locator: "letter"}], how_known: "Her own letter."}
  - {value: "Lord Byron (byron-lord)", relation: family, note: "father; never met after infancy", certainty: 1.0, cites: [{source: S1, locator: "Biography, paragraph 1"}, {source: S2, locator: "paragraph 2"}], how_known: "Two sources."}

review:
  roster_status_reason: {value: "Core in v8 (F 5: Claude, DeepSeek, Gemini, GPT, Grok).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 1"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "How she met Babbage: at a party on 5 June 1833 (MacTutor) vs introduced by Mary Somerville (Britannica). Not used for any computed field."
    - "Crosse letter (S4) is a secondary quotation with ellipses; primary check pending (P26)."
  open_questions:
    - "Read Toole (1992) for the Crosse letter and earlier letters (before 1843) on religion."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "J. J. O'Connor and E. F. Robertson"
    year: 2002
    citation: "O'Connor, J. J., and E. F. Robertson. \"Ada Lovelace.\" MacTutor History of Mathematics, University of St Andrews, last updated August 2002. https://mathshistory.st-andrews.ac.uk/Biographies/Lovelace/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Lovelace/"
    accessed: 2026-10-08
    reliability_note: "Standard reference biography; quotes Babbage (1864) and Baum (1986)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, collaborators]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Ada Lovelace.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Ada-Lovelace."
    url: "https://www.britannica.com/biography/Ada-Lovelace"
    accessed: 2026-10-08
    reliability_note: "Unsigned editors' article; whole article read."
    used_for: [identity, basics, contribution, childhood, heritage, timing, collaborators]
  - id: S3
    type: primary
    kind: letter
    author: "Augusta Ada Lovelace"
    year: 1844
    citation: "Lovelace, Augusta Ada, to Michael Faraday, 16 October 1844. IEE MS SC 2. Ɛpsilon: The Michael Faraday Collection, letter Faraday1620; also in The Correspondence of Michael Faraday, vol. 3 (1996). https://epsilon.ac.uk/view/faraday/letters/Faraday1620."
    url: "https://epsilon.ac.uk/view/faraday/letters/Faraday1620"
    accessed: 2026-10-08
    reliability_note: "Scholarly-edition transcription of the manuscript (Faraday correspondence project). The follow-up of 24 October 1844 (Faraday1632) was also read; it has no worldview content."
    used_for: [identity, basics, worldview, timing, lane_b, collaborators]
  - id: S4
    type: primary
    kind: letter
    author: "Augusta Ada Lovelace"
    year: 1844
    citation: "Lovelace, Ada, to Andrew Crosse, probably 16 November 1844, as given in \"Ada Lovelace writes to Andrew Crosse,\" MacTutor History of Mathematics (Extras). https://mathshistory.st-andrews.ac.uk/Extras/Lovelace_letter/."
    url: "https://mathshistory.st-andrews.ac.uk/Extras/Lovelace_letter/"
    accessed: 2026-10-08
    reliability_note: "Secondary quotation: MacTutor's abridged text (with ellipses) does not name its printed source on the page; primary check pending (P26)."
    used_for: [worldview, lane_b]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-08
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# Ada Lovelace

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Ada Lovelace (1815–1852), daughter of Lord Byron, published in 1843 her Notes on Menabrea's memoir on Babbage's Analytical Engine, describing how it could be programmed [S1; S2]. In private letters of 1844 she called herself 'a Unitarian Christian' with Swedenborgian, Catholic and Rosicrucian leanings [S3] and wrote that 'Religion to me is science, and science is religion' [S4]. Draft: CHRIST 0.5; A 0 (0.5); B 4 (0.5); mid_basin BELOW_THRESHOLD.

## Life and work

Brought up by her mother Lady Byron, taught by private tutors, married William King in 1835 (Countess of Lovelace from 1838), studied advanced mathematics with De Morgan from 1841, and died of cancer in 1852 [S1; S2].

## Contribution and impact

The 1843 Notes [S1; S2]; Ada Lovelace Day [S2]; Turing's 'Lady Lovelace's Objection' [S2].

## Childhood and education

Private tutors from about age six, with a mathematical emphasis set by her mother [S1]; Somerville's mentoring from 1834 [S1].

## Adult working worldview

Creator God, science as reading God's works, and an expected 'vital law' for living things like gravitation [S3; S4]. Both letters are from 1844, after the Notes.

## Heritage (context only)

English aristocracy [S1; S2].

## Timing

First lasting contribution 1843, age 28. First LIO-type view 1844 (0.5; earlier works not read), after major work.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form partly, circle partly [S1; S3; S4].

## Open questions

- Primary check of the Crosse letter in Toole (1992).

## Research log

- 2026-10-08: Read MacTutor biography and Extras (Crosse letter), Britannica (editors), Epsilon letters Faraday1620 and Faraday1632. Epsilon keyword search returned nothing; letters fetched by number.
