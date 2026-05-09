"""Table-level completeness and structural invariants."""
import pytest

from name_variants import ALL_TABLES, lookup_key
from name_variants.chinese_surnames import CHINESE_SURNAME_VARIANTS


def test_minimum_entry_counts():
    """Each table must have a meaningful number of entries."""
    minimums = {
        "chinese": 100,
        "arabic": 50,
        "japanese": 100,
        "korean": 50,
        "vietnamese": 40,
        "indian_hindi": 40,
        "indian_tamil": 30,
        "indian_bengali": 30,
        "persian": 40,
        "hebrew": 40,
        "thai": 40,
        "greek": 40,
        "turkish": 40,
        "russian": 40,
        "indonesian_malay": 30,
    }
    for table_name, minimum in minimums.items():
        count = len(ALL_TABLES[table_name])
        assert count >= minimum, (
            f"{table_name}: only {count} entries, expected >= {minimum}"
        )


def test_no_empty_variant_lists():
    for table_name, table in ALL_TABLES.items():
        for canonical, variants in table.items():
            assert variants, f"{table_name}: {canonical!r} has empty variant list"


def test_no_duplicate_variants_within_entry():
    for table_name, table in ALL_TABLES.items():
        for canonical, variants in table.items():
            assert len(variants) == len(set(variants)), (
                f"{table_name}: {canonical!r} has duplicate variants: {variants}"
            )


def test_every_canonical_self_lookup(canonical_entry):
    """Every unambiguous canonical self-resolves; ambiguous ones are skipped."""
    from name_variants import lookup_candidates
    _table_name, canonical = canonical_entry
    # Pure-ASCII canonicals that genuinely appear in multiple tables are
    # ambiguous by design — last-write-wins picks one, which is expected.
    if len(lookup_candidates(canonical)) > 1:
        pytest.skip(f"ambiguous romanization '{canonical}' maps to multiple canonicals")
    result = lookup_key(canonical)
    assert result == canonical, (
        f"{_table_name}: canonical {canonical!r} self-lookup returned {result!r}"
    )


def test_known_ambiguous_latin_canonicals():
    """Document canonicals that are intentionally ambiguous across tables."""
    from name_variants import lookup_candidates
    # Pure-ASCII names shared across language tables — losing their self-lookup
    # is expected; lookup_candidates() is the right API for these.
    known_ambiguous = ["chu", "nam", "chi", "kim", "hasan", "hassan"]
    for name in known_ambiguous:
        assert len(lookup_candidates(name)) > 1, (
            f"'{name}' expected to be ambiguous but is now unambiguous"
        )


def test_known_romanization_collisions_are_documented():
    """
    Some romanizations genuinely map to multiple surnames (e.g. 'ng' for both
    黄 and 吴). These are acceptable — assert they exist so we know the table
    is realistic, not sanitized.
    """
    ng_entries = [char for char, variants in CHINESE_SURNAME_VARIANTS.items()
                  if "ng" in variants]
    assert len(ng_entries) >= 2, "'ng' should be ambiguous across Chinese surnames"
