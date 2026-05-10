# NameCluster Design

**Date:** 2026-05-10

## Problem

The `lookup_key()` API assumed a name maps to one canonical form. That assumption is wrong.
"Chan" is simultaneously 陈 (Chinese surname) **and** 찬 (Korean given name). No member is
more "canonical" than any other — 陈 and 陳 are co-equal representations of the same identity.

The flat last-write-wins index forced a false choice, made table ordering load-bearing, and
caused the CJK given-name tables to strip genuine romanization variants just to avoid collisions.

## Solution

Replace the key→value model with **equivalence classes** (clusters):

- Every representation in a cluster is co-equal — no privileged member
- `lookup("Chan")` returns **all** clusters that contain "chan" as a member
- Ambiguity is exposed, not suppressed

## Core Abstraction

```python
@dataclass(frozen=True)
class NameCluster:
    forms: frozenset[str]    # all representations — equally valid
    language: str            # which table produced this cluster
    frequency: int | None    # population bearer count (for sorting results)

    def __contains__(self, text: str) -> bool   # "Chan" in cluster
    def __iter__(self)                           # iterate all forms
    def __len__(self)
    # No .canonical, no .key, no privileged member exposed
```

Stable cluster identity for deduplication uses `hash((forms, language))` — internal, never
exposed as a member string.

## Public API

```python
# Core
lookup(text: str) -> list[NameCluster]       # all matching clusters, sorted by frequency desc
share_cluster(a: str, b: str) -> bool         # do a and b appear in any common cluster?
normalize(text: str, *, strip_diacritics=False) -> str  # unchanged

# Standalone utilities (not on cluster)
lookup_dialect(text: str) -> str | None      # Chinese romanization dialect tag
```

## Removed

`lookup_key`, `lookup_all`, `lookup_candidates`, `canonicalize`, `is_variant`,
`get_language_for_canonical`, `get_frequency`, `language_distribution`

## Data Format

Unchanged. Existing `{storage_key: [variants]}` files are kept as-is. The storage key is a
dict key for Python purposes only — not semantically privileged. Clusters include it as one
member among equals via `frozenset({storage_key} | set(variants))`.

## Key Consequence

CJK given-name tables had romanizations stripped to avoid `lookup_key` collisions. Those strips
are reverted — "chan" belongs in 찬's variants, "yong" in 용's, etc. Conflicts are now features:
they represent genuine multi-language ambiguity that `lookup()` correctly surfaces.
