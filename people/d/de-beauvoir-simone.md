---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch K)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to philosophy. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch K, order P32: F 5, rank 72). Basics from Britannica (Britannica Editors, unsigned; Top Questions not cited) and SEP (Bergoffen and Burke, rev. 2023). Worldview from The Ethics of Ambiguity (1947; Frechtman translation 1948, marxists.org web copy), Part I. Not a scientist (P30). primary_system EXIST (0.5, alt ATHE); A 4 (0.5, alt BELOW_THRESHOLD); B UNKNOWN (P16); mid_basin BELOW_THRESHOLD. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Audit fixes (fallacy_catalog audit of 2d75649, run 1). mid_basin how_known explains BELOW_THRESHOLD: the A ≥ 3 branch reads A only (P10). SEP's 'at age fourteen' line cited explicitly for A 4. EXIST kept (0.5, alternative ATHE), with a note that the EXIST system file does not separate atheist from theist existentialism."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #71, F5 rank 72). Needs: A faded; B UNKNOWN; sources 3. Dual bio: Britannica Editors (S1; live Cloudflare-thin, Top Questions via Wayback) + Wikipedia EN (S5, P50). Primary/own words: Ethics of Ambiguity Part I–III Frechtman (S3 marxists.org web copy, 0.7 cap) — 'far from God's absence authorizing all license'; 'if God does not exist, man's faults are inexpiable'. Memoirs of a Dutiful Daughter (1958) S6 — IA borrow 401; long quotation via W. Scott Haine / A Woman's Paris (secondary quotation): 'One night I summoned God, if He really existed… I was very glad He didn't exist.' Paris Review Art of Fiction No. 35 (S7, recorded interview): acknowledges lost religious faith. All Said and Done 1974 p. 478 (S8, secondary quotation via Wikipedia/Goodreads): atheist vs faith-as-evasion. Force of Circumstance lead 'God had died when I was fourteen' noted in open_questions (IA 401). Added Ethics of Ambiguity 1947 as lasting contribution (Britannica Top Questions + SEP §5). P47 source_quality on S1–S8. A_locus 4 @0.5 → 4 @0.7 (written_profession; drop BELOW_THRESHOLD alt — Memoirs/All Said resolve Ethics conditional; unofficial Ethics + secondary Memoirs keep 0.7 not 1.0); support stays corroborated (S3+S2+S6+S8). B_cause stays UNKNOWN (not a scientist; Ethics 'nature' passages are human-nature/ethics/Hegel, not P16 natural order; P41 not stretched from 'strange power'). primary_system EXIST @0.5 alt ATHE unchanged. mid_basin BELOW_THRESHOLD → false @0.7 (A≥3 branch, P10). Chart-moving NO (still unplotted: B UNKNOWN). No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: de-beauvoir-simone
  display_name: "Simone de Beauvoir"
  roster:
    canonical_name: "Simone de Beauvoir"
    rank: 72
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Simone-Lucie-Ernestine-Marie Bertrand de Beauvoir", certainty: 0.7, cites: [{source: S1, locator: "header ('In full')"}], how_known: "Britannica."}
  native_name: {value: UNKNOWN, how_known: "French, Latin script."}
  aliases: []

basics:
  birth:
    date: {value: "1908-01-09", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "§1"}], how_known: "Britannica and SEP agree."}
    place: {value: "Paris, France", modern_name: "Paris, France", polity_then: "France", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "§1"}], how_known: "Two sources."}
  death:
    date: {value: "1986-04-14", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Paris, France", modern_name: "Paris, France", polity_then: "France", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1943, certainty: 0.7, cites: [{source: S1, locator: "novels paragraph"}], how_known: "L'Invitée (1943; She Came To Stay), first listed lasting work (P30)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Birth year bucket (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "France (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Paris."}
  sex_as_recorded: {value: "female", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [French], certainty: 0.7, cites: [{source: S1, locator: "titles"}], how_known: "Britannica."}
  occupations: {value: ["writer", "philosopher", "teacher"], certainty: 0.7, cites: [{source: S1, locator: "opening; paragraph 2"}], how_known: "Britannica."}
contribution:
  primary_domain: philosophy
  fields: {value: ["philosophy", "literature", "feminist theory"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "L'Invitée (She Came To Stay)", year: 1943, kind: work, lasting: "novel expounding existential themes (S1)", certainty: 0.7, cites: [{source: S1, locator: "novels paragraph"}], how_known: "Britannica."}
    - {value: "Pour une morale de l'ambiguïté (The Ethics of Ambiguity)", year: 1947, kind: work, lasting: "Named among her principal works (S1 Top Questions); SEP §5 on her existentialist ethics (S2)", certainty: 0.7, cites: [{source: S1, locator: "Top Questions ('Notable works')"}, {source: S2, locator: "§5"}], how_known: "Britannica Top Questions and SEP."}
    - {value: "Le Deuxième Sexe (The Second Sex)", year: 1949, kind: work, lasting: "'a classic of feminist literature' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "Les Mandarins (The Mandarins)", year: 1954, kind: work, lasting: "Prix Goncourt (S1)", certainty: 0.7, cites: [{source: S1, locator: "novels paragraph"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "The Second Sex 'became a classic of feminist literature'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Pyrrhus et Cinéas", year: 1944, kind: book, certainty: 0.7, cites: [{source: S2, locator: "§4"}], how_known: "SEP; philosophical essay before Ethics; not separately scored as lasting here."}
    - {value: "Mémoires d'une jeune fille rangée (Memoirs of a Dutiful Daughter)", year: 1958, kind: book, certainty: 0.7, cites: [{source: S1, locator: "Top Questions"}], how_known: "Britannica; autobiography (after lasting-contribution span)."}
  honours:
    - {value: "Prix Goncourt", year: 1954, certainty: 0.7, cites: [{source: S1, locator: "novels paragraph"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "(S1, S2).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Catholic", certainty: 0.7, cites: [{source: S2, locator: "§1"}, {source: S5, locator: "Religious upbringing"}], how_known: "SEP: 'a traditional bourgeois, Catholic upbringing'; Wikipedia: raised Catholic, convent schools."}
  family_religious_practice: {value: "Mother devout (regular confession and Mass); Simone took communion three times a week at age 7; intended to become a nun", certainty: 0.5, cites: [{source: S5, locator: "Religious upbringing"}], how_known: "Wikipedia Religious upbringing (dual bio, P50); not checked against Memoirs page images (IA borrow 401)."}
  parents_and_household:
    - {value: "Father Georges Bertrand de Beauvoir; mother Françoise (née Brasseur); sister Hélène", role: parents, certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP."}
  household_circumstances: {value: "Bourgeois family that lost class status in 1919", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP."}
  schooling:
    - {value: "Institut Adeline Désir, private Catholic school for girls", stage: "grammar or secondary school", run_by: "religious body", certainty: 0.7, cites: [{source: S2, locator: "§1"}, {source: S1, locator: "opening"}], how_known: "SEP and Britannica."}
    - {value: "Sorbonne; agrégation in philosophy, 1929", stage: university, run_by: "state or municipal", certainty: 0.7, cites: [{source: S1, locator: "paragraph 2"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [French], certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "Rejected the existence of God at fourteen", year: 1922, certainty: 0.7, cites: [{source: S2, locator: "§1"}, {source: S6, locator: "Jockey / mysticism passage (via Haine secondary quotation)"}], how_known: "SEP gives the age; Memoirs own account of summoning God and being glad He did not exist (S6). Year 1908+14=1922 at 0.5 for the exact year only; event itself at 0.7."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1943–1954", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system:
    value: EXIST
    basis: scholarly_reconstruction
    certainty: 0.5
    cites: [{source: S2, locator: "opening; §5"}, {source: S1, locator: "opening"}]
    rationale: "SEP: in Ethics of Ambiguity 'She identifies herself as an existentialist'; Britannica: significant philosopher of existentialism. Named alternative: ATHE, since SEP calls The Ethics of Ambiguity 'a secularism that rejects the ideas of God and Humanity' and she remains an atheist (S5, S8)."
    how_known: "Reconstruction in SEP and Britannica (0.5 cap); Ethics web copy does not itself carry a first-person 'I am an existentialist' line in Parts I–III as read."
    note: "systems/EXIST.md does not separate atheist from theist existentialism; her EXIST is the atheist kind (A 4), so ATHE stays the named alternative."
  secondary_system: {value: UNKNOWN, how_known: "None scored; ATHE is the named alternative to EXIST, not a second system."}
  candidate_codes_considered:
    - {code: EXIST, reason: "Self-identified existentialist in Ethics per SEP (S2); Ethics treatise during the span (S3)."}
    - {code: ATHE, reason: "Rejected God at fourteen; 'God's absence' (S3); Memoirs glad He did not exist (S6); All Said and Done atheist vs faith (S8)."}
  lio_axes:
    A_locus:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S3, locator: "Part I ('God's absence'; 'if God does not exist')"}, {source: S2, locator: "§1 ('at age fourteen Beauvoir rejected the existence of God')"}, {source: S6, locator: "Jockey / mysticism passage (via Haine)"}, {source: S8, locator: "p. 478 (via Wikipedia / Goodreads)"}]
      how_known: "Published Ethics during the span (unofficial Frechtman web copy, 0.7 cap, §7) plus published autobiography Memoirs (secondary quotation pending IA page check) and All Said and Done atheist self-description (secondary quotation). Retrospective self-report about the teen rejection capped at 0.7 (P20); web copy and secondary quotations keep the score at 0.7, not 1.0."
      rationale: "No God (A 4): Ethics treats 'God's absence' as the human condition ('far from God's absence authorizing all license… a world which is not the work of a strange power, but of himself'); Memoirs: 'I was very glad He didn't exist'; All Said and Done contrasts the atheist who 'confronts honestly' with faith as evasion. Create-pass named alternative BELOW_THRESHOLD (Ethics conditional 'if God does not exist') dropped: Memoirs and All Said and Done affirm non-existence unconditionally. Paris Review (S7) corroborates loss of faith as interview but is not required for the score."
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30). Ethics passages on 'nature' concern human nature, Hegelian natural law vs morality, and Marxist naturalization of oppression — not a P16 statement of the order of physical nature (coder's call). 'World which is not the work of a strange power' is about human responsibility for the human world, not exceptionless natural law (P41 not applied). Second Sex biology unread."}
    C_ledger: {value: UNKNOWN, how_known: "'A God can pardon, efface, and compensate. But if God does not exist, man's faults are inexpiable' bears on C, but it is about human responsibility without a cosmic ledger; not scored (coder's call)."}
    D_authority: {value: UNKNOWN, how_known: "'the genuine man will not agree to recognize any foreign absolute' may bear on D; not scored at this reading."}
    E_scope: {value: UNKNOWN, how_known: "Not read (P7)."}
  mid_basin: {value: false, certainty: 0.7, cites: [{source: S3, locator: "Part I"}, {source: S6, locator: "Jockey / mysticism passage (via Haine)"}], how_known: "A 4 at 0.7: the A ≥ 3 branch reads A only (P10), so B UNKNOWN does not block it."}
  statements:
    - text: "However, far from God’s absence authorizing all license, the contrary is the case, because man is abandoned on the earth, because his acts are definitive, absolute engagements. He bears the responsibility for a world which is not the work of a strange power, but of himself, where his defeats are inscribed, and his victories as well."
      cites: [{source: S3, locator: "Part I"}]
      date: "1947"
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Frechtman translation (1948), marxists.org web copy of Part I; not checked against Philosophical Library 1948 or Open Road reprint (0.7 cap, §7). Re-read 2026-10-24."
    - text: "A God can pardon, efface, and compensate. But if God does not exist, man’s faults are inexpiable."
      cites: [{source: S3, locator: "Part I"}]
      date: "1947"
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "As above. Conditional phrasing; A score rests on the 'God's absence' assertion plus Memoirs/All Said and Done."
    - text: "One night I summoned God, if He really existed, to show Himself to me. He didn't, and I never addressed another word to Him. I was very glad He didn't exist. I should have hated it if what was going on here below had had to end up in eternity."
      cites: [{source: S6, locator: "Jockey / mysticism passage (via Haine secondary quotation)"}]
      date: "1958"
      context: "Memoirs of a Dutiful Daughter (1958), recounting teen / early adult break with God; after the lasting-contribution span, but documents the lifelong atheism already assumed in Ethics (P31 continuity)."
      axes: [A_locus]
      kind: "autobiography"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Long quotation in W. Scott Haine interview on A Woman's Paris (2014), citing Memoirs; IA borrow of memoirsofdutiful00beau returned 401. Primary page check pending (P26)."
    - text: "Faith allows an evasion of those difficulties which the atheist confronts honestly. And to crown all, the believer derives a sense of great superiority from this very cowardice itself."
      cites: [{source: S8, locator: "p. 478 (via Wikipedia Religious upbringing / Goodreads)"}]
      date: "1974"
      context: "All Said and Done (Tout compte fait), English Putnam 1974 p. 478; post-span adult affirmation of the atheist stance."
      axes: [A_locus]
      kind: "autobiography"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Wording as on Wikipedia and Goodreads; book not borrowed (IA 401)."
    - text: "That may be that in my case the vocation was accentuated because I had lost religious faith"
      cites: [{source: S7, locator: "loss of religious faith exchange"}]
      date: "1965"
      context: "Paris Review Art of Fiction No. 35; interviewer links loss of faith to writing; she does not deny it."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "newspaper interview"
      verified_on: 2026-10-24
      note: "Transcript on theparisreview.org; supports continuity of loss of faith, not scored alone for A."
  changes_over_life:
    - {value: "Initially devout Catholic; rejected the existence of God at fourteen; remained an atheist", year: 1922, certainty: 0.7, cites: [{source: S2, locator: "§1"}, {source: S5, locator: "Religious upbringing"}, {source: S6, locator: "Jockey / mysticism passage (via Haine)"}], how_known: "SEP, Wikipedia, Memoirs quotation."}
  coder_notes: "Coder's call. B left UNKNOWN rather than P41 B 3@0.5 from 'strange power' — that line is about the human world of engagements, not physical nature. Ethics Parts I–III scanned for nature-order; none found. Pyrrhus et Cinéas (1944) and Second Sex biology unread. No fallacy_catalog (Jason)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "French bourgeois", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP."}
  religious_heritage_by_birth: {value: "Catholic", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: "Catholic school / convent education; communion three times a week at age 7 (S5)", certainty: 0.5, cites: [{source: S5, locator: "Religious upbringing"}], how_known: "Wikipedia; dual bio."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1943–1954", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "First to last listed lasting contribution (P29, P30): L'Invitée 1943 through Les Mandarins 1954; Ethics 1947 falls inside."}
  age_at_first_lasting_contribution: {value: 35, certainty: 0.7, cites: [{source: S1, locator: "opening; novels paragraph"}], how_known: "1943 − 1908 = 35 (P30)."}
  first_evidence_of_lio_type_views: {value: "1947, age 39: 'far from God’s absence authorizing all license'", year: 1947, age: 39, certainty: 0.5, cites: [{source: S3, locator: "Part I"}], how_known: "Earlier works (L'Invitée 1943, Pyrrhus et Cinéas 1944) not read for locus: 'earlier works not read' (P30 #7). Childhood rejection is earlier but the published adult Ethics line is the first evidence cited for the working worldview."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S3, locator: "Part I"}], how_known: "1947 falls in 1943–1954."}
  worldview_during_major_work: {value: EXIST, certainty: 0.5, cites: [{source: S2, locator: "opening; §5"}], how_known: "As primary_system."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Essays and novels, not deductive geometric argument (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Not read."}
  circle_present: {value: "no", rationale: "No God as source or end; Ethics starts from God's absence (S3).", certainty: 0.5, cites: [{source: S3, locator: "Part I"}], how_known: "Coder's reading."}
  reading: "Secular atheist existentialism; mid_basin false via A 4."
  notes: "Lane B only. Not plotted (B_cause UNKNOWN)."

institutions:
  - {value: "Les Temps modernes (co-founder and editor, 1945)", role: editor, kind: other, certainty: 0.7, cites: [{source: S1, locator: "paragraph 2"}], how_known: "Britannica."}
collaborators:
  - {value: "Jean-Paul Sartre", relation: collaborator, certainty: 0.7, cites: [{source: S1, locator: "paragraph 2"}], how_known: "Lifelong association."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 72"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Ethics quotations from unofficial marxists.org Frechtman web copy (0.7 cap)."
    - "Memoirs and All Said and Done quotations are secondary; IA borrow 401 — primary page check pending."
  open_questions:
    - "Borrow Memoirs of a Dutiful Daughter (IA memoirsofdutiful00beau) for page images of the God-summoning passage; Force of Circumstance 'God had died when I was fourteen'."
    - "Check Ethics Frechtman wording against Philosophical Library 1948 or Open Road edition."
    - "Read Pyrrhus et Cinéas (1944) for earlier locus evidence; Second Sex biology chapters only if a P16 nature-order remark appears (unlikely)."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Simone de Beauvoir.\" Encyclopaedia Britannica, updated 11 September 2026. https://www.britannica.com/biography/Simone-de-Beauvoir. Top Questions body also read via Wayback."
    url: "https://www.britannica.com/biography/Simone-de-Beauvoir"
    accessed: 2026-10-24
    reliability_note: "Unsigned editors' body; Top Questions cited for Ethics among notable works. Live fetch thin 2026-10-24; Wayback used for Top Questions."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: encyclopedia
    author: "Debra Bergoffen and Megan Burke"
    citation: "Bergoffen, Debra, and Megan Burke. \"Simone de Beauvoir.\" Stanford Encyclopedia of Philosophy, substantive revision 11 January 2023. https://plato.stanford.edu/entries/beauvoir/."
    url: "https://plato.stanford.edu/entries/beauvoir/"
    accessed: 2026-10-24
    reliability_note: "Signed scholarly entry."
    source_quality: "reference entry"
    used_for: [basics, childhood, worldview, heritage, timing, contribution]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Simone de Beauvoir"
    citation: "Beauvoir, Simone de. The Ethics of Ambiguity. 1947. Trans. Bernard Frechtman. New York: Philosophical Library, 1948. Marxists Internet Archive web copy, Parts I–III. https://www.marxists.org/reference/subject/ethics/de-beauvoir/ambiguity/ch01.htm."
    url: "https://www.marxists.org/reference/subject/ethics/de-beauvoir/ambiguity/ch01.htm"
    accessed: 2026-10-24
    reliability_note: "Web transcription of the Frechtman translation; 0.7 cap until checked against a publisher edition."
    source_quality: "unofficial web copy"
    used_for: [worldview, timing, lane_b]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S5
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. \"Simone de Beauvoir.\" Wikipedia, English. https://en.wikipedia.org/wiki/Simone_de_Beauvoir."
    url: "https://en.wikipedia.org/wiki/Simone_de_Beauvoir"
    accessed: 2026-10-24
    reliability_note: "P50 dual bio with Britannica. Used for Religious upbringing (communion, nun aspiration, lifelong atheist) and All Said and Done p. 478 citation trail. Not sole warrant for A."
    source_quality: "reference entry"
    used_for: [childhood, heritage, worldview]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Simone de Beauvoir"
    citation: "Beauvoir, Simone de. Memoirs of a Dutiful Daughter. 1958. English translation. Long quotation of the Jockey / mysticism God-summoning passage as printed in W. Scott Haine interview, \"French Impressions…\" A Woman's Paris, 11 February 2014. http://barbararedmond.com/2014/02/11/french-impressions-w-scott-haine-on-the-origins-of-simone-de-beauvoirs-cafe-life-and-the-entry-of-france-into-wwii-part-one/."
    url: "http://barbararedmond.com/2014/02/11/french-impressions-w-scott-haine-on-the-origins-of-simone-de-beauvoirs-cafe-life-and-the-entry-of-france-into-wwii-part-one/"
    accessed: 2026-10-24
    reliability_note: "Primary autobiography; wording verified only as secondary quotation in Haine 2014. IA identifiers memoirsofdutiful00beau etc. returned 401 on download. Primary page check pending."
    source_quality: "primary / own words"
    used_for: [childhood, worldview]
  - id: S7
    type: primary
    kind: other
    author: "Simone de Beauvoir; Madeleine Gobeil (interviewer)"
    citation: "de Beauvoir, Simone. \"The Art of Fiction No. 35.\" Interview by Madeleine Gobeil. The Paris Review, no. 34, Spring–Summer 1965. https://www.theparisreview.org/interviews/4444/the-art-of-fiction-no-35-simone-de-beauvoir."
    url: "https://www.theparisreview.org/interviews/4444/the-art-of-fiction-no-35-simone-de-beauvoir"
    accessed: 2026-10-24
    reliability_note: "Published interview transcript; own words on loss of religious faith."
    source_quality: "newspaper interview"
    used_for: [worldview]
  - id: S8
    type: primary
    kind: "published work by the subject"
    author: "Simone de Beauvoir"
    citation: "Beauvoir, Simone de. All Said and Done. Trans. Patrick O'Brian. New York: G. P. Putnam's Sons, 1974, p. 478. Wording as cited on Wikipedia \"Simone de Beauvoir\" (Religious upbringing) and Goodreads quote 8995381."
    url: "https://en.wikipedia.org/wiki/Simone_de_Beauvoir"
    accessed: 2026-10-24
    reliability_note: "Primary autobiography; page/wording from secondary citation trail (Wikipedia/Goodreads). IA allsaiddone00beau returned 401. Primary page check pending."
    source_quality: "primary / own words"
    used_for: [worldview]
---

# Simone de Beauvoir

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Simone de Beauvoir (1908–1986), French existentialist philosopher, novelist and feminist [S1, S2]. Deepen D1: primary_system EXIST (0.5, alt ATHE); **A 4 at 0.7** (corroborated); B UNKNOWN; **mid_basin false** at 0.7. Not plotted (B UNKNOWN).

## Life and work

Sorbonne; teaching 1931–43; Les Temps modernes [S1].

## Contribution and impact

L'Invitée (1943); The Ethics of Ambiguity (1947) [S1, S2]; The Second Sex (1949); The Mandarins (1954) [S1].

## Childhood and education

Catholic upbringing; rejected God at fourteen [S2, S6]. Communion three times a week at age 7; intended to become a nun [S5].

## Adult working worldview

Ethics: 'far from God’s absence authorizing all license, the contrary is the case' [S3]. Memoirs: 'I was very glad He didn't exist' [S6]. All Said and Done: atheist who 'confronts honestly' vs faith as evasion [S8]. Paris Review: vocation accentuated by lost religious faith [S7].

## Heritage (context only)

Catholic, bourgeois [S2].

## Timing

First lasting contribution 1943, at 35 [S1]. Ethics 1947 during 1943–1954 span.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle [S3]. B_cause UNKNOWN (no P16 nature-order statement).

## Open questions

- Memoirs / Force of Circumstance / All Said and Done page images (IA borrow).
- Frechtman Ethics against a publisher edition.
- Pyrrhus et Cinéas; Second Sex only if a nature-order remark appears.

## Research log

- 2026-10-15: Read Britannica (Editors), SEP (Bergoffen and Burke) and The Ethics of Ambiguity Part I.
- 2026-10-24: Deepen D1. Re-read Ethics Parts I–III (marxists.org). SEP and Wikipedia dual bio. Memoirs quotation via Haine 2014 (IA 401). Paris Review 1965. All Said and Done p. 478 via Wikipedia/Goodreads. A 4 → 0.7; mid_basin → false; B stays UNKNOWN. Chart-moving NO.
