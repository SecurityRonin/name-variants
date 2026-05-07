"""
Korean surname lookup: Hangul → romanization variants.

Key problem: two incompatible romanization systems are both in active use:
  - McCune-Reischauer (MR): used in passports until 2000, still widespread
  - Revised Romanization of Korean (RR): official since 2000
Plus diaspora variants that follow neither system consistently.

Examples:
  박 → Park (diaspora/MR) / Bak (RR)
  이 → Lee (diaspora) / Yi (MR) / Rhee (older) / Li (Chinese-context)
  최 → Choi (MR/diaspora) / Choe (RR)
  정 → Jung / Jeong (RR) / Chung / Chong (MR)

Sources:
  - Statistics Korea surname frequency (2015 census)
  - NIKL Revised Romanization guidelines
  - McCune-Reischauer standard
  - Common diaspora (US/HK/Australia) spelling conventions
"""

KOREAN_SURNAME_VARIANTS: dict[str, list[str]] = {
    # ── Top 10 (covers ~64% of Korean population) ──────────────────────────
    "김": ["kim", "gim"],
    "이": ["lee", "yi", "rhee", "li", "ie", "rhie", "ree", "i"],
    "박": ["park", "bak", "pak"],
    "최": ["choi", "choe", "choy"],
    "정": ["jung", "jeong", "chung", "chong", "joung"],
    "강": ["kang", "gang", "kahng"],
    "조": ["jo", "cho", "joe"],
    "윤": ["yoon", "yun", "youn"],
    "장": ["jang", "chang", "jahng"],
    "임": ["lim", "im", "rim"],
    # ── 11-50 ───────────────────────────────────────────────────────────────
    "한": ["han", "hahn", "haan"],
    "오": ["oh", "o", "ohh"],
    "서": ["seo", "suh", "so", "sue"],
    "신": ["shin", "sin", "shinn"],
    "권": ["kwon", "gwon", "kwan", "kweon"],
    "황": ["hwang", "whang"],
    "안": ["an", "ahn"],
    "송": ["song", "soong"],
    "류": ["ryu", "ryoo", "yoo", "yu"],
    "전": ["jeon", "chon", "jun", "cheon"],
    "홍": ["hong", "hoong"],
    "고": ["ko", "go", "goh"],
    "문": ["moon", "mun"],
    "양": ["yang", "ryang"],
    "손": ["son", "sohn", "shon"],
    "배": ["bae", "bai", "pae"],
    "백": ["baek", "paek", "back"],
    "허": ["heo", "huh", "hur"],
    "유": ["yoo", "yu", "yuh"],
    "남": ["nam", "nahm"],
    "심": ["shim", "sim"],
    "노": ["noh", "roh", "no"],
    "하": ["ha", "hah"],
    "곽": ["kwak", "gwak", "kwack"],
    "성": ["sung", "seong", "soung"],
    "차": ["cha", "chah"],
    "주": ["joo", "ju", "choo"],
    "우": ["woo", "wu", "u"],
    "구": ["koo", "ku", "goo"],
    "민": ["min", "minn"],
    "나": ["na", "rha"],
    "도": ["do", "doh", "to"],
    "엄": ["um", "eom", "ohm"],
    "여": ["yeo", "yuh", "yo"],
    "추": ["chu", "choo"],
    "함": ["ham", "hahm"],
    "표": ["pyo", "poe"],
    "원": ["won", "weon"],
    "천": ["cheon", "chun", "chon"],
    "방": ["bang", "pahng"],
    "공": ["gong", "kong"],
    "채": ["chae", "che"],
    "변": ["byun", "byeon", "byon"],
    "마": ["ma", "mah"],
    "석": ["seok", "suk"],
    # ── 51-100 ──────────────────────────────────────────────────────────────
    "경": ["kyung", "gyeong", "kyeong"],
    "봉": ["bong", "pong"],
    "두": ["du", "doo"],
    "위": ["wi", "wee"],
    "태": ["tae", "tai"],
    "진": ["jin", "chin"],
    "선": ["sun", "seon"],
    "은": ["eun", "un"],
    "길": ["gil", "kil"],
    "국": ["kook", "kuk", "guk"],
    "부": ["boo", "bu"],
    "지": ["ji", "chi"],
    "어": ["eo", "uh"],
    "연": ["yeon", "yun", "yon"],
    "승": ["seung", "sung"],
    "사": ["sa", "sar"],
    "소": ["so", "soh"],
    "목": ["mok", "mock"],
    "로": ["roh", "ro", "no"],
    "제": ["je", "jeh"],
    "감": ["gam", "kam", "kahm"],
    "옥": ["ok", "ohk"],
    "무": ["mu", "moo"],
    "라": ["ra", "la", "rha"],
    "용": ["yong", "ryong"],
    "동": ["dong", "tong"],
    "맹": ["maeng", "meng"],
    "모": ["mo", "moh"],
    "반": ["ban", "van", "pan"],
    "복": ["bok", "bock"],
    "명": ["myung", "myeong", "myong"],
    "탁": ["tak", "tack"],
    "상": ["sang", "shahng"],
    "인": ["in", "inn"],
    "온": ["on", "ohn"],
    "편": ["pyeon", "pyon"],
    "수": ["su", "soo"],
    "팽": ["paeng", "peng"],
    "독": ["dok", "dock"],
    "각": ["gak", "kak"],
    "탄": ["than"],
    "포": ["po", "poh"],
    "피": ["pi", "pee"],
    "예": ["ye", "yeh"],
    "탕": ["tang", "tahng"],
}
