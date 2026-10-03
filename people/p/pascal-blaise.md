---
record:
  record_type: person
  schema_version: "1.2"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (executor agent for v8, RUNBOOK stage 3, batch A: early modern philosophers)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (stage 3, batch A). Basics from SEP 'Blaise Pascal' (Clarke) and Britannica (Jerphagnon, first page). Worldview from the Pensées (Gutenberg copy of the Dutton 1958 English edition, §7 cap 0.7) and the Préface sur le Traité du vide (Brunschvicg–Boutroux 1923 edition, Wikisource transcription checked against the Internet Archive scan of pp. 131–132). DRAFT SCORES for v8's review: primary_system CHRIST 0.7; A 0, B 2, C 1, D 2, E 1, all at 0.7; mid_basin TODO (A ≤ 1 with B = 2). Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit fixes, stage 3 batch A (two blind runs at 59a8371). #246: 'noblesse de robe' removed (not in the sources read). #236: D cites now fragments 269 and 278 only (273 was not used in the rationale). #250: value kept; the rationale now applies the written LIO definition and the open threshold is a method question for v8. Bylines: SEP now Clarke and Wood; Britannica now Jerphagnon and Orcibal. Pensées numbering note no longer says it follows Brunschvicg. Not reviewed."}

identity:
  id: pascal-blaise
  display_name: "Blaise Pascal"
  roster:
    canonical_name: "Blaise Pascal"
    rank: 14
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Blaise Pascal", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "opening"}], how_known: "Two sources."}
  native_name: {value: "Blaise Pascal", certainty: 1.0, cites: [{source: S2, locator: "opening"}], how_known: "French name as given."}
  aliases:
    - {name: "Blaise-Pascal", kind: "roster alias"}
    - {name: "Pascal-Blaise", kind: "roster alias"}

basics:
  birth:
    date: {value: "1623-06-19", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "opening"}], how_known: "Two sources agree."}
    place: {value: "Clermont (now Clermont-Ferrand)", modern_name: "Clermont-Ferrand, Puy-de-Dôme, France", polity_then: "Kingdom of France", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "opening"}], how_known: "Two sources agree."}
  death:
    date: {value: "1662-08-19", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "opening"}], how_known: "Two sources agree."}
    place: {value: "Paris", modern_name: "Paris, France", polity_then: "Kingdom of France", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "opening"}], how_known: "Two sources agree."}
  first_lasting_contribution_year: {value: 1640, certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "'Pascal’s life to the Port-Royal years'"}], how_known: "Essai pour les coniques (1640), on projective geometry; the coder's choice of first lasting contribution. The calculating machine (1642–1645) and the vacuum work (1647–1648) give the same era bucket."}
  era_bucket: {value: "1600 to 1749", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "From first_lasting_contribution_year (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "France is Western Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "§1 (Paris, Rouen, Clermont)"}], how_known: "Worked in Paris and Rouen."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "As the sources record it."}
  languages_of_work: {value: [French, Latin], certainty: 0.7, cites: [{source: S1, locator: "§1 (French titles)"}, {source: S2, locator: "'Pascal’s life to the Port-Royal years' (Latin title De Alea Geometriae)"}], how_known: "His main works have French titles; Britannica names a Latin treatise."}
  occupations: {value: [mathematician, physicist, "religious philosopher", writer], certainty: 1.0, cites: [{source: S2, locator: "opening"}, {source: S1, locator: "§1"}], how_known: "Britannica: 'French mathematician, physicist, religious philosopher, and master of prose'."}

contribution:
  fields: {value: [mathematics, physics, "theology and religious philosophy"], certainty: 1.0, cites: [{source: S2, locator: "opening"}, {source: S1, locator: "§1"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Foundations of the theory of probability, in correspondence with Fermat; Traité du triangle arithmétique", year: "1654", kind: theory, lasting: "probability theory", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "opening"}], how_known: "Two sources; SEP notes the work was published only after his death and recognised later."}
    - {value: "Pascal's principle of pressure; barometric experiments on the vacuum and the weight of the air, including the Puy-de-Dôme experiment carried out by Florin Périer on 19 September 1648", year: "1647–1648", kind: "law or principle", lasting: "hydrostatics; Pascal's principle", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "opening"}], how_known: "Two sources."}
    - {value: "Calculating machine (the Pascaline)", year: "1642–1645", kind: invention, lasting: "early mechanical calculator", certainty: 1.0, cites: [{source: S1, locator: "§1 (prototype 1645)"}, {source: S2, locator: "'Pascal’s life to the Port-Royal years' (1642–1644)"}], how_known: "Two sources; dates differ slightly."}
    - {value: "Essai pour les coniques, on projective geometry after Desargues", year: "1640", kind: work, lasting: "projective geometry (Pascal's theorem on conics)", certainty: 0.7, cites: [{source: S2, locator: "'Pascal’s life to the Port-Royal years'"}, {source: S1, locator: "§1"}], how_known: "Two sources for the essay; the name 'Pascal's theorem' is coder's knowledge, not in the sources read (flag)."}
  evidence_of_impact:
    - {value: "Pascal's principle of pressure named after him", kind: "named after them", certainty: 1.0, cites: [{source: S2, locator: "opening"}], how_known: "Britannica."}
    - {value: "His intuitionism influenced Rousseau, Bergson and the Existentialists", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Expériences nouvelles touchant le vide", year: 1647, kind: book, certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
    - {value: "Récit de la grande expérience de l'équilibre des liqueurs", year: 1648, kind: book, certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
    - {value: "Lettres provinciales (Provincial Letters)", year: "1656–1657", kind: book, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "'Pascal’s life to the Port-Royal years'"}], how_known: "SEP and Britannica."}
    - {value: "Pensées (posthumous notes)", year: 1670, kind: notebook, certainty: 1.0, cites: [{source: S1, locator: "opening; §1"}, {source: S3, locator: "Eliot introduction"}], how_known: "SEP: published posthumously in 1670 as a notebook of fragments."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Probability theory, Pascal's principle and the calculating machine.", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "opening"}], how_known: "Sources agree."}

childhood:
  family_religion: {value: "Roman Catholic", certainty: 1.0, cites: [{source: S2, locator: "'Pascal’s life to the Port-Royal years' ('Until 1646 the Pascal family held strictly Roman Catholic principles')"}, {source: S1, locator: "§1"}], how_known: "Britannica; SEP describes the family's turn to Jansenist practice in 1646."}
  family_religious_practice: {value: "Strictly Roman Catholic principles, though often substituting 'polite respectability' for inward religion, until the family's turn to Jansenist piety in 1646", certainty: 0.7, cites: [{source: S2, locator: "'Pascal’s life to the Port-Royal years'"}], how_known: "Britannica only."}
  parents_and_household:
    - {value: "Father, Étienne Pascal, presiding judge of the tax court at Clermont and an accomplished mathematician, who educated his children himself", name: "Étienne Pascal", role: father, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "'Pascal’s life to the Port-Royal years'"}], how_known: "Two sources."}
    - {value: "Mother died when he was three (1626)", role: mother, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "'Pascal’s life to the Port-Royal years'"}], how_known: "Two sources; her name is not given in the pages read."}
    - {value: "Sisters Gilberte (b. 1620) and Jacqueline (b. 1625)", role: siblings, certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  household_circumstances: {value: "Raised by his father with his two sisters; poor health from the age of two; the family moved to Paris in 1631 and to Rouen in 1639–1640", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "'Pascal’s life to the Port-Royal years'"}], how_known: "Two sources."}
  schooling:
    - {value: "Educated at home by his father only, first in classical languages and mathematics; never trained in theology or the philosophy of the schools", stage: home, years: "to c. 1640", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "'Pascal’s life to the Port-Royal years'"}], how_known: "SEP states it; Britannica agrees that Étienne devoted himself to his children's education."}
  early_mathematics: {value: "advanced mathematics", note: "Wrote the Essai pour les coniques at sixteen and was introduced to the Mersenne circle as a promising young mathematician.", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "'Pascal’s life to the Port-Royal years'"}], how_known: "Two sources."}
  early_geometric_style_reasoning: {value: "Home education focused on mathematics; projective geometry after Desargues by sixteen", certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "'Pascal’s life to the Port-Royal years'"}], how_known: "Two sources on the subjects; whether he learned Euclid-style proof as a child is not stated in the pages read."}
  early_science_exposure:
    - {value: "Introduced to the Mersenne circle by his father", year: "before 1640", age: "under 17", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  key_early_reading:
    - {value: "Desargues's work on projective geometry", certainty: 0.7, cites: [{source: S2, locator: "'Pascal’s life to the Port-Royal years'"}], how_known: "Britannica: the Essai was based on his study of Desargues."}
  childhood_mentors:
    - {value: "Étienne Pascal (father, sole teacher)", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  languages_in_childhood: {value: [French, Latin, Greek], certainty: 0.5, cites: [{source: S1, locator: "§1 ('classical languages')"}], how_known: "SEP says 'classical languages' without naming them; Latin and Greek are the coder's reading."}
  notable_events:
    - {value: "Mother's death", year: "1626", age: 3, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "'Pascal’s life to the Port-Royal years'"}], how_known: "Two sources."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1640–1662", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "From the Essai to his death."}
  nominal_affiliations:
    - {value: "Roman Catholic, Jansenist (Port-Royal)", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "'Pascal’s life to the Port-Royal years'"}], how_known: "SEP: his commitment to Jansenism was 'unqualified'; Britannica: he entered Port-Royal in January 1655."}
  self_described_science_religion_relation:
    value: "Two domains with separate rights: in theology authority is decisive because its principles are 'au dessus de la nature et de la raison', but in subjects 'qui tombent sous le sens ou sous le raisonnement' authority is useless and reason alone decides; 'Elles ont leurs droits separés' (Préface sur le Traité du vide). In religion, 'It is the heart which experiences God, and not the reason' (Pensées 278)."
    certainty: 0.7
    cites: [{source: S4, locator: "pp. 131–132"}, {source: S3, locator: "fragment 278"}]
    how_known: "His own texts. The Préface was checked against a scan of a scholarly edition, but the Pensées are posthumous notes read in an unofficial copy (§7), so 0.7."
  primary_system:
    value: CHRIST
    basis: consistent_private_letters
    certainty: 0.7
    cites: [{source: S3, locator: "fragments 555, 838"}, {source: S1, locator: "§1; §2"}]
    how_known: "His own notebook (the Pensées, posthumous, read in an unofficial copy, §7) consistent with the Provincial Letters as quoted by SEP; capped at 0.7 by §7 and by a named alternative."
    rationale: "DRAFT. A Catholic of Jansenist commitment: the Roman Catholic Church is the only true church, 'outside of which I am fully convinced there is no salvation' (Provincial Letters, quoted S1 §2), and his commitment to Jansenism 'was unqualified' (S1 §1). He rejects the God of reason: 'The God of Christians is not a God who is simply the author of mathematical truths' but 'the God of Abraham, the God of Isaac, the God of Jacob' (Pensées 555), and the metaphysical proofs 'make little impression' (542), so CLASS_THEISM, whose first use_when test is arguing to God by reason, does not fit; the same fragment says Christianity abhors deism. The CHRIST system file names him among modern defenders of faith. Named alternative: CLTHEI (popular interventionist God), since he affirms present-day miracles such as the Holy Thorn cure (838)."
  secondary_system: {value: UNKNOWN, how_known: "No second system in the sources read."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Coded (DRAFT, 0.7): Catholic Jansenist; no salvation outside the Church; God of Abraham, not of the philosophers. CHRIST is a sourced draft system file.", cites: [{source: S1, locator: "§2"}, {source: S3, locator: "fragment 555"}]}
    - {code: CLTHEI, reason: "Named alternative: present-day miracles for the Church (Pensées 838–839). Not coded: his writing is confessional Catholic theology, not a generic interventionist theism.", cites: [{source: S3, locator: "fragments 838, 839"}]}
    - {code: CLASS_THEISM, reason: "Rejected: he denies that metaphysical proofs bring men to God (Pensées 542; S1 §2, 'The metaphysical proofs … have little value').", cites: [{source: S3, locator: "fragment 542"}, {source: S1, locator: "§2"}]}
    - {code: DEISM, reason: "Rejected in his own words: 'atheism, or [...] deism, two things which the Christian religion abhors almost equally' (Pensées 555).", cites: [{source: S3, locator: "fragment 555"}]}
  lio_axes:
    A_locus:
      value: 0
      basis: consistent_private_letters
      certainty: 0.7
      cites: [{source: S3, locator: "fragment 555"}]
      how_known: "His own notebook in an unofficial copy (§7); a named alternative (1)."
      rationale: "DRAFT. At the transcendent-person pole: the God of Christians is 'the God of Abraham, the God of Isaac, the God of Jacob [...] a God of love and of comfort, a God who fills the soul and heart of those whom He possesses' (Pensées 555), explicitly not 'simply the author of mathematical truths, or of the order of the elements'. No immanence-in-nature feature like the one that gave Aquinas and Newton 1 in what was read. Named alternative: 1 (God present in the soul of those he possesses)."
    B_cause:
      value: 2
      basis: consistent_private_letters
      certainty: 0.7
      cites: [{source: S3, locator: "fragments 803, 804, 838"}, {source: S1, locator: "§1; §4"}]
      how_known: "His own notebook (§7) and SEP; two named alternatives (1 and 3)."
      rationale: "DRAFT, judgment call. Scored on his account of nature (P6). His physics is lawful and experimental: in matters of sense and reasoning authority is useless (S4, p. 132), and observations would settle whether the earth moves whatever Rome decreed (Provincial Letters, quoted S1 §4). But present-day miracles in nature are real and central: a miracle is 'an effect, which exceeds the natural power of the means which are employed for it' (803); 'grace and miracles; both supernatural' (804); and at Port-Royal 'God Himself chooses this house in order to display conspiciously therein His power' (838; the Holy Thorn cure of his niece, 1656, translator's note). SEP: he 'believed uncritically that God performs miracles' (S1 §1). Lawful nature with live, frequent exceptions, so 2. Named alternatives: 3 (Aquinas pattern, lawful nature with accepted miracles) and 1 (the CHRIST system score)."
    C_ledger:
      value: 1
      basis: consistent_private_letters
      certainty: 0.7
      cites: [{source: S1, locator: "§2; §6"}, {source: S2, locator: "'Pascal’s life to the Port-Royal years'"}]
      how_known: "His own words as quoted by SEP (Provincial Letters) and SEP's account of his Jansenism; a named alternative (0)."
      rationale: "DRAFT. Leans to the personal pole: salvation or its absence is personal and eternal, and there is 'no salvation' outside the Roman Church (Provincial Letters, quoted S1 §2). Limited by its form: in his Jansenism grace, not good works, is the key to salvation (S2), and faith is given 'without any merit on the part of the recipient' (S1 §6), so it is not a ledger of deeds. Same reading as the CHRIST system file (1). Named alternative: 0."
    D_authority:
      value: 2
      basis: consistent_private_letters
      certainty: 0.7
      cites: [{source: S4, locator: "pp. 131–132"}, {source: S3, locator: "fragments 269, 278"}, {source: S1, locator: "§4"}]
      how_known: "Préface checked against a scan of the 1923 edition; it is a draft published after his death, read with the Pensées (§7) and SEP; a named alternative (1)."
      rationale: "DRAFT. Two domains, each with its own authority, so D 2 (same-pattern rule). In theology authority 'a la principale force [...] parce qu’elle y est inseparable de la verité'; in subjects of sense and reasoning 'l’authorité y est inutile ; la raison seule a lieu d’en connoistre. Elles ont leurs droits separés' (Préface, pp. 131–132). Named alternative: 1, because in religion reason must submit ('Submission is the use of reason in which consists true Christianity', Pensées 269) and the heart, not reason, knows God (278)."
    E_scope:
      value: 1
      basis: consistent_private_letters
      certainty: 0.7
      cites: [{source: S3, locator: "fragments 838, 839"}]
      how_known: "His own notebook in an unofficial copy (§7); a named alternative (2)."
      rationale: "DRAFT. Scored on the world's order (P7). Leans exception: God acts in particular events for a particular community. God 'chooses this house' (Port-Royal) for 'miraculous alleviations' (838), and 'the Church has always had miracles against' its enemies (839). Same reading as the CHRIST system file (E 1). Salvation only in the Church is a C matter (P7). Named alternative: 2, since his physical treatises treat nature as uniform."
  mid_basin: {value: TODO, how_known: "A_locus = 0 at 0.7 and B_cause = 2 at 0.7. A ≤ 1 but B = 2 falls between the branches of the P4 test (CODING_GUIDE §6).", note: "Needs a decision on B (2, or the named alternatives 3 and 1), not more evidence. B 3 would make it true; B 1 would make it false."}
  statements:
    - text: "The God of Christians is not a God who is simply the author of mathematical truths, or of the order of the elements; that is the view of heathens and Epicureans. He is not merely a God who exercises His providence over the life and fortunes of men, to bestow on those who worship Him a long and happy life. That was the portion of the Jews. But the God of Abraham, the God of Isaac, the God of Jacob, the God of Christians, is a God of love and of comfort, a God who fills the soul and heart of those whom He possesses"
      cites: [{source: S3, locator: "fragment 555"}]
      date: "1670"
      context: "Pensées, posthumous notes for an apology, first published 1670 (S1, opening); written in the Port-Royal years (S2), not a dated manuscript."
      axes: [A_locus]
      kind: "notebook or diary"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "Thereby they fall either into atheism, or into deism, two things which the Christian religion abhors almost equally."
      cites: [{source: S3, locator: "fragment 555"}]
      date: "1670"
      context: "Same fragment, on those who seek God without Christ the mediator."
      axes: [A_locus]
      kind: "notebook or diary"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "It is the heart which experiences God, and not the reason. This, then, is faith: God felt by the heart, not by the reason."
      cites: [{source: S3, locator: "fragment 278"}]
      date: "1670"
      context: "Pensées; follows 277, 'The heart has its reasons, which reason does not know.'"
      axes: [D_authority]
      kind: "notebook or diary"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "Submission is the use of reason in which consists true Christianity."
      cites: [{source: S3, locator: "fragment 269"}]
      date: "1670"
      context: "Pensées, on the place of reason in faith."
      axes: [D_authority]
      kind: "notebook or diary"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "It is an effect, which exceeds the natural power of the means which are employed for it; and what is not a miracle is an effect, which does not exceed the natural power of the means which are employed for it."
      cites: [{source: S3, locator: "fragment 803"}]
      date: "1670"
      context: "Pensées, section on miracles: definition of a miracle."
      axes: [B_cause]
      kind: "notebook or diary"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "Now God Himself chooses this house in order to display conspiciously therein His power."
      cites: [{source: S3, locator: "fragment 838 (Dutton ed. p. 247, per translator's note 333)"}]
      date: "1670"
      context: "Pensées, on the Holy Thorn at Port-Royal; translator's note 333: his niece Marguerite Périer was cured on 24 March 1656. Spelling 'conspiciously' as in the copy."
      axes: [B_cause, E_scope]
      kind: "notebook or diary"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "Il n’en est pas de mesme des subjets qui tombent sous le sens ou sous le raisonnement : l’authorité y est inutile ; la raison seule a lieu d’en connoistre. Elles ont leurs droits separés : l’une avoit tantost tout l’advantage ; ici l’autre regne à son tour."
      cites: [{source: S4, locator: "pp. 131–132"}]
      context: "Fragment de préface sur le Traité du vide, after the passage on theology; unpublished in his lifetime and undated here (the edition's volume covers 1647–1651; date not checked further, flag). Editor's footnote marker after 'connoistre' omitted."
      axes: [D_authority, B_cause]
      kind: "other"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
  changes_over_life:
    - {value: "Turn to Jansenist piety in 1646 (via the Deschamps brothers) and the conversion of the night of 23 November 1654 (the Memorial); after 1654 he left mathematics and the vacuum booklet aside for religious writing", year: "1646; 1654", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "'Pascal’s life to the Port-Royal years'"}], how_known: "Two sources."}
  coder_notes: "DRAFT SCORES for v8's review. The Pensées are posthumous notes (S1 §1: 'reliably attributed to Pascal only when he expressed similar views elsewhere'), so the basis used is consistent_private_letters (notebooks), not written_profession; see report method question. The Gutenberg Pensées uses its own numbering (not checked against Brunschvicg's order; lens audit run 2); the numbers given are those printed in that copy, not Lafuma or Sellier numbers. The Provincial Letters were not opened; their words are SEP quotations. The Préface quotation is the only one checked against page images (Internet Archive scan of the 1923 Brunschvicg–Boutroux edition)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "French; family of a provincial royal tax official", certainty: 0.7, cites: [{source: S2, locator: "'Pascal’s life to the Port-Royal years'"}, {source: S1, locator: "§1"}], how_known: "Father's office from both sources. The coder's label 'noblesse de robe' was removed: it is not in the sources read, and a value needs a cited source (lens audit #246)."}
  religious_heritage_by_birth: {value: "Roman Catholic", certainty: 1.0, cites: [{source: S2, locator: "'Pascal’s life to the Port-Royal years'"}], how_known: "Britannica."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1640–1662", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "Essai (1640) to the Pensées notes at his death."}
  age_at_first_lasting_contribution: {value: 16, certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "'Pascal’s life to the Port-Royal years'"}], how_known: "Born June 1623; Essai 1640, so 16 or 17 depending on the month (not stated)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "Checked SEP §1–§4, Britannica's first page and the Pensées read: no LIO-type God-world view found; his lawful physics is paired with a transcendent, miracle-working God."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "DATA_DICTIONARY defines lawful-order views as 'law without exemption'. His physics is lawful and reason alone rules in matters of sense and reasoning (S4, p. 132), but he holds that miracles continue in nature (B 2; fragments 803, 838) and that a personal God acts in particular events (A 0, E 1; fragments 555, 838), so no law-without-exemption view was found. The lens audit (#250, one run) proposed 'unclear'; the value is left pending a written threshold for 'LIO-type views' (method question).", certainty: 0.7, cites: [{source: S3, locator: "fragments 555, 803, 838"}, {source: S4, locator: "p. 132"}], how_known: "Coder's reading of the texts read, against the DATA_DICTIONARY definition."}
  worldview_during_major_work: {value: "Catholic throughout; Jansenist from 1646; intensified after 1654", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "'Pascal’s life to the Port-Royal years'"}], how_known: "Two sources."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "A geometer by training and in method for physics (S4), but he holds that the heart, not geometrical reasoning, knows God (Pensées 277–278).", certainty: 0.5, cites: [{source: S3, locator: "fragments 277, 278"}, {source: S1, locator: "§1; §4"}], how_known: "Coder's reading."}
  form_acquired: {value: "childhood or adolescence", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "Mathematics at home from his father; the Essai at sixteen."}
  circle_present: {value: "no", rationale: "God is the God of Abraham, not the author of the order of the elements (Pensées 555).", certainty: 0.7, cites: [{source: S3, locator: "fragment 555"}], how_known: "His own words in an unofficial copy."}
  reading: "As belief, not finding: early mathematical form present, circle absent, and he explicitly separates geometric reason from knowledge of God. A case against reading form as sufficient for the circle."
  notes: ""

institutions:
  - {value: "Port-Royal (Jansenist convent and community)", role: "associate; entered January 1655 without becoming one of the solitaires", years: "1655–1662", kind: "religious body", certainty: 1.0, cites: [{source: S2, locator: "'Pascal’s life to the Port-Royal years'"}, {source: S1, locator: "§1"}], how_known: "Two sources."}
  - {value: "Mersenne circle (Paris)", role: "young member, introduced by his father", years: "before 1640", kind: "academy or learned society", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
collaborators:
  - {value: "Pierre de Fermat", roster_id: de-fermat-pierre, relation: correspondent, note: "1654 correspondence on probabilities in games of chance", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "opening"}], how_known: "SEP names the correspondence; Britannica credits him with founding probability."}
  - {value: "Florin Périer", relation: family, note: "brother-in-law; carried out the Puy-de-Dôme experiment, 19 September 1648", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  - {value: "Antoine Arnauld", relation: collaborator, note: "Pascal defended him in the Provincial Letters", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  - {value: "René Descartes", roster_id: descartes-rene, relation: other, note: "met him in Paris in September 1647 to discuss the expected barometer results", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}

review:
  roster_status_reason: {value: "Core in v8 (F 5: all five models).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 14"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Calculating machine: 1642–1644 (Britannica) vs prototype 1645 (SEP)."
    - "Pensées read only in a Gutenberg copy of an English translation with its own numbering; no Lafuma or Sellier concordance checked."
    - "Britannica read as its first page only."
  open_questions:
    - "Check the Pensées quotations against Lafuma or Sellier and give those numbers; that would lift the §7 cap."
    - "Read the Provincial Letters directly (I, 781 and I, 813 in Le Guern's edition, per SEP)."
    - "Decide B (2 vs 3 vs 1), which decides mid_basin."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Desmond Clarke and William Wood"
    year: 2015
    citation: "Clarke, Desmond, and William Wood. \"Blaise Pascal.\" Stanford Encyclopedia of Philosophy (substantive revision 22 Jun 2015). https://plato.stanford.edu/entries/pascal/."
    url: "https://plato.stanford.edu/entries/pascal/"
    accessed: 2026-10-02
    reliability_note: "Scholarly reference work; read in full. Cited by section. Its quotations of the Provincial Letters are secondary quotations (Le Guern's edition, volume and page)."
    used_for: [identity, basics, contribution, childhood, worldview, timing, lane_b, institutions, collaborators]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Lucien Jerphagnon and Jean Orcibal"
    citation: "Jerphagnon, Lucien, and Jean Orcibal. \"Blaise Pascal.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Blaise-Pascal."
    url: "https://www.britannica.com/biography/Blaise-Pascal"
    accessed: 2026-10-02
    reliability_note: "Signed article; first page only. Cited by section heading."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Blaise Pascal"
    year: 1670
    citation: "Pascal, Blaise. Pascal's Pensées. Introduction by T. S. Eliot. New York: E. P. Dutton, 1958 (Dutton Paperback). Project Gutenberg eBook 18269, https://www.gutenberg.org/ebooks/18269."
    url: "https://www.gutenberg.org/ebooks/18269"
    accessed: 2026-10-02
    reliability_note: "Unofficial web copy of an English translation (translator not named in the eBook text); capped at 0.7 under CODING_GUIDE §7. Cited by the fragment numbers printed in this copy (the eBook says only that its notes are 'mainly based on those of M. Brunschvicg'; whether its numbering follows Brunschvicg's order was not checked); no page numbers except one taken from the translator's notes."
    used_for: [contribution, worldview, timing, lane_b]
  - id: S4
    type: primary
    kind: "scholarly edition"
    author: "Blaise Pascal"
    year: 1923
    citation: "Pascal, Blaise. \"Fragment de préface sur le Traité du vide.\" In Œuvres de Blaise Pascal, ed. Léon Brunschvicg and Pierre Boutroux, 2nd ed., vol. II (1647–1651), pp. 127–145. Paris: Hachette, 1923. Wikisource transcription https://fr.wikisource.org/wiki/Œuvres_de_Blaise_Pascal/Fragment_de_préface_sur_le_Traité_du_vide; scan https://archive.org/details/uvresdeblaisepas02pasc."
    url: "https://fr.wikisource.org/wiki/%C5%92uvres_de_Blaise_Pascal/Fragment_de_pr%C3%A9face_sur_le_Trait%C3%A9_du_vide"
    accessed: 2026-10-02
    reliability_note: "Wikisource transcription; the quoted passage was checked against the page images of pp. 131–132 (Commons file 'Œuvres de Blaise Pascal, II.djvu', from the Internet Archive scan), so the page numbers are the printed ones."
    used_for: [worldview]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# Blaise Pascal

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Blaise Pascal (1623–1662), French mathematician, physicist and religious writer, laid the foundations of probability theory with Fermat, formulated Pascal's principle of pressure and built a calculating machine [S1, §1; S2]. A Catholic of unqualified Jansenist commitment, he wrote that the God of Christians is "the God of Abraham", not "simply the author of mathematical truths" [S3, 555]. Draft code CHRIST at 0.7. Axes A 0, B 2, C 1, D 2, E 1, all at 0.7; mid_basin TODO (B = 2).

## Life and work

Educated only by his father, he wrote the Essai pour les coniques in 1640, built the calculating machine, ran the vacuum experiments of 1647–1648, turned to Jansenism in 1646, had the conversion of 23 November 1654, wrote the Provincial Letters (1656–1657) and left the notes published as the Pensées [S1, §1; S2].

## Contribution and impact

Probability (with Fermat), hydrostatics, the Pascaline and projective geometry [S1; S2].

## Childhood and education

His mother died when he was three; his father, a tax judge and mathematician, educated him at home in classical languages and mathematics [S1, §1; S2].

## Adult working worldview

Theology rests on authority and sense-and-reason subjects on reason alone: "Elles ont leurs droits separés" [S4, p. 132]. God is known by the heart [S3, 278]; miracles continue, as at Port-Royal [S3, 838].

## Heritage (context only)

French Catholic family of a royal tax official [S1; S2]. Context only.

## Timing

First lasting contribution taken as the Essai of 1640, at 16 [S1; S2]. No LIO-type views found.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form present early; circle absent [S3, 555].

## Open questions

- Check the Pensées against Lafuma or Sellier; read the Provincial Letters directly.
- Decide B, which decides mid_basin.

## Research log

- 2026-10-02: Read SEP "Blaise Pascal" (Clarke, full), Britannica (Jerphagnon, first page), the Pensées (Gutenberg 18269) and the Wikisource Préface (Brunschvicg–Boutroux 1923), and viewed the scan of pp. 131–132. Wikipedia not used.
- 2026-10-02 (lens audit fixes): Re-checked the SEP and Britannica bylines and the Gutenberg Pensées note on Brunschvicg; no new sources.
