## Examples

### Remove all whitespaces in a block

Sometimes you just want to concatenate a list of items without any spaces in
between. If you don't pass any arguments to `whiteless`, this is what happens.
If you absolutely must pass an argument, pass `all`.

**Input:**

```django
{!tests/examples/remove-all-whitespaces.md!}
```

**Output:**

```text
{!tests/examples/remove-all-whitespaces.output!}
```

### Remove leading whitespaces

To remove all leading whitespaces inside the block, pass the `leading`
argument.

**Input:**

```django
{!tests/examples/remove-leading-whitespaces.md!}
```

**Output:**

```text
{!tests/examples/remove-leading-whitespaces.output!}
```

### Remove trailing whitespaces

Unsurprisingly, to remove all trailing whitespaces, pass `trailing`.

**Input:**

```django
{!tests/examples/remove-trailing-whitespaces.md!}
```

**Output:**

```text
{!tests/examples/remove-trailing-whitespaces.output!}
```

### Remove leading and trailing whitespaces

You can combine `leading` and `trailing` to remove both leading and trailing
whitespaces.

**Input:**

```django
{!tests/examples/remove-leading-trailing-whitespaces.md!}
```

**Output:**

```text
{!tests/examples/remove-leading-trailing-whitespaces.output!}
```

### Replace all whitespaces with a single space

If you have a lot of whitespace in a block and want to remove the extras, but
keep a single space, pass `space`.

**Input:**

```django
{!tests/examples/replace-with-space.md!}
```

**Output:**

```text
{!tests/examples/replace-with-space.output!}
```

### Remove trailing newlines

Sometimes, your project style forces you to add a trailing newline to the end
of every file, but it makes the output just wrong. In that scenario, you can
use `{% eof %}` at the end of your template. Technically, it removes any
immediately subsequent whitespaces from the output.

(For technical reasons, the input below looks like it has no trailing newlines,
but in actuality, it has two.)

**Input:**

```django
{!tests/examples/remove-trailing-newlines.md!}
```

**Output:**

```text
{!tests/examples/remove-trailing-newlines.output!}
```
