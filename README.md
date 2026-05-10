[![PyPI](https://img.shields.io/pypi/v/name-variants?style=flat-square)](https://pypi.org/project/name-variants/)
[![Stars](https://img.shields.io/github/stars/SecurityRonin/name-variants?style=flat-square)](https://github.com/SecurityRonin/name-variants/stargazers)
[![Tests](https://img.shields.io/github/actions/workflow/status/SecurityRonin/name-variants/ci.yml?style=flat-square&label=tests)](https://github.com/SecurityRonin/name-variants/actions)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)

# name-variants

**Multilingual name romanization equivalence classes.** `"Chan"` is simultaneously 陈 (Chinese surname) _and_ 찬 (Korean given name) _and_ whatever else it might be — `lookup()` returns all of them.

Covers 18 language tables: Chinese (surnames + given names), Korean (surnames + given names), Japanese (surnames + given names), Arabic, Vietnamese, Indian (Hindi/Tamil/Bengali), Persian, Hebrew, Thai, Greek, Turkish, Russian, Indonesian/Malay.

---

## Core concept

Every name entry is a `NameCluster` — an equivalence class where all representations are **co-equal members**:

```
陈  陳  chen  chan  tan  tan  ...   ← all in one Chinese surname cluster
찬  chan  chahn                     ← all in one Korean given-name cluster
```

`lookup("Chan")` returns **both** clusters. No privileged "canonical" form. 陈 and 陳 (Simplified vs Traditional) are equals.

---

## Installation

```bash
pip install name-variants
```

Optional extras:

```bash
pip install "name-variants[normalize]"   # opencc (Traditional↔Simplified) + jaconv
pip install "name-variants[pandas]"      # pandas Series accessor
```

---

## Usage

### lookup() — the primary API

```python
from name_variants import lookup, share_cluster, NameCluster

clusters = lookup("Chan")
# [NameCluster(language='chinese', 68 forms),
#  NameCluster(language='korean_given', 3 forms)]

for c in clusters:
    print(c.language, sorted(c.forms)[:5])
# chinese   ['chan', 'chen', 'tan', '陈', '陳', ...]
# korean_given ['chan', 'chahn', '찬']

# All forms are co-equal — both scripts present
assert "陈" in clusters[0]   # Simplified
assert "陳" in clusters[0]   # Traditional — same cluster

# Membership is case-insensitive
assert "CHAN" in clusters[0]
assert "Chan" in clusters[0]
```

### share_cluster() — equivalence check

```python
share_cluster("Chan", "Chen")        # True  — same Chinese cluster
share_cluster("Chou", "Zhou")        # True  — Wade-Giles = Pinyin
share_cluster("Chiang", "Jiang")     # True  — Chiang Kai-shek / 蒋介石
share_cluster("Hsu", "Xu")           # True  — Taiwan diaspora form
share_cluster("Chan", "Kim")         # False — different names
share_cluster("", "Chan")            # False — empty input
```

### normalize() — text preprocessing

```python
from name_variants import normalize

normalize("  NGUYỄN  ")                    # "nguyễn"
normalize("Nguyễn", strip_diacritics=True) # "nguyen"
normalize("chan​")                          # strips zero-width spaces
```

### lookup_dialect() — Chinese romanization system tag

```python
from name_variants import lookup_dialect

lookup_dialect("chan")    # "cantonese"
lookup_dialect("chen")    # "mandarin_pinyin"
lookup_dialect("chou")    # "wade_giles"
lookup_dialect("hsu")     # "wade_giles"
lookup_dialect("tsao")    # "wade_giles"
lookup_dialect("陳")      # "traditional"
```

---

## Romanization systems covered

| System | Examples |
|---|---|
| Mandarin Pinyin | Zhou, Zhang, Wang, Xu |
| Wade-Giles | Chou, Chang, Wang, Hsu, Tsao, Kuo, Hsieh |
| Cantonese (Jyutping/Yale) | Chan, Wong, Ng, Lam, Tsui |
| Hokkien/Min Nan | Tan, Ng, Lim, Goh |
| Hakka | Fong, Thong |
| Teochew | Teo, Ng |
| Traditional characters | 陳, 劉, 張, 楊, 趙 |

---

## NameCluster reference

```python
@dataclass(frozen=True)
class NameCluster:
    forms: frozenset[str]    # all representations — co-equal
    language: str            # "chinese", "korean", "vietnamese", etc.
    frequency: int | None    # approximate global bearer count

    def __contains__(self, text: str) -> bool  # case-insensitive
    def __iter__(self)                          # iterate all forms
    def __len__(self)
```

`lookup()` returns clusters sorted by `frequency` descending, so the most statistically likely interpretation comes first.

---

## CLI

```bash
pip install name-variants  # includes the nv command

nv lookup Chan
# [chinese] (~90M bearers)
#   陈  陳  chan  chen  ...
# [korean_given]
#   찬  chan  chahn

nv match Chan Chen          # true
nv match Chan Kim           # false
nv match --exit-code Chan Chen && echo same  # shell-scripting friendly

nv cluster-csv names.csv --col name --out out.csv
# adds name_cluster_id column (stable 12-char hex per cluster)

nv dedupe names.csv --col name --out out.csv
# adds cluster_id column grouping romanization variants
```

---

## Pandas accessor

```python
import pandas as pd
import name_variants  # registers .nv accessor
from name_variants import NameCluster

s = pd.Series(["Chan", "Chen", "Smith", "Park"])

s.nv.lookup()
# 0    [NameCluster(chinese, ...), NameCluster(korean_given, ...)]
# 1    [NameCluster(chinese, ...)]
# 2    []
# 3    [NameCluster(korean, ...)]

s.nv.cluster_id()
# 0    a3f2b1c4d5e6   ← same as row 1 (Chan and Chen share chinese cluster)
# 1    a3f2b1c4d5e6
# 2                   ← empty string for unknown
# 3    9b8c7d6e5f4a

a = pd.Series(["Chan", "Park"])
b = pd.Series(["Chen", "Bak"])
a.nv.share_cluster_with(b)   # [True, True]
```

---

## Language tables

| Key | Coverage |
|---|---|
| `chinese` | ~500 surnames, Pinyin + Wade-Giles + Cantonese + Hokkien + Traditional |
| `chinese_given` | ~120 common given-name characters |
| `arabic` | ~200 names, multiple transliteration systems |
| `japanese` | ~200 surnames (Hepburn + macron variants) |
| `japanese_given` | ~107 common given-name kanji |
| `korean` | ~150 surnames (Revised Romanization + McCune-Reischauer) |
| `korean_given` | ~70 common given-name syllables |
| `vietnamese` | ~50 surnames with diacritics and stripped forms |
| `indian_hindi` | ~200 names |
| `indian_tamil` | ~150 names |
| `indian_bengali` | ~150 names |
| `persian` | ~150 names |
| `hebrew` | ~150 names |
| `thai` | ~100 names |
| `greek` | ~100 names |
| `turkish` | ~80 names (with dotted-I variants) |
| `russian` | ~150 surnames (multiple transliteration systems) |
| `indonesian_malay` | ~120 names |

```python
from name_variants import ALL_TABLES
print(list(ALL_TABLES.keys()))  # all 18 table names
```

---

## Optional native extension (Rust/PyO3)

A compiled Rust extension ships pre-built wheels for Python 3.11–3.13 on Linux and macOS:

```python
from name_variants import _native
_native.lookup("Chan")
# [{"language": "chinese", "forms": ["陈", "陳", "chan", "chen", ...]},
#  {"language": "korean_given", "forms": ["찬", "chan", "chahn"]}]
```

Build from source:

```bash
pip install maturin
maturin build --manifest-path name-variants-py/Cargo.toml --interpreter python3.11
pip install target/wheels/*.whl
```

---

## Design

**Why equivalence classes instead of a canonical key?**

Early versions used a `lookup_key()` that returned one "canonical" form per romanization string. This forced a false choice: `"Chan"` had to map to either `陈` _or_ `찬`, not both. Table ordering became load-bearing, and romanizations were silently stripped from given-name tables to avoid collisions.

The `NameCluster` model eliminates this: every romanization system's output (Pinyin, Wade-Giles, Cantonese, Hokkien…) is just another form in the `frozenset`. `lookup()` returns all matching clusters. Ambiguity is surfaced, not suppressed.

---

## Contributing

```bash
git clone https://github.com/SecurityRonin/name-variants
cd name-variants
pip install -e ".[dev]"
pytest
```

Data files are in `name_variants/*_names.py` and `name_variants/*_surnames.py`. Each file is a plain Python dict — easy to read and edit. PRs adding missing variants or new romanization systems are welcome.

---

*MIT License · Built for NLP, NER, and entity deduplication pipelines.*
