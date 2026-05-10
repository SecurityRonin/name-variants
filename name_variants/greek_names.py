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

GREEK_NAME_VARIANTS: dict[str, dict] = {
    "Κωνσταντίνος": {
        "forms": ["konstantinos", "constantine", "costas", "kostas"],
    },
    "Γεώργιος": {
        "forms": ["georgios", "george", "giorgos", "georgis"],
    },
    "Χρήστος": {
        "forms": ["christos", "hristos", "chris"],
    },
    "Νικόλαος": {
        "forms": ["nikolaos", "nicholas", "nikos", "nikolas"],
    },
    "Δημήτριος": {
        "forms": ["dimitrios", "demetrius", "dimitris", "demitrios"],
    },
    "Ιωάννης": {
        "forms": ["ioannis", "john", "giannis", "yannis"],
    },
    "Ανδρέας": {
        "forms": ["andreas", "andrew", "andres"],
    },
    "Σταύρος": {
        "forms": ["stavros"],
    },
    "Αλέξανδρος": {
        "forms": ["alexandros", "alexander", "alex"],
    },
    "Παναγιώτης": {
        "forms": ["panagiotis", "panayiotis", "panos"],
    },
    "Αθανάσιος": {
        "forms": ["athanasios", "thanasis", "thanos", "nasios"],
    },
    "Βασίλειος": {
        "forms": ["vasileios", "vasilis", "vasily", "basil"],
    },
    "Ευάγγελος": {
        "forms": ["evangelos", "vangelis", "angelos"],
    },
    "Μιχαήλ": {
        "forms": ["michael", "michail", "mihail"],
    },
    "Θεόδωρος": {
        "forms": ["theodoros", "theodore"],
    },
    "Σπυρίδων": {
        "forms": ["spyridon", "spyros", "spiro"],
    },
    "Ελευθέριος": {
        "forms": ["eleftherios", "eleutherios", "lefteris"],
    },
    "Αντώνιος": {
        "forms": ["antonios", "antonis", "anthony"],
    },
    "Λάμπρος": {
        "forms": ["lambros"],
    },
    "Μάριος": {
        "forms": ["marios", "mario"],
    },
    "Πέτρος": {
        "forms": ["petros", "peter", "petro"],
    },
    "Θωμάς": {
        "forms": ["thomas", "tomas"],
    },
    "Νέστωρ": {
        "forms": ["nestor"],
    },
    "Αχιλλέας": {
        "forms": ["achilleas", "achilles"],
    },
    "Οδυσσέας": {
        "forms": ["odysseas", "odysseus", "ulysses"],
    },
    "Ηρακλής": {
        "forms": ["iraklís", "herakles", "hercules"],
    },
    "Αγαμέμνων": {
        "forms": ["agamemnon"],
    },
    "Αριστείδης": {
        "forms": ["aristeidis", "aristides"],
    },
    "Θεμιστοκλής": {
        "forms": ["themistocles", "themistoklis"],
    },
    "Μαρία": {
        "forms": ["maria", "mary"],
    },
    "Ελένη": {
        "forms": ["eleni", "helen", "elena"],
    },
    "Κατερίνα": {
        "forms": ["katerina", "catherine", "katrina"],
    },
    "Αναστασία": {
        "forms": ["anastasia", "natasha"],
    },
    "Σοφία": {
        "forms": ["sofia", "sophia"],
    },
    "Ειρήνη": {
        "forms": ["eirini", "irene", "irini"],
    },
    "Παρασκευή": {
        "forms": ["paraskevi", "voula"],
    },
    "Βασιλική": {
        "forms": ["vasiliki", "vicky"],
    },
    "Χριστίνα": {
        "forms": ["christina", "kristina"],
    },
    "Δήμητρα": {
        "forms": ["dimitra", "demeter"],
    },
    "Αθηνά": {
        "forms": ["athena", "athina"],
    },
    "Ολυμπία": {
        "forms": ["olympia"],
    },
    "Κλεοπάτρα": {
        "forms": ["kleopatra", "cleopatra"],
    },
    "Αφροδίτη": {
        "forms": ["afroditi", "aphrodite"],
    },
    "Αγγελική": {
        "forms": ["angeliki", "angelica"],
    },
    "Μαγδαληνή": {
        "forms": ["magdalini", "magdalene"],
    },
    "Φωτεινή": {
        "forms": ["foteini", "photini"],
    },
    "Ευθυμία": {
        "forms": ["efthimia", "euthimia"],
    },
    "Χαρίκλεια": {
        "forms": ["hariklia", "charikleia"],
    },
    "Κυριακή": {
        "forms": ["kyriaki", "kyria"],
    },
    "Παπαδόπουλος": {
        "forms": ["papadopoulos", "papadopulos"],
    },
    "Παπαδημητρίου": {
        "forms": ["papadimitriou"],
    },
    "Γεωργίου": {
        "forms": ["georgiou", "georgios"],
    },
    "Νικολάου": {
        "forms": ["nikolaou", "nikolaos"],
    },
    "Αντωνίου": {
        "forms": ["antoniou", "antonios"],
    },
    "Δημητρίου": {
        "forms": ["dimitriou", "demetriou"],
    },
    "Χριστοδούλου": {
        "forms": ["christodoulou"],
    },
    "Αναστασίου": {
        "forms": ["anastasiou"],
    },
    "Κωνσταντίνου": {
        "forms": ["konstantinou", "constantinou"],
    },
    "Σταυρίδης": {
        "forms": ["stavridis", "stavrides"],
    },
    "Καραγιάννης": {
        "forms": ["karagiannis", "caragiannis"],
    },
}
