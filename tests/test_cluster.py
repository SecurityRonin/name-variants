"""Tests for NameCluster and lookup() — the new core API."""
import pytest

from name_variants import NameCluster, lookup, share_cluster

# ── NameCluster basics ────────────────────────────────────────────────────────

def test_cluster_is_immutable():
    c = NameCluster(forms=frozenset({"陈", "chen", "chan"}), language="chinese")
    with pytest.raises((AttributeError, TypeError)):
        c.language = "other"  # type: ignore[misc]


def test_cluster_contains_casefolded_romanization():
    c = NameCluster(forms=frozenset({"陈", "chen", "chan"}), language="chinese")
    assert "Chan" in c      # casefolded match
    assert "CHEN" in c


def test_cluster_contains_native_script():
    c = NameCluster(forms=frozenset({"陈", "chen", "chan"}), language="chinese")
    assert "陈" in c        # direct script match


def test_cluster_does_not_contain_different_script_form():
    c = NameCluster(forms=frozenset({"陈", "chen", "chan"}), language="chinese")
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


def test_lookup_unknown_name_returns_empty():
    assert lookup("Smith") == []
    assert lookup("Kowalski") == []


def test_lookup_empty_string_returns_empty():
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


def test_share_cluster_left_empty_returns_false():
    assert share_cluster("", "Chan") is False


def test_share_cluster_right_empty_returns_false():
    assert share_cluster("Chan", "") is False


def test_share_cluster_both_empty_returns_false():
    assert share_cluster("", "") is False


def test_share_cluster_both_unknown():
    assert share_cluster("Smith", "Smyth") is False


def test_share_cluster_case_insensitive():
    assert share_cluster("CHAN", "chen") is True


def test_share_cluster_park_bak():
    assert share_cluster("Park", "Bak") is True


def test_share_cluster_lee_yi():
    assert share_cluster("Lee", "Yi") is True
