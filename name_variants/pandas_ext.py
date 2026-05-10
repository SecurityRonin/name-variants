"""Pandas Series accessor for name-variants."""
from __future__ import annotations

import hashlib

import pandas as pd


@pd.api.extensions.register_series_accessor("nv")
class NameVariantsAccessor:
    """Accessor: series.nv.lookup(), .share_cluster_with(), .cluster_id()"""

    def __init__(self, obj: pd.Series) -> None:
        self._obj = obj

    def lookup(self) -> pd.Series:
        """Return list[NameCluster] for each element."""
        from name_variants import lookup as nv_lookup
        return self._obj.map(lambda x: nv_lookup(str(x)) if pd.notna(x) else [])

    def share_cluster_with(self, other: pd.Series) -> pd.Series:
        """Element-wise: do self[i] and other[i] share any NameCluster?"""
        from name_variants import share_cluster
        return pd.Series(
            [share_cluster(str(a), str(b)) for a, b in zip(self._obj, other)],
            index=self._obj.index,
        )

    def cluster_id(self) -> pd.Series:
        """Stable 12-char hex ID for the highest-frequency matching cluster, or '' if unknown."""
        from name_variants import lookup as nv_lookup

        def _id(x: object) -> str:
            clusters = nv_lookup(str(x)) if pd.notna(x) else []
            if not clusters:
                return ""
            c = clusters[0]
            return hashlib.sha256(
                f"{c.language}:{sorted(c.forms)}".encode()
            ).hexdigest()[:12]

        return self._obj.map(_id)
