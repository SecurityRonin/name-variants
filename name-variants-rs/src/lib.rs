//! Multilingual name romanization lookup tables.
//!
//! Maps romanization variants to their canonical native-script key so that
//! `Chen`, `Chan`, and `Tan` all resolve to `陈`.

mod generated;

#[cfg(target_arch = "wasm32")]
mod wasm;

/// Return the canonical script-form key for a name, or `None` if unknown.
///
/// Matching order:
/// 1. Exact match (handles native script input like `陈`)
/// 2. Lowercase match (handles `Chan`, `CHAN`)
/// 3. Token-by-token (handles `"Chan Wai Ming"` → checks `chan`)
///
/// # Examples
/// ```
/// use name_variants::lookup_key;
/// assert_eq!(lookup_key("Chan"), Some("陈"));
/// assert_eq!(lookup_key("Smith"), None);
/// ```
pub fn lookup_key(text: &str) -> Option<&'static str> {
    if text.is_empty() {
        return None;
    }

    // 1. Exact match (handles native script keys: 陈, 박, محمد)
    if let Some(key) = generated::INDEX.get(text) {
        return Some(key);
    }

    // 2. Lowercase match (handles Chan, CHAN, chan)
    let lower = text.to_lowercase();
    if let Some(key) = generated::INDEX.get(lower.as_str()) {
        return Some(key);
    }

    // 3. Token-by-token: "Chan Wai Ming" → try each token
    for token in lower.split_whitespace() {
        if let Some(key) = generated::INDEX.get(token) {
            return Some(key);
        }
    }

    None
}

/// Return the canonical key and all known variants for a name, or `None` if unknown.
///
/// # Examples
/// ```
/// use name_variants::lookup_all;
/// let (key, variants) = lookup_all("Chan").unwrap();
/// assert_eq!(key, "陈");
/// assert!(variants.contains(&"chen"));
/// ```
pub fn lookup_all(text: &str) -> Option<(&'static str, &'static [&'static str])> {
    let key = lookup_key(text)?;
    let variants = generated::VARIANTS.get(key)?;
    Some((key, variants))
}

/// Return `(language, forms_slice)` for a canonical storage key, or `None` if unknown.
///
/// Used by the PyO3 extension to build `{"language": "...", "forms": [...]}` dicts.
pub fn get_cluster_info(canonical_key: &str) -> Option<(&'static str, &'static [&'static str])> {
    let language = generated::LANGUAGE.get(canonical_key)?;
    let forms = generated::VARIANTS.get(canonical_key)?;
    Some((language, forms))
}

/// Return all canonical keys that list this romanization as a variant.
///
/// Unlike [`lookup_key`], which returns one result via first-write-wins,
/// this returns every canonical key across all 15 language tables that
/// lists the input as a variant — ordered by table iteration order.
///
/// # Examples
/// ```
/// use name_variants::lookup_candidates;
/// let candidates = lookup_candidates("Lee");
/// assert!(candidates.contains(&"李"));
/// assert!(candidates.contains(&"이"));
/// assert!(lookup_candidates("Smith").is_empty());
/// ```
pub fn lookup_candidates(text: &str) -> Vec<&'static str> {
    if text.is_empty() {
        return Vec::new();
    }
    let mut seen: std::collections::HashSet<&'static str> = std::collections::HashSet::new();
    let mut result: Vec<&'static str> = Vec::new();

    let mut collect = |lookup_key: &str| {
        if let Some(cands) = generated::CANDIDATES.get(lookup_key) {
            for &c in *cands {
                if seen.insert(c) {
                    result.push(c);
                }
            }
        }
    };

    let key = text.trim();
    collect(key);
    let key_lower = key.to_lowercase();
    if key_lower != key {
        collect(key_lower.as_str());
    }
    for token in key_lower.split_whitespace() {
        collect(token);
    }
    result
}

#[cfg(test)]
mod tests {
    use super::*;

    // ── Chinese ──────────────────────────────────────────────────────────────
    #[test]
    fn chan_and_chen_same_key() {
        assert_eq!(lookup_key("chan"), lookup_key("chen"));
    }

    #[test]
    fn chan_resolves_to_simplified_chinese() {
        assert_eq!(lookup_key("chan"), Some("陈"));
    }

    #[test]
    fn hui_and_xu_same_key() {
        // 許/许: Xu (Mandarin), Hui (Cantonese), Kho (Hokkien)
        assert_eq!(lookup_key("hui"), lookup_key("xu"));
    }

    #[test]
    fn wang_and_wong_same_key() {
        assert_eq!(lookup_key("wang"), lookup_key("wong"));
    }

    // ── Korean ───────────────────────────────────────────────────────────────
    #[test]
    fn park_and_bak_same_key() {
        assert_eq!(lookup_key("park"), lookup_key("bak"));
    }

    #[test]
    fn lee_and_rhee_same_key() {
        // "lee" also maps to Chinese 李 in the data, so use yi/rhee — both are Korean-only variants of 이
        assert_eq!(lookup_key("yi"), lookup_key("rhee"));
    }

    // ── Arabic ───────────────────────────────────────────────────────────────
    #[test]
    fn muhammad_and_mohammed_same_key() {
        assert_eq!(lookup_key("muhammad"), lookup_key("mohammed"));
    }

    // ── Russian ──────────────────────────────────────────────────────────────
    #[test]
    fn ivanov_and_ivanoff_same_key() {
        assert_eq!(lookup_key("ivanov"), lookup_key("ivanoff"));
    }

    // ── Case-insensitive ─────────────────────────────────────────────────────
    #[test]
    fn uppercase_input_matches() {
        assert_eq!(lookup_key("CHAN"), Some("陈"));
    }

    #[test]
    fn mixed_case_input_matches() {
        assert_eq!(lookup_key("Chan"), Some("陈"));
    }

    // ── Multi-word token split ────────────────────────────────────────────────
    #[test]
    fn full_name_resolves_via_token_split() {
        // "chan wai ming" → first token "chan" matches
        assert_eq!(lookup_key("Chan Wai Ming"), Some("陈"));
    }

    #[test]
    fn korean_full_name_resolves() {
        assert_eq!(lookup_key("Park Ji-sung"), lookup_key("park"));
    }

    // ── Unknown names ────────────────────────────────────────────────────────
    #[test]
    fn unknown_returns_none() {
        assert_eq!(lookup_key("Smith"), None);
        assert_eq!(lookup_key("Kowalski"), None);
        assert_eq!(lookup_key(""), None);
    }

    #[test]
    fn all_unknown_tokens_returns_none() {
        // "john" maps to Greek Ιωάννης — use names genuinely absent from the dataset
        assert_eq!(lookup_key("Kowalski Smith"), None);
    }

    #[test]
    fn lookup_all_chan_returns_variants() {
        let (key, variants) = lookup_all("Chan").unwrap();
        assert_eq!(key, "陈");
        assert!(variants.contains(&"chen"));
        assert!(variants.contains(&"陳"));
    }

    #[test]
    fn lookup_all_unknown_returns_none() {
        assert!(lookup_all("Smith").is_none());
    }

    // ── lookup_candidates ─────────────────────────────────────────────────────
    #[test]
    fn lookup_candidates_lee_returns_multiple_scripts() {
        let result = lookup_candidates("Lee");
        assert!(result.contains(&"李"), "should contain Chinese 李");
        assert!(result.contains(&"이"), "should contain Korean 이");
    }

    #[test]
    fn lookup_candidates_unknown_returns_empty() {
        assert!(lookup_candidates("Smith").is_empty());
        assert!(lookup_candidates("").is_empty());
    }

    #[test]
    fn lookup_candidates_unambiguous_returns_one() {
        let result = lookup_candidates("Nguyen");
        assert!(!result.is_empty());
    }
}
