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

VIETNAMESE_SURNAME_VARIANTS: dict[str, list[str]] = {
    # ── Surnames (covers ~99% of Vietnamese population) ───────────────────
    "nguyễn": ["nguyen", "nguyên", "nguyn"],
    "trần": ["tran", "trần", "trant"],
    "lê": ["le", "lê"],
    "phạm": ["pham", "phan"],
    "hoàng": ["hoang", "hong", "hwang"],
    "huỳnh": ["huynh", "huyhn", "huynt"],
    "phan": ["phan"],
    "vũ": ["vu", "voo", "wu"],
    "võ": ["vo", "voh"],
    "đặng": ["dang", "dặng"],
    "bùi": ["bui", "buj"],
    "đỗ": ["do", "doe"],
    "hồ": ["ho", "hoh"],
    "ngô": ["ngo", "ngoh"],
    "dương": ["duong", "dong"],
    "lý": ["ly", "li"],
    "trịnh": ["trinh", "trịnh"],
    "đinh": ["dinh"],
    "lưu": ["luu", "lyu", "lu"],
    "phùng": ["phung", "fung"],
    "đoàn": ["doan", "joan"],
    "vương": ["vuong", "vuonh"],
    "trương": ["truong", "trương"],
    "tô": ["to", "toh"],
    "đào": ["dao", "dow"],
    "hà": ["ha", "hah"],
    "mai": ["mai", "my"],
    "tạ": ["ta", "tar"],
    "thái": ["thai", "thi"],
    "lâm": ["lam", "lahm"],
    "quách": ["quach", "kwach"],
    "chu": ["chu", "choo"],
    "kiều": ["kieu", "kew"],
    "lương": ["luong", "lyong"],
    "thạch": ["thach", "tahk"],
    "khúc": ["khuc", "kook"],
    "đức": ["duc", "duk"],
    "văn": ["van", "vahn"],
    "sơn": ["son", "sohn"],
    "ninh": ["ninh", "nin"],
    "lại": ["lai", "lie"],
    "trọng": ["trong", "trung"],
    "hùng": ["hung", "hoong"],
    "khổng": ["khong", "kong"],
    "doãn": ["doan", "dwan"],
    "tống": ["tong", "song"],
    "mạc": ["mac", "mak"],
    "vừa": ["vua", "vwa"],
    "bạch": ["bach", "bahk"],
    "đỗ": ["do", "doe"],
    "cam": ["cam", "kahm"],
    "liêu": ["lieu", "lyew"],
    # ── Common given name components (appear standalone in LLM output) ─────
    "thị": ["thi", "thy"],      # female particle
    "văn": ["van", "vahn"],     # male particle
    "thắng": ["thang", "thaing"],
    "minh": ["minh", "min"],
    "anh": ["anh", "ann"],
    "hương": ["huong", "hwong"],
    "linh": ["linh", "lin"],
    "dũng": ["dung", "zoong"],
    "tuấn": ["tuan", "twahn"],
    "hải": ["hai", "hy"],
    "nam": ["nam", "nahm"],
    "quang": ["quang", "kwang"],
    "long": ["long", "lohng"],
    "đức": ["duc", "duk"],
    "hòa": ["hoa", "hwah"],
    "bình": ["binh", "bin"],
    "khoa": ["khoa", "kwah"],
    "thành": ["thanh", "tahn"],
    "phương": ["phuong", "fwong"],
    "ngọc": ["ngoc", "nyok"],
    "lan": ["lan", "lahn"],
    "mai": ["mai", "my"],
    "thu": ["thu", "too"],
    "loan": ["loan", "lwan"],
    "chi": ["chi", "chee"],
    "nga": ["nga", "nyah"],
    "diễm": ["diem", "dyem"],
    "nhung": ["nhung", "noong"],
    "trang": ["trang", "chahng"],
    "uyên": ["uyen", "wien"],
    "thúy": ["thuy", "twee"],
    "xuân": ["xuan", "swan"],
    "kim": ["kim", "gim"],
    "hồng": ["hong", "hoong"],
    "yến": ["yen", "yenn"],
    "ly": ["ly"],
}
