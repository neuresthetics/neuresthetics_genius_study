---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch T; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: '2026-10-25'
  change_log:
    - {date: 2026-10-25, by: "Grok Bot", summary: "Perpetual deepen: family_religion TODO synced from religious_heritage_by_birth (context only). Chart-moving NO. No figures/; no fallacy_catalog."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch T, order P32: F 4, rank 112). Basics from Britannica (Britannica Editors; revised by Kara Rogers), the Science History Institute and the Salk Institute. Worldview from The John Callaway Interviews (WTTW; broadcast 30 June 1981), AAPB transcript (status 'Correct'). Scientist (P30). All worldview fields rest on one recorded interview after the working years (P1 cap 0.5). primary_system PANT (0.5, alt ATHE); A 4 (0.5, alt BELOW_THRESHOLD); B 3 (0.5, alt 4); C UNKNOWN; D BELOW_THRESHOLD; E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD (A 4 at 0.5). Plotted (faded). Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit fixes for batch T (blind audit of 754bb24, run 1: SA3, SA7 WEAKEN; ruling T2, v8's call on the auditor's advice). primary_system PANT -> ATHE at 0.5, alternative PANT ('God was invented because of the necessity for having a form of order' withdraws the entity-term). The killed-virus principle is listed as a discovery (Britannica: killed virus of each of the three types 'could induce antibody formation in monkeys'), so the scientist status no longer rests on an invention (P33). S4 locators now carry AAPB transcript timecodes. A 4, B 3 (0.5) unchanged; plot unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #111 / F4 rank 112). Goals: lift A/B to 0.7 if stronger own-voice; chart-moving if both ≥0.7 and/or corroboration. Read The Survival of the Wisest (1973 Harper & Row; unofficial PDF OCR, S6) — post-span under P1, so certainty stays 0.5; no lift to 0.7. Dual bio: Britannica (S1) + Wikipedia EN (S7) (P50). P47 source_quality on S1–S7. A stays 4 @0.5 alt BELOW (ruling T2); support single→corroborated (S4 interview + S6 book: 'without arbitrary reference to a presumed purposeful Being'; order that prevails in the universe). B stays 3 @0.5 alt 4 (P16 addendum / P35); support single→corroborated (S4 + S6: 'order that prevails in the universe'; cannot 'exist free from the operation of the laws of Nature'; cannot 'defy, or [act] counter to, the laws of Nature'). D BELOW→4 @0.5 (S6 naturalistic vs arbitrary moralistic self-regulation; religion founders' systems 'product of imagination, without basis in reality'). primary ATHE @0.5 alt PANT unchanged; SECHUM noted (AHA Humanist of the Year 1976, S7) but rejected for primary. mid BELOW (A 0.5). Chart-moving YES: hollow→filled (both A and B corroborated); still faded (min(A,B)=0.5). Man Unfolding / Anatomy of Reality unread. No fallacy_catalog. No figures/. Draft, not reviewed."}

identity:
  id: salk-jonas
  display_name: "Jonas Salk"
  roster:
    canonical_name: "Jonas Salk"
    rank: 112
    F: 4
    models: [Claude, DeepSeek, Gemini, Grok]
    band: "core (3–4)"
    status: core
    field: medicine
    field_bucket: medicine
  full_name: {value: "Jonas Edward Salk", certainty: 1.0, cites: [{source: S1, locator: "facts box (In full)"}, {source: S3, locator: "opening"}, {source: S7, locator: "infobox / lead"}], how_known: "Britannica, the Salk Institute and Wikipedia agree."}
  native_name: {value: "Jonas Edward Salk", certainty: 0.7, cites: [{source: S1, locator: "facts box"}], how_known: "English; same as the full name."}
  aliases:
    - {name: "Jonas-Salk", kind: "roster alias"}
    - {name: "Salk-Jonas", kind: "roster alias"}

basics:
  birth:
    date: {value: "1914-10-28", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "facts box (Born)"}, {source: S3, locator: "opening"}, {source: S7, locator: "infobox"}], how_known: "Britannica, the Salk Institute and Wikipedia agree."}
    place: {value: "New York, New York", modern_name: "New York City, United States", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "facts box (Born)"}, {source: S3, locator: "opening"}, {source: S7, locator: "infobox"}], how_known: "Britannica, the Salk Institute and Wikipedia."}
  death:
    date: {value: "1995-06-23", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "facts box (Died)"}, {source: S3, locator: "closing paragraph"}, {source: S7, locator: "infobox"}], how_known: "Britannica, the Salk Institute and Wikipedia."}
    place: {value: "La Jolla, California", modern_name: "La Jolla, San Diego, California, United States", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "facts box (Died)"}, {source: S3, locator: "closing paragraph"}, {source: S7, locator: "infobox"}], how_known: "Britannica, the Salk Institute and Wikipedia."}
  first_lasting_contribution_year: {value: 1952, certainty: 0.7, cites: [{source: S2, locator: "The 'Killed-Virus' Principle"}], how_known: "The killed-virus polio vaccine, first tested in humans in 1952 (S2); proven in the 1954 field trial and announced 12 April 1955 (S2, S3). A range date sets the span start (P12)."}
  era_bucket: {value: "1950 on", certainty: 0.7, cites: [{source: S2, locator: "The 'Killed-Virus' Principle"}], how_known: "1952 (P2)."}
  region_of_birth: {value: "North America", certainty: 1.0, cites: [{source: S1, locator: "facts box"}, {source: S3, locator: "opening"}], how_known: "United States (P3)."}
  region_of_work: {value: "North America", certainty: 1.0, cites: [{source: S1, locator: "body"}, {source: S2, locator: "The Virus Research Laboratory and Poliovirus"}], how_known: "Pittsburgh."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S3, locator: "opening"}], how_known: "'the eldest of three sons'."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Coder's reading."}
  occupations: {value: ["physician", "virologist and medical researcher", "professor of bacteriology, preventive and experimental medicine (Pittsburgh)", "founding director of the Salk Institute"], certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Britannica."}

contribution:
  fields: {value: ["virology", "immunology", "medicine"], certainty: 0.7, cites: [{source: S1, locator: "body"}, {source: S2, locator: "Salk's Education and Work on Influenza"}], how_known: "Britannica and the Science History Institute."}
  lasting_original_contributions:
    - {value: "First safe and effective (inactivated, killed-virus) polio vaccine: killed virus of each of the three types induces antibodies; human testing 1952; national field trial 1954; declared safe and effective 12 April 1955", year: 1952, kind: invention, lasting: "'developed the first safe and effective vaccine for polio' (S1); recommended again for US use in 1999 and 2009 'because it cannot accidentally cause polio' (S2)", certainty: 1.0, cites: [{source: S1, locator: "body"}, {source: S2, locator: "The 'Killed-Virus' Principle; Field Trials; Live-Virus versus Killed-Virus Controversy"}], how_known: "Britannica and the Science History Institute. Range 1952–1955: work and its proof (P12, P29). The vaccine itself is an invention, which alone would not make him a scientist (P33); the result it rests on is listed separately as a discovery."}
    - {value: "Killed-virus principle: killed poliovirus of each of the three types, though incapable of producing the disease, induces antibody formation (shown in monkeys)", year: 1952, kind: discovery, lasting: "the basis of the first safe and effective polio vaccine (S1, S2)", certainty: 0.5, cites: [{source: S1, locator: "body, third paragraph ('He then demonstrated that killed virus of each of the three ... could induce antibody formation in monkeys')"}, {source: S2, locator: "The 'Killed-Virus' Principle"}], how_known: "Britannica and SHI. Britannica gives no year; dated with the vaccine's first human tests (1952), coder's call, inside the 1952–1955 range. A result about natural systems tested by experiment, so he is a scientist (P30, P33; batch T audit SA3)."}
  evidence_of_impact:
    - {value: "US polio cases fell from an average of more than 45,000 a year before the vaccine to 910 by 1962", kind: other, certainty: 0.7, cites: [{source: S3, locator: "1954–1955 paragraph"}], how_known: "Salk Institute page."}
    - {value: "Presidential Medal of Freedom, 1977", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "last paragraph"}], how_known: "Britannica."}
  major_works:
    - {value: "Man Unfolding", year: 1972, certainty: 0.7, cites: [{source: S6, locator: "About the Author"}, {source: S7, locator: "Selected publications"}], how_known: "Cited on the Survival of the Wisest jacket and Wikipedia; text not read this pass."}
    - {value: "The Survival of the Wisest", year: 1973, certainty: 1.0, cites: [{source: S6, locator: "title page / copyright 1973 Harper & Row"}], how_known: "Primary book read (OCR) this pass."}
    - {value: "Anatomy of Reality: Merging of Intuition and Reason", year: 1983, certainty: 0.7, cites: [{source: S7, locator: "Selected publications"}], how_known: "Wikipedia list; not read."}
  honours:
    - {value: "Presidential Medal of Freedom", year: 1977, certainty: 0.7, cites: [{source: S1, locator: "last paragraph"}], how_known: "Britannica."}
    - {value: "American Humanist Association Humanist of the Year", year: 1976, certainty: 0.7, cites: [{source: S7, locator: "Honors and recognition"}], how_known: "Wikipedia; SECHUM lead only — no humanist self-label read."}
  definition_fit: {value: "clearly meets", rationale: "(S1, S2).", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Jewish", certainty: 0.5, cites: [{source: S2, locator: "Salk's Education"}, {source: S7, locator: "Early life and education"}], how_known: "Same as religious_heritage_by_birth; immigrant Jewish parents (context only, P19)."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father: Daniel Salk, son of Jewish immigrants (S2); born in New Jersey to Jewish immigrant parents (S7)", certainty: 0.7, cites: [{source: S2, locator: "Salk's Education"}, {source: S7, locator: "Early life and education"}], how_known: "Wikipedia clarifies the father's generation; S3's 'Russian-Jewish immigrant' for the father is superseded at 0.7."}
    - {value: "Mother: Dora (née Press) Salk, born in Minsk; emigrated to the United States at age 12", certainty: 1.0, cites: [{source: S2, locator: "Salk's Education"}, {source: S7, locator: "Early life and education"}], how_known: "SHI and Wikipedia."}
  household_circumstances: {value: "Immigrant family; eldest of three sons; first in the family to attend college", certainty: 0.7, cites: [{source: S3, locator: "opening"}, {source: S7, locator: "Early life and education"}], how_known: "Salk Institute and Wikipedia."}
  schooling:
    - {value: "Townsend Harris Hall Prep School (public school for gifted students), entered at age 13", stage: "grammar or secondary school", run_by: "state or municipal", years: "c. 1927–c. 1929", certainty: 0.7, cites: [{source: S7, locator: "Early life and education"}], how_known: "Wikipedia (Oshinsky); years the coder's from age 13 and CCNY entry at 15."}
    - {value: "City College of New York, B.S. in chemistry 1934 (entered after high school at 15; Wikipedia) / degree in science 1933 (S2)", stage: university, run_by: "state or municipal", years: "c. 1929–1934", certainty: 0.5, cites: [{source: S2, locator: "Salk's Education"}, {source: S7, locator: "Education"}], how_known: "SHI says science 1933; Wikipedia says chemistry 1934. 0.5."}
    - {value: "New York University School of Medicine, M.D. 1939", stage: university, run_by: other, years: "1933–1939", certainty: 1.0, cites: [{source: S1, locator: "body"}, {source: S2, locator: "Salk's Education"}, {source: S7, locator: "Medical school"}], how_known: "Britannica, SHI and Wikipedia."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["English"], certainty: 0.5, cites: [{source: S3, locator: "opening"}], how_known: "Coder's reading (New York birth)."}
  notable_events:
    - {value: "Prayed to God as a child, then 'soon realized that I had to do something about it myself'; his mother's saying 'God helps those who help themselves'", certainty: 0.5, cites: [{source: S4, locator: "transcript, religion exchange (AAPB 00:28:53–00:29:57)"}], how_known: "(interview) His recollection in 1981."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1952–1955", certainty: 0.7, cites: [{source: S2, locator: "The 'Killed-Virus' Principle; Field Trials"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Religion 'serves a very important purpose'; 'my use of the term order is the same as the word God'; scientists 'perform the kinds of miracles' people pray for (1981); Survival of the Wisest: new means for 'inner self-regulation based upon naturalistic rather than on arbitrary moralistic formulations' (1973)", certainty: 0.5, cites: [{source: S4, locator: "transcript, religion exchange (AAPB 00:25:45–00:29:57); closing segment (AAPB 00:55:10–00:58:34)"}, {source: S6, locator: "pp. 122–123"}], how_known: "(interview + book) Both after the working years (P1 cap 0.5)."}
  primary_system:
    value: ATHE
    basis: written_profession
    certainty: 0.5
    cites: [{source: S4, locator: "transcript, religion exchange (AAPB 00:26:47–00:28:53); closing segment (AAPB 00:57:15–00:58:34)"}, {source: S6, locator: "p. 2 (purposeful Being / order)"}]
    rationale: "(interview + book) Ruling T2 stands. Interview: he gives the God=order equation to others and then withdraws the entity-term — 'God was invented because of the necessity for having a form of order'; what exists is order ('we are manifestations of the existence of order'); 'that's where God is' (in 'the miracle of life') fails the two-part PANT test. Survival of the Wisest (1973) agrees in writing: 'without arbitrary reference to a presumed purposeful Being, we cannot establish the reality of the illusion that everything in Nature has a preconceived or predesigned purpose' — the illusion 'arises, in part, from the order that prevails in the universe' (p. 2). Named alternative PANT: interview equation of God and order as 'the same phenomenon', with order as one whole. SECHUM lead (AHA Humanist of the Year 1976, S7) is not a self-label and does not displace ATHE."
    how_known: "(interview + book) Both after the working years (1952–1955), so 0.5 (P1). Independent source ids → corroborated (P48)."
    alternatives:
      - {value: PANT, note: "God and order 'the same phenomenon'; 'that's where God is'.", cites: [{source: S4, locator: "transcript, religion exchange (AAPB 00:26:47–00:27:49); closing segment (AAPB 00:57:15–00:58:34)"}]}
  secondary_system: {value: UNKNOWN, how_known: "One system (P29). SECHUM is a named lead from the AHA award (S7), not coded as secondary."}
  candidate_codes_considered:
    - {code: ATHE, reason: "'God was invented because of the necessity for having a form of order' (S4); rejection of a 'presumed purposeful Being' (S6 p. 2); chosen at 0.5 (ruling T2)."}
    - {code: PANT, reason: "God and order 'the same phenomenon'; God 'where' life and creation are; named alternative."}
    - {code: SECHUM, reason: "Rejected for primary: AHA Humanist of the Year 1976 (S7) is an award, not a self-label or public identity as the humanist movement."}
    - {code: JUDA, reason: "Heritage only (S2, S3, S7); never a code."}
  lio_axes:
    A_locus:
      value: 4
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S4, locator: "transcript, religion exchange (AAPB 00:25:45–00:29:57); closing segment (AAPB 00:55:10–00:58:34)"}, {source: S6, locator: "p. 2 (purposeful Being / order)"}]
      rationale: "(interview + book) Immanent / no-personal-God pole: interview locates what others call God in order and in life/man, against 'a God that is in the form of a person'; 'God was invented'. Book: no 'presumed purposeful Being'; the teleology illusion arises from 'the order that prevails in the universe' (p. 2). Named alternative BELOW_THRESHOLD: 'God was invented' / God-talk as figure of speech (ruling T2 / prior alt)."
      how_known: "(interview + book) Own words (P8); both after the working years, so 0.5 (P1). Independent source ids → corroborated (P48)."
      alternatives:
        - {value: BELOW_THRESHOLD, note: "God-talk as figure of speech / entity-term withdrawn.", cites: [{source: S4, locator: "transcript, religion exchange (AAPB 00:25:45–00:29:57)"}, {source: S6, locator: "p. 2"}]}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S4, locator: "transcript, religion exchange (AAPB 00:25:45–00:29:57)"}, {source: S6, locator: "p. 2; p. 32; p. 66; pp. 122–123"}]
      rationale: "(interview + book) Scored on his account of nature (P6, P16). Interview: 'it is the existence of order that is fundamental to our existence'; he affirms the interviewer's table/sun continuity. Survival of the Wisest: 'the order that prevails in the universe' (p. 2); 'The being acts according to the laws of Nature and, existing by virtue of these laws' (p. 32); 'It is unrealistic to believe that some Utopian human state could exist free from the operation of the laws of Nature' and equally unreal that Man can 'defy, or [act] counter to, the laws of Nature' (p. 66). No stated no-exception claim → B 3 at 0.5, alternative 4 (P16 addendum). P35 working-science floor no longer the sole basis, but P1 post-span cap and the missing no-exception clause keep certainty at 0.5 and value at 3. 'Miracles' of scientists / 'miracle of life' remain figures of speech."
      how_known: "(interview + book) Both after the working years (P1). Independent source ids → corroborated (P48). Working science (P35) still agrees as floor."
      alternatives:
        - {value: 4, note: "P16 addendum: a remark on lawful order / laws of Nature cannot rule out a no-exception nature.", cites: [{source: S6, locator: "p. 2; p. 66"}, {source: S4, locator: "transcript, religion exchange (AAPB 00:25:45–00:29:57)"}]}
    C_ledger: {value: UNKNOWN, how_known: "(interview + book) Nothing on reward and punishment of persons (P19). S6 p. 85 treats afterlife imagination as 'harmless faith' when it does not promise rewards for earthly deprivation — lead only, not a ledger claim."}
    D_authority:
      value: 4
      basis: written_profession
      certainty: 0.5
      support: single
      cites: [{source: S6, locator: "pp. 44–45; pp. 122–123"}]
      rationale: "(book) Observation/nature over revelation: founders of religions have formulated systems 'the product of imagination, without basis in \"reality\"'; poetic formulations have been 'regarded too literally' (pp. 44–45). 'New means are needed for inner self-regulation based upon naturalistic rather than on arbitrary moralistic formulations' (pp. 122–123). Religion keeps no domain of its own → D 4 (P27). After the working years, so 0.5 (P1). Named alternative BELOW_THRESHOLD: if the naturalistic/moralistic line is read as ethics-method only, not epistemic authority against revelation."
      how_known: "(book) Written profession after the span (P1). Interviewer's earlier quotation of the same line (S4) is not scored alone; the book supplies the own-voice text."
      alternatives:
        - {value: BELOW_THRESHOLD, note: "If naturalistic vs moralistic is ethics-method only, not D's revelation/observation contrast.", cites: [{source: S6, locator: "pp. 122–123"}]}
    E_scope: {value: BELOW_THRESHOLD, how_known: "(interview + book) 'we are manifestations of the existence of order' and Man as part of Nature / under the laws of Nature are leads that humans fall under the same order, not a statement that the same rules govern human choice (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "P4 test: A 4 at 0.5, below the 0.7 threshold the A ≥ 3 branch needs (Hawking, Watson, Shannon, Crick precedents). Corroboration fills the hollow ring but does not lift darkness."}
  statements:
    - text: "Now, to me, it is the existence of order that is fundamental to our existence, that we are manifestations of the existence of order."
      cites: [{source: S4, locator: "transcript, religion exchange (AAPB 00:26:47–00:27:49)"}]
      date: "1981-06-30"
      context: "Answering John Callaway's question on reverence for religion; he has just said religion 'is based upon a belief system ... in a certain way in which the world is put together'."
      axes: [B_cause, A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "AAPB transcript (status 'Correct'); broadcast date from the AAPB record."
    - text: "Now, some might say that my use of the term order is the same as the word God. We're both describing the same phenomenon. The difference between the idea of order and the idea of an anthropomorphic God. A God that is in the form of a person that thinks like a person and a personal God that looks after me personally and individually."
      cites: [{source: S4, locator: "transcript, religion exchange (AAPB 00:26:47–00:28:53)"}]
      date: "1981-06-30"
      context: "Same exchange, after Callaway's lines about the table and the sun."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Transcript line breaks joined."
    - text: "Well, that's why God was invented. You see God was invented because of the necessity for having a form of order."
      cites: [{source: S4, locator: "transcript, religion exchange (AAPB 00:27:49–00:28:53)"}]
      date: "1981-06-30"
      context: "Reply to Callaway's 'It's why they made a god out of you.'"
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Basis of the ATHE value (ruling T2) and of A's BELOW_THRESHOLD alternative."
    - text: "I'm very much aware of the miracle of life and very much aware of the miracle of man. And for me, that's where that's where God is. That's where creation exists now."
      cites: [{source: S4, locator: "transcript, closing segment (AAPB 00:57:15–00:58:34)"}]
      date: "1981-06-30"
      context: "Closing segment, on the Salk Institute's 'temple'-like architecture and scientists as 'the new priesthood'."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Repetition as transcribed."
    - text: "From an objective point of view and without arbitrary reference to a presumed purposeful Being, we cannot establish the reality of the illusion that everything in Nature has a preconceived or predesigned purpose, or project. This illusion arises, in part, from the order that prevails in the universe, and from the direction of evolution in the cosmos, with the emergence of Man, capable of perceiving and examining the process itself as we are trying to do."
      cites: [{source: S6, locator: "p. 2"}]
      date: "1973"
      context: "Opening chapter 'A Way to Perceive'; after discussing Man's relationship to Nature."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "OCR of 1973 Harper & Row; hyphenation rejoined; page number from running header sequence (ch. 1 opens at p. 1)."
    - text: "The being acts according to the laws of Nature and, existing by virtue of these laws, takes on a reality that is not easily dismissed even though its precise structure and chemistry cannot be defined."
      cites: [{source: S6, locator: "p. 32"}]
      date: "1973"
      context: "Chapter on biologic analogues of being and ego."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "OCR; hyphenation rejoined."
    - text: "It is unrealistic to believe that some Utopian human state could exist free from the operation of the laws of Nature. That Man can operate, collectively or individually, according to rules that defy, or are counter to, the laws of Nature is equally unreal."
      cites: [{source: S6, locator: "p. 66"}]
      date: "1973"
      context: "Chapter 'To Distinguish the Wholesome from the Sick'."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "OCR; hyphenation rejoined. Bracketed '[act]' not used — 'are counter to' as printed."
    - text: "The role of religious and political organizations has been to enlighten and to guide. Now new means are needed for inner self-regulation based upon naturalistic rather than on arbitrary moralistic formulations."
      cites: [{source: S6, locator: "pp. 122–123"}]
      date: "1973"
      context: "Closing chapter 'Wisdom a New Kind of Fitness'; the line Callaway later quotes in the 1981 interview."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "OCR; hyphenation rejoined. Supersedes scoring the interviewer's quotation alone."
  changes_over_life:
    - {value: "Childhood prayer gave way to self-reliance ('I had to do something about it myself')", certainty: 0.5, cites: [{source: S4, locator: "transcript, religion exchange (AAPB 00:28:53–00:29:57)"}], how_known: "(interview) His recollection; undated."}
  coder_notes: "Coder's call. Working years remain 1952–1955 (vaccine range); Survival of the Wisest (1973) and the 1981 interview are both after the span, so P1 caps every worldview score at 0.5 — no path to 0.7 without in-span own-voice or a lasting contribution that extends the span. Deepen corroborates A and B (hollow→filled) and scores D 4 @0.5 from the book. Man Unfolding (1972) and Anatomy of Reality (1983) remain unread leads. AHA Humanist of the Year 1976 is a SECHUM lead only."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Jewish (Russian-Jewish immigrant mother; father born in New Jersey to Jewish immigrant parents)", certainty: 0.7, cites: [{source: S2, locator: "Salk's Education"}, {source: S7, locator: "Early life and education"}], how_known: "Wikipedia clarifies the father's generation."}
  religious_heritage_by_birth: {value: "Jewish", certainty: 0.5, cites: [{source: S2, locator: "Salk's Education"}, {source: S7, locator: "Early life and education"}], how_known: "Inferred from Jewish immigrant parents; practice not stated."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1952–1955", certainty: 0.7, cites: [{source: S2, locator: "The 'Killed-Virus' Principle; Field Trials"}], how_known: "From the first human tests (1952) to the announced field-trial result (12 April 1955): one lasting contribution dated as a range (P12, P29, P30). Later AIDS-vaccine work was not a lasting contribution; biophilosophy books are not P30 science results."}
  age_at_first_lasting_contribution: {value: 38, certainty: 0.7, cites: [{source: S1, locator: "facts box"}, {source: S2, locator: "The 'Killed-Virus' Principle"}], how_known: "1952 − 1914 = 38 (P30); 37 or 38 depending on the month of the first tests."}
  first_evidence_of_lio_type_views: {value: "1973 (Survival of the Wisest): 'order that prevails in the universe' / no 'presumed purposeful Being' — A 4 / B 3", year: 1973, certainty: 0.5, cites: [{source: S6, locator: "p. 2"}], how_known: "(book) Earliest own-voice source read; after the span (P30 #7)."}
  lio_views_relative_to_major_work: {value: "after major work", certainty: 0.5, cites: [{source: S6, locator: "p. 2"}, {source: S4, locator: "transcript, closing segment (AAPB 00:55:10–00:58:34)"}], how_known: "(book + interview) First evidence read is 18–26 years after the span; no in-span worldview statement found."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "Salk's Education"}], how_known: "Not assessed."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "Salk's Education"}], how_known: "Not read."}
  circle_present: {value: "unclear", rationale: "God and order 'the same phenomenon' and humans 'manifestations' of order would suggest it, but only in a late interview, with 'God was invented' and the book's rejection of a 'purposeful Being' against it.", certainty: 0.5, cites: [{source: S4, locator: "transcript, religion exchange (AAPB 00:26:47–00:28:53); closing segment (AAPB 00:57:15–00:58:34)"}, {source: S6, locator: "p. 2"}], how_known: "(interview + book) Coder's reading."}
  reading: "Order / laws of Nature as the fundamental reality; God-talk as invented name for order or as reverent language for life; naturalistic self-regulation over arbitrary moralistic formulations; human self-reliance in place of prayer."
  notes: ""

institutions:
  - {value: "University of Pittsburgh School of Medicine (Virus Research Laboratory)", role: "associate professor of bacteriology and head of the laboratory, later professor", years: "1947–1963", kind: university, certainty: 0.7, cites: [{source: S1, locator: "body"}, {source: S2, locator: "The Virus Research Laboratory"}], how_known: "Britannica and SHI; end year the coder's."}
  - {value: "University of Michigan School of Public Health", role: "research fellow, later assistant professor of epidemiology", years: "1942–1947", kind: university, certainty: 0.7, cites: [{source: S1, locator: "body"}, {source: S3, locator: "1942 paragraph"}], how_known: "Britannica and the Salk Institute."}
  - {value: "National Foundation for Infantile Paralysis (March of Dimes)", role: "funded the polio work and the field trial", kind: "patron or funder", certainty: 0.7, cites: [{source: S2, locator: "The Virus Research Laboratory; Field Trials"}, {source: S3, locator: "1947 paragraph"}], how_known: "SHI and the Salk Institute."}
  - {value: "Salk Institute for Biological Studies", role: "founder, fellow and director", years: "1963–1995", kind: "research institute", certainty: 0.5, cites: [{source: S1, locator: "last paragraph"}, {source: S3, locator: "1963 paragraph"}], how_known: "Britannica and the Salk Institute say 1963; SHI says 1962. 0.5."}
collaborators:
  - {value: "Thomas Francis Jr.", relation: teacher, note: "mentor at NYU and Michigan; directed the 1954 field trial", certainty: 1.0, cites: [{source: S2, locator: "Salk's Education; Field Trials"}, {source: S3, locator: "1942 paragraph"}], how_known: "SHI and the Salk Institute."}
  - {value: "Albert Sabin", relation: "rival or critic", note: "live-virus oral vaccine; long dispute", certainty: 0.7, cites: [{source: S2, locator: "Live-Virus versus Killed-Virus Controversy"}], how_known: "SHI."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 112"}], how_known: "Study roster."}
  controversies:
    - {value: "Not awarded a Nobel Prize nor elected to the National Academy of Sciences; colleagues' animosity ('publicity hound')", certainty: 0.7, cites: [{source: S2, locator: "Later Research"}], how_known: "SHI."}
  data_quality_flags:
    - "All worldview evidence is post-span (1973 book; 1981 interview); P1 caps at 0.5."
    - "Survival of the Wisest read as unofficial PDF OCR, not a library print or IA borrow."
    - "Sources differ on CCNY degree year (1933/1934) and on the Salk Institute's founding year (1962/1963)."
  open_questions:
    - "Read Man Unfolding (1972) and Anatomy of Reality (1983) for further written statements on God and order."
    - "Any in-span (1952–1955) own-voice locus or nature-order remark that could lift past P1."
    - "Family religious practice."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors (revised by Kara Rogers)"
    citation: "Britannica Editors. \"Jonas Salk.\" Encyclopaedia Britannica (updated 10 September 2026). https://www.britannica.com/biography/Jonas-Salk. Read live 2026-10-19; dual-bio check 2026-10-24."
    url: "https://www.britannica.com/biography/Jonas-Salk"
    accessed: 2026-10-24
    reliability_note: "Unsigned body; facts box and body cited, the question boxes not."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, timing, institutions]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "Science History Institute"
    citation: "Science History Institute. \"Jonas Salk and Albert Bruce Sabin.\" Scientific Biographies. https://www.sciencehistory.org/education/scientific-biographies/jonas-salk/"
    url: "https://www.sciencehistory.org/education/scientific-biographies/jonas-salk/"
    accessed: 2026-10-19
    reliability_note: "Museum and library biography; unsigned."
    source_quality: other
    used_for: [basics, contribution, childhood, heritage, timing, institutions, collaborators, review]
  - id: S3
    type: secondary
    kind: "institutional page"
    author: "Salk Institute for Biological Studies"
    citation: "Salk Institute. \"About Jonas Salk.\" History of Salk. https://www.salk.edu/about/history-of-salk/jonas-salk/"
    url: "https://www.salk.edu/about/history-of-salk/jonas-salk/"
    accessed: 2026-10-19
    reliability_note: "The institute he founded; may be laudatory."
    source_quality: other
    used_for: [identity, basics, contribution, childhood, heritage, institutions, collaborators]
  - id: S4
    type: primary
    kind: other
    author: "Jonas Salk, with John Callaway"
    citation: "\"Jonas Salk.\" The John Callaway Interviews, WTTW (Chicago), broadcast 30 June 1981. American Archive of Public Broadcasting, cpb-aacip-526-g73707xt6p; transcript (AAPB status 'Correct')."
    url: "https://americanarchive.org/catalog/cpb-aacip-526-g73707xt6p"
    accessed: 2026-10-19
    reliability_note: "Archive transcript of a recorded broadcast interview; his own words count (P8), the interviewer's lines and quotations do not. After the working years (P1 cap 0.5)."
    source_quality: "primary / own words"
    used_for: [worldview, childhood, timing, lane_b]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Jonas Salk"
    citation: "Salk, Jonas. The Survival of the Wisest. New York: Harper & Row, 1973. Unofficial PDF OCR read 2026-10-24 (avalonlibrary.net copy of the Harper & Row printing); page numbers from the OCR running headers."
    url: "https://avalonlibrary.net/ebooks/Jonas%20Salk%20-%20The%20Survival%20of%20the%20Wisest.pdf"
    accessed: 2026-10-24
    reliability_note: "Own-voice book (P8 written profession); unofficial web OCR, not a library print or Internet Archive borrow (IA copy print-disabled). After the working years (P1 cap 0.5)."
    source_quality: "unofficial web copy"
    used_for: [worldview, contribution, timing, lane_b]
  - id: S7
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Jonas Salk.\" https://en.wikipedia.org/wiki/Jonas_Salk. Read live 2026-10-24 (dual bio with S1, P50)."
    url: "https://en.wikipedia.org/wiki/Jonas_Salk"
    accessed: 2026-10-24
    reliability_note: "Crowd-edited; used for dual bio, schooling (Townsend Harris), parents, AHA Humanist of the Year 1976, and selected publications. Worldview not coded from Wikipedia alone."
    source_quality: "reference entry"
    used_for: [identity, basics, childhood, heritage, contribution, review]
---

# Jonas Salk

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Jonas Salk (1914–1995), American physician and virologist who developed the first safe and effective polio vaccine [S1]. Deepen D1: primary_system ATHE (0.5, alt PANT; ruling T2); A 4 (0.5, corroborated S4+S6); B 3 (0.5, alt 4; corroborated S4+S6); D 4 (0.5, S6); mid_basin BELOW_THRESHOLD. Plotted (faded, now filled).

## Life and work

NYU, Michigan, Pittsburgh, the Salk Institute [S1, S2, S3, S7].

## Contribution and impact

The killed-virus polio vaccine, 1952–1955 [S2]. Later biophilosophy books include *The Survival of the Wisest* (1973) [S6].

## Childhood and education

Eldest son of Jewish immigrant parents in New York; Townsend Harris Hall, CCNY, NYU [S2, S3, S7].

## Adult working worldview

(Interview 1981 + *Survival of the Wisest* 1973, both after the 1952–1955 span; P1 caps at 0.5.) 'my use of the term order is the same as the word God' / 'God was invented' [S4]; 'without arbitrary reference to a presumed purposeful Being' / 'order that prevails in the universe' / cannot 'exist free from the operation of the laws of Nature' [S6].

## Heritage (context only)

Jewish [S2, S7].

## Timing

1952–1955, from age 38 [S2]. First LIO evidence read: 1973 [S6].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Order / laws of Nature as fundamental reality; God-talk as invented name or reverent language [S4, S6].

## Open questions

- *Man Unfolding* (1972) and *Anatomy of Reality* (1983).
- Any in-span (1952–1955) own-voice locus or nature-order remark.

## Research log

- 2026-10-19: Read Britannica, SHI, the Salk Institute page and the AAPB transcript.
- 2026-10-24: Deepen D1. Read *The Survival of the Wisest* (1973) unofficial PDF OCR; Wikipedia EN dual bio; P47 source_quality; A/B corroborated (hollow→filled); still faded under P1.
