---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 7
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, fourth batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (fourth batch, RUNBOOK §1 order). Basics from Britannica (Robert W. Smith). Worldview from his own lectures in The Nature of Science and Other Lectures (Huntington Library, 1954), read in a user-uploaded Internet Archive scan (page images), so capped at 0.7 under CODING_GUIDE §7. Childhood religion from Christianson's biography (publisher's preview). Baptist upbringing; as an adult he set science (public knowledge from observation and experiment) beside a private world of values whose premises 'are in the nature of religious convictions'. primary_system BELOW_THRESHOLD (AGNOS candidate, stub). B 4 (0.7), D 2 (0.7); A, C, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 4 (two blind runs at b21655b). #12/#1 (run 1 note): the Christianson 'p. 183' locator for his adult religion could not be verified (outside the publisher's preview, pp. 13–29) and is withdrawn from the primary_system note and the open question. Decisions P12/P13 recheck: first_lasting_contribution_year 1923 is already the start year of the earliest listed item; the undated '1920s' classification does not set it (noted). No value changed. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02). Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs; BELOW_THRESHOLD vs UNKNOWN per P19; kind lists (P21: research institute, school stage and run_by, scholarly edition). Full before → after list: reports/stage3_rulings_changes.csv. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "P30 rule 5 age sweep: ages recomputed as event year − birth year, with no month adjustment (scripts/recompute_ages.py; every change is in reports/p30_age_changes.csv). No other value changed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Span alignment (P29, P30 and its addendum): timing.major_work_period checked, 1923–1936 unchanged; worldview.working_years 1914–1953 → 1923–1936, equal to the span (P30 addendum f); lasting item added: The Realm of the Nebulae (1936); 2 headline values rest on evidence outside the span and are left unchanged for a ruling (open questions). Listed in reports/p30_span_alignment.csv. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "P31 (continuity rule, v8's pick, 2026-10-02): the 2 values the span check flagged as resting on evidence outside the span are resolved, since changes_over_life documents no change of view between the span and that evidence; no value or certainty changed; the Open questions pointer line was removed. Listed in reports/p30_span_alignment.csv. Not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #156, F 3, rank 164). Needs: A BELOW_THRESHOLD; primary BELOW (AGNOS candidate). Recovered Christianson p.183 adult-religion passage via Wikipedia EN verbatim quotation (S5 ref 47) and TodayInSci (S6: Grace Burke Hubble Huntington MS locator for 'We do not know why we are born…'). Emerson (1939) belief/Creator reply and Whitehead-Creator cocktail talk are Grace-reported speech — cannot score A or primary alone (CODING_GUIDE §1 / P18). Reply neither places nor denies a personal God (P19/P20: AGNOS with no locus → A BELOW). S2 Nature of Science two-domains already on file; still silent on locus. P50 Wikipedia dual bio (S5). P47 source_quality on S1–S6. P48 support on B (corroborated S2+S1) and D (single S2). primary_system stays BELOW_THRESHOLD (AGNOS lead strengthened, not opened); A stays BELOW; B 4 @0.7; D 2 @0.7; mid BELOW; not plotted. Chart-moving NO. No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: hubble-edwin
  display_name: "Edwin Hubble"
  roster:
    canonical_name: "Edwin Hubble"
    rank: 164
    F: 3
    models: [Claude, DeepSeek, Gemini]
    band: "core (3–4)"
    status: core
    field: astronomy
    field_bucket: astronomy
  full_name: {value: "Edwin Powell Hubble", certainty: 1.0, cites: [{source: S1, locator: "'Also known as: Edwin Powell Hubble'"}, {source: S3, locator: "p. 13 ('Edwin Powell, who arrived by kerosene lamp')"}, {source: S5, locator: "lead / infobox"}], how_known: "Britannica, Christianson preview, and Wikipedia agree (P50)."}
  native_name: {value: "Edwin Hubble (English)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "English name."}
  aliases:
    - {name: "Hubble-Edwin", kind: "roster alias"}

basics:
  birth:
    date: {value: "1889-11-20", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "infobox"}], how_known: "Britannica and Wikipedia agree (P50)."}
    place: {value: "Marshfield, Missouri", modern_name: "Marshfield, Missouri, USA", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "infobox / Early life"}], how_known: "Britannica and Wikipedia agree (P50)."}
  death:
    date: {value: "1953-09-28", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "infobox"}], how_known: "Britannica and Wikipedia agree (P50)."}
    place: {value: "San Marino, California", modern_name: "San Marino, California, USA", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "infobox / Personal life"}], how_known: "Britannica and Wikipedia agree (P50)."}
  first_lasting_contribution_year: {value: 1923, certainty: 0.7, cites: [{source: S1, locator: "'In 1923 Hubble found Cepheid variable stars in the Andromeda Nebula'"}], how_known: "Cepheids in the Andromeda Nebula, which settled that spirals are galaxies outside the Milky Way: the earliest listed contribution, dated 1923–1924, taken at its start year (decisions P12, P13). The galaxy classification is dated only '1920s' in S1, so it does not set the year (P12); a source dating it before 1923 would move the year."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "1923 paragraph"}], how_known: "From first_lasting_contribution_year (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "USA is North America in data/reference/regions.csv (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "Mount Wilson paragraphs"}], how_known: "Mount Wilson Observatory, California, from 1919."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "As the source records it."}
  languages_of_work: {value: [English], certainty: 1.0, cites: [{source: S2, locator: "title page"}, {source: S1, locator: "1936 paragraph"}], how_known: "His books and lectures are in English."}
  occupations: {value: ["astronomer", "observatory staff astronomer"], certainty: 0.7, cites: [{source: S1, locator: "opening; Mount Wilson paragraphs"}], how_known: "Britannica."}

contribution:
  fields: {value: ["extragalactic astronomy", "observational cosmology"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Distance to the Andromeda Nebula from its Cepheid variables, showing that spiral nebulae are galaxies beyond the Milky Way", year: "1923–1924", kind: discovery, lasting: "convinced most astronomers that the universe contains many galaxies", certainty: 0.7, cites: [{source: S1, locator: "'In 1923 Hubble found Cepheid variable stars' paragraph; summary box ('In 1923-24')"}], how_known: "Britannica article and its summary."}
    - {value: "Linear redshift–distance relation for galaxies (Hubble's law), with Milton Humason", year: "1929–1931", kind: "law or principle", lasting: "read as the expansion of the universe; the Hubble constant", certainty: 0.7, cites: [{source: S1, locator: "'In 1929 Hubble published his first paper on the relationship between redshift and distance'; summary box"}], how_known: "Britannica. Hubble himself resisted reading the redshifts definitely as velocities (S1)."}
    - {value: "Morphological classification of galaxies (spirals, ellipticals, irregulars)", year: "1920s", kind: method, lasting: "standard classification scheme", certainty: 0.7, cites: [{source: S1, locator: "summary box ('He also classified galaxies by their morphology')"}], how_known: "Britannica summary; year not given there."}
    - {value: "The Realm of the Nebulae: his account of the methods of extragalactic astronomy", year: 1936, kind: "work", lasting: "methods and techniques extragalactic astronomers followed for decades", certainty: 0.7, cites: [{source: S1, locator: "paragraph on 1936 ('his important book The Realm of the Nebulae'; 'By then he had certainly done much to lay down the methods and techniques that extragalactic astronomers would follow')"}], how_known: "One encyclopedia article, so 0.7. Added 2026-10-02 under the P30 addendum (the latest lasting work must be listed)."}
  evidence_of_impact:
    - {value: "Britannica calls him 'the leading observational cosmologist of the 20th century' and 'the central figure in the establishment of extragalactic astronomy'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening; paragraph after the 1936 book"}], how_known: "One signed encyclopedia article."}
  major_works:
    - {value: "The Realm of the Nebulae", year: 1936, kind: book, certainty: 0.7, cites: [{source: S1, locator: "'the year he published his important book The Realm of the Nebulae'"}], how_known: "Britannica."}
    - {value: "The Nature of Science and Other Lectures (posthumous)", year: 1954, kind: book, certainty: 1.0, cites: [{source: S2, locator: "title page and contents"}], how_known: "The book itself."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Established extragalactic astronomy and the redshift–distance law.", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Baptist (both parents; the family joined First Baptist Church, Wheaton, in 1901)", certainty: 0.7, cites: [{source: S3, locator: "pp. 14, 15, 23"}], how_known: "Christianson's biography (one scholarly source)."}
  family_religious_practice: {value: "Father 'an inveterate student of the Bible who lived his religion'; mother a 'fine Bible student' who taught the women's Sunday school class; Edwin sang in the First Baptist choir; a Sunday-morning 'trek to church' was routine, and a brother was forbidden to play golf on Sundays 'for religious reasons'", certainty: 0.7, cites: [{source: S3, locator: "pp. 14, 15, 26, 29"}], how_known: "Christianson."}
  parents_and_household:
    - {value: "Father, John Powell Hubble, a businessman in the insurance industry, often away on business", name: "John Powell Hubble", role: father, certainty: 1.0, cites: [{source: S1, locator: "paragraph 2"}, {source: S3, locator: "p. 14"}], how_known: "Two sources."}
    - {value: "Mother, Virginia Lee James, a homemaker who ran the household during John's absences", name: "Virginia Lee Hubble (née James)", role: mother, certainty: 1.0, cites: [{source: S1, locator: "paragraph 2"}, {source: S3, locator: "p. 15"}], how_known: "Two sources."}
  household_circumstances: {value: "One of eight children", certainty: 0.7, cites: [{source: S1, locator: "paragraph 2"}], how_known: "Britannica."}
  schooling:
    - {value: "University of Chicago (graduated 1910); a year as Robert Millikan's student laboratory assistant", stage: university, years: "1906–1910", certainty: 0.7, cites: [{source: S1, locator: "paragraph 3"}], how_known: "Britannica."}
    - {value: "University of Oxford as a Rhodes Scholar; B.A. in jurisprudence, taken at his father's insistence", stage: university, years: "1910–1913", certainty: 0.7, cites: [{source: S1, locator: "paragraph 3"}], how_known: "Britannica."}
    - {value: "University of Chicago graduate study in astronomy at Yerkes Observatory under Edwin Frost; dissertation 'Photographic Investigations of Faint Nebulae' (1917)", stage: university, years: "1914–1917", certainty: 0.7, cites: [{source: S1, locator: "paragraphs 4–5"}], how_known: "Britannica."}
  early_mathematics: {value: TODO, note: "Not stated in the sources read."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [English], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "American family."}
  notable_events:
    - {value: "Father's death, after which 'the way was open for him to pursue a scientific career'", year: "1913", certainty: 0.7, cites: [{source: S1, locator: "paragraph 3"}], how_known: "Britannica."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1923–1936", certainty: 0.7, cites: [{source: S1, locator: "1923 paragraph to 1936 book"}], how_known: "Equal to timing.major_work_period (P30 addendum f; span check 2026-10-02). Was 1914–1953: Graduate study at Yerkes to death."}
  nominal_affiliations:
    - {value: "Raised Baptist (First Baptist Church, Wheaton, from 1901; sang in its choir)", years: "1901–", role: "member by upbringing", certainty: 0.7, cites: [{source: S3, locator: "pp. 23, 26"}], how_known: "Christianson; adult membership or practice not checked in the pages read."}
  self_described_science_religion_relation:
    value: "Two aspects of one universe: 'the realm of science, the public domain of positive knowledge' and 'the world of values, the private domain of personal wisdom'; knowledge comes from observation and experiment, wisdom from personal experience. The premises of values 'are in the nature of religious convictions', derived 'from authority, or from revelation, or from the inner conscience', and tested by personal experience, not by experiment."
    certainty: 0.7
    cites: [{source: S2, locator: "pp. 38–39 ('Experiment and Experience', 1938)"}]
    how_known: "His own Caltech commencement address, printed in S2 and checked on the page images. Capped at 0.7 under CODING_GUIDE §7: the access copy is a user upload to the Internet Archive and its provenance cannot be confirmed from the copy itself."
  primary_system:
    value: BELOW_THRESHOLD
    cites: [{source: S2, locator: "pp. 38–39"}, {source: S5, locator: "Personal life / ref 47 (Christianson p. 183)"}, {source: S6, locator: "Creator / born-into-the-world quotations"}]
    how_known: "S2 places religion with private values and never names God. Christianson p. 183 (via S5/S6) gives Grace-reported adult remarks that neither affirm nor deny a Creator — reported speech cannot open a code alone (§1 / P18). Baptist upbringing (S3) is childhood and never a code."
    note: "Candidate: AGNOS (explicit suspension). Deepen D1 recovered the withdrawn p. 183 passage: early Whitehead 'Creator' talk, then less certain ('We do not know why we are born… physical aspects'); to depressed friend John Emerson about belief/Creator: 'I can't understand it, so I just trust myself to it, and forget about it' (Grace journals / Christianson). Fits AGNOS suspension tone but is reported speech and does not state suspension in his own published words — keep BELOW (P19). AGNOS system file filled (no longer create-pass stub)."
  secondary_system: {value: UNKNOWN, how_known: "No second system evidenced in the sources read."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Leading candidate, not coded: S2 two-domains + Grace-reported Emerson reply (S5/S6) read as suspension, but no own-voice 'I am agnostic' / explicit suspension on God's existence; reported speech cannot open the code alone.", cites: [{source: S2, locator: "pp. 38–39"}, {source: S5, locator: "ref 47"}, {source: S6, locator: "Creator reply"}]}
    - {code: CHRIST, reason: "Considered: Baptist upbringing and choir (S3). Rejected for adult working years: upbringing never a code; no adult Christian profession in sources read; Wikipedia notes later uncertainty (S5).", cites: [{source: S3, locator: "pp. 14, 23, 26"}, {source: S5, locator: "Personal life"}]}
    - {code: ATHE, reason: "Rejected: no positive naturalism or denial of God in own words; Emerson reply trusts 'the whole thing' without denying a Creator.", cites: [{source: S5, locator: "ref 47"}, {source: S6, locator: "Creator reply"}]}
  lio_axes:
    A_locus:
      value: BELOW_THRESHOLD
      how_known: "S2 silent on God. Christianson p. 183 / Emerson reply (S5, S6) is Grace-reported speech and neither places nor denies a personal God (P19/P20)."
      note: "Deepen D1: recovered adult-religion passage does not open A. Early Whitehead Creator speculation then 'less certain'; Emerson asked about belief in a Creator — reply 'trust myself to it, and forget about it' suspends without a locus. P20: an agnostic with no stated locus view gets A BELOW_THRESHOLD. Reported speech cannot score A alone (§1)."
    B_cause:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S2, locator: "p. 10 ('The Nature of Science', 1948)"}, {source: S1, locator: "1923 and 1929 paragraphs"}]
      how_known: "His own lecture, capped at 0.7 under §7 (unofficial scan). Two source ids → corroborated (P48)."
      rationale: "Scored on his account of nature (P6). Laws are general statements of invariable association, and 'invariable' is the working assumption that an association seen in many cases will hold in the next one (p. 10); his own work extended measured regularities (the Cepheid period–luminosity relation, the redshift–distance relation) to the galaxies (S1). No miracle, petition or exemption appears in anything read. Deepen D1: no change to value/certainty."
    C_ledger: {value: UNKNOWN, how_known: "Nothing on judgement, afterlife or reward and punishment in the sources read (S2, S5 Personal life, S6)."}
    D_authority:
      value: 2
      basis: written_profession
      certainty: 0.7
      support: single
      cites: [{source: S2, locator: "pp. 38–39"}]
      how_known: "His own address, capped at 0.7 under §7; a named alternative, so 0.7 in any case. One source id → single (P48)."
      rationale: "Two domains, each with its own authority, so D 2 (same-pattern rule, as for Einstein, Planck and Heisenberg). Knowledge comes from observation and experiment in 'the public domain'; the premises of values come 'from authority, or from revelation, or from the inner conscience' and are tested by personal experience in 'the private domain' (pp. 38–39). Named alternative: 3, if revelation is read as reduced to private conviction that never governs questions of fact."
      alternatives:
        - {value: 3, note: "If revelation is read as reduced to private conviction that never governs questions of fact.", cites: [{source: S2, locator: "pp. 38–39"}]}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Nothing read addresses whether any group is favoured in events. Working science bears on the first question (same laws everywhere) but not on favour for a group in events, so E stays BELOW_THRESHOLD; not scored from working science alone (P19)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD (the P4 test needs A at certainty ≥ 0.7)."}
  statements:
    - text: "The term “invariable” represents an assumption. If an association is observed to hold in many cases of a particular kind, it is assumed that the same association will be found in the next case that will be observed in the future."
      cites: [{source: S2, locator: "p. 10"}]
      date: "1948"
      context: "'The Nature of Science', one of his Hitchcock Lectures at the University of California (1948), printed in S2; on what a law of nature is."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "The premises are in the nature of religious convictions. They are derived from authority, or from revelation, or from the inner conscience. Their validity is tested not by impersonal experiment, but by personal experience."
      cites: [{source: S2, locator: "p. 38"}]
      date: "1938"
      context: "'Experiment and Experience', his Commencement Address at the California Institute of Technology (1938), printed in S2; on the premises of judgements of good and evil."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "The universe in which we live has two aspects. On the one hand is the realm of science, the public domain of positive knowledge. On the other hand is the world of values, the private domain of personal wisdom. Knowledge comes from observation and experiment; wisdom comes from personal experience."
      cites: [{source: S2, locator: "p. 39"}]
      date: "1938"
      context: "Same address; the next page."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "The whole thing is so much bigger than I am, and I can't understand it, so I just trust myself to it, and forget about it."
      cites: [{source: S5, locator: "Personal life / ref 47 (Christianson p. 183)"}, {source: S6, locator: "Creator reply quotation"}]
      date: "1939"
      context: "Grace-reported reply to depressed friend John Emerson (actor/playwright) asking about his belief / belief in a Creator; year from secondary narrative (Nautilus citing Christianson). Reported speech — does not score A or primary alone."
      axes: []
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
    - text: "We do not know why we are born into the world, but we can try to find out what sort of a world it is — at least in its physical aspects."
      cites: [{source: S5, locator: "ref 47"}, {source: S6, locator: "born-into-the-world quotation (Grace Burke Hubble, Huntington MS Characteristics 2:82(9) Box 7)"}]
      context: "Undated adult remark; Christianson p. 183 sequences it after the 1923 Whitehead Creator talk as Hubble growing 'even less certain'. TodayInSci cites Grace Burke Hubble's Huntington writings. Reported speech / Grace mediation — context only, not scored."
      axes: []
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
  changes_over_life:
    - {value: "Baptist upbringing (family church, choir) to an adult view that sets religious premises in a private world of values; Grace-reported Emerson reply (c.1939) shows continued suspension without a dated conversion statement", year: "1901–1939", certainty: 0.5, cites: [{source: S3, locator: "pp. 23, 26"}, {source: S2, locator: "pp. 38–39"}, {source: S5, locator: "ref 47"}], how_known: "Coder's comparison; no dated break documented in own words; Emerson year from secondary narrative."}
  coder_notes: "Deepen D1: AGNOS remains candidate only — system file is filled, but own-voice still silent on God. S2 §7 0.7 cap unchanged (IA user-upload scan). Christianson p. 183 recovered via Wikipedia/TodayInSci quotation of the monograph and Grace Huntington MS path; physical book / full Grace journals still unread. Pope couplet (S2 p. 44) is another's words, not scored. Mayall NAS memoir PDF blocked this pass (403); Wikipedia Personal life covers funeral/burial silence."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "American (Missouri and Illinois family)", certainty: 0.7, cites: [{source: S1, locator: "opening; paragraph 3 ('Rhodes Scholar from Illinois')"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Baptist", certainty: 0.7, cites: [{source: S3, locator: "pp. 14–15"}], how_known: "Christianson."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO, note: "Christianson (pp. 15, 26) says his mother taught the women's Sunday school class and Edwin sang in the choir and attended services; his own religious instruction is not described in the pages read."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1923–1936", certainty: 0.7, cites: [{source: S1, locator: "1923 paragraph to 1936 book"}], how_known: "From the Andromeda Cepheids (1923–1924) to The Realm of the Nebulae (1936), the first and last listed lasting contributions (P29). Span check 2026-10-02 (P29, P30 and its addendum): span unchanged. The 1936 book was not on the list, which ended in 1931; S1 calls it 'his important book' and says that by then he had laid down methods extragalactic astronomers followed for decades, so it was added."}
  age_at_first_lasting_contribution: {value: 34, certainty: 0.7, cites: [{source: S1, locator: "opening; 1923 paragraph"}], how_known: "Born November 1889; Andromeda Cepheids 1923 (month not given in S1). P30 (rule 5): 1923 − 1889 = 34, with no month adjustment; was 33 until the P30 age sweep (2026-10-02)."}
  first_evidence_of_lio_type_views: {value: "Caltech commencement address on science and values", year: 1938, certainty: 0.7, cites: [{source: S2, locator: "pp. 36–39"}], how_known: "Earliest dated statement read; capped by §7."}
  lio_views_relative_to_major_work: {value: "after major work", rationale: "The statements read are from 1938 and 1948, after the 1923–1936 work; earlier views not read.", certainty: 0.5, cites: [{source: S2, locator: "pp. 3, 36"}], how_known: "Dates of the lectures."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "His method as he describes it is inductive: laws are invariable associations assumed from many observed cases (S2, p. 10), not consequences drawn from definitions and axioms.", certainty: 0.5, cites: [{source: S2, locator: "p. 10"}], how_known: "Coder's reading of one lecture."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "paragraphs 3–4"}], how_known: "Nothing on method in his schooling."}
  circle_present: {value: "no", rationale: "He separates the realm of science from the world of values and says nothing identifying God with Nature.", certainty: 0.5, cites: [{source: S2, locator: "p. 39"}], how_known: "Coder's reading."}
  reading: "As belief, not finding: form absent (inductive method), circle absent. The record does not test H1."
  notes: ""

institutions:
  - {value: "Yerkes Observatory (University of Chicago)", role: "graduate student", years: "1914–1917", kind: university, certainty: 0.7, cites: [{source: S1, locator: "paragraph 4"}], how_known: "Britannica."}
  - {value: "U.S. Army", role: "officer in France (rose to major)", years: "1917–1919", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "paragraph 5"}], how_known: "Britannica."}
  - {value: "Mount Wilson Observatory", role: "staff astronomer", years: "1919–1953", kind: "research institute", certainty: 0.7, cites: [{source: S1, locator: "paragraphs 5–6 and last paragraph"}], how_known: "Britannica (start year from the end of the war)."}
  - {value: "Aberdeen Proving Ground, Maryland", role: "administrative post in World War II", years: "1942–1945", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "last paragraph"}], how_known: "Britannica gives 'during World War II' only; years are the U.S. war years."}
collaborators:
  - {value: "Milton Humason", relation: collaborator, note: "measured the galaxy spectra for the redshift–distance relation", certainty: 0.7, cites: [{source: S1, locator: "redshift paragraph"}], how_known: "Britannica."}
  - {value: "Richard C. Tolman", relation: collaborator, note: "galaxy counts and cosmological models in the mid-1930s", certainty: 0.7, cites: [{source: S1, locator: "Tolman sentence"}], how_known: "Britannica."}
  - {value: "Henrietta Swan Leavitt", roster_id: leavitt-henrietta-swan, relation: "influenced by", note: "used her Cepheid period–luminosity relation for the Andromeda distance", certainty: 0.7, cites: [{source: S1, locator: "1923 paragraph"}], how_known: "Britannica (Hubble article names the period–luminosity relationship)."}
  - {value: "George Ellery Hale", relation: "mentor or employer", note: "hired him for Mount Wilson and held the post open during the war", certainty: 0.7, cites: [{source: S1, locator: "paragraph 5"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3: Claude, DeepSeek, Gemini).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 164"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "S2's access copy is a user upload to the Internet Archive (FineReader PDF with page images); fields resting on it are capped at 0.7 under CODING_GUIDE §7 until checked against a library copy of the 1954 Huntington Library edition."
    - "S3 childhood chapters read in publisher's preview (pp. 1–36); adult-religion p. 183 recovered only via Wikipedia/TodayInSci quotation of Christianson and Grace Huntington MS — not a physical-book read."
    - "Mayall NAS memoir PDF blocked (403) this pass; Wikipedia Personal life used for funeral/burial silence (P50)."
    - "Emerson Creator reply and born-into-the-world line are Grace-reported speech; cannot open A or primary alone."
  open_questions:
    - "Physical Christianson (or Grace Burke Hubble Huntington journals Box 7) for own-hand / first-person wording beyond Grace mediation — only that could open AGNOS or A honestly."
    - "Check S2 against a library copy (Huntington Library, 1954) to lift the §7 cap."
    - "Mayall NAS memoir (1970) full PDF if accessible — prior partial web copy had no religion score."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Robert W. Smith"
    citation: "Smith, Robert W. \"Edwin Hubble.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Edwin-Hubble."
    url: "https://www.britannica.com/biography/Edwin-Hubble"
    accessed: 2026-10-02
    reliability_note: "Signed article (one page). Paragraphs counted from the opening '(born November 20, 1889'; the summary box is cited as such."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Edwin Hubble"
    year: 1954
    citation: "Hubble, Edwin. The Nature of Science and Other Lectures. San Marino, CA: The Huntington Library, 1954. Access copy https://archive.org/details/hubble-nature-of-science-and-other-lectures."
    url: "https://archive.org/details/hubble-nature-of-science-and-other-lectures"
    accessed: 2026-10-02
    reliability_note: "His own lectures, published posthumously by the Huntington Library. Access copy is a user upload to the Internet Archive (page images with OCR); quoted passages were checked on the page images. Page numbers are the book's printed numbers. Unofficial copy, so §7 cap of 0.7."
    source_quality: "archive scan (OCR only)"
    used_for: [basics, contribution, worldview, timing, lane_b]
  - id: S3
    type: secondary
    kind: "scholarly book"
    author: "Gale E. Christianson"
    year: 1995
    citation: "Christianson, Gale E. Edwin Hubble: Mariner of the Nebulae. Bristol and Philadelphia: Institute of Physics Publishing, 1995 (ISBN 0750304235). Publisher's preview PDF https://api.pageplace.de/preview/DT0400.9781351453868_A36688568/preview-9781351453868_A36688568.pdf."
    url: "https://api.pageplace.de/preview/DT0400.9781351453868_A36688568/preview-9781351453868_A36688568.pdf"
    accessed: 2026-10-02
    reliability_note: "Full-length biography; childhood chapters read in publisher's preview (pp. 1–36). Adult-religion p. 183 not read in the physical book this pass — recovered via S5/S6 quotation of the Chicago 1996 reprint."
    source_quality: "scholarly edition or monograph"
    used_for: [identity, childhood, worldview, heritage]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S5
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. \"Edwin Hubble.\" Wikipedia, English. https://en.wikipedia.org/wiki/Edwin_Hubble."
    url: "https://en.wikipedia.org/wiki/Edwin_Hubble"
    accessed: 2026-10-24
    reliability_note: "P50 dual bio with Britannica. Personal life quotes Christianson p. 183 (ref 47) and Bezzi Hubble Time p. 93 (ref 48) at length on adult religion; used for those quotations and basic facts. Agnostics category ignored for coding."
    source_quality: "reference entry"
    used_for: [identity, basics, worldview, review]
  - id: S6
    type: secondary
    kind: "other"
    author: "Today in Science History (quoting Christianson / Grace Burke Hubble Huntington MS)"
    citation: "\"Edwin Powell Hubble Quotes.\" Today in Science History. https://todayinsci.com/H/Hubble_Edwin/HubbleEdwin-Quotations.htm."
    url: "https://todayinsci.com/H/Hubble_Edwin/HubbleEdwin-Quotations.htm"
    accessed: 2026-10-24
    reliability_note: "Secondary quotation site. Creator-reply cited to Christianson 1996 p. 183; born-into-the-world line cited to Edwin P. Hubble Manuscript Collection, Huntington Library, writings of Grace Burke Hubble on E.P.H. Characteristics, 2:82(9) Box 7. Used to document Grace mediation path; not own-hand Hubble."
    source_quality: "other"
    used_for: [worldview]
---

# Edwin Hubble

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Edwin Hubble (1889–1953), American astronomer, showed from Cepheid variables that the Andromeda Nebula is a galaxy far outside the Milky Way and found the linear redshift–distance relation for galaxies [S1, S5]. Raised Baptist [S3, pp. 14–15, 23]; as an adult he set public science beside private religious convictions [S2, pp. 38–39]. Deepen D1: Christianson p. 183 recovered (Grace-reported Emerson Creator reply; Whitehead talk then less certain) [S5, S6] — still no own-voice place/deny of God. primary_system **BELOW_THRESHOLD** (AGNOS candidate); **A BELOW**; **B 4 @0.7** support corroborated; **D 2 @0.7** support single; mid BELOW; **not plotted**. Chart-moving **NO**.

## Life and work

Chicago (BS 1910), Oxford as a Rhodes Scholar in jurisprudence, a year of school teaching, then graduate astronomy at Yerkes (PhD 1917), army service in France, and Mount Wilson from 1919 until his death [S1, S5]. No funeral; burial site undisclosed by Grace [S5].

## Contribution and impact

Andromeda Cepheids (1923–24), galaxy classification, the redshift–distance relation with Humason (1929–31), and The Realm of the Nebulae (1936) [S1].

## Childhood and education

Both parents were devout Baptists; the family joined First Baptist Church, Wheaton, in 1901 and Edwin sang in its choir [S3, pp. 14–15, 23, 26].

## Adult working worldview

In his 1938 Caltech address he described "two aspects" of the universe: the public realm of science, known by observation and experiment, and the private world of values, whose premises come "from authority, or from revelation, or from the inner conscience" [S2, pp. 38–39]. In 1948 he described laws as invariable associations, "invariable" being an assumption [S2, p. 10]. Grace-reported Emerson reply (c.1939) on belief/Creator: "trust myself to it, and forget about it" [S5, S6] — reported speech, no locus. D 2 follows the same-pattern rule (two domains).

## Heritage (context only)

American Baptist family [S1; S3]. Context only.

## Timing

First lasting contribution 1923, at about 34 [S1]. Own-voice worldview statements read are from 1938 and 1948 (S2); Emerson reply ~1939 is Grace-reported.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form absent (inductive method); circle absent.

## Open questions

- Physical Christianson / Grace Huntington journals for own-hand wording beyond Grace mediation.
- Library copy of S2 to lift §7 cap.
- Mayall NAS memoir PDF if accessible.

## Research log

- 2026-10-02: Read Britannica (Smith); The Nature of Science and Other Lectures in a user-uploaded Internet Archive scan (pp. 3–44, page images checked for pp. 10, 38, 39); Christianson's publisher preview (pp. 1–36). The NAS memoir (Mayall) was seen only as a partial web copy and not used.
- 2026-10-24 (deepen D1, queue #156): Wikipedia EN dual bio (P50) with full Christianson p.183 quotation; TodayInSci Grace Huntington MS path; Wikiquote/Nautilus Emerson context; FFRF tertiary label ignored for coding; Mayall PDF 403; IA full Christianson borrow blocked. Kept A/primary BELOW (P19/P20). P47 on S1–S6; P48 B corroborated / D single. No fallacy_catalog. No figures/.
