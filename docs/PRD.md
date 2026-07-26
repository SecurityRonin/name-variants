# name-variants — Purpose & Scope

> Library-tier intent doc (a concise Purpose & Scope, per the fleet PRD & ADR
> Standard and [ADR-0003 doc-naming](https://github.com/SecurityRonin/ronin-issen)).
> It is not a full product PRD; the depth matches a linked library, not an
> examiner-run tool.

## What it is

`name-variants` resolves a romanized name to the set of native-script names it
could represent, and answers whether two romanizations are the same underlying
name. `"Chan"` is simultaneously 陳 / 陈 (Chinese) and 찬 (a Korean given name);
`lookup("Chan")` returns *both* clusters, and `share_cluster("Hsu", "Xu")` is
`True`.

The unit of meaning is the **`NameCluster`** — a frozenset of co-equal
representations of one name, with no canonical/preferred form. `陳`, `陈`, `chen`,
`chan`, `tan`, `chern` all belong to one Chinese-surname cluster; none is more
"real" than the others. Ambiguity is returned, not silently resolved (see
[ADR-0001](decisions/0001-equivalence-class-name-model.md)).

The name data is a hand-curated set of 18 language tables (Chinese surnames and
given names, Japanese, Korean, Arabic, Vietnamese, the three Indian scripts,
Persian, Hebrew, Thai, Greek, Turkish, Russian, Indonesian/Malay), each a plain
Python dict of `{ native_key: {forms, frequency, dialects} }`. Those dicts are the
single source of truth for every runtime surface (see
[ADR-0002](decisions/0002-multi-runtime-from-single-source.md)).

## Who links it

- **Python consumers** link the pure-Python package `name-variants` (PyPI). This
  is the primary, fully-featured surface: the `lookup` / `share_cluster` /
  `dialect` / `normalize` API, plus a `nv` CLI, a pandas `.nv` accessor, and an
  MCP server (`nv-mcp`) for AI clients. Zero required runtime dependencies beyond
  `click` (pandas and MCP are optional extras).
- **Rust consumers** depend on the crate `name-variants` (crates.io; source in
  `name-variants-rs/`). It exposes `lookup_key`, `lookup_all`, `lookup_candidates`,
  and `get_cluster_info` over compile-time `phf` maps — zero runtime
  dependencies, and Rust users never need Python.
- **Python consumers wanting native speed** can additionally build the optional
  PyO3 extension `name_variants._native` (`name-variants-py`, wheel-only,
  `publish = false`) over the Rust core. It is an accelerator; the pure-Python
  implementation stays the default and the reference behavior.
- **JavaScript / browser consumers** use `name-variants-wasm`, a wasm-bindgen
  build (separate npm artifact) exposing `lookup_key` and `lookup_candidates`.

## Scope

- Equivalence-class lookup: given a name in any known romanization or native
  script, return every `NameCluster` that contains it, ordered by bearer
  frequency (most likely interpretation first).
- Equivalence testing (`share_cluster`) for record-linkage / dedup / entity
  matching across romanization systems.
- Chinese romanization-system tagging (`dialect`): Mandarin Pinyin, Wade-Giles,
  Cantonese, Hokkien, Hakka, Teochew, Postal, Traditional, Simplified.
- Text normalization (`normalize`): NFC, casefold, whitespace collapse, Unicode
  format-character stripping, optional diacritic stripping.
- Cross-runtime parity: the same table data drives Python, Rust, an optional
  native Python extension, and wasm.

## Non-goals

- **Not a transliteration/romanization *engine*.** It does not generate a
  romanization from arbitrary text; it looks names up against curated tables.
  Names absent from the tables return empty (`lookup("Smith") == []`), by design.
- **Not a phonetic/fuzzy matcher.** Matching is exact/lowercase/token-split
  against known forms — not Soundex, edit-distance, or ML similarity.
- **Not a personal-data store or identity resolver.** It maps orthographic
  variants of *names*, not people; it holds no PII and makes no claim that two
  same-cluster names belong to the same individual.
- **Not exhaustive.** Coverage is a curated, frequency-weighted subset per
  language, not a census of every surname.
- **No canonical/preferred output form** — surfacing ambiguity is the point;
  callers that need a single key choose one from the returned cluster.

## Success criteria

- `share_cluster` is symmetric and correct for the documented cross-system pairs
  (Hsu/Xu, Chou/Zhou, Chiang/Jiang, Tsao/Cao, Park/Bak, Muhammad/Mohammed,
  Ivanov/Ivanoff), verified in the Python and Rust test suites.
- Rust and Python return equivalent clusters for the same input (the codegen
  drift-check keeps `generated.rs` in sync with the Python tables).
- Zero required runtime dependencies for both the Rust crate and the core Python
  import; optional capabilities (pandas, MCP, native extension) stay opt-in.
