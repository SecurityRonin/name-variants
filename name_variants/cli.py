"""
nv — name-variants CLI.

Commands:
    lookup          Resolve a name to its canonical key.
    match           Test if two names share a canonical key.
    canonicalize-csv  Add a canonical-key column to a CSV file.
    dedupe          Add a cluster_id column grouping rows by canonical key.
"""

from __future__ import annotations

import csv
import sys

import click

from name_variants import canonicalize, is_variant, lookup_key


@click.group()
def cli() -> None:
    """Multilingual name variant lookup and normalization tools."""


@cli.command()
@click.argument("name")
def lookup(name: str) -> None:
    """Resolve NAME to its canonical key (passthrough if unknown)."""
    click.echo(canonicalize(name))


@cli.command()
@click.argument("a")
@click.argument("b")
@click.option(
    "--exit-code",
    is_flag=True,
    default=False,
    help="Exit 0 if same canonical, 1 if different (for shell scripting).",
)
def match(a: str, b: str, exit_code: bool) -> None:
    """Test whether A and B share a canonical key."""
    same = is_variant(a, b)
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
            row[output_col] = canonicalize(row[col])
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
@click.option("--col", required=True, help="Name of the column to group by canonical key.")
@click.option("--out", default=None, help="Output CSV path (default: stdout).")
def dedupe(file: str, col: str, out: str | None) -> None:
    """Add a cluster_id column grouping rows that share a canonical key."""
    with open(file, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames is None or col not in reader.fieldnames:
            raise click.ClickException(f"Column '{col}' not found in {file}")
        fieldnames = list(reader.fieldnames) + ["cluster_id"]
        rows = list(reader)

    # Assign cluster IDs: canonical key → integer id (unknowns each get their own)
    cluster_map: dict[str, int] = {}
    _unknown_counter = 0

    def _cluster(name: str) -> str:
        nonlocal _unknown_counter
        key = lookup_key(name)
        if key is None:
            # Each unknown name gets a unique cluster
            _unknown_counter += 1
            synthetic = f"__unknown_{name.lower().strip()}__"
            if synthetic not in cluster_map:
                cluster_map[synthetic] = len(cluster_map) + 1
            return str(cluster_map[synthetic])
        if key not in cluster_map:
            cluster_map[key] = len(cluster_map) + 1
        return str(cluster_map[key])

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
