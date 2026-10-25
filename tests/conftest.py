import pytest


@pytest.fixture(
    params=list(
        " \t\n\r\v\f\x1c\x1d\x1e\x1f\x85\xa0\u1680"
        "\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a"
        "\u2028\u2029\u202f\u205f\u3000"
    )
    + [" \n\f\t", "\r\n\xa0\u2003", "\x1c\x85\u2028\u3000"]
)
def whitespace(request):
    return request.param
