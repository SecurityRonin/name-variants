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

TURKISH_NAME_VARIANTS: dict[str, list[str]] = {
    # ── Male given names ─────────────────────────────────────────────────────
    "mehmet": ["mehmet", "mehmed", "mahmoud"],
    "mustafa": ["mustafa", "mustaffa"],
    "ahmet": ["ahmet", "ahmed", "ahmad"],
    "ali": ["ali", "aly"],
    "hüseyin": ["huseyin", "husseyin", "husein"],
    "hasan": ["hasan", "hassan"],
    "ibrahim": ["ibrahim", "ebrahim"],
    "ismail": ["ismail", "esmail"],
    "ömer": ["omer", "umar"],
    "süleyman": ["suleyman", "suleiman", "souleyman"],
    "yusuf": ["yusuf", "yosef"],
    "murat": ["murat", "murad"],
    "can": ["can", "jan"],
    "emre": ["emre", "emree"],
    "burak": ["burak", "buurak"],
    "cem": ["cem", "gem", "ghem"],
    "kemal": ["kemal", "cemal"],
    "tarık": ["tarik", "tarig"],
    "sercan": ["sercan", "sirkan"],
    "deniz": ["deniz", "denees"],
    "berk": ["berk", "berg"],
    "onur": ["onur", "honor"],
    "ufuk": ["ufuk", "oufuk"],
    "barış": ["baris", "barish"],
    "umut": ["umut", "oomut"],
    "güneş": ["gunes", "gunesh"],
    "kaan": ["kaan", "kan"],
    "tuğrul": ["tugrul", "tughrul"],
    "selçuk": ["selcuk", "seldjuk"],
    "oğuz": ["oguz", "oghuz"],
    "çağatay": ["cagatay", "chagatai"],
    "ayhan": ["ayhan", "iyhan"],
    # ── Male surnames (with diacritic variants) ──────────────────────────────
    "çelik": ["celik", "chelik"],
    "şahin": ["sahin", "shahin"],
    "yıldız": ["yildiz", "yildis"],
    "öztürk": ["ozturk", "oezturk"],
    "kaya": ["kaya", "kayaa"],
    "demir": ["demir", "dimir"],
    "doğan": ["dogan", "doghan"],
    "arslan": ["arslan", "aslan"],
    "aydın": ["aydin", "aydeen"],
    "özdemir": ["ozdemir", "oezemir"],
    "şimşek": ["simsek", "shimsek"],
    "güler": ["guler", "gyuler"],
    "çetin": ["cetin", "chetin"],
    "koç": ["koc", "koch"],
    "erdoğan": ["erdogan", "erdoghan"],
    "gündüz": ["gunduz", "guenduz"],
    "bulut": ["bulut", "buloot"],
    "aktaş": ["aktas", "aktash"],
    "yılmaz": ["yilmaz", "yilmas"],
    "polat": ["polat", "polad"],
    # ── Female given names ────────────────────────────────────────────────────
    "fatma": ["fatma"],
    "ayşe": ["ayse", "aysha", "aisha"],
    "emine": ["emine", "emina"],
    "hatice": ["hatice", "khatija"],
    "zeynep": ["zeynep", "zaynab"],
    "elif": ["elif", "eleef"],
    "derya": ["derya", "deria"],
    "selin": ["selin", "selen"],
    "büşra": ["busra", "bushra"],
    "gül": ["gul", "gull"],
    "hülya": ["hulya", "hoolya"],
    "özlem": ["ozlem", "ozzlem"],
    "aslı": ["asli", "usli"],
    "nur": ["nur", "nour"],
    "şule": ["sule", "shoole"],
    "yeliz": ["yeliz", "yelees"],
    "filiz": ["filiz", "filees"],
    "esra": ["esra", "esraa"],
    "tuğba": ["tugba", "tughba"],
    "gamze": ["gamze", "ghamze"],
    "pınar": ["pinar", "piner"],
    "çiğdem": ["cigdem", "chigdem"],
}
