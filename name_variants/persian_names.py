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

PERSIAN_NAME_VARIANTS: dict[str, dict] = {
    'محمد': {
        "forms": ['mohammad', 'muhammad', 'mohammed', 'mohamed', 'mohamad'],
        "frequency": 150_000_000,
    },
    'علی': {
        "forms": ['ali', 'aly'],
    },
    'حسین': {
        "forms": ['hossein', 'hussein', 'husain', 'hosein'],
    },
    'رضا': {
        "forms": ['reza', 'riza', 'ridha', 'reda'],
    },
    'احمد': {
        "forms": ['ahmad', 'ahmed', 'ahmaad'],
    },
    'حسن': {
        "forms": ['hasan', 'hassan'],
        "frequency": 10_000_000,
    },
    'مهدی': {
        "forms": ['mahdi', 'mehdi', 'mehdy'],
    },
    'امیر': {
        "forms": ['amir', 'ameer'],
    },
    'محسن': {
        "forms": ['mohsen', 'muhsin', 'mohssen'],
    },
    'علیرضا': {
        "forms": ['alireza', 'ali-reza', 'aliriza'],
    },
    'میلاد': {
        "forms": ['milad', 'milaad'],
    },
    'آرش': {
        "forms": ['arash', 'aarash'],
    },
    'سینا': {
        "forms": ['sina', 'seena'],
    },
    'داریوش': {
        "forms": ['dariush', 'daryush', 'dariusch'],
    },
    'فرهاد': {
        "forms": ['farhad', 'farhaad'],
    },
    'کامران': {
        "forms": ['kamran', 'kamraan'],
    },
    'بهرام': {
        "forms": ['bahram', 'bahraum'],
    },
    'شاهرام': {
        "forms": ['shahram', 'shahraum'],
    },
    'فریدون': {
        "forms": ['fereydoon', 'fereydoun', 'faridon', 'faridun'],
    },
    'کیانوش': {
        "forms": ['kianoush', 'kianoosh', 'kianush'],
    },
    'پیمان': {
        "forms": ['peyman', 'payman'],
    },
    'پویا': {
        "forms": ['pouya', 'puya'],
    },
    'رامین': {
        "forms": ['ramin', 'raamin'],
    },
    'نیما': {
        "forms": ['nima', 'neema'],
    },
    'سامان': {
        "forms": ['saman', 'saaman'],
    },
    'بهزاد': {
        "forms": ['behzad', 'bahzad'],
    },
    'کاوه': {
        "forms": ['kaveh', 'kavé'],
    },
    'سهراب': {
        "forms": ['sohrab', 'sohrob'],
    },
    'مازیار': {
        "forms": ['maziar', 'mazyar'],
    },
    'ناصر': {
        "forms": ['nasser', 'nasir'],
    },
    'منصور': {
        "forms": ['mansour', 'mansur', 'manssur'],
    },
    'خسرو': {
        "forms": ['khosrow', 'khosrau', 'kosrow'],
    },
    'ایرج': {
        "forms": ['iraj', 'eeaj'],
    },
    'جمشید': {
        "forms": ['jamshid', 'djamshid'],
    },
    'شاپور': {
        "forms": ['shapour', 'shapur'],
    },
    'کورش': {
        "forms": ['koroush', 'cyrus', 'koorosh'],
    },
    'اردشیر': {
        "forms": ['ardeshir', 'ardashir'],
    },
    'هوشنگ': {
        "forms": ['houshang', 'hooshangh'],
    },
    'مهران': {
        "forms": ['mehran', 'mahran'],
    },
    'وحید': {
        "forms": ['vahid', 'wahid'],
    },
    'عباس': {
        "forms": ['abbas', 'abas'],
    },
    'جواد': {
        "forms": ['javad', 'djavad'],
    },
    'صادق': {
        "forms": ['sadegh', 'sadeq'],
    },
    'اصغر': {
        "forms": ['asghar', 'asgar'],
    },
    'اکبر': {
        "forms": ['akbar', 'akber'],
    },
    'تقی': {
        "forms": ['taghi', 'taqui'],
    },
    'حمید': {
        "forms": ['hamid', 'hameed'],
    },
    'کریم': {
        "forms": ['karim', 'kareem'],
    },
    'مجید': {
        "forms": ['majid', 'majeed'],
    },
    'فاطمه': {
        "forms": ['fateme', 'fatemeh', 'fatime'],
    },
    'زهرا': {
        "forms": ['zahra', 'zehra'],
    },
    'مریم': {
        "forms": ['maryam', 'mariam'],
    },
    'زینب': {
        "forms": ['zeinab', 'zaynab', 'zainab'],
    },
    'نرگس': {
        "forms": ['narges', 'nargess', 'nargis'],
    },
    'شیرین': {
        "forms": ['shirin', 'shireen'],
    },
    'پریسا': {
        "forms": ['parisa', 'pareesa'],
    },
    'الناز': {
        "forms": ['elnaz', 'elnaaz'],
    },
    'نگار': {
        "forms": ['negar', 'negaar'],
    },
    'شادی': {
        "forms": ['shadi', 'shaadi'],
    },
    'آذر': {
        "forms": ['azar', 'aazar'],
    },
    'مهناز': {
        "forms": ['mahnaz', 'mahnaaz'],
    },
    'ملیحه': {
        "forms": ['maliheh', 'malihe'],
    },
    'سمیرا': {
        "forms": ['samira', 'sameera'],
    },
    'بهاره': {
        "forms": ['bahareh', 'bahar'],
    },
    'گلناز': {
        "forms": ['golnaz', 'golnaaz'],
    },
    'مهسا': {
        "forms": ['mahsa', 'mahsaa'],
    },
    'سپیده': {
        "forms": ['sepideh', 'spideh'],
    },
    'رویا': {
        "forms": ['roya', 'ruya'],
    },
    'فریبا': {
        "forms": ['fariba', 'farieba'],
    },
    'منیره': {
        "forms": ['monireh', 'monirehh'],
    },
    'پروانه': {
        "forms": ['parvaneh', 'parvane'],
    },
    'طاهره': {
        "forms": ['tahereh', 'tahere', 'tahera'],
    },
    'ناهید': {
        "forms": ['nahid', 'naahid'],
    },
    'نسرین': {
        "forms": ['nasrin', 'nassrin'],
    },
    'گلی': {
        "forms": ['goli', 'golee'],
    },
    'محمدی': {
        "forms": ['mohammadi', 'mohamadi', 'mahammadi'],
    },
    'احمدی': {
        "forms": ['ahmadi', 'ahmaady'],
    },
    'رضایی': {
        "forms": ['rezaei', 'rezaee', 'razayi'],
    },
    'حسینی': {
        "forms": ['hosseini', 'hosseiny', 'hussaini'],
    },
    'موسوی': {
        "forms": ['mousavi', 'moosavi', 'musavi'],
    },
}
