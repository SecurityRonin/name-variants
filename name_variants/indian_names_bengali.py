"""
Indian names — Bengali lookup.
West Bengal, Bangladesh, and Bengali diaspora.

Romanization variant problem:
  Chatterjee / Chattopadhyay / Chattopadhyaya — same surname, three spellings
  Mukherjee / Mukhopadhyay / Mookherjee
  Banerjee / Bandyopadhyay / Bannerjee

The -jee/-ji/-ee endings are colonial anglicizations of -padhyay/-upadhyay.
Both forms appear in legal documents — often for the same person.

Sources:
  - ISO 15919 Bengali romanization
  - National Library at Kolkata romanization
  - Common UK/US/HK diaspora spellings
"""

INDIAN_NAMES_BENGALI: dict[str, list[str]] = {
    # ── Common Bengali surnames ─────────────────────────────────────────────
    "চট্টোপাধ্যায়": ["chattopadhyay", "chatterjee", "chattopadhyaya", "chatterji"],
    "মুখোপাধ্যায়": ["mukhopadhyay", "mukherjee", "mookherjee", "mukherji"],
    "বন্দ্যোপাধ্যায়": ["bandyopadhyay", "banerjee", "bannerjee", "banerji"],
    "ভট্টাচার্য": ["bhattacharya", "bhattacharyya", "bhattacherjee", "bhattacharjee"],
    "গঙ্গোপাধ্যায়": ["gangopadhyay", "ganguly", "ganguli"],
    "সেন": ["sen", "senne"],
    "বসু": ["basu", "bose", "bossu"],
    "দত্ত": ["datta", "dutt", "datt"],
    "ঘোষ": ["ghosh", "ghose", "gosh"],
    "মিত্র": ["mitra", "mitter", "mittra"],
    "রায়": ["ray", "roy", "rai"],
    "সরকার": ["sarkar", "sarcar"],
    "চক্রবর্তী": ["chakraborty", "chakravarti", "chakrabarti"],
    "দে": ["de", "dey", "day"],
    "দাস": ["das", "dass", "doss"],
    "পাল": ["pal", "paul"],
    "নন্দী": ["nandi", "nandy"],
    "মজুমদার": ["majumdar", "majumdaar", "majumder"],
    "বিশ্বাস": ["biswas", "bisvas", "biswaas"],
    "হালদার": ["halder", "haldar"],
    "রাহা": ["raha"],
    "সিংহ": ["sinha", "singha", "siha"],
    "চৌধুরী": ["choudhury", "chowdhury", "chaudhury", "chaudhari"],
    "নাগ": ["nag", "naag"],
    "চ্যাটার্জি": ["chaterjee"],
    # ── Common Bengali given name components ────────────────────────────────
    "সুভাষ": ["subhash", "subhas"],
    "প্রদীপ": ["pradeep", "pradip"],
    "সুকান্ত": ["sukanta", "sukant"],
    "অমিতাভ": ["amitabh", "amitabha"],
    "সৌমেন": ["soumen", "souman"],
    "দেবাশিস": ["debasish", "debashis"],
    "অনির্বাণ": ["anirban", "anirbaan"],
    "ঈশান": ["ishan", "ishaan", "eshan"],
    "রুদ্র": ["rudra", "rudro"],
    "শান্তনু": ["shantanu", "santanu"],
    "সোমনাথ": ["somnath"],
    "তপন": ["tapan"],
    "বিপ্লব": ["biplob", "biplav"],
    "পার্থ": ["partha", "partho"],
    "অর্ণব": ["arnab", "arnav"],
    "সৌরভ": ["sourav", "saurav"],
    "ঋত্বিক": ["ritwik", "ritwick"],
    "সায়নী": ["sayani", "saayani"],
    "মৌসুমী": ["mousumi", "moushumi", "mousomi"],
    "শর্মিলা": ["sharmila", "shormila"],
    "স্বাতী": ["swati", "swatee"],
    "রীতা": ["rita", "reeta"],
    "মিতা": ["mita", "meeta"],
    "চৈতালী": ["chaitali", "chaitaali"],
    "দেবযানী": ["debayani", "devayani"],
    "তৃষা": ["trisha", "tresha"],
    "পায়েল": ["payel", "payal"],
    "মধুমিতা": ["madhumita", "madhumitha"],
    "সুচিত্রা": ["suchitra", "sucheetra"],
    "অপর্ণা": ["aparna", "apurna"],
    "সুপ্রিয়া": ["supriya", "supria"],
}
