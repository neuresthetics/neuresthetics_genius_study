---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z10; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #167, F 3, rank 177). Goals: any own-voice religion/locus/nature; keep silence if none; do not force plot. Hunt: Jewish birth family (father Emil Kiesler Galician-Jewish; mother Gertrud Lichtwitz Hungarian-Jewish, Shearer/Wiki: mother converted to Catholicism and raised Hedy Christian though unbaptized); NDB Konfession jüdisch, seit 1933 römisch-katholisch + Mandl veranlasste Konversion; JWA Barton: converted to Christianity to marry Mandl 1933, remained silent about Jewish identity; Dean/Bombshell letter (via Oregon Jewish Life / JWeekly): mother 1938 Catholic papers, Hedy 'I don’t want to be identified as a Jew in Hollywood' — concealment/identity, not creed; EBSCO Lewis secondary: did not renounce Judaism but did not practice. Ecstasy and Me destiny/afterlife quote left lead only (disowned ≤0.5 P29). No first-hand religion/locus/nature scored. primary/A/B/mid stay UNKNOWN. Heritage + nominal_affiliations + changes_over_life filled (heritage ≠ worldview; membership ≠ ideology). Chart-moving NO. P47 source_quality; P48; P50 Wikipedia. No fallacy_catalog; no figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z10 audit fixes (FAIL, P13; v8's calls on the auditor's advice): 'achieved recognition as a noted inventor' is not a lasting claim about the device, and its later use is only in the Top Questions box (P26), so no lasting work is supported; the patent moves to major_works, dated by its 10 June 1941 filing (formal submission, P30 #1). Span 1942 -> UNKNOWN; age and era UNKNOWN. Not plotted."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z10, order P32: F 3, rank 177). Basics from Britannica (Britannica Editors; body only, the Top Questions box not cited, P26); the patent from Google Patents (US 2,292,387, 'Secret communication system', filed 1941-06-10, granted 1942-08-11, inventors Hedy Kiesler Markey and George Antheil). No own-voice statement on religion or nature read. Not a scientist (invention, P33). All worldview fields UNKNOWN. Span 1942 (patent grant), age 29 (birth 1913/14; earlier year used, as for Chaucer). Not plotted. Draft, not reviewed."}

identity:
  id: lamarr-hedy
  display_name: "Hedy Lamarr"
  roster:
    canonical_name: "Hedy Lamarr"
    rank: 177
    F: 3
    models: [Gemini, GPT, Grok]
    band: "core (3–4)"
    status: "core"
    field: "invention"
    field_bucket: "invention / engineering"
  full_name: {value: "Hedy Lamarr", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lead"}], how_known: "Britannica + Wikipedia."}
  native_name: {value: "Hedwig Eva Maria Kiesler", certainty: 0.7, cites: [{source: S1, locator: "heading"}, {source: S5, locator: "Namensvariante"}], how_known: "Britannica; NDB."}
  aliases:
    - {name: "Hedy-Lamarr", kind: "roster alias"}
    - {name: "Lamarr-Hedy", kind: "roster alias"}
    - {name: "Hedwig Eva Maria Kiesler", kind: "birth name"}
    - {name: "Hedy Kiesler Markey", kind: "other"}

basics:
  birth:
    date: {value: "1913-11-09", certainty: 0.5, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "9. November 1914"}], how_known: "Britannica: 'November 9, 1913/14'; NDB and JWA prefer 1914. Year left uncertain; earlier year kept as Z10."}
    place: {value: "Vienna", modern_name: "Vienna, Austria", polity_then: "Austria-Hungary", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "2000-01-19", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "19. Januar 2000"}], how_known: "Two sources."}
    place: {value: "near Orlando, Florida", modern_name: "Casselberry / near Orlando, Florida, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "Casselberry"}], how_known: "Britannica; NDB Casselberry."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "No lasting work supported (P13): Britannica's body says only that she 'achieved recognition as a noted inventor'; the device's later use is in the Top Questions box (P26). Z10 audit."}
  era_bucket: {value: UNKNOWN, how_known: "No first lasting year (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Austria (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Hollywood from 1937."}
  sex_as_recorded: {value: "female", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English", "German"], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Inferred."}
  occupations: {value: ["film actress", "inventor"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["radio communications"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions: []
  evidence_of_impact:
    - {value: "Recognized as a noted inventor years after her screen career", kind: "other", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Frequency-hopping 'secret communication system' (with George Antheil), US patent 2,292,387", year: 1941, kind: "device", certainty: 0.7, cites: [{source: S2, locator: "front page"}], how_known: "Filed 10 June 1941 (formal submission, the P30 #1 dating event), granted 11 August 1942. Not a supported lasting contribution (P13, P26)."}
    - {value: "Algiers", year: 1938, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
    - {value: "Samson and Delilah", year: 1949, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  honours: []
  definition_fit: {value: "arguable", rationale: "Film star; inventor recognized late (S1).", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Jewish birth family (both parents of Jewish descent); mother Gertrud converted to Catholicism and raised Hedy as a Christian (Shearer via Wikipedia), though Hedy was not baptized as a child", certainty: 0.7, cites: [{source: S4, locator: "Early life: mother converted… not baptized"}, {source: S5, locator: "Genealogie; jüdischen Bankiersfamilie"}, {source: S6, locator: "Jewish identity"}], how_known: "Wikipedia summarizing Shearer + NDB genealogy + JWA. Heritage/practice, not a worldview code."}
  family_religious_practice: {value: "Mother described as practicing Christian after her conversion; Hedy raised Christian but unbaptized in childhood; Jewish communal heritage kept silent later", certainty: 0.5, cites: [{source: S4, locator: "Early life"}, {source: S6, locator: "silence about Jewish identity"}], how_known: "Secondary biographies; no household liturgy primary."}
  parents_and_household:
    - {value: "Emil Kiesler (born Samuel Aron Kiesler), Viennese banker; Galician-Jewish family from Lemberg", role: "father", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S5, locator: "Emil Kiesler"}], how_known: "Britannica + NDB."}
    - {value: "Gertrud (Trude) Kiesler née Lichtwitz, concert pianist; upper-class Hungarian-Jewish family; converted to Catholicism", role: "mother", certainty: 0.7, cites: [{source: S4, locator: "Early life"}, {source: S5, locator: "Gertrud… Lichtwitz"}, {source: S8, locator: "mother converted 1938 / letter"}], how_known: "Wikipedia/Shearer + NDB; Dean letter context for 1938 papers."}
  household_circumstances: {value: "Prosperous Viennese banker's household (Wien-Döbling)", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S5, locator: "Wien-Döbling"}], how_known: "Britannica + NDB."}
  schooling:
    - {value: "Private tutors; Mädchen-Mittelschule / boarding school (left without completion 1929); Döbling-Akademie art and design; Reinhardt theatre contacts", stage: "grammar or secondary school", years: "c.1920–1930", certainty: 0.5, cites: [{source: S1, locator: "text"}, {source: S5, locator: "Schulbesuch"}], how_known: "Britannica + NDB table."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["German"], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Vienna; inferred."}
  notable_events:
    - {value: "Raised Christian by Catholic-convert mother but not baptized as a child (Shearer via Wikipedia)", certainty: 0.5, cites: [{source: S4, locator: "Early life"}], how_known: "Secondary biography via Wikipedia; Shearer pages not re-checked this pass."}

worldview:
  unit: "adult working worldview"
  working_years: {value: UNKNOWN, how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Jewish by birth (parents of Jewish descent); childhood Christian rearing without baptism (Shearer); Catholic conversion arranged for 1933 marriage to Fritz Mandl (Karlskirche wedding; NDB Konfession seit 1933 römisch-katholisch); Hollywood-era concealment of Jewish identity (Dean letter to mother, 1938 Catholic papers); later insisted to children she was not Jewish (Bombshell)", certainty: 0.7, cites: [{source: S5, locator: "Konfession; Mandl veranlasste Konversion"}, {source: S6, locator: "converted… Mandl"}, {source: S8, locator: "letter quote"}, {source: S4, locator: "Early life"}], how_known: "Public secondary consensus + Dean interview report of a letter. Membership/concealment is not a worldview code (JUDA.md / CHRIST.md; heritage ≠ ideology)."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No own words linking invention to religion or nature-order read. Circulating Ecstasy and Me destiny/afterlife lines left as leads (disowned memoir, P29)."}
  primary_system: {value: UNKNOWN, certainty: 0.5, cites: [{source: S7, locator: "Early Life: did not practice"}], how_known: "No scored own-voice creed. Jewish heritage and Mandl-arranged Catholic conversion are affiliation/heritage only (not JUDA or CHRIST). EBSCO (S7) says she did not renounce Judaism but did not practice — secondary paraphrase only, does not score JUDA. Silence kept."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: JUDA, reason: "Weighed and rejected as ideology code. Jewish birth and communal heritage are clear (S4–S6) but JUDA.md / CODING_GUIDE: heritage is never a code. EBSCO (S7) says she did not practice; she concealed Jewish identity in Hollywood and told children she was not Jewish. No own-voice Jewish theology read.", cites: [{source: S7, locator: "Early Life"}, {source: S6, locator: "silent about her Jewish identity"}]}
    - {code: CHRIST, reason: "Weighed and rejected. Childhood Christian rearing (unbaptized) and 1933 Mandl-arranged Catholic conversion are public practice/affiliation (membership ≠ ideology, CHRIST.md). No written_profession of Christian doctrine found; conversion was marriage-arranged per NDB/JWA. Not scored."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing first-hand on God/locus read (P19). Destiny/afterlife lines attributed to disowned Ecstasy and Me left unscored (P29 ≤0.5; no plot force)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P33: the device is an invention); no statement on law-or-exception nature read."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "A and B are UNKNOWN (P19). Do not force plot."}
  statements: []
  changes_over_life:
    - {value: "1933: Catholic conversion from Judaism arranged by first husband Fritz Mandl; married at Karlskirche (NDB; JWA). Affiliation/practice shift — not scored as CHRIST written_profession.", year: 1933, certainty: 0.7, cites: [{source: S5, locator: "veranlasste… Konversion"}, {source: S6, locator: "converted to Christianity to marry… Mandl"}, {source: S4, locator: "married Mandl at the Karlskirche"}], how_known: "NDB + JWA + Wikipedia."}
    - {value: "c.1938 Hollywood concealment: letter asking mother to convert to Catholicism so Hedy would not 'be identified as a Jew in Hollywood' (Dean / Bombshell, reported in Oregon Jewish Life and JWeekly). Identity politics / studio pressure — not a creed statement for A or primary_system.", year: 1938, certainty: 0.5, cites: [{source: S8, locator: "Please do this for me…"}, {source: S6, locator: "silent about her Jewish identity"}], how_known: "Director interview report of a letter; letter itself not imaged this pass."}
  coder_notes: "Deepen D1 (#167): heritage and Mandl conversion filled; primary/A/B left UNKNOWN (silence). Ecstasy and Me disowned — destiny/afterlife quotes ≤0.5 lead only (P29). Interviews and Shearer 2010 still leads for any real own-voice religion/locus. Chart-moving NO. Do not touch figures/. No fallacy_catalog."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Austrian; father Galician-Jewish (Lemberg); mother Hungarian-Jewish (Budapest Lichtwitz)", certainty: 0.7, cites: [{source: S4, locator: "Early life"}, {source: S5, locator: "Genealogie"}, {source: S6, locator: "Jewish identity"}], how_known: "Wikipedia + NDB + JWA."}
  religious_heritage_by_birth: {value: "Jewish by birth family; mother Catholic convert who raised Hedy as a Christian (unbaptized in childhood per Shearer); Hedy's own 1933 Catholic conversion for Mandl marriage", certainty: 0.7, cites: [{source: S4, locator: "Early life"}, {source: S5, locator: "Konfession jüdisch, seit 1933 römisch-katholisch"}, {source: S6, locator: "converted… Mandl"}], how_known: "Three secondary accounts. Not a worldview code."}
  baptism_or_initiation: {value: "Not baptized as a child (Shearer via Wikipedia). Catholic conversion 1933 for marriage to Mandl (NDB; JWA). Mother's 1938 Catholic papers per Dean letter report.", certainty: 0.5, cites: [{source: S4, locator: "not baptized"}, {source: S5, locator: "seit 1933 römisch-katholisch"}, {source: S8, locator: "mother converted 1938"}], how_known: "Secondary; baptismal register unread."}
  childhood_catechism: {value: UNKNOWN, how_known: "Christian rearing asserted by Shearer; specific catechism not read."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "No supported lasting work (P13; Z10 audit). The patent would date to its 1941 filing (P30 #1) if a source called it lasting."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "No first lasting year."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None scored. Concealment letter is identity, not locus/nature."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "No scored adult creed; patent year itself unsupported as lasting (P13)."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Device invention (S1, S2).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No Lane B data. Heritage and Hollywood concealment do not supply A or B."
  notes: ""

institutions:
  - {value: "Metro-Goldwyn-Mayer", role: "contract actress", years: "1938–1945", kind: "employer", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
collaborators:
  - {value: "George Antheil", relation: "collaborator", note: "co-inventor", certainty: 0.7, cites: [{source: S2, locator: "front page"}], how_known: "Patent."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 177"}], how_known: "Study roster."}
  controversies:
    - {value: "Ecstasy and Me (1966) ghostwritten autobiography disowned; she sued collaborators — do not code worldview from it without care (P29 ≤0.5).", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
    - {value: "Public silence / denial of Jewish identity vs documented Jewish birth and 1933 Catholic conversion — heritage dispute, not a scored axis.", certainty: 0.5, cites: [{source: S6, locator: "silent"}, {source: S8, locator: "letter"}], how_known: "JWA + Dean interview."}
  data_quality_flags:
    - "No scored own-voice religion, locus, or nature statement."
    - "Shearer 2010 and Dean letter cited via secondary report; pages/letter not imaged."
    - "Ecstasy and Me disowned — circulating destiny quotes left as leads."
  open_questions:
    - "Primary text of the mother-conversion letter (Bombshell archive)."
    - "Shearer 2010 pages on childhood Christian rearing / baptism (vs Wikipedia summary)."
    - "Any non-disowned interview with religion, God, afterlife, or nature-order."
    - "Church register for 1933 Catholic conversion / Karlskirche marriage."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Britannica Editors"
    citation: "'Hedy Lamarr.' Encyclopaedia Britannica. https://www.britannica.com/biography/Hedy-Lamarr"
    url: "https://www.britannica.com/biography/Hedy-Lamarr"
    accessed: 2026-10-19
    reliability_note: "Unsigned article; body cited, question boxes not used (P26)."
    used_for: [identity, basics, contribution, childhood, timing, institutions, review]
    source_quality: "reference entry"
  - id: S2
    type: primary
    kind: "archive record"
    author: "Hedy Kiesler Markey and George Antheil"
    citation: "Markey, Hedy Kiesler, and George Antheil. 'Secret communication system.' US Patent 2,292,387, filed 10 June 1941, granted 11 August 1942. Google Patents. https://patents.google.com/patent/US2292387A/en"
    url: "https://patents.google.com/patent/US2292387A/en"
    accessed: 2026-10-19
    reliability_note: "Patent record (dates and inventors read)."
    used_for: [basics, contribution, timing, collaborators]
    source_quality: "primary / own words"
  - id: S3
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [review]
    source_quality: "study roster"
  - id: S4
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "Wikipedia. 'Hedy Lamarr' (English). Early life (mother Catholic convert; Hedy raised Christian, not baptized; Karlskirche marriage), citing Shearer, Beautiful: The Life of Hedy Lamarr (2010)."
    url: "https://en.wikipedia.org/wiki/Hedy_Lamarr"
    accessed: 2026-10-24
    reliability_note: "P50 Wikipedia allowed as dual-bio / lead pointer; Shearer pages not re-checked this pass."
    used_for: [identity, childhood, heritage, worldview, review]
    source_quality: "reference entry"
  - id: S5
    type: secondary
    kind: "encyclopedia"
    author: "NDB-online / Deutsche Biographie"
    citation: "Deutsche Biographie (NDB-online). 'Lamarr, Hedy.' https://www.deutsche-biographie.de/ (PDF dbo090250). Konfession jüdisch, seit 1933 römisch-katholisch; Mandl veranlasste Konversion; genealogy."
    url: "https://www.deutsche-biographie.de/sfz162159.html"
    accessed: 2026-10-24
    reliability_note: "Signed NDB-online article; PDF text read."
    used_for: [identity, basics, childhood, heritage, worldview]
    source_quality: "reference entry"
  - id: S6
    type: secondary
    kind: "encyclopedia"
    author: "Ruth Barton"
    citation: "Barton, Ruth. 'Hedy Lamarr.' Shalvi/Hyman Encyclopedia of Jewish Women. Jewish Women's Archive, 23 June 2021. https://jwa.org/encyclopedia/article/lamarr-hedy"
    url: "https://jwa.org/encyclopedia/article/lamarr-hedy"
    accessed: 2026-10-24
    reliability_note: "Signed encyclopedia article; silence on Jewish identity; Mandl conversion."
    used_for: [childhood, heritage, worldview, review]
    source_quality: "reference entry"
  - id: S7
    type: tertiary
    kind: "encyclopedia"
    author: "Lewis, Norma"
    citation: "Lewis, Norma. 'Hedy Lamarr.' EBSCO Research Starters (biography). https://www.ebsco.com/research-starters/biography/hedy-lamarr/"
    url: "https://www.ebsco.com/research-starters/biography/hedy-lamarr/"
    accessed: 2026-10-24
    reliability_note: "Unsigned/reference starter; 'did not renounce… did not practice' is secondary paraphrase — not used to score JUDA."
    used_for: [childhood, worldview]
    source_quality: "reference entry"
  - id: S8
    type: secondary
    kind: "other"
    author: "Michael Fox (reporting Alexandra Dean / Bombshell)"
    citation: "Fox, Michael. 'To Hedy Lamarr, beauty was only skin deep.' Oregon Jewish Life, 26 April 2018 (same reporting also in JWeekly, 27 Feb 2018). Dean quotes Lamarr letter: 'Please do this for me, because I don’t want to be identified as a Jew in Hollywood.'"
    url: "https://orjewishlife.com/14098-2/"
    accessed: 2026-10-24
    reliability_note: "Journalist interview with documentary director; letter itself not imaged. Used for concealment/heritage only, not creed scores."
    used_for: [heritage, worldview, review]
    source_quality: "newspaper interview"
---

## Summary

Hedy Lamarr (1913/14–2000), film star and inventor [S1]. Deepen D1: Jewish heritage and Mandl-era Catholic conversion documented; no scored own-voice religion, locus, or nature. primary / A / B / mid UNKNOWN. Not plotted.

## Life and work

Vienna Jewish banker's daughter; Hollywood from 1937 [S1, S5]. Frequency-hopping patent with Antheil filed 1941 [S2] — not supported as lasting (P13).

## Contribution and impact

US patent 2,292,387 [S2]. Screen career Algiers, Samson and Delilah [S1].

## Childhood and education

Jewish birth family; mother Catholic convert; raised Christian but unbaptized (Shearer via S4). Private tutors; Reinhardt contacts [S1, S5].

## Adult working worldview

No scored own-voice creed, locus, or nature. 1933 Mandl-arranged Catholic conversion and Hollywood concealment of Jewish identity are affiliation/heritage only (not JUDA or CHRIST). Ecstasy and Me destiny lines left as leads (disowned, P29).

## Heritage (context only)

Jewish communal heritage (father Galician-Jewish; mother Hungarian-Jewish). Childhood Christian rearing; 1933 Catholic conversion for Mandl marriage; 1938 mother-conversion letter for Hollywood non-identification as a Jew [S4–S6, S8]. Never a worldview code.

## Timing

UNKNOWN (no supported lasting work).

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Primary of Dean/Bombshell mother-conversion letter.
- Shearer 2010 pages vs Wikipedia summary.
- Non-disowned interview on religion / nature.

## Research log

- 2026-10-19: Read Britannica; patent record.
- 2026-10-24 (D1): Wikipedia EN (Shearer via Early life); NDB-online PDF; JWA Barton; EBSCO Lewis; Oregon Jewish Life / JWeekly Dean letter report; Ecstasy and Me destiny quotes left unscored; no figures/.
