---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 6
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, fourth batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (fourth batch, RUNBOOK §1 order). Basics from Britannica (Robert W. Smith). Worldview from his own lectures in The Nature of Science and Other Lectures (Huntington Library, 1954), read in a user-uploaded Internet Archive scan (page images), so capped at 0.7 under CODING_GUIDE §7. Childhood religion from Christianson's biography (publisher's preview). Baptist upbringing; as an adult he set science (public knowledge from observation and experiment) beside a private world of values whose premises 'are in the nature of religious convictions'. primary_system BELOW_THRESHOLD (AGNOS candidate, stub). B 4 (0.7), D 2 (0.7); A, C, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 4 (two blind runs at b21655b). #12/#1 (run 1 note): the Christianson 'p. 183' locator for his adult religion could not be verified (outside the publisher's preview, pp. 13–29) and is withdrawn from the primary_system note and the open question. Decisions P12/P13 recheck: first_lasting_contribution_year 1923 is already the start year of the earliest listed item; the undated '1920s' classification does not set it (noted). No value changed. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02). Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs; BELOW_THRESHOLD vs UNKNOWN per P19; kind lists (P21: research institute, school stage and run_by, scholarly edition). Full before → after list: reports/stage3_rulings_changes.csv. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "P30 rule 5 age sweep: ages recomputed as event year − birth year, with no month adjustment (scripts/recompute_ages.py; every change is in reports/p30_age_changes.csv). No other value changed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Span alignment (P29, P30 and its addendum): timing.major_work_period checked, 1923–1936 unchanged; worldview.working_years 1914–1953 → 1923–1936, equal to the span (P30 addendum f); lasting item added: The Realm of the Nebulae (1936); 2 headline values rest on evidence outside the span and are left unchanged for a ruling (open questions). Listed in reports/p30_span_alignment.csv. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "P31 (continuity rule, v8's pick, 2026-10-02): the 2 values the span check flagged as resting on evidence outside the span are resolved, since changes_over_life documents no change of view between the span and that evidence; no value or certainty changed; the Open questions pointer line was removed. Listed in reports/p30_span_alignment.csv. Not reviewed."}

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
  full_name: {value: "Edwin Powell Hubble", certainty: 1.0, cites: [{source: S1, locator: "'Also known as: Edwin Powell Hubble'"}, {source: S3, locator: "p. 13 ('Edwin Powell, who arrived by kerosene lamp')"}], how_known: "Two sources."}
  native_name: {value: "Edwin Hubble (English)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "English name."}
  aliases:
    - {name: "Hubble-Edwin", kind: "roster alias"}

basics:
  birth:
    date: {value: "1889-11-20", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Marshfield, Missouri", modern_name: "Marshfield, Missouri, USA", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1953-09-28", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "San Marino, California", modern_name: "San Marino, California, USA", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
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
    cites: [{source: S2, locator: "pp. 38–39"}, {source: S3, locator: "pp. 14–29"}]
    how_known: "His lectures place religion with values and say nothing about God, so no code can be read from them. The Baptist upbringing (S3) is childhood religion and is never a code."
    note: "Candidate: AGNOS (stub system file, flagged). Christianson's account of his adult religion is not in the publisher's preview, which covers pp. 13–29; the 'p. 183' locator given here before was never seen and is withdrawn (lens audit, batch 4, #12). Reading the later chapters could settle the code."
  secondary_system: {value: UNKNOWN, how_known: "No system evidence in the sources read."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Leading candidate, not coded (BELOW_THRESHOLD): his lectures treat religious premises as private convictions outside knowledge, which fits suspension, but he states no view on God in what was read. AGNOS is a stub system file (flag).", cites: [{source: S2, locator: "pp. 38–39"}]}
    - {code: CHRIST, reason: "Considered: Baptist upbringing and church choir (S3). Rejected for the adult working years: membership and upbringing are never a code, and nothing read shows adult Christian belief.", cites: [{source: S3, locator: "pp. 14, 23, 26"}]}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Nothing read places or denies God.", note: "Stays BELOW_THRESHOLD (P19/P20): his lectures treat religious premises as private convictions outside knowledge, which bears on the point, but he neither places nor explicitly denies a personal God in what was read."}
    B_cause:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S2, locator: "p. 10 ('The Nature of Science', 1948)"}, {source: S1, locator: "1923 and 1929 paragraphs"}]
      how_known: "His own lecture, capped at 0.7 under §7 (unofficial scan)."
      rationale: "Scored on his account of nature (P6). Laws are general statements of invariable association, and 'invariable' is the working assumption that an association seen in many cases will hold in the next one (p. 10); his own work extended measured regularities (the Cepheid period–luminosity relation, the redshift–distance relation) to the galaxies (S1). No miracle, petition or exemption appears in anything read."
    C_ledger: {value: UNKNOWN, how_known: "Nothing on judgement, afterlife or reward and punishment in the sources read."}
    D_authority:
      value: 2
      basis: written_profession
      certainty: 0.7
      cites: [{source: S2, locator: "pp. 38–39"}]
      how_known: "His own address, capped at 0.7 under §7; a named alternative, so 0.7 in any case."
      rationale: "Two domains, each with its own authority, so D 2 (same-pattern rule, as for Einstein, Planck and Heisenberg). Knowledge comes from observation and experiment in 'the public domain'; the premises of values come 'from authority, or from revelation, or from the inner conscience' and are tested by personal experience in 'the private domain' (pp. 38–39). Named alternative: 3, if revelation is read as reduced to private conviction that never governs questions of fact."
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
  changes_over_life:
    - {value: "Baptist upbringing (family church, choir) to an adult view that sets religious premises in a private world of values; no dated change or statement on God was read", year: "1901–1938", certainty: 0.5, cites: [{source: S3, locator: "pp. 23, 26"}, {source: S2, locator: "pp. 38–39"}], how_known: "Coder's comparison of two sources; no dated break is documented in what was read."}
  coder_notes: "AGNOS is a stub system file (flag). S2 is a posthumous collection of his unpublished lectures (Huntington Library, 1954); the access copy is a user-uploaded Internet Archive scan with page images, so every field resting on it is capped at 0.7 under CODING_GUIDE §7 until checked against a library copy. The Pope couplet he quotes (S2, p. 44) is a quotation of another author and is not scored. S3 was read only in the publisher's preview (pp. 1–36 of the 1995 IOP edition); its chapter on his adult religion is not in the preview."

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
    - "S3 read in the publisher's preview only (pp. 1–36)."
    - "Birth and death facts from one source (Britannica); the NAS memoir by Mayall (1970) was seen only in a partial web copy and is not cited."
  open_questions:
    - "Read Christianson, Edwin Hubble: Mariner of the Nebulae (1995), the passage on his adult religion in the chapters after the preview (pp. 13–29; no page verified), for a first-hand statement on God."
    - "Check S2 against a library copy (Huntington Library, 1954) to lift the §7 cap."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Robert W. Smith"
    citation: "Smith, Robert W. \"Edwin Hubble.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Edwin-Hubble."
    url: "https://www.britannica.com/biography/Edwin-Hubble"
    accessed: 2026-10-02
    reliability_note: "Signed article (one page). Paragraphs counted from the opening '(born November 20, 1889'; the summary box is cited as such."
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
    used_for: [basics, contribution, worldview, timing, lane_b]
  - id: S3
    type: secondary
    kind: "scholarly book"
    author: "Gale E. Christianson"
    year: 1995
    citation: "Christianson, Gale E. Edwin Hubble: Mariner of the Nebulae. Bristol and Philadelphia: Institute of Physics Publishing, 1995 (ISBN 0750304235). Publisher's preview PDF https://api.pageplace.de/preview/DT0400.9781351453868_A36688568/preview-9781351453868_A36688568.pdf."
    url: "https://api.pageplace.de/preview/DT0400.9781351453868_A36688568/preview-9781351453868_A36688568.pdf"
    accessed: 2026-10-02
    reliability_note: "Full-length biography; read in the publisher's preview (early chapters only). Page numbers are the printed numbers."
    used_for: [identity, childhood, worldview, heritage]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# Edwin Hubble

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Edwin Hubble (1889–1953), American astronomer, showed from Cepheid variables that the Andromeda Nebula is a galaxy far outside the Milky Way and found the linear redshift–distance relation for galaxies [S1]. Raised in a Baptist family [S3, pp. 14–15, 23], as an adult he set the public realm of science beside a private world of values whose premises are "in the nature of religious convictions" [S2, pp. 38–39]. primary_system BELOW_THRESHOLD (AGNOS candidate, stub). B 4 and D 2, both at 0.7 (capped: unofficial scan); A and E below threshold, C UNKNOWN; mid_basin below threshold.

## Life and work

Chicago (BS 1910), Oxford as a Rhodes Scholar in jurisprudence, a year of school teaching, then graduate astronomy at Yerkes (PhD 1917), army service in France, and Mount Wilson from 1919 until his death [S1].

## Contribution and impact

Andromeda Cepheids (1923–24), galaxy classification, the redshift–distance relation with Humason (1929–31), and The Realm of the Nebulae (1936) [S1].

## Childhood and education

Both parents were devout Baptists; the family joined First Baptist Church, Wheaton, in 1901 and Edwin sang in its choir [S3, pp. 14–15, 23, 26].

## Adult working worldview

In his 1938 Caltech address he described "two aspects" of the universe: the public realm of science, known by observation and experiment, and the private world of values, whose premises come "from authority, or from revelation, or from the inner conscience" [S2, pp. 38–39]. In 1948 he described laws as invariable associations, "invariable" being an assumption [S2, p. 10]. Nothing read states a view on God. D 2 follows the same-pattern rule (two domains, each with its own authority).

## Heritage (context only)

American Baptist family [S1; S3]. Context only.

## Timing

First lasting contribution 1923, at about 34 [S1]. The worldview statements read are from 1938 and 1948.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form absent (inductive method); circle absent.

## Open questions

- Christianson's chapter on his adult religion; a library copy of S2.

## Research log

- 2026-10-02: Read Britannica (Smith); The Nature of Science and Other Lectures in a user-uploaded Internet Archive scan (pp. 3–44, page images checked for pp. 10, 38, 39); Christianson's publisher preview (pp. 1–36). The NAS memoir (Mayall) was seen only as a partial web copy and not used.
