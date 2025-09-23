from fastapi import APIRouter
from starlette import status

router = APIRouter(
    prefix="/robot",
    tags=["robot"]
)


@router.get("/", status_code=status.HTTP_204_NO_CONTENT)
async def first_robot_api():
    return {"robot": ""}