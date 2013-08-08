import docutils.nodes
import docutils.utils
import nose.tools
import pybtex.plugin
import pybtex.database
from pybtex.richtext import HRef, Tag, Text
from unittest import TestCase

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


class TestCitation(TestCase):

    def setUp(self):
        data = pybtex.database.BibliographyData({
            'hongquin1997': pybtex.database.Entry(
                'article',
                fields={
                    'language': u'english',
                    'title': u'Predicting the Diffusion Coefficient in Supercritical Fluids',
                    'journal': u'Ind. Eng. Chem. Res.',
                    'volume': u'36',
                    'year': u'1997',
                    'pages': u'888-895',
                },
                persons={'author': [
                    pybtex.database.Person(u'Liu, Hongquin'),
                    pybtex.database.Person(u'Ruckenstein, Eli')]},
                )})
        style = pybtex.plugin.find_plugin('pybtex.style.formatting', 'plain')()
        self.backend = Backend()
        entries = list(style.format_entries(data.entries.itervalues()))
        self.entry = entries[0]
        self.document = docutils.utils.new_document('test.rst')

    def test_citation(self):
        node = self.backend.citation(self.entry, self.document)
        nose.tools.assert_equal(
            str(node),
            '<citation ids="hongquin1997" names="hongquin1997">'
            '<label>hongquin1997</label>'
            'Hongquin Liu and Eli Ruckenstein. '
            'Predicting the diffusion coefficient in supercritical fluids. '
            '<emphasis>Ind. Eng. Chem. Res.</emphasis>, '
            '36:888\\u2013895, 1997.'
            '</citation>')

    def test_citation_reference(self):
        node = self.backend.citation_reference(self.entry, self.document)
        nose.tools.assert_equal(
            str(node),
            '<citation_reference ids="id1" refname="hongquin1997">'
            'hongquin1997'
            '</citation_reference>')

    def tearDown(self):
        del self.backend
        del self.entry
        del self.document

