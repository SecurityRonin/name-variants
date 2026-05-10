"""Feature 7: CJK given-name tables — RED/GREEN tests."""

from name_variants import ALL_TABLES, lookup

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
    assert lookup("明") != []
    assert lookup("Ming") != []


def test_chinese_given_wei():
    assert lookup("伟") != []


def test_chinese_given_fang():
    assert lookup("芳") != []


def test_chinese_given_yang():
    # Yang is both a surname (杨) and given name (阳/洋/扬) — clusters should include both
    assert lookup("Yang") != []


# ── Korean given-name lookups ─────────────────────────────────────────────────


def test_korean_given_jae():
    # 재 (Jae) — common given name component
    assert lookup("재") != [] or lookup("Jae") != []


def test_korean_given_min():
    assert lookup("민") != [] or lookup("Min") != []


def test_korean_given_ji():
    assert lookup("지") != [] or lookup("Ji") != []


# ── Japanese given-name lookups ───────────────────────────────────────────────


def test_japanese_given_kenji():
    assert lookup("Kenji") != []


def test_japanese_given_yuki():
    assert lookup("Yuki") != []


def test_japanese_given_haruto():
    assert lookup("Haruto") != []


# ── Round-trip test ───────────────────────────────────────────────────────────


def test_all_given_canonicals_self_lookup():
    for table_name in ["chinese_given", "korean_given", "japanese_given"]:
        for canonical in ALL_TABLES[table_name]:
            clusters = lookup(canonical)
            assert any(canonical in c for c in clusters), (
                f"{table_name}: {canonical!r} not found in any cluster from lookup({canonical!r})"
            )
