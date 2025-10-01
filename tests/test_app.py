import pytest
from src.app import add, divide


def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Tidak boleh bagi nol"):
        divide(10, 0)
