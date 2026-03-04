import pytest

from code.calculator import add


def test_add_positive_numbers() -> None:
    assert add(2, 3) == 5


def test_add_negative_numbers() -> None:
    assert add(-2, -3) == -5


def test_add_mixed_numbers() -> None:
    assert add(-2, 5) == 3


def test_add_floats() -> None:
    assert add(2.5, 3.5) == 6.0
