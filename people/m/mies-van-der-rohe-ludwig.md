---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA6)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 20c_early. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #189/228, F 3, rank 201): hunted first-person God/nature statements. Own words via Neumeyer (The Artless Word) as quoted in Colombo 2017: building art as 'spatial execution of spiritual decisions' (1926); unlocked from a 'spiritual centre' / 'life process' (1928); architecture may 'reach up through all degrees of value to the highest realm of spiritual existence' (1938 Armour inaugural). Reported (Farnsworth memoir via Schulze/Windhorst, via Colombo): after Schrödinger What is Life?, 'I want to know what I have to expect after death' — secondhand, not scored. Architectural / spirit-of-epoch / spiritual-centre metaphors do not score pantheism or B (standing rule; Corbusier/Wright P16 path). 'God is in the details' remains architectural axiom (Wikiquote: NY Herald Tribune 28 Jun 1959). Misattributed Wright line 'I believe in God, only I spell it Nature' rejected (not Mies). Heritage: Catholic (Deutsche Biographie 'katholisch'; Domschule Aachen; Michigan Modern Catholic school / Augustine–Aquinas). A UNKNOWN; B UNKNOWN; primary UNKNOWN (CHRIST heritage only — no adult profession). Mid UNKNOWN. Dual bio P50 (Britannica + Wikipedia EN); Deutsche Biographie + Michigan Modern + Colombo/Neumeyer added; P47 on all. Not plotted. Fallacy audit none; figures not refreshed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA6, order P32: F 3, rank 201). Source: Britannica, signed by Wolf Von Eckardt (scholars edition, read in full). Lasting work: the unbuilt Friedrichstrasse Office Building (S1 dates it 1919; MoMA, holder of the drawings, dates it 1921, S3) and Glass Skyscraper (1921) projects, which established 'skin and bones construction'; 'Few unbuilt buildings surpassed them ... in their influence on the development of the architecture of the time' (S1); and the Barcelona chair (1929), 'an instant classic of 20th-century furniture design' (S1). AA6 audit: the Friedrichstrasse project was an entry to the Turmhaus competition (brief November 1921, entries due January 1922), so its public statement (P30) is dated 1921 at 0.5, alternatives 1919 (S1) and 1922 (submission deadline). Span 1921–1929 at 0.5 (weakest lasting item), age 35. S1 also calls him 'the only modern architect who formulated a genuinely contemporary and universally applicable architectural canon' (body of work, undated; not used to extend the span). 'God is in the details' is an attributed axiom on architecture, not a profession of belief; not used. Worldview: no own words read. primary_system UNKNOWN; A UNKNOWN; not a scientist; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: mies-van-der-rohe-ludwig
  display_name: "Ludwig Mies van der Rohe"
  roster:
    canonical_name: "Ludwig Mies van der Rohe"
    rank: 201
    F: 3
    models: [Claude, DeepSeek, Gemini]
    band: "core (3–4)"
    status: "core"
    field: "architecture"
    field_bucket: "arts"
  full_name: {value: "Maria Ludwig Michael Mies", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S4, locator: "infobox / Born"}], how_known: "Britannica and Wikipedia EN agree (P50)."}
  native_name: {value: "Ludwig Mies van der Rohe", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S4, locator: "lede"}], how_known: "Britannica and Wikipedia EN."}
  aliases:
    - {name: "Mies van der Rohe", kind: "roster alias"}
    - {name: "Mies van der Rohe-Ludwig", kind: "roster alias"}
    - {name: "Maria Ludwig Michael Mies", kind: "birth name"}
    - {name: "Ludwig Mies", kind: "other"}

basics:
  birth:
    date: {value: "1886-03-27", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S4, locator: "infobox"}], how_known: "Britannica and Wikipedia EN agree (P50)."}
    place: {value: "Aachen", modern_name: "Aachen, Germany", polity_then: "Kingdom of Prussia, German Empire", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S4, locator: "infobox"}], how_known: "Two sources (P50)."}
  death:
    date: {value: "1969-08-17", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S4, locator: "infobox / Death and legacy"}], how_known: "Britannica and Wikipedia EN (NYT obituary cited on Wikipedia) agree on 17 August 1969 (P50). NDB/Deutsche Biographie header text once prints 19 August — not used against the dual-bio pair."}
    place: {value: "Chicago, Illinois", modern_name: "Chicago, Illinois, United States", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S4, locator: "infobox"}], how_known: "Two sources (P50)."}
  first_lasting_contribution_year: {value: 1921, certainty: 0.5, cites: [{source: S1, locator: "Work after World War I"}, {source: S3, locator: "object 1005.1965"}], how_known: "Friedrichstrasse Skyscraper competition entry ('Honeycomb'), dated 1921 by MoMA (S3); competition entries due January 1922 (P30, a formal submission). Alternatives: 1919 (S1's date) and 1922 (submission deadline). 0.5 while the dates conflict."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "Work after World War I"}], how_known: "1921, and each alternative (1919, 1922), falls in 1850 to 1949 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Germany (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Work after World War I"}], how_known: "Berlin during the span (1921–1929); Chicago from 1937/38."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["German", "English"], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Worked in Germany, then the United States; inferred."}
  occupations: {value: ["architect", "furniture designer", "teacher"], certainty: 0.7, cites: [{source: S1, locator: "Introduction; Work after World War I; Mies in America"}], how_known: "Britannica."}

contribution:
  era_bucket: 20c_early
  fields: {value: ["architecture", "furniture design"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Friedrichstrasse Office Building (1921) and Glass Skyscraper (1921) projects: 'skin and bones construction'", year: 1921, kind: "work", lasting: "'Few unbuilt buildings surpassed them in the variety of ideas and in their influence on the development of the architecture of the time' (S1)", certainty: 0.5, cites: [{source: S1, locator: "Work after World War I"}, {source: S3, locator: "object 1005.1965"}], how_known: "Britannica dates the Friedrichstrasse project 1919; MoMA dates it 1921 and describes the competition entry, 'this seminal project' (S3). 0.5 while the dates conflict; alternatives 1919 and 1922."}
    - {value: "Barcelona chair (for the German Pavilion, Barcelona)", year: 1929, kind: "invention", lasting: "'became an instant classic of 20th-century furniture design' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Work after World War I"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "'the only modern architect who formulated a genuinely contemporary and universally applicable architectural canon'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Late work"}], how_known: "Britannica (Von Eckardt)."}
  major_works:
    - {value: "German (Barcelona) Pavilion", year: 1929, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "Work after World War I"}], how_known: "Britannica."}
    - {value: "Tugendhat House, Brno", year: 1930, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "Work after World War I"}], how_known: "Britannica."}
    - {value: "Seagram Building, New York (with Philip Johnson)", year: 1958, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "Mies in America"}], how_known: "Britannica: 1956–58."}
    - {value: "New National Gallery, Berlin", year: 1968, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "Late work"}], how_known: "Britannica."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Acknowledged leading master of the International Style (S1).", certainty: 0.7, cites: [{source: S1, locator: "Late work"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Catholic (Roman)", certainty: 0.7, cites: [{source: S5, locator: "Religious Denomination / NDB katholisch"}, {source: S6, locator: "Catholic school"}], how_known: "Deutsche Biographie lists denomination katholisch; Michigan Modern: attended Catholic school. Heritage context only — not an adult profession."}
  family_religious_practice: {value: UNKNOWN, how_known: "Denomination and school known; household practice not stated."}
  parents_and_household:
    - {value: "Son of a master mason who owned a small stonecutter's shop (Michael Mies); mother Amalie Rohe", role: "family", certainty: 0.7, cites: [{source: S1, locator: "Early training and influence"}, {source: S5, locator: "Genealogy"}], how_known: "Britannica; Deutsche Biographie genealogy."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated beyond craft household."}
  schooling:
    - {value: "Domschule (cathedral school) / Catholic school in Aachen; left after a few years; apprenticed to Aachen architects at 15; then Bruno Paul and Peter Behrens in Berlin", certainty: 0.7, cites: [{source: S1, locator: "Early training and influence"}, {source: S5, locator: "Biography"}, {source: S6, locator: "opening biography"}], how_known: "Britannica; Deutsche Biographie (Domschule); Michigan Modern (Catholic school; Augustine and Aquinas taught)."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated; later proportional clarity is adult work."}
  early_science_exposure: []
  key_early_reading:
    - {value: "St. Augustine and St. Thomas Aquinas (taught in Catholic school; later architectural-philosophy reading)", certainty: 0.5, cites: [{source: S6, locator: "opening biography"}], how_known: "Michigan Modern; secondary summary — not a childhood diary."}
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated; German-speaking Aachen."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1921–1929", certainty: 0.5, cites: [{source: S1, locator: "Work after World War I"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Criticized reducing life to measurable crystals (reported); quoted Schrödinger later on science silent about God and eternity — still not a self-description of his own God locus (S7)."}
  primary_system: {value: UNKNOWN, how_known: "Catholic upbringing and Domschule are heritage only (S5; S6). Adult first-person package is architectural: building art as spatial execution of spiritual decisions; spiritual centre / life process; spiritual existence as highest architectural value-degree (S7 via Neumeyer). That does not name CHRIST practice, ATHE, PANTHE, or NONE. 'God is in the details' is an architectural axiom (S8), not a profession. No lead strong enough to name."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Catholic denomination and Domschule (S5; S6). Not coded as adult primary: heritage/context; no first-person adult confession of Christian faith found."}
    - {code: PANT, reason: "Web quote farms sometimes attach Wright's 'I believe in God, only I spell it Nature' to Mies. Rejected: that line is Wright (Quote magazine 1966 / Wikiquote Wright), not Mies."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "First-person architectural-spiritual remarks found (S7) do not fix divine locus: 'spiritual decisions', 'spiritual centre', and 'spiritual existence' name architectural/epochal Geist, not God identified with Nature, a transcendent person, or absence of God (P19). Standing rule: architecture metaphors alone do not score A. Do not invent."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30). No P16 cause-order claim about how events happen in nature. Spirit-of-epoch / life-process / framework-for-living language is architectural program (S7), not natural-law metaphysics. Standing rule: architecture/nature metaphors alone do not score B. Do not invent."}
    C_ledger: {value: UNKNOWN, how_known: "Not scored."}
    D_authority: {value: UNKNOWN, how_known: "Not scored. Aquinas/truth reading is intellectual influence (secondary leads), not a scored D profession."}
    E_scope: {value: UNKNOWN, how_known: "Not scored."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied (P19)."}
  statements:
    - text: "One will have to understand that building art is always the spatial execution of spiritual decisions, that it is tied to its times and can only manifest itself in addressing vital tasks with the means of its own time."
      cites: [{source: S7, locator: "Neumeyer p. 253 / 1926 lecture, quoted in Colombo"}]
      date: "1926-03-17"
      context: "Lecture manuscript (first version 17 March 1926); architectural theory of Baukunst as Zeitgeist, not a God-locus profession."
      axes: []
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Does not unlock A/B/primary: 'spiritual decisions' = architectural/epochal spirit. Axes left empty."
    - text: "The building-art can only be unlocked from a spiritual centre and can only be understood as a life process."
      cites: [{source: S7, locator: "Neumeyer p. 299 / Preconditions of Architectural Work 1928, quoted in Colombo"}]
      date: "1928"
      context: "Lecture 'The Preconditions of Architectural Work' (1928), given in several German cities."
      axes: []
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Spiritual centre / life process = architectural philosophy; not pantheism or B."
    - text: "In its simplest form, architecture is entirely rooted in practical considerations, but it can reach up through all degrees of value to the highest realm of spiritual existence."
      cites: [{source: S7, locator: "Neumeyer p. 316 / Armour Institute inaugural 1938, quoted in Colombo"}]
      date: "1938"
      context: "Inaugural address as director of architecture at Armour Institute of Technology."
      axes: []
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Value hierarchy for architecture; empty axes."
    - text: "God is in the details."
      cites: [{source: S8, locator: "On restraint in Design, New York Herald Tribune, 28 June 1959"}]
      date: "1959-06-28"
      context: "Widely associated aphorism on architectural detailing/craft; Wikiquote cites Herald Tribune."
      axes: []
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Architectural axiom — not a profession of theism (already flagged at create)."
    - text: "It is unspiritual. What about man and his hopes for immortality? … I want to know what I have to expect after death."
      cites: [{source: S7, locator: "Farnsworth memoir via Schulze/Windhorst p. 250, quoted in Colombo n.38"}]
      context: "Reported reaction to Schrödinger, What is Life? (1944); secondhand via Edith Farnsworth memoir as cited in Schulze & Windhorst."
      axes: []
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Curiosity about afterlife / rejection of crystal-reductionism; not a scored God-locus or afterlife doctrine. Empty axes."
  changes_over_life: []
  coder_notes: "Deepen D1 2026-10-24: Keep silence on A/B/primary. Neumeyer Artless Word (via Colombo 2017) supplies the main first-person architectural-spiritual package; Deutsche Biographie + Michigan Modern supply Catholic heritage/school; Wikiquote for 'God is in the details'. Reject Wright Nature/God misattribution. Optional unread: Neumeyer full volume page-check; Schulze Critical Biography continuous read for any clearer adult confession; Guardini Letters from Lake Como as influence only (not Mies's profession)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German (Rhineland / Aachen)", certainty: 0.7, cites: [{source: S5, locator: "Genealogy"}], how_known: "Deutsche Biographie genealogy (Aachen; Eifel parents)."}
  religious_heritage_by_birth: {value: "Catholic (Roman)", certainty: 0.7, cites: [{source: S5, locator: "Religious Denomination katholisch"}, {source: S6, locator: "Catholic school"}], how_known: "Deutsche Biographie denomination; Catholic school. Context only."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated in sources read."}
  childhood_catechism: {value: UNKNOWN, how_known: "Catholic school taught Augustine and Aquinas (S6); catechism practice not separately attested."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1921–1929", certainty: 0.5, cites: [{source: S1, locator: "Work after World War I"}], how_known: "From the Friedrichstrasse project (1921, MoMA; alternatives 1919 and 1922) to the Barcelona chair (1929), the two lasting items (P29, P30); 0.5, following its weakest lasting item."}
  age_at_first_lasting_contribution: {value: 35, certainty: 0.5, cites: [{source: S1, locator: "Introduction"}, {source: S3, locator: "object 1005.1965"}], how_known: "1921 − 1886 = 35 (P30 year difference); alternatives 33 (1919) and 36 (1922)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "Architectural-spiritual remarks found; none scored as LIO axes."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None scored."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None scored. 1926–1928 spiritual-decisions / spiritual-centre texts fall in or beside the span but are architectural program, not LIO scores."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Rectilinear forms; 'exceptional sense of proportion' (S1).", certainty: 0.5, cites: [{source: S1, locator: "Mies in America"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No scored LIO data. Architectural spiritual-centre language is not Lane-B pantheism."
  notes: "Do not treat skin-and-bones / nature-as-setting (Farnsworth) as B."

institutions:
  - {value: "Bauhaus", role: "director", years: "1930–1933", kind: "other", certainty: 0.7, cites: [{source: S1, locator: "Work after World War I"}], how_known: "Britannica."}
  - {value: "Armour Institute / Illinois Institute of Technology", role: "director of the School of Architecture", years: "1938–1958", kind: "university", certainty: 0.7, cites: [{source: S1, locator: "Mies in America"}], how_known: "Britannica."}
collaborators:
  - {value: "Philip Johnson", relation: "collaborator", note: "Seagram Building", certainty: 0.7, cites: [{source: S1, locator: "Mies in America"}], how_known: "Britannica."}
  - {value: "Peter Behrens", relation: "teacher", note: "worked in his office", certainty: 0.7, cites: [{source: S1, locator: "Early training and influence"}], how_known: "Britannica."}
  - {value: "Lilly Reich", relation: "collaborator", note: "furniture and interiors, late 1920s–1930s", certainty: 0.7, cites: [{source: S4, locator: "Personal life / Furniture"}], how_known: "Wikipedia EN."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 201"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Worldview: first-person architectural-spiritual remarks found; A/B/primary remain UNKNOWN (architecture metaphors not scored)."
    - "First lasting year 1921 at 0.5 (Britannica 1919, MoMA 1921, entries due 1922)."
    - "After-death remark is secondhand (Farnsworth memoir via Schulze), not a verified transcript."
  open_questions:
    - "Whether Neumeyer full volume or Schulze continuous biography contains any clearer adult God-locus profession (unlikely to clear standing-rule bar alone)."
    - "Guardini influence is reading/network, not Mies's own confession — leave as open secondary lead."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Wolf Von Eckardt"
    citation: "Von Eckardt, Wolf. 'Ludwig Mies van der Rohe.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/Ludwig-Mies-van-der-Rohe/52600"
    url: "https://kids.britannica.com/scholars/article/Ludwig-Mies-van-der-Rohe/52600"
    accessed: 2026-10-24
    reliability_note: "Signed article, scholars edition, read in full at create; dual-bio first source (P50)."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, timing, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [review]
  - id: S3
    type: secondary
    kind: "institutional page"
    author: "The Museum of Modern Art"
    citation: "'Ludwig Mies van der Rohe. Friedrichstrasse Skyscraper Project, Berlin-Mitte, Germany (Exterior perspective from north). 1921.' MoMA collection, object 1005.1965. https://www.moma.org/collection/works/787"
    url: "https://www.moma.org/collection/works/787"
    accessed: 2026-10-19
    reliability_note: "Holder of the drawings; collection page read in full."
    source_quality: "other"
    used_for: [basics, contribution, timing]
  - id: S4
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    year: 2026
    citation: "'Ludwig Mies van der Rohe.' Wikipedia EN. https://en.wikipedia.org/wiki/Ludwig_Mies_van_der_Rohe"
    url: "https://en.wikipedia.org/wiki/Ludwig_Mies_van_der_Rohe"
    accessed: 2026-10-24
    reliability_note: "Dual-bio second source (P50) for identity/dates/places. English article has no Religion infobox field; Spanish Wikipedia's 'Catolicismo romano' not used alone for adult primary."
    source_quality: "reference entry"
    used_for: [identity, basics, collaborators]
  - id: S5
    type: tertiary
    kind: "encyclopedia"
    author: "Wolf Tegethoff / Deutsche Biographie (NDB)"
    year: 1994
    citation: "Tegethoff, Wolf. 'Mies van der Rohe (bis etwa 1921 Mies), Ludwig.' Neue Deutsche Biographie 17 (1994), pp. 479–481; Deutsche Biographie online. https://www.deutsche-biographie.de/118582291.html"
    url: "https://www.deutsche-biographie.de/118582291.html?language=en"
    accessed: 2026-10-24
    reliability_note: "Authoritative German national biography; Religious Denomination katholisch; Domschule; genealogy. Heritage/context only."
    source_quality: "reference entry"
    used_for: [childhood, heritage, basics]
  - id: S6
    type: secondary
    kind: "institutional page"
    author: "Michigan Modern / Michigan State Historic Preservation Office"
    citation: "'Ludwig Mies van der Rohe.' Michigan Modern. https://www.michiganmodern.org/modern-designers/ludwig-mies-van-der-rohe/"
    url: "https://www.michiganmodern.org/modern-designers/ludwig-mies-van-der-rohe/"
    accessed: 2026-10-24
    reliability_note: "State historic-preservation site; states Catholic school and Augustine/Aquinas teaching. Secondary summary for heritage/schooling."
    source_quality: "other"
    used_for: [childhood, heritage]
  - id: S7
    type: secondary
    kind: "journal article"
    author: "Luciana Fornari Colombo"
    year: 2017
    citation: "Colombo, Luciana Fornari. 'What is life? Exploring Mies van der Rohe's concept of architecture as a life process.' The Journal of Architecture 22(8) (2017): 1267–1286. https://doi.org/10.1080/13602365.2017.1393836 . Quotes Mies via Fritz Neumeyer, The Artless Word (MIT Press, 1991), and Farnsworth memoir via Schulze & Windhorst (2012)."
    url: "https://architecture-history.org/library/AJ/Exploring%20Mies%20van%20der%20Rohe's%20concept%20of%20architecture%20as%20a%20life%20process.pdf"
    accessed: 2026-10-24
    reliability_note: "Peer-reviewed; Mies lines are Neumeyer transcriptions quoted with page numbers. Preferred over unsourced quote farms. Farnsworth after-death line is secondhand — flagged."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview]
  - id: S8
    type: secondary
    kind: "other"
    author: "Wikiquote contributors"
    citation: "'Ludwig Mies van der Rohe.' Wikiquote. https://en.wikiquote.org/wiki/Ludwig_Mies_van_der_Rohe (cites 'On restraint in Design', New York Herald Tribune, 28 June 1959, for 'God is in the details')."
    url: "https://en.wikiquote.org/wiki/Ludwig_Mies_van_der_Rohe"
    accessed: 2026-10-24
    reliability_note: "Used only for the attributed Herald Tribune locator of the architectural axiom; not for theology."
    source_quality: "other"
    used_for: [worldview]
---

## Summary

Ludwig Mies van der Rohe (1886–1969), architect [S1]. Deepen D1: architectural-spiritual first-person remarks found; A/B/primary stay UNKNOWN (architecture metaphors not scored). Catholic heritage only. Not plotted.

## Life and work

Aachen (Catholic Domschule); Berlin; Chicago [S1; S5]. Bauhaus director; IIT [S1].

## Contribution and impact

Friedrichstrasse project 1921 [S3]; Barcelona chair 1929 [S1].

## Childhood and education

Catholic school; Augustine and Aquinas taught; mason's son; no formal architectural degree [S1; S5; S6].

## Adult working worldview

Building art as spatial execution of spiritual decisions; spiritual centre / life process; spiritual existence as highest architectural value-degree [S7]. 'God is in the details' is craft axiom [S8]. A/B UNKNOWN. Primary UNKNOWN (CHRIST heritage only).

## Heritage (context only)

Catholic (Roman) [S5; S6].

## Timing

1921–1929 (0.5), age 35 [S1, S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No scored LIO data.

## Open questions

- Neumeyer full volume / Schulze continuous read for any clearer adult God-locus line.
- Guardini as influence only.

## Research log

- 2026-10-24: Deepen D1. Britannica/Wikipedia P50; Deutsche Biographie; Michigan Modern; Colombo/Neumeyer package; Wikiquote axiom. Rejected Wright Nature/God misattribution. Wrote drafts/deepen_mies-van-der-rohe-ludwig.md (untracked). Person-file-only commit. No figures/.
- 2026-10-19: Read Britannica (Von Eckardt, scholars edition).
