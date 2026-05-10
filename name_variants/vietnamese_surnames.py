"""
Vietnamese surname lookup: toned form → romanization variants.

Key problem: Vietnamese uses a Latin alphabet with tone marks and
diacritics that are almost always stripped in Western documents.
The toned form is canonical; tone-stripped is the most common variant.

Note: Vietnamese surnames are few (~100 cover virtually all population).
Nguyễn alone is ~40% of Vietnam. This table focuses on all surnames
plus their common given name variants, since Vietnamese names are
3-4 syllables and LLMs often mangle the tone marks.

Romanization variants:
  - Full Unicode (canonical): Nguyễn
  - ASCII-stripped: Nguyen
  - Alternative diacritic: Nguyên (wrong but appears in documents)

Sources:
  - General Statistics Office of Vietnam surname frequency
  - Standard Vietnamese orthography (Quốc ngữ)
  - Common diaspora (US/Australia/France/HK) spelling patterns
"""

VIETNAMESE_SURNAME_VARIANTS: dict[str, dict] = {
    'nguyễn': {
        "forms": ['nguyen', 'nguyên', 'nguyn'],
        "frequency": 39_000_000,
    },
    'trần': {
        "forms": ['tran', 'trần', 'trant'],
        "frequency": 11_000_000,
    },
    'lê': {
        "forms": ['le', 'lee', 'lê'],
        "frequency": 9_500_000,
    },
    'phạm': {
        "forms": ['pham', 'phan'],
        "frequency": 7_500_000,
    },
    'hoàng': {
        "forms": ['hoang', 'hong', 'hwang'],
        "frequency": 5_100_000,
    },
    'huỳnh': {
        "forms": ['huynh', 'huyhn', 'huynt'],
        "frequency": 3_900_000,
    },
    'phan': {
        "forms": ['phan'],
        "frequency": 1_500_000,
    },
    'vũ': {
        "forms": ['vu', 'voo', 'wu'],
        "frequency": 1_600_000,
    },
    'võ': {
        "forms": ['vo', 'voh'],
        "frequency": 1_200_000,
    },
    'đặng': {
        "forms": ['dang', 'dặng'],
        "frequency": 1_100_000,
    },
    'bùi': {
        "forms": ['bui', 'buj'],
        "frequency": 1_000_000,
    },
    'đỗ': {
        "forms": ['do', 'doe'],
        "frequency": 950_000,
    },
    'hồ': {
        "forms": ['ho', 'hoh'],
        "frequency": 900_000,
    },
    'ngô': {
        "forms": ['ngo', 'ngoh'],
        "frequency": 850_000,
    },
    'dương': {
        "forms": ['duong', 'dong'],
        "frequency": 800_000,
    },
    'lý': {
        "forms": ['ly', 'li'],
    },
    'trịnh': {
        "forms": ['trinh', 'trịnh'],
    },
    'đinh': {
        "forms": ['dinh'],
    },
    'lưu': {
        "forms": ['luu', 'lyu', 'lu'],
    },
    'phùng': {
        "forms": ['phung', 'fung'],
    },
    'đoàn': {
        "forms": ['doan', 'joan'],
    },
    'vương': {
        "forms": ['vuong', 'vuonh'],
    },
    'trương': {
        "forms": ['truong', 'trương'],
    },
    'tô': {
        "forms": ['to', 'toh'],
    },
    'đào': {
        "forms": ['dao', 'dow'],
    },
    'hà': {
        "forms": ['ha', 'hah'],
    },
    'mai': {
        "forms": ['mai', 'my'],
    },
    'tạ': {
        "forms": ['ta', 'tar'],
    },
    'thái': {
        "forms": ['thai', 'thi'],
    },
    'lâm': {
        "forms": ['lam', 'lahm'],
    },
    'quách': {
        "forms": ['quach', 'kwach'],
    },
    'chu': {
        "forms": ['chu', 'choo'],
    },
    'kiều': {
        "forms": ['kieu', 'kew'],
    },
    'lương': {
        "forms": ['luong', 'lyong'],
    },
    'thạch': {
        "forms": ['thach', 'tahk'],
    },
    'khúc': {
        "forms": ['khuc', 'kook'],
    },
    'đức': {
        "forms": ['duc', 'duk'],
    },
    'văn': {
        "forms": ['van', 'vahn'],
    },
    'sơn': {
        "forms": ['son', 'sohn'],
    },
    'ninh': {
        "forms": ['ninh', 'nin'],
    },
    'lại': {
        "forms": ['lai', 'lie'],
    },
    'trọng': {
        "forms": ['trong', 'trung'],
    },
    'hùng': {
        "forms": ['hung', 'hoong'],
    },
    'khổng': {
        "forms": ['khong', 'kong'],
    },
    'doãn': {
        "forms": ['doan', 'dwan'],
    },
    'tống': {
        "forms": ['tong', 'song'],
    },
    'mạc': {
        "forms": ['mac', 'mak'],
    },
    'vừa': {
        "forms": ['vua', 'vwa'],
    },
    'bạch': {
        "forms": ['bach', 'bahk'],
    },
    'cam': {
        "forms": ['cam', 'kahm'],
    },
    'liêu': {
        "forms": ['lieu', 'lyew'],
    },
    'thị': {
        "forms": ['thi', 'thy'],
    },
    'thắng': {
        "forms": ['thang', 'thaing'],
    },
    'minh': {
        "forms": ['minh', 'min'],
    },
    'anh': {
        "forms": ['anh', 'ann'],
    },
    'hương': {
        "forms": ['huong', 'hwong'],
    },
    'linh': {
        "forms": ['linh', 'lin'],
    },
    'dũng': {
        "forms": ['dung', 'zoong'],
    },
    'tuấn': {
        "forms": ['tuan', 'twahn'],
    },
    'hải': {
        "forms": ['hai', 'hy'],
    },
    'nam': {
        "forms": ['nam', 'nahm'],
    },
    'quang': {
        "forms": ['quang', 'kwang'],
    },
    'long': {
        "forms": ['long', 'lohng'],
    },
    'hòa': {
        "forms": ['hoa', 'hwah'],
    },
    'bình': {
        "forms": ['binh', 'bin'],
    },
    'khoa': {
        "forms": ['khoa', 'kwah'],
    },
    'thành': {
        "forms": ['thanh', 'tahn'],
    },
    'phương': {
        "forms": ['phuong', 'fwong'],
    },
    'ngọc': {
        "forms": ['ngoc', 'nyok'],
    },
    'lan': {
        "forms": ['lan', 'lahn'],
    },
    'thu': {
        "forms": ['thu', 'too'],
    },
    'loan': {
        "forms": ['loan', 'lwan'],
    },
    'chi': {
        "forms": ['chi', 'chee'],
    },
    'nga': {
        "forms": ['nga', 'nyah'],
    },
    'diễm': {
        "forms": ['diem', 'dyem'],
    },
    'nhung': {
        "forms": ['nhung', 'noong'],
    },
    'trang': {
        "forms": ['trang', 'chahng'],
    },
    'uyên': {
        "forms": ['uyen', 'wien'],
    },
    'thúy': {
        "forms": ['thuy', 'twee'],
    },
    'xuân': {
        "forms": ['xuan', 'swan'],
    },
    'kim': {
        "forms": ['kim', 'gim'],
    },
    'hồng': {
        "forms": ['hong', 'hoong'],
    },
    'yến': {
        "forms": ['yen', 'yenn'],
    },
    'ly': {
        "forms": ['ly'],
    },
}
