from fastapi import APIRouter
from src.api.calculator import router as calculator_router

router = APIRouter()
router.include_router(calculator_router, prefix="/calculator", tags=["calculator"])
