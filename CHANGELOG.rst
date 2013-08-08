0.2.0 (in development)
----------------------

* Backward incompatible API change: the backend now renders into a
  list of docutils nodes instead of a single docutils node.

* New :meth:`Backend.paragraph` method to render an entry into a single
  docutils paragraph.

* The <inline> wrapper nodes are no more, leading to much simpler
  generated code.

* Full test coverage.

* Generated citation nodes now contain text inside a paragraph.

0.1.0 (7 August 2013)
---------------------

* Copied the backend from pybtex.

* Initial documentation.

* Initial tests and travis.ci integration.
