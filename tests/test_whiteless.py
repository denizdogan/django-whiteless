import pytest
from django.template import Context, Template

from whiteless.templatetags.whiteless import leading, remove_all, space, strip, trailing


@pytest.mark.parametrize("transform", [remove_all, space, strip, leading, trailing])
@pytest.mark.parametrize(
    "value", ["", "foobar", "café東京🙂", "\u200b", "\ufeff", "\u200bcafé\ufeff"]
)
def test_transformers_preserve_non_whitespace(transform, value):
    assert transform(value) == value


@pytest.mark.parametrize("transform", [remove_all, space, strip, leading, trailing])
def test_transformers_remove_whitespace_only(transform, whitespace):
    assert transform(whitespace) == ""


def test_transformers_wrapped_content(whitespace):
    value = whitespace + "café" + whitespace + "東京" + whitespace
    assert remove_all(value) == "café東京"
    assert space(value) == " café 東京 "
    assert strip(value) == "café" + whitespace + "東京"
    assert leading(value) == "café" + whitespace + "東京" + whitespace
    assert trailing(value) == whitespace + "café" + whitespace + "東京"


def test_transformers_internal_whitespace(whitespace):
    value = "a" + whitespace + "b"
    assert remove_all(value) == "ab"
    assert space(value) == "a b"
    assert strip(value) == value
    assert leading(value) == value
    assert trailing(value) == value


@pytest.mark.parametrize(
    ("value", "removed", "spaced", "stripped", "led", "trailed"),
    [
        ("\n\tfoo", "foo", " foo", "foo", "foo", "\n\tfoo"),
        ("foo\t\n", "foo", "foo ", "foo", "foo\t\n", "foo"),
        (
            " \u200b\t\ufeff\n",
            "\u200b\ufeff",
            " \u200b \ufeff ",
            "\u200b\t\ufeff",
            "\u200b\t\ufeff\n",
            " \u200b\t\ufeff",
        ),
    ],
)
def test_transformers_edges(value, removed, spaced, stripped, led, trailed):
    assert remove_all(value) == removed
    assert space(value) == spaced
    assert strip(value) == stripped
    assert leading(value) == led
    assert trailing(value) == trailed


class TestWhiteless:
    @pytest.mark.parametrize(
        ("options", "expected"),
        [
            ("", "ab"),
            ("all", "ab"),
            ("space", " a b "),
            ("strip", "a \t b"),
            ("leading", "a \t b \n"),
            ("trailing", "\n a \t b"),
            ("space strip", "a b"),
            ("leading trailing space", "a b"),
        ],
    )
    def test_options(self, options, expected):
        tmpl = Template(
            "{% load whiteless %}{% whiteless " + options + " %}"
            "\n a \t b \n{% endwhiteless %}"
        )
        assert tmpl.render(Context()) == expected

    @pytest.mark.parametrize(
        ("options", "expected"),
        [
            ("unknown", "\n a \t b \n"),
            ("strip unknown", "a \t b"),
            ("unknown all", "ab"),
            ('"strip"', "\n a \t b \n"),
            ("strip=True", "\n a \t b \n"),
            ("123", "\n a \t b \n"),
            ("space unknown strip", "a b"),
        ],
    )
    def test_unknown_options_are_ignored(self, options, expected):
        tmpl = Template(
            "{% load whiteless %}{% whiteless " + options + " %}"
            "\n a \t b \n{% endwhiteless %}"
        )
        for _ in range(2):
            assert tmpl.render(Context()) == expected

    def test_transformers_preserve_order_and_are_reusable(self):
        tmpl = Template(
            "{% load whiteless %}{% whiteless space leading trailing space %}"
            "{{ value }}{% endwhiteless %}"
        )
        assert tmpl.nodelist[-1].transformers == (space, leading, trailing, space)
        for value, expected in [
            ("  first \n value  ", "first value"),
            ("\t second   value \n", "second value"),
        ]:
            assert tmpl.render(Context({"value": value})) == expected

    def test_transformers_are_reused_in_loops(self):
        tmpl = Template(
            "{% load whiteless %}{% for value in values %}"
            "{% whiteless space strip %}{{ value }}{% endwhiteless %}"
            "{% endfor %}"
        )
        assert tmpl.render(Context({"values": [" a  b ", " c  d "]})) == "a bc d"

    def test_nested_blocks(self):
        tmpl = Template(
            "{% load whiteless %}{% whiteless space %}\n outer "
            "{% whiteless all %} inner words {% endwhiteless %} end \n"
            "{% endwhiteless %}"
        )
        assert tmpl.render(Context()) == " outer innerwords end "

    @pytest.mark.parametrize(
        ("autoescape", "expected"),
        [("on", "&lt;b&gt;x&lt;/b&gt;"), ("off", "<b>x</b>")],
    )
    def test_autoescape(self, autoescape, expected):
        tmpl = Template(
            "{% load whiteless %}{% autoescape " + autoescape + " %}"
            "{% whiteless %}{{ value }}{% endwhiteless %}{% endautoescape %}"
        )
        assert tmpl.render(Context({"value": "<b> x </b>"})) == expected
