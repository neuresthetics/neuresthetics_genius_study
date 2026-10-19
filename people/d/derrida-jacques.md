---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch R)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-18
  last_updated: 2026-10-18
  change_log:
    - {date: 2026-10-18, by: "Grok Bot", summary: "Record created (stage 3 batch R, order P32: F 4, rank 103). Basics from Britannica (Britannica Editors, unsigned; body read live). Worldview from 'Circumfession' (1991; English in Bennington and Derrida, Jacques Derrida, 1993) as quoted by Elisabeth Loevlie, Religions 4 (2013), with the 2002 exchange with John Caputo as she reports it; secondary quotations. Not a scientist (P30). primary_system and A BELOW_THRESHOLD ('I quite rightly pass for an atheist', with God 'called by other names'); B UNKNOWN (P16); mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-18, by: "Grok Bot", summary: "Batch R audit fixes (gs_0454445_R run 1). Alternative span end is now 1967, not 1974: Glas is listed under major_works, not as a lasting contribution, so it cannot set the end (P13, P30 addendum b; DE5). Specters of Marx now cites Loevlie §1 for its lasting status ('hauntology, first coined in his Spectres of Marx in 1993 [...] a fruitful critical topos'), so the item rises from 0.5 to 0.7 (one source); the span stays 1967–1993 at 0.5."}

identity:
  id: derrida-jacques
  display_name: "Jacques Derrida"
  roster:
    canonical_name: "Jacques Derrida"
    rank: 103
    F: 4
    models: [Claude, DeepSeek, Gemini, Grok]
    band: "core (3–4)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Jacques Derrida", certainty: 0.7, cites: [{source: S1, locator: "title; header ('Also known as: Jackie Derrida')"}], how_known: "Britannica title; the header line also gives 'Jackie Derrida'."}
  native_name: {value: UNKNOWN, how_known: "French; same as the display name."}
  aliases:
    - {name: "Derrida-Jacques", kind: "roster alias"}
    - {name: "Jackie Derrida", kind: other}

basics:
  birth:
    date: {value: "1930-07-15", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica body."}
    place: {value: "El Biar, Algeria", modern_name: "El Biar, Algeria", polity_then: "French Algeria", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Life and work'"}], how_known: "Britannica ('French-governed Algeria')."}
  death:
    date: {value: "2004-10-08", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica body."}
    place: {value: "Paris, France", modern_name: "Paris, France", polity_then: "France", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1967, certainty: 0.7, cites: [{source: S1, locator: "'Life and work' (three books published in 1967)"}], how_known: "Writing and Difference, Of Grammatology and Speech and Phenomena, all 1967 (S1), the earliest works the body names (P17)."}
  era_bucket: {value: "1950 on", certainty: 0.7, cites: [{source: S1, locator: "'Life and work'"}], how_known: "1967 (P2)."}
  region_of_birth: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Algeria (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "'Life and work'"}], how_known: "Paris (Sorbonne, ENS, EHESS); he also taught at Yale and UC Irvine (S1)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["French"], certainty: 0.7, cites: [{source: S1, locator: "titles"}], how_known: "Britannica gives the French titles."}
  occupations: {value: ["philosopher", "university teacher of philosophy"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Life and work'"}], how_known: "Britannica."}

contribution:
  fields: {value: ["philosophy", "literary theory"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Life and work'"}], how_known: "Britannica (critique of Western philosophy; analyses of language, writing and meaning; later work on literature)."}
  lasting_original_contributions:
    - {value: "Deconstruction and différance, set out in Writing and Difference, Of Grammatology and Speech and Phenomena", year: 1967, kind: "concept or term", lasting: "'the principal exponent of deconstruction, a term he coined'; his analyses were 'highly controversial yet immensely influential' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Life and work'"}], how_known: "Britannica; the three books dated 1967."}
    - {value: "Specters of Marx (Spectres de Marx), on the legacy of Marxism; coins 'hauntology'", year: 1993, kind: work, lasting: "named among the 'notably' later works (S1); 'Derrida's term hauntology, first coined in his Spectres of Marx in 1993 [...] The term has proven itself a fruitful critical topos' (S2, §1)", certainty: 0.7, cites: [{source: S1, locator: "'Life and work' (later period)"}, {source: S2, locator: "§1 (Introduction)"}], how_known: "Britannica names the work; Loevlie (S2, §1) says the term it coined has proven 'a fruitful critical topos', so its lasting status rests on a source, not only on the coder's reading of 'notably' (R audit fix, DE5 note). One source for the lasting claim, so 0.7. The latest listed lasting contribution (P30 addendum b)."}
  evidence_of_impact:
    - {value: "International celebrity 'comparable only to that of Jean-Paul Sartre a generation earlier'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "'Life and work'"}], how_known: "Britannica."}
  major_works:
    - {value: "Dissemination (La Dissémination) and Margins of Philosophy (Marges de la philosophie)", year: 1972, kind: book, certainty: 0.7, cites: [{source: S1, locator: "'Life and work'"}], how_known: "Britannica."}
    - {value: "Glas", year: 1974, kind: book, certainty: 0.7, cites: [{source: S1, locator: "'Life and work'"}], how_known: "Britannica."}
    - {value: "'Circumfession'", year: 1991, kind: book, certainty: 0.7, cites: [{source: S1, locator: "'Life and work' (last sentence)"}, {source: S2, locator: "§2"}], how_known: "Britannica calls it autobiographical; published in Bennington's Jacques Derrida (S2)."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Sephardic Jewish", certainty: 0.7, cites: [{source: S1, locator: "'Life and work'"}], how_known: "'born to Sephardic Jewish parents' (S1)."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Sephardic Jewish parents in French-governed Algeria", role: parents, certainty: 0.7, cites: [{source: S1, locator: "'Life and work'"}], how_known: "Britannica."}
  household_circumstances: {value: TODO}
  schooling:
    - {value: "École Normale Supérieure, Paris", stage: university, years: "1949–", certainty: 0.5, cites: [{source: S1, locator: "'Life and work'"}], how_known: "Britannica: went to France in 1949 and studied at the ENS; entry and end years not given (the coder uses 1949 as the start)."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["French"], certainty: 0.5, cites: [{source: S1, locator: "'Life and work' ('Educated in the French tradition')"}], how_known: "Coder's reading."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1967–1993", certainty: 0.5, cites: [{source: S1, locator: "'Life and work'"}, {source: S2, locator: "§1 (Introduction)"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read on science and religion."}
  primary_system: {value: BELOW_THRESHOLD, cites: [{source: S2, locator: "§2 (quoting 'Circumfession', p. 155)"}], how_known: "His published self-description is hedged: 'the constancy of God in my life is called by other names so that I quite rightly pass for an atheist' ('Circumfession', 1991, inside the working years). He says he 'passes for' an atheist while keeping 'God' under other names, and in 2002 (as Loevlie reports the exchange with Caputo) he called the bold claims 'I am a believer' and 'I am an atheist' ridiculous. No code fits clearly; candidates ATHE and AGNOS; JUDA is heritage only. Secondary quotation (P26)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: ATHE, reason: "'I quite rightly pass for an atheist' (1991), hedged by 'pass for' and by God 'called by other names'."}
    - {code: AGNOS, reason: "Lead: he rejects both 'I am a believer' and 'I am an atheist' (2002, as reported)."}
    - {code: JUDA, reason: "Heritage (S1); 'the question of Jewishness and the Jewish tradition' in Shibboleth and 'Circumfession' (S1) is a topic, not a stated belief."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, cites: [{source: S2, locator: "§2"}], how_known: "The one self-statement read places God nowhere: God's 'constancy' in his life is 'called by other names', and he 'quite rightly' passes for an atheist. That is neither a stated disbelief (A 4, P38) nor a locus; the 2002 remarks as reported (God 'has no essence, no presence, no substance', in Loevlie's paraphrase) are a reading of the word 'God', not a placing. Too hedged to score (P19, P38 by analogy)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); no statement of his on nature or the physical world was read, so B is not scored (P16)."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "B is UNKNOWN, which takes precedence (P19); A is BELOW_THRESHOLD."}
  statements:
    - text: "she must have known that the constancy of God in my life is called by other names so that I quite rightly pass for an atheist"
      cites: [{source: S2, locator: "§2, quoting 'Circumfession', p. 155"}, {source: S4, locator: "note 1, quoting 'Circumfession', pp. 154–55"}]
      date: "1991"
      context: "'Circumfession: Fifty-nine Periods and Periphrases', published in French in 1991 and in English in Geoffrey Bennington and Jacques Derrida, Jacques Derrida (Chicago, 1993), p. 155, as quoted by Loevlie (S2). Referring to his mother. Stanley (S4), quoting pp. 154–55, has a comma after 'names' and a longer context ('My religion about which nobody knows anything ... the omnipresence to me of what I call God in my absolved absolutely private language'); Loevlie, and Stanley's own body text, give the first phrase as 'my religion about which nobody understands anything' (p. 154). The wording of the quoted sentence is the same in both apart from the comma."
      axes: [A_locus]
      kind: autobiography
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "Published autobiographical text (written profession, P28). Print check pending (Chicago 1993, pp. 154–55)."
    - text: "True believers know they run the risk of being radical atheists"
      cites: [{source: S2, locator: "§2, quoting Sherwood and Hart, eds., Derrida and Religion (2005), p. 46"}]
      date: "2002"
      context: "Derrida's answer to John Caputo's question 'Why do you say that you rightly pass for an atheist ...?' at a 2002 conference in Canada, printed in Yvonne Sherwood and Kevin Hart, eds., Derrida and Religion: Other Testaments (Routledge, 2005), pp. 46–47, as quoted by Loevlie (S2); she reports that he called the claims 'I am a believer' and 'I am an atheist' 'absolutely ridiculous' (p. 47). After the working years (P20), and recorded speech in an edited volume."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "Context only; Loevlie mostly paraphrases the answer. Print check pending."
  changes_over_life: []
  coder_notes: "Coder's call. The 'Circumfession' sentence is his own published wording, but the self-label is hedged twice ('pass for'; God under 'other names'), so primary_system and A stay BELOW_THRESHOLD rather than ATHE and A 4. Leads: 'Circumfession' in print; 'Faith and Knowledge' (1996) and The Gift of Death (1992) for religion; Caputo, The Prayers and Tears of Jacques Derrida (1997)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Sephardic Jewish, French Algeria", certainty: 0.7, cites: [{source: S1, locator: "'Life and work'"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Jewish", certainty: 0.7, cites: [{source: S1, locator: "'Life and work'"}], how_known: "Britannica."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1967–1993", certainty: 0.5, cites: [{source: S1, locator: "'Life and work'"}, {source: S2, locator: "§1 (Introduction)"}], how_known: "First to last listed lasting contribution (P29, P30). The end year is Specters of Marx (1993), the latest listed lasting contribution (P30 addendum b; lasting per S2, §1). Named alternative end 1967: Glas (1974) is listed under major_works, not lasting_original_contributions, so it cannot set the end (P13, addendum b); without Specters the latest listed lasting item is the 1967 group (R audit fix, DE5)."}
  age_at_first_lasting_contribution: {value: 37, certainty: 0.7, cites: [{source: S1, locator: "opening; 'Life and work'"}], how_known: "1967 − 1930 = 37 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No axis scored at 3 or 4 (P27 anchor)."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "A BELOW_THRESHOLD; B UNKNOWN.", certainty: 0.5, cites: [{source: S2, locator: "§2"}], how_known: "Coder's reading."}
  worldview_during_major_work: {value: "Passes 'quite rightly' for an atheist while keeping 'God' under other names (1991)", certainty: 0.5, cites: [{source: S2, locator: "§2"}], how_known: "Secondary quotation of his published text."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Textual and deconstructive method, not axiomatic (S1).", certainty: 0.5, cites: [{source: S1, locator: "'Life and work'"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Life and work'"}], how_known: "Not read."}
  circle_present: {value: "unclear", rationale: "God 'called by other names'.", certainty: 0.5, cites: [{source: S2, locator: "§2"}], how_known: "Coder's reading."}
  reading: "A hedged atheism that keeps the word 'God' in a private sense."
  notes: ""

institutions:
  - {value: "Sorbonne, Paris", role: "teacher of philosophy", years: "1960–1964", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Life and work'"}], how_known: "Britannica."}
  - {value: "École Normale Supérieure, Paris", role: "teacher of philosophy", years: "1964–1984", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Life and work'"}], how_known: "Britannica."}
  - {value: "École des Hautes Études en Sciences Sociales, Paris", role: "teacher", years: "1984–1999", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Life and work'"}], how_known: "Britannica."}
collaborators:
  - {value: "Ferdinand de Saussure", relation: "influenced by", note: "différance builds on his theory of meaning", certainty: 0.7, cites: [{source: S1, locator: "'Life and work'"}], how_known: "Britannica."}
  - {value: "Geoffrey Bennington", relation: collaborator, note: "co-author of Jacques Derrida (1991/1993), which contains 'Circumfession'", certainty: 0.7, cites: [{source: S2, locator: "§2; reference 4"}], how_known: "Loevlie."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 103"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Britannica article is unsigned (Britannica Editors)."
    - "The 'Circumfession' sentence is read only as a secondary quotation; two web quotations differ by a comma and in the wording of the preceding phrase."
  open_questions:
    - "Read 'Circumfession' in print (Chicago 1993, pp. 154–55) and Derrida and Religion (2005), pp. 46–47."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Jacques Derrida.\" Encyclopaedia Britannica (revised 4 October 2026). https://www.britannica.com/biography/Jacques-Derrida. Read live 2026-10-18."
    url: "https://www.britannica.com/biography/Jacques-Derrida"
    accessed: 2026-10-18
    reliability_note: "Unsigned article. Body and header only; the AI-generated Top Questions are not cited."
    used_for: [identity, basics, contribution, childhood, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "journal article"
    author: "Elisabeth M. Loevlie"
    citation: "Loevlie, Elisabeth M. \"Faith in the Ghosts of Literature. Poetic Hauntology in Derrida, Blanchot and Morrison’s Beloved.\" Religions 4, no. 3 (2013): 336–350. https://www.mdpi.com/2077-1444/4/3/336"
    url: "https://www.mdpi.com/2077-1444/4/3/336"
    accessed: 2026-10-18
    reliability_note: "Peer-reviewed open-access article, read directly; quotes 'Circumfession' with page numbers (Chicago 1993) and reports the 2002 exchange from Sherwood and Hart (2005)."
    used_for: [worldview, timing, lane_b, collaborators]
  - id: S4
    type: secondary
    kind: "journal article"
    author: "Jon Stanley"
    citation: "Stanley, Jon. \"Why Every Christian Should ‘Quite Rightly Pass for an Atheist’.\" The Other Journal (April 2008). https://theotherjournal.com/2008/04/why-every-christian-should-quite-rightly-pass-for-an-atheist/"
    url: "https://theotherjournal.com/2008/04/why-every-christian-should-quite-rightly-pass-for-an-atheist/"
    accessed: 2026-10-18
    reliability_note: "Essay in an online theology journal, read directly; note 1 quotes the 'Circumfession' passage at length with pages (Chicago 1993). Used only to check the wording."
    used_for: [worldview]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-18
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Jacques Derrida

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Jacques Derrida (1930–2004), French philosopher of deconstruction [S1]. Draft: primary_system and A BELOW_THRESHOLD; B UNKNOWN (P16); mid_basin UNKNOWN. Not plotted.

## Life and work

El Biar, then Paris (Sorbonne, ENS, EHESS) [S1].

## Contribution and impact

Deconstruction and différance (1967); later work on literature, Marxism and psychoanalysis [S1].

## Childhood and education

Sephardic Jewish family in French Algeria; ENS from 1949 [S1].

## Adult working worldview

'I quite rightly pass for an atheist' (1991) [S2, §2].

## Heritage (context only)

Sephardic Jewish [S1].

## Timing

1967–1993, from age 37 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. 'God' kept under other names [S2].

## Open questions

- 'Circumfession' in print.

## Research log

- 2026-10-18: Read Britannica (live), Loevlie (MDPI) and Stanley (The Other Journal) directly.
