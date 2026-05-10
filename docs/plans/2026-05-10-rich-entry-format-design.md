# Rich Entry Format Design

**Date:** 2026-05-10

## Problem

Adding one Chinese surname variant currently requires touching 3 separate locations:
1. `chinese_surnames.py` → `CHINESE_SURNAME_VARIANTS["徐"]` (add variant)
2. `chinese_surnames.py` → `CHINESE_ROMANIZATION_DIALECTS["hsu"]` (tag dialect)
3. `frequencies.py` → `ALL_FREQUENCIES["徐"]` (update frequency)

Coverage gaps are invisible: only 20/110 Chinese surnames have frequency data, only 30/110
have dialect tags. Both silently return `None`. There is no single source of truth.

## Solution

Enrich every table entry from `{key: [forms]}` to a uniform `NameEntry` TypedDict:

```python
class NameEntry(TypedDict):
    forms: list[str]
    frequency: NotRequired[int]
    dialects: NotRequired[dict[str, str]]
```

All 18 data files migrate at once. Frequency and dialect metadata live inline with
the forms they describe.

## Before / After

```python
# Before
"陈": ["陳", "chen", "chan", "tan", ...]

# After
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

# Entry with no known frequency or dialect tags
"苗": {
    "forms": ["miao"],
},
```

## Files Deleted

- `name_variants/frequencies.py` — gone; frequency lives inline
- `CHINESE_ROMANIZATION_DIALECTS` dict in `chinese_surnames.py` — gone; dialects live inline

## API Impact

`NameCluster.frequency` and `lookup_dialect()` are unchanged from the caller's perspective.
Internally, `_build_clusters()` reads `entry["forms"]` and `entry.get("frequency")`.
`lookup_dialect()` builds a lazy index by scanning `entry.get("dialects", {})` across all
tables instead of importing a separate dict.

## Single Source of Truth

After migration, adding "tsz" as a Hakka variant of 曹 with Wade-Giles tag is one edit:

```python
"曹": {
    "forms": [..., "tsz"],
    "frequency": 7_000_000,
    "dialects": {
        ...,
        "tsz": "hakka",
    },
},
```
