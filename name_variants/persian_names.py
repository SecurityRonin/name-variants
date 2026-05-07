"""
Persian/Farsi name lookup: Persian script → romanization variants.

Key problem: Persian uses the Arabic script but different pronunciation,
creating variants distinct from the Arabic name table:
  حسین → Hossein (Persian) vs. Hussein (Arabic)
  محمد → Mohammad (Persian) vs. Muhammad (Arabic)
  رضا → Reza (standard) / Rizza / Ridha (Arabic-influenced)

Also covers overlapping Iranian diaspora patterns (UK/US/HK):
  Shahram / Shahram, Fereydoon / Fereydoun / Faridon

Sources:
  - ALA-LC Persian romanization standard
  - DMG (Deutsche Morgenländische Gesellschaft) — common in academic contexts
  - Common Iranian diaspora (UK/US/Canada) spellings
"""

PERSIAN_NAME_VARIANTS: dict[str, list[str]] = {
    # ── Male given names ─────────────────────────────────────────────────────
    "محمد": ["mohammad", "muhammad", "mohammed", "mohamed", "mohamad"],
    "علی": ["ali", "aly"],
    "حسین": ["hossein", "hussein", "husain", "hosein"],
    "رضا": ["reza", "riza", "ridha", "reda"],
    "احمد": ["ahmad", "ahmed", "ahmaad"],
    "حسن": ["hasan", "hassan"],
    "مهدی": ["mahdi", "mehdi", "mehdy"],
    "امیر": ["amir", "ameer"],
    "محسن": ["mohsen", "muhsin", "mohssen"],
    "علیرضا": ["alireza", "ali-reza", "aliriza"],
    "میلاد": ["milad", "milaad"],
    "آرش": ["arash", "aarash"],
    "سینا": ["sina", "seena"],
    "داریوش": ["dariush", "daryush", "dariusch"],
    "فرهاد": ["farhad", "farhaad"],
    "کامران": ["kamran", "kamraan"],
    "بهرام": ["bahram", "bahraum"],
    "شاهرام": ["shahram", "shahraum"],
    "فریدون": ["fereydoon", "fereydoun", "faridon", "faridun"],
    "کیانوش": ["kianoush", "kianoosh", "kianush"],
    "پیمان": ["peyman", "payman"],
    "پویا": ["pouya", "puya"],
    "رامین": ["ramin", "raamin"],
    "نیما": ["nima", "neema"],
    "سامان": ["saman", "saaman"],
    "بهزاد": ["behzad", "bahzad"],
    "کاوه": ["kaveh", "kavé"],
    "سهراب": ["sohrab", "sohrob"],
    "مازیار": ["maziar", "mazyar"],
    "ناصر": ["nasser", "nasir"],
    "منصور": ["mansour", "mansur", "manssur"],
    "خسرو": ["khosrow", "khosrau", "kosrow"],
    "ایرج": ["iraj", "eeaj"],
    "جمشید": ["jamshid", "djamshid"],
    "شاپور": ["shapour", "shapur"],
    "کورش": ["koroush", "cyrus", "koorosh"],
    "اردشیر": ["ardeshir", "ardashir"],
    "هوشنگ": ["houshang", "hooshangh"],
    "مهران": ["mehran", "mahran"],
    "وحید": ["vahid", "wahid"],
    "عباس": ["abbas", "abas"],
    "جواد": ["javad", "djavad"],
    "صادق": ["sadegh", "sadeq"],
    "اصغر": ["asghar", "asgar"],
    "اکبر": ["akbar", "akber"],
    "تقی": ["taghi", "taqui"],
    "حمید": ["hamid", "hameed"],
    "کریم": ["karim", "kareem"],
    "مجید": ["majid", "majeed"],
    # ── Female given names ───────────────────────────────────────────────────
    "فاطمه": ["fateme", "fatemeh", "fatime"],
    "زهرا": ["zahra", "zehra"],
    "مریم": ["maryam", "mariam"],
    "زینب": ["zeinab", "zaynab", "zainab"],
    "نرگس": ["narges", "nargess", "nargis"],
    "شیرین": ["shirin", "shireen"],
    "پریسا": ["parisa", "pareesa"],
    "الناز": ["elnaz", "elnaaz"],
    "نگار": ["negar", "negaar"],
    "شادی": ["shadi", "shaadi"],
    "آذر": ["azar", "aazar"],
    "مهناز": ["mahnaz", "mahnaaz"],
    "ملیحه": ["maliheh", "malihe"],
    "سمیرا": ["samira", "sameera"],
    "بهاره": ["bahareh", "bahar"],
    "گلناز": ["golnaz", "golnaaz"],
    "مهسا": ["mahsa", "mahsaa"],
    "سپیده": ["sepideh", "spideh"],
    "رویا": ["roya", "ruya"],
    "فریبا": ["fariba", "farieba"],
    "منیره": ["monireh", "monirehh"],
    "پروانه": ["parvaneh", "parvane"],
    "طاهره": ["tahereh", "tahere", "tahera"],
    "ناهید": ["nahid", "naahid"],
    "نسرین": ["nasrin", "nassrin"],
    "گلی": ["goli", "golee"],
}
