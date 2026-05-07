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

INDONESIAN_MALAY_NAME_VARIANTS: dict[str, list[str]] = {
    # ── Old Dutch oe→u systematic variants ──────────────────────────────────
    "sukarno": ["sukarno", "soekarno"],
    "suharto": ["suharto", "soeharto"],
    "susilo": ["susilo", "soesilo"],
    "suryadi": ["suryadi", "soerjadi"],
    "subagio": ["subagio", "soebagio"],
    "sutrisno": ["sutrisno", "soetrisno"],
    "sudirman": ["sudirman", "soedirman"],
    "sugiyono": ["sugiyono", "soegiyono"],
    "sumarsono": ["sumarsono", "soemarsono"],
    "sunarso": ["sunarso", "soenarso"],
    "supartono": ["supartono", "soepartono"],
    "subroto": ["subroto", "soebroto"],
    "surya": ["surya", "soerya"],
    "suryono": ["suryono", "soerjono"],
    "sutopo": ["sutopo", "soetopo"],
    # ── Old Dutch dj→j systematic variants ───────────────────────────────────
    "joko": ["joko", "djoko"],
    "jokowi": ["jokowi", "djokowi"],
    "juanda": ["juanda", "djuanda"],
    "jaksa": ["jaksa", "djaksa"],
    "jakarta": ["jakarta", "djakarta"],
    "jenderal": ["jenderal", "djenderal"],
    # ── Common Indonesian surnames / family name components ──────────────────
    "nasution": ["nasution", "nasoetion"],
    "situmorang": ["situmorang", "sitoemorang"],
    "simatupang": ["simatupang", "simatoepang"],
    "lumbantobing": ["lumbantobing", "loembantoebing"],
    "simbolon": ["simbolon", "simboeloen"],
    "panjaitan": ["panjaitan", "pandjaitan"],
    "simanjuntak": ["simanjuntak", "simandjoentak"],
    "pakpahan": ["pakpahan", "pakpahan"],
    "hutapea": ["hutapea", "hoetapea"],
    "nainggolan": ["nainggolan", "naingolan"],
    "sinaga": ["sinaga", "sinaga"],
    "rajagukguk": ["rajagukguk", "radjagoekoek"],
    # ── Common Malay names ────────────────────────────────────────────────────
    # Note: muhammad/mohamad covered by arabic_names محمد entry

    "ahmad": ["ahmad", "ahmed"],
    "mohd": ["mohd", "md"],        # common abbreviation
    "abd": ["abd", "ab"],          # Abdul abbreviation
    "rahman": ["rahman", "rahman"],
    "rahim": ["rahim", "raheem"],
    "aziz": ["aziz", "azees"],
    "hamid": ["hamid", "hameed"],
    "hassan": ["hassan", "hasan"],
    "ibrahim": ["ibrahim", "ebrahim"],
    "ismail": ["ismail", "esmail"],
    "abdullah": ["abdullah", "abdallah"],
    "razak": ["razak", "razack"],
    "mahathir": ["mahathir", "mahatheer"],
    "anwar": ["anwar", "anwaar"],
    # ── Common Indonesian given names ─────────────────────────────────────────
    "budi": ["budi", "boedi"],
    "dewi": ["dewi", "dewie"],
    "sri": ["sri", "srie"],
    "eko": ["eko", "eco"],
    "agus": ["agus", "agoes"],
    "hendra": ["hendra", "hendra"],
    "rini": ["rini", "reenie"],
    "sari": ["sari", "sarie"],
    "wati": ["wati", "watie"],
    "yanti": ["yanti", "janti"],
    "purnomo": ["purnomo", "poernomo"],
    "pranowo": ["pranowo", "pranowo"],
    "wahyudi": ["wahyudi", "wahjoedi"],
    "priyono": ["priyono", "prijono"],
    "santoso": ["santoso", "santoeso"],
    "handoyo": ["handoyo", "handojo"],
    "widodo": ["widodo", "widodo"],
    "suprapto": ["suprapto", "soeprapto"],
    "rahayu": ["rahayu", "rahajoe"],
    "susanti": ["susanti", "soesanti"],
    "kurniawan": ["kurniawan", "koerniawan"],
    "cahyono": ["cahyono", "cahjono"],
    "nugroho": ["nugroho", "noegroho"],
    "wibowo": ["wibowo", "wibobo"],
    "hartono": ["hartono", "hartono"],
    "gunawan": ["gunawan", "goenawan"],
    "setiawan": ["setiawan", "setijawan"],
    "kusuma": ["kusuma", "koesoema"],
    "saputra": ["saputra", "sapoetra"],
    "pratama": ["pratama", "pratama"],
}
