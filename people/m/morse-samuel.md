---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 4
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch X)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to invention. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #127). P47 source_quality on S1–S6. P48: A_locus support corroborated (S2 in-span letters + S5 WallBuilders 1836 album poem with God/Christ; Rigi diary 1831 nature-God language added as statement). P50: Wikipedia EN dual bio (S6) agrees birth 1791-04-27 Charlestown / death 1872-04-02 New York with Britannica. B stays BELOW_THRESHOLD under Ruling X1: Rankin 1835 reported speech (God created the great forces of nature) is teleology/providence, not a P16 lawful-order or exception claim; no own-voice laws-of-nature statement found in Letters and Journals or Foreign Conspiracy. primary CHRIST @0.7 and A 0 @0.7 held; mid BELOW; not plotted. No fallacy_catalog; no figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit fixes for batch X (gs_a1ff932_X run 1): (MO2) the telegraph dated by its first public statement, the patent caveat sent on 3 October 1837 (S2 vol. II chs. XXIII–XXIV; P30 #1): first lasting year 1832 -> 1837, span 1832–1838 -> 1837–1838, age 41 -> 46; era unchanged; the 1835 pamphlet now falls just before the span. (MO5) CLTHEI rejected under its use_when (2) (no in-span text expects God to act against or beyond nature's course); CLASS_THEISM listed as rejected. Ruling X1 (v8's call on the auditor's advice): B stays BELOW_THRESHOLD, named reading 1; only an answer claimed against or beyond nature's course bears on B (recorded under P16). CHRIST, A 0, E 1 unchanged."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch X, order P32: F 4, rank 128). Basics from Britannica (Carleton Mabee; Britannica Editors). Worldview from his own letters in Samuel F. B. Morse: His Letters and Journals (ed. Edward Lind Morse, 1914; Project Gutenberg) and his pamphlet Foreign Conspiracy (1835; archive.org scan). Not a scientist (P33: inventions). primary_system CHRIST (0.7); A 0 (0.7); B BELOW_THRESHOLD (named reading 1, RQ-AU1 analogy; RQ-X1); C, D UNKNOWN; E 1 (0.5, alt BELOW_THRESHOLD); mid_basin BELOW_THRESHOLD. Span 1832–1838 (0.7). Not plotted. Draft, not reviewed."}

identity:
  id: morse-samuel
  display_name: "Samuel Morse"
  roster:
    canonical_name: "Samuel Morse"
    rank: 128
    F: 4
    models: [Claude, Gemini, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: invention
    field_bucket: "invention / engineering"
  full_name: {value: "Samuel Finley Breese Morse", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts ('In full')"}], how_known: "Britannica."}
  native_name: {value: "Samuel Finley Breese Morse", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "English."}
  aliases:
    - {name: "Morse-Samuel", kind: "roster alias"}
    - {name: "Samuel-Morse", kind: "roster alias"}
    - {name: "Samuel F. B. Morse", kind: "other"}

basics:
  birth:
    date: {value: "1791-04-27", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts (Born)"}, {source: S6, locator: "infobox (Born)"}], how_known: "Britannica; Wikipedia EN agrees (P50 dual bio)."}
    place: {value: "Charlestown, Massachusetts", modern_name: "Charlestown, Boston, Massachusetts, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts (Born)"}], how_known: "Britannica."}
  death:
    date: {value: "1872-04-02", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts (Died)"}, {source: S6, locator: "infobox (Died)"}], how_known: "Britannica; Wikipedia EN agrees (P50 dual bio)."}
    place: {value: "New York, New York", modern_name: "New York City, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts (Died)"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1837, certainty: 0.7, cites: [{source: S2, locator: "vol. II ch. XXIII (caveat 'of October 3, 1837'); ch. XXIV (sent to Washington on October 3; receipt acknowledged October 6)"}, {source: S1, locator: "opening ('developed an electric telegraph (1832–35)')"}], how_known: "The electric telegraph, dated by its earliest documented public statement under P30 #1: the caveat sent to the Patent Office on 3 October 1837 (S2). 1832 (the idea conceived on the voyage home) and 1835 (first working model) were private (Britannica's range 1832–35); batch X audit, MO2."}
  era_bucket: {value: "1750 to 1849", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "1837 (P2); 1832 and 1835 give the same bucket."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "United States (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "telegraph paragraphs (New York, Morristown, Washington–Baltimore)"}], how_known: "Britannica; art study in England 1811 and Europe to 1832."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S2, locator: "letters"}], how_known: "Coder's reading."}
  occupations: {value: ["painter", "inventor", "teacher of art, University of the City of New York", "first president of the National Academy of Design (1826–1845)"], certainty: 0.7, cites: [{source: S1, locator: "opening; leadership and telegraph paragraphs"}], how_known: "Britannica."}

contribution:
  primary_domain: invention
  fields: {value: ["telegraphy", "painting"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "An electric telegraph (recording electromagnetic telegraph; first US line, Washington–Baltimore, 1844)", year: 1837, kind: invention, lasting: "'Even during Morse's own lifetime, the world was much changed by the telegraph'; his 1837 instrument is preserved by the Smithsonian (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; telegraph paragraphs; legacy paragraph"}], how_known: "Britannica dates the development 1832–35; dated by the patent caveat of 3 October 1837, its first public statement (P30 #1; S2 vol. II chs. XXIII–XXIV; batch X audit, MO2). An invention, not a theory or result, so not a scientist (P33)."}
    - {value: "Morse Code (with Alfred Vail)", year: 1838, kind: "concept or term", lasting: "'the system of dots and dashes that became known throughout the world as the Morse Code' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Top Questions; telegraph paragraph ('By 1838')"}], how_known: "Britannica. Latest dated lasting item, so it ends the span (P30 addendum b)."}
    - {value: "Portraits (Lafayette, William Cullen Bryant and others)", kind: "body of work", lasting: "'some of the finest portraits ever done by an American artist'; 'his reputation as an artist has grown' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Top Questions; legacy paragraph"}], how_known: "Britannica; undated there, so it sets no span (P39)."}
  evidence_of_impact:
    - {value: "Telegraph lines 'over continents and under oceans'; wealth and fame in his lifetime", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "patent and legacy paragraphs"}], how_known: "Britannica."}
    - {value: "1854 US Supreme Court decision upholding his patent rights", kind: other, certainty: 0.7, cites: [{source: S1, locator: "controversy paragraph"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Telegraph and Morse Code changed communication worldwide (S1).", certainty: 0.7, cites: [{source: S1, locator: "legacy paragraph"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Congregationalist (father a Congregational clergyman)", certainty: 0.7, cites: [{source: S1, locator: "opening ('Congregational clergyman Jedidiah Morse')"}], how_known: "Britannica."}
  family_religious_practice: {value: "'austere parents'", certainty: 0.5, cites: [{source: S1, locator: "Top Questions; opening"}], how_known: "Britannica's word; practice not described."}
  parents_and_household:
    - {value: "Father: Jedidiah Morse, geographer and Congregational clergyman", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  household_circumstances: {value: "Clerical, orthodox household; parents distressed by his painting", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  schooling:
    - {value: "Phillips Academy, Andover, Massachusetts", stage: "grammar or secondary school", run_by: private, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; 'an unsteady and eccentric student'."}
    - {value: "Yale College, New Haven (graduated 1810)", stage: university, run_by: other, years: "to 1810", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; lectures on electricity aroused his interest."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure:
    - {value: "Yale lectures on electricity", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1837–1838", certainty: 0.7, cites: [{source: S1, locator: "opening; telegraph paragraph"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Protestant, by his own public identification ('we, Protestant republicans of the United States', 1835)", certainty: 0.7, cites: [{source: S3, locator: "p. 30"}], how_known: "His own published pamphlet (pseudonym Brutus; authorship stated in his letter of 20 May 1835, S2 vol. II ch. XXII)."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No statement on science and religion as such read; the 1868 banquet speech ascribes the telegraph's origin to God (statements) but does not state a relation."}
  primary_system:
    value: CHRIST
    basis: consistent_private_letters
    certainty: 0.7
    cites: [{source: S2, locator: "vol. II ch. XXIV (letters of 8 November 1837 and 15 March 1838)"}, {source: S3, locator: "p. 30"}, {source: S5, locator: "letter to Mary Pattison, 14 September 1836"}, {source: S2, locator: "vol. II chs. XXX–XXXI (letters of 31 May and 23 June 1844)"}]
    rationale: "Inside the span, two private letters pray to a provident God ('through a kind Providence', 1837; 'let us pay to Him who shows it to us the homage of grateful and obedient hearts, with most earnest prayers for grace', 1838); just before it, his published pamphlet calls himself one of the 'Protestant republicans' (1835) and his 1836 album poem addresses God and Christ (S5). After the span the faith is explicit and Christian ('Pray for me then ... that I may have a heart to praise the great Deliverer', 1844; 'Not unto us ... but to God be all the glory', public speech, 1868). Consistent private letters, so 0.7 (§3); Britannica records his religious controversies 'with Unitarians and Roman Catholics' and gifts to seminaries and Bible societies (S1)."
    how_known: "Own letters (edited 1914) and pamphlet."
  secondary_system: {value: UNKNOWN, how_known: "One system (P29)."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Chosen: Protestant (Congregational) faith in letters and pamphlet."}
    - {code: CLTHEI, reason: "Rejected under its use_when (2): no in-span text expects God to act against or beyond the regular course of nature; the in-span letters speak of providence through friends and events (batch X audit, MO5)."}
    - {code: CLASS_THEISM, reason: "Rejected: no systematic theology read; CHRIST fits the stated Christian faith (batch X audit, MO5)."}
  lio_axes:
    A_locus:
      value: 0
      basis: consistent_private_letters
      certainty: 0.7
      support: corroborated
      cites: [{source: S2, locator: "vol. II ch. XXIV (8 November 1837; 15 March 1838)"}, {source: S2, locator: "vol. I ch. XVIII (Rigi diary, 28 August 1831)"}, {source: S5, locator: "letter to Mary Pattison, New York, 14 September 1836 (album poem)"}, {source: S2, locator: "vol. II ch. XXXI (23 June 1844)"}]
      rationale: "Transcendent person: a God addressed in prayer who shows and grants ('Him who shows it to us', 1838; 'a kind Providence', 1837); before the span, Rigi diary adores the Creator of those wonders and lifts the heart from nature up to nature’s God (1831), and the 1836 album poem yields the pen to God and to cleansing by the blood of God’s own son (S5). After the span, 'his salvation did come in answer to prayer' and 'The ways of God are mysterious' (1844). Two in-span private letters carry the score at 0.7; S5 and the Rigi diary are independent agreeing sources → corroborated (P48)."
      how_known: "Own letters and diary (S2); WallBuilders manuscript letter of 1836 (S5)."
    B_cause: {value: BELOW_THRESHOLD, how_known: "Not a scientist (P33: inventions), so B needs a statement of his about nature (P16). Closest own words: after the span he reads a physical accident (a fall that wounded his leg) as providential: 'The ways of God are mysterious, and I find prayer answered in a way not at all anticipated. This accident, as we are apt to call it, I can plainly see is calculated to effect many salutary objects' (23 June 1844). A God who answers prayer through events is BELOW_THRESHOLD evidence by analogy with the petitionary-prayer addendum (P16, RQ-AU1), with B 1 at 0.5 as the named reading (after the span, P1 cap 0.5 in any case). Ruling X1 (v8's call on the auditor's advice): stays BELOW_THRESHOLD, named reading 1 (2 a further reading). It is one private letter, after the span, and the answer comes through an 'accident, as we are apt to call it', providence working through ordinary events, not an exception to nature's course; a reported answer to one's own prayer through ordinary events is E evidence, not B; only an answer claimed against or beyond nature's course bears on B. Deepen D1: Rankin recollection (S2 vol. II ch. XXIII; reported speech) that Morse said God 'created the great forces of nature… as expressions of good-will to man' is teleology/providence, not a P16 lawful-order or exception claim, and cannot score alone (§7). No own-voice 'laws of nature' / exceptionless-order statement found in Letters and Journals (both vols.), Foreign Conspiracy (1835), or the 1868 banquet speech ('Science and Art are not opposed' is about art). Keep B BELOW."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read on reward or punishment of persons (P19)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read on revelation against observation; 'Science and Art are not opposed' (1868) is about art (P19)."}
    E_scope:
      value: 1
      basis: consistent_private_letters
      certainty: 0.5
      support: single
      cites: [{source: S2, locator: "vol. II ch. XXIV (8 November 1837)"}, {source: S2, locator: "vol. II ch. XXX (31 May 1844)"}]
      rationale: "Scored on the world's order (P7): favour in providence for himself. 'Through a kind Providence, I have been thrown among most attentive, and kind, and skilful friends' (1837, in span); 'It is his work, and He alone could have carried me thus far through all my trials and enabled me to triumph over the obstacles, physical and moral' and 'none but He who has all hearts in his hands ... could so have brought light out of darkness' (1844, after span). Leans to the pole, limited to his own affairs. Named alternative BELOW_THRESHOLD: 'a kind Providence' may be a set phrase (as for the formulas in ruling U2)."
      how_known: "Own letters; the strongest wording is after the span. Single source id (S2) → support single (P48)."
      alternatives:
        - {value: BELOW_THRESHOLD, note: "Providence formulas as conventional phrasing.", cites: [{source: S2, locator: "vol. II ch. XXIV"}]}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 0 at 0.7 but B BELOW_THRESHOLD; no branch of the P4 test is met (P19)."}
  statements:
    - text: "But, through a kind Providence, I have been thrown among most attentive, and kind, and skilful friends, who have treated me more like one of their own children than like a stranger."
      cites: [{source: S2, locator: "vol. II ch. XXIV, letter to Sidney Morse, Morristown, 8 November 1837"}]
      date: "1837-11-08"
      context: "On an illness while building the telegraph machinery at the Vails' in Morristown."
      axes: [A_locus, E_scope]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "Letters and Journals, ed. Edward Lind Morse (1914), Project Gutenberg #11018; web copy without page images (0.7 cap)."
    - text: "I see nothing now but an unclouded prospect, for which let us pay to Him who shows it to us the homage of grateful and obedient hearts, with most earnest prayers for grace to use prosperity aright."
      cites: [{source: S2, locator: "vol. II ch. XXIV, letter to Alfred Vail, 15 March 1838"}]
      date: "1838-03-15"
      context: "While a congressional appropriation for the telegraph still seemed possible."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "As above."
    - text: "Is it likely that we, Protestant republicans of the United States, have won the kind regards of the Austrian government, which has been the persevering foe of the Reformation and its republican fruits since the days of Luther?"
      cites: [{source: S3, locator: "p. 30"}]
      date: "1835"
      context: "Foreign Conspiracy, on Austria's support for Catholic missions in the United States."
      axes: []
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-19
      note: "1835 Leavitt, Lord edition, archive.org scan, read through its OCR text (page image not viewed; OCR line breaks and hyphens removed); published under the pseudonym Brutus. Membership-level identification only; scores no axis."
    - text: "It is his work, and He alone could have carried me thus far through all my trials and enabled me to triumph over the obstacles, physical and moral, which opposed me."
      cites: [{source: S2, locator: "vol. II ch. XXX, letter to Sidney Morse, 31 May 1844"}]
      date: "1844-05-31"
      context: "A week after the first public message on the Washington–Baltimore line ('What hath God wrought!', chosen by Annie Ellsworth)."
      axes: [A_locus, E_scope]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "After the span (P1 cap 0.5)."
    - text: "The ways of God are mysterious, and I find prayer answered in a way not at all anticipated. This accident, as we are apt to call it, I can plainly see is calculated to effect many salutary objects."
      cites: [{source: S2, locator: "vol. II ch. XXXI, letter to Sidney Morse, 23 June 1844"}]
      date: "1844-06-23"
      context: "On a leg wound from a fall that kept him in bed; the letter adds that 'his salvation did come in answer to prayer'."
      axes: [B_cause]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "After the span (P1 cap 0.5)."
    - text: "If not a sparrow falls to the ground without a definite purpose in the plans of infinite wisdom, can the creation of an instrumentality so vitally affecting the interests of the whole human race have an origin less humble than the Father of every good and perfect gift?"
      cites: [{source: S2, locator: "vol. II ch. XXXIX, speech at the banquet at Delmonico's, New York, 30 December 1868"}]
      date: "1868-12-30"
      context: "Closing words of his public speech at the banquet in his honour presided over by Chief Justice Chase."
      axes: [A_locus, E_scope]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "Speech text as printed by his son (1914). After the span (P1 cap 0.5)."
    - text: "I am alone on the mountain with such a scene spread before me that I must adore, and weak, indeed, must be that faith which, on this day, in such a scene, does not lift the heart from nature up to nature's God."
      cites: [{source: S2, locator: "vol. I ch. XVIII, diary entry, summit of the Rigi, 28 August 1831"}]
      date: "1831-08-28"
      context: "European art-study travel; sunrise from the Rigi after describing sublimity as an 'emotion of taste' that may coexist with true religious feeling; he distinguishes mere taste from devotion to 'that Being by whom these wonders were created'."
      axes: [A_locus]
      kind: "notebook or diary"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Letters and Journals, ed. Edward Lind Morse (1914), Project Gutenberg #11017; before the span. Nature → Creator; not a P16 lawful-order claim (scores A, not B)."
    - text: "Yield then thy pen to God to draw / On the next leaf his perfect law / To when thy book of life is done / Cleans'd by the blood of God's own son / From Sin's dark blots, and Folly's stain / A purer volume shall remain / And rest, (to Grace a splendid prize,) / In Heaven's alcoves in the skies."
      cites: [{source: S5, locator: "letter to Mary Pattison, New York, 14 September 1836"}]
      date: "1836-09-14"
      context: "Private letter enclosing album verses; Morse adds 'The moral is better than the poetry'."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "primary facsimile"
      verified_on: 2026-10-24
      note: "WallBuilders Library manuscript letter (images on the cited page). Just before the span. Christian transcendent God / Christ; corroborates A (P48)."
    - text: "He had been long impressed with the belief that God had created the great forces of nature, not only as manifestations of his own infinite power, but as expressions of good-will to man, to do him good, and that every one of God's great forces could yet be utilized for man's welfare."
      cites: [{source: S2, locator: "vol. II ch. XXIII, Robert G. Rankin reminiscence of a conversation c. fall 1835"}]
      date: "1835"
      context: "Rankin's later recollection (via Prime) of Morse explaining magnetism at the unfinished University building; Rankin says 'if I do not recollect the very words… they were substantially as follows'."
      axes: []
      kind: "reported speech"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Reported speech (§7): lead only; cannot score B alone. Teleology/providence of forces for man's welfare, not a P16 statement of nature's lawful course or exception. Deepen D1 negative B check."
  changes_over_life: []
  coder_notes: "Span: 1837 (telegraph, the patent caveat of 3 October 1837, its first public statement under P30 #1; batch X audit, MO2) to 1838 (Morse Code). Earlier private stages: 1832 (idea) and 1835 (first working model), Britannica's range 1832–35; 1844 (first line) is the completion of the telegraph, not a separate listed item. Not a scientist (P33). The two in-span letters carry the code and A; the strongest wording (answered prayer, providence in his trials) is from 1844 and later. The Rankin recollection (S2 vol. II ch. XXIII) has Morse say God created nature's forces 'as expressions of good-will to man'; reported speech (§7), a lead only. Editor's phrases ('his belief that he was but a chosen vessel') are not his words. Ruling X1 keeps B BELOW_THRESHOLD. Deepen D1 (2026-10-24): A corroborated (P48) via S5 1836 letter + Rigi 1831; Rankin and full Letters search yield no P16 B lift."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "New England Protestant (Congregational clergy family)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Congregationalism", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica (father's church)."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1837–1838", certainty: 0.7, cites: [{source: S2, locator: "vol. II chs. XXIII–XXIV (caveat, 3 October 1837)"}, {source: S1, locator: "opening; telegraph paragraph"}], how_known: "From the telegraph (patent caveat, 3 October 1837; P30 #1) to the Morse Code (1838) (P30). Earlier private stages in coder_notes."}
  age_at_first_lasting_contribution: {value: 46, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "vol. II ch. XXIII"}], how_known: "1837 − 1791 = 46 (P30)."}
  first_evidence_of_lio_type_views: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "letters read"}], how_known: "No axis scored at 3 or 4."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "letters read"}], how_known: "As above."}
  worldview_during_major_work: {value: "CHRIST: prayer to a provident God (1837, 1838)", certainty: 0.7, cites: [{source: S2, locator: "vol. II ch. XXIV"}], how_known: "In-span letters."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Not assessed."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Not assessed."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "Inventor as instrument of providence."
  notes: ""

institutions:
  - {value: "National Academy of Design", role: "founder and first president", years: "1826–1845", kind: "academy or learned society", certainty: 0.7, cites: [{source: S1, locator: "leadership paragraph"}], how_known: "Britannica."}
  - {value: "University of the City of New York (later New York University)", role: "teacher of art", years: UNKNOWN, kind: university, certainty: 0.7, cites: [{source: S1, locator: "telegraph paragraph"}], how_known: "Britannica; years not given."}
  - {value: "Vassar College", role: "founder and trustee", years: UNKNOWN, kind: university, certainty: 0.7, cites: [{source: S1, locator: "old age paragraph"}], how_known: "Britannica."}
collaborators:
  - {value: "Alfred Vail", relation: collaborator, note: "co-developer of the code; partner in telegraph rights", certainty: 0.7, cites: [{source: S1, locator: "telegraph paragraph"}], how_known: "Britannica."}
  - {value: "Leonard Gale", relation: collaborator, note: "chemist; introduced Joseph Henry's work; partner", certainty: 0.7, cites: [{source: S1, locator: "telegraph paragraph"}], how_known: "Britannica."}
  - {value: "Joseph Henry", relation: other, note: "his electromagnets made long-distance signalling possible", certainty: 0.7, cites: [{source: S1, locator: "telegraph paragraph"}], how_known: "Britannica."}
  - {value: "Washington Allston", relation: teacher, note: "painting, England, from 1811", certainty: 0.7, cites: [{source: S1, locator: "early career paragraph"}], how_known: "Britannica."}
  - {value: "Jedidiah Morse", relation: family, note: "father", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 128"}], how_known: "Study roster."}
  controversies:
    - {value: "Ran on anti-immigrant and anti-Roman Catholic tickets for mayor of New York (1836, 1841); wrote against a 'Popery' conspiracy", certainty: 0.7, cites: [{source: S1, locator: "telegraph paragraph"}, {source: S3, locator: "title page"}], how_known: "Britannica and his pamphlet."}
    - {value: "Controversies 'in politics with the Irish and abolitionists' and priority disputes over the telegraph", certainty: 0.7, cites: [{source: S1, locator: "controversy paragraph"}], how_known: "Britannica."}
  data_quality_flags:
    - "Letters read in his son's 1914 edition on Project Gutenberg (no page images)."
    - "S5 WallBuilders transcript checked against manuscript images on the same page (2026-10-24)."
  open_questions:
    - "RQ-X1 closed for deepen D1: B stays BELOW under Ruling X1; no true P16 nature-order own-voice found."
    - "Any later Morse essay on Bible-and-sciences lectureship content (Wikipedia/Standage lead) that might state nature's lawful order."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Carleton Mabee; Britannica Editors"
    citation: "Mabee, Carleton, and Britannica Editors. \"Samuel F.B. Morse.\" Encyclopaedia Britannica (updated 10 October 2026). https://www.britannica.com/biography/Samuel-F-B-Morse. Read live 2026-10-19."
    url: "https://www.britannica.com/biography/Samuel-F-B-Morse"
    accessed: 2026-10-19
    reliability_note: "Signed article by his biographer; Quick Facts and body cited; Top Questions used only where the body agrees."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators, review]
  - id: S2
    type: primary
    kind: "scholarly edition"
    author: "Samuel F. B. Morse; ed. Edward Lind Morse"
    citation: "Morse, Edward Lind, ed. Samuel F. B. Morse: His Letters and Journals. 2 vols. 1914 (vol. II 'Published November 1914'). Project Gutenberg eBooks #11017 (vol. I) and #11018 (vol. II). https://www.gutenberg.org/ebooks/11018"
    url: "https://www.gutenberg.org/ebooks/11018"
    accessed: 2026-10-19
    reliability_note: "Edited letters with the editor's narrative; only Morse's own letters and speeches are quoted as his words. Gutenberg text without page images (web copy, 0.7 cap); cited by volume, chapter and letter date. Publisher not shown in the Gutenberg text. Houghton Mifflin, Boston, 1914."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, timing]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Samuel F. B. Morse (as 'Brutus')"
    citation: "[Morse, Samuel F. B.] Foreign Conspiracy against the Liberties of the United States: The Numbers of Brutus. New York: Leavitt, Lord & Co., 1835. Internet Archive foreignconspiracy00morsrich (UC Berkeley copy). https://archive.org/details/foreignconspiracy00morsrich"
    url: "https://archive.org/details/foreignconspiracy00morsrich"
    accessed: 2026-10-19
    reliability_note: "Library scan of the 1835 edition; read through the OCR text with printed page headers. Authorship: his letter of 20 May 1835 speaks of 'the charge I have made' (S2 vol. II ch. XXII)."
    source_quality: "primary / own words"
    used_for: [worldview, review]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S5
    type: primary
    kind: letter
    author: "Samuel F. B. Morse"
    citation: 'Morse, Samuel F. B. Letter to Mary Pattison, New York, 14 September 1836. WallBuilders Library (manuscript images and transcript). https://wallbuilders.com/resource/samuel-f-b-morse-what-hath-god-wrought/'
    url: "https://wallbuilders.com/resource/samuel-f-b-morse-what-hath-god-wrought/"
    accessed: 2026-10-24
    reliability_note: "Manuscript images of Morse's hand and a full transcript on the page; album poem on God / God's own son used for A. Advocacy site framing ignored; only the letter text used."
    source_quality: "primary / own words"
    used_for: [worldview]
  - id: S6
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: '"Samuel Morse." Wikipedia (English). https://en.wikipedia.org/wiki/Samuel_Morse'
    url: "https://en.wikipedia.org/wiki/Samuel_Morse"
    accessed: 2026-10-24
    reliability_note: "P50 dual bio check only: birth 1791-04-27 Charlestown and death 1872-04-02 New York City agree with Britannica (S1). Anti-Catholic and charity paragraphs used as leads, not as axis evidence."
    source_quality: "reference entry"
    used_for: [identity, review]
---

# Samuel Morse

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Samuel F. B. Morse (1791–1872), American painter and inventor of an electric telegraph and, with Alfred Vail, the Morse Code [S1]. Deepen D1: primary_system CHRIST (0.7); A 0 (0.7, support corroborated); B BELOW_THRESHOLD (Ruling X1; no P16 lift); mid_basin BELOW_THRESHOLD. Not plotted.

## Life and work

Painter trained under Allston; president of the National Academy of Design; telegraph conceived 1832, patent caveat 1837; first line 1844 [S1; S2].

## Contribution and impact

Electric telegraph (1832–35), Morse Code (1838), portraits [S1].

## Childhood and education

Son of the Congregational clergyman Jedidiah Morse; Phillips Academy and Yale [S1].

## Adult working worldview

Prayer to a provident God in his letters [S2]; Rigi diary nature-God language (1831) [S2]; 1836 album poem on God and Christ [S5]; self-identified Protestant [S3]. B stays BELOW under Ruling X1 [S2].

## Heritage (context only)

Congregational [S1].

## Timing

1837–1838, from age 46 [S1; S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Not assessed [S1].

## Open questions

- RQ-X1 closed for deepen D1 (B stays BELOW; no P16).
- Bible-and-sciences lectureship content (Standage/Wikipedia lead).

## Research log

- 2026-10-19: Read Britannica (Mabee), the Letters and Journals (Gutenberg) and Foreign Conspiracy (archive.org).
- 2026-10-24: Deepen D1 — re-read Letters and Journals vols. I–II (Gutenberg) for P16; Rigi diary 1831; WallBuilders 1836 letter (S5); Wikipedia EN (P50); Rankin reported speech logged as negative B check. No figures/. No fallacy_catalog.
