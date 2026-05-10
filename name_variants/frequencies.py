"""
Approximate population counts per canonical surname key.
Sources: national census data, population registry statistics.
Data is approximate and represents surname bearer counts globally.
"""

# Chinese surnames (National Bureau of Statistics China 2020)
CHINESE_SURNAME_FREQUENCIES: dict[str, int] = {
    "王": 106_760_000,
    "李": 95_300_000,
    "张": 87_500_000,
    "刘": 73_000_000,
    "陈": 70_500_000,
    "杨": 46_200_000,
    "黄": 32_000_000,
    "赵": 28_400_000,
    "吴": 27_400_000,
    "周": 25_600_000,
    "徐": 20_800_000,
    "孙": 18_400_000,
    "马": 17_300_000,
    "朱": 14_900_000,
    "胡": 14_700_000,
    "郭": 14_000_000,
    "何": 13_700_000,
    "高": 13_600_000,
    "林": 18_700_000,
    "罗": 12_800_000,
}

# Korean surnames (Ministry of the Interior 2021)
KOREAN_SURNAME_FREQUENCIES: dict[str, int] = {
    "김": 10_687_000,
    "이": 7_307_000,
    "박": 4_192_000,
    "최": 2_334_000,
    "정": 2_151_000,
    "강": 1_176_000,
    "조": 1_059_000,
    "윤": 1_029_000,
    "장": 992_000,
    "임": 822_000,
    "한": 773_000,
    "오": 763_000,
    "서": 751_000,
    "신": 739_000,
    "권": 705_000,
}

# Vietnamese surnames (General Statistics Office 2022)
VIETNAMESE_SURNAME_FREQUENCIES: dict[str, int] = {
    "nguyễn": 39_000_000,
    "trần": 11_000_000,
    "lê": 9_500_000,
    "phạm": 7_500_000,
    "hoàng": 5_100_000,
    "huỳnh": 3_900_000,
    "phan": 1_500_000,
    "vũ": 1_600_000,
    "võ": 1_200_000,
    "đặng": 1_100_000,
    "bùi": 1_000_000,
    "đỗ": 950_000,
    "hồ": 900_000,
    "ngô": 850_000,
    "dương": 800_000,
}

# Russian surnames (approximate, Rosstat)
RUSSIAN_SURNAME_FREQUENCIES: dict[str, int] = {
    "Иванов": 1_500_000,
    "Смирнов": 1_100_000,
    "Кузнецов": 900_000,
    "Попов": 650_000,
    "Васильев": 620_000,
    "Петров": 600_000,
    "Соколов": 580_000,
    "Михайлов": 570_000,
    "Новиков": 510_000,
    "Федоров": 490_000,
}

# Arabic/Islamic names (rough global estimates)
ARABIC_NAME_FREQUENCIES: dict[str, int] = {
    "محمد": 150_000_000,
    "أحمد": 22_000_000,
    "علي": 20_000_000,
    "عمر": 14_000_000,
    "عبدالله": 12_000_000,
    "حسن": 10_000_000,
    "حسين": 9_000_000,
    "إبراهيم": 8_000_000,
    "يوسف": 7_500_000,
    "محمود": 7_000_000,
}

# Japanese surnames (Ministry of Justice 2022, family register data)
JAPANESE_SURNAME_FREQUENCIES: dict[str, int] = {
    "佐藤": 1_928_000,
    "鈴木": 1_806_000,
    "高橋": 1_421_000,
    "田中": 1_336_000,
    "伊藤": 1_085_000,
    "渡辺": 1_083_000,
    "山本": 1_050_000,
    "中村": 1_033_000,
    "小林": 1_011_000,
    "加藤": 888_000,
    "吉田": 863_000,
    "山田": 838_000,
    "佐々木": 680_000,
    "山口": 659_000,
    "松本": 638_000,
}

# All frequency maps combined
ALL_FREQUENCIES: dict[str, int] = {
    **CHINESE_SURNAME_FREQUENCIES,
    **KOREAN_SURNAME_FREQUENCIES,
    **VIETNAMESE_SURNAME_FREQUENCIES,
    **RUSSIAN_SURNAME_FREQUENCIES,
    **ARABIC_NAME_FREQUENCIES,
    **JAPANESE_SURNAME_FREQUENCIES,
}
