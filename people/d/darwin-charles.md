---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch B)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (stage 3 batch B). Basics from Britannica (Desmond, first page). Worldview from the Autobiography (Barlow ed. 1958, Darwin Online; pp. 87 and 94 checked on the page scans), three letters in the Darwin Correspondence Project (Gray 1860, Fordyce 1879, McDermott 1880), the DCP essay 'What did Darwin believe?', the Origin (1859, p. 488 checked on the scan) and the Descent (1871). primary_system BELOW_THRESHOLD (AGNOS candidate, stub). A 2 (0.7), B 4 (0.7), C 4 (0.7), D 4 (0.7), E 4 (0.7); mid_basin TODO (A = 2). All scores are drafts for v8's review. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit fixes, stage 3 batch B (two blind runs at 3db6511). #14, #15: geologist and geology now cite Britannica's later sections ('The London years, 1836–42'; 'The squire naturalist in Downe'), not the opening. #32: Paley taken out of early_geometric_style_reasoning (read for the B.A. of January 1831, at about 21; S1 p. 59 and footnote), and key_early_reading dated. #65: Beagle role is 'self-financed gentleman companion' to Fitzroy, not surgeon-naturalist (Britannica). #39: value unchanged; the reason now names its actual basis (v8's batch instructions, not a written rule) and says it awaits v8's ruling. #50: the mid_basin TODO now cites CODING_GUIDE §6 (P4) instead of an unwritten rule. Left for v8 as method questions: #7/#9 (whether Coral Reefs, 1842, must be listed; it would move the era) and #39 (stub systems). Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 rulings P14–P28 (v8, main 6aeba87), schema 1.3. primary_system BELOW_THRESHOLD → DEISM 0.5 for the Origin years (alternative CLASS_THEISM; RATN considered and rejected under P22; revelation test met, P27; AGNOS moved to changes_over_life) (P20); secondary UNKNOWN → BELOW_THRESHOLD (1860 agnostic strand) (P19); A_locus 2 → 1 (0.7), scored for 1859 (P20); B_cause 4 → 3 (0.7): the 1859 book states one limited exception, the creation of the first forms (B 3 anchor, P27); mid_basin TODO → true (0.7), unchanged by B 3, flagged as a sensitive result for lens; Coral Reefs (1842) listed, first_lasting_contribution_year 1859 → 1842 and the 1859 alternative dropped (P17, P23), era 1850 to 1949 → 1750 to 1849 (CODING_GUIDE §8, P2), age 50 → 33; first_evidence_of_lio_type_views late 1830s → 1859, the earliest dated statement of his own scored at 3 or 4 (P27); Autobiography quotes kind notebook or diary → autobiography (P18) and checked against a scholarly edition (P21); Origin p. 489 and Descent quotes → primary transcription (P21); new statement Origin p. 490; single-source 1.0 fields rechecked (P15) (region_of_work, definition_fit → 0.7; region_of_birth, sex keep 1.0 with a second cite). New source S10 (Coral Reefs). Not reviewed."}

identity:
  id: darwin-charles
  display_name: "Charles Darwin"
  roster:
    canonical_name: "Charles Darwin"
    rank: 16
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: biology
    field_bucket: "biology / life science"
  full_name: {value: "Charles Robert Darwin", certainty: 0.7, cites: [{source: S8, locator: "'Also known as' line"}], how_known: "Britannica only."}
  native_name: {value: "Charles Robert Darwin (English)", certainty: 0.7, cites: [{source: S8, locator: "'Also known as' line"}], how_known: "English name."}
  aliases:
    - {name: "Charles-Darwin", kind: "roster alias"}
    - {name: "Darwin-Charles", kind: "roster alias"}

basics:
  birth:
    date: {value: "1809-02-12", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "p. 21"}, {source: S8, locator: "Born line"}], how_known: "His own statement and Britannica agree."}
    place: {value: "Shrewsbury", modern_name: "Shrewsbury, Shropshire, England, UK", polity_then: "United Kingdom", certainty: 1.0, cites: [{source: S1, locator: "p. 21"}, {source: S8, locator: "Born line"}], how_known: "Two sources agree."}
  death:
    date: {value: "1882-04-19", calendar: gregorian, certainty: 0.7, cites: [{source: S8, locator: "Died line"}], how_known: "Britannica only."}
    place: {value: "Downe, Kent", modern_name: "Downe, London Borough of Bromley, England, UK", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S8, locator: "Died line"}], how_known: "Britannica only."}
  first_lasting_contribution_year:
    value: 1842
    certainty: 0.7
    cites: [{source: S10, locator: "title page; preface signed '2nd May, 1842', p. vi"}, {source: S8, locator: "'The Beagle voyage' ('He imagined (correctly) that those reefs grew on sinking mountain rims'); 'The squire naturalist in Downe' (books on coral reefs 'secured his reputation')"}]
    how_known: "Under the first-lasting-year rules (P17, P23) with P12 and P13: the year of the earliest listed lasting contribution, now the coral-reef theory as published in The Structure and Distribution of Coral Reefs (1842; S10). Britannica, the source that names it, calls the theory correct (S8, 'The Beagle voyage'). 0.7: one source for its lasting status (P15), and named alternatives. The item is dated by the published book (S10, title page), as v8 answered on 2026-10-02; the sources date different stages of one theory (formed by April 1836, read in 1837, published in 1842), which is not a disagreement between sources (P25), so 0.7, not 0.5. The Origin (1859) is no longer an alternative: it could set the year only if Coral Reefs were taken off the list, which P23 rules out. The Journal of Researches (1839) is not listed: Britannica says only that he 'became well known' through it, not that it is lasting."
    alternatives:
      - {value: 1837, cites: [{source: S10, locator: "p. 4, footnote ('A brief account of my views on coral formations [...] was read May 31, 1837, before the Geological Society')"}], note: "If the coral-reef item is dated from its first public statement rather than the book (P12 would then read it as a range 1837–1842). Same era bucket, 1750 to 1849."}
      - {value: 1836, cites: [{source: S8, locator: "'The Beagle voyage' ('By April 1836 [...] Darwin already had his theory of reef formation')"}], note: "If the item is dated from when he formed the theory, on the voyage. Same era bucket."}
  era_bucket: {value: "1750 to 1849", certainty: 0.7, cites: [{source: S10, locator: "title page"}, {source: S8, locator: "'The Beagle voyage'"}], how_known: "The bucket follows first_lasting_contribution_year (CODING_GUIDE §8; P2), now 1842, Coral Reefs by its publication year (P17, P23). Every candidate year now listed (1842, 1837, 1836) is in 1750 to 1849. Kept at 0.7 because the coral-reef item's lasting status rests on Britannica alone (P15); without that item the year would be 1859, in 1850 to 1949."}
  region_of_birth: {value: "Northern Europe", certainty: 1.0, cites: [{source: S8, locator: "Born line"}, {source: S1, locator: "p. 21 ('I was born at Shrewsbury')"}], how_known: "Two sources give Shrewsbury; UK is Northern Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S8, locator: "opening; Died line"}], how_known: "Worked in England (Down House, Kent) after the Beagle voyage. One source cited, so 0.7 under the single-source rule (P15)."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S8, locator: "opening"}, {source: S1, locator: "pp. 22–23, Francis Darwin's note ('both he and his brother')"}], how_known: "As two sources record it."}
  languages_of_work: {value: [English], certainty: 1.0, cites: [{source: S6, locator: "title page"}], how_known: "His books are in English."}
  occupations: {value: ["naturalist", "geologist"], certainty: 0.7, cites: [{source: S8, locator: "opening ('English naturalist')"}, {source: S8, locator: "'Evolution by natural selection: the London years, 1836–42' ('a gentleman geologist') and 'The squire naturalist in Downe' (books on coral reefs and South American geology 'secured his reputation as a career geologist'), section pages reopened 2026-10-02"}], how_known: "Britannica: 'naturalist' in the opening; 'geologist' in the later sections named in the second cite (the opening does not say it)."}

contribution:
  fields: {value: ["natural history", "evolutionary biology", "geology"], certainty: 0.7, cites: [{source: S8, locator: "opening"}, {source: S8, locator: "'Evolution by natural selection: the London years, 1836–42' ('a gentleman geologist') and 'The squire naturalist in Downe' (books on coral reefs and South American geology 'secured his reputation as a career geologist'), section pages reopened 2026-10-02"}], how_known: "Britannica: natural history and evolutionary studies in the opening; geology in the later sections named in the second cite."}
  lasting_original_contributions:
    - {value: "Subsidence theory of coral-reef formation: atolls and barrier reefs grow upward as their foundations sink (The Structure and Distribution of Coral Reefs)", year: "1842", kind: theory, lasting: "Britannica calls it correct ('He imagined (correctly) that those reefs grew on sinking mountain rims')", certainty: 0.7, cites: [{source: S10, locator: "p. 4 ('both in atolls and barrier-reefs, the foundation on which the coral was primarily attached, has subsided; and that during this downward movement, the reefs have grown upwards'); title page"}, {source: S8, locator: "'The Beagle voyage'; 'The squire naturalist in Downe'"}], how_known: "His own book (S10) for the theory and date; Britannica alone for its being correct, so 0.7. Added under the first-lasting-year rules (P17, P23). Darwin says a brief account was read on 31 May 1837 (S10, p. 4, footnote). The item's year is the book's publication (S10, title page), as v8 answered on 2026-10-02 (P17, P23)."}
    - {value: "Theory of evolution by natural selection", year: "1859", kind: theory, lasting: "foundation of modern biology", certainty: 1.0, cites: [{source: S6, locator: "pp. 488–490"}, {source: S8, locator: "opening"}], how_known: "His own book and Britannica."}
    - {value: "Descent of humans from earlier, less highly organised forms", year: "1871", kind: theory, lasting: "standard biology", certainty: 1.0, cites: [{source: S7, locator: "vol. 2, p. 385"}], how_known: "His own book."}
  evidence_of_impact:
    - {value: "Burial in Westminster Abbey", kind: other, certainty: 0.7, cites: [{source: S8, locator: "opening ('accorded the ultimate British accolade of burial in Westminster Abbey')"}], how_known: "Britannica; a posthumous honour."}
  major_works:
    - {value: "On the Origin of Species by Means of Natural Selection", year: 1859, kind: book, certainty: 1.0, cites: [{source: S6, locator: "title page"}, {source: S8, locator: "opening"}], how_known: "Read on Darwin Online."}
    - {value: "The Descent of Man, and Selection in Relation to Sex", year: 1871, kind: book, certainty: 1.0, cites: [{source: S7, locator: "vol. 2"}], how_known: "Read on Darwin Online."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founder of the theory of evolution by natural selection.", certainty: 0.7, cites: [{source: S8, locator: "opening"}], how_known: "One source cited, so 0.7 under the single-source rule (P15)."}

childhood:
  family_religion: {value: "Mixed: Unitarian mother; the children christened in the Church of England", certainty: 0.7, cites: [{source: S1, locator: "pp. 22–23, Francis Darwin's note"}, {source: S8, locator: "'Early life and education'"}], how_known: "Francis Darwin's note in the Autobiography: 'Mrs. Darwin was a Unitarian'; 'both he and his brother were christened and intended to belong to the Church of England'. Britannica: mother the daughter of 'the Unitarian pottery industrialist Josiah Wedgwood'."}
  family_religious_practice: {value: "As a small child he went to the school of the Unitarian minister, Mr Case", certainty: 0.7, cites: [{source: S1, locator: "pp. 22–23"}], how_known: "Autobiography and Francis Darwin's note."}
  parents_and_household:
    - {value: "Father, Robert Waring Darwin, society doctor", name: "Robert Waring Darwin", role: father, certainty: 0.7, cites: [{source: S8, locator: "'Early life and education'"}], how_known: "Britannica."}
    - {value: "Mother, Susannah Wedgwood, daughter of Josiah Wedgwood; died July 1817, when he was eight", name: "Susannah Darwin (née Wedgwood)", role: mother, certainty: 0.7, cites: [{source: S8, locator: "'Early life and education'"}, {source: S1, locator: "p. 22"}], how_known: "Britannica (name); Autobiography (death)."}
  household_circumstances: {value: "Prosperous medical family; second son", certainty: 0.7, cites: [{source: S8, locator: "'Early life and education'"}], how_known: "Britannica."}
  schooling:
    - {value: "Shrewsbury School (Anglican; classics by rote)", stage: "grammar or secondary school", years: "1818–1825", certainty: 0.7, cites: [{source: S8, locator: "'Early life and education'"}], how_known: "Britannica."}
    - {value: "Euclid with a private tutor", stage: tutor, years: TODO, certainty: 1.0, cites: [{source: S1, locator: "p. 43"}], how_known: "His own account."}
    - {value: "University of Edinburgh, medicine", stage: university, years: "1825–1827", certainty: 0.7, cites: [{source: S8, locator: "'Early life and education'"}], how_known: "Britannica ('his two years at Edinburgh')."}
    - {value: "Christ's College, Cambridge (intended for the church)", stage: university, years: "1828–", certainty: 0.7, cites: [{source: S8, locator: "'Early life and education'"}], how_known: "Britannica."}
  early_mathematics: {value: "geometry (Euclid-style proof)", note: "'I was taught Euclid by a private tutor, and I distinctly remember the intense satisfaction which the clear geometrical proofs gave me.'", certainty: 1.0, cites: [{source: S1, locator: "p. 43"}], how_known: "His own account."}
  early_geometric_style_reasoning: {value: "Euclid with a private tutor while at school", certainty: 0.7, cites: [{source: S1, locator: "p. 43 ('I was taught Euclid by a private tutor'); p. 59 ('Euclid, which latter gave me much pleasure, as it did whilst at school')"}], how_known: "His own account. Paley is not counted here: he read Paley's Evidences and Natural Theology for his B.A. examination in his last Cambridge year (S1, p. 59; Francis Darwin's footnote there: 'Tenth in the list of January 1831'), at about 21, not in childhood."}
  early_science_exposure:
    - {value: "Edinburgh: dissenting science and Robert Edmond Grant", year: 1825, age: 16, certainty: 0.7, cites: [{source: S8, locator: "'Early life and education'"}], how_known: "Britannica."}
  key_early_reading:
    - {value: "Paley, Evidences of Christianity and Natural Theology (Cambridge, last year before the B.A. of January 1831, at about 21; after childhood)", certainty: 1.0, cites: [{source: S1, locator: "p. 59 and footnote"}], how_known: "His own account; the date is from Francis Darwin's footnote ('Tenth in the list of January 1831')."}
  childhood_mentors: []
  languages_in_childhood: {value: [English], certainty: 0.7, cites: [{source: S8, locator: "'Early life and education'"}], how_known: "English family."}
  notable_events:
    - {value: "Death of his mother", year: "1817", age: 8, certainty: 1.0, cites: [{source: S1, locator: "p. 22"}], how_known: "His own account."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1831–1882", certainty: 0.7, cites: [{source: S8, locator: "opening"}], how_known: "From the Beagle voyage to his death."}
  nominal_affiliations: []
  self_described_science_religion_relation:
    value: "Laws of nature leave no room for design in variation or for miracles ('Everything in nature is the result of fixed laws'; 'the more we know of the fixed laws of nature the more incredible do miracles become'), while the first cause stays an open question: 'The mystery of the beginning of all things is insoluble by us'. He held his theory compatible with theism ('absurd to doubt that a man may be an ardent Theist & an evolutionist')."
    certainty: 0.7
    cites: [{source: S1, locator: "pp. 86, 87, 94"}, {source: S2, locator: "letter text"}]
    how_known: "His own private writing (Autobiography for his family; private letter)."
  primary_system:
    value: DEISM
    basis: consistent_private_letters
    certainty: 0.5
    cites: [{source: S1, locator: "pp. 92–93 (checked on the page scan)"}, {source: S1, locator: "pp. 85–87"}, {source: S6, locator: "p. 488"}, {source: S3, locator: "letter text"}]
    how_known: "Coded for the working years of the major work, the Origin (1859), the same period as A_locus (CODING_GUIDE §5, 'Changes over life'; P20). His own retrospective words: 'When thus reflecting I feel compelled to look to a First Cause having an intelligent mind in some degree analogous to that of man; and I deserve to be called a Theist. This conclusion was strong in my mind about the time, as far as I can remember, when I wrote the Origin of Species; and it is since that time that it has very gradually with many fluctuations become weaker' (S1, pp. 92–93). He reached it by reason, from 'the extreme difficulty or rather impossibility of conceiving this immense and wonderful universe [...] as the result of blind chance or necessity' (p. 92), and had already given up revelation and miracles in 1836–39 (S1, pp. 85–87). The Origin's 'laws impressed on matter by the Creator' and 'secondary causes' (S6, p. 488) and the 1860 'designed laws' (S3) agree."
    rationale: "Draft judgment (one line): DEISM, because his own writing affirms a creator known by reason and rejects revelation and miracles (systems/DEISM.md use_when); he called himself a 'Theist', not a deist, so the code is the coder's mapping. Certainty 0.5, not 0.7: the passage is a retrospective self-report (main text 1876) and it hedges. The dating sentence is a later addendum (S1, p. 93, footnote: 'Addendum of four lines added later'), it says 'as far as I can remember', the next sentence asks whether 'the mind of man [...] be trusted when it draws such grand conclusions', and the 1860 letter adds 'Not that this notion at all satisfies me' (S3). 'with many fluctuations' describes the weakening after the Origin, not 1859 itself. Revelation test (P27): met; he rejects revelation as a source of truth ('I do not believe in the Bible as a divine revelation', S4; disbelief 'at last complete', S1, p. 87). His route to the First Cause argues from the world, the universe being inconceivable 'as the result of blind chance or necessity' (S1, p. 92), so RATN, which P22 keeps for arguments from the idea of God, does not apply. Named alternative: CLASS_THEISM, which also argues from the world to a first cause (P22) and treats nature as an order of secondary causes, but nothing read holds God simple or immutable. AGNOS, his later self-description, is in changes_over_life."
  secondary_system: {value: BELOW_THRESHOLD, note: "Some evidence of an agnostic strand in the Origin years: in 1860 he wrote of 'designed laws' and added 'Not that this notion at all satisfies me. I feel most deeply that the whole subject is too profound for the human intellect' (S3). Too weak to code a second system for that period; the full agnosticism is later (changes_over_life).", how_known: "Rechecked for the 1859 period after primary_system was moved to it; some evidence, not enough (P19)."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Not coded as primary: his own later self-description, 'content to remain an Agnostic' (S1, p. 94, 1876) and 'an agnostic would be the most correct description of my state of mind' (S2, 1879), which is after the major work; recorded in changes_over_life. The DCP editors add: 'Is he then an agnostic? Yes, but not all of the time' (S5). AGNOS is a stub system file (flag, sourcing backlog).", cites: [{source: S1, locator: "p. 94"}, {source: S2, locator: "letter text"}, {source: S5, locator: "section on the Fordyce letter"}]}
    - {code: DEISM, reason: "Coded at 0.5 (primary_system) for the Origin years: a First Cause 'having an intelligent mind' reached by reason (S1, pp. 92–93), revelation and miracles given up in 1836–39 (S1, pp. 85–87), species by 'secondary causes' under 'laws impressed on matter by the Creator' (S6, p. 488), and 'designed laws' (S3). He called himself a 'Theist', not a deist. Meets the revelation test (P27): 'I do not believe in the Bible as a divine revelation' (S4). DEISM is a draft system file.", cites: [{source: S1, locator: "pp. 85–87, 92–93"}, {source: S6, locator: "p. 488"}, {source: S3, locator: "letter text"}]}
    - {code: CLASS_THEISM, reason: "Runner-up (named alternative): argues to a First Cause by reason (S1, p. 92) and treats nature as an order of 'secondary causes' (S6, p. 488), two of the three use_when tests in systems/CLASS_THEISM.md; but nothing read holds God simple, immutable or impassible, and he had given up revelation (S1, pp. 85–87), which CLASS_THEISM keeps. His argument is a posteriori, as P22 asks of CLASS_THEISM, but it does not reach the simple, immutable God that P22's line names. CLASS_THEISM is a draft system file.", cites: [{source: S1, locator: "pp. 85–87, 92"}, {source: S6, locator: "p. 488"}]}
    - {code: RATN, reason: "Rejected (P22): RATN is for arguments to God from the idea of God or from reason alone; his First Cause argument runs from the world, the impossibility of conceiving 'this immense and wonderful universe' as 'the result of blind chance or necessity' (S1, p. 92). RATN is a stub system file (flag, P14).", cites: [{source: S1, locator: "p. 92"}]}
    - {code: CHRIST, reason: "Rejected: 'quite orthodox' only on the Beagle (S1, p. 85); later 'I do not believe in the Bible as a divine revelation, & therefore not in Jesus Christ as the son of God' (S4).", cites: [{source: S1, locator: "p. 85"}, {source: S4, locator: "letter text"}]}
    - {code: ATHE, reason: "Rejected: 'In my most extreme fluctuations I have never been an atheist in the sense of denying the existence of a God' (S2). ATHE is a stub system file (flag).", cites: [{source: S2, locator: "letter text"}]}
  lio_axes:
    A_locus:
      value: 1
      basis: consistent_private_letters
      certainty: 0.7
      cites: [{source: S1, locator: "pp. 92–93"}, {source: S6, locator: "p. 488"}, {source: S3, locator: "letter text"}]
      how_known: "Scored for his worldview during the major work, the Origin of 1859, under the major-work-period rule (P20), the same period as primary_system. Contemporary evidence carries it: the Origin's public wording (1859) and an 1860 private letter; his retrospective account (Autobiography) agrees but is hedged (see primary_system). Named alternatives cap it at 0.7. Changed from 2 (which averaged the Origin-era theism with the later agnosticism). Sensitive: see mid_basin."
      rationale: "Draft judgment (one line): leans to the transcendent-person pole with limits. Around the Origin he felt 'compelled to look to a First Cause having an intelligent mind in some degree analogous to that of man; and I deserve to be called a Theist. This conclusion was strong in my mind about the time, as far as I can remember, when I wrote the Origin of Species' (S1, pp. 92–93); the Origin speaks of 'the laws impressed on matter by the Creator' (S6, p. 488); in 1860 he leaned to 'designed laws' (S3). A mind only 'in some degree analogous' to ours, acting through laws, is the pole's feature present but limited, so 1. Named alternatives: 0, if the Creator is read as a full personal God; 2, the earlier whole-life reading. Later he became agnostic (changes_over_life), which this axis does not score."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      cites: [{source: S6, locator: "pp. 484, 488–490"}, {source: S1, locator: "pp. 86–87"}, {source: S3, locator: "letter text"}]
      how_known: "His own published book (p. 488 checked on the scan; pp. 484 and 490 read on the Darwin Online transcription), matched by his private writing. A named alternative, so 0.7, not 1.0 (CODING_GUIDE §3). Was 4; 3 under the B 3 anchor (P27)."
      rationale: "Scored on his account of nature (P6). Species arise by 'secondary causes, like those determining the birth and death of the individual' (S6, p. 488) and 'have all been produced by laws acting around us' (S6, p. 489); privately, 'Everything in nature is the result of fixed laws' (S1, p. 87). No miracle, petition or exemption in his account of living things after their beginning. But the same book leaves the beginning outside the laws: 'the first creature [...] was created' (S6, p. 488), life 'was first breathed' into 'some one primordial form' (S6, p. 484) and was 'originally breathed into a few forms or into one' (S6, p. 490). A stated general lawfulness with one stated, limited exception, a creation act, is 3 under the B 3 anchor (P27). Named alternative: 4, if the creation wording is read as a concession of the 1859 book rather than his own view (privately, 'Everything in nature is the result of fixed laws', S1, p. 87)."
    C_ledger:
      value: 4
      basis: consistent_private_letters
      certainty: 0.7
      cites: [{source: S1, locator: "pp. 87, 94"}, {source: S3, locator: "letter text"}]
      how_known: "His own private writing; a named alternative, so 0.7 in any case."
      rationale: "Draft judgment (one line): no moral reckoning in events or after death. 'The lightning kills a man, whether a good one or bad one, owing to the excessively complex action of natural laws' (S3); everlasting punishment is 'a damnable doctrine' (S1, p. 87). Named alternative: 3, since he did not deny a future life outright; he only lacked an 'assured and ever present belief in [...] a future existence with retribution and reward' (S1, p. 94)."
    D_authority:
      value: 4
      basis: consistent_private_letters
      certainty: 0.7
      cites: [{source: S1, locator: "pp. 85–86"}, {source: S4, locator: "letter text"}]
      how_known: "His own private writing (Autobiography and a private letter), ceiling 0.7."
      rationale: "Draft judgment (one line): revelation has no authority for him. The Old Testament 'was no more to be trusted than the sacred books of the Hindoos' (S1, p. 85); miracles become more incredible as we know 'the fixed laws of nature' (S1, p. 86); 'I do not believe in the Bible as a divine revelation' (S4)."
    E_scope:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S6, locator: "pp. 488–489"}, {source: S7, locator: "vol. 2, p. 385"}, {source: S3, locator: "letter text"}]
      how_known: "His published books for humans under the same laws as other organisms; the 'no favour in events' part comes from a private letter, and there is a named alternative, so 0.7 (not 1.0)."
      rationale: "Scored on the world's order (P7). The same laws for all kinds, humans included: 'Light will be thrown on the origin of man and his history' (S6, p. 488); 'man is descended from some less highly organised form' (S7, p. 385); and events fall on the good and the bad alike (S3). Named alternative: 3, because in 1860 he still allowed that all these laws 'may have been expressly designed by an omniscient Creator' (S3); design of the whole is not favour for a group, so it is not preferred."
  mid_basin: {value: true, certainty: 0.7, cites: [{source: S6, locator: "p. 488"}, {source: S3, locator: "letter text"}, {source: S1, locator: "pp. 92–93"}, {source: S6, locator: "pp. 488–490"}], how_known: "DRAFT. P4/P6 test (CODING_GUIDE §6): A_locus 1 (0.7) ≤ 1 and B_cause 3 (0.7) ≥ 3, both at ≥ 0.7, so true (B was 4 before the P27 anchor; the result does not change); certainty is the lower of the two (0.7). Follows from scoring A for 1859 (P20); it was TODO while A was 2. Consistent with primary_system DEISM, whose system file says deists usually pass the test.", note: "SENSITIVE RESULT, lens to check specifically: mid_basin true rests on A_locus 1 at 0.7 for 1859. A is carried by the Origin's public 'laws impressed on matter by the Creator' (S6, p. 488) and the 1860 Gray letter's 'designed laws' (S3), while the Autobiography's dating of his theism to the Origin years is a later, hedged addendum ('as far as I can remember', S1, p. 93), which is why primary_system DEISM is held at 0.5. If lens reads the hedges (that one, and Gray's 'Not that this notion at all satisfies me') as applying to A as well, A drops to 0.5 and mid_basin becomes BELOW_THRESHOLD."}
  statements:
    - text: "Whilst on board the Beagle I was quite orthodox"
      cites: [{source: S1, locator: "p. 85"}]
      date: "1876"
      context: "Autobiography, section 'Religious Belief'; written late in life for his family (S5). Date: the main narrative was written May–August 1876 (Barlow's preface, p. 5); later addenda were inserted up to 1882, and which passages are addenda was not checked page by page."
      axes: [D_authority]
      kind: "autobiography"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "But I had gradually come, by this time, to see that the Old Testament from its manifestly false history of the world, with the Tower of Babel, the rainbow as a sign, etc., etc., and from its attributing to God the feelings of a revengeful tyrant, was no more to be trusted than the sacred books of the Hindoos, or the beliefs of any barbarian."
      cites: [{source: S1, locator: "p. 85"}]
      date: "1876"
      context: "Same section; on 1836–1839 ('these two years')."
      axes: [D_authority]
      kind: "autobiography"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "that the more we know of the fixed laws of nature the more incredible do miracles become"
      cites: [{source: S1, locator: "p. 86"}]
      date: "1876"
      context: "Same section; one of the reflections that led to disbelief in Christianity."
      axes: [B_cause, D_authority]
      kind: "autobiography"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "Thus disbelief crept over me at a very slow rate, but was at last complete. The rate was so slow that I felt no distress, and have never since doubted even for a single second that my conclusion was correct. I can indeed hardly see how anyone ought to wish Christianity to be true; for if so the plain language of the text seems to show that the men who do not believe, and this would include my Father, Brother and almost all my best friends, will be everlastingly punished. And this is a damnable doctrine."
      cites: [{source: S1, locator: "p. 87 (checked on the page scan)"}]
      date: "1876"
      context: "Same section. Emma Darwin's annotation (footnote on the same page) asked that this passage not be published; it was restored in the 1958 edition."
      axes: [C_ledger]
      kind: "autobiography"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "There seems to be no more design in the variability of organic beings and in the action of natural selection, than in the course which the wind blows. Everything in nature is the result of fixed laws."
      cites: [{source: S1, locator: "p. 87 (checked on the page scan)"}]
      date: "1876"
      context: "Same section; on Paley's argument from design."
      axes: [B_cause]
      kind: "autobiography"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "When thus reflecting I feel compelled to look to a First Cause having an intelligent mind in some degree analogous to that of man; and I deserve to be called a Theist."
      cites: [{source: S1, locator: "pp. 92–93"}]
      date: "1876"
      context: "Same section. The next sentence: this conclusion 'was strong in my mind about the time, as far as I can remember, when I wrote the Origin of Species; and it is since that time that it has very gradually with many fluctuations become weaker.'"
      axes: [A_locus]
      kind: "autobiography"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "I cannot pretend to throw the least light on such abstruse problems. The mystery of the beginning of all things is insoluble by us; and I for one must be content to remain an Agnostic."
      cites: [{source: S1, locator: "p. 94 (checked on the page scan)"}]
      date: "1876"
      context: "Same section, closing the discussion of a First Cause."
      axes: [A_locus]
      kind: "autobiography"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "I cannot persuade myself that a beneficent & omnipotent God would have designedly created the Ichneumonidæ with the express intention of their feeding within the living bodies of caterpillars, or that a cat should play with mice."
      cites: [{source: S3, locator: "letter text"}]
      date: "1860-05-22"
      context: "Private letter to Asa Gray; DCP dates it 22 May [1860]."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "I am inclined to look at everything as resulting from designed laws, with the details, whether good or bad, left to the working out of what we may call chance. Not that this notion at all satisfies me. I feel most deeply that the whole subject is too profound for the human intellect."
      cites: [{source: S3, locator: "letter text"}]
      date: "1860-05-22"
      context: "Same letter."
      axes: [A_locus, B_cause]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "The lightning kills a man, whether a good one or bad one, owing to the excessively complex action of natural laws"
      cites: [{source: S3, locator: "letter text"}]
      date: "1860-05-22"
      context: "Same letter; he goes on that 'all these laws may have been expressly designed by an omniscient Creator, who foresaw every future event & consequence.'"
      axes: [C_ledger, E_scope]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "In my most extreme fluctuations I have never been an atheist in the sense of denying the existence of a God.— I think that generally (& more and more so as I grow older) but not always, that an agnostic would be the most correct description of my state of mind."
      cites: [{source: S2, locator: "letter text"}]
      date: "1879-05-07"
      context: "Private letter to John Fordyce, who had asked about his views; it opens 'It seems to me absurd to doubt that a man may be an ardent Theist & an evolutionist.—'"
      axes: [A_locus]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "I am sorry to have to inform you that I do not believe in the Bible as a divine revelation, & therefore not in Jesus Christ as the son of God."
      cites: [{source: S4, locator: "letter text"}]
      date: "1880-11-24"
      context: "Private letter to Frederick McDermott, who had asked whether he believed in the New Testament (DCP footnote)."
      axes: [D_authority]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "To my mind it accords better with what we know of the laws impressed on matter by the Creator, that the production and extinction of the past and present inhabitants of the world should have been due to secondary causes, like those determining the birth and death of the individual."
      cites: [{source: S6, locator: "p. 488 (checked on the page scan)"}]
      date: "1859"
      context: "Origin of Species, first edition, final chapter."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "have all been produced by laws acting around us."
      cites: [{source: S6, locator: "p. 489"}]
      date: "1859"
      context: "Origin, first edition, the 'entangled bank' passage."
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "There is grandeur in this view of life, with its several powers, having been originally breathed into a few forms or into one; and that, whilst this planet has gone cycling on according to the fixed law of gravity, from so simple a beginning endless forms most beautiful and most wonderful have been, and are being, evolved."
      cites: [{source: S6, locator: "p. 490"}]
      date: "1859"
      context: "Origin, first edition, closing sentence. Read with p. 484 ('some one primordial form, into which life was first breathed') and p. 488 ('the first creature [...] was created')."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "The main conclusion arrived at in this work, and now held by many naturalists who are well competent to form a sound judgment, is that man is descended from some less highly organised form."
      cites: [{source: S7, locator: "vol. 2, p. 385"}]
      date: "1871"
      context: "Descent of Man, first edition, 'General summary and conclusion'."
      axes: [E_scope]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
  changes_over_life:
    - {value: "Orthodox Christian on the Beagle; disbelief in Christianity came slowly over the following years 'but was at last complete'", year: "1836–1839 onward", certainty: 0.7, cites: [{source: S1, locator: "pp. 85–87"}], how_known: "His own retrospective account (private writing)."}
    - {value: "Theist (a First Cause with an intelligent mind) around the writing of the Origin; this 'very gradually with many fluctuations' became weaker afterwards", year: "c. 1859 onward", certainty: 0.7, cites: [{source: S1, locator: "pp. 92–93"}], how_known: "His own retrospective account."}
    - {value: "AGNOS: in later life agnostic, 'content to remain an Agnostic' (Autobiography, 1876), and 'generally (& more and more so as I grow older) but not always' an agnostic (1879)", year: "by 1876", certainty: 0.7, cites: [{source: S1, locator: "p. 94"}, {source: S2, locator: "letter text"}], how_known: "Autobiography and private letter agree. Recorded here, not as primary_system, because the code follows the major-work period (CODING_GUIDE §5; P20)."}
  coder_notes: "AGNOS and ATHE are stub system files (flag); DEISM and CHRIST are drafts. The Autobiography is treated as private writing (basis consistent_private_letters): the DCP editors say it was 'intended for the highly select audience of his family and immediate social circle' and should not be read 'as a neutral account' (S5); flagged as a method question. The DCP essay also notes that 'His published writings are particularly reserved or altogether silent on religion' (S5). Barlow's 1958 edition of the Autobiography and the DCP letters are scholarly editions; the Origin and the Descent on Darwin Online are primary transcriptions, and Origin p. 488 was also checked on the page images of the 1859 printing (primary facsimile) (P21). None is an unofficial web copy. Statement dates: Barlow's preface (S1, p. 5) says the main narrative was finished 'between May and August, 1876' and addenda were added during his last six years; a footnote on p. 92 marks one addendum near the First Cause passage, so that passage may be later than 1876."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English; the Darwin and Wedgwood families", certainty: 0.7, cites: [{source: S8, locator: "'Early life and education'"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Unitarian mother; Church of England by christening", certainty: 0.7, cites: [{source: S1, locator: "pp. 22–23, Francis Darwin's note"}], how_known: "Francis Darwin's note."}
  baptism_or_initiation: {value: "Christened in the Church of England", certainty: 0.7, cites: [{source: S1, locator: "pp. 22–23, Francis Darwin's note"}], how_known: "Francis Darwin's note."}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1837–1871", certainty: 0.7, cites: [{source: S8, locator: "opening"}, {source: S7, locator: "vol. 2"}], how_known: "From the private formulation to the Descent."}
  age_at_first_lasting_contribution: {value: 33, certainty: 0.7, cites: [{source: S8, locator: "Born line"}, {source: S10, locator: "preface signed '2nd May, 1842', p. vi"}], how_known: "Born 12 February 1809; Coral Reefs (1842) has its preface signed 2 May 1842, so it appeared after his 33rd birthday. Was 50 (the Origin, 1859) before the first-lasting-year rules (P17, P23); 28 or 27 under the 1837 or 1836 alternatives, so 0.7, the certainty of the year (P15)."}
  first_evidence_of_lio_type_views: {value: "1859: the Origin's account of species produced by 'secondary causes' and 'laws acting around us' (age 50)", certainty: 0.7, cites: [{source: S6, locator: "pp. 488–489"}, {source: S1, locator: "pp. 85–87"}], how_known: "The earliest dated statement of his own in this record that is scored at 3 or 4 (B_cause 3, E_scope 4), under the LIO-type view anchor (P27). His 1876 retrospective dates his loss of belief in revelation and miracles to 1836–39 (S1, pp. 85–87), but that statement is dated 1876 and retrospective (P20 cap 0.7); his notebooks of 1837–39 were not read. Was 'Late 1830s' from the retrospective."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "The first dated LIO-type statement (P27), the Origin of 1859, falls inside the major-work period 1837–1871; his retrospective puts the doubts about revelation in 1836–39, also inside it.", certainty: 0.7, cites: [{source: S1, locator: "pp. 85–87"}, {source: S8, locator: "opening"}], how_known: "Autobiography and Britannica."}
  worldview_during_major_work: {value: "Theist with an intelligent First Cause acting through laws, without revelation (coded DEISM, 0.5); this weakened after the Origin and gave way to agnosticism by 1876 (AGNOS, changes_over_life)", certainty: 0.5, cites: [{source: S1, locator: "pp. 92–94"}, {source: S6, locator: "p. 488"}, {source: S3, locator: "letter text"}], how_known: "His own retrospective account (hedged: 'as far as I can remember', a later addendum) with the Origin and an 1860 letter. The major work falls in a different phase from his later life (CODING_GUIDE §5): primary_system and A_locus are both scored for this phase (P20)."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "He took 'intense satisfaction' in Euclid's proofs and delight in the logic of Paley (S1, pp. 43, 59), but his books argue from observation, not from definitions and axioms.", certainty: 0.5, cites: [{source: S1, locator: "pp. 43, 59"}], how_known: "Coder's reading."}
  form_acquired: {value: "childhood or adolescence", certainty: 0.5, cites: [{source: S1, locator: "p. 43"}], how_known: "Euclid at school."}
  circle_present: {value: "partly", rationale: "Laws 'impressed on matter by the Creator' (S6, p. 488) tie God and nature through law, but he later left the first cause 'insoluble' (S1, p. 94).", certainty: 0.5, cites: [{source: S6, locator: "p. 488"}, {source: S1, locator: "p. 94"}], how_known: "Coder's reading."}
  reading: "As belief, not finding: form partly present (early Euclid), circle partly present in the Origin years and fading after. The record does not test H1."
  notes: ""

institutions:
  - {value: "HMS Beagle survey voyage", role: "self-financed gentleman companion to the captain, Robert Fitzroy (not the ship's surgeon-naturalist)", years: "1831–1836", kind: other, certainty: 0.7, cites: [{source: S8, locator: "map caption 'HMS Beagle in 1831–36'"}, {source: S8, locator: "'Early life and education', the Beagle sentence ('not as a lowly surgeon-naturalist but as a self-financed gentleman companion to the 26-year-old captain')"}], how_known: "Britannica."}
collaborators:
  - {value: "Asa Gray", relation: correspondent, note: "1860 letter on design", certainty: 1.0, cites: [{source: S3, locator: "letter text"}], how_known: "The letter."}
  - {value: "Robert Edmond Grant", relation: teacher, note: "Edinburgh", certainty: 0.7, cites: [{source: S8, locator: "'Early life and education'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 5: Claude, DeepSeek, Gemini, GPT, Grok).", certainty: 0.7, cites: [{source: S9, locator: "roster.csv, rank 16"}], how_known: "Study roster."}
  controversies:
    - {value: "Whether his late view is agnostic or a fluctuating theism; the DCP editors answer 'Is he then an agnostic?' with 'Yes, but not all of the time'", certainty: 0.7, cites: [{source: S5, locator: "section on the Fordyce letter"}], how_known: "Project editors' essay."}
  data_quality_flags:
    - "Britannica read as its first page, plus the section pages 'Evolution by natural selection: the London years, 1836–42' (which also carries 'The squire naturalist in Downe') and 'The Beagle voyage', reopened 2026-10-02."
    - "The Autobiography is private writing for his family (S5); it is treated as consistent_private_letters, not as a public profession."
    - "Era follows the first lasting year (CODING_GUIDE §8; P2): Coral Reefs, 1842 by publication year, so 1750 to 1849; alternatives 1837 and 1836 kept."
    - "SENSITIVE RESULT, lens to check specifically: mid_basin true rests on A_locus 1 at 0.7 for 1859. A is carried by the Origin's public 'laws impressed on matter by the Creator' (S6, p. 488) and the 1860 Gray letter's 'designed laws' (S3), while the Autobiography's dating of his theism to the Origin years is a later, hedged addendum ('as far as I can remember', S1, p. 93), which is why primary_system DEISM is held at 0.5. If lens reads the hedges (that one, and Gray's 'Not that this notion at all satisfies me') as applying to A as well, A drops to 0.5 and mid_basin becomes BELOW_THRESHOLD."
  open_questions:
    - "AGNOS (his later self-description) is a stub system file; it is recorded in changes_over_life, not coded (sourcing backlog)."
    - "Which religion passages of the Autobiography are 1876 text and which are later addenda (Barlow, p. 5; footnote p. 92)."

sources:
  - id: S1
    type: primary
    kind: "scholarly edition"
    author: "Charles Darwin; ed. Nora Barlow"
    year: 1958
    citation: "Darwin, Charles. The Autobiography of Charles Darwin 1809–1882. With the original omissions restored. Edited by Nora Barlow. London: Collins, 1958. Darwin Online, item F1497. http://darwin-online.org.uk/content/frameset?itemID=F1497&viewtype=text&pageseq=1."
    url: "http://darwin-online.org.uk/content/frameset?itemID=F1497&viewtype=text&pageseq=1"
    accessed: 2026-10-02
    reliability_note: "Main narrative May–August 1876, addenda to 1882 (preface, p. 5). Darwin Online transcription of the printed edition; pp. 87 and 94 checked on the page scans (image seq 89 and 96). Written for his family, so private writing."
    used_for: [basics, childhood, worldview, heritage, timing, lane_b]
  - id: S2
    type: primary
    kind: letter
    author: "Charles Darwin"
    year: 1879
    citation: "Darwin, Charles. Letter to John Fordyce, 7 May 1879. Darwin Correspondence Project, letter no. DCP-LETT-12041 (source of text: Linnean Society of London, Quentin Keynes Collection). https://www.darwinproject.ac.uk/letter/DCP-LETT-12041.xml."
    url: "https://www.darwinproject.ac.uk/letter/DCP-LETT-12041.xml"
    accessed: 2026-10-02
    reliability_note: "Scholarly edition (Cambridge University Library)."
    used_for: [worldview]
  - id: S3
    type: primary
    kind: letter
    author: "Charles Darwin"
    year: 1860
    citation: "Darwin, Charles. Letter to Asa Gray, 22 May [1860]. Darwin Correspondence Project, letter no. DCP-LETT-2814. https://www.darwinproject.ac.uk/letter/DCP-LETT-2814.xml."
    url: "https://www.darwinproject.ac.uk/letter/DCP-LETT-2814.xml"
    accessed: 2026-10-02
    reliability_note: "Scholarly edition."
    used_for: [worldview, collaborators]
  - id: S4
    type: primary
    kind: letter
    author: "Charles Darwin"
    year: 1880
    citation: "Darwin, Charles. Letter to Frederick McDermott, 24 November 1880. Darwin Correspondence Project, letter no. DCP-LETT-12851 (source of text: Bonhams, New York, 2015). https://www.darwinproject.ac.uk/letter/DCP-LETT-12851.xml."
    url: "https://www.darwinproject.ac.uk/letter/DCP-LETT-12851.xml"
    accessed: 2026-10-02
    reliability_note: "Scholarly edition; text from a dealer's catalogue."
    used_for: [worldview]
  - id: S5
    type: secondary
    kind: "institutional page"
    author: "Darwin Correspondence Project (editors)"
    citation: "Darwin Correspondence Project. \"What did Darwin believe?\" University of Cambridge. https://www.darwinproject.ac.uk/commentary/religion/what-did-darwin-believe."
    url: "https://www.darwinproject.ac.uk/commentary/religion/what-did-darwin-believe"
    accessed: 2026-10-02
    reliability_note: "Unsigned essay by the project editors."
    used_for: [worldview, review]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Charles Darwin"
    year: 1859
    citation: "Darwin, Charles. On the Origin of Species by Means of Natural Selection. London: John Murray, 1859 (first edition). Darwin Online, item F373. http://darwin-online.org.uk/content/frameset?itemID=F373&viewtype=text&pageseq=1."
    url: "http://darwin-online.org.uk/content/frameset?itemID=F373&viewtype=text&pageseq=1"
    accessed: 2026-10-02
    reliability_note: "Darwin Online transcription; p. 488 checked on the page scan."
    used_for: [basics, contribution, worldview, lane_b]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "Charles Darwin"
    year: 1871
    citation: "Darwin, Charles. The Descent of Man, and Selection in Relation to Sex. Vol. 2. London: John Murray, 1871. Darwin Online, item F937.2. http://darwin-online.org.uk/content/frameset?itemID=F937.2&viewtype=text&pageseq=1."
    url: "http://darwin-online.org.uk/content/frameset?itemID=F937.2&viewtype=text&pageseq=1"
    accessed: 2026-10-02
    reliability_note: "Darwin Online transcription (text only; scan not checked)."
    used_for: [contribution, worldview, timing]
  - id: S8
    type: tertiary
    kind: encyclopedia
    author: "Adrian J. Desmond"
    citation: "Desmond, Adrian J. \"Charles Darwin.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Charles-Darwin."
    url: "https://www.britannica.com/biography/Charles-Darwin"
    accessed: 2026-10-02
    reliability_note: "Signed article. First page read; the section pages 'Evolution by natural selection: the London years, 1836–42' (with 'The squire naturalist in Downe') and 'The Beagle voyage' reopened 2026-10-02 for the geology and Beagle claims. Cited by section."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators]
  - id: S9
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
  - id: S10
    type: primary
    kind: "published work by the subject"
    author: "Charles Darwin"
    year: 1842
    citation: "Darwin, Charles. The Structure and Distribution of Coral Reefs. Being the first part of the geology of the voyage of the Beagle. London: Smith, Elder and Co., 1842. Darwin Online, item F271. https://darwin-online.org.uk/content/frameset?itemID=F271&viewtype=text&pageseq=1."
    url: "https://darwin-online.org.uk/content/frameset?itemID=F271&viewtype=text&pageseq=1"
    accessed: 2026-10-02
    reliability_note: "Darwin Online transcription of the first edition (scholarly). Read for the title page, the preface date (p. vi), p. 4 and the contents (Chapter V, the theory, pp. 88–118); not checked on the page scans."
    used_for: [basics, contribution, timing]
---

# Charles Darwin

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Charles Robert Darwin (1809–1882), English naturalist, set out the theory of evolution by natural selection in the Origin of Species (1859) [S6; S8]. In private writing he said that disbelief in Christianity "crept over me at a very slow rate, but was at last complete" [S1, p. 87], that he was a theist about the time of the Origin and later "content to remain an Agnostic" [S1, pp. 93–94], and that he had "never been an atheist in the sense of denying the existence of a God" [S2]. Draft under v8's stage 3 rulings (P14–P28), scored for the Origin years (P20): primary_system DEISM (0.5; alternative CLASS_THEISM), from his own hedged retrospective account [S1, pp. 92–93]; later AGNOS [S1, p. 94; S2]. Draft scores: A 1 (0.7) [S6, p. 488; S3]; B 3 (0.7; P27 anchor), C 4 (0.7), D 4 (0.7), E 4 (0.7); mid_basin true (0.7), flagged as a sensitive result for lens (see the record's mid_basin note).

## Life and work

Born in Shrewsbury, he studied medicine at Edinburgh (1825) and went to Christ's College, Cambridge (1828), sailed on HMS Beagle (1831–36), formulated his theory privately in 1837–39 and published it in 1859 [S8]. His coral-reef theory, formed on the voyage [S8], was read to the Geological Society on 31 May 1837 [S10, p. 4] and published as The Structure and Distribution of Coral Reefs in 1842 [S10]. The Descent of Man followed in 1871 [S7].

## Contribution and impact

The subsidence theory of coral reefs, which Britannica calls correct [S10, p. 4; S8]. Evolution by natural selection [S6, pp. 488–490] and the descent of humans from "some less highly organised form" [S7, vol. 2, p. 385]. He was buried in Westminster Abbey [S8].

## Childhood and education

His mother, a Wedgwood, was a Unitarian and died in 1817; the boys were christened in the Church of England [S1, pp. 22–23; S8]. He was taught Euclid by a private tutor and remembered "the intense satisfaction which the clear geometrical proofs gave me" [S1, p. 43]. Later, reading Paley for his B.A. examination (January 1831, at about 21), he found its logic "gave me as much delight as did Euclid" [S1, p. 59].

## Adult working worldview

His account of nature is lawful throughout: species arise by "secondary causes" under "laws impressed on matter by the Creator" [S6, p. 488], and "Everything in nature is the result of fixed laws" [S1, p. 87]. He rejected revelation [S1, p. 85; S4] and eternal punishment [S1, p. 87]. Around the Origin he held a First Cause "having an intelligent mind" [S1, pp. 92–93], coded DEISM at 0.5 for that period; it weakened afterwards into agnosticism [S1, p. 94; S2]. The Autobiography was written for his family and should not be read as a neutral account [S5].

## Heritage (context only)

Unitarian mother; Church of England by christening [S1, pp. 22–23]. Context only.

## Timing

First lasting contribution 1842, Coral Reefs, dated by the published book [S10; S8], at age 33, so era 1750 to 1849 (P12, P13, P17, P23). Alternatives: 1837 (Geological Society reading) [S10, p. 4], 1836 (theory formed on the voyage) [S8]. The Origin (1859) is not an alternative, since the list is not pruned to move the year (P23). The era follows the first lasting year (CODING_GUIDE §8; P2).

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form partly present (early Euclid [S1, p. 43]); circle partly present in the Origin years [S6, p. 488].

## Open questions

- mid_basin true is a sensitive result for lens to check (see the record's mid_basin note).
- AGNOS (later life) is a stub system file; recorded in changes_over_life only (sourcing backlog).
- Which religion passages of the Autobiography are later addenda [S1, p. 5].

## Research log

- 2026-10-02: Read Britannica (Desmond, first page); the Autobiography on Darwin Online (pp. 87 and 94 checked on the scans); DCP letters 2814, 12041 and 12851 and the essay 'What did Darwin believe?'; the Origin (p. 488 checked on the scan) and the Descent, vol. 2.
- 2026-10-02 (lens audit fixes): Reopened Britannica's section pages ('The London years, 1836–42', with 'The squire naturalist in Downe'; 'The Beagle voyage') and the first page's 'Early life and education'; reopened the Autobiography p. 59 with Francis Darwin's footnote.
- 2026-10-02 (v8 method rulings): Reopened the Autobiography pp. 92–94 on Darwin Online; Britannica's 'The Beagle voyage' and 'The squire naturalist in Downe'; read The Structure and Distribution of Coral Reefs (1842) on Darwin Online (title page, preface p. vi, p. 4, contents).
- 2026-10-02 (stage 3 rulings P14–P28): Reopened the Origin (1859) on Darwin Online, pp. 484, 488–490, for the B 3 anchor (P27) and the revelation and argument tests (P22, P27).
