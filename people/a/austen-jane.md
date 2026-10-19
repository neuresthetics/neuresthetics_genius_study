---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch S)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-18
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-18, by: "Grok Bot", summary: "Record created (stage 3 batch S, order P32: F 4, rank 106). Basics from Britannica (Brian C. Southam, signed; body only, read live). Worldview from her letters to Fanny Knight in the Brabourne edition (1884), read in the Republic of Pemberley's web transcription (unofficial web copy, 0.7 cap). Not a scientist. primary_system CHRIST (0.7, consistent private letters); A BELOW_THRESHOLD; B UNKNOWN (P16, P19); C BELOW_THRESHOLD; D, E UNKNOWN; mid_basin UNKNOWN. Not plotted. The three prayers attributed to her are context only (attribution not settled, P42). Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit fixes for batch S (blind audit of c5d448a, run 1: AU4 FAIL, AU5 WEAKEN; ruling S3, v8's call on the auditor's advice). The three prayers now count as her words under P42 (S3, Stovel: 'It seems clear that Jane Austen composed the prayers'), at 0.5: undated manuscripts copied by others, attributed by one scholar. A BELOW_THRESHOLD -> 0 at 0.5, alternative 1. 'Thou art every where present' now quoted from a source read (S5, a web transcription of the prayers). Henry Austen's 1818 remark added as context for CHRIST. B stays UNKNOWN (P16), so mid_basin stays UNKNOWN and she stays unplotted."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit fixes for batch T (Austen second blind run at 754bb24: prayer treatment holds; AU-P5 WEAKEN; ruling RQ-AU1, v8's call on the auditor's advice). B UNKNOWN -> BELOW_THRESHOLD, named reading 1 at 0.5 (her own petitions for physical protection are not a statement about nature under P16); mid_basin UNKNOWN -> BELOW_THRESHOLD; still not plotted. 'important but not decisive' marked as the coder's translation of S5's Italian summary; 'accepted by most editors; doubted by Todd and Bree'; the disputed hand of the inscription flagged; the A basis label explained (P18 private-document row). New statement: prayer I, fourth paragraph."}

identity:
  id: austen-jane
  display_name: "Jane Austen"
  roster:
    canonical_name: "Jane Austen"
    rank: 106
    F: 4
    models: [DeepSeek, Gemini, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: literature
    field_bucket: literature
  full_name: {value: "Jane Austen", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  native_name: {value: "Jane Austen", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "English; same as the display name."}
  aliases:
    - {name: "Austen-Jane", kind: "roster alias"}
    - {name: "Jane-Austen", kind: "roster alias"}

basics:
  birth:
    date: {value: "1775-12-16", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica body."}
    place: {value: "Steventon, Hampshire, England", modern_name: "Steventon, United Kingdom", polity_then: "Kingdom of Great Britain", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Early life and family'"}], how_known: "Britannica."}
  death:
    date: {value: "1817-07-18", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening; 'Unfinished works and death'"}], how_known: "Britannica body."}
    place: {value: "Winchester, Hampshire, England", modern_name: "Winchester, United Kingdom", polity_then: "United Kingdom of Great Britain and Ireland", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1811, certainty: 0.7, cites: [{source: S1, locator: "'Move to Chawton and publishing success'"}], how_known: "Sense and Sensibility, published November 1811, the earliest listed novel (P13, P30: first publication is its first public statement; drafts from about 1795 were not public)."}
  era_bucket: {value: "1750 to 1849", certainty: 0.7, cites: [{source: S1, locator: "'Move to Chawton and publishing success'"}], how_known: "1811 (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United Kingdom (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "'Move to Chawton and publishing success'"}], how_known: "Chawton, Hampshire."}
  sex_as_recorded: {value: "female", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica ('English writer')."}
  occupations: {value: ["novelist"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["the novel"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Sense and Sensibility", year: 1811, kind: work, lasting: "'timeless classics that remained critical and popular successes for more than two centuries' (S1, of the novels)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Move to Chawton and publishing success'"}], how_known: "Britannica (November 1811)."}
    - {value: "Pride and Prejudice", year: 1813, kind: work, lasting: "as above (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Move to Chawton and publishing success'"}], how_known: "Britannica (January 1813)."}
    - {value: "Mansfield Park", year: 1814, kind: work, lasting: "as above (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Move to Chawton and publishing success'"}], how_known: "Britannica."}
    - {value: "Emma", year: 1815, kind: work, lasting: "as above (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Move to Chawton and publishing success'"}], how_known: "Britannica (December 1815)."}
    - {value: "Persuasion", year: 1816, kind: work, lasting: "as above (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Move to Chawton and publishing success'; 'Unfinished works and death'"}], how_known: "Published posthumously in December 1817; dated by its last documented act in life, the end of writing in August 1816 ('written August 1815–August 1816'; P30 posthumous rule). The latest listed lasting contribution (P30 addendum). Northanger Abbey (written about 1798–99, looked at again in 1816, published with Persuasion) is not listed separately; its 1816 revisit gives the same end year."}
  evidence_of_impact:
    - {value: "'first gave the novel its distinctly modern character'; Scott's review of Emma (1816) and Whately's (1821) 'provided the foundation for serious criticism'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Unfinished works and death'"}], how_known: "Britannica (signed)."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Church of England: father the Anglican rector of Steventon", certainty: 0.7, cites: [{source: S1, locator: "'Early life and family'"}], how_known: "Britannica."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father George Austen, Anglican rector and scholar who 'encouraged the love of learning in his children'; mother Cassandra Austen (née Leigh); seventh of eight children; closest companion her sister Cassandra", certainty: 0.7, cites: [{source: S1, locator: "'Early life and family'"}], how_known: "Britannica."}
  household_circumstances: {value: "Steventon rectory; family theatricals ('The great family amusement was acting')", certainty: 0.7, cites: [{source: S1, locator: "'Early life and family'"}], how_known: "Britannica."}
  schooling: []
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["English"], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "Juvenilia in three manuscript notebooks, about 1787–1793", certainty: 0.7, cites: [{source: S1, locator: "'Early writings'"}], how_known: "Britannica."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1811–1816", certainty: 0.7, cites: [{source: S1, locator: "'Move to Chawton and publishing success'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Church of England (rector's daughter)", certainty: 0.7, cites: [{source: S1, locator: "'Early life and family'"}], how_known: "Context only; the code rests on her letters."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing on science in the letters read (Brabourne letters LXXX–LXXXIV, S2)."}
  primary_system:
    value: CHRIST
    basis: consistent_private_letters
    certainty: 0.7
    cites: [{source: S2, locator: "letters LXXX (18 November 1814) and LXXXI (30 November 1814)"}]
    rationale: "CHRIST's v8 note: Christian belief (Christ, scripture, creeds, church) shown in her own writing, with no more specific philosophical position. Two private letters to her niece, twelve days apart and consistent: she is 'by no means convinced that we ought not all to be evangelicals', the suitor's 'acting more strictly up to the precepts of the New Testament' is no objection, and 'I cannot suppose we differ in our ideas of the Christian religion'. No other code was considered plausible: CLTHEI needs a God who intervenes beyond the creeds, which the letters do not show."
    how_known: "Two consistent private letters (0.7 ceiling), inside the working years; read in an unofficial web copy of the Brabourne edition, which is also capped at 0.7."
    note: "Supporting context (not a basis): her brother Henry, introducing her as the author of her novels in 1818, wrote that 'her opinions accorded strictly with those of our Established Church' (quoted by Stovel, S3, part II). The prayers (S3, S5), now counted as hers under P42 at 0.5, are Prayer Book Christianity in form and content (S3, part II)."
  secondary_system: {value: UNKNOWN, how_known: "One system (P29)."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Letters of November 1814 (S2)."}
    - {code: CLTHEI, reason: "Rejected: no petition or intervention beyond ordinary Christian piety. The prayers (counted as hers at 0.5 under P42) ask God to guard the household and travellers and to care for the sick, but in the form of the Book of Common Prayer's collects (S3, part II): creedal intercession, not a God who intervenes beyond the creeds."}
  lio_axes:
    A_locus:
      value: 0
      basis: consistent_private_letters
      certainty: 0.5
      cites: [{source: S3, locator: "parts I–II"}, {source: S5, locator: "prayers I–III"}]
      rationale: "Transcendent personal pole. The three prayers address a Father in heaven who sees, judges and pardons: 'Have we thought irreverently of Thee, have we disobeyed thy Commandments' (I), 'Pardon Oh God! whatever thou has seen amiss in us' (II), 'secure an Eternity of Happiness with each other in thy Heavenly Kingdom. Grant this most merciful Father, for the sake of our Blessed Saviour' (III). Named alternative 1: 'Thou art every where present, from Thee no secret can be hid' (I) adds omnipresence, though as the knowledge of a personal judge, not identity with the world. The 1817 letter ('I hope Heaven, in its mercy, will take her soon', letter LXXXIII) is consistent but after the working years and conventional."
      how_known: "P42 (ruling S3, v8's call on the auditor's advice): a source read attributes these texts to her (S3: 'It seems clear that Jane Austen composed the prayers'; the Doody and Murray edition 'treats the prayers as Jane Austen's own'). Undated manuscripts, copied by others (Stovel: Cassandra's inscription, Henry's hand; Todd and Bree, as summarised in S5: James Austen and Cassandra, c. 1818–1819), attributed on the family inscription; the attribution is accepted by most editors and doubted by Todd and Bree, so 0.5 (private ceiling and the attribution doubt). Who wrote the inscription is itself disputed: Stovel says Cassandra's hand (S3, part I); S5's summary of Todd and Bree says a hand very like Charles Austen's. Basis label: consistent_private_letters is the basis table's private-document row, which P18 assigns to an unpublished or private document such as a prayer (three prayers on two sheets, consistent); the prayers are not letters, and since the surviving copies are in other hands their kind is 'unpublished manuscript', not 'document in own hand'. Le Faye places them in her later life (quoted in S3, part III), which may or may not fall in 1811–1816."
      alternatives:
        - {value: 1, note: "'Thou art every where present' (prayer I).", cites: [{source: S5, locator: "prayer I, first paragraph"}]}
    B_cause:
      value: BELOW_THRESHOLD
      cites: [{source: S5, locator: "prayer I, fourth paragraph; prayer III, fifth to last paragraphs"}, {source: S3, locator: "part II"}]
      how_known: "Not a scientist (P30). Ruling RQ-AU1 (v8's call on the auditor's advice, Austen second blind run at 754bb24): a person's own prayer for physical protection or healing is not a statement about nature under P16; petitionary prayer only implies a God who answers by acting, which is BELOW_THRESHOLD evidence (P19). The prayers petition for physical protection: 'guard us, and all we love, from Evil this night ... heartily do we pray for the safety of all that travel by Land or by Sea' (I); 'Bring us in safety to the beginning of another day'; 'assuage the pangs of disease'; 'avert from them all material & lasting Evil of Body or Mind' (III). Stovel calls the petitions 'the work of the common, generic believer' (S3, part II). The 1817 hope that 'Heaven, in its mercy' will take Harriot (letter LXXXIII) is about a death; checked and off-point."
      note: "Named reading 1 at 0.5 (petition answered within a created order), not adopted under RQ-AU1; Newton's private petition was likewise only a named alternative on B (P7 table)."
    C_ledger: {value: BELOW_THRESHOLD, how_known: "Evangelicals 'from reason and feeling must be happiest and safest' (letter LXXX) may refer to salvation, but the sense is not explicit; 'if we believe the doctrine of original sin' (letter LXXXII, February 1817) is playful. Too indirect (P19)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing on revelation against observation or reason in the letters read (S2)."}
    E_scope: {value: UNKNOWN, how_known: "Nothing on the world's order in the letters read (S2)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "P4 test: B is BELOW_THRESHOLD (RQ-AU1) and A is 0 only at 0.5 (prayers, P42 ruling S3), under the 0.7 bar (P10, P19). No needed axis is UNKNOWN."}
  statements:
    - text: "And, as to there being any objection from his goodness, from the danger of his becoming even evangelical, I cannot admit that.  I am by no means convinced that we ought not all to be evangelicals, and am at least persuaded that they who are so from reason and feeling must be happiest and safest."
      cites: [{source: S2, locator: "letter LXXX, Chawton, Friday 18 November 1814"}]
      date: "1814-11-18"
      context: "Letter to her niece Fanny Knight, advising on a suitor whose religious seriousness Fanny feared; she goes on 'don't be frightened by the idea of his acting more strictly up to the precepts of the New Testament than others.'"
      axes: [C_ledger]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-18
      note: "Brabourne edition (1884), read in the Republic of Pemberley's web transcription; Le Faye numbering not checked (TODO)."
    - text: "I cannot suppose we differ in our ideas of the Christian religion.  You have given an excellent description of it.  We only affix a different meaning to the word evangelical."
      cites: [{source: S2, locator: "letter LXXXI, 23 Hans Place, Wednesday 30 November 1814"}]
      date: "1814-11-30"
      context: "Letter to Fanny Knight, answering Fanny's account of the Christian religion."
      axes: []
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-18
      note: "As above. Supports primary_system only."
    - text: "I hope Heaven, in its mercy, will take her soon."
      cites: [{source: S2, locator: "letter LXXXIII, Chawton, Thursday 13 March [1817]"}]
      date: "1817-03-13"
      context: "Letter to Fanny Knight, of her niece Harriot, diagnosed with 'water on the brain'. Brabourne dates it 1816; the transcription's note says it is 1817. After the working years."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-18
      note: "As above."
    - text: "Give us grace, Almighty Father, so to pray, as to deserve to be heard, to address thee with our Hearts, as with our Lips. Thou art every where present, from Thee no secret can be hid; may the knowledge of this, teach us to fix our Thoughts on Thee, with Reverence & Devotion that we pray not in vain."
      cites: [{source: S5, locator: "prayer I, first paragraph"}]
      context: "Opening of the first prayer ('Evening Prayer'), a household evening prayer; undated (S3, part III). The manuscript sheet carries the inscription 'Prayers Composed by my ever dear Sister Jane' (S3, part I)."
      axes: [A_locus]
      kind: "unpublished manuscript"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Unofficial web transcription of the Mills College manuscript (S5); this paragraph is not in Stovel's excerpts. Where Stovel quotes prayer I (from 'Look with Mercy'), S5 agrees except for small variants ('Resolution' for 'resolutions', '&' for 'and')."
    - text: "More particularly do we pray for the safety and welfare of our own family & friends wheresoever dispersed, beseeching Thee to avert from them all material & lasting Evil of Body or Mind; & may we by the assistance of thy Holy Spirit so conduct ourselves on Earth as to secure an Eternity of Happiness with each other in thy Heavenly Kingdom. Grant this most merciful Father, for the sake of our Blessed Saviour in whose Holy Name & Words we further address thee."
      cites: [{source: S5, locator: "prayer III, last paragraph"}, {source: S3, locator: "part II"}]
      context: "Close of the third prayer, before the Lord's Prayer; undated."
      axes: [A_locus]
      kind: "unpublished manuscript"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "S5's text; Stovel (S3, part II) quotes the 'may we by the Assistance ...' clause and the 'Grant this' sentence with the same words (capitals and '&' differ)."
    - text: "Be Gracious to our Necessities, and guard us, and all we love, from Evil this night. May the sick and afflicted, be now, & ever thy care; and heartily do we pray for the safety of all that travel by Land or by Sea, for the comfort & protection of the Orphan & Widow, & that thy pity may be shewn upon all Captives & Prisoners."
      cites: [{source: S5, locator: "prayer I, fourth paragraph"}]
      context: "First prayer; petitions for the household and for others. Undated."
      axes: [B_cause]
      kind: "unpublished manuscript"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "S5's text, checked live 2026-10-19. Petition, not a statement about nature (ruling RQ-AU1)."
    - text: "her opinions accorded strictly with those of our Established Church"
      cites: [{source: S3, locator: "part II"}]
      date: "1818"
      context: "Henry Austen's words in introducing her as the author of her novels (the 1818 Biographical Notice), quoted by Stovel."
      axes: []
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-19
      note: "Her brother's characterisation, not her words: supporting context for CHRIST only."
  changes_over_life: []
  coder_notes: "Coder's call. CHRIST rests on two private letters of November 1814. The three prayers (Mills College manuscript) count as hers under P42 (ruling S3), at 0.5, and give A 0 (alternative 1). The prayers' petitions for physical protection bear on B only as an implication, so B is BELOW_THRESHOLD with 1 named (ruling RQ-AU1) and she is not plotted. Doubt on the attribution: S5's Italian headnote, summarising Todd and Bree, calls the inscription the only evidence, 'un indizio importante ma non decisivo' ('important but not decisive' is the coder's translation of S5's summary, not Todd and Bree's words). The attribution is accepted by most editors; doubted by Todd and Bree. Words that the Pemberley transcription restores from outside the Brabourne text are not quoted."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English (Hampshire gentry and clergy)", certainty: 0.7, cites: [{source: S1, locator: "'Early life and family'"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Church of England", certainty: 0.7, cites: [{source: S1, locator: "'Early life and family'"}], how_known: "Britannica (father a rector)."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1811–1816", certainty: 0.7, cites: [{source: S1, locator: "'Move to Chawton and publishing success'"}], how_known: "Sense and Sensibility (1811) to Persuasion (finished August 1816; published posthumously December 1817), first to last listed lasting contribution (P29, P30 posthumous rule)."}
  age_at_first_lasting_contribution: {value: 36, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "1811 − 1775 = 36 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement of hers is scored at 3 or 4."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "letters LXXX–LXXXIV"}], how_known: "In the sources read."}
  worldview_during_major_work: {value: "Anglican Christian, sympathetic to evangelical seriousness", certainty: 0.7, cites: [{source: S2, locator: "letters LXXX, LXXXI"}], how_known: "Her letters of November 1814."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Novelist; no definition-to-consequence work.", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Early life and family'"}], how_known: "Not read."}
  circle_present: {value: "no", rationale: "No identification of God and Nature in the letters read.", certainty: 0.5, cites: [{source: S2, locator: "letters LXXX–LXXXIV"}], how_known: "Coder's reading."}
  reading: "An Anglican novelist with no stated view of nature: off the H1 axes."
  notes: ""

institutions: []
collaborators:
  - {value: "Henry Austen", relation: family, note: "brother; go-between with her publishers, announced her authorship", certainty: 0.7, cites: [{source: S1, locator: "'Move to Chawton'; 'Unfinished works and death'"}], how_known: "Britannica."}
  - {value: "Fanny Knight", relation: correspondent, note: "niece", certainty: 0.7, cites: [{source: S2, locator: "letters LXXX–LXXXIV"}], how_known: "The letters."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 106"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Letters read in an unofficial web transcription of the Brabourne edition (1884), which cuts some passages; the transcription restores some cut words in brackets (not quoted). Not checked against Le Faye's edition."
    - "Brabourne misdates letters LXXXII–LXXXIV to 1816; the transcription notes they are of 1817."
    - "Cassandra destroyed many letters; 'Only 160 out of thousands' survive (S1)."
    - "The hand of the prayers' inscription ('Prayers Composed by my ever dear Sister Jane') is disputed: Cassandra's (Stovel, S3 part I) or very like Charles Austen's (Todd and Bree as summarised in S5)."
  open_questions:
    - "Check the letters against Le Faye (4th ed.) and read the letters to Cassandra for religious remarks."
    - "Read Todd and Bree on the prayers' attribution and text (Later Manuscripts, pp. cxviii–cxxvi, Appendix D); the transcription read (S5) is unofficial."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Brian C. Southam"
    citation: "Southam, Brian C. \"Jane Austen.\" Encyclopaedia Britannica (revised 18 October 2026). https://www.britannica.com/biography/Jane-Austen. Read live 2026-10-18."
    url: "https://www.britannica.com/biography/Jane-Austen"
    accessed: 2026-10-18
    reliability_note: "Signed article. Body only; the AI-generated question boxes are not cited."
    used_for: [identity, basics, contribution, childhood, heritage, timing, collaborators, lane_b, worldview]
  - id: S2
    type: primary
    kind: "scholarly edition"
    author: "Jane Austen; ed. Edward, Lord Brabourne"
    citation: "Austen, Jane. Letters of Jane Austen, ed. Edward, Lord Brabourne (London: Richard Bentley, 1884), letters to Fanny Knight LXXX–LXXXIV. Web transcription: Republic of Pemberley, https://pemberley.com/janeinfo/brablt15.html"
    url: "https://pemberley.com/janeinfo/brablt15.html"
    accessed: 2026-10-18
    reliability_note: "Unofficial web copy of a Victorian edition (0.7 cap, §7); the edition omits some passages, which the transcription restores in brackets."
    used_for: [worldview, timing, collaborators, lane_b]
  - id: S3
    type: secondary
    kind: "journal article"
    author: "Bruce Stovel"
    citation: "Stovel, Bruce. \"'A Nation Improving in Religion': Jane Austen's Prayers and Their Place in Her Life and Art.\" Persuasions 16 (1994): 185–196. https://jasna.org/persuasions/printed/number16/stovel.htm"
    url: "https://jasna.org/persuasions/printed/number16/stovel.htm"
    accessed: 2026-10-18
    reliability_note: "Read in full on 2026-10-19 (parts I–IV). Persuasions is JASNA's journal; the article attributes the prayers to her and quotes them from the manuscripts; it also quotes Henry Austen (1818) and Le Faye on the dating."
    used_for: [worldview]
  - id: S5
    type: primary
    kind: other
    author: "Jane Austen (attributed); web transcription by jausten.it"
    citation: "Austen, Jane (attributed). Prayers I–III (Mills College, Heller Rare Book Room manuscript). Web transcription with Italian translation and notes: \"Jane Austen - Preghiere\", jausten.it, http://www.jausten.it/jaaopreghiere.html"
    url: "http://www.jausten.it/jaaopreghiere.html"
    accessed: 2026-10-19
    reliability_note: "Unofficial web transcription (0.7 cap); its headnote summarises Todd and Bree, Later Manuscripts (Cambridge, 2008), pp. cxviii–cxxvi, on the hands and the dating of the copies. Agrees with Stovel's excerpts apart from small variants."
    used_for: [worldview]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-18
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Jane Austen

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Jane Austen (1775–1817), English novelist [S1]. Draft: primary_system CHRIST (0.7); A 0 (0.5, from the prayers, P42); B BELOW_THRESHOLD (RQ-AU1); mid_basin BELOW_THRESHOLD. Not plotted.

## Life and work

Steventon, Bath, Southampton, Chawton [S1].

## Contribution and impact

Six novels, 1811–1817 [S1].

## Childhood and education

Rector's daughter [S1].

## Adult working worldview

'I am by no means convinced that we ought not all to be evangelicals' (1814) [S2, letter LXXX].

## Heritage (context only)

Church of England [S1].

## Timing

1811–1816, from age 36 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Off the axes [S2].

## Open questions

- Le Faye check; prayers.

## Research log

- 2026-10-18: Read Britannica (live) and the Brabourne letters to Fanny Knight (Pemberley transcription). Prayers known from search extracts only.
- 2026-10-19: Read Stovel (S3) in full and the jausten.it transcription of the three prayers (S5); prayers scored under P42 (ruling S3).
