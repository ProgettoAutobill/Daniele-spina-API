from pydantic import BaseModel
from typing import List, Optional


class PosConnectResponse(BaseModel):
    status: str
    message: str
    authToken: Optional[str] = None