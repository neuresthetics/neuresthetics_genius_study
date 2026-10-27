---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 4
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Q)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-18
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to philosophy. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-25, by: "Grok Bot", summary: "Perpetual deepen: religious_heritage_by_birth / family_religion / baptism TODO→Lutheran (Württemberg Protestant) @0.7 (S9+S1; Christened; Tübinger Stift; lifelong Lutheran). Catechism UNKNOWN. Chart-moving NO. No figures/; no fallacy_catalog."}
    - {date: 2026-10-18, by: "Grok Bot", summary: "Record created (stage 3 batch Q, order P32: F 4, rank 98). Basics from Britannica (T. Malcolm Knox, signed; body through 'Early life', read live) and SEP 'Hegel' (Paul Redding, revision of 19 September 2025). Worldview from the Encyclopaedia (3rd ed. 1830) in Wallace's translations (Philosophy of Mind §§564–565, §573 Remark; Logic §16 Remark), Project Gutenberg web copies; the Lectures on the History of Philosophy (Michelet's compiled edition, Haldane trans.) as context. Not a scientist (P30). primary_system IDEAL (0.5, alt PANENT, CHRIST); A 3 (0.5, alt 2); B BELOW_THRESHOLD (alt 3); D 3 (0.5, alt 2); mid_basin BELOW_THRESHOLD. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-18, by: "Grok Bot", summary: "Batch Q audit fixes (gs_0b3023d_Q run 1: 43 hold, 4 weaken, 1 fail). D quote now 'a cognition of the necessity' (H8); SEP locators §3 and §3.1.2 for the Science of Logic (H9). Notes: A gains a BELOW_THRESHOLD alternative for SEP's §2.3 non-metaphysical reading; the Michelet miracle passage cites the P42 addendum (reported speech); 'Göschel' flagged as the coder's identification of Wallace's 'C. F. G—l'. Jason's ruling (2026-10-18, RQ Q1): B BELOW_THRESHOLD → 2 at 0.5, alternative 3, from Encyclopaedia (1830) §248 with its Remark and §250, read in zeno.org's web copy of Werke vol. 9 (new S7, cap 0.7). Now plotted, faded, at A3/B2; mid_basin stays BELOW_THRESHOLD."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #97 / F4 rank 98). Re-read zeno.org German Encyclopaedia Nature §§248–250 (S7) and Mind §§564–565, §573 Remark (new S8); Wallace Mind/Logic retained. Dual bio Wikipedia (S9, P50). P47 source_quality on all sources. A stays 3 @0.5 corroborated (alt 2; alt BELOW for SEP §2.3 non-metaphysical); B stays 2 @0.5 corroborated (alt 3; Jason RQ Q1). Contested readings + post-span Enc. 1830 keep certainty at 0.5 (P20/P25); cannot lift to ≥0.7. mid_basin stays BELOW_THRESHOLD. Chart already faded filled — chart-moving NO. Draft deepen report in drafts/ (untracked)."}

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
    date: {value: "1770-08-27", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "§1 (year)"}, {source: S9, locator: "lead (27 August 1770)"}], how_known: "Britannica gives the day; SEP agrees on 1770 and Stuttgart; Wikipedia dual bio (P50)."}
    place: {value: "Stuttgart, Württemberg", modern_name: "Stuttgart, Germany", polity_then: "Duchy of Württemberg (Holy Roman Empire)", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "§1"}], how_known: "Britannica and SEP."}
  death:
    date: {value: "1831-11-14", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "§1 (year)"}, {source: S9, locator: "lead (14 November 1831)"}], how_known: "Britannica; SEP gives 1831; Wikipedia dual bio (P50)."}
    place: {value: "Berlin", modern_name: "Berlin, Germany", polity_then: "Kingdom of Prussia", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1807, certainty: 0.7, cites: [{source: S2, locator: "§1; §2 (corpus)"}, {source: S4, locator: "Bibliographical Notice"}], how_known: "Phenomenology of Spirit, published 1807 (SEP; Wallace's notice)."}
  era_bucket: {value: "1750 to 1849", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "First lasting year 1807 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Germany (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "Jena, Bamberg, Nuremberg, Heidelberg, Berlin."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["German"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  occupations: {value: ["philosopher", "university professor", "gymnasium headmaster", "newspaper editor"], certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP."}

contribution:
  primary_domain: philosophy
  fields: {value: ["metaphysics", "logic", "philosophy of history", "political philosophy", "philosophy of religion"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "§§2–3"}], how_known: "Britannica and SEP."}
  lasting_original_contributions:
    - {value: "Phenomenology of Spirit", year: 1807, kind: work, lasting: "his 'first major work' (S2)", certainty: 0.7, cites: [{source: S2, locator: "§1"}, {source: S4, locator: "Bibliographical Notice"}], how_known: "SEP and Wallace agree on 1807."}
    - {value: "Science of Logic (three books)", year: "1812–1816", kind: work, lasting: "one of 'Hegel's two major stand-alone books' (S2)", certainty: 0.7, cites: [{source: S2, locator: "§3 ('two major stand-alone books'); §3.1.2 ('appeared in 1812, 1813, and 1816')"}], how_known: "SEP."}
    - {value: "Encyclopaedia of the Philosophical Sciences", year: 1817, kind: work, lasting: "'the only complete, matured, and authentic statement of Hegel's philosophical system' (S4)", certainty: 0.7, cites: [{source: S2, locator: "§1"}, {source: S4, locator: "Bibliographical Notice"}], how_known: "SEP; later editions 1827 and 1830 (S3, Preface)."}
    - {value: "Elements of the Philosophy of Right", year: 1821, kind: work, lasting: "'his major work in political philosophy' (S2)", certainty: 0.5, cites: [{source: S2, locator: "§1"}, {source: S4, locator: "Bibliographical Notice"}], how_known: "SEP gives 1821; Wallace's notice gives 1820 (the book appeared before its title-page year). A P25 conflict, so 0.5 with 1820 the named alternative."}
    - {value: "Dialectical system of absolute idealism", kind: "body of work", lasting: "'the last of the great philosophical system builders of modern times' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; undated."}
  evidence_of_impact:
    - {value: "Influence on Kierkegaard, the Marxists, the logical positivists, Moore and Russell (by reaction)", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Lutheran (Württemberg Protestant)", certainty: 0.7, cites: [{source: S9, locator: "Early life (Christened; Tübinger Stift Protestant seminary); Religion (identified as a Lutheran his entire life)"}, {source: S1, locator: "Early life (Tübingen theology; parents wished him for orders)"}], how_known: "Wikipedia: christened; entered Protestant seminary; lifelong Lutheran identity. Britannica: Tübingen with view to taking orders. Context only."}
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
    cites: [{source: S1, locator: "opening ('absolute idealist inspired by Christian insights')"}, {source: S3, locator: "§§564–565, §573 Remark"}, {source: S8, locator: "§564 Remark; §565; §573 Remark"}, {source: S2, locator: "§2.2–2.4"}]
    rationale: "Absolute idealism: God as 'absolute spirit', 'the essential and actual spirit of nature and spirit' (§565), whose self-knowledge is 'his self-consciousness in man' (§564); the being of external things is 'untruth' beside God's 'absolute universality' (§573 Remark). Named alternatives: PANENT (a divine spirit that includes the world and exceeds it; he denies that 'each and every secular thing is God') and CHRIST (he treats Christianity as the absolute, revealed religion and calls himself Lutheran in the compiled lectures). SEP sets out traditional-metaphysical and post-Kantian (non-metaphysical) readings, so the code is contested."
    how_known: "Wallace English (S3) plus zeno.org German Werke (S8) for §§564–565, §573; SEP traditional vs non-metaphysical readings (S2). Contested reading, 0.5 (P25)."
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
      support: corroborated
      cites: [{source: S3, locator: "§§564–565, §573 Remark"}, {source: S8, locator: "§564 Remark; §565; §573 Remark (German)"}, {source: S2, locator: "§2.2"}]
      rationale: "Leans to the immanent pole: German 'Gott ist nur Gott, insofern er sich selber weiß; sein Sichwissen ist ferner sein Selbstbewußtsein im Menschen' (§564 Remark, adopting Aphorisms of 'C. F. G—l' / Göschel per coder); God is 'der an und für sich seiende Geist der Natur und des Geistes' (§565). Stated limit: he rejects the pantheism charge that 'Alles, d.h. die empirischen Dinge ohne Unterschied… sei Gott' (§573 Remark). Named alternative 2: the revealed, triune God of §§564–571 can be read as a personal God beyond the world (mixed). SEP: traditional reading has the mind of God becoming actual only via its particularization in the minds of his finite material creatures; post-Kantian readers deny the metaphysics."
      how_known: "Wallace English (S3) corroborated by zeno.org German Werke (S8) and SEP §2.2 (S2); distinct source ids → corroborated (P48). Contested reading (named alts) keeps certainty at 0.5 (P25); web copies cap 0.7 anyway (P26)."
      alternatives:
        - {value: 2, note: "Revealed triune God as a person beyond the world (§§564–571).", cites: [{source: S3, locator: "§§564–565"}, {source: S8, locator: "§564 Remark; §565"}]}
        - {value: BELOW_THRESHOLD, note: "SEP §2.3, the post-Kantian non-metaphysical reading: Hegel's 'God' is not a claim about a being at all, so the text bears on A only indirectly (P19).", cites: [{source: S2, locator: "§2.3"}]}
    B_cause:
      value: 2
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S7, locator: "§248 and Remark; §250"}, {source: S4, locator: "§16 Remark"}]
      rationale: "Account of nature in his own published text (P16): nature 'zeigt daher in ihrem Dasein keine Freiheit, sondern Notwendigkeit und Zufälligkeit' (§248: shows in its existence no freedom, but necessity and contingency); against those who praise nature for staying 'bei aller Zufälligkeit ihrer Existenzen ewigen Gesetzen getreu' he sets spirit's Willkür above 'das gesetzmäßige Wandeln der Gestirne' (§248 Remark); and the 'gleichgültigen Zufälligkeit und unbestimmbaren Regellosigkeit' of nature's forms is granted its place: 'Die Zufälligkeit und Bestimmbarkeit von außen hat in der Sphäre der Natur ihr Recht', 'die Ohnmacht der Natur' (§250). Conceptual necessity governs nature's stages, but contingency and indeterminable irregularity hold of the concrete detail: lawfulness covering only part of nature (P27 B 2 anchor). The Logic §16 Remark agrees ('the Idea of Nature, when parcelled out in detail, is dissipated into contingencies'). Named alternative 3: if that contingency is read as nature's shortfall from the concept rather than a gap in its order, with spirit's Willkür as the one free-will exception (P30 #14), B is 3. Jason's ruling (2026-10-18, RQ Q1 of the batch Q audit, on the auditor's recommendation)."
      how_known: "zeno.org German Werke Nature §§248–250 (S7) re-read word for word 2026-10-24, corroborated by Wallace Logic §16 Remark (S4); distinct ids → corroborated (P48). 1830 after the span (1807–1821) and §250 reading contested → certainty stays 0.5 (P20/P25; Jason RQ Q1). Michelet miracle passage stays context only (P42)."
      alternatives:
        - {value: 3, note: "Contingency read as nature's impotence to realise the concept, not an exception; Willkür as the one free-will exception (P30 #14).", cites: [{source: S7, locator: "§248 Remark; §250"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing scored at this reading."}
    D_authority:
      value: 3
      basis: written_profession
      certainty: 0.5
      cites: [{source: S3, locator: "§573 and Remark"}]
      rationale: "Speculative reason outranks revelation's form but keeps its content: philosophy is 'a cognition of the necessity in the content of the absolute picture-idea' and of 'the objective and external revelation presupposed by representation', its 'liberation from the one-sidedness of the forms'; 'the content of religion and philosophy is the same'. Revelation keeps one stated point, its content, which philosophy recognises and 'does not disparage'. Named alternative 2: 'religion is the truth for all men', read as a domain of its own. Coder's reading."
      how_known: "Encyclopaedia (1830), Wallace's translation via a web copy; 0.5."
      alternatives:
        - {value: 2, note: "Religion as 'the truth for all men' in its own form.", cites: [{source: S3, locator: "§573 Remark"}]}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 3 @0.5 (contested) is under the 0.7 the A ≥ 3 branch needs (P10); B 2 @0.5 likewise (P19). Deepen D1 did not lift either certainty."}
  statements:
    - text: "God is God only so far as he knows himself: his self-knowledge is, further, his self-consciousness in man, and man’s knowledge of God, which proceeds to man’s self-knowledge in God."
      cites: [{source: S3, locator: "§564 Remark (Gutenberg)"}]
      date: "1830"
      context: "Encyclopaedia, 3rd ed. (1830), Philosophy of Mind §564 Remark, adopting propositions from the Aphorisms on Knowing and Not-knowing by 'C. F. G—l' (Berlin, 1829), whom the coder identifies as Karl Friedrich Göschel (Wallace gives only the abbreviation); Wallace's translation."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Wallace web copy; German parallel added (S8) 2026-10-24."
    - text: "Gott ist nur Gott, insofern er sich selber weiß; sein Sichwissen ist ferner sein Selbstbewußtsein im Menschen und das Wissen des Menschen von Gott, das fortgeht zum Sichwissen des Menschen in Gott."
      cites: [{source: S8, locator: "§564 Remark"}]
      date: "1830"
      context: "Encyclopaedia (1830) Philosophy of Mind §564 Remark (German Werke). Same propositions as Wallace's English; Aphorisms of C. F. G—l / Göschel."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "zeno.org web copy of Werke; checked word for word against the page 2026-10-24."
    - text: "and so—thus he understands philosophy—each and every secular thing is God. It is only his own stupidity, and the falsifications due to such misconception, which generate the imagination and the allegation of such pantheism."
      cites: [{source: S3, locator: "§573 Remark (Gutenberg)"}]
      date: "1830"
      context: "Encyclopaedia (1830) §573 Remark, rejecting the charge of pantheism."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Wallace web copy; German parallel added (S8)."
    - text: "So machen sie jene Allgemeinheit zu der, welche sie die pantheistische nennen, – daß Alles, d.h. die empirischen Dinge ohne Unterschied, die höher geachteten wie die gemeinen, sei, Substantialität besitze, und dies Sein der weltlichen Dinge sei Gott. – Es ist nur die eigene Gedankenlosigkeit und eine daraus hervorgehende Verfälschung der Begriffe, welche die Vorstellung und Versicherung von dem Pantheismus erzeugt."
      cites: [{source: S8, locator: "§573 Remark"}]
      date: "1830"
      context: "§573 Remark (German): he attributes the pantheism charge — that every empirical thing is God — to thoughtlessness and falsification of concepts."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "zeno.org web copy; checked word for word 2026-10-24."
    - text: "Similarly the Idea of Nature, when parcelled out in detail, is dissipated into contingencies. Natural history, geography, and medicine stumble upon descriptions of existence, upon kinds and distinctions, which are not determined by reason, but by sport and adventitious incidents."
      cites: [{source: S4, locator: "§16 Remark (Gutenberg)"}]
      date: "1830"
      context: "Encyclopaedia Logic §16 Remark, Wallace's translation (2nd ed. 1892) of the 1830 text."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "Wallace web copy; Nature German parallel in S7 (deepen D1)."
    - text: "Die Natur zeigt daher in ihrem Dasein keine Freiheit, sondern Notwendigkeit und Zufälligkeit."
      cites: [{source: S7, locator: "§248"}]
      date: "1830"
      context: "Encyclopaedia (1830), Philosophy of Nature, Introduction, 'Begriff der Natur', §248 (nature shows in its existence no freedom, but necessity and contingency). Coder's translation."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "zeno.org web copy of Werke vol. 9; re-checked word for word 2026-10-24."
    - text: "Die Natur bleibe, gibt man ferner als ihren Vorzug an, bei aller Zufälligkeit ihrer Existenzen ewigen Gesetzen getreu; aber doch wohl auch das Reich des Selbstbewußtseins! [...] Wenn aber die geistige Zufälligkeit, die Willkür, bis zum Bösen fortgeht, so ist dies selbst noch ein unendlich Höheres als das gesetzmäßige Wandeln der Gestirne oder als die Unschuld der Pflanze; denn was sich so verirrt, ist noch Geist."
      cites: [{source: S7, locator: "§248 Remark"}]
      date: "1830"
      context: "§248 Remark: against praising nature for staying true to eternal laws amid all the contingency of its existences; spirit's free choice, even in evil, ranks above the lawful motion of the stars. The cut drops one sentence on Providence guiding human affairs. Coder's translation."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "zeno.org web copy; re-checked word for word 2026-10-24."
    - text: "Der Widerspruch der Idee, indem sie als Natur sich selbst äußerlich ist, ist näher der Widerspruch einerseits der durch den Begriff gezeugten Notwendigkeit ihrer Gebilde und deren in der organischen Totalität vernünftigen Bestimmung, – andererseits deren gleichgültigen Zufälligkeit und unbestimmbaren Regellosigkeit. Die Zufälligkeit und Bestimmbarkeit von außen hat in der Sphäre der Natur ihr Recht."
      cites: [{source: S7, locator: "§250"}]
      date: "1830"
      context: "§250: the contradiction between the necessity of nature's forms, generated by the concept, and their indifferent contingency and indeterminable irregularity; contingency and determinability from outside have their right in the sphere of nature. Later in §250: 'Es ist die Ohnmacht der Natur, die Begriffsbestimmungen nur abstrakt zu erhalten und die Ausführung des Besonderen äußerer Bestimmbarkeit auszusetzen.' Coder's translation."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "zeno.org web copy; re-checked word for word 2026-10-24."
    - text: "Christ reproved the Pharisees for wishing to see miracles; the Spirit alone comprehends Spirit, the miracle is only a presentiment of that Spirit; and if the miracle be the suspension of natural laws, Spirit itself is the real miracle in the operations of nature."
      cites: [{source: S5, locator: "Introduction, B.2 (Gutenberg vol. 1)"}]
      context: "Lectures on the History of Philosophy, Introduction, as compiled by Michelet (2nd ed. 1840) from Hegel's manuscripts and students' notes from courses of 1805–1830; Haldane's translation. No single year, so the date is left out."
      axes: [B_cause]
      kind: "other"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "Compiled lecture text (Michelet, from manuscripts and students' notes): reported speech under the P42 addendum on disciples' records; context only."
  changes_over_life:
    - {value: "Early Kantian reading of Christianity as rational morality (Bern, 1790s), later freed from Kant's influence (Frankfurt)", certainty: 0.7, cites: [{source: S1, locator: "Early life"}], how_known: "Britannica; before the span, does not split it (P31)."}
  coder_notes: "B 2 at 0.5, alternative 3, is Jason's ruling (2026-10-18, RQ Q1). Deepen D1 (2026-10-24): German Mind §§564–573 (S8) and re-read Nature §§248–250 (S7); A/B stay 0.5 under contested-reading caps (P25) despite corroboration (P48). Enc. 1830 after span; 1817/1807 unread (P30 #7). Miracle passage context only (P42). Britannica Top Questions / Quick Facts not cited (P26)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German (Württemberg)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Lutheran (Württemberg Protestant)", certainty: 0.7, cites: [{source: S9, locator: "Early life (Christened Georg Wilhelm Friedrich; Tübinger Stift); Religion (Lutheran his entire life)"}, {source: S1, locator: "Early life"}], how_known: "Dual bio: Wikipedia christening + Protestant seminary + Lutheran self-identity; Britannica Tübingen theology track. Context only — not scored adult primary_system by itself (P19)."}
  baptism_or_initiation: {value: "Lutheran christening (infant)", certainty: 0.7, cites: [{source: S9, locator: "Early life: Christened Georg Wilhelm Friedrich"}], how_known: "Wikipedia states he was christened; Lutheran infant baptism is the default for that christening in Württemberg. No parish register opened."}
  childhood_catechism: {value: UNKNOWN, how_known: "No childhood catechism curriculum named in S1–S9; seminary training is later (age 18)."}

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
    - "Encyclopaedia Nature §§248–250 and Mind §§564–573 re-checked in zeno.org German Werke (web copy, not GW critical edition)."
    - "Only Britannica's 'Early life' section was returned by the create-pass fetch."
    - "Contested A (SEP §2.3) and B (§250) keep certainty at 0.5; chart stays faded."
  open_questions:
    - "GW critical edition (GW 19/20) print check for Enc. Nature and Mind; Phenomenology ch. VII and Lectures on the Philosophy of Religion (Jaeschke) for in-span A/B; Miller/Petry Nature English as a second translation."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "T. Malcolm Knox"
    citation: "Knox, T. Malcolm. \"Georg Wilhelm Friedrich Hegel.\" Encyclopaedia Britannica (revised 23 August 2026). https://www.britannica.com/biography/Georg-Wilhelm-Friedrich-Hegel. Read live 2026-10-18 (the Wayback Machine was rate-limiting); the fetch returned the opening and 'Early life'."
    url: "https://www.britannica.com/biography/Georg-Wilhelm-Friedrich-Hegel"
    accessed: 2026-10-18
    reliability_note: "Signed article. Body only; the AI-generated Top Questions and Quick Facts are not cited."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, collaborators]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Paul Redding"
    citation: "Redding, Paul. \"Georg Wilhelm Friedrich Hegel.\" Stanford Encyclopedia of Philosophy (substantive revision 19 September 2025). https://plato.stanford.edu/entries/hegel/"
    url: "https://plato.stanford.edu/entries/hegel/"
    accessed: 2026-10-18
    reliability_note: "Signed SEP entry, read directly."
    source_quality: "reference entry"
    used_for: [basics, contribution, worldview, timing, institutions, collaborators, review]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "G. W. F. Hegel"
    citation: "Hegel, G. W. F. Hegel's Philosophy of Mind (Encyclopaedia, part 3), trans. William Wallace (Oxford: Clarendon Press, 1894). Project Gutenberg eBook #39064. https://www.gutenberg.org/ebooks/39064"
    url: "https://www.gutenberg.org/ebooks/39064"
    accessed: 2026-10-18
    reliability_note: "Web copy of a translation of the 1830 text (Wallace's preface); Hegel's paragraphs only, editors' Zusätze omitted. Secondary quotation, cap 0.7."
    source_quality: "unofficial web copy"
    used_for: [worldview, timing, lane_b]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "G. W. F. Hegel"
    citation: "Hegel, G. W. F. The Logic of Hegel (Encyclopaedia, part 1), trans. William Wallace, 2nd ed. (Oxford: Clarendon Press, 1892). Project Gutenberg eBook #55108. https://www.gutenberg.org/ebooks/55108"
    url: "https://www.gutenberg.org/ebooks/55108"
    accessed: 2026-10-18
    reliability_note: "Web copy; includes Wallace's 'Bibliographical Notice' and the editors' Zusätze (not cited as Hegel's words). Secondary quotation."
    source_quality: "unofficial web copy"
    used_for: [basics, contribution, worldview]
  - id: S5
    type: secondary
    kind: "scholarly book"
    author: "G. W. F. Hegel (ed. K. L. Michelet; trans. E. S. Haldane)"
    citation: "Hegel, G. W. F. Lectures on the History of Philosophy, vol. 1, trans. E. S. Haldane (London: Kegan Paul, 1892), from Michelet's 2nd ed. (1840). Project Gutenberg eBook #51635. https://www.gutenberg.org/ebooks/51635"
    url: "https://www.gutenberg.org/ebooks/51635"
    accessed: 2026-10-18
    reliability_note: "Posthumous edition compiled from Hegel's manuscripts and students' notes (translator's preface); wording not certainly Hegel's. Context only (P42)."
    source_quality: "scholarly reconstruction"
    used_for: [worldview]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "G. W. F. Hegel"
    citation: "Hegel, G. W. F. Enzyklopädie der philosophischen Wissenschaften im Grundrisse (1830), Zweiter Teil: Die Naturphilosophie, Einleitung, 'Begriff der Natur' (§§247–251). Werke vol. 9, web copy at zeno.org. http://www.zeno.org/Philosophie/M/Hegel,+Georg+Wilhelm+Friedrich/Enzyklop%C3%A4die+der+philosophischen+Wissenschaften+im+Grundrisse/Zweiter+Teil%3A+Die+Naturphilosophie/Einleitung/Begriff+der+Natur"
    url: "http://www.zeno.org/Philosophie/M/Hegel,+Georg+Wilhelm+Friedrich/Enzyklop%C3%A4die+der+philosophischen+Wissenschaften+im+Grundrisse/Zweiter+Teil%3A+Die+Naturphilosophie/Einleitung/Begriff+der+Natur"
    accessed: 2026-10-18
    reliability_note: "Web copy of the Werke text (main paragraphs and Remarks; no Zusätze quoted); cap 0.7; print check pending."
    source_quality: "unofficial web copy"
    used_for: [worldview]
  - id: S8
    type: primary
    kind: "published work by the subject"
    author: "G. W. F. Hegel"
    citation: "Hegel, G. W. F. Enzyklopädie der philosophischen Wissenschaften im Grundrisse (1830), Dritter Teil: Die Philosophie des Geistes, 3. Abteilung: Der absolute Geist — B. Die geoffenbarte Religion (§§564–571) and C. Die Philosophie (§§572–577). Werke web copy at zeno.org."
    url: "http://www.zeno.org/Philosophie/M/Hegel,+Georg+Wilhelm+Friedrich/Enzyklop%C3%A4die+der+philosophischen+Wissenschaften+im+Grundrisse/Dritter+Teil%3A+Die+Philosophie+des+Geistes/3.+Abteilung%3A+Der+absolute+Geist/B.+Die+geoffenbarte+Religion"
    accessed: 2026-10-24
    reliability_note: "Web copy of the Werke text (main paragraphs and Remarks; no Zusätze quoted as Hegel's words); cap 0.7; GW critical print check pending."
    source_quality: "unofficial web copy"
    used_for: [worldview]
  - id: S9
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. 'Georg Wilhelm Friedrich Hegel.' https://en.wikipedia.org/wiki/Georg_Wilhelm_Friedrich_Hegel. Read 2026-10-24 (dual bio P50) and 2026-10-25 (Early life: Christened; Tübinger Stift; Religion: Lutheran identity)."
    url: "https://en.wikipedia.org/wiki/Georg_Wilhelm_Friedrich_Hegel"
    accessed: 2026-10-25
    reliability_note: "Dual biography check against Britannica/SEP (P50); heritage context from Early life / Religion; worldview not taken from Wikipedia."
    source_quality: "reference entry"
    used_for: [basics, heritage]
  - id: S6
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-18
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
---

# Georg Wilhelm Friedrich Hegel

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Georg Wilhelm Friedrich Hegel (1770–1831), German absolute idealist [S1; S2; S9]. Draft: primary_system IDEAL (0.5, alt PANENT, CHRIST); A 3 at 0.5 corroborated (alt 2; alt BELOW); B 2 at 0.5 corroborated (alt 3; Jason's ruling); D 3 at 0.5 (alt 2); mid_basin BELOW_THRESHOLD. Plotted, faded filled, at A3/B2.

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

- GW critical edition; Phenomenology ch. VII; Jaeschke Lectures on the Philosophy of Religion; Miller/Petry Nature English.

## Research log

- 2026-10-18: Read Britannica (live, opening and Early life), SEP, and Wallace's and Haldane's translations on Project Gutenberg.
- 2026-10-24: Deepen D1 — re-read zeno.org German Nature §§248–250 and Mind §§564–573; Wikipedia dual bio; A/B stay 0.5 contested/corroborated; chart-moving NO.
