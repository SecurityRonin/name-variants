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

THAI_NAME_VARIANTS: dict[str, dict] = {
    "สมชาย": {
        "forms": ["somchai", "somjai", "somchaai"],
    },
    "ประยุทธ์": {
        "forms": ["prayuth", "prayut", "prayudh", "prayooth"],
    },
    "ทักษิณ": {
        "forms": ["thaksin", "takshin", "taxin"],
    },
    "สุรยุทธ์": {
        "forms": ["surayuth", "surayud"],
    },
    "วิชัย": {
        "forms": ["wichai", "vichai", "witchai"],
    },
    "สมศักดิ์": {
        "forms": ["somsak", "somksak"],
    },
    "ชาตรี": {
        "forms": ["chatree", "chatri"],
    },
    "อานันท์": {
        "forms": ["anand", "anan", "arnant"],
    },
    "ธนากร": {
        "forms": ["thanakorn", "tanakorn"],
    },
    "ภูมิ": {
        "forms": ["poom", "phoom", "bhum"],
    },
    "กฤษณ์": {
        "forms": ["krit", "krich", "krish"],
    },
    "วรวุฒิ": {
        "forms": ["worawut", "vorawut"],
    },
    "เอกชัย": {
        "forms": ["ekachai", "akechai"],
    },
    "นพดล": {
        "forms": ["nopadol", "noppadon"],
    },
    "พิทักษ์": {
        "forms": ["phitak", "pitak"],
    },
    "ชัยวัฒน์": {
        "forms": ["chaiwat", "chaivat"],
    },
    "สิทธิชัย": {
        "forms": ["sittchai", "sittichai"],
    },
    "วสันต์": {
        "forms": ["wasan", "vasan"],
    },
    "ศิริชัย": {
        "forms": ["sirichai", "serichai"],
    },
    "ประสิทธิ์": {
        "forms": ["prasit", "prasith"],
    },
    "ไพบูลย์": {
        "forms": ["paiboon", "paibul"],
    },
    "บุญมี": {
        "forms": ["boonmee", "bunmee"],
    },
    "บุญชัย": {
        "forms": ["boonchai", "bunchai"],
    },
    "จัน": {
        "forms": ["chan", "jan"],
    },
    "ชาญชัย": {
        "forms": ["chanchai", "changchai"],
    },
    "สุพจน์": {
        "forms": ["suphot", "supoch"],
    },
    "สมหญิง": {
        "forms": ["somying"],
    },
    "นงนุช": {
        "forms": ["nongnuch", "nongnooch"],
    },
    "อรทัย": {
        "forms": ["orathai", "aurathai"],
    },
    "สุมาลี": {
        "forms": ["sumalee", "sumali"],
    },
    "วิไลวรรณ": {
        "forms": ["wilaiwan", "vilaivan"],
    },
    "ปรียา": {
        "forms": ["priya", "preya"],
    },
    "กนกวรรณ": {
        "forms": ["kanokwan", "kanokvarn"],
    },
    "ศิริพร": {
        "forms": ["siriporn", "siripon"],
    },
    "มณีรัตน์": {
        "forms": ["maneerat", "manerat"],
    },
    "สุภาพร": {
        "forms": ["supaporn", "supapone"],
    },
    "ทิพวรรณ": {
        "forms": ["thippawan", "tippawan"],
    },
    "บุษบา": {
        "forms": ["butsaba", "bussaba"],
    },
    "พรทิพย์": {
        "forms": ["porntip", "pontip", "porntipp"],
    },
    "จันทรา": {
        "forms": ["chantra", "jantara"],
    },
    "ดาวเรือง": {
        "forms": ["daorueang", "daoreang"],
    },
    "เพ็ญพักตร์": {
        "forms": ["penpak", "penpag"],
    },
    "มาลัย": {
        "forms": ["malai", "maalai"],
    },
    "ชูใจ": {
        "forms": ["choosai", "chujai"],
    },
    "รัตนา": {
        "forms": ["rattana", "ratana"],
    },
    "อมรา": {
        "forms": ["amora", "amra"],
    },
    "ลดาวัลย์": {
        "forms": ["ladawan", "ladaval"],
    },
    "นภาพร": {
        "forms": ["naphaporn", "napaporn"],
    },
    "ศุภรา": {
        "forms": ["suphara", "supara"],
    },
    "พัชรา": {
        "forms": ["patchara", "patchra"],
    },
    "อุษา": {
        "forms": ["usa", "usha"],
    },
    "ศรี": {
        "forms": ["sri", "si", "see"],
    },
    "ไทย": {
        "forms": ["thai", "tai"],
    },
    "วัน": {
        "forms": ["wan", "van"],
    },
    "ดี": {
        "forms": ["dee", "di"],
    },
    "สุข": {
        "forms": ["suk", "sook"],
    },
    "ใจ": {
        "forms": ["jai", "chai"],
    },
    "พร": {
        "forms": ["porn", "pon", "phon"],
    },
    "ชัย": {
        "forms": ["chai"],
    },
    "ดวง": {
        "forms": ["duang", "doung"],
    },
    "แก้ว": {
        "forms": ["kaew", "keo"],
    },
    "ทอง": {
        "forms": ["thong", "tong"],
    },
    "รัก": {
        "forms": ["rak", "rack"],
    },
    "นิ": {
        "forms": ["ni", "nee"],
    },
    "มณี": {
        "forms": ["manee", "mani"],
    },
    "รุ่ง": {
        "forms": ["rung", "roong"],
    },
    "เรือง": {
        "forms": ["rueang", "reang"],
    },
    "แสง": {
        "forms": ["saeng", "sang"],
    },
    "อร": {
        "forms": ["on", "orn"],
    },
}
