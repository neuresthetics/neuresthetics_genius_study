---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch X)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch X, order P32: F 4, rank 130). Basics from Britannica (Martin Evan Jay; Britannica Editors) and IEP (Stephen P. Thornton). Worldview from his own published works in authorized English translations (Project Gutenberg web copies, 0.7 cap): The Psychopathology of Everyday Life (Brill, 1914) and Totem and Taboo (Brill) inside the span; The Future of an Illusion (Robson-Scott, 1928) and Civilization and Its Discontents (Riviere, 1930) after it (P1 cap 0.5). Not a scientist for B (psychoanalysis an interpretive theory of the psyche, P35 addendum, Jung precedent; RQ-X3). primary_system ATHE (0.7); A 4 (0.7, alt BELOW_THRESHOLD); B 3 (0.5, alt 4; P41 extension); C 4 (0.5); D 4 (0.5); E 4 (0.5, alt 3); mid_basin false (A ≥ 3, P10). Span 1899–1923 (0.7). Plotted (faded). Draft, not reviewed."}

identity:
  id: freud-sigmund
  display_name: "Sigmund Freud"
  roster:
    canonical_name: "Sigmund Freud"
    rank: 130
    F: 4
    models: [Claude, DeepSeek, Gemini, GPT]
    band: "core (3–4)"
    status: core
    field: psychology
    field_bucket: "psychology / neuroscience"
  full_name: {value: "Sigmund Freud", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "title"}], how_known: "Britannica and IEP."}
  native_name: {value: "Sigmund Freud", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "German-language name as given."}
  aliases:
    - {name: "Freud-Sigmund", kind: "roster alias"}
    - {name: "Sigmund-Freud", kind: "roster alias"}

basics:
  birth:
    date: {value: "1856-05-06", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts (Born)"}, {source: S2, locator: "§1 Life (year only)"}], how_known: "Britannica gives the day; IEP agrees on 1856."}
    place: {value: "Freiberg, Moravia", modern_name: "Příbor, Czech Republic", polity_then: "Austrian Empire", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts (Born)"}, {source: S2, locator: "§1 Life ('Frieberg, Moravia')"}], how_known: "Both sources."}
  death:
    date: {value: "1939-09-23", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts (Died)"}, {source: S2, locator: "§1 Life (year only)"}], how_known: "Britannica gives the day; IEP agrees on 1939."}
    place: {value: "London", modern_name: "London, England, United Kingdom", polity_then: "United Kingdom", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts (Died)"}, {source: S2, locator: "§1 Life ('exiled in England')"}], how_known: "Both sources."}
  first_lasting_contribution_year: {value: 1899, certainty: 0.7, cites: [{source: S1, locator: "Top Questions ('The Interpretation of Dreams (1899/1900)')"}, {source: S2, locator: "§1 Life ('In 1900 ... generally regarded as his greatest work')"}], how_known: "The Interpretation of Dreams, published late 1899 with 1900 on the title page; Britannica writes 1899/1900, IEP 1900 (P30 dating rule: first publication). Alternative 1895 (Studies on Hysteria with Breuer, IEP: the technique's 'classical expression'), not listed because it is joint and its cathartic method was later given up (S2 §1)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "Top Questions"}, {source: S2, locator: "§1 Life"}], how_known: "1899 (P2); 1895 or 1900 give the same bucket."}
  region_of_birth: {value: "Eastern Europe", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts ('now Příbor, Czech Republic')"}], how_known: "Czechia is Eastern Europe (P3; Gödel precedent)."}
  region_of_work: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "'Early life and training' (Vienna until 1938)"}, {source: S2, locator: "§1 Life"}], how_known: "Vienna (P3; Mozart precedent)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["German"], certainty: 0.7, cites: [{source: S1, locator: "'Early life and training' ('Entwurf einer Psychologie')"}], how_known: "Coder's reading of the German titles."}
  occupations: {value: ["neurologist", "physician", "founder of psychoanalysis", "lecturer in neuropathology, University of Vienna"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Early life and training'"}, {source: S2, locator: "§1 Life"}], how_known: "Britannica and IEP."}

contribution:
  fields: {value: ["psychoanalysis", "psychology", "neurology"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "opening"}], how_known: "Both sources."}
  lasting_original_contributions:
    - {value: "The Interpretation of Dreams: dreams as disguised wish-fulfilment, manifest and latent content; the core of psychoanalytic theory", year: 1899, kind: work, lasting: "'generally regarded as his greatest work' (S2 §1); listed first among his writings (S1)", certainty: 0.7, cites: [{source: S1, locator: "Top Questions"}, {source: S2, locator: "§1 Life; §6"}], how_known: "Britannica and IEP. An interpretive theory of the psyche, not a testable theory of natural systems on IEP's account (S2 §7a), so not a scientist for B (P35 addendum; RQ-X3)."}
    - {value: "Psychoanalysis as a theory and therapy: the unconscious, repression, free association, infantile sexuality", year: 1899, kind: "body of work", lasting: "'Notwithstanding the multiple manifestations of psychoanalysis as it exists today, it can in almost all fundamental respects be traced directly back to Freud's original work' (S2 opening); 'the most influential intellectual legislator of his age' (S1)", certainty: 0.7, cites: [{source: S2, locator: "opening; §§3–6"}, {source: S1, locator: "opening"}], how_known: "IEP and Britannica; dated to the Interpretation of Dreams (P12, coder's call), alternative 1895."}
    - {value: "Tripartite model of the mind (id, ego, super-ego) in The Ego and the Id", year: 1923, kind: theory, lasting: "'his famous tripartite model of the structure of the mind' (S2 §5)", certainty: 0.7, cites: [{source: S2, locator: "§1 Life ('his 1923 work The Ego and the Id'); §5"}], how_known: "IEP. Latest listed lasting item, so it ends the span (P30 addendum b)."}
  evidence_of_impact:
    - {value: "'the most influential intellectual legislator of his age'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "Influence on psychology, anthropology, semiotics and the arts", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "IEP."}
  major_works:
    - {value: "Studies on Hysteria (with Josef Breuer)", year: 1895, kind: book, certainty: 0.7, cites: [{source: S2, locator: "§1 Life"}], how_known: "IEP."}
    - {value: "The Psychopathology of Everyday Life", year: 1901, kind: book, certainty: 0.7, cites: [{source: S2, locator: "§1 Life ('1901')"}, {source: S1, locator: "Top Questions ('(1904)')"}], how_known: "IEP 1901; Britannica's 1904 is the book edition (conflict noted)."}
    - {value: "Totem and Taboo", year: 1913, kind: book, certainty: 0.7, cites: [{source: S1, locator: "Top Questions"}], how_known: "Britannica."}
    - {value: "The Future of an Illusion", year: 1927, kind: book, certainty: 0.7, cites: [{source: S4, locator: "title page"}, {source: S6, locator: "ch. II ('In my Future of an Illusion')"}], how_known: "His own later reference (S6); the German year 1927 is not stated in the sources read beyond the 1928 translation (coder's dating, 0.7)."}
    - {value: "Civilization and Its Discontents", year: 1930, kind: book, certainty: 0.7, cites: [{source: S1, locator: "Top Questions"}], how_known: "Britannica."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founder of psychoanalysis; 'the most influential intellectual legislator of his age' (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Jewish", certainty: 0.7, cites: [{source: S1, locator: "'Early life and training' ('a Jewish wool merchant')"}, {source: S2, locator: "§1 Life ('Freud, who was Jewish')"}], how_known: "Both sources name the family Jewish; practice not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated in the sources read."}
  parents_and_household:
    - {value: "Father: Jakob Freud, Jewish wool merchant, 40 at Sigmund's birth, married once before", certainty: 0.7, cites: [{source: S1, locator: "'Early life and training'"}], how_known: "Britannica."}
    - {value: "Mother: Amalie Nathansohn", certainty: 0.7, cites: [{source: S1, locator: "'Early life and training'"}], how_known: "Britannica."}
    - {value: "Two older half-brothers (Emmanuel and Philip); nephew John, a year older, close companion", certainty: 0.7, cites: [{source: S1, locator: "'Early life and training'"}, {source: S2, locator: "§2"}], how_known: "Both sources."}
  household_circumstances: {value: "Family moved for economic reasons to Leipzig (1859) and then Vienna", certainty: 0.7, cites: [{source: S1, locator: "'Early life and training'"}], how_known: "Britannica; IEP has the move at age four."}
  schooling:
    - {value: "Sperl Gymnasium, Vienna", stage: "grammar or secondary school", run_by: "state or municipal", years: "to 1873", certainty: 0.5, cites: [{source: S1, locator: "'Early life and training' ('In 1873 Freud was graduated from the Sperl Gymnasium')"}], how_known: "Britannica; run_by the coder's reading."}
    - {value: "University of Vienna, medical school (physiology under Ernst Brücke; MD 1881)", stage: university, run_by: "state or municipal", years: "1873–1881", certainty: 0.7, cites: [{source: S1, locator: "Top Questions; 'Early life and training'"}, {source: S2, locator: "§1 Life"}], how_known: "Both sources; run_by the coder's reading."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure:
    - {value: "Turned to medicine 'apparently inspired by a public reading of an essay by Goethe on nature'", certainty: 0.7, cites: [{source: S1, locator: "'Early life and training'"}], how_known: "Britannica."}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["German"], certainty: 0.5, cites: [{source: S1, locator: "'Early life and training'"}], how_known: "Coder's reading (Vienna from age four)."}
  notable_events:
    - {value: "Move to Vienna", year: 1860, certainty: 0.7, cites: [{source: S1, locator: "'Early life and training' ('Leipzig and then a year after to Vienna')"}], how_known: "Britannica (1859 plus one year)."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1899–1923", certainty: 0.7, cites: [{source: S1, locator: "Top Questions"}, {source: S2, locator: "§1 Life"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Religious doctrines are illusions; 'scientific work is our only way to the knowledge of external reality' (1927)", certainty: 0.5, cites: [{source: S4, locator: "ch. VI"}], how_known: "His own published book, four years after the span (P1 cap 0.5); web copy of the 1928 translation."}
  primary_system:
    value: ATHE
    basis: written_profession
    certainty: 0.7
    cites: [{source: S5, locator: "ch. IV"}, {source: S3, locator: "ch. XII (superstition section)"}, {source: S6, locator: "ch. II"}, {source: S4, locator: "ch. VI"}]
    rationale: "Inside the span, his published works explain God as a projection: 'god at bottom is nothing but an exalted father' (Totem and Taboo, 1913) and 'a large portion of the mythological conception of the world which reaches far into the most modern religions is nothing but psychology projected into the outer world', so that the myths 'of God, of good and evil, of immortality' become meta-psychology (Psychopathology, 1914 trans.). After the span the denial is explicit: the Providence of 'the ordinary man' is 'so patently infantile, so incongruous with reality' and 'this religion is not tenable' (Civilization, 1930). ATHE's naturalism fits; no other code named. Capped at 0.7 because every text is read in a web copy of an English translation (§7)."
    how_known: "Own published works; in-span texts imply the denial, post-span texts state it (P1 cap 0.5 for those alone)."
  secondary_system: {value: UNKNOWN, how_known: "One system (P29)."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Chosen: God as a projected father; religion 'not tenable'."}
    - {code: AGNOS, reason: "Rejected: 'Of the reality value of most of them we cannot judge' (1927) concerns proof of doctrines; his texts deny the God of religion, not suspend judgement."}
    - {code: JUDA, reason: "Heritage only (S1, S2); no profession read."}
  lio_axes:
    A_locus:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S5, locator: "ch. IV"}, {source: S6, locator: "ch. II"}]
      rationale: "No separate God: 'god at bottom is nothing but an exalted father' (1913, in span); the answering Providence is 'so incongruous with reality' that 'this religion is not tenable' (1930, after span). Named alternative BELOW_THRESHOLD: the 1913 passage allows 'other origins and meanings of god upon which psychoanalysis can throw no light', and in 1927 he says of religious doctrines 'neither can they be refuted'. Web copy, so 0.7 at most."
      how_known: "Own published works (translations, web copies)."
      alternatives:
        - {value: BELOW_THRESHOLD, note: "Hedges in 1913 ('other origins') and 1927 ('neither can they be refuted').", cites: [{source: S5, locator: "ch. IV"}, {source: S4, locator: "ch. VI"}]}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.5
      cites: [{source: S3, locator: "ch. XII, p. 278; superstition section (index: p. 306)"}]
      rationale: "Scored on his account of nature (P6); not a scientist for B (P35 addendum: interpretive theory of the psyche, Jung precedent; RQ-X3). He holds that 'determinism reaches farther than we suppose' and treats the supernatural as projection ('psychology projected into the outer world'), rejecting omens; but he states no exceptionless order, and says he believes 'in outer (real) chance', meaning coincidence. Rejecting intervention without a stated exceptionless order is B 3 at 0.5, alternative 4 (P41 extension, Tolstoy precedent)."
      how_known: "One in-span book (translation, web copy)."
      alternatives:
        - {value: 4, note: "P41 extension; 'determinism reaches farther than we suppose'.", cites: [{source: S3, locator: "ch. XII, p. 278"}]}
    C_ledger:
      value: 4
      basis: written_profession
      certainty: 0.5
      cites: [{source: S4, locator: "ch. VI"}]
      rationale: "Impersonal consequence or none: 'it would indeed be very nice if there were ... a moral world order and a future life, but ... it is very odd that this is all just as we should wish it ourselves' (1927). An implied denial in a post-span book (P1 cap 0.5). Named alternative BELOW_THRESHOLD (implication only)."
      how_known: "Own published book after the span."
      alternatives:
        - {value: BELOW_THRESHOLD, note: "Implied, not stated.", cites: [{source: S4, locator: "ch. VI"}]}
    D_authority:
      value: 4
      basis: written_profession
      certainty: 0.5
      cites: [{source: S4, locator: "ch. VI"}, {source: S3, locator: "superstition section (index: p. 306)"}]
      rationale: "Observation and reason outrank revelation: 'scientific work is our only way to the knowledge of external reality. Again, it is merely illusion to expect anything from intuition or trance' (1927, after span, P1 cap 0.5). In span, religion's 'transcendental reality' is 'destined to be changed again by science into psychology of the unconscious' (Psychopathology). No domain left to revelation."
      how_known: "Own published books; the explicit statement is after the span."
    E_scope:
      value: 4
      basis: written_profession
      certainty: 0.5
      cites: [{source: S3, locator: "ch. XII, p. 278; superstition section (index: p. 306)"}]
      rationale: "Scored on the world's order (P7). Same rules for the mind as elsewhere ('Here, as in still other spheres, determinism reaches farther than we suppose'), and no hidden favours: 'I do not believe that an occurrence in which my mental life takes no part can teach me anything hidden concerning the future shaping of reality'. One in-span book; 'farther than we suppose' is not 'everywhere', so 0.5 with 3 as the named alternative."
      how_known: "Own published book (translation, web copy)."
      alternatives:
        - {value: 3, note: "Scope of determinism stated as 'farther than we suppose', not universal.", cites: [{source: S3, locator: "ch. XII, p. 278"}]}
  mid_basin: {value: false, certainty: 0.7, cites: [{source: S5, locator: "ch. IV"}, {source: S6, locator: "ch. II"}], how_known: "A 4 at 0.7: the A ≥ 3 branch reads A only (P4, P10)."}
  statements:
    - text: "By abandoning a part of our psychic capacity as unexplainable through purposive ideas we ignore the realms of determinism in our mental life. Here, as in still other spheres, determinism reaches farther than we suppose."
      cites: [{source: S3, locator: "ch. XII, opening of section I (p. 278 per the index)"}]
      date: "1914"
      context: "The Psychopathology of Everyday Life, ch. XII 'Determinism, Chance, and Superstitious Beliefs'."
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "Brill's authorized translation (Macmillan, 1914), Project Gutenberg #67332; web copy without scans (0.7 cap). German first edition 1901 (S2); dated by the edition read; in the span either way."
    - text: "I do not believe that an occurrence in which my mental life takes no part can teach me anything hidden concerning the future shaping of reality; but I do believe that an unintentional manifestation of my own mental activity surely contains something concealed which belongs only to my mental life--that is, I believe in outer (real) chance, but not in inner (psychic) accidents."
      cites: [{source: S3, locator: "ch. XII, superstition section (index: p. 306)"}]
      date: "1914"
      context: "Same chapter, how he differs from a superstitious person."
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "As above."
    - text: "As a matter of fact, I believe that a large portion of the mythological conception of the world which reaches far into the most modern religions is nothing but psychology projected into the outer world."
      cites: [{source: S3, locator: "ch. XII, superstition section (index: p. 306)"}]
      date: "1914"
      context: "Same section; he goes on to 'explain in this way the myths of paradise and the fall of man, of God, of good and evil, of immortality, and the like--that is, to transform metaphysics into meta-psychology'. Italics of the printed text not kept."
      axes: [A_locus, D_authority]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "As above."
    - text: "However, psychoanalytic investigation of the individual teaches with especial emphasis that god is in every case modelled after the father and that our personal relation to god is dependent upon our relation to our physical, fluctuating and changing with him, and that god at bottom is nothing but an exalted father."
      cites: [{source: S5, locator: "ch. IV 'The Infantile Recurrence of Totemism'"}]
      date: "1913"
      context: "Totem and Taboo, on how the idea of god enters the totem sacrifice; the passage adds 'quite aside from all the other origins and meanings of god upon which psychoanalysis can throw no light'."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "Brill's authorized translation (Kegan Paul, London), Project Gutenberg #41214 from Google scans; web copy (0.7 cap). Dated by the German book (S1: 1913)."
    - text: "Of the reality value of most of them we cannot judge; just as they cannot be proved, neither can they be refuted. We still know too little to approach them critically. The riddles of the universe only reveal themselves slowly to our enquiry, to many questions science can as yet give no answer; but scientific work is our only way to the knowledge of external reality. Again, it is merely illusion to expect anything from intuition or trance"
      cites: [{source: S4, locator: "ch. VI"}]
      date: "1927"
      context: "The Future of an Illusion, after calling religious doctrines illusions, some comparable 'to delusions'."
      axes: [A_locus, D_authority]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "Robson-Scott's translation (1928), Project Gutenberg #76774; web copy. After the span (P1 cap 0.5); dated by the German book."
    - text: "We say to ourselves: it would indeed be very nice if there were a God, who was both creator of the world and a benevolent providence, if there were a moral world order and a future life, but at the same time it is very odd that this is all just as we should wish it ourselves."
      cites: [{source: S4, locator: "ch. VI (end)"}]
      date: "1927"
      context: "Same chapter, on what the psychological origin of religious ideas implies."
      axes: [A_locus, C_ledger]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "As above."
    - text: "The whole thing is so patently infantile, so incongruous with reality, that to one whose attitude to humanity is friendly it is painful to think that the great majority of mortals will never be able to rise above this view of life. It is even more humiliating to discover what a large number of those alive to-day, who must see that this religion is not tenable, yet try to defend it inch by inch"
      cites: [{source: S6, locator: "ch. II"}]
      date: "1930"
      context: "Civilization and Its Discontents, on 'what the ordinary man understands by his religion': a 'solicitous Providence' in the form of 'a greatly exalted father' who can 'be softened by their prayers'."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "Riviere's translation (1930), Project Gutenberg #78221; web copy. After the span (P1 cap 0.5)."
  changes_over_life: []
  coder_notes: "Coder's call on the span: 1899 (The Interpretation of Dreams; Britannica 1899/1900, IEP 1900) to 1923 (The Ego and the Id, IEP's 'famous tripartite model'). Alternative start 1895 (Studies on Hysteria, joint with Breuer); alternative end 1930 if Civilization and Its Discontents is counted lasting (Britannica lists it among his writings without calling it lasting); either way the values stand. Not a scientist for B: IEP reports the critics' case that the theory is not falsifiable and calls it a 'theoretical model' (§5, §7a), so it falls under the P35 addendum's interpretive theories (Jung), though Freud called it a science (RQ-X3). Everything is read in English translations on Project Gutenberg (web copies, 0.7 cap); German originals not read. Lead: the 1918 letter to Pfister ('a completely godless Jew'), not read. Plotted (faded)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Jewish", certainty: 0.7, cites: [{source: S1, locator: "'Early life and training'"}, {source: S2, locator: "§1 Life"}], how_known: "Both sources."}
  religious_heritage_by_birth: {value: "Judaism", certainty: 0.7, cites: [{source: S1, locator: "'Early life and training'"}, {source: S2, locator: "§1 Life"}], how_known: "Both sources."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1899–1923", certainty: 0.7, cites: [{source: S1, locator: "Top Questions"}, {source: S2, locator: "§1 Life; §5"}], how_known: "From The Interpretation of Dreams (1899) to The Ego and the Id (1923) (P12, P30). Coder's call; alternatives in coder_notes."}
  age_at_first_lasting_contribution: {value: 43, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts; Top Questions"}], how_known: "1899 − 1856 = 43 (P30); 44 under IEP's 1900."}
  first_evidence_of_lio_type_views: {value: "1913–1914: god as 'an exalted father'; religion as 'psychology projected into the outer world'", year: 1913, certainty: 0.7, cites: [{source: S5, locator: "ch. IV"}, {source: S3, locator: "ch. XII"}], how_known: "Earliest texts read (P30 #7); the 1901 German first edition of the Psychopathology not checked for the passage."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S5, locator: "ch. IV"}, {source: S3, locator: "ch. XII"}], how_known: "Inside 1899–1923."}
  worldview_during_major_work: {value: "ATHE: God as a projected father (1913); determinism in mental life", certainty: 0.7, cites: [{source: S5, locator: "ch. IV"}, {source: S3, locator: "ch. XII"}], how_known: "In-span texts."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S2, locator: "§5 (tripartite model)"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "§2"}], how_known: "Not assessed."}
  circle_present: {value: "no", rationale: "No unity claim; mind as an energy system under determinism.", certainty: 0.5, cites: [{source: S2, locator: "§2; §3"}], how_known: "Coder's reading."}
  reading: "Psychic determinism; religion as projection."
  notes: ""

institutions:
  - {value: "University of Vienna", role: "medical student (physiology laboratory of Ernst Brücke); lecturer in neuropathology from 1885", years: "1873–1938", kind: university, certainty: 0.5, cites: [{source: S1, locator: "'Early life and training'"}, {source: S2, locator: "§1 Life"}], how_known: "Both sources; the end year is the coder's (left Vienna 1938)."}
  - {value: "Vienna General Hospital", role: "clinical assistant", years: "1882–1885", kind: other, certainty: 0.7, cites: [{source: S1, locator: "Top Questions; 'Early life and training'"}], how_known: "Britannica."}
  - {value: "Salpêtrière clinic, Paris", role: "student of Charcot", years: "1885–1886", kind: other, certainty: 0.7, cites: [{source: S1, locator: "'Early life and training'"}, {source: S2, locator: "§1 Life"}], how_known: "Both sources."}
collaborators:
  - {value: "Josef Breuer", relation: collaborator, note: "Studies on Hysteria (1895)", certainty: 0.7, cites: [{source: S1, locator: "'Early life and training'"}, {source: S2, locator: "§1 Life"}], how_known: "Both sources."}
  - {value: "Wilhelm Fliess", relation: correspondent, note: "closest friend and interlocutor for 15 years", certainty: 0.7, cites: [{source: S1, locator: "'Early life and training'"}], how_known: "Britannica."}
  - {value: "Jean-Martin Charcot", relation: teacher, note: "Paris, 1885–86", certainty: 0.7, cites: [{source: S1, locator: "'Early life and training'"}, {source: S2, locator: "§1 Life"}], how_known: "Both sources."}
  - {value: "Ernst Brücke", relation: teacher, note: "physiology laboratory, University of Vienna", certainty: 0.7, cites: [{source: S1, locator: "'Early life and training'"}, {source: S2, locator: "§1 Life; §2"}], how_known: "Both sources."}
  - {value: "Carl Jung and Alfred Adler", relation: "student or assistant", note: "early followers who founded rival schools", certainty: 0.7, cites: [{source: S2, locator: "§1 Life"}], how_known: "IEP."}
  - {value: "Anna Freud", relation: family, note: "daughter, psychoanalyst", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "§1 Life"}], how_known: "Both sources."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S7, locator: "roster.csv, rank 130"}], how_known: "Study roster."}
  controversies:
    - {value: "Scientific status of psychoanalysis disputed (Popper's falsifiability criterion; coherence of its causal claims; efficacy of therapy)", certainty: 0.7, cites: [{source: S2, locator: "§7a–d"}], how_known: "IEP."}
    - {value: "Cocaine advocacy in the 1880s led to a friend's addiction and 'tarnished his medical reputation for a time'", certainty: 0.7, cites: [{source: S1, locator: "'Early life and training'"}], how_known: "Britannica."}
  data_quality_flags:
    - "All of his texts read in English translations on Project Gutenberg (web copies, 0.7 cap)."
    - "The Psychopathology is dated 1901 (IEP) or 1904 (Britannica); read in the 1914 translation of a later edition."
  open_questions:
    - "RQ-X3: is psychoanalysis a theory of natural systems for P30/P35 (Freud a scientist), or interpretive like Jung's?"
    - "Read the German originals and the 1918 Pfister letter."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Martin Evan Jay; Britannica Editors"
    citation: "Jay, Martin Evan, and Britannica Editors. \"Sigmund Freud.\" Encyclopaedia Britannica (updated 1 October 2026). https://www.britannica.com/biography/Sigmund-Freud. Read live 2026-10-19."
    url: "https://www.britannica.com/biography/Sigmund-Freud"
    accessed: 2026-10-19
    reliability_note: "Signed article; the fetched text stopped inside 'Early life and training'. Quick Facts and body cited; the Top Questions answers on education and works are cited only where IEP or the body agrees."
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, collaborators, review]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Stephen P. Thornton"
    citation: "Thornton, Stephen P. \"Sigmund Freud (1856—1939).\" Internet Encyclopedia of Philosophy. https://iep.utm.edu/freud/"
    url: "https://iep.utm.edu/freud/"
    accessed: 2026-10-19
    reliability_note: "Signed peer-reviewed encyclopedia article (University of Limerick); no revision date shown."
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, collaborators, review, lane_b]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Sigmund Freud; trans. A. A. Brill"
    citation: "Freud, Sigmund. Psychopathology of Everyday Life. Trans. A. A. Brill. New York: Macmillan, 1914. Project Gutenberg eBook #67332. https://www.gutenberg.org/ebooks/67332"
    url: "https://www.gutenberg.org/ebooks/67332"
    accessed: 2026-10-19
    reliability_note: "Authorized translation; Gutenberg transcription without page images (web copy, 0.7 cap); page numbers from the book's index."
    used_for: [worldview, timing]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Sigmund Freud; trans. W. D. Robson-Scott"
    citation: "Freud, Sigmund. The Future of an Illusion. Trans. W. D. Robson-Scott. 1928 (Gutenberg header: 'Edinburgh: Horace Liverwright and the institute of psycho-analysis, 1928'). Project Gutenberg eBook #76774. https://www.gutenberg.org/ebooks/76774"
    url: "https://www.gutenberg.org/ebooks/76774"
    accessed: 2026-10-19
    reliability_note: "Translation read by Strachey (translator's note); Gutenberg transcription (web copy). Imprint as the Gutenberg header gives it (not checked against the book). Cited by chapter."
    used_for: [worldview, contribution]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Sigmund Freud; trans. A. A. Brill"
    citation: "Freud, Sigmund. Totem and Taboo: Resemblances between the Psychic Lives of Savages and Neurotics. Authorized English translation by A. A. Brill. London: Kegan Paul, Trench, Trubner. Project Gutenberg eBook #41214. https://www.gutenberg.org/ebooks/41214"
    url: "https://www.gutenberg.org/ebooks/41214"
    accessed: 2026-10-19
    reliability_note: "Proofread transcription (Distributed Proofreaders) from Google scans; no page numbers kept; cited by chapter (web copy)."
    used_for: [worldview, timing]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Sigmund Freud; trans. Joan Riviere"
    citation: "Freud, Sigmund. Civilization and Its Discontents. Trans. Joan Riviere. New York: Jonathan Cape & Harrison Smith, 1930. Project Gutenberg eBook #78221. https://www.gutenberg.org/ebooks/78221"
    url: "https://www.gutenberg.org/ebooks/78221"
    accessed: 2026-10-19
    reliability_note: "Authorized translation; Gutenberg transcription (web copy). Cited by chapter."
    used_for: [worldview, contribution]
  - id: S7
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Sigmund Freud

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Sigmund Freud (1856–1939), Austrian neurologist and founder of psychoanalysis [S1, S2]. Draft: primary_system ATHE (0.7); A 4 (0.7); B 3 (0.5, alt 4); mid_basin false. Plotted (faded).

## Life and work

Vienna from 1860; Paris with Charcot 1885–86; private practice from 1886; exile to London 1938 [S1, S2].

## Contribution and impact

The Interpretation of Dreams (1899/1900), psychoanalysis, the tripartite model (1923) [S1, S2].

## Childhood and education

Jewish family; Sperl Gymnasium; medicine at Vienna under Brücke [S1, S2].

## Adult working worldview

God as 'an exalted father' (1913) [S5]; religion as 'psychology projected into the outer world' [S3]; later, religion 'not tenable' (1930) [S6].

## Heritage (context only)

Jewish [S1, S2].

## Timing

1899–1923, from age 43 [S1, S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Not assessed [S2].

## Open questions

- RQ-X3: Freud and the P35 addendum.

## Research log

- 2026-10-19: Read Britannica (Jay), IEP (Thornton), and Gutenberg texts of the Psychopathology, Totem and Taboo, The Future of an Illusion and Civilization and Its Discontents.
