---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch T; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to economics. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch T, order P32: F 4, rank 111). Basics from Britannica (Britannica Editors, unsigned; body only). Worldview from 'My Early Beliefs' (read to the Memoir Club 9 September 1938; published 1949; Collected Writings vol. 10, pp. 433–450), read in an excerpt web copy with CW page numbers. Not a scientist (P30). primary_system BELOW_THRESHOLD; A BELOW_THRESHOLD; B UNKNOWN (P16, P19); C, E UNKNOWN; D BELOW_THRESHOLD; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit notes for batch T (blind audit of 754bb24, run 1): S2 kind 'published work by the subject' -> other (read to a private club in 1938, published only in 1949), matching the statements' kind 'unpublished manuscript'; verified_against 'scholarly edition' -> 'primary transcription' (an unofficial excerpt web copy, not the printed volume). No value changes."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #110 / F4 rank 111). Goals: keep A/B honest; unlikely to plot without clear A and P16 B. Re-opened My Early Beliefs excerpt web copy (S2; CW 10 pp. 433–450 numbers); Internet Archive 1949 Two Memoirs print-disabled this pass (CW 10 print/OCR not checked). Added Wikipedia EN (S5) dual bio (P50); Economic Possibilities for our Grandchildren 1930 (S6, Economics Network text of Nation & Athenæum essays); Treatise on Probability 1921 Uniformity/atomic-law chapters via djmarsay excerpt of Gutenberg-available text (S7) as negative P16 check. P47 source_quality on every source. A stays BELOW_THRESHOLD: Moore ethics as 'religion' ≠ theistic code; no own-voice locus on God's existence or place; secondary atheist/agnostic labels (Wikipedia / biographers) are leads only. B stays UNKNOWN (P16/P30): not a scientist; Treatise Uniformity of Nature / atomic character of natural law is inductive-logic analysis of scientists' assumptions, not a worldview profession of nature's order; Economic Possibilities 'evolved by nature' / 'bounty of nature' / return to 'principles of religion' is economic-ethical rhetoric, not P16 lawfulness. Childhood/heritage: Congregational household (S5); mother Florence Ada Keynes named. Chart: still unplotted. No fallacy_catalog. No figures/. Draft, not reviewed."}

identity:
  id: keynes-john-maynard
  display_name: "John Maynard Keynes"
  roster:
    canonical_name: "John Maynard Keynes"
    rank: 111
    F: 4
    models: [Claude, DeepSeek, Gemini, GPT]
    band: "core (3–4)"
    status: core
    field: economics
    field_bucket: "social science"
  full_name: {value: "John Maynard Keynes", certainty: 1.0, cites: [{source: S1, locator: "title; opening"}, {source: S5, locator: "lead; infobox"}], how_known: "Britannica + Wikipedia (P50 dual bio)."}
  native_name: {value: "John Maynard Keynes", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "English; same as the display name."}
  aliases:
    - {name: "John-Maynard-Keynes", kind: "roster alias"}
    - {name: "Keynes-John Maynard", kind: "roster alias"}
    - {name: "J. M. Keynes", kind: other}
    - {name: "Baron Keynes", kind: "title or honorific"}

basics:
  birth:
    date: {value: "1883-06-05", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "facts box (Born)"}, {source: S5, locator: "infobox"}], how_known: "Britannica + Wikipedia."}
    place: {value: "Cambridge, Cambridgeshire, England", modern_name: "Cambridge, United Kingdom", polity_then: "United Kingdom", certainty: 1.0, cites: [{source: S1, locator: "facts box (Born)"}, {source: S5, locator: "infobox"}], how_known: "Britannica + Wikipedia."}
  death:
    date: {value: "1946-04-21", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "facts box (Died)"}, {source: S5, locator: "infobox"}], how_known: "Britannica + Wikipedia."}
    place: {value: "Firle, Sussex", modern_name: "Firle, East Sussex, United Kingdom", polity_then: "United Kingdom", certainty: 1.0, cites: [{source: S1, locator: "facts box (Died)"}, {source: S5, locator: "infobox; Death"}], how_known: "Britannica + Wikipedia (Tilton near Firle)."}
  first_lasting_contribution_year: {value: 1919, certainty: 0.5, cites: [{source: S1, locator: "Background and early career"}], how_known: "The Economic Consequences of the Peace (1919), whose 'permanent importance' Britannica names. Alternative 1913: Indian Currency and Finance, 'his first major work ... a definitive examination' (S1), not called lasting; coder's call, so 0.5."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "Background and early career"}], how_known: "1919 (P2); 1913 gives the same bucket."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "facts box"}], how_known: "United Kingdom (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "Key contributions"}], how_known: "Cambridge and London."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "works named"}], how_known: "Britannica."}
  occupations: {value: ["economist", "journalist", "financier", "civil servant (India Office, Treasury)", "fellow of King's College, Cambridge"], certainty: 0.7, cites: [{source: S1, locator: "opening; Background and early career; Later works"}], how_known: "Britannica."}

contribution:
  primary_domain: economics
  fields: {value: ["economics"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "The Economic Consequences of the Peace: analysis of the Versailles reparations", year: 1919, kind: work, lasting: "'The permanent importance of this polemical essay lies in its economic analysis of the stringent reparations' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Background and early career"}], how_known: "Britannica."}
    - {value: "The General Theory of Employment, Interest and Money: theory of prolonged unemployment and government-sponsored full employment (Keynesian economics)", year: 1936, kind: theory, lasting: "'one of the most influential economics books in history' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; Key contributions"}], how_known: "Britannica dates it 1935–36; 1936 is the publication year. The latest listed lasting contribution (P30 addendum b): 'The General Theory was Keynes's last major written work' (S1). A theory of society, not of physical or natural systems, so not a scientist (P30)."}
  evidence_of_impact:
    - {value: "The Keynesian model 'was a core part of economics textbooks from the late 1940s until the late 1980s'", kind: "standard textbook canon", certainty: 0.7, cites: [{source: S1, locator: "Later works and assessment"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Congregational (Nonconformist Protestant)", certainty: 0.7, cites: [{source: S5, locator: "Early life and education (attended a Congregational Church; Skidelsky p. 14 cite)"}], how_known: "Wikipedia summarizing Skidelsky; father's family Congregationalist Nonconformist tradition (heritage context)."}
  family_religious_practice: {value: "Attended Congregational Church; loving attentive household", certainty: 0.7, cites: [{source: S5, locator: "Early life and education"}], how_known: "Wikipedia / Skidelsky via Wikipedia."}
  parents_and_household:
    - {value: "Father: John Neville Keynes, economist and academic administrator at Cambridge", certainty: 0.7, cites: [{source: S1, locator: "Background and early career"}, {source: S5, locator: "Early life"}], how_known: "Britannica + Wikipedia."}
    - {value: "Mother: Florence Ada Keynes (née Brown), social reformer; later mayor of Cambridge; one of the first female graduates of Cambridge", certainty: 0.7, cites: [{source: S1, locator: "Background and early career"}, {source: S5, locator: "Early life"}], how_known: "Britannica (unnamed in body previously) + Wikipedia names her."}
  household_circumstances: {value: "Moderately prosperous upper-middle-class academic family", certainty: 0.7, cites: [{source: S1, locator: "Background and early career"}, {source: S5, locator: "Early life"}], how_known: "Britannica + Wikipedia."}
  schooling:
    - {value: "Perse School for Girls kindergarten (from 1889); St Faith's preparatory school (from 1892)", stage: "elementary school", run_by: other, years: "1889–1897", certainty: 0.7, cites: [{source: S5, locator: "Early life and education"}], how_known: "Wikipedia."}
    - {value: "Eton College (King's Scholarship, 1897–1902): mathematics, classics, history; Tomline Prize for mathematics 1901", stage: "grammar or secondary school", run_by: other, years: "1897–1902", certainty: 0.7, cites: [{source: S5, locator: "Early life and education"}], how_known: "Wikipedia (Britannica Top Questions box previously unused)."}
    - {value: "King's College, Cambridge, from 1902: B.A. mathematics first class 1904; M.A. 1909; Cambridge Apostles; Marshall turned him to economics", stage: university, run_by: other, years: "1902–1909", certainty: 0.7, cites: [{source: S1, locator: "Background and early career"}, {source: S5, locator: "Early life and education"}], how_known: "Britannica + Wikipedia."}
  early_mathematics: {value: "advanced mathematics", certainty: 0.7, cites: [{source: S1, locator: "Background and early career"}, {source: S5, locator: "Early life (BA mathematics; Tomline Prize)"}], how_known: "Mathematics BA; Marshall moved his interests from mathematics and the classics to economics (S1)."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading:
    - {value: "G. E. Moore, Principia Ethica (1903)", certainty: 0.7, cites: [{source: S2, locator: "p. 435"}], how_known: "His memoir."}
  childhood_mentors: []
  languages_in_childhood: {value: ["English"], certainty: 0.5, cites: [{source: S1, locator: "facts box"}], how_known: "Coder's reading."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1919–1936", certainty: 0.5, cites: [{source: S1, locator: "Background and early career; Key contributions"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Moore's ethics as a 'religion' ('one’s attitude towards oneself and the ultimate'), regarded at the time 'as entirely rational and scientific in character'; 'It is still my religion under the surface' (1938)", certainty: 0.5, cites: [{source: S2, locator: "pp. 435, 437, 441–442"}], how_known: "Memoir read to a private club in 1938, after the working years (P1 cap 0.5); an excerpt web copy. Moore ethics ≠ theistic code."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "Deepen D1: still no own-voice statement on God's existence or nature in S2 My Early Beliefs (full excerpt re-opened), S6 Economic Possibilities (return to 'principles of religion and traditional virtue' = avarice/usury ethics, not a theistic system), or S7 Treatise. His 'religion' is Moore's ethics of good states of mind / neo-Platonism of states of mind, not ATHE/AGNOS/SECHUM/CHRIST. Christians were 'the enemy' as 'representatives of tradition, convention and hocus-pocus' then retracted toward Benthamism (S2, p. 445) — group early view, not a denial of God. Wikipedia/biographer secondary labels (atheist / ferocious agnostic / Cambridge Heretics) are leads, not scored evidence of a positive code (P19)."}
  secondary_system: {value: UNKNOWN, how_known: "One system (P29)."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Rejected: no denial of God read in his words. Secondary 'said to be an atheist' (S5) is a lead."}
    - {code: AGNOS, reason: "Rejected: no stated suspension read in own voice (biographer 'ferocious agnostic' / Cambridge University 'agnostic' via S5 are secondary)."}
    - {code: SECHUM, reason: "Rejected: an ethic of private goods; public identity was not the humanist movement (Cambridge Heretics association via S5 is secondary lead only)."}
    - {code: CHRIST, reason: "Rejected: Christians as early 'enemy'; Moore religion unworldly vs New Testament; Congregational childhood is heritage (P20)."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Deepen D1 re-check (S2 full excerpt; S5 Philosophical and spiritual views; S6): no locus view in own words. 'Our Ideal was a merciful God' (S2, p. 441) describes Moore's ethical Ideal (vindictive punishment hedged), a figure of speech. 'Return to … principles of religion and traditional virtue' (S6) is about avarice/usury/love of money as vices, not where God is. Secondary atheist/agnostic reports (S5) are leads. Evidence of Moorean 'religion' and hostility to Christian convention bears on ethics, not A_locus at ≥0.5 (P19).", note: "Moore ethics ≠ theistic code; no scored locus."}
    B_cause: {value: UNKNOWN, how_known: "Deepen D1: not a scientist (P30) — lasting contributions are economics (Versailles analysis; General Theory of employment), not theories about physical or natural systems. For a non-scientist, B needs an explicit own-voice remark on the order of nature (P16). Checked and off-point (P19): (1) S2 My Early Beliefs — nothing on nature/physical law; (2) S7 Treatise on Probability ch. XIX/XXI — 'Uniformity of Nature' and 'atomic character of natural law' analyse inductive assumptions scientists 'appear commonly to act' on ('if this kind of assumption is warranted'; 'nature might still be uniform' as hypothetical); meta-epistemology of induction, not a worldview profession that nature is lawful; (3) S6 Economic Possibilities — 'expressly evolved by nature', 'bounty of nature', science and technical inventions — economic-historical rhetoric, not a stated general lawfulness vs exception. Coder's call: UNKNOWN, not BELOW_THRESHOLD (nothing scored that bears on B at any strength)."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing on reward and punishment of persons; Moore's 'vindictive punishment' (S2, p. 441) is Moore's view, not his. S6 ethics of avarice is virtue ethics, not personal afterlife ledger (P19)."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "Lead only: 'We used to regard the Christians as the enemy, because they appeared as the representatives of tradition, convention and hocus-pocus' (S2, p. 445) describes the group's early view and is retracted in the same sentence ('In truth it was the Benthamite calculus ...'); it is not a statement on revelation against observation. After the working years in any case (P1). No stronger D statement in S6/S7."}
    E_scope: {value: UNKNOWN, how_known: "Not a scientist; nothing on same laws everywhere (P7/P19). Treatise uniformity discussion is about inductive relevance of time/space position, not E's in-group exceptions test."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN, which takes precedence for the P4 test (§6, P19); A is also BELOW_THRESHOLD."}
  statements:
    - text: "It seems to me looking back, that this religion of ours was a very good one to grow up under. It remains nearer the truth than any other that I know, with less irrelevant extraneous matter and nothing to be ashamed of"
      cites: [{source: S2, locator: "pp. 441–442"}]
      date: "1938-09-09"
      context: "'My Early Beliefs', a paper read to the Memoir Club at Tilton, defending the Cambridge circle of 1902–14 against D. H. Lawrence; the 'religion' is Moore's ethics. The passage ends 'It is still my religion under the surface.'"
      axes: []
      kind: "unpublished manuscript"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Unpublished in his lifetime (read to a private club in 1938; first published 1949), hence the kind. Read in an unofficial web copy of an anthology excerpt that keeps the Collected Writings vol. 10 page numbers, with cuts marked '…'; not checked against the printed CW 10 or 1949 Two Memoirs (IA print-disabled this pass), so 'primary transcription', not 'scholarly edition'."
    - text: "We used to regard the Christians as the enemy, because they appeared as the representatives of tradition, convention and hocus-pocus. In truth it was the Benthamite calculus, based on an over-valuation of the economic criterion, which was destroying the quality of the popular Ideal."
      cites: [{source: S2, locator: "p. 445"}]
      date: "1938-09-09"
      context: "Same paper. Group early view, then retracted toward Benthamism as the real enemy."
      axes: [D_authority]
      kind: "unpublished manuscript"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "As above. Lead for D only; keeps D BELOW_THRESHOLD."
    - text: "I see us free, therefore, to return to some of the most sure and certain principles of religion and traditional virtue—that avarice is a vice, that the exaction of usury is a misdemeanour, and the love of money is detestable"
      cites: [{source: S6, locator: "part II (near end)"}]
      date: "1930"
      context: "Economic Possibilities for our Grandchildren (Nation & Athenæum, Oct. 1930). Future ethics after the economic problem is solved; avarice/usury/precaution must remain 'our gods' until then. Not a theistic locus or nature-order claim."
      axes: []
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Economics Network HTML of the 1930 essays; not checked against Essays in Persuasion print. Supporting context for primary_system BELOW (religion = virtue ethics here)."
    - text: "The law of the Uniformity of Nature appears to me to amount to an assertion … of a generalised judgment of irrelevance, namely, of the irrelevance of mere position in time and space to generalisations which have no reference to particular positions in time and space."
      cites: [{source: S7, locator: "ch. XIX (djmarsay excerpt of Treatise)"}]
      date: "1921"
      context: "A Treatise on Probability, ch. XIX. Inductive-logic analysis of what 'Uniformity of Nature' means for analogy; not a profession that nature is lawful as worldview (P16). Negative check for B."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Quoted via djmarsay blog excerpt of Gutenberg-available Treatise text; Gutenberg #32625 direct fetch blocked this pass. Does not score B (meta-epistemology of induction)."
  changes_over_life: []
  coder_notes: "Coder's call. Deepen D1: A BELOW and B UNKNOWN kept honest — Moore religion ≠ theism; Treatise Uniformity ≠ P16 profession; Economic Possibilities religion-language is virtue ethics. Memoir after working years (1938; P1 cap) and states no view of God. Leads: Skidelsky and Moggridge on his religion (secondary); Wikipedia atheist/agnostic/Heretics labels; letters to Strachey/Grant unread. Not plotted."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Congregational Nonconformist Protestant", certainty: 0.7, cites: [{source: S5, locator: "Early life (Congregational Church; Skidelsky)"}], how_known: "Wikipedia / Skidelsky. Heritage only (P20)."}
  baptism_or_initiation: {value: BELOW_THRESHOLD, how_known: "Wikipedia 'may have been religiously confirmed' (secondary); not verified in a primary. Withheld."}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1919–1936", certainty: 0.5, cites: [{source: S1, locator: "Background and early career; Key contributions"}], how_known: "The Economic Consequences of the Peace (1919) to The General Theory (1936), first to last listed lasting contribution (P29, P30). 0.5: the start is a coder's call (alternative 1913, Indian Currency and Finance)."}
  age_at_first_lasting_contribution: {value: 36, certainty: 0.5, cites: [{source: S1, locator: "facts box; Background and early career"}], how_known: "1919 − 1883 = 36 (P30); 30 with the 1913 alternative."}
  first_evidence_of_lio_type_views: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "pp. 433–450"}, {source: S6, locator: "full essay"}, {source: S7, locator: "ch. XIX–XXI (negative)"}], how_known: "None that score A or B in the sources read (P19)."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "pp. 433–450"}, {source: S6, locator: "full essay"}], how_known: "None that score A or B in the sources read."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "Background and early career"}], how_known: "Mathematics degree; not assessed."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "Background and early career"}], how_known: "Not read."}
  circle_present: {value: "no", rationale: "No God-Nature identity read.", certainty: 0.5, cites: [{source: S2, locator: "pp. 433–450"}], how_known: "Coder's reading."}
  reading: "A Moorean ethic of good states of mind called a 'religion', with no stated theology; later essay returns to 'principles of religion' as virtue ethics against avarice. Treatise discusses Uniformity of Nature as inductive logic, not pantheism or exceptionless nature."
  notes: "Belief model only. Not plotted."

institutions:
  - {value: "King's College, Cambridge", role: fellow, years: "1909–1946", kind: university, certainty: 0.7, cites: [{source: S1, locator: "Key contributions"}, {source: S5, locator: "Career"}], how_known: "Britannica + Wikipedia."}
  - {value: "HM Treasury", role: "adviser (World War I and II)", years: "1915–1919; 1940–1946", kind: "government or state body", certainty: 0.5, cites: [{source: S1, locator: "Background and early career; Later works"}], how_known: "Britannica; years partly the coder's."}
  - {value: "Bank of England", role: "director (Court)", years: "1941–1946", kind: "government or state body", certainty: 0.7, cites: [{source: S5, locator: "Second World War"}], how_known: "Wikipedia."}
collaborators:
  - {value: "Alfred Marshall", relation: teacher, note: "turned his interests to economics", certainty: 0.7, cites: [{source: S1, locator: "Background and early career"}], how_known: "Britannica."}
  - {value: "G. E. Moore", relation: "influenced by", note: "Principia Ethica as 'our religion'", certainty: 0.7, cites: [{source: S2, locator: "pp. 435–442"}], how_known: "His memoir."}
  - {value: "Lytton Strachey", relation: "other", note: "introduced him to 'the Society' (the Apostles)", certainty: 0.7, cites: [{source: S1, locator: "Background and early career"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 111"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Britannica article unsigned (Britannica Editors)."
    - "Worldview source My Early Beliefs is a 1938 memoir read in an excerpt web copy; after the working years; CW 10 / 1949 Two Memoirs print not checked (IA print-disabled)."
    - "Treatise Uniformity passages via djmarsay secondary quotation; Gutenberg direct fetch blocked this pass."
  open_questions:
    - "CW vol. 10 print/OCR or 1949 Two Memoirs for My Early Beliefs page-check (lift verified_against)."
    - "Letters (Strachey, Grant) and Skidelsky vols for any own-voice God denial or nature-order profession."
    - "Baptism / confirmation primary evidence."
    - "Essays in Persuasion print check for Economic Possibilities."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"John Maynard Keynes.\" Encyclopaedia Britannica (updated 29 September 2026). https://www.britannica.com/money/John-Maynard-Keynes. Read live 2026-10-19; reopened 2026-10-24 (fetch timeout on reopen — prior body retained)."
    url: "https://www.britannica.com/money/John-Maynard-Keynes"
    accessed: 2026-10-24
    reliability_note: "Unsigned article. Body and facts box only; the AI-generated question boxes are not cited."
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, collaborators]
    source_quality: "reference entry"
  - id: S2
    type: primary
    kind: other
    author: "John Maynard Keynes"
    citation: "Keynes, John Maynard. 'My Early Beliefs' (read to the Memoir Club, Tilton, 9 September 1938; first published in Two Memoirs, 1949). The Collected Writings of John Maynard Keynes, vol. 10, pp. 433–450. Excerpt read at https://neilhacker.com/wp-content/uploads/2021/01/my-early-beliefs.pdf (full excerpt reopened 2026-10-24)."
    url: "https://neilhacker.com/wp-content/uploads/2021/01/my-early-beliefs.pdf"
    accessed: 2026-10-24
    reliability_note: "Unofficial web copy of an anthology excerpt (with an editor's headnote and cuts marked '…'), keeping the CW page numbers in brackets; not checked against the printed CW 10 or 1949 Two Memoirs (Internet Archive copy print-disabled this pass). Kind 'other', not 'published work by the subject': a paper read to a private club and published only after his death (1949), consistent with the statements' kind 'unpublished manuscript'."
    used_for: [worldview, childhood, timing, lane_b, collaborators]
    source_quality: "unofficial web copy"
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [identity, review]
    source_quality: "study roster"
  - id: S5
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"John Maynard Keynes.\" English Wikipedia. https://en.wikipedia.org/wiki/John_Maynard_Keynes. Read live 2026-10-24 (lead, infobox, Early life and education, Philosophical and spiritual views, Death)."
    url: "https://en.wikipedia.org/wiki/John_Maynard_Keynes"
    accessed: 2026-10-24
    reliability_note: "Tertiary; used for dual bio (P50) and childhood/heritage leads (Congregational; mother named; Eton). Secondary atheist/agnostic/Heretics labels are leads only, not scored as worldview."
    used_for: [identity, basics, childhood, heritage, institutions, worldview]
    source_quality: "reference entry"
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "John Maynard Keynes"
    citation: "Keynes, John Maynard. \"Economic Possibilities for our Grandchildren.\" The Nation and Athenæum, 11 and 18 October 1930. HTML at https://www.economicsnetwork.ac.uk/archive/keynes_persuasion/Economic_Possibilities_for_our_Grandchildren.htm (Economics Network archive of Essays in Persuasion text). Read 2026-10-24."
    url: "https://www.economicsnetwork.ac.uk/archive/keynes_persuasion/Economic_Possibilities_for_our_Grandchildren.htm"
    accessed: 2026-10-24
    reliability_note: "Published 1930 essay (inside working years). Web HTML of the essay text; Essays in Persuasion print check pending."
    used_for: [worldview, timing]
    source_quality: "unofficial web copy"
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "John Maynard Keynes"
    citation: "Keynes, John Maynard. A Treatise on Probability (Macmillan, 1921), ch. XIX–XXI (Uniformity of Nature; atomic character of natural law). Passages as excerpted at https://djmarsay.wordpress.com/mathematics/maths-subjects/uncertainty-maths/broader-uncertainty/keynes-treatise-on-probability/keynes-on-the-principle-of-uniformity-from-his-treatise/ (djmarsay). Gutenberg ebook #32625 exists; direct fetch blocked this pass. Read 2026-10-24."
    url: "https://djmarsay.wordpress.com/mathematics/maths-subjects/uncertainty-maths/broader-uncertainty/keynes-treatise-on-probability/keynes-on-the-principle-of-uniformity-from-his-treatise/"
    accessed: 2026-10-24
    reliability_note: "Primary work; wording verified only via secondary web excerpt of Gutenberg-available chapters. Used as negative P16 check for B (inductive logic, not worldview profession). Gutenberg locator TODO if print pages needed."
    used_for: [worldview, timing]
    source_quality: "unofficial web copy"
---

# John Maynard Keynes

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

John Maynard Keynes (1883–1946), English economist [S1][S5]. Deepen D1: primary_system BELOW_THRESHOLD; A BELOW_THRESHOLD; B UNKNOWN; D BELOW_THRESHOLD; C, E UNKNOWN; mid_basin UNKNOWN. Not plotted. Moore ethics as 'religion' ≠ theistic code; no P16 nature-order profession in Treatise Uniformity analysis or Economic Possibilities [S2][S6][S7].

## Life and work

Cambridge academic family; Congregational Nonconformist household; Eton and King's College, Cambridge; India Office, Treasury, Bank of England [S1][S5].

## Contribution and impact

The Economic Consequences of the Peace (1919) to The General Theory (1936) [S1]. Not a scientist under P30 (economics of society, not physical/natural systems).

## Childhood and education

Congregational church attendance; Perse / St Faith's / Eton / King's; Moore Principia Ethica [S5][S2].

## Adult working worldview

Moore's ethics as 'still my religion under the surface' [S2, p. 442]. Economic Possibilities (1930) returns to 'principles of religion and traditional virtue' as anti-avarice ethics [S6]. Treatise (1921) Uniformity of Nature = inductive irrelevance judgment, not scored B [S7]. No own-voice God locus [S2][S5][S6].

## Heritage (context only)

English; Congregational Nonconformist by birth [S1][S5].

## Timing

1919–1936, from age 36 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Moorean ethic called a religion; no theology; no God=Nature circle [S2][S6][S7].

## Open questions

- CW 10 / Two Memoirs print check for My Early Beliefs.
- Letters and Skidelsky for own-voice God or nature-order statements.
- Baptism/confirmation primary.

## Research log

- 2026-10-19: Read Britannica (live) and the excerpt of 'My Early Beliefs' (CW 10).
- 2026-10-24 deepen D1: Reopened S2 full excerpt; Wikipedia (S5); Economic Possibilities (S6); Treatise Uniformity via djmarsay (S7). IA Two Memoirs print-disabled; Gutenberg Treatise fetch blocked. A BELOW / B UNKNOWN kept. No figures/. No fallacy_catalog.
