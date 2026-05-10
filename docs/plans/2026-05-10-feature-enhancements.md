# name-variants v0.2 Feature Enhancements

**Date:** 2026-05-10
**Branch:** main (direct)
**TDD discipline:** RED commit → GREEN commit per feature, no exceptions.

## Feature List

| # | Feature | Complexity | Deps |
|---|---------|-----------|------|
| 1 | `is_variant`, `canonicalize`, `normalize` | LOW | stdlib only |
| 2 | CLI: `nv canonicalize-csv`, `nv dedupe` | LOW | click |
| 3 | Pandas `.nv` accessor | LOW | pandas (optional extra) |
| 4 | PyO3 native binding | MEDIUM | pyo3, maturin |
| 5 | Frequency annotations + `language_distribution()` | MEDIUM | data sourcing |
| 6 | Dialect tags for Chinese romanizations | MEDIUM | data |
| 7 | CJK given-name tables | HIGH | data sourcing |
| 8 | WASM build | MEDIUM | wasm-pack |

---

## Batch 1 — Features 1, 2, 3 (Pure Python)

### Task 1.1 — RED tests for `normalize`, `is_variant`, `canonicalize`

Create `tests/test_utils.py` with failing tests:

```python
from name_variants import normalize, is_variant, canonicalize

# normalize
def test_normalize_casefold(): assert normalize("CHAN") == "chan"
def test_normalize_whitespace(): assert normalize("  chan  ") == "chan"
def test_normalize_zero_width(): assert normalize("chan​") == "chan"
def test_normalize_nfc(): ...  # composed vs decomposed diacritics
def test_normalize_keeps_diacritics(): assert normalize("nguyễn") == "nguyễn"
def test_normalize_strip_diacritics(): assert normalize("nguyễn", strip_diacritics=True) == "nguyen"
def test_normalize_empty(): assert normalize("") == ""

# is_variant
def test_is_variant_same(): assert is_variant("Chan", "Chen") is True
def test_is_variant_hokkien(): assert is_variant("Tan", "Chen") is True
def test_is_variant_different(): assert is_variant("Chan", "Kim") is False
def test_is_variant_both_unknown(): assert is_variant("Smith", "Smyth") is False
def test_is_variant_one_unknown(): assert is_variant("Chan", "Smith") is False
def test_is_variant_empty(): assert is_variant("", "") is False

# canonicalize
def test_canonicalize_known(): assert canonicalize("Chan") == "陈"
def test_canonicalize_unknown_passthrough(): assert canonicalize("Smith") == "Smith"
def test_canonicalize_unknown_lower(): assert canonicalize("Smith", fallback="lower") == "smith"
def test_canonicalize_case(): assert canonicalize("CHAN") == "陈"
```

Verification: `pytest tests/test_utils.py` — expect all FAIL with ImportError.

### Task 1.2 — GREEN implementation of `normalize`, `is_variant`, `canonicalize`

Add to `name_variants/__init__.py`:

```python
import unicodedata as _ud

def normalize(text: str, *, strip_diacritics: bool = False) -> str:
    """NFC + casefold + collapse whitespace + strip zero-width chars."""
    # Remove Unicode format characters (zero-width spaces, BOM, etc.)
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
    """lookup_key with fallback strategy for unknown names."""
    key = lookup_key(text)
    if key is not None:
        return key
    if fallback == "lower":
        return text.lower().strip()
    return text.strip()

def is_variant(a: str, b: str) -> bool:
    """True iff both strings resolve to the same canonical key."""
    if not a or not b:
        return False
    ka, kb = lookup_key(a), lookup_key(b)
    return ka is not None and ka == kb
```

Update `__all__` to include `normalize`, `canonicalize`, `is_variant`.

Verification: `pytest tests/test_utils.py` — expect all PASS.

---

### Task 1.3 — RED tests for CLI

Create `tests/test_cli.py`:

```python
from click.testing import CliRunner
from name_variants.cli import cli

def test_lookup_known(): result = runner.invoke(cli, ["lookup", "Chan"]); assert "陈" in result.output
def test_lookup_unknown(): assert "Smith" in result.output  # passthrough
def test_match_same(): assert "True" in runner.invoke(cli, ["match", "Chan", "Chen"]).output
def test_match_different(): assert "False" in runner.invoke(cli, ["match", "Chan", "Kim"]).output
def test_canonicalize_csv(): ...  # uses temp CSV file
def test_dedupe(): ...  # uses temp CSV file
```

### Task 1.4 — GREEN implementation of CLI

Create `name_variants/cli.py` using click.
Add `[project.scripts] nv = "name_variants.cli:cli"` to `pyproject.toml`.
Add `click>=8.0` to `[project.dependencies]`.

---

### Task 1.5 — RED tests for Pandas accessor

Create `tests/test_pandas_accessor.py`:

```python
pd = pytest.importorskip("pandas")
import name_variants.pandas_ext  # registers accessor

def test_nv_lookup(): s.nv.lookup()[0] == "陈"
def test_nv_canonical_passthrough(): s.nv.canonical()[2] == "Smith"
def test_nv_is_variant_of(): ...
def test_nv_cluster_id(): ...
```

### Task 1.6 — GREEN implementation of Pandas accessor

Create `name_variants/pandas_ext.py`.
Add `pandas` to `[project.optional-dependencies] pandas = ["pandas>=1.3"]`.

---

## Batch 2 — Feature 4 (PyO3 Native Binding)

### Task 2.1 — RED tests for native binding

Create `tests/test_native.py` (tests that require the extension to be built):

```python
import pytest
# Tests that FAIL if native extension is not built
def test_native_module_exists():
    import name_variants._native  # ImportError if not built

def test_native_lookup_key_matches_python():
    from name_variants._native import lookup_key as native_lookup
    assert native_lookup("Chan") == "陈"
```

### Task 2.2 — Rust PyO3 binding implementation

- Create `name-variants-py/` crate with PyO3 bindings
- Configure `pyproject.toml` for maturin optional build
- Add `[native]` extra: `pip install 'name-variants[native]'`

---

## Batch 3 — Features 5+6 (Frequency + Dialect)

### Task 3.1 — RED tests for `language_distribution`

```python
def test_language_distribution_returns_dict(): ...
def test_language_distribution_nguyen_is_vietnamese(): result["vietnamese"] > 0.9
def test_language_distribution_lee_is_ambiguous(): len(result) >= 2
def test_language_distribution_unknown(): result == {}
```

### Task 3.2 — GREEN: frequency data + `language_distribution()`

- Add `name_variants/frequencies.py` with top-N surname frequencies per language
- Implement `language_distribution(text)` in `__init__.py`

### Task 3.3 — RED tests for dialect tags

```python
def test_chinese_dialect_chan_is_cantonese(): ...
def test_chinese_dialect_tan_is_hokkien(): ...
def test_chinese_dialect_chen_is_mandarin(): ...
def test_lookup_dialect(): ...
```

### Task 3.4 — GREEN: dialect metadata + `lookup_dialect()`

- Add `CHINESE_ROMANIZATION_DIALECTS` dict to `chinese_surnames.py`
- Implement `lookup_dialect(text)` in `__init__.py`

---

## Batch 4 — Feature 7 (CJK Given Names)

### Task 4.1 — RED tests for CJK given names

```python
def test_chinese_given_name_ming(): assert lookup_key("Ming") is not None
def test_korean_given_name_jae(): assert lookup_key("재") is not None
def test_japanese_given_name_kenji(): assert lookup_key("Kenji") is not None
```

### Task 4.2 — GREEN: create CJK given-name tables

- `name_variants/chinese_given_names.py` (~150 entries)
- `name_variants/korean_given_names.py` (~80 entries)
- `name_variants/japanese_given_names.py` (~100 entries)
- Add to `ALL_TABLES` and regenerate `generated.rs`

---

## Batch 5 — Feature 8 (WASM Build)

### Task 5.1 — Set up wasm-pack infrastructure

- Configure `name-variants-rs` for `wasm32-unknown-unknown`
- Add `wasm-bindgen` bindings
- Add `wasm-pack build` to CI
- Create `name-variants-wasm/` JS package skeleton

### Task 5.2 — WASM tests

- Node.js smoke tests via `wasm-pack test --node`
