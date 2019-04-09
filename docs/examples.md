## Examples

To use any of this functionality, you need to load the `whiteless` tag library:

    {% load whiteless %}

### Remove all whitespaces in a block

```djangotemplate
{!tests/examples/remove-all-whitespaces.md!}
```

Output:

```djangotemplate
{!tests/examples/remove-all-whitespaces.output!}
```

### Remove leading whitespaces

```djangotemplate
{!tests/examples/remove-leading-whitespaces.md!}
```

Output:

```djangotemplate
{!tests/examples/remove-leading-whitespaces.output!}
```

### Remove trailing whitespaces

```djangotemplate
{!tests/examples/remove-trailing-whitespaces.md!}
```

Output:

```djangotemplate
{!tests/examples/remove-trailing-whitespaces.output!}
```

### Remove leading and trailing whitespaces

```djangotemplate
{!tests/examples/remove-leading-trailing-whitespaces.md!}
```

Output:

```djangotemplate
{!tests/examples/remove-leading-trailing-whitespaces.output!}
```

### Replace whitespaces with a single space

```djangotemplate
{!tests/examples/replace-with-space.md!}
```

Output:

```djangotemplate
{!tests/examples/replace-with-space.output!}
```

### Remove trailing newlines

In some projects, files are required to end with a trailing newline by style
convention. If this newline causes issues in your project, you can remove it by
ending the template with `{% eof %}`:

```
Hello world!{% eof %}

```

(Note the trailing newline above. It will be removed from the output.)
Technically, `{% eof %}` removes all of its subsequent whitespaces. It is
currently not possible to remove whitespaces before it. For that, look at
[Remove leading whitespaces](#remove-leading-whitespaces) instead.
