from django.template import Context, Template
from hypothesis import example

from tests.utils import given_only_whitespaces


class TestEof(object):
    @given_only_whitespaces
    @example("\n\t\f")
    def test_trailing_whitespaces(self, s):
        tmpl = Template("{% load whiteless %}{% eof %}" + s)
        out = tmpl.render(Context())
        assert out == ""

    @given_only_whitespaces
    def test_leading_whitespaces(self, s):
        tmpl = Template("{% load whiteless %}" + s + "{% eof %}")
        out = tmpl.render(Context())
        assert out == s
