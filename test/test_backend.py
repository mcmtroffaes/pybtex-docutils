import nose.tools
from pybtex.richtext import HRef, Tag, Text

from pybtex_docutils import Backend


def render_str(richtext):
    return "".join(str(node) for node in richtext.render(Backend()))


def test_tag():
    tag = Tag('emph', 'hello')
    nose.tools.assert_equal(render_str(tag), '<emphasis>hello</emphasis>')


def test_tag_text():
    tag = Tag('emph', Text('hello', ' world'))
    nose.tools.assert_equal(
        render_str(tag), '<emphasis>hello world</emphasis>')


def test_href():
    href = HRef('http://www.example.com', 'hyperlinked text')
    nose.tools.assert_equal(
        render_str(href),
        '<reference refuri="http://www.example.com">'
        'hyperlinked text'
        '</reference>')


def test_href_text():
    href = HRef('http://www.example.com', Text('hyperlinked', ' text'))
    nose.tools.assert_equal(
        render_str(href),
        '<reference refuri="http://www.example.com">'
        'hyperlinked text'
        '</reference>')

def test_render_sequence():
    text = Text('hello ', Tag('emph', 'world'))
    nose.tools.assert_equal(
        render_str(text),
        'hello <emphasis>world</emphasis>')
