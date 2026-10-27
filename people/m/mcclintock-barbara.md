---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 4
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch D)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to biology. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-25, by: "Grok Bot", summary: "Perpetual deepen: native_name TODO→Barbara McClintock @1.0 (matches full_name). Chart-moving NO."}
    - {date: 2026-10-23, by: "Grok Bot", summary: "Deepen pass D1 (queue #10). P47 source_quality on every source. Primary: The Origin and Behavior of Mutable Loci in Maize (PNAS 1950; S4 full text now read) and Nobel lecture The Significance of Responses of the Genome to Challenge (8 Dec 1983; new S6) — own words on chromosome mechanisms, precise control of transposition, genome sensing/programmed responses. B_cause stays 3 @ 0.5 (P16 Hilbert / P35: lawful physical regularities, no no-exception claim) but basis inference_from_work → written_profession; support single → corroborated (S4+S6). A_locus stays UNKNOWN after Nobel biographical note, Nobel lecture, 1950 PNAS, Keller 1983 (S7 interview biography; Tibetan Buddhism / oneness quotes are epistemology, not God), Martienssen oral history and Humanist profile (both secondary paraphrase, unused for A under P19). Creighton & McClintock 1931 (S3) still bibliographic only (PMC/PNAS PDF blocked). Chart: still unplotted (A UNKNOWN; B faded @ 0.5). No fallacy_catalog (Jason 2026-10-23). Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch D, order P32: F 5, rank 10). Basics from her Nobel autobiographical note and the NLM Profiles in Science overview; paper dates from Europe PMC records of PNAS. No statement of hers on religion, God or nature was read. primary_system UNKNOWN; B_cause 3 at 0.5 from working science (P35, alternative 4); A, C, D UNKNOWN; E BELOW_THRESHOLD; mid_basin UNKNOWN. Draft, not reviewed."}

identity:
  id: mcclintock-barbara
  display_name: "Barbara McClintock"
  roster:
    canonical_name: "Barbara McClintock"
    rank: 10
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: genetics
    field_bucket: "biology / life science"
  full_name: {value: "Barbara McClintock", certainty: 1.0, cites: [{source: S1, locator: "heading"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources."}
  native_name: {value: "Barbara McClintock", certainty: 1.0, cites: [{source: S1, locator: "heading"}, {source: S2, locator: "paragraph 1"}], how_known: "Same as full_name (English)."}
  aliases:
    - {name: "Barbara-McClintock", kind: "roster alias"}
    - {name: "McClintock-Barbara", kind: "roster alias"}

basics:
  birth:
    date: {value: "1902-06-16", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "table ('Hartford, Connecticut, U.S.A, 16 June, 1902')"}, {source: S2, locator: "paragraph 1"}], how_known: "Her own Nobel note and NLM agree."}
    place: {value: "Hartford, Connecticut", modern_name: "Hartford, Connecticut, USA", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "table"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources."}
  death:
    date: {value: "1992-09-02", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "closing note"}, {source: S2, locator: "last paragraph"}], how_known: "Two sources."}
    place: {value: "Huntington Hospital, near Cold Spring Harbor, New York", modern_name: "Huntington, New York, USA", polity_then: "United States", certainty: 0.7, cites: [{source: S2, locator: "last paragraph"}], how_known: "NLM alone."}
  first_lasting_contribution_year: {value: 1931, certainty: 1.0, cites: [{source: S3, locator: "PNAS 17(8):492–497, August 1931"}, {source: S2, locator: "paragraph 4 (physical correlate of crossing-over)"}], how_known: "Creighton and McClintock's cytological proof of crossing-over, published August 1931 (primary journal record), the earliest listed lasting contribution (P30)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S3, locator: "1931"}], how_known: "From 1931 (P2)."}
  region_of_birth: {value: "North America", certainty: 1.0, cites: [{source: S1, locator: "table"}, {source: S2, locator: "paragraph 1"}], how_known: "USA (P3)."}
  region_of_work: {value: "North America", certainty: 1.0, cites: [{source: S1, locator: "positions held"}, {source: S2, locator: "paragraphs 2–3"}], how_known: "Cornell, Missouri, Cold Spring Harbor."}
  sex_as_recorded: {value: "female", certainty: 1.0, cites: [{source: S2, locator: "paragraph 1 ('She')"}, {source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [English], certainty: 1.0, cites: [{source: S3, locator: "title"}, {source: S4, locator: "title"}], how_known: "Her papers are in English."}
  occupations: {value: ["cytogeneticist", "research scientist"], certainty: 1.0, cites: [{source: S1, locator: "text and positions"}, {source: S2, locator: "paragraphs 1–3"}], how_known: "Two sources."}

contribution:
  primary_domain: biology
  fields: {value: ["cytogenetics", "maize genetics"], certainty: 1.0, cites: [{source: S1, locator: "paragraph 3"}, {source: S2, locator: "paragraph 4"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Cytological proof that genetic crossing-over goes with physical exchange between chromosomes (with Harriet Creighton)", year: 1931, kind: discovery, lasting: "physical basis of genetic recombination", certainty: 1.0, cites: [{source: S3, locator: "PNAS 17:492–497 (1931)"}, {source: S2, locator: "paragraph 4"}], how_known: "Primary record and NLM."}
    - {value: "Transposition ('mobile genetic elements') and gene control in maize", year: 1950, kind: discovery, lasting: "Nobel Prize 1983 for mobile genetic elements", certainty: 1.0, cites: [{source: S4, locator: "PNAS 36:344–355 (June 1950); Ds/Ac transposition and precise developmental control, pp. 344–355"}, {source: S6, locator: "Nobel lecture 1983 (controlling elements; genome responses)"}, {source: S2, locator: "paragraphs 4–6"}], how_known: "1950 PNAS full text (deepen D1) plus Nobel lecture; NLM places the work in the 1940s and 1950s (a 1948 Carnegie Year Book report was not opened)."}
  evidence_of_impact:
    - {value: "Nobel Prize in Physiology or Medicine 1983, unshared", kind: "honours in lifetime", certainty: 1.0, cites: [{source: S2, locator: "paragraph 6"}, {source: S6, locator: "lecture heading"}], how_known: "NLM and her Nobel lecture."}
  major_works:
    - {value: "The origin and behavior of mutable loci in maize, PNAS 36: 344–355", year: 1950, kind: "paper or paper series", certainty: 1.0, cites: [{source: S4, locator: "full text pp. 344–355"}], how_known: "Primary paper read."}
    - {value: "The Significance of Responses of the Genome to Challenge (Nobel lecture)", year: 1983, kind: "paper or paper series", certainty: 1.0, cites: [{source: S6, locator: "lecture title page"}], how_known: "Primary lecture text."}
  honours:
    - {value: "National Medal of Science", year: 1970, certainty: 0.5, cites: [{source: S1, locator: "awards (1970)"}, {source: S2, locator: "paragraph 6 (1971)"}], how_known: "Real dispute on the year: her Nobel list says 1970, NLM says 1971.", alternatives: [{value: "1971", cites: [{source: S2, locator: "paragraph 6"}]}]}
  definition_fit: {value: "clearly meets", rationale: "Discovered transposition; physical basis of crossing-over.", certainty: 1.0, cites: [{source: S2, locator: "paragraphs 4–6"}, {source: S3, locator: "record"}, {source: S4, locator: "full text"}], how_known: "Primary paper and NLM."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not in the sources read (Nobel note, NLM, Keller 1983)."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not in the sources read."}
  parents_and_household:
    - {value: "One of four children of Thomas Henry McClintock and Sara Handy McClintock", role: other, certainty: 0.7, cites: [{source: S2, locator: "paragraph 1"}], how_known: "NLM alone."}
  household_circumstances: {value: TODO}
  schooling:
    - {value: "Erasmus Hall High School, Brooklyn; graduated 1919", stage: "grammar or secondary school", years: "–1919", certainty: 1.0, cites: [{source: S1, locator: "table"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1931–1950", certainty: 1.0, cites: [{source: S3, locator: "1931"}, {source: S4, locator: "1950"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No statement of hers pairing science and religion as such. Keller (S7) records interview remarks on Tibetan Buddhist training methods and on limits of 'the scientific method' as a route to 'the truth' — epistemology, not a science–religion relation (P19)."}
  primary_system: {value: UNKNOWN, cites: [{source: S1, locator: "whole note"}, {source: S2, locator: "whole overview"}, {source: S6, locator: "whole lecture"}, {source: S7, locator: "interview chapters on mysticism / Tibetan Buddhism"}], how_known: "Nothing of hers asserting or denying God (P19). Keller/Martienssen report interest in Tibetan Buddhist training and 'oneness'; those are not a primary_system code and are unused for A.", note: "Lead unused: Humanist.com profile ('little patience for religion') is tertiary opinion. Comfort, The Tangled Field (2001) not opened."}
  secondary_system: {value: UNKNOWN, how_known: "No system evidence."}
  candidate_codes_considered: []
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Deepen D1 checked Nobel biographical note (S1), Nobel lecture (S6), 1950 PNAS (S4), Keller 1983 interview biography (S7): no first-person statement placing or denying God (P19). Keller quotes on Tibetan Buddhism and 'Basically, everything is one' concern knowing/method, not A. Martienssen oral history and Humanist profile are secondary paraphrase, unused for A."}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S4, locator: "pp. 345, 354 (mechanism of variegation; precise control of Ds/Ac transposition)"}, {source: S6, locator: "pp. 180–181, 199 (programmed genome responses; genome as sensing organ)"}]
      how_known: "Her own 1950 PNAS paper (S4) and 1983 Nobel lecture (S6). Scientist under P30 (results about physical/biological systems). Named alternative 4, so 0.5 (P16 Hilbert addendum / P35). Two independent publications → corroborated (P48)."
      rationale: "Scored on her account of nature (P6). 1950: variegation rests on a chromosome mechanism 'basically the same in all organisms'; Ds/Ac transposition occurs under 'precise control' by Ac dosage/organization. 1983: genomes meet challenges by programmed/sensing mechanisms and the genome is a 'highly sensitive organ of the cell' that monitors, corrects, and restructures. These are lawful physical/biological regularities in her own words, with no stated no-exception / miracle claim → B 3 at 0.5, alternative 4 (P16 Hilbert; P35). Named alternative: 4. Keller's paraphrase that she shares the credo 'nature is lawful' is not used (P49)."
    C_ledger: {value: UNKNOWN, how_known: "Nothing in the sources read (P19)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing on revelation; working science does not bear on D (P19)."}
    E_scope: {value: BELOW_THRESHOLD, note: "Scored on the world's order (P7); not scored from working science alone.", how_known: "BELOW_THRESHOLD under P19."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, which takes precedence (§6, P19)."}
  statements:
    - text: "The author believes that the mechanism underlying the phenomenon of variegation is basically the same in all organisms."
      cites: [{source: S4, locator: "p. 345"}]
      date: "1950"
      context: "Opening of The Origin and Behavior of Mutable Loci in Maize (PNAS). States a common physical mechanism across organisms."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-23
    - text: "There can be little question that transpositions of both Ds and Ac occur and that the time of their occurrence in the development of a tissue is under precise control. This control is determined by the number of Ac loci present and their organization and possibly their position in the chromosome complement."
      cites: [{source: S4, locator: "p. 354"}]
      date: "1950"
      context: "Closing discussion of Ds/Ac in the 1950 PNAS paper; developmental timing of transposition as a controlled chromosomal process."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-23
    - text: "In contrast to such \"shocks\" for which the genome is unprepared, are those a genome must face repeatedly, and for which it is prepared to respond in a programmed manner. … Each of these initiates a highly programmed sequence of events within the cell that serves to cushion the effects of the shock. Some sensing mechanism must be present in these instances to alert the cell to imminent danger, and to set in motion the orderly sequence of events that will mitigate this danger."
      cites: [{source: S6, locator: "pp. 180–181 (Introduction)"}]
      date: "1983-12-08"
      context: "Nobel lecture, The Significance of Responses of the Genome to Challenge. Programmed cellular responses to stress."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-23
    - text: "In the future attention undoubtedly will be centered on the genome, and with greater appreciation of its significance as a highly sensitive organ of the cell, monitoring genomic activities and correcting common errors, sensing the unusual and unexpected events, and responding to them, often by restructuring the genome."
      cites: [{source: S6, locator: "p. 199 (Concluding statement)"}]
      date: "1983-12-08"
      context: "Closing paragraph of the Nobel lecture."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-23
  changes_over_life: []
  coder_notes: "Deepen D1: B now rests on her own 1950 PNAS and 1983 Nobel lecture (written_profession), still capped at 0.5 with alt 4 (no no-exception claim). A stays UNKNOWN — no God statement in S1/S4/S6; Keller's interview quotes on Tibetan Buddhism and oneness are epistemology (P19). Keller's 'nature is lawful' sentence is Keller's voice, unused for B (P49). Martienssen ('she never believed in them') and Humanist.com ('little patience for religion') are secondary/tertiary, unused for A. Creighton 1931 full text not opened (PDF blocked)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: TODO}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not in the sources read."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not in the sources read."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not in the sources read."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1931–1950", certainty: 1.0, cites: [{source: S3, locator: "1931"}, {source: S4, locator: "1950"}], how_known: "First to last listed lasting contribution (P29, P30). Her later South American maize work (published 1981) is not listed as lasting; the 1983 Nobel lecture restates earlier results."}
  age_at_first_lasting_contribution: {value: 29, certainty: 1.0, cites: [{source: S3, locator: "1931"}, {source: S1, locator: "1902"}], how_known: "1931 − 1902 = 29 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement scored at 3 or 4 with ≥0.7 (P27)."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "B 3 @ 0.5 rests on lawful regularities without a no-exception claim and is not an LIO-type view at 3/4 with ≥0.7 (P27). Nothing on God.", certainty: 0.5, cites: [{source: S4, locator: "pp. 345, 354"}, {source: S6, locator: "pp. 180–181, 199"}], how_known: "Scored B is below the LIO-type-view bar (P27)."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Experimental cytogenetics; nothing read on proof training.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Nothing read."}
  circle_present: {value: "unclear", rationale: "No God–Nature statement read.", certainty: 0.5, cites: [{source: S1, locator: "whole note"}, {source: S6, locator: "whole lecture"}], how_known: "No evidence either way."}
  reading: "As belief, not finding: form and circle unclear. Does not test H1."
  notes: ""

institutions:
  - {value: "Cornell University", role: "student (B.S. 1923, M.A. 1925, Ph.D. 1927), instructor, research associate", years: "1919–1936", kind: university, certainty: 1.0, cites: [{source: S1, locator: "table"}, {source: S2, locator: "paragraphs 1–3"}], how_known: "Two sources."}
  - {value: "Carnegie Institution of Washington, Department of Genetics, Cold Spring Harbor", role: "staff member", years: "1942–1967", kind: "research institute", certainty: 1.0, cites: [{source: S1, locator: "positions"}, {source: S2, locator: "paragraph 3"}], how_known: "Two sources."}
collaborators:
  - {value: "Harriet B. Creighton", relation: collaborator, note: "co-author of the 1931 paper", certainty: 1.0, cites: [{source: S3, locator: "authors"}], how_known: "Primary record."}
  - {value: "George W. Beadle and Marcus M. Rhoades", relation: collaborator, note: "Cornell maize cytogenetics group", certainty: 0.7, cites: [{source: S1, locator: "paragraph 5"}], how_known: "Her own Nobel note (autobiographical; one source)."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 10"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "National Medal of Science year: 1970 (Nobel note) vs 1971 (NLM)."
    - "Britannica blocked (Cloudflare, 2026-10-15)."
    - "Creighton & McClintock 1931 PNAS full text: PMC/PNAS PDF blocked this pass (2026-10-23); bibliographic record only."
    - "1950 PNAS statements verified against an unofficial course PDF of the PNAS pages (UniRoma), not the publisher PDF (P21 unofficial web copy)."
  open_questions:
    - "Open Creighton & McClintock 1931 PNAS full text for a further B primary (crossing-over as physical exchange)."
    - "Comfort, The Tangled Field (2001), for any first-person God/religion lines beyond Keller."
    - "Carnegie Year Book reports 1948–1951 if an earlier public statement of transposition is needed for dating."

sources:
  - id: S1
    type: primary
    kind: "published work by the subject"
    author: "Barbara McClintock"
    year: 1984
    citation: "McClintock, Barbara. \"Barbara McClintock – Biographical.\" In Les Prix Nobel 1983, ed. Wilhelm Odelberg. Stockholm: Nobel Foundation, 1984. NobelPrize.org."
    url: "https://www.nobelprize.org/prizes/medicine/1983/mcclintock/biographical/"
    accessed: 2026-10-23
    source_quality: "primary / own words"
    reliability_note: "Autobiographical note written at the time of the award, with a table of dates and positions. Re-read for A (no God/religion)."
    used_for: [identity, basics, contribution, childhood, worldview, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "National Library of Medicine"
    citation: "National Library of Medicine. \"Biographical Overview.\" The Barbara McClintock Papers, Profiles in Science. https://profiles.nlm.nih.gov/spotlight/ll/feature/biographical-overview."
    url: "https://profiles.nlm.nih.gov/spotlight/ll/feature/biographical-overview"
    accessed: 2026-10-15
    source_quality: "reference entry"
    reliability_note: "Archival institution's overview."
    used_for: [identity, basics, contribution, childhood, worldview, timing, lane_b, institutions]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Harriet B. Creighton and Barbara McClintock"
    year: 1931
    citation: "Creighton, Harriet B., and Barbara McClintock. \"A Correlation of Cytological and Genetical Crossing-Over in Zea Mays.\" PNAS 17, no. 8 (1931): 492–497. https://doi.org/10.1073/pnas.17.8.492."
    url: "https://doi.org/10.1073/pnas.17.8.492"
    accessed: 2026-10-23
    source_quality: "primary / own words"
    reliability_note: "Primary journal paper; this pass still only Europe PMC/PNAS bibliographic record (PMC1076098). Full-text PDF blocked (Cloudflare). Used for contribution dating, not for B quotes."
    used_for: [basics, contribution, timing, collaborators]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Barbara McClintock"
    year: 1950
    citation: "McClintock, Barbara. \"The Origin and Behavior of Mutable Loci in Maize.\" PNAS 36, no. 6 (1950): 344–355. https://doi.org/10.1073/pnas.36.6.344."
    url: "https://doi.org/10.1073/pnas.36.6.344"
    accessed: 2026-10-23
    source_quality: "primary / own words"
    reliability_note: "Deepen D1: full text read from an unofficial UniRoma course PDF reproducing the PNAS pages (pp. 344–355). Statements marked verified_against unofficial web copy. Publisher/PMC PDF blocked."
    used_for: [basics, contribution, worldview, timing]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [identity, review]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Barbara McClintock"
    year: 1983
    citation: "McClintock, Barbara. \"The Significance of Responses of the Genome to Challenge.\" Nobel Lecture, 8 December 1983. In Les Prix Nobel 1983. Stockholm: Nobel Foundation. NobelPrize.org PDF."
    url: "https://www.nobelprize.org/uploads/2018/06/mcclintock-lecture.pdf"
    accessed: 2026-10-23
    source_quality: "primary / own words"
    reliability_note: "Official Nobel Foundation PDF of the lecture; page numbers from the Les Prix Nobel reprint in that PDF (pp. 180–199)."
    used_for: [contribution, worldview, timing, lane_b]
  - id: S7
    type: secondary
    kind: "scholarly book"
    author: "Evelyn Fox Keller"
    year: 1983
    citation: "Keller, Evelyn Fox. A Feeling for the Organism: The Life and Work of Barbara McClintock. San Francisco: W. H. Freeman, 1983."
    accessed: 2026-10-23
    source_quality: "scholarly edition or monograph"
    reliability_note: "Interview-based scholarly biography. Used as A-negative check and for open questions. Keller's own 'nature is lawful' paraphrase (near pp. 199–200 of the Freeman printing) is not McClintock's words and is unused for B (P49). Interview quotes on Tibetan Buddhism and oneness unused for A (epistemology, P19)."
    used_for: [worldview, review]

---

# Barbara McClintock

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Barbara McClintock (1902–1992), American cytogeneticist, gave with Harriet Creighton the cytological proof of crossing-over (1931) and discovered transposition in maize (1950 paper), for which she received the unshared 1983 Nobel Prize [S2; S3; S4; S6]. Deepen D1 (P47–P50): her own 1950 PNAS and 1983 Nobel lecture give B 3 at 0.5, written_profession, corroborated (S4+S6); A stays UNKNOWN (no God statement; Keller Buddhism/oneness quotes unused for A); mid_basin UNKNOWN. Still unplotted (A UNKNOWN; B faded).

## Life and work

Cornell (Ph.D. 1927), Missouri (1936–1941), Cold Spring Harbor from 1942 [S1; S2].

## Contribution and impact

Crossing-over proof [S3]; mobile genetic elements / controlling elements [S4; S6; S2]. Nobel Prize 1983 [S2; S6].

## Childhood and education

Erasmus Hall High School, Brooklyn [S1; S2].

## Adult working worldview

No God statement found [S1; S4; S6; S7]. B scored 3 at 0.5 from her own account of chromosome mechanisms and genome responses (written_profession; alt 4 under P16/P35), corroborated across the 1950 paper and the Nobel lecture [S4; S6].

## Heritage (context only)

Not researched.

## Timing

First lasting contribution 1931, at 29 [S3]. Major-work period 1931–1950 [S3; S4].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form and circle unclear; no God–Nature statement [S1; S6].

## Open questions

- Creighton & McClintock 1931 full text (PDF blocked this pass).
- Comfort (2001); Carnegie Year Books 1948–1951.

## Research log

- 2026-10-15: Read the Nobel note, NLM overview and Europe PMC records. Britannica blocked.
- 2026-10-23: Deepen D1 (queue #10). S4 full text (unofficial PNAS-page PDF); S6 Nobel lecture (official PDF); S7 Keller 1983. B support single → corroborated; basis → written_profession; A stays UNKNOWN. P47 labels. No fallacy_catalog (Jason 2026-10-23).
