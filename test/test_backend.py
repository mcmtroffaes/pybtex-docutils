import nose.tools
from pybtex_docutils import Backend


def test_href():
    from pybtex.richtext import HRef
    href = HRef('http://www.example.com', 'hyperlinked text')
    nose.tools.assert_equal(
        str(href.render(Backend())),
        '<reference refuri="http://www.example.com">'
        '<inline>hyperlinked text</inline>'
        '</reference>')
