---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z3; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages and archive.org OCR of Fabrica 1543"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to early_modern. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #142): opened Fabrica 1543 preface (English web translation + Latin IA OCR) and Book VI ch. 15 soul passage (Garrison English on vesaliusfabrica.com, Latin verified on IA OCR p. 594). Own voice: 'infinite Creator of things'; immortal soul as body's lodging/instrument (microcosm); 'summus rerum opifex Deus' (Book I); 'nostrae religionis' / abstains from locating types and seats of the soul to avoid faith/immortality censors. Still no clear A locus score — Creator/immortal-soul language is thin and he explicitly refuses soul-location dispute (P19). primary stays UNKNOWN (lead CHRIST, now with own-voice Catholic framing). A stays UNKNOWN. B stays 3 @0.5 alt 4 (P35/P16: preface is dissection/observation narrative, not explicit cause-order talk); support single→corroborated (S1+S3/S4). mid UNKNOWN; still not plotted. P47 source_quality; P50 Wikipedia EN (birth 31 Dec 1514 agrees with CE; death month June Britannica vs 15 Oct Wikipedia — noted). No figures/; no fallacy_catalog."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z3, order P32: F 3, rank 147). Source: Britannica (Marcel Florkin, signed). No own words on religion read; Catholic setting (Leuven, imperial court) and a pilgrimage to the Holy Sepulchre in 1564 are leads. A scientist (P30: anatomy from his own dissections). Span 1543 (Fabrica). primary_system UNKNOWN (lead CHRIST); A UNKNOWN; B 3 (0.5, alt 4); C, D, E UNKNOWN; mid_basin UNKNOWN. Not plotted (no A). Draft, not reviewed."}

identity:
  id: vesalius-andreas
  display_name: "Andreas Vesalius"
  roster:
    canonical_name: "Andreas Vesalius"
    rank: 147
    F: 3
    models: [Claude, DeepSeek, Gemini]
    band: "core (3–4)"
    status: core
    field: medicine
    field_bucket: medicine
  full_name: {value: "Andreas Vesalius", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "lead"}], how_known: "Britannica; Wikipedia EN agrees."}
  native_name: {value: "Andries van Wesel", certainty: 0.7, cites: [{source: S1, locator: "opening (Flemish)"}, {source: S5, locator: "infobox (Andries van Wezel)"}], how_known: "Britannica; Wikipedia EN."}
  aliases:
    - {name: "Vesalius-Andreas", kind: "roster alias"}
    - {name: "Andries van Wesel", kind: "birth name"}

basics:
  birth:
    date: {value: "1514-12-31", calendar: julian, certainty: 0.7, cites: [{source: S5, locator: "infobox"}, {source: S6, locator: "opening (31 Dec., 1514)"}, {source: S1, locator: "opening (December 1514)"}], how_known: "P50: Wikipedia EN and Catholic Encyclopedia agree on 31 December 1514; Britannica gives December 1514 (month only)."}
    place: {value: "Brussels, Duchy of Brabant", modern_name: "Brussels, Belgium", polity_then: "Habsburg Netherlands", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "infobox"}], how_known: "Britannica; Wikipedia EN."}
  death:
    date: {value: "1564-06", calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "opening (June 1564)"}, {source: S5, locator: "infobox (15 October 1564)"}], how_known: "Year 1564 agreed (Britannica, Wikipedia EN, CE). Month conflicts: Britannica June vs Wikipedia 15 October — kept Britannica month at 0.5."}
    place: {value: "Zacynthus (Zakynthos)", modern_name: "Zakynthos, Greece", polity_then: "Republic of Venice", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "infobox"}], how_known: "Britannica; Wikipedia EN."}
  first_lasting_contribution_year: {value: 1543, certainty: 0.7, cites: [{source: S1, locator: "'Life'"}, {source: S3, locator: "title page / colophon context"}], how_known: "De humani corporis fabrica, printed in Basel in 1543."}
  era_bucket: {value: "1400 to 1599", certainty: 1.0, cites: [{source: S1, locator: "'Life'"}], how_known: "1543 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Belgium (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.5, cites: [{source: S1, locator: "'Life'"}], how_known: "Padua (the Fabrica's dissections and drawings); later the imperial court and Madrid; 0.5."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Latin"], certainty: 0.7, cites: [{source: S1, locator: "'Life'"}, {source: S3, locator: "Latin text"}], how_known: "Latin titles; Fabrica in Latin."}
  occupations: {value: ["physician", "anatomist", "lecturer in surgery (Padua)", "imperial physician"], certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}

contribution:
  era_bucket: early_modern
  fields: {value: ["anatomy", "medicine"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "De humani corporis fabrica libri septem", year: 1543, kind: work, lasting: "'the first comprehensive textbook of anatomy'; 'After Vesalius, anatomy became a scientific discipline' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Life'"}, {source: S3, locator: "1543 Basel"}], how_known: "Britannica; primary Fabrica."}
  evidence_of_impact:
    - {value: "After Vesalius, anatomy became a scientific discipline", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  major_works: []
  honours:
    - {value: "Made a count, with a lifetime pension, by Charles V", year: 1556, certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "Founder of modern anatomy (S1).", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated; Catholic Brabant is the setting only."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Andreas Vesalius (father), court apothecary to Charles V", role: father, certainty: 0.7, cites: [{source: S1, locator: "'Life'"}, {source: S6, locator: "opening"}], how_known: "Britannica; Catholic Encyclopedia."}
  household_circumstances: {value: "Family of physicians and pharmacists", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  schooling:
    - {value: "Catholic University of Leuven", stage: university, run_by: "religious body", years: "1529–1533", certainty: 0.5, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica; run_by the coder's reading of 'Catholic University', 0.5."}
    - {value: "University of Paris medical school", stage: university, run_by: other, years: "1533–1536", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1543", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Anatomy of body and spirit plus 'a certain divinity that issues from a harmony of the two'; knowledge of humankind 'attests the wisdom … of the infinite Creator of things'; but he 'shall completely avoid' dispute on types/seats of the soul lest censors of 'our most truthful and sacred religion' charge doubt of faith or immortality of souls (Fabrica preface; VI.15)", certainty: 0.7, cites: [{source: S4, locator: "preface (Creator; body/spirit/divinity; immortal soul)"}, {source: S7, locator: "Bk. VI ch. 15 English"}, {source: S3, locator: "p. 594 Latin (religionis censores; animarum immortalitate)"}], how_known: "Primary Fabrica; English translations checked against Latin OCR."}
  primary_system: {value: UNKNOWN, how_known: "Lead CHRIST: Leuven/imperial Catholic setting, 1564 Holy Land pilgrimage (S1; S5; S6), plus own-voice 'nostrae religionis' and sacred-faith/immortality framing while refusing soul-location (S3; S7). Still below coding threshold — no full profession of a working Christian metaphysics (V3)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Lead: Catholic setting, pilgrimage, 'our … religion', Creator and immortal-soul language (S1; S3–S7). Not coded: he abstains from soul doctrine and gives no developed creed."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Own voice names an 'infinite Creator', an immortal soul lodged in the body, and God as 'summus rerum opifex', but also refuses to locate types/seats of the soul (S3; S4; S7). Thin Creator/soul language plus explicit abstention — no clear A score (P19). Keep UNKNOWN."}
    B_cause:
      value: 3
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S1, locator: "'Life'"}, {source: S4, locator: "preface (investigation of nature; Galen never dissected a human body)"}, {source: S3, locator: "preface / Book I"}]
      how_known: "Scientist (P30) with working science in the Fabrica preface (hands-on dissection; 'investigation of nature'; Galen corrected by observation). P35/P16: that is discovery practice, not an explicit account of miracles vs lawlike cause — B 3 at 0.5, alt 4."
      rationale: "P35."
      support: corroborated
      alternatives:
        - {value: 4, note: "P35 alternative.", cites: [{source: S1, locator: "'Life'"}, {source: S4, locator: "preface"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing scored; salvation/eternity language appears only inside the VI.15 'as if' about censors (S7)."}
    D_authority: {value: UNKNOWN, how_known: "Observation over Galen's authority is medical, not a claim about revelation vs reason (P16)."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read that scores E."}
  mid_basin: {value: UNKNOWN, how_known: "A UNKNOWN."}
  statements:
    - text: "…though they are obviously captivated by a knowledge of humankind that is most pleasant to them and attests the wisdom (if anything does) of the infinite Creator of things, they cannot bring themselves actually to attend an occasional dissection."
      cites: [{source: S4, locator: "Fabrica preface (English web translation)"}, {source: S3, locator: "praefatio (Latin OCR)"}]
      date: "1542-08-01"
      context: "Fabrica dedicatory preface to Charles V (dated Padua, 1 Aug 1542); on readers who love Creator-attesting knowledge of man but avoid dissection."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Stock Creator language; does not by itself score A."
    - text: "…so you would sometimes be delighted to ponder the construction of the most perfect of all creatures, and take pleasure in considering the lodging place and instrument of the immortal soul—a domicile which, because it admirably resembles the universe in many of its names, was fitly called a microcosm by the ancients."
      cites: [{source: S4, locator: "Fabrica preface"}, {source: S3, locator: "praefatio (immortalis animae diversorio)"}]
      date: "1542-08-01"
      context: "Preface closing flattery to Charles V; body as microcosm / lodging of immortal soul."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Dedicatory; not a scored A locus claim."
    - text: "To avoid running afoul of some 'idle talker' here, or some critic of doctrine, I shall completely avoid this dispute concerning the types of soul and their location. For, today, you will find many judges of our most truthful and sacred religion, especially among the natives of my country, and if they heard anyone muttering about the opinions of Plato, Aristotle, Galen, or their interpreters, about the soul, even when the subject is Anatomy … they leap to the conclusion that such a person is in doubt about the faith or has some uncertainty about the immortality of Souls…"
      cites: [{source: S7, locator: "Bk. VI ch. 15 English (Garrison)"}, {source: S3, locator: "p. 594 Latin ('ab hac de animae speciebus earundemque sedibus disceptatione prorsus abstinebo'; 'nostrae religionis censores')"}]
      date: "1543"
      context: "Fabrica Book VI ch. 15 (1543 p. 594); refuses to locate soul types/seats."
      axes: [A_locus, D_authority]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Own-voice Catholic 'our religion' framing + explicit abstention — blocks scoring A from soul doctrine."
    - text: "…it now becomes obvious to us from the reborn art of dissection, from the careful reading of Galen's books, and from the welcome restoration of many portions thereof, that he himself never dissected a human body, but in fact was deceived by his monkeys…"
      cites: [{source: S4, locator: "Fabrica preface"}, {source: S3, locator: "praefatio (Latin OCR)"}]
      date: "1542-08-01"
      context: "Preface; method — observation corrects Galen."
      axes: [B_cause, D_authority]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Working-science method; does not lift B above 0.5 (P35)."
    - text: "…disgracefully spurning what is a principal and most ancient branch of medicine, one preeminently reliant (if anything is) upon the investigation of nature…"
      cites: [{source: S4, locator: "Fabrica preface"}, {source: S3, locator: "praefatio"}]
      date: "1542-08-01"
      context: "Preface; surgery/anatomy as investigation of nature."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
    - text: "Huius enim temperamenti summus rerum opifex Deus substantiam merito efformavit, corpori universo fundamenti instar subjiciendam."
      cites: [{source: S3, locator: "Book I ch. 1 (bone; Latin OCR)"}]
      date: "1543"
      context: "Fabrica Book I opening on bone: God the supreme craftsman of things fashioned bone as the body's foundation."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Latin kept (no checked English for this sentence this pass). Stock Opifex-Deus; does not score A alone."
  changes_over_life:
    - {value: "1564 pilgrimage to the Holy Land / Holy Sepulchre; died on return (Zakynthos). Motive unknown in his words; Inquisition-penance story is later rumour dismissed by modern biographers (S5; S6).", year: 1564, certainty: 0.7, cites: [{source: S1, locator: "'Life'"}, {source: S5, locator: "Death"}, {source: S6, locator: "pilgrimage; Inquisition rumour"}], how_known: "Britannica; Wikipedia EN; Catholic Encyclopedia."}
  coder_notes: "Deepen filled the Fabrica preface / VI.15 gap. A stays UNKNOWN despite Creator and immortal-soul language because he explicitly abstains from soul location and never states a locus doctrine. B stays P35 ceiling 0.5."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Brabantine (Flemish)", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Catholic (setting)", certainty: 0.5, cites: [{source: S1, locator: "'Life'"}, {source: S6, locator: "opening"}], how_known: "Catholic Brabant / Leuven; not a baptismal record."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1543", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "The Fabrica (1543), the only lasting work named (P29, P30)."}
  age_at_first_lasting_contribution: {value: 29, certainty: 0.7, cites: [{source: S1, locator: "opening; 'Life'"}, {source: S4, locator: "preface ('not yet passed beyond my twenty-eighth year')"}], how_known: "1543 − 1514 = 29 (P30 year difference); preface says not yet 28 in Aug 1542 — consistent with Dec 1514 birth."}
  first_evidence_of_lio_type_views: {value: "1542–1543 (Fabrica preface and Book VI.15)", certainty: 0.7, cites: [{source: S4, locator: "preface"}, {source: S7, locator: "VI.15"}], how_known: "Creator / immortal soul / religion-censor passages."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S4, locator: "preface"}, {source: S3, locator: "1543"}], how_known: "Inside the Fabrica itself."}
  worldview_during_major_work: {value: "Catholic setting with Creator and immortal-soul language; refuses to locate the soul", certainty: 0.5, cites: [{source: S4, locator: "preface"}, {source: S7, locator: "VI.15"}], how_known: "Own words; not a coded system."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Descriptive anatomy (S1).", certainty: 0.5, cites: [{source: S1, locator: "'Life'"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Body as microcosm resembling the universe (preface) is analogy, not identity of God with nature.", certainty: 0.5, cites: [{source: S4, locator: "preface (microcosm)"}], how_known: "Coder's reading."}
  reading: "Hands-on anatomy under stock Creator language; soul location refused."
  notes: ""

institutions:
  - {value: "University of Padua", role: "lecturer in surgery", years: "1537–1543", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  - {value: "Household of Emperor Charles V; court of Philip II", role: physician, years: "1543–1564", kind: other, certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
collaborators:
  - {value: "Galen", roster_id: galen, relation: "rival or critic", note: "corrected Galenic anatomy", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}, {source: S4, locator: "preface"}], how_known: "Britannica; Fabrica preface."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 147"}], how_known: "Study roster."}
  controversies:
    - {value: "Inquisition / living dissection / forced pilgrimage story: later rumour (Languet), generally dismissed (S5; S6).", certainty: 0.7, cites: [{source: S5, locator: "Death"}, {source: S6, locator: "Inquisition rumour"}], how_known: "Wikipedia EN; Catholic Encyclopedia."}
  data_quality_flags:
    - "Death month conflicts (Britannica June vs Wikipedia 15 Oct 1564)."
    - "Preface English from unofficial web copy; key phrases checked against Latin IA OCR."
  open_questions:
    - "Full Garrison–Hast New Fabrica English for Book I Opifex sentence (Latin used)."
    - "Any letter with personal creed beyond Fabrica."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Marcel Florkin"
    citation: "Florkin, Marcel. \"Andreas Vesalius.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Andreas-Vesalius. Read live 2026-10-19; rechecked 2026-10-24."
    url: "https://www.britannica.com/biography/Andreas-Vesalius"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Signed article; body cited, question boxes not (P26)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [review]
  - id: S3
    type: primary
    kind: published work by the subject
    author: "Andreas Vesalius"
    citation: "Vesalius, Andreas. De humani corporis fabrica libri septem. Basel: Joannes Oporinus, 1543. Internet Archive / NLM scan 2295005R (djvu OCR)."
    url: "https://archive.org/details/2295005R.nlm.nih.gov"
    accessed: 2026-10-24
    source_quality: "archive scan (OCR only)"
    reliability_note: "1543 Basel; noisy Latin OCR. Used to verify preface and Book VI p. 594 soul/religion passage and Book I Opifex Deus."
    used_for: [contribution, worldview, timing, collaborators]
  - id: S4
    type: secondary
    kind: other
    author: "Andreas Vesalius; English translator (web copy, faculty.washington.edu/jwoiak)"
    citation: "Vesalius, Andreas. Preface to De humani corporis fabrica (English translation). Hosted as PDF at http://faculty.washington.edu/jwoiak/downloads/copy_of_Vesalius-preface.pdf (accessed 2026-10-24)."
    url: "http://faculty.washington.edu/jwoiak/downloads/copy_of_Vesalius-preface.pdf"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Complete English preface; Creator, immortal-soul/microcosm, Galen-never-dissected, investigation-of-nature passages checked against S3 Latin OCR."
    used_for: [worldview, timing, collaborators]
  - id: S5
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Andreas Vesalius.\" English Wikipedia (accessed 2026-10-24). https://en.wikipedia.org/wiki/Andreas_Vesalius"
    url: "https://en.wikipedia.org/wiki/Andreas_Vesalius"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "P50 dual bio; notes Inquisition story as unfounded. Death date 15 Oct 1564 conflicts with Britannica June."
    used_for: [identity, basics, worldview, review]
  - id: S6
    type: secondary
    kind: encyclopedia
    author: "Catholic Encyclopedia (New Advent)"
    citation: "\"Andreas Vesalius.\" The Catholic Encyclopedia. New Advent. https://www.newadvent.org/cathen/15378c.htm"
    url: "https://www.newadvent.org/cathen/15378c.htm"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Birth 31 Dec 1514; pilgrimage; dismisses Inquisition tale; notes Louvain soul-seat dispute and that he avoided stating an opinion."
    used_for: [basics, childhood, worldview, heritage, review]
  - id: S7
    type: secondary
    kind: other
    author: "Daniel H. Garrison (trans./commentary); vesaliusfabrica.com"
    citation: "Garrison, Daniel H. \"Vesalius & Religion.\" The Fabric of the Human Body site. English of Fabrica Bk. VI ch. 15 (1543 p. 594). https://www.vesaliusfabrica.com/en/vesalius/history-context/vesalius-religion.html"
    url: "https://www.vesaliusfabrica.com/en/vesalius/history-context/vesalius-religion.html"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Garrison New Fabrica translator; English soul/religion passage verified against S3 Latin OCR p. 594."
    used_for: [worldview, timing]
---

# Andreas Vesalius

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Andreas Vesalius (1514–1564), Renaissance anatomist [S1]. Draft: primary_system UNKNOWN (lead CHRIST); A UNKNOWN; B 3 (0.5, alt 4, support corroborated). Not plotted. Deepen D1 opened Fabrica preface and VI.15; codes unchanged.

## Life and work

Brussels, Leuven, Paris, Padua, the imperial court [S1]. 1564 Holy Land pilgrimage; died Zakynthos [S1; S5].

## Contribution and impact

The Fabrica (1543) [S1; S3].

## Childhood and education

Family of physicians; Leuven; Paris [S1].

## Adult working worldview

Creator and immortal-soul language in the Fabrica preface; God as *summus rerum opifex* in Book I; refuses to locate types/seats of the soul (VI.15) [S3; S4; S7]. No coded A.

## Heritage (context only)

Brabantine; Catholic setting [S1; S6].

## Timing

1543, age 29 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Microcosm analogy only [S4].

## Open questions

- Full New Fabrica English for Book I Opifex sentence.
- Personal letters with creed.

## Research log

- 2026-10-19: Read Britannica (Florkin).
- 2026-10-24: Deepen D1 — Fabrica 1543 IA OCR; preface English (UW web); Garrison VI.15; Wikipedia; Catholic Encyclopedia. Codes unchanged.
