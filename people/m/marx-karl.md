---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch H)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch H, order P32: F 5, rank 48). Basics from Britannica (McLellan) and SEP (Wolff and Leopold). Worldview from the Introduction to A Contribution to the Critique of Hegel's Philosophy of Right (1844), read in the marxists.org English web copy (0.7 cap). Not a scientist under P30. primary_system ATHE 0.7; A 4 at 0.7 (alt BELOW_THRESHOLD); B UNKNOWN (no statement on the order of nature read, P16); C, D, E UNKNOWN; mid_basin false at 0.7 (A ≥ 3 branch). Not plotted. Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Batch H audit (cae9cb2, run 1: weaken #6): S1 author corrected to David T. McLellan, the byline on the live page when re-checked. No value changes."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #48). Needs: A single source; B UNKNOWN. Verified Critique HPR Introduction religion quotes against MECW vol. 3 scholarly edition (S5: pp. 175–176). Added Economic and Philosophic Manuscripts Estranged Labour (S5 p. 276: 'man is a part of nature') and Capital vol. 1 ch. 7 Fowkes Penguin (S6 p. 290: everlasting nature-imposed condition) for B. P47 source_quality on S1–S6. P48: A support single→corroborated (S3+S5); B newly scored 3 @ 0.5 written_profession support corroborated (S5+S6; P16/P41, alt 4). Dated Das Kapital vol. 1 to 1867 from the 25 July 1867 preface (S6); major_work_period / working_years 1844–1867. Statements verified_against → scholarly edition. Chart-moving YES: unplotted → faded filled (A 4 @ 0.7 corr; B 3 @ 0.5 corr). No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: marx-karl
  display_name: "Karl Marx"
  roster:
    canonical_name: "Karl Marx"
    rank: 48
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Karl Heinrich Marx", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  native_name: {value: UNKNOWN, how_known: "German in Latin script."}
  aliases: []

basics:
  birth:
    date: {value: "1818-05-05", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "opening (year 1818)"}], how_known: "Britannica day; SEP year agrees (P15)."}
    place: {value: "Trier, Rhine province, Prussia", modern_name: "Trier, Germany", polity_then: "Kingdom of Prussia", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1883-03-14", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "opening (year 1883)"}], how_known: "Britannica day; SEP year agrees (P15)."}
    place: {value: "London, England", modern_name: "London, United Kingdom", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1844, certainty: 0.7, cites: [{source: S1, locator: "'Early years' (Deutsch-französische Jahrbücher)"}, {source: S3, locator: "header ('First published: in Deutsch-Französische Jahrbücher, 7 & 10 February 1844')"}, {source: S5, locator: "Introduction, pp. 175–176"}], how_known: "The Critique of Hegel's Philosophy of Right: Introduction, with its 'oft-quoted' opium remark (S1), first published February 1844 (S3; S5). The 1844 Manuscripts were unpublished for about 100 years (S1)."}
  era_bucket: {value: "1750 to 1849", certainty: 0.7, cites: [{source: S3, locator: "header"}, {source: S5, locator: "Introduction, p. 175"}], how_known: "From 1844 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Germany is Western Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.5, cites: [{source: S1, locator: "'Early years'"}], how_known: "Cologne, Paris, Brussels, then London from 1850 (Northern Europe); the early works are Western European (0.5)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [German], certainty: 0.7, cites: [{source: S1, locator: "'Early years' (German titles)"}], how_known: "Britannica."}
  occupations: {value: ["philosopher", "economist", "journalist", "revolutionary"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Early years'"}], how_known: "Britannica."}

contribution:
  fields: {value: ["political philosophy", "economics", "theory of history"], certainty: 0.7, cites: [{source: S2, locator: "contents (§§1–3)"}], how_known: "SEP."}
  lasting_original_contributions:
    - {value: "Critique of Hegel's Philosophy of Right: Introduction (religion as 'the opium of the people')", year: 1844, kind: work, lasting: "'oft-quoted' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}, {source: S3, locator: "header"}, {source: S5, locator: "pp. 175–176"}], how_known: "Britannica; publication date from marxists.org header; wording checked in MECW 3."}
    - {value: "The Communist Manifesto (with Engels)", year: 1848, kind: work, lasting: "'the most celebrated pamphlet in the history of the socialist movement' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "Das Kapital, Volume One", year: 1867, kind: work, lasting: "'the movement's most important book' (S1); SEP treats Capital Volume 1 as his economic masterpiece (§3)", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "1867 Preface, closing date 'London, July 25, 1867'; ch. 7"}, {source: S2, locator: "§3.1 Reading Capital"}], how_known: "Preface dated 25 July 1867 (S6); Britannica and SEP confirm Capital Vol. 1 as lasting contribution."}
  evidence_of_impact:
    - {value: "Basis of the body of thought known as Marxism", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founder of Marxism (S1, S2).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Jewish by descent; father baptized in the Evangelical Established Church about a year before Karl's birth", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father Heinrich, a lawyer and 'man of the Enlightenment'; mother Henrietta Pressburg, from Holland", role: parents, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  household_circumstances: {value: "Successful lawyer's household, eldest surviving son of nine children", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  schooling:
    - {value: "High school in Trier", stage: "grammar or secondary school", run_by: "state or municipal", years: "1830–1835", ages: "12–17", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica; run_by is the coder's reading."}
    - {value: "University of Bonn, then University of Berlin (law and philosophy)", stage: university, run_by: "state or municipal", years: "1835–", ages: "17–", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events:
    - {value: "Baptized", year: 1824, age: 6, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica: baptized when he was six."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1844–1867", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "1867 Preface date"}], how_known: "Equals timing.major_work_period (first lasting 1844 to Capital vol. 1, 1867)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read that pairs natural science with religion as such; Capital uses the physicist as a methodological analogy (S6 Preface), not a science–religion relation."}
  primary_system:
    value: ATHE
    basis: written_profession
    certainty: 0.7
    cites: [{source: S3, locator: "paragraphs 1–4"}, {source: S5, locator: "Introduction, pp. 175–176"}, {source: S1, locator: "'Early years'"}]
    rationale: "Religion is a human product ('Man makes religion, religion does not make man'), heaven a 'fantastic reality' in which man finds only the reflection of himself, and its abolition 'the demand for their real happiness' (S3; S5 pp. 175–176); combined with Feuerbach's materialism (S1). Atheism with naturalism. Named alternative: SECHUM ('man is the highest essence for man'), not chosen because the text is a critique of religion as such. Contested label keeps 0.7."
    how_known: "Published Introduction checked in MECW 3 (S5) against the marxists.org English web copy (S3); German MEW 1 not read."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Chosen: religion as a human projection; materialism (S1)."}
    - {code: SECHUM, reason: "Alternative: 'man is the highest essence for man' (S3/S5) is humanist; not chosen because the text is a critique of religion as such."}
  lio_axes:
    A_locus:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S3, locator: "paragraphs 1–2"}, {source: S5, locator: "Introduction, pp. 175–176"}]
      how_known: "Published Introduction in marxists.org English web copy (S3) verified against MECW vol. 3 scholarly edition (S5 pp. 175–176). Named alternative BELOW_THRESHOLD. Independent source ids → corroborated (P48); value/certainty unchanged (contested alt keeps 0.7)."
      rationale: "No separate God: God and heaven are man's reflection ('Man makes religion, religion does not make man'; 'the fantastic reality of heaven' where he sought a superhuman being and found only the reflection of himself) (S5 pp. 175–176). Scored like Pauling's rejection of the supernatural (A 4). Named alternative: BELOW_THRESHOLD, since the passage criticizes religion rather than stating 'there is no God' in so many words."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S5, locator: "Economic and Philosophic Manuscripts, Estranged Labour, p. 276"}, {source: S6, locator: "Capital vol. 1, ch. 7, p. 290 (Fowkes)"}]
      how_known: "Own published/manuscript wording on nature in two independent works: 1844 Manuscripts in MECW 3 (S5) and Capital vol. 1 in Fowkes Penguin (S6). Not a scientist under P30. P16/P41: lawful/orderly nature without a stated no-exception claim → B 3 at 0.5, alt 4. Independent source ids → corroborated (P48)."
      rationale: "Scored on his account of nature (P6, P16; not a scientist under P30). Estranged Labour: 'man's physical and spiritual life is linked to nature means simply that nature is linked to itself, for man is a part of nature' (S5 p. 276). Capital labour-process: labour is 'the universal condition for the metabolic interaction between man and nature, the everlasting nature-imposed condition of human existence' and is 'common to all forms of society' (S6 p. 290). That states a standing natural order/constraint without saying nature is exceptionless or denying miracles in so many words. Under P41 (and the P16 Hilbert addendum), B 4 needs a stated no-exception claim, so 3 at 0.5. Named alternative 4: ATHE removes a divine intervenor, and no physical miracle or exemption is affirmed in the passages read. Independent sources → corroborated (P48)."
    C_ledger: {value: UNKNOWN, how_known: "Nothing read on personal afterlife reward or punishment."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read that pits revelation against observation as competing authorities."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: false, certainty: 0.7, cites: [{source: S3, locator: "paragraphs 1–2"}, {source: S5, locator: "pp. 175–176"}], how_known: "A_locus 4 (≥ 3): the A ≥ 3 branch reads A only (P10), so 0.7."}
  statements:
    - text: "The basis of irreligious criticism is: Man makes religion, religion does not make man."
      cites: [{source: S3, locator: "paragraph 2"}, {source: S5, locator: "Introduction, p. 175"}]
      date: "1844"
      context: "Opening of the Introduction, after 'criticism of religion is the premise of all criticism'."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "MECW 3 wording ('basis'); marxists.org web had 'foundation'. Emphasis marks dropped. German MEW 1 not read."
    - text: "Religion is the sigh of the oppressed creature, the heart of a heartless world, just as it is the spirit of spiritless conditions. It is the opium of the people."
      cites: [{source: S3, locator: "paragraph 4"}, {source: S5, locator: "Introduction, p. 175"}]
      date: "1844"
      context: "Same Introduction; SEP also cites MECW 3: 175 for the opium remark (S2 §1.2)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "MECW 3 wording ('just as it is the spirit of spiritless conditions'); earlier web wording had 'and the soul of soulless conditions'."
    - text: "That man's physical and spiritual life is linked to nature means simply that nature is linked to itself, for man is a part of nature."
      cites: [{source: S5, locator: "Economic and Philosophic Manuscripts, Estranged Labour, p. 276"}]
      date: "1844"
      context: "After 'Nature is man's inorganic body'; species-life discussion in the First Manuscript."
      axes: [B_cause]
      kind: "unpublished manuscript"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Written 1844; first published much later (S1). Counts as own words in a scholarly edition (S5); basis ceiling for axes remains written_profession only where the text was published by him — Capital supplies the published nature-order claim. Used here as independent corroborating nature statement (P48)."
    - text: "It is the universal condition for the metabolic interaction between man and nature, the everlasting nature-imposed condition of human existence, and it is therefore independent of every form of that existence, or rather it is common to all forms of society in which human beings live."
      cites: [{source: S6, locator: "Capital vol. 1, ch. 7, §1 The Labour Process, p. 290 (Fowkes)"}]
      date: "1867"
      context: "Close of the abstract labour-process analysis, before returning to the capitalist."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Fowkes Penguin English; German Capital / MECW 35 not opened this pass. Moore–Aveling web (marxists.org) has parallel 'everlasting Nature-imposed condition' wording."
  changes_over_life:
    - {value: "School writings showed 'a spirit of Christian devotion'; moved toward atheism with the Young Hegelians in Berlin", year: 1836, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica; the scored worldview is the adult one."}
  coder_notes: "Deepen D1 (queue #48): A labelled support single→corroborated (S3+S5 MECW Intro); B UNKNOWN→3 @ 0.5 written_profession, support corroborated (S5 EPM + S6 Capital Fowkes; P16/P41, alt 4). Not a scientist (P30): B on own account of nature. Capital vol. 1 dated 1867 from preface; major_work_period extended to 1844–1867. Chart: unplotted → faded filled (fill cue; darkness min(A,B)=0.5). C/D/E still UNKNOWN. German originals (MEW) and MECW Capital volume unread. No fallacy_catalog (Jason 2026-10-24)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German-Jewish (descended from rabbis)", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Jewish by descent; Evangelical (Prussian Protestant) by family conversion", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  baptism_or_initiation: {value: "Baptized at age six (Evangelical)", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1844–1867", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Early years'"}, {source: S6, locator: "1867 Preface date; ch. 7"}, {source: S2, locator: "§3.1"}], how_known: "1844 first lasting contribution to Capital vol. 1 dated 1867 (P29, P30)."}
  age_at_first_lasting_contribution: {value: 26, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "1844 − 1818 = 26 (P30)."}
  first_evidence_of_lio_type_views: {value: "Critique HPR Introduction (A 4: religion as human product) and 1844 Manuscripts Estranged Labour (B: man a part of nature); Capital 1867 labour-process restates everlasting nature-imposed condition", year: 1844, age: 26, certainty: 0.7, cites: [{source: S5, locator: "Introduction pp. 175–176; EPM p. 276"}, {source: S6, locator: "ch. 7, p. 290"}], how_known: "Earliest dated LIO-type evidence at A 4 / B 3 is 1844 (S5); Capital 1867 is inside the major-work span."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S5, locator: "pp. 175–176, 276"}, {source: S6, locator: "p. 290"}], how_known: "1844 A/B evidence opens the major-work span; Capital 1867 B evidence is at its end."}
  worldview_during_major_work: {value: "ATHE", certainty: 0.7, cites: [{source: S3, locator: "paragraphs 1–4"}, {source: S5, locator: "pp. 175–176"}], how_known: "As primary_system."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Nothing read on mathematics as form.", certainty: 0.5, cites: [{source: S1, locator: "'Early years'"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Early years'"}], how_known: "Humanities courses at Bonn (S1)."}
  circle_present: {value: "no", rationale: "God as human projection; nature as man's inorganic body / everlasting constraint, not God=Nature.", certainty: 0.5, cites: [{source: S5, locator: "pp. 175–176, 276"}, {source: S6, locator: "p. 290"}], how_known: "Coder's reading."}
  reading: "Religion as a human product; nature as standing material condition of human life; no lawful-God circle."
  notes: "Belief model only; H1 not tested."

institutions:
  - {value: "Rheinische Zeitung, Cologne", role: editor, years: "1842–1843", kind: employer, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
collaborators:
  - {value: "Friedrich Engels", relation: collaborator, note: "lifelong collaborator from 1844", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 48"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags: []
  open_questions:
    - "German originals (MEW 1 Introduction; German Capital) and MECW Capital volume still unread; Fowkes English used for Capital."
    - "No explicit no-exception / miracle-denial wording found for B 4; P41 keeps B at 0.5."
    - "C_ledger, D_authority, E_scope still UNKNOWN."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "David T. McLellan"
    citation: "McLellan, David T. \"Karl Marx.\" Encyclopaedia Britannica, updated 4 September 2026. https://www.britannica.com/biography/Karl-Marx."
    url: "https://www.britannica.com/biography/Karl-Marx"
    accessed: 2026-10-15
    reliability_note: "Signed article body (opening and 'Early years'); the Top Questions box is not used. Britannica lists several contributors; the byline shown was Lewis S. Feuer in one fetch on 2026-10-15 and David T. McLellan in the auditor's and a later fetch the same day, so the record uses McLellan."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: encyclopedia
    author: "Jonathan Wolff and David Leopold"
    year: 2025
    citation: "Wolff, Jonathan, and David Leopold. \"Karl Marx.\" Stanford Encyclopedia of Philosophy, first published 26 August 2003, substantive revision 27 March 2025. https://plato.stanford.edu/entries/marx/."
    url: "https://plato.stanford.edu/entries/marx/"
    accessed: 2026-10-24
    reliability_note: "Peer-reviewed reference article; authors as shown in the citation information on the page. Cites MECW 3: 175 for the opium remark (§1.2) and treats Capital Volume 1 as the economic masterpiece (§3)."
    source_quality: "reference entry"
    used_for: [basics, contribution, timing]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Karl Marx"
    year: 1844
    citation: "Marx, Karl. \"A Contribution to the Critique of Hegel's Philosophy of Right: Introduction.\" Deutsch-Französische Jahrbücher, February 1844. English web copy, Marxists Internet Archive."
    url: "https://www.marxists.org/archive/marx/works/1843/critique-hpr/intro.htm"
    accessed: 2026-10-15
    reliability_note: "Unofficial web copy; transcription source unknown; §7 cap 0.7 until checked in S5."
    source_quality: "unofficial web copy"
    used_for: [basics, contribution, worldview, timing, lane_b]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S5
    type: primary
    kind: "scholarly edition"
    author: "Karl Marx"
    year: 1975
    citation: "Marx, Karl, and Frederick Engels. Collected Works, Volume 3: Karl Marx March 1843–August 1844. London: Lawrence & Wishart, 1975. Contribution to the Critique of Hegel's Philosophy of Law. Introduction, pp. 175–176; Economic and Philosophic Manuscripts of 1844, Estranged Labour, p. 276."
    url: "https://files.libcom.org/files/2022-12/MECW_03.pdf"
    accessed: 2026-10-24
    reliability_note: "Lawrence & Wishart / International Publishers MECW scholarly collected works. Used to verify Introduction religion quotes (pp. 175–176) and to read the Estranged Labour nature passage (p. 276). PDF via libcom."
    source_quality: "scholarly edition or monograph"
    used_for: [basics, contribution, worldview, timing, lane_b]
  - id: S6
    type: primary
    kind: "scholarly edition"
    author: "Karl Marx"
    year: 1976
    citation: "Marx, Karl. Capital: A Critique of Political Economy, Volume One. Translated by Ben Fowkes. Harmondsworth: Penguin Books in association with New Left Review, 1976. 1867 Preface (dated London, 25 July 1867); Chapter 7, 'The Labour Process and the Valorization Process', §1, p. 290 (everlasting nature-imposed condition)."
    url: "https://opencuny.org/classicaltheory/files/2013/08/Marx_Capital_ch7.pdf"
    accessed: 2026-10-24
    reliability_note: "Standard English scholarly translation (Fowkes). Chapter 7 read in a PDF extract of the Penguin pagination; Preface date also confirmed via marxists.org English web of the 1867 Preface. German Capital / MECW 35 not opened."
    source_quality: "scholarly edition or monograph"
    used_for: [contribution, worldview, timing]

---

# Karl Marx

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Karl Marx (1818–1883), German philosopher, economist and revolutionary: Critique HPR Introduction (1844), The Communist Manifesto (1848), Das Kapital vol. 1 (1867) [S1; S2; S6]. Deepen D1 (P47–P50): primary_system ATHE 0.7; A 4 @ 0.7 written_profession, support corroborated (S3+S5; alt BELOW_THRESHOLD); B 3 @ 0.5 written_profession, support corroborated (S5+S6; P16/P41, alt 4); C, D, E UNKNOWN; mid_basin false @ 0.7. Chart: unplotted → faded filled (fill cue; darkness min(A,B)=0.5).

## Life and work

Trier, Bonn, Berlin; Rheinische Zeitung; Paris, Brussels, London [S1].

## Contribution and impact

Critique of Hegel's Philosophy of Right: Introduction (1844) [S1; S3; S5], Manifesto (1848) [S1], Capital Volume One (1867) [S1; S2; S6].

## Childhood and education

Jewish family; father baptized before his birth; Karl baptized at six [S1].

## Adult working worldview

'Man makes religion, religion does not make man'; religion 'is the opium of the people' [S3; S5, pp. 175–176]. Man 'is a part of nature' [S5, p. 276]; labour is the 'everlasting nature-imposed condition of human existence' [S6, p. 290].

## Heritage (context only)

German-Jewish, Evangelical by conversion [S1].

## Timing

First lasting contribution 1844, at 26; major-work period 1844–1867 [S1; S5; S6]. LIO-type evidence during the span (1844 A/B; 1867 B).

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle [S5; S6].

## Open questions

- German MEW / MECW Capital unread; Fowkes English used for Capital.
- No explicit no-exception claim for B 4 (P41 keeps 0.5).
- C, D, E UNKNOWN.

## Research log

- 2026-10-15: Read Britannica (McLellan, opening and 'Early years'), SEP contents, and the marxists.org Introduction.
- 2026-10-24: Deepen D1. MECW vol. 3 (libcom PDF): Introduction pp. 175–176; EPM Estranged Labour p. 276. Capital vol. 1 Fowkes ch. 7 p. 290 + 1867 Preface date. SEP reopened for Capital / MECW cites. No fallacy_catalog.
