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

import unicodedata as _ud

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
    "vietnamese": VIETNAMESE_SURNAME_VARIANTS,
    "korean": KOREAN_SURNAME_VARIANTS,
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

# Lazy-built inverted index: romanization (lowercase) → canonical key (last-write-wins)
_INDEX: dict[str, str] | None = None
# Lazy-built variants map: canonical key → variants list
_VARIANTS: dict[str, list[str]] | None = None
# Lazy-built multi-match map: romanization (lowercase) → all canonical keys across all tables
_CANDIDATES: dict[str, list[str]] | None = None


def _build_index() -> tuple[dict[str, str], dict[str, list[str]], dict[str, list[str]]]:
    index: dict[str, str] = {}
    variants: dict[str, list[str]] = {}
    candidates: dict[str, list[str]] = {}
    for table in ALL_TABLES.values():
        for canonical, variants_list in table.items():
            index[canonical] = canonical
            variants[canonical] = variants_list
            # candidates: canonical maps to itself for direct script-form lookup
            if canonical not in candidates.get(canonical, []):
                candidates.setdefault(canonical, []).append(canonical)
            for variant in variants_list:
                v = variant.lower().strip()
                if v:
                    index[v] = canonical  # last-write-wins — preserves lookup_key behaviour
                    if canonical not in candidates.get(v, []):
                        candidates.setdefault(v, []).append(canonical)
    return index, variants, candidates


def _get_index() -> dict[str, str]:
    global _INDEX, _VARIANTS, _CANDIDATES
    if _INDEX is None:
        _INDEX, _VARIANTS, _CANDIDATES = _build_index()
    return _INDEX


def _get_variants() -> dict[str, list[str]]:
    global _INDEX, _VARIANTS, _CANDIDATES
    if _VARIANTS is None:
        _INDEX, _VARIANTS, _CANDIDATES = _build_index()
    return _VARIANTS


def _get_candidates() -> dict[str, list[str]]:
    global _INDEX, _VARIANTS, _CANDIDATES
    if _CANDIDATES is None:
        _INDEX, _VARIANTS, _CANDIDATES = _build_index()
    return _CANDIDATES


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


def lookup_candidates(text: str) -> list[str]:
    """
    Return all canonical keys that have this romanization as a variant.

    Unlike lookup_key(), which returns one result via last-write-wins,
    this returns every canonical key across all 15 language tables that
    lists the input as a variant — ordered by table iteration order.

    Examples:
        lookup_candidates("Lee")    → ["이", "李", "lê"]  (Korean, Chinese, Vietnamese)
        lookup_candidates("Ng")     → ["黄", "吴"]         (ambiguous Hokkien)
        lookup_candidates("Nguyen") → ["nguyễn"]           (unambiguous)
        lookup_candidates("Smith")  → []
    """
    if not text:
        return []
    cands = _get_candidates()
    seen: set[str] = set()
    result: list[str] = []

    def _collect(lookup_key: str) -> None:
        for canonical in cands.get(lookup_key, []):
            if canonical not in seen:
                seen.add(canonical)
                result.append(canonical)

    key = text.strip()
    _collect(key)
    key_lower = key.lower()
    if key_lower != key:
        _collect(key_lower)
    for token in key_lower.split():
        _collect(token)

    return result


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


def normalize(text: str, *, strip_diacritics: bool = False) -> str:
    """
    NFC + casefold + collapse whitespace + strip Unicode format characters.

    strip_diacritics=True additionally removes combining marks (NFD→strip Mn→NFC),
    e.g. "Nguyễn" → "nguyen".  Default False preserves diacritics for round-trip
    lookup.
    """
    # Strip Unicode format characters (zero-width spaces, BOM, soft hyphens, …)
    text = "".join(ch for ch in text if _ud.category(ch) != "Cf")
    text = _ud.normalize("NFC", text)
    text = text.casefold()
    text = " ".join(text.split())
    if strip_diacritics:
        text = _ud.normalize("NFD", text)
        text = "".join(ch for ch in text if _ud.category(ch) != "Mn")
        text = _ud.normalize("NFC", text)
    return text


def canonicalize(text: str, fallback: str = "passthrough") -> str:
    """
    Return the canonical key for a name, or apply fallback for unknown names.

    Unlike lookup_key(), this never returns None.

    fallback="passthrough"  → return text.strip() as-is (default)
    fallback="lower"        → return text.lower().strip()
    """
    key = lookup_key(text)
    if key is not None:
        return key
    if fallback == "lower":
        return text.lower().strip()
    return text.strip()


def is_variant(a: str, b: str) -> bool:
    """
    Return True iff both strings resolve to the same canonical key.

    Returns False if either string is empty or unknown.
    """
    if not a or not b:
        return False
    ka = lookup_key(a)
    if ka is None:
        return False
    return ka == lookup_key(b)


def _get_language_for_canonical(canonical: str) -> str | None:
    """Return the language table name for a canonical key."""
    for lang, table in ALL_TABLES.items():
        if canonical in table:
            return lang
    return None


def get_language_for_canonical(canonical: str) -> str | None:
    """Return the language table name for a canonical key, or None if not found."""
    return _get_language_for_canonical(canonical)


def get_frequency(canonical: str) -> int | None:
    """Return approximate global bearer count for a canonical key, or None."""
    from name_variants.frequencies import ALL_FREQUENCIES

    return ALL_FREQUENCIES.get(canonical)


def language_distribution(text: str) -> dict[str, float]:
    """
    Return a probability distribution over languages for this name.

    Uses lookup_candidates() to find all matching canonicals, then weights
    them by population frequency. Returns {} for unknown names.

    Example:
        language_distribution("Lee") -> {"korean": 0.82, "chinese": 0.15, "vietnamese": 0.03}
    """
    from name_variants.frequencies import ALL_FREQUENCIES

    candidates = lookup_candidates(text)
    if not candidates:
        return {}

    # Build (canonical, language, frequency) triples
    triples = []
    for canonical in candidates:
        lang = _get_language_for_canonical(canonical)
        freq = ALL_FREQUENCIES.get(canonical, 0)
        triples.append((canonical, lang, freq))

    total = sum(f for _, _, f in triples)
    if total == 0:
        # No frequency data — return uniform distribution
        langs = list({lang for _, lang, _ in triples})
        weight = 1.0 / len(langs)
        return {lang: weight for lang in langs}

    dist: dict[str, float] = {}
    for _, lang, freq in triples:
        if lang:
            dist[lang] = dist.get(lang, 0.0) + freq / total
    return dist


def lookup_dialect(text: str) -> str | None:
    """
    Return the romanization dialect/system for this variant string.

    Returns one of: "mandarin_pinyin", "cantonese", "hokkien", "hakka",
    "teochew", "wade_giles", "traditional", "simplified"

    Returns None for non-Chinese names or untagged variants.
    """
    from name_variants.chinese_surnames import CHINESE_ROMANIZATION_DIALECTS

    return CHINESE_ROMANIZATION_DIALECTS.get(text.lower().strip())


__all__ = [
    "lookup_key",
    "lookup_all",
    "lookup_candidates",
    "ALL_TABLES",
    "normalize",
    "canonicalize",
    "is_variant",
    "get_frequency",
    "get_language_for_canonical",
    "language_distribution",
    "lookup_dialect",
]
