## 1.0.x

**1.0.0**

- Many small tweaks to public API; see documentation.
- C++ examples updated.
- Float32 functionality now available and tested in Python.

## 0.3.x

- Changed symmetric EMD storage from lower triangular to upper triangular to match SciPy's `squareform` function.

**0.3.4**

- Fixed bug with masking out particles farther than R from the origin.

**0.3.3**

- Wheels are now built against older NumPy versions to facilitate compatibility.

**0.3.2**

- Migrated continuous integration testing and building to travis-ci.com.
- Changed location of `nbins` argument to `CorrelationDimension` to better match boost histogram usage.
- Building wheels for more architectures now.
- Using SWIG 4.0.2.

**0.3.1**

- C++ example added.
- Documentation updated.
- Small tweaks to some methods.

**0.3.0**

- Changes to some argument names.
- First version that EnergyFlow is designed to work with.
- First version with online documentation.

## 0.2.x

**0.2.0**

- First public version that should have reliable functionality.
- Tests written that cover most of the code.

## 0.1.x

- Rapid testing and development including getting the Python build system on [Travis-CI](https://travis-ci.org/github/pkomiske/Wasserstein).