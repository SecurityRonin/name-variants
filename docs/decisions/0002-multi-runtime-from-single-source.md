# 2. Multi-runtime distribution from one Python-dict source via committed codegen

Date: 2026-07-27
Status: Accepted

## Context

The same name tables must be usable from four runtimes with very different
constraints:

- **Python** — the primary, feature-rich surface (library + `nv` CLI + pandas
  accessor + MCP server), where editing data as plain dicts must stay trivial.
- **Rust** — a crates.io crate for native consumers, ideally with zero runtime
  dependencies and no Python at build or run time.
- **Native-accelerated Python** — a fast path for large batch workloads.
- **JavaScript / browser** — a wasm build for client-side use.

Maintaining four hand-kept copies of ~1,500 table entries would guarantee drift.
The tables also need to stay human-editable (contributors add a variant by
editing one dict entry — forms, frequency, and dialect tag colocated), which
rules out an opaque binary or generated-only format as the source.

## Decision

The 18 Python table modules (`name_variants/*_names.py`, `*_surnames.py`) are the
**single source of truth**. Every other runtime is derived from them:

- **Rust core (`name-variants-rs`, crate `name-variants`).** `codegen/gen_rust.py`
  reads the Python dicts and emits `name-variants-rs/src/generated.rs` — compile-
  time `phf` maps (`INDEX`, `VARIANTS`, `CANDIDATES`, `LANGUAGE`). The generated
  file is **committed**, so Rust users never need Python, and `phf` keeps the only
  dependency to a compile-time perfect-hash builder (**zero runtime deps**). A CI
  drift-check regenerates and diffs to keep `generated.rs` in sync with the tables.
- **Native Python extension (`name-variants-py`).** A PyO3 (`pyo3` 0.22)
  `cdylib` named `_native`, built by maturin, depending on `name-variants-rs` by
  path and imported as `name_variants._native`. It is **`publish = false`** — it
  ships only as a PyPI wheel, never to crates.io — and is an *optional
  accelerator*: the pure-Python implementation remains the default and the
  behavioral reference (`tests/test_native.py` skips when it is not built).
- **WebAssembly (`name-variants-wasm`).** `name-variants-rs/src/wasm.rs`
  (`#[cfg(target_arch = "wasm32")]`, `wasm-bindgen`) exposes `lookup_key` /
  `lookup_candidates`; it is packaged as a **separate npm artifact** with its own
  `package.json`, not a Cargo workspace member.

References: `codegen/gen_rust.py`, `name-variants-rs/src/{lib,generated,wasm}.rs`,
`name-variants-py/{Cargo.toml,src/lib.rs}`, `pyproject.toml` (`[tool.maturin]`),
`name-variants-wasm/package.json`.

## Consequences

- One edit to a Python dict, one `python codegen/gen_rust.py` run, and every
  runtime is updated; the drift-check makes a stale `generated.rs` a red CI, not a
  silent divergence.
- Rust and wasm consumers get the full dataset with no Python dependency and no
  runtime dependencies.
- Python stays the reference implementation; the native extension is strictly an
  optional speed-up, so a missing/unbuilt extension degrades to correct pure
  Python rather than failing.
- The Cargo workspace has exactly two members (`name-variants-rs`,
  `name-variants-py`); the wasm build is deliberately outside the workspace
  because it targets a different registry (npm) and toolchain (`wasm-pack`).
- Regenerating after a data change is a required step in the contributor loop; a
  forgotten regeneration is the main failure mode the CI drift-check guards
  against.
