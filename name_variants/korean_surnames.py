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

KOREAN_SURNAME_VARIANTS: dict[str, dict] = {
    "김": {
        "forms": ["kim", "gim"],
        "frequency": 10_687_000,
    },
    "이": {
        "forms": ["lee", "yi", "rhee", "li", "ie", "rhie", "ree", "i"],
        "frequency": 7_307_000,
    },
    "박": {
        "forms": ["park", "bak", "pak"],
        "frequency": 4_192_000,
    },
    "최": {
        "forms": ["choi", "choe", "choy"],
        "frequency": 2_334_000,
    },
    "정": {
        "forms": ["jung", "jeong", "chung", "chong", "joung"],
        "frequency": 2_151_000,
    },
    "강": {
        "forms": ["kang", "gang", "kahng"],
        "frequency": 1_176_000,
    },
    "조": {
        "forms": ["jo", "cho", "joe"],
        "frequency": 1_059_000,
    },
    "윤": {
        "forms": ["yoon", "yun", "youn"],
        "frequency": 1_029_000,
    },
    "장": {
        "forms": ["jang", "chang", "jahng"],
        "frequency": 992_000,
    },
    "임": {
        "forms": ["lim", "im", "rim"],
        "frequency": 822_000,
    },
    "한": {
        "forms": ["han", "hahn", "haan"],
        "frequency": 773_000,
    },
    "오": {
        "forms": ["oh", "o", "ohh"],
        "frequency": 763_000,
    },
    "서": {
        "forms": ["seo", "suh", "so", "sue"],
        "frequency": 751_000,
    },
    "신": {
        "forms": ["shin", "sin", "shinn"],
        "frequency": 739_000,
    },
    "권": {
        "forms": ["kwon", "gwon", "kwan", "kweon"],
        "frequency": 705_000,
    },
    "황": {
        "forms": ["hwang", "whang"],
    },
    "안": {
        "forms": ["an", "ahn"],
    },
    "송": {
        "forms": ["song", "soong"],
    },
    "류": {
        "forms": ["ryu", "ryoo", "yoo", "yu"],
    },
    "전": {
        "forms": ["jeon", "chon", "jun", "cheon"],
    },
    "홍": {
        "forms": ["hong", "hoong"],
    },
    "고": {
        "forms": ["ko", "go", "goh"],
    },
    "문": {
        "forms": ["moon", "mun"],
    },
    "양": {
        "forms": ["yang", "ryang"],
    },
    "손": {
        "forms": ["son", "sohn", "shon"],
    },
    "배": {
        "forms": ["bae", "bai", "pae"],
    },
    "백": {
        "forms": ["baek", "paek", "back"],
    },
    "허": {
        "forms": ["heo", "huh", "hur"],
    },
    "유": {
        "forms": ["yoo", "yu", "yuh"],
    },
    "남": {
        "forms": ["nam", "nahm"],
    },
    "심": {
        "forms": ["shim", "sim"],
    },
    "노": {
        "forms": ["noh", "roh", "no"],
    },
    "하": {
        "forms": ["ha", "hah"],
    },
    "곽": {
        "forms": ["kwak", "gwak", "kwack"],
    },
    "성": {
        "forms": ["sung", "seong", "soung"],
    },
    "차": {
        "forms": ["cha", "chah"],
    },
    "주": {
        "forms": ["joo", "ju", "choo"],
    },
    "우": {
        "forms": ["woo", "wu", "u"],
    },
    "구": {
        "forms": ["koo", "ku", "goo"],
    },
    "민": {
        "forms": ["min", "minn"],
    },
    "나": {
        "forms": ["na", "rha"],
    },
    "도": {
        "forms": ["do", "doh", "to"],
    },
    "엄": {
        "forms": ["um", "eom", "ohm"],
    },
    "여": {
        "forms": ["yeo", "yuh", "yo"],
    },
    "추": {
        "forms": ["chu", "choo"],
    },
    "함": {
        "forms": ["ham", "hahm"],
    },
    "표": {
        "forms": ["pyo", "poe"],
    },
    "원": {
        "forms": ["won", "weon"],
    },
    "천": {
        "forms": ["cheon", "chun", "chon"],
    },
    "방": {
        "forms": ["bang", "pahng"],
    },
    "공": {
        "forms": ["gong", "kong"],
    },
    "채": {
        "forms": ["chae", "che"],
    },
    "변": {
        "forms": ["byun", "byeon", "byon"],
    },
    "마": {
        "forms": ["ma", "mah"],
    },
    "석": {
        "forms": ["seok", "suk"],
    },
    "경": {
        "forms": ["kyung", "gyeong", "kyeong"],
    },
    "봉": {
        "forms": ["bong", "pong"],
    },
    "두": {
        "forms": ["du", "doo"],
    },
    "위": {
        "forms": ["wi", "wee"],
    },
    "태": {
        "forms": ["tae", "tai"],
    },
    "진": {
        "forms": ["jin", "chin"],
    },
    "선": {
        "forms": ["sun", "seon"],
    },
    "은": {
        "forms": ["eun", "un"],
    },
    "길": {
        "forms": ["gil", "kil"],
    },
    "국": {
        "forms": ["kook", "kuk", "guk"],
    },
    "부": {
        "forms": ["boo", "bu"],
    },
    "지": {
        "forms": ["ji", "chi"],
    },
    "어": {
        "forms": ["eo", "uh"],
    },
    "연": {
        "forms": ["yeon", "yun", "yon"],
    },
    "승": {
        "forms": ["seung", "sung"],
    },
    "사": {
        "forms": ["sa", "sar"],
    },
    "소": {
        "forms": ["so", "soh"],
    },
    "목": {
        "forms": ["mok", "mock"],
    },
    "로": {
        "forms": ["roh", "ro", "no"],
    },
    "제": {
        "forms": ["je", "jeh"],
    },
    "감": {
        "forms": ["gam", "kam", "kahm"],
    },
    "옥": {
        "forms": ["ok", "ohk"],
    },
    "무": {
        "forms": ["mu", "moo"],
    },
    "라": {
        "forms": ["ra", "la", "rha"],
    },
    "용": {
        "forms": ["yong", "ryong"],
    },
    "동": {
        "forms": ["dong", "tong"],
    },
    "맹": {
        "forms": ["maeng", "meng"],
    },
    "모": {
        "forms": ["mo", "moh"],
    },
    "반": {
        "forms": ["ban", "van", "pan"],
    },
    "복": {
        "forms": ["bok", "bock"],
    },
    "명": {
        "forms": ["myung", "myeong", "myong"],
    },
    "탁": {
        "forms": ["tak", "tack"],
    },
    "상": {
        "forms": ["sang", "shahng"],
    },
    "인": {
        "forms": ["in", "inn"],
    },
    "온": {
        "forms": ["on", "ohn"],
    },
    "편": {
        "forms": ["pyeon", "pyon"],
    },
    "수": {
        "forms": ["su", "soo"],
    },
    "팽": {
        "forms": ["paeng", "peng"],
    },
    "독": {
        "forms": ["dok", "dock"],
    },
    "각": {
        "forms": ["gak", "kak"],
    },
    "탄": {
        "forms": ["than"],
    },
    "포": {
        "forms": ["po", "poh"],
    },
    "피": {
        "forms": ["pi", "pee"],
    },
    "예": {
        "forms": ["ye", "yeh"],
    },
    "탕": {
        "forms": ["tang", "tahng"],
    },
}
