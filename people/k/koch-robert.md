---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA9)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #202/228, F 3, rank 215). Goals: firm B; seek any A; do not force plot. Read: Koch 1882 Die Aetiologie der Tuberkulose English (Pinner/Pinner via German History Intersections; S6) — own-words complete proof of parasitic nature / causal connection of tubercle bacilli; Encyclopedia.com DSB Dolman (S8) — parents Lutherans; Deutsche Biographie NDB Kümmel (S9) — Konfession lutherisch; Wikipedia EN Personal life (S7) citing Brock 1988 p. 296 'Religion never entered his life' (secondary biographer characterization, not Koch own-words). Nobel lecture (S10) is prophylaxis/control, not B/A. B stays 3 @ 0.5 inference_from_work; support labelled corroborated (S1+S6; P48); alt 4 named (P35 working-science cap — no own statement on law-and-exception / miracles). A stays UNKNOWN (P19): no first-person God/religion statement; Brock/Wikipedia irreligious is secondary only; Lutheran is heritage. primary_system UNKNOWN. mid UNKNOWN. Chart-moving NO. Childhood parents + Lutheran heritage filled. P47 source_quality on S1–S10. No fallacy_catalog. No figures/. Draft, not reviewed."}
    - {date: 2026-10-20, by: "Grok Bot", summary: "AA10 audit fix: postulates item year stays UNKNOWN, with 1884 as the candidate only (catalogue record, paper not read)."}
    - {date: 2026-10-20, by: "Grok Bot", summary: "AA9 audit fixes: postulates candidate year 1884 (S4), span alternative 1876–1884; death 27 May 1910 at 0.7 (NobelPrize.org, S5); region of work Eastern Europe (Wollstein), alternative Western Europe."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA9, order P32: F 3, rank 215). Source: Britannica scholars edition, signed by Lloyd Grenfell Stevenson (read in full); Britannica students edition (S3) for the death-day conflict. Lasting: the anthrax life cycle (announced at Breslau, 1876), which 'afforded for the first time convincing proof of the definite causal relation of a particular microorganism to a particular disease' (S1); Koch's postulates (named after him; S1 gives no year; candidate 1884, Die Aetiologie der Tuberkulose, Mitt. Kaiserl. Gesundheitsamte II, S4). Tuberculosis (1882) and cholera (1883) discoveries carry prize-time praise only in S1 (Nobel 1905), so not listed as lasting (P13). Span 1876 at 0.5, alternative 1876–1884 (postulates candidate year), age 33. Death 27 May 1910 at 0.7 (NobelPrize.org, S5). Region of work Eastern Europe (Wollstein, now Wolsztyn, Poland, where the span took place: AA6 rule, P3 modern country), alternative Western Europe. Scientist: B 3 at 0.5, alt 4 (P35). Worldview UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: koch-robert
  display_name: "Robert Koch"
  roster:
    canonical_name: "Robert Koch"
    rank: 215
    F: 3
    models: [Claude, DeepSeek, Gemini]
    band: "core (3–4)"
    status: "core"
    field: "medicine"
    field_bucket: "medicine"
  full_name: {value: "Robert Heinrich Hermann Koch", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  native_name: {value: "Robert Koch", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  aliases: []

basics:
  birth:
    date: {value: "1843-12-11", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S8, locator: "opening (b. Clausthal … 11 December 1843)"}, {source: S9, locator: "Lebensdaten / NDB (* 11.12.1843)"}], how_known: "Britannica + DSB + Deutsche Biographie agree."}
    place: {value: "Clausthal, Hannover", modern_name: "Clausthal-Zellerfeld, Germany", polity_then: "Kingdom of Hanover", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S8, locator: "opening"}, {source: S9, locator: "Geburtsort Clausthal (Harz)"}], how_known: "Three sources."}
  death:
    date: {value: "1910-05-27", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S5, locator: "Died"}, {source: S3, locator: "para. 6 (28 May conflict)"}, {source: S8, locator: "opening (d. Baden-Baden … 27 May 1910)"}, {source: S9, locator: "† 27.5.1910"}], how_known: "Britannica scholars, NobelPrize.org, DSB, and Deutsche Biographie agree on 27 May. Students edition (S3) says 28 May; not a real dispute."}
    place: {value: "Baden-Baden", modern_name: "Baden-Baden, Germany", polity_then: "German Empire", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S8, locator: "opening"}, {source: S9, locator: "Sterbeort Baden-Baden"}], how_known: "Three sources."}
  first_lasting_contribution_year: {value: 1876, certainty: 0.7, cites: [{source: S1, locator: "Anthrax research"}], how_known: "The anthrax life cycle 'was announced and illustrated at Breslau in 1876' (S1); P30 first public statement."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "Anthrax research"}], how_known: "1876 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Germany (P3)."}
  region_of_work: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "Early training; Anthrax research"}], how_known: "The 1876 span work was done at Wollstein, now Wolsztyn, Poland (AA6 rule; P3 modern country; regions.csv puts Poland in Eastern Europe). Alternative Western Europe (Berlin, home region)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["German"], certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S6, locator: "title (German original)"}], how_known: "Coder's reading: German papers and Berlin societies; 1882 paper published in German."}
  occupations: {value: ["physician", "bacteriologist"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

contribution:
  fields: {value: ["medicine", "bacteriology"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica: 'one of the founders of bacteriology'."}
  lasting_original_contributions:
    - {value: "Life cycle of the anthrax bacillus (spore formation), the first proof that a specific microorganism causes a specific disease", year: 1876, kind: "discovery", lasting: "'The anthrax work afforded for the first time convincing proof of the definite causal relation of a particular microorganism to a particular disease' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Anthrax research"}], how_known: "Announced at Breslau, 1876 (S1)."}
    - {value: "Koch's postulates (four criteria for proving that a disease is caused by a specific organism)", year: UNKNOWN, kind: "method", lasting: "'called Koch's postulates' (S1): named after him", certainty: 0.5, cites: [{source: S1, locator: "Contributions to general bacteriology and pathology"}, {source: S4, locator: "bibliographic record"}, {source: S6, locator: "closing (complete proof of the parasitic nature)"}], how_known: "Item year UNKNOWN: S1 places them after his move to the Imperial Health Office in Berlin but gives no year. Candidate year 1884 (not set: Loeffler's 1883 formulation and Koch's expanded 1884 Mittheilungen paper are the usual scholarly anchors; S4 is a catalogue record; 1882 primary S6 states the complete-proof standard for tuberculosis but does not list the four named postulates)."}
  evidence_of_impact:
    - {value: "Koch's postulates", kind: "named after them", certainty: 0.7, cites: [{source: S1, locator: "Contributions to general bacteriology and pathology"}], how_known: "Britannica."}
    - {value: "Nobel Prize for Physiology or Medicine (1905), for tuberculosis", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    - {value: "'his place in the history of science was universally recognized'; his pupils 'were the creators of the new era of bacteriology'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Historical assessment"}], how_known: "Stevenson."}
  major_works:
    - {value: "Paper on the investigation, preservation and photographing of bacteria", year: 1877, kind: "paper or paper series", certainty: 0.7, cites: [{source: S1, locator: "Contributions to general bacteriology and pathology"}], how_known: "Britannica."}
    - {value: "Etiology of wound infection", year: 1878, kind: "paper or paper series", certainty: 0.7, cites: [{source: S1, locator: "Contributions to general bacteriology and pathology"}], how_known: "Britannica."}
    - {value: "Announcement of the tubercle bacillus (Physiological Society of Berlin, 24 March 1882); Die Aetiologie der Tuberkulose", year: 1882, kind: "paper or paper series", certainty: 1.0, cites: [{source: S1, locator: "Studies of tuberculosis and cholera"}, {source: S6, locator: "title and opening"}], how_known: "Britannica plus the English translation of the 1882 paper (S6)."}
  honours:
    - {value: "Nobel Prize for Physiology or Medicine", year: 1905, certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "Founder of bacteriology (S1).", certainty: 0.7, cites: [{source: S1, locator: "Historical assessment"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Lutheran (Evangelical Lutheran)", certainty: 1.0, cites: [{source: S8, locator: "parents … were Lutherans"}, {source: S9, locator: "Konfession: lutherisch"}], how_known: "DSB (parents Lutherans) and Deutsche Biographie (confession lutherisch). Heritage / baptismal affiliation — not adult worldview."}
  family_religious_practice: {value: UNKNOWN, how_known: "Sources name Lutheran affiliation; no detail on household practice (church attendance, piety)."}
  parents_and_household:
    - {value: "Father Hermann Koch, mining official (later Bergrat / overseer of local mines)", name: "Hermann Koch", role: father, certainty: 1.0, cites: [{source: S8, locator: "opening (Hermann Koch … mining official)"}, {source: S9, locator: "Genealogie (V Hermann)"}], how_known: "DSB and Deutsche Biographie."}
    - {value: "Mother Mathilde Julie Henriette Biewend, daughter of an iron-mine inspector", name: "Mathilde Julie Henriette Koch (née Biewend)", role: mother, certainty: 1.0, cites: [{source: S8, locator: "opening"}, {source: S1, locator: "Introduction (parents named in some Britannica editions; DSB confirms)"}], how_known: "DSB; Britannica also names the parents in related coverage."}
  household_circumstances: {value: "Large mining-town household in Clausthal (Harz); third of thirteen siblings (two died in infancy); father rose to mine overseer", certainty: 0.7, cites: [{source: S8, locator: "opening paragraphs on family"}], how_known: "DSB Dolman."}
  schooling:
    - {value: "Clausthal Gymnasium; graduated 1862", stage: "grammar or secondary school", years: "1851–1862", certainty: 0.7, cites: [{source: S8, locator: "primary school 1848; Gymnasium 1851; graduated 1862"}], how_known: "DSB."}
    - {value: "University of Göttingen, medicine (graduated 1866; teacher Jacob Henle)", stage: university, years: "1862–1866", certainty: 0.7, cites: [{source: S1, locator: "Early training; Anthrax research"}, {source: S8, locator: "Göttingen"}], how_known: "Britannica and DSB."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated beyond good school standing in mathematics (S8)."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure:
    - {value: "Uncle Eduard Biewend: natural-history excursions and early photography; boy collected plants, insects, minerals", certainty: 0.7, cites: [{source: S8, locator: "early paragraphs on maternal uncle"}], how_known: "DSB."}
  key_early_reading: []
  childhood_mentors:
    - {value: "Eduard Biewend (maternal uncle)", role: "relative / science mentor", certainty: 0.7, cites: [{source: S8, locator: "early paragraphs"}], how_known: "DSB."}
  languages_in_childhood: {value: ["German"], certainty: 0.7, cites: [{source: S8, locator: "Clausthal schooling"}], how_known: "Inferred from German schooling; 0.7."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1876", certainty: 0.5, cites: [{source: S1, locator: "Anthrax research"}], how_known: "Equals timing.major_work_period; alternative 1876–1884."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No statement of his on science and religion in S1–S10 (2026-10-24 deepen). Nobel lecture (S10) is public-health prophylaxis, not a religion relation."}
  primary_system:
    value: UNKNOWN
    cites: [{source: S1, locator: "whole article"}, {source: S6, locator: "whole excerpt (aetiology only)"}, {source: S7, locator: "Personal life ('He was irreligious') → Brock 1988 p. 296"}, {source: S8, locator: "whole DSB entry"}, {source: S9, locator: "Konfession lutherisch"}, {source: S10, locator: "Nobel lecture"}]
    how_known: "Deepen D1: no first-person belief profession. Brock via Wikipedia (S7): biographer line 'Religion never entered his life' — secondary characterization, not Koch's own words (P19, P49). Deutsche Biographie / DSB Lutheran is heritage (S8, S9), not adult system. Under P19: UNKNOWN."
    note: "Lead open: Thomas D. Brock, Robert Koch: A Life in Medicine and Bacteriology (1988/1999), p. 296 context — full chapter not opened this pass; Wikipedia quotes only the one sentence. Gradmann Laboratory Disease (2009) not opened for belief pages."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Rejected for coding: Wikipedia/Brock 'irreligious' / 'Religion never entered his life' is biographer paraphrase without Koch's own denial of God (P19, P49). Lead only.", cites: [{source: S7, locator: "Personal life + note 70 (Brock p. 296)"}]}
    - {code: CHRIST, reason: "Rejected: Lutheran is religious_heritage_by_birth / Deutsche Biographie Konfession field, not adult profession (P19).", cites: [{source: S8, locator: "parents were Lutherans"}, {source: S9, locator: "lutherisch"}]}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing of his on God or the divine in S1–S10 (P19). Brock/Wikipedia irreligious is secondary only; Lutheran parents/confession are heritage, not A. Nobel lecture silent on God."}
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      support: corroborated
      cites: [{source: S1, locator: "Anthrax research; Contributions"}, {source: S6, locator: "closing paragraphs (complete proof of the parasitic nature; causal connection)"}]
      how_known: "Scientist (P30). B from working science with no statement of his own on law and exception / miracles, so 3 at 0.5, alternative 4, never 4 (P35). Two independent source ids (Britannica synthesis of the anthrax/postulates programme + Koch's own 1882 aetiology paper) → corroborated (P48). Named alternative 4 kept under P35."
      rationale: "Experimental bacteriology: a specific organism produces a specific disease under stated conditions. Britannica (S1): anthrax work gave 'convincing proof of the definite causal relation of a particular microorganism to a particular disease'; postulates named after him. Koch 1882 own words (S6): 'it has been possible for the first time to establish the complete proof of the parasitic nature of a human infectious disease'; prior cases where 'parasites occur simultaneously with the pathological process, but the causal connection between the two has not been established' — he claims to have closed that gap for tuberculosis. Lawful specific causation in working science. No miracle, petition, or exception-to-law claim in anything read. P35 bars lifting to 4 (or to written_profession certainty ≥0.7) without his own statement on law-and-exception. Named alternative: 4."
      alternatives:
        - {value: 4, note: "Working science cannot tell lawful-with-exceptions from exceptionless (P35). Would need an own-words no-exception / laws-of-nature claim (Pasteur/Wilson pattern).", cites: [{source: S1, locator: "Anthrax research; Contributions"}, {source: S6, locator: "closing"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing on judgement, reward or afterlife in the sources read (P19)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing on revelation or scripture. Working science does not bear on D (P19)."}
    E_scope: {value: UNKNOWN, how_known: "Not scored from working science alone (P19, P30 addendum); no universal-order own-words."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied; UNKNOWN takes precedence (§6, P19)."}
  statements:
    - text: "it has been possible for the first time to establish the complete proof of the parasitic nature of a human infectious disease, and this of the most important one. So far such proof was established only for anthrax, while in a number of other infectious diseases in human beings […] it was only known that parasites occur simultaneously with the pathological process, but the causal connection between the two has not been established."
      cites: [{source: S6, locator: "closing paragraphs (significance)"}]
      date: "1882"
      context: "Die Aetiologie der Tuberkulose (24 March 1882 lecture; Berliner klinische Wochenschrift 1882). English: Pinner and Pinner for American Review of Tuberculosis 1932, excerpted at German History Intersections. Own-words methodological claim of complete causal proof; corroborates B inference_from_work (P48); not a P16 law-and-exception statement (P35, P49)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
  changes_over_life: []
  coder_notes: "Deepen D1: A stays UNKNOWN — no God/religion own-words; Brock 'Religion never entered his life' (via Wikipedia note 70) logged as secondary lead only. B stays 3 @ 0.5 inference_from_work with support corroborated (S1+S6); not lifted to written_profession / 0.7 because 1882 text is disease-aetiology method, not a meta claim about laws of nature and exceptions (contrast Pasteur lois de l'univers). Lutheran heritage filled (S8+S9). Gradmann and full Brock chapter still open leads. statements holds one B-warrant quote from S6."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S9, locator: "Clausthal"}], how_known: "German birth and career; coder's reading."}
  religious_heritage_by_birth: {value: "Lutheran (Evangelical Lutheran)", certainty: 1.0, cites: [{source: S8, locator: "They were Lutherans"}, {source: S9, locator: "Konfession: lutherisch"}], how_known: "DSB (parents Lutherans) and Deutsche Biographie (lutherisch). Context only — not a worldview code."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Infant Lutheran baptism is a common secondary lead (e.g. popular accounts) but not confirmed in S1–S10 scholarly pages this pass."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1876", certainty: 0.5, cites: [{source: S1, locator: "Anthrax research"}], how_known: "The one dated lasting item (P29, P30); 0.5 under the weakest-work rule. Alternative 1876–1884 (postulates candidate year, S4)."}
  age_at_first_lasting_contribution: {value: 33, certainty: 0.7, cites: [{source: S1, locator: "Introduction; Anthrax research"}], how_known: "1876 − 1843 = 33 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No LIO-type own-words scored; B rests on working science, which is not an LIO-type view (P27)."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "Nothing of his on God or nature at the LIO-type-view bar (P27); B is working-science inference only.", certainty: 0.5, cites: [{source: S1, locator: "whole article"}, {source: S6, locator: "whole excerpt"}, {source: S7, locator: "Personal life"}], how_known: "Absence in the sources read; not evidence of absence."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "A and primary_system UNKNOWN; B is working-science inference only."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Bacteriology / experimental pathology (S1, S6).", certainty: 0.5, cites: [{source: S1, locator: "text"}, {source: S6, locator: "methods"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "No God–Nature statement read.", certainty: 0.5, cites: [{source: S1, locator: "text"}, {source: S7, locator: "Personal life"}], how_known: "Coder's reading."}
  reading: "As belief, not finding: no geometric form; circle unclear. The record does not test H1 (A UNKNOWN)."
  notes: ""

institutions:
  - {value: "Imperial Health Office, Berlin", role: "head of bacteriology laboratory", years: UNKNOWN, kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "Contributions to general bacteriology and pathology"}], how_known: "Britannica; years not given."}
collaborators:
  - {value: "Ferdinand Cohn", relation: "collaborator", note: "published the 1876 anthrax paper", certainty: 0.7, cites: [{source: S1, locator: "Anthrax research"}], how_known: "Britannica."}
  - {value: "Jacob Henle", relation: "teacher", note: "Göttingen", certainty: 0.7, cites: [{source: S1, locator: "Anthrax research"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 215"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "A and primary_system UNKNOWN: no own-words belief; Brock irreligious is secondary only."
    - "B faded (0.5) under P35; support now corroborated."
    - "Postulates candidate year 1884; span alternative 1876–1884."
  open_questions:
    - "Read Brock 1988/1999 p. 296 chapter context (and any letters) for a first-person religion statement that could move A / primary_system."
    - "Read Gradmann Laboratory Disease (2009) for belief pages."
    - "Read the 1884 Mittheilungen expanded tuberculosis paper (or Loeffler 1883) to confirm the named postulates and fix the span end."
    - "Own-words laws-of-nature / exception claim that would lift B past P35 (none found this pass)."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Lloyd Grenfell Stevenson"
    citation: "Stevenson, Lloyd Grenfell. 'Robert Koch.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/Robert-Koch/45848"
    url: "https://kids.britannica.com/scholars/article/Robert-Koch/45848"
    accessed: 2026-10-19
    source_quality: "reference entry"
    reliability_note: "Signed article, scholars edition, read in full."
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
    citation: "'Robert Koch.' Britannica (students edition). https://kids.britannica.com/students/article/Robert-Koch/275309"
    url: "https://kids.britannica.com/students/article/Robert-Koch/275309"
    accessed: 2026-10-19
    source_quality: "reference entry"
    reliability_note: "Read in full; used only for the death-day note."
    used_for: [basics]
  - id: S4
    type: secondary
    kind: "database"
    author: "WorldCat"
    citation: "WorldCat record: Koch, Robert. 'Die Aetiologie der Tuberkulose.' Mittheilungen aus dem Kaiserlichen Gesundheitsamte 2 (Berlin: Hirschwald, 1884), pp. 1–88. OCLC 880639195. https://search.worldcat.org/title/880639195"
    url: "https://search.worldcat.org/title/880639195"
    accessed: 2026-10-19
    source_quality: "other"
    reliability_note: "Bibliographic record read; the 1884 paper itself not read."
    used_for: [contribution]
  - id: S5
    type: secondary
    kind: "institutional page"
    author: "NobelPrize.org"
    citation: "'Robert Koch – Facts.' NobelPrize.org. https://www.nobelprize.org/prizes/medicine/1905/koch/facts/"
    url: "https://www.nobelprize.org/prizes/medicine/1905/koch/facts/"
    accessed: 2026-10-19
    source_quality: "other"
    reliability_note: "Facts page, read in full."
    used_for: [basics]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Robert Koch"
    citation: "Koch, Robert. 'Die Ätiologie der Tuberkulose' (Berliner klinische Wochenschrift 19 [1882]: 221–30). English: 'The Aetiology of Tuberculosis,' trans. Berna Pinner and Max Pinner for American Review of Tuberculosis (1932), excerpted at German History Intersections. https://germanhistory-intersections.org/en/knowledge-and-education/ghis:document-25"
    url: "https://germanhistory-intersections.org/en/knowledge-and-education/ghis:document-25"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Authoritative English translation excerpt of the 1882 lecture/paper (Pinner and Pinner). Closing paragraphs on complete proof / causal connection read in full; middle microscopy detail skimmed. German original cited on the page."
    used_for: [contribution, worldview, statements]
  - id: S7
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors (citing Thomas D. Brock)"
    citation: "'Robert Koch.' Wikipedia. Personal life: 'He was irreligious,' citing Thomas D. Brock, Robert Koch: A Life in Medicine and Bacteriology (ASM Press, 1988), p. 296: 'Religion never entered his life.' https://en.wikipedia.org/wiki/Robert_Koch"
    url: "https://en.wikipedia.org/wiki/Robert_Koch"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Used only for the Brock p. 296 quotation chain (secondary biographer characterization). Not used to score A or primary_system (P19, P49). Dual-bio dates already covered by S1/S5/S8/S9."
    used_for: [worldview]
  - id: S8
    type: secondary
    kind: "encyclopedia"
    author: "Claude E. Dolman"
    citation: "Dolman, Claude E. 'Koch, Heinrich Hermann Robert.' Dictionary of Scientific Biography, via Encyclopedia.com. https://www.encyclopedia.com/people/medicine/medicine-biographies/robert-koch"
    url: "https://www.encyclopedia.com/people/medicine/medicine-biographies/robert-koch"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Signed DSB entry; whole long article read. Parents 'were Lutherans'; childhood and career detail. No adult religion profession of Koch's own."
    used_for: [identity, basics, childhood, worldview, heritage]
  - id: S9
    type: secondary
    kind: "encyclopedia"
    author: "Werner Friedrich Kümmel"
    citation: "Kümmel, Werner Friedrich. 'Koch, Robert.' Neue Deutsche Biographie 12 (1980): 251–255; Deutsche Biographie online. https://www.deutsche-biographie.de/sfz43565.html"
    url: "https://www.deutsche-biographie.de/sfz43565.html"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "NDB signed article; Konfession lutherisch and genealogy read. Confession field = heritage/baptismal affiliation in this series, not coded as adult primary_system."
    used_for: [basics, childhood, worldview, heritage]
  - id: S10
    type: primary
    kind: "published work by the subject"
    author: "Robert Koch"
    citation: "Koch, Robert. Nobel Lecture, 12 December 1905 ('How the Fight Against Tuberculosis Now Stands' / German parallel). NobelPrize.org. https://www.nobelprize.org/prizes/medicine/1905/koch/lecture/"
    url: "https://www.nobelprize.org/prizes/medicine/1905/koch/lecture/"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Own lecture on tuberculosis control and prophylaxis; skimmed for God/religion/law-of-nature language — none scored for A or for lifting B past P35."
    used_for: [worldview]
---

## Summary

Robert Koch (1843–1910), physician and bacteriologist [S1, S8]. Deepen D1: primary_system UNKNOWN; A UNKNOWN; B 3 @ 0.5 inference_from_work, support corroborated (S1+S6), alt 4 (P35); mid_basin UNKNOWN. Not plotted.

## Life and work

Clausthal (Lutheran mining family); Wollstein anthrax work; Berlin Imperial Health Office; tuberculosis 1882; cholera expedition; later tropical medicine [S1, S8, S9].

## Contribution and impact

Anthrax cycle 1876 (first convincing specific microbe–disease proof) [S1]. 1882 aetiology of tuberculosis: own claim of complete proof of parasitic nature / causal connection [S6]. Koch's postulates named after him (item year UNKNOWN; candidate 1884) [S1, S4]. Nobel 1905 [S1].

## Childhood and education

Parents Hermann Koch and Mathilde Biewend, Lutherans; Clausthal Gymnasium; Göttingen medicine under Henle [S8, S9, S1].

## Adult working worldview

No first-person God or religion statement in sources read. Brock via Wikipedia: 'Religion never entered his life' — secondary lead only, not scored [S7]. Lutheran is heritage [S8, S9]. B from working science (anthrax/TB causal proof) at 3 @ 0.5, corroborated by Britannica and the 1882 paper; P35 keeps alt 4 and bars lift without a law-and-exception own-words claim [S1, S6].

## Heritage (context only)

Lutheran by birth / Konfession [S8, S9]. Not a worldview code.

## Timing

1876, age 33 [S1]. Alternative span end 1884 (postulates candidate).

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No geometric form; A unknown so H1 not tested.

## Open questions

- Brock 1988/1999 full context; Gradmann 2009.
- 1884 Mittheilungen / Loeffler 1883 for named postulates year.
- Own-words law-and-exception claim for B lift.

## Research log

- 2026-10-24: Deepen D1. Primary 1882 (S6); DSB Dolman (S8); Deutsche Biographie (S9); Wikipedia→Brock irreligious lead (S7); Nobel lecture skim (S10). B support corroborated; A/primary/mid UNKNOWN; Lutheran heritage filled. Person-file-only local commit. No fallacy_catalog. No figures/.
- 2026-10-20: AA9 audit fixes: postulates candidate year 1884 (S4), span alternative 1876–1884; death 27 May 1910 at 0.7 (NobelPrize.org, S5); region of work Eastern Europe (Wollstein), alternative Western Europe.
- 2026-10-20: AA10 audit fix: postulates item year stays UNKNOWN, with 1884 as the candidate only (catalogue record, paper not read).
- 2026-10-20: Read Britannica (Stevenson, scholars edition) and the students edition.
