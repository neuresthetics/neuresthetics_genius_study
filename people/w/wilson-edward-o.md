---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z7)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 20c_late. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #155, F 3, rank 163). P31 continuity: create-pass P20 0.5 cap on after-span interviews superseded — no documented change of view between 1971–1975 and 1978/1998/2006 (Baptist→secular ~1946 is pre-span). New S5 On Human Nature (1978) Ch.1 written_profession: 'genetic chance and environmental necessity, not God, made the species. Deity can still be sought in the origin of the ultimate units of matter… but not in the origin of species'; species 'lack any immanent purpose or guidance from agents beyond their immediate environment'. Multi-secondary agreement (Miller Finding Darwin's God p.180; Whitman academic citation 1978/2004:1–2; HUP sample search-index). P47 source_quality on every source. P50 Wikipedia S6 dual-bio. primary_system DEISM 0.5→0.7 recorded_interview (S2+S3; OHN content matches); A 3 0.5→0.7 written_profession (OHN + interviews), alts 1 and BELOW; B 3 0.5→0.7 written_profession (OHN + Salon no-intervention; P35 inference-only cap no longer binds), alt 4; support corroborated both axes (P48). mid_basin BELOW_THRESHOLD→false @0.7 (A≥3 branch, P10). Chart-moving YES: faded→dark (min A/B cert 0.5→0.7); fill already filled. Span kept 1971–1975 (coder's P29/P30 call; OHN stays major_works, cited under P31). No fallacy_catalog. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z7 audit fix (P10): mid_basin false 0.5 -> BELOW_THRESHOLD; RQ-Z7-1 answered: A 3 at 0.5 holds (Franklin precedent)."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z7, order P32: F 3, rank 163). Basics from Britannica (Michael Ruse, signed). Own words: Psychology Today interview (1998) and Salon interview (2006), both after the span: 'a provisional deist is someone like myself who leaves it open'; 'I do feel confident that there is no intervention of a deity in the origin of life and humanity'; raised 'a devout Southern Baptist'. Scientist (P30). Span 1971–1975. primary_system DEISM (0.5, alt AGNOS); A 3 (0.5; alts 1 and BELOW_THRESHOLD): explicit denial of a personal, intervening God (P20), with at most an impersonal 'creative force'; B 3 (0.5, alt 4; P35, P16 addendum); C, D, E UNKNOWN; mid_basin false (0.5; A ≥ 3 branch). Plotted (A 3, B 3). Draft, not reviewed."}

identity:
  id: wilson-edward-o
  display_name: "E. O. Wilson"
  roster:
    canonical_name: "Edward O. Wilson"
    rank: 163
    F: 3
    models: [Claude, Gemini, GPT]
    band: "core (3–4)"
    status: "core"
    field: "biology"
    field_bucket: "biology / life science"
  full_name: {value: "Edward Osborne Wilson", certainty: 0.7, cites: [{source: S1, locator: "In full"}, {source: S6, locator: "lead"}], how_known: "Britannica and Wikipedia agree (P50)."}
  native_name: {value: "Edward O. Wilson", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "lead"}], how_known: "Britannica and Wikipedia."}
  aliases:
    - {name: "E-O-Wilson", kind: "roster alias"}
    - {name: "E.O. Wilson", kind: "roster alias"}
    - {name: "Edward O- Wilson", kind: "roster alias"}
    - {name: "Wilson-Edward O-", kind: "roster alias"}

basics:
  birth:
    date: {value: "1929-06-10", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "lead"}], how_known: "Britannica and Wikipedia agree."}
    place: {value: "Birmingham, Alabama", modern_name: "Birmingham, Alabama, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "Early life"}], how_known: "Britannica and Wikipedia agree."}
  death:
    date: {value: "2021-12-26", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "lead"}], how_known: "Britannica and Wikipedia agree."}
    place: {value: "Burlington, Massachusetts", modern_name: "Burlington, Massachusetts, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "Death"}], how_known: "Britannica and Wikipedia agree."}
  first_lasting_contribution_year: {value: 1971, certainty: 0.5, cites: [{source: S1, locator: "body"}], how_known: "The Insect Societies (1971), 'his definitive work'; earlier pheromone and taxon-cycle work is undated in the body, so 0.5."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "body"}], how_known: "1971 (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "USA (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Harvard."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Inferred."}
  occupations: {value: ["biologist", "entomologist", "professor"], certainty: 0.7, cites: [{source: S1, locator: "body"}, {source: S6, locator: "lead"}], how_known: "Britannica and Wikipedia."}

contribution:
  era_bucket: 20c_late
  fields: {value: ["myrmecology", "sociobiology", "biodiversity"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "lead"}], how_known: "Britannica and Wikipedia."}
  lasting_original_contributions:
    - {value: "The Insect Societies", year: 1971, kind: "work", lasting: "'his definitive work on ants and other social insects' (S1)", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Britannica."}
    - {value: "Sociobiology: The New Synthesis (kin-selection account of altruism)", year: 1975, kind: "theory", lasting: "founded sociobiology as its 'foremost proponent' (S1)", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "Crafoord Prize 1990; Pulitzer Prizes 1979 and 1991", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Britannica."}
  major_works:
    - {value: "On Human Nature", year: 1978, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Britannica; Pulitzer 1979. Not added to lasting_original_contributions this pass — span kept 1971–1975 by the create-pass coder's call; cited for worldview under P31."}
    - {value: "Consilience", year: 1998, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Britannica."}
  honours:
    - {value: "Crafoord Prize", year: 1990, certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "World authority on ants; founder of sociobiology (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Southern Baptist (fundamentalist)", certainty: 0.7, cites: [{source: S3, locator: "'You grew up in a religious family?'"}, {source: S7, locator: "'went under the water'"}], how_known: "(interview) 'I grew up as a Southern Baptist with strict adherence to the Bible' (S3); High Profiles: raised in the Southern Baptist Convention (S7)."}
  family_religious_practice: {value: "Baptised at 14 ('went under the water'); faithful boy until late adolescence", certainty: 0.7, cites: [{source: S7, locator: "'went under the water'"}], how_known: "(interview) High Profiles (S7)."}
  parents_and_household: []
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["English"], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Inferred."}
  notable_events:
    - {value: "Childhood eye injury and adolescent partial deafness turned him from birds to insects", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Britannica."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1971–1975", certainty: 0.5, cites: [{source: S1, locator: "body"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Evolutionary biology leaves very little room for a theistic God; religious belief itself is an adaptation (interview titles / body); scientific humanism as worldview compatible with science (Wikipedia paraphrase of Consilience-era claim, not scored as system)", certainty: 0.5, cites: [{source: S2, locator: "'evolutionary biology leaves very little room'"}, {source: S3, locator: "title / religion-as-adaptation exchange"}, {source: S6, locator: "Scientific humanism"}], how_known: "Interviews plus Wikipedia secondary; Consilience first-hand not borrowed this pass."}
  primary_system:
    value: DEISM
    basis: recorded_interview
    certainty: 0.7
    cites: [{source: S2, locator: "'You call yourself a deist'"}, {source: S3, locator: "'I've heard you call yourself a deist'"}, {source: S5, locator: "Ch. 1 Dilemma, pp. 1–2 (2004)"}]
    how_known: "(interview) 1998 and 2006 at the recorded_interview ceiling 0.7. P31: no change of view documented between the 1971–1975 span and these interviews (Baptist→secular ~1946 is pre-span). Near-span written_profession OHN 1978 matches the provisional-deist content (deity open at matter origin, not species). Named alternative AGNOS, so 0.7 not 1.0."
    rationale: "Self-described 'provisional deist': 'a deist is a person who's willing to buy the idea that some creative force determined the parameters of the universe when it began' and 'leaves it open' (S2); 'I am not a theist, but I'll be a provisional deist' / 'no intervention of a deity in the origin of life and humanity' (S3). OHN Ch.1: deity may be sought in quarks/matter origin 'but not in the origin of species' (S5). Alternative AGNOS: Wikipedia notes he also preferred 'agnostic' over 'atheist' in some summaries (S6); he rejects the AGNOS label in S2 as 'arrogantly dismiss[ing] the whole thing', so DEISM stays primary."
    alternatives:
      - {value: AGNOS, note: "Leaves the creator question open; Wikipedia 'preferring agnostic' paraphrase (S6); he rejects the label in S2.", cites: [{source: S2, locator: "'to say you're agnostic'"}, {source: S6, locator: "God and religion"}]}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: DEISM, reason: "Coded: his own label (provisional deist); OHN content matches."}
    - {code: AGNOS, reason: "Named alternative: leaves it open; Wikipedia prefers-agnostic note; he rejects the label in S2."}
    - {code: ATHE, reason: "Rejected: he refuses the atheist label ('claim knowledge you cannot have'); keeps cosmological-creator hypothesis open."}
  lio_axes:
    A_locus:
      value: 3
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S5, locator: "Ch. 1 Dilemma, pp. 1–2 (2004)"}, {source: S2, locator: "'You call yourself a deist'"}, {source: S3, locator: "'distinction between theism and deism'"}]
      how_known: "Near-span published book (OHN 1978) plus matching interviews. P31 continuity (no post-span change). Named alternatives, so 0.7 not 1.0. Independent source ids → corroborated (P48)."
      rationale: "Explicit denial of a personal intervening God in life's and humanity's origin: 'not God, made the species' (S5); 'no intervention of a deity in the origin of life and humanity' (S3); 'evolutionary biology leaves very little room for a theistic God' (S2). What he leaves open is 'some creative force' / 'super-intelligent force' / deity at 'quarks and electron shells', not a person who acts in the living world — so 3, not the DEISM-system default A 1. Alternatives: 1 (deist creator read as distant transcendent person, matching system DEISM); BELOW_THRESHOLD (creator question left open / 'provisional')."
      alternatives:
        - {value: 1, note: "Deist creator read as a distant transcendent person (system DEISM A 1).", cites: [{source: S2, locator: "'You call yourself a deist'"}, {source: S5, locator: "Deity can still be sought"}]}
        - {value: BELOW_THRESHOLD, note: "The creator question left open ('provisional').", cites: [{source: S3, locator: "'provisional'"}]}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S5, locator: "Ch. 1 Dilemma, pp. 1–2 (2004)"}, {source: S3, locator: "'I do feel confident'"}]
      how_known: "Own published book near the span (OHN 1978) plus matching interview. P31. Named alternative, so 0.7. Independent source ids → corroborated (P48). P35's working-science-only 0.5 cap no longer binds — he states cause and exception for living nature."
      rationale: "Scored on his account of nature (P6, P16). OHN: species made by 'genetic chance and environmental necessity, not God'; they 'lack any immanent purpose or guidance from agents beyond their immediate environment'; deity open only at matter/quarks origin, 'not in the origin of species' (S5). Salon: 'no intervention of a deity in the origin of life and humanity' (S3). Stated general lawfulness for the living world with one stated, limited exception at the cosmological/matter origin — B 3 under the B 3 anchor (Darwin / P27 pattern), not bare P35 inference. Named alternative 4: if the cosmological-deity opening is read as empty and nature is exceptionless throughout."
      alternatives:
        - {value: 4, note: "If the matter-origin deity line is read as a residual hedge rather than a stated exception, leaving exceptionless natural causation (P35-style alt).", cites: [{source: S5, locator: "Ch. 1 Dilemma"}, {source: S3, locator: "'no intervention'"}]}
    C_ledger: {value: UNKNOWN, how_known: "Not scored this pass."}
    D_authority: {value: UNKNOWN, how_known: "Not scored this pass."}
    E_scope: {value: UNKNOWN, how_known: "Not scored this pass."}
  mid_basin: {value: false, certainty: 0.7, cites: [{source: S5, locator: "Ch. 1 Dilemma, pp. 1–2"}, {source: S2, locator: "'You call yourself a deist'"}, {source: S3, locator: "'distinction between theism and deism'"}], how_known: "A_locus 3 at 0.7: the A ≥ 3 branch reads A only (P10). Deepen D1 lifted A past the 0.5 BELOW_THRESHOLD of the Z7 audit."}
  statements:
    - text: "If humankind evolved by Darwinian natural selection, genetic chance and environmental necessity, not God, made the species. Deity can still be sought in the origin of the ultimate units of matter, in quarks and electron shells (Hans Küng was right to ask atheists why there is something instead of nothing) but not in the origin of species."
      cites: [{source: S5, locator: "Ch. 1 Dilemma, pp. 1–2 (2004 reprint)"}]
      date: "1978"
      context: "On Human Nature, Ch. 1 Dilemma; near-span written profession (3 years after Sociobiology)."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
    - text: "no species, ours included, possesses a purpose beyond the imperatives created by its genetic history. Species may have vast potential for material and mental progress but they lack any immanent purpose or guidance from agents beyond their immediate environment"
      cites: [{source: S5, locator: "Ch. 1 Dilemma, pp. 1–2 (2004 reprint)"}]
      date: "1978"
      context: "On Human Nature, Ch. 1; first spiritual dilemma of the new naturalism."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
    - text: "I've been doing a kind of Pascalian waffling as a deist. I think being an atheist is to claim knowledge you cannot have. And to say you're agnostic is to arrogantly dismiss the whole thing by saying that it's unknowable. But a provisional deist is someone like myself who leaves it open. You see, evolutionary biology leaves very little room for a theistic God."
      cites: [{source: S2, locator: "'You call yourself a deist'"}]
      date: "1998-09"
      context: "Psychology Today interview; after the span (P31 continuity — no documented change)."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
    - text: "But I do feel confident that there is no intervention of a deity in the origin of life and humanity. … That is the distinction between theism and deism. … So I am not a theist, but I'll be a provisional deist."
      cites: [{source: S3, locator: "'I've heard you call yourself a deist'"}]
      date: "2006-03-21"
      context: "Salon interview; after the span (P31 continuity)."
      axes: [A_locus, B_cause]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
  changes_over_life:
    - {value: "Devout Southern Baptist in youth (baptised at 14); faith fell away with evolutionary biology in late adolescence / University of Alabama years — 'Baptist & Christian no more'", year: 1946, certainty: 0.5, cites: [{source: S3, locator: "'By the time you got to college'"}, {source: S7, locator: "'went under the water'"}, {source: S6, locator: "God and religion"}], how_known: "Interviews + Wikipedia quote; year from college entry, approximate. Pre-span; does not trigger P31 retrospective cap for 1978/1998/2006 evidence."}
  coder_notes: "RQ-Z7-1 answered by the Z7 audit: A 3 at 0.5 held (Franklin precedent). Deepen D1: P31 lifts A and DEISM to 0.7; OHN written_profession lifts B to 0.7 (P35 no longer binds). Chart-moving YES (both axes ≥0.7). Naturalist (1994) still unread first-hand; Consilience baptism/Baptist pages not borrowed (High Profiles covers baptism)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: "Southern Baptist", certainty: 0.7, cites: [{source: S3, locator: "'You grew up in a religious family?'"}, {source: S7, locator: "Southern Baptist Convention"}], how_known: "(interview)."}
  baptism_or_initiation: {value: "Baptised at age 14 in the Southern Baptist Convention ('went under the water')", certainty: 0.7, cites: [{source: S7, locator: "'went under the water'"}], how_known: "(interview) High Profiles."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1971–1975", certainty: 0.5, cites: [{source: S1, locator: "body"}], how_known: "The Insect Societies (1971) to Sociobiology (1975) (P29, P30); On Human Nature (1978) left in major_works only by the create-pass coder's call — not expanded this deepen."}
  age_at_first_lasting_contribution: {value: 42, certainty: 0.5, cites: [{source: S1, locator: "opening; body"}], how_known: "1971 − 1929 = 42 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: "c. 1946–1949 (conversion to evolution at university)", certainty: 0.5, cites: [{source: S3, locator: "'By the time you got to college'"}], how_known: "(interview)."}
  lio_views_relative_to_major_work: {value: "before major work", certainty: 0.5, cites: [{source: S3, locator: "'By the time you got to college'"}], how_known: "(interview). Near-span OHN 1978 restates the same non-intervention / provisional-deist content."}
  worldview_during_major_work: {value: "Provisional-deist content attested near-span in OHN 1978 (P31); self-label 'provisional deist' in 1998/2006 interviews with no documented change", certainty: 0.7, cites: [{source: S5, locator: "Ch. 1"}, {source: S2, locator: "'provisional deist'"}, {source: S3, locator: "'provisional deist'"}], how_known: "P31 continuity."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Field biology and taxonomy (S1).", certainty: 0.5, cites: [{source: S1, locator: "body"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Harvard University", role: "professor; curator in entomology", years: "1956–1997", kind: "university", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Britannica."}
collaborators:
  - {value: "W. L. Brown", relation: "collaborator", note: "character displacement", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Britannica."}
  - {value: "Bert Hölldobler", relation: "collaborator", note: "The Ants (1990)", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 163"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "OHN Ch.1 quotes verified via multi-secondary agreement (Miller p.180; Whitman 1978/2004:1–2; HUP sample index); full publisher PDF / IA borrow of OHN and Consilience not obtained this pass (P26 page-check open)."
    - "Create-pass P20 0.5 wording on interviews superseded by P31 continuity (no post-span change documented)."
  open_questions:
    - "Naturalist (1994) first-hand on religion still unread."
    - "Whether to add On Human Nature (1978, Pulitzer) to lasting_original_contributions and extend span to 1971–1978 (P30 addendum)."
    - "OHN Ch.8 Religion and Consilience Baptist pages first-hand (IA borrow / HUP full)."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Michael Ruse"
    citation: "Ruse, Michael. 'E.O. Wilson.' Encyclopaedia Britannica (rev. 2026). https://www.britannica.com/biography/Edward-O-Wilson"
    url: "https://www.britannica.com/biography/Edward-O-Wilson"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Signed article; body cited, Top Questions not used (P26)."
    used_for: [identity, basics, contribution, childhood, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "other"
    author: "E. O. Wilson, interviewed by Psychology Today"
    citation: "'E.O. Wilson Is on Top of the World.' Psychology Today (September 1998). https://www.psychologytoday.com/us/articles/199809/eo-wilson-is-on-top-of-the-world"
    url: "https://www.psychologytoday.com/us/articles/199809/eo-wilson-is-on-top-of-the-world"
    accessed: 2026-10-24
    source_quality: "newspaper interview"
    reliability_note: "Published interview transcript (recorded_interview, P8)."
    used_for: [worldview]
  - id: S3
    type: primary
    kind: "other"
    author: "E. O. Wilson, interviewed by Steve Paulson"
    citation: "Paulson, Steve. '\"Religious belief itself is an adaptation\".' Salon (21 March 2006). https://www.salon.com/2006/03/21/wilson_19/"
    url: "https://www.salon.com/2006/03/21/wilson_19/"
    accessed: 2026-10-24
    source_quality: "newspaper interview"
    reliability_note: "Published interview transcript (recorded_interview, P8)."
    used_for: [childhood, worldview, heritage, timing]
  - id: S4
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [review]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Edward O. Wilson"
    citation: "Wilson, Edward O. On Human Nature. Cambridge, MA: Harvard University Press, 1978; 25th anniversary ed. with new preface, 2004. Ch. 1 'Dilemma', pp. 1–2 (2004). Quotes checked against Miller, Finding Darwin's God (p. 180); Whitman academic PDF citing Wilson 1978/2004:1–2; HUP sample search-index agreement."
    url: "https://www.hup.harvard.edu/books/9780674016385"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Published own book (written_profession). Full HUP/IA PDF not retrieved this pass; short Ch.1 passages agree word-for-word across independent secondaries (P26 full-page check open). Near-span (1978 vs span end 1975)."
    used_for: [worldview]
  - id: S6
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "Wikipedia. 'E. O. Wilson.' https://en.wikipedia.org/wiki/E._O._Wilson"
    url: "https://en.wikipedia.org/wiki/E._O._Wilson"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "P50 dual-biography with Britannica; used for identity dates/places and God-and-religion paraphrase only, not as sole basis for scores."
    used_for: [identity, basics, worldview]
  - id: S7
    type: primary
    kind: "other"
    author: "E. O. Wilson, interviewed by High Profiles"
    citation: "'E. O. Wilson.' High Profiles. https://highprofiles.info/interview/e-o-wilson/"
    url: "https://highprofiles.info/interview/e-o-wilson/"
    accessed: 2026-10-24
    source_quality: "newspaper interview"
    reliability_note: "Published interview; baptism / Southern Baptist Convention own words. After the span (P31)."
    used_for: [childhood, heritage, worldview]
---

## Summary

E. O. Wilson (1929–2021), biologist [S1, S6]. Deepen D1: DEISM @0.7; A 3 @0.7, B 3 @0.7 (both corroborated); mid_basin false. Chart-moving: faded→dark. Span 1971–1975.

## Life and work

Alabama; Harvard 1956–97 [S1]. Died Burlington, Massachusetts, 2021-12-26 [S1, S6].

## Contribution and impact

Insect Societies; Sociobiology; biodiversity [S1]. On Human Nature (1978, Pulitzer) cited for worldview under P31; left outside lasting_original_contributions this pass.

## Childhood and education

Southern Baptist upbringing; baptised at 14; faith fell away with evolutionary biology in late adolescence [S3, S7, S6].

## Adult working worldview

Provisional deist (own label, S2/S3). OHN 1978: species by genetic chance and environmental necessity, not God; deity open at matter origin only; no guidance from agents beyond the immediate environment [S5]. Interviews: no deity intervention in origin of life/humanity; rejects atheist label; rejects pure agnostic label [S2, S3]. P31: no post-span change documented.

## Heritage (context only)

Southern Baptist by birth; baptised at 14 [S3, S7].

## Timing

1971–1975, age 42 [S1]. OHN 1978 near-span under P31.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Naturalist (1994) first-hand.
- Add OHN 1978 to lasting contributions / extend span?
- OHN Ch.8 Religion and Consilience first-hand.

## Research log

- 2026-10-19: Read Britannica (Ruse); Psychology Today and Salon interviews.
- 2026-10-24 (deepen D1, queue #155): Re-read Psych Today and Salon HTML; harvested OHN Ch.1 Dilemma quotes via Miller p.180 + Whitman 1978/2004:1–2 + HUP sample index (full OHN/Consilience PDF not borrowed); Wikipedia dual-bio (P50); High Profiles baptism; P47 on S1–S7; P31 lift DEISM/A/B to 0.7; mid_basin false; chart YES faded→dark. No fallacy_catalog. No figures/.
