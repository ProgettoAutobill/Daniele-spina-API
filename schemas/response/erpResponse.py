from pydantic import BaseModel


class ErpConnectResponse(BaseModel):
    status: str
    message: str
    authToken: str = None