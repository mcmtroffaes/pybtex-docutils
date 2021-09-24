import os.path
import re
from docutils.core import publish_file
from docutils.parsers.rst import directives

from pybtex_docutils import SimpleBibliography


def html_citation_ref(key):
    return re.compile(
        fr'<a class="citation-reference" '
        fr'href="#{key.lower()}" id="\w+">'
        fr'\[{key}]'
        fr'</a>')


def html_citation(key):
    return re.compile(
        fr'<dt class="label" id="{key.lower()}">'
        fr'<span class="brackets">'
        fr'(?:<a class="fn-backref" href="#\w+">)?'
        fr'{key}'
        fr'(?:</a>)?'
        fr'</span>'
        fr'(?:<span class="fn-backref">\('
        fr'<a href="#\w+">1</a>'
        fr',<a href="#\w+">2</a>'
        fr'(,<a href="#\w+">3</a>)?'
        fr'(,<a href="#\w+">\d+</a>)*'
        fr'\)</span>)?'
        fr'</dt>\n')


def test_simplebibliography():
    directives.register_directive("bibliography", SimpleBibliography)
    source_path = os.path.join(
        os.path.dirname(__file__),
        "roots", "test_simplebibliography", "index.rst")
    result = publish_file(source_path=source_path, writer_name="html5")
    assert re.search(html_citation_ref('Mandel2009'), result) is not None
    assert re.search(html_citation_ref('Evensen2003'), result) is not None
    assert re.search(html_citation_ref('Lorenc1986'), result) is None
    assert re.search(html_citation('Mandel2009'), result) is not None
    assert re.search(html_citation('Evensen2003'), result) is not None
    assert re.search(html_citation('Lorenc1986'), result) is not None
