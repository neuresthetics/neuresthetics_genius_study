---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch M; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-17
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-17, by: "Grok Bot", summary: "Record created (stage 3 batch M, order P32: F 5, rank 82). Basics from Britannica (Sadie, signed; body text only, Q&A boxes not cited). Worldview from letters 69 (1777), 107, 108 and 110 (1778) in Lady Wallace's translation, Gutenberg #5307. primary_system CHRIST (0.7); A 0 (0.7); B BELOW_THRESHOLD (Providence about events in his life, not nature, P16); C 0 (0.5, alt 1); mid_basin BELOW_THRESHOLD. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-17, by: "Grok Bot", summary: "Batch M audit fixes (/workspace/genius_study_audit/gs_159d60d_M/run1/, run 1: 16 hold, 3 weaken): A 0 and CHRIST lowered from 0.7 to 0.5 (letters predate the working years, P20; Franklin precedent). Values and mid_basin unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #81, F5 rank 82). Needs: A single source; A faded; B BELOW_THRESHOLD. New S4: DME / Bauer–Deutsch Nr. 1044 German autograph transcription (Vienna, 4 April 1787) — within-span private letter thanking 'meinem gott' and daily 'meinem Schöpfer' for familiarity with death as key to true blessedness (primary language). S5: DME English of BD 0355 (Augsburg, 23–25 Oct. 1777) corroborates Wallace 'Gott vor Augen' / omnipotence / wrath / mercy wording. S6: DME English BD 0458 (Paris, 3 July 1778) Voltaire 'reward' and God-alone-takes-life Providence. S7 Wikipedia EN dual-bio (P50): baptismal Joannes Chrysostomus…; practicing Catholic; Freemason 14 Dec. 1784 Zur Wohltätigkeit. S8 Morgan Library exhibition English of BD 1044 (Anderson-line). P47 source_quality on S1–S8. Mapped Wallace Gutenberg letter 69 ≈ BD 0355; 107 ≈ BD 0458; 108 ≈ BD 0462; 1787 death letter = BD 1044. Freemasonry join stays in changes_over_life; no documented change of A (still personal Gott/Schöpfer after 1784). Under P31 adult evidence + within-span 1787 → A 0 and CHRIST raised 0.5→0.7; support single→corroborated (S2+S4+S5; P48). B stays BELOW_THRESHOLD (P16): 1778–1787 Providence and 'Nature speaks in me' (1781 marriage letter, context only) are life/sexual nature, not nature's causal order; no Naturegesetze / law-vs-exception statement read. C stays 0 @0.5 (alt 1). mid_basin BELOW_THRESHOLD (B unscored). Chart-moving NO (still unplotted). Anderson print / full Bauer–Deutsch vols unread beyond DME web. No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: mozart-wolfgang-amadeus
  display_name: "Wolfgang Amadeus Mozart"
  roster:
    canonical_name: "Wolfgang Amadeus Mozart"
    rank: 82
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: music
    field_bucket: music
  full_name: {value: "Johann Chrysostom Wolfgang Amadeus Mozart", certainty: 0.7, cites: [{source: S1, locator: "header ('In full'; baptized Johannes Chrysostomus Wolfgangus Theophilus Mozart)"}, {source: S7, locator: "Baptismal record / Early life"}], how_known: "Britannica; Wikipedia baptismal form."}
  native_name: {value: UNKNOWN, how_known: "German in Latin script; he 'most commonly called himself Wolfgang Amadé or Wolfgang Gottlieb' (S1)."}
  aliases:
    - {name: "Mozart-Wolfgang Amadeus", kind: "roster alias"}
    - {name: "Wolfgang-Amadeus-Mozart", kind: "roster alias"}
    - {name: "Wolfgang Amadé Mozart", kind: "other"}

basics:
  birth:
    date: {value: "1756-01-27", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "opening"}], how_known: "Britannica; Wikipedia."}
    place: {value: "Salzburg, archbishopric of Salzburg", modern_name: "Salzburg, Austria", polity_then: "Archbishopric of Salzburg (Holy Roman Empire)", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "Getreidegasse 9"}], how_known: "Britannica; Wikipedia."}
  death:
    date: {value: "1791-12-05", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening; 'The last year'"}, {source: S7, locator: "opening"}], how_known: "Britannica; Wikipedia."}
    place: {value: "Vienna", modern_name: "Vienna, Austria", polity_then: "Habsburg Monarchy (Holy Roman Empire)", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "opening"}], how_known: "Britannica; Wikipedia."}
  first_lasting_contribution_year: {value: 1784, certainty: 0.5, cites: [{source: S1, locator: "'The central Viennese period'"}], how_known: "The 1784 piano concertos, with which 'he established a new level of piano concerto writing' (S1), are the earliest work the body text marks as lasting (P13). Die Entführung (1782) is dated but not marked as lasting; earlier works are described as accomplished, not lasting. 0.5 because the choice is the coder's."}
  era_bucket: {value: "1750 to 1849", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "From 1784 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Salzburg (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Salzburg and Vienna; tours of western Europe and Italy."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [German, Italian], certainty: 0.5, cites: [{source: S1, locator: "opera sections"}], how_known: "German singspiels and Italian operas (S1); letters in German. Coder's summary."}
  occupations: {value: ["composer", "pianist", "court Konzertmeister (Salzburg)"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'The Italian tours'"}], how_known: "Britannica."}

contribution:
  fields: {value: ["music composition"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Piano concertos of 1784", year: 1784, kind: work, lasting: "'he established a new level of piano concerto writing' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'The central Viennese period'"}], how_known: "Britannica."}
    - {value: "Le nozze di Figaro (K 492)", year: 1786, kind: work, lasting: "staged May 1, 1786, 'warmly received' and revived in 1789–90 (S1)", certainty: 0.7, cites: [{source: S1, locator: "'From Figaro to Don Giovanni'"}], how_known: "Britannica."}
    - {value: "Don Giovanni", year: 1787, kind: work, lasting: "given in Prague on October 29, 1787 (S1)", certainty: 0.7, cites: [{source: S1, locator: "'From Figaro to Don Giovanni'"}], how_known: "Britannica."}
    - {value: "Die Zauberflöte", year: 1791, kind: work, lasting: "'soon the opera became the most loved of all of Mozart's works for the stage' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'The last year'"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "Haydn in 1785: 'Your son is the greatest composer known to me in person or by name'", kind: "other", certainty: 0.7, cites: [{source: S1, locator: "'The central Viennese period'"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "'widely recognized as one of the greatest composers in the history of Western music' (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Roman Catholic", certainty: 0.7, cites: [{source: S7, locator: "'Mozart was raised a Catholic'"}], how_known: "Wikipedia; Salzburg archbishopric household."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father Leopold Mozart, violinist, author of a violin manual, deputy Kapellmeister at the Salzburg court", role: father, certainty: 0.7, cites: [{source: S1, locator: "'Early life and works'"}, {source: S7, locator: "Early life"}], how_known: "Britannica; Wikipedia."}
    - {value: "Mother Anna Maria Pertl, of a middle-class family in local administration", role: mother, certainty: 0.7, cites: [{source: S1, locator: "'Early life and works'"}, {source: S7, locator: "Early life"}], how_known: "Britannica; Wikipedia."}
  household_circumstances: {value: TODO}
  schooling: []
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Leopold Mozart (father), music teacher", certainty: 0.7, cites: [{source: S1, locator: "'Early life and works'"}], how_known: "Britannica."}
  languages_in_childhood: {value: [German], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading (Salzburg)."}
  notable_events:
    - {value: "Family tour of western Europe as a child performer", year: 1763, age: 7, certainty: 0.7, cites: [{source: S1, locator: "'Early life and works'"}], how_known: "Britannica (mid-1763 to November 1766)."}
    - {value: "Baptized the day after birth as Joannes Chrysostomus Wolfgangus Theophilus Mozart", year: 1756, age: 0, certainty: 0.7, cites: [{source: S7, locator: "Baptismal record / Early life"}], how_known: "Wikipedia."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1784–1791", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Roman Catholic (raised and practicing)", certainty: 0.7, cites: [{source: S7, locator: "'raised a Catholic and remained a practicing Catholic throughout his life'"}], how_known: "Wikipedia."}
    - {value: "Freemasonry (lodge Zur Wohltätigkeit, from 14 Dec. 1784)", certainty: 0.7, cites: [{source: S1, locator: "'From Figaro to Don Giovanni'"}, {source: S7, locator: "14 December 1784"}], how_known: "Britannica; Wikipedia. Membership, not by itself a worldview code."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read on science."}
  primary_system:
    value: CHRIST
    basis: consistent_private_letters
    certainty: 0.7
    cites: [{source: S4, locator: "BD 1044, Vienna, 4 April 1787 (Gott / Schöpfer)"}, {source: S2, locator: "Gutenberg letter ≈ Wallace Augsburg 25 Oct. 1777 / BD 0355"}, {source: S5, locator: "DME English BD 0355"}, {source: S7, locator: "practicing Catholic"}]
    rationale: "Practising Catholic in private letters across 1777–1787 and still thanking a personal Gott/Schöpfer inside the working years (BD 1044). Named alternative: none chosen as system code; Freemasonry from late 1784 is membership (S1; S7) and does not displace CHRIST — the 1787 letter after lodge entry still addresses Gott and Schöpfer."
    how_known: "Within-span private letter (S4 German) plus earlier consistent private letters (S2; S5) and Wikipedia practicing-Catholic summary (S7). Private writing / web scholarly edition, 0.7 ceiling. Batch M 0.5 pre-span cap lifted by within-span 1787 under P31 (no documented change of A/system after Freemasonry join)."
  secondary_system: {value: UNKNOWN, how_known: "No second system coded; Freemasonry kept as nominal affiliation only."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Rosary / good Christian life (1778), personal Gott and Schöpfer (1777, 1787), practicing Catholic (S7)."}
    - {code: CLTHEI, reason: "A providential personal God; CHRIST is more specific."}
  lio_axes:
    A_locus:
      value: 0
      basis: consistent_private_letters
      certainty: 0.7
      support: corroborated
      cites: [{source: S4, locator: "BD 1044 German: 'ich danke meinem gott' / 'danke ich alle tage meinem Schöpfer'"}, {source: S2, locator: "Wallace Augsburg 25 Oct. 1777 / Gutenberg letter 69"}, {source: S5, locator: "DME English BD 0355: 'I have God constantly before my eyes… omnipotence… wrath… love… mercy towards his creatures'"}, {source: S8, locator: "Morgan exhibition English of BD 1044"}, {source: S1, locator: "'From Figaro to Don Giovanni' (Masonic teaching on death letter)"}]
      how_known: "Within-span private letter 4 April 1787 (S4 German primary transcription; S8 EN exhibition) plus consistent 1777 private letters (S2 Wallace; S5 DME EN of same BD 0355). Independent source ids → corroborated (P48). Private writing / unofficial or web scholarly copies, 0.7 ceiling. Freemasonry join (1784) is documented but does not change locus — still personal Gott/Schöpfer in 1787 (P31)."
      rationale: "A personal God apart from the world who rules over persons: 'I have God constantly before my eyes… recognise his omnipotence… fear his wrath… love… mercy towards his creatures' (1777, BD 0355); 'ich danke meinem gott' and daily thanks to 'meinem Schöpfer' for learning death as the key to true blessedness (1787, BD 1044). Named alternative: 1 (Masonic impersonal 'friend of mankind' death imagery sits beside personal Gott/Schöpfer, not instead of it)."
      alternatives: [{value: 1, cites: [{source: S1, locator: "'From Figaro to Don Giovanni' (Masonic teaching on death)"}, {source: S4, locator: "BD 1044 death as best friend of man"}], note: "1787 death-as-best-friend teaching that Britannica ties to Masonic instruction; still thanks Gott/Schöpfer in the same letter. Alt cites subset of value cites (P48)."}]
    B_cause: {value: BELOW_THRESHOLD, how_known: "Providence statements are about events in his own life (mother's death: 'manifest will of God', Wallace/BD 0462–adjacent; 'only God' gives or takes life, BD 0458; plans; death as key to blessedness, BD 1044), not about the order of nature (P16), as for Beethoven. 'Nature speaks in me' (Vienna, 15 Dec. 1781, BD 0648) is sexual appetite / marriage rationale, not nature's laws — context only, not scored. No Naturgesetze / law-vs-exception statement read."}
    C_ledger:
      value: 0
      basis: consistent_private_letters
      certainty: 0.5
      support: corroborated
      cites: [{source: S2, locator: "Gutenberg letter 69; letter 107"}, {source: S6, locator: "DME English BD 0458: Voltaire 'that is the reward!'"}, {source: S4, locator: "BD 1044: death as key to true blessedness / thanks to Schöpfer"}, {source: S1, locator: "Masonic teaching note on 1787 death letter"}]
      how_known: "Private letters; 0.5 because the wording is conventional piety and an alternative is named. S2+S6+S4 → corroborated (P48)."
      rationale: "Reward and punishment of persons: 'I fear his wrath' (1777); on Voltaire's death, 'that is the reward!' (BD 0458, 1778); mother in heavenly bliss; 1787 death as key to true blessedness under Schöpfer. Named alternative: 1."
      alternatives: [{value: 1, cites: [{source: S4, locator: "BD 1044 death consolation"}, {source: S1, locator: "Masonic teaching note"}], note: "Conventional piety / possible Masonic afterlife consolation without clear personal merit ledger. Alt cites subset of value cites (P48)."}]
    D_authority: {value: UNKNOWN, how_known: "Nothing read on revelation against observation."}
    E_scope: {value: UNKNOWN, how_known: "'He will never abandon his servants' (1777) is about his own life; not scored (P7). Researched; no universal-scope claim read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 0 at 0.7 support corroborated, but B is BELOW_THRESHOLD, so neither branch can be tested (P4, P10, P48). Still unplotted."}
  statements:
    - text: "May Papa live without disquiet. I have God constantly before my eyes. I recognise his omnipotence, I fear his wrath, but I also recognise his love, his compassion and mercy towards his creatures. He will never abandon his servants – – if anything goes in accordance with his will, it will also be in accordance – – with mine; therefore it cannot go wrong – – I must be happy and content."
      cites: [{source: S5, locator: "DME English BD 0355, Augsburg, 23–25 Oct. 1777"}, {source: S2, locator: "Wallace Gutenberg letter 69, Augsburg, Oct. 25, 1777"}]
      date: "1777-10-25"
      context: "To his father; name-day thanks. Wallace wording checked against DME English of Bauer–Deutsch Nr. 0355."
      axes: [A_locus, C_ledger]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Wallace 1865 via Gutenberg #5307 cross-checked to DME English BD 0355 (Mozarteum). German autograph PDF for BD 0355 not retrieved this pass (HTML error on BD_0355.pdf path); English DME + Wallace agree on locus content. Pre-span under P31 still usable (no documented A change)."
    - text: "godless archscoundrel Voltaire has, so to speak, groaned his last like beast – that is the reward!"
      cites: [{source: S6, locator: "DME English BD 0458, Paris, 3 July 1778"}, {source: S2, locator: "Wallace Gutenberg letter 107"}]
      date: "1778-07-03"
      context: "To his father, written the night his mother died."
      axes: [C_ledger]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Wallace 'ungodly arch-villain… This is his reward!' matched to DME English BD 0458 'godless archscoundrel… that is the reward!'. Same night as mother's death; also contains 'only God' gives or takes life (life-Providence, not B)."
    - text: "remember that God Almighty has ordained it, and how can we rebel against Him? Let us rather pray to Him and thank Him for His goodness, for she died a happy death."
      cites: [{source: S2, locator: "Gutenberg letter 108, Paris, July 9, 1778"}, {source: S2, locator: "maps to DME BD 0462 (English PDF read in deepen; Wallace retained as cite)"}]
      date: "1778-07-09"
      context: "To his father, on his mother's death. DME BD 0462 English: surrender to God's will and worship his providence; 'God Almighty would have it so'."
      axes: [A_locus, B_cause]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "DME English BD 0462 read 2026-10-24 (parallel wording). About a death in his family, not nature's order (P16) — B cite is negative evidence."
    - text: "In the first place, I must tell you that NOTHING could have saved my mother. No doctor in the world could have restored her to health. It was the manifest will of God; her time was come, and God chose to take her to Himself."
      cites: [{source: S2, locator: "Gutenberg letter 110, Paris, July 31, 1778"}]
      date: "1778-07-31"
      context: "To his father."
      axes: [B_cause]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-17
      note: "Wallace only this pass (BD number not re-fetched). About a death in his family, not nature's order (P16)."
    - text: "da der tod |: genau zu nemmen :| der wahre Endzweck unsers lebens ist, so habe ich mich seit ein Paar Jahren mit diesem wahren, besten freunde des Menschen so bekannt gemacht, daß sein Bild nicht allein nichts schreckendes mehr für mich hat, sondern recht viel beruhigendes und tröstendes! – und ich danke meinem gott daß er mir das glück gegönnt hat mir die gelegenheit |: sie verstehen mich :| zu verschaffen, ihn als den schlüssel zu unserer wahren glückseeligkeit kennen zu lernen. – ich lege mich nie zu bette ohne zu bedenken daß ich vielleicht |: so Jung als ich bin :| den andern tag nicht mehr seÿn werde – und es wird doch kein Mensch von allen die mich kennen sagn können daß ich im umgange Mürrisch oder trauerig wäre – und für diese glückseeligkeit danke ich alle tage meinem Schöpfer, und wünsche sie vom Herzen Jedem meiner Mitmenschen."
      cites: [{source: S4, locator: "DME German BD 1044, Vienna, 4 April 1787"}, {source: S8, locator: "Morgan exhibition English"}, {source: S4, locator: "DME English parallel: 'I thank my God' / 'I thank my creator every day'"}]
      date: "1787-04-04"
      context: "Last extant letter to Leopold before Leopold's death (28 May 1787). Written inside working years, after Freemasonry join (14 Dec. 1784). Britannica ties the death-as-friend teaching to Masonic instruction; the same letter thanks Gott and Schöpfer."
      axes: [A_locus, C_ledger]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Primary German from Internationale Stiftung Mozarteum DME transcription of Bauer–Deutsch Nr. 1044 (Bibliotheca Mozartiana). Within-span A evidence. Death-friend imagery is Masonic-adjacent context; locus score rests on Gott/Schöpfer."
  changes_over_life:
    - {value: "Joined Freemasonry (lodge Zur Wohltätigkeit) on 14 December 1784; composed Masonic music thereafter", year: 1784, age: 28, certainty: 0.7, cites: [{source: S1, locator: "'From Figaro to Don Giovanni'"}, {source: S7, locator: "14 December 1784"}], how_known: "Britannica; Wikipedia. Does not document a change of A — BD 1044 (1787) still thanks Gott/Schöpfer."}
  coder_notes: "Deepen D1: A 0 @ 0.7 support corroborated (DME German BD 1044 + Wallace/DME BD 0355). CHRIST 0.7. B stays BELOW_THRESHOLD (P16). Freemasonry is affiliation, not a scored A shift. Anderson print Letters and full Bauer–Deutsch paper vols unread beyond DME web PDFs. Chart still unplotted."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Salzburg German-speaking", certainty: 0.5, cites: [{source: S1, locator: "'Early life and works'"}, {source: S7, locator: "Early life"}], how_known: "Coder's reading."}
  religious_heritage_by_birth: {value: "Roman Catholic", certainty: 0.7, cites: [{source: S7, locator: "raised a Catholic; baptismal record"}], how_known: "Wikipedia."}
  baptism_or_initiation: {value: "Baptized day after birth (28 Jan. 1756) as Joannes Chrysostomus Wolfgangus Theophilus Mozart", certainty: 0.7, cites: [{source: S7, locator: "Baptismal record / Early life"}], how_known: "Wikipedia."}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1784–1791", certainty: 0.5, cites: [{source: S1, locator: "'The central Viennese period'; 'The last year'"}], how_known: "First to last listed lasting contribution (P29, P30); the start is the coder's pick (see first_lasting_contribution_year)."}
  age_at_first_lasting_contribution: {value: 28, certainty: 0.5, cites: [{source: S1, locator: "opening; 1784"}], how_known: "1784 − 1756 = 28 (P30)."}
  first_evidence_of_lio_type_views: {value: "1777-10-25", certainty: 0.7, cites: [{source: S5, locator: "BD 0355"}, {source: S2, locator: "Wallace letter 69"}], how_known: "A 0 private letter (God before my eyes / omnipotence / wrath / mercy)."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "BD 1044 (4 April 1787) falls inside 1784–1791; earlier A letters (1777–78) agree and predate the span. B remains BELOW_THRESHOLD.", certainty: 0.7, cites: [{source: S4, locator: "BD 1044, 1787"}, {source: S1, locator: "span"}], how_known: "Dates."}
  worldview_during_major_work: {value: "Personal Catholic Gott/Schöpfer in private letters (BD 1044, 1787) after Freemason lodge entry; Providence about life events; no statement on nature's causal order read.", certainty: 0.7, cites: [{source: S4, locator: "BD 1044"}, {source: S7, locator: "practicing Catholic; Freemasonry"}], how_known: "Within-span letter plus Wikipedia affiliations."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Nothing read that states a geometric / mathematical form of the world.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Nothing read."}
  circle_present: {value: "unclear", rationale: "God as ruler of his life and Schöpfer thanked for death-consolation; nothing on God as source or end of a cosmic order of nature.", certainty: 0.5, cites: [{source: S4, locator: "BD 1044"}, {source: S5, locator: "BD 0355"}], how_known: "Coder's reading of letters scored for Lane A."}
  reading: "Providentialist Catholic in private letters 1777–1787; Freemason after 1784; Lane A A=0, B unscored."
  notes: "Lane B separate from Lane A. H1 not tested (B BELOW_THRESHOLD)."

institutions:
  - {value: "Salzburg court (honorary Konzertmeister, 1769; salaried Konzertmeister)", role: musician, years: "1769–1781", kind: other, certainty: 0.7, cites: [{source: S1, locator: "'Early life and works'; 'Vienna: the early years'"}], how_known: "Britannica; discharge granted June 9, 1781."}
  - {value: "Freemason lodge Zur Wohltätigkeit (Beneficence), Vienna", role: member, years: "1784–1791", kind: other, certainty: 0.7, cites: [{source: S7, locator: "14 December 1784"}], how_known: "Wikipedia."}
collaborators:
  - {value: "Lorenzo Da Ponte", relation: collaborator, note: "librettist of Figaro and Don Giovanni", certainty: 0.7, cites: [{source: S1, locator: "'From Figaro to Don Giovanni'"}], how_known: "Britannica."}
  - {value: "Emanuel Schikaneder", relation: collaborator, note: "Die Zauberflöte", certainty: 0.7, cites: [{source: S1, locator: "'The last year'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 82"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Early letters also in 19th-century Wallace translation; locus wording cross-checked to DME English BD 0355 / BD 0458 / BD 0462 and German BD 1044."
    - "German PDF for BD 0355 not retrieved this pass (path returned HTML)."
  open_questions:
    - "Anderson print Letters or Bauer–Deutsch paper volumes for any nature-order statement for B."
    - "German autograph / DME German of BD 0355 if the PDF path is restored."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Stanley Sadie"
    citation: "Sadie, Stanley. \"Wolfgang Amadeus Mozart.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Wolfgang-Amadeus-Mozart. Read live (first pages) and in Wayback snapshots: main page 2026-10-12 15:37:40 UTC; sections 'The Italian tours' 20260902024550, 'Mannheim and Paris' 20250918141441, 'Vienna: the early years' 20250911111426, 'The central Viennese period' 20261004215915, 'From Figaro to Don Giovanni' 20260307234235, 'The last year' 20260820031618, 'Mozart's place' 20250911120103. Deepen D1 re-opened Wayback main 2026-10-12."
    url: "https://www.britannica.com/biography/Wolfgang-Amadeus-Mozart"
    accessed: 2026-10-24
    reliability_note: "Signed article (Sadie, editor of The New Grove); byline agrees live and in Wayback. Body text only; Q&A boxes and Top Questions not cited. Live britannica.com may 403; Wayback used."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: letter
    author: "Wolfgang Amadeus Mozart"
    citation: "Mozart, Wolfgang Amadeus. The Letters of Wolfgang Amadeus Mozart, vol. 1, trans. Lady Wallace from the collection of Ludwig Nohl (1865). Project Gutenberg eBook #5307. https://www.gutenberg.org/ebooks/5307. Letters used: Wallace Augsburg 25 Oct. 1777 (≈ BD 0355); Paris 3 July 1778 (≈ BD 0458); Paris 9 July 1778 (≈ BD 0462); Paris 31 July 1778."
    url: "https://www.gutenberg.org/ebooks/5307"
    accessed: 2026-10-24
    reliability_note: "19th-century translation, keyed text; unofficial web copy, §7 cap 0.7. Locus wording of 1777/1778 letters cross-checked to DME (S5, S6) in deepen D1."
    source_quality: "unofficial web copy"
    used_for: [worldview, timing, lane_b]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-17
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S4
    type: primary
    kind: scholarly edition
    author: "Wolfgang Amadeus Mozart"
    citation: "Mozart, Wolfgang Amadé. Letter to Leopold Mozart, Vienna, 4 April 1787. Bauer–Deutsch Nr. 1044 (Bd. 4, S. 40–42). German transcription and English translation, Digital Mozart Edition / Internationale Stiftung Mozarteum. German: https://dme.mozarteum.at/DME/objs/raradocs/transcr/pdf/BD_1044.pdf ; English: https://dme.mozarteum.at/DME/objs/raradocs/transcr/pdf_eng/1044_WAM_LM_1787.pdf ; catalog: https://dme.mozarteum.at/DME/briefe/letter.php?mid=1614 ."
    url: "https://dme.mozarteum.at/DME/briefe/letter.php?mid=1614"
    accessed: 2026-10-24
    reliability_note: "Scholarly digital edition of the German autograph (Bibliotheca Mozartiana). Primary language for within-span A. Web scholarly edition; private letter, 0.7 ceiling."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, timing, lane_b]
  - id: S5
    type: primary
    kind: scholarly edition
    author: "Wolfgang Amadeus Mozart"
    citation: "Mozart, Wolfgang Amadé. Letter to Leopold Mozart, Augsburg, 23–25 October 1777. Bauer–Deutsch Nr. 0355. English translation, Digital Mozart Edition / Internationale Stiftung Mozarteum. https://dme.mozarteum.at/DME/objs/raradocs/transcr/pdf_eng/0355_WAM_LM_1777.pdf ."
    url: "https://dme.mozarteum.at/DME/objs/raradocs/transcr/pdf_eng/0355_WAM_LM_1777.pdf"
    accessed: 2026-10-24
    reliability_note: "DME English of BD 0355; corroborates Wallace 'God constantly before my eyes' / omnipotence / wrath / mercy. German PDF path returned HTML this pass."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, timing]
  - id: S6
    type: primary
    kind: scholarly edition
    author: "Wolfgang Amadeus Mozart"
    citation: "Mozart, Wolfgang Amadé. Letter to Leopold Mozart, Paris, 3 July 1778. Bauer–Deutsch Nr. 0458. English translation, Digital Mozart Edition / Internationale Stiftung Mozarteum. https://dme.mozarteum.at/DME/objs/raradocs/transcr/pdf_eng/0458_WAM_LM_1778.pdf ."
    url: "https://dme.mozarteum.at/DME/objs/raradocs/transcr/pdf_eng/0458_WAM_LM_1778.pdf"
    accessed: 2026-10-24
    reliability_note: "DME English; Voltaire 'reward' and God-alone-takes-life Providence (life events, not B)."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview]
  - id: S7
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. \"Wolfgang Amadeus Mozart.\" Wikipedia. https://en.wikipedia.org/wiki/Wolfgang_Amadeus_Mozart ."
    url: "https://en.wikipedia.org/wiki/Wolfgang_Amadeus_Mozart"
    accessed: 2026-10-24
    reliability_note: "P50 dual-source biography with S1. Used for baptismal name, practicing Catholic, Freemason lodge date (Solomon 1995 via wiki)."
    source_quality: "other"
    used_for: [identity, basics, childhood, worldview, heritage, timing, institutions]
  - id: S8
    type: primary
    kind: letter
    author: "Wolfgang Amadeus Mozart"
    citation: "Mozart, Wolfgang Amadeus. Autograph letter to Leopold Mozart, Vienna, 4 April 1787. English exhibition translation. The Morgan Library & Museum, online exhibition 'Mozart's last letter to his father'. https://www.themorgan.org/exhibitions/online/mozart/429 . International Mozarteum Foundation, DocBD 1044."
    url: "https://www.themorgan.org/exhibitions/online/mozart/429"
    accessed: 2026-10-24
    reliability_note: "Independent English exhibition translation of BD 1044 (Anderson-line wording); used with S4 German. Unofficial web page of museum exhibition."
    source_quality: "unofficial web copy"
    used_for: [worldview]
---

# Wolfgang Amadeus Mozart

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Wolfgang Amadeus Mozart (1756–1791), Austrian composer [S1; S7]. Deepen D1 (P47–P50): primary_system CHRIST (0.7); A 0 at 0.7 consistent_private_letters, support corroborated (S2+S4+S5; alt 1); B BELOW_THRESHOLD (P16); C 0 at 0.5 (alt 1); D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Still unplotted (B BELOW).

## Life and work

Child prodigy taught by his father; Salzburg court; Vienna from 1781 [S1]. Freemason, lodge Zur Wohltätigkeit, from 14 December 1784 [S7].

## Contribution and impact

Piano concertos of 1784; Figaro (1786), Don Giovanni (1787), Die Zauberflöte (1791) [S1].

## Childhood and education

Baptized Joannes Chrysostomus Wolfgangus Theophilus Mozart [S7]. Taught by Leopold Mozart; toured western Europe 1763–66 [S1]. Raised Catholic [S7].

## Adult working worldview

'I have God constantly before my eyes… omnipotence… wrath… love… mercy towards his creatures' (BD 0355 / Wallace, 1777) [S5; S2]. Within the working years: 'ich danke meinem gott' and daily thanks to 'meinem Schöpfer' for death as key to true blessedness (BD 1044, 4 April 1787) [S4; S8]. Freemason from end of 1784 [S1; S7]. A 0 at 0.7, support corroborated; B BELOW_THRESHOLD (P16).

## Heritage (context only)

Salzburg Catholic family; baptismal record [S1; S7].

## Timing

First lasting contribution 1784, at 28 [S1]. LIO-type A evidence from 1777; within-span confirmation 1787 [S5; S4].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form/circle unclear; H1 not tested (B BELOW).

## Open questions

- Anderson print or full Bauer–Deutsch paper vols for any nature-order statement for B.
- German DME of BD 0355 if PDF path restored.

## Research log

- 2026-10-17: Read Britannica (Sadie) live and in Wayback section snapshots; read Gutenberg #5307 (Wallace vol. 1) and searched it for God, Providence, will of God, Catholic; volume 2 not on Gutenberg.
- 2026-10-24 (deepen D1, queue #81): DME German+English BD 1044 (1787); DME English BD 0355, 0458, 0462; Morgan exhibition EN of 1044; Wikipedia EN dual-bio (baptism, practicing Catholic, Freemason 14 Dec. 1784). Re-opened Wallace Gutenberg and Britannica Wayback. P47 on S1–S8; A support single→corroborated and cert 0.5→0.7; B stays BELOW (P16). Chart-moving NO. No fallacy_catalog (Jason).
