from fastapi import APIRouter
from starlette import status

router = APIRouter(
    prefix="/dashboard",
    tags=["dashboard"]
)


@router.get("/", status_code=status.HTTP_204_NO_CONTENT)
async def first_dashboard_api():
    return {"dashboard": ""}