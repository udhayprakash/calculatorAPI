import pytest
from src.core.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("num1, num2, expected", [
    (2, 3, 5),
    (10, 5, 15),
    (-2, 2, 0),
    (0.5, 0.5, 1.0),
])
def test_add(num1, num2, expected):
    assert add(num1, num2) == expected

@pytest.mark.parametrize("num1, num2, expected", [
    (5, 3, 2),
    (10, 5, 5),
    (-2, 2, -4),
    (1.5, 0.5, 1.0),
])
def test_subtract(num1, num2, expected):
    assert subtract(num1, num2) == expected

@pytest.mark.parametrize("num1, num2, expected", [
    (2, 3, 6),
    (10, 5, 50),
    (-2, 2, -4),
    (0.5, 0.5, 0.25),
])
def test_multiply(num1, num2, expected):
    assert multiply(num1, num2) == expected

@pytest.mark.parametrize("num1, num2, expected", [
    (10, 2, 5),
    (10, 5, 2),
    (-10, 2, -5),
    (0.5, 0.25, 2),
])
def test_divide(num1, num2, expected):
    assert divide(num1, num2) == expected

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
