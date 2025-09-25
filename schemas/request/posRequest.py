from pydantic import BaseModel
from typing import Literal, Optional, Dict, List, Any


class PosConnectRequest(BaseModel):
    posType: str
    connectionParams: Dict[str, Any]
    storeId: str


class PosProductSyncRequest(BaseModel):
    syncDirection: str
    productCategories: List[str]
