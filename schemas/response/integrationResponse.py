from pydantic import BaseModel, Field
from typing import List, Optional


class IntegrationCorrelationResult(BaseModel):
    dataSourcePair: str
    correlationScore: float
    insights: List[str]


class IntegrationCorrelationResponse(BaseModel):
    results: List[IntegrationCorrelationResult] = Field(..., alias="results")
    totalPairs: int = Field(..., alias="totalPairs")
    message: str


class IntegrationInventoryImpactEntry(BaseModel):
    category: str
    stockValue: float
    cashFlowImpact: float


class IntegrationInventoryImpactResponse(BaseModel):
    timeframe: int
    totalStockValue: float
    totalCashFlowImpact: float
    details: List[IntegrationInventoryImpactEntry]
    message: str
