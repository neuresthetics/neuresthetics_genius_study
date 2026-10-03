---
record:
  record_type: person
  schema_version: "1.2"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (executor agent for v8, RUNBOOK stage 3, batch A: early modern philosophers)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (stage 3, batch A). Basics from SEP 'Immanuel Kant' (Rohlf) and Britannica (Bird, first page); religion from SEP 'Kant's Philosophy of Religion' (Pasternack). Worldview quotations read in the Akademie-Ausgabe text of the Bonner Kant-Korpus (AA III, V, VI), a scholarly edition. DRAFT SCORES for v8's review: primary_system BELOW_THRESHOLD (best fit KANT is a stub file); A 1, B 4, C 1, D 4, E 4, all at 0.7; mid_basin true (0.7). Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit fixes, stage 3 batch A (two blind runs at 59a8371). #379: 'lived his entire life' now cited to Britannica 'Background and early years' and SEP religion §2.1.1, not SEP §1. #405: early_mathematics 'other' (curriculum only; no source says advanced). #415: wording only; he declines to contest revelation and miracles (AA VI 155; VI 88 n.) rather than accepting them; value unchanged. #390: stray 'ancestor gloss' wording fixed. #420: heading §3.3.1.2 rechecked in the live entry; kept. Bylines: SEP religion now Pasternack and Fugate; Britannica now Bird and Duignan. #416, #456 left (stub-system rule awaits v8). Not reviewed."}

identity:
  id: kant-immanuel
  display_name: "Immanuel Kant"
  roster:
    canonical_name: "Immanuel Kant"
    rank: 41
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Immanuel Kant", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "opening"}], how_known: "Two sources."}
  native_name: {value: "Immanuel Kant", certainty: 1.0, cites: [{source: S3, locator: "opening"}], how_known: "German name as given."}
  aliases:
    - {name: "Immanuel-Kant", kind: "roster alias"}
    - {name: "Kant-Immanuel", kind: "roster alias"}

basics:
  birth:
    date: {value: "1724-04-22", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "opening"}], how_known: "Two sources agree."}
    place: {value: "Königsberg, East Prussia", modern_name: "Kaliningrad, Russia", polity_then: "Kingdom of Prussia", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "opening"}], how_known: "Two sources agree."}
  death:
    date: {value: "1804-02-12", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "opening"}], how_known: "Two sources agree."}
    place: {value: "Königsberg", modern_name: "Kaliningrad, Russia", polity_then: "Kingdom of Prussia", certainty: 1.0, cites: [{source: S3, locator: "opening; 'Background and early years'"}, {source: S2, locator: "§2.1.1"}], how_known: "Britannica gives the death place and says 'Kant lived in the remote province where he was born for his entire life' ('Background and early years'); SEP 'Kant's Philosophy of Religion' says he 'lived his entire life in the city of Königsberg' (S2 §2.1.1). SEP 'Immanuel Kant' §1 does not say so; it has him spend six years as a private tutor 'outside Königsberg' (lens audit #379)."}
  first_lasting_contribution_year: {value: 1755, certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "Universal Natural History and Theory of the Heavens (1755), with what became the nebular hypothesis. The coder's choice; his first book (Living Forces, 1746/1747) was not lasting. The Critique of Pure Reason (1781) gives the same era bucket."}
  era_bucket: {value: "1750 to 1849", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "From first_lasting_contribution_year (P2)."}
  region_of_birth: {value: "Eastern Europe", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "Königsberg is now Kaliningrad, Russia (S1); Russia is Eastern Europe in data/reference/regions.csv (P3: modern country; the historical polity is in place.polity_then). Flagged because it puts a Prussian in Eastern Europe."}
  region_of_work: {value: "Eastern Europe", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "Worked all his life in Königsberg; same modern-country rule (P3) and flag as region_of_birth."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "As the sources record it."}
  languages_of_work: {value: [German, Latin], certainty: 1.0, cites: [{source: S1, locator: "§1 (German works; Latin dissertations of 1755–1756)"}], how_known: "SEP."}
  occupations: {value: [philosopher, "university professor", "private tutor"], certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "opening"}], how_known: "Two sources."}

contribution:
  fields: {value: [epistemology, metaphysics, ethics, aesthetics, "natural philosophy", "philosophy of religion"], certainty: 1.0, cites: [{source: S3, locator: "opening"}, {source: S1, locator: "§1"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Transcendental idealism and the critical philosophy (the understanding as source of the general laws of nature; knowledge limited to appearances)", year: "1781", kind: theory, lasting: "foundation of later Kantianism and idealism", certainty: 1.0, cites: [{source: S1, locator: "opening; §§2–3"}, {source: S3, locator: "opening"}], how_known: "Two sources."}
    - {value: "The categorical imperative and the autonomy of the will", year: "1785–1788", kind: "law or principle", lasting: "central in moral philosophy", certainty: 1.0, cites: [{source: S1, locator: "§5"}], how_known: "SEP."}
    - {value: "Nebular hypothesis of the formation of the solar system", year: "1755", kind: theory, lasting: "ancestor of modern accounts of planet formation", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP; the 'ancestor' wording in lasting is the coder's (flag)."}
  evidence_of_impact:
    - {value: "Arguably one of the greatest philosophers of all time; his work greatly influenced all subsequent philosophy", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S3, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Universal Natural History and Theory of the Heavens", year: 1755, kind: book, certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
    - {value: "Critique of Pure Reason (2nd ed. 1787)", year: 1781, kind: book, certainty: 1.0, cites: [{source: S1, locator: "opening; §1"}, {source: S3, locator: "opening"}], how_known: "Two sources."}
    - {value: "Critique of Practical Reason", year: 1788, kind: book, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "opening"}], how_known: "Two sources."}
    - {value: "Critique of the Power of Judgment", year: 1790, kind: book, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "opening"}], how_known: "Two sources."}
    - {value: "Religion within the Boundaries of Mere Reason", year: 1793, kind: book, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "§1"}], how_known: "Two sources."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founder of the critical philosophy; one of the most influential philosophers.", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "opening"}], how_known: "Sources agree."}

childhood:
  family_religion: {value: "Lutheran Pietist", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "'Background and early years'"}], how_known: "Two sources: both parents were Pietists (devoted followers of the Pietist branch of the Lutheran church)."}
  family_religious_practice: {value: "Devout Pietist parents; his mother's 'genuine religiosity' he described as 'not at all enthusiastic'", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "'Background and early years'"}], how_known: "Two sources."}
  parents_and_household:
    - {value: "Father, a master harness maker (saddler); died 1746", role: father, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "'Background and early years'"}], how_known: "Two sources; his name is not given in the pages read."}
    - {value: "Mother, daughter of a harness maker, better educated than most women of her class", role: mother, certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "'Background and early years'"}], how_known: "SEP; Britannica praises her character and intelligence."}
  household_circumstances: {value: "Artisan family of modest means, the fourth of nine children and eldest surviving; never destitute but at times dependent on extended family", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "'Background and early years'"}], how_known: "Two sources."}
  schooling:
    - {value: "Collegium Fridericianum, a Pietist Latin school (gymnasium) directed by Franz Albert Schultz, the family's pastor", stage: "religious school", years: "1732–1740", certainty: 0.7, cites: [{source: S1, locator: "§1 (ages eight through fifteen)"}, {source: S3, locator: "'Background and early years' (from age eight, eight and a half years; directed by his pastor)"}, {source: S2, locator: "§2.1.1 (directed by Schultz)"}], how_known: "Three sources; the length differs (ages 8–15 vs eight and a half years); years are the coder's arithmetic. That Schultz was the pastor Britannica mentions is the coder's link of S2 and S3 (flag)."}
    - {value: "University of Königsberg (the Albertina): philosophy, mathematics and physics; enrolled as a theological student per Britannica", stage: university, years: "1740–c. 1746", certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "'Background and early years'"}], how_known: "Two sources; the end year is approximate (father's death in 1746 forced him to withdraw, S3)."}
  early_mathematics: {value: "other", note: "Mathematics and physics in first-year philosophy at the Albertina, from 1740 (age 16): philosophy 'encompassed mathematics and physics' (SEP), and he was 'principally attracted to mathematics and physics' (Britannica). The level he reached is not stated.", certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "'Background and early years'"}], how_known: "Two sources; neither gives a level, so the value is 'other' with a description, as in the Bohr record, not 'advanced mathematics' (lens audit #405). This is at university (age 16+), inside the before-18 window."}
  early_geometric_style_reasoning: {value: "Latin classics at school; Wolffian rationalist philosophy and Newton at university (Knutzen)", certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "'Background and early years'"}], how_known: "Two sources."}
  early_science_exposure:
    - {value: "Introduced to Newton's work by Martin Knutzen at the Albertina", year: "1740s", age: "16–22", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "'Background and early years'"}], how_known: "Two sources."}
  key_early_reading:
    - {value: "Latin classics, especially Lucretius", certainty: 0.7, cites: [{source: S3, locator: "'Background and early years'"}, {source: S1, locator: "§1"}], how_known: "Britannica names Lucretius ('presumably'); SEP the Latin classics."}
  childhood_mentors:
    - {value: "The family's pastor, who made his schooling possible and directed the school", certainty: 0.7, cites: [{source: S3, locator: "'Background and early years'"}], how_known: "Britannica (unnamed there); SEP S2 §2.1.1 names Franz Albert Schultz as the school's director."}
  languages_in_childhood: {value: [German, Latin], certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "'Background and early years'"}], how_known: "German-speaking Königsberg; Latin school."}
  notable_events:
    - {value: "Reacted strongly against the 'forced soul-searching' of his Pietist schooling", year: "1732–1740", age: "8–15", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP, after Kuehn."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1746–1798", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "First book to the Conflict of the Faculties."}
  nominal_affiliations:
    - {value: "Lutheran by upbringing (Pietist)", certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "§2.1.1"}], how_known: "Upbringing from both SEP entries; his adult church practice is not stated in what was read."}
  self_described_science_religion_relation:
    value: "Knowledge is limited to appearances so that faith has room: 'Ich mußte also das Wissen aufheben, um zum Glauben Platz zu bekommen' (KrV, B XXX). God is a postulate of pure practical reason, morally necessary to assume (KpV, AA V 125); in the investigation of nature miracles are never reckoned with (Religion, AA VI 87–88)."
    certainty: 0.7
    cites: [{source: S4, locator: "AA III 19"}, {source: S5, locator: "AA V 125"}, {source: S6, locator: "AA VI 87–88"}]
    how_known: "His own published works in the Akademie-Ausgabe text; 0.7 because SEP (S2 §3.3.1) names competing readings of what kind of assent this is."
  primary_system:
    value: BELOW_THRESHOLD
    cites: [{source: S5, locator: "AA V 124–125"}, {source: S6, locator: "AA VI 153–155"}, {source: S2, locator: "§3.2; §3.6"}]
    how_known: "His own position is a moral faith: God and immortality as postulates of practical reason, religion as 'das Erkenntniß aller unserer Pflichten als göttlicher Gebote' (AA VI 153), miracles and petition kept out of the maxims of reason. The code that fits is KANT (Kantianism), and KANT is a stub system file, so under the stub rule it cannot be coded."
    note: "Candidate: KANT (stub). Founders rule conflict: he is the founder of the system the code names, so a reviewer may want KANT at 1.0 once the file is filled (see report method question). Also considered: CLASS_THEISM (no: he rejects the theoretical proofs of God, S2 §3.1.2), DEISM (no: his own 'Deism' means the useless God of transcendental theology, S2 §3.2. DEISM's do_not_use_when names a person who 'accepts revelation and miracles'; Kant does not accept them either: he declines to contest revelation, AA VI 155, and he does not take belief in miracles into the maxims of reason, 'ohne doch ihre Möglichkeit oder Wirklichkeit anzufechten', AA VI 88 n. So that clause fits only in part, and the rejection rests on S2 §3.2; lens audit #415), CHRIST (Pasternack's 'successful Christian apologist' reading, S2 §3.6.1; not coded, because he subordinates church faith to pure rational faith, AA VI 153). Backlog: fill KANT."
  secondary_system: {value: UNKNOWN, how_known: "No second system in what was read."}
  candidate_codes_considered:
    - {code: KANT, reason: "Best fit; not coded because KANT is a stub system file (BELOW_THRESHOLD by rule).", cites: [{source: S5, locator: "AA V 124–125"}, {source: S6, locator: "AA VI 153"}]}
    - {code: CHRIST, reason: "Considered: Lutheran Pietist upbringing; extensive treatment of Christian doctrines; one reading makes him a Christian apologist (S2 §3.6.1). Not coded: church faith is a vehicle that the true church should be able to do without in time ('den Kirchenglauben [...] mit der Zeit entbehren zu können', AA VI 153). CHRIST is a draft system file.", cites: [{source: S2, locator: "§3.6"}, {source: S6, locator: "AA VI 153"}]}
    - {code: DEISM, reason: "Considered and rejected: in Kant's own terms the deist's God is 'useless' and he favours 'Theism' (S2 §3.2); he does not contest revelation (AA VI 155).", cites: [{source: S2, locator: "§3.2"}, {source: S6, locator: "AA VI 155"}]}
    - {code: CLASS_THEISM, reason: "Rejected: he denies that God can be proved by theoretical reason (S2 §3.1.2; S1 §2.2).", cites: [{source: S2, locator: "§3.1.2"}]}
  lio_axes:
    A_locus:
      value: 1
      basis: written_profession
      certainty: 0.7
      cites: [{source: S5, locator: "AA V 124–125"}, {source: S2, locator: "§3.3.1; §3.5.1"}]
      how_known: "His own published text in a scholarly edition; capped at 0.7 because SEP names competing readings (S2 §3.3.1)."
      rationale: "DRAFT. Leans to the transcendent-person pole: the postulate is 'das Dasein einer von der Natur unterschiedenen Ursache der gesammten Natur', and that cause is 'ein Wesen, das durch Verstand und Willen die Ursache (folglich der Urheber) der Natur ist, d. i. Gott' (KpV, AA V 125): distinct from nature, with understanding and will. Not 0, because God is held only as a postulate, 'subjectiv, d. i. Bedürfniß' (AA V 125), and is not known. Named alternatives: 0 (personal author and judge), and 2 or BELOW_THRESHOLD on the reading that God is held 'Only as a mere symbol' (S2 §3.3.1.2, heading)."
    B_cause:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "AA III 166"}, {source: S6, locator: "AA VI 87–88"}]
      how_known: "His own published texts in a scholarly edition; a named alternative (3)."
      rationale: "DRAFT. Scored on his account of nature (P6). At the LIO pole: 'Alle Veränderungen geschehen nach dem Gesetze der Verknüpfung der Ursache und Wirkung' (KrV, Second Analogy, AA III 166). The natural scientist's business is to seek the causes of events 'in dieser ihren Naturgesetzen' (Religion, AA VI 87), and experiences 'sind [...] nichts anders als Naturwirkungen und sollen auch nie anders beurtheilt werden' (AA VI 88). Reason must either admit miracles daily or never, and only 'never' is compatible with reason (AA VI 88). Named alternative: 3, because he does not deny miracles: he does not take them into his maxims 'ohne doch ihre Möglichkeit oder Wirklichkeit anzufechten' (AA VI 88 n.), and the free noumenal self is 'not part of nature' (S1 §5.2)."
    C_ledger:
      value: 1
      basis: written_profession
      certainty: 0.7
      cites: [{source: S5, locator: "AA V 124–125"}, {source: S1, locator: "§6"}]
      how_known: "His own published text in a scholarly edition; a named alternative (2)."
      rationale: "DRAFT, judgment call. Leans to personal reward: the highest good is happiness in 'der genauen Übereinstimmung der Glückseligkeit mit der Sittlichkeit', and a supreme cause of nature is postulated to secure it (AA V 125), with the immortality postulate (AA V 124; S1 §6.2). Limited: the moral law must be followed without regard to reward, and happiness follows worthiness by the author of nature rather than by a ledger of rites; the postulate is a need of reason, not knowledge. Named alternative: 2."
    D_authority:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S6, locator: "AA VI 153–155"}, {source: S4, locator: "AA III 19"}]
      how_known: "His own published texts in a scholarly edition; a named alternative (3)."
      rationale: "DRAFT. At the reason pole: religion is 'das Erkenntniß aller unserer Pflichten als göttlicher Gebote' (AA VI 153); in natural religion one must first know that something is a duty before recognising it as a divine command (AA VI 154); a statutory church is the true one only in so far as it approaches 'dem reinen Vernunftglauben' and can in time do without church faith (AA VI 153). Named alternative: 3, because he does not contest the possibility of revelation or its use as a vehicle (AA VI 155), and SEP reads his religion as more affirmative of Christian doctrine (S2 §3.6)."
    E_scope:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "AA III 166"}, {source: S6, locator: "AA VI 87–88; 194"}]
      how_known: "His own published texts in a scholarly edition; a named alternative (3)."
      rationale: "DRAFT. Scored on the world's order (P7). At the LIO pole: one law of cause and effect for all changes (AA III 166); 'In Geschäften kann man also unmöglich auf Wunder rechnen' (AA VI 87); and petition as a means of grace is 'ein abergläubischer Wahn (ein Fetischmachen)' (AA VI 194). No favour for a group in events. The ethical community and the highest good are C matters (P7). Named alternative: 3 (miracles not denied, AA VI 88 n.)."
  mid_basin: {value: true, certainty: 0.7, cites: [{source: S5, locator: "AA V 125"}, {source: S4, locator: "AA III 166"}], how_known: "P4/P6 test: A_locus 1 (0.7) ≤ 1 and B_cause 4 (0.7) ≥ 3, both at ≥ 0.7, so true. Certainty is the lower of the two (0.7). DRAFT: the result holds for A 0 and B 3; it would fail if A were read as 2 (the symbol-only reading)."}
  statements:
    - text: "Ich mußte also das Wissen aufheben, um zum Glauben Platz zu bekommen"
      cites: [{source: S4, locator: "AA III 19 (B XXX)"}]
      date: "1787"
      context: "Preface to the second edition of the Critique of Pure Reason; B XXX per SEP (S1 §2.2; S2 §1). In SEP's English: 'I had to deny knowledge in order to make room for faith'."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "Alle Veränderungen geschehen nach dem Gesetze der Verknüpfung der Ursache und Wirkung."
      cites: [{source: S4, locator: "AA III 166"}]
      date: "1787"
      context: "Critique of Pure Reason, second edition, principle of the Second Analogy."
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "Also wird auch das Dasein einer von der Natur unterschiedenen Ursache der gesammten Natur, welche den Grund dieses Zusammenhanges, nämlich der genauen Übereinstimmung der Glückseligkeit mit der Sittlichkeit, enthalte, postulirt."
      cites: [{source: S5, locator: "AA V 125"}]
      date: "1788"
      context: "Critique of Practical Reason, Dialectic, section V, 'Das Dasein Gottes, als ein Postulat der reinen praktischen Vernunft'."
      axes: [A_locus, C_ledger]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "Also ist die oberste Ursache der Natur, so fern sie zum höchsten Gute vorausgesetzt werden muß, ein Wesen, das durch Verstand und Willen die Ursache (folglich der Urheber) der Natur ist, d. i. Gott."
      cites: [{source: S5, locator: "AA V 125"}]
      date: "1788"
      context: "Same section."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "daß diese moralische Nothwendigkeit subjectiv, d. i. Bedürfniß, und nicht objectiv, d. i. selbst Pflicht, sei"
      cites: [{source: S5, locator: "AA V 125"}]
      date: "1788"
      context: "Same section: the necessity of assuming God's existence is a need of reason, not a duty."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "In Geschäften kann man also unmöglich auf Wunder rechnen, oder sie bei seinem Vernunftgebrauch (und der ist in allen Fällen des Lebens nöthig) irgend in Anschlag bringen."
      cites: [{source: S6, locator: "AA VI 87"}]
      date: "1793"
      context: "Religion, General Remark to Part Two (on miracles); he goes on to count the natural scientist's work among such 'Geschäfte'."
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "er nimmt den Wunderglauben nicht in seine Maximen (weder der theoretischen noch praktischen Vernunft) auf, ohne doch ihre Möglichkeit oder Wirklichkeit anzufechten."
      cites: [{source: S6, locator: "AA VI 88, note"}]
      date: "1793"
      context: "Footnote glossing 'statuirt [...] keine Wunder' in the same remark."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "Aber es sind Erfahrungen; für uns sind sie also nichts anders als Naturwirkungen und sollen auch nie anders beurtheilt werden"
      cites: [{source: S6, locator: "AA VI 88, note"}]
      date: "1793"
      context: "Same long note, on whether the preservation of species needs a direct influence of the Creator each time."
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "Religion ist (subjectiv betrachtet) das Erkenntniß aller unserer Pflichten als göttlicher Gebote"
      cites: [{source: S6, locator: "AA VI 153"}]
      date: "1793"
      context: "Religion, Part Four, Part One, opening definition."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "Das Beten, als ein innerer förmlicher Gottesdienst und darum als Gnadenmittel gedacht, ist ein abergläubischer Wahn (ein Fetischmachen)"
      cites: [{source: S6, locator: "AA VI 194"}]
      date: "1793"
      context: "Religion, General Remark to Part Four, on means of grace; he keeps 'der Geist des Gebets' as a moral disposition (AA VI 195)."
      axes: [E_scope]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
  changes_over_life:
    - {value: "Pre-critical natural theology (his own argument for God's existence in The Only Possible Argument, 1763) gave way in the critical period to the denial of theoretical proofs and a moral faith", year: "1763; 1781", certainty: 0.7, cites: [{source: S2, locator: "§2.2.1; §2.2.3; §3.1.2"}], how_known: "SEP Pasternack."}
  coder_notes: "DRAFT SCORES for v8's review. All own-word quotations were read in the Bonner Kant-Korpus (korpora.org), the electronic text of the Akademie-Ausgabe, and are cited by AA volume and page; the §7 cap for unofficial copies does not apply, but every axis names an alternative, so all sit at 0.7. German quoted as printed in AA (e.g. 'Erkenntniß', 'nothwendig'). The Gutenberg English texts (Abbott, Meiklejohn) were downloaded but not used for quotations. KANT is a stub: primary_system is BELOW_THRESHOLD by the stub rule (report backlog). Region coded by modern country (Russia), which puts a Prussian in Eastern Europe (flag)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German-speaking artisan family of Königsberg; Kant claimed a Scottish descent for his father, for which scholars found no basis", certainty: 0.7, cites: [{source: S3, locator: "'Background and early years'"}, {source: S1, locator: "§1"}], how_known: "Britannica on the claim; SEP on the family."}
  religious_heritage_by_birth: {value: "Lutheran Pietist", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "'Background and early years'"}], how_known: "Two sources."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: "Pietist schooling at the Collegium Fridericianum", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "'Background and early years'"}], how_known: "Two sources."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1755–1798", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "Universal Natural History to the Conflict of the Faculties."}
  age_at_first_lasting_contribution: {value: 31, certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "Born April 1724; Universal Natural History 1755."}
  first_evidence_of_lio_type_views: {value: "Lawful mechanical formation of the solar system (nebular hypothesis) in Universal Natural History", year: 1755, age: 31, certainty: 0.5, cites: [{source: S1, locator: "§1"}], how_known: "SEP names the hypothesis; reading it as an LIO-type view of nature is the coder's, and the book itself was not read."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "Lawful nature from 1755; the full exclusion of miracles from the maxims of reason in 1793.", certainty: 0.5, cites: [{source: S1, locator: "§1"}, {source: S6, locator: "AA VI 87–88"}], how_known: "Dates of what was read."}
  worldview_during_major_work: {value: "Moral faith of the critical period (no coded system: KANT is a stub)", certainty: 0.7, cites: [{source: S5, locator: "AA V 125"}, {source: S6, locator: "AA VI 153"}], how_known: "His own texts of 1788 and 1793."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "Trained in Wolffian demonstrative philosophy and taught mathematics (S1 §1), but the critical philosophy argues that philosophy cannot proceed by the mathematician's method of constructing concepts (not read directly here).", certainty: 0.5, cites: [{source: S1, locator: "§1"}], how_known: "SEP on his training and teaching; the critical point is the coder's knowledge and not checked in a source read (flag)."}
  form_acquired: {value: "adulthood, before major work", certainty: 0.5, cites: [{source: S1, locator: "§1"}], how_known: "Mathematics and physics at the Albertina from 1740."}
  circle_present: {value: "no", rationale: "God is 'eine[r] von der Natur unterschiedenen Ursache' (AA V 125), postulated, not identified with nature.", certainty: 0.7, cites: [{source: S5, locator: "AA V 125"}], how_known: "His own words in a scholarly edition."}
  reading: "As belief, not finding: lawful nature at the LIO pole with a transcendent moral author held by faith. Passes mid_basin; circle absent."
  notes: ""

institutions:
  - {value: "University of Königsberg (Albertina)", role: "unsalaried lecturer 1755–1770, then professor of logic and metaphysics until he stopped teaching in 1796", years: "1755–1796", kind: university, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "opening ('Privatdozent' 15 years, then the chair)"}], how_known: "Two sources."}
collaborators:
  - {value: "Martin Knutzen", relation: teacher, note: "favourite teacher; introduced him to Newton", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "'Background and early years'"}], how_known: "Two sources (Britannica describes the teacher without naming him)."}
  - {value: "Isaac Newton", roster_id: newton-isaac, relation: "influenced by", note: "Newton's physics, through Knutzen", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "'Background and early years'"}], how_known: "Two sources."}
  - {value: "Gottfried Wilhelm Leibniz", roster_id: leibniz-gottfried-wilhelm, relation: "influenced by", note: "through Christian Wolff's synthesis, taught at the Albertina", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  - {value: "Jean-Jacques Rousseau", roster_id: rousseau-jean-jacques, relation: "influenced by", note: "deep influence on his moral philosophy in the mid-1760s", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  - {value: "David Hume", roster_id: hume-david, relation: "influenced by", note: "British sentimentalist ideas in his 1760s reflections", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP §1; the better-known influence on causation was not checked in a source read (flag)."}

review:
  roster_status_reason: {value: "Core in v8 (F 5: all five models).", certainty: 0.7, cites: [{source: S7, locator: "roster.csv, rank 41"}], how_known: "Study roster."}
  controversies:
    - {value: "Royal rescript of October 1794 reprimanding his writings on Christianity; he agreed to refrain from public writing on religion", certainty: 1.0, cites: [{source: S2, locator: "§3.6"}, {source: S1, locator: "§1"}], how_known: "Two SEP entries."}
  data_quality_flags:
    - "Living Forces: started 1744, dated 1746 (Britannica) vs 1747 (SEP)."
    - "Collegium Fridericianum: ages 8–15 (SEP) vs eight and a half years (Britannica)."
    - "Region by modern country puts Königsberg (now Kaliningrad) in Eastern Europe."
    - "Britannica read as its first page only."
  open_questions:
    - "Fill the KANT system file; then recode primary_system (founders rule)."
    - "Decide how far the 'symbol only' reading of his God (S2 §3.3.1.2) should move A."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Michael Rohlf"
    year: 2024
    citation: "Rohlf, Michael. \"Immanuel Kant.\" Stanford Encyclopedia of Philosophy (substantive revision 31 Jul 2024). https://plato.stanford.edu/entries/kant/."
    url: "https://plato.stanford.edu/entries/kant/"
    accessed: 2026-10-02
    reliability_note: "Scholarly reference work; §1, §2.2, §5–6 read. Cited by section."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators, review]
  - id: S2
    type: secondary
    kind: encyclopedia
    author: "Lawrence Pasternack and Courtney Fugate"
    year: 2025
    citation: "Pasternack, Lawrence, and Courtney Fugate. \"Kant's Philosophy of Religion.\" Stanford Encyclopedia of Philosophy (substantive revision 13 Oct 2025). https://plato.stanford.edu/entries/kant-religion/."
    url: "https://plato.stanford.edu/entries/kant-religion/"
    accessed: 2026-10-02
    reliability_note: "Scholarly reference work; §1, §2.1.1, §3.2, §3.3.1 (with §3.3.1.2, 'Only as a mere symbol'), §3.5.1, §3.6 read (revision of 13 Oct 2025; the §3.3.1.2 heading was rechecked in the live entry on 2026-10-02). Cited by section."
    used_for: [contribution, worldview, review]
  - id: S3
    type: tertiary
    kind: encyclopedia
    author: "Otto Allen Bird and Brian Duignan"
    citation: "Bird, Otto Allen, and Brian Duignan. \"Immanuel Kant.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Immanuel-Kant."
    url: "https://www.britannica.com/biography/Immanuel-Kant"
    accessed: 2026-10-02
    reliability_note: "Signed article; first page only. Cited by section heading."
    used_for: [identity, basics, contribution, childhood, heritage, institutions, collaborators]
  - id: S4
    type: primary
    kind: "scholarly edition"
    author: "Immanuel Kant"
    year: 1787
    citation: "Kant, Immanuel. Kritik der reinen Vernunft, 2. Auflage 1787. In Kant's gesammelte Schriften, ed. Königlich Preußische Akademie der Wissenschaften, vol. III. Electronic edition: Bonner Kant-Korpus, https://korpora.org/kant/aa03/."
    url: "https://korpora.org/kant/aa03/"
    accessed: 2026-10-02
    reliability_note: "Akademie-Ausgabe text of the second edition (1787), cited by AA volume and page (pages 19 and 166 read)."
    used_for: [worldview]
  - id: S5
    type: primary
    kind: "scholarly edition"
    author: "Immanuel Kant"
    year: 1788
    citation: "Kant, Immanuel. Kritik der praktischen Vernunft (1788). Akademie-Ausgabe vol. V. Electronic edition: Bonner Kant-Korpus, https://korpora.org/kant/aa05/."
    url: "https://korpora.org/kant/aa05/"
    accessed: 2026-10-02
    reliability_note: "Akademie-Ausgabe text, cited by AA page (124–125 read)."
    used_for: [worldview, lane_b]
  - id: S6
    type: primary
    kind: "scholarly edition"
    author: "Immanuel Kant"
    year: 1793
    citation: "Kant, Immanuel. Die Religion innerhalb der Grenzen der bloßen Vernunft (1793). Akademie-Ausgabe vol. VI. Electronic edition: Bonner Kant-Korpus, https://korpora.org/kant/aa06/."
    url: "https://korpora.org/kant/aa06/"
    accessed: 2026-10-02
    reliability_note: "Akademie-Ausgabe text, cited by AA page (84–89, 153–155, 194–196 read)."
    used_for: [worldview, timing]
  - id: S7
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# Immanuel Kant

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Immanuel Kant (1724–1804), German philosopher of Königsberg, founded the critical philosophy [S1; S3]. He limited knowledge to appearances to make room for faith [S4, AA III 19], postulated a God distinct from nature on moral grounds [S5, AA V 125], and excluded miracles and petition from the maxims of reason [S6, AA VI 87–88, 194]. primary_system BELOW_THRESHOLD (KANT is a stub). Axes A 1, B 4, C 1, D 4, E 4, all at 0.7; mid_basin true at 0.7 (draft).

## Life and work

Pietist schooling, the Albertina from 1740, private tutor, then lecturer (1755–1770) and professor at Königsberg until 1796 [S1, §1; S3].

## Contribution and impact

Transcendental idealism, the categorical imperative and the nebular hypothesis [S1].

## Childhood and education

Artisan Pietist family; Collegium Fridericianum from age eight; Newton through Knutzen [S1, §1; S3].

## Adult working worldview

God and immortality are postulates of pure practical reason [S5]. All changes follow the law of cause and effect [S4, AA III 166]. Religion is the recognition of duties as divine commands [S6, AA VI 153].

## Heritage (context only)

Lutheran Pietist artisan family [S1; S3]. Context only.

## Timing

First lasting contribution taken as the Universal Natural History of 1755 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Circle absent [S5].

## Open questions

- Fill KANT; settle the founders-rule conflict.

## Research log

- 2026-10-02: Read SEP "Immanuel Kant" (Rohlf), SEP "Kant's Philosophy of Religion" (Pasternack), Britannica (Bird, first page), and the Bonner Kant-Korpus pages AA III 19, 166; V 124–125; VI 84–89, 153–155, 194–196. Wikipedia not used.
- 2026-10-02 (lens audit fixes): Re-fetched the live SEP "Kant's Philosophy of Religion" (rev. 13 Oct 2025) to check §3.3.1.2, and re-read Britannica "Background and early years" and Religion AA VI 88 n. and VI 155.
