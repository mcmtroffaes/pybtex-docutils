import re

import docutils
import docutils.parsers.rst.directives as directives
from docutils.core import publish_file

from pybtex_docutils import SimpleBibliography


def html_citation_ref(key):
    if docutils.__version_info__ < (0, 18):
        return re.compile(
            rf'<a class="citation-reference" '
            rf'href="#{key.lower()}" id="\w+">'
            rf"\[{key}]"
            rf"</a>"
        )
    else:
        return re.compile(
            rf'<a class="citation-reference" '
            rf'href="#{key.lower()}" id="[a-zA-Z0-9_-]+" '
            rf'role="doc-biblioref">'
            rf"\[{key}]"
            rf"</a>"
        )


def html_citation(key):
    if docutils.__version_info__ < (0, 18):
        return re.compile(
            rf'<dt class="label" id="{key.lower()}">'
            rf'<span class="brackets">'
            rf'(?:<a class="fn-backref" href="#\w+">)?'
            rf"{key}"
            rf"(?:</a>)?"
            rf"</span>"
            rf'(?:<span class="fn-backref">\('
            rf'<a href="#\w+">1</a>'
            rf',<a href="#\w+">2</a>'
            rf'(,<a href="#\w+">3</a>)?'
            rf'(,<a href="#\w+">\d+</a>)*'
            rf"\)</span>)?"
            rf"</dt>\n"
        )
    else:
        return re.compile(
            rf'<div class="citation" id="{key.lower()}" '
            rf'role="doc-biblioentry">\s*'
            rf'<span class="label">'
            rf'<span class="fn-bracket">\[</span>'
            rf'(?:<a role="doc-backlink" href="#[a-zA-Z0-9_-]+">)?'
            rf"{key}"
            rf"(?:</a>)?"
            rf'<span class="fn-bracket">]</span>'
            rf"</span>"
        )


def test_simplebibliography(test_roots):
    directives.register_directive("bibliography", SimpleBibliography)
    source_path = test_roots / "test_simplebibliography" / "index.rst"
    result = publish_file(source_path=str(source_path), writer_name="html5")
    assert re.search(html_citation_ref("Mandel2009"), result) is not None
    assert re.search(html_citation_ref("Evensen2003"), result) is not None
    assert re.search(html_citation_ref("Lorenc1986"), result) is None
    assert re.search(html_citation("Mandel2009"), result) is not None
    assert re.search(html_citation("Evensen2003"), result) is not None
    assert re.search(html_citation("Lorenc1986"), result) is not None
