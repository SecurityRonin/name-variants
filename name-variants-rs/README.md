# name-variants

Multilingual name romanization lookup tables for Rust — Chinese, Japanese, Korean,
Arabic, Vietnamese, Indian, Persian, Hebrew, Thai, Greek, Turkish, Russian, Indonesian/Malay.

Maps romanization variants to their canonical native-script key so that
`Chen`, `Chan`, and `Tan` all resolve to `陳`.

## Usage

```rust
use name_variants::lookup_key;

assert_eq!(lookup_key("Chan"),      Some("陳"));
assert_eq!(lookup_key("chen"),      Some("陳"));   // case-insensitive
assert_eq!(lookup_key("park"),      Some("박"));
assert_eq!(lookup_key("Muhammad"),  Some("محمد"));
assert_eq!(lookup_key("Smith"),     None);

// Multi-word: first matching token wins
assert_eq!(lookup_key("Chan Wai Ming"), Some("陳"));
```

## Install

```toml
[dependencies]
name-variants = "0.1"
```

## Design

- **Canonical key is always the native script form** — `陳`, `박`, `محمد`
- **Zero runtime dependencies** — all data in a compile-time perfect hash map (`phf`)
- **Case-insensitive** — input is lowercased before lookup
- **`None` for unknowns** — explicit signal to fall back to fuzzy matching
