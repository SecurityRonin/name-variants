[![PyPI](https://img.shields.io/pypi/v/name-variants?style=flat-square)](https://pypi.org/project/name-variants/)
[![Tests](https://img.shields.io/github/actions/workflow/status/SecurityRonin/name-variants/ci.yml?style=flat-square&label=tests)](https://github.com/SecurityRonin/name-variants/actions)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
[![Sponsor](https://img.shields.io/badge/sponsor-h4x0r-ea4aaa?logo=github-sponsors&style=flat-square)](https://github.com/sponsors/h4x0r)

# name-variants

**`"Chan"` is simultaneously 陈 and 찬 and ชาน — `lookup()` returns all of them.**

1,558 name entries across 18 language tables. Every romanization system produces a member of an equivalence class: no canonical form, no ordering dependency, no silent data loss. `share_cluster("Hsu", "Xu")` is `True`. `lookup("Chan")` returns a Chinese surname cluster *and* a Korean given-name cluster, sorted by bearer count.

```bash
pip install name-variants
```

---

## The core idea

A `NameCluster` is a frozenset of co-equal representations. `陈`, `陳`, `chen`, `chan`, `tan`, `ong` are all members of the same Chinese surname cluster — none is more "real" than another. `lookup()` returns every cluster that contains your query, sorted by frequency:

```python
from name_variants import lookup, share_cluster

clusters = lookup("Chan")
# [NameCluster(language='chinese', 68 forms),
#  NameCluster(language='korean_given', 3 forms)]

# Both Chinese scripts are in the same cluster — co-equal
assert "陈" in clusters[0]   # Simplified
assert "陳" in clusters[0]   # Traditional

# Membership is case-insensitive
assert "CHAN" in clusters[0]

# Ambiguity is surfaced, not suppressed
assert len(clusters) == 2    # Chinese AND Korean, not one-or-the-other
```

---

## API

### lookup() — all matching clusters

```python
from name_variants import lookup

lookup("Chan")
# [NameCluster(language='chinese', 68 forms),
#  NameCluster(language='korean_given', 3 forms)]

lookup("Nguyen")
# [NameCluster(language='vietnamese', 4 forms)]

lookup("Smith")
# []
```

Results are sorted by `frequency` descending — most statistically likely interpretation first.

### share_cluster() — equivalence check

```python
from name_variants import share_cluster

share_cluster("Chan", "Chen")        # True  — same Chinese cluster
share_cluster("Chou", "Zhou")        # True  — Wade-Giles = Pinyin
share_cluster("Chiang", "Jiang")     # True  — Chiang Kai-shek / 蒋介石
share_cluster("Hsu", "Xu")           # True  — Taiwan diaspora romanization
share_cluster("Tsao", "Cao")         # True  — Ts'ao Ts'ao / 曹操
share_cluster("Chan", "Kim")         # False — different names
share_cluster("", "Chan")            # False — empty input
```

### lookup_dialect() — Chinese romanization system tag

```python
from name_variants import lookup_dialect

lookup_dialect("chen")   # "mandarin_pinyin"
lookup_dialect("chan")   # "cantonese"
lookup_dialect("tan")    # "hokkien"
lookup_dialect("chou")   # "wade_giles"
lookup_dialect("hsu")    # "wade_giles"
lookup_dialect("陳")     # "traditional"
lookup_dialect("Smith")  # None
```

### normalize() — text preprocessing

```python
from name_variants import normalize

normalize("  NGUYỄN  ")                    # "nguyễn"
normalize("Nguyễn", strip_diacritics=True) # "nguyen"
normalize("chan​")                          # strips zero-width spaces
```

---

## CLI

```bash
nv lookup Chan
# [chinese] (~90M bearers)
#   陈  陳  chan  chen  tan  ...
# [korean_given]
#   찬  chan  chahn

nv match Chan Chen          # true
nv match Chan Kim           # false
nv match --exit-code Chan Chen && echo same   # shell-scripting friendly

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

Install the extra: `pip install "name-variants[pandas]"`

---

## Language tables

| Language | Entries | Coverage |
|---|---|---|
| `chinese` | 140 | Pinyin + Wade-Giles + Cantonese + Hokkien + Hakka + Teochew + Traditional |
| `japanese` | 143 | Hepburn + macron variants |
| `korean` | 100 | Revised Romanization + McCune-Reischauer |
| `arabic` | 92 | Multiple transliteration systems |
| `vietnamese` | 84 | Diacritics + stripped forms |
| `russian` | 79 | Multiple transliteration systems |
| `indonesian_malay` | 77 | — |
| `persian` | 80 | — |
| `indian_hindi` | 80 | — |
| `hebrew` | 75 | — |
| `turkish` | 74 | Dotted-İ variants |
| `greek` | 60 | — |
| `thai` | 68 | — |
| `indian_bengali` | 56 | — |
| `indian_tamil` | 53 | — |
| `chinese_given` | 120 | Common given-name characters with Pinyin |
| `korean_given` | 70 | Common given-name syllables |
| `japanese_given` | 107 | Common given-name kanji |

```python
from name_variants import ALL_TABLES
list(ALL_TABLES.keys())   # all 18 table names
```

---

## Chinese romanization systems

| System | Examples |
|---|---|
| Mandarin Pinyin | Zhou, Zhang, Wang, Xu |
| Wade-Giles | Chou, Chang, Wang, Hsu, Tsao, Kuo, Hsieh |
| Cantonese (Jyutping/Yale) | Chan, Wong, Ng, Lam, Tsui |
| Hokkien/Min Nan | Tan, Ng, Lim, Goh |
| Hakka | Fong, Thong |
| Teochew | Teo, Ng |
| Postal romanization | Peking, Nanking, Chungking |
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

---

## Optional extras

```bash
pip install "name-variants[normalize]"   # opencc (Traditional↔Simplified) + jaconv
pip install "name-variants[pandas]"      # pandas Series .nv accessor
```

---

## Optional native extension (Rust/PyO3)

Pre-built wheels for Python 3.11–3.13 on Linux and macOS:

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

## Why equivalence classes instead of a canonical key?

Early versions returned one "canonical" form per romanization string. This forced a false choice: `"Chan"` had to map to either `陈` *or* `찬`, not both. Table ordering became load-bearing — whichever table was imported last won. Romanizations had to be stripped from given-name tables to prevent collisions.

The `NameCluster` model eliminates this: every romanization system's output is just another member of a frozenset. `lookup()` returns all matching clusters. Ambiguity is surfaced, not suppressed. The most likely interpretation comes first by frequency.

---

## Contributing

```bash
git clone https://github.com/SecurityRonin/name-variants
cd name-variants
pip install -e ".[dev]"
pytest
```

Data files are in `name_variants/*_names.py` and `name_variants/*_surnames.py`. Each entry is a plain Python dict — easy to read and edit:

```python
"陈": {
    "forms": ["陳", "chen", "chan", "tan", ...],
    "frequency": 90_000_000,
    "dialects": {
        "chen": "mandarin_pinyin",
        "chan": "cantonese",
        "tan":  "hokkien",
        "陳":   "traditional",
    },
},
```

Adding a new variant is one edit to one entry — forms, frequency, and dialect tag colocated.

---

*MIT License · Built for NLP, NER, and entity deduplication pipelines.*
