"""
name-variants — multilingual name romanization lookup tables.

Usage:
    from name_variants import lookup, share_cluster, ALL_TABLES

    lookup("Chan")              # → [NameCluster(chinese, ...), ...]
    share_cluster("Chan", "Chen")  # → True
"""

from __future__ import annotations

import unicodedata as _ud
from dataclasses import dataclass
from typing import NotRequired, TypedDict


class NameEntry(TypedDict):
    forms: list[str]
    frequency: NotRequired[int]
    dialects: NotRequired[dict[str, str]]


from name_variants.arabic_names import ARABIC_NAME_VARIANTS
from name_variants.chinese_given_names import CHINESE_GIVEN_NAME_VARIANTS
from name_variants.chinese_surnames import CHINESE_SURNAME_VARIANTS
from name_variants.greek_names import GREEK_NAME_VARIANTS
from name_variants.hebrew_names import HEBREW_NAME_VARIANTS
from name_variants.indian_names_bengali import INDIAN_NAMES_BENGALI
from name_variants.indian_names_hindi import INDIAN_NAMES_HINDI
from name_variants.indian_names_tamil import INDIAN_NAMES_TAMIL
from name_variants.indonesian_malay_names import INDONESIAN_MALAY_NAME_VARIANTS
from name_variants.japanese_given_names import JAPANESE_GIVEN_NAME_VARIANTS
from name_variants.japanese_surnames import JAPANESE_SURNAME_VARIANTS
from name_variants.korean_given_names import KOREAN_GIVEN_NAME_VARIANTS
from name_variants.korean_surnames import KOREAN_SURNAME_VARIANTS
from name_variants.persian_names import PERSIAN_NAME_VARIANTS
from name_variants.russian_surnames import RUSSIAN_SURNAME_VARIANTS
from name_variants.thai_names import THAI_NAME_VARIANTS
from name_variants.turkish_names import TURKISH_NAME_VARIANTS
from name_variants.vietnamese_surnames import VIETNAMESE_SURNAME_VARIANTS

@dataclass(frozen=True)
class NameCluster:
    """Equivalence class of name representations — all forms are co-equal."""

    forms: frozenset[str]
    language: str
    frequency: int | None = None

    def __contains__(self, text: str) -> bool:
        t = text.strip()
        return t in self.forms or t.lower() in self.forms

    def __iter__(self):
        return iter(self.forms)

    def __len__(self) -> int:
        return len(self.forms)

    def __repr__(self) -> str:
        return f"NameCluster(language={self.language!r}, {len(self.forms)} forms)"


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
    "chinese_given": CHINESE_GIVEN_NAME_VARIANTS,
    "korean_given": KOREAN_GIVEN_NAME_VARIANTS,
    "japanese_given": JAPANESE_GIVEN_NAME_VARIANTS,
}

_CLUSTERS: list["NameCluster"] | None = None
_FORM_INDEX: dict[str, list["NameCluster"]] | None = None
_DIALECT_INDEX: dict[str, str] | None = None


def _build_clusters() -> tuple[list["NameCluster"], dict[str, list["NameCluster"]]]:
    clusters: list[NameCluster] = []
    form_index: dict[str, list[NameCluster]] = {}

    for language, table in ALL_TABLES.items():
        for storage_key, entry in table.items():
            forms_list: list[str] = entry["forms"]
            frequency: int | None = entry.get("frequency")

            forms = frozenset(
                {storage_key}
                | {v.lower().strip() for v in forms_list if v.strip()}
            )
            cluster = NameCluster(forms=forms, language=language, frequency=frequency)
            clusters.append(cluster)
            for form in forms:
                form_index.setdefault(form, []).append(cluster)

    return clusters, form_index


def _get_form_index() -> dict[str, list["NameCluster"]]:
    global _CLUSTERS, _FORM_INDEX
    if _FORM_INDEX is None:
        _CLUSTERS, _FORM_INDEX = _build_clusters()
    return _FORM_INDEX



def lookup(text: str) -> list[NameCluster]:
    """
    Return all NameClusters that contain this text as a member form.

    Results are sorted by frequency descending (highest bearer count first).
    Returns [] for unknown names or empty input.

    Examples:
        lookup("Chan")   → [NameCluster(chinese, ...), NameCluster(korean_given, ...)]
        lookup("Nguyen") → [NameCluster(vietnamese, ...)]
        lookup("Smith")  → []
    """
    if not text or not text.strip():
        return []

    idx = _get_form_index()
    seen: set[NameCluster] = set()
    result: list[NameCluster] = []

    def _collect(key: str) -> None:
        for cluster in idx.get(key, []):
            if cluster not in seen:
                seen.add(cluster)
                result.append(cluster)

    key = text.strip()
    _collect(key)
    key_lower = key.lower()
    if key_lower != key:
        _collect(key_lower)
    for token in key_lower.split():
        _collect(token)

    result.sort(key=lambda c: c.frequency or 0, reverse=True)
    return result


def share_cluster(a: str, b: str) -> bool:
    """
    Return True iff both strings appear in any common NameCluster.

    Returns False if either string is empty or unknown.

    Examples:
        share_cluster("Chan", "Chen")  → True
        share_cluster("Chan", "Li")    → False
    """
    if not a or not b:
        return False
    a_set = set(lookup(a))
    return any(c in a_set for c in lookup(b))



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



def _build_dialect_index() -> dict[str, str]:
    index: dict[str, str] = {}
    for table in ALL_TABLES.values():
        for entry in table.values():
            for form, dialect in entry.get("dialects", {}).items():
                index[form.lower()] = dialect
    return index


def _get_dialect_index() -> dict[str, str]:
    global _DIALECT_INDEX
    if _DIALECT_INDEX is None:
        _DIALECT_INDEX = _build_dialect_index()
    return _DIALECT_INDEX


def lookup_dialect(text: str) -> str | None:
    """
    Return the romanization dialect/system for this variant string.

    Returns one of: "mandarin_pinyin", "cantonese", "hokkien", "hakka",
    "teochew", "wade_giles", "traditional", "simplified", "postal"

    Returns None for non-Chinese names or untagged variants.
    """
    return _get_dialect_index().get(text.lower().strip())


__all__ = [
    "NameCluster",
    "NameEntry",
    "lookup",
    "share_cluster",
    "ALL_TABLES",
    "normalize",
    "lookup_dialect",
]
