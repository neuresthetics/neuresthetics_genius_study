---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch W)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch W, order P32: F 4, rank 126). Basics from Britannica (Deryck V. Cooke). Own voice read in English in Ellis's translation of Religion and Art (1880; Prose Works vol. 6, 1897; Wagner Library web edition). Not a scientist (P30). primary_system BELOW_THRESHOLD (Schopenhauerian world-denial read into Christianity and Buddhism; no listed code fits; leads CHRIST, BUDDH); A BELOW_THRESHOLD; B 3 (0.5, alt 4; P41 extension); C, E UNKNOWN; D BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Span 1843–1882 (0.7). Not plotted. Draft, not reviewed."}

identity:
  id: wagner-richard
  display_name: "Richard Wagner"
  roster:
    canonical_name: "Richard Wagner"
    rank: 126
    F: 4
    models: [Claude, DeepSeek, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: music
    field_bucket: music
  full_name: {value: "Wilhelm Richard Wagner", certainty: 0.7, cites: [{source: S1, locator: "facts box (In full)"}], how_known: "Britannica."}
  native_name: {value: "Wilhelm Richard Wagner", certainty: 0.7, cites: [{source: S1, locator: "facts box"}], how_known: "German; same as the full name."}
  aliases:
    - {name: "Richard-Wagner", kind: "roster alias"}

basics:
  birth:
    date: {value: "1813-05-22", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "facts box (Born); opening"}], how_known: "Britannica."}
    place: {value: "Leipzig", modern_name: "Leipzig, Germany", polity_then: "Kingdom of Saxony", certainty: 0.7, cites: [{source: S1, locator: "facts box (Born)"}], how_known: "Britannica; polity_then is the coder's."}
  death:
    date: {value: "1883-02-13", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "facts box (Died); opening"}], how_known: "Britannica."}
    place: {value: "Venice", modern_name: "Venice, Italy", polity_then: "Kingdom of Italy", certainty: 0.7, cites: [{source: S1, locator: "facts box (Died)"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1843, certainty: 0.7, cites: [{source: S1, locator: "opening; 'Early life'"}], how_known: "The Flying Dutchman, first produced at Dresden on 2 January 1843, his 'first representative opera' and the first of the major works Britannica lists. Dated by first performance (composed 1841). Alternative 1842 (Rienzi), not listed among the major works."}
  era_bucket: {value: "1750 to 1849", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "1843 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "facts box"}], how_known: "Germany is Western Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Dresden, Zürich and (later) Bayreuth; Germany and Switzerland are Western Europe (P3)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "As recorded."}
  languages_of_work: {value: ["German"], certainty: 0.7, cites: [{source: S1, locator: "body"}, {source: S2, locator: "About this Title (original title 'Religion und Kunst')"}], how_known: "Coder's reading."}
  occupations: {value: ["composer", "dramatist and librettist of his own works", "conductor (Dresden court opera 1843–1849)", "writer of prose treatises"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Early life'"}], how_known: "Britannica: 'dramatic composer and theorist'."}

contribution:
  fields: {value: ["music", "opera and music drama", "music theory and aesthetics"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "The Flying Dutchman: an opera that 'integrated the music with the dramatic content' in an innovative way", year: 1843, kind: work, lasting: "among the major works whose 'operas and music had a revolutionary influence on the course of Western music' (S1, opening)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Early life'"}], how_known: "Britannica. Dated by first performance (2 January 1843)."}
    - {value: "Tristan und Isolde (composed 1857–59; first performed 1865), with a new subtlety in the use of leitmotifs and Liszt-stimulated harmonic subtleties", year: 1865, kind: work, lasting: "among the major works with 'revolutionary influence' (S1, opening)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Early life' (Tristan paragraphs)"}], how_known: "Britannica. Dated by first performance (P30)."}
    - {value: "Music drama woven from leitmotifs, outlined in Opera and Drama and realized in The Ring of the Nibelung", year: 1869, kind: method, lasting: "'This texture would be woven from basic thematic ideas, which have come to be known as leitmotifs'; in The Ring 'his style became unified and deepened immeasurably' (S1); the tetralogy among the major works (S1, opening)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Early life' (Ring paragraphs)"}], how_known: "Britannica dates The Ring '1869–76' (P12 start; range end 1876, P30 addendum b). The theory was written 1849–52; the method is dated by its realization."}
    - {value: "Parsifal", year: 1882, kind: work, lasting: "among the major works with 'revolutionary influence' (S1, opening)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "His operas and music 'had a revolutionary influence on the course of Western music, either by extension of his discoveries or reaction against them'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "The term leitmotif became standard for his method", kind: "standard textbook canon", certainty: 0.7, cites: [{source: S1, locator: "'Early life' (Ring paragraphs)"}], how_known: "Britannica."}
  major_works:
    - {value: "Der fliegende Holländer (The Flying Dutchman)", year: 1843, kind: composition, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "Tannhäuser", year: 1845, kind: composition, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "Lohengrin", year: 1850, kind: composition, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "Oper und Drama (Opera and Drama)", year: 1851, kind: book, certainty: 0.5, cites: [{source: S1, locator: "'Early life' ('From 1849 to 1852 he produced his basic prose works')"}], how_known: "Britannica dates the group 1849–1852; the year is the coder's within it (0.5)."}
    - {value: "Tristan und Isolde", year: 1865, kind: composition, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "Der Ring des Nibelungen", year: 1876, kind: composition, certainty: 0.7, cites: [{source: S1, locator: "opening ('1869–76')"}], how_known: "Britannica."}
    - {value: "Parsifal", year: 1882, kind: composition, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Revolutionary influence on Western music (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household: []
  household_circumstances: {value: "Artistic and theatrical household: several elder sisters became opera singers or actresses", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  schooling:
    - {value: "Kreuzschule, Dresden; Nicolaischule, Leipzig ('a negligent scholar')", stage: "grammar or secondary school", run_by: other, years: "1820s", certainty: 0.5, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica; years not given (coder's decade, 0.5)."}
    - {value: "Leipzig University, enrolled as an adjunct with inferior privileges", stage: university, run_by: "state or municipal", years: "to 1833", certainty: 0.5, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica ('On leaving the university that year' 1833); run_by is the coder's."}
    - {value: "Six months of study with Theodor Weinlig, cantor of the Thomasschule", stage: tutor, run_by: private, years: "c. 1831–1832", certainty: 0.5, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica; years the coder's."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading:
    - {value: "Plays of Shakespeare, Goethe and Schiller; the scores of Beethoven's quartets and symphonies", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  childhood_mentors: []
  languages_in_childhood: {value: ["German"], certainty: 0.5, cites: [{source: S1, locator: "'Early life'"}], how_known: "Coder's reading."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1843–1882", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read on science and religion; the 1880 essay's passing remark on 'the so-called Natural sciences' (S2, pp. 235–236) is about civilisation, not religion."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "His own essay (Religion and Art, 1880, in the span) reads religions through Schopenhauer: 'the deepest basis of every true religion' is 'recognition of the frailty of this world, and the consequent charge to free ourselves therefrom'; Christianity's founder was 'not wise, but divine', his teaching 'the deed of free-willed suffering'; the Buddha's 'last great doctrine' is 'the unity of all things living'; and the Jewish 'Creator of heaven and earth' is rejected as 'a wrathful God of Punishment' whom Art 'doomed' (S2, pp. 213–217). This is a Schopenhauerian world-denial that keeps a Christ without a Creator; no listed code fits it (Britannica dates the turn to Schopenhauer's 'world-renouncing pessimism' to the late 1850s, S1). Leads: CHRIST (the suffering Saviour, Parsifal) and BUDDH (renunciation, unity of the living). Flagged for the auditor (RQ-W2)."}
  secondary_system: {value: UNKNOWN, how_known: "None (P29)."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Lead: 'the suffering god upon the cross ... still fills us with ecstatic throes'; but the Creator is rejected and doctrine read as 'mythic allegories'."}
    - {code: BUDDH, reason: "Lead: renunciation and 'the unity of all things living'; no stated adherence."}
    - {code: ATHE, reason: "Rejected: he speaks of 'the truth ineffably divine' and calls Christ divine; he names the 'Atheism of our day' as the Church's ruin, not his view."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Mixed: he rejects the transcendent 'Creator of heaven and earth' and praises the Greeks, who never thought of 'God' as a Person, yet calls the crucified Christ 'the quintessence of all pitying Love' and 'divine', and the beyond 'superhuman' and 'far above Nature' (S2, pp. 215–217). Named readings: 2–3 (a Schopenhauerian divine without a creator-person) and 1 (Christ as a personal divine). Not enough for a value."}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.5
      cites: [{source: S2, locator: "pp. 215–216; p. 218"}]
      rationale: "Scored on his account of nature (P6). He treats the laws of Nature as 'founded on our own power of perception, and bound inextricably with the functions of our brain', makes belief in miracles a consequence of the inner 'reversal of the will to live', and reads the virgin birth as 'A thought of infinite depth, expressed in form of miracle', not as a physical exception. That reads miracles figuratively without stating an exceptionless order: B 3 at 0.5, alternative 4 (P41 extension, Tolstoy precedent). A BELOW_THRESHOLD reading is possible, since he does not deny the miracles in so many words."
      how_known: "His own essay, read in Ellis's translation in a web edition (0.7 cap), scored at 0.5 because the reading of 'miracle' is the coder's."
      alternatives:
        - {value: 4, note: "P41 extension: miracles rejected as events but no exceptionless order stated.", cites: [{source: S2, locator: "pp. 215–216"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read on reward and punishment of persons in his own view (P19); the essay rejects the 'God of Punishment' as a figure, which is a lead for A, not a ledger."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "Lead toward 3: Art saves 'the spirit of religion by recognising the figurative value of the mythic symbols which the former would have us believe in their literal sense' (S2, p. 213), so dogma's literal claims lose authority. But he keeps 'Revelation' as 'the greatest miracle of all' (the inner turn, p. 216), and says nothing on observation against revelation."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read on the world's order (P7, P19)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A is BELOW_THRESHOLD and B is only at 0.5; no branch of the P4 test is met."}
  statements:
    - text: "ONE might say that where Religion becomes artificial, it is reserved for Art to save the spirit of religion by recognising the figurative value of the mythic symbols which the former would have us believe in their literal sense, and revealing their deep and hidden truth through an ideal presentation."
      cites: [{source: S2, locator: "§I, p. 213"}]
      date: "1880"
      context: "Opening of Religion and Art (Bayreuther Blätter, October 1880)."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "Ellis's English translation (1897), Wagner Library web edition with the 1897 page numbers; German original not read. Web copy (0.7 cap)."
    - text: "If by a miracle we mean an incident that sets aside the laws of Nature; and if, after ripe deliberation, we recognise these laws as founded on our own power of perception, and bound inextricably with the functions of our brain: then belief in miracles must be comprehensible to us as an almost necessary consequence of the reversal of the \"will to live,\" in defiance of all Nature."
      cites: [{source: S2, locator: "§I, pp. 215–216"}]
      date: "1880"
      context: "On 'the belief in miracles' and the demand that natural man know the world as 'null'."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "As above."
    - text: "As though impelled by an artistic need, leaving Jehova the \"Father\" to shift for himself, Belief devised the necessary miracle of the Saviour's birth by a Mother who, not herself a goddess, became divine through her virginal conception of a son without human contact, against the laws of Nature. A thought of infinite depth, expressed in form of miracle."
      cites: [{source: S2, locator: "§I, pp. 217–218"}]
      date: "1880"
      context: "After rejecting the Jewish 'Creator of heaven and earth, a wrathful God of Punishment' as 'doomed by Art' (p. 217)."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "As above; page marker [218] falls inside the passage."
  changes_over_life:
    - {value: "From a revolutionary, optimistic social philosophy (prose works 1849–52) to 'a metaphysical, world-renouncing pessimism, nurtured by his discovery of the philosophy of Arthur Schopenhauer' (by 1857)", certainty: 0.7, cites: [{source: S1, locator: "'Early life' (Zürich and Tristan paragraphs)"}], how_known: "Britannica."}
  coder_notes: "Coder's call. Only one text of his read (Religion and Art, 1880), in English translation; the axes rest on it. Characters' words in the dramas (Parsifal, Tristan) are not his view (P42). Leads not read: letters to Liszt and Röckel on Schopenhauer and Buddhism (1854–56), Mein Leben, Cosima Wagner's diaries (reported speech). RQ-W2: whether the essay's Schopenhauerian reading of Christ and the Buddha is enough for any code."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German (Saxon)", certainty: 0.5, cites: [{source: S1, locator: "facts box"}], how_known: "Coder's reading of the birthplace."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1843–1882", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "From The Flying Dutchman (1843) to Parsifal (1882), dated by first performance (P12, P30). Alternative start 1842 (Rienzi)."}
  age_at_first_lasting_contribution: {value: 30, certainty: 0.7, cites: [{source: S1, locator: "facts box; 'Early life'"}], how_known: "1843 − 1813 = 30 (P30, year difference); 29 by month (premiere 2 January, birthday 22 May)."}
  first_evidence_of_lio_type_views: {value: "1880: laws of Nature founded on perception; miracles read figuratively (B 3)", year: 1880, certainty: 0.5, cites: [{source: S2, locator: "pp. 215–218"}], how_known: "Earliest own text read; earlier prose and letters not read (P30 #7)."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.5, cites: [{source: S2, locator: "pp. 215–218"}], how_known: "1880 falls inside the span."}
  worldview_during_major_work: {value: "Schopenhauerian world-denial read into Christianity and Buddhism; art as the saviour of religion's kernel", certainty: 0.5, cites: [{source: S1, locator: "'Early life'"}, {source: S2, locator: "pp. 213–217"}], how_known: "Coder's summary; the 1850s turn (S1) and the 1880 essay (S2)."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "No geometric method in his work.", certainty: 0.5, cites: [{source: S1, locator: "body"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "body"}], how_known: "Not applicable."}
  circle_present: {value: "partly", rationale: "'the unity of all things living' (the Buddha's doctrine as he states it) and pity for all life; but the world is to be denied, not embraced.", certainty: 0.5, cites: [{source: S2, locator: "p. 214"}], how_known: "Coder's reading."}
  reading: "Art rescues the figurative kernel of religion: world-denial, pity and the unity of the living."
  notes: ""

institutions:
  - {value: "Dresden court opera", role: "conductor", years: "1843–1849", kind: employer, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  - {value: "Philharmonic Society of London", role: "conducted its concerts", years: "1855", kind: other, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
collaborators:
  - {value: "Theodor Weinlig", relation: teacher, note: "six months of composition study", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  - {value: "Arthur Schopenhauer", relation: "influenced by", note: "world-renouncing pessimism; supremacy of music among the arts", certainty: 0.7, cites: [{source: S1, locator: "'Early life' (Tristan paragraphs)"}], how_known: "Britannica."}
  - {value: "Franz Liszt", relation: "influenced by", note: "tone poems and their harmonic subtleties", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  - {value: "Giacomo Meyerbeer", relation: other, note: "recommended him in Paris", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  - {value: "Minna Planer", relation: family, note: "wife from 1836", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 126"}], how_known: "Study roster."}
  controversies:
    - {value: "Anti-Jewish polemic in his prose: Religion and Art itself rejects the 'Jewish tribal god' (pp. 241–242)", certainty: 0.7, cites: [{source: S2, locator: "§III, pp. 241–242"}], how_known: "His essay; Das Judenthum in der Musik (1850, revised 1869) not read."}
  data_quality_flags:
    - "One own text read, in translation; Britannica body read only through the Tristan years (later life, Bayreuth and Cosima not read)."
  open_questions:
    - "RQ-W2: is any code reachable from the Schopenhauerian reading of Christ and the Buddha?"
    - "Read the letters to Liszt (7 June 1855) and Röckel (23 August 1856) and the German Religion und Kunst."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Deryck V. Cooke (Britannica)"
    citation: "Cooke, Deryck V. \"Richard Wagner.\" Encyclopaedia Britannica (updated 8 October 2026). https://www.britannica.com/biography/Richard-Wagner-German-composer. Read live 2026-10-19."
    url: "https://www.britannica.com/biography/Richard-Wagner-German-composer"
    accessed: 2026-10-19
    reliability_note: "Signed body read through the 'Early life' section (to Tristan); question boxes not cited."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Richard Wagner (trans. William Ashton Ellis)"
    citation: "Wagner, Richard. \"Religion and Art\" (Religion und Kunst, Bayreuther Blätter, October 1880). In Richard Wagner's Prose Works, trans. William Ashton Ellis, vol. 6, pp. 211–252. London, 1897. The Wagner Library, edition 1.1 (PDF, University of Notre Dame)."
    url: "https://pls.nd.edu/assets/192300/wagner_religion_and_art_online_version.pdf"
    accessed: 2026-10-19
    reliability_note: "Contemporary English translation with the 1897 page numbers in brackets; web edition, not scan-checked (0.7 cap). German text not read (the Gesammelte Schriften vol. 10 OCR is Fraktur garble)."
    used_for: [worldview, timing, lane_b, review]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Richard Wagner

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Richard Wagner (1813–1883), German dramatic composer and theorist [S1]. Draft: primary_system BELOW_THRESHOLD; A BELOW_THRESHOLD; B 3 (0.5, alt 4); mid_basin BELOW_THRESHOLD. Not plotted.

## Life and work

Dresden, Paris, Zürich [S1].

## Contribution and impact

The Flying Dutchman (1843) to Parsifal (1882); leitmotif music drama [S1].

## Childhood and education

Theatrical family; Kreuzschule, Nicolaischule, Leipzig University [S1].

## Adult working worldview

Religion and Art (1880): Art saves 'the spirit of religion' [S2, p. 213].

## Heritage (context only)

Saxon [S1].

## Timing

1843–1882, from age 30 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Unity of the living [S2, p. 214].

## Open questions

- RQ-W2.

## Research log

- 2026-10-19: Read Britannica (to Tristan) and Ellis's Religion and Art.
