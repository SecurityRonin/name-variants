"""Tests for the optional PyO3 native extension."""
import pytest

# These tests are SKIPPED if the native extension is not built.
# To build: maturin develop --manifest-path name-variants-py/Cargo.toml
try:
    from name_variants._native import lookup_all, lookup_candidates, lookup_key

    HAS_NATIVE = True
except ImportError:
    HAS_NATIVE = False

pytestmark = pytest.mark.skipif(not HAS_NATIVE, reason="native extension not built")


def test_native_lookup_key_known():
    assert lookup_key("Chan") == "陈"


def test_native_lookup_key_unknown():
    assert lookup_key("Smith") is None


def test_native_lookup_all_returns_tuple():
    result = lookup_all("Chan")
    assert result is not None
    key, variants = result
    assert key == "陈"
    assert "chen" in variants


def test_native_lookup_candidates_ambiguous():
    result = lookup_candidates("Lee")
    assert "이" in result
    assert "李" in result


def test_native_lookup_candidates_unknown():
    assert lookup_candidates("Smith") == []
