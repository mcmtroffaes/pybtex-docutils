import docutils.nodes
import docutils.utils
import nose.tools
import pybtex.plugin
from pybtex.database import BibliographyData, Entry, Person
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


def test_citation():
    data = BibliographyData({
        'hongquin1997': Entry(
            'article',
            fields={
                'language': u'english',
                'title': u'Predicting the Diffusion Coefficient in Supercritical Fluids',
                'journal': u'Ind. Eng. Chem. Res.',
                'volume': u'36',
                'year': u'1997',
                'pages': u'888-895',
            },
            persons={'author': [Person(u'Liu, Hongquin'),
                                Person(u'Ruckenstein, Eli')]},
            )})
    style = pybtex.plugin.find_plugin('pybtex.style.formatting', 'plain')()
    backend = Backend()
    entries = list(style.format_entries(data.entries.itervalues()))
    entry = entries[0]
    document = docutils.utils.new_document('test.rst')
    node = backend.citation(entry, document)
    nose.tools.assert_equal(
        str(node),
        '<citation ids="hongquin1997" names="hongquin1997">'
        '<label>hongquin1997</label>'
        'Hongquin Liu and Eli Ruckenstein. '
        'Predicting the diffusion coefficient in supercritical fluids. '
        '<emphasis>Ind. Eng. Chem. Res.</emphasis>, '
        '36:888\\u2013895, 1997.'
        '</citation>')
