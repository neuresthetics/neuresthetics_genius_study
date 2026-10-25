---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AB1; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-20, by: "Grok Bot", summary: "AB1 audit fix: S1's bibliography dates the Philosophical Letters to 1734; wording corrected (no score change)."}
    - {date: 2026-10-20, by: "Grok Bot", summary: "Record created (stage 3 batch AB1, order P32: F 3, rank 223). Sources: SEP 'Voltaire' (J.B. Shank, 2024, read in full); Britannica students edition (S3) for full birth and death dates. Lasting: the philosophe authorship from Lettres philosophiques (1734), 'the key turning point', with which he 'pointed modern philosophy down several paths that it subsequently followed' and 'remains today an iconic hero' (S1); Candide (1759), 'Voltaire's most widely known text' (S1). Span 1734–1759 at 0.5 (alternative end 1778, his death, since the campaign for philosophie ran to the end), age 40. Worldview: S1 says 'it would be wrong to call Voltaire an atheist, or even an anti-Christian', that his 'personal religious views were subtle', and places him among debates of 'the so-called deists' while distancing him 'from more radical deists like Toland'; no own words on God quoted. primary_system BELOW_THRESHOLD (DEISM lead); A UNKNOWN (P19). Not a scientist (defender and popularizer of Newtonian science, not a contributor; P33 logic); B UNKNOWN. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #210/228, F 3, rank 223): firm A and B if sources allow; do not force plot. Own-voice: Philosophical Dictionary 'Theist' / 'Théisme' / 'Miracles' (1764; S4–S6); Poème sur le désastre de Lisbonne (1756; S7); SEP and Britannica retained. P31: no documented change between span 1734–1759 and 1764 Dictionary — adult written profession counts at normal certainty. primary BELOW→DEISM 0.7 written_profession (alt CLASS_THEISM); A UNKNOWN→1 @0.7 written_profession, support corroborated; B UNKNOWN→4 @0.7 written_profession, support corroborated, alt 3; mid UNKNOWN→true @0.7. Chart-moving YES (would plot dark filled at next figure refresh; figures/ not touched). P47 on all. No fallacy_catalog. Draft, not reviewed."}

identity:
  id: voltaire
  display_name: "Voltaire"
  roster:
    canonical_name: "Voltaire"
    rank: 223
    F: 3
    models: [DeepSeek, GPT, Grok]
    band: "core (3–4)"
    status: "core"
    field: "philosophy"
    field_bucket: "philosophy"
  full_name: {value: "François-Marie d’Arouet", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP; pen name Voltaire. Britannica students edition writes 'Arouet' (S3)."}
  native_name: {value: "François-Marie Arouet", certainty: 0.7, cites: [{source: S3, locator: "para. 2"}], how_known: "Britannica."}
  aliases:
    - {name: "François-Marie Arouet", kind: "birth name"}
    - {name: "Voltaire", kind: "pen or art name"}

basics:
  birth:
    date: {value: "1694-11-21", certainty: 0.7, cites: [{source: S3, locator: "para. 2"}, {source: S1, locator: "opening"}], how_known: "Britannica students edition; SEP gives 1694."}
    place: {value: "Paris", modern_name: "Paris, France", polity_then: "Kingdom of France", certainty: 0.7, cites: [{source: S3, locator: "para. 2"}], how_known: "Britannica."}
  death:
    date: {value: "1778-05-30", certainty: 0.7, cites: [{source: S3, locator: "para. 4"}, {source: S1, locator: "1.6"}], how_known: "Britannica students edition; SEP gives 1778."}
    place: {value: "Paris", modern_name: "Paris, France", polity_then: "Kingdom of France", certainty: 0.5, cites: [{source: S3, locator: "para. 4"}], how_known: "Britannica: returned to Paris in February 1778 and died on May 30; place implied, not stated."}
  first_lasting_contribution_year: {value: 1734, certainty: 0.7, cites: [{source: S1, locator: "1. Voltaire's Life; 1.3"}], how_known: "Lettres philosophiques, 'published in 1734 ... the key turning point' (S1); P30 publication. S1's bibliography also dates the Philosophical Letters (Letters on the English Nation) to 1734."}
  era_bucket: {value: "1600 to 1749", certainty: 1.0, cites: [{source: S1, locator: "1.3"}], how_known: "1734 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "1.1"}], how_known: "France (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "1.3–1.6"}], how_known: "Cirey, Paris, Berlin, Geneva and Ferney: France, Prussia and Switzerland all fall in Western Europe."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["French", "English"], certainty: 0.7, cites: [{source: S1, locator: "1.2; Bibliography"}], how_known: "French works; English Essays of 1727 (S1)."}
  occupations: {value: ["writer", "philosopher", "playwright", "historian"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}

contribution:
  fields: {value: ["philosophy", "literature", "history"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  lasting_original_contributions:
    - {value: "The philosophe authorship and campaign: a new conception of philosophy and the philosopher, beginning with Lettres philosophiques", year: 1734, kind: "body of work", lasting: "'At the center of his work was a new conception of philosophy and the philosopher that in several crucial respects influenced the modern concept of each'; he 'pointed modern philosophy down several paths that it subsequently followed' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; 1.3"}], how_known: "From Lettres philosophiques, 1734 (S1)."}
    - {value: "Candide, ou l'Optimisme", year: 1759, kind: "work", lasting: "'Voltaire's most widely known text' (S1)", certainty: 0.5, cites: [{source: S1, locator: "2"}], how_known: "First published 1759 (S1); 0.5 because 'most widely known' is thin lasting wording (P13)."}
  evidence_of_impact:
    - {value: "'Voltaire remains today an iconic hero for everyone who sees a positive linkage between critical reason and political resistance'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "1.7"}], how_known: "SEP."}
  major_works:
    - {value: "Philosophical Dictionary", year: 1764, kind: "book", certainty: 0.7, cites: [{source: S3, locator: "para. 5"}], how_known: "Britannica students edition."}
    - {value: "The Century of Louis XIV", year: 1751, kind: "book", certainty: 0.7, cites: [{source: S3, locator: "para. 5"}], how_known: "Britannica students edition."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Defined the Enlightenment philosophe (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated beyond Jesuit schooling (S1)."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Fourth of five children of a well-to-do public official and an aristocratic mother", role: "family", certainty: 0.7, cites: [{source: S1, locator: "1.1"}], how_known: "SEP."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Jesuit Collège Louis-le-Grand, Paris", certainty: 0.7, cites: [{source: S1, locator: "1.1"}], how_known: "SEP."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1734–1759", certainty: 0.5, cites: [{source: S1, locator: "1.3; 2"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Newtonian physics demonstrates a creative intelligence ('a catechist proclaims God to the children, and Newton demonstrates Him to the learned'); the 'prodigious order of nature' and immutable mathematical laws are God's work, not a theatre of miracles (S4 Atheism; S6 Miracles).", certainty: 0.7, cites: [{source: S4, locator: "Atheism, 'Newton demonstrates Him'"}, {source: S6, locator: "Miracles §1"}], how_known: "Own words in the Philosophical Dictionary (P31)."}
  primary_system:
    value: DEISM
    basis: written_profession
    certainty: 0.7
    cites: [{source: S4, locator: "Theist"}, {source: S5, locator: "Théisme"}, {source: S6, locator: "Miracles §1"}]
    how_known: "Philosophical Dictionary (1764). P31: no documented change of view between the 1734–1759 span and 1764 (Lisbon poem 1756 already affirms a just Creator against optimism). Named alternative CLASS_THEISM, so 0.7 not 1.0. DEISM system file names Voltaire among French philosophe deists."
    rationale: "Own preferred label is 'théiste' (S4, S5): a Supreme Being known by reason from design/order ('Newton demonstrates Him'; 'a mushroom is the work of an infinite wisdom'), worship and justice without sects, laughing at Mecca and Lorette. Miracles: 'Il est donc absurde de croire des miracles' — violation of 'lois mathématiques, divines, immuables, éternelles' is a contradiction (S6). Meets DEISM use_when (creator by reason; rejects miracles and church/sectarian authority as religious knowledge) and P27. Named alternative CLASS_THEISM: Theist still affirms Providence that 'acts' and rewards/punishes; Théisme's protective line 'Notre religion révélée n'est même ... que cette loi naturelle perfectionnée' can be read as keeping a place for revelation (Catholic mask). ATHE rejected: he argues at length against atheism (S4)."
    alternatives:
      - {value: CLASS_THEISM, note: "Providence that acts / moral Governor; Théisme protective 'religion révélée' line if taken straight rather than as cover.", cites: [{source: S4, locator: "Theist"}, {source: S5, locator: "Théisme"}]}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: DEISM, reason: "Coded at 0.7: own 'théiste' profession; creator by reason/design; miracles absurd; rejects Mecca/Lorette/sects (P27)."}
    - {code: CLASS_THEISM, reason: "Named alternative: Providence that acts; protective revelation wording in Théisme."}
    - {code: CHRIST, reason: "Rejected: S1 notes he is not anti-Christian on a broad reading, but own words reject sectarian pilgrimage and treat Gospel miracles under ironic cover while calling miracle belief absurd."}
    - {code: ATHE, reason: "Rejected: Atheism article argues for a creative intelligence; Theist is 'firmly persuaded' of a Supreme Being."}
  lio_axes:
    A_locus:
      value: 1
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S4, locator: "Theist"}, {source: S7, locator: "Lisbon poem note 2; body"}, {source: S5, locator: "Théisme"}]
      how_known: "Written profession in Dictionary (1764) plus in-span Lisbon poem (1756). Independent works → corroborated (P48). Named alternative, so 0.7 not 1.0. Matches DEISM-system default A 1."
      rationale: "Transcendent creator distinct from the world: 'Supreme Being ... who has formed all beings' (S4); Lisbon note: 'there is likewise an infinity between God and all created beings whatever' (S7); Théisme: 'Dieu créateur' known from organized nature (S5). Moral Providence (punishes/rewards) keeps him nearer a thin person than Wilson's A 3 non-intervening force — so 1, not 3. Alternative 0: fully transcendent without personal moral-governance reading of Providence."
      alternatives:
        - {value: 0, note: "Supreme Being / Eternal Geometer read as fully transcendent without personal moral governance.", cites: [{source: S4, locator: "Theist; Atheism 'Eternal Geometer'"}]}
    B_cause:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S6, locator: "Miracles §1–§2"}, {source: S7, locator: "Lisbon poem (eternal / general laws)"}, {source: S4, locator: "Atheism (order / Newton)"}]
      how_known: "Own published statements about nature (P16); not a scientist (P30/P33 — Newtonian popularizer, not a contributor), so B rests on words, not P35. Dictionary + Lisbon → corroborated. Named alternative, so 0.7. P41's 0.5 cap for non-scientists who reject miracles without stating exceptionless order does not bind: he states immutability."
      rationale: "Scored on his account of nature (P6, P16). Miracles: nature's 'lois mathématiques, divines, immuables, éternelles'; 'une loi ne peut être à la fois immuable et violée'; God 'n'y changera jamais rien'; 'Il est donc absurde de croire des miracles'; nature as 'l'ordre éternel des choses' makes miracle 'impossible dans cet ordre' (S6). Lisbon: the Creator 'fix[ed] the laws of fate' and rules by 'general laws' (S7). Explicit no-exception claim → B 4. Alternative 3: Theist Providence that 'acts' / punishes, and Lisbon's remark that 'Nature is never very strict or rigid in her method of proceeding' (note 2), read as a limited softening rather than exceptionless order."
      alternatives:
        - {value: 3, note: "Providence that acts (Theist) or Lisbon 'Nature never very strict' read as a stated limited exception / soft lawfulness.", cites: [{source: S4, locator: "Theist"}, {source: S7, locator: "note 2"}]}
    C_ledger: {value: UNKNOWN, how_known: "Theist affirms God punishes crimes and rewards virtue (leans 1) but not scored this pass (do not force)."}
    D_authority: {value: UNKNOWN, how_known: "Miracles and Theist put reason over sectarian revelation (leans 3–4) but not scored this pass."}
    E_scope: {value: UNKNOWN, how_known: "Miracles rejects special favors for a few 'ants' (leans 3–4) but not scored this pass."}
  mid_basin:
    value: true
    certainty: 0.7
    cites: [{source: S4, locator: "Theist"}, {source: S6, locator: "Miracles §1"}, {source: S7, locator: "Lisbon poem"}]
    how_known: "P4/P6 test: A_locus 1 (0.7) ≤ 1 and B_cause 4 (0.7) ≥ 3, both at ≥ 0.7, so true. Certainty is the lower of the two (0.7). Named alternatives (A 0, B 3) stay on the same side of the A≤1 and B≥3 conditions (P30). Support corroborated on both (P48) → filled; darkness dark."
  statements:
    - text: "THE theist is a man firmly persuaded of the existence of a Supreme Being as good as He is powerful, who has formed all beings with extension, vegetating, sentient and reflecting; who perpetuates their species, who punishes crimes without cruelty, and rewards virtuous actions with kindness. The theist does not know how God punishes, how he protects, how he pardons, for he is not reckless enough to flatter himself that he knows how God acts, but he knows that God acts and that He is just. [...] He laughs at Lorette and at Mecca; but he succours the needy and defends the oppressed."
      cites: [{source: S4, locator: "Theist"}]
      date: "1764"
      context: "Philosophical Dictionary, article 'Theist' (Woolf tr.); after the listed span, under P31 continuity."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
    - text: "Un miracle est la violation des lois mathématiques, divines, immuables, éternelles. Par ce seul exposé, un miracle est une contradiction dans les termes : une loi ne peut être à la fois immuable et violée. [...] ainsi il n'y changera jamais rien. [...] Il est donc absurde de croire des miracles, c'est déshonorer en quelque sorte la Divinité."
      cites: [{source: S6, locator: "Miracles, Section I"}]
      date: "1764"
      context: "Dictionnaire philosophique, article Miracles; philosophers' argument Voltaire advances (ironic Christian concessions follow)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "French original; protective Christian concessions later in the article are not taken as his scored view (same voice as Theist laughing at Lorette)."
    - text: "Comme on raffine sur tout, on raffina sur cette définition ; on appela miracle ce qui est impossible à la nature ; mais on ne songea pas que c'était dire que tout miracle est réellement impossible. Car qu'est-ce que la nature ? Vous entendez par ce mot l'ordre éternel des choses. Un miracle serait donc impossible dans cet ordre. En ce sens Dieu ne pourrait faire de miracle."
      cites: [{source: S6, locator: "Miracles, Section II"}]
      date: "1764"
      context: "Dictionnaire philosophique, Miracles §2; nature as eternal order."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
    - text: "there is likewise an infinity between God and all created beings whatever. [...] God is the cause and the regulator of that order. Homer's Jupiter was the slave of destiny; but, according to more rational philosophy, God is the master of destiny."
      cites: [{source: S7, locator: "Lisbon Earthquake, note 2"}]
      date: "1756"
      context: "Poème sur le désastre de Lisbonne, author's note (Fleming tr.); within the span."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
    - text: "All's right, you answer, the eternal cause / Rules not by partial, but by general laws. [...] Are you then sure, the power which could create / The universe and fix the laws of fate, / Could not have found for man a proper place, / But earthquakes must destroy the human race?"
      cites: [{source: S7, locator: "Lisbon Earthquake, body"}]
      date: "1756"
      context: "Lisbon poem; challenges optimism while affirming a Creator who fixed general laws."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
    - text: "Newton's intelligence, therefore, came from another intelligence. [...] The world is assuredly an admirable machine; therefore there is in the world an admirable intelligence, wherever it may be. [...] Either the heavenly bodies are great geometers, or the Eternal Geometer has arranged the heavenly bodies. [...] All that I know is that one must worship Him and be just."
      cites: [{source: S4, locator: "Atheism, Section I"}]
      date: "1764"
      context: "Philosophical Dictionary, Atheism; design / Eternal Geometer argument against atheists."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
  changes_over_life: []
  coder_notes: "D1: DEISM/A1/B4/mid true from Dictionary + Lisbon. Span left 1734–1759 at 0.5 (alt end 1778); Dictionary used under P31. Traité sur la tolérance (1763) and Éléments de la philosophie de Newton (1738) not re-read as page text this pass — would corroborate further. C/D/E left UNKNOWN (do not force). Chart-moving YES; figures/ untouched."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: "Roman Catholic (context)", certainty: 0.5, cites: [{source: S1, locator: "1.1"}, {source: S8, locator: "Early life"}], how_known: "Jesuit Collège Louis-le-Grand (S1); Wikipedia dual-bio (P50) notes Catholic baptismal context. Context only — never a worldview code."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not confirmed in sources read this pass."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1734–1759", certainty: 0.5, cites: [{source: S1, locator: "1.3; 2"}], how_known: "Lettres philosophiques (1734) to Candide (1759), first and last lasting items (P29, P30); 0.5 following Candide (weakest-work rule). Alternative 1734–1778. Dictionary 1764 used for worldview under P31, not by expanding the span this pass."}
  age_at_first_lasting_contribution: {value: 40, certainty: 0.7, cites: [{source: S1, locator: "1. Voltaire's Life"}], how_known: "S1: 'published in 1734 when he was forty years old'; 1734 − 1694 = 40."}
  first_evidence_of_lio_type_views: {value: "1756", certainty: 0.7, cites: [{source: S7, locator: "Lisbon Earthquake"}], how_known: "In-span Lisbon poem carries scored A/B statements (Creator; general/eternal laws). Dictionary 1764 restates. Earlier works (Éléments 1738) not re-read as page text — year certainty would drop to 0.5 if earlier unread works are required; Lisbon is the earliest dated LIO-type view checked this pass."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S7, locator: "1756"}], how_known: "Lisbon is inside 1734–1759; Dictionary under P31 agrees."}
  worldview_during_major_work: {value: "DEISM (0.7); A 1 / B 4", certainty: 0.7, cites: [{source: S4, locator: "Theist"}, {source: S6, locator: "Miracles"}, {source: S7, locator: "Lisbon"}], how_known: "Coded from Lisbon (in-span) and Dictionary (P31)."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Enlightenment critique and prose satire (S1); Newtonian popularization is not geometric-form work in the Lane B sense.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "Lane B only. No geometric-form claim from this deepen."
  notes: ""

institutions:
  - {value: "Court of Frederick II of Prussia", role: "guest and chamberlain", years: "1750–1753", kind: "patron or funder", certainty: 0.5, cites: [{source: S1, locator: "1.5"}, {source: S3, locator: "para. 4"}], how_known: "Britannica students edition gives 1750 and 'three years later'."}
collaborators:
  - {value: "Émilie du Châtelet", relation: "collaborator", note: "companion and fellow Newtonian, from 1733", certainty: 0.7, cites: [{source: S1, locator: "1.3–1.4"}], how_known: "SEP."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 223"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Deepen D1: DEISM / A 1 / B 4 / mid true; chart would move at next figure refresh (figures/ not touched)."
    - "Candide lasting at 0.5; span end still 1759 at 0.5 (alt 1778)."
    - "Miracles article mixes philosophers' voice with ironic Christian concessions — scored from the philosophers' / Theist voice."
  open_questions:
    - "Span end: 1759 (Candide) or 1778?"
    - "Éléments de la philosophie de Newton (1738) page-text for earlier LIO evidence."
    - "Traité sur la tolérance (1763) for further P27 / C corroboration."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "J.B. Shank"
    citation: "Shank, J.B. 'Voltaire.' Stanford Encyclopedia of Philosophy (substantive revision 21 August 2024). https://plato.stanford.edu/entries/voltaire/"
    url: "https://plato.stanford.edu/entries/voltaire/"
    accessed: 2026-10-19
    source_quality: "reference entry"
    reliability_note: "Signed encyclopedia entry, read in full."
    used_for: [identity, basics, contribution, childhood, worldview, timing, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [review]
  - id: S3
    type: tertiary
    kind: "encyclopedia"
    author: "Encyclopaedia Britannica"
    citation: "'Voltaire.' Britannica (students edition). https://kids.britannica.com/students/article/Voltaire/277627"
    url: "https://kids.britannica.com/students/article/Voltaire/277627"
    accessed: 2026-10-19
    source_quality: "reference entry"
    reliability_note: "Read in full; used for full dates and a few works."
    used_for: [basics, contribution]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Voltaire (François-Marie Arouet)"
    citation: "Voltaire. Philosophical Dictionary. Selected and translated by H.I. Woolf. New York: Knopf, 1924. Articles 'Theist' and 'Atheism' via Hanover Historical Texts. https://history.hanover.edu/texts/voltaire/voltheis.html ; Atheism in Project Gutenberg eBook 18569."
    url: "https://history.hanover.edu/texts/voltaire/voltheis.html"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Own published dictionary (1764); English Woolf translation of Theist read in full; Atheism section read in Gutenberg selection."
    used_for: [worldview]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Voltaire (François-Marie Arouet)"
    citation: "Voltaire. Dictionnaire philosophique, article 'Théisme'. French text via monsieurdevoltaire.com (web copy of the article)."
    url: "https://www.monsieurdevoltaire.com/article-dictionnaire-philosophique-t-comme-theisme-104781128.html"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "French article text; unofficial web copy of a public-domain work. Cross-checked against the Theist article (S4)."
    used_for: [worldview]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Voltaire (François-Marie Arouet)"
    citation: "Voltaire. Dictionnaire philosophique, article 'Miracles' (1764). French text via monsieurdevoltaire.com and correspondance-voltaire.de."
    url: "https://www.monsieurdevoltaire.com/article-dictionnaire-philosophique-m-comme-miracles-partie-1-116229987.html"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "French article Sections I–II read; unofficial web copy of a public-domain work. Chicago Intertextual Hub confirms 1764 Dictionnaire locus."
    used_for: [worldview]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "Voltaire (François-Marie Arouet)"
    citation: "Voltaire. 'The Lisbon Earthquake' (Poème sur le désastre de Lisbonne, 1756). In The Works of Voltaire, Vol. 36, tr. William F. Fleming. Wikisource."
    url: "https://en.wikisource.org/wiki/The_Works_of_Voltaire/Volume_36/The_Lisbon_Earthquake"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "In-span poem plus author's notes; English Fleming translation on Wikisource, read in full."
    used_for: [worldview, timing]
  - id: S8
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "Wikipedia. 'Voltaire.' English Wikipedia. Dual-biography use only (P50)."
    url: "https://en.wikipedia.org/wiki/Voltaire"
    accessed: 2026-10-24
    source_quality: "other"
    reliability_note: "P50 dual-bio / heritage context only; not used for worldview scores."
    used_for: [heritage]
---

## Summary

Voltaire (1694–1778), French writer and philosophe [S1]. Deepen D1: primary_system DEISM (0.7); A 1 (0.7, corroborated); B 4 (0.7, corroborated); mid_basin true (0.7). Would plot dark filled at the next chart refresh; figures/ not refreshed this pass. Draft, not reviewed.

## Life and work

Paris; England; Cirey; Berlin; Ferney [S1].

## Contribution and impact

Lettres philosophiques 1734; Candide 1759 [S1]. Philosophical Dictionary 1764 used for worldview under P31 [S4–S6].

## Childhood and education

Louis-le-Grand [S1].

## Adult working worldview

Own words: theist / Supreme Being by reason and design; miracles as contradiction of immutable divine mathematical laws; Lisbon poem affirms a Creator who fixed general laws while rejecting optimism [S4–S7]. Coded DEISM; A 1 / B 4; mid true.

## Heritage (context only)

Catholic schooling context [S1; S8]. Context only.

## Timing

1734–1759, age 40 [S1]. First checked LIO-type view: Lisbon 1756 [S7].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No geometric-form claim from this deepen.

## Open questions

- Span end 1759 vs 1778; Éléments 1738 and Traité 1763 unread as page text.

## Research log

- 2026-10-24: Deepen D1 — Dictionary Theist / Théisme / Miracles; Lisbon poem; Wikipedia dual-bio. DEISM / A 1 / B 4 / mid true. Person file only.
- 2026-10-20: AB1 audit fix: S1's bibliography dates the Philosophical Letters to 1734; wording corrected (no score change).
- 2026-10-20: Read SEP (Shank, 2024) and Britannica students edition.
