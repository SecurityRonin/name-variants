# MCP Server Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Expose `lookup`, `share_cluster`, and `dialect` as MCP tools so AI assistants can query name-variant equivalence classes.

**Architecture:** A single `name_variants/server.py` module using `FastMCP` from the `mcp` SDK. Tools are thin wrappers over the existing public API; `NameCluster` objects are serialized to plain dicts (`{language, forms, frequency}`) before returning. The server is installed as an `[mcp]` optional extra and run via the `nv-mcp` entry point.

**Tech Stack:** Python 3.11+, `mcp>=1.0` (Anthropic MCP SDK, `FastMCP`), `pytest` (sync tests using `asyncio.run`)

---

### Context you need

- Public API lives in `name_variants/__init__.py`: `lookup(text) -> list[NameCluster]`, `share_cluster(a, b) -> bool`, `dialect(text) -> str | None`
- `NameCluster` is a frozen dataclass: `forms: frozenset[str]`, `language: str`, `frequency: int | None`
- Existing tests in `tests/` use plain `pytest` (no asyncio plugin). Follow the same pattern.
- `FastMCP` lives at `mcp.server.fastmcp.FastMCP`
- In-process tool calls: `content_list, raw = await mcp_instance.call_tool(name, args)` — `raw["result"]` holds the Python return value
- Wrap `asyncio.run(...)` in a sync helper for tests — no `pytest-asyncio` needed

---

### Task 1: Add `[mcp]` extra and `nv-mcp` entry point

**Files:**
- Modify: `pyproject.toml`

**Step 1: Add the extra and entry point**

In `pyproject.toml`, add to `[project.optional-dependencies]`:
```toml
mcp = ["mcp>=1.0"]
```

Add to `[project.scripts]`:
```toml
nv-mcp = "name_variants.server:main"
```

Also add `mcp>=1.0` to the `dev` extra so tests can import it without the extra being installed.

**Step 2: Install and verify**

```bash
pip install -e ".[mcp,dev]"
python3 -c "from mcp.server.fastmcp import FastMCP; print('ok')"
```
Expected: `ok`

**Step 3: Commit**

```bash
git add pyproject.toml
git commit -m "chore: add [mcp] extra and nv-mcp entry point"
```

---

### Task 2: `_cluster_to_dict` helper + `lookup` tool (TDD)

**Files:**
- Create: `name_variants/server.py`
- Create: `tests/test_mcp_server.py`

**Step 1: Write the failing tests**

Create `tests/test_mcp_server.py`:

```python
"""Tests for the MCP server tools."""
import asyncio

import pytest

from name_variants import NameCluster
from name_variants.server import _cluster_to_dict, mcp


def _call(tool: str, args: dict):
    _, raw = asyncio.run(mcp.call_tool(tool, args))
    return raw["result"]


# ── _cluster_to_dict ─────────────────────────────────────────────────────────

def test_cluster_to_dict_fields():
    c = NameCluster(forms=frozenset(["chen", "陈"]), language="chinese", frequency=90_000_000)
    d = _cluster_to_dict(c)
    assert d["language"] == "chinese"
    assert sorted(d["forms"]) == sorted(["chen", "陈"])
    assert d["frequency"] == 90_000_000
    assert isinstance(d["forms"], list)


def test_cluster_to_dict_no_frequency():
    c = NameCluster(forms=frozenset(["kim"]), language="korean")
    d = _cluster_to_dict(c)
    assert d["frequency"] is None


# ── lookup tool ──────────────────────────────────────────────────────────────

def test_lookup_chan_returns_chinese_first():
    result = _call("lookup", {"text": "Chan"})
    assert len(result) >= 1
    assert result[0]["language"] == "chinese"
    assert "chan" in result[0]["forms"]


def test_lookup_unknown_returns_empty():
    result = _call("lookup", {"text": "Smith"})
    assert result == []


def test_lookup_result_is_list_of_dicts():
    result = _call("lookup", {"text": "Chan"})
    for item in result:
        assert "language" in item
        assert "forms" in item
        assert "frequency" in item
        assert isinstance(item["forms"], list)
```

**Step 2: Run to confirm RED**

```bash
pytest tests/test_mcp_server.py -v
```
Expected: `ImportError: cannot import name 'server' from 'name_variants'`

**Step 3: Write minimal implementation**

Create `name_variants/server.py`:

```python
"""MCP server exposing name-variants tools."""
from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from name_variants import NameCluster
from name_variants import dialect as _dialect
from name_variants import lookup as _lookup
from name_variants import share_cluster as _share_cluster

mcp = FastMCP(
    "name-variants",
    instructions=(
        "Query multilingual name romanization equivalence classes. "
        "lookup() returns every cluster containing a name form. "
        "share_cluster() tests whether two strings are romanizations of the same name. "
        "dialect() identifies the Chinese romanization system."
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
    """Return all name clusters containing this romanization or script form, sorted by bearer count."""
    return [_cluster_to_dict(c) for c in _lookup(text)]


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
```

**Step 4: Run to confirm GREEN**

```bash
pytest tests/test_mcp_server.py::test_cluster_to_dict_fields \
       tests/test_mcp_server.py::test_cluster_to_dict_no_frequency \
       tests/test_mcp_server.py::test_lookup_chan_returns_chinese_first \
       tests/test_mcp_server.py::test_lookup_unknown_returns_empty \
       tests/test_mcp_server.py::test_lookup_result_is_list_of_dicts -v
```
Expected: 5 passed

**Step 5: RED commit**

```bash
git add tests/test_mcp_server.py
git commit -m "test(mcp): RED — lookup tool and _cluster_to_dict tests"
```

**Step 6: GREEN commit**

```bash
git add name_variants/server.py
git commit -m "feat(mcp): lookup tool and _cluster_to_dict helper"
```

---

### Task 3: `share_cluster` and `dialect` tools (TDD)

**Files:**
- Modify: `tests/test_mcp_server.py`
- Modify: `name_variants/server.py`

**Step 1: Add failing tests**

Append to `tests/test_mcp_server.py`:

```python
# ── share_cluster tool ───────────────────────────────────────────────────────

def test_share_cluster_same():
    assert _call("share_cluster", {"a": "Chan", "b": "Chen"}) is True


def test_share_cluster_different():
    assert _call("share_cluster", {"a": "Chan", "b": "Kim"}) is False


def test_share_cluster_empty_input():
    assert _call("share_cluster", {"a": "", "b": "Chan"}) is False


# ── dialect tool ─────────────────────────────────────────────────────────────

def test_dialect_cantonese():
    assert _call("dialect", {"text": "chan"}) == "cantonese"


def test_dialect_mandarin():
    assert _call("dialect", {"text": "chen"}) == "mandarin_pinyin"


def test_dialect_wade_giles():
    assert _call("dialect", {"text": "chou"}) == "wade_giles"


def test_dialect_unknown_returns_none():
    assert _call("dialect", {"text": "Smith"}) is None
```

**Step 2: Run to confirm RED**

```bash
pytest tests/test_mcp_server.py -v
```
Expected: 7 new failures (`share_cluster` and `dialect` tools not found)

**Step 3: Add the two tools to `server.py`**

After the `lookup` tool definition, add:

```python
@mcp.tool()
def share_cluster(a: str, b: str) -> bool:
    """Return True if both strings appear in any common name cluster (romanization equivalence check)."""
    return _share_cluster(a, b)


@mcp.tool()
def dialect(text: str) -> str | None:
    """Return the Chinese romanization system for this variant: mandarin_pinyin, cantonese, hokkien, wade_giles, traditional, etc. Returns None for non-Chinese or untagged forms."""
    return _dialect(text)
```

**Step 4: Run to confirm GREEN**

```bash
pytest tests/test_mcp_server.py -v
```
Expected: all tests pass

**Step 5: RED commit**

```bash
git add tests/test_mcp_server.py
git commit -m "test(mcp): RED — share_cluster and dialect tool tests"
```

**Step 6: GREEN commit**

```bash
git add name_variants/server.py
git commit -m "feat(mcp): share_cluster and dialect tools"
```

---

### Task 4: `nv-mcp` entry point smoke test + lint

**Files:**
- Modify: `tests/test_mcp_server.py`
- No source changes needed

**Step 1: Add smoke test**

Append to `tests/test_mcp_server.py`:

```python
# ── server smoke test ────────────────────────────────────────────────────────

def test_server_has_three_tools():
    tool_names = {t.name for t in asyncio.run(mcp.list_tools())}
    assert tool_names == {"lookup", "share_cluster", "dialect"}
```

**Step 2: Run to confirm RED**

```bash
pytest tests/test_mcp_server.py::test_server_has_three_tools -v
```
Expected: PASS (already green — this is a validation that wires to the entry point)

**Step 3: Verify `nv-mcp` entry point exists**

```bash
which nv-mcp && nv-mcp --help
```
Expected: help text from FastMCP (or the process starts and blocks — Ctrl-C to exit)

**Step 4: Run ruff**

```bash
ruff check name_variants/server.py && ruff format --check name_variants/server.py
```
Fix any issues: `ruff check --fix name_variants/server.py && ruff format name_variants/server.py`

**Step 5: Commit**

```bash
git add tests/test_mcp_server.py
git commit -m "test(mcp): smoke test — server exposes exactly three tools"
```

---

### Task 5: README — MCP section + extras cleanup

**Files:**
- Modify: `README.md`

**Step 1: Update the Optional extras section**

Replace the existing "Optional extras" section with:

```markdown
## Extras

```bash
pip install "name-variants[pandas]"   # pandas Series .nv accessor
pip install "name-variants[mcp]"      # MCP server (Claude Desktop / Claude Code)
```
```

**Step 2: Add MCP usage section** (after the CLI section)

```markdown
## MCP server

```bash
pip install "name-variants[mcp]"
```

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "name-variants": {
      "command": "nv-mcp"
    }
  }
}
```

Three tools are exposed:

| Tool | Arguments | Returns |
|---|---|---|
| `lookup` | `text: str` | list of `{language, forms[], frequency}` clusters |
| `share_cluster` | `a: str, b: str` | `true` / `false` |
| `dialect` | `text: str` | romanization system string or `null` |
```

**Step 3: Commit**

```bash
git add README.md
git commit -m "docs: add MCP server section and extras table"
```

---

### Task 6: CI — test the `[mcp]` extra

**Files:**
- Modify: `.github/workflows/ci.yml`

**Step 1: Add mcp to the test install step**

Find the `python-tests` job's `pip install` step and change:
```yaml
pip install -e ".[dev]"
```
to:
```yaml
pip install -e ".[dev,mcp,pandas]"
```

This ensures `tests/test_mcp_server.py` runs in CI.

**Step 2: Run full test suite locally**

```bash
pytest -x -v
```
Expected: all tests pass including `test_mcp_server.py`

**Step 3: Commit**

```bash
git add .github/workflows/ci.yml
git commit -m "ci: install mcp extra so test_mcp_server runs in CI"
```

---

### Final verification

```bash
pytest -v
ruff check name_variants/ tests/
git log --oneline -10
```
