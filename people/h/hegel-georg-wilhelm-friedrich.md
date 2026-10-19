---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Q)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-18
  last_updated: 2026-10-18
  change_log:
    - {date: 2026-10-18, by: "Grok Bot", summary: "Record created (stage 3 batch Q, order P32: F 4, rank 98). Basics from Britannica (T. Malcolm Knox, signed; body through 'Early life', read live) and SEP 'Hegel' (Paul Redding, revision of 19 September 2025). Worldview from the Encyclopaedia (3rd ed. 1830) in Wallace's translations (Philosophy of Mind §§564–565, §573 Remark; Logic §16 Remark), Project Gutenberg web copies; the Lectures on the History of Philosophy (Michelet's compiled edition, Haldane trans.) as context. Not a scientist (P30). primary_system IDEAL (0.5, alt PANENT, CHRIST); A 3 (0.5, alt 2); B BELOW_THRESHOLD (alt 3); D 3 (0.5, alt 2); mid_basin BELOW_THRESHOLD. Not plotted. Draft, not reviewed."}

identity:
  id: hegel-georg-wilhelm-friedrich
  display_name: "Georg Wilhelm Friedrich Hegel"
  roster:
    canonical_name: "Georg Wilhelm Friedrich Hegel"
    rank: 98
    F: 4
    models: [Claude, Gemini, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Georg Wilhelm Friedrich Hegel", certainty: 0.7, cites: [{source: S1, locator: "title and opening"}], how_known: "Britannica."}
  native_name: {value: UNKNOWN, how_known: "German; same as full name."}
  aliases:
    - {name: "G. W. F. Hegel", kind: other}

basics:
  birth:
    date: {value: "1770-08-27", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "§1 (year)"}], how_known: "Britannica gives the day; SEP agrees on 1770 and Stuttgart."}
    place: {value: "Stuttgart, Württemberg", modern_name: "Stuttgart, Germany", polity_then: "Duchy of Württemberg (Holy Roman Empire)", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "§1"}], how_known: "Britannica and SEP."}
  death:
    date: {value: "1831-11-14", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "§1 (year)"}], how_known: "Britannica; SEP gives 1831."}
    place: {value: "Berlin", modern_name: "Berlin, Germany", polity_then: "Kingdom of Prussia", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1807, certainty: 0.7, cites: [{source: S2, locator: "§1; §2 (corpus)"}, {source: S4, locator: "Bibliographical Notice"}], how_known: "Phenomenology of Spirit, published 1807 (SEP; Wallace's notice)."}
  era_bucket: {value: "1750 to 1849", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "First lasting year 1807 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Germany (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "Jena, Bamberg, Nuremberg, Heidelberg, Berlin."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["German"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  occupations: {value: ["philosopher", "university professor", "gymnasium headmaster", "newspaper editor"], certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP."}

contribution:
  fields: {value: ["metaphysics", "logic", "philosophy of history", "political philosophy", "philosophy of religion"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "§§2–3"}], how_known: "Britannica and SEP."}
  lasting_original_contributions:
    - {value: "Phenomenology of Spirit", year: 1807, kind: work, lasting: "his 'first major work' (S2)", certainty: 0.7, cites: [{source: S2, locator: "§1"}, {source: S4, locator: "Bibliographical Notice"}], how_known: "SEP and Wallace agree on 1807."}
    - {value: "Science of Logic (three books)", year: "1812–1816", kind: work, lasting: "one of 'Hegel's two major stand-alone books' (S2)", certainty: 0.7, cites: [{source: S2, locator: "§2; §5 ('appeared in 1812, 1813, and 1816')"}], how_known: "SEP."}
    - {value: "Encyclopaedia of the Philosophical Sciences", year: 1817, kind: work, lasting: "'the only complete, matured, and authentic statement of Hegel's philosophical system' (S4)", certainty: 0.7, cites: [{source: S2, locator: "§1"}, {source: S4, locator: "Bibliographical Notice"}], how_known: "SEP; later editions 1827 and 1830 (S3, Preface)."}
    - {value: "Elements of the Philosophy of Right", year: 1821, kind: work, lasting: "'his major work in political philosophy' (S2)", certainty: 0.5, cites: [{source: S2, locator: "§1"}, {source: S4, locator: "Bibliographical Notice"}], how_known: "SEP gives 1821; Wallace's notice gives 1820 (the book appeared before its title-page year). A P25 conflict, so 0.5 with 1820 the named alternative."}
    - {value: "Dialectical system of absolute idealism", kind: "body of work", lasting: "'the last of the great philosophical system builders of modern times' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; undated."}
  evidence_of_impact:
    - {value: "Influence on Kierkegaard, the Marxists, the logical positivists, Moore and Russell (by reaction)", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Son of a revenue officer; learned the elements of Latin from his mother", role: parents, certainty: 0.7, cites: [{source: S1, locator: "Early life"}], how_known: "Britannica."}
  household_circumstances: {value: TODO}
  schooling:
    - {value: "Stuttgart grammar school until 18", stage: "grammar or secondary school", years: "–1788", certainty: 0.7, cites: [{source: S1, locator: "Early life"}], how_known: "Britannica."}
    - {value: "University of Tübingen (philosophy and classics, graduated 1790; then theology to 1793), entered with a view to taking orders, as his parents wished", stage: university, years: "1788–1793", certainty: 0.7, cites: [{source: S1, locator: "Early life"}, {source: S2, locator: "§1"}], how_known: "Britannica and SEP."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["German", "Latin"], certainty: 0.5, cites: [{source: S1, locator: "Early life"}], how_known: "Latin from his mother (Britannica); German is the coder's inference."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1807–1821", certainty: 0.5, cites: [{source: S2, locator: "§1"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Lutheran ('we Lutherans—I am a Lutheran and will remain the same')", certainty: 0.5, cites: [{source: S5, locator: "Introduction, B.2 (Gutenberg vol. 1)"}], how_known: "Lectures on the History of Philosophy as compiled by Michelet from Hegel's manuscripts and students' notes (2nd ed. 1840); not certain to be his own wording, so context only."}
  self_described_science_religion_relation: {value: "The content of religion and philosophy is the same; philosophy is the cognition of that content in the form of thought", certainty: 0.5, cites: [{source: S3, locator: "§573 Remark"}], how_known: "Encyclopaedia §573 Remark (1830), Wallace's translation, web copy."}
  primary_system:
    value: IDEAL
    basis: written_profession
    certainty: 0.5
    cites: [{source: S1, locator: "opening ('absolute idealist inspired by Christian insights')"}, {source: S3, locator: "§§564–565, §573 Remark"}, {source: S2, locator: "§2.2–2.4"}]
    rationale: "Absolute idealism: God as 'absolute spirit', 'the essential and actual spirit of nature and spirit' (§565), whose self-knowledge is 'his self-consciousness in man' (§564); the being of external things is 'untruth' beside God's 'absolute universality' (§573 Remark). Named alternatives: PANENT (a divine spirit that includes the world and exceeds it; he denies that 'each and every secular thing is God') and CHRIST (he treats Christianity as the absolute, revealed religion and calls himself Lutheran in the compiled lectures). SEP sets out traditional-metaphysical and post-Kantian (non-metaphysical) readings, so the code is contested."
    how_known: "Published work in Wallace's translation via a web copy (secondary quotation, P26); contested reading, 0.5."
  secondary_system: {value: UNKNOWN, how_known: "One published system only (P29)."}
  candidate_codes_considered:
    - {code: IDEAL, reason: "Absolute idealism (S1, S3)."}
    - {code: PANENT, reason: "God's spirit includes and exceeds the world; pantheism denied (§573 Remark)."}
    - {code: CHRIST, reason: "Revealed religion as absolute religion; Lutheran self-label in compiled lectures."}
    - {code: PANT, reason: "Rejected: he denies that everything is God (§573 Remark)."}
  lio_axes:
    A_locus:
      value: 3
      basis: written_profession
      certainty: 0.5
      cites: [{source: S3, locator: "§§564–565, §573 Remark"}, {source: S2, locator: "§2.2"}]
      rationale: "Leans to the immanent pole: 'God is God only so far as he knows himself: his self-knowledge is, further, his self-consciousness in man' (§564, adopting Göschel's propositions); God is 'the essential and actual spirit of nature and spirit' (§565). The stated limit: God is not identical with the world; he mocks the charge that his philosophy holds 'each and every secular thing is God' (§573 Remark). Named alternative 2: the revealed, triune God of §§564–571 can be read as a personal God beyond the world (mixed). SEP: on the traditional reading 'the mind of God becomes actual only via its particularization in the minds of \"his\" finite material creatures'; post-Kantian readers deny the metaphysics."
      how_known: "Encyclopaedia (1830) in Wallace's translation, web copy; contested reading, 0.5."
      alternatives:
        - {value: 2, note: "Revealed triune God as a person beyond the world (§§564–571).", cites: [{source: S3, locator: "§§564–565"}]}
    B_cause:
      value: BELOW_THRESHOLD
      basis: written_profession
      cites: [{source: S4, locator: "§16 Remark"}, {source: S5, locator: "Introduction, B.2"}]
      how_known: "Not a scientist (P30); his account of nature (P16) bears on the axis only indirectly. The Encyclopaedia says 'the Idea of Nature, when parcelled out in detail, is dissipated into contingencies' whose kinds 'are not determined by reason, but by sport and adventitious incidents' (Logic §16 Remark): contingency in the detail of nature, which is neither a lawful order with no exceptions nor intervention. The compiled lectures say 'Christ reproved the Pharisees for wishing to see miracles' and 'if the miracle be the suspension of natural laws, Spirit itself is the real miracle in the operations of nature', which reinterprets miracle without denying it, and is a compiled lecture text. No stated lawful order and no rejection of miracles in his own published text read, so neither P41 nor the P16 addendum applies (P19)."
      note: "Named alternative 3 at 0.5 (P41 extension) if the lecture's reinterpretation of miracle is read as a rejection in his own words."
      alternatives:
        - {value: 3, note: "Miracle reinterpreted as spirit (compiled lectures), P41 extension.", cites: [{source: S5, locator: "Introduction, B.2"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing scored at this reading."}
    D_authority:
      value: 3
      basis: written_profession
      certainty: 0.5
      cites: [{source: S3, locator: "§573 and Remark"}]
      rationale: "Speculative reason outranks revelation's form but keeps its content: philosophy is 'the cognition of the necessity in the content of the absolute picture-idea' and of 'the objective and external revelation presupposed by representation', its 'liberation from the one-sidedness of the forms'; 'the content of religion and philosophy is the same'. Revelation keeps one stated point, its content, which philosophy recognises and 'does not disparage'. Named alternative 2: 'religion is the truth for all men', read as a domain of its own. Coder's reading."
      how_known: "Encyclopaedia (1830), Wallace's translation via a web copy; 0.5."
      alternatives:
        - {value: 2, note: "Religion as 'the truth for all men' in its own form.", cites: [{source: S3, locator: "§573 Remark"}]}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 3 is at 0.5, under the 0.7 the A ≥ 3 branch needs (P10), and B is BELOW_THRESHOLD (P19)."}
  statements:
    - text: "God is God only so far as he knows himself: his self-knowledge is, further, his self-consciousness in man, and man’s knowledge of God, which proceeds to man’s self-knowledge in God."
      cites: [{source: S3, locator: "§564 Remark (Gutenberg)"}]
      date: "1830"
      context: "Encyclopaedia, 3rd ed. (1830), Philosophy of Mind §564 Remark, adopting propositions from Göschel's Aphorismen (1829); Wallace's translation."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "Web copy of Wallace (1894); check against the German (GW 20) pending."
    - text: "and so—thus he understands philosophy—each and every secular thing is God. It is only his own stupidity, and the falsifications due to such misconception, which generate the imagination and the allegation of such pantheism."
      cites: [{source: S3, locator: "§573 Remark (Gutenberg)"}]
      date: "1830"
      context: "Encyclopaedia (1830) §573 Remark, rejecting the charge of pantheism."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "As above."
    - text: "Similarly the Idea of Nature, when parcelled out in detail, is dissipated into contingencies. Natural history, geography, and medicine stumble upon descriptions of existence, upon kinds and distinctions, which are not determined by reason, but by sport and adventitious incidents."
      cites: [{source: S4, locator: "§16 Remark (Gutenberg)"}]
      date: "1830"
      context: "Encyclopaedia Logic §16 Remark, Wallace's translation (2nd ed. 1892) of the 1830 text."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "Web copy; German check pending."
    - text: "Christ reproved the Pharisees for wishing to see miracles; the Spirit alone comprehends Spirit, the miracle is only a presentiment of that Spirit; and if the miracle be the suspension of natural laws, Spirit itself is the real miracle in the operations of nature."
      cites: [{source: S5, locator: "Introduction, B.2 (Gutenberg vol. 1)"}]
      context: "Lectures on the History of Philosophy, Introduction, as compiled by Michelet (2nd ed. 1840) from Hegel's manuscripts and students' notes from courses of 1805–1830; Haldane's translation. No single year, so the date is left out."
      axes: [B_cause]
      kind: "other"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "Compiled lecture text; whether this sentence is Hegel's own wording is not known (P42 caution); context only."
  changes_over_life:
    - {value: "Early Kantian reading of Christianity as rational morality (Bern, 1790s), later freed from Kant's influence (Frankfurt)", certainty: 0.7, cites: [{source: S1, locator: "Early life"}], how_known: "Britannica; before the span, does not split it (P31)."}
  coder_notes: "Coder's call. B left BELOW_THRESHOLD rather than 3: the only miracle passage is in a compiled lecture text, and his own published remark is about contingency, not exceptions. The Encyclopaedia cites quote the 1830 text; earlier editions (1817) not checked (P30 #7), so first_evidence is capped at 0.5. Britannica's Top Questions and Quick Facts not cited (P26)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German (Württemberg)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1807–1821", certainty: 0.5, cites: [{source: S2, locator: "§1"}], how_known: "Phenomenology (1807) to Philosophy of Right (1821; 1820 per Wallace), P30; 0.5 for the end-year conflict."}
  age_at_first_lasting_contribution: {value: 37, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "§1"}], how_known: "1807 − 1770 = 37 (P30)."}
  first_evidence_of_lio_type_views: {value: "1830: Encyclopaedia 3rd ed., §564 on God's self-consciousness in man", year: 1830, certainty: 0.5, cites: [{source: S3, locator: "§564"}], how_known: "Earliest dated text read with the A 3 view; the 1807 and 1817 texts not read (P30 #7)."}
  lio_views_relative_to_major_work: {value: "unclear", rationale: "The text read is from 1830, after the span; under P31 it counts for the span, but earlier works were not checked.", certainty: 0.5, cites: [{source: S3, locator: "§564"}], how_known: "Coder's reading."}
  worldview_during_major_work: {value: "Absolute idealism with an immanent, self-knowing God (as read in the 1830 Encyclopaedia)", certainty: 0.5, cites: [{source: S3, locator: "§§564–573"}], how_known: "P31 continuity."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not read.", certainty: 0.5, cites: [{source: S1, locator: "Early life"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "Early life"}], how_known: "Not read."}
  circle_present: {value: "partly", rationale: "God knows himself through man's knowledge of God.", certainty: 0.5, cites: [{source: S3, locator: "§564"}], how_known: "Coder's reading."}
  reading: "A self-knowing absolute spirit realised in nature and human mind."
  notes: ""

institutions:
  - {value: "University of Jena", role: "lecturer, then extraordinary professor", years: "1801–1806", kind: university, certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP (moved to Jena 1801; departed after the 1806 occupation)."}
  - {value: "Gymnasium, Nuremberg", role: "headmaster and philosophy teacher", years: "1808–1815", kind: employer, certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP."}
  - {value: "University of Heidelberg", role: "chair of philosophy", years: "1816–1818", kind: university, certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP."}
  - {value: "University of Berlin", role: "chair of philosophy", years: "1818–1831", kind: university, certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP."}
collaborators:
  - {value: "Friedrich Schelling", relation: collaborator, note: "co-edited the Critical Journal of Philosophy, 1802–1803", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP."}
  - {value: "Friedrich Hölderlin", relation: other, note: "student friend at Tübingen", certainty: 0.7, cites: [{source: S1, locator: "Early life"}, {source: S2, locator: "§1"}], how_known: "Britannica and SEP."}
  - {value: "Immanuel Kant", relation: "influenced by", certainty: 0.7, cites: [{source: S1, locator: "Early life"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S6, locator: "roster.csv, rank 98"}], how_known: "Study roster."}
  controversies:
    - {value: "Traditional metaphysical versus post-Kantian (non-metaphysical) readings of Hegel's God", certainty: 0.7, cites: [{source: S2, locator: "§2.2–2.4"}], how_known: "SEP; bears on A and primary_system."}
  data_quality_flags:
    - "Philosophy of Right dated 1821 (SEP) against 1820 (Wallace)."
    - "Encyclopaedia quotations are Wallace's translations via Project Gutenberg; German check pending."
    - "Only Britannica's 'Early life' section was returned by the fetch."
  open_questions:
    - "Check §564 and §573 in GW 20; read the 1807 Phenomenology (ch. VII) and the Lectures on the Philosophy of Religion (Jaeschke ed.) for A, B and the miracle question."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "T. Malcolm Knox"
    citation: "Knox, T. Malcolm. \"Georg Wilhelm Friedrich Hegel.\" Encyclopaedia Britannica (revised 23 August 2026). https://www.britannica.com/biography/Georg-Wilhelm-Friedrich-Hegel. Read live 2026-10-18 (the Wayback Machine was rate-limiting); the fetch returned the opening and 'Early life'."
    url: "https://www.britannica.com/biography/Georg-Wilhelm-Friedrich-Hegel"
    accessed: 2026-10-18
    reliability_note: "Signed article. Body only; the AI-generated Top Questions and Quick Facts are not cited."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, collaborators]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Paul Redding"
    citation: "Redding, Paul. \"Georg Wilhelm Friedrich Hegel.\" Stanford Encyclopedia of Philosophy (substantive revision 19 September 2025). https://plato.stanford.edu/entries/hegel/"
    url: "https://plato.stanford.edu/entries/hegel/"
    accessed: 2026-10-18
    reliability_note: "Signed SEP entry, read directly."
    used_for: [basics, contribution, worldview, timing, institutions, collaborators, review]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "G. W. F. Hegel"
    citation: "Hegel, G. W. F. Hegel's Philosophy of Mind (Encyclopaedia, part 3), trans. William Wallace (Oxford: Clarendon Press, 1894). Project Gutenberg eBook #39064. https://www.gutenberg.org/ebooks/39064"
    url: "https://www.gutenberg.org/ebooks/39064"
    accessed: 2026-10-18
    reliability_note: "Web copy of a translation of the 1830 text (Wallace's preface); Hegel's paragraphs only, editors' Zusätze omitted. Secondary quotation, cap 0.7."
    used_for: [worldview, timing, lane_b]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "G. W. F. Hegel"
    citation: "Hegel, G. W. F. The Logic of Hegel (Encyclopaedia, part 1), trans. William Wallace, 2nd ed. (Oxford: Clarendon Press, 1892). Project Gutenberg eBook #55108. https://www.gutenberg.org/ebooks/55108"
    url: "https://www.gutenberg.org/ebooks/55108"
    accessed: 2026-10-18
    reliability_note: "Web copy; includes Wallace's 'Bibliographical Notice' and the editors' Zusätze (not cited as Hegel's words). Secondary quotation."
    used_for: [basics, contribution, worldview]
  - id: S5
    type: secondary
    kind: "scholarly book"
    author: "G. W. F. Hegel (ed. K. L. Michelet; trans. E. S. Haldane)"
    citation: "Hegel, G. W. F. Lectures on the History of Philosophy, vol. 1, trans. E. S. Haldane (London: Kegan Paul, 1892), from Michelet's 2nd ed. (1840). Project Gutenberg eBook #51635. https://www.gutenberg.org/ebooks/51635"
    url: "https://www.gutenberg.org/ebooks/51635"
    accessed: 2026-10-18
    reliability_note: "Posthumous edition compiled from Hegel's manuscripts and students' notes (translator's preface); wording not certainly Hegel's. Context only."
    used_for: [worldview]
  - id: S6
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-18
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Georg Wilhelm Friedrich Hegel

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Georg Wilhelm Friedrich Hegel (1770–1831), German absolute idealist [S1; S2]. Draft: primary_system IDEAL (0.5, alt PANENT, CHRIST); A 3 at 0.5 (alt 2); B BELOW_THRESHOLD (alt 3); D 3 at 0.5 (alt 2); mid_basin BELOW_THRESHOLD. Not plotted.

## Life and work

Tübingen, Jena, Bamberg, Nuremberg, Heidelberg, Berlin [S2, §1].

## Contribution and impact

Phenomenology (1807), Science of Logic (1812–16), Encyclopaedia (1817), Philosophy of Right (1821) [S2].

## Childhood and education

Son of a revenue officer; Tübingen seminary [S1].

## Adult working worldview

'God is God only so far as he knows himself' [S3, §564]; pantheism denied [S3, §573].

## Heritage (context only)

Württemberg [S1].

## Timing

1807–1821 [S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Self-knowing spirit [S3].

## Open questions

- German checks; Phenomenology ch. VII; Lectures on the Philosophy of Religion.

## Research log

- 2026-10-18: Read Britannica (live, opening and Early life), SEP, and Wallace's and Haldane's translations on Project Gutenberg.
