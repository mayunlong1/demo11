import pytest


@pytest.mark.parametrize('a, b', [
    [[1, 2, 3], [4, 5, 6]],
    [[3, 2, 1], [6, 5, 4]]
])
def test_demo(a, b):
    assert 1 in a
