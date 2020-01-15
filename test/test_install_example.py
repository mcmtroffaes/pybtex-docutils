# -*- coding: utf-8 -*-

expected_result = (
    u'<paragraph>D.\xa0Lindley. <emphasis>Making Decisions</emphasis>. '
    u'Wiley, 2nd edition, 1985.</paragraph>'
    )


def test_install_example():
    result = []

    # example begin
    import six
    import pybtex.database.input.bibtex
    import pybtex.plugin

    style = pybtex.plugin.find_plugin('pybtex.style.formatting', 'plain')()
    backend = pybtex.plugin.find_plugin('pybtex.backends', 'docutils')()
    parser = pybtex.database.input.bibtex.Parser()
    data = parser.parse_stream(six.StringIO(u"""
    @Book{1985:lindley,
      author =    {D. Lindley},
      title =     {Making Decisions},
      publisher = {Wiley},
      year =      {1985},
      edition =   {2nd},
    }
    """))
    for entry in style.format_entries(six.itervalues(data.entries)):
        print(backend.paragraph(entry))
    # example end
        result.append(backend.paragraph(entry))

    assert len(result) == 1
    assert six.text_type(result[0]) == expected_result
