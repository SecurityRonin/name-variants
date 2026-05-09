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

HEBREW_NAME_VARIANTS: dict[str, list[str]] = {
    # ── Male given names ─────────────────────────────────────────────────────
    "יצחק": ["yitzhak", "yitzchak", "isaac", "izak", "yizhak"],
    "משה": ["moshe", "moses", "moishe"],
    "אברהם": ["avraham", "abraham", "avrahim"],
    "יוסף": ["yosef", "joseph", "yossef"],
    "דוד": ["david", "daveed", "davyd"],
    "יעקב": ["yaakov", "jacob", "jakob"],
    "אהרון": ["aaron", "aharon", "aron"],
    "שמואל": ["shmuel", "samuel", "schmuel"],
    "בנימין": ["binyamin", "benjamin", "benyamin"],
    "שלמה": ["shlomo", "solomon", "shlomoh"],
    "חיים": ["chaim", "haim", "hayim", "hayyim"],
    "מנחם": ["menachem", "menahem", "menakhem"],
    "אריה": ["aryeh", "arye", "arie"],
    "אליעזר": ["eliezer", "eleazar", "eliazar"],
    "זאב": ["zeev", "zev", "ze'ev"],
    "נחמן": ["nachman", "nahman"],
    "ברוך": ["baruch", "boruch", "barukh"],
    "פינחס": ["pinchas", "phinehas", "pinhas"],
    "גדליה": ["gedaliah", "gedalya"],
    "ישראל": ["israel", "yisrael", "yisra'el"],
    "נתן": ["natan", "nathan"],
    "אלי": ["eli", "elie", "ely"],
    "גיל": ["gil", "geel"],
    "עמיר": ["amir", "ameer"],
    "רון": ["ron", "ronn"],
    "אייל": ["eyal", "ayyal"],
    "ניר": ["nir", "neer"],
    "ידין": ["yadin", "yaadin"],
    "עמוס": ["amos", "amoss"],
    "יגאל": ["yigal", "yigael"],
    "אביגדור": ["avigdor", "avigdore"],
    "צבי": ["tzvi", "zvi", "tsvi"],
    "אחיעזר": ["achiezer", "ahi'ezer"],
    "מתתיהו": ["mattityahu", "matthias", "matityahu"],
    "עקיבא": ["akiva", "aqiva"],
    "שמעון": ["shimon", "simeon", "simon"],
    "לוי": ["levi", "levy"],
    "ראובן": ["reuven", "reuben", "ruben"],
    "יהודה": ["yehuda", "judah", "yehudah"],
    "גדעון": ["gideon", "gidon"],
    "אלדד": ["eldad", "eldaad"],
    # ── Female given names ───────────────────────────────────────────────────
    "שרה": ["sarah", "sara"],
    "רבקה": ["rivka", "rebekah", "rebecca"],
    "רחל": ["rachel", "rahel"],
    "לאה": ["leah", "lea"],
    "מרים": ["miriam", "maryam"],
    "דינה": ["dinah", "dina"],
    "תמר": ["tamar", "tamara"],
    "דבורה": ["devorah", "deborah", "dvora"],
    "חנה": ["hanna", "hannah", "chana"],
    "שולמית": ["shulamit", "shulamith"],
    "ציפורה": ["tzipora", "zipporah", "tsippora"],
    "נעמי": ["naomi", "no'omi"],
    "אסתר": ["esther", "ester"],
    "רות": ["ruth", "rut"],
    "יעל": ["yael", "jael"],
    "גלית": ["galit", "galeet"],
    "עינת": ["einat", "aynat"],
    "רוני": ["roni", "ronni"],
    "טלי": ["tali", "talee"],
    "מיכל": ["michal", "mickel"],
    "שירה": ["shira", "sheerah"],
    "יפה": ["yafa", "jaffa"],
    "ענת": ["anat", "anath"],
    "נילי": ["nili", "neeli"],
    "אורית": ["orit", "oreet"],
    "דליה": ["dalia", "dalya"],
    "ליאת": ["liat", "lyat"],
    "שני": ["shani", "shaani"],
    "אלינור": ["elinor", "eleanor"],
    "נעה": ["noa", "no'a"],
    # ── Common surnames ───────────────────────────────────────────────────────
    "כהן": ["cohen", "kohen", "kohn", "cohn"],
    "מזרחי": ["mizrahi", "mizrachi"],
    "פרץ": ["peretz", "perets", "peres"],
    "שפירא": ["shapira", "shapiro", "schapiro"],
}
