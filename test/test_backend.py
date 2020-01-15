# -*- coding: utf-8 -*-

import docutils.nodes
import docutils.utils
import pytest
import pybtex.plugin
import pybtex.database
from pybtex.richtext import HRef, Tag, Text

from pybtex_docutils import Backend
import six


def render_str(richtext):
    return "".join(str(node) for node in richtext.render(Backend()))


# may remove this test when new pybtex is out
def test_text():
    assert Backend().format_text('hi') == Backend().format_str('hi')


def test_tag():
    tag = Tag('em', 'hello')
    assert render_str(tag) == '<emphasis>hello</emphasis>'


def test_tag_text():
    tag = Tag('em', Text('hello', ' world'))
    assert render_str(tag) == '<emphasis>hello world</emphasis>'


def test_tag_strong():
    tag = Tag('strong', 'hello')
    assert render_str(tag) == '<strong>hello</strong>'


def test_tag_i():
    tag = Tag('i', 'hello')
    assert render_str(tag) == '<emphasis>hello</emphasis>'


def test_tag_b():
    tag = Tag('b', 'hello')
    assert render_str(tag) == '<strong>hello</strong>'


def test_tag_tt():
    tag = Tag('tt', 'hello')
    assert render_str(tag) == '<literal>hello</literal>'


def test_tag_unknown():
    tag = Tag('***unknown***', 'hello')
    assert render_str(tag) == 'hello'


def test_href():
    href = HRef('http://www.example.com', 'hyperlinked text')
    assert render_str(href) == (
        '<reference refuri="http://www.example.com">'
        'hyperlinked text'
        '</reference>')


def test_href_text():
    href = HRef('http://www.example.com', Text('hyperlinked', ' text'))
    assert render_str(href) == (
        '<reference refuri="http://www.example.com">'
        'hyperlinked text'
        '</reference>')


def test_render_sequence():
    text = Text('hello ', Tag('em', 'world'))
    assert render_str(text) == 'hello <emphasis>world</emphasis>'


@pytest.fixture
def entry():
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
    entries = list(style.format_entries(six.itervalues(data.entries)))
    return entries[0]


@pytest.fixture
def document():
    return docutils.utils.new_document('test.rst')


def test_citation(entry, document):
    node = Backend().citation(entry, document)
    assert six.text_type(node) == (
        u'<citation ids="hongquin1997" names="hongquin1997">'
        u'<label>hongquin1997</label>'
        u'<paragraph>'
        u'Hongquin Liu and Eli Ruckenstein. '
        u'Predicting the diffusion coefficient in supercritical fluids. '
        u'<emphasis>Ind. Eng. Chem. Res.</emphasis>, '
        u'36:888–895, 1997.'
        u'</paragraph>'
        u'</citation>')


def test_citation_reference(entry, document):
    node = Backend().citation_reference(entry, document)
    assert str(node) == (
        '<citation_reference ids="id1" refname="hongquin1997">'
        'hongquin1997'
        '</citation_reference>')


def test_citation_use_label(entry, document):
    node = Backend().citation(
        entry, document, use_key_as_label=False)
    assert six.text_type(node) == (
        u'<citation ids="hongquin1997" names="hongquin1997">'
        u'<label>1</label>'
        u'<paragraph>'
        u'Hongquin Liu and Eli Ruckenstein. '
        u'Predicting the diffusion coefficient in supercritical fluids. '
        u'<emphasis>Ind. Eng. Chem. Res.</emphasis>, '
        u'36:888–895, 1997.'
        u'</paragraph>'
        u'</citation>')


def test_citation_reference_use_label(entry, document):
    node = Backend().citation_reference(
        entry, document, use_key_as_label=False)
    assert str(node) == (
        '<citation_reference ids="id1" refname="hongquin1997">'
        '1'
        '</citation_reference>')


def test_footnote(entry, document):
    node = Backend().footnote(entry, document)
    assert six.text_type(node) == (
        u'<footnote auto="1" ids="hongquin1997" names="hongquin1997">'
        u'<paragraph>'
        u'Hongquin Liu and Eli Ruckenstein. '
        u'Predicting the diffusion coefficient in supercritical fluids. '
        u'<emphasis>Ind. Eng. Chem. Res.</emphasis>, '
        u'36:888–895, 1997.'
        u'</paragraph>'
        u'</footnote>')


def test_footnote_reference(entry, document):
    node = Backend().footnote_reference(entry, document)
    assert str(node) == (
        '<footnote_reference auto="1" ids="[\'id1\']" '
        'refname="hongquin1997"/>')


def test_write_entry():
    with pytest.raises(NotImplementedError):
        Backend().write_entry(None, None, None)
