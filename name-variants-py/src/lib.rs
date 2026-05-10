use pyo3::prelude::*;
use pyo3::types::{PyDict, PyList};

/// Return all NameClusters that contain this text as a member form.
///
/// Returns a list of dicts: ``[{"language": "chinese", "forms": ["陈", "chen", ...]}, ...]``
/// Returns ``[]`` for unknown names or empty input.
#[pyfunction]
fn lookup(py: Python<'_>, text: &str) -> PyResult<PyObject> {
    let candidates = name_variants::lookup_candidates(text);
    let results = PyList::empty_bound(py);

    for storage_key in &candidates {
        if let Some((language, forms)) = name_variants::get_cluster_info(storage_key) {
            let d = PyDict::new_bound(py);
            d.set_item("language", language)?;
            // Build forms list: canonical key first, then variants (deduped)
            let mut all_forms: Vec<&str> = vec![storage_key];
            for &f in forms {
                if f != *storage_key {
                    all_forms.push(f);
                }
            }
            let py_forms = PyList::new_bound(py, &all_forms);
            d.set_item("forms", py_forms)?;
            results.append(d)?;
        }
    }

    Ok(results.into())
}

/// PyO3 native extension for name-variants.
///
/// Optional high-performance backend. Import via ``name_variants._native``.
#[pymodule]
fn _native(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(lookup, m)?)?;
    Ok(())
}
