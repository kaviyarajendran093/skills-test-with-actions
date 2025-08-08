import math
import pytest
from calculations import area_of_circle, get_nth_fibonacci


# ----- Tests for area_of_circle -----

def test_area_of_circle_negative():
    """Negative radius should raise ValueError."""
    with pytest.raises(ValueError):
        area_of_circle(-1)


def test_area_of_circle_zero():
    """Radius 0 should return 0."""
    assert area_of_circle(0) == 0


def test_area_of_circle_positive():
    """Positive radius should return correct area."""
    assert math.isclose(area_of_circle(2), math.pi * 4)


# ----- Tests for get_nth_fibonacci -----

def test_fibonacci_negative():
    """Negative n should raise ValueError."""
    with pytest.raises(ValueError):
        get_nth_fibonacci(-1)


def test_fibonacci_zero():
    """n=0 should return 0."""
    assert get_nth_fibonacci(0) == 0


def test_fibonacci_one():
    """n=1 should return 1."""
    assert get_nth_fibonacci(1) == 1


def test_fibonacci_large():
    """A larger n should return the correct Fibonacci number."""
    assert get_nth_fibonacci(10) == 55
