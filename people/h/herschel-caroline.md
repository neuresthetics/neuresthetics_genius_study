---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 9
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, third batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 19c. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #149, F 3, rank 155). Re-searched full 1876 Memoir (IA OCR + Gutenberg #52923 clean text); Hoskin Autobiographies excerpt (German History Intersections, S6); Phil. Trans. comet letters (IA, S7 — observational only); Wikipedia EN dual bio (S5; P50). Extra conventional God-bless / thank-God closings found; no Creator / nature-cause / why-heavens-move own-voice. Aubert 1786 'Being who has ordered all these things to move' is TO her, not hers. CHRIST stays 0.5; A 0 stays 0.5 (named alt 1 formula); B stays BELOW_THRESHOLD (P6; not reconstructed from comet-sweeping); C/D/E BELOW; mid BELOW. support single on A (P48; only S3). P47 source_quality S1–S7. Chart-moving NO (not plotted). No figures/; no fallacy_catalog. Draft, not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (third batch, RUNBOOK §1 order). Basics from Britannica and MacTutor; her own words from Memoir and Correspondence of Caroline Herschel (John Murray, 1876), page images checked for pp. 17–18, 235–236, 275, 347 and 351. Primary CHRIST at 0.5 (consistent_private_letters, below the ceiling because the evidence is brief devotional phrases: a Nunc dimittis citation, thanksgiving and prayer to 'the Almighty', 'as long as God pleases'); A 0 at 0.5; B, C, D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Schema 1.1 → 1.2 (decision P8 adds basis recorded_interview and statement kind 'recorded interview'); no content change."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 3, #121 (run 1): 'later buried in the garrison church' overstated p. 347. Only the funeral service ('the holy words spoken over it') was held in the garrison church; she asked to be laid beside her father and mother (p. 347), and her epitaph says her father lies 'hierneben begraben' (p. 351). family_religion, the CHRIST rationale and the body now say so. The christening and confirmation in the garrison church are now attributed to the editor (p. 347); her own recollection records the confirmation and first communion (pp. 17–18) without naming the church. No score changed. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 4 (two blind runs at b21655b). Decision P13 recheck: first_lasting_contribution_year 1786 → 1783 (the listed three nebulae of 1783, the earliest listed contribution; the old alternative is now the value), age 36 → 33; era unchanged. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02). Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs. Full before → after list: reports/stage3_rulings_changes.csv. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Span alignment (P29, P30 and its addendum): timing.major_work_period 1786–1828 → 1783–1828; worldview.working_years 1772–1848 → 1783–1828, equal to the span (P30 addendum f); 2 headline values rest on evidence outside the span and are left unchanged for a ruling (open questions). Listed in reports/p30_span_alignment.csv. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "P31 (continuity rule, v8's pick, 2026-10-02): the 2 values the span check flagged as resting on evidence outside the span are resolved, since changes_over_life documents no change of view between the span and that evidence; no value or certainty changed; the Open questions pointer line was removed. Listed in reports/p30_span_alignment.csv. Not reviewed."}

identity:
  id: herschel-caroline
  display_name: "Caroline Herschel"
  roster:
    canonical_name: "Caroline Herschel"
    rank: 155
    F: 3
    models: [DeepSeek, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: astronomy
    field_bucket: astronomy
  full_name: {value: "Caroline Lucretia Herschel", certainty: 1.0, cites: [{source: S1, locator: "'Also known as'"}, {source: S2, locator: "heading"}], how_known: "Two sources."}
  native_name: {value: "Carolina Lucretia Herschel (German form on her epitaph: 'Carolina Herschel')", certainty: 0.7, cites: [{source: S3, locator: "p. 351 (epitaph)"}], how_known: "Epitaph as printed; the full German form with 'Lucretia' is not in a source read."}
  aliases:
    - {name: "Caroline Lucretia Herschel", kind: "roster alias"}
    - {name: "Caroline-Herschel", kind: "roster alias"}
    - {name: "Carolina Herschel", kind: other}

basics:
  birth:
    date: {value: "1750-03-16", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "p. 351 (epitaph)"}], how_known: "Two sources agree."}
    place: {value: "Hanover", modern_name: "Hannover, Lower Saxony, Germany", polity_then: "Electorate of Brunswick-Lüneburg (Hanover)", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "p. 351 (epitaph)"}], how_known: "Two sources agree."}
  death:
    date: {value: "1848-01-09", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "p. 351 (epitaph)"}], how_known: "Two sources agree."}
    place: {value: "Hanover", modern_name: "Hannover, Lower Saxony, Germany", polity_then: "Kingdom of Hanover", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "p. 347"}], how_known: "Two sources agree."}
  first_lasting_contribution_year: {value: 1783, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "The three nebulae she detected by telescope in 1783 (Britannica), the earliest listed contribution (decision P13); 0.7 because only one source calls them out. Her first comet followed on 1 August 1786 (S1; S2, 1786 paragraph). Was 1786, with 1783 as the alternative, until the batch 4 lens audit."}
  era_bucket: {value: "1750 to 1849", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "From first_lasting_contribution_year 1783 (P2); the first comet (1786) gives the same bucket."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Germany is Western Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "paragraphs 2–4"}, {source: S2, locator: "Bath to Slough paragraphs"}], how_known: "Comets and the Flamsteed index were done in England (UK, Northern Europe), 1772–1822; the nebula catalogue was finished in Hanover (Western Europe) after 1822. Two regions, so 0.7.", alternatives: [{value: "Western Europe", cites: [{source: S2, locator: "1822 paragraph"}], note: "Hanover, 1822–1848."}]}
  sex_as_recorded: {value: "female", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "As the sources record it."}
  languages_of_work: {value: [English, German], certainty: 0.7, cites: [{source: S3, locator: "pp. 235–236, 275 (letters in English)"}, {source: S2, locator: "Bath paragraph (William taught her English)"}], how_known: "Letters printed in English; German was her first language."}
  occupations: {value: ["astronomer", "singer", "assistant to William Herschel"], certainty: 1.0, cites: [{source: S1, locator: "paragraphs 1–3"}, {source: S2, locator: "Bath paragraphs"}], how_known: "Two sources."}

contribution:
  era_bucket: 19c
  fields: {value: ["observational astronomy", "comets", "star and nebula catalogues"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "summary"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Discovery of eight comets, the first in 1786 (one periodic: 35P/Herschel–Rigollet)", year: "1786–1797", kind: discovery, lasting: "first comets discovered by a woman", certainty: 1.0, cites: [{source: S1, locator: "opening; paragraph 3"}, {source: S2, locator: "1786 and 1797 paragraphs"}], how_known: "Two sources."}
    - {value: "Index to Flamsteed's Observations of the Fixed Stars, with 560 omitted stars and errata", year: "1798", kind: work, lasting: "published by the Royal Society", certainty: 1.0, cites: [{source: S1, locator: "paragraph 3"}, {source: S2, locator: "Flamsteed paragraph"}], how_known: "Two sources."}
    - {value: "Catalogue of about 2,500 nebulae and star clusters (reduction of William Herschel's sweeps)", year: "1822–1828", kind: work, lasting: "Royal Astronomical Society gold medal, 1828", certainty: 1.0, cites: [{source: S1, locator: "paragraph 4"}, {source: S2, locator: "1822 paragraph"}], how_known: "Two sources."}
    - {value: "Three nebulae detected by telescope", year: "1783", kind: discovery, lasting: "early independent discoveries", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "Comet 35P/Herschel–Rigollet and the minor planet Lucretia (1889)", kind: "named after them", certainty: 0.7, cites: [{source: S1, locator: "paragraph 3"}, {source: S2, locator: "final paragraph"}], how_known: "One source for each name."}
    - {value: "Royal pension from George III (1787) as William's assistant, which Britannica calls the first salary of a professional female astronomer", kind: "honours in lifetime", certainty: 1.0, cites: [{source: S1, locator: "paragraph 3"}, {source: S2, locator: "1787 paragraph"}], how_known: "Two sources."}
  major_works:
    - {value: "Catalogue of Stars, Taken from Mr. Flamsteed's Observations [...] (Index to Flamsteed)", year: 1798, kind: book, certainty: 0.7, cites: [{source: S2, locator: "Flamsteed paragraph"}], how_known: "MacTutor gives the subject; the printed title was not checked (flag)."}
  honours:
    - {value: "Gold Medal of the (Royal) Astronomical Society", year: 1828, certainty: 1.0, cites: [{source: S1, locator: "paragraph 4"}, {source: S2, locator: "1822 paragraph"}], how_known: "Two sources; they differ on what it was for (see flags)."}
    - {value: "Honorary member of the Royal Astronomical Society (with Mary Somerville, the first women)", year: 1835, certainty: 0.7, cites: [{source: S2, locator: "honours paragraph"}], how_known: "MacTutor; her own letter mentions the choice (S3, p. 276)."}
    - {value: "Member of the Royal Irish Academy", year: 1838, certainty: 1.0, cites: [{source: S2, locator: "honours paragraph"}, {source: S3, locator: "p. 351 (epitaph)"}], how_known: "Two sources (the epitaph gives no year)."}
    - {value: "Gold Medal for Science from the King of Prussia", year: 1846, certainty: 0.7, cites: [{source: S2, locator: "honours paragraph (her 96th birthday)"}], how_known: "MacTutor."}
  definition_fit: {value: "clearly meets", rationale: "Independent discoveries (comets, nebulae) and major catalogues; her largest work reduced her brother's observations.", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "1822 paragraph"}], how_known: "Coder's reading of the two sources."}

childhood:
  family_religion: {value: "Christian / Protestant family line; christened and confirmed in the garrison church of Hanover, where her funeral service was also held; she was buried beside her parents", certainty: 1.0, cites: [{source: S3, locator: "pp. 1–2 (Isaac memorandum: brothers left Moravia as Protestants), 17–18, 347, 351"}, {source: S5, locator: "Early life"}], how_known: "Memoir: Isaac's memo (transcribed by her) traces Herschels leaving Moravia as Protestants (S3 pp. 1–2). Editor (p. 347): funeral in garrison church of her christening/confirmation; buried beside parents; epitaph 'hierneben begraben' (p. 351). Own recollection of confirmation/first communion (pp. 17–18) without naming the church. Wikipedia agrees Hanover birth and family outline (S5)."}
  family_religious_practice: {value: "Church attendance and confirmation instruction as a girl", certainty: 1.0, cites: [{source: S3, locator: "pp. 16–17"}], how_known: "Her own recollection: 'my constant attendance at church and school' (p. 17); her mother released her from housework for the 'necessary preparation for her daughter's confirmation' (p. 16)."}
  parents_and_household:
    - {value: "Father, Isaac Herschel, oboist and later bandmaster in the Hanoverian Foot Guards, with interests in music, philosophy and astronomy", name: "Isaac Herschel", role: father, certainty: 0.7, cites: [{source: S2, locator: "paragraph 1"}], how_known: "MacTutor."}
    - {value: "Mother, Anna Ilse Moritzen, who opposed her daughters' education", name: "Anna Ilse Herschel (née Moritzen)", role: mother, certainty: 1.0, cites: [{source: S2, locator: "paragraph 1"}, {source: S1, locator: "paragraph 2"}], how_known: "Two sources (Britannica on the opposition)."}
  household_circumstances: {value: "Six children; brothers trained as musicians; she was kept to household work, especially after her father's death in 1767; typhus at about ten stunted her growth", certainty: 1.0, cites: [{source: S1, locator: "paragraph 2"}, {source: S2, locator: "paragraphs 1–3"}], how_known: "Two sources."}
  schooling:
    - {value: "School in Hanover alongside confirmation instruction (school not named)", stage: other, years: "–1764", certainty: 0.7, cites: [{source: S3, locator: "p. 17"}], how_known: "Her recollection; the school is not named."}
    - {value: "Lessons in dressmaking; studied to qualify as a governess", stage: other, years: "after 1767", certainty: 0.7, cites: [{source: S2, locator: "paragraph 3"}], how_known: "MacTutor."}
    - {value: "Taught singing, English, algebra, geometry and spherical trigonometry by her brother William in Bath", stage: tutor, years: "1772–1782", certainty: 1.0, cites: [{source: S1, locator: "paragraph 2"}, {source: S2, locator: "Bath paragraphs"}], how_known: "Two sources."}
  early_mathematics: {value: TODO, note: "Her mathematics (algebra, geometry, spherical trigonometry) came from William in Bath, from age 22; childhood mathematics not researched."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Her father showed her constellations on a frosty night after watching a comet", certainty: 0.7, cites: [{source: S2, locator: "paragraph 2 (quoting the Memoir)"}], how_known: "MacTutor quoting her recollection."}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [German], certainty: 0.7, cites: [{source: S2, locator: "Bath paragraph"}], how_known: "Born in Hanover; William taught her English after 1772."}
  notable_events:
    - {value: "Confirmed on a Sunday during William's visit, then received first communion the following Sunday, the day he left", year: "1764", certainty: 0.7, cites: [{source: S3, locator: "pp. 17–18"}], how_known: "Her recollection; the year comes from the editor's narrative (William arrived 2 April 1764), so 'Sunday the 8th' is 8 April 1764."}
    - {value: "Typhus at about ten", year: "1760", certainty: 0.7, cites: [{source: S1, locator: "paragraph 2"}], how_known: "Britannica (age 10)."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1783–1828", certainty: 1.0, cites: [{source: S1, locator: "paragraphs 1–4"}, {source: S2, locator: "1786–1828 paragraphs"}], how_known: "Equal to timing.major_work_period (P30 addendum f; span check 2026-10-02). Was 1772–1848: From Bath to her death."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Deepen D1 re-search of Memoir full text (IA + Gutenberg) and Hoskin Autobiographies excerpt (S6): no statement relating astronomy and religion. 'Minding the heavens' = observing. Aubert's 1786 'Being who has ordered all these things to move as we find them' is addressed TO her (S3), not her voice."}
  primary_system:
    value: CHRIST
    basis: consistent_private_letters
    certainty: 0.5
    cites: [{source: S3, locator: "pp. 235, 236, 275"}]
    how_known: "Deepen D1: same three private letters (2× 3 Mar 1829; 23 Apr 1835) re-checked in Gutenberg #52923 against prior page-image notes; plus recurring conventional closings ('God bless you', 'thank God', 'God grant') across later letters — still brief devotion, not a creed. Below 0.7: conventional letter piety + family edition with cuts. Protestant Moravia heritage (S3 pp. 1–2) is context only."
    rationale: "CHRIST: scripture (Luke 2:29 / Simeon), thanksgiving and prayer to 'the Almighty', lifespan 'as long as God pleases'. Upbringing and garrison-church rites do not code by themselves. Named alternative CLTHEI only if petition showed God acting against nature's course — none found (deepen confirmed)."
    alternatives:
      - {value: CLTHEI, cites: [{source: S3, locator: "p. 275"}], note: "A prayer for future protection is petition; preferred only if her writing showed God acting in particular events beyond nature's course. None found."}
  secondary_system: {value: UNKNOWN, how_known: "No second system in the sources read."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Chosen at 0.5: scripture, thanksgiving and prayer in her letters (S3, pp. 235–236, 275).", cites: [{source: S3, locator: "pp. 235–236, 275"}]}
    - {code: CLTHEI, reason: "Prayer for protection is petition; not chosen because nothing read shows God expected to act against the course of nature.", cites: [{source: S3, locator: "p. 275"}]}
    - {code: DEISM, reason: "Rejected: she prays to God for protection and treats her lifespan as in God's pleasure (S3, pp. 235, 275).", cites: [{source: S3, locator: "pp. 235, 275"}]}
  lio_axes:
    A_locus:
      value: 0
      basis: consistent_private_letters
      certainty: 0.5
      support: single
      cites: [{source: S3, locator: "pp. 235, 275"}]
      how_known: "Deepen D1: same two private letters (1829, 1835) re-checked; additional 'God bless' / 'thank God' closings corroborate conventional piety but do not lift past brief-phrase ceiling. Support single (P48): only S3. Named alt 1 (formula) keeps contested reading ≤0.7."
      rationale: "Personal God ('the Almighty') addressed in thanksgiving and petition; lifespan under God's pleasure — A 0. Nothing places God in the world. Alternative 1: formulaic letter closings without settled locus belief."
      alternatives:
        - {value: 1, note: "Read the Almighty / God-pleases phrases as conventional letter formula rather than a personal-locus profession.", cites: [{source: S3, locator: "pp. 235, 275"}]}
    B_cause: {value: BELOW_THRESHOLD, how_known: "Scored on her account of nature (P6). Deepen D1: Memoir + Hoskin Autobiographies excerpt (S6) + Phil. Trans. comet letters (S7) give sweeping, reducing, cataloguing — no own-voice on why the heavens move. Providential phrases concern her life, not nature. Aubert 1786 'Being who has ordered all these things to move as we find them' is TO her (S3), not hers. Not reconstructed from comet-sweeping alone (standing deepen rule)."}
    C_ledger: {value: BELOW_THRESHOLD, how_known: "No statement on reward, punishment or judgement in her own words read.", note: "Her epitaph, said by the editor to be 'of her own composition' (S3, p. 347), speaks of her father gone before 'zu einem besseren Leben' (p. 351); it was completed after her death (it gives her age at death), so the wording cannot be assigned to her with confidence, and it states hope of an afterlife, not a ledger."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "Nothing read on revelation against observation. Quoting Luke to express joy (p. 236) shows use of scripture, not its authority over natural knowledge."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). 'A prayer for future protection' (p. 275, a single letter) asks for protection but says nothing about God answering petition with particular events; not enough to score."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus only 0.5 and B_cause BELOW_THRESHOLD, under the P4 test's 0.7 bar. Chart-moving NO (deepen 2026-10-24)."}
  statements:
    - text: "But as long as God pleases I shall remain"
      cites: [{source: S3, locator: "p. 235"}]
      date: "1829-03-03"
      context: "Closing line before her signature ('Your most affectionate sister, C. Herschel') in a letter to William's widow, Lady Herschel, on John Herschel's marriage, after arrangements for her belongings at her death."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: 'But I can at this present moment find no words which would better express my happiness than those which escaped in exclamation from my lips, according to Simeon. See St. Luke, cap. ii., v. 29: "Lord, now lettest thou thy servant depart in peace!"'
      cites: [{source: S3, locator: "p. 236"}]
      date: "1829-03-03"
      context: "Letter to her nephew J. F. W. Herschel on news of his engagement."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "Each time after having read them over again they are put by, under thanksgiving to the Almighty, with a prayer for future protection."
      cites: [{source: S3, locator: "p. 275"}]
      date: "1835-04-23"
      context: "Letter to her nephew's wife ('My dearest Niece'), about the five letters received from the family at the Cape."
      axes: [A_locus, E_scope]
      kind: "private letter"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
  changes_over_life: []
  coder_notes: "Deepen D1 2026-10-24: full Memoir re-search (IA OCR + Gutenberg #52923); Hoskin Autobiographies pp. 71–77 excerpt (S6) — assistant-astronomer narrative, no locus/cause; Phil. Trans. comet discovery letters (S7) observational only. Aubert Aug 1786 letter TO her has the only 'Being who has ordered … move' line in the volume — not scored. Devotional closings ('God bless you', 'thank God', 'God grant') recur; not lifted past CHRIST/A @0.5. Epitaph authorship still uncertain (C). Destroyed 1788–1798 diaries (S2/S5) leave a known gap. Chart stays unplotted / not chart-moving."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Hanoverian German; a musicians' family", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: "Christian / Protestant (Hanover garrison church; family left Moravia as Protestants)", certainty: 1.0, cites: [{source: S3, locator: "pp. 1–2, 347"}, {source: S5, locator: "Early life"}], how_known: "Isaac memorandum via Memoir; editor on garrison church; Wikipedia family outline."}
  baptism_or_initiation: {value: "Christened in the garrison church, Hanover", certainty: 1.0, cites: [{source: S3, locator: "p. 347"}], how_known: "Editor's account, checked on the page image."}
  childhood_catechism: {value: "Confirmation instruction, then confirmation and first communion in 1764 (in the garrison church, per the editor)", certainty: 1.0, cites: [{source: S3, locator: "pp. 16–18, 347"}], how_known: "Her recollection (pp. 17–18, which do not name the church) and the editor's narrative (pp. 16, 347)."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1783–1828", certainty: 1.0, cites: [{source: S1, locator: "paragraphs 1–4"}, {source: S2, locator: "1786–1828 paragraphs"}], how_known: "From the three nebulae of 1783 to the nebula catalogue (1822–1828), the first and last listed lasting contributions (P29). Span check 2026-10-02 (P29, P30 and its addendum): was 1786–1828, which started with the first comet rather than the earliest listed item."}
  age_at_first_lasting_contribution: {value: 33, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Born 16 March 1750; three nebulae in 1783 (month not given), so 33 for most of the year. Was 36 (first comet, August 1786) until the batch 4 lens audit."}
  first_evidence_of_lio_type_views: {value: "1829", certainty: 0.5, cites: [{source: S3, locator: "pp. 235–236"}], how_known: "Earliest dated A-bearing letters (3 Mar 1829); after the 1783–1828 span; continuity assumed under P31 (no change_of_view documented). Brief conventional phrases → 0.5."}
  lio_views_relative_to_major_work: {value: "after major work", rationale: "A-bearing letters 1829/1835 post-date the nebula-catalogue span end 1828; no in-span LIO statement found.", certainty: 0.5, cites: [{source: S3, locator: "pp. 235–236, 275"}], how_known: "Deepen D1 dating."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "No in-span LIO statement; CHRIST/A evidence is post-span private letters (P31 continuity for the coded values)."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Observational and computational work (sweeps, reductions, catalogues); no definition-and-consequence argument read.", certainty: 0.5, cites: [{source: S2, locator: "Bath to 1828 paragraphs"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "Bath paragraphs"}], how_known: "Geometry and spherical trigonometry learned from William; interest only in useful parts (S2)."}
  circle_present: {value: "no", rationale: "Her God language (S3) is personal and petitionary, not a God–Nature identity.", certainty: 0.5, cites: [{source: S3, locator: "pp. 235, 275"}], how_known: "Coder's reading of brief phrases."}
  reading: "As belief, not finding: no geometric form and no circle in what was read. The record does not test H1."
  notes: ""

institutions:
  - {value: "King George III (royal pension as William's assistant)", role: "pensioned assistant astronomer", years: "1787–", kind: "patron or funder", certainty: 1.0, cites: [{source: S1, locator: "paragraph 3"}, {source: S2, locator: "1787 paragraph"}], how_known: "Two sources."}
  - {value: "Royal Astronomical Society", role: "gold medallist (1828); honorary member (1835)", years: "1828–1848", kind: "academy or learned society", certainty: 1.0, cites: [{source: S1, locator: "paragraph 4"}, {source: S2, locator: "honours paragraph"}], how_known: "Two sources."}
  - {value: "Royal Irish Academy", role: member, years: "1838–1848", kind: "academy or learned society", certainty: 0.7, cites: [{source: S2, locator: "honours paragraph"}, {source: S3, locator: "p. 351"}], how_known: "Two sources; year from MacTutor only."}
collaborators:
  - {value: "William Herschel", roster_id: herschel-william, relation: collaborator, note: "brother; she kept house, ground mirrors, recorded and reduced his observations (1772–1822)", certainty: 1.0, cites: [{source: S1, locator: "paragraphs 1–3"}, {source: S2, locator: "Bath to 1822 paragraphs"}], how_known: "Two sources."}
  - {value: "John Herschel", relation: family, note: "nephew; she helped educate him and compiled the nebula catalogue for his work", certainty: 1.0, cites: [{source: S2, locator: "1822 paragraph"}, {source: S3, locator: "p. 236"}], how_known: "Two sources."}
  - {value: "Mary Somerville", roster_id: somerville-mary, relation: correspondent, note: "elected with her as the first women honorary members of the RAS (1835); a letter from Somerville to her is printed", certainty: 0.7, cites: [{source: S2, locator: "honours paragraph"}, {source: S3, locator: "p. 274"}], how_known: "Two sources."}
  - {value: "Carl Friedrich Gauss", roster_id: gauss-carl-friedrich, relation: other, note: "visited her in Hanover", certainty: 0.7, cites: [{source: S2, locator: "Hanover paragraph"}], how_known: "MacTutor."}

review:
  roster_status_reason: {value: "Core in v8 (F 3: DeepSeek, GPT, Grok).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 155"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "What the 1828 gold medal was for: Britannica says an 'unpublished revision and reorganization of their work'; MacTutor says the catalogue of 2,500 nebulae."
    - "Britannica article is signed only 'The Editors'."
    - "The 1876 Memoir is a family edition with editorial cuts; letters were read as printed, not against manuscripts."
    - "Printed title of the 1798 Flamsteed index not checked."
    - "Hoskin Autobiographies (2003) full book not obtained; only pp. 71–77 public excerpt (S6)."
  open_questions:
    - "Full Hoskin Autobiographies (2003) and Discoverers of the Universe (2011) for any religion / nature-cause lines beyond the public excerpt."
    - "Epitaph manuscript in her hand (RAS Herschel papers)."
    - "Any in-span (1783–1828) public or private statement on God / nature's order stronger than letter closings."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "The Editors of Encyclopaedia Britannica"
    citation: "\"Caroline Herschel.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Caroline-Lucretia-Herschel."
    url: "https://www.britannica.com/biography/Caroline-Lucretia-Herschel"
    accessed: 2026-10-02
    reliability_note: "Unsigned editors' article, four paragraphs; cited by paragraph."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "J J O'Connor and E F Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Caroline Lucretia Herschel.\" MacTutor History of Mathematics, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Herschel_Caroline/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Herschel_Caroline/"
    accessed: 2026-10-02
    reliability_note: "Biography drawing on Hoskin and the Memoir; cited by paragraph subject."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S3
    type: primary
    kind: letter
    author: "Caroline Herschel; ed. Mrs. John Herschel"
    year: 1876
    citation: "Herschel, Mrs. John (ed.). Memoir and Correspondence of Caroline Herschel. London: John Murray, 1876. Internet Archive memoircorrespond00hersiala (University of California Libraries)."
    url: "https://archive.org/details/memoircorrespond00hersiala"
    accessed: 2026-10-02
    reliability_note: "Her recollections and letters as printed by the family, with editorial cuts. Page images checked for pp. 17, 18, 235, 236, 275, 276, 347 and 351; deepen D1 also used IA full OCR and Gutenberg #52923 clean text for volume-wide search."
    source_quality: "primary / own words"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S5
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Caroline Herschel. Wikipedia. https://en.wikipedia.org/wiki/Caroline_Herschel"
    url: "https://en.wikipedia.org/wiki/Caroline_Herschel"
    accessed: 2026-10-24
    reliability_note: "Unsigned tertiary; dual-source bio (P50) against Britannica/MacTutor — birth/death Hanover 1750–1848, parents Isaac/Anna Ilse Moritzen, typhus, Bath 1772, comets, Flamsteed index, RAS gold 1828, destroyed diaries after William's marriage."
    source_quality: "reference entry"
    used_for: [basics, childhood, contribution, heritage, review]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Caroline Herschel; ed. Michael Hoskin"
    citation: "Herschel, Caroline. Caroline Herschel's Autobiographies. Ed. Michael Hoskin. Cambridge: Science History Publications, 2003, pp. 71–77. Excerpt: German History Intersections."
    url: "https://germanhistory-intersections.org/en/knowledge-and-education/ghis:document-154"
    accessed: 2026-10-24
    reliability_note: "Public excerpt of Hoskin edition (assistant-astronomer years, sweeper, injury). No religion or nature-cause language in the excerpt; full book not obtained."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, contribution]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "Caroline Herschel"
    citation: "Herschel, Caroline. Account of the Discovery of a New Comet. Philosophical Transactions of the Royal Society. Internet Archive philtrans00577081 (and related Phil. Trans. comet letters)."
    url: "https://archive.org/details/philtrans00577081"
    accessed: 2026-10-24
    reliability_note: "Public scientific letters on comet discovery; checked for locus/cause language — observational positions and announcements only; none found."
    source_quality: "primary / own words"
    used_for: [worldview, contribution]
---

# Caroline Herschel

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Caroline Lucretia Herschel (1750–1848), Hanover-born astronomer in England, discovered eight comets (1786–1797), indexed Flamsteed's observations (1798) and catalogued about 2,500 nebulae for her nephew John; she won the Astronomical Society's gold medal in 1828 [S1; S2; S5]. Letters show brief Christian devotion: Simeon's canticle, thanksgiving and prayer to "the Almighty", "as long as God pleases" [S3, pp. 235–236, 275]. Primary CHRIST at 0.5; A 0 at 0.5 (alt 1); B–E below threshold; mid_basin below threshold. Chart-moving NO.

## Life and work

Kept from schooling by her mother, she joined William in Bath in 1772, trained as a singer, and moved with him into astronomy, sweeping for comets and reducing his observations; after his death in 1822 she returned to Hanover [S1; S2; S5].

## Contribution and impact

Comets, the Flamsteed index and the nebula catalogue; a royal pension from 1787 [S1; S2; S5]. Phil. Trans. comet letters are observational announcements only [S7].

## Childhood and education

Protestant family line (Moravia → Saxony per Isaac's memo) [S3, pp. 1–2]; christened and confirmed in the Hanover garrison church per the editor [S3, p. 347]; she recalls the confirmation herself [S3, p. 17]; household drudgery; William taught her English and mathematics in Bath [S2; S5]. Funeral in the same church; buried beside her parents [S3, pp. 347, 351].

## Adult working worldview

Brief post-span private-letter devotion [S3, pp. 235–236, 275]; deepen found no astronomy–religion statement and no own-voice account of why the heavens move [S3; S6; S7].

## Heritage (context only)

Hanoverian musicians' family; Protestant Moravia ancestry; garrison-church rites [S3; S5]. Context only.

## Timing

First lasting contribution 1783, three nebulae, at 33 [S1]; first comet 1786, at 36 [S1]. A-bearing letters 1829/1835 after the span.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No geometric form; no circle.

## Open questions

- Full Hoskin Autobiographies / Discoverers; epitaph manuscript; in-span LIO stronger than letter closings.

## Research log

- 2026-10-02: Read Britannica and MacTutor; searched the full text of the 1876 Memoir (Internet Archive) and checked the cited pages on the page images.
- 2026-10-24: Deepen D1 — Memoir re-search (IA + Gutenberg #52923); Hoskin excerpt S6; Phil. Trans. S7; Wikipedia S5. Scores unchanged; chart NO.
