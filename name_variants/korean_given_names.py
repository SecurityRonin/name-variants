"""Korean given-name romanization variants.

Canonical keys are Hangul syllables (single or compound).
Variants are romanizations (lowercase).

Genuine romanization ambiguity is a feature: lookup() returns ALL matching
clusters, so no romanization should be stripped to avoid collisions.
"""

KOREAN_GIVEN_NAME_VARIANTS: dict[str, dict] = {
    "재": {
        "forms": ["jae"],
    },
    "민": {
        "forms": ["min", "meen"],
    },
    "지": {
        "forms": ["ji", "jee", "chi"],
    },
    "현": {
        "forms": ["hyun", "hyeon"],
    },
    "준": {
        "forms": ["joon"],
    },
    "서": {
        "forms": ["seo", "suh"],
        "frequency": 751_000,
    },
    "은": {
        "forms": ["eun", "un"],
    },
    "수": {
        "forms": ["su", "soo"],
    },
    "진": {
        "forms": ["jin", "jean"],
    },
    "혜": {
        "forms": ["hye", "hae", "hey"],
    },
    "아": {
        "forms": ["ah", "a"],
    },
    "영": {
        "forms": ["yeong"],
    },
    "미": {
        "forms": ["mi", "mee"],
    },
    "나": {
        "forms": ["na", "nah"],
    },
    "소": {
        "forms": ["so"],
    },
    "윤": {
        "forms": ["yoon"],
        "frequency": 1_029_000,
    },
    "하": {
        "forms": ["hah"],
    },
    "유": {
        "forms": ["yoo"],
    },
    "세": {
        "forms": ["se", "say"],
    },
    "연": {
        "forms": ["yeon"],
    },
    "정": {
        "forms": ["jeong", "jung"],
        "frequency": 2_151_000,
    },
    "경": {
        "forms": ["kyung", "kyeong", "gyeong"],
    },
    "성": {
        "forms": ["seong"],
    },
    "호": {
        "forms": ["hoh"],
    },
    "기": {
        "forms": ["ki", "gi", "kee"],
    },
    "철": {
        "forms": ["cheol", "chul", "chol"],
    },
    "종": {
        "forms": ["jong"],
    },
    "원": {
        "forms": ["won", "weon"],
    },
    "희": {
        "forms": ["hyi"],
    },
    "태": {
        "forms": ["tae"],
    },
    "선": {
        "forms": ["seon", "sen"],
    },
    "환": {
        "forms": ["hwan", "hwon"],
    },
    "우": {
        "forms": ["wu", "woo", "u"],
    },
    "도": {
        "forms": ["doh"],
    },
    "찬": {
        "forms": ["chan", "chahn"],
    },
    "빈": {
        "forms": ["been"],
    },
    "인": {
        "forms": ["in", "een"],
    },
    "석": {
        "forms": ["seok", "suk", "seck"],
    },
    "한": {
        "forms": ["hahn"],
        "frequency": 773_000,
    },
    "상": {
        "forms": ["sahng"],
    },
    "오": {
        "forms": ["oh"],
        "frequency": 763_000,
    },
    "창": {
        "forms": ["chang", "chahng"],
    },
    "안": {
        "forms": ["ahn"],
    },
    "승": {
        "forms": ["seung"],
    },
    "국": {
        "forms": ["guk", "kuk"],
    },
    "병": {
        "forms": ["byung", "byeong", "byong"],
    },
    "길": {
        "forms": ["gil"],
    },
    "광": {
        "forms": ["gwang", "kwang"],
    },
    "봉": {
        "forms": ["bong", "bohng"],
    },
    "용": {
        "forms": ["yong", "ryong"],
    },
    "가": {
        "forms": ["ga", "ka"],
    },
    "다": {
        "forms": ["da"],
    },
    "라": {
        "forms": ["ra", "la"],
    },
    "마": {
        "forms": ["ma"],
    },
    "바": {
        "forms": ["ba"],
    },
    "사": {
        "forms": ["sa"],
    },
    "자": {
        "forms": ["ja"],
    },
    "차": {
        "forms": ["cha", "ca"],
    },
    "파": {
        "forms": ["pa"],
    },
    "혁": {
        "forms": ["hyuk", "hyeok"],
    },
    "민준": {
        "forms": ["minjun"],
    },
    "서준": {
        "forms": ["seojun"],
    },
    "예린": {
        "forms": ["yerin"],
    },
    "지우": {
        "forms": ["jiu", "jiwo"],
    },
    "지호": {
        "forms": ["jiho"],
    },
    "지훈": {
        "forms": ["jihun", "jihoon"],
    },
    "수현": {
        "forms": ["suhyun", "soohyeon"],
    },
    "예준": {
        "forms": ["yejun"],
    },
    "도현": {
        "forms": ["dohyun", "dohyeon"],
    },
    "시우": {
        "forms": ["siwo"],
    },
}
