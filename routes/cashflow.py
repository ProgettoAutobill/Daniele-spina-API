from fastapi import APIRouter
from starlette import status

router = APIRouter(
    prefix="/cashflow",
    tags=["cashflow"]
)


@router.get("/", status_code=status.HTTP_204_NO_CONTENT)
async def first_cashflow_api():
    return {"cashflow": ""}