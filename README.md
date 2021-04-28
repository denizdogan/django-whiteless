# django-whiteless

Django template tags which deal with pesky whitespaces!

[![CircleCI](https://circleci.com/gh/denizdogan/django-whiteless/tree/master.svg?style=svg)](https://circleci.com/gh/denizdogan/django-whiteless/tree/master)

- Django 2.x and 3.x
- Python 3.7, 3.8, 3.9

## Installation

Install the latest version from PyPI:

```bash
$ pip install django-whiteless
```

Add `"whiteless"` to `INSTALLED_APPS`:

```python
INSTALLED_APPS = (
    # ...
    "whiteless",
)
```

## Usage

The library consists of two template tags, `{% whiteless %}` and `{% eof %}`.
This is how you use them.

### Remove all whitespaces

```djangotemplate
{% whiteless %}
    ...
{% endwhiteless %}
```

### Remove leading whitespaces

```djangotemplate
{% whiteless leading %}
    ...
{% endwhiteless %}
```

### Remove trailing whitespaces

```djangotemplate
{% whiteless trailing %}
    ...
{% endwhiteless %}
```

### Remove leading and trailing whitespaces

```djangotemplate
{% whiteless leading trailing %}
    ...
{% endwhiteless %}
```

### Replace whitespaces with a single space

```djangotemplate
{% whiteless space %}
    ...
{% endwhiteless %}
```

Note that if there are leading or trailing whitespaces in the block, those will
also be replaced by a single space. In order to remove leading and trailing
whitespaces and replace all other whitespaces with a single space, use:

```djangotemplate
{% whiteless space leading trailing %}
    ...
{% endwhiteless %}
```

### Remove trailing whitespaces at end of file

```djangotemplate
Hello there!{% eof %}
```

This is useful if e.g. your project style guide requires all files to end with
a newline but that causes issues with your template.

Note that `{% eof %}` cannot be used inside other tags. It only removes
whitespaces that immediately follow itself.

## Development

```shell
$ poetry shell
$ poetry install
$ pre-commit install  # install git hooks
$ tox  # run tests
```

## License

[MIT](LICENSE)
