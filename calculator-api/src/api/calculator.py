from fastapi import APIRouter, Depends
from src.core.operations import add, subtract, multiply, divide
from src.schemas.calculator import CalculatorInput, CalculatorOutput

router = APIRouter()

@router.post("/add", response_model=CalculatorOutput)
def add_numbers(input_data: CalculatorInput = Depends()):
    result = add(input_data.num1, input_data.num2)
    return {"result": result}

@router.post("/subtract", response_model=CalculatorOutput)
def subtract_numbers(input_data: CalculatorInput = Depends()):
    result = subtract(input_data.num1, input_data.num2)
    return {"result": result}

@router.post("/multiply", response_model=CalculatorOutput)
def multiply_numbers(input_data: CalculatorInput = Depends()):
    result = multiply(input_data.num1, input_data.num2)
    return {"result": result}

@router.post("/divide", response_model=CalculatorOutput)
def divide_numbers(input_data: CalculatorInput = Depends(CalculatorInput)):
    result = divide(input_data.num1, input_data.num2)
    return {"result": result}
