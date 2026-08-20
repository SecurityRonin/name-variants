// `#[pyfunction]` expands to a wrapper carrying an `Into<PyErr>` that clippy
// reports against this crate's spans. It lives in pyo3's generated sibling item,
// so a function-scoped allow does not reach it, and there is nothing here to
// remove. Crate-scoped because this crate is nothing but pyo3 bindings
// (publish = false); drop it when pyo3 stops emitting the conversion.
#![allow(clippy::useless_conversion)]

use pyo3::prelude::*;
use pyo3::types::{PyDict, PyList};

/// Return all `NameClusters` that contain this text as a member form.
///
/// Returns a list of dicts: ``[{"language": "chinese", "forms": ["陈", "chen", ...]}, ...]``
/// Returns ``[]`` for unknown names or empty input.
#[pyfunction]
fn lookup<'py>(py: Python<'py>, text: &str) -> PyResult<Bound<'py, PyList>> {
    let candidates = name_variants::lookup_candidates(text);
    let results = PyList::empty(py);

    for storage_key in &candidates {
        if let Some((language, forms)) = name_variants::get_cluster_info(storage_key) {
            let d = PyDict::new(py);
            d.set_item("language", language)?;
            // Build forms list: canonical key first, then variants (deduped)
            let mut all_forms: Vec<&str> = vec![storage_key];
            for &f in forms {
                if f != *storage_key {
                    all_forms.push(f);
                }
            }
            let py_forms = PyList::new(py, &all_forms)?;
            d.set_item("forms", py_forms)?;
            results.append(d)?;
        }
    }

    Ok(results)
}

/// `PyO3` native extension for name-variants.
///
/// Optional high-performance backend. Import via ``name_variants._native``.
#[pymodule]
fn _native(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(lookup, m)?)?;
    Ok(())
}
