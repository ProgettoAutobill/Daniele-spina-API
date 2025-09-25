from typing import List
from pydantic import BaseModel, Field
from datetime import date


class CrunchDetectionLiquidityCrisis(BaseModel):
    liquidityCrisis: date = Field(description="Data prevista della crisi di liquidità")
    probability: float = Field(ge=0.0, le=1.0, description="Probabilità stimata")


class CrunchDetectionResponse(BaseModel):
    forecast_horizon: int
    confidence_threshold: float
    crises: List[CrunchDetectionLiquidityCrisis]


class AccountingDataResponse(BaseModel):
    updatedCount: int
    totalAmount: float
    message: str
