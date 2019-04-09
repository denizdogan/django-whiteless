from django.template import Context, Template
from hypothesis import example

from tests.utils import given_only_whitespaces


class TestEof(object):
    @given_only_whitespaces
    @example("\n\t\f")
    def test_trailing_whitespaces(self, s):
        c = Context()
        assert "" == Template("{% load whiteless %}{% eof %}" + s).render(c)

    @given_only_whitespaces
    def test_leading_whitespaces(self, s):
        c = Context()
        assert s == Template("{% load whiteless %}" + s + "{% eof %}").render(c)
