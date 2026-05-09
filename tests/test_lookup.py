"""Tests for lookup_key(), lookup_all(), lookup_candidates(), and ALL_TABLES completeness."""
from name_variants import ALL_TABLES, lookup_all, lookup_candidates, lookup_key

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


# ── lookup_candidates — multi-script ambiguous romanizations ─────────────────

def test_candidates_lee_returns_korean_chinese_vietnamese():
    # "lee" legitimately appears in Korean 이, Chinese 李, and Vietnamese lê
    result = lookup_candidates("Lee")
    assert "이" in result
    assert "李" in result
    assert "lê" in result


def test_candidates_ng_returns_both_chinese_surnames():
    # "ng" is ambiguous between 黄 (Huang) and 吴 (Wu) in Hokkien/Cantonese
    result = lookup_candidates("Ng")
    assert "黄" in result
    assert "吴" in result


def test_candidates_unambiguous_returns_single():
    # "nguyen" only appears under nguyễn
    result = lookup_candidates("Nguyen")
    assert result == ["nguyễn"]


def test_candidates_unknown_returns_empty():
    assert lookup_candidates("Smith") == []
    assert lookup_candidates("") == []


def test_lookup_key_still_wins_korean_for_lee():
    # lookup_key must keep its single-best-match contract — Korean wins for "lee"
    assert lookup_key("Lee") == "이"


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


# ── Vietnamese (extended) ─────────────────────────────────────────────────────

def test_le_variants():
    assert lookup_key("Le") == lookup_key("lê")


def test_pham_variants():
    assert lookup_key("Pham") == lookup_key("phạm")


def test_hoang_variants():
    assert lookup_key("Hoang") == lookup_key("hoàng")


# ── Arabic (extended) ─────────────────────────────────────────────────────────

def test_ali_variants():
    assert lookup_key("Ali") is not None


def test_hassan_variants():
    assert lookup_key("Hassan") == lookup_key("Hasan")


def test_arabic_script_direct():
    assert lookup_key("محمد") is not None


# ── Russian (extended) ────────────────────────────────────────────────────────

def test_sokolov_variants():
    assert lookup_key("Sokolov") == lookup_key("Sokoloff")


def test_petrov_variants():
    assert lookup_key("Petrov") is not None


def test_cyrillic_direct():
    assert lookup_key("Иванов") is not None
    assert lookup_key("Иванов") == lookup_key("Ivanov")


# ── Edge cases ────────────────────────────────────────────────────────────────

def test_whitespace_only_returns_none():
    assert lookup_key("   ") is None


def test_single_char_does_not_crash():
    result = lookup_key("A")
    assert result is None or isinstance(result, str)


def test_numbers_return_none():
    assert lookup_key("12345") is None


def test_very_long_input_returns_none():
    assert lookup_key("a" * 1000) is None


def test_mixed_script_input():
    # Token loop hits "陈" directly
    assert lookup_key("Chan 陈") is not None


def test_leading_trailing_whitespace_handled():
    assert lookup_key("  Chan  ") == lookup_key("Chan")


def test_case_insensitive_lookup():
    assert lookup_key("CHAN") == lookup_key("chan")
    assert lookup_key("Chan") == lookup_key("CHAN")


# ── Multi-word token lookup (extended) ───────────────────────────────────────

def test_multi_word_arabic():
    assert lookup_key("Mohammed Al-Rashid") == lookup_key("Muhammad")


def test_multi_word_japanese():
    assert lookup_key("Sato Kenji") == lookup_key("Sato")


def test_multi_word_no_match_returns_none():
    assert lookup_key("Smith Johnson Williams") is None


# ── Japanese ──────────────────────────────────────────────────────────────────

def test_sato_lookup():
    assert lookup_key("Sato") is not None
    assert lookup_key("Satō") == lookup_key("Sato")  # macron variant


def test_suzuki_lookup():
    assert lookup_key("Suzuki") is not None


def test_tanaka_lookup():
    assert lookup_key("Tanaka") is not None


def test_japanese_kanji_direct():
    assert lookup_key("佐藤") is not None
    assert lookup_key("佐藤") == lookup_key("Sato")


# ── Indian names ──────────────────────────────────────────────────────────────

def test_hindi_sharma_variants():
    assert lookup_key("Sharma") is not None


def test_hindi_singh_variants():
    assert lookup_key("Singh") is not None


def test_tamil_murugan_variants():
    assert lookup_key("Murugan") is not None


def test_bengali_chatterjee_variants():
    assert lookup_key("Chatterjee") is not None
    assert lookup_key("Chatterjee") == lookup_key("Chattopadhyay")


# ── Thai ──────────────────────────────────────────────────────────────────────

def test_thai_canonical_self_lookup():
    from name_variants import ALL_TABLES
    thai_table = ALL_TABLES["thai"]
    assert len(thai_table) > 0
    some_canonical = next(iter(thai_table))
    assert lookup_key(some_canonical) == some_canonical


def test_thai_romanization_lookup():
    from name_variants import ALL_TABLES
    for canonical, variants in ALL_TABLES["thai"].items():
        if variants:
            assert lookup_key(variants[0]) == canonical
            break


# ── Greek ─────────────────────────────────────────────────────────────────────

def test_greek_papadopoulos_variants():
    assert lookup_key("Papadopoulos") is not None


def test_greek_canonical_self_lookup():
    from name_variants import ALL_TABLES
    some_canonical = next(iter(ALL_TABLES["greek"]))
    assert lookup_key(some_canonical) == some_canonical


# ── Turkish ───────────────────────────────────────────────────────────────────

def test_turkish_yilmaz_variants():
    assert lookup_key("Yilmaz") is not None
    assert lookup_key("Yilmaz") == lookup_key("Yılmaz")


# ── Persian ───────────────────────────────────────────────────────────────────

def test_persian_mohammadi_variants():
    assert lookup_key("Mohammadi") is not None


# ── Hebrew ────────────────────────────────────────────────────────────────────

def test_hebrew_cohen_variants():
    assert lookup_key("Cohen") is not None
    assert lookup_key("Cohen") == lookup_key("Kohen")


# ── Indonesian/Malay ──────────────────────────────────────────────────────────

def test_indonesian_santoso_variants():
    assert lookup_key("Santoso") is not None


def test_malay_rahman_variants():
    assert lookup_key("Rahman") is not None
