#!/usr/bin/env python3
"""
Convert all 18 name_variants data files from list format to rich NameEntry dict format.

Reads frequency data from name_variants/frequencies.py and dialect tags from
name_variants/chinese_surnames.CHINESE_ROMANIZATION_DIALECTS, then inlines them
into each table entry.

Run from repo root:
    python scripts/migrate_to_rich_format.py
"""
from __future__ import annotations
import importlib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from name_variants.frequencies import ALL_FREQUENCIES  # noqa: E402
from name_variants.chinese_surnames import CHINESE_ROMANIZATION_DIALECTS  # noqa: E402

NV = Path(__file__).parent.parent / "name_variants"

# (module_name, variable_name) for all 18 tables
TABLES = [
    ("arabic_names",           "ARABIC_NAME_VARIANTS"),
    ("chinese_given_names",    "CHINESE_GIVEN_NAME_VARIANTS"),
    ("chinese_surnames",       "CHINESE_SURNAME_VARIANTS"),
    ("greek_names",            "GREEK_NAME_VARIANTS"),
    ("hebrew_names",           "HEBREW_NAME_VARIANTS"),
    ("indian_names_bengali",   "INDIAN_NAMES_BENGALI"),
    ("indian_names_hindi",     "INDIAN_NAMES_HINDI"),
    ("indian_names_tamil",     "INDIAN_NAMES_TAMIL"),
    ("indonesian_malay_names", "INDONESIAN_MALAY_NAME_VARIANTS"),
    ("japanese_given_names",   "JAPANESE_GIVEN_NAME_VARIANTS"),
    ("japanese_surnames",      "JAPANESE_SURNAME_VARIANTS"),
    ("korean_given_names",     "KOREAN_GIVEN_NAME_VARIANTS"),
    ("korean_surnames",        "KOREAN_SURNAME_VARIANTS"),
    ("persian_names",          "PERSIAN_NAME_VARIANTS"),
    ("russian_surnames",       "RUSSIAN_SURNAME_VARIANTS"),
    ("thai_names",             "THAI_NAME_VARIANTS"),
    ("turkish_names",          "TURKISH_NAME_VARIANTS"),
    ("vietnamese_surnames",    "VIETNAMESE_SURNAME_VARIANTS"),
]


def format_forms(forms: list[str]) -> str:
    return "[" + ", ".join(repr(f) for f in forms) + "]"


def format_entry(key: str, forms: list[str], frequency: int | None,
                 dialects: dict[str, str]) -> str:
    lines = [f"    {key!r}: {{"]
    lines.append(f'        "forms": {format_forms(forms)},')
    if frequency is not None:
        lines.append(f'        "frequency": {frequency:_},')
    if dialects:
        lines.append('        "dialects": {')
        for form, dialect in sorted(dialects.items()):
            lines.append(f"            {form!r}: {dialect!r},")
        lines.append("        },")
    lines.append("    },")
    return "\n".join(lines)


def migrate(module_name: str, var_name: str) -> None:
    mod = importlib.import_module(f"name_variants.{module_name}")
    table: dict = getattr(mod, var_name)

    filepath = NV / f"{module_name}.py"
    src = filepath.read_text(encoding="utf-8")

    # Build new entries
    entry_lines: list[str] = []
    for key, value in table.items():
        # Handle already-migrated entries (idempotent)
        if isinstance(value, dict):
            forms = value.get("forms", [])
            existing_freq = value.get("frequency")
            existing_dialects = value.get("dialects", {})
        else:
            forms = list(value)
            existing_freq = None
            existing_dialects = {}

        frequency = existing_freq or ALL_FREQUENCIES.get(key)

        # Dialect tags: use existing inline tags, fall back to CHINESE_ROMANIZATION_DIALECTS
        if module_name == "chinese_surnames":
            dialects = dict(existing_dialects)
            for form in forms:
                fl = form.lower()
                if fl not in dialects and fl in CHINESE_ROMANIZATION_DIALECTS:
                    dialects[fl] = CHINESE_ROMANIZATION_DIALECTS[fl]
        else:
            dialects = dict(existing_dialects)

        entry_lines.append(format_entry(key, forms, frequency, dialects))

    new_entries_str = "\n".join(entry_lines)

    # Locate and replace the dict body in the source file.
    # The pattern finds VAR_NAME = {\n...body...\n}
    # We allow for optional type annotation between the var name and the = {
    pattern = (
        rf"({re.escape(var_name)}"
        rf"(?:[^=\n]*?)= \{{\n)"
        rf"(.*?)"
        rf"(\n\}}\s*\n)"
    )
    match = re.search(pattern, src, re.DOTALL)
    if not match:
        print(f"  WARNING: could not locate {var_name} dict in {filepath.name}")
        return

    new_src = src[: match.start(2)] + new_entries_str + src[match.end(2):]

    # Update the type annotation to dict[str, dict]
    new_src = re.sub(
        rf"({re.escape(var_name)}): dict\[str, list\[str\]\]",
        r"\1: dict[str, dict]",
        new_src,
    )

    filepath.write_text(new_src, encoding="utf-8")
    print(f"  Migrated {filepath.name}")


if __name__ == "__main__":
    print("Migrating data files to rich NameEntry format...")
    for module_name, var_name in TABLES:
        migrate(module_name, var_name)
    print("Done. Run: python -m pytest tests/test_data_format.py -v")
