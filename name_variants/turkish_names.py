"""
Turkish name lookup: Turkish (Latin with diacritics) → ASCII variants.

Key problem: Turkish uses Latin script but with diacritics that are
routinely stripped in Western documents:
  Çelik → Celik
  Şahin → Sahin
  Yıldız → Yildiz
  Öztürk → Ozturk
  Güneş → Gunes

Also covers Ottoman-era Arabic-script names that were romanized differently
by different diaspora communities.

Sources:
  - Turkish Language Association (TDK) romanization
  - Common Turkish diaspora (Germany/UK/US) spelling patterns
  - ISO 233-3 for the diacritic mappings
"""

TURKISH_NAME_VARIANTS: dict[str, dict] = {
    "mehmet": {
        "forms": ["mehmet", "mehmed", "mahmoud"],
    },
    "mustafa": {
        "forms": ["mustafa", "mustaffa"],
    },
    "ahmet": {
        "forms": ["ahmet", "ahmed", "ahmad"],
    },
    "ali": {
        "forms": ["ali", "aly"],
    },
    "hüseyin": {
        "forms": ["huseyin", "husseyin", "husein"],
    },
    "hasan": {
        "forms": ["hasan", "hassan"],
    },
    "ibrahim": {
        "forms": ["ibrahim", "ebrahim"],
    },
    "ismail": {
        "forms": ["ismail", "esmail"],
    },
    "ömer": {
        "forms": ["omer", "umar"],
    },
    "süleyman": {
        "forms": ["suleyman", "suleiman", "souleyman"],
    },
    "yusuf": {
        "forms": ["yusuf", "yosef"],
    },
    "murat": {
        "forms": ["murat", "murad"],
    },
    "can": {
        "forms": ["can", "jan"],
    },
    "emre": {
        "forms": ["emre", "emree"],
    },
    "burak": {
        "forms": ["burak", "buurak"],
    },
    "cem": {
        "forms": ["cem", "gem", "ghem"],
    },
    "kemal": {
        "forms": ["kemal", "cemal"],
    },
    "tarık": {
        "forms": ["tarik", "tarig"],
    },
    "sercan": {
        "forms": ["sercan", "sirkan"],
    },
    "deniz": {
        "forms": ["deniz", "denees"],
    },
    "berk": {
        "forms": ["berk", "berg"],
    },
    "onur": {
        "forms": ["onur", "honor"],
    },
    "ufuk": {
        "forms": ["ufuk", "oufuk"],
    },
    "barış": {
        "forms": ["baris", "barish"],
    },
    "umut": {
        "forms": ["umut", "oomut"],
    },
    "güneş": {
        "forms": ["gunes", "gunesh"],
    },
    "kaan": {
        "forms": ["kaan", "kan"],
    },
    "tuğrul": {
        "forms": ["tugrul", "tughrul"],
    },
    "selçuk": {
        "forms": ["selcuk", "seldjuk"],
    },
    "oğuz": {
        "forms": ["oguz", "oghuz"],
    },
    "çağatay": {
        "forms": ["cagatay", "chagatai"],
    },
    "ayhan": {
        "forms": ["ayhan", "iyhan"],
    },
    "çelik": {
        "forms": ["celik", "chelik"],
    },
    "şahin": {
        "forms": ["sahin", "shahin"],
    },
    "yıldız": {
        "forms": ["yildiz", "yildis"],
    },
    "öztürk": {
        "forms": ["ozturk", "oezturk"],
    },
    "kaya": {
        "forms": ["kaya", "kayaa"],
    },
    "demir": {
        "forms": ["demir", "dimir"],
    },
    "doğan": {
        "forms": ["dogan", "doghan"],
    },
    "arslan": {
        "forms": ["arslan", "aslan"],
    },
    "aydın": {
        "forms": ["aydin", "aydeen"],
    },
    "özdemir": {
        "forms": ["ozdemir", "oezemir"],
    },
    "şimşek": {
        "forms": ["simsek", "shimsek"],
    },
    "güler": {
        "forms": ["guler", "gyuler"],
    },
    "çetin": {
        "forms": ["cetin", "chetin"],
    },
    "koç": {
        "forms": ["koc", "koch"],
    },
    "erdoğan": {
        "forms": ["erdogan", "erdoghan"],
    },
    "gündüz": {
        "forms": ["gunduz", "guenduz"],
    },
    "bulut": {
        "forms": ["bulut", "buloot"],
    },
    "aktaş": {
        "forms": ["aktas", "aktash"],
    },
    "yılmaz": {
        "forms": ["yilmaz", "yilmas"],
    },
    "polat": {
        "forms": ["polat", "polad"],
    },
    "fatma": {
        "forms": ["fatma"],
    },
    "ayşe": {
        "forms": ["ayse", "aysha", "aisha"],
    },
    "emine": {
        "forms": ["emine", "emina"],
    },
    "hatice": {
        "forms": ["hatice", "khatija"],
    },
    "zeynep": {
        "forms": ["zeynep", "zaynab"],
    },
    "elif": {
        "forms": ["elif", "eleef"],
    },
    "derya": {
        "forms": ["derya", "deria"],
    },
    "selin": {
        "forms": ["selin", "selen"],
    },
    "büşra": {
        "forms": ["busra", "bushra"],
    },
    "gül": {
        "forms": ["gul", "gull"],
    },
    "hülya": {
        "forms": ["hulya", "hoolya"],
    },
    "özlem": {
        "forms": ["ozlem", "ozzlem"],
    },
    "aslı": {
        "forms": ["asli", "usli"],
    },
    "nur": {
        "forms": ["nur", "nour"],
    },
    "şule": {
        "forms": ["sule", "shoole"],
    },
    "yeliz": {
        "forms": ["yeliz", "yelees"],
    },
    "filiz": {
        "forms": ["filiz", "filees"],
    },
    "esra": {
        "forms": ["esra", "esraa"],
    },
    "tuğba": {
        "forms": ["tugba", "tughba"],
    },
    "gamze": {
        "forms": ["gamze", "ghamze"],
    },
    "pınar": {
        "forms": ["pinar", "piner"],
    },
    "çiğdem": {
        "forms": ["cigdem", "chigdem"],
    },
}
