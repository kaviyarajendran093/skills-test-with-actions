import math
import pytest
from src.calculations import area_of_circle, get_nth_fibonacci

def test_area_of_circle_large_radius():
    large_radius = 1e6
    result = area_of_circle(large_radius)
    expected = math.pi * large_radius**2
    assert math.isclose(result, expected)

def test_area_of_circle_small_radius():
    small_radius = 1e-10
    result = area_of_circle(small_radius)
    expected = math.pi * small_radius**2
    assert math.isclose(result, expected)

def test_area_of_circle_type():
    assert isinstance(area_of_circle(2), float)

def test_get_nth_fibonacci_large_n():
    # 50th Fibonacci number is 12586269025
    assert get_nth_fibonacci(50) == 12586269025

def test_get_nth_fibonacci_non_integer_type_errors():
    with pytest.raises(TypeError):
        get_nth_fibonacci(3.14)
    with pytest.raises(TypeError):
        get_nth_fibonacci("fifteen")
    with pytest.raises(TypeError):
        get_nth_fibonacci(None)

def test_get_nth_fibonacci_output_type():
    assert isinstance(get_nth_fibonacci(10), int)
