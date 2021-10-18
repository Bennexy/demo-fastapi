
import sys
sys.path.append(".")
from fastapi import APIRouter, Form

router = APIRouter(tags=["Calculator"])


@router.post("/add")
async def add(value_1: int = Form(...), value_2: int = Form(...)):
    return value_1 + value_2


@router.post("/multiply")
async def multiply(value_1: int = Form(...), value_2: int = Form(...)):
    return value_1 * value_2



