"""
Chinese surname lookup: Simplified Han → romanization variants.
Covers Mandarin (Pinyin), Cantonese (Jyutping/Yale), Hokkien/Teochew/Hakka, Wade-Giles.

Key: always Traditional character (where one exists). Simplified form is included
as a co-equal member of the same cluster with dialect tag "simplified".
Romanizations: all lowercase.

Sources:
  - 百家姓 census + modern CNKI surname frequency data
  - HK Immigration Department romanization standards
  - SEA Chinese (Singapore/Malaysia) naming conventions
  - Jyutping romanization for Cantonese
"""

CHINESE_SURNAME_VARIANTS: dict[str, dict] = {
    "王": {
        "forms": ["wang", "wong", "ong", "ang"],
        "frequency": 106_760_000,
        "dialects": {
            "ang": "hokkien",
            "ong": "hokkien",
            "wang": "mandarin_pinyin",
            "wong": "cantonese",
        },
    },
    "李": {
        "forms": ["li", "lee", "lei", "ly"],
        "frequency": 95_300_000,
        "dialects": {
            "lee": "cantonese",
            "lei": "cantonese",
            "li": "mandarin_pinyin",
            "ly": "hokkien",
        },
    },
    "張": {
        "forms": [
            "zhang",
            "chang",
            "cheung",
            "cheong",
            "teo",
            "tio",
            "chong",
            "chung",
            "jeung",
            "张",
        ],
        "frequency": 87_500_000,
        "dialects": {
            "chang": "wade_giles",
            "cheong": "cantonese",
            "cheung": "cantonese",
            "chong": "hakka",
            "chung": "hakka",
            "jeung": "cantonese",
            "teo": "hokkien",
            "tio": "teochew",
            "zhang": "mandarin_pinyin",
            "张": "simplified",
        },
    },
    "劉": {
        "forms": ["liu", "lau", "lew", "low", "liew", "刘"],
        "frequency": 73_000_000,
        "dialects": {
            "lau": "cantonese",
            "lew": "cantonese",
            "liew": "hokkien",
            "liu": "mandarin_pinyin",
            "low": "hokkien",
            "刘": "simplified",
        },
    },
    "陳": {
        "forms": ["chen", "chan", "tan", "chin", "zen", "chern", "陈"],
        "frequency": 70_500_000,
        "dialects": {
            "chan": "cantonese",
            "chen": "mandarin_pinyin",
            "chern": "wade_giles",
            "chin": "hakka",
            "tan": "hokkien",
            "zen": "mandarin_pinyin",
            "陈": "simplified",
        },
    },
    "楊": {
        "forms": ["yang", "yeung", "yeong", "yong", "young", "io", "杨"],
        "frequency": 46_200_000,
        "dialects": {
            "io": "teochew",
            "yang": "mandarin_pinyin",
            "yeong": "cantonese",
            "yeung": "cantonese",
            "yong": "hokkien",
            "young": "hokkien",
            "杨": "simplified",
        },
    },
    "黃": {
        "forms": ["huang", "ng", "oei", "uy", "wee", "way", "huong", "黄"],
        "frequency": 32_000_000,
        "dialects": {
            "huang": "mandarin_pinyin",
            "huong": "hokkien",
            "ng": "cantonese",
            "oei": "hokkien",
            "uy": "hokkien",
            "way": "hokkien",
            "wee": "hokkien",
            "黄": "simplified",
        },
    },
    "趙": {
        "forms": ["zhao", "chao", "chew", "chu", "chiu", "tio", "dzao", "赵"],
        "frequency": 28_400_000,
        "dialects": {
            "chao": "wade_giles",
            "chew": "cantonese",
            "chiu": "cantonese",
            "chu": "cantonese",
            "dzao": "wade_giles",
            "tio": "teochew",
            "zhao": "mandarin_pinyin",
            "赵": "simplified",
        },
    },
    "吳": {
        "forms": ["wu", "ng", "goh", "ngo", "woo", "ou", "吴"],
        "frequency": 27_400_000,
        "dialects": {
            "goh": "hokkien",
            "ng": "cantonese",
            "ngo": "cantonese",
            "ou": "teochew",
            "woo": "cantonese",
            "wu": "mandarin_pinyin",
            "吴": "simplified",
        },
    },
    "周": {
        "forms": ["zhou", "chow", "jou", "chu", "chou", "tsou", "chau"],
        "frequency": 25_600_000,
        "dialects": {
            "chau": "cantonese",
            "chou": "wade_giles",
            "chow": "cantonese",
            "chu": "cantonese",
            "jou": "wade_giles",
            "tsou": "wade_giles",
            "zhou": "mandarin_pinyin",
        },
    },
    "徐": {
        "forms": ["xu", "hsu", "hui", "tsui", "chui", "kho", "khoo", "zee"],
        "frequency": 20_800_000,
        "dialects": {
            "hsu": "wade_giles",
            "hui": "cantonese",
            "kho": "hokkien",
            "khoo": "hokkien",
            "xu": "mandarin_pinyin",
        },
    },
    "孙": {
        "forms": ["sun", "suen", "soon"],
        "frequency": 18_400_000,
    },
    "马": {
        "forms": ["ma", "mah"],
        "frequency": 17_300_000,
    },
    "朱": {
        "forms": ["zhu", "chu", "choo"],
        "frequency": 14_900_000,
        "dialects": {
            "chu": "cantonese",
            "zhu": "mandarin_pinyin",
        },
    },
    "胡": {
        "forms": ["hu", "woo", "foo"],
        "frequency": 14_700_000,
        "dialects": {
            "woo": "cantonese",
        },
    },
    "郭": {
        "forms": ["guo", "kuo", "kwok", "kuok", "kok", "quek"],
        "frequency": 14_000_000,
        "dialects": {
            "guo": "mandarin_pinyin",
            "kok": "hokkien",
            "kuo": "wade_giles",
            "kuok": "cantonese",
            "kwok": "cantonese",
            "quek": "hokkien",
        },
    },
    "何": {
        "forms": ["he", "ho", "hoe"],
        "frequency": 13_700_000,
    },
    "高": {
        "forms": ["gao", "kao", "ko", "cao", "koh"],
        "frequency": 13_600_000,
        "dialects": {
            "cao": "mandarin_pinyin",
            "gao": "mandarin_pinyin",
            "kao": "wade_giles",
        },
    },
    "林": {
        "forms": ["lin", "lim", "lam", "ling", "lum"],
        "frequency": 18_700_000,
        "dialects": {
            "lam": "cantonese",
            "lim": "hokkien",
            "lin": "mandarin_pinyin",
            "ling": "hakka",
            "lum": "cantonese",
        },
    },
    "鄭": {
        "forms": ["zheng", "cheng", "teh", "tay", "tee", "ching", "zeng", "郑"],
        "dialects": {
            "cheng": "cantonese",
            "ching": "hakka",
            "tay": "hokkien",
            "tee": "hokkien",
            "teh": "hokkien",
            "zeng": "mandarin_pinyin",
            "zheng": "mandarin_pinyin",
            "郑": "simplified",
        },
    },
    "谢": {
        "forms": ["謝", "xie", "hsieh", "tse", "chia", "sia", "ze"],
        "dialects": {
            "hsieh": "wade_giles",
            "tse": "cantonese",
            "xie": "mandarin_pinyin",
        },
    },
    "羅": {
        "forms": ["luo", "lo", "law", "loh", "罗"],
        "frequency": 12_800_000,
        "dialects": {
            "law": "cantonese",
            "lo": "cantonese",
            "loh": "hokkien",
            "luo": "mandarin_pinyin",
            "罗": "simplified",
        },
    },
    "梁": {
        "forms": ["liang", "leung", "neo"],
        "dialects": {
            "leung": "cantonese",
            "liang": "mandarin_pinyin",
            "neo": "hokkien",
        },
    },
    "宋": {
        "forms": ["song", "soong", "sung"],
        "dialects": {
            "song": "mandarin_pinyin",
            "soong": "wade_giles",
            "sung": "wade_giles",
        },
    },
    "唐": {
        "forms": ["tang", "tong", "dong", "thong"],
        "dialects": {
            "dong": "mandarin_pinyin",
            "tang": "mandarin_pinyin",
            "thong": "hokkien",
            "tong": "cantonese",
        },
    },
    "許": {
        "forms": ["xu", "hui", "kho", "khoo", "heui", "hee", "许"],
        "dialects": {
            "hee": "hokkien",
            "heui": "cantonese",
            "hui": "cantonese",
            "kho": "hokkien",
            "khoo": "hokkien",
            "xu": "mandarin_pinyin",
            "许": "simplified",
        },
    },
    "韩": {
        "forms": ["韓", "han", "hon", "hann"],
    },
    "馮": {
        "forms": ["feng", "fung", "fong", "hong", "foong", "冯"],
        "dialects": {
            "feng": "mandarin_pinyin",
            "fong": "cantonese",
            "foong": "hokkien",
            "fung": "cantonese",
            "冯": "simplified",
        },
    },
    "邓": {
        "forms": ["鄧", "deng", "tang", "teng", "ding"],
        "dialects": {
            "tang": "mandarin_pinyin",
        },
    },
    "曹": {
        "forms": ["cao", "tsao", "chou", "cho"],
        "dialects": {
            "cao": "mandarin_pinyin",
            "chou": "wade_giles",
            "tsao": "wade_giles",
        },
    },
    "彭": {
        "forms": ["peng", "phang", "pheng"],
    },
    "曾": {
        "forms": ["zeng", "tsang", "tseng"],
        "dialects": {
            "tsang": "cantonese",
            "tseng": "wade_giles",
            "zeng": "mandarin_pinyin",
        },
    },
    "蕭": {
        "forms": ["xiao", "hsiao", "siu", "sieu", "sew", "萧"],
        "dialects": {
            "hsiao": "wade_giles",
            "sew": "hokkien",
            "sieu": "hokkien",
            "siu": "cantonese",
            "xiao": "mandarin_pinyin",
            "萧": "simplified",
        },
    },
    "田": {
        "forms": ["tian", "tin"],
    },
    "董": {
        "forms": ["dong", "tung"],
        "dialects": {
            "dong": "mandarin_pinyin",
        },
    },
    "袁": {
        "forms": ["yuan", "yuen"],
    },
    "潘": {
        "forms": ["pan", "poon", "pua"],
    },
    "于": {
        "forms": ["yu", "yee", "ee"],
    },
    "蔣": {
        "forms": ["jiang", "chiang", "cheung", "tsiang", "蒋"],
        "dialects": {
            "cheung": "cantonese",
            "chiang": "wade_giles",
            "jiang": "mandarin_pinyin",
            "tsiang": "wade_giles",
            "蒋": "simplified",
        },
    },
    "蔡": {
        "forms": ["cai", "chua", "tsai", "chai"],
        "dialects": {
            "cai": "mandarin_pinyin",
            "chai": "cantonese",
            "chua": "hokkien",
            "tsai": "wade_giles",
        },
    },
    "余": {
        "forms": ["yu", "yee", "ee"],
    },
    "蘇": {
        "forms": ["su", "soo", "soh", "see", "苏"],
        "dialects": {
            "see": "hokkien",
            "soh": "hokkien",
            "soo": "hokkien",
            "su": "mandarin_pinyin",
            "苏": "simplified",
        },
    },
    "葉": {
        "forms": ["ye", "yeh", "yap", "ip", "yip", "jip", "叶"],
        "dialects": {
            "ip": "cantonese",
            "jip": "hakka",
            "yap": "cantonese",
            "ye": "mandarin_pinyin",
            "yeh": "wade_giles",
            "yip": "cantonese",
            "叶": "simplified",
        },
    },
    "吕": {
        "forms": ["呂", "lu", "lui", "loo", "lv"],
    },
    "魏": {
        "forms": ["wei", "ngai"],
    },
    "程": {
        "forms": ["cheng", "ching"],
        "dialects": {
            "cheng": "cantonese",
            "ching": "hakka",
        },
    },
    "沈": {
        "forms": ["shen", "shum", "sim"],
    },
    "江": {
        "forms": ["jiang", "kong", "kang"],
        "dialects": {
            "jiang": "mandarin_pinyin",
        },
    },
    "傅": {
        "forms": ["fu", "foo", "phu"],
    },
    "华": {
        "forms": ["華", "hua", "wah", "wa"],
    },
    "钟": {
        "forms": ["鍾", "zhong", "chung", "tung", "tsong"],
        "dialects": {
            "chung": "hakka",
        },
    },
    "卢": {
        "forms": ["盧", "lu", "lo", "loh", "luu"],
        "dialects": {
            "lo": "cantonese",
            "loh": "hokkien",
        },
    },
    "汪": {
        "forms": ["ong"],
        "dialects": {
            "ong": "hokkien",
        },
    },
    "戴": {
        "forms": ["dai", "tai"],
    },
    "崔": {
        "forms": ["cui", "choi", "tsui"],
    },
    "任": {
        "forms": ["ren", "yam"],
    },
    "陆": {
        "forms": ["陸", "lu", "luk", "look"],
    },
    "廖": {
        "forms": ["liao", "lew", "liu"],
        "dialects": {
            "lew": "cantonese",
            "liu": "mandarin_pinyin",
        },
    },
    "姚": {
        "forms": ["yao", "yeu", "yiu"],
    },
    "方": {
        "forms": ["fang", "fong", "hong"],
        "dialects": {
            "fong": "cantonese",
        },
    },
    "金": {
        "forms": ["jin", "kim", "gim", "kam"],
    },
    "邱": {
        "forms": ["qiu", "khoo", "kew", "kiu"],
        "dialects": {
            "khoo": "hokkien",
        },
    },
    "谭": {
        "forms": ["譚", "tam", "tham"],
    },
    "韦": {
        "forms": ["wei", "wee"],
        "dialects": {
            "wee": "hokkien",
        },
    },
    "贾": {
        "forms": ["jia", "ka"],
    },
    "邹": {
        "forms": ["zou", "chow", "tsou"],
        "dialects": {
            "chow": "cantonese",
            "tsou": "wade_giles",
        },
    },
    "石": {
        "forms": ["shi", "shek"],
    },
    "熊": {
        "forms": ["xiong", "hung"],
    },
    "孟": {
        "forms": ["meng", "mang"],
    },
    "秦": {
        "forms": ["qin", "chin"],
        "dialects": {
            "chin": "hakka",
        },
    },
    "薛": {
        "forms": ["xue", "sit"],
    },
    "侯": {
        "forms": ["hou", "hau"],
    },
    "雷": {
        "forms": ["lei", "lui"],
        "dialects": {
            "lei": "cantonese",
        },
    },
    "白": {
        "forms": ["bai", "pak"],
    },
    "龙": {
        "forms": ["龍", "long", "loong", "lung"],
    },
    "段": {
        "forms": ["duan", "tuan"],
    },
    "郝": {
        "forms": ["hao", "hak"],
    },
    "孔": {
        "forms": ["kong", "hung"],
    },
    "邵": {
        "forms": ["shao", "shiu"],
    },
    "史": {
        "forms": ["shi", "see"],
        "dialects": {
            "see": "hokkien",
        },
    },
    "毛": {
        "forms": ["mao", "mo"],
    },
    "常": {
        "forms": ["chang", "seong"],
        "dialects": {
            "chang": "wade_giles",
        },
    },
    "万": {
        "forms": ["wan", "man"],
    },
    "顾": {
        "forms": ["gu", "ku"],
    },
    "赖": {
        "forms": ["lai", "lye"],
    },
    "武": {
        "forms": ["wu", "moo"],
        "dialects": {
            "wu": "mandarin_pinyin",
        },
    },
    "康": {
        "forms": ["kang", "hong"],
    },
    "贺": {
        "forms": ["he", "ho"],
    },
    "严": {
        "forms": ["yan", "yim", "ngeam"],
    },
    "尹": {
        "forms": ["yin", "wan"],
    },
    "钱": {
        "forms": ["錢", "qian", "chien", "chin"],
        "dialects": {
            "chien": "wade_giles",
            "chin": "hakka",
            "qian": "mandarin_pinyin",
        },
    },
    "施": {
        "forms": ["shi", "see", "si"],
        "dialects": {
            "see": "hokkien",
        },
    },
    "洪": {
        "forms": ["hong", "ang"],
        "dialects": {
            "ang": "hokkien",
        },
    },
    "龚": {
        "forms": ["gong", "kung"],
    },
    "姜": {
        "forms": ["jiang", "keong"],
        "dialects": {
            "jiang": "mandarin_pinyin",
        },
    },
    "范": {
        "forms": ["fan", "fam", "huan"],
    },
    "杜": {
        "forms": ["du", "to", "toh"],
    },
    "丁": {
        "forms": ["ding", "teng"],
    },
    "牛": {
        "forms": ["niu", "ngau"],
    },
    "翁": {
        "forms": ["weng", "yung", "ang"],
        "dialects": {
            "ang": "hokkien",
        },
    },
    "甘": {
        "forms": ["gan", "gam", "kam"],
    },
    "肖": {
        "forms": ["xiao", "siu"],
        "dialects": {
            "siu": "cantonese",
            "xiao": "mandarin_pinyin",
        },
    },
    "欧阳": {
        "forms": ["ouyang", "au-yeung"],
    },
    "司徒": {
        "forms": ["situ", "szeto", "sze-to"],
    },
    "诸葛": {
        "forms": ["zhuge", "chu-kot"],
    },
    "游": {
        "forms": ["you", "yau", "yu"],
    },
    "向": {
        "forms": ["xiang", "heung"],
    },
    "管": {
        "forms": ["guan", "koon"],
        "dialects": {
            "guan": "mandarin_pinyin",
        },
    },
    "文": {
        "forms": ["wen", "man", "mun"],
    },
    "岑": {
        "forms": ["cen", "sam", "sim"],
    },
    "麦": {
        "forms": ["mai", "mak"],
    },
    "章": {
        "forms": ["zhang", "cheung"],
        "dialects": {
            "cheung": "cantonese",
            "zhang": "mandarin_pinyin",
        },
    },
    "欧": {
        "forms": ["ou", "au"],
        "dialects": {
            "ou": "teochew",
        },
    },
    "项": {
        "forms": ["xiang", "hong"],
    },
    "祝": {
        "forms": ["zhu", "juk"],
        "dialects": {
            "zhu": "mandarin_pinyin",
        },
    },
    "封": {
        "forms": ["feng", "fung"],
        "dialects": {
            "feng": "mandarin_pinyin",
            "fung": "cantonese",
        },
    },
    "房": {
        "forms": ["fang", "fong"],
        "dialects": {
            "fong": "cantonese",
        },
    },
    "邢": {
        "forms": ["xing", "hing"],
    },
    "庄": {
        "forms": ["zhuang", "chong"],
        "dialects": {
            "chong": "hakka",
        },
    },
    "温": {
        "forms": ["wen", "wan", "wun"],
    },
    "花": {
        "forms": ["hua", "fa"],
    },
    "涂": {
        "forms": ["tu", "toh"],
    },
    "鲁": {
        "forms": ["lu", "lo"],
        "dialects": {
            "lo": "cantonese",
        },
    },
    "苟": {
        "forms": ["gou", "kau"],
    },
    "缪": {
        "forms": ["miao", "miu"],
    },
    "卓": {
        "forms": ["zhuo", "cheuk"],
    },
    "池": {
        "forms": ["chi", "chee"],
    },
    "凌": {
        "forms": ["ling", "leng"],
        "dialects": {
            "ling": "hakka",
        },
    },
    "桂": {
        "forms": ["gui", "kwai"],
    },
    "蒲": {
        "forms": ["pu", "po"],
    },
    "连": {
        "forms": ["lian", "lin"],
        "dialects": {
            "lin": "mandarin_pinyin",
        },
    },
    "柳": {
        "forms": ["liu", "lau"],
        "dialects": {
            "lau": "cantonese",
            "liu": "mandarin_pinyin",
        },
    },
    "司": {
        "forms": ["si", "see"],
        "dialects": {
            "see": "hokkien",
        },
    },
    "仇": {
        "forms": ["chou", "kau"],
        "dialects": {
            "chou": "wade_giles",
        },
    },
    "贝": {
        "forms": ["bei", "bui"],
    },
    "伍": {
        "forms": ["wu", "ng"],
        "dialects": {
            "ng": "cantonese",
            "wu": "mandarin_pinyin",
        },
    },
    "洗": {
        "forms": ["xian", "sin"],
    },
    "舒": {
        "forms": ["shu", "shoo"],
    },
    "商": {
        "forms": ["shang", "soeng"],
    },
    "關": {
        "forms": ["guan", "kwan", "kwaan", "关"],
        "dialects": {
            "guan": "mandarin_pinyin",
            "kwaan": "cantonese",
            "kwan": "cantonese",
            "关": "simplified",
        },
    },
}
