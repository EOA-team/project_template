"""Unit tests for the calculator module."""

from src.calculator import add


def test_add_positive_numbers() -> None:
    """Test adding two positive numbers."""
    assert add(2, 3) == 5


def test_add_negative_numbers() -> None:
    """Test adding two negative numbers."""
    assert add(-2, -3) == -5


def test_add_mixed_numbers() -> None:
    """Test adding a positive and a negative number."""
    assert add(-2, 5) == 3


def test_add_floats() -> None:
    """Test adding two floating-point numbers."""
    assert add(2.5, 3.5) == 6.0
