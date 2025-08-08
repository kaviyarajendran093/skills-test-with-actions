import math
import pytest

def area_of_circle(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

def get_nth_fibonacci(n):
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n cannot be negative")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def test_fibonacci_small_numbers():
    assert get_nth_fibonacci(2) == 1
    assert get_nth_fibonacci(3) == 2
    assert get_nth_fibonacci(5) == 5

def test_fibonacci_large_number():
    # 30th Fibonacci number is 832040
    assert get_nth_fibonacci(30) == 832040

def test_fibonacci_non_integer_input():
    with pytest.raises(TypeError):
        get_nth_fibonacci(5.5)

def test_fibonacci_string_input():
    with pytest.raises(TypeError):
        get_nth_fibonacci("10")

def test_area_of_circle_positive():
    assert math.isclose(area_of_circle(1), math.pi)
    assert math.isclose(area_of_circle(0), 0)

def test_area_of_circle_negative():
    with pytest.raises(ValueError):
        area_of_circle(-1)