#!/usr/bin/env python3
"""Migrate chinese_surnames.py keys from Simplified to Traditional.

For each entry that has a form tagged "traditional" in its dialects:
  - New dict key = Traditional form
  - Remove Traditional form from forms list
  - Add old Simplified key to forms list (if not already present)
  - In dialects: remove <trad>: "traditional", add <simp>: "simplified"

Entries with no "traditional" dialect tag are left unchanged.
"""
import copy
import sys
from pathlib import Path

# Ensure project root is on path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from name_variants.chinese_surnames import CHINESE_SURNAME_VARIANTS  # noqa: E402


def build_migrated() -> dict:
    new_variants: dict = {}
    for key, entry in CHINESE_SURNAME_VARIANTS.items():
        e = copy.deepcopy(entry)
        dialects = e.get("dialects", {})
        trad_forms = [f for f, d in dialects.items() if d == "traditional"]
        if trad_forms:
            trad = trad_forms[0]
            new_key = trad
            if trad in e["forms"]:
                e["forms"].remove(trad)
            if key not in e["forms"]:
                e["forms"].append(key)
            del dialects[trad]
            dialects[key] = "simplified"
        else:
            new_key = key
        new_variants[new_key] = e
    return new_variants


def format_frequency(freq: int) -> str:
    """Format frequency with underscores matching original style."""
    s = str(freq)
    # Insert underscores every 3 digits from the right
    parts = []
    while len(s) > 3:
        parts.append(s[-3:])
        s = s[:-3]
    parts.append(s)
    return "_".join(reversed(parts))


def render_entry(key: str, entry: dict) -> list[str]:
    lines = [f"    {key!r}: {{"]
    # forms
    forms_repr = repr(entry["forms"])
    lines.append(f"        \"forms\": {forms_repr},")
    # frequency
    if "frequency" in entry:
        freq_str = format_frequency(entry["frequency"])
        lines.append(f"        \"frequency\": {freq_str},")
    # dialects
    if "dialects" in entry:
        d = entry["dialects"]
        lines.append("        \"dialects\": {")
        for form, dialect in sorted(d.items()):
            lines.append(f"            {form!r}: {dialect!r},")
        lines.append("        },")
    lines.append("    },")
    return lines


def generate_file(new_variants: dict) -> str:
    header = '''\
"""
Chinese surname lookup: Simplified Han → romanization variants.
Covers Mandarin (Pinyin), Cantonese (Jyutping/Yale), Hokkien/Teochew/Hakka, Wade-Giles.

Key: always Traditional character (where one exists). Simplified form is included
as a co-equal member of the same cluster with dialect tag "simplified".
Romanizations: all lowercase.

Sources:
  - 百家姓 census + modern CNKI surname frequency data
  - HK Immigration Department romanization standards
  - SEA Chinese (Singapore/Malaysia) naming conventions
  - Jyutping romanization for Cantonese
"""

CHINESE_SURNAME_VARIANTS: dict[str, dict] = {
'''
    body_lines: list[str] = []
    for key, entry in new_variants.items():
        body_lines.extend(render_entry(key, entry))
    footer = "}\n"
    return header + "\n".join(body_lines) + "\n" + footer


def main() -> None:
    new_variants = build_migrated()
    content = generate_file(new_variants)
    target = ROOT / "name_variants" / "chinese_surnames.py"
    target.write_text(content, encoding="utf-8")
    print(f"Wrote {target} ({len(new_variants)} entries)")

    # Quick validation
    changed = sum(
        1 for k, v in new_variants.items()
        if any(d == "simplified" for d in v.get("dialects", {}).values())
    )
    print(f"  {changed} entries migrated to Traditional keys")
    unchanged = len(new_variants) - changed
    print(f"  {unchanged} entries unchanged (identical in both scripts)")


if __name__ == "__main__":
    main()
