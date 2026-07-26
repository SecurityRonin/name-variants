# name-variants — PyPI Publication Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Publish `name-variants` to PyPI as a versioned, installable Python package with zero runtime dependencies.

**Architecture:** Pure data package — Python dicts only. hatchling build backend. GitHub Actions CI for automated PyPI publish on tag push.

**Tech Stack:** hatchling, twine/trusted publisher (OIDC), GitHub Actions, pytest, ruff

---

## Task 1: Package Metadata and README

**Files:**
- Modify: `pyproject.toml`
- Create: `README.md`
- Create: `LICENSE`

**Step 1: Finalise `pyproject.toml`**

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "name-variants"
version = "0.1.0"
description = "Multilingual name romanization lookup tables: Chinese, Japanese, Korean, Arabic, Vietnamese, Indian, Persian, Hebrew, Thai, Greek, Turkish, Russian, Indonesian/Malay"
readme = "README.md"
license = { text = "MIT" }
requires-python = ">=3.11"
authors = [{ name = "SecurityRonin" }]
keywords = [
    "names", "romanization", "transliteration", "cjk", "arabic",
    "multilingual", "nlp", "ner", "pseudonymization",
]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Topic :: Text Processing :: Linguistic",
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
]
dependencies = []

[project.optional-dependencies]
normalize = [
    "opencc-python-reimplemented>=0.1",
    "jaconv>=0.3",
]
dev = [
    "pytest>=8.0",
    "ruff>=0.9",
    "build>=1.0",
    "twine>=5.0",
]

[project.urls]
Homepage = "https://github.com/SecurityRonin/name-variants"
Repository = "https://github.com/SecurityRonin/name-variants"
Issues = "https://github.com/SecurityRonin/name-variants/issues"

[tool.hatch.build.targets.wheel]
packages = ["name_variants"]

[tool.hatch.build.targets.sdist]
include = ["name_variants/", "tests/", "README.md", "LICENSE"]

[tool.ruff]
target-version = "py311"
line-length = 100

[tool.ruff.lint]
select = ["E", "F", "W", "I", "UP"]

[tool.pytest.ini_options]
testpaths = ["tests"]
```

**Step 2: Write `README.md`**

```markdown
# name-variants

Multilingual name romanization lookup tables for NLP, entity resolution, and document processing.

Maps native script forms to all known romanization variants so that `陳 / Chen / Chan / Tan`,
`박 / Park / Bak`, `Nguyễn / Nguyen`, and `محمد / Muhammad / Mohammed` are treated as the same entity.

## Languages

| Script | Coverage | Example |
|--------|----------|---------|
| Chinese (Han) | 200+ surnames | `陈 → Chen / Chan / Tan / Chin` |
| Arabic | 100+ given names | `محمد → Muhammad / Mohammed / Mohamed` |
| Japanese | 150+ surnames | `田中 → Tanaka` |
| Korean | 100+ surnames | `박 → Park / Bak / Pak` |
| Vietnamese | 80+ surnames + given | `Nguyễn → Nguyen` |
| Hindi/North Indian | 80+ names | `शर्मा → Sharma / Sarma` |
| Tamil | 60+ names | `சுப்பிரமணியம் → Subramaniam / Subramanian` |
| Bengali | 60+ names | `চট্টোপাধ্যায় → Chattopadhyay / Chatterjee` |
| Persian/Farsi | 80+ names | `حسین → Hossein / Hussein` |
| Hebrew | 80+ names | `יצחק → Yitzhak / Isaac` |
| Thai | 80+ names | `ประยุทธ์ → Prayuth / Prayut` |
| Greek | 70+ names | `Κωνσταντίνος → Konstantinos / Constantine` |
| Turkish | 70+ names | `Çelik → Celik` |
| Russian/Slavic | 80+ names | `Иванов → Ivanov / Ivanoff` |
| Indonesian/Malay | 60+ names | `Suharto → Soeharto` |

## Usage

```python
from name_variants import lookup_key

lookup_key("Chan")      # → "陈"
lookup_key("陳")        # → "陈"
lookup_key("Tan")       # → "陈"
lookup_key("Xu")        # → "许"
lookup_key("Hui")       # → "许"  (Cantonese romanization of 許)
lookup_key("Park")      # → "박"
lookup_key("Bak")       # → "박"
lookup_key("Nguyen")    # → "nguyễn"
lookup_key("Muhammad")  # → "محمد"
lookup_key("Mohammed")  # → "محمد"
lookup_key("Unknown")   # → None  (not in any table)
```

### Checking if two names are variants of each other

```python
def same_person(a: str, b: str) -> bool:
    ka, kb = lookup_key(a), lookup_key(b)
    if ka is not None and kb is not None:
        return ka == kb
    # Fall back to fuzzy matching for unknown names
    from rapidfuzz import fuzz
    return fuzz.ratio(a.lower(), b.lower()) >= 85
```

## Design

- **Script form is always the canonical key** — `陈`, `박`, `محمد`, not romanizations
- **Zero runtime dependencies** — pure Python dicts
- **Lowercase romanizations** — callers casefold before lookup
- **`None` for unknowns** — explicit signal to fall back to fuzzy matching

## Install

```bash
pip install name-variants
```

Optional: CJK normalization helpers (opencc + jaconv):
```bash
pip install "name-variants[normalize]"
```
```

**Step 3: Write `LICENSE`**

Standard MIT license text. Replace `[year]` with `2026` and `[author]` with `SecurityRonin`.

**Step 4: Verify package builds**

```bash
pip install build
python -m build
ls dist/
```
Expected: `name_variants-0.1.0-py3-none-any.whl` and `name_variants-0.1.0.tar.gz`

**Step 5: Verify wheel contents**

```bash
python -m zipfile -l dist/name_variants-0.1.0-py3-none-any.whl | grep name_variants
```
Expected: all 16 `name_variants/*.py` files listed

**Step 6: Commit**

```bash
git add README.md LICENSE pyproject.toml
git commit -m "docs: README, LICENSE, finalise pyproject.toml for PyPI"
```

---

## Task 2: Test Suite Completeness

**Files:**
- Modify: `tests/test_lookup.py`
- Create: `tests/test_tables.py`

**Step 1: Write failing tests for table completeness**

```python
# tests/test_tables.py
import pytest
from name_variants import ALL_TABLES


def test_minimum_entry_counts():
    """Each table must have a meaningful number of entries."""
    minimums = {
        "chinese": 100,
        "arabic": 50,
        "japanese": 100,
        "korean": 50,
        "vietnamese": 40,
        "indian_hindi": 40,
        "indian_tamil": 30,
        "indian_bengali": 30,
        "persian": 40,
        "hebrew": 40,
        "thai": 40,
        "greek": 40,
        "turkish": 40,
        "russian": 40,
        "indonesian_malay": 30,
    }
    for table_name, minimum in minimums.items():
        count = len(ALL_TABLES[table_name])
        assert count >= minimum, (
            f"{table_name}: only {count} entries, expected >= {minimum}"
        )


def test_no_empty_variant_lists():
    for table_name, table in ALL_TABLES.items():
        for canonical, variants in table.items():
            assert variants, f"{table_name}: {canonical!r} has empty variant list"


def test_no_duplicate_variants_within_entry():
    for table_name, table in ALL_TABLES.items():
        for canonical, variants in table.items():
            assert len(variants) == len(set(variants)), (
                f"{table_name}: {canonical!r} has duplicate variants: {variants}"
            )


def test_known_romanization_collisions_are_documented():
    """
    Some romanizations genuinely map to multiple surnames (e.g. 'ng' for both
    黄 and 吴). These are acceptable — assert they exist so we know the table
    is realistic, not sanitized.
    """
    from name_variants.chinese_surnames import CHINESE_SURNAME_VARIANTS
    # 'ng' should appear under at least two entries
    ng_entries = [char for char, variants in CHINESE_SURNAME_VARIANTS.items()
                  if "ng" in variants]
    assert len(ng_entries) >= 2, "'ng' should be ambiguous across Chinese surnames"
```

**Step 2: Run tests to verify they fail or pass**

```bash
pytest tests/ -v
```

**Step 3: Fix any failures (expand tables if minimum counts not met)**

**Step 4: Commit**

```bash
git add tests/
git commit -m "test: completeness assertions for all 15 language tables"
```

---

## Task 3: GitHub Repository Setup

**Step 1: Create repo on GitHub**

```bash
gh repo create SecurityRonin/name-variants \
  --public \
  --description "Multilingual name romanization lookup tables: Chinese, Japanese, Korean, Arabic, Vietnamese, Indian, Persian, Hebrew, Thai, Greek, Turkish, Russian, Indonesian/Malay" \
  --homepage "https://pypi.org/project/name-variants/"
```

**Step 2: Push**

```bash
git remote add origin https://github.com/SecurityRonin/name-variants.git
git push -u origin main
```

**Step 3: Add topics on GitHub**

```bash
gh repo edit SecurityRonin/name-variants \
  --add-topic nlp \
  --add-topic names \
  --add-topic romanization \
  --add-topic transliteration \
  --add-topic cjk \
  --add-topic arabic \
  --add-topic multilingual
```

---

## Task 4: PyPI Trusted Publisher Setup (OIDC — no API keys)

Trusted Publisher is the modern PyPI publish method: no tokens stored in GitHub secrets.

**Step 1: Create PyPI account / project**

1. Go to https://pypi.org and log in as `SecurityRonin`
2. Go to https://pypi.org/manage/account/publishing/
3. Add a new pending publisher:
   - **PyPI project name:** `name-variants`
   - **Owner:** `SecurityRonin`
   - **Repository:** `name-variants`
   - **Workflow:** `publish.yml`
   - **Environment:** `pypi`

**Step 2: Create GitHub Actions workflow**

```yaml
# .github/workflows/publish.yml
name: Publish to PyPI

on:
  push:
    tags:
      - "v*"

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install build
      - run: python -m build
      - uses: actions/upload-artifact@v4
        with:
          name: dist
          path: dist/

  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.11", "3.12", "3.13"]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - run: pip install -e ".[dev]"
      - run: pytest tests/ -v

  publish:
    needs: [build, test]
    runs-on: ubuntu-latest
    environment: pypi
    permissions:
      id-token: write   # required for OIDC trusted publisher
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: dist
          path: dist/
      - uses: pypa/gh-action-pypi-publish@release/v1
```

**Step 3: Create GitHub Actions CI workflow (runs on every PR)**

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.11", "3.12", "3.13"]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - run: pip install -e ".[dev]"
      - run: ruff check name_variants/ tests/
      - run: pytest tests/ -v
```

**Step 4: Commit and push workflows**

```bash
mkdir -p .github/workflows
git add .github/workflows/
git commit -m "ci: GitHub Actions for CI and PyPI trusted publisher publish"
git push origin main
```

---

## Task 5: First Release — v0.1.0

**Step 1: Final check — build and inspect locally**

```bash
python -m build
python -m twine check dist/*
```
Expected: `PASSED` for both wheel and sdist

**Step 2: Test install from wheel locally**

```bash
pip install dist/name_variants-0.1.0-py3-none-any.whl
python -c "from name_variants import lookup_key; print(lookup_key('Chan'))"
```
Expected: `陈`

**Step 3: Tag and push**

```bash
git tag v0.1.0
git push origin v0.1.0
```

**Step 4: Watch the publish workflow**

```bash
gh run watch --repo SecurityRonin/name-variants
```
Expected: build → test (3 Python versions) → publish, all green

**Step 5: Verify on PyPI**

```bash
pip install name-variants
python -c "from name_variants import lookup_key; print(lookup_key('Park'))"
```
Expected: `박`

---

## Task 6: Post-Publish — Dependents

After PyPI publish, update consumers to use the published version:

**veil** (`~/src/veil/pyproject.toml`):
```toml
"name-variants>=0.1.0",
```
Remove `[tool.uv.sources]` dev override once published.

**Future releases:**
- `v0.2.0` — expand all tables to 500 entries each
- `v0.3.0` — add `normalize` helpers (opencc + jaconv integration) as built-in
- `v1.0.0` — stable API, full 500-entry coverage, comprehensive test suite
