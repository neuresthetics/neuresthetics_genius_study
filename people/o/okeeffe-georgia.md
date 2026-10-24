---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Q; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-18
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-18, by: "Grok Bot", summary: "Record created (stage 3 batch Q, order P32: F 4, rank 99). Basics from Britannica (Barbara Buhler Lynes, signed; body read live through 'New Mexico'). Worldview: only a late remark reported second-hand ('I don't think much of God', at 96, quoted in a 2005 Merton Seasonal review of Coombs 2003) and a fan blog quoting an unnamed source (lead only, not cited). primary_system BELOW_THRESHOLD; A BELOW_THRESHOLD; B UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-18, by: "Grok Bot", summary: "Batch Q audit fixes (gs_0b3023d_Q run 1). Abstractions item year 1916 (291, May 1916; P30 #1), matching the field (O7, P13); 1915 composition noted. Notes: basis 'scholarly_reconstruction' removed from the BELOW_THRESHOLD primary_system and A (the remark is reported speech); the 'only partly returned' caveat dropped and the 'New Mexico' section page cited; Betz's year and issue noted as from the URL and index pages; the 1960 aerial abstractions noted as a possible span end; S1 shows no revision date. Values unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #98 / F4 rank 99). Needs: A BELOW; B UNKNOWN; artist not scientist — B needs P16 nature-order own-voice. Dual bio Wikipedia EN (S4, P50). P47 source_quality on S1–S8. Hunt: Access O'Keeffe Museum 'In Her Words' (S7) — aesthetic nature lines, no God place/deny, no P16; Wikiquote (S8) same; Betz/Coombs 'I don't think much of God' still third-hand (Coombs 2003 not on IA); fan blog religion quotes (S5) still unnamed archive; Merrill ASSIST NEWS (S6) Ginsberg 'It's hard to say' via assistant + Pedernal jokey God quip; Perry Miller Adato 1975/1977 transcripts catalogued but museum API 500 / full text not free. A stays BELOW_THRESHOLD (no place/deny ≥0.7). B stays UNKNOWN (aesthetics ≠ nature-order, P16). primary BELOW; mid UNKNOWN. Chart-moving NO. Draft deepen report in drafts/ (untracked). No fallacy_catalog. No figures refresh."}

identity:
  id: okeeffe-georgia
  display_name: "Georgia O'Keeffe"
  roster:
    canonical_name: "Georgia O'Keeffe"
    rank: 99
    F: 4
    models: [DeepSeek, Gemini, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: art
    field_bucket: arts
  full_name: {value: "Georgia O'Keeffe", certainty: 1.0, cites: [{source: S1, locator: "title"}, {source: S4, locator: "lead / infobox (Georgia Totto O'Keeffe)"}], how_known: "Britannica and Wikipedia agree (P15)."}
  native_name: {value: UNKNOWN, how_known: "English."}
  aliases:
    - {name: "Georgia Totto O'Keeffe", kind: "birth name"}

basics:
  birth:
    date: {value: "1887-11-15", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening sentence"}, {source: S4, locator: "infobox"}], how_known: "Britannica and Wikipedia agree."}
    place: {value: "near Sun Prairie, Wisconsin", modern_name: "Sun Prairie, Wisconsin, United States", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "opening sentence"}, {source: S4, locator: "infobox / Early life"}], how_known: "Britannica and Wikipedia agree."}
  death:
    date: {value: "1986-03-06", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening sentence"}, {source: S4, locator: "infobox"}], how_known: "Britannica and Wikipedia agree."}
    place: {value: "Santa Fe, New Mexico", modern_name: "Santa Fe, New Mexico, United States", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "opening sentence"}, {source: S4, locator: "infobox / Late career and death"}], how_known: "Britannica and Wikipedia agree."}
  first_lasting_contribution_year: {value: 1916, certainty: 0.5, cites: [{source: S1, locator: "'An emerging Modernist'"}, {source: S4, locator: "First abstractions (Stieglitz exhibited ten drawings at 291, April 1916)"}], how_known: "First public showing: Stieglitz hung 10 drawings at 291 in 1916 (P30 #1, earliest documented public showing). The 1915 composition of the abstractions (No. 3–Special) is noted but not the alternative basis: P30 addendum c applies only when no public showing exists."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "'An emerging Modernist'"}], how_known: "1916 (P2); the 1915 composition falls in the same bucket."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "opening sentence"}, {source: S4, locator: "infobox"}], how_known: "United States (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "'New York'; 'New Mexico'"}, {source: S4, locator: "New York; New Mexico"}], how_known: "New York, Lake George, New Mexico."}
  sex_as_recorded: {value: "female", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S4, locator: "lead"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  occupations: {value: ["painter", "art teacher"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Early years'"}, {source: S4, locator: "lead / Early life"}], how_known: "Britannica and Wikipedia."}

contribution:
  fields: {value: ["painting", "American Modernism"], certainty: 0.7, cites: [{source: S1, locator: "opening sentence"}, {source: S4, locator: "lead (American modernism)"}], how_known: "Britannica and Wikipedia."}
  lasting_original_contributions:
    - {value: "Charcoal abstractions such as No. 3–Special", year: 1916, kind: work, lasting: "'one of a handful of American and European Modernists' working in abstraction (S1)", certainty: 0.7, cites: [{source: S1, locator: "'An emerging Modernist'"}, {source: S4, locator: "First abstractions"}], how_known: "Britannica. Dated by first public showing: 10 drawings in a group exhibition at 291 in 1916 (P30 #1, P13). Composed 1915 (No. 3–Special, 1915), noted; the composition date is not used because a public showing exists."}
    - {value: "Large-format flower paintings (Black Iris, 1926; Jimson Weed/White Flower No. 1, 1932)", year: "1926–1932", kind: work, lasting: "the work 'by which she remains best known today' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'New York'"}, {source: S4, locator: "Flower paintings / Notable work"}], how_known: "Britannica and Wikipedia."}
    - {value: "New York skyscraper paintings (Radiator Building—Night, New York, 1927)", year: 1927, kind: work, lasting: "'some of her most distinctive paintings' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'New York'"}, {source: S4, locator: "New York Skyscraper paintings"}], how_known: "Britannica and Wikipedia."}
    - {value: "New Mexico landscapes and bones (From the White Place, 1940; Pelvis IV, 1944; Black Place III, 1944)", year: "1929–1944", kind: work, lasting: "named among her works in the signed body (S1)", certainty: 0.7, cites: [{source: S1, locator: "'New Mexico' (section page)"}, {source: S4, locator: "New Mexico / Skull and desert motifs"}], how_known: "Britannica 'New Mexico' section page; Wikipedia New Mexico section."}
  evidence_of_impact:
    - {value: "'among the most influential figures in Modernism'", kind: other, certainty: 0.7, cites: [{source: S1, locator: "opening sentence"}], how_known: "Britannica."}
    - {value: "Called the 'Mother of American modernism' (popular epithet)", kind: other, certainty: 0.5, cites: [{source: S4, locator: "lead"}], how_known: "Wikipedia lead; epithet, not a scholarly ranking."}
  major_works:
    - {value: "Georgia O'Keeffe (Viking Press autobiography)", year: 1976, kind: "book", certainty: 0.7, cites: [{source: S4, locator: "Late career and death / Publications"}], how_known: "Wikipedia; late autobiography — post-span for lasting painting contributions."}
  honours:
    - {value: "Art Students League William Merritt Chase still-life prize", year: 1908, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}, {source: S4, locator: "Academic training"}], how_known: "Britannica and Wikipedia."}
    - {value: "Presidential Medal of Freedom", year: 1977, certainty: 0.7, cites: [{source: S4, locator: "Awards and honors"}], how_known: "Wikipedia."}
    - {value: "National Medal of Arts", year: 1985, certainty: 0.7, cites: [{source: S4, locator: "Awards and honors / infobox"}], how_known: "Wikipedia."}
  definition_fit: {value: "clearly meets", rationale: "(S1; S4).", certainty: 0.7, cites: [{source: S1, locator: "opening sentence"}, {source: S4, locator: "lead"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Wisconsin farm family; boarded at Catholic Sacred Heart Academy (Madison) and graduated from Chatham Episcopal Institute (Virginia) — schooling context, not a documented adult creed", certainty: 0.5, cites: [{source: S4, locator: "Early life and education"}], how_known: "Wikipedia schooling; family denominational label not stated as such in S1/S4. ASSIST NEWS (S6) asserts Episcopalian upbringing — secondary lead only, not used as the value."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Francis Calyxtus O'Keeffe, dairy farmer (Irish descent)", role: father, certainty: 0.7, cites: [{source: S4, locator: "Early life"}, {source: S1, locator: "'Early years'"}], how_known: "Wikipedia names; Britannica dairy-farm household."}
    - {value: "Ida (Totto) O'Keeffe", role: mother, certainty: 0.7, cites: [{source: S4, locator: "Early life"}], how_known: "Wikipedia."}
    - {value: "Grew up with six siblings on a Wisconsin dairy farm", role: parents, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}, {source: S4, locator: "Early life (second of seven)"}], how_known: "Britannica and Wikipedia."}
  household_circumstances: {value: "Dairy farm; art lessons at home", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}, {source: S4, locator: "Early life (Sara Mann watercolor)"}], how_known: "Britannica and Wikipedia."}
  schooling:
    - {value: "Sacred Heart Academy, Madison, Wisconsin (boarder)", stage: "grammar or secondary school", years: "1901–1902", certainty: 0.7, cites: [{source: S4, locator: "Early life and education"}], how_known: "Wikipedia."}
    - {value: "Chatham Episcopal Institute, Virginia (now Chatham Hall); graduated 1905", stage: "grammar or secondary school", years: "–1905", certainty: 0.7, cites: [{source: S4, locator: "Early life and education"}], how_known: "Wikipedia."}
    - {value: "Art Institute of Chicago (1905–06); Art Students League, New York", stage: other, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}, {source: S4, locator: "Academic training"}], how_known: "Britannica and Wikipedia (adult training, after high school)."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1916–1944", certainty: 0.5, cites: [{source: S1, locator: "'An emerging Modernist'; 'New Mexico'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read that equates science and religion as systems."}
  primary_system:
    value: BELOW_THRESHOLD
    cites: [{source: S2, locator: "p. 29"}, {source: S5, locator: "fan-blog religion quotes"}, {source: S6, locator: "Ginsberg exchange"}]
    how_known: "No clear creed label in a primary or scholarly own-voice source. Late 'I don't think much of God' (S2) is third-hand and post-span. Fan-blog 'I'm not in a religion' / 'might be a buddhist' (S5) lack a named archival cite (P26). Merrill reports 'It's hard to say' to Ginsberg (S6) — suspension via assistant. Candidates AGNOS, BUDDH (P19); ATHE considered and rejected."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Late third-hand 'I don't think much of God' (S2); Merrill 'It's hard to say' (S6) — leads only, not enough to code."}
    - {code: BUDDH, reason: "Fan-blog 'I might be a buddhist' (S5); aesthetic preference for Buddhist art by the blog's own account — lead only."}
    - {code: ATHE, reason: "Not supported; late coolness toward God (S2) is not an outright denial, and Pedernal God-language is jokey figurative — lead against ATHE."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, cites: [{source: S2, locator: "p. 29"}, {source: S5, locator: "religion quotes"}, {source: S6, locator: "Ginsberg / Pedernal"}, {source: S4, locator: "Pedernal caption"}], how_known: "No own-voice place or deny of God at ≥0.7. 'I don't think much of God' (age 96) says little of where God is and reaches us third-hand (S2 quoting Coombs): reported speech cannot score an axis alone (§7; P19, P26); also decades after the span (P25). Fan-blog 'not in a religion' / Buddhist maybe (S5) are affiliation/ethics, not locus, and unnamed-source. Merrill 'It's hard to say' (S6) is suspension via assistant report (P42). Pedernal 'God told me if I painted it enough, I could have it' (S4/S6/S8) is jokey figurative ownership of a mountain, not a theological place claim. Alternatives: [].", alternatives: []}
    B_cause: {value: UNKNOWN, how_known: "Painter, not a scientist (P30). Access O'Keeffe / Wikiquote lines on the 'unexplainable thing in nature', desert bones, and 'wideness and wonder' (S7, S8) are aesthetic wonder and seeing — not own-voice on nature's order, immutable law, or exceptions (P16). Coombs's 'mysterious energy or presence' reading of the paintings is the critic's, not her statement (off-point, P19). Deepen D1: no P16 statement found."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN (§6, P19)."}
  statements:
    - text: "I don't think much of God."
      cites: [{source: S2, locator: "p. 29"}]
      context: "Quoted by Betz from Coombs (2003) as O'Keeffe's 'exclamation, at age 96' (so 1983–84); Coombs's page and source not seen. Deepen D1: Coombs still unread (not on IA)."
      axes: [A_locus]
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Third-hand; post-span. Cannot score A alone (§7)."
    - text: "I feel I'm a very religious person — religion to me means respect for people — but I'm not in a religion."
      cites: [{source: S5, locator: "never a catholic, maybe a buddhist"}]
      context: "Fan blog quotes an unnamed archival interview (likely Perry Miller Adato era); museum full transcripts not opened this pass."
      axes: [A_locus]
      kind: "reported speech"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Lead only (P26). Ethico-aesthetic affiliation, not a place/deny of God. Not used to score A."
    - text: "I couldn't be a catholic… I might be a buddhist."
      cites: [{source: S5, locator: "never a catholic, maybe a buddhist"}]
      context: "Same fan-blog post; blog itself frames Buddhist lean as aesthetic (tranquility of Buddhist art)."
      axes: [A_locus]
      kind: "reported speech"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Lead only (P26). Not used to score primary_system or A."
    - text: "It's hard to say."
      cites: [{source: S6, locator: "Ginsberg exchange via C.S. Merrill"}]
      context: "Reply to Allen Ginsberg's 'What is it you believe?' at Ghost Ranch, as reported by assistant C.S. Merrill in ASSIST NEWS / God Reports."
      axes: [A_locus]
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Assistant-reported suspension (P42). Lead only — not scored."
    - text: "It's my private mountain. It belongs to me. God told me if I painted it enough, I could have it."
      cites: [{source: S4, locator: "Personal life (Cerro Pedernal caption)"}, {source: S6, locator: "Pedernal quip"}, {source: S8, locator: "Wikiquote Pedernal"}]
      context: "Often-cited jokey remark about Cerro Pedernal near Ghost Ranch; Wikipedia cites Abrams / Eisler-type biography trail."
      axes: [A_locus]
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Figurative / jokey ownership of a landscape motif — not a theological place claim. Not scored."
    - text: "The unexplainable thing in nature that makes me feel the world is big far beyond my understanding — to understand maybe by trying to put it into form. To find the feeling of infinity on the horizon line or just over the next hill."
      cites: [{source: S7, locator: "1970s (Barbara Rose, NYRB 1977)"}, {source: S8, locator: "Wikiquote"}]
      context: "Quoted in Barbara Rose's 1977 NYRB piece; also on Access O'Keeffe 'In Her Words' and Wikiquote. Inside late career; aesthetic."
      axes: [B_cause]
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Aesthetic wonder / infinity feeling — fails P16 (not nature-order, law, or exceptions). Documented to show the B hunt."
    - text: "I have used these things to say what is to me the wideness and wonder of the world as I live in it."
      cites: [{source: S7, locator: "1940s — About Painting Desert Bones (An American Place 1944 brochure)"}]
      context: "Own exhibition statement on bones/desert (1944), inside the working span."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Aesthetic / experiential — not P16 nature-order. Museum 'In Her Words' transcription of her brochure statement."
  changes_over_life:
    - {value: "Schooling at Sacred Heart Academy and Chatham Episcopal Institute (heritage context) → adult working years with no clear creed place/deny in accessible own-voice → late reported suspension / coolness toward God (age 96; assistant/fan-blog leads)", certainty: 0.5, cites: [{source: S4, locator: "Early life"}, {source: S2, locator: "p. 29"}, {source: S5, locator: "religion quotes"}, {source: S6, locator: "Ginsberg"}], how_known: "Sequence of sources; adult A unscored."}
  coder_notes: "Deepen D1 2026-10-24: honest silence. Artist (P30): B needs P16; aesthetics alone not enough. A stays BELOW; B stays UNKNOWN. No fallacy_catalog. No figures refresh."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Wisconsin farm family; father Irish descent; maternal grandfather Hungarian (George Victor Totto)", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}, {source: S4, locator: "Early life"}], how_known: "Britannica farm; Wikipedia ancestry detail."}
  religious_heritage_by_birth: {value: "Christian schooling milieu (Catholic Sacred Heart Academy boarder; Chatham Episcopal Institute graduate) — family creed label not stated in S1/S4", certainty: 0.5, cites: [{source: S4, locator: "Early life and education"}], how_known: "Wikipedia schooling only; not coded as adult CHRIST."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1916–1944", certainty: 0.5, cites: [{source: S1, locator: "'An emerging Modernist'; 'New York'; 'New Mexico'"}, {source: S4, locator: "First abstractions through Black Place / pelvis series"}], how_known: "First public showing (1916) to Pelvis IV and Black Place III (1944), the latest works the Britannica body names in the part read (P30). Coder's call on the end year. Possible later end under P30 addendum b: the aerial abstractions after 1959, such as Blue, Black and Grey (1960), if they count as lasting (S1, 'New Mexico' section page; S4 Sky Above Clouds)."}
  age_at_first_lasting_contribution: {value: 29, certainty: 0.5, cites: [{source: S1, locator: "opening sentence; 'An emerging Modernist'"}], how_known: "1916 − 1887 = 29 (year subtraction, as in every other record; she was 28 in May 1916). (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No axis scored; late reported remarks are post-span and third-hand."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "Nothing scored on A or B.", certainty: 0.5, cites: [{source: S2, locator: "p. 29"}, {source: S7, locator: "In Her Words"}], how_known: "Coder's reading after deepen D1."}
  worldview_during_major_work: {value: BELOW_THRESHOLD, how_known: "As primary_system; aesthetic nature statements in-span do not yield A or B scores."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Ovals, hooked or V-shapes and spirals as her 'own' shapes (S1); visual, not a stated order.", certainty: 0.5, cites: [{source: S1, locator: "'New York'"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Early years'"}, {source: S4, locator: "First abstractions (Dow)"}], how_known: "Dow's harmonious arrangement of line, colour and notan (S1/S4)."}
  circle_present: {value: "unclear", rationale: "Spirals (S1); infinity-on-horizon language is aesthetic (S7).", certainty: 0.5, cites: [{source: S1, locator: "'New York'"}, {source: S7, locator: "unexplainable thing in nature"}], how_known: "Coder's reading."}
  reading: "Dow's design principles; aesthetic wonder at nature; no stated cosmology or nature-order claim."
  notes: "Lane B only. Flower/desert paintings not used to score A/B (P42 art-as-persona)."

institutions:
  - {value: "Columbia College, South Carolina", role: "art teacher", years: "1915", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'An emerging Modernist'"}, {source: S4, locator: "First abstractions"}], how_known: "Britannica and Wikipedia."}
  - {value: "West Texas State Normal College, Canyon", role: "head of the art department", years: "1916–1918", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'An emerging Modernist'"}, {source: S4, locator: "Early life / First abstractions"}], how_known: "Britannica and Wikipedia."}
collaborators:
  - {value: "Alfred Stieglitz (dealer and promoter; husband from 1924)", relation: family, certainty: 0.7, cites: [{source: S1, locator: "'An emerging Modernist'"}, {source: S4, locator: "Personal life / infobox"}], how_known: "Britannica and Wikipedia."}

review:
  roster_status_reason: {value: "Core in v8 (F 4; decision R1).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 99"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "No verified primary interview transcript for religion remarks; fan-blog and assistant reports are leads (P26, P42)."
    - "Coombs 2003 unread; 'I don't think much of God' remains third-hand via Betz."
    - "Perry Miller Adato 1975/1977 museum transcripts catalogued but not freely readable (API 500)."
    - "Artist: B requires P16; aesthetic nature statements documented and rejected for scoring."
  open_questions:
    - "Open Perry Miller Adato 1975/1977 transcripts at the Georgia O'Keeffe Museum Archives for the fan-blog religion quotes."
    - "Check Coombs (2003) page and source for 'I don't think much of God'."
    - "Robinson Georgia O'Keeffe: A Life for the God-as-female claim in print."
    - "Spot-check Greenough My Faraway One / Pollitzer Lovingly, Georgia for any A place/deny or P16 B (museum In Her Words sample suggests aesthetic silence)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Barbara Buhler Lynes"
    citation: "Lynes, Barbara Buhler. \"Georgia O'Keeffe.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Georgia-OKeeffe. Read live 2026-10-18, with the section page https://www.britannica.com/biography/Georgia-OKeeffe/New-Mexico. The page shows no revision date. Deepen D1 2026-10-24: body retained; dual bio with S4."
    url: "https://www.britannica.com/biography/Georgia-OKeeffe"
    accessed: 2026-10-18
    source_quality: "reference entry"
    reliability_note: "Signed article by the former curator of the Georgia O'Keeffe Museum. Body only; AI 'Top Questions' and Quick Facts not cited."
    used_for: [identity, basics, contribution, childhood, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: journal article
    author: "Margaret B. Betz"
    citation: "Betz, Margaret B. \"Transcendent Creativity.\" Review of Mystery Hidden Yet Revealed by Marie Theresa Coombs (Eugene, OR: Wipf and Stock, 2003). The Merton Seasonal 30, no. 1 (Spring 2005): 28–29. https://merton.org/ITMS/Seasonal/30/30-1BetzRevCoombs.pdf (volume, issue and year from the URL and the Merton Center's index pages, not the PDF text)"
    url: "https://merton.org/ITMS/Seasonal/30/30-1BetzRevCoombs.pdf"
    accessed: 2026-10-18
    source_quality: "other"
    reliability_note: "Book review quoting a devotional study; the quotation is secondary at two removes. Coombs 2003 not opened deepen D1."
    used_for: [worldview, timing]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-18
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [identity, review]
  - id: S4
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. \"Georgia O'Keeffe.\" Wikipedia. https://en.wikipedia.org/wiki/Georgia_O%27Keeffe. Dual bio (P50). Read 2026-10-24."
    url: "https://en.wikipedia.org/wiki/Georgia_O%27Keeffe"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Used for dual-bio basics, schooling, Pedernal caption, awards. Worldview coding does not rest on Wikipedia paraphrases of spirituality."
    used_for: [identity, basics, contribution, childhood, heritage, institutions, collaborators, worldview]
  - id: S5
    type: secondary
    kind: other
    author: "My Georgia O'Keeffe (fan blog)"
    citation: "\"Georgia O'Keeffe: never a catholic, maybe a buddhist.\" mygeorgiaokeeffe.com. https://mygeorgiaokeeffe.com/georgia-okeeffe-never-a-catholic-maybe-a-buddhist/ (religion quotes without named archival cite)."
    url: "https://mygeorgiaokeeffe.com/georgia-okeeffe-never-a-catholic-maybe-a-buddhist/"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Fan blog; quotes unnamed archives. Lead only (P26) — not used to score A or primary_system."
    used_for: [worldview]
  - id: S6
    type: secondary
    kind: other
    author: "ASSIST News / God Reports (via C.S. Merrill)"
    citation: "\"Georgia O'Keeffe and Faith.\" ASSIST News / God Reports. https://www.assistnews.net/georgia-okeeffe-and-faith/ (Merrill-reported Ginsberg exchange; Pedernal; Robinson God-as-female)."
    url: "https://www.assistnews.net/georgia-okeeffe-and-faith/"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Devotional journalism quoting an assistant and biographers. Reported speech (P42). Lead only."
    used_for: [worldview]
  - id: S7
    type: secondary
    kind: other
    author: "Georgia O'Keeffe Museum (Access O'Keeffe)"
    citation: "Georgia O'Keeffe Museum. \"Georgia O'Keeffe In Her Own Words.\" Access O'Keeffe. https://access-ok.okeeffemuseum.org/in-her-words/ (decade-by-decade statements including 1939/1944 desert-bones brochure text and Rose 1977 'unexplainable thing in nature'). Read 2026-10-24."
    url: "https://access-ok.okeeffemuseum.org/in-her-words/"
    accessed: 2026-10-24
    source_quality: "other"
    reliability_note: "Museum-curated selection of her statements with bibliographic notes. Used to document aesthetic nature language and the absence of A place/deny / P16 B in the sample."
    used_for: [worldview, timing]
  - id: S8
    type: secondary
    kind: other
    author: "Wikiquote contributors"
    citation: "Wikiquote contributors. \"Georgia O'Keeffe.\" https://en.wikiquote.org/wiki/Georgia_O%27Keeffe. Read 2026-10-24 for Pedernal and nature lines."
    url: "https://en.wikiquote.org/wiki/Georgia_O%27Keeffe"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Quote aggregator; cross-checked against S7 where overlapping. Not used alone to score."
    used_for: [worldview]
---

# Georgia O'Keeffe

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Georgia O'Keeffe (1887–1986), American Modernist painter [S1; S4]. Deepen D1: primary_system BELOW_THRESHOLD; A BELOW_THRESHOLD; B UNKNOWN; mid_basin UNKNOWN. Not plotted. Chart-moving NO.

## Life and work

Wisconsin farm; Sacred Heart Academy and Chatham Episcopal Institute; Chicago and New York art schools; Dow's principles; abstractions shown by Stieglitz at 291 (1916); New York; New Mexico from 1929 [S1; S4].

## Contribution and impact

Abstractions, flowers, skyscrapers, New Mexico landscapes [S1; S4]. Presidential Medal of Freedom (1977); National Medal of Arts (1985) [S4].

## Childhood and education

Dairy farm, six siblings, art lessons at home [S1; S4]. Sacred Heart Academy boarder; Chatham Episcopal Institute graduate [S4].

## Adult working worldview

No scored A place/deny or P16 B. Late third-hand 'I don't think much of God' [S2, p. 29]; fan-blog and assistant religion leads [S5; S6]; Pedernal jokey God quip [S4; S6; S8]. In-span aesthetic nature statements (desert bones; 'unexplainable thing in nature') fail P16 [S7; S8].

## Heritage (context only)

Wisconsin farm family; Christian schooling milieu [S1; S4].

## Timing

1916–1944 [S1; S4].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Ovals and spirals; Dow [S1; S4]. Aesthetic wonder, not cosmology [S7].

## Open questions

- Perry Miller Adato 1975/1977 museum transcripts.
- Coombs (2003) for the late God remark.
- Robinson God-as-female in print; Greenough / Pollitzer letter volumes spot-check.

## Research log

- 2026-10-18: Read Britannica (live), Betz's review (PDF), and a fan blog (lead only).
- 2026-10-24: Deepen D1. Wikipedia EN dual bio; Access O'Keeffe In Her Words; Wikiquote; Merrill ASSIST NEWS; fan blog re-checked; Coombs 2003 not on IA; Adato transcript API 500. Wrote drafts/deepen_okeeffe-georgia.md (untracked). A BELOW / B UNKNOWN kept. No figures refresh. No fallacy_catalog.
