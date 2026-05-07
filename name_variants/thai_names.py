"""
Thai name lookup: Thai script → romanization variants.

Key problem: Thai romanization is highly inconsistent even within official documents.
The Royal Thai General System (RTGS) is official but widely ignored in passports
and legal documents, which use phonetic approximations.

  ประยุทธ์ → Prayuth (RTGS) / Prayut / Prayudh / Prayooth
  ทักษิณ → Thaksin (common) / Takshin / Thuxin
  สมชาย → Somchai (common) / Somjai / Somshay

Also: Thai surnames are long compounds, often unique to a family.
This table focuses on first names (given names), which are standardized.

Sources:
  - RTGS 2023 (Royal Thai General System)
  - Thai passport romanization conventions
  - Common Central Thai phonetic approximations
"""

THAI_NAME_VARIANTS: dict[str, list[str]] = {
    # ── Common male given names ──────────────────────────────────────────────
    "สมชาย": ["somchai", "somjai", "somchaai"],
    "ประยุทธ์": ["prayuth", "prayut", "prayudh", "prayooth"],
    "ทักษิณ": ["thaksin", "takshin", "taxin"],
    "สุรยุทธ์": ["surayuth", "surayud"],
    "วิชัย": ["wichai", "vichai", "witchai"],
    "สมศักดิ์": ["somsak", "somksak"],
    "ชาตรี": ["chatree", "chatri"],
    "อานันท์": ["anand", "anan", "arnant"],
    "ธนากร": ["thanakorn", "tanakorn"],
    "ภูมิ": ["poom", "phoom", "bhum"],
    "กฤษณ์": ["krit", "krich", "krish"],
    "วรวุฒิ": ["worawut", "vorawut"],
    "เอกชัย": ["ekachai", "akechai"],
    "นพดล": ["nopadol", "noppadon"],
    "พิทักษ์": ["phitak", "pitak"],
    "ชัยวัฒน์": ["chaiwat", "chaivat"],
    "สิทธิชัย": ["sittchai", "sittichai"],
    "วสันต์": ["wasan", "vasan"],
    "ศิริชัย": ["sirichai", "serichai"],
    "ประสิทธิ์": ["prasit", "prasith"],
    "ไพบูลย์": ["paiboon", "paibul"],
    "บุญมี": ["boonmee", "bunmee"],
    "บุญชัย": ["boonchai", "bunchai"],
    "ชาญชัย": ["chanchai", "changchai"],
    "สุพจน์": ["suphot", "supoch"],
    # ── Common female given names ────────────────────────────────────────────
    "สมหญิง": ["somying"],
    "นงนุช": ["nongnuch", "nongnooch"],
    "อรทัย": ["orathai", "aurathai"],
    "สุมาลี": ["sumalee", "sumali"],
    "วิไลวรรณ": ["wilaiwan", "vilaivan"],
    "ปรียา": ["priya", "preya"],
    "กนกวรรณ": ["kanokwan", "kanokvarn"],
    "ศิริพร": ["siriporn", "siripon"],
    "มณีรัตน์": ["maneerat", "manerat"],
    "สุภาพร": ["supaporn", "supapone"],
    "ทิพวรรณ": ["thippawan", "tippawan"],
    "บุษบา": ["butsaba", "bussaba"],
    "พรทิพย์": ["porntip", "pontip", "porntipp"],
    "จันทรา": ["chantra", "jantara"],
    "ดาวเรือง": ["daorueang", "daoreang"],
    "เพ็ญพักตร์": ["penpak", "penpag"],
    "มาลัย": ["malai", "maalai"],
    "ชูใจ": ["choosai", "chujai"],
    "รัตนา": ["rattana", "ratana"],
    "อมรา": ["amora", "amra"],
    "ลดาวัลย์": ["ladawan", "ladaval"],
    "นภาพร": ["naphaporn", "napaporn"],
    "ศุภรา": ["suphara", "supara"],
    "พัชรา": ["patchara", "patchra"],
    "อุษา": ["usa", "usha"],
    # ── Common name components (appear standalone) ───────────────────────────
    "ศรี": ["sri", "si", "see"],
    "ไทย": ["thai", "tai"],
    "วัน": ["wan", "van"],
    "ดี": ["dee", "di"],
    "สุข": ["suk", "sook"],
    "ใจ": ["jai", "chai"],
    "พร": ["porn", "pon", "phon"],
    "ชัย": ["chai"],
    "ดวง": ["duang", "doung"],
    "แก้ว": ["kaew", "keo"],
    "ทอง": ["thong", "tong"],
    "รัก": ["rak", "rack"],
    "นิ": ["ni", "nee"],
    "มณี": ["manee", "mani"],
    "รุ่ง": ["rung", "roong"],
    "เรือง": ["rueang", "reang"],
    "แสง": ["saeng", "sang"],
    "อร": ["on", "orn"],
}
