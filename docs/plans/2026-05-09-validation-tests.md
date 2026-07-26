# name-variants: Validation Test Coverage Plan

**Date:** 2026-05-09
**Triggered by:** veil integration work — the veil project uses `lookup_key()` for cross-script entity merging, exposing gaps in the current test suite.

## What Is Already Covered

`tests/test_lookup.py` covers:
- Table completeness (all 15 tables, lowercase romanizations, non-empty keys)
- Chinese: Chan/Chen, Tan/Chen (Hokkien), Traditional ↔ Simplified, Xu/Hui, Wang/Wong
- Korean: Park/Bak, Lee/Yi/Rhee, Choi/Choe, Jung/Chung
- `lookup_candidates` ambiguity: Lee (3 scripts), Ng (2 Chinese), Nguyen (unambiguous)
- Unknown names: Kowalski, Smith, Johnson
- Edge: empty string

## What Is Missing

### 1. Vietnamese — diacritics and Romanization variants

The existing tests only test `lookup_candidates("Nguyen")` — no direct `lookup_key` round-trip with diacritics.

```python
def test_nguyen_lookup_key_direct():
    assert lookup_key("Nguyen") is not None
    assert lookup_key("Nguyen") == lookup_key("nguyễn")

def test_tran_variants():
    # Trần → tran, tràn, tran
    assert lookup_key("Tran") is not None
    assert lookup_key("Tran") == lookup_key("trần")

def test_le_variants():
    assert lookup_key("Le") == lookup_key("lê")

def test_pham_variants():
    assert lookup_key("Pham") == lookup_key("phạm")

def test_hoang_variants():
    assert lookup_key("Hoang") == lookup_key("hoàng")
```

### 2. Arabic — Muhammad/Mohammed and common variants

```python
def test_muhammad_and_mohammed_same_key():
    assert lookup_key("Muhammad") is not None
    assert lookup_key("Muhammad") == lookup_key("Mohammed")
    assert lookup_key("Muhammad") == lookup_key("Mohamed")
    assert lookup_key("Muhammad") == lookup_key("Mohammad")

def test_ali_variants():
    assert lookup_key("Ali") is not None

def test_hassan_variants():
    assert lookup_key("Hassan") == lookup_key("Hasan")

def test_arabic_script_direct():
    # Native script keys should return themselves
    assert lookup_key("محمد") is not None
```

### 3. Russian — Ivanov/Ivanoff and transliteration variants

```python
def test_ivanov_and_ivanoff_same_key():
    assert lookup_key("Ivanov") is not None
    assert lookup_key("Ivanov") == lookup_key("Ivanoff")

def test_sokolov_variants():
    # Sokolov / Sokoloff / Sokolov
    assert lookup_key("Sokolov") == lookup_key("Sokoloff")

def test_petrov_variants():
    assert lookup_key("Petrov") is not None

def test_cyrillic_direct():
    assert lookup_key("Иванов") is not None
    assert lookup_key("Иванов") == lookup_key("Ivanov")
```

### 4. Japanese — Kanji and romaji round-trips

```python
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
```

### 5. Indian names (Hindi, Tamil, Bengali)

```python
def test_hindi_sharma_variants():
    assert lookup_key("Sharma") is not None

def test_hindi_singh_variants():
    assert lookup_key("Singh") is not None

def test_tamil_murugan_variants():
    assert lookup_key("Murugan") is not None

def test_bengali_chatterjee_variants():
    # Chatterjee / Chattopadhyay
    assert lookup_key("Chatterjee") is not None
    assert lookup_key("Chatterjee") == lookup_key("Chattopadhyay")
```

### 6. Thai names

```python
def test_thai_script_direct():
    # At least one Thai canonical key is resolvable
    from name_variants import ALL_TABLES
    thai_table = ALL_TABLES["thai"]
    assert len(thai_table) > 0
    some_canonical = next(iter(thai_table))
    assert lookup_key(some_canonical) == some_canonical

def test_thai_romanization_lookup():
    # Sombat, Somchai etc. — pick a real entry from the table
    from name_variants import ALL_TABLES
    thai_table = ALL_TABLES["thai"]
    for canonical, variants in thai_table.items():
        if variants:
            assert lookup_key(variants[0]) == canonical
            break
```

### 7. Greek, Turkish, Persian, Hebrew, Indonesian/Malay

Same pattern for the remaining 5 language tables — each should have at least:
1. A direct canonical key self-lookup test
2. A romanization-to-canonical round-trip test
3. A variants-match test (if multiple romanizations exist for the same name)

```python
# Greek
def test_greek_papadopoulos_variants():
    assert lookup_key("Papadopoulos") is not None

def test_greek_script_direct():
    from name_variants import ALL_TABLES
    some_canonical = next(iter(ALL_TABLES["greek"]))
    assert lookup_key(some_canonical) == some_canonical

# Turkish
def test_turkish_yilmaz_variants():
    assert lookup_key("Yilmaz") is not None  # Yılmaz with dotless-i
    assert lookup_key("Yilmaz") == lookup_key("Yılmaz")

# Persian
def test_persian_mohammadi_variants():
    assert lookup_key("Mohammadi") is not None

# Hebrew
def test_hebrew_cohen_variants():
    assert lookup_key("Cohen") is not None
    assert lookup_key("Cohen") == lookup_key("Kohen")

# Indonesian/Malay
def test_indonesian_santoso_variants():
    assert lookup_key("Santoso") is not None

def test_malay_rahman_variants():
    assert lookup_key("Rahman") is not None
```

### 8. Edge Cases

```python
def test_whitespace_only_returns_none():
    assert lookup_key("   ") is None

def test_single_char_returns_none_or_valid():
    # Single letters should not crash
    result = lookup_key("A")
    assert result is None or isinstance(result, str)

def test_numbers_return_none():
    assert lookup_key("12345") is None

def test_very_long_input_returns_none():
    assert lookup_key("a" * 1000) is None

def test_mixed_script_input():
    # "Chan 陈" — token lookup should find 陈 directly
    assert lookup_key("Chan 陈") is not None

def test_leading_trailing_whitespace_handled():
    assert lookup_key("  Chan  ") == lookup_key("Chan")

def test_case_insensitive_lookup():
    assert lookup_key("CHAN") == lookup_key("chan")
    assert lookup_key("Chan") == lookup_key("CHAN")
```

### 9. Multi-word Token Lookup (beyond Chan Wai Ming)

```python
def test_multi_word_arabic():
    # "Mohammed Al-Rashid" — first token "mohammed" matches
    assert lookup_key("Mohammed Al-Rashid") == lookup_key("Muhammad")

def test_multi_word_japanese():
    assert lookup_key("Sato Kenji") == lookup_key("Sato")

def test_multi_word_no_match_returns_none():
    assert lookup_key("Smith Johnson Williams") is None
```

## Priority Order

1. **Vietnamese + Arabic + Russian** — highest-value gaps for veil's cross-script merging
2. **Japanese** — large surname table, no coverage
3. **Edge cases** — prevent crashes on unexpected input
4. **Indian + Thai + Greek + Turkish + Persian + Hebrew + Indonesian** — completeness

## Implementation Notes

- These should live in `tests/test_lookup.py` alongside existing tests (same file, new sections)
- Add a `conftest.py` with a fixture that validates all 15 table entries can be self-looked-up (canonical key → same canonical) as a property test, catching future regressions when new entries are added
- Consider adding `pytest-parametrize` for the per-language variant tests to avoid boilerplate
