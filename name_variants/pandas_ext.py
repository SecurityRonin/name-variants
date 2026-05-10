"""
Pandas Series accessor: import to register .nv on pd.Series.

    import name_variants.pandas_ext  # registers accessor
    df["name"].nv.lookup()
    df["name"].nv.canonical()
    df["name"].nv.candidates()
    df["name"].nv.is_variant_of(df["name2"])
    df["name"].nv.cluster_id()
"""

from __future__ import annotations

import pandas as pd

from name_variants import canonicalize, is_variant, lookup_candidates, lookup_key


@pd.api.extensions.register_series_accessor("nv")
class NameVariantsAccessor:
    def __init__(self, pandas_obj: pd.Series) -> None:
        self._obj = pandas_obj

    def lookup(self) -> pd.Series:
        """Map each name to its canonical key, or None if unknown."""
        return self._obj.map(lambda x: lookup_key(x) if isinstance(x, str) else None)

    def canonical(self, fallback: str = "passthrough") -> pd.Series:
        """Map each name to its canonical key; apply fallback for unknowns."""
        return self._obj.map(
            lambda x: canonicalize(x, fallback=fallback) if isinstance(x, str) else x
        )

    def candidates(self) -> pd.Series:
        """Map each name to the list of all canonical keys it matches."""
        return self._obj.map(
            lambda x: lookup_candidates(x) if isinstance(x, str) else []
        )

    def is_variant_of(self, other: pd.Series) -> pd.Series:
        """Element-wise: True iff this series and other share a canonical key."""
        return pd.Series(
            [bool(is_variant(str(a), str(b))) for a, b in zip(self._obj, other)],
            index=self._obj.index,
        )

    def cluster_id(self) -> pd.Series:
        """Assign a stable string cluster ID grouping names by canonical key."""
        cluster_map: dict[str, str] = {}

        def _assign(name: str) -> str:
            if not isinstance(name, str):
                return f"__na_{id(name)}__"
            key = lookup_key(name)
            bucket = key if key is not None else f"__unknown_{name.lower().strip()}__"
            if bucket not in cluster_map:
                cluster_map[bucket] = str(len(cluster_map) + 1)
            return cluster_map[bucket]

        return self._obj.map(_assign)
