---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA2; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to visual_arts. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #175, F 3, rank 186). Goals: RA perspective lectures / Fallacies of Hope own words if any; keep silence if none; do not force plot. Hunt: Tate chronology baptism St Paul's Covent Garden 14 May 1775 and burial St Paul's Cathedral 30 Dec 1851 (S5); Tate Imms Colour Studies citing Ruskin Fors Clavigera Letter 45 (1874) for reported 'The Sun is God' a few weeks before death, with Eastlake/Bartlett sun-on-face death reports that do not carry the phrase (S6); MFA Boston Slave Ship entry with RA 1840 Fallacies of Hope catalogue verse (S7); lecture clause 'Light is therefore colour, and shadow the privation of it' (c.1818 lecture material; pedagogy/optics, not creed) via Bank of England / Gage chain (S8); Independent review of Hamilton 1997 and Bailey 1997 on Son/sun ambiguity and Ruskin invention claim (S9). primary BELOW_THRESHOLD (CHRIST lead from Anglican baptism/burial + biblical painting subjects only; PANT rejected — landscape/sun subjects fail S6 two-part test; 'sun is God' reported-speech lead of doubtful provenance). A BELOW_THRESHOLD (no own locus; named reading A 2 if Ruskin phrase authenticated as God=sun). B UNKNOWN (not a scientist; Fallacies storm/sun verse is subject/poetry, not law/exception — P16). C/D/E UNKNOWN; mid UNKNOWN (B UNKNOWN takes precedence, P19). Chart: still unplotted. P47 source_quality on S1–S9. No fallacy_catalog; no figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Correction found while coding AA4: region_of_birth and region_of_work are Northern Europe, not Western Europe; the United Kingdom is M49 Northern Europe (P3, data/reference/regions.csv)."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "AA3 audit fix: the Tate (Wilton) and National Gallery (Egerton) entries were fetched and read in full on 2026-10-19 and are relabelled 'read in full'."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "AA2 audit fix: the span ends are now dated by exhibition, The Shipwreck at Turner's gallery in 1805 (Tate, S2) and Rain, Steam, and Speed at the RA in 1844 (Egerton, National Gallery, S3), so first-lasting year, span, working_years and age rise from 0.5 to 0.7. Not plotted."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA2, order P32: F 3, rank 186). Source: Britannica, signed by Martin R. F. Butlin (scholars edition, read in full). Lasting claim: 'perhaps the greatest landscapist of the 19th century ... a pioneer in the study of light, color, and atmosphere' (Legacy), a body of work. Span: from The Shipwreck and the Thames sketches of 1805, when he 'was developing his original approach to landscape', to Rain, Steam, and Speed (1844), the last dated work Britannica names among the 'outstanding examples of his late work'; dates as Britannica gives them. No religious statement read: worldview all UNKNOWN; not a scientist. Span 1805–1844, age 30. Not plotted. Draft, not reviewed."}

identity:
  id: turner-j-m-w
  display_name: "J.M.W. Turner"
  roster:
    canonical_name: "J.M.W. Turner"
    rank: 186
    F: 3
    models: [Claude, Gemini, Grok]
    band: "core (3–4)"
    status: "core"
    field: "art"
    field_bucket: "arts"
  full_name: {value: "Joseph Mallord William Turner", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  native_name: {value: "Joseph Mallord William Turner", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  aliases:
    - {name: "J-M-W Turner", kind: "roster alias"}
    - {name: "Turner-J-M-W", kind: "roster alias"}

basics:
  birth:
    date: {value: "1775-04-23", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S5, locator: "1775"}], how_known: "Britannica; Tate chronology (traditional date)."}
    place: {value: "London", modern_name: "London, United Kingdom", polity_then: "Kingdom of Great Britain", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S5, locator: "1775, 21 Maiden Lane"}], how_known: "Britannica; Tate."}
  death:
    date: {value: "1851-12-19", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S5, locator: "1851, 19 December"}], how_known: "Britannica; Tate chronology."}
    place: {value: "Chelsea, London", modern_name: "London, United Kingdom", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "Later life and works"}, {source: S5, locator: "1851, Davis Place"}], how_known: "Britannica; Tate."}
  first_lasting_contribution_year: {value: 1805, certainty: 0.7, cites: [{source: S1, locator: "Early life and works"}, {source: S2, locator: "Study for 'The Shipwreck'"}], how_known: "'The Shipwreck (1805) suggests that at this time Turner was developing his original approach to landscape' (S1); Tate: 'The painting The Shipwreck was exhibited in Turner's own gallery in 1805' (S2); exhibition is the P30 #1 dating event."}
  era_bucket: {value: "1750 to 1849", certainty: 0.7, cites: [{source: S1, locator: "Early life and works; Later life and works"}], how_known: "1805–1844, one bucket (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "United Kingdom (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "London; tours of Britain and the Continent."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "Middle years"}], how_known: "Titles and appended verse in English."}
  occupations: {value: ["painter", "printmaker"], certainty: 0.7, cites: [{source: S1, locator: "Introduction; Liber Studiorum"}], how_known: "Britannica."}

contribution:
  primary_domain: visual_arts
  fields: {value: ["painting"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Landscape painting as the study of light, colour and atmosphere (body of work, 1805–1844)", year: 1805, kind: "body of work", lasting: "'perhaps the greatest landscapist of the 19th century ... a pioneer in the study of light, color, and atmosphere'; 'one of the most innovative and technically gifted painters of his century' (S1, Legacy)", certainty: 0.7, cites: [{source: S1, locator: "Legacy; Early life and works; Later life and works"}], how_known: "Britannica (Butlin); span from The Shipwreck (exhibited 1805, S2) to Rain, Steam, and Speed (exhibited 1844, S3)."}
  evidence_of_impact:
    - {value: "Ruskin's Modern Painters (1843) written to prove his superiority; the Turner Bequest", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Legacy; Later life and works"}], how_known: "Britannica."}
  major_works:
    - {value: "The Fighting Temeraire", year: 1839, kind: "artwork", certainty: 0.7, cites: [{source: S1, locator: "Later life and works"}], how_known: "Britannica: dated (1839)."}
    - {value: "Rain, Steam, and Speed—the Great Western Railway", year: 1844, kind: "artwork", certainty: 0.7, cites: [{source: S1, locator: "Later life and works"}, {source: S3, locator: "Exhibited"}], how_known: "Exhibited RA 1844 (62) (S3); end of the body-of-work span."}
    - {value: "Liber Studiorum", year: 1807, kind: "artwork", certainty: 0.7, cites: [{source: S1, locator: "Early life and works"}], how_known: "Britannica: first part June 1807, abandoned 1819 after 71 plates."}
    - {value: "Slave Ship (Slavers Throwing Overboard the Dead and Dying, Typhoon Coming On)", year: 1840, kind: "artwork", certainty: 0.7, cites: [{source: S7, locator: "title; Exhibited RA 1840"}], how_known: "MFA Boston; Fallacies of Hope catalogue verse paired at RA 1840."}
  honours:
    - {value: "Full member of the Royal Academy", year: 1802, kind: "membership", certainty: 0.7, cites: [{source: S1, locator: "Early life and works"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "Perhaps the greatest landscapist of the 19th century (S1).", certainty: 0.7, cites: [{source: S1, locator: "Legacy"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Church of England (Anglican) by baptismal practice", certainty: 0.7, cites: [{source: S5, locator: "14 May 1775 baptised at St Paul's, Covent Garden"}], how_known: "Parish baptism at a Church of England church (heritage only)."}
  family_religious_practice: {value: UNKNOWN, how_known: "Baptism recorded; degree of household practice not stated in sources read."}
  parents_and_household:
    - {value: "Son of a barber; mother later committed to a mental hospital", role: "family", certainty: 0.7, cites: [{source: S1, locator: "Early life and works"}], how_known: "Britannica."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Royal Academy schools, from 1789", certainty: 0.7, cites: [{source: S1, locator: "Early life and works"}, {source: S5, locator: "1789, 11 December"}], how_known: "Britannica; Tate chronology."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events:
    - {value: "Baptised 14 May 1775 at St Paul's, Covent Garden", certainty: 0.7, cites: [{source: S5, locator: "1775, 14 May"}], how_known: "Tate chronology."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1805–1844", certainty: 0.7, cites: [{source: S1, locator: "Early life and works; Later life and works"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Baptised Church of England (St Paul's, Covent Garden, 1775); buried in the crypt of St Paul's Cathedral (1851)", certainty: 0.7, cites: [{source: S5, locator: "1775 baptism; 1851, 30 December burial"}], how_known: "Tate chronology. Heritage / institutional burial (RA notables) ≠ adult CHRIST creed."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not a scientist; no science–religion statement read."}
  primary_system:
    value: BELOW_THRESHOLD
    how_known: "Own public words opened: RA Fallacies of Hope catalogue verse with Slave Ship (1840) names storm, sun, chains and 'fallacious Hope' / market — moral-poetic framing, not a creed (S7). Perspective-lecture clause 'Light is therefore colour…' is optics/pedagogy (S8). Biblical painting subjects (e.g. Light and Colour … Moses Writing the Book of Genesis, 1843) are subjects, not profession (P16). Reported last words 'The Sun is God' (Ruskin Fors Clavigera 1874 via Tate S6) remain a lead of doubtful provenance (Bailey rejects; Hamilton notes Son/sun ambiguity; Hunter 2024 'mythical dying words'). Lead CHRIST from Anglican baptism/burial and biblical subjects only — insufficient for scored CHRIST. PANT fails S6 two-part test (no God–Nature identity claim in own writing). Do not force open primary."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Lead only: C of E baptism (S5); burial St Paul's Cathedral (S5); biblical titles/subjects in late oils. Heritage and painting subjects ≠ adult doctrine (CHRIST.md membership ≠ ideology; P16)."}
    - {code: PANT, reason: "Rejected: sun/landscape power and Ruskin's 'Sun-worshipper' gloss do not pass the two-part PANT test (own writing identifying God with Nature as what exists + a mark beyond feeling). Nature-power in paintings is subject, not profession (P16)."}
    - {code: ATHE, reason: "Rejected: no denial of God; Fallacies hope-critique is not atheism."}
  lio_axes:
    A_locus:
      value: BELOW_THRESHOLD
      how_known: "No first-person locus statement in lectures or Fallacies catalogue verse. Ruskin's reported 'The Sun is God' (S6) would, if authenticated as identifying God with the sun, suggest A 2 — but it is reported speech of doubtful provenance and cannot score an axis alone (§7). Named reading A 2 does not reach 0.5. Do not force open A."
      alternatives:
        - {value: 2, note: "If Ruskin's 'The Sun is God' were authenticated as Turner's claim that God is the sun / Nature — still reported speech; Bailey/Hamilton/Gage/Hunter dispute the chain.", cites: [{source: S6, locator: "Ruskin Fors Clavigera Letter 45 (1874)"}]}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30). Fallacies 'angry setting sun' / typhoon verse and landscape subjects dramatise nature's power; they do not state law vs exception about nature's order (P16). Do not invent B from sun imagery or RA perspective optics."}
    C_ledger: {value: UNKNOWN, how_known: "Fallacies hope-as-fallacy is ethical-literary, not a scored afterlife/reward ledger."}
    D_authority: {value: UNKNOWN, how_known: "Not scored."}
    E_scope: {value: UNKNOWN, how_known: "Not scored."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN, which takes precedence (§6, P19); A_locus is BELOW_THRESHOLD. Do not force plot without B."}
  statements:
    - text: "Aloft all hands, strike the top-masts and belay; Yon angry setting sun and fierce-edged clouds Declare the Typhon's coming. Before it sweeps your decks, throw overboard The dead and dying - ne'er heed their chains Hope, Hope, fallacious Hope! Where is thy market now?"
      cites: [{source: S7, locator: "RA 1840 catalogue extract from Fallacies of Hope (1812)"}]
      date: "1840"
      context: "Royal Academy exhibition catalogue paired with Slave Ship (Slavers Throwing Overboard the Dead and Dying, Typhoon Coming On). In-span (1840 within 1805–1844)."
      axes: []
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "MFA Boston quotes the RA catalogue extract; Finberg 1961 p.474 cited there for fuller verse corpus. Moral-poetic / market indictment — not a creed or B law-statement. Axes left empty (P16: nature-power as subject)."
    - text: "Light is therefore colour, and shadow the privation of it."
      cites: [{source: S8, locator: "RA perspective lecture material, associated with 1818"}]
      date: "1818"
      context: "Royal Academy Professor of Perspective lecture papers (British Library Add MS 46151 tradition); in-span pedagogy on light/colour."
      axes: []
      kind: "unpublished manuscript"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Secure lecture wording per Gage Colour in Turner / Bank of England £20 note documentation chain (S8). Optics and pictorial instruction — not a religious profession. Primary check of BL lecture MS pending."
    - text: "\"The Sun is God,\" said Turner, a few weeks before he died with the setting sun on his face. He meant it, as Zoroaster meant it; and was a Sun-worshipper of the old breed."
      cites: [{source: S6, locator: "Ruskin, Fors Clavigera Letter 45 (September 1874), Library Edition XXVIII p.147, as quoted by Imms"}]
      date: "1874"
      context: "Ruskin's report, published decades after Turner's death (1851); not a bedside diary. Eastlake (1852) and Bartlett (to Ruskin, 1857) report sun on Turner's face at death without the phrase."
      axes: []
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Lead only. Tate documents the chain and its limits. Independent (S9): Bailey discounts / claims Ruskin invention; Hamilton allows Son/sun ambiguity. Cannot score A or primary (§7 reported speech)."
  changes_over_life:
    - {value: "Public Fallacies of Hope catalogue verses from 1812 (Hannibal) through Slave Ship (1840) and late Deluge pair (1843): hope as fallacy; biblical narrative subjects recur. No creed shift documented in own words. Reported 'Sun is God' is posthumous Ruskin lore, not a dated life-change.", year: 1840, certainty: 0.5, cites: [{source: S7, locator: "1840 verse"}, {source: S6, locator: "Ruskin 1874"}, {source: S5, locator: "chronology 1812 Fallacies"}], how_known: "Catalogue practice across the span; last-words lore after death."}
  coder_notes: "Deepen D1 (#175): lectures give optics ('Light is therefore colour'), not God; Fallacies Slave Ship verse is own public words but not a locus/creed; 'sun is God' stays lead. primary/A BELOW; B UNKNOWN; mid UNKNOWN; chart NO. Blockers: BL lecture MS / Gage monograph pages; Finberg 1961 verse corpus; Hamilton 1997 print pages; any authenticated own-words God statement. Do not touch figures/. No fallacy_catalog."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated beyond English London birth."}
  religious_heritage_by_birth: {value: "Church of England (Anglican)", certainty: 0.7, cites: [{source: S5, locator: "baptised at St Paul's, Covent Garden"}], how_known: "Parish baptism. Heritage ≠ worldview code."}
  baptism_or_initiation: {value: "Baptised 14 May 1775 at St Paul's, Covent Garden", certainty: 0.7, cites: [{source: S5, locator: "1775, 14 May"}], how_known: "Tate chronology (parish register not imaged this pass)."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1805–1844", certainty: 0.7, cites: [{source: S1, locator: "Early life and works; Later life and works"}], how_known: "Body of work from The Shipwreck (exhibited 1805, S2) to Rain, Steam, and Speed (exhibited RA 1844, S3) (P29, P31, P30 #1)."}
  age_at_first_lasting_contribution: {value: 30, certainty: 0.7, cites: [{source: S1, locator: "Introduction; Early life and works"}], how_known: "1805 − 1775 = 30 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: "BELOW_THRESHOLD — Fallacies catalogue verse 1840 is own words but not a locus/creed statement; Ruskin's 'Sun is God' is posthumous reported speech", certainty: 0.5, cites: [{source: S7, locator: "1840"}, {source: S6, locator: "Ruskin 1874"}], how_known: "Own public verse opened; no scorable LIO profession."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.5, cites: [{source: S7, locator: "1840"}, {source: S5, locator: "1812 Fallacies"}], how_known: "Fallacies practice from 1812; Slave Ship verse 1840 in span — still below A/primary scoring threshold."}
  worldview_during_major_work: {value: "BELOW_THRESHOLD for primary and A; B UNKNOWN. Landscape/sun subjects and Fallacies hope-verse do not open a system. Reported sun-is-God lore is after death.", certainty: 0.5, cites: [{source: S7, locator: "1840 verse"}, {source: S6, locator: "Ruskin"}, {source: S1, locator: "power of nature as subject"}], how_known: "Deepen D1 reading."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Colour and atmosphere over drawn structure (S1); he was professor of perspective (1807) but lasting work is atmospheric.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed; do not infer pantheist circle from sun subjects.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No Lane B data. Do not invent B from light/colour lectures or storm subjects."
  notes: "Lane B is labeled belief, not a finding."

institutions:
  - {value: "Royal Academy of Arts", role: "member; professor of perspective 1807–1837/38", years: "1799–1851", kind: "academy or learned society", certainty: 0.7, cites: [{source: S1, locator: "Early life and works; Later life and works"}, {source: S5, locator: "1807 Professor; 1837 resigns"}], how_known: "Britannica; Tate chronology (associate 1799, full 1802; resigns professorship 28 Dec 1837)."}
collaborators:
  - {value: "John Ruskin", relation: "rival or critic", note: "Modern Painters (1843); later reported the 'Sun is God' remark", certainty: 0.7, cites: [{source: S1, locator: "Legacy"}, {source: S6, locator: "Ruskin"}], how_known: "Britannica; Tate."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 186"}], how_known: "Study roster."}
  controversies:
    - {value: "Reported last words 'The Sun is God' — Ruskin 1874; disputed provenance (Bailey; Hamilton Son/sun; Gage/Hunter mythical)", certainty: 0.5, cites: [{source: S6, locator: "Imms summary"}, {source: S9, locator: "Bailey vs Hamilton"}], how_known: "Tate + Independent review of 1997 biographies."}
  data_quality_flags:
    - "No authenticated own-words creed or A-locus statement."
    - "Fallacies of Hope complete MS not found; catalogue extracts only."
  open_questions:
    - "Any authenticated first-person statement locating or denying God (would open A / possibly primary)."
    - "BL Add MS 46151 lecture papers / Gage Colour in Turner for fuller lecture wording beyond the light/colour clause."
    - "Hamilton 1997 print pages on religion; Finberg 1961 Fallacies corpus."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Martin R. F. Butlin"
    citation: "Butlin, Martin R. F. 'J.M.W. Turner.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/JMW-Turner/73869"
    url: "https://kids.britannica.com/scholars/article/JMW-Turner/73869"
    accessed: 2026-10-19
    reliability_note: "Signed article, read in full."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, lane_b, institutions]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "Tate"
    citation: "'Study for The Shipwreck', c.1799–1805, in J.M.W. Turner: Sketchbooks, Drawings and Watercolours, Tate Research Publication. https://www.tate.org.uk/art/research-publications/jmw-turner/joseph-mallord-william-turner-study-for-the-shipwreck-r1178107"
    url: "https://www.tate.org.uk/art/research-publications/jmw-turner/joseph-mallord-william-turner-study-for-the-shipwreck-r1178107"
    accessed: 2026-10-19
    reliability_note: "Signed museum catalogue entry (Andrew Wilton, May 2013), read in full: 'The painting The Shipwreck was exhibited in Turner's own gallery in 1805'."
    source_quality: "other"
    used_for: [basics, timing]
  - id: S3
    type: secondary
    kind: "institutional page"
    author: "Judy Egerton"
    citation: "Egerton, Judy. 'Rain, Steam, and Speed – The Great Western Railway.' The British Paintings (National Gallery, 2000), online catalogue. https://www.nationalgallery.org.uk/paintings/catalogues/egerton-2000/rain-steam-and-speed-the-great-western-railway"
    url: "https://www.nationalgallery.org.uk/paintings/catalogues/egerton-2000/rain-steam-and-speed-the-great-western-railway"
    accessed: 2026-10-19
    reliability_note: "Signed museum catalogue entry, read in full: 'Exhibited RA 1844 (62)'."
    source_quality: "other"
    used_for: [contribution, timing]
  - id: S4
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [review]
  - id: S5
    type: secondary
    kind: "institutional page"
    author: "David Blayney Brown"
    citation: "Brown, David Blayney. 'Chronology', December 2012, in J.M.W. Turner: Sketchbooks, Drawings and Watercolours, Tate Research Publication. https://www.tate.org.uk/art/research-publications/jmw-turner/chronology-r1109229"
    url: "https://www.tate.org.uk/art/research-publications/jmw-turner/chronology-r1109229"
    accessed: 2026-10-24
    reliability_note: "Signed Tate Research chronology, read in full this pass: baptism 14 May 1775 St Paul's Covent Garden; burial 30 Dec 1851 St Paul's Cathedral crypt; Professor of Perspective; Fallacies first extract 1812."
    source_quality: "other"
    used_for: [basics, childhood, heritage, worldview, institutions, timing]
  - id: S6
    type: secondary
    kind: "institutional page"
    author: "Matthew Imms"
    citation: "Imms, Matthew. 'Colour Studies of the Sun and Clouds at Dawn and Sunset c.1815–40', March 2016, in J.M.W. Turner: Sketchbooks, Drawings and Watercolours, Tate Research Publication (November 2016). https://www.tate.org.uk/art/research-publications/jmw-turner/colour-studies-of-the-sun-and-clouds-at-dawn-and-sunset-r1183166"
    url: "https://www.tate.org.uk/art/research-publications/jmw-turner/colour-studies-of-the-sun-and-clouds-at-dawn-and-sunset-r1183166"
    accessed: 2026-10-24
    reliability_note: "Signed Tate Research subset essay, read in full: quotes Ruskin 1853 sun-on-face account and Fors Clavigera Letter 45 (1874) 'The Sun is God… Sun-worshipper'; also Eastlake 1852 and Bartlett 1857 sun-at-death reports without the phrase."
    source_quality: "scholarly reconstruction"
    used_for: [worldview, review]
  - id: S7
    type: secondary
    kind: "institutional page"
    author: "Museum of Fine Arts, Boston"
    citation: "Museum of Fine Arts, Boston. 'Slave Ship (Slavers Throwing Overboard the Dead and Dying, Typhoon Coming On)', accession 99.22. https://collections.mfa.org/objects/31102"
    url: "https://collections.mfa.org/objects/31102"
    accessed: 2026-10-24
    reliability_note: "Museum collection entry quoting the RA 1840 Fallacies of Hope catalogue extract in full; points to Finberg 1961 p.474 for fuller verse."
    source_quality: "other"
    used_for: [contribution, worldview, timing]
  - id: S8
    type: secondary
    kind: "other"
    author: "Bank of England; John Gage (via secondary chain)"
    citation: "Bank of England, 'Light is therefore colour' (Governor remarks at polymer £20 launch, 10 October 2019), documenting the lecture clause; wording tradition in Gage, Colour in Turner: Poetry and Truth (1969), as summarised in TheHistoryOfArt.org Turner quotes dossier (Tom Gurney, updated 2026). https://www.bankofengland.co.uk/-/media/boe/files/speech/2019/light-is-therefore-colour-governor-remarks-at-the-new-20-launch.pdf"
    url: "https://www.bankofengland.co.uk/-/media/boe/files/speech/2019/light-is-therefore-colour-governor-remarks-at-the-new-20-launch.pdf"
    accessed: 2026-10-24
    reliability_note: "Lecture clause is the secure wording used on the £20 note; full Gage monograph / BL Add MS 46151 not opened this pass (secondary quotation; primary check pending)."
    source_quality: "unofficial web copy"
    used_for: [worldview]
  - id: S9
    type: secondary
    kind: "other"
    author: "The Independent (review of Hamilton 1997 and Bailey 1997)"
    citation: "'The two Turners', The Independent, review discussing James Hamilton, Turner: A Life (1997) and Anthony Bailey, Standing in the Sun (1997) on the deathbed 'sun is God' / Son ambiguity. https://www.independent.co.uk/arts-entertainment/the-two-turners-1258732.html"
    url: "https://www.independent.co.uk/arts-entertainment/the-two-turners-1258732.html"
    accessed: 2026-10-24
    reliability_note: "Newspaper review of two biographies; used only for the Hamilton Son/sun caveat and Bailey's rejection of the Ruskin anecdote — not as a primary of Turner's words. Hamilton 1997 print unread this pass."
    source_quality: "newspaper interview"
    used_for: [worldview, review]
---

## Summary

J.M.W. Turner (1775–1851), English landscape painter, pioneer of light, colour and atmosphere [S1]. Baptised Anglican (1775); buried St Paul's Cathedral (1851) [S5]. Deepen D1: primary_system BELOW_THRESHOLD (CHRIST lead only; PANT rejected; 'sun is God' doubtful reported speech); A BELOW_THRESHOLD; B UNKNOWN; mid_basin UNKNOWN — still unplotted.

## Life and work

London birth; RA schools from 1789; Professor of Perspective 1807–1837; tours of Britain and the Continent [S1][S5].

## Contribution and impact

Light, colour and atmosphere, body of work 1805–1844; Ruskin's Modern Painters; Turner Bequest [S1]. Slave Ship (1840) with Fallacies of Hope catalogue verse [S7].

## Childhood and education

Barber's son; baptised St Paul's Covent Garden 14 May 1775; RA schools [S1][S5].

## Adult working worldview

Own public words: Fallacies of Hope catalogue verse (Slave Ship, 1840) — storm, sun, fallacious hope, market; not a creed [S7]. Lecture clause 'Light is therefore colour…' — optics/pedagogy [S8]. Biblical painting subjects are subjects, not profession (P16). Reported 'The Sun is God' (Ruskin 1874) is a lead of doubtful provenance [S6][S9]. Lead CHRIST (baptism/burial/subjects); PANT fails the two-part test. A BELOW; B UNKNOWN; mid UNKNOWN.

## Heritage (context only)

Church of England baptism; St Paul's Cathedral burial. Heritage ≠ code [S5].

## Timing

1805–1844, age 30 [S1][S2][S3]. Fallacies practice from 1812; Slave Ship verse 1840 in span — still below A/primary threshold.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data. Do not invent B from light lectures or storm subjects.

## Open questions

- Authenticated first-person God locus or denial.
- BL lecture MSS / Gage monograph; Finberg Fallacies corpus; Hamilton 1997 print.

## Research log

- 2026-10-24: Deepen D1 (queue #175). Tate chronology (baptism/burial); Tate Imms (Ruskin sun-is-God chain); MFA Slave Ship Fallacies verse; lecture light/colour clause; Independent on Hamilton/Bailey. primary/A → BELOW_THRESHOLD; B stays UNKNOWN; mid UNKNOWN; not plotted. P47 on S1–S9. No fallacy_catalog; no figures/.
- 2026-10-19: AA2 audit fix: the span ends are now dated by exhibition, The Shipwreck at Turner's gallery in 1805 (Tate, S2) and Rain, Steam, and Speed at the RA in 1844 (Egerton, National Gallery, S3), so first-lasting year, span, working_years and age rise from 0.5 to 0.7. Not plotted.
- 2026-10-19: AA3 audit fix: the Tate (Wilton) and National Gallery (Egerton) entries were fetched and read in full on 2026-10-19 and are relabelled 'read in full'.
- 2026-10-19: Correction found while coding AA4: region_of_birth and region_of_work are Northern Europe, not Western Europe; the United Kingdom is M49 Northern Europe (P3, data/reference/regions.csv).
- 2026-10-19: Read Britannica (Butlin).
