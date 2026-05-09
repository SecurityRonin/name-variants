"""
pytest fixtures shared across the test suite.
"""

import pytest

from name_variants import ALL_TABLES


def pytest_generate_tests(metafunc):
    if "canonical_entry" in metafunc.fixturenames:
        entries = [
            (table_name, canonical)
            for table_name, table in ALL_TABLES.items()
            for canonical in table
        ]
        ids = [f"{t}:{c}" for t, c in entries]
        metafunc.parametrize("canonical_entry", entries, ids=ids)


@pytest.fixture
def all_canonicals():
    """All (table_name, canonical_key) pairs across every table."""
    return [
        (table_name, canonical)
        for table_name, table in ALL_TABLES.items()
        for canonical in table
    ]
