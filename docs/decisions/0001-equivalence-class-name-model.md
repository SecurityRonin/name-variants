# 1. NameCluster equivalence classes instead of a canonical key

Date: 2026-07-27
Status: Accepted

## Context

A name-variant lookup can be modelled two ways:

1. **Canonical key** — every romanization maps to one "true" form, e.g.
   `"Chan" → 陳`. Lookup returns a single answer.
2. **Equivalence class** — all representations of a name are co-equal members of
   a set, with no preferred form. Lookup returns every set the input belongs to.

The canonical-key model breaks on the data this library targets:

- `"Chan"` is a valid romanization of the Chinese surname 陳/陈 (Cantonese) *and*
  of a Korean given name 찬. A single canonical key must pick one and drop the
  other — silent data loss.
- Chinese has two scripts for the same surname (Traditional 陳 / Simplified 陈).
  Neither is "more canonical"; choosing one is arbitrary.
- With one flat variant→key map, whichever table is loaded last wins for shared
  romanizations, so **table ordering becomes load-bearing** and given-name
  romanizations must be scrubbed from surname tables to avoid collisions.

The library's whole value proposition — record linkage across romanization
systems for OSINT / entity matching / dedup — depends on *surfacing* ambiguity,
not suppressing it.

## Decision

The unit of meaning is the `NameCluster`: a `frozenset` of co-equal forms plus a
`language` tag and an optional bearer `frequency`. There is no canonical or
preferred form inside a cluster.

- `lookup(text)` returns **all** clusters containing `text` (as native script,
  lowercased, or a whitespace token), sorted by `frequency` descending so the
  statistically most likely interpretation comes first — but every candidate is
  returned. Unknown input returns `[]`, never a guess.
- `share_cluster(a, b)` is `True` iff some cluster contains both — the
  equivalence test that record-linkage callers actually want.
- Membership is case-insensitive; empty/whitespace input is not a match.

Reference: `name_variants/__init__.py` (`NameCluster`, `lookup`,
`share_cluster`, `_build_clusters`). The Rust core stores a first-write-wins flat
index for `lookup_key` but preserves the multi-cluster semantics through
`lookup_candidates` + `get_cluster_info`, which the PyO3 binding uses to
reconstruct the same list-of-clusters result (`name-variants-rs/src/lib.rs`,
`name-variants-py/src/lib.rs`).

## Consequences

- Ambiguity is a first-class result, not an error or a silently-chosen winner;
  callers decide how to disambiguate using `frequency` and `language`.
- Adding a romanization is one edit to one table entry's `forms` list — no
  re-tuning of table order and no cross-table collision surgery.
- Callers that need a single string must choose one member of a returned cluster
  themselves; the library deliberately provides no "the answer" accessor.
- The Rust surface exposes both a single-key convenience (`lookup_key`, first
  match) and the full candidate set (`lookup_candidates`); the single-key path is
  a convenience over the same data, not a competing canonical-key model.
