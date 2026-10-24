---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch U)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #116 / F4 rank 117). Goals: find own texts on God/nature if any; keep honest BELOW/UNKNOWN; prefer interviews/essays in or near span. Read Caruso 1967 Qui êtes-vous / Conversation (Dits et écrits I §50/61; S5): species 'ne fonctionnaient pas … ni pour Dieu'; idea of God as functional myth parallel to humanism; 'you believe in the transcendental and I don't' = Kantian transcendental, not God-locus. Qu'est-ce qu'un philosophe? (1966; S6): death of God as Hegel/Feuerbach/Nietzsche diagnosis, not personal denial. Foucault Responds to Sartre (Foucault Live; S7): man as correlative image of god / death of subject not death of god. Dual bio Wikipedia EN (S8, P50) labels him atheist via secondary cites only. P47 on S1–S8. A stays BELOW (no own A1–A4; cultural God-talk and scholar absence-report do not settle locus; P20: absence ≠ ATHE without denial). B UNKNOWN→BELOW (philosopher, P16/P30: anti-teleology and episteme histories checked; no own-voice natural-law / exception claim). mid UNKNOWN→BELOW (A and B both BELOW). primary BELOW unchanged (ATHE lead only). Chart-moving NO. No fallacy_catalog. No figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit fixes for batch U (gs_59bb9fc_U run 1): FO5, The History of Sexuality item now the multivolume work, range 1976–1984 (vols. 2–3 in 1984, SEP); span and working_years 1975–1979 -> 1975–1984; note, SEP revision date (21 April 2026) added to S2. No scored value changes."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch U, order P32: F 4, rank 117). Basics from Britannica (James Faubion, Britannica Editors) and SEP (Gutting and Oksala); Catholic upbringing and the absence of belief from Michael C. Behrent's Commonweal interview (15 October 2026). No text of his own on God or nature read. Not a scientist (P30). primary_system BELOW_THRESHOLD; A BELOW_THRESHOLD; B, C, D, E UNKNOWN; mid_basin UNKNOWN. Span 1975–1979 (0.5). Not plotted. Draft, not reviewed."}

identity:
  id: foucault-michel
  display_name: "Michel Foucault"
  roster:
    canonical_name: "Michel Foucault"
    rank: 117
    F: 4
    models: [Claude, DeepSeek, Gemini, Grok]
    band: "core (3–4)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Paul-Michel Foucault", certainty: 0.7, cites: [{source: S1, locator: "facts box (In full)"}], how_known: "Britannica."}
  native_name: {value: "Paul-Michel Foucault", certainty: 0.7, cites: [{source: S1, locator: "facts box"}], how_known: "French; same as the full name."}
  aliases:
    - {name: "Foucault-Michel", kind: "roster alias"}

basics:
  birth:
    date: {value: "1926-10-15", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "facts box (Born)"}, {source: S2, locator: "§1 Biographical Sketch"}, {source: S8, locator: "Infobox / Early years"}], how_known: "Britannica, SEP and Wikipedia EN agree (P50)."}
    place: {value: "Poitiers", modern_name: "Poitiers, France", polity_then: "France", certainty: 1.0, cites: [{source: S1, locator: "facts box (Born)"}, {source: S2, locator: "§1 Biographical Sketch"}], how_known: "Britannica and SEP."}
  death:
    date: {value: "1984-06-25", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "facts box (Died)"}, {source: S2, locator: "§1 Biographical Sketch"}], how_known: "Britannica and SEP."}
    place: {value: "Paris", modern_name: "Paris, France", polity_then: "France", certainty: 1.0, cites: [{source: S1, locator: "facts box (Died)"}, {source: S2, locator: "§1 Biographical Sketch"}], how_known: "Britannica and SEP; an early victim of AIDS (S2)."}
  first_lasting_contribution_year: {value: 1975, certainty: 0.5, cites: [{source: S2, locator: "§3.4 History of the Prison"}, {source: S3, locator: "answer on where newcomers should start"}], how_known: "Discipline and Punish (1975). Coder's call between this and The Order of Things (1966); see timing.major_work_period."}
  era_bucket: {value: "1950 on", certainty: 0.5, cites: [{source: S2, locator: "§3.4 History of the Prison"}], how_known: "1975 (P2); 1966 under the alternative, same bucket."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "facts box"}, {source: S2, locator: "§1 Biographical Sketch"}], how_known: "France (P3)."}
  region_of_work: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "'Education and career'"}, {source: S2, locator: "§1 Biographical Sketch"}], how_known: "France, chiefly Paris (Collège de France)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "'Education and career'"}], how_known: "'The son and grandson of a physician'."}
  languages_of_work: {value: ["French"], certainty: 0.7, cites: [{source: S1, locator: "'Education and career'"}], how_known: "Coder's reading."}
  occupations: {value: ["philosopher and historian", "professor of the history of systems of thought, Collège de France", "cultural attaché (Uppsala, Warsaw, Hamburg)"], certainty: 0.7, cites: [{source: S1, locator: "'Education and career'"}, {source: S2, locator: "§1 Biographical Sketch"}], how_known: "Britannica and SEP."}

contribution:
  fields: {value: ["philosophy", "history of systems of thought", "social theory"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "opening; §1"}], how_known: "Britannica and SEP."}
  lasting_original_contributions:
    - {value: "Discipline and Punish (Surveiller et punir): the modern prison and disciplinary power as subject formation", year: 1975, kind: work, lasting: "'The critical impact of Discipline and Punish' (S2); among 'His best-known works' (S1, question box); 'The orthodox answer' for where to start (S3)", certainty: 0.7, cites: [{source: S1, locator: "'Education and career'"}, {source: S2, locator: "§3.4 History of the Prison"}, {source: S3, locator: "answer on where newcomers should start"}], how_known: "SEP and Behrent. Not a theory about natural systems, so not a scientist (P30)."}
    - {value: "The History of Sexuality (vol. 1, 1976: power as productive and diffuse, 'microphysics of power'; vols. 2–3, The Use of Pleasure and The Care of the Self, 1984: the ethical self in antiquity)", year: 1976, kind: work, lasting: "'one of the most influential contemporary understandings of power' (S2); 'The History of Sexuality, a multivolume history' among 'His best-known works' and 'canonical for gay and lesbian studies and queer theory' (S1, question box)", certainty: 0.7, cites: [{source: S2, locator: "§3.5 History of Modern Sexuality"}, {source: S3, locator: "answer on the fourth volume"}, {source: S1, locator: "question box (best-known works)"}], how_known: "SEP; date of vol. 1 from Behrent ('published the first volume in 1976'); vols. 2–3 from SEP ('his last two books (1984) ... The Use of Pleasure and The Care of the Self'). Range 1976–1984: start 1976 (P12), end 1984 (P30 addendum b, end of range); batch U audit fix FO5."}
    - {value: "Collège de France lectures Security, Territory, Population (1977–78) and The Birth of Biopolitics (1978–79): government and governmentality", year: 1977, kind: "body of work", lasting: "'have been especially influential' (S2)", certainty: 0.5, cites: [{source: S2, locator: "§4 Foucault after Foucault"}], how_known: "SEP. Published posthumously; dated by delivery (P30), range 1977–1979, start year (P12). Inside the span; the end is set by The History of Sexuality (1984)."}
  evidence_of_impact:
    - {value: "'one of the most influential and controversial scholars of the post-World War II period'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "'regularly reported to be the most cited scholar in the social sciences and humanities'", kind: other, certainty: 0.5, cites: [{source: S3, locator: "question on summarizing his thought"}], how_known: "The interviewer's words, not Behrent's; 0.5."}
  major_works:
    - {value: "Folie et déraison (History of Madness)", year: 1961, certainty: 0.7, cites: [{source: S1, locator: "'Education and career'"}], how_known: "Britannica: 'critical praise but a limited audience'."}
    - {value: "Les Mots et les choses (The Order of Things)", year: 1966, certainty: 0.7, cites: [{source: S1, locator: "'Education and career'"}, {source: S3, locator: "answer on The Order of Things"}], how_known: "Britannica ('wide notice'); Behrent: 'basically a forgotten book'."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "'one of the most influential' scholars after 1945 (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Catholic (nominal)", certainty: 0.5, cites: [{source: S3, locator: "first answer"}], how_known: "Behrent: 'nominally Catholic'; parents married in church; the maternal Malapert side had 'a Voltairian streak'. One scholar's account."}
  family_religious_practice: {value: "Maternal grandmother went to Mass almost daily and the boys sometimes went with her; he served as an altar boy at Saint-Porchaire", certainty: 0.5, cites: [{source: S3, locator: "first answer"}], how_known: "Behrent, citing the brother's memory."}
  parents_and_household:
    - {value: "Father: Paul Foucault, surgeon and obstetrician in Poitiers, of a family of doctors", certainty: 0.7, cites: [{source: S1, locator: "'Education and career'"}, {source: S3, locator: "first answer"}], how_known: "Britannica ('son and grandson of a physician') and Behrent."}
    - {value: "Mother: of the Malapert family, pharmacists in Poitiers; died 1987", certainty: 0.5, cites: [{source: S3, locator: "first answer"}], how_known: "Behrent."}
  household_circumstances: {value: "'solidly bourgeois' provincial medical family", certainty: 0.7, cites: [{source: S1, locator: "'Education and career'"}, {source: S3, locator: "first answer"}], how_known: "Britannica and Behrent."}
  schooling:
    - {value: "Collège Saint-Stanislas, Poitiers, run by the Brothers of the Christian Schools (De La Salle); most of his high-school years; taught philosophy by the Benedictine Marcel Pierrot", stage: "grammar or secondary school", run_by: "religious body", years: "to 1943", certainty: 0.5, cites: [{source: S3, locator: "first answer"}], how_known: "Behrent; end year the coder's reading of the 1942–43 baccalaureate year."}
    - {value: "State lycée in Poitiers, before Saint-Stanislas and again to prepare for the ENS entrance exam", stage: "grammar or secondary school", run_by: "state or municipal", certainty: 0.5, cites: [{source: S3, locator: "first answer"}], how_known: "Behrent; years not stated."}
    - {value: "École Normale Supérieure, Paris: psychology and philosophy; graduated 1952", stage: university, run_by: "state or municipal", years: "1946–1952", certainty: 0.7, cites: [{source: S1, locator: "'Education and career'"}], how_known: "Britannica; operator the coder's reading."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Marcel Pierrot, Benedictine monk of Ligugé, his philosophy teacher", certainty: 0.5, cites: [{source: S3, locator: "first answer"}], how_known: "Behrent, from Pierrot's handwritten autobiography."}
  languages_in_childhood: {value: ["French"], certainty: 0.5, cites: [{source: S1, locator: "'Education and career'"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "His expected philosophy teacher, the priest Georges Duret, was arrested by the Gestapo in September 1942", certainty: 0.5, cites: [{source: S3, locator: "first answer"}], how_known: "Behrent."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1975–1984", certainty: 0.5, cites: [{source: S2, locator: "§3.4; §3.5; §4"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Raised nominally Catholic; altar boy; Catholic secondary school", certainty: 0.5, cites: [{source: S3, locator: "first answer"}], how_known: "Behrent. Upbringing only; no code (CHRIST do_not_use_when)."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Interviews read treat religion as historical/political practice and God as cultural myth; no own science–religion formula."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "Deepen D1: own interviews reached (S5–S7) still give no denial or profession. Behrent: nowhere evidence he believed in God (S3); Wikipedia 'Foucault was an atheist' is secondary (S8). Caruso treats the idea of God as a dispensable functional myth parallel to humanism (S5); Qu'est-ce qu'un philosophe? and Foucault Responds to Sartre discuss Nietzsche's death of God as cultural/philosophical diagnosis (S6, S7) — not 'I do not believe in God'. P20: absence of belief ≠ ATHE without his own denial/suspension. Lead toward ATHE only."}
  secondary_system: {value: UNKNOWN, how_known: "One system (P29)."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Lead strengthened: scholar absence-report (S3), Wikipedia secondary label (S8), God-as-myth / death-of-God cultural diagnosis in own interviews (S5–S7); still no own denial (P20)."}
    - {code: AGNOS, reason: "Rejected: no stated suspension read."}
    - {code: CHRIST, reason: "Rejected: upbringing only (S3)."}
  lio_axes:
    A_locus:
      value: BELOW_THRESHOLD
      cites: [{source: S5, locator: "close: idea of God as functional myth; 'you believe in the transcendental and I don't'"}, {source: S6, locator: "death of God as Hegel/Feuerbach/Nietzsche"}, {source: S7, locator: "man as correlative image of god; death of subject not death of god"}, {source: S3, locator: "first answer"}]
      how_known: "Primary interviews reached this pass. Caruso (S5): living species do not function for God; the idea of God was a myth that let humanity think it needed a justification for control — cultural diagnosis, not a personal locus. 'You believe in the transcendental and I don't' is Kantian/philosophical transcendental vs historicist method, not denial of a personal God. S6/S7: death of God as others' thesis. Behrent absence-report (S3) and Wikipedia 'atheist' (S8) are secondary. No A1–A4 in his own voice. Evidence bears weakly (God-talk as myth) but under 0.5 for a locus score → BELOW (P19, P20)."
    B_cause:
      value: BELOW_THRESHOLD
      cites: [{source: S5, locator: "species function without telos toward God/man"}, {source: S7, locator: "Foucault Live scanned for natural-law / miracle / exception claims"}]
      how_known: "Not a scientist (P30). Philosopher: B only from own-voice nature / physical-world claims (P16). Caruso anti-teleology of living species (they function, not for God or man) checked — purpose, not law-vs-exception. Foucault Live / Order of Things materials describe historical epistemes of natural history, not his claim that nature is lawful with or without exemptions. Looked and insufficient → BELOW (P19)."
    C_ledger: {value: UNKNOWN, how_known: "Nothing on reward and punishment of persons in his own view (P19); his histories of Christian confession and 'salvation' (S2 §3.5, S3) describe others' views. In-span 'political spirituality' and Hermeneutics of the Subject 'spirituality' are practices of self-transformation, not a ledger of deserts."}
    D_authority: {value: UNKNOWN, how_known: "Nothing on revelation against observation read (P19). Rejection of 'the transcendental' (S5) is methodological (Kantian condition of possibility), not a scored D stance on revelation vs observation."}
    E_scope: {value: UNKNOWN, how_known: "Nothing on favour for a group in the world's order read (P7, P19)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus and B_cause are both BELOW_THRESHOLD (P19; Kafka / Heidegger pattern)."}
  statements:
    - text: "Il faut se résigner à prendre, face à l'humanité, une position analogue à celle qu'on a prise, vers la fin du XVIIIe siècle, au regard des autres espèces vivantes, lorsque l'on s'est aperçu qu'elles ne fonctionnaient pas pour quelqu'un — ni pour elles-mêmes, ni pour l'homme, ni pour Dieu —, mais qu'elles fonctionnaient, c'est tout. [...] L'espèce ne fonctionne pas pour elle-même, ni pour l'homme, ni pour la plus grande gloire de Dieu ; elle se limite à fonctionner."
      cites: [{source: S5, locator: "Caruso conversation, near close (Dits et écrits I §61)"}]
      date: "1967"
      context: "Interview with P. Caruso; anti-teleology of living species; later compares the idea of man to the idea of God as functional myths."
      axes: [A_locus, B_cause]
      kind: other
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "French transcription at 1libertaire; English parallel in Foucault Live ('you believe in the transcendental and I don't' is a separate exchange in the same interview family — Kantian transcendental, not God)."
    - text: "For Hegel, Reason takes the place of God; [...] for Feuerbach, God was the illusion that alienated Man; [...] for Nietzsche finally, the death of God means the end of metaphysics, but the place remains empty, and it is absolutely not Man who takes the place of God."
      cites: [{source: S6, locator: "reply on death of God"}]
      date: "1966"
      context: "'Qu'est-ce qu'un philosophe?', Connaissance des hommes no. 22; diagnosis of others' theses."
      axes: [A_locus]
      kind: other
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Not a personal profession or denial."
    - text: "Man of the 19th century is god incarnated in humanity. [...] Nietzsche was the one who by denouncing the death of god at the same time denounced this divinized man that the 19th century never ceased to dream. [...] The death of man is nothing to get particularly excited about. [...] I don't mean by it the death of god but the death of the subject."
      cites: [{source: S7, locator: "'Foucault Responds to Sartre'"}]
      date: "1968"
      context: "Interview collected in Foucault Live; cultural diagnosis of humanism after Nietzsche."
      axes: [A_locus]
      kind: other
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Death of God / man as philosophical diagnosis, not personal creed."
  changes_over_life:
    - {value: "Catholic upbringing and schooling; 'embraced and then abandoned communism' at the ENS", certainty: 0.5, cites: [{source: S1, locator: "'Education and career'"}, {source: S3, locator: "first answer"}], how_known: "Britannica (communism) and Behrent (upbringing); before the span."}
  coder_notes: "Deepen D1 2026-10-24: Caruso 1967, Qu'est-ce qu'un philosophe 1966, and Foucault Responds to Sartre read for A/B. No own denial → primary and A stay BELOW (P20). B UNKNOWN→BELOW after P16 check (anti-teleology ≠ law/exception). mid BELOW. Span call unchanged (1975–1984; alt 1966). In-span political spirituality / Hermeneutics 'spirituality' are practice-of-self terms, not God-belief. Lille 1952–53 course still unread in full (Behrent paraphrase only). Not plotted."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "French provincial bourgeoisie", certainty: 0.5, cites: [{source: S1, locator: "'Education and career'"}], how_known: "Coder's reading of 'solidly bourgeois'."}
  religious_heritage_by_birth: {value: "Catholic", certainty: 0.5, cites: [{source: S3, locator: "first answer"}], how_known: "Behrent."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1975–1984", certainty: 0.5, cites: [{source: S2, locator: "§3.4; §3.5; §4"}, {source: S3, locator: "answer on where newcomers should start"}], how_known: "From Discipline and Punish (1975) to the last volumes of The History of Sexuality (1984) (P12, P30 addendum b; batch U audit fix FO5). Coder's call on the start; alternative 1966 (coder_notes)."}
  age_at_first_lasting_contribution: {value: 49, certainty: 0.5, cites: [{source: S1, locator: "facts box"}, {source: S2, locator: "§3.4"}], how_known: "1975 − 1926 = 49 (P30); 40 under the 1966 alternative."}
  first_evidence_of_lio_type_views: {value: "Qu'est-ce qu'un philosophe? / Caruso (death of God; God as myth)", year: 1966, certainty: 0.5, cites: [{source: S6, locator: "death of God reply"}, {source: S5, locator: "Caruso close"}], how_known: "Earliest own-voice God-talk read this pass is 1966–67 interviews; still below threshold for a scored A/B value."}
  lio_views_relative_to_major_work: {value: "before major work", certainty: 0.5, cites: [{source: S5, locator: "1967"}, {source: S6, locator: "1966"}], how_known: "God-as-myth / death-of-God interviews precede the 1975–1984 span; no change of view documented for the span. Still BELOW for scoring."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "§3"}], how_known: "Not assessed."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "§3"}], how_known: "Not assessed."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S2, locator: "§3"}], how_known: "Coder's reading."}
  reading: "Power and knowledge as inseparable; the subject formed by practices."
  notes: ""

institutions:
  - {value: "University of Lille", role: "teacher", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Education and career'"}], how_known: "Britannica; years not stated (after 1952)."}
  - {value: "French cultural service (Uppsala, Warsaw, Hamburg)", role: "cultural attaché", years: "1955–1960", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "'Education and career'"}], how_known: "Britannica."}
  - {value: "University of Clermont-Ferrand", role: "teacher", years: "1960–1966", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Education and career'"}], how_known: "Britannica."}
  - {value: "University of Tunis", role: "teacher", years: "1966–1968", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Education and career'"}], how_known: "Britannica."}
  - {value: "Collège de France", role: "professor of the history of systems of thought", years: "1970–1984", kind: "research institute", certainty: 0.5, cites: [{source: S1, locator: "'Education and career'"}, {source: S2, locator: "§1 Biographical Sketch"}], how_known: "Britannica says awarded the chair in 1970; SEP says elected in 1969. 0.5."}
collaborators:
  - {value: "Marcel Pierrot", relation: teacher, note: "Benedictine monk; school philosophy teacher (1942–43)", certainty: 0.5, cites: [{source: S3, locator: "first answer"}], how_known: "Behrent."}
  - {value: "Friedrich Nietzsche", relation: "influenced by", note: "'his greatest philosophical influence' (S3)", certainty: 0.5, cites: [{source: S3, locator: "first answer"}], how_known: "Behrent."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 117"}], how_known: "Study roster."}
  controversies:
    - {value: "Vilified by the right as deviant and subversive in his lifetime; some on the left later rejected his approach", certainty: 0.5, cites: [{source: S3, locator: "standfirst"}], how_known: "Commonweal's introduction."}
  data_quality_flags:
    - "A/B still BELOW after primary interviews: cultural God-talk and anti-teleology do not settle locus or P16 law/exception."
    - "Span start is a coder's call with a named alternative (1966)."
    - "Wikipedia 'Foucault was an atheist' is secondary; not used as own denial."
  open_questions:
    - "Full Dits et écrits vols. for any 'je ne crois pas en Dieu' or equivalent (searches of Foucault Live and major interviews found none)."
    - "1952–53 Lille course 'Knowledge of Man and Transcendental Reflection' (2022) in full — Behrent paraphrase only so far."
    - "Hand-check Order of Things / Birth of Biopolitics for any overlooked P16 nature-order profession (unlikely)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "James Faubion; Britannica Editors"
    citation: "Faubion, James, and Britannica Editors. \"Michel Foucault.\" Encyclopaedia Britannica (updated 11 October 2026). https://www.britannica.com/biography/Michel-Foucault. Read live 2026-10-19."
    url: "https://www.britannica.com/biography/Michel-Foucault"
    accessed: 2026-10-19
    reliability_note: "Signed article; facts box and 'Education and career' cited; question boxes cited only where marked."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Gary Gutting and Johanna Oksala"
    citation: "Gutting, Gary, and Johanna Oksala. \"Michel Foucault.\" Stanford Encyclopedia of Philosophy (first published 2 April 2003; substantive revision 21 April 2026). https://plato.stanford.edu/entries/foucault/"
    url: "https://plato.stanford.edu/entries/foucault/"
    accessed: 2026-10-19
    reliability_note: "Signed scholarly encyclopedia; §1, §3.4, §3.5 and §4 used."
    source_quality: "reference entry"
    used_for: [basics, contribution, worldview, timing, institutions]
  - id: S3
    type: secondary
    kind: other
    author: "Michael C. Behrent, interviewed by Daniel Steinmetz-Jenkins"
    citation: "Steinmetz-Jenkins, Daniel. \"Foucault at a Hundred: An interview with Michael C. Behrent.\" Commonweal, 15 October 2026. https://www.commonwealmagazine.org/steinmetz-jenkins-foucault-interview-Behrent"
    url: "https://www.commonwealmagazine.org/steinmetz-jenkins-foucault-interview-Behrent"
    accessed: 2026-10-19
    reliability_note: "Email interview with the intellectual historian Michael C. Behrent (author of Becoming Foucault: The Poitiers Years). Behrent's answers are a scholar's account; the interviewer's lines are not cited as fact. Locators by answer."
    source_quality: "scholarly edition or monograph"
    used_for: [childhood, heritage, worldview, contribution, timing, collaborators, review]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S5
    type: primary
    kind: other
    author: "Michel Foucault; interviewer P. Caruso"
    citation: "Foucault, Michel. \"Qui êtes-vous, professeur Foucault?\" / \"Conversation avec Michel Foucault\" (entretien avec P. Caruso). La Fiera letteraria, 28 Sept. 1967; fuller text in Caruso, Conversazioni con Claude Lévi-Strauss, Michel Foucault, Jacques Lacan (Milan: Mursia, 1969). Dits et écrits I, textes n° 50 and 61. French web transcription read 2026-10-24; English parallels in Foucault Live (S7)."
    url: "http://1libertaire.free.fr/MFoucault176.html"
    accessed: 2026-10-24
    reliability_note: "Own recorded interview; web transcription of the Dits et écrits text. Locators by topic near the close (species/God myth; transcendental exchange)."
    source_quality: "primary / own words"
    used_for: [worldview, review]
  - id: S6
    type: primary
    kind: other
    author: "Michel Foucault; interviewer M.-G. Foy"
    citation: "Foucault, Michel. \"Qu'est-ce qu'un philosophe?\" (entretien avec M.-G. Foy). Connaissance des hommes, no. 22 (automne 1966): 9. Dits et écrits I, texte n° 42. Web transcription read 2026-10-24."
    url: "http://1libertaire.free.fr/MFoucault128.html"
    accessed: 2026-10-24
    reliability_note: "Own recorded interview; short; death-of-God reply diagnoses Hegel/Feuerbach/Nietzsche, not a personal creed."
    source_quality: "primary / own words"
    used_for: [worldview, review]
  - id: S7
    type: primary
    kind: other
    author: "Michel Foucault; edited by Sylvère Lotringer"
    citation: "Foucault, Michel. \"Foucault Responds to Sartre\" and related interviews, in Foucault Live: Collected Interviews, 1961–1984, ed. Sylvère Lotringer, trans. Lysa Hochroth and John Johnston (New York: Semiotext(e), 1996). PDF (Monoskop) searched 2026-10-24 for God / nature / law / miracle / atheism."
    url: "https://monoskop.org/images/8/83/Foucault_Live_Collected_Interviews_1961-1984_1996.pdf"
    accessed: 2026-10-24
    reliability_note: "Collected interviews; English translations. Used for death-of-God/man passages and negative search for P16 nature-law claims and personal atheism formulae."
    source_quality: "primary / own words"
    used_for: [worldview, review]
  - id: S8
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Michel Foucault.\" English Wikipedia. https://en.wikipedia.org/wiki/Michel_Foucault. Read live 2026-10-24."
    url: "https://en.wikipedia.org/wiki/Michel_Foucault"
    accessed: 2026-10-24
    reliability_note: "Crowdsourced; dual bio (P50) against Britannica/SEP. 'Foucault was an atheist' is a secondary label with biography cites — not treated as his own denial."
    source_quality: "reference entry"
    used_for: [identity, basics, childhood, heritage, worldview, review]

---

# Michel Foucault

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Michel Foucault (1926–1984), French philosopher and historian [S1; S8]. Deepen D1: primary_system BELOW_THRESHOLD; A BELOW_THRESHOLD; B BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not plotted (chart-moving NO).

## Life and work

ENS, Lille, Uppsala, Warsaw, Hamburg, Clermont-Ferrand, Tunis, the Collège de France [S1, S2].

## Contribution and impact

Discipline and Punish (1975), The History of Sexuality (1976–1984), the governmentality lectures [S2].

## Childhood and education

A nominally Catholic medical family in Poitiers; Catholic school [S1, S3].

## Adult working worldview

Behrent: no evidence he believed in God [S3]. Own interviews: God as functional myth / death of God as cultural diagnosis [S5–S7]; no personal denial (P20). Anti-teleology of species [S5] is not a P16 law claim. A and B BELOW; mid BELOW.

## Heritage (context only)

Catholic [S3].

## Timing

1975–1984, from age 49 [S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Not assessed.

## Open questions

- Any remaining Dits et écrits item with an explicit personal denial; Lille 1952–53 course in full.

## Research log

- 2026-10-19: Read Britannica, SEP and the Commonweal interview.
- 2026-10-24: Deepen D1. Caruso 1967 (S5), Qu'est-ce qu'un philosophe 1966 (S6), Foucault Live / Responds to Sartre (S7), Wikipedia EN (S8). A stays BELOW; B UNKNOWN→BELOW; mid BELOW. Chart-moving NO.
