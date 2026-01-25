# note: tests require pybtex-docutils to be installed
# so its entry points can be found

from importlib.metadata import entry_points

import pytest

import pybtex_docutils


@pytest.mark.plugin
def test_importlib_metadata_entry_point():
    for ep in entry_points(group="pybtex.backends", name="docutils"):
        assert ep.load() is pybtex_docutils.Backend


@pytest.mark.plugin
def test_pybtex_find_plugin():
    from pybtex.plugin import find_plugin

    assert find_plugin("pybtex.backends", "docutils") is pybtex_docutils.Backend
