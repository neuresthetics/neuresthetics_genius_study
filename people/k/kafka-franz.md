---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch P; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-18
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 20c_early. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-18, by: "Grok Bot", summary: "Record created (stage 3 batch P, order P32: F 4, rank 96). Basics from Britannica (Britannica Editors, unsigned; body only). Worldview from the Zürau aphorisms (notebooks of 1917–18), published by Max Brod and H. J. Schoeps as 'Betrachtungen über Sünde, Leid, Hoffnung und den wahren Weg' in Beim Bau der Chinesischen Mauer (Berlin: Kiepenheuer, 1931), read in the proofread Wikisource transcription. Not a scientist (P30). primary_system BELOW_THRESHOLD; A BELOW_THRESHOLD (alt 3); B BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-18, by: "Grok Bot", summary: "Batch P audit fixes (gs_08be43b_P run 1: 39 hold, 6 weaken). Page cites corrected from each Wikisource page's own source: no. 50 on p. 234 (KA4), no. 54 on p. 235 (KA5), and the aphorism printed as '70. 71' on pp. 238–239 (KA6, also in the A_locus cites). Ruling P3 (v8's pick on the auditor's advice): A and B stay BELOW_THRESHOLD. Values unchanged; not plotted."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #95, F4 rank 96). Needs: A BELOW alt 3 (Zürau figurative, P3); B BELOW; primary BELOW; mid BELOW; not plotted; not a scientist (P30). Dual bio: Britannica (S1) + Wikipedia EN (S4) (P50). P47 source_quality on S1–S7. Sought Brod diaries/letters on IA (diaries191019230000kafk and peers): OCR download 401 access-restricted — full Brod Diaries not opened. Blue Octavo / Kafka Project quote 'Believing means liberating the indestructible element in oneself…' (S5) is same Zürau-period material and still does not equate God with the indestructible. Wikisource Brief an den Vater (1919, S6): inherited Judaism as 'Nichts' / temple formality — heritage and practice critique, not a place/deny of God (P42/P3). Brod-reported 1920 conversation 'hope enough… only not for us' (Wikiquote via Brod biography, S7) is third-party reported speech — lead only, not Lane A. Aphorisms 69 and 74 re-read (S2): believe in the indestructible in oneself / paradise destructibility — still no God=indestructible equate. A stays BELOW_THRESHOLD alt 3 (P3 reopen condition not met). B stays BELOW (P16: spiritual-world aphorism ≠ lawful nature). primary BELOW; mid BELOW. Chart-moving NO (still not plotted). No fallacy_catalog. Draft, not reviewed."}

identity:
  id: kafka-franz
  display_name: "Franz Kafka"
  roster:
    canonical_name: "Franz Kafka"
    rank: 96
    F: 4
    models: [Claude, Gemini, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: literature
    field_bucket: literature
  full_name: {value: "Franz Kafka", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lead"}], how_known: "Britannica and Wikipedia agree (P15)."}
  native_name: {value: "Franz Kafka", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lead"}], how_known: "German; same spelling."}
  aliases:
    - {name: "Franz-Kafka", kind: "roster alias"}
    - {name: "Kafka-Franz", kind: "roster alias"}

basics:
  birth:
    date: {value: "1883-07-03", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "infobox / lead"}], how_known: "Britannica and Wikipedia agree."}
    place: {value: "Prague, Bohemia, Austria-Hungary", modern_name: "Prague, Czechia", polity_then: "Austria-Hungary", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "infobox / Early life"}], how_known: "Britannica and Wikipedia agree."}
  death:
    date: {value: "1924-06-03", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "infobox / Death"}], how_known: "Britannica and Wikipedia agree."}
    place: {value: "Kierling, near Vienna, Austria", modern_name: "Kierling (Klosterneuburg), Austria", polity_then: "Austria", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "Death (Hoffmann sanatorium, Kierling)"}], how_known: "Britannica Kierling; Wikipedia names Klosterneuburg / Hoffmann sanatorium — same place."}
  first_lasting_contribution_year: {value: 1913, certainty: 0.7, cites: [{source: S1, locator: "father paragraph"}, {source: S4, locator: "Stories (Das Urteil 1912 night / published 1912–13)"}], how_known: "Das Urteil (1913; The Judgment), the earliest dated lasting work S1 names (P13, P17); Wikipedia dates the breakthrough night 22 Sept 1912."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "From 1913 (P2); every listed year gives the same bucket."}
  region_of_birth: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Czechia (P3)."}
  region_of_work: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "double life paragraph"}, {source: S4, locator: "Employment / Personal life"}], how_known: "Prague; Berlin only in 1923–24."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [German], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lead"}], how_known: "'a German-language writer' (S1)."}
  occupations: {value: ["writer", "insurance official", "lawyer by training"], certainty: 0.7, cites: [{source: S1, locator: "double life paragraph"}, {source: S4, locator: "Employment"}], how_known: "Britannica and Wikipedia."}

contribution:
  era_bucket: 20c_early
  fields: {value: ["fiction"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lead"}], how_known: "Britannica and Wikipedia."}
  lasting_original_contributions:
    - {value: "Das Urteil (The Judgment)", year: 1913, kind: work, lasting: "'reflected directly' the father conflict central to his work (S1)", certainty: 0.5, cites: [{source: S1, locator: "father paragraph"}, {source: S4, locator: "Stories"}], how_known: "Britannica; lasting status is the coder's reading."}
    - {value: "Die Verwandlung (The Metamorphosis)", year: 1915, kind: work, lasting: "named in the opening as one of the works that 'express the anxieties and alienation felt by many in 20th-century Europe and North America' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lead / Stories"}], how_known: "Britannica and Wikipedia."}
    - {value: "Der Prozess (The Trial)", year: 1925, kind: work, lasting: "named in the opening with The Metamorphosis (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "Novels"}], how_known: "Britannica; published after his death (1924)."}
    - {value: "Das Schloss (The Castle)", year: 1926, kind: work, lasting: "one of the novels that portray 'a man's desperate struggle with an overwhelming power' (S1)", certainty: 0.5, cites: [{source: S1, locator: "father paragraph"}, {source: S4, locator: "Novels"}], how_known: "Britannica; posthumous; lasting status the coder's reading."}
  evidence_of_impact:
    - {value: "Works 'express the anxieties and alienation felt by many in 20th-century Europe and North America'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Betrachtungen über Sünde, Leid, Hoffnung und den wahren Weg (Zürau Aphorisms)", year: 1931, kind: "book", certainty: 0.7, cites: [{source: S2, locator: "headnote (1931 Kiepenheuer)"}, {source: S4, locator: "Personal life (Zürau notebooks)"}], how_known: "Posthumous 1931 publication of 1917–18 notebooks; worldview source."}
    - {value: "Brief an den Vater (Letter to His Father)", year: 1919, kind: "other", certainty: 0.7, cites: [{source: S6, locator: "headnote (composed 1919)"}, {source: S4, locator: "Early life / Personal life"}], how_known: "Long unsent letter; heritage / father conflict."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Jewish; his father 'held only perfunctorily to the religious practices and social formalities of the Jewish community'", certainty: 0.7, cites: [{source: S1, locator: "father paragraph"}, {source: S6, locator: "Judentum section (temple four days a year; 'Nichts')"}], how_known: "Britannica; confirmed in Brief an den Vater's account of inherited practice."}
  family_religious_practice: {value: "Perfunctory temple attendance (father ~four high holidays); Seder at home; Kafka later called the inherited material a 'Nichts'", certainty: 0.7, cites: [{source: S1, locator: "father paragraph"}, {source: S6, locator: "Judentum section"}, {source: S4, locator: "Early life (synagogue on four high holidays)"}], how_known: "Britannica, Wikipedia, and Brief an den Vater."}
  parents_and_household:
    - {value: "Hermann Kafka, merchant", role: father, certainty: 0.7, cites: [{source: S1, locator: "Life paragraph"}, {source: S4, locator: "Early life"}], how_known: "Britannica and Wikipedia."}
    - {value: "Julie Löwy", role: mother, certainty: 0.7, cites: [{source: S1, locator: "Life paragraph"}, {source: S4, locator: "Early life"}], how_known: "Britannica and Wikipedia."}
  household_circumstances: {value: "Prosperous middle-class Jewish family; eldest surviving child", certainty: 0.7, cites: [{source: S1, locator: "Life paragraph"}, {source: S4, locator: "Early life"}], how_known: "Britannica and Wikipedia."}
  schooling:
    - {value: "Altstädter Deutsches Gymnasium (Altstädter Staatsgymnasium), Prague", stage: "grammar or secondary school", years: "1893–1901", certainty: 0.7, cites: [{source: S1, locator: "father paragraph"}, {source: S4, locator: "Education"}], how_known: "Britannica; Wikipedia dates 1893–Matura 1901."}
    - {value: "Deutsche Karl-Ferdinands-Universität, Prague (doctorate in law, 1906)", stage: university, years: "1901–1906", certainty: 0.7, cites: [{source: S1, locator: "double life paragraph"}, {source: S4, locator: "Education / Employment"}], how_known: "Britannica and Wikipedia."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [German], certainty: 0.7, cites: [{source: S1, locator: "father paragraph"}, {source: S4, locator: "Early life (Standard German)"}], how_known: "'German in both language and culture' (S1); also Czech at gymnasium (S4)."}
  notable_events:
    - {value: "As an adolescent declared himself a socialist and an atheist", year: UNKNOWN, certainty: 0.7, cites: [{source: S1, locator: "father paragraph"}, {source: S4, locator: "Judaism and Zionism ('As a teenager, Kafka declared himself an atheist')"}], how_known: "Britannica and Wikipedia. Adolescent evidence, off-point for the working years (P29); does not score adult A alone."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1913–1924", certainty: 0.7, cites: [{source: S1, locator: "opening; father paragraph"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "The aphorisms read are private and figurative: belief in a personal God is 'one of the possible expressions' of a hidden trust in 'something indestructible' in oneself (no. 50), and 'There is nothing but a spiritual world' (no. 54). They fit no code clearly; candidates JUDA (heritage and later sympathy for Zionism, S1/S4), EXIST (lead only). Britannica's paraphrase of his isolation 'with God, or, as he put it, with true indestructible Being' remains a lead, not his wording. Deepen D1: no diary/letter own-voice equate of God with the indestructible found (IA Brod Diaries blocked; Blue Octavo 'Believing…' and Brief an den Vater do not supply it)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: JUDA, reason: "Heritage; Brief an den Vater on inherited 'Nichts' of practice; 'marked interest and sympathy for a socialized Zionism' (S1); Wikipedia Zionism/Hebrew study — political and cultural, not a clear doctrinal primary_system."}
    - {code: EXIST, reason: "Lead only; Brod-reported hope conversation (S7) and absurdist readings are third-party / critical, not a self-label."}
    - {code: ATHE, reason: "Adolescent atheism (S1/S4) is before the working years (P29); adult figurative aphorisms do not deny God outright."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, cites: [{source: S2, locator: "no. 50 (p. 234); no. 69; no. 70. 71 (pp. 238–239); no. 74"}, {source: S5, locator: "'Believing means liberating…' (Blue Octavo)"}, {source: S6, locator: "Judentum section"}], how_known: "Private aphorism, figurative: 'Der Mensch kann nicht leben ohne ein dauerndes Vertrauen zu etwas Unzerstörbarem in sich ... Eine der Ausdrucksmöglichkeiten dieses Verborgenbleibens ist der Glaube an einen persönlichen Gott' (no. 50), and 'Das Unzerstörbare ist eines; jeder einzelne Mensch ist es und gleichzeitig ist es allen gemeinsam' (no. '70. 71'). That places what is ultimate within persons and treats a personal God as one expression of it, which leans to A 3, but no view on God's existence or locus is stated outright. Named alternative: 3. Ruling P3: stays BELOW_THRESHOLD — no. 50 describes what belief in a personal God expresses without asserting or denying God, and no. '70. 71' never identifies the indestructible with God. Deepen D1 reopen check: Blue Octavo 'Believing means liberating the indestructible element in oneself…' (S5) is faith/being language without God=indestructible; Brief an den Vater (S6) criticizes inherited Jewish practice as 'Nichts' without placing or denying God; Brod Diaries IA-blocked. Reopen condition (own-voice equate) not met. Translation the coder's."}
    B_cause: {value: BELOW_THRESHOLD, cites: [{source: S2, locator: "no. 54"}], how_known: "Not a scientist (P30). The one remark on nature read, 'Es gibt nichts anderes als eine geistige Welt; was wir sinnliche Welt nennen, ist das Böse in der geistigen' (no. 54), is about the status of the sensible world, not its law or exceptions, so it bears on B only indirectly (P16, P19). Deepen D1: no nature-order / immutable-law statement found in accessible letters or aphorisms."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing scored; no. 40 ('Nur unser Zeitbegriff läßt uns das Jüngste Gericht so nennen, eigentlich ist es ein Standrecht', S2) remains a figurative lead."}
    D_authority: {value: UNKNOWN, how_known: "Brief an den Vater rejects father's 'Nichts' of Jewish practice as binding example, but that is family/heritage authority, not a clear D score on religion's say over nature or conscience (left unscored)."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A and B are both BELOW_THRESHOLD (P19)."}
  statements:
    - text: "Der Mensch kann nicht leben ohne ein dauerndes Vertrauen zu etwas Unzerstörbarem in sich, wobei sowohl das Unzerstörbare als auch das Vertrauen ihm dauernd verborgen bleiben können. Eine der Ausdrucksmöglichkeiten dieses Verborgenbleibens ist der Glaube an einen persönlichen Gott."
      cites: [{source: S2, locator: "no. 50 (p. 234)"}]
      context: "Zürau notebooks, 1917–18 (inside the working years); published posthumously in 1931 (S2). Undated within that span, so no single year is given."
      axes: [A_locus]
      kind: "notebook or diary"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Wikisource transcription of the 1931 edition, proofread twice against page scans; web copy, cap 0.7. Page from the Wikisource page markers. Re-read deepen D1."
    - text: "Es gibt nichts anderes als eine geistige Welt; was wir sinnliche Welt nennen, ist das Böse in der geistigen, und was wir böse nennen, ist nur eine Notwendigkeit eines Augenblicks unserer ewigen Entwicklung."
      cites: [{source: S2, locator: "no. 54 (p. 235)"}]
      context: "Same notebooks."
      axes: [B_cause]
      kind: "notebook or diary"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "As above. Spiritual-world claim ≠ nature-order (P16)."
    - text: "Das Unzerstörbare ist eines; jeder einzelne Mensch ist es und gleichzeitig ist es allen gemeinsam, daher die beispiellos untrennbare Verbindung der Menschen."
      cites: [{source: S2, locator: "no. 70. 71 (pp. 238–239)"}]
      context: "Same notebooks."
      axes: [A_locus]
      kind: "notebook or diary"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "As above. Does not name God."
    - text: "Theoretisch gibt es eine vollkommene Glücksmöglichkeit: An das Unzerstörbare in sich glauben und nicht zu ihm streben."
      cites: [{source: S2, locator: "no. 69"}]
      context: "Same Zürau notebooks; adjacent to nos. 50 and 70.71 on the indestructible."
      axes: [A_locus]
      kind: "notebook or diary"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Believe in the indestructible in oneself — still no equate with God."
    - text: "Believing means liberating the indestructible element in oneself, or, more accurately, being indestructible, or, more accurately, being."
      cites: [{source: S5, locator: "Blue Octavo Notebooks (Kafka Project / LibQuotes attribution)"}]
      context: "Blue Octavo Notebooks (Zürau-period Oktavhefte), English translation; Kafka Project archive labels it 'Diaries' but standard attribution is Blue Octavo (1954)."
      axes: [A_locus]
      kind: "notebook or diary"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Deepen D1 reopen candidate: still faith/being language without identifying the indestructible as God. German primary page not opened this pass."
    - text: "Was habe ich mit Juden gemeinsam? Ich habe kaum etwas mit mir gemeinsam und sollte mich ganz still, zufrieden damit daß ich atmen kann, in einen Winkel stellen."
      cites: [{source: S4, locator: "Judaism and Zionism (diary 8 Jan 1914)"}, {source: S6, locator: "Judentum section (inherited practice as 'Nichts')"}]
      date: "1914-01-08"
      context: "Diary entry on commonality with Jews (Wikipedia quotes German); Brief an den Vater (1919) expands on inherited temple formality as 'Nichts' / 'Spass' — heritage distance, not a creed denial of God."
      axes: [A_locus]
      kind: "notebook or diary"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Used as heritage context; does not place or deny God. Full Brod Diaries IA-blocked."
    - text: "Oh, hope enough, infinite hope — only not for us."
      cites: [{source: S7, locator: "Brod-reported 1920 conversation (Wikiquote)"}]
      context: "Reported by Max Brod (biography); often cited as Kafka on hope and God. Third-party reported speech."
      axes: [A_locus]
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Lead only (P42). Not used to score A or primary_system."
  changes_over_life:
    - {value: "Adolescent atheism / socialism (Britannica, Wikipedia) → adult Zürau figurative metaphysics (1917–18) → Brief an den Vater critique of inherited Jewish formality (1919); no clear adult creed label", certainty: 0.5, cites: [{source: S1, locator: "father paragraph"}, {source: S2, locator: "nos. 50, 54"}, {source: S6, locator: "Judentum section"}], how_known: "Sources agree on sequence; adult A unscored under P3."}
  coder_notes: "Deepen D1 2026-10-24: P3 reopen condition (diaries equate God with indestructible) not met in accessible own-voice texts. IA Brod Diaries OCR 401. Blue Octavo and Brief an den Vater checked. Brod hope conversation (S7) stays third-party lead (P42). A and B stay BELOW. Not a scientist (P30). No fallacy_catalog."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Jewish, German-speaking, of Prague", certainty: 0.7, cites: [{source: S1, locator: "father paragraph"}, {source: S4, locator: "Early life"}], how_known: "Britannica and Wikipedia."}
  religious_heritage_by_birth: {value: "Jewish", certainty: 0.7, cites: [{source: S1, locator: "Life paragraph"}, {source: S4, locator: "Early life"}], how_known: "Britannica and Wikipedia."}
  baptism_or_initiation: {value: "Bar mitzvah at age 13; Jewish education ended then", certainty: 0.7, cites: [{source: S4, locator: "Education"}], how_known: "Wikipedia."}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1913–1924", certainty: 0.7, cites: [{source: S1, locator: "opening; father paragraph"}], how_known: "From the first listed lasting contribution (1913) to his death (1924): the span never runs past death (P30), though two listed works appeared posthumously."}
  age_at_first_lasting_contribution: {value: 30, certainty: 0.7, cites: [{source: S1, locator: "opening; father paragraph"}], how_known: "1913 − 1883 = 30 (P30)."}
  first_evidence_of_lio_type_views: {value: "1917–18: Zürau aphorisms on the indestructible and a personal God", year: 1917, certainty: 0.5, cites: [{source: S2, locator: "no. 50"}], how_known: "Brod Diaries still not fully readable this pass (P30 #7); Brief an den Vater 1919 is heritage, not LIO place/deny."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "1917–18 falls inside 1913–1924.", certainty: 0.5, cites: [{source: S2, locator: "no. 50"}], how_known: "Dates of what was read."}
  worldview_during_major_work: {value: "Figurative: trust in an 'indestructible' within persons; the sensible world as evil within the spiritual (1917–18); inherited Jewish practice criticized as empty formality (1919)", certainty: 0.5, cites: [{source: S2, locator: "nos. 50, 54, 71"}, {source: S6, locator: "Judentum section"}], how_known: "His notebooks and letter."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Not a geometric style.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Not read."}
  circle_present: {value: "unclear", rationale: "The indestructible within persons; figurative; personal God as one possible expression.", certainty: 0.5, cites: [{source: S2, locator: "no. 50; no. 70. 71"}], how_known: "Coder's reading."}
  reading: "An indestructible core in each person; the personal God as one of its expressions; sensible world as evil within a spiritual world — figurative, not a nature-order claim."
  notes: "Lane B only. Fiction (Trial, Castle) not used to score A/B (P42 drama/persona)."

institutions:
  - {value: "Assicurazioni Generali (Prague)", role: "insurance clerk", years: "1907–1908", kind: commercial, certainty: 0.7, cites: [{source: S1, locator: "double life paragraph"}, {source: S4, locator: "Employment"}], how_known: "Britannica and Wikipedia."}
  - {value: "Workers' Accident Insurance Institute for the Kingdom of Bohemia", role: "official", years: "1908–1922", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "double life paragraph"}, {source: S4, locator: "Employment"}], how_known: "Britannica and Wikipedia."}
collaborators:
  - {value: "Max Brod", relation: other, note: "closest friend, literary executor and biographer; published aphorisms and diaries against Kafka's wish to burn them", certainty: 0.7, cites: [{source: S1, locator: "double life paragraph"}, {source: S4, locator: "Max Brod"}], how_known: "Britannica and Wikipedia."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 96"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Britannica article is unsigned (Britannica Editors); live fetch 403 this pass — body retained from create-pass; Wikipedia dual bio added."
    - "Worldview rests on figurative private aphorisms (P3, P42)."
    - "Brod Diaries (IA) access-restricted (OCR 401); full critical diaries (Ross Benjamin / Fischer) unread."
    - "Brod-reported conversations are third-party (P42) — not used to score A."
  open_questions:
    - "Open full Brod / critical Diaries (IA borrow or library) for any own-voice God=indestructible equate — P3 reopen."
    - "German Blue Octavo primary page for the 'Believing means…' line."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Franz Kafka.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Franz-Kafka. Read live 2026-10-18 (Wayback rate-limited); re-check 2026-10-24 returned 403 — body retained from create-pass."
    url: "https://www.britannica.com/biography/Franz-Kafka"
    accessed: 2026-10-18
    source_quality: "reference entry"
    reliability_note: "Unsigned article. Body only; the Top Questions and Quick Facts are not cited."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Franz Kafka"
    citation: "Kafka, Franz. \"Betrachtungen über Sünde, Leid, Hoffnung und den wahren Weg.\" In Beim Bau der Chinesischen Mauer, ed. Max Brod and Hans Joachim Schoeps (Berlin: Gustav Kiepenheuer, 1931). Wikisource transcription: https://de.wikisource.org/wiki/Betrachtungen_%C3%BCber_S%C3%BCnde,_Leid,_Hoffnung_und_den_wahren_Weg"
    url: "https://de.wikisource.org/wiki/Betrachtungen_%C3%BCber_S%C3%BCnde,_Leid,_Hoffnung_und_den_wahren_Weg"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Volunteer transcription of the 1931 edition, marked as proofread twice against the page scans; treated as a web copy (cap 0.7). Re-read deepen D1 including nos. 69 and 74."
    used_for: [worldview, timing, lane_b, contribution]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-18
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [identity, review]
  - id: S4
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. \"Franz Kafka.\" Wikipedia. https://en.wikipedia.org/wiki/Franz_Kafka. Dual bio (P50). Read 2026-10-24."
    url: "https://en.wikipedia.org/wiki/Franz_Kafka"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Used for dual-bio basics, adolescent atheism cite, diary 'Was habe ich mit Juden gemeinsam' lead, and Zürau/Blue Octavo context. Worldview coding rests on S2/S6, not on Wikipedia paraphrases of 'indestructible Being'."
    used_for: [identity, basics, contribution, childhood, heritage, institutions, collaborators, worldview]
  - id: S5
    type: secondary
    kind: other
    author: "Franz Kafka (via Kafka Project / Blue Octavo attributions)"
    citation: "Kafka Project Archive of Quotes (\"Believing means liberating the indestructible element in oneself…\", labeled Diaries); standard book attribution The Blue Octavo Notebooks (1954). https://www.kafka.org/archive/quotes/"
    url: "https://www.kafka.org/archive/quotes/"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "English web quote; German primary page unread. Used only to test P3 reopen — does not equate God with the indestructible."
    used_for: [worldview]
  - id: S6
    type: primary
    kind: letter
    author: "Franz Kafka"
    citation: "Kafka, Franz. Brief an den Vater (composed autumn 1919). Wikisource transcription of the facsimile edition (Fischer, 1994): https://de.wikisource.org/wiki/Brief_an_den_Vater"
    url: "https://de.wikisource.org/wiki/Brief_an_den_Vater"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Wikisource proofread transcription of the facsimile; unsent letter. Judentum section used for heritage/practice, not A place/deny."
    used_for: [worldview, childhood, heritage, contribution]
  - id: S7
    type: secondary
    kind: other
    author: "Max Brod (via Wikiquote)"
    citation: "Wikiquote contributors. \"Franz Kafka\" — Brod-reported 1920 conversation ('Oh, hope enough, infinite hope — only not for us'), from Brod, Franz Kafka: A Biography. https://en.wikiquote.org/wiki/Franz_Kafka"
    url: "https://en.wikiquote.org/wiki/Franz_Kafka"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Third-party reported speech (P42). Lead only — not used to score A or primary_system."
    used_for: [worldview]
---

# Franz Kafka

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Franz Kafka (1883–1924), German-language writer of Prague [S1; S4]. Deepen D1: primary_system BELOW_THRESHOLD; A BELOW_THRESHOLD (alt 3; P3 reopen not met); B BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not plotted. Chart-moving NO.

## Life and work

Law doctorate 1906; insurance official 1907–1922; died 1924 [S1; S4].

## Contribution and impact

Das Urteil (1913), Die Verwandlung (1915), Der Prozess (1925), Das Schloss (1926) [S1; S4]. Zürau Aphorisms (1931 posthumous); Brief an den Vater (1919) [S2; S6].

## Childhood and education

Prosperous Jewish family; Altstädter Gymnasium; adolescent atheism [S1; S4]. Inherited temple practice later called a 'Nichts' [S6].

## Adult working worldview

Zürau aphorisms on the indestructible and a personal God [S2, nos. 50, 54, 69, 70.71]. Blue Octavo 'Believing…' does not equate God with the indestructible [S5]. No nature-order statement for B [S2 no. 54; P16].

## Heritage (context only)

Jewish, German-speaking [S1; S4].

## Timing

First lasting contribution 1913, at 30 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Figurative [S2]. Fiction not scored for A/B (P42).

## Open questions

- Full Brod / critical Diaries for P3 reopen.
- German Blue Octavo primary page.

## Research log

- 2026-10-18: Read Britannica (live) and the Wikisource transcription of the 1931 aphorisms directly.
- 2026-10-24: Deepen D1. Wikipedia EN dual bio; Wikisource Brief an den Vater; Wikisource aphorisms re-read (incl. 69, 74); Kafka Project / Blue Octavo quote; Wikiquote Brod hope lead; IA Brod Diaries OCR 401. Wrote drafts/deepen_kafka-franz.md (untracked). No figures refresh. No fallacy_catalog.
