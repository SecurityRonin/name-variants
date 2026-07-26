"""Tests for the .nv pandas Series accessor."""

import pytest

pd = pytest.importorskip("pandas")

import name_variants.pandas_ext  # noqa: E402, F401 — registers .nv accessor
from name_variants import NameCluster  # noqa: E402


def test_nv_lookup_returns_list_of_clusters():
    s = pd.Series(["Chan", "Smith"])
    result = s.nv.lookup()
    assert isinstance(result[0], list)
    assert all(isinstance(c, NameCluster) for c in result[0])


def test_nv_lookup_known_name():
    s = pd.Series(["Chan"])
    result = s.nv.lookup()
    langs = [c.language for c in result[0]]
    assert "chinese" in langs


def test_nv_lookup_unknown_returns_empty_list():
    s = pd.Series(["Smith"])
    result = s.nv.lookup()
    assert result[0] == []


def test_nv_share_cluster_with_same():
    a = pd.Series(["Chan", "Park"])
    b = pd.Series(["Chen", "Bak"])
    result = a.nv.share_cluster_with(b)
    assert result[0]  # Chan/Chen share chinese cluster
    assert result[1]  # Park/Bak share korean cluster


def test_nv_share_cluster_with_different():
    a = pd.Series(["Chan"])
    b = pd.Series(["Kim"])
    result = a.nv.share_cluster_with(b)
    assert not result[0]


def test_nv_share_cluster_with_preserves_index():
    a = pd.Series(["Chan", "Park"], index=[10, 20])
    b = pd.Series(["Chen", "Bak"], index=[10, 20])
    result = a.nv.share_cluster_with(b)
    assert list(result.index) == [10, 20]


def test_nv_cluster_id_known_returns_12char_hex():
    s = pd.Series(["Chan"])
    result = s.nv.cluster_id()
    cid = result[0]
    assert isinstance(cid, str)
    assert len(cid) == 12
    assert all(c in "0123456789abcdef" for c in cid)


def test_nv_cluster_id_unknown_returns_empty_string():
    s = pd.Series(["Smith"])
    result = s.nv.cluster_id()
    assert result[0] == ""


def test_nv_cluster_id_same_cluster_same_id():
    s = pd.Series(["Chan", "Chen"])
    result = s.nv.cluster_id()
    assert result[0] == result[1]


def test_nv_cluster_id_different_clusters_different_ids():
    s = pd.Series(["Chan", "Park"])
    result = s.nv.cluster_id()
    assert result[0] != result[1]


def test_nv_cluster_id_returns_string_series():
    s = pd.Series(["Chan", "Smith", "Park"])
    result = s.nv.cluster_id()
    assert isinstance(result, pd.Series)
    # pandas >= 3.0 infers StringDtype for string data; earlier versions use object.
    # The contract is a Series of strings, not a specific dtype representation.
    assert pd.api.types.is_string_dtype(result)
    assert all(isinstance(v, str) for v in result)
