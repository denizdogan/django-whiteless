import re

from django import template
from django.template import Node
from django.template.defaulttags import CommentNode

try:  # django >= 2.0
    from django.template.base import TokenType

    TOKEN_TEXT = TokenType.TEXT
except ImportError:  # django <= 1.11
    from django.template.base import TOKEN_TEXT

register = template.Library()


def leading(value):
    """
    Strip all leading whitespaces.
    :param value: The value
    :type value: str
    :return: The value with all leading whitespaces removed
    :rtype: str
    """
    return value.lstrip()


def remove_all(value):
    """
    Remove all whitespaces from a string.
    :param value: The value
    :type value: str
    :return: The value with all whitespaces removed
    :rtype: str
    """
    return re.sub(r"\s+", "", value)


def space(value):
    """
    Replace all whitespaces by a single space.
    :param value: The value
    :type value: str
    :return: The value with all whitespaces replaced by a single space
    :rtype: str
    """
    output = re.sub(r"\s+", " ", value)
    if output == " ":
        return ""
    return output


def strip(value):
    """
    Strip all leading and trailing whitespaces.
    :param value: The value
    :type value: str
    :return: The value with all leading and trailing whitespaces removed
    :rtype: str
    """
    return value.strip()


def trailing(value):
    """
    Strip all trailing whitespaces.
    :param value: The value
    :type value: str
    :return: The value with all trailing whitespaces removed
    :rtype: str
    """
    return value.rstrip()


_TRANSFORMERS = {
    "all": remove_all,
    "space": space,
    "strip": strip,
    "leading": leading,
    "trailing": trailing,
}


@register.tag
def whiteless(parser, token):
    """
    Remove whitespaces in various ways depending on the arguments.

    ``all`` (default)
        Removes all whitespaces in the block

    ``space``
        Replaces all whitespaces in the block with a single space

    ``leading``
        Removes all whitespaces immediately following ``{% whiteless %}``

    ``trailing``
        Removes all whitespaces immediately preceding ``{% endwhiteless %}``

    :param parser: Template parser object
    :type parser: django.template.base.Parser
    :param token: Template token object
    :type token: django.template.base.Token
    :return: WhitelessNode object
    :rtype: WhitelessNode
    """
    args = token.split_contents()[1:]

    # default is to remove all whitespaces
    # otherwise collect transformers
    if not len(args):
        transformers = (remove_all,)
    else:
        transformers = (_TRANSFORMERS.get(t) for t in args)
        transformers = list(filter(None, transformers))  # remove not found

    # parse up to endwhiteless and remove it
    nodelist = parser.parse(("endwhiteless",))
    parser.delete_first_token()
    return WhitelessNode(nodelist, transformers)


class WhitelessNode(Node):
    def __init__(self, nodelist, transformers):
        """
        Constructor.
        :param nodelist: List of nodes in the block
        :type nodelist: django.template.base.NodeList
        :param transformers: List of transformers to apply to the content
        :type transformers: callable
        """
        self.nodelist = nodelist
        self.transformers = transformers

    def render(self, context):
        """
        Render the node.
        :param context: Template context
        :type context: django.template.context.Context
        :return: Output
        :rtype: str
        """
        value = self.nodelist.render(context)
        for transformer in self.transformers:
            value = transformer(value)
        return value


@register.tag
def eof(parser, _token):
    """
    Remove the immediately subsequent newlines.
    :param parser: Template parser
    :type parser: django.template.base.Parser
    :param _token: Current token
    :type _token: django.template.base.Token
    :return: EofNode object
    :rtype: EofNode
    """
    # remove the leading whitespaces of the immediately subsequent tokens
    while len(parser.tokens) and parser.tokens[0].token_type == TOKEN_TEXT:
        contents = parser.tokens[0].contents  # type: str
        stripped = contents.lstrip()
        if contents == stripped:
            break
        parser.tokens[0].contents = stripped
    return EofNode()


class EofNode(CommentNode):
    """
    Equal to a comment in spirit.
    """

    pass
