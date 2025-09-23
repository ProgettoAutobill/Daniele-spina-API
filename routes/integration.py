from fastapi import APIRouter
from starlette import status

router = APIRouter(
    prefix="/integration",
    tags=["integration"]
)


@router.get("/", status_code=status.HTTP_204_NO_CONTENT)
async def first_integration_api():
    return {"integration": ""}