"""Chinese given-name romanization variants.

Canonical keys are Simplified Chinese characters.
Variants are romanizations (lowercase, with and without tone marks).

Genuine romanization ambiguity is a feature: lookup() returns ALL matching
clusters.  Both bare and tonal pinyin forms are included.
"""

CHINESE_GIVEN_NAME_VARIANTS: dict[str, dict] = {
    "明": {
        "forms": ["ming", "míng"],
    },
    "文": {
        "forms": ["wen", "wén"],
    },
    "伟": {
        "forms": ["wei", "wěi"],
    },
    "强": {
        "forms": ["qiang", "qiáng"],
    },
    "军": {
        "forms": ["jun", "jūn"],
    },
    "杰": {
        "forms": ["jie", "jié"],
    },
    "勇": {
        "forms": ["yong", "yǒng"],
    },
    "涛": {
        "forms": ["tao", "tāo"],
    },
    "志": {
        "forms": ["zhi", "zhì"],
    },
    "超": {
        "forms": ["chao", "chāo"],
    },
    "刚": {
        "forms": ["gang", "gāng"],
    },
    "磊": {
        "forms": ["lei", "lěi"],
    },
    "鑫": {
        "forms": ["xin", "xīn"],
    },
    "健": {
        "forms": ["jian", "jiàn"],
    },
    "博": {
        "forms": ["bo", "bó"],
    },
    "辉": {
        "forms": ["hui", "huī"],
    },
    "浩": {
        "forms": ["hao", "hào"],
    },
    "飞": {
        "forms": ["fei", "fēi"],
    },
    "亮": {
        "forms": ["liang", "liàng"],
    },
    "帅": {
        "forms": ["shuai", "shuài"],
    },
    "龙": {
        "forms": ["long", "lóng"],
    },
    "武": {
        "forms": ["wu", "wǔ"],
    },
    "斌": {
        "forms": ["bin", "bīn"],
    },
    "峰": {
        "forms": ["feng", "fēng"],
    },
    "海": {
        "forms": ["hǎi"],
    },
    "锋": {
        "forms": ["feng", "fèng"],
    },
    "宇": {
        "forms": ["yu", "yǔ"],
    },
    "昊": {
        "forms": ["hao", "háo"],
    },
    "翔": {
        "forms": ["xiang", "xiáng"],
    },
    "凯": {
        "forms": ["kai", "kǎi"],
    },
    "晨": {
        "forms": ["chen", "chén"],
    },
    "泽": {
        "forms": ["ze", "zé"],
    },
    "轩": {
        "forms": ["xuan", "xuān"],
    },
    "炀": {
        "forms": ["yang", "yáng"],
    },
    "睿": {
        "forms": ["rui", "ruì"],
    },
    "鹏": {
        "forms": ["peng", "péng"],
    },
    "坤": {
        "forms": ["kun", "kūn"],
    },
    "东": {
        "forms": ["dong", "dōng"],
    },
    "旭": {
        "forms": ["xu", "xù"],
    },
    "芳": {
        "forms": ["fang", "fāng"],
    },
    "燕": {
        "forms": ["yan", "yàn"],
    },
    "娟": {
        "forms": ["juan", "juān"],
    },
    "艳": {
        "forms": ["yan", "yàn"],
    },
    "霞": {
        "forms": ["xia", "xiá"],
    },
    "萍": {
        "forms": ["ping", "píng"],
    },
    "丽": {
        "forms": ["li", "lì"],
    },
    "英": {
        "forms": ["ying", "yīng"],
    },
    "静": {
        "forms": ["jing", "jìng"],
    },
    "玲": {
        "forms": ["ling", "líng"],
    },
    "秀": {
        "forms": ["xiu", "xiù"],
    },
    "梅": {
        "forms": ["mei", "méi"],
    },
    "敏": {
        "forms": ["min", "mǐn"],
    },
    "雪": {
        "forms": ["xue", "xuě"],
    },
    "雅": {
        "forms": ["ya", "yǎ"],
    },
    "婷": {
        "forms": ["ting", "tíng"],
    },
    "欣": {
        "forms": ["xin", "xīn"],
    },
    "晶": {
        "forms": ["jing", "jīng"],
    },
    "慧": {
        "forms": ["hui", "huì"],
    },
    "薇": {
        "forms": ["wei", "wēi"],
    },
    "琳": {
        "forms": ["lin", "lín"],
    },
    "莹": {
        "forms": ["ying", "yíng"],
    },
    "佳": {
        "forms": ["jiā"],
    },
    "倩": {
        "forms": ["qian", "qiàn"],
    },
    "洁": {
        "forms": ["jié"],
    },
    "颖": {
        "forms": ["ying", "yǐng"],
    },
    "蕾": {
        "forms": ["lei", "lěi"],
    },
    "璐": {
        "forms": ["lu", "lù"],
    },
    "嘉": {
        "forms": ["jiā"],
    },
    "蓉": {
        "forms": ["rong", "róng"],
    },
    "珊": {
        "forms": ["shan", "shān"],
    },
    "琪": {
        "forms": ["qi", "qí"],
    },
    "晴": {
        "forms": ["qing", "qíng"],
    },
    "菊": {
        "forms": ["ju", "jú"],
    },
    "凤": {
        "forms": ["feng", "fèng"],
    },
    "兰": {
        "forms": ["lan", "lán"],
    },
    "红": {
        "forms": ["hong", "hóng"],
    },
    "春": {
        "forms": ["chun", "chūn"],
    },
    "桂": {
        "forms": ["gui", "guì"],
    },
    "淑": {
        "forms": ["shu", "shū"],
    },
    "香": {
        "forms": ["xiang", "xiāng"],
    },
    "萱": {
        "forms": ["xuan", "xuān"],
    },
    "彤": {
        "forms": ["tong", "tóng"],
    },
    "悦": {
        "forms": ["yue", "yuè"],
    },
    "华": {
        "forms": ["hua", "huá"],
    },
    "阳": {
        "forms": ["yang", "yáng"],
    },
    "洋": {
        "forms": ["yang", "yáng"],
    },
    "扬": {
        "forms": ["yang", "yáng"],
    },
    "晓": {
        "forms": ["xiao", "xiǎo"],
    },
    "子": {
        "forms": ["zi", "zǐ"],
    },
    "天": {
        "forms": ["tian", "tiān"],
    },
    "心": {
        "forms": ["xin", "xīn"],
    },
    "云": {
        "forms": ["yun", "yún"],
    },
    "思": {
        "forms": ["si", "sī"],
    },
    "宁": {
        "forms": ["ning", "níng"],
    },
    "安": {
        "forms": ["an", "ān"],
    },
    "乐": {
        "forms": ["le", "lè"],
    },
    "诚": {
        "forms": ["cheng", "chéng"],
    },
    "灿": {
        "forms": ["can", "càn"],
    },
    "青": {
        "forms": ["qing", "qīng"],
    },
    "然": {
        "forms": ["ran", "rán"],
    },
    "奇": {
        "forms": ["qi", "qí"],
    },
    "远": {
        "forms": ["yuan", "yuǎn"],
    },
    "畅": {
        "forms": ["chang", "chàng"],
    },
    "康": {
        "forms": ["kang", "kāng"],
    },
    "成": {
        "forms": ["cheng", "chéng"],
    },
    "林": {
        "forms": ["lin", "lín"],
        "frequency": 18_700_000,
    },
    "建": {
        "forms": ["jian", "jiàn"],
    },
    "国": {
        "forms": ["guo", "guó"],
    },
    "平": {
        "forms": ["ping", "píng"],
    },
    "新": {
        "forms": ["xin", "xīn"],
    },
    "向": {
        "forms": ["xiang", "xiàng"],
    },
    "光": {
        "forms": ["guang", "guāng"],
    },
    "利": {
        "forms": ["li", "lì"],
    },
    "德": {
        "forms": ["de", "dé"],
    },
    "继": {
        "forms": ["ji", "jì"],
    },
    "仁": {
        "forms": ["ren", "rén"],
    },
    "义": {
        "forms": ["yi", "yì"],
    },
    "礼": {
        "forms": ["li", "lǐ"],
    },
    "信": {
        "forms": ["xin", "xìn"],
    },
    "智": {
        "forms": ["zhi", "zhì"],
    },
}
