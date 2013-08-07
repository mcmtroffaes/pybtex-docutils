import nose.tools
from pybtex.richtext import HRef, Tag, Text

from pybtex_docutils import Backend


def test_tag():
    tag = Tag('emph', 'hello')
    nose.tools.assert_equal(
        str(tag.render(Backend())),
        '<emphasis><inline>hello</inline></emphasis>')


def test_tag_text():
    tag = Tag('emph', Text('hello', ' world'))
    nose.tools.assert_equal(
        str(tag.render(Backend())),
        '<emphasis><inline>'
        '<inline>hello</inline><inline> world</inline>'
        '</inline></emphasis>')


def test_href():
    href = HRef('http://www.example.com', 'hyperlinked text')
    nose.tools.assert_equal(
        str(href.render(Backend())),
        '<reference refuri="http://www.example.com">'
        '<inline>hyperlinked text</inline>'
        '</reference>')


def test_href_text():
    href = HRef('http://www.example.com', Text('hyperlinked', ' text'))
    nose.tools.assert_equal(
        str(href.render(Backend())),
        '<reference refuri="http://www.example.com">'
        '<inline>'
        '<inline>hyperlinked</inline><inline> text</inline>'
        '</inline>'
        '</reference>')
