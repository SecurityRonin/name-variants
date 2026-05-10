"""Tests for normalize(), is_variant(), and canonicalize() utility functions."""
import unicodedata

from name_variants import canonicalize, is_variant, normalize


# ── normalize ─────────────────────────────────────────────────────────────────

def test_normalize_casefold():
    assert normalize("CHAN") == "chan"
    assert normalize("Chan") == "chan"


def test_normalize_whitespace_strip():
    assert normalize("  chan  ") == "chan"


def test_normalize_whitespace_collapse():
    assert normalize("chan  wai   ming") == "chan wai ming"


def test_normalize_zero_width_space():
    assert normalize("chan​") == "chan"


def test_normalize_zero_width_joiner():
    assert normalize("chan‍") == "chan"


def test_normalize_bom():
    assert normalize("﻿chan") == "chan"


def test_normalize_nfc_composed():
    # NFD decomposed 'é' should round-trip to NFC 'é'
    nfd = unicodedata.normalize("NFD", "é")
    assert normalize(nfd) == "é"


def test_normalize_keeps_diacritics():
    # Default: diacritics preserved
    assert normalize("nguyễn") == "nguyễn"
    assert normalize("Nguyễn") == "nguyễn"


def test_normalize_strip_diacritics_vietnamese():
    assert normalize("Nguyễn", strip_diacritics=True) == "nguyen"
    assert normalize("nguyễn", strip_diacritics=True) == "nguyen"


def test_normalize_strip_diacritics_turkish():
    assert normalize("Çelik", strip_diacritics=True) == "celik"


def test_normalize_strip_diacritics_arabic_stays():
    # Arabic script has no Latin diacritics — should pass through unchanged
    result = normalize("محمد", strip_diacritics=True)
    assert result == "محمد"


def test_normalize_empty():
    assert normalize("") == ""


def test_normalize_whitespace_only():
    assert normalize("   ") == ""


# ── is_variant ────────────────────────────────────────────────────────────────

def test_is_variant_same_chinese():
    assert is_variant("Chan", "Chen") is True


def test_is_variant_hokkien_mandarin():
    # Hokkien Tan = Mandarin Chen = 陈
    assert is_variant("Tan", "Chen") is True


def test_is_variant_different_names():
    assert is_variant("Chan", "Kim") is False


def test_is_variant_both_unknown():
    assert is_variant("Smith", "Smyth") is False


def test_is_variant_one_unknown():
    assert is_variant("Chan", "Smith") is False


def test_is_variant_empty_strings():
    assert is_variant("", "") is False


def test_is_variant_one_empty():
    assert is_variant("Chan", "") is False
    assert is_variant("", "Chan") is False


def test_is_variant_korean_romanizations():
    assert is_variant("Park", "Bak") is True
    assert is_variant("Lee", "Yi") is True


def test_is_variant_case_insensitive():
    assert is_variant("CHAN", "chen") is True


# ── canonicalize ──────────────────────────────────────────────────────────────

def test_canonicalize_known_name():
    assert canonicalize("Chan") == "陈"


def test_canonicalize_case_insensitive():
    assert canonicalize("CHAN") == "陈"
    assert canonicalize("chan") == "陈"


def test_canonicalize_unknown_passthrough_default():
    result = canonicalize("Smith")
    assert result == "Smith"


def test_canonicalize_unknown_passthrough_explicit():
    result = canonicalize("Smith", fallback="passthrough")
    assert result == "Smith"


def test_canonicalize_unknown_lower():
    result = canonicalize("Smith", fallback="lower")
    assert result == "smith"


def test_canonicalize_unknown_lower_strips():
    result = canonicalize("  Smith  ", fallback="lower")
    assert result == "smith"


def test_canonicalize_returns_str_not_none():
    result = canonicalize("UnknownXyz")
    assert isinstance(result, str)


def test_canonicalize_passthrough_strips_whitespace():
    result = canonicalize("  Smith  ")
    assert result == "Smith"


def test_canonicalize_known_vietnamese():
    assert canonicalize("Nguyen") == "nguyễn"


def test_canonicalize_known_korean():
    assert canonicalize("Park") == "박"
