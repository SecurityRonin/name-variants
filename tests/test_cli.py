"""Tests for the nv CLI (lookup, match, canonicalize-csv, dedupe commands)."""
import csv

import pytest
from click.testing import CliRunner

from name_variants.cli import cli


@pytest.fixture
def runner():
    return CliRunner()


# ── nv lookup ─────────────────────────────────────────────────────────────────

def test_lookup_known(runner):
    result = runner.invoke(cli, ["lookup", "Chan"])
    assert result.exit_code == 0
    assert "陈" in result.output


def test_lookup_unknown_passthrough(runner):
    result = runner.invoke(cli, ["lookup", "Smith"])
    assert result.exit_code == 0
    assert "Smith" in result.output


def test_lookup_multiword(runner):
    result = runner.invoke(cli, ["lookup", "Chan Wai Ming"])
    assert result.exit_code == 0
    assert "陈" in result.output


# ── nv match ──────────────────────────────────────────────────────────────────

def test_match_same_name(runner):
    result = runner.invoke(cli, ["match", "Chan", "Chen"])
    assert result.exit_code == 0
    assert "true" in result.output.lower()


def test_match_different_names(runner):
    result = runner.invoke(cli, ["match", "Chan", "Kim"])
    assert result.exit_code == 0
    assert "false" in result.output.lower()


def test_match_exit_code_same(runner):
    # exit code 0 when same (truthy), 1 when different — useful for shell scripting
    assert runner.invoke(cli, ["match", "--exit-code", "Chan", "Chen"]).exit_code == 0


def test_match_exit_code_different(runner):
    assert runner.invoke(cli, ["match", "--exit-code", "Chan", "Kim"]).exit_code == 1


# ── nv canonicalize-csv ───────────────────────────────────────────────────────

def _write_csv(tmp_path, rows, headers=("id", "name")):
    p = tmp_path / "input.csv"
    p.write_text(
        "\n".join([",".join(headers)] + [",".join(str(v) for v in r) for r in rows])
        + "\n"
    )
    return str(p)


def test_canonicalize_csv_adds_column(runner, tmp_path):
    src = _write_csv(tmp_path, [("1", "Chan"), ("2", "Smith"), ("3", "Park")])
    out = str(tmp_path / "out.csv")
    result = runner.invoke(cli, ["canonicalize-csv", src, "--col", "name", "--out", out])
    assert result.exit_code == 0
    rows = list(csv.DictReader(open(out)))
    assert rows[0]["name_canonical"] == "陈"
    assert rows[1]["name_canonical"] == "Smith"   # passthrough for unknown
    assert rows[2]["name_canonical"] == "박"


def test_canonicalize_csv_stdout(runner, tmp_path):
    src = _write_csv(tmp_path, [("1", "Chan")])
    result = runner.invoke(cli, ["canonicalize-csv", src, "--col", "name"])
    assert result.exit_code == 0
    assert "陈" in result.output


def test_canonicalize_csv_custom_output_column(runner, tmp_path):
    src = _write_csv(tmp_path, [("1", "Chan")])
    out = str(tmp_path / "out.csv")
    runner.invoke(cli, ["canonicalize-csv", src, "--col", "name", "--out", out, "--out-col", "key"])
    rows = list(csv.DictReader(open(out)))
    assert "key" in rows[0]
    assert rows[0]["key"] == "陈"


def test_canonicalize_csv_missing_col_error(runner, tmp_path):
    src = _write_csv(tmp_path, [("1", "Chan")])
    result = runner.invoke(cli, ["canonicalize-csv", src, "--col", "nonexistent"])
    assert result.exit_code != 0


# ── nv dedupe ─────────────────────────────────────────────────────────────────

def test_dedupe_adds_cluster_id(runner, tmp_path):
    src = _write_csv(tmp_path, [
        ("1", "Chan"), ("2", "Chen"), ("3", "Smith"), ("4", "Park"), ("5", "Bak"),
    ])
    out = str(tmp_path / "out.csv")
    result = runner.invoke(cli, ["dedupe", src, "--col", "name", "--out", out])
    assert result.exit_code == 0
    rows = list(csv.DictReader(open(out)))
    # Chan and Chen should share a cluster_id
    assert rows[0]["cluster_id"] == rows[1]["cluster_id"]
    # Park and Bak should share a cluster_id
    assert rows[3]["cluster_id"] == rows[4]["cluster_id"]
    # Smith cluster is its own
    assert rows[2]["cluster_id"] != rows[0]["cluster_id"]


def test_dedupe_stdout(runner, tmp_path):
    src = _write_csv(tmp_path, [("1", "Chan"), ("2", "Chen")])
    result = runner.invoke(cli, ["dedupe", src, "--col", "name"])
    assert result.exit_code == 0
    assert "cluster_id" in result.output
