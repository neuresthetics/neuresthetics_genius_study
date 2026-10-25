---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA1; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #168, F 3, rank 178). Goals: Vence/Jazz primary if available; open A/primary carefully; do not force plot without B. Hunt: Musée Matisse Nice French 1951 letter to Mgr Rémond (Art Sacré juillet–août 1951) — chapel as 'chef-d'œuvre', 'vie consacrée à la recherche de la vérité', 'signification supérieure de ce monument' (commission / masterpiece framing, not creed); bishop-quoted 'Je commence par le profane… j'aboutis au divin' left lead (Rémond via L'Art sacré, not Matisse hand this pass); Flanner New Yorker 1951: once anticlerical, 'known to be not a practicing Catholic' — chapel ≠ doctrine. Jazz re-read Private Print Flam Matisse on Art: French sense via Wikiquote mirror; Répertoire:6 / Schneider 1984 p.710 n.35 'divine pilot' draft variant logged as lead (unpublished notebook, after span). Spurling Unknown Matisse (NYT first chapter): baptized seven days old Le Cateau; confirmed 1881 St-Martin Bohain; raised Republicans and Roman Catholics; later distaste for Catholic upbringing; Hail Marys/Paternosters as nerve-calm (heritage). primary BELOW_THRESHOLD kept (Jazz conditional work-bound belief + refused gratitude; CHRIST/AGNOS leads only; after-span P20). A BELOW kept (helper/agent thin; no locus; after span). B UNKNOWN (not scientist; no nature-order). mid BELOW; not plotted. Chart-moving NO. P47 source_quality; P48; P50 Wikipedia. No fallacy_catalog; no figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "AA1 audit note: added the Met 'Fauvism' essay (Sabine Rewald, 2004) as S4, corroborating the 1905 Salon d'Automne dating; search-excerpt labels kept. No value changes."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA1, order P32: F 3, rank 178). Basics from Britannica (Roy Donald McMullen, signed; body). Lasting work and dating from the Met's Heilbrunn essay 'Henri Matisse (1869–1954)' (body, seen as a search excerpt): Woman with a Hat, 'when exhibited at the 1905 Salon d'Automne', gave rise to Fauvism; public exhibition is the P30 #1 dating event (RQ-Z7-N1). Own words: Jazz (published 30 September 1947), after the span, in Jack Flam's translation (web copy of Matisse on Art): 'Do I believe in God? Yes, when I work ... I feel no gratitude toward Him'. Conditional, work-bound belief with refused acknowledgement, so primary_system BELOW_THRESHOLD (leads CHRIST: Vence chapel, not read; PANT not supported); A BELOW_THRESHOLD; not a scientist, B UNKNOWN; C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Span 1905, age 36 (1905 − 1869). Not plotted. Draft, not reviewed."}

identity:
  id: matisse-henri
  display_name: "Henri Matisse"
  roster:
    canonical_name: "Henri Matisse"
    rank: 178
    F: 3
    models: [Claude, Gemini, GPT]
    band: "core (3–4)"
    status: "core"
    field: "art"
    field_bucket: "arts"
  full_name: {value: "Henri-Émile-Benoît Matisse", certainty: 0.7, cites: [{source: S1, locator: "heading"}], how_known: "Britannica."}
  native_name: {value: "Henri Matisse", certainty: 0.7, cites: [{source: S1, locator: "heading"}], how_known: "Britannica."}
  aliases:
    - {name: "Matisse-Henri", kind: "roster alias"}

basics:
  birth:
    date: {value: "1869-12-31", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Le Cateau, Picardy", modern_name: "Le Cateau-Cambrésis, France", polity_then: "France", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1954-11-03", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Nice", modern_name: "Nice, France", polity_then: "France", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1905, certainty: 0.7, cites: [{source: S2, locator: "Fauvist period"}], how_known: "Woman with a Hat exhibited at the 1905 Salon d'Automne, which 'gave rise to the first of the avant-garde movements ... named \"Fauvism\"' (S2); public exhibition dates artworks (P30 #1, RQ-Z7-N1)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S2, locator: "Fauvist period"}], how_known: "1905 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "France (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Formative years"}], how_known: "Paris; later Nice."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["French"], certainty: 0.7, cites: [{source: S3, locator: "Jazz text"}], how_known: "French text."}
  occupations: {value: ["painter", "sculptor", "printmaker"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["painting"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Fauvism (Woman with a Hat)", year: 1905, kind: "work", lasting: "'leader of the Fauvist movement' (S1, body); Woman with a Hat 'gave rise to the first of the avant-garde movements' (S2, body)", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Fauvist period"}, {source: S4, locator: "para. 2"}], how_known: "Britannica and the Met essays; dated by the 1905 Salon d'Automne showing (S2; S4: 'When their pictures were exhibited later that year at the Salon d'Automne')."}
  evidence_of_impact:
    - {value: "Often regarded as the most important French painter of the 20th century", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Le Bonheur de vivre", year: 1906, kind: "artwork", certainty: 0.5, cites: [{source: S2, locator: "Fauvist period"}], how_known: "Met: 1905–6; shown at the 1906 Salon des Indépendants (not in the source read); not called lasting."}
    - {value: "Jazz", year: 1947, kind: "book", certainty: 0.7, cites: [{source: S3, locator: "introduction"}], how_known: "Published 30 September 1947 (Flam)."}
    - {value: "Chapelle du Rosaire (Vence)", year: 1951, kind: "artwork", certainty: 0.7, cites: [{source: S6, locator: "letter / consecration 25 June 1951"}, {source: S8, locator: "chapel consecration"}], how_known: "Consecrated 25 June 1951; Matisse's design of the Dominican chapel (after the span)."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Most important French painter of the 20th century (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Roman Catholic (Republicans and Roman Catholics, class custom)", certainty: 0.7, cites: [{source: S7, locator: "Bohain childhood; baptism/confirmation"}], how_known: "Spurling: sons 'brought up as good Republicans and Roman Catholics according to the custom of their class and time'."}
  family_religious_practice: {value: "Catholic baptism and confirmation; later distaste for the upbringing (heritage, not adult creed)", certainty: 0.7, cites: [{source: S7, locator: "baptism; confirmation 1881; distaste"}], how_known: "Spurling."}
  parents_and_household:
    - {value: "Father Hippolyte Henri Matisse (seed-merchant, Bohain); mother Anna Héloïse Gérard (housepaints / colour sense)", certainty: 0.7, cites: [{source: S7, locator: "opening chapters"}], how_known: "Spurling."}
  household_circumstances: {value: "Rising provincial shopkeeping / seed-merchant household in industrialising Bohain; earlier weaver's cottage birth at Le Cateau", certainty: 0.7, cites: [{source: S7, locator: "Bohain; Le Cateau"}], how_known: "Spurling."}
  schooling:
    - {value: "Primary school Bohain; Collège of Le Cateau (day boy with grandmother); later Saint-Quentin", stage: "grammar or secondary school", years: "c. 1870s–1880s", certainty: 0.5, cites: [{source: S7, locator: "schooling"}, {source: S1, locator: "Formative years"}], how_known: "Spurling + Britannica (Saint-Quentin law clerk path)."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["French"], certainty: 0.5, cites: [{source: S7, locator: "patois"}], how_known: "Spurling (also notes Picard/Flemish patois of Bohain)."}
  notable_events:
    - {value: "Confirmed 1881, church of St-Martin, Bohain", year: 1881, certainty: 0.7, cites: [{source: S7, locator: "confirmation 1881"}], how_known: "Spurling."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1905", certainty: 0.7, cites: [{source: S2, locator: "Fauvist period"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Baptized and confirmed Roman Catholic (childhood); designed Chapelle du Rosaire for Dominican sisters at Vence (1947–51); Flanner: not a practicing Catholic, once anticlerical", certainty: 0.7, cites: [{source: S7, locator: "baptism/confirmation"}, {source: S6, locator: "chapel"}, {source: S8, locator: "not a practicing Catholic"}], how_known: "Heritage + public commission + contemporary profile. Chapel commission ≠ CHRIST doctrine (standing rule; CHRIST.md membership ≠ ideology)."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not a scientist; no science–religion statement read."}
  primary_system:
    value: BELOW_THRESHOLD
    how_known: "Jazz (1947, after the span; P20): 'Do I believe in God? Yes, when I work' / French 'Oui, quand je travaille', helper 'someone who makes me do things that surpass myself', yet 'I feel no gratitude toward Him' / conjurer — conditional work-bound belief with refused acknowledgement, no doctrine. Vence 1951 letter (S6): presents the chapel as 'chef-d'œuvre' and a life 'consacrée à la recherche de la vérité' with 'signification supérieure' — masterpiece / truth-seeking framing for a Dominican commission, not a creed (Flanner S8: not practicing Catholic). Leads CHRIST (chapel + Christian imagery / Imitation of Christ bedside in Flam notes) and AGNOS (belief only when working). PANT fails part 1 (no God–Nature identity). Do not open primary."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Lead only: Vence Dominican chapel commission and 1951 letter; Jazz 'communicant' simile and à Kempis bedside (Flam notes). Commission ≠ doctrine; Flanner not practicing; Jazz refuses gratitude."}
    - {code: AGNOS, reason: "Lead only: belief affirmed only 'when I work'; suspension outside work moods."}
    - {code: PANT, reason: "Rejected: no God–Nature identity statement."}
  lio_axes:
    A_locus:
      value: BELOW_THRESHOLD
      how_known: "Jazz helper 'who makes me do things that surpass myself' and Répertoire:6 draft 'divine pilot' (Schneider via Flam n.35, unpublished, after span) suggest an agent beyond him, but belief is conditional, gratitude refused, no locus (0 vs 1) stated, and both texts are after the 1905 span (P20). Named reading A 1 does not reach 0.5. Do not force open A."
      alternatives:
        - {value: 1, note: "Helper/agent beyond the painter (Jazz 'someone'; draft 'divine pilot') — thin, after-span, conditional.", cites: [{source: S3, locator: "Jazz, 'Do I believe in God?'; note 15"}]}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30/P33); no statement on nature or cause-order read. Do not invent B from colour/light talk or chapel fenestration."}
    C_ledger: {value: UNKNOWN, how_known: "Jazz 'Future life' consolation for those who developed talents is hedged wish, after span; not scored."}
    D_authority: {value: UNKNOWN, how_known: "Not scored."}
    E_scope: {value: UNKNOWN, how_known: "Not scored."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD and B_cause UNKNOWN; P4 test cannot be applied. Do not force plot without B."}
  statements:
    - text: "Do I believe in God? Yes, when I work. When I am submissive and modest. I sense myself helped immensely by someone who makes me do things that surpass myself. Still, I feel no gratitude toward Him because it is as if I were watching a conjurer whose tricks I cannot see through. I then find myself thwarted of the profit of the experience that should be the reward for my effort. I am ungrateful without remorse."
      cites: [{source: S3, locator: "Jazz, 'Do I believe in God?'"}]
      date: "1947"
      context: "Jazz (Tériade, 1947), handwritten text; after the span."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Jack Flam translation (Matisse on Art) via Private Print. French sense (Wikiquote / web mirrors): 'Si je crois en Dieu? Oui, quand je travaille… Pourtant je ne me sens envers lui aucune reconnaissance car c'est comme si je me trouvais devant un prestidigitateur…'. Not checked against the 1947 printing or Flam's book pages (0.7 cap, §7)."
    - text: "Si je crois en Dieu? Oui, quand je travaille. Quand je suis soumis et modeste, je me sens tellement aidé par quelqu'un qui me fait faire des choses qui me surpassent. Pourtant je ne me sens envers lui aucune reconnaissance car c'est comme si je me trouvais devant un prestidigitateur dont je ne puis percer les tours."
      cites: [{source: S9, locator: "Jazz (1947) French"}, {source: S3, locator: "English parallel"}]
      date: "1947"
      context: "Same Jazz passage; French as mirrored on Wikiquote (P50 wiki caution)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "French corroboration of sense for S3; wiki mirror, not 1947 printing. Lead/corroboration under P26/P50."
    - text: "I am guided like a medium pure and simple. If my pride gets in the way, my work does not go very well and after a few oaths I come round and give in to it again and things improve since my mind is set at rest by my own powerlessness when I feel the divine pilot is not with me."
      cites: [{source: S3, locator: "Flam note 15; Schneider 1984 p. 710 n. 35"}]
      date: "1946"
      context: "Répertoire:6 draft variant of the Jazz God passage; unpublished notebook, after the span."
      axes: [A_locus]
      kind: "other"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Flam cites Schneider 1984 n.35; draft not the published Jazz text. Lead strengthening work-bound helper language; does not open A or primary."
    - text: "Excellence, Je vous présente en toute humilité la chapelle du Rosaire de Vence. … Cette œuvre m'a demandé quatre ans de travail exclusif et assidu, et elle est le résultat de toute ma vie active. Je la considère malgré toutes ses imperfections comme mon chef-d'œuvre. … Je compte, Excellence, sur votre longue expérience des hommes et votre haute sagesse pour juger un effort qui est le résultat d'une vie consacrée à la recherche de la vérité."
      cites: [{source: S6, locator: "Letter to Mgr Rémond; Art Sacré n°11-12 juillet–août 1951"}]
      date: "1951-06"
      context: "Letter read at consecration of Chapelle du Rosaire, 25 June 1951 (Matisse absent); after the span."
      axes: []
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "French text as given by Musée Matisse Nice (exhibition page quoting Art Sacré). Masterpiece / truth-seeking presentation of a Dominican commission — not scored as CHRIST doctrine (Flanner: not practicing Catholic)."
    - text: "I started with the secular and now in the evening of my life, I naturally end with the divine."
      cites: [{source: S6, locator: "quoted by Monsignor Rémond, L'Art sacré, July–August 1951"}]
      date: "1951"
      context: "Attributed to Matisse by Bishop Rémond in L'Art sacré; Musée Matisse English page."
      axes: []
      kind: "other"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Bishop's quotation, not Matisse hand this pass. Lead only — does not open primary or A."
  changes_over_life:
    - {value: "Late religious-art commission: Chapelle du Rosaire, Vence (design from c. 1947; consecrated 1951), with 1951 letter to the Bishop of Nice framing the chapel as his masterpiece and a life given to 'recherche de la vérité'. Contemporary profile: not a practicing Catholic, formerly anticlerical (Flanner). Same after-span window as Jazz (1947). Does not split the 1905 span scores (P31); after-span evidence at P20 weight. Heritage Catholic baptism/confirmation ≠ adult code.", year: 1951, certainty: 0.7, cites: [{source: S6, locator: "1951 letter"}, {source: S8, locator: "not practicing Catholic"}, {source: S3, locator: "Jazz 1947"}], how_known: "Museum letter + Flanner + Jazz."}
  coder_notes: "Deepen D1 (#168): Vence letter and Jazz/Flam notes filled; Schneider divine-pilot draft logged; Spurling heritage filled. primary/A stay BELOW; B UNKNOWN; chart-moving NO. Art Sacré page images / 1947 Jazz printing / Schneider monograph pages still blockers. Do not touch figures/. No fallacy_catalog."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "French Flemish / Picard northern stock (Matisse–Gérard weaver and tanner families)", certainty: 0.7, cites: [{source: S7, locator: "family origins"}], how_known: "Spurling."}
  religious_heritage_by_birth: {value: "Roman Catholic (Republicans and Roman Catholics of the class)", certainty: 0.7, cites: [{source: S7, locator: "brought up as … Roman Catholics"}], how_known: "Spurling. Heritage ≠ worldview code."}
  baptism_or_initiation: {value: "Baptized at seven days old before leaving Le Cateau; confirmed 1881, St-Martin, Bohain", certainty: 0.7, cites: [{source: S7, locator: "baptism; confirmation 1881"}], how_known: "Spurling (biography; parish registers not imaged this pass)."}
  childhood_catechism: {value: "Hail Marys and Paternosters of childhood; seventy years later still used to calm nerves (Spurling)", certainty: 0.5, cites: [{source: S7, locator: "Hail Marys and Paternosters"}], how_known: "Spurling paraphrase of late reminiscence; heritage practice, not adult creed."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1905", certainty: 0.7, cites: [{source: S2, locator: "Fauvist period"}], how_known: "The 1905 Salon d'Automne showing, the one supported lasting work (P29, P30 #1)."}
  age_at_first_lasting_contribution: {value: 36, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "1905 − 1869 = 36 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: "1947 (Jazz God passage; after span)", certainty: 0.5, cites: [{source: S3, locator: "Jazz"}], how_known: "First own-words God statement read; after span."}
  lio_views_relative_to_major_work: {value: "after major work", certainty: 0.7, cites: [{source: S3, locator: "1947"}, {source: S2, locator: "1905"}], how_known: "Scored religious texts are 1947/1951; lasting contribution 1905."}
  worldview_during_major_work: {value: "UNKNOWN for 1905 Fauve years; scored religious statements are after-span Jazz (1947) and Vence letter (1951), kept at BELOW_THRESHOLD under P20.", certainty: 0.5, cites: [{source: S3, locator: "Jazz"}, {source: S6, locator: "1951 letter"}], how_known: "No in-span creed texts read."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Expressive colour (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No Lane B data. Do not invent B from colour, light, or chapel design."
  notes: ""

institutions: []
collaborators:
  - {value: "Gustave Moreau", relation: "teacher", note: "atelier, École des Beaux-Arts", certainty: 0.7, cites: [{source: S1, locator: "Formative years"}], how_known: "Britannica."}
  - {value: "Sister Jacques-Marie (Monique Bourgeois)", relation: "collaborator", note: "former nurse/model; Dominican; sparked Vence chapel project", certainty: 0.7, cites: [{source: S6, locator: "Sister Jacques-Marie"}, {source: S8, locator: "Sœur Jacques"}], how_known: "Musée Matisse; Flanner."}
  - {value: "Père Marie-Alain Couturier", relation: "collaborator", note: "Dominican; Art Sacré movement; chapel", certainty: 0.7, cites: [{source: S6, locator: "Couturier"}, {source: S8, locator: "Père Couturier"}], how_known: "Two sources."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 178"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Jazz and Vence letter are after the 1905 span (P20)."
    - "Jazz Flam text is unofficial web copy; 1947 printing unread."
    - "Divine-pilot variant is unpublished Répertoire:6 via Schneider/Flam note."
    - "Bishop-quoted 'secular…divine' is secondary (Rémond)."
  open_questions:
    - "1947 Jazz printing / Flam book pages vs web copy."
    - "Schneider 1984 monograph pages for Répertoire:6."
    - "Art Sacré 1951 page images of the full letter."
    - "Any in-span (c. 1905) own-words on God or nature."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Roy Donald McMullen"
    citation: "McMullen, Roy Donald. 'Henri Matisse.' Encyclopaedia Britannica (rev. 28 August 2026). https://www.britannica.com/biography/Henri-Matisse"
    url: "https://www.britannica.com/biography/Henri-Matisse"
    accessed: 2026-10-19
    reliability_note: "Signed article; body cited, question boxes not used (P26)."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, lane_b, collaborators]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "The Metropolitan Museum of Art (Heilbrunn Timeline of Art History)"
    citation: "'Henri Matisse (1869–1954).' Heilbrunn Timeline of Art History, The Metropolitan Museum of Art. https://www.metmuseum.org/essays/henri-matisse-1869-1954"
    url: "https://www.metmuseum.org/essays/henri-matisse-1869-1954"
    accessed: 2026-10-19
    reliability_note: "Museum reference essay body, seen as a search excerpt; author not recorded."
    source_quality: "other"
    used_for: [basics, contribution, timing]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Henri Matisse (trans. Jack Flam)"
    citation: "Matisse, Henri. Jazz (Paris: Tériade, 1947), text in Jack Flam, Matisse on Art; web copy at Private Print (2019). https://privateprint.mk/en/blog/dzhez"
    url: "https://privateprint.mk/en/blog/dzhez"
    accessed: 2026-10-24
    reliability_note: "Unofficial web copy of Flam's translation with notes including Schneider 1984 n.35 (0.7 cap, §7). Re-fetched D1."
    source_quality: "unofficial web copy"
    used_for: [worldview, contribution]
  - id: S4
    type: secondary
    kind: "institutional page"
    author: "Sabine Rewald"
    citation: "Rewald, Sabine. 'Fauvism.' Heilbrunn Timeline of Art History, The Metropolitan Museum of Art (October 2004). https://www.metmuseum.org/en/essays/fauvism"
    url: "https://www.metmuseum.org/en/essays/fauvism"
    accessed: 2026-10-19
    reliability_note: "Signed museum reference essay, seen as a search excerpt (page behind a bot check); corroborates S2."
    source_quality: "other"
    used_for: [contribution, timing]
  - id: S5
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [review]
  - id: S6
    type: primary
    kind: "letter"
    author: "Henri Matisse (letter); Musée Matisse Nice (quotation)"
    citation: "Letter to Monsignor Rémond, Bishop of Nice (June 1951), published L'Art sacré n°11-12 (juillet–août 1951); French text quoted by Musée Matisse Nice. https://www.musee-matisse-nice.org/fr/exposition/les-cinquante-ans-de-la-chapelle-du-rosaire-de-la-passion-a-la-resurrection/ ; English context https://www.musee-matisse-nice.org/en/the-artist/matisse-and-the-rosary-chapel/"
    url: "https://www.musee-matisse-nice.org/fr/exposition/les-cinquante-ans-de-la-chapelle-du-rosaire-de-la-passion-a-la-resurrection/"
    accessed: 2026-10-24
    reliability_note: "Museum quotation of the letter as published in Art Sacré; page images of Art Sacré unread. Bishop-quoted 'secular…divine' on the English page is secondary (Rémond)."
    source_quality: "primary / own words"
    used_for: [worldview, contribution, collaborators]
  - id: S7
    type: secondary
    kind: "scholarly book"
    author: "Hilary Spurling"
    citation: "Spurling, Hilary. The Unknown Matisse: A Life of Henri Matisse, the Early Years, 1869–1908 (Knopf). Chapter 1 excerpt, New York Times Books First. https://archive.nytimes.com/www.nytimes.com/books/first/s/spurling-matisse.html"
    url: "https://archive.nytimes.com/www.nytimes.com/books/first/s/spurling-matisse.html"
    accessed: 2026-10-24
    reliability_note: "Signed biography first chapter (NYT Books First excerpt); baptism/confirmation and Catholic upbringing from this text. Parish registers not imaged."
    source_quality: "scholarly edition or monograph"
    used_for: [childhood, heritage]
  - id: S8
    type: secondary
    kind: "journal article"
    author: "Janet Flanner"
    citation: "Flanner, Janet. 'How War Changed the Way We See Matisse' (King of the Wild Beasts II). The New Yorker (22 December 1951; magazine dated 29 December 1951). https://www.newyorker.com/magazine/1951/12/29/henri-matisse-profile-king-of-the-wild-beasts-ii"
    url: "https://www.newyorker.com/magazine/1951/12/29/henri-matisse-profile-king-of-the-wild-beasts-ii"
    accessed: 2026-10-24
    reliability_note: "Contemporary profile; states Matisse was once anticlerical and 'known to be not a practicing Catholic'. Secondary on practice."
    source_quality: "newspaper interview"
    used_for: [worldview, contribution, collaborators]
  - id: S9
    type: primary
    kind: "published work by the subject"
    author: "Henri Matisse (French Jazz text via Wikiquote mirror)"
    citation: "Matisse, Henri. Jazz (1947), French text as mirrored at Wikiquote 'Henri Matisse'. https://en.wikiquote.org/wiki/Henri_Matisse"
    url: "https://en.wikiquote.org/wiki/Henri_Matisse"
    accessed: 2026-10-24
    reliability_note: "Wiki mirror of French Jazz lines (P50 Wikipedia caution); used only to corroborate sense of S3 Flam English. Not a scored sole source."
    source_quality: "unofficial web copy"
    used_for: [worldview]
---

## Summary

Henri Matisse (1869–1954), painter [S1]. Deepen D1: primary BELOW_THRESHOLD (leads CHRIST, AGNOS); A BELOW; B UNKNOWN; mid BELOW. Not plotted.

## Life and work

Paris; Nice; Vence chapel 1947–51 [S1, S6].

## Contribution and impact

Fauvism, 1905 [S1, S2, S4]. Jazz 1947; Chapelle du Rosaire 1951 [S3, S6].

## Childhood and education

Bohain / Le Cateau; Roman Catholic baptism and 1881 confirmation; Republicans and Catholics [S7]. Saint-Quentin; law clerk [S1].

## Adult working worldview

Jazz (1947, after span): 'Do I believe in God? Yes, when I work' — conditional, no gratitude [S3]. Vence 1951 letter: chapel as masterpiece / 'recherche de la vérité' — commission, not creed [S6]; Flanner: not practicing Catholic [S8].

## Heritage (context only)

Roman Catholic by birth and initiation [S7]. Heritage ≠ worldview code.

## Timing

1905, age 36 [S2]. Religious statements 1947/1951 after major work.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data. Do not invent B.

## Open questions

- 1947 Jazz printing / Flam book pages.
- Schneider 1984 Répertoire:6 pages.
- Art Sacré 1951 page images.
- In-span (c. 1905) own-words on God or nature.

## Research log

- 2026-10-24: Deepen D1 — Musée Matisse Vence letter (FR); Private Print Jazz/Flam notes (divine pilot); Spurling NYT first chapter (baptism/confirmation); Flanner New Yorker 1951 (not practicing); Wikiquote French Jazz mirror. Scores unchanged (BELOW / UNKNOWN). Chart-moving NO.
- 2026-10-19: AA1 audit note: added the Met 'Fauvism' essay (Sabine Rewald, 2004) as S4, corroborating the 1905 Salon d'Automne dating; search-excerpt labels kept. No value changes.
- 2026-10-19: Read Britannica (McMullen); Met essay excerpt; Jazz text (Flam).
