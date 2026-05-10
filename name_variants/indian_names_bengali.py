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

INDIAN_NAMES_BENGALI: dict[str, dict] = {
    'চট্টোপাধ্যায়': {
        "forms": ['chattopadhyay', 'chatterjee', 'chattopadhyaya', 'chatterji'],
    },
    'মুখোপাধ্যায়': {
        "forms": ['mukhopadhyay', 'mukherjee', 'mookherjee', 'mukherji'],
    },
    'বন্দ্যোপাধ্যায়': {
        "forms": ['bandyopadhyay', 'banerjee', 'bannerjee', 'banerji'],
    },
    'ভট্টাচার্য': {
        "forms": ['bhattacharya', 'bhattacharyya', 'bhattacherjee', 'bhattacharjee'],
    },
    'গঙ্গোপাধ্যায়': {
        "forms": ['gangopadhyay', 'ganguly', 'ganguli'],
    },
    'সেন': {
        "forms": ['sen', 'senne'],
    },
    'বসু': {
        "forms": ['basu', 'bose', 'bossu'],
    },
    'দত্ত': {
        "forms": ['datta', 'dutt', 'datt'],
    },
    'ঘোষ': {
        "forms": ['ghosh', 'ghose', 'gosh'],
    },
    'মিত্র': {
        "forms": ['mitra', 'mitter', 'mittra'],
    },
    'রায়': {
        "forms": ['ray', 'roy', 'rai'],
    },
    'সরকার': {
        "forms": ['sarkar', 'sarcar'],
    },
    'চক্রবর্তী': {
        "forms": ['chakraborty', 'chakravarti', 'chakrabarti'],
    },
    'দে': {
        "forms": ['de', 'dey', 'day'],
    },
    'দাস': {
        "forms": ['das', 'dass', 'doss'],
    },
    'পাল': {
        "forms": ['pal', 'paul'],
    },
    'নন্দী': {
        "forms": ['nandi', 'nandy'],
    },
    'মজুমদার': {
        "forms": ['majumdar', 'majumdaar', 'majumder'],
    },
    'বিশ্বাস': {
        "forms": ['biswas', 'bisvas', 'biswaas'],
    },
    'হালদার': {
        "forms": ['halder', 'haldar'],
    },
    'রাহা': {
        "forms": ['raha'],
    },
    'সিংহ': {
        "forms": ['sinha', 'singha', 'siha'],
    },
    'চৌধুরী': {
        "forms": ['choudhury', 'chowdhury', 'chaudhury', 'chaudhari'],
    },
    'নাগ': {
        "forms": ['nag', 'naag'],
    },
    'চ্যাটার্জি': {
        "forms": ['chaterjee'],
    },
    'সুভাষ': {
        "forms": ['subhash', 'subhas'],
    },
    'প্রদীপ': {
        "forms": ['pradeep', 'pradip'],
    },
    'সুকান্ত': {
        "forms": ['sukanta', 'sukant'],
    },
    'অমিতাভ': {
        "forms": ['amitabh', 'amitabha'],
    },
    'সৌমেন': {
        "forms": ['soumen', 'souman'],
    },
    'দেবাশিস': {
        "forms": ['debasish', 'debashis'],
    },
    'অনির্বাণ': {
        "forms": ['anirban', 'anirbaan'],
    },
    'ঈশান': {
        "forms": ['ishan', 'ishaan', 'eshan'],
    },
    'রুদ্র': {
        "forms": ['rudra', 'rudro'],
    },
    'শান্তনু': {
        "forms": ['shantanu', 'santanu'],
    },
    'সোমনাথ': {
        "forms": ['somnath'],
    },
    'তপন': {
        "forms": ['tapan'],
    },
    'বিপ্লব': {
        "forms": ['biplob', 'biplav'],
    },
    'পার্থ': {
        "forms": ['partha', 'partho'],
    },
    'অর্ণব': {
        "forms": ['arnab', 'arnav'],
    },
    'সৌরভ': {
        "forms": ['sourav', 'saurav'],
    },
    'ঋত্বিক': {
        "forms": ['ritwik', 'ritwick'],
    },
    'সায়নী': {
        "forms": ['sayani', 'saayani'],
    },
    'মৌসুমী': {
        "forms": ['mousumi', 'moushumi', 'mousomi'],
    },
    'শর্মিলা': {
        "forms": ['sharmila', 'shormila'],
    },
    'স্বাতী': {
        "forms": ['swati', 'swatee'],
    },
    'রীতা': {
        "forms": ['rita', 'reeta'],
    },
    'মিতা': {
        "forms": ['mita', 'meeta'],
    },
    'চৈতালী': {
        "forms": ['chaitali', 'chaitaali'],
    },
    'দেবযানী': {
        "forms": ['debayani', 'devayani'],
    },
    'তৃষা': {
        "forms": ['trisha', 'tresha'],
    },
    'পায়েল': {
        "forms": ['payel', 'payal'],
    },
    'মধুমিতা': {
        "forms": ['madhumita', 'madhumitha'],
    },
    'সুচিত্রা': {
        "forms": ['suchitra', 'sucheetra'],
    },
    'অপর্ণা': {
        "forms": ['aparna', 'apurna'],
    },
    'সুপ্রিয়া': {
        "forms": ['supriya', 'supria'],
    },
}
