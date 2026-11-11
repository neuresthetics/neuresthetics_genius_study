---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA2)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 20c_early. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA2, order P32: F 3, rank 187). Basics from Britannica (Wilfrid Desan, signed; scholars edition, read in full) and SEP 'Jean-Paul Sartre' (Reynolds and Renaudie, rev. 2026). Lasting work: Nausea (1938; SEP 'highly influential'; Britannica 'a most original ... piece of work') and Being and Nothingness (1943; Britannica 'a philosopher of remarkable originality and depth'; SEP 'his most famous philosophical book', what 'remains alive'); span 1938–1943 by publication (P30 #1), age 33. Own words: the public lecture Existentialism Is a Humanism (given late 1945, published 1946), two years after the span (P20 cap 0.5), read in an unofficial web copy of Mairet's translation (marxists.org; 0.7 cap, §7): 'Atheistic existentialism, of which I am a representative ...'; 'we only mean to say that God does not exist'. primary_system EXIST 0.5 (written_profession, P20), alt ATHE, as for de Beauvoir (systems/EXIST.md does not split atheist from theist existentialism); A 4 at 0.5, alt BELOW_THRESHOLD; not a scientist, B UNKNOWN; C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD (P10). Not plotted (B UNKNOWN). Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #176, F3 rank 187). Needs: A faded single-source; B UNKNOWN. Dual bio: Britannica Desan (S1) + Wikipedia EN (S5, P50). Primary: Being and Nothingness Barnes (S6, IA OCR of Philosophical Library / Washington Square Press) — Part Four Ch. 2 III: 'the idea of God is contradictory and we lose ourselves in vain. Man is a useless passion' (in-span 1943); Introduction contingency / de trop of being-in-itself (ontology, not P16). Existentialism Is a Humanism (S3) kept as after-span corroboration. The Words / Les Mots Frechtman Braziller 1964 (S7, IA OCR): baptized Catholic; raised Catholic; 'He never looked at me again'; 'He vegetated in me for a while, then He died' (post-span autobiography, P20). P47 source_quality on S1–S7. A_locus 4 @0.5 → 4 @0.7 (written_profession; drop BELOW_THRESHOLD alt — BN unconditional contradiction of God resolves lecture 'even if God existed'; unofficial BN/lecture + Words retrospective keep 0.7 not 1.0); support: corroborated (S6+S3+S7). B_cause stays UNKNOWN (not a scientist; BN contingency/de trop is ontology of being-in-itself, not a P16 statement of exceptionless physical order; P41 not stretched). primary_system EXIST @0.5 alt ATHE unchanged. mid_basin BELOW_THRESHOLD → false @0.7 (A≥3 branch, P10). Chart-moving NO (still unplotted: B UNKNOWN). Nausea / The Flies character speech not scored for A (P42). No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: sartre-jean-paul
  display_name: "Jean-Paul Sartre"
  roster:
    canonical_name: "Jean-Paul Sartre"
    rank: 187
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: "core"
    field: "philosophy"
    field_bucket: "philosophy"
  full_name: {value: "Jean-Paul Charles Aymard Sartre", certainty: 0.7, cites: [{source: S5, locator: "lead"}], how_known: "Wikipedia lead (full form); Britannica gives Jean-Paul Sartre."}
  native_name: {value: "Jean-Paul Sartre", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  aliases:
    - {name: "Sartre-Jean-Paul", kind: "roster alias"}

basics:
  birth:
    date: {value: "1905-06-21", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "Paris", modern_name: "Paris, France", polity_then: "France", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  death:
    date: {value: "1980-04-15", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "Paris", modern_name: "Paris, France", polity_then: "France", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1938, certainty: 0.7, cites: [{source: S1, locator: "Early life and writings"}, {source: S2, locator: "opening"}], how_known: "Nausea, published 1938 (S1); called 'highly influential' (S2); publication (P30 #1)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "Early life and writings"}], how_known: "1938–1943 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "France (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Early life and writings"}], how_known: "Le Havre, Laon, Paris."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["French"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "French titles."}
  occupations: {value: ["philosopher", "novelist", "playwright"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

contribution:
  era_bucket: 20c_early
  fields: {value: ["philosophy", "literature"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "La Nausée (Nausea)", year: 1938, kind: "work", lasting: "'highly influential works of literature ... like Nausea (1938)' (S2); 'a most original, fiercely individualistic ... piece of work' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Early life and writings"}, {source: S2, locator: "opening"}], how_known: "Britannica and SEP; published 1938."}
    - {value: "L’Être et le néant (Being and Nothingness)", year: 1943, kind: "work", lasting: "'it was above all in ... (1943; Being and Nothingness) that Sartre revealed himself as a philosopher of remarkable originality and depth' (S1); 'what remains alive ... his most famous philosophical book' (S2)", certainty: 0.7, cites: [{source: S1, locator: "Early life and writings"}, {source: S2, locator: "opening"}], how_known: "Britannica and SEP; published 1943."}
  evidence_of_impact:
    - {value: "Awarded (and declined) the 1964 Nobel Prize for Literature", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  major_works:
    - {value: "Existentialism Is a Humanism (public lecture)", year: 1945, kind: "lecture series", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "SEP: given 'towards the end of 1945'; published 1946."}
    - {value: "Les Mouches (The Flies)", year: 1943, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "Early life and writings"}, {source: S5, locator: "Career"}], how_known: "Britannica / Wikipedia; in-span drama — character speech not used for A (P42)."}
    - {value: "Les Mots (The Words)", year: 1964, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S7, locator: "title page"}], how_known: "Britannica; Frechtman Braziller 1964 (S7). Autobiography after the span."}
    - {value: "Critique of Dialectical Reason, vol. 1", year: 1960, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "Political activities"}], how_known: "Britannica: 'a major work'; not called lasting."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "The leading exponent of existentialism in the 20th century (S1).", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Catholic baptism / registration; maternal grandfather Charles Schweitzer Lutheran / Protestant; household 'believed in God, as a matter of discretion'", certainty: 0.7, cites: [{source: S7, locator: "pp. 97–100 (Frechtman)"}], how_known: "The Words: baptized; raised Catholic; grandfather ridiculed Catholicism; grandmother sceptic."}
  family_religious_practice: {value: "Nominal Catholic registration; Thursday religious instruction at Abbé Dibildos Institute for about six months; grandfather anti-clerical table-talk; mother had 'her own God'", certainty: 0.7, cites: [{source: S7, locator: "pp. 97–102"}], how_known: "The Words."}
  parents_and_household:
    - {value: "Father Jean-Baptiste Sartre died early; raised in the home of maternal grandfather Charles (Karl) Schweitzer with mother Anne-Marie", role: "family", certainty: 0.7, cites: [{source: S1, locator: "Early life and writings"}, {source: S7, locator: "Part 1"}], how_known: "Britannica and The Words."}
  household_circumstances: {value: "Meudon then Paris (1 Rue le Goff); grandfather founded Modern Language Institute", certainty: 0.7, cites: [{source: S7, locator: "Part 1"}], how_known: "The Words."}
  schooling:
    - {value: "Lycée Henri IV; École Normale Supérieure (graduated 1929)", certainty: 0.7, cites: [{source: S1, locator: "Early life and writings"}], how_known: "Britannica."}
    - {value: "Childhood religious instruction at Abbé Dibildos Institute (brief)", certainty: 0.7, cites: [{source: S7, locator: "pp. 100–101"}], how_known: "The Words."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated in sources read."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events:
    - {value: "Childhood break with felt presence of God after burning a rug and blaspheming; thereafter 'He never looked at me again'", certainty: 0.7, cites: [{source: S7, locator: "pp. 101–102"}], how_known: "The Words (retrospective autobiography)."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1938–1943", certainty: 0.7, cites: [{source: S1, locator: "Early life and writings"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system:
    value: EXIST
    basis: written_profession
    certainty: 0.5
    cites: [{source: S3, locator: "para. on 'atheistic existentialism'"}, {source: S6, locator: "Part Four Ch. 2 III"}]
    how_known: "Public lecture (late 1945, published 1946), two years after the span, so capped at 0.5 (P20); unofficial web copy (0.7 cap, §7). BN (1943) is the existentialist treatise but does not use the label 'existentialist' in the scored line; lecture supplies the self-description."
    rationale: "'Atheistic existentialism, of which I am a representative' (S3). Named alternative ATHE: BN 'the idea of God is contradictory' (S6) and lecture 'God does not exist' (S3); systems/EXIST.md does not split atheist from theist existentialism, so ATHE stays the alternative, as for de Beauvoir."
    note: "systems/EXIST.md does not separate atheist from theist existentialism; his EXIST is the atheist kind (A 4), so ATHE stays the named alternative."
  secondary_system: {value: UNKNOWN, how_known: "None scored; ATHE is the named alternative to EXIST, not a second system."}
  candidate_codes_considered:
    - {code: EXIST, reason: "Self-described atheistic existentialist in 1945 lecture (S3); BN 1943 is the major existentialist treatise (S1, S2)."}
    - {code: ATHE, reason: "BN: idea of God contradictory; lecture: God does not exist; Words: God 'died' in childhood (S6, S3, S7)."}
  lio_axes:
    A_locus:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S6, locator: "Part Four Ch. 2 III ('idea of God is contradictory')"}, {source: S3, locator: "para. on 'abandonment'"}, {source: S7, locator: "pp. 101–102"}]
      how_known: "BN (1943, during span) in author's philosophical voice asserts the idea of God is contradictory (IA OCR of Barnes translation — archive scan / unofficial, 0.7 cap). Lecture (1945, after span) corroborates 'God does not exist' (P20). Words (1964) retrospective childhood end of felt God (P20). Unofficial copies keep the score at 0.7, not 1.0."
      rationale: "No God (A 4): BN — 'the idea of God is contradictory and we lose ourselves in vain. Man is a useless passion'; lecture — 'we only mean to say that God does not exist'; Words — God 'died' / 'He never looked at me again'. Create-pass named alternative BELOW_THRESHOLD (lecture 'even if God existed that would make no difference') dropped: BN asserts contradiction unconditionally; the lecture line sets the ethical question aside, not a theist option. Nausea / The Flies not used for A (P42 character/drama speech)."
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30). BN Introduction on contingency of being-in-itself ('Uncreated, without reason for being… de trop for eternity') is ontology of being, not a P16 statement of the exceptionless order of physical nature (coder's call). P41 not stretched from denying God as Ens causa sui. Nausea Roquentin contingency is character speech (P42)."}
    C_ledger: {value: UNKNOWN, how_known: "Lead: 'useless passion' / no Ens causa sui may bear on C; not scored at this reading."}
    D_authority: {value: UNKNOWN, how_known: "Lead: man 'is nothing else but what he makes of himself' (S3); not scored."}
    E_scope: {value: UNKNOWN, how_known: "Not read (P7)."}
  mid_basin: {value: false, certainty: 0.7, cites: [{source: S6, locator: "Part Four Ch. 2 III"}, {source: S3, locator: "para. on 'abandonment'"}], how_known: "A 4 at 0.7: the A ≥ 3 branch reads A only (P10), so B UNKNOWN does not block it."}
  statements:
    - text: "But the idea of God is contradictory and we lose ourselves in vain. Man is a useless passion."
      cites: [{source: S6, locator: "Part Four, Chapter 2, III (closing of existential psychoanalysis)"}]
      date: "1943"
      context: "Being and Nothingness (L'Être et le néant, 1943), Hazel E. Barnes translation; during the lasting-contribution span."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "IA OCR of Barnes English (in.ernet.dli.2015.6651 / related IA items); not checked against a clean Philosophical Library 1956 page image. OCR has minor character errors nearby; wording of this closing couplet is standard across editions (0.7 cap)."
    - text: "Uncreated, without reason for being, without any connection with another being, being-in-itself is de trop for eternity."
      cites: [{source: S6, locator: "Introduction / The Pursuit of Being (contingency of being-in-itself)"}]
      date: "1943"
      context: "BN Introduction: ontological contingency of being-in-itself — recorded for B discussion, not scored as P16 nature-order."
      axes: []
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Not used for B_cause (ontology ≠ exceptionless physical law). OCR as above."
    - text: "Atheistic existentialism, of which I am a representative, declares with greater consistency that if God does not exist there is at least one being whose existence comes before its essence, a being which exists before it can be defined by any conception of it."
      cites: [{source: S3, locator: "para. on 'atheistic existentialism'"}]
      date: "1945"
      context: "Public lecture Existentialism Is a Humanism, Paris, late 1945 (S2), published 1946; after the span."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Mairet's translation (in Kaufmann, ed., 1956/1989) as posted at marxists.org; not checked against the Nagel 1946 text or the Yale 2007 Macomber edition (0.7 cap, §7)."
    - text: "And when we speak of “abandonment” – a favorite word of Heidegger – we only mean to say that God does not exist, and that it is necessary to draw the consequences of his absence right to the end."
      cites: [{source: S3, locator: "para. on 'abandonment'"}]
      date: "1945"
      context: "Same lecture."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "As above."
    - text: "I have just related the story of a missed vocation: I needed God, He was given to me, I received Him without realizing that I was seeking Him. Failing to take root in my heart, He vegetated in me for a while, then He died."
      cites: [{source: S7, locator: "pp. 101–102"}]
      date: "1964"
      context: "The Words (Les Mots), Frechtman translation; retrospective on childhood faith; after the lasting-contribution span (P20)."
      axes: [A_locus]
      kind: "autobiography"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "IA OCR of Braziller 1964 Frechtman; corroborates lifelong atheism assumed in BN, not sole warrant for A during the span."
    - text: "Indignation saved me. I flew into a rage against so crude an indiscretion, I blasphemed, I muttered like my grandfather: \"God damn it, God damn it, God damn it.\" He never looked at me again."
      cites: [{source: S7, locator: "pp. 101–102"}]
      date: "1964"
      context: "The Words: childhood episode after burning a rug; felt gaze of God then permanent absence."
      axes: [A_locus]
      kind: "autobiography"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "As above; childhood recollection in post-span autobiography."
  changes_over_life:
    - {value: "Baptized and raised Catholic; childhood end of felt relation to God; remained an atheist (BN; lecture; Words)", year: 1943, certainty: 0.7, cites: [{source: S7, locator: "pp. 97–102"}, {source: S6, locator: "Part Four Ch. 2 III"}, {source: S3, locator: "abandonment"}], how_known: "Words for childhood; BN for adult philosophical denial during the span."}
  coder_notes: "Coder's call. B left UNKNOWN rather than P41 B 3@0.5 from denying Ens causa sui / contingency of being — those lines are ontology of being-in-itself and the failed project of becoming God, not exceptionless natural law (P16). Nausea and The Flies unread for authorial non-character voice (P42). No fallacy_catalog (Jason)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "French (Alsatian Schweitzer maternal line; Périgord Sartre paternal)", certainty: 0.7, cites: [{source: S7, locator: "Part 1"}, {source: S5, locator: "Early life"}], how_known: "The Words; Wikipedia."}
  religious_heritage_by_birth: {value: "Catholic (baptized / registered); maternal grandfather Protestant Lutheran", certainty: 0.7, cites: [{source: S7, locator: "pp. 97–100"}], how_known: "The Words."}
  baptism_or_initiation: {value: "Baptized Catholic ('I had been baptized, like so many others, in order to preserve my independence')", certainty: 0.7, cites: [{source: S7, locator: "p. 98"}], how_known: "The Words."}
  childhood_catechism: {value: "Raised in the Catholic faith; Thursday instruction at Abbé Dibildos Institute (~six months); said daily prayers as a child", certainty: 0.7, cites: [{source: S7, locator: "pp. 97–101"}], how_known: "The Words."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1938–1943", certainty: 0.7, cites: [{source: S1, locator: "Early life and writings"}], how_known: "Nausea (1938) to Being and Nothingness (1943), the listed lasting works (P29, P30 #1)."}
  age_at_first_lasting_contribution: {value: 33, certainty: 0.7, cites: [{source: S1, locator: "Introduction; Early life and writings"}], how_known: "1938 − 1905 = 33 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: "1943, age 38: 'the idea of God is contradictory'", year: 1943, age: 38, certainty: 0.7, cites: [{source: S6, locator: "Part Four Ch. 2 III"}], how_known: "BN during the span. Childhood Words episode is earlier but retrospective (1964). Lecture 1945 is after the span."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S6, locator: "Part Four Ch. 2 III"}], how_known: "1943 falls at the end of 1938–1943."}
  worldview_during_major_work: {value: EXIST, certainty: 0.5, cites: [{source: S3, locator: "atheistic existentialism"}, {source: S6, locator: "Part Four Ch. 2 III"}], how_known: "As primary_system (lecture label after span at 0.5; BN atheist ontology during span)."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Phenomenological ontology, not deductive geometric argument (S1, S6).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Not applicable to BN's method as scored here."}
  circle_present: {value: "no", rationale: "Idea of God contradictory; no God as source or end (S6, S3).", certainty: 0.7, cites: [{source: S6, locator: "Part Four Ch. 2 III"}], how_known: "Coder's reading of BN."}
  reading: "Secular atheist existentialism; mid_basin false via A 4."
  notes: "Lane B only. Not plotted (B_cause UNKNOWN)."

institutions:
  - {value: "Les Temps modernes (co-founder and editor, 1945)", role: editor, kind: other, certainty: 0.7, cites: [{source: S1, locator: "Post-World War II work"}], how_known: "Britannica."}
collaborators:
  - {value: "Simone de Beauvoir", relation: "collaborator", note: "lifelong partner; co-founded Les Temps Modernes", certainty: 0.7, cites: [{source: S1, locator: "Early life and writings; Post-World War II work"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 187"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "BN and Words verified via IA OCR / unofficial copies (0.7 cap)."
    - "EXIST self-label is after the span (P20)."
  open_questions:
    - "Clean Philosophical Library / Washington Square Barnes page image for BN God line (would confirm OCR)."
    - "Yale 2007 Macomber Existentialism Is a Humanism vs Mairet marxists.org wording."
    - "War Diaries / Carnets (1939–40) primary on childhood loss of faith — secondary trail only this pass."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Wilfrid Desan"
    citation: "Desan, Wilfrid. 'Jean-Paul Sartre.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/Jean-Paul-Sartre/65811"
    url: "https://kids.britannica.com/scholars/article/Jean-Paul-Sartre/65811"
    accessed: 2026-10-24
    reliability_note: "Signed article, read in full."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, timing, collaborators, institutions]
  - id: S2
    type: secondary
    kind: "encyclopedia"
    author: "Jack Reynolds and Pierre-Jean Renaudie"
    citation: "Reynolds, Jack, and Pierre-Jean Renaudie. 'Jean-Paul Sartre.' Stanford Encyclopedia of Philosophy (rev. 10 July 2026). https://plato.stanford.edu/entries/sartre/"
    url: "https://plato.stanford.edu/entries/sartre/"
    accessed: 2026-10-24
    reliability_note: "Signed scholarly reference article."
    source_quality: "reference entry"
    used_for: [basics, contribution, worldview]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Jean-Paul Sartre (trans. Philip Mairet)"
    citation: "Sartre, Jean-Paul. Existentialism Is a Humanism (lecture 1945; Paris: Nagel, 1946), trans. Philip Mairet, in Walter Kaufmann, ed., Existentialism from Dostoyevsky to Sartre (Meridian, 1989); web copy at marxists.org. https://www.marxists.org/reference/archive/sartre/works/exist/sartre.htm"
    url: "https://www.marxists.org/reference/archive/sartre/works/exist/sartre.htm"
    accessed: 2026-10-24
    reliability_note: "Unofficial web copy of a published translation (0.7 cap, §7)."
    source_quality: "unofficial web copy"
    used_for: [worldview, timing]
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
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. \"Jean-Paul Sartre.\" Wikipedia, English. https://en.wikipedia.org/wiki/Jean-Paul_Sartre."
    url: "https://en.wikipedia.org/wiki/Jean-Paul_Sartre"
    accessed: 2026-10-24
    reliability_note: "P50 dual bio with Britannica. Used for full name and career cross-check (The Flies). Not sole warrant for A."
    source_quality: "reference entry"
    used_for: [identity, contribution, heritage]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Jean-Paul Sartre (trans. Hazel E. Barnes)"
    citation: "Sartre, Jean-Paul. Being and Nothingness: An Essay on Phenomenological Ontology. 1943. Trans. Hazel E. Barnes. New York: Philosophical Library, 1956 (Washington Square Press reprints). Internet Archive OCR: https://archive.org/stream/in.ernet.dli.2015.6651/2015.6651.Being-And-Nothingness_djvu.txt (and related IA items)."
    url: "https://archive.org/details/beingnothingness00wash"
    accessed: 2026-10-24
    reliability_note: "Primary philosophical treatise during the span; wording checked in IA OCR of Barnes English (archive scan). Clean publisher page image not opened this pass (0.7 cap)."
    source_quality: "archive scan (OCR only)"
    used_for: [worldview, timing, lane_b]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "Jean-Paul Sartre (trans. Bernard Frechtman)"
    citation: "Sartre, Jean-Paul. The Words. Trans. Bernard Frechtman. New York: George Braziller, 1964 (from Les Mots, Gallimard 1964). Internet Archive OCR stream of the Braziller text."
    url: "https://archive.org/stream/SartreJeanPaulLiteraryAndPhilosophicalEssaysCollier1962/Sartre%2C%20Jean-Paul%20-%20Words%2C%20The%20%28Braziller%2C%201964%29_djvu.txt"
    accessed: 2026-10-24
    reliability_note: "Primary autobiography after the span; IA OCR of Frechtman Braziller 1964. Used for heritage, childhood faith, and corroboration of lifelong atheism (P20)."
    source_quality: "archive scan (OCR only)"
    used_for: [childhood, heritage, worldview]
---

# Jean-Paul Sartre

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Jean-Paul Sartre (1905–1980), French philosopher and writer [S1]. Deepen D1: primary_system EXIST (0.5, alt ATHE); **A 4 at 0.7** (corroborated); B UNKNOWN; **mid_basin false** at 0.7. Not plotted (B UNKNOWN).

## Life and work

Paris; Le Havre; Laon; Paris [S1]. Co-founded Les Temps modernes with de Beauvoir [S1].

## Contribution and impact

Nausea (1938); Being and Nothingness (1943) [S1, S2]. The Flies (1943); Existentialism Is a Humanism (1945/46); The Words (1964) [S1, S5, S7].

## Childhood and education

Baptized Catholic; raised with Catholic instruction and a Protestant grandfather who ridiculed papism [S7]. Childhood end of felt relation to God [S7]. Lycée Henri IV; ENS [S1].

## Adult working worldview

BN (1943): 'the idea of God is contradictory… Man is a useless passion' [S6]. Lecture (1945): 'Atheistic existentialism, of which I am a representative'; 'God does not exist' [S3]. Words (1964): God 'died' in childhood; 'He never looked at me again' [S7]. BN contingency / de trop of being-in-itself is ontology, not scored for B [S6].

## Heritage (context only)

Catholic baptism; Alsatian Schweitzer maternal line (Lutheran grandfather); French [S7, S5].

## Timing

First lasting contribution 1938, at 33 [S1]. BN 1943 during 1938–1943 span.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle [S6]. B_cause UNKNOWN (no P16 nature-order statement).

## Open questions

- Clean Barnes BN page image; Yale Macomber lecture text.
- War Diaries primary on childhood loss of faith.

## Research log

- 2026-10-19: Read Britannica (Desan); SEP; the 1945 lecture (web copy).
- 2026-10-24: Deepen D1 — BN Barnes IA OCR (God contradictory; contingency/de trop); Words Frechtman IA OCR (baptism, childhood God); Wikipedia dual bio; A 4@0.7; B UNKNOWN; mid false.
