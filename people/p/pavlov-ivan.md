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
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 20c_early. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #173/228, F 3, rank 184). Goals: own words or better biography for AGNOS/A; do not force plot without A. Read Todes 2014/2015 via author's OUP blog (S5), Roger Smith Somatosphere review of Todes (S6), EUSP seminar summary of Todes on last manuscripts (S7); Windholz 1986 Kreps quotation as cited (S8); Babkin 1949 IA OCR (S9). Todes archival reconstruction: atheism firmly formed in the 1860s (not closet believer). Windholz via Kreps (student, 1920s reported speech): 'I became an unbeliever, an atheist in my school years' / belief-in-God claims 'sheer fantasy'. Babkin corroborates Gantt's envy-of-wife's-faith line (Seraphima letter quoting Pavlov) and 'Belief in Science' (organism as machine; science to answer life's questions / replace religion — milieu, not a locus). Viral 'letter to the students' still unscored (doubtful provenance; no authentic text found). primary AGNOS → ATHE @0.5 scholarly_reconstruction (Todes+Windholz), named alt AGNOS (Gantt). A stays BELOW_THRESHOLD: reported speech cannot score an axis on its own (§1 / P18); no published ontological 'there is no God' (Penrose/ATHE lack-of-belief precedent). B stays 3 @0.5 alt 4 (P35); support corroborated S1+S9. mid BELOW. Not plotted. P47 on S1–S9. No fallacy_catalog. No figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "AA2 audit fixes: the Gantt paraphrase is undated, so its date is removed rather than set to his death year (P12; the schema's date field takes no UNKNOWN). Added S3, his Selected Works (Moscow 1955), whose editors date the Madrid paper to April 1903. No score change."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA2, order P32: F 3, rank 184). Source: Britannica, signed by W. Horsley Gantt (his former collaborator; scholars edition, read in full). Lasting work: the conditioned reflex ('known chiefly for his development of the concept'); dated by its first public exposition at the XIV International Medical Congress, Madrid, 1903 (Campos-Bueno, journal article), the public reading as dating event (P30 #1). Worldview from Gantt's account: 'Although Pavlov held to scientific agnosticism, he considered true religion beneficial; he said that he envied no one anything except his wife her devout religious faith' (undated; a scholar's account, so scholarly_reconstruction, 0.5). primary_system AGNOS 0.5, alt BELOW_THRESHOLD; A BELOW_THRESHOLD (agnosticism states no locus); scientist (laws of the conditioned reflex: testable claims about organisms), so B 3 at 0.5 from working science, alt 4 (P24, P35); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Span 1903, age 54. Not plotted. Draft, not reviewed."}

identity:
  id: pavlov-ivan
  display_name: "Ivan Pavlov"
  roster:
    canonical_name: "Ivan Pavlov"
    rank: 184
    F: 3
    models: [Claude, DeepSeek, Gemini]
    band: "core (3–4)"
    status: "core"
    field: "psychology"
    field_bucket: "psychology / neuroscience"
  full_name: {value: "Ivan Petrovich Pavlov", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  native_name: {value: "Иван Петрович Павлов", certainty: 0.5, cites: [{source: S1, locator: "Introduction"}], how_known: "Cyrillic spelling the coder's."}
  aliases:
    - {name: "Pavlov-Ivan", kind: "roster alias"}

basics:
  birth:
    date: {value: "1849-09-26", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica: September 14 Old Style, September 26 New Style."}
    place: {value: "Ryazan", modern_name: "Ryazan, Russia", polity_then: "Russian Empire", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  death:
    date: {value: "1936-02-27", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "Leningrad", modern_name: "Saint Petersburg, Russia", polity_then: "Soviet Union", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1903, certainty: 0.7, cites: [{source: S2, locator: "text"}, {source: S3, locator: "pp. 25, 151–152"}], how_known: "First public exposition of his theory of conditional reflexes at the XIV International Medical Congress, Madrid, April 1903 (S2; S3: 'the paper read by Pavlov at the International Medical Congress in Madrid in April 1903'); public reading of a paper is the P30 #1 dating event (Z10 ruling)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S2, locator: "text"}], how_known: "1903 (P2)."}
  region_of_birth: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Russia (P3)."}
  region_of_work: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "Life"}], how_known: "St Petersburg."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Russian", "French"], certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Madrid lecture in French (S2)."}
  occupations: {value: ["physiologist"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

contribution:
  era_bucket: 20c_early
  fields: {value: ["physiology", "psychology"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "The conditioned (conditional) reflex and its laws", year: 1903, kind: "theory", lasting: "'known chiefly for his development of the concept of the conditioned reflex'; 'Pavlov's work laid the basis for the scientific analysis of behaviour' (S1, body)", certainty: 0.7, cites: [{source: S1, locator: "Introduction; Legacy"}, {source: S2, locator: "text"}], how_known: "Britannica (Gantt); dated by the Madrid lecture, 1903 (S2)."}
  evidence_of_impact:
    - {value: "Nobel Prize for Physiology or Medicine, 1904 (digestive secretions)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  major_works:
    - {value: "Lectures on the Work of the Digestive Glands", year: 1897, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "Life"}], how_known: "Britannica: the digestion work 'culminated in his book ... in 1897'; not called lasting in the body."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Laid the basis for the scientific analysis of behaviour (S1).", certainty: 0.7, cites: [{source: S1, locator: "Legacy"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Russian Orthodox", certainty: 0.7, cites: [{source: S1, locator: "Life"}, {source: S9, locator: "Early Years / father a priest"}], how_known: "Priest's son; church school and seminary (S1, S9)."}
  family_religious_practice: {value: "church school and theological seminary", certainty: 0.7, cites: [{source: S1, locator: "Life"}, {source: S9, locator: "Ecclesiastical Seminary"}], how_known: "Britannica; Babkin."}
  parents_and_household:
    - {value: "First son of a priest, grandson of a sexton; church school and theological seminary in Ryazan", role: "family", certainty: 0.7, cites: [{source: S1, locator: "Life"}, {source: S9, locator: "Early Years"}], how_known: "Britannica; Babkin."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated beyond clerical poverty of origin (S7)."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1903", certainty: 0.7, cites: [{source: S2, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No published own-words science–religion essay read; unfinished late manuscript on science/Christianity/Bolshevism noted by Todes (S7) is a lead only."}
  primary_system:
    value: ATHE
    basis: scholarly_reconstruction
    certainty: 0.5
    cites: [{source: S5, locator: "fact 6 (author's summary)"}, {source: S6, locator: "religion paragraph"}, {source: S7, locator: "seminar summary on atheism and late manuscript"}, {source: S8, locator: "Kreps quotation / Windholz conclusion"}, {source: S1, locator: "Opposition to communism, last para. (AGNOS alt)"}]
    how_known: "Todes (definitive archival biography): atheism firmly formed in the 1860s; impatient with non-scientific knowledge claims; defended believers' freedom without being a closet believer (S5, S6). Windholz 1986 reports student E. M. Kreps (1920s): Pavlov called claims of his religiosity / belief in God / church attendance 'sheer fantasy' and said he became 'an unbeliever, an atheist' in seminary years (S8; reported speech). Named alternative AGNOS: Gantt Britannica 'scientific agnosticism' (S1). Ceiling 0.5 (P49 reconstruction; named alt)."
    rationale: "Working metaphysics is positive naturalism / atheism per best biography (Todes) and the Kreps self-label as reported by Windholz, not Gantt's softer 'scientific agnosticism'. He valued religion's psychological/cultural role and opposed Bolshevik persecution (S5, S1) — use, not theism. Alternative AGNOS remains live because Gantt (collaborator) used that label and no written profession of atheism was read."
    alternatives:
      - {value: AGNOS, note: "Gantt (Britannica, former collaborator): 'Pavlov held to scientific agnosticism' while considering true religion beneficial (S1). Softer than Todes/Kreps atheist reading.", cites: [{source: S1, locator: "Opposition to communism, last para."}]}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Coded at 0.5: Todes archival atheism from 1860s (S5/S6); Kreps via Windholz self-label 'atheist' (S8)."}
    - {code: AGNOS, reason: "Named alternative: Gantt 'scientific agnosticism' (S1)."}
    - {code: CHRIST, reason: "Rejected: priest's son left seminary 1870 (S1); 1924 'I also am the son of a priest' is solidarity, not profession; wife devout, he not."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "No published ontological denial of a creating/directing God was read. Kreps via Windholz denies his own religiosity / belief in God as 'sheer fantasy' and self-labels 'atheist' (S8), but that is reported speech and cannot score an axis on its own (CODING_GUIDE §1 / statement kind). Todes reconstructs atheism without a quoted locus sentence in the sources read (S5/S6). Gantt's AGNOS reading also leaves no locus (S1). systems/ATHE.md: lack-of-belief sense may leave A BELOW. Named reading (not scored): A 4 at 0.5 if a published own-words denial is later found. Do not force plot."}
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      support: corroborated
      cites: [{source: S1, locator: "Laws of conditioned reflex"}, {source: S9, locator: "pp. 84–85 Belief in Science; organism as machine (Paris 1900)"}]
      how_known: "Scientist (P30, P35 addendum): laws of the conditioned reflex are testable claims about organisms (S1). Babkin quotes his treating the living organism as a machine (Paris 1900) and the Twenty Years preface as a 'profession of faith' in objective study of higher nervous activity (S7). No statement of his own on law and exception, so 3 at 0.5, alternative 4, never 4 (P24, P35). S1+S7 → corroborated (P48)."
      rationale: "He 'was led to formulate the laws of the conditioned reflex' and insisted mental phenomena be reduced 'to measurable physiological quantities' (S1); Babkin: organism 'merely a machine' (S7). Alternative 4."
      alternatives:
        - {value: 4, note: "Working science cannot tell lawful-with-exceptions from exceptionless (P35).", cites: [{source: S1, locator: "Legacy"}, {source: S9, locator: "Belief in Science"}]}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Lead: insisted that mental phenomena could be dealt with scientifically only by measurable quantities (S1); not scored."}
    E_scope: {value: UNKNOWN, how_known: "Scientist under P30; working physiology alone does not score E without a statement (P19)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied."}
  statements:
    - text: "Although Pavlov held to scientific agnosticism, he considered true religion beneficial; he said that he envied no one anything except his wife her devout religious faith."
      cites: [{source: S1, locator: "Opposition to communism, last para."}]
      context: "Gantt's summary of his views in the Britannica article; undated, so no date is recorded (P12; AA2 audit)."
      axes: [A_locus]
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-19
      note: "Gantt's paraphrase, not Pavlov's words; cannot score an axis on its own (§1). Backs the AGNOS alternative at scholarly_reconstruction 0.5."
    - text: "I envy no one else, but I envy you your religious faith."
      cites: [{source: S9, locator: "p. 28 (Seraphima Vasilievna letter of 1936-05-22 quoting Pavlov)"}]
      context: "Babkin prints Seraphima's letter after Pavlov's death, quoting his habitual remark to her; she replies that God judges by deeds."
      axes: []
      kind: "reported speech"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Corroborates Gantt's envy line (S1). About religion's felt value for his wife, not his own theism. Reported speech; not scored for A/primary."
    - text: "Listen, good fellow, in regard to [claims of] my religiosity, my belief in God, my church attendance, there is no truth in it; it is sheer fantasy. I was a seminarian, and like the majority of seminarians, I became an unbeliever, an atheist in my school years."
      cites: [{source: S8, locator: "Kreps quotation as printed via Windholz 1986"}]
      context: "Student E. M. Kreps asking whether Pavlov was religious (1920s); Windholz, Journal for the Scientific Study of Religion 25 (1986): 320–27."
      axes: [A_locus]
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Reported speech; cannot score an axis on its own (§1). Supports primary ATHE at scholarly_reconstruction together with Todes (S5/S6). JSTOR PDF closed this pass; wording verified from the Windholz citation as printed in standard secondary digests that quote the same Kreps lines."
    - text: "Indeed, in all stages mentioned in our discussion, the living organism showed itself to be merely a machine—a very complicated one, of course, but just as submissive and obedient as any other machine."
      cites: [{source: S9, locator: "p. 85 (quoting Pavlov at XIII International Medical Congress, Paris 1900)"}]
      date: "1900"
      context: "Babkin, 'Pavlov's Belief in Science'; double vagotomy discussion. Pre-span for dating of lasting work (1903) but adult evidence for working science (P31)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Public scientific address as quoted by Babkin. Supports B working-science reading; does not alone state no-exception (P35)."
  changes_over_life: []
  coder_notes: "D1 2026-10-24: Todes (via author blog + scholarly reviews) and Windholz/Kreps open ATHE over Gantt AGNOS; A not forced from reported speech. Viral 'letter to the students' / online belief quotes remain unscored (doubtful provenance; no authentic text located). Unfinished late Koltushi manuscript on science/Christianity/Bolshevism (Todes) is a lead for own words if published/editioned later. Babkin 1949 read on IA OCR for religion and Belief-in-Science chapters."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: "Russian Orthodox (priest's son)", certainty: 0.7, cites: [{source: S1, locator: "Life"}, {source: S9, locator: "Early Years"}], how_known: "Britannica; Babkin."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1903", certainty: 0.7, cites: [{source: S2, locator: "text"}], how_known: "The Madrid lecture, the dating event for the one listed lasting work (P29, P30 #1)."}
  age_at_first_lasting_contribution: {value: 54, certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S2, locator: "text"}], how_known: "1903 − 1849 = 54 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "Kreps (1920s) and Gantt (undated) are leads; seminary-years atheism is childhood/youth (off-point for first adult evidence dating)."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "Todes places atheism from the 1860s through the life; no sourced change across 1903 (P31)."}
  worldview_during_major_work: {value: ATHE, certainty: 0.5, cites: [{source: S5, locator: "fact 6"}, {source: S6, locator: "religion paragraph"}], how_known: "As primary_system; Todes: atheism from 1860s, so covers 1903 span."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Experimental physiology, not geometric argument (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Imperial Medical Academy, St Petersburg", role: "professor of physiology", years: "1890–1924", kind: "university", certainty: 0.7, cites: [{source: S1, locator: "Life"}], how_known: "Britannica."}
  - {value: "Institute of Experimental Medicine", role: "head of physiology", years: UNKNOWN, kind: "research institute", certainty: 0.5, cites: [{source: S1, locator: "Life"}], how_known: "Britannica."}
collaborators:
  - {value: "Carl Ludwig", relation: "teacher", note: "Leipzig, 1884–86", certainty: 0.7, cites: [{source: S1, locator: "Life"}], how_known: "Britannica."}
  - {value: "Rudolf Heidenhain", relation: "teacher", note: "Breslau", certainty: 0.7, cites: [{source: S1, locator: "Life"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 184"}], how_known: "Study roster."}
  controversies:
    - {value: "Online 'letter to the students' and similar belief quotes circulate without settled provenance; not used for scores (coder_notes; standing deepen rule).", certainty: 0.5, cites: [{source: S5, locator: "author's corrective facts (complex relation to religion)"}], how_known: "No authentic text located this pass; Todes stresses complexity against simple believer/non-believer myths."}
  data_quality_flags:
    - "Primary ATHE rests on scholarly reconstruction (Todes) plus reported speech (Kreps via Windholz); no written profession of atheism read."
    - "Gantt AGNOS paraphrase remains a live named alternative."
    - "Windholz 1986 JSTOR PDF closed this pass; Kreps wording verified from standard citations of that article."
  open_questions:
    - "Full Todes 2014 monograph pages on religion (archive quotations) for any written own words."
    - "Published edition of the unfinished late manuscript on science, Christianity, and Bolshevism (Todes)."
    - "Windholz 1986 full PDF / Kreps memoir primary publication."


sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "W. Horsley Gantt"
    citation: "Gantt, W. Horsley. Ivan Pavlov. Encyclopaedia Britannica (scholars edition)."
    url: "https://kids.britannica.com/scholars/article/Ivan-Pavlov/58811"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Signed article by his former collaborator; read in full (re-read D1)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "journal article"
    author: "J. J. Campos-Bueno"
    citation: "Campos-Bueno, J. J. Neuron Doctrine and Conditional Reflexes at the XIV International Medical Congress of Madrid of 1903. Universidad Complutense eprint 15010."
    url: "https://eprints.ucm.es/id/eprint/15010/1/jjcamposbueno_pavlov-cajal_art24.pdf"
    accessed: 2026-10-19
    source_quality: "scholarly edition or monograph"
    reliability_note: "Scholarly article; Madrid 1903 dating."
    used_for: [basics, timing]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "I. P. Pavlov (ed. Kh. S. Koshtoyants)"
    citation: "Pavlov, I. P. Selected Works, ed. Kh. S. Koshtoyants, trans. S. Belsky (Moscow: Foreign Languages Publishing House, 1955). Internet Archive."
    url: "https://archive.org/details/in.ernet.dli.2015.63960"
    accessed: 2026-10-19
    source_quality: "archive scan (OCR only)"
    reliability_note: "Edited collection; OCR read for introduction, editors note, lecture opening."
    used_for: [basics, timing]
  - id: S4
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [review]
  - id: S5
    type: secondary
    kind: "institutional page"
    author: "Daniel P. Todes"
    citation: "Todes, Daniel P. Ivan Pavlov in 22 surprising facts. OUPblog, 21 Nov 2014."
    url: "https://blog.oup.com/2014/11/ivan-pavlov-surprising-facts/"
    accessed: 2026-10-24
    source_quality: "scholarly reconstruction"
    reliability_note: "Author summary of Ivan Pavlov: A Russian Life in Science (OUP 2014). Fact 6: atheist. Full monograph pages not obtained this pass."
    used_for: [worldview, review]
  - id: S6
    type: secondary
    kind: "institutional page"
    author: "Roger Smith"
    citation: "Smith, Roger. Review of Daniel P. Todes, Ivan Pavlov: A Russian Life in Science. Somatosphere, 23 Jan 2015."
    url: "https://somatosphere.com/2015/pavlov.html/"
    accessed: 2026-10-24
    source_quality: "scholarly reconstruction"
    reliability_note: "Scholarly review: Todes puts to rest closet-believer story; atheism from the 1860s."
    used_for: [worldview]
  - id: S7
    type: secondary
    kind: "institutional page"
    author: "Kristina Emelyanenko (reporting Daniel P. Todes)"
    citation: "Emelyanenko, Kristina. Whats the Most Terrible Thing in Life: Ivan Pavlovs Last Winter. European University at St. Petersburg, 24 Sep 2015."
    url: "https://eusp.org/en/news/what-s-the-most-terrible-thing-in-life-ivan-pavlov-s-last-winter"
    accessed: 2026-10-24
    source_quality: "scholarly reconstruction"
    reliability_note: "Seminar report of Todes on unfinished late manuscripts and lifelong atheism."
    used_for: [worldview, review]
  - id: S8
    type: secondary
    kind: "journal article"
    author: "George Windholz"
    citation: "Windholz, George. Pavlovs Religious Orientation. Journal for the Scientific Study of Religion 25, no. 3 (1986): 320-27. doi:10.2307/1386296"
    url: "https://doi.org/10.2307/1386296"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Concludes Pavlov was personally an atheist while opposing persecution. Kreps quotation verified from standard citations of this article; JSTOR PDF closed this pass."
    used_for: [worldview]
  - id: S9
    type: secondary
    kind: "scholarly book"
    author: "B. P. Babkin"
    citation: "Babkin, B. P. Pavlov: A Biography. Chicago: University of Chicago Press, 1949. Internet Archive OCR (in.ernet.dli.2015.156540)."
    url: "https://archive.org/details/in.ernet.dli.2015.156540"
    accessed: 2026-10-24
    source_quality: "archive scan (OCR only)"
    reliability_note: "Pupil biography; religion chapter and Belief in Science (pp. 84-85) read in OCR."
    used_for: [childhood, worldview, heritage]

---

## Summary

Ivan Pavlov (1849–1936), physiologist [S1]. Deepen D1: ATHE (0.5; alt AGNOS); A BELOW; B 3 (0.5). Not plotted.

## Life and work

Ryazan; St Petersburg [S1]. Priest's son; left seminary for university 1870 [S1, S9].

## Contribution and impact

Conditioned reflex [S1]; Madrid 1903 [S2]. Nobel 1904 (digestion) [S1].

## Childhood and education

Church school and seminary; father a priest [S1, S9].

## Adult working worldview

Todes: atheism from the 1860s; defended religious freedom without being a believer [S5, S6]. Kreps via Windholz (reported speech): self-label 'atheist'; belief-in-God claims 'sheer fantasy' [S8]. Gantt alternative: 'scientific agnosticism' and envy of wife's faith [S1]; Babkin corroborates the envy line [S9]. A not scored from reported speech alone.

## Heritage (context only)

Russian Orthodox by birth (priest's son) [S1, S9].

## Timing

1903, age 54 [S2]. Atheism from 1860s per Todes covers the span [S5].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Full Todes monograph pages; late unfinished manuscript edition; Windholz/Kreps primary.

## Research log

- 2026-10-24: Deepen D1. Todes (OUP blog + Smith review + EUSP), Windholz/Kreps, Babkin OCR. primary AGNOS→ATHE @0.5; A stays BELOW (reported speech rule); B support corroborated. Viral student-letter unscored. No figures/.
- 2026-10-19: AA2 audit fixes: the Gantt paraphrase is undated, so its date is removed rather than set to his death year (P12; the schema's date field takes no UNKNOWN). Added S3, his Selected Works (Moscow 1955), whose editors date the Madrid paper to April 1903. No score change.
- 2026-10-19: Read Britannica (Gantt); Campos-Bueno excerpt.
