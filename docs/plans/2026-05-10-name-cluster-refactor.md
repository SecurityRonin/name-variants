# NameCluster Refactor Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Replace the `lookup_key` / last-write-wins architecture with `NameCluster` equivalence
classes and a `lookup()` function that returns all matching clusters.

**Architecture:** Each name table entry becomes a `NameCluster(forms, language, frequency)` where
`forms` is a `frozenset` of all representations — storage key + variants — with no privileged member.
`lookup(text)` searches a form→clusters index and returns every cluster containing the input.

**Tech Stack:** Python 3.11+, dataclasses (stdlib), pytest, click, pandas (optional), pyo3/maturin

---

### Task 1: Commit design doc

**Files:**
- Already written: `docs/plans/2026-05-10-name-cluster-design.md`
- Already written: `docs/plans/2026-05-10-name-cluster-refactor.md`

**Step 1: Commit**

```bash
git add docs/plans/2026-05-10-name-cluster-design.md docs/plans/2026-05-10-name-cluster-refactor.md
git commit -m "docs: NameCluster architecture design + implementation plan"
```

---

### Task 2 (RED): Tests for NameCluster and lookup()

**Files:**
- Create: `tests/test_cluster.py`

**Step 1: Write the failing tests**

```python
"""Tests for NameCluster and lookup() — the new core API."""
import pytest
from name_variants import NameCluster, lookup, share_cluster


# ── NameCluster basics ────────────────────────────────────────────────────────

def test_cluster_is_immutable():
    c = NameCluster(forms=frozenset({"陈", "chen", "chan"}), language="chinese")
    with pytest.raises((AttributeError, TypeError)):
        c.language = "other"  # type: ignore[misc]


def test_cluster_contains_casefolded():
    c = NameCluster(forms=frozenset({"陈", "chen", "chan"}), language="chinese")
    assert "Chan" in c      # casefolded match
    assert "CHEN" in c
    assert "陈" in c        # direct script match
    assert "陳" not in c    # different character — not in this cluster


def test_cluster_iteration():
    forms = frozenset({"陈", "chen", "chan"})
    c = NameCluster(forms=forms, language="chinese")
    assert set(c) == forms


def test_cluster_len():
    c = NameCluster(forms=frozenset({"陈", "chen", "chan"}), language="chinese")
    assert len(c) == 3


def test_cluster_no_privileged_member():
    c = NameCluster(forms=frozenset({"陈", "陳", "chen", "chan"}), language="chinese")
    # Both Simplified and Traditional are present — neither is "the" canonical
    assert "陈" in c.forms
    assert "陳" in c.forms


def test_cluster_frequency_optional():
    c = NameCluster(forms=frozenset({"陈"}), language="chinese")
    assert c.frequency is None
    c2 = NameCluster(forms=frozenset({"陈"}), language="chinese", frequency=100_000_000)
    assert c2.frequency == 100_000_000


# ── lookup() ─────────────────────────────────────────────────────────────────

def test_lookup_returns_list():
    result = lookup("Chan")
    assert isinstance(result, list)
    assert all(isinstance(c, NameCluster) for c in result)


def test_lookup_chan_has_chinese_cluster():
    clusters = lookup("Chan")
    langs = [c.language for c in clusters]
    assert "chinese" in langs


def test_lookup_chan_chinese_cluster_contains_both_scripts():
    clusters = lookup("Chan")
    chinese = next(c for c in clusters if c.language == "chinese")
    assert "陈" in chinese
    assert "陳" in chinese     # Traditional form also in the cluster


def test_lookup_chan_has_korean_given_cluster():
    # 찬 (praise) has "chan" as its Revised Romanization — both are valid
    clusters = lookup("Chan")
    langs = [c.language for c in clusters]
    assert "korean_given" in langs, (
        f"Expected korean_given in lookup('Chan'), got: {langs}"
    )


def test_lookup_case_insensitive():
    assert lookup("chan") == lookup("Chan")
    assert lookup("CHAN") == lookup("Chan")


def test_lookup_unknown_returns_empty():
    assert lookup("Smith") == []
    assert lookup("Kowalski") == []
    assert lookup("") == []


def test_lookup_whitespace_only_returns_empty():
    assert lookup("   ") == []


def test_lookup_multiword_finds_first_token_match():
    # "Chan Wai Ming" — "Chan" token hits Chinese cluster
    clusters = lookup("Chan Wai Ming")
    langs = [c.language for c in clusters]
    assert "chinese" in langs


def test_lookup_lee_returns_multiple_clusters():
    # "Lee" is Korean 이 (surname), Chinese 李 (surname), Vietnamese lê — all valid
    clusters = lookup("Lee")
    langs = [c.language for c in clusters]
    assert "korean" in langs
    assert "chinese" in langs


def test_lookup_nguyen_returns_single_vietnamese_cluster():
    clusters = lookup("Nguyen")
    assert len(clusters) == 1
    assert clusters[0].language == "vietnamese"


def test_lookup_native_script_direct():
    clusters = lookup("陈")
    assert any(c.language == "chinese" for c in clusters)


def test_lookup_sorted_by_frequency_desc():
    # Higher-frequency clusters should appear first
    clusters = lookup("Lee")
    freqs = [c.frequency or 0 for c in clusters]
    assert freqs == sorted(freqs, reverse=True)


# ── share_cluster() ───────────────────────────────────────────────────────────

def test_share_cluster_same_chinese():
    assert share_cluster("Chan", "Chen") is True


def test_share_cluster_hokkien_mandarin():
    assert share_cluster("Tan", "Chen") is True


def test_share_cluster_different_names():
    assert share_cluster("Chan", "Kim") is False


def test_share_cluster_empty_returns_false():
    assert share_cluster("", "Chan") is False
    assert share_cluster("Chan", "") is False
    assert share_cluster("", "") is False


def test_share_cluster_both_unknown():
    assert share_cluster("Smith", "Smyth") is False


def test_share_cluster_case_insensitive():
    assert share_cluster("CHAN", "chen") is True


def test_share_cluster_korean_romanizations():
    assert share_cluster("Park", "Bak") is True
    assert share_cluster("Lee", "Yi") is True
```

**Step 2: Run to confirm RED**

```bash
python -m pytest tests/test_cluster.py -v --tb=short 2>&1 | tail -20
```

Expected: `ImportError: cannot import name 'NameCluster' from 'name_variants'` (all fail)

**Step 3: Commit RED**

```bash
git add tests/test_cluster.py
git commit -m "test: RED — NameCluster + lookup() + share_cluster() tests"
```

---

### Task 3 (GREEN): Implement NameCluster, lookup(), share_cluster()

**Files:**
- Modify: `name_variants/__init__.py`

**Step 1: Add NameCluster class** (add near top of `__init__.py`, after imports)

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class NameCluster:
    """Equivalence class of name representations — all forms are co-equal."""

    forms: frozenset[str]
    language: str
    frequency: int | None = None

    def __contains__(self, text: str) -> bool:
        t = text.strip()
        return t in self.forms or t.lower() in self.forms

    def __iter__(self):
        return iter(self.forms)

    def __len__(self) -> int:
        return len(self.forms)

    def __repr__(self) -> str:
        return f"NameCluster(language={self.language!r}, {len(self.forms)} forms)"
```

**Step 2: Add cluster-building internals** (replace the existing `_build_index` block with this
plus the new index builder; keep old index builder for now — remove it in Task 10)

```python
# Lazy-built cluster list and form→[cluster] index
_CLUSTERS: list["NameCluster"] | None = None
_FORM_INDEX: dict[str, list["NameCluster"]] | None = None


def _build_clusters() -> tuple[list["NameCluster"], dict[str, list["NameCluster"]]]:
    from name_variants.frequencies import ALL_FREQUENCIES

    clusters: list[NameCluster] = []
    form_index: dict[str, list[NameCluster]] = {}

    for language, table in ALL_TABLES.items():
        for storage_key, variants in table.items():
            forms = frozenset(
                {storage_key}
                | {v.lower().strip() for v in variants if v.strip()}
            )
            freq = ALL_FREQUENCIES.get(storage_key)
            cluster = NameCluster(forms=forms, language=language, frequency=freq)
            clusters.append(cluster)
            for form in forms:
                form_index.setdefault(form, []).append(cluster)

    return clusters, form_index


def _get_form_index() -> dict[str, list["NameCluster"]]:
    global _CLUSTERS, _FORM_INDEX
    if _FORM_INDEX is None:
        _CLUSTERS, _FORM_INDEX = _build_clusters()
    return _FORM_INDEX
```

**Step 3: Add lookup() and share_cluster()**

```python
def lookup(text: str) -> list[NameCluster]:
    """
    Return all NameClusters that contain this text as a member form.

    Searches all 18 language tables. Returns clusters sorted by frequency
    descending (highest bearer count first). Returns [] for unknown names.

    Examples:
        lookup("Chan")   → [NameCluster(chinese, ...), NameCluster(korean_given, ...)]
        lookup("Nguyen") → [NameCluster(vietnamese, ...)]
        lookup("Smith")  → []
    """
    if not text or not text.strip():
        return []

    idx = _get_form_index()
    seen: set[int] = set()
    result: list[NameCluster] = []

    def _collect(key: str) -> None:
        for cluster in idx.get(key, []):
            cid = id(cluster)
            if cid not in seen:
                seen.add(cid)
                result.append(cluster)

    key = text.strip()
    _collect(key)
    key_lower = key.lower()
    if key_lower != key:
        _collect(key_lower)
    for token in key_lower.split():
        _collect(token)

    result.sort(key=lambda c: c.frequency or 0, reverse=True)
    return result


def share_cluster(a: str, b: str) -> bool:
    """
    Return True iff both strings appear in any common NameCluster.

    Returns False if either string is empty or unknown.

    Examples:
        share_cluster("Chan", "Chen")  → True   (both in chinese cluster)
        share_cluster("Chan", "Li")    → False
    """
    if not a or not b:
        return False
    a_clusters = set(lookup(a))
    b_clusters = lookup(b)
    return any(c in a_clusters for c in b_clusters)
```

**Step 4: Add to `__all__`** — add `"NameCluster"`, `"lookup"`, `"share_cluster"` to the existing
`__all__` list (keep old names for now).

**Step 5: Run tests**

```bash
python -m pytest tests/test_cluster.py -v --tb=short 2>&1 | tail -30
```

Expected: most pass, but `test_lookup_chan_has_korean_given_cluster` FAILS because "chan" was
stripped from 찬's variants in Task 10 of the CJK agent. That's fixed in Task 4 of this plan.

**Step 6: Commit GREEN (partial — one test still red)**

```bash
git add name_variants/__init__.py
git commit -m "feat: NameCluster + lookup() + share_cluster() — GREEN (CJK restore pending)"
```

---

### Task 4 (RED→GREEN): Restore stripped romanizations in CJK given-name tables

The CJK given-name tables had romanizations stripped to avoid `lookup_key` collisions. Those
strips are now wrong — conflicts are features with `lookup()`. Restore them.

**Files:**
- Modify: `name_variants/korean_given_names.py`
- Modify: `name_variants/chinese_given_names.py`
- Modify: `name_variants/japanese_given_names.py`

**Step 1: Verify test_lookup_chan_has_korean_given_cluster still fails**

```bash
python -m pytest tests/test_cluster.py::test_lookup_chan_has_korean_given_cluster -v
```

Expected: FAIL

**Step 2: Restore Korean given-name romanizations**

In `korean_given_names.py`, restore the forms that were stripped. Key restorations:

```python
# Before (stripped): "찬": ["chahn"]
# After (restored):  "찬": ["chan", "chahn"]

# Before: "용": ["ryong"]
# After:  "용": ["yong", "ryong"]

# Before: "가": ["ga"]
# After:  "가": ["ga", "ka"]

# Before: "광": ["gwang"]
# After:  "광": ["gwang", "kwang"]

# Before: "지": ["ji", "jee", "chi"]   (chi conflicts with chinese_given 池/治)
# chi is legitimate for 지 in some romanization systems — restore if stripped

# Before: "정": ["jeong", "jung"]      (jung conflicts with korean surname 정)
# jung IS 정 romanized — and now that's fine (both lookup to 정 in different contexts)
```

To find all stripped forms, check what the Revised Romanization of each character should be:
- 찬 → "chan" (RR)
- 용 → "yong" (RR)
- 가 → "ga", "ka" (RR + older)
- 광 → "gwang", "kwang"

Edit `korean_given_names.py` to restore these variants.

**Step 3: Audit `chinese_given_names.py`** for stripped romanizations

Tone-marked forms (míng, wěi) were kept, but bare forms may have been stripped. Restore:
- Any bare pinyin that was removed to avoid conflicts with Chinese surname romanizations
  (conflicts are now OK — they enrich `lookup()` results)

**Step 4: Audit `japanese_given_names.py`** similarly

Restore macron-stripped forms if they match Japanese given-name romanizations.

**Step 5: Run the full cluster test suite**

```bash
python -m pytest tests/test_cluster.py -v --tb=short 2>&1 | tail -20
```

Expected: all pass including `test_lookup_chan_has_korean_given_cluster`.

**Step 6: Commit**

```bash
git add name_variants/korean_given_names.py name_variants/chinese_given_names.py \
        name_variants/japanese_given_names.py
git commit -m "feat(data): restore CJK given-name romanizations stripped for lookup_key compat"
```

---

### Task 5 (RED→GREEN): Rewrite test_lookup.py for new API

Replace all `lookup_key()` / `lookup_candidates()` / `lookup_all()` calls.

**Files:**
- Rewrite: `tests/test_lookup.py`

**Key patterns:**

```python
# Old: assert lookup_key("Chan") == lookup_key("Chen")
# New: assert share_cluster("Chan", "Chen")

# Old: assert lookup_key("Chan") == "陈"
# New: assert any("陈" in c for c in lookup("Chan"))
# or:  assert any(c.language == "chinese" for c in lookup("Chan"))

# Old: result = lookup_candidates("Lee")
#      assert "이" in result and "李" in result
# New: clusters = lookup("Lee")
#      all_forms = {f for c in clusters for f in c.forms}
#      assert "이" in all_forms and "李" in all_forms

# Old: assert lookup_candidates("Nguyen") == ["nguyễn"]
# New: clusters = lookup("Nguyen")
#      assert len(clusters) == 1
#      assert "nguyễn" in clusters[0]

# Old: assert lookup_key("陳") == "陈"  (Traditional → Simplified canonical)
# New: assert share_cluster("陳", "陈")
# and: assert any("陈" in c and "陳" in c for c in lookup("陈"))

# Old: assert lookup_key("Kowalski") is None
# New: assert lookup("Kowalski") == []

# Old: result = lookup_all("Chan")
#      assert result[0] == "陈"
# New: clusters = lookup("Chan")
#      assert any("陈" in c for c in clusters)
```

**Step 1: Rewrite the file** following these patterns for all 60+ tests.

Keep `test_all_tables_present`, `test_all_romanizations_are_lowercase`,
`test_all_keys_nonempty` unchanged — they test data, not the lookup API.

**Step 2: Run**

```bash
python -m pytest tests/test_lookup.py -v --tb=short 2>&1 | tail -20
```

Expected: all pass.

**Step 3: Commit**

```bash
git add tests/test_lookup.py
git commit -m "test: rewrite test_lookup.py for lookup()/share_cluster() API"
```

---

### Task 6 (RED→GREEN): Rewrite test_utils.py for new API

**Files:**
- Rewrite: `tests/test_utils.py`

**Changes:**
- Replace `is_variant()` with `share_cluster()` — identical semantics
- Remove all `canonicalize()` tests (function removed)
- Keep all `normalize()` tests unchanged

```python
# Old: from name_variants import canonicalize, is_variant, normalize
# New: from name_variants import normalize, share_cluster

# Old: assert is_variant("Chan", "Chen") is True
# New: assert share_cluster("Chan", "Chen") is True

# Old: assert canonicalize("Chan") == "陈"
# Delete this test — no canonical

# Old: assert canonicalize("Smith") == "Smith"
# Delete — no canonicalize function
```

**Step 1: Rewrite the file**

**Step 2: Run**

```bash
python -m pytest tests/test_utils.py -v --tb=short 2>&1 | tail -20
```

**Step 3: Commit**

```bash
git add tests/test_utils.py
git commit -m "test: rewrite test_utils.py — share_cluster replaces is_variant, drop canonicalize"
```

---

### Task 7 (RED→GREEN): Update CLI

The CLI commands use the old API. Update them to use `lookup()` and `share_cluster()`.

**Files:**
- Modify: `name_variants/cli.py`
- Modify: `tests/test_cli.py`

**`nv lookup <name>`** — show all matching clusters:

```python
@cli.command()
@click.argument("name")
def lookup_cmd(name: str) -> None:
    """Look up all name clusters matching NAME."""
    from name_variants import lookup as nv_lookup
    clusters = nv_lookup(name)
    if not clusters:
        click.echo(f"{name}: no match")
        return
    for c in clusters:
        forms_str = "  ".join(sorted(c.forms))
        freq = f"  (~{c.frequency:,} bearers)" if c.frequency else ""
        click.echo(f"[{c.language}]{freq}")
        click.echo(f"  {forms_str}")
```

**`nv match <a> <b>`** — use `share_cluster()`:

```python
@cli.command()
@click.argument("a")
@click.argument("b")
@click.option("--exit-code", is_flag=True)
def match(a: str, b: str, exit_code: bool) -> None:
    from name_variants import share_cluster
    result = share_cluster(a, b)
    click.echo("true" if result else "false")
    if exit_code and not result:
        raise SystemExit(1)
```

**`nv canonicalize-csv`** — rename to `nv cluster-csv`; output a `cluster_id` column
(stable hex hash) instead of a canonical string. Keep `--col` and `--out` flags.

```python
import hashlib

def _cluster_id(name: str) -> str:
    from name_variants import lookup as nv_lookup
    clusters = nv_lookup(name)
    if not clusters:
        return ""
    # Use the first (highest-frequency) cluster's stable hash
    c = clusters[0]
    h = hashlib.sha256(f"{c.language}:{sorted(c.forms)}".encode()).hexdigest()[:12]
    return h

@cli.command("cluster-csv")
@click.argument("file")
@click.option("--col", required=True)
@click.option("--out", default=None)
@click.option("--out-col", default=None)
def cluster_csv(file: str, col: str, out: str | None, out_col: str | None) -> None:
    """Add a cluster_id column to a CSV."""
    import csv, sys
    out_col = out_col or f"{col}_cluster_id"
    # ... same CSV read/write pattern as old canonicalize-csv
```

**`nv dedupe`** — update to use `_cluster_id()` helper.

**Step 1: Update tests first** (`tests/test_cli.py`):

```python
# Old: test_lookup_known checks "陈" in output
# New: check "[chinese]" in output

# Old: test_canonicalize_csv_adds_column checks rows[0]["name_canonical"] == "陈"
# New: test_cluster_csv_adds_column checks rows[0]["name_cluster_id"] is a 12-char hex string

# Remove test_lookup_unknown_passthrough (no passthrough — unknown returns "no match")
```

**Step 2: Run tests RED**

```bash
python -m pytest tests/test_cli.py -v --tb=short 2>&1 | tail -20
```

**Step 3: Implement CLI changes**

**Step 4: Run tests GREEN**

```bash
python -m pytest tests/test_cli.py -v --tb=short 2>&1 | tail -20
```

**Step 5: Commit**

```bash
git add name_variants/cli.py tests/test_cli.py
git commit -m "feat(cli): lookup/match/cluster-csv/dedupe use NameCluster API"
```

---

### Task 8 (RED→GREEN): Update Pandas accessor

**Files:**
- Modify: `name_variants/pandas_ext.py`
- Modify: `tests/test_pandas_accessor.py`

**Changes:**

```python
# Old: def lookup(self) -> pd.Series:  # canonical key or None
# New: def lookup(self) -> pd.Series:  # list[NameCluster] per element

# Old: def canonical(self, fallback="passthrough") -> pd.Series:
# Remove — no canonical

# Old: def is_variant_of(self, other: pd.Series) -> pd.Series:
# New: def share_cluster_with(self, other: pd.Series) -> pd.Series:

# Old: def cluster_id(self) -> pd.Series:  # using canonical as ID
# New: def cluster_id(self) -> pd.Series:  # using sha256 hash of (language, forms)
```

Updated accessor:

```python
@pd.api.extensions.register_series_accessor("nv")
class NameVariantsAccessor:
    def __init__(self, obj: pd.Series) -> None:
        self._obj = obj

    def lookup(self) -> pd.Series:
        """Return list[NameCluster] for each element."""
        from name_variants import lookup as nv_lookup
        return self._obj.map(lambda x: nv_lookup(str(x)) if pd.notna(x) else [])

    def share_cluster_with(self, other: pd.Series) -> pd.Series:
        """Element-wise: do self[i] and other[i] share a cluster?"""
        from name_variants import share_cluster
        return pd.Series(
            [share_cluster(str(a), str(b)) for a, b in zip(self._obj, other)],
            index=self._obj.index,
        )

    def cluster_id(self) -> pd.Series:
        """Stable cluster hash for the highest-frequency matching cluster."""
        import hashlib
        from name_variants import lookup as nv_lookup

        def _id(x: object) -> str:
            clusters = nv_lookup(str(x)) if pd.notna(x) else []
            if not clusters:
                return ""
            c = clusters[0]
            return hashlib.sha256(
                f"{c.language}:{sorted(c.forms)}".encode()
            ).hexdigest()[:12]

        return self._obj.map(_id)

    def candidates(self) -> pd.Series:
        """Return list[NameCluster] — alias for lookup()."""
        return self.lookup()
```

**Step 1: Update tests to RED, then implement, then verify GREEN**

```bash
python -m pytest tests/test_pandas_accessor.py -v --tb=short 2>&1 | tail -20
```

**Step 2: Commit**

```bash
git add name_variants/pandas_ext.py tests/test_pandas_accessor.py
git commit -m "feat(pandas): .nv accessor uses NameCluster API"
```

---

### Task 9 (RED→GREEN): Update remaining test files

**Files:**
- Modify: `tests/conftest.py`
- Modify: `tests/test_tables.py`
- Modify: `tests/test_frequency.py`
- Modify: `tests/test_dialect.py`
- Modify: `tests/test_cjk_given_names.py`

**conftest.py** — property test parametrization unchanged (still iterates ALL_TABLES), but the
assertion changes:

```python
# Old: candidates = lookup_candidates(canonical)
#      assert canonical in candidates
# New: clusters = lookup(canonical)
#      assert any(canonical in c for c in clusters), (
#          f"{_table_name}: {canonical!r} not in any cluster from lookup({canonical!r})"
#      )
```

**test_tables.py** — same change as conftest.py.

**test_frequency.py** — remove `get_language_for_canonical` tests; add cluster-based tests:

```python
# Old: from name_variants import get_frequency, get_language_for_canonical, language_distribution
# New: from name_variants import lookup

# Old: assert get_frequency("陈") is not None
# New: clusters = lookup("陈")
#      assert any(c.frequency for c in clusters)

# Old: assert get_language_for_canonical("陈") == "chinese"
# New: clusters = lookup("陈")
#      assert any(c.language == "chinese" for c in clusters)

# Old: dist = language_distribution("Lee")
# Remove language_distribution tests (function removed)
```

**test_dialect.py** — `lookup_dialect()` stays as standalone util; tests unchanged.

**test_cjk_given_names.py** — replace `lookup_key` with `lookup`:

```python
# Old: assert lookup_key("Wei") is not None  (Chinese given name)
# New: assert len(lookup("Wei")) > 0

# Old: assert lookup_key("재") == "재"
# New: assert any("재" in c for c in lookup("재"))
```

**Step 1: Make all changes**

**Step 2: Run**

```bash
python -m pytest tests/test_tables.py tests/test_frequency.py tests/test_dialect.py \
        tests/test_cjk_given_names.py -v --tb=short 2>&1 | tail -20
```

**Step 3: Commit**

```bash
git add tests/conftest.py tests/test_tables.py tests/test_frequency.py \
        tests/test_dialect.py tests/test_cjk_given_names.py
git commit -m "test: update property test + frequency/dialect/CJK tests for NameCluster API"
```

---

### Task 10: Remove old API from __init__.py

**Files:**
- Modify: `name_variants/__init__.py`

**Step 1: Verify all tests pass before removal**

```bash
python -m pytest tests/ --tb=short -q 2>&1 | tail -10
```

Must be 0 failures before proceeding.

**Step 2: Remove these functions from `__init__.py`**:
- `_build_index()` (old index builder)
- `_get_index()`, `_get_variants()`, `_get_candidates()`
- `_INDEX`, `_VARIANTS`, `_CANDIDATES` globals
- `lookup_key()`
- `lookup_all()`
- `lookup_candidates()`
- `canonicalize()`
- `is_variant()`
- `get_language_for_canonical()`
- `_get_language_for_canonical()`
- `get_frequency()`
- `language_distribution()`

**Keep:** `lookup_dialect()` (standalone utility, not tied to "key" concept)

**Step 3: Update `__all__`**:

```python
__all__ = [
    "NameCluster",
    "lookup",
    "share_cluster",
    "ALL_TABLES",
    "normalize",
    "lookup_dialect",
]
```

**Step 4: Run full suite**

```bash
python -m pytest tests/ --tb=short -q 2>&1 | tail -10
```

Expected: 0 failures.

**Step 5: Commit**

```bash
git add name_variants/__init__.py
git commit -m "refactor: remove lookup_key / canonicalize / is_variant old API"
```

---

### Task 11 (RED→GREEN): Update PyO3 bindings

**Files:**
- Modify: `name-variants-py/src/lib.rs`
- Modify: `tests/test_native.py`

The native extension exposed `lookup_key`, `lookup_all`, `lookup_candidates`. Update to expose
`lookup()` returning a list of dicts (since PyO3 can't directly expose Python dataclasses).

**Step 1: Update test_native.py**

```python
# Old: assert _native.lookup_key("Chan") == "陈"
# New: result = _native.lookup("Chan")
#      assert isinstance(result, list)
#      assert any(r["language"] == "chinese" for r in result)
#      assert any("陈" in r["forms"] for r in result)
```

**Step 2: Update lib.rs**

```rust
#[pyfunction]
fn lookup(text: &str) -> Vec<HashMap<String, PyObject>> {
    // Call Rust lookup_candidates to get all matching storage keys,
    // then return list of dicts with "language", "forms" keys
    // (Full NameCluster semantics via the Rust layer)
    todo!()
}
```

Note: The Rust codegen needs updating to regenerate `generated.rs` after romanization
restorations in Task 4. Run: `python codegen/gen_rust.py` before rebuilding.

**Step 3: Rebuild and test**

```bash
maturin develop --manifest-path name-variants-py/Cargo.toml
python -m pytest tests/test_native.py -v
```

**Step 4: Commit**

```bash
git add name-variants-py/src/lib.rs tests/test_native.py
git commit -m "feat(pyo3): native extension exposes lookup() returning cluster dicts"
```

---

### Task 12: Full suite + Rust codegen regeneration

**Step 1: Regenerate Rust generated.rs** (after Task 4 restored romanizations)

```bash
python codegen/gen_rust.py
cargo test --manifest-path name-variants-rs/Cargo.toml
```

**Step 2: Run full Python test suite**

```bash
python -m pytest tests/ -q 2>&1 | tail -5
```

Expected: 0 failures.

**Step 3: Commit codegen**

```bash
git add name-variants-rs/src/generated.rs
git commit -m "chore(codegen): regenerate generated.rs after CJK romanization restore"
```

---

**Plan complete and saved to `docs/plans/2026-05-10-name-cluster-refactor.md`.**

Two execution options:

**1. Subagent-Driven (this session)** — I dispatch a fresh subagent per task, review between tasks

**2. Parallel Session (separate)** — Open new session with executing-plans, batch execution with checkpoints

Which approach?
