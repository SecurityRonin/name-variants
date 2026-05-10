"""
Hebrew name lookup: Hebrew script → romanization variants.

Key problem: Hebrew romanization has no single standard in common use.
Biblical names have English cognates (יצחק → Isaac/Yitzhak/Yitzchak),
modern Israeli names have ALA-LC and informal variants.

Also covers Ashkenazi vs. Sephardic pronunciation differences:
  שבת → Shabbat (Ashkenazi) / Shabbath / Shabat

Sources:
  - ALA-LC Hebrew romanization
  - Academy of the Hebrew Language transliteration guidelines
  - Common diaspora (US/UK/HK) and biblical English variants
"""

HEBREW_NAME_VARIANTS: dict[str, dict] = {
    "יצחק": {
        "forms": ["yitzhak", "yitzchak", "isaac", "izak", "yizhak"],
    },
    "משה": {
        "forms": ["moshe", "moses", "moishe"],
    },
    "אברהם": {
        "forms": ["avraham", "abraham", "avrahim"],
    },
    "יוסף": {
        "forms": ["yosef", "joseph", "yossef"],
    },
    "דוד": {
        "forms": ["david", "daveed", "davyd"],
    },
    "יעקב": {
        "forms": ["yaakov", "jacob", "jakob"],
    },
    "אהרון": {
        "forms": ["aaron", "aharon", "aron"],
    },
    "שמואל": {
        "forms": ["shmuel", "samuel", "schmuel"],
    },
    "בנימין": {
        "forms": ["binyamin", "benjamin", "benyamin"],
    },
    "שלמה": {
        "forms": ["shlomo", "solomon", "shlomoh"],
    },
    "חיים": {
        "forms": ["chaim", "haim", "hayim", "hayyim"],
    },
    "מנחם": {
        "forms": ["menachem", "menahem", "menakhem"],
    },
    "אריה": {
        "forms": ["aryeh", "arye", "arie"],
    },
    "אליעזר": {
        "forms": ["eliezer", "eleazar", "eliazar"],
    },
    "זאב": {
        "forms": ["zeev", "zev", "ze'ev"],
    },
    "נחמן": {
        "forms": ["nachman", "nahman"],
    },
    "ברוך": {
        "forms": ["baruch", "boruch", "barukh"],
    },
    "פינחס": {
        "forms": ["pinchas", "phinehas", "pinhas"],
    },
    "גדליה": {
        "forms": ["gedaliah", "gedalya"],
    },
    "ישראל": {
        "forms": ["israel", "yisrael", "yisra'el"],
    },
    "נתן": {
        "forms": ["natan", "nathan"],
    },
    "אלי": {
        "forms": ["eli", "elie", "ely"],
    },
    "גיל": {
        "forms": ["gil", "geel"],
    },
    "עמיר": {
        "forms": ["amir", "ameer"],
    },
    "רון": {
        "forms": ["ron", "ronn"],
    },
    "אייל": {
        "forms": ["eyal", "ayyal"],
    },
    "ניר": {
        "forms": ["nir", "neer"],
    },
    "ידין": {
        "forms": ["yadin", "yaadin"],
    },
    "עמוס": {
        "forms": ["amos", "amoss"],
    },
    "יגאל": {
        "forms": ["yigal", "yigael"],
    },
    "אביגדור": {
        "forms": ["avigdor", "avigdore"],
    },
    "צבי": {
        "forms": ["tzvi", "zvi", "tsvi"],
    },
    "אחיעזר": {
        "forms": ["achiezer", "ahi'ezer"],
    },
    "מתתיהו": {
        "forms": ["mattityahu", "matthias", "matityahu"],
    },
    "עקיבא": {
        "forms": ["akiva", "aqiva"],
    },
    "שמעון": {
        "forms": ["shimon", "simeon", "simon"],
    },
    "לוי": {
        "forms": ["levi", "levy"],
    },
    "ראובן": {
        "forms": ["reuven", "reuben", "ruben"],
    },
    "יהודה": {
        "forms": ["yehuda", "judah", "yehudah"],
    },
    "גדעון": {
        "forms": ["gideon", "gidon"],
    },
    "אלדד": {
        "forms": ["eldad", "eldaad"],
    },
    "שרה": {
        "forms": ["sarah", "sara"],
    },
    "רבקה": {
        "forms": ["rivka", "rebekah", "rebecca"],
    },
    "רחל": {
        "forms": ["rachel", "rahel"],
    },
    "לאה": {
        "forms": ["leah", "lea"],
    },
    "מרים": {
        "forms": ["miriam", "maryam"],
    },
    "דינה": {
        "forms": ["dinah", "dina"],
    },
    "תמר": {
        "forms": ["tamar", "tamara"],
    },
    "דבורה": {
        "forms": ["devorah", "deborah", "dvora"],
    },
    "חנה": {
        "forms": ["hanna", "hannah", "chana"],
    },
    "שולמית": {
        "forms": ["shulamit", "shulamith"],
    },
    "ציפורה": {
        "forms": ["tzipora", "zipporah", "tsippora"],
    },
    "נעמי": {
        "forms": ["naomi", "no'omi"],
    },
    "אסתר": {
        "forms": ["esther", "ester"],
    },
    "רות": {
        "forms": ["ruth", "rut"],
    },
    "יעל": {
        "forms": ["yael", "jael"],
    },
    "גלית": {
        "forms": ["galit", "galeet"],
    },
    "עינת": {
        "forms": ["einat", "aynat"],
    },
    "רוני": {
        "forms": ["roni", "ronni"],
    },
    "טלי": {
        "forms": ["tali", "talee"],
    },
    "מיכל": {
        "forms": ["michal", "mickel"],
    },
    "שירה": {
        "forms": ["shira", "sheerah"],
    },
    "יפה": {
        "forms": ["yafa", "jaffa"],
    },
    "ענת": {
        "forms": ["anat", "anath"],
    },
    "נילי": {
        "forms": ["nili", "neeli"],
    },
    "אורית": {
        "forms": ["orit", "oreet"],
    },
    "דליה": {
        "forms": ["dalia", "dalya"],
    },
    "ליאת": {
        "forms": ["liat", "lyat"],
    },
    "שני": {
        "forms": ["shani", "shaani"],
    },
    "אלינור": {
        "forms": ["elinor", "eleanor"],
    },
    "נעה": {
        "forms": ["noa", "no'a"],
    },
    "כהן": {
        "forms": ["cohen", "kohen", "kohn", "cohn"],
    },
    "מזרחי": {
        "forms": ["mizrahi", "mizrachi"],
    },
    "פרץ": {
        "forms": ["peretz", "perets", "peres"],
    },
    "שפירא": {
        "forms": ["shapira", "shapiro", "schapiro"],
    },
}
