pybtex-docutils
===============

|imagegithub| |imagecodecov|

Overview
--------

A docutils backend for pybtex.

* Download: https://pypi.org/project/pybtex-docutils/#files

* Documentation: https://pybtex-docutils.readthedocs.io/

* Development: http://github.com/mcmtroffaes/pybtex-docutils/

.. |imagegithub| image:: https://github.com/mcmtroffaes/pybtex-docutils/actions/workflows/python-package.yml/badge.svg
    :target: https://github.com/mcmtroffaes/pybtex-docutils/actions/workflows/python-package.yml
    :alt: github-ci

.. |imagecodecov| image:: https://codecov.io/gh/mcmtroffaes/pybtex-docutils/branch/develop/graph/badge.svg
    :target: https://codecov.io/gh/mcmtroffaes/pybtex-docutils
    :alt: codecov

Installation
------------

For use with Sphinx, simply install
`sphinxcontrib-bibtex <https://sphinxcontrib-bibtex.readthedocs.io/>`_.

For use with pure docutils,
install the module with ``pip install pybtex_docutils``, or from
source using ``pip install -e .``.

Minimal Example
---------------

For use with Sphinx, refer to the
`sphinxcontrib-bibtex <https://sphinxcontrib-bibtex.readthedocs.io/>`_
documentation.

For use with pure docutils, the module exposes a new ``simplebibliography``
directive, which will generate a citation for every entry in the specified
bib files.
This new directive is only intended
for simple single document workflows
that do not require the full power of Sphinx.
You need exactly one of these directives in your document,
placed at the location where you want the citations to appear
(typically, at the end).

For example:

.. code-block:: rest

   See  [Nelson1987]_ for an introduction to non-standard analysis.

   .. simplebibliography:: refs.bib

where ``refs.bib`` might contain:

.. code-block::

   @Book{Nelson1987,
     author = {Edward Nelson},
     title = {Radically Elementary Probability Theory},
     publisher = {Princeton University Press},
     year = {1987}
   }

Note that citation keys are used as labels. For this to work, it is thus
necessary that all keys in your bib file are valid citation labels for
docutils. In particular, they cannot contain colons.
This limitation is lifted in ``sphinxcontrib-bibtex``,
which also provides many more citation features.

To use the directive, you have to write your own command script
(there seems to be no other way currently to extend docutils). For instance:

.. code-block:: python

   #!/usr/bin/env python3
   from docutils.parsers.rst import directives, Directive
   from docutils.core import publish_cmdline, default_description

   from pybtex_docutils import SimpleBibliography

   description = ('Like rst2html5.py, but with .. simplebibliography support'
                  + default_description)

   if __name__ == '__main__':
       directives.register_directive("simplebibliography", SimpleBibliography)
       publish_cmdline(writer_name='html5', description=description)

You can then run this command as if you would run ``rst2html5``.
