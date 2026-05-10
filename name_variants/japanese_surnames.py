"""
Japanese surname lookup: kanji → Hepburn romanization variants.
Standard Hepburn + modified variants (ou/o/oh, uu/u, etc.).

Sources:
  - MEXT romanization guidelines
  - Hepburn standard (ALA-LC) + common Western variants
"""

JAPANESE_SURNAME_VARIANTS: dict[str, dict] = {
    '佐藤': {
        "forms": ['sato', 'satou', 'satoh', 'satō'],
        "frequency": 1_928_000,
    },
    '鈴木': {
        "forms": ['suzuki'],
        "frequency": 1_806_000,
    },
    '高橋': {
        "forms": ['takahashi'],
        "frequency": 1_421_000,
    },
    '田中': {
        "forms": ['tanaka'],
        "frequency": 1_336_000,
    },
    '伊藤': {
        "forms": ['ito', 'itou', 'itoh'],
        "frequency": 1_085_000,
    },
    '渡辺': {
        "forms": ['watanabe'],
        "frequency": 1_083_000,
    },
    '山本': {
        "forms": ['yamamoto'],
        "frequency": 1_050_000,
    },
    '中村': {
        "forms": ['nakamura'],
        "frequency": 1_033_000,
    },
    '小林': {
        "forms": ['kobayashi'],
        "frequency": 1_011_000,
    },
    '加藤': {
        "forms": ['kato', 'katou', 'katoh'],
        "frequency": 888_000,
    },
    '吉田': {
        "forms": ['yoshida'],
        "frequency": 863_000,
    },
    '山田': {
        "forms": ['yamada'],
        "frequency": 838_000,
    },
    '佐々木': {
        "forms": ['sasaki'],
        "frequency": 680_000,
    },
    '山口': {
        "forms": ['yamaguchi'],
        "frequency": 659_000,
    },
    '松本': {
        "forms": ['matsumoto'],
        "frequency": 638_000,
    },
    '井上': {
        "forms": ['inoue', 'inouye'],
    },
    '木村': {
        "forms": ['kimura'],
    },
    '林': {
        "forms": ['hayashi'],
        "frequency": 18_700_000,
    },
    '斎藤': {
        "forms": ['saito', 'saitou', 'saitoh'],
    },
    '清水': {
        "forms": ['shimizu'],
    },
    '池田': {
        "forms": ['ikeda'],
    },
    '橋本': {
        "forms": ['hashimoto'],
    },
    '阿部': {
        "forms": ['abe'],
    },
    '森': {
        "forms": ['mori'],
    },
    '石川': {
        "forms": ['ishikawa'],
    },
    '山崎': {
        "forms": ['yamazaki', 'yamasaki'],
    },
    '前田': {
        "forms": ['maeda'],
    },
    '岡田': {
        "forms": ['okada'],
    },
    '長谷川': {
        "forms": ['hasegawa'],
    },
    '藤田': {
        "forms": ['fujita'],
    },
    '近藤': {
        "forms": ['kondo', 'kondou', 'kondoh'],
    },
    '石田': {
        "forms": ['ishida'],
    },
    '後藤': {
        "forms": ['goto', 'gotou', 'gotoh'],
    },
    '村上': {
        "forms": ['murakami'],
    },
    '坂本': {
        "forms": ['sakamoto'],
    },
    '遠藤': {
        "forms": ['endo', 'endou', 'endoh'],
    },
    '青木': {
        "forms": ['aoki'],
    },
    '藤井': {
        "forms": ['fujii'],
    },
    '西村': {
        "forms": ['nishimura'],
    },
    '福田': {
        "forms": ['fukuda'],
    },
    '太田': {
        "forms": ['ota', 'ohta', 'oota'],
    },
    '三浦': {
        "forms": ['miura'],
    },
    '岡本': {
        "forms": ['okamoto'],
    },
    '松田': {
        "forms": ['matsuda'],
    },
    '中島': {
        "forms": ['nakajima', 'nakashima'],
    },
    '浜田': {
        "forms": ['hamada'],
    },
    '藤原': {
        "forms": ['fujiwara'],
    },
    '小川': {
        "forms": ['ogawa'],
    },
    '中田': {
        "forms": ['nakata', 'nakada'],
    },
    '上田': {
        "forms": ['ueda'],
    },
    '原田': {
        "forms": ['harada'],
    },
    '野口': {
        "forms": ['noguchi'],
    },
    '今井': {
        "forms": ['imai'],
    },
    '川口': {
        "forms": ['kawaguchi'],
    },
    '千葉': {
        "forms": ['chiba'],
    },
    '内田': {
        "forms": ['uchida'],
    },
    '大野': {
        "forms": ['ohno', 'ono'],
    },
    '西田': {
        "forms": ['nishida'],
    },
    '河野': {
        "forms": ['kono', 'kawano'],
    },
    '武田': {
        "forms": ['takeda'],
    },
    '金子': {
        "forms": ['kaneko'],
    },
    '中野': {
        "forms": ['nakano'],
    },
    '杉山': {
        "forms": ['sugiyama'],
    },
    '石原': {
        "forms": ['ishihara'],
    },
    '宮崎': {
        "forms": ['miyazaki'],
    },
    '山下': {
        "forms": ['yamashita'],
    },
    '大塚': {
        "forms": ['otsuka'],
    },
    '岩崎': {
        "forms": ['iwasaki'],
    },
    '広瀬': {
        "forms": ['hirose'],
    },
    '横山': {
        "forms": ['yokoyama'],
    },
    '辻': {
        "forms": ['tsuji'],
    },
    '菊地': {
        "forms": ['kikuchi'],
    },
    '佐野': {
        "forms": ['sano'],
    },
    '丸山': {
        "forms": ['maruyama'],
    },
    '樋口': {
        "forms": ['higuchi'],
    },
    '岩田': {
        "forms": ['iwata'],
    },
    '村田': {
        "forms": ['murata'],
    },
    '久保': {
        "forms": ['kubo'],
    },
    '上野': {
        "forms": ['ueno'],
    },
    '野村': {
        "forms": ['nomura'],
    },
    '藤本': {
        "forms": ['fujimoto'],
    },
    '古川': {
        "forms": ['furukawa'],
    },
    '平野': {
        "forms": ['hirano'],
    },
    '大久保': {
        "forms": ['okubo'],
    },
    '田村': {
        "forms": ['tamura'],
    },
    '中山': {
        "forms": ['nakayama'],
    },
    '水野': {
        "forms": ['mizuno'],
    },
    '西川': {
        "forms": ['nishikawa'],
    },
    '服部': {
        "forms": ['hattori'],
    },
    '黒田': {
        "forms": ['kuroda'],
    },
    '谷口': {
        "forms": ['taniguchi'],
    },
    '篠原': {
        "forms": ['shinohara'],
    },
    '北村': {
        "forms": ['kitamura'],
    },
    '栗原': {
        "forms": ['kurihara'],
    },
    '大西': {
        "forms": ['onishi'],
    },
    '木下': {
        "forms": ['kinoshita'],
    },
    '安田': {
        "forms": ['yasuda'],
    },
    '田口': {
        "forms": ['taguchi'],
    },
    '小野': {
        "forms": ['ono'],
    },
    '松井': {
        "forms": ['matsui'],
    },
    '山内': {
        "forms": ['yamauchi'],
    },
    '平田': {
        "forms": ['hirata'],
    },
    '川村': {
        "forms": ['kawamura'],
    },
    '本田': {
        "forms": ['honda'],
    },
    '高田': {
        "forms": ['takada', 'takata'],
    },
    '竹内': {
        "forms": ['takeuchi'],
    },
    '秋山': {
        "forms": ['akiyama'],
    },
    '富田': {
        "forms": ['tomita'],
    },
    '石井': {
        "forms": ['ishii'],
    },
    '宮田': {
        "forms": ['miyata'],
    },
    '浅野': {
        "forms": ['asano'],
    },
    '松尾': {
        "forms": ['matsuo'],
    },
    '安藤': {
        "forms": ['ando', 'andou'],
    },
    '関': {
        "forms": ['seki'],
    },
    '奥田': {
        "forms": ['okuda'],
    },
    '横田': {
        "forms": ['yokota'],
    },
    '矢野': {
        "forms": ['yano'],
    },
    '神田': {
        "forms": ['kanda'],
    },
    '沼田': {
        "forms": ['numata'],
    },
    '中川': {
        "forms": ['nakagawa'],
    },
    '藤沢': {
        "forms": ['fujisawa'],
    },
    '小松': {
        "forms": ['komatsu'],
    },
    '内山': {
        "forms": ['uchiyama'],
    },
    '高山': {
        "forms": ['takayama'],
    },
    '早川': {
        "forms": ['hayakawa'],
    },
    '永田': {
        "forms": ['nagata'],
    },
    '川上': {
        "forms": ['kawakami'],
    },
    '岡村': {
        "forms": ['okamura'],
    },
    '野田': {
        "forms": ['noda'],
    },
    '三宅': {
        "forms": ['miyake'],
    },
    '牧': {
        "forms": ['maki'],
    },
    '長島': {
        "forms": ['nagashima'],
    },
    '渡部': {
        "forms": ['watabe'],
    },
    '坂田': {
        "forms": ['sakata'],
    },
    '岸': {
        "forms": ['kishi'],
    },
    '菅': {
        "forms": ['suga', 'kan'],
    },
    '麻生': {
        "forms": ['aso'],
    },
    '小泉': {
        "forms": ['koizumi'],
    },
    '安倍': {
        "forms": ['abe'],
    },
    '鳩山': {
        "forms": ['hatoyama'],
    },
    '細川': {
        "forms": ['hosokawa'],
    },
    '竹下': {
        "forms": ['takeshita'],
    },
    '中曽根': {
        "forms": ['nakasone'],
    },
}
