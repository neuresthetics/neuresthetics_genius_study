---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch R; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-18
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to biology. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-18, by: "Grok Bot", summary: "Record created (stage 3 batch R, order P32: F 4, rank 105). Basics from Britannica (Britannica Editors, unsigned; body only, read live) and the 1953 Nature paper's publisher page (date). Worldview from his own signed op-ed in Time, 25 March 2016 ('a lifelong atheist'; 'my God-rejecting views'; 'secular Christianity'), read directly; written profession, after the working years (1953–1965), so capped at 0.5 (P20, Shannon and Hawking precedent). Scientist (P30). primary_system ATHE (0.5); A 4 (0.5); B 3 (0.5, alt 4; P35); mid_basin BELOW_THRESHOLD. Plotted (faded), like Crick. Draft, not reviewed."}
    - {date: 2026-10-18, by: "Grok Bot", summary: "Batch R audit fixes (gs_0454445_R run 1). Op-ed locators corrected: the 'I never go to Sunday services' statement is paragraph 7, and primary_system and A cite paragraphs 2, 4 and 7 (WA4). Ruling R1 recorded (v8's call on the auditor's advice): 'lifelong' does not lift the P1 cap, so ATHE and A 4 stay at 0.5. Span 1953–1965 with 1968 as the alternative recorded as v8's call. The 2003 Scientific American interview noted as an unread lead (still post-span if confirmed). No value changed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #104 / F4 rank 105). Needs: A 4 @0.5; B 3 @0.5 alt 4 (P35); primary ATHE @0.5; mid BELOW; plotted faded (like Crick). Dual bio: Britannica (S1) + Wikipedia EN (S7) (P50). P47 source_quality on S1–S8. In-span: Nobel Lecture 11 Dec 1962 (S8, nobelprize.org PDF): replication by 'thoroughly understood conventional chemical forces'; DNA structure reinforced belief that 'long-range forces, or for that matter any form of mysticism, would not be involved in protein synthesis' — B 3 @0.5 → 4 @0.7 written_profession (P35 no longer binds); alt 3 if 'mysticism' read as Jordan long-range forces only. Post-span A corroboration (P20 keeps 0.5): SciAm Apr 2003 (S5) 'never thought there was a spiritual basis for life' / molecular basis; Telegraph 20 Mar 2003 (S6) religious explanations 'myths from the past' / 'Every time you understand something, religion becomes less likely'; Time 2016 (S3); Wikipedia (S7) 'escapee from the Catholic religion' (Genes Girls Gamow p. 118) + Discover 'luckiest thing… father didn't believe in God' (primary Discover unread). No in-span God/atheist self-label; no P38 agnostic pairing. A support corroborated; B support corroborated (S8+S5). primary ATHE @0.5. mid BELOW (A 0.5). Chart-moving YES: hollow→filled (both corroborated); still faded (min(A,B)=0.5). Double Helix / MBG / Avoid Boring People IA borrow-restricted. No fallacy_catalog. No figures refresh. Draft, not reviewed."}

identity:
  id: watson-james
  display_name: "James Watson"
  roster:
    canonical_name: "James Watson"
    rank: 105
    F: 4
    models: [Claude, DeepSeek, Gemini, Grok]
    band: "core (3–4)"
    status: core
    field: biology
    field_bucket: "biology / life science"
  full_name: {value: "James Dewey Watson", certainty: 1.0, cites: [{source: S1, locator: "header ('Also known as')"}, {source: S7, locator: "lead / infobox"}], how_known: "Britannica and Wikipedia agree (P15)."}
  native_name: {value: UNKNOWN, how_known: "English; same as the display name."}
  aliases:
    - {name: "Watson-James", kind: "roster alias"}

basics:
  birth:
    date: {value: "1928-04-06", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "infobox"}], how_known: "Britannica and Wikipedia agree."}
    place: {value: "Chicago, Illinois, U.S.", modern_name: "Chicago, Illinois, United States", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "Early life and education"}], how_known: "Britannica and Wikipedia agree."}
  death:
    date: {value: "2025-11-06", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "infobox / lead"}], how_known: "Britannica and Wikipedia agree."}
    place: {value: "East Northport, New York, U.S.", modern_name: "East Northport, New York, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1953, certainty: 0.7, cites: [{source: S1, locator: "'Research' (spring 1953; Nature, April–May 1953)"}, {source: S2, locator: "citation metadata"}], how_known: "The double-helix model, published in Nature in April 1953 (S2) (P13, P17)."}
  era_bucket: {value: "1950 on", certainty: 0.7, cites: [{source: S2, locator: "citation metadata"}], how_known: "1953 (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United States (P3)."}
  region_of_work: {value: "North America", certainty: 0.5, cites: [{source: S1, locator: "'Research'"}, {source: S7, locator: "Career"}], how_known: "Harvard and Cold Spring Harbor; the double helix itself was found at Cambridge (Northern Europe); coder's call on the main region."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.5, cites: [{source: S1, locator: "'Research'"}], how_known: "Coder's reading."}
  occupations: {value: ["geneticist", "biophysicist", "professor of biology", "laboratory director"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Research'"}, {source: S7, locator: "lead"}], how_known: "Britannica and Wikipedia."}

contribution:
  primary_domain: biology
  fields: {value: ["genetics", "molecular biology"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Research'"}, {source: S7, locator: "lead"}], how_known: "Britannica and Wikipedia."}
  lasting_original_contributions:
    - {value: "Double-helix model of DNA, with specific base pairing (with Francis Crick)", year: 1953, kind: discovery, lasting: "'Their research answered one of the fundamental questions in genetics'; Nobel Prize 1962 (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Research'"}, {source: S2, locator: "citation metadata"}], how_known: "Britannica; year from the Nature paper (S2). A result about natural systems, so he is a scientist (P30)."}
    - {value: "Molecular Biology of the Gene (textbook)", year: 1965, kind: work, lasting: "'one of the most extensively used modern biology texts' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Research'"}], how_known: "Britannica. The latest listed lasting work (P30 addendum b); The Double Helix (1968), which Britannica describes only as an account that 'aroused some controversy', is not listed (coder's call; alternative end 1968)."}
  evidence_of_impact:
    - {value: "Nobel Prize for Physiology or Medicine, 1962, with Crick and Wilkins", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S8, locator: "lecture header"}], how_known: "Britannica; Nobel lecture PDF."}
  major_works:
    - {value: "The Double Helix", year: 1968, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "'Research'"}, {source: S7, locator: "The Double Helix"}], how_known: "Personal account; IA borrow-restricted this pass; not used for worldview scores."}
    - {value: "Genes, Girls, and Gamow", year: 2002, kind: "book", certainty: 0.5, cites: [{source: S7, locator: "cite ggg (p. 118)"}], how_known: "Wikipedia cites p. 118 'escapee from the Catholic religion'; full book unread (IA borrow-restricted)."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Mixed: Irish Catholic mother ('modestly religious' / nominally Catholic); Episcopalian father who lost his belief / had no religious beliefs", certainty: 0.7, cites: [{source: S3, locator: "paragraph 1"}, {source: S5, locator: "spiritual-basis paragraph"}, {source: S7, locator: "Early life"}], how_known: "Own accounts (Time 2016; SciAm 2003); Wikipedia agrees."}
  family_religious_practice: {value: "Neither parent attended church; he went to Sunday mass with his 'very religious grandmother' for a few years, then stopped (WWII / Franco)", certainty: 0.7, cites: [{source: S3, locator: "paragraphs 1–2"}, {source: S6, locator: "Watson quotations (Church fascists / Franco)"}], how_known: "Time 2016; Telegraph 2003 interview paraphrase of his wartime stop."}
  parents_and_household: []
  household_circumstances: {value: "South Side of Chicago in the 1930s", certainty: 0.5, cites: [{source: S3, locator: "paragraph 1"}], how_known: "His own account (S3)."}
  schooling:
    - {value: "University of Chicago, entered at 15, graduated 1947", stage: university, run_by: private, years: "1943–1947", ages: "15–19", certainty: 0.7, cites: [{source: S1, locator: "'Research'"}, {source: S7, locator: "Early life and education"}], how_known: "Britannica and Wikipedia; start year from his age at entry; run_by the coder's."}
    - {value: "Indiana University, PhD 1950 (virus research)", stage: university, run_by: "state or municipal", years: "–1950", certainty: 0.7, cites: [{source: S1, locator: "'Research'"}, {source: S7, locator: "Early life and education"}], how_known: "Britannica and Wikipedia; run_by the coder's."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Birdwatching with father after leaving mass; later ornithology interest leading into science", certainty: 0.5, cites: [{source: S6, locator: "Watson quotations"}], how_known: "Telegraph 2003 interview paraphrase."}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["English"], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "First Communion; stopped going to services by age 11 (rejecting need for God-like creator; Church as Franco-supporting fascists)", year: 1939, certainty: 0.5, cites: [{source: S3, locator: "paragraph 2"}, {source: S6, locator: "Watson quotations"}], how_known: "Retrospective accounts (S3, S6); year from 'by age 11'."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1953–1965", certainty: 0.7, cites: [{source: S1, locator: "'Research'"}, {source: S2, locator: "citation metadata"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Darwinian evolution and DNA-based genetics a 'very compelling alternative framework' to religion; 'most scientists see no need to postulate the existence of God-like entities' (2016); 'Every time you understand something, religion becomes less likely' (2003); explanation for life must be molecular, not spiritual (2003)", certainty: 0.5, cites: [{source: S3, locator: "paragraph 3"}, {source: S5, locator: "spiritual-basis paragraph"}, {source: S6, locator: "Watson quotations"}], how_known: "Post-span interviews and op-ed (P20)."}
  primary_system:
    value: ATHE
    basis: written_profession
    certainty: 0.5
    cites: [{source: S3, locator: "paragraphs 2, 4 and 7"}, {source: S5, locator: "spiritual-basis paragraph"}, {source: S6, locator: "Watson quotations"}, {source: S7, locator: "Personal life (atheist; escapee)"}]
    rationale: "Self-description: 'a reply that I am a lifelong atheist'; 'my God-rejecting views'; by 11 he was 'rejecting the need for an all-knowing God-like creator of our physical world' (S3). SciAm 2003: never a spiritual basis for life. Telegraph 2003: religious explanations 'myths from the past'. Wikipedia: atheist; 'escapee from the Catholic religion' (Genes Girls Gamow). Named alternative: SECHUM ('secular Christianity'; Humanist Manifesto signer per S7)."
    how_known: "Multiple post-span own-voice sources agree (Time, SciAm, Telegraph). After the working years (1953–1965), so 0.5 (P20). 'Lifelong' does not lift the cap (ruling R1). Independent source ids → corroborated (P48). No in-span atheist self-label found."
  secondary_system: {value: UNKNOWN, how_known: "SECHUM is a named alternative from Time; Humanist Manifesto 2003 signer (S7) — manifesto text not used to code a secondary system."}
  candidate_codes_considered:
    - {code: ATHE, reason: "'I am a lifelong atheist' (2016); outspoken atheist (Telegraph 2003 framing); Wikipedia 'was an atheist'."}
    - {code: SECHUM, reason: "'my secular Christianity'; faith in human nature and in 'scientific and humanistic knowledge' (2016); Humanist Manifesto signer (S7)."}
    - {code: CHRIST, reason: "Rejected: 'secular Christianity' is offered with 'my God-rejecting views'; he never goes to services."}
    - {code: AGNOS, reason: "Rejected for primary: no agnostic self-label found (Web of Stories attributes agnostic to father, not to him). No P38 pairing."}
  lio_axes:
    A_locus:
      value: 4
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S3, locator: "paragraphs 2, 4 and 7"}, {source: S5, locator: "spiritual-basis paragraph"}, {source: S6, locator: "Watson quotations"}, {source: S7, locator: "Personal life / Early life (escapee; Discover quote)"}]
      rationale: "No God: 'a lifelong atheist'; 'my God-rejecting views'; faith 'not ... in an all-powerful, life-instructions-providing God' (S3). SciAm: 'I never thought there was a spiritual basis for life'. Telegraph: religious explanations 'myths from the past'. No agnostic self-label, so P38 does not bind; the cap is P20's (all A own-voice read is post-span). No in-span God/atheist statement found in Nobel lecture or reachable open sources."
      how_known: "Signed op-ed + recorded interviews + Wikipedia secondary for Genes Girls / Discover quotes. Independent source ids → corroborated (P48). Certainty stays 0.5 under P20."
    B_cause:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S8, locator: "prologue (chemical forces / mysticism paragraph)"}, {source: S5, locator: "spiritual-basis / molecular-basis paragraph"}]
      rationale: "Scored on his account of nature (P6, P16). Nobel Lecture 11 Dec 1962 (inside span): gene-replication scheme 'involved thoroughly understood conventional chemical forces'; DNA structure 'reinforced our belief that Pauling's arguments were sound and that long-range forces, or for that matter any form of mysticism, would not be involved in protein synthesis'. That denies mystic / undiscovered-force exemptions for living systems in favour of ordinary chemistry — B 4; P35's working-science-only cap no longer binds. SciAm 2003 agrees: explanation for life 'had to be about the molecular basis for life'; 'never thought there was a spiritual basis for life'. Named alternative 3: if 'mysticism' is read only as Jordan's quantum long-range forces (the immediate context) rather than a general no-exception claim about nature's order."
      how_known: "Nobelprize.org PDF of the published lecture (authoritative edition) → 0.7 written_profession. SciAm interview (P8 recorded_interview) corroborates the anti-mystical / molecular account of life (P48). Independent source ids → corroborated."
      alternatives:
        - {value: 3, note: "If Nobel 'mysticism' is read narrowly as only Pascual Jordan's long-range quantum resonance forces, not a general exceptionless-order claim.", cites: [{source: S8, locator: "prologue (Jordan / Pauling / mysticism)"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read; the remark that 'the fear of going to hell has effectively disappeared' for many Americans (S3) is about others."}
    D_authority: {value: UNKNOWN, how_known: "Leads only (not scored this pass): Telegraph 'myths from the past' / 'religion becomes less likely'; Time religious edicts as root of violence yet sermons must embrace present moral challenges — mixed and post-span."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 4 but at 0.5: the A ≥ 3 branch reads A only (P10) and needs 0.7, as for Crick, Shannon and Skinner. B is now 4 @0.7 but does not decide this branch."}
  statements:
    - text: "By age 11, just a year after my First Communion, I, too, stopped going to services, rejecting the need for an all-knowing God-like creator of our physical world."
      cites: [{source: S3, locator: "paragraph 2"}]
      date: "2016-03-25"
      context: "Op-ed 'Nobel Scientist: I Place My Faith in Human Gods', Time (Ideas), 25 March 2016; retrospective account of c. 1939."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-18
      note: "Read on time.com, the publisher's own text of the op-ed (marked primary transcription as the nearest value); the page also carries unrelated sponsored newsletter text, ignored."
    - text: "The obvious sincerity of the questioner demanded more than a reply that I am a lifelong atheist."
      cites: [{source: S3, locator: "paragraph 4"}]
      date: "2016-03-25"
      context: "Same op-ed; he goes on: 'faith was essential to my life, but it was not faith in an all-powerful, life-instructions-providing God.'"
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-18
      note: ""
    - text: "I never go to Sunday services; I don’t need sermons to maintain my secular Christianity. Nowadays my God-rejecting views are much more broadly accepted by educated men and women than when World War II ended and my father would have seriously jeopardized his job in business if he ever publicly expressed the atheistic view he passed on to me."
      cites: [{source: S3, locator: "paragraph 7"}]
      date: "2016-03-25"
      context: "Same op-ed."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-18
      note: ""
    - text: "I liked explanations. And so if you wanted an explanation for life, it had to be about the molecular basis for life. I never thought there was a spiritual basis for life; I was very lucky to be brought up by a father who had no religious beliefs."
      cites: [{source: S5, locator: "spiritual-basis paragraph"}]
      date: "2003-04"
      context: "Scientific American interview with editor John Rennie, Cold Spring Harbor Laboratory, published April 2003 (Vol. 288 No. 4) as 'Celebrating the Genetic Jubilee: A Conversation with James D. Watson'; abridged/edited conversation."
      axes: [A_locus, B_cause]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Read on scientificamerican.com publisher page. Post-span (P8, P20). Supports A (no spiritual basis) and corroborates B (molecular / chemical account of life)."
    - text: "Every time you understand something, religion becomes less likely."
      cites: [{source: S6, locator: "Watson quotations"}]
      date: "2003-03-20"
      context: "Interview with The Telegraph (Matt Ridley), published 20 March 2003 as 'Do our genes reveal the hand of God?'; paired with his calling religious explanations 'myths from the past'."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Read via Wayback Machine capture of telegraph.co.uk. Post-span (P8, P20)."
    - text: "Furthermore, this replication scheme involved thoroughly understood conventional chemical forces. Previously, some theoretical physicists, among them Pascual Jordan, had proposed that many biological phenomena, particularly gene replication, might be based on still undiscovered long-range forces arising from quantum mechanical resonance interactions. Pauling thoroughly disliked this conjecture and firmly insisted that known short-range forces between complementary surfaces would be the basis of biological replication. The establishment of the DNA structure reinforced our belief that Pauling's arguments were sound and that long-range forces, or for that matter any form of mysticism, would not be involved in protein synthesis."
      cites: [{source: S8, locator: "prologue (chemical forces / mysticism paragraph)"}]
      date: "1962-12-11"
      context: "Nobel Lecture, 'The involvement of RNA in the synthesis of proteins', Stockholm, 11 December 1962; published in Nobel Lectures, Physiology or Medicine 1942–1962."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Read from nobelprize.org official PDF (watson-lecture.pdf). Inside working years. 'Our belief' = Watson and Crick."
  changes_over_life:
    - {value: "Childhood Catholic practice → stop by ~11 (creator rejected; Church as Franco fascists) → adult molecular anti-mysticism (Nobel 1962) → late outspoken atheist / 'secular Christianity' (2003–2016)", certainty: 0.5, cites: [{source: S3, locator: "paragraphs 2–7"}, {source: S6, locator: "Watson quotations"}, {source: S8, locator: "prologue"}], how_known: "Consistent anti-theism in post-span sources; in-span evidence is B (anti-mysticism), not an atheist self-label."}
  coder_notes: "Deepen D1 2026-10-24: Nobel 1962 PDF lifts B off P35; SciAm/Telegraph/Wikipedia corroborate A at P20 0.5 (no P38). Double Helix, MBG, Avoid Boring People, Genes Girls Gamow full texts IA borrow-restricted — residual leads for earlier A. No fallacy_catalog."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "American; mother Irish Catholic", certainty: 0.5, cites: [{source: S3, locator: "paragraph 1"}], how_known: "His own account."}
  religious_heritage_by_birth: {value: "Roman Catholic (mother) and Episcopalian (father)", certainty: 0.7, cites: [{source: S3, locator: "paragraph 1"}, {source: S7, locator: "Early life"}], how_known: "Own account and Wikipedia."}
  baptism_or_initiation: {value: "First Communion (c. age 10)", certainty: 0.5, cites: [{source: S3, locator: "paragraph 2"}], how_known: "His own account; age from 'a year' before 11."}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1953–1965", certainty: 0.7, cites: [{source: S1, locator: "'Research'"}, {source: S2, locator: "citation metadata"}], how_known: "Double helix (1953) to Molecular Biology of the Gene (1965), first to last listed lasting contribution (P29, P30); alternative end 1968 (The Double Helix), not listed: Britannica calls it only 'an informal personal account' that 'aroused some controversy', so P30 addendum b does not force it onto the list. Span end 1965 with 1968 as the alternative is v8's call (2026-10-18; OPEN_DECISIONS P20, with R1); either end leaves the 2016 op-ed after the span; Nobel 1962 falls inside either span."}
  age_at_first_lasting_contribution: {value: 25, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "citation metadata"}], how_known: "1953 − 1928 = 25 (P30; birthday 6 April, paper 25 April)."}
  first_evidence_of_lio_type_views: {value: "1962: Nobel Lecture rejects 'any form of mysticism' for protein synthesis in favour of conventional chemical forces (B); explicit atheist / no-God labels first read in 2003–2016 (A)", year: 1962, certainty: 0.7, cites: [{source: S8, locator: "prologue"}, {source: S5, locator: "spiritual-basis paragraph"}, {source: S3, locator: "paragraph 4"}], how_known: "Nobel PDF for B; later interviews/op-ed for A self-labels (P30 #7)."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "Nobel Lecture 1962 falls inside 1953–1965 (B). Explicit A self-labels are after (2003–2016); by his retrospective account the rejection of a creator begins c. 1939.", certainty: 0.5, cites: [{source: S8, locator: "prologue"}, {source: S3, locator: "paragraph 2"}], how_known: "Dates of what was read; mixed B-during / A-after → 0.5."}
  worldview_during_major_work: {value: "Anti-mystical molecular biologist (Nobel 1962: conventional chemical forces; no mysticism in protein synthesis); explicit atheist self-label not yet read from inside the span", certainty: 0.5, cites: [{source: S8, locator: "prologue"}], how_known: "Nobel lecture; A self-labels are post-span."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "Structural model-building of DNA (S1).", certainty: 0.5, cites: [{source: S1, locator: "'Research'"}], how_known: "Coder's reading."}
  form_acquired: {value: "through the profession", certainty: 0.5, cites: [{source: S1, locator: "'Research' (X-ray diffraction at the Cavendish)"}], how_known: "Coder's reading."}
  circle_present: {value: "no", rationale: "No God (post-span A); in-span anti-mysticism for life processes (B).", certainty: 0.5, cites: [{source: S3, locator: "paragraph 4"}, {source: S8, locator: "prologue"}], how_known: "Coder's reading."}
  reading: "Atheist molecular biologist who calls himself a secular Christian; in-span, rejects mysticism for ordinary chemical forces in gene/protein synthesis."
  notes: ""

institutions:
  - {value: "University of Copenhagen", role: researcher, years: UNKNOWN, kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Research'"}], how_known: "Britannica (before 1951; years not given)."}
  - {value: "Cavendish Laboratory, University of Cambridge", role: researcher, years: "1951–1953", kind: "research institute", certainty: 0.7, cites: [{source: S1, locator: "'Research'"}], how_known: "Britannica."}
  - {value: "Harvard University", role: "teacher; professor of biology 1961–76", years: "1955–1976", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Research'"}], how_known: "Britannica."}
  - {value: "Laboratory of Quantitative Biology, Cold Spring Harbor", role: director, years: "1968–2007", kind: "research institute", certainty: 0.7, cites: [{source: S1, locator: "'Research'; 'Controversy'"}], how_known: "Britannica (assumed leadership 1968; resigned 2007); end year from the resignation in 'Controversy'."}
  - {value: "National Institutes of Health (Human Genome Project)", role: "helped direct the Human Genome Project", years: "1988–1992", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "'Research'"}], how_known: "Britannica."}
collaborators:
  - {value: "Francis Crick", relation: collaborator, note: "double helix; Nobel 1962", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Research'"}], how_known: "Britannica."}
  - {value: "Maurice Wilkins", relation: collaborator, note: "shared the 1962 Nobel Prize", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Britannica names him as co-laureate; 'collaborator' is the coder's reading."}
  - {value: "Oswald Avery", relation: "influenced by", note: "his experiments showing DNA affects heredity", certainty: 0.7, cites: [{source: S1, locator: "'Research'"}], how_known: "Britannica."}
  - {value: "John Tooze", relation: collaborator, note: "co-author of The DNA Story (1981)", certainty: 0.7, cites: [{source: S1, locator: "'Research'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 105"}], how_known: "Study roster."}
  controversies:
    - {value: "2007 statement on race and intelligence, denounced as racist; resigned from Cold Spring Harbor; honorary titles removed in 2019", certainty: 0.7, cites: [{source: S1, locator: "'Controversy'"}, {source: S7, locator: "Controversies"}], how_known: "Britannica and Wikipedia."}
  data_quality_flags:
    - "Britannica article is unsigned (Britannica Editors); read live."
    - "A self-labels remain post-span (P20 @0.5); in-span A not found."
    - "Double Helix / MBG / Genes Girls Gamow / Avoid Boring People full texts IA borrow-restricted this pass."
  open_questions:
    - "Find an in-span (1953–1965) God/atheist self-label in Double Helix drafts, letters, or MBG to lift A past P20 0.5."
    - "Primary check Genes Girls Gamow p. 118 'escapee' and Discover July 2003 'luckiest thing' quotes (Wikipedia secondary only this pass)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"James Watson.\" Encyclopaedia Britannica (revised 2 September 2026, by Amy Tikkanen). https://www.britannica.com/biography/James-Dewey-Watson. Read live 2026-10-18; rechecked 2026-10-24."
    url: "https://www.britannica.com/biography/James-Dewey-Watson"
    accessed: 2026-10-24
    reliability_note: "Unsigned article. Body and header only; the AI-generated questions and At a Glance are not cited."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, timing, lane_b, institutions, collaborators, review]
  - id: S2
    type: primary
    kind: "journal article"
    author: "J. D. Watson and F. H. C. Crick"
    citation: "Watson, J. D., and F. H. C. Crick. \"Molecular Structure of Nucleic Acids: A Structure for Deoxyribose Nucleic Acid.\" Nature 171 (April 1953): 737. https://www.nature.com/articles/171737a0"
    url: "https://www.nature.com/articles/171737a0"
    accessed: 2026-10-18
    reliability_note: "Publisher's page; used for the date only (citation metadata), as in the Crick record."
    source_quality: "primary / own words"
    used_for: [basics, contribution, timing]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "James Watson"
    citation: "Watson, James. \"Nobel Scientist: I Place My Faith in Human Gods.\" Time (Ideas), 25 March 2016. https://time.com/4259269/nobel-scientist-religion/"
    url: "https://time.com/4259269/nobel-scientist-religion/"
    accessed: 2026-10-18
    reliability_note: "His own signed op-ed, read directly. Paragraph numbers count the op-ed's text only; the page also carries unrelated sponsored newsletter material, ignored. Post-span (P20)."
    source_quality: "primary / own words"
    used_for: [childhood, worldview, heritage, timing, lane_b]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-18
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S5
    type: primary
    kind: other
    author: "James D. Watson (interviewed by John Rennie)"
    citation: "Rennie, John. \"Celebrating the Genetic Jubilee: A Conversation with James D. Watson.\" Scientific American 288, no. 4 (April 2003): 66. https://www.scientificamerican.com/article/a-conversation-with-james/"
    url: "https://www.scientificamerican.com/article/a-conversation-with-james/"
    accessed: 2026-10-24
    reliability_note: "Publisher's page; abridged/edited conversation. Post-span (P8, P20). Also reprinted in Free Inquiry Frontlines (June 2003)."
    source_quality: "newspaper interview"
    used_for: [childhood, worldview]
  - id: S6
    type: primary
    kind: other
    author: "James Watson (interviewed for The Telegraph)"
    citation: "Ridley, Matt. \"Do our genes reveal the hand of God?\" The Telegraph, 20 March 2003. https://www.telegraph.co.uk/connected/main.jhtml?xml=/connected/2003/03/19/ecfgod19.xml (read via Wayback Machine capture 2008-06-04)."
    url: "https://web.archive.org/web/20080604203926/http://www.telegraph.co.uk/connected/main.jhtml?xml=/connected/2003/03/19/ecfgod19.xml"
    accessed: 2026-10-24
    reliability_note: "Wayback capture of telegraph.co.uk; Watson quotes in own voice amid reporter framing. Post-span (P8, P20)."
    source_quality: "newspaper interview"
    used_for: [childhood, worldview]
  - id: S7
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. \"James Watson.\" Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/wiki/James_Watson. Read live 2026-10-24."
    url: "https://en.wikipedia.org/wiki/James_Watson"
    accessed: 2026-10-24
    reliability_note: "Dual bio with Britannica (P50). Used for biography cross-check and for secondary quotes of Genes Girls Gamow p. 118 ('escapee') and Discover July 2003 ('luckiest thing… father didn't believe in God') — those book/magazine primaries unread this pass."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, review]
  - id: S8
    type: primary
    kind: "published work by the subject"
    author: "James D. Watson"
    citation: "Watson, James D. \"The involvement of RNA in the synthesis of proteins.\" Nobel Lecture, 11 December 1962. In Nobel Lectures, Physiology or Medicine 1942–1962. https://www.nobelprize.org/uploads/2018/06/watson-lecture.pdf"
    url: "https://www.nobelprize.org/uploads/2018/06/watson-lecture.pdf"
    accessed: 2026-10-24
    reliability_note: "Official Nobel Prize Foundation PDF of the published lecture; pdftotext extraction verified this pass. Inside working years."
    source_quality: "primary / own words"
    used_for: [contribution, worldview, timing]
---

# James Watson

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

James Watson (1928–2025), American geneticist and biophysicist [S1; S7]. Deepen D1: primary_system ATHE (0.5, corroborated); A 4 at 0.5 corroborated (P20; no P38); B 4 at 0.7 corroborated (Nobel 1962 anti-mysticism / chemical forces; alt 3); mid_basin BELOW_THRESHOLD. Plotted faded; chart-moving YES (hollow→filled; still faded because A stays 0.5).

## Life and work

Chicago, Indiana, Copenhagen, Cambridge, Harvard, Cold Spring Harbor [S1; S7].

## Contribution and impact

The double helix (1953) and Molecular Biology of the Gene (1965) [S1; S2]. Nobel Lecture 1962 on RNA in protein synthesis [S8].

## Childhood and education

Catholic mother, Episcopalian father; stopped going to mass by 11 [S3; S5; S6].

## Adult working worldview

In-span: rejects 'any form of mysticism' for protein synthesis in favour of conventional chemical forces (1962) [S8]. Post-span: 'lifelong atheist' (2016) [S3]; never a spiritual basis for life (2003) [S5]; religious explanations 'myths from the past' (2003) [S6].

## Heritage (context only)

Irish Catholic and Episcopalian [S3; S7].

## Timing

1953–1965, from age 25 [S1; S2]. Nobel Lecture 1962 inside span [S8].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No God (post-span A) [S3; S5; S6]; in-span anti-mysticism for life chemistry [S8].

## Open questions

- In-span God/atheist self-label (Double Helix, letters, MBG).
- Primary check Genes Girls Gamow p. 118 and Discover July 2003.

## Research log

- 2026-10-18: Read Britannica (live) and the Time op-ed directly; Nature citation as in the Crick record.
- 2026-10-24: Deepen D1 — Nobel lecture PDF (S8); SciAm 2003 (S5); Telegraph 2003 via Wayback (S6); Wikipedia dual bio (S7). IA borrow wall on Double Helix / MBG / Genes Girls / Avoid Boring People.
