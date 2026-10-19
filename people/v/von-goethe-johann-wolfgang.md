---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch T)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch T, order P32: F 4, rank 110). Basics from Britannica (Boyle; body read only to 1769, the rest cut off in the fetch) and the IEP (Jensen). Worldview from his letters to F. H. Jacobi of 9 June 1785 and 6 January 1813 and to Knebel of 6 January 1785 (Weimarer Ausgabe IV, read in Zeno.org's transcription). Scientist (P30: intermaxillary bone 1784, Metamorphose der Pflanzen 1790). primary_system PANT (0.7); A 4 (0.7, alt 2); B 3 (0.5, alt 4); C, D UNKNOWN; E BELOW_THRESHOLD; mid_basin false (0.7). Plotted. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit fixes for batch T (blind audit of 754bb24, run 1: GO4, GO6 WEAKEN). IEP §2 now quoted verbatim ('it was Spinoza (1632-77) from whom Goethe adopted the view ...') in primary_system and the Spinoza note; 'left its mark' (which the IEP says of his organic ontology) dropped from the Metamorphose entry, now quoting 'his theory of morphology, that of Linnaeus’ biology'. Zeno/WA page locators: no. 2040 is p. 2 and no. 6471 is p. 226 (Zeno's [n] closes page n), in the statements, primary_system, self-described relation, the A cites and the A alternative. No value changes."}

identity:
  id: von-goethe-johann-wolfgang
  display_name: "Johann Wolfgang von Goethe"
  roster:
    canonical_name: "Johann Wolfgang von Goethe"
    rank: 110
    F: 4
    models: [Claude, DeepSeek, Gemini, Grok]
    band: "core (3–4)"
    status: core
    field: polymath
    field_bucket: polymath
  full_name: {value: "Johann Wolfgang von Goethe", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "title; §1"}], how_known: "Britannica and IEP agree; ennobled by Joseph II (S2)."}
  native_name: {value: "Johann Wolfgang von Goethe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "German; same as the display name."}
  aliases:
    - {name: "Goethe-Johann Wolfgang von", kind: "roster alias"}

basics:
  birth:
    date: {value: "1749-08-28", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "§1"}], how_known: "Britannica and IEP agree."}
    place: {value: "Frankfurt am Main", modern_name: "Frankfurt am Main, Germany", polity_then: "Free Imperial City of Frankfurt, Holy Roman Empire", certainty: 1.0, cites: [{source: S1, locator: "opening; Early years"}, {source: S2, locator: "§1"}], how_known: "Britannica and IEP agree; polity from Britannica ('virtually a self-governing republic, a city-state within the Holy Roman Empire')."}
  death:
    date: {value: "1832-03-22", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "§1"}], how_known: "Britannica and IEP agree."}
    place: {value: "Weimar", modern_name: "Weimar, Germany", polity_then: "Grand Duchy of Saxe-Weimar-Eisenach", certainty: 1.0, cites: [{source: S1, locator: "opening ('Weimar, Saxe-Weimar')"}, {source: S2, locator: "§1"}], how_known: "Britannica and IEP agree."}
  first_lasting_contribution_year: {value: 1773, certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "Götz von Berlichingen (1773), the earliest work the IEP credits with lasting influence ('all owe tremendous debts to Götz and Werther', §6); the 1770–71 song collections are not listed as lasting."}
  era_bucket: {value: "1750 to 1849", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "1773 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "§1"}], how_known: "Germany (P3)."}
  region_of_work: {value: "Western Europe", certainty: 1.0, cites: [{source: S2, locator: "§1"}, {source: S1, locator: "opening"}], how_known: "Weimar from 1775 (Germany)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S2, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["German"], certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "IEP; German titles."}
  occupations: {value: ["poet", "playwright", "novelist", "scientist", "statesman", "theatre director"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["literature", "morphology", "botany", "colour theory"], certainty: 0.7, cites: [{source: S2, locator: "§§1, 4, 5"}], how_known: "IEP."}
  lasting_original_contributions:
    - {value: "Götz von Berlichingen", year: 1773, kind: work, lasting: "Heine, Novalis and others 'all owe tremendous debts to Götz and Werther' (S2 §6)", certainty: 0.7, cites: [{source: S2, locator: "§§1, 6"}], how_known: "IEP."}
    - {value: "Die Leiden des jungen Werther", year: 1774, kind: work, lasting: "'brought Goethe nearly instant worldwide acclaim'; 'the archetype' of the Sturm und Drang (S2 §1)", certainty: 1.0, cites: [{source: S2, locator: "§1"}, {source: S1, locator: "opening ('the greatest German literary figure of the modern era')"}], how_known: "IEP; Britannica names him the greatest German literary figure of the era."}
    - {value: "Discovery of the intermaxillary bone in humans", year: 1784, kind: discovery, lasting: "named as his discovery (S2 §4)", certainty: 0.5, cites: [{source: S2, locator: "§4"}], how_known: "IEP names the discovery without calling it lasting; coder's call. With the Metamorphosis it makes him a scientist (P30)."}
    - {value: "Die Metamorphose der Pflanzen: plant organs as modifications of one basic form (morphology)", year: 1790, kind: theory, lasting: "'his theory of colors challenged the reigning paradigm of Newton’s optics; and his theory of morphology, that of Linnaeus’ biology' (S2, opening)", certainty: 0.7, cites: [{source: S2, locator: "opening; §4"}], how_known: "IEP; a theory about natural systems (P30)."}
    - {value: "Faust (Part One 1808; Part Two finished 1831, published 1832)", year: 1831, kind: work, lasting: "'Europe’s greatest long poem since John Milton’s Paradise Lost' (S1)", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "§1 ('having finally finished Faust the previous year')"}], how_known: "Britannica and IEP; dated by the end of writing (P30 posthumous rule). The latest listed lasting contribution (P30 addendum b)."}
  evidence_of_impact:
    - {value: "'considered the greatest German literary figure of the modern era'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours:
    - {value: "Ennobled by Emperor Joseph II; Geheimrat of Weimar (1782)", year: 1782, certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "IEP."}
  definition_fit: {value: "clearly meets", rationale: "(S1, S2).", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "opening"}], how_known: "Britannica and IEP."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father: Johann Caspar Goethe (1710–82), man of leisure on an inherited fortune, who directed his children's education", certainty: 1.0, cites: [{source: S1, locator: "Early years"}, {source: S2, locator: "§1"}], how_known: "Britannica and IEP."}
    - {value: "Mother: Catharina Elisabeth Textor (1731–1808), daughter of Frankfurt's most senior official", certainty: 1.0, cites: [{source: S1, locator: "Early years"}, {source: S2, locator: "§1"}], how_known: "Britannica and IEP."}
  household_circumstances: {value: "Wealthy bourgeois household in Frankfurt", certainty: 0.7, cites: [{source: S1, locator: "Early years"}], how_known: "Britannica."}
  schooling:
    - {value: "Educated at home by tutors until 16", stage: tutor, run_by: family, years: "–1765", certainty: 0.7, cites: [{source: S1, locator: "Early years"}], how_known: "Britannica."}
    - {value: "Law at Leipzig (1765–68, no degree) and Strasbourg (Licentiatus Juris 1771)", stage: university, run_by: "state or municipal", years: "1765–1771", certainty: 1.0, cites: [{source: S1, locator: "Early years"}, {source: S2, locator: "§1"}], how_known: "Britannica and IEP."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Studied alchemy in 1768–69 after his return from Leipzig", certainty: 0.7, cites: [{source: S1, locator: "Early years"}], how_known: "Britannica."}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["German", "Greek", "Latin", "French", "Italian"], certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "IEP: learned Greek, Latin, French and Italian 'relatively well by the age of eight'."}
  notable_events:
    - {value: "Severe illness in 1768–69, followed by 'a brief conversion from freethinking to evangelical Christianity'", year: 1769, certainty: 0.7, cites: [{source: S1, locator: "Early years"}], how_known: "Britannica; before the span (pre-1773)."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1773–1831", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Lutheran Frankfurt upbringing (coder's reading); opposed to the church wedding ceremony", certainty: 0.5, cites: [{source: S1, locator: "Early years"}], how_known: "Context only; the church-wedding remark is in Britannica's Top Questions box, which is not cited, so only the upbringing is noted (coder's reading)."}
  self_described_science_religion_relation: {value: "'als Dichter und Künstler bin ich Polytheist, Pantheist hingegen als Naturforscher, und eins so entschieden als das andre' (to Jacobi, 6 January 1813)", certainty: 0.7, cites: [{source: S3, locator: "WA IV 23, no. 6471, p. 226"}], how_known: "Private letter (web transcription of the Weimarer Ausgabe)."}
  primary_system:
    value: PANT
    basis: consistent_private_letters
    certainty: 0.7
    cites: [{source: S3, locator: "WA IV 7, no. 2134, pp. 61–63; WA IV 23, no. 6471, p. 226"}, {source: S2, locator: "§2"}]
    rationale: "Two-part test (PANT use_when). Part 1: on Spinoza, 'Er beweist nicht das Daseyn Gottes, das Daseyn ist Gott' — being itself is God — which he praises as 'theissimum ia christianissimum', and he knows the divine 'nur in und aus den rebus singularibus' and seeks it 'in herbis et lapidibus' (1785); in 1813, 'Pantheist hingegen als Naturforscher'. Part 2: 'die höchste Realität ..., welche der Grund des ganzen Spinozismus ist, worauf alles übrige ruht, woraus alles übrige fliest' (one ground of all). The IEP (§2): 'it was Spinoza (1632-77) from whom Goethe adopted the view that God is both immanent with the world and identical with it'. The 1813 letter also says he is a polytheist as a poet and that a God for his moral personality 'ist ... schon gesorgt' (context for A's alternative)."
    how_known: "Two consistent private letters 28 years apart, both inside the working years, plus a scholar (IEP); private ceiling 0.7."
  secondary_system: {value: UNKNOWN, how_known: "One system (P29)."}
  candidate_codes_considered:
    - {code: PANT, reason: "'das Daseyn ist Gott'; 'Pantheist ... als Naturforscher'; chosen."}
    - {code: PANENT, reason: "Rejected: no God that exceeds the world is stated."}
    - {code: CHRIST, reason: "Nominal upbringing and a brief 1769 conversion, before the span; rejected as working code."}
    - {code: ATHE, reason: "Rejected: the identity of God and being is a claim about what exists, with a mark beyond feeling (part 2)."}
  lio_axes:
    A_locus:
      value: 4
      basis: consistent_private_letters
      certainty: 0.7
      cites: [{source: S3, locator: "WA IV 7, no. 2134, pp. 61–62; WA IV 23, no. 6471, p. 226"}, {source: S2, locator: "§2"}]
      rationale: "Immanent pole: God identical with being ('das Daseyn ist Gott'), known only in and from singular things. Named alternative 2: in 1813 he holds different views in different domains — pantheist as natural scientist, polytheist as poet, and a God 'für meine Persönlichkeit, als sittlicher Mensch' — which matches the scale's 'holds both in different domains'."
      how_known: "Two private letters inside the working years; private ceiling and an alternative named, so 0.7."
      alternatives:
        - {value: 2, note: "Domain split in the 1813 letter.", cites: [{source: S3, locator: "WA IV 23, no. 6471, p. 226"}]}
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      cites: [{source: S3, locator: "WA IV 7, no. 2040, p. 2"}, {source: S2, locator: "§4"}]
      rationale: "Scored on his account of nature (P6). Working science (morphology: every organ 'built according to the same basic form', S2 §4) plus a remark on lawful order with no stated no-exception claim: 'der Wahrheit und Wichtigkeit der sich ewig immer gleichen Natur' (to Knebel, 1785). B 3 at 0.5 with 4 as the named alternative (P35; P16 addendum logic)."
      how_known: "Working science and one remark in a private letter; P35 gives 0.5."
      alternatives:
        - {value: 4, note: "P35: working science cannot rule out a lawful nature with no exception.", cites: [{source: S2, locator: "§4"}]}
    C_ledger: {value: UNKNOWN, how_known: "The sources read say nothing on reward and punishment of persons (P19)."}
    D_authority: {value: UNKNOWN, how_known: "The sources read say nothing on revelation against observation (P19)."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Not scored from working science alone (P19); 'die Consequenz der Natur' (to Knebel, 2 April 1785, WA IV 7, no. 2091) is a lead, not a statement that the same rules govern humans."}
  mid_basin: {value: false, certainty: 0.7, cites: [{source: S3, locator: "WA IV 7, no. 2134"}], how_known: "P4 test: A 4 at 0.7; the A ≥ 3 branch reads A only (P10). A's named alternative 2 would leave the test without a branch."}
  statements:
    - text: "Du erkennst die höchste Realität an, welche der Grund des ganzen Spinozismus ist, worauf alles übrige ruht, woraus alles übrige fliest. Er beweist nicht das Daseyn Gottes, das Daseyn ist Gott. Und wenn ihn andre deshalb Atheum schelten, so mögte ich ihn theissimum ia christianissimum nennen und preisen."
      cites: [{source: S3, locator: "WA IV 7, no. 2134, p. 61"}]
      date: "1785-06-09"
      context: "Letter from Ilmenau to Friedrich Heinrich Jacobi, answering Jacobi's book on Spinoza's doctrine (the pantheism controversy)."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "Weimarer Ausgabe IV, read in Zeno.org's web transcription with WA page numbers."
    - text: "Vergieb mir daß ich so gerne schwiege wenn von einem göttlichen Wesen die Rede ist, das ich nur in und aus den rebus singularibus erkenne, zu deren nähern und tiefern Betrachtung niemand mehr aufmuntern kann als Spinoza selbst, obgleich vor seinem Blicke alle einzelne Dinge zu verschwinden scheinen."
      cites: [{source: S3, locator: "WA IV 7, no. 2134, p. 62"}]
      date: "1785-06-09"
      context: "Same letter; it closes 'Hier bin ich auf und unter Bergen, suche das göttliche in herbis et lapidibus.'"
      axes: [A_locus]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "As above."
    - text: "Ich für mich kann, bey den mannigfaltigen Richtungen meines Wesens, nicht an einer Denkweise genug haben; als Dichter und Künstler bin ich Polytheist, Pantheist hingegen als Naturforscher, und eins so entschieden als das andre. Bedarf ich eines Gottes für meine Persönlichkeit, als sittlicher Mensch, so ist dafür auch schon gesorgt."
      cites: [{source: S3, locator: "WA IV 23, no. 6471, p. 226"}]
      date: "1813-01-06"
      context: "Letter from Weimar to Jacobi, answering his New Year letter: 'Die Menschen werden durch Gesinnungen vereinigt, durch Meynungen getrennt.'"
      axes: [A_locus]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "As above. The basis of A's alternative 2."
    - text: "Bey der offenbaren Nichtigkeit sovieler andrer Dinge und der Wahrheit und Wichtigkeit der sich ewig immer gleichen Natur giebt mich's nicht wunder."
      cites: [{source: S3, locator: "WA IV 7, no. 2040, p. 2"}]
      date: "1785-01-06"
      context: "Letter to Carl Ludwig von Knebel, on the theologian Semler's turn to natural history."
      axes: [B_cause]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "As above."
  changes_over_life:
    - {value: "1768–69: brief conversion from freethinking to evangelical Christianity during illness, before the span", certainty: 0.7, cites: [{source: S1, locator: "Early years"}], how_known: "Britannica."}
  coder_notes: "Coder's call. Two private letters (1785, 1813) carry primary_system and A; the published Dichtung und Wahrheit (books 14 and 16, on Spinoza) is an unread lead that could raise the basis to written_profession. A character's words (Faust, 'Prometheus') are not used (P42). The fetched Britannica text stops after 1769; its later sections were not read."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German (Frankfurt bourgeoisie)", certainty: 0.7, cites: [{source: S1, locator: "Early years"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1773–1831", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "Götz (1773) to the end of writing Faust II (1831), first to last listed lasting contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 24, certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "1773 − 1749 = 24 (P30)."}
  first_evidence_of_lio_type_views: {value: "1785: 'das Daseyn ist Gott'", year: 1785, certainty: 0.5, cites: [{source: S3, locator: "WA IV 7, no. 2134"}], how_known: "Earlier letters not searched."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S3, locator: "WA IV 7, 23"}], how_known: "1785 and 1813, inside 1773–1831."}
  worldview_during_major_work: {value: "Spinozist pantheism in natural science, with poetic polytheism and a moral God in their own domains", certainty: 0.7, cites: [{source: S3, locator: "WA IV 23, no. 6471"}], how_known: "His letters."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Morphology and intuition, not deduction.", certainty: 0.5, cites: [{source: S2, locator: "§4"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "§2"}], how_known: "Not read."}
  circle_present: {value: "yes", rationale: "'das Daseyn ist Gott'.", certainty: 0.7, cites: [{source: S3, locator: "WA IV 7, no. 2134"}], how_known: "His letter."}
  reading: "A Spinozist naturalist who keeps poetry and morals in their own domains."
  notes: ""

institutions:
  - {value: "Court of Saxe-Weimar", role: "privy councillor; mines, finance, war and roads commissions; theatre", years: "1775–1832", kind: "government or state body", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "IEP."}
collaborators:
  - {value: "Friedrich Schiller", relation: collaborator, note: "close collaboration 1794–1805", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "IEP."}
  - {value: "Johann Gottfried Herder", relation: "influenced by", note: "met in Strasbourg, 1770; shared reading of Spinoza", certainty: 0.7, cites: [{source: S2, locator: "§1"}, {source: S3, locator: "WA IV 7, no. 2047"}], how_known: "IEP; his letter to Jacobi of 12 January 1785."}
  - {value: "Friedrich Heinrich Jacobi", relation: correspondent, note: "letters on Spinoza (1785, 1813)", certainty: 0.7, cites: [{source: S3, locator: "WA IV 7, no. 2134"}], how_known: "His letters."}
  - {value: "Baruch Spinoza", roster_id: spinoza-baruch, relation: "influenced by", note: "'it was Spinoza (1632-77) from whom Goethe adopted the view that God is both immanent with the world and identical with it' (S2 §2)", certainty: 0.7, cites: [{source: S2, locator: "§2"}], how_known: "IEP."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 110"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Britannica fetch cut off after the early years; later facts rest on the IEP."
    - "Letters read in a web transcription of the Weimarer Ausgabe (Zeno.org)."
  open_questions:
    - "Read Dichtung und Wahrheit (books 14, 16) on Spinoza."
    - "Childhood religion."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Nicholas Boyle"
    citation: "Boyle, Nicholas. \"Johann Wolfgang von Goethe.\" Encyclopaedia Britannica (revised 3 September 2026). https://www.britannica.com/biography/Johann-Wolfgang-von-Goethe. Read live 2026-10-19 (opening and 'Early years (1749–69)' only)."
    url: "https://www.britannica.com/biography/Johann-Wolfgang-von-Goethe"
    accessed: 2026-10-19
    reliability_note: "Signed article. Body only; the AI-generated question boxes are not cited. Later sections not retrieved."
    used_for: [identity, basics, contribution, childhood, worldview, heritage]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Anthony K. Jensen"
    citation: "Jensen, Anthony K. \"Goethe, Johann Wolfgang von.\" Internet Encyclopedia of Philosophy. https://iep.utm.edu/goethe/"
    url: "https://iep.utm.edu/goethe/"
    accessed: 2026-10-19
    reliability_note: "Signed, peer-reviewed encyclopedia article. Section numbers: §1 Life and Works, §2 Philosophical Background, §4 Science and Methodology, §5 Theory of Colors, §6 Influence."
    used_for: [identity, basics, contribution, childhood, worldview, timing, institutions, collaborators, lane_b]
  - id: S3
    type: primary
    kind: letter
    author: "Johann Wolfgang von Goethe"
    citation: "Goethe, Johann Wolfgang. Briefe. Goethes Werke, Weimarer Ausgabe, Abt. IV, vols. 7 (1785) and 23 (1813). Read in Zeno.org's transcription: http://www.zeno.org/Literatur/M/Goethe,+Johann+Wolfgang/Briefe/1785 and /1813."
    url: "http://www.zeno.org/Literatur/M/Goethe,+Johann+Wolfgang/Briefe/1785"
    accessed: 2026-10-19
    reliability_note: "Web transcription of the scholarly edition, with WA letter and page numbers; not checked against the printed volumes (0.7 cap in any case for private letters)."
    used_for: [worldview, timing, lane_b, collaborators]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Johann Wolfgang von Goethe

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Johann Wolfgang von Goethe (1749–1832), German poet, dramatist and scientist [S1, S2]. Draft: primary_system PANT (0.7); A 4 at 0.7 (alt 2); B 3 at 0.5 (alt 4); C, D UNKNOWN; E BELOW_THRESHOLD; mid_basin false (0.7). Plotted.

## Life and work

Frankfurt, Leipzig, Strasbourg, Weimar from 1775 [S1, S2].

## Contribution and impact

Götz (1773), Werther (1774), the intermaxillary bone (1784), the Metamorphosis of Plants (1790), Faust (finished 1831) [S1, S2].

## Childhood and education

Home tutors; law at Leipzig and Strasbourg [S1, S2].

## Adult working worldview

'Er beweist nicht das Daseyn Gottes, das Daseyn ist Gott' [S3, WA IV 7, p. 61].

## Heritage (context only)

Frankfurt bourgeoisie [S1].

## Timing

1773–1831, from age 24 [S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. God as being itself [S3].

## Open questions

- Dichtung und Wahrheit on Spinoza.

## Research log

- 2026-10-19: Read Britannica (live, opening and early years), the IEP article, and the 1785 and 1813 letters in Zeno.org's WA transcription.
