from hypothesis import given, strategies as st

given_double_whitespaces = given(st.from_regex(r"\s\s"))
given_leading_double_whitespaces = given(st.from_regex(r"^\s\s"))
given_leading_trailing_whitespaces = given(st.from_regex(r"^\s\S+\s$"))
given_leading_whitespaces = given(st.from_regex(r"^\s+\S+"))
given_no_whitespace = given(st.from_regex(r"^\S+$", fullmatch=True))
given_only_whitespaces = given(st.from_regex(r"^\s+$", fullmatch=True))
given_some_whitespace = given(st.from_regex(r"\s"))
given_trailing_whitespaces = given(st.from_regex(r"\S+\s+$"))
