---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z7; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 20c_early. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (skip catch-up 8/13; F3 rank 161). Needs: firm A/primary if primary sources allow; prefer memoir/interviews over secondary; Sacred Concerts are work not profession; not scientist for B; do not force plot. Music Is My Mistress still borrow-only on IA (unread). Opened Guideposts Feb 1971 essay by Ellington (S3); 1965 First Sacred Concert program note via Tucker Duke Ellington Reader (S4); Les Tomkins interview 1 Dec 1973 / Crescendo Jan 1974 (S5); Wikipedia EN dual bio (S6, P50). primary_system UNKNOWN → CHRIST @0.5 (written_profession): Guideposts own prayer/Bible/dependence-on-God profession; program note 'God has total understanding' / 'Every man prays…'; interview affirms Lord's Prayer settings and rejects 'God is dead'. No adult denomination stated (parents Methodist/Baptist) — still CHRIST under v8 Christian-belief note, not a church-membership test. A_locus UNKNOWN → 0 @0.5 alt 1 (transcendent personal God who hears prayer; after span). B_cause stays UNKNOWN → BELOW_THRESHOLD (not scientist; petitionary prayer / communication 'miracles' are not P16 nature-order — Austen RQ-AU1; Sacred Concerts work not B). mid_basin UNKNOWN → BELOW_THRESHOLD. Chart-moving NO. Childhood religion from Guideposts. P47 source_quality on S1–S6. No fallacy_catalog. No figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z7, order P32: F 3, rank 161). Basics from Britannica (body). His words on God (Music Is My Mistress, 1973, pp. 262, 267–269: 'Every man prays in his own language, and there is no language that God does not understand'; 'Now I can say openly what I have been saying to myself on my knees') were seen only as quoted on secondary pages; the archive.org scans are borrow-only and were not read. Second-hand quotations alone (V3), so primary_system UNKNOWN (lead CHRIST); A, B, C, D, E UNKNOWN; mid_basin UNKNOWN. Not a scientist. Span 1926–1943. Not plotted. Draft, not reviewed."}

identity:
  id: ellington-duke
  display_name: "Duke Ellington"
  roster:
    canonical_name: "Duke Ellington"
    rank: 161
    F: 3
    models: [Claude, Gemini, GPT]
    band: "core (3–4)"
    status: "review"
    field: "music"
    field_bucket: "music"
  full_name: {value: "Edward Kennedy Ellington", certainty: 0.7, cites: [{source: S1, locator: "Also known as"}, {source: S6, locator: "lede"}], how_known: "Britannica; Wikipedia."}
  native_name: {value: "Duke Ellington", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "lede"}], how_known: "English name used in sources; nickname Duke from childhood (Britannica/Wikipedia)."}
  aliases:
    - {name: "Edward Kennedy Ellington", kind: "birth name"}
    - {name: "Duke-Ellington", kind: "roster alias"}

basics:
  birth:
    date: {value: "1899-04-29", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "lede"}], how_known: "Britannica; Wikipedia."}
    place: {value: "Washington, D.C.", modern_name: "Washington, D.C., United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "lede"}], how_known: "Britannica; Wikipedia."}
  death:
    date: {value: "1974-05-24", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "lede"}], how_known: "Britannica; Wikipedia."}
    place: {value: "New York City", modern_name: "New York, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "lede"}], how_known: "Britannica; Wikipedia."}
  first_lasting_contribution_year: {value: 1926, certainty: 0.7, cites: [{source: S1, locator: "Ellington's ensemble"}], how_known: "'East St. Louis Toodle-oo' (1926), named among the 'masterpieces' of his early style."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "Ellington's ensemble"}], how_known: "1926 (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "USA (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "Ellington's ensemble"}], how_known: "New York; wide touring."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Inferred."}
  occupations: {value: ["pianist", "composer", "bandleader"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  era_bucket: 20c_early
  fields: {value: ["jazz", "big-band jazz"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "'East St. Louis Toodle-oo' and 'Black and Tan Fantasy' (jungle style)", year: 1926, kind: "work", lasting: "'masterpieces' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Ellington's ensemble"}], how_known: "Britannica: 1926, 1927."}
    - {value: "Black, Brown and Beige", year: 1943, kind: "work", lasting: "first in a series of suites (S1)", certainty: 0.5, cites: [{source: S1, locator: "Classical forms"}], how_known: "Britannica; lastingness the coder's call, so the span end is 0.5."}
  evidence_of_impact:
    - {value: "The greatest jazz composer and bandleader of his time", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Mood Indigo", year: 1930, kind: "composition", certainty: 0.7, cites: [{source: S1, locator: "Ellington's ensemble"}], how_known: "Britannica."}
    - {value: "Sacred Concerts (three)", year: 1973, kind: "composition", certainty: 0.7, cites: [{source: S1, locator: "Classical forms"}], how_known: "Britannica: 1965, 1968, 1973. Work, not a worldview profession (Sacred Concerts alone do not score CHRIST/A)."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Greatest jazz composer of his time (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Methodist (father) and Baptist (mother)", certainty: 0.5, cites: [{source: S3, locator: "two churches / Sunday paragraph"}], how_known: "(published essay) Guideposts 1971: every Sunday father's Methodist church then mother's Baptist church."}
  family_religious_practice: {value: "Regular Sunday church attendance at both parents' churches", certainty: 0.5, cites: [{source: S3, locator: "two churches paragraph"}], how_known: "Guideposts."}
  parents_and_household:
    - {value: "Father a caterer / later Navy Department blueprint technician; mother played piano; secure household", certainty: 0.5, cites: [{source: S3, locator: "parents paragraphs"}, {source: S1, locator: "Early life and career"}], how_known: "Guideposts; Britannica middle-class note."}
  household_circumstances: {value: "Secure middle-class family in Washington, D.C.", certainty: 0.7, cites: [{source: S1, locator: "Early life and career"}], how_known: "Britannica."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading:
    - {value: "Bible (read through multiple times in adulthood after parents' deaths; childhood Sunday school noted by biographer Jewell only — not used as primary)", certainty: 0.5, cites: [{source: S3, locator: "Bible / four times"}], how_known: "Guideposts own-voice on adult rereading."}
  childhood_mentors: []
  languages_in_childhood: {value: ["English"], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Inferred."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1926–1943", certainty: 0.5, cites: [{source: S1, locator: "Ellington's ensemble; Classical forms"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing on science vs religion as such; music framed as worship (S3)."}
  primary_system:
    value: CHRIST
    basis: written_profession
    certainty: 0.5
    cites: [{source: S3, locator: "prayer / dependence / on my knees / act of worship"}, {source: S4, locator: "God has total understanding; Every man prays…"}, {source: S5, locator: "Lord's Prayer settings; God is dead lyric"}]
    rationale: "Own published Guideposts essay (Feb 1971, S3): regular petitionary prayer; total dependence on God; Bible and Ten Commandments as way of life; Sacred Concert music 'an act of worship' and 'an expression of God in my life'; 'saying in music what I have been saying on my knees for a long time.' 1965 First Sacred Concert program note (S4, via Tucker): God blesses timing; 'One and only One has all the wisdom'; 'Every man prays in his own language…'; Bible theme 'In the beginning God.' Tomkins interview Dec 1973 (S5): affirms Lord's Prayer settings and the lyric that mentioning God eliminates 'is dead.' Sacred Concerts themselves remain work, not the profession (brief / prior create). No adult denominational membership stated (childhood Methodist/Baptist only) — CHRIST does not require a named church. After major-work span 1926–1943 (P20) → 0.5. Support corroborated (P48): essay, program note, and interview agree on personal Christian theism / prayer."
    how_known: "(published essay + program note + interview) Guideposts by Ellington (S3); Tucker reprint of 1965 program note (S4); Tomkins/Crescendo interview (S5). Music Is My Mistress still unread first-hand (IA borrow-only); overlapping 'on my knees' / 'every man prays' lines appear in Guideposts and the program note, so memoir V3 quotes are not needed to score."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Chosen: Guideposts prayer/Bible/worship profession (S3); program note and interview (S4, S5)."}
    - {code: CLTHEI, reason: "Named alternative only: personal intervening God fits classical theism; not chosen as primary because the profession is Christian (Bible, Lord's Prayer, church Sacred Concerts), not bare philosophical theism."}
    - {code: DEISM, reason: "Rejected: regular petitionary prayer and dependence contradict a non-intervening God."}
    - {code: AGNOS, reason: "Rejected: no suspension; explicit profession."}
  lio_axes:
    A_locus:
      value: 0
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S3, locator: "prayer / total dependence / accountable to Him"}, {source: S4, locator: "One and only One; God has total understanding; Thank God"}]
      rationale: "Transcendent personal God outside the self/world who hears prayer, to whom one is accountable, who blesses timing and has 'total understanding' (S3, S4). Not identified with the world. Named alternative 1: nothing states 'outside the world' as a metaphysical thesis beyond personal transcendence / One-and-only-One language. After span → 0.5."
      how_known: "(published essay + program note) Guideposts (S3) and 1965 program note (S4); interview S5 corroborates Christian prayer language. After major-work span (P20)."
      alternatives:
        - {value: 1, note: "If 'One and only One' / prayer God is read as personal without a clear transcendent-outside-world claim.", cites: [{source: S4, locator: "One and only One has all the wisdom"}]}
    B_cause:
      value: BELOW_THRESHOLD
      cites: [{source: S3, locator: "I pray regularly… dependence on Him"}, {source: S4, locator: "miracles have happened (honesty/communication); God has blessed my timing"}]
      how_known: "Not a scientist (P30; musician). No P16 statement about the lawful order of nature. Own petitionary prayer and 'miracles have happened' about honest communication (S4) are not statements about nature (RQ-AU1 / P16 Austen addendum) → BELOW_THRESHOLD. Sacred Concerts are compositions (work), not a B score. Named reading 1 at 0.5 (answered petition within a created order) not adopted under RQ-AU1."
      note: "Named reading 1 @0.5 rejected under RQ-AU1; communication-miracles line is not physical-nature order."
    C_ledger: {value: BELOW_THRESHOLD, how_known: "Guideposts: accountable to God at end of life's 'lease'; sin to grieve past a point; Ten Commandments as way of life (S3). Suggests personal moral accounting but too thin for a scored C without a clearer reward/punishment claim (P19)."}
    D_authority: {value: UNKNOWN, how_known: "Bible and Ten Commandments valued (S3); nothing comparing revelation to observation/reason."}
    E_scope: {value: UNKNOWN, how_known: "'Every man prays in his own language' (S3/S4) is about prayer/worship accessibility, not the world's causal order (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is 0 only at 0.5 and B_cause is BELOW_THRESHOLD, under the P4 0.7 bar (P19). Not plotted."}
  statements:
    - text: "One sure way I know to meet my problems is prayer. I pray regularly, when I arise, when I retire. I pray my thanks for whatever He gives me: a thought, a bar of music, food. I believe I am helped by prayer. It makes me aware of my total dependence on Him."
      cites: [{source: S3, locator: "prayer paragraph"}]
      date: "1971-02"
      context: "Guideposts essay by Duke Ellington (Feb 1971)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Used for CHRIST and A 0; petition language supports B BELOW under RQ-AU1, not a nature-order score."
    - text: "It continues to be an expression of God in my life. I am only saying in music what I have been saying on my knees for a long time."
      cites: [{source: S3, locator: "closing paragraph"}]
      date: "1971-02"
      context: "Guideposts; on the Sacred Concerts as worship (not a substitute for ordinary worship)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
    - text: "Wisdom is something that man partially enjoys—One and only One has all the wisdom. God has total understanding. There are some people who speak one language and some who speak many languages. Every man prays in his own language, and there is no language that God does not understand."
      cites: [{source: S4, locator: "Tucker Reader pp. 371–2"}]
      date: "1965-09"
      context: "Ellington's program note for the First Sacred Concert, Grace Cathedral, San Francisco (16 Sept 1965); reprinted in The Duke Ellington Reader, ed. Mark Tucker."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Scholarly anthology reprint of his program note; treated as his published words (primary type). Overlaps Guideposts 'every man prays' line."
    - text: "Yet, every time God's children have thrown away fear in pursuit of honesty—trying to communicate themselves, understood or not—miracles have happened. … I know that God has blessed my timing, without which no thing could have happened… Thank God…"
      cites: [{source: S4, locator: "Tucker Reader pp. 371–2"}]
      date: "1965-09"
      context: "Same First Sacred Concert program note."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "'Miracles' here about honest communication, not a P16 nature-order claim; used for A/CHRIST context and B BELOW rationale."
    - text: "…one of the songs is: 'Every Man Prays In His Own Language, And There's No Language God Does Not Understand.' So… we did the Lord's Prayer—six different versions of our own. … The silliest thing I ever read was that somebody said: 'God is dead'. And the mere mention of the first word automatically eliminates the second and the third."
      cites: [{source: S5, locator: "On sacred music / Westminster / Something About Believing"}]
      date: "1973-12-01"
      context: "Interview by Les Tomkins, Congress Theatre Eastbourne; published Crescendo, January 1974."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
    - text: "My parents loved us, fed us, cleaned us, took us to church. Two churches. Every Sunday we first went to my father's church, Methodist. Then my mother took us to her church, Baptist."
      cites: [{source: S3, locator: "two churches paragraph"}]
      date: "1971-02"
      context: "Guideposts essay; childhood religion."
      axes: []
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Childhood heritage; not adult primary_system by itself."
  changes_over_life: []
  coder_notes: "Music Is My Mistress (1973) still IA borrow-only — unread. Guideposts + program note cover the famous 'knees' / 'every man prays' lines. Sacred Concerts = work. Not scientist. Chart needs A&B ≥0.7; A 0@0.5 and B BELOW → unplotted."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "African American", certainty: 0.7, cites: [{source: S1, locator: "Classical forms"}, {source: S6, locator: "Black, Brown and Beige"}], how_known: "Britannica; Wikipedia."}
  religious_heritage_by_birth: {value: "Methodist (father) and Baptist (mother)", certainty: 0.5, cites: [{source: S3, locator: "two churches"}], how_known: "Guideposts."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Sunday school mentioned only in secondary Jewell (via Princeton page); not used without first-hand."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1926–1943", certainty: 0.5, cites: [{source: S1, locator: "Ellington's ensemble; Classical forms"}], how_known: "East St. Louis Toodle-oo (1926) to Black, Brown and Beige (1943) (P29, P30); end is the coder's call."}
  age_at_first_lasting_contribution: {value: 27, certainty: 0.7, cites: [{source: S1, locator: "opening; Ellington's ensemble"}], how_known: "1926 − 1899 = 27 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: "1965: First Sacred Concert program note (A/CHRIST); 1971 Guideposts essay", year: 1965, certainty: 0.5, cites: [{source: S4, locator: "program note"}, {source: S3, locator: "Guideposts"}], how_known: "First scored own-voice LIO evidence is 1965 program note; Guideposts says sacred music began earlier 'inside me' but that is retrospective, not a dated score."}
  lio_views_relative_to_major_work: {value: "after major work", certainty: 0.5, cites: [{source: S4, locator: "1965"}, {source: S3, locator: "1971"}, {source: S5, locator: "1973"}], how_known: "Scored sources after span end 1943 (P20)."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "No contemporaneous 1926–1943 creed source read; Come Sunday (in BBB 1943) is work, not profession."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Music (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "CHRIST @0.5; A 0 @0.5; B BELOW (no P16 nature remark). Not plotted."
  notes: "Lane B labeled belief only."

institutions: []
collaborators:
  - {value: "Billy Strayhorn", relation: "collaborator", note: "composing-arranging partner 1939–67", certainty: 0.7, cites: [{source: S1, locator: "Legacy"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Review in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 161"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Music Is My Mistress still unread first-hand (IA print-disabled / borrow-only)."
    - "Program note verified via Tucker anthology reprint (scholarly secondary carrier of primary text)."
    - "A and primary after major-work span → 0.5."
  open_questions:
    - "Borrow/read Music Is My Mistress pp. ~259–270 for memoir wording and any during-span leads."
    - "Any 1920s–1940s own-voice creed statement that could lift certainty past after-span 0.5."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "'Duke Ellington.' Encyclopaedia Britannica (rev. 2026). https://www.britannica.com/biography/Duke-Ellington"
    url: "https://www.britannica.com/biography/Duke-Ellington"
    accessed: 2026-10-19
    reliability_note: "Unsigned editorial article; body cited, not the question boxes (P26)."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, heritage, timing, lane_b, collaborators]
  - id: S2
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [review]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Duke Ellington"
    citation: "Ellington, Duke. \"Guideposts Classics: Duke Ellington on His Path of Prayer.\" Guideposts, February 1971. https://guideposts.org/articles/prayer/true-stories-of-answered-prayer/guideposts-classics-duke-ellington-on-his-path-of/. Read 2026-10-24."
    url: "https://guideposts.org/articles/prayer/true-stories-of-answered-prayer/guideposts-classics-duke-ellington-on-his-path-of/"
    accessed: 2026-10-24
    reliability_note: "Byline Duke Ellington; Guideposts presents as his Feb 1971 essay. First-person profession of prayer and Sacred Concert worship. Used for CHRIST, A, childhood religion."
    source_quality: "primary / own words"
    used_for: [worldview, childhood, heritage, timing]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Duke Ellington (program note; reprinted in Tucker)"
    citation: "Ellington, Duke. Program note for the First Sacred Concert (Grace Cathedral, San Francisco, 16 September 1965). Reprinted in Mark Tucker, ed., The Duke Ellington Reader (Oxford University Press, 1993), pp. 371–372. Text also hosted at https://music2.princeton.edu/jeffery/ellington.html. Read 2026-10-24."
    url: "https://music2.princeton.edu/jeffery/ellington.html"
    accessed: 2026-10-24
    reliability_note: "His 1965 program note; read via scholarly reprint / course page quoting Tucker. Treated as primary words; carrier is secondary."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, timing]
  - id: S5
    type: primary
    kind: other
    author: "Duke Ellington (interviewed by Les Tomkins)"
    citation: "Tomkins, Les. Interview with Duke Ellington, 1 December 1973, Congress Theatre Eastbourne. Published Crescendo, January 1974, pp. 6–7. Transcript: National Jazz Archive, https://nationaljazzarchive.org.uk/explore/interviews/1622007-duke-ellington-interview-2. Read 2026-10-24."
    url: "https://nationaljazzarchive.org.uk/explore/interviews/1622007-duke-ellington-interview-2"
    accessed: 2026-10-24
    reliability_note: "Recorded/published interview transcript; Ellington first-person on Sacred Concerts, Lord's Prayer, 'God is dead' lyric."
    source_quality: "newspaper interview"
    used_for: [worldview, timing]
  - id: S6
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Duke Ellington.\" https://en.wikipedia.org/wiki/Duke_Ellington. Read via API extract 2026-10-24."
    url: "https://en.wikipedia.org/wiki/Duke_Ellington"
    accessed: 2026-10-24
    reliability_note: "Dual-bio second source (P50) for dates/places; notes Sacred Concerts / jazz Christian liturgy; no adult creed article."
    source_quality: "reference entry"
    used_for: [identity, basics, heritage, review]
---

## Summary

Duke Ellington (1899–1974), jazz composer and bandleader [S1]. Deepen D1: primary CHRIST @0.5 (Guideposts 1971; 1965 program note; 1973 interview); A 0 @0.5 alt 1; B BELOW_THRESHOLD (not scientist; petition ≠ P16 nature). Mid BELOW. Not plotted.

## Life and work

Washington, New York, world tours [S1]. Three Sacred Concerts (1965–1973) [S1].

## Contribution and impact

Jungle-style masterpieces; Mood Indigo; Black, Brown and Beige; Sacred Concerts [S1].

## Childhood and education

Secure middle-class Washington family [S1]. Methodist father and Baptist mother; both churches every Sunday [S3].

## Adult working worldview

Guideposts (1971): regular prayer, dependence on God, Bible, Sacred music as worship / words on his knees [S3]. 1965 program note: God has total understanding; every man prays in his own language [S4]. 1973 interview: Lord's Prayer settings; rejects "God is dead" [S5]. Sacred Concerts remain work, not the profession score alone. Music Is My Mistress still unread first-hand.

## Heritage (context only)

African American [S1, S6]; Methodist/Baptist childhood [S3].

## Timing

1926–1943, age 27 [S1]. Scored LIO evidence after span (1965–1973).

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. CHRIST and A after-span at 0.5; B BELOW; not plotted.

## Open questions

- Music Is My Mistress first-hand (IA borrow).
- Any during-span own-voice creed for certainty lift.

## Research log

- 2026-10-19: Read Britannica; memoir quotes only second-hand.
- 2026-10-24: Deepen D1. Guideposts 1971; Tucker program note; Tomkins interview; Wikipedia. IA Mistress still blocked. Wrote drafts/deepen_ellington-duke.md (untracked). No figures. No fallacy_catalog.
