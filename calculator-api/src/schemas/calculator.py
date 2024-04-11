from pydantic import BaseModel, validator

class CalculatorInput(BaseModel):
    num1: float
    num2: float

    @validator('num2')
    def num2_not_zero(cls, v, values):
        if v == 0 and values.get('operation') == 'divide':
            raise ValueError('num2 cannot be zero for division.')
        return v

class CalculatorOutput(BaseModel):
    result: float
