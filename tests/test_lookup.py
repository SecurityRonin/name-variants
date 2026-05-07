"""Tests for lookup_key(), lookup_all(), and ALL_TABLES completeness."""
from name_variants import ALL_TABLES, lookup_all, lookup_key

# ── Table completeness ────────────────────────────────────────────────────────

def test_all_tables_present():
    expected = {
        "chinese", "arabic", "japanese", "korean", "vietnamese",
        "indian_hindi", "indian_tamil", "indian_bengali",
        "persian", "hebrew", "thai", "greek", "turkish",
        "russian", "indonesian_malay",
    }
    assert set(ALL_TABLES.keys()) == expected


def test_all_romanizations_are_lowercase():
    for table_name, table in ALL_TABLES.items():
        for canonical, variants in table.items():
            for v in variants:
                assert v == v.lower(), (
                    f"{table_name}: {canonical!r} has non-lowercase variant {v!r}"
                )


def test_all_keys_nonempty():
    for table_name, table in ALL_TABLES.items():
        for canonical, variants in table.items():
            assert canonical.strip(), f"{table_name}: empty canonical key"
            for v in variants:
                assert v.strip(), f"{table_name}: {canonical!r} has empty variant"


# ── Chinese lookups ───────────────────────────────────────────────────────────

def test_chan_and_chen_same_key():
    assert lookup_key("Chan") == lookup_key("Chen")


def test_tan_and_chen_same_key():
    # Hokkien Tan = Mandarin Chen = 陈
    assert lookup_key("Tan") == lookup_key("Chen")


def test_traditional_and_simplified_same_key():
    # 陳 (Traditional) should resolve to 陈 (Simplified) key
    # Direct lookup without opencc — Traditional char in index
    assert lookup_key("陈") is not None
    assert lookup_key("陳") == lookup_key("陈")
    assert lookup_key("劉") == lookup_key("刘")
    assert lookup_key("許") == lookup_key("许")


def test_traditional_chinese_resolves_to_simplified():
    """Traditional forms must resolve to the Simplified canonical key."""
    assert lookup_key("陳") == "陈"
    assert lookup_key("劉") == "刘"
    assert lookup_key("張") == "张"
    assert lookup_key("楊") == "杨"
    assert lookup_key("趙") == "赵"
    assert lookup_key("吳") == "吴"
    assert lookup_key("鄭") == "郑"
    assert lookup_key("許") == "许"
    assert lookup_key("關") == "关"


def test_xu_and_hui_same_key():
    assert lookup_key("Xu") == lookup_key("Hui")


def test_wang_and_wong_same_key():
    assert lookup_key("Wang") == lookup_key("Wong")


def test_different_chinese_surnames_different_keys():
    assert lookup_key("Chen") != lookup_key("Li")
    assert lookup_key("Wong") != lookup_key("Xu")


# ── Korean lookups ────────────────────────────────────────────────────────────

def test_park_and_bak_same_key():
    assert lookup_key("Park") == lookup_key("Bak")


def test_lee_and_yi_same_key():
    # 이: Lee (diaspora) / Yi (MR) / Rhee (older)
    assert lookup_key("Lee") == lookup_key("Yi")
    assert lookup_key("Lee") == lookup_key("Rhee")


def test_choi_and_choe_same_key():
    assert lookup_key("Choi") == lookup_key("Choe")


def test_jung_and_chung_same_key():
    assert lookup_key("Jung") == lookup_key("Chung")


# ── Vietnamese lookups ────────────────────────────────────────────────────────

def test_nguyen_stripped():
    key = lookup_key("Nguyen")
    assert key is not None
    assert key == lookup_key("nguyễn")


def test_tran_stripped():
    assert lookup_key("Tran") == lookup_key("trần")


# ── Arabic lookups ────────────────────────────────────────────────────────────

def test_muhammad_variants():
    k = lookup_key("Muhammad")
    assert k == lookup_key("Mohammed")
    assert k == lookup_key("Mohamed")


def test_fatima_variants():
    assert lookup_key("Fatima") == lookup_key("Fatimah")


# ── Russian lookups ───────────────────────────────────────────────────────────

def test_ivanov_and_ivanoff():
    assert lookup_key("Ivanov") == lookup_key("Ivanoff")


def test_dostoevsky_variants():
    assert lookup_key("Dostoevsky") == lookup_key("Dostoyevsky")


# ── Hebrew lookups ────────────────────────────────────────────────────────────

def test_yitzhak_and_isaac():
    assert lookup_key("Yitzhak") == lookup_key("Isaac")


# ── Turkish lookups ───────────────────────────────────────────────────────────

def test_celik_and_chelik():
    assert lookup_key("Celik") == lookup_key("çelik")


# ── Unknown names ─────────────────────────────────────────────────────────────

def test_unknown_returns_none():
    assert lookup_key("Kowalski") is None
    assert lookup_key("Smith") is None
    assert lookup_key("Johnson") is None


def test_empty_string_returns_none():
    assert lookup_key("") is None


# ── Token-level lookup in multi-word names ────────────────────────────────────

def test_chan_in_full_name():
    # "Chan Wai Ming" → "Chan" token matches → returns Chinese surname key
    key = lookup_key("Chan Wai Ming")
    assert key is not None
    assert key == lookup_key("Chen")


def test_park_in_full_name():
    key = lookup_key("Park Ji-sung")
    assert key is not None
    assert key == lookup_key("Bak")


# ── lookup_all ────────────────────────────────────────────────────────────────

def test_lookup_all_returns_key_and_variants():
    result = lookup_all("Chan")
    assert result is not None
    key, variants = result
    assert key == "陈"
    assert "chen" in variants
    assert "chan" in variants


def test_lookup_all_traditional_shows_in_variants():
    result = lookup_all("陈")
    assert result is not None
    key, variants = result
    assert key == "陈"
    assert "陳" in variants


def test_lookup_all_unknown_returns_none():
    assert lookup_all("Smith") is None
    assert lookup_all("") is None


def test_lookup_all_multiword():
    result = lookup_all("Chan Wai Ming")
    assert result is not None
    assert result[0] == "陈"
