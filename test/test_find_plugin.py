# note: tests require pybtex-docutils to be installed
# so its entry points can be found

import pybtex_docutils

def test_pkg_resources_entry_point():
    from pkg_resources import iter_entry_points
    for ep in iter_entry_points("pybtex.backends", "docutils"):
        assert ep.load() is pybtex_docutils.Backend

def test_pybtex_find_plugin():
    from pybtex.plugin import find_plugin
    assert find_plugin("pybtex.backends", "docutils") is pybtex_docutils.Backend

    
