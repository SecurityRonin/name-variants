"""
Arabic name lookup: Arabic script → romanization variants.
Covers Egyptian, Levantine, Gulf, North African, South Asian Muslim naming.

Sources:
  - ALA-LC Arabic romanization
  - Hans Wehr transliteration
  - Egyptian/Gulf/Levantine colloquial transcription
  - Common HK/UK diaspora spellings
"""

ARABIC_NAME_VARIANTS: dict[str, dict] = {
    'محمد': {
        "forms": ['muhammad', 'mohammed', 'mohamed', 'mohammad', 'mohamad', 'mehmed', 'mehmet'],
        "frequency": 150_000_000,
    },
    'أحمد': {
        "forms": ['ahmad', 'ahmed', 'ahmet'],
        "frequency": 22_000_000,
    },
    'علي': {
        "forms": ['ali', 'aly'],
        "frequency": 20_000_000,
    },
    'عمر': {
        "forms": ['omar', 'umar', 'omer'],
        "frequency": 14_000_000,
    },
    'إبراهيم': {
        "forms": ['ibrahim', 'abraham', 'ebrahim', 'brahim'],
        "frequency": 8_000_000,
    },
    'خالد': {
        "forms": ['khaled', 'khalid'],
    },
    'يوسف': {
        "forms": ['youssef', 'yousef', 'yusuf', 'yusef'],
        "frequency": 7_500_000,
    },
    'عبدالله': {
        "forms": ['abdullah', 'abdallah', 'abd-allah'],
        "frequency": 12_000_000,
    },
    'حسن': {
        "forms": ['hassan', 'hasan'],
        "frequency": 10_000_000,
    },
    'حسين': {
        "forms": ['hussein', 'husain', 'hussain', 'hossein'],
        "frequency": 9_000_000,
    },
    'عبدالرحمن': {
        "forms": ['abdulrahman', 'abd-al-rahman', 'abdurrahman'],
    },
    'سعيد': {
        "forms": ['saeed', 'said', "sa'id"],
    },
    'سليمان': {
        "forms": ['sulayman', 'suleiman', 'sulaiman', 'solomon'],
    },
    'مصطفى': {
        "forms": ['mustafa', 'mostafa'],
    },
    'محمود': {
        "forms": ['mahmoud', 'mahmud', 'mahmood'],
        "frequency": 7_000_000,
    },
    'إسماعيل': {
        "forms": ['ismail', 'esmail', 'ismael'],
    },
    'عثمان': {
        "forms": ['uthman', 'osman', 'othman'],
    },
    'يحيى': {
        "forms": ['yahya', 'yahia', 'yehya'],
    },
    'إدريس': {
        "forms": ['idris', 'idrees'],
    },
    'داود': {
        "forms": ['dawud', 'dawood', 'david'],
    },
    'صالح': {
        "forms": ['saleh', 'salih'],
    },
    'عبدالعزيز': {
        "forms": ['abdulaziz', 'abdelaziz'],
    },
    'طارق': {
        "forms": ['tariq', 'tarek'],
    },
    'بلال': {
        "forms": ['bilal', 'bilel'],
    },
    'كريم': {
        "forms": ['karim', 'kareem'],
    },
    'جمال': {
        "forms": ['jamal', 'gamal'],
    },
    'زياد': {
        "forms": ['ziyad', 'ziad'],
    },
    'أيمن': {
        "forms": ['ayman', 'aymen'],
    },
    'رامي': {
        "forms": ['rami', 'ramy'],
    },
    'ياسر': {
        "forms": ['yasser', 'yasir'],
    },
    'فيصل': {
        "forms": ['faisal', 'faysal'],
    },
    'وليد': {
        "forms": ['walid', 'waleed'],
    },
    'منير': {
        "forms": ['munir', 'mounir'],
    },
    'شريف': {
        "forms": ['sharif', 'shareef', 'sherif'],
    },
    'هشام': {
        "forms": ['hisham', 'hesham', 'hicham'],
    },
    'حامد': {
        "forms": ['hamid', 'hamed'],
    },
    'عادل': {
        "forms": ['adel', 'adil'],
    },
    'رشيد': {
        "forms": ['rashid', 'rachid'],
    },
    'ناصر': {
        "forms": ['nasser', 'nasir', 'naseer'],
    },
    'حكيم': {
        "forms": ['hakim', 'hakeem'],
    },
    'سمير': {
        "forms": ['samir', 'samer'],
    },
    'تامر': {
        "forms": ['tamer', 'tamir'],
    },
    'لطفي': {
        "forms": ['lutfi', 'lotfi'],
    },
    'ضياء': {
        "forms": ['diya', 'zia'],
    },
    'جهاد': {
        "forms": ['jihad', 'djihad'],
    },
    'مجدي': {
        "forms": ['magdi', 'majdi'],
    },
    'صفوان': {
        "forms": ['safwan', 'sofwan'],
    },
    'أسامة': {
        "forms": ['osama', 'usama', 'ousama'],
    },
    'زكريا': {
        "forms": ['zakariya', 'zechariah', 'zacharia'],
    },
    'فاطمة': {
        "forms": ['fatima', 'fatimah', 'fatema'],
    },
    'عائشة': {
        "forms": ['aisha', 'ayesha', 'aesha'],
    },
    'مريم': {
        "forms": ['maryam', 'mariam', 'miriam'],
    },
    'زينب': {
        "forms": ['zainab', 'zaynab', 'zeinab'],
    },
    'سارة': {
        "forms": ['sara', 'sarah'],
    },
    'نور': {
        "forms": ['noor', 'nur', 'noura'],
    },
    'أمينة': {
        "forms": ['amina', 'aminah', 'ameena'],
    },
    'هند': {
        "forms": ['hind', 'hend'],
    },
    'سلمى': {
        "forms": ['salma', 'saloma'],
    },
    'رنا': {
        "forms": ['rana', 'rania'],
    },
    'نادية': {
        "forms": ['nadia', 'nadya'],
    },
    'سمية': {
        "forms": ['samia', 'samya'],
    },
    'منى': {
        "forms": ['mona', 'muna'],
    },
    'رانيا': {
        "forms": ['rania', 'ranya'],
    },
    'ليلى': {
        "forms": ['layla', 'leila', 'leyla', 'laila'],
    },
    'خديجة': {
        "forms": ['khadija', 'khadijah'],
    },
    'أسماء': {
        "forms": ['asma', 'asmaa'],
    },
    'سناء': {
        "forms": ['sana', 'sanaa'],
    },
    'إيمان': {
        "forms": ['iman', 'eiman'],
    },
    'دينا': {
        "forms": ['dina', 'deena'],
    },
    'ياسمين': {
        "forms": ['yasmin', 'jasmine', 'yasmine'],
    },
    'نوال': {
        "forms": ['nawal', 'naouwal'],
    },
    'هدى': {
        "forms": ['huda', 'houda'],
    },
    'وفاء': {
        "forms": ['wafa', 'wafaa'],
    },
    'سلوى': {
        "forms": ['salwa', 'solwa'],
    },
    'رحمة': {
        "forms": ['rahma', 'rahmat'],
    },
    'لبنى': {
        "forms": ['lubna', 'loubna'],
    },
    'سحر': {
        "forms": ['sahar', 'sehar'],
    },
    'غادة': {
        "forms": ['ghada', 'ghade'],
    },
    'ريم': {
        "forms": ['reem', 'rim'],
    },
    'شيرين': {
        "forms": ['shirin', 'shireen', 'cherine'],
    },
    'حنان': {
        "forms": ['hanan', 'hanane'],
    },
    'شيماء': {
        "forms": ['shayma', 'chaima'],
    },
    'ملاك': {
        "forms": ['malak', 'melak'],
    },
    'نجوى': {
        "forms": ['najwa', 'nagwa'],
    },
    'بسمة': {
        "forms": ['basma', 'bassma'],
    },
    'رشا': {
        "forms": ['rasha', 'racha'],
    },
    'لمياء': {
        "forms": ['lamia', 'lamya'],
    },
    'عبير': {
        "forms": ['abeer', 'abir'],
    },
    'روان': {
        "forms": ['rawan', 'rowan'],
    },
    'زهراء': {
        "forms": ['zahra', 'zahrae', 'zohra'],
    },
    'ميسون': {
        "forms": ['maysun', 'maisun'],
    },
    'ثريا': {
        "forms": ['thuraya', 'thoraya', 'soraiya'],
    },
}
