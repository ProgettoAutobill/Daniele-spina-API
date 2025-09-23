from fastapi import APIRouter
from starlette import status

router = APIRouter(
    prefix="/pos",
    tags=["pos"]
)


@router.get("/", status_code=status.HTTP_204_NO_CONTENT)
async def first_pos_api():
    return {"pos": ""}