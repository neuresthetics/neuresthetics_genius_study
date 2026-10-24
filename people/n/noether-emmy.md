---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 4
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch B)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (stage 3 batch B). Basics from MacTutor and Britannica (Britannica Editors, first page); Weyl's funeral address (English translation on MacTutor) read for her character. No statement by Noether on religion, God or nature was found in what was read. primary_system BELOW_THRESHOLD; all five axes BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. All codings are drafts for v8's review. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit fix, stage 3 batch B (two blind runs at 3db6511). S3: the translator is now credited (Ian Beaumont, in Peter Roquette's article 'Emmy Noether and Hermann Weyl', per the MacTutor page); the earlier note said the page named none. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 rulings P14–P28 (v8, main 6aeba87), schema 1.3. full_name 1.0 → 0.7, alternative 'Emmy Amalie Noether' (P15); primary_system BELOW_THRESHOLD → UNKNOWN, A–E BELOW_THRESHOLD → UNKNOWN, mid_basin BELOW_THRESHOLD → UNKNOWN (P19, P16); IAS kind university → research institute (P21); schooling/0 stage dame or charity school → elementary school, schooling/1 run_by state or municipal (P21); first-year 1921 alternative dropped, since only taking the theorem off the list could give it (P23); Dick quotations marked primary check pending (P26); single-source 1.0 fields → 0.7 (P15) (major_works/0, definition_fit, working_years, Gordan); region_of_birth, region_of_work keep 1.0 with a Britannica cite. Not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "D1 deepen (queue #22; no fallacy_catalog). Read Noether 1918 Invariante Variationsprobleme (Tavel arXiv), Tollmien Lebensläufe (1907/1919 CVs), Tollmien 2000 Dissidentin note, Dick 1981 OCR (Jewish-religion classes primary-check), NDB (israelitisch / seit 1920 evangelisch), JKG Göttingen on 1920 Austritt. A stays UNKNOWN (no locus statement). B UNKNOWN → 3 @ 0.5 inference_from_work, alt 4, support corroborated (P30 scientist; P35). Contested adult affiliation (Dissidentin vs evangelisch) in nominal_affiliations; JUDA/CHRIST rejected. P47 on S1–S10. working_years aligned to major_work_period 1915–1933 (P30). Chart still unplotted. Not reviewed."}

identity:
  id: noether-emmy
  display_name: "Emmy Noether"
  roster:
    canonical_name: "Emmy Noether"
    rank: 22
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Amalie Emmy Noether", certainty: 0.7, cites: [{source: S1, locator: "heading ('Emmy Amalie Noether')"}, {source: S2, locator: "'Also known as: Amalie Emmy Noether'; Quick Facts 'In full: Amalie Emmy Noether'"}], how_known: "Two sources give both names, in different orders, so 0.7 under the name-order rule (P15). Draft judgment (one line): Britannica's order kept as the value.", alternatives: [{value: "Emmy Amalie Noether", cites: [{source: S1, locator: "heading"}], note: "MacTutor's order."}]}
  native_name: {value: "Amalie Emmy Noether (German)", certainty: 0.7, cites: [{source: S2, locator: "'Also known as' line"}], how_known: "German name."}
  aliases:
    - {name: "Emmy Amalie Noether", kind: "roster alias"}
    - {name: "Emmy-Noether", kind: "roster alias"}
    - {name: "Noether-Emmy", kind: "roster alias"}

basics:
  birth:
    date: {value: "1882-03-23", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Info"}, {source: S2, locator: "Born line"}], how_known: "Two sources agree."}
    place: {value: "Erlangen, Bavaria", modern_name: "Erlangen, Bavaria, Germany", polity_then: "German Empire (Kingdom of Bavaria)", certainty: 1.0, cites: [{source: S1, locator: "Quick Info"}, {source: S2, locator: "Born line"}], how_known: "Two sources agree."}
  death:
    date: {value: "1935-04-14", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Info"}, {source: S2, locator: "Died line"}], how_known: "Two sources agree."}
    place: {value: "Bryn Mawr, Pennsylvania", modern_name: "Bryn Mawr, Pennsylvania, USA", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "Quick Info"}, {source: S2, locator: "Died line"}], how_known: "Two sources agree."}
  first_lasting_contribution_year:
    value: 1918
    certainty: 0.7
    cites: [{source: S2, locator: "'In 1918 Noether discovered'"}]
    how_known: "Noether's theorem linking symmetries and conservation laws (Britannica), the earliest listed lasting contribution, so it sets the year (P17, P23); the 1921 ideal theory is later. Britannica alone dates it, so 0.7 (P15). The draft's 1921 alternative is dropped: it could be the year only if the theorem were taken off the list (P23)."
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S2, locator: "1918 paragraph"}, {source: S1, locator: "Biography (1921)"}], how_known: "The year (1918) and every other listed lasting contribution (the 1921 ideal theory, S1) fall in 1850–1949 (P2); two sources, and the bucket does not depend on which item is earliest, so 1.0 (P15)."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "Quick Info"}, {source: S2, locator: "Born line"}], how_known: "Germany is Western Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "Biography"}, {source: S2, locator: "opening ('invited to the University of Göttingen in 1915')"}], how_known: "Erlangen and Göttingen until 1933; Bryn Mawr and Princeton (North America) 1933–1935."}
  sex_as_recorded: {value: "female", certainty: 1.0, cites: [{source: S1, locator: "Biography"}, {source: S2, locator: "opening"}], how_known: "As the sources record it."}
  languages_of_work: {value: [German], certainty: 1.0, cites: [{source: S1, locator: "Biography (paper titles)"}, {source: S2, locator: "paper titles"}], how_known: "Her papers are in German."}
  occupations: {value: ["mathematician", "university lecturer"], certainty: 1.0, cites: [{source: S1, locator: "Biography"}, {source: S2, locator: "opening"}], how_known: "Two sources."}

contribution:
  fields: {value: ["abstract algebra", "invariant theory", "ring and ideal theory", "mathematical physics"], certainty: 1.0, cites: [{source: S1, locator: "Summary; Biography"}, {source: S2, locator: "opening"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Noether's theorem: symmetries of a physical system correspond to conservation laws", year: "1918", kind: theory, lasting: "key result in theoretical physics", certainty: 1.0, cites: [{source: S2, locator: "1918 paragraph"}, {source: S1, locator: "Biography (1915 paragraph)"}, {source: S5, locator: "title and §1"}], how_known: "Two biographies plus her 1918 paper."}
    - {value: "Abstract ideal theory in rings with the ascending chain condition (Idealtheorie in Ringbereichen)", year: "1921", kind: theory, lasting: "foundation of modern commutative algebra", certainty: 1.0, cites: [{source: S1, locator: "Biography (1921)"}, {source: S2, locator: "ideal theory paragraph"}], how_known: "Two sources."}
    - {value: "Noncommutative algebras and their representations (with Hasse and Brauer)", year: "1927–1933", kind: theory, lasting: "structure theory of algebras", certainty: 1.0, cites: [{source: S1, locator: "Biography (1927 onward)"}, {source: S2, locator: "1927 paragraph"}], how_known: "Two sources."}
  evidence_of_impact:
    - {value: "Much of van der Waerden's Moderne Algebra, vol. 2, is her work", kind: "standard textbook canon", certainty: 0.7, cites: [{source: S1, locator: "Biography (1924)"}], how_known: "MacTutor."}
    - {value: "Einstein: 'the most significant creative mathematical genius thus far produced since the higher education of women began'", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S2, locator: "last paragraph"}], how_known: "Britannica quoting Einstein (secondary quotation)."}
  major_works:
    - {value: "Idealtheorie in Ringbereichen", year: 1921, kind: "paper or paper series", certainty: 0.7, cites: [{source: S1, locator: "Biography (1921)"}], how_known: "MacTutor alone, so 0.7 under the single-source rule (P15)."}
    - {value: "Invariante Variationsprobleme", year: 1918, kind: "paper or paper series", certainty: 1.0, cites: [{source: S5, locator: "title"}, {source: S2, locator: "1918 paragraph"}], how_known: "Her published paper plus Britannica."}
  honours:
    - {value: "Alfred Ackermann-Teubner Memorial Prize (with Emil Artin)", year: 1932, certainty: 0.7, cites: [{source: S1, locator: "Biography (1932)"}], how_known: "MacTutor."}
  definition_fit: {value: "clearly meets", rationale: "A founder of modern abstract algebra; Noether's theorem in physics.", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "One source cited, so 0.7 under the single-source rule (P15)."}

childhood:
  family_religion: {value: "Jewish (both parents of Jewish origin)", certainty: 0.7, cites: [{source: S1, locator: "Biography, paragraph 1"}], how_known: "MacTutor: 'Both Emmy's parents were of Jewish origin'."}
  family_religious_practice: {value: "At school she 'was one of the few who attended classes in the Jewish religion'", certainty: 0.7, cites: [{source: S1, locator: "Biography, Auguste Dick quotation on the Fahrstrasse school"}, {source: S8, locator: "p. 9 (English 1981: 'one of the few who attended classes in the Jewish religion')"}], how_known: "MacTutor quoting Dick; primary-check against Dick 1981 OCR (S8) confirms the wording (P26 cleared)."}
  parents_and_household:
    - {value: "Father, Max Noether, mathematician and professor at Erlangen", name: "Max Noether", role: father, certainty: 1.0, cites: [{source: S1, locator: "Biography, paragraph 1"}, {source: S2, locator: "opening"}], how_known: "Two sources."}
    - {value: "Mother, Ida Amalia Kaufmann (1852–1915), from a wealthy Cologne family", name: "Ida Amalia Noether (née Kaufmann)", role: mother, certainty: 0.7, cites: [{source: S1, locator: "Biography, paragraph 1"}], how_known: "MacTutor."}
  household_circumstances: {value: "Eldest of four children (three younger brothers); academic household in Erlangen", certainty: 0.7, cites: [{source: S1, locator: "Biography, paragraph on her brothers and first school"}], how_known: "MacTutor."}
  schooling:
    - {value: "Elementary school on Fahrstrasse, Erlangen", stage: "elementary school", years: "–1889", certainty: 0.7, cites: [{source: S1, locator: "Biography, paragraph on her brothers and first school"}], how_known: "MacTutor ('After elementary school'). Stage is the level (P21), so elementary school (was dame or charity school as the nearest stage); MacTutor does not say who ran it, so no run_by."}
    - {value: "Städtische Höhere Töchter Schule, Erlangen (German, English, French, arithmetic)", stage: "grammar or secondary school", run_by: "state or municipal", years: "1889–1897", certainty: 0.7, cites: [{source: S1, locator: "Biography, high-school paragraph (1889–1897, 1900)"}], how_known: "MacTutor. run_by from the school's name, 'Städtische' (municipal) (P21)."}
    - {value: "Certified teacher of English and French (Bavarian state examinations)", stage: other, years: "1900", certainty: 1.0, cites: [{source: S1, locator: "Biography, high-school paragraph (1889–1897, 1900)"}, {source: S2, locator: "opening"}], how_known: "Two sources."}
    - {value: "University of Erlangen (auditor 1900–1902; matriculated 1904; doctorate 1907 under Paul Gordan), with a semester at Göttingen 1903–04", stage: university, years: "1900–1907", certainty: 1.0, cites: [{source: S1, locator: "Biography, university paragraphs (1900–1907)"}, {source: S2, locator: "opening"}], how_known: "Two sources."}
  early_mathematics: {value: "arithmetic only", note: "Arithmetic at the girls' high school; university mathematics began at 18 (MacTutor).", certainty: 0.5, cites: [{source: S1, locator: "Biography, high-school paragraph (1889–1897, 1900)"}], how_known: "MacTutor lists her school subjects; nothing more on mathematics before 17."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [German, English, French], certainty: 0.7, cites: [{source: S1, locator: "Biography, high-school paragraph (1889–1897, 1900)"}], how_known: "English and French at school."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1915–1933", certainty: 1.0, cites: [{source: S1, locator: "Biography"}, {source: S2, locator: "1915–1933 paragraphs"}], how_known: "Aligned to timing.major_work_period (P30 addendum): Göttingen years from the Hilbert invitation through Nazi dismissal."}
  nominal_affiliations:
    - {value: "israelitische Konfession (Jewish confession) stated on her own doctoral curriculum vitae", year: 1907, role: member, certainty: 1.0, cites: [{source: S6, locator: "1907 handwritten Lebenslauf transcription ('bayerischer Staatsangehörigkeit und israelitischer Konfession')"}], how_known: "Her own words in the 1907 doctoral CV (Tollmien transcription of Erlangen Promotionsakte). Membership, not ideology."}
    - {value: "Left the Jewish community (Austritt) in 1920; adult formal affiliation contested — Tollmien reconstructs Dissidentin (Konfessionslos); NDB states evangelisch since 1920", year: 1920, role: other, certainty: 0.5, cites: [{source: S7, locator: "paragraph on 1919 Habilitationslebenslauf omitting israelitische Konfession; Dissidentin reading"}, {source: S9, locator: "header '(israelitisch, seit 1920 evangelisch)'"}, {source: S10, locator: "announcement of Tollmien Lehrhaus: Austritt 1920"}], how_known: "Contested (P25): Tollmien (scholarly reconstruction) vs NDB reference entry; JKG Göttingen event page attributes the 1920 Austritt to Tollmien's research. No baptism record read. Named alternatives kept. Membership still not a worldview code.", alternatives: [{value: "Dissidentin / Konfessionslos (no church) in the 1920s", cites: [{source: S7, locator: "Dissidentin sentence"}], note: "Tollmien 2000."}, {value: "evangelisch (Protestant) from 1920", cites: [{source: S9, locator: "header"}], note: "NDB; baptism not verified this pass."}]}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Searched MacTutor, Britannica, Weyl funeral address, 1918 paper, 1907/1919 Lebensläufe, Dick 1981 OCR, Tollmien, NDB: no statement of hers linking science and religion."}
  primary_system:
    value: UNKNOWN
    cites: [{source: S1, locator: "Biography"}, {source: S6, locator: "1907 and 1919 Lebensläufe"}, {source: S7, locator: "Dissidentin paragraph"}, {source: S9, locator: "header Konfession line"}]
    how_known: "D1 re-search still finds no statement of hers on God, nature-as-divine, or a metaphysical system. 1907 israelitische Konfession and 1920 Austritt / contested Dissidentin-vs-evangelisch are nominal_affiliations only (membership ≠ ideology). Weyl (S3) speaks of God and souls in Weyl's voice. Kept UNKNOWN (P19 silence on working metaphysics)."
    note: "Draft judgment (one line): UNKNOWN — affiliation facts do not yield a code; named alternative BELOW_THRESHOLD if v8 treats Dissidentin plus silence as weak evidence of AGNOS/SECHUM without a system statement."
  secondary_system: {value: UNKNOWN, how_known: "No second-system evidence in sources read."}
  candidate_codes_considered:
    - {code: JUDA, reason: "Rejected: Jewish heritage, childhood religion classes, and 1907 israelitische Konfession are heritage/membership; she left the Jewish community in 1920 (S10/S7); no adult Jewish practice or belief statement found. Heritage is never a code.", cites: [{source: S1, locator: "Biography, paragraph 1 and Dick quotation"}, {source: S6, locator: "1907 Lebenslauf"}, {source: S10, locator: "1920 Austritt"}]}
    - {code: CHRIST, reason: "Rejected: NDB's 'seit 1920 evangelisch' is a contested membership claim (alt Dissidentin); no confession of Christian belief or locus statement found.", cites: [{source: S9, locator: "header"}, {source: S7, locator: "Dissidentin"}]}
    - {code: AGNOS, reason: "Not coded: Dissidentin / Austritt show leaving formal religion, not an explicit suspension of judgment about God (P20). AGNOS is also a stub system file.", cites: [{source: S7, locator: "Dissidentin"}]}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "D1 searched MacTutor, Britannica, Weyl funeral address, 1907/1919 Lebensläufe, 1918 paper, Dick 1981, Tollmien, NDB: nothing of hers places or denies God. 1920 Austritt / Dissidentin / contested evangelisch are affiliation facts, not locus (P20). Kept UNKNOWN (P19 silence), not BELOW_THRESHOLD — affiliation evidence does not speak to A. Named alternative if v8 prefers BELOW_THRESHOLD on Dissidentin-as-weak-evidence: A BELOW_THRESHOLD."}
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      support: corroborated
      cites: [{source: S5, locator: "§1 / note 15 (field equations; 'laws of conservation')"}, {source: S6, locator: "1919 Lebenslauf paragraph on Invariante Variationsprobleme (Erhaltungssätze; Feldgleichungen)"}, {source: S2, locator: "1918 paragraph (Noether's theorem)"}]
      how_known: "Scientist under P30 (listed lasting contribution about physical systems: Noether's theorem). No statement of her own on law vs reserved exception, so B 3 at 0.5 with 4 as named alternative, never 4 (P35). Two independent streams: her published 1918 paper (S5) plus her own 1919 CV description of Erhaltungssätze (S6), with Britannica's theorem note (S2) agreeing → corroborated (P48)."
      rationale: "Draft judgment (one line): leans LIO from working mathematical physics, not the pole. Scored on her account of nature (P6). Invariante Variationsprobleme treats conservation laws (Erhaltungssätze) and field-equation dependencies in mechanics and relativity as special cases of invariance under continuous groups (S5; S6 in her own CV words); that is lawful physical structure without a stated no-exception or anti-miracle claim. Named alternative: 4."
    C_ledger: {value: UNKNOWN, how_known: "Still nothing of hers on judgement, reward or afterlife. Weyl's 'souls will meet again' (S3) is Weyl's voice. Kept UNKNOWN (P19)."}
    D_authority: {value: UNKNOWN, how_known: "Still nothing on revelation or scripture. Kept UNKNOWN (P19)."}
    E_scope: {value: UNKNOWN, how_known: "Scored on the world's order (P7). Still nothing of hers on favour for a group in events or on the same rules for every kind of being. Weyl's 'did not believe in evil' (S3) is about trust in people. Kept UNKNOWN (P19), as on the 2026-10-02 ruling for this mathematician."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied; UNKNOWN takes precedence over B's score (§6, P19)."}
  statements:
    - text: "Ich, Amalie Emmy Noether, bayerischer Staatsangehörigkeit und israelitischer Konfession, bin geboren zu Erlangen am 23. März 1882 …"
      cites: [{source: S6, locator: "1907 handwritten Lebenslauf (Erlangen Promotionsakte)"}]
      date: "1907-12"
      context: "Opening of her doctoral curriculum vitae; states Jewish confession as a legal/confessional membership fact."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
    - text: "Die zweite Arbeit 'Invariante Variationsprobleme' … zieht die Folgerungen aus der Invarianz eines Variationsproblems gegenüber einer solchen Gruppe. In dem allgemeinen Resultate sind als Spezialfälle die in der Mechanik bekannten Sätze über erste Integrale, die Erhaltungssätze und die in der Relativitätstheorie aufgetretenen Abhängigkeiten zwischen den Feldgleichungen enthalten …"
      cites: [{source: S6, locator: "1919 Habilitationslebenslauf, Differentialinvarianten paragraph"}]
      date: "1919-05"
      context: "Her own description of the 1918 paper in the habilitation CV: conservation laws and relativity field-equation dependencies as special cases."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
    - text: "ψ_i = 0, or, somewhat more generally, ψ_i = T_i, where T_i are newly adjoined functions, are referred to in physics as 'field equations.' In the case ψ_i = T_i, the identities (13) goes over into equations Div B^(λ) = Σ T_i δu_i^(λ), likewise known in physics as laws of conservation."
      cites: [{source: S5, locator: "§1, note 15 and following (Tavel English)"}]
      date: "1918"
      context: "Published theorem paper linking variational invariance to conservation laws / field equations."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
  changes_over_life: []
  coder_notes: "D1 coder's call: A stays UNKNOWN (not BELOW) because Austritt/Dissidentin/evangelisch speak to affiliation, not locus (P20/P19). B raised via P30 scientist + P35 working-science path; her 1918/1919 conservation-law wording supports the inference but does not state no-exception, so not written_profession 0.7. Contested 1920 affiliation logged under nominal_affiliations with alternatives (P25); does not move primary_system. JUDA and CHRIST rejected. Weyl (S3) remains Weyl's voice for God/souls. Politics (USPD/SPD, pacifism) not scored. Open: Rowe/Koreuber 2020 full text; baptism register for NDB evangelisch claim; Hasse letters already maths-heavy."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German Jewish", certainty: 1.0, cites: [{source: S1, locator: "Biography, paragraph 1"}, {source: S2, locator: "1933 paragraph ('Noether and many other Jewish professors')"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: "Jewish", certainty: 0.7, cites: [{source: S1, locator: "Biography, paragraph 1 and Dick quotation"}], how_known: "MacTutor."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "NDB claims evangelisch since 1920 but no baptism record was read this pass; Tollmien's Dissidentin reading conflicts. Contested affiliation is under nominal_affiliations."}
  childhood_catechism: {value: "Classes in the Jewish religion at school", certainty: 0.7, cites: [{source: S1, locator: "Biography, Auguste Dick quotation on the Fahrstrasse school"}, {source: S8, locator: "p. 9"}], how_known: "Dick 1981 (S8) confirms MacTutor's quotation (P26 cleared)."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1915–1933", certainty: 1.0, cites: [{source: S1, locator: "Biography"}, {source: S2, locator: "1915–1933 paragraphs"}], how_known: "Göttingen years."}
  age_at_first_lasting_contribution: {value: 36, certainty: 0.7, cites: [{source: S2, locator: "Born line; 1918 paragraph"}], how_known: "Born March 1882; theorem 1918 (month not checked; 35 or 36)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement of hers scored at 3 or 4 as an LIO-type view; B rests on working science, which is not an LIO-type view (P27)."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "Nothing of hers on God or nature was read at the LIO-type-view bar (P27); B is inference_from_work only.", certainty: 0.5, cites: [{source: S1, locator: "Biography"}, {source: S5, locator: "whole"}, {source: S6, locator: "Lebensläufe"}], how_known: "Absence at the P27 bar in sources read; not evidence of absence."}
  worldview_during_major_work: {value: "Affiliation contested after 1920 Austritt (Dissidentin vs evangelisch); working metaphysics UNKNOWN; B inferred from mathematical physics", certainty: 0.5, cites: [{source: S7, locator: "Dissidentin"}, {source: S9, locator: "header"}, {source: S5, locator: "§1"}], how_known: "Synthesis of D1 sources; not a code."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "She remoulded 'the axiomatic approach into a powerful research instrument' (Weyl, S3); her ideal theory is built from axioms (S2).", certainty: 0.5, cites: [{source: S3, locator: "paragraph on her work"}, {source: S2, locator: "ideal theory paragraph ('On an axiomatic basis')"}], how_known: "Coder's reading of two sources."}
  form_acquired: {value: "adulthood, before major work", certainty: 0.5, cites: [{source: S1, locator: "Biography, university and Fischer paragraphs"}], how_known: "Mathematics from age 18; Fischer moved her toward Hilbert's abstract approach after 1911."}
  circle_present: {value: "unclear", rationale: "No God–Nature statement read.", certainty: 0.5, cites: [{source: S1, locator: "Biography"}], how_known: "No evidence either way."}
  reading: "As belief, not finding: form present, circle unclear. The record does not test H1."
  notes: ""

institutions:
  - {value: "University of Göttingen", role: "lectured under Hilbert's name; Privatdozent from 1919", years: "1915–1933", kind: university, certainty: 1.0, cites: [{source: S1, locator: "Biography (1915, 1919)"}, {source: S2, locator: "1915 paragraph"}], how_known: "Two sources."}
  - {value: "Bryn Mawr College", role: "visiting professor", years: "1933–1935", kind: university, certainty: 1.0, cites: [{source: S1, locator: "Biography (1933)"}, {source: S2, locator: "1933 paragraph"}], how_known: "Two sources."}
  - {value: "Institute for Advanced Study, Princeton", role: "weekly lectures", years: "1934–1935", kind: "research institute", certainty: 0.7, cites: [{source: S1, locator: "Biography (February 1934)"}], how_known: "MacTutor. Kind 'research institute' (P21)."}
collaborators:
  - {value: "David Hilbert", relation: "mentor or employer", note: "invited her to Göttingen in 1915", certainty: 1.0, cites: [{source: S1, locator: "Biography (1915)"}, {source: S2, locator: "1915 paragraph"}], how_known: "Two sources."}
  - {value: "Paul Gordan", relation: teacher, note: "doctoral adviser", certainty: 0.7, cites: [{source: S1, locator: "Biography (1907)"}], how_known: "MacTutor alone, so 0.7 under the single-source rule (P15)."}
  - {value: "Hermann Weyl", relation: other, note: "colleague; gave her funeral address", certainty: 1.0, cites: [{source: S3, locator: "whole"}], how_known: "The address."}
  - {value: "Albert Einstein", roster_id: einstein-albert, relation: other, note: "praised her mathematics; her 1915 work served general relativity", certainty: 0.7, cites: [{source: S2, locator: "1915 paragraph; last paragraph"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 5: Claude, DeepSeek, Gemini, GPT, Grok).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 22"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "A_locus and primary_system still UNKNOWN after D1; B scored only at 0.5 (P35)."
    - "Adult formal religion contested: Tollmien Dissidentin vs NDB evangelisch since 1920 (P25)."
    - "full_name: the two sources give the given names in different orders, so 0.7 (P15)."
    - "Britannica still first-page read from 2026-10-02 (live fetch often 403)."
  open_questions:
    - "Baptism / Kirchenaustritt primary register for the 1920 affiliation change (to settle Dissidentin vs evangelisch)."
    - "Rowe & Koreuber, Proving It Her Way (2020), and Tollmien's Judentum booklets, for any private religion remark."
    - "German text of Invariante Variationsprobleme beside Tavel (print check) if B is ever lifted toward written_profession 0.7."

sources:
  - id: S1
    type: secondary
    kind: "institutional page"
    author: "J J O'Connor and E F Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Emmy Amalie Noether.\" MacTutor History of Mathematics, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Noether_Emmy/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Noether_Emmy/"
    accessed: 2026-10-02
    reliability_note: "Biography; paragraphs counted from 'Emmy Noether's father'."
    source_quality: "scholarly reconstruction"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Emmy Noether.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Emmy-Noether."
    url: "https://www.britannica.com/biography/Emmy-Noether"
    accessed: 2026-10-02
    reliability_note: "Unsigned editors' article; first page only."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, heritage, timing, lane_b, institutions, collaborators]
  - id: S3
    type: primary
    kind: other
    author: "Hermann Weyl"
    year: 1935
    citation: "Weyl, Hermann. Address at the funeral of Emmy Noether, 1935. English translation on MacTutor History of Mathematics. https://mathshistory.st-andrews.ac.uk/Extras/Weyl_Noether/."
    url: "https://mathshistory.st-andrews.ac.uk/Extras/Weyl_Noether/"
    accessed: 2026-10-02
    reliability_note: "Speech given on 18 April 1935. MacTutor follows the English translation by Ian Beaumont printed in Peter Roquette's article 'Emmy Noether and Hermann Weyl' (page reopened 2026-10-02). Weyl's words, not Noether's; used for her character and work only."
    source_quality: "primary / own words"
    used_for: [worldview, lane_b, collaborators]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Emmy Noether"
    year: 1918
    citation: "Noether, Emmy. \"Invariante Variationsprobleme.\" Nachrichten der Königlichen Gesellschaft der Wissenschaften zu Göttingen, Mathematisch-physikalische Klasse (1918): 235–257. English: M. A. Tavel, Transport Theory and Statistical Physics 1 (1971): 183–207; arXiv:physics/0503066."
    url: "https://ar5iv.labs.arxiv.org/html/physics/0503066"
    accessed: 2026-10-24
    reliability_note: "Her published theorem paper; Tavel English used this pass (German print check open)."
    source_quality: "primary / own words"
    used_for: [worldview, contribution, timing]
  - id: S6
    type: primary
    kind: other
    author: "Emmy Noether (transcription Cordula Tollmien)"
    year: 1907
    citation: "Noether, Emmy. Doctoral Lebenslauf (1907) and Habilitation Lebenslauf (1919). Transcriptions at Cordula Tollmien, \"Emmy Noether (1882–1935) – Lebensläufe.\" https://cordula-tollmien.de/noetherlebenslauf.html."
    url: "https://cordula-tollmien.de/noetherlebenslauf.html"
    accessed: 2026-10-24
    reliability_note: "Scholarly transcriptions of Erlangen Promotionsakte and Göttingen Personalakte; her own CV wording."
    source_quality: "primary / own words"
    used_for: [worldview, childhood, heritage, contribution]
  - id: S7
    type: secondary
    kind: "scholarly book"
    author: "Cordula Tollmien"
    year: 2000
    citation: "Tollmien, Cordula. \"Die Mutter der modernen Algebra\" — Emmy Noether (1882–1935). Lecture, TU Braunschweig, 24 May 2000; printed (shortened) in Frauenbüro der TU Braunschweig (ed.), Weibliche Exzellenzen (2000). https://www.cordula-tollmien.de/noethervortragbraunschweig2000.html."
    url: "https://www.cordula-tollmien.de/noethervortragbraunschweig2000.html"
    accessed: 2026-10-24
    reliability_note: "Historian of Noether; Dissidentin reading of the 1919 CV omission of israelitische Konfession; cites her 1990 Göttinger Jahrbuch biography."
    source_quality: "scholarly reconstruction"
    used_for: [worldview, heritage]
  - id: S8
    type: secondary
    kind: "scholarly book"
    author: "Auguste Dick"
    year: 1981
    citation: "Dick, Auguste. Emmy Noether 1882–1935. Translated by H. I. Blocher. Boston: Birkhäuser, 1981. OCR text via Internet Archive stream EmmyNoether1882-1935_201503."
    url: "https://archive.org/stream/EmmyNoether1882-1935_201503/Dick-EmmyNoether1882-1935_cropped_djvu.txt"
    accessed: 2026-10-24
    reliability_note: "Standard short biography; OCR used for the Jewish-religion-classes quotation (P26). No adult religion statement found in searchable text."
    source_quality: "scholarly edition or monograph"
    used_for: [childhood, heritage, worldview]
  - id: S9
    type: tertiary
    kind: encyclopedia
    author: "Rudolf Fritsch"
    year: 1999
    citation: "Fritsch, Rudolf. \"Noether, Amalie Emmy.\" In Neue Deutsche Biographie 19 (1999): 320–321. Online: https://www.deutsche-biographie.de/gnd118588443.html."
    url: "https://www.deutsche-biographie.de/gnd118588443.html"
    accessed: 2026-10-24
    reliability_note: "Reference entry; header states '(israelitisch, seit 1920 evangelisch)' without citing a baptism register — contested against Tollmien Dissidentin."
    source_quality: "reference entry"
    used_for: [worldview, heritage]
  - id: S10
    type: secondary
    kind: other
    author: "Jüdische Kultusgemeinde für Göttingen und Südniedersachsen"
    year: 2018
    citation: "JKG Göttingen. \"Die jüdische Mathematikerin Emmy Noether\" (announcement of Cordula Tollmien Lehrhaus talk, 16 Sept 2018). https://jkg-goettingen.org/2018/09/06/die-juedische-mathematikerin-emmy-noether/."
    url: "https://jkg-goettingen.org/2018/09/06/die-juedische-mathematikerin-emmy-noether/"
    accessed: 2026-10-24
    reliability_note: "Community event page summarizing Tollmien: Noether left the Jewish community in 1920; Einstein later said she was not a 'gute Jüdin'. Secondary to Tollmien's research."
    source_quality: "newspaper interview"
    used_for: [worldview, heritage]
---

# Emmy Noether

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Amalie Emmy Noether (1882–1935), German mathematician, proved the theorem linking symmetries to conservation laws (1918) and built the abstract theory of ideals and algebras [S2; S1; S5]. Both parents were of Jewish origin [S1]. Her own 1907 doctoral CV states *israelitischer Konfession* [S6]; by 1920 she left the Jewish community [S10], with adult formal affiliation contested (Tollmien: Dissidentin; NDB: evangelisch) [S7; S9]. No statement of hers places or denies God. Draft D1 (2026-10-24): primary_system UNKNOWN; A UNKNOWN; B 3 @ 0.5 inference_from_work (alt 4), support corroborated; C–E UNKNOWN; mid_basin UNKNOWN. Chart still unplotted.

## Life and work

Daughter of the Erlangen mathematician Max Noether, she qualified as a language teacher, then studied mathematics at Erlangen (doctorate 1907), worked at Göttingen from 1915, was dismissed by the Nazis in 1933 and taught at Bryn Mawr until her death in 1935 [S1; S2].

## Contribution and impact

Noether's theorem (1918) — symmetries of a physical system correspond to conservation laws — ideal theory (1921), and noncommutative algebras with Hasse and Brauer (1927–1933) [S1; S2; S5]. Her own 1919 Lebenslauf describes the 1918 paper as drawing out Erhaltungssätze and relativity field-equation dependencies as special cases of variational invariance [S6].

## Childhood and education

At school she was one of the few who attended classes in the Jewish religion (Dick) [S1; S8]. 1907 doctoral Lebenslauf: "bayerischer Staatsangehörigkeit und israelitischer Konfession" [S6].

## Adult working worldview

No locus statement found. 1919 habilitation Lebenslauf omits the Konfession clause [S6; S7]. Contested adult affiliation: Tollmien Dissidentin vs NDB evangelisch since 1920; JKG Göttingen (Tollmien talk) places Austritt from the Jewish community in 1920 [S7; S9; S10]. Weyl's funeral address speaks of God and souls in Weyl's voice [S3]. Lane A draft: A UNKNOWN; B 3 @ 0.5 inference_from_work from the 1918 theorem / Erhaltungssätze wording (P30/P35), alt 4, support corroborated [S5; S6; S2]; C–E UNKNOWN; mid_basin UNKNOWN.

## Heritage (context only)

German Jewish [S1; S2]. Context only — never a worldview code.

## Timing

First lasting contribution 1918 [S2]. Major-work period 1915–1933 [S1; S2]. No LIO-type views at the P27 bar; B is working-science inference only.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form present (axiomatic algebra [S3; S2]); circle unclear (no God–Nature statement).

## Open questions

- Baptism / Kirchenaustritt register for 1920 (settle Dissidentin vs evangelisch).
- Rowe & Koreuber, *Proving It Her Way* (2020); Tollmien Judentum booklets for private religion remarks.
- German print of *Invariante Variationsprobleme* beside Tavel if B is ever lifted toward written_profession 0.7.

## Research log

- 2026-10-02: Read MacTutor, Britannica (editors, first page) and Weyl's funeral address (MacTutor translation). Nothing on her religious views found.
- 2026-10-02 (v8 method rulings): Reopened MacTutor (heading, Biography 1907, 1921, February 1934) and Britannica (Born line, opening, 1915 paragraph) for the name order and the single-source fields.
- 2026-10-24 (D1 deepen, queue #22): Read Noether 1918 *Invariante Variationsprobleme* (Tavel arXiv, S5); Tollmien Lebensläufe 1907/1919 (S6); Tollmien 2000 Braunschweig lecture (Dissidentin, S7); Dick 1981 OCR (Jewish-religion classes primary-check, S8); NDB Fritsch (israelitisch / seit 1920 evangelisch, S9); JKG Göttingen Tollmien talk announcement (1920 Austritt, S10). A stays UNKNOWN; B UNKNOWN → 3 @ 0.5; chart still unplotted. Not reviewed.
