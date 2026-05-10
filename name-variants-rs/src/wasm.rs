// WASM bindings — compiled only when targeting wasm32.
// Build with: wasm-pack build name-variants-rs --target web

use wasm_bindgen::prelude::*;

/// Return the canonical script-form key for a name, or `undefined` if unknown.
#[wasm_bindgen]
pub fn lookup_key(text: &str) -> Option<String> {
    crate::lookup_key(text).map(|s| s.to_string())
}

/// Return all canonical keys that list this romanization as a variant.
#[wasm_bindgen]
pub fn lookup_candidates(text: &str) -> Vec<String> {
    crate::lookup_candidates(text)
        .iter()
        .map(|s| s.to_string())
        .collect()
}
