"""
Indonesian/Malay name lookup.

Lower variant severity than other scripts — already Latin — but there are two
key sources of variation:

1. Old Dutch orthography vs. modern Indonesian:
   Soekarno → Sukarno
   Soeharto → Suharto
   Djojohadikusumo → Djojohadikusumo (unchanged — Javanese names)
   oe → u (systematic)
   dj → j (systematic)
   j → y (partially: Yogyakarta was Jogjakarta)

2. Malay vs. Indonesian spelling differences:
   Malaysian Malay retained some older spellings

Sources:
  - Indonesian government romanization (EYD 2022)
  - Ejaan Yang Disempurnakan (EYD) spelling reform
  - Malaysian DEWAN romanization
  - Common Javanese, Sundanese, Batak, Minangkabau naming patterns
"""

INDONESIAN_MALAY_NAME_VARIANTS: dict[str, dict] = {
    "sukarno": {
        "forms": ["sukarno", "soekarno"],
    },
    "suharto": {
        "forms": ["suharto", "soeharto"],
    },
    "susilo": {
        "forms": ["susilo", "soesilo"],
    },
    "suryadi": {
        "forms": ["suryadi", "soerjadi"],
    },
    "subagio": {
        "forms": ["subagio", "soebagio"],
    },
    "sutrisno": {
        "forms": ["sutrisno", "soetrisno"],
    },
    "sudirman": {
        "forms": ["sudirman", "soedirman"],
    },
    "sugiyono": {
        "forms": ["sugiyono", "soegiyono"],
    },
    "sumarsono": {
        "forms": ["sumarsono", "soemarsono"],
    },
    "sunarso": {
        "forms": ["sunarso", "soenarso"],
    },
    "supartono": {
        "forms": ["supartono", "soepartono"],
    },
    "subroto": {
        "forms": ["subroto", "soebroto"],
    },
    "surya": {
        "forms": ["surya", "soerya"],
    },
    "suryono": {
        "forms": ["suryono", "soerjono"],
    },
    "sutopo": {
        "forms": ["sutopo", "soetopo"],
    },
    "joko": {
        "forms": ["joko", "djoko"],
    },
    "jokowi": {
        "forms": ["jokowi", "djokowi"],
    },
    "juanda": {
        "forms": ["juanda", "djuanda"],
    },
    "jaksa": {
        "forms": ["jaksa", "djaksa"],
    },
    "jakarta": {
        "forms": ["jakarta", "djakarta"],
    },
    "jenderal": {
        "forms": ["jenderal", "djenderal"],
    },
    "nasution": {
        "forms": ["nasution", "nasoetion"],
    },
    "situmorang": {
        "forms": ["situmorang", "sitoemorang"],
    },
    "simatupang": {
        "forms": ["simatupang", "simatoepang"],
    },
    "lumbantobing": {
        "forms": ["lumbantobing", "loembantoebing"],
    },
    "simbolon": {
        "forms": ["simbolon", "simboeloen"],
    },
    "panjaitan": {
        "forms": ["panjaitan", "pandjaitan"],
    },
    "simanjuntak": {
        "forms": ["simanjuntak", "simandjoentak"],
    },
    "pakpahan": {
        "forms": ["pakpahan"],
    },
    "hutapea": {
        "forms": ["hutapea", "hoetapea"],
    },
    "nainggolan": {
        "forms": ["nainggolan", "naingolan"],
    },
    "sinaga": {
        "forms": ["sinaga"],
    },
    "rajagukguk": {
        "forms": ["rajagukguk", "radjagoekoek"],
    },
    "ahmad": {
        "forms": ["ahmad", "ahmed"],
    },
    "mohd": {
        "forms": ["mohd", "md"],
    },
    "abd": {
        "forms": ["abd", "ab"],
    },
    "rahman": {
        "forms": ["rahman"],
    },
    "rahim": {
        "forms": ["rahim", "raheem"],
    },
    "aziz": {
        "forms": ["aziz", "azees"],
    },
    "hamid": {
        "forms": ["hamid", "hameed"],
    },
    "ali": {
        "forms": ["ali", "aly"],
    },
    "omar": {
        "forms": ["omar", "umar", "oemar"],
    },
    "fatimah": {
        "forms": ["fatimah", "fatima", "fatema"],
    },
    "yusuf": {
        "forms": ["yusuf", "yusof", "jusuf", "yosef"],
    },
    "hassan": {
        "forms": ["hassan", "hasan"],
    },
    "ibrahim": {
        "forms": ["ibrahim", "ebrahim"],
    },
    "ismail": {
        "forms": ["ismail", "esmail"],
    },
    "abdullah": {
        "forms": ["abdullah", "abdallah"],
    },
    "razak": {
        "forms": ["razak", "razack"],
    },
    "mahathir": {
        "forms": ["mahathir", "mahatheer"],
    },
    "anwar": {
        "forms": ["anwar", "anwaar"],
    },
    "budi": {
        "forms": ["budi", "boedi"],
    },
    "dewi": {
        "forms": ["dewi", "dewie"],
    },
    "sri": {
        "forms": ["sri", "srie"],
    },
    "eko": {
        "forms": ["eko", "eco"],
    },
    "agus": {
        "forms": ["agus", "agoes"],
    },
    "hendra": {
        "forms": ["hendra"],
    },
    "rini": {
        "forms": ["rini", "reenie"],
    },
    "sari": {
        "forms": ["sari", "sarie"],
    },
    "wati": {
        "forms": ["wati", "watie"],
    },
    "yanti": {
        "forms": ["yanti", "janti"],
    },
    "purnomo": {
        "forms": ["purnomo", "poernomo"],
    },
    "pranowo": {
        "forms": ["pranowo"],
    },
    "wahyudi": {
        "forms": ["wahyudi", "wahjoedi"],
    },
    "priyono": {
        "forms": ["priyono", "prijono"],
    },
    "santoso": {
        "forms": ["santoso", "santoeso"],
    },
    "handoyo": {
        "forms": ["handoyo", "handojo"],
    },
    "widodo": {
        "forms": ["widodo"],
    },
    "suprapto": {
        "forms": ["suprapto", "soeprapto"],
    },
    "rahayu": {
        "forms": ["rahayu", "rahajoe"],
    },
    "susanti": {
        "forms": ["susanti", "soesanti"],
    },
    "kurniawan": {
        "forms": ["kurniawan", "koerniawan"],
    },
    "cahyono": {
        "forms": ["cahyono", "cahjono"],
    },
    "nugroho": {
        "forms": ["nugroho", "noegroho"],
    },
    "wibowo": {
        "forms": ["wibowo", "wibobo"],
    },
    "hartono": {
        "forms": ["hartono"],
    },
    "gunawan": {
        "forms": ["gunawan", "goenawan"],
    },
    "setiawan": {
        "forms": ["setiawan", "setijawan"],
    },
    "kusuma": {
        "forms": ["kusuma", "koesoema"],
    },
    "saputra": {
        "forms": ["saputra", "sapoetra"],
    },
    "pratama": {
        "forms": ["pratama"],
    },
}
