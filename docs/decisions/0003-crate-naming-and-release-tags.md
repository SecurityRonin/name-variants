# 3. Crate/package naming and release-plz tag scheme

Date: 2026-07-27
Status: Accepted

## Context

The repository is `name-variants` and contains several publishable artifacts on
three registries (PyPI, crates.io, npm) with independent version streams. Naming
and release automation have to avoid three concrete collisions:

- The workspace directory `name-variants-rs/` should not force an ugly
  `name-variants-rs` *crate* name on crates.io.
- The PyO3 extension is a Rust crate in the workspace but must never be published
  to crates.io — it is only a PyPI wheel.
- release-plz's default git tag for a single-published-crate workspace is a bare
  `v{{ version }}`, which collides with the fleet convention where a `v[0-9]*`
  tag triggers a *binary* release pipeline.

## Decision

- **Rust crate name is `name-variants`, not `name-variants-rs`.** The directory is
  `name-variants-rs/` (to sit beside `name-variants-py/`), but `Cargo.toml` sets
  `name = "name-variants"` with `[lib] name = "name_variants"`, matching the
  Python import name and the PyPI distribution name for one concept, one name
  across registries.
- **`name-variants-py` is `publish = false`.** It is the PyO3/PyPI-wheel side; it
  is a Cargo workspace member for building but is never a crates.io target.
  release-plz is told the same via `[[package]] name = "name-variants-py"`,
  `release = false` in `release-plz.toml`.
- **Publishing is split by registry.** The Rust crate publishes to crates.io via
  **release-plz** (PR-based, conventional-commit-driven, on merge to `main`); the
  Python package publishes to PyPI from its own hatchling build. They carry
  independent versions (crate `0.1.0`, PyPI `0.1.3` at time of writing).
- **release-plz tags are package-prefixed:** `git_tag_name =
  "{{ package }}-v{{ version }}"`, e.g. `name-variants-v0.1.1`. The character
  after the first `v` is a letter, so the tag never matches a `v[0-9]*` glob and
  cannot fire a binary-release workflow. `release_commits` is an allowlist
  (`feat|fix|perf|refactor|doc|revert`) so `chore`/`ci`/`test`/`style`/`build`
  commits — including release-plz's own release commit — never re-trigger a
  release (the changelog-churn loop).

References: `name-variants-rs/Cargo.toml`, `name-variants-py/Cargo.toml`,
`release-plz.toml`, `pyproject.toml`.

## Consequences

- A Rust user runs `cargo add name-variants` and a Python user runs
  `pip install name-variants` — the same name on both registries.
- The version streams diverge intentionally; the crate and the wheel are not
  lockstepped, and release-plz only ever bumps/publishes the crate.
- The package-prefixed tag both prevents the binary-pipeline false trigger and is
  the prerequisite for the per-crate tagging release-plz assumes.
- The wasm npm package (`name-variants-wasm`) has its own version and is released
  outside release-plz.
