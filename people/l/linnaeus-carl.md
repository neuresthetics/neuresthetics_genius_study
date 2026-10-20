---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z5)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z5 audit fixes (Z5-20, Z5-21, Z5-22, Z5-24; RQ-Z5-2 answered): 'Vis illud Naturam vocare' re-cited to the printed editions (S8: 1758 facsimile, p. 5; S7: 1766) and dated 1758, with footnote (b) to Seneca, Quaest. Nat. II.45; the 1735 Latin corrected to the folio (S9); 'Deum sempiternum' re-cited to S7/S8 with the 1758 variant noted; 'aeternae legis imperio' added as a B lead; B basis scholarly_reconstruction -> inference_from_work (P24). Values unchanged (A 0 @0.5 alt 2; B 3 @0.5 alt 4). RQ-Z5-N1 logged in OPEN_DECISIONS, not applied."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z5, order P32: F 3, rank 154). Basics from Britannica (Staffan Müller-Wille, signed) and Britannica Scholars 'Species Plantarum'. Own words via Wikiquote (Latin with translations): Systema Naturae 1735, 'Genus omne est naturale, in primordio tale creatum'; 12th ed. (1766), Imperium Naturae, 'Deum sempiternum, immensum, omniscium, omnipotentem ... vidi et obstupui!'; the fuller Latin (a creyentesintelectuales blog transcription) continues 'Vis illud Naturam vocare, non errabis'. Secondary quotations, primary check pending; 1766 is after the span (P20). A scientist (P30: taxonomy from specimens). Span 1735–1753. primary_system CHRIST (0.5); A 0 (0.5, alt 2); B 3 (0.5, alt 4; P35); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Plotted (faded). Draft, not reviewed."}

identity:
  id: linnaeus-carl
  display_name: "Carl Linnaeus"
  roster:
    canonical_name: "Carl Linnaeus"
    rank: 154
    F: 3
    models: [Claude, Gemini, Grok]
    band: "core (3–4)"
    status: core
    field: biology
    field_bucket: "biology / life science"
  full_name: {value: "Carl Linnaeus (ennobled Carl von Linné)", certainty: 0.7, cites: [{source: S1, locator: "Also known as"}], how_known: "Britannica."}
  native_name: {value: "Carl von Linné", certainty: 0.7, cites: [{source: S1, locator: "Swedish"}], how_known: "Britannica."}
  aliases:
    - {name: "Linnaeus-Carl", kind: "roster alias"}
    - {name: "Carolus Linnaeus", kind: "latinized"}

basics:
  birth:
    date: {value: "1707-05-23", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Born"}], how_known: "Britannica."}
    place: {value: "Råshult, Småland", modern_name: "Råshult, Sweden", polity_then: "Swedish Empire", certainty: 0.7, cites: [{source: S1, locator: "Born"}], how_known: "Britannica."}
  death:
    date: {value: "1778-01-10", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Died"}], how_known: "Britannica."}
    place: {value: "Uppsala", modern_name: "Uppsala, Sweden", polity_then: "Sweden", certainty: 0.7, cites: [{source: S1, locator: "Died"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1735, certainty: 0.7, cites: [{source: S1, locator: "'The sexual system of classification'"}], how_known: "Systema Naturae, 1735."}
  era_bucket: {value: "1600 to 1749", certainty: 1.0, cites: [{source: S1, locator: "text"}], how_known: "1735 (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "Born"}], how_known: "Sweden (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S2, locator: "text"}], how_known: "Uppsala from 1742; Netherlands 1735–38."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Latin", "Swedish"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Latin titles."}
  occupations: {value: ["naturalist", "physician", "professor of medicine and botany (Uppsala)"], certainty: 0.7, cites: [{source: S2, locator: "text"}], how_known: "Britannica."}

contribution:
  fields: {value: ["botany", "zoology", "taxonomy"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Systema Naturae: hierarchical classification of the three kingdoms", year: 1735, kind: work, lasting: "'Linnaeus's classification system has survived in biology' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'The sexual system of classification'"}], how_known: "Britannica."}
    - {value: "Species Plantarum: binomial nomenclature applied to plants", year: 1753, kind: work, lasting: "'the foundation for modern botanical and zoological nomenclature' (S3)", certainty: 0.7, cites: [{source: S3, locator: "text"}], how_known: "Britannica Scholars."}
  evidence_of_impact:
    - {value: "Starting point of botanical nomenclature", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S3, locator: "text"}], how_known: "Britannica Scholars."}
  major_works:
    - {value: "Philosophia Botanica", year: 1751, kind: book, certainty: 0.7, cites: [{source: S3, locator: "text"}], how_known: "Britannica Scholars."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founder of modern taxonomy and nomenclature (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Lutheran (son of a curate)", certainty: 0.5, cites: [{source: S1, locator: "'Early life and travels'"}], how_known: "Britannica: 'son of a curate'; Lutheran from the Swedish church, coder's addition."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household: []
  household_circumstances: {value: "Curate's family in poor Småland", certainty: 0.7, cites: [{source: S1, locator: "'Early life and travels'"}], how_known: "Britannica."}
  schooling:
    - {value: "Växjö gymnasium", stage: "grammar or secondary school", run_by: "state or municipal", years: "1720s", certainty: 0.5, cites: [{source: S1, locator: "'Early life and travels'"}], how_known: "Britannica; run_by and years the coder's."}
    - {value: "Lund University; Uppsala University; MD Harderwijk 1735", stage: university, run_by: "state or municipal", years: "1727–1735", certainty: 0.7, cites: [{source: S1, locator: "'Early life and travels'"}], how_known: "Britannica."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure:
    - {value: "Tournefort's plant system, Vaillant on plant sexuality, Boerhaave, via a Växjö teacher", certainty: 0.7, cites: [{source: S1, locator: "'Early life and travels'"}], how_known: "Britannica."}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["Swedish"], certainty: 0.5, cites: [{source: S1, locator: "Born"}], how_known: "Inferred."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1735–1753", certainty: 0.5, cites: [{source: S1, locator: "text"}, {source: S3, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "'Finis Creationis telluris est gloria Dei ex opere Naturae per Hominem solum' (Systema Naturae, late editions)", certainty: 0.5, cites: [{source: S4, locator: "Systema Naturae"}], how_known: "Wikiquote; secondary quotation."}
  primary_system:
    value: CHRIST
    basis: written_profession
    certainty: 0.5
    cites: [{source: S4, locator: "Systema Naturae"}, {source: S1, locator: "'Early life and travels'"}]
    how_known: "Psalm verses and praises in Systema Naturae (from 1758, per S5); curate's son (S1). Secondary quotations and after the span, so 0.5."
    rationale: "CHRIST: biblical praise in his main work. Alternative BELOW_THRESHOLD: the Imperium Naturae passage blends Stoic and Aristotelian sources ('Vis illud Naturam vocare')."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Coded at 0.5."}
    - {code: PANT, reason: "Rejected: 'Naturam vocare' is one of three names offered for a Creator who is 'Domino & Artifice'."}
  lio_axes:
    A_locus:
      value: 0
      basis: written_profession
      certainty: 0.5
      cites: [{source: S8, locator: "Imperium Naturae, p. 5"}, {source: S7, locator: "Imperium Naturae, opening paragraph"}]
      how_known: "Printed editions read (1758 facsimile; 1766); after the 1735–1753 span (P20), and a named alternative, so 0.5. See RQ-Z5-N1."
      rationale: "An 'eternal, immeasurable, all-knowing, all-powerful God', 'Lord and Artificer' of the world's work, First Mover and Cause of causes. Alternative 2: 'If you call it Nature, you will not err; it is that from which all things are born.'"
      alternatives:
        - {value: 2, note: "'Vis illud Naturam vocare, non errabis' (after Seneca, Quaest. Nat. II.45, note b).", cites: [{source: S8, locator: "Imperium Naturae, p. 5, note (b)"}, {source: S7, locator: "Imperium Naturae, note (b)"}]}
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      cites: [{source: S1, locator: "'The sexual system of classification'"}, {source: S9, locator: "Observationes in Regnum Vegetabile"}]
      how_known: "A scientist with working science (P30: classification from specimens), so B 3 at 0.5, alternative 4 (P35, P24: basis inference_from_work). Genera 'created as such in the beginning' (1735) fits a creation followed by lawful order. Lead (not scored, after the span): the 1758 Imperium Naturae MUNDUS paragraph says the heavens move 'aeternae legis imperio, nec esse temere errantis hunc ordinem' (after Seneca; S8 p. 5, S7)."
      rationale: "P35."
      alternatives:
        - {value: 4, note: "P35 alternative.", cites: [{source: S1, locator: "text"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nemesis Divina (unpublished) not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 0 at 0.5 is under the 0.7 bar (§6, P10)."}
  statements:
    - text: "Genus omne est naturale, in ipso primordio tale creatum: hinc pro lubitu & secundum cujuscunque theoriam non proterve discindendum, vel conglutinandum est."
      cites: [{source: S9, locator: "Observationes in Regnum Vegetabile, folio sheet"}]
      date: "1735"
      context: "Systema Naturae, 1st ed. (Leiden 1735), botanical observations."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-19
      note: "Read in the 1735 folio scan (archive.org mobot31753002972252); long s normalized. Corrects the Wikiquote wording ('in primordio', 'libitu', 'secundem cujuscimque', 'aut', no closing 'est')."
    - text: "Deum sempiternum, immensum, omniscium, omnipotentem expergefactus a tergo transeuntem vidi et obstupui! legi aliquot Ejus vestigia per creata rerum, in quibus omnibus, etiam in minimis, ut fere nullis, quæ Vis! quanta Sapientia! quam inextricabilis Perfectio!"
      cites: [{source: S7, locator: "Imperium Naturae, opening paragraph"}, {source: S8, locator: "Imperium Naturae, p. 5"}]
      date: "1766"
      context: "Imperium Naturae, 12th edition (1766); first printed in the 10th edition (1758). After the span."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-19
      note: "Wording as in the 1766 scan, long s normalized. The 1758 text lacks 'immensum' and 'expergefactus' ('DEUM sempiternum, omniscium, omnipotentem a tergo transeuntem vidi & obstupui!')."
    - text: "Vis illud Fatum vocare, non errabis, est ex quo suspensa sunt omnia. Vis illud Naturam vocare, non errabis, est ex quo nata sunt omnia. Vis illud Providentiam vocare, recte dices"
      cites: [{source: S8, locator: "Imperium Naturae, p. 5, and note (b)"}, {source: S7, locator: "Imperium Naturae, opening paragraph, and note (b)"}]
      date: "1758"
      context: "Imperium Naturae, 10th edition (1758), repeated in the 12th (1766), after 'mundani hujus operis Domino & Artifice'. Footnote (b) cites Seneca, Quaest. Nat. II.45: Linnaeus adopts Seneca's three names (Fatum, Natura, Providentia) for the Lord and Artificer. After the span."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-19
      note: "Read in both scans (archive.org carolilinnaeisy01gesegoog, the 1894 facsimile of 1758; bub_gb_siAOAAAAQAAJ, 1766); long s normalized. The blog transcription (S5) matches."
  changes_over_life: []
  coder_notes: "Imperium Naturae checked in the 1758 facsimile and the 1766 edition (RQ-Z5-2 answered: the passage is in print, so the alternative 2 stands). RQ-Z5-N1 (open): ICZN Article 3 and Opinion 3 treat the 10th edition (1758) as the starting point of zoological nomenclature ('the work which inaugurated the consistent general application of binary nomenclature in zoology'); if it is listed as lasting, the span ends 1758 and the Imperium Naturae falls inside it. Not applied. Read Nemesis Divina for C."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Swedish", certainty: 0.7, cites: [{source: S1, locator: "Born"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Lutheran", certainty: 0.5, cites: [{source: S1, locator: "'Early life and travels'"}], how_known: "Curate's son; coder's addition."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1735–1753", certainty: 0.5, cites: [{source: S1, locator: "text"}, {source: S3, locator: "text"}], how_known: "Systema Naturae (1735) to Species Plantarum (1753) (P29, P30); the 10th edition of Systema Naturae (1758, zoological starting point) is a later candidate, so 0.5."}
  age_at_first_lasting_contribution: {value: 28, certainty: 0.7, cites: [{source: S1, locator: "Born; text"}], how_known: "1735 − 1707 = 28 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: "1735", certainty: 0.5, cites: [{source: S9, locator: "Observationes in Regnum Vegetabile"}], how_known: "Created genera ('in ipso primordio tale creatum')."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.5, cites: [{source: S4, locator: "Systema Naturae"}], how_known: "Same work."}
  worldview_during_major_work: {value: "CHRIST", certainty: 0.5, cites: [{source: S4, locator: "Systema Naturae"}], how_known: "Secondary quotations."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Hierarchical classification, not proof (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Uppsala University", role: "professor of medicine and botany", years: "1742–1778", kind: university, certainty: 0.7, cites: [{source: S2, locator: "text"}], how_known: "Britannica."}
collaborators:
  - {value: "Herman Boerhaave", relation: "influenced by", note: "introduced him to Clifford", certainty: 0.7, cites: [{source: S2, locator: "text"}], how_known: "Britannica."}
  - {value: "George Clifford", relation: "mentor or employer", note: "curator of his garden", certainty: 0.7, cites: [{source: S2, locator: "text"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S6, locator: "roster.csv, rank 154"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Own words now read in printed editions (1735 folio; 1758 facsimile; 1766); Wikiquote and the blog kept as finding aids only."
  open_questions:
    - "Facsimile of the Imperium Naturae; Nemesis Divina."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Staffan Müller-Wille"
    citation: "Müller-Wille, Staffan. \"Carolus Linnaeus.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Carolus-Linnaeus"
    url: "https://www.britannica.com/biography/Carolus-Linnaeus"
    accessed: 2026-10-19
    reliability_note: "Signed article; opening through 'The sexual system of classification' read."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Staffan Müller-Wille"
    citation: "Müller-Wille, Staffan. \"Carolus Linnaeus.\" Britannica Scholars (Britannica Kids). https://kids.britannica.com/scholars/article/Carolus-Linnaeus/48407"
    url: "https://kids.britannica.com/scholars/article/Carolus-Linnaeus/48407"
    accessed: 2026-10-19
    reliability_note: "Same article, later sections, read via search excerpt."
    used_for: [basics, institutions, collaborators]
  - id: S3
    type: tertiary
    kind: encyclopedia
    author: "Encyclopaedia Britannica"
    citation: "\"Species Plantarum.\" Britannica Scholars. https://kids.britannica.com/scholars/article/Species-Plantarum/103290"
    url: "https://kids.britannica.com/scholars/article/Species-Plantarum/103290"
    accessed: 2026-10-19
    reliability_note: "Unsigned article, read via search excerpt."
    used_for: [contribution, worldview, timing]
  - id: S4
    type: secondary
    kind: other
    author: "Wikiquote contributors"
    citation: "\"Carl Linnaeus.\" Wikiquote. https://en.wikiquote.org/wiki/Carl_Linnaeus"
    url: "https://en.wikiquote.org/wiki/Carl_Linnaeus"
    accessed: 2026-10-19
    reliability_note: "Latin quotations with sources named (Systema Naturae editions; Ramsbottom 1938); secondary."
    used_for: [worldview, timing]
  - id: S5
    type: secondary
    kind: other
    author: "Creyentes Intelectuales (blog)"
    citation: "\"Carlos Linneo: 'El propósito de la Creación es la Gloria de Dios'.\" Creyentes Intelectuales, July 2014. http://creyentesintelectuales.blogspot.com/2014/07/carlos-linneo.html"
    url: "http://creyentesintelectuales.blogspot.com/2014/07/carlos-linneo.html"
    accessed: 2026-10-19
    reliability_note: "Advocacy blog; used only for its Latin transcription of the Imperium Naturae (note 9) and the Psalm placements; low reliability."
    used_for: [worldview]
  - id: S6
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [review]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "Carl Linnaeus"
    citation: "Linnaeus, Carl. Systema naturae per regna tria naturae. 12th ed. Holmiae: L. Salvius, 1766. Scan: https://archive.org/details/bub_gb_siAOAAAAQAAJ"
    url: "https://archive.org/details/bub_gb_siAOAAAAQAAJ"
    accessed: 2026-10-19
    reliability_note: "Printed edition, Google Books scan with OCR; Imperium Naturae read."
    used_for: [worldview]
  - id: S8
    type: primary
    kind: "published work by the subject"
    author: "Carl Linnaeus"
    citation: "Linnaeus, Carl. Systema naturae. Regnum animale. Editio decima, 1758. Facsimile ed. Societas zoologica germanica. Lipsiae: W. Engelmann, 1894. Scan: https://archive.org/details/carolilinnaeisy01gesegoog"
    url: "https://archive.org/details/carolilinnaeisy01gesegoog"
    accessed: 2026-10-19
    reliability_note: "Page-for-page reprint of the 10th edition; Imperium Naturae, p. 5, read."
    used_for: [worldview]
  - id: S9
    type: primary
    kind: "published work by the subject"
    author: "Carl Linnaeus"
    citation: "Linnaeus, Carl. Systema naturae, sive regna tria naturae systematice proposita. Lugduni Batavorum: Theodor Haak, 1735. Scan: https://archive.org/details/mobot31753002972252"
    url: "https://archive.org/details/mobot31753002972252"
    accessed: 2026-10-19
    reliability_note: "First edition folio, Missouri Botanical Garden scan."
    used_for: [worldview]
---

## Summary

Carl Linnaeus (1707–1778), naturalist [S1]. Draft: CHRIST (0.5); A 0 (0.5, alt 2); B 3 (0.5, alt 4). Plotted (faded).

## Life and work

Småland, Uppsala, the Netherlands, Uppsala [S1, S2].

## Contribution and impact

Systema Naturae; binomial nomenclature [S1, S3].

## Childhood and education

Curate's son; Växjö; Lund and Uppsala [S1].

## Adult working worldview

Creator praised throughout Systema Naturae [S4, S5].

## Heritage (context only)

Swedish Lutheran [S1].

## Timing

1735–1753, age 28 [S1, S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Facsimile check.

## Research log

- 2026-10-19: Read Britannica (Müller-Wille), Britannica Scholars, Wikiquote, blog transcription.
