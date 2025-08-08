import math
import pytest
from src.calculations import area_of_circle, get_nth_fibonacci

def test_area_of_circle_positive():
    assert math.isclose(area_of_circle(1), math.pi)
    assert math.isclose(area_of_circle(0), 0)

def test_area_of_circle_negative():
    with pytest.raises(ValueError):
        area_of_circle(-1)

def test_fibonacci_small_numbers():
    assert get_nth_fibonacci(2) == 1
    assert get_nth_fibonacci(3) == 2
    assert get_nth_fibonacci(5) == 5

def test_fibonacci_large_number():
    assert get_nth_fibonacci(30) == 832040

def test_fibonacci_non_integer_input():
    with pytest.raises(TypeError):
        get_nth_fibonacci(5.5)

def test_fibonacci_string_input():
    with pytest.raises(TypeError):
        get_nth_fibonacci("10")