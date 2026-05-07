"""
Greek name lookup: Greek script → romanization variants.

Key problem: Greek has classical English cognates (different from modern pronunciation),
ISO 843 romanization, BGN/PCGN, and informal transliterations.
  Κωνσταντίνος → Konstantinos (ISO) / Constantine (classical English) / Costas (informal)
  Γεώργιος → Georgios (ISO) / George (English) / Giorgos (informal)
  Χρήστος → Christos (common) / Hristos (ISO)

Sources:
  - ISO 843 Greek romanization
  - BGN/PCGN 1962 system
  - Classical English name cognates
  - Common Greek diaspora (Australia/UK/US/HK) spellings
"""

GREEK_NAME_VARIANTS: dict[str, list[str]] = {
    # ── Male given names ─────────────────────────────────────────────────────
    "Κωνσταντίνος": ["konstantinos", "constantine", "costas", "kostas"],
    "Γεώργιος": ["georgios", "george", "giorgos", "georgis"],
    "Χρήστος": ["christos", "hristos", "chris"],
    "Νικόλαος": ["nikolaos", "nicholas", "nikos", "nikolas"],
    "Δημήτριος": ["dimitrios", "demetrius", "dimitris", "demitrios"],
    "Ιωάννης": ["ioannis", "john", "giannis", "yannis"],
    "Ανδρέας": ["andreas", "andrew", "andres"],
    "Σταύρος": ["stavros"],
    "Αλέξανδρος": ["alexandros", "alexander", "alex"],
    "Παναγιώτης": ["panagiotis", "panayiotis", "panos"],
    "Αθανάσιος": ["athanasios", "thanasis", "thanos", "nasios"],
    "Βασίλειος": ["vasileios", "vasilis", "vasily", "basil"],
    "Ευάγγελος": ["evangelos", "vangelis", "angelos"],
    "Μιχαήλ": ["michael", "michail", "mihail"],
    "Θεόδωρος": ["theodoros", "theodore"],
    "Σπυρίδων": ["spyridon", "spyros", "spiro"],
    "Ελευθέριος": ["eleftherios", "eleutherios", "lefteris"],
    "Αντώνιος": ["antonios", "antonis", "anthony"],
    "Λάμπρος": ["lambros"],
    "Μάριος": ["marios", "mario"],
    "Πέτρος": ["petros", "peter", "petro"],
    "Θωμάς": ["thomas", "tomas"],
    "Νέστωρ": ["nestor"],
    "Αχιλλέας": ["achilleas", "achilles"],
    "Οδυσσέας": ["odysseas", "odysseus", "ulysses"],
    "Ηρακλής": ["iraklís", "herakles", "hercules"],
    "Αγαμέμνων": ["agamemnon"],
    "Αριστείδης": ["aristeidis", "aristides"],
    "Θεμιστοκλής": ["themistocles", "themistoklis"],
    # ── Female given names ────────────────────────────────────────────────────
    "Μαρία": ["maria", "mary"],
    "Ελένη": ["eleni", "helen", "elena"],
    "Κατερίνα": ["katerina", "catherine", "katrina"],
    "Αναστασία": ["anastasia", "natasha"],
    "Σοφία": ["sofia", "sophia"],
    "Ειρήνη": ["eirini", "irene", "irini"],
    "Παρασκευή": ["paraskevi", "voula"],
    "Βασιλική": ["vasiliki", "vicky"],
    "Χριστίνα": ["christina", "kristina"],
    "Δήμητρα": ["dimitra", "demeter"],
    "Αθηνά": ["athena", "athina"],
    "Ολυμπία": ["olympia"],
    "Κλεοπάτρα": ["kleopatra", "cleopatra"],
    "Αφροδίτη": ["afroditi", "aphrodite"],
    "Αγγελική": ["angeliki", "angelica"],
    "Μαγδαληνή": ["magdalini", "magdalene"],
    "Φωτεινή": ["foteini", "photini"],
    "Ευθυμία": ["efthimia", "euthimia"],
    "Χαρίκλεια": ["hariklia", "charikleia"],
    "Κυριακή": ["kyriaki", "kyria"],
    # ── Common Greek surnames ─────────────────────────────────────────────────
    "Παπαδόπουλος": ["papadopoulos", "papadopulos"],
    "Παπαδημητρίου": ["papadimitriou"],
    "Γεωργίου": ["georgiou", "georgios"],
    "Νικολάου": ["nikolaou", "nikolaos"],
    "Αντωνίου": ["antoniou", "antonios"],
    "Δημητρίου": ["dimitriou", "demetriou"],
    "Χριστοδούλου": ["christodoulou"],
    "Αναστασίου": ["anastasiou"],
    "Κωνσταντίνου": ["konstantinou", "constantinou"],
    "Σταυρίδης": ["stavridis", "stavrides"],
    "Καραγιάννης": ["karagiannis", "caragiannis"],
}
