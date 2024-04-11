from typing import Union

def add(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    return num1 + num2

def subtract(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    return num1 - num2

def multiply(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    return num1 * num2

def divide(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return num1 / num2
