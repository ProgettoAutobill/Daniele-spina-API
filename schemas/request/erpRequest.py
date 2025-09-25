from pydantic import BaseModel
from typing import Dict, Any, List


class ErpConnectRequest(BaseModel):
    erpType: str
    connectionParams: Dict[str, Any]
    syncFrequency: str


class ErpSyncRequest(BaseModel):
    syncDirection: str
    dataModules: List[str]


class ErpMappingRequest(BaseModel):
    erpType: str
    entityType: str
    fieldMappings: Dict[str, str]