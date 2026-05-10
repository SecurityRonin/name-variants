#!/usr/bin/env python3
"""
Generate name-variants-rs/src/generated.rs from name_variants/*.py tables.

Usage (from repo root):
    python codegen/gen_rust.py

The generated file is committed to source — Rust users do not need Python.
Re-run whenever a Python table is updated.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
PACKAGE_DIR = REPO_ROOT / "name_variants"
OUTPUT_PATH = REPO_ROOT / "name-variants-rs" / "src" / "generated.rs"

# Module path → (variable name holding the dict, language label matching ALL_TABLES keys)
TABLE_MODULES: list[tuple[str, str, str]] = [
    ("chinese_surnames", "CHINESE_SURNAME_VARIANTS", "chinese"),
    ("arabic_names", "ARABIC_NAME_VARIANTS", "arabic"),
    ("japanese_surnames", "JAPANESE_SURNAME_VARIANTS", "japanese"),
    ("korean_surnames", "KOREAN_SURNAME_VARIANTS", "korean"),
    ("vietnamese_surnames", "VIETNAMESE_SURNAME_VARIANTS", "vietnamese"),
    ("indian_names_hindi", "INDIAN_NAMES_HINDI", "indian_hindi"),
    ("indian_names_tamil", "INDIAN_NAMES_TAMIL", "indian_tamil"),
    ("indian_names_bengali", "INDIAN_NAMES_BENGALI", "indian_bengali"),
    ("persian_names", "PERSIAN_NAME_VARIANTS", "persian"),
    ("hebrew_names", "HEBREW_NAME_VARIANTS", "hebrew"),
    ("thai_names", "THAI_NAME_VARIANTS", "thai"),
    ("greek_names", "GREEK_NAME_VARIANTS", "greek"),
    ("turkish_names", "TURKISH_NAME_VARIANTS", "turkish"),
    ("russian_surnames", "RUSSIAN_SURNAME_VARIANTS", "russian"),
    ("indonesian_malay_names", "INDONESIAN_MALAY_NAME_VARIANTS", "indonesian_malay"),
    ("chinese_given_names", "CHINESE_GIVEN_NAME_VARIANTS", "chinese_given"),
    ("korean_given_names", "KOREAN_GIVEN_NAME_VARIANTS", "korean_given"),
    ("japanese_given_names", "JAPANESE_GIVEN_NAME_VARIANTS", "japanese_given"),
]


def load_table(module_name: str, var_name: str, language: str = "") -> dict[str, list[str]]:
    """Load a table dict from a name_variants module file."""
    module_path = PACKAGE_DIR / f"{module_name}.py"
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    table = getattr(mod, var_name)
    assert isinstance(table, dict), f"{module_name}.{var_name} is not a dict"
    return table


def build_flat_index(
    tables: list[tuple[str, dict[str, list[str]]]]
) -> dict[str, str]:
    """Build flat {variant_lowercase → canonical_key} index.

    Duplicates (same romanization under multiple entries) keep the first
    occurrence — this mirrors the Python _build_index() behavior.
    """
    index: dict[str, str] = {}
    for _name, table in tables:
        for canonical, variants in table.items():
            # canonical key maps to itself (for direct script-form lookup)
            if canonical not in index:
                index[canonical] = canonical
            for variant in variants:
                v = variant.lower().strip()
                if v and v not in index:
                    index[v] = canonical
    return index


def build_variants_map(
    tables: list[tuple[str, dict[str, list[str]]]]
) -> dict[str, list[str]]:
    """canonical_key → variants list (first-occurrence-wins, same as build_flat_index)."""
    variants_map: dict[str, list[str]] = {}
    for _name, table in tables:
        for canonical, variants in table.items():
            if canonical not in variants_map:
                variants_map[canonical] = variants
    return variants_map


def build_language_map(
    tables: list[tuple[str, str, dict[str, list[str]]]]
) -> dict[str, str]:
    """canonical_key → language label (first-occurrence-wins)."""
    language_map: dict[str, str] = {}
    for language, table in tables:
        for canonical in table:
            if canonical not in language_map:
                language_map[canonical] = language
    return language_map


def build_candidates_map(
    tables: list[tuple[str, dict[str, list[str]]]]
) -> dict[str, list[str]]:
    """variant_lowercase → [all canonical keys that list it as a variant].

    Mirrors Python _build_index() candidates logic:
    - Each canonical maps to itself (for direct script-form lookup).
    - Each romanization variant (lowercased) maps to every canonical that has it.
    - Order matches table iteration order; duplicates are deduplicated preserving first.
    """
    candidates: dict[str, list[str]] = {}

    def _add(lookup_key: str, canonical: str) -> None:
        lst = candidates.setdefault(lookup_key, [])
        if canonical not in lst:
            lst.append(canonical)

    for _name, table in tables:
        for canonical, variants in table.items():
            # canonical maps to itself
            _add(canonical, canonical)
            for variant in variants:
                v = variant.lower().strip()
                if v:
                    _add(v, canonical)
    return candidates


def escape_rust_str(s: str) -> str:
    """Escape a string for use in a Rust string literal."""
    return s.replace("\\", "\\\\").replace('"', '\\"')


def generate(
    index: dict[str, str],
    variants_map: dict[str, list[str]],
    candidates_map: dict[str, list[str]],
    language_map: dict[str, str],
) -> str:
    """Render the Rust generated.rs content."""
    # INDEX entries (variant → canonical)
    index_entries = "\n".join(
        f'    "{escape_rust_str(k)}" => "{escape_rust_str(v)}",'
        for k, v in sorted(index.items())
    )

    # VARIANTS / CANDIDATES entries (key → &[values])
    def fmt_list(vs: list[str]) -> str:
        items = ", ".join(f'"{escape_rust_str(v)}"' for v in vs)
        return f"&[{items}]"

    variants_entries = "\n".join(
        f'    "{escape_rust_str(k)}" => {fmt_list(vs)},'
        for k, vs in sorted(variants_map.items())
    )

    candidates_entries = "\n".join(
        f'    "{escape_rust_str(k)}" => {fmt_list(vs)},'
        for k, vs in sorted(candidates_map.items())
    )

    language_entries = "\n".join(
        f'    "{escape_rust_str(k)}" => "{escape_rust_str(v)}",'
        for k, v in sorted(language_map.items())
    )

    return f"""\
// GENERATED FILE — do not edit by hand.
// Run: python codegen/gen_rust.py
// to regenerate from name_variants/*.py source tables.
//
// INDEX entries: {len(index)}
// VARIANTS entries: {len(variants_map)}
// CANDIDATES entries: {len(candidates_map)}
// LANGUAGE entries: {len(language_map)}

use phf::phf_map;

pub(crate) static INDEX: phf::Map<&'static str, &'static str> = phf_map! {{
{index_entries}
}};

pub(crate) static VARIANTS: phf::Map<&'static str, &'static [&'static str]> = phf_map! {{
{variants_entries}
}};

pub(crate) static CANDIDATES: phf::Map<&'static str, &'static [&'static str]> = phf_map! {{
{candidates_entries}
}};

pub(crate) static LANGUAGE: phf::Map<&'static str, &'static str> = phf_map! {{
{language_entries}
}};
"""


def main() -> None:
    # tables_raw: (module_name, table_dict) for index/variants/candidates
    tables_raw = []
    # tables_lang: (language_label, table_dict) for language map
    tables_lang = []
    for module_name, var_name, language in TABLE_MODULES:
        table = load_table(module_name, var_name)
        tables_raw.append((module_name, table))
        tables_lang.append((language, table))
        print(f"  loaded {module_name}: {len(table)} entries", file=sys.stderr)

    index = build_flat_index(tables_raw)
    variants_map = build_variants_map(tables_raw)
    candidates_map = build_candidates_map(tables_raw)
    language_map = build_language_map(tables_lang)
    print(
        f"  flat index: {len(index)} entries, variants: {len(variants_map)} keys,"
        f" candidates: {len(candidates_map)} keys, language: {len(language_map)} keys",
        file=sys.stderr,
    )

    missing = set(index.values()) - set(variants_map.keys())
    if missing:
        print(
            f"  WARNING: {len(missing)} canonical keys in INDEX have no VARIANTS entry:"
            f" {sorted(missing)[:5]}...",
            file=sys.stderr,
        )

    content = generate(index, variants_map, candidates_map, language_map)
    OUTPUT_PATH.write_text(content, encoding="utf-8")
    print(f"  wrote {OUTPUT_PATH}", file=sys.stderr)


if __name__ == "__main__":
    main()
