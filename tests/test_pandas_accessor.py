"""Tests for the Pandas .nv Series accessor."""
import pytest

pd = pytest.importorskip("pandas")
import pandas as pd  # noqa: E402 — after importorskip


@pytest.fixture(autouse=True)
def _register():
    import name_variants.pandas_ext  # noqa: F401 — registers the accessor


# ── .nv.lookup() ─────────────────────────────────────────────────────────────

def test_nv_lookup_known():
    s = pd.Series(["Chan", "Chen", "Park"])
    result = s.nv.lookup()
    assert result[0] == "陈"
    assert result[1] == "陈"
    assert result[2] == "박"


def test_nv_lookup_unknown_is_none():
    s = pd.Series(["Smith", "Johnson"])
    result = s.nv.lookup()
    assert result[0] is None
    assert result[1] is None


def test_nv_lookup_preserves_index():
    s = pd.Series(["Chan", "Smith"], index=[10, 20])
    result = s.nv.lookup()
    assert result.index.tolist() == [10, 20]


# ── .nv.canonical() ──────────────────────────────────────────────────────────

def test_nv_canonical_passthrough_default():
    s = pd.Series(["Chan", "Smith"])
    result = s.nv.canonical()
    assert result[0] == "陈"
    assert result[1] == "Smith"   # passthrough


def test_nv_canonical_lower_fallback():
    s = pd.Series(["Chan", "Smith"])
    result = s.nv.canonical(fallback="lower")
    assert result[0] == "陈"
    assert result[1] == "smith"


def test_nv_canonical_never_returns_none():
    s = pd.Series(["UnknownXyz"])
    result = s.nv.canonical()
    assert result[0] is not None
    assert isinstance(result[0], str)


# ── .nv.candidates() ─────────────────────────────────────────────────────────

def test_nv_candidates_ambiguous():
    s = pd.Series(["Lee"])
    result = s.nv.candidates()
    candidates = result[0]
    assert "이" in candidates
    assert "李" in candidates


def test_nv_candidates_unambiguous():
    s = pd.Series(["Nguyen"])
    result = s.nv.candidates()
    assert result[0] == ["nguyễn"]


def test_nv_candidates_unknown_empty_list():
    s = pd.Series(["Smith"])
    result = s.nv.candidates()
    assert result[0] == []


# ── .nv.is_variant_of() ──────────────────────────────────────────────────────

def test_nv_is_variant_of_same():
    s1 = pd.Series(["Chan", "Park"])
    s2 = pd.Series(["Chen", "Bak"])
    result = s1.nv.is_variant_of(s2)
    assert result[0] is True
    assert result[1] is True


def test_nv_is_variant_of_different():
    s1 = pd.Series(["Chan"])
    s2 = pd.Series(["Kim"])
    result = s1.nv.is_variant_of(s2)
    assert result[0] is False


def test_nv_is_variant_of_preserves_index():
    s1 = pd.Series(["Chan", "Park"], index=[5, 6])
    s2 = pd.Series(["Chen", "Kim"], index=[5, 6])
    result = s1.nv.is_variant_of(s2)
    assert result.index.tolist() == [5, 6]


# ── .nv.cluster_id() ─────────────────────────────────────────────────────────

def test_nv_cluster_id_same_canonical_same_cluster():
    s = pd.Series(["Chan", "Chen", "Tan"])
    result = s.nv.cluster_id()
    assert result[0] == result[1] == result[2]


def test_nv_cluster_id_different_canonical_different_cluster():
    s = pd.Series(["Chan", "Park"])
    result = s.nv.cluster_id()
    assert result[0] != result[1]


def test_nv_cluster_id_unknowns_get_own_cluster():
    s = pd.Series(["Smith", "Johnson"])
    result = s.nv.cluster_id()
    # Each unknown gets its own stable cluster
    assert result[0] != result[1]


def test_nv_cluster_id_returns_string_series():
    s = pd.Series(["Chan"])
    result = s.nv.cluster_id()
    assert result.dtype == object or str(result.dtype).startswith("str")
