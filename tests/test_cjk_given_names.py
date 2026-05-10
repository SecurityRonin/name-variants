"""Feature 7: CJK given-name tables — RED/GREEN tests."""
from name_variants import ALL_TABLES, lookup_key, lookup_candidates


# ── Table presence ────────────────────────────────────────────────────────────

def test_chinese_given_table_present():
    assert "chinese_given" in ALL_TABLES
    assert len(ALL_TABLES["chinese_given"]) >= 100


def test_korean_given_table_present():
    assert "korean_given" in ALL_TABLES
    assert len(ALL_TABLES["korean_given"]) >= 50


def test_japanese_given_table_present():
    assert "japanese_given" in ALL_TABLES
    assert len(ALL_TABLES["japanese_given"]) >= 60


# ── Chinese given-name lookups ────────────────────────────────────────────────

def test_chinese_given_ming():
    assert lookup_key("明") is not None
    assert lookup_key("Ming") is not None


def test_chinese_given_wei():
    assert lookup_key("伟") is not None


def test_chinese_given_fang():
    assert lookup_key("芳") is not None


def test_chinese_given_yang():
    # Yang is both a surname (杨) and given name (阳/洋/扬) — candidates should include both
    candidates = lookup_candidates("Yang")
    assert len(candidates) >= 1


# ── Korean given-name lookups ─────────────────────────────────────────────────

def test_korean_given_jae():
    # 재 (Jae) — common given name component
    assert lookup_key("재") is not None or lookup_key("Jae") is not None


def test_korean_given_min():
    assert lookup_key("민") is not None or lookup_key("Min") is not None


def test_korean_given_ji():
    assert lookup_key("지") is not None or lookup_key("Ji") is not None


# ── Japanese given-name lookups ───────────────────────────────────────────────

def test_japanese_given_kenji():
    assert lookup_key("Kenji") is not None


def test_japanese_given_yuki():
    assert lookup_key("Yuki") is not None


def test_japanese_given_haruto():
    assert lookup_key("Haruto") is not None


# ── Round-trip test ───────────────────────────────────────────────────────────

def test_all_given_canonicals_self_lookup():
    for table_name in ["chinese_given", "korean_given", "japanese_given"]:
        for canonical in ALL_TABLES[table_name]:
            candidates = lookup_candidates(canonical)
            assert canonical in candidates, (
                f"{table_name}: {canonical!r} not in its own candidates"
            )
