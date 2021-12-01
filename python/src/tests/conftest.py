import pytest

@pytest.fixture
def build_list():
    return list(range(10))
