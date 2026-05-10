use pyo3::prelude::*;

/// Return the canonical script-form key for a name, or ``None`` if unknown.
#[pyfunction]
fn lookup_key(text: &str) -> Option<&'static str> {
    name_variants::lookup_key(text)
}

/// Return ``(canonical_key, [variants])`` for a name, or ``None`` if unknown.
#[pyfunction]
fn lookup_all(text: &str) -> Option<(&'static str, Vec<&'static str>)> {
    name_variants::lookup_all(text).map(|(k, v)| (k, v.to_vec()))
}

/// Return all canonical keys that list this romanization as a variant.
#[pyfunction]
fn lookup_candidates(text: &str) -> Vec<&'static str> {
    name_variants::lookup_candidates(text)
}

/// PyO3 native extension for name-variants.
///
/// Optional high-performance backend. Import via ``name_variants._native``.
#[pymodule]
fn _native(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(lookup_key, m)?)?;
    m.add_function(wrap_pyfunction!(lookup_all, m)?)?;
    m.add_function(wrap_pyfunction!(lookup_candidates, m)?)?;
    Ok(())
}
