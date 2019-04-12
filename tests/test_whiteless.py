import re

from hypothesis import assume, example

from tests.utils import (
    given_double_whitespaces,
    given_leading_double_whitespaces,
    given_leading_trailing_whitespaces,
    given_leading_whitespaces,
    given_no_whitespace,
    given_only_whitespaces,
    given_some_whitespace,
    given_trailing_whitespaces,
)
from whiteless.templatetags.whiteless import leading, remove_all, space, strip, trailing


class TestRemoveAll(object):
    def test_empty_string(self):
        output = remove_all("")
        assert output == ""

    @given_some_whitespace
    @example("\n foo\tbar  \r  \tx\t")
    def test_whitespaces(self, value):
        output = remove_all(value)
        assert not re.search(r"\s", output)
        assert output == re.sub(r"\s+", "", value)

    @given_no_whitespace
    @example("foobar")
    def test_no_whitespaces(self, value):
        output = remove_all(value)
        assert output == value

    @given_only_whitespaces
    @example(" \n\f\t")
    def test_only_whitespaces(self, value):
        output = remove_all(value)
        assert output == ""


class TestSpace(object):
    def test_empty_string(self):
        output = space("")
        assert output == "", output

    @given_no_whitespace
    @example("foobar")
    def test_no_whitespaces(self, value):
        output = space(value)
        assert output == value, output

    @given_only_whitespaces
    @example(" \n\f\t")
    def test_only_whitespaces(self, value):
        output = space(value)
        assert output == "", output

    @given_double_whitespaces
    @example("\n foo\tbar  \r  \tx\t")
    def test_double_whitespaces(self, value):
        output = space(value)
        assert not re.search(r"\s\s", output)
        assert not re.search(r"[^\S ]", output)

    @given_leading_double_whitespaces
    @example("\ffoo bar baz")
    def test_leading_whitespaces(self, value):
        assume(re.search(r"\S", value))
        output = space(value)
        assert output[0] == " "

    @given_trailing_whitespaces
    @example("foo bar baz\t")
    def test_trailing_whitespaces(self, value):
        assume(re.search(r"\S", value))
        output = space(value)
        assert output[-1] == " "


class TestStrip(object):
    def test_empty_string(self):
        output = strip("")
        assert output == ""

    @given_no_whitespace
    @example("foobar")
    def test_no_whitespaces(self, value):
        output = strip(value)
        assert output == value

    @given_only_whitespaces
    @example(" \n\f\t")
    def test_only_whitespaces(self, value):
        output = strip(value)
        assert output == ""

    @given_leading_whitespaces
    @example("\n\tfoobar")
    def test_leading_whitespaces(self, value):
        output = strip(value)
        assert not re.search(r"^\s", output)

    @given_trailing_whitespaces
    @example("foobar\t\n")
    def test_trailing_whitespaces(self, value):
        output = strip(value)
        assert not re.search(r"\s$", output)

    @given_leading_trailing_whitespaces
    @example("\n\tfoobar\t\n")
    def test_leading_trailing_whitespaces(self, value):
        output = strip(value)
        assert not re.search(r"^\s", output)
        assert not re.search(r"\s$", output)


class TestLeading(object):
    def test_empty_string(self):
        output = leading("")
        assert output == ""

    @given_no_whitespace
    @example("foobar")
    def test_no_whitespaces(self, value):
        output = leading(value)
        assert output == value

    @given_only_whitespaces
    @example(" \n\f\t")
    def test_only_whitespaces(self, value):
        output = leading(value)
        assert output == ""

    @given_leading_whitespaces
    @example("\n\tfoobar")
    def test_leading_whitespaces(self, value):
        output = leading(value)
        assert not re.search(r"^\s", output)

    @given_trailing_whitespaces
    @example("foobar\t\n")
    def test_trailing_whitespaces(self, value):
        output = leading(value)
        assert not re.search(r"^\s", output)
        assert re.search(r"\s$", output)

    @given_leading_trailing_whitespaces
    @example("\n\tfoobar\t\n")
    def test_leading_trailing_whitespaces(self, value):
        output = leading(value)
        assert not re.search(r"^\s", output)
        assert re.search(r"\s$", output)


class TestTrailing(object):
    def test_empty_string(self):
        output = trailing("")
        assert output == ""

    @given_no_whitespace
    @example("foobar")
    def test_no_whitespaces(self, value):
        output = trailing(value)
        assert output == value

    @given_only_whitespaces
    @example(" \n\f\t")
    def test_only_whitespaces(self, value):
        output = trailing(value)
        assert output == ""

    @given_leading_whitespaces
    @example("\n\tfoobar")
    def test_leading_whitespaces(self, value):
        output = trailing(value)
        assert not re.search(r"\s$", output)
        assert re.search(r"^\s", output)

    @given_trailing_whitespaces
    @example("foobar\t\n")
    def test_trailing_whitespaces(self, value):
        output = trailing(value)
        assert not re.search(r"\s$", output)

    @given_leading_trailing_whitespaces
    @example("\n\tfoobar\t\n")
    def test_leading_trailing_whitespaces(self, value):
        output = trailing(value)
        assert not re.search(r"\s$", output)
        assert re.search(r"^\s", output)
