# django-whiteless

Django template tags for removing and normalizing whitespace.

[![Checks](https://github.com/denizdogan/django-whiteless/actions/workflows/check.yaml/badge.svg)](https://github.com/denizdogan/django-whiteless/actions/workflows/check.yaml)
[![Coverage](https://codecov.io/gh/denizdogan/django-whiteless/graph/badge.svg)](https://app.codecov.io/github/denizdogan/django-whiteless)

## Installation

```sh
pip install django-whiteless
```

Add `"whiteless"` to `INSTALLED_APPS`, then load the tags in your template:

```djangotemplate
{% load whiteless %}
```

## Usage

### `{% whiteless %}`

Remove all whitespace from a rendered block:

```djangotemplate
{% whiteless %}
    Hello, world!
{% endwhiteless %}
```

Output: `Hello,world!`

Pass options to change the behavior:

| Option | Effect |
| --- | --- |
| `all` (default) | Remove all whitespace |
| `space` | Collapse whitespace to single spaces |
| `leading` | Remove whitespace at the start |
| `trailing` | Remove whitespace at the end |
| `strip` | Remove whitespace at both ends |

Combine options in the order they should run. For example, collapse whitespace
and trim the result:

```djangotemplate
{% whiteless space strip %}
    Hello,     {{ name }}!
{% endwhiteless %}
```

With `name="Mark"`, the output is `Hello, Mark!`.

Transformations include whitespace in variable values, not just indentation.
This is not an HTML-aware minifier. Each block is processed independently, so
spaces from adjacent loop iterations are not collapsed together.

### `{% eof %}`

Remove whitespace immediately following the tag, such as a final newline:

```djangotemplate
Hello!{% eof %}
```

It does not reach past another tag or comment, or trim variable values.

## Compatibility

Supports maintained Python and Django release lines:

| Django | Python |
| --- | --- |
| 5.2 LTS | 3.11–3.14 |
| 6.0 | 3.12–3.14 |
| 6.1 | 3.12–3.15* |

Use the latest patch releases. *Python 3.15 passes this library's tests with
Django 6.1.2; Django's official support starts with 6.1.3.*

## Development

With [mise](https://mise.jdx.dev/) installed:

```sh
mise trust
mise run setup
mise run check
mise run test:all
```

Matrix tests use [tox](https://tox.wiki/) with uv and the committed lockfile.

## License

[MIT](LICENSE)
