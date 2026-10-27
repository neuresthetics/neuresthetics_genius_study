---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 4
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z5)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-26
  change_log:
    - {date: 2026-10-26, by: "Grok Bot", summary: "RQ-Z5-N1 settled (Jason t275u unblock, 2026-10-26): Systema Naturae 10th ed. (1758) listed as a lasting contribution on ICZN Art. 3 (S15) per P13/P17; span 1735–1758. Imperium Naturae (1758) now in-span own written profession: A 0 @0.7 adds S7/S8 (DEUM sempiternum ... Domino & Artifice) so alt 2 cites are a subset → A corroborated; B 3 lifted 0.5→0.7 on in-span own-voice aeternae legis imperio (S8) with Nova creatio nulla (P35 does not apply: own statements, not work-only inference); alt 4 kept. mid_basin BELOW_THRESHOLD→true (P4). Chart: faded hollow → dark filled."}
    - {date: 2026-10-25, by: "Grok Bot", summary: "Deepen D2: B_cause support single→corroborated. Alt 4 cites trimmed to S11 only (Nova creatio nulla) — drop exclusive Britannica S1 which added no independent alt content (P48). A stays single (after-span Imperium alt S7/S8 exclusive by design; RQ-Z5-N1). Still faded hollow. No fallacy_catalog; no figures/. Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #148, F 3, rank 154). Opened Species Plantarum 1753 Lectorem / Swedish dedication (Gutenberg #20771, S10); Philosophia Botanica 1751 OCR (IA philosophiabota00linn, S11); Systema 1744 Paris 4th (IA carolilinaeimedi00linn, S12); Nemesis Divina Barr 1923 (S14, after-span private MS). Wikipedia EN dual bio (S13; P50). A_locus 0: 0.5→0.7 written_profession in-span (SP Lectorem Dominus/Creator/summum Ens + PB Creator/legem Naturae); after-span Imperium Naturam-vocare kept as named alt 2 (P20; contested ≤0.7); support single (P48: alt 2 cites S7/S8 exclusive). B_cause stays 3 @0.5 alt 4 (P16/P35: Nova creatio nulla / legem Naturae / primordio creatum are creation-then-lawful-generation, not a no-exception lift); basis inference_from_work→written_profession; support single (alt 4 cites S1 exclusive). primary CHRIST stays 0.5 (Lutheran + in-span Creator/Lord; Psalms/Imperium still after-span). C stays UNKNOWN (Nemesis read: just Gud / Heliga Skrift; private after-span). E UNKNOWN→BELOW_THRESHOLD (P19 scientist). mid BELOW; plotted faded. Span 1735–1753 unchanged; RQ-Z5-N1 OPEN not applied. P47 source_quality on S1–S14. Chart-moving NO. No figures/; no fallacy_catalog. Draft, not reviewed."}
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
    place: {value: "Uppsala", modern_name: "Uppsala, Sweden", polity_then: "Sweden", certainty: 0.5, cites: [{source: S1, locator: "Died"}, {source: S13, locator: "Died (Hammarby)"}], how_known: "Britannica Died Uppsala; Wikipedia Died Hammarby (buried Uppsala Cathedral). Real place dispute → 0.5 (P25).", alternatives: [{value: "Hammarby", note: "Wikipedia; estate near Uppsala where he spent summers and last illness.", cites: [{source: S13, locator: "Died; Final years"}]}]}
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
    - {value: "Systema Naturae, 10th edition: consistent binomial nomenclature for animals; starting point of zoological nomenclature", year: 1758, kind: work, lasting: "'The date 1 January 1758 is arbitrarily fixed in this Code as the date of the starting point of zoological nomenclature' — 10th edition deemed published that day (S15)", certainty: 0.7, cites: [{source: S15, locator: "Article 3; 3.1"}], how_known: "ICZN Code Art. 3 (RQ-Z5-N1 settled 2026-10-26)."}
    - {value: "Species Plantarum: binomial nomenclature applied to plants", year: 1753, kind: work, lasting: "'the foundation for modern botanical and zoological nomenclature' (S3)", certainty: 0.7, cites: [{source: S3, locator: "text"}], how_known: "Britannica Scholars."}
  evidence_of_impact:
    - {value: "Starting point of botanical nomenclature", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S3, locator: "text"}], how_known: "Britannica Scholars."}
  major_works:
    - {value: "Philosophia Botanica", year: 1751, kind: book, certainty: 0.7, cites: [{source: S3, locator: "text"}], how_known: "Britannica Scholars."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founder of modern taxonomy and nomenclature (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Lutheran (son of a curate / Lutheran minister)", certainty: 0.7, cites: [{source: S1, locator: "'Early life and travels'"}, {source: S13, locator: "Childhood (Nils Linnaeus, Lutheran minister)"}], how_known: "Britannica curate; Wikipedia Nils as Lutheran minister and curate/rector of Stenbrohult."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Nils (Nicolaus) Linnaeus (Ingemarsson), Lutheran minister; curate then rector of Stenbrohult", role: father, certainty: 0.7, cites: [{source: S13, locator: "Childhood"}, {source: S1, locator: "'Early life and travels'"}], how_known: "Wikipedia + Britannica curate's son."}
    - {value: "Christina Brodersonia, daughter of rector Samuel Brodersonius", role: mother, certainty: 0.7, cites: [{source: S13, locator: "Childhood"}], how_known: "Wikipedia."}
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
  working_years: {value: "1735–1758", certainty: 0.5, cites: [{source: S1, locator: "text"}, {source: S3, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Species Plantarum Lectorem: the world is the Omnipotent's theatre; guests must study the Creator's works (opera Creatoris) and acknowledge the Lord's magnificence; Swedish dedication praises the Almighty Creator's wonders (Alsmägtiga Skaparen)", certainty: 0.7, cites: [{source: S10, locator: "LECTORI ÆQUO; Swedish royal dedication"}, {source: S4, locator: "Finis Creationis (late editions, finding aid)"}, {source: S5, locator: "Psalm placements / Imperium (finding aid)"}], how_known: "In-span 1753 own-voice (Gutenberg transcription of Species Plantarum). Late-edition Finis Creationis and Imperium Psalm placements kept as secondary finding aids only (S4; S5)."}
  primary_system:
    value: CHRIST
    basis: written_profession
    certainty: 0.5
    cites: [{source: S10, locator: "LECTORI ÆQUO"}, {source: S1, locator: "'Early life and travels'"}, {source: S13, locator: "Childhood"}]
    how_known: "In-span Creator/Dominus/summum Ens in Species Plantarum 1753 (S10) plus Lutheran curate's-son heritage (S1; S13). Psalm verses and Imperium Naturae remain after the 1735–1753 span (P20), so CHRIST stays 0.5 rather than 0.7 — Creator/Lord language alone is not specifically Christological."
    rationale: "CHRIST: Lutheran natural theologian praising Dominus/Creator in the lasting botanical work. Named alternative BELOW_THRESHOLD / CLTHEI: in-span Lectorem is personal-Creator language without Christ/Trinity; after-span Imperium blends Stoic Seneca names (Fatum/Natura/Providentia)."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Coded at 0.5 (Lutheran + Creator/Lord; Psalms after span)."}
    - {code: CLTHEI, reason: "Lead from in-span Lectorem Creator/summum Ens without Christ-specific wording."}
    - {code: PANT, reason: "Rejected for the span: in-span texts treat Nature as the Creator's work/law, not as God; after-span 'Naturam vocare' is one Seneca name for Domino & Artifice."}
  lio_axes:
    A_locus:
      value: 0
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S8, locator: "Imperium Naturae, p. 5 (DEUM sempiternum, omniscium, omnipotentem ... Domino & Artifice)"}, {source: S7, locator: "Imperium Naturae, opening paragraph"}, {source: S10, locator: "LECTORI ÆQUO (omnipotentis / Domini / Creatoris / summum Ens)"}, {source: S11, locator: "Introductio §1 arte divina; Creator commissit generationem; Creatoris artificio"}, {source: S12, locator: "Creator hominem ... Artificem ex opere"}]
      how_known: "Deepen D1: in-span own voice. Species Plantarum 1753 Lectorem — world as omnipotentis theatrum; magnificentiam Domini; opera Creatoris; summum Ens (S10). Philosophia Botanica 1751 — Naturalia composita arte divina; Creator entrusted species generation to Nature's law; Creatoris artificio distinct species (S11). Systema 1744 — Creator placed man to admire the Artificer from the work (S12). Named alternative 2 from after-span Imperium Naturae (P20) keeps the contested-reading ceiling at 0.7 and makes support single under P48 (alt cites S7/S8 exclusive of the value). 2026-10-26: RQ-Z5-N1 settled, span 1735–1758; Imperium Naturae 1758 (S8; S7) is in-span and names DEUM omnipotent, Domino & Artifice — added to cites; alt 2 cites now a subset → corroborated (P48). Alt 2 kept; 0.7 ceiling stays (contested reading)."
      rationale: "Personal Creator / Lord / supreme Being as locus — A 0. Alternative 2: after-span 'Vis illud Naturam vocare, non errabis' (Seneca note on Domino & Artifice); in-span texts treat Nature as the Creator's work and law, not as the locus itself."
      alternatives:
        - {value: 2, note: "After-span (1758/1766 Imperium Naturae): 'Vis illud Naturam vocare, non errabis' (Seneca, Quaest. Nat. II.45, note b). In-span since 2026-10-26; kept as named alternative under the contested-reading rule.", cites: [{source: S8, locator: "Imperium Naturae, p. 5, note (b)"}, {source: S7, locator: "Imperium Naturae, note (b)"}]}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S9, locator: "Observationes in Regnum Vegetabile (primordio tale creatum)"}, {source: S11, locator: "Nova creatio nulla; legem Naturae ... Creator; Genus ... primordio tale creatum"}, {source: S10, locator: "LECTORI ÆQUO (Creatoris opera; Naturae regna)"}, {source: S8, locator: "Imperium Naturae, p. 5 (MUNDUS ... aeternae legis imperio, nec esse temere errantis hunc ordinem)"}]
      how_known: "Deepen D1: in-span own voice states creation of genera/species at the beginning then continued generation under Nature's law that the Creator entrusted (S9; S11), with no new creation (Nova creatio nulla). Scientist under P30. Certainty stays 0.5: P16 addendum / P35 — an explicit lawful-order / creation-then-generation remark without a stated no-exception claim across nature cannot lift B past 0.5; alternative 4 kept. D2: support corroborated (P48) — alt 4 cites now only S11 (subset of value cites); exclusive Britannica S1 dropped from alt as non-independent. A still single via Imperium alt (RQ-Z5-N1). 2026-10-26 (RQ-Z5-N1 settled, span to 1758): in-span own voice, Imperium Naturae 1758 — the world's bodies proceed 'aeternae legis imperio', the order not wandering at random (S8, p. 5; Seneca echo, note f, adopted in his own text) — with Nova creatio nulla gives own-voice statements on law and creation, so P35's work-only cap does not apply; B 3 at 0.7 (creation at the beginning as the stated exception; alt 4 kept)."
      rationale: "Creation act then lawful generation of species (B 3). Named alternative 4 (P16/P35: no exceptionless claim for all of nature)."
      alternatives:
        - {value: 4, note: "P16/P35 default alternative; Nova creatio nulla covers species generation, not a universal no-miracle claim.", cites: [{source: S11, locator: "Nova creatio nulla"}]}
    C_ledger: {value: UNKNOWN, cites: [{source: S14, locator: "rättvis Gud / Gud ser dig / Heliga Skrift"}], how_known: "Nemesis Divina (Barr 1923 ed., S14) read: private MS for his son — 'här bor en rättvis Gud' / 'Gud ser dig' / Heliga Skrift; after the 1735–1753 span and unpublished in his lifetime (P20) → not scored. Would be a C 0 lead if ever in-span public."}
    D_authority: {value: UNKNOWN, how_known: "No in-span statement on revelation vs observation scored this pass."}
    E_scope: {value: BELOW_THRESHOLD, note: "Scientist under P30; working science bears on E's first question but E is not scored from working science alone (P19).", how_known: "BELOW_THRESHOLD under P19 (scientist, no statement; deepen 2026-10-24). Was UNKNOWN."}
  mid_basin: {value: true, certainty: 0.7, cites: [{source: S8, locator: "Imperium Naturae, p. 5"}, {source: S10, locator: "LECTORI ÆQUO"}, {source: S11, locator: "Nova creatio nulla"}], how_known: "P4: A 0 ≤ 1 and B 3 ≥ 3, both at 0.7 (RQ-Z5-N1 settled 2026-10-26, span 1735–1758)."}
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
    - text: "Homo sui conscius observat MUNDUM esse omnipotentis theatrum, undique adornatum summis Omnisciæ sapientiæ miraculis, se vero in hunc, tamquam Hospitem introductum, ut hisce deliciis sese delectando magnificentiam Domini agnoscat. … HOSPITES ut digni evadamus orbis, opera hæc Creatoris scrutari nobis necesse est, quæ ita cum nostris commodis combinavit summum Ens"
      cites: [{source: S10, locator: "LECTORI ÆQUO"}]
      date: "1753"
      context: "Species Plantarum, preface to the reader (in-span lasting work)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Project Gutenberg eBook #20771 transcription of the 1753 Latin; long s / ligatures normalized in the source. Swedish royal dedication in the same volume praises Alsmägtiga Skaparens underverk (Almighty Creator's wonders)."
    - text: "Naturalia composita arte divina. … Exemplohorrendo sapiant Botanici ne minima circumstantia variet rem contra legem Naturæ, cui specierum generationem commissit Creator, non hominibus. … Distinguimus Creatoris artificio distinctas species a Naturæ ludentis varietatibus. … Nova creatio nulla: sed continuata generatio. … Genus omne est naturale, in primordio tale creatum."
      cites: [{source: S11, locator: "Introductio §1; Differentiæ (Creator/legem Naturæ); §79 Nova creatio; §159 Genus"}]
      date: "1751"
      context: "Philosophia Botanica (Stockholm/Amsterdam 1751), in-span."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "IA philosophiabota00linn OCR; wording normalized from OCR (iexusparcreatum → sexus par creatum in nearby §132; long s). Repeats the 1735 primordio creatum line and adds Creator/Nature's-law framing."
    - text: "Quæro itaque, quamobrem Creator hominem ejusmodi sensibus et intellectu proditum, in globum terraqueum collocaverit, … anne ob aliam causam, quam ut Observator Artificem ex opere pulcherrimo admiraretur"
      cites: [{source: S12, locator: "Fundamenta / opening Creator paragraph"}]
      date: "1744"
      context: "Systema naturæ, 4th ed. (Paris: David, 1744), in-span."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "IA carolilinaeimedi00linn OCR; long s normalized. Creator / Artifex framing of natural history."
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
  coder_notes: "Deepen D1 2026-10-24: A lifted on in-span Species Plantarum Lectorem + Philosophia Botanica + Systema 1744 Creator language; Imperium Naturae stays after-span under open RQ-Z5-N1 (alt 2 retained as contested after-span reading). B enriched to written_profession but held at 0.5 (P16/P35). Nemesis Divina (Barr 1923) read — private after-span MS for Carl Jr.; C not scored. E set BELOW_THRESHOLD (P19). Chart stays faded; not chart-moving. RQ-Z5-N1 dry-run (deepen report only): span→1758 would put Imperium in-span → A already 0.7, B could reach 0.7 on aeternae legis imperio → mid_basin true."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Swedish", certainty: 0.7, cites: [{source: S1, locator: "Born"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Lutheran", certainty: 0.7, cites: [{source: S1, locator: "'Early life and travels'"}, {source: S13, locator: "Childhood"}], how_known: "Father Lutheran minister (Wikipedia); Britannica curate's son."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1735–1758", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S15, locator: "Article 3"}], how_known: "Systema Naturae (1735) to Systema Naturae 10th ed. (1758, ICZN zoological starting point) (P29, P30; RQ-Z5-N1 settled 2026-10-26)."}
  age_at_first_lasting_contribution: {value: 28, certainty: 0.7, cites: [{source: S1, locator: "Born; text"}], how_known: "1735 − 1707 = 28 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: "1735", certainty: 0.7, cites: [{source: S9, locator: "Observationes in Regnum Vegetabile"}, {source: S10, locator: "LECTORI ÆQUO"}], how_known: "1735 primordio creatum; 1753 Lectorem Creator/Dominus in the lasting Species Plantarum."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S10, locator: "LECTORI ÆQUO"}, {source: S9, locator: "Observationes"}], how_known: "In-span lasting works."}
  worldview_during_major_work: {value: "CHRIST", certainty: 0.5, cites: [{source: S10, locator: "LECTORI ÆQUO"}, {source: S1, locator: "'Early life and travels'"}], how_known: "In-span Creator/Lord + Lutheran heritage; not specifically Christological at 0.7."}

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
    - "Own words read in printed editions / transcriptions (1735 folio; 1744 Paris; 1751 Philosophia Botanica OCR; 1753 Species Plantarum Gutenberg; 1758 facsimile; 1766); Wikiquote and the blog kept as finding aids only."
    - "Death place: Britannica Uppsala vs Wikipedia Hammarby (buried Uppsala Cathedral)."
  open_questions:
    - "Page-image check of Species Plantarum 1753 Lectorem (currently Gutenberg) and Philosophia Botanica Creator pages (currently OCR)."
    - "Whether any in-span public statement matches Nemesis Divina's retributive Gud for C."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Staffan Müller-Wille"
    citation: "Müller-Wille, Staffan. \"Carolus Linnaeus.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Carolus-Linnaeus"
    url: "https://www.britannica.com/biography/Carolus-Linnaeus"
    accessed: 2026-10-19
    reliability_note: "Signed article; opening through 'The sexual system of classification' read."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Staffan Müller-Wille"
    citation: "Müller-Wille, Staffan. \"Carolus Linnaeus.\" Britannica Scholars (Britannica Kids). https://kids.britannica.com/scholars/article/Carolus-Linnaeus/48407"
    url: "https://kids.britannica.com/scholars/article/Carolus-Linnaeus/48407"
    accessed: 2026-10-19
    reliability_note: "Same article, later sections, read via search excerpt."
    source_quality: "reference entry"
    used_for: [basics, institutions, collaborators]
  - id: S3
    type: tertiary
    kind: encyclopedia
    author: "Encyclopaedia Britannica"
    citation: "\"Species Plantarum.\" Britannica Scholars. https://kids.britannica.com/scholars/article/Species-Plantarum/103290"
    url: "https://kids.britannica.com/scholars/article/Species-Plantarum/103290"
    accessed: 2026-10-19
    reliability_note: "Unsigned article, read via search excerpt."
    source_quality: "reference entry"
    used_for: [contribution, worldview, timing]
  - id: S4
    type: secondary
    kind: other
    author: "Wikiquote contributors"
    citation: "\"Carl Linnaeus.\" Wikiquote. https://en.wikiquote.org/wiki/Carl_Linnaeus"
    url: "https://en.wikiquote.org/wiki/Carl_Linnaeus"
    accessed: 2026-10-19
    reliability_note: "Latin quotations with sources named (Systema Naturae editions; Ramsbottom 1938); secondary. Finding aid only after deepen."
    source_quality: "unofficial web copy"
    used_for: [worldview, timing]
  - id: S5
    type: secondary
    kind: other
    author: "Creyentes Intelectuales (blog)"
    citation: "\"Carlos Linneo: 'El propósito de la Creación es la Gloria de Dios'.\" Creyentes Intelectuales, July 2014. http://creyentesintelectuales.blogspot.com/2014/07/carlos-linneo.html"
    url: "http://creyentesintelectuales.blogspot.com/2014/07/carlos-linneo.html"
    accessed: 2026-10-19
    reliability_note: "Advocacy blog; used only for its Latin transcription of the Imperium Naturae (note 9) and the Psalm placements; low reliability. Finding aid only."
    source_quality: "unofficial web copy"
    used_for: [worldview]
  - id: S6
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [review]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "Carl Linnaeus"
    citation: "Linnaeus, Carl. Systema naturae per regna tria naturae. 12th ed. Holmiae: L. Salvius, 1766. Scan: https://archive.org/details/bub_gb_siAOAAAAQAAJ"
    url: "https://archive.org/details/bub_gb_siAOAAAAQAAJ"
    accessed: 2026-10-19
    reliability_note: "Printed edition, Google Books scan with OCR; Imperium Naturae read (after span)."
    source_quality: "primary / own words"
    used_for: [worldview]
  - id: S8
    type: primary
    kind: "published work by the subject"
    author: "Carl Linnaeus"
    citation: "Linnaeus, Carl. Systema naturae. Regnum animale. Editio decima, 1758. Facsimile ed. Societas zoologica germanica. Lipsiae: W. Engelmann, 1894. Scan: https://archive.org/details/carolilinnaeisy01gesegoog"
    url: "https://archive.org/details/carolilinnaeisy01gesegoog"
    accessed: 2026-10-19
    reliability_note: "Page-for-page reprint of the 10th edition; Imperium Naturae, p. 5, read (after span)."
    source_quality: "primary / own words"
    used_for: [worldview]
  - id: S9
    type: primary
    kind: "published work by the subject"
    author: "Carl Linnaeus"
    citation: "Linnaeus, Carl. Systema naturae, sive regna tria naturae systematice proposita. Lugduni Batavorum: Theodor Haak, 1735. Scan: https://archive.org/details/mobot31753002972252"
    url: "https://archive.org/details/mobot31753002972252"
    accessed: 2026-10-19
    reliability_note: "First edition folio, Missouri Botanical Garden scan."
    source_quality: "primary / own words"
    used_for: [worldview]
  - id: S10
    type: primary
    kind: "published work by the subject"
    author: "Carl Linnaeus"
    citation: "Linnaeus, Carl. Species Plantarum. Stockholm: L. Salvius, 1753. Project Gutenberg eBook #20771 (transcription)."
    url: "https://www.gutenberg.org/ebooks/20771"
    accessed: 2026-10-24
    reliability_note: "Public-domain keyed transcription of the 1753 Latin; LECTORI ÆQUO and Swedish royal dedication read for Creator/Dominus language."
    source_quality: "unofficial web copy"
    used_for: [worldview, timing, contribution]
  - id: S11
    type: primary
    kind: "published work by the subject"
    author: "Carl Linnaeus"
    citation: "Linnaeus, Carl. Philosophia Botanica. Stockholm: G. Kiesewetter / Amsterdam: Z. Chatelain, 1751. Internet Archive scan philosophiabota00linn (OCR)."
    url: "https://archive.org/details/philosophiabota00linn"
    accessed: 2026-10-24
    reliability_note: "Printed 1751 treatise; IA OCR used this pass (Introductio arte divina; Creator/legem Naturæ; Nova creatio nulla; primordio creatum)."
    source_quality: "archive scan (OCR only)"
    used_for: [worldview]
  - id: S12
    type: primary
    kind: "published work by the subject"
    author: "Carl Linnaeus"
    citation: "Linnaeus, Carl. Systema naturæ … Editio quarta. Parisiis: M.-A. David, 1744. Internet Archive carolilinaeimedi00linn (OCR)."
    url: "https://archive.org/details/carolilinaeimedi00linn"
    accessed: 2026-10-24
    reliability_note: "Paris 4th edition; IA OCR used this pass (Creator / Artifex paragraph; primordio creatum)."
    source_quality: "archive scan (OCR only)"
    used_for: [worldview]
  - id: S13
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: 'Carl Linnaeus. Wikipedia. https://en.wikipedia.org/wiki/Carl_Linnaeus'
    url: "https://en.wikipedia.org/wiki/Carl_Linnaeus"
    accessed: 2026-10-24
    reliability_note: "Unsigned tertiary; used for dual-source bio (P50): parents, Lutheran minister father, death at Hammarby vs Britannica Uppsala, Species Plantarum 1753 dating."
    source_quality: "reference entry"
    used_for: [basics, childhood, heritage, review]
  - id: S14
    type: primary
    kind: "published work by the subject"
    author: "Carl Linnaeus; ed. Knut Barr"
    citation: "Linné, Carl von. Nemesis Divina. Utgiven och kommenterad av Knut Barr. Stockholm: Wahlström & Widstrand, 1923. Internet Archive nemesisdivina00linn."
    url: "https://archive.org/details/nemesisdivina00linn"
    accessed: 2026-10-24
    reliability_note: "Posthumous edition of a private manuscript compiled for his son; after the coded span; used only to close the C unread flag — not scored (P20)."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview]
  - id: S15
    type: secondary
    kind: "institutional page"
    author: "International Commission on Zoological Nomenclature"
    citation: "International Code of Zoological Nomenclature, 4th ed., Article 3 (Starting point). https://code.iczn.org/zoological-nomenclature/article-3-starting-point"
    url: "https://code.iczn.org/zoological-nomenclature/article-3-starting-point"
    accessed: 2026-10-26
    reliability_note: "Official Code text; Art. 3 and 3.1 read: 1 January 1758 starting point; Systema Naturae 10th ed. deemed published that day."
    source_quality: "reference entry"
    used_for: [contribution, timing]
---

## Summary

Carl Linnaeus (1707–1778), naturalist [S1; S13]. Draft: CHRIST (0.5); A 0 (0.7, alt 2); B 3 (0.7, alt 4); mid_basin true. Plotted (dark, filled) after RQ-Z5-N1 settled 2026-10-26.

## Life and work

Småland, Uppsala, the Netherlands, Uppsala; died Hammarby or Uppsala (sources disagree) [S1; S13].

## Contribution and impact

Systema Naturae; Species Plantarum binomial nomenclature; Philosophia Botanica [S1; S3; S10; S11].

## Childhood and education

Son of Lutheran minister Nils Linnaeus; Växjö; Lund and Uppsala [S1; S13].

## Adult working worldview

In-span: Species Plantarum 1753 Lectorem (omnipotentis / Domini / Creatoris / summum Ens) and Philosophia Botanica Creator / Nature's-law language [S10; S11; S12]. After-span Imperium Naturae kept as alt 2 / RQ-Z5-N1 lead only [S7; S8].

## Heritage (context only)

Swedish Lutheran [S1; S13].

## Timing

1735–1758, age 28 [S1; S15]. RQ-Z5-N1 settled 2026-10-26.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Page images for SP Lectorem and PB Creator pages.
- In-span public C matching Nemesis themes.

## Research log

- 2026-10-19: Read Britannica (Müller-Wille), Britannica Scholars, Wikiquote, blog transcription; Imperium Naturae in 1758/1766 prints.
- 2026-10-24: Deepen D1 — Species Plantarum Gutenberg Lectorem; Philosophia Botanica OCR; Systema 1744 OCR; Nemesis Divina Barr 1923; Wikipedia dual bio. A→0.7; B held @0.5; C unread flag closed without score.
- 2026-10-26: ICZN Art. 3 read; RQ-Z5-N1 settled; Imperium Naturae 1758 scored in-span.
