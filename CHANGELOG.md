# Change log

## 2.0.0 (unreleased)

### Breaking changes

- Require Python 3.11+ and Django 5.2-6.1. Projects on older runtimes must upgrade before installing 2.x.


### Fixes and improvements

- Fix `{% eof %}` stripping a distant text token instead of the immediately following whitespace.
- Support every maintained release line: Python 3.11–3.15 and Django 5.2 LTS, 6.0, and 6.1.
- Test all 11 supported Python/Django combinations. Python 3.15/Django 6.1 is a required compatibility check while upstream official support awaits Django 6.1.3.
- Add runtime API type annotations and a `py.typed` marker for type checkers.
- Add regression tests for token boundaries, nested tags, escaping, repeated rendering, and the existing behavior of ignoring unknown options.
- Replace Hypothesis with deterministic pytest cases covering ASCII and Unicode whitespace, mixed whitespace, empty strings, and non-whitespace preservation.

### Development and release tooling

- Replace Poetry, Black, and isort with uv, Ruff, ty, and standard Python package metadata.
- Define the Python/Django compatibility matrix in tox, using tox-uv and `uv.lock` for reproducible environments.
- Use `uv_build` for pure-Python package builds, reusing uv's bundled backend.
- Use Ruff and ty defaults without custom rules or suppressions. Remove auxiliary pre-commit, workflow-linter, and Twine tooling.
- Manage tools with `mise.lock` and Python dependencies with `uv.lock`, including Django-specific test groups. Mise tasks create and synchronize `.venv` automatically.
- Replace Travis CI with GitHub Actions, installed-wheel tests, Codecov coverage uploads, and dependency updates.
- Publish locally with `mise run publish`, running checks and building fresh artifacts before uploading with uv.

## 1.0.0

- Fix: Whiteless is only used on first run of a for loop ([#1][i1])
- Add Django 3.x support
- Add Python 3.8 and 3.9 support
- Drop Django 1.11 support
- Drop Python 2.7, 3.5 and 3.6 support

## 0.1.0 through 0.1.3

- First release
- Packaging fixes
- Metadata additions
- Documentation

[i1]: https://github.com/denizdogan/django-whiteless/issues/1
