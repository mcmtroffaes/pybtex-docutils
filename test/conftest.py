from pathlib import Path

import pytest

collect_ignore = ["roots"]


@pytest.fixture
def test_roots() -> Path:
    return Path(__file__).parent.absolute() / "roots"
