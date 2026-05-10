# Rich Entry Format Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Convert all 18 name-variants data files from `{key: [forms]}` to a uniform
`NameEntry` TypedDict `{key: {"forms": [...], "frequency"?: int, "dialects"?: {...}}}`,
eliminating `frequencies.py` and `CHINESE_ROMANIZATION_DIALECTS` as separate concerns.

**Architecture:** Migration script converts all 18 data files programmatically. `_build_clusters()`
is updated to read `entry["forms"]`. `lookup_dialect()` builds its index from inline `"dialects"`
keys. Old separate dicts are deleted. All existing tests must pass throughout.

**Tech Stack:** Python 3.11 TypedDict, pytest, existing name-variants codebase

---

### Task 1: Commit design doc

**Files:**
- Already written: `docs/plans/2026-05-10-rich-entry-format-design.md`
- Already written: `docs/plans/2026-05-10-rich-entry-format.md`

**Step 1: Commit**

```bash
git add docs/plans/2026-05-10-rich-entry-format-design.md \
        docs/plans/2026-05-10-rich-entry-format.md
git commit -m "docs: rich NameEntry format design + implementation plan"
```

---

### Task 2 (RED): Format validation tests

**Files:**
- Create: `tests/test_data_format.py`

**Step 1: Write the failing tests**

```python
"""Validate that all 18 data files use the rich NameEntry format."""
import importlib
import pytest
from name_variants import ALL_TABLES


def test_all_entries_are_dicts():
    for table_name, table in ALL_TABLES.items():
        for key, entry in table.items():
            assert isinstance(entry, dict), (
                f"{table_name}[{key!r}]: expected dict, got {type(entry).__name__}"
            )


def test_all_entries_have_forms_list():
    for table_name, table in ALL_TABLES.items():
        for key, entry in table.items():
            assert "forms" in entry, f"{table_name}[{key!r}]: missing 'forms' key"
            assert isinstance(entry["forms"], list), (
                f"{table_name}[{key!r}]: 'forms' must be a list"
            )
            assert entry["forms"], f"{table_name}[{key!r}]: 'forms' must be non-empty"


def test_no_unknown_keys():
    valid = {"forms", "frequency", "dialects"}
    for table_name, table in ALL_TABLES.items():
        for key, entry in table.items():
            extra = set(entry.keys()) - valid
            assert not extra, f"{table_name}[{key!r}]: unknown keys {extra}"


def test_frequency_is_positive_int_when_present():
    for table_name, table in ALL_TABLES.items():
        for key, entry in table.items():
            if "frequency" in entry:
                assert isinstance(entry["frequency"], int) and entry["frequency"] > 0, (
                    f"{table_name}[{key!r}]: frequency must be a positive int"
                )


def test_dialects_is_str_str_dict_when_present():
    valid_dialects = {
        "mandarin_pinyin", "cantonese", "hokkien", "hakka",
        "teochew", "wade_giles", "traditional", "simplified", "postal",
    }
    for table_name, table in ALL_TABLES.items():
        for key, entry in table.items():
            if "dialects" in entry:
                d = entry["dialects"]
                assert isinstance(d, dict), (
                    f"{table_name}[{key!r}]: dialects must be a dict"
                )
                for form, dialect in d.items():
                    assert isinstance(form, str) and isinstance(dialect, str), (
                        f"{table_name}[{key!r}]: dialects values must be str->str"
                    )
                    assert dialect in valid_dialects, (
                        f"{table_name}[{key!r}]: unknown dialect {dialect!r}"
                    )


def test_frequencies_module_deleted():
    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("name_variants.frequencies")


def test_chinese_romanization_dialects_removed():
    from name_variants import chinese_surnames
    assert not hasattr(chinese_surnames, "CHINESE_ROMANIZATION_DIALECTS"), (
        "CHINESE_ROMANIZATION_DIALECTS should be removed from chinese_surnames.py"
    )


def test_lookup_dialect_works_without_separate_dict():
    from name_variants import lookup_dialect
    assert lookup_dialect("chen") == "mandarin_pinyin"
    assert lookup_dialect("chou") == "wade_giles"
    assert lookup_dialect("chan") == "cantonese"
    assert lookup_dialect("Smith") is None
```

**Step 2: Run to confirm RED**

```bash
python -m pytest tests/test_data_format.py -v --tb=short 2>&1 | tail -20
```

Expected: all 9 tests fail — entries are lists, not dicts; `frequencies` module exists; etc.

**Step 3: Commit RED**

```bash
git add tests/test_data_format.py
git commit -m "test: RED — rich NameEntry format validation"
```

---

### Task 3 (GREEN): Add NameEntry TypedDict + update `_build_clusters()` transitionally

Update `__init__.py` so it supports **both** the old list format and the new dict format.
This lets us migrate data files incrementally without breaking existing tests.

**Files:**
- Modify: `name_variants/__init__.py`

**Step 1: Add TypedDict import and NameEntry type**

Add near the top of `__init__.py`, after `from dataclasses import dataclass`:

```python
from typing import NotRequired, TypedDict


class NameEntry(TypedDict):
    forms: list[str]
    frequency: NotRequired[int]
    dialects: NotRequired[dict[str, str]]
```

**Step 2: Update `_build_clusters()` to handle both formats**

Replace the existing `_build_clusters()` with:

```python
def _build_clusters() -> tuple[list["NameCluster"], dict[str, list["NameCluster"]]]:
    clusters: list[NameCluster] = []
    form_index: dict[str, list[NameCluster]] = {}

    for language, table in ALL_TABLES.items():
        for storage_key, entry in table.items():
            # Support both old list format and new rich dict format
            if isinstance(entry, dict):
                forms_list: list[str] = entry["forms"]
                frequency: int | None = entry.get("frequency")
            else:
                forms_list = entry  # type: ignore[assignment]
                frequency = None

            forms = frozenset(
                {storage_key}
                | {v.lower().strip() for v in forms_list if v.strip()}
            )
            cluster = NameCluster(forms=forms, language=language, frequency=frequency)
            clusters.append(cluster)
            for form in forms:
                form_index.setdefault(form, []).append(cluster)

    return clusters, form_index
```

**Step 3: Update `lookup_dialect()` to build from ALL_TABLES**

Replace the existing `lookup_dialect()`:

```python
_DIALECT_INDEX: dict[str, str] | None = None


def _build_dialect_index() -> dict[str, str]:
    index: dict[str, str] = {}
    for table in ALL_TABLES.values():
        for entry in table.values():
            if isinstance(entry, dict):
                for form, dialect in entry.get("dialects", {}).items():
                    index[form.lower()] = dialect
    # Fall back to legacy CHINESE_ROMANIZATION_DIALECTS if present (removed in Task 6)
    try:
        from name_variants.chinese_surnames import CHINESE_ROMANIZATION_DIALECTS
        for form, dialect in CHINESE_ROMANIZATION_DIALECTS.items():
            if form not in index:
                index[form] = dialect
    except ImportError:
        pass
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
```

Also remove the old `_FORM_INDEX` reset — add `_DIALECT_INDEX = None` to the global
resets if any, and keep `_CLUSTERS` and `_FORM_INDEX` resets.

**Step 4: Run existing suite — must stay green**

```bash
python -m pytest tests/ -q --tb=short --ignore=tests/test_data_format.py 2>&1 | tail -5
```

Expected: all pass (old format still works).

**Step 5: Commit**

```bash
git add name_variants/__init__.py
git commit -m "refactor: _build_clusters + lookup_dialect support rich NameEntry (transitional)"
```

---

### Task 4 (GREEN): Write and run the data migration script

**Files:**
- Create: `scripts/migrate_to_rich_format.py`

**Step 1: Create the migration script**

```python
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
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from name_variants.frequencies import ALL_FREQUENCIES  # noqa: E402
from name_variants.chinese_surnames import CHINESE_ROMANIZATION_DIALECTS  # noqa: E402

NV = Path(__file__).parent.parent / "name_variants"

# (module_name, variable_name) for all 18 tables
TABLES = [
    ("arabic_names",          "ARABIC_NAME_VARIANTS"),
    ("chinese_given_names",   "CHINESE_GIVEN_NAME_VARIANTS"),
    ("chinese_surnames",      "CHINESE_SURNAME_VARIANTS"),
    ("greek_names",           "GREEK_NAME_VARIANTS"),
    ("hebrew_names",          "HEBREW_NAME_VARIANTS"),
    ("indian_names_bengali",  "INDIAN_NAMES_BENGALI"),
    ("indian_names_hindi",    "INDIAN_NAMES_HINDI"),
    ("indian_names_tamil",    "INDIAN_NAMES_TAMIL"),
    ("indonesian_malay_names","INDONESIAN_MALAY_NAME_VARIANTS"),
    ("japanese_given_names",  "JAPANESE_GIVEN_NAME_VARIANTS"),
    ("japanese_surnames",     "JAPANESE_SURNAME_VARIANTS"),
    ("korean_given_names",    "KOREAN_GIVEN_NAME_VARIANTS"),
    ("korean_surnames",       "KOREAN_SURNAME_VARIANTS"),
    ("persian_names",         "PERSIAN_NAME_VARIANTS"),
    ("russian_surnames",      "RUSSIAN_SURNAME_VARIANTS"),
    ("thai_names",            "THAI_NAME_VARIANTS"),
    ("turkish_names",         "TURKISH_NAME_VARIANTS"),
    ("vietnamese_surnames",   "VIETNAMESE_SURNAME_VARIANTS"),
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
    # The variable starts with "VAR_NAME: dict[..." and the dict ends with "}\n"
    import re
    pattern = (
        rf"({re.escape(var_name)}"
        rf"(?:: dict\[[^\]]*\](?:\[[^\]]*\])*)? = \{{\n)"
        rf"(.*?)"
        rf"(\n\}}\s*\n)"
    )
    match = re.search(pattern, src, re.DOTALL)
    if not match:
        print(f"  WARNING: could not locate {var_name} dict in {filepath.name}")
        return

    new_src = src[: match.start(2)] + new_entries_str + src[match.end(2) :]

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
```

**Step 2: Create the scripts/ directory and save the file**

```bash
mkdir -p scripts
# write the file as above
```

**Step 3: Run the migration**

```bash
python scripts/migrate_to_rich_format.py
```

Expected output: 18 lines of "Migrated <filename>.py"

**Step 4: Verify format tests pass**

```bash
python -m pytest tests/test_data_format.py -v --tb=short 2>&1 | tail -20
```

Expected: most pass. The two tests for `frequencies` deletion and
`CHINESE_ROMANIZATION_DIALECTS` removal will still fail — that happens in Task 6.

**Step 5: Verify existing suite still passes**

```bash
python -m pytest tests/ -q --tb=short \
  --ignore=tests/test_data_format.py 2>&1 | tail -5
```

Expected: all pass.

**Step 6: Commit**

```bash
git add scripts/migrate_to_rich_format.py name_variants/
git commit -m "feat(data): migrate all 18 tables to rich NameEntry format"
```

---

### Task 5: Remove transitional isinstance branch + tighten `_build_clusters()`

Now that all data files use the dict format, remove the old-format fallback.

**Files:**
- Modify: `name_variants/__init__.py`

**Step 1: Remove the `isinstance` branch from `_build_clusters()`**

Replace:
```python
if isinstance(entry, dict):
    forms_list: list[str] = entry["forms"]
    frequency: int | None = entry.get("frequency")
else:
    forms_list = entry  # type: ignore[assignment]
    frequency = None
```

With:
```python
forms_list: list[str] = entry["forms"]
frequency: int | None = entry.get("frequency")
```

**Step 2: Remove the fall-back import from `_build_dialect_index()`**

Remove the entire `try/except ImportError` block that imports
`CHINESE_ROMANIZATION_DIALECTS`. The function should only read from `ALL_TABLES`.

**Step 3: Run full suite**

```bash
python -m pytest tests/ -q --tb=short --ignore=tests/test_data_format.py 2>&1 | tail -5
```

Expected: all pass.

**Step 4: Commit**

```bash
git add name_variants/__init__.py
git commit -m "refactor: remove transitional list-format support from _build_clusters"
```

---

### Task 6: Delete `frequencies.py` and remove `CHINESE_ROMANIZATION_DIALECTS`

**Files:**
- Delete: `name_variants/frequencies.py`
- Modify: `name_variants/chinese_surnames.py` — remove `CHINESE_ROMANIZATION_DIALECTS`

**Step 1: Delete frequencies.py**

```bash
git rm name_variants/frequencies.py
```

**Step 2: Remove `CHINESE_ROMANIZATION_DIALECTS` from `chinese_surnames.py`**

Open `name_variants/chinese_surnames.py`. Find and delete the entire
`CHINESE_ROMANIZATION_DIALECTS: dict[str, str] = { ... }` block (it's a standalone
dict definition after `CHINESE_SURNAME_VARIANTS`).

**Step 3: Run format validation — should now be fully green**

```bash
python -m pytest tests/test_data_format.py -v --tb=short 2>&1 | tail -15
```

Expected: all 9 pass.

**Step 4: Run full suite**

```bash
python -m pytest tests/ -q --tb=short 2>&1 | tail -5
```

Expected: all pass. If `test_dialect.py` or any test imports `frequencies` or
`CHINESE_ROMANIZATION_DIALECTS` directly, fix those imports now.

**Step 5: Commit**

```bash
git add name_variants/chinese_surnames.py
git commit -m "refactor: delete frequencies.py + CHINESE_ROMANIZATION_DIALECTS — data now inline"
```

---

### Task 7: Update Rust codegen

**Files:**
- Modify: `codegen/gen_rust.py`
- Modify: `name-variants-rs/src/generated.rs` (regenerated)

**Step 1: Read `codegen/gen_rust.py`**

Find every place that reads table values as a list (e.g. `for variant in variants:` or
`variants_list = table[key]`). Update to read `entry["forms"]` instead.

The key pattern to change (find the exact lines by reading the file):

```python
# Before (somewhere in gen_rust.py)
for canonical, variants in table.items():
    # uses variants as a list

# After
for canonical, entry in table.items():
    variants = entry["forms"]
    # rest unchanged
```

Also update the LANGUAGE map generation if it uses the old format.

**Step 2: Regenerate**

```bash
python codegen/gen_rust.py
```

**Step 3: Run Rust tests**

```bash
cargo test --manifest-path name-variants-rs/Cargo.toml 2>&1 | tail -10
```

Expected: all pass.

**Step 4: Run full Python suite**

```bash
python -m pytest tests/ -q --tb=no 2>&1 | tail -5
```

**Step 5: Commit**

```bash
git add codegen/gen_rust.py name-variants-rs/src/generated.rs
git commit -m "chore(codegen): update gen_rust.py for rich NameEntry format + regenerate"
```

---

### Task 8: Rebuild PyO3 native extension

The `.so` baked into the repo was built against the old `generated.rs`. Rebuild it.

**Step 1: Build**

```bash
maturin build --manifest-path name-variants-py/Cargo.toml \
  --interpreter python3.11 2>&1 | tail -5
pip install target/wheels/*.whl --force-reinstall --quiet
```

**Step 2: Run native tests**

```bash
python -m pytest tests/test_native.py -v --tb=short 2>&1 | tail -15
```

Expected: all pass.

**Step 3: Copy .so into source tree** (the existing repo has it checked in)

```bash
cp target/wheels/*/name_variants/_native*.so name_variants/
```

**Step 4: Commit**

```bash
git add name_variants/_native*.so
git commit -m "chore(pyo3): rebuild native extension against regenerated generated.rs"
```

---

### Task 9: Final sweep — full suite + push

**Step 1: Run the complete test suite**

```bash
python -m pytest tests/ -v --tb=short 2>&1 | tail -20
```

Expected: 0 failures, 0 errors.

**Step 2: Push**

```bash
git push origin main
```

---

**Plan complete and saved to `docs/plans/2026-05-10-rich-entry-format.md`.**

Two execution options:

**1. Subagent-Driven (this session)** — I dispatch a fresh subagent per task, review between tasks

**2. Parallel Session (separate)** — Open new session with executing-plans, batch execution with checkpoints

Which approach?
