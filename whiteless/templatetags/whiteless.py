from __future__ import annotations

import re
from collections.abc import Callable

from django import template
from django.template import Context, Node
from django.template.base import NodeList, Parser, Token, TokenType
from django.template.defaulttags import CommentNode

register = template.Library()


def leading(value: str) -> str:
    """Remove leading whitespace."""
    return value.lstrip()


def remove_all(value: str) -> str:
    """Remove all whitespace."""
    return re.sub(r"\s+", "", value)


def space(value: str) -> str:
    """Collapse whitespace to single spaces; return empty for whitespace-only input."""
    output = re.sub(r"\s+", " ", value)
    if output == " ":
        return ""
    return output


def strip(value: str) -> str:
    """Remove leading and trailing whitespace."""
    return value.strip()


def trailing(value: str) -> str:
    """Remove trailing whitespace."""
    return value.rstrip()


_Transformer = Callable[[str], str]

_TRANSFORMERS: dict[str, _Transformer] = {
    "all": remove_all,
    "space": space,
    "strip": strip,
    "leading": leading,
    "trailing": trailing,
}


@register.tag
def whiteless(parser: Parser, token: Token) -> WhitelessNode:
    """Compile a block that transforms rendered whitespace.

    Options are applied in order:
    - all: remove all whitespace (the default).
    - space: collapse whitespace to single spaces.
    - leading: remove whitespace at the start of the rendered block.
    - trailing: remove whitespace at the end of the rendered block.
    - strip: remove whitespace at both ends.
    """
    args = token.split_contents()[1:]

    # default is to remove all whitespaces
    # otherwise collect transformers
    transformers: tuple[_Transformer, ...]
    if not args:
        transformers = (remove_all,)
    else:
        transformers = tuple(_TRANSFORMERS[arg] for arg in args if arg in _TRANSFORMERS)

    # parse up to endwhiteless and remove it
    nodelist = parser.parse(("endwhiteless",))
    parser.delete_first_token()
    return WhitelessNode(nodelist, transformers)


class WhitelessNode(Node):
    def __init__(
        self, nodelist: NodeList, transformers: tuple[_Transformer, ...]
    ) -> None:
        """Store the block and its ordered whitespace transformations."""
        self.nodelist = nodelist
        self.transformers = transformers

    def render(self, context: Context) -> str:
        """Render the block and apply its whitespace transformations."""
        value = self.nodelist.render(context)
        for transformer in self.transformers:
            value = transformer(value)
        return value


@register.tag
def eof(parser: Parser, _token: Token) -> EofNode:
    """Remove leading whitespace from the immediately following text token."""
    # remove leading whitespaces only from the immediately subsequent text token
    if parser.tokens:
        token = parser.next_token()
        if token.token_type == TokenType.TEXT:
            token.contents = token.contents.lstrip()
        parser.prepend_token(token)
    return EofNode()


class EofNode(CommentNode):
    """Render nothing after the following text token has been trimmed."""
