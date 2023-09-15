from fastapi import APIRouter
from starlette import status
from app.api import schemas
from app.api.utils import form_payload
from datetime import datetime

router = APIRouter(
    prefix="/api",
    tags=["API"],
)


@router.get("/rates", response_model=schemas.CurrencySchema, status_code=status.HTTP_200_OK)
async def convert_currency(value: int, from_c: str, to_c: str):
    res = form_payload(value, from_c, to_c)
    return res
