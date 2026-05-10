"""Tests for normalize() and share_cluster() utility functions."""
import unicodedata

from name_variants import normalize, share_cluster

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


# ── share_cluster ─────────────────────────────────────────────────────────────

def test_is_variant_same_chinese():
    assert share_cluster("Chan", "Chen") is True


def test_is_variant_hokkien_mandarin():
    # Hokkien Tan = Mandarin Chen = 陈
    assert share_cluster("Tan", "Chen") is True


def test_is_variant_different_names():
    assert share_cluster("Chan", "Kim") is False


def test_is_variant_both_unknown():
    assert share_cluster("Smith", "Smyth") is False


def test_is_variant_one_unknown():
    assert share_cluster("Chan", "Smith") is False


def test_is_variant_empty_strings():
    assert share_cluster("", "") is False


def test_is_variant_one_empty():
    assert share_cluster("Chan", "") is False
    assert share_cluster("", "Chan") is False


def test_is_variant_korean_romanizations():
    assert share_cluster("Park", "Bak") is True
    assert share_cluster("Lee", "Yi") is True


def test_is_variant_case_insensitive():
    assert share_cluster("CHAN", "chen") is True
