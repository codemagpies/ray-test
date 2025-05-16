use pyo3::prelude::*;

#[pyfunction]
fn double(x: usize) -> PyResult<usize> {
    Ok(x * 2)
}

#[pymodule]
fn rust_math(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(double, m)?)?;
    Ok(())
}
