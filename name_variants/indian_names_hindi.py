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

INDIAN_NAMES_HINDI: dict[str, dict] = {
    "शर्मा": {
        "forms": ["sharma", "sarma", "sherma"],
    },
    "सिंह": {
        "forms": ["singh", "sing"],
    },
    "वर्मा": {
        "forms": ["varma", "verma", "varman"],
    },
    "मिश्रा": {
        "forms": ["mishra", "misra", "mitra"],
    },
    "श्रीवास्तव": {
        "forms": ["srivastava", "shrivastava", "srivastav", "shrivastav"],
    },
    "पाठक": {
        "forms": ["pathak", "patak"],
    },
    "तिवारी": {
        "forms": ["tiwari", "tivari", "tewari"],
    },
    "पांडे": {
        "forms": ["pandey", "pande", "panday"],
    },
    "दुबे": {
        "forms": ["dubey", "dube", "dubé"],
    },
    "यादव": {
        "forms": ["yadav", "yadaw"],
    },
    "पटेल": {
        "forms": ["patel", "patil", "pattel"],
    },
    "गुप्ता": {
        "forms": ["gupta"],
    },
    "जोशी": {
        "forms": ["joshi", "josi"],
    },
    "अग्रवाल": {
        "forms": ["agrawal", "agarwal"],
    },
    "चौधरी": {
        "forms": ["chaudhary", "chaudhury", "choudhary", "choudhury", "chowdhury"],
    },
    "राय": {
        "forms": ["rai", "ray", "roi"],
    },
    "कुमार": {
        "forms": ["kumar", "koomar"],
    },
    "खान": {
        "forms": ["khan", "kahn"],
    },
    "त्रिपाठी": {
        "forms": ["tripathi", "tripati"],
    },
    "दीक्षित": {
        "forms": ["dixit", "dikshit", "dikshita"],
    },
    "अवस्थी": {
        "forms": ["awasthi", "avasthi"],
    },
    "सक्सेना": {
        "forms": ["saxena", "saksena"],
    },
    "भार्गव": {
        "forms": ["bhargava", "bhargav"],
    },
    "बाजपेई": {
        "forms": ["bajpai", "bajpei", "bajpeyi"],
    },
    "राम": {
        "forms": ["ram", "raam"],
    },
    "कृष्ण": {
        "forms": ["krishna", "krishn", "krushna"],
    },
    "विष्णु": {
        "forms": ["vishnu", "bisnu"],
    },
    "शिव": {
        "forms": ["shiv", "shiva", "siva"],
    },
    "देव": {
        "forms": ["dev", "deb"],
    },
    "प्रकाश": {
        "forms": ["prakash", "prakasam"],
    },
    "मोहन": {
        "forms": ["mohan", "mohen"],
    },
    "लाल": {
        "forms": ["lal", "laal"],
    },
    "चंद": {
        "forms": ["chand", "chandra"],
    },
    "नाथ": {
        "forms": ["nath", "natha"],
    },
    "दास": {
        "forms": ["das", "doss", "dass"],
    },
    "प्रसाद": {
        "forms": ["prasad", "prasada"],
    },
    "नारायण": {
        "forms": ["narayan", "narayana"],
    },
    "बाबू": {
        "forms": ["babu", "baboo"],
    },
    "सुब्रमण्यम": {
        "forms": ["subramaniam", "subramanian", "subramanyam", "subrahmanyam"],
    },
    "रमेश": {
        "forms": ["ramesh"],
    },
    "सुरेश": {
        "forms": ["suresh", "sooresh"],
    },
    "महेश": {
        "forms": ["mahesh"],
    },
    "राजेश": {
        "forms": ["rajesh"],
    },
    "दिनेश": {
        "forms": ["dinesh"],
    },
    "नरेश": {
        "forms": ["naresh", "narresh"],
    },
    "अनिल": {
        "forms": ["anil", "aneel"],
    },
    "सुनील": {
        "forms": ["sunil", "suneel"],
    },
    "विनोद": {
        "forms": ["vinod", "binod"],
    },
    "अरविंद": {
        "forms": ["arvind", "aravind", "arvinda"],
    },
    "विजय": {
        "forms": ["vijay", "bijay"],
    },
    "अजय": {
        "forms": ["ajay"],
    },
    "संजय": {
        "forms": ["sanjay"],
    },
    "रवि": {
        "forms": ["ravi", "rabi"],
    },
    "अमित": {
        "forms": ["amit", "ameet"],
    },
    "पवन": {
        "forms": ["pawan", "pavan"],
    },
    "ललित": {
        "forms": ["lalit", "laleet"],
    },
    "आनंद": {
        "forms": ["anand", "ananda"],
    },
    "संदीप": {
        "forms": ["sandeep", "sandip"],
    },
    "अभिषेक": {
        "forms": ["abhishek", "abhisheck"],
    },
    "मनोज": {
        "forms": ["manoj", "manodj"],
    },
    "प्रीति": {
        "forms": ["preeti", "priti", "preety"],
    },
    "नीता": {
        "forms": ["neeta", "nita", "neita"],
    },
    "सीता": {
        "forms": ["sita", "seeta"],
    },
    "गीता": {
        "forms": ["gita", "geeta"],
    },
    "सुनीता": {
        "forms": ["sunita", "suneeta"],
    },
    "रेखा": {
        "forms": ["rekha"],
    },
    "ममता": {
        "forms": ["mamta", "mamata"],
    },
    "सविता": {
        "forms": ["savita", "savitta"],
    },
    "रीता": {
        "forms": ["rita", "reeta"],
    },
    "लता": {
        "forms": ["lata", "laata"],
    },
    "पूजा": {
        "forms": ["pooja", "puja"],
    },
    "दीपा": {
        "forms": ["deepa", "dipa"],
    },
    "कविता": {
        "forms": ["kavita", "kavitha"],
    },
    "अनीता": {
        "forms": ["anita", "aneeta"],
    },
    "शोभा": {
        "forms": ["shobha", "shobhna"],
    },
    "उषा": {
        "forms": ["usha", "oosha"],
    },
    "आशा": {
        "forms": ["asha", "aasha"],
    },
    "मीना": {
        "forms": ["meena", "mina"],
    },
    "वीणा": {
        "forms": ["veena", "vina"],
    },
    "सरला": {
        "forms": ["sarla", "sarala"],
    },
    "शांति": {
        "forms": ["shanti", "shanthi"],
    },
}
