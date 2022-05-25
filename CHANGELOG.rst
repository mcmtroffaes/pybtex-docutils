1.0.2 (in development)
----------------------

* New ``simplebibliography``
  directive, which will generate a citation for every entry in the specified
  bib files, intended for simple single document workflows that do not require
  the full power of Sphinx.

* Fix deprecation warning with docutils 0.18 (see issue #21, reported by
  drammock).

1.0.1 (29 July 2021)
--------------------

* Add py.typed so mypy finds the type annotations.

* Switch to github actions for regression testing.

1.0.0 (15 January 2021)
-----------------------

* Drop Python 2.7, 3.4, and 3.5 support.

* Add type annotations.

* Add support for sub and sup tags.

0.2.2 (9 October 2019)
----------------------

* Drop Python 3.3 support.

* New footnote and footnote_reference methods for docutils footnote
  support.

0.2.1 (8 December 2014)
-----------------------

* Add Python 3.4 support, drop Python 3.2 support.

* Support more tags, also fail gracefully on unknown tags (see issue
  #6, reported by Jellby).

* Use universal wheel for distribution.

0.2.0 (8 August 2013)
---------------------

* **BACKWARD INCOMPATIBLE**
  The backend now renders into a
  list of docutils nodes instead of a single docutils node.

* New :meth:`~pybtex_docutils.Backend.paragraph` method
  to render an entry into a single
  docutils paragraph.

* The ``<inline>`` wrapper nodes are no more, leading to much simpler
  generated code.

* Full test coverage.

* Generated citation nodes now contain text inside a paragraph.

* Minimal example.

0.1.0 (7 August 2013)
---------------------

* Copied the backend from pybtex.

* Initial documentation.

* Initial tests and travis.ci integration.
