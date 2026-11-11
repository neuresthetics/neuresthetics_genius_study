---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA3)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 19c. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #177, F 3, rank 188). Needs: A UNKNOWN; B UNKNOWN; letters/own words on God/religion if any. Read: Reinthaler letter 9 Oct 1867 English (S5 Richmond faculty reprint; Wikipedia S4 cites Musgrave 1985 p. 80) — gladly omit 'German' for 'human'/'Menschen' and John 3:16, keep biblical lines as musician; Kalbeck Taufzeugnis St. Michaelis baptism 26 May 1833 (S6); Wikipedia EN dual bio (S4: Lutheran baptism/confirmation; Swafford agnostic/humanist; Dvořák 'believes in nothing'); Suk Mar 1896 Schopenhauer recollection via Beller-McKenna secondary trail (S4/S7) — reported speech after span. Do not code pantheism/religion from Requiem musical subject alone (standing rule). P47 source_quality on S1–S7. P50 dual bio S1+S4. primary_system UNKNOWN→BELOW_THRESHOLD (AGNOS/SECHUM candidates; no own-voice 'I am agnostic' / denial); A UNKNOWN→BELOW_THRESHOLD (Reinthaler is text-selection, not locus; Suk reported speech; P20 AGNOS-candidate no locus); B stays UNKNOWN (not a scientist; no nature-order); mid UNKNOWN→BELOW_THRESHOLD; not plotted. Chart-moving NO. No fallacy_catalog. No figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "AA3 audit fix (v8's call on the auditor's advice): Bremen 1868 gave all six movements then existing, so RQ-Z8-1 does not apply and the movement-5 reasoning is removed; span 1868 now 0.7; the 1869 Leipzig alternative is cited to Swafford's BSO programme note (S3, read in full). Swafford's 'skeptic and agnostic' added as a worldview lead only."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA3, order P32: F 3, rank 188). Source: Britannica, signed by Robert Simpson and Karl Geiringer (scholars edition, read in full). Lasting work: Ein deutsches Requiem, 'still considered one of the most significant works of 19th-century choral music'; dated by its 'first performance at Bremen on Good Friday, 1868' (premiere, P30 #1). Bremen gave 'the six then-existing movements' (BSO note, S3), so the premiere dates the work at 0.7; alternative 1869, 'the first performance of the complete seven-movement work' in Leipzig (S3). Worldview: no own words read. Britannica calls the Requiem 'a large, objective, nonreligious humane vision' and his 'essential quality is perhaps stoicism', describing the music, not a profession. primary_system UNKNOWN (leads SECHUM, CHRIST: biblical texts 'selected by the composer'); A UNKNOWN; not a scientist; C, D, E UNKNOWN; mid_basin UNKNOWN. Span 1868 at 0.7, age 35. Not plotted. Draft, not reviewed."}

identity:
  id: brahms-johannes
  display_name: "Johannes Brahms"
  roster:
    canonical_name: "Johannes Brahms"
    rank: 188
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: "core"
    field: "music"
    field_bucket: "music"
  full_name: {value: "Johannes Brahms", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S4, locator: "lead / infobox"}], how_known: "Britannica and Wikipedia agree (P50)."}
  native_name: {value: "Johannes Brahms", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S4, locator: "lead"}], how_known: "German name; Britannica and Wikipedia agree (P50)."}
  aliases: []

basics:
  birth:
    date: {value: "1833-05-07", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S4, locator: "infobox"}, {source: S6, locator: "Taufzeugnis (born 7 May 1833)"}], how_known: "Britannica, Wikipedia, and Kalbeck baptism extract agree (P50 / primary register)."}
    place: {value: "Hamburg", modern_name: "Hamburg, Germany", polity_then: "Free City of Hamburg (German Confederation)", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S4, locator: "infobox / Youth"}], how_known: "Britannica and Wikipedia agree (P50)."}
  death:
    date: {value: "1897-04-03", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S4, locator: "infobox"}], how_known: "Britannica and Wikipedia agree (P50)."}
    place: {value: "Vienna", modern_name: "Vienna, Austria", polity_then: "Austria-Hungary", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S4, locator: "infobox / Later Life"}], how_known: "Britannica and Wikipedia agree (P50)."}
  first_lasting_contribution_year: {value: 1868, certainty: 0.7, cites: [{source: S1, locator: "The young pianist and music director"}, {source: S3, locator: "Composition and premiere"}], how_known: "'first performance at Bremen on Good Friday, 1868' (S1); 'The first performance of the six then-existing movements' (S3); premiere (P30 #1). Alternative 1869: the fifth movement was added in May 1868 and 'The first performance of the complete seven-movement work took place in Leipzig on February 18, 1869' (S3)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "The young pianist and music director"}], how_known: "1868 or 1869, one bucket (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Germany (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "The young pianist and music director"}], how_known: "Vienna from 1863."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["German"], certainty: 0.7, cites: [{source: S1, locator: "The young pianist and music director"}], how_known: "German texts."}
  occupations: {value: ["composer", "pianist", "conductor"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S4, locator: "infobox"}], how_known: "Britannica; Wikipedia agrees."}

contribution:
  era_bucket: 19c
  fields: {value: ["music"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Ein deutsches Requiem (A German Requiem)", year: 1868, kind: "work", lasting: "'still considered one of the most significant works of 19th-century choral music' (S1)", certainty: 0.7, cites: [{source: S1, locator: "The young pianist and music director"}, {source: S3, locator: "Composition and premiere"}], how_known: "Britannica; premiere of the six then-existing movements, Bremen, Good Friday 1868 (S3); complete seven-movement work Leipzig 1869 (S3)."}
  evidence_of_impact:
    - {value: "'The great master of symphonic and sonata style in the second half of the 19th century'; the 'three great Bs'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Introduction; Maturity and fame"}], how_known: "Britannica."}
  major_works:
    - {value: "Symphony No. 1 in C Minor", year: 1876, kind: "composition", certainty: 0.7, cites: [{source: S1, locator: "Maturity and fame"}], how_known: "Britannica: 'completed in 1876 and first heard in the same year'; not called lasting."}
    - {value: "Symphony No. 4 in E Minor", year: 1885, kind: "composition", certainty: 0.5, cites: [{source: S1, locator: "Maturity and fame"}], how_known: "Britannica: 1884–85; premiere year not given."}
  honours:
    - {value: "Honorary degree, University of Breslau", year: 1879, kind: "award", certainty: 0.7, cites: [{source: S1, locator: "Maturity and fame"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "The great master of symphonic and sonata style in the second half of the 19th century (S1).", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Lutheran (Evangelisch-Lutherische Kirche; St. Michaelis parish, Hamburg)", certainty: 0.7, cites: [{source: S6, locator: "Taufzeugnis header and text"}, {source: S4, locator: "Requiem and personal beliefs"}], how_known: "Baptism register of the Evangelisch-Lutherische Kirche St. Michaelis (S6); Wikipedia cites Musgrave for confirmation at St. Michael's (S4)."}
  family_religious_practice: {value: "Infant baptism and later confirmation in the Lutheran Hauptkirche St. Michaelis, Hamburg", certainty: 0.7, cites: [{source: S6, locator: "full extract"}, {source: S4, locator: "Requiem and personal beliefs (baptised; confirmed at age fifteen)"}], how_known: "Primary baptism extract (S6); confirmation from Wikipedia citing Musgrave A Brahms Reader (S4) — confirmation register not fetched this pass."}
  parents_and_household:
    - {value: "Father Johann Jakob (Johann Jacob) Brahms, musician (Musicus; horn and double bass)", name: "Johann Jakob Brahms", role: "father", certainty: 1.0, cites: [{source: S1, locator: "The young pianist and music director"}, {source: S6, locator: "Taufzeugnis"}], how_known: "Britannica and baptism register."}
    - {value: "Mother Johanna Henrika Christiane Nissen (seamstress)", name: "Johanna Henrika Christiane Brahms (née Nissen)", role: "mother", certainty: 0.7, cites: [{source: S6, locator: "Taufzeugnis"}, {source: S4, locator: "Youth / Upbringing"}], how_known: "Baptism register names her; Wikipedia on family."}
  household_circumstances: {value: "Musical Hamburg household; early years in poorer Gängeviertel apartments (Wikipedia)", certainty: 0.7, cites: [{source: S4, locator: "Youth / Upbringing"}, {source: S1, locator: "The young pianist and music director ('impecunious')"}], how_known: "Britannica and Wikipedia."}
  schooling:
    - {value: "Piano with Otto Friedrich Willibald Cossel from about age seven, then with Eduard Marxsen", stage: "other", years: "c. 1840–1848", certainty: 0.7, cites: [{source: S1, locator: "The young pianist and music director"}, {source: S4, locator: "Youth / Training"}], how_known: "Britannica; Wikipedia agrees."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Eduard Marxsen (pianist/composer; conveyed Classical tradition)", certainty: 0.7, cites: [{source: S1, locator: "The young pianist and music director"}, {source: S4, locator: "Youth / Training"}], how_known: "Britannica and Wikipedia."}
  languages_in_childhood: {value: ["German"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Hamburg German family."}
  notable_events:
    - {value: "Baptized 26 May 1833 at St. Michaelis, Hamburg, by Pastor von Ahsen", year: "1833", certainty: 1.0, cites: [{source: S6, locator: "full extract"}], how_known: "Primary baptism-register extract printed in Kalbeck."}
    - {value: "Confirmed at age fifteen at St. Michael's Church, Hamburg (13 April 1848 tradition / hymnal date)", year: "1848", certainty: 0.7, cites: [{source: S4, locator: "Requiem and personal beliefs (Musgrave)"}], how_known: "Wikipedia citing Musgrave; confirmation register not fetched."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1868", certainty: 0.7, cites: [{source: S1, locator: "The young pianist and music director"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Lutheran by baptism and confirmation (St. Michaelis, Hamburg); adult church membership / practice not evidenced in sources read", years: "1833–", role: "baptized and confirmed Lutheran", certainty: 0.7, cites: [{source: S6, locator: "Taufzeugnis"}, {source: S4, locator: "Requiem and personal beliefs"}], how_known: "Heritage only — never a worldview code."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing on science and religion in the sources read."}
  primary_system:
    value: BELOW_THRESHOLD
    cites: [{source: S5, locator: "Brahms to Reinthaler, 9 Oct 1867"}, {source: S3, locator: "skeptic and agnostic / secular humanist paragraph"}, {source: S4, locator: "Requiem and personal beliefs"}]
    how_known: "Reinthaler letter is own-hand on Requiem text selection (universality; omit John 3:16), not a system self-label. Swafford (S3) and Wikipedia via Swafford (S4) call him agnostic/humanist without quoting an own-voice label. Suk Schopenhauer remark (S4/S7) is reported speech after the span. No listed code opened."
    note: "Candidates: AGNOS (Swafford 'skeptic and agnostic'; Suk recollection leans non-religious) and SECHUM (Swafford 'secular humanist'; Britannica 'nonreligious humane vision' of the Requiem — music description, not profession). CHRIST considered for biblical texts and Lutheran heritage — rejected as adult working code (heritage never a code; text selection deliberately omits Christocentric John 3:16). Do not code pantheism/religion from musical subject alone."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Leading candidate, not coded: Swafford/Wikipedia scholarly label; Suk Mar 1896 reported speech ('too much Schopenhauer… things appear differently'). No own-voice 'I am agnostic' or explicit suspension on God's existence (P19).", cites: [{source: S3, locator: "skeptic and agnostic paragraph"}, {source: S4, locator: "Requiem and personal beliefs"}, {source: S7, locator: "Suk / Beller-McKenna quotation"}]}
    - {code: SECHUM, reason: "Lead: Swafford 'secular humanist'; Britannica 'nonreligious humane vision' of the Requiem; Reinthaler wish to replace 'German' with 'human'/'Menschen'. No public humanist manifesto or own ethical-system label — keep candidate only.", cites: [{source: S3, locator: "secular humanist"}, {source: S1, locator: "Aims and achievements"}, {source: S5, locator: "9 Oct 1867"}]}
    - {code: CHRIST, reason: "Considered: Lutheran baptism/confirmation; biblical Requiem and Four Serious Songs texts. Rejected for adult working years: heritage never a code; Reinthaler consciously omits John 3:16; musical biblical subject alone does not open CHRIST.", cites: [{source: S6, locator: "Taufzeugnis"}, {source: S5, locator: "9 Oct 1867"}, {source: S1, locator: "Final years (Vier ernste Gesänge)"}]}
    - {code: ATHE, reason: "Rejected: Dvořák's 'he believes in nothing' is Dvořák's (or Suk-reported) words about Brahms, not Brahms's own denial; no positive naturalism in own words.", cites: [{source: S4, locator: "Requiem and personal beliefs"}]}
  lio_axes:
    A_locus:
      value: BELOW_THRESHOLD
      how_known: "Reinthaler letter (S5) explains Requiem text choices (omit 'German' / John 3:16; keep biblical lines as musician) — not a place/deny of a personal God. Suk Schopenhauer remark (S4/S7) is reported speech after span and does not locate God. Swafford agnostic label is scholarly reconstruction without own locus statement. P20: an agnostic with no stated locus view gets A BELOW_THRESHOLD; candidate status does not open a numeric score."
      note: "Do not score A from Requiem subject matter or biblical libretto alone (standing deepen rule / P30 musical texts). Named reading if forced: denial lean from deliberate Christocentric omission, still under 0.5 and withheld."
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); no own-words account of nature's law vs exception found. Musical architecture and Schopenhauer reading are not P16 nature-order claims."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing first-hand on judgement, afterlife, or reward and punishment as his view (P19). Requiem consolation texts are selected scripture, not a ledger profession."}
    D_authority: {value: UNKNOWN, how_known: "Nothing scored on revelation vs observation (P19). Reinthaler letter is about textual universality, not epistemic authority."}
    E_scope: {value: UNKNOWN, how_known: "Nothing on the world's order / favour for a group in events (P7, P19)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD (the P4 test needs A at certainty ≥ 0.7)."}
  statements:
    - text: "Concerning the text, I want to admit that I would gladly give up the \"German\" [in the title] and simply put \"human\" [Menschen] — also with full knowledge and consent go without passages like John 3:16. Yet I have now probably taken quite a lot, because I am a musician, because I could use it, because I cannot dispute or cross out a \"henceforth\" from my honorable poets."
      cites: [{source: S5, locator: "Brahms to Reinthaler, 9 Oct 1867 (full English)"}, {source: S4, locator: "Requiem and personal beliefs (Musgrave 1985 p. 80 citation)"}]
      date: "1867-10-09"
      context: "Private letter to conductor Karl Reinthaler declining to add explicitly Christological text (e.g. John 3:16 / saving death of Christ) to Ein deutsches Requiem before the Bremen performance. Own-hand on text selection for universality — not scored as A locus or system profession (musical libretto / text-choice; standing deepen rule)."
      axes: []
      kind: "private letter"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
    - text: "I have read too much Schopenhauer, and things appear much differently to me."
      cites: [{source: S7, locator: "Suk recollection via Beller-McKenna 1994a p. 191"}, {source: S4, locator: "Requiem and personal beliefs (Swafford / Dvořák trail)"}]
      date: "1896-03"
      context: "Josef Suk recalling a March 1896 Vienna conversation with Brahms and Dvořák on faith and religion (after the 1868 span). Wordings vary in secondary literature ('to be religious' vs 'things appear differently'). Reported speech — cannot open A or primary alone (§1 / P18). Dvořák's reported reaction ('he believes in nothing') is Dvořák's words about Brahms, not Brahms's."
      axes: []
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
  changes_over_life:
    - {value: "Lutheran baptism and confirmation in Hamburg to an adult stance scholars describe as skeptic/agnostic/humanist; Reinthaler 1867 shows deliberate non-Christocentric Requiem text choice during the span; Suk 1896 Schopenhauer remark is after-span reported speech — no dated own-voice conversion statement", year: "1833–1896", certainty: 0.5, cites: [{source: S6, locator: "Taufzeugnis"}, {source: S5, locator: "9 Oct 1867"}, {source: S3, locator: "skeptic and agnostic"}, {source: S7, locator: "Suk"}], how_known: "Coder's comparison across heritage, letter, and secondary recollection."}
  coder_notes: "Deepen D1: Reinthaler is the only first-hand religion-adjacent own words found; it governs libretto universality, not A. Avins Life and Letters and Musgrave A Brahms Reader physical volumes unread — English letter checked on Richmond faculty reprint (S5) and Wikipedia/Musgrave citation path (S4). Suk wording via Beller-McKenna secondary (S7); Loader 1998 not opened. Spurious Joachim 'no atheist composer' quote avoided. Four Serious Songs (1896) biblical texts not scored as CHRIST (same musical-subject rule). Chart stays unplotted."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German (Hamburg; father from Heide in Holstein)", certainty: 0.7, cites: [{source: S4, locator: "Youth / Upbringing"}, {source: S6, locator: "father gebürtig aus Heide"}], how_known: "Wikipedia and baptism register."}
  religious_heritage_by_birth: {value: "Lutheran", certainty: 0.7, cites: [{source: S6, locator: "Evangelisch-Lutherische Kirche / St. Michaelis"}, {source: S4, locator: "Requiem and personal beliefs"}], how_known: "Baptism register and Wikipedia/Musgrave."}
  baptism_or_initiation: {value: "Baptized 1833-05-26 at Hauptkirche St. Michaelis, Hamburg, by Pastor von Ahsen; sponsors Johann Brahms, Diederich Pilipp Detmering, Catharina Margaretha Stäcker", certainty: 1.0, cites: [{source: S6, locator: "full Taufzeugnis extract"}], how_known: "Primary baptism-register extract (Kalbeck Anhang)."}
  childhood_catechism: {value: "Confirmed at age fifteen at St. Michael's Church, Hamburg (Wikipedia citing Musgrave; hymnal tradition 13 April 1848)", certainty: 0.7, cites: [{source: S4, locator: "Requiem and personal beliefs"}], how_known: "Secondary; confirmation register not fetched this pass."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1868", certainty: 0.7, cites: [{source: S1, locator: "The young pianist and music director"}], how_known: "The one listed lasting work, dated by its premiere (P29, P30 #1); alternative 1869."}
  age_at_first_lasting_contribution: {value: 35, certainty: 0.7, cites: [{source: S1, locator: "Introduction; The young pianist and music director"}], how_known: "1868 − 1833 = 35 (P30 year difference); 36 on the 1869 alternative."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "Reinthaler 1867 is text-selection, not a scored LIO axis statement (P27). No axis scored at 3 or 4."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "No scored LIO values."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Primary and A remain BELOW_THRESHOLD; Reinthaler letter is during/near the Requiem premiere year but does not open codes."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Musical architecture and counterpoint, not geometric argument from definitions and axioms (S1).", certainty: 0.5, cites: [{source: S1, locator: "Aims and achievements"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "no", rationale: "Nothing identifying God with Nature; Reinthaler and Suk do not state a circle.", certainty: 0.5, cites: [{source: S5, locator: "9 Oct 1867"}, {source: S3, locator: "text"}], how_known: "Coder's reading."}
  reading: "As belief, not finding: form absent, circle absent. A and B do not test H1. The record does not place a chart point."
  notes: ""

institutions:
  - {value: "Gesellschaft der Musikfreunde, Vienna", role: "principal conductor", years: "1872–1875", kind: "employer", certainty: 0.7, cites: [{source: S1, locator: "The young pianist and music director; Maturity and fame"}], how_known: "Britannica."}
  - {value: "Wiener Singakademie", role: "conductor", years: "1863–1864", kind: "employer", certainty: 0.7, cites: [{source: S4, locator: "Maturity / Move to Vienna"}], how_known: "Wikipedia."}
collaborators:
  - {value: "Robert Schumann", relation: "mentor or employer", note: "1853 article launched him", certainty: 0.7, cites: [{source: S1, locator: "The young pianist and music director"}], how_known: "Britannica."}
  - {value: "Joseph Joachim", relation: "collaborator", note: "violinist", certainty: 0.7, cites: [{source: S1, locator: "The young pianist and music director"}], how_known: "Britannica."}
  - {value: "Clara Schumann", relation: "collaborator", note: "lifelong friend", certainty: 0.7, cites: [{source: S1, locator: "The young pianist and music director"}], how_known: "Britannica."}
  - {value: "Antonín Dvořák", relation: "collaborator", note: "Brahms advocated for him; Suk reports 1896 religion conversation", certainty: 0.7, cites: [{source: S1, locator: "The young pianist and music director"}, {source: S4, locator: "Requiem and personal beliefs"}], how_known: "Britannica; Wikipedia."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 188"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Reinthaler English checked on unofficial faculty web reprint (S5); Musgrave/Avins scholarly letter editions unread — letter fields capped accordingly."
    - "Suk Schopenhauer line is secondary recollection (Beller-McKenna / Wikipedia trail); wordings vary; after span."
    - "Swafford 'skeptic and agnostic' / 'secular humanist' is scholarly characterization without Brahms self-label."
    - "Confirmation details rest on Wikipedia citing Musgrave; confirmation register not fetched."
  open_questions:
    - "Avins Johannes Brahms: Life and Letters and Musgrave A Brahms Reader / The Music of Brahms for authoritative Reinthaler German/English and any further belief letters."
    - "Physical Swafford Johannes Brahms: A Biography for the agnostic/humanist claim's documentary basis beyond the BSO note."
    - "Suk primary memoir text (not only Beller-McKenna quotation) for exact 1896 wording."
    - "St. Michaelis confirmation register for 1848 entry."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Robert Simpson and Karl Geiringer"
    citation: "Simpson, Robert, and Karl Geiringer. 'Johannes Brahms.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/Johannes-Brahms/16167"
    url: "https://kids.britannica.com/scholars/article/Johannes-Brahms/16167"
    accessed: 2026-10-24
    reliability_note: "Signed article, read in full."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, timing, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [review]
  - id: S3
    type: secondary
    kind: "other"
    author: "Jan Swafford"
    citation: "Swafford, Jan. 'A German Requiem' (programme note). Boston Symphony Orchestra. https://www.bso.org/works/a-german-requiem"
    url: "https://www.bso.org/works/a-german-requiem"
    accessed: 2026-10-24
    reliability_note: "Signed orchestra programme note by Brahms's biographer, read in full. 'Skeptic and agnostic' / 'secular humanist' kept as scholarly lead, not own words."
    source_quality: "other"
    used_for: [basics, contribution, worldview, timing]
  - id: S4
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "Wikipedia. 'Johannes Brahms.' https://en.wikipedia.org/wiki/Johannes_Brahms"
    url: "https://en.wikipedia.org/wiki/Johannes_Brahms"
    accessed: 2026-10-24
    reliability_note: "P50 dual bio with Britannica. Used for Lutheran baptism/confirmation (cites Musgrave), Reinthaler paraphrase (cites Musgrave 1985), Swafford agnostic/humanist, Dvořák trail. Not used alone to open worldview codes."
    source_quality: "reference entry"
    used_for: [identity, basics, childhood, worldview, heritage, institutions, collaborators]
  - id: S5
    type: primary
    kind: "letter"
    author: "Johannes Brahms (English translation)"
    year: 1867
    citation: "Brahms to Karl Reinthaler, 9 October 1867. English on University of Richmond faculty page (jriehl Choral Music Creed). https://facultystaff.richmond.edu/~jriehl/local/Choral_Music_Creed/brahms.html — cf. Musgrave, The Music of Brahms (1985), p. 80 (via S4)."
    url: "https://facultystaff.richmond.edu/~jriehl/local/Choral_Music_Creed/brahms.html"
    accessed: 2026-10-24
    reliability_note: "Subject's letter in English web reprint; German original / Avins or Musgrave scholarly edition not checked this pass — unofficial web copy cap."
    source_quality: "unofficial web copy"
    used_for: [worldview]
  - id: S6
    type: primary
    kind: "archive record"
    author: "Evangelisch-Lutherische Kirche St. Michaelis, Hamburg (via Kalbeck)"
    year: 1833
    citation: "Taufzeugnis extract: Kalbeck, Max. Johannes Brahms, 4. Band, Anhang, 3. Taufzeugnis. Printed at Zeno.org. http://www.zeno.org/Musik/M/Kalbeck,+Max/Johannes+Brahms/4.+Band/Anhang/3.+Taufzeugnis"
    url: "http://www.zeno.org/Musik/M/Kalbeck,+Max/Johannes+Brahms/4.+Band/Anhang/3.+Taufzeugnis"
    accessed: 2026-10-24
    reliability_note: "Printed extract from the St. Michaelis baptism register (Jahrgang 1833 Nr. 494), certified 1901; primary document path for baptism."
    source_quality: "other"
    used_for: [basics, childhood, heritage, worldview]
  - id: S7
    type: secondary
    kind: "other"
    author: "Daniel Beller-McKenna (via FSU thesis quotation)"
    year: 1994
    citation: "Beller-McKenna, Daniel (1994a), as quoted in Florida State University thesis on Brahms Vier ernste Gesänge: Suk recollection — 'I have read too much Schopenhauer, and things appear much differently to me' (Beller-McKenna 1994a, p. 191). https://repository.lib.fsu.edu/islandora/object/fsu:254217"
    url: "https://repository.lib.fsu.edu/islandora/object/fsu:254217/datastream/PDF/view"
    accessed: 2026-10-24
    reliability_note: "Secondary quotation of secondary; Suk memoir not opened. Used only as reported-speech lead, not to score axes."
    source_quality: "scholarly reconstruction"
    used_for: [worldview]
---

## Summary

Johannes Brahms (1833–1897), German composer and pianist, lasting work *Ein deutsches Requiem* (Bremen premiere of the six then-existing movements, Good Friday 1868) [S1, S3]. Lutheran baptism St. Michaelis Hamburg [S6]. Deepen D1: Reinthaler letter 9 Oct 1867 on Requiem text (omit "German"/John 3:16 for human universality) [S5]; Suk 1896 Schopenhauer remark is after-span reported speech [S7]. primary_system **BELOW_THRESHOLD** (AGNOS/SECHUM candidates); **A BELOW**; **B UNKNOWN**; mid BELOW; **not plotted**. Chart-moving **NO**.

## Life and work

Born Hamburg 7 May 1833; died Vienna 3 April 1897 [S1, S4]. Piano training with Cossel and Marxsen; launched by Schumann 1853; settled in Vienna from the 1860s; conductor of the Singakademie and later the Gesellschaft der Musikfreunde [S1, S4].

## Contribution and impact

*A German Requiem*, Op. 45 — biblical texts selected by Brahms; premiere of six movements Bremen Good Friday 1868; complete seven-movement work Leipzig 1869 [S1, S3]. Britannica: among the most significant 19th-century choral works; "three great Bs" [S1].

## Childhood and education

Lutheran parish household; baptized 26 May 1833 St. Michaelis by Pastor von Ahsen [S6]; confirmed at fifteen at St. Michael's [S4]. Early piano with Cossel, then Marxsen [S1, S4].

## Adult working worldview

No own-voice system label or God locus found. Reinthaler letter (near span): gladly replace "German" with "human"/"Menschen" and omit John 3:16, keeping biblical lines as a musician [S5] — text selection, not A. Swafford: "skeptic and agnostic" / "secular humanist" [S3] — scholarly lead. Suk (Mar 1896): too much Schopenhauer, things appear differently [S7] — reported speech after span. Coding: primary **BELOW_THRESHOLD** (AGNOS/SECHUM candidates; CHRIST rejected as adult code); **A BELOW_THRESHOLD** (P20); **B UNKNOWN** (not a scientist); C/D/E UNKNOWN; mid BELOW. Do not code religion from Requiem subject alone.

## Heritage (context only)

Lutheran by baptism and confirmation (Hamburg St. Michaelis) [S6, S4]. German (Holstein father) [S4, S6]. Heritage never a worldview code.

## Timing

Major work 1868, age 35 [S1, S3]. Reinthaler 1867 is near-span text-choice; no scored LIO axis at ≥3.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form absent; circle absent. Unplotted (A BELOW, B UNKNOWN).

## Open questions

- Avins / Musgrave letter editions for authoritative Reinthaler text.
- Physical Swafford biography for documentary basis of agnostic/humanist claim.
- Suk primary memoir wording.
- Confirmation register 1848.

## Research log

- 2026-10-24 (deepen D1, queue #177): Reinthaler English (S5); Kalbeck Taufzeugnis (S6); Wikipedia dual bio (S4); Suk via Beller-McKenna (S7); re-read Britannica and Swafford BSO note. P47 on S1–S7. primary/A/mid → BELOW_THRESHOLD; B UNKNOWN; chart-moving NO. No fallacy_catalog. No figures/.
- 2026-10-19: AA3 audit fix (v8's call on the auditor's advice): Bremen 1868 gave all six movements then existing, so RQ-Z8-1 does not apply and the movement-5 reasoning is removed; span 1868 now 0.7; the 1869 Leipzig alternative is cited to Swafford's BSO programme note (S3, read in full). Swafford's 'skeptic and agnostic' added as a worldview lead only.
- 2026-10-19: Read Britannica (Simpson, Geiringer); BSO programme note (Swafford).
