import pytest
from django.template import Context, Template


class TestEof:
    def test_trailing_whitespaces(self, whitespace):
        tmpl = Template("{% load whiteless %}{% eof %}" + whitespace)
        out = tmpl.render(Context())
        assert out == ""

    def test_leading_whitespaces(self, whitespace):
        tmpl = Template("{% load whiteless %}" + whitespace + "{% eof %}")
        out = tmpl.render(Context())
        assert out == whitespace

    @pytest.mark.parametrize(
        ("source", "expected"),
        [
            ("{% eof %}", ""),
            ("before{% eof %}", "before"),
            ("{% eof %} \n\ttext  inside \n", "text  inside \n"),
            ("{% eof %} \n{{ value }} \n later", " value  \n later"),
            ("{% eof %}{{ value }} \n later", " value  \n later"),
            ("{% eof %} \n{# comment #} \n later", " \n later"),
            ("{% eof %}{# comment #} \n later", " \n later"),
            (
                "{% eof %} \n{% comment %}ignored{% endcomment %} \n later",
                " \n later",
            ),
            (
                "{% eof %}{% if True %} \n inside{% endif %} \n later",
                " \n inside \n later",
            ),
            (
                "{% eof %} \n{% if True %} \n inside{% endif %} \n later",
                " \n inside \n later",
            ),
            ("{% if True %}inside{% eof %}{% endif %} \n later", "inside \n later"),
            ("{% if True %}inside{% eof %} \n{% endif %} \n later", "inside \n later"),
            (
                "{% whiteless strip %} inside{% eof %} \n{% endwhiteless %} \n later",
                "inside \n later",
            ),
            (
                "{% if False %}unused{% eof %}{% else %} \n inside{% endif %}",
                " \n inside",
            ),
            (
                (
                    "{% for item in items %}{% if item %}{{ item }}{% eof %}"
                    "{% endif %}{% endfor %} \n later"
                ),
                "12 \n later",
            ),
        ],
    )
    def test_only_immediate_text_is_stripped(self, source, expected):
        tmpl = Template("{% load whiteless %}" + source)
        for _ in range(2):
            assert (
                tmpl.render(Context({"value": " value ", "items": [1, 2]})) == expected
            )

    def test_repeated_render_with_different_contexts(self):
        tmpl = Template("{% load whiteless %}{% eof %} \n{{ value }} \n later")
        assert tmpl.render(Context({"value": " first "})) == " first  \n later"
        assert tmpl.render(Context({"value": " second "})) == " second  \n later"
