---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch B)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (stage 3 batch B). Basics from MacTutor and Britannica (Britannica Editors, first page); Weyl's funeral address (English translation on MacTutor) read for her character. No statement by Noether on religion, God or nature was found in what was read. primary_system BELOW_THRESHOLD; all five axes BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. All codings are drafts for v8's review. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit fix, stage 3 batch B (two blind runs at 3db6511). S3: the translator is now credited (Ian Beaumont, in Peter Roquette's article 'Emmy Noether and Hermann Weyl', per the MacTutor page); the earlier note said the page named none. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 rulings P14–P28 (v8, main 6aeba87), schema 1.3. full_name 1.0 → 0.7, alternative 'Emmy Amalie Noether' (P15); primary_system BELOW_THRESHOLD → UNKNOWN, A–E BELOW_THRESHOLD → UNKNOWN, mid_basin BELOW_THRESHOLD → UNKNOWN (P19, P16); IAS kind university → research institute (P21); schooling/0 stage dame or charity school → elementary school, schooling/1 run_by state or municipal (P21); first-year 1921 alternative dropped, since only taking the theorem off the list could give it (P23); Dick quotations marked primary check pending (P26); single-source 1.0 fields → 0.7 (P15) (major_works/0, definition_fit, working_years, Gordan); region_of_birth, region_of_work keep 1.0 with a Britannica cite. Not reviewed."}

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
    - {value: "Noether's theorem: symmetries of a physical system correspond to conservation laws", year: "1918", kind: theory, lasting: "key result in theoretical physics", certainty: 1.0, cites: [{source: S2, locator: "1918 paragraph"}, {source: S1, locator: "Biography (1915 paragraph)"}], how_known: "Two sources."}
    - {value: "Abstract ideal theory in rings with the ascending chain condition (Idealtheorie in Ringbereichen)", year: "1921", kind: theory, lasting: "foundation of modern commutative algebra", certainty: 1.0, cites: [{source: S1, locator: "Biography (1921)"}, {source: S2, locator: "ideal theory paragraph"}], how_known: "Two sources."}
    - {value: "Noncommutative algebras and their representations (with Hasse and Brauer)", year: "1927–1933", kind: theory, lasting: "structure theory of algebras", certainty: 1.0, cites: [{source: S1, locator: "Biography (1927 onward)"}, {source: S2, locator: "1927 paragraph"}], how_known: "Two sources."}
  evidence_of_impact:
    - {value: "Much of van der Waerden's Moderne Algebra, vol. 2, is her work", kind: "standard textbook canon", certainty: 0.7, cites: [{source: S1, locator: "Biography (1924)"}], how_known: "MacTutor."}
    - {value: "Einstein: 'the most significant creative mathematical genius thus far produced since the higher education of women began'", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S2, locator: "last paragraph"}], how_known: "Britannica quoting Einstein (secondary quotation)."}
  major_works:
    - {value: "Idealtheorie in Ringbereichen", year: 1921, kind: "paper or paper series", certainty: 0.7, cites: [{source: S1, locator: "Biography (1921)"}], how_known: "MacTutor alone, so 0.7 under the single-source rule (P15)."}
  honours:
    - {value: "Alfred Ackermann-Teubner Memorial Prize (with Emil Artin)", year: 1932, certainty: 0.7, cites: [{source: S1, locator: "Biography (1932)"}], how_known: "MacTutor."}
  definition_fit: {value: "clearly meets", rationale: "A founder of modern abstract algebra; Noether's theorem in physics.", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "One source cited, so 0.7 under the single-source rule (P15)."}

childhood:
  family_religion: {value: "Jewish (both parents of Jewish origin)", certainty: 0.7, cites: [{source: S1, locator: "Biography, paragraph 1"}], how_known: "MacTutor: 'Both Emmy's parents were of Jewish origin'."}
  family_religious_practice: {value: "At school she 'was one of the few who attended classes in the Jewish religion'", certainty: 0.7, cites: [{source: S1, locator: "Biography, Auguste Dick quotation on the Fahrstrasse school"}], how_known: "MacTutor quoting Dick's biography (secondary quotation; primary check pending, P26)."}
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
  working_years: {value: "1907–1935", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "From her doctorate to her death. MacTutor alone, so 0.7 under the single-source rule (P15)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No statement by Noether on science and religion was found in what was read."}
  primary_system:
    value: UNKNOWN
    cites: [{source: S1, locator: "Biography"}]
    how_known: "Searched MacTutor, Britannica (first page) and Weyl's funeral address: none gives a statement of hers on religion, God or nature. Jewish heritage and childhood religion classes (S1) are heritage, not evidence for a code; Weyl's address (S3) speaks of God and souls in Weyl's own voice. Re-sorted from BELOW_THRESHOLD under P19."
    note: "Draft judgment (one line): UNKNOWN, because the only religion facts are heritage, which is never a code; the alternative v8 may prefer is BELOW_THRESHOLD, if childhood religion classes count as weak evidence. Leads: Dick's biography (1970/1981) and the Noether–Hasse letters."
  secondary_system: {value: UNKNOWN, how_known: "No system evidence in what was read."}
  candidate_codes_considered:
    - {code: JUDA, reason: "Rejected: Jewish heritage and religion classes at school only (S1); no adult practice or belief recorded. Heritage is never a code.", cites: [{source: S1, locator: "Biography, paragraph 1 and Dick quotation"}]}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Searched MacTutor, Britannica (first page) and Weyl's address: nothing of hers on God. Re-sorted from BELOW_THRESHOLD under P19."}
    B_cause: {value: UNKNOWN, how_known: "Searched the same sources: no remark of hers on nature or natural law. Her work is mainly pure algebra, and Noether's theorem, though physics-facing, is a mathematical theorem; Britannica's gloss that 'conservation laws are a consequence of the symmetry properties of nature' is the encyclopedia's wording, not hers. B needs a statement about nature, and physics-facing work counts only with an explicit remark on natural law (P16); none was found, so UNKNOWN (P19). Flag: BELOW_THRESHOLD is the alternative if v8 counts physics-facing work as weak evidence."}
    C_ledger: {value: UNKNOWN, how_known: "Searched the same sources: nothing of hers on judgement, reward or afterlife. Weyl's hope that 'souls will meet again after this life' (S3) is Weyl's, not hers. Re-sorted under P19."}
    D_authority: {value: UNKNOWN, how_known: "Searched the same sources: nothing on revelation or scripture. Re-sorted under P19."}
    E_scope: {value: UNKNOWN, how_known: "Scored on the world's order (P7). Searched the same sources: nothing on favour for a group in events or on the same rules for every kind of being. Weyl's remark that she 'did not believe in evil' (S3) describes her trust in people, not the world's order. Re-sorted under P19. P19 keeps E at BELOW_THRESHOLD for a scientist's working science; her work is mathematics, and v8 agreed to UNKNOWN (2026-10-02)."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus and B_cause are UNKNOWN, so the P4 test cannot be applied; UNKNOWN because a needed axis is UNKNOWN (§6)."}
  statements: []
  changes_over_life: []
  coder_notes: "JUDA is a sourced system file but is rejected (heritage only). Weyl's funeral address (S3) was read in the English translation on MacTutor; it is Weyl's speech, used only for her character (pacifism, openness in 1933), not for her beliefs. MacTutor also quotes Weyl that after 1918 'she sided more or less with the Social Democrats' and 'always remained [...] a convinced pacifist' (politics, not scored). statements is empty because no religious or metaphysical statement of hers was found. No recorded interview exists in what was searched."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German Jewish", certainty: 1.0, cites: [{source: S1, locator: "Biography, paragraph 1"}, {source: S2, locator: "1933 paragraph ('Noether and many other Jewish professors')"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: "Jewish", certainty: 0.7, cites: [{source: S1, locator: "Biography, paragraph 1 and Dick quotation"}], how_known: "MacTutor."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: "Classes in the Jewish religion at school", certainty: 0.7, cites: [{source: S1, locator: "Biography, Auguste Dick quotation on the Fahrstrasse school"}], how_known: "Secondary quotation (MacTutor quoting Dick; primary check pending, P26)."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1915–1933", certainty: 1.0, cites: [{source: S1, locator: "Biography"}, {source: S2, locator: "1915–1933 paragraphs"}], how_known: "Göttingen years."}
  age_at_first_lasting_contribution: {value: 36, certainty: 0.7, cites: [{source: S2, locator: "Born line; 1918 paragraph"}], how_known: "Born March 1882; theorem 1918 (month not checked; 35 or 36)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No worldview statement found."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "Nothing read on God or nature.", certainty: 0.5, cites: [{source: S1, locator: "Biography"}], how_known: "Absence in two biographies; not evidence of absence."}
  worldview_during_major_work: {value: TODO}

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
    - "No worldview evidence found; record is basics only. Worldview fields re-sorted to UNKNOWN (P19)."
    - "full_name: the two sources give the given names in different orders, so 0.7 (P15)."
    - "Britannica read as its first page only."
  open_questions:
    - "Dick, Emmy Noether 1882–1935 (1970; English 1981), and the Noether–Hasse correspondence, for any statement on religion."
    - "B for physics-facing work without a remark on natural law: drafted as UNKNOWN under P16; v8 to confirm UNKNOWN rather than BELOW_THRESHOLD."

sources:
  - id: S1
    type: secondary
    kind: "institutional page"
    author: "J J O'Connor and E F Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Emmy Amalie Noether.\" MacTutor History of Mathematics, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Noether_Emmy/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Noether_Emmy/"
    accessed: 2026-10-02
    reliability_note: "Biography; paragraphs counted from 'Emmy Noether's father'."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Emmy Noether.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Emmy-Noether."
    url: "https://www.britannica.com/biography/Emmy-Noether"
    accessed: 2026-10-02
    reliability_note: "Unsigned editors' article; first page only."
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
    used_for: [worldview, lane_b, collaborators]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# Emmy Noether

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Amalie Emmy Noether (1882–1935), German mathematician, proved the theorem linking symmetries to conservation laws (1918) and built the abstract theory of ideals and algebras [S2; S1]. Both parents were of Jewish origin [S1]. No statement of hers on religion, God or nature was found. Draft under v8's stage 3 rulings (P14–P28): primary_system UNKNOWN; all axes UNKNOWN; mid_basin UNKNOWN (P19).

## Life and work

Daughter of the Erlangen mathematician Max Noether, she qualified as a language teacher, then studied mathematics at Erlangen (doctorate 1907), worked at Göttingen from 1915, was dismissed by the Nazis in 1933 and taught at Bryn Mawr until her death in 1935 [S1; S2].

## Contribution and impact

Noether's theorem (1918), ideal theory (1921) and noncommutative algebra [S1; S2].

## Childhood and education

At school she was one of the few who attended classes in the Jewish religion (Dick, quoted by MacTutor) [S1].

## Adult working worldview

Not established. Weyl's funeral address describes her openness and pacifism, and speaks of God and souls in his own voice [S3].

## Heritage (context only)

German Jewish [S1; S2]. Context only.

## Timing

First lasting contribution 1918 [S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form present (axiomatic algebra [S3; S2]); circle unclear.

## Open questions

- Dick's biography and the Noether–Hasse letters.
- B for physics-facing work without a remark on natural law (drafted UNKNOWN under P16).

## Research log

- 2026-10-02: Read MacTutor, Britannica (editors, first page) and Weyl's funeral address (MacTutor translation). Nothing on her religious views found.
- 2026-10-02 (v8 method rulings): Reopened MacTutor (heading, Biography 1907, 1921, February 1934) and Britannica (Born line, opening, 1915 paragraph) for the name order and the single-source fields.
