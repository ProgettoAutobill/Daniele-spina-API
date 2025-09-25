from pydantic import BaseModel
from typing import Dict, Any


class ErpConnectRequest(BaseModel):
    erpType: str
    connectionParams: Dict[str, Any]
    syncFrequency: str

