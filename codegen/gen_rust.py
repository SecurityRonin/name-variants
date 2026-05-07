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

# Module path → variable name holding the dict
TABLE_MODULES: list[tuple[str, str]] = [
    ("chinese_surnames", "CHINESE_SURNAME_VARIANTS"),
    ("arabic_names", "ARABIC_NAME_VARIANTS"),
    ("japanese_surnames", "JAPANESE_SURNAME_VARIANTS"),
    ("korean_surnames", "KOREAN_SURNAME_VARIANTS"),
    ("vietnamese_surnames", "VIETNAMESE_SURNAME_VARIANTS"),
    ("indian_names_hindi", "INDIAN_NAMES_HINDI"),
    ("indian_names_tamil", "INDIAN_NAMES_TAMIL"),
    ("indian_names_bengali", "INDIAN_NAMES_BENGALI"),
    ("persian_names", "PERSIAN_NAME_VARIANTS"),
    ("hebrew_names", "HEBREW_NAME_VARIANTS"),
    ("thai_names", "THAI_NAME_VARIANTS"),
    ("greek_names", "GREEK_NAME_VARIANTS"),
    ("turkish_names", "TURKISH_NAME_VARIANTS"),
    ("russian_surnames", "RUSSIAN_SURNAME_VARIANTS"),
    ("indonesian_malay_names", "INDONESIAN_MALAY_NAME_VARIANTS"),
]


def load_table(module_name: str, var_name: str) -> dict[str, list[str]]:
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


def escape_rust_str(s: str) -> str:
    """Escape a string for use in a Rust string literal."""
    return s.replace("\\", "\\\\").replace('"', '\\"')


def generate(index: dict[str, str], variants_map: dict[str, list[str]]) -> str:
    """Render the Rust generated.rs content."""
    # INDEX entries (variant → canonical)
    index_entries = "\n".join(
        f'    "{escape_rust_str(k)}" => "{escape_rust_str(v)}",'
        for k, v in sorted(index.items())
    )

    # VARIANTS entries (canonical → &[variants])
    def fmt_variants(vs: list[str]) -> str:
        items = ", ".join(f'"{escape_rust_str(v)}"' for v in vs)
        return f"&[{items}]"

    variants_entries = "\n".join(
        f'    "{escape_rust_str(k)}" => {fmt_variants(vs)},'
        for k, vs in sorted(variants_map.items())
    )

    return f"""\
// GENERATED FILE — do not edit by hand.
// Run: python codegen/gen_rust.py
// to regenerate from name_variants/*.py source tables.
//
// INDEX entries: {len(index)}
// VARIANTS entries: {len(variants_map)}

use phf::phf_map;

pub(crate) static INDEX: phf::Map<&'static str, &'static str> = phf_map! {{
{index_entries}
}};

pub(crate) static VARIANTS: phf::Map<&'static str, &'static [&'static str]> = phf_map! {{
{variants_entries}
}};
"""


def main() -> None:
    tables = []
    for module_name, var_name in TABLE_MODULES:
        table = load_table(module_name, var_name)
        tables.append((module_name, table))
        print(f"  loaded {module_name}: {len(table)} entries", file=sys.stderr)

    index = build_flat_index(tables)
    variants_map = build_variants_map(tables)
    print(f"  flat index: {len(index)} entries, variants: {len(variants_map)} keys", file=sys.stderr)

    missing = set(index.values()) - set(variants_map.keys())
    if missing:
        print(f"  WARNING: {len(missing)} canonical keys in INDEX have no VARIANTS entry: {sorted(missing)[:5]}...", file=sys.stderr)

    content = generate(index, variants_map)
    OUTPUT_PATH.write_text(content, encoding="utf-8")
    print(f"  wrote {OUTPUT_PATH}", file=sys.stderr)


if __name__ == "__main__":
    main()
