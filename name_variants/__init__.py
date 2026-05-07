"""
name-variants — multilingual name romanization lookup tables.

Usage:
    from name_variants import lookup_key, ALL_TABLES

    lookup_key("Chan")     # → "陈"
    lookup_key("Nguyen")   # → "nguyễn"
    lookup_key("Park")     # → "박"
    lookup_key("Unknown")  # → None
"""

from __future__ import annotations

from name_variants.arabic_names import ARABIC_NAME_VARIANTS
from name_variants.chinese_surnames import CHINESE_SURNAME_VARIANTS
from name_variants.greek_names import GREEK_NAME_VARIANTS
from name_variants.hebrew_names import HEBREW_NAME_VARIANTS
from name_variants.indian_names_bengali import INDIAN_NAMES_BENGALI
from name_variants.indian_names_hindi import INDIAN_NAMES_HINDI
from name_variants.indian_names_tamil import INDIAN_NAMES_TAMIL
from name_variants.indonesian_malay_names import INDONESIAN_MALAY_NAME_VARIANTS
from name_variants.japanese_surnames import JAPANESE_SURNAME_VARIANTS
from name_variants.korean_surnames import KOREAN_SURNAME_VARIANTS
from name_variants.persian_names import PERSIAN_NAME_VARIANTS
from name_variants.russian_surnames import RUSSIAN_SURNAME_VARIANTS
from name_variants.thai_names import THAI_NAME_VARIANTS
from name_variants.turkish_names import TURKISH_NAME_VARIANTS
from name_variants.vietnamese_surnames import VIETNAMESE_SURNAME_VARIANTS

ALL_TABLES: dict[str, dict[str, list[str]]] = {
    "chinese": CHINESE_SURNAME_VARIANTS,
    "arabic": ARABIC_NAME_VARIANTS,
    "japanese": JAPANESE_SURNAME_VARIANTS,
    "korean": KOREAN_SURNAME_VARIANTS,
    "vietnamese": VIETNAMESE_SURNAME_VARIANTS,
    "indian_hindi": INDIAN_NAMES_HINDI,
    "indian_tamil": INDIAN_NAMES_TAMIL,
    "indian_bengali": INDIAN_NAMES_BENGALI,
    "persian": PERSIAN_NAME_VARIANTS,
    "hebrew": HEBREW_NAME_VARIANTS,
    "thai": THAI_NAME_VARIANTS,
    "greek": GREEK_NAME_VARIANTS,
    "turkish": TURKISH_NAME_VARIANTS,
    "russian": RUSSIAN_SURNAME_VARIANTS,
    "indonesian_malay": INDONESIAN_MALAY_NAME_VARIANTS,
}

# Lazy-built inverted index: romanization (lowercase) → canonical key
_INDEX: dict[str, str] | None = None
# Lazy-built variants map: canonical key → variants list (last-write-wins, same as _INDEX)
_VARIANTS: dict[str, list[str]] | None = None


def _build_index() -> tuple[dict[str, str], dict[str, list[str]]]:
    index: dict[str, str] = {}
    variants: dict[str, list[str]] = {}
    for table in ALL_TABLES.values():
        for canonical, variants_list in table.items():
            # The canonical key itself maps to itself
            index[canonical] = canonical
            # Last-write-wins for both dicts (same iteration order)
            variants[canonical] = variants_list
            for variant in variants_list:
                v = variant.lower().strip()
                if v:
                    index[v] = canonical
    return index, variants


def _get_index() -> dict[str, str]:
    global _INDEX, _VARIANTS
    if _INDEX is None:
        _INDEX, _VARIANTS = _build_index()
    return _INDEX


def _get_variants() -> dict[str, list[str]]:
    global _INDEX, _VARIANTS
    if _VARIANTS is None:
        _INDEX, _VARIANTS = _build_index()
    return _VARIANTS


def lookup_key(text: str) -> str | None:
    """
    Return the canonical key for a name, or None if not in any table.

    The canonical key is always the native script form (Simplified Chinese
    character, Arabic word, Hangul block, Cyrillic word, etc.).

    Callers should casefold and normalize whitespace before passing text.
    This function does a basic casefold internally.

    Examples:
        lookup_key("Chan")     → "陈"
        lookup_key("陳")       → "陈"   (Traditional → looks up as-is; caller
                                         should run opencc first for best results)
        lookup_key("Nguyen")   → "nguyễn"
        lookup_key("Unknown")  → None
    """
    idx = _get_index()

    # Direct lookup (handles native script keys)
    key = text.strip()
    if key in idx:
        return idx[key]

    # Casefolded lookup (handles romanizations)
    key_lower = key.lower()
    if key_lower in idx:
        return idx[key_lower]

    # Token-by-token: "Chan Wai Ming" → try "chan", "wai", "ming"
    for token in key_lower.split():
        if token in idx:
            return idx[token]

    return None


def lookup_all(text: str) -> tuple[str, list[str]] | None:
    """
    Return (canonical_key, all_variants) for a name, or None if unknown.

    Examples:
        lookup_all("Chan")   → ("陈", ["陳", "chen", "chan", "tan", ...])
        lookup_all("Smith")  → None
        lookup_all("")       → None
    """
    key = lookup_key(text)
    if key is None:
        return None
    variants = _get_variants().get(key)
    if variants is None:
        return key, []
    return key, variants


__all__ = ["lookup_key", "lookup_all", "ALL_TABLES"]
