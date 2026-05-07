"""
Indian names — Hindi/North Indian/Sanskrit lookup.
Covers surnames and common given name components from Hindi-speaking regions.

Romanization variant problem: no official standard adopted for everyday use.
IAST (academic), Harvard-Kyoto, and colloquial all produce different spellings.
  Sharma → Sarma (Bengali variant)
  Singh → Sing (simplified)
  Mishra → Misra / Mishra / Mitra
  Srivastava → Shrivastava / Shrivastav / Srivastav

Sources:
  - Census of India surname frequency data
  - IAST transliteration standard
  - Common colloquial/diaspora spellings (UK/US/HK)
"""

INDIAN_NAMES_HINDI: dict[str, list[str]] = {
    # ── Common surnames ──────────────────────────────────────────────────────
    "शर्मा": ["sharma", "sarma", "sherma"],
    "सिंह": ["singh", "sing"],
    "वर्मा": ["varma", "verma", "varman"],
    "मिश्रा": ["mishra", "misra", "mitra"],
    "श्रीवास्तव": ["srivastava", "shrivastava", "srivastav", "shrivastav"],
    "पाठक": ["pathak", "patak"],
    "तिवारी": ["tiwari", "tivari", "tewari"],
    "पांडे": ["pandey", "pande", "panday"],
    "दुबे": ["dubey", "dube", "dubé"],
    "यादव": ["yadav", "yadaw"],
    "गुप्ता": ["gupta"],
    "जोशी": ["joshi", "josi"],
    "अग्रवाल": ["agrawal", "agarwal"],
    "चौधरी": ["chaudhary", "chaudhury", "choudhary", "choudhury", "chowdhury"],
    "राय": ["rai", "ray", "roi"],
    "कुमार": ["kumar", "koomar"],
    "खान": ["khan", "kahn"],
    "श्रीवास्तव": ["srivastava", "shrivastava"],
    "त्रिपाठी": ["tripathi", "tripati"],
    "दीक्षित": ["dixit", "dikshit", "dikshita"],
    "अवस्थी": ["awasthi", "avasthi"],
    "सक्सेना": ["saxena", "saksena"],
    "भार्गव": ["bhargava", "bhargav"],
    "श्रीवास्तव": ["srivastava"],
    "बाजपेई": ["bajpai", "bajpei", "bajpeyi"],
    # ── Common given name components ─────────────────────────────────────────
    "राम": ["ram", "raam"],
    "कृष्ण": ["krishna", "krishn", "krushna"],
    "विष्णु": ["vishnu", "bisnu"],
    "शिव": ["shiv", "shiva", "siva"],
    "देव": ["dev", "deb"],
    "प्रकाश": ["prakash", "prakasam"],
    "मोहन": ["mohan", "mohen"],
    "लाल": ["lal", "laal"],
    "चंद": ["chand", "chandra"],
    "नाथ": ["nath", "natha"],
    "दास": ["das", "doss", "dass"],
    "प्रसाद": ["prasad", "prasada"],
    "नारायण": ["narayan", "narayana"],
    "बाबू": ["babu", "baboo"],
    "सुब्रमण्यम": ["subramaniam", "subramanian", "subramanyam", "subrahmanyam"],
    "रमेश": ["ramesh"],
    "सुरेश": ["suresh", "sooresh"],
    "महेश": ["mahesh"],
    "राजेश": ["rajesh"],
    "दिनेश": ["dinesh"],
    "नरेश": ["naresh", "narresh"],
    "अनिल": ["anil", "aneel"],
    "सुनील": ["sunil", "suneel"],
    "विनोद": ["vinod", "binod"],
    "अरविंद": ["arvind", "aravind", "arvinda"],
    "विजय": ["vijay", "bijay"],
    "अजय": ["ajay"],
    "संजय": ["sanjay"],
    "विजय": ["vijay", "bijay"],
    "रवि": ["ravi", "rabi"],
    "अमित": ["amit", "ameet"],
    "पवन": ["pawan", "pavan"],
    "ललित": ["lalit", "laleet"],
    "आनंद": ["anand", "ananda"],
    "संदीप": ["sandeep", "sandip"],
    "अभिषेक": ["abhishek", "abhisheck"],
    "मनोज": ["manoj", "manodj"],
    "प्रीति": ["preeti", "priti", "preety"],
    "नीता": ["neeta", "nita", "neita"],
    "सीता": ["sita", "seeta"],
    "गीता": ["gita", "geeta"],
    "सुनीता": ["sunita", "suneeta"],
    "रेखा": ["rekha"],
    "ममता": ["mamta", "mamata"],
    "सविता": ["savita", "savitta"],
    "रीता": ["rita", "reeta"],
    "लता": ["lata", "laata"],
    "पूजा": ["pooja", "puja"],
    "दीपा": ["deepa", "dipa"],
    "कविता": ["kavita", "kavitha"],
    "अनीता": ["anita", "aneeta"],
    "शोभा": ["shobha", "shobhna"],
    "उषा": ["usha", "oosha"],
    "आशा": ["asha", "aasha"],
    "मीना": ["meena", "mina"],
    "वीणा": ["veena", "vina"],
    "सरला": ["sarla", "sarala"],
    "शांति": ["shanti", "shanthi"],
}
