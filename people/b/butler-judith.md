---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA5)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to philosophy. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (skip catch-up 12/13; F3 rank 196). Goals: firm A/primary; do not force plot. Re-opened AVIVA 2010 (S2) and Haaretz/Aloni 2010 (S3) in full; Feminism and Religion / Kile Jones 2014 interview (S5); Wikipedia dual bio (S6, P50); CUP blog Aloni excerpt confirms same conversation as S3. primary_system stays AGNOS @0.5 (recorded_interview): S2 'probably an agnostic' + sceptical of any notion of the divine; after-span P20 and 'probably' hedge keep 0.5; S3/S5 corroborate this-world Jewish ethics without theistic profession (P48 support → corroborated; certainty still 0.5). A_locus stays BELOW_THRESHOLD (P20: agnostic with no stated locus view; afterlife/redemption line is C lead, not A denial). B_cause stays UNKNOWN (P30 theorist/philosopher, not scientist; Feminism&Religion science/sex-assignment remarks are construct debate, not P16 nature-order). C_ledger scored 4 @0.5 from S3 own-voice 'no after world' / 'no hopes in a final redemption' (alt BELOW). mid_basin BELOW. Chart-moving NO. Childhood/heritage/schooling enriched; P47 source_quality on S1–S6. No fallacy_catalog. No figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "AA5 audit fix (v8's call on the auditor's advice): the 'newspaper interview' label is kept with a note that these are her own emailed answers to an online magazine; Haaretz 2010 interview (Aloni) read in full and added as S3; heritage raised to 0.7."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA5, order P32: F 3, rank 196). Sources: Britannica, signed by Brian Duignan (read in full), and Butler's emailed answers to AVIVA-Berlin (2010, read in full). Lasting work: Gender Trouble (1990), 'one of the foundational texts of queer theory', whose performative theory 'greatly influenced the development of cultural theory, gender studies' (S1); span 1990, age 34. Own words (S2): 'I am very sceptical of efforts to define or portray any notion of the divine. I am probably an agnostic on religious matters, but I do sometimes still attend the synagogue'. 2010, after the span (P20 cap 0.5); written answers to an online magazine, labelled 'newspaper interview' as the nearest P21 value (auditor to confirm). primary_system AGNOS 0.5 (recorded_interview), alt BELOW_THRESHOLD ('probably'); A BELOW_THRESHOLD; not a scientist, B UNKNOWN; mid_basin BELOW_THRESHOLD. Heritage: practising Reform/Conservative Jewish family (S2). Britannica uses they/them; sex_as_recorded left UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: butler-judith
  display_name: "Judith Butler"
  roster:
    canonical_name: "Judith Butler"
    rank: 196
    F: 3
    models: [DeepSeek, Gemini, GPT]
    band: "core (3–4)"
    status: "provisional"
    field: "philosophy"
    field_bucket: "philosophy"
  full_name: {value: "Judith Pamela Butler", certainty: 0.7, cites: [{source: S1, locator: "At a Glance"}, {source: S6, locator: "infobox / lead"}], how_known: "Britannica quick facts; Wikipedia corroborates."}
  native_name: {value: "Judith Butler", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S6, locator: "title"}], how_known: "Britannica; Wikipedia (P50)."}
  aliases:
    - {name: "Butler-Judith", kind: "roster alias"}
    - {name: "Judith-Butler", kind: "roster alias"}

basics:
  birth:
    date: {value: "1956-02-24", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S6, locator: "Early life and education"}], how_known: "Britannica; Wikipedia (P50)."}
    place: {value: "Cleveland, Ohio", modern_name: "Cleveland, Ohio, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S6, locator: "Early life and education"}], how_known: "Britannica; Wikipedia (P50)."}
  death:
    date: {value: UNKNOWN, how_known: "Living (S1; S6)."}
    place: {value: UNKNOWN, how_known: "Living (S1; S6)."}
  first_lasting_contribution_year: {value: 1990, certainty: 0.7, cites: [{source: S1, locator: "Introduction; Gender Trouble paragraphs"}], how_known: "Gender Trouble: Feminism and the Subversion of Identity (1990) (S1); publication (P30 #1)."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "text"}], how_known: "1990 (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "USA (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Wesleyan, Johns Hopkins, Berkeley."}
  sex_as_recorded: {value: UNKNOWN, how_known: "Britannica uses they/them pronouns (S1); Wikipedia likewise; not recorded as a sex in the sources read."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "English books."}
  occupations: {value: ["philosopher", "cultural theorist", "professor"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

contribution:
  primary_domain: philosophy
  fields: {value: ["philosophy", "gender studies", "queer theory"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Gender Trouble: Feminism and the Subversion of Identity (performative theory of gender)", year: 1990, kind: "work", lasting: "'one of the foundational texts of queer theory'; 'greatly influenced the development of cultural theory, gender studies, and some schools of philosophical feminism' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Introduction; later paragraphs"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "Founding text of queer theory; continued to inform debate in cultural theory", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica (which also reports significant criticism)."}
  major_works:
    - {value: "Bodies That Matter", year: 1993, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    - {value: "Parting Ways: Jewishness and the Critique of Zionism", year: 2012, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founding text of queer theory (S1).", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Judaism (Reform; mother raised Orthodox then Conservative)", certainty: 0.7, cites: [{source: S3, locator: "parents' relation to Judaism"}, {source: S2, locator: "Jewish Life/Roots"}], how_known: "Own voice (S3): parents practicing Jews; mother Orthodox→Conservative→Reform; father Reform from the start."}
  family_religious_practice: {value: "practising — Hebrew school, synagogue, special Jewish-ethics classes", certainty: 0.7, cites: [{source: S3, locator: "Hebrew school; Jewish ethics"}, {source: S2, locator: "Jewish Life/Roots"}], how_known: "Own voice: Hebrew school plus after-school Jewish ethics; continued Jewish studies through high school (S3)."}
  parents_and_household:
    - {value: "Father a dentist; mother a fair-housing advocate; a practising Jewish family", role: "family", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S2, locator: "Jewish Life/Roots"}], how_known: "Britannica; AVIVA (interviewer's question, which Butler answers)."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Hebrew school (Cleveland) plus special after-school classes on Jewish ethics (rabbi tutorial from age 14)", stage: other, run_by: "religious body", certainty: 0.7, cites: [{source: S3, locator: "Hebrew school; tutorial"}, {source: S6, locator: "Early life and education"}], how_known: "Own voice (S3); Wikipedia (P50)."}
    - {value: "Bennington College (transfer)", stage: "university", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S6, locator: "Early life and education"}], how_known: "Britannica; Wikipedia."}
    - {value: "Yale University (BA 1978, PhD 1984); Fulbright year at Heidelberg (1979)", stage: "university", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S6, locator: "Early life and education"}], how_known: "Britannica; Wikipedia."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading:
    - {value: "Existential theology (Martin Buber); questions on Spinoza's excommunication, German Idealism and Nazism", certainty: 0.7, cites: [{source: S3, locator: "tutorial topics"}], how_known: "Own voice: topics chosen for the rabbi's punishment tutorial at 14 (S3)."}
  childhood_mentors:
    - {value: "Hebrew-school rabbi (punishment tutorial at age 14 that became first philosophy training)", role: "tutor", certainty: 0.7, cites: [{source: S3, locator: "You are too talkative in class"}, {source: S6, locator: "Early life and education"}], how_known: "Own voice (S3); Wikipedia."}
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events:
    - {value: "Age-14 synagogue tutorial after being 'too talkative'; chose Spinoza / German Idealism / Buber as topics", year: 1970, certainty: 0.5, cites: [{source: S3, locator: "tutorial"}, {source: S6, locator: "Early life and education"}], how_known: "Own voice; year from age 14 and 1956 birth (approximate)."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1990", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Occasional synagogue attendance (music and singing); Jewish cultural/ethical identity without doctrine profession", certainty: 0.5, cites: [{source: S2, locator: "Jewish Life/Roots"}, {source: S5, locator: "Judaism actively celebrates the patriarchs"}], how_known: "S2: sometimes still attend synagogue; S5: Judaism as 'my own' tradition whose feminist re-readings 'are not my practices'."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "S5 discusses scientific paradigms for sex-assignment as performativity, not a personal science–religion creed."}
  primary_system:
    value: AGNOS
    basis: recorded_interview
    certainty: 0.5
    cites: [{source: S2, locator: "Jewish Life/Roots"}, {source: S3, locator: "no after world / Jewish values"}, {source: S5, locator: "my own [religion]"}]
    how_known: "(interview) Own emailed answers AVIVA-Berlin 2010 (S2) after the span (P20); Haaretz/Aloni 2010 (S3) and Feminism and Religion 2014 (S5) corroborate this-world / cultural Jewishness without theistic profession (P48; primary_system has no support field — certainty still 0.5). 'Probably' hedge + after-span keep certainty 0.5."
    rationale: "AGNOS: 'I am probably an agnostic on religious matters' and 'very sceptical of efforts to define or portray any notion of the divine' (S2). Not ATHE: no stated denial of God's existence. Not JUDA as working code: no doctrine professed; synagogue is music/singing and cultural ethics (S2, S5). Alternative BELOW_THRESHOLD: 'probably' hedges the label."
    alternatives:
      - {value: BELOW_THRESHOLD, note: "'probably an agnostic' hedges; occasional synagogue attendance continues.", cites: [{source: S2, locator: "Jewish Life/Roots"}]}
  secondary_system: {value: UNKNOWN, how_known: "Jewish ethics / precarious-life value (S3) is cultural-ethical, not a second system code."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Coded at 0.5 (S2 own label); S3/S5 corroborate non-theistic working stance."}
    - {code: JUDA, reason: "Lead only: Jewish upbringing, occasional synagogue, 'my own' tradition (S2/S5); no doctrine professed — rejected as primary."}
    - {code: ATHE, reason: "Rejected: no 'I do not believe in God' / atheist self-label; afterlife denial (S3) is C, not ATHE."}
  lio_axes:
    A_locus:
      value: BELOW_THRESHOLD
      how_known: "P20: an agnostic with no stated locus view gets A BELOW_THRESHOLD. S2 sceptical of 'any notion of the divine' is suspension, not explicit denial of a personal intervening God. S3 'no after world' / 'no final redemption' is scored on C_ledger, not A."
    B_cause:
      value: UNKNOWN
      how_known: "Not a scientist (P30: philosopher / cultural theorist). No P16 nature-order own-voice in sources read; S5 sex-determination / scientific-paradigm remarks are about social assignment, not lawful nature."
    C_ledger:
      value: 4
      basis: recorded_interview
      certainty: 0.5
      support: single
      cites: [{source: S3, locator: "because there is no after world"}]
      how_known: "(interview) Haaretz/Aloni 2010, after the span (P20 → 0.5). Own endorsement of a Jewish-formation idea she 'took'."
      rationale: "Explicit denial of afterworld and final redemption as grounds for this-world care: 'because there is no after world, because we don't have any hopes in a final redemption, we have to take especially good care of life in the here and now' (S3). C 4 = impersonal consequence or none. Alternative BELOW_THRESHOLD: framed as a value taken from Jewish formation, not a free-standing metaphysical treatise."
      alternatives:
        - {value: BELOW_THRESHOLD, note: "Framed as Jewish-formation value rather than a standalone creed statement.", cites: [{source: S3, locator: "Jewish values"}]}
    D_authority: {value: UNKNOWN, how_known: "Not read on revelation vs observation."}
    E_scope: {value: UNKNOWN, how_known: "Not read on world's-order scope; afterlife/redemption scored on C (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied."}
  statements:
    - text: "I am very sceptical of efforts to define or portray any notion of the divine. I am probably an agnostic on religious matters, but I do sometimes still attend the synagogue, and the music and singing is profound and moving to me."
      cites: [{source: S2, locator: "Jewish Life/Roots"}]
      date: "2010"
      context: "Emailed answers to AVIVA-Berlin after the 2010 Berlin CSD; after the span."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "newspaper interview"
      verified_on: 2026-10-24
      note: "Stretch of the P21 value, noted on the AA5 audit: these are Butler's own emailed written answers, published by an online magazine, not a journalist's quotation in a newspaper; no further schema value added."
    - text: "The other idea was that life is transient, and because of that, because there is no after world, because we don't have any hopes in a final redemption, we have to take especially good care of life in the here and now. Life has to be protected. It is precarious. I would even go so far as to say that precarious life is, in a way, a Jewish value for me."
      cites: [{source: S3, locator: "Jewish values / no after world"}]
      date: "2010"
      context: "Haaretz interview with Udi Aloni; describing ideas taken from Jewish philosophy and formation; after the span."
      axes: [C_ledger]
      kind: "recorded interview"
      verified_against: "newspaper interview"
      verified_on: 2026-10-24
    - text: "Of course, there are many religions, including my own, that have strong patriarchal bias. Judaism actively celebrates the patriarchs, but many feminists have found ways to re-read or read against the patriarchal grain. … Those are not my practices, but I understand and respect them."
      cites: [{source: S5, locator: "feminist critiques of patriarchal religion"}]
      date: "2014"
      context: "Feminism and Religion interview (Kile Jones); after the span; cultural affiliation without feminist-theology practice."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "newspaper interview"
      verified_on: 2026-10-24
      note: "Supports nominal Jewish affiliation and rejection of JUDA-as-doctrine; does not score A by itself."
  changes_over_life: []
  coder_notes: "Deepen D1: primary AGNOS firmed (support corroborated) but certainty stays 0.5 (P20 after-span + 'probably' hedge). A stays BELOW (P20 agnostic-no-locus). B UNKNOWN (not scientist; no P16). C newly scored 4 @0.5 from S3 afterlife/redemption denial. Son's bar-mitzvah anecdote (S3/CUP: son said he didn't believe in god) is the son's voice — not used for Butler's A. Parting Ways (2012) unread beyond Britannica locator. No fallacy_catalog (Jason)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Jewish (maternal family from Hungary; relatives killed in the Holocaust)", certainty: 0.7, cites: [{source: S3, locator: "mother's uncles and aunts"}, {source: S6, locator: "Early life and education"}], how_known: "Own voice (S3); Wikipedia (P50)."}
  religious_heritage_by_birth: {value: "Jewish (Reform; mother raised Orthodox)", certainty: 0.7, cites: [{source: S2, locator: "Jewish Life/Roots"}, {source: S3, locator: "parents' relation to Judaism"}], how_known: "'My parents were practicing Jews. My mother grew up in an orthodox synagogue and after my grandfather died, she went to a conservative synagogue and a little later ended up in a reform synagogue. My father was in reform synagogues from the beginning' (S3, read in full); AVIVA (S2)."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: "Hebrew school and special Jewish-ethics classes through high school", certainty: 0.7, cites: [{source: S3, locator: "Hebrew school; Jewish ethics"}], how_known: "Own voice (S3)."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1990", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "The one listed lasting work (P29, P30 #1)."}
  age_at_first_lasting_contribution: {value: 34, certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "1990 − 1956 = 34 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: "2010 (after the span): AVIVA agnostic self-label; Haaretz no-afterworld Jewish-value line", certainty: 0.5, cites: [{source: S2, locator: "Jewish Life/Roots"}, {source: S3, locator: "no after world"}], how_known: "Both interviews after Gender Trouble (P20)."}
  lio_views_relative_to_major_work: {value: "after major work", certainty: 0.5, cites: [{source: S2, locator: "2010"}, {source: S3, locator: "2010"}], how_known: "Creed statements 2010; lasting work 1990."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "No in-span creed statement; adult AGNOS/C rest on after-span interviews (P20). No change_over_life documented (P31 continuity assumed, not scored into the span)."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Critical theory / queer theory (S1); no geometric nature-order program.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "Living philosopher/theorist; AGNOS working label after the span; not plotted (A BELOW, B UNKNOWN)."
  notes: "Lane B only. Do not treat synagogue attendance or Jewish ethics as a theistic plot cue."

institutions:
  - {value: "University of California, Berkeley", role: "Maxine Elliot Professor of Rhetoric and Comparative Literature", years: "1998", kind: "university", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica: appointed 1998."}
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 196"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Profession after the span; online-magazine interview (S2) and newspaper interviews (S3, S5)."
    - "A BELOW_THRESHOLD by P20 (agnostic, no locus denial); chart cannot plot without A."
  open_questions:
    - "P21 label for an online magazine's written interview (S2)."
    - "In-span or near-span own-voice creed that would lift AGNOS past P20 0.5 (unlikely given 'probably' hedge)."
    - "Parting Ways (2012) print for fuller Jewish-ethics metaphysics (unread beyond Britannica)."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Brian Duignan"
    citation: "Duignan, Brian. 'Judith Butler.' Encyclopaedia Britannica. https://www.britannica.com/biography/Judith-Butler"
    url: "https://www.britannica.com/biography/Judith-Butler"
    accessed: 2026-10-19
    reliability_note: "Signed article, read in full."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, timing, institutions]
  - id: S2
    type: primary
    kind: "other"
    author: "Judith Butler, interviewed by AVIVA-Berlin"
    citation: "'AVIVA-Interview with Judith Butler.' AVIVA-Berlin (2010). https://www.aviva-berlin.de/aviva/content_Interviews.php?id=1427323"
    url: "https://www.aviva-berlin.de/aviva/content_Interviews.php?id=1427323"
    accessed: 2026-10-24
    reliability_note: "Her emailed answers as published by the online magazine, read in full (deepen re-read)."
    source_quality: "newspaper interview"
    used_for: [childhood, worldview, heritage]
  - id: S3
    type: primary
    kind: "other"
    author: "Judith Butler, interviewed by Udi Aloni"
    citation: "Aloni, Udi. 'Judith Butler: As a Jew, I was taught it was ethically imperative to speak up.' Haaretz, 24 February 2010. Internet Archive copy. https://web.archive.org/web/20100227081749/http://www.haaretz.com/hasen/spages/1152017.html"
    url: "https://web.archive.org/web/20100227081749/http://www.haaretz.com/hasen/spages/1152017.html"
    accessed: 2026-10-24
    reliability_note: "Newspaper interview, archived copy re-read in full on deepen; same Aloni conversation excerpted on CUP blog 2012."
    source_quality: "newspaper interview"
    used_for: [heritage, worldview, childhood]
  - id: S4
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [review]
  - id: S5
    type: primary
    kind: "other"
    author: "Judith Butler, interviewed by Kile Jones"
    citation: "Jones, Kile. 'Sex, Religion, and Discourse: An Interview with Judith Butler.' Feminism and Religion, 19 February 2014. https://feminismandreligion.com/2014/02/19/sex-religion-and-discourse-an-interview-with-judith-butler/"
    url: "https://feminismandreligion.com/2014/02/19/sex-religion-and-discourse-an-interview-with-judith-butler/"
    accessed: 2026-10-24
    reliability_note: "Published Q&A; after the span; Judaism as 'my own' without feminist re-reading practice; science/sex-assignment remarks not P16."
    source_quality: "newspaper interview"
    used_for: [worldview]
  - id: S6
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "'Judith Butler.' Wikipedia (English). Accessed via MediaWiki API / page text, 24 October 2026."
    url: "https://en.wikipedia.org/wiki/Judith_Butler"
    accessed: 2026-10-24
    reliability_note: "Dual bio (P50) for birth date/place, early education, Hebrew-school tutorial; not used alone for A/B."
    source_quality: "reference entry"
    used_for: [identity, basics, childhood, heritage]
---

## Summary

Judith Butler (b. 1956), philosopher and gender theorist [S1; S6]. Deepen D1: primary_system AGNOS (0.5, alt BELOW_THRESHOLD; support corroborated); A BELOW_THRESHOLD; B UNKNOWN; C 4 (0.5, alt BELOW); mid_basin BELOW_THRESHOLD. Not plotted. Chart-moving NO.

## Life and work

Born Cleveland, Ohio, 24 February 1956 [S1; S6]. Hebrew school and Jewish-ethics tutorial from age 14 [S3; S6]. Bennington; Yale BA 1978 / PhD 1984; Heidelberg Fulbright 1979 [S1; S6]. Taught Wesleyan, Johns Hopkins; Maxine Elliot Professor, UC Berkeley from 1998 [S1]. Living.

## Contribution and impact

*Gender Trouble* (1990): foundational queer-theory text; performative theory of gender [S1]. Later *Bodies That Matter* (1993), *Parting Ways* (2012) [S1]. Span = 1990 (one lasting contribution listed).

## Childhood and education

Practising Reform/Conservative Jewish household; father dentist, mother fair-housing advocate [S1; S2; S3]. Hebrew school plus special ethics classes; rabbi tutorial on Spinoza, German Idealism, Buber [S3; S6].

## Adult working worldview

Own voice after the span (P20): 'probably an agnostic' and sceptical of any notion of the divine [S2]; occasional synagogue for music [S2]; Judaism 'my own' but feminist biblical re-readings 'not my practices' [S5]; 'no after world' / 'no hopes in a final redemption' as a Jewish value grounding this-world care [S3]. Coded AGNOS @0.5; A BELOW; B UNKNOWN; C 4 @0.5.

## Heritage (context only)

Jewish by birth (Reform; mother raised Orthodox); maternal Hungarian relatives killed in the Holocaust [S3; S6]. Heritage is not a worldview code.

## Timing

First lasting contribution 1990, age 34 [S1]. Creed evidence 2010–2014, after the span [S2; S3; S5].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Theorist, not scientist; no geometric nature-order program scored. Not plotted.

## Open questions

- P21 label for S2 online-magazine written answers.
- In-span creed (unlikely to lift past P20 given 'probably').
- *Parting Ways* print unread beyond Britannica.

## Research log

- 2026-10-24: Deepen D1. Re-read AVIVA (S2) and Haaretz/Aloni (S3); opened Feminism and Religion (S5) and Wikipedia (S6, P50). CUP Aloni blog = same conversation as S3. Firm AGNOS/A under P20; score C 4 @0.5; B UNKNOWN. Chart NO. No fallacy_catalog; no figures/.
- 2026-10-19: AA5 audit fix (v8's call on the auditor's advice): the 'newspaper interview' label is kept with a note that these are her own emailed answers to an online magazine; Haaretz 2010 interview (Aloni) read in full and added as S3; heritage raised to 0.7.
- 2026-10-19: Read Britannica (Duignan); AVIVA interview.
