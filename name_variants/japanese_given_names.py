"""Japanese given-name romanization variants.

Canonical keys are kanji (single or compound) or katakana for kana-only names.
Variants are romanizations (lowercase).

Genuine romanization ambiguity is a feature: lookup() returns ALL matching
clusters.  Macron forms (ō, ū) and bare forms (o, u) coexist where applicable.
"""

JAPANESE_GIVEN_NAME_VARIANTS: dict[str, dict] = {
    '大翔': {
        "forms": ['hiroto', 'haruto', 'yamato'],
    },
    '悠真': {
        "forms": ['yuma'],
    },
    '蒼': {
        "forms": ['ao', 'sou'],
    },
    '湊': {
        "forms": ['minato'],
    },
    '律': {
        "forms": ['ritsu'],
    },
    '朝陽': {
        "forms": ['asahi'],
    },
    '樹': {
        "forms": ['itsuki', 'ki', 'tatsuki'],
    },
    '大和': {
        "forms": ['yamato'],
    },
    '颯': {
        "forms": ['sou', 'hayate'],
    },
    '竜': {
        "forms": ['tatsu'],
    },
    '健': {
        "forms": ['ken', 'takeshi'],
    },
    '誠': {
        "forms": ['makoto', 'sei'],
    },
    '翔': {
        "forms": ['sho', 'tsubasa', 'kakeru'],
    },
    '豊': {
        "forms": ['yutaka', 'toyo'],
    },
    '拓': {
        "forms": ['taku', 'hiroshi'],
    },
    '健太': {
        "forms": ['kenta'],
    },
    '雄太': {
        "forms": ['yuta'],
    },
    '次郎': {
        "forms": ['jiro'],
    },
    '三郎': {
        "forms": ['saburo'],
    },
    '太郎': {
        "forms": ['taro'],
    },
    '一郎': {
        "forms": ['ichiro'],
    },
    '慎': {
        "forms": ['makoto'],
    },
    '剛': {
        "forms": ['tsuyoshi'],
    },
    '豪': {
        "forms": ['takeshi'],
    },
    '進': {
        "forms": ['susumu'],
    },
    '徹': {
        "forms": ['toru', 'tetsu'],
    },
    '浩': {
        "forms": ['hiroshi'],
    },
    '弘': {
        "forms": ['hiroshi', 'hiro'],
    },
    '聡': {
        "forms": ['satoshi'],
    },
    '智': {
        "forms": ['satoshi', 'tomo'],
    },
    '勇': {
        "forms": ['isamu'],
    },
    '優': {
        "forms": ['masaru'],
    },
    '光': {
        "forms": ['hikaru', 'mitsu', 'kou'],
    },
    '輝': {
        "forms": ['hikaru', 'teru'],
    },
    '和': {
        "forms": ['kazu', 'nagi'],
    },
    '剣': {
        "forms": ['ken'],
    },
    '龍': {
        "forms": ['tatsu'],
    },
    '海': {
        "forms": ['kai', 'umi'],
    },
    '空': {
        "forms": ['sora'],
    },
    '葵': {
        "forms": ['aoi'],
    },
    '玲': {
        "forms": ['rei'],
    },
    '涼': {
        "forms": ['ryo', 'ryou'],
    },
    '颯太': {
        "forms": ['sota'],
    },
    '大輝': {
        "forms": ['daiki', 'taiki'],
    },
    '悠': {
        "forms": ['hisashi'],
    },
    '京': {
        "forms": ['kyo', 'miyako'],
    },
    '恵': {
        "forms": ['megumi', 'kei'],
    },
    '誉': {
        "forms": ['homare'],
    },
    '陽葵': {
        "forms": ['himari', 'hinata'],
    },
    '凛': {
        "forms": ['rin'],
    },
    '咲': {
        "forms": ['saki'],
    },
    '陽菜': {
        "forms": ['hina', 'haruna'],
    },
    '結菜': {
        "forms": ['yuna'],
    },
    '莉子': {
        "forms": ['riko'],
    },
    '芽依': {
        "forms": ['mei'],
    },
    '愛': {
        "forms": ['ai', 'megumi'],
    },
    '美咲': {
        "forms": ['misaki'],
    },
    '心春': {
        "forms": ['koharu'],
    },
    '結衣': {
        "forms": ['yui'],
    },
    '桜': {
        "forms": ['sakura'],
    },
    '花音': {
        "forms": ['kanon'],
    },
    '七海': {
        "forms": ['nanami'],
    },
    '彩': {
        "forms": ['aya', 'sai', 'iro'],
    },
    '華': {
        "forms": ['hana'],
    },
    '由美': {
        "forms": ['yumi'],
    },
    '明美': {
        "forms": ['akemi'],
    },
    '真由美': {
        "forms": ['mayumi'],
    },
    '亜希': {
        "forms": ['aki'],
    },
    '奈々': {
        "forms": ['nana'],
    },
    '里奈': {
        "forms": ['rina'],
    },
    '美穂': {
        "forms": ['miho'],
    },
    '千夏': {
        "forms": ['chinatsu'],
    },
    '沙織': {
        "forms": ['saori'],
    },
    '佳奈': {
        "forms": ['kana'],
    },
    '恵美': {
        "forms": ['emi'],
    },
    '奈緒': {
        "forms": ['nao'],
    },
    '亜矢': {
        "forms": ['aya'],
    },
    '圭': {
        "forms": ['kei'],
    },
    '奏': {
        "forms": ['kanade'],
    },
    '咲夜': {
        "forms": ['sakuya'],
    },
    '杏': {
        "forms": ['anzu'],
    },
    '澪': {
        "forms": ['mio'],
    },
    '瑠': {
        "forms": ['ru'],
    },
    '栞': {
        "forms": ['shiori'],
    },
    '朱': {
        "forms": ['ake'],
        "frequency": 14_900_000,
    },
    '夏': {
        "forms": ['natsu'],
    },
    '雪': {
        "forms": ['yuki', 'setsu'],
    },
    '月': {
        "forms": ['tsuki', 'getsu'],
    },
    '星': {
        "forms": ['hoshi', 'sei'],
    },
    '風': {
        "forms": ['kaze'],
    },
    '花': {
        "forms": ['hana'],
    },
    '雅': {
        "forms": ['masa', 'miyabi'],
    },
    '仁': {
        "forms": ['hitoshi'],
    },
    '高太郎': {
        "forms": ['kotaro'],
    },
    '五郎': {
        "forms": ['goro'],
    },
    '四郎': {
        "forms": ['shiro'],
    },
    'ケンジ': {
        "forms": ['kenji'],
    },
    'ユキ': {
        "forms": ['yuki'],
    },
    'リョウ': {
        "forms": ['ryo'],
    },
    'ハルト': {
        "forms": ['haruto'],
    },
    'ソウタ': {
        "forms": ['sota'],
    },
    'イツキ': {
        "forms": ['itsuki'],
    },
    'アオイ': {
        "forms": ['aoi'],
    },
    'コトネ': {
        "forms": ['kotone'],
    },
    'ヒカル': {
        "forms": ['hikaru'],
    },
    'ナオミ': {
        "forms": ['naomi'],
    },
    'マイ': {
        "forms": ['mai'],
    },
}
