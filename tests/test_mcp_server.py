"""Tests for the MCP server tools."""
import asyncio

from name_variants import NameCluster
from name_variants.server import _cluster_to_dict, mcp


def _call(tool: str, args: dict):
    _, raw = asyncio.run(mcp.call_tool(tool, args))
    return raw["result"]


# ── _cluster_to_dict ─────────────────────────────────────────────────────────

def test_cluster_to_dict_fields():
    c = NameCluster(forms=frozenset(["chen", "陈"]), language="chinese", frequency=90_000_000)
    d = _cluster_to_dict(c)
    assert d["language"] == "chinese"
    assert sorted(d["forms"]) == sorted(["chen", "陈"])
    assert d["frequency"] == 90_000_000
    assert isinstance(d["forms"], list)


def test_cluster_to_dict_no_frequency():
    c = NameCluster(forms=frozenset(["kim"]), language="korean")
    d = _cluster_to_dict(c)
    assert d["frequency"] is None


# ── lookup tool ──────────────────────────────────────────────────────────────

def test_lookup_chan_returns_chinese_first():
    result = _call("lookup", {"text": "Chan"})
    assert len(result) >= 1
    assert result[0]["language"] == "chinese"
    assert "chan" in result[0]["forms"]


def test_lookup_unknown_returns_empty():
    result = _call("lookup", {"text": "Smith"})
    assert result == []


def test_lookup_result_is_list_of_dicts():
    result = _call("lookup", {"text": "Chan"})
    for item in result:
        assert "language" in item
        assert "forms" in item
        assert "frequency" in item
        assert isinstance(item["forms"], list)


# ── share_cluster tool ───────────────────────────────────────────────────────

def test_share_cluster_same():
    assert _call("share_cluster", {"a": "Chan", "b": "Chen"}) is True


def test_share_cluster_different():
    assert _call("share_cluster", {"a": "Chan", "b": "Kim"}) is False


def test_share_cluster_empty_input():
    assert _call("share_cluster", {"a": "", "b": "Chan"}) is False


# ── dialect tool ─────────────────────────────────────────────────────────────

def test_dialect_cantonese():
    assert _call("dialect", {"text": "chan"}) == "cantonese"


def test_dialect_mandarin():
    assert _call("dialect", {"text": "chen"}) == "mandarin_pinyin"


def test_dialect_wade_giles():
    assert _call("dialect", {"text": "chou"}) == "wade_giles"


def test_dialect_unknown_returns_none():
    assert _call("dialect", {"text": "Smith"}) is None
