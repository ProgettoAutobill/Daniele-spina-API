from pydantic import BaseModel
from typing import Dict, Any, List


class ErpConnectRequest(BaseModel):
    erpType: str
    connectionParams: Dict[str, Any]
    syncFrequency: str


class ErpSyncRequest(BaseModel):
    syncDirection: str
    dataModules: List[str]
