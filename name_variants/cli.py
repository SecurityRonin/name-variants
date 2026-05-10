"""
nv — name-variants CLI.

Commands:
    lookup           Show all clusters for a name.
    match            Test if two names share a cluster.
    canonicalize-csv Add a canonical-key column to a CSV file.
    dedupe           Add a cluster_id column grouping rows by cluster.
"""

from __future__ import annotations

import csv
import sys

import click

from name_variants import lookup as _lookup_api, share_cluster


def _canonical_key(name: str) -> str:
    """
    Return the best single canonical form for a name.

    Uses the storage key of the highest-frequency cluster, or passthrough
    for unknown names — mirroring the old canonicalize() behaviour.
    """
    clusters = _lookup_api(name)
    if not clusters:
        return name.strip()
    # Find the storage key: the form that appears as a key in the source table.
    from name_variants import ALL_TABLES
    cluster = clusters[0]
    lang = cluster.language
    table = ALL_TABLES.get(lang, {})
    for form in cluster.forms:
        if form in table:
            return form
    # fallback: pick shortest form (native script is usually compact)
    return min(cluster.forms, key=len)


@click.group()
def cli() -> None:
    """Multilingual name variant lookup and normalization tools."""


@cli.command()
@click.argument("name")
def lookup(name: str) -> None:
    """Show clusters containing NAME (passthrough if unknown)."""
    clusters = _lookup_api(name)
    if clusters:
        for cluster in clusters:
            click.echo(f"{cluster.language}: {sorted(cluster.forms)}")
    else:
        click.echo(name.strip())


@cli.command()
@click.argument("a")
@click.argument("b")
@click.option(
    "--exit-code",
    is_flag=True,
    default=False,
    help="Exit 0 if same cluster, 1 if different (for shell scripting).",
)
def match(a: str, b: str, exit_code: bool) -> None:
    """Test whether A and B share a cluster."""
    same = share_cluster(a, b)
    click.echo("True" if same else "False")
    if exit_code and not same:
        sys.exit(1)


@cli.command("canonicalize-csv")
@click.argument("file", type=click.Path(exists=True))
@click.option("--col", required=True, help="Name of the column to canonicalize.")
@click.option("--out", default=None, help="Output CSV path (default: stdout).")
@click.option("--out-col", default=None, help="Output column name (default: {col}_canonical).")
def canonicalize_csv(file: str, col: str, out: str | None, out_col: str | None) -> None:
    """Add a canonical-key column to a CSV file."""
    with open(file, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames is None or col not in reader.fieldnames:
            raise click.ClickException(f"Column '{col}' not found in {file}")
        output_col = out_col or f"{col}_canonical"
        fieldnames = list(reader.fieldnames) + [output_col]
        rows = []
        for row in reader:
            row[output_col] = _canonical_key(row[col])
            rows.append(row)

    dest = open(out, "w", newline="", encoding="utf-8") if out else sys.stdout
    try:
        writer = csv.DictWriter(dest, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    finally:
        if out:
            dest.close()


@cli.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("--col", required=True, help="Name of the column to group by cluster.")
@click.option("--out", default=None, help="Output CSV path (default: stdout).")
def dedupe(file: str, col: str, out: str | None) -> None:
    """Add a cluster_id column grouping rows that share a cluster."""
    with open(file, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames is None or col not in reader.fieldnames:
            raise click.ClickException(f"Column '{col}' not found in {file}")
        fieldnames = list(reader.fieldnames) + ["cluster_id"]
        rows = list(reader)

    cluster_map: dict[frozenset[str], int] = {}

    def _cluster(name: str) -> str:
        clusters = _lookup_api(name)
        if clusters:
            key = clusters[0].forms
            if key not in cluster_map:
                cluster_map[key] = len(cluster_map) + 1
            return str(cluster_map[key])
        synthetic = frozenset([name.lower().strip()])
        if synthetic not in cluster_map:
            cluster_map[synthetic] = len(cluster_map) + 1
        return str(cluster_map[synthetic])

    for row in rows:
        row["cluster_id"] = _cluster(row[col])

    dest = open(out, "w", newline="", encoding="utf-8") if out else sys.stdout
    try:
        writer = csv.DictWriter(dest, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    finally:
        if out:
            dest.close()
