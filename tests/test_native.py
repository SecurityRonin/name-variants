"""Tests for the optional name_variants._native PyO3 extension."""

import pytest


def _skip_if_no_native():
    try:
        from name_variants import _native  # noqa: F401
    except ImportError:
        pytest.skip("_native extension not built — run: maturin develop")


def test_native_lookup_chan_returns_list():
    _skip_if_no_native()
    from name_variants import _native

    result = _native.lookup("Chan")
    assert isinstance(result, list)
    assert len(result) > 0


def test_native_lookup_chan_has_chinese():
    _skip_if_no_native()
    from name_variants import _native

    result = _native.lookup("Chan")
    assert any(r["language"] == "chinese" for r in result)


def test_native_lookup_chan_chinese_has_both_scripts():
    _skip_if_no_native()
    from name_variants import _native

    result = _native.lookup("Chan")
    chinese = next(r for r in result if r["language"] == "chinese")
    assert "陈" in chinese["forms"]
    assert "陳" in chinese["forms"]


def test_native_lookup_unknown_returns_empty():
    _skip_if_no_native()
    from name_variants import _native

    assert _native.lookup("Smith") == []
    assert _native.lookup("") == []


def test_native_lookup_returns_dicts_with_forms_and_language():
    _skip_if_no_native()
    from name_variants import _native

    result = _native.lookup("Park")
    assert len(result) > 0
    r = result[0]
    assert "forms" in r
    assert "language" in r
    assert isinstance(r["forms"], list)
    assert isinstance(r["language"], str)
