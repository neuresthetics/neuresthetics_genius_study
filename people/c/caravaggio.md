---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z5)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to early_modern. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #147, F 3, rank 153). Needs: A UNKNOWN; B UNKNOWN; thin sources; hunt trial/Order docs. Read 1603 Baglione libel deposition (Italian via Sgarbi/Filodiritto S5; Friedländer p.276 via Jasiński 2022 S6; EN Prestel S7) — valent'huomo / 'imitar bene le cose naturali' = pictorial mimesis only, no religion. Prestel: almost no own-voice writings beyond that deposition. Order of St John: Bulla Receptionis / Knight of Obedience 14 July 1608, expelled Dec 1608 as foul and rotten member (S4, S8) — nominal affiliation / status-pardon path, not scored CHRIST profession (P16 commissions ≠ belief; standard Order vows not own creed statement). Dual bio Wikipedia EN (S4) + retained Britannica Graham-Dixon (S1; live Cloudflare-blocked this pass). Baptism Santo Stefano in Brolo, Milan (S4). primary_system UNKNOWN (CHRIST lead only); A UNKNOWN; B UNKNOWN (P16); C–E UNKNOWN; mid_basin UNKNOWN. P47 on S1–S8. Chart-moving NO. No fallacy_catalog (Jason). Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z8 audit fix (v8's call on the auditor's advice): S3 page was read; author Keith Christiansen (October 2003). Values unchanged."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z7 audit fix (RQ-Z7-N1, v8's call on the auditor's advice: artworks are dated by public unveiling or installation, P30 #1, as publication is for texts). The Contarelli canvases were unveiled in 1600 (Met Heilbrunn essay, S3: 'were unveiled in 1600, and established his reputation'), so the item year, first-lasting year and span are 1600; age 28 -> 29; era '1400 to 1599' -> '1600 to 1749' (edge year goes to the later bucket)."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z5 audit fix (Z5-30, P26/P13): question-box and caption 'lasting' cites removed. Read the signed body section 'Rome: 1599–1606': contract of 23 July 1599 for the Contarelli Chapel side canvases (The Calling and The Martyrdom of St. Matthew); 'The paintings for the Contarelli Chapel instantly established Caravaggio as the most dynamic and original painter working in Rome.' Lasting list is now the Contarelli canvases alone (1599–1600; caption date, range start under P12). Conversion of St. Paul and Entombment dropped from the lasting list (no body text calls them lasting). Span 1601–1604 -> 1599–1600; age 30 -> 28; era '1600 to 1749' -> '1400 to 1599'. Worldview unchanged (all UNKNOWN); not plotted."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z5, order P32: F 3, rank 153). Source: Britannica (Andrew Graham-Dixon, signed; opening, 'Becoming Caravaggio', 'Tragic childhood' read). No own words on religion read; religious commissions are work, not profession (P16). Not a scientist. Span 1601–1604 at 0.5 (Conversion of St. Paul 1601; Entombment 1602–04, latest year P30 #4), from captions. primary_system UNKNOWN (lead CHRIST); A UNKNOWN; B UNKNOWN; C, D, E UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: caravaggio
  display_name: "Caravaggio"
  roster:
    canonical_name: "Caravaggio"
    rank: 153
    F: 3
    models: [Claude, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: art
    field_bucket: arts
  full_name: {value: "Michelangelo Merisi", certainty: 0.7, cites: [{source: S1, locator: "Also known as"}, {source: S4, locator: "lede / Early life"}], how_known: "Britannica and Wikipedia."}
  native_name: {value: "Michelangelo Merisi da Caravaggio", certainty: 0.7, cites: [{source: S1, locator: "'Tragic childhood'"}, {source: S4, locator: "lede"}], how_known: "Named from the Lombard town; dual-sourced form."}
  aliases:
    - {name: "Michelangelo Merisi", kind: "birth name"}
    - {name: "Michelangelo Merisi da Caravaggio", kind: "other"}
    - {name: "Fra Michelangelo", kind: "religious name"}

basics:
  birth:
    date: {value: "1571-09-29", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "'Tragic childhood'"}, {source: S4, locator: "infobox / Early life"}], how_known: "Feast of St Michael; Wikipedia and Britannica agree on 29 September 1571."}
    place: {value: "Milan (baptized Santo Stefano in Brolo); family of Caravaggio, Lombardy", modern_name: "Milan, Lombardy, Italy", polity_then: "Duchy of Milan", certainty: 0.7, cites: [{source: S4, locator: "Early life — baptism certificate found 2007"}, {source: S1, locator: "Born; 'Tragic childhood'"}], how_known: "Wikipedia: born Milan; baptism certificate Santo Stefano in Brolo (2007 find). Britannica still said 'probably… Caravaggio' — dual-sourced toward Milan."}
  death:
    date: {value: "1610-07-18", calendar: gregorian, certainty: 0.5, cites: [{source: S1, locator: "Died"}, {source: S4, locator: "Death"}], how_known: "Britannica July 18/19; Wikipedia 18 July 1610 — day still soft."}
    place: {value: "Porto Ercole, Tuscany", modern_name: "Porto Ercole, Italy", polity_then: "State of the Presidi", certainty: 0.7, cites: [{source: S1, locator: "Died"}, {source: S4, locator: "Death"}], how_known: "Dual-sourced."}
  first_lasting_contribution_year: {value: 1600, certainty: 0.7, cites: [{source: S1, locator: "'Rome: 1599–1606' (body)"}, {source: S3, locator: "para. 2"}], how_known: "Dated by public unveiling (RQ-Z7-N1, P30 #1): the canvases 'were unveiled in 1600' (S3). Contarelli side canvases: contract 23 July 1599 (body)."}
  era_bucket: {value: "1600 to 1749", certainty: 1.0, cites: [{source: S3, locator: "para. 2"}], how_known: "1600 (P2; edge year goes to the later bucket)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "Born"}, {source: S4, locator: "Early life"}], how_known: "Italy (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S4, locator: "Biography — Rome, Naples, Malta"}], how_known: "Rome; later Naples, Malta, Sicily."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S4, locator: "lede"}], how_known: "As recorded."}
  languages_of_work: {value: ["Italian"], certainty: 0.7, cites: [{source: S5, locator: "1603 deposition Italian"}, {source: S1, locator: "text"}], how_known: "Trial testimony in Italian; painting career in Italian courts."}
  occupations: {value: ["painter"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lede"}], how_known: "Dual-sourced."}

contribution:
  era_bucket: early_modern
  fields: {value: ["painting"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lede"}], how_known: "Dual-sourced."}
  lasting_original_contributions:
    - {value: "The Calling of St. Matthew and The Martyrdom of St. Matthew, Contarelli Chapel, San Luigi dei Francesi", year: 1600, kind: work, lasting: "'instantly established Caravaggio as the most dynamic and original painter working in Rome' (S1, body)", certainty: 0.7, cites: [{source: S1, locator: "'Rome: 1599–1606' (body)"}, {source: S3, locator: "para. 2"}], how_known: "Signed body text (P13). Dated by unveiling, 1600 (S3; RQ-Z7-N1, P30 #1); contract 23 July 1599 (body)."}
  evidence_of_impact:
    - {value: "Shaped Rembrandt, Velázquez, Géricault and filmmakers", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "'Becoming Caravaggio'"}], how_known: "Britannica."}
    - {value: "Caravaggisti / tenebrist following across Europe", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S4, locator: "The Caravaggisti"}, {source: S3, locator: "essay"}], how_known: "Wikipedia and Met Heilbrunn."}
  major_works:
    - {value: "The Conversion of St. Paul (second version), Santa Maria del Popolo", year: 1601, kind: artwork, certainty: 0.7, cites: [{source: S1, locator: "'Rome: 1599–1606' (body: commissioned autumn 1600); caption 1601"}], how_known: "Named in the body; not called lasting there, so not on the lasting list."}
    - {value: "The Beheading of Saint John the Baptist, St John's Co-Cathedral, Valletta", year: 1608, kind: artwork, certainty: 0.7, cites: [{source: S4, locator: "Malta"}, {source: S8, locator: "Beheading / passaggio"}], how_known: "Largest work; only signed painting; Order altarpiece — not added to lasting list (P13: lasting claim remains Contarelli in S1 body)."}
  honours:
    - {value: "Knight of Obedience, Order of St John (Malta), 14 July 1608 — expelled December 1608", certainty: 0.7, cites: [{source: S4, locator: "Malta — inducted / foul and rotten member"}, {source: S8, locator: "Bulla Receptionis 14 July 1608"}], how_known: "Wikipedia and Mid-Med Bank / UM account of Bulla Receptionis. Institutional honour, not a worldview profession."}
  definition_fit: {value: "clearly meets", rationale: "'His influence on the course of Western art has been immense' (S1).", certainty: 0.7, cites: [{source: S1, locator: "'Becoming Caravaggio'"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Roman Catholic (Lombard Counter-Reformation milieu)", certainty: 0.5, cites: [{source: S4, locator: "Early life — baptism; Borromeo influence noted"}, {source: S1, locator: "'Tragic childhood'"}], how_known: "Baptism in Milan parish; Catholic Lombardy setting. Heritage only — not adult profession."}
  family_religious_practice: {value: UNKNOWN, how_known: "Baptism recorded; household practice not detailed."}
  parents_and_household:
    - {value: "Fermo Merisi, father — household administrator / architect-decorator to the marquess of Caravaggio (S4); Britannica had called him a stonemason (S1); d. 1577 plague", role: father, certainty: 0.5, cites: [{source: S4, locator: "Early life"}, {source: S1, locator: "'Tragic childhood'"}], how_known: "Dual bios disagree on exact trade; death 1577 agreed."}
    - {value: "Lucia Aratori, mother (d. 1584)", role: mother, certainty: 0.7, cites: [{source: S1, locator: "'Tragic childhood'"}, {source: S4, locator: "Early life"}], how_known: "Dual-sourced."}
  household_circumstances: {value: "Artisan / service family; father and most male relatives died of plague in 1577; poverty after", certainty: 0.7, cites: [{source: S1, locator: "'Tragic childhood'"}, {source: S4, locator: "Early life"}], how_known: "Dual-sourced."}
  schooling:
    - {value: "Apprenticeship to Simone Peterzano, Milan (contract 1584; four years)", certainty: 0.7, cites: [{source: S4, locator: "Early life"}, {source: S1, locator: "'Tragic childhood' / Becoming"}], how_known: "Dual-sourced."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Simone Peterzano", role: master painter, certainty: 0.7, cites: [{source: S4, locator: "Early life"}, {source: S1, locator: "text"}], how_known: "Dual-sourced apprenticeship."}
  languages_in_childhood: {value: ["Italian"], certainty: 0.5, cites: [{source: S4, locator: "Milan / Caravaggio"}], how_known: "Inferred Lombard Italian."}
  notable_events:
    - {value: "Plague deaths of father, grandparents and uncle", year: 1577, certainty: 0.7, cites: [{source: S1, locator: "'Tragic childhood'"}, {source: S4, locator: "Early life"}], how_known: "Dual-sourced."}
    - {value: "Baptism, parish of Santo Stefano in Brolo, Milan (certificate found 2007)", year: 1571, certainty: 0.7, cites: [{source: S4, locator: "Early life — baptism certificate"}], how_known: "Wikipedia citing 2007 find; heritage only."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1600", certainty: 0.7, cites: [{source: S3, locator: "para. 2"}], how_known: "Equals timing.major_work_period (Contarelli unveiling)."}
  nominal_affiliations:
    - {value: "Roman Catholic baptism / Counter-Reformation patronage milieu (not a scored confessional profession)", role: member, certainty: 0.5, cites: [{source: S4, locator: "Early life — baptism"}, {source: S1, locator: "church commissions"}], how_known: "Baptized Catholic; worked for church patrons. Prestel (S7): almost no own-voice writings on belief. Not coded as primary_system."}
    - {value: "Order of St John (Knights Hospitaller), Knight of Obedience — admitted 14 July 1608; expelled December 1608 as 'foul and rotten member' (putridum et foetidum)", role: member, certainty: 0.7, cites: [{source: S4, locator: "Malta — inducted / expelled"}, {source: S8, locator: "Bulla Receptionis 14 July 1608"}], how_known: "Documented admission and expulsion. Status / pardon path under Grand Master Wignacourt; standard Order vows are institutional formula, not an own-word creed statement read this pass. Not scored as primary_system CHRIST."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not a scientist; no science–religion remark in own words."}
  primary_system: {value: UNKNOWN, how_known: "No scorable adult profession of CHRIST or any other system in own words. Prestel (S7): other than the September 1603 deposition, almost no quotes or writings in Caravaggio's own voice. Checked and held off-point: (1) Contarelli and other religious canvases — commissions/subjects, not avowed belief (P16; Rembrandt pattern); (2) 1603 Baglione libel deposition — about painters and 'imitar bene le cose naturali', no religious profession (S5, S6, S7); (3) Order of St John knighthood 1608 — institutional honour with standard vows, expelled within months (S4, S8). CHRIST = Catholic baptism / patronage lead only."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Lead only: Catholic baptism (S4), Counter-Reformation church commissions (S1, S3), brief Knight of Obedience in the Order of St John (S4, S8). Not scored — no own-word redeeming/personal God or creed statement; Prestel notes near-total silence in own voice; P16 commissions ≠ belief."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Sources read say nothing on locus of the divine in his own words (P19). Checked off-point: 1603 deposition is about artistic merit and Baglione's Resurrection as painting ('goffa'), not a God-locus profession (S5–S7); religious canvases are commissions/subjects; Order vows unread as personal composition — institutional formula for knighthood. Named alternative if a personal God profession appears in fuller document editions: A 0."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30/P33). No statement of his own on nature's causal order (P16). Trial phrase 'imitar bene le cose naturali' / 'imitate natural things well' (S5, S6, S7) = pictorial mimesis / art-process claim — same pattern as Rembrandt 'naetuereelste beweechgelickheijt', Picasso Zervos 'nature', Michelangelo natura poems. Not B."}
    C_ledger: {value: UNKNOWN, how_known: "No ledger / judgment statement in own words. Order vows of obedience/poverty/chastity are institutional formula, not scored as C."}
    D_authority: {value: UNKNOWN, how_known: "No own-word authority claim read (scripture, Church, reason)."}
    E_scope: {value: UNKNOWN, how_known: "Not a scientist; no statement on same laws everywhere (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "A and B UNKNOWN (P19)."}
  statements:
    - text: "Quella parola valent'huomo presso di me vuol dire che sappi far bene dell'arte sua, cosi in pittura valent'huomo che sappi dipingere bene et imitar bene le cose naturali."
      cites: [{source: S5, locator: "Sgarbi transcription of 13 Sept 1603 interrogation"}, {source: S6, locator: "Friedländer 1955 p. 276 via Jasiński 2022 n.11"}]
      date: "1603-09-13"
      context: "Baglione libel trial, Rome — asked what he means by valent'huomo (worthy man / good painter)."
      axes: [B_cause]
      kind: "other"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Court deposition (kind=other). Art-process claim (paint well and imitate natural things well). Not scored for B under P16. Italian from Sgarbi/Filodiritto; Friedländer locus via Jasiński. EN parallel in Prestel (S7)."
    - text: "I was seized the other day in the Piazza Navona. I do not know why. I am a painter. … By a good man I mean someone who can perform well in his art, and by a good painter a man who can paint well and imitate natural things well. … I do not amuse myself with composing verses, either in Latin or Italian."
      cites: [{source: S7, locator: "Masters of Art: Caravaggio — 1603 deposition EN excerpt"}]
      date: "1603-09-13"
      context: "Same Baglione libel deposition — EN reading copy."
      axes: [B_cause]
      kind: "other"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "EN of the same art-only testimony. Prestel also states that beyond this deposition we have almost no quotes in his own voice. Off-point for A/B religion."
    - text: "Quella pittura della Resurrezione li al Gesù a me non me piace perchè è goffa et l'ho per la peggio che abbia fatta."
      cites: [{source: S5, locator: "Sgarbi — Baglione's Gesù Resurrection criticized"}]
      date: "1603-09-13"
      context: "Same trial — aesthetic judgment on Baglione's Resurrection altarpiece, not a theological claim about the Resurrection."
      axes: [A_locus]
      kind: "other"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Subject is a religious painting; the remark is craft criticism ('clumsy' / worst work). Off-point for A."
  changes_over_life: []
  coder_notes: "Deepen D1 2026-10-24 (queue #147): Open targets from create-pass (1603 libel testimony; Order of St John admission) both read and held off scoring. Do not code CHRIST/A 0 from church commissions, Maltese knighthood, or trial talk about a Resurrection canvas. B permanently likely UNKNOWN unless a nature-causal remark surfaces (trial 'cose naturali' is mimesis). Chart-moving NO. No fallacy_catalog (Jason)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Lombard (Milan / Caravaggio)", certainty: 0.7, cites: [{source: S1, locator: "'Tragic childhood'"}, {source: S4, locator: "Early life"}], how_known: "Dual-sourced."}
  religious_heritage_by_birth: {value: "Roman Catholic", certainty: 0.7, cites: [{source: S4, locator: "Early life — Santo Stefano in Brolo baptism"}], how_known: "Baptism certificate (2007 find) per Wikipedia."}
  baptism_or_initiation: {value: "Baptized, Santo Stefano in Brolo, Milan (certificate found February 2007)", certainty: 0.7, cites: [{source: S4, locator: "Early life"}], how_known: "Wikipedia. Heritage only — not adult worldview code."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not read; Borromeo Counter-Reformation influence on imagery is art-historical, not catechism evidence."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1600", certainty: 0.7, cites: [{source: S1, locator: "'Rome: 1599–1606' (body)"}, {source: S3, locator: "para. 2"}], how_known: "The one lasting work named in the body read, the Contarelli canvases, dated by their unveiling in 1600 (S3; RQ-Z7-N1, P30 #1; P29)."}
  age_at_first_lasting_contribution: {value: 29, certainty: 0.7, cites: [{source: S1, locator: "Born"}, {source: S3, locator: "para. 2"}], how_known: "1600 − 1571 = 29 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "1603 deposition checked and left off-point; no LIO-scorable statement."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S5, locator: "1603 deposition"}, {source: S7, locator: "almost no own voice"}], how_known: "Own words in/near working years checked; none score A/B."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Axes UNKNOWN."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "Strong chiaroscuro / tenebrism and staged multi-figure compositions (Contarelli, Cerasi) — pictorial structure present; not High Renaissance Euclidean ideal (S1, S3, S4).", certainty: 0.5, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "essay"}, {source: S4, locator: "As an artist"}], how_known: "Coder's reading of dual bio + Met essay."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Not tested for H1."}
  circle_present: {value: "unclear", rationale: "No worldview statement that would feed H1 circle.", certainty: 0.5, cites: [{source: S5, locator: "deposition checked"}], how_known: "Coder's reading."}
  reading: "Lane B only: pictorial form partly present (chiaroscuro); no H1 circle from worldview. 'Imitar bene le cose naturali' is art technique, not Lane A B_cause. Religious subject matter ≠ CHRIST worldview."
  notes: "Do not treat Contarelli / Maltese altarpieces or Order knighthood as CHRIST primary_system."

institutions:
  - {value: "Order of St John (Knights Hospitaller), Malta — Knight of Obedience 14 July–December 1608", role: member, kind: "other", certainty: 0.7, cites: [{source: S4, locator: "Malta"}, {source: S8, locator: "Bulla Receptionis"}], how_known: "Admitted then expelled; institutional, not creed score."}
  - {value: "Contarelli Chapel / San Luigi dei Francesi (church commission)", role: painter, kind: "patron or funder", certainty: 0.7, cites: [{source: S1, locator: "'Rome: 1599–1606'"}, {source: S3, locator: "para. 2"}], how_known: "Contract 1599; unveiling 1600."}
collaborators:
  - {value: "Costanza Colonna", relation: other, note: "patron; refuge and protection; family ties to Caravaggio town / Knights", certainty: 0.7, cites: [{source: S1, locator: "'Tragic childhood'"}, {source: S4, locator: "Malta — Fabrizio Sforza Colonna"}], how_known: "Dual-sourced."}
  - {value: "Cardinal Francesco Maria del Monte", relation: other, note: "early Roman patron; aided after 1603 sentence", certainty: 0.7, cites: [{source: S7, locator: "lenient sentence / del Monte"}, {source: S4, locator: "Beginnings in Rome"}], how_known: "Prestel and Wikipedia."}
  - {value: "Alof de Wignacourt", relation: other, note: "Grand Master; inducted Caravaggio as knight", certainty: 0.7, cites: [{source: S4, locator: "Malta"}, {source: S8, locator: "admission"}], how_known: "Dual-sourced."}
  - {value: "Simone Peterzano", relation: teacher, certainty: 0.7, cites: [{source: S4, locator: "Early life"}, {source: S1, locator: "text"}], how_known: "Dual-sourced."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 153"}], how_known: "Study roster."}
  controversies:
    - {value: "Sexuality and model relationships are heavily debated in secondary literature; not used for worldview coding.", certainty: 0.5, cites: [{source: S4, locator: "Sexuality"}], how_known: "Wikipedia section flagged; left unused for LIO."}
  data_quality_flags:
    - "Almost no own-voice text survives beyond the 1603 Baglione deposition (S7 Prestel)."
    - "Britannica Graham-Dixon live Cloudflare-blocked 2026-10-24; retained from original collect + audit reads."
    - "Friedländer Caravaggio Studies (1955) IA borrow-restricted; Italian deposition via Sgarbi/Filodiritto and Friedländer locus via Jasiński 2022."
    - "Order vow formula text unread as Caravaggio's personal composition — institutional statutes only."
  open_questions:
    - "Full Friedländer Documents appendix / Hibbard appendices Italian+EN of all process depositions."
    - "Latin text of Bulla Receptionis and any personally spoken vow wording beyond Order statute formula."
    - "Any letter or reported speech with a non-commission locus claim (unlikely per Prestel)."
    - "Britannica Graham-Dixon religion/Malta body when Cloudflare unblocked."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Andrew Graham-Dixon"
    citation: "Graham-Dixon, Andrew. \"Caravaggio.\" Encyclopaedia Britannica (updated 20 September 2026). https://www.britannica.com/biography/Caravaggio"
    url: "https://www.britannica.com/biography/Caravaggio"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Signed article; body cited from original collect and Z5/Z7 audit reads. Live 2026-10-24 Cloudflare-blocked; Top Questions not cited alone (P26)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, collaborators]
  - id: S2
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [review]
  - id: S3
    type: secondary
    kind: "other"
    author: "Keith Christiansen"
    citation: "Christiansen, Keith. 'Caravaggio (Michelangelo Merisi) (1571–1610) and His Followers.' October 2003. Heilbrunn Timeline of Art History, The Metropolitan Museum of Art. Archived 2017-12-19: https://web.archive.org/web/20171219134404/http://www.metmuseum.org/toah/hd/crvg/hd_crvg.htm"
    url: "https://web.archive.org/web/20171219134404/http://www.metmuseum.org/toah/hd/crvg/hd_crvg.htm"
    accessed: 2026-10-19
    source_quality: "reference entry"
    reliability_note: "Signed museum reference essay (Keith Christiansen, October 2003); the archived page was read (Z8 audit) and says the canvases 'were unveiled in 1600, and established his reputation'."
    used_for: [basics, contribution, worldview, timing, lane_b]
  - id: S4
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Caravaggio.\" https://en.wikipedia.org/wiki/Caravaggio (sections: Early life; Malta; Death; Primary sources). Wikitext fetched 2026-10-24."
    url: "https://en.wikipedia.org/wiki/Caravaggio"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Dual-source bio with S1 (P50). Used for baptism certificate find, Malta induction/expulsion, career geography. Not used alone for worldview scores."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators, review]
  - id: S5
    type: primary
    kind: "other"
    author: "Michelangelo Merisi da Caravaggio (deposition); Vittorio Sgarbi (transcription quoted)"
    citation: "Filodiritto. 'Caravaggio (1571-1610): Un interrogatorio provvidenziale' — Italian transcription of 13 September 1603 Baglione-trial interrogation, quoting Vittorio Sgarbi, Caravaggio (Skira, 2005), p. 17. https://www.filodiritto.com/caravaggio-1571-1610-un-interrogatorio-provvidenziale"
    url: "https://www.filodiritto.com/caravaggio-1571-1610-un-interrogatorio-provvidenziale"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Web reprint of Sgarbi's Italian of the process deposition; cross-checked against Friedländer locus in S6 and EN in S7. Own voice on painting only."
    used_for: [worldview, languages_of_work]
  - id: S6
    type: secondary
    kind: "journal article"
    author: "Mateusz Jasiński"
    citation: "Jasiński, Mateusz. 'Imitar bene le cose naturali According to Caravaggio and the Caravaggisti.' Rocznik Muzeum Narodowego w Warszawie. Nowa Seria / Journal of the National Museum in Warsaw. New Series 11(47) (2022): cites Walter Friedländer, Caravaggio Studies (Princeton, 1955), p. 276 for the Italian valent'huomo / imitar bene le cose naturali line. https://rocznik.mnw.art.pl/ojs/index.php/rm/article/download/23/57/83"
    url: "https://rocznik.mnw.art.pl/ojs/index.php/rm/article/download/23/57/83"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Peer-reviewed museum journal; used for Friedländer 1955 p. 276 citation of the deposition Italian (Friedländer IA borrow-restricted this pass)."
    used_for: [worldview]
  - id: S7
    type: secondary
    kind: "other"
    author: "Prestel / Masters of Art series (Caravaggio excerpt)"
    citation: "Masters of Art: Caravaggio (Prestel) — publisher leseprobe PDF with EN of the 1603 deposition and note that beyond that deposition 'we have almost no quotes or writings of any kind in Caravaggio's own voice.' https://prestelpublishing.penguinrandomhouse.de/leseprobe/Masters-of-Art-Caravaggio/leseprobe_9783791391625.pdf"
    url: "https://prestelpublishing.penguinrandomhouse.de/leseprobe/Masters-of-Art-Caravaggio/leseprobe_9783791391625.pdf"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Publisher sample PDF; EN deposition + explicit near-silence claim. Not used alone for bio facts."
    used_for: [worldview, collaborators, review]
  - id: S8
    type: secondary
    kind: "other"
    author: "Mid-Med Bank Limited / University of Malta OAR reprint"
    citation: "Mid-Med Bank Limited Report and Accounts 1986 — 'Caravaggio in Malta' (Bulla Receptionis 14 July 1608; Knight of Obedience; Beheading as passaggio). OAR@UM bitstream. https://www.um.edu.mt/library/oar/bitstream/123456789/103777/1/Mid-Med%20Bank%20Limited%20Report%20and%20Accounts%201986_Caravaggio%20in%20Malta.pdf"
    url: "https://www.um.edu.mt/library/oar/bitstream/123456789/103777/1/Mid-Med%20Bank%20Limited%20Report%20and%20Accounts%201986_Caravaggio%20in%20Malta.pdf"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Bank annual-report essay on Malta documents; used for Bulla Receptionis date and knighthood mechanics. Cross-checked with Wikipedia Malta section (S4). Not a creed profession."
    used_for: [contribution, worldview, institutions, collaborators]
---

## Summary

Caravaggio (1571–1610), Italian Baroque painter [S1; S4]. Deepen D1: primary_system UNKNOWN (CHRIST lead only); A UNKNOWN; B UNKNOWN (P16); C–E UNKNOWN; mid_basin UNKNOWN. Chart-moving NO (still unplottable). Not a scientist.

## Life and work

Born Milan (baptized Santo Stefano in Brolo); raised between Milan and Caravaggio after 1576 plague [S4; S1]. Rome fame from Contarelli Chapel unveiling 1600 [S1; S3]. Malta: Knight of Obedience 14 July 1608, expelled December 1608 [S4; S8]. Died Porto Ercole 1610 [S1; S4].

## Contribution and impact

Contarelli canvases established him as Rome's most dynamic painter [S1; S3]. Chiaroscuro / tenebrism shaped Caravaggisti, Rembrandt, Velázquez [S1; S4].

## Childhood and education

Apprenticed to Simone Peterzano (1584) [S4; S1]. Father and male kin died in 1577 plague [S1; S4].

## Adult working worldview

Almost no own voice survives beyond the 13 September 1603 Baglione libel deposition [S7]. That testimony defines a good painter as one who paints well and imitates natural things well — art mimesis, not nature's causal order (P16) and not a God-locus claim [S5; S6; S7]. Religious commissions and brief Maltese knighthood are work / institutional status, not scored CHRIST profession [P16]. All LIO axes UNKNOWN; mid_basin UNKNOWN.

## Heritage (context only)

Lombard; Roman Catholic baptism [S4]. Heritage ≠ adult worldview code.

## Timing

1600 Contarelli unveiling, age 29 [S1; S3]. No LIO-type views found relative to major work.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Pictorial form partly present (chiaroscuro); no H1 circle. Form ≠ A/B score. 'Cose naturali' = art technique [S5; S6].

## Open questions

- Full Friedländer / Hibbard document appendices.
- Bulla Receptionis Latin and any personally spoken vow wording.
- Any letter with a locus claim (unlikely per Prestel S7).

## Research log

- 2026-10-19: Read Britannica (Graham-Dixon), first sections.
- 2026-10-19 (Z5 audit fix): read the body section 'Rome: 1599–1606'; question-box and caption lasting cites removed.
- 2026-10-19 (Z7): Contarelli dated by 1600 unveiling (S3); span/age/era corrected.
- 2026-10-24 (Deepen D1): 1603 deposition Italian+EN (S5–S7); Order of St John Bulla/expulsion (S4, S8); Wikipedia dual bio (S4); held UNKNOWN; P47 on S1–S8; no fallacy_catalog; no figures/.
