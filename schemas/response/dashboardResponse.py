from pydantic import BaseModel
from typing import List, Dict, Any


class DashboardUnifiedResponse(BaseModel):
    dataSources: List[str]
    timeframe: str
    viewType: str
    aggregatedData: Dict[str, Any]
    message: str