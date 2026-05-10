"""Tests for lookup(), share_cluster(), and ALL_TABLES completeness."""
from name_variants import ALL_TABLES, lookup, share_cluster

# ── Table completeness ────────────────────────────────────────────────────────

def test_all_tables_present():
    expected = {
        "chinese", "arabic", "japanese", "korean", "vietnamese",
        "indian_hindi", "indian_tamil", "indian_bengali",
        "persian", "hebrew", "thai", "greek", "turkish",
        "russian", "indonesian_malay",
        "chinese_given", "korean_given", "japanese_given",
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
    assert share_cluster("Chan", "Chen")


def test_tan_and_chen_same_key():
    # Hokkien Tan = Mandarin Chen = 陈
    assert share_cluster("Tan", "Chen")


def test_traditional_and_simplified_same_key():
    # 陳 (Traditional) should be in the same cluster as 陈 (Simplified)
    assert lookup("陈") != []
    assert share_cluster("陳", "陈")
    assert share_cluster("劉", "刘")
    assert share_cluster("許", "许")


def test_traditional_chinese_resolves_to_simplified():
    """Traditional forms must be in the same cluster as their Simplified form."""
    assert any("陈" in c and "陳" in c for c in lookup("陈"))
    assert any("刘" in c and "劉" in c for c in lookup("刘"))
    assert any("张" in c and "張" in c for c in lookup("张"))
    assert any("杨" in c and "楊" in c for c in lookup("杨"))
    assert any("赵" in c and "趙" in c for c in lookup("赵"))
    assert any("吴" in c and "吳" in c for c in lookup("吴"))
    assert any("郑" in c and "鄭" in c for c in lookup("郑"))
    assert any("许" in c and "許" in c for c in lookup("许"))
    assert any("关" in c and "關" in c for c in lookup("关"))


def test_xu_and_hui_same_key():
    assert share_cluster("Xu", "Hui")


def test_wang_and_wong_same_key():
    assert share_cluster("Wang", "Wong")


def test_different_chinese_surnames_different_keys():
    assert not share_cluster("Chen", "Li")
    assert not share_cluster("Wong", "Xu")


# ── Korean lookups ────────────────────────────────────────────────────────────

def test_park_and_bak_same_key():
    assert share_cluster("Park", "Bak")


def test_lee_and_yi_same_key():
    # 이: Lee (diaspora) / Yi (MR) / Rhee (older)
    assert share_cluster("Lee", "Yi")
    assert share_cluster("Lee", "Rhee")


def test_choi_and_choe_same_key():
    assert share_cluster("Choi", "Choe")


def test_jung_and_chung_same_key():
    assert share_cluster("Jung", "Chung")


# ── Vietnamese lookups ────────────────────────────────────────────────────────

def test_nguyen_stripped():
    assert lookup("Nguyen") != []
    assert share_cluster("Nguyen", "nguyễn")


def test_tran_stripped():
    assert share_cluster("Tran", "trần")


# ── Arabic lookups ────────────────────────────────────────────────────────────

def test_muhammad_variants():
    assert share_cluster("Muhammad", "Mohammed")
    assert share_cluster("Muhammad", "Mohamed")


def test_fatima_variants():
    assert share_cluster("Fatima", "Fatimah")


# ── Russian lookups ───────────────────────────────────────────────────────────

def test_ivanov_and_ivanoff():
    assert share_cluster("Ivanov", "Ivanoff")


def test_dostoevsky_variants():
    assert share_cluster("Dostoevsky", "Dostoyevsky")


# ── Hebrew lookups ────────────────────────────────────────────────────────────

def test_yitzhak_and_isaac():
    assert share_cluster("Yitzhak", "Isaac")


# ── Turkish lookups ───────────────────────────────────────────────────────────

def test_celik_and_chelik():
    assert share_cluster("Celik", "çelik")


# ── lookup — multi-script ambiguous romanizations ─────────────────────────────

def test_candidates_lee_returns_korean_chinese_vietnamese():
    # "lee" legitimately appears in Korean 이, Chinese 李, and Vietnamese lê
    clusters = lookup("Lee")
    all_forms = {f for c in clusters for f in c.forms}
    assert "이" in all_forms
    assert "李" in all_forms
    assert "lê" in all_forms


def test_candidates_ng_returns_both_chinese_surnames():
    # "ng" is ambiguous between 黄 (Huang) and 吴 (Wu) in Hokkien/Cantonese
    clusters = lookup("Ng")
    all_forms = {f for c in clusters for f in c.forms}
    assert "黄" in all_forms
    assert "吴" in all_forms


def test_candidates_unambiguous_returns_single():
    # "nguyen" only appears under nguyễn
    clusters = lookup("Nguyen")
    assert len(clusters) == 1 and "nguyễn" in clusters[0]


def test_candidates_unknown_returns_empty():
    assert lookup("Smith") == []
    assert lookup("") == []


# ── Unknown names ─────────────────────────────────────────────────────────────

def test_unknown_returns_empty():
    assert lookup("Kowalski") == []
    assert lookup("Smith") == []
    assert lookup("Johnson") == []


def test_empty_string_returns_empty():
    assert lookup("") == []


# ── Token-level lookup in multi-word names ────────────────────────────────────

def test_chan_in_full_name():
    # "Chan Wai Ming" → "Chan" token matches → returns Chinese surname cluster
    clusters = lookup("Chan Wai Ming")
    assert any(c.language == "chinese" for c in clusters)


def test_chan_in_full_name_shares_cluster_with_chen():
    assert share_cluster("Chan Wai Ming", "Chen")


def test_park_in_full_name():
    assert share_cluster("Park Ji-sung", "Bak")


# ── lookup — cluster contents ─────────────────────────────────────────────────

def test_lookup_returns_cluster_with_variants():
    clusters = lookup("Chan")
    assert any(c.language == "chinese" for c in clusters)
    chinese = next(c for c in clusters if c.language == "chinese")
    assert "chen" in chinese and "chan" in chinese


def test_lookup_traditional_shows_in_forms():
    clusters = lookup("陈")
    assert any(c.language == "chinese" for c in clusters)
    chinese = next(c for c in clusters if c.language == "chinese")
    assert "陳" in chinese


def test_lookup_unknown_returns_empty():
    assert lookup("Smith") == []
    assert lookup("") == []


def test_lookup_multiword():
    clusters = lookup("Chan Wai Ming")
    assert any(c.language == "chinese" for c in clusters)


# ── Vietnamese (extended) ─────────────────────────────────────────────────────

def test_le_variants():
    assert share_cluster("Le", "lê")


def test_pham_variants():
    assert share_cluster("Pham", "phạm")


def test_hoang_variants():
    assert share_cluster("Hoang", "hoàng")


# ── Arabic (extended) ─────────────────────────────────────────────────────────

def test_ali_variants():
    assert lookup("Ali") != []


def test_hassan_variants():
    assert share_cluster("Hassan", "Hasan")


def test_arabic_script_direct():
    assert lookup("محمد") != []


# ── Russian (extended) ────────────────────────────────────────────────────────

def test_sokolov_variants():
    assert share_cluster("Sokolov", "Sokoloff")


def test_petrov_variants():
    assert lookup("Petrov") != []


def test_cyrillic_direct():
    assert lookup("Иванов") != []
    assert share_cluster("Иванов", "Ivanov")


# ── Edge cases ────────────────────────────────────────────────────────────────

def test_whitespace_only_returns_empty():
    assert lookup("   ") == []


def test_single_char_does_not_crash():
    result = lookup("A")
    assert result == [] or isinstance(result, list)


def test_numbers_return_empty():
    assert lookup("12345") == []


def test_very_long_input_returns_empty():
    assert lookup("a" * 1000) == []


def test_mixed_script_input():
    # Token loop hits "陈" directly
    assert lookup("Chan 陈") != []


def test_leading_trailing_whitespace_handled():
    assert lookup("  Chan  ") == lookup("Chan")


def test_case_insensitive_lookup():
    assert share_cluster("CHAN", "chan")
    assert share_cluster("Chan", "CHAN")


# ── Multi-word token lookup (extended) ───────────────────────────────────────

def test_multi_word_arabic():
    assert share_cluster("Mohammed Al-Rashid", "Muhammad")


def test_multi_word_japanese():
    assert share_cluster("Sato Kenji", "Sato")


def test_multi_word_no_match_returns_empty():
    assert lookup("Smith Johnson Williams") == []


# ── Japanese ──────────────────────────────────────────────────────────────────

def test_sato_lookup():
    assert lookup("Sato") != []
    assert share_cluster("Satō", "Sato")  # macron variant


def test_suzuki_lookup():
    assert lookup("Suzuki") != []


def test_tanaka_lookup():
    assert lookup("Tanaka") != []


def test_japanese_kanji_direct():
    assert lookup("佐藤") != []
    assert share_cluster("佐藤", "Sato")


# ── Indian names ──────────────────────────────────────────────────────────────

def test_hindi_sharma_variants():
    assert lookup("Sharma") != []


def test_hindi_singh_variants():
    assert lookup("Singh") != []


def test_tamil_murugan_variants():
    assert lookup("Murugan") != []


def test_bengali_chatterjee_variants():
    assert lookup("Chatterjee") != []
    assert share_cluster("Chatterjee", "Chattopadhyay")


# ── Thai ──────────────────────────────────────────────────────────────────────

def test_thai_canonical_self_lookup():
    from name_variants import ALL_TABLES
    thai_table = ALL_TABLES["thai"]
    assert len(thai_table) > 0
    some_canonical = next(iter(thai_table))
    assert any(some_canonical in c for c in lookup(some_canonical))


def test_thai_romanization_lookup():
    from name_variants import ALL_TABLES
    for canonical, variants in ALL_TABLES["thai"].items():
        if variants:
            assert share_cluster(variants[0], canonical)
            break


# ── Greek ─────────────────────────────────────────────────────────────────────

def test_greek_papadopoulos_variants():
    assert lookup("Papadopoulos") != []


def test_greek_canonical_self_lookup():
    from name_variants import ALL_TABLES
    some_canonical = next(iter(ALL_TABLES["greek"]))
    assert any(some_canonical in c for c in lookup(some_canonical))


# ── Turkish ───────────────────────────────────────────────────────────────────

def test_turkish_yilmaz_variants():
    assert lookup("Yilmaz") != []
    assert share_cluster("Yilmaz", "Yılmaz")


# ── Persian ───────────────────────────────────────────────────────────────────

def test_persian_mohammadi_variants():
    assert lookup("Mohammadi") != []


# ── Hebrew ────────────────────────────────────────────────────────────────────

def test_hebrew_cohen_variants():
    assert lookup("Cohen") != []
    assert share_cluster("Cohen", "Kohen")


# ── Indonesian/Malay ──────────────────────────────────────────────────────────

def test_indonesian_santoso_variants():
    assert lookup("Santoso") != []


def test_malay_rahman_variants():
    assert lookup("Rahman") != []
