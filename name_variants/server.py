"""MCP server exposing name-variants tools."""
from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from name_variants import NameCluster
from name_variants import lookup as _lookup

mcp = FastMCP(
    "name-variants",
    instructions=(
        "Query multilingual name romanization equivalence classes. "
        "lookup() returns every cluster containing a name form. "
        "share_cluster() tests whether two strings are romanizations of the same name. "
        "dialect() returns the Chinese romanization system for a variant."
    ),
)


def _cluster_to_dict(cluster: NameCluster) -> dict:
    return {
        "language": cluster.language,
        "forms": sorted(cluster.forms),
        "frequency": cluster.frequency,
    }


@mcp.tool()
def lookup(text: str) -> list[dict]:
    """Return all name clusters containing this form, sorted by bearer count."""
    return [_cluster_to_dict(c) for c in _lookup(text)]


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
