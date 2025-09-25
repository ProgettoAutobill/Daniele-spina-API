from pydantic import BaseModel
from typing import Literal, Optional, Dict, List


class IntegrationCorrelationRequest(BaseModel):
    dataSources: List[str]
    correlationType: str