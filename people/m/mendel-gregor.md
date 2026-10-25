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
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #165, F 3, rank 174). Goals: open A if primary sermon/letters allow; corroborate CHRIST/B; do not force plot without A. Hunt: Orel/Zumkeller Easter Predigtskizze still only as secondary (Der Imkerfreund 1972 / Graney PDF / Wikiquote from 1970 Brno symposium; Folia Mendeliana cited on teaching sites but volumes unread). Undated; Richter/ldysinger place it in abbot/latter years → after 1865 span. Standing rule: do not score A from undated after-span secondary sermon quotes without primary check → A stays UNKNOWN. Lebenslauf 17 Apr 1850 (Mrs Hugo Iltis tr.; ldysinger / Orel quotations): 'His circumstances decided his vocational choice' — own words on economic entry (corroborates BELOW alt; does not reverse CHRIST office+faith reconstruction). Nägeli letters 1866–1873 (Piternick tr., Genetics 1950 / ESP PDF of Correns 1905): 3 July 1870 — Hieracium vs Pisum 'manifestation of a higher, more fundamental, law'; 27 Sept 1870 — Hieracium 'exception' to Gärtner pollen claim 'must find a natural explanation' (anomaly in florets, not a no-miracle / exceptionless-nature claim). B stays 3 @0.5 alt 4 (P35 not lifted to 4); basis → written_profession; support corroborated (Versuche + Nägeli). CHRIST stays @0.5 scholarly_reconstruction (Richter + office; Iltis economic motive now tied to Lebenslauf). E UNKNOWN→BELOW_THRESHOLD (P19 scientist). mid UNKNOWN (no A). Chart-moving NO. P47 source_quality; P48; P49; P50 Wikipedia. No fallacy_catalog; no figures/ (parent refreshes per Jason t223u). Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z10 audit fix (FAIL; v8's call on the auditor's advice, P30 #1): dated by the public readings of 8 February and 8 March 1865 (Sitzungs-Berichte of the same volume), not the 1866 printing. Span 1866 -> 1865, age 44 -> 43. Not plotted."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z10, order P32: F 3, rank 174). Basics from Britannica (Robert Olby, signed; body, not the Top Questions box); the paper from its printing (Verhandlungen des naturforschenden Vereines in Brünn IV, für das Jahr 1865, Brünn 1866, pp. 3–47; Deutsches Textarchiv). Worldview: Augustinian friar, priest (ordained 1846) and abbot (1868); Richter (2015, journal article) says he 'was deeply rooted in his Christian faith' and cites surviving sermon outlines from his later years. The sermon text itself was seen only as a secondary quotation (Graney, Vatican Observatory, from Der Imkerfreund 1972), V3, so it is a lead, not a scoring statement. primary_system CHRIST (0.5, scholarly_reconstruction; alt BELOW_THRESHOLD); A UNKNOWN (lead 1); scientist (laws of heredity: testable claims about organisms), so B 3 at 0.5 from working science, alt 4 (P24, P35); C, D, E UNKNOWN; mid_basin UNKNOWN (A UNKNOWN). Span 1866, age 44. Not plotted (no A). Draft, not reviewed."}

identity:
  id: mendel-gregor
  display_name: "Gregor Mendel"
  roster:
    canonical_name: "Gregor Mendel"
    rank: 174
    F: 3
    models: [Claude, Gemini, Grok]
    band: "core (3–4)"
    status: "core"
    field: "biology"
    field_bucket: "biology / life science"
  full_name: {value: "Gregor Johann Mendel", certainty: 0.7, cites: [{source: S1, locator: "heading"}, {source: S6, locator: "lead"}], how_known: "Britannica + Wikipedia: born Johann Mendel; 'Gregor' given on entering the Augustinian order."}
  native_name: {value: "Gregor Johann Mendel", certainty: 0.7, cites: [{source: S1, locator: "heading"}], how_known: "Britannica."}
  aliases:
    - {name: "Mendel-Gregor", kind: "roster alias"}
    - {name: "Johann Mendel", kind: "birth name"}
    - {name: "Gregor", kind: "religious name"}

basics:
  birth:
    date: {value: "1822-07-20", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "infobox"}], how_known: "Two sources (baptism sometimes given as 22 July)."}
    place: {value: "Heinzendorf, Silesia", modern_name: "Hynčice, Czech Republic", polity_then: "Austrian Empire", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "infobox"}], how_known: "Two sources."}
  death:
    date: {value: "1884-01-06", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "infobox"}], how_known: "Two sources."}
    place: {value: "Brünn", modern_name: "Brno, Czech Republic", polity_then: "Austria-Hungary", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "infobox"}], how_known: "Two sources."}
  first_lasting_contribution_year: {value: 1865, certainty: 0.7, cites: [{source: S2, locator: "Inhalts-Verzeichniss (Sitzungs-Berichte, 8 February and 8 March 1865); p. 3"}], how_known: "Versuche über Pflanzen-Hybriden was read in public at the society's sessions of 8 February and 8 March 1865 (listed in the volume's Sitzungs-Berichte; 'Vorgelegt in den Sitzungen vom 8. Februar und 8. März 1865', p. 3); a public reading is the P30 #1 dating event, earlier than the 1866 printing (Z10 audit)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S2, locator: "p. 3"}], how_known: "1865 (P2)."}
  region_of_birth: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Czech Republic (P3)."}
  region_of_work: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "Education and early career"}], how_known: "Brünn (Brno), Moravia."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["German"], certainty: 0.7, cites: [{source: S2, locator: "p. 3"}], how_known: "German text."}
  occupations: {value: ["botanist", "teacher", "Augustinian friar and priest", "abbot"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["genetics", "botany"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Laws of heredity from pea hybrids (Mendelism)", year: 1865, kind: "law or principle", lasting: "'the first person to lay the mathematical foundation of the science of genetics, in what came to be called Mendelism' (S1, body)", certainty: 0.7, cites: [{source: S1, locator: "opening; Experimental period"}], how_known: "Britannica body; dated by the 1865 public readings (S2, p. 3; P30 #1)."}
  evidence_of_impact:
    - {value: "Mendelism; the law of independent assortment named by his successors", kind: "named after them", certainty: 0.7, cites: [{source: S1, locator: "opening; Experimental period"}], how_known: "Britannica."}
  major_works:
    - {value: "Versuche über Pflanzen-Hybriden", year: 1866, kind: "paper or paper series", certainty: 0.7, cites: [{source: S2, locator: "pp. 3–47"}], how_known: "The printing (read 1865)."}
    - {value: "Ueber einige aus künstlicher Befruchtung gewonnenen Hieracium-Bastarde", year: 1869, kind: "paper or paper series", certainty: 0.7, cites: [{source: S8, locator: "1869 paper"}, {source: S7, locator: "letters 1866–1873"}], how_known: "Hieracium report; context for Nägeli letters."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founder of the mathematical science of genetics (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Catholic (German-speaking Silesian peasant family)", certainty: 0.7, cites: [{source: S3, locator: "deeply religious peasant family"}, {source: S6, locator: "Early life"}], how_known: "Richter + Wikipedia."}
  family_religious_practice: {value: "Household piety (Richter: tile with Holy Trinity / 'Dein Wille geschehe')", certainty: 0.5, cites: [{source: S3, locator: "opening anecdote"}], how_known: "Family remembrance via Richter; not independently verified this pass."}
  parents_and_household:
    - {value: "Father, Anton Mendel, small farmer", role: "father", certainty: 0.7, cites: [{source: S1, locator: "Education and early career"}, {source: S5, locator: "Lebenslauf"}], how_known: "Britannica + own Lebenslauf."}
    - {value: "Mother, Rosine (née Schwirtlich) Mendel", role: "mother", certainty: 0.7, cites: [{source: S6, locator: "Early life"}], how_known: "Wikipedia."}
    - {value: "Sister Theresia gave up dowry money to support his studies", role: "family", certainty: 0.7, cites: [{source: S6, locator: "Early life"}, {source: S5, locator: "context"}], how_known: "Two sources."}
  household_circumstances: {value: "Small farm; successive disasters left him supporting himself by tutoring from age sixteen", certainty: 0.7, cites: [{source: S5, locator: "Lebenslauf"}], how_known: "Own 1850 Lebenslauf."}
  schooling:
    - {value: "Village school, Heinzendorf; Piarist college, Leipnik", stage: "elementary school", years: "before 1834", certainty: 0.7, cites: [{source: S5, locator: "Lebenslauf"}], how_known: "Own Lebenslauf."}
    - {value: "Imperial Royal Gymnasium, Troppau (Opava)", stage: "grammar or secondary school", years: "1834–1840", certainty: 0.7, cites: [{source: S5, locator: "Lebenslauf"}, {source: S6, locator: "Early life"}], how_known: "Two sources."}
    - {value: "Philosophical Institute, University of Olmütz (Olomouc)", stage: "university", years: "1840–1843", certainty: 0.7, cites: [{source: S5, locator: "Lebenslauf"}, {source: S1, locator: "Education and early career"}], how_known: "Two sources."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure:
    - {value: "Monastery botanical and mineralogical collection; courses in agriculture, pomiculture, wine-growing (Brünn, 1846)", certainty: 0.7, cites: [{source: S5, locator: "Lebenslauf"}], how_known: "Own Lebenslauf."}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["German"], certainty: 0.5, cites: [{source: S6, locator: "Early life"}], how_known: "German-speaking family (Wikipedia)."}
  notable_events:
    - {value: "Entered Augustinian monastery of St Thomas, Altbrünn, citing freedom from 'bitter struggle for existence' (Lebenslauf)", year: 1843, certainty: 0.7, cites: [{source: S5, locator: "Lebenslauf"}], how_known: "Own words."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1865", certainty: 0.7, cites: [{source: S2, locator: "p. 3"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Augustinian Order (OSA); ordained priest 1846; abbot of St Thomas, Altbrünn from 1868", certainty: 0.7, cites: [{source: S1, locator: "Education and early career"}, {source: S6, locator: "infobox / Academic career"}], how_known: "Public office and Britannica/Wikipedia."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No systematic science-vs-religion essay read. Easter Predigtskizze (lead) unites Natur und Übernatur in a grace metaphor — not scored as a science-religion profession (undated after-span secondary)."}
  primary_system:
    value: CHRIST
    basis: scholarly_reconstruction
    certainty: 0.5
    cites: [{source: S3, locator: "deeply rooted in his Christian faith; sermon outlines"}, {source: S1, locator: "priest and abbot"}, {source: S4, locator: "Easter Predigtskizze (lead)"}]
    how_known: "P49: scholarly reconstruction at most 0.5. Richter (OSA, family) reconstructs lifelong Catholic faith and cites surviving sermon outlines; public record is ordained priest and elected abbot. Sermon text still only secondary (S4); Folia Mendeliana volumes unread."
    rationale: "Catholic priest and abbot whose later sermon outlines (lead) speak of grace, sacraments, risen Christ and 'liebe Gott' (S3, S4). Named alternative BELOW_THRESHOLD: own Lebenslauf (1850) says circumstances decided his vocational choice and he entered to escape the bitter struggle for existence (S5); Iltis and others read monastery entry as economic (S6, S9). Economic motive for entry does not by itself cancel later office and the faith reconstruction, but keeps CHRIST at 0.5."
    alternatives:
      - {value: BELOW_THRESHOLD, note: "Lebenslauf economic motive for monastery entry; Iltis 'without religious interest' claim (countered by Orel/Zumkeller sermon find, still secondary).", cites: [{source: S5, locator: "circumstances decided"}, {source: S9, locator: "Iltis / Wikiquote discussion"}]}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Priest, abbot; Richter faith reconstruction; sermon lead. BELOW_THRESHOLD kept as named alternative on primary_system (Lebenslauf economic entry), not as a systems/ code."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Lead only: Easter Predigtskizze — personal God ('liebe Gott'), grace, Eucharist, risen Christ uniting Natur und Übernatur (S4). Undated; placed in abbot / latter years (after 1865 span) by Richter and secondary notes; seen only as secondary quotation (Der Imkerfreund / Graney / Wikiquote of Zumkeller 1970). Standing deepen rule: do not score A from undated after-span secondary sermon quotes without primary check. Folia Mendeliana (Moravian Museum) unread. Nägeli letters have no God-talk. Do not force plot."}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S2, locator: "pp. 3–4; allgemein giltiges Gesetz"}, {source: S7, locator: "3 July 1870; higher, more fundamental law"}]
      how_known: "Scientist (P30). Own words: seeks a generally valid law for hybrids in Versuche (in span, S2); letter to Nägeli, 3 July 1870 (after span), treats Pisum/Hieracium opposites as 'individual phenomena, which are the manifestation of a higher, more fundamental, law' (S7). Support corroborated (P48). 0.5: P35 — no statement of his own that nature is exceptionless / admits no miracles; after-span letter weight (P20). Named alternative 4."
      rationale: "Lawful nature in heredity science (B 3). The 27 Sept 1870 remark that a Hieracium 'exception' to Gärtner's pollen claim 'must find a natural explanation' is about floral structure, not a no-miracle profession — does not lift P35 to B 4."
      alternatives:
        - {value: 4, note: "Working science / lawful-order remarks without a stated no-exception claim cannot distinguish lawful-with-exceptions from exceptionless (P35).", cites: [{source: S2, locator: "p. 3"}, {source: S7, locator: "3 July 1870"}]}
    C_ledger: {value: UNKNOWN, how_known: "Sermon lead (grace, Eucharist, eternal glory) is undated after-span secondary — same bar as A; not scored."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scientist: working science bears on 'same laws everywhere' but without his own statement E stays BELOW_THRESHOLD (P19). Nägeli 'higher law' unifying Pisum/Hieracium is a lead, not scored as E this pass."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied (P19). Do not force plot without A."}
  statements:
    - text: "Therefore, after having finished his philosophical studies, he felt himself compelled to step into a station of life, which would free him from the bitter struggle for existence. His circumstances decided his vocational choice. He requested and received in the year 1843 admission to the Augustinian Monastery St. Thomas in Altbrünn."
      cites: [{source: S5, locator: "Lebenslauf, 17 April 1850"}]
      date: "1850-04-17"
      context: "Third-person curriculum vitae for teacher examination; before the span. Own account of monastery entry."
      axes: []
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Mrs Hugo Iltis translation via teaching reprint (S5); wording matches Orel/PNAS quotations. Used for CHRIST alt BELOW, not for A."
    - text: "On this occasion I cannot resist remarking how striking it is that the hybrids of Hieracium show a behavior exactly opposite to those of Pisum. Evidently we are here dealing only with individual phenomena, which are the manifestation of a higher, more fundamental, law."
      cites: [{source: S7, locator: "letter to Carl Nägeli, Brünn, 3 July 1870"}]
      date: "1870-07-03"
      context: "Private scientific letter after the 1865 span; adult working science continued."
      axes: [B_cause]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Piternick English of Correns 1905 edition (Genetics 1950 / ESP). German: Ausfluss eines höheren allgemeinen Gesetzes (Nogler 2006). After-span → 0.5 (P20); does not state no-exception (P35)."
    - text: "Far be it from me to interpret the result of this experiment as showing that Gärtner is wrong when he claims the pollen of the hybrid to be ineffectual in competition with the parental pollen. No proof to the contrary may be deduced from this experiment; the exception which Hieracium seems to make in this respect must find a natural explanation in the peculiar structure of the florets and the reaction of the organs of fertilization."
      cites: [{source: S7, locator: "letter to Carl Nägeli, Brünn, 27 September 1870"}]
      date: "1870-09-27"
      context: "Same correspondence; 'exception' = apparent anomaly vs Gärtner, explained naturally — not a miracle / exceptionless-nature claim."
      axes: [B_cause]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Supports natural explanation of anomalies; does not lift B to 4 under P35."
  changes_over_life:
    - {value: "1850 Lebenslauf frames monastery entry as economic relief; later office as priest/abbot and (undated) sermon outlines are the faith side of the record. No documented reverse of Christian affiliation in adult years.", year: 1843, certainty: 0.5, cites: [{source: S5, locator: "Lebenslauf"}, {source: S3, locator: "faith"}, {source: S4, locator: "sermon lead"}], how_known: "Own Lebenslauf + scholarly reconstruction."}
  coder_notes: "Deepen D1 (#165): A left UNKNOWN (undated after-span secondary sermon; Folia Mendeliana unread). B corroborated via Nägeli 1870 but P35 still caps at 3 @0.5 alt 4. CHRIST @0.5 kept; Lebenslauf documents BELOW alt. Chart-moving NO. Parent to refresh combined chart after this person (Jason t223u) — do not touch figures/ here. No fallacy_catalog."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German-speaking Silesian / Moravian", certainty: 0.7, cites: [{source: S6, locator: "Early life"}, {source: S3, locator: "ethnic German family"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: "Catholic", certainty: 0.7, cites: [{source: S3, locator: "deeply religious peasant family"}, {source: S6, locator: "Early life"}], how_known: "Two sources."}
  baptism_or_initiation: {value: "Baptised Johann (Catholic); baptism date often given as 22 July 1822", certainty: 0.5, cites: [{source: S6, locator: "birthnote"}], how_known: "Wikipedia; not parish register this pass."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1865", certainty: 0.7, cites: [{source: S2, locator: "p. 3"}], how_known: "Versuche über Pflanzen-Hybriden, read 1865 (printed 1866), the one listed lasting work (P29, P30 #1)."}
  age_at_first_lasting_contribution: {value: 43, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "p. 3"}], how_known: "1865 − 1822 = 43 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No scored LIO-type view at 3 or 4 with certainty ≥ 0.7 from a dated own statement (P27). B 3 @0.5 from lawful-order remarks is not first_evidence under that rule."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "No scored LIO-type first evidence."}
  worldview_during_major_work: {value: "Catholic priest in St Thomas monastery; heredity work framed as search for generally valid natural law (Versuche). Faith reconstruction is for adult life including later abbacy; sermon lead is after span.", certainty: 0.5, cites: [{source: S1, locator: "Experimental period"}, {source: S2, locator: "p. 3"}, {source: S3, locator: "faith"}], how_known: "Office + paper + Richter."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Combinatorial, mathematical treatment of hybrid ratios (S1).", certainty: 0.5, cites: [{source: S1, locator: "Experimental period"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data for geometric Lane B model beyond combinatorial ratios."
  notes: "Sermon Natur/Übernatur metaphor is Lane A lead material (unscored), not a geometric claim."

institutions:
  - {value: "Augustinian monastery of St Thomas, Altbrünn", role: "friar, priest; abbot from 1868", years: "1843–1884", kind: "religious body", certainty: 0.7, cites: [{source: S1, locator: "Education and early career"}, {source: S6, locator: "Academic career"}], how_known: "Two sources."}
  - {value: "Brünn Realschule", role: "teacher (physics / natural history)", years: "1854–1868", kind: "employer", certainty: 0.7, cites: [{source: S1, locator: "Education and early career"}, {source: S6, locator: "Academic career"}], how_known: "Two sources."}
  - {value: "University of Vienna", role: "student (physics, natural sciences)", years: "1851–1853", kind: "university", certainty: 0.7, cites: [{source: S1, locator: "Education and early career"}, {source: S6, locator: "Academic career"}], how_known: "Two sources."}
collaborators:
  - {value: "Cyril Napp", relation: "mentor or employer", note: "abbot; permitted the experiments", certainty: 0.7, cites: [{source: S1, locator: "Experimental period"}], how_known: "Britannica."}
  - {value: "Carl Nägeli", relation: "correspondent", note: "Hieracium specialist; letters 1866–1873", certainty: 0.7, cites: [{source: S7, locator: "letters"}], how_known: "Correns edition."}
  - {value: "Franz Unger", relation: "teacher", note: "Vienna", certainty: 0.7, cites: [{source: S1, locator: "Education and early career"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S10, locator: "roster.csv, rank 174"}], how_known: "Study roster."}
  controversies:
    - {value: "Fisher (1936) argued Mendel's ratios were 'too good'; later defenses by Hartl/Fairbanks and others — not a worldview issue", certainty: 0.5, cites: [{source: S6, locator: "Mendelian paradox"}], how_known: "Wikipedia summary; not re-adjudicated."}
  data_quality_flags:
    - "Easter Predigtskizze still secondary / undated / after-span; Folia Mendeliana unread."
    - "Iltis Life of Mendel (1924/1932) not read first-hand this pass — economic-motive claim via Lebenslauf + secondary reports."
  open_questions:
    - "Folia Mendeliana / Zumkeller edition of Predigtskizzen — date, full German, archival shelfmark."
    - "Iltis first-hand pages on religious interest vs economic entry."
    - "Any in-span (c. 1865) first-person God or sacrament statement besides office."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Robert Olby"
    citation: "Olby, Robert. 'Gregor Mendel.' Encyclopaedia Britannica (rev. 29 August 2026). https://www.britannica.com/biography/Gregor-Mendel"
    url: "https://www.britannica.com/biography/Gregor-Mendel"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Signed article; body cited, question boxes not used (P26)."
    used_for: [identity, basics, contribution, childhood, worldview, institutions, collaborators, lane_b, timing]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Gregor Mendel"
    citation: "Mendel, Gregor. 'Versuche über Pflanzen-Hybriden.' Verhandlungen des naturforschenden Vereines in Brünn IV (für das Jahr 1865), Abhandlungen, pp. 3–47. Brünn, 1866. Deutsches Textarchiv. https://www.deutschestextarchiv.de/book/show/mendel_pflanzenhybriden_1866"
    url: "https://www.deutschestextarchiv.de/book/show/mendel_pflanzenhybriden_1866"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Transcription of the 1866 printing (title page and opening read)."
    used_for: [basics, contribution, worldview, timing]
  - id: S3
    type: secondary
    kind: "journal article"
    author: "Clemens Richter"
    citation: "Richter, Clemens, OSA. 'Remembering Johann Gregor Mendel: a human, a Catholic priest, an Augustinian monk, and abbot.' Molecular Genetics & Genomic Medicine 3(6) (2015): 483–485. https://pmc.ncbi.nlm.nih.gov/articles/PMC4694133/"
    url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC4694133/"
    accessed: 2026-10-24
    source_quality: "scholarly reconstruction"
    reliability_note: "Commemorative address by a member of his order and family; published article, read in full. P49 cap 0.5 for reconstructed faith."
    used_for: [worldview, heritage, childhood]
  - id: S4
    type: secondary
    kind: "other"
    author: "J. H. Graney (tr.); Der Imkerfreund / Zumkeller–Orel"
    citation: "Graney, J. H. (trans.). 'A brief portion of an Easter sermon by Gregor Mendel.' Vatican Observatory (2017), from Der Imkerfreund 27–28 (1972), p. 254 (Zumkeller report on Orel Predigtskizze, Brno symposium 1970). https://www.vaticanobservatory.org/wp-content/uploads/2017/10/Mendel-Easter-Sermon-JHG.pdf"
    url: "https://www.vaticanobservatory.org/wp-content/uploads/2017/10/Mendel-Easter-Sermon-JHG.pdf"
    accessed: 2026-10-24
    source_quality: "other"
    reliability_note: "Secondary quotation of undated sermon outline (V3); lead only for A. Folia Mendeliana museum print unread."
    used_for: [worldview]
  - id: S5
    type: primary
    kind: "letter"
    author: "Gregor Mendel"
    citation: "Mendel, Gregor. Curriculum vitae / Lebenslauf, Znaim, 17 April 1850 (third person), for teacher examination. English tr. Mrs Hugo Iltis, Mendel Museum; teaching reprint at ldysinger.com; quotations also in Orel and PNAS Fairbanks 2022."
    url: "http://www.ldysinger.com/@texts2/1880_mendel/00d_introd.htm"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Own Lebenslauf; English via Iltis museum translation on a teaching site — wording cross-checked against Orel/PNAS secondary quotations. German archival original not opened this pass."
    used_for: [worldview, childhood, heritage, timing]
  - id: S6
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "Wikipedia. 'Gregor Mendel.' https://en.wikipedia.org/wiki/Gregor_Mendel"
    url: "https://en.wikipedia.org/wiki/Gregor_Mendel"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "P50 dual bio; Early life / Academic career / paradox section. Not sole support for LIO scores."
    used_for: [identity, basics, childhood, heritage, institutions, collaborators, review]
  - id: S7
    type: primary
    kind: "letter"
    author: "Gregor Mendel"
    citation: "Mendel, Gregor. Letters to Carl Nägeli, 1866–1873. English: Leonie Kellen Piternick and George Piternick, Genetics 35(5, pt 2): 1–29 (1950), from Correns 1905. ESP reprint PDF. http://old.esp.org/foundations/genetics/classical/holdings/m/gm-let.pdf (IA mirror used 2026-10-24)."
    url: "https://web.archive.org/web/20150923211639/http://www.esp.org/foundations/genetics/classical/holdings/m/gm-let.pdf"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Scholarly English of Correns edition; German quoted via Nogler 2006 where needed."
    used_for: [worldview, contribution, collaborators]
  - id: S8
    type: secondary
    kind: "journal article"
    author: "Günter A. Nogler"
    citation: "Nogler, Günter A. 'The Lesser-Known Mendel: His Experiments on Hieracium.' Genetics 172(1) (2006): 1–6. https://pmc.ncbi.nlm.nih.gov/articles/PMC1456139/"
    url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC1456139/"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Scholarly article; German Ausfluss eines höheren allgemeinen Gesetzes and Hieracium context."
    used_for: [worldview, contribution]
  - id: S9
    type: secondary
    kind: "other"
    author: "Wikiquote Talk / Iltis reception"
    citation: "Wikiquote Talk:Gregor Mendel — German block quoting Zumkeller on Iltis's claim that Mendel entered the monastery for economic reasons without religious interest, and Orel's Predigtskizze find. https://en.wikiquote.org/wiki/Talk:Gregor_Mendel"
    url: "https://en.wikiquote.org/wiki/Talk:Gregor_Mendel"
    accessed: 2026-10-24
    source_quality: "other"
    reliability_note: "Secondary discussion of Iltis vs Orel/Zumkeller; Iltis monograph not read first-hand."
    used_for: [worldview]
  - id: S10
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [review]
---

## Summary

Gregor Mendel (1822–1884), botanist and Augustinian abbot [S1; S6]. Deepen D1: CHRIST @0.5 (alt BELOW); A UNKNOWN; B 3 @0.5 alt 4 (corroborated); mid UNKNOWN. Not plotted. Chart-moving NO.

## Life and work

St Thomas monastery, Brünn Realschule, Vienna study [S1; S6]. Nägeli correspondence 1866–1873 [S7].

## Contribution and impact

Laws of heredity, read 1865, printed 1866 [S1; S2]. Hieracium work [S8; S7].

## Childhood and education

Catholic farming family; Troppau; Olmütz; monastery 1843 [S5; S6].

## Adult working worldview

CHRIST @0.5 scholarly reconstruction (Richter; office); Lebenslauf economic entry as BELOW alt [S3; S5]. A unscored (sermon lead) [S4]. B 3 @0.5 from Versuche + Nägeli higher-law letter; P35 blocks 4 [S2; S7].

## Heritage (context only)

Catholic German-speaking Silesian [S3; S6].

## Timing

1865, age 43 [S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Combinatorial ratios only.

## Open questions

- Folia Mendeliana / Zumkeller Predigtskizzen primary.
- Iltis first-hand.
- In-span God statement beyond office.

## Research log

- 2026-10-19: Britannica (Olby); DTA Versuche; Richter 2015; Graney sermon excerpt.
- 2026-10-24 (D1): Nägeli letters (ESP/IA Piternick PDF); Nogler Hieracium PMC; Lebenslauf (ldysinger/Iltis tr.); Wikipedia dual bio; Wikiquote Talk Iltis/Zumkeller; Folia Mendeliana still unread. No figures/.
