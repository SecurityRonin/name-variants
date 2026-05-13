"""Validate that all 18 data files use the rich NameEntry format."""

import importlib

import pytest

from name_variants import ALL_TABLES


def test_all_entries_are_dicts():
    for table_name, table in ALL_TABLES.items():
        for key, entry in table.items():
            assert isinstance(entry, dict), (
                f"{table_name}[{key!r}]: expected dict, got {type(entry).__name__}"
            )


def test_all_entries_have_forms_list():
    for table_name, table in ALL_TABLES.items():
        for key, entry in table.items():
            assert "forms" in entry, f"{table_name}[{key!r}]: missing 'forms' key"
            assert isinstance(entry["forms"], list), (
                f"{table_name}[{key!r}]: 'forms' must be a list"
            )
            assert entry["forms"], f"{table_name}[{key!r}]: 'forms' must be non-empty"


def test_no_unknown_keys():
    valid = {"forms", "frequency", "dialects"}
    for table_name, table in ALL_TABLES.items():
        for key, entry in table.items():
            extra = set(entry.keys()) - valid
            assert not extra, f"{table_name}[{key!r}]: unknown keys {extra}"


def test_frequency_is_positive_int_when_present():
    for table_name, table in ALL_TABLES.items():
        for key, entry in table.items():
            if "frequency" in entry:
                assert isinstance(entry["frequency"], int) and entry["frequency"] > 0, (
                    f"{table_name}[{key!r}]: frequency must be a positive int"
                )


def test_dialects_is_str_str_dict_when_present():
    valid_dialects = {
        "mandarin_pinyin",
        "cantonese",
        "hokkien",
        "hakka",
        "teochew",
        "wade_giles",
        "traditional",
        "simplified",
        "postal",
    }
    for table_name, table in ALL_TABLES.items():
        for key, entry in table.items():
            if "dialects" in entry:
                d = entry["dialects"]
                assert isinstance(d, dict), f"{table_name}[{key!r}]: dialects must be a dict"
                for form, dialect in d.items():
                    assert isinstance(form, str) and isinstance(dialect, str), (
                        f"{table_name}[{key!r}]: dialects values must be str->str"
                    )
                    assert dialect in valid_dialects, (
                        f"{table_name}[{key!r}]: unknown dialect {dialect!r}"
                    )


def test_frequencies_module_deleted():
    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("name_variants.frequencies")


def test_chinese_romanization_dialects_removed():
    from name_variants import chinese_surnames

    assert not hasattr(chinese_surnames, "CHINESE_ROMANIZATION_DIALECTS"), (
        "CHINESE_ROMANIZATION_DIALECTS should be removed from chinese_surnames.py"
    )


def test_dialect_works_without_separate_dict():
    from name_variants import dialect

    assert dialect("chen") == "mandarin_pinyin"
    assert dialect("chou") == "wade_giles"
    assert dialect("chan") == "cantonese"
    assert dialect("Smith") is None


def test_chinese_surnames_use_traditional_keys():
    from name_variants.chinese_surnames import CHINESE_SURNAME_VARIANTS

    for key, entry in CHINESE_SURNAME_VARIANTS.items():
        dialects = entry.get("dialects", {})
        trad_forms = [f for f, d in dialects.items() if d == "traditional"]
        assert len(trad_forms) == 0 or key in trad_forms, (
            f"Key {key!r} should be the Traditional form but traditional form is {trad_forms}"
        )
