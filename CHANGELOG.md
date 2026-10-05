# Changelog

All notable changes to pyDevSup will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2.1.0] - 2026-10-05

### Added

- Alarm message support: `Record.setSevr()` accepts an optional `amsg`
  argument, using `recGblSetSevrMsg()` where EPICS Base supports it and
  falling back to `recGblSetSevr()` on older versions ([#48](https://github.com/epics-modules/pyDevSup/pull/48))
- Windows support: pyDevSup can be built and run on Windows ([#51](https://github.com/epics-modules/pyDevSup/pull/51))
- Full-width `INT64`/`UINT64` record support, which had previously been
  truncated to `epicsInt32`/`epicsUInt32` ([#50](https://github.com/epics-modules/pyDevSup/pull/50))
- Long string record support ([#50](https://github.com/epics-modules/pyDevSup/pull/50))
- `calcout` record support ([#50](https://github.com/epics-modules/pyDevSup/pull/50))
- `workflow_dispatch` manual trigger for CI builds ([#53](https://github.com/epics-modules/pyDevSup/pull/53))
- Documentation note that pyDevSup cannot be used with static EPICS builds,
  and why ([#53](https://github.com/epics-modules/pyDevSup/pull/53))
- This CHANGELOG file ([#57](https://github.com/epics-modules/pyDevSup/pull/57))

### Changed

- Static, pre-generated `.dbd` files (`_dbapi.dbd`, `_int64.dbd`,
  `_lsilso.dbd`) are installed instead of being generated at runtime from a
  temporary file, avoiding a Windows file-locking issue and allowing
  EPICS-Base-version-conditional content ([#50](https://github.com/epics-modules/pyDevSup/pull/50))
- `makehelper.py` reworked to use `sysconfig` instead of `distutils` ([#51](https://github.com/epics-modules/pyDevSup/pull/51))
- Consolidated `.gitignore` handling into a single top-level file, based on
  EPICS base template gitignore ([#55](https://github.com/epics-modules/pyDevSup/pull/55))
- Minor `dbfield.c` cleanup: dropped an unneeded `Python.h` include and
  declared `aval` directly as `PyArrayObject *`, avoiding a cast ([#53](https://github.com/epics-modules/pyDevSup/pull/53))
- Removed a now-deprecated `PyEval_InitThreads()` call in `setup.c` ([#53](https://github.com/epics-modules/pyDevSup/pull/53))

### Fixed

- `assign_array()` in `dbfield.c` reworked to use the same
  `(prset=dbGetRset(...)) && prset->get_array_info` NULL-guarded pattern used
  elsewhere in the file ([#53](https://github.com/epics-modules/pyDevSup/pull/53))
- `disect.py`'s Python 3 fallback for the Python-2-only `InstanceType`
  import, which left the name undefined and crashed example programs ([#53](https://github.com/epics-modules/pyDevSup/pull/53))

## [2.0.0] - 2025-12-23

**Repository moved**: pyDevSup moved from `mdavidsaver` location to `epics-modules` as discussed here: https://github.com/epics-modules/pyDevSup/issues/41

### Changed

- **Dropped Python 2 support; Python >= 3.6 is now required** ([#43](https://github.com/epics-modules/pyDevSup/pull/43))
- **NumPy v2 compatibility**: replaced use of `NPY_CARRAY`/`NPY_CARRAY_RO`,
  which were removed in newer NumPy, in `dbfield.c` ([#43](https://github.com/epics-modules/pyDevSup/pull/43))
- Removed the pinned NumPy version from `requirements-latest.txt` ([#43](https://github.com/epics-modules/pyDevSup/pull/43))
- Migrated CI from Travis-CI to GitHub Actions, covering Debian 11/12/13 and
  Python 3.6 through 3.13, plus EPICS Base 3.14 and 3.15
- Added macOS to the CI build matrix
- Updated source/release links in the README and documentation to point at
  `epics-modules/pyDevSup` instead of the original `mdavidsaver` ([#44](https://github.com/epics-modules/pyDevSup/pull/44))
- Switched the test runner to `nose2`

### Fixed

- Builds for newer gcc versions ([#43](https://github.com/epics-modules/pyDevSup/pull/43))
- Handling of new/unknown `initHooks` states added by newer EPICS Base
  versions

## [1.2] - 2020-03-10

### Changed

- Ensure `cleanupPy()` runs early, and only once, during IOC shutdown ([#20](https://github.com/epics-modules/pyDevSup/pull/20))
- Avoid a deadlock between the GIL and record scan locks
- Further Python 3 fixes

### Fixed

- `UINT64` handling for EPICS Base >= 3.16
- Build for EPICS Base 3.14
- Executable linking issue
- Miscellaneous compiler warnings

## [1.1] - 2019-03-12

### Added

- `SKIP_DB_INSTALL` option for package builds ([#3](https://github.com/epics-modules/pyDevSup/pull/3))
- `RELEASE.local` support
- Travis-CI integration
- String waveform (`VAL`) handling ([#11](https://github.com/epics-modules/pyDevSup/pull/11))
- Debian packaging for all supported Python 3 versions ([#14](https://github.com/epics-modules/pyDevSup/pull/14))

### Changed

- Ported the module to Python 3 (while retaining Python 2 compatibility) ([#12](https://github.com/epics-modules/pyDevSup/pull/12))
- Separated the `softIocPy` build out from the core Python module build ([#12](https://github.com/epics-modules/pyDevSup/pull/12))
- Don't install Python signal handlers during interpreter init
  (fixes [#5](https://github.com/epics-modules/pyDevSup/issues/5))
  ([#19](https://github.com/epics-modules/pyDevSup/pull/19))
- Python 2/3-compatible dict method usage ([#16](https://github.com/epics-modules/pyDevSup/pull/16))

### Fixed

- macOS build failure ([#17](https://github.com/epics-modules/pyDevSup/pull/17))
- `pyIocApp`'s Makefile ([#18](https://github.com/epics-modules/pyDevSup/pull/18))
- Record.setTime(datetime) error ([#7](https://github.com/epics-modules/pyDevSup/pull/7))

## [1.0] - 2016-04-22

### Added

- `aSub` (array subroutine) record support
- `AsyncOffload` helper
- `Field` get/put of arrays to work with numpy.ndarray
- `devsup.db.initHook()` decorator
- `Record.setTime()` accepting a float
- Archiver Appliance monitoring support (`archApp`)
- Debian packaging

### Changed

- `disect`: track types by name string
- Simpler unicode-to-`char*` conversion

### Fixed

- Reference-counting and a reference leak in `logApp`'s inotify
  wrapper
- Improper use of `DBENTRY` in `dbrec`

## [v0.2] - 2014-06-16

### Added

- Parameter table (`ptable`) framework for building device support from
  Python parameter objects
- Support for building against multiple Python versions, `PY_VER` variable
- Context manager for record locking; thread-safe processing reason tracking
- `Field.getarraylen()` and general array field length get/set

### Changed

- Release the GIL on error paths
- Updated `softIocPy`

## [v0.1] - 2013-07-16

Initial public release.

### Added

- Generic Python device support for standard EPICS record types
- `devsup` Python package (`db`, `ptable`, `disect`, etc.)
- `softIocPy`, an IOC shell with an embedded Python interpreter
- Initial documentation and test IOC

[Unreleased]: https://github.com/epics-modules/pyDevSup/compare/2.1.0...HEAD
[2.1.0]: https://github.com/epics-modules/pyDevSup/compare/2.0.0...2.1.0
[2.0.0]: https://github.com/epics-modules/pyDevSup/compare/1.2...2.0.0
[1.2]: https://github.com/epics-modules/pyDevSup/compare/1.1...1.2
[1.1]: https://github.com/epics-modules/pyDevSup/compare/1.0...1.1
[1.0]: https://github.com/epics-modules/pyDevSup/compare/v0.2...1.0
[v0.2]: https://github.com/epics-modules/pyDevSup/compare/v0.1...v0.2
[v0.1]: https://github.com/epics-modules/pyDevSup/releases/tag/v0.1
